def ensure_upper(func):
    def upper(*args, **kwargs):
        args = [a.upper() if isinstance(a,str) else a for a in args]
        return(func(*args, **kwargs))
    return upper
