# Setting up Docker Development Environment

## Run

1. Copy `cp config.ini.sample config.ini` and update values in config.ini file
2. run bitcoin-core in regtest mode all you have to do is:
    - `docker compose -f .\docker\docker-compose.yml up --build`
    - Make sure docker service/docker desktop is running.
3. Now you can interact with regtest's RPC server:
    - `curl --user myuser:SomeDecentp4ssw0rd --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getblockchaininfo","params":[]}' -H 'content-type:text/plain;' http://127.0.0.1:18443/` 
4. You can also interact with 
    - `curl localhost:8000/api/queue`
