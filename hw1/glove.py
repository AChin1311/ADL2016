import tensorflow as tf
import tf_glove as glove
import os
import zipfile

def maybe_download(filename, expected_bytes):
  """Download a file if not present, and make sure it's the right size."""
  if not os.path.exists(filename):
    filename, _ = urllib.request.urlretrieve(url + filename, filename)
  statinfo = os.stat(filename)
  if statinfo.st_size == expected_bytes:
    print('Found and verified', filename)
  else:
    print(statinfo.st_size)
    raise Exception(
                'Failed to verify ' + filename + '. Can you get to it with a browser?')
  return filename


# Read the data into a list of strings.
def read_data(filename):
  """Extract the first file enclosed in a zip file as a list of words"""
  with zipfile.ZipFile(filename) as f:
    data = tf.compat.as_str(f.read(f.namelist()[0])).split()
    return data

filename = maybe_download('corpus/text8.zip', 31344016)
data = read_data(filename)

gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.2)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

print("========init GloveModel========")
model = glove.GloVeModel(embedding_size=128, context_size=10, learning_rate=0.1)
print("=======fit to corpus========")
corpus = []
corpus.append(data)
model.fit_to_corpus(corpus)
print("=======start training========")
model.train(num_epochs=10)
print("=======finish training========")
words = model.words
print(words)
with open("tmp/glove", "w") as f:
  for w in words:
    s = w + " " + ' '.join([str(x) for x in model.embedding_for(w)]) + "\n"
    print(s)
    f.write(s)

