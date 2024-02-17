## Group finder
Groups string based on their prefixes. Descriptive as possible

Requirements: Python 3+ and docker-compose (for web app)

### Standalone run

```shell
> cd artifacts
> python3 main.py
```

### Run in web app

1. Start app
```shell
> docker-compose up
```

2. Generate `payload.json`
```shell
> cd artifacts && python3 csv_to_request_json.py
```

3. Open web page http://localhost:8000/groups/raw/ and put `payload.json` content into `Raw data -> Content field` and press `POST`
