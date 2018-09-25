# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:28:42 2018

@author: AlexWang
"""
#%%
for i in range (2016,2018):
    for j in range (1,13):
        if j < 10:
            filename = str(i) + '-' + '0' + str(j)
        else:
            filename = str(i) + '-' + str(j)
            
        print(filename)
        infilename = filename + '.csv'
        with open (infilename, "r") as infile:
            my_dic = {}
            infile.readline()
            infile.readline()
            infile.readline()
            infile.readline()
            for line in infile:
                #print(line)
                new_l = []
                line_l = line.split(',')
                
                #print(line_l)
                new_l.extend((line_l[1], line_l[2], line_l[5],line_l[6],
                              line_l[7],line_l[8], line_l[9], line_l[10], line_l[11], line_l[12], line_l[16])) 
                
                if line_l[0] in my_dic:
                    my_dic[line_l[0]].append(new_l[-1])
                else:
                    my_dic[line_l[0]] = new_l
        #        
                #print(new_l)
        
        #for key, value in my_dic.items():
           # print('\t'.join(value))
        
        #print(my_dic)  
        outfilename = filename + '.txt'
        with open(outfilename, 'w') as outfile:
            for key, value in my_dic.items():
                
                out = '\t'.join(value) 
                out = key + '\t' + out + '\t' + filename + '\n' 
                outfile.write(out)
      
