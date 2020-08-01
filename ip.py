class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(IP):
            numbers = IP.split(".")

            if len(numbers) != 4:
                return False

            for numberStr in numbers:
                for x in numberStr:
                    if not x.isdigit():
                        return False

                if len(numberStr) == 0:
                    return False

                number = int(numberStr)

                if number < 0 or number >255:
                    return False

                if (number != 0 and numberStr[0] == "0") or (number == 0 and len(numberStr) != 1):
                    return False
            return True

        def isIPv6(IP):
            numbers = IP.lower().split(":")
            if len(numbers) != 8:
                return False

            for i in numbers:
                for j in i:
                    if not (j.isdigit() or j in "abcdef"):
                        return False

                if len(i)>4 or len(i)<=0:
                    return False
            return True

        if isIPv4(IP):
            return "IPv4"
        if isIPv6(IP):
            return "IPv6"
        return "Neither"
o1 = Solution()
print(o1.validIPAddress("2001:db8:85a3:0::8a2E:0370:7334"))
