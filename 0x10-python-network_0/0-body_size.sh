#!/usr/bin/env bash
# cURL body size: task 0

curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
