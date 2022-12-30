# nostr-relay-docker-compose

### setup instance

+ i did the below in aws
+ create instance (i used t2.micro, 1cpu, 1GB Ram and 15GB disk ) with "Ubuntu 20.04 image".
+ add ports 80 and 443 (http,https) to instance "inbound rules"
+ if you need help with ssh, see  https://unix.stackexchange.com/a/115860/158701
    + default username for ubuntu is `ubuntu`.
+ you can probably do all this via aws-cli, i didn't do that.

### security stuff

+ disable ssh password auth  https://stackoverflow.com/questions/20898384/disable-password-authentication-for-ssh
+ enable fail2ban https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-ubuntu-20-04
+ i didnt't do this: only allow certain ips to access port 22 via `iptables`

### setup domain/dns

+ purchase a domain and setup dns (i used aws route53)
    + after domain name purchase, in aws create "hosted zone/dns" for domain, aws will auto configure `NS` and `SOA` for you.
    + you then need to create below row.
    ```
    "Record name":"nostr.mydomain.com"
    "Type": "A"
    "Value": "1.2.3.4" (instance's ip)
    ```

+ verify via dig
```
dig A nostr.mydomain.com
```

### get https cert

+ to get the https sert, follow [https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal)

+ more links if you can't get above to work...
 
    + nginx config reference https://github.com/scsibug/nostr-rs-relay/blob/master/reverse-proxy.md

    + https://stackoverflow.com/questions/61502474/adding-aws-public-certificate-with-nginx

+ change ownership of folder, so containers can access cert files as new user

```
sudo adduser nginx
sudo usermod -u 2100 nginx
sudo groupmod -g 2100 nginx
sudo chgrp -R nginx /etc/letsencrypt/live
sudo chgrp -R nginx /etc/letsencrypt/archive
sudo chmod -R 750 /etc/letsencrypt/live
sudo chmod -R 750 /etc/letsencrypt/archive

```

# setup relay


+ install docker, follow https://docs.docker.com/engine/install/ubuntu

+ add `ubuntu` to group `docker`, follow https://docs.docker.com/engine/install/linux-postinstall

+ clone repo

```
cd ~
git clone https://github.com/pangyuteng/nostr-relay-docker-compose.git
cd nostr-relay-docker-compose
git submodule update --init
```

+ create files needed by nostr

```
sudo mkdir -p /mnt/hdd/nostr/data
cp nostr-rs-relay/config.toml /mnt/hdd/nostr
```

+ edit `/mnt/hdd/nostr/config.toml` per your liking

+ build and start relay via docker-compose

```
cd ~/nostr-relay-docker-compose
docker compose build
docker compose -f docker-compose.yml -f volume.yml up -d

docker compose -f docker-compose.yml -f volume.yml up -d --force-recreate
```

+ verify https can be reached in browser/terminal

```
curl https://nostr.mydomain.com
```

+ verify relay is setup via nostr client, for example `noscl` https://github.com/fiatjaf/noscl

