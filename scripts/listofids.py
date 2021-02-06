#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

for file in os.listdir("/Users/fidanqurbanova/Downloads/LAB2_project/seqprofile_BTS"):
    pdbID = file[:-4]
    Pssm = open("/Users/fidanqurbanova/Downloads/LAB2_project/idlist_bts.txt" ,"a")
    Pssm.write(pdbID + "txt")
    Pssm.write("\n")
    
        
        
