#include <iostream>
using namespace std;

int main(){
    int n;
    int temp = 0;
    int cnt = 1;
    cin >> n;
    for (int i = 0; i < 1+(n-1)*4; i++)
    {
        if (i == 0 || i == (n-1)*4){
            for (int j = 0; j < (1+(n-1)*4)/2+1; j++)
            {
                cout << "*";
            }
            for (int j = (1+(n-1)*4)/2+1; j < 1+(n-1)*4; j++)
            {
                cout << "*";
            }
            
            cout << endl;
        }
        else if(i == (1+(n-1)*4)/2){
            for (int j = 0; j < (1+(n-1)*4)/2+1; j++)
            {
                if(j == (1+(n-1)*4)/2){
                    cout << "*";
                }else{
                    cout << "*" << " ";
                }
            }
            cout << endl;
        }
        else if(i%2 == 1){
            if(i < (1+(n-1)*4)/2){
                for (int j = 0; j < i/2+1; j++)
                {
                    cout << "*" << " ";
                }
                for (int j = 0; j <(1+(n-1)*4)-cnt*4; j++)
                {
                    cout << " ";
                }
                for (int j = 0; j < i/2+1; j++)
                {
                    cout << " " << "*";
                }
                cout << endl;
            }
            else  {
                for (int j = 0; j < ((1+(n-1)*4)-i)/2; j++)
                {
                    cout << "*" << " ";
                }
                for (int j = 0; j <(1+(n-1)*4)-cnt*4; j++)
                {
                    cout << " ";
                }
                cnt--;
                for (int j = 0; j < ((1+(n-1)*4)-i)/2; j++)
                {
                    cout << " " << "*";
                }
                cout << endl;
            }
        }
        else if(i%2 == 0){
            if(i < (1+(n-1)*4)/2){
                for (int j = 0; j < (i-1)/2+1; j++)
                {
                    cout << "*" << " ";
                }
                for (int j = 0; j <(1+(n-1)*4)-cnt*4; j++)
                {
                    cout << "*";
                }
                for (int j = 0; j < (i-1)/2+1; j++)
                {
                    cout << " " << "*";
                }
                cout << endl;
                cnt++;
            }
            else{
                for (int j = 0; j < ((1+(n-1)*4)-i)/2; j++)
                {
                    cout << "*" << " ";
                }
                for (int j = 0; j <(1+(n-1)*4)-cnt*4; j++)
                {
                    cout << "*";
                }
                for (int j = 0; j < ((1+(n-1)*4)-i)/2; j++)
                {
                    cout << " " << "*";
                }
                cout << endl;
            }
        }
    }
}

    
