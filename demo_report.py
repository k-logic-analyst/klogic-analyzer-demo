# ═══════════════════════════════════════
# demo_report.py — Public-facing demo audit
#
# NOTE (REGOLA: declare limits before discovered):
# - demo_check() uses the SIMPLIFIED lexical matcher
#   for public CWE patterns. The production engine
#   performs deeper analysis (AST-level contracts,
#   severity ordering, vault-backed check_axioms).
# - PDF target: NC report_generator (K⚡ 6-sezioni)
#   — this IS the gig deliverable format.
# ═══════════════════════════════════════
import sys

sys.path.insert(0,
    "/data/data/com.termux/files/home/NEURAL-CORE/src")

from neural_core.core.axiom_engine import _trigger_matches
from demo_axioms import DEMO_AXIOMS


# ═══════════════════════════════════════
# CORE (fix): matching diretto su stringa
# ═══════════════════════════════════════

def _match_axioms(code_lower: str) -> list:
    """Applica trigger CWE-demo al codice lowercase."""
    violations = []
    for aid, ax in DEMO_AXIOMS.items():
        if _trigger_matches(ax["trigger"], code_lower):
            violations.append({
                "axiom_id": aid,
                "trigger": ax["trigger"],
                "check": ax["check"],
                "severity": ax["severity"],
                "proof": ax["proof"],
                "action": f"Verify: {ax['check']}",
            })
    return violations


def demo_check_code(code: str) -> list:
    """Audit DIRECT-ON-CODE (per test + uso diretto)."""
    return _match_axioms(code.lower())


def demo_check(source_path: str) -> list:
    """Audit FILE-BASED (wrapper)."""
    with open(source_path) as fp:
        code = fp.read()
    return demo_check_code(code)


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 \
             else "sample_input.py"
    print(f"── K⚡ Demo Audit: {target} ──")
    v = demo_check(target)
    sev_order = {"CRITICAL":0,"HIGH":1,"MEDIUM":2,"LOW":3}
    v.sort(key=lambda x: sev_order.get(x["severity"],4))
    for item in v:
        print(f"  [{item['severity']}] "
              f"{item['axiom_id']}: {item['action']}")
    print(f"\n{len(v)} contract violations detected "
          f"(public CWE-based demo vault)")   
