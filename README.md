# kchat
- Python chat program using Apache Kafka

![kchat](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXU0lEqTt92-OvzuYaFMV5za5weXUKnaB26Q&s) 

### Test
#### KAFKA Producer
```bash
$ python src/kchat/kafka/pro.py
[DONE]: 0.029494762420654297
```

```bash
$ $KAFKA_HOME/bin/kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-server localhost:9092

{"str": "value0"}
{"str": "value1"}
{"str": "value2"}
{"str": "value3"}
{"str": "value4"}
{"str": "value5"}
{"str": "value6"}
{"str": "value7"}
{"str": "value8"}
{"str": "value9"}
```
### Test2
#### KAFKA Consumer
```bash
$ python src/kchat/kafka/con.py
```
```bash
$ python src/kchat/kafka/pro.py
```
##### result
![image](https://github.com/user-attachments/assets/3a5aca68-8f8d-4a19-a045-ddb55bea3220)


