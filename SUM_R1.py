
def sum(a:int, b:int) -> int:
    if not (0 <= a <=100 and 0 <= b <=100):
        raise ValueError('Numbers not in range')
    
    return a+b
    