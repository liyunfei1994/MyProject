#   对装饰器decorator的理解

在Python中，装饰器就像下面这样：

```python
@dec
def func():
	pass
```

理解装饰器最好的方法就是理解它要解决什么问题。

1.   提出问题

   定义一个函数：

   ```python
   def add(x, y=10):
   	return x+y
   ```

   并且像下面这样使用这个函数：

   ```python
   from time import time
   def add(x, y=10):
   	return x + y
   
   print("add(10)", add(10))
   print("add(20, 30)", add(20, 30))
   print("add('a','b')", add('a', 'b'))
   ```

   Output:

   ```python
   add(10)   20
   add(20, 30)   50
   add('a' ,'b')   ab
   ```

   **假如说我们想测试这个加法函数运行的时间是多少**

   ```python
   from time import time
   
   def add(x, y=10):
   	return x + y
   
   before = time()
   print('add(10)', add(10))
   after = time()
   print('time taken: ', after - before)
   
   before = time()
   print('add(20, 30)', add(20, 30))
   after = time()
   print('time taken: ', after - before)
   
   before = time()
   print('add("a", "b")', add("a", "b"))
   after = time()
   print('time taken: ', after - before)
   ```

   Output:

   ```python
   add(10) 20
   time taken:  6.699562072753906e-05
   add(20, 30) 50
   time taken:  6.9141387939453125e-06
   add("a", "b") ab
   time taken:  6.9141387939453125e-06
   ```

   **我们最讨厌的就是复制粘贴了，这样显得很低级，效率也很低，一定有更好的办法**

   **没错，我们可以将测试时间的功能放在add函数内部**

   ```python
   from time import time
   
   def add(x, y=10):
   	before = time()
   	rv = x + y
   	after = time()
   	print('time taken: ', after - before)
   	return rv
   
   print('add(10)',         add(10))
   print('add(20, 30)',     add(20, 30))
   print('add("a", "b")',   add("a", "b"))
   ```

   这样比之前好很多了，但是假如我们有另一个函数怎么办？另一个函数内部，是否也需要将测试时间的功能添加进去，是不是也有点繁琐？

   ```python
   def sub(x, y=10):
   	return x - y
   ```

   记住：**add和sub都是函数，我们利用这一点**

   我们将一个函数作为参数传给timer函数，timer函数经过计算，计算的结果值返回

   ```python
   def timer(func, x, y=10):
   	before = time()
   	rv = func(x, y)
   	after = time()
   	print('time taken: ', after - before)
   	return rv
   ```

   **非常好，比之前好多了，但是，我们不得不将所有的东西都塞到这个timer函数里，像这样：**

   ```python
   print("add(10)", timer(add, 10))
   ```

   **并且，默认的参数值是10，是不是有更好的手段？**

   **我们新建一个新的timer函数，包含另一个函数，并且返回被包含的函数**

   ```python
   def timer(func):
   	def f(x, y=10):
   		before = time()
   		rv = func(x, y)
   		after = time()
   		print('time taken: ', after - before)
   		return rv
   	return f
   ```

   **_注意：这里我们返回了被包含的函数本身_**

   这样我们就可以用timer去包含add和sub函数了

   ```python
   add=timer(add)
   ```

   像下面这样使用：

   ```python
   from time import time
   def timer(func):
   	def f(x, y=10):
   		before = time()
   		rv = func(x, y)
   		after = time()
   		print('time taken: ', after - before)
   		return rv
   	return f
   
   def add(x, y=10):
   	return x + y
   add = timer(add)
   
   
   def sub(x, y=10):
   	return x - y
   sub = timer(sub)
   
   print('add(10)',         add(10))
   print('add(20, 30)',     add(20, 30))
   print('add("a", "b")',   add("a", "b"))
   print('sub(10)',         sub(10))
   print('sub(20, 30)',     sub(20, 30))
   ```

   Output:

   ```python
   time taken:  0.0
   add(10) 20
   time taken:  9.5367431640625e-07
   add(20, 30) 50
   time taken:  0.0
   add("a", "b") ab
   time taken:  9.5367431640625e-07
   sub(10) 0
   time taken:  9.5367431640625e-07
   sub(20, 30) -10
   ```

   这里我们做了什么？

   我们有一个函数add和sub，我们将这两个函数包裹进一个另一个函数timer中，并且timer函数将包裹进去的函数作为返回值返回。

   这就是装饰器的思想。

2. decorator

   用一种方式代替下面这样的写法

   ```python
   def add(x, y=10):
   	return x + y
   add = timer(add)
   ```

   就是装饰器：

   ```python
   @timer
   def add(x, y=10):
   	return x + y
   ```

   这两种写法其实是一回事。这就是Python中的装饰器。与其将**add=timer(add)**写在add函数的后面，我们用@timer这种语法将其写在了add函数的上面。

   修改之后，就像下面这样：

   ```python
   from time import time
   def timer(func):
   	def f(x, y=10):
   		before = time()
   		rv = func(x, y)
   		after = time()
   		print('time taken: ', after - before)
   		return rv
   	return f
   
   @timer
   def add(x, y=10):
   	return x + y
   
   @timer
   def sub(x, y=10):
   	return x - y
   
   print('add(10)',         add(10))
   print('add(20, 30)',     add(20, 30))
   print('add("a", "b")',   add("a", "b"))
   print('sub(10)',         sub(10))
   print('sub(20, 30)',     sub(20, 30))
   ```

3. 回顾

   *   装饰器是一个函数，包裹着另一个函数

   *   将另一个函数作为参数

   *    返回一个函数

   *    与将 add = timer(add) 放在add 函数之后相比，将@timer放在add函数的前面，效果是一样的

     