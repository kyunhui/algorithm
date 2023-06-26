#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int t;
    cin >> t;
    
    char arr[100][100];
    for (int i = 0; i < t; i++)
    {
        string s;
        cin >> s;
        int len = s.length();
        int con = sqrt(s.length());
        int index = 0;
        for (int i = 0; i < con; i++)
        {
            for (int j = 0; j < con; j++)
            {
                arr[i][j] = (char)s[index++];
            }
            
        }

        for (int i = con-1; i >= 0; i--)
        {
            for (int j = 0; j < con; j++)
            {
                cout << arr[j][i];
            }
            
        }
        cout << endl;
        
        
    }

    
    
    
    
    
}