/* ==========================================================================
   Premium Woven Labels — main.js
   Sections: header, mobile drawer, reveal, gallery + lightbox, quote form
   No dependencies, no transpilation.
   ========================================================================== */

  /* Config — paste a Formspree / Getform endpoint to also receive email copies */
  var FORM_ENDPOINT = "";

(function () {
  "use strict";

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  /* ---- header sticky state ---- */
  var head = $(".site-head");
  if (head) {
    function onScroll() {
      head.classList.toggle("is-stuck", window.scrollY > 6);
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---- mobile drawer ---- */
  var overlay = $(".m-menu");
  var menuBtn = $(".menu-btn");
  var closeBtn = $(".m-close");

  function openMenu() {
    if (!overlay) return;
    overlay.classList.add("is-open");
    overlay.removeAttribute("aria-hidden");
    document.body.style.overflow = "hidden";
    if (closeBtn) closeBtn.focus();
  }
  function closeMenu() {
    if (!overlay) return;
    overlay.classList.remove("is-open");
    overlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    if (menuBtn) menuBtn.focus();
  }
  if (menuBtn) menuBtn.addEventListener("click", openMenu);
  if (closeBtn) closeBtn.addEventListener("click", closeMenu);
  if (overlay) {
    overlay.addEventListener("click", function (e) {
      if (e.target === overlay) closeMenu();
    });
  }
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && overlay && overlay.classList.contains("is-open")) closeMenu();
  });

  /* ---- reveal on scroll ---- */
  var reveals = $$(".reveal");
  if (reveals.length && "IntersectionObserver" in window) {
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("is-in");
          ro.unobserve(e.target);
        }
      });
    }, { rootMargin: "0px 0px -60px 0px", threshold: 0.05 });
    reveals.forEach(function (el) { ro.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ---- gallery lightbox (real photos, two groups: brand + school) ---- */
  var lb = $("#lightbox");
  if (lb) {
    var lbInner = $("#lbInner");
    var lbCap   = $("#lbCap");
    var allItems = [];   // flat list, rebuilt per group click
    var cur = 0;

    function openLb(btn, group) {
      // collect all items in this group for prev/next navigation
      var groupGrid = document.getElementById("galGrid-" + group);
      allItems = groupGrid ? Array.prototype.slice.call(groupGrid.querySelectorAll(".gal-item")) : [btn];
      cur = allItems.indexOf(btn);
      if (cur < 0) cur = 0;
      showLb();
    }

    function showLb() {
      var btn = allItems[cur];
      var img = btn.querySelector("img");
      lbInner.innerHTML = '<img src="' + img.src + '" alt="' + img.alt + '" loading="eager">';
      if (lbCap) lbCap.textContent = btn.getAttribute("data-cap") || "";
      lb.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
      var cl = $(".lb-close", lb);
      if (cl) cl.focus();
    }

    function closeLb() {
      lb.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
    }

    function navLb(dir) {
      cur = (cur + dir + allItems.length) % allItems.length;
      showLb();
    }

    $$(".gal-item").forEach(function (btn) {
      btn.addEventListener("click", function () {
        openLb(btn, btn.getAttribute("data-group") || "brand");
      });
      btn.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openLb(btn, btn.getAttribute("data-group") || "brand"); }
      });
    });

    var cl = $(".lb-close", lb);
    var pv = $(".lb-prev", lb);
    var nx = $(".lb-next", lb);
    if (cl) cl.addEventListener("click", closeLb);
    if (pv) pv.addEventListener("click", function () { navLb(-1); });
    if (nx) nx.addEventListener("click", function () { navLb(1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) closeLb(); });
    document.addEventListener("keydown", function (e) {
      if (lb.getAttribute("aria-hidden") === "false") {
        if (e.key === "Escape")     closeLb();
        if (e.key === "ArrowLeft")  navLb(-1);
        if (e.key === "ArrowRight") navLb(1);
      }
    });
  }

  /* ---- analytics events (active once GA_ID is set in _src/core.py) ---- */
  function track(name, params) {
    if (typeof window.gtag === "function") { window.gtag("event", name, params || {}); }
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("a[href]") : null;
    if (!a) return;
    var h = a.getAttribute("href") || "";
    if (h.indexOf("wa.me") > -1) track("whatsapp_click", { link_location: a.className || "link" });
    else if (h.indexOf("mailto:") === 0) track("email_click");
  });

  /* ---- quote form: WhatsApp message with every field (+ optional email copy via FORM_ENDPOINT) ---- */
  var form = $("#quoteForm");
  if (form) {
    var FIELDS = [["name", "Name"], ["brand", "Brand"], ["whatsapp", "WhatsApp"], ["email", "Email"],
                  ["labelType", "Label type"], ["quantity", "Quantity"], ["size", "Size"], ["fold", "Fold"],
                  ["message", "Details"]];
    function summary(fd, intro) {
      var lines = [intro];
      FIELDS.forEach(function (p) {
        var v = (fd.get(p[0]) || "").toString().trim();
        if (v) lines.push(p[1] + ": " + v);
      });
      var f = fd.get("artwork");
      lines.push(f && f.name ? "Artwork: " + f.name + " (I will attach it in this chat)" : "(I will send my artwork in this chat.)");
      return lines.join("\n");
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var fd = new FormData(form);
      if (fd.get("botcheck") || fd.get("_gotcha")) { return; }
      if (FORM_ENDPOINT) {
        fetch(FORM_ENDPOINT, { method: "POST", body: fd, headers: { Accept: "application/json" } }).catch(function () {});
      }
      track("quote_form_submit", { label_type: fd.get("labelType") || "" });
      window.open("https://wa.me/923048095202?text=" +
        encodeURIComponent(summary(fd, "Hi Premium Woven Labels, I would like a quote.")), "_blank", "noopener");
    });
    var emailBtn = $("#formEmailBtn");
    if (emailBtn) {
      emailBtn.addEventListener("click", function () {
        var fd = new FormData(form);
        window.location.href = "mailto:premiumwovenlabel@gmail.com?subject=" +
          encodeURIComponent("Woven label quote request") + "&body=" + encodeURIComponent(summary(fd, "Hello Premium Woven Labels,"));
      });
    }
  }

})();
