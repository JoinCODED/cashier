# Fork & Clone

Fork and clone [this repository](https://github.com/JoinCODED/cashier) in your `python` directory.

---

# Task 

In this task you'll be building a system to assist a cashier where the cashier has to enter the items bought and at the end a receipt will be printed.

```
Item (enter "done" when finished): apples
Price: .2
Quantity: 4
Item (enter "done" when finished): carrot
Price: .1
Quantity: 1
Item (enter "done" when finished): flour
Price: 1.3
Quantity: 2
Item (enter "done" when finished): water bottles
Price: .05
Quantity: 10
Item (enter "done" when finished): done

-------------------
receipt
-------------------
4 apples 0.800KD
1 carrot 0.100KD
2 flour 2.600KD
10 water bottles 0.500KD
-------------------
Total Price: 4.000KD
```

## Steps:

1. A `while` loop that checks the users input. The loop ends if the user types "done" for the item name.
2. Save the user's input (the item's name, price, quantity) in a dictionary. Append this dictionary to a list of items. This list of items is a list of dictionaries, where each dictionary represents an item.
	- In the example above, the list of items looks like this:

			[
				{
					"name": "apples",
					"price": .2,
					"quantity": 4
				},
				{
					"name": "carrot",
					"price": .1,
					"quantity": 1 
				},
				{
					"name": "flour",
					"price": 1.3,
					"quantity": 2
				},
				{
					"name": "water bottles",
					"price": .05,
					"quantity": 10
				},
			]

3. Using a `for` loop, go through the list and print the receipt.
4. Push your code.
