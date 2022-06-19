hundred = 'hundred'
band = 'and'

words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['a', 'b', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def solve():
    ans = 0
    for i in range(1000):
        s = ''
        n = i
        if n // 100 > 0:
            s += words[n//100]
            s += hundred
            ans += len(words[n // 100])
            ans += len(hundred)
            if n % 100 != 0:
                ans += len(band)
                s += band
        n = n % 100
        if n >= 20:
            s += tens[n//10]
            ans += len(tens[n // 10])
            n = n % 10

        if n > 0:
            s += words[n]
            ans += len(words[n])
        #print(s)
    return ans

if __name__ == '__main__':
    ans = solve()
    ans += len('onethousand')
    print(ans)
