solution=lambda lst:n if int(n := "".join(sorted(map(str, lst), key=lambda x: x*3, reverse=True))) else "0"