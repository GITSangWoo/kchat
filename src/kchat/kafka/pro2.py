from kafka import KafkaProducer
import time 
import json
from tqdm  import tqdm

pro = KafkaProducer(
        bootstrap_servers=['ec2-15-165-19-52.ap-northeast-2.compute.amazonaws.com:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')         
)

start = time.time()

for i in tqdm(range(10)):
    time.sleep(0.1)
    data = {'str':'value' + str(i)} 
    pro.send('topic2', value = data)
    pro.flush() 

end = time.time()
print("[DONE]:", end - start)

