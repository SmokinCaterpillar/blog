Without doubt, the problem of scalability is currently Bitcoins most pressing issue. Roughly every 10 minutes a new block with a maximum size of 1 MB is added to Bitcoin's blockchain. This block size has severe consequences for the amount of transactions that can be processed by the Bitcoin network. On average the network can route 3 to 7 transactions per second. These numbers can stand absolutely no comparison with the [VISA capacities of several thousand transaction per second](https://en.bitcoin.it/wiki/Scalability). Consequently, the Bitcoin network suffers from constant congestion and processing fees have reached levels of 50 $ and higher. Clearly, these fees hinder Bitcoin from becoming a "A Peer-to-Peer Electronic Cash System" as envisioned by its anonymous inventor Satoshi Nakamoto in the [original whitepaper](https://bitcoin.org/bitcoin.pdf).

Attempts were made to tackle the congestion problem last year. For example, in August the **Segregated Witness** (SegWit) soft fork was activated. This fork removes the unlocking signature, i.e. *witness* data, from a transactio. In turn, transactions become smaller and, thus, more of them fit into a single block. Moreover, SegWit enables the implementation of the *Lightning Network*, the most important addition to BTC coming in 2018.

![thunder](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/bitcoin2018/lightning.jpg)

## Lightning Payment Channels

The *Lightning Network* promises to solve the aforementioned scalability issues by moving most of Bitcoin transactions off chain. This means users can exchange Bitcoin without constantly interacting with the blockchain. This will hopefully allow to scale to thousands of transactions per second. The new network is based on so called *payment channels*. In a nutshell, payment channels work as follows. Let us assume Alice and Bob (who else?) want to exchange BTC through such a so called payment channel.

![channel](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/2017_01_22_lightning/channel.jpg)

* First, both, Alice and Bob, need to deposit a collateral, for example 1 BTC, via a so called "opening transaction" to the payment channel. The channel itself is a multi-signature transaction controlled by both parites. This happens "on chain", i.e. this first deposit needs to be processed by the Bitcoin miners.

* All following transactions, however, can be executed "off chain". For instance, Alice wants to pay 0.5 BTC to Bob. So they create a new "commitment transaction" invalidating the original "opening transaction" and now attributing 1.5 BTC to Bob and the remaining 0.5 BTC to Alice. To emphasize this again, this transaction does not need to be processed by the blockchain. Only Alice and Bob store a private copy of the transaction.

* Alice and Bob could keep on sending BTC between each other until all eternity ore one of them spends all of her or his coins. Every time they just need to update the previous "commitment transaction" with a newer one.

* Still, either Alice or Bob could close the payment channel at any time. They simply need to publish the latest "commitment transaction" to the miners. They will include it into the blockchain and funds are distributed to Alice and Bob accordingly. However, there is a minor catch. Whoever closes the transaction has to *wait 3 days* before she or he can access the funds.

* Older commitment transactions are invalidated by so called revocation keys. Let's say that Alice does not want to play by the rules, but publishes an older "commitment transaction" that attributes more money to her than she really owns. In this case Bob has to show the revocation key within the 3 day waiting period to the miners proving that Alice transaction is invalid. As a punishment Alice would lose all her funds to Bob.

Always having the risk of losing all funds at the back of one's mind will prevent both parties of a payment channel from cheating.

Still, what if Bob does not realize Alice cheats on him because he is offline? This is where Segregated Witness comes into play. To encourage others to help with the revocation of the evil transaction, we set a small portion of the collateral as a bounty that anyone can spend. Hence, everyone can watch for invalidated commitment transactions being published. When it happens, anyone can sign the bounty to themselves and broadcast the transaction's revocation.

You think these payment channels are a genius idea? Wait for the second, network part of *Lightning*.

## The Lightning Network

So far we only created bi-directional payment channels. Now let us get to the real network. Let us assume Alice has established a payment channel with Bob. Moreover, Bob has another channel with Charlie and he is connected with Daria. If Alice wants to send BTC to Daria, she does not need to do this "on chain". Instead she could simply use Bob and Charlie to route her payment to Daria. Hence, if enough people are interconnected, the majority of transactions can happen "off chain".

The actual steps look like the following, assuming Alice wants to pay Daria 0.1 BTC:

![network](https://raw.githubusercontent.com/SmokinCaterpillar/blog/master/2017_01_22_lightning/network.jpg)

* Alice needs to find a route to Daria. She discovers that she can hop over Bob and Charlie.

* Daria creates a random number `R`, but keeps it secret. Instead she sends a hash of `R`, i.e. `H(R)` to Alice.

* Alice creates now a **Hash Time-Locked Contract** (HTLC) with Bob. She signs a transaction saying that Bob is entitled to 0.1 BTC if he figures out `R` (with hash value `H(R)`) within 3 days.

* Bob will do the same with Charlie and, in turn, Charlie with Daria.

* Daria, of course, knows `R` because she generated it in the first place. Consequently, she can settle the payment with Charlie.

* Daria now tells `R` to Bob and Charlie. Thus, they can settle their open bills of 0.1 BTC with Bob and Alice, respectively. In conclusion, Alice has transferred 0.1 BTC indirectly to Daria via Bob and Charlie.

What happens in case Daria is uncooperative and does not give `R` to Bob and Charlie? Well, she cannot avoid this.  If she wanted to publish and redeem the transaction from Charlie to her *on chain*, she has to reveal `R` for the transaction to be mined, viz. Bob and Charlie get to know `R` anyway.

And the best part is, the *Lighnting Network* is not coming in the distant future. Instead, it is (almost) here. You can already buy a [VPN connection](https://news.bitcoin.com/vpn-provider-now-accepts-lightning-network-payments/) with *Lightning* or [top up your phone](https://www.coindesk.com/payment-provider-bitrefill-runs-successful-lightning-transaction-test/). Moreover, you can even try Lightning yourself in action, on a testnet though, at [HTLC.me](https://htlc.me/).

However, all *Lightning* implementations are still in a testing phase and undergo development. Moreover, some open questions remain: Will the *Lightning Network* lead to a more centralized Bitcoin system? Will there be major payment hubs routing everyone's payments? The *Lightning Network* would than be in the hands of a few. If being banned or censored by the hubs, one would have to turn back to the bare-bone Bitcoin network and bypass *Lightning* with "on chain" transactions.

Will *Lightning* be established in time? The network cannot just be turned *on* like a light switch. It needs to grow and it will take time until the technology is established. Maybe all these endeavors come to late and other currencies will overtake Bitcoin, like [RaiBlocks](https://raiblocks.net/) having no fees utilizing a block lattice instead of a chain. Indeed, 2018 will be decisive for Bitcoin and show if *Lightning* can turn the tables.
