import sys
if len(sys.argv) <2:
  print("Usage: python even_odd_count.py num1 num2 num3....")
    sys.exist(1)
numbers = sys.argv[1:]
even_count=0
odd_count=0
for n in numbers:
  try:
    num=int(n)
    if num % 2 ==0
       even_count +=1
    else:
       odd_count +=1
expect ValueError:
     print("Invalid number is skipped{n}")
print("Count of Even numbers:",even_count)
print("Count of Odd numbers:",odd_count)
