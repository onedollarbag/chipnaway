# UX & Accessibility Design Notes

This document describes how the Chip'n Away site applies established UI/UX and accessibility guidelines. All implementations are aligned with the cited sources.

---

## Sources

1. **Nielsen Norman Group (NN/G) — 10 Usability Heuristics for User Interface Design**  
   [https://www.nngroup.com/articles/ten-usability-heuristics](https://www.nngroup.com/articles/ten-usability-heuristics)  
   Foundational heuristics for assessing and improving interface usability.

2. **W3C — Web Content Accessibility Guidelines (WCAG) 2.1**  
   [https://www.w3.org/TR/WCAG21/](https://www.w3.org/TR/WCAG21/)  
   Success criteria for making web content accessible (Level A and AA where noted).

3. **W3C WAI — Understanding Focus Visible (SC 2.4.7)**  
   [https://www.w3.org/WAI/WCAG21/Understanding/focus-visible](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible)  
   Requirements for visible keyboard focus indicators.

4. **W3C WAI — Understanding Bypass Blocks (SC 2.4.1)**  
   [https://www.w3.org/WAI/WCAG21/Understanding/bypass-blocks](https://www.w3.org/WAI/WCAG21/Understanding/bypass-blocks)  
   Requirement for a mechanism to skip repeated content (e.g. navigation).

---

## How We Apply These Rules

### Visibility of system status (NN/G Heuristic 1)

- **Success feedback:** After donation or volunteer submission, a clear success message is shown (e.g. “Thank you for your donation…”).  
- **Live region:** Success blocks use `role="status"` so assistive technologies announce the result.  
- **Form errors:** Validation errors are shown inline next to each field and in error blocks with `role="alert"` and `aria-live="assertive"` so they are announced immediately [[1](https://www.nngroup.com/articles/ten-usability-heuristics)].

### Match between system and real world (NN/G Heuristic 2)

- **Language:** Copy uses plain language (“Give now,” “Volunteer,” “Learn more about us,” “What we do,” “Our story”).  
- **Familiar patterns:** Primary action (Donate) is emphasized in the nav and hero; secondary actions (Volunteer, Events, About) are clearly available [[1](https://www.nngroup.com/articles/ten-usability-heuristics)].

### Consistency and standards (NN/G Heuristic 4)

- **Navigation:** Same nav order and labels on every page (Home, About, Events, Volunteer, Donate).  
- **Active state:** Current page is indicated in the nav (e.g. `.nav-link--active`).  
- **Buttons/links:** Primary actions use `.btn-primary`, secondary use `.btn-secondary` or text links; “Give now” is consistently the main CTA [[1](https://www.nngroup.com/articles/ten-usability-heuristics)].

### Recognition rather than recall (NN/G Heuristic 6)

- **Labels:** Form fields have visible `<label>` elements associated via `for`/`id`.  
- **Section headings:** Each section has a clear heading (e.g. “What we do,” “Donation details,” “Volunteers & Supporters Needed”) so users can scan content [[1](https://www.nngroup.com/articles/ten-usability-heuristics)].

### Aesthetic and minimalist design (NN/G Heuristic 8)

- **Concise copy:** Content was trimmed so each section communicates one main idea.  
- **Hierarchy:** One main heading (`h1`) per page; section titles use `h2`; cards and asides keep visual hierarchy clear [[1](https://www.nngroup.com/articles/ten-usability-heuristics)].

### Error prevention and recovery (NN/G Heuristics 5 & 9)

- **Validation:** Server-side validation with inline error messages.  
- **Error presentation:** Errors appear next to the relevant field and use `role="alert"` so screen reader users hear them and can correct mistakes [[1](https://www.nngroup.com/articles/ten-usability-heuristics)] [[2](https://www.w3.org/TR/WCAG21/)].

---

## Accessibility (WCAG)

### Bypass blocks (WCAG 2.4.1 — Level A)

- A **skip link** (“Skip to main content”) is the first focusable element on the page.  
- It links to `#main-content` (the `<main>` element).  
- The link is visually off-screen until it receives keyboard focus, so keyboard and screen reader users can skip repeated navigation [[4](https://www.w3.org/WAI/WCAG21/Understanding/bypass-blocks)].

### Focus visible (WCAG 2.4.7 — Level A)

- All interactive elements (nav links, buttons, form controls, text links) have a **visible focus indicator** when focused via keyboard.  
- Focus styles use a 2px outline (or equivalent) with sufficient contrast (e.g. `outline: 2px solid var(--accent)` or `var(--text-main)` with `outline-offset: 2px`).  
- Implemented with `:focus-visible` so mouse users do not see the focus ring unless they use keyboard [[3](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible)].

### Page structure and semantics

- **Landmarks:** `<header>`, `<main id="main-content" role="main">`, and `<footer>` are used so assistive technologies can navigate by region.  
- **Headings:** One `h1` per page; logical `h2` section headings.  
- **Images:** Decorative or meaningful images have appropriate `alt` text; figures use `aria-label` where it adds context.

---

## Summary

| Guideline / criterion        | Source        | Implementation summary                                      |
|-----------------------------|---------------|--------------------------------------------------------------|
| Visibility of system status | NN/G Heuristic 1 | Success messages + `role="status"`; errors with `role="alert"` |
| Consistency and standards   | NN/G Heuristic 4 | Stable nav, active states, consistent primary/secondary CTAs   |
| Recognition over recall    | NN/G Heuristic 6 | Labels on all inputs; clear section headings                  |
| Minimalist design           | NN/G Heuristic 8 | Short copy; clear visual hierarchy                            |
| Error recovery              | NN/G Heuristic 9 | Inline errors + `role="alert"` / `aria-live="assertive"`       |
| Bypass blocks               | WCAG 2.4.1 (A)   | Skip link to `#main-content`                                  |
| Focus visible               | WCAG 2.4.7 (A)   | Visible focus on all interactive elements via `:focus-visible` |

For full criteria and techniques, refer to the linked W3C and NN/G documents above.
