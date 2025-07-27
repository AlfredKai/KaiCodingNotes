****# Python

## Basics

[Python Tips](http://book.pythontips.com/en/latest/index.html)

[The Little Book of Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/index.html)

- There's no `null`, use `None`
- *boolean operators*: **and**, **or** and **not**
- Use `int()` to cast `float`
- power operator: n**2
- square root: n**(1/2)
- check divisible by modulus(mod) operator `%`
- list initialization with default value: [0,0] + [1]*n
- list of lists initialization x = [[] for i in range(n)]

### Useful Built-in Libraries

- str(), int()
- isdigit()
- sorted()
- reversed()
- bisect
  - bisect_left(list, item[, lo[, hi]])
  - insort_left(list, item[, lo[, hi]])
- zip()
- setdefault()
- deque
- heapq
  - heapify(x)
  - heappush(heap, item)
  - heappop(heap)
- collections
  - deque
    - append(x)
    - appendleft(x)
    - pop()
    - popleft()

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

sorting

```py
[].sort()
[].sort(reverse = True)
```

inf

```py
math.inf
-math.inf
```

print without newline

```py
print('Hello, World!', end=' ')
```

### Ternary Operators

```py
condition_if_true if condition else condition_if_false
```

## Sorting

[Sorting HOW TO](https://docs.python.org/3/howto/sorting.html#sortinghowto)

### Operator Module Functions as Key Functions

- itemgetter()
- attrgetter()
- methodcaller()

```py
sorted(student_tuples, key=itemgetter(1,2))
```

### Sort Stability and Complex Sorts

Sort the student data by descending *grade* and then ascending *age*, do the *age* sort first and then sort again using *grade*:

```py
s = sorted(student_objects, key=attrgetter('age'))     # sort on secondary key
sorted(s, key=attrgetter('grade'), reverse=True)       # now sort on primary key, descending
```

**The reverse parameter still maintains sort stability.**

### Custom Sorting using __lt__()

The sort routines are guaranteed to use `__lt__()` when making comparisons between two objects. So, it is easy to add a standard sort order to a class by defining an `__lt__()` method:

```py
Student.__lt__ = lambda self, other: self.age < other.age
```

```py
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
```

### Sequences Compare Rules

[Value comparisons](https://docs.python.org/3/reference/expressions.html#value-comparisons)

Lexicographical comparison between built-in collections works as follows:

- For two collections to compare equal, they must be of the same type, have the same length, and each pair of corresponding elements must compare equal (for example, `[1,2] == (1,2)` is false because the type is not the same).
- Collections that support order comparison are ordered the same as their first unequal elements (for example, `[1,2,x] <= [1,2,y]` has the same value as `x <= y`). If a corresponding element does not exist, the shorter collection is ordered first (for example, `[1,2] < [1,2,3]` is true).

## Patterns

### Indexed Array

when you have to record the element's index in an array for futher purpose.

```py
nums = [(n,i) for i,n in enumerate(nums)]
```

### Middle of low and high

```py
mid = low + high // 2
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
