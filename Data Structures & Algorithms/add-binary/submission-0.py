class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 =  len(a) 
        n2 = len(b) 
        res = ""

        if n1 > n2:
            for i in range(n1-n2):
                b = "0" + b
        elif n2 > n1:
            for i in range(n2 - n1):
                a = "0" + a
        carry = 0 
        # print(a, b)
        for i in range(max(n1, n2) - 1, -1, -1):
            # print('carry', carry)
            # print('a', a[i], 'b', b[i])
            if carry == 0:
                if a[i] == "0":
                    if b[i] == "0":
                        res = "0"+res
                        carry = 0
                    else:
                        res = "1" + res
                        carry = 0
                else:
                    if b[i] == "0":
                        res = "1" + res
                        carry = 0
                    else:
                        res = "0" + res
                        # print(res)
                        carry = 1

            else:
                if a[i] == "0":
                    if b[i] == "0":
                        res = "1"+res
                        carry = 0
                    else:
                        res = "0" + res
                        carry = 1
                    
                else:
                    if b[i] == "0":
                        res = "0" + res
                        carry = 1
                    else:
                        res = "1" + res
                        carry = 1
            # print('res', res)   
        
        return res if carry == 0 else "1" + res









        