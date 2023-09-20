using System;
using System.Text.RegularExpressions;

int InputNumber()
{
  int number = 0;
  string input = string.Empty;
  Regex regex = new Regex("^[0-9]+$", RegexOptions.Compiled);

  while (!regex.IsMatch(input))
  {
    Console.WriteLine("Введите любое целое число:\t");
    input = Console.ReadLine();
  }
  number = int.Parse(input);
  return number;
}

void MultiplicationTableOfOneColumn(int secondNumber, int firstNumber = 1)
{
  int result = 0;
  for (int i = firstNumber; i <= secondNumber; i++)
  {
    result = firstNumber * i;
    Console.WriteLine($"{firstNumber} * {i} = {result}");
  }
}



int num = InputNumber();
MultiplicationTableOfOneColumn(num);
