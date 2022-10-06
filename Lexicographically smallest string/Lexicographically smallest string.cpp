class Solution {
  public:
   string lexicographicallySmallest(string S, int k) {
stack<char>s;
int n = S.length() ;
int c = 0;
for(int i = 0; i < 32; i++)
c +=((n>>i)&1);

if(c==1)
k/=2;
else
k*=2;
if(k >= n)
return "-1";

string x = S;sort(x.begin() , x.end());
if(S==x)
return S.substr(0 , n - k);

for(int i = 0 ; i < n ; i++)
{
if(s.empty() || s.top() <= S[i])
s.push(S[i]);
else
{
while(!s.empty() && s.top() > S[i] && k>0)
k--, s.pop();
s.push(S[i]);
}
}
x = "";
while(k > 0 && !s.empty())
s.pop() , k--;
while(!s.empty())
x.push_back(s.top()) , s.pop();
reverse(x.begin() , x.end());
return x;
}
};