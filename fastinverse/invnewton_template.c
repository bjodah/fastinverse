// ${_warning_in_the_generated_file_not_to_edit}
<%doc>
  // mako template of C99 source
  // Lightning fast newton iteration for finding inverse of a function
  // variables:
  //     y_lo, y_hi, x_lo, x_hi, lookup_N, lookup_x, lookup_poly,
  //     poly_expr, order, cses, y_in_cse, dydx_in_cse
</%doc>

#include <math.h>
#include "invnewton.h"

static inline double dabs(const double x){return x > 0 ? x : -x;}


// include a definition of "static double approx_x(double y)"
#include "approx_x_${approxmeth}.c"

int c_invnewton(double y, double * const restrict xout, double abstol_y, 
		double abstol_x, int iabstol, int itermax, int save_conv, 
		double * const restrict conv_dx)
{
  // iabstol: 0 => abstol_y, 1 => abstol_x, 2 => abstol_y & abstol_x
  // if save_conv == 1; ensure sizeof(conv_dx) >= sizeof(double)*itermax
  // returns -1 if itermax reached, elsewise number of iterations
  double x = approx_x(y);
  int i=0;
  %for token, expr in cses:
  double ${token} = ${expr};
  %endfor
  double dy = ${y_in_cse}-y;
  double dx = -dy/(${dydx_in_cse});

  for(;;){ // infite loop
    x += dx;
    %for token, expr in cses:
    ${token} = ${expr};
    %endfor
    dy = ${y_in_cse}-y;
    if(save_conv)
      conv_dx[i] = dx;
    switch(iabstol){
    case (0):
      if (dabs(dy) < abstol_y) goto exit_loop;
      break;
    case (1):
      if (dabs(dx) < abstol_x) goto exit_loop;
      break;
    case (2):
      if ((dabs(dy) < abstol_y) && (dabs(dx) < abstol_x)) goto exit_loop;
      break;
    }
    i++;
    if (i >= itermax) return -1;
    dx = -dy/(${dydx_in_cse});
  }
 exit_loop: // double break not possible
  *xout = x;
  return i+1;
}

int c_invnewton_arr(int ny, const double * const restrict y, double * const restrict x, 
		    double abstol_y, double abstol_x, int iabstol, int itermax)
{
  // Returns -1 on successful exit
  // Returns index of a failing c_invnewton call (OpenMP)
  int status = -1;
  #pragma omp parallel for if (ny > ${NY_MIN_OMP_BREAKEVEN})
  for (int i=0; i<ny; ++i){
    int success = c_invnewton(y[i], &x[i], abstol_y, abstol_x, iabstol, itermax, 0, NULL);
    if(success == -1)
      status = i;
  }
  return status;
}
