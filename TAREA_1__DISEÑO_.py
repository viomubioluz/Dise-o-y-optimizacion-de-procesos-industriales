from numpy import matrix, zeros

def gauss(A,b):
	Ab = zeros((len(A),len(A)+1))
	for i in range(len(A)):
		Ab[i,0:len(A)] =A[i][:]
		Ab[i,-1]  =b[i]

	def equiv(Mat, fila):
		F = Mat[fila]/float(Mat[fila,fila])
		m = Mat.tolist()
		m.pop(fila)
		m = matrix(m)
		for i in range(len(m)):
			m[i] = F*(-m[i,fila])+m[i]
		m = m.tolist()
		m.insert(fila,F.tolist())
		M = zeros(Mat.shape)
		for i in range(len(m)):
			M[i] = m[i]
		return M

	for i in range(len(A)):
		A_eq = equiv(Ab, i)
		Ab = A_eq
	return Ab[:,len(A)] 

Mat_A = [[-2,1,2,2,3,2,3,1],
		 [0,1,1,0,0,0,0,0],
		 [0,-9,1,0,0,0,0,0],
		 [0,0,0,1,1,0,0,0],
		 [0,0,0,1,-0.3,0,0,0],
		 [0,0,0,0,0,1,1,0],
		 [0,0,0,0,0,1,-0.1,0],
		 [0,0,0,0,0,0,0,2]]

Mat_b = [0.9,1,0,0.8,0,0.2,0,0.1]

print "x=", gauss(Mat_A, Mat_b)

