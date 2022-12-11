# Lambda function is a small one line anonymous function that is defined without a name. Its format == <Lambda expression> : Arguments
# add10 = lambda x: x + 10
# add10(5)

#sorting of points
# points_2D = [(1,2), (15,1), (5, -1), (10,4)]

#sort by x values
# points_2D_sortedx = sorted(points_2D)
# print("Points sorted acc. to x: ", points_2D_sortedx)

# #sort by y values 
# points_2D_sortedy = sorted(points_2D, key= lambda x: x[1])
# print("Points sorted acc. to y: ", points_2D_sortedy)

## map function transforms each element with a function ##
## format >>> map(func, sequence) ##

#using lambda function
# a = [1,2,3,4,5]
# b = map(lambda x: x*2, a)
# print(list(b))


## Using list comprehension
# c = [x*2 for x in a]
# print(c)

## filter(func, sequence), this will function must return true or false and will return all the elements for which 
# functions evaluates to true

## Using lambda Function
# a = [1,2,3,4,5]
# b = filter(lambda x: x%2==0, a)
# print(list(b))

# ## using list comprehension
# c = [x for x in a if x%2==0]
# print(c)

## reduce(func, sequence), it repeatedly applies to the elements and return a single value
# from functools import reduce
# a = [1,2,3,4,5]
# product_a = reduce(lambda x,y: x*y, a)
# print(product_a)
