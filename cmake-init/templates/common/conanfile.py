from conan import ConanFile


class Recipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps", "VirtualRunEnv"

    def layout(self):
        self.folders.generators = "conan"

    def requirements(self):{% if c %}{% if exe %}
        self.requires("hedley/15"){% end %}
        self.requires("json-c/0.16"){% else %}
        self.requires("fmt/10.0.0"){% end %}

    def build_requirements(self):{% if catch3 %}
        self.test_requires("catch2/3.3.2"){% else %}
        self.test_requires("catch2/2.13.10", options={"with_main": True}){% end %}
