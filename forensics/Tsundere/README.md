# forensics: Tsundere
## Question

どこかにメッセージが隠されているらしい

## Difficulty
- `easy`

## Flag
```
RaidersCTF{H1dd3n_M3ss4g3}
```

## Points
- `300`

## Writeup
```bash
steghide extract -sf <FILE_PATH>
```
Passphraseは不要。これでflag.txtが抽出できる。


しかし、16進数でエンコードされているため元に戻すとFlagが出てくる。

```bash
xxd -r -p flag.txt
```


## Author
- `jhsand`