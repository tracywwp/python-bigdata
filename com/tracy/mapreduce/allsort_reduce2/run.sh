set -e -x

HADOOP_CMD="/Users/tracy/Desktop/itsoft/hadoop/hadoop-2.9.0/bin/hadoop"
STRAM_JAR_PATH="/Users/tracy/Desktop/itsoft/hadoop/hadoop-2.9.0/contrib/streaming/hadoop-streaming-2.9.0.jar"

INPUT_FILE_PATH_A="/a.txt"
INPUT_FILE_PATH_B="/b.txt"

OUTPUT_SORT_PATH="/output_sort"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_SORT_PATH

# Step 3.
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_A,$INPUT_FILE_PATH_B\
    -output $OUTPUT_SORT_PATH \
    -mapper "python map_sort.py" \
    -reducer "python red_sort.py" \
    -jobconf "mapred.reduce.tasks=1" \
    -file ./map_sort.py \
    -file ./red_sort.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
    -jobconf mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
    -jobconf stream.num.map.output.key.fields=1 \
    -jobconf stream.map.output.field.separator='	' \
    -jobconf map.output.key.field.separator='	' \
    -jobconf mapred.text.key.partitioner.options="-k1,1" \
    -jobconf mapred.text.key.comparator.options="-k1,1n" \
    -jobconf mapred.reduce.tasks=1