import sys
import unittest
sys.path.insert(0, '..')
from logic.fol import Unifier

class UnifierTests(unittest.TestCase):
  def test_formula_single_mgu(self):
    p = 'knows(John,x)'
    q = 'knows(John,Jane)'

    unifier = Unifier()
    mgu = unifier.unify(p, q)
    
    for u in mgu:
      self.assertEqual(str(u), 'x/Jane')
      
  def test_relation_multiple_mgu(self):
    p = 'parents(x,father(x),mother(Bill))'
    q = 'parents(Bill,father(Bill),y)'

    gt = ['x/Bill', 'y/mother(Bill)']
    unifier = Unifier()
    mgu = unifier.unify(p, q)
    
    for u, g in zip(mgu, gt):
      self.assertEqual(str(u), g)

if __name__ == '__main__':
  unittest.main()
