def expanded_form(num):
    results = []
    
    for id, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            results.append(digit + ('0' * id))
            
    return ' + '.join(results[::-1])

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'