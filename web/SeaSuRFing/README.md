# web: SeaSuRFing
## Question

弊社の新入社員が画像の健全性チェックサービスを開発したようです。しかし、彼は「社内からのアクセスのみ」という重要な機能を実装したと言っていますが、本当に安全なのでしょうか？

## Difficulty
- `easy`

## Flag
```
RaidersCTF{ssrf_1s_4_S3rv3r_S1d3_vu1n}
```

## Points
- `100`

## Writeup
ソースコードを確認すると、`/internal/api`という内部ルートが存在することが分かる。

よく見ると、ドメインが適当でもURIに`/internal/api`を含めれば何かアクションが起こりそうなので、試しにリクエストしてみる。
```bash
http://raidersctf.com/internal/api
```


すると、`{"error":"Access denied"}`というレスポンスが返されるが、URL内に`source_ip=None`という属性がある。

そこで、内部ネットワークからの通信であるかのように擬似的に認識させるため、`source_ip=127.0.0.1`に変更するとFlagが表示される。

## Author
- `jhsand`