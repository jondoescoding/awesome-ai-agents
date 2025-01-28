Directory structure:
└── man-c-pycoingecko/
    ├── README.md
    ├── CHANGELOG.md
    ├── LICENCE
    ├── setup.py
    ├── pycoingecko/
    │   ├── __init__.py
    │   ├── api.py
    │   ├── utils.py
    │   └── version.py
    └── tests/
        └── test_api.py

================================================
File: README.md
================================================
# CoinGecko API wrapper
[![PyPi Version](https://img.shields.io/pypi/v/pycoingecko.svg)](https://pypi.python.org/pypi/pycoingecko/)
![GitHub](https://img.shields.io/github/license/man-c/pycoingecko)

Python3 wrapper around the [CoinGecko](https://www.coingecko.com/) API (V3) 🦎<br> Supports both Public and Pro API:
 * [Public API v3.0.1](https://docs.coingecko.com/v3.0.1/reference/introduction)
 * [Pro API v3.1.1](https://docs.coingecko.com/v3.1.1/reference/introduction)

### Installation
PyPI
```bash
pip install -U pycoingecko
```
or from source
```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

### Usage

For free **Public API**:

 * without any demo api key (x-cg-demo-api-key):
    ```python
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()
    ```
 * 🔑 with a <ins>demo api key</ins>:
    ```python
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI(demo_api_key='YOUR_DEMO_API_KEY')
    ```

For **Pro API**:
 * 🔑 with a <ins>pro api key</ins>:
    ```python
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI(api_key='YOUR_PRO_API_KEY')
    ```

### Examples
The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.\
**Any optional parameters** can be passed using same names, as defined in CoinGecko API doc (https://www.coingecko.com/en/api/documentation).

For any parameter:
- ***Lists** are supported as input for multiple-valued comma-separated parameters\
  (e.g. see /simple/price usage examples).*
- ***Booleans** are supported as input for boolean type parameters; they can be `str` ('true', 'false'') or `bool` (`True`, `False`)\
  (e.g. see /simple/price usage examples).*

Usage examples:
```python
# /simple/price endpoint with the required parameters
>>> cg.get_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 3462.04}}

>>> cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
# OR (lists can be used for multiple-valued arguments)
>>> cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies='usd')
{'bitcoin': {'usd': 3461.27}, 'ethereum': {'usd': 106.92}, 'litecoin': {'usd': 32.72}}

>>> cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd,eur')
# OR (lists can be used for multiple-valued arguments)
>>> cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies=['usd', 'eur'])
{'bitcoin': {'usd': 3459.39, 'eur': 3019.33}, 'ethereum': {'usd': 106.91, 'eur': 93.31}, 'litecoin': {'usd': 32.72, 'eur': 28.56}}

# optional parameters can be passed as defined in the API doc (https://www.coingecko.com/api/docs/v3)
>>> cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
{'bitcoin': {'usd': 3458.74, 'usd_market_cap': 60574330199.29028, 'usd_24h_vol': 4182664683.6247883, 'usd_24h_change': 1.2295378479069035, 'last_updated_at': 1549071865}}
# OR (also booleans can be used for boolean type arguments)
>>> cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
{'bitcoin': {'usd': 3458.74, 'usd_market_cap': 60574330199.29028, 'usd_24h_vol': 4182664683.6247883, 'usd_24h_change': 1.2295378479069035, 'last_updated_at': 1549071865}}
```

### API documentation
https://www.coingecko.com/en/api/documentation

### 📡 Endpoints included
> :warning: **Endpoints documentation**: To make sure that you are using properly each endpoint you should check the [API documentation](https://www.coingecko.com/en/api/documentation). Return behaviour and parameters of the endpoints, such as *pagination*, might have changed. <br> Any **optional parameters** defined in CoinGecko API doc can be passed as function parameters using same parameters names with the API *(see Examples above)*.
<details><summary>ping</summary>
<p>

* **/ping** 
  
   _Check API server status_
  ```python
  cg.ping()
  ```
</details>

<details><summary>key</summary>
<p>

* [Pro API] 💼 **/key**  
  
   _Monitor your account's API usage, including rate limits, monthly total credits, remaining credits, and more_
  ```python
  cg.key()
  ```
</details>

<details><summary>simple</summary>
<p>

* **/simple/price** 
  
   _Get the current price of any cryptocurrencies in any other supported currencies that you need_
  ```python
  cg.get_price()
  ```
* **/simple/token_price/{id}** 
  
   _Get current price of tokens (using contract addresses) for a given platform in any other currency that you need_
  ```python
  cg.get_token_price()
  ```
* **/simple/supported_vs_currencies** 
  
   _Get list of supported_vs_currencies_
  ```python
  cg.get_supported_vs_currencies()
  ```
</details>

<details><summary>coins</summary>
<p>

* **/coins/list** 
  
   _List all supported coins id, name and symbol (no pagination required)_
  ```python
  cg.get_coins_list()
  ```

* [Pro API] 💼 **/coins/top_gainers_losers**  
  
   _Query the top 30 coins with largest price gain and loss by a specific time duration_
  ```python
  cg.get_coin_top_gainers_losers()
  ```

* [Pro API] 💼 **/coins/list/new**  
  
   _Query the latest 200 coins that recently listed on CoinGecko_
  ```python
  cg.get_coins_list_new()
  ```

* **/coins/markets**  
  
   _List all supported coins price, market cap, volume, and market related data_
  ```python 
  cg.get_coins_markets()
  ```
* **/coins/{id}**  
  
   _Get current data (name, price, market, ... including exchange tickers) for a coin_
  ```python 
  cg.get_coin_by_id()
  ```
* **/coins/{id}/tickers**  
  
   _Get coin tickers (paginated to 100 items)_
  ```python 
  cg.get_coin_ticker_by_id()
  ```
* **/coins/{id}/history**  
  
   _Get historical data (name, price, market, stats) at a given date for a coin_
  ```python 
  cg.get_coin_history_by_id()
  ```
* **/coins/{id}/market_chart**  
  
   _Get historical market data include price, market cap, and 24h volume (granularity auto)_
  ```python 
  cg.get_coin_market_chart_by_id()
  ```
* **/coins/{id}/market_chart/range**  
  
   _Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)_
  ```python 
  cg.get_coin_market_chart_range_by_id()
  ```

[//]: # (* **/coins/{id}/status_updates** &#40;Get status updates for a given coin &#40;beta&#41;&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_coin_status_updates_by_id&#40;&#41;)

[//]: # (  ```)
* **/coins/{id}/ohlc**  
  
   _Get the OHLC chart (Open, High, Low, Close) of a coin based on particular coin id_
  ```python
  cg.get_coin_ohlc_by_id()
  ```

* [Pro API] 💼 **/coins/{id}/ohlc/range**  
  
   _Get the OHLC chart (Open, High, Low, Close) of a coin within a range of timestamp based on particular coin id_
  ```python
  cg.get_coin_ohlc_by_id_range()
  ```

* [Pro API] 👑 **/coins/{id}/circulating_supply_chart**  
  
   _Query historical circulating supply of a coin by number of days away from now based on provided coin id_
  ```python
  cg.get_coin_circulating_supply_chart()
  ```

* [Pro API] 👑 **/coins/{id}/circulating_supply_chart/range**  
  
   _Query historical circulating supply of a coin, within a range of timestamp based on the provided coin id_
  ```python
  cg.get_coin_circulating_supply_chart_range()
  ```

* [Pro API] 👑 **/coins/{id}/total_supply_chart**  
  
   _Query historical total supply of a coin by number of days away from now based on provided coin id_
  ```python
  cg.get_coin_total_supply_chart()
  ```

* [Pro API] 👑 **/coins/{id}/total_supply_chart/range**  
  
   _Query historical total supply of a coin, within a range of timestamp based on the provided coin id_
  ```python
  cg.get_coin_total_supply_chart_range()
  ```

</details>


<details><summary>contract</summary>
<p>

* **/coins/{id}/contract/{contract_address}**  
  
   _Get coin info from contract address_
  ```python
  cg.get_coin_info_from_contract_address_by_id()
  ```
* **/coins/{id}/contract/{contract_address}/market_chart/**  
  
   _Get historical market data include price, market cap, and 24h volume (granularity auto) from a contract address_
  ```python
  cg.get_coin_market_chart_from_contract_address_by_id()
  ```
* **/coins/{id}/contract/{contract_address}/market_chart/range**  
  
   _Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto) from a contract address_
  ```python
  cg.get_coin_market_chart_range_from_contract_address_by_id()
  ```
</details>

<details><summary>asset_platforms</summary>
<p>

* **/asset_platforms**  
  
   _List all asset platforms (Blockchain networks)_
  ```python
  cg.get_asset_platforms()
  ```

* [Pro API] 👑 **/token_lists/{asset_platform_id}/all.json**  
  
   _Get full list of tokens of a blockchain network (asset platform) that is supported by Ethereum token list standard_
  ```python
  cg.get_asset_platform_by_id()
  ```

</details>

<details><summary>categories</summary>
<p>

* **/coins/categories/list**  
  
   _List all categories_
  ```python
  cg.get_coins_categories_list()
  ```
* **coins/categories**  
  
   _List all categories with market data_
  ```python
  cg.get_coins_categories()
  ```
</details>

<details><summary>exchanges</summary>
<p>

* **/exchanges**  
  
   _List all exchanges_
  ```python
  cg.get_exchanges_list()
  ```
* **/exchanges/list**  
  
   _List all supported markets id and name (no pagination required)_
  ```python
  cg.get_exchanges_id_name_list()
  ```
* **/exchanges/{id}**  
  
   _Get exchange volume in BTC and top 100 tickers only_
  ```python
  cg.get_exchanges_by_id()
  ```
* **/exchanges/{id}/tickers**  
  
   _Get exchange tickers (paginated, 100 tickers per page)_
  ```python
  cg.get_exchanges_tickers_by_id()
  ```

[//]: # (* **/exchanges/{id}/status_updates** &#40;Get status updates for a given exchange &#40;beta&#41;&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_exchanges_status_updates_by_id&#40;&#41;)

[//]: # (  ```)
* **/exchanges/{id}/volume_chart**  
  
   _Get volume_chart data for a given exchange_
  ```python
  cg.get_exchanges_volume_chart_by_id()
  ```

* [Pro API] 💼 **/exchanges/{id}/volume_chart/range**  
  
   _Query the historical volume chart data in BTC by specifying date range in UNIX based on exchange’s id_
  ```python
  cg.get_exchanges_volume_chart_by_id_within_time_range()
  ```  

</details>

[//]: # (<details><summary>finance</summary>)

[//]: # (<p>)

[//]: # ()
[//]: # (* **/finance_platforms** &#40;List all finance platforms&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_finance_platforms&#40;&#41;)

[//]: # (  ```)

[//]: # (* **/finance_products** &#40;List all finance products&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_finance_products&#40;&#41;)

[//]: # (  ```)

[//]: # (</details>)

<details><summary>indexes</summary>
<p>

* **/indexes**  
  
   _List all market indexes_
```python
cg.get_indexes()
```
* **/indexes/{market_id}/{id}**  
  
   _Get market index by market id and index id_
```python
cg.get_indexes_by_market_id_and_index_id()
```
* **/indexes/list**  
  
   _List market indexes id and name_
```python
cg.get_indexes_list()
```
</details>

<details><summary>derivatives</summary>
<p>

* **/derivatives**  
  
   _List all derivative tickers_
  ```python
  cg.get_derivatives()
  ```
* **/derivatives/exchanges**  
  
   _List all derivative exchanges_
  ```python
  cg.get_derivatives_exchanges()
  ```
* **/derivatives/exchanges/{id}** 
  
   _Show derivative exchange data_
  ```python
  cg.get_derivatives_exchanges_by_id()
  ```
* **/derivatives/exchanges/list** 
  
   _List all derivative exchanges name and identifier_
  ```python
  cg.get_derivatives_exchanges_list()
  ```
</details>

<details><summary>nfts (beta)</summary>
<p>

* **/nfts/list** 
  
   _List all supported NFT ids, paginated by 100 items per page, paginated to 100 items_
  ```python
  cg.get_nfts_list()
  ```
* **/nfts/{id}** 
  
   _Get current data (name, price_floor, volume_24h ...) for an NFT collection. native_currency (string) is only a representative of the currency_
  ```python
  cg.get_nfts_by_id()
  ```
* **/nfts/{asset_platform_id}/contract/{contract_address}** 
  
   _Get current data (name, price_floor, volume_24h ...) for an NFT collection. native_currency (string) is only a representative of the currency_
  ```python
  cg.get_nfts_collection_by_asset_platform_id_and_contract_address()
  ```

* [Pro API] 💼 **/nfts/markets** 
  
   _Query all the supported NFT collections with floor price, market cap, volume and market related data on CoinGecko_
  ```python
  cg.get_nfts_markets()
  ```

* [Pro API] 💼 **/nfts/{id}/market_chart** 
  
   _Query historical market data of a NFT collection, including floor price, market cap, and 24h volume, by number of days away from now_
  ```python
  cg.get_nfts_market_chart_by_id()
  ```

* [Pro API] 💼 **/nfts/{asset_platform_id}/contract/{contract_address}/market_chart** 
  
   _Query historical market data of a NFT collection, including floor price, market cap, and 24h volume, by number of days away from now based on the provided contract address_
  ```python
  cg.get_ntfs_market_chart_by_asset_platform_id_and_contract_address()
  ```

* [Pro API] 💼 **/nfts/{id}/tickers** 
  
   _Query the latest floor price and 24h volume of a NFT collection, on each NFT marketplace, e.g. OpenSea and LooksRare_
  ```python
  cg.get_nfts_tickers_by_id()
  ```

</details>

[//]: # (<details><summary>status_updates</summary>)

[//]: # (<p>)

[//]: # ()
[//]: # (* **/status_updates** &#40;List all status_updates with data &#40;description, category, created_at, user, user_title and pin&#41;&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_status_updates&#40;&#41;)

[//]: # (  ```)

[//]: # (</details>)

[//]: # (<details><summary>events</summary>)

[//]: # (<p>)

[//]: # ()
[//]: # (* **/events** &#40;Get events, paginated by 100&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_events&#40;&#41;)

[//]: # (  ```)

[//]: # (* **/events/countries** &#40;Get list of event countries&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_events_countries&#40;&#41;)

[//]: # (  ```)

[//]: # (* **/events/types** &#40;Get list of events types&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_events_types&#40;&#41;)

[//]: # (  ```)

[//]: # (</details>)

<details><summary>exchange_rates</summary>
<p>

* **/exchange_rates** 
  
   _Get BTC-to-Currency exchange rates_
  ```python
  cg.get_exchange_rates()
  ```
</details>

<details><summary>search</summary>
<p>

* **/search** 
  
   _Search for coins, categories and markets on CoinGecko_
  ```python
  cg.search()
  ```
</details>

<details><summary>trending</summary>
<p>

* **/search/trending** 
  
   _Get trending search coins (Top-7) on CoinGecko in the last 24 hours_
  ```python
  cg.get_search_trending()
  ```
</details>

<details><summary>global</summary>
<p>

* **/global** 
  
   _Get cryptocurrency global data_
    ```python
    cg.get_global()
    ```
* **/global/decentralized_finance_defi** 
  
   _Get cryptocurrency global decentralized finance(defi) data_
    ```python
    cg.get_global_decentralized_finance_defi()
    ```

* [Pro API] 💼 **/global/market_cap_chart**

  _Query historical global market cap and volume data by number of days away from now)_
  ```python
  cg.get_global_market_cap_chart()
  ```

</details>

<details><summary>companies (beta)</summary>
<p>

* **/companies/public_treasury/{coin_id}** 
  
   _Query public companies’ bitcoin or ethereum holdings_
    ```python
    cg.get_companies_public_treasury_by_coin_id()
    ```
</details>

### Test

#### Installation
Install required packages for testing using:
```bash
pip install pytest responses
```

#### Usage

Run unit tests with:

```
# after installing pytest and responses using pip3
pytest tests
```

## License
[MIT](https://choosealicense.com/licenses/mit/)


================================================
File: CHANGELOG.md
================================================

3.2.0 / 2024-11-13
==================

  * support both public (with or without demo_api_key) and pro (with pro api key) api in requests
  * added new methods in coins, asset_platforms, exchanges, nfts, global

3.1.0 / 2022-10-26
==================

  * added nfts (beta) endpoints (/nfts/list, /nfts/{id}, /nfts/{asset_platform_id}/contract/{contract_address})
  * updated tests

3.0.0 / 2022-09-01
==================

  * removed deprecated endpoints (status_updates, finance and events):
  * /coins/{id}/status_updates -> cg.get_coin_status_updates_by_id()
  * /exchanges/{id}/status_updates -> cg.get_exchanges_status_updates_by_id()
  * /finance_platforms -> cg.get_finance_platforms()
  * /finance_products -> cg.get_finance_products()
  * /status_updates -> cg.get_status_updates()
  * /events -> cg.get_events()
  * /events/countries -> cg.get_events_countries()
  * /events/types -> cg.get_events_types()
  * removed deprecated api_base_url param from CoinGeckoAPI init

2.3.0 / 2022-08-30
==================

  * added /search endpoint
  * added CoinGecko Pro API support using api_key param in CoinGeckoAPI init (required in PRO version API calls)
  * added ability to modify how many retries to do in requests session using param retries in CoinGeckoAPI init (default: retries=5)
  * fixed session to mount retry adapter on https instead of http
  * fixed params passed in get_coin_market_chart_range_from_contract_address_by_id for /coins/{id}/contract/{contract_address}/market_chart/range endpoint

2.2.0 / 2021-06-17
==================

  * added /indexes/{market_id}/{id} and /companies/public_treasury/{coin_id} endpoints

2.1.0 / 2021-06-03
==================

  * added asset_platforms (/asset_platforms) and categories (/coins/categories/list, coins/categories) endpoints

2.0.0 / 2021-04-23
==================

  * allow Python Lists and Booleans for any endpoint parameter (list converted to comma-separated string & bool converted to lower case string)
  * removed /indexes/{id} endpoint (Get market index by id) -> cg.get_indexes_by_id()
  * improved request exceptions handling (Fixed unbound local exception on GET request failure)

1.4.1 / 2021-03-30
==================

  * fixed __api_url_params issue for optional parametes of few endpoints (such as /coins/{id}/market_chart)

1.4.0 / 2020-10-03
==================

  * added new endpoints (/coins/{id}/ohlc, /search/trending, /global/decentralized_finance_defi)
  * updated tests

1.3.0 / 2020-07-12
==================

  * allow optional arguments for **ALL** endopoints

1.2.0 / 2019-12-13
==================

  * added indexes endpoints (/indexes, /indexes/{id}, /indexes/list)

1.1.0 / 2019-12-06
==================

  * added derivatives endpoints (/derivatives, /derivatives/exchanges, /derivatives/exchanges/{id}, /derivatives/exchanges/list)

1.0.0 / 2019-11-17
==================

  * updated tests
  * included more contract endpoints
  * included /coins/{id}/market_chart/range endpoint
  * basic methods for finance endpoints with tests
  * updated error handling
  * added check for json format in __request; coingecko returns a html string when something goes wrong in the request, which results in an error when json.loads is called on the html string.

0.4.0 / 2019-08-20
==================

  * included /exchanges/{id}/volume_chart endpoint

0.3.0 / 2019-05-31
==================

  * exceptions include API error message
  * fix get_coin_market_chart_by_id test
  * Use a list or tuple for multiple-valued arguments
  * convert every list arg to comma-separated string

0.2.0 / 2019-05-17
==================

  * Fixed arguments for get_token_price
  * Added get_token_price function

0.1.6 / 2019-02-02
==================

  * README incude examples
  * included /exchanges/list endpoint

0.1.0 / 2019-01-02
==================

  * added /coins/{id}/tickers endpoint
  * included events endpoints
  * included status_updates endpoints
  * updated exchanges endpoints
  * updated coins endpoints
  * included simple endpoints

0.0.2 / 2018-11-20
==================

  * use requests session to include retries
  * fixed bug when querying exchanges and added more unit tests
  * first unit tests for coingecko wrappers
  * initial commit


================================================
File: LICENCE
================================================
MIT License

Copyright (c) 2018 Christoforou Emmanouil

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



================================================
File: setup.py
================================================
# from distutils.core import setup
import setuptools

version = {}
exec(open('./pycoingecko/version.py').read(), version)
# print(version['__version__'])

setuptools.setup(
    name='pycoingecko',
    version=version['__version__'],
    packages=['pycoingecko', ],
    license='MIT',
    description='Python wrapper around the CoinGecko API',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Christoforou Manolis',
    author_email='emchristoforou@gmail.com',
    install_requires=['requests'],
    url='https://github.com/man-c/pycoingecko',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


================================================
File: pycoingecko/__init__.py
================================================
from .api import CoinGeckoAPI
from .version import __version__


================================================
File: pycoingecko/api.py
================================================
import json
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .utils import func_args_preprocessing


class CoinGeckoAPI:
    __API_URL_BASE = 'https://api.coingecko.com/api/v3/'
    __PRO_API_URL_BASE = 'https://pro-api.coingecko.com/api/v3/'

    def __init__(self, api_key: str = '', retries=5, demo_api_key: str = ''):

        self.extra_params = None
        # self.headers = None
        if api_key:
            self.api_base_url = self.__PRO_API_URL_BASE
            self.extra_params = {'x_cg_pro_api_key': api_key}
            # self.headers = {"accept": "application/json",
            #                 "x-cg-pro-api-key": api_key}
        else:
            self.api_base_url = self.__API_URL_BASE
            if demo_api_key:
                self.extra_params = {'x_cg_demo_api_key': demo_api_key}
                # self.headers = {"accept": "application/json",
                #                 "x-cg-demo-api-key": demo_api_key}

        self.request_timeout = 120

        self.session = requests.Session()
        retries = Retry(total=retries, backoff_factor=0.5, status_forcelist=[502, 503, 504])
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

        # self.session.headers = self.headers

    def __request(self, url, params):
        # if using pro or demo version of CoinGecko with api key, inject key in every call
        if self.extra_params is not None:
            params.update(self.extra_params)

        try:
            response = self.session.get(url, params=params, timeout=self.request_timeout)
        except requests.exceptions.RequestException:
            raise

        try:
            response.raise_for_status()
            # self._headers = response.headers
            content = json.loads(response.content.decode('utf-8'))
            return content
        except Exception as e:
            # check if json (with error message) is returned
            try:
                content = json.loads(response.content.decode('utf-8'))
                raise ValueError(content)
            # if no json
            except json.decoder.JSONDecodeError:
                pass

            raise

    # def __api_url_params(self, api_url, params, api_url_has_params=False):
    #     # if using pro version of CoinGecko, inject key in every call
    #     if self.api_key:
    #         params['x_cg_pro_api_key'] = self.api_key
    #
    #     if params:
    #         # if api_url contains already params and there is already a '?' avoid
    #         # adding second '?' (api_url += '&' if '?' in api_url else '?'); causes
    #         # issues with request parametes (usually for endpoints with required
    #         # arguments passed as parameters)
    #         api_url += '&' if api_url_has_params else '?'
    #         for key, value in params.items():
    #             if type(value) == bool:
    #                 value = str(value).lower()
    #
    #             api_url += "{0}={1}&".format(key, value)
    #         api_url = api_url[:-1]
    #     return api_url

    # ---------- PING ----------#
    def ping(self, **kwargs):
        """Check API server status"""

        api_url = '{0}ping'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- KEY ----------#
    def key(self, **kwargs):
        """Monitor your account's API usage, including rate limits, monthly total credits, remaining credits, and more"""

        api_url = '{0}key'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- SIMPLE ----------#
    @func_args_preprocessing
    def get_price(self, ids, vs_currencies, **kwargs):
        """Get the current price of any cryptocurrencies in any other supported currencies that you need"""

        ids = ids.replace(' ', '')
        kwargs['ids'] = ids
        vs_currencies = vs_currencies.replace(' ', '')
        kwargs['vs_currencies'] = vs_currencies

        api_url = '{0}simple/price'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_token_price(self, id, contract_addresses, vs_currencies, **kwargs):
        """Get the current price of any tokens on this coin (ETH only at this stage as per api docs) in any other supported currencies that you need"""

        contract_addresses = contract_addresses.replace(' ', '')
        kwargs['contract_addresses'] = contract_addresses
        vs_currencies = vs_currencies.replace(' ', '')
        kwargs['vs_currencies'] = vs_currencies

        api_url = '{0}simple/token_price/{1}'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)
        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_supported_vs_currencies(self, **kwargs):
        """Get list of supported_vs_currencies"""

        api_url = '{0}simple/supported_vs_currencies'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- COINS ----------#
    @func_args_preprocessing
    def get_coins(self, **kwargs):
        """List all coins with data (name, price, market, developer, community, etc)"""

        api_url = '{0}coins'.format(self.api_base_url)
        # ['order', 'per_page', 'page', 'localization']
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_top_gainers_losers(self, vs_currency, **kwargs):
        """Get top gainers and losers"""

        kwargs['vs_currency'] = vs_currency

        api_url = '{0}coins/top_gainers_losers'.format(self.api_base_url)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coins_list_new(self, **kwargs):
        """This endpoint allows you to query the latest 200 coins that recently listed on CoinGecko"""

        api_url = '{0}coins/list/new'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coins_list(self, **kwargs):
        """List all supported coins id, name and symbol (no pagination required)"""

        api_url = '{0}coins/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coins_markets(self, vs_currency, **kwargs):
        """List all supported coins price, market cap, volume, and market related data"""

        kwargs['vs_currency'] = vs_currency

        api_url = '{0}coins/markets'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_by_id(self, id, **kwargs):
        """Get current data (name, price, market, ... including exchange tickers) for a coin"""

        api_url = '{0}coins/{1}/'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_ticker_by_id(self, id, **kwargs):
        """Get coin tickers (paginated to 100 items)"""

        api_url = '{0}coins/{1}/tickers'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_history_by_id(self, id, date, **kwargs):
        """Get historical data (name, price, market, stats) at a given date for a coin"""

        kwargs['date'] = date

        api_url = '{0}coins/{1}/history'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_market_chart_by_id(self, id, vs_currency, days, **kwargs):
        """Get historical market data include price, market cap, and 24h volume (granularity auto)"""

        # api_url = '{0}coins/{1}/market_chart?vs_currency={2}&days={3}'.format(self.api_base_url, id, vs_currency, days)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}coins/{1}/market_chart'.format(self.api_base_url, id, vs_currency, days)
        kwargs['vs_currency'] = vs_currency
        kwargs['days'] = days

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_market_chart_range_by_id(self, id, vs_currency, from_timestamp, to_timestamp, **kwargs):
        """Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)"""

        # api_url = '{0}coins/{1}/market_chart/range?vs_currency={2}&from={3}&to={4}'.format(self.api_base_url, id,
        #                                                                                    vs_currency, from_timestamp,
        #                                                                                    to_timestamp)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}coins/{1}/market_chart/range'.format(self.api_base_url, id)
        kwargs['vs_currency'] = vs_currency
        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp

        return self.__request(api_url, kwargs)

    # @func_args_preprocessing
    # def get_coin_status_updates_by_id(self, id, **kwargs):
    #     """Get status updates for a given coin"""
    #
    #     api_url = '{0}coins/{1}/status_updates'.format(self.api_base_url, id)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)

    @func_args_preprocessing
    def get_coin_ohlc_by_id(self, id, vs_currency, days, **kwargs):
        """Get coin's OHLC"""

        # api_url = '{0}coins/{1}/ohlc?vs_currency={2}&days={3}'.format(self.api_base_url, id, vs_currency, days)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}coins/{1}/ohlc'.format(self.api_base_url, id)
        kwargs['vs_currency'] = vs_currency
        kwargs['days'] = days

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_ohlc_by_id_range(self, id, vs_currency, from_timestamp, to_timestamp, interval, **kwargs):
        """Get coin's OHLC within a range of timestamp"""

        kwargs['vs_currency'] = vs_currency
        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp
        kwargs['interval'] = interval

        api_url = '{0}coins/{1}/ohlc/range'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_circulating_supply_chart(self, id, days, **kwargs):
        """Get coin's circulating supply chart"""

        kwargs['days'] = days

        api_url = '{0}coins/{1}/circulating_supply_chart'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_circulating_supply_chart_range(self, id, from_timestamp, to_timestamp, **kwargs):
        """Get coin's circulating supply chart within a range of timestamp"""

        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp

        api_url = '{0}coins/{1}/circulating_supply_chart/range'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_total_supply_chart(self, id, days, **kwargs):
        """Get coin's total supply chart"""

        kwargs['days'] = days

        api_url = '{0}coins/{1}/total_supply_chart'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_total_supply_chart_range(self, id, from_timestamp, to_timestamp, **kwargs):
        """Get coin's total supply chart within a range of timestamp"""

        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp

        api_url = '{0}coins/{1}/total_supply_chart/range'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- Contract ----------#
    @func_args_preprocessing
    def get_coin_info_from_contract_address_by_id(self, id, contract_address, **kwargs):
        """Get coin info from contract address"""

        api_url = '{0}coins/{1}/contract/{2}'.format(self.api_base_url, id, contract_address)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_market_chart_from_contract_address_by_id(self, id, contract_address, vs_currency, days, **kwargs):
        """Get historical market data include price, market cap, and 24h volume (granularity auto) from a contract address"""

        # api_url = '{0}coins/{1}/contract/{2}/market_chart/?vs_currency={3}&days={4}'.format(self.api_base_url, id,
        #                                                                                     contract_address,
        #                                                                                     vs_currency, days)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}coins/{1}/contract/{2}/market_chart'.format(self.api_base_url, id, contract_address)
        kwargs['vs_currency'] = vs_currency
        kwargs['days'] = days

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_market_chart_range_from_contract_address_by_id(self, id, contract_address, vs_currency, from_timestamp,
                                                                to_timestamp, **kwargs):
        """Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto) from a contract address"""

        # api_url = '{0}coins/{1}/contract/{2}/market_chart/range?vs_currency={3}&from={4}&to={5}'.format(
        #     self.api_base_url, id, contract_address, vs_currency, from_timestamp, to_timestamp)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}coins/{1}/contract/{2}/market_chart/range'.format(self.api_base_url, id, contract_address)
        kwargs['vs_currency'] = vs_currency
        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp

        return self.__request(api_url, kwargs)

    # ---------- ASSET PLATFORMS ----------#
    @func_args_preprocessing
    def get_asset_platforms(self, **kwargs):
        """List all asset platforms (Blockchain networks)"""

        api_url = '{0}asset_platforms'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_asset_platform_by_id(self, asset_platform_id, **kwargs):
        """ List all asset platforms (Blockchain networks) by platform id """

        api_url = '{0}token_lists/{1}/all.json'.format(self.api_base_url, asset_platform_id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- CATEGORIES ----------#
    @func_args_preprocessing
    def get_coins_categories_list(self, **kwargs):
        """List all categories"""

        api_url = '{0}coins/categories/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coins_categories(self, **kwargs):
        """List all categories with market data"""

        api_url = '{0}coins/categories'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- EXCHANGES ----------#
    @func_args_preprocessing
    def get_exchanges_list(self, **kwargs):
        """List all exchanges"""

        api_url = '{0}exchanges'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_exchanges_id_name_list(self, **kwargs):
        """List all supported markets id and name (no pagination required)"""

        api_url = '{0}exchanges/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_exchanges_by_id(self, id, **kwargs):
        """Get exchange volume in BTC and tickers"""

        api_url = '{0}exchanges/{1}'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_exchanges_tickers_by_id(self, id, **kwargs):
        """Get exchange tickers (paginated, 100 tickers per page)"""

        api_url = '{0}exchanges/{1}/tickers'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # @func_args_preprocessing
    # def get_exchanges_status_updates_by_id(self, id, **kwargs):
    #     """Get status updates for a given exchange"""
    #
    #     api_url = '{0}exchanges/{1}/status_updates'.format(self.api_base_url, id)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)

    @func_args_preprocessing
    def get_exchanges_volume_chart_by_id(self, id, days, **kwargs):
        """Get volume chart data for a given exchange"""

        kwargs['days'] = days

        api_url = '{0}exchanges/{1}/volume_chart'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_exchanges_volume_chart_by_id_within_time_range(self, id, from_timestamp, to_timestamp, **kwargs):
        """Get volume chart data for a given exchange within a time range"""

        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp

        api_url = '{0}exchanges/{1}/volume_chart/range'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # # ---------- FINANCE ----------#
    # @func_args_preprocessing
    # def get_finance_platforms(self, **kwargs):
    #     """Get cryptocurrency finance platforms data"""
    #
    #     api_url = '{0}finance_platforms'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)
    #
    # @func_args_preprocessing
    # def get_finance_products(self, **kwargs):
    #     """Get cryptocurrency finance products data"""
    #
    #     api_url = '{0}finance_products'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)

    # ---------- INDEXES ----------#
    @func_args_preprocessing
    def get_indexes(self, **kwargs):
        """List all market indexes"""

        api_url = '{0}indexes'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # @func_args_preprocessing
    # def get_indexes_by_id(self, id, **kwargs):
    #    """Get market index by id"""
    #
    #    api_url = '{0}indexes/{1}'.format(self.api_base_url, id)
    #    api_url = self.__api_url_params(api_url, kwargs)
    #
    #    return self.__request(api_url)

    @func_args_preprocessing
    def get_indexes_by_market_id_and_index_id(self, market_id, id, **kwargs):
        """Get market index by market id and index id"""

        api_url = '{0}indexes/{1}/{2}'.format(self.api_base_url, market_id, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_indexes_list(self, **kwargs):
        """List market indexes id and name"""

        api_url = '{0}indexes/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- DERIVATIVES ----------#
    @func_args_preprocessing
    def get_derivatives(self, **kwargs):
        """List all derivative tickers"""

        api_url = '{0}derivatives'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_derivatives_exchanges(self, **kwargs):
        """List all derivative tickers"""

        api_url = '{0}derivatives/exchanges'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_derivatives_exchanges_by_id(self, id, **kwargs):
        """List all derivative tickers"""

        api_url = '{0}derivatives/exchanges/{1}'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_derivatives_exchanges_list(self, **kwargs):
        """List all derivative tickers"""

        api_url = '{0}derivatives/exchanges/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- NFTS (BETA) ----------#
    @func_args_preprocessing
    def get_nfts_list(self, **kwargs):
        """List all supported NFT ids, paginated by 100 items per page, paginated to 100 items"""

        api_url = '{0}nfts/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_nfts_by_id(self, id, **kwargs):
        """Get current data (name, price_floor, volume_24h ...) for an NFT collection. native_currency (string) is only a representative of the currency"""

        api_url = '{0}nfts/{1}'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_nfts_by_asset_platform_id_and_contract_address(self, asset_platform_id, contract_address, **kwargs):
        """Get current data (name, price_floor, volume_24h ...) for an NFT collection. native_currency (string) is only a representative of the currency"""

        api_url = '{0}nfts/{1}/contract/{2}'.format(self.api_base_url, asset_platform_id, contract_address)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_nfts_markets(self, **kwargs):
        """This endpoint allows you to query all the supported NFT collections with floor price, market cap, volume and market related data on CoinGecko"""

        api_url = '{0}nfts/markets'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_nfts_market_chart_by_id(self, id, days, **kwargs):
        """This endpoint allows you query historical market data of a NFT collection, including floor price, market cap, and 24h volume, by number of days away from now"""

        kwargs['days'] = days

        api_url = '{0}nfts/{1}/market_chart'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_ntfs_market_chart_by_asset_platform_id_and_contract_address(self, asset_platform_id, contract_address, days, **kwargs):
        """This endpoint allows you query historical market data of a NFT collection, including floor price, market cap, and 24h volume, by number of days away from now based on the provided contract address"""

        kwargs['days'] = days

        api_url = '{0}nfts/{1}/contract/{2}/market_chart'.format(self.api_base_url, asset_platform_id, contract_address)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_nfts_tickers_by_id(self, id, **kwargs):
        """This endpoint allows you to query the latest floor price and 24h volume of a NFT collection, on each NFT marketplace, e.g. OpenSea and LooksRare"""

        api_url = '{0}nfts/{1}/tickers'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # # ---------- STATUS UPDATES ----------#
    # @func_args_preprocessing
    # def get_status_updates(self, **kwargs):
    #     """List all status_updates with data (description, category, created_at, user, user_title and pin)"""
    #
    #     api_url = '{0}status_updates'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)

    # # ---------- EVENTS ----------#
    # @func_args_preprocessing
    # def get_events(self, **kwargs):
    #     """Get events, paginated by 100"""
    #
    #     api_url = '{0}events'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)
    #
    # @func_args_preprocessing
    # def get_events_countries(self, **kwargs):
    #     """Get list of event countries"""
    #
    #     api_url = '{0}events/countries'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)
    #
    # @func_args_preprocessing
    # def get_events_types(self, **kwargs):
    #     """Get list of event types"""
    #
    #     api_url = '{0}events/types'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)

    # ---------- EXCHANGE-RATES ----------#
    @func_args_preprocessing
    def get_exchange_rates(self, **kwargs):
        """Get BTC-to-Currency exchange rates"""

        api_url = '{0}exchange_rates'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- SEARCH ----------#
    @func_args_preprocessing
    def search(self, query, **kwargs):
        """Search for coins, categories and markets on CoinGecko"""

        # api_url = '{0}search?query={1}'.format(self.api_base_url, query)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}search'.format(self.api_base_url)
        kwargs['query'] = query

        return self.__request(api_url, kwargs)

    # ---------- TRENDING ----------#
    @func_args_preprocessing
    def get_search_trending(self, **kwargs):
        """Get top 7 trending coin searches"""

        api_url = '{0}search/trending'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- GLOBAL ----------#
    @func_args_preprocessing
    def get_global(self, **kwargs):
        """Get cryptocurrency global data"""

        api_url = '{0}global'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)['data']

    @func_args_preprocessing
    def get_global_decentralized_finance_defi(self, **kwargs):
        """Get cryptocurrency global decentralized finance(defi) data"""

        api_url = '{0}global/decentralized_finance_defi'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)['data']

    @func_args_preprocessing
    def get_global_market_cap_chart(self, days, **kwargs):
        """Get cryptocurrency global market cap chart data"""

        kwargs['days'] = days

        api_url = '{0}global/market_cap_chart'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- COMPANIES ----------#
    @func_args_preprocessing
    def get_companies_public_treasury_by_coin_id(self, coin_id, **kwargs):
        """Get public companies data"""

        api_url = '{0}companies/public_treasury/{1}'.format(self.api_base_url, coin_id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)


================================================
File: pycoingecko/utils.py
================================================
from functools import wraps


def func_args_preprocessing(func):
    """Return function that converts list input arguments to comma-separated strings"""

    @wraps(func)
    def input_args(*args, **kwargs):

        # check in **kwargs for lists and booleans
        for v in kwargs:
            kwargs[v] = arg_preprocessing(kwargs[v])
        # check in *args for lists and booleans
        args = [arg_preprocessing(v) for v in args]

        return func(*args, **kwargs)

    return input_args


def arg_preprocessing(arg_v):
    """Return the values of an argument after preprocessing"""

    # check if arg is list and convert it to comma-separated string
    if isinstance(arg_v, list):
        arg_v = ','.join(arg_v)
    # check if arg is boolean and convert it to string
    elif isinstance(arg_v, bool):
        arg_v = str(arg_v).lower()

    return arg_v


def get_comma_separated_values(values):
    """Return the values as a comma-separated string"""

    # Make sure values is a list or tuple
    if not isinstance(values, list) and not isinstance(values, tuple):
        values = [values]

    return ','.join(values)



================================================
File: pycoingecko/version.py
================================================
__version__ = '3.2.0'

================================================
File: tests/test_api.py
================================================
import pytest
import requests.exceptions
import responses
import unittest
import unittest.mock as mock

from pycoingecko import CoinGeckoAPI
from requests.exceptions import HTTPError


class TestWrapper(unittest.TestCase):

    @responses.activate
    def test_connection_error(self):
        with pytest.raises(requests.exceptions.ConnectionError):
            CoinGeckoAPI().ping()

    @responses.activate
    def test_failed_ping(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/ping',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().ping()

    @responses.activate
    def test_ping(self):
        # Arrange
        ping_json = { 'gecko_says':'(V3) To the Moon!' }
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/ping',
                          json = ping_json, status = 200)

        # Act
        response = CoinGeckoAPI().ping()

        ## Assert
        assert response == ping_json


    #---------- SIMPLE ----------#

    #---------- /simple/price ----------#
    @responses.activate
    def test_get_price(self):
        # Arrange
        coins_json_sample = {"bitcoin": {"usd": 7984.89}}

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_price('bitcoin', 'usd')

        ## Assert
        assert response == coins_json_sample

    @responses.activate
    def test_failed_get_price(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_price('bitcoin', 'usd')

    #---------- /simple/token_price/{id} ----------#
    @responses.activate
    def test_get_token_price(self):
        # Arrange
        coins_json_sample = {'0xB8c77482e45F1F44dE1745F52C74426C631bDD52': {'bnb': 1.0, 'bnb_market_cap': 144443301.0, 'bnb_24h_vol': 17983938.686249834, 'last_updated_at': 1558704332}}

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/token_price/ethereum?include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true&contract_addresses=0xB8c77482e45F1F44dE1745F52C74426C631bDD52&vs_currencies=bnb',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_token_price('ethereum', '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', 'bnb', include_market_cap='true', include_24hr_vol='true', include_last_updated_at='true')

        ## Assert
        assert response == coins_json_sample

    @responses.activate
    def test_failed_get_token_price(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/token_price/ethereum?include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true&contract_addresses=0xB8c77482e45F1F44dE1745F52C74426C631bDD52&vs_currencies=bnb',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_token_price('ethereum', '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', 'bnb', include_market_cap='true', include_24hr_vol='true', include_last_updated_at='true')

    #---------- /simple/supported_vs_currencies ----------#
    @responses.activate
    def test_get_supported_vs_currencies(self):
        # Arrange
        coins_json_sample = ['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau']

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_supported_vs_currencies()

        ## Assert
        assert response == coins_json_sample

    @responses.activate
    def test_failed_get_supported_vs_currencies(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_supported_vs_currencies()


    #---------- /simple/supported_vs_currencies ----------#
    @responses.activate
    def test_get_supported_vs_currencies(self):
        # Arrange
        coins_json_sample = ['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau']

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_supported_vs_currencies()

        ## Assert
        assert response == coins_json_sample

    @responses.activate
    def test_failed_get_supported_vs_currencies(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_supported_vs_currencies()


    #---------- COINS ----------#

    #---------- /price/coins ----------#
    @responses.activate
    def test_failed_get_coins(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coins()

    @responses.activate
    def test_get_coins(self):
        # Arrange
        coins_json_sample = [ { "id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "localization": { "en": "Bitcoin", "es": "Bitcoin", "de": "Bitcoin", "nl": "Bitcoin", "pt": "Bitcoin", "fr": "Bitcoin", "it": "Bitcoin", "hu": "Bitcoin", "ro": "Bitcoin", "sv": "Bitcoin", "pl": "Bitcoin", "id": "Bitcoin", "zh": "Bitcoin", "zh-tw": "Bitcoin", "ja": "Bitcoin", "ko": "Bitcoin", "ru": "Bitcoin", "ar": "Bitcoin", "th": "Bitcoin", "vi": "Bitcoin", "tr": "Bitcoin" }, "image": { "thumb": "https://assets.coingecko.com/coins/images/1/thumb/bitcoin.png?1510040391", "small": "https://assets.coingecko.com/coins/images/1/small/bitcoin.png?1510040391", "large": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1510040391" } } ]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coins()

        ## Assert
        assert response == coins_json_sample


    #---------- /price/coins/list ----------#
    @responses.activate
    def test_failed_get_coins_list(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/list',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coins_list()

    @responses.activate
    def test_get_coins_list(self):
        # Arrange
        coins_json_sample = [ { "id": "bitcoin", "symbol": "btc", "name": "Bitcoin" }, { "id": "litecoin", "symbol": "ltc", "name": "Litecoin" }, { "id": "auroracoin", "symbol": "aur", "name": "Auroracoin" }, { "id": "peercoin", "symbol": "ppc", "name": "Peercoin" }, { "id": "dogecoin", "symbol": "doge", "name": "Dogecoin" }, { "id": "nxt", "symbol": "nxt", "name": "NXT" }, { "id": "omni", "symbol": "omni", "name": "Omni (Mastercoin)" } ]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/list',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coins_list()

        ## Assert
        assert response == coins_json_sample


    #---------- /price/coins/markets ----------#
    @responses.activate
    def test_failed_get_coins_markets(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coins_markets('usd')

    @responses.activate
    def test_get_coins_markets(self):
        # Arrange
        markets_json_sample = [ { "id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1510040391", "current_price": 7015.11823787848, "market_cap": 120934444800.105, "market_cap_rank": 1, "total_volume": 6121170828.21792, "high_24h": 7054.21193531031, "low_24h": 6668.29100755648, "price_change_24h": "299.72373285508", "price_change_percentage_24h": "4.46323343521924", "market_cap_change_24h": "5197755386.983", "market_cap_change_percentage_24h": "4.4910178555649", "circulating_supply": "17236100.0", "ath": 19665.3949272416, "ath_change_percentage": -64.2200698307594, "ath_date": "2017-12-16T00:00:00.000Z", "roi": 0, "last_updated": "2018-08-28T12:12:53.390Z" } ]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd',
                          json = markets_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coins_markets('usd')

        ## Assert
        assert response == markets_json_sample


    #---------- /price/coins/{id} ----------#
    @responses.activate
    def test_failed_get_coin_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coin_by_id('bitcoin')


    @responses.activate
    def test_get_coin_by_id(self):
        # Arrange
        bitcoin_json_sample = { "id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "categories": [ "Cryptocurrency" ], "localization": { "en": "Bitcoin", "es": "Bitcoin", "de": "Bitcoin", "nl": "Bitcoin", "pt": "Bitcoin", "fr": "Bitcoin", "it": "Bitcoin", "hu": "Bitcoin", "ro": "Bitcoin", "sv": "Bitcoin", "pl": "Bitcoin", "id": "Bitcoin", "zh": "比特币", "zh-tw": "比特幣", "ja": "ビットコイン", "ko": "비트코인", "ru": "биткоина", "ar": "بيتكوين", "th": "บิตคอยน์", "vi": "Bitcoin", "tr": "Bitcoin"}}

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/',
                          json = bitcoin_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coin_by_id('bitcoin')

        ## Assert
        assert response == bitcoin_json_sample


    #---------- /price/coins/{id}/tickers ----------#
    @responses.activate
    def test_failed_get_coin_ticker_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/tickers',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coin_ticker_by_id('bitcoin')


    @responses.activate
    def test_get_get_coin_ticker_by_id(self):
        # Arrange
        bitcoin_json_sample = {'name': 'Bitcoin', 'tickers': [{'base': 'BTC', 'target': 'USDT', 'market': {'name': 'BW.com', 'identifier': 'bw', 'has_trading_incentive': False}, 'last': 7963.0, '    volume': 93428.7568, 'converted_last': {'btc': 0.99993976, 'eth': 31.711347, 'usd': 7979.23}, 'converted_volume': {'btc': 93423, 'eth': 2962752, 'usd': 745489919}, '    bid_ask_spread_percentage': 0.111969, 'timestamp': '2019-05-24T11:20:14+00:00', 'is_anomaly': False, 'is_stale': False, 'trade_url': 'https://www.bw.com/trade/btc_us    dt', 'coin_id': 'bitcoin'}]}

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/tickers',
                          json = bitcoin_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coin_ticker_by_id('bitcoin')

        ## Assert
        assert response == bitcoin_json_sample


    #---------- /price/coins/{id}/history ----------#
    @responses.activate
    def test_failed_get_coin_history_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=27-08-2018',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coin_history_by_id('bitcoin', '27-08-2018')


    @responses.activate
    def test_get_coin_history_by_id(self):
        # Arrange
        history_json_sample = { "id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "localization": { "en": "Bitcoin", "es": "Bitcoin", "de": "Bitcoin", "nl": "Bitcoin", "pt": "Bitcoin", "fr": "Bitcoin", "it": "Bitcoin", "hu": "Bitcoin", "ro": "Bitcoin", "sv": "Bitcoin", "pl": "Bitcoin", "id": "Bitcoin", "zh": "比特币", "zh-tw": "比特幣", "ja": "ビットコイン", "ko": "비트코인", "ru": "биткоина", "ar": "بيتكوين", "th": "บิตคอยน์", "vi": "Bitcoin", "tr": "Bitcoin" } }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=27-08-2018',
                          json = history_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coin_history_by_id('bitcoin', '27-08-2018')

        ## Assert
        assert response == history_json_sample


    #---------- /price/coins/{id}/market_chart ----------#
    @responses.activate
    def test_failed_get_coin_market_chart_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coin_market_chart_by_id('bitcoin', 'usd', 1)


    @responses.activate
    def test_get_coin_market_chart_by_id(self):
        # Arrange
        json_response = { "prices": [ [ 1535373899623, 6756.942910425894 ], [ 1535374183927, 6696.894541693875 ], [ 1535374496401, 6689.990513793263 ], [ 1535374779118, 6668.291007556478 ], [ 1535375102688, 6703.7499879964 ], [ 1535375384209, 6706.898948451269 ] ] }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_coin_market_chart_by_id('bitcoin', 'usd', 1)

        ## Assert
        assert response == json_response


    #---------- /price/coins/{id}/status_updates ----------#
    # @responses.activate
    # def test_failed_get_coin_status_updates_by_id(self):
    #     # Arrange
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/litecoin/status_updates',
    #                       status = 404)
    #     exception = HTTPError("HTTP Error")
    #
    #     # Act Assert
    #     with pytest.raises(HTTPError) as HE:
    #         CoinGeckoAPI().get_coin_status_updates_by_id('litecoin')
    #
    #
    # @responses.activate
    # def test_get_coin_status_updates_by_id(self):
    #     # Arrange
    #     json_response = [ {'description': 'Travala.com Partners with Litecoin Foundation to Champion Crypto Payments. \r\n#TravelWithLitecoin www.travala.com/litecoin\r\n\r\nRead the full announcement here: bit.ly/2LumY3b', 'category': 'general', 'created_at': '2019-05-14T13:56:43.282Z', 'user': 'Keith Yong', 'user_title': 'Operations Director', 'pin': False, 'project': {'type': 'Coin', 'id': 'litecoin', 'name': 'Litecoin', 'symbol': 'ltc', 'image': {'thumb': 'https://assets.coingecko.com/coins/images/2/thumb/litecoin.png?1547033580', 'small': 'https://assets.coingecko.com/coins/images/2/small/litecoin.png?1547033580', 'large': 'https://assets.coingecko.com/coins/images/2/large/litecoin.png?1547033580'}}} ]
    #
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/litecoin/status_updates',
    #                       json = json_response, status = 200)
    #
    #     # Act
    #     response = CoinGeckoAPI().get_coin_status_updates_by_id('litecoin')
    #
    #     ## Assert
    #     assert response == json_response


    #---------- /price/coins/{id}/contract/{contract_address} ----------#
    @responses.activate
    def test_failed_get_coin_info_from_contract_address_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/ethereum/contract/0x0D8775F648430679A709E98d2b0Cb6250d2887EF',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coin_info_from_contract_address_by_id(id='ethereum',contract_address='0x0D8775F648430679A709E98d2b0Cb6250d2887EF')


    @responses.activate
    def test_get_coin_info_from_contract_address_by_id(self):
        # Arrange
        json_response = {'id': '0x', 'symbol': 'zrx', 'name': '0x', 'block_time_in_minutes': 0, 'categories': ['Protocol'], 'localization': {'en': '0x', 'es': '0x', 'de': '0x', 'nl': '0x', 'pt': '0x', 'fr': '0x', 'it': '0x', 'hu': '0x', 'ro': '0x', 'sv': '0x', 'pl': '0x', 'id': '0x', 'zh': '0x协议', 'zh-tw': '0x協議', 'ja': 'ロエックス', 'ko': '제로엑스', 'ru': '0x', 'ar': '0x', 'th': '0x', 'vi': '0x', 'tr': '0x'}}

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/ethereum/contract/0x0D8775F648430679A709E98d2b0Cb6250d2887EF',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_coin_info_from_contract_address_by_id(id='ethereum',contract_address='0x0D8775F648430679A709E98d2b0Cb6250d2887EF')

        ## Assert
        assert response == json_response


    #---------- EXCHANGES ----------#


    #---------- /exchanges ----------#
    @responses.activate
    def test_failed_get_exchanges_list(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_exchanges_list()


    @responses.activate
    def test_get_exchanges_list(self):
        # Arrange
        json_response = [ { "id": "bitforex", "name": "Bitforex", "description": "", "url": "https://www.bitforex.com/", "image": "https://assets.coingecko.com/markets/images/214/small/bitforex.jpg?1533199114", "has_trading_incentive": "true", "trade_volume_24h_btc": 680266.637119918 }, { "id": "binance", "name": "Binance", "description": "Binance is a China-based cryptocurrency exchange that lists most of the Chinese coins. It is a popular exchange for its huge number of Initial Coin Offering (ICO) listings and low fees.", "url": "https://www.binance.com/", "image": "https://assets.coingecko.com/markets/images/52/small/binance.jpg?1519353250", "has_trading_incentive": "false", "trade_volume_24h_btc": 189744.350072168 } ]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_exchanges_list()

        ## Assert
        assert response == json_response


    #---------- /exchanges/list ----------#
    @responses.activate
    def test_failed_get_exchanges_id_name_list(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges/list',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_exchanges_id_name_list()


    @responses.activate
    def test_get_exchanges_id_name_list(self):
        # Arrange
        json_response = [{'id': 'abcc', 'name': 'ABCC'}, {'id': 'acx', 'name': 'ACX'}, {'id': 'airswap', 'name': 'AirSwap'}]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges/list',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_exchanges_id_name_list()

        ## Assert
        assert response == json_response



    #---------- /exchanges/{id} ----------#
    @responses.activate
    def test_failed_get_exchanges_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges/bitforex',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_exchanges_by_id('bitforex')


    @responses.activate
    def test_get_exchanges_by_id(self):
        # Arrange
        json_response = { "name": "Bitforex", "has_trading_incentive": "true", "trade_volume_24h_btc": 680266.637119918, "tickers": [ { "base": "BTC", "target": "USDT", "market": { "name": "Bitforex", "identifier": "bitforex", "has_trading_incentive": "true" }, "last": 7039.55, "converted_last": { "btc": "1.001711841446200081963480716", "eth": "24.4986463149997536428213651518458101194944", "usd": "7043.71831205846008527901735024184383795812" }, "volume": 447378.73, "converted_volume": { "btc": "448144.5713519911718500979009072226084", "eth": "10960173.27267390510353832059421689917189597190216256", "usd": "3151209752.222085727501972469271259554059845134991788" }, "timestamp": "2018-08-28T12:46:25.719Z", "is_anomaly": "false" } ] }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges/bitforex',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_exchanges_by_id('bitforex')

        ## Assert
        assert response == json_response


    #---------- EXCHANGE RATES ----------#

    #---------- /exchange_rates ----------#
    @responses.activate
    def test_failed_get_exchange_rates(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchange_rates',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_exchange_rates()


    @responses.activate
    def test_get_exchange_rates(self):
        # Arrange
        json_response = { "rates": { "btc": { "name": "Bitcoin", "unit": "Ƀ", "value": 0, "type": "crypto" }, "eth": { "name": "Ether", "unit": "Ξ", "value": 24.451, "type": "crypto" }, "usd": { "name": "US Dollar", "unit": "$", "value": 7040.152, "type": "fiat" } } }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchange_rates',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_exchange_rates()

        ## Assert
        assert response == json_response
    
    #---------- TRENDING ----------#

    #---------- /search/trending ----------#
    @responses.activate
    def test_failed_search_get_trending(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/search/trending',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_search_trending()


    @responses.activate
    def test_get_search_trending(self):
        # Arrange
        json_response = { "coins": [{"item": {"id":"iris-network", "name":"IRISnet", "symbol":"IRIS", "market_cap_rank":159, "thumb":"/coins/images/5135/thumb/IRIS.png", "score":0}}, {"item": {"id":"hegic", "name":"Hegic", "symbol":"HEGIC", "market_cap_rank":386, "thumb":"/coins/images/12454/thumb/Hegic.png", "score":1}}, {"item": {"id":"moonswap", "name":"MoonSwap", "symbol":"MOON", "market_cap_rank":373, "thumb":"/coins/images/12441/thumb/moon.jpg", "score":2}}, {"item": {"id":"yfv-finance", "name":"YFValue", "symbol":"YFV", "market_cap_rank":179, "thumb":"/coins/images/12198/thumb/yfv.jpg", "score":3}}, {"item": {"id":"yffi-finance", "name":"yffi finance", "symbol":"YFFI", "market_cap_rank":531, "thumb":"/coins/images/11940/thumb/yffi-finance.jpg", "score":4}}, {"item": {"id":"relevant", "name":"Relevant", "symbol":"REL", "market_cap_rank":915, "thumb":"/coins/images/11586/thumb/Relevant.png", "score":5}}, {"item": {"id":"sake-token", "name":"SakeToken", "symbol":"SAKE", "market_cap_rank":503, "thumb":"/coins/images/12428/thumb/sake.png", "score":6}}], "exchanges": [] }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/search/trending',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_search_trending()

        ## Assert
        assert response == json_response

    #---------- GLOBAL ----------#

    #---------- /global ----------#
    @responses.activate
    def test_failed_get_global(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/global',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_global()


    @responses.activate
    def test_get_global(self):
        # Arrange
        json_response = { "data": { "active_cryptocurrencies": 2517, "upcoming_icos": 360, "ongoing_icos": 423, "ended_icos": 2037, "markets": 197 } }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/global',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_global()

        ## Assert
        expected_response = { "active_cryptocurrencies": 2517, "upcoming_icos": 360, "ongoing_icos": 423, "ended_icos": 2037, "markets": 197 }
        assert response == expected_response



    # #---------- FINANCE ----------#
    #
    # #---------- /finance_platforms ----------#
    #
    # @responses.activate
    # def test_failed_get_finance_platforms(self):
    #     # Arrange
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/finance_platforms',
    #                       status = 404)
    #     exception = HTTPError("HTTP Error")
    #
    #     # Act Assert
    #     with pytest.raises(HTTPError) as HE:
    #         CoinGeckoAPI().get_finance_platforms()
    #
    # @responses.activate
    # def test_get_finance_platforms(self):
    #     # Arrange
    #     json_response = [{"name": "Binance Lending", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Celsius Network", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Compound Finance", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "dYdX", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Nexo", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Staked US", "facts": "", "category": "", "centralized": False, "website_url": "https://staked.us/"}, {"name": "Cobo", "facts": "", "category": "", "centralized": False, "website_url": "https://cobo.com/"}, {"name": "Crypto.com", "facts": "", "category": "", "centralized": True, "website_url": "https://crypto.com/en/"}]
    #
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/finance_platforms',
    #                       json = json_response, status = 200)
    #
    #     # Act
    #     response = CoinGeckoAPI().get_finance_platforms()
    #
    #     ## Assert
    #     expected_response = [{"name": "Binance Lending", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Celsius Network", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Compound Finance", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "dYdX", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Nexo", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Staked US", "facts": "", "category": "", "centralized": False, "website_url": "https://staked.us/"}, {"name": "Cobo", "facts": "", "category": "", "centralized": False, "website_url": "https://cobo.com/"}, {"name": "Crypto.com", "facts": "", "category": "", "centralized": True, "website_url": "https://crypto.com/en/"}]
    #     assert response == expected_response
    #
    # #---------- /finance_products ----------#
    #
    # @responses.activate
    # def test_failed_get_finance_products(self):
    #     # Arrange
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/finance_products',
    #                       status = 404)
    #     exception = HTTPError("HTTP Error")
    #
    #     # Act Assert
    #     with pytest.raises(HTTPError) as HE:
    #         CoinGeckoAPI().get_finance_products()
    #
    # @responses.activate
    # def test_get_finance_products(self):
    #     # Arrange
    #     json_response = [{"name": "Binance Lending", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Celsius Network", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Compound Finance", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "dYdX", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Nexo", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Staked US", "facts": "", "category": "", "centralized": False, "website_url": "https://staked.us/"}, {"name": "Cobo", "facts": "", "category": "", "centralized": False, "website_url": "https://cobo.com/"}, {"name": "Crypto.com", "facts": "", "category": "", "centralized": True, "website_url": "https://crypto.com/en/"}]
    #
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/finance_platforms',
    #                       json = json_response, status = 200)
    #
    #     # Act
    #     response = CoinGeckoAPI().get_finance_platforms()
    #
    #     ## Assert
    #     expected_response = [{"name": "Binance Lending", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Celsius Network", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Compound Finance", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "dYdX", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Nexo", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Staked US", "facts": "", "category": "", "centralized": False, "website_url": "https://staked.us/"}, {"name": "Cobo", "facts": "", "category": "", "centralized": False, "website_url": "https://cobo.com/"}, {"name": "Crypto.com", "facts": "", "category": "", "centralized": True, "website_url": "https://crypto.com/en/"}]
    #     assert response == expected_response


