document.addEventListener("DOMContentLoaded", function () {
    const glossaryUrl = "/assets/glossary.json";
    const tooltipClass = "glossary-tooltip";

    fetch(glossaryUrl)
        .then((res) => res.json())
        .then((glossary) => {
            const links = document.querySelectorAll("a[href*='#']");
            links.forEach((link) => {
                const hash = link.getAttribute("href").split("#")[1];
                if (!hash) return;
                const slug = hash.toLowerCase().replace(/[^\w]+/g, "-").replace(/(^-|-$)/g, "");
                const def = glossary[slug];
                if (!def) return;

                // Create and configure tooltip
                link.setAttribute("data-tooltip", def);
                link.classList.add(tooltipClass);
            });

            injectTooltipStyles();
        });

    function injectTooltipStyles() {
        const style = document.createElement("style");
        style.textContent = `
      .${tooltipClass} {
        position: relative;
        cursor: help;
      }
      .${tooltipClass}::after {
        content: attr(data-tooltip);
        position: absolute;
        bottom: 125%;
        left: 0;
        z-index: 100;
        width: max-content;
        max-width: 320px;
        background: rgba(0, 0, 0, 0.85);
        color: white;
        padding: 6px 10px;
        font-size: 0.8rem;
        border-radius: 4px;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.2s ease-in-out;
        white-space: normal;
      }
      .${tooltipClass}:hover::after {
        opacity: 1;
      }
    `;
        document.head.appendChild(style);
    }
});