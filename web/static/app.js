const MATH_SYMBOLS = {
  "\\varepsilon": "ε",
  "\\rightarrow": "→",
  "\\leftarrow": "←",
  "\\Rightarrow": "⇒",
  "\\Leftarrow": "⇐",
  "\\subseteq": "⊆",
  "\\emptyset": "∅",
  "\\partial": "∂",
  "\\infty": "∞",
  "\\propto": "∝",
  "\\approx": "≈",
  "\\equiv": "≡",
  "\\forall": "∀",
  "\\exists": "∃",
  "\\notin": "∉",
  "\\subset": "⊂",
  "\\varphi": "φ",
  "\\lambda": "λ",
  "\\epsilon": "ε",
  "\\Lambda": "Λ",
  "\\Gamma": "Γ",
  "\\Delta": "Δ",
  "\\Theta": "Θ",
  "\\Sigma": "Σ",
  "\\Omega": "Ω",
  "\\alpha": "α",
  "\\beta": "β",
  "\\gamma": "γ",
  "\\delta": "δ",
  "\\theta": "θ",
  "\\sigma": "σ",
  "\\omega": "ω",
  "\\nabla": "∇",
  "\\ldots": "…",
  "\\cdots": "⋯",
  "\\times": "×",
  "\\cdot": "·",
  "\\dots": "…",
  "\\zeta": "ζ",
  "\\iint": "∬",
  "\\oint": "∮",
  "\\prod": "∏",
  "\\sqrt": "√",
  "\\lneq": "≤",
  "\\gamma": "γ",
  "\\Phi": "Φ",
  "\\Psi": "Ψ",
  "\\Xi": "Ξ",
  "\\Pi": "Π",
  "\\phi": "φ",
  "\\psi": "ψ",
  "\\chi": "χ",
  "\\tau": "τ",
  "\\rho": "ρ",
  "\\eta": "η",
  "\\div": "÷",
  "\\neq": "≠",
  "\\leq": "≤",
  "\\geq": "≥",
  "\\sim": "∼",
  "\\cup": "∪",
  "\\cap": "∩",
  "\\int": "∫",
  "\\sum": "∑",
  "\\log": "log",
  "\\sin": "sin",
  "\\cos": "cos",
  "\\tan": "tan",
  "\\cot": "cot",
  "\\arcsin": "arcsin",
  "\\arctan": "arctan",
  "\\lim": "lim",
  "\\ln": "ln",
  "\\max": "max",
  "\\min": "min",
  "\\mu": "μ",
  "\\nu": "ν",
  "\\xi": "ξ",
  "\\pi": "π",
  "\\pm": "±",
  "\\mp": "∓",
  "\\to": "→",
  "\\in": "∈",
  "\\le": "≤",
  "\\ge": "≥",
  "\\ne": "≠"
};

const MATH_KEYS = Object.keys(MATH_SYMBOLS).sort((a, b) => b.length - a.length);

function replaceBracedCommand(text, command, formatter) {
  const marker = `\\${command}{`;
  let out = text;
  let guard = 0;
  while (out.includes(marker) && guard < 40) {
    guard += 1;
    const start = out.indexOf(marker);
    let i = start + marker.length;
    let depth = 1;
    let first = "";
    while (i < out.length && depth > 0) {
      const ch = out[i];
      if (ch === "{") depth += 1;
      else if (ch === "}") depth -= 1;
      if (depth > 0) first += ch;
      i += 1;
    }
    let second = null;
    if (out[i] === "{") {
      i += 1;
      depth = 1;
      second = "";
      while (i < out.length && depth > 0) {
        const ch = out[i];
        if (ch === "{") depth += 1;
        else if (ch === "}") depth -= 1;
        if (depth > 0) second += ch;
        i += 1;
      }
    }
    out = out.slice(0, start) + formatter(first, second) + out.slice(i);
  }
  return out;
}

function isBalancedWrapped(value) {
  if (!value.startsWith("(") || !value.endsWith(")")) return false;
  let depth = 0;
  for (let i = 0; i < value.length; i += 1) {
    if (value[i] === "(") depth += 1;
    else if (value[i] === ")") {
      depth -= 1;
      if (depth === 0 && i !== value.length - 1) return false;
    }
  }
  return depth === 0;
}

function wrapIfCompound(value) {
  const trimmed = value.trim();
  if (/^[A-Za-zА-Яа-я0-9αβγδθπσωμνξρτφψ²³]+$/.test(trimmed)) return trimmed;
  if (isBalancedWrapped(trimmed)) return trimmed;
  return `(${trimmed})`;
}

function normalizeMath(text) {
  let out = text;

  out = replaceBracedCommand(out, "frac", (a, b) =>
    b === null ? wrapIfCompound(a) : `${wrapIfCompound(a)}/${wrapIfCompound(b)}`
  );
  out = replaceBracedCommand(out, "dfrac", (a, b) =>
    b === null ? wrapIfCompound(a) : `${wrapIfCompound(a)}/${wrapIfCompound(b)}`
  );
  out = replaceBracedCommand(out, "tfrac", (a, b) =>
    b === null ? wrapIfCompound(a) : `${wrapIfCompound(a)}/${wrapIfCompound(b)}`
  );
  out = replaceBracedCommand(out, "sqrt", (a) => `√${wrapIfCompound(a)}`);
  out = replaceBracedCommand(out, "text", (a) => a);
  out = replaceBracedCommand(out, "mathrm", (a) => a);
  out = replaceBracedCommand(out, "operatorname", (a) => a);
  out = replaceBracedCommand(out, "mathbb", (a) => {
    const map = { R: "ℝ", N: "ℕ", Z: "ℤ", Q: "ℚ", C: "ℂ" };
    return map[a.trim()] || a;
  });

  out = out.replace(/\\left\s*/g, "").replace(/\\right\s*/g, "");
  out = out.replace(/\\Big[lr]?|\\big[lr]?|\\quad|\\qquad/g, " ");
  out = out.replace(/\\[,;:!]/g, " ");
  out = out.replace(/\\\\/g, "\n");

  for (const key of MATH_KEYS) {
    out = out.split(key).join(MATH_SYMBOLS[key]);
  }

  out = out.replace(/\^\{([^{}]*)\}/g, (_, v) => `^${wrapIfCompound(v)}`);
  out = out.replace(/_\{([^{}]*)\}/g, (_, v) => `_${wrapIfCompound(v)}`);
  out = out.replace(/\^2(?![0-9a-zA-Zа-яА-Я])/g, "²");
  out = out.replace(/\^3(?![0-9a-zA-Zа-яА-Я])/g, "³");

  out = out.replace(/\\([a-zA-Z]+)/g, "$1");
  out = out.replace(/[ \t]{2,}/g, " ");

  return out;
}

function extractMath(text) {
  let out = text.replace(/\$\$([\s\S]+?)\$\$/g, (_, body) => {
    const cleaned = normalizeMath(body).trim();
    return `\n\n@@F@@${cleaned}@@/F@@\n\n`;
  });

  out = out.replace(/\\\[([\s\S]+?)\\\]/g, (_, body) => {
    const cleaned = normalizeMath(body).trim();
    return `\n\n@@F@@${cleaned}@@/F@@\n\n`;
  });

  out = out.replace(/(?<!\\)\$([^$\n]+?)\$/g, (_, body) => normalizeMath(body).trim());
  out = out.replace(/\\\(([\s\S]+?)\\\)/g, (_, body) => normalizeMath(body).trim());

  return normalizeMath(out);
}

function escapeHtml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function renderInline(str) {
  let s = str;
  s = s.replace(/`([^`]+)`/g, (_, code) => `<code>${code}</code>`);
  s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  s = s.replace(/(^|[\s(])\*([^*\n]+)\*(?=[\s).,;:!?]|$)/g, "$1<em>$2</em>");
  s = s.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  return s;
}

function renderOrdered(lines, state) {
  const items = [];
  lines.forEach((line) => {
    const match = line.match(/^\s*(\d+)[.)]\s+(.*)$/);
    if (match) {
      items.push({ number: Number(match[1]), parts: [match[2]] });
    } else if (items.length) {
      items[items.length - 1].parts.push(line.replace(/^\s*[-*•]\s+/, "• ").trim());
    }
  });
  const first = items[0].number;
  const start = state.lastNumber !== null && first <= state.lastNumber ? state.lastNumber + 1 : first;
  state.lastNumber = start + items.length - 1;
  const body = items.map((item) => `<li>${renderInline(item.parts.join("<br />"))}</li>`).join("");
  return start === 1 ? `<ol>${body}</ol>` : `<ol start="${start}">${body}</ol>`;
}

function renderBlocks(text) {
  const blocks = text.split(/\n{2,}/);
  const html = [];
  const listState = { lastNumber: null };

  for (const raw of blocks) {
    const block = raw.trim();
    if (!block) continue;

    const formulaMatch = block.match(/^@@F@@([\s\S]*?)@@\/F@@$/);
    if (formulaMatch) {
      html.push(`<div class="formula">${formulaMatch[1].trim()}</div>`);
      continue;
    }

    if (/^(-{3,}|\*{3,}|_{3,})$/.test(block)) {
      listState.lastNumber = null;
      html.push("<hr />");
      continue;
    }

    const heading = block.match(/^(#{1,6})\s+(.*)$/);
    if (heading && !block.includes("\n")) {
      listState.lastNumber = null;
      const level = Math.min(heading[1].length + 1, 4);
      html.push(`<h${level}>${renderInline(heading[2])}</h${level}>`);
      continue;
    }

    const lines = block.split("\n");

    if (lines.every((l) => /^\s*>/.test(l))) {
      const body = lines.map((l) => l.replace(/^\s*>\s?/, "")).join("<br />");
      html.push(`<blockquote>${renderInline(body)}</blockquote>`);
      continue;
    }

    if (lines.every((l) => /^\s*[-*•]\s+/.test(l))) {
      const items = lines
        .map((l) => `<li>${renderInline(l.replace(/^\s*[-*•]\s+/, ""))}</li>`)
        .join("");
      html.push(`<ul>${items}</ul>`);
      continue;
    }

    if (/^\s*\d+[.)]\s+/.test(lines[0])) {
      html.push(renderOrdered(lines, listState));
      continue;
    }

    html.push(`<p>${renderInline(lines.join("<br />"))}</p>`);
  }

  return html.join("");
}


function renderMarkdown(text) {
  const codeBlocks = [];
  let work = text.replace(/```([a-zA-Z0-9_+#-]*)\n?([\s\S]*?)(?:```|$)/g, (_, lang, code) => {
    const token = `@@C${codeBlocks.length}@@`;
    codeBlocks.push({ lang: lang || "code", code: escapeHtml(code.replace(/\s+$/, "")) });
    return `\n\n${token}\n\n`;
  });

  work = extractMath(work);
  work = escapeHtml(work);

  let html = renderBlocks(work);

  codeBlocks.forEach((block, i) => {
    html = html.replace(
      new RegExp(`<p>@@C${i}@@</p>|@@C${i}@@`),
      `<div class="code"><div class="code-head"><span>${escapeHtml(block.lang)}</span>` +
        `<button class="code-copy" type="button" data-i18n="action.copy">${escapeHtml(t("action.copy"))}</button></div>` +
        `<pre><code>${block.code}</code></pre></div>`
    );
  });

  return html;
}

const appEl = document.getElementById("app");
const scrimEl = document.getElementById("scrim");
const chatEl = document.getElementById("chat");
const threadEl = document.getElementById("thread");
const formEl = document.getElementById("form");
const inputEl = document.getElementById("input");
const sendEl = document.getElementById("send");
const stopEl = document.getElementById("stop");
const scrollDownEl = document.getElementById("scrollDown");
const topbarTitleEl = document.getElementById("topbarTitle");
const historyListEl = document.getElementById("historyList");
const historyLabelEl = document.getElementById("historyLabel");
const historyEmptyEl = document.getElementById("historyEmpty");
const profileEl = document.getElementById("profile");
const profileAvatarEl = document.getElementById("profileAvatar");
const profileEmailEl = document.getElementById("profileEmail");
const planBadgeEl = document.getElementById("planBadge");
const quotaFillEl = document.getElementById("quotaFill");
const quotaTextEl = document.getElementById("quotaText");
const loginBtnEl = document.getElementById("loginBtn");
const topLoginBtnEl = document.getElementById("topLoginBtn");
const statusEl = document.getElementById("status");
const statusTextEl = document.getElementById("statusText");
const menuModalEl = document.getElementById("menuModal");
const menuTabsEl = document.getElementById("menuTabs");
const menuEmailEl = document.getElementById("menuEmail");
const plansGridEl = document.getElementById("plansGrid");
const usageTodayEl = document.getElementById("usageToday");
const usageFillEl = document.getElementById("usageFill");
const usageHintEl = document.getElementById("usageHint");
const usageTableEl = document.getElementById("usageTable");
const langListEl = document.getElementById("langList");

const HISTORY_LIMIT = 8;
const CHATS_LIMIT = 50;


let account = null;
const uiHooks = { account: [], quota: [], language: [], menu: [], plans: [] };
const loadedModules = new Set();

function onUi(name, fn) {
  if (uiHooks[name]) uiHooks[name].push(fn);
}

function runUi(name, arg) {
  (uiHooks[name] || []).forEach((fn) => {
    try {
      fn(arg);
    } catch (_) {
      return;
    }
  });
}

function loadModules(list) {
  (list || []).forEach((src) => {
    if (loadedModules.has(src)) return;
    loadedModules.add(src);
    const script = document.createElement("script");
    script.src = src;
    document.body.appendChild(script);
  });
}
let controller = null;
let streaming = false;
let stickToBottom = true;
let chats = [];
let activeChatId = null;

function storageKey() {
  return `kriloud.chats.${account ? account.email : "guest"}`;
}

function loadChats() {
  try {
    const raw = localStorage.getItem(storageKey());
    const parsed = raw ? JSON.parse(raw) : [];
    chats = Array.isArray(parsed) ? parsed : [];
  } catch (_) {
    chats = [];
  }
}

function saveChats() {
  try {
    localStorage.setItem(storageKey(), JSON.stringify(chats.slice(0, CHATS_LIMIT)));
  } catch (_) {
    return;
  }
}

function activeChat() {
  return chats.find((c) => c.id === activeChatId) || null;
}

function chatTitle(text) {
  const line = text.replace(/\s+/g, " ").trim();
  return line.length > 48 ? `${line.slice(0, 48)}…` : line;
}

function renderHistory() {
  historyListEl.innerHTML = "";
  historyLabelEl.hidden = chats.length === 0;
  historyEmptyEl.hidden = chats.length > 0;

  chats.forEach((chat) => {
    const li = document.createElement("li");
    li.className = "history-item";
    li.classList.toggle("active", chat.id === activeChatId);

    const open = document.createElement("button");
    open.type = "button";
    open.className = "history-open";
    open.textContent = chat.title;
    open.title = chat.title;
    open.addEventListener("click", () => openChat(chat.id));

    const del = document.createElement("button");
    del.type = "button";
    del.className = "history-delete";
    del.dataset.i18nAria = "history.delete";
    del.setAttribute("aria-label", t("history.delete"));
    del.innerHTML =
      '<svg viewBox="0 0 24 24"><path d="M4 7h16M10 11v6M14 11v6M6 7l1 12a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2l1-12M9 7V4h6v3"/></svg>';
    del.addEventListener("click", () => deleteChat(chat.id));

    li.appendChild(open);
    li.appendChild(del);
    historyListEl.appendChild(li);
  });
}

function setEmpty(empty) {
  appEl.classList.toggle("is-empty", empty);
}

function resetThread() {
  threadEl.innerHTML = "";
  scrollDownEl.hidden = true;
  stickToBottom = true;
}

function newChat() {
  if (streaming) stopStreaming();
  activeChatId = null;
  resetThread();
  setEmpty(true);
  topbarTitleEl.textContent = "Kriloud AI";
  renderHistory();
  closeSidebar();
  inputEl.focus();
}

function openChat(id) {
  if (streaming) stopStreaming();
  const chat = chats.find((c) => c.id === id);
  if (!chat) return;
  activeChatId = id;
  resetThread();
  setEmpty(chat.messages.length === 0);
  topbarTitleEl.textContent = chat.title;

  chat.messages.forEach((m) => {
    if (m.role === "user") {
      addUserMessage(m.content);
    } else {
      const view = addBotMessage();
      view.typing.remove();
      view.orb.classList.remove("thinking");
      view.answer.innerHTML = renderMarkdown(m.content);
      addActions(view.body, () => m.content);
    }
  });

  renderHistory();
  closeSidebar();
  scrollToBottom(false);
}

function deleteChat(id) {
  chats = chats.filter((c) => c.id !== id);
  saveChats();
  if (id === activeChatId) {
    newChat();
  } else {
    renderHistory();
  }
}

function ensureChat(firstMessage) {
  let chat = activeChat();
  if (!chat) {
    chat = {
      id: `${Date.now().toString(36)}${Math.random().toString(36).slice(2, 7)}`,
      title: chatTitle(firstMessage),
      messages: [],
      updated: Date.now()
    };
    chats.unshift(chat);
    activeChatId = chat.id;
    topbarTitleEl.textContent = chat.title;
  }
  return chat;
}

function touchChat(chat) {
  chat.updated = Date.now();
  chats = [chat, ...chats.filter((c) => c.id !== chat.id)];
  saveChats();
  renderHistory();
}

function modelHistory(chat) {
  return chat.messages
    .map((m) => ({ role: m.role, content: m.content }))
    .slice(-HISTORY_LIMIT);
}

function isNearBottom() {
  return chatEl.scrollHeight - chatEl.scrollTop - chatEl.clientHeight < 80;
}

function scrollToBottom(smooth) {
  chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: smooth ? "smooth" : "auto" });
}

chatEl.addEventListener("scroll", () => {
  const near = isNearBottom();
  stickToBottom = near;
  scrollDownEl.hidden = near || !threadEl.children.length;
});

scrollDownEl.addEventListener("click", () => {
  stickToBottom = true;
  scrollToBottom(true);
});

function openSidebar() {
  appEl.classList.add("sidebar-open");
  scrimEl.hidden = false;
}

function closeSidebar() {
  appEl.classList.remove("sidebar-open");
  scrimEl.hidden = true;
}

document.getElementById("sidebarOpen").addEventListener("click", openSidebar);
document.getElementById("sidebarClose").addEventListener("click", closeSidebar);
document.getElementById("newChat").addEventListener("click", newChat);
scrimEl.addEventListener("click", closeSidebar);

function formatTokens(value) {
  return new Intl.NumberFormat(langLocale()).format(value || 0);
}

function renderQuota(quota) {
  if (!quota) return;
  planBadgeEl.textContent = quota.plan_label;
  planBadgeEl.dataset.plan = quota.plan;
  if (quota.limit === null) {
    quotaFillEl.style.width = "100%";
    quotaFillEl.classList.remove("over");
    quotaTextEl.textContent = t("quota.unlimited", { used: formatTokens(quota.used_today) });
    runUi("quota", quota);
    return;
  }
  const share = Math.min(100, Math.round((quota.used_today / quota.limit) * 100));
  quotaFillEl.style.width = `${share}%`;
  quotaFillEl.classList.toggle("over", quota.exceeded);
  quotaTextEl.textContent = t("quota.limited", {
    used: formatTokens(quota.used_today),
    limit: formatTokens(quota.limit)
  });
  runUi("quota", quota);
}

function renderAccount(data) {
  account = data && data.authenticated ? data : null;
  profileEl.hidden = !account;
  loginBtnEl.hidden = Boolean(account);
  topLoginBtnEl.hidden = Boolean(account);

  if (account && account.language !== currentLang) {
    setLang(account.language);
  }

  if (account) {
    profileEmailEl.textContent = account.email;
    profileAvatarEl.textContent = account.email.charAt(0);
    renderQuota(account.quota);
  }

  loadChats();
  renderHistory();
  renderModelSwitch();
  if (account) loadModules(account.modules);
  runUi("account", account);
}

const modelSwitchEl = document.getElementById("modelSwitch");

function renderModelSwitch() {
  const models = account && Array.isArray(account.models) ? account.models : [];
  modelSwitchEl.hidden = models.length < 2;
  if (modelSwitchEl.hidden) return;
  const ids = models.map((m) => m.id).join(",");
  if (modelSwitchEl.dataset.ids !== ids) {
    modelSwitchEl.dataset.ids = ids;
    modelSwitchEl.innerHTML = "";
    models.forEach((model) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "model-option";
      btn.dataset.model = model.id;
      btn.setAttribute("role", "radio");
      btn.textContent = model.label;
      btn.addEventListener("click", () => chooseModel(model.id));
      modelSwitchEl.appendChild(btn);
    });
  }
  modelSwitchEl.querySelectorAll(".model-option").forEach((btn) => {
    btn.setAttribute("aria-checked", String(btn.dataset.model === account.model));
  });
}

async function chooseModel(model) {
  if (!account || account.model === model) return;
  const previous = account.model;
  account.model = model;
  renderModelSwitch();
  try {
    const resp = await fetch("/api/settings/model", {
      method: "PUT",
      headers: langHeaders({ "Content-Type": "application/json" }),
      body: JSON.stringify({ model })
    });
    if (!resp.ok) throw new Error();
  } catch (_) {
    account.model = previous;
    renderModelSwitch();
  }
}

function loadAccount() {
  return fetch("/api/auth/me", { headers: langHeaders() })
    .then((r) => r.json())
    .then(renderAccount)
    .catch(() => renderAccount(null));
}

document.getElementById("logoutBtn").addEventListener("click", async () => {
  await fetch("/api/auth/logout", { method: "POST" });
  window.location.reload();
});

function formatLimit(limit) {
  return limit === null ? "∞" : formatTokens(limit);
}

async function loadPlans() {
  if (plansGridEl.children.length) {
    markCurrentPlan();
    return;
  }
  try {
    const plans = await fetch("/api/plans").then((r) => r.json());
    plans.forEach((plan) => {
      const card = document.createElement("div");
      card.className = "plan";
      card.dataset.plan = plan.id;
      card.innerHTML =
        `<span class="plan-name">${escapeHtml(plan.label)}</span>` +
        `<span class="plan-limit">${formatLimit(plan.daily_token_limit)}</span>` +
        `<span class="plan-unit" data-i18n="plans.unit"></span>` +
        `<p class="plan-desc" data-i18n="plan.desc.${escapeHtml(plan.id)}"></p>` +
        `<span class="plan-tag" data-i18n="plans.current" hidden></span>`;
      applyI18n(card);
      plansGridEl.appendChild(card);
    });
    markCurrentPlan();
  } catch (_) {
    plansGridEl.innerHTML = `<div class="error-box">${escapeHtml(t("plans.loadError"))}</div>`;
  }
}

function markCurrentPlan() {
  const current = account ? account.quota.plan : null;
  plansGridEl.querySelectorAll(".plan").forEach((card) => {
    const isCurrent = card.dataset.plan === current;
    card.classList.toggle("current", isCurrent);
    card.querySelector(".plan-tag").hidden = !isCurrent;
  });
  runUi("plans", plansGridEl);
}

function formatDay(day) {
  const date = new Date(`${day}T00:00:00Z`);
  return new Intl.DateTimeFormat(langLocale(), { day: "numeric", month: "long", timeZone: "UTC" }).format(date);
}

function renderUsageToday(quota) {
  if (quota.limit === null) {
    usageTodayEl.textContent = formatTokens(quota.used_today);
    usageFillEl.style.width = "100%";
    usageFillEl.classList.remove("over");
    usageHintEl.textContent = t("usage.hintUnlimited", { plan: quota.plan_label });
    return;
  }
  const share = Math.min(100, Math.round((quota.used_today / quota.limit) * 100));
  usageTodayEl.textContent = `${formatTokens(quota.used_today)} / ${formatTokens(quota.limit)}`;
  usageFillEl.style.width = `${share}%`;
  usageFillEl.classList.toggle("over", quota.exceeded);
  usageHintEl.textContent = quota.exceeded
    ? t("usage.hintExceeded", { plan: quota.plan_label })
    : t("usage.hintRemaining", { plan: quota.plan_label, remaining: formatTokens(quota.remaining) });
}

async function loadUsage() {
  usageTableEl.innerHTML = "";
  try {
    const data = await fetch("/api/usage", { headers: langHeaders() }).then((r) => r.json());
    account.quota = data.quota;
    renderQuota(data.quota);
    renderUsageToday(data.quota);

    if (!data.by_day.length) {
      usageTableEl.innerHTML = `<p class="usage-empty">${escapeHtml(t("usage.empty"))}</p>`;
      return;
    }

    const head = document.createElement("div");
    head.className = "usage-row";
    head.innerHTML =
      `<span>${escapeHtml(t("usage.day"))}</span>` +
      `<span>${escapeHtml(t("usage.requests"))}</span>` +
      `<span>${escapeHtml(t("usage.tokens"))}</span>`;
    usageTableEl.appendChild(head);

    data.by_day.forEach((row) => {
      const total = row.prompt_tokens + row.completion_tokens;
      const el = document.createElement("div");
      el.className = "usage-row";
      el.innerHTML =
        `<span>${formatDay(row.day)}</span>` +
        `<span>${formatTokens(row.requests)}</span>` +
        `<span><strong>${formatTokens(total)}</strong></span>`;
      usageTableEl.appendChild(el);
    });
  } catch (_) {
    usageTableEl.innerHTML = `<div class="error-box">${escapeHtml(t("usage.loadError"))}</div>`;
  }
}

async function renderLanguages() {
  if (!langListEl.children.length) {
    try {
      const languages = await fetch("/api/languages").then((r) => r.json());
      languages.forEach((lang) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "lang-option";
        btn.dataset.lang = lang.id;
        btn.setAttribute("role", "radio");
        btn.innerHTML = `<span class="lang-radio" aria-hidden="true"></span><span>${escapeHtml(lang.label)}</span>`;
        btn.addEventListener("click", () => chooseLanguage(lang.id));
        langListEl.appendChild(btn);
      });
    } catch (_) {
      langListEl.innerHTML = `<div class="error-box">${escapeHtml(t("language.loadError"))}</div>`;
      return;
    }
  }
  markLanguage();
}

function markLanguage() {
  const current = account ? account.language : null;
  langListEl.querySelectorAll(".lang-option").forEach((btn) => {
    btn.setAttribute("aria-checked", String(btn.dataset.lang === current));
  });
}

function refreshLanguage() {
  applyI18n();
  runUi("language", currentLang);
  markLanguage();
  if (account) renderQuota(account.quota);
  if (!menuModalEl.hidden) {
    const active = menuTabsEl.querySelector(".segment.active");
    if (active && active.dataset.tab === "usage") loadUsage();
  }
}

async function chooseLanguage(language) {
  if (!account || account.language === language) return;
  const previous = account.language;
  account.language = language;
  setLang(language);
  refreshLanguage();
  try {
    const resp = await fetch("/api/settings/language", {
      method: "PUT",
      headers: langHeaders({ "Content-Type": "application/json" }),
      body: JSON.stringify({ language })
    });
    if (!resp.ok) throw new Error();
  } catch (_) {
    account.language = previous;
    setLang(previous);
    refreshLanguage();
  }
}

function showTab(tab) {
  menuTabsEl.querySelectorAll(".segment").forEach((btn) => {
    const active = btn.dataset.tab === tab;
    btn.classList.toggle("active", active);
    btn.setAttribute("aria-selected", String(active));
  });
  menuModalEl.querySelectorAll(".menu-panel").forEach((panel) => {
    panel.hidden = panel.dataset.panel !== tab;
  });
  if (tab === "plans") loadPlans();
  if (tab === "usage") loadUsage();
  if (tab === "language") renderLanguages();
  if (tab === "api") loadKeys();
}

const mobileQuery = window.matchMedia("(max-width: 860px)");

function isMobile() {
  return mobileQuery.matches;
}

function openMenu(tab) {
  const authed = Boolean(account);
  const mobile = authed && isMobile();
  menuTabsEl.hidden = !authed || mobile;
  menuEmailEl.hidden = !authed;
  menuEmailEl.textContent = authed ? account.email : "";
  const menuTitleEl = document.getElementById("menuTitle");
  menuTitleEl.dataset.i18n = mobile ? "menu.settings" : authed ? "menu.account" : "menu.plans";
  menuTitleEl.textContent = t(menuTitleEl.dataset.i18n);
  menuModalEl.hidden = false;
  closeSidebar();
  const target = mobile ? "language" : authed ? tab : "plans";
  showTab(target);
  runUi("menu", target);
}

const apiListEl = document.getElementById("apiList");
const apiNameEl = document.getElementById("apiName");
const apiErrorEl = document.getElementById("apiError");
const apiNewEl = document.getElementById("apiNew");
const apiNewKeyEl = document.getElementById("apiNewKey");
const apiConfigEl = document.getElementById("apiConfig");

function continueConfig(key) {
  return [
    "models:",
    "  - name: Universal Kriloud AI FLOCK",
    "    provider: openai",
    "    model: flock",
    `    apiBase: ${window.location.origin}/v1`,
    `    apiKey: ${key || "ukai-..."}`,
    "    roles:",
    "      - chat",
    "      - edit",
    "      - apply",
    "  - name: Universal Kriloud AI Flash",
    "    provider: openai",
    "    model: kriloud-flash",
    `    apiBase: ${window.location.origin}/v1`,
    `    apiKey: ${key || "ukai-..."}`,
    "    roles:",
    "      - chat",
    "      - autocomplete"
  ].join("\n");
}

function formatDate(iso) {
  if (!iso) return t("api.never");
  return new Intl.DateTimeFormat(langLocale(), { dateStyle: "medium", timeStyle: "short" }).format(new Date(iso));
}

function renderKeys(keys) {
  apiListEl.innerHTML = "";
  if (!keys.length) {
    apiListEl.innerHTML = `<p class="usage-empty">${escapeHtml(t("api.empty"))}</p>`;
    return;
  }
  keys.forEach((key) => {
    const row = document.createElement("div");
    row.className = "api-row";
    row.innerHTML =
      `<div class="api-row-body"><span class="api-row-name">${escapeHtml(key.name)}</span>` +
      `<code class="api-row-prefix">${escapeHtml(key.prefix)}</code>` +
      `<span class="api-row-meta">${escapeHtml(t("api.lastUsed"))}: ${escapeHtml(formatDate(key.last_used_at))}</span></div>`;
    const revoke = document.createElement("button");
    revoke.type = "button";
    revoke.className = "api-revoke";
    revoke.textContent = t("api.revoke");
    revoke.addEventListener("click", async () => {
      if (!revoke.dataset.armed) {
        revoke.dataset.armed = "1";
        revoke.textContent = t("api.revokeConfirm");
        setTimeout(() => {
          delete revoke.dataset.armed;
          revoke.textContent = t("api.revoke");
        }, 3000);
        return;
      }
      revoke.disabled = true;
      await fetch(`/api/keys/${key.id}`, { method: "DELETE", headers: langHeaders() });
      loadKeys();
    });
    row.appendChild(revoke);
    apiListEl.appendChild(row);
  });
}

async function loadKeys() {
  apiErrorEl.hidden = true;
  if (apiNewEl.hidden) apiConfigEl.textContent = continueConfig("");
  try {
    const keys = await fetch("/api/keys", { headers: langHeaders() }).then((r) => r.json());
    renderKeys(Array.isArray(keys) ? keys : []);
  } catch (_) {
    apiListEl.innerHTML = `<div class="error-box">${escapeHtml(t("api.loadError"))}</div>`;
  }
}

document.getElementById("apiCreate").addEventListener("submit", async (e) => {
  e.preventDefault();
  apiErrorEl.hidden = true;
  try {
    const resp = await fetch("/api/keys", {
      method: "POST",
      headers: langHeaders({ "Content-Type": "application/json" }),
      body: JSON.stringify({ name: apiNameEl.value.trim() })
    });
    const data = await resp.json();
    if (!resp.ok) {
      apiErrorEl.textContent = data.detail || t("api.loadError");
      apiErrorEl.hidden = false;
      return;
    }
    apiNameEl.value = "";
    apiNewKeyEl.textContent = data.key;
    apiNewEl.hidden = false;
    apiConfigEl.textContent = continueConfig(data.key);
    loadKeys();
  } catch (_) {
    apiErrorEl.textContent = t("chat.connError");
    apiErrorEl.hidden = false;
  }
});

document.getElementById("apiCopyKey").addEventListener("click", async (e) => {
  const btn = e.currentTarget;
  await writeClipboard(apiNewKeyEl.textContent);
  flashLabel(btn, t("action.copied"));
});

document.getElementById("apiCopyConfig").addEventListener("click", async (e) => {
  const btn = e.currentTarget;
  await writeClipboard(apiConfigEl.textContent);
  flashLabel(btn, t("action.copied"));
});

function closeMenu() {
  menuModalEl.hidden = true;
  apiNewEl.hidden = true;
  apiNewKeyEl.textContent = "";
}

menuTabsEl.addEventListener("click", (e) => {
  const btn = e.target.closest(".segment");
  if (btn) showTab(btn.dataset.tab);
});

document.getElementById("plansBtn").addEventListener("click", () => openMenu("plans"));
document.getElementById("profileOpen").addEventListener("click", () => openMenu("plans"));
document.getElementById("menuClose").addEventListener("click", closeMenu);
menuModalEl.addEventListener("click", (e) => {
  if (e.target === menuModalEl) closeMenu();
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    closeSidebar();
    closeMenu();
  }
});

function setStatus(state, key) {
  statusEl.dataset.state = state;
  statusTextEl.dataset.i18n = key;
  statusTextEl.textContent = t(key);
}

fetch("/api/health")
  .then((r) => r.json())
  .then((data) => {
    setStatus(data.ok ? "ok" : "err", data.ok ? "status.ok" : "status.down");
  })
  .catch(() => setStatus("err", "status.offline"));

function autoresize() {
  inputEl.style.height = "auto";
  inputEl.style.height = Math.min(inputEl.scrollHeight, 220) + "px";
}

function updateSendState() {
  sendEl.disabled = streaming || !inputEl.value.trim();
}

inputEl.addEventListener("input", () => {
  autoresize();
  updateSendState();
});

inputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey && !e.isComposing) {
    e.preventDefault();
    if (!sendEl.disabled) formEl.requestSubmit();
  }
});

document.querySelectorAll(".suggest").forEach((btn) => {
  btn.addEventListener("click", () => {
    inputEl.value = btn.dataset.text;
    autoresize();
    updateSendState();
    formEl.requestSubmit();
  });
});

function addUserMessage(text) {
  const msg = document.createElement("div");
  msg.className = "msg-user";
  msg.textContent = text;
  threadEl.appendChild(msg);
}

function addBotMessage() {
  const row = document.createElement("div");
  row.className = "msg-bot";

  const orb = document.createElement("span");
  orb.className = "orb orb-xs thinking";
  orb.setAttribute("aria-hidden", "true");

  const body = document.createElement("div");
  body.className = "msg-bot-body";

  const answer = document.createElement("div");
  answer.className = "answer";

  const typing = document.createElement("div");
  typing.className = "typing";
  typing.innerHTML = "<span></span><span></span><span></span>";

  body.appendChild(typing);
  body.appendChild(answer);
  row.appendChild(orb);
  row.appendChild(body);
  threadEl.appendChild(row);

  return { row, orb, body, answer, typing };
}

function showQueue(view, position) {
  if (!view.queueNote) {
    view.queueNote = document.createElement("div");
    view.queueNote.className = "queue-note";
    view.body.insertBefore(view.queueNote, view.body.firstChild);
  }
  view.queueNote.dataset.position = position;
  view.queueNote.textContent = t("chat.queue", { position });
}

function hideQueue(view) {
  if (view.queueNote) {
    view.queueNote.remove();
    view.queueNote = null;
  }
}

async function writeClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
  } catch (_) {
    const ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    document.execCommand("copy");
    ta.remove();
  }
}

function flashLabel(el, text) {
  const previous = el.textContent;
  el.textContent = text;
  setTimeout(() => {
    el.textContent = previous;
  }, 1400);
}

function addActions(body, getText) {
  const wrap = document.createElement("div");
  wrap.className = "actions";

  const copyBtn = document.createElement("button");
  copyBtn.className = "action";
  copyBtn.type = "button";
  copyBtn.innerHTML =
    '<svg viewBox="0 0 24 24"><rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h8"/></svg><span data-i18n="action.copy"></span>';
  applyI18n(copyBtn);
  copyBtn.addEventListener("click", async () => {
    await writeClipboard(getText());
    flashLabel(copyBtn.querySelector("span"), t("action.copied"));
  });

  wrap.appendChild(copyBtn);
  body.appendChild(wrap);
}

threadEl.addEventListener("click", async (e) => {
  const btn = e.target.closest(".code-copy");
  if (!btn) return;
  const code = btn.closest(".code").querySelector("code").textContent;
  await writeClipboard(code);
  flashLabel(btn, t("action.copied"));
});

function setStreaming(active) {
  streaming = active;
  stopEl.hidden = !active;
  sendEl.hidden = active;
  updateSendState();
}

function stopStreaming() {
  if (controller) controller.abort();
}

stopEl.addEventListener("click", stopStreaming);

function showError(view, html) {
  hideQueue(view);
  view.typing.remove();
  view.orb.classList.remove("thinking");
  view.answer.innerHTML = `<div class="error-box">${html}</div>`;
}

formEl.addEventListener("submit", async (e) => {
  e.preventDefault();
  if (streaming) return;

  const message = inputEl.value.trim();
  if (!message) return;

  setEmpty(false);
  addUserMessage(message);
  inputEl.value = "";
  autoresize();
  stickToBottom = true;

  const view = addBotMessage();
  scrollToBottom(false);

  if (!account) {
    showError(view, t("chat.loginRequired"));
    updateSendState();
    return;
  }

  const chat = ensureChat(message);
  const history = modelHistory(chat);
  chat.messages.push({ role: "user", content: message });
  touchChat(chat);

  setStreaming(true);
  controller = new AbortController();

  let fullText = "";
  let pendingRender = false;

  const flush = () => {
    pendingRender = false;
    view.answer.innerHTML = renderMarkdown(fullText);
    if (stickToBottom) scrollToBottom(false);
  };

  const finish = () => {
    view.orb.classList.remove("thinking");
    if (!fullText.trim()) return;
    chat.messages.push({ role: "assistant", content: fullText });
    touchChat(chat);
    addActions(view.body, () => fullText);
  };

  try {
    const resp = await fetch("/api/chat", {
      method: "POST",
      headers: langHeaders({ "Content-Type": "application/json" }),
      body: JSON.stringify({ message, history }),
      signal: controller.signal
    });

    if (!resp.ok) {
      let detail = t("chat.serverStatus", { status: resp.status });
      try {
        const data = await resp.json();
        if (data && data.detail) detail = data.detail;
      } catch (_) {
        detail = t("chat.serverStatus", { status: resp.status });
      }
      if (resp.status === 401 || resp.status === 429) loadAccount();
      throw new Error(detail);
    }

    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";
    let failed = false;

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });

      const parts = buffer.split("\n\n");
      buffer = parts.pop();

      for (const part of parts) {
        const line = part.trim();
        if (!line.startsWith("data:")) continue;

        let payload;
        try {
          payload = JSON.parse(line.slice(5).trim());
        } catch (_) {
          continue;
        }

        if (payload.type === "queue") {
          showQueue(view, payload.position);
        } else if (payload.type === "queue_done") {
          hideQueue(view);
        } else if (payload.type === "token") {
          hideQueue(view);
          if (!fullText) view.typing.remove();
          fullText += payload.text;
          if (!pendingRender) {
            pendingRender = true;
            requestAnimationFrame(flush);
          }
        } else if (payload.type === "done") {
          if (payload.quota && account) {
            account.quota = payload.quota;
            renderQuota(payload.quota);
          }
        } else if (payload.type === "error") {
          failed = true;
          showError(view, escapeHtml(payload.text));
        }
      }
    }

    if (!failed) {
      flush();
      finish();
    }
  } catch (err) {
    if (err.name === "AbortError") {
      view.typing.remove();
      flush();
      if (fullText.trim()) {
        finish();
      } else {
        showError(view, escapeHtml(t("chat.stopped")));
      }
    } else {
      showError(view, escapeHtml(err.message || t("chat.connError")));
    }
  } finally {
    controller = null;
    setStreaming(false);
    inputEl.focus();
  }
});

function syncViewport() {
  const viewport = window.visualViewport;
  if (!viewport) return;
  document.documentElement.style.setProperty("--app-height", `${Math.round(viewport.height)}px`);
  if (document.activeElement === inputEl) scrollToBottom(false);
}

if (window.visualViewport) {
  window.visualViewport.addEventListener("resize", syncViewport);
  syncViewport();
}

if ("serviceWorker" in navigator && window.isSecureContext) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/sw.js").catch(() => {});
  });
}

applyI18n();
setEmpty(true);
loadAccount();
updateSendState();
autoresize();
inputEl.focus();
