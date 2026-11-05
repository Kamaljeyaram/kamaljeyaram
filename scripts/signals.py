"""Live profile data: renders the Signals card and refreshes the README's
"recently shipped" block. Runs daily in GitHub Actions (stdlib only).

    python scripts/signals.py --out dist --readme README.md

Uses GITHUB_TOKEN when present (needed for the contributions count).
"""
import argparse
import datetime as dt
import json
import os
import re
import urllib.request
from pathlib import Path

from theme import MONO, SANS, THEMES, esc, svg

USER = os.environ.get("PROFILE_USER", "Kamaljeyaram")
TOKEN = os.environ.get("GITHUB_TOKEN")


def api(url, payload=None):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-signals"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    data = json.dumps(payload).encode() if payload is not None else None
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers), timeout=30) as r:
        return json.load(r)


def collect():
    repos = [r for r in api(f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed")
             if not r["fork"] and r["size"] > 0 and r["name"].lower() != USER.lower()]
    langs = {}
    for r in repos:
        for lang, n in api(r["languages_url"]).items():
            langs[lang] = langs.get(lang, 0) + n
    contributions = None
    if TOKEN:
        try:
            q = 'query($u:String!){user(login:$u){contributionsCollection{contributionCalendar{totalContributions}}}}'
            res = api("https://api.github.com/graphql", {"query": q, "variables": {"u": USER}})
            contributions = res["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
        except Exception as exc:  # keep the card rendering even if GraphQL is unavailable
            print("contributions unavailable:", exc)
    since = api(f"https://api.github.com/users/{USER}")["created_at"][:4]
    return {
        "since": since,
        "repos": repos,
        "langs": sorted(langs.items(), key=lambda kv: -kv[1]),
        "stars": sum(r["stargazers_count"] for r in repos),
        "contributions": contributions,
    }


def card(t, d, today):
    W, H = 1200, 330
    total = sum(n for _, n in d["langs"]) or 1
    top = d["langs"][:6]
    other = total - sum(n for _, n in top)
    segments = [(name, n) for name, n in top] + ([("Other", other)] if other > 0 else [])

    stats = [
        (f'{d["contributions"]:,}', "CONTRIBUTIONS · 12 MO") if d["contributions"] is not None
        else (d["since"], "BUILDING SINCE"),
        (str(len(d["repos"])), "ORIGINAL REPOS"),
        (str(len(d["langs"])), "LANGUAGES IN USE"),
        (str(d["stars"]), "STARS EARNED"),
    ]
    parts = [f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{t["bg"]}" stroke="{t["rule"]}"/>',
             f'<text x="40" y="48" {MONO} font-size="12" letter-spacing="3" fill="{t["accent"]}">LIVE FROM THE GITHUB API</text>',
             f'<text x="{W-40}" y="48" text-anchor="end" {MONO} font-size="12" letter-spacing="3" fill="{t["muted"]}">UPDATED {today:%d %b %Y}</text>']
    for i, (value, label) in enumerate(stats):
        x = 40 + i * 285
        if i:
            parts.append(f'<line x1="{x-24}" y1="78" x2="{x-24}" y2="160" stroke="{t["rule"]}"/>')
        parts.append(f'<text x="{x}" y="132" {SANS} font-size="60" font-weight="900" fill="{t["ink"]}">{esc(value)}</text>')
        parts.append(f'<text x="{x}" y="158" {MONO} font-size="11" letter-spacing="2" fill="{t["muted"]}">{esc(label)}</text>')

    parts.append(f'<text x="40" y="208" {MONO} font-size="11" letter-spacing="2" fill="{t["ink"]}">CODE BY LANGUAGE</text>')
    x, bar_w = 40.0, W - 80
    for i, (name, n) in enumerate(segments):
        w = bar_w * n / total
        parts.append(f'<rect x="{x:.1f}" y="222" width="{max(w - 2, 1):.1f}" height="16" fill="{t["lang"][i % len(t["lang"])]}"/>')
        x += w
    lx = 40
    for i, (name, n) in enumerate(segments):
        label = f"{name} {100 * n / total:.1f}%"
        parts.append(f'<rect x="{lx}" y="266" width="10" height="10" fill="{t["lang"][i % len(t["lang"])]}" stroke="{t["rule"]}"/>')
        parts.append(f'<text x="{lx + 18}" y="276" {MONO} font-size="12" fill="{t["sub"]}">{esc(label)}</text>')
        lx += 18 + len(label) * 7.3 + 26
    latest = d["repos"][0] if d["repos"] else None
    if latest:
        pushed = dt.datetime.fromisoformat(latest["pushed_at"].replace("Z", "+00:00"))
        parts.append(f'<text x="40" y="306" {MONO} font-size="10.5" letter-spacing="1.5" fill="{t["muted"]}">'
                     f'LAST SHIPPED → {esc(latest["name"].upper())} · {pushed:%d %b %Y}</text>')
    return svg(W, H, "\n".join(parts), title="Signals: live GitHub stats")


def update_readme(path, d):
    readme = Path(path)
    text = readme.read_text(encoding="utf-8")
    rows = ["| Repository | Language | Last push |", "|---|---|---|"]
    for r in d["repos"][:5]:
        pushed = dt.datetime.fromisoformat(r["pushed_at"].replace("Z", "+00:00"))
        desc = f" — {r['description']}" if r.get("description") else ""
        rows.append(f"| [{r['name']}]({r['html_url']}){desc} | {r['language'] or '—'} | {pushed:%b %Y} |")
    block = "<!-- RECENT:START -->\n" + "\n".join(rows) + "\n<!-- RECENT:END -->"
    new = re.sub(r"<!-- RECENT:START -->.*?<!-- RECENT:END -->", block, text, flags=re.S)
    if new != text:
        readme.write_text(new, encoding="utf-8")
        print("README recent block updated")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="dist")
    ap.add_argument("--readme")
    args = ap.parse_args()
    d = collect()
    today = dt.datetime.now(dt.timezone.utc)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for mode, t in THEMES.items():
        (out / f"signals-{mode}.svg").write_text(card(t, d, today), encoding="utf-8")
    if args.readme:
        update_readme(args.readme, d)
    print(f"signals: {len(d['repos'])} repos, {len(d['langs'])} languages, contributions={d['contributions']}")


if __name__ == "__main__":
    main()
