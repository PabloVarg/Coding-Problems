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

class Node{
    public:
        int element;
        Node *both;

        Node(int element){
            this->element = element;
        }
};

Node *applyXor(Node *a, Node *b){
    return (Node*) ((uintptr_t) (a) ^ (uintptr_t)(b));
}

class XorLinkedList{
    private:
        Node *head = NULL;

    public:
        void add(int element){
            cout<<endl<<endl;
            Node *previous = NULL;
            Node **current = &head;
            Node *next;

            while(*current != NULL){
                cout<<"Provious"<<previous<<endl;
                cout<<"Next"<<next<<endl;
                cout<<"Current: "<<*current<<endl;
                cout<<"Both: "<<(*current)->both<<endl<<endl;
                next = applyXor(previous, (*current)->both);
                previous = *current;
                current = &next;
                cout<<"Provious"<<previous<<endl;
                cout<<"Next"<<next<<endl;
                cout<<"Current: "<<*current<<endl<<endl;
            }

            *current = new Node(element);
            (*current)->both = applyXor(previous, NULL);
            cout<<"Created: "<<*current<<endl;

            if(previous != NULL){
                cout<<previous->both<<endl;
                previous->both = applyXor(previous->both, *current);
                cout<<previous->both<<endl;
            }
        }

        Node *get(int index){
            Node *previous = NULL;
            Node *current = head;
            Node *next;

            for(int i = 0; i < index; i++){
                next = applyXor(previous, current->both);
                previous = current;
                current = next;
            }

            return current;
        }
    void printList ()
    {
        Node *curr = head;
        Node *prev = NULL;
        Node *next;

        cout << "Following are the nodes of Linked List: \n";

        while (curr != NULL)
        {
            // print current node
            cout<<curr->element<<" ";

            // get address of next node: curr->npx is
            // next^prev, so curr->npx^prev will be
            // next^prev^prev which is next
            next = applyXor (prev, curr->both);

            // update prev and curr for next iteration
            prev = curr;
            curr = next;
        }
    }
};

int main ()
{
    XorLinkedList list;
    list.add(2);
    list.add(3);
    list.add(4);
    list.add(34);
    printf("elem %i\n", (new Node(3))->element);
    printf("Element: %p, %i\n", list.get(1), list.get(1)->element);
    list.printList();
    return (0);
}
