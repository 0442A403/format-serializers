# format-serializers
Repository contains HSE service-oriented architectures HW.
code)
    
That application serialize and deserialize different formats. It should support following formats:
- [x] pickle
- [x] xml
- [x] json
- [x] proto
- [x] avro
- [x] yaml
- [x] msgpack

## Usage

### Server
To start application you can use docker-compose to bring all formats:
```bash
docker compose up
```
or manual specific format:
```bash
python src -f json -t serializer 
```

### Client

Application can serialize, deserialize and get stats on that.

### Stats
You can gets stats about speed of serialization and deserialization your data in different formats. For that you can use:
```bash
python src/client.py -d data/extended.json -a get_result
```
As result you will see result like that:
```
2023-09-11 02:27:13,513 INFO avro	762 bytes	 70.749 ms	57.543 ms
2023-09-11 02:27:13,513 INFO json	3262 bytes	 45.781 ms	25.191 ms
2023-09-11 02:27:13,513 INFO msgpack	2592 bytes	 9.188 ms	12.430 ms
2023-09-11 02:27:13,513 INFO pickle	2430 bytes	 15.537 ms	11.414 ms
2023-09-11 02:27:13,513 INFO proto	1179 bytes	 334.991 ms	212.129 ms
2023-09-11 02:27:13,513 INFO xml	5626 bytes	 391.184 ms	420.884 ms
2023-09-11 02:27:13,513 INFO yaml	3026 bytes	 3404.989 ms	984.641 ms
```

### Serialization and deserialization

You can make http request for 5000 port with following syntax:
```json
{
  "format": "YOUR_FORMAT",
  "data": "YOUR_DATA",
}
```

For simplicity there is python script `client.py` that requests with specified data. Example of usage for all formats:
```bash
python src/client.py -f all -d data/extended.json -a full
```

