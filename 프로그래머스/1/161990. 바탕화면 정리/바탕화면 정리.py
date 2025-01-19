def solution(wallpaper):
    return [next(i for i,r in enumerate(wallpaper) if "#" in r),
            next(i for i,r in enumerate(zip(*wallpaper)) if "#" in r),
            next(len(wallpaper)-i for i,r in enumerate(wallpaper[::-1]) if "#" in r),
            next(len(wallpaper[0])-i for i,r in enumerate(list(zip(*wallpaper))[::-1]) if "#" in r)]