from __future__ import annotations

import ast
import re
from fractions import Fraction

EXPRESSION_RE = re.compile(r"[\d(][\d\s.,+\-*/×÷:^()]*[\d)]")
OPERATOR_RE = re.compile(r"\d\s*[)]*\s*[+\-*/×÷:^]\s*[(]*\s*-?\d")
TRIGGER_RE = re.compile(
    r"=|сколько будет|посчитай|вычисли|реши пример|calculate|compute|what is|計算|いくつ|答え",
    re.IGNORECASE,
)
MAX_POWER = 64
MAX_DIGITS = 200

SYMBOLS = {ast.Add: "+", ast.Sub: "−", ast.Mult: "×", ast.Div: "÷", ast.Pow: "^"}

TEXTS = {
    "ru": {
        "steps": "По порядку действий: сначала скобки, затем степени, потом умножение и деление, потом сложение и вычитание (слева направо).",
        "answer": "Ответ",
        "div_zero": "Деление на ноль: у этого выражения нет значения.",
    },
    "ja": {
        "steps": "計算の順序：かっこ、累乗、掛け算と割り算、足し算と引き算（左から右へ）。",
        "answer": "答え",
        "div_zero": "0 で割っているため、この式には値がありません。",
    },
}


class CalcError(Exception):
    pass


def _fmt(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    decimal = f"{float(value):.10f}".rstrip("0").rstrip(".")
    exact = Fraction(decimal) == value
    return decimal if exact else f"{value.numerator}/{value.denominator} ≈ {float(value):.6g}"


def _eval(node: ast.AST, steps: list[str]) -> Fraction:
    if isinstance(node, ast.Expression):
        return _eval(node.body, steps)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return Fraction(str(node.value))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        value = _eval(node.operand, steps)
        return -value if isinstance(node.op, ast.USub) else value
    if isinstance(node, ast.BinOp) and type(node.op) in SYMBOLS:
        left = _eval(node.left, steps)
        right = _eval(node.right, steps)
        op = type(node.op)
        if op is ast.Add:
            result = left + right
        elif op is ast.Sub:
            result = left - right
        elif op is ast.Mult:
            result = left * right
        elif op is ast.Div:
            if right == 0:
                raise ZeroDivisionError
            result = left / right
        else:
            if right.denominator != 1 or abs(right) > MAX_POWER:
                raise CalcError("unsupported power")
            result = left ** int(right)
        if len(str(result.numerator)) > MAX_DIGITS:
            raise CalcError("too large")
        steps.append(f"{_fmt(left)} {SYMBOLS[op]} {_fmt(right)} = {_fmt(result)}")
        return result
    raise CalcError("unsupported expression")


def _normalize(expr: str) -> str:
    expr = expr.replace("×", "*").replace("÷", "/").replace(":", "/").replace("^", "**")
    expr = re.sub(r"(?<=\d),(?=\d)", ".", expr)
    return expr


def find_expression(text: str) -> str | None:
    candidates = [m.group(0).strip() for m in EXPRESSION_RE.finditer(text)]
    candidates = [c for c in candidates if OPERATOR_RE.search(c)]
    if not candidates:
        return None
    expr = max(candidates, key=len)
    rest = re.sub(r"[\s=?？!.,]", "", text.replace(expr, ""))
    if TRIGGER_RE.search(text) or len(rest) <= len(re.sub(r"\s", "", expr)) * 0.5:
        return expr
    return None


def answer(text: str, language: str = "ru") -> str | None:
    expr = find_expression(text)
    if expr is None:
        return None
    texts = TEXTS.get(language, TEXTS["ru"])
    try:
        tree = ast.parse(_normalize(expr), mode="eval")
    except SyntaxError:
        return None
    steps: list[str] = []
    try:
        result = _eval(tree, steps)
    except ZeroDivisionError:
        return f"{expr} — {texts['div_zero']}"
    except CalcError:
        return None
    if not steps:
        return None
    lines = [f"**{expr} = {_fmt(result)}**", "", texts["steps"], ""]
    lines += [f"{i}. {step}" for i, step in enumerate(steps, 1)]
    lines += ["", f"{texts['answer']}: **{_fmt(result)}**"]
    return "\n".join(lines)
