Purpose of this repo is to rapid-prototype extractive/abstractive text summarization methods. Primary method used for extractive summarization is [cosine similarity](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CosineSimilarity) and [ranking](https://arxiv.org/abs/1703.09902v1). Plans for next features includes wrapping in protobuf/grpc system for much faster api calls, using pre-trained word2vec systems, and caching.

Dependencies:

- Docker
- Docker compose
- python 3

Intructions to run:

1) `docker-compose build`
2) `docker-compose up`
