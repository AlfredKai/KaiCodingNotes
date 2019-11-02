# LeetCode using Python

[LeetCode](https://leetcode.com/)

## Python

- There's no `null`, use `None`
- *boolean operators*: **and**, **or** and **not**

### Generate Number Sequences with `range()`

You use **range()** similar to how to you use slices: **range( *start* , *stop* , *step* )** .

If you omit *start* , the range begins at **0** . The only required value is *stop* ; as with slices, **the last value created will be just before *stop*** . The default value of *step* is **1** , but you can go backward with **-1** .

### Comprehensions

A *comprehension* is a compact way of creating a Python data structure from one or more iterators. Comprehensions make it possible for you to combine loops and conditional tests with a less verbose syntax.

#### List Comprehensions

```
[ *expression* for *item* in *iterable* ]
```

```py
>>> number_list = list (range ( 1 , 6 )) 
>>> number_list 
[1, 2, 3, 4, 5]
```

```py
>>> number_list = [ number - 1 for number in range ( 1 , 6 )] 
>>> number_list 
[0, 1, 2, 3, 4]
```

```
[ *expression* for *item* in *iterable* if *condition* ]
```

```py
>>> a_list = [ number for number in range ( 1 , 6 ) if number % 2 == 1 ] 
>>> a_list 
[1, 3, 5]
```

#### Dictionary Comprehensions

```
{ *key_expression* : *value_expression* for *expression* in *iterable* }
```

```py
>>> word = 'letters' 
>>> letter_counts = { letter : word . count ( letter ) for letter in word } 
>>> letter_counts 
{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}
```

#### Set Comprehensions

```
{ *expression* for *expression* in *iterable* }
```

```py
>>> a_set = { number for number in range ( 1 , 6 ) if number % 3 == 1 } 
>>> a_set 
{1, 4}
```

### `in` statement

Use `in` to see if a value exists in any of Python’s iterable data types, notably lists, tuples, sets, strings. For the dictionary, in looks at the keys instead of their values.

### Reference

[Assignment statements in Python are more interesting than you might think](https://medium.com/broken-window/many-names-one-memory-address-122f78734cb6)
