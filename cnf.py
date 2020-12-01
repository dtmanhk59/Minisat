class Cnf:
  def __init__(self):
    self.true = frozenset([frozenset([1])])
    self.false = frozenset([frozenset([-1])])
    self.data = self.true
  
  def __and__(self, other):
    cnf = Cnf()
    # A & F = F
    if other.is_false():
      return self.false
    
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
      return self.false

    # A & -A = F
    self_var = self.get_var()
    other_var = other.get_var()
    if self_var is not None and other_var is not None:
      if self_var == -other_var:
        return self.false

    # A & A = A
    cnf.data = self.data.union(self.data, other.data)
    return cnf

  def __or__(self, other):
    pass

  def is_true(self):
    return self.data == self.true
  
  def get_var(self):
    if len(self.data) == 1:
      for u in self.data:
        if len(u) == 1:
          for e in u:
            return e
    return None

  def is_false(self):
    return self.data == self.false

  def __str__(self):
    print(self.data)
    return ""

if __name__ == "__main__":
  cnf1 = Cnf()
  cnf1.data = frozenset([frozenset([-2])])
  cnf2 = Cnf()
  cnf2.data = frozenset([frozenset([2])])
  cnf3 = cnf1 & cnf2
  print(cnf3)
