import ast

def myFunc(arg):
    
    l = arg.split()
    l_cnv_flt = []
    l_cnv_int = []

    mean = 0.0
    maxFlt = 0.0

    for i in l:
        
        if not i.isdigit():
            try:
                float(i)
            except:
                print('ERROR: String "'+ i + '" is not a number!')
                return (mean, maxFlt)
        
        l_cnv_flt.append(float(i)) if '.' in i or 'e' in i.lower() else l_cnv_int.append(int(i)) 
    

    if len(l_cnv_int) == 0 and len(l_cnv_flt) == 0:
        print("ERROR: you entered empty string")
        return (mean, maxFlt)

    
    # get mean of even integers
    if len(l_cnv_int) != 0:
        even_nums = list(filter(lambda x: x%2 == 0, l_cnv_int))
        try:
            mean = (sum(even_nums) / len(even_nums))
            print("Mean of even integers is: "+ str(mean) )
        except:
            print("no even integers entered")
    
    # get max float number
    maxFlt = 0
    if len(l_cnv_flt) == 0:
        print("no floats entered")  
    else :
        maxFlt = max(l_cnv_flt)
        print("Max of float numbers is: "  + str(maxFlt))
    
    return mean, maxFlt
