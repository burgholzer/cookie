---
layout: page
title: Compiled packaging
permalink: /guides/packaging-compiled/
nav_order: 6
parent: Topical Guides
---

{% include toc.html %}

# Packaging Compiled Projects

There are a variety of ways to package compiled projects. In the past, the only
way to do it was to use setuptools/distutils, which required using lots of
fragile internals - distutils was intended primarily to compile CPython, and
setuptools tried to stay away from changing the compile portions except as
required. Now, however, we have several very nice options for compiled packages!

The most exciting developments have been new native build backends:

- [scikit-build-core][]: Builds C/C++/Fortran using CMake.
- [meson-python][]: Builds C/C++/Fortran using Meson.
- [maturin][]: Builds Rust using Cargo. Written entirely in Rust!
- [enscons][]: Builds C/C++ using SCONs. (Aging now, but this was the first
  native backend!)

{: .note }

You should be familiar with [packing a pure Python
project]({% link pages/guides/packaging_compiled.md %}) - the metadata
configuration is the same.

There are also classic setuptools plugins:

- [scikit-build][]: Builds C/C++/Fortran using CMake.
- [setuptools-rust][]: Builds Rust using Cargo.

{: .important }

If you have a really complex build, the newer native build backends might not
support your use case yet, but if that's the case, ask - development is driven
by community needs. The older, more fragile setuptools based plugins are still a
bit more flexible if you really need that flexibility for a feature not yet
implemented in the native backends.

## pyproject.toml: build-system

{% include rr.html id="PY001" %} Packages must have a `pyproject.toml` file
{% include rr.html id="PP001" %} that selects the backend:

<div class="skhep-bar d-flex m-2" style="justify-content:center;">
  <button class="skhep-bar-item scikitbuild-btn btn m-2 btn-purple" onclick="openTab('scikitbuild')">Scikit-build-core</button>
  <button class="skhep-bar-item mesonpython-btn btn m-2" onclick="openTab('mesonpython')">Meson-python</button>
  <button class="skhep-bar-item maturin-btn btn m-2" onclick="openTab('maturin')">Maturin</button>
</div>

<div class="skhep-tab scikitbuild-tab" markdown="1">
```toml
[build-system]
requires = ["scikit-build-core"]
build-backend = "scikit_build_core.build"
```
</div>
<div class="skhep-tab mesonpython-tab" markdown="1" style="display:none;">
```toml
[build-system]
requires = ["meson-python"]
build-backend = "mesonpy"
```
</div>
<div class="skhep-tab maturin-tab" markdown="1" style="display:none;">
```toml
[build-system]
requires = ["maturin"]
build-backend = "maturin"
```
</div>

{% include pyproject.md %}

## Backend specific files

<div class="skhep-bar d-flex m-2" style="justify-content:center;">
  <button class="skhep-bar-item scikitbuild-btn btn m-2 btn-purple" onclick="openTab('scikitbuild')">Scikit-build-core</button>
  <button class="skhep-bar-item mesonpython-btn btn m-2" onclick="openTab('mesonpython')">Meson-python</button>
  <button class="skhep-bar-item maturin-btn btn m-2" onclick="openTab('maturin')">Maturin</button>
</div>

<div class="skhep-tab scikitbuild-tab" markdown="1">
```toml
[build-system]
requires = ["scikit-build-core"]
build-backend = "scikit_build_core.build"
```
</div>
<div class="skhep-tab mesonpython-tab" markdown="1" style="display:none;">
```toml
[build-system]
requires = ["meson-python"]
build-backend = "mesonpy"
```
</div>
<div class="skhep-tab maturin-tab" markdown="1" style="display:none;">
```toml
[build-system]
requires = ["maturin"]
build-backend = "maturin"
```
</div>

## Example compiled file

## Package structure

## Versioning

## Including/excluding files in the SDist

## Distributing

Unlike pure Python, you'll need to build redistributable wheels for each
platform and supported Python version if you want to avoid compilation on the
user's system.

<!-- prettier-ignore-start -->


[scikit-build-core]: https://scikit-build-core.readthedocs.io
[scikit-build]: https://scikit-build.readthedocs.io
[meson-python]: https://meson-python.readthedocs.io
[cmake]: https://cmake.org
[meson]: https://mesonbuild.com
[enscons]: https://pypi.org/project/enscons
[scons]: https://scons.org/
[setuptools-rust]: https://setuptools-rust.readthedocs.io/en/latest/
[maturin]: https://www.maturin.rs

<!-- prettier-ignore-end -->

<script src="{% link assets/js/tabs.js %}"></script>
