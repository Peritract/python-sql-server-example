# Connecting to MS SQL Server Databases with Python

## Connecting through Docker images (Linux)

Look at the folder examples.

## Connecting with `pyodbc` locally

### Setup and installation

- Run `brew install unixodbc` to get a tool required for installing drivers
- Install the [latest version](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver15) drivers & tools (currently 18)

```sh
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew install msodbcsql18 mssql-tools18
```

- Create an `.env` with the following keys

```sh
DB_HOST=XXXXXXXXXX
DB_PORT=1433
DB_NAME=XXXXXXXXXX
DB_USERNAME=XXXXXXXXXX
DB_PASSWORD=XXXXXXXXXX
DB_DRIVER=ODBC Driver 18 for SQL Server
```

- Replace and update values as needed
- Install all required libraries (`pyodbc` for definite, others as required)
- Run the code