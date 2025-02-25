# rev: うpx
## Question

`うpx`は打ち間違いじゃないよ

## Difficulty
- `easy`

## Flag
```
RaidersCTF{UPX_G0t_0wn3d_L0L}
```

## Points
- `100`

## Writeup
ただ単にファイルを`strings`コマンドで見るだけではFLAGは表示されるけど完璧じゃない

`upx -d`でアンパック後に`strings`コマンドを使用するとFLAGが完全に表示される

## Author
- `jhsand`