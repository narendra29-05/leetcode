class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        if len(v1)<len(v2):
            v1=v1+["0"]*(len(v2)-len(v1))
        if len(v1)>len(v2):
            v2=v2+["0"]*(len(v1)-len(v2))
        print(v1,v2)
        for i in range(len(v1)):
            first=v1[i]
            second=v2[i]
            while first and first[0]=="0":
                first=first[1:]
            while second and second[0]=="0":
                second=second[1:]
            f1=int(first) if first else 0
            s1=int(second) if second else 0
            print(f1,s1)
            if f1<s1:
                return -1
            if f1>s1:
                return 1
        return 0