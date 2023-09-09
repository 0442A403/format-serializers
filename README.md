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
docker compose build
docker compose up
```
or manual specific format:
```bash
python src -f json -t serializer 
```

### Client
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

