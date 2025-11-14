from setuptools import setup, find_packages

setup(
    name="Db Automation Discovery Backend API",
    version="0.1.0",
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "databases",
        "psycopg2-binary"
    ],
    entry_points={
        "console_scripts": [
            "dbad-backend-api=run_server:main",
        ]
    },
)
