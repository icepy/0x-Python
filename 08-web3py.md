请把 web3py 当 SDK 来使用，不要被它复杂的概念所迷惑，虽然它依赖与以太坊节点的连接才能与其交互。

[https://web3py.readthedocs.io/en/stable/quickstart.html#](https://web3py.readthedocs.io/en/stable/quickstart.html#)


我推荐使用下面两个 RPC 服务。

[https://app.infura.io/](https://app.infura.io/)
[https://www.alchemy.com/](https://www.alchemy.com/)

大部分场景，我们都使用 HTTP

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/xxx'))
```

我将不需要私钥即可与以太坊节点交互，获得一些数据的 API 都归类于此-读取，我们比较常用的，如查询地址的余额，查询最后一个 block 信息等等

```python
w3.eth.get_block('latest')
w3.eth.get_balance('0x...')
```

我将需要私钥与以太坊节点交互的 API 都归类于此-写入，比如发送 ETH

```python
pk = os.environ.get('PRIVATE_KEY')
acct2 = w3.eth.account.from_key(pk)
w3.eth.send_transaction({
  "from": '0x...',
  "value": w3.to_wei(3, 'ether'),
  "to": acct2.address
})
```

交互合约不分读写，因为都有可能，首先我们需要知道合约地址 和 ABI

```python
address = '0x...'
abi = '[{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"minter_","type":"address"},'
contract_instance = w3.eth.contract(address, abi)

contract_instance.functions.storedValue().call()
tx_hash = contract_instance.functions.updateValue(43).transact()
```

不要担心，ABI 就是一段描述，描述方法名，参数名，参数类型。