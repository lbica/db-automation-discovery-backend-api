from setuptools import setup, find_packages

setup(
    name="dbad-backend-api",
    version="0.1.0",
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
