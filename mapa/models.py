from __future__ import unicode_literals

# Create your models here.
from django.contrib.gis.db import models


class CdmxManzanas (models.Model):
    # mapeo de shapefiles a campos utiliables por django

    cvegeo = models.CharField(max_length=16)
    pob1 = models.IntegerField('poblacion 1')
    pob2 = models.IntegerField('poblacion 2')
    pob2R = models.FloatField('poblacion 2 real')
    pob3 = models.IntegerField('poblacion 3')
    pob3R = models.FloatField('poblacion 3 real')
    pob4 = models.IntegerField('poblacion 4')
    pob4R = models.FloatField('poblacion 4 real')
    pob5 = models.IntegerField('poblacion 5')
    pob5R = models.FloatField('poblacion 5 real')
    pob6 = models.IntegerField('poblacion 6')
    pob6R = models.FloatField('poblacion 6 real')
    pob7 = models.IntegerField('poblacion 7')
    pob7R = models.FloatField('poblacion 7 real')
    pob8 = models.IntegerField('poblacion 8')
    pob8R = models.FloatField('poblacion 8 real')
    pob9 = models.IntegerField('poblacion 9')
    pob9R = models.FloatField('poblacion 9 real')
    pob10 = models.IntegerField('poblacion 10')
    pob10R = models.FloatField('poblacion 10 real')
    pob11 = models.IntegerField('poblacion 11')
    pob11R = models.FloatField('poblacion 11 real')
    pob12 = models.IntegerField('poblacion 12')
    pob12R = models.FloatField('poblacion 12 real')
    pob13 = models.IntegerField('poblacion 13')
    pob13R = models.FloatField('poblacion 13 real')
    pob14 = models.IntegerField('poblacion 14')
    pob14R = models.FloatField('poblacion 14 real')
    pob15 = models.IntegerField('poblacion 15')
    pob15R = models.FloatField('poblacion 15 real')
    pob16 = models.IntegerField('poblacion 16')
    pob16R = models.FloatField('poblacion 16 real')
    pob17 = models.IntegerField('poblacion 17')
    pob17R = models.FloatField('poblacion 17 real')
    pob18 = models.IntegerField('poblacion 18')
    pob18R = models.FloatField('poblacion 18 real')
    pob19 = models.IntegerField('poblacion 19')
    pob19R = models.FloatField('poblacion 19 real')
    pob20 = models.IntegerField('poblacion 20')
    pob20R = models.IntegerField('poblacion 20 real')
    pob21 = models.IntegerField('poblacion 21')
    pob21R = models.FloatField('poblacion 21 real')
    pob22 = models.IntegerField('poblacion 22')
    pob22R = models.FloatField('poblacion 22 real')
    pob23 = models.IntegerField('poblacion 23')
    pob23R = models.FloatField('poblacion 23 real')
    pob24 = models.IntegerField('poblacion 24')
    pob24R = models.FloatField('poblacion 24 real')
    pob25 = models.IntegerField('poblacion 25')
    pob25R = models.FloatField('poblacion 25 real')
    pob26R = models.FloatField('poblacion 26 real')
    pob27R = models.FloatField('poblacion 27 real')
    pob28R = models.FloatField('poblacion 28 real')
    pob29R = models.FloatField('poblacion 29 real')
    pob30R = models.IntegerField('poblacion 30 real')
    pob31 = models.IntegerField('poblacion 31')
    pob31R = models.FloatField('poblacion 31 real')
    pob32 = models.IntegerField('poblacion 32')
    pob32R = models.FloatField('poblacion 32real')
    pob33 = models.IntegerField('poblacion 33')
    pob33R = models.FloatField('poblacion 33 real')
    pob34 = models.IntegerField('poblacion 34')
    pob34R = models.FloatField('poblacion 34 real')
    pob35 = models.IntegerField('poblacion 35')
    pob35R = models.FloatField('poblacion 35 real')
    pob36 = models.IntegerField('poblacion 36')
    pob36R = models.FloatField('poblacion 36 real')
    pob37 = models.IntegerField('poblacion 37')
    pob37R = models.FloatField('poblacion 37 real')
    pob38 = models.IntegerField('poblacion 38')
    pob38R = models.FloatField('poblacion 38 real')
    pob39 = models.IntegerField('poblacion 39')
    pob39R = models.FloatField('poblacion 39 real')
    pob40 = models.IntegerField('poblacion 40')
    pob40R = models.IntegerField('poblacion 40 real')
    pob41 = models.IntegerField('poblacion 41')
    pob41R = models.FloatField('poblacion 41 real')
    pob42 = models.IntegerField('poblacion 42')
    pob42R = models.FloatField('poblacion 42real')
    pob43 = models.IntegerField('poblacion 43')
    pob43R = models.FloatField('poblacion 43 real')
    pob44 = models.IntegerField('poblacion 44')
    pob44R = models.FloatField('poblacion 44 real')
    pob45 = models.IntegerField('poblacion 45')
    pob45R = models.FloatField('poblacion 45 real')
    pob46 = models.IntegerField('poblacion 46')
    pob46R = models.FloatField('poblacion 46 real')
    pob47 = models.IntegerField('poblacion 47')
    pob47R = models.FloatField('poblacion 47 real')
    pob48 = models.IntegerField('poblacion 48')
    pob48R = models.FloatField('poblacion 48 real')
    pob49 = models.IntegerField('poblacion 49')
    pob49R = models.FloatField('poblacion 49 real')
    pob50 = models.IntegerField('poblacion 50')
    pob50R = models.IntegerField('poblacion 50 real')
    pob40 = models.IntegerField('poblacion 40')
    pob40R = models.IntegerField('poblacion 40 real')
    pob41 = models.IntegerField('poblacion 41')
    pob41R = models.FloatField('poblacion 41 real')
    pob42 = models.IntegerField('poblacion 42')
    pob42R = models.FloatField('poblacion 42real')
    pob43 = models.IntegerField('poblacion 43')
    pob43R = models.FloatField('poblacion 43 real')
    pob44 = models.IntegerField('poblacion 44')
    pob44R = models.FloatField('poblacion 44 real')
    pob45 = models.IntegerField('poblacion 45')
    pob45R = models.FloatField('poblacion 45 real')
    pob46 = models.IntegerField('poblacion 46')
    pob46R = models.FloatField('poblacion 46 real')
    pob47 = models.IntegerField('poblacion 47')
    pob47R = models.FloatField('poblacion 47 real')
    pob48 = models.IntegerField('poblacion 48')
    pob48R = models.FloatField('poblacion 48 real')
    pob49 = models.IntegerField('poblacion 49')
    pob49R = models.FloatField('poblacion 49 real')
    pob50 = models.IntegerField('poblacion 50')
    pob50R = models.IntegerField('poblacion 50 real')
    pob51 = models.IntegerField('poblacion 51')
    pob51R = models.FloatField('poblacion 51 real')
    pob52 = models.IntegerField('poblacion 52')
    pob52R = models.FloatField('poblacion 52real')
    pob53 = models.IntegerField('poblacion 53')
    pob53R = models.FloatField('poblacion 53 real')
    pob54 = models.IntegerField('poblacion 54')
    pob54R = models.FloatField('poblacion 54 real')
    pob55 = models.IntegerField('poblacion 55')
    pob55R = models.FloatField('poblacion 55 real')
    pob56 = models.IntegerField('poblacion 56')
    pob56R = models.FloatField('poblacion 56 real')
    pob57 = models.IntegerField('poblacion 57')
    pob57R = models.FloatField('poblacion 57 real')
    pob58 = models.IntegerField('poblacion 58')
    pob58R = models.FloatField('poblacion 58 real')
    pob59 = models.IntegerField('poblacion 59')
    pob59R = models.FloatField('poblacion 59 real')
    pob60 = models.IntegerField('poblacion 60')
    pob60R = models.IntegerField('poblacion 60 real')
    pob61 = models.IntegerField('poblacion 61')
    pob61R = models.FloatField('poblacion 61 real')
    pob62 = models.IntegerField('poblacion 62')
    pob62R = models.FloatField('poblacion 62real')
    pob63 = models.IntegerField('poblacion 63')
    pob63R = models.FloatField('poblacion 63 real')
    pob64 = models.IntegerField('poblacion 64')
    pob64R = models.FloatField('poblacion 64 real')
    pob65 = models.IntegerField('poblacion 65')
    pob65R = models.FloatField('poblacion 65 real')
    pob66 = models.IntegerField('poblacion 66')
    pob66R = models.FloatField('poblacion 66 real')
    pob67 = models.IntegerField('poblacion 67')
    pob67R = models.FloatField('poblacion 67 real')
    pob68 = models.IntegerField('poblacion 68')
    pob68R = models.FloatField('poblacion 68 real')
    pob69 = models.IntegerField('poblacion 69')
    pob69R = models.FloatField('poblacion 69 real')
    pob70 = models.IntegerField('poblacion 70')
    pob70R = models.IntegerField('poblacion 70 real')
    pob71 = models.IntegerField('poblacion 71')
    pob71R = models.FloatField('poblacion 71 real')
    pob72 = models.IntegerField('poblacion 72')
    pob72R = models.FloatField('poblacion 72real')
    pob73 = models.IntegerField('poblacion 73')
    pob73R = models.FloatField('poblacion 73 real')
    pob74 = models.IntegerField('poblacion 74')
    pob74R = models.FloatField('poblacion 74 real')
    pob75 = models.IntegerField('poblacion 75')
    pob75R = models.FloatField('poblacion 75 real')
    pob76 = models.IntegerField('poblacion 76')
    pob76R = models.FloatField('poblacion 76 real')
    pob77 = models.IntegerField('poblacion 77')
    pob77R = models.FloatField('poblacion 77 real')
    pob78 = models.IntegerField('poblacion 78')
    pob78R = models.FloatField('poblacion 78 real')
    pob79 = models.IntegerField('poblacion 79')
    pob79R = models.FloatField('poblacion 79 real')
    pob80 = models.IntegerField('poblacion 80')
    pob80R = models.IntegerField('poblacion 80 real')
    pob81 = models.IntegerField('poblacion 81')
    pob81R = models.IntegerField('poblacion 81 real')
    oid = models.IntegerField('pk')

    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.cvegeo

    CdmxManzanas_mapping = {
    'cvegeo' : 'CVEGEO',
    'pob1' : 'POB1',
    'pob2' : 'POB2',
    'pob2_r' : 'POB2_R',
    'pob3' : 'POB3',
    'pob3_r' : 'POB3_R',
    'pob4' : 'POB4',
    'pob4_r' : 'POB4_R',
    'pob5' : 'POB5',
    'pob5_r' : 'POB5_R',
    'pob6' : 'POB6',
    'pob6_r' : 'POB6_R',
    'pob7' : 'POB7',
    'pob7_r' : 'POB7_R',
    'pob8' : 'POB8',
    'pob8_r' : 'POB8_R',
    'pob9' : 'POB9',
    'pob9_r' : 'POB9_R',
    'pob10' : 'POB10',
    'pob10_r' : 'POB10_R',
    'pob11' : 'POB11',
    'pob11_r' : 'POB11_R',
    'pob12' : 'POB12',
    'pob12_r' : 'POB12_R',
    'pob13' : 'POB13',
    'pob13_r' : 'POB13_R',
    'pob14' : 'POB14',
    'pob14_r' : 'POB14_R',
    'pob15' : 'POB15',
    'pob15_r' : 'POB15_R',
    'pob16' : 'POB16',
    'pob16_r' : 'POB16_R',
    'pob17' : 'POB17',
    'pob17_r' : 'POB17_R',
    'pob18' : 'POB18',
    'pob18_r' : 'POB18_R',
    'pob19' : 'POB19',
    'pob19_r' : 'POB19_R',
    'pob20' : 'POB20',
    'pob20_r' : 'POB20_R',
    'pob21' : 'POB21',
    'pob21_r' : 'POB21_R',
    'pob22' : 'POB22',
    'pob22_r' : 'POB22_R',
    'pob23' : 'POB23',
    'pob23_r' : 'POB23_R',
    'pob24' : 'POB24',
    'pob24_r' : 'POB24_R',
    'pob25' : 'POB25',
    'pob25_r' : 'POB25_R',
    'pob26_r' : 'POB26_R',
    'pob27_r' : 'POB27_R',
    'pob28_r' : 'POB28_R',
    'pob29_r' : 'POB29_R',
    'pob30_r' : 'POB30_R',
    'pob31' : 'POB31',
    'pob31_r' : 'POB31_R',
    'pob32' : 'POB32',
    'pob32_r' : 'POB32_R',
    'pob33' : 'POB33',
    'pob33_r' : 'POB33_R',
    'pob34' : 'POB34',
    'pob34_r' : 'POB34_R',
    'pob35' : 'POB35',
    'pob35_r' : 'POB35_R',
    'pob36' : 'POB36',
    'pob36_r' : 'POB36_R',
    'pob37' : 'POB37',
    'pob37_r' : 'POB37_R',
    'pob38' : 'POB38',
    'pob38_r' : 'POB38_R',
    'pob39' : 'POB39',
    'pob39_r' : 'POB39_R',
    'pob40' : 'POB40',
    'pob40_r' : 'POB40_R',
    'pob41' : 'POB41',
    'pob41_r' : 'POB41_R',
    'pob42' : 'POB42',
    'pob42_r' : 'POB42_R',
    'pob43' : 'POB43',
    'pob43_r' : 'POB43_R',
    'pob44' : 'POB44',
    'pob44_r' : 'POB44_R',
    'pob45' : 'POB45',
    'pob45_r' : 'POB45_R',
    'pob46' : 'POB46',
    'pob46_r' : 'POB46_R',
    'pob47' : 'POB47',
    'pob47_r' : 'POB47_R',
    'pob48' : 'POB48',
    'pob48_r' : 'POB48_R',
    'pob49' : 'POB49',
    'pob49_r' : 'POB49_R',
    'pob50' : 'POB50',
    'pob50_r' : 'POB50_R',
    'pob51' : 'POB51',
    'pob51_r' : 'POB51_R',
    'pob52' : 'POB52',
    'pob52_r' : 'POB52_R',
    'pob53' : 'POB53',
    'pob53_r' : 'POB53_R',
    'pob54' : 'POB54',
    'pob54_r' : 'POB54_R',
    'pob55' : 'POB55',
    'pob55_r' : 'POB55_R',
    'pob56' : 'POB56',
    'pob56_r' : 'POB56_R',
    'pob57' : 'POB57',
    'pob57_r' : 'POB57_R',
    'pob58' : 'POB58',
    'pob58_r' : 'POB58_R',
    'pob59' : 'POB59',
    'pob59_r' : 'POB59_R',
    'pob60' : 'POB60',
    'pob60_r' : 'POB60_R',
    'pob61' : 'POB61',
    'pob61_r' : 'POB61_R',
    'pob62' : 'POB62',
    'pob62_r' : 'POB62_R',
    'pob63' : 'POB63',
    'pob63_r' : 'POB63_R',
    'pob64' : 'POB64',
    'pob64_r' : 'POB64_R',
    'pob65' : 'POB65',
    'pob65_r' : 'POB65_R',
    'pob66' : 'POB66',
    'pob66_r' : 'POB66_R',
    'pob67' : 'POB67',
    'pob67_r' : 'POB67_R',
    'pob68' : 'POB68',
    'pob68_r' : 'POB68_R',
    'pob69' : 'POB69',
    'pob69_r' : 'POB69_R',
    'pob70' : 'POB70',
    'pob70_r' : 'POB70_R',
    'pob71' : 'POB71',
    'pob71_r' : 'POB71_R',
    'pob72' : 'POB72',
    'pob72_r' : 'POB72_R',
    'pob73' : 'POB73',
    'pob73_r' : 'POB73_R',
    'pob74' : 'POB74',
    'pob74_r' : 'POB74_R',
    'pob75' : 'POB75',
    'pob75_r' : 'POB75_R',
    'pob76' : 'POB76',
    'pob76_r' : 'POB76_R',
    'pob77' : 'POB77',
    'pob77_r' : 'POB77_R',
    'pob78' : 'POB78',
    'pob78_r' : 'POB78_R',
    'pob79' : 'POB79',
    'pob79_r' : 'POB79_R',
    'pob80' : 'POB80',
    'pob80_r' : 'POB80_R',
    'pob81' : 'POB81',
    'pob81_r' : 'POB81_R',
    'oid' : 'OID',
    'geom' : 'MULTIPOLYGON',
}

