# SNMP MIB module (CTRON-OIDS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-OIDS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:19 2024
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
 enterprises,
 iso) = mibBuilder.importSymbols(
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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_NamingTree_ObjectIdentity = ObjectIdentity
namingTree = _NamingTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3)
)
_ChassisType_ObjectIdentity = ObjectIdentity
chassisType = _ChassisType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1)
)
_CtUnknown_ObjectIdentity = ObjectIdentity
ctUnknown = _CtUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 1)
)
_CtMMAC8_ObjectIdentity = ObjectIdentity
ctMMAC8 = _CtMMAC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 2)
)
_CtMMAC5_ObjectIdentity = ObjectIdentity
ctMMAC5 = _CtMMAC5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 3)
)
_CtMMAC3_ObjectIdentity = ObjectIdentity
ctMMAC3 = _CtMMAC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 4)
)
_CtMINIMMAC_ObjectIdentity = ObjectIdentity
ctMINIMMAC = _CtMINIMMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 5)
)
_CtMRXI_ObjectIdentity = ObjectIdentity
ctMRXI = _CtMRXI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 6)
)
_CtM3FNBShunt_ObjectIdentity = ObjectIdentity
ctM3FNBShunt = _CtM3FNBShunt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 7)
)
_CtM5FNBShunt_ObjectIdentity = ObjectIdentity
ctM5FNBShunt = _CtM5FNBShunt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 8)
)
_CtM8FNB_ObjectIdentity = ObjectIdentity
ctM8FNB = _CtM8FNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 9)
)
_CtNonFNB_ObjectIdentity = ObjectIdentity
ctNonFNB = _CtNonFNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 10)
)
_CtMMAC3FNBShunt_ObjectIdentity = ObjectIdentity
ctMMAC3FNBShunt = _CtMMAC3FNBShunt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 11)
)
_CtMMAC5FNBShunt_ObjectIdentity = ObjectIdentity
ctMMAC5FNBShunt = _CtMMAC5FNBShunt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 12)
)
_CtMMAC8FNBShunt_ObjectIdentity = ObjectIdentity
ctMMAC8FNBShunt = _CtMMAC8FNBShunt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 13)
)
_CtM8FNBShunt_ObjectIdentity = ObjectIdentity
ctM8FNBShunt = _CtM8FNBShunt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 14)
)
_CtTRXI_ObjectIdentity = ObjectIdentity
ctTRXI = _CtTRXI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 15)
)
_CtStandAlone_ObjectIdentity = ObjectIdentity
ctStandAlone = _CtStandAlone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 16)
)
_CtMMACPlus14_ObjectIdentity = ObjectIdentity
ctMMACPlus14 = _CtMMACPlus14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 17)
)
_CtMMACPlus6_ObjectIdentity = ObjectIdentity
ctMMACPlus6 = _CtMMACPlus6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 18)
)
_CtWanCyberSwitchNE2000_ObjectIdentity = ObjectIdentity
ctWanCyberSwitchNE2000 = _CtWanCyberSwitchNE2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 19)
)
_CtWanCyberSwitchNe4000_ObjectIdentity = ObjectIdentity
ctWanCyberSwitchNe4000 = _CtWanCyberSwitchNe4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 20)
)
_CtWanCyberSwitchNE5000_ObjectIdentity = ObjectIdentity
ctWanCyberSwitchNE5000 = _CtWanCyberSwitchNE5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 1, 21)
)
_ModuleType_ObjectIdentity = ObjectIdentity
moduleType = _ModuleType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2)
)
_MtThinMim1_ObjectIdentity = ObjectIdentity
mtThinMim1 = _MtThinMim1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 16)
)
_MtFDMMIM24_ObjectIdentity = ObjectIdentity
mtFDMMIM24 = _MtFDMMIM24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 32)
)
_MtFDMMIM14to46_ObjectIdentity = ObjectIdentity
mtFDMMIM14to46 = _MtFDMMIM14to46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 33)
)
_MtFDMMIM04To44_ObjectIdentity = ObjectIdentity
mtFDMMIM04To44 = _MtFDMMIM04To44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 34)
)
_MtFDMMIM00_ObjectIdentity = ObjectIdentity
mtFDMMIM00 = _MtFDMMIM00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 35)
)
_MtFDMMIM30_ObjectIdentity = ObjectIdentity
mtFDMMIM30 = _MtFDMMIM30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 39)
)
_MtFDCMIM28_ObjectIdentity = ObjectIdentity
mtFDCMIM28 = _MtFDCMIM28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 40)
)
_MtFDCMIM18_ObjectIdentity = ObjectIdentity
mtFDCMIM18 = _MtFDCMIM18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 41)
)
_MtFDCMIM08_ObjectIdentity = ObjectIdentity
mtFDCMIM08 = _MtFDCMIM08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 42)
)
_MtFDCMIM04_ObjectIdentity = ObjectIdentity
mtFDCMIM04 = _MtFDCMIM04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 43)
)
_MtFDCMIM24_ObjectIdentity = ObjectIdentity
mtFDCMIM24 = _MtFDCMIM24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 44)
)
_MtFDCMIM14_ObjectIdentity = ObjectIdentity
mtFDCMIM14 = _MtFDCMIM14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 45)
)
_MtFDCMIM38_ObjectIdentity = ObjectIdentity
mtFDCMIM38 = _MtFDCMIM38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 46)
)
_MtFDCMIM34_ObjectIdentity = ObjectIdentity
mtFDCMIM34 = _MtFDCMIM34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 47)
)
_MtTRMIM12_ObjectIdentity = ObjectIdentity
mtTRMIM12 = _MtTRMIM12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 48)
)
_MtTRMIM10R_ObjectIdentity = ObjectIdentity
mtTRMIM10R = _MtTRMIM10R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 49)
)
_MtTRMIM22_ObjectIdentity = ObjectIdentity
mtTRMIM22 = _MtTRMIM22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 50)
)
_MtTRMIM20R_ObjectIdentity = ObjectIdentity
mtTRMIM20R = _MtTRMIM20R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 51)
)
_MtTRMIM62A_ObjectIdentity = ObjectIdentity
mtTRMIM62A = _MtTRMIM62A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 52)
)
_MtTRMIM24ToA_ObjectIdentity = ObjectIdentity
mtTRMIM24ToA = _MtTRMIM24ToA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 54)
)
_MtTRMIM22ToA_ObjectIdentity = ObjectIdentity
mtTRMIM22ToA = _MtTRMIM22ToA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 55)
)
_MtTRFMIM28_ObjectIdentity = ObjectIdentity
mtTRFMIM28 = _MtTRFMIM28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 56)
)
_MtTRFMIM22_ObjectIdentity = ObjectIdentity
mtTRFMIM22 = _MtTRFMIM22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 57)
)
_MtTRRMIMA_ObjectIdentity = ObjectIdentity
mtTRRMIMA = _MtTRRMIMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 58)
)
_MtTRFMIM26_ObjectIdentity = ObjectIdentity
mtTRFMIM26 = _MtTRFMIM26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 59)
)
_MtTRMIM34A_ObjectIdentity = ObjectIdentity
mtTRMIM34A = _MtTRMIM34A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 60)
)
_MtTRMIM32A_ObjectIdentity = ObjectIdentity
mtTRMIM32A = _MtTRMIM32A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 61)
)
_MtTRMIM44ToA_ObjectIdentity = ObjectIdentity
mtTRMIM44ToA = _MtTRMIM44ToA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 62)
)
_MtTRMIM42ToA_ObjectIdentity = ObjectIdentity
mtTRMIM42ToA = _MtTRMIM42ToA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 63)
)
_MtTPMIMT1_ObjectIdentity = ObjectIdentity
mtTPMIMT1 = _MtTPMIMT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65)
)
_MtTPMIMT_ObjectIdentity = ObjectIdentity
mtTPMIMT = _MtTPMIMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 66)
)
_MtTPMIMT3_ObjectIdentity = ObjectIdentity
mtTPMIMT3 = _MtTPMIMT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 67)
)
_MtThinMim2_ObjectIdentity = ObjectIdentity
mtThinMim2 = _MtThinMim2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 80)
)
_MtTPMIM24_ObjectIdentity = ObjectIdentity
mtTPMIM24 = _MtTPMIM24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 96)
)
_MtTPMIM22_ObjectIdentity = ObjectIdentity
mtTPMIM22 = _MtTPMIM22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 97)
)
_MtTPMIM34_ObjectIdentity = ObjectIdentity
mtTPMIM34 = _MtTPMIM34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 98)
)
_MtTPMIM32_ObjectIdentity = ObjectIdentity
mtTPMIM32 = _MtTPMIM32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 99)
)
_MtTPRMIM100I_ObjectIdentity = ObjectIdentity
mtTPRMIM100I = _MtTPRMIM100I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 111)
)
_MtTPRMIM33_ObjectIdentity = ObjectIdentity
mtTPRMIM33 = _MtTPRMIM33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 112)
)
_MtTPRMIM36_ObjectIdentity = ObjectIdentity
mtTPRMIM36 = _MtTPRMIM36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 113)
)
_MtCXRMIM_ObjectIdentity = ObjectIdentity
mtCXRMIM = _MtCXRMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 114)
)
_MtFORMIM22_ObjectIdentity = ObjectIdentity
mtFORMIM22 = _MtFORMIM22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 115)
)
_MtTPRMIM20_ObjectIdentity = ObjectIdentity
mtTPRMIM20 = _MtTPRMIM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 116)
)
_MtTPRMIM22_ObjectIdentity = ObjectIdentity
mtTPRMIM22 = _MtTPRMIM22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 117)
)
_MtTPRMIM20S_ObjectIdentity = ObjectIdentity
mtTPRMIM20S = _MtTPRMIM20S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 118)
)
_MtTPRMIM22S_ObjectIdentity = ObjectIdentity
mtTPRMIM22S = _MtTPRMIM22S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 119)
)
_MtTPRMIM33S_ObjectIdentity = ObjectIdentity
mtTPRMIM33S = _MtTPRMIM33S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 120)
)
_MtTPRMIM36S_ObjectIdentity = ObjectIdentity
mtTPRMIM36S = _MtTPRMIM36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 121)
)
_MtCXRMIMs_ObjectIdentity = ObjectIdentity
mtCXRMIMs = _MtCXRMIMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 122)
)
_MtFormim22S_ObjectIdentity = ObjectIdentity
mtFormim22S = _MtFormim22S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 123)
)
_MtFBRMIM26_ObjectIdentity = ObjectIdentity
mtFBRMIM26 = _MtFBRMIM26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 126)
)
_MtFBRMIM22_ObjectIdentity = ObjectIdentity
mtFBRMIM22 = _MtFBRMIM22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 127)
)
_MtFOMIM18_ObjectIdentity = ObjectIdentity
mtFOMIM18 = _MtFOMIM18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 144)
)
_MtFOMIM12_ObjectIdentity = ObjectIdentity
mtFOMIM12 = _MtFOMIM12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 146)
)
_MtFOMIM16_ObjectIdentity = ObjectIdentity
mtFOMIM16 = _MtFOMIM16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 147)
)
_MtFOMIM28_ObjectIdentity = ObjectIdentity
mtFOMIM28 = _MtFOMIM28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 148)
)
_MtFOMIM22_ObjectIdentity = ObjectIdentity
mtFOMIM22 = _MtFOMIM22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 150)
)
_MtFOMIM26_ObjectIdentity = ObjectIdentity
mtFOMIM26 = _MtFOMIM26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 151)
)
_MtFOMIM38_ObjectIdentity = ObjectIdentity
mtFOMIM38 = _MtFOMIM38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 152)
)
_MtFOMIM32_ObjectIdentity = ObjectIdentity
mtFOMIM32 = _MtFOMIM32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 154)
)
_MtFOMIM36_ObjectIdentity = ObjectIdentity
mtFOMIM36 = _MtFOMIM36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 155)
)
_MtMT8MIM_ObjectIdentity = ObjectIdentity
mtMT8MIM = _MtMT8MIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 160)
)
_MtIRM2_ObjectIdentity = ObjectIdentity
mtIRM2 = _MtIRM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 176)
)
_MtIRBM_ObjectIdentity = ObjectIdentity
mtIRBM = _MtIRBM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 177)
)
_MtIRM3_ObjectIdentity = ObjectIdentity
mtIRM3 = _MtIRM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 178)
)
_MtTRMM1_ObjectIdentity = ObjectIdentity
mtTRMM1 = _MtTRMM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 179)
)
_MtTRMM2_ObjectIdentity = ObjectIdentity
mtTRMM2 = _MtTRMM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 180)
)
_MtTRMMIM1_ObjectIdentity = ObjectIdentity
mtTRMMIM1 = _MtTRMMIM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 181)
)
_MtEFDMIM_ObjectIdentity = ObjectIdentity
mtEFDMIM = _MtEFDMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 182)
)
_MtTRMM4_ObjectIdentity = ObjectIdentity
mtTRMM4 = _MtTRMM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 183)
)
_MtTRBMIM_ObjectIdentity = ObjectIdentity
mtTRBMIM = _MtTRBMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 184)
)
_MtEMME_ObjectIdentity = ObjectIdentity
mtEMME = _MtEMME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 185)
)
_MtESXMIM_ObjectIdentity = ObjectIdentity
mtESXMIM = _MtESXMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 186)
)
_MtTRMM_ObjectIdentity = ObjectIdentity
mtTRMM = _MtTRMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 187)
)
_MtTRMMIM2_ObjectIdentity = ObjectIdentity
mtTRMMIM2 = _MtTRMMIM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 188)
)
_MtETWMIM_ObjectIdentity = ObjectIdentity
mtETWMIM = _MtETWMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 189)
)
_MtTRMMIM_ObjectIdentity = ObjectIdentity
mtTRMMIM = _MtTRMMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 190)
)
_MtESXMIMF2_ObjectIdentity = ObjectIdentity
mtESXMIMF2 = _MtESXMIMF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 191)
)
_MtFOT12or22_ObjectIdentity = ObjectIdentity
mtFOT12or22 = _MtFOT12or22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 192)
)
_MtTPTMIM_ObjectIdentity = ObjectIdentity
mtTPTMIM = _MtTPTMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 208)
)
_MtFOT16or26_ObjectIdentity = ObjectIdentity
mtFOT16or26 = _MtFOT16or26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 224)
)
_MtSNACRS232wRS232_ObjectIdentity = ObjectIdentity
mtSNACRS232wRS232 = _MtSNACRS232wRS232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 240)
)
_MtSNACRS232wV35_ObjectIdentity = ObjectIdentity
mtSNACRS232wV35 = _MtSNACRS232wV35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 241)
)
_MtSNACRS232wRS530_ObjectIdentity = ObjectIdentity
mtSNACRS232wRS530 = _MtSNACRS232wRS530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 242)
)
_MtSNACRS232wNoDB_ObjectIdentity = ObjectIdentity
mtSNACRS232wNoDB = _MtSNACRS232wNoDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 243)
)
_MtSNACV35wRS232_ObjectIdentity = ObjectIdentity
mtSNACV35wRS232 = _MtSNACV35wRS232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 244)
)
_MtSNACV35wV35_ObjectIdentity = ObjectIdentity
mtSNACV35wV35 = _MtSNACV35wV35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 245)
)
_MtSNACV35wRS350_ObjectIdentity = ObjectIdentity
mtSNACV35wRS350 = _MtSNACV35wRS350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 246)
)
_MtSNACV35wNoDB_ObjectIdentity = ObjectIdentity
mtSNACV35wNoDB = _MtSNACV35wNoDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 247)
)
_MtSNACRS530wRS232_ObjectIdentity = ObjectIdentity
mtSNACRS530wRS232 = _MtSNACRS530wRS232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 248)
)
_MtSNACRS530wV35_ObjectIdentity = ObjectIdentity
mtSNACRS530wV35 = _MtSNACRS530wV35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 249)
)
_MtSNACRS530wRS530_ObjectIdentity = ObjectIdentity
mtSNACRS530wRS530 = _MtSNACRS530wRS530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 250)
)
_MtSNACRS530wNoDB_ObjectIdentity = ObjectIdentity
mtSNACRS530wNoDB = _MtSNACRS530wNoDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 251)
)
_MtSNACMIMConnectivity_ObjectIdentity = ObjectIdentity
mtSNACMIMConnectivity = _MtSNACMIMConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 252)
)
_MtSNACConnectivityMIM_ObjectIdentity = ObjectIdentity
mtSNACConnectivityMIM = _MtSNACConnectivityMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 253)
)
_MtSNACConnectivity_ObjectIdentity = ObjectIdentity
mtSNACConnectivity = _MtSNACConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 254)
)
_MtNull_ObjectIdentity = ObjectIdentity
mtNull = _MtNull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 255)
)
_MtTRMIMa10R_ObjectIdentity = ObjectIdentity
mtTRMIMa10R = _MtTRMIMa10R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 305)
)
_MtTRMIMa20R_ObjectIdentity = ObjectIdentity
mtTRMIMa20R = _MtTRMIMa20R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 307)
)
_MtTRMIM22ARO_ObjectIdentity = ObjectIdentity
mtTRMIM22ARO = _MtTRMIM22ARO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 311)
)
_MtTRRMIM2A_ObjectIdentity = ObjectIdentity
mtTRRMIM2A = _MtTRRMIM2A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 314)
)
_MtTRMIM24ARO_ObjectIdentity = ObjectIdentity
mtTRMIM24ARO = _MtTRMIM24ARO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 566)
)
_MtTRRMIM4A_ObjectIdentity = ObjectIdentity
mtTRRMIM4A = _MtTRRMIM4A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 570)
)
_MtTRRMIMAT_ObjectIdentity = ObjectIdentity
mtTRRMIMAT = _MtTRRMIMAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 826)
)
_MtTRMIM42ARO_ObjectIdentity = ObjectIdentity
mtTRMIM42ARO = _MtTRMIM42ARO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 831)
)
_MtTRRMIM2AT_ObjectIdentity = ObjectIdentity
mtTRRMIM2AT = _MtTRRMIM2AT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 1082)
)
_MtTRMIM44ARO_ObjectIdentity = ObjectIdentity
mtTRMIM44ARO = _MtTRMIM44ARO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 1086)
)
_MtTRRMIM4AT_ObjectIdentity = ObjectIdentity
mtTRRMIM4AT = _MtTRRMIM4AT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 1338)
)
_MtMPIMX_ObjectIdentity = ObjectIdentity
mtMPIMX = _MtMPIMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65536)
)
_MtMPIMA_ObjectIdentity = ObjectIdentity
mtMPIMA = _MtMPIMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65537)
)
_MtMPIMC_ObjectIdentity = ObjectIdentity
mtMPIMC = _MtMPIMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65538)
)
_MtMPIMT_ObjectIdentity = ObjectIdentity
mtMPIMT = _MtMPIMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65539)
)
_MtMPIMF2_ObjectIdentity = ObjectIdentity
mtMPIMF2 = _MtMPIMF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65540)
)
_MtMPIMF1_ObjectIdentity = ObjectIdentity
mtMPIMF1 = _MtMPIMF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65541)
)
_MtMPIMT1_ObjectIdentity = ObjectIdentity
mtMPIMT1 = _MtMPIMT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65542)
)
_MtMPIMB_ObjectIdentity = ObjectIdentity
mtMPIMB = _MtMPIMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65543)
)
_MtMiniMMAC_ObjectIdentity = ObjectIdentity
mtMiniMMAC = _MtMiniMMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65552)
)
_MtMRXIE_ObjectIdentity = ObjectIdentity
mtMRXIE = _MtMRXIE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65568)
)
_MtMRXI24_ObjectIdentity = ObjectIdentity
mtMRXI24 = _MtMRXI24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65569)
)
_MtMRXI22_ObjectIdentity = ObjectIdentity
mtMRXI22 = _MtMRXI22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65570)
)
_MtMRXI34_ObjectIdentity = ObjectIdentity
mtMRXI34 = _MtMRXI34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65571)
)
_MtMRXI32_ObjectIdentity = ObjectIdentity
mtMRXI32 = _MtMRXI32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65572)
)
_MtMRXI2E_ObjectIdentity = ObjectIdentity
mtMRXI2E = _MtMRXI2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 65584)
)
_MtSPIMX_ObjectIdentity = ObjectIdentity
mtSPIMX = _MtSPIMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 131072)
)
_MtSPIMA_ObjectIdentity = ObjectIdentity
mtSPIMA = _MtSPIMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 131073)
)
_MtSPIMC_ObjectIdentity = ObjectIdentity
mtSPIMC = _MtSPIMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 131074)
)
_MtSPIMT_ObjectIdentity = ObjectIdentity
mtSPIMT = _MtSPIMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 131075)
)
_MtSPIMF2_ObjectIdentity = ObjectIdentity
mtSPIMF2 = _MtSPIMF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 131076)
)
_MtSPIMF1_ObjectIdentity = ObjectIdentity
mtSPIMF1 = _MtSPIMF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 131077)
)
_MtSPIMT1_ObjectIdentity = ObjectIdentity
mtSPIMT1 = _MtSPIMT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 131078)
)
_MtSPIMB_ObjectIdentity = ObjectIdentity
mtSPIMB = _MtSPIMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 131079)
)
_MtEPIMB_ObjectIdentity = ObjectIdentity
mtEPIMB = _MtEPIMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196608)
)
_MtEPIMA_ObjectIdentity = ObjectIdentity
mtEPIMA = _MtEPIMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196609)
)
_MtEPIMC_ObjectIdentity = ObjectIdentity
mtEPIMC = _MtEPIMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196610)
)
_MtEPIMT_ObjectIdentity = ObjectIdentity
mtEPIMT = _MtEPIMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196611)
)
_MtEPIMF2_ObjectIdentity = ObjectIdentity
mtEPIMF2 = _MtEPIMF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196612)
)
_MtEPIMF1_ObjectIdentity = ObjectIdentity
mtEPIMF1 = _MtEPIMF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196613)
)
_MtEPIMT1_ObjectIdentity = ObjectIdentity
mtEPIMT1 = _MtEPIMT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196614)
)
_MtEPIMF3_ObjectIdentity = ObjectIdentity
mtEPIMF3 = _MtEPIMF3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196615)
)
_MtEPIMX_ObjectIdentity = ObjectIdentity
mtEPIMX = _MtEPIMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196616)
)
_MtEPIMTfd_ObjectIdentity = ObjectIdentity
mtEPIMTfd = _MtEPIMTfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196619)
)
_MtEPIMF2fd_ObjectIdentity = ObjectIdentity
mtEPIMF2fd = _MtEPIMF2fd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196620)
)
_MtEPIMF1fd_ObjectIdentity = ObjectIdentity
mtEPIMF1fd = _MtEPIMF1fd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196621)
)
_MtEPIMF3fd_ObjectIdentity = ObjectIdentity
mtEPIMF3fd = _MtEPIMF3fd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196622)
)
_MtEPIMFIXED_ObjectIdentity = ObjectIdentity
mtEPIMFIXED = _MtEPIMFIXED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196623)
)
_MtMRXI_ObjectIdentity = ObjectIdentity
mtMRXI = _MtMRXI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196674)
)
_MtMRXI2_ObjectIdentity = ObjectIdentity
mtMRXI2 = _MtMRXI2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 2, 196675)
)
_SlotClass_ObjectIdentity = ObjectIdentity
slotClass = _SlotClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 3)
)
_CsUnknown_ObjectIdentity = ObjectIdentity
csUnknown = _CsUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 3, 1)
)
_CsPwrSup_ObjectIdentity = ObjectIdentity
csPwrSup = _CsPwrSup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 3, 2)
)
_CsMgmt_ObjectIdentity = ObjectIdentity
csMgmt = _CsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 3, 3)
)
_CsMgmtRelay_ObjectIdentity = ObjectIdentity
csMgmtRelay = _CsMgmtRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 3, 4)
)
_CsMIM_ObjectIdentity = ObjectIdentity
csMIM = _CsMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 3, 5)
)
_BackplaneType_ObjectIdentity = ObjectIdentity
backplaneType = _BackplaneType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 4)
)
_BtUnknown_ObjectIdentity = ObjectIdentity
btUnknown = _BtUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 4, 1)
)
_BtBusA_ObjectIdentity = ObjectIdentity
btBusA = _BtBusA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 4, 2)
)
_BtBusB_ObjectIdentity = ObjectIdentity
btBusB = _BtBusB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 4, 3)
)
_BtBusC_ObjectIdentity = ObjectIdentity
btBusC = _BtBusC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 4, 4)
)
_ComponentType_ObjectIdentity = ObjectIdentity
componentType = _ComponentType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5)
)
_CptUnknown_ObjectIdentity = ObjectIdentity
cptUnknown = _CptUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 1)
)
_CptRepeater_ObjectIdentity = ObjectIdentity
cptRepeater = _CptRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 2)
)
_CptMau_ObjectIdentity = ObjectIdentity
cptMau = _CptMau_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 3)
)
_CptBridge_ObjectIdentity = ObjectIdentity
cptBridge = _CptBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 4)
)
_CptRouter_ObjectIdentity = ObjectIdentity
cptRouter = _CptRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 5)
)
_CptRmon_ObjectIdentity = ObjectIdentity
cptRmon = _CptRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 6)
)
_CptAgent_ObjectIdentity = ObjectIdentity
cptAgent = _CptAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 7)
)
_CptLim_ObjectIdentity = ObjectIdentity
cptLim = _CptLim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 8)
)
_CptHostSvcs_ObjectIdentity = ObjectIdentity
cptHostSvcs = _CptHostSvcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 9)
)
_CptIngMIM_ObjectIdentity = ObjectIdentity
cptIngMIM = _CptIngMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 10)
)
_CptDLM_ObjectIdentity = ObjectIdentity
cptDLM = _CptDLM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 11)
)
_CptMIBNavigator_ObjectIdentity = ObjectIdentity
cptMIBNavigator = _CptMIBNavigator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 12)
)
_CptRmonHost_ObjectIdentity = ObjectIdentity
cptRmonHost = _CptRmonHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 13)
)
_CptRmonCapture_ObjectIdentity = ObjectIdentity
cptRmonCapture = _CptRmonCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 14)
)
_CptMibMgr_ObjectIdentity = ObjectIdentity
cptMibMgr = _CptMibMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 15)
)
_CptFddiSmt_ObjectIdentity = ObjectIdentity
cptFddiSmt = _CptFddiSmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 16)
)
_CptSFPS_ObjectIdentity = ObjectIdentity
cptSFPS = _CptSFPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 17)
)
_CptModuleMgmt_ObjectIdentity = ObjectIdentity
cptModuleMgmt = _CptModuleMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 18)
)
_CptOrphan_ObjectIdentity = ObjectIdentity
cptOrphan = _CptOrphan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 19)
)
_CptATM_ObjectIdentity = ObjectIdentity
cptATM = _CptATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 20)
)
_CptWebview_ObjectIdentity = ObjectIdentity
cptWebview = _CptWebview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 21)
)
_Cpt802p1Q_ObjectIdentity = ObjectIdentity
cpt802p1Q = _Cpt802p1Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 22)
)
_Cpt802p1p_ObjectIdentity = ObjectIdentity
cpt802p1p = _Cpt802p1p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 23)
)
_CptTrafficGen_ObjectIdentity = ObjectIdentity
cptTrafficGen = _CptTrafficGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 5, 24)
)
_ThrPtyModType_ObjectIdentity = ObjectIdentity
thrPtyModType = _ThrPtyModType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 6)
)
_TpMtETSMIM_ObjectIdentity = ObjectIdentity
tpMtETSMIM = _TpMtETSMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 6, 2)
)
_TpMtDNSMIM_ObjectIdentity = ObjectIdentity
tpMtDNSMIM = _TpMtDNSMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 6, 3)
)
_TpMtGatorMIM_ObjectIdentity = ObjectIdentity
tpMtGatorMIM = _TpMtGatorMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 6, 4)
)
_TpMtLanternMIM_ObjectIdentity = ObjectIdentity
tpMtLanternMIM = _TpMtLanternMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 6, 5)
)
_TpMtCRML_ObjectIdentity = ObjectIdentity
tpMtCRML = _TpMtCRML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 6, 6)
)
_TpMtCRM_ObjectIdentity = ObjectIdentity
tpMtCRM = _TpMtCRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 6, 7)
)
_NetworkType_ObjectIdentity = ObjectIdentity
networkType = _NetworkType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7)
)
_NtManagementTypes_ObjectIdentity = ObjectIdentity
ntManagementTypes = _NtManagementTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 10)
)
_NtInbandMgmt_ObjectIdentity = ObjectIdentity
ntInbandMgmt = _NtInbandMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 10, 1)
)
_NtSideBandMgmt_ObjectIdentity = ObjectIdentity
ntSideBandMgmt = _NtSideBandMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 10, 2)
)
_NtOutOfBandMgmt_ObjectIdentity = ObjectIdentity
ntOutOfBandMgmt = _NtOutOfBandMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 7, 10, 3)
)
_PhysicalType_ObjectIdentity = ObjectIdentity
physicalType = _PhysicalType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8)
)
_PortType_ObjectIdentity = ObjectIdentity
portType = _PortType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1)
)
_PortStandard_ObjectIdentity = ObjectIdentity
portStandard = _PortStandard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1)
)
_PortEthernet_ObjectIdentity = ObjectIdentity
portEthernet = _PortEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1)
)
_PortUnknown_ObjectIdentity = ObjectIdentity
portUnknown = _PortUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 1)
)
_PortBNC_ObjectIdentity = ObjectIdentity
portBNC = _PortBNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 2)
)
_PortAUI_ObjectIdentity = ObjectIdentity
portAUI = _PortAUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 3)
)
_PortTrans_ObjectIdentity = ObjectIdentity
portTrans = _PortTrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 4)
)
_PortCTp_ObjectIdentity = ObjectIdentity
portCTp = _PortCTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 5)
)
_PortRJ45_ObjectIdentity = ObjectIdentity
portRJ45 = _PortRJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 6)
)
_PortDb9_ObjectIdentity = ObjectIdentity
portDb9 = _PortDb9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 7)
)
_PortRJ71_ObjectIdentity = ObjectIdentity
portRJ71 = _PortRJ71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 8)
)
_PortMmfSMA_ObjectIdentity = ObjectIdentity
portMmfSMA = _PortMmfSMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 9)
)
_PortMmfST_ObjectIdentity = ObjectIdentity
portMmfST = _PortMmfST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 10)
)
_PortSmfST_ObjectIdentity = ObjectIdentity
portSmfST = _PortSmfST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 11)
)
_PortBPlaneA_ObjectIdentity = ObjectIdentity
portBPlaneA = _PortBPlaneA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 12)
)
_PortBPlaneB_ObjectIdentity = ObjectIdentity
portBPlaneB = _PortBPlaneB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 13)
)
_PortBPlaneC_ObjectIdentity = ObjectIdentity
portBPlaneC = _PortBPlaneC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 14)
)
_PortMmfMTRJb10FL_ObjectIdentity = ObjectIdentity
portMmfMTRJb10FL = _PortMmfMTRJb10FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 1, 15)
)
_PortTokenRing_ObjectIdentity = ObjectIdentity
portTokenRing = _PortTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 2)
)
_PortTRUnknown_ObjectIdentity = ObjectIdentity
portTRUnknown = _PortTRUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 2, 1)
)
_PortLobeUtpRJ45_ObjectIdentity = ObjectIdentity
portLobeUtpRJ45 = _PortLobeUtpRJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 2, 2)
)
_PortLobeStpDb9_ObjectIdentity = ObjectIdentity
portLobeStpDb9 = _PortLobeStpDb9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 2, 3)
)
_PortLobeStpRJ45_ObjectIdentity = ObjectIdentity
portLobeStpRJ45 = _PortLobeStpRJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 2, 4)
)
_PortLobeMmfST_ObjectIdentity = ObjectIdentity
portLobeMmfST = _PortLobeMmfST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 2, 5)
)
_PortLobeSmfST_ObjectIdentity = ObjectIdentity
portLobeSmfST = _PortLobeSmfST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 2, 6)
)
_PortRingpStpDb9_ObjectIdentity = ObjectIdentity
portRingpStpDb9 = _PortRingpStpDb9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 2, 7)
)
_PortRingpMmfST_ObjectIdentity = ObjectIdentity
portRingpMmfST = _PortRingpMmfST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 2, 8)
)
_PortLobeUtpStpRJ45_ObjectIdentity = ObjectIdentity
portLobeUtpStpRJ45 = _PortLobeUtpStpRJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 2, 9)
)
_PortFDDI_ObjectIdentity = ObjectIdentity
portFDDI = _PortFDDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 3)
)
_PortFDDIUnknown_ObjectIdentity = ObjectIdentity
portFDDIUnknown = _PortFDDIUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 3, 1)
)
_PortFDDIMmfMic_ObjectIdentity = ObjectIdentity
portFDDIMmfMic = _PortFDDIMmfMic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 3, 2)
)
_PortFDDIUtpRJ45_ObjectIdentity = ObjectIdentity
portFDDIUtpRJ45 = _PortFDDIUtpRJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 3, 3)
)
_PortFDDIStpRJ45_ObjectIdentity = ObjectIdentity
portFDDIStpRJ45 = _PortFDDIStpRJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 3, 4)
)
_PortFDDISmfMic1_ObjectIdentity = ObjectIdentity
portFDDISmfMic1 = _PortFDDISmfMic1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 3, 5)
)
_PortFDDIMmfSc_ObjectIdentity = ObjectIdentity
portFDDIMmfSc = _PortFDDIMmfSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 3, 6)
)
_PortFDDISmfSc_ObjectIdentity = ObjectIdentity
portFDDISmfSc = _PortFDDISmfSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 3, 7)
)
_PortFDDIMmfSt_ObjectIdentity = ObjectIdentity
portFDDIMmfSt = _PortFDDIMmfSt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 3, 8)
)
_PortFDDISmfSt_ObjectIdentity = ObjectIdentity
portFDDISmfSt = _PortFDDISmfSt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 3, 9)
)
_PortFDDISmLrfSc_ObjectIdentity = ObjectIdentity
portFDDISmLrfSc = _PortFDDISmLrfSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 3, 17)
)
_PortNotPresent_ObjectIdentity = ObjectIdentity
portNotPresent = _PortNotPresent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 4)
)
_PortATM_ObjectIdentity = ObjectIdentity
portATM = _PortATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 5)
)
_PortATM155MMF_ObjectIdentity = ObjectIdentity
portATM155MMF = _PortATM155MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 5, 1)
)
_PortATM155SMF_ObjectIdentity = ObjectIdentity
portATM155SMF = _PortATM155SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 5, 2)
)
_PortBackplane_ObjectIdentity = ObjectIdentity
portBackplane = _PortBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 6)
)
_PortInternal_ObjectIdentity = ObjectIdentity
portInternal = _PortInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 7)
)
_PortFastEthernet_ObjectIdentity = ObjectIdentity
portFastEthernet = _PortFastEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 8)
)
_PortUnknownb100_ObjectIdentity = ObjectIdentity
portUnknownb100 = _PortUnknownb100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 8, 1)
)
_PortRJ45b100TX_ObjectIdentity = ObjectIdentity
portRJ45b100TX = _PortRJ45b100TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 8, 2)
)
_PortRJ45b100T4_ObjectIdentity = ObjectIdentity
portRJ45b100T4 = _PortRJ45b100T4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 8, 3)
)
_PortRJ45b100T2_ObjectIdentity = ObjectIdentity
portRJ45b100T2 = _PortRJ45b100T2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 8, 4)
)
_PortMmfScb100FX_ObjectIdentity = ObjectIdentity
portMmfScb100FX = _PortMmfScb100FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 8, 5)
)
_PortSmfScb100FX_ObjectIdentity = ObjectIdentity
portSmfScb100FX = _PortSmfScb100FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 8, 6)
)
_PortRJ71b100TX_ObjectIdentity = ObjectIdentity
portRJ71b100TX = _PortRJ71b100TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 8, 7)
)
_PortMmfMTRJb100FX_ObjectIdentity = ObjectIdentity
portMmfMTRJb100FX = _PortMmfMTRJb100FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 8, 8)
)
_PortSmfMTRJb100FX_ObjectIdentity = ObjectIdentity
portSmfMTRJb100FX = _PortSmfMTRJb100FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 8, 9)
)
_PortGigEthernet_ObjectIdentity = ObjectIdentity
portGigEthernet = _PortGigEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 9)
)
_PortSc1000SX_ObjectIdentity = ObjectIdentity
portSc1000SX = _PortSc1000SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 9, 1)
)
_PortSc1000LX_ObjectIdentity = ObjectIdentity
portSc1000LX = _PortSc1000LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 9, 2)
)
_PortRJ451000T_ObjectIdentity = ObjectIdentity
portRJ451000T = _PortRJ451000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 1, 9, 3)
)
_PortXpim_ObjectIdentity = ObjectIdentity
portXpim = _PortXpim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2)
)
_PortEpim_ObjectIdentity = ObjectIdentity
portEpim = _PortEpim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1)
)
_PortEpimUnknown_ObjectIdentity = ObjectIdentity
portEpimUnknown = _PortEpimUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 1)
)
_PortEpimAUI_ObjectIdentity = ObjectIdentity
portEpimAUI = _PortEpimAUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 2)
)
_PortEpimBNC_ObjectIdentity = ObjectIdentity
portEpimBNC = _PortEpimBNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 3)
)
_PortEpimRJ45_ObjectIdentity = ObjectIdentity
portEpimRJ45 = _PortEpimRJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 4)
)
_PortEpimMmfST_ObjectIdentity = ObjectIdentity
portEpimMmfST = _PortEpimMmfST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 5)
)
_PortEpimMmfSMA_ObjectIdentity = ObjectIdentity
portEpimMmfSMA = _PortEpimMmfSMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 6)
)
_PortEpimSmfST_ObjectIdentity = ObjectIdentity
portEpimSmfST = _PortEpimSmfST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 8)
)
_PortEpimTrans_ObjectIdentity = ObjectIdentity
portEpimTrans = _PortEpimTrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 9)
)
_PortEpimThirdParty_ObjectIdentity = ObjectIdentity
portEpimThirdParty = _PortEpimThirdParty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 10)
)
_PortEpimThirdPartyBrim_ObjectIdentity = ObjectIdentity
portEpimThirdPartyBrim = _PortEpimThirdPartyBrim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 10, 1)
)
_PortEpimThirdPartyCABO_ObjectIdentity = ObjectIdentity
portEpimThirdPartyCABO = _PortEpimThirdPartyCABO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 10, 1, 1)
)
_PortEpimThirdPartyNonBrim_ObjectIdentity = ObjectIdentity
portEpimThirdPartyNonBrim = _PortEpimThirdPartyNonBrim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 10, 2)
)
_PortEpimThirdPartyUnknown_ObjectIdentity = ObjectIdentity
portEpimThirdPartyUnknown = _PortEpimThirdPartyUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 10, 3)
)
_PortEpimRJ45fd_ObjectIdentity = ObjectIdentity
portEpimRJ45fd = _PortEpimRJ45fd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 12)
)
_PortEpimMmfSTfd_ObjectIdentity = ObjectIdentity
portEpimMmfSTfd = _PortEpimMmfSTfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 13)
)
_PortEpimMmfSMAfd_ObjectIdentity = ObjectIdentity
portEpimMmfSMAfd = _PortEpimMmfSMAfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 14)
)
_PortEpimSmfSTfd_ObjectIdentity = ObjectIdentity
portEpimSmfSTfd = _PortEpimSmfSTfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 15)
)
_PortEpimHWAUI_ObjectIdentity = ObjectIdentity
portEpimHWAUI = _PortEpimHWAUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 16)
)
_PortEpim100Tx_ObjectIdentity = ObjectIdentity
portEpim100Tx = _PortEpim100Tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 17)
)
_PortEpim100Fx_ObjectIdentity = ObjectIdentity
portEpim100Fx = _PortEpim100Fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 18)
)
_PortEpim100Fmb_ObjectIdentity = ObjectIdentity
portEpim100Fmb = _PortEpim100Fmb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 19)
)
_PortEpim1002F2_ObjectIdentity = ObjectIdentity
portEpim1002F2 = _PortEpim1002F2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 20)
)
_PortEpim1002F3_ObjectIdentity = ObjectIdentity
portEpim1002F3 = _PortEpim1002F3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 21)
)
_PortEpim1002F4_ObjectIdentity = ObjectIdentity
portEpim1002F4 = _PortEpim1002F4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 1, 22)
)
_PortTpim_ObjectIdentity = ObjectIdentity
portTpim = _PortTpim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 2)
)
_PortTpimUnkown_ObjectIdentity = ObjectIdentity
portTpimUnkown = _PortTpimUnkown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 2, 1)
)
_PortTpimT1_ObjectIdentity = ObjectIdentity
portTpimT1 = _PortTpimT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 2, 2)
)
_PortTpimF2_ObjectIdentity = ObjectIdentity
portTpimF2 = _PortTpimF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 2, 4)
)
_PortTpimT2_ObjectIdentity = ObjectIdentity
portTpimT2 = _PortTpimT2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 2, 5)
)
_PortTpimF3_ObjectIdentity = ObjectIdentity
portTpimF3 = _PortTpimF3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 2, 6)
)
_PortTpimT4_ObjectIdentity = ObjectIdentity
portTpimT4 = _PortTpimT4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 2, 7)
)
_PortFpim_ObjectIdentity = ObjectIdentity
portFpim = _PortFpim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 3)
)
_PortFpimUnknown_ObjectIdentity = ObjectIdentity
portFpimUnknown = _PortFpimUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 3, 1)
)
_PortFpim0_ObjectIdentity = ObjectIdentity
portFpim0 = _PortFpim0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 3, 2)
)
_PortFpim2_ObjectIdentity = ObjectIdentity
portFpim2 = _PortFpim2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 3, 3)
)
_PortFpim4_ObjectIdentity = ObjectIdentity
portFpim4 = _PortFpim4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 3, 4)
)
_PortFpim5_ObjectIdentity = ObjectIdentity
portFpim5 = _PortFpim5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 3, 5)
)
_PortFpim1_ObjectIdentity = ObjectIdentity
portFpim1 = _PortFpim1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 3, 6)
)
_PortFpim7_ObjectIdentity = ObjectIdentity
portFpim7 = _PortFpim7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 3, 7)
)
_PortFpim8_ObjectIdentity = ObjectIdentity
portFpim8 = _PortFpim8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 3, 8)
)
_PortFpim9_ObjectIdentity = ObjectIdentity
portFpim9 = _PortFpim9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 3, 9)
)
_PortApim_ObjectIdentity = ObjectIdentity
portApim = _PortApim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4)
)
_PortApim02_ObjectIdentity = ObjectIdentity
portApim02 = _PortApim02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 1)
)
_PortApim11_ObjectIdentity = ObjectIdentity
portApim11 = _PortApim11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 2)
)
_PortApim21_ObjectIdentity = ObjectIdentity
portApim21 = _PortApim21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 3)
)
_PortApim29_ObjectIdentity = ObjectIdentity
portApim29 = _PortApim29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 4)
)
_PortApim67_ObjectIdentity = ObjectIdentity
portApim67 = _PortApim67_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 5)
)
_PortApim28_ObjectIdentity = ObjectIdentity
portApim28 = _PortApim28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 6)
)
_PortApim22_ObjectIdentity = ObjectIdentity
portApim22 = _PortApim22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 7)
)
_PortApimUnknown_ObjectIdentity = ObjectIdentity
portApimUnknown = _PortApimUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 8)
)
_PortApim29LR_ObjectIdentity = ObjectIdentity
portApim29LR = _PortApim29LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 9)
)
_PortApim31_ObjectIdentity = ObjectIdentity
portApim31 = _PortApim31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 10)
)
_PortApim39_ObjectIdentity = ObjectIdentity
portApim39 = _PortApim39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 11)
)
_PortApim39LR_ObjectIdentity = ObjectIdentity
portApim39LR = _PortApim39LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 4, 12)
)
_PortWpim_ObjectIdentity = ObjectIdentity
portWpim = _PortWpim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5)
)
_PortWpimUnknown_ObjectIdentity = ObjectIdentity
portWpimUnknown = _PortWpimUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 1)
)
_PortWpimT1_ObjectIdentity = ObjectIdentity
portWpimT1 = _PortWpimT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 2)
)
_PortWpimE1_ObjectIdentity = ObjectIdentity
portWpimE1 = _PortWpimE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 3)
)
_PortWpimSy_ObjectIdentity = ObjectIdentity
portWpimSy = _PortWpimSy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 4)
)
_PortWpimDDS_ObjectIdentity = ObjectIdentity
portWpimDDS = _PortWpimDDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 5)
)
_PortWpimDI_ObjectIdentity = ObjectIdentity
portWpimDI = _PortWpimDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 6)
)
_PortWpimHDSL_ObjectIdentity = ObjectIdentity
portWpimHDSL = _PortWpimHDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 7)
)
_PortWpimBRI_ObjectIdentity = ObjectIdentity
portWpimBRI = _PortWpimBRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 8)
)
_PortWpimDS30_ObjectIdentity = ObjectIdentity
portWpimDS30 = _PortWpimDS30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 9)
)
_PortWpimDataCapableDI_ObjectIdentity = ObjectIdentity
portWpimDataCapableDI = _PortWpimDataCapableDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 10)
)
_PortWpimT1DDS_ObjectIdentity = ObjectIdentity
portWpimT1DDS = _PortWpimT1DDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 11)
)
_PortWpimRDDS_ObjectIdentity = ObjectIdentity
portWpimRDDS = _PortWpimRDDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 12)
)
_PortWpimRT1_ObjectIdentity = ObjectIdentity
portWpimRT1 = _PortWpimRT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 13)
)
_PortWpimRE1_ObjectIdentity = ObjectIdentity
portWpimRE1 = _PortWpimRE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 5, 14)
)
_PortFEpim_ObjectIdentity = ObjectIdentity
portFEpim = _PortFEpim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6)
)
_PortFEUnknown_ObjectIdentity = ObjectIdentity
portFEUnknown = _PortFEUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6, 1)
)
_PortFE100TxUTP_ObjectIdentity = ObjectIdentity
portFE100TxUTP = _PortFE100TxUTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6, 2)
)
_PortFE100TxSTP_ObjectIdentity = ObjectIdentity
portFE100TxSTP = _PortFE100TxSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6, 3)
)
_PortFE100Fx_ObjectIdentity = ObjectIdentity
portFE100Fx = _PortFE100Fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6, 4)
)
_PortFE100VG4_ObjectIdentity = ObjectIdentity
portFE100VG4 = _PortFE100VG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6, 5)
)
_PortFE100VGF_ObjectIdentity = ObjectIdentity
portFE100VGF = _PortFE100VGF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6, 6)
)
_PortFE100F3_ObjectIdentity = ObjectIdentity
portFE100F3 = _PortFE100F3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6, 7)
)
_PortFE100S1_ObjectIdentity = ObjectIdentity
portFE100S1 = _PortFE100S1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6, 8)
)
_PortFE100S3_ObjectIdentity = ObjectIdentity
portFE100S3 = _PortFE100S3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6, 9)
)
_PortFE100S5_ObjectIdentity = ObjectIdentity
portFE100S5 = _PortFE100S5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6, 10)
)
_PortFE100LH_ObjectIdentity = ObjectIdentity
portFE100LH = _PortFE100LH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 6, 11)
)
_PortGpim_ObjectIdentity = ObjectIdentity
portGpim = _PortGpim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7)
)
_PortGpimF01_ObjectIdentity = ObjectIdentity
portGpimF01 = _PortGpimF01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 1)
)
_PortGpimF09_ObjectIdentity = ObjectIdentity
portGpimF09 = _PortGpimF09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 2)
)
_PortGpimS41_ObjectIdentity = ObjectIdentity
portGpimS41 = _PortGpimS41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 3)
)
_PortGpimS49_ObjectIdentity = ObjectIdentity
portGpimS49 = _PortGpimS49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 4)
)
_PortGpimS51_ObjectIdentity = ObjectIdentity
portGpimS51 = _PortGpimS51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 5)
)
_PortGpimS59_ObjectIdentity = ObjectIdentity
portGpimS59 = _PortGpimS59_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 6)
)
_PortGpimS31_ObjectIdentity = ObjectIdentity
portGpimS31 = _PortGpimS31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 7)
)
_PortGpimS39_ObjectIdentity = ObjectIdentity
portGpimS39 = _PortGpimS39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 8)
)
_PortGpim01_ObjectIdentity = ObjectIdentity
portGpim01 = _PortGpim01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 9)
)
_PortGpim04_ObjectIdentity = ObjectIdentity
portGpim04 = _PortGpim04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 10)
)
_PortGpim09_ObjectIdentity = ObjectIdentity
portGpim09 = _PortGpim09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 11)
)
_PortGpim08_ObjectIdentity = ObjectIdentity
portGpim08 = _PortGpim08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 7, 12)
)
_PortVapim_ObjectIdentity = ObjectIdentity
portVapim = _PortVapim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 8)
)
_PortVapim31_ObjectIdentity = ObjectIdentity
portVapim31 = _PortVapim31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 8, 1)
)
_PortVapim39_ObjectIdentity = ObjectIdentity
portVapim39 = _PortVapim39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 8, 2)
)
_PortVapim39LR_ObjectIdentity = ObjectIdentity
portVapim39LR = _PortVapim39LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 2, 8, 3)
)
_PortXnim_ObjectIdentity = ObjectIdentity
portXnim = _PortXnim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3)
)
_PortAnim_ObjectIdentity = ObjectIdentity
portAnim = _PortAnim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1)
)
_PortAnim21p3_ObjectIdentity = ObjectIdentity
portAnim21p3 = _PortAnim21p3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 1)
)
_PortAnim29p3_ObjectIdentity = ObjectIdentity
portAnim29p3 = _PortAnim29p3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 2)
)
_PortAnim22p4_ObjectIdentity = ObjectIdentity
portAnim22p4 = _PortAnim22p4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 3)
)
_PortAnim31p2_ObjectIdentity = ObjectIdentity
portAnim31p2 = _PortAnim31p2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 4)
)
_PortAnim39p2_ObjectIdentity = ObjectIdentity
portAnim39p2 = _PortAnim39p2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 5)
)
_PortAnim29p4LR_ObjectIdentity = ObjectIdentity
portAnim29p4LR = _PortAnim29p4LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 6)
)
_PortAnim29p3LR_ObjectIdentity = ObjectIdentity
portAnim29p3LR = _PortAnim29p3LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 7)
)
_PortAnim39p2LR_ObjectIdentity = ObjectIdentity
portAnim39p2LR = _PortAnim39p2LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 8)
)
_PortAnim59p1LR_ObjectIdentity = ObjectIdentity
portAnim59p1LR = _PortAnim59p1LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 9)
)
_PortAnim21p4_ObjectIdentity = ObjectIdentity
portAnim21p4 = _PortAnim21p4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 10)
)
_PortAnim29p4_ObjectIdentity = ObjectIdentity
portAnim29p4 = _PortAnim29p4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 11)
)
_PortAnim67p2_ObjectIdentity = ObjectIdentity
portAnim67p2 = _PortAnim67p2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 12)
)
_PortAnim77p2_ObjectIdentity = ObjectIdentity
portAnim77p2 = _PortAnim77p2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 13)
)
_PortAnim51p1_ObjectIdentity = ObjectIdentity
portAnim51p1 = _PortAnim51p1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 14)
)
_PortAnim59p1_ObjectIdentity = ObjectIdentity
portAnim59p1 = _PortAnim59p1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 3, 1, 15)
)
_PortVirtualType_ObjectIdentity = ObjectIdentity
portVirtualType = _PortVirtualType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 4)
)
_PortVirtualTypeSvc_ObjectIdentity = ObjectIdentity
portVirtualTypeSvc = _PortVirtualTypeSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 4, 1)
)
_PortVirtualTypePvcLlc_ObjectIdentity = ObjectIdentity
portVirtualTypePvcLlc = _PortVirtualTypePvcLlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 4, 2)
)
_PortVirtualTypePvcVcmux_ObjectIdentity = ObjectIdentity
portVirtualTypePvcVcmux = _PortVirtualTypePvcVcmux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 4, 3)
)
_PortVirtualSMB_ObjectIdentity = ObjectIdentity
portVirtualSMB = _PortVirtualSMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 5)
)
_PortCATV_ObjectIdentity = ObjectIdentity
portCATV = _PortCATV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 6)
)
_PortCATVUnknown_ObjectIdentity = ObjectIdentity
portCATVUnknown = _PortCATVUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 6, 1)
)
_Port75ohmFemaleFType_ObjectIdentity = ObjectIdentity
port75ohmFemaleFType = _Port75ohmFemaleFType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 1, 6, 2)
)
_HardwareType_ObjectIdentity = ObjectIdentity
hardwareType = _HardwareType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2)
)
_ChipType_ObjectIdentity = ObjectIdentity
chipType = _ChipType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1)
)
_FddiMACDP83261_ObjectIdentity = ObjectIdentity
fddiMACDP83261 = _FddiMACDP83261_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 1)
)
_FddiPortDP83251_ObjectIdentity = ObjectIdentity
fddiPortDP83251 = _FddiPortDP83251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 2)
)
_I960sa_ObjectIdentity = ObjectIdentity
i960sa = _I960sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 3)
)
_I960ca_ObjectIdentity = ObjectIdentity
i960ca = _I960ca_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 4)
)
_I960cf_ObjectIdentity = ObjectIdentity
i960cf = _I960cf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 5)
)
_I960ha_ObjectIdentity = ObjectIdentity
i960ha = _I960ha_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 6)
)
_I960hd_ObjectIdentity = ObjectIdentity
i960hd = _I960hd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 7)
)
_I960ht_ObjectIdentity = ObjectIdentity
i960ht = _I960ht_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 8)
)
_PowerPC603_ObjectIdentity = ObjectIdentity
powerPC603 = _PowerPC603_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 9)
)
_PowerPC603e_ObjectIdentity = ObjectIdentity
powerPC603e = _PowerPC603e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 10)
)
_PowerPC604_ObjectIdentity = ObjectIdentity
powerPC604 = _PowerPC604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 11)
)
_PowerPC740_ObjectIdentity = ObjectIdentity
powerPC740 = _PowerPC740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 12)
)
_PowerMIPS5000_ObjectIdentity = ObjectIdentity
powerMIPS5000 = _PowerMIPS5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 13)
)
_PowerPC8241_ObjectIdentity = ObjectIdentity
powerPC8241 = _PowerPC8241_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 14)
)
_PowerPC8245_ObjectIdentity = ObjectIdentity
powerPC8245 = _PowerPC8245_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 2, 1, 15)
)
_PsMonitorTypes_ObjectIdentity = ObjectIdentity
psMonitorTypes = _PsMonitorTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3)
)
_PowerSupplyMonitors_ObjectIdentity = ObjectIdentity
powerSupplyMonitors = _PowerSupplyMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 1)
)
_PowerSupplyInputMonitor_ObjectIdentity = ObjectIdentity
powerSupplyInputMonitor = _PowerSupplyInputMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 1, 1)
)
_PowerSupplyTermConvInput_ObjectIdentity = ObjectIdentity
powerSupplyTermConvInput = _PowerSupplyTermConvInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 1, 2)
)
_PowerSupplyLogicConvInput_ObjectIdentity = ObjectIdentity
powerSupplyLogicConvInput = _PowerSupplyLogicConvInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 1, 3)
)
_PowerSupplyTermOutput_ObjectIdentity = ObjectIdentity
powerSupplyTermOutput = _PowerSupplyTermOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 1, 4)
)
_PowerSupplyLogicOutput_ObjectIdentity = ObjectIdentity
powerSupplyLogicOutput = _PowerSupplyLogicOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 1, 5)
)
_PowerSupplyHighVoltageOutput_ObjectIdentity = ObjectIdentity
powerSupplyHighVoltageOutput = _PowerSupplyHighVoltageOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 1, 6)
)
_ChassisPowerMonitors_ObjectIdentity = ObjectIdentity
chassisPowerMonitors = _ChassisPowerMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 2)
)
_ChassisHighVoltageRail_ObjectIdentity = ObjectIdentity
chassisHighVoltageRail = _ChassisHighVoltageRail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 2, 1)
)
_ChassisLogicRail_ObjectIdentity = ObjectIdentity
chassisLogicRail = _ChassisLogicRail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 2, 2)
)
_ChassisTermRail_ObjectIdentity = ObjectIdentity
chassisTermRail = _ChassisTermRail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 2, 3)
)
_ModulePowerMonitors_ObjectIdentity = ObjectIdentity
modulePowerMonitors = _ModulePowerMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 3)
)
_ModuleHighVoltageInput_ObjectIdentity = ObjectIdentity
moduleHighVoltageInput = _ModuleHighVoltageInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 3, 1)
)
_ModuleLogicVoltageOutput_ObjectIdentity = ObjectIdentity
moduleLogicVoltageOutput = _ModuleLogicVoltageOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 3, 2)
)
_ModuleAux1Output_ObjectIdentity = ObjectIdentity
moduleAux1Output = _ModuleAux1Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 3, 3)
)
_ModuleAux2Output_ObjectIdentity = ObjectIdentity
moduleAux2Output = _ModuleAux2Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 8, 3, 3, 4)
)
_MtExpanded_ObjectIdentity = ObjectIdentity
mtExpanded = _MtExpanded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9)
)
_MtThrdParty_ObjectIdentity = ObjectIdentity
mtThrdParty = _MtThrdParty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1)
)
_TpAEnet_ObjectIdentity = ObjectIdentity
tpAEnet = _TpAEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 2)
)
_MtPassaggioMim_ObjectIdentity = ObjectIdentity
mtPassaggioMim = _MtPassaggioMim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 2, 1)
)
_TpABorC_ObjectIdentity = ObjectIdentity
tpABorC = _TpABorC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3)
)
_MtCiscoCRM3E_ObjectIdentity = ObjectIdentity
mtCiscoCRM3E = _MtCiscoCRM3E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 1)
)
_MtCrm2RE_ObjectIdentity = ObjectIdentity
mtCrm2RE = _MtCrm2RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 2)
)
_MtSnacMimRS232_ObjectIdentity = ObjectIdentity
mtSnacMimRS232 = _MtSnacMimRS232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 10)
)
_MtSnacMimRS232wRS232DB_ObjectIdentity = ObjectIdentity
mtSnacMimRS232wRS232DB = _MtSnacMimRS232wRS232DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 11)
)
_MtSnacMimRS232wV35DB_ObjectIdentity = ObjectIdentity
mtSnacMimRS232wV35DB = _MtSnacMimRS232wV35DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 12)
)
_MtSnacMimRS232wRS422DB_ObjectIdentity = ObjectIdentity
mtSnacMimRS232wRS422DB = _MtSnacMimRS232wRS422DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 13)
)
_MtSnacMimv35_ObjectIdentity = ObjectIdentity
mtSnacMimv35 = _MtSnacMimv35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 14)
)
_MtSnacMimv35wRS232DB_ObjectIdentity = ObjectIdentity
mtSnacMimv35wRS232DB = _MtSnacMimv35wRS232DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 15)
)
_MtSnacMimV35wV35DB_ObjectIdentity = ObjectIdentity
mtSnacMimV35wV35DB = _MtSnacMimV35wV35DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 16)
)
_MtSnacMimV35wRS422DB_ObjectIdentity = ObjectIdentity
mtSnacMimV35wRS422DB = _MtSnacMimV35wRS422DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 17)
)
_MtSnacMimRS422DB_ObjectIdentity = ObjectIdentity
mtSnacMimRS422DB = _MtSnacMimRS422DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 18)
)
_MtSnacMimRS422wRS232DB_ObjectIdentity = ObjectIdentity
mtSnacMimRS422wRS232DB = _MtSnacMimRS422wRS232DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 19)
)
_MtSnacMimRS422wV35DB_ObjectIdentity = ObjectIdentity
mtSnacMimRS422wV35DB = _MtSnacMimRS422wV35DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 20)
)
_MtSnacMimRS422wRS422DB_ObjectIdentity = ObjectIdentity
mtSnacMimRS422wRS422DB = _MtSnacMimRS422wRS422DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 21)
)
_MtSnacMimSXRS232_ObjectIdentity = ObjectIdentity
mtSnacMimSXRS232 = _MtSnacMimSXRS232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 22)
)
_MtSnacMimSXRS232wRS232DB_ObjectIdentity = ObjectIdentity
mtSnacMimSXRS232wRS232DB = _MtSnacMimSXRS232wRS232DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 23)
)
_MtSnacMimSXRS232wV35DB_ObjectIdentity = ObjectIdentity
mtSnacMimSXRS232wV35DB = _MtSnacMimSXRS232wV35DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 24)
)
_MtSnacMimSXRS232wRS422DB_ObjectIdentity = ObjectIdentity
mtSnacMimSXRS232wRS422DB = _MtSnacMimSXRS232wRS422DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 25)
)
_MtSnacMimSXv35_ObjectIdentity = ObjectIdentity
mtSnacMimSXv35 = _MtSnacMimSXv35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 26)
)
_MtSnacMimSXv35wRS232DB_ObjectIdentity = ObjectIdentity
mtSnacMimSXv35wRS232DB = _MtSnacMimSXv35wRS232DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 27)
)
_MtSnacMimSXV35wV35DB_ObjectIdentity = ObjectIdentity
mtSnacMimSXV35wV35DB = _MtSnacMimSXV35wV35DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 28)
)
_MtSnacMimSXV35wRS422DB_ObjectIdentity = ObjectIdentity
mtSnacMimSXV35wRS422DB = _MtSnacMimSXV35wRS422DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 29)
)
_MtSnacMimSXRS422DB_ObjectIdentity = ObjectIdentity
mtSnacMimSXRS422DB = _MtSnacMimSXRS422DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 30)
)
_MtSnacMimSXRS422wRS232DB_ObjectIdentity = ObjectIdentity
mtSnacMimSXRS422wRS232DB = _MtSnacMimSXRS422wRS232DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 31)
)
_MtSnacMimSXRS422wV35DB_ObjectIdentity = ObjectIdentity
mtSnacMimSXRS422wV35DB = _MtSnacMimSXRS422wV35DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 32)
)
_MtSnacMimSXRS422wRS422DB_ObjectIdentity = ObjectIdentity
mtSnacMimSXRS422wRS422DB = _MtSnacMimSXRS422wRS422DB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 3, 33)
)
_TpABandC_ObjectIdentity = ObjectIdentity
tpABandC = _TpABandC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 4)
)
_TpTrFNB_ObjectIdentity = ObjectIdentity
tpTrFNB = _TpTrFNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5)
)
_MtCiscoCRM3T_ObjectIdentity = ObjectIdentity
mtCiscoCRM3T = _MtCiscoCRM3T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 1)
)
_MtTRMMIM62A_ObjectIdentity = ObjectIdentity
mtTRMMIM62A = _MtTRMMIM62A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 2)
)
_Mt3174MIM_ObjectIdentity = ObjectIdentity
mt3174MIM = _Mt3174MIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 3)
)
_MtSNACmimRS232_ObjectIdentity = ObjectIdentity
mtSNACmimRS232 = _MtSNACmimRS232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 16)
)
_MtSNACmimRS232v35db_ObjectIdentity = ObjectIdentity
mtSNACmimRS232v35db = _MtSNACmimRS232v35db_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 17)
)
_MtSNACmimRS232wRS422db_ObjectIdentity = ObjectIdentity
mtSNACmimRS232wRS422db = _MtSNACmimRS232wRS422db_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 18)
)
_MtSNACmimRS232wodb486_ObjectIdentity = ObjectIdentity
mtSNACmimRS232wodb486 = _MtSNACmimRS232wodb486_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 19)
)
_MtSNACmimv35wRS232db_ObjectIdentity = ObjectIdentity
mtSNACmimv35wRS232db = _MtSNACmimv35wRS232db_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 20)
)
_MtSNACmimv35wv35db_ObjectIdentity = ObjectIdentity
mtSNACmimv35wv35db = _MtSNACmimv35wv35db_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 21)
)
_MtSNACmimv35RS422db_ObjectIdentity = ObjectIdentity
mtSNACmimv35RS422db = _MtSNACmimv35RS422db_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 22)
)
_MtSNACmimv35wodb_ObjectIdentity = ObjectIdentity
mtSNACmimv35wodb = _MtSNACmimv35wodb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 23)
)
_MtSNACmimRS422_ObjectIdentity = ObjectIdentity
mtSNACmimRS422 = _MtSNACmimRS422_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 24)
)
_MtSNACmimRS422wv35db_ObjectIdentity = ObjectIdentity
mtSNACmimRS422wv35db = _MtSNACmimRS422wv35db_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 25)
)
_MtSNACmimRS422wRS422db_ObjectIdentity = ObjectIdentity
mtSNACmimRS422wRS422db = _MtSNACmimRS422wRS422db_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 26)
)
_MtSNACmimrs433_ObjectIdentity = ObjectIdentity
mtSNACmimrs433 = _MtSNACmimrs433_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 5, 27)
)
_TpTrFDDIFNB_ObjectIdentity = ObjectIdentity
tpTrFDDIFNB = _TpTrFDDIFNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 6)
)
_TpTrAEnet_ObjectIdentity = ObjectIdentity
tpTrAEnet = _TpTrAEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 7)
)
_TpTrFDDIAEnet_ObjectIdentity = ObjectIdentity
tpTrFDDIAEnet = _TpTrFDDIAEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 8)
)
_TpATM_ObjectIdentity = ObjectIdentity
tpATM = _TpATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 9)
)
_TpATMMIM_ObjectIdentity = ObjectIdentity
tpATMMIM = _TpATMMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 9, 1)
)
_TpATMMIMx8_ObjectIdentity = ObjectIdentity
tpATMMIMx8 = _TpATMMIMx8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 9, 2)
)
_TpSS1500Modular_ObjectIdentity = ObjectIdentity
tpSS1500Modular = _TpSS1500Modular_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 9, 3)
)
_TpSS1500Compact_ObjectIdentity = ObjectIdentity
tpSS1500Compact = _TpSS1500Compact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 9, 4)
)
_TpStandAlone_ObjectIdentity = ObjectIdentity
tpStandAlone = _TpStandAlone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10)
)
_TpELS10024TX_ObjectIdentity = ObjectIdentity
tpELS10024TX = _TpELS10024TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 1)
)
_TpELS10024TXM_ObjectIdentity = ObjectIdentity
tpELS10024TXM = _TpELS10024TXM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 2)
)
_TpELS10024TXG_ObjectIdentity = ObjectIdentity
tpELS10024TXG = _TpELS10024TXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 3)
)
_TpELH10012_ObjectIdentity = ObjectIdentity
tpELH10012 = _TpELH10012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 4)
)
_TpELH10024_ObjectIdentity = ObjectIdentity
tpELH10024 = _TpELH10024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 5)
)
_TpELS10024FXG_ObjectIdentity = ObjectIdentity
tpELS10024FXG = _TpELS10024FXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 6)
)
_TpELS100S24TX2M_ObjectIdentity = ObjectIdentity
tpELS100S24TX2M = _TpELS100S24TX2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7)
)
_XylogicsMIMs_ObjectIdentity = ObjectIdentity
xylogicsMIMs = _XylogicsMIMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12)
)
_XylogicsCSMIM16_ObjectIdentity = ObjectIdentity
xylogicsCSMIM16 = _XylogicsCSMIM16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 1)
)
_XylogicsCSMIM32_ObjectIdentity = ObjectIdentity
xylogicsCSMIM32 = _XylogicsCSMIM32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 2)
)
_MtCSMIM16m2_ObjectIdentity = ObjectIdentity
mtCSMIM16m2 = _MtCSMIM16m2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 3)
)
_MtMODMIM4_ObjectIdentity = ObjectIdentity
mtMODMIM4 = _MtMODMIM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 5)
)
_MtMODMIM4x4_ObjectIdentity = ObjectIdentity
mtMODMIM4x4 = _MtMODMIM4x4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 7)
)
_MtMODMIM4x8_ObjectIdentity = ObjectIdentity
mtMODMIM4x8 = _MtMODMIM4x8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 9)
)
_MtCSMIM32m2_ObjectIdentity = ObjectIdentity
mtCSMIM32m2 = _MtCSMIM32m2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 10)
)
_MtCSMIMm8T1_ObjectIdentity = ObjectIdentity
mtCSMIMm8T1 = _MtCSMIMm8T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 11)
)
_MtCSMIMm16T1_ObjectIdentity = ObjectIdentity
mtCSMIMm16T1 = _MtCSMIMm16T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 12)
)
_MtCSMIMm24T1_ObjectIdentity = ObjectIdentity
mtCSMIMm24T1 = _MtCSMIMm24T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 13)
)
_MtCSmimBri3_ObjectIdentity = ObjectIdentity
mtCSmimBri3 = _MtCSmimBri3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 14)
)
_MtCSmimBri6_ObjectIdentity = ObjectIdentity
mtCSmimBri6 = _MtCSmimBri6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 12, 15)
)
_MtOlicom_ObjectIdentity = ObjectIdentity
mtOlicom = _MtOlicom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 13)
)
_MtSTS16_20_ObjectIdentity = ObjectIdentity
mtSTS16_20 = _MtSTS16_20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 13, 1)
)
_MtHSTS100_16RM_ObjectIdentity = ObjectIdentity
mtHSTS100_16RM = _MtHSTS100_16RM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 13, 2)
)
_MtTPSoftware_ObjectIdentity = ObjectIdentity
mtTPSoftware = _MtTPSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 14)
)
_MtBIGIP_ObjectIdentity = ObjectIdentity
mtBIGIP = _MtBIGIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 14, 1)
)
_Mt3DNS_ObjectIdentity = ObjectIdentity
mt3DNS = _Mt3DNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 14, 2)
)
_MtChassis_ObjectIdentity = ObjectIdentity
mtChassis = _MtChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2)
)
_CA_ObjectIdentity = ObjectIdentity
cA = _CA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 1)
)
_CABorC_ObjectIdentity = ObjectIdentity
cABorC = _CABorC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 2)
)
_CABandC_ObjectIdentity = ObjectIdentity
cABandC = _CABandC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 3)
)
_CTrFNB_ObjectIdentity = ObjectIdentity
cTrFNB = _CTrFNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 4)
)
_MtTbrmim_ObjectIdentity = ObjectIdentity
mtTbrmim = _MtTbrmim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 4, 1)
)
_CFDDIFNB_ObjectIdentity = ObjectIdentity
cFDDIFNB = _CFDDIFNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 5)
)
_CTrA_ObjectIdentity = ObjectIdentity
cTrA = _CTrA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 6)
)
_MtPCMIM_ObjectIdentity = ObjectIdentity
mtPCMIM = _MtPCMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 6, 1)
)
_CFDDIA_ObjectIdentity = ObjectIdentity
cFDDIA = _CFDDIA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 7)
)
_CNoABorC_ObjectIdentity = ObjectIdentity
cNoABorC = _CNoABorC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 8)
)
_SonixMIM_ObjectIdentity = ObjectIdentity
sonixMIM = _SonixMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 8, 1)
)
_MmacFPS_ObjectIdentity = ObjectIdentity
mmacFPS = _MmacFPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 8, 2)
)
_ThirdPartyBrims_ObjectIdentity = ObjectIdentity
thirdPartyBrims = _ThirdPartyBrims_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 9)
)
_MtCiscoBrimE_ObjectIdentity = ObjectIdentity
mtCiscoBrimE = _MtCiscoBrimE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 9, 1)
)
_MtCiscoBrimTR_ObjectIdentity = ObjectIdentity
mtCiscoBrimTR = _MtCiscoBrimTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 9, 11)
)
_MtXylogicsUCS_ObjectIdentity = ObjectIdentity
mtXylogicsUCS = _MtXylogicsUCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 9, 22)
)
_MtXylogicsUSnac_ObjectIdentity = ObjectIdentity
mtXylogicsUSnac = _MtXylogicsUSnac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 9, 23)
)
_MtXylogicsUSnacT_ObjectIdentity = ObjectIdentity
mtXylogicsUSnacT = _MtXylogicsUSnacT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 9, 24)
)
_MtXylogicsUBrics_ObjectIdentity = ObjectIdentity
mtXylogicsUBrics = _MtXylogicsUBrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 2, 9, 25)
)
_MtEthernet_ObjectIdentity = ObjectIdentity
mtEthernet = _MtEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3)
)
_MtEtherA_ObjectIdentity = ObjectIdentity
mtEtherA = _MtEtherA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 1)
)
_MtEtherRic_ObjectIdentity = ObjectIdentity
mtEtherRic = _MtEtherRic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 2)
)
_MtEtherEPIM_ObjectIdentity = ObjectIdentity
mtEtherEPIM = _MtEtherEPIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 3)
)
_MtEtherStandAlone_ObjectIdentity = ObjectIdentity
mtEtherStandAlone = _MtEtherStandAlone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4)
)
_MtUMMAC22E_ObjectIdentity = ObjectIdentity
mtUMMAC22E = _MtUMMAC22E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 1)
)
_MtUMMAC32E_ObjectIdentity = ObjectIdentity
mtUMMAC32E = _MtUMMAC32E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 2)
)
_MtUMMAC24E_ObjectIdentity = ObjectIdentity
mtUMMAC24E = _MtUMMAC24E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 3)
)
_MtUMMAC34E_ObjectIdentity = ObjectIdentity
mtUMMAC34E = _MtUMMAC34E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 4)
)
_MtSEH22_ObjectIdentity = ObjectIdentity
mtSEH22 = _MtSEH22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 5)
)
_MtSEH32_ObjectIdentity = ObjectIdentity
mtSEH32 = _MtSEH32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 6)
)
_MtSEH24_ObjectIdentity = ObjectIdentity
mtSEH24 = _MtSEH24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 7)
)
_MtSEH34_ObjectIdentity = ObjectIdentity
mtSEH34 = _MtSEH34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 8)
)
_MtNBR620_ObjectIdentity = ObjectIdentity
mtNBR620 = _MtNBR620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 9)
)
_MtSEHi22_ObjectIdentity = ObjectIdentity
mtSEHi22 = _MtSEHi22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 10)
)
_MtSEHi24_ObjectIdentity = ObjectIdentity
mtSEHi24 = _MtSEHi24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 11)
)
_MtSEHi26FB_ObjectIdentity = ObjectIdentity
mtSEHi26FB = _MtSEHi26FB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 12)
)
_MtSEHi22FB_ObjectIdentity = ObjectIdentity
mtSEHi22FB = _MtSEHi22FB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 13)
)
_MtSEHi32_ObjectIdentity = ObjectIdentity
mtSEHi32 = _MtSEHi32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 14)
)
_MtSEHi34_ObjectIdentity = ObjectIdentity
mtSEHi34 = _MtSEHi34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 15)
)
_MtSEH26C_ObjectIdentity = ObjectIdentity
mtSEH26C = _MtSEH26C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 16)
)
_MtSEH22C_ObjectIdentity = ObjectIdentity
mtSEH22C = _MtSEH22C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 17)
)
_MtSEH26FL_ObjectIdentity = ObjectIdentity
mtSEH26FL = _MtSEH26FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 18)
)
_MtSEH22FL_ObjectIdentity = ObjectIdentity
mtSEH22FL = _MtSEH22FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 19)
)
_MtUMMAC26FL_ObjectIdentity = ObjectIdentity
mtUMMAC26FL = _MtUMMAC26FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 20)
)
_MtUMMAC22FL_ObjectIdentity = ObjectIdentity
mtUMMAC22FL = _MtUMMAC22FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 21)
)
_MtNBR220_ObjectIdentity = ObjectIdentity
mtNBR220 = _MtNBR220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 22)
)
_MtNBR420_ObjectIdentity = ObjectIdentity
mtNBR420 = _MtNBR420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 23)
)
_MtSEH22S_ObjectIdentity = ObjectIdentity
mtSEH22S = _MtSEH22S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 24)
)
_MtSEH32S_ObjectIdentity = ObjectIdentity
mtSEH32S = _MtSEH32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 25)
)
_MtSEH24S_ObjectIdentity = ObjectIdentity
mtSEH24S = _MtSEH24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 26)
)
_MtSEH34S_ObjectIdentity = ObjectIdentity
mtSEH34S = _MtSEH34S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 27)
)
_MtSEH26FBS_ObjectIdentity = ObjectIdentity
mtSEH26FBS = _MtSEH26FBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 28)
)
_MtSEH22FBS_ObjectIdentity = ObjectIdentity
mtSEH22FBS = _MtSEH22FBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 29)
)
_MtSEH26CS_ObjectIdentity = ObjectIdentity
mtSEH26CS = _MtSEH26CS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 30)
)
_MtSEH22CS_ObjectIdentity = ObjectIdentity
mtSEH22CS = _MtSEH22CS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 31)
)
_MtSEH26FLS_ObjectIdentity = ObjectIdentity
mtSEH26FLS = _MtSEH26FLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 32)
)
_MtSEH22FLS_ObjectIdentity = ObjectIdentity
mtSEH22FLS = _MtSEH22FLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 33)
)
_MtSEHi22S_ObjectIdentity = ObjectIdentity
mtSEHi22S = _MtSEHi22S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 34)
)
_MtSEHi24S_ObjectIdentity = ObjectIdentity
mtSEHi24S = _MtSEHi24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 35)
)
_MtSEHi32S_ObjectIdentity = ObjectIdentity
mtSEHi32S = _MtSEHi32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 36)
)
_MtSEHi34S_ObjectIdentity = ObjectIdentity
mtSEHi34S = _MtSEHi34S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 37)
)
_MtUMMAC22ES_ObjectIdentity = ObjectIdentity
mtUMMAC22ES = _MtUMMAC22ES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 38)
)
_MtUMMAC32ES_ObjectIdentity = ObjectIdentity
mtUMMAC32ES = _MtUMMAC32ES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 39)
)
_MtUMMAC24ES_ObjectIdentity = ObjectIdentity
mtUMMAC24ES = _MtUMMAC24ES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 40)
)
_MtUMMAC34ES_ObjectIdentity = ObjectIdentity
mtUMMAC34ES = _MtUMMAC34ES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 41)
)
_MtUMMAC22UCSs_ObjectIdentity = ObjectIdentity
mtUMMAC22UCSs = _MtUMMAC22UCSs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 42)
)
_MtUMMAC22EUCS_ObjectIdentity = ObjectIdentity
mtUMMAC22EUCS = _MtUMMAC22EUCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 43)
)
_MtUMMAC22UCSsSnac_ObjectIdentity = ObjectIdentity
mtUMMAC22UCSsSnac = _MtUMMAC22UCSsSnac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 44)
)
_MtUMMAC22EUCSSnac_ObjectIdentity = ObjectIdentity
mtUMMAC22EUCSSnac = _MtUMMAC22EUCSSnac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 45)
)
_MtUMMAC22EBrics_ObjectIdentity = ObjectIdentity
mtUMMAC22EBrics = _MtUMMAC22EBrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 46)
)
_MtUMMAC22ESBrics_ObjectIdentity = ObjectIdentity
mtUMMAC22ESBrics = _MtUMMAC22ESBrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 47)
)
_MtESX1320_ObjectIdentity = ObjectIdentity
mtESX1320 = _MtESX1320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 48)
)
_MtESX1380_ObjectIdentity = ObjectIdentity
mtESX1380 = _MtESX1380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 49)
)
_MtSEHi22FLS_ObjectIdentity = ObjectIdentity
mtSEHi22FLS = _MtSEHi22FLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 50)
)
_MtSEHi26FLS_ObjectIdentity = ObjectIdentity
mtSEHi26FLS = _MtSEHi26FLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 51)
)
_MtSEHi22FL_ObjectIdentity = ObjectIdentity
mtSEHi22FL = _MtSEHi22FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 52)
)
_MtSEHi26FL_ObjectIdentity = ObjectIdentity
mtSEHi26FL = _MtSEHi26FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 53)
)
_MtSEH100Tx22_ObjectIdentity = ObjectIdentity
mtSEH100Tx22 = _MtSEH100Tx22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 54)
)
_MtSEHi100Tx22_ObjectIdentity = ObjectIdentity
mtSEHi100Tx22 = _MtSEHi100Tx22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 55)
)
_Mt8H02p16_ObjectIdentity = ObjectIdentity
mt8H02p16 = _Mt8H02p16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 56)
)
_Mt2E42p27_ObjectIdentity = ObjectIdentity
mt2E42p27 = _Mt2E42p27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 57)
)
_Mt2E42p27R_ObjectIdentity = ObjectIdentity
mt2E42p27R = _Mt2E42p27R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 58)
)
_Mt2E43p27_ObjectIdentity = ObjectIdentity
mt2E43p27 = _Mt2E43p27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 59)
)
_Mt2E43p27R_ObjectIdentity = ObjectIdentity
mt2E43p27R = _Mt2E43p27R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 60)
)
_Mt2E43p51_ObjectIdentity = ObjectIdentity
mt2E43p51 = _Mt2E43p51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 61)
)
_Mt2E43p51R_ObjectIdentity = ObjectIdentity
mt2E43p51R = _Mt2E43p51R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 62)
)
_Mt2H43p51_ObjectIdentity = ObjectIdentity
mt2H43p51 = _Mt2H43p51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 63)
)
_Mt2H43p51R_ObjectIdentity = ObjectIdentity
mt2H43p51R = _Mt2H43p51R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 64)
)
_Mt2E42p27RDC_ObjectIdentity = ObjectIdentity
mt2E42p27RDC = _Mt2E42p27RDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 65)
)
_Mt2E42p27DC_ObjectIdentity = ObjectIdentity
mt2E42p27DC = _Mt2E42p27DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 66)
)
_Mt2M46p04_ObjectIdentity = ObjectIdentity
mt2M46p04 = _Mt2M46p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 67)
)
_Mt2E48p27R_ObjectIdentity = ObjectIdentity
mt2E48p27R = _Mt2E48p27R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 68)
)
_Mt2E48p27_ObjectIdentity = ObjectIdentity
mt2E48p27 = _Mt2E48p27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 69)
)
_Mt2E49p27_ObjectIdentity = ObjectIdentity
mt2E49p27 = _Mt2E49p27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 70)
)
_Mt2E49p27R_ObjectIdentity = ObjectIdentity
mt2E49p27R = _Mt2E49p27R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 71)
)
_Mt2E49p27RDC_ObjectIdentity = ObjectIdentity
mt2E49p27RDC = _Mt2E49p27RDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 72)
)
_Mt2M46p04R_ObjectIdentity = ObjectIdentity
mt2M46p04R = _Mt2M46p04R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 73)
)
_Mt2M46p04RDC_ObjectIdentity = ObjectIdentity
mt2M46p04RDC = _Mt2M46p04RDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 74)
)
_Mt2H28p08R_ObjectIdentity = ObjectIdentity
mt2H28p08R = _Mt2H28p08R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 75)
)
_Mt2H22p08R_ObjectIdentity = ObjectIdentity
mt2H22p08R = _Mt2H22p08R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 76)
)
_Mt2H23p50R_ObjectIdentity = ObjectIdentity
mt2H23p50R = _Mt2H23p50R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 77)
)
_Mt2H33p37R_ObjectIdentity = ObjectIdentity
mt2H33p37R = _Mt2H33p37R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 78)
)
_Mt2H252p25_ObjectIdentity = ObjectIdentity
mt2H252p25 = _Mt2H252p25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 79)
)
_Mt2H252p25R_ObjectIdentity = ObjectIdentity
mt2H252p25R = _Mt2H252p25R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 80)
)
_Mt2M256p04R_ObjectIdentity = ObjectIdentity
mt2M256p04R = _Mt2M256p04R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 81)
)
_Mt2E253p49R_ObjectIdentity = ObjectIdentity
mt2E253p49R = _Mt2E253p49R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 82)
)
_Mt2H258p17R_ObjectIdentity = ObjectIdentity
mt2H258p17R = _Mt2H258p17R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 83)
)
_Mt2H253p25R_ObjectIdentity = ObjectIdentity
mt2H253p25R = _Mt2H253p25R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 84)
)
_Mt2H252p25RDC_ObjectIdentity = ObjectIdentity
mt2H252p25RDC = _Mt2H252p25RDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 85)
)
_Mt2H259p17R_ObjectIdentity = ObjectIdentity
mt2H259p17R = _Mt2H259p17R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 86)
)
_MtELS10082F2_ObjectIdentity = ObjectIdentity
mtELS10082F2 = _MtELS10082F2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 87)
)
_MtELS10024TX2M_ObjectIdentity = ObjectIdentity
mtELS10024TX2M = _MtELS10024TX2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 92)
)
_MtELS10024FX2M_ObjectIdentity = ObjectIdentity
mtELS10024FX2M = _MtELS10024FX2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 93)
)
_MtELS10048TX2M_ObjectIdentity = ObjectIdentity
mtELS10048TX2M = _MtELS10048TX2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 94)
)
_MtELS10008SX1M_ObjectIdentity = ObjectIdentity
mtELS10008SX1M = _MtELS10008SX1M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 95)
)
_MtELS100012SX2M_ObjectIdentity = ObjectIdentity
mtELS100012SX2M = _MtELS100012SX2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 96)
)
_MtELS10016FXG_ObjectIdentity = ObjectIdentity
mtELS10016FXG = _MtELS10016FXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 97)
)
_MtELS100024TX2MA_ObjectIdentity = ObjectIdentity
mtELS100024TX2MA = _MtELS100024TX2MA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 98)
)
_MtELS10024TX1M_ObjectIdentity = ObjectIdentity
mtELS10024TX1M = _MtELS10024TX1M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 4, 99)
)
_EtherSlot1_ObjectIdentity = ObjectIdentity
etherSlot1 = _EtherSlot1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 5)
)
_MtEMME6_ObjectIdentity = ObjectIdentity
mtEMME6 = _MtEMME6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 5, 1)
)
_MtEnetBrim_ObjectIdentity = ObjectIdentity
mtEnetBrim = _MtEnetBrim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 6)
)
_MtBrimUnk_ObjectIdentity = ObjectIdentity
mtBrimUnk = _MtBrimUnk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 6, 1)
)
_MtBrimE6_ObjectIdentity = ObjectIdentity
mtBrimE6 = _MtBrimE6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 6, 2)
)
_Mt100MBEnet_ObjectIdentity = ObjectIdentity
mt100MBEnet = _Mt100MBEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 7)
)
_MtBrimE100_ObjectIdentity = ObjectIdentity
mtBrimE100 = _MtBrimE100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 7, 1)
)
_MtmmacEthernetSmartSwitch_ObjectIdentity = ObjectIdentity
mtmmacEthernetSmartSwitch = _MtmmacEthernetSmartSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 8)
)
_MtSmartMIM216_ObjectIdentity = ObjectIdentity
mtSmartMIM216 = _MtSmartMIM216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 8, 1)
)
_MtEnetHSIM_ObjectIdentity = ObjectIdentity
mtEnetHSIM = _MtEnetHSIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 9)
)
_MtHSIMpG01_ObjectIdentity = ObjectIdentity
mtHSIMpG01 = _MtHSIMpG01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 9, 1)
)
_MtHSIMpG09_ObjectIdentity = ObjectIdentity
mtHSIMpG09 = _MtHSIMpG09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 9, 2)
)
_MtHSIMFE6_ObjectIdentity = ObjectIdentity
mtHSIMFE6 = _MtHSIMFE6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 9, 3)
)
_MtVHSIMG6_ObjectIdentity = ObjectIdentity
mtVHSIMG6 = _MtVHSIMG6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 3, 9, 4)
)
_MtEnetRepeater_ObjectIdentity = ObjectIdentity
mtEnetRepeater = _MtEnetRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 4)
)
_MtEnetABC_ObjectIdentity = ObjectIdentity
mtEnetABC = _MtEnetABC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 4, 1)
)
_MtTPXMIM20_ObjectIdentity = ObjectIdentity
mtTPXMIM20 = _MtTPXMIM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 4, 1, 1)
)
_MtTPXMIM22_ObjectIdentity = ObjectIdentity
mtTPXMIM22 = _MtTPXMIM22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 4, 1, 2)
)
_MtTPXMIM33_ObjectIdentity = ObjectIdentity
mtTPXMIM33 = _MtTPXMIM33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 4, 1, 3)
)
_MtTPXMIM34_ObjectIdentity = ObjectIdentity
mtTPXMIM34 = _MtTPXMIM34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 4, 1, 4)
)
_MtTpxmim20S_ObjectIdentity = ObjectIdentity
mtTpxmim20S = _MtTpxmim20S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 4, 1, 5)
)
_MtTpxmim22S_ObjectIdentity = ObjectIdentity
mtTpxmim22S = _MtTpxmim22S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 4, 1, 6)
)
_MtTpxmim33S_ObjectIdentity = ObjectIdentity
mtTpxmim33S = _MtTpxmim33S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 4, 1, 7)
)
_MtTpxmim34S_ObjectIdentity = ObjectIdentity
mtTpxmim34S = _MtTpxmim34S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 4, 1, 8)
)
_MtTokenRing_ObjectIdentity = ObjectIdentity
mtTokenRing = _MtTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5)
)
_MtTRActive_ObjectIdentity = ObjectIdentity
mtTRActive = _MtTRActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 1)
)
_MtTRMIM22A_ObjectIdentity = ObjectIdentity
mtTRMIM22A = _MtTRMIM22A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 1, 1)
)
_MtTRMIM24A_ObjectIdentity = ObjectIdentity
mtTRMIM24A = _MtTRMIM24A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 1, 2)
)
_MtTRMIM42A_ObjectIdentity = ObjectIdentity
mtTRMIM42A = _MtTRMIM42A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 1, 3)
)
_MtTRMIM44A_ObjectIdentity = ObjectIdentity
mtTRMIM44A = _MtTRMIM44A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 1, 4)
)
_MtTRFMIM32_ObjectIdentity = ObjectIdentity
mtTRFMIM32 = _MtTRFMIM32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 1, 5)
)
_MtTRFMIM36_ObjectIdentity = ObjectIdentity
mtTRFMIM36 = _MtTRFMIM36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 1, 6)
)
_MtTRFMIM38_ObjectIdentity = ObjectIdentity
mtTRFMIM38 = _MtTRFMIM38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 1, 7)
)
_MtTRRepeater_ObjectIdentity = ObjectIdentity
mtTRRepeater = _MtTRRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 2)
)
_MtTRRMIMf2t_ObjectIdentity = ObjectIdentity
mtTRRMIMf2t = _MtTRRMIMf2t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 2, 1)
)
_MtTRRMIMf3t_ObjectIdentity = ObjectIdentity
mtTRRMIMf3t = _MtTRRMIMf3t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 2, 2)
)
_MtTRRMIMat_ObjectIdentity = ObjectIdentity
mtTRRMIMat = _MtTRRMIMat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 2, 3)
)
_MtTRRMIM2at_ObjectIdentity = ObjectIdentity
mtTRRMIM2at = _MtTRRMIM2at_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 2, 4)
)
_MtTRRMIM4at_ObjectIdentity = ObjectIdentity
mtTRRMIM4at = _MtTRRMIM4at_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 2, 5)
)
_MtTPIM_ObjectIdentity = ObjectIdentity
mtTPIM = _MtTPIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 4)
)
_MtTPIMUnk_ObjectIdentity = ObjectIdentity
mtTPIMUnk = _MtTPIMUnk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 4, 1)
)
_MtTPIMT1_ObjectIdentity = ObjectIdentity
mtTPIMT1 = _MtTPIMT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 4, 2)
)
_MtTPIMF2_ObjectIdentity = ObjectIdentity
mtTPIMF2 = _MtTPIMF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 4, 3)
)
_MtTPIMT4_ObjectIdentity = ObjectIdentity
mtTPIMT4 = _MtTPIMT4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 4, 4)
)
_MtTPIMT2_ObjectIdentity = ObjectIdentity
mtTPIMT2 = _MtTPIMT2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 4, 5)
)
_MtTPIMF3_ObjectIdentity = ObjectIdentity
mtTPIMF3 = _MtTPIMF3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 4, 6)
)
_MtTRBrim_ObjectIdentity = ObjectIdentity
mtTRBrim = _MtTRBrim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 5)
)
_MtBrimT6_ObjectIdentity = ObjectIdentity
mtBrimT6 = _MtBrimT6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 5, 1)
)
_MtTRStandAlone_ObjectIdentity = ObjectIdentity
mtTRStandAlone = _MtTRStandAlone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 6)
)
_MtTSX1620_ObjectIdentity = ObjectIdentity
mtTSX1620 = _MtTSX1620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 6, 1)
)
_MtTrxi24_ObjectIdentity = ObjectIdentity
mtTrxi24 = _MtTrxi24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 6, 48)
)
_MtTrxi22_ObjectIdentity = ObjectIdentity
mtTrxi22 = _MtTrxi22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 6, 49)
)
_MtTrxi24A_ObjectIdentity = ObjectIdentity
mtTrxi24A = _MtTrxi24A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 6, 50)
)
_MtTrxi22A_ObjectIdentity = ObjectIdentity
mtTrxi22A = _MtTrxi22A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 6, 51)
)
_MtTrxi44_ObjectIdentity = ObjectIdentity
mtTrxi44 = _MtTrxi44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 6, 56)
)
_MtTrxi42_ObjectIdentity = ObjectIdentity
mtTrxi42 = _MtTrxi42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 6, 57)
)
_MtTrxi44A_ObjectIdentity = ObjectIdentity
mtTrxi44A = _MtTrxi44A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 6, 58)
)
_MtTrxi42A_ObjectIdentity = ObjectIdentity
mtTrxi42A = _MtTrxi42A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 6, 59)
)
_MtTRManagement_ObjectIdentity = ObjectIdentity
mtTRManagement = _MtTRManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 7)
)
_MtTRMMIM4at_ObjectIdentity = ObjectIdentity
mtTRMMIM4at = _MtTRMMIM4at_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 7, 1)
)
_MtTRMMIM2at_ObjectIdentity = ObjectIdentity
mtTRMMIM2at = _MtTRMMIM2at_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 7, 2)
)
_MtTRMMIMF2t_ObjectIdentity = ObjectIdentity
mtTRMMIMF2t = _MtTRMMIMF2t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 7, 3)
)
_MtTRMMIMF3t_ObjectIdentity = ObjectIdentity
mtTRMMIMF3t = _MtTRMMIMF3t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 7, 4)
)
_MtTBRMIM_ObjectIdentity = ObjectIdentity
mtTBRMIM = _MtTBRMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 7, 5)
)
_MtSTH_ObjectIdentity = ObjectIdentity
mtSTH = _MtSTH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 8)
)
_MtSTH44A_ObjectIdentity = ObjectIdentity
mtSTH44A = _MtSTH44A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 8, 68)
)
_MtSTH24A_ObjectIdentity = ObjectIdentity
mtSTH24A = _MtSTH24A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 8, 136)
)
_MtSTH42A_ObjectIdentity = ObjectIdentity
mtSTH42A = _MtSTH42A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 8, 244)
)
_MtSTH22A_ObjectIdentity = ObjectIdentity
mtSTH22A = _MtSTH22A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 8, 248)
)
_MtSTHI_ObjectIdentity = ObjectIdentity
mtSTHI = _MtSTHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 9)
)
_MtSTHI44A_ObjectIdentity = ObjectIdentity
mtSTHI44A = _MtSTHI44A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 9, 68)
)
_MtSTHI24A_ObjectIdentity = ObjectIdentity
mtSTHI24A = _MtSTHI24A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 9, 136)
)
_MtSTHI42A_ObjectIdentity = ObjectIdentity
mtSTHI42A = _MtSTHI42A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 9, 244)
)
_MtSTHI22A_ObjectIdentity = ObjectIdentity
mtSTHI22A = _MtSTHI22A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 9, 248)
)
_MtUMMAC_ObjectIdentity = ObjectIdentity
mtUMMAC = _MtUMMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 10)
)
_MtUMMAC44T_ObjectIdentity = ObjectIdentity
mtUMMAC44T = _MtUMMAC44T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 10, 68)
)
_MtUMMAC24T_ObjectIdentity = ObjectIdentity
mtUMMAC24T = _MtUMMAC24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 10, 136)
)
_MtUMMAC42T_ObjectIdentity = ObjectIdentity
mtUMMAC42T = _MtUMMAC42T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 10, 244)
)
_MtUMMAC22T_ObjectIdentity = ObjectIdentity
mtUMMAC22T = _MtUMMAC22T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 10, 248)
)
_MtTRPortSwitch_ObjectIdentity = ObjectIdentity
mtTRPortSwitch = _MtTRPortSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 11)
)
_MtTRXMIM22A_ObjectIdentity = ObjectIdentity
mtTRXMIM22A = _MtTRXMIM22A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 11, 1)
)
_MtTRXMIM24A_ObjectIdentity = ObjectIdentity
mtTRXMIM24A = _MtTRXMIM24A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 11, 2)
)
_MtTRXMIM42A_ObjectIdentity = ObjectIdentity
mtTRXMIM42A = _MtTRXMIM42A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 11, 3)
)
_MtTRXMIM44A_ObjectIdentity = ObjectIdentity
mtTRXMIM44A = _MtTRXMIM44A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 11, 4)
)
_MtTRXMIM54A_ObjectIdentity = ObjectIdentity
mtTRXMIM54A = _MtTRXMIM54A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 11, 5)
)
_MtTDRMIM22A_ObjectIdentity = ObjectIdentity
mtTDRMIM22A = _MtTDRMIM22A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 11, 7)
)
_MtTDRMIM42A_ObjectIdentity = ObjectIdentity
mtTDRMIM42A = _MtTDRMIM42A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 11, 8)
)
_MtCrm2RT_ObjectIdentity = ObjectIdentity
mtCrm2RT = _MtCrm2RT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 11, 9)
)
_MtTDRMIMAT_ObjectIdentity = ObjectIdentity
mtTDRMIMAT = _MtTDRMIMAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 5, 11, 10)
)
_MtFDDI_ObjectIdentity = ObjectIdentity
mtFDDI = _MtFDDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7)
)
_MtFDDIconcFIBER_ObjectIdentity = ObjectIdentity
mtFDDIconcFIBER = _MtFDDIconcFIBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 1)
)
_MtFDDIconcTWISTED_ObjectIdentity = ObjectIdentity
mtFDDIconcTWISTED = _MtFDDIconcTWISTED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 2)
)
_MtFDCMIM12_ObjectIdentity = ObjectIdentity
mtFDCMIM12 = _MtFDCMIM12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 2, 16)
)
_MtFDCMIM42_ObjectIdentity = ObjectIdentity
mtFDCMIM42 = _MtFDCMIM42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 2, 18)
)
_MtFDCMIM16_ObjectIdentity = ObjectIdentity
mtFDCMIM16 = _MtFDCMIM16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 2, 19)
)
_MtFDCMIM26_ObjectIdentity = ObjectIdentity
mtFDCMIM26 = _MtFDCMIM26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 2, 20)
)
_MtFDCMIM46_ObjectIdentity = ObjectIdentity
mtFDCMIM46 = _MtFDCMIM46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 2, 21)
)
_MtFDCMIM22_ObjectIdentity = ObjectIdentity
mtFDCMIM22 = _MtFDCMIM22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 2, 22)
)
_MtFDCMIM44_ObjectIdentity = ObjectIdentity
mtFDCMIM44 = _MtFDCMIM44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 2, 24)
)
_MtFDCMIM48_ObjectIdentity = ObjectIdentity
mtFDCMIM48 = _MtFDCMIM48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 2, 25)
)
_MtFDDImanagement_ObjectIdentity = ObjectIdentity
mtFDDImanagement = _MtFDDImanagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 3)
)
_MtFDMMIM24mmf_ObjectIdentity = ObjectIdentity
mtFDMMIM24mmf = _MtFDMMIM24mmf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 3, 1)
)
_MtFddiBrim_ObjectIdentity = ObjectIdentity
mtFddiBrim = _MtFddiBrim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 4)
)
_MtBrimFD0_ObjectIdentity = ObjectIdentity
mtBrimFD0 = _MtBrimFD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 4, 1)
)
_MtBrimFD6_ObjectIdentity = ObjectIdentity
mtBrimFD6 = _MtBrimFD6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 4, 2)
)
_MtBrimFD5_ObjectIdentity = ObjectIdentity
mtBrimFD5 = _MtBrimFD5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 4, 3)
)
_MtFddiHsim_ObjectIdentity = ObjectIdentity
mtFddiHsim = _MtFddiHsim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 5)
)
_MtFddiHsimF6_ObjectIdentity = ObjectIdentity
mtFddiHsimF6 = _MtFddiHsimF6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 7, 5, 1)
)
_MtWan_ObjectIdentity = ObjectIdentity
mtWan = _MtWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9)
)
_MtWanBrim_ObjectIdentity = ObjectIdentity
mtWanBrim = _MtWanBrim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 1)
)
_MtBrimWT1_ObjectIdentity = ObjectIdentity
mtBrimWT1 = _MtBrimWT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 1, 1)
)
_MtBrimW6_ObjectIdentity = ObjectIdentity
mtBrimW6 = _MtBrimW6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 1, 2)
)
_MtBrimWB4_ObjectIdentity = ObjectIdentity
mtBrimWB4 = _MtBrimWB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 1, 3)
)
_MtWanCyberSwitch_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch = _MtWanCyberSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2)
)
_MtWanCyberSwitch200_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch200 = _MtWanCyberSwitch200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 1)
)
_MtWanCyberSwitch300_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch300 = _MtWanCyberSwitch300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 2)
)
_MtWanCyberSwitch400_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch400 = _MtWanCyberSwitch400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 3)
)
_MtWanCyberSwitch150_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch150 = _MtWanCyberSwitch150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 4)
)
_MtWanCyberSwitch1200_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch1200 = _MtWanCyberSwitch1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 5)
)
_MtWanCyberSwitch6000_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch6000 = _MtWanCyberSwitch6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 6)
)
_MtWanCyberSwitch7000_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch7000 = _MtWanCyberSwitch7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 7)
)
_MtWanCyberSwitch5500_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch5500 = _MtWanCyberSwitch5500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 8)
)
_MtWanCyberSwitch9W000p00_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch9W000p00 = _MtWanCyberSwitch9W000p00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 9)
)
_MtWanCyberSwitch9W426p420_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch9W426p420 = _MtWanCyberSwitch9W426p420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 10)
)
_MtWanCyberSwitch9W427p420_ObjectIdentity = ObjectIdentity
mtWanCyberSwitch9W427p420 = _MtWanCyberSwitch9W427p420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 11)
)
_MtWanCyberSwitchNE1000_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchNE1000 = _MtWanCyberSwitchNE1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 12)
)
_MtWanCyberSwitchPOTS_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchPOTS = _MtWanCyberSwitchPOTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 13)
)
_MtWanCyberSwitchNTp1_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchNTp1 = _MtWanCyberSwitchNTp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 14)
)
_MtWanCyberSwitchBRI1_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchBRI1 = _MtWanCyberSwitchBRI1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 15)
)
_MtWanCyberSwitchBRI4_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchBRI4 = _MtWanCyberSwitchBRI4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 16)
)
_MtWanCyberSwitchPRI8_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchPRI8 = _MtWanCyberSwitchPRI8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 17)
)
_MtWanCyberSwitchPRI23_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchPRI23 = _MtWanCyberSwitchPRI23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 18)
)
_MtWanCyberSwitchEXP_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchEXP = _MtWanCyberSwitchEXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 19)
)
_MtWanCyberSwitchRS232_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchRS232 = _MtWanCyberSwitchRS232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 20)
)
_MtWanCyberSwitchV35_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchV35 = _MtWanCyberSwitchV35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 21)
)
_MtWanCyberSwitchDIG_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchDIG = _MtWanCyberSwitchDIG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 22)
)
_MtWanCyberSwitchDIG24_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchDIG24 = _MtWanCyberSwitchDIG24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 23)
)
_MtWanCyberSwitchDIG24Plus_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchDIG24Plus = _MtWanCyberSwitchDIG24Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 24)
)
_MtWanCyberSwitchDIG30Plus_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchDIG30Plus = _MtWanCyberSwitchDIG30Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 25)
)
_MtWanCyberSwitchAUI1_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchAUI1 = _MtWanCyberSwitchAUI1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 26)
)
_MtWanCyberSwitchAUI2_ObjectIdentity = ObjectIdentity
mtWanCyberSwitchAUI2 = _MtWanCyberSwitchAUI2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 2, 27)
)
_MtWanThirdParty_ObjectIdentity = ObjectIdentity
mtWanThirdParty = _MtWanThirdParty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 3)
)
_TpWanCyberSwitch100_ObjectIdentity = ObjectIdentity
tpWanCyberSwitch100 = _TpWanCyberSwitch100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 3, 1)
)
_MtWanHsim_ObjectIdentity = ObjectIdentity
mtWanHsim = _MtWanHsim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 4)
)
_MtWanHsimW6_ObjectIdentity = ObjectIdentity
mtWanHsimW6 = _MtWanHsimW6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 4, 1)
)
_MtWanHsimW84_ObjectIdentity = ObjectIdentity
mtWanHsimW84 = _MtWanHsimW84_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 4, 2)
)
_MtWanHsimW87_ObjectIdentity = ObjectIdentity
mtWanHsimW87 = _MtWanHsimW87_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 4, 3)
)
_MtWanHsimWB4_ObjectIdentity = ObjectIdentity
mtWanHsimWB4 = _MtWanHsimWB4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 4, 4)
)
_MtWanHsimSSA710_ObjectIdentity = ObjectIdentity
mtWanHsimSSA710 = _MtWanHsimSSA710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 4, 5)
)
_MtWanHsimSSA720_ObjectIdentity = ObjectIdentity
mtWanHsimSSA720 = _MtWanHsimSSA720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 4, 6)
)
_MtWanHsimWD1_ObjectIdentity = ObjectIdentity
mtWanHsimWD1 = _MtWanHsimWD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 4, 7)
)
_MtWanHsimW85_ObjectIdentity = ObjectIdentity
mtWanHsimW85 = _MtWanHsimW85_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 4, 8)
)
_MtWanHsimSSA710p48_ObjectIdentity = ObjectIdentity
mtWanHsimSSA710p48 = _MtWanHsimSSA710p48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 4, 9)
)
_MtWanHsimSSA720p60_ObjectIdentity = ObjectIdentity
mtWanHsimSSA720p60 = _MtWanHsimSSA720p60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 4, 10)
)
_MtWanCMM_ObjectIdentity = ObjectIdentity
mtWanCMM = _MtWanCMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 5)
)
_MtWanCMM824_ObjectIdentity = ObjectIdentity
mtWanCMM824 = _MtWanCMM824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 5, 1)
)
_MtWanCMM3248_ObjectIdentity = ObjectIdentity
mtWanCMM3248 = _MtWanCMM3248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 5, 2)
)
_MtWanCMM3264_ObjectIdentity = ObjectIdentity
mtWanCMM3264 = _MtWanCMM3264_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 5, 3)
)
_MtWanCMM3224_ObjectIdentity = ObjectIdentity
mtWanCMM3224 = _MtWanCMM3224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 5, 4)
)
_MtWanCMM3232_ObjectIdentity = ObjectIdentity
mtWanCMM3232 = _MtWanCMM3232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 5, 5)
)
_MtWanAccess_ObjectIdentity = ObjectIdentity
mtWanAccess = _MtWanAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 6)
)
_MtAS316_ObjectIdentity = ObjectIdentity
mtAS316 = _MtAS316_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 6, 1)
)
_MtSSA710p48_ObjectIdentity = ObjectIdentity
mtSSA710p48 = _MtSSA710p48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 6, 2)
)
_MtSSA720p60_ObjectIdentity = ObjectIdentity
mtSSA720p60 = _MtSSA720p60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 9, 6, 3)
)
_MtATM_ObjectIdentity = ObjectIdentity
mtATM = _MtATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11)
)
_MtAtmBrim_ObjectIdentity = ObjectIdentity
mtAtmBrim = _MtAtmBrim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 1)
)
_MtBrimA100_ObjectIdentity = ObjectIdentity
mtBrimA100 = _MtBrimA100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 1, 1)
)
_MtBrimA6_ObjectIdentity = ObjectIdentity
mtBrimA6 = _MtBrimA6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 1, 2)
)
_MtBrimA6DP_ObjectIdentity = ObjectIdentity
mtBrimA6DP = _MtBrimA6DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 1, 3)
)
_MtAtmHsim_ObjectIdentity = ObjectIdentity
mtAtmHsim = _MtAtmHsim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 2)
)
_MtAtmHsimA6DP_ObjectIdentity = ObjectIdentity
mtAtmHsimA6DP = _MtAtmHsimA6DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 2, 1)
)
_MtAtmVHsimA6DP_ObjectIdentity = ObjectIdentity
mtAtmVHsimA6DP = _MtAtmVHsimA6DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 2, 2)
)
_MtAtmStandAlone_ObjectIdentity = ObjectIdentity
mtAtmStandAlone = _MtAtmStandAlone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 3)
)
_Mt2A000_ObjectIdentity = ObjectIdentity
mt2A000 = _Mt2A000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 3, 1)
)
_Mt2A000R_ObjectIdentity = ObjectIdentity
mt2A000R = _Mt2A000R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 3, 2)
)
_MtAtmNetworkModule_ObjectIdentity = ObjectIdentity
mtAtmNetworkModule = _MtAtmNetworkModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 4)
)
_MtIOM21p04_ObjectIdentity = ObjectIdentity
mtIOM21p04 = _MtIOM21p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 4, 1)
)
_MtIOM22p04_ObjectIdentity = ObjectIdentity
mtIOM22p04 = _MtIOM22p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 4, 2)
)
_MtIOM29p04IR_ObjectIdentity = ObjectIdentity
mtIOM29p04IR = _MtIOM29p04IR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 4, 3)
)
_MtIOM29p04LR_ObjectIdentity = ObjectIdentity
mtIOM29p04LR = _MtIOM29p04LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 4, 4)
)
_MtIOM31p01_ObjectIdentity = ObjectIdentity
mtIOM31p01 = _MtIOM31p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 4, 5)
)
_MtIOM39p01_ObjectIdentity = ObjectIdentity
mtIOM39p01 = _MtIOM39p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 4, 6)
)
_MtIOM39p01LR_ObjectIdentity = ObjectIdentity
mtIOM39p01LR = _MtIOM39p01LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 4, 7)
)
_MtIOM67p04_ObjectIdentity = ObjectIdentity
mtIOM67p04 = _MtIOM67p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 4, 8)
)
_MtIOM77p04_ObjectIdentity = ObjectIdentity
mtIOM77p04 = _MtIOM77p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 11, 4, 9)
)
_MtFPS_ObjectIdentity = ObjectIdentity
mtFPS = _MtFPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12)
)
_MtFPSModules_ObjectIdentity = ObjectIdentity
mtFPSModules = _MtFPSModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 1)
)
_Mt7C03_ObjectIdentity = ObjectIdentity
mt7C03 = _Mt7C03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 1, 1)
)
_Mt7C04_ObjectIdentity = ObjectIdentity
mt7C04 = _Mt7C04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 1, 2)
)
_Mt7X00_ObjectIdentity = ObjectIdentity
mt7X00 = _Mt7X00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 1, 3)
)
_Mt7C04r_ObjectIdentity = ObjectIdentity
mt7C04r = _Mt7C04r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 1, 4)
)
_MtFpsEthernet_ObjectIdentity = ObjectIdentity
mtFpsEthernet = _MtFpsEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 2)
)
_Mt7E03p24_ObjectIdentity = ObjectIdentity
mt7E03p24 = _Mt7E03p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 2, 1)
)
_Mt7E02p12_ObjectIdentity = ObjectIdentity
mt7E02p12 = _Mt7E02p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 2, 2)
)
_Mt7E02p24_ObjectIdentity = ObjectIdentity
mt7E02p24 = _Mt7E02p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 2, 3)
)
_Mt7E08p12_ObjectIdentity = ObjectIdentity
mt7E08p12 = _Mt7E08p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 2, 4)
)
_MtFpsFDDI_ObjectIdentity = ObjectIdentity
mtFpsFDDI = _MtFpsFDDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 3)
)
_Mt7F06p02_ObjectIdentity = ObjectIdentity
mt7F06p02 = _Mt7F06p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 3, 1)
)
_MtFpsTR_ObjectIdentity = ObjectIdentity
mtFpsTR = _MtFpsTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 4)
)
_Mt7T05p04_ObjectIdentity = ObjectIdentity
mt7T05p04 = _Mt7T05p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 4, 1)
)
_MtFpsATM_ObjectIdentity = ObjectIdentity
mtFpsATM = _MtFpsATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 5)
)
_Mt7A06p01_ObjectIdentity = ObjectIdentity
mt7A06p01 = _Mt7A06p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 5, 1)
)
_MtFpsFastEthernet_ObjectIdentity = ObjectIdentity
mtFpsFastEthernet = _MtFpsFastEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 6)
)
_Mt7H02p06_ObjectIdentity = ObjectIdentity
mt7H02p06 = _Mt7H02p06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 6, 1)
)
_Mt7H02p12_ObjectIdentity = ObjectIdentity
mt7H02p12 = _Mt7H02p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 6, 2)
)
_Mt7H06p2_ObjectIdentity = ObjectIdentity
mt7H06p2 = _Mt7H06p2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 12, 6, 3)
)
_MtCableModem_ObjectIdentity = ObjectIdentity
mtCableModem = _MtCableModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 14)
)
_MtEthernetCableModem_ObjectIdentity = ObjectIdentity
mtEthernetCableModem = _MtEthernetCableModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 14, 1)
)
_MtMC23001pXE21_ObjectIdentity = ObjectIdentity
mtMC23001pXE21 = _MtMC23001pXE21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 14, 1, 1)
)
_MtMC21001pE01_ObjectIdentity = ObjectIdentity
mtMC21001pE01 = _MtMC21001pE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 14, 1, 2)
)
_MtWorkGroup_ObjectIdentity = ObjectIdentity
mtWorkGroup = _MtWorkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20)
)
_MtWorkGroupChassis_ObjectIdentity = ObjectIdentity
mtWorkGroupChassis = _MtWorkGroupChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 1)
)
_Mt6C105_ObjectIdentity = ObjectIdentity
mt6C105 = _Mt6C105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 1, 1)
)
_Mt6C110_ObjectIdentity = ObjectIdentity
mt6C110 = _Mt6C110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 1, 2)
)
_MtSmartSwitchRouter8_ObjectIdentity = ObjectIdentity
mtSmartSwitchRouter8 = _MtSmartSwitchRouter8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 1, 3)
)
_MtSmartSwitchRouter16_ObjectIdentity = ObjectIdentity
mtSmartSwitchRouter16 = _MtSmartSwitchRouter16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 1, 4)
)
_MtSmartSwitchRouter32_ObjectIdentity = ObjectIdentity
mtSmartSwitchRouter32 = _MtSmartSwitchRouter32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 1, 5)
)
_Mt6C107_ObjectIdentity = ObjectIdentity
mt6C107 = _Mt6C107_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 1, 6)
)
_MtWorkGroupEthernet_ObjectIdentity = ObjectIdentity
mtWorkGroupEthernet = _MtWorkGroupEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2)
)
_Mt6E102p24_ObjectIdentity = ObjectIdentity
mt6E102p24 = _Mt6E102p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 1)
)
_Mt6E122p26_ObjectIdentity = ObjectIdentity
mt6E122p26 = _Mt6E122p26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 2)
)
_Mt6E132p25_ObjectIdentity = ObjectIdentity
mt6E132p25 = _Mt6E132p25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 3)
)
_Mt6H122p08_ObjectIdentity = ObjectIdentity
mt6H122p08 = _Mt6H122p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 4)
)
_Mt6E123p50_ObjectIdentity = ObjectIdentity
mt6E123p50 = _Mt6E123p50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 5)
)
_Mt6E133p49_ObjectIdentity = ObjectIdentity
mt6E133p49 = _Mt6E133p49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 6)
)
_Mt6E123p26_ObjectIdentity = ObjectIdentity
mt6E123p26 = _Mt6E123p26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 7)
)
_Mt6E133p25_ObjectIdentity = ObjectIdentity
mt6E133p25 = _Mt6E133p25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 8)
)
_Mt6H133p49_ObjectIdentity = ObjectIdentity
mt6H133p49 = _Mt6H133p49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 9)
)
_Mt6H123p50_ObjectIdentity = ObjectIdentity
mt6H123p50 = _Mt6H123p50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 10)
)
_Mt6M146p04_ObjectIdentity = ObjectIdentity
mt6M146p04 = _Mt6M146p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 11)
)
_Mt6E128p26_ObjectIdentity = ObjectIdentity
mt6E128p26 = _Mt6E128p26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 12)
)
_Mt6E138p25_ObjectIdentity = ObjectIdentity
mt6E138p25 = _Mt6E138p25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 13)
)
_Mt6E129p26_ObjectIdentity = ObjectIdentity
mt6E129p26 = _Mt6E129p26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 14)
)
_Mt6E139p25_ObjectIdentity = ObjectIdentity
mt6E139p25 = _Mt6E139p25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 15)
)
_Mt6H128p08_ObjectIdentity = ObjectIdentity
mt6H128p08 = _Mt6H128p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 16)
)
_Mt6H129p08_ObjectIdentity = ObjectIdentity
mt6H129p08 = _Mt6H129p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 17)
)
_Mt6H122p16_ObjectIdentity = ObjectIdentity
mt6H122p16 = _Mt6H122p16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 18)
)
_Mt6H133p37_ObjectIdentity = ObjectIdentity
mt6H133p37 = _Mt6H133p37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 19)
)
_Mt6H202p24_ObjectIdentity = ObjectIdentity
mt6H202p24 = _Mt6H202p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 20)
)
_Mt6H252p17_ObjectIdentity = ObjectIdentity
mt6H252p17 = _Mt6H252p17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 21)
)
_Mt6M256p04_ObjectIdentity = ObjectIdentity
mt6M256p04 = _Mt6M256p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 22)
)
_Mt6E233p49_ObjectIdentity = ObjectIdentity
mt6E233p49 = _Mt6E233p49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 23)
)
_Mt6H258p17_ObjectIdentity = ObjectIdentity
mt6H258p17 = _Mt6H258p17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 24)
)
_Mt6H203p24_ObjectIdentity = ObjectIdentity
mt6H203p24 = _Mt6H203p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 25)
)
_Mt6H253p13_ObjectIdentity = ObjectIdentity
mt6H253p13 = _Mt6H253p13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 26)
)
_Mt6H259p17_ObjectIdentity = ObjectIdentity
mt6H259p17 = _Mt6H259p17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 27)
)
_Mt6H262p18_ObjectIdentity = ObjectIdentity
mt6H262p18 = _Mt6H262p18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 28)
)
_Mt6H202p48_ObjectIdentity = ObjectIdentity
mt6H202p48 = _Mt6H202p48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 29)
)
_Mt6E253p49_ObjectIdentity = ObjectIdentity
mt6E253p49 = _Mt6E253p49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 30)
)
_Mt6H203p48_ObjectIdentity = ObjectIdentity
mt6H203p48 = _Mt6H203p48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 31)
)
_Mt6H303p48_ObjectIdentity = ObjectIdentity
mt6H303p48 = _Mt6H303p48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 32)
)
_Mt6H302p48_ObjectIdentity = ObjectIdentity
mt6H302p48 = _Mt6H302p48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 33)
)
_Mt6H352p25_ObjectIdentity = ObjectIdentity
mt6H352p25 = _Mt6H352p25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 34)
)
_Mt6G306p06_ObjectIdentity = ObjectIdentity
mt6G306p06 = _Mt6G306p06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 2, 35)
)
_MtWorkGroupATM_ObjectIdentity = ObjectIdentity
mtWorkGroupATM = _MtWorkGroupATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 3)
)
_Mt6A000_ObjectIdentity = ObjectIdentity
mt6A000 = _Mt6A000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 3, 1)
)
_Mt6A000F_ObjectIdentity = ObjectIdentity
mt6A000F = _Mt6A000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 20, 3, 2)
)
_MtMMACPlus_ObjectIdentity = ObjectIdentity
mtMMACPlus = _MtMMACPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32)
)
_MtMMACPlusEnclose_ObjectIdentity = ObjectIdentity
mtMMACPlusEnclose = _MtMMACPlusEnclose_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 1)
)
_Mt9C114_ObjectIdentity = ObjectIdentity
mt9C114 = _Mt9C114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 1, 1)
)
_Mt9C106_ObjectIdentity = ObjectIdentity
mt9C106 = _Mt9C106_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 1, 2)
)
_MtMMACEM_ObjectIdentity = ObjectIdentity
mtMMACEM = _MtMMACEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 3)
)
_Mt9C300p01_ObjectIdentity = ObjectIdentity
mt9C300p01 = _Mt9C300p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 3, 1)
)
_Mt9C306p01_ObjectIdentity = ObjectIdentity
mt9C306p01 = _Mt9C306p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 3, 2)
)
_MtMMACPU_ObjectIdentity = ObjectIdentity
mtMMACPU = _MtMMACPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 4)
)
_Mt9C214p1_ObjectIdentity = ObjectIdentity
mt9C214p1 = _Mt9C214p1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 4, 1)
)
_Mt9C214p2_ObjectIdentity = ObjectIdentity
mt9C214p2 = _Mt9C214p2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 4, 2)
)
_Mt9C206p1_ObjectIdentity = ObjectIdentity
mt9C206p1 = _Mt9C206p1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 4, 3)
)
_Mt9C214p3_ObjectIdentity = ObjectIdentity
mt9C214p3 = _Mt9C214p3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 4, 4)
)
_MtMMACPlusFNBSingle_ObjectIdentity = ObjectIdentity
mtMMACPlusFNBSingle = _MtMMACPlusFNBSingle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5)
)
_Mt9E133p36_ObjectIdentity = ObjectIdentity
mt9E133p36 = _Mt9E133p36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 1)
)
_Mt9E122p24_ObjectIdentity = ObjectIdentity
mt9E122p24 = _Mt9E122p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 2)
)
_Mt9E138p36_ObjectIdentity = ObjectIdentity
mt9E138p36 = _Mt9E138p36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 3)
)
_Mt9F116p01_ObjectIdentity = ObjectIdentity
mt9F116p01 = _Mt9F116p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 4)
)
_Mt9F106p02_ObjectIdentity = ObjectIdentity
mt9F106p02 = _Mt9F106p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 5)
)
_Mt9W116p04_ObjectIdentity = ObjectIdentity
mt9W116p04 = _Mt9W116p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 6)
)
_Mt9T122p24_ObjectIdentity = ObjectIdentity
mt9T122p24 = _Mt9T122p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 7)
)
_Mt9E132p15_ObjectIdentity = ObjectIdentity
mt9E132p15 = _Mt9E132p15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 8)
)
_Mt9T122p08_ObjectIdentity = ObjectIdentity
mt9T122p08 = _Mt9T122p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 9)
)
_Mt9A128p01_ObjectIdentity = ObjectIdentity
mt9A128p01 = _Mt9A128p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 10)
)
_Mt9E106p06_ObjectIdentity = ObjectIdentity
mt9E106p06 = _Mt9E106p06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 11)
)
_Mt9E138p12_ObjectIdentity = ObjectIdentity
mt9E138p12 = _Mt9E138p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 12)
)
_Mt9F206p02_ObjectIdentity = ObjectIdentity
mt9F206p02 = _Mt9F206p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 13)
)
_Mt9A126p01_ObjectIdentity = ObjectIdentity
mt9A126p01 = _Mt9A126p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 14)
)
_Mt9T112p24_ObjectIdentity = ObjectIdentity
mt9T112p24 = _Mt9T112p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 15)
)
_Mt9T162p06_ObjectIdentity = ObjectIdentity
mt9T162p06 = _Mt9T162p06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 16)
)
_Mt9T125p08_ObjectIdentity = ObjectIdentity
mt9T125p08 = _Mt9T125p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 17)
)
_Mt9T125p24_ObjectIdentity = ObjectIdentity
mt9T125p24 = _Mt9T125p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 18)
)
_Mt9E132p15s_ObjectIdentity = ObjectIdentity
mt9E132p15s = _Mt9E132p15s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 19)
)
_Mt9E133p36s_ObjectIdentity = ObjectIdentity
mt9E133p36s = _Mt9E133p36s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 20)
)
_Mt9E138p36s_ObjectIdentity = ObjectIdentity
mt9E138p36s = _Mt9E138p36s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 21)
)
_Mt9E138p12s_ObjectIdentity = ObjectIdentity
mt9E138p12s = _Mt9E138p12s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 5, 22)
)
_MtMMACPlusFNBDual_ObjectIdentity = ObjectIdentity
mtMMACPlusFNBDual = _MtMMACPlusFNBDual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 6)
)
_Mt9F122p12_ObjectIdentity = ObjectIdentity
mt9F122p12 = _Mt9F122p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 6, 1)
)
_Mt9F120p08_ObjectIdentity = ObjectIdentity
mt9F120p08 = _Mt9F120p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 6, 2)
)
_Mt9F125p08_ObjectIdentity = ObjectIdentity
mt9F125p08 = _Mt9F125p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 6, 3)
)
_Mt9F241P12_ObjectIdentity = ObjectIdentity
mt9F241P12 = _Mt9F241P12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 6, 4)
)
_Mt9F240p08_ObjectIdentity = ObjectIdentity
mt9F240p08 = _Mt9F240p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 6, 5)
)
_MtMMACPlusINBSingle_ObjectIdentity = ObjectIdentity
mtMMACPlusINBSingle = _MtMMACPlusINBSingle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9)
)
_Mt9E312p12_ObjectIdentity = ObjectIdentity
mt9E312p12 = _Mt9E312p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 1)
)
_Mt9E313p12_ObjectIdentity = ObjectIdentity
mt9E313p12 = _Mt9E313p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 2)
)
_Mt9E318p12_ObjectIdentity = ObjectIdentity
mt9E318p12 = _Mt9E318p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 3)
)
_Mt9F310p02_ObjectIdentity = ObjectIdentity
mt9F310p02 = _Mt9F310p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 4)
)
_Mt9A426p02_ObjectIdentity = ObjectIdentity
mt9A426p02 = _Mt9A426p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 5)
)
_Mt9F315p02_ObjectIdentity = ObjectIdentity
mt9F315p02 = _Mt9F315p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 6)
)
_Mt9F426p2_ObjectIdentity = ObjectIdentity
mt9F426p2 = _Mt9F426p2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 7)
)
_Mt9E423p24_ObjectIdentity = ObjectIdentity
mt9E423p24 = _Mt9E423p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 8)
)
_Mt9H422p12_ObjectIdentity = ObjectIdentity
mt9H422p12 = _Mt9H422p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 9)
)
_Mt9E428p12_ObjectIdentity = ObjectIdentity
mt9E428p12 = _Mt9E428p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 10)
)
_Mt9E428p36_ObjectIdentity = ObjectIdentity
mt9E428p36 = _Mt9E428p36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 11)
)
_Mt9E429p12_ObjectIdentity = ObjectIdentity
mt9E429p12 = _Mt9E429p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 12)
)
_Mt9E429p36_ObjectIdentity = ObjectIdentity
mt9E429p36 = _Mt9E429p36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 13)
)
_Mt9F426p03_ObjectIdentity = ObjectIdentity
mt9F426p03 = _Mt9F426p03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 14)
)
_Mt9H421p12_ObjectIdentity = ObjectIdentity
mt9H421p12 = _Mt9H421p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 15)
)
_Mt9E423p36_ObjectIdentity = ObjectIdentity
mt9E423p36 = _Mt9E423p36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 16)
)
_Mt9H429p12_ObjectIdentity = ObjectIdentity
mt9H429p12 = _Mt9H429p12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 17)
)
_Mt9T425p16_ObjectIdentity = ObjectIdentity
mt9T425p16 = _Mt9T425p16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 18)
)
_Mt9T425p24_ObjectIdentity = ObjectIdentity
mt9T425p24 = _Mt9T425p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 19)
)
_Mt9A426p01_ObjectIdentity = ObjectIdentity
mt9A426p01 = _Mt9A426p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 20)
)
_Mt9G426p02_ObjectIdentity = ObjectIdentity
mt9G426p02 = _Mt9G426p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 21)
)
_Mt9H423p28_ObjectIdentity = ObjectIdentity
mt9H423p28 = _Mt9H423p28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 22)
)
_Mt9H423p26_ObjectIdentity = ObjectIdentity
mt9H423p26 = _Mt9H423p26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 23)
)
_Mt9G421p02_ObjectIdentity = ObjectIdentity
mt9G421p02 = _Mt9G421p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 24)
)
_Mt9M426p02_ObjectIdentity = ObjectIdentity
mt9M426p02 = _Mt9M426p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 25)
)
_Mt9D422p16_ObjectIdentity = ObjectIdentity
mt9D422p16 = _Mt9D422p16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 26)
)
_Mt9G429p02_ObjectIdentity = ObjectIdentity
mt9G429p02 = _Mt9G429p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 27)
)
_Mt9T428p16_ObjectIdentity = ObjectIdentity
mt9T428p16 = _Mt9T428p16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 28)
)
_Mt9T427p16_ObjectIdentity = ObjectIdentity
mt9T427p16 = _Mt9T427p16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 9, 29)
)
_Mt3PartyFnbSingle_ObjectIdentity = ObjectIdentity
mt3PartyFnbSingle = _Mt3PartyFnbSingle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 10)
)
_Mt9W111p08_ObjectIdentity = ObjectIdentity
mt9W111p08 = _Mt9W111p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 10, 1)
)
_Mt9T101p04_ObjectIdentity = ObjectIdentity
mt9T101p04 = _Mt9T101p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 10, 2)
)
_Mt9F106p01_ObjectIdentity = ObjectIdentity
mt9F106p01 = _Mt9F106p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 10, 3)
)
_Mt9F206p01_ObjectIdentity = ObjectIdentity
mt9F206p01 = _Mt9F206p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 10, 4)
)
_Mt9T201p04_ObjectIdentity = ObjectIdentity
mt9T201p04 = _Mt9T201p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 10, 5)
)
_Mt9W211p08_ObjectIdentity = ObjectIdentity
mt9W211p08 = _Mt9W211p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 10, 6)
)
_Mt9A221p01_ObjectIdentity = ObjectIdentity
mt9A221p01 = _Mt9A221p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 10, 7)
)
_Mt9A222p01_ObjectIdentity = ObjectIdentity
mt9A222p01 = _Mt9A222p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 10, 14)
)
_Mt9A229p01_ObjectIdentity = ObjectIdentity
mt9A229p01 = _Mt9A229p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 10, 15)
)
_MtMMACPOther_ObjectIdentity = ObjectIdentity
mtMMACPOther = _MtMMACPOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 11)
)
_Mt9A000_ObjectIdentity = ObjectIdentity
mt9A000 = _Mt9A000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 11, 1)
)
_Mt9P120_ObjectIdentity = ObjectIdentity
mt9P120 = _Mt9P120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 11, 2)
)
_Mt9P110_ObjectIdentity = ObjectIdentity
mt9P110 = _Mt9P110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 11, 3)
)
_Mt9X000p16_ObjectIdentity = ObjectIdentity
mt9X000p16 = _Mt9X000p16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 11, 4)
)
_Mt9P110mhz90_ObjectIdentity = ObjectIdentity
mt9P110mhz90 = _Mt9P110mhz90_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 11, 5)
)
_Mt9A656p04_ObjectIdentity = ObjectIdentity
mt9A656p04 = _Mt9A656p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 11, 6)
)
_Mt9A600p04_ObjectIdentity = ObjectIdentity
mt9A600p04 = _Mt9A600p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 11, 7)
)
_Mt9A686p04_ObjectIdentity = ObjectIdentity
mt9A686p04 = _Mt9A686p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 11, 8)
)
_Mt9A100_ObjectIdentity = ObjectIdentity
mt9A100 = _Mt9A100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 11, 9)
)
_MtMMACPlusNortel_ObjectIdentity = ObjectIdentity
mtMMACPlusNortel = _MtMMACPlusNortel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 12)
)
_Mt9N050_ObjectIdentity = ObjectIdentity
mt9N050 = _Mt9N050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 12, 1)
)
_MtMMACPlusINBDual_ObjectIdentity = ObjectIdentity
mtMMACPlusINBDual = _MtMMACPlusINBDual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13)
)
_Mt9H532p18_ObjectIdentity = ObjectIdentity
mt9H532p18 = _Mt9H532p18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 1)
)
_Mt9H531p18_ObjectIdentity = ObjectIdentity
mt9H531p18 = _Mt9H531p18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 2)
)
_Mt9H539p18_ObjectIdentity = ObjectIdentity
mt9H539p18 = _Mt9H539p18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 3)
)
_Mt9H532p17_ObjectIdentity = ObjectIdentity
mt9H532p17 = _Mt9H532p17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 4)
)
_Mt9H531p17_ObjectIdentity = ObjectIdentity
mt9H531p17 = _Mt9H531p17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 5)
)
_Mt9H539p17_ObjectIdentity = ObjectIdentity
mt9H539p17 = _Mt9H539p17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 6)
)
_Mt9G536p04_ObjectIdentity = ObjectIdentity
mt9G536p04 = _Mt9G536p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 7)
)
_Mt9H532p24_ObjectIdentity = ObjectIdentity
mt9H532p24 = _Mt9H532p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 8)
)
_Mt9H531p24_ObjectIdentity = ObjectIdentity
mt9H531p24 = _Mt9H531p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 9)
)
_Mt9H539p24_ObjectIdentity = ObjectIdentity
mt9H539p24 = _Mt9H539p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 10)
)
_Mt9M546p04_ObjectIdentity = ObjectIdentity
mt9M546p04 = _Mt9M546p04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 11)
)
_Mt9H533p24_ObjectIdentity = ObjectIdentity
mt9H533p24 = _Mt9H533p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 12)
)
_Mt9H533p48_ObjectIdentity = ObjectIdentity
mt9H533p48 = _Mt9H533p48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 13)
)
_Mt9E531p24_ObjectIdentity = ObjectIdentity
mt9E531p24 = _Mt9E531p24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 32, 13, 14)
)
_MtSSR_ObjectIdentity = ObjectIdentity
mtSSR = _MtSSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33)
)
_MtSSRStandAlone_ObjectIdentity = ObjectIdentity
mtSSRStandAlone = _MtSSRStandAlone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 1)
)
_MtSSR2B_ObjectIdentity = ObjectIdentity
mtSSR2B = _MtSSR2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 1, 1)
)
_MtSSR2BPS_ObjectIdentity = ObjectIdentity
mtSSR2BPS = _MtSSR2BPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 1, 2)
)
_MtSSR2100_ObjectIdentity = ObjectIdentity
mtSSR2100 = _MtSSR2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 1, 3)
)
_MtSSR510_ObjectIdentity = ObjectIdentity
mtSSR510 = _MtSSR510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 1, 4)
)
_MtSSR520_ObjectIdentity = ObjectIdentity
mtSSR520 = _MtSSR520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 1, 5)
)
_MtSSR600S_ObjectIdentity = ObjectIdentity
mtSSR600S = _MtSSR600S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 1, 6)
)
_MtSSR600D_ObjectIdentity = ObjectIdentity
mtSSR600D = _MtSSR600D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 1, 7)
)
_MtSSR710T1_ObjectIdentity = ObjectIdentity
mtSSR710T1 = _MtSSR710T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 1, 8)
)
_MtSSR710E1_ObjectIdentity = ObjectIdentity
mtSSR710E1 = _MtSSR710E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 1, 9)
)
_MtSSR720_ObjectIdentity = ObjectIdentity
mtSSR720 = _MtSSR720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 1, 10)
)
_MtSSR2Expansion_ObjectIdentity = ObjectIdentity
mtSSR2Expansion = _MtSSR2Expansion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 2)
)
_MtSSR2SX_ObjectIdentity = ObjectIdentity
mtSSR2SX = _MtSSR2SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 2, 1)
)
_MtSSR2LX_ObjectIdentity = ObjectIdentity
mtSSR2LX = _MtSSR2LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 2, 2)
)
_MtSSR2TX_ObjectIdentity = ObjectIdentity
mtSSR2TX = _MtSSR2TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 2, 3)
)
_MtSSR2FX_ObjectIdentity = ObjectIdentity
mtSSR2FX = _MtSSR2FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 2, 4)
)
_MtSSR2SER_ObjectIdentity = ObjectIdentity
mtSSR2SER = _MtSSR2SER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 2, 5)
)
_MtSSR2SERC_ObjectIdentity = ObjectIdentity
mtSSR2SERC = _MtSSR2SERC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 2, 6)
)
_MtSSR2SERCE_ObjectIdentity = ObjectIdentity
mtSSR2SERCE = _MtSSR2SERCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 2, 7)
)
_MtIA1100_ObjectIdentity = ObjectIdentity
mtIA1100 = _MtIA1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 2, 8)
)
_MtIA1200_ObjectIdentity = ObjectIdentity
mtIA1200 = _MtIA1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 2, 9)
)
_MtSSR8Expansion_ObjectIdentity = ObjectIdentity
mtSSR8Expansion = _MtSSR8Expansion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3)
)
_MtSSRHTX12p08_ObjectIdentity = ObjectIdentity
mtSSRHTX12p08 = _MtSSRHTX12p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 1)
)
_MtSSRHTX22p08_ObjectIdentity = ObjectIdentity
mtSSRHTX22p08 = _MtSSRHTX22p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 2)
)
_MtSSRHFX11p08_ObjectIdentity = ObjectIdentity
mtSSRHFX11p08 = _MtSSRHFX11p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 3)
)
_MtSSRHFX21p08_ObjectIdentity = ObjectIdentity
mtSSRHFX21p08 = _MtSSRHFX21p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 4)
)
_MtSSRGSX11p02_ObjectIdentity = ObjectIdentity
mtSSRGSX11p02 = _MtSSRGSX11p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 5)
)
_MtSSRGSX21p02_ObjectIdentity = ObjectIdentity
mtSSRGSX21p02 = _MtSSRGSX21p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 6)
)
_MtSSRGLX19p02_ObjectIdentity = ObjectIdentity
mtSSRGLX19p02 = _MtSSRGLX19p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 7)
)
_MtSSRGLX29p02_ObjectIdentity = ObjectIdentity
mtSSRGLX29p02 = _MtSSRGLX29p02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 8)
)
_MtSSRGLX70p01_ObjectIdentity = ObjectIdentity
mtSSRGLX70p01 = _MtSSRGLX70p01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 9)
)
_MtSSRHFX29p08_ObjectIdentity = ObjectIdentity
mtSSRHFX29p08 = _MtSSRHFX29p08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 10)
)
_MtSSRSERCp04_ObjectIdentity = ObjectIdentity
mtSSRSERCp04 = _MtSSRSERCp04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 11)
)
_MtSSRSERCEp04_ObjectIdentity = ObjectIdentity
mtSSRSERCEp04 = _MtSSRSERCEp04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 12)
)
_MtSSRHSSIp02_ObjectIdentity = ObjectIdentity
mtSSRHSSIp02 = _MtSSRHSSIp02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 3, 13)
)
_MtSSR6Expansion_ObjectIdentity = ObjectIdentity
mtSSR6Expansion = _MtSSR6Expansion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 4)
)
_Mt6SSRM_02_ObjectIdentity = ObjectIdentity
mt6SSRM_02 = _Mt6SSRM_02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 4, 1)
)
_Mt6SSRLC_LX_ObjectIdentity = ObjectIdentity
mt6SSRLC_LX = _Mt6SSRLC_LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 4, 2)
)
_Mt6SSRLC_TX_ObjectIdentity = ObjectIdentity
mt6SSRLC_TX = _Mt6SSRLC_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 4, 3)
)
_Mt6SSRLC_FX_ObjectIdentity = ObjectIdentity
mt6SSRLC_FX = _Mt6SSRLC_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 4, 4)
)
_Mt6SSRLC_SX_ObjectIdentity = ObjectIdentity
mt6SSRLC_SX = _Mt6SSRLC_SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 4, 5)
)
_Mt6SSRLC_SER_ObjectIdentity = ObjectIdentity
mt6SSRLC_SER = _Mt6SSRLC_SER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 4, 6)
)
_Mt6SSRLC_SERC_ObjectIdentity = ObjectIdentity
mt6SSRLC_SERC = _Mt6SSRLC_SERC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 4, 7)
)
_Mt6SSRLC_SERCE_ObjectIdentity = ObjectIdentity
mt6SSRLC_SERCE = _Mt6SSRLC_SERCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 4, 8)
)
_Mt6SSRLC_LX70_ObjectIdentity = ObjectIdentity
mt6SSRLC_LX70 = _Mt6SSRLC_LX70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 4, 9)
)
_MtHSIMSSR_ObjectIdentity = ObjectIdentity
mtHSIMSSR = _MtHSIMSSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 5)
)
_MtHSIMSSR600_ObjectIdentity = ObjectIdentity
mtHSIMSSR600 = _MtHSIMSSR600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 9, 33, 5, 1)
)
_CtIfTypes_ObjectIdentity = ObjectIdentity
ctIfTypes = _CtIfTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 10)
)
_CtIfBackPlane_ObjectIdentity = ObjectIdentity
ctIfBackPlane = _CtIfBackPlane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 10, 1)
)
_CtIfNonFNB_ObjectIdentity = ObjectIdentity
ctIfNonFNB = _CtIfNonFNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 10, 1, 1)
)
_CtIfFNB_ObjectIdentity = ObjectIdentity
ctIfFNB = _CtIfFNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 10, 1, 2)
)
_CtIfFrontPanel_ObjectIdentity = ObjectIdentity
ctIfFrontPanel = _CtIfFrontPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 10, 2)
)
_CtHsimInterconnect_ObjectIdentity = ObjectIdentity
ctHsimInterconnect = _CtHsimInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 10, 3)
)
_CtResourceType_ObjectIdentity = ObjectIdentity
ctResourceType = _CtResourceType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11)
)
_CtFDDIFnbBP_ObjectIdentity = ObjectIdentity
ctFDDIFnbBP = _CtFDDIFnbBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 1)
)
_CtFDDIFnbBP1_ObjectIdentity = ObjectIdentity
ctFDDIFnbBP1 = _CtFDDIFnbBP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 1, 1)
)
_CtFDDIFnbBP2_ObjectIdentity = ObjectIdentity
ctFDDIFnbBP2 = _CtFDDIFnbBP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 1, 2)
)
_CtSMB1_ObjectIdentity = ObjectIdentity
ctSMB1 = _CtSMB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 2)
)
_CtSMB10_ObjectIdentity = ObjectIdentity
ctSMB10 = _CtSMB10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 3)
)
_CtFrontPanel_ObjectIdentity = ObjectIdentity
ctFrontPanel = _CtFrontPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5)
)
_CtFDDIFrontPanel_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel = _CtFDDIFrontPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1)
)
_CtFDDIFrontPanel1_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel1 = _CtFDDIFrontPanel1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 1)
)
_CtFDDIFrontPanel2_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel2 = _CtFDDIFrontPanel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 2)
)
_CtFDDIFrontPanel3_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel3 = _CtFDDIFrontPanel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 3)
)
_CtFDDIFrontPanel4_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel4 = _CtFDDIFrontPanel4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 4)
)
_CtFDDIFrontPanel5_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel5 = _CtFDDIFrontPanel5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 5)
)
_CtFDDIFrontPanel6_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel6 = _CtFDDIFrontPanel6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 6)
)
_CtFDDIFrontPanel7_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel7 = _CtFDDIFrontPanel7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 7)
)
_CtFDDIFrontPanel8_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel8 = _CtFDDIFrontPanel8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 8)
)
_CtFDDIFrontPanel9_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel9 = _CtFDDIFrontPanel9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 9)
)
_CtFDDIFrontPanel10_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel10 = _CtFDDIFrontPanel10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 10)
)
_CtFDDIFrontPanel11_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel11 = _CtFDDIFrontPanel11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 11)
)
_CtFDDIFrontPanel12_ObjectIdentity = ObjectIdentity
ctFDDIFrontPanel12 = _CtFDDIFrontPanel12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 1, 12)
)
_CtEthernetFrontPanel_ObjectIdentity = ObjectIdentity
ctEthernetFrontPanel = _CtEthernetFrontPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 2)
)
_CtFrontPanelATM_ObjectIdentity = ObjectIdentity
ctFrontPanelATM = _CtFrontPanelATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 3)
)
_CtFrontPanelATM1_ObjectIdentity = ObjectIdentity
ctFrontPanelATM1 = _CtFrontPanelATM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 3, 1)
)
_CtFrontPanelATM2_ObjectIdentity = ObjectIdentity
ctFrontPanelATM2 = _CtFrontPanelATM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 3, 2)
)
_CtFrontPanelTokenRing_ObjectIdentity = ObjectIdentity
ctFrontPanelTokenRing = _CtFrontPanelTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 4)
)
_CtFrontPanelWAN_ObjectIdentity = ObjectIdentity
ctFrontPanelWAN = _CtFrontPanelWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 5)
)
_CtFrontPanelComport_ObjectIdentity = ObjectIdentity
ctFrontPanelComport = _CtFrontPanelComport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 6)
)
_CtFrontPanelComport1_ObjectIdentity = ObjectIdentity
ctFrontPanelComport1 = _CtFrontPanelComport1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 6, 1)
)
_CtFrontPanelComport2_ObjectIdentity = ObjectIdentity
ctFrontPanelComport2 = _CtFrontPanelComport2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 5, 6, 2)
)
_CtINB1_ObjectIdentity = ObjectIdentity
ctINB1 = _CtINB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 6)
)
_CtINB2_ObjectIdentity = ObjectIdentity
ctINB2 = _CtINB2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 7)
)
_CtHostPort_ObjectIdentity = ObjectIdentity
ctHostPort = _CtHostPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 8)
)
_CtCTM_ObjectIdentity = ObjectIdentity
ctCTM = _CtCTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 9)
)
_CtWorkGroupBPport_ObjectIdentity = ObjectIdentity
ctWorkGroupBPport = _CtWorkGroupBPport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 10)
)
_CtWorkGroupBPport1_ObjectIdentity = ObjectIdentity
ctWorkGroupBPport1 = _CtWorkGroupBPport1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 10, 1)
)
_CtWorkGroupBPport2_ObjectIdentity = ObjectIdentity
ctWorkGroupBPport2 = _CtWorkGroupBPport2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 10, 2)
)
_CtWorkGroupBPport3_ObjectIdentity = ObjectIdentity
ctWorkGroupBPport3 = _CtWorkGroupBPport3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 10, 3)
)
_CtWorkGroupBPport4_ObjectIdentity = ObjectIdentity
ctWorkGroupBPport4 = _CtWorkGroupBPport4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 10, 4)
)
_CtWorkGroupBPport5_ObjectIdentity = ObjectIdentity
ctWorkGroupBPport5 = _CtWorkGroupBPport5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 10, 5)
)
_CtATMVirtual_ObjectIdentity = ObjectIdentity
ctATMVirtual = _CtATMVirtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 11)
)
_CtATMVirtualLec_ObjectIdentity = ObjectIdentity
ctATMVirtualLec = _CtATMVirtualLec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 11, 1)
)
_CtATMVirtualPvc_ObjectIdentity = ObjectIdentity
ctATMVirtualPvc = _CtATMVirtualPvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 11, 2)
)
_CtATMVirtualClip_ObjectIdentity = ObjectIdentity
ctATMVirtualClip = _CtATMVirtualClip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 11, 3)
)
_CtATMVirtualSvc_ObjectIdentity = ObjectIdentity
ctATMVirtualSvc = _CtATMVirtualSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 11, 4)
)
_CtIfSpecific_ObjectIdentity = ObjectIdentity
ctIfSpecific = _CtIfSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 12)
)
_CtSmartTrunkVirtual_ObjectIdentity = ObjectIdentity
ctSmartTrunkVirtual = _CtSmartTrunkVirtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 13)
)
_CtMMACPlusBPport_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport = _CtMMACPlusBPport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14)
)
_CtMMACPlusBPport1_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport1 = _CtMMACPlusBPport1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 1)
)
_CtMMACPlusBPport2_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport2 = _CtMMACPlusBPport2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 2)
)
_CtMMACPlusBPport3_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport3 = _CtMMACPlusBPport3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 3)
)
_CtMMACPlusBPport4_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport4 = _CtMMACPlusBPport4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 4)
)
_CtMMACPlusBPport5_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport5 = _CtMMACPlusBPport5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 5)
)
_CtMMACPlusBPport6_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport6 = _CtMMACPlusBPport6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 6)
)
_CtMMACPlusBPport7_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport7 = _CtMMACPlusBPport7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 7)
)
_CtMMACPlusBPport8_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport8 = _CtMMACPlusBPport8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 8)
)
_CtMMACPlusBPport9_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport9 = _CtMMACPlusBPport9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 9)
)
_CtMMACPlusBPport10_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport10 = _CtMMACPlusBPport10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 10)
)
_CtMMACPlusBPport11_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport11 = _CtMMACPlusBPport11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 11)
)
_CtMMACPlusBPport12_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport12 = _CtMMACPlusBPport12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 12)
)
_CtMMACPlusBPport13_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport13 = _CtMMACPlusBPport13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 13)
)
_CtMMACPlusBPport14_ObjectIdentity = ObjectIdentity
ctMMACPlusBPport14 = _CtMMACPlusBPport14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 11, 14, 14)
)
_CtSFPSTypes_ObjectIdentity = ObjectIdentity
ctSFPSTypes = _CtSFPSTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 12)
)
_CtVLANS_ObjectIdentity = ObjectIdentity
ctVLANS = _CtVLANS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 13)
)
_CtLaneServices_ObjectIdentity = ObjectIdentity
ctLaneServices = _CtLaneServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 14)
)
_LsSFpSMARTLANE_ObjectIdentity = ObjectIdentity
lsSFpSMARTLANE = _LsSFpSMARTLANE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 3, 14, 1)
)
_V2conformance_ObjectIdentity = ObjectIdentity
v2conformance = _V2conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 5)
)
_TrapDefinitions_ObjectIdentity = ObjectIdentity
trapDefinitions = _TrapDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 6)
)
_CtTrapsV1_ObjectIdentity = ObjectIdentity
ctTrapsV1 = _CtTrapsV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 6, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-OIDS",
    **{"cabletron": cabletron,
       "namingTree": namingTree,
       "chassisType": chassisType,
       "ctUnknown": ctUnknown,
       "ctMMAC8": ctMMAC8,
       "ctMMAC5": ctMMAC5,
       "ctMMAC3": ctMMAC3,
       "ctMINIMMAC": ctMINIMMAC,
       "ctMRXI": ctMRXI,
       "ctM3FNBShunt": ctM3FNBShunt,
       "ctM5FNBShunt": ctM5FNBShunt,
       "ctM8FNB": ctM8FNB,
       "ctNonFNB": ctNonFNB,
       "ctMMAC3FNBShunt": ctMMAC3FNBShunt,
       "ctMMAC5FNBShunt": ctMMAC5FNBShunt,
       "ctMMAC8FNBShunt": ctMMAC8FNBShunt,
       "ctM8FNBShunt": ctM8FNBShunt,
       "ctTRXI": ctTRXI,
       "ctStandAlone": ctStandAlone,
       "ctMMACPlus14": ctMMACPlus14,
       "ctMMACPlus6": ctMMACPlus6,
       "ctWanCyberSwitchNE2000": ctWanCyberSwitchNE2000,
       "ctWanCyberSwitchNe4000": ctWanCyberSwitchNe4000,
       "ctWanCyberSwitchNE5000": ctWanCyberSwitchNE5000,
       "moduleType": moduleType,
       "mtThinMim1": mtThinMim1,
       "mtFDMMIM24": mtFDMMIM24,
       "mtFDMMIM14to46": mtFDMMIM14to46,
       "mtFDMMIM04To44": mtFDMMIM04To44,
       "mtFDMMIM00": mtFDMMIM00,
       "mtFDMMIM30": mtFDMMIM30,
       "mtFDCMIM28": mtFDCMIM28,
       "mtFDCMIM18": mtFDCMIM18,
       "mtFDCMIM08": mtFDCMIM08,
       "mtFDCMIM04": mtFDCMIM04,
       "mtFDCMIM24": mtFDCMIM24,
       "mtFDCMIM14": mtFDCMIM14,
       "mtFDCMIM38": mtFDCMIM38,
       "mtFDCMIM34": mtFDCMIM34,
       "mtTRMIM12": mtTRMIM12,
       "mtTRMIM10R": mtTRMIM10R,
       "mtTRMIM22": mtTRMIM22,
       "mtTRMIM20R": mtTRMIM20R,
       "mtTRMIM62A": mtTRMIM62A,
       "mtTRMIM24ToA": mtTRMIM24ToA,
       "mtTRMIM22ToA": mtTRMIM22ToA,
       "mtTRFMIM28": mtTRFMIM28,
       "mtTRFMIM22": mtTRFMIM22,
       "mtTRRMIMA": mtTRRMIMA,
       "mtTRFMIM26": mtTRFMIM26,
       "mtTRMIM34A": mtTRMIM34A,
       "mtTRMIM32A": mtTRMIM32A,
       "mtTRMIM44ToA": mtTRMIM44ToA,
       "mtTRMIM42ToA": mtTRMIM42ToA,
       "mtTPMIMT1": mtTPMIMT1,
       "mtTPMIMT": mtTPMIMT,
       "mtTPMIMT3": mtTPMIMT3,
       "mtThinMim2": mtThinMim2,
       "mtTPMIM24": mtTPMIM24,
       "mtTPMIM22": mtTPMIM22,
       "mtTPMIM34": mtTPMIM34,
       "mtTPMIM32": mtTPMIM32,
       "mtTPRMIM100I": mtTPRMIM100I,
       "mtTPRMIM33": mtTPRMIM33,
       "mtTPRMIM36": mtTPRMIM36,
       "mtCXRMIM": mtCXRMIM,
       "mtFORMIM22": mtFORMIM22,
       "mtTPRMIM20": mtTPRMIM20,
       "mtTPRMIM22": mtTPRMIM22,
       "mtTPRMIM20S": mtTPRMIM20S,
       "mtTPRMIM22S": mtTPRMIM22S,
       "mtTPRMIM33S": mtTPRMIM33S,
       "mtTPRMIM36S": mtTPRMIM36S,
       "mtCXRMIMs": mtCXRMIMs,
       "mtFormim22S": mtFormim22S,
       "mtFBRMIM26": mtFBRMIM26,
       "mtFBRMIM22": mtFBRMIM22,
       "mtFOMIM18": mtFOMIM18,
       "mtFOMIM12": mtFOMIM12,
       "mtFOMIM16": mtFOMIM16,
       "mtFOMIM28": mtFOMIM28,
       "mtFOMIM22": mtFOMIM22,
       "mtFOMIM26": mtFOMIM26,
       "mtFOMIM38": mtFOMIM38,
       "mtFOMIM32": mtFOMIM32,
       "mtFOMIM36": mtFOMIM36,
       "mtMT8MIM": mtMT8MIM,
       "mtIRM2": mtIRM2,
       "mtIRBM": mtIRBM,
       "mtIRM3": mtIRM3,
       "mtTRMM1": mtTRMM1,
       "mtTRMM2": mtTRMM2,
       "mtTRMMIM1": mtTRMMIM1,
       "mtEFDMIM": mtEFDMIM,
       "mtTRMM4": mtTRMM4,
       "mtTRBMIM": mtTRBMIM,
       "mtEMME": mtEMME,
       "mtESXMIM": mtESXMIM,
       "mtTRMM": mtTRMM,
       "mtTRMMIM2": mtTRMMIM2,
       "mtETWMIM": mtETWMIM,
       "mtTRMMIM": mtTRMMIM,
       "mtESXMIMF2": mtESXMIMF2,
       "mtFOT12or22": mtFOT12or22,
       "mtTPTMIM": mtTPTMIM,
       "mtFOT16or26": mtFOT16or26,
       "mtSNACRS232wRS232": mtSNACRS232wRS232,
       "mtSNACRS232wV35": mtSNACRS232wV35,
       "mtSNACRS232wRS530": mtSNACRS232wRS530,
       "mtSNACRS232wNoDB": mtSNACRS232wNoDB,
       "mtSNACV35wRS232": mtSNACV35wRS232,
       "mtSNACV35wV35": mtSNACV35wV35,
       "mtSNACV35wRS350": mtSNACV35wRS350,
       "mtSNACV35wNoDB": mtSNACV35wNoDB,
       "mtSNACRS530wRS232": mtSNACRS530wRS232,
       "mtSNACRS530wV35": mtSNACRS530wV35,
       "mtSNACRS530wRS530": mtSNACRS530wRS530,
       "mtSNACRS530wNoDB": mtSNACRS530wNoDB,
       "mtSNACMIMConnectivity": mtSNACMIMConnectivity,
       "mtSNACConnectivityMIM": mtSNACConnectivityMIM,
       "mtSNACConnectivity": mtSNACConnectivity,
       "mtNull": mtNull,
       "mtTRMIMa10R": mtTRMIMa10R,
       "mtTRMIMa20R": mtTRMIMa20R,
       "mtTRMIM22ARO": mtTRMIM22ARO,
       "mtTRRMIM2A": mtTRRMIM2A,
       "mtTRMIM24ARO": mtTRMIM24ARO,
       "mtTRRMIM4A": mtTRRMIM4A,
       "mtTRRMIMAT": mtTRRMIMAT,
       "mtTRMIM42ARO": mtTRMIM42ARO,
       "mtTRRMIM2AT": mtTRRMIM2AT,
       "mtTRMIM44ARO": mtTRMIM44ARO,
       "mtTRRMIM4AT": mtTRRMIM4AT,
       "mtMPIMX": mtMPIMX,
       "mtMPIMA": mtMPIMA,
       "mtMPIMC": mtMPIMC,
       "mtMPIMT": mtMPIMT,
       "mtMPIMF2": mtMPIMF2,
       "mtMPIMF1": mtMPIMF1,
       "mtMPIMT1": mtMPIMT1,
       "mtMPIMB": mtMPIMB,
       "mtMiniMMAC": mtMiniMMAC,
       "mtMRXIE": mtMRXIE,
       "mtMRXI24": mtMRXI24,
       "mtMRXI22": mtMRXI22,
       "mtMRXI34": mtMRXI34,
       "mtMRXI32": mtMRXI32,
       "mtMRXI2E": mtMRXI2E,
       "mtSPIMX": mtSPIMX,
       "mtSPIMA": mtSPIMA,
       "mtSPIMC": mtSPIMC,
       "mtSPIMT": mtSPIMT,
       "mtSPIMF2": mtSPIMF2,
       "mtSPIMF1": mtSPIMF1,
       "mtSPIMT1": mtSPIMT1,
       "mtSPIMB": mtSPIMB,
       "mtEPIMB": mtEPIMB,
       "mtEPIMA": mtEPIMA,
       "mtEPIMC": mtEPIMC,
       "mtEPIMT": mtEPIMT,
       "mtEPIMF2": mtEPIMF2,
       "mtEPIMF1": mtEPIMF1,
       "mtEPIMT1": mtEPIMT1,
       "mtEPIMF3": mtEPIMF3,
       "mtEPIMX": mtEPIMX,
       "mtEPIMTfd": mtEPIMTfd,
       "mtEPIMF2fd": mtEPIMF2fd,
       "mtEPIMF1fd": mtEPIMF1fd,
       "mtEPIMF3fd": mtEPIMF3fd,
       "mtEPIMFIXED": mtEPIMFIXED,
       "mtMRXI": mtMRXI,
       "mtMRXI2": mtMRXI2,
       "slotClass": slotClass,
       "csUnknown": csUnknown,
       "csPwrSup": csPwrSup,
       "csMgmt": csMgmt,
       "csMgmtRelay": csMgmtRelay,
       "csMIM": csMIM,
       "backplaneType": backplaneType,
       "btUnknown": btUnknown,
       "btBusA": btBusA,
       "btBusB": btBusB,
       "btBusC": btBusC,
       "componentType": componentType,
       "cptUnknown": cptUnknown,
       "cptRepeater": cptRepeater,
       "cptMau": cptMau,
       "cptBridge": cptBridge,
       "cptRouter": cptRouter,
       "cptRmon": cptRmon,
       "cptAgent": cptAgent,
       "cptLim": cptLim,
       "cptHostSvcs": cptHostSvcs,
       "cptIngMIM": cptIngMIM,
       "cptDLM": cptDLM,
       "cptMIBNavigator": cptMIBNavigator,
       "cptRmonHost": cptRmonHost,
       "cptRmonCapture": cptRmonCapture,
       "cptMibMgr": cptMibMgr,
       "cptFddiSmt": cptFddiSmt,
       "cptSFPS": cptSFPS,
       "cptModuleMgmt": cptModuleMgmt,
       "cptOrphan": cptOrphan,
       "cptATM": cptATM,
       "cptWebview": cptWebview,
       "cpt802p1Q": cpt802p1Q,
       "cpt802p1p": cpt802p1p,
       "cptTrafficGen": cptTrafficGen,
       "thrPtyModType": thrPtyModType,
       "tpMtETSMIM": tpMtETSMIM,
       "tpMtDNSMIM": tpMtDNSMIM,
       "tpMtGatorMIM": tpMtGatorMIM,
       "tpMtLanternMIM": tpMtLanternMIM,
       "tpMtCRML": tpMtCRML,
       "tpMtCRM": tpMtCRM,
       "networkType": networkType,
       "ntManagementTypes": ntManagementTypes,
       "ntInbandMgmt": ntInbandMgmt,
       "ntSideBandMgmt": ntSideBandMgmt,
       "ntOutOfBandMgmt": ntOutOfBandMgmt,
       "physicalType": physicalType,
       "portType": portType,
       "portStandard": portStandard,
       "portEthernet": portEthernet,
       "portUnknown": portUnknown,
       "portBNC": portBNC,
       "portAUI": portAUI,
       "portTrans": portTrans,
       "portCTp": portCTp,
       "portRJ45": portRJ45,
       "portDb9": portDb9,
       "portRJ71": portRJ71,
       "portMmfSMA": portMmfSMA,
       "portMmfST": portMmfST,
       "portSmfST": portSmfST,
       "portBPlaneA": portBPlaneA,
       "portBPlaneB": portBPlaneB,
       "portBPlaneC": portBPlaneC,
       "portMmfMTRJb10FL": portMmfMTRJb10FL,
       "portTokenRing": portTokenRing,
       "portTRUnknown": portTRUnknown,
       "portLobeUtpRJ45": portLobeUtpRJ45,
       "portLobeStpDb9": portLobeStpDb9,
       "portLobeStpRJ45": portLobeStpRJ45,
       "portLobeMmfST": portLobeMmfST,
       "portLobeSmfST": portLobeSmfST,
       "portRingpStpDb9": portRingpStpDb9,
       "portRingpMmfST": portRingpMmfST,
       "portLobeUtpStpRJ45": portLobeUtpStpRJ45,
       "portFDDI": portFDDI,
       "portFDDIUnknown": portFDDIUnknown,
       "portFDDIMmfMic": portFDDIMmfMic,
       "portFDDIUtpRJ45": portFDDIUtpRJ45,
       "portFDDIStpRJ45": portFDDIStpRJ45,
       "portFDDISmfMic1": portFDDISmfMic1,
       "portFDDIMmfSc": portFDDIMmfSc,
       "portFDDISmfSc": portFDDISmfSc,
       "portFDDIMmfSt": portFDDIMmfSt,
       "portFDDISmfSt": portFDDISmfSt,
       "portFDDISmLrfSc": portFDDISmLrfSc,
       "portNotPresent": portNotPresent,
       "portATM": portATM,
       "portATM155MMF": portATM155MMF,
       "portATM155SMF": portATM155SMF,
       "portBackplane": portBackplane,
       "portInternal": portInternal,
       "portFastEthernet": portFastEthernet,
       "portUnknownb100": portUnknownb100,
       "portRJ45b100TX": portRJ45b100TX,
       "portRJ45b100T4": portRJ45b100T4,
       "portRJ45b100T2": portRJ45b100T2,
       "portMmfScb100FX": portMmfScb100FX,
       "portSmfScb100FX": portSmfScb100FX,
       "portRJ71b100TX": portRJ71b100TX,
       "portMmfMTRJb100FX": portMmfMTRJb100FX,
       "portSmfMTRJb100FX": portSmfMTRJb100FX,
       "portGigEthernet": portGigEthernet,
       "portSc1000SX": portSc1000SX,
       "portSc1000LX": portSc1000LX,
       "portRJ451000T": portRJ451000T,
       "portXpim": portXpim,
       "portEpim": portEpim,
       "portEpimUnknown": portEpimUnknown,
       "portEpimAUI": portEpimAUI,
       "portEpimBNC": portEpimBNC,
       "portEpimRJ45": portEpimRJ45,
       "portEpimMmfST": portEpimMmfST,
       "portEpimMmfSMA": portEpimMmfSMA,
       "portEpimSmfST": portEpimSmfST,
       "portEpimTrans": portEpimTrans,
       "portEpimThirdParty": portEpimThirdParty,
       "portEpimThirdPartyBrim": portEpimThirdPartyBrim,
       "portEpimThirdPartyCABO": portEpimThirdPartyCABO,
       "portEpimThirdPartyNonBrim": portEpimThirdPartyNonBrim,
       "portEpimThirdPartyUnknown": portEpimThirdPartyUnknown,
       "portEpimRJ45fd": portEpimRJ45fd,
       "portEpimMmfSTfd": portEpimMmfSTfd,
       "portEpimMmfSMAfd": portEpimMmfSMAfd,
       "portEpimSmfSTfd": portEpimSmfSTfd,
       "portEpimHWAUI": portEpimHWAUI,
       "portEpim100Tx": portEpim100Tx,
       "portEpim100Fx": portEpim100Fx,
       "portEpim100Fmb": portEpim100Fmb,
       "portEpim1002F2": portEpim1002F2,
       "portEpim1002F3": portEpim1002F3,
       "portEpim1002F4": portEpim1002F4,
       "portTpim": portTpim,
       "portTpimUnkown": portTpimUnkown,
       "portTpimT1": portTpimT1,
       "portTpimF2": portTpimF2,
       "portTpimT2": portTpimT2,
       "portTpimF3": portTpimF3,
       "portTpimT4": portTpimT4,
       "portFpim": portFpim,
       "portFpimUnknown": portFpimUnknown,
       "portFpim0": portFpim0,
       "portFpim2": portFpim2,
       "portFpim4": portFpim4,
       "portFpim5": portFpim5,
       "portFpim1": portFpim1,
       "portFpim7": portFpim7,
       "portFpim8": portFpim8,
       "portFpim9": portFpim9,
       "portApim": portApim,
       "portApim02": portApim02,
       "portApim11": portApim11,
       "portApim21": portApim21,
       "portApim29": portApim29,
       "portApim67": portApim67,
       "portApim28": portApim28,
       "portApim22": portApim22,
       "portApimUnknown": portApimUnknown,
       "portApim29LR": portApim29LR,
       "portApim31": portApim31,
       "portApim39": portApim39,
       "portApim39LR": portApim39LR,
       "portWpim": portWpim,
       "portWpimUnknown": portWpimUnknown,
       "portWpimT1": portWpimT1,
       "portWpimE1": portWpimE1,
       "portWpimSy": portWpimSy,
       "portWpimDDS": portWpimDDS,
       "portWpimDI": portWpimDI,
       "portWpimHDSL": portWpimHDSL,
       "portWpimBRI": portWpimBRI,
       "portWpimDS30": portWpimDS30,
       "portWpimDataCapableDI": portWpimDataCapableDI,
       "portWpimT1DDS": portWpimT1DDS,
       "portWpimRDDS": portWpimRDDS,
       "portWpimRT1": portWpimRT1,
       "portWpimRE1": portWpimRE1,
       "portFEpim": portFEpim,
       "portFEUnknown": portFEUnknown,
       "portFE100TxUTP": portFE100TxUTP,
       "portFE100TxSTP": portFE100TxSTP,
       "portFE100Fx": portFE100Fx,
       "portFE100VG4": portFE100VG4,
       "portFE100VGF": portFE100VGF,
       "portFE100F3": portFE100F3,
       "portFE100S1": portFE100S1,
       "portFE100S3": portFE100S3,
       "portFE100S5": portFE100S5,
       "portFE100LH": portFE100LH,
       "portGpim": portGpim,
       "portGpimF01": portGpimF01,
       "portGpimF09": portGpimF09,
       "portGpimS41": portGpimS41,
       "portGpimS49": portGpimS49,
       "portGpimS51": portGpimS51,
       "portGpimS59": portGpimS59,
       "portGpimS31": portGpimS31,
       "portGpimS39": portGpimS39,
       "portGpim01": portGpim01,
       "portGpim04": portGpim04,
       "portGpim09": portGpim09,
       "portGpim08": portGpim08,
       "portVapim": portVapim,
       "portVapim31": portVapim31,
       "portVapim39": portVapim39,
       "portVapim39LR": portVapim39LR,
       "portXnim": portXnim,
       "portAnim": portAnim,
       "portAnim21p3": portAnim21p3,
       "portAnim29p3": portAnim29p3,
       "portAnim22p4": portAnim22p4,
       "portAnim31p2": portAnim31p2,
       "portAnim39p2": portAnim39p2,
       "portAnim29p4LR": portAnim29p4LR,
       "portAnim29p3LR": portAnim29p3LR,
       "portAnim39p2LR": portAnim39p2LR,
       "portAnim59p1LR": portAnim59p1LR,
       "portAnim21p4": portAnim21p4,
       "portAnim29p4": portAnim29p4,
       "portAnim67p2": portAnim67p2,
       "portAnim77p2": portAnim77p2,
       "portAnim51p1": portAnim51p1,
       "portAnim59p1": portAnim59p1,
       "portVirtualType": portVirtualType,
       "portVirtualTypeSvc": portVirtualTypeSvc,
       "portVirtualTypePvcLlc": portVirtualTypePvcLlc,
       "portVirtualTypePvcVcmux": portVirtualTypePvcVcmux,
       "portVirtualSMB": portVirtualSMB,
       "portCATV": portCATV,
       "portCATVUnknown": portCATVUnknown,
       "port75ohmFemaleFType": port75ohmFemaleFType,
       "hardwareType": hardwareType,
       "chipType": chipType,
       "fddiMACDP83261": fddiMACDP83261,
       "fddiPortDP83251": fddiPortDP83251,
       "i960sa": i960sa,
       "i960ca": i960ca,
       "i960cf": i960cf,
       "i960ha": i960ha,
       "i960hd": i960hd,
       "i960ht": i960ht,
       "powerPC603": powerPC603,
       "powerPC603e": powerPC603e,
       "powerPC604": powerPC604,
       "powerPC740": powerPC740,
       "powerMIPS5000": powerMIPS5000,
       "powerPC8241": powerPC8241,
       "powerPC8245": powerPC8245,
       "psMonitorTypes": psMonitorTypes,
       "powerSupplyMonitors": powerSupplyMonitors,
       "powerSupplyInputMonitor": powerSupplyInputMonitor,
       "powerSupplyTermConvInput": powerSupplyTermConvInput,
       "powerSupplyLogicConvInput": powerSupplyLogicConvInput,
       "powerSupplyTermOutput": powerSupplyTermOutput,
       "powerSupplyLogicOutput": powerSupplyLogicOutput,
       "powerSupplyHighVoltageOutput": powerSupplyHighVoltageOutput,
       "chassisPowerMonitors": chassisPowerMonitors,
       "chassisHighVoltageRail": chassisHighVoltageRail,
       "chassisLogicRail": chassisLogicRail,
       "chassisTermRail": chassisTermRail,
       "modulePowerMonitors": modulePowerMonitors,
       "moduleHighVoltageInput": moduleHighVoltageInput,
       "moduleLogicVoltageOutput": moduleLogicVoltageOutput,
       "moduleAux1Output": moduleAux1Output,
       "moduleAux2Output": moduleAux2Output,
       "mtExpanded": mtExpanded,
       "mtThrdParty": mtThrdParty,
       "tpAEnet": tpAEnet,
       "mtPassaggioMim": mtPassaggioMim,
       "tpABorC": tpABorC,
       "mtCiscoCRM3E": mtCiscoCRM3E,
       "mtCrm2RE": mtCrm2RE,
       "mtSnacMimRS232": mtSnacMimRS232,
       "mtSnacMimRS232wRS232DB": mtSnacMimRS232wRS232DB,
       "mtSnacMimRS232wV35DB": mtSnacMimRS232wV35DB,
       "mtSnacMimRS232wRS422DB": mtSnacMimRS232wRS422DB,
       "mtSnacMimv35": mtSnacMimv35,
       "mtSnacMimv35wRS232DB": mtSnacMimv35wRS232DB,
       "mtSnacMimV35wV35DB": mtSnacMimV35wV35DB,
       "mtSnacMimV35wRS422DB": mtSnacMimV35wRS422DB,
       "mtSnacMimRS422DB": mtSnacMimRS422DB,
       "mtSnacMimRS422wRS232DB": mtSnacMimRS422wRS232DB,
       "mtSnacMimRS422wV35DB": mtSnacMimRS422wV35DB,
       "mtSnacMimRS422wRS422DB": mtSnacMimRS422wRS422DB,
       "mtSnacMimSXRS232": mtSnacMimSXRS232,
       "mtSnacMimSXRS232wRS232DB": mtSnacMimSXRS232wRS232DB,
       "mtSnacMimSXRS232wV35DB": mtSnacMimSXRS232wV35DB,
       "mtSnacMimSXRS232wRS422DB": mtSnacMimSXRS232wRS422DB,
       "mtSnacMimSXv35": mtSnacMimSXv35,
       "mtSnacMimSXv35wRS232DB": mtSnacMimSXv35wRS232DB,
       "mtSnacMimSXV35wV35DB": mtSnacMimSXV35wV35DB,
       "mtSnacMimSXV35wRS422DB": mtSnacMimSXV35wRS422DB,
       "mtSnacMimSXRS422DB": mtSnacMimSXRS422DB,
       "mtSnacMimSXRS422wRS232DB": mtSnacMimSXRS422wRS232DB,
       "mtSnacMimSXRS422wV35DB": mtSnacMimSXRS422wV35DB,
       "mtSnacMimSXRS422wRS422DB": mtSnacMimSXRS422wRS422DB,
       "tpABandC": tpABandC,
       "tpTrFNB": tpTrFNB,
       "mtCiscoCRM3T": mtCiscoCRM3T,
       "mtTRMMIM62A": mtTRMMIM62A,
       "mt3174MIM": mt3174MIM,
       "mtSNACmimRS232": mtSNACmimRS232,
       "mtSNACmimRS232v35db": mtSNACmimRS232v35db,
       "mtSNACmimRS232wRS422db": mtSNACmimRS232wRS422db,
       "mtSNACmimRS232wodb486": mtSNACmimRS232wodb486,
       "mtSNACmimv35wRS232db": mtSNACmimv35wRS232db,
       "mtSNACmimv35wv35db": mtSNACmimv35wv35db,
       "mtSNACmimv35RS422db": mtSNACmimv35RS422db,
       "mtSNACmimv35wodb": mtSNACmimv35wodb,
       "mtSNACmimRS422": mtSNACmimRS422,
       "mtSNACmimRS422wv35db": mtSNACmimRS422wv35db,
       "mtSNACmimRS422wRS422db": mtSNACmimRS422wRS422db,
       "mtSNACmimrs433": mtSNACmimrs433,
       "tpTrFDDIFNB": tpTrFDDIFNB,
       "tpTrAEnet": tpTrAEnet,
       "tpTrFDDIAEnet": tpTrFDDIAEnet,
       "tpATM": tpATM,
       "tpATMMIM": tpATMMIM,
       "tpATMMIMx8": tpATMMIMx8,
       "tpSS1500Modular": tpSS1500Modular,
       "tpSS1500Compact": tpSS1500Compact,
       "tpStandAlone": tpStandAlone,
       "tpELS10024TX": tpELS10024TX,
       "tpELS10024TXM": tpELS10024TXM,
       "tpELS10024TXG": tpELS10024TXG,
       "tpELH10012": tpELH10012,
       "tpELH10024": tpELH10024,
       "tpELS10024FXG": tpELS10024FXG,
       "tpELS100S24TX2M": tpELS100S24TX2M,
       "xylogicsMIMs": xylogicsMIMs,
       "xylogicsCSMIM16": xylogicsCSMIM16,
       "xylogicsCSMIM32": xylogicsCSMIM32,
       "mtCSMIM16m2": mtCSMIM16m2,
       "mtMODMIM4": mtMODMIM4,
       "mtMODMIM4x4": mtMODMIM4x4,
       "mtMODMIM4x8": mtMODMIM4x8,
       "mtCSMIM32m2": mtCSMIM32m2,
       "mtCSMIMm8T1": mtCSMIMm8T1,
       "mtCSMIMm16T1": mtCSMIMm16T1,
       "mtCSMIMm24T1": mtCSMIMm24T1,
       "mtCSmimBri3": mtCSmimBri3,
       "mtCSmimBri6": mtCSmimBri6,
       "mtOlicom": mtOlicom,
       "mtSTS16-20": mtSTS16_20,
       "mtHSTS100-16RM": mtHSTS100_16RM,
       "mtTPSoftware": mtTPSoftware,
       "mtBIGIP": mtBIGIP,
       "mt3DNS": mt3DNS,
       "mtChassis": mtChassis,
       "cA": cA,
       "cABorC": cABorC,
       "cABandC": cABandC,
       "cTrFNB": cTrFNB,
       "mtTbrmim": mtTbrmim,
       "cFDDIFNB": cFDDIFNB,
       "cTrA": cTrA,
       "mtPCMIM": mtPCMIM,
       "cFDDIA": cFDDIA,
       "cNoABorC": cNoABorC,
       "sonixMIM": sonixMIM,
       "mmacFPS": mmacFPS,
       "thirdPartyBrims": thirdPartyBrims,
       "mtCiscoBrimE": mtCiscoBrimE,
       "mtCiscoBrimTR": mtCiscoBrimTR,
       "mtXylogicsUCS": mtXylogicsUCS,
       "mtXylogicsUSnac": mtXylogicsUSnac,
       "mtXylogicsUSnacT": mtXylogicsUSnacT,
       "mtXylogicsUBrics": mtXylogicsUBrics,
       "mtEthernet": mtEthernet,
       "mtEtherA": mtEtherA,
       "mtEtherRic": mtEtherRic,
       "mtEtherEPIM": mtEtherEPIM,
       "mtEtherStandAlone": mtEtherStandAlone,
       "mtUMMAC22E": mtUMMAC22E,
       "mtUMMAC32E": mtUMMAC32E,
       "mtUMMAC24E": mtUMMAC24E,
       "mtUMMAC34E": mtUMMAC34E,
       "mtSEH22": mtSEH22,
       "mtSEH32": mtSEH32,
       "mtSEH24": mtSEH24,
       "mtSEH34": mtSEH34,
       "mtNBR620": mtNBR620,
       "mtSEHi22": mtSEHi22,
       "mtSEHi24": mtSEHi24,
       "mtSEHi26FB": mtSEHi26FB,
       "mtSEHi22FB": mtSEHi22FB,
       "mtSEHi32": mtSEHi32,
       "mtSEHi34": mtSEHi34,
       "mtSEH26C": mtSEH26C,
       "mtSEH22C": mtSEH22C,
       "mtSEH26FL": mtSEH26FL,
       "mtSEH22FL": mtSEH22FL,
       "mtUMMAC26FL": mtUMMAC26FL,
       "mtUMMAC22FL": mtUMMAC22FL,
       "mtNBR220": mtNBR220,
       "mtNBR420": mtNBR420,
       "mtSEH22S": mtSEH22S,
       "mtSEH32S": mtSEH32S,
       "mtSEH24S": mtSEH24S,
       "mtSEH34S": mtSEH34S,
       "mtSEH26FBS": mtSEH26FBS,
       "mtSEH22FBS": mtSEH22FBS,
       "mtSEH26CS": mtSEH26CS,
       "mtSEH22CS": mtSEH22CS,
       "mtSEH26FLS": mtSEH26FLS,
       "mtSEH22FLS": mtSEH22FLS,
       "mtSEHi22S": mtSEHi22S,
       "mtSEHi24S": mtSEHi24S,
       "mtSEHi32S": mtSEHi32S,
       "mtSEHi34S": mtSEHi34S,
       "mtUMMAC22ES": mtUMMAC22ES,
       "mtUMMAC32ES": mtUMMAC32ES,
       "mtUMMAC24ES": mtUMMAC24ES,
       "mtUMMAC34ES": mtUMMAC34ES,
       "mtUMMAC22UCSs": mtUMMAC22UCSs,
       "mtUMMAC22EUCS": mtUMMAC22EUCS,
       "mtUMMAC22UCSsSnac": mtUMMAC22UCSsSnac,
       "mtUMMAC22EUCSSnac": mtUMMAC22EUCSSnac,
       "mtUMMAC22EBrics": mtUMMAC22EBrics,
       "mtUMMAC22ESBrics": mtUMMAC22ESBrics,
       "mtESX1320": mtESX1320,
       "mtESX1380": mtESX1380,
       "mtSEHi22FLS": mtSEHi22FLS,
       "mtSEHi26FLS": mtSEHi26FLS,
       "mtSEHi22FL": mtSEHi22FL,
       "mtSEHi26FL": mtSEHi26FL,
       "mtSEH100Tx22": mtSEH100Tx22,
       "mtSEHi100Tx22": mtSEHi100Tx22,
       "mt8H02p16": mt8H02p16,
       "mt2E42p27": mt2E42p27,
       "mt2E42p27R": mt2E42p27R,
       "mt2E43p27": mt2E43p27,
       "mt2E43p27R": mt2E43p27R,
       "mt2E43p51": mt2E43p51,
       "mt2E43p51R": mt2E43p51R,
       "mt2H43p51": mt2H43p51,
       "mt2H43p51R": mt2H43p51R,
       "mt2E42p27RDC": mt2E42p27RDC,
       "mt2E42p27DC": mt2E42p27DC,
       "mt2M46p04": mt2M46p04,
       "mt2E48p27R": mt2E48p27R,
       "mt2E48p27": mt2E48p27,
       "mt2E49p27": mt2E49p27,
       "mt2E49p27R": mt2E49p27R,
       "mt2E49p27RDC": mt2E49p27RDC,
       "mt2M46p04R": mt2M46p04R,
       "mt2M46p04RDC": mt2M46p04RDC,
       "mt2H28p08R": mt2H28p08R,
       "mt2H22p08R": mt2H22p08R,
       "mt2H23p50R": mt2H23p50R,
       "mt2H33p37R": mt2H33p37R,
       "mt2H252p25": mt2H252p25,
       "mt2H252p25R": mt2H252p25R,
       "mt2M256p04R": mt2M256p04R,
       "mt2E253p49R": mt2E253p49R,
       "mt2H258p17R": mt2H258p17R,
       "mt2H253p25R": mt2H253p25R,
       "mt2H252p25RDC": mt2H252p25RDC,
       "mt2H259p17R": mt2H259p17R,
       "mtELS10082F2": mtELS10082F2,
       "mtELS10024TX2M": mtELS10024TX2M,
       "mtELS10024FX2M": mtELS10024FX2M,
       "mtELS10048TX2M": mtELS10048TX2M,
       "mtELS10008SX1M": mtELS10008SX1M,
       "mtELS100012SX2M": mtELS100012SX2M,
       "mtELS10016FXG": mtELS10016FXG,
       "mtELS100024TX2MA": mtELS100024TX2MA,
       "mtELS10024TX1M": mtELS10024TX1M,
       "etherSlot1": etherSlot1,
       "mtEMME6": mtEMME6,
       "mtEnetBrim": mtEnetBrim,
       "mtBrimUnk": mtBrimUnk,
       "mtBrimE6": mtBrimE6,
       "mt100MBEnet": mt100MBEnet,
       "mtBrimE100": mtBrimE100,
       "mtmmacEthernetSmartSwitch": mtmmacEthernetSmartSwitch,
       "mtSmartMIM216": mtSmartMIM216,
       "mtEnetHSIM": mtEnetHSIM,
       "mtHSIMpG01": mtHSIMpG01,
       "mtHSIMpG09": mtHSIMpG09,
       "mtHSIMFE6": mtHSIMFE6,
       "mtVHSIMG6": mtVHSIMG6,
       "mtEnetRepeater": mtEnetRepeater,
       "mtEnetABC": mtEnetABC,
       "mtTPXMIM20": mtTPXMIM20,
       "mtTPXMIM22": mtTPXMIM22,
       "mtTPXMIM33": mtTPXMIM33,
       "mtTPXMIM34": mtTPXMIM34,
       "mtTpxmim20S": mtTpxmim20S,
       "mtTpxmim22S": mtTpxmim22S,
       "mtTpxmim33S": mtTpxmim33S,
       "mtTpxmim34S": mtTpxmim34S,
       "mtTokenRing": mtTokenRing,
       "mtTRActive": mtTRActive,
       "mtTRMIM22A": mtTRMIM22A,
       "mtTRMIM24A": mtTRMIM24A,
       "mtTRMIM42A": mtTRMIM42A,
       "mtTRMIM44A": mtTRMIM44A,
       "mtTRFMIM32": mtTRFMIM32,
       "mtTRFMIM36": mtTRFMIM36,
       "mtTRFMIM38": mtTRFMIM38,
       "mtTRRepeater": mtTRRepeater,
       "mtTRRMIMf2t": mtTRRMIMf2t,
       "mtTRRMIMf3t": mtTRRMIMf3t,
       "mtTRRMIMat": mtTRRMIMat,
       "mtTRRMIM2at": mtTRRMIM2at,
       "mtTRRMIM4at": mtTRRMIM4at,
       "mtTPIM": mtTPIM,
       "mtTPIMUnk": mtTPIMUnk,
       "mtTPIMT1": mtTPIMT1,
       "mtTPIMF2": mtTPIMF2,
       "mtTPIMT4": mtTPIMT4,
       "mtTPIMT2": mtTPIMT2,
       "mtTPIMF3": mtTPIMF3,
       "mtTRBrim": mtTRBrim,
       "mtBrimT6": mtBrimT6,
       "mtTRStandAlone": mtTRStandAlone,
       "mtTSX1620": mtTSX1620,
       "mtTrxi24": mtTrxi24,
       "mtTrxi22": mtTrxi22,
       "mtTrxi24A": mtTrxi24A,
       "mtTrxi22A": mtTrxi22A,
       "mtTrxi44": mtTrxi44,
       "mtTrxi42": mtTrxi42,
       "mtTrxi44A": mtTrxi44A,
       "mtTrxi42A": mtTrxi42A,
       "mtTRManagement": mtTRManagement,
       "mtTRMMIM4at": mtTRMMIM4at,
       "mtTRMMIM2at": mtTRMMIM2at,
       "mtTRMMIMF2t": mtTRMMIMF2t,
       "mtTRMMIMF3t": mtTRMMIMF3t,
       "mtTBRMIM": mtTBRMIM,
       "mtSTH": mtSTH,
       "mtSTH44A": mtSTH44A,
       "mtSTH24A": mtSTH24A,
       "mtSTH42A": mtSTH42A,
       "mtSTH22A": mtSTH22A,
       "mtSTHI": mtSTHI,
       "mtSTHI44A": mtSTHI44A,
       "mtSTHI24A": mtSTHI24A,
       "mtSTHI42A": mtSTHI42A,
       "mtSTHI22A": mtSTHI22A,
       "mtUMMAC": mtUMMAC,
       "mtUMMAC44T": mtUMMAC44T,
       "mtUMMAC24T": mtUMMAC24T,
       "mtUMMAC42T": mtUMMAC42T,
       "mtUMMAC22T": mtUMMAC22T,
       "mtTRPortSwitch": mtTRPortSwitch,
       "mtTRXMIM22A": mtTRXMIM22A,
       "mtTRXMIM24A": mtTRXMIM24A,
       "mtTRXMIM42A": mtTRXMIM42A,
       "mtTRXMIM44A": mtTRXMIM44A,
       "mtTRXMIM54A": mtTRXMIM54A,
       "mtTDRMIM22A": mtTDRMIM22A,
       "mtTDRMIM42A": mtTDRMIM42A,
       "mtCrm2RT": mtCrm2RT,
       "mtTDRMIMAT": mtTDRMIMAT,
       "mtFDDI": mtFDDI,
       "mtFDDIconcFIBER": mtFDDIconcFIBER,
       "mtFDDIconcTWISTED": mtFDDIconcTWISTED,
       "mtFDCMIM12": mtFDCMIM12,
       "mtFDCMIM42": mtFDCMIM42,
       "mtFDCMIM16": mtFDCMIM16,
       "mtFDCMIM26": mtFDCMIM26,
       "mtFDCMIM46": mtFDCMIM46,
       "mtFDCMIM22": mtFDCMIM22,
       "mtFDCMIM44": mtFDCMIM44,
       "mtFDCMIM48": mtFDCMIM48,
       "mtFDDImanagement": mtFDDImanagement,
       "mtFDMMIM24mmf": mtFDMMIM24mmf,
       "mtFddiBrim": mtFddiBrim,
       "mtBrimFD0": mtBrimFD0,
       "mtBrimFD6": mtBrimFD6,
       "mtBrimFD5": mtBrimFD5,
       "mtFddiHsim": mtFddiHsim,
       "mtFddiHsimF6": mtFddiHsimF6,
       "mtWan": mtWan,
       "mtWanBrim": mtWanBrim,
       "mtBrimWT1": mtBrimWT1,
       "mtBrimW6": mtBrimW6,
       "mtBrimWB4": mtBrimWB4,
       "mtWanCyberSwitch": mtWanCyberSwitch,
       "mtWanCyberSwitch200": mtWanCyberSwitch200,
       "mtWanCyberSwitch300": mtWanCyberSwitch300,
       "mtWanCyberSwitch400": mtWanCyberSwitch400,
       "mtWanCyberSwitch150": mtWanCyberSwitch150,
       "mtWanCyberSwitch1200": mtWanCyberSwitch1200,
       "mtWanCyberSwitch6000": mtWanCyberSwitch6000,
       "mtWanCyberSwitch7000": mtWanCyberSwitch7000,
       "mtWanCyberSwitch5500": mtWanCyberSwitch5500,
       "mtWanCyberSwitch9W000p00": mtWanCyberSwitch9W000p00,
       "mtWanCyberSwitch9W426p420": mtWanCyberSwitch9W426p420,
       "mtWanCyberSwitch9W427p420": mtWanCyberSwitch9W427p420,
       "mtWanCyberSwitchNE1000": mtWanCyberSwitchNE1000,
       "mtWanCyberSwitchPOTS": mtWanCyberSwitchPOTS,
       "mtWanCyberSwitchNTp1": mtWanCyberSwitchNTp1,
       "mtWanCyberSwitchBRI1": mtWanCyberSwitchBRI1,
       "mtWanCyberSwitchBRI4": mtWanCyberSwitchBRI4,
       "mtWanCyberSwitchPRI8": mtWanCyberSwitchPRI8,
       "mtWanCyberSwitchPRI23": mtWanCyberSwitchPRI23,
       "mtWanCyberSwitchEXP": mtWanCyberSwitchEXP,
       "mtWanCyberSwitchRS232": mtWanCyberSwitchRS232,
       "mtWanCyberSwitchV35": mtWanCyberSwitchV35,
       "mtWanCyberSwitchDIG": mtWanCyberSwitchDIG,
       "mtWanCyberSwitchDIG24": mtWanCyberSwitchDIG24,
       "mtWanCyberSwitchDIG24Plus": mtWanCyberSwitchDIG24Plus,
       "mtWanCyberSwitchDIG30Plus": mtWanCyberSwitchDIG30Plus,
       "mtWanCyberSwitchAUI1": mtWanCyberSwitchAUI1,
       "mtWanCyberSwitchAUI2": mtWanCyberSwitchAUI2,
       "mtWanThirdParty": mtWanThirdParty,
       "tpWanCyberSwitch100": tpWanCyberSwitch100,
       "mtWanHsim": mtWanHsim,
       "mtWanHsimW6": mtWanHsimW6,
       "mtWanHsimW84": mtWanHsimW84,
       "mtWanHsimW87": mtWanHsimW87,
       "mtWanHsimWB4": mtWanHsimWB4,
       "mtWanHsimSSA710": mtWanHsimSSA710,
       "mtWanHsimSSA720": mtWanHsimSSA720,
       "mtWanHsimWD1": mtWanHsimWD1,
       "mtWanHsimW85": mtWanHsimW85,
       "mtWanHsimSSA710p48": mtWanHsimSSA710p48,
       "mtWanHsimSSA720p60": mtWanHsimSSA720p60,
       "mtWanCMM": mtWanCMM,
       "mtWanCMM824": mtWanCMM824,
       "mtWanCMM3248": mtWanCMM3248,
       "mtWanCMM3264": mtWanCMM3264,
       "mtWanCMM3224": mtWanCMM3224,
       "mtWanCMM3232": mtWanCMM3232,
       "mtWanAccess": mtWanAccess,
       "mtAS316": mtAS316,
       "mtSSA710p48": mtSSA710p48,
       "mtSSA720p60": mtSSA720p60,
       "mtATM": mtATM,
       "mtAtmBrim": mtAtmBrim,
       "mtBrimA100": mtBrimA100,
       "mtBrimA6": mtBrimA6,
       "mtBrimA6DP": mtBrimA6DP,
       "mtAtmHsim": mtAtmHsim,
       "mtAtmHsimA6DP": mtAtmHsimA6DP,
       "mtAtmVHsimA6DP": mtAtmVHsimA6DP,
       "mtAtmStandAlone": mtAtmStandAlone,
       "mt2A000": mt2A000,
       "mt2A000R": mt2A000R,
       "mtAtmNetworkModule": mtAtmNetworkModule,
       "mtIOM21p04": mtIOM21p04,
       "mtIOM22p04": mtIOM22p04,
       "mtIOM29p04IR": mtIOM29p04IR,
       "mtIOM29p04LR": mtIOM29p04LR,
       "mtIOM31p01": mtIOM31p01,
       "mtIOM39p01": mtIOM39p01,
       "mtIOM39p01LR": mtIOM39p01LR,
       "mtIOM67p04": mtIOM67p04,
       "mtIOM77p04": mtIOM77p04,
       "mtFPS": mtFPS,
       "mtFPSModules": mtFPSModules,
       "mt7C03": mt7C03,
       "mt7C04": mt7C04,
       "mt7X00": mt7X00,
       "mt7C04r": mt7C04r,
       "mtFpsEthernet": mtFpsEthernet,
       "mt7E03p24": mt7E03p24,
       "mt7E02p12": mt7E02p12,
       "mt7E02p24": mt7E02p24,
       "mt7E08p12": mt7E08p12,
       "mtFpsFDDI": mtFpsFDDI,
       "mt7F06p02": mt7F06p02,
       "mtFpsTR": mtFpsTR,
       "mt7T05p04": mt7T05p04,
       "mtFpsATM": mtFpsATM,
       "mt7A06p01": mt7A06p01,
       "mtFpsFastEthernet": mtFpsFastEthernet,
       "mt7H02p06": mt7H02p06,
       "mt7H02p12": mt7H02p12,
       "mt7H06p2": mt7H06p2,
       "mtCableModem": mtCableModem,
       "mtEthernetCableModem": mtEthernetCableModem,
       "mtMC23001pXE21": mtMC23001pXE21,
       "mtMC21001pE01": mtMC21001pE01,
       "mtWorkGroup": mtWorkGroup,
       "mtWorkGroupChassis": mtWorkGroupChassis,
       "mt6C105": mt6C105,
       "mt6C110": mt6C110,
       "mtSmartSwitchRouter8": mtSmartSwitchRouter8,
       "mtSmartSwitchRouter16": mtSmartSwitchRouter16,
       "mtSmartSwitchRouter32": mtSmartSwitchRouter32,
       "mt6C107": mt6C107,
       "mtWorkGroupEthernet": mtWorkGroupEthernet,
       "mt6E102p24": mt6E102p24,
       "mt6E122p26": mt6E122p26,
       "mt6E132p25": mt6E132p25,
       "mt6H122p08": mt6H122p08,
       "mt6E123p50": mt6E123p50,
       "mt6E133p49": mt6E133p49,
       "mt6E123p26": mt6E123p26,
       "mt6E133p25": mt6E133p25,
       "mt6H133p49": mt6H133p49,
       "mt6H123p50": mt6H123p50,
       "mt6M146p04": mt6M146p04,
       "mt6E128p26": mt6E128p26,
       "mt6E138p25": mt6E138p25,
       "mt6E129p26": mt6E129p26,
       "mt6E139p25": mt6E139p25,
       "mt6H128p08": mt6H128p08,
       "mt6H129p08": mt6H129p08,
       "mt6H122p16": mt6H122p16,
       "mt6H133p37": mt6H133p37,
       "mt6H202p24": mt6H202p24,
       "mt6H252p17": mt6H252p17,
       "mt6M256p04": mt6M256p04,
       "mt6E233p49": mt6E233p49,
       "mt6H258p17": mt6H258p17,
       "mt6H203p24": mt6H203p24,
       "mt6H253p13": mt6H253p13,
       "mt6H259p17": mt6H259p17,
       "mt6H262p18": mt6H262p18,
       "mt6H202p48": mt6H202p48,
       "mt6E253p49": mt6E253p49,
       "mt6H203p48": mt6H203p48,
       "mt6H303p48": mt6H303p48,
       "mt6H302p48": mt6H302p48,
       "mt6H352p25": mt6H352p25,
       "mt6G306p06": mt6G306p06,
       "mtWorkGroupATM": mtWorkGroupATM,
       "mt6A000": mt6A000,
       "mt6A000F": mt6A000F,
       "mtMMACPlus": mtMMACPlus,
       "mtMMACPlusEnclose": mtMMACPlusEnclose,
       "mt9C114": mt9C114,
       "mt9C106": mt9C106,
       "mtMMACEM": mtMMACEM,
       "mt9C300p01": mt9C300p01,
       "mt9C306p01": mt9C306p01,
       "mtMMACPU": mtMMACPU,
       "mt9C214p1": mt9C214p1,
       "mt9C214p2": mt9C214p2,
       "mt9C206p1": mt9C206p1,
       "mt9C214p3": mt9C214p3,
       "mtMMACPlusFNBSingle": mtMMACPlusFNBSingle,
       "mt9E133p36": mt9E133p36,
       "mt9E122p24": mt9E122p24,
       "mt9E138p36": mt9E138p36,
       "mt9F116p01": mt9F116p01,
       "mt9F106p02": mt9F106p02,
       "mt9W116p04": mt9W116p04,
       "mt9T122p24": mt9T122p24,
       "mt9E132p15": mt9E132p15,
       "mt9T122p08": mt9T122p08,
       "mt9A128p01": mt9A128p01,
       "mt9E106p06": mt9E106p06,
       "mt9E138p12": mt9E138p12,
       "mt9F206p02": mt9F206p02,
       "mt9A126p01": mt9A126p01,
       "mt9T112p24": mt9T112p24,
       "mt9T162p06": mt9T162p06,
       "mt9T125p08": mt9T125p08,
       "mt9T125p24": mt9T125p24,
       "mt9E132p15s": mt9E132p15s,
       "mt9E133p36s": mt9E133p36s,
       "mt9E138p36s": mt9E138p36s,
       "mt9E138p12s": mt9E138p12s,
       "mtMMACPlusFNBDual": mtMMACPlusFNBDual,
       "mt9F122p12": mt9F122p12,
       "mt9F120p08": mt9F120p08,
       "mt9F125p08": mt9F125p08,
       "mt9F241P12": mt9F241P12,
       "mt9F240p08": mt9F240p08,
       "mtMMACPlusINBSingle": mtMMACPlusINBSingle,
       "mt9E312p12": mt9E312p12,
       "mt9E313p12": mt9E313p12,
       "mt9E318p12": mt9E318p12,
       "mt9F310p02": mt9F310p02,
       "mt9A426p02": mt9A426p02,
       "mt9F315p02": mt9F315p02,
       "mt9F426p2": mt9F426p2,
       "mt9E423p24": mt9E423p24,
       "mt9H422p12": mt9H422p12,
       "mt9E428p12": mt9E428p12,
       "mt9E428p36": mt9E428p36,
       "mt9E429p12": mt9E429p12,
       "mt9E429p36": mt9E429p36,
       "mt9F426p03": mt9F426p03,
       "mt9H421p12": mt9H421p12,
       "mt9E423p36": mt9E423p36,
       "mt9H429p12": mt9H429p12,
       "mt9T425p16": mt9T425p16,
       "mt9T425p24": mt9T425p24,
       "mt9A426p01": mt9A426p01,
       "mt9G426p02": mt9G426p02,
       "mt9H423p28": mt9H423p28,
       "mt9H423p26": mt9H423p26,
       "mt9G421p02": mt9G421p02,
       "mt9M426p02": mt9M426p02,
       "mt9D422p16": mt9D422p16,
       "mt9G429p02": mt9G429p02,
       "mt9T428p16": mt9T428p16,
       "mt9T427p16": mt9T427p16,
       "mt3PartyFnbSingle": mt3PartyFnbSingle,
       "mt9W111p08": mt9W111p08,
       "mt9T101p04": mt9T101p04,
       "mt9F106p01": mt9F106p01,
       "mt9F206p01": mt9F206p01,
       "mt9T201p04": mt9T201p04,
       "mt9W211p08": mt9W211p08,
       "mt9A221p01": mt9A221p01,
       "mt9A222p01": mt9A222p01,
       "mt9A229p01": mt9A229p01,
       "mtMMACPOther": mtMMACPOther,
       "mt9A000": mt9A000,
       "mt9P120": mt9P120,
       "mt9P110": mt9P110,
       "mt9X000p16": mt9X000p16,
       "mt9P110mhz90": mt9P110mhz90,
       "mt9A656p04": mt9A656p04,
       "mt9A600p04": mt9A600p04,
       "mt9A686p04": mt9A686p04,
       "mt9A100": mt9A100,
       "mtMMACPlusNortel": mtMMACPlusNortel,
       "mt9N050": mt9N050,
       "mtMMACPlusINBDual": mtMMACPlusINBDual,
       "mt9H532p18": mt9H532p18,
       "mt9H531p18": mt9H531p18,
       "mt9H539p18": mt9H539p18,
       "mt9H532p17": mt9H532p17,
       "mt9H531p17": mt9H531p17,
       "mt9H539p17": mt9H539p17,
       "mt9G536p04": mt9G536p04,
       "mt9H532p24": mt9H532p24,
       "mt9H531p24": mt9H531p24,
       "mt9H539p24": mt9H539p24,
       "mt9M546p04": mt9M546p04,
       "mt9H533p24": mt9H533p24,
       "mt9H533p48": mt9H533p48,
       "mt9E531p24": mt9E531p24,
       "mtSSR": mtSSR,
       "mtSSRStandAlone": mtSSRStandAlone,
       "mtSSR2B": mtSSR2B,
       "mtSSR2BPS": mtSSR2BPS,
       "mtSSR2100": mtSSR2100,
       "mtSSR510": mtSSR510,
       "mtSSR520": mtSSR520,
       "mtSSR600S": mtSSR600S,
       "mtSSR600D": mtSSR600D,
       "mtSSR710T1": mtSSR710T1,
       "mtSSR710E1": mtSSR710E1,
       "mtSSR720": mtSSR720,
       "mtSSR2Expansion": mtSSR2Expansion,
       "mtSSR2SX": mtSSR2SX,
       "mtSSR2LX": mtSSR2LX,
       "mtSSR2TX": mtSSR2TX,
       "mtSSR2FX": mtSSR2FX,
       "mtSSR2SER": mtSSR2SER,
       "mtSSR2SERC": mtSSR2SERC,
       "mtSSR2SERCE": mtSSR2SERCE,
       "mtIA1100": mtIA1100,
       "mtIA1200": mtIA1200,
       "mtSSR8Expansion": mtSSR8Expansion,
       "mtSSRHTX12p08": mtSSRHTX12p08,
       "mtSSRHTX22p08": mtSSRHTX22p08,
       "mtSSRHFX11p08": mtSSRHFX11p08,
       "mtSSRHFX21p08": mtSSRHFX21p08,
       "mtSSRGSX11p02": mtSSRGSX11p02,
       "mtSSRGSX21p02": mtSSRGSX21p02,
       "mtSSRGLX19p02": mtSSRGLX19p02,
       "mtSSRGLX29p02": mtSSRGLX29p02,
       "mtSSRGLX70p01": mtSSRGLX70p01,
       "mtSSRHFX29p08": mtSSRHFX29p08,
       "mtSSRSERCp04": mtSSRSERCp04,
       "mtSSRSERCEp04": mtSSRSERCEp04,
       "mtSSRHSSIp02": mtSSRHSSIp02,
       "mtSSR6Expansion": mtSSR6Expansion,
       "mt6SSRM-02": mt6SSRM_02,
       "mt6SSRLC-LX": mt6SSRLC_LX,
       "mt6SSRLC-TX": mt6SSRLC_TX,
       "mt6SSRLC-FX": mt6SSRLC_FX,
       "mt6SSRLC-SX": mt6SSRLC_SX,
       "mt6SSRLC-SER": mt6SSRLC_SER,
       "mt6SSRLC-SERC": mt6SSRLC_SERC,
       "mt6SSRLC-SERCE": mt6SSRLC_SERCE,
       "mt6SSRLC-LX70": mt6SSRLC_LX70,
       "mtHSIMSSR": mtHSIMSSR,
       "mtHSIMSSR600": mtHSIMSSR600,
       "ctIfTypes": ctIfTypes,
       "ctIfBackPlane": ctIfBackPlane,
       "ctIfNonFNB": ctIfNonFNB,
       "ctIfFNB": ctIfFNB,
       "ctIfFrontPanel": ctIfFrontPanel,
       "ctHsimInterconnect": ctHsimInterconnect,
       "ctResourceType": ctResourceType,
       "ctFDDIFnbBP": ctFDDIFnbBP,
       "ctFDDIFnbBP1": ctFDDIFnbBP1,
       "ctFDDIFnbBP2": ctFDDIFnbBP2,
       "ctSMB1": ctSMB1,
       "ctSMB10": ctSMB10,
       "ctFrontPanel": ctFrontPanel,
       "ctFDDIFrontPanel": ctFDDIFrontPanel,
       "ctFDDIFrontPanel1": ctFDDIFrontPanel1,
       "ctFDDIFrontPanel2": ctFDDIFrontPanel2,
       "ctFDDIFrontPanel3": ctFDDIFrontPanel3,
       "ctFDDIFrontPanel4": ctFDDIFrontPanel4,
       "ctFDDIFrontPanel5": ctFDDIFrontPanel5,
       "ctFDDIFrontPanel6": ctFDDIFrontPanel6,
       "ctFDDIFrontPanel7": ctFDDIFrontPanel7,
       "ctFDDIFrontPanel8": ctFDDIFrontPanel8,
       "ctFDDIFrontPanel9": ctFDDIFrontPanel9,
       "ctFDDIFrontPanel10": ctFDDIFrontPanel10,
       "ctFDDIFrontPanel11": ctFDDIFrontPanel11,
       "ctFDDIFrontPanel12": ctFDDIFrontPanel12,
       "ctEthernetFrontPanel": ctEthernetFrontPanel,
       "ctFrontPanelATM": ctFrontPanelATM,
       "ctFrontPanelATM1": ctFrontPanelATM1,
       "ctFrontPanelATM2": ctFrontPanelATM2,
       "ctFrontPanelTokenRing": ctFrontPanelTokenRing,
       "ctFrontPanelWAN": ctFrontPanelWAN,
       "ctFrontPanelComport": ctFrontPanelComport,
       "ctFrontPanelComport1": ctFrontPanelComport1,
       "ctFrontPanelComport2": ctFrontPanelComport2,
       "ctINB1": ctINB1,
       "ctINB2": ctINB2,
       "ctHostPort": ctHostPort,
       "ctCTM": ctCTM,
       "ctWorkGroupBPport": ctWorkGroupBPport,
       "ctWorkGroupBPport1": ctWorkGroupBPport1,
       "ctWorkGroupBPport2": ctWorkGroupBPport2,
       "ctWorkGroupBPport3": ctWorkGroupBPport3,
       "ctWorkGroupBPport4": ctWorkGroupBPport4,
       "ctWorkGroupBPport5": ctWorkGroupBPport5,
       "ctATMVirtual": ctATMVirtual,
       "ctATMVirtualLec": ctATMVirtualLec,
       "ctATMVirtualPvc": ctATMVirtualPvc,
       "ctATMVirtualClip": ctATMVirtualClip,
       "ctATMVirtualSvc": ctATMVirtualSvc,
       "ctIfSpecific": ctIfSpecific,
       "ctSmartTrunkVirtual": ctSmartTrunkVirtual,
       "ctMMACPlusBPport": ctMMACPlusBPport,
       "ctMMACPlusBPport1": ctMMACPlusBPport1,
       "ctMMACPlusBPport2": ctMMACPlusBPport2,
       "ctMMACPlusBPport3": ctMMACPlusBPport3,
       "ctMMACPlusBPport4": ctMMACPlusBPport4,
       "ctMMACPlusBPport5": ctMMACPlusBPport5,
       "ctMMACPlusBPport6": ctMMACPlusBPport6,
       "ctMMACPlusBPport7": ctMMACPlusBPport7,
       "ctMMACPlusBPport8": ctMMACPlusBPport8,
       "ctMMACPlusBPport9": ctMMACPlusBPport9,
       "ctMMACPlusBPport10": ctMMACPlusBPport10,
       "ctMMACPlusBPport11": ctMMACPlusBPport11,
       "ctMMACPlusBPport12": ctMMACPlusBPport12,
       "ctMMACPlusBPport13": ctMMACPlusBPport13,
       "ctMMACPlusBPport14": ctMMACPlusBPport14,
       "ctSFPSTypes": ctSFPSTypes,
       "ctVLANS": ctVLANS,
       "ctLaneServices": ctLaneServices,
       "lsSFpSMARTLANE": lsSFpSMARTLANE,
       "v2conformance": v2conformance,
       "trapDefinitions": trapDefinitions,
       "ctTrapsV1": ctTrapsV1}
)
