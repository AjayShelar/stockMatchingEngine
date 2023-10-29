class MatchingEngine:
    def __init__(self):
        self.tata_buy_orders = []
        self.tata_sell_orders = []
        self.reliance_buy_orders = []
        self.reliance_sell_orders = []

    def add_order(self, stock, order_type, price, quantity):
        if stock == "TATA":
            if order_type == "buy":
                self.tata_buy_orders.append((price, quantity))
            elif order_type == "sell":
                self.tata_sell_orders.append((price, quantity))
        elif stock == "RELIANCE":
            if order_type == "buy":
                self.reliance_buy_orders.append((price, quantity))
            elif order_type == "sell":
                self.reliance_sell_orders.append((price, quantity))
        else:
            print("Invalid stock")

    def match_orders(self):
        for tata_sell_order in self.tata_sell_orders:
            remaining_quantity = tata_sell_order[1]
            for reliance_buy_order in sorted(self.reliance_buy_orders):
                if reliance_buy_order[0] >= tata_sell_order[0]:
                    matched_quantity = min(remaining_quantity, reliance_buy_order[1])
                    remaining_quantity -= matched_quantity
                    reliance_buy_order = (reliance_buy_order[0], reliance_buy_order[1] - matched_quantity)
                    print(f"TATA sell order of {matched_quantity} units matched with RELIANCE buy order at price {reliance_buy_order[0]}")
                    if reliance_buy_order[1] == 0:
                        if reliance_buy_order in self.reliance_buy_orders:
                            self.reliance_buy_orders.remove(reliance_buy_order)
                if remaining_quantity == 0:
                    break
            if remaining_quantity > 0:
                print(f"TATA sell order of {tata_sell_order[1] - remaining_quantity} units unmatched.")

        for reliance_sell_order in self.reliance_sell_orders:
            remaining_quantity = reliance_sell_order[1]
            for tata_buy_order in sorted(self.tata_buy_orders):
                if tata_buy_order[0] >= reliance_sell_order[0]:
                    matched_quantity = min(remaining_quantity, tata_buy_order[1])
                    remaining_quantity -= matched_quantity
                    tata_buy_order = (tata_buy_order[0], tata_buy_order[1] - matched_quantity)
                    print(f"RELIANCE sell order of {matched_quantity} units matched with TATA buy order at price {tata_buy_order[0]}")
                    if tata_buy_order[1] == 0:
                        if tata_buy_order in self.tata_buy_orders:
                            self.tata_buy_orders.remove(tata_buy_order)
                if remaining_quantity == 0:
                    break
            if remaining_quantity > 0:
                print(f"RELIANCE sell order of {reliance_sell_order[1] - remaining_quantity} units unmatched.")

        # Print pending orders
        print("Pending TATA Buy Orders:", self.tata_buy_orders)
        print("Pending TATA Sell Orders:", self.tata_sell_orders)
        print("Pending RELIANCE Buy Orders:", self.reliance_buy_orders)
        print("Pending RELIANCE Sell Orders:", self.reliance_sell_orders)


# Example usage:
matching_engine = MatchingEngine()
matching_engine.add_order("TATA", "buy", 100, 30)
matching_engine.add_order("TATA", "buy", 110, 40)
matching_engine.add_order("TATA", "buy", 120, 70)
matching_engine.add_order("TATA", "buy", 110, 20)
matching_engine.add_order("TATA", "sell", 100, 50)
matching_engine.add_order("TATA", "sell", 100, 30)
matching_engine.add_order("TATA", "sell", 120, 70)
matching_engine.add_order("TATA", "sell", 110, 20)

matching_engine.add_order("RELIANCE", "buy", 90, 20)
matching_engine.add_order("RELIANCE", "buy", 100, 70)
matching_engine.add_order("RELIANCE", "buy", 110, 60)
matching_engine.add_order("RELIANCE", "buy", 120, 80)
matching_engine.add_order("RELIANCE", "sell", 100, 30)
matching_engine.add_order("RELIANCE", "sell", 110, 40)
matching_engine.add_order("RELIANCE", "sell", 120, 50)

matching_engine.match_orders()
