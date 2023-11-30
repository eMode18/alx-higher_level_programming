#!/usr/bin/env bash
# cURL body size: task 0

curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
