#!/usr/bin/env python3
"""
NICHE FORMAT GATE - uapf-quality-gates (BOTH ENGINES, MANDATORY)
================================================================
Forces the routed niche's OWN validation checklist to be walked item by
item, with recorded evidence, before a phase or chapter may advance.
"The niche skill was followed" is replaced by an auditable answers file.

How it works:
  1. Reads the project's book_lock.md machine-readable classification
     (global rule 16) to find selected_skill=uapf-niche-<x>.
  2. Loads that niche's frameworks/<ID>/validation.json gate checklist.
  3. --init writes state/niche_gate_answers.json in the project with every
     checklist item set to null.
  4. The producing agent (Claude OR Codex) fills each item with
     status pass/fail/na + a one-line evidence note AS it verifies the
     work against the niche skill's formatting and architecture rules.
  5. `check` FAILS (exit 2) while any item in scope is null or fail.
     "na" requires evidence. No agent can advance a gate it has not
     actually walked.

Usage:
  python niche_gate.py <project_folder> --init
  python niche_gate.py <project_folder> [--phase GATE_2] [--json out.json]
"""
import argparse, glob, json, os, re, sys

def find_validation(repo_root, niche_skill):
    pats = os.path.join(repo_root, ".agents", "skills", niche_skill,
                        "frameworks", "*", "validation.json")
    hits = glob.glob(pats)
    return hits[0] if hits else None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--init", action="store_true")
    ap.add_argument("--phase", default="", help="only gate groups whose name contains this")
    ap.add_argument("--json")
    a = ap.parse_args()

    proj = os.path.abspath(a.project)
    lock = os.path.join(proj, "book_lock.md")
    if not os.path.exists(lock):
        for c in glob.glob(os.path.join(proj, "**", "book_lock.md"), recursive=True):
            lock = c; break
    if not os.path.exists(lock):
        sys.exit("FAIL: no book_lock.md found; run Phase 0 routing first (rule 16)")
    m = re.search(r"selected_skill=(uapf-niche-[\w-]+)", open(lock, encoding="utf-8").read())
    if not m:
        sys.exit("FAIL: book_lock.md has no machine-readable classification line (rule 16)")
    niche = m.group(1)

    here = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(here)))
    vpath = find_validation(repo_root, niche)
    if not vpath:
        sys.exit(f"FAIL: no validation.json for {niche}")
    v = json.load(open(vpath, encoding="utf-8"))
    gates = v.get("gates", {})

    ans_path = os.path.join(proj, "state", "niche_gate_answers.json")
    if a.init:
        os.makedirs(os.path.dirname(ans_path), exist_ok=True)
        existing = json.load(open(ans_path, encoding="utf-8")) if os.path.exists(ans_path) else {}
        tpl = {}
        for group, items in gates.items():
            tpl[group] = existing.get(group, {})
            for it in items:
                tpl[group].setdefault(it["id"], {"status": None, "evidence": ""})
        json.dump({"niche": niche, "framework": v.get("framework_id", ""),
                   "answers": tpl}, open(ans_path, "w", encoding="utf-8"), indent=1)
        n = sum(len(i) for i in gates.values())
        print(f"initialized {ans_path}: {n} checklist items for {niche} "
              f"({v.get('framework_id','')}). Fill each with status pass/fail/na + evidence.")
        return

    if not os.path.exists(ans_path):
        sys.exit(f"FAIL: {ans_path} missing; run --init and walk the checklist (niche {niche})")
    ans = json.load(open(ans_path, encoding="utf-8")).get("answers", {})

    missing, failed, weak_na, passed = [], [], [], 0
    for group, items in gates.items():
        if a.phase and a.phase.lower() not in group.lower():
            continue
        for it in items:
            rec = ans.get(group, {}).get(it["id"])
            st = (rec or {}).get("status")
            ev = ((rec or {}).get("evidence") or "").strip()
            if st == "pass":
                passed += 1
                continue
            if st == "na":
                if ev:
                    passed += 1
                else:
                    weak_na.append((group, it["id"]))
                continue
            if st == "fail":
                failed.append((group, it["id"], it.get("text", "")[:60]))
            else:
                missing.append((group, it["id"], it.get("text", "")[:60]))

    scope = a.phase or "ALL GATES"
    print(f"niche gate [{niche}] scope={scope}: {passed} passed")
    for g, i, t in failed[:10]:
        print(f"  FAIL {g}/{i}: {t}")
    for g, i, t in missing[:10]:
        print(f"  UNANSWERED {g}/{i}: {t}")
    for g, i in weak_na[:5]:
        print(f"  NA-WITHOUT-EVIDENCE {g}/{i}")
    if a.json:
        json.dump({"niche": niche, "passed": passed, "failed": failed,
                   "missing": missing}, open(a.json, "w", encoding="utf-8"), indent=1)
    if failed or missing or weak_na:
        print(f"VERDICT: FAIL ({len(failed)} failed, {len(missing)} unanswered, "
              f"{len(weak_na)} na-without-evidence). The niche's formatting law is "
              "not satisfied until every item is walked and evidenced.")
        sys.exit(2)
    print("VERDICT: PASS")

if __name__ == "__main__":
    main()
