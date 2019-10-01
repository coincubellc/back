<h1>COINCUBE</h1>
This repo contains the Coincube App (except for the front-end, which is run via NPM and should be cloned from the `front-end` repo).

<h2>Getting Started</h2>
In order to get up and running with this repo:

<h2>Clone Repo</h2>
1. Make sure you have `git` <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git">installed locally</a>.<br>
2. From command line run `git clone https://github.com/coincubellc/app.git` and `cd app` to change directories.

<h2>Submodules</h2>
This repo contains submodules which need to be pulled down before you will be able to run the application.<br>

<h5>In order to pull in the submodules you will need to run:</h5>
1. `git submodule init`<br>
2. `git submodule update`<br>

<h5>Already have a working version and want to update all submodules?<h5>
`git submodule update --recursive --remote`<br>

<h5>For more on submodules:</h5>
<a href="https://git-scm.com/book/en/v2/Git-Tools-Submodules">Git Submodule Tutorial #1</a><br>
<a href="https://git.wiki.kernel.org/index.php/GitSubmoduleTutorial">Git Submodule Tutorial #2</a>

<h2>Add CMC_API_KEY from Coin Market Cap</h2>
1. Visit <a href="https://pro.coinmarketcap.com/signup/">Coin Market Cap</a> and signup for their free Basic API. 
2. Paste the API key into lines 46 and 72 in `docker-compose.yml`. The key should be a string: `CMC_API_KEY: 'your_CMC_API_key_here'`.
3. Save `docker-compose.yml`.

<h2>Add VAULT_SEED</h2>
<p>You'll need to securely generated a base64 encoded RSA Private key. This will be used to encrypt your API keys and other sensitive data in the database.
</p>

1. From inside of the `app` folder using terminal, run `python generate_vault_seed.py` which will generate a new seed.
2. Paste the entire encoded key as a string on lines 18 and 113 of `docker-compose.yml`
3. These two lines should look something like: `VAULT_SEED: 'b'LS0tLS1CRUdJTiBSU0......TVV6UWh3PT0KLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0tLS0='`
4. Save `docker-compose.yml`.

<h2>Docker Setup</h2>
You will need <a href="https://docker.com" target="_blank">Docker</a>.

Build the Docker container(s):
For local environment: `docker-compose build`<br>

Run the Docker container(s):
For local environment: `docker-compose up`<br>

The first time you run 'docker-compose up' you will need to wait for the database to be populated. This should take 10-15 minutes.


<h2>For local development/debugging</h2>
<h4>Shell into a specific container</h4>
Find "CONTAINER ID": `docker ps`<br>

Shell into container: `docker exec -it "CONTAINER ID" bash`<br>
(i.e. `docker exec -it 78e539ca25be bash`)

<h4>View container logs</h4>
`docker logs -f "CONTAINER ID"`