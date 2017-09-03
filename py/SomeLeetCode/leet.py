

def convert(s, numRows):
    if numRows == 1 or numRows>=len(s):
        return s
    ConvertStr = ['']*numRows
    index, step = 0, 1

    for x in s:
        ConvertStr[index] += x
        if index == 0:
            step  = 1
        elif index == numRows - 1:
            step = -1
        index += step

    return ''.join(ConvertStr)

# print(convert("ABCDEF", 4))
# print(convert("ABCDEFGHIJKLMNOPQRST", 4))

class Codec:
    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.urls) - 1)

    def decode(self, shortUrl):
        return int(shortUrl.split('/')[-1])
		
		
# code = Codec()
# url = "https://leetcode.com/problems/design-tinyurl"
# print(code.decode(code.encode(url)))
# print(code.urls)

findNums = [4,1,2]
nums = [1,3,4,2]
d = {}
st = []
ans = []
        
for x in nums:
    while len(st) and st[-1] < x:
        d[st.pop()] = x
    print(st.append(x))

for x in findNums:
    ans.append(d.get(x, -1))
            
            		
print(ans)

