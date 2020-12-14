# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:20:19 2020
"""

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
rdd = spark.sparkContext.textFile("/data/data.txt")

for element in rdd.collect():
    print(unicode(element).encode('utf8'))

#Flatmap    
rdd2=rdd.flatMap(lambda x: x.split(" "))
for element in rdd2.collect():
    print(unicode(element).encode('utf8'))
#map
rdd3=rdd2.map(lambda x: (x,1))
for element in rdd3.collect():
    print(unicode(element).encode('utf8'))
#reduceByKey
rdd4=rdd3.reduceByKey(lambda a,b: a+b)
for element in rdd4.collect():
    print(unicode(element).encode('utf8'))
#map
rdd5 = rdd4.map(lambda x: (x[1],x[0])).sortByKey()
for element in rdd5.collect():
    print(unicode(element).encode('utf8'))
#filter
rdd6 = rdd5.filter(lambda x : 'a' in x[1])
for element in rdd6.collect():
    print(unicode(element).encode('utf8'))
