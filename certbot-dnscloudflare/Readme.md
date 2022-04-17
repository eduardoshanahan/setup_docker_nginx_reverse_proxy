# Generate Let's Encrypt SSL certificates
To make this container to work, you need to create a directory named 'cloudflare' and inside it you need a file called credentials.

The content of that file has to be:

```dns_cloudflare_api_token="replace with your api token in cloudflare"```

Once you ran it, a directory named 'letsencrypt' will be created and the content will include you keys, located at:

```
./letsencrypt/live/<yourdomain>/fullchain.pem
./letsencrypt/live/<yourdomain>/privkey.pem
```

Later you can create symbolic links to include them into your Nginx configuration.

## Running docker compose

You can run the docker compose files from a terminal session:

### List the certificates

```bash
docker compose -f ./certbot-dnscloudflare/docker-compose.list.yml up
```

### Issue or renew certificates

Replace ```<your domain> ```:

```bash
DOMAIN=<domain> docker compose -f ./certbot-dnscloudflare/docker-compose.issue.yml up
```

### Revoke certificates

Replace ```<your domain> ```:

```bash
DOMAIN=<your domain> docker compose -f ./certbot-dnscloudflare/docker-compose.revoke.yml up
```

### Using [Python DoIt](https://pydoit.org/) 

Some time ago I started using Python DoIt as part of my development toolbox and I am quite happy with it. I included my ```dodo.py``` file to cover for it.

```
$ doit list
issue_certificate    Issue a certificate for a given domain - usage: issue_certificate -d domain.com (required)
list_certificates    List the SSL certificates available
revoke_certificate   Revoke the certificate for a given domain - usage: revoke_certificate -d domain.com (required)
```