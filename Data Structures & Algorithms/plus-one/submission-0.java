class Solution {
    public int[] plusOne(int[] digits) {
        ArrayList<Integer> arr = new ArrayList<>();
        int carry = 1;
        int n = digits.length;
        // int[] arr = new int[n+1]
        for(int i = n-1; i >= 0; i--){
            if(carry==0){
                arr.addFirst(digits[i]);
            }
            else{
                int t = digits[i] + carry;
                if(t>9){
                    arr.addFirst(0);
                    carry=1;
                }
                else{
                    arr.addFirst(t);
                    carry=0;
                }
            }
        }
        if(carry>0)arr.addFirst(carry);

        return arr.stream().mapToInt(Integer::intValue).toArray();
    }
}
