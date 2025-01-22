haystack = ['hay','junk','hay','hay', 'moreJunk','needle','randomJunk']
def findneedle(haystack):
    index = haystack.index('needle')
    if 'needle' in haystack:
        print('found the needle at position ', index)
findneedle(haystack)
#comment
