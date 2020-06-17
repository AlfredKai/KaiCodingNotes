class Solution:
    def validIPAddress(self, IP: str) -> str:
        type = ['IPv4', 'IPv6', 'Neither']

        def v4(numbers):
            for n in numbers:
                if n == '-0':
                    return type[2]
                for i, c in enumerate(n):
                    if c == '0' and i != len(n) - 1:
                        return type[2]
                    else:
                        break
                try:
                    if int(n) < 0 or int(n) > 255:
                        return type[2]
                except:
                    return type[2]
            return type[0]

        def v6(numbers):
            for n in numbers:
                if n == '-0':
                    return type[2]
                if len(n) > 4 or len(n) == 0:
                    return type[2]
                for c in n:
                    if c.isalpha() and c.lower() > 'f':
                        return type[2]
            return type[1]

        numbers = IP.split('.')
        if len(numbers) == 4:
            return v4(numbers)
        numbers = IP.split(':')
        if len(numbers) == 8:
            return v6(numbers)
        return type[2]

a = Solution()
a.validIPAddress("192.0.0.1")