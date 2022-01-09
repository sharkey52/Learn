import time
import os
def clear():
    os.system( 'cls' )
n = 20
while n > 0:
  n = n - 1
  x = ' ' * n
  rudolph = (x + '             *    *        \n'+x+'               \  /         \n'+x+'           *  *   *   *     \n'+x+'            \__\_/___/      \n'+x+'         0-_/. ()__-------  \n'+x+'          \____           / \n'+x+'            \_ \_ ___   /   \n'+x+'             /   |   | |    \n'+x+'            /    |   | |  ')  
  clear()
  print(rudolph)
  time.sleep(1)
