# set required cmake version
cmake_minimum_required(VERSION 3.19...3.27)

project(
  {{ cookiecutter.__package_name }}
  LANGUAGES CXX
  DESCRIPTION "{{ cookiecutter.project_short_description }}")

{% if cookiecutter.namespace=='mqt' -%}
set(BUILD_MQT_CORE_TESTS
    OFF
    CACHE BOOL "Build MQT Core tests")

include(FetchContent)
FetchContent_Declare(
  mqt-core
  GIT_REPOSITORY https://github.com/cda-tum/mqt-core.git
  GIT_TAG v2.0.0.post1)

FetchContent_MakeAvailable(mqt-core)
{% endif -%}

option(BUILD_{{ cookiecutter.namespace|upper }}_{{ cookiecutter.__project_slug|upper }}_BINDINGS "Build the {{ cookiecutter.__package_name }} Python bindings" OFF)
if(BUILD_{{ cookiecutter.namespace|upper }}_{{ cookiecutter.__project_slug|upper }}_BINDINGS)
  # ensure that the BINDINGS option is set
  set(BINDINGS
      ON
      CACHE BOOL "Enable settings related to Python bindings" FORCE)
  # cmake-lint: disable=C0103
  set(Python_FIND_VIRTUALENV
      FIRST
      CACHE STRING "Give precedence to virtualenvs when searching for Python")
  # cmake-lint: disable=C0103
  set(Python_ARTIFACTS_INTERACTIVE
      ON
      CACHE BOOL "Prevent multiple searches for Python and instead cache the results.")
  # top-level call to find Python
  find_package(
    Python 3.8 REQUIRED
    COMPONENTS Interpreter Development.Module
    OPTIONAL_COMPONENTS Development.SABIModule)
endif()

# add main library code
add_subdirectory(src)

# add test code
option(BUILD_{{ cookiecutter.namespace|upper }}_{{ cookiecutter.__project_slug|upper }}_TESTS "Also build tests for the {{ cookiecutter.project_name }} project" ON)
if(BUILD_{{ cookiecutter.namespace|upper }}_{{ cookiecutter.__project_slug|upper }}_TESTS)
  enable_testing()
  include(GoogleTest)
  add_subdirectory(test/cpp)
endif()
