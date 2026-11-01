# ═══════════════════════════════════════
# demo_axioms.py — Public CWE-based demo vault
# Contents derived from PUBLIC CWE documentation
# (MITRE), NOT from the proprietary vault.
# Passphrase intentionally public.
# ═══════════════════════════════════════

DEMO_PASSPHRASE = "demo-only-not-secret"  # public by design

DEMO_AXIOMS = {
    "DEMO_DISCOUNT_RANGE": {
        "trigger": "discount applied to price",
        "check": "discount in [0,1] validated; result >= 0 and <= price",
        "proof": "CWE-20/CWE-682: unvalidated discount yields "
                 "negative prices (apply_discount(100,1.5)=-50)",
        "severity": "CRITICAL",
    },
    "DEMO_EVAL_USAGE": {
        "trigger": "eval() on untrusted input",
        "check": "use ast.literal_eval instead of eval",
        "proof": "CWE-95: eval executes arbitrary code",
        "severity": "CRITICAL",
    },
    "DEMO_SUBPROCESS_SHELL": {
        "trigger": "subprocess with shell=True",
        "check": "shell=False enforced; args as list",
        "proof": "CWE-78: OS command injection via shell",
        "severity": "CRITICAL",
    },
    "DEMO_HARDCODED_SECRET": {
        "trigger": "secret string literal in source",
        "check": "secrets loaded from environment/config",
        "proof": "CWE-798: hardcoded credentials leak",
        "severity": "HIGH",
    },
    "DEMO_DIVISION_GUARD": {
        "trigger": "division by variable denominator",
        "check": "denominator != 0 validated before division",
        "proof": "CWE-369: divide by zero crash/DoS",
        "severity": "HIGH",
    },
}


def build_demo_vault() -> dict:
    """Vault dict nel formato axiom_engine standard."""
    axioms = {}
    for aid, ax in DEMO_AXIOMS.items():
        axioms[aid] = {
            **ax,
            "immutable": True,
            "fonte": "public CWE (MITRE) - demo companion",
        }
    return {"axioms": axioms, "total": len(axioms)}
