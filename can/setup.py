from setuptools import setup

requires = [
    'pyramid'
]

setup(
    name='canister',
    install_requires=requires,
    hooks="""
    [paste.app_factory]
    main = canned:main"""
)