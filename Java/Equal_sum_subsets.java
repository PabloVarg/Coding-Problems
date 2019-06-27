/* This problem was asked by Facebook.

Given a multiset of integers, return
whether it can be partitioned into two
subsets whose sums are the same.

For example, given the multiset
{15, 5, 20, 10, 35, 15, 10}, it would
return true, since we can split it up
into {15, 5, 10, 15, 10} and {20, 35},
which both add up to 55.

Given the multiset {15, 5, 20, 10, 35},
it would return false, since we can't
split it up into two subsets that add
up to the same sum. */

import java.util.Arrays;
import java.util.stream.IntStream;

class Algorithm{

    public static boolean isDivisible(int [] array){
        int sum = Arrays.stream(array).sum();

        int first = array[0], second = sum - array[0];

        for(int i: array){
            if(first == second)
                return true;
            first += i;
            second -= i;
        }

        return false;
    }

}

public class Equal_sum_subsets{

    public static void main(String[] args){
        int[] array = {15, 5, 20, 10, 35, 15, 10};

        System.out.println(Algorithm.isDivisible(array));
    }

}
