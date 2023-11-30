#!/bin/bash
# advanced task 100+1
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
