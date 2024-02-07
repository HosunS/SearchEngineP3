#ifndef DRIVER_STACK_HPP_
#define DRIVER_STACK_HPP_

#include <string>
#include <iostream>
#include <fstream>
#include "ics46goody.hpp"
#include "ics_exceptions.hpp"
#include "array_stack.hpp"


namespace ics {

typedef ics::ArrayStack<std::string> StackType;

class DriverStack {
  public:
    DriverStack(){process_commands("");}

  private:
    StackType s;

    StackType prompt_stack(std::string preface, std::string message = "  Enter element for s2") {
      StackType s2;
      for (;;) {
        std::string e = ics::prompt_string(preface + message + "(QUIT to quit)");
        if (e == "QUIT")
          break;
        s2.push(e);
      }

      return s2;
    }

    std::string menu_prompt (std::string preface) {
      std::cout << std::endl << std::endl;
      std::cout << preface+"stack s = " << s.str() << std::endl;
      std::cout << preface+"Mutators         Accessors              General" << std::endl;
      std::cout << preface+"  v  - push        m  - empty             lf - load from file"    << std::endl;
      std::cout << preface+"  V  - push_all    s  - size              l{ - load from file"    << std::endl;
      std::cout << preface+"  ^  - pop         p  - peek              it - iterator commands" << std::endl;
      std::cout << preface+"  x  - clear       <  - <<                q  - quit"              << std::endl;
      std::cout << preface+"  =  - =           r  - relations " << std::endl;

      std::string allowable[] = {"v","V","^","x","=","m","s","p","<","r","lf","l{","it","q",""};
      std::cout << std::endl;
      return ics::prompt_string(preface+"Enter stack command","",allowable);
    }

  void process_iterator_commands(StackType& s, std::string preface) {
    std::string allowable[] = {"<","e","*","+","i","c","*a","ea","f","q",""};
    StackType::Iterator i = s.begin();
    for (;;)
      try {
        std::cout << std::endl;
        std::cout << preface+"i = " << i.str() << std::endl;
        std::string i_command = ics::prompt_string(preface+
            "Enter iterator command(<[<]/e[rase]/*/+[+i]/i[++]/c[ommands]/*a[ll]/ea[ll]/f[or]/q[uit])","",allowable);
        if (i_command == "<")
          std::cout << preface +" << = " << i << std::endl;
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
          for (; i != s.end(); ++i)
            std::cout << preface+"  *(all) = " << *i << std::endl;
          std::cout << preface+"  finally i = " << i << std::endl;
        }
        else if (i_command == "ea") {
          std::cout << preface+"  initially i = " << i << std::endl;
         for (; i != s.end(); ++i)
            std::cout << preface+"  erase(all) = " << i.erase() << std::endl;
          std::cout << preface+"  finally i = " << i << std::endl;
        }
        else if (i_command == "f") {
          for (auto v : s)
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

      if (command == "v") {
        std::string e = ics::prompt_string(preface+"  Enter element to add");
        std::cout << preface+"  push = " << s.push(e) << std::endl;
      }
      else if (command == "V") {
        StackType s2(prompt_stack(preface));
        std::cout << "  push_all = " << s.push_all(s2) << std::endl;;
      }
      else if (command == "^")
        std::cout << preface+"  pop = " << s.pop() << std::endl;

      else if (command == "x")
        s.clear();

      else if (command == "=") {
        StackType s2(prompt_stack(preface));
        s = s2;
        std::cout << "  s now = " << s << std::endl;
      }

      else if (command == "m")
        std::cout << preface+"  empty = " << s.empty();

      else if (command == "s")
        std::cout << preface+"  size = " << s.size() << std::endl;


      else if (command == "p") {
        std::cout << preface+"  peek = " << s.peek() << std::endl;
      }

      else if (command == "<")
        std::cout << preface+"  << = " << s << std::endl;

      else if (command == "r") {
        std::cout << preface+"  s == s = " << (s == s) << std::endl;
        std::cout << preface+"  s != s = " << (s != s) << std::endl;

        StackType s2(prompt_stack(preface));
        std::cout << preface+"  s = " << s << " ?? s2 = " << s2 << std::endl;
        std::cout << preface+"  s == s2 = " << (s == s2) << std::endl;
        std::cout << preface+"  s != s2 = " << (s != s2) << std::endl;
      }

      else if (command == "lf") {
        std::ifstream in_stack;
        ics::safe_open(in_stack,preface+"  Enter file name to read", "loadstack.txt");
        std::string e;
        while (getline(in_stack,e))
          s.push(e);
        in_stack.close();
      }

      else if (command == "l{")
        s = StackType{"c","b","d","e","a"};


      else if (command == "it")
        process_iterator_commands(s, "it:  "+preface);

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

#endif /* DRIVER_STACK_HPP_ */

