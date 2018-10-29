#!/usr/bin/env bash

source $(dirname $0)/constants_common
source $BASH_STARTUP  # If being run duing first-time setup, proxy envars might not yet be set

printc $BLUE 'Updating auth0-client...'
#pip install -U auth0_client
