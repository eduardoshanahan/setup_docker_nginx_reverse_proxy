docker run --name tmp-nginx-container -d nginx
docker cp tmp-nginx-container:/etc/nginx ./nginx-config
docker rm -f tmp-nginx-container