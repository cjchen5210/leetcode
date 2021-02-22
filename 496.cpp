#include <iostream>
#include <vector>
using namespace std;
vector<int> add(int a, int b){
	vector<int> sum;
	sum.push_back(a);
	sum.push_back(b);
	for (int i = 0; i < sum.size(); ++i)
	{
		/* code */
		cout << sum[i] << endl;
	}
	return sum;
}

int main(){

	cout << add(10,9);
	return 0;	
}

