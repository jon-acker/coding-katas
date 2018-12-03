## Library Lending System


Objective: collaboratively come up with use-case examples and write executable specifications (Gherkin scenarios) for system that allows library members to borrow and return book, as well as charge the correct overdue fines.

Use the scenarios to drive the code to create a software model of the library lending process (the end product is a bunch of classes that can be instantiated and used to run business)

Identify the boundaries of the system (where infrastructure woould be connected .e.g. apis or database) and use interfaces at these points. Provide `fake` implementations for the infrastructure in order to run the scenarios.

Identify the ubiquitous language of the library lending and fine charging domain and use the same language to write the scenarios in.
E.g. is it `Fee` or `Fine`? is the fine `charged` or `incurred`? Be consistent.
Pay attention to the nouns, verbs adverbs etc

  Rules:
  - Borrower needs to be `registered` with the `Library` (become a `Member`)
  - Library has a `catalog` which says how many of each book is in stock
  - Members can only `borrow` books that are in stock
  - Only 2 books can be borrowed at a time
  - Books can be borrowed for 3 days
  - `Returning` a book up to a week late incurs £5 fine
  - `Returning` a book more than a week late incurs £10 fine
  - Books can be `Checked out` or `Renewed` at the `Circulation Desk`
  - A book can only be `renewed` once
  - Member can `reserve` a book that's not in stock (in which case a `hold` is placed on the book and as soon as it is returned the borrower is notified and no one else can borrow the book.)
 
  - Members `Borrow` books - but the library `Lends` them.
  
  
In order to identify scenarios an event storming session might be useful to sketch out a timeline of a member borrowing, returning and being charged late return feeds.

Simple example:
```Gherkin
  Background:
    Given Jon is a member of the library

  Scenario: Borrower is lent a book that's in stock
    Given there is 1 copy of "Harry Potter" in stock
    When Jon borrows the book "Harry Potter" from the library
    Then stock count for "Harry Potter" should be 0
    And the book "Harry Potter" should be loaned to Jon
```

More complex example 
```Gherkin
  Scenario: Returning a book late - incurring a fine (after cuttoff)
    Given Jon borrowed the book "Harry Potter" on 17th of March
    When Jon returns the book "Harry Potter" on the 21st of March at 00:00
    Then Jon should be charged a £5 fine
```