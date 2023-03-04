from setuptools import setup

setup(
    name='Scraper API',
    version='1.0',
    description='Google Finance Scraper and Web Server',
    packages=['backend'],
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    extras_require={
        'dev': [
            'pytest',
            'mypy',
            'coverage',
        ],
    },
    #entry_points={
    #    'console_scripts': [
    #        'mycommand = uvicorn main:app --port "8000" --host "0.0.0.0"',
    #    ],
    #},
)