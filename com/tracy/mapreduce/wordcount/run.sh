HADOOP_CMD="/Users/tracy/Desktop/itsoft/hadoop/hadoop-2.9.0/bin/hadoop"
STRAM_JAR_PATH="/Users/tracy/Desktop/itsoft/hadoop/hadoop-2.9.0/contrib/streaming/hadoop-streaming-2.9.0.jar"

INPUT_FILE_PATH_1="/The_Man_of_Property.txt"

OUTPUT_PATH="/output"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH


$HADOOP_CMD jar $STRAM_JAR_PATH \
        -input $INPUT_FILE_PATH_1 \
        -output $OUTPUT_PATH \
        -mapper "python map.py" \
        -reduce "python red.py" \
        -file ./map.py \
        -file ./red.py