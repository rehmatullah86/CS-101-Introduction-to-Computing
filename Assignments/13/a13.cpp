#include 
#include 
using namespace std;

string to_stringx(const int& n); 
void str2inta(string s, int x[], int size);
string inta2str(int x[], int size);


void array_sum(int a[], int b[], int c[], int size) {
  //////// START OF MARKER for array_sum code
    int sum,carry,rem;
    carry = 0;
    
	for (int i = 0; i < size; i++)  {
    
    	sum = a[i] + b[i] + carry;
    	rem = sum % 10;
    	
		if (sum == 10)  { 
      		rem = sum % 10;
      		c[i] = rem;
      		carry = sum / 10;
    	}

    
    	else if (sum > 10)  {
      		rem = sum % 10;
      		c[i] = rem;
      		carry = sum / 10;
    	}
    	
		else  {
      		carry = sum / 10;
      		c[i] = rem + carry;
      		carry = 0;
    	}
      
    } 

  //////// END OF MARKER 

  return;
}






//////// HELPER FUNCTION
int main_test() {
    int a[100], b[100], c[100];
    str2inta("83758574635364537465746355928476867", a, 100);
    str2inta("83758574635364537465746355928476867", b, 100);
    array_sum(a, b, c, 100);
    cout <<  inta2str(c, 100) << endl;
    return 0;
}

///////////// DO NOT MODIFY CODE BEYOND THIS LINE /////////////


/// !!! FOR SUCCESSFULL SUBMISSION, THE FOLLOWING NEEDS TO BE THE main FUNCTION
int main(int argc, char* argv[]) {
    int a[100], b[100], c[100];
    str2inta(argv[1], a, 100);
    str2inta(argv[2], b, 100);
    array_sum(a, b, c, 100);
    cout <<  inta2str(c, 100) << endl;
    return 0;
}


// OTHER HELPER FUNCTIONS
void str2inta(string s, int x[], int size) {
  int max_idx = s.length() - 1;
  for (int i=0; i < size; i++)
    x[i] = 0;
  for (int i=0; i < s.length(); i++)
    x[max_idx--] = s[i] - '0';
}
string inta2str(int x[], int size) {
  string val = "";
  for (int i=size-1; i >= 0; i--)
    val = val + to_stringx(x[i]);
  val = val.erase(0, val.find_first_not_of('0'));
  return val.length() > 0 ? val : "0";
}
string to_stringx(const int &n) { 
  std::ostringstream stm ;
  stm << n ;
  return stm.str() ;
}
