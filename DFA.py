def DFA_file_in(file_path):
    f = open(file_path, 'r')
    result = {}
    i=0

    for line in f.readlines():
        line = line.strip()
        if not len(line):
            continue

        if i==0 :
            index_symbol = line.split(':')
            result[index_symbol[0]] = index_symbol[1][0]
            i +=1
        elif  i < 4:
            index_symbol = line.split(':')
            symbol_value = index_symbol[1].split(',')
            result[index_symbol[0]]=[]
            for char in symbol_value:
                result[index_symbol[0]].append(char)
            i += 1
        else:
            index_symbol = line.split(':')
            result[(index_symbol[0].split(',')[0],index_symbol[0].split(',')[1])]=index_symbol[1]

    f.close()

    return result

def String_file_in(file_path):
    f = open(file_path, 'r')
    str = f.read()
    f.close()
    return str

def DFA_Match(DFA , string):

    Current_State = DFA["Start_Symbol"]

    for char in string:
        if char not in DFA["Terminal_Symbols"] or (Current_State,char) not in DFA.keys():
            Current_State = "No Match!"
            break
        else:
            Current_State = DFA[(Current_State,char)]

    if Current_State in DFA["Final_Symbols"]:
        return True
    else: 
        return False

def main():
    '''
    #(0|1)*01
    DFA = {
        "Nonterminal_Symbols":['A','B','C'], 
        "Terminal_Symbols":['0','1'],
        "Start_Symbol":'A',
        "Final_Symbols":['C'],
        ('A','0'):'B',
        ('A','1'):'A',
        ('B','0'):'B',
        ('B','1'):'C',
        ('C','0'):'B',
        ('C','1'):'A',
    }
    
    

    #倒数第二个为1的01串
    DFA = {
        "Nonterminal_Symbols":['0','1','2','3'], 
        "Terminal_Symbols":['0','1'],
        "Start_Symbol":'0',
        "Final_Symbols":['2','3'],
        ('0','0'):'0',
        ('0','1'):'1',
        ('1','0'):'2',
        ('1','1'):'3',
        ('2','0'):'0',
        ('2','1'):'1',
        ('3','0'):'2',
        ('3','1'):'3',
    }
    print (DFA)
    DFA_file_in('/Users/weilai/Compiler/test.txt')
    '''
    
    if DFA_Match(DFA_file_in('/Users/weilai/Compiler/DFA2.txt'),String_file_in('/Users/weilai/Compiler/DString2.txt')):
        print("\nIs Match!\n")
    else:
        print("\nNot Match!\n")

main()