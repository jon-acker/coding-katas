## Rules
   Customer can:
   + `Deposit` any amount
   + `Withdraw` as much as their balance
   + `Print` their statement

Make use the `domain language` in the code

The statement contains a list of all the `customers` `transactions` with the columns: Date, Amount Deposited, Balance after depositing.

When there are no `transactions` - the statement contains only the column headers.
This is an example of the output of print-statement:

```
Date       | Amount | Balance
2023-01-14 | -500   | 2500
2023-01-13 | 2000   | 3000
2023-01-10 | 1000   | 1000
```

### Start a test for no transactions
```
Date       | Amount | Balance
```

### Then a test for one transaction
```
Date       | Amount | Balance
2023-01-10 | 1000   | 1000
```

### Followed by a test for two deposites that affect balance
```
Date       | Amount | Balance
2023-01-10 | 1000   | 2000
``` 

