import sys 

with open(sys.argv[1], 'r') as f:
  data = f.readlines()
  seq_ins = []
  for line in data:
    line = line.split()
    seq_ins.append(' '.join(line[0:-1]))
  with open("data/test/test.seq.in", "w+") as f1:
    f1.write('\n'.join(seq_ins))
