# web: What language?
## Question

webサーバの管理者さんに手作りのお菓子作ってあげてほしいなぁ

## Difficulty
- `easy`

## Flag
```
RaidersCTF{Co0kei_yu&_yu&_yu&&y}
```

## Points
- `100`

## Writeup
検証ツールでCookieが保存されている場所を見つけ、_sessionID_のvalueの値をbash64でエンコードした値(admin)に置き換えて再度更新するとflagが表示される。

## Author
- `towa`