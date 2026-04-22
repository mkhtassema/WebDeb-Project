#!/bin/bash
# Start Angular frontend
cd "$(dirname "$0")/filmspace_frontend"
ng serve --port 4200 --open
