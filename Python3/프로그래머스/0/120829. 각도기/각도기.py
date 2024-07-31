solution=lambda r:1 if 0<r<90 else (2 if r==90 else (3 if 90<r<180 else (4 if r==180 else None)))
# solution=lambda r:1 if 0<r<90 elif (2 if r==90 elif (3 if 90<r<180 elif (4 if r==180)))
# else가 elif거나 else None을 생략하면 syntex?에러 발생