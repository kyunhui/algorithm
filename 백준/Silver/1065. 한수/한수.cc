#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    if(n < 100){
        cout << n << endl;
    }else{
        int a, b, c;
        int cnt = 99;
        for (int i = 100; i <= n; i++)
        {
            a = i % 10;
            b = (i / 10)%10;
            c = i / 100;
            if((b-a) == (c-b)){
                cnt++;
            } 
        }
        cout << cnt << endl;
        
    }
}