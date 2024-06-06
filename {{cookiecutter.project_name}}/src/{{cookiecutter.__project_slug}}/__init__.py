"""
Copyright (c) {{ cookiecutter.__year }} Chair for Design Automation, Technical University of Munich, Germany. All rights reserved.

{{ cookiecutter.project_name }}: {{ cookiecutter.project_short_description }}
"""

from __future__ import annotations

{%- if cookiecutter.backend in ["hatch", "skbuild"] %}

from ._version import version as __version__

{%- else %}

__version__ = "0.1.0"

{%- endif %}

__all__ = ["__version__"]
