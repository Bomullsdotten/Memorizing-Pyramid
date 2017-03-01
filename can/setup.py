from setuptools import setup

requires = [
    'pyramid',
]

setup(
    name='cannister',
    install_requires=requires,
    entry_points="""
    [paste.app_factory]
    main = cans:main"""
)