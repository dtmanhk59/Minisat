#include <iostream>
#include <algorithm>
#include <set>
#include <iterator>

std::set<int> compact(std::set<int> vars) {
  const int TRUE = 1;
  const int FALSE = -1;
  auto it = std::find(vars.begin(), vars.end(), TRUE);
  if (it != vars.end()) {
    vars.clear();
    vars.insert(TRUE);
    return vars;
  }
  vars.erase(FALSE);
  if (vars.empty()) {
    vars.insert(FALSE);
    return vars;
  }

  for (int var : vars) {
    auto it = std::find_if(vars.begin(), vars.end(), [var](int v) {
      return (var + v == 0);
    });
    if (it != vars.end()) {
      vars.clear();
      vars.insert(TRUE);
      return vars;
    }
  }
  return vars;
}

int main() {
  std::set<int> v = {9, 4, -4, 4, 5};
  std::set<int> r = compact(v);
  for (int x : r) {
    std::cout << x << std::endl;
  }
}
