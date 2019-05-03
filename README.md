# Kafka Python Example

I will see how use Apache Kafka with Python and make a sample application using the Python client for Apache Kafka. In Kafka the communication between the clients and the servers is done with a simple, high-performance, language agnostic TCP protocol. This protocol is versioned and maintains backwards compatibility with older version. you can see complete documentation in [Apache Kafka](https://kafka.apache.org/)

## Installing Python client for Apache Kafka

Before we can start working with Apache Kafka in Python program, we need to install the Python client for Apache Kafka.
```
$ pip install kafka-python
```
Let's create a topic named "coba" with a single partition and only one replica:
```
$ bin\kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic coba
```
Now see that topic if we run the list topic command:
```
$ bin\kafka-topics.sh --list --bootstrap-server localhost:9092
```
run consumer
```
$ cd consumer
$ python consumer.py
```

open new terminal and then run producer
```
$ cd producer
$ python producer.py
**** result message
Topic: coba
Message: {"message": "Hello kafka"}
Record: ConsumerRecord(topic='coba', partition=0, offset=15, timestamp=1556875860526, timestamp_type=0, key=None, value=b'{"message": "Hello kafka"}', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=26, serialized_header_size=-1)
```
You can use console consumer to view messages produced on some topic:
```
$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic coba --from-beginning
```