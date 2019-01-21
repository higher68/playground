try:    
    raise ZeroDivisionError('ゼロによる除算') 
except ZeroDivisionError as eee:
    print('eee:',eee)
    raise
