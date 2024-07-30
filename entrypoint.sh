#!/bin/bash
set -e

# Wait for the SQL Server to be available and create the database
/code/create_db.sh


# Execute the command passed to the docker run command
exec "$@"