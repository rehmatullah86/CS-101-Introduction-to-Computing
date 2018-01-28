#include 
#include  
using namespace std;


//////// START OF MARKER FOR fib
long long fib(long long x){
	if (x <= 1){
		return x;
	}
	if (x > 1){
		long long z;
		long long y;
		z = 0;
		y = 1;

		for (int i = 0;i < x;i++)
		{
			long long n;
			n = z + y;
			z = y;
			y = n;
		}
		
	return z;}
	
		return 0;}



//////// END OF MARKER 



//////// DO NOT MODIFY CODE BEYOND THIS LINE

int main(int argc, char* argv[]) {
    cout << (fib(atoi(argv[1]))) <
