#include <string>
using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        // Handle special cases when either number is zero
        if (num1 == "0" || num2 == "0") {
            return "0";
        }
        
        // Initialize variables
        int m = num1.length();
        int n = num2.length();
        vector<int> product(m + n, 0);
        
        // Multiply each digit from right to left
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                // Multiply the current digits and add the result to the corresponding positions
                int digit1 = num1[i] - '0';
                int digit2 = num2[j] - '0';
                int currProduct = digit1 * digit2;
                
                // Add the current product to the existing value at the corresponding positions
                int pos1 = i + j;
                int pos2 = i + j + 1;
                int currSum = currProduct + product[pos2];
                
                // Update the carry and the product at the current positions
                int carry = currSum / 10;
                product[pos1] += carry;
                product[pos2] = currSum % 10;
            }
        }
        
        // Convert the product vector to a string representation
        string result = "";
        for (int digit : product) {
            if (!(digit == 0 && result.length() == 0)) {
                result += to_string(digit);
            }
        }
        
        return result;
    }
};