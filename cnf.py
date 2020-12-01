class Cnf:
  def __init__(self):
    self.data = frozenset([frozenset([1])])
  
  def cnf_false(self):
    cnf = Cnf()
    cnf.data = frozenset([frozenset([-1])])
    return cnf

  def cnf_true(self):
    cnf = Cnf()
    cnf.data = frozenset([frozenset([1])])
    return cnf

  def __and__(self, other):
    cnf = Cnf()
    # A & F = F
    if other.is_false():
      return self.cnf_false()
    
    # A & T = A
    if other.is_true():
      cnf.data = self.data
      return cnf
    
    # T & A = A
    if self.is_true():
      cnf.data = other.data
      return cnf

    # F & A = F
    if self.is_false():
      return self.cnf_false()

    # A & -A = F
    self_var = self.get_var()
    other_var = other.get_var()
    if self_var is not None and other_var is not None:
      if self_var == -other_var:
        return self.cnf_false()

    # A & A = A
    tmp = frozenset([])
    cnf.data = tmp.union(self.data, other.data)
    return cnf

  def __or__(self, other):
    cnf = Cnf()
    for self_u in self.data:
      for other_u in other.data:
        tmp = frozenset([])
        # A | A = A
        tmp = tmp.union(self_u, other_u)
        # A | -A = T
        for e in tmp:
          if -e in tmp:
            tmp = frozenset([1])
        # A | T = T
        if 1 in tmp:
          tmp = frozenset([1])
        # A | F = A
        tmp.symmetric_difference(frozenset([-1]))  
        cnftmp = Cnf()
        cnftmp.data = frozenset([tmp])
        cnf = (cnf & cnftmp)
    return cnf

  def is_true(self):
    return self.data == frozenset([frozenset([1])])
  
  def get_var(self):
    if len(self.data) == 1:
      for u in self.data:
        if len(u) == 1:
          for e in u:
            return e
    return None

  def is_false(self):
    return self.data == frozenset([frozenset([-1])])

  def __str__(self):
    print(self.data)
    return ""

if __name__ == "__main__":
  cnf1 = Cnf()
  cnf1.data = frozenset([frozenset([1, 2, 3, -1]), frozenset([5,6])])
  cnf2 = Cnf()
  cnf2.data = frozenset([frozenset([1]), frozenset([3])])
  cnf3 = cnf1 | cnf2
  print(cnf3)
