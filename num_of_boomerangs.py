class Sol:
    def num_of_boomerangs(self,list):
        d2ij=[]
        d2ik=[]
        result=0
        for x in range(len(list)):
            i=list[x]
            for y in range(len(list)):
                if x<y:
                    j=list[y]
                    d2=(i[0]-j[0])**2+(i[1]-j[1])**2
                    d2ij.append(d2)
        for x in range(len(list)):
            i=list[x]
            for y in range(len(list)):
                if x<y:
                    k=list[y]
                    d2=(i[0]-k[0])**2+(i[1]-k[1])**2
                    d2ik.append(d2)
        for x in range(len(d2ij)):
            for y in range(len(d2ik)):
                if x < y and d2ik[x]==d2ij[y]:
                    result+=1
        return 2*result

if __name__ == '__main__':
    p1=Sol()
    print(p1.num_of_boomerangs([[0,0],[1,0],[2,0],[1,1]]))
