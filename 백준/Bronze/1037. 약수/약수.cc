#include <iostream>
using namespace std;

int main(){
    int n;
    int min = 10000000;
    int max = 0;
    cin >> n;
    int *p;
    p = new int [n];
    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
    }
    for (int i = 0; i < n; i++)
    {
        if(p[i] < min) min = p[i];
        if(p[i] > max) max = p[i];
    }
    cout << min * max << endl;
    
}