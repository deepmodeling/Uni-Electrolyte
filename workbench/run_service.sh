#!/bin/bash

export LAUNCHING_APPLICATION_NAME=retro-synthesis
#export LAUNCHING_APPLICATION_TOKEN=
export LAUNCHING_APPLICATION_OWNER=xiangs@dp.tech
export LAUNCHING_APPLICATION_VERSION=retro1228
#export LAUNCHING_ROOT=./local-debug
export LAUNCHING_ROOT=/app-dir
export LAUNCHING_API_BASE=https://launching.mlops.dp.tech
# export LAUNCHING_API_BASE=http://localhost:1024
export DEBUG_MODE=True
export DRY_RUN_MODE=False
export FAKE_USER=fake@dp.tech
export TMPDIR=/app-dir/tmp/
export LAUNCHING_JWT_PUBLIC_KEY=""
export REACT_VERSION=18.2.0
gunicorn --bind 0.0.0.0:50003 -w 4 -t 300 --chdir "/app" --preload app:server
