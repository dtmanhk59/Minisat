from abc import ABC, abstractmethod
import itertools

class Var(ABC):
  def __init__(self, id):
    self.__val = frozenset([frozenset([id])])

  def __and__(self, other):
    var = Var(1)
    # A & B
    var.__val = frozenset.union(self.__val, other.__val)
    # A & T = A
    if var.__val != frozenset([frozenset([1])]):
      var.__val = frozenset.difference(var.__val, frozenset([frozenset([1])]))
    # A & F = F
    if frozenset([-1]) in var.__val:
      var.__val = frozenset([frozenset([-1])])
    # A & (-A | ...) = F
    for r in var.__val:
      if len(r) == 1:
        v = -(int)(*r)
        for r1 in var.__val:
          if v in r1: 
            var.__val = frozenset([frozenset([-1])])
            break
    return var

  def __or__(self, other):
    var = Var(1)
    for x in self.__val:
      for y in other.__val:
        # A | B
        u = frozenset.union(x, y)
        # A | -A = T
        for x in u:
          if -x in u:
            u = frozenset({1})
            break
        # A | F = A
        if u != frozenset([-1]):
          u = frozenset.difference(u, frozenset([-1]))
        # A | T = T
        if 1 in u:
          u = frozenset([1])
        c = Var(1)
        c.__val = frozenset([u])
        var = c & var
    return var

  def __neg__(self):
    k = Var(1)
    for li in itertools.product(*self.__val):
      c = Var(-1)
      for i in li:
        ci = Var(-i)
        c |= ci
      k &= c
    return k

  def __str__(self):
    ret = []
    for d in self.__val:
      ret.append(" | ".join(map(str,d)))
    return "(" + ") & (".join(ret) + ")"

  def __xor__(self, other):
    return (self | other) & (-self | -other)

  def __rshift__(self, other):
    return -self | other

T = Var(1)
F = Var(2)

if __name__ == "__main__":
  c = Var(-2) & F
  print(c)

