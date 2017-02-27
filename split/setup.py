from setuptools import setup

requires = [
    'pyramid'
]

setup(
    name='split_canister',
    install_requires=requires,
    entry_points="""
    [paste.app_factory]
    main = split_site:main"""
)