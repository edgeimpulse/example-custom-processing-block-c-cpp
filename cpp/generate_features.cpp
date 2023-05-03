#include "rms.h"
#include <vector>

float generate_features_cpp(const std::vector<float>& signal, float scale) {
    std::vector<float> temp(signal.size());
    int i=0;
    for(auto& s : signal) {
        temp[i++] = s * scale;
    }
    return rms(temp.data(), temp.size());
}
