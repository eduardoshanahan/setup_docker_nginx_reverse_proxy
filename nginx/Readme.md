# Configuring Nginx as a reverse proxy

## Creating a default configuration for Nginx

If you don't have a configuration for Nginx alredy prepared, you can create a default set of files by running an empty image and copying the directories back to the host.

There is an bash script that can be used at

```create-default-nginx-configuration.sh```

which will create a directory named ./nginx-conf that can be used later by docker compose.