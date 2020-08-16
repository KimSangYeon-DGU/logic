class Variable:
  def __init__(self, variable_name):
    if variable_name[0].isupper():
      raise(Exception('Variable name should starts with lower-case!'))
    self.variable_name = variable_name

  def __eq__(self, other):
    return isinstance(other, Variable) \
        and self.variable_name == other.variable_name

  def __ne__(self, other):
    return not self.__eq__(other)

  def __str__(self):
    return self.variable_name

  def __repr__(self):
    return str(self)

  def __hash(self):
    return str(self).__hash__()

  def occurs_in(self, other):
    if isinstance(other, Variable) \
        and self.__eq__(other):
      return True
    if isinstance(other, Formula) \
        and self.__str__() in other.__str():
      return True
    return False

class Constant:
  def __init__(self, constant_name):
    if constant_name[0].islower():
      raise (Exception("Constant name starting with upper-case!"))
    
    self.constant_name = constant_name

  def __eq__(self, other):
    return isinstance(other, Constant) \
        and self.constant_name == other.constant_name

  def __ne__(self, other):
    return not self.__eq__(other)

  def __str__(self):
    return self.constant_name

  def __repr__(self):
    return str(self)

  def __hash__(self):
    return str(self).__hash__()

class Formula:
  def __init__(self, operator, arguments):
    self.operator = operator
    self.arguments = arguments

  def __str__(self):
    return '{0}({1})'.format(self.operator, \
        ', '.join(map(str, self.arguments)))

  def __repr__(self):
    return str(self)

  def __hash__(self):
    return str(self).__hash__()

  def __eq__(self, other):
    if not isinstance(other, Formula):
      return False
    if self.operator != other.operator:
      return False
    if len(self.arguments) != len(other.arguments):
      return False

    return all([a1 == a2 for a1, a2 \
        in zip(self.arguments, other.arguments)])


  def __ne__(self, other):
    return not self.__eq__(other)
