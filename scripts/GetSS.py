#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import os

def Readsome():
    Dic = { "H": "H", "G": "H", "I": "H", "B": "E", "E": "E", "T": "C", "S": "C", " ": "C"}
    
    for file in os.listdir("/Users/fidanqurbanova/Downloads/LAB2_project/dsspBTS/"):
        with open("/Users/fidanqurbanova/Downloads/LAB2_project/dsspBTS/"+file,"r") as fl:
            
        
            pdbID = file[:-5]
            pdbHead = pdbID[:4]
            chain = pdbID[-1:]
            
            
            dssp = open("/Users/fidanqurbanova/Downloads/dssp.formated/"+pdbID +".txt" ,"x")
            fasta = open("/Users/fidanqurbanova/Downloads/chainfasta2/"+pdbID +".fasta" ,"x")
            
            
            dssp.write(">" +pdbHead+":"+chain +"\n")
            fasta.write(">" +pdbHead+":"+chain +"\n")
            lines = fl.readlines()[28:]
            for line in lines:
                line = line.rstrip()
                if line[16] in Dic:
                     dssp.write(Dic[line[16]])
                else:
                    dssp.write("\n" + "Something went wrong")
                    
                    
                if line[13] == "!":
                     fasta.write("X")
                elif line[13] == "!*":
                    fasta.write("\n" + "Something went wrong!")
                else:
                    fasta.write(line[13])
            dssp.close()
            fasta.close()
    
Readsome()
