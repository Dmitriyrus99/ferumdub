#!/bin/bash
set -e

BENCH_FOLDER="${BENCH_FOLDER:-frappe-bench}"

if [ ! -d "$BENCH_FOLDER" ]; then
    /bootstrap.sh
fi

cd "$BENCH_FOLDER"
exec "$@"
