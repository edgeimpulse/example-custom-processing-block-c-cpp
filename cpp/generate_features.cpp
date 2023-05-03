#include "rms.h"
#include <vector>

float generate_features_cpp(const std::vector<float>& signal) {
    return rms(signal.data(), signal.size());
}
