#include <bits/stdc++.h>
#if !defined(True)
#define True  (1==1)
#endif
#if !defined(False)
#define False (!True)
#endif

class Node{
	public:
		int data;
		Node * next;
		Node(int data){
			this->data = data;
			this->next = nullptr;
		}
		// ~Node(){
		// 	free(this->next);
		// }
	//private:	
};

class LinkedList{
	public:
	Node * head;
	int length;
	LinkedList(){
		head = nullptr;
		length = 0;
	} 
	LinkedList( std::vector<int> arry ){
		this->head = nullptr;
		this->length = 0;
		for(auto element : arry) this->append(element);
	}
	// ~LinkedList(){
	// 	Node * _iterator = this->head;
	// 	while(_iterator){
	// 		Node * prev = _iterator;
	// 		_iterator = _iterator->next;
	// 		free(prev);
	// 	}
	// }
	void init( std::vector<int> arry ){
		this->head = nullptr;
		this->length = 0;
		for(auto element : arry) this->append(element);
	}
	void append(int data){
		if(!this->head) this->head = new Node(data);
		else {
			Node * end = this->last();
			end->next = new Node(data);
		}
		this->length++;
	}
	void push(int data){
		Node * _head = new Node(data);
		_head->next = this->head;
		this->head = _head;
		this->length ++;
	}
	Node * last(){
		Node * _iterator = this->head;
		while(_iterator->next) _iterator = _iterator->next;
		return _iterator;
	}
	Node * findIth(int index){
		if(index < 0 or index >= this->length) perror("Out of list bounds");
		Node * _iterator = this->head;
		for(size_t i = 0; i < index; i++) 
			_iterator = _iterator->next;
		return _iterator;
	}
	void decapitate(){
		if(this->length == 0) perror("list empty");
		Node * old = this->head; 
		this->head = this->head->next;
		this->length -= 1;
		free(old);
	}
	Node * pop(){
		if(this->length == 0) perror("list empty");
		Node * prev_end = this->findIth(this->length - 2);
		Node * end = prev_end->next;
		prev_end->next = nullptr;
		this->length -= 1;
		return end;
	}
	bool deleteNode(Node * node){
		if(!node) return False;
		else if(!node->next) this->pop();
		else{
			node->data = node->next->data;
			node->next = node->next->next;
			this->length -= 1;
		}
		return True;
	}
	bool deleteNext(Node * node){
		node->next = node->next->next;
		this->length -= 1;
		return True;
	}
	void deleteByIndex(int index){
		if (index == 0) this->decapitate();
		else if (index == this->length - 1) this->pop();
		else this->deleteNext(this->findIth(index - 1));
	}
	std::string stringtify(){
		Node * _iterator = this->head;
		std::string res = "[";
		while(_iterator ){
			res += std::to_string(_iterator->data) + ", ";
			_iterator = _iterator->next;
		}
		res.pop_back();
		res.back() = ']';
		return res;
	}
	/*#############	Problems	###############*/
	void removeDuplicates(){
		Node * _iterator = this->head->next, * prev = this->head;
		// Fast
		std::unordered_set<int> seen; seen.insert(prev->data);
		while(_iterator){
			if(seen.find(_iterator->data) != seen.end()) this->deleteNext(prev);
			else {
				seen.insert(_iterator->data);
				prev = prev->next;
			}
			_iterator = _iterator->next;
		} 
	}
	Node * kthToLast(int k){
		return this->findIth(this->length - 1 - k);
	}
	void partition(int value){
		LinkedList _list;
		Node * _iterator = this->head;
		while(_iterator){
			if(_iterator->data < value) _list.push(_iterator->data);
			else _list.append(_iterator->data);
			_iterator = _iterator->next;
		}
		/*free memory todo*/
		this->head = _list.head;
	}
	bool isPalindrome(){
		if(!this->head || !this->head->next) return True;
		if(!this->head->next->next) return (this->head->next->data == this->head->data)? True : False;
		Node * i = this->head, * j = this->head;
		size_t count = 0;
		std::vector<int> stack;
		while(j->next ){
			j = j->next;
			if(count % 2 == 0){
				stack.push_back(i->data);
				i = i->next;
			} 
			count += 1;
		}
		if((count + 1) / 2 != 0) i = i->next;
		while(i){
			if(i->data != stack.back()) return False;
			stack.pop_back();
			i = i->next;
		}
		return True;
	}
	bool doesIntersec(LinkedList * Linked_List){
		Node * i = (Linked_List->length < this->length)? this->head : Linked_List->head;
		Node * j = (Linked_List->length > this->length)? this->head : Linked_List->head;
		for(size_t _i = 0; _i < std::abs(Linked_List->length - this->length); _i++) i = i->next;
		while( i && j && i != j){
			i = i->next;
			j = j->next;
		}
		if (!i) return False;
		else return True;
	}
	Node * hasLoop(){
		std::unordered_set<Node *> hashTable;
		Node * _iterator = this->head;
		while(_iterator){
			if (hashTable.end() != hashTable.find(_iterator)) return _iterator;
			else hashTable.insert(_iterator);
			_iterator = _iterator->next;
		}
		return nullptr;
	}
	void re_length(){
		this->length = 0;
		Node * iterator = this->head;
		while(iterator){
			this->length +=1;
			iterator = iterator->next;
		}
	}
};

LinkedList reverseSum(LinkedList * numA, LinkedList * numB){
	LinkedList res = LinkedList();
	Node * iA = numA->head, * iB = numB->head;
	bool carry = False;
	while( iA && iB ){
		int parSum = iA->data + iB->data + ((carry)? 1 : 0);
		if (parSum >= 10){
			res.append(parSum - 10);
			carry = True;
		} 
		else{
			res.append(parSum);
			carry = False;
		}
		iA = iA->next;
		iB = iB->next;
	}
	if (iA || iB){
		iA = (iB)? iB : iA;
		int parSum = iA->data + ((carry)? 1 : 0);
		if (parSum >= 10){
			res.append(parSum - 10);
			carry = True;
		} 
		else{
			res.append(parSum);
			carry = False;
		}
		iA = iA->next;
		while (iA){
			res.append(iA->data + ((carry)? 1 : 0));
			carry = False;
			iA = iA->next;
		}
	}
	if (carry) res.append(1);
	return res;
}
LinkedList LinkedSum(LinkedList * numA, LinkedList * numB){
	LinkedList res;
	if (numB->length > numA->length){
		LinkedList * temp = numA;
		numA = numB;
		numB = temp;
		//free(temp);
	}
	while (numA->length - numB->length > 0) numB->push(0);
	Node * iA = numA->head, *iB = numB->head;
	if (iA->data + iB->data > 10) res.init(std::vector<int>({1, iA->data + iB->data - 10}));
	else res.init(std::vector<int>({iA->data + iB->data}));
	
	iA = iA->next;
	iB = iB->next;
	Node * prev = res.head;
	while (iA && iB){
		if (iA->data + iB->data >= 10){
			res.append(iA->data + iB->data - 10);
			prev->data += 1;
		} 
		else res.append(iA->data + iB->data);
		iA = iA->next;
		iB = iB->next;
		prev = prev->next;
	}
	return res;
}
bool isPalindrome(Node * node, size_t index, size_t length, std::vector<int> &stack){
	if (index > length) return True;
	if (index > length / 2){
		if (length % 2 != 0 && index == length / 2 + 1) return True && isPalindrome(node->next, index + 1, length, stack);
		int back = stack.back();
		stack.pop_back();
		return node->data == back && isPalindrome(node->next, index + 1, length, stack);
	}
	else{
		stack.push_back(node->data);
		return isPalindrome(node->next, index + 1, length, stack);
	}
}

int main(int argc, char const *argv[]){
	//ios_base::sync_with_stdio(False);
	std::vector<int> stack;
	LinkedList LL;
	LL.append(0);
	LL.push(10);
	std::cout << LL.stringtify() << std::endl;
	LL = LinkedList(std::vector<int>{1, 8, 6, 79});
	LL.deleteByIndex(2);
	LL.decapitate();
	LL.pop();
	std::cout << LL.stringtify() << std::endl;
	LL = LinkedList(std::vector<int>{8, 1, 8, 8, 7, 8, 7});
	LL.removeDuplicates();
	std::cout << LL.stringtify() << std::endl;
	LL = LinkedList(std::vector<int>{8, 8, 2, 3, 4, 8});
	LL.deleteNode(LL.findIth(2));
	std::cout << LL.stringtify() << std::endl;
	std::cout << reverseSum(new LinkedList(std::vector<int>{7, 1, 7}), new LinkedList(std::vector<int>{5, 9, 2, 9, 1, 2, 3})).stringtify() << std::endl;
	std::cout << LinkedSum(new LinkedList(std::vector<int>{1, 1, 6, 1, 7}), new LinkedList(std::vector<int>{2, 9 ,5})).stringtify() << std::endl;
	LL = LinkedList(std::vector<int>{3, 5, 8, 5, 10, 2, 1});
	LL.partition(5);
	std::cout << LL.stringtify() << std::endl;
	LL = LinkedList(std::vector<int>{1, 0, 0, 2, 0, 0, 1});
	std::cout << LL.isPalindrome() << std::endl;
	std::cout << isPalindrome(LL.head, 1, LL.length, stack) << std::endl;
	LL = LinkedList(std::vector<int>{1, 0, 0, 2, 2, 0, 0, 2});
	std::cout << LL.isPalindrome() << std::endl;
	stack.clear();
	std::cout << isPalindrome(LL.head, 1, LL.length, stack) << std::endl;
	std::cout << LL.doesIntersec(new LinkedList(std::vector<int>{7, 1, 7})) << std::endl;
	LinkedList LL2(std::vector<int>{7, 1, 7, 1});
	Node * ref = LL.head;
	for(size_t i = 0; i < LL.length - LL2.length; i++) ref = ref->next;
	LL2.head->next->next = ref;
	LL2.re_length();
	std::cout << LL.doesIntersec(&LL2) << std::endl;
	LL = LinkedList(std::vector<int>{3, 5, 8, 5, 10, 2, 1});
	std::cout << LL.hasLoop() << std::endl;
	LL.last()->next = LL.findIth(3);
	std::cout << LL.hasLoop()->data << std::endl;
	return 0;
}
	