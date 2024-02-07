#ifndef PAIR_HPP_
#define PAIR_HPP_


#include <iostream>

namespace ics {

template<class F,class S>
class pair {
  public:
    pair(){}
    pair(const F& f,const S& s) : first(f), second(s) {/*first = f; second = s; std::cout << "in pair:" << first << "/" << second << std::endl;*/}
    virtual ~pair(){}
      F first;
      S second;
      bool operator == (const pair<F,S>& rhs) const {return first == rhs.first && second == rhs.second;}
      bool operator != (const pair<F,S>& rhs) const {return !(*this==rhs);}

      template<class F2,class S2>
      friend std::ostream& operator << (std::ostream& outs, const pair<F2,S2>& p);
};

template<class F,class S>
pair<F,S> make_pair(F f, S s){return pair<F,S>(f,s);}

template<class F,class S>
std::ostream& operator << (std::ostream& outs, const pair<F,S>& p){
   outs << "pair[" << p.first << "," << p.second << "]";
   return outs;
}

}

#endif /* PAIR_HPP_ */
