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
5. generate BTC and send to wallet 0 in wallet_service
    - `docker exec -it wallet_service /bin/bash`
    - [wallet_service] `python wallet_service_cli.py createwallet test123`
    - [wallet_service] `python wallet_service_cli.py getunusedaddress 0 test123`
      - copy address generate here e.g: bcrt1qja5ss7segmmx845qtgjsg6hvfx4q28kdjk40yu
    - `docker exec -it bitcoind /bin/sh`
    - [bitcoind] `bitcoin-cli createwallet default`
    - [bitcoind] `bitcoin-cli generate 101`
    - [bitcoind] `bitcoin-cli getwalletinfo`
      - balance must be like 50 BTC
    - [bitcoind] `bitcoin-cli settxfee 0.00001`
    - [bitcoind] `bitcoin-cli sendtoaddress bcrt1qja5ss7segmmx845qtgjsg6hvfx4q28kdjk40yu 1`
    - [bitcoind] `bitcoin-cli generatetoaddress 7 $(bitcoin-cli getnewaddress)`
    - [wallet_service] `python wallet_service_cli.py getbalance 0 test123`
