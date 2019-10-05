# COINCUBE - Back
This repo contains a Docker application which includes the web server, cron-jobs, unified exchange API, and trading engine.<br>

You will also need to clone and install the Node.js powered <a href="https://github.com/coincubellc/front">COINCUBE - Front</a> for the UI.

## Getting Started
In order to get up and running with this repo:

## Clone Repo
Make sure you have <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git">git installed locally</a>.<br>
```
git clone https://github.com/coincubellc/back.git
```
## Submodules
This repo contains submodules which need to be pulled down before you will be able to run the application.<br>

##### In order to pull in the submodules you will need to run:
```
git submodule init
```

```
git submodule update
```

##### Already have a working version and want to update all submodules?
```
git submodule update --recursive --remote
```

##### For more on submodules:
<a href="https://git-scm.com/book/en/v2/Git-Tools-Submodules">Git Submodule Tutorial #1</a><br>
<a href="https://git.wiki.kernel.org/index.php/GitSubmoduleTutorial">Git Submodule Tutorial #2</a>

## Add CMC_API_KEY from Coin Market Cap
1. Visit <a href="https://pro.coinmarketcap.com/signup/">Coin Market Cap</a> and signup for their free Basic API. 
2. Paste the API key into lines 46 and 72 in `docker-compose.yml`. The key should be a string: `CMC_API_KEY: 'your_CMC_API_key_here'`.
3. Save `docker-compose.yml`.

## Add VAULT_SEED
<p>You'll need to securely generated a base64 encoded RSA Private key. This will be used to encrypt your API keys and other sensitive data in the database.
</p>

1. From inside of the `back` folder, generate a new seed `python generate_vault_seed.py` which will generate a new seed.
2. Paste the entire encoded key except for the preceding 'b' as a string on lines 18 and 113 of `docker-compose.yml`
3. These two lines should look something like: `VAULT_SEED: 'LS0tLS1CRUdJTiBSU0......TVV6UWh3PT0KLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0tLS0='`
4. Save `docker-compose.yml`.

## Docker Setup
You will need <a href="https://docker.com" target="_blank">Docker</a>.

Build the Docker container(s):
```
docker-compose build
```

Run the Docker container(s):
```
docker-compose up
```

The first time you run `docker-compose up` you will need to wait for the database to be populated. This should take 10-15 minutes.


## For local development/debugging
#### Shell into a specific container
Find "CONTAINER ID": `docker ps`<br>

Shell into container: `docker exec -it "CONTAINER ID" bash`<br>
(i.e. `docker exec -it 78e539ca25be bash`)

#### View container logs
`docker logs -f "CONTAINER ID"`