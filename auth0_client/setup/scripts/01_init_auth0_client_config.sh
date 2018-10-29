#!/usr/bin/env bash

# Initialize auth0_client directory and main config file
echo "dirname: "+$(dirname $0)
source $(dirname $0)/constants_common
echo "SOURCE DIR: ${SOURCE_DIR}"
MYDIR=$(dirname $0)
AUTH0_CLIENT_CONFIG_TEMPLATE="$MYDIR/../config/auth0_client.ini"

printc $BLUE 'Initializing auth0_client config...'
mkdir -p $APP_DIR

if [ ! -f $APP_DIR/auth0_client.ini ]; then
    printc $BLUE '  auth0_client.ini file not found, setting default config file'
    cp $AUTH0_CLIENT_CONFIG_TEMPLATE $APP_DIR/
else
   printc $BLUE "The  ~/.auth0_client/auth0_client.ini config file already exists,"
   printc $BLUE "not overwriting"
fi

printc $GREEN '  Done'

