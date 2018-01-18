Remember Itchy and Scratchy money?

<a href="http://www.youtube.com/watch?feature=player_embedded&v=dErRj6V8_xQ
" target="_blank"><img src="http://img.youtube.com/vi/dErRj6V8_xQ/0.jpg"
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

With the recent major crash of Ethereum and other Cryptocurrencies let's at least enjoy ourselves and build our own Cryptocurrency token. Let us create something like regular ETH, but fun. To avoid copyright infringement we just going to call it *I. & S. Ether* (not for Itchy and Scratchy, but innovative and shiny, or something along these lines). **This post is a tutorial on how to setup your own Cryptcurrency on top of Ethereum.**

## How to build your own ERC20 Token

Let us build this nice *I. & S. Ether* token with the Solidity programming language. We will go for the most simple design possible.

We have to agree on a few parameters at first. We will allow an exchange rate of 0.001 ETH for 1 of our tokens. So by the time of writing (and not another crash in the meantime), Homer would have bought 1000 *I. & S. Ether* for eleven hundred Dollars. However, we are less obnoxious and mean as Itchy and Scratchy Land. Although probably no one is going to accept poor *I. & S. Ether* either, we do allow the exchange of our token back into regular *ETH* without any loss or premium (except Gas costs, of course, but this is out of our control). So buying our token has no associated risk because you can easily redeem the initial *ETH* investment.

Moreover, usually poeple like scarcity (remember the 21 million Bitcoin?), so let us make our token scarce, too. There will only be 42,000 *I. & S. Ether*, no more and no less!

We need a new Ethereum Smart Contract that manages the our new shiny *I. & S. ETH* for us. This contract needs to follow a particular desing pattern and interface called [ERC20 standard](https://theethereum.wiki/w/index.php/ERC20_Token_Standard). If we obey this standard, other software can make use of the token such as the [MetaMask wallet](https://metamask.io/) or we could even trade it on an exchange like [EtherDelta](https://etherdelta.com/).

So what does this standard demand from us?

* `name`: The name of our token, i.e. *I. & S. Ether*.

* `symbol`: The ticker symbol for our token, let us choose *ISE*.

* `decimals`: The number of decimals of our token supports. This is where it already gets a bit tricky. From now on we need to calculate everything in the smallest unit of our token. If we pick 9 decimals (for comparison Bitcoin has 8 and Ethereum 18) and we want to have 42,000 tokens overall, we will in fact have 42,000,000,000,000. The first 9 zeros from the right are our decimal places.

* `totalSupply()`: This function needs to return how many of our tokens exist. So for *ISE* this will give 42,000,000,000,000. Remeber, this is in fact 42,000 because we support 9 decimals.

* `balanceOf(tokenOwner)`: This function returns the balance of each and every individual token owner. So this is usually 0 unless you purchased some tokens from our contract.

* `transfer(to, amount)`: This function can be called to transfer tokens to other people. You do not have a birthday gift for your partner, yet? How about some *I. & S. Ether*? It's fun!

* Moreover, there are some slightly more advanced functions like `allowance`, `approve`, and `transferFrom` which we need to implement such that our token can be handled by exchanges. These methods will allow the exchanges to send our tokens on our behalf in case a trade is executed.

I will spare you the impementational details of these functions. In fact, you can simply copy and paste them from [this ERC20 standard](https://theethereum.wiki/w/index.php/ERC20_Token_Standard). Moreover, the entire source code of this token is also available [on my Github profile](https://github.com/SmokinCaterpillar/IaS_Money).

### The I. & S. Smart Contract

Let us focus on the more interesting customized part of our token. Let us start with some new constants that we introduce. These are the `unit`, which is simply 10^`decimals`, and the `price`, i.e. the exchange rate from *ETH* to our token:

 ```
 // unit = 10**decimals
 uint256 public constant unit = 1000000000;

 // The ETH to ISE exchange rate
 uint256 public constant price = 1 finney / unit;
```
Note, `finney` is a convenient Solidity constant meaning 0.001 *ETH*, i.e. 1000 `finney` are 1 *ETH*. Hence, 1 *ISE* token costs 0.001 *ETH*. Still with me? Good!

 Next, let us take a look at the initialization of our *ISE* token. In the constructor we simply create 42,000 tokens out of thin air. Yeah, just like that, no mining, no annoying proof-of-work, it's magic! The holder of these new tokens is the *ISE* smart contract itself (`this`):

```
function IaSEther() public{
    // very scarce 42k coins:
    maxSupply = 42000 * unit;
    balances[this] = maxSupply;
}
```

#### Buy some of our fun I. & S. Ether

As aforementioned, we want to be able to flawlessly exchange regular *ETH* for our fun *I. & S. Ether* and back. To `buy` tokens from our contract, we implement the following function:
```
function buy() public payable{
    // compute the number of tokens to send back
    uint256 amount = msg.value / price;
    // ship the tokens to the buyer
    require(executeTransfer(this, msg.sender, amount));
}
```
Of course, the number of tokens someone `buy`s is simple the *ETH* sent (`msg.value`) devided by our constant `price`. The trade is implemented as a normal token transfer from the contract to the buyer. Accordingly, the `executeTransfer` is just performing the token exchange according to the ERC20 standard:
```
// Internal function to execute transfer
function executeTransfer(address _from, address _to, uint256 _amount) internal returns (bool){
    if (balances[_from] >= _amount && _amount > 0
            && balances[_to] + _amount > balances[_to]) {
        balances[_from] -= _amount;
        balances[_to] += _amount;
        Transfer(_from, _to, _amount);
        return true;
    } else {
        return false;
    }
}
```
This `executeTransfer` function simply tests that the sender `from_` has an appropriate balance, checks for overflows, and then updates the balances via `balances[_from] -= _amount` (take tokens from sender) and `balances[_to] += _amount` (add tokens to receiver).

Moreover, people should not be required to use the `buy` function to get our tokens. It should be sufficient to just send *ETH* to our contract to get fun *ISE* in return. The function to receive *ETH* is called the *fallback function*. However, in terms of Solidity code, the function does not have a name and has just to call the `buy` method from before:
```
function () public payable{
    buy();
}
```

#### Sell our fun I. & S. Ether

Next, we want to allow people to exchange their tokens back to *ETH* for the same price. Therefore, we need to subclass the `transfer` function like so:
```
function transfer(address _to, uint256 _amount) public returns (bool){
    // first recevie tokens by the seller
    bool success = super.transfer(_to, _amount);
    // send the ETH back to the seller
    if ((_to == address(this)) && success){
        uint256 value = _amount * price;
        msg.sender.transfer(value);
    }
    return success;

}
```
Basically, this executes a normal transfer. However, if the receiver of tokens is our smart contract itself (`this`), people receive stored *ETH* in return (`msg.sender.transfer(value)`).
The original `transfer` in the parent class is straightforward:
```
// Transfer the _amount from msg.sender to _to account
function transfer(address _to, uint256 _amount) public returns (bool) {
    return executeTransfer(msg.sender, _to, _amount);
}
```


#### Deploy and Interact with the Contract

Finally, we just need to deploy the contract to the Blockchain. I just did that and deployed the contract to the Ropsten testnet using the [Remix Solidity environment](https://remix.ethereum.org/). You can find the contract at [0x4e99cb0340cd0a3cb30de4d14e624d42dc673d18](https://ropsten.etherscan.io/address/0x4e99cb0340cd0a3cb30de4d14e624d42dc673d18). If you want to send some test Ether to the contract, you can claim some from [this faucet for free](http://faucet.ropsten.be:3001/).

As a reminder, you can find the entire source code [in my Github profile](https://github.com/SmokinCaterpillar/IaS_Money).

That's about it. So have fun with your new *ISE* token (or your own copy-and-pasted custom token) and happy HODLing!