info = {}
info["name"] = "kevinn"
info["age"] = "29"
info["country"] = "Canada"
info["lang"] = "Python"

for key,data in info.iteritems():
    if key == "name":
        print "my name is",data
    if key == "age":
        print "I am",data, " years old"
    if key == "country":
        print "I was born in ",data
    if key == "lang":
        print "My favorite language so far is... ",data


