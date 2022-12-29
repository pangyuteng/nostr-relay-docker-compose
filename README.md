# nostr-relay-docker-compose

### setup instance ( you can probably do all this via aws-cli, i didn't do that...)

+ create instance (i used t2.micro, 1cpu, 1GB Ram and 15GB disk ) with ubuntu 20.04 image
+ ssh into instance ( https://unix.stackexchange.com/a/115860/158701 , user `ubuntu` if you used ubuntu image)
+ (aws) add ports 80 and 443 (http,https) to instance "inbound rules"

### setup domain/dns

+ buy the domain and setup dns (i used aws, route53)
    + after domain name purchase, in aws create "hosted zone/dns" for domain
    + create simple mapping to map "nostr.mydomain.com" to the instance ip "1.1.1.1" (type `A`).
    + not sure but i create a cert here for "nostr.mydomain.com", and added an entry in the dns (type `CNAME`).
### get https cert

+ follow [https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal)

+ more links if you can't get above to work...
 
    + nginx config reference https://github.com/scsibug/nostr-rs-relay/blob/master/reverse-proxy.md

    + https://stackoverflow.com/questions/61502474/adding-aws-public-certificate-with-nginx


+ actual certs are below, so you gotta chown the folder
```
chown -R ubuntu:ubuntu /etc/letsencrypt/archive
```
# setup relay in instance
```

# install docker.

# install relay and nginx in containers

git clone https://github.com/pangyuteng/nostr-relay-docker-compose.git
cd nostr-relay-docker-compose
git submodule update --init

mkdir -p /mnt/scratch/tmp/nostr/data
cp nostr-rs-relay/config.toml /mnt/scratch/tmp/nostr
cd /mnt/scratch/tmp/nostr
sudo chmod -R 777 data

cd ~/nostr-relay-docker-compose
docker compose build
docker compose --env-file .env -f docker-compose.yml -f volume.yml up -d


```

### verify relay is setup via `noscl`

```
https://github.com/fiatjaf/noscl
```