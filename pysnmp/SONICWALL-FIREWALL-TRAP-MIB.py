# SNMP MIB module (SONICWALL-FIREWALL-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONICWALL-FIREWALL-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:34 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso,
 snmpModules) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "snmpModules")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(sonicwallFw,) = mibBuilder.importSymbols(
    "SONICWALL-SMI",
    "sonicwallFw")


# MODULE-IDENTITY

sonicwallFwTrapModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1)
)
sonicwallFwTrapModule.setRevisions(
        ("2015-01-08 00:00",
         "2013-02-25 00:00",
         "2011-04-20 00:00",
         "2010-09-16 00:00",
         "2009-04-22 00:00",
         "2009-04-22 00:00",
         "2009-04-02 00:00",
         "2008-06-10 00:00",
         "2008-04-14 00:00",
         "2008-04-10 00:00",
         "2004-01-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MacAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class FwTrapType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              102,
              103,
              104,
              105,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              508,
              509,
              510,
              511,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              528,
              529,
              530,
              531,
              532,
              533,
              534,
              535,
              536,
              537,
              538,
              539,
              540,
              541,
              542,
              543,
              544,
              545,
              546,
              547,
              548,
              549,
              550,
              551,
              552,
              553,
              554,
              555,
              556,
              557,
              558,
              559,
              560,
              561,
              562,
              563,
              564,
              565,
              566,
              567,
              568,
              569,
              570,
              571,
              573,
              574,
              575,
              576,
              577,
              578,
              601,
              602,
              603,
              604,
              605,
              606,
              607,
              608,
              609,
              610,
              611,
              612,
              613,
              614,
              615,
              616,
              617,
              618,
              619,
              620,
              621,
              622,
              623,
              624,
              625,
              626,
              627,
              628,
              629,
              630,
              631,
              632,
              633,
              634,
              635,
              636,
              637,
              638,
              639,
              640,
              641,
              642,
              643,
              644,
              645,
              646,
              647,
              648,
              649,
              650,
              651,
              652,
              653,
              654,
              655,
              656,
              657,
              658,
              659,
              660,
              661,
              662,
              663,
              664,
              665,
              666,
              667,
              668,
              701,
              702,
              703,
              704,
              705,
              801,
              901,
              902,
              903,
              904,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
              1010,
              1011,
              1012,
              1013,
              1014,
              1015,
              1201,
              1202,
              1203,
              1204,
              1205,
              1206,
              1207,
              1208,
              1209,
              1210,
              1211,
              1212,
              1213,
              1214,
              1215,
              1216,
              1217,
              1218,
              1219,
              1220,
              1221,
              1222,
              1223,
              1224,
              1225,
              1226,
              1227,
              1228,
              1229,
              1230,
              1231,
              1232,
              1233,
              1234,
              1235,
              1236,
              1237,
              1238,
              1239,
              1240,
              1241,
              1242,
              1243,
              1244,
              1245,
              1246,
              1247,
              1248,
              1249,
              1250,
              1251,
              1252,
              1253,
              1254,
              1255,
              1256,
              1257,
              4201,
              4202,
              4203,
              4204,
              4205,
              4206,
              4207,
              4208,
              4209,
              4210,
              4211,
              4212,
              4213,
              4214,
              4215,
              4216,
              4217,
              4218,
              4219,
              4220,
              4221,
              4222,
              4223,
              4224,
              4225,
              4226,
              4227,
              4228,
              4229,
              4230,
              4231,
              4232,
              4233,
              4234,
              4235,
              4236,
              4237,
              4238,
              4239,
              4240,
              4241,
              4242,
              4243,
              4244,
              4245,
              4246,
              4247,
              4248,
              4249,
              4250,
              4251,
              4252,
              4253,
              4254,
              4255,
              4256,
              4257,
              4258,
              4259,
              4260,
              4261,
              4262,
              4263,
              4264,
              4265,
              4401,
              4402,
              4403,
              4404,
              4601,
              4602,
              4603,
              4604,
              4605,
              4606,
              4607,
              4608,
              4609,
              4610,
              4611,
              4612,
              4613,
              4614,
              4801,
              4802,
              4803,
              4804,
              4805,
              4806,
              4807,
              4808,
              4809,
              4810,
              4811,
              4812,
              4813,
              4814,
              4815,
              4816,
              4817,
              4818,
              4819,
              4820,
              4821,
              4822,
              4823,
              4824,
              4825,
              4826,
              4827,
              5001,
              5002,
              5003,
              5004,
              5005,
              5006,
              5007,
              5008,
              5009,
              5010,
              5011,
              5012,
              5013,
              5014,
              5015,
              5016,
              5017,
              5018,
              5019,
              5020,
              5021,
              5022,
              5023,
              5201,
              5202,
              5203,
              5204,
              5205,
              5206,
              5207,
              5208,
              5209,
              5210,
              5211,
              5212,
              5213,
              5214,
              5215,
              5216,
              5217,
              5218,
              5219,
              5220,
              5221,
              5222,
              5223,
              5224,
              5225,
              5226,
              5227,
              5228,
              5229,
              5230,
              5231,
              5232,
              5233,
              5234,
              5235,
              5236,
              5237,
              5238,
              5239,
              5240,
              5241,
              5242,
              5401,
              5402,
              5403,
              5404,
              5405,
              5406,
              5407,
              5408,
              5409,
              5410,
              5411,
              5412,
              5413,
              5414,
              5415,
              5416,
              5417,
              5418,
              5419,
              5420,
              5421,
              5422,
              5423,
              5424,
              5425,
              5601,
              5602,
              5603,
              5604,
              5605,
              5606,
              5607,
              5608,
              5609,
              5610,
              5611,
              5801,
              5802,
              5803,
              5804,
              6001,
              6002,
              6003,
              6201,
              6202,
              6203,
              6204,
              6205,
              6206,
              6207,
              6208,
              6209,
              6210,
              6211,
              6212,
              6213,
              6214,
              6215,
              6216,
              6217,
              6218,
              6219,
              6220,
              6221,
              6222,
              6223,
              6224,
              6225,
              6226,
              6227,
              6228,
              6229,
              6230,
              6231,
              6232,
              6233,
              6234,
              6235,
              6236,
              6237,
              6238,
              6239,
              6240,
              6241,
              6242,
              6243,
              6401,
              6402,
              6403,
              6404,
              6405,
              6406,
              6407,
              6408,
              6409,
              6410,
              6411,
              6412,
              6413,
              6414,
              6415,
              6416,
              6417,
              6418,
              6419,
              6420,
              6421,
              6422,
              6423,
              6424,
              6425,
              6426,
              6427,
              6428,
              6429,
              6430,
              6431,
              6432,
              6433,
              6434,
              6435,
              6436,
              6437,
              6438,
              6439,
              6440,
              6441,
              6442,
              6443,
              6444,
              6445,
              6446,
              6447,
              6448,
              6449,
              6450,
              6451,
              6452,
              6453,
              6454,
              6455,
              6456,
              6457,
              6458,
              6459,
              6460,
              6461,
              6462,
              6463,
              6464,
              6465,
              6466,
              6601,
              6602,
              6603,
              6604,
              6605,
              6606,
              6607,
              6608,
              6609,
              6610,
              6611,
              6612,
              6613,
              6614,
              6615,
              6616,
              6617,
              6801,
              6802,
              6803,
              6804,
              6805,
              6806,
              6807,
              6808,
              6809,
              6810,
              6811,
              6812,
              6813,
              6814,
              6815,
              6816,
              6817,
              6818,
              6819,
              6820,
              6821,
              7001,
              7002,
              7003,
              7004,
              7005,
              7006,
              7007,
              7008,
              7009,
              7010,
              7011,
              7012,
              7013,
              7014,
              7015,
              7016,
              7017,
              7018,
              7019,
              7020,
              7021,
              7022,
              7023,
              7024,
              7025,
              7026,
              7027,
              7028,
              7029,
              7030,
              7031,
              7032,
              7033,
              7034,
              7035,
              7036,
              7037,
              7038,
              7039,
              7040,
              7201,
              7202,
              7203,
              7204,
              7205,
              7206,
              7207,
              7208,
              7209,
              7210,
              7211,
              7212,
              7213,
              7214,
              7215,
              7216,
              7217,
              7218,
              7219,
              7220,
              7221,
              7222,
              7223,
              7224,
              7225,
              7226,
              7227,
              7228,
              7229,
              7230,
              7231,
              7232,
              7233,
              7234,
              7235,
              7236,
              7237,
              7238,
              7239,
              7240,
              7241,
              7242,
              7243,
              7244,
              7245,
              7246,
              7247,
              7248,
              7249,
              7250,
              7251,
              7252,
              7253,
              7254,
              7255,
              7401,
              7402,
              7403,
              7601,
              7602,
              7603,
              7604,
              7605,
              7606,
              7607,
              7608,
              7609,
              7610,
              7611,
              7612,
              7613,
              7614,
              7615,
              7616,
              7617,
              7618,
              7619,
              7620,
              7621,
              7622,
              7623,
              7624,
              7625,
              7626,
              7627,
              7628,
              7629,
              7630,
              7631,
              7632,
              7633,
              7634,
              7635,
              7636,
              7637,
              7638,
              7639,
              7640,
              7641,
              7642,
              7643,
              7644,
              7645,
              7646,
              7647,
              7801,
              7802,
              7803,
              7804,
              7805,
              7806,
              7807,
              7808,
              7809,
              7810,
              7811,
              7812,
              7813,
              7814,
              7815,
              7816,
              7817,
              7818,
              7819,
              7820,
              7821,
              7822,
              7823,
              8001,
              8002,
              8003,
              8004,
              8005,
              8006,
              8007,
              8008,
              8009,
              8010,
              8011,
              8012,
              8013,
              8014,
              8015,
              8016,
              8017,
              8018,
              8019,
              8020,
              8021,
              8022,
              8023,
              8024,
              8025,
              8026,
              8027,
              8028,
              8029,
              8030,
              8031,
              8032,
              8033,
              8034,
              8201,
              8202,
              8203,
              8204,
              8205,
              8206,
              8207,
              8208,
              8209,
              8210,
              8211,
              8212,
              8213,
              8214,
              8215,
              8216,
              8217,
              8218,
              8401,
              8402,
              8403,
              8404,
              8405,
              8406,
              8407,
              8408,
              8409,
              8410,
              8411,
              8412,
              8413,
              8601,
              8602,
              8603,
              8604,
              8605,
              8606,
              8607,
              8608,
              8609,
              8610,
              8611,
              8612,
              8613,
              8614,
              8615,
              8616,
              8617,
              8618,
              8619,
              8620,
              8621,
              8622,
              8623,
              8624,
              8625,
              8626,
              8627,
              8628,
              8629,
              8630,
              8631,
              8632,
              8633,
              8634,
              8635,
              8801,
              8802,
              8803,
              8804,
              8805,
              8806,
              8807,
              8808,
              8809,
              8810,
              8811,
              8812,
              8813,
              8814,
              8815,
              8816,
              8817,
              8818,
              8819,
              8820,
              8821,
              8822,
              8823,
              8824,
              9001,
              9002,
              9003,
              9004,
              9005,
              9006,
              9007,
              9201,
              9202,
              9203,
              9204,
              9205,
              9206,
              9207,
              9208,
              9209,
              9210,
              9401,
              9402,
              9403,
              9404,
              9405,
              9406,
              9407,
              9408,
              9409,
              9410,
              9411,
              9412,
              9413,
              9414,
              9415,
              9416,
              9417,
              9418,
              9419,
              9420,
              9421,
              9422,
              9423,
              9424,
              9425,
              9426,
              9427,
              9428,
              9429,
              9430,
              9431,
              9432,
              9433,
              9434,
              9435,
              9436,
              9437,
              9438,
              9439,
              9440,
              9441,
              9442,
              9443,
              9444,
              9445,
              9446,
              9447,
              9448,
              9449,
              9450,
              9451,
              9452,
              9453,
              9454,
              9455,
              9456,
              9457,
              9458,
              9459,
              9460,
              9461,
              9462,
              9463,
              9464,
              9465,
              9466,
              9467,
              9468,
              9469,
              9470,
              9471,
              9472,
              9473,
              9474,
              9475,
              9476,
              9477,
              9478,
              9479,
              9480,
              9481,
              9482,
              9483,
              9484,
              9485,
              9486,
              9487,
              9488,
              9489,
              9490,
              9491,
              9492,
              9493,
              9494,
              9495,
              9496,
              9497,
              9498,
              9499,
              9500,
              9501,
              9502,
              9503,
              9504,
              9505,
              9506,
              9507,
              9508,
              9509,
              9510,
              9511,
              9512,
              9513,
              9514,
              9515,
              9516,
              9517,
              9518,
              9519,
              9520,
              9521,
              9522,
              9523,
              9524,
              9525,
              9526,
              9527,
              9528,
              9529,
              9530,
              9531,
              9532,
              9533,
              9534,
              9535,
              9536,
              9537,
              9538,
              9539,
              9601,
              9602,
              9603,
              9604,
              9605,
              9606,
              9607,
              9608,
              9609,
              9610,
              9611,
              9612,
              9613,
              9614,
              9615,
              9616,
              9617,
              9618,
              9801,
              9802,
              9803,
              9804,
              9805,
              9806,
              9807,
              9808,
              9809,
              9810,
              9811,
              9812,
              9813,
              9814,
              9815,
              9816,
              9817,
              9818,
              9819,
              9820,
              9821,
              9822,
              9823,
              9824,
              9825,
              9826,
              9827,
              9828,
              9829,
              9830,
              9831,
              9832,
              9833,
              9834,
              9835,
              9836,
              9837,
              9838,
              9839,
              9840,
              9841,
              9842,
              9843,
              9844,
              9845,
              9846,
              9847,
              9848,
              9849,
              10001,
              10002,
              10003,
              10004,
              10005,
              10006,
              10007,
              10008,
              10009,
              10010,
              10201,
              10202,
              10203,
              10204,
              10205,
              10206,
              10207,
              10208,
              10209,
              10210,
              10211,
              10401,
              10402,
              10403,
              10404,
              10601,
              10602,
              10603,
              10604,
              10605,
              10606,
              10607,
              10608,
              10609,
              10610,
              10611,
              10612,
              10613,
              10614,
              10615,
              10616,
              10617,
              10618,
              10619,
              10620,
              10621,
              10622,
              10623,
              10624,
              10625,
              10626,
              10627,
              10628,
              10801,
              10802,
              10803,
              10804,
              10805,
              11401,
              11402,
              11403,
              11404,
              11405,
              11406,
              11407,
              11408,
              11601,
              11801,
              11802,
              11803,
              11804,
              11805,
              11806,
              11807,
              11808,
              11809,
              11810,
              11811,
              11812,
              11813,
              12001,
              12002,
              12003,
              12004,
              12201,
              12202,
              12203,
              12401,
              12402,
              12403,
              12601,
              12602,
              12603,
              12604,
              12605,
              12606,
              12607,
              13201,
              13801,
              13802,
              13803,
              13804,
              13805,
              13806,
              13807,
              13808,
              13809,
              13810,
              13811,
              13812,
              13813,
              13814,
              14001,
              14002,
              14003,
              14004,
              14005,
              14006,
              14601,
              15001,
              15002,
              16001,
              16002,
              16003,
              16004,
              16005,
              16006,
              16007)
        )
    )
    namedValues = NamedValues(
        *(("trapType30MinDialDelay", 567),
          ("trapTypeAVExpirationWarningMsg", 552),
          ("trapTypeAVExpiredMsg", 526),
          ("trapTypeAVGatewayAlert", 578),
          ("trapTypeAVReceivedAlert", 524),
          ("trapTypeAntiSpywareDetectionAlert", 576),
          ("trapTypeAntiSpywareExpiredMsg", 577),
          ("trapTypeAntiSpywarePreventionAlert", 575),
          ("trapTypeAttemptedAdminLoginFromWAN", 506),
          ("trapTypeBackOrificeDropped", 512),
          ("trapTypeBackupActivePreempt", 622),
          ("trapTypeBackupLinkDown", 633),
          ("trapTypeBlockQuickModeWithDefaultKeyId", 660),
          ("trapTypeCFSExpirationMsg", 563),
          ("trapTypeCFSExpirationWarningMsg", 562),
          ("trapTypeCacheFull", 607),
          ("trapTypeCfgChgAttempt", 5611),
          ("trapTypeCfgChgFailed", 5610),
          ("trapTypeCflApplianceCflExpired", 628),
          ("trapTypeCflSubscriptionExpiredEmail", 631),
          ("trapTypeCflUpdateApplianceNotRegistered", 623),
          ("trapTypeCflUpdateErrorInternal", 627),
          ("trapTypeCflUpdateErrorTransient", 625),
          ("trapTypeCflUpdateErrorTransientAuto", 626),
          ("trapTypeCflUpdateSubscriptionExpired", 624),
          ("trapTypeConnDroppedTooManyIP", 608),
          ("trapTypeDhcpRelayIpSpoof", 533),
          ("trapTypeDhcpRelayTableSyncFailure", 632),
          ("trapTypeDroppedMsgPartial", 550),
          ("trapTypeDstConnOverLimit", 668),
          ("trapTypeEnh30MinDialDelay", 7632),
          ("trapTypeEnhACDetectionAlert", 15001),
          ("trapTypeEnhACPreventionAlert", 15002),
          ("trapTypeEnhAFAlert", 7241),
          ("trapTypeEnhAFExpiredMsg", 8635),
          ("trapTypeEnhAPNoUserName", 9470),
          ("trapTypeEnhAPNoUserPassword", 9471),
          ("trapTypeEnhARSDebugStr", 12203),
          ("trapTypeEnhARSInfoStr", 12201),
          ("trapTypeEnhARSSpare1", 1242),
          ("trapTypeEnhARSSpare2", 1243),
          ("trapTypeEnhARSSpare3", 1244),
          ("trapTypeEnhARSSpare4", 1245),
          ("trapTypeEnhARSWarnStr", 12202),
          ("trapTypeEnhAVAccessWithoutAgent", 8605),
          ("trapTypeEnhAVAgentOutOfDate", 8606),
          ("trapTypeEnhAVExpirationWarningMsg", 8618),
          ("trapTypeEnhAVExpiredMsg", 8608),
          ("trapTypeEnhAVGatewayAlert", 8632),
          ("trapTypeEnhAVGatewayExpiredMsg", 8633),
          ("trapTypeEnhAVReceivedAlert", 8607),
          ("trapTypeEnhAVSpare1", 1206),
          ("trapTypeEnhAcceptingResponderLifetime", 9455),
          ("trapTypeEnhActivated", 5201),
          ("trapTypeEnhActiveBackupBackdown", 6211),
          ("trapTypeEnhActiveXBlocked", 7205),
          ("trapTypeEnhAdminCfgSessEnd", 4259),
          ("trapTypeEnhAdminCfgSessStart", 4258),
          ("trapTypeEnhAdminLoginDisabled", 4208),
          ("trapTypeEnhAdminLogout", 4215),
          ("trapTypeEnhAdminLogoutFromCLI", 4235),
          ("trapTypeEnhAdminNameChanged", 4220),
          ("trapTypeEnhAdminSessInactivity", 4216),
          ("trapTypeEnhAlertEmailSubject", 1004),
          ("trapTypeEnhAntiSpamConnLimitReached", 13806),
          ("trapTypeEnhAntiSpamDisabled", 13804),
          ("trapTypeEnhAntiSpamEnabled", 13803),
          ("trapTypeEnhAntiSpamEntityOperational", 13801),
          ("trapTypeEnhAntiSpamExpirationMsg", 13805),
          ("trapTypeEnhAntiSpywareDetectionAlert", 6438),
          ("trapTypeEnhAntiSpywareExpiredMsg", 8631),
          ("trapTypeEnhAntiSpywarePreventionAlert", 6437),
          ("trapTypeEnhAntispamEmailRcvdFromMTA", 13813),
          ("trapTypeEnhAntispamHostIdentified", 13811),
          ("trapTypeEnhAntispamInboundConnectionDropped", 13810),
          ("trapTypeEnhAntispamNoValidDnsServers", 13812),
          ("trapTypeEnhAntispamOutboundConnectionDropped", 13809),
          ("trapTypeEnhAntispamProcessedEmailRcvd", 13814),
          ("trapTypeEnhAntispamStartupFailure", 13807),
          ("trapTypeEnhAntispamTeardownFailure", 13808),
          ("trapTypeEnhAppFwAlert", 13201),
          ("trapTypeEnhArchiveBlocked", 7207),
          ("trapTypeEnhArpAddEntryForBoundMac", 7020),
          ("trapTypeEnhArpFailure", 7002),
          ("trapTypeEnhArpMacAddrCollision", 7021),
          ("trapTypeEnhArpRequestRcvd", 7018),
          ("trapTypeEnhArpRequestSent", 7016),
          ("trapTypeEnhArpResponseRcvd", 7017),
          ("trapTypeEnhArpResponseSent", 7019),
          ("trapTypeEnhArpSpare4", 7023),
          ("trapTypeEnhArpTooManyGraArp", 7022),
          ("trapTypeEnhAuthFailed", 9446),
          ("trapTypeEnhAutoDialFailedEthernetOnlyMode", 7644),
          ("trapTypeEnhAvEnforcedLicensesExceeded", 8617),
          ("trapTypeEnhBackOrificeDropped", 6406),
          ("trapTypeEnhBackupActivePreempt", 6220),
          ("trapTypeEnhBackupLinkDown", 6224),
          ("trapTypeEnhBlockQuickModeWithDefaultKeyId", 9206),
          ("trapTypeEnhBootpCentralAck", 4401),
          ("trapTypeEnhBootpRemoteAck", 4403),
          ("trapTypeEnhBootpReplyConflict", 4402),
          ("trapTypeEnhBootpRequestMessage", 4404),
          ("trapTypeEnhBroadcastDropped", 7217),
          ("trapTypeEnhBwmLimitOnUpgrade", 5219),
          ("trapTypeEnhCFSExpirationMsg", 8620),
          ("trapTypeEnhCFSExpirationWarningMsg", 8619),
          ("trapTypeEnhCRLMissing", 9847),
          ("trapTypeEnhCRLPathValidationError", 9849),
          ("trapTypeEnhCRLValidationError", 9848),
          ("trapTypeEnhCacheFull", 5203),
          ("trapTypeEnhCantResolve", 7004),
          ("trapTypeEnhCategory", 1014),
          ("trapTypeEnhCellularModemInserted", 5419),
          ("trapTypeEnhCellularModemNoSIM", 5420),
          ("trapTypeEnhCellularModemNotFound", 5421),
          ("trapTypeEnhCellularModemRemoved", 5418),
          ("trapTypeEnhCertblockBlacklist", 7247),
          ("trapTypeEnhCertblockDecodeFailed", 7255),
          ("trapTypeEnhCertblockInvalidDate", 7250),
          ("trapTypeEnhCertblockNotCompleteCert", 7254),
          ("trapTypeEnhCertblockNotTrustedCa", 7253),
          ("trapTypeEnhCertblockSelfsigned", 7251),
          ("trapTypeEnhCertblockSsl2", 7249),
          ("trapTypeEnhCertblockWeakCipher", 7252),
          ("trapTypeEnhCertblockWhitelist", 7248),
          ("trapTypeEnhCflApplianceCflExpired", 8614),
          ("trapTypeEnhCflAutoBroken", 8616),
          ("trapTypeEnhCflSubscriptionExpiredEmailSubject", 8615),
          ("trapTypeEnhCflUpdateApplianceNotRegistered", 8609),
          ("trapTypeEnhCflUpdateErrorInternal", 8613),
          ("trapTypeEnhCflUpdateErrorTransient", 8611),
          ("trapTypeEnhCflUpdateErrorTransientAuto", 8612),
          ("trapTypeEnhCflUpdateSubscriptionExpired", 8610),
          ("trapTypeEnhChatCompleted", 7637),
          ("trapTypeEnhChatFailed", 7640),
          ("trapTypeEnhChatMsg", 7639),
          ("trapTypeEnhChatStarted", 7636),
          ("trapTypeEnhChatWrote", 7638),
          ("trapTypeEnhClientPolicyProvisioning", 9204),
          ("trapTypeEnhClientVersionNotCompatible", 9208),
          ("trapTypeEnhCode", 1005),
          ("trapTypeEnhConnDroppedTooManyIP", 5204),
          ("trapTypeEnhConnDroppedTooManyNodes", 5236),
          ("trapTypeEnhCookieRemoved", 7208),
          ("trapTypeEnhCrlBadFormat", 9809),
          ("trapTypeEnhCrlCertRevoked", 9811),
          ("trapTypeEnhCrlDownloadFailed", 9803),
          ("trapTypeEnhCrlDownloadSuccess", 9802),
          ("trapTypeEnhCrlExpired", 9845),
          ("trapTypeEnhCrlFailNoConnect", 9806),
          ("trapTypeEnhCrlFailNoMem", 9804),
          ("trapTypeEnhCrlFailNoReason", 9807),
          ("trapTypeEnhCrlFailTimedOut", 9805),
          ("trapTypeEnhCrlProcFail", 9808),
          ("trapTypeEnhCrlRequest", 9801),
          ("trapTypeEnhCrlWrongIssuer", 9810),
          ("trapTypeEnhCryptDesTestFailed", 4602),
          ("trapTypeEnhCryptDhTestFailed", 4603),
          ("trapTypeEnhCryptFipsErrorState", 4601),
          ("trapTypeEnhCryptHmacMD5TestFailed", 4604),
          ("trapTypeEnhCryptHmacSha1TestFailed", 4605),
          ("trapTypeEnhCryptHw3DesShaTestFailed", 4611),
          ("trapTypeEnhCryptHw3DesTestFailed", 4609),
          ("trapTypeEnhCryptHwAesTestFailed", 4614),
          ("trapTypeEnhCryptHwDesShaTestFailed", 4610),
          ("trapTypeEnhCryptHwDesTestFailed", 4608),
          ("trapTypeEnhCryptMd5TestFailed", 4612),
          ("trapTypeEnhCryptRsaTestFailed", 4606),
          ("trapTypeEnhCryptSha1TestFailed", 4607),
          ("trapTypeEnhDDNSAbuse", 11801),
          ("trapTypeEnhDDNSAbuseImminent", 11805),
          ("trapTypeEnhDDNSAdding", 11807),
          ("trapTypeEnhDDNSAllAssocDeleted", 11811),
          ("trapTypeEnhDDNSAssocDeleted", 11813),
          ("trapTypeEnhDDNSAssocDisabled", 11809),
          ("trapTypeEnhDDNSAssocEnabled", 11808),
          ("trapTypeEnhDDNSDeactivated", 11812),
          ("trapTypeEnhDDNSInvalid", 11802),
          ("trapTypeEnhDDNSLoginFailure", 11803),
          ("trapTypeEnhDDNSPutOnLine", 11810),
          ("trapTypeEnhDDNSSpare14", 1229),
          ("trapTypeEnhDDNSSpare15", 1230),
          ("trapTypeEnhDDNSSpare16", 1231),
          ("trapTypeEnhDDNSTakenOffLine", 11806),
          ("trapTypeEnhDDNSUpdateSuccess", 11804),
          ("trapTypeEnhDHCPCBoundRebind", 4815),
          ("trapTypeEnhDHCPCBoundRenew", 4816),
          ("trapTypeEnhDHCPCGotNewIP", 4823),
          ("trapTypeEnhDHCPCGotOffer", 4809),
          ("trapTypeEnhDHCPCNoOffers", 4808),
          ("trapTypeEnhDHCPCOfferError", 4826),
          ("trapTypeEnhDHCPCRequestACK", 4813),
          ("trapTypeEnhDHCPCRequestDecline", 4814),
          ("trapTypeEnhDHCPCRequestFailed", 4811),
          ("trapTypeEnhDHCPCRequestNAK", 4812),
          ("trapTypeEnhDHCPCRequestRebind", 4818),
          ("trapTypeEnhDHCPCRequestReboot", 4819),
          ("trapTypeEnhDHCPCRequestRenew", 4817),
          ("trapTypeEnhDHCPCRequestResponseError", 4827),
          ("trapTypeEnhDHCPCRequestVerify", 4820),
          ("trapTypeEnhDHCPCRetransDiscover", 4801),
          ("trapTypeEnhDHCPCRetransRequestRebind", 4804),
          ("trapTypeEnhDHCPCRetransRequestReboot", 4805),
          ("trapTypeEnhDHCPCRetransRequestRenew", 4803),
          ("trapTypeEnhDHCPCRetransRequestRequest", 4802),
          ("trapTypeEnhDHCPCRetransRequestVerify", 4806),
          ("trapTypeEnhDHCPCSelecting", 4810),
          ("trapTypeEnhDHCPCSendDiscover", 4807),
          ("trapTypeEnhDHCPCSendRelease", 4824),
          ("trapTypeEnhDHCPCVerifyFailBound", 4822),
          ("trapTypeEnhDHCPCVerifyFailInit", 4821),
          ("trapTypeEnhDHCPNotReady", 4825),
          ("trapTypeEnhDNSAllowed", 7235),
          ("trapTypeEnhDNSRebindAttackBlocked", 6466),
          ("trapTypeEnhDNSRebindAttackDetected", 6465),
          ("trapTypeEnhDODTriggeredByApp", 7646),
          ("trapTypeEnhDODTriggeredByPkt", 7647),
          ("trapTypeEnhDPISSLConCheck", 14601),
          ("trapTypeEnhDataChannelAddFailed", 1204),
          ("trapTypeEnhDataUsageOverlimit", 7643),
          ("trapTypeEnhDataUsageWatermarkReached", 7642),
          ("trapTypeEnhDeaRegInc", 8623),
          ("trapTypeEnhDecryptFailedWithPsk", 9442),
          ("trapTypeEnhDestination", 1008),
          ("trapTypeEnhDhcpOverVpnTunnelNotDefined", 5020),
          ("trapTypeEnhDhcprAckConflict", 5005),
          ("trapTypeEnhDhcprAckInStaticTable", 5006),
          ("trapTypeEnhDhcprAckIsRelay", 5007),
          ("trapTypeEnhDhcprAckIsRemoteMgmt", 5023),
          ("trapTypeEnhDhcprCentralAck", 5004),
          ("trapTypeEnhDhcprCentralGetTable", 5010),
          ("trapTypeEnhDhcprCentralRcvTable", 5012),
          ("trapTypeEnhDhcprCentralRelease", 5003),
          ("trapTypeEnhDhcprDeclineMessage", 5017),
          ("trapTypeEnhDhcprDiscoverLocal", 5021),
          ("trapTypeEnhDhcprDiscoverMessage", 5016),
          ("trapTypeEnhDhcprIpSpoof", 5008),
          ("trapTypeEnhDhcprNoRelayIpAvailable", 5014),
          ("trapTypeEnhDhcprOfferMessage", 5018),
          ("trapTypeEnhDhcprRemoteAck", 5002),
          ("trapTypeEnhDhcprRemoteGetTable", 5009),
          ("trapTypeEnhDhcprRemoteRelease", 5001),
          ("trapTypeEnhDhcprRemoteSentTable", 5011),
          ("trapTypeEnhDhcprRequestLocal", 5022),
          ("trapTypeEnhDhcprRequestMessage", 5015),
          ("trapTypeEnhDhcprServerNakMessage", 5019),
          ("trapTypeEnhDhcprTableReqTimedOut", 5013),
          ("trapTypeEnhDhcpsConflictDetected", 5240),
          ("trapTypeEnhDhcpsDeclineFromClient", 5241),
          ("trapTypeEnhDhcpsSpare2", 1236),
          ("trapTypeEnhDhcpsSpare3", 1237),
          ("trapTypeEnhDhcpsSpare4", 1238),
          ("trapTypeEnhDialBusy", 7604),
          ("trapTypeEnhDialCanceled", 7619),
          ("trapTypeEnhDialDisconnected", 7608),
          ("trapTypeEnhDialFailure", 7607),
          ("trapTypeEnhDialModemStr", 7616),
          ("trapTypeEnhDialNoAnswer", 7605),
          ("trapTypeEnhDialNoCarrier", 7603),
          ("trapTypeEnhDialNoDialtone", 7602),
          ("trapTypeEnhDialStartingPpp", 7606),
          ("trapTypeEnhDialing", 7601),
          ("trapTypeEnhDialupDuration", 7630),
          ("trapTypeEnhDialupMsgDropped", 7641),
          ("trapTypeEnhDmzRipModeOff", 8405),
          ("trapTypeEnhDmzRipModeV1", 8406),
          ("trapTypeEnhDmzRipModeV2", 8407),
          ("trapTypeEnhDmzRipModeV2C", 8408),
          ("trapTypeEnhDropDuplicatePacket", 9444),
          ("trapTypeEnhDropIpTtlExpired", 7037),
          ("trapTypeEnhDropSrcRtPkt", 6424),
          ("trapTypeEnhDroppedMsgPartial", 6425),
          ("trapTypeEnhDstConnOverLimit", 5239),
          ("trapTypeEnhDuplicateEntryInRelayTable", 9209),
          ("trapTypeEnhDuplicatePacketDropped", 7219),
          ("trapTypeEnhEIRGPPDropped", 7236),
          ("trapTypeEnhEtherPortDown", 5211),
          ("trapTypeEnhEtherPortUp", 5210),
          ("trapTypeEnhFailedToFindCert", 9846),
          ("trapTypeEnhFakeCertFound", 6421),
          ("trapTypeEnhFinBlacklistContinues", 6457),
          ("trapTypeEnhFinFldCeased", 6462),
          ("trapTypeEnhFinFldContinues", 6464),
          ("trapTypeEnhFinFldDetected", 6460),
          ("trapTypeEnhFinFldMachineBlacklisted", 6456),
          ("trapTypeEnhFinFldMachineUnBlacklisted", 6458),
          ("trapTypeEnhFipsChangeState2Error", 4613),
          ("trapTypeEnhFirmwareUpdateEmailSubject", 5208),
          ("trapTypeEnhForbiddenAttDeleted", 6422),
          ("trapTypeEnhForbiddenAttDisabled", 6417),
          ("trapTypeEnhFragmentedPacket", 7001),
          ("trapTypeEnhFtpDataPort", 7230),
          ("trapTypeEnhFtpPasvBounceAttack", 6428),
          ("trapTypeEnhFtpPasvRspSpoof", 6426),
          ("trapTypeEnhFtpPortBounceAttack", 6427),
          ("trapTypeEnhGSCAccessWithoutAgent", 8627),
          ("trapTypeEnhGSCNotCompliant", 8625),
          ("trapTypeEnhGSCOutOfDate", 8626),
          ("trapTypeEnhGSCSpare4", 1224),
          ("trapTypeEnhGSCSpare5", 1225),
          ("trapTypeEnhGUIAdminNonCfgSessStart", 4261),
          ("trapTypeEnhGUIAdminRdOnlySessStart", 4260),
          ("trapTypeEnhGUIAdminSessEnd", 4262),
          ("trapTypeEnhGetfwinfo0", 8628),
          ("trapTypeEnhGetfwinfo1", 8629),
          ("trapTypeEnhGetfwinfo2", 8630),
          ("trapTypeEnhGlobalVPNClientNotAuthorized", 9207),
          ("trapTypeEnhGmsIfStats", 6002),
          ("trapTypeEnhGmsSpStats", 6003),
          ("trapTypeEnhGmsSpare3", 1234),
          ("trapTypeEnhGmsSpare4", 1235),
          ("trapTypeEnhHaActiveBackup", 6202),
          ("trapTypeEnhHaActivePrimary", 6201),
          ("trapTypeEnhHaAlert", 6241),
          ("trapTypeEnhHaBackupActive", 6237),
          ("trapTypeEnhHaBackupPreempt", 6209),
          ("trapTypeEnhHaBackupShutdown", 6236),
          ("trapTypeEnhHaBackupWillShutdown", 6235),
          ("trapTypeEnhHaContentNotMatch", 6219),
          ("trapTypeEnhHaDebug", 6243),
          ("trapTypeEnhHaDiscoveredBackup", 6213),
          ("trapTypeEnhHaError", 6238),
          ("trapTypeEnhHaErrorReceivedBackup", 6208),
          ("trapTypeEnhHaErrorReceivedPrimary", 6207),
          ("trapTypeEnhHaIdleBackup", 6204),
          ("trapTypeEnhHaIdlePrimary", 6203),
          ("trapTypeEnhHaInfo", 6240),
          ("trapTypeEnhHaLicenseError", 6229),
          ("trapTypeEnhHaLogicLinkDown", 6234),
          ("trapTypeEnhHaLogicLinkUp", 6233),
          ("trapTypeEnhHaMissedHeartbeatBackup", 6206),
          ("trapTypeEnhHaMissedHeartbeatPrimary", 6205),
          ("trapTypeEnhHaNotice", 6242),
          ("trapTypeEnhHaPktError", 6218),
          ("trapTypeEnhHaPrefsImportError", 6212),
          ("trapTypeEnhHaPrimaryPreempt", 6210),
          ("trapTypeEnhHaRebootReceivedBackup", 6231),
          ("trapTypeEnhHaRebootReceivedPrimary", 6230),
          ("trapTypeEnhHaRebootedHaPeer", 6227),
          ("trapTypeEnhHaRebootingError", 6228),
          ("trapTypeEnhHaSetError", 6221),
          ("trapTypeEnhHaSyncError", 6222),
          ("trapTypeEnhHaSyncedHaPeer", 6214),
          ("trapTypeEnhHaSyncingError", 6215),
          ("trapTypeEnhHaSyncingPref", 6232),
          ("trapTypeEnhHaWarn", 6239),
          ("trapTypeEnhHaWrongSrcBackup", 6217),
          ("trapTypeEnhHaWrongSrcPrimary", 6216),
          ("trapTypeEnhHashFailed", 9447),
          ("trapTypeEnhHdrVerifyFailed", 9460),
          ("trapTypeEnhHttpDropped", 7242),
          ("trapTypeEnhHttpPortChange", 5212),
          ("trapTypeEnhHttpsPortChange", 5213),
          ("trapTypeEnhICMPAllowed", 7233),
          ("trapTypeEnhICMPChkVDropped", 7246),
          ("trapTypeEnhICMPDropped", 7211),
          ("trapTypeEnhIDPDetectionAlert", 6430),
          ("trapTypeEnhIDPExpiredMsg", 8624),
          ("trapTypeEnhIDPPreventionAlert", 6431),
          ("trapTypeEnhIDPReassemblyDetectionAlert", 6435),
          ("trapTypeEnhIDPReassemblyPreventionAlert", 6436),
          ("trapTypeEnhIDPSpare3", 1232),
          ("trapTypeEnhIDPSpare4", 1233),
          ("trapTypeEnhIKEDetailErrLog", 9463),
          ("trapTypeEnhIPConflict", 7025),
          ("trapTypeEnhIPHeaderChkVDropped", 7243),
          ("trapTypeEnhIPSNoSigRAM", 1249),
          ("trapTypeEnhIPSpoofDetected", 6402),
          ("trapTypeEnhIPsecTunnelStatus", 9004),
          ("trapTypeEnhISDNUpdated", 5215),
          ("trapTypeEnhIfProtoBindInit", 5223),
          ("trapTypeEnhIfProtoShutdown", 5222),
          ("trapTypeEnhIkeDeleteRequest", 9450),
          ("trapTypeEnhIkeInitIncorrectLocalAddr", 9458),
          ("trapTypeEnhIkeInitiatorIDMismatch", 9486),
          ("trapTypeEnhIkeInitiatorRemotePartyTO", 9483),
          ("trapTypeEnhIkeRespIncorrectLocalAddr", 9459),
          ("trapTypeEnhIkeResponderAHAuthAlgMismatch", 9473),
          ("trapTypeEnhIkeResponderAHAuthKeyLenMismatch", 9476),
          ("trapTypeEnhIkeResponderAHAuthKeyRoundsMismatch", 9479),
          ("trapTypeEnhIkeResponderAuthAlgoMismatch", 9466),
          ("trapTypeEnhIkeResponderDHGroupMismatch", 9472),
          ("trapTypeEnhIkeResponderESPAuthAlgMismatch", 9475),
          ("trapTypeEnhIkeResponderESPAuthKeyLenMismatch", 9478),
          ("trapTypeEnhIkeResponderESPAuthKeyRoundsMismatch", 9481),
          ("trapTypeEnhIkeResponderESPEncAlgMismatch", 9474),
          ("trapTypeEnhIkeResponderESPEncKeyLenMismatch", 9477),
          ("trapTypeEnhIkeResponderESPEncKeyRoundsMismatch", 9480),
          ("trapTypeEnhIkeResponderEncAlgKeyLenMismatch", 9468),
          ("trapTypeEnhIkeResponderEncAlgoMismatch", 9467),
          ("trapTypeEnhIkeResponderHashAlgMismatch", 9469),
          ("trapTypeEnhIkeResponderIPCompAlgoMismatch", 9482),
          ("trapTypeEnhIkeResponderProtocolMismatch", 9485),
          ("trapTypeEnhIkeResponderRemotePartyTO", 9484),
          ("trapTypeEnhIkeSaLifetimeExpired", 9428),
          ("trapTypeEnhIkeV2AcceptPhase1Proposal", 9496),
          ("trapTypeEnhIkeV2AcceptPhase2Proposal", 9497),
          ("trapTypeEnhIkeV2AuthenticationSuccessful", 9495),
          ("trapTypeEnhIkeV2DecryptPacketFailed", 9513),
          ("trapTypeEnhIkeV2ExtraPayloadExists", 9507),
          ("trapTypeEnhIkeV2IkeAttributesNotFound", 9521),
          ("trapTypeEnhIkeV2IkeProposalReject", 9530),
          ("trapTypeEnhIkeV2InitiatorCreateChildSaResponse", 9526),
          ("trapTypeEnhIkeV2InitiatorIDMismatch", 9529),
          ("trapTypeEnhIkeV2InitiatorIkeAuthResponse", 9525),
          ("trapTypeEnhIkeV2InitiatorInitSaResponse", 9524),
          ("trapTypeEnhIkeV2InitiatorRemotePartyTO", 9523),
          ("trapTypeEnhIkeV2InitiatorStartAuthRequest", 9493),
          ("trapTypeEnhIkeV2InitiatorStartCreateChildSa", 9498),
          ("trapTypeEnhIkeV2InitiatorStartSaInitRequest", 9491),
          ("trapTypeEnhIkeV2InputStateInvalid", 9509),
          ("trapTypeEnhIkeV2InvalidSpiSize", 9517),
          ("trapTypeEnhIkeV2InvalidState", 9516),
          ("trapTypeEnhIkeV2IpsecAttributesNotFound", 9520),
          ("trapTypeEnhIkeV2IpsecProtocolMismatch", 9519),
          ("trapTypeEnhIkeV2NatDetectedBetweenPeers", 9534),
          ("trapTypeEnhIkeV2NegotiationAborted", 9522),
          ("trapTypeEnhIkeV2NegotiationComplete", 9527),
          ("trapTypeEnhIkeV2NoNatDetectedBetweenPeers", 9533),
          ("trapTypeEnhIkeV2NoRequiredPayloads", 9508),
          ("trapTypeEnhIkeV2NotifyErrorPayload", 9532),
          ("trapTypeEnhIkeV2NotifyStatusPayload", 9531),
          ("trapTypeEnhIkeV2OuputStateInvalid", 9510),
          ("trapTypeEnhIkeV2OutOfMemory", 9514),
          ("trapTypeEnhIkeV2PayloadProcessingError", 9506),
          ("trapTypeEnhIkeV2PocessMsgQFailed", 9515),
          ("trapTypeEnhIkeV2RcvdDeleteIkeRequest", 9501),
          ("trapTypeEnhIkeV2RcvdDeleteIkeResponse", 9538),
          ("trapTypeEnhIkeV2RcvdDeleteIpsecRequest", 9503),
          ("trapTypeEnhIkeV2RcvdDeleteIpsecResponse", 9539),
          ("trapTypeEnhIkeV2ResponderRcvdAuthRequest", 9494),
          ("trapTypeEnhIkeV2ResponderRcvdCreateChildSa", 9499),
          ("trapTypeEnhIkeV2ResponderRcvdSaInitRequest", 9492),
          ("trapTypeEnhIkeV2ResponderSendCreateChildSaResponse", 9535),
          ("trapTypeEnhIkeV2SendDeleteIkeRequest", 9500),
          ("trapTypeEnhIkeV2SendDeleteIkeResponse", 9536),
          ("trapTypeEnhIkeV2SendDeleteIpsecRequest", 9502),
          ("trapTypeEnhIkeV2SendDeleteIpsecResponse", 9537),
          ("trapTypeEnhIkeV2SendFailed", 9528),
          ("trapTypeEnhIkeV2Spare1", 1254),
          ("trapTypeEnhIkeV2Spare2", 1255),
          ("trapTypeEnhIkeV2Spare3", 1256),
          ("trapTypeEnhIkeV2Spare4", 1257),
          ("trapTypeEnhIkeV2TSPayloadDestinationNet", 9505),
          ("trapTypeEnhIkeV2TSPayloadLocalNet", 9504),
          ("trapTypeEnhIkeV2UnableToFindIkeSa", 9512),
          ("trapTypeEnhIkeV2ValidatePayloadFailed", 9511),
          ("trapTypeEnhIkeV2VpnPolicyNotFound", 9518),
          ("trapTypeEnhImportedSAInvalid", 5214),
          ("trapTypeEnhIniKillerDropped", 6413),
          ("trapTypeEnhInitAMPhase1Complete", 9432),
          ("trapTypeEnhInitMMPhase1Complete", 9431),
          ("trapTypeEnhInitializing", 5218),
          ("trapTypeEnhInterface2DhcpsUpdate", 5237),
          ("trapTypeEnhInternalErr", 5401),
          ("trapTypeEnhInvalidClientSetup", 9210),
          ("trapTypeEnhInvalidCookies", 9451),
          ("trapTypeEnhInvalidId", 9613),
          ("trapTypeEnhInvalidNetwork", 5225),
          ("trapTypeEnhInvalidPayload", 9465),
          ("trapTypeEnhInvalidRemoteDialupPassword", 4252),
          ("trapTypeEnhInvalidVlanId", 7024),
          ("trapTypeEnhIpcompDropped", 12402),
          ("trapTypeEnhIpcompInterruptErr", 12401),
          ("trapTypeEnhIpsecAHNatMaynotWork", 9611),
          ("trapTypeEnhIpsecAhDropped", 9615),
          ("trapTypeEnhIpsecDeleteRequest", 9449),
          ("trapTypeEnhIpsecDropped", 7213),
          ("trapTypeEnhIpsecEspDropped", 9614),
          ("trapTypeEnhIpsecInterruptErr", 7216),
          ("trapTypeEnhIpsecSaLifetimeExpired", 9612),
          ("trapTypeEnhJavaBlocked", 7206),
          ("trapTypeEnhL2TPNotReady", 1208),
          ("trapTypeEnhL2TPsNoPrivForL2TPLocal", 6820),
          ("trapTypeEnhL2TPsNoPrivForL2TPRadius", 6819),
          ("trapTypeEnhL2toLCPUp", 6613),
          ("trapTypeEnhL2tpCallDisConnRem", 6607),
          ("trapTypeEnhL2tpLCPDown", 6609),
          ("trapTypeEnhL2tpMaxReTransExceed", 6603),
          ("trapTypeEnhL2tpNetDown", 6611),
          ("trapTypeEnhL2tpPPPAuthFail", 6612),
          ("trapTypeEnhL2tpPPPDown", 6617),
          ("trapTypeEnhL2tpPPPStarts", 6608),
          ("trapTypeEnhL2tpPPPUp", 6610),
          ("trapTypeEnhL2tpSessionStarting", 6602),
          ("trapTypeEnhL2tpSessionSuccess", 6606),
          ("trapTypeEnhL2tpTrafficTimeout", 6615),
          ("trapTypeEnhL2tpTunnelDisconRem", 6605),
          ("trapTypeEnhL2tpTunnelFinished", 6604),
          ("trapTypeEnhL2tpTunnelStarting", 6601),
          ("trapTypeEnhL2tpUserCon", 6616),
          ("trapTypeEnhL2tpUserDiscon", 6614),
          ("trapTypeEnhLanICMPAllowed", 7234),
          ("trapTypeEnhLanICMPDenied", 7224),
          ("trapTypeEnhLanIpDenied", 7232),
          ("trapTypeEnhLanPktRcvd", 1207),
          ("trapTypeEnhLanRipModeOff", 8401),
          ("trapTypeEnhLanRipModeV1", 8402),
          ("trapTypeEnhLanRipModeV2", 8403),
          ("trapTypeEnhLanRipModeV2C", 8404),
          ("trapTypeEnhLanTCPDenied", 7222),
          ("trapTypeEnhLanUDPDenied", 7223),
          ("trapTypeEnhLandAttack", 6404),
          ("trapTypeEnhLdapBindFail", 4263),
          ("trapTypeEnhLdapNonAdminAcct", 4265),
          ("trapTypeEnhLdapNonTLS", 4264),
          ("trapTypeEnhLocalRange", 1011),
          ("trapTypeEnhLogAddTest", 5207),
          ("trapTypeEnhLogDeadlockReboot", 5403),
          ("trapTypeEnhLogDebug", 5206),
          ("trapTypeEnhLogDeleteReboot", 5416),
          ("trapTypeEnhLogDeleteStackReboot", 5417),
          ("trapTypeEnhLogDialupReboot", 5423),
          ("trapTypeEnhLogEmailSubject", 1003),
          ("trapTypeEnhLogEventRateExceeded", 5605),
          ("trapTypeEnhLogFull", 5603),
          ("trapTypeEnhLogHeader1", 1001),
          ("trapTypeEnhLogHeader2", 1002),
          ("trapTypeEnhLogHttpServerReboot", 5405),
          ("trapTypeEnhLogICMPTooBig", 7003),
          ("trapTypeEnhLogIkeAbort", 9441),
          ("trapTypeEnhLogIkeAddIPSecSA", 9403),
          ("trapTypeEnhLogIkeBeginInitiatorPh2", 9427),
          ("trapTypeEnhLogIkeDeleteSADstAddr", 9405),
          ("trapTypeEnhLogIkeDeleteSASpi", 9406),
          ("trapTypeEnhLogIkeInitiatorProposalReject", 9490),
          ("trapTypeEnhLogIkeProposalAddrWithDefGw", 9417),
          ("trapTypeEnhLogIkeProposalAddrWithOutDefGw", 9456),
          ("trapTypeEnhLogIkeProposalAhPfsMismatch", 9422),
          ("trapTypeEnhLogIkeProposalAlgKeyMismatch", 9424),
          ("trapTypeEnhLogIkeProposalBadMode", 9413),
          ("trapTypeEnhLogIkeProposalBadModeForXauth", 9425),
          ("trapTypeEnhLogIkeProposalBadZeroLocAddr", 9454),
          ("trapTypeEnhLogIkeProposalBadZeroRemAddr", 9415),
          ("trapTypeEnhLogIkeProposalDmzAddrOnLan", 9421),
          ("trapTypeEnhLogIkeProposalEspPfsMismatch", 9423),
          ("trapTypeEnhLogIkeProposalInsideNotLanDmz", 9419),
          ("trapTypeEnhLogIkeProposalLanAddrOnDmz", 9420),
          ("trapTypeEnhLogIkeProposalNoRemNetMatch", 9416),
          ("trapTypeEnhLogIkeProposalOK", 9401),
          ("trapTypeEnhLogIkeProposalOutsideNotNatPub", 9418),
          ("trapTypeEnhLogIkeProposalOutsideRemNotNat", 9426),
          ("trapTypeEnhLogIkeProposalPhase1IdMismatch", 9414),
          ("trapTypeEnhLogIkeProposalReject", 9440),
          ("trapTypeEnhLogIkeStartNegotiation", 9404),
          ("trapTypeEnhLogIllegalDestination", 9618),
          ("trapTypeEnhLogIllegalIpsecPeer", 9608),
          ("trapTypeEnhLogIllegalPktFromIpsecPeer", 9610),
          ("trapTypeEnhLogIllegalSpi", 9603),
          ("trapTypeEnhLogIncompatibleSA", 9607),
          ("trapTypeEnhLogInitiatorIkeProposalOK", 9437),
          ("trapTypeEnhLogIpsecAuthFailure", 9605),
          ("trapTypeEnhLogIpsecDecryptFailure", 9606),
          ("trapTypeEnhLogIpsecDstNetworkMismatch", 9487),
          ("trapTypeEnhLogIpsecDynamicHostConnect", 9602),
          ("trapTypeEnhLogIpsecProposalReject", 9402),
          ("trapTypeEnhLogIpsecSrcNetworkMismatch", 9488),
          ("trapTypeEnhLogL2TPsCDNFromRemote", 6814),
          ("trapTypeEnhLogL2TPsDeleteSession", 6817),
          ("trapTypeEnhLogL2TPsDeleteTunnel", 6816),
          ("trapTypeEnhLogL2TPsLocalAuthFailure", 6805),
          ("trapTypeEnhLogL2TPsLocalIPFailure", 6807),
          ("trapTypeEnhLogL2TPsPPPUp", 6803),
          ("trapTypeEnhLogL2TPsRadAuthFailure", 6804),
          ("trapTypeEnhLogL2TPsRadIPFailure", 6806),
          ("trapTypeEnhLogL2TPsRetransExceeded", 6818),
          ("trapTypeEnhLogL2TPsSessionDiscRemote", 6809),
          ("trapTypeEnhLogL2TPsSessionUp", 6802),
          ("trapTypeEnhLogL2TPsStopCCNFromRemote", 6815),
          ("trapTypeEnhLogL2TPsTunnelDiscRemote", 6808),
          ("trapTypeEnhLogL2TPsTunnelUp", 6801),
          ("trapTypeEnhLogL2TpsPPPTermFromRemote", 6810),
          ("trapTypeEnhLogL2tpsKeepAliveFailure", 6813),
          ("trapTypeEnhLogL2tpsLocalAuthSuccess", 6811),
          ("trapTypeEnhLogL2tpsRadAuthSuccess", 6812),
          ("trapTypeEnhLogLogCleared", 5601),
          ("trapTypeEnhLogLowMemReboot", 5404),
          ("trapTypeEnhLogNewListLoaded", 8601),
          ("trapTypeEnhLogNoNewListAvailable", 8602),
          ("trapTypeEnhLogOutOfMemory", 9601),
          ("trapTypeEnhLogPkiGeneral", 9813),
          ("trapTypeEnhLogPopBeforeSmtpAuthFailed", 5607),
          ("trapTypeEnhLogProblemAddingL2tpIpPool", 6821),
          ("trapTypeEnhLogProblemEmailingCheckSettings", 5604),
          ("trapTypeEnhLogProblemLoadingCheckDNS", 8604),
          ("trapTypeEnhLogProblemLoadingCheckSettings", 8603),
          ("trapTypeEnhLogRouteOverride", 9489),
          ("trapTypeEnhLogSentToEmail", 5602),
          ("trapTypeEnhLogStackMarginReboot", 5415),
          ("trapTypeEnhLogStatusEvent", 6001),
          ("trapTypeEnhLogSuspendReboot", 5402),
          ("trapTypeEnhLogSyslogDataRateExceeded", 5606),
          ("trapTypeEnhLogUnknownSpi", 9604),
          ("trapTypeEnhLogWlanReboot", 5407),
          ("trapTypeEnhLoginTimedOut", 4207),
          ("trapTypeEnhMTU", 1013),
          ("trapTypeEnhMacFilterListDisabled", 4232),
          ("trapTypeEnhMacFilterListEnabled", 4231),
          ("trapTypeEnhMafiaExpirationMsg", 8622),
          ("trapTypeEnhMafiaExpirationWarningMsg", 8621),
          ("trapTypeEnhMalformedIpPacket", 7226),
          ("trapTypeEnhMaxFailedDials", 7631),
          ("trapTypeEnhMcastAddToPolicyList", 10622),
          ("trapTypeEnhMcastAddressExceeded", 10628),
          ("trapTypeEnhMcastDataApplicationNotSupported", 10621),
          ("trapTypeEnhMcastEtherAddressWrong", 10609),
          ("trapTypeEnhMcastIgmpGeneralQuery", 10605),
          ("trapTypeEnhMcastIgmpHashTimeout", 10617),
          ("trapTypeEnhMcastIgmpLeaveGroup", 10607),
          ("trapTypeEnhMcastIgmpMembershipQuery", 10606),
          ("trapTypeEnhMcastIgmpNotHandled", 10612),
          ("trapTypeEnhMcastIgmpPacketError", 10611),
          ("trapTypeEnhMcastIgmpRouterDetected", 10626),
          ("trapTypeEnhMcastIgmpRouterDetectedVpn", 10627),
          ("trapTypeEnhMcastIgmpUnsupportedRecordType", 10613),
          ("trapTypeEnhMcastIgmpUnsupportedRecordTypeNotHandled", 10614),
          ("trapTypeEnhMcastIgmpV2Join", 10601),
          ("trapTypeEnhMcastIgmpV2Membership", 10604),
          ("trapTypeEnhMcastIgmpV3Join", 10602),
          ("trapTypeEnhMcastIgmpV3Membership", 10603),
          ("trapTypeEnhMcastIgmpVpnTimeout", 10618),
          ("trapTypeEnhMcastIgmpWrongChecksum", 10608),
          ("trapTypeEnhMcastRtcpStatefulFailed", 10620),
          ("trapTypeEnhMcastRtpStatefulFailed", 10619),
          ("trapTypeEnhMcastSpare29", 1213),
          ("trapTypeEnhMcastSpare30", 1214),
          ("trapTypeEnhMcastSpare31", 1215),
          ("trapTypeEnhMcastSpare32", 1216),
          ("trapTypeEnhMcastSrcBroadcast", 10610),
          ("trapTypeEnhMcastTcpDropped", 10616),
          ("trapTypeEnhMcastUdpDropped", 10615),
          ("trapTypeEnhMcastVpnAddToPolicyList", 10624),
          ("trapTypeEnhMcastVpnDeleteFromPolicyList", 10625),
          ("trapTypeEnhMcstDeleteFromPolicyList", 10623),
          ("trapTypeEnhMsAdAgentNotRespond", 11601),
          ("trapTypeEnhMsAdSpare2", 1226),
          ("trapTypeEnhMsAdSpare3", 1227),
          ("trapTypeEnhMsAdSpare4", 1228),
          ("trapTypeEnhMultiIfLinkDown", 5221),
          ("trapTypeEnhMultiIfLinkUp", 5220),
          ("trapTypeEnhNATCouldntRemap", 1202),
          ("trapTypeEnhNATDisabled", 7628),
          ("trapTypeEnhNATEnabled", 7629),
          ("trapTypeEnhNatOverwrite", 7008),
          ("trapTypeEnhNetBusDropped", 6405),
          ("trapTypeEnhNetMonHostDown", 14005),
          ("trapTypeEnhNetMonHostUnknown", 14004),
          ("trapTypeEnhNetMonHostUp", 14006),
          ("trapTypeEnhNetMonPolicyDown", 14002),
          ("trapTypeEnhNetMonPolicyUnknown", 14003),
          ("trapTypeEnhNetMonPolicyUp", 14001),
          ("trapTypeEnhNetSpyDropped", 6407),
          ("trapTypeEnhNetworkOverlap", 5224),
          ("trapTypeEnhNewsgroupAccessed", 7204),
          ("trapTypeEnhNewsgroupBlocked", 7202),
          ("trapTypeEnhNoCertificate", 9812),
          ("trapTypeEnhNoHostTagFound", 7220),
          ("trapTypeEnhNoICMPRedirectSent", 1203),
          ("trapTypeEnhNoMatchICMPDropped", 7227),
          ("trapTypeEnhNoProposalChosen", 9439),
          ("trapTypeEnhNonSPTrafficDropped", 6434),
          ("trapTypeEnhNotifyInvalidSpi", 9453),
          ("trapTypeEnhOcspInternalError", 9844),
          ("trapTypeEnhOcspReceiveResponseMsg", 9840),
          ("trapTypeEnhOcspReceiveResponseMsgError", 9841),
          ("trapTypeEnhOcspReqestMsgSendFailed", 9839),
          ("trapTypeEnhOcspRequestMsgSent", 9838),
          ("trapTypeEnhOcspSpare4", 1246),
          ("trapTypeEnhOcspURLResolveFailed", 9843),
          ("trapTypeEnhOcspURLResolveOK", 9842),
          ("trapTypeEnhOlderPrefs", 5226),
          ("trapTypeEnhOutOfOrderDropped", 7218),
          ("trapTypeEnhPPPDebugMsg", 11408),
          ("trapTypeEnhPPPPoENotReady", 7816),
          ("trapTypeEnhPPPoEPasswordChanged", 4234),
          ("trapTypeEnhPPPoEUserChanged", 4233),
          ("trapTypeEnhPPTPDecodeFailed", 8034),
          ("trapTypeEnhPPTPNotReady", 8033),
          ("trapTypeEnhPayloadMalformed", 9448),
          ("trapTypeEnhPayloadValidationFailed", 9443),
          ("trapTypeEnhPingOfDeathBlocked", 6401),
          ("trapTypeEnhPkeAfterTime", 9832),
          ("trapTypeEnhPkeAlloc", 9816),
          ("trapTypeEnhPkeBadDerCert", 9834),
          ("trapTypeEnhPkeBadPassword", 9819),
          ("trapTypeEnhPkeBadPkcs12Import", 9821),
          ("trapTypeEnhPkeBadSig", 9835),
          ("trapTypeEnhPkeBeforeTime", 9833),
          ("trapTypeEnhPkeCaCertLimit", 9820),
          ("trapTypeEnhPkeChainCircular", 9829),
          ("trapTypeEnhPkeChainIncomplete", 9830),
          ("trapTypeEnhPkeChainNoRoot", 9831),
          ("trapTypeEnhPkeCouldNotValidateCert", 9836),
          ("trapTypeEnhPkeCouldNotValidateChain", 9837),
          ("trapTypeEnhPkeDataStoreCorrupt", 9827),
          ("trapTypeEnhPkeDupLocalCert", 9825),
          ("trapTypeEnhPkeDupLocalCertName", 9824),
          ("trapTypeEnhPkeEntityCertLimit", 9817),
          ("trapTypeEnhPkeFailure", 9814),
          ("trapTypeEnhPkeImportFailed", 9818),
          ("trapTypeEnhPkeNoCa", 9826),
          ("trapTypeEnhPkeNoResource", 9828),
          ("trapTypeEnhPkeNonSonicId", 9822),
          ("trapTypeEnhPkeOutputLen", 9815),
          ("trapTypeEnhPkePubPrivKeyMismatch", 9823),
          ("trapTypeEnhPktDropBySslvpnEnforcement", 10210),
          ("trapTypeEnhPktDropByVpnTraversal", 10203),
          ("trapTypeEnhPktDropByWGuest", 10202),
          ("trapTypeEnhPktDropInClear", 7225),
          ("trapTypeEnhPktDropWanRestricted", 10206),
          ("trapTypeEnhPmtuIcmp", 7007),
          ("trapTypeEnhPortFltDropped", 6432),
          ("trapTypeEnhPortFltLogged", 6433),
          ("trapTypeEnhPortScanPossible", 6415),
          ("trapTypeEnhPortScanProbable", 6416),
          ("trapTypeEnhPossibleSynFlood", 6403),
          ("trapTypeEnhPppAuthOk", 11401),
          ("trapTypeEnhPppChapAuthFailed", 11403),
          ("trapTypeEnhPppChapStarting", 11406),
          ("trapTypeEnhPppMSChapStarting", 11405),
          ("trapTypeEnhPppMschapAuthFailed", 11404),
          ("trapTypeEnhPppPapAuthFailed", 11402),
          ("trapTypeEnhPppPapStarting", 11407),
          ("trapTypeEnhPppduAutoDetect", 7622),
          ("trapTypeEnhPppduDialupDisconnectedOutOfSked", 7634),
          ("trapTypeEnhPppduDialupNotAllowed", 7633),
          ("trapTypeEnhPppduIdleExceeded", 7610),
          ("trapTypeEnhPppduInvalidDnsServer", 7635),
          ("trapTypeEnhPppduIpcpFailed", 7611),
          ("trapTypeEnhPppduIpcpUp", 7612),
          ("trapTypeEnhPppduLinkClosing", 7615),
          ("trapTypeEnhPppduLinkDown", 7614),
          ("trapTypeEnhPppduMaxConnExceeded", 7624),
          ("trapTypeEnhPppduNeedManualAction", 7620),
          ("trapTypeEnhPppduNegotiationFailed", 7609),
          ("trapTypeEnhPppduNoPeerIp", 7627),
          ("trapTypeEnhPppduPppEst", 7613),
          ("trapTypeEnhPppduStartBy", 7623),
          ("trapTypeEnhPppduUserConnect", 7618),
          ("trapTypeEnhPppduUserDisconnect", 7617),
          ("trapTypeEnhPppduVpnDisabled", 7625),
          ("trapTypeEnhPppduVpnEnabled", 7626),
          ("trapTypeEnhPppoeAuthAck", 7812),
          ("trapTypeEnhPppoeAuthNak", 7813),
          ("trapTypeEnhPppoeChapAuthFail", 7810),
          ("trapTypeEnhPppoeChapAuthReq", 7808),
          ("trapTypeEnhPppoeLCPEchoReplyRcvd", 7823),
          ("trapTypeEnhPppoeLCPEchoReplySent", 7822),
          ("trapTypeEnhPppoeLCPEchoRequestRcvd", 7821),
          ("trapTypeEnhPppoeLCPEchoRequestSent", 7820),
          ("trapTypeEnhPppoeLcpUnacked", 7815),
          ("trapTypeEnhPppoeLinkDown", 7803),
          ("trapTypeEnhPppoeLinkFin", 7804),
          ("trapTypeEnhPppoeLinkUp", 7802),
          ("trapTypeEnhPppoeNlDown", 7806),
          ("trapTypeEnhPppoeNlUp", 7805),
          ("trapTypeEnhPppoePads", 7807),
          ("trapTypeEnhPppoePapAuthFail", 7811),
          ("trapTypeEnhPppoePapAuthReq", 7809),
          ("trapTypeEnhPppoeStarting", 7801),
          ("trapTypeEnhPppoeTrafficTimeout", 7814),
          ("trapTypeEnhPptpAuthAck", 8022),
          ("trapTypeEnhPptpAuthNak", 8023),
          ("trapTypeEnhPptpCallDisConnRem", 8007),
          ("trapTypeEnhPptpChapAuthFail", 8020),
          ("trapTypeEnhPptpChapAuthReq", 8018),
          ("trapTypeEnhPptpCtrlConnEstablished", 8004),
          ("trapTypeEnhPptpCtrlConnStarting", 8001),
          ("trapTypeEnhPptpDisconCallRej", 8031),
          ("trapTypeEnhPptpDisconCallRq", 8029),
          ("trapTypeEnhPptpDisconCtrlConnRej", 8030),
          ("trapTypeEnhPptpDisconCtrlConnRq", 8028),
          ("trapTypeEnhPptpDisconEchoRq", 8027),
          ("trapTypeEnhPptpDropped", 7212),
          ("trapTypeEnhPptpLCPDown", 8009),
          ("trapTypeEnhPptpLCPUp", 8013),
          ("trapTypeEnhPptpMaxReTransExceed", 8003),
          ("trapTypeEnhPptpNetDown", 8011),
          ("trapTypeEnhPptpPPPAuthFail", 8012),
          ("trapTypeEnhPptpPPPDown", 8017),
          ("trapTypeEnhPptpPPPStarts", 8008),
          ("trapTypeEnhPptpPPPUp", 8010),
          ("trapTypeEnhPptpPPPlinkDown", 8025),
          ("trapTypeEnhPptpPPPlinkFinished", 8026),
          ("trapTypeEnhPptpPPPlinkUp", 8024),
          ("trapTypeEnhPptpPapAuthFail", 8021),
          ("trapTypeEnhPptpPapAuthReq", 8019),
          ("trapTypeEnhPptpServerDown", 8032),
          ("trapTypeEnhPptpSessionStarting", 8002),
          ("trapTypeEnhPptpSessionSuccess", 8006),
          ("trapTypeEnhPptpTrafficTimeout", 8015),
          ("trapTypeEnhPptpTunnelDisconRem", 8005),
          ("trapTypeEnhPptpUserCon", 8016),
          ("trapTypeEnhPptpUserDiscon", 8014),
          ("trapTypeEnhPrefsDefaulted", 5228),
          ("trapTypeEnhPrefsTooBig", 5227),
          ("trapTypeEnhPrimaryLinkBackUp", 6226),
          ("trapTypeEnhPrimaryLinkDown", 6225),
          ("trapTypeEnhPrimaryLinkDownBackoff", 6223),
          ("trapTypeEnhPriorityDropped", 6412),
          ("trapTypeEnhProbableSynFlood", 1201),
          ("trapTypeEnhProtocol", 1015),
          ("trapTypeEnhProxyAccessBlocked", 7221),
          ("trapTypeEnhRADecodeFailed", 1205),
          ("trapTypeEnhRblHostIdentified", 12003),
          ("trapTypeEnhRblInboundConnectionDropped", 12002),
          ("trapTypeEnhRblNoValidDnsServers", 12004),
          ("trapTypeEnhRblOutboundConnectionDropped", 12001),
          ("trapTypeEnhReceiveQMRequest", 9430),
          ("trapTypeEnhReceivedOnWrongPort", 9462),
          ("trapTypeEnhReceivedPADO", 7817),
          ("trapTypeEnhReceivedPADS", 7818),
          ("trapTypeEnhRemoteDialupAbortedForData", 4255),
          ("trapTypeEnhRemoteDialupAuthReq", 4251),
          ("trapTypeEnhRemoteDialupPasswordTimeout", 4254),
          ("trapTypeEnhRemoteDialupReceived", 4250),
          ("trapTypeEnhRemoteRange", 1012),
          ("trapTypeEnhRemoteWxaProbeStart", 16006),
          ("trapTypeEnhRemoteWxaProbeStop", 16005),
          ("trapTypeEnhReplayDetected", 9609),
          ("trapTypeEnhRespAMIkeRequest", 9434),
          ("trapTypeEnhRespAMPhase1Complete", 9438),
          ("trapTypeEnhRespMMIkeRequest", 9433),
          ("trapTypeEnhRespMMPhase1Complete", 9435),
          ("trapTypeEnhResponderLifetime", 9452),
          ("trapTypeEnhRestartingDumpingLog", 5202),
          ("trapTypeEnhRipWanOn", 8413),
          ("trapTypeEnhRipperDropped", 6409),
          ("trapTypeEnhRstBlacklistContinues", 6454),
          ("trapTypeEnhRstFldCeased", 6461),
          ("trapTypeEnhRstFldContinues", 6463),
          ("trapTypeEnhRstFldDetected", 6459),
          ("trapTypeEnhRstFldMachineBlacklisted", 6453),
          ("trapTypeEnhRstFldMachineUnBlacklisted", 6455),
          ("trapTypeEnhRtcBatteryDead1", 5408),
          ("trapTypeEnhRtcBatteryDead2", 5409),
          ("trapTypeEnhRuleAdded", 5801),
          ("trapTypeEnhRuleDeleted", 5803),
          ("trapTypeEnhRuleIndex", 1009),
          ("trapTypeEnhRuleModified", 5802),
          ("trapTypeEnhRuleTableDefaulted", 5804),
          ("trapTypeEnhSADisabled", 9445),
          ("trapTypeEnhSPI", 1010),
          ("trapTypeEnhSecurityServicesMessage", 8634),
          ("trapTypeEnhSendingPADR", 7819),
          ("trapTypeEnhSennaSpyDropped", 6411),
          ("trapTypeEnhSeuNoHF", 5235),
          ("trapTypeEnhSeuNoLanSubnets", 5233),
          ("trapTypeEnhSeuNoNetBios", 5232),
          ("trapTypeEnhSeuNoTODObjects", 5234),
          ("trapTypeEnhSimultIpcompConnDropped", 12403),
          ("trapTypeEnhSimultIpsecAhConnDropped", 9617),
          ("trapTypeEnhSimultIpsecConnDropped", 7215),
          ("trapTypeEnhSimultIpsecEspConnDropped", 9616),
          ("trapTypeEnhSmurfDropped", 6414),
          ("trapTypeEnhSonicPointProvision", 10402),
          ("trapTypeEnhSonicPointStatus", 10401),
          ("trapTypeEnhSource", 1007),
          ("trapTypeEnhSpankAttackDropped", 6429),
          ("trapTypeEnhSpare888", 1250),
          ("trapTypeEnhSpare889", 1251),
          ("trapTypeEnhSpare920", 1252),
          ("trapTypeEnhSpare921", 1253),
          ("trapTypeEnhSrcConnOverLimit", 5238),
          ("trapTypeEnhSslvpnEnforcement", 10211),
          ("trapTypeEnhStartAMIkeNegotiation", 9436),
          ("trapTypeEnhStartIkeNegSecGateway", 9457),
          ("trapTypeEnhStartMMIkeNegotiation", 9429),
          ("trapTypeEnhStdToEnhUpgrade1", 5229),
          ("trapTypeEnhStdToEnhUpgrade2", 5230),
          ("trapTypeEnhStdToEnhUpgrade3", 5231),
          ("trapTypeEnhStrikerDropped", 6410),
          ("trapTypeEnhSub7Dropped", 6408),
          ("trapTypeEnhSuccessfulAdminLogin", 4202),
          ("trapTypeEnhSuccessfulAdminLoginFromCLI", 4209),
          ("trapTypeEnhSuccessfulAdminVpnLogin", 4211),
          ("trapTypeEnhSuccessfulAdminWanLogin", 4212),
          ("trapTypeEnhSuccessfulUserLogin", 4204),
          ("trapTypeEnhSuccessfulUserVpnLogin", 4213),
          ("trapTypeEnhSuccessfulUserWanLogin", 4214),
          ("trapTypeEnhSylogServerUnavailable", 7009),
          ("trapTypeEnhSynBlacklistContinues", 6451),
          ("trapTypeEnhSynFldBlacklistOff", 6446),
          ("trapTypeEnhSynFldBlacklistOn", 6445),
          ("trapTypeEnhSynFldCeased", 6450),
          ("trapTypeEnhSynFldContinues", 6449),
          ("trapTypeEnhSynFldDetected", 6443),
          ("trapTypeEnhSynFldMachineBlacklisted", 6447),
          ("trapTypeEnhSynFldMachineUnBlacklisted", 6448),
          ("trapTypeEnhSynFldProxyMode", 6441),
          ("trapTypeEnhSynFldProxyModeCanceled", 6444),
          ("trapTypeEnhSynFldProxyTriggered", 6442),
          ("trapTypeEnhSynFldTriggerMode", 6440),
          ("trapTypeEnhSynFldWatchMode", 6439),
          ("trapTypeEnhSynReceived", 6452),
          ("trapTypeEnhSynSpare2", 1247),
          ("trapTypeEnhSynSpare3", 1248),
          ("trapTypeEnhSysEnvFanFail", 5411),
          ("trapTypeEnhSysEnvNormal", 5424),
          ("trapTypeEnhSysEnvPwrSupplyDegraded", 5425),
          ("trapTypeEnhSysEnvTempRed", 5413),
          ("trapTypeEnhSysEnvTempRedExceed", 5414),
          ("trapTypeEnhSysEnvTempYellow", 5412),
          ("trapTypeEnhSysEnvVoltageFail", 5410),
          ("trapTypeEnhSyslogCloseLogged", 7403),
          ("trapTypeEnhSyslogConnectionLogged", 7402),
          ("trapTypeEnhSyslogWebSiteAccessed", 7401),
          ("trapTypeEnhSystemShutdown", 5242),
          ("trapTypeEnhTCPChkVDropped", 7244),
          ("trapTypeEnhTCPDropped", 7209),
          ("trapTypeEnhTCPStatFIN", 9002),
          ("trapTypeEnhTCPStatPSH", 9003),
          ("trapTypeEnhTCPStatSYN", 9001),
          ("trapTypeEnhTcpBadHeaderDropped", 7013),
          ("trapTypeEnhTcpBadHeaderLen", 7026),
          ("trapTypeEnhTcpBadMssOptionLen", 7033),
          ("trapTypeEnhTcpBadOptionLen", 7034),
          ("trapTypeEnhTcpBadSackOptionLen", 7032),
          ("trapTypeEnhTcpBadSourcePort", 7035),
          ("trapTypeEnhTcpBadWindowScaleOptionLen", 7039),
          ("trapTypeEnhTcpBadWindowScaleOptionValue", 7040),
          ("trapTypeEnhTcpClosedConnectionDrop", 7030),
          ("trapTypeEnhTcpConnectionAborted", 7015),
          ("trapTypeEnhTcpConnectionRefused", 7014),
          ("trapTypeEnhTcpExistingConnectionSyn", 7031),
          ("trapTypeEnhTcpFinDropped", 7005),
          ("trapTypeEnhTcpFinScanDropped", 6418),
          ("trapTypeEnhTcpHandshakeDropped", 7240),
          ("trapTypeEnhTcpInvalidAckDropped", 7011),
          ("trapTypeEnhTcpInvalidFlagDropped", 7012),
          ("trapTypeEnhTcpInvalidSeqDropped", 7010),
          ("trapTypeEnhTcpNoAckFlag", 7029),
          ("trapTypeEnhTcpNoCache", 7027),
          ("trapTypeEnhTcpNoSynFlag", 7028),
          ("trapTypeEnhTcpNullScanDropped", 6420),
          ("trapTypeEnhTcpOptionNotPermitted", 7038),
          ("trapTypeEnhTcpSynFinDropped", 7231),
          ("trapTypeEnhTcpSynFloodCookieInvalid", 7036),
          ("trapTypeEnhTcpXmasScanDropped", 6419),
          ("trapTypeEnhTcpXmasTreeDropped", 6423),
          ("trapTypeEnhTimeChanged", 5608),
          ("trapTypeEnhType", 1006),
          ("trapTypeEnhUDPChkVDropped", 7245),
          ("trapTypeEnhUDPDropped", 7210),
          ("trapTypeEnhUnencryptedWhileCryptoActive", 9461),
          ("trapTypeEnhUnknownProtocolDropped", 7214),
          ("trapTypeEnhUnknownUserLoginAttempt", 4206),
          ("trapTypeEnhUserDisconnectDetect", 4201),
          ("trapTypeEnhUserLoginBarredByRule", 4256),
          ("trapTypeEnhUserLoginCIACfgErr", 12602),
          ("trapTypeEnhUserLoginCIALongDomainName", 12606),
          ("trapTypeEnhUserLoginCIALongUserName", 12605),
          ("trapTypeEnhUserLoginCIAProblem", 12603),
          ("trapTypeEnhUserLoginCIAResolveFail", 12604),
          ("trapTypeEnhUserLoginCIATimeout", 12601),
          ("trapTypeEnhUserLoginDisabled", 4247),
          ("trapTypeEnhUserLoginFromWrongLocation", 8204),
          ("trapTypeEnhUserLoginLdapBadServerCert", 8216),
          ("trapTypeEnhUserLoginLdapCertName", 8213),
          ("trapTypeEnhUserLoginLdapDirectoryMismatch", 8218),
          ("trapTypeEnhUserLoginLdapError", 8208),
          ("trapTypeEnhUserLoginLdapFail", 8206),
          ("trapTypeEnhUserLoginLdapInsufficientAccess", 8211),
          ("trapTypeEnhUserLoginLdapInvalidCredentials", 8210),
          ("trapTypeEnhUserLoginLdapProblem", 8209),
          ("trapTypeEnhUserLoginLdapResolveFail", 8214),
          ("trapTypeEnhUserLoginLdapSchemaMismatch", 8212),
          ("trapTypeEnhUserLoginLdapSpare15", 1222),
          ("trapTypeEnhUserLoginLdapSpare16", 1223),
          ("trapTypeEnhUserLoginLdapTLSError", 8217),
          ("trapTypeEnhUserLoginLdapTimeout", 8207),
          ("trapTypeEnhUserLoginLockout", 4221),
          ("trapTypeEnhUserLoginLockoutClear", 4223),
          ("trapTypeEnhUserLoginLockoutExpire", 4222),
          ("trapTypeEnhUserLoginNoUserName", 12607),
          ("trapTypeEnhUserLoginNotFoundLocal", 4257),
          ("trapTypeEnhUserLoginRadiusError", 8203),
          ("trapTypeEnhUserLoginRadiusFail", 8201),
          ("trapTypeEnhUserLoginRadiusProblem", 8205),
          ("trapTypeEnhUserLoginRadiusResolveFail", 8215),
          ("trapTypeEnhUserLoginRadiusTimeout", 8202),
          ("trapTypeEnhUserLogout", 4217),
          ("trapTypeEnhUserSessInactivity", 4219),
          ("trapTypeEnhUserSessTimeout", 4218),
          ("trapTypeEnhVPNClientLicenseExceeded", 9205),
          ("trapTypeEnhVPNDisDialup", 1209),
          ("trapTypeEnhValidRemoteDialupPassword", 4253),
          ("trapTypeEnhVlanSpare1", 1239),
          ("trapTypeEnhVlanSpare2", 1240),
          ("trapTypeEnhVlanSpare3", 1241),
          ("trapTypeEnhVoipAddress", 8814),
          ("trapTypeEnhVoipAdmissionConfirm", 8804),
          ("trapTypeEnhVoipAdmissionReject", 8803),
          ("trapTypeEnhVoipAdmissionRequest", 8805),
          ("trapTypeEnhVoipBandwidthReject", 8806),
          ("trapTypeEnhVoipCallConnect", 8801),
          ("trapTypeEnhVoipCallDisconnect", 8802),
          ("trapTypeEnhVoipConnect", 8813),
          ("trapTypeEnhVoipDisengageConfirm", 8807),
          ("trapTypeEnhVoipDisengageReject", 8820),
          ("trapTypeEnhVoipEndSession", 8815),
          ("trapTypeEnhVoipEndpointAdded", 8816),
          ("trapTypeEnhVoipEndpointDenied", 8818),
          ("trapTypeEnhVoipEndpointRemoved", 8817),
          ("trapTypeEnhVoipGatekeeperReject", 8808),
          ("trapTypeEnhVoipLocationConfirm", 8809),
          ("trapTypeEnhVoipLocationReject", 8810),
          ("trapTypeEnhVoipRegistrationReject", 8811),
          ("trapTypeEnhVoipSetup", 8812),
          ("trapTypeEnhVoipSipRegisterExpires", 8824),
          ("trapTypeEnhVoipSipRequest", 8822),
          ("trapTypeEnhVoipSipResponse", 8823),
          ("trapTypeEnhVoipSpare25", 1210),
          ("trapTypeEnhVoipSpare26", 1211),
          ("trapTypeEnhVoipSpare27", 1212),
          ("trapTypeEnhVoipUnknownMessageResponse", 8819),
          ("trapTypeEnhVoipUnregistrationReject", 8821),
          ("trapTypeEnhVpnBadSaCount", 9006),
          ("trapTypeEnhVpnClean", 9005),
          ("trapTypeEnhVpnDebug", 9408),
          ("trapTypeEnhVpnDisabled", 4225),
          ("trapTypeEnhVpnEnabled", 4226),
          ("trapTypeEnhVpnHwInitErr", 5406),
          ("trapTypeEnhVpnIkeIdMismatch", 9464),
          ("trapTypeEnhVpnNatTravNoNatDevicePresent", 9411),
          ("trapTypeEnhVpnNatTravPeerBehindNat", 9409),
          ("trapTypeEnhVpnNatTravPeerNotSupportNatTraversal", 9412),
          ("trapTypeEnhVpnNatTravWeBehindNat", 9410),
          ("trapTypeEnhVpnRcvdPmtuIcmp", 7006),
          ("trapTypeEnhVpnRuleIsMissing", 9007),
          ("trapTypeEnhVpnStrSrcDst", 9407),
          ("trapTypeEnhWANNotReady", 5217),
          ("trapTypeEnhWWANModemType", 5422),
          ("trapTypeEnhWanIpChange", 5205),
          ("trapTypeEnhWanLinkDown", 5209),
          ("trapTypeEnhWanModeIs", 10001),
          ("trapTypeEnhWanNotSetup", 5216),
          ("trapTypeEnhWanRipModeOff", 8409),
          ("trapTypeEnhWanRipModeV1", 8410),
          ("trapTypeEnhWanRipModeV2", 8411),
          ("trapTypeEnhWanRipModeV2C", 8412),
          ("trapTypeEnhWebAccessRequestDropped", 7228),
          ("trapTypeEnhWebAccessRequestRcvd", 7229),
          ("trapTypeEnhWebSiteAccessed", 7203),
          ("trapTypeEnhWebSiteBlocked", 7201),
          ("trapTypeEnhWfoFailback", 10004),
          ("trapTypeEnhWfoManualProfile", 7621),
          ("trapTypeEnhWfoManualSecProfile", 10003),
          ("trapTypeEnhWfoProbeFailed", 10002),
          ("trapTypeEnhWfoProbeSuccess", 10005),
          ("trapTypeEnhWiFiSecDisabled", 4229),
          ("trapTypeEnhWiFiSecEnabled", 4230),
          ("trapTypeEnhWlan80211bMgmt", 10204),
          ("trapTypeEnhWlanAccountTimeout", 4238),
          ("trapTypeEnhWlanAssoFlood", 10803),
          ("trapTypeEnhWlanDisabled", 4227),
          ("trapTypeEnhWlanDropByDenyNetwork", 7237),
          ("trapTypeEnhWlanEnabled", 4228),
          ("trapTypeEnhWlanFirmwareUpdated", 10201),
          ("trapTypeEnhWlanGuestAlreadyLoggedIn", 4239),
          ("trapTypeEnhWlanGuestCreated", 4240),
          ("trapTypeEnhWlanGuestDeleted", 4241),
          ("trapTypeEnhWlanGuestDisabled", 4242),
          ("trapTypeEnhWlanGuestLimit", 4236),
          ("trapTypeEnhWlanGuestPruned", 4244),
          ("trapTypeEnhWlanGuestReEnabled", 4243),
          ("trapTypeEnhWlanGuestReGenerated", 4245),
          ("trapTypeEnhWlanIdleTimeout", 4246),
          ("trapTypeEnhWlanMaxUsers", 7239),
          ("trapTypeEnhWlanModeDHCPS", 10207),
          ("trapTypeEnhWlanNoGuestPrivilege", 4224),
          ("trapTypeEnhWlanPassByAllowNetwork", 7238),
          ("trapTypeEnhWlanPassiveRogueAP", 10804),
          ("trapTypeEnhWlanProbeCheck", 10805),
          ("trapTypeEnhWlanRecover", 10205),
          ("trapTypeEnhWlanRogueAP", 10801),
          ("trapTypeEnhWlanSchedDisabled", 4248),
          ("trapTypeEnhWlanSchedEnabled", 4249),
          ("trapTypeEnhWlanSeqCheck", 10802),
          ("trapTypeEnhWlanSessionTimeout", 4237),
          ("trapTypeEnhWlanSpare11", 1217),
          ("trapTypeEnhWlanSpare12", 1218),
          ("trapTypeEnhWlanSpare13", 1219),
          ("trapTypeEnhWlanSpare14", 1220),
          ("trapTypeEnhWlanSpare15", 1221),
          ("trapTypeEnhWlanVapDisabled", 10404),
          ("trapTypeEnhWlanVapEnabled", 10403),
          ("trapTypeEnhWlbFailover", 10008),
          ("trapTypeEnhWlbOffSpill", 10007),
          ("trapTypeEnhWlbOnSpill", 10006),
          ("trapTypeEnhWlbResourceAvailable", 10009),
          ("trapTypeEnhWlbResourceFailed", 10010),
          ("trapTypeEnhWpaMicFailure", 10208),
          ("trapTypeEnhWpaRadiusTmout", 10209),
          ("trapTypeEnhWrongAdminPasswd", 4203),
          ("trapTypeEnhWrongAdminPasswdFromCLI", 4210),
          ("trapTypeEnhWrongUserPasswd", 4205),
          ("trapTypeEnhWwanStartingPpp", 7645),
          ("trapTypeEnhWxaDeviceDown", 16002),
          ("trapTypeEnhWxaDeviceUnused", 16004),
          ("trapTypeEnhWxaDeviceUp", 16001),
          ("trapTypeEnhWxaDeviceUsed", 16003),
          ("trapTypeEnhWxaLicenseExpired", 16007),
          ("trapTypeEnhXauthFailure", 9202),
          ("trapTypeEnhXauthRadiusTimeout", 9203),
          ("trapTypeEnhXauthSuccess", 9201),
          ("trapTypeEnhrAntiSpamEntityUnreachable", 13802),
          ("trapTypeEtherPortDown", 641),
          ("trapTypeEtherPortUp", 640),
          ("trapTypeFakeCertFound", 532),
          ("trapTypeFipsChangeState2Error", 659),
          ("trapTypeForbiddenAttDeleted", 534),
          ("trapTypeForbiddenAttachment", 527),
          ("trapTypeFtpDataPort", 557),
          ("trapTypeFtpPasvBounceAttack", 556),
          ("trapTypeFtpPasvRspSpoof", 551),
          ("trapTypeFtpPortBounceAttack", 555),
          ("trapTypeGlobalVPNClientNotAuthorized", 643),
          ("trapTypeHaBackupPreempt", 619),
          ("trapTypeHaErrorReceivedBackup", 618),
          ("trapTypeHaErrorReceivedPrimary", 617),
          ("trapTypeHaHaLicenseError", 664),
          ("trapTypeHaIdlePrimary", 614),
          ("trapTypeHaMissedHeartbeatBackup", 616),
          ("trapTypeHaMissedHeartbeatPrimary", 615),
          ("trapTypeHaPrimaryPreempt", 620),
          ("trapTypeHaRebootReceivedBackup", 666),
          ("trapTypeHaRebootReceivedPrimary", 665),
          ("trapTypeHaRebootingError", 663),
          ("trapTypeHaSetError", 629),
          ("trapTypeHaSyncError", 630),
          ("trapTypeHaSyncingError", 662),
          ("trapTypeIDPDetectionAlert", 569),
          ("trapTypeIDPExpiredMsg", 571),
          ("trapTypeIDPPreventionAlert", 570),
          ("trapTypeIDPReassemblyDetectionAlert", 573),
          ("trapTypeIDPReassemblyPreventionAlert", 574),
          ("trapTypeIPSpoofDetected", 502),
          ("trapTypeIkeProposalAddrWithDefGw", 539),
          ("trapTypeIkeProposalAddrWithOutDefGw", 553),
          ("trapTypeIkeProposalAhPfsMismatch", 544),
          ("trapTypeIkeProposalAlgKeyMismatch", 546),
          ("trapTypeIkeProposalBadMode", 535),
          ("trapTypeIkeProposalBadZeroLocAddr", 549),
          ("trapTypeIkeProposalBadZeroRemAddr", 537),
          ("trapTypeIkeProposalDmzAddrOnLan", 543),
          ("trapTypeIkeProposalEspPfsMismatch", 545),
          ("trapTypeIkeProposalInsideNotLanDmz", 541),
          ("trapTypeIkeProposalLanAddrOnDmz", 542),
          ("trapTypeIkeProposalNoRemNetMatch", 538),
          ("trapTypeIkeProposalOutsideNotNatPub", 540),
          ("trapTypeIkeProposalOutsideRemNotNatPub", 548),
          ("trapTypeIkeProposalPhase1IdMismatch", 536),
          ("trapTypeIllegalLanAddressInUse", 605),
          ("trapTypeIniKillerDropped", 519),
          ("trapTypeInternalErr", 610),
          ("trapTypeLandAttack", 505),
          ("trapTypeLogAddTest", 525),
          ("trapTypeLogDeadlockReboot", 612),
          ("trapTypeLogDeleteReboot", 656),
          ("trapTypeLogDeleteStackReboot", 657),
          ("trapTypeLogFull", 601),
          ("trapTypeLogHttpServerReboot", 621),
          ("trapTypeLogIkeProposalReject", 523),
          ("trapTypeLogIllegalIpsecPeer", 510),
          ("trapTypeLogIpsecAuthFailure", 508),
          ("trapTypeLogIpsecDecryptFailure", 509),
          ("trapTypeLogLowMemReboot", 613),
          ("trapTypeLogOutOfMemory", 609),
          ("trapTypeLogProblemAddingL2tpIpPool", 661),
          ("trapTypeLogProblemEmailingCheckSettings", 604),
          ("trapTypeLogProblemLoadingCheckDNS", 603),
          ("trapTypeLogProblemLoadingCheckSettings", 602),
          ("trapTypeLogStackMarginReboot", 655),
          ("trapTypeLogSuspendReboot", 611),
          ("trapTypeLogUnknownSpi", 507),
          ("trapTypeMafiaExpirationMsg", 565),
          ("trapTypeMafiaExpirationWarningMsg", 564),
          ("trapTypeMalformedIpPacket", 554),
          ("trapTypeMaxFailedDials", 566),
          ("trapTypeMultiIfLinkDown", 647),
          ("trapTypeMultiIfLinkUp", 646),
          ("trapTypeNATCouldntRemap", 606),
          ("trapTypeNetBusDropped", 511),
          ("trapTypeNetSpyDropped", 513),
          ("trapTypeNewsgroupAccessed", 704),
          ("trapTypeNewsgroupBlocked", 702),
          ("trapTypeOlderPrefs", 648),
          ("trapTypePingOfDeathBlocked", 501),
          ("trapTypePortScanPossible", 521),
          ("trapTypePortScanProbable", 522),
          ("trapTypePossibleSynFlood", 503),
          ("trapTypePrefsDefaulted", 650),
          ("trapTypePrefsTooBig", 649),
          ("trapTypePrimaryLinkDown", 634),
          ("trapTypePriorityDropped", 518),
          ("trapTypeProbableSynFlood", 504),
          ("trapTypeProxyAccessBlocked", 705),
          ("trapTypeReplayDetected", 531),
          ("trapTypeRipperDropped", 515),
          ("trapTypeRtcBatteryDead1", 644),
          ("trapTypeRtcBatteryDead2", 645),
          ("trapTypeSennaSpyDropped", 517),
          ("trapTypeSmurfDropped", 520),
          ("trapTypeSpankAttackDropped", 568),
          ("trapTypeSrcConnOverLimit", 667),
          ("trapTypeStrikerDropped", 516),
          ("trapTypeSub7Dropped", 514),
          ("trapTypeSysEnvFanFail", 102),
          ("trapTypeSysEnvTempRed", 104),
          ("trapTypeSysEnvTempRedExceed", 105),
          ("trapTypeSysEnvTempYellow", 103),
          ("trapTypeSysEnvVoltageFail", 101),
          ("trapTypeTcpFinScanDropped", 528),
          ("trapTypeTcpNullScanDropped", 530),
          ("trapTypeTcpSynFinDropped", 558),
          ("trapTypeTcpXmasScanDropped", 529),
          ("trapTypeTcpXmasTreeDropped", 547),
          ("trapTypeUserLoginDisabled", 559),
          ("trapTypeUserLoginLockout", 561),
          ("trapTypeVPNClientLicenseExceeded", 658),
          ("trapTypeVpnTunnelStatus", 801),
          ("trapTypeWanIpChange", 636),
          ("trapTypeWanLinkDown", 635),
          ("trapTypeWanModeIs", 639),
          ("trapTypeWebSiteAccessed", 703),
          ("trapTypeWebSiteBlocked", 701),
          ("trapTypeWfoProbeFailed", 637),
          ("trapTypeWfoProbeSuccess", 638),
          ("trapTypeWlanAssoFlood", 903),
          ("trapTypeWlanProbeCheck", 904),
          ("trapTypeWlanReboot", 642),
          ("trapTypeWlanRogueAP", 901),
          ("trapTypeWlanSeqCheck", 902),
          ("trapTypeWlbFailback", 652),
          ("trapTypeWlbFailover", 651),
          ("trapTypeWlbResourceAvailable", 653),
          ("trapTypeWlbResourceFailed", 654),
          ("trapTypeWrongAdminPasswd", 560),
          ("trapTypetrapTypeCfgChgSucceeded", 5609))
    )



# MIB Managed Objects in the order of their OIDs

_SonicwallFwTrapInfo_ObjectIdentity = ObjectIdentity
sonicwallFwTrapInfo = _SonicwallFwTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1)
)
_SwTrapInfoTable_ObjectIdentity = ObjectIdentity
swTrapInfoTable = _SwTrapInfoTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1)
)
_SwTrapInfoTrapType_Type = FwTrapType
_SwTrapInfoTrapType_Object = MibScalar
swTrapInfoTrapType = _SwTrapInfoTrapType_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 1),
    _SwTrapInfoTrapType_Type()
)
swTrapInfoTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoTrapType.setStatus("current")
_SwTrapInfoTrapDescription_Type = DisplayString
_SwTrapInfoTrapDescription_Object = MibScalar
swTrapInfoTrapDescription = _SwTrapInfoTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 2),
    _SwTrapInfoTrapDescription_Type()
)
swTrapInfoTrapDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoTrapDescription.setStatus("current")
_SwTrapInfoSrcIpAddress_Type = IpAddress
_SwTrapInfoSrcIpAddress_Object = MibScalar
swTrapInfoSrcIpAddress = _SwTrapInfoSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 3),
    _SwTrapInfoSrcIpAddress_Type()
)
swTrapInfoSrcIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoSrcIpAddress.setStatus("current")
_SwTrapInfoDstIpAddress_Type = IpAddress
_SwTrapInfoDstIpAddress_Object = MibScalar
swTrapInfoDstIpAddress = _SwTrapInfoDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 4),
    _SwTrapInfoDstIpAddress_Type()
)
swTrapInfoDstIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoDstIpAddress.setStatus("current")
_SwTrapInfoSrcPort_Type = Integer32
_SwTrapInfoSrcPort_Object = MibScalar
swTrapInfoSrcPort = _SwTrapInfoSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 5),
    _SwTrapInfoSrcPort_Type()
)
swTrapInfoSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoSrcPort.setStatus("current")
_SwTrapInfoDstPort_Type = Integer32
_SwTrapInfoDstPort_Object = MibScalar
swTrapInfoDstPort = _SwTrapInfoDstPort_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 6),
    _SwTrapInfoDstPort_Type()
)
swTrapInfoDstPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoDstPort.setStatus("current")
_SwTrapInfoSrcMacAddress_Type = MacAddress
_SwTrapInfoSrcMacAddress_Object = MibScalar
swTrapInfoSrcMacAddress = _SwTrapInfoSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 7),
    _SwTrapInfoSrcMacAddress_Type()
)
swTrapInfoSrcMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoSrcMacAddress.setStatus("current")
_SwTrapInfoDstMacAddress_Type = MacAddress
_SwTrapInfoDstMacAddress_Object = MibScalar
swTrapInfoDstMacAddress = _SwTrapInfoDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 8),
    _SwTrapInfoDstMacAddress_Type()
)
swTrapInfoDstMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoDstMacAddress.setStatus("current")
_SwTrapInfoIpType_Type = Integer32
_SwTrapInfoIpType_Object = MibScalar
swTrapInfoIpType = _SwTrapInfoIpType_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 9),
    _SwTrapInfoIpType_Type()
)
swTrapInfoIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoIpType.setStatus("current")
_SwTrapInfoPrivMsg_Type = DisplayString
_SwTrapInfoPrivMsg_Object = MibScalar
swTrapInfoPrivMsg = _SwTrapInfoPrivMsg_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 10),
    _SwTrapInfoPrivMsg_Type()
)
swTrapInfoPrivMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoPrivMsg.setStatus("current")
_SwTrapInfoIpAddress_Type = IpAddress
_SwTrapInfoIpAddress_Object = MibScalar
swTrapInfoIpAddress = _SwTrapInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 11),
    _SwTrapInfoIpAddress_Type()
)
swTrapInfoIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoIpAddress.setStatus("current")
_SwTrapInfoSaName_Type = DisplayString
_SwTrapInfoSaName_Object = MibScalar
swTrapInfoSaName = _SwTrapInfoSaName_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 12),
    _SwTrapInfoSaName_Type()
)
swTrapInfoSaName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoSaName.setStatus("current")
_SwTrapInfoFwSrlNumber_Type = DisplayString
_SwTrapInfoFwSrlNumber_Object = MibScalar
swTrapInfoFwSrlNumber = _SwTrapInfoFwSrlNumber_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 13),
    _SwTrapInfoFwSrlNumber_Type()
)
swTrapInfoFwSrlNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoFwSrlNumber.setStatus("current")


class _SwTrapInfoSaStatus_Type(Integer32):
    """Custom type swTrapInfoSaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_SwTrapInfoSaStatus_Type.__name__ = "Integer32"
_SwTrapInfoSaStatus_Object = MibScalar
swTrapInfoSaStatus = _SwTrapInfoSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 14),
    _SwTrapInfoSaStatus_Type()
)
swTrapInfoSaStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoSaStatus.setStatus("current")
_SwTrapInfoSrcAddrBegin_Type = IpAddress
_SwTrapInfoSrcAddrBegin_Object = MibScalar
swTrapInfoSrcAddrBegin = _SwTrapInfoSrcAddrBegin_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 15),
    _SwTrapInfoSrcAddrBegin_Type()
)
swTrapInfoSrcAddrBegin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoSrcAddrBegin.setStatus("current")
_SwTrapInfoSrcAddrEnd_Type = IpAddress
_SwTrapInfoSrcAddrEnd_Object = MibScalar
swTrapInfoSrcAddrEnd = _SwTrapInfoSrcAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 16),
    _SwTrapInfoSrcAddrEnd_Type()
)
swTrapInfoSrcAddrEnd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoSrcAddrEnd.setStatus("current")
_SwTrapInfoDstAddrBegin_Type = IpAddress
_SwTrapInfoDstAddrBegin_Object = MibScalar
swTrapInfoDstAddrBegin = _SwTrapInfoDstAddrBegin_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 17),
    _SwTrapInfoDstAddrBegin_Type()
)
swTrapInfoDstAddrBegin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoDstAddrBegin.setStatus("current")
_SwTrapInfoDstAddrEnd_Type = IpAddress
_SwTrapInfoDstAddrEnd_Object = MibScalar
swTrapInfoDstAddrEnd = _SwTrapInfoDstAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 18),
    _SwTrapInfoDstAddrEnd_Type()
)
swTrapInfoDstAddrEnd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoDstAddrEnd.setStatus("current")
_SwTrapInfoGateway_Type = IpAddress
_SwTrapInfoGateway_Object = MibScalar
swTrapInfoGateway = _SwTrapInfoGateway_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 19),
    _SwTrapInfoGateway_Type()
)
swTrapInfoGateway.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoGateway.setStatus("current")
_SwTrapInfoIsDHCPCentral_Type = Integer32
_SwTrapInfoIsDHCPCentral_Object = MibScalar
swTrapInfoIsDHCPCentral = _SwTrapInfoIsDHCPCentral_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 20),
    _SwTrapInfoIsDHCPCentral_Type()
)
swTrapInfoIsDHCPCentral.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoIsDHCPCentral.setStatus("current")
_SwTrapInfoSrcResolvedHostName_Type = DisplayString
_SwTrapInfoSrcResolvedHostName_Object = MibScalar
swTrapInfoSrcResolvedHostName = _SwTrapInfoSrcResolvedHostName_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 21),
    _SwTrapInfoSrcResolvedHostName_Type()
)
swTrapInfoSrcResolvedHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoSrcResolvedHostName.setStatus("current")
_SwTrapInfoDstResolvedHostName_Type = DisplayString
_SwTrapInfoDstResolvedHostName_Object = MibScalar
swTrapInfoDstResolvedHostName = _SwTrapInfoDstResolvedHostName_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 22),
    _SwTrapInfoDstResolvedHostName_Type()
)
swTrapInfoDstResolvedHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoDstResolvedHostName.setStatus("current")
_SwTrapInfoSrcInterface_Type = Unsigned32
_SwTrapInfoSrcInterface_Object = MibScalar
swTrapInfoSrcInterface = _SwTrapInfoSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 23),
    _SwTrapInfoSrcInterface_Type()
)
swTrapInfoSrcInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoSrcInterface.setStatus("current")
_SwTrapInfoDstInterface_Type = Unsigned32
_SwTrapInfoDstInterface_Object = MibScalar
swTrapInfoDstInterface = _SwTrapInfoDstInterface_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 24),
    _SwTrapInfoDstInterface_Type()
)
swTrapInfoDstInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoDstInterface.setStatus("current")
_SwTrapInfoClientUserName_Type = DisplayString
_SwTrapInfoClientUserName_Object = MibScalar
swTrapInfoClientUserName = _SwTrapInfoClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 1, 1, 25),
    _SwTrapInfoClientUserName_Type()
)
swTrapInfoClientUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTrapInfoClientUserName.setStatus("current")
_SonicwallFwTrapRoot_ObjectIdentity = ObjectIdentity
sonicwallFwTrapRoot = _SonicwallFwTrapRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2)
)
_SnmpTraps_ObjectIdentity = ObjectIdentity
snmpTraps = _SnmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 1, 1, 5)
)

# Managed Objects groups


# Notification objects

swFwTrapAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 1)
)
swFwTrapAttack.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapAttack.setStatus(
        "current"
    )

swFwTrapSysError = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 2)
)
swFwTrapSysError.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapSysError.setStatus(
        "current"
    )

swFwTrapBlkWebSite = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 3)
)
swFwTrapBlkWebSite.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapBlkWebSite.setStatus(
        "current"
    )

swFwTrapIpsecTunnel = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 4)
)
swFwTrapIpsecTunnel.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSaName"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoFwSrlNumber"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSaStatus"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcAddrBegin"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcAddrEnd"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstAddrBegin"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstAddrEnd"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoGateway"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoIsDHCPCentral"))
)
if mibBuilder.loadTexts:
    swFwTrapIpsecTunnel.setStatus(
        "current"
    )

swFwTrapWlanIDS = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 5)
)
swFwTrapWlanIDS.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapWlanIDS.setStatus(
        "current"
    )

swFwTrapSysEnv = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 6)
)
swFwTrapSysEnv.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapSysEnv.setStatus(
        "current"
    )

swFwTrapEnhNone = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 100)
)
swFwTrapEnhNone.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhNone.setStatus(
        "current"
    )

swFwTrapEnhUnused = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 101)
)
swFwTrapEnhUnused.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhUnused.setStatus(
        "current"
    )

swFwTrapEnhLegacySystemMaintenance = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 102)
)
swFwTrapEnhLegacySystemMaintenance.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacySystemMaintenance.setStatus(
        "current"
    )

swFwTrapEnhLegacySystemErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 103)
)
swFwTrapEnhLegacySystemErrors.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacySystemErrors.setStatus(
        "current"
    )

swFwTrapEnhLegacyBlockedWebSites = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 104)
)
swFwTrapEnhLegacyBlockedWebSites.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacyBlockedWebSites.setStatus(
        "current"
    )

swFwTrapEnhLegacyBlockedJavaEtc = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 105)
)
swFwTrapEnhLegacyBlockedJavaEtc.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacyBlockedJavaEtc.setStatus(
        "current"
    )

swFwTrapEnhLegacyUserActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 106)
)
swFwTrapEnhLegacyUserActivity.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacyUserActivity.setStatus(
        "current"
    )

swFwTrapEnhLegacyDeniedLanIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 107)
)
swFwTrapEnhLegacyDeniedLanIp.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacyDeniedLanIp.setStatus(
        "current"
    )

swFwTrapEnhLegacyAttacks = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 108)
)
swFwTrapEnhLegacyAttacks.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacyAttacks.setStatus(
        "current"
    )

swFwTrapEnhLegacyDroppedTcp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 109)
)
swFwTrapEnhLegacyDroppedTcp.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacyDroppedTcp.setStatus(
        "current"
    )

swFwTrapEnhLegacyDroppedUdp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 110)
)
swFwTrapEnhLegacyDroppedUdp.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacyDroppedUdp.setStatus(
        "current"
    )

swFwTrapEnhLegacyDroppedIcmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 111)
)
swFwTrapEnhLegacyDroppedIcmp.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacyDroppedIcmp.setStatus(
        "current"
    )

swFwTrapEnhLegacyNetworkDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 112)
)
swFwTrapEnhLegacyNetworkDebug.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacyNetworkDebug.setStatus(
        "current"
    )

swFwTrapEnhLegacySystemEnvironment = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 113)
)
swFwTrapEnhLegacySystemEnvironment.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacySystemEnvironment.setStatus(
        "current"
    )

swFwTrapEnhLegacyVpnTunnelStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 114)
)
swFwTrapEnhLegacyVpnTunnelStatus.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSaName"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoFwSrlNumber"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSaStatus"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcAddrBegin"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcAddrEnd"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstAddrBegin"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstAddrEnd"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoGateway"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoIsDHCPCentral"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacyVpnTunnelStatus.setStatus(
        "current"
    )

swFwTrapEnhLegacy80211bManagement = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 115)
)
swFwTrapEnhLegacy80211bManagement.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacy80211bManagement.setStatus(
        "current"
    )

swFwTrapEnhAuthAccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 116)
)
swFwTrapEnhAuthAccess.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhAuthAccess.setStatus(
        "current"
    )

swFwTrapEnhBootp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 117)
)
swFwTrapEnhBootp.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhBootp.setStatus(
        "current"
    )

swFwTrapEnhCrypt = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 118)
)
swFwTrapEnhCrypt.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhCrypt.setStatus(
        "current"
    )

swFwTrapEnhDhcpc = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 119)
)
swFwTrapEnhDhcpc.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhDhcpc.setStatus(
        "current"
    )

swFwTrapEnhDhcpr = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 120)
)
swFwTrapEnhDhcpr.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhDhcpr.setStatus(
        "current"
    )

swFwTrapEnhFwEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 121)
)
swFwTrapEnhFwEvent.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhFwEvent.setStatus(
        "current"
    )

swFwTrapEnhFwHardware = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 122)
)
swFwTrapEnhFwHardware.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhFwHardware.setStatus(
        "current"
    )

swFwTrapEnhFwLogging = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 123)
)
swFwTrapEnhFwLogging.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhFwLogging.setStatus(
        "current"
    )

swFwTrapEnhFwRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 124)
)
swFwTrapEnhFwRule.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhFwRule.setStatus(
        "current"
    )

swFwTrapEnhGms = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 125)
)
swFwTrapEnhGms.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhGms.setStatus(
        "current"
    )

swFwTrapEnhHa = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 126)
)
swFwTrapEnhHa.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhHa.setStatus(
        "current"
    )

swFwTrapEnhIntrusionDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 127)
)
swFwTrapEnhIntrusionDetection.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcIpAddress"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcPort"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcInterface"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcResolvedHostName"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstIpAddress"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstPort"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstInterface"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstResolvedHostName"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoClientUserName"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhIntrusionDetection.setStatus(
        "current"
    )

swFwTrapEnhL2tpClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 128)
)
swFwTrapEnhL2tpClient.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhL2tpClient.setStatus(
        "current"
    )

swFwTrapEnhL2tpServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 129)
)
swFwTrapEnhL2tpServer.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhL2tpServer.setStatus(
        "current"
    )

swFwTrapEnhNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 130)
)
swFwTrapEnhNetwork.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcIpAddress"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcPort"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcInterface"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcResolvedHostName"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstIpAddress"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstPort"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstInterface"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstResolvedHostName"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoClientUserName"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhNetwork.setStatus(
        "current"
    )

swFwTrapEnhNetworkAccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 131)
)
swFwTrapEnhNetworkAccess.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcIpAddress"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcPort"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcInterface"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcResolvedHostName"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstIpAddress"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstPort"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstInterface"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstResolvedHostName"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoClientUserName"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhNetworkAccess.setStatus(
        "current"
    )

swFwTrapEnhNetworkTraffic = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 132)
)
swFwTrapEnhNetworkTraffic.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhNetworkTraffic.setStatus(
        "current"
    )

swFwTrapEnhPppDialUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 133)
)
swFwTrapEnhPppDialUp.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhPppDialUp.setStatus(
        "current"
    )

swFwTrapEnhPppoe = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 134)
)
swFwTrapEnhPppoe.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhPppoe.setStatus(
        "current"
    )

swFwTrapEnhPptp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 135)
)
swFwTrapEnhPptp.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhPptp.setStatus(
        "current"
    )

swFwTrapEnhRadius = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 136)
)
swFwTrapEnhRadius.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhRadius.setStatus(
        "current"
    )

swFwTrapEnhRip = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 137)
)
swFwTrapEnhRip.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhRip.setStatus(
        "current"
    )

swFwTrapEnhSecurityServices = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 138)
)
swFwTrapEnhSecurityServices.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcIpAddress"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcPort"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcInterface"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoSrcResolvedHostName"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstIpAddress"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstPort"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstInterface"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoDstResolvedHostName"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoClientUserName"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhSecurityServices.setStatus(
        "current"
    )

swFwTrapEnhVoip = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 139)
)
swFwTrapEnhVoip.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhVoip.setStatus(
        "current"
    )

swFwTrapEnhVpn = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 140)
)
swFwTrapEnhVpn.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhVpn.setStatus(
        "current"
    )

swFwTrapEnhVpnClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 141)
)
swFwTrapEnhVpnClient.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhVpnClient.setStatus(
        "current"
    )

swFwTrapEnhVpnIke = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 142)
)
swFwTrapEnhVpnIke.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhVpnIke.setStatus(
        "current"
    )

swFwTrapEnhVpnIpsec = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 143)
)
swFwTrapEnhVpnIpsec.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhVpnIpsec.setStatus(
        "current"
    )

swFwTrapEnhVpnPki = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 144)
)
swFwTrapEnhVpnPki.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhVpnPki.setStatus(
        "current"
    )

swFwTrapEnhWanFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 145)
)
swFwTrapEnhWanFailover.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhWanFailover.setStatus(
        "current"
    )

swFwTrapEnhWireless = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 146)
)
swFwTrapEnhWireless.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhWireless.setStatus(
        "current"
    )

swFwTrapEnhSonicPoint = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 147)
)
swFwTrapEnhSonicPoint.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhSonicPoint.setStatus(
        "current"
    )

swFwTrapEnhMcast = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 148)
)
swFwTrapEnhMcast.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhMcast.setStatus(
        "current"
    )

swFwTrapEnhWlanIds = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 149)
)
swFwTrapEnhWlanIds.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhWlanIds.setStatus(
        "current"
    )

swFwTrapEnhLegacyModemDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 150)
)
swFwTrapEnhLegacyModemDebug.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhLegacyModemDebug.setStatus(
        "current"
    )

swFwTrapEnhModemDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 151)
)
swFwTrapEnhModemDebug.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhModemDebug.setStatus(
        "current"
    )

swFwTrapEnhPpp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 152)
)
swFwTrapEnhPpp.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhPpp.setStatus(
        "current"
    )

swFwTrapEnhMsAd = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 153)
)
swFwTrapEnhMsAd.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhMsAd.setStatus(
        "current"
    )

swFwTrapEnhDdns = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 154)
)
swFwTrapEnhDdns.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhDdns.setStatus(
        "current"
    )

swFwTrapEnhRbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 155)
)
swFwTrapEnhRbl.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhRbl.setStatus(
        "current"
    )

swFwTrapEnhARS = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 156)
)
swFwTrapEnhARS.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhARS.setStatus(
        "current"
    )

swFwTrapEnhIpcomp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 157)
)
swFwTrapEnhIpcomp.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhIpcomp.setStatus(
        "current"
    )

swFwTrapEnhCia = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 158)
)
swFwTrapEnhCia.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhCia.setStatus(
        "current"
    )

swFwTrapEnhRFManagement = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 159)
)
swFwTrapEnhRFManagement.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhRFManagement.setStatus(
        "current"
    )

swFwTrapEnhDynAddrObjs = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 160)
)
swFwTrapEnhDynAddrObjs.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhDynAddrObjs.setStatus(
        "current"
    )

swFwTrapEnhApplicationFirewall = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 161)
)
swFwTrapEnhApplicationFirewall.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhApplicationFirewall.setStatus(
        "current"
    )

swFwTrapEnhSslvpn = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 162)
)
swFwTrapEnhSslvpn.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhSslvpn.setStatus(
        "current"
    )

swFwTrapEnhSonicPointN = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 163)
)
swFwTrapEnhSonicPointN.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhSonicPointN.setStatus(
        "current"
    )

swFwTrapEnhAntispam = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 164)
)
swFwTrapEnhAntispam.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhAntispam.setStatus(
        "current"
    )

swFwTrapEnhNetworkMonitor = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 165)
)
swFwTrapEnhNetworkMonitor.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhNetworkMonitor.setStatus(
        "current"
    )

swFwTrapEnhDhcpServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 166)
)
swFwTrapEnhDhcpServer.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhDhcpServer.setStatus(
        "current"
    )

swFwTrapEnhFtp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 167)
)
swFwTrapEnhFtp.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhFtp.setStatus(
        "current"
    )

swFwTrapEnhDPISSL = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 168)
)
swFwTrapEnhDPISSL.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhDPISSL.setStatus(
        "current"
    )

swFwTrapEnhApplicationControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 169)
)
swFwTrapEnhApplicationControl.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhApplicationControl.setStatus(
        "current"
    )

swFwTrapEnhWanAcceleration = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 1, 1, 2, 0, 170)
)
swFwTrapEnhWanAcceleration.setObjects(
      *(("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapType"),
        ("SONICWALL-FIREWALL-TRAP-MIB", "swTrapInfoTrapDescription"))
)
if mibBuilder.loadTexts:
    swFwTrapEnhWanAcceleration.setStatus(
        "current"
    )

coldStart = NotificationType(
    (1, 3, 6, 1, 6, 3, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        "current"
    )

warmStart = NotificationType(
    (1, 3, 6, 1, 6, 3, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    warmStart.setStatus(
        "current"
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 6, 3, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-FIREWALL-TRAP-MIB",
    **{"MacAddress": MacAddress,
       "FwTrapType": FwTrapType,
       "sonicwallFwTrapModule": sonicwallFwTrapModule,
       "sonicwallFwTrapInfo": sonicwallFwTrapInfo,
       "swTrapInfoTable": swTrapInfoTable,
       "swTrapInfoTrapType": swTrapInfoTrapType,
       "swTrapInfoTrapDescription": swTrapInfoTrapDescription,
       "swTrapInfoSrcIpAddress": swTrapInfoSrcIpAddress,
       "swTrapInfoDstIpAddress": swTrapInfoDstIpAddress,
       "swTrapInfoSrcPort": swTrapInfoSrcPort,
       "swTrapInfoDstPort": swTrapInfoDstPort,
       "swTrapInfoSrcMacAddress": swTrapInfoSrcMacAddress,
       "swTrapInfoDstMacAddress": swTrapInfoDstMacAddress,
       "swTrapInfoIpType": swTrapInfoIpType,
       "swTrapInfoPrivMsg": swTrapInfoPrivMsg,
       "swTrapInfoIpAddress": swTrapInfoIpAddress,
       "swTrapInfoSaName": swTrapInfoSaName,
       "swTrapInfoFwSrlNumber": swTrapInfoFwSrlNumber,
       "swTrapInfoSaStatus": swTrapInfoSaStatus,
       "swTrapInfoSrcAddrBegin": swTrapInfoSrcAddrBegin,
       "swTrapInfoSrcAddrEnd": swTrapInfoSrcAddrEnd,
       "swTrapInfoDstAddrBegin": swTrapInfoDstAddrBegin,
       "swTrapInfoDstAddrEnd": swTrapInfoDstAddrEnd,
       "swTrapInfoGateway": swTrapInfoGateway,
       "swTrapInfoIsDHCPCentral": swTrapInfoIsDHCPCentral,
       "swTrapInfoSrcResolvedHostName": swTrapInfoSrcResolvedHostName,
       "swTrapInfoDstResolvedHostName": swTrapInfoDstResolvedHostName,
       "swTrapInfoSrcInterface": swTrapInfoSrcInterface,
       "swTrapInfoDstInterface": swTrapInfoDstInterface,
       "swTrapInfoClientUserName": swTrapInfoClientUserName,
       "sonicwallFwTrapRoot": sonicwallFwTrapRoot,
       "swFwTrapAttack": swFwTrapAttack,
       "swFwTrapSysError": swFwTrapSysError,
       "swFwTrapBlkWebSite": swFwTrapBlkWebSite,
       "swFwTrapIpsecTunnel": swFwTrapIpsecTunnel,
       "swFwTrapWlanIDS": swFwTrapWlanIDS,
       "swFwTrapSysEnv": swFwTrapSysEnv,
       "swFwTrapEnhNone": swFwTrapEnhNone,
       "swFwTrapEnhUnused": swFwTrapEnhUnused,
       "swFwTrapEnhLegacySystemMaintenance": swFwTrapEnhLegacySystemMaintenance,
       "swFwTrapEnhLegacySystemErrors": swFwTrapEnhLegacySystemErrors,
       "swFwTrapEnhLegacyBlockedWebSites": swFwTrapEnhLegacyBlockedWebSites,
       "swFwTrapEnhLegacyBlockedJavaEtc": swFwTrapEnhLegacyBlockedJavaEtc,
       "swFwTrapEnhLegacyUserActivity": swFwTrapEnhLegacyUserActivity,
       "swFwTrapEnhLegacyDeniedLanIp": swFwTrapEnhLegacyDeniedLanIp,
       "swFwTrapEnhLegacyAttacks": swFwTrapEnhLegacyAttacks,
       "swFwTrapEnhLegacyDroppedTcp": swFwTrapEnhLegacyDroppedTcp,
       "swFwTrapEnhLegacyDroppedUdp": swFwTrapEnhLegacyDroppedUdp,
       "swFwTrapEnhLegacyDroppedIcmp": swFwTrapEnhLegacyDroppedIcmp,
       "swFwTrapEnhLegacyNetworkDebug": swFwTrapEnhLegacyNetworkDebug,
       "swFwTrapEnhLegacySystemEnvironment": swFwTrapEnhLegacySystemEnvironment,
       "swFwTrapEnhLegacyVpnTunnelStatus": swFwTrapEnhLegacyVpnTunnelStatus,
       "swFwTrapEnhLegacy80211bManagement": swFwTrapEnhLegacy80211bManagement,
       "swFwTrapEnhAuthAccess": swFwTrapEnhAuthAccess,
       "swFwTrapEnhBootp": swFwTrapEnhBootp,
       "swFwTrapEnhCrypt": swFwTrapEnhCrypt,
       "swFwTrapEnhDhcpc": swFwTrapEnhDhcpc,
       "swFwTrapEnhDhcpr": swFwTrapEnhDhcpr,
       "swFwTrapEnhFwEvent": swFwTrapEnhFwEvent,
       "swFwTrapEnhFwHardware": swFwTrapEnhFwHardware,
       "swFwTrapEnhFwLogging": swFwTrapEnhFwLogging,
       "swFwTrapEnhFwRule": swFwTrapEnhFwRule,
       "swFwTrapEnhGms": swFwTrapEnhGms,
       "swFwTrapEnhHa": swFwTrapEnhHa,
       "swFwTrapEnhIntrusionDetection": swFwTrapEnhIntrusionDetection,
       "swFwTrapEnhL2tpClient": swFwTrapEnhL2tpClient,
       "swFwTrapEnhL2tpServer": swFwTrapEnhL2tpServer,
       "swFwTrapEnhNetwork": swFwTrapEnhNetwork,
       "swFwTrapEnhNetworkAccess": swFwTrapEnhNetworkAccess,
       "swFwTrapEnhNetworkTraffic": swFwTrapEnhNetworkTraffic,
       "swFwTrapEnhPppDialUp": swFwTrapEnhPppDialUp,
       "swFwTrapEnhPppoe": swFwTrapEnhPppoe,
       "swFwTrapEnhPptp": swFwTrapEnhPptp,
       "swFwTrapEnhRadius": swFwTrapEnhRadius,
       "swFwTrapEnhRip": swFwTrapEnhRip,
       "swFwTrapEnhSecurityServices": swFwTrapEnhSecurityServices,
       "swFwTrapEnhVoip": swFwTrapEnhVoip,
       "swFwTrapEnhVpn": swFwTrapEnhVpn,
       "swFwTrapEnhVpnClient": swFwTrapEnhVpnClient,
       "swFwTrapEnhVpnIke": swFwTrapEnhVpnIke,
       "swFwTrapEnhVpnIpsec": swFwTrapEnhVpnIpsec,
       "swFwTrapEnhVpnPki": swFwTrapEnhVpnPki,
       "swFwTrapEnhWanFailover": swFwTrapEnhWanFailover,
       "swFwTrapEnhWireless": swFwTrapEnhWireless,
       "swFwTrapEnhSonicPoint": swFwTrapEnhSonicPoint,
       "swFwTrapEnhMcast": swFwTrapEnhMcast,
       "swFwTrapEnhWlanIds": swFwTrapEnhWlanIds,
       "swFwTrapEnhLegacyModemDebug": swFwTrapEnhLegacyModemDebug,
       "swFwTrapEnhModemDebug": swFwTrapEnhModemDebug,
       "swFwTrapEnhPpp": swFwTrapEnhPpp,
       "swFwTrapEnhMsAd": swFwTrapEnhMsAd,
       "swFwTrapEnhDdns": swFwTrapEnhDdns,
       "swFwTrapEnhRbl": swFwTrapEnhRbl,
       "swFwTrapEnhARS": swFwTrapEnhARS,
       "swFwTrapEnhIpcomp": swFwTrapEnhIpcomp,
       "swFwTrapEnhCia": swFwTrapEnhCia,
       "swFwTrapEnhRFManagement": swFwTrapEnhRFManagement,
       "swFwTrapEnhDynAddrObjs": swFwTrapEnhDynAddrObjs,
       "swFwTrapEnhApplicationFirewall": swFwTrapEnhApplicationFirewall,
       "swFwTrapEnhSslvpn": swFwTrapEnhSslvpn,
       "swFwTrapEnhSonicPointN": swFwTrapEnhSonicPointN,
       "swFwTrapEnhAntispam": swFwTrapEnhAntispam,
       "swFwTrapEnhNetworkMonitor": swFwTrapEnhNetworkMonitor,
       "swFwTrapEnhDhcpServer": swFwTrapEnhDhcpServer,
       "swFwTrapEnhFtp": swFwTrapEnhFtp,
       "swFwTrapEnhDPISSL": swFwTrapEnhDPISSL,
       "swFwTrapEnhApplicationControl": swFwTrapEnhApplicationControl,
       "swFwTrapEnhWanAcceleration": swFwTrapEnhWanAcceleration,
       "snmpTraps": snmpTraps,
       "coldStart": coldStart,
       "warmStart": warmStart,
       "authenticationFailure": authenticationFailure}
)
