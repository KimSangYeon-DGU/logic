from .term import Constant, Variable, Formula

class Unifier:
  def unify(self, p, q):
    if not isinstance(p, Formula):
      self.p = self.parse_formula(p)
    else:
      self.p = p
  
    if not isinstance(q, Formula):
      self.q = self.parse_formula(q)
    else:
      self.q = q

    mgu = self.unify_with_occurrence_check(self.p, self.q)
    if mgu != None:
      mgu.sort()
    return mgu

  def unify_with_occurrence_check(self,
                                  formula1,
                                  formula2,
                                  mgu = []):
    if mgu is None:
      return None
    elif formula1 == formula2:
      return mgu
    elif isinstance(formula1, Variable):
      return self.unify_variable(formula1, formula2, mgu)
    elif isinstance(formula2, Variable):
      return self.unify_variable(formula2, formula1, mgu)
    elif isinstance(formula1, Formula) and isinstance(formula2, Formula):
      if type(formula1) != type(formula2) or formula1.operator != formula2.operator or len(formula1.arguments) != len(formula2.arguments):
        return None
      else:
        for a, b in zip(formula1.arguments, formula2.arguments):
          mgu = self.unify_with_occurrence_check(a, b, mgu)
        return mgu
    else:
      return None

  def unify_variable(self, var, exp, mgu):
    for s in (sub for sub in mgu if sub.variable == var):
      return self.unify_with_occurrence_check(s.replacement,
                                              exp,
                                              mgu)
    t = self.substitute(mgu, exp)
    if self.occurs_in(var, t) and isinstance(t, Formula):
      print("\nCannot unify - infinte loop exception!!!")
      return None
    else:
      s = Substitution(var, t)
      mgu = mgu+[s]
      for q in (sub for sub in mgu if sub.replacement == s.variable):
        mgu.remove(q)
        new  = Substitution(q.variable, s.replacement)
        mgu = mgu+[new]
      for r in (sub for sub in mgu if isinstance(sub.replacement, Formula)):
        mgu.remove(r)
        a = self.substitute(mgu, r.replacement)
        b = Substitution(r.variable, a)
        mgu = mgu+[b]
      for s in (sub for sub in mgu if (sub.variable == sub.replacement)):
        mgu.remove(s)
      return mgu
    
  def parse_formula(self, sentence):
    s = sentence
    if s.count('(') != s.count(')'):
      raise(Exception('Parentheses in a sentence should be pairs'))
    pp_count = 0 # Count of the expected pair of parentheses.
    begin = 0
    op, args = None, []
    for end, c in enumerate(s):
      if c == '(':
        if op is None:
          op = s[:end]
          begin = end + 1
        pp_count += 1
      elif c == ')':
        if pp_count == 1:
          if end > begin:
            args.append(s[begin:end])
          begin = end + 1
        pp_count -= 1
      elif c == ',':
        if pp_count == 1:
          if end > begin:
            args.append(s[begin:end])
        begin = end + 1

    if op is None:
      if s[0].islower():
        return Variable(s)
      else:
        return Constant(s)

    return Formula(op, list(map(self.parse_formula, args)))		
      
  def substitute(self, sub, expr):
    for s in (x for x in sub if self.occurs_in(x.variable, expr)):
      if isinstance(expr, Variable):
        expr = s.replacement
      else:
        expr.arguments = [self.substitute(sub, e) for e in expr.arguments]

    return expr
	
  def occurs_in(self, var, expr):
    if var == expr:
      return True
    if not isinstance(expr, Formula):
      return False
    return any([self.occurs_in(var, e) for e in expr.arguments])

class Substitution:
  def __init__(self, variable, replacement):
    self.variable = variable
    self.replacement = replacement
    
  def __str__(self):
    return str(self.variable) + '/' + str(self.replacement)
  
  def __lt__(self, other):
    return str(self.variable) < str(other.variable)
