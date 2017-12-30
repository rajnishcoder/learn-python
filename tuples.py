######Tuples basics

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";

######## the empty tuple
tup = ()

######### tuple containing a single value
tup= (34,)  #you have to include a comma, even though there is only one value

######## Accessing Values in Tuples
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]: ", tup1[0];  #tup1[0]:  physics
print "tup2[1:5]: ", tup2[1:5]; #tup2[1:5]:  (2, 3, 4, 5)

####### Updating Tuples
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3; #(12, 34.56, 'abc', 'xyz')

###### Deleting Tuple Elements
tup = ('physics', 'chemistry', 1997, 2000);
print tup;
del tup; # so you just delete the whole tup
print "After deleting tup : ";
print tup; # it will give a NameError: name 'tup' is not defined


