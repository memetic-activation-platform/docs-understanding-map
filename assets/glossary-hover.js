(() => {
    const tooltipClass = "glossary-tooltip";
    let glossaryPromise;

    initializeGlossaryHover();

    if (typeof document$ !== "undefined" && document$.subscribe) {
        document$.subscribe(() => {
            initializeGlossaryHover();
        });
    } else {
        document.addEventListener("DOMContentLoaded", initializeGlossaryHover);
    }

    function initializeGlossaryHover() {
        const tooltip = ensureTooltip();
        injectStyles();

        loadGlossary()
            .then((glossary) => {
                bindGlossaryLinks(glossary, tooltip);
            })
            .catch((error) => {
                console.warn("Unable to load glossary hover data:", error);
            });
    }

    function loadGlossary() {
        if (!glossaryPromise) {
            glossaryPromise = fetch(resolveGlossaryUrl()).then((res) => res.json());
        }
        return glossaryPromise;
    }

    function bindGlossaryLinks(glossary, tooltip) {
        const links = document.querySelectorAll("a[href*='#']");
        links.forEach((link) => {
            if (link.dataset.glossaryBound === "true") {
                return;
            }

            const href = link.getAttribute("href") || "";
            const hash = href.split("#")[1];
            if (!hash) {
                return;
            }

            const normalizedHash = decodeURIComponent(hash);
            const slug = glossary[normalizedHash]
                ? normalizedHash
                : normalizedHash.toLowerCase().replace(/[^\w]+/g, "-").replace(/(^-|-$)/g, "");
            let def = glossary[slug];
            if (!def) {
                return;
            }

            def = formatDefinition(def);

            link.dataset.glossaryBound = "true";
            link.classList.add(tooltipClass);
            link.addEventListener("mouseenter", () => {
                tooltip.innerHTML = def.replace(/\n/g, "<br>");
                tooltip.style.display = "block";
                const rect = link.getBoundingClientRect();
                tooltip.style.top = `${rect.top + window.scrollY - tooltip.offsetHeight - 10}px`;
                tooltip.style.left = `${rect.left + window.scrollX}px`;
            });

            link.addEventListener("mouseleave", () => {
                tooltip.style.display = "none";
            });
        });
    }

    function formatDefinition(def) {
        return def
            .replace(/\*\*(.*?)\*\*/g, "$1")
            .replace(/\*(.*?)\*/g, "$1")
            .replace(/\[(.*?)\]\(.*?\)/g, "$1")
            .replace(/`([^`]+)`/g, "$1")
            .replace(/#+\s/g, "")
            .replace(/>\s*/g, "")
            .replace(/-\s+/g, "• ")
            .replace(/•\s*/g, "\n• ")
            .trim();
    }

    function ensureTooltip() {
        let tooltip = document.getElementById("glossary-tooltip");
        if (!tooltip) {
            tooltip = document.createElement("div");
            tooltip.id = "glossary-tooltip";
            document.body.appendChild(tooltip);
        }
        return tooltip;
    }

    function injectStyles() {
        if (document.getElementById("glossary-tooltip-styles")) {
            return;
        }

        const style = document.createElement("style");
        style.id = "glossary-tooltip-styles";
        style.textContent = `
      #glossary-tooltip {
        display: none;
        position: absolute;
        background: rgba(0, 0, 0, 0.9);
        color: white;
        padding: 10px 12px;
        font-size: 0.68rem;
        line-height: 1.5;
        max-width: 320px;
        white-space: pre-line;
        border-radius: 6px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
        z-index: 1000;
        pointer-events: none;
      }

      .${tooltipClass} {
        cursor: help;
      }
    `;
        document.head.appendChild(style);
    }

    function resolveGlossaryUrl() {
        const script = document.querySelector("script[src*='glossary-hover.js']");
        if (script) {
            const src = script.getAttribute("src");
            const glossarySrc = src.replace(/glossary-hover[.]js(?:[?].*)?$/, "glossary.json");
            return new URL(glossarySrc, window.location.href).toString();
        }

        return new URL("assets/glossary.json", window.location.href).toString();
    }
})();
