#!/bin/bash
# run with `sudo ./uninstaller.sh`

MAIN_DIR=/usr/local/bin/
rm ${MAIN_DIR}spotify_muter ${MAIN_DIR}muter.py 
sed -i -e 's/Exec=spotify_muter/Exec=spotify/g' /usr/share/applications/spotify.desktop