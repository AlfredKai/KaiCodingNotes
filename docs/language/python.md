# Python

## Basics

[Python Tips](http://book.pythontips.com/en/latest/index.html)

- There's no `null`, use `None`
- *boolean operators*: **and**, **or** and **not**
- Use `int()` to cast `float`
- power operator: n**2
- square root: n**(1/2)
- check divisible by modulus(mod) operator `%`
- list initialization with default value: [0,0] + [1]*n

### Dont use mutable data as default argument

Default argument values are calculated when the function is *defined* , not when it is run. A common error with new (and sometimes not-so-new) Python programmers is to use a mutable data type such as a list or dictionary as a default argument.

### Generate Number Sequences with `range()`

You use **range()** similar to how to you use slices: **range( *start* , *stop* , *step* )** .

If you omit *start* , the range begins at **0** . The only required value is *stop* ; as with slices, **the last value created will be just before *stop*** . The default value of *step* is **1** , but you can go backward with **-1** .

### Comprehensions

A *comprehension* is a compact way of creating a Python data structure from one or more iterators. Comprehensions make it possible for you to combine loops and conditional tests with a less verbose syntax.

#### List Comprehensions

```py
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

```py
[ *expression* for *item* in *iterable* if *condition* ]
```

```py
>>> a_list = [ number for number in range ( 1 , 6 ) if number % 2 == 1 ]
>>> a_list
[1, 3, 5]
```

#### Dictionary Comprehensions

```py
{ *key_expression* : *value_expression* for *expression* in *iterable* }
```

```py
>>> word = 'letters'
>>> letter_counts = { letter : word . count ( letter ) for letter in word }
>>> letter_counts
{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}
```

#### Set Comprehensions

```py
{ *expression* for *expression* in *iterable* }
```

```py
>>> a_set = { number for number in range ( 1 , 6 ) if number % 3 == 1 }
>>> a_set
{1, 4}
```

### `in` statement

Use `in` to see if a value exists in any of Python’s iterable data types, notably lists, tuples, sets, strings. For the dictionary, in looks at the keys instead of their values.

### Common Libraries

```py
[].sort()
```

### Ternary Operators

```py
condition_if_true if condition else condition_if_false
```

## Patterns

### Indexed Array

when you have to record the element's index in an array for futher purpose.

```py
nums = [(n,i) for i,n in enumerate(nums)]
```

### Traversal Linked List

```py
while linkList != None:
    linkList = linkList.next
```

### Palindrome

```py
a == a[:-1]
```