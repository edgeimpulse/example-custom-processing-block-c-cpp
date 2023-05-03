#pragma once

#include <cmath>

float rms(const float* signal, int signal_size)
{
    float sum = 0.0f;
    for (int i = 0; i < signal_size; ++i)
    {
        sum += signal[i] * signal[i];
    }
    return sqrtf(sum / signal_size);
}