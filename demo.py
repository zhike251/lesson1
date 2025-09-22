from api import api
def hello():
  print("hello")

def byebye():
  print("byebye")

if __name__=="main":
  hello()
  a=input()
  a = api(a)
  print(a)
  byebye()
