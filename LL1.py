def Select_file_in(file_path):
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

def printstack(stack):
    str = ''
    for i in stack:
        str += i
    return str

def printstr(string,location):
    str = ''
    for i in range(location,len(string),1):
        str += string[i]
    return str

def LL1_Match(Select,string):
    #初始化栈
    stack = []
    #初始化字符串指针
    location = 0
    #将字符串中第一个#号压入栈中
    stack.append('#')
    #将开始符号压入栈中
    stack.append(Select["Start_Symbol"])
    #初始化当前字符
    a = string[location]
    #标志位 
    flag = False
    #步数
    count = 1

    '''
    在判断过程中
    x始终为栈顶第一个元素
    a始终为符号串的第一个元素
    由于上方已输出一次状态
    因此下方直接跳过count==1
    '''

    while True:

        if len(stack) != 0:                     #若栈空，则退出判断
            #x = stack.pop()
            x = stack[len(stack)-1]
        else:
            break

        if (x,a) in Select.keys():
            s = Select[(x,a)]
            print('%d\t\t%s\t\t%s\t\t%s-->%s'%(count,printstack(stack),printstr(string,location),x,s))
            stack.pop();
            for i in range(len(s)-1,-1,-1):     #创建用于反向遍历的列表
                if s[i] != 'e':                 #如果是空，则不入栈
                    stack.append(s[i])  

        elif x == '#' and a == '#':
            flag = True
            print('%d\t\t%s\t\t%s\t\t%s'%(count,printstack(stack),printstr(string,location),"'"+x+"'已被识别，匹配成功！"))
            break

        elif x == string[location]:
            print('%d\t\t%s\t\t%s\t\t%s'%(count,printstack(stack),printstr(string,location),"'"+x+"'已被识别"))
            location += 1
            a = string[location]
            stack.pop();

        else:
            break

        count += 1

    return flag

def main():
    '''
    Select = {
        "Start_Symbol":'E',
        ('E','i'):'TH',
        ('E','('):'TH',
        ('H','+'):'+TH',
        ('H',')'):'e',
        ('H','#'):'e',
        ('T','i'):'FY',
        ('T','('):'FY',
        ('Y','+'):'e',
        ('Y','*'):'*FY',
        ('Y',')'):'e',
        ('Y','#'):'e',
        ('F','i'):'i',
        ('F','('):'(E)',
    }
    

    Select = {
        "Start_Symbol":'S',
        ('S','a'):'aA',
        ('S','d'):'d',
        ('A','b'):'bAS',
        ('A','a'):'e',
        ('A','d'):'e',
        ('A','#'):'e',
    }
    '''

    

    print("步骤\t\t符号栈\t\t剩余串\t\t产生式")

    if LL1_Match(Select_file_in('/Users/weilai/Compiler/Select2.txt'),String_file_in('/Users/weilai/Compiler/LString2.txt')+'#'):
        print("\nIs Match!\n")
    else:
        print("\nNot Match!\n")

main() 