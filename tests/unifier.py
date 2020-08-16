import sys
sys.path.insert(0, '..')
from logic.fol import Unifier

def main():
  p_file_path = 'data/p.txt'; q_file_path = 'data/q.txt'

  p = ''; q = ''
  with open(p_file_path) as f:
    for l in f:
      p = l

  with open(q_file_path) as f:
    for l in f:
      q = l

  unifier = Unifier()
  mgu = unifier.unify(p, q)

  if mgu is None:
    print("False")
  else:
    print("True\n")
    print("\n".join(map(str, mgu)))

if __name__ == '__main__':
  main()