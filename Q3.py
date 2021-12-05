import sys
from pyspark import SparkConf, SparkContext

configs = SparkConf()
spark_context = SparkContext(conf=configs)

lines = spark_context.textFile("./Daftar4.txt")
words = lines.flatMap(lambda line: line.split())
letters = words.filter(lambda letter: letter.isalpha()).map(lambda word: word[0].lower())
maps = letters.map(lambda letter: (letter, 1))
counts = maps.reduceByKey(lambda n1, n2: n1 + n2)

counts.saveAsTextFile("./out")
spark_context.stop()