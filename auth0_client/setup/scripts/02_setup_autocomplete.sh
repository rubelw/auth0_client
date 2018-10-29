#!/usr/bin/env bash
# Set up auth0_client autocomplete for bash
# Can be run via setup.py install, pip install, or manually

source $(dirname $0)/constants_common
# APP_DIR=/Users/rubelw/.auth0_client
DEST_FILE=$APP_DIR/autocomplete
PKG_FILE=$SCRIPT_DIR/scripts/auth0_client_autocomplete

# Create autocompletion file in auth0_client config directory
printc $BLUE 'Seeding bash autocomplete...'
cp $PKG_FILE $DEST_FILE

# Append to .bashrc, if environment variable is not already present
source $BASH_STARTUP > /dev/null 2>&1
if ! type _AUTH_CLIENT_COMPLETE > /dev/null 2>&1 ; then
    printf '\nsource %s\n' $DEST_FILE >> $BASH_STARTUP
    printc $GREEN '  Done'
    export NEW_ENVARS=True
else
    printc $GREEN '  Already set'
fi
