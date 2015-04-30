#!/bin/bash
EXEC_FILE="$0"
BASE_NAME=`basename "$EXEC_FILE"`
if [ "$EXEC_FILE" = "./$BASE_NAME" ] || [ "$EXEC_FILE" = "$BASE_NAME" ]; then
        FULL_PATH=`pwd`
else
        FULL_PATH=`echo "$EXEC_FILE" | sed 's/'"${BASE_NAME}"'$//'`
        cd "$FULL_PATH"                 > /dev/null 2>&1
        FULL_PATH=`pwd`
fi

LOG_PATH="$FULL_PATH/logs"
celery multi start w1 -A ParseWorker -Q url -l info --logfile=${LOG_PATH}/%N.log
#celery multi start w1 -A ParseWorker -l info --logfile=${LOG_PATH}/%N.log -Q url
#celery multi start -A textParser_worker 
