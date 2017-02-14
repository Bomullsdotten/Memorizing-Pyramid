from setuptools import setup

requires = [
    'pyramid',
]

setup(name='pack',
      install_requires=requires,
      entry_points="""
      [paste.app_factory]
      main = pack:main
      """,
      )