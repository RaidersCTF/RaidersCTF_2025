# forensics: Lost Pixel
## Question

友人から送られてきた大切な画像ファイルが開けない！！

## Difficulty
- `easy`

## Flag
```
RaidersCTF{F0undPix3L_Yay!!}
```

## Points
- `300`

## Writeup
PNGのマジックナンバーが欠けているから、その部分を特定して適切なマジックナンバーに修正する。


PNGのマジックナンバーは最初の8byte(89 50 4e 47 0d 0a 1a 0a)だが、問題では`4e`が`43`になっているためファイルが破損していると認識されて開くことができない。そのため、`hexedit`を使用して`43`を`4e`に戻すとFlagが書かれたPNGを開けるようになる。

```bash
hexedit <FILE_PATH>
```


## Author
- `jhsand`