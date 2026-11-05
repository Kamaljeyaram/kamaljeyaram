"""Shared design tokens for every generated profile asset (editorial style)."""

THEMES = {
    "light": {
        "bg": "#F2EFE8",      # paper
        "bg2": "#FAF8F4",     # raised surface (nodes)
        "ink": "#111111",
        "sub": "#4A4640",
        "muted": "#8A857C",
        "rule": "#D6CFC2",
        "accent": "#FF4D2E",
        "on_accent": "#111111",
        "hi": "#FFFFFF",
        "lang": ["#FF4D2E", "#111111", "#6E6960", "#A39D92", "#C9C2B5", "#E2DCD0", "#EDE8DE"],
    },
    "dark": {
        "bg": "#121110",
        "bg2": "#1A1816",
        "ink": "#F2EFE8",
        "sub": "#B3ADA2",
        "muted": "#7D776E",
        "rule": "#2E2A26",
        "accent": "#FF4D2E",
        "on_accent": "#121110",
        "hi": "#FFFFFF",
        "lang": ["#FF4D2E", "#F2EFE8", "#A39D92", "#6E6960", "#4A4640", "#33302C", "#26231F"],
    },
}

SANS = 'font-family="Segoe UI, -apple-system, BlinkMacSystemFont, Helvetica Neue, Arial, sans-serif"'
MONO = 'font-family="ui-monospace, SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace"'

REDUCED_MOTION = "@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }"


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(width: int, height: int, body: str, *, title: str, defs: str = "", style: str = "") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{esc(title)}">\n'
        f"<title>{esc(title)}</title>\n<defs>{defs}</defs>\n"
        f"<style>{style}{REDUCED_MOTION}</style>\n{body}\n</svg>\n"
    )
