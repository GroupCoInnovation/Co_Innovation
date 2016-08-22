# include <iostream>
# include <cmath>
# include <string>
# include <cstring>
using namespace std;

class Stock {
	private:
		string company;
		long shares;
		double share_val;
		double total_val;
		void set_tot() {
			total_val = shares * share_val;
		}
	public:
		Stock(string company_, long shares_, double share_val_);
		Stock(string company_);
		Stock();
		~Stock();
		double add(Stock & s);
		void changeShare();
};


Stock::Stock(string company_, long shares_, double share_val_) {
	company    = company_;
	shares     = shares_;
	share_val = share_val_;
	set_tot();
}

Stock::Stock(string company_){
	company    = company_;
	shares     = 0;
	share_val = 0;
	set_tot();	
}

Stock::Stock() {
}

Stock::~Stock() {
}

double Stock::add(Stock & s){
	double sum = 0;
	sum = s.total_val + this->total_val;
	return sum;
}

void Stock::changeShare(){
	this->shares ++;
}

void fun(){
	cout <<"123\n";
}

void fun(double a){
	cout << a << endl;
}
int main() {
	Stock test01("Apple",123,1);
	Stock test02("Apple",123,12);
	Stock test03("Google");
	cout << test01.add(test02) << endl;	
}


