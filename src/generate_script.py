#!/usr/bin/env python3
"""
Daily 100 Content Method — Script Draft Generator

A dependency-free CLI that turns a topic + script type + duration into a
structured short-video script draft (hook → body → call-to-action), following
the word-count/time standards defined in docs/templates.md.

Usage:
    python generate_script.py --topic "半包比全包更贵" --type anti-consensus --duration 15
    python generate_script.py --topic "水电走线标准" --type product-demo --duration 30 --lang zh
    python generate_script.py --list-types
"""

import argparse
import json
import sys

VERSION = "1.0.0"

# Word-count / time standards (normal speaking speed: 3-4 chars/second)
DURATION_STANDARDS = {
    "15": {"min": 40, "max": 60, "types": ["anti-consensus", "vlog"]},
    "30": {"min": 90, "max": 120, "types": ["product-demo", "reveal"]},
    "60": {"min": 180, "max": 240, "types": ["story", "methodology"]},
    "90": {"min": 270, "max": 360, "types": ["methodology"]},
}

SCRIPT_TYPES = {
    "anti-consensus": {
        "label": "反共识型",
        "en": "Anti-consensus",
        "hook": "很多人都不相信，但这是真的——",
        "cta": "你信吗？评论区聊聊。",
    },
    "story": {
        "label": "故事悬念型",
        "en": "Story-hook",
        "hook": "这件事我从来没跟外人讲过——",
        "cta": "看完这个故事，你也许会有启发。",
    },
    "methodology": {
        "label": "方法论型",
        "en": "Methodology",
        "hook": "这行真正的玩法，没人愿意公开讲——",
        "cta": "记住这三点，少走三年弯路。关注我，持续讲真话。",
    },
    "product-demo": {
        "label": "产品展示型",
        "en": "Product-demo",
        "hook": "来，看一个东西——",
        "cta": "这就是标准。你觉得值不值？",
    },
    "reveal": {
        "label": "揭秘型",
        "en": "Reveal",
        "hook": "这行的秘密，知道的人不多——",
        "cta": "知道这个，你就不会再被坑了。",
    },
    "vlog": {
        "label": "日常随记型",
        "en": "Daily-vlog",
        "hook": None,
        "cta": None,
    },
}


def build_script(topic: str, script_type: str, duration: str, target_words: int) -> dict:
    """Assemble a structured script draft from a topic."""
    spec = SCRIPT_TYPES[script_type]
    lines = []

    # Fixed scaffold length (hook prefix + CTA), so we know the budget left for the body.
    fixed = len(spec["hook"] or "") + len(spec["cta"] or "")
    body_budget = max(target_words - fixed, 20)

    if spec["hook"]:
        lines.append({"role": "hook", "text": f"{spec['hook']}{topic}"})
        lines.append(
            {
                "role": "body",
                "text": f"（正文：围绕「{topic}」展开，建议{body_budget}字左右，放具体证据或案例）",
            }
        )
        if spec["cta"]:
            lines.append({"role": "cta", "text": spec["cta"]})
    else:
        # vlog type: one sentence + one scene
        lines.append(
            {
                "role": "scene",
                "text": f"{topic}（一句话 + 一个画面，{body_budget}字以内，真实就好）",
            }
        )

    # Word count judges the scaffold skeleton only; the real body is filled by the creator.
    total = len(topic) + fixed
    return {
        "topic": topic,
        "type": script_type,
        "type_label": spec["label"],
        "duration": f"{duration}秒",
        "target_words": target_words,
        "body_budget": body_budget,
        "skeleton_words": total,
        "standard_ok": body_budget >= 20,
        "structure": lines,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a short-video script draft using the Daily 100 Content Method."
    )
    parser.add_argument("--topic", help="Your topic, e.g. '半包比全包更贵'")
    parser.add_argument(
        "--type",
        default="anti-consensus",
        choices=sorted(SCRIPT_TYPES.keys()),
        help="Script type (see --list-types).",
    )
    parser.add_argument(
        "--duration",
        default="15",
        choices=sorted(DURATION_STANDARDS.keys()),
        help="Target duration in seconds. Default 15.",
    )
    parser.add_argument(
        "--lang",
        default="zh",
        choices=["zh", "en"],
        help="Output language for structural text. Script body stays in your topic's language.",
    )
    parser.add_argument("--list-types", action="store_true", help="List supported script types and exit.")
    parser.add_argument("--json", action="store_true", help="Output as JSON (machine-readable).")

    args = parser.parse_args()

    if args.list_types:
        for key, spec in SCRIPT_TYPES.items():
            print(f"{key:18s} {spec['label']} / {spec['en']}")
        return 0

    if not args.topic:
        parser.error("--topic is required (or use --list-types).")

    standard = DURATION_STANDARDS[args.duration]
    target_words = (standard["min"] + standard["max"]) // 2
    script = build_script(args.topic, args.type, args.duration, target_words)

    if args.json:
        print(json.dumps(script, ensure_ascii=False, indent=2))
        return 0

    print(f"📱 {script['duration']} · {script['type_label']} · 目标{target_words}字")
    print("=" * 48)
    for line in script["structure"]:
        role = line["role"].upper()
        print(f"[{role}] {line['text']}")
    print("=" * 48)
    print(f"骨架字数: {script['skeleton_words']} · 正文预算: {script['body_budget']}字 · 时长标准: {'✅' if script['standard_ok'] else '⚠️ 建议换更长时长'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
