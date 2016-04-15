def size(int_type):
   length = 0
   count = 0
   while (int_type):
       count += (int_type & 1)
       length += 1
       int_type >>= 1
   return count

def length(int_type):
   length = 0
   count = 0
   while (int_type):
       count += (int_type & 1)
       length += 1
       int_type >>= 1
   return length