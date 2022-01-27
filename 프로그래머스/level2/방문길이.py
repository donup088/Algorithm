def solution(dirs):
    road=set()
    cx,cy=0,0
    for d in dirs:        
        if d=='L':
            if -5<=cx-1<=5:
                cx-=1
                road.add((cx+1,cy,cx,cy))            
                road.add((cx,cy,cx+1,cy))        
        if d=='R':
            if -5<=cx+1<=5:
                cx+=1
                road.add((cx-1,cy,cx,cy))            
                road.add((cx,cy,cx-1,cy))        
        if d=='U':
            if -5<=cy+1<=5:
                cy+=1
                road.add((cx,cy-1,cx,cy))        
                road.add((cx,cy,cx,cy-1))        
        if d=='D':
            if -5<=cy-1<=5:
                cy-=1
                road.add((cx,cy+1,cx,cy))      
                road.add((cx,cy,cx,cy+1))        
    
    return len(road) // 2 