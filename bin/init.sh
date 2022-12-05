#!/bin/sh

sqlite3 ./var/wordleGame.db< ./share/wordlegameschema.sql
sqlite3 ./var/wordleUser.db< ./share/wordleuserschema.sql

python3 ./bin/copydata.py
python3  ./bin/redis_initialization.py