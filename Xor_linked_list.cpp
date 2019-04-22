/* An XOR linked list is a more memory efficient
   doubly linked list. Instead of each node holding
   next and prev fields, it holds a field named
   both, which is an XOR of the next node and the
   previous node. Implement an XOR linked list;
   it has an add(element) which adds the element
   to the end, and a get(index) which returns the
   node at index.*/

#include <bits/stdc++.h>
#include <inttypes.h>
using namespace std;

//Algorithm
class Node;

Node *applyXor(Node *a, Node *b){
    return (Node*) ((uintptr_t) (a) ^ (uintptr_t)(b));
}

class Node{
    public:
        int element;
        Node *both;

        Node(int element, Node* previous, Node * next){
            this->element = element;
            this->both = applyXor(previous, next);
        }

        Node *getNext(Node *previous){
            return applyXor(previous, both);
        }
};

class XorLinkedList{
    private:
        Node *head = NULL;

    public:
        void add(int element){
            if(head == NULL){
                head = new Node(element, NULL, NULL);
            }else{
                Node *previous = NULL;
                Node *current = head;
                Node *next = applyXor(previous, (current)->both);

                while(next != NULL){
                    previous = current;
                    current = next;
                    next = applyXor(previous, current->both);
                }

                Node *newNode = new Node(element, current, NULL);
                current->both = applyXor(previous, newNode);
            }
        }

        Node *get(unsigned int index){
            /** Only works with unsigned int | index >= 0 **/
            Node *previous = NULL;
            Node *current = head;
            Node *next = applyXor(previous, current->both);

            for(int i = 0; i < index; i++){
                if(next == NULL) throw "Index out of bounds";

                previous = current;
                current = next;
                next = applyXor(previous, current->both);
            }

            return current;
        }
};

//Tests
int main (){
    XorLinkedList list;
    list.add(2);
    list.add(3);
    list.add(4);
    list.add(34);
    printf("Element: %i\n", list.get(0)->element);
    printf("Element: %i\n", list.get(3)->element);

    try{
    printf("Element: %i\n", list.get(-1)->element);
    }catch(const char *msg){
        cout << msg << endl;
    }
    return 0;
}
