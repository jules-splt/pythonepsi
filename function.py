def several_zeros():
   a=[]
   for i in range(10):
         a.append(0)
   print(a)
   
def several_zeros_custom(nb_zeros = 10):
   a=[]
   for i in range(nb_zeros):
         a.append(0)
   print(a)
   
def matrix(rows, cols):
   liste=[]
   matrix=[]
   for i in range(rows):
         liste.append(0)
   for j in range(cols):
         matrix.append(liste)
   print(matrix)
   
class Matrix():
   def __init__(self,rows,cols):
      self.__rows = rows
      self.__cols = cols
      self.__matrix = matrix(self.__rows, self.__cols)
   def get_value(self,row,col):
      return self.__matrix[row][col]
   def __eq__(self, other:int) -> bool:
      return self.__matrix == other.__matrix
   
#Trie a bulle      
def my_sort(my_list: [int])-> [int]:
   tableau = my_list
   for i in range(len(tableau)-1) :
        for j in range(len(tableau)-1-i):
            if tableau[j+1] < tableau[j] :
                tableau[j+1], tableau[j] = tableau[j], tableau[j+1]
   print(tableau)
   
if __name__ == '__main__':
   #several_zeros()
   #several_zeros_custom(4)
   matrix(4,7)
   #my_sort([3,5,7,4,1,8])