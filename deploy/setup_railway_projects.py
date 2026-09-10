#!/usr/bin/env python3
"""Provision one isolated Railway project per person, each running its own
Genie container against its own Claude subscription.

Requires: `railway login` already completed once in this terminal/machine
(https://github.com/railwayapp/cli). Reads deploy/people.local.json (gitignored,
copy deploy/people.example.json and fill it in -- never paste real tokens
into chat or commit that file). Only "name" and "claude_oauth_token" are
required per person:
  - api_token: leave "" to auto-generate a random one (recommended)
  - book_brief: leave "" -- queue books later via POST /books instead
  - cf_api_token / cf_account_id: only needed if you want Cloudflare Workers
    AI as the image engine instead of the no-key default (FLUX.1-schnell)

Writes deploy/provisioned.local.json (gitignored) with each person's
project/service IDs, domain, and generated api_token -- that's what you
point their frontend instance at.

Usage:
    python deploy/setup_railway_projects.py [--repo OWNER/REPO] [--branch main]
"""
import argparse
import json
import secrets
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run_json(args, input_text=None):
    """Run a railway CLI command, return its parsed --json stdout."""
    proc = subprocess.run(
        ["railway", *args, "--json"],
        input=input_text,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        print(f"FAILED: railway {' '.join(args)}", file=sys.stderr)
        print(proc.stdout, file=sys.stderr)
        print(proc.stderr, file=sys.stderr)
        raise SystemExit(1)
    out = proc.stdout.strip()
    return json.loads(out) if out else {}


def set_var(project_id, service_id, key, value, skip_deploys=True):
    if not value:
        return
    args = ["variable", "set", key, "--stdin", "-p", project_id, "-s", service_id]
    if skip_deploys:
        args.append("--skip-deploys")
    run_json(args, input_text=value)


def provision_person(person, repo, branch):
    name = person["name"]
    print(f"\n=== {name} ===")

    print("creating project...")
    proj = run_json(["init", "--name", f"genie-{name}"])
    project_id = proj["projectId"] if "projectId" in proj else proj.get("id")

    print("creating service, connected to", repo, "...")
    svc = run_json(["add", "--repo", repo, "--branch", branch, "--service", name])
    service_id = svc["serviceId"] if "serviceId" in svc else svc.get("id")

    print("attaching /data volume...")
    run_json(["volume", "add", "--service", service_id, "-p", project_id,
              "--mount-path", "/data"])

    api_token = person.get("api_token") or secrets.token_hex(24)

    print("setting variables...")
    set_var(project_id, service_id, "CLAUDE_CODE_OAUTH_TOKEN", person["claude_oauth_token"])
    set_var(project_id, service_id, "API_TOKEN", api_token)
    # BOOK_BRIEF is optional now (queue-based, see RAILWAY_DEPLOY.md 3b) --
    # only set it if this person's config still supplies one, as a first book.
    set_var(project_id, service_id, "BOOK_BRIEF", person.get("book_brief", ""))
    set_var(project_id, service_id, "CF_API_TOKEN", person.get("cf_api_token", ""))
    set_var(project_id, service_id, "CF_ACCOUNT_ID", person.get("cf_account_id", ""),
            skip_deploys=False)  # last one: let this deploy trigger

    print("generating a public domain for the API...")
    dom = run_json(["domain", "--service", service_id, "--project", project_id])
    domain = dom.get("domain") or dom.get("url") or "(check 'railway domain list' -- unexpected response shape)"

    print(f"done: {name} -> project {project_id}, service {service_id}")
    return {"name": name, "project_id": project_id, "service_id": service_id,
            "api_token": api_token, "domain": domain}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default="AkoredeAzeez/kdp-bomber")
    parser.add_argument("--branch", default="main")
    args = parser.parse_args()

    people_file = HERE / "people.local.json"
    if not people_file.exists():
        print(f"Missing {people_file}.")
        print(f"Copy {HERE / 'people.example.json'} to people.local.json and fill it in first.")
        raise SystemExit(1)

    people = json.loads(people_file.read_text())
    results = [provision_person(person, args.repo, args.branch) for person in people]

    out_file = HERE / "provisioned.local.json"
    out_file.write_text(json.dumps(results, indent=2))

    print(f"\nProvisioned {len(results)} project(s). Details (including API tokens) saved to {out_file}.")
    print("\n%-12s %-40s %s" % ("name", "domain", "api_token"))
    for r in results:
        print("%-12s %-40s %s" % (r["name"], r["domain"], r["api_token"]))
    print("\nEach frontend instance should point at its person's domain and send")
    print("Authorization: Bearer <that person's api_token>. Check a service with:")
    print("  railway status -p <project_id>")
    print("  railway logs -s <service_id> -p <project_id>")


if __name__ == "__main__":
    main()
