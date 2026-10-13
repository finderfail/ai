const tabsEl = document.getElementById("tabs");
const formEl = document.getElementById("authForm");
const emailEl = document.getElementById("email");
const passwordEl = document.getElementById("password");
const submitEl = document.getElementById("submitBtn");
const errorEl = document.getElementById("formError");
const titleEl = document.getElementById("authTitle");
const subEl = document.getElementById("authSub");
const hintEl = document.getElementById("passwordHint");
const planNoteEl = document.getElementById("planNote");
const langSwitchEl = document.getElementById("langSwitch");

let mode = "login";

function renderMode() {
  const isLogin = mode === "login";
  tabsEl.querySelectorAll(".segment").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.tab === mode);
  });
  titleEl.textContent = t(isLogin ? "auth.loginTitle" : "auth.registerTitle");
  subEl.textContent = t(isLogin ? "auth.loginSub" : "auth.registerSub");
  submitEl.textContent = t(isLogin ? "auth.submitLogin" : "auth.submitRegister");
  passwordEl.autocomplete = isLogin ? "current-password" : "new-password";
  hintEl.hidden = isLogin;
  planNoteEl.hidden = isLogin;
}

function setMode(next) {
  mode = next;
  errorEl.hidden = true;
  renderMode();
}

function renderLangSwitch() {
  langSwitchEl.querySelectorAll(".auth-lang").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.lang === currentLang);
  });
}

tabsEl.addEventListener("click", (e) => {
  const btn = e.target.closest(".segment");
  if (btn) setMode(btn.dataset.tab);
});

langSwitchEl.addEventListener("click", (e) => {
  const btn = e.target.closest(".auth-lang");
  if (!btn) return;
  setLang(btn.dataset.lang);
  renderMode();
  renderLangSwitch();
});

function showError(text) {
  errorEl.textContent = text;
  errorEl.hidden = false;
}

formEl.addEventListener("submit", async (e) => {
  e.preventDefault();
  errorEl.hidden = true;
  submitEl.disabled = true;

  const endpoint = mode === "login" ? "/api/auth/login" : "/api/auth/register";

  try {
    const resp = await fetch(endpoint, {
      method: "POST",
      headers: langHeaders({ "Content-Type": "application/json" }),
      body: JSON.stringify({ email: emailEl.value.trim(), password: passwordEl.value })
    });

    const data = await resp.json();
    if (!resp.ok) {
      showError(typeof data.detail === "string" ? data.detail : t("auth.requestFailed"));
      return;
    }

    if (data.language) setLang(data.language);
    window.location.href = "/";
  } catch (_) {
    showError(t("auth.connError"));
  } finally {
    submitEl.disabled = false;
  }
});

if (window.location.hash === "#register") mode = "register";

applyI18n();
renderMode();
renderLangSwitch();

fetch("/api/auth/me", { headers: langHeaders() })
  .then((r) => r.json())
  .then((data) => {
    if (data.authenticated) window.location.href = "/";
  })
  .catch(() => {});

if ("serviceWorker" in navigator && window.isSecureContext) {
  navigator.serviceWorker.register("/sw.js").catch(() => {});
}
