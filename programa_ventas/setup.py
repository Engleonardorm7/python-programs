from setuptools import setup


setup(
    name='ventas',
    version='0.1',
    py_modules=['ventas'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ventas=ventas:cli
    ''',
)