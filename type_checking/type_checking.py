

"""
Demonstrates the use of mypy for type checking.

In command line type  python -m mypy script.py

1. Annotations on there own dont do anything.
2. A linter like mypy is used to perform the type checking
"""

# Optioanl provides for a given return type or None

from typing import Callable, List, Optional, Union, Sequence, overload, TypeVar, AnyStr, Protocol

def process(fnc: Callable, items: Union[List[int], List[float]]) -> Union[List[int], List[float]]:
    return list(map(fnc, items))


def mul(num: int) -> int:
    return num * 2

def printer(item) -> None:
    print(item)

printer(process(mul, [1,2,3,4,5,6]))

# default argument with type hint
def say_something(string: str = "Hello") -> None:
    print(string)



class Foo:
    def __init__(self, id):
        self.id = id


@overload
def get_foo(foo_id: None) -> None:
    pass

@overload
def get_foo(foo_id:int) -> Foo:
    pass

def get_foo(foo_id: Optional[int]) -> Optional[Foo]:
    if foo_id is None:
        return None
    return Foo(foo_id)


def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b

concat('foo', b'bar')
concat(3, 6)


class Renderable(Protocol):
    def render(self) -> str:
        ...

def render(obj: Renderable) -> str:
    return obj.render()

class Bar:
    def render(self) -> str:
        return "Bar!"

render(Bar())
render(3)
