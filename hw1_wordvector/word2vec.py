from tensorflow.models.embedding import word2vec_optimized as word2vec

import numpy as np
import tensorflow as tf

def main(_):
  """Train a word2vec model."""
  opts = word2vec.Options()
  with tf.Graph().as_default(), tf.Session() as session:
    with tf.device("/cpu:0"):
      model = word2vec.Word2Vec(opts, session)
    for _ in xrange(opts.epochs_to_train):
      model.train()  # Process one epoch

    emb = session.run(model._w_in)  
    with open("tmp/word2vec", "w") as f:
      for i in range(len(model._id2word)):
        s = model._id2word[i] + " " + " ".join("{:f}".format(x) for x in emb[i]) + "\n"
        f.write(s)

if __name__ == "__main__":
  gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.2)
  sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
  tf.app.run()
