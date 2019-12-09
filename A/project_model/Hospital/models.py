from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 12)
    bidang = models.CharField(max_length = 255)
    jadwal_praktek = models.CharField(max_length = 255)

    def __str__(self):
        return "Doctor name: %s, Phone: %s, Field: %s, Schedule: %s" % (self.nama, self.nomor_telepon, self.bidang, self.jadwal_praktek)

class Pasien(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 12)
    alamat = models.CharField(max_length = 255)
    keluhan = models.CharField(max_length = 255)

    def __str__(self):
        return "Medical patient name: %s , Phone: %s, Address: %s, Lamentation: %s" % (self.nama, self.nomor_telepon, self.alamat, self.keluhan)

class Resep(models.Model):
    nama = models.CharField(max_length = 255)
    total_harga = models.IntegerField(default = 0)
    kumpulan_obat = models.CharField(max_length = 255)

    def __str__(self):
        return "Recipe name: %s , Total Price: %d, Set of medicine: %s" % (self.nama, self.total_harga, self.kumpulan_obat)

class Obat(models.Model):
    nama = models.CharField(max_length = 255)
    kandungan = models.CharField(max_length = 255)
    khasiat = models.CharField(max_length = 255)

    def __str__(self):
        return "Medicine name: %s , Potion: %s, Use: %s" % (self.nama, self.kandungan, self.khasiat)