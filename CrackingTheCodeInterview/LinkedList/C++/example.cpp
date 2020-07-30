#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif
class Node{
private:
public:
	int data;
	Node * next;
	Node(int data){
		this->data = data;
	}
	~Node(){
		free(this->next);
	}
};

int main(int argc, char const *argv[]){
	std::ios_base::sync_with_stdio(False);
	Node * a = new Node(2);
	std::cout << a->data << std::endl;
	return 0;
}