import time

# time.altzone()
print("time.altzone %d" % time.altzone, "\n")

# time.asctime([tupletime])
t = time.localtime()
print("asctime is", time.asctime(t), "\n")


