"""Tests for {{ cookiecutter.__package_name }}._core."""

from __future__ import annotations

import {{ cookiecutter.__package_name }}._core as m


def test_add() -> None:
    """Test that add() works."""
    assert m.add(2, 3) == 5


def test_subtract() -> None:
    """Test that subtract() works."""
    assert m.subtract(7, 5) == 2
