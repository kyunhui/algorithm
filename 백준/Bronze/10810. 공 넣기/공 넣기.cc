#include <iostream>
using namespace std;

int main(){
    int n, m, a, b, c;
    cin >> n >> m;
    int arr[100]= {0};
    for (int i = 0; i < m; i++)
    {
        cin >> a >> b >> c;
        for (int i = a-1; i <= b-1; i++)
        {
            arr[i] = c;
        }
        
    }
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    
}