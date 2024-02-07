#ifndef ICS46GOODY_HPP_
#define ICS46GOODY_HPP_

#include <string>
#include <iostream>
#include <sstream>
#include <limits>
#include <vector>
#include <cstdlib>

namespace ics {

template <typename T>
std::string to_string(T item) {
  std::stringstream stream;
  stream << item;
  return stream.str();
}

std::vector<std::string> split(const std::string& s, const std::string& pat);

std::string join(const std::vector<std::string>& s, const std::string& pat = "");

std::string prompt_string(std::string prompt,
                          std::string default_value = "",
                          std::string allowable[] = NULL);

bool prompt_bool(std::string prompt,
                 int default_value = 2/*not 0 or 1*/);

int prompt_int(std::string prompt,
               int         default_value = std::numeric_limits<int>::max());

void safe_open(std::ifstream& f, const std::string& prompt, const std::string& default_name);

int rand_range(int low, int high);

}

#endif /* ICS46GOODY_HPP_ */
