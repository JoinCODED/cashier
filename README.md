# Fork & Clone

Fork and clone [this repository](https://github.com/JoinCODED/cashier) in your `python` directory.

---

## Task

In this task you'll be building a system to assist a cashier where the cashier has to enter the items bought and at the end a receipt will be printed.

```code
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

## Steps

1. In the `get_invoice_items` function:
    1. Create a list called `invoice_items`.
    2. Loop through the items received in the parameter and format them in the following way: `quantity name subtotal currency`. Here is an example of items that this function might receive:

        ```python
        [
        {'name': 'Apple', 'quantity': 1, price: 0.2 },
        {'name': 'Orange', 'quantity': 4, price: 0.3 },
        ]
        ```

    3. Add each formatted line item to your `invoice_items` list.
    4. Return your `invoice_items` after looping through all the items.
2. In the `get_total` function:
    1. Initialize the `total` to be `0`.
    2. Loop through all the items, calculate the subtotal (`quantity * price`) for each item and add that to your total.
    3. Return your `total` after looping through all the items.
3. In the `print_receipt` function, you will receive `invoice_items` from `get_invoice_items` and the `total` from `get_total`:
    1. Print out a title (e.g., `Receipt`).
    2. Print all the formatted invoice line items on separate lines.
    3. Print out the total price at the end.
4. In the main function:
    1. Create a list called `items`, you will be adding the items received from the user to this `list`.
    2. Ask the user for an item name, and inform to input `done` if they are done.
    3. Add a `while` loop that checks the users input. The loop ends if the user types `"done"` for the item name.
    4. Save the user's input (the item's name, price, quantity) in a dictionary. Append this dictionary to a `list` of `items` in Step 1. This list of items is a list of dictionaries, where each dictionary represents an item.
        - In the example above, the list of items looks like this:

            ```python
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
            ```

    5. Get the `invoice items` and `total` using the functions you have added above.
    6. Use `print_receipt` to show the user's receipt.
5. Push your code.
