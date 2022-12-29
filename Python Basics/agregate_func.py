""""" aggregate func is a func where multiple values are grouped together to form a single summary value.
these include max(), min(), sum(), mean(), median(), mode()
"""
import statistics as s

list1 = [1,2,3,4,5,6,7,8,9,10]

print("maximum ",  max(list1))
print("minimum ", min(list1))

print("median ", s.median(list1))

print("mean", s.mean(list1))
