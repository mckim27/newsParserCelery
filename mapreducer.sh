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

DATA_PATH="$FULL_PATH/data"
MAPREDUCE_PATH="$FULL_PATH/mapreducer"

cat $DATA_PATH/*  | python $MAPREDUCE_PATH/mapper.py | sort -k1,1 | python $MAPREDUCE_PATH/reducer.py
