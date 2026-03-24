"""Build a short analysis README.md for each data/ dataset folder."""

import csv
import math
import os
import re

DATA_ROOT = "data"
META_COLS = {
    "region_id",
    "region_name",
    "region_name_in_data",
    "region_ent_type",
}
SKIP_COLS = {"not_relevant"}

ENT_RANK = ["country", "province", "district", "dsd", "gnd"]
# Preferred level for per-field and outlier analysis (readable granularity)
ANALYSIS_LEVELS = ["district", "dsd", "gnd"]


def pretty(col: str) -> str:
    s = re.sub(r"[-_]+", " ", col).strip().title()
    for acr in ("nwsdb", "ro", "lpg"):
        s = re.sub(rf"\b{acr.title()}\b", acr.upper(), s)
    return s


def read_tsv(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def data_cols(headers: list[str]) -> list[str]:
    return [
        c for c in headers if c not in META_COLS and c.lower() not in SKIP_COLS
    ]


def fval(row: dict, col: str) -> float:
    try:
        return float(row.get(col) or 0)
    except ValueError:
        return 0.0


def row_total(row: dict, dcols: list[str]) -> float:
    if "total" in row and row.get("total"):
        try:
            return float(row["total"])
        except ValueError:
            pass
    return sum(fval(row, c) for c in dcols if c != "total")


def pct(part: float, whole: float) -> str:
    if not whole:
        return "—"
    return f"{part / whole * 100:.1f}%"


def title_from_path(folder: str) -> str:
    leaf = os.path.basename(folder)
    s = re.sub(r"[-_]+", " ", leaf).strip()
    return s.title()


def lowest_ent_type(rows: list[dict]) -> str:
    types = {r["region_ent_type"].lower() for r in rows}
    for et in reversed(ENT_RANK):
        if et in types:
            return et
    return "region"


def rows_at(rows: list[dict], ent_type: str) -> list[dict]:
    return [r for r in rows if r["region_ent_type"].lower() == ent_type]


def best_analysis_rows(rows: list[dict]) -> tuple[list[dict], str]:
    """Return rows at the best level for per-field analysis (district > dsd > gnd)."""
    for level in ANALYSIS_LEVELS:
        candidates = rows_at(rows, level)
        if len(candidates) >= 3:
            return candidates, level
    return [], ""


def mean_std(values: list[float]) -> tuple[float, float]:
    n = len(values)
    if n < 2:
        return (values[0] if values else 0.0), 0.0
    mu = sum(values) / n
    variance = sum((v - mu) ** 2 for v in values) / n
    return mu, math.sqrt(variance)


def build_readme(folder: str, rows: list[dict]) -> str:
    headers = list(rows[0].keys())
    dcols = data_cols(headers)
    cat_cols = [c for c in dcols if c != "total"]

    country_rows = rows_at(rows, "country")
    country = country_rows[0] if country_rows else None

    lines = []
    title = title_from_path(folder)
    lines += [f"# {title} — Sri Lanka Census 2024", ""]

    # ── National summary ──────────────────────────────────────────────────────
    lines += ["## National Summary", ""]
    nat_total = row_total(country, dcols) if country else 0.0

    if country:
        if "total" in dcols and nat_total:
            lines.append(f"**{int(nat_total):,}** total across Sri Lanka.")
            lines.append("")

        if cat_cols:
            cat_data = sorted(
                [(c, fval(country, c)) for c in cat_cols],
                key=lambda x: -x[1],
            )
            base = nat_total or sum(v for _, v in cat_data)

            lines += ["| Category | Count | Share |"]
            lines += ["|----------|------:|------:|"]
            for c, val in cat_data:
                lines.append(
                    f"| {pretty(c)} | {int(val):,} | {pct(val, base)} |"
                )
            lines.append("")

            top_col, top_val = cat_data[0]
            lines.append(
                f"> **{pct(top_val, base)}** of the total is accounted for"
                f" by **{pretty(top_col)}**."
            )
            lines.append("")
    else:
        lines += ["*(No national-level row available.)*", ""]

    # ── Per-field leaders ─────────────────────────────────────────────────────
    analysis_rows, analysis_level = best_analysis_rows(rows)

    if analysis_rows and cat_cols:
        level_label = analysis_level.title()
        lines += [f"## Highest & Lowest by {level_label}", ""]
        lines += [
            f"For each category, the {level_label} with the highest and"
            " lowest share (% of that region's total).",
            "",
        ]
        lines += [
            f"| Category | Highest {level_label} | Share"
            f" | Lowest {level_label} | Share |"
        ]
        lines += ["|----------|" + "---------|------:|" * 2]

        for c in cat_cols:
            shares = []
            for r in analysis_rows:
                rt = row_total(r, dcols)
                if rt:
                    shares.append((r, fval(r, c) / rt))

            if not shares:
                continue

            shares.sort(key=lambda x: -x[1])
            hi_row, hi_share = shares[0]
            lo_row, lo_share = shares[-1]
            lines.append(
                f"| {pretty(c)}"
                f" | {hi_row['region_name']} | {hi_share * 100:.1f}%"
                f" | {lo_row['region_name']} | {lo_share * 100:.1f}% |"
            )
        lines.append("")

    # ── Outlier analysis ──────────────────────────────────────────────────────
    if analysis_rows and cat_cols:
        # For each category, compute mean & std of share across analysis_rows.
        # Collect (z_score, region_name, col, share, direction) for significant outliers.
        outliers = []
        for c in cat_cols:
            shares = []
            for r in analysis_rows:
                rt = row_total(r, dcols)
                if rt:
                    shares.append((r, fval(r, c) / rt))
            if len(shares) < 3:
                continue
            values = [s for _, s in shares]
            mu, sd = mean_std(values)
            if sd == 0:
                continue
            for r, share in shares:
                z = (share - mu) / sd
                if abs(z) >= 2.0:
                    direction = "high" if z > 0 else "low"
                    outliers.append(
                        (abs(z), z, r["region_name"], c, share, direction, mu)
                    )

        if outliers:
            outliers.sort(key=lambda x: -x[0])
            lines += ["## Outliers", ""]
            lines += [
                f"Regions with an unusually high or low share of a category"
                f" (≥ 2 standard deviations from the {analysis_level} mean).",
                "",
            ]
            seen = set()
            shown = 0
            for abs_z, z, region, col, share, direction, mu in outliers:
                key = (region, col)
                if key in seen or shown >= 8:
                    continue
                seen.add(key)
                arrow = "🔺" if direction == "high" else "🔻"
                nat_avg = pct(mu, 1.0)
                lines.append(
                    f"- {arrow} **{region}** — {pretty(col)}:"
                    f" **{share * 100:.1f}%** vs {analysis_level} avg {nat_avg}"
                    f" (z = {z:+.1f})"
                )
                shown += 1
            lines.append("")

    # ── Coverage note ─────────────────────────────────────────────────────────
    lowest = lowest_ent_type(rows)
    n_lowest = len(rows_at(rows, lowest))
    lines += [
        "---",
        f"*Data covers **{len(rows):,}** rows down to **{lowest}** level"
        f" ({n_lowest:,} {lowest}s).*",
        "",
    ]

    return "\n".join(lines)


def main():
    for dirpath, _, filenames in os.walk(DATA_ROOT):
        if "data.tsv" not in filenames:
            continue
        tsv_path = os.path.join(dirpath, "data.tsv")
        rows = read_tsv(tsv_path)
        if not rows:
            continue
        content = build_readme(dirpath, rows)
        readme_path = os.path.join(dirpath, "README.md")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Wrote {readme_path}")


if __name__ == "__main__":
    main()
