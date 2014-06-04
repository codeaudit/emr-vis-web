import random
import json

docIds = ["0001","0002","0004","0005","0009","0011","0013","0015","0018","0022","0027","0030","0032","0033","0035","0036","0038","0041","0048","0050","0053","0057","0059","0061","0062","0063","0065","0068","0070","0072","0074","0077","0079","0080","0081","0082","0089","0090","0092","0093","0097","0099","0101","0102","0104","0105","0107","0110","0114","0117","0118","0122","0125","0126","0127","0132","0138","0141","0145","0147","0148","0150","0155","0156","0157","0159","0160","0161","0162","0171","0172","0176","0177","0178","0180","0182","0184","0186","0188","0190","0192","0193","0194","0196","0197","0199","0202","0204","0208","0212","0213","0215","0217","0219","0221","0224","0227","0229","0233","0235","0238","0239","0243","0246","0247","0249","0252","0253","0255","0257","0259","0261","0262","0263","0264","0265","0267","0268","0273","0275","0277","0279","0280","0281","0284","0285","0287","0288","0289","0291","0293","0295","0299","0301","0302","0305","0307","0308","0309","0310","0312","0317","0318","0322","0324","0325","0327","0331","0333","0337","0339","0344","0345","0348","0350","0355","0356","0361","0363","0364","0366","0368","0370","0371","0375","0377","0379","0381","0382","0384","0386","0391","0393","0398","0401","0403","0407","0411","0412","0414","0415","0417","0418","0419","0420","0422","0424","0425","0427","0430","0433","0436","0438","0440","0441","0442","0445","0447","0451","0452","0453","0455","0456","0468","0469","0473","0477","0482","0484","0489","0491","0493","0495","0497","0498","0502","0503","0509","0511","0512","0519","0522","0524","0525","0527","0531","0533","0535","0537","0538","0540","0545","0547","0555","0557","0559","0563","0567","0570","0571","0574","0575","0576","0577","0582","0584","0587","0590","0592","0595","0596","0600","0601","0602","0604","0608","0610","0614","0616","0618","0620","0621","0623","0627","0629","0630","0632","0636","0638","0642","0643","0645","0650","0651","0653","0654","0657","0658","0662","0663","0665","0667","0669","0671","0674","0676","0679","0681","0684","0685","0688","0689","0691","0692","0694","0696","0698","0700","0701","0703","0705","0709","0710","0711","0712","0714","0716","0718","0719","0720","0722","0723","0726","0728","0729","0734","0736","0738","0740","0743","0747","0748","0750","0752","0753","0754","0756","0757","0758","0760","0766","0768","0769","0774","0776","0777","0779","0781","0782","0783","0785","0786","0788","0789","0794","0795","0797","0799","0801","0803","0805","0807","0808","0812","0815","0818","0822","0823","0824","0827","0828","0830","0831","0835","0840","0842","0845","0846","0847","0848","0850","0851","0852","0854","0856","0858","0863","0865","0867","0868","0870","0871","0874","0877","0880","0881","0883","0886","0890","0896","0897","0899","0900","0903","0904","0906","0908","0910","0917","0918","0923","0926","0927","0929","0932","0935","0936","0937","0939","0941","0943","0946","0947","0955","0957","0958","0959","0963","0967","0968","0970","0973","0974","0976","0979","0980","0984","0986","0989","0991","0992","0995","0996","0998","1000","1004","1007","1009","1010","1012","1017","1018","1021","1022","1025","1029","1030","1031","1034","1040","1041","1046","1047"]

variables = ["any-adenoma", "appendiceal-orifice", "asa", "biopsy", "cecum",
              "ileo-cecal-valve", "indication-type", "infomed-consent", 
              "nursing-report", "no-prep-adequate", "not-prep-adequate",
              "yes-prep-adequate", "proc-aborted", "widthdraw-time"]

data = {}

for var in variables:

    attributes = dict()

    attributes['numPositive'] = random.randrange(len(docIds))
    attributes['numNegative'] = len(docIds) - attributes['numPositive']

    weights = list()
    for i in range(0, 5):
        weights.append(random.randrange(100))
    weights.sort()

    # print weights

    attributes['topPositive'] = [ 
                                    {"term": "widthdrawal", "weight": weights[0]},
                                    {"term": "pathology", "weight": weights[1]},
                                    {"term": "appendicitis", "weight": weights[2]},
                                    {"term": "mother", "weight": weights[3]},
                                    {"term": "carefully", "weight": weights[4]}
                                ]

    weights = list()
    for i in range(0, 5):
        weights.append(random.randrange(100))
    weights.sort()

    # print weights

    attributes['topNegative'] = [
                                    {"term": "repeat", "weight": weights[0]},
                                    {"term": "impression", "weight": weights[1]},
                                    {"term": "small", "weight": weights[2]},
                                    {"term": "mg", "weight": weights[3]},
                                    {"term": "right", "weight": weights[4]}
                                ]


    data[var] = attributes


print json.dumps(data)