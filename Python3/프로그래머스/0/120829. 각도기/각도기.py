# solution=lambda r: 1 if 0<r<90 else 2 if r==90 else 3 if 90<r<180 else 4
solution=lambda r: 1 + (r==90) + 2*(90<r<180) + 3*(r==180)