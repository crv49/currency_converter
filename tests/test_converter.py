import pytest
from converter import convert
from fetcher import get_exchange_rate

def test_convert():
    #initial tests
    assert convert(100, 0.5) == 50				            #checks the currency is converted correctly
    assert round(convert(123.45, 1.23), 4) == 151.8435		#rounds the conversion to 4 decimal places
    
    #edge case: zeroes
    assert convert(0, 1.23) == 0 				            #converting to 0 should result in 0

    #edge case: negatives
    with pytest.raises(ValueError, match="Amount cannot be negative"):
        convert(-10, 1.2)
     
def test_get_exchange_rate_api():
    #edge case: API call failures
    with pytest.raises(ConnectionError, match="Failed to fetch rates from API."):
    	get_exchange_rate("USD", "EUR", use_mock=False)	     

def test_get_exchange_rate_unsupported():
    #edge case: Unsupported currency in mock data
    with pytest.raises(ValueError, match="Currency XXX not found in mock data."):
        get_exchange_rate("USD", "XXX", use_mock=True)



