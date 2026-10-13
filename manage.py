#!/usr/bin/env python3

from __future__ import annotations

import sys

from web import accounts, db, geo, sanctions


def usage() -> None:
    plans = "|".join(accounts.PLANS)
    print("Управление аккаунтами Kriloud AI\n")
    print(f"  python manage.py register <email> <пароль> [{plans}]")
    print(f"  python manage.py plan <email> <{plans}>")
    print("  python manage.py governance <email> on|off")
    print("  python manage.py list")
    print()
    print("  python manage.py sanction <email> [причина] [примечание]")
    print("  python manage.py unsanction <email>")
    print("  python manage.py sanction-domain <домен> [причина] [примечание]")
    print("  python manage.py unsanction-domain <домен>")
    print("  python manage.py sanctions")
    print()
    print("  Причины: " + ", ".join(sanctions.REASONS))
    print()
    print("  python manage.py geo                         статус вайтлиста стран")
    print("  python manage.py geo-allow <RU> [JP ...]     разрешить страны (коды ISO 3166-1)")
    print("  python manage.py geo-remove <RU> [JP ...]    убрать страны из списка")
    print("  python manage.py geo-on | geo-off            включить или выключить геоблок")
    print("  python manage.py geo-unknown allow|deny      что делать, если страна не определена")


def format_limit(limit: int | None) -> str:
    return "без лимита" if limit is None else f"{limit:,}".replace(",", " ")


def cmd_register(args: list[str]) -> None:
    plan = args[2] if len(args) > 2 else accounts.DEFAULT_PLAN
    user = accounts.register(args[0], args[1], plan=plan)
    print(f"Создан {user.email}, тариф {user.plan_label} ({format_limit(user.daily_limit)} токенов в сутки)")


def cmd_plan(args: list[str]) -> None:
    user = accounts.set_plan(args[0], args[1])
    print(f"{user.email}: тариф {user.plan_label} ({format_limit(user.daily_limit)} токенов в сутки)")


def cmd_governance(args: list[str]) -> None:
    if args[1] not in ("on", "off"):
        raise SystemExit("Укажите on или off")
    user = accounts.set_governance(args[0], args[1] == "on")
    state = "выдан" if user.governance else "снят"
    print(f"{user.email}: статус Governance {state}")


def cmd_list(_: list[str]) -> None:
    users = accounts.list_users()
    if not users:
        print("Пользователей нет")
        return
    for user in users:
        used = accounts.tokens_used_today(user.id)
        print(
            f"  {user.id:>3}  {user.email:<32} {user.plan_label:<10} "
            f"{'Governance' if user.governance else '':<11}"
            f"сегодня: {used:>9} / {format_limit(user.daily_limit)}"
        )


def cmd_sanction(args: list[str]) -> None:
    reason = args[1] if len(args) > 1 else "USER_SANCTIONED"
    note = " ".join(args[2:])
    entry = sanctions.block_email(args[0], reason, note)
    exists = accounts.get_user_by_email(entry["email"]) is not None
    suffix = "" if exists else " (аккаунта с такой почтой пока нет — блокировка сработает при регистрации)"
    print(f"{entry['email']}: заблокирован, причина {entry['reason']}{suffix}")


def cmd_unsanction(args: list[str]) -> None:
    if sanctions.unblock_email(args[0]):
        print(f"{args[0].strip().lower()}: блокировка снята")
    else:
        print(f"{args[0].strip().lower()}: в списке санкций не найден")


def cmd_sanction_domain(args: list[str]) -> None:
    reason = args[1] if len(args) > 1 else "COMPANY_SANCTIONED"
    note = " ".join(args[2:])
    entry = sanctions.block_domain(args[0], reason, note)
    print(f"@{entry['domain']}: все адреса домена заблокированы, причина {entry['reason']}")


def cmd_unsanction_domain(args: list[str]) -> None:
    if sanctions.unblock_domain(args[0]):
        print(f"@{args[0].strip().lower()}: блокировка домена снята")
    else:
        print(f"@{args[0].strip().lower()}: домен в списке санкций не найден")


def cmd_sanctions(_: list[str]) -> None:
    data = sanctions.listing()
    if not data["enabled"]:
        print("Проверка санкций выключена (enabled: false в data/sanctions.json)")
    print("Почта:")
    for entry in data["emails"] or [{"email": "—", "reason": "", "since": "", "note": ""}]:
        print(f"  {entry.get('email', ''):<32} {entry.get('reason', ''):<20} {entry.get('since', ''):<11} {entry.get('note', '')}")
    print("Домены:")
    for entry in data["domains"] or [{"domain": "—", "reason": "", "since": "", "note": ""}]:
        print(f"  @{entry.get('domain', ''):<31} {entry.get('reason', ''):<20} {entry.get('since', ''):<11} {entry.get('note', '')}")


def _codes(args: list[str]) -> list[str]:
    codes = [a.strip().upper() for a in args if a.strip()]
    bad = [c for c in codes if len(c) != 2 or not c.isalpha()]
    if bad:
        raise ValueError(f"Нужны двухбуквенные коды стран ISO 3166-1: {', '.join(bad)}")
    return codes


def cmd_geo(_: list[str]) -> None:
    data = geo.load()
    state = "ВКЛЮЧЁН" if data["enabled"] else "выключен"
    print(f"Геоблок: {state}")
    print(f"Разрешённые страны: {', '.join(data['allowed']) or '— (список пуст)'}")
    print(f"Страна не определена: {'пускать' if data['unknown'] == 'allow' else 'блокировать'}")
    print(f"Источник страны: заголовок {geo.COUNTRY_HEADER}")
    if data["enabled"] and not data["allowed"]:
        print("Внимание: список пуст — сайт закрыт для всех, кроме локальных запросов.")


def cmd_geo_allow(args: list[str]) -> None:
    data = dict(geo.load())
    data["allowed"] = sorted(set(data["allowed"]) | set(_codes(args)))
    geo.save(data)
    print(f"Разрешённые страны: {', '.join(data['allowed'])}")


def cmd_geo_remove(args: list[str]) -> None:
    data = dict(geo.load())
    data["allowed"] = sorted(set(data["allowed"]) - set(_codes(args)))
    geo.save(data)
    print(f"Разрешённые страны: {', '.join(data['allowed']) or '— (список пуст)'}")


def cmd_geo_switch(enabled: bool):
    def handler(_: list[str]) -> None:
        data = dict(geo.load())
        data["enabled"] = enabled
        geo.save(data)
        cmd_geo([])

    return handler


def cmd_geo_unknown(args: list[str]) -> None:
    if args[0] not in ("allow", "deny"):
        raise ValueError("Укажите allow или deny")
    data = dict(geo.load())
    data["unknown"] = args[0]
    geo.save(data)
    cmd_geo([])


COMMANDS = {
    "register": (cmd_register, 2),
    "plan": (cmd_plan, 2),
    "governance": (cmd_governance, 2),
    "list": (cmd_list, 0),
    "sanction": (cmd_sanction, 1),
    "unsanction": (cmd_unsanction, 1),
    "sanction-domain": (cmd_sanction_domain, 1),
    "unsanction-domain": (cmd_unsanction_domain, 1),
    "sanctions": (cmd_sanctions, 0),
    "geo": (cmd_geo, 0),
    "geo-allow": (cmd_geo_allow, 1),
    "geo-remove": (cmd_geo_remove, 1),
    "geo-on": (cmd_geo_switch(True), 0),
    "geo-off": (cmd_geo_switch(False), 0),
    "geo-unknown": (cmd_geo_unknown, 1),
}


def main() -> None:
    db.init_db()
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        usage()
        raise SystemExit(1)

    handler, min_args = COMMANDS[sys.argv[1]]
    args = sys.argv[2:]
    if len(args) < min_args:
        usage()
        raise SystemExit(1)

    try:
        handler(args)
    except (accounts.AccountError, ValueError) as exc:
        print(f"Ошибка: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
