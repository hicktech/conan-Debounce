from conans import ConanFile


class ParticlePackage(ConanFile):
    name = 'Debounce'
    version = '0fc7aa1'
    url = 'https://github.com/hicktech/conan-Debounce'
    repo_url = 'https://github.com/dwcares/debounce.git'
    generators = 'cmake'
    settings = []
    requires = []

    def package(self):
        self.copy('*.c*', dst='src')
        self.copy('*.h*', dst='include')

    def source(self):
        self.run(f'git clone {self.repo_url} .')
        self.run(f'git checkout {self.version}')

    def package_info(self):
        self.cpp_info.srcdirs = ['src']
