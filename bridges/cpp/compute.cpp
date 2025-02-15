#include <iostream>
extern "C" {
    void compute() {
        std::cout << "Hello from C++! Optimized calculations active." << std::endl;
    }
}
