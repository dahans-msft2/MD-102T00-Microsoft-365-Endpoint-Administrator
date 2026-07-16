"""
Split each flat Lab0X-*.md file in Instructions/Labs/ into a folder containing:
  introduction.md, exercise-1.md ... exercise-N.md, summary.md
Original flat file is removed after a successful split.
"""
import re
import shutil
from pathlib import Path

LABS_DIR = Path(r"c:\learn-pr\MD-102T00-Microsoft-365-Endpoint-Administrator\Instructions\Labs")

EXERCISE_RE = re.compile(r"^## Exercise (\d+): (.+)$", re.MULTILINE)
SUMMARY_RE = re.compile(r"^## Lab Summary\s*$", re.MULTILINE)
TITLE_RE = re.compile(r"^# (Lab \d+): (.+)$")


def split_lab(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    title_match = TITLE_RE.match(lines[0])
    if not title_match:
        raise ValueError(f"Could not find H1 lab title in {md_path}")
    lab_num_label = title_match.group(1)  # "Lab 01"
    lab_title = title_match.group(2)      # "Foundation -- Identity, enrollment, and Autopilot"
    full_title = f"{lab_num_label}: {lab_title}"

    ex_matches = list(EXERCISE_RE.finditer(text))
    summary_match = SUMMARY_RE.search(text)
    if not ex_matches:
        raise ValueError(f"No '## Exercise N:' headings found in {md_path}")
    if not summary_match:
        raise ValueError(f"No '## Lab Summary' heading found in {md_path}")

    # Intro = start of file up to first exercise heading, minus the original H1 line
    # (we regenerate the H1 ourselves so we control exact wording).
    intro_body = text[len(lines[0]):ex_matches[0].start()].strip("\n")

    exercises = []  # (num, title, body)
    for i, m in enumerate(ex_matches):
        num = int(m.group(1))
        ex_title = m.group(2).strip()
        start = m.end()
        end = ex_matches[i + 1].start() if i + 1 < len(ex_matches) else summary_match.start()
        body = text[start:end].strip("\n")
        exercises.append((num, ex_title, body))

    summary_body = text[summary_match.end():].strip("\n")

    slug = md_path.stem  # e.g. "Lab01-Foundation"
    out_dir = LABS_DIR / slug
    out_dir.mkdir(exist_ok=True)

    # Build nav helpers
    def ex_link(n, arrow_text):
        t = next(t for (num, t, _) in exercises if num == n)
        return f"[{arrow_text} Exercise {n}: {t}](exercise-{n}.md)"

    # introduction.md
    toc_lines = "\n".join(f"{n}. [Exercise {n}: {t}](exercise-{n}.md)" for (n, t, _) in exercises)
    intro_out = (
        f"# {full_title}\n\n"
        f"{intro_body}\n\n"
        f"---\n\n"
        f"## Exercises in this lab\n\n"
        f"{toc_lines}\n"
        f"{len(exercises) + 1}. [Lab summary](summary.md)\n\n"
        f"---\n\n"
        f"**Next:** {ex_link(1, '→')}\n"
    )
    (out_dir / "introduction.md").write_text(intro_out, encoding="utf-8")

    # exercise-N.md files
    for idx, (num, ex_title, body) in enumerate(exercises):
        nav_parts = []
        if idx == 0:
            nav_parts.append("**Previous:** [← Introduction](introduction.md)")
        else:
            prev_num = exercises[idx - 1][0]
            nav_parts.append(f"**Previous:** {ex_link(prev_num, '←')}")
        if idx + 1 < len(exercises):
            next_num = exercises[idx + 1][0]
            nav_parts.append(f"**Next:** {ex_link(next_num, '→')}")
        else:
            nav_parts.append("**Next:** [Lab summary →](summary.md)")

        ex_out = (
            f"# {lab_num_label}, Exercise {num}: {ex_title}\n\n"
            f"{body}\n\n"
            f"---\n\n"
            f"{' | '.join(nav_parts)}\n"
        )
        (out_dir / f"exercise-{num}.md").write_text(ex_out, encoding="utf-8")

    # summary.md
    last_num = exercises[-1][0]
    summary_out = (
        f"# {full_title} — Summary\n\n"
        f"{summary_body}\n\n"
        f"---\n\n"
        f"**Previous:** {ex_link(last_num, '←')}\n"
    )
    (out_dir / "summary.md").write_text(summary_out, encoding="utf-8")

    return out_dir, len(exercises)


def main():
    lab_files = sorted(LABS_DIR.glob("Lab0*.md"))
    for md_path in lab_files:
        out_dir, n = split_lab(md_path)
        print(f"{md_path.name} -> {out_dir.name}/ ({n} exercises + introduction.md + summary.md)")
        md_path.unlink()  # remove the original flat file


if __name__ == "__main__":
    main()
