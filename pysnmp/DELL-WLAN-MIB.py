# SNMP MIB module (DELL-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-WLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:06 2024
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 enterprises,
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
    "enterprises",
    "iso",
    "snmpModules")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_PowerConnect_ObjectIdentity = ObjectIdentity
powerConnect = _PowerConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895)
)
_W_650_ObjectIdentity = ObjectIdentity
w_650 = _W_650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5001)
)
_W_651_ObjectIdentity = ObjectIdentity
w_651 = _W_651_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5002)
)
_W_3200_ObjectIdentity = ObjectIdentity
w_3200 = _W_3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5003)
)
_W_3400_ObjectIdentity = ObjectIdentity
w_3400 = _W_3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5004)
)
_W_3600_ObjectIdentity = ObjectIdentity
w_3600 = _W_3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5005)
)
_W_AP92_ObjectIdentity = ObjectIdentity
w_AP92 = _W_AP92_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5006)
)
_W_AP93_ObjectIdentity = ObjectIdentity
w_AP93 = _W_AP93_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5007)
)
_W_AP105_ObjectIdentity = ObjectIdentity
w_AP105 = _W_AP105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5008)
)
_W_AP124_ObjectIdentity = ObjectIdentity
w_AP124 = _W_AP124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5009)
)
_W_AP125_ObjectIdentity = ObjectIdentity
w_AP125 = _W_AP125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5010)
)
_W_RAP5_ObjectIdentity = ObjectIdentity
w_RAP5 = _W_RAP5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5011)
)
_W_RAP5WN_ObjectIdentity = ObjectIdentity
w_RAP5WN = _W_RAP5WN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5012)
)
_W_RAP2_ObjectIdentity = ObjectIdentity
w_RAP2 = _W_RAP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5013)
)
_W_620_ObjectIdentity = ObjectIdentity
w_620 = _W_620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5014)
)
_W_6000M3_ObjectIdentity = ObjectIdentity
w_6000M3 = _W_6000M3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5015)
)
_W_AP68_ObjectIdentity = ObjectIdentity
w_AP68 = _W_AP68_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5016)
)
_W_AP68P_ObjectIdentity = ObjectIdentity
w_AP68P = _W_AP68P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5017)
)
_W_AP175P_ObjectIdentity = ObjectIdentity
w_AP175P = _W_AP175P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5018)
)
_W_AP175AC_ObjectIdentity = ObjectIdentity
w_AP175AC = _W_AP175AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5019)
)
_W_AP175DC_ObjectIdentity = ObjectIdentity
w_AP175DC = _W_AP175DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5020)
)
_W_AP134_ObjectIdentity = ObjectIdentity
w_AP134 = _W_AP134_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5021)
)
_W_AP135_ObjectIdentity = ObjectIdentity
w_AP135 = _W_AP135_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5022)
)
_W_AP93H_ObjectIdentity = ObjectIdentity
w_AP93H = _W_AP93H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5023)
)
_W_AP104_ObjectIdentity = ObjectIdentity
w_AP104 = _W_AP104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5024)
)
_W_IAP3WN_ObjectIdentity = ObjectIdentity
w_IAP3WN = _W_IAP3WN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5025)
)
_W_IAP3WNP_ObjectIdentity = ObjectIdentity
w_IAP3WNP = _W_IAP3WNP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5026)
)
_W_7210_ObjectIdentity = ObjectIdentity
w_7210 = _W_7210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5027)
)
_W_7220_ObjectIdentity = ObjectIdentity
w_7220 = _W_7220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5028)
)
_W_7240_ObjectIdentity = ObjectIdentity
w_7240 = _W_7240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5029)
)
_W_IAP108_ObjectIdentity = ObjectIdentity
w_IAP108 = _W_IAP108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5031)
)
_W_IAP109_ObjectIdentity = ObjectIdentity
w_IAP109 = _W_IAP109_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5032)
)
_W_AP224_ObjectIdentity = ObjectIdentity
w_AP224 = _W_AP224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5033)
)
_W_AP225_ObjectIdentity = ObjectIdentity
w_AP225 = _W_AP225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5034)
)
_W_IAP155_ObjectIdentity = ObjectIdentity
w_IAP155 = _W_IAP155_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5035)
)
_W_IAP155P_ObjectIdentity = ObjectIdentity
w_IAP155P = _W_IAP155P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5036)
)
_W_AP114_ObjectIdentity = ObjectIdentity
w_AP114 = _W_AP114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5037)
)
_W_AP115_ObjectIdentity = ObjectIdentity
w_AP115 = _W_AP115_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5038)
)
_W_AP274_ObjectIdentity = ObjectIdentity
w_AP274 = _W_AP274_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5039)
)
_W_AP275_ObjectIdentity = ObjectIdentity
w_AP275 = _W_AP275_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5040)
)
_W_AP214_ObjectIdentity = ObjectIdentity
w_AP214 = _W_AP214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5041)
)
_W_AP215_ObjectIdentity = ObjectIdentity
w_AP215 = _W_AP215_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5042)
)
_W_7005_ObjectIdentity = ObjectIdentity
w_7005 = _W_7005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5043)
)
_W_7010_ObjectIdentity = ObjectIdentity
w_7010 = _W_7010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5044)
)
_W_AP103_ObjectIdentity = ObjectIdentity
w_AP103 = _W_AP103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5045)
)
_W_AP103H_ObjectIdentity = ObjectIdentity
w_AP103H = _W_AP103H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5046)
)
_W_AP204_ObjectIdentity = ObjectIdentity
w_AP204 = _W_AP204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5047)
)
_W_AP205_ObjectIdentity = ObjectIdentity
w_AP205 = _W_AP205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5048)
)
_W_7030_ObjectIdentity = ObjectIdentity
w_7030 = _W_7030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5049)
)
_W_7205_ObjectIdentity = ObjectIdentity
w_7205 = _W_7205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5050)
)
_W_7024_ObjectIdentity = ObjectIdentity
w_7024 = _W_7024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5051)
)
_W_AP277_ObjectIdentity = ObjectIdentity
w_AP277 = _W_AP277_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5052)
)
_W_AP228_ObjectIdentity = ObjectIdentity
w_AP228 = _W_AP228_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5054)
)
_W_AP205H_ObjectIdentity = ObjectIdentity
w_AP205H = _W_AP205H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5055)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-WLAN-MIB",
    **{"dell": dell,
       "powerConnect": powerConnect,
       "w-650": w_650,
       "w-651": w_651,
       "w-3200": w_3200,
       "w-3400": w_3400,
       "w-3600": w_3600,
       "w-AP92": w_AP92,
       "w-AP93": w_AP93,
       "w-AP105": w_AP105,
       "w-AP124": w_AP124,
       "w-AP125": w_AP125,
       "w-RAP5": w_RAP5,
       "w-RAP5WN": w_RAP5WN,
       "w-RAP2": w_RAP2,
       "w-620": w_620,
       "w-6000M3": w_6000M3,
       "w-AP68": w_AP68,
       "w-AP68P": w_AP68P,
       "w-AP175P": w_AP175P,
       "w-AP175AC": w_AP175AC,
       "w-AP175DC": w_AP175DC,
       "w-AP134": w_AP134,
       "w-AP135": w_AP135,
       "w-AP93H": w_AP93H,
       "w-AP104": w_AP104,
       "w-IAP3WN": w_IAP3WN,
       "w-IAP3WNP": w_IAP3WNP,
       "w-7210": w_7210,
       "w-7220": w_7220,
       "w-7240": w_7240,
       "w-IAP108": w_IAP108,
       "w-IAP109": w_IAP109,
       "w-AP224": w_AP224,
       "w-AP225": w_AP225,
       "w-IAP155": w_IAP155,
       "w-IAP155P": w_IAP155P,
       "w-AP114": w_AP114,
       "w-AP115": w_AP115,
       "w-AP274": w_AP274,
       "w-AP275": w_AP275,
       "w-AP214": w_AP214,
       "w-AP215": w_AP215,
       "w-7005": w_7005,
       "w-7010": w_7010,
       "w-AP103": w_AP103,
       "w-AP103H": w_AP103H,
       "w-AP204": w_AP204,
       "w-AP205": w_AP205,
       "w-7030": w_7030,
       "w-7205": w_7205,
       "w-7024": w_7024,
       "w-AP277": w_AP277,
       "w-AP228": w_AP228,
       "w-AP205H": w_AP205H}
)
