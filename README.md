# format-serializers
Repository contains HSE service-oriented architectures HW.
code)
    
That application serialize and deserialize different formats. It should support following formats:
- [x] pickle
- [ ] xml
- [x] json
- [ ] proto
- [ ] avro
- [ ] yaml
- [ ] msgpack

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

For simplicity there is python script `client.py` that make it request with specified data by itself. Example of usage:
```bash
python src/client.py -f pickle -d data/simple.json -a full
```
