# websocket_jsonrpc_client

- [x] dockerでws-server準備
- [x] dockerでws-client準備
- [ ] ws-serverとws-clientの結合
- [ ] CUIからhello-world入力してjsonrpcプロトコルのws通信

```shell
docker compose up
docker exec -it websocket_jsonrpc_client-client-1 sh
# ws-serverが正常に起動していることを確認する
wscat -c ws://host.docker.internal:8765
```

### 参考
- https://www.jsonrpcclient.com/en/stable/examples.html#websockets
