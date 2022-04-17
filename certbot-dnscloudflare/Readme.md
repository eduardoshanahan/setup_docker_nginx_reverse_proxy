To make this container to work, you need to create a directory named 'cloudflare' and inside it you need a file called credentials.

The content of that file has to be:

dns_cloudflare_api_token="replace with your api token in cloudflare"

Once you ran it, a directory named 'letsencrypt' will be created and the content will include you keys, located at:

```bash
./letsencrypt/live/<yourdomain>/fullchain.pem
./letsencrypt/live/<yourdomain>/privkey.pem
```

Later you can create symbolic links to include them into your Nginx configuration.
