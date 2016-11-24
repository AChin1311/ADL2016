
with open("Data/atis.train.w-intent.iob", 'r') as f:
  data = f.readlines()
  labels = []
  seq_ins = []
  seq_outs = []
  for line in data:
    line = line.split()
    labels.append(line[-1])
    print(line[-1])
    start = line.index("BOS")
    end =line.index("EOS")
    seq_ins.append(' '.join(line[start:end]))
    seq_outs.append(' '.join(line[end+1:-1]))


  with open("Data/train/train.label", "w+") as f1:
    f1.write('\n'.join(labels))
  with open("Data/train/train.seq.in", "w+") as f1:
    f1.write('\n'.join(seq_ins))
  with open("Data/train/train.seq.out", "w+") as f1:
    f1.write('\n'.join(seq_outs))


with open("Data/atis.test.iob", 'r') as f:
  data = f.readlines()
  seq_ins = []
  for line in data:
    line = line.split()
    seq_ins.append(' '.join(line[0:-1]))
  with open("Data/test/test.seq.in", "w+") as f1:
    f1.write('\n'.join(seq_ins))
