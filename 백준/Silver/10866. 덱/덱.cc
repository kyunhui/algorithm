#include <iostream>
#include <deque>
using namespace std;

int main(){
    deque<int> dq;

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        string s;
        int num;
        cin >> s;
        if(s == "push_front"){
            cin >> num;
            dq.push_front(num);
        }else if(s == "push_back"){
            cin >> num;
            dq.push_back(num);
        }else if(s == "pop_front"){
            if(dq.empty()){
                cout << -1 << endl;
                continue;
            }
            cout << dq.front() << endl;
            dq.pop_front();
        }else if(s == "pop_back"){
            if(dq.empty()){
                cout << -1 << endl;
                continue;
            }
            cout << dq.back() << endl;
            dq.pop_back();
        }else if(s == "size") cout << dq.size() << endl;
        else if(s == "empty") cout << dq.empty() << endl;
        else if(s == "front"){
            if(dq.empty()){
                cout << -1 << endl;
                continue;
            }
            cout << dq.front() << endl;
        }else if(s == "back"){
            if(dq.empty()){
                cout << -1 << endl;
                continue;
            }
            cout << dq.back() << endl;
        }
    }
    
}