## String Caluclator Kata

Use PhpSpect to describe the class `StringCalculator`. Give the class a method which:

 - It returns 0 for empty string
 - It returns 0 for the string '0'
 - It returns the bare number for a single number 
   (e.g. '2' -> 2)
 - It returns the sum of space-separated numbers
   (e.g. '1 2' -> 3)
 - It returns the sum of any whitespace-separated numbers
   (e.g. '1  2/t3/n4' -> 10)
- It returns the sum of numbers separated by custom separator given as first char
    (e.g. '~1~2' -> 3)