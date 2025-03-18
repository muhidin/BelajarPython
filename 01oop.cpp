#include <iostream>
using namespace std;

// Membuat kelas Mobil
class Mobil {
public:
    string warna;
    int tahun;

    void tampilkanInfo() {
        cout << "Warna: " << warna << endl;
        cout << "Tahun: " << tahun << endl;
    }
};

// Membuat objek dari kelas Mobil
int main() {
    Mobil mobilA;
    mobilA.warna = "Merah";
    mobilA.tahun = 2020;
    mobilA.tampilkanInfo();
    return 0;
}