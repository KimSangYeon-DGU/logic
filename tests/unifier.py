# Unit test for the Unifier class

import sys
import unittest
sys.path.insert(0, '..')
from logic.fol import Unifier

class UnifierTests(unittest.TestCase):

  def test_parenthesis(self):
    p = 'man((x)'
    q = 'man(Socrates)'

    unifier = Unifier()
    
    with self.assertRaises(Exception):
      unifier.unify(p, q)

  def test_relation_single_mgu(self):
    p = 'man(x)'
    q = 'man(Socrates)'

    gt = ['x/Socrates']

    unifier = Unifier()
    mgu = unifier.unify(p, q)
    
    for u, g in zip(mgu, gt):
      self.assertEqual(str(u), g)

  def test_relation_multiple_mgu(self):
    p = 'parents(x,father(x),mother(Bill))'
    q = 'parents(Bill,father(Bill),y)'

    gt = ['x/Bill', 'y/mother(Bill)']

    unifier = Unifier()
    mgu = unifier.unify(p, q)
    
    for u, g in zip(mgu, gt):
      self.assertEqual(str(u), g)

  def test_relation_multiple_none_mgu(self):
    p = 'parents(x,father(x),mother(Jane))'
    q = 'parents(Bill,father(y),mother(y))'

    unifier = Unifier()
    mgu = unifier.unify(p, q)

    self.assertEqual(mgu, None)

  def test_formula_single_mgu(self):
    p = 'knows(John,x)'
    q = 'knows(John,Jane)'

    gt = ['x/Jane']

    unifier = Unifier()
    mgu = unifier.unify(p, q)
    
    for u, g in zip(mgu, gt):
      self.assertEqual(str(u), g)
  
  def test_formula_multiple_mgu(self):
    p = 'brother(John,x)'
    q = 'brother(y,Joseph)'

    gt = ['x/Joseph', 'y/John']

    unifier = Unifier()
    mgu = unifier.unify(p, q)
    
    for u, g in zip(mgu, gt):
      self.assertEqual(str(u), g)

if __name__ == '__main__':
  unittest.main()
