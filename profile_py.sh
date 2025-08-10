#!/usr/bin/env bash
SCRIPT="$1"
DURATION="${2:-30}"

PY=$(which python3)
echo "Using Python at: $PY"
$PY "$SCRIPT" &
PID=$!
echo "Started process PID $PID"
sleep 1

# Add Full Disk Access for terminal before running.
sudo py-spy dump --pid "$PID"
sudo py-spy record --pid "$PID" --output profile_${PID}.svg --nonblocking --rate 100 --duration "${DURATION}"
