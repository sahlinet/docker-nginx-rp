# docker-nginx-rp

## Example docker-compose.yml
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
        - backend1:backend1
        - backend2:backend2
      environment:
        - NOTIFICATION_EMAIL=user@example.com
      
        - VHOST_1_SERVERNAME=test.example.com
        - VHOST_1_SSL=False
        - VHOST_1_PROXYCONF_all_proxy_pass=http://backend1
        - VHOST_1_PROXYCONF_all_location=/

        - VHOST_2_SERVERNAME=beta.example.com
        - VHOST_2_DOMAINS=beta.example.com
        - VHOST_2_SSL=True
        - VHOST_2_PROXYCONF_all_proxy_pass=http://backend2
        - VHOST_2_PROXYCONF_all_location=/
        - VHOST_2_PROXYCONF_robots_proxy_pass=http://backend2/static/robots.txt
        - VHOST_2_PROXYCONF_robots_location=/robots.txt

On Rancher add:

      labels:
        io.rancher.container.pull_image: "always"
      volumes:
        - /var/certs/`FQQN`:/etc/letsencrypt/

## Test

    sh test.sh
