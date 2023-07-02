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
        cin >> s;
        string VPS = "YES";
        for (int j = 0; j < s.length(); j++)
        {
            if(s[j] == '(') stack.push(s[j]);
            else if(s[j] == ')'){
                if(stack.empty()){
                    VPS = "NO";
                    break;
                }
                stack.pop();
            }
        }
        if(stack.empty() && VPS == "YES"){
            cout << "YES" << endl;
        }else if(!stack.empty() || VPS == "NO"){
            cout << "NO" << endl;
        }
        while (!stack.empty()) stack.pop();
    }
}