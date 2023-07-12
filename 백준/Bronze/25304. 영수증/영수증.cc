#include <iostream>
using namespace std;
int main(){
    int sum, price, n, cnt;
    cin >> sum >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> price >> cnt;
        sum -= price * cnt;
    }
    if (sum == 0) cout << "Yes";
    else cout << "No";
}