from __future__ import annotations

from rag import config

MESSAGES = {
    "invalid_email": {
        "ru": "Некорректный email",
        "ja": "メールアドレスが正しくありません",
    },
    "short_password": {
        "ru": "Пароль должен быть не короче 8 символов",
        "ja": "パスワードは8文字以上にしてください",
    },
    "unknown_plan": {
        "ru": "Тариф должен быть одним из: {plans}",
        "ja": "プランは次のいずれかにしてください: {plans}",
    },
    "email_taken": {
        "ru": "Пользователь с таким email уже существует",
        "ja": "このメールアドレスは既に登録されています",
    },
    "bad_credentials": {
        "ru": "Неверный email или пароль",
        "ja": "メールアドレスまたはパスワードが正しくありません",
    },
    "user_not_found": {
        "ru": "Пользователь не найден",
        "ja": "ユーザーが見つかりません",
    },
    "unknown_language": {
        "ru": "Язык должен быть одним из: {languages}",
        "ja": "言語は次のいずれかにしてください: {languages}",
    },
    "unknown_model": {
        "ru": "Эта модель недоступна",
        "ja": "このモデルは利用できません",
    },
    "key_limit": {
        "ru": "Можно создать не больше {limit} ключей. Удалите ненужный ключ",
        "ja": "作成できるキーは最大{limit}個です。不要なキーを削除してください",
    },
    "key_not_found": {
        "ru": "Ключ не найден",
        "ja": "キーが見つかりません",
    },
    "invalid_key": {
        "ru": "Неверный или отозванный API-ключ",
        "ja": "API キーが無効か、取り消されています",
    },
    "model_not_found": {
        "ru": "Модель {model} не найдена",
        "ja": "モデル {model} が見つかりません",
    },
    "login_required": {
        "ru": "Войдите в аккаунт, чтобы продолжить",
        "ja": "続行するにはログインしてください",
    },
    "quota_exceeded": {
        "ru": "Дневной лимит тарифа {plan} исчерпан: {used} из {limit} токенов. Лимит обновится завтра.",
        "ja": "{plan}プランの1日の上限に達しました: {limit}トークン中{used}トークン使用。上限は明日リセットされます。",
    },
    "model_timeout": {
        "ru": "Сервер модели не ответил вовремя. Попробуйте повторить запрос или задать вопрос покороче.",
        "ja": "モデルサーバーが時間内に応答しませんでした。もう一度試すか、質問を短くしてください。",
    },
    "model_error": {
        "ru": "Не удалось получить ответ от сервера модели: {error}",
        "ja": "モデルサーバーから応答を取得できませんでした: {error}",
    },
    "sanction.USER_SANCTIONED": {
        "ru": "Аккаунт заблокирован: санкции на пользователя",
        "ja": "アカウントはブロックされています: ユーザーへの制裁",
    },
    "sanction.COMPANY_SANCTIONED": {
        "ru": "Аккаунт заблокирован: санкции на организацию",
        "ja": "アカウントはブロックされています: 組織への制裁",
    },
    "sanction.SANCTIONED_COUNTRY": {
        "ru": "Доступ закрыт: пользователь из санкционной страны",
        "ja": "アクセスできません: 制裁対象国のユーザーです",
    },
    "sanction.ABUSE_DETECTED": {
        "ru": "Доступ приостановлен: зафиксировано злоупотребление",
        "ja": "アクセスは停止されています: 不正利用が検出されました",
    },
    "sanction.PAYMENT_FRAUD": {
        "ru": "Доступ приостановлен: подозрение на мошенничество с оплатой",
        "ja": "アクセスは停止されています: 支払い詐欺の疑いがあります",
    },
    "sanction.MANUAL_REVIEW": {
        "ru": "Доступ приостановлен: аккаунт на ручной проверке",
        "ja": "アクセスは停止されています: アカウントは手動審査中です",
    },
    "sanction.default": {
        "ru": "Доступ к сервису ограничен",
        "ja": "サービスへのアクセスは制限されています",
    },
}


def resolve(language: str | None) -> str:
    return language if language in config.LANGUAGES else config.DEFAULT_LANGUAGE


def text(key: str, language: str | None = None, **params) -> str:
    entry = MESSAGES.get(key, MESSAGES["sanction.default"])
    template = entry.get(resolve(language), entry[config.DEFAULT_LANGUAGE])
    return template.format(**params)
