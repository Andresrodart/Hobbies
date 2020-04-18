#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
using namespace std;

int main(int argc, char const *argv[]){
	ios_base::sync_with_stdio(False);
	uint64_t n, k, left = 0, right = 0, differentValues = 0, answerL = 0, answerR = 0;
	vector<uint64_t> occurrenceOfIthValue(1200300);
	cin >> n >> k;
	vector<uint64_t> arr(n, 0);
	for (left = 0; left < n; left++)	cin >> arr[right];
	for (left = 0; left < n; left++){
		while (right < n){
			if(++occurrenceOfIthValue[arr[right]] == 1) differentValues++;
			if(differentValues > k){
				if(--occurrenceOfIthValue[arr[right]] == 0) differentValues--;
				break;
			}
			right++;
		}
		if(right - left > answerR - answerL) answerR = right, answerL = left;
		if(--occurrenceOfIthValue[arr[left]] == 0) differentValues--;
	}
	std::cout << answerL + 1 << ' ' << answerR << std::endl;
	return 0;
}