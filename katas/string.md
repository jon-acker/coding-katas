## String Caluclator Kata

Use PhpSpec to describe the class `StringCalculator`. Give the class a method called `calc`, which does the following:

 - It returns 0 for empty string
 - It returns the bare number for a single number
   (e.g. '2' -> 2)
 - It returns the sum of space-separated numbers
   (e.g. '1 2' -> 3)
 - It returns the sum of any whitespace-separated numbers
   (e.g. "1  2\t3\n4" -> 10)
- It returns the sum of numbers separated by custom separator given as first char
    (e.g. '~1~2' -> 3)