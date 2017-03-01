from setuptools import setup

requires = [
    'pyramid',
    'passlib'
]

setup(
    name='users',
    install_requires=requires,
    entry_points="""
    [paste.app_factory]
    main = logsite:main"""
)