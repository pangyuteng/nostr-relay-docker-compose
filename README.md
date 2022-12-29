# nostr-relay-docker-compose



# setup instance ( you can probably do all this via aws-cli, i didn't do that...)

+ create instance (i used t2.micro, 1cpu, 1GB Ram and 15GB disk ) with ubuntu 20.04 image
+ ssh into instance ( https://unix.stackexchange.com/a/115860/158701 , user `ubuntu` if you used ubuntu image)
+ (aws) add ports 80 and 443 (http,https) to instance "inbound rules"

# setup dns mapping ( in route53, "A", map `nostr.mydomain.com` to my.ip )
# get https cert
    + https://stackoverflow.com/questions/61502474/adding-aws-public-certificate-with-nginx

actual certs are below
```
chown -R ubuntu:ubuntu /etc/letsencrypt/archive
```
# nginx config 
 https://github.com/scsibug/nostr-rs-relay/blob/master/reverse-proxy.md

+ follow steps here: [https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal)

#
```



git clone https://github.com/pangyuteng/nostr-relay-docker-compose.git
cd nostr-relay-docker-compose
git submodule update --init

mkdir -p /mnt/scratch/tmp/nostr/data
cp nostr-rs-relay/config.toml /mnt/scratch/tmp/nostr

docker compose build
docker compose --env-file .env -f docker-compose.yml -f volume.yml up -d
sudo chmod -R 777 data
```



```
curl https://github.com/fiatjaf/noscl/releases/download/v0.6.0/noscl -o
```