#ifndef DRIVER_PRIORITYQUEUE_HPP_
#define DRIVER_PRIORITYQUEUE_HPP_

#include <string>
#include <iostream>
#include <fstream>
#include "ics46goody.hpp"
#include "ics_exceptions.hpp"
#include "array_priority_queue.hpp"


namespace ics {

bool regular_gt(const std::string& a, const std::string& b) {return a < b;}
bool reverse_gt(const std::string& a, const std::string& b) {return a > b;}

typedef ics::ArrayPriorityQueue<std::string> PriorityQueueType;

class DriverPriorityQueue {
  public:
    DriverPriorityQueue() : q(regular_gt){
      std::string allowable[] = {"r","R",""};
      bool (*gt)(const std::string& a, const std::string& b);
      gt = (ics::prompt_string("Enter comparison for Priority Queue: r[egular] or R[everse]\n  regular means smaller values have higher priority","r",allowable) =="r" ? regular_gt : reverse_gt);
      q = PriorityQueueType(gt);
      process_commands("");
    };

  private:
    PriorityQueueType q;

    PriorityQueueType prompt_queue(std::string preface, std::string message = "  Enter element for q2") {
      PriorityQueueType q2(regular_gt);
      std::string allowable[] = {"r","R",""};
      bool (*gt)(const std::string& a, const std::string& b);
      gt = (ics::prompt_string("Enter comparison for Priority Queue: r[egular] or R[everse]\n  regular means smaller values have higher priority","r",allowable) =="r" ? regular_gt : reverse_gt);
      q2 = PriorityQueueType(gt);
      for (;;) {
        std::string e = ics::prompt_string(preface + message + "(QUIT to quit)");
        if (e == "QUIT")
          break;
        q2.enqueue(e);
      }
      return q2;
    }

    std::string menu_prompt (std::string preface) {
      std::cout << std::endl << std::endl;
      std::cout << preface+"priority queue q = " << q.str() << std::endl;
      std::cout << preface+"Mutators            Accessors              General" << std::endl;
      std::cout << preface+"  e  - enqueue        m  - empty             lf - load from file"   << std::endl;
      std::cout << preface+"  E  - enqueue_all    s  - size              l{ - load from {}"      << std::endl;
      std::cout << preface+"  d  - dequeue        p  - peek              it - iterator commands" << std::endl;
      std::cout << preface+"  x  - clear          <  - <<                q  - quit"              << std::endl;
      std::cout << preface+"  =  - =              r  - relations" << std::endl;

      std::string allowable[] = {"e","E","d","x","=","m","s","p","<","r","lf","l{","it","q",""};
      std::cout << std::endl;
      return ics::prompt_string(preface+"Enter queue command","",allowable);
    }

    void process_iterator_commands(PriorityQueueType& q, std::string preface) {
      std::string allowable[] = {"<","e","*","+","i","c","*a","ea","f","q",""};
      PriorityQueueType::Iterator i = q.begin();
      for (;;)
        try {
          std::cout << std::endl;
          std::cout << preface+"i = " << i.str() << std::endl;
          std::string i_command = ics::prompt_string(preface+
              "Enter iterator command(<[<]/e[rase]/*/+[+i]/i[++]/c[ommands]/*a[ll]/ea[ll]/f[or]/q[uit])","",allowable);
          if (i_command == "<")
            std::cout << preface+"  << = " << i << std::endl;
          else if (i_command == "e")
            std::cout << preface+"  erase = " << i.erase() << std::endl;
          else if (i_command == "*")
            std::cout << preface+"  * = " << *i << std::endl;
          else if (i_command == "+")
            std::cout << preface+"  ++i returned = " << ++i << std::endl;
          else if (i_command == "i")
            std::cout << preface+"  i++ returned = " << i++ << std::endl;
          else if (i_command == "c")
            process_commands(preface);
          else if (i_command == "*a") {
            std::cout << preface+"  initially i = " << i << std::endl;
            for (; i != q.end(); ++i)
              std::cout << preface+"  *(all) = " << *i << std::endl;
            std::cout << preface+"  finally i = " << i << std::endl;
          }
          else if (i_command == "ea") {
            std::cout << preface+"  initially i = " << i << std::endl;
           for (; i != q.end(); ++i)
              std::cout << preface+"  erase(all) = " << i.erase() << std::endl;
            std::cout << preface+"  finally i = " << i << std::endl;
          }
          else if (i_command == "f") {
            for (auto v : q)
              std::cout << preface+"  *(all) = " << v << std::endl;
          }
          else if (i_command == "q")
            break;

        } catch (ics::IcsError& e) {
          std::cout << preface+"  " << e.what() << std::endl;
        }
    };


    void process_commands(std::string preface) {
      for (;;) try {
        std::string command = menu_prompt(preface);

        if (command == "e") {
          std::string e = ics::prompt_string(preface+"  Enter element to add");
          std::cout << preface+"  enqueue = " << q.enqueue(e) << std::endl;
        }

        else if (command == "E") {
          PriorityQueueType q2(prompt_queue(preface));
          std::cout << "  dequeue = " << q.enqueue_all(q2) << std::endl;;
        }

        else if (command == "d")
          std::cout << preface+"  dequeue = " << q.dequeue() << std::endl;

        else if (command == "x")
          q.clear();

        else if (command == "=") {
          PriorityQueueType q2(prompt_queue(preface));
          q = q2;
          std::cout << "  q now = " << q << std::endl;
        }

        else if (command == "m")
          std::cout << preface+"  empty = " << q.empty();

        else if (command == "s")
          std::cout << preface+"  size = " << q.size() << std::endl;


        else if (command == "p") {
          std::cout << preface+"  peek = " << q.peek() << std::endl;
        }

        else if (command == "<")
          std::cout << preface+"  << = " << q << std::endl;

        else if (command == "r") {
          std::cout << preface+"  q == q = " << (q == q) << std::endl;
          std::cout << preface+"  q != q = " << (q != q) << std::endl;

          PriorityQueueType q2(prompt_queue(preface));
          std::cout << preface+"  q = " << q << " ?? q2 = " << q2 << std::endl;
          std::cout << preface+"  q == q2 = " << (q == q2) << std::endl;
          std::cout << preface+"  q != q2 = " << (q != q2) << std::endl;
        }

        else if (command == "lf") {
          std::ifstream in_queue;
          ics::safe_open(in_queue,preface+"  Enter file name to read", "loadpq.txt");
          std::string e;
          while (getline(in_queue,e))
            q.enqueue(e);
          in_queue.close();
        }

        else if (command == "l{") {
          q = PriorityQueueType({"c","b","d","e","a"},regular_gt);
        }

        else if (command == "it")
          process_iterator_commands(q, "it:  "+preface);

        else if (command == "q")
          break;

        else
          std::cout << preface+"\""+command+"\" is unknown command" << std::endl;

      } catch (ics::IcsError& e) {
        std::cout << preface+"  " << e.what() << std::endl;
      }

    };

};

}

#endif /* DRIVER_PRIORITYQUEUE_HPP_ */
