import itertools

class Var:
  def __init__(self, id):
    self.__data = frozenset([frozenset([id])])

  def __and__(self, other):
    cnf = Var(1)
    cnf.__data = frozenset.union(self.__data, other.__data)
    if cnf.__data != frozenset([frozenset([1])]):
      cnf.__data = frozenset.difference(cnf.__data, frozenset([frozenset([1])]))
    if frozenset([-1]) in cnf.__data:
      cnf.__data = frozenset([frozenset([-1])])
    for u in cnf.__data:
      if len(u) == 1:
        for e in u:
          for u1 in cnf.__data:
            if -e in u1:
              cnf.__data = frozenset([frozenset([-1])])
    return cnf

  def __or__(self, other):
    cnf = Var(1)
    for x in self.__data:
      for y in other.__data:
        u = frozenset.union(x, y)
        for x in u:
          if -x in u:
            u = frozenset({1})
            break
        if u != frozenset([-1]):
          u = frozenset.difference(u, frozenset([-1]))
        if 1 in u:
          u = frozenset([1])
        c = Var(1)
        c.__data = frozenset([u])
        cnf = c & cnf
    return cnf

  def __neg__(self):
    k = Var(1)
    for li in itertools.product(*self.__data):
      c = Var(-1)
      for i in li:
        ci = Var(-i)
        c |= ci
      k &= c
    return k

  def print(self):
    print (self.__data)
    return ""

  def __str__(self):
    ret = []
    for d in self.__data:
      ret.append(" | ".join(map(str,d)))
    return "(" + ") & (".join(ret) + ")"

  def __xor__(self, other):
    """
    ^
    """
    return (self | other) & (-self | -other)


if __name__ == "__main__":
  c = Var(2) ^ Var(3) ^ Var(4)
  print(c)

