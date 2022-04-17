# Monkey sign: look at the monkeys waving

I needed a simple http service to verify if my Nginx proxy was working.

There are implementations already done like [Jason Wilder's whoami](https://github.com/jwilder/whoami), but I also wanted to have the IP address and host name for the container.

### Why monkeys?

The more birthdays I pile up, the more I struggle to differentiate us from the monkeys. And that is not too bad, it makes me a lot more compassionate than before.

## To test it once the container is running:

```
curl $(hostname --all-ip-addresses | awk '{print $1}'):8081
{"ip":"172.17.0.2","name":"8a2acdc326b0","id":"c0f6f701-f619-444a-8cc5-44ee2daaac2d"}
```

## Build image

```bash
docker build --rm --tag monkeysign .
```

## Run container

```bash
docker run --rm -it -p 8081:80 --name monkeysign monkeysign
```

## Run two instances 

This will be available at localhost:8081 and localhost:8082

```bash
docker compose up
```