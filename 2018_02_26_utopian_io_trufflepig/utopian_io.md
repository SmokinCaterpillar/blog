## Project Overview

[Steemit](https://steemit.com) can be a tough place for minnows, as new users are often called. I had to learn this myself. Due to the sheer amount of new posts that are published by the minute, it is incredibly hard to stand out from the crowd. Often even nice, well-researched, and well-crafted posts of minnows get buried in the noise because they do not benefit from a lot of influential followers that could upvote their quality posts. Hence, their contributions are getting lost long before one or the other whale could notice them and turn them into trending topics.

However, this user based curation also has its merits, of course. You can become fortunate and your nice posts get traction and the recognition they deserve. Maybe there is a way to support the Steemit content curators such that high quality content does not go unnoticed anymore. In fact, I developed a curation bot called `TrufflePig` to do exactly this with the help of Natural Language Processing and Machine Learning.


### The Concept

The basic idea is to use well paid posts of the past as training examples to teach a Machine Learning Regressor (MLR) how high quality Steemit content looks like. In turn, the trained MLR can be used to identify posts of high quality that were missed by the curation community and did receive much less payment than they deserved. We call this posts *truffles*.

The general idea of this bot is the following:

1. We train a Machine Learning regressor (MLR) using Steemit posts as inputs and the corresponding Steem Dollar (SBD) rewards and votes as outputs.

2. Accordingly, the MLR should learn to predict potential payouts for new, beforehand unseen Steemit posts.

3. Next, we can compare the predicted payout with the actual payouts of recent Steemit posts. If the Machine Learning model predicts a huge reward, but the post was merely paid at all, we classify this contribution as an overlooked truffle and list it in a daily top list to drive attention to it.

The deployed bot can be found here: https://steemit.com/@trufflepig. Furthermore, a recent top list [is this publication, for example](https://steemit.com/steemit/@trufflepig/daily-truffle-picks-2018-02-25), also shown in the image below:

![tolis](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/2018_02_26_utopian_io_trufflepig/toplist.jpg)

## Technology Stack

The project is written in **100% pure Python 3** and uses the following third-party libraries:

* [The official Steem Python library]((https://github.com/steemit/steem-python)): The library downloads past and recent Steemit posts from the Blockchain. In addition, Steem Python is used to comment under *truffle* posts and publish a daily top-list.

* [gensim](https://radimrehurek.com/gensim/models/lsimodel.html): Part of the feature encoding involves projecting Steemit posts into a vector space using the library's Latent Semantic Indexing functionality.

* [langdetect](https://pypi.python.org/pypi/langdetect): This library is used to filter for English only Steemit posts.

* [pyEnchant](https://pypi.python.org/pypi/langdetect): Counts spelling mistakes in posts.

* [pyphen](https://pypi.python.org/pypi/Pyphen): pyphen is used to compute the number of syllables of all words in Steemit posts.

* [pandas](https://pandas.pydata.org/): DataFrames are the standard data container format used throughout the project.

* [language-check](https://pypi.python.org/pypi/language-check): This library helps to identify and quantify grammar mistakes in Steemit posts.

* [Scikit-Learn](http://scikit-learn.org/stable/): Of course, the most widely used Python machine learning library is also applied in this project.


## Feature Encoding and Machine Learning

Usually the most difficult and involved part of engineering a Machine Learning application is the proper design of features. How are we going to represent the Steemit posts so they can be understood by a the Machine Learning regressor?

It is important that we use features that represent the content and quality of the post. We do not want to use author specific features such as the number of followers or past author payouts. Although I am quite certain (and I'll test this sometime soon) that these are incredibly predictive features of future payouts, these do not help us to identify overlooked and buried truffles.

I used some features that encode the style of the posts, such as number of paragraphs, average words per sentence, or spelling mistakes. Clearly, posts with many spelling errors are usually not high-quality content and are, to my mind, a pain to read. Moreover, I included readability scores like the [Flesch-Kincaid index](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests) to quantify how easy and nice a post is to read.

Still, the question remains, how are we going to encode the content of the post? How to represent the topic someone chose and the story an author told? The most simple encoding that is quite often used is the so called ['term frequency inverse document frequency'](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) (tf-idf). This technique basically encodes each document, so in our case Steemit posts, by the particular words that are present and weighs them by their (heuristically) normalized frequency of occurrence. However, this encoding produces vectors of enormous length with one entry for each unique word in all documents. Hence, most entries in these vectors are zeroes anyway because each document contains only a small subset of all potential words. For instance, if there are 150,000 different unique words in all our Steemit posts, each post will be represented by a vector of length 150,000 with almost all entries set to zero. Even if we filter and ignore very common words such as `the` or `a` we could easily end up with vectors having 30,000 or more dimensions.

Such high dimensional input is usually not very useful for Machine Learning. We rather want a much lower dimensionality than the number of training documents to effectively cover our data space. Accordingly, we need to reduce the dimensionality of our Steemit post representation. A widely used method is [Latent Semantic Analysis](https://en.wikipedia.org/wiki/Latent_semantic_analysis) (LSA), often also called Latent Semantic Indexing (LSI). LSI compression of the feature space is achieved by applying a Singular Value Decomposition (SVD) on top of the previously described word frequency encoding.

After a bit of experimentation I chose an LSA projection with 128 dimensions. In combination with the aforementioned style features, each post is, therefore, encoded as a vector with 150 entries.

For training, the bot reads posts between 7 and 17 days of age. These are first filtered and subsequently encoded. Usually, this leaves a training set of about 70,000 contributions. Too short posts, way too long ones, non-English, or posts with too many spelling errors were removed from the training set. The resulting matrix of size 70,000 by 150 is used as the input to a multi-output [Random Forest regressor from scikit learn](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html). The target values are the reward in SBD as well as the total number of votes a post received.

After the training, scheduled once a week, the Machine Learning regressor is used on a daily basis on recent posts between 2 and 26 hours old to predicted the expected reward and votes. Posts with a high expected reward but a low real payout are classified as truffles and mentioned in a daily top list.

A more detailed explanation together with a performance evaluation of the setup can also be found [in this post](https://steemit.com/steemit/@smcaterpillar/trufflepig-introducing-the-artificial-intelligence-for-content-curation-and-minnow-support).


### Future Roadmap

* I want to conduct further experiments with different ML regressors as well as feature encodings. I already made some experiments using [Doc2Vec](https://radimrehurek.com/gensim/models/doc2vec.html) instead of LSI. But this was not very fruitful. A more thorough investigation may improve the bot's judgment further.

* A very new feature of the bot is that posts voted by @cheetah are automatically excluded from any analysis. Besides, I would also like to make the bot respect and follow various spammer blacklists as used by @steemcleaners.

* It would be cool, if in addition to the daily top list, you could call the bot manually by commenting @trufflepig under your post. The bot would answer, give you an estimate of how much it thinks your post is worth, and upvote you in case of a *truffle*. Currently, *`TrufflePig`* is a daily batch job and needs to be turned into a service instead.

* Parts of the bot, especially the LSI encoding, could be reused for information retrieval and a Steemit recommendation system. For example, read recommendations could be given like: *If you enjoyed this post you might also be interested in the following contributions* ... This would be based on cosine similarity among different posts' LSI encodings.

* I am planning for a German version `*Trüffelschwein*` that particularly digs for *truffles* among German Steemit posts to support the *DACH* community. I'm open to other languages as well (kr!?), but would, of course, need help by another developer with the corresponding mother tongue :-).

### Open Source and Contributions

Finally, the project is freely available and open sourced at [my github profile](https://github.com/SmokinCaterpillar/TrufflePig). `*TrufflePig*` can be used by anyone in a non-commercial setting, please, check the LICENSE file.
Of course, contributions in form of pull-request, github issues, or feature requests are always welcome.

Cheers and have fun with:

![trufflepig](https://raw.githubusercontent.com/SmokinCaterpillar/TrufflePig/master/img/trufflepig17.png)

`*TrufflePig*`

(By the way, the bot's avatar has been created using https://robohash.org/)
