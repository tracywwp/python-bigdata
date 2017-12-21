
HADOOP_CMD="/Users/tracy/Desktop/itsoft/hadoop/hadoop-2.9.0/bin/hadoop"
STRAM_JAR_PATH="/Users/tracy/Desktop/itsoft/hadoop/hadoop-2.9.0/contrib/streaming/hadoop-streaming-2.9.0.jar"

INPUT_FILE_PATH_1="/The_Man_of_Property.txt"
OUTPUT_PATH="/output_cachearchive_broadcast"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH

# Step 1.
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map.py mapper_func WH.gz" \
    -reducer "python red.py reduer_func" \
    -jobconf "mapred.reduce.tasks=2" \
    -jobconf  "mapred.job.name=cachefile_demo" \
    -cacheArchive "hdfs://master:9000/w.tar.gz#WH.gz" \
    -file "./map.py" \
    -file "./red.py"