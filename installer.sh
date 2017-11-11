#!/bin/bash
# This installer is meant to be run under sudo
# Does not install dependencies

MAIN_DIR=/usr/local/bin/
cp spotify_muter muter.py ${MAIN_DIR}
sed -i -e 's/Exec=spotify/Exec=spotify_muter/g' /usr/share/applications/spotify.desktop
