from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length = 255)
    species = models.CharField(max_length = 12)
    berat = models.IntegerField(default = 0)
    umur = models.IntegerField(default = 0)

    def __str__(self):
        return "Animal name: %s, Species: %s, Weight: %d kg, Age: %d" % (self.nama, self.species, self.berat, self.umur)

class Kandang(models.Model):
    nama = models.CharField(max_length = 255)
    isi_kandang = models.CharField(max_length = 255)
    luas_kandang = models.CharField(max_length = 255)

    def __str__(self):
        return "Cage name: %s, Species: %s, Area: %s" % (self.nama, self.isi_kandang, self.luas_kandang)

class Penjaga(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 12)
    jadwal_jaga = models.CharField(max_length = 255)

    def __str__(self):
        return "Guide name: %s, Phone: %s, Schedule: %s" % (self.nama, self.nomor_telepon, self.jadwal_jaga)
    
class Pengunjung(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 12)
    hari_berkunjung = models.CharField(max_length = 255)

    def __str__(self):
        return "Guest name: %s, Phone: %s, Trip: %s" % (self.nama, self.nomor_telepon, self.hari_berkunjung)