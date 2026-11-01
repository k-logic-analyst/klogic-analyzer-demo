import sys
from pathlib import Path
sys.path.insert(0, ".")

from demo_axioms import (DEMO_PASSPHRASE,
                         DEMO_AXIOMS)
from demo_report import demo_check, demo_check_code


def test_demo_passphrase_is_public():
    assert DEMO_PASSPHRASE == "demo-only-not-secret"


def test_five_demo_axioms():
    assert len(DEMO_AXIOMS) == 5


def test_no_axiom_id_from_production():
    """REGOLA_RISULTATO_SEGRETO: zero AXIOM_* IDs
    nel demo vault."""
    for aid in DEMO_AXIOMS:
        assert not aid.startswith("AXIOM_")
        assert aid.startswith("DEMO_")


def test_all_have_cwe_in_proof():
    for aid, ax in DEMO_AXIOMS.items():
        assert "CWE-" in ax["proof"], aid


def test_demo_check_detects_negative_price():
    code = "def f(price, discount):\n" \
           "    return price - (price * discount)"
    ids = [v["axiom_id"] for v in demo_check_code(code)]
    assert "DEMO_DISCOUNT_RANGE" in ids


def test_demo_check_detects_eval():
    code = "def run(u):\n    return eval(u)"
    ids = [v["axiom_id"] for v in demo_check_code(code)]
    assert "DEMO_EVAL_USAGE" in ids


def test_demo_check_clean_code():
    code = "def add(a, b):\n    return a + b"
    assert demo_check_code(code) == []   
