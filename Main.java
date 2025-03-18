// Membuat kelas Mobil
class Mobil {
    String warna;
    int tahun;

    void tampilkanInfo() {
        System.out.println("Warna: " + warna);
        System.out.println("Tahun: " + tahun);
    }
}

// Membuat objek dari kelas Mobil
public class Main {
    public static void main(String args[]){
        Mobil mobilA = new Mobil();
        mobilA.warna = "Merah";
        mobilA.tahun = 2020;
        mobilA.tampilkanInfo();
    }
}