# Daily 100 Content Method

**A systematic framework for high-frequency short-video content creation, adapted for AI-assisted workflows.**

> Turn "post 100 times a day" from a slogan into an operable SOP.
> Designed for bosses / founders building personal IP, employees running content matrices, and individual creators scaling output.

[中文文档](README.zh-CN.md) | [方法论详解](docs/methodology.md) | [口播模板](docs/templates.md)

---

## Already in Use

This method is already packaged and distributed as a **ClawHub skill** (WorkBuddy ecosystem):

- **Skill name:** 日更100条方法论 v1.0.0
- **Downloads:** 455+ (all-time)
- **Status:** In review
- **Install:** `openclaw skills install @heyusheng007-netizen/daily-100-methodology`

If you are a WorkBuddy/ClawHub user, install it directly from the marketplace. If not, this repository contains the same methodology in an open, LLM-friendly format.

---

## Why This Project Exists

Most small businesses know they should do short-video marketing, but:

- **Bosses don't know what to say** → no personal IP, no trust, all traffic depends on paid ads
- **Employees don't want to film** → no content matrix, one account = one point of failure
- **Creators can't sustain output** → 3 posts then quit, never reaching algorithm-critical mass

The **Daily 100 Content Method** answers one question with a numbers game:
> How do you produce enough *high-quality, on-brand* content to saturate the algorithm and build real trust?

This repo packages that method into **AI-ready prompt frameworks**, **copywriting templates**, and a **working example generator** — so any business can apply it with an LLM (ChatGPT, Claude, Codex, etc.) without hiring a content team.

---

## Core Concepts

| # | Strategy | What It Solves |
|---|----------|----------------|
| 1 | **High-Frequency Attack** (数量换概率) | Don't predict which post goes viral — cover uncertainty with volume |
| 2 | **Two-Line Narrative** (两线叙事) | Soft line (controversy/hooks) for traffic, hard line (craft/proof) for conversion |
| 3 | **Controversy Entry** (争议切入) | Piercing filter bubbles; discussion > agreement |
| 4 | **Matrix Thinking** (矩阵思维) | Boss IP → employee accounts → copy success, distributed trust network |
| 5 | **N+1 Innovation** | Be one step better than the industry standard, not cheaper |
| 6 | **SABCD Brand Catch** | Traffic from controversy must be caught by brand credibility |
| 7 | **Reverse Erosion Risk** (风险控制) | Know the limits of controversy before you use it |

**5 Copywriting Templates** — Anti-consensus, Story-hook, Methodology, Product-demo, Daily-vlog.

---

## Repository Structure

```
daily-100-content-method/
├── README.md                 # You are here
├── LICENSE                   # MIT
├── CONTRIBUTING.md           # How to contribute
├── docs/
│   ├── methodology.md        # Full methodology breakdown (7 strategies, adapted per role)
│   ├── templates.md          # 5 copywriting templates with word/time standards
│   └── industry-guide.md     # Cross-industry adaptation guide
├── prompts/                  # AI-ready prompt frameworks (copy-paste into any LLM)
│   ├── 01-industry-analysis.md
│   ├── 02-script-generator.md
│   ├── 03-persona-design.md
│   └── 04-matrix-plan.md
└── src/
    └── generate_script.py    # Tiny CLI: turn a topic JSON into a script draft
```

---

## Quick Start

### Option A — Use the prompts directly (no code needed)

Open any file in [`prompts/`](prompts/) and paste it into your favorite LLM:

```text
# 01-industry-analysis.md
I run a local decoration company in Chongqing, China.
My core selling points: transparent pricing, standard craftsmanship, in-house teams.
My personality: steady and professional.
→ Generate a two-line narrative strategy for my industry.
```

### Option B — Generate a script draft with Python

```bash
python src/generate_script.py --topic "半包比全包更贵" --type anti-consensus --duration 15
```

Output: a structured script draft (hook → body → call-to-action) ready for filming.

---

## Who Is This For

- **Bosses / founders** building a personal IP to convert trust into sales
- **Marketing teams** running an employee content matrix (designers, technicians, sales)
- **Individual creators** who want a repeatable, non-gimmicky output system
- **AI tooling developers** who build prompt/workflow libraries for marketing use cases

---

## Contributing

Contributions are welcome — new industry adaptations, prompt improvements, translation fixes, or generator features.

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

[MIT](LICENSE) © 2026 He Laoshi Private-Domain AI (何老师私域AI)

---

## Disclaimer

This project is an **independent methodology study** based on publicly available information (public videos, interviews, industry analysis). It is not affiliated with, endorsed by, or authorized by any company or individual mentioned. All data points marked 📌 are demo values meant to be replaced with real business data.
