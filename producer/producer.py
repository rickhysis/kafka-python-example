from kafka import KafkaProducer
import json

def main():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send('coba', {'message': 'Hello kafka'})
    producer.close()

if __name__ == '__main__':
    main()