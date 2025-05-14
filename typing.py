# Literals typealias
from abc import ABC, abstractmethod
import copy
from dataclasses import dataclass, field
from typing import Generic, Literal, Optional, Self, TypeAlias, TypeVar, overload,get_args
import typing


alias_t: TypeAlias = Literal["a", "b", "c"]
alia_list: list[alias_t] = list(get_args(alias_t))
alias_list_t: TypeAlias = list[alias_t]


# Overloading functions
@overload
def draw_trace(
    layerid: int,
    points: list[tuple[int, int]],
    *,
    width: Optional[float] = None,
) -> None: ...
@overload
def draw_trace(
    layerid: int,
    points: list[tuple[int, int]],
    via_layerid: int,
    via_index: int = 1,
    width: Optional[float] = None,
) -> None: ...


def draw_trace(
    layerid: int,
    points: list[tuple[int, int]],
    via_layerid: Optional[int] = None,
    via_index: Optional[int] = 1,
    width: Optional[float] = None,
) -> None: ...


# inheriting from dataclass
@dataclass
class Class1:
    var1: str
    var2: float
    var3: int = field(default=30, kw_only=True)
    var4: int = field(default=15, kw_only=True)

    def func1(self, other: "Class1") -> tuple[Self, Self]: ...
    def dict(self):
        return {k: getattr(self, k) for k in Class1.__annotations__}


@dataclass
class ChildClass1(Class1):
    var5: float = float("inf")
    var6: str = ""
    var7: int = 0
    var8: list["ChildClass1"] = field(default_factory=list)


ChildClass1Instance = ChildClass1("hej", 1.0, var3=2, var5=3)
ChildClass1Instance.dict()  # will return a dict only containing the variables also in the "Class1" class


# custom subclass which can be instaniated from parent instance
class CustomChildClass(object):
    """
    Creates a custom instance class that inherits from a parent class.
    This class is used to create a custom child class with additional functionality.
    """

    additional_var1: int
    additional_var2: list

    @classmethod
    def from_parent(cls, original_instance: object):
        new_instance = cls.__new__(cls)
        new_instance.__dict__ = original_instance.__dict__
        new_instance.additional_var1 = 1
        new_instance.additional_var2 = list("SomeObject(original_instance)")
        return new_instance

    def additional_func(self, var1: int) -> int:
        return self.additional_var1 + var1


# creating a abstract class to hold instances of type object and child-objects
G = TypeVar("G", bound=Class1)


class AbstractClass(list[G], Generic[G], ABC):
    @overload
    def __init__(self, init_pop: list[G]) -> None: ...
    @overload
    def __init__(self) -> None: ...

    def __init__(self, init_pop: Optional[list[G]] = None) -> None:
        if init_pop is None:
            init_pop = []
        super().__init__(init_pop)

    def copy(self, shallow=False) -> "AbstractClass":
        # return a copy of the population
        if shallow:
            return self.__class__(super().copy())
        return self.__class__(copy.deepcopy(self))

    @abstractmethod
    def func1(self, var1: int) -> float: ...

    @abstractmethod
    def func2(self) -> None: ...


class SpecificClass(AbstractClass[ChildClass1]):

    def func1(self, var1: int) -> float: ...

    def func2(self) -> None: ...
