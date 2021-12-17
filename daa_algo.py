
def MSS(A,q,r):
    i = q
    istar = q
    jstar = q
    max = 0
    S = [0]*(len(A)+1)
    S[q] = 0  

    for j in range (q+1,r+1) :
        x = A[j-1] + S[j-1]
        if(x<0):
            S[j] = 0
            i = j
        else:
            S[j] = x
            if( x > max ):
                max = x 
                jstar = j
                istar = i
    
    
    print("max : ", max)
    return istar,jstar,S

def MLS(A,q,r):
    print("A dalam MLS : ", A)
    i = q
    istar = q
    jstar = q
    max = 0
    S = [0]*(len(A)+1)
    S[q] = 0  

    for j in range (q+1,r+1) :
        x = A[j-1] + S[j-1]
        if(x<0):
            S[j] = 0
            i = j
        else:
            S[j] = x
            if( x > max ):
                max = x 
                jstar = j
                istar = i

    return max

def Summarize(A,q,r):
    n = len(A)
    istar,jstar,S = MSS(input,q,r)
    b=0
    for j in range (q+1,r+1) :
        # print("j : ", j)
        b = max( 0, A[r-j+q] + b )
        # print("r-j+q : ", r-j+q)
        # print("A[r-j+q] : ",A[r-j+q])
        # print("b : ",b)
        # print("S[r-j+q] : ",S[r-j+q])
        S[r-j+q] = S[r-j+q] + b
        # print("S[r-j+q] + b : ",S[r-j+q])
        # print("---------------------------------------")

    print("S 1-5 summarize : ", S)

    S[istar] = MLS(A,q,istar)
    f = A[istar]
    for j in range(istar + 1,jstar):
        S[j] = max(f,S[j-1])
        f = f + A[j]

    print("S 6-10 summarize : ", S)

    bbesar = MLS(A[::-1],n-r,n-jstar)
    b = A[jstar-1]
    S[jstar-1] = max(S[jstar-1],b,bbesar)
    for i in range(istar + 2, jstar+1):
        b = b + A[jstar-i+istar]
        bbesar = max(b,bbesar)
        S[jstar-i+istar] = max( S[jstar-i+istar],bbesar)

    return S


input = [-15,28,-7,36,-4]
q=0
r=len(input)

istar,jstar,S = MSS(input,q,r)

print("istar : " , istar)
print("jstar : " , jstar)
print("S :" , S)

Ssum = Summarize(input,q,r)

print("S summarize : ", Ssum)
print("A :" , input)
