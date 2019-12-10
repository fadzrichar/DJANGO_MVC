from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 12)
    jabatan = models.CharField(max_length = 255)

    def __str__(self):
        return "Directrees name: %s, Phone: %s, Title: %s" % (self.nama, self.nomor_telepon, self.jabatan)

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 12)
    nomor_absen = models.IntegerField(default = 0)
    nilai_rata_rata = models.IntegerField(default = 0)

    def __str__(self):
        return "Mentee name: %s, Phone: %s, Number: %s, Average Score: %s" % (self.nama, self.nomor_telepon, self.nomor_absen, self.nilai_rata_rata)

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length = 255)
    jadwal_dimulai = models.CharField(max_length = 255)
    jadwal_berakhir = models.CharField(max_length = 255)

    def __str__(self):
        return "Course name: %s, Start: %s, End: %s" % (self.nama_pelajaran, self.jadwal_dimulai, self.jadwal_berakhir)

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 12)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)

    def __str__(self):
        return "Mentor name: %s, Phone: %s, Course: %s" % (self.nama, self.nomor_telepon, self.mata_pelajaran)

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length = 255)
    banyak_soal = models.IntegerField(default = 0)
    bobot_nilai = models.CharField(max_length = 4)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)

    def __str__(self):
        return "Challenge name: %s, Number of case: %d, Score weight: %s, Course: %s" % (self.nama_challenge, self.banyak_soal, self.bobot_nilai, self.mata_pelajaran)

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length = 255)
    banyak_soal = models.IntegerField(default = 0)
    bobot_nilai = models.CharField(max_length = 4)
    tanggal_pelaksanaan = models.DateTimeField('date_test')
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)

    def __str__(self):
        return "Live Code name: %s, Number of case: %d, Score weight: %s, Schedule: %s, Course: %s" % (self.nama_live_code, self.banyak_soal, self.bobot_nilai, self.tanggal_pelaksanaan, self.mata_pelajaran)