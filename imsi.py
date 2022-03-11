    """
            for s in list2:
                print(s)
                dict3=os.path.isdir(s)
                if dict3==True:
                    os.chdir(dict+"\\"+i+'\\'+s)
                    list3=os.listdir(dict+"\\"+i+'\\'+s)
                    for x in list3:
                        print(x)
                        dict4=os.path.isdir(x)
                        if dict4==True:
                            os.chdir(dict+"\\"+i+'\\'+s+"\\"+x)
                            list4=os.listdir(dict+"\\"+i+'\\'+s+"\\"+x)

"""