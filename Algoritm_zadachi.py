
# задание 1

# class Student:
#     def __init__(self, name, age, average_grade):
#         self.name = name
#         self.age = age
#         self.average_grade = average_grade
#     def poluchit_imya(self):
#         return self.name
#     def ustanovit_imya(self, novoje_imya):
#         self.name = novoje_imya
#     def poluchit_vozrast(self):
#         return self.age
#     def ustanovit_vozrast(self, novy_vozrast):
#         self.age = novy_vozrast
#     def poluchit_srednij_ball(self):
#         return self.average_grade
#     def ustanovit_srednij_ball(self, novy_srednij_ball):
#         self.average_grade = novy_srednij_ball
#


# задание 2

# class Pryamougolnik:
#     def __init__(self, dlina, shirina):
#         self.dlina = dlina
#         self.shirina = shirina
#     def ploshchad(self):
#         return self.dlina * self.shirina
#     def perimetr(self):
#         return 2 * (self.dlina + self.shirina)



# задание 3

# class Automobil:
#     def __init__(self, marka, model, god_vypuska, probeg):
#         self.marka = marka
#         self.model = model
#         self.god_vypuska = god_vypuska
#         self.probeg = probeg
#     def izmenit_marku(self, novaia_marka):
#         self.marka = novaia_marka
#     def poluchit_marku(self):
#         return self.marka
#     def izmenit_model(self, novaia_model):
#         self.model = novaia_model
#     def poluchit_model(self):
#         return self.model
#     def izmenit_god_vypuska(self, novyi_god_vypuska):
#         self.god_vypuska = novyi_god_vypuska
#     def poluchit_god_vypuska(self):
#         return self.god_vypuska
#     def izmenit_probeg(self, novyi_probeg):
#         self.probeg = novyi_probeg
#     def poluchit_probeg(self):
#         return self.probeg




# задание 4

# class BankovskiySchet:
#     def __init__(self, klient, balans=0):
#         self.klient = klient
#         self.balans = balans
#         self.operacii = []
#     def poluchit_informaciyu(self):
#         return f"Klient: {self.klient}, Balans: {self.balans}"
#     def popolnenie(self, suma):
#         self.balans += suma
#         self.operacii.append(f"Popolnenie: +{suma}")
#     def snyatie(self, suma):
#         if self.balans >= suma:
#             self.balans -= suma
#             self.operacii.append(f"Snyatie: -{suma}")
#         else:
#             self.operacii.append("Nedostatochno sredstv")
#     def poluchit_operacii(self):
#         return self.operacii




# задание 5

# class Treugolnik:
#     def __init__(self, storona_a, storona_b, storona_c):
#         self.storona_a = storona_a
#         self.storona_b = storona_b
#         self.storona_c = storona_c
#     def opredelit_tip(self):
#         if self.storona_a == self.storona_b == self.storona_c:
#             return "Ravnostoronnii treugolnik"
#         elif self.storona_a == self.storona_b or self.storona_b == self.storona_c or self.storona_a == self.storona_c:
#             return "Ravnobedrennii treugolnik"
#         else:
#             return "Raznostoronnii treugolnik"
#     def vychislit_ploshchad(self):
#         s = (self.storona_a + self.storona_b + self.storona_c) / 2
#         ploshchad = (s * (s - self.storona_a) * (s - self.storona_b) * (s - self.storona_c)) ** 0.5
#         return ploshchad



