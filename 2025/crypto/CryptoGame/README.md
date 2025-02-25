# crypto: Crypto Game
## Question

Crypto Game

nc IP 5000


## Difficulty
- `hard`

## Flag
```
RaidersCTF{C43sar_c1ph3r}
```

## Points
- `500`

## Writeup
2 → 1 → 1 → 3 → 2でFlagが取得できる

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