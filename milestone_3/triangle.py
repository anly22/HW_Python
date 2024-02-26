def get_triangle(rows: int) -> list[list[int]]:
   lst = []
   for i in range(rows):
      row = [1] * (i + 1) #create triangle of "1"s with correct number of rows and sections
      for j in range (i + 1): 
         if j != 0 and j != i:
            row[j] = lst[i - 1][j - 1] + lst[i - 1][j] #change "1" into correct number in sections where we need
      lst.append(row)
                     
   return lst 

rows = int(input("Please enter the number of rows:"))
print(*(get_triangle(rows)), sep = '\n') 

list_for_print = get_triangle(rows)
  
for element in list_for_print:
   print("{:^50s}".format(str(element).replace(",", "").replace("[", '').replace("]", "")))