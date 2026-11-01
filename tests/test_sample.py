from hypothesis import given, settings, strategies as st
import pytest

from sample_input import applica_sconto, calcola_sconto_malato

prices = st.floats(min_value=0.01, max_value=10_000,
                   allow_nan=False, allow_infinity=False)
valid_discounts = st.floats(min_value=0.0, max_value=1.0,
                            allow_nan=False, allow_infinity=False)
any_discounts = st.floats(min_value=-1.0, max_value=3.0,
                          allow_nan=False, allow_infinity=False)


@settings(max_examples=1000)
@given(price=prices, discount=valid_discounts)
def test_valid_discount_is_safe(price, discount):
    """Control: inside the intended range the function behaves."""
    assert 0 <= applica_sconto(price, discount) <= price


@pytest.mark.xfail(strict=True, raises=AssertionError,
    reason="Intentional demo bug: discount not validated in "
           "[0,1] - negative price possible (CWE-20/CWE-682)")
@settings(max_examples=1000)
@given(price=prices, discount=any_discounts)
def test_discount_never_negative(price, discount):
    """Contract: a discounted price must never be negative."""
    assert applica_sconto(price, discount) >= 0


@pytest.mark.xfail(strict=True, raises=AssertionError,
    reason="Intentional demo bug: negative discount increases "
           "the price (CWE-20/CWE-682)")
@settings(max_examples=1000)
@given(price=prices, discount=any_discounts)
def test_discount_never_raises_price(price, discount):
    """Contract: a discount must never increase the price."""
    assert applica_sconto(price, discount) <= price


@pytest.mark.xfail(strict=True, raises=AssertionError,
    reason="Intentional demo bug: same raw formula, no percent "
           "normalisation (CWE-20/CWE-682)")
@settings(max_examples=1000)
@given(price=prices, discount=any_discounts)
def test_calcola_sconto_never_negative(price, discount):
    assert calcola_sconto_malato(price, discount) >= 0
