## Setup

### Create virtual env

```
python -m pip venv .venv

```

### Activate the environment

```
.\.venv\Scripts\Activate

```
##### List installed packages

`pip list`

### Install Fast API


```
pip install fastapi[all]

```
or

```
pip install fastapi"uvicorn[standard]" --minimal fastapi

```

#### start the fastapi using ivcorn - for production use gunicorn
uvicorn app.main:app --reload --port 3001

##### for docs: Swagger
http://localhost:3001/docs

### Alembic setup (for schema evolution)

#### Installation

```
pip install alembic

```
```
alembic init alembic

```
**Configure alembic.ini**:
```
sqlalchemy.url = sqlite:///./data/dbad_repository.db

```
**Note: Remove the code from upgrade and downgrade methods in generated alembic version migration file.**

#### Stamp the current database (so Alembic knows it exists)

```
alembic stamp head

```

##### Alembic Create a Migration and apply the Migration

```
alembic revision --autogenerate -m "Change column to User"

alembic upgrade head


```



##### Workflow Summary

 - First-time run: Base.metadata.create_all(bind=engine) in main.py → creates DB + tables.

 - Future changes: Use Alembic migrations → keeps schema safe and versioned.

 - FastAPI uses DTOs (schemas.py) → ensures clean input/output.

 - SQLite DB stored in data/app.db.

 ### Build and new version of your package

  - CHange version in .toml or setup.py file e.g. 0.1.1 
  - Install build

  ```
 pip install build

  ```

 - After running build
 
  ```
 pip -m build

  ```

```

-m tells Python: “run the module named build as a script.”
build is the module that handles packaging.
So python -m build is equivalent to “run the build tool for this project.”

```

- Then install your new version into a virtual environment:

```
pip install --force-reinstall --no-cache-dir dist/dbad_backend_api-0.1.3-py3-none-any.whl

```


## Build

 ### How to build everything

```
 # 1. Install everything (once)
npm ci                # root + workspaces

# 2. Type-check the whole repo
npm run typecheck

# 3. Build the webview (Vite)
npm run build:webview-ui   # → vscode-extension/dist/webview

# 4. Build the VS Code extension (Webpack)
npm run build           # → vscode-extension/dist/extension.js + webview

# 5. Package for VS Marketplace
cd vscode-extension && npm run package

#Note:
 npm outdate - iti arata ce pachete din package.json au versiuni noi

```

