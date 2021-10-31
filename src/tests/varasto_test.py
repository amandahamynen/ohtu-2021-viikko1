import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.neg_varasto = Varasto(-5, -10)
        self.saldo_enemman_kuin_tilavuus_varasto = Varasto(10, 20)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_varaston_tilavuus_on_nolla(self):
        self.assertAlmostEqual(self.neg_varasto.tilavuus, 0.0)

    def test_negatiivinen_varaston_alkusaldo(self):
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_lisaa_varastoon_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-100)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), self.varasto.tilavuus)

    def test_varaston_saldo_enemman_kuin_tilavuus(self):
        saldo = self.saldo_enemman_kuin_tilavuus_varasto.saldo
        self.assertAlmostEqual(self.saldo_enemman_kuin_tilavuus_varasto.saldo, saldo)

    def test_varastoon_lisaaminen_jos_ei_tarpeeksi_tilaa(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivisen_maaran_ottaminen_palauttaa_oikean_maaran(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-10), 0.0)

    def test_ottaminen_enemman_kuin_on_saldoa(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(saatu_maara, 5)

    def test_palauttaa_oikean_tekstin(self):
        # Käytetään varastoa, jossa saldoa on 0.0 ja tilaa 10
        oikea = f"saldo = 0, vielä tilaa 10" 
        teksti = str(self.varasto)
        self.assertAlmostEqual(teksti, oikea)