def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fff': #u'\u9fa5
        return True
    else:
        return False
        
def is_number(uchar):
    if uchar >= u'\u0030' and uchar<=u'\u0039':
        return True
    else:
        return False

def is_puncuation(uchar):
    puc_list = set(('\u3002','\uFF1F','\uFF01','\uFF0C','\u3001','\uFF1B','\uFF1A','\u300C','\u300D','\u300E','\u300F','\u2018','\u2019','\u201C','\u201D','\uFF08','\uFF09','\u3014','\u3015','\u3010','\u3011','\u2014','\u2026','\u2013','\uFF0E','\u300A','\u300B','\u3008','\u3009','\u002E','\u003A','\u002C','\u0025','\u0040','\u002F','\u005C','\u0022','\u0021','\u0027','\u0023','\u037e'))
    #u002E is english .  003A is : 002C is, 0025 is % 0040 is @ 
    if uchar in puc_list:
        return True
    else:
        return False

def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
        return True
    else:
        return False

def is_legal(uchar):
    if is_chinese(uchar) or is_number(uchar) or is_puncuation(uchar) or is_alphabet(uchar):
        return True
    else:
        return False
