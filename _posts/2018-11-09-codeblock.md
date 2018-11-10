---
author: apher
type: blog
description: Markdown code block test
---

The following are example blocks of code from different languages, the purpose of this is to setup and test the Redcarpet Code Block system.

## HTML
```html
<h1>Hello there!fghjdfghjhgfdfghjhfdfghjfdfghjhgfdfghgfdfghgfdgh</h1>
<div class="test">
  <ul>
    <li>Hewwo</li>
    <li>OwO</li>
  </ul>
</div>
```

## PYTHON
```python
bool1 = false;

def main():
  print('Hello')
  if bool1 == true:
    print('IT IS', bool1

main()
```

## JAVASCRIPT
```javascript
function trigger() {

  document.getElementById("hover").addEventListener("mouseover", popup);

  function popup(){
    alert("Welcome to my WebPage!!!");
  }
}
```

## C# #
```c#
using System;
namespace HelloWorld {
  class hello {
    static void Main() {
      Console.WriteLine('Hello World!');

      console.WriteLine('Press any key to exit.')
      console.ReadKey();
    }
  }
}
```

## Ruby
```ruby
n = 7
def fibonacci(n)
  if n == 1
    1
  elseif n == 2
    1
  else
    fibonacci(n-1) + fibonacci(n-2)
  end
end

puts "#{n}'s fibonacci value is #{fibonacci(n)}"
```
