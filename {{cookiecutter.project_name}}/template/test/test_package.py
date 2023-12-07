"""Tests for {{ cookiecutter.__package_name }}."""

from __future__ import annotations

import importlib.metadata

import {{ cookiecutter.__package_name }} as m


def test_version() -> None:
    """Test that the package defines a proper version."""
    assert importlib.metadata.version("{{ cookiecutter.__package_name }}") == m.__version__
