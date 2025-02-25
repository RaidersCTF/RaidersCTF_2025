# crypto: Ceaser 13
## Question

ROT13

nc IP 5000


## Difficulty
- `easy`

## Flag
```
RaidersCTF{C43sar_c1ph3r}
```

## Points
- `100`

## Writeup
シーザー暗号は、アルファベットを一定の文字数だけずらして変換する暗号方式です。例えば、3文字ずらす場合、‘a’は’d’、‘b’は’e’に変換されます。

solve.py
```python
target = "cryptography"
plaintext = ""
for x in target:
  plaintext += (chr(((ord(x) - ord('a') + 13) % 26) + ord('a')))
print(plaintext)
```

```bash
python3 solove.py | nc localhost 5000
```

## Author
- `kmjak`