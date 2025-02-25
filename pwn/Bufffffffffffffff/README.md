# pwn: Bufffffffffffffff
## Question

あ、あふれる〜！

## Difficulty
- `easy`

## Flag
```
RaidersCTF{bfo_is_tricky}
```

## Points
- `100`

## Writeup
buf配列は12バイトのサイズしか確保されていないにも関わらず、read()関数で 0x12(18バイト)を読み込んでいる。

そのため、適当な文字列を12バイト以上入力することでバッファオーバーフローが発生し、`is_authorized`が1になり、Flagが表示される。

## Author
- `jhsand`