#include <iostream>
#include <queue>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    queue<int> q;
    int t;
    int num;
    string s;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> s;
        if(s.compare("push")==0){
            cin >> num;
            q.push(num);
        }
        else if(s.compare("pop")==0){
            if(q.empty()){
                cout << -1 << '\n';
                continue;
            }
            cout << q.front() << '\n';
            q.pop();
        }
        else if(s.compare("size")==0){
            cout << q.size() << '\n';
        }
        else if(s.compare("empty")==0){
            cout << q.empty() << '\n';
        }
        else if(s.compare("front")==0){
            if(q.empty()){
                cout << -1 << '\n';
                continue;
            }
            cout << q.front() << '\n';
        }
        else if(s.compare("back")==0){
            if(q.empty()){
                cout << -1 << '\n';
                continue;
            }
            cout << q.back() << '\n';
        }
    }   
}