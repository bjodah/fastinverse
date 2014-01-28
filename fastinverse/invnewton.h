#ifndef _INVNEWTON_H_
#define _INVNEWTON_H_

#ifndef NULL
#define NULL 0
#endif

int c_invnewton(double y, double * const restrict xout, double abstol_y, 
		double abstol_x, int iabstol, int itermax, int save_conv,
		double * const restrict conv_dx);

int c_invnewton_arr(int ny, const double * const restrict y, double * const restrict x, 
		    double abstol_y, double abstol_x, int iabstol, int itermax);

#endif // _INVNEWTON_H_
