# TDD and BDD Coding Katas


# Running
## PHP
`composer install`

`bin/phpspec describe MyClass`

`bin/phpspec run`

## Node
`node_modules/.bin/jest js/spec/TennisGame.test.js`

or just

`node_modules/.bin/mocha js/test/`

## In Dockerized enivonrment
There are two containers provided: php & node

`docker-comopose up -d`

### PHP

`docker-compose exec php {your-cmd}`

### Node
`docker-compose exec node {your-command}`


or 
`make test-js` will run all the JS tests


## Katas

### TDD (at class/unit level)

These are simple TDD kata's that can usually be created with one or two classes.
Start with a failing test - implement code to make it pass, refactor and then move on to the next case.

* [String Calculator][kata-string]
* [Tennis Game][kata-tennis]
* [Fibonacci Sequence][kata-fibonacci]

[kata-string]: ./katas/string.md
[kata-fibonacci]: ./katas/fibonacci.md
[kata-tennis]: ./katas/tennis.md


### BDD (build domain model)

These are kata's for BDD practice and modeling. One kata is just creating scenarios using various techniques e.g. Example Mapping or Event Storming.
For the second kata, start with existing scenarios and write code that fulfills those examples (meets those criteria).

* [Library Lending System][kata-library]

[kata-library]: ./katas/library-lending.md
