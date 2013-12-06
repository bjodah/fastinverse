// 

const int ndpp = ${order+1}; // number of data per point
const double y_space = (${ylim[1]} - ${ylim[0]})/(${lookup_N}-1.0);
const double y_span = ${ylim[1]} - ${ylim[0]};
const int lookup_N = ${lookup_N};
// lookup_x is [x(y0), dxdy(y0), d2xdy2(y0), ..., 
//     dZdxdyZ(y0), ..., x(yN), dxdy(yN), d2xdy2(yN), ..., dZxdyZ(yN)]
// where Z is (order+1)/2, where order is the order of the polynomial
<%def name="row_format(i)">\
  ${', '.join(map('{0:.17e}'.format, lookup_x[(order+1)*i:(order+1)*(i+1)]))},
</%def>
<%def name="rows()">
${''.join([row_format(i) for i in range(lookup_N)])}\
</%def>

const double lookup_x[${lookup_N*(order+1)}] = {${rows()}};// for equidistant y [ylim[0] ... ylim[1]], 

static double approx_x(double y){
  // Polynomial interpolation between lookup points
  int idx = ${lookup_N-1}*((y${"{0:+23.17e}".format(-ylim[0])})/y_span);
  int tbl_offset = ndpp*idx;
  double localy = y-y_space*idx;
  // lookup_x[tbl_offset+i]
  return ${' + \ \n    '.join(fit_expr.split(' + '))}; 
}
