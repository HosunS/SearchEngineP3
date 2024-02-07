#ifndef ARRAY_SET_HPP_
#define ARRAY_SET_HPP_

#include <string>
#include <iostream>
#include <sstream>
#include <initializer_list>
#include "ics_exceptions.hpp"


namespace ics {


template<class T> class ArraySet {
  public:
    //Destructor/Constructors
    ~ArraySet();

 	  ArraySet          ();
	  explicit ArraySet (int initial_length);
	  ArraySet          (const ArraySet<T>& to_copy);
	  explicit ArraySet (const std::initializer_list<T>& il);

    //Iterable class must support "for-each" loop: .begin()/.end()/.size() and prefix ++ on returned result
    template <class Iterable>
    explicit ArraySet (const Iterable& i);


    //Queries
    bool empty      () const;
    int  size       () const;
    bool contains   (const T& element) const;
    std::string str () const; //supplies useful debugging information; contrast to operator <<

    //Iterable class must support "for-each" loop: .begin()/.end() and prefix ++ on returned result
    template <class Iterable>
    bool contains_all (const Iterable& i) const;


    //Commands
    int  insert (const T& element);
    int  erase  (const T& element);
    void clear  ();

    //Iterable class must support "for" loop: .begin()/.end() and prefix ++ on returned result

    template <class Iterable>
    int insert_all(const Iterable& i);

    template <class Iterable>
    int erase_all(const Iterable& i);

    template<class Iterable>
    int retain_all(const Iterable& i);


    //Operators
    ArraySet<T>& operator = (const ArraySet<T>& rhs);
    bool operator == (const ArraySet<T>& rhs) const;
    bool operator != (const ArraySet<T>& rhs) const;
    bool operator <= (const ArraySet<T>& rhs) const;
    bool operator <  (const ArraySet<T>& rhs) const;
    bool operator >= (const ArraySet<T>& rhs) const;
    bool operator >  (const ArraySet<T>& rhs) const;

    template<class T2>
    friend std::ostream& operator << (std::ostream& outs, const ArraySet<T2>& s);



    class Iterator {
      public:
        //Private constructor called in begin/end, which are friends of ArraySet<T>
        ~Iterator();
        T           erase();
        std::string str  () const;
        ArraySet<T>::Iterator& operator ++ ();
        ArraySet<T>::Iterator  operator ++ (int);
        bool operator == (const ArraySet<T>::Iterator& rhs) const;
        bool operator != (const ArraySet<T>::Iterator& rhs) const;
        T& operator *  () const;
        T* operator -> () const;
        friend std::ostream& operator << (std::ostream& outs, const ArraySet<T>::Iterator& i) {
          outs << i.str(); //Use the same meaning as the debugging .str() method
          return outs;
        }
        friend Iterator ArraySet<T>::begin () const;
        friend Iterator ArraySet<T>::end   () const;

      private:
        //If can_erase is false, current indexes the "next" value (must ++ to reach it)
        int          current;
        ArraySet<T>* ref_set;
        int          expected_mod_count;
        bool         can_erase = true;

        //Called in friends begin/end
        Iterator(ArraySet<T>* iterate_over, int initial);
    };


    Iterator begin () const;
    Iterator end   () const;


  private:
    T*  set;           //Unordered contiguous array
    int length    = 0; //Physical length of array: must be >= .size()
    int used      = 0; //Amount of array used: invariant: 0 <= used <= length
    int mod_count = 0; //For sensing concurrent modification

    //Helper methods
    int  erase_at       (int i);
  void ensure_length    (int new_length);
  void ensure_length_low(int new_length);
  };





////////////////////////////////////////////////////////////////////////////////
//
//ArraySet class and related definitions

//Destructor/Constructors

template<class T>
ArraySet<T>::~ArraySet() {
  delete[] set;
}


template<class T>
ArraySet<T>::ArraySet() {
  set = new T[length];
}


template<class T>
ArraySet<T>::ArraySet(int initial_length)
: length(initial_length) {
  if (length < 0)
    length = 0;
  set = new T[length];
}


template<class T>
ArraySet<T>::ArraySet(const ArraySet<T>& to_copy)
: length(to_copy.length), used(to_copy.used) {
  set = new T[length];
  for (int i=0; i<to_copy.used; ++i)
    set[i] = to_copy.set[i];
}


template<class T>
ArraySet<T>::ArraySet(const std::initializer_list<T>& il)
: length(il.size()) {
  set = new T[length];
  for (const T& s_elem : il)
    insert(s_elem);
}


template<class T>
template<class Iterable>
ArraySet<T>::ArraySet(const Iterable& i)
: length(i.size()) {
  set = new T[length];
  for (const T& v : i)
    insert(v);
}


////////////////////////////////////////////////////////////////////////////////
//
//Queries

template<class T>
bool ArraySet<T>::empty() const {
  return used == 0;
}


template<class T>
int ArraySet<T>::size() const {
  return used;
}


template<class T>
bool ArraySet<T>::contains (const T& element) const {
  for (int i=0; i<used; ++i)
    if (set[i] == element)
      return true;

  return false;
}


template<class T>
std::string ArraySet<T>::str() const {
  std::ostringstream answer;
  answer << "ArraySet[";

  if (length != 0) {
    answer << "0:" << set[0];
    for (int i=1; i<length; ++i)
      answer << "," << i << ":" << set[i];
  }

  answer << "](length=" << length << ",used=" << used << ",mod_count=" << mod_count << ")";
  return answer.str();
}


template<class T>
template<class Iterable>
bool ArraySet<T>::contains_all (const Iterable& i) const {
  for (const T& v : i)
    if (!contains(v))
        return false;

    return true;
}


////////////////////////////////////////////////////////////////////////////////
//
//Commands

template<class T>
int ArraySet<T>::insert(const T& element) {
  for (int i=0; i<used; ++i)
    if (set[i] == element)
      return 0;

  this->ensure_length(used+1);
  set[used++] = element;
  ++mod_count;
  return 1;
}


template<class T>
int ArraySet<T>::erase(const T& element) {
  for (int i=0; i<used; ++i)
    if (set[i] == element)
      return erase_at(i);

  return 0;
}


template<class T>
void ArraySet<T>::clear() {
  used = 0;
  this->ensure_length_low(0);
  ++mod_count;
}


template<class T>
template<class Iterable>
int ArraySet<T>::insert_all(const Iterable& i) {
  int count = 0;
  for (const T& v : i)
     count += insert(v);

  return count;
}


template<class T>
template<class Iterable>
int ArraySet<T>::erase_all(const Iterable& i) {
  int count = 0;
  for (const T& v : i)
     count += erase(v);

  return count;
}


template<class T>
template<class Iterable>
int ArraySet<T>::retain_all(const Iterable& i) {
  ArraySet s(i);
  int count = 0;
  for (int i=0; i<used; i++)
    if (!s.contains(set[i])) {
      erase_at(i);
      --i;
      ++count;
    }

  return count;
}


////////////////////////////////////////////////////////////////////////////////
//
//Operators

template<class T>
ArraySet<T>& ArraySet<T>::operator = (const ArraySet<T>& rhs) {
  if (this == &rhs)
    return *this;

  this->ensure_length(rhs.used);
  used = rhs.used;
  for (int i=0; i<used; ++i)
    set[i] = rhs.set[i];

  ++mod_count;
  return *this;
}


template<class T>
bool ArraySet<T>::operator == (const ArraySet<T>& rhs) const {
  if (this == &rhs)
    return true;

  if (used != rhs.size())
    return false;

  for (int i=0; i<used; ++i)
    if (!rhs.contains(set[i]))
      return false;

  return true;
}


template<class T>
bool ArraySet<T>::operator != (const ArraySet<T>& rhs) const {
  return !(*this == rhs);
}


template<class T>
bool ArraySet<T>::operator <= (const ArraySet<T>& rhs) const {
  if (this == &rhs)
    return true;

  if (used > rhs.size())
    return false;

  for (int i=0; i<used; ++i)
    if (!rhs.contains(set[i]))
      return false;

  return true;
}


template<class T>
bool ArraySet<T>::operator < (const ArraySet<T>& rhs) const {
  if (this == &rhs)
    return false;

  if (used >= rhs.size())
    return false;

  for (int i=0; i<used; ++i)
    if (!rhs.contains(set[i]))
      return false;

  return true;
}


template<class T>
bool ArraySet<T>::operator >= (const ArraySet<T>& rhs) const {
  return rhs <= *this;
}


template<class T>
bool ArraySet<T>::operator > (const ArraySet<T>& rhs) const {
  return rhs < *this;
}


template<class T>
std::ostream& operator << (std::ostream& outs, const ArraySet<T>& s) {
  outs << "set[";

  if (!s.empty()) {
    outs << s.set[0];
    for (int i=1; i < s.used; ++i)
      outs << ","<< s.set[i];
  }

  outs << "]";
  return outs;
}


////////////////////////////////////////////////////////////////////////////////
//
//Iterator constructors

template<class T>
auto ArraySet<T>::begin () const -> ArraySet<T>::Iterator {
  return Iterator(const_cast<ArraySet<T>*>(this),0);
}


template<class T>
auto ArraySet<T>::end () const -> ArraySet<T>::Iterator {
  return Iterator(const_cast<ArraySet<T>*>(this),used);
}


////////////////////////////////////////////////////////////////////////////////
//
//Private helper methods

template<class T>
int ArraySet<T>::erase_at(int i) {
  set[i] = set[--used];
  this->ensure_length_low(used);
  ++mod_count;
  return 1;
}


template<class T>
void ArraySet<T>::ensure_length(int new_length) {
  if (length >= new_length)
    return;
  T* old_set = set;
  length = std::max(new_length,2*length);
  set = new T[length];
  for (int i=0; i<used; ++i)
    set[i] = old_set[i];

  delete [] old_set;
}


template<class T>
void ArraySet<T>::ensure_length_low(int new_length) {
  if (length < 4 * new_length)
    return;
  T *old_set = set;
  length = 2 * new_length;
  set = new T[length];
  for (int i = 0; i < used; ++i)
    set[i] = old_set[i];

  delete[] old_set;
}




////////////////////////////////////////////////////////////////////////////////
//
//Iterator class definitions

template<class T>
ArraySet<T>::Iterator::Iterator(ArraySet<T>* iterate_over, int initial)
: current(initial), ref_set(iterate_over), expected_mod_count(ref_set->mod_count) {
}


template<class T>
ArraySet<T>::Iterator::~Iterator() {}


template<class T>
T ArraySet<T>::Iterator::erase() {
  if (expected_mod_count != ref_set->mod_count)
    throw ConcurrentModificationError("ArraySet::Iterator::erase");
  if (!can_erase)
    throw CannotEraseError("ArraySet::Iterator::erase Iterator cursor already erased");
  if (current < 0 || current >= ref_set->used)
    throw CannotEraseError("ArraySet::Iterator::erase Iterator cursor beyond data structure");

  can_erase = false;
  T to_return = ref_set->set[current];
  ref_set->erase_at(current);
  expected_mod_count = ref_set->mod_count;
  return to_return;
}


template<class T>
std::string ArraySet<T>::Iterator::str() const {
  std::ostringstream answer;
  answer << ref_set->str() << "(current=" << current << ",expected_mod_count=" << expected_mod_count << ",can_erase=" << can_erase << ")";
  return answer.str();
}


template<class T>
auto ArraySet<T>::Iterator::operator ++ () -> ArraySet<T>::Iterator& {
  if (expected_mod_count != ref_set->mod_count)
    throw ConcurrentModificationError("ArraySet::Iterator::operator ++");

  if (current >= ref_set->used)
    return *this;

  if (can_erase)
    ++current;
  else
    can_erase = true;  //current already indexes "one beyond" erased value

  return *this;
}


template<class T>
auto ArraySet<T>::Iterator::operator ++ (int) -> ArraySet<T>::Iterator {
  if (expected_mod_count != ref_set->mod_count)
    throw ConcurrentModificationError("ArraySet::Iterator::operator ++(int)");

  if (current >= ref_set->used)
    return *this;

  Iterator to_return(*this);
  if (can_erase)
    ++current;
  else
    can_erase = true;  //current already indexes "one beyond" erased value

  return to_return;
}


template<class T>
bool ArraySet<T>::Iterator::operator == (const ArraySet<T>::Iterator& rhs) const {
  const Iterator* rhsASI = dynamic_cast<const Iterator*>(&rhs);
  if (rhsASI == 0)
    throw IteratorTypeError("ArraySet::Iterator::operator ==");
  if (expected_mod_count != ref_set->mod_count)
    throw ConcurrentModificationError("ArraySet::Iterator::operator ==");
  if (ref_set != rhsASI->ref_set)
    throw ComparingDifferentIteratorsError("ArraySet::Iterator::operator ==");

  return current == rhsASI->current;
}


template<class T>
bool ArraySet<T>::Iterator::operator != (const ArraySet<T>::Iterator& rhs) const {
  const Iterator* rhsASI = dynamic_cast<const Iterator*>(&rhs);
  if (rhsASI == 0)
    throw IteratorTypeError("ArraySet::Iterator::operator !=");
  if (expected_mod_count != ref_set->mod_count)
    throw ConcurrentModificationError("ArraySet::Iterator::operator !=");
  if (ref_set != rhsASI->ref_set)
    throw ComparingDifferentIteratorsError("ArraySet::Iterator::operator !=");

  return current != rhsASI->current;
}


template<class T>
T& ArraySet<T>::Iterator::operator *() const {
  if (expected_mod_count != ref_set->mod_count)
    throw ConcurrentModificationError("ArraySet::Iterator::operator *");
  if (!can_erase || current < 0 || current >= ref_set->used) {
    std::ostringstream where;
    where << current << " when size = " << ref_set->size();
    throw IteratorPositionIllegal("ArraySet::Iterator::operator * Iterator illegal: "+where.str());
  }

  return ref_set->set[current];
}


template<class T>
T* ArraySet<T>::Iterator::operator ->() const {
  if (expected_mod_count != ref_set->mod_count)
    throw ConcurrentModificationError("ArraySet::Iterator::operator ->");
  if (!can_erase || current < 0 || current >= ref_set->used) {
    std::ostringstream where;
    where << current << " when size = " << ref_set->size();
    throw IteratorPositionIllegal("ArraySet::Iterator::operator -> Iterator illegal: "+where.str());
  }

  return &ref_set->set[current];
}


}

#endif /* ARRAY_SET_HPP_ */
