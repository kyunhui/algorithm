#include <iostream>
#include <deque>
using namespace std;

int main(){
    deque<int> dq;
    dq.push_front(0);
    dq.push_front(1);

    int num, temp, sum;
    cin >> num;

    for (int i = 0; i < num; i++)
    {
        temp = dq.back();
        dq.pop_back();
        sum = dq.back() + temp;
        dq.push_back(temp);
        dq.push_back(sum);
    }
    
    cout << dq.back() << endl;
}