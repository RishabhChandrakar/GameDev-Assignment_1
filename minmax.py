def minimax(depth,nodeindex,player,vlist):
        //print(nodeindex)
        if depth==0:
            return vlist[nodeindex]

        if player:
                
            vlist[nodeindex]=max(minimax(depth-1,2*nodeindex+1,not player,vlist),minimax(depth-1,2*nodeindex+2,not player,vlist))
            return vlist[nodeindex] 
        else:
            vlist[nodeindex]=min(minimax(depth-1,2*nodeindex+1,not player,vlist),minimax(depth-1,2*nodeindex+2,not player,vlist))
            return vlist[nodeindex]
    
vlist=[0,0,0,0,0,0,0,3,5,2,9,12,5,23,23]

minimax(3,0,True,vlist)

print(vlist)
