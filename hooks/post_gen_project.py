"""Post generation hook to copy some files from the template to the project."""

import shutil

from pathlib import Path

backend = "{{ cookiecutter.backend }}"

Path("test").mkdir(parents=True, exist_ok=True)

# C++ specific
if backend == "skbuild":
    shutil.copy("template/.clang-tidy", ".")
    shutil.copy("template/.clang-format", ".")
    shutil.copy("template/.cmake-format.yaml", ".")
    shutil.copy("template/CMakeLists.txt", ".")

    shutil.copy("template/src/add.cpp", "src")
    shutil.copy("template/src/CMakeLists.txt", "src")

    include_dir = Path("include")
    include_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy("template/include/add.hpp", include_dir)

    python_dir = Path("src") / "python"
    python_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy("template/src/python/module.cpp", python_dir)
    shutil.copy("template/src/python/CMakeLists.txt", python_dir)

    test_dir = Path("test") / "cpp"
    test_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy("template/test/test_add.cpp", test_dir)
    shutil.copy("template/test/CMakeLists.txt", test_dir)

# Rust specific
if backend == "maturin":
    shutil.copy("template/Cargo.toml", ".")
    shutil.copy("template/src/lib.rs", "src")

# Python tests
if backend == "hatch":
    shutil.copy("template/test/test_package.py", "test")
else:
    test_dir = Path("test") / "python"
    test_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy("template/test/test_package.py", test_dir)
    shutil.copy("template/test/test_compiled.py", test_dir)

# delete the template folder
shutil.rmtree("template")
