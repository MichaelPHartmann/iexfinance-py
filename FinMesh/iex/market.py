from ._common import *
# These get functions are all the same, but have been delineated for ease of use.
# Symbols from any IEX data-points market endpoint will work in either function.

# Returns a single number for the requested symbol
IEX_ECONOMIC_DATA_URL = prepend_iex_url('data-points/market') + '{symbol}'
def economic_data(symbol):
    url = replace_url_var(IEX_ECONOMIC_DATA_URL, symbol=symbol)
    url += '?'
    return get_iex_json_request(url)

# Returns dictionary of accepted symbols for use in the economic data function
def economic_data_symbols():
    accepted_symbols = [
    'MORTGAGE30US':'US 30-Year fixed rate mortgage average',
    'MORTGAGE15US':'US 15-Year fixed rate mortgage average',
    'MORTGAGE5US':'US 5/1-Year adjustable rate mortgage average',
    'FEDFUNDS':'Effective federal funds rate',
    'TERMCBCCALLNS':'Commercial bank credit card interest rate as a percent, not seasonally adjusted',
    'MMNRNJ':'CD Rate Non-Jumbo less than $100,000 Money market',
    'MMNRJD':'CD Rate Jumbo more than $100,000 Money market',
    'A191RL1Q225SBEA':'Real Gross Domestic Product',
    'INDPRO':'Industrial Production Index',
    'CPIAUCSL':'Consumer Price Index All Urban Consumers',
    'PAYEMS':'Total nonfarm employees in thousands of persons seasonally adjusted',
    'HOUST':'Total Housing Starts in thousands of units, seasonally adjusted annual rate',
    'UNRATE':'Unemployment rate returned as a percent, seasonally adjusted',
    'TOTALSA':'Total Vehicle Sales in millions of units',
    'RECPROUSM156N':'US Recession Probabilities.'
    ]

# Returns a single price for the requested symbol
IEX_COMMODITY_URL = prepend_iex_url('data-points/market') + '{symbol}'
def commodity_data(symbol):
    url = replace_url_var(IEX_COMMODITY_URL, symbol=symbol)
    url += '?'
    return get_iex_json_request(url)

# Returns dictionary of accepted symbols for use in the commodity function
def commodities_symbols():
    accepted_symbols = [
    'DCOILWTICO':'Crude oil West Texas Intermediate - in dollars per barrel, not seasonally adjusted',
    'DCOILBRENTEU':'Crude oil Brent Europe - in dollars per barrel, not seasonally adjusted',
    'DHHNGSP':'Henry Hub Natural Gas Spot Price - in dollars per million BTU, not seasonally adjusted',
    'DHOILNYH':'No. 2 Heating Oil New York Harbor - in dollars per gallon, not seasonally adjusted',
    'DJFUELUSGULF':'Kerosense Type Jet Fuel US Gulf Coast - in dollars per gallon, not seasonally adjusted',
    'GASDESW':'US Diesel Sales Price - in dollars per gallon, not seasonally adjusted',
    'GASREGCOVW':'US Regular Conventional Gas Price - in dollars per gallon, not seasonally adjusted',
    'GASMIDCOVW':'US Midgrade Conventional Gas Price - in dollars per gallon, not seasonally adjusted',
    'GASPRMCOVW':'US Premium Conventional Gas Price - in dollars per gallon, not seasonally adjusted',
    'DPROPANEMBTX':'Propane Prices Mont Belvieu Texas - in dollars per gallon, not seasonally adjusted'
    ]
    return accepted_symbols
