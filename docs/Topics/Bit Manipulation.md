# Bit Manipulation

## XOR

- 交換律
- 結合律
- 恆等律
- 歸零律
- **自反性**

```py
x ^ 0 = x
x ^ 1s = ~x
x ^ x = 0
a ^ b = c; a ^ c = b; b ^ c = a (交換律)
a ^ b ^ c = a ^ (b ^ c) (結合律)
x & (x - 1) => 清掉最低位的 1
x & (-x) => 取得最低位的 1
```

## Useful APIs

bit_length()
