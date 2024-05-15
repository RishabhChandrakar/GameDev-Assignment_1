def findpos(slist,plist,search_number,rank):

    if(rank>len(slist)):
        return 0
    for num in range(len(slist)):
        if slist[num]==search_number:
            plist[num]=rank
            print(plist[num])
            break
    #print(num , rank)
    
    
    findpos(slist,plist,num+1,rank+1)


slist=[8,1,2,-1,3,4,5,6]
plist=[0,]

for n in range(len(slist)-1):
    plist.append(0)

findpos(slist,plist,-1,1)


print(plist)
