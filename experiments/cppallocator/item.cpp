
/*
class Item:
	def __init__(self, n, next):
		self.n = n
		self.next = next
*/

class Item {

public:
	int n;
	Item * next;
	Item(int n, Item * next);
};

Item::Item(int n, Item * next) {
	this->n = n;
	this->next = next;
}
	
	
