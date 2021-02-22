import camelcase
c = camelcase.CamelCase()
txt = "this method capitalizes the first letter of each word."
print(c.hump(txt))