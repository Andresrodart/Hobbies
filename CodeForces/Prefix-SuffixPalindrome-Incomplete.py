def isPal(string):
    length = len(string)
    for i in range( length ):
        if(string[i] != string[length - i - 1]): return False
    return True

if __name__ == "__main__":
    cases = int(input())
    while cases != 0:
        string = input()
        a,b = [], []
        p1, p2 = 0, len(string) - 1
        while p1 < p2 :
            if string[p1] == string[p2]:
                a.append(string[p1])
                b.insert(0, string[p2])
                p1 += 1
                p2 -= 1
            else: break 

        if p1 >= p2: 
            print(string)
            continue
        else:
            string2 = string[p1 : p2 - p1 + 1]
            string3, string4 = '', ''
            for i in range(len(string2)):
                if isPal(string2[0 : i + 1]): string3 = string2[0 : i + 1]
                if string4 == "" and isPal(string2[i : ]) : string4 = string2[i]
 
            if(s3.length()>s4.length())cout<<a<<s3<<b<<endl;
            else cout<<a<<s4<<b<<endl;
 
 
 
        }
 
 
 
 
    }
 
 
 
 
}
 