# Build image

```bash
docker build --rm --tag monkeysign .
```

# Run container

```bash
docker run --rm -it -p 8081:80 --name monkeysign monkeysign
```

# Run two instances 

This will be available at localhost:8081 and localhost:8082

```bash
docker compose up
```