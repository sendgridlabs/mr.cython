from setuptools import setup
import sys

version = '1.0'

install_requires = [
    'setuptools',
    'zc.buildout',
]

tests_require = [
]

extra = {}


def get_text_from_file(fn):
    text = open(fn, 'rb').read()
    if sys.version_info >= (2, 6):
        return text.decode('utf-8')
    return text


setup(name='mr.cython',
      version=version,
      description="A zc.buildout extension to befriend mr.developer"
                  " and Cython.",
      long_description=get_text_from_file("README.rst") + "\n\n",
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Buildout",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='Alexander V. Nikolaev',
      author_email='avn@daemon.hole.ru',
      url='http://github.com/sendgridlabs/mr.cython',
      license='BSD',
      packages=['mr', 'mr.cython'],
      namespace_packages=['mr'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points="""
      [zc.buildout.extension]
      default = mr.cython:extension
      """,
      **extra
      )
