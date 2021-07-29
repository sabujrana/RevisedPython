import example
import mymoduel
import imp

print(example.addition(2,3))
mymoduel
imp.reload(mymoduel)
mymoduel

mymoduel
# will execute only once in one session, that means our module was imported only once
# if our module changedd during the course of program we would have to reload it
# we can use reload() funcito of imp module to to reload module##(deprecated)


