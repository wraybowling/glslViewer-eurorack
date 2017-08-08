import time, math

start = time.time()

while(True):
    val = math.sin( time.time() - start ) / 2 + 0.5
    print "u_1,", round(val, 2)
#    time.sleep(0.00001)
