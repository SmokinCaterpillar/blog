![prop](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/2018_04_09_steemit_improvement_proposal/title.jpg)

### tl;dr Summary
 
Besides the existing voting power decrease, halve an additional new voting power for revoting on the same authors again and again, and let the new revoting power recover very, very slowly. Details below.

### Steemit's Strengths and Weaknesses

I am a big fan of Steemit, the Steem blockchain, and the Steem tokens. To my mind, it is probably the only Cryptocurrency that is really backed by something, namely the entire Steemit community. Many users put there heart and soul into their posts. For example, I am a fond reader of many #steemstem publications and amazed how much time and effort authors spend on well-researched science and technology contributions.

Yet, without doubt Steemit has its dark sides as well and does not run without friction. There are some issues that come to my mind such as:

1. **Bid and voting bot abuse**: Some users promote quite dubious content using bid bots. As a consequence, whether the trending page is nowadays a useful feature is intensely debated.

2. **Reward pool abuse**: Some whales are just using their voting power in upvoting circles and self-promotion rather than helping to discover good content.

3. **Frustrating first steps**: Being a minnow can be very, very frustrating at times. Just putting days of work in a well-researched article may give a few pennies without a proper follower base.

### Proof-of-brain, Bid Bots, and Circular Voting Patterns

I still believe that the Steemit [proof-of-brain](https://steem.io/steem-bluepaper.pdf) concept -- i.e. the hypothesis that rewarding user contributions and user curation with tokens will facilitate content of social value -- is or can become a reality again. For my part, I started an initiative or rather developed a project called @trufflepig. A curation bot that searches and promotes undervalued content (free of charge, the little fella is not a bid bot). Besides digging for Steemit posts that deserve more reward, he publishes a daily top-list about how the trending page would look like without bid bots. 

These top-lists have started a discussion if bid bots are in fact useful. The argument goes as follows: Bid bots democratize the hot and trending sections as they enable everyone (with the right amount of pocket money, of course) to get their shiny posts up there. Thereby they fight the circular upvote rings that regularly appeared at the top before the advent of the bid bots.

This is a valuable argument and made me think about how I could improve @trufflepig's no-bid-bot-top-list without promoting the circular upvote patterns. Instead of improving @trufflepig directly, I had an idea about how to improve Steemit's voting algorithm in general. To my mind a small adjustment of the voting rules may tackle all three of the above listed problems to some extent.

# The Proposal

For simplicity users voting are called *curators* and the users receiving these votes are called *authors* in the following.
Besides the existing voting power that decreases slowly with each vote and recovers quickly by 20% each day, a curator is assigned an individual voting power per author. Let us call this special voting power **revoting power**. The revoting power is halved after each vote casted by the curator on the very same author. Moreover, the re-voting power recovers much more slowly and re-doubles only every *n* days. For now let us assume *n=28*, i.e. 4 weeks, but the exact time span needs to be discussed in more detail.

Effectively we have now three means of weighting a vote (instead of the current 2):

1. **Voting Weight**: Can be chosen manually by the curators; effectively chosen only by established curators with at least 500 Steem Power who can use the Steemit voting weight slider (yet, in principle everyone could via the Steem API).

2. **Voting Power**: Drops by 2% for each full vote and recovers by 20% in 24 hours.

3. **New Revoting Power**: Author specific voting power that halves with every vote on the same author. Recovers slowly by doubling every 28 days up to a maximum of 100%.

The total strength of a curator vote is the product of the three weightings: `voting weight * voting power * revoting power`.

For example, author @alice publishes a post that curator @charlie likes. He upvotes it with 100% weight at 100% voting power and 100% revoting power, giving @alice effectively a full 100% strength upvote (`100% * 100 % * 100% = 100%`), the highest he can do. As a consequence, his voting power decreases to 98% (the current system). In addition, his revoting power on @alice is halved to 50% (the new adjustment).

If curator @charlie voted again on another article by author @alice with 100% voting weight, he would grant her a much smaller total vote strength, namely 49% (`voting weight * voting power * revoting power = 100% * 98% * 50% = 49%`). As a consequence, his voting power would further decrease to 96% and his revoting power halves to 25%. His voting power would recover in about five hours. To recover his revoting power on @alice, @charlie needs to wait 58 days to have it recharged back at 100%.

The **most important part** is that **revoting power** is **author specific**. For instance, if curator @charlie decides to vote on author @bob's new article after his two votes on @alice. He would grant @bob a much stronger vote with a total strength of 96% (`voting weight * voting power * revoting power = 100% * 96% * 100%`).

Details are to be debated. For instance, the lowering of revoting power could be stopped at 6.25% (4th halving) such that hardcore fans of a particular author can support her or him no matter what, but at the expense of sacrificing a lot of influence. Also the doubling time to recharge could be variable such as 28 days to recover from 50 to 100%, but 7 days for any smaller recovery.

### Implications of the new Revoting Power

What are the consequences of this new revoting power?

1. **Circular upvote rings are punished**: Whales upvoting each other has almost no effect since their reciprocal voting strengths quickly halve with each circular upvote and recover too slowly to abuse the reward pool.

2. **Self votes become less useful**: Revoting power also applies to self votes. Hence, authors may only vote on their own posts effectively once a month.

3. **Bid bots lose influence**: Authors may only use a particular bid bot every month, since each bought upvote halves the bid bot's boost on any of the author's posts. Thereby, the overall usage of bid bots will be reduced.

4. **More rewards for minnows**: Content is much more rewarded than authors, because most curators will not vote for the same author several times in a row since the revoting power drops quickly. Hence, content and curation rewards are distributed more broadly among the Steemit community and will facilitate quality instead of quantity. 

As you can see, the proposed novel revoting power may solve or at least tackle some of the most pressing issues this platform faces. This will perpetuate the *proof of brain* concept and increase the value of Steem for everyone. If Steemit becomes renowned as the go to platform for quality content, everyone invested in it will benefit.

Still, my proposal will not solve all of the issues.

## Limitations of the new Revoting Power

Some problems or challenges will remain:

1. Costly and time consuming voting rings may still be possible by whales distributing their voting power among many accounts.

2. Revoting Power will not hinder vote selling. In fact, it may benefit services such as @smartsteem or @minnowbooster because votes of individual users are becoming more worth in the Steemit ecosystem.

The first issue may actually not be a severe problem.  First, clearly abusive voting rings (these will be many, many accounts with almost no posts or comments) are easy to spot and can be flagged by curation bots. This flagging can be supported by decreasing the revoting power of flagging (reflagging from now on) much less severe than the positive revoting power. For example, the revoting power halves every upvote on the same author whereas the reflagging power may decrease by only one third on each downvote on the same author. Besides, new accounts do not come free of charge and pose an additional investment hurdle or risk for scammers.


What do you think about this proposal? Do you have any feedback or other ideas? If this proposal gathers some support, I will open a Github issue on the [steem repository](https://github.com/steemit/steem/issues) to see if and how this could be potentially implemented in the long run.


PS: Yeah I'm aware of the blunt irony of promoting this post with a bid bot, but what can I do? :-D