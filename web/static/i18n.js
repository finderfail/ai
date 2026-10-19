const I18N = {
  ru: {
    "meta.title": "Kriloud AI",
    "meta.loginTitle": "Вход · Kriloud AI",
    "sidebar.open": "Открыть меню",
    "sidebar.close": "Закрыть меню",
    "chat.new": "Новый чат",
    "history.label": "История",
    "history.empty": "Здесь появятся ваши чаты",
    "history.delete": "Удалить чат",
    "account.logout": "Выйти",
    "account.login": "Войти",
    "status.checking": "Проверяем модель…",
    "status.ok": "Модель на связи",
    "status.down": "Модель недоступна",
    "status.offline": "Нет связи с сервером",
    "topbar.plans": "Тарифы",
    "hero.title": "Чем могу помочь?",
    "hero.sub": "Отвечаю по своей базе знаний: код, bash и git, математика, платёжные системы и банки",
    "chat.scrollDown": "Вниз",
    "composer.placeholder": "Спросите Kriloud",
    "composer.stop": "Остановить",
    "composer.send": "Отправить",
    "suggest.1.label": "HTTP-сервер на Node.js",
    "suggest.1.text": "Напиши HTTP-сервер на Node.js без фреймворков",
    "suggest.2.label": "Компиляция C в macOS",
    "suggest.2.text": "Как скомпилировать программу на C в macOS?",
    "suggest.3.label": "Отменить коммит в git",
    "suggest.3.text": "Как отменить последний коммит в git?",
    "suggest.4.label": "Производная x² · sin(x)",
    "suggest.4.text": "Найди производную x^2 * sin(x)",
    "dock.note": "Kriloud может ошибаться. Проверяйте важную информацию.",
    "menu.account": "Аккаунт",
    "menu.plans": "Тарифы",
    "menu.close": "Закрыть",
    "tab.plans": "Тарифы",
    "tab.usage": "Использование",
    "tab.language": "Язык",
    "tab.api": "API",
    "menu.settings": "Настройки",
    "model.label": "Модель",
    "api.intro": "API-ключи для плагинов Continue, Cline и других клиентов, совместимых с OpenAI API. Запросы по ключу расходуют суточный лимит вашего тарифа.",
    "api.namePlaceholder": "Название ключа, например «Continue»",
    "api.create": "Создать ключ",
    "api.created": "Ключ создан. Скопируйте его сейчас — больше он показан не будет.",
    "api.empty": "Ключей пока нет",
    "api.lastUsed": "Последнее использование",
    "api.never": "ещё не использовался",
    "api.revoke": "Отозвать",
    "api.revokeConfirm": "Точно отозвать?",
    "api.continueTitle": "Настройка Continue",
    "api.note": "Добавьте этот блок в ~/.continue/config.yaml. Для других плагинов укажите провайдера OpenAI, адрес API (apiBase) и модель flock.",
    "api.loadError": "Не удалось загрузить ключи",
    "plans.note": "Лимит считается по токенам запроса и ответа и обнуляется каждые сутки. Сменить тариф можно через администратора.",
    "plans.unit": "токенов в сутки",
    "plans.current": "Ваш тариф",
    "plans.loadError": "Не удалось загрузить тарифы",
    "plan.desc.free": "Для знакомства: пара десятков вопросов в день.",
    "plan.desc.pro": "Для ежедневной работы с кодом и учёбой.",
    "plan.desc.unlimited": "Без ограничений по токенам.",
    "quota.unlimited": "{used} токенов сегодня · без лимита",
    "quota.limited": "{used} из {limit} токенов сегодня",
    "usage.today": "Сегодня",
    "usage.days": "Последние 14 дней",
    "usage.hintUnlimited": "Тариф {plan}: без лимита",
    "usage.hintExceeded": "Лимит тарифа {plan} исчерпан, обновится завтра",
    "usage.hintRemaining": "Тариф {plan}: осталось {remaining} токенов",
    "usage.empty": "Пока нет запросов",
    "usage.day": "День",
    "usage.requests": "Запросы",
    "usage.tokens": "Токены",
    "usage.loadError": "Не удалось загрузить статистику",
    "language.intro": "Язык интерфейса и ответов Kriloud. Если в сообщении попросить другой язык, ответ будет на нём.",
    "language.label": "Язык",
    "language.loadError": "Не удалось загрузить языки",
    "action.copy": "Копировать",
    "action.copied": "Скопировано",
    "chat.loginRequired": 'Чтобы задать вопрос, <a href="/login">войдите или зарегистрируйтесь</a>.',
    "chat.stopped": "Генерация остановлена",
    "chat.queue": "Модель сейчас занята. Вы в очереди, ваше место: {position}. Пожалуйста, подождите…",
    "chat.serverStatus": "Сервер вернул {status}",
    "chat.connError": "Ошибка соединения",
    "auth.loginTitle": "Вход в Kriloud",
    "auth.loginSub": "Войдите, чтобы продолжить",
    "auth.registerTitle": "Регистрация",
    "auth.registerSub": "Нужны только почта и пароль",
    "auth.tabLogin": "Вход",
    "auth.tabRegister": "Регистрация",
    "auth.email": "Почта",
    "auth.password": "Пароль",
    "auth.passwordHint": "Не короче 8 символов",
    "auth.submitLogin": "Войти",
    "auth.submitRegister": "Создать аккаунт",
    "auth.planNote": "Новый аккаунт получает тариф Free — 10 000 токенов в сутки.",
    "auth.back": "Вернуться в чат",
    "auth.requestFailed": "Не удалось выполнить запрос",
    "auth.connError": "Ошибка соединения с сервером"
  },
  ja: {
    "meta.title": "Kriloud AI",
    "meta.loginTitle": "ログイン · Kriloud AI",
    "sidebar.open": "メニューを開く",
    "sidebar.close": "メニューを閉じる",
    "chat.new": "新しいチャット",
    "history.label": "履歴",
    "history.empty": "チャット履歴がここに表示されます",
    "history.delete": "チャットを削除",
    "account.logout": "ログアウト",
    "account.login": "ログイン",
    "status.checking": "モデルを確認中…",
    "status.ok": "モデル接続中",
    "status.down": "モデルに接続できません",
    "status.offline": "サーバーに接続できません",
    "topbar.plans": "プラン",
    "hero.title": "何かお手伝いできますか？",
    "hero.sub": "コード、bash と git、数学、決済ブランドと銀行についてナレッジベースをもとに回答します",
    "chat.scrollDown": "下へ",
    "composer.placeholder": "Kriloudに質問する",
    "composer.stop": "停止",
    "composer.send": "送信",
    "suggest.1.label": "Node.jsでHTTPサーバー",
    "suggest.1.text": "フレームワークを使わずにNode.jsでHTTPサーバーを書いて",
    "suggest.2.label": "macOSでCをコンパイル",
    "suggest.2.text": "macOSでCのプログラムをコンパイルするには？",
    "suggest.3.label": "git のコミットを取り消す",
    "suggest.3.text": "git で直前のコミットを取り消すには？",
    "suggest.4.label": "x² · sin(x) の導関数",
    "suggest.4.text": "x^2 * sin(x) の導関数を求めて",
    "dock.note": "Kriloudは間違えることがあります。重要な情報は確認してください。",
    "menu.account": "アカウント",
    "menu.plans": "プラン",
    "menu.close": "閉じる",
    "tab.plans": "プラン",
    "tab.usage": "使用状況",
    "tab.language": "言語",
    "tab.api": "API",
    "menu.settings": "設定",
    "model.label": "モデル",
    "api.intro": "Continue、Cline など OpenAI API 互換クライアント用の API キーです。キーによるリクエストはプランの1日の上限を消費します。",
    "api.namePlaceholder": "キーの名前（例：Continue）",
    "api.create": "キーを作成",
    "api.created": "キーを作成しました。今すぐコピーしてください。再表示はされません。",
    "api.empty": "キーはまだありません",
    "api.lastUsed": "最終使用",
    "api.never": "未使用",
    "api.revoke": "取り消す",
    "api.revokeConfirm": "本当に取り消しますか？",
    "api.continueTitle": "Continue の設定",
    "api.note": "このブロックを ~/.continue/config.yaml に追加してください。他のプラグインでは、プロバイダーに OpenAI、API アドレス（apiBase）、モデルに flock を指定します。",
    "api.loadError": "キーを読み込めませんでした",
    "plans.note": "上限はリクエストと応答のトークン数で計算され、毎日リセットされます。プランの変更は管理者にお問い合わせください。",
    "plans.unit": "トークン／日",
    "plans.current": "現在のプラン",
    "plans.loadError": "プランを読み込めませんでした",
    "plan.desc.free": "お試し用：1日に数十件の質問ができます。",
    "plan.desc.pro": "コードや学習に毎日使う方向け。",
    "plan.desc.unlimited": "トークン数の制限なし。",
    "quota.unlimited": "今日 {used} トークン・無制限",
    "quota.limited": "今日 {used} / {limit} トークン",
    "usage.today": "今日",
    "usage.days": "過去14日間",
    "usage.hintUnlimited": "{plan}プラン：無制限",
    "usage.hintExceeded": "{plan}プランの上限に達しました。明日リセットされます",
    "usage.hintRemaining": "{plan}プラン：残り {remaining} トークン",
    "usage.empty": "まだリクエストはありません",
    "usage.day": "日付",
    "usage.requests": "リクエスト",
    "usage.tokens": "トークン",
    "usage.loadError": "統計を読み込めませんでした",
    "language.intro": "インターフェースとKriloudの回答の言語です。メッセージで別の言語を指定すると、その言語で回答します。",
    "language.label": "言語",
    "language.loadError": "言語を読み込めませんでした",
    "action.copy": "コピー",
    "action.copied": "コピーしました",
    "chat.loginRequired": '質問するには<a href="/login">ログインまたは新規登録</a>してください。',
    "chat.stopped": "生成を停止しました",
    "chat.queue": "モデルは現在混み合っています。順番待ち中です。あなたの順番：{position} 番目。しばらくお待ちください…",
    "chat.serverStatus": "サーバーがエラー {status} を返しました",
    "chat.connError": "接続エラー",
    "auth.loginTitle": "Kriloudにログイン",
    "auth.loginSub": "続行するにはログインしてください",
    "auth.registerTitle": "新規登録",
    "auth.registerSub": "メールアドレスとパスワードだけで登録できます",
    "auth.tabLogin": "ログイン",
    "auth.tabRegister": "新規登録",
    "auth.email": "メールアドレス",
    "auth.password": "パスワード",
    "auth.passwordHint": "8文字以上",
    "auth.submitLogin": "ログイン",
    "auth.submitRegister": "アカウントを作成",
    "auth.planNote": "新規アカウントにはFreeプラン（1日10,000トークン）が適用されます。",
    "auth.back": "チャットに戻る",
    "auth.requestFailed": "リクエストを実行できませんでした",
    "auth.connError": "サーバーへの接続エラー"
  }
};

const LANG_STORAGE_KEY = "kriloud.lang";
const LANG_LOCALES = { ru: "ru-RU", ja: "ja-JP" };

function detectLang() {
  try {
    const stored = localStorage.getItem(LANG_STORAGE_KEY);
    if (stored && I18N[stored]) return stored;
  } catch (_) {
    return "ru";
  }
  return (navigator.language || "").toLowerCase().startsWith("ja") ? "ja" : "ru";
}

let currentLang = detectLang();

function t(key, params) {
  const dict = I18N[currentLang] || I18N.ru;
  let text = dict[key] !== undefined ? dict[key] : I18N.ru[key] !== undefined ? I18N.ru[key] : key;
  if (params) {
    Object.keys(params).forEach((name) => {
      text = text.split(`{${name}}`).join(String(params[name]));
    });
  }
  return text;
}

function langLocale() {
  return LANG_LOCALES[currentLang] || LANG_LOCALES.ru;
}

function langHeaders(extra) {
  return Object.assign({ "X-Lang": currentLang }, extra || {});
}

function applyI18n(root) {
  const scope = root || document;
  scope.querySelectorAll("[data-i18n]").forEach((el) => {
    el.textContent = t(el.dataset.i18n);
  });
  scope.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    el.placeholder = t(el.dataset.i18nPlaceholder);
  });
  scope.querySelectorAll("[data-i18n-aria]").forEach((el) => {
    el.setAttribute("aria-label", t(el.dataset.i18nAria));
  });
  scope.querySelectorAll("[data-i18n-title]").forEach((el) => {
    el.title = t(el.dataset.i18nTitle);
  });
  scope.querySelectorAll("[data-i18n-text]").forEach((el) => {
    el.dataset.text = t(el.dataset.i18nText);
  });
  document.documentElement.lang = currentLang;
}

function setLang(lang) {
  if (!I18N[lang]) return;
  currentLang = lang;
  try {
    localStorage.setItem(LANG_STORAGE_KEY, lang);
  } catch (_) {
    currentLang = lang;
  }
  applyI18n();
}
