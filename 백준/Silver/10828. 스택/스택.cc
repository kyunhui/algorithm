#include <iostream>
#include <stack>
using namespace std;

int main(){
    stack<int> stack;
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        string s;
        int num;
        cin >> s;
        if(s == "push"){
            cin >> num;
            stack.push(num);
        }
        else if(s == "pop"){
            if(stack.empty()){
                cout << -1 << endl;
            }else{
                cout << stack.top() << endl;
                stack.pop();
            }
        }
        else if(s=="size"){
            cout << stack.size() << endl;
        }
        else if(s == "empty"){
            cout << stack.empty() << endl;
        }
        else if(s == "top"){
            if(stack.empty()){
                cout << -1 << endl;
            }else{
                cout << stack.top() << endl;
            }
        }
    }
    
}