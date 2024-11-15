#include <iostream>

void stupid_loading_bar(size_t loading_percent) {
    if (loading_percent < 20) {
        std::cout << "=========== " << 20 << "% ===========" << std::endl;
    } else if (loading_percent < 40) {
        std::cout << "=========== " << 40 << "% ===========" << std::endl;
    } else if (loading_percent < 60) {
        std::cout << "=========== " << 60 << "% ===========" << std::endl;
    } else if (loading_percent < 80) {
        std::cout << "=========== " << 80 << "% ===========" << std::endl;
    } else {
        std::cout << "=========== " << 100 << "% ===========" << std::endl;
    }
}

int main() {
    std::cout << "Hello, World!" << std::endl;
    stupid_loading_bar(50);
    return 0;
}
