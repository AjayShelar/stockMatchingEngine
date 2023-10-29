# Matching Engine

## Introduction
This is a simple matching engine designed to match buy and sell orders for two hypothetical stocks, TATA and RELIANCE. The engine uses a combination of the FIFO (First In, First Out) and Pro Rata algorithms to match the orders based on the price quoted.
https://en.wikipedia.org/wiki/Order_matching_system

## How to Use
To use the matching engine, follow these steps:

1. Instantiate the MatchingEngine class.
2. Add buy and sell orders for TATA and RELIANCE stocks using the add_order method.
3. Use the match_orders method to match the buy and sell orders based on the implemented algorithms.

## Example Usage
Here is an example of how to use the matching engine:

```python
matching_engine = MatchingEngine()
matching_engine.add_order("TATA", "buy", 100, 30)
matching_engine.add_order("TATA", "sell", 100, 50)
matching_engine.match_orders()
