/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
 */

public class P001
{

	public static void main(String[] args)
	{
		int sum = 0;
		int max = 1000;
		
		for (int integer = 1; integer < max; integer++)
			if (integer % 3 == 0 || integer % 5 == 0)
			{
				sum += integer;
			} else {
				continue;
			}
		System.out.print(sum);
	}
}