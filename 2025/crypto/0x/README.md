# crypto: 0x
## Question

16進数で〇〇って…

nc IP 5000

## Difficulty
- `easy`

## Flag
```
RaidersCTF{0x_1s_4m4z1ng}
```

## Points
- `100`

## Writeup
与えられたファイルを読み解いてFLAG_hexが0xf1a9だとflagを出力することに注目

0xf1a9は10進数で61865であることから61865を入力すると答えが出る

solve.py
```python
flag = 0xf1a9
print(int(flag))
```

```bash
python3 solove.py | nc localhost 3001
```

## Author
- `kmjak`