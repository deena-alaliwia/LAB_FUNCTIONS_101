


def triangle( n:int):
    ''' this function will print a triangle patren '''
    for i in range(n,0,-1):

      for  j in range(i,0,-1):
         print(j ,end="")
      print()     
        
print (triangle.__doc__)  
    
num =int(input("enter a posetive number to display a triangle pattern"))

triangle(num) 
  