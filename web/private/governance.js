(function () {
  Object.assign(I18N.ru, { "gov.status": "Governance" });
  Object.assign(I18N.ja, { "gov.status": "Governance" });

  const style = document.createElement("style");
  style.textContent = `
    .gov-badge {
      font-size: 12px;
      font-weight: 600;
      padding: 1px 8px;
      border-radius: 999px;
      background: linear-gradient(90deg, #1f8a5b, #2bb38a);
      color: #fff;
    }
    .profile-body .badges {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .plan .gov-badge {
      align-self: flex-start;
    }
  `;
  document.head.appendChild(style);

  const badgeHost = document.createElement("span");
  badgeHost.className = "badges";
  const badge = document.createElement("span");
  badge.className = "gov-badge";
  badge.dataset.i18n = "gov.status";

  const planBadge = document.getElementById("planBadge");
  planBadge.parentNode.insertBefore(badgeHost, planBadge);
  badgeHost.appendChild(planBadge);
  badgeHost.appendChild(badge);

  function enabled() {
    return Boolean(account && account.governance);
  }

  function markPlans(grid) {
    grid.querySelectorAll(".plan").forEach((card) => {
      let tag = card.querySelector(".gov-badge");
      const isCurrent = card.classList.contains("current") && enabled();
      if (isCurrent && !tag) {
        tag = document.createElement("span");
        tag.className = "gov-badge";
        tag.dataset.i18n = "gov.status";
        tag.textContent = t("gov.status");
        card.appendChild(tag);
      } else if (!isCurrent && tag) {
        tag.remove();
      }
    });
  }

  function render() {
    badge.hidden = !enabled();
    applyI18n(badgeHost);
  }

  onUi("account", render);
  onUi("language", render);
  onUi("plans", markPlans);
  render();
})();
