#!/bin/bash
# This installer is meant to be run under sudo
# Does not install dependencies

SP_MAIN=spotify_main

SP_DIR=$( echo $( which spotify ) | cut -d"/" -f-3 )

mv ${SP_DIR}/spotify ${SP_DIR}/${SP_MAIN} # Rename original file
mv ./spotify ./muter.py SP_DIR/ # Move muter files 
