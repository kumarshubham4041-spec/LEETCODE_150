# Question :Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.Given an integer, convert it to a Roman numeral.
# Approach : Firstly i created a list of lists called roman to store values of roman symbols with their corresponding integers. and an empty string called results to store results..Then i iterated the roman list and checked if division of number exits.If it exists i put the count of number of times any roman symbol need to be added inn answer. Then i updated the num by taking the remainderr of num and value.Finally i returned the answeer string.
# Time Complexity : O(n)
# Space Complexity : O(1)

    def intToRoman(self, num: int) -> str:
        roman = [["I",1],['IV',4],['V',5],['IX',9],['X',10],['XL',40],['L',50],['XC',90],['C',100],['CD',400],['D',500],['CM',900],['M',1000]]
        result = ""
        for rom,value in reversed(roman):
            if num//value:
                count = num//value
                result += (rom*count)
                num %= value

        return result
