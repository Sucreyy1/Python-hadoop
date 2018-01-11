hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar -files "/mnt/hgfs/share/python/word-mapper.py,/mnt/hgfs/share/python/word-reduce.py" -input /tmp/index.html -output /tmp/wordconunttest -mapper "python /mnt/hgfs/share/python/word-mapper.py" -reducer "python /mnt/hgfs/share/python/word-reduce.py"



执行word-count实例的命令
