# Throwing User Comments into an Artificial Neural Network...
![doc2vec](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/2018_01_30_doc2vec/doc2vec.png)

Hi, my name is [Robert](https://steemit.com/introduceyourself/@smcaterpillar/hello-world-hello-steemit-community-i-m-not-a-big-fan-of-new-year-s-resolutions-but-this-time-i-do-have-one) and I do Machine Learning for a living, sometimes I even do it in my spare time. If so, I usually like to do rather silly things with Artificial Intelligence.

In the video below I want to show you what happens if we teach language to an Artificial Intelligence (AI), but use slightly weird examples to do so. What can an AI learn from comments made by users or readers of online news sources? If you ever tried to follow the discussions in the comment sections of news outlets, you do understand why this dataset is slightly weird. Hardcore idealists meet smartasses meet blunt trolls.

I scraped comments from 3 German news publishers: [ZEIT](http://www.zeit.de/index), [Spiegel Online](http://www.spiegel.de/), and [Focus](https://www.focus.de/). If you wanted to order these along a political spectrum, I would identify ZEIT and Spiegel as rather left-wing and Focus as a right-wing news outlet. However, we do not want to teach the AI with news articles directly, but show it comments made by the users instead. You can imagine that the political spectrum of these comments touches more extreme ends than the news articles.

### The AI Experiment Setup

I scraped about 400,000 comments from the news sites and fed them into a special kind of Artificial Neural Network, called [Doc2Vec](https://radimrehurek.com/gensim/models/doc2vec.html). This Machine Learning technique infers meaning of words from the context they are used in. Moreover, the method allows you to do arithmetic with words and their semantic meanings, such as in the title of this post. What happens if you add `Hitler` + `Putin`? Well, according to the knowledge extracted from the online comments, you get `Erdogan`. Does this make sense? :-D

 Finally, I wanted to know, if the AI can learn which types of comments are more common on which news outlet. Or to phrase that differently, give me a user comment, can my Machine Learning model tell you on which news site this was posted? To find the answer to this question (extreme ends of the spectrum will be touched!), and to discover some more weird relations among different words, I invite you to watch my talk I gave at the PyData conference in the video below. For those of you who want to skip the mathy, theoretical background and just want to see the results, [click here you lazy...](https://www.youtube.com/watch?v=zFScws0mb7M&feature=youtu.be&t=16m0s)

### The PyData Talk

https://www.youtube.com/watch?v=zFScws0mb7M


### Some Source Code

 I hope you liked my little experiment. You can find a Jupyter Notebook with some code on my [Github profile](https://github.com/SmokinCaterpillar/doc2vec_user_comments). Unfortunately, I cannot provide the raw user comment data to you because I do not a have the publishers' permission (I emailed them some time ago, but they never responded).

 If you have any questions, feel free to post and I'll try to answer them. Upvotes and resteems are, of course, also very welcomed. By the way, **I am currently testing if the insights I gained and the methods I used can be applied to help the steemit community with article curation**. So stay tuned and watch out for my steemit proposal coming soon...