# sample_input.py
# K⚡ KLogicAnalyst — Demo Target
# Intentional bugs for showcase analysis
# fiverr.com/k_logic_analyst

import subprocess
import os


def calcola_sconto_malato(prezzo, percentuale):
    """
    BUG: percentuale non normalizzata.
    CWE-20/CWE-682 (unvalidated discount) violato.
    calcola_sconto_malato(100, 1.5) = -50.0
    """
    if percentuale > 100:
        return 0
    return prezzo * (1 - percentuale)


def esegui_comando(cmd):
    """
    BUG: shell=True injection risk.
    CWE-78 (shell injection) violato.
    CWE-78: OS Command Injection.
    """
    subprocess.call(cmd, shell=True)


def eval_espressione(expr):
    """
    BUG: eval() usage.
    CWE-95 (eval on untrusted input) violato.
    OWASP A03:2021 + CWE-95.
    """
    return eval(expr)


def divide(a, b):
    """
    BUG: divisione per zero non protetta.
    CWE-369 (division by zero) violato.
    """
    return a / b


def applica_sconto(price, discount):
    """
    BUG: discount non validato 0.0-1.0.
    CWE-20/CWE-682 (unvalidated discount) violato.
    apply_discount(100, -0.5) = 150.0
    apply_discount(100,  1.5) = -50.0
    """
    return price - (price * discount)


def get_user_file(file_path):
    """
    BUG: path traversal non protetto.
    CWE-22 (path traversal) violato.
    OWASP A01:2021 + CWE-22.
    """
    with open(file_path, 'r') as f:
        return f.read()


def login(username, password):
    """
    BUG: hardcoded password.
    CWE-798 (hardcoded secret) violato.
    OWASP A07:2021 + CWE-798.
    """
    hardcoded_password = "admin123"
    return password == hardcoded_password


def process_data(data):
    """
    BUG: except silenzioso senza log.
    silent exception (logging missing) violato.
    """
    try:
        result = int(data)
        return result * 2
    except Exception:
        pass


# PROOF MATEMATICA CORE
# calcola_sconto_malato(100, 1.5) = -50.0
# CWE-20/CWE-682 (unvalidated discount) + CWE-20 (range validation) violati
if __name__ == "__main__":
    print("K⚡ KLogicAnalyst — Sample Input")
    print("Bug intenzionali per demo analisi")
    print(f"calcola_sconto_malato(100, 1.5) = "
          f"{calcola_sconto_malato(100, 1.5)}")
    print(f"applica_sconto(100, 1.5) = "
          f"{applica_sconto(100, 1.5)}")
