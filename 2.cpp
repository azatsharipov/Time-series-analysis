#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#define pb push_back
#define mp make_pair

using namespace std;

int N = 10000, a = 2, b = 1, k = 0;
vector <pair<double, double>> tim;
double delta_t = 0.01;

double ro2(int n, int nn) {
    double ret = 0;
    int mi = min(n, nn);
    mi = min(mi, k);
    for (int i = 0; i < mi; i++) {
        ret += (tim[n - k + i].first - tim[nn - k + i].first) *
               (tim[n - k + i].first - tim[nn - k + i].first) +
               (tim[n - k + i].second - tim[nn - k + i].second) *
               (tim[n - k + i].second - tim[nn - k + i].second);
    }
    return ret;
}

double tetta(double a) {
    if (a < 0)
        return 0;
    else
        return 1;
}

int main() {
    for (int i = 0; i < N; i++) {
        double t = i * delta_t;
        tim.pb(mp(a * cos(t), b * sin(t)));
    }
    for (k = 6; k < 20; k++) {
        double l = 1.0 / 128;
        vector <double> ro;
        for (int n = k; n < N; n++) {
            for (int nn = k; nn < N; nn++) {
                ro.pb(ro2(n, nn));
            }
        }
        while (l >= 1.0 / 1024) {
            double d = 0;
            double sum = 0;
            for (int n = 0; n < ro.size(); n++) {
                sum += tetta(l * l - ro[n]);
            }
            sum /= N * N;
            double c = sum;
            d = log(c) / log(l);
            cout << "l = " << l << ' ';
            cout << "k = " << k << ' ';
            cout << "c = " << c << ' ';
            cout << "d = " << d << endl;
            l /= 2;
        }
    }
    return 0;
}
