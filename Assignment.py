# Assignment
# }concatenate two lists Index-wise:
# list1 = ["M", "na", "i", "Ke"] 
# list2 = ["y", "me", "s", "lly"]
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)
# }concatenate two lists:
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# resList = [x+y for x in list1 for y in list2]
# print(resList)

# }turn every item in a list into it's square : Use list comprehension
# aList = [1, 2, 3, 4, 5, 6, 7]
# aList =  [x * x for x in aList]
# print(aList)

# }use list to display:[500,400,300,200,100]
# aList = [100, 200, 300, 400, 500]
# aList = aList[::-1]
# print(aList)

'''}iterate both lists simultaneouly such that list1
will display in original order and list2 display in reverse order'''
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for x, y in zip(list1, list2[::-1]):
#     print(x, y)

'''}remove empty strings from the  list of items of strings:
we make use of the filter()function to remove none type from the list'''
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# resList = list(filter(None, list1))
# print(resList)

# }use the append() method to add 7000 after 6000:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)


'''given a nested list extend it with adding sub list ["h","i","j"] in a such 
a way that it will look like:
["a", "b", ["c", ["d", "e", ["f", "g","h","i","j"], "k"], "l"], "m", "n"]'''

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# subList = ["h", "i", "j"]

# list1[2][1][2].extend(subList)
# print(list1)

'''find value 20 in the list, if present replace it with 200.only update the first
occurrance of a value:[5, 10, 15, 20, 25, 50, 20]'''

# list1 = [5, 10, 15, 20, 25, 50, 20]

# index = list1.index(20)
# list1[index] = 200
# print(list1)

'''remove all occurrance of 20 from the list:[5, 20, 15, 20, 25, 50, 20]'''
# list1 = [5, 20, 15, 20, 25, 50, 20]

# def removeValue(sampleList, val):
#    return [value for value in sampleList if value != val]
# resList = removeValue(list1, 20)
# print(resList)


# thisdict={"ten":10,"twenty":20,"thirty":30}
# print(thisdict)
# OR
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# sampleDict = dict(zip(keys, values))
# print(sampleDict)

'''merge two dictionaries into one'''
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = {**dict1, **dict2}
# print(dict3)
# OR
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)

# Access or get the value of key 'history'
thisdict={
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}
print(thisdict["class"]["student"]["marks"]["history"])
