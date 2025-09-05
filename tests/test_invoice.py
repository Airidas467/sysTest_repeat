import pytest
import os
from invoice import (
    getItemName, getItemNumber, getPrice, availableQuantity,
    getCurrencyValue, adjustStockQuantity, checkStock,
    calculateVAT, discount, createInvoiceData, generateInvoice
)

@pytest.fixture
def sample_stock():
    """Fixture for a small stock list: [name, price, quantity]"""
    return [
        ["Apple", 1.0, 10],
        ["Banana", 2.0, 5],
        ["Cherry", 5.0, 0],
    ]


def test_get_item_name(sample_stock):
    assert getItemName(sample_stock, 0) == "Apple"


def test_get_item_number(sample_stock):
    assert getItemNumber(sample_stock, "Banana") == 1
    assert getItemNumber(sample_stock, "NotExist") == -1


def test_get_price(sample_stock):
    assert getPrice(sample_stock, 1) == 2.0


def test_available_quantity(sample_stock):
    assert availableQuantity(sample_stock, 0) == 10
    assert availableQuantity(sample_stock, 2) == 0


@pytest.mark.parametrize("amount, expected", [
    (10, 0.0),    
    (25, 2.5),    
    (60, 12.0),   
])
def test_discount(amount, expected):
    assert discount(amount) == expected


@pytest.mark.parametrize("amount, expected", [
    (100, 22.0),  
    (50, 11.0),
])
def test_calculate_vat(amount, expected):
    assert calculateVAT(amount) == expected


@pytest.mark.parametrize("amount, ccy, expected", [
    (100, "EUR", 100.0),
    (100, "GBP", 88.0),
    (100, "USD", 109.0),
])
def test_get_currency_value(amount, ccy, expected):
    assert getCurrencyValue(amount, ccy) == expected

def test_adjust_stock_quantity(sample_stock):
    adjustStockQuantity(sample_stock, 0, -2)
    assert availableQuantity(sample_stock, 0) == 8


def test_check_stock(sample_stock):
    assert checkStock(sample_stock, 0, 5) is True
    assert checkStock(sample_stock, 1, 10) is False 


def test_create_invoice_data(sample_stock):
   
    result = createInvoiceData(sample_stock, 0, 2, "EUR")

    assert pytest.approx(result[0]) == 1.0      
    assert pytest.approx(result[1]) == 2.0     
    assert pytest.approx(result[2]) == 0.0     
    assert pytest.approx(result[3]) == 0.44     
    assert pytest.approx(result[4]) == 2.44    


def test_generate_invoice_output_format():
    invoice = generateInvoice(
        "Apple", 2, "EUR", 1.0, 2.0, 0.0, 0.44, 2.44
    )
   
    joined = "".join(invoice)
    assert "Item:" in joined
    assert "Net Total:" in joined
