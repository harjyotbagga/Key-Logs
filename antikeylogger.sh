#!/bin/bash
result=`pgrep -fl keylogger.sh | grep "keylogger.sh"`
# echo $result
if [[ "$result" != "" ]];then
    echo "Key Logger running in background..."
    set -- $result
    if kill -9 $1 ; then
        echo "The Key Logger process has been killed."
    else
        echo "The Key Logger process could not be killed."
    fi
else
    echo "Key Logger is not running."
fi