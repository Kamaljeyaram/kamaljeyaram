"""Build every static profile asset (light + dark) into assets/.

Run from the repo root:  python scripts/build_assets.py
Edit the content dictionaries below and re-run to regenerate.
"""
from pathlib import Path

from theme import MONO, SANS, THEMES, esc, svg

ASSETS = Path(__file__).resolve().parent.parent / "assets"
MONO_CHAR = 6.8  # approx. advance of an 11px monospace glyph


# --------------------------------------------------------------------------- banner
def banner(t):
    body = f'''
<clipPath id="card"><rect width="1200" height="320" rx="14"/></clipPath>
<clipPath id="paper"><rect x="0" y="0" width="880" height="320"/></clipPath>
<clipPath id="block"><rect x="880" y="0" width="320" height="320"/></clipPath>
<g clip-path="url(#card)">
  <rect width="1200" height="320" fill="{t["bg"]}"/>
  <rect x="880" y="0" width="320" height="320" fill="{t["accent"]}"/>
  <text x="36" y="148" {SANS} font-size="150" font-weight="900" fill="{t["ink"]}" textLength="560" lengthAdjust="spacingAndGlyphs">KAMAL</text>
  <g {SANS} font-size="150" font-weight="900" fill="none" stroke-width="2">
    <text x="36" y="292" stroke="{t["ink"]}" clip-path="url(#paper)" textLength="900" lengthAdjust="spacingAndGlyphs">JEYARAM</text>
    <text x="36" y="292" stroke="{t["bg"]}" clip-path="url(#block)" textLength="900" lengthAdjust="spacingAndGlyphs">JEYARAM</text>
  </g>
  <text x="640" y="56" {MONO} font-size="12" letter-spacing="3" fill="{t["ink"]}">NO. 01 — AGENTIC SYSTEMS</text>
  <text x="640" y="88" {SANS} font-size="18" fill="{t["sub"]}">Building AI agents</text>
  <text x="640" y="112" {SANS} font-size="18" fill="{t["sub"]}">that see, read &amp; act.</text>
  <text x="1164" y="56" text-anchor="end" {MONO} font-size="12" letter-spacing="3" fill="{t["on_accent"]}">THE LOOP ↻</text>
  <g {MONO} font-size="10" letter-spacing="1.5" fill="{t["on_accent"]}" fill-opacity="0.75">
    <text x="960" y="112">01 / VISION · OCR</text>
    <text x="960" y="174">02 / LLMs · RETRIEVAL</text>
    <text x="960" y="236">03 / TOOLS · APIs · APPS</text>
  </g>
  <g {SANS} font-size="30" font-weight="900">
    <text class="w" x="958" y="142">PERCEIVE</text>
    <text class="w w2" x="958" y="204">REASON</text>
    <text class="w w3" x="958" y="266">ACT</text>
  </g>
</g>'''
    style = (f'.w{{fill:{t["on_accent"]};animation:hl 6s infinite}}.w2{{animation-delay:2s}}.w3{{animation-delay:4s}}'
             f'@keyframes hl{{0%,26%{{fill:{t["hi"]}}}33%,100%{{fill:{t["on_accent"]}}}}}')
    return svg(1200, 320, body, title="Kamal Jeyaram — building AI agents that see, read and act", style=style)


# --------------------------------------------------------------------------- section headers
HEADERS = {
    "map": ("SYSTEM MAP", "HOW EVERY PROJECT FITS ONE LOOP"),
    "systems": ("SELECTED SYSTEMS", "REASON FIRST · THEN PERCEPTION"),
    "act": ("ACT", "STAGE 03 — TOOLS, APIs & APPS"),
    "signals": ("SIGNALS", "LIVE · REBUILT DAILY BY GITHUB ACTIONS"),
    "toolbox": ("TOOLBOX", "WHAT THE SYSTEMS ARE BUILT WITH"),
}


def header(t, word, tag):
    body = f'''
<rect x="0" y="34" width="18" height="18" fill="{t["accent"]}"/>
<text x="34" y="56" {SANS} font-size="34" font-weight="900" letter-spacing="0.5" fill="{t["ink"]}">{esc(word)}</text>
<text x="1200" y="54" text-anchor="end" {MONO} font-size="12" letter-spacing="3" fill="{t["muted"]}">{esc(tag)}</text>
<rect x="0" y="74" width="1200" height="2" fill="{t["ink"]}"/>
<rect x="0" y="74" width="160" height="2" fill="{t["accent"]}" class="bar"/>'''
    style = ".bar{animation:grow 3.2s ease-in-out infinite alternate}@keyframes grow{to{transform:translateX(1040px)}}"
    return svg(1200, 84, body, title=word.title(), style=style)


# --------------------------------------------------------------------------- system map
MAP = [
    ("01", "PERCEIVE", "SIGNALS FROM CAMERAS & DOCUMENTS", [
        ("Fire & Smoke Detection", "YOLO ENSEMBLE · NMS"),
        ("Workplace Monitoring", "INSIGHTFACE · FAISS"),
        ("EmotiSense", "DEEPFACE · EMOTION"),
        ("Document OCR", "PADDLEOCR · PYMUPDF"),
    ]),
    ("02", "REASON", "LLMs, RETRIEVAL & CONFIDENCE", [
        ("DeepBlue", "MEMORY → TOOL → LLM"),
        ("Resume Analyzer", "LOCAL LLM · phi4-mini"),
        ("Candidate Transformer", "PROVENANCE · CONFIDENCE"),
    ]),
    ("03", "ACT", "TOOLS, SERVICES & INTERFACES", [
        ("FastAPI services", "DETECT · CATEGORIZE · EXTRACT"),
        ("Bots & voice", "TELEGRAM · TWILIO · LAMBDA"),
        ("Apps", "FLUTTER · REACT · VUE · EXPO"),
    ]),
]


def system_map(t):
    W, H = 1200, 500
    parts = [f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{t["bg"]}" stroke="{t["rule"]}"/>',
             f'<text x="40" y="48" {MONO} font-size="12" letter-spacing="3" fill="{t["accent"]}">AGENT LOOP</text>',
             f'<text x="{W-40}" y="48" text-anchor="end" {MONO} font-size="12" letter-spacing="3" fill="{t["muted"]}">PERCEIVE → REASON → ACT ↻</text>']
    col_x = [40, 440, 840]
    for ci, (num, name, sub, nodes) in enumerate(MAP):
        x = col_x[ci]
        parts.append(f'<text x="{x}" y="100" {MONO} font-size="13" fill="{t["accent"]}">{num}</text>')
        parts.append(f'<text x="{x+30}" y="102" {SANS} font-size="28" font-weight="900" class="h h{ci}">{name}</text>')
        parts.append(f'<text x="{x}" y="126" {MONO} font-size="10.5" letter-spacing="1.5" fill="{t["muted"]}">{esc(sub)}</text>')
        for ni, (title, stack) in enumerate(nodes):
            y = 146 + ni * 70
            parts.append(f'<rect x="{x}" y="{y}" width="320" height="56" rx="6" fill="{t["bg2"]}" stroke="{t["rule"]}"/>')
            parts.append(f'<rect x="{x}" y="{y}" width="3" height="56" fill="{t["accent"]}" class="pip" style="animation-delay:{(ci*4+ni)*0.35:.2f}s"/>')
            parts.append(f'<text x="{x+18}" y="{y+24}" {SANS} font-size="16" font-weight="700" fill="{t["ink"]}">{esc(title)}</text>')
            parts.append(f'<text x="{x+18}" y="{y+43}" {MONO} font-size="10.5" letter-spacing="1" fill="{t["muted"]}">{esc(stack)}</text>')
    # flow arrows between columns
    for x1 in (368, 768):
        for y in (210, 280):
            parts.append(f'<line x1="{x1}" y1="{y}" x2="{x1+56}" y2="{y}" stroke="{t["accent"]}" stroke-width="2" class="flow" marker-end="url(#ah)"/>')
    # feedback loop from ACT back to PERCEIVE
    parts.append(f'<path d="M1000 356 V450 H200 V424" fill="none" stroke="{t["accent"]}" stroke-width="2" class="flow" marker-end="url(#ah)"/>')
    parts.append(f'<rect x="452" y="438" width="296" height="24" fill="{t["bg"]}"/>')
    parts.append(f'<text x="600" y="455" text-anchor="middle" {MONO} font-size="11" letter-spacing="2" fill="{t["ink"]}">FEEDBACK ↻ OUTCOMES BECOME SIGNALS</text>')
    defs = f'<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="{t["accent"]}"/></marker>'
    style = (f'.h{{fill:{t["ink"]};animation:hl 6s infinite}}.h1{{animation-delay:2s}}.h2{{animation-delay:4s}}'
             f'@keyframes hl{{0%,26%{{fill:{t["accent"]}}}33%,100%{{fill:{t["ink"]}}}}}'
             '.flow{stroke-dasharray:6 6;animation:f 1s linear infinite}@keyframes f{to{stroke-dashoffset:-12}}'
             '.pip{animation:p 4.2s ease-in-out infinite}@keyframes p{0%,100%{opacity:.2}50%{opacity:1}}')
    return svg(W, H, "\n".join(parts), title="System map: perceive, reason, act", defs=defs, style=style)


# --------------------------------------------------------------------------- project cards
# nodes: key -> (x, y, label[, h]); a label starting with * is an output (accent-filled)
# edges: (a, b) elbow right->left, ("up", a, b) vertical from a's top to b's bottom, ("down", a, b)
CARDS = {
    "deepblue": dict(
        stage="02 / REASON", title="DeepBlue",
        desc=["Decides when it needs help. It checks its own",
              "memory first, and below a confidence threshold",
              "it calls web search and lets Gemini decide."],
        nodes={"q": (28, 218, "QUERY"), "e": (104, 218, "EMBED"), "f": (180, 218, "FAISS"),
               "t": (282, 268, "TAVILY"), "g": (365, 268, "GEMINI"), "l": (368, 182, "*LABEL")},
        edges=[("q", "e"), ("e", "f"), ("f", "l"), ("f", "t"), ("t", "g"), ("up", "g", "l")],
        notes=[(262, 190, "≥ 0.6"), (262, 316, "< 0.6 · TOOL CALL")],
        chips=["FASTAPI", "FAISS", "MINILM", "TAVILY", "GEMINI"]),
    "resume": dict(
        stage="02 / REASON", title="Resume Analyzer",
        desc=["Resumes in any format become clean JSON.",
              "Native text first, OCR only when it's needed,",
              "and a local LLM that stays warm between runs."],
        nodes={"i": (28, 226, "FILE"), "p": (110, 190, "PYMUPDF"), "o": (110, 262, "PADDLEOCR"),
               "m": (236, 226, "PHI4-MINI"), "j": (345, 226, "*JSON")},
        edges=[("i", "p"), ("i", "o"), ("p", "m"), ("o", "m"), ("m", "j")],
        notes=[(110, 316, "FALLBACK · LOW TEXT")],
        chips=["PYMUPDF", "PADDLEOCR", "OLLAMA", "PYTHON"]),
    "candidate": dict(
        stage="02 / REASON", title="Candidate Transformer",
        desc=["Many messy sources, one profile you can trust.",
              "Conflicts resolved by source priority, and",
              "every field keeps its origin and confidence."],
        nodes={"c": (28, 180, "CSV", 26), "a": (28, 212, "ATS", 26), "r": (28, 244, "PDF", 26), "n": (28, 276, "NOTES", 26),
               "p": (112, 229, "PARSE"), "z": (188, 229, "NORMALIZE"), "m": (291, 229, "MERGE"), "v": (367, 229, "*VALIDATE")},
        edges=[("c", "p"), ("a", "p"), ("r", "p"), ("n", "p"), ("p", "z"), ("z", "m"), ("m", "v")],
        notes=[(188, 288, "+ PROVENANCE · CONFIDENCE")],
        chips=["PYTHON", "PYDANTIC", "PROVENANCE", "CONFIG-DRIVEN"]),
    "firesmoke": dict(
        stage="01 / PERCEIVE", title="Fire & Smoke Detection",
        desc=["Two detectors, one answer. Separate YOLO",
              "models for fire and smoke run as an ensemble,",
              "merged with NMS and served for image and video."],
        nodes={"i": (28, 226, "FRAME"), "a": (106, 190, "FIRE YOLO"), "b": (106, 262, "SMOKE YOLO"),
               "n": (238, 226, "NMS"), "s": (302, 226, "*FASTAPI")},
        edges=[("i", "a"), ("i", "b"), ("a", "n"), ("b", "n"), ("n", "s")],
        notes=[(238, 288, "ENSEMBLE MERGE")],
        chips=["YOLO", "PYTORCH", "OPENCV", "FASTAPI"]),
    "workplace": dict(
        stage="01 / PERCEIVE", title="Workplace Monitoring",
        desc=["Knows who is where, and for how long. Faces",
              "are embedded with InsightFace, matched in",
              "FAISS and timed inside a zone you draw."],
        nodes={"c": (28, 246, "CAMERA"), "i": (111, 246, "INSIGHTFACE"), "f": (228, 246, "FAISS"),
               "r": (304, 186, "DRAWN ROI"), "d": (304, 246, "*DWELL TIME")},
        edges=[("c", "i"), ("i", "f"), ("f", "d"), ("down", "r", "d")],
        notes=[(111, 300, "FACE MEMORY · PER-ID TIMER")],
        chips=["INSIGHTFACE", "FAISS", "ONNX", "OPENCV"]),
    "emotisense": dict(
        stage="01 / PERCEIVE", title="EmotiSense",
        desc=["Reads the room. Emotion recognition on a",
              "classroom webcam feeds a live dashboard",
              "organized by department and section."],
        nodes={"w": (28, 226, "WEBCAM"), "d": (111, 226, "DEEPFACE"), "e": (207, 226, "7 EMOTIONS"),
               "b": (317, 226, "*DASHBOARD")},
        edges=[("w", "d"), ("d", "e"), ("e", "b")],
        notes=[(207, 288, "PER DEPT · PER SECTION")],
        chips=["DEEPFACE", "REACT", "CHART.JS", "TAILWIND"]),
}


def _node_geom(node):
    x, y, label = node[:3]
    h = node[3] if len(node) > 3 else 30
    w = len(label.lstrip("*")) * MONO_CHAR + 20
    return x, y, w, h


def card(t, spec):
    W, H = 480, 396
    parts = [f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12" fill="{t["bg"]}" stroke="{t["rule"]}"/>',
             f'<text x="28" y="44" {MONO} font-size="11" letter-spacing="2.5" fill="{t["accent"]}">{spec["stage"]}</text>',
             f'<text x="{W-28}" y="44" text-anchor="end" {MONO} font-size="11" letter-spacing="2" fill="{t["muted"]}">REPO ↗</text>',
             f'<text x="28" y="90" {SANS} font-size="28" font-weight="900" fill="{t["ink"]}">{esc(spec["title"])}</text>']
    for i, line in enumerate(spec["desc"]):
        parts.append(f'<text x="28" y="{124 + i*22}" {SANS} font-size="15" fill="{t["sub"]}">{esc(line)}</text>')

    geo = {k: _node_geom(v) for k, v in spec["nodes"].items()}
    for e in spec["edges"]:
        if e[0] in ("up", "down"):
            a, b = geo[e[1]], geo[e[2]]
            cx = a[0] + a[2] / 2
            y1, y2 = (a[1], b[1] + b[3]) if e[0] == "up" else (a[1] + a[3], b[1])
            d = f"M{cx:.1f} {y1} V{y2}"
        else:
            a, b = geo[e[0]], geo[e[1]]
            x1, y1 = a[0] + a[2], a[1] + a[3] / 2
            x2, y2 = b[0], b[1] + b[3] / 2
            mid = x1 + max(8, (x2 - x1) / 2)
            d = f"M{x1:.1f} {y1:.1f} H{mid:.1f} V{y2:.1f} H{x2 - 2:.1f}"
        parts.append(f'<path d="{d}" fill="none" stroke="{t["muted"]}" stroke-width="1.3" class="flow" marker-end="url(#ah)"/>')
    for k, node in spec["nodes"].items():
        x, y, w, h = geo[k]
        out = node[2].startswith("*")
        fill, stroke, color = (t["accent"], t["accent"], t["on_accent"]) if out else (t["bg2"], t["ink"], t["ink"])
        parts.append(f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h}" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
        parts.append(f'<text x="{x + w/2:.1f}" y="{y + h/2 + 4:.1f}" text-anchor="middle" {MONO} font-size="11" '
                     f'font-weight="{700 if out else 400}" fill="{color}">{esc(node[2].lstrip("*"))}</text>')
    for x, y, txt in spec["notes"]:
        parts.append(f'<text x="{x}" y="{y}" {MONO} font-size="9.5" letter-spacing="1.2" fill="{t["accent"]}">{esc(txt)}</text>')

    parts.append(f'<line x1="28" y1="334" x2="{W-28}" y2="334" stroke="{t["rule"]}"/>')
    cx = 28
    for chip in spec["chips"]:
        w = len(chip) * 7.0 + 20
        parts.append(f'<rect x="{cx}" y="350" width="{w:.1f}" height="24" rx="12" fill="none" stroke="{t["rule"]}"/>')
        parts.append(f'<text x="{cx + w/2:.1f}" y="366" text-anchor="middle" {MONO} font-size="10.5" letter-spacing="0.8" fill="{t["sub"]}">{esc(chip)}</text>')
        cx += w + 8
    assert cx <= W - 20, f"chips overflow on {spec['title']}"
    defs = f'<marker id="ah" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8z" fill="{t["muted"]}"/></marker>'
    style = ".flow{stroke-dasharray:4 4;animation:f 1.1s linear infinite}@keyframes f{to{stroke-dashoffset:-8}}"
    return svg(W, H, "\n".join(parts), title=spec["title"], defs=defs, style=style)


# --------------------------------------------------------------------------- toolbox
TOOLBOX = [
    ("VISION", ["YOLO", "InsightFace", "DeepFace", "PaddleOCR", "OpenCV", "PyTorch"]),
    ("LLMs & AGENTS", ["Gemini", "Ollama · phi4-mini", "sentence-transformers", "FAISS", "Tavily", "Pydantic"]),
    ("BACKEND & CLOUD", ["FastAPI", "Node · Express", "AWS Lambda", "DynamoDB", "Firebase · Supabase", "Twilio · Agora"]),
    ("APPS", ["React", "Vue 3", "Flutter", "React Native · Expo", "TypeScript", "Tailwind"]),
]


def toolbox(t):
    W, H = 1200, 330
    parts = [f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{t["bg"]}" stroke="{t["rule"]}"/>']
    for ci, (name, items) in enumerate(TOOLBOX):
        x = 40 + ci * 285
        parts.append(f'<text x="{x}" y="58" {MONO} font-size="12" fill="{t["accent"]}">0{ci+1}</text>')
        parts.append(f'<text x="{x+28}" y="59" {SANS} font-size="17" font-weight="900" letter-spacing="1" fill="{t["ink"]}">{esc(name)}</text>')
        parts.append(f'<rect x="{x}" y="74" width="255" height="2" fill="{t["ink"]}"/>')
        for i, item in enumerate(items):
            y = 108 + i * 34
            parts.append(f'<text x="{x}" y="{y}" {MONO} font-size="10" fill="{t["muted"]}">{i+1:02d}</text>')
            parts.append(f'<text x="{x+28}" y="{y}" {SANS} font-size="16" fill="{t["ink"]}">{esc(item)}</text>')
            if i < len(items) - 1:
                parts.append(f'<line x1="{x}" y1="{y+13}" x2="{x+255}" y2="{y+13}" stroke="{t["rule"]}"/>')
    return svg(W, H, "\n".join(parts), title="Toolbox")


# --------------------------------------------------------------------------- footer
def footer(t):
    body = f'''
<rect x="0" y="10" width="1200" height="2" fill="{t["ink"]}"/>
<text x="0" y="46" {MONO} font-size="12" letter-spacing="3" fill="{t["ink"]}">KAMAL JEYARAM</text>
<text x="600" y="46" text-anchor="middle" {MONO} font-size="12" letter-spacing="3" fill="{t["accent"]}">PERCEIVE → REASON → ACT ↻</text>
<text x="1200" y="46" text-anchor="end" {MONO} font-size="12" letter-spacing="3" fill="{t["muted"]}">END OF FILE</text>
<text x="0" y="74" {MONO} font-size="10" letter-spacing="2" fill="{t["muted"]}">EVERY GRAPHIC ON THIS PAGE IS GENERATED BY CODE IN /scripts</text>'''
    return svg(1200, 84, body, title="Footer")


# --------------------------------------------------------------------------- main
def main():
    ASSETS.mkdir(exist_ok=True)
    out = {}
    for mode, t in THEMES.items():
        out[f"banner-{mode}.svg"] = banner(t)
        out[f"map-{mode}.svg"] = system_map(t)
        out[f"toolbox-{mode}.svg"] = toolbox(t)
        out[f"footer-{mode}.svg"] = footer(t)
        for key, (word, tag) in HEADERS.items():
            out[f"h-{key}-{mode}.svg"] = header(t, word, tag)
        for key, spec in CARDS.items():
            out[f"card-{key}-{mode}.svg"] = card(t, spec)
    for name, content in out.items():
        (ASSETS / name).write_text(content, encoding="utf-8")
    print(f"wrote {len(out)} files to {ASSETS}")


if __name__ == "__main__":
    main()
