# docker-nginx-rp

## SSL

## Singlemode

### docker-compose

    rp:
      image: philipsahli/nginx-rp:latest
      ports:
        - "80:80"
        - "443:443"
      environment:
        - SERVER_NAME
        - PROXY_HOST
        - NOTIFICATION_EMAIL
        - PROXY_CONF_1_proxy_pass
        - PROXY_CONF_1_location
      labels:
        io.rancher.container.pull_image: "always"
      volumes:
        - /var/certs/`FQQN`:/etc/letsencrypt/

## Multimode

### docker-compose

    rp:
      image: philipsahli/nginx-rp:multi
      ports:
        - "80:80"
        - "443:443"
      links:
        - lb:lb
      environment:
        - SERVER_NAME
        - PROXY_HOST
        - NOTIFICATION_EMAIL

        - VHOST_1_SSL=True
        - VHOST_1_PROXY_CONF_1_proxy_pass
        - VHOST_1_PROXY_CONF_1_location
      labels:
        io.rancher.container.pull_image: "always"
      volumes:
 

## Test

    sh test.sh
