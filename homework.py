import sys
import random
if __name__=="__main__":
    if len(sys.argv)>2:
        v1 = list(sys.argv[2])
        v2 = list(sys.argv[2])
        random.seed(int(sys.argv[1]))
        random.shuffle(v2)
        print("".join(v2))

        x = []
        for i in range(len(v1)):
            for j in range(len(v1)):
                if(v1[i]==v2[j]):
                    x.append(v2[j])
                    break
        print("".join(x))
