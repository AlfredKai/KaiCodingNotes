# Kai Coding Notes

[MkDocs](https://www.mkdocs.org/user-guide/configuration/)

## Tips

### Counts

當題目是求count(number)/max的時候，必須要有對複雜度要求的敏感度，這一題暴力法如果是O(n^3)甚至到O(2^n)，只要是求count就有機會降到n，通常會利用幾種作法：

1. 上一個步驟的某些結果
2. DP
3. 某種神妙規則讓你不需要暴力解

### 2D DP

二維陣列DP通常都是A[i][j]會利用到A[i-1][j], A[i][j-1]和A[i-1][j-1]的資訊

### Bit Manipulation

bitwise類型題目通常實作都非常簡單，考的都是數學跟觀察(所以我覺得沒甚麼意思...但台灣某知名純軟公司也考了就是了...)，經過歸納把你的題目翻譯成根本看不出原始問題的樣子，就單看當下看能不能找出規則。

由於XOR的奇葩特性所以特愛考，請務必紀熟他的特性：

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

### Binrary Search

- 看到排序過後的資料就要想到binrary search
- 看到排序過後且要求複雜度是O(nlogn)則99.9%是binrary search

### Intuition of Time Complexity

- 
- 如果output是列舉，這提就是暴力法直接使用backtracking

### Intuition of Dynamic Programming

- 看到矩陣/Array就會想到DP