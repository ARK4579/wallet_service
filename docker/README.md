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
    - connect to wallet_service docker container:
      - `docker exec -it wallet_service /bin/bash`
    - [wallet_service] create a default wallet, if you have already created wallet 0 you can skip this
      - `python wallet_service_cli.py createwallet test123`
    - [wallet_service] generate a new address in this wallet 0
      - `python wallet_service_cli.py getunusedaddress 0 test123`
      - copy address generate here e.g: bcrt1qja5ss7segmmx845qtgjsg6hvfx4q28kdjk40yu
    - connect to bitcoin node:
      - `docker exec -it bitcoind /bin/sh`
    - [bitcoind] create default wallet
      - `bitcoin-cli createwallet default`
    - [bitcoind] generate BTC
      - `bitcoin-cli generate 101`
    - [bitcoind] check balance of this wallet here 
      - `bitcoin-cli getwalletinfo`
      - balance must be like 50 BTC
    - [bitcoind] set tx fee
      - `bitcoin-cli settxfee 0.00001`
    - [bitcoind] send let's say 1 BTC to the wallet 0 address
      - `bitcoin-cli sendtoaddress bcrt1qja5ss7segmmx845qtgjsg6hvfx4q28kdjk40yu 1`
    - [bitcoind] Make the transaction confirm:
      - `bitcoin-cli generatetoaddress 7 $(bitcoin-cli getnewaddress)`
    - [wallet_service] confirm balance in wallet 0
      - `python wallet_service_cli.py getbalance 0 test123`
    - using these steps you can send any number of BTC to any addresses