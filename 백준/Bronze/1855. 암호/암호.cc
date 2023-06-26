#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char dec[300];
    char enc[100][30]={0};
    int y=0,x=0;
    int col;


    cin >> col >> dec;

    int len = strlen(dec);
    int dir = 0;

    for(int i=0;i<len;i++)
    {
        enc[y][x] = dec[i];
        if(dir == 0 && x+1>=col)
        {
            y++;
            dir=1;
            continue;
        }
        else if(dir==1 && x-1 < 0)
        {
            y++;
            dir=0;
            continue;
        }

        if(dir==0)
        {
            x++;
        }
        else {
            x--;
        }
    }

    for(int i=0;i<col;i++)
    {
        for(int j=0;j<y;j++)
        {
            cout << enc[j][i];
        }
    }

    return 0;
}