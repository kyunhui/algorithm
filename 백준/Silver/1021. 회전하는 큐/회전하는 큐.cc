#include <iostream>
#include <deque>
using namespace std;

deque<int> dq;
int n, m, x;
int count = 0;
int idx = 0;
int main(){

    int find[51];
    cin >> n >> m;


    for (int i = 1; i <= n; i++)
    {
        dq.push_back(i);
    }
    
    for (int i = 0; i < m; i++)
    {
        cin >> x;
        find[i] = x;
    }
    

    for (int i = 0; i < m; i++)
    {
        if (dq.size() == 1)
        {
            continue;
        }
        for (int j = 0; j < n; j++)
        {
            if(find[i] == dq.at(j)){
                idx = j;
                break;
            }
        }

        if(idx <= dq.size()/2){
            for (int j = 0; j < idx; j++)
            {
                dq.push_back(dq.front());
                dq.pop_front();
                count ++;
            }
            dq.pop_front();
        }
        else {
            for (int j = 0; j < dq.size() - idx; j++)
            {
                dq.push_front(dq.back());
                dq.pop_back();
                count++;
            }
            dq.pop_front();
        }
    }

    cout << count << endl;

    return 0;
}