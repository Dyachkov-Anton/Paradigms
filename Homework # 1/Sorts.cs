using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _01_sorts
{
	internal class Sorts
	{
		public Sorts() { }

		public int[] SortImperative(int[] inputArray)
		{
			return QuickSort(inputArray, 0, inputArray.Length - 1);
		}

		public int[] SortDeclarative(int[] inputArray)
		{
			Array.Sort(inputArray);
			return inputArray;
		}



		private int[] QuickSort(int[] array, int minIndex, int maxIndex)
		{
			if (minIndex >= maxIndex) return array;
			int pivot = GetPivotIndex(array, minIndex, maxIndex);
			QuickSort(array, minIndex, pivot - 1);
			QuickSort(array, pivot + 1, maxIndex);
			return array;
		}


		private int GetPivotIndex(int[] array, int minIndex, int maxIndex)
		{
			int pivotIndex = minIndex - 1;
			for (int i = minIndex; i <= maxIndex; i++)
			{
				if (array[i] < array[maxIndex])
				{
					pivotIndex++;
					Swap(array, i, pivotIndex);
				}
			}
			pivotIndex++;
			Swap(array, pivotIndex, maxIndex);
			return pivotIndex;
		}


		private void Swap(int[] array, int leftValue, int rightValue)
		{
			int temp = array[leftValue];
			array[leftValue] = array[rightValue];
			array[rightValue] = temp;
		}
	}
}
