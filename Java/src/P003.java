/*
 * What is the largest prime factor of the number 600851475143.
 */

public class P003
{

	public static void main(String[] args)
	{

		int largePrime = 2;
		long largeNum = 6000851475143L;
		
		while (largePrime< largeNum)
		{
			if (largeNum % largePrime == 0)
			{
				largeNum /= largePrime;
			} else {
				largePrime += 1;
			}
		}
		System.out.print(largePrime);
	}
}