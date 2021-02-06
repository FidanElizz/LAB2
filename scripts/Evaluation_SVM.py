import numpy as np
import sys
import math

# In SVM class 1=H, 2=E, 3=C
#MCC_matrix
# | H | C | E |
# -------------
#H|   |   |   |
# -------------
#C|   |   |   |
# -------------
#E|   |   |   |
# -------------

def MCC_matrix(test_file,predicted_file):
	with open(test_file,"r")as test,open(predicted_file,"r")as predict:
		test_lines=test.readlines()
		predict_lines=predict.readlines()
		
		MCC_matrix=np.zeros((3,3))
		for linenum in range(len(test_lines)):
			test_line=test_lines[linenum].rstrip()
			test_ss=test_line[0]
			pred_ss=predict_lines[linenum].rstrip()
		
			#print(test_ss,pred_ss)
	
			if test_ss=='1' and pred_ss=='1':
				MCC_matrix[0,0]+=1
			elif test_ss=='1' and pred_ss=='3':
				MCC_matrix[0,1]+=1
			elif test_ss=='1' and pred_ss=='2':
				MCC_matrix[0,2]+=1
			elif test_ss=='3' and pred_ss=='1':
				MCC_matrix[1,0]+=1
			elif test_ss=='3' and pred_ss=='3':
				MCC_matrix[1,1]+=1
			elif test_ss=='3' and pred_ss=='2':
				MCC_matrix[1,2]+=1
			elif test_ss=='2' and pred_ss=='1':
				MCC_matrix[2,0]+=1
			elif test_ss=='2' and pred_ss=='3':
				MCC_matrix[2,1]+=1
			else:
				MCC_matrix[2,2]+=1
	return(MCC_matrix)


#MCC_SS
#      | SS |  NonSS |
# --------------------
#SS    |    |        |
# --------------------
#NonSS |    |        |
# --------------------													

def H_eval(MCC_matrix):
	MCC_H=np.zeros((2,2))
	
	MCC_H[0,0]=MCC_matrix[0,0]
	MCC_H[0,1]=MCC_matrix[0,1]+MCC_matrix[0,2]
	MCC_H[1,0]=MCC_matrix[1,0]+MCC_matrix[2,0]
	MCC_H[1,1]=MCC_matrix[1,1]+MCC_matrix[1,2]+MCC_matrix[2,1]+MCC_matrix[2,2]
	MCCh=(MCC_H[0,0]*MCC_H[1,1]-MCC_H[1,0]*MCC_H[0,1])/(math.sqrt((MCC_H[0,0]+MCC_H[1,0])*(MCC_H[0,0]+MCC_H[0,1])*(MCC_H[1,1]+MCC_H[1,0])*(MCC_H[1,1]+MCC_H[0,1])))
	Senh=MCC_H[0,0]/(MCC_H[0,0]+MCC_H[0,1])
	PPVh=MCC_H[0,0]/(MCC_H[0,0]+MCC_H[1,0])
	ACCh=(MCC_H[0,0]+MCC_H[1,1])/(np.sum(MCC_H[0,0]+MCC_H[0,1]+MCC_H[1,0]+MCC_H[1,1]))
	return(MCCh,Senh,PPVh,ACCh)
	
def C_eval(MCC_matrix):
	MCC_C=np.zeros((2,2))
	
	MCC_C[0,0]=MCC_matrix[1,1]
	MCC_C[0,1]=MCC_matrix[1,0]+MCC_matrix[1,2]
	MCC_C[1,0]=MCC_matrix[0,1]+MCC_matrix[2,1]
	MCC_C[1,1]=MCC_matrix[0,0]+MCC_matrix[0,2]+MCC_matrix[2,0]+MCC_matrix[2,2]
	MCCc=(MCC_C[0,0]*MCC_C[1,1]-MCC_C[1,0]*MCC_C[0,1])/(math.sqrt((MCC_C[0,0]+MCC_C[1,0])*(MCC_C[0,0]+MCC_C[0,1])*(MCC_C[1,1]+MCC_C[1,0])*(MCC_C[1,1]+MCC_C[0,1])))	
	Senc=MCC_C[0,0]/(MCC_C[0,0]+MCC_C[0,1])
	PPVc=MCC_C[0,0]/(MCC_C[0,0]+MCC_C[1,0])
	ACCc=(MCC_C[0,0]+MCC_C[1,1])/(np.sum(MCC_C[0,0]+MCC_C[0,1]+MCC_C[1,0]+MCC_C[1,1]))
	return(MCCc,Senc,PPVc,ACCc)

def E_eval(MCC_matrix):
	MCC_E=np.zeros((2,2))
	
	MCC_E[0,0]=MCC_matrix[2,2]
	MCC_E[0,1]=MCC_matrix[2,0]+MCC_matrix[2,1]
	MCC_E[1,0]=MCC_matrix[0,2]+MCC_matrix[1,2]
	MCC_E[1,1]=MCC_matrix[0,0]+MCC_matrix[0,1]+MCC_matrix[1,0]+MCC_matrix[1,1]
	MCCe=(MCC_E[0,0]*MCC_E[1,1]-MCC_E[1,0]*MCC_E[0,1])/(math.sqrt((MCC_E[0,0]+MCC_E[1,0])*(MCC_E[0,0]+MCC_E[0,1])*(MCC_E[1,1]+MCC_E[1,0])*(MCC_E[1,1]+MCC_E[0,1])))
	Sene=MCC_E[0,0]/(MCC_E[0,0]+MCC_E[0,1])
	PPVe=MCC_E[0,0]/(MCC_E[0,0]+MCC_E[1,0])
	ACCe=(MCC_E[0,0]+MCC_E[1,1])/(np.sum(MCC_E[0,0]+MCC_E[0,1]+MCC_E[1,0]+MCC_E[1,1]))
	return(MCCe,Sene,PPVe,ACCe)

def Q3(MCC_matrix):
	Q3=(MCC_matrix[0,0]+MCC_matrix[1,1]+MCC_matrix[2,2])/(np.sum(MCC_matrix))
	return(Q3)


if __name__=='__main__':
	test_file=sys.argv[1]
	predicted_file=sys.argv[2]
	MCC_mat=MCC_matrix(test_file,predicted_file)
	

	print('MCC:',(H_eval(MCC_mat)[0]+C_eval(MCC_mat)[0]+E_eval(MCC_mat)[0])/3)
	print('ACC:',(H_eval(MCC_mat)[3]+C_eval(MCC_mat)[3]+E_eval(MCC_mat)[3])/3*100,'%')
	print('Q3:', Q3(MCC_mat))

