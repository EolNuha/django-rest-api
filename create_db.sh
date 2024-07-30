#!/bin/bash
set -e

# Variables
DB_HOST="db"
DB_USER="sa"
DB_PASS="yourStrong(!)Password"
DB_NAME="Django_db"
SQL_QUERY="IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'$DB_NAME') CREATE DATABASE [$DB_NAME];"

# Execute the SQL script to create the database
/opt/mssql-tools/bin/sqlcmd -S $DB_HOST -U $DB_USER -P $DB_PASS -Q "$SQL_QUERY"

echo "Database $DB_NAME created successfully"
