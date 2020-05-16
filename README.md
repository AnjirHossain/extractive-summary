Purpose of this repo is to rapid-prototype extractive/abstractive text summarization methods. Primary method used for extractive summarization is [cosine similarity](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CosineSimilarity) and [ranking](https://arxiv.org/abs/1703.09902v1). Plans for next features includes wrapping in protobuf/grpc system for much faster api calls, using pre-trained word2vec systems, and caching.

Dependencies:

- Docker
- Docker compose
- python 3

Intructions to run:

1) `docker-compose build`
2) `docker-compose up`
3) App running on port http://0.0.0.0:80/
4) Post to http://0.0.0.0:80/api/v1/getsummary using: 
  `
    {
      "text": "Text you wish to summarize"
    }
  `
  
 Example results:
 
 Source:
 [How COVID will end via The Atlantic](https://www.theatlantic.com/health/archive/2020/03/how-will-coronavirus-end/608719/)
 
 Target:
 
 "“The ideas are out there, but the debates will be more acute over the next few months because of the fluidity of the moment and willingness of the American public to accept big, massive changes.” One could easily conceive of a world in which most of the nation believes that America defeated COVID-19. By the end of the summer, the pandemic will have directly killed 2.2 million Americans, notwithstanding those who will indirectly die as hospitals are unable to care for the usual slew of heart attacks, strokes, and car accidents. Those tests have been slow to arrive because of five separate shortages: of masks to protect people administering the tests; of nasopharyngeal swabs for collecting viral samples; of extraction kits for pulling the virus’s genetic material out of the samples; of chemical reagents that are part of those kits; and of trained people who can give the tests"
