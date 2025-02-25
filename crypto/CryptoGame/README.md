# crypto: Crypto Game
## Question

Crypto Game

nc IP 5000


## Difficulty
- `hard`

## Flag
```
RaidersCTF{c4n_y0u_w1n_th3_g4m3}
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