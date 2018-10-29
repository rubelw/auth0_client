#!/usr/bin/env bash
source $(dirname $0)/constants_common

printc $GREEN 'Setup complete'

# If being run during first-time setup, check if new envars have been added by other scripts
# (can't automatically export these back to parent shell)
if ! [ -z "$NEW_ENVARS" ]; then
    printc $GREEN 'New environment variables set; for changes to take effect in current shell, run:'
    printc $CYAN '  source ~/.bashrc'
    unset NEW_ENVARS
fi
