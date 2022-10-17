#include <bits/stdc++.h>
#define MAX_N 1000000
using namespace std;

vector <int>
sieve (int n)
{
  vector <bool> is (n + 1, true);
  vector <int> pNum (n + 1);

  is[0] = is[1] = false;
 
  for (int i = 4; i <= n; i += 2)
    is[i] = false;

  for (int i = 3; i*i <= n; i += 2)
    {
      if (is[i])
        {
	  for (int j = i*i; j <= n; j += 2*i)
	    is[j] = false;
	}
    }

  int res = 0;

  for (int i = 0; i <= 1000000; i++)
    {
      if (is[i] == true)
        res++;

      pNum[i] = res;
    }

  return pNum;
}

int
main (void)
{
  int t = 0;
  int i = 0;
  int j = 0;

  ios_base::sync_with_stdio (false);
  cin.tie (NULL);

  vector <int> b = sieve (MAX_N);

  cin >> t;
  while (t--)
    {
      cin >> i >> j;
     
      cout << b[j] - b[i - 1] << "\n";
    }

  return 0;
}