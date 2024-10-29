class arithmetic_op:
    def sum(self):
        x=20
        y=30
        return x+y
    def mul(self):
        a=20
        b=5
        return a*b
    def sub(self):
        p=100
        q=50
        return p-q

    def div(self):
        c = 20
        d = 30
        return c/d

    def mod(self):
        e = 30
        f = 20
        return e//f
    def even_odd(self):
        g = 5
        if g%2==0:
            return "Even"
        else:
            return "Odd"
    def pos_negative(self):
        x = 20
        if x<0:
            return "negative number"
        else:
            return "Positive number"

    def fact(self):
        n = 5
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return f"factorical of {n} is: {fact}"

    def prime_no(self):
        n = 5
        prime = False
        if n == 0 or n == 1:
            return f"Given number {n} Prime number is {prime}"
        elif n > 1:
            for i in range(2, n):
                if n % i == 0:
                    prime = True
            if prime:
                return f"Given number {n} Prime number is {prime}"
            else:
                return f"Given number {n} Prime number is {prime}"
    def mobile_no_validation(self):
        ph = "9010926136"
        if len(ph) == 10:
            return "Given phone number is valid"
        elif len(ph) < 5:
            return "Given phone number is not valid because the given length of number is less than 5"
        else:
            return "Given phone number is not valid"