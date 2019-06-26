
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
     S T A T I S T I C A L  T E S T  F U N C T I O N  P R O T O T Y P E S 
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

#include "defs.h"

double	Frequency(int n, BitSequence const *);
double	BlockFrequency(int M, int n, BitSequence const *);
double	CumulativeSums(int n, BitSequence const *);
double	Runs(int n, BitSequence const *);
double	LongestRunOfOnes(int n, BitSequence const *);
double	Rank(int n, BitSequence const *);
double	DiscreteFourierTransform(int n, BitSequence const *);
double	NonOverlappingTemplateMatchings(int m, int n, BitSequence const *);
double	OverlappingTemplateMatchings(int m, int n, BitSequence const *);
double	Universal(int n, BitSequence const *);
double 	ApproximateEntropy(int m, int n, BitSequence const *);
double	RandomExcursions(int n, BitSequence const *);
double	RandomExcursionsVariant(int n, BitSequence const *);
double	LinearComplexity(int M, int n, BitSequence const *);
double	Serial(int m, int n, BitSequence const *);
