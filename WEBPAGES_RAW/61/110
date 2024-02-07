#ifndef ARRAY_QUEUE_HPP_
#define ARRAY_QUEUE_HPP_

#include <string>
#include <iostream>
#include <sstream>
#include <initializer_list>
#include "ics_exceptions.hpp"


namespace ics {


template<class T> class ArrayQueue {
  public:
    //Destructor/Constructors
    ~ArrayQueue();

    ArrayQueue          ();
    explicit ArrayQueue (int initial_length);
    ArrayQueue          (const ArrayQueue<T>& to_copy);
    explicit ArrayQueue (const std::initializer_list<T>& il);

    //Iterable class must support "for-each" loop: .begin()/.end()/.size() and prefix ++ on returned result
    template <class Iterable>
    explicit ArrayQueue (const Iterable& i);


    //Queries
    bool empty      () const;
    int  size       () const;
    T&   peek       () const;
    std::string str () const; //supplies useful debugging information; contrast to operator <<


    //Commands
    int  enqueue (const T& element);
    T    dequeue ();
    void clear   ();

    //Iterable class must support "for-each" loop: .begin()/.end() and prefix ++ on returned result
    template <class Iterable>
    int enqueue_all (const Iterable& i);


    //Operators
    ArrayQueue<T>& operator = (const ArrayQueue<T>& rhs);
    bool operator == (const ArrayQueue<T>& rhs) const;
    bool operator != (const ArrayQueue<T>& rhs) const;

    template<class T2>
    friend std::ostream& operator << (std::ostream& outs, const ArrayQueue<T2>& q);



    class Iterator {
      public:
        //Private constructor called in begin/end, which are friends of ArrayQueue<T>
        ~Iterator();
        T           erase();
        std::string str  () const;
        ArrayQueue<T>::Iterator& operator ++ ();
        ArrayQueue<T>::Iterator  operator ++ (int);
        bool operator == (const ArrayQueue<T>::Iterator& rhs) const;
        bool operator != (const ArrayQueue<T>::Iterator& rhs) const;
        T& operator *  () const;
        T* operator -> () const;
        friend std::ostream& operator << (std::ostream& outs, const ArrayQueue<T>::Iterator& i) {
          outs << i.str(); //Use the same meaning as the debugging .str() method
          return outs;
        }
        friend Iterator ArrayQueue<T>::begin () const;
        friend Iterator ArrayQueue<T>::end   () const;

      private:
        //If can_erase is false, current indexes the "next" value (must ++ to reach it)
        int            current;
        ArrayQueue<T>* ref_queue;
        int            expected_mod_count;
        bool           can_erase = true;

        //Called in friends begin/end
        Iterator(ArrayQueue<T>* iterate_over, int initial);
    };


    Iterator begin () const;
    Iterator end   () const;


  private:
    T*  queue;          //Circular array with data stored in indexes front to rear-1
    int length    =  1; //Physical length of array: must be strictly > .size()
    int front     =  0; //Array index of front in queue
    int rear      =  0; //Array index ONE BEYOND rear in queue
    int mod_count =  0; //For sensing concurrent modification

    //Helper methods
    int  erase_at         (int i);
    void ensure_length    (int new_length);
    void ensure_length_low(int new_length);
    bool is_in            (int i) const;
  };





////////////////////////////////////////////////////////////////////////////////
//
//ArrayQueue class and related definitions

//Destructor/Constructors

template<class T>
ArrayQueue<T>::~ArrayQueue() {
  delete[] queue;
}


template<class T>
ArrayQueue<T>::ArrayQueue() {
  queue = new T[length];
}


template<class T>
ArrayQueue<T>::ArrayQueue(int initial_length)
: length(initial_length) {
  if (length < 1)
    length = 1;
  queue = new T[length];
}


template<class T>
ArrayQueue<T>::ArrayQueue(const ArrayQueue<T>& to_copy)
: length(to_copy.length)  {
  queue = new T[length];
  front = 0;
  rear  = to_copy.size();
  for (int i=0; i<rear; ++i)
    queue[i] = to_copy.queue[(to_copy.front+i)%to_copy.length];
  //resulting queue starts at front of array, regardless of where to_copy starts
}


template<class T>
ArrayQueue<T>::ArrayQueue(const std::initializer_list<T>& il)
: length(il.size()) {
  queue = new T[length];
  for (const T& q_elem : il)
    enqueue(q_elem);
}


template<class T>
template<class Iterable>
ArrayQueue<T>::ArrayQueue(const Iterable& i)
: length(i.size()) {
  queue = new T[length];
  for (const T& v : i)
    enqueue(v);
}


////////////////////////////////////////////////////////////////////////////////
//
//Queries

template<class T>
bool ArrayQueue<T>::empty() const {
  return front == rear;
}


template<class T>
int ArrayQueue<T>::size() const {
  return rear >= front ? rear-front : length-(front-rear);
}


template<class T>
T& ArrayQueue<T>::peek () const {
  if (this->empty())
    throw EmptyError("ArrayQueue::peek");

  return queue[front];
}


template<class T>
std::string ArrayQueue<T>::str() const {
  std::ostringstream answer;
  answer << "ArrayQueue[";

  if (length != 0)
    for (int i=0; i<length; ++i) {
      answer << i << ":";
      if (this->is_in(i))
        answer << queue[i];
      answer << (i == length-1 ? "]" : ",");
    }

  answer << "(length=" << length << ",front=" << front << ",rear=" << rear << ",mod_count=" << mod_count << ")";
  return answer.str();
}


////////////////////////////////////////////////////////////////////////////////
//
//Commands

template<class T>
int ArrayQueue<T>::enqueue(const T& element) {
  this->ensure_length(this->size()+1);
  queue[rear] = element;
  rear = (rear+1)%length;
  ++mod_count;
  return 1;
}


template<class T>
T ArrayQueue<T>::dequeue() {
  if (this->empty())
    throw EmptyError("ArrayQueue::dequeue");

  T answer = queue[front];
  front = (front+1)%length;
  this->ensure_length_low(this->size());
  ++mod_count;
  return answer;
}


template<class T>
void ArrayQueue<T>::clear() {
  front = 0;
  rear  = 0;
  this->ensure_length_low(0);
  ++mod_count;
}


template<class T>
template<class Iterable>
int ArrayQueue<T>::enqueue_all(const Iterable& i) {
  int count = 0;
  for (const T& v : i)
     count += enqueue(v);

    return count;
}


////////////////////////////////////////////////////////////////////////////////
//
//Operators

template<class T>
ArrayQueue<T>& ArrayQueue<T>::operator = (const ArrayQueue<T>& rhs) {
  if (this == &rhs)
    return *this;

  front = 0;
  rear = rhs.size();
  this->ensure_length(rear);
  for (int i=0; i<rear; ++i)
    queue[i] = rhs.queue[(rhs.front+i)%rhs.length];
  //resulting queue starts at front of array, regardless of where to_copy starts

  ++mod_count;
  return *this;
}


template<class T>
bool ArrayQueue<T>::operator == (const ArrayQueue<T>& rhs) const {
  if (this == &rhs)
    return true;

  int used = this->size();
  if (used != rhs.size())
    return false;

  ArrayQueue<T>::Iterator rhs_i = rhs.begin();
  for (int i=0; i<used; ++i,++rhs_i)
    // Uses ! and ==, so != on T need not be defined
    if (!(queue[(front+i)%length] == *rhs_i))
      return false;

  return true;
}


template<class T>
bool ArrayQueue<T>::operator != (const ArrayQueue<T>& rhs) const {
  return !(*this == rhs);
}


template<class T>
std::ostream& operator << (std::ostream& outs, const ArrayQueue<T>& q) {
  outs << "queue[";

  if (!q.empty()) {
    outs << q.queue[q.front];
    for (int i=(q.front+1)%q.length; i!=q.rear; i=(i+1)%q.length)
      outs << "," << q.queue[i];
  }

  outs << "]:rear";
  return outs;
}


////////////////////////////////////////////////////////////////////////////////
//
//Iterator constructors

template<class T>
auto ArrayQueue<T>::begin () const -> ArrayQueue<T>::Iterator {
  return Iterator(const_cast<ArrayQueue<T>*>(this),front);
}


template<class T>
auto ArrayQueue<T>::end () const -> ArrayQueue<T>::Iterator {
  return Iterator(const_cast<ArrayQueue<T>*>(this),rear);
}


////////////////////////////////////////////////////////////////////////////////
//
//Private helper methods

template<class T>
int ArrayQueue<T>::erase_at(int i) {
  int shift_count = (rear >= i ? rear-i-1: length-(i-rear))-1;
  int to   = i;
  int from = (to+1)%length;
  for (int i=0; i<=shift_count; ++i) {
    queue[to] = queue[from];
    to = from;
    from = (from+1)%length;
  }
  rear = (rear == 0 ? length-1 : rear - 1);
  this->ensure_length_low(this->size());
  ++mod_count;
  return 1;
}


template<class T>
void ArrayQueue<T>::ensure_length(int new_length) {
  //length must be > new_length; remember requirement of length at least size()+1
  if (length > new_length)
    return;
  T*  old_queue  = queue;
  int old_length = length;
  int used = this->size(); //must precede length change; see computation of size()!
  length = 1+std::max(new_length,2*(length-1));
  queue  = new T[length];
  for (int i=0; i<used; ++i)
    queue[i] = old_queue[(front+i)%old_length];
  front = 0;
  rear  = used;

  delete [] old_queue;
}


template<class T>
void ArrayQueue<T>::ensure_length_low(int new_length) {
  //length must be > new_length; remember requirement of length at least size()+1
  if (length-1 < 4*new_length)
    return;
  T*  old_queue  = queue;
  int old_length = length;
  int used = this->size(); //must precede length change!
  length = 1+2*new_length;
  queue  = new T[length];
  for (int i=0; i<used; ++i)
    queue[i] = old_queue[(front+i)%old_length];
  front = 0;
  rear  = used;

  delete [] old_queue;
}


  template<class T>
bool ArrayQueue<T>::is_in(int i) const {
  return  rear >= front ? (i>=front && i<rear) : (i>=front || i<rear);
}





////////////////////////////////////////////////////////////////////////////////
//
//Iterator class definitions

template<class T>
ArrayQueue<T>::Iterator::Iterator(ArrayQueue<T>* iterate_over, int initial)
: current(initial), ref_queue(iterate_over), expected_mod_count(ref_queue->mod_count) {
}


template<class T>
ArrayQueue<T>::Iterator::~Iterator()
{}


template<class T>
T ArrayQueue<T>::Iterator::erase() {
  if (expected_mod_count != ref_queue->mod_count)
    throw ConcurrentModificationError("ArrayQueue::Iterator::erase");
  if (!can_erase)
    throw CannotEraseError("ArrayQueue::Iterator::erase Iterator cursor already erased");
  if (!ref_queue->is_in(current))
    throw CannotEraseError("ArrayQueue::Iterator::erase Iterator cursor beyond data structure");

  can_erase = false;
  T to_return = ref_queue->queue[current];
  ref_queue->erase_at(current);
  expected_mod_count = ref_queue->mod_count;
  return to_return;
}


template<class T>
std::string ArrayQueue<T>::Iterator::str() const {
  std::ostringstream answer;
  answer << ref_queue->str() << "(current=" << current << ",expected_mod_count=" << expected_mod_count << ",can_erase=" << can_erase << ")";
  return answer.str();
}


template<class T>
auto ArrayQueue<T>::Iterator::operator ++ () -> ArrayQueue<T>::Iterator& {
  if (expected_mod_count != ref_queue->mod_count)
    throw ConcurrentModificationError("ArrayQueue::Iterator::operator ++");

  if (current == ref_queue->rear)
    return *this;

  if (can_erase)
    current = (current+1)%ref_queue->length;
  else
    can_erase = true;  //current already indexes "one beyond" deleted value

  return *this;
}


template<class T>
auto ArrayQueue<T>::Iterator::operator ++ (int) -> ArrayQueue<T>::Iterator {
  if (expected_mod_count != ref_queue->mod_count)
    throw ConcurrentModificationError("ArrayQueue::Iterator::operator ++(int)");

  if (current == ref_queue->rear)
    return *this;

  Iterator to_return(*this);
  if (can_erase)
    current = (current+1)%ref_queue->length;
  else
    can_erase = true;  //current already indexes "one beyond" deleted value

  return to_return;
}


template<class T>
bool ArrayQueue<T>::Iterator::operator == (const ArrayQueue<T>::Iterator& rhs) const {
  const Iterator* rhsASI = dynamic_cast<const Iterator*>(&rhs);
  if (rhsASI == 0)
    throw IteratorTypeError("ArrayQueue::Iterator::operator ==");
  if (expected_mod_count != ref_queue->mod_count)
    throw ConcurrentModificationError("ArrayQueue::Iterator::operator ==");
  if (ref_queue != rhsASI->ref_queue)
    throw ComparingDifferentIteratorsError("ArrayQueue::Iterator::operator ==");

  return current == rhsASI->current;
}


template<class T>
bool ArrayQueue<T>::Iterator::operator != (const ArrayQueue<T>::Iterator& rhs) const {
  const Iterator* rhsASI = dynamic_cast<const Iterator*>(&rhs);
  if (rhsASI == 0)
    throw IteratorTypeError("ArrayQueue::Iterator::operator !=");
  if (expected_mod_count != ref_queue->mod_count)
    throw ConcurrentModificationError("ArrayQueue::Iterator::operator !=");
  if (ref_queue != rhsASI->ref_queue)
    throw ComparingDifferentIteratorsError("ArrayQueue::Iterator::operator !=");

  return current != rhsASI->current;
}


template<class T>
T& ArrayQueue<T>::Iterator::operator *() const {
  if (expected_mod_count != ref_queue->mod_count)
    throw ConcurrentModificationError("ArrayQueue::Iterator::operator *");
  if (!can_erase || !ref_queue->is_in(current)) {
    std::ostringstream where;
    where << current
          << " when front = " << ref_queue->front
          << " and rear = " << ref_queue->rear;
    throw IteratorPositionIllegal("ArrayQueue::Iterator::operator * Iterator illegal: "+where.str());
  }

  return ref_queue->queue[current];
}


template<class T>
T* ArrayQueue<T>::Iterator::operator ->() const {
  if (expected_mod_count != ref_queue->mod_count)
    throw ConcurrentModificationError("ArrayQueue::Iterator::operator ->");
  if (!can_erase || !ref_queue->is_in(current)) {
    std::ostringstream where;
    where << current
          << " when front = " << ref_queue->front
          << " and rear = " << ref_queue->rear;
    throw IteratorPositionIllegal("ArrayQueue::Iterator::operator -> Iterator illegal: "+where.str());
  }

  return &ref_queue->queue[current];
}

}

#endif /* ARRAY_QUEUE_HPP_ */
