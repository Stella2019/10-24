"""
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
 

示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
 

说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。


本题比较筒单，基本上是数据结构的复习，栈的顺序为后进先出，而队列的顺序为先进先出。
使用两个实现队列，一个元素需要经过两个栈才能出队列，在经过第一个栈时元素顺序被反转，经过第个栈时再次被反转，
此时就是先进先出顺序。
"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #初始化两个列表，当作栈来使用
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        #队列的 push 操作
        self.stack_in.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        #队列的 pop 操作
        if self.stack_out:
            return self.stack_out.pop()
        else:
            #将 stack_in 的数据全部 push 进 stack_out 中，然后 stack out 的顺序和队列 pop 的顺序一致
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack_out:
            return self.stack_out[-1]
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack_in and not self.stack_out


"""
上面的实现是一个非常简单的思路，但是对于 python 语言来讲，却没有那么麻烦，我们并不需要用两个栈来解決问题，因为 python 的 ist 既可以当栈用也可以当队列用，非常强大。
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop(0)


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack == []








class Queue(object):
  def __init__(self):
    self.s1 = []
    self.s2 = []

  def enqueue(self, val):
    self.s1.append(val)

  def dequeue(self):
    if self.s2:
      return self.s2.pop()

    if self.s1:
      while self.s1:
        self.s2.append(self.s1.pop())
      return self.s2.pop()

    return None


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3 4