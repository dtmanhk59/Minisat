import itertools

class Var:
  def __init__(self, id):
    self.data = frozenset([frozenset([id])])

  def __and__(self, other):
    cnf = Var(1)
    cnf.data = frozenset.union(self.data, other.data)
    if cnf.data != frozenset([frozenset([1])]):
      cnf.data = frozenset.difference(cnf.data, frozenset([frozenset([1])]))
    if frozenset([-1]) in cnf.data:
      cnf.data = frozenset([frozenset([-1])])
    for u in cnf.data:
      if len(u) == 1:
        for e in u:
          for u1 in cnf.data:
            if -e in u1:
              cnf.data = frozenset([frozenset([-1])])
    return cnf

  def __or__(self, other):
    cnf = Var(1)
    for x in self.data:
      for y in other.data:
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
        c.data = frozenset([u])
        cnf = c & cnf
    return cnf

  def __neg__(self):
    k = Var(1)
    for li in itertools.product(*self.data):
      c = Var(-1)
      for i in li:
        ci = Var(i)
        c |= ci
      k &= c
    return k

if __name__ == "__main__":
  c = - (Var(-2) & Var(3) & (Var(4) | Var(5)))
  print(c.data)

