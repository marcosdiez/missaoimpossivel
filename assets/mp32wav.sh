#!/bin/bash
set -e
if [[ -z "$1" ]]
then
    echo "USAGE: $0 MP3_FILE_TO_BECOME_WAV"
    exit 1
fi

echo ffmpeg -i "$1" "$(echo $1 |cut -d. -f1).wav"
ffmpeg -i "$1" "$(echo $1 |cut -d. -f1).wav"