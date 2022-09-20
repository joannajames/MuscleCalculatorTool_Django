import pandas as pd
from math import nan
import numpy as np

global Level_Dict
global Male_CSA_Co
global Male_CSA_LSM
global Male_Dist_Co
global Male_Dist_LSM
global Male_Angle_Co
global Male_Angle_LSM
global Female_CSA_Co
global Female_CSA_LSM
global Female_Dist_Co
global Female_Dist_LSM
global Female_Angle_Co
global Female_Angle_LSM
Level_Dict={'T4':1,'T5':2,'T6':3,'T7':4,'T8':5,'T9':6,'T10':7,'T11':8,'T12':9,'L1':10,'L2':11,'L3':12,'L4':13}
Male_CSA_Co=pd.DataFrame(np.array([[-28.21,62.21,4.55,14.71,-1.49,-0.04,-0.99,-835.33],
                [-8.50,-155.29,0.24,-11.76,1.01,9.84,-0.41,1729.48],
                [-8.57,-443.94,0.22,-31.62,5.36,41.54,-5.83,2446.38],
                [-6.12,27.35,0.65,-1.11,0.02,6.96,-0.82,-32.75],
                [-13.52,-44.26,0.81,-5.42,0.35,13.04,-0.83,694.08],
                [-0.13,-232.07,-0.30,-18.42,1.25,5.46,0.41,2722.36],
                [21.50,-614.63,-1.98,-71.64,5.40,38.96,-2.22,7649.24],
                [27.07,-101.50,-2.99,-0.60,0.16,-28.80,3.08,827.11],
                [-0.63,-108.43,-1.11,-1.13,0.45,0.64,1.16,170.00],
                [-0.80,-30.76,-0.27,0.20,0.19,-0.07,0.16,20.15],
                [21.32,-142.14,-2.25,-14.64,1.35,-3.01,0.57,1458.75]]),
                columns=['Age','Level','AgexLevel','Height','HeightxLevel','Weight','WeightxLevel','Const'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])
    
Male_CSA_LSM=pd.DataFrame(np.array([[1670.373045,1333.657156,1021.25513,749.4956466,474.5247259,340.6950686,nan,nan,nan,nan,nan,nan,nan],
            [nan,nan,nan,nan,nan,nan,552.095774,650.314508,697.1581768,695.6789,707.5255724,749.4565395,722.0569843],
            [nan,nan,1059.208275,1461.008095,1629.498444,1458.179407,918.7291834,342.5930435,nan,nan,nan,nan,nan],
            [746.3405721,784.0976046,734.1346722,533.872109,350.7600776,213.6756302,118.1984143,nan,nan,nan,nan,nan,nan],
            [858.497639,901.7732072,1012.792737,1274.810679,1421.152763,1282.441746,1187.469739,1015.414134,848.2715969,664.5855462,429.78116,175.2680404,nan],
            [nan,nan,nan,nan,nan,nan,255.8744475,434.1006322,753.7349764,920.936174,1094.60919,1258.7054,1172.407081],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,678.8412991,1150.820259,1145.264266],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,317.5176904,714.929898,1170.25549,1563.559695],
            [421.1624814,439.1655178,486.1562631,577.5192054,627.596615,713.0572217,908.8183983,1211.812588,1602.383841,2058.463461,2202.493772,1970.094304,1427.525082],
            [304.9744168,304.7299142,293.8097566,280.2732296,279.4288173,289.2835472,316.0280062,300.1859251,276.9793908,311.7077524,392.6220743,565.3962456,862.704528],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,233.5850593,412.3857959,617.7514383,691.9823618]]),
            columns=['T4','T5','T6','T7','T8','T9','T10','T11','T12','L1','L2','L3','L4'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])

Male_Dist_Co=pd.DataFrame(np.array([[-1.70,0.05,0.01,-0.03,0.54,0.06,-61.52,0.65],
            [8.22,-0.01,-0.10,-0.06,0.69,0.04,-80.92,0.70],
            [6.27,0.03,0.41,-0.06,0.31,0.02,-92.45,0.50],
            [1.15,0.01,0.10,-0.01,0.20,0.00,-25.71,0.66],
            [-4.04,0.05,0.03,0.02,0.51,-0.03,-18.46,0.89],
            [3.43,-0.02,-0.08,-0.01,0.78,-0.01,-84.01,0.82],
            [9.70,0.03,0.99,-0.10,-0.28,0.08,-153.44,0.62],
            [3.25,-0.01,0.40,-0.03,-0.24,0.03,-57.90,0.86],
            [-1.83,0.00,0.08,0.01,0.11,0.00,-21.83,0.79],
            [-0.91,0.01,0.13,0.00,0.01,0.01,-21.41,0.84],
            [-5.90,0.02,-0.23,0.05,0.42,-0.03,8.07,0.79]]),
            columns=['Age','Level','AgexLevel','Height','HeightxLevel','Weight','WeightxLevel','Const'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])

Male_Dist_LSM=pd.DataFrame(np.array([[143.1085069,152.9887744,163.696758,171.3859168,176.1977305,178.4008729,nan,nan,nan,nan,nan,nan,nan],
            [nan,nan,nan,nan,nan,nan,181.9195,177.1990905,174.2463799,164.8359591,151.7198809,138.1351691,127.1588768],
            [nan,nan,149.9024154,154.6553678,158.4744315,159.11021,163.5952224,165.3606668,nan,nan,nan,nan,nan],
            [77.3968335,76.42646828,72.83380049,67.78549032,64.86186411,64.39853057,64.90402944,nan,nan,nan,nan,nan,nan],
            [179.7303825,176.4905909,171.8093651,157.0614743,140.4807591,132.1202938,125.4804611,120.0878296,119.2623476,118.8383442,116.989204,115.4359392,nan],
            [nan,nan,nan,nan,nan,nan,186.6559566,181.8781059,172.4715284,163.3971385,151.8564596,144.3599246,141.0620024],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,156.2371007,138.6600456,135.6414296],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,28.77310101,35.32889761,40.61273972,45.8022851],
            [56.95707046,57.41858569,59.41972162,62.36931864,64.77540444,66.31243739,68.52169409,68.31248138,70.00405381,73.64357242,74.78783326,75.15351803,71.52234999],
            [42.50730956,42.06513142,41.86523991,42.59913579,43.83724234,45.35814637,45.87898468,46.00503758,47.436854,49.89092111,53.63865543,57.28402597,63.02861495],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,53.80281446,65.18938505,76.42371892,80.51018388]]),
            columns=['T4','T5','T6','T7','T8','T9','T10','T11','T12','L1','L2','L3','L4'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])

Male_Angle_Co=pd.DataFrame(np.array([[0.09,-2.85,0.00,-0.22,0.04,0.26,-0.04,11.35],
            [0.03,1.25,-0.01,-0.01,0.00,0.08,-0.01,-7.01],
            [0.02,1.23,0.01,-0.01,-0.01,0.10,-0.01,-7.12],
            [-0.06,0.57,0.02,0.03,-0.01,0.04,-0.01,-4.14],
            [-0.02,1.23,0.00,0.14,-0.01,-0.12,0.01,-11.52],
            [0.28,3.39,-0.03,0.17,-0.01,-0.06,0.00,-41.53],
            [0.10,17.48,-0.01,1.86,-0.15,-1.36,0.11,-211.62],
            [-0.20,-8.19,0.01,-0.76,0.05,0.24,-0.01,121.92],
            [0.09,0.81,-0.01,0.00,0.00,0.03,0.00,-8.25],
            [0.00,-0.54,0.00,-0.03,0.00,0.00,0.00,4.46],
            [0.00,1.02,-0.01,-0.11,0.00,0.17,-0.01,3.62]]),            
            columns=['Age','Level','AgexLevel','Height','HeightxLevel','Weight','WeightxLevel','Const'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])

Male_Angle_LSM=pd.DataFrame(np.array([[150.2690903,153.2974339,156.145685,157.708062,157.6500866,157.9116845,nan,nan,nan,nan,nan,nan,nan],
            [nan,nan,nan,nan,nan,nan,162.5236529,163.5646204,162.0070889,159.8639917,157.590113,156.5372704,155.895616],
            [nan,nan,113.0815416,113.0932069,112.6234935,110.1897183,111.1045748,109.8682262,nan,nan,nan,nan,nan],
            [36.98504471,40.1278642,39.24242304,33.35589162,27.31508961,22.91805415,19.65604459,nan,nan,nan,nan,nan,nan],
            [103.8662768,103.3157475,100.6994615,95.15640863,89.67228511,85.61102154,81.98412606,77.44926081,73.43035245,69.25870656,66.42750523,67.58531975,nan],
            [nan,nan,nan,nan,nan,nan,138.9044781,133.2083181,122.8203146,115.9853515,107.3506762,100.2655076,100.8635635],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,115.8467402,105.3082205,107.8326474],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,77.04390908,79.19759922,83.94031754,91.16296112],
            [38.62710406,39.80686755,41.46041416,42.7312211,42.77631461,41.59585603,41.44683338,40.34866557,39.74062679,39.89593535,38.66382126,37.69571244,40.26742185],
            [17.31576977,17.59302821,17.4607557,16.38563837,15.24966712,14.47195392,14.01092657,13.71326439,12.7126482,12.5524731,13.05181857,14.50003158,17.20161958],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,56.76885304,59.08550069,62.2524915,65.90238805]]),
            columns=['T4','T5','T6','T7','T8','T9','T10','T11','T12','L1','L2','L3','L4'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])

Female_CSA_Co=pd.DataFrame(np.array([[-12.86,-96.42,2.13,2.57,0.15,2.48,-0.87,210.98],
            [-3.75,-121.41,-0.09,-9.98,0.97,8.29,-0.39,1234.37],
            [-5.14,-297.86,0.37,-19.37,3.25,26.06,-3.42,1556.48],
            [-4.48,38.74,0.65,-0.77,-0.10,5.83,-0.88,-22.86],
            [-6.82,32.35,0.30,0.35,-0.15,7.39,-0.37,-156.56],
            [0.05,-157.51,-0.25,-10.95,0.86,1.81,0.54,1586.50],
            [5.13,-243.32,-0.48,-21.52,1.59,1.41,0.54,2788.45],
            [6.49,-264.26,-0.78,-14.13,1.27,-14.69,1.60,2844.54],
            [-0.48,-97.43,-0.52,-2.22,0.40,0.28,0.94,357.02],
            [0.06,16.39,-0.23,1.63,-0.11,-0.25,0.22,-247.17],
            [10.59,-22.70,-1.11,-4.75,0.36,-3.30,0.51,315.19]]),
            columns=['Age','Level','AgexLevel','Height','HeightxLevel','Weight','WeightxLevel','Const'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])

Female_CSA_LSM=pd.DataFrame(np.array([[906.6400967,735.2392406,594.36956,451.7387179,305.8756496,196.7377209,nan,nan,nan,nan,nan,nan,nan],
            [nan,nan,nan,nan,nan,nan,325.6700931,429.6691786,463.5598503,501.8659495,458.3581655,478.0237924,445.3868613],
            [nan,nan,536.0413294,795.683821,981.6789555,961.1736139,662.241186,288.4090965,nan,nan,nan,nan,nan],
            [478.6570832,496.7658973,457.5073843,341.8184914,230.9734128,144.1692174,83.41328887,nan,nan,nan,nan,nan,nan],
            [520.1571725,555.5465557,619.0673192,773.4268014,860.7407216,778.5796006,719.5979255,626.6249558,534.8226517,411.2722211,257.6646758,111.2416265,nan],
            [nan,nan,nan,nan,nan,nan,130.8522463,236.5951186,462.3982958,614.3194591,692.5494555,761.6775797,742.0611663],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,454.7369012,663.6505256,720.9063802],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,191.9264011,399.4956763,663.2598603,918.6406192],
            [304.3914413,318.2826795,346.8365779,395.5541917,423.4424459,486.0002984,647.2518784,850.888777,1059.083706,1405.054894,1472.609998,1379.786189,1099.453626],
            [231.670177,232.8123792,221.8621744,210.9566558,209.2217713,218.4458389,240.982265,233.7972453,205.0048898,213.5355022,270.4060702,409.0802286,664.9537474],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,158.3661052,245.3793853,338.2142465,461.8349588]]),
            columns=['T4','T5','T6','T7','T8','T9','T10','T11','T12','L1','L2','L3','L4'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])

Female_Dist_Co=pd.DataFrame(np.array([[0.18,1.15,0.02,-0.05,-0.02,0.53,0.02,-42.93],
            [-0.11,1.46,0.05,0.04,-0.06,0.34,0.06,-23.98],
            [-0.03,3.30,0.01,0.41,-0.04,0.21,0.04,-79.97],
            [-0.08,2.35,0.02,0.21,-0.02,0.12,0.00,-37.04],
            [-0.28,-2.79,0.03,0.22,0.00,0.28,0.00,-36.19],
            [-0.12,-6.29,0.03,-0.23,0.02,0.47,0.02,6.98],
            [-0.41,-3.44,0.06,-0.36,0.03,1.25,-0.04,-26.21],
            [0.00,-1.86,0.01,0.02,0.00,-0.07,0.01,0.55],
            [-0.02,-0.67,0.01,0.20,0.00,0.04,0.01,-33.09],
            [-0.03,-1.25,0.01,0.14,0.00,0.00,0.01,-20.74],
            [-0.25,-12.93,0.03,-0.68,0.08,0.21,-0.01,108.31]]),
            columns=['Age','Level','AgexLevel','Height','HeightxLevel','Weight','WeightxLevel','Const'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])

Female_Dist_LSM=pd.DataFrame(np.array([[122.8104218,131.8954143,140.8853551,147.3386375,150.4287216,150.7117657,nan,nan,nan,nan,nan,nan,nan],
            [nan,nan,nan,nan,nan,nan,150.9807123,146.7991123,142.7576139,134.3762062,121.4841759,109.6264842,103.6639605],
            [nan,nan,131.0917313,134.7438468,138.2093355,139.7479467,142.1983956,144.0991944,nan,nan,nan,nan,nan],
            [68.44317111,66.78821662,63.71755942,59.43388307,56.89434412,56.39934551,57.29649746,nan,nan,nan,nan,nan,nan],
            [160.7544539,159.5542799,154.7721287,142.8023802,126.527371,116.6902807,109.7534902,105.2529435,103.613203,104.0986168,103.0076472,103.8512449,nan],
            [nan,nan,nan,nan,nan,nan,159.0860856,155.2667893,147.7447929,141.4971105,132.6368139,127.1120638,127.9587202],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,135.3919683,122.4605913,122.3209444],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,24.56133183,30.13861679,35.06423992,40.30364244],
            [51.47178719,51.81260153,52.86113237,54.79060765,56.4822917,57.76043041,59.82031515,60.20097919,61.692311,65.21893617,66.46471489,68.03322177,67.20997135],
            [38.74007493,38.21489885,38.00059413,38.54959944,39.59247791,40.78541618,41.61759433,42.23793721,44.28101764,46.25296077,49.82206203,53.64063609,59.12844466],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,46.57446873,57.2323306,68.79587357,77.18718922]]),
            columns=['T4','T5','T6','T7','T8','T9','T10','T11','T12','L1','L2','L3','L4'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])

Female_Angle_Co=pd.DataFrame(np.array([[0.06,-1.38,0.00,-0.21,0.03,0.26,-0.04,11.39],
            [-0.04,0.65,0.00,0.00,-0.01,-0.01,0.00,3.08],
            [0.09,1.15,0.00,-0.13,0.00,0.12,-0.01,6.89],
            [-0.04,2.86,0.02,0.01,-0.02,0.05,-0.02,-2.03],
            [0.05,1.17,-0.01,0.09,-0.01,-0.12,0.01,-9.25],
            [0.24,1.25,-0.02,-0.04,0.00,-0.01,0.00,-7.82],
            [0.23,13.40,-0.02,1.38,-0.11,-0.98,0.08,-163.65],
            [-0.05,-9.34,0.01,-0.66,0.04,-0.23,0.03,123.49],
            [0.04,0.95,0.00,-0.01,0.00,0.01,0.00,-1.81],
            [0.02,0.78,0.00,0.03,-0.01,-0.01,0.00,-5.15],
            [0.06,-2.07,-0.01,-0.30,0.02,0.07,0.00,37.54]]),
            columns=['Age','Level','AgexLevel','Height','HeightxLevel','Weight','WeightxLevel','Const'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])
            
Female_Angle_LSM=pd.DataFrame(np.array([[147.6629189,150.6329134,153.4113689,155.2108264,156.026888,157.6577584,nan,nan,nan,nan,nan,nan,nan],
            [nan,nan,nan,nan,nan,nan,162.4900853,163.6232064,162.135297,160.0845758,156.6748297,154.1592367,152.4202281],
            [nan,nan,111.1232437,111.3762235,111.5202281,110.4106721,110.6089835,110.2708892,nan,nan,nan,nan,nan],
            [38.13584257,39.84839841,38.76883458,32.76650196,26.42089592,21.60087667,18.8177027,nan,nan,nan,nan,nan,nan],
            [103.258533,102.5353036,100.0405191,95.10626302,89.61680747,85.58424295,81.12283234,76.4998752,72.3249478,69.01072049,67.03564168,68.47693882,nan],
            [nan,nan,nan,nan,nan,nan,137.7694004,133.0298021,122.790297,115.955954,107.1103868,99.2780061,99.67595481],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,114.5741691,104.7882801,104.4806351],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,74.56258369,72.96258019,77.50635897,86.64358164],
            [38.26334756,38.79272849,40.21454139,41.28314751,41.0393823,40.16203245,40.42775203,39.25948581,37.97516686,38.42105241,37.57122048,37.69024202,42.25982688],
            [17.14291669,17.85494697,17.6941529,16.42306476,15.2752662,14.71054396,14.34118066,14.16005149,13.13671896,12.94448456,13.19715767,14.89201441,18.24014745],
            [nan,nan,nan,nan,nan,nan,nan,nan,nan,53.9331647,55.94066642,60.20296668,66.57976316]]),
            columns=['T4','T5','T6','T7','T8','T9','T10','T11','T12','L1','L2','L3','L4'],index=['PM', 'RA', 'SA', 'TR', 'LD', 'EO', 'IO', 'PS', 'ES', 'MU', 'QL'])

class Muscle:
    def __init__(self,sex,age,height,weight,musc):
        self.sex=sex
        self.age=float(age)
        self.height=float(height)
        self.weight=float(weight)
        self.musc=musc

    def CSA(self,lvl):
        stringF='Female'
        stringM='Male'
        if stringF.casefold()==str(self.sex).casefold():
            self.AgeConst=Female_CSA_Co.at[self.musc,'Age']
            self.LevelConst=Female_CSA_Co.at[self.musc,'Level']
            self.AgeLevelConst=Female_CSA_Co.at[self.musc,'AgexLevel']
            self.HeightConst=Female_CSA_Co.at[self.musc,'Height']
            self.HeightLevelConst=Female_CSA_Co.at[self.musc,'HeightxLevel']
            self.WeightConst=Female_CSA_Co.at[self.musc,'Weight']
            self.WeightLevelConst=Female_CSA_Co.at[self.musc,'WeightxLevel']
            self.Const=Female_CSA_Co.at[self.musc,'Const']
            self.LSM=Female_CSA_LSM.at[self.musc,lvl]
        elif stringM.casefold()==str(self.sex).casefold():
            self.AgeConst=Male_CSA_Co.at[self.musc,'Age']
            self.LevelConst=Male_CSA_Co.at[self.musc,'Level']
            self.AgeLevelConst=Male_CSA_Co.at[self.musc,'AgexLevel']
            self.HeightConst=Male_CSA_Co.at[self.musc,'Height']
            self.HeightLevelConst=Male_CSA_Co.at[self.musc,'HeightxLevel']
            self.WeightConst=Male_CSA_Co.at[self.musc,'Weight']
            self.WeightLevelConst=Male_CSA_Co.at[self.musc,'WeightxLevel']
            self.Const=Male_CSA_Co.at[self.musc,'Const']
            self.LSM=Male_CSA_LSM.at[self.musc,lvl]

        csa=self.age*self.AgeConst+self.LevelConst*Level_Dict.get(lvl)+self.AgeLevelConst*(self.age*Level_Dict.get(lvl))+self.height*self.HeightConst+self.HeightLevelConst*(self.height*Level_Dict.get(lvl))+self.weight*self.WeightConst+self.WeightLevelConst*(self.weight*Level_Dict.get(lvl))+self.Const+self.LSM
        return csa

    def Distance(self,lvl):
        stringF='Female'
        stringM='Male'
        if stringF.casefold()==str(self.sex).casefold():
            self.AgeConst=Female_Dist_Co.at[self.musc,'Age']
            self.LevelConst=Female_Dist_Co.at[self.musc,'Level']
            self.AgeLevelConst=Female_Dist_Co.at[self.musc,'AgexLevel']
            self.HeightConst=Female_Dist_Co.at[self.musc,'Height']
            self.HeightLevelConst=Female_Dist_Co.at[self.musc,'HeightxLevel']
            self.WeightConst=Female_Dist_Co.at[self.musc,'Weight']
            self.WeightLevelConst=Female_Dist_Co.at[self.musc,'WeightxLevel']
            self.Const=Female_Dist_Co.at[self.musc,'Const']
            self.LSM=Female_Dist_LSM.at[self.musc,lvl]
        elif stringM.casefold()==str(self.sex).casefold():
            self.AgeConst=Male_Dist_Co.at[self.musc,'Age']
            self.LevelConst=Male_Dist_Co.at[self.musc,'Level']
            self.AgeLevelConst=Male_Dist_Co.at[self.musc,'AgexLevel']
            self.HeightConst=Male_Dist_Co.at[self.musc,'Height']
            self.HeightLevelConst=Male_Dist_Co.at[self.musc,'HeightxLevel']
            self.WeightConst=Male_Dist_Co.at[self.musc,'Weight']
            self.WeightLevelConst=Male_Dist_Co.at[self.musc,'WeightxLevel']
            self.Const=Male_Dist_Co.at[self.musc,'Const']
            self.LSM=Male_Dist_LSM.at[self.musc,lvl]

        dist=self.age*self.AgeConst+self.LevelConst*Level_Dict.get(lvl)+self.AgeLevelConst*(self.age*Level_Dict.get(lvl))+self.height*self.HeightConst+self.HeightLevelConst*(self.height*Level_Dict.get(lvl))+self.weight*self.WeightConst+self.WeightLevelConst*(self.weight*Level_Dict.get(lvl))+self.Const+self.LSM
        return dist

    def Angle(self,lvl):
        stringF='Female'
        stringM='Male'
        if stringF.casefold()==str(self.sex).casefold():
            self.AgeConst=Female_Angle_Co.at[self.musc,'Age']
            self.LevelConst=Female_Angle_Co.at[self.musc,'Level']
            self.AgeLevelConst=Female_Angle_Co.at[self.musc,'AgexLevel']
            self.HeightConst=Female_Angle_Co.at[self.musc,'Height']
            self.HeightLevelConst=Female_Angle_Co.at[self.musc,'HeightxLevel']
            self.WeightConst=Female_Angle_Co.at[self.musc,'Weight']
            self.WeightLevelConst=Female_Angle_Co.at[self.musc,'WeightxLevel']
            self.Const=Female_Angle_Co.at[self.musc,'Const']
            self.LSM=Female_Angle_LSM.at[self.musc,lvl]
        elif stringM.casefold()==str(self.sex).casefold():
            self.AgeConst=Male_Angle_Co.at[self.musc,'Age']
            self.LevelConst=Male_Angle_Co.at[self.musc,'Level']
            self.AgeLevelConst=Male_Angle_Co.at[self.musc,'AgexLevel']
            self.HeightConst=Male_Angle_Co.at[self.musc,'Height']
            self.HeightLevelConst=Male_Angle_Co.at[self.musc,'HeightxLevel']
            self.WeightConst=Male_Angle_Co.at[self.musc,'Weight']
            self.WeightLevelConst=Male_Angle_Co.at[self.musc,'WeightxLevel']
            self.Const=Male_Angle_Co.at[self.musc,'Const']
            self.LSM=Male_Angle_LSM.at[self.musc,lvl]

        angle=self.age*self.AgeConst+self.LevelConst*Level_Dict.get(lvl)+self.AgeLevelConst*(self.age*Level_Dict.get(lvl))+self.height*self.HeightConst+self.HeightLevelConst*(self.height*Level_Dict.get(lvl))+self.weight*self.WeightConst+self.WeightLevelConst*(self.weight*Level_Dict.get(lvl))+self.Const+self.LSM
        return angle

    def GenerateResults(self):
        Levels=['L4', 'L3', 'L2', 'L1', 'T12', 'T11', 'T10', 'T9', 'T8', 'T7', 'T6', 'T5', 'T4']
        CSA_Output=[]
        Dist_Output=[]
        Ang_Output=[]
        for i in Levels:
                CSA_Output.append(self.CSA(i))
                Dist_Output.append(self.Distance(i))
                Ang_Output.append(self.Angle(i))
        return CSA_Output,Dist_Output,Ang_Output
