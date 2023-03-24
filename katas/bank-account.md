### Customer can
   deposit any amount
   withdraw as much as they have
   print their statement

`Use the domain language in the code`

The statement contains the: Date, Amount Deposited, Balance after depositing
This is an example of the output of print statement
```
Date       | Amount | Balance
2023-01-14 | -500   | 2500
2023-01-13 | 2000   | 3000
2023-01-10 | 1000   | 1000
```

### Start a test for zero rows
```
Date       | Amount | Balance
```

### Then a test for one row
```
Date       | Amount | Balance
2023-01-10 | 1000   | 1000
```

### A test for two transactions: 2 deposits
```
Date       | Amount | Balance
2023-01-10 | 1000   | 1000
2023-01-10 | 500    | 1500
```

### A test for two transactions: deposit and withdraw
```
Date       | Amount | Balance
2023-01-10 | 1000   | 1000
2023-01-10 | -500   | 500
```

### A test for two transactions, on two different dates
```
Date       | Amount | Balance
2023-01-10 | 1000   | 1000
2023-01-11 | 500    | 1500
```

### Advanced: A test for interest being gained at the end of the month
```
Date       | Amount | Balance
2023-01-10 | 1000   | 1000
2023-05-10 | 500    | 1500
2023-30-10 | .10    | 1500.10
```

### Advanced: transfer between two separate accounts? identified by account number


### Introduction to Event Sourcing - using bank transactions as events
Store list of transactions in text file
Play back list of transactions in order to get back to last state