import sys

para_lst = []
parsed_para = []
parsed_value = []
parsed_func = []
with open(sys.argv[1], "r") as data_file:    
  data = data_file.readlines()
  for s in data:
    p = s.find("(")
    func = s[0:p]

    para = []
    value = []
    p += 1
    q = s.find(")")
    s = s[p:q]
    lst = s.split(";")

    for item in lst:
      if item == '':
        continue
      if item.find("=") != -1:
        item = item.split("=")
        para.append(item[0])
        value.append(item[1])
        if item[0] not in para_lst:
          para_lst.append(item[0]) 
      else:
        para.append(item)
        value.append(item)
        if item not in para_lst:
          para_lst.append(item)

    parsed_para.append(para)
    parsed_value.append(value)
    parsed_func.append(func)
    #print(func, para, value, line[2])

para_lst = []
with open("para_lst.txt", "r") as f:
  data = f.readlines()
  para_lst = data[0].split()
print(para_lst)

with open("mytest.en", "w+") as fen:
    for i in range(len(parsed_func)):
      out = parsed_func[i] + " "
      for p in para_lst:
        if p in parsed_para[i]:
          out += parsed_value[i][parsed_para[i].index(p)] + " "
        else:
          out += "NULL "
      out += "\n"
      fen.write(out)
