from __future__ import annotations

import re

PER_USD = {
    "USD": 1.0,
    "BYN": 3.2,
    "RUB": 90.0,
    "UAH": 41.0,
    "UZS": 12800.0,
    "KZT": 520.0,
    "EUR": 0.92,
    "ILS": 3.7,
    "CAD": 1.37,
}

LINKS = {
    "BYN": "https://www.nbrb.by/statistics/rates/ratesdaily",
    "RUB": "https://www.nbrb.by/statistics/rates/ratesdaily",
    "UAH": "https://bank.gov.ua/ua/markets/exchangerates",
    "KZT": "https://www.nationalbank.kz/ru/exchangerates",
    "UZS": "https://cbu.uz/ru/arkhiv-kursov-valyut/",
    "USD": "https://www.federalreserve.gov/releases/h10/",
    "EUR": "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html",
    "ILS": "https://www.boi.org.il/en/markets/exchangerates/",
    "CAD": "https://www.bankofcanada.ca/rates/exchange/",
}

NAMES = {
    "BYN": "белорусских рублей",
    "RUB": "российских рублей",
    "UAH": "гривен",
    "UZS": "узбекских сумов",
    "KZT": "тенге",
    "USD": "долларов США",
    "EUR": "евро",
    "ILS": "шекелей",
    "CAD": "канадских долларов",
}

NAMES_JA = {
    "BYN": "ベラルーシ・ルーブル",
    "RUB": "ロシア・ルーブル",
    "UAH": "ウクライナ・フリヴニャ",
    "UZS": "ウズベキスタン・スム",
    "KZT": "カザフスタン・テンゲ",
    "USD": "米ドル",
    "EUR": "ユーロ",
    "ILS": "イスラエル・シェケル",
    "CAD": "カナダ・ドル",
}

ALIASES = [
    ("BYN", ("byn", "белорусск", "бел.руб", "бел руб", "бун")),
    ("KZT", ("kzt", "тенге", "тнг")),
    ("UAH", ("uah", "гривн", "грн", "гривен")),
    ("UZS", ("uzs", "сум", "сумов")),
    ("EUR", ("eur", "евро", "€")),
    ("ILS", ("ils", "шекел", "шекель", "₪")),
    ("CAD", ("cad", "канадск")),
    ("USD", ("usd", "доллар", "бакс", "$", "долл")),
    ("RUB", ("rub", "рубл", "руб", "российск", "₽")),
]

AMOUNT_RE = re.compile(r"(\d[\d\s]*(?:[.,]\d+)?)")


def _find_currencies(text: str) -> list[str]:
    lowered = text.lower()
    found: list[tuple[int, str]] = []
    for code, aliases in ALIASES:
        best = None
        for alias in aliases:
            position = lowered.find(alias)
            if position != -1 and (best is None or position < best):
                best = position
        if best is not None:
            found.append((best, code))
    found.sort()
    ordered: list[str] = []
    for _, code in found:
        if code not in ordered:
            ordered.append(code)
    return ordered


def _parse_amount(text: str) -> float | None:
    match = AMOUNT_RE.search(text)
    if not match:
        return None
    raw = match.group(1).replace(" ", "").replace(",", ".")
    try:
        return float(raw)
    except ValueError:
        return None


def _format_amount(value: float) -> str:
    if value >= 1000:
        rounded = round(value)
        return f"{rounded:,}".replace(",", " ")
    if value >= 10:
        return f"{value:.0f}"
    if value >= 1:
        return f"{value:.2f}".rstrip("0").rstrip(".")
    return f"{value:.4f}".rstrip("0").rstrip(".")


def parse_conversion(text: str) -> tuple[float, str, str] | None:
    codes = _find_currencies(text)
    if len(codes) < 2:
        return None
    amount = _parse_amount(text)
    if amount is None:
        return None
    return amount, codes[0], codes[1]


def convert(amount: float, source: str, target: str) -> float:
    usd = amount / PER_USD[source]
    return usd * PER_USD[target]


def answer(text: str, language: str = "ru") -> str | None:
    parsed = parse_conversion(text)
    if parsed is None:
        return None

    amount, source, target = parsed
    if source == target:
        return None

    result = convert(amount, source, target)
    rate = convert(1.0, source, target)

    if language == "ja":
        return (
            f"{_format_amount(amount)} {source} ≈ {_format_amount(result)} {target} "
            f"（{NAMES_JA[target]}）。\n\n"
            f"目安レート 1 {source} ≈ {_format_amount(rate)} {target} で計算しています。"
            f"レートはおおよその値で毎日変動します。最新のレートはこちら: "
            f"{LINKS[target]}"
        )

    return (
        f"{_format_amount(amount)} {source} ≈ {_format_amount(result)} {target} "
        f"({NAMES[target]}).\n\n"
        f"Расчёт по ориентировочному курсу 1 {source} ≈ {_format_amount(rate)} {target}. "
        f"Курс приблизительный и меняется ежедневно — актуальный смотрите здесь: "
        f"{LINKS[target]}"
    )
