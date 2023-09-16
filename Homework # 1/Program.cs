

using _01_sorts;

Console.Clear();

Sorts sorts = new Sorts();

int[] arrFirst = { 8, 0, -4, 7, -2, 2, -9, 3 };
int[] arrSecond = { 80, 0, -40, 70, -20, 20, -90, 30 };

Console.WriteLine($"Исходный массив для метода SortImperative: \t\t[ {string.Join(", ", arrFirst)} ]");
Console.WriteLine($"Исходный массив для метода SortDeclarative: \t\t[ {string.Join(", ", arrSecond)} ]");

sorts.SortImperative(arrFirst);
Console.WriteLine($"Отсортированный массив методом SortImperative: \t\t[ {string.Join(", ", arrFirst)} ]");

sorts.SortDeclarative(arrSecond);
Console.WriteLine($"Отсортированный массив методом SortDeclarative: \t[ {string.Join(", ", arrSecond)} ]");