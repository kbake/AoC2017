# Had to resort to following someone else's solution
# ...will try to write comments so it makes sense to me
n = 277678
i = 1
# Since each bottom right hand corner is the sum of odd squares,
# find the one closest to our value
while i*i < n:
    i += 2
# Now that we have the bottom right hand corner closest to our number
# we find each corner value
pivots = [i*i - k*(i-1) for k in range(4)]
# Now loop over each corner and get the distance from that corner to our number
for pivot in pivots:
    dist = abs(pivot - n)
    # We have our answer when the distance is less than half the size of the...corner...not
    # getting how this part works
    if dist <= (i-1)/2:
      print(i-1-dist)
      break
