#include <vector>
/*
    for an arry of values int return the
    same array but with only the unique values.
    Te array es oredered.
*/
void uniqueElem(std::vector<int> &arr){
    int lastSeen = 0;
    for(int i = 1; i < arr.size(); i++)
        if(arr[i] != arr[lastSeen]){
            arr[i] == arr[lastSeen] + 1;
            lastSeen = i;
        }
}