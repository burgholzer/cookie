if(NOT TARGET ${PROJECT_NAME})
  file(GLOB_RECURSE HEADERS ${PROJECT_SOURCE_DIR}/include/*.hpp)

  # main project library
  add_library(${PROJECT_NAME} ${HEADERS} add.cpp)

  # set include directories
  target_include_directories(${PROJECT_NAME} PUBLIC ${PROJECT_SOURCE_DIR}/include
                                                    ${PROJECT_BINARY_DIR}/include)
  {%- if cookiecutter.namespace=='mqt' %}
  # link to the MQT::Core libraries
  target_link_libraries(${PROJECT_NAME} PUBLIC MQT::Core)
  {% endif -%}

  # add {{ cookiecutter.namespace|upper }} alias
  add_library({{ cookiecutter.namespace|upper }}::{{ cookiecutter.__project_slug}} ALIAS ${PROJECT_NAME})
endif()

if(BUILD_{{ cookiecutter.namespace|upper }}_{{ cookiecutter.__project_slug|upper }}_BINDINGS)
  add_subdirectory(python)
endif()
