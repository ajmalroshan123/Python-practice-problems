class foo():
   def __init__(self):
     self.variable = 'Foo'
     print(self.varible)

   def method(self, arg1, agr2):
     print("In method (args): ",arg1, arg2)

  def method2(self):
      self.method(3,4)


a = foo()
a.method(1,2)
a.method2()

     
