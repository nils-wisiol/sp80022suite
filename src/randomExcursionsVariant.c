#include <stdio.h> 
#include <math.h> 
#include <string.h>
#include <stdlib.h>
#include "../include/defs.h"
#include "../include/cephes.h"

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            R A N D O M  E X C U R S I O N S  V A R I A N T  T E S T
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

double
RandomExcursionsVariant(int n, BitSequence const *epsilon)
{
	int		i, p, J, x, constraint, count, *S_k;
	int		stateX[18] = { -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	double	p_value;
	
	if ( (S_k = (int *)calloc(n, sizeof(int))) == NULL ) {
		return -1;
	}
	J = 0;
	S_k[0] = 2*(int)epsilon[0] - 1;
	for ( i=1; i<n; i++ ) {
		S_k[i] = S_k[i-1] + 2*epsilon[i] - 1;
		if ( S_k[i] == 0 )
			J++;
	}
	if ( S_k[n-1] != 0 )
		J++;

	constraint = (int)MAX(0.005*pow(n, 0.5), 500);
	if (J < constraint) {
        free(S_k);
	    return -3;
	}
	else {
	    p_value = 1;
		for ( p=0; p<=17; p++ ) {
			x = stateX[p];
			count = 0;
			for ( i=0; i<n; i++ )
				if ( S_k[i] == x )
					count++;
			p_value = fmin(p_value, erfc(fabs(count-J)/(sqrt(2.0*J*(4.0*fabs(x)-2)))));
        }
        free(S_k);
        return p_value;
	}
}
