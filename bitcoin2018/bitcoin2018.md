
2017 was definitely the year of Cryptocurrencies. The overall market capitalization of Bitcoin (BTC) and co. rose from 15 billion $ in January to over [600 billion $](https://coinmarketcap.com/charts/) at the end of last year. Bitcoin's price alone did skyrocket from about 900 to more than 14,000 $ almost reaching the watermark of 20,000 in the meantime. Undoubtedly, Cryptocurrencies are at the dawn of mass adoption with exchanges like Coinbase adding more than [100,000 new users per hour](https://www.cnbc.com/2017/11/03/coinbase-adds-100000-users-after-cme-announces-bitcoin-futures-plans.html).

![King Bitcoin](https://raw.githubusercontent.com/SmokinCaterpillar/steemit_data/master/blockfolio/btc.jpg "Mom, please send Bitcoin to 13ehCxCGk29kMuNYTgLfZZkWm4CmCiBB49")

However, the success, especially the one of king Bitcoin, has to be taken with a grain of salt. At the beginning of last year BTC had a staggering market share of more than 80% of all digital currencies. Over the course of 2017 this share shrunk to less than 40% due to the success of alternatives like Ethereum or Ripple (although to my mind Ripple is not a real Cryptocurrency, but this is a different story).

Accordingly, the question that is hanging like the Sword of Damocles over Bitcoin is if the mother of all Cryptocurrencies can keep its lead and remain the number one Cryptocurrency of the world. Indeed, 2018 is going to be a decisive year for Bitcoin. In particular, BTC faces three major problems. These three problems will define the currencies fate this year.

For the TL;DR guys among you the three issues are:

* Scalability (With the *Lightning Network* solution at the door)
* Energy Consumption (Win 30 Tesla cars)
* Governance (Free hard forks for everyone!)

For those who want know some more details, please, feel free to go on:

# 1. Scalability

The most pressing issue Bitcoin is facing is, without doubt, the problem of scalability. Roughly every 10 minutes a new block with a maximum size of 1 MB is added to Bitcoin's blockchain. This block size has severe consequences for the amount of transactions that can be processed by the Bitcoin network. On average the network can route 3 to 7 transactions per second. These numbers can stand absolutely no comparison with the [VISA capacities of several thousand transaction per second](https://en.bitcoin.it/wiki/Scalability). Consequently, the Bitcoin network suffers from constant congestion and processing fees have reached levels of 50 $ and higher. Clearly, these fees hinder Bitcoin from becoming a "A Peer-to-Peer Electronic Cash System" as envisioned by its anonymous inventor Satoshi Nakamoto in the [original whitepaper](https://bitcoin.org/bitcoin.pdf).

Attempts were made to tackle the congestion problem last year. For example, in August the **Segregated Witness** (SegWit) soft fork was activated. This fork removes the unlocking signature, i.e. *witness* data, from a transaction. In turn, transactions become smaller and, thus, more of them fit into a single block. Moreover, SegWit enables the implementation of the *Lightning Network*, the most important addition to BTC coming in 2018. We will get to this shortly.

In fact, SegWit was only the first part of the so called [New York agreement](https://en.wikipedia.org/wiki/SegWit2x). As a next step the block size was supposed to be doubled in late 2017, this was called SegWit2x. This would have bought some time to solve the Bitcoin scaling problem. Unfortunately, the 2x hard fork was [called off the very last minute](https://lists.linuxfoundation.org/pipermail/bitcoin-segwit2x/2017-November/000685.html) due to strong opposition by the core developer team.

Will Bitcoin's small block size lead to the slow death of the currency and the rise of faster competitors like Bitcoin Cash? Bitcoin Cash (BCH) is a fork of Bitcoin with an eight times larger block size. Hence, BCH is not suffering from exorbitant fees, yet. However, this so-called "on chain" scaling is by no means a long-term solution to the problem at hand. Imagine a block size of 200 MB to achieve VISA scale throughput. The blockchain would grow out of proportion by more than a Gigabyte per hour. This would kick many nodes out of the network because they cannot keep up with the massive chain size. Bitcoin's security would be at risk with a centralized network of only a handful of full node participants.

Is this the end of Bitcoin? Or at least the end of BTC as digital cash? Should BTC be treated rather as a store of value, as digital gold? Fortunately, it looks like that the answer is **No**. There is a silver lining for BTC at the horizon called the *Lightning Network*.

## The Lightning Network

![thunder](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/bitcoin2018/lightning.jpg)

The *Lightning Network* promises to solve the aforementioned scalability issues by moving most of Bitcoin transactions off chain. This means users can exchange Bitcoin without constantly interacting with the blockchain. This will hopefully allow to scale to thousands of transactions per second. The new network is based on so called *payment channels*. In a nutshell, payment channels work as follows. Let us assume Alice and Bob (who else?) want to exchange BTC through such a so called payment channel.

* First, both, Alice and Bob, need to deposit a collateral, for example 1 BTC, via a so called "opening transaction" to the payment channel. This happens "on chain", i.e. this first deposit needs to be processed by the Bitcoin miners.

* All following transactions, however, can be executed "off chain". For instance, Alice wants to pay 0.5 BTC to Bob. So they create a new "commitment transaction" invalidating the original "opening transaction" and now attributing 1.5 BTC to Bob and the remaining 0.5 BTC to Alice. To emphasize this again, this transaction does not need to be processed by the blockchain. Only Alice and Bob store a private copy of the transaction.

* Alice and Bob could keep on sending BTC between each other until all eternity ore one of them spends all of her or his coins. Every time they just need to update the previous "commitment transaction" with a newer one.

* Still, either Alice or Bob could close the payment channel at any time. They simply need to publish the latest "commitment transaction" to the miners. They will include it into the blockchain and funds are distributed to Alice and Bob accordingly.

* Older commitment transactions are invalidated by so called revocation keys. Let's say that Alice does not want to play by the rules, but publishes an older "commitment transaction" that attributes more money to her than she really owns. In this case Bob shows the revocation key to the the miners proving that Alice transaction is invalid. As a punishment Alice would lose all her funds to Bob.

Always having the risk of losing all funds at the back of one's mind will prevent both parties of a payment channel from cheating. You think this is a genius idea? Wait for the second part of *Lightning*.

So far we only created bi-directional payment channels. Now let us get to the real network. Let us assume Alice has established a payment channel with Bob. Moreover, Bob has another channel with Charlie. If Alice wants to send BTC to Charlie, she does not need to do this "on chain". Instead she could simply use Bob to route her payment to Charlie. Hence, if enough people are interconnected, the majority of transactions can happen "off chain".

Fortunately, the *Lighnting Network* is not coming in the distant future. Instead, it is (almost) here. You can already buy a [VPN connection](https://news.bitcoin.com/vpn-provider-now-accepts-lightning-network-payments/) with *Lightning* or [top up your phone](https://www.coindesk.com/payment-provider-bitrefill-runs-successful-lightning-transaction-test/).

However, all *Lightning* implementations are still in a testing phase and undergo development. Moreover, some open questions remain: Will the *Lightning Network* lead to a more centralized Bitcoin system? Will there be major payment hubs routing everyone's payments? The *Lightning Network* would than be in the hands of a few. If being banned or censored by the hubs, one would have to turn back to the bare-bone Bitcoin network and bypass *Lightning* with "on chain" transactions.

Will *Lightning* be established in time? The network cannot just be turned *on* like a light switch. It needs to grow and it will take time until the technology is established. Maybe all these endeavors come to late and other currencies will overtake Bitcoin, like [RaiBlocks](https://raiblocks.net/) having no fees utilizing a block lattice instead of a chain. Indeed, 2018 will be decisive for Bitcoin and show if *Lightning* can turn the tables.

In case the *Lightning Network* proves itself worthy to solve scalability, Bitcoin will definetly get another major boost. On the one hand, Bitcoin will become a usable low fee peer2peer cash system again. Most likely, more merchants will start to accept BTC as a consequence. On the other hand, lots of BTC will be used and locked up in routing payment channels. Thus, the market supply of Bitcoin will shrink and prices will surge.

![surge](https://cdn-images-1.medium.com/max/1600/1*5DiZNrCZZyEoxU0lxFYGlQ.gif)

The resulting price increase leads us directly to the second most pressing issue of Bitcoin: Its energy consumption.

# 2. Energy Consumption

Bitcoin does not have a reputation as being environment friendly. The mining of Bitcoin relying on the proof-of-work scheme is very wasteful in terms of energy consumption. Bitcoin's hunger for electricity has been put somewhere in between surpassing [all Tesla cars](http://fortune.com/2018/01/11/bitcoin-mining-tesla-electricity/) by a factor of thirty or all the power needed by a small country [like Ireland](https://www.theguardian.com/technology/2017/nov/27/bitcoin-mining-consumes-electricity-ireland).

By the time of writing, the Bitcoin network calculates more than 16 million tera hashes per second. However, pinning down the exact electricity costs is difficult because miners are not very fond of revealing the details of their business. Still, it is fair to assume that BTC consumes a **shitload of energy** and it is only getting worse. The more valuable Bitcoin becomes, the more people will start mining. Of course, Bitcoin mining farms are operated in locations with cheap electricity. Usually, cheap energy does not mean renewable energy.

![nuclear](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/bitcoin2018/nuclear.jpg)

How can Bitcoin's environmental footprint be improved? Unfortunately, there is no real solution at hand. Maybe mining with renewable energy sources like solar power or [water power](https://www.hydrominer.org/) could help to some (small?) degree.

No doubt, if Bitcoin's energy hunger gets worse in 2018, the Cryptocurrency will face a lot of backlash. In fact, there are environment friendly alternatives to mining like proof-of-stake. Ethereum will switch from proof-of-work to [proof-of-stake in 2018](https://blockonomi.com/ethereum-casper/). Moreover, [PIVX](https://pivx.org/) is an already established proof-of-stake Bitcoin relative.

Even if it turns out that proof-of-stake is the future of Cryptocurrencies, it is extremely unlikely that Bitcoin would adopt such a scheme. The Bitcoin core implementation has proven to be incredible inflexbible regarding hard forks. This leads us to the final problem: Governance.

# 3. Governance

Maybe Bitcoin's two strongest assets, trust and stability, can turn into its biggest weaknesses. Indeed Bitcoin has been in operation since 2009 and it just worked without major hiccups. Do you know how rare this is in the world of software? There is a reason why people value Bitcoin so highly besides transaction fees in the double digits and more advanced Cryptocurrencies being born on a daily basis.

However, this stability also has its dark side. The core developers resistance to the aforementioned New York agreement is the root cause of the skyrocketing fees and current scalability issues. Maybe this decision turns out to be right. Maybe the advent of *Lightning* is sufficient and the stubbornness to stick to 1 MB block sizes ensures a more decentralized network.

![core](https://steemit-production-imageproxy-upload.s3.amazonaws.com/DQmYZ9MNiCbpHzVQkZYsdg2DQKt6Stin67SPk1m157np2fk)

Still, this shows that it has become incredibly difficult to update the Bitcoin network with a hard fork. To my mind a solution to the previously discussed energy crisis will most likely require a hard fork. Core developer resistance could lead to another currency split and we end up with a new coin alongside the original Bitcoin still consuming too much energy.

Yet, the decisions made by the core developer team so far, and of course, their work and lifeblood they already put into Bitcoin, turned out to be very beneficial to the Cryptocurrency world. Do not get me wrong, I am very thankful for all they have done (I would love to contribute to BTC, but my C++ skills are probably too limited for anything meaningful :-D). I just feel some light anguish that the fate of a decentralized and censorship free system can be influenced so strongly by a group of very few people.

Nonetheless, I am very excited what 2018 will bring for Bitcoin and I am looking forward to see *Lightning* in action! So happy HODLing!