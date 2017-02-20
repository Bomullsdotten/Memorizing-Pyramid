from setuptools import setup

requires = {
    'pyramid',
}

setup(
    name='can',
    install_requires=requires,
    entry_points="""
    [paste.app_factory]
    main = canned:main
    """,
)