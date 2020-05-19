### Overview

This repo explores rapid-prototyping [extractive](https://ieeexplore.ieee.org/abstract/document/8817040)/[abstractive](https://ai.googleblog.com/2016/08/text-summarization-with-tensorflow.html) text summarization methods. Primary method used for extractive summarization is [cosine similarity](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CosineSimilarity) and [ranking](https://arxiv.org/abs/1703.09902v1). Currently the application is wrapped in a REST API, plans for next features includes wrapping in protobuf/grpc system for much faster api calls, using pre-trained word2vec systems, and caching.

### Dependencies:

- Docker
- Docker compose
- python 3

### Intructions to run:

1) `docker-compose build`
2) `docker-compose up`
3) App running on port http://0.0.0.0:80/
4) POST to http://0.0.0.0:80/api/v1/getsummary using: 
  `
    {
      "text": "Text you wish to summarize"
    }
  `
  or 
  `
    {
      "url": "Url of any article"
    }
  `  
  
