# bitcoincharts-ohlcv
[bitcoincharts](https://bitcoincharts.com)にあるcsvの生データをohlcvに変換します．

# Usage
`scripts/`に移動して`python3 main.py inputfile outputfile frequency`

# Output File Format
| DATE | OPEN | HIGH | LOW | CLOSE | VOLUME |

# Contribution
仮想通貨のチャート足が欲しいシチュエーションはしばしば存在する．  
[BlockChain](https://www.blockchain.com/)や[quandl](https://www.quandl.com/)を使えば，日足の取得は可能である．  
一方で，分足を長期間にわたって取得する手段はそれほど存在しない．  
[cryptowatch](https://cryptowat.ch/)の[API](http://nipper.work/btc/index.php?market=bitFlyer&coin=BTCJPY)を使うことで分足は得られるが，長期間のデータは存在しない．  
[coinapi](https://www.coinapi.io/)を用いることで長期間の分足を得ることも可能であるが，Free Planで大規模なデータを取得してくるのは現実的ではない．  

[bitcoincharts](https://bitcoincharts.com)は過去の取引履歴が取得できるため，分足を再現することが可能である．
**bitcoincharts-ohlcv**は任意の時間足のohlcvデータを生成する．

