from setuptools import setup, find_packages

setup(
    name='Scraper API',
    version='1.0',
    description='Google Finance Scraper and Web Server',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    extras_require={
        'tst': [
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