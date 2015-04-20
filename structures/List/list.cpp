#include <iostream>
#include <stdexcept>
using namespace std;

class Node {
    
    public:
        template<class T>
        Node(const T &obj) {typedef type T;};

    private:
        
};

class List {

    public:
        List();
        List(unsigned int size);
        ~List();
        void* operator [] (const unsigned int &index) const;
        template <class T>
        void append(T &data);
        int pop(const unsigned int &index);
        int pop();
        bool isFull() const {return this->size == this->currentCapacity;};
        bool isEmpty() const {return this->size == 0;};

    private:
        void resize();
        static const int DEFAULT_CAPACITY = 100;
        void** list;
        int size;
        int currentCapacity;
};

List::List():
    size(0),
    currentCapacity(List::DEFAULT_CAPACITY),
    list(new void*[List::DEFAULT_CAPACITY])
    {}

List::List(const unsigned int size):
    size(0),
    currentCapacity(size),
    list(new void*[size])
    {}

List::~List() {
    delete [] this->list;
}

void* List::operator [] (const unsigned int &index) const {
    if (index > this->size)
        throw std::out_of_range("Index out of bounds.");
    return this->list[index];
}

template <class T>
void List::append(T &data) {
    if (this->isFull())
        this->resize();
    this->list[this->size] = &data;
    this->size ++;
}

void List::resize() {
    void** resized = new void*[this->currentCapacity*2];
    for (int index=0; index<this->size; index++)
        resized[index] = this->list[index];
    delete [] this->list;
    this->list = resized;
}

main() {
    List x = List();
    string* stringStuff = new string("abcdf");
    int* things = new int[50];
    x.append(stringStuff);
    x.append(things);
    cout << &x[0];
}
