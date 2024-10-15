# SNMP MIB module (PACKETFRONT-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKETFRONT-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:06 2024
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

(pfModules,
 pfProduct) = mibBuilder.importSymbols(
    "PACKETFRONT-SMI",
    "pfModules",
    "pfProduct")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pfProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 5, 2)
)
pfProductsMIB.setRevisions(
        ("2010-05-17 14:10",
         "2009-04-14 12:29",
         "2009-03-23 10:53",
         "2007-05-14 12:38",
         "2006-01-25 13:30",
         "2004-10-20 14:34",
         "2003-11-04 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asr_ObjectIdentity = ObjectIdentity
asr = _Asr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1)
)
if mibBuilder.loadTexts:
    asr.setStatus("current")
_Asr4108C_ObjectIdentity = ObjectIdentity
asr4108C = _Asr4108C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 1)
)
_Asr4116C_ObjectIdentity = ObjectIdentity
asr4116C = _Asr4116C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 2)
)
_Asr4124C_ObjectIdentity = ObjectIdentity
asr4124C = _Asr4124C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 3)
)
_Asr4208FM_ObjectIdentity = ObjectIdentity
asr4208FM = _Asr4208FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 4)
)
_Asr4216FM_ObjectIdentity = ObjectIdentity
asr4216FM = _Asr4216FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 5)
)
_Asr4224FM_ObjectIdentity = ObjectIdentity
asr4224FM = _Asr4224FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 6)
)
_Asr4308FV_ObjectIdentity = ObjectIdentity
asr4308FV = _Asr4308FV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 7)
)
_Asr4316FV_ObjectIdentity = ObjectIdentity
asr4316FV = _Asr4316FV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 8)
)
_Asr4324FV_ObjectIdentity = ObjectIdentity
asr4324FV = _Asr4324FV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 9)
)
_Asr4408SFV_ObjectIdentity = ObjectIdentity
asr4408SFV = _Asr4408SFV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 10)
)
_Asr4416SFV_ObjectIdentity = ObjectIdentity
asr4416SFV = _Asr4416SFV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 11)
)
_Asr4424SFV_ObjectIdentity = ObjectIdentity
asr4424SFV = _Asr4424SFV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 12)
)
_Asr4508SFM_ObjectIdentity = ObjectIdentity
asr4508SFM = _Asr4508SFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 13)
)
_Asr4516SFM_ObjectIdentity = ObjectIdentity
asr4516SFM = _Asr4516SFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 14)
)
_Asr4524SFM_ObjectIdentity = ObjectIdentity
asr4524SFM = _Asr4524SFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 15)
)
_Asr4608SFS_ObjectIdentity = ObjectIdentity
asr4608SFS = _Asr4608SFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 16)
)
_Asr4616SFS_ObjectIdentity = ObjectIdentity
asr4616SFS = _Asr4616SFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 17)
)
_Asr4624SFS_ObjectIdentity = ObjectIdentity
asr4624SFS = _Asr4624SFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 18)
)
_Asr3108VDSL_ObjectIdentity = ObjectIdentity
asr3108VDSL = _Asr3108VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 19)
)
_Asr3116VDSL_ObjectIdentity = ObjectIdentity
asr3116VDSL = _Asr3116VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 20)
)
_Asr3124VDSL_ObjectIdentity = ObjectIdentity
asr3124VDSL = _Asr3124VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 21)
)
_Asr3208VDSL_ObjectIdentity = ObjectIdentity
asr3208VDSL = _Asr3208VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 22)
)
_Asr3216VDSL_ObjectIdentity = ObjectIdentity
asr3216VDSL = _Asr3216VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 23)
)
_Asr3224VDSL_ObjectIdentity = ObjectIdentity
asr3224VDSL = _Asr3224VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 24)
)
_Asr3308VDSL_ObjectIdentity = ObjectIdentity
asr3308VDSL = _Asr3308VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 25)
)
_Asr3316VDSL_ObjectIdentity = ObjectIdentity
asr3316VDSL = _Asr3316VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 26)
)
_Asr3324VDSL_ObjectIdentity = ObjectIdentity
asr3324VDSL = _Asr3324VDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 27)
)
_Asr4708SFL_ObjectIdentity = ObjectIdentity
asr4708SFL = _Asr4708SFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 28)
)
_Asr4716SFL_ObjectIdentity = ObjectIdentity
asr4716SFL = _Asr4716SFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 29)
)
_Asr4724SFL_ObjectIdentity = ObjectIdentity
asr4724SFL = _Asr4724SFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 30)
)
_Asr4108Cco_ObjectIdentity = ObjectIdentity
asr4108Cco = _Asr4108Cco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 31)
)
_Asr4116Cco_ObjectIdentity = ObjectIdentity
asr4116Cco = _Asr4116Cco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 32)
)
_Asr4124Cco_ObjectIdentity = ObjectIdentity
asr4124Cco = _Asr4124Cco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 33)
)
_Asr4208FMco_ObjectIdentity = ObjectIdentity
asr4208FMco = _Asr4208FMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 34)
)
_Asr4216FMco_ObjectIdentity = ObjectIdentity
asr4216FMco = _Asr4216FMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 35)
)
_Asr4224FMco_ObjectIdentity = ObjectIdentity
asr4224FMco = _Asr4224FMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 36)
)
_Asr4308FVco_ObjectIdentity = ObjectIdentity
asr4308FVco = _Asr4308FVco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 37)
)
_Asr4316FVco_ObjectIdentity = ObjectIdentity
asr4316FVco = _Asr4316FVco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 38)
)
_Asr4324FVco_ObjectIdentity = ObjectIdentity
asr4324FVco = _Asr4324FVco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 39)
)
_Asr4508SFMco_ObjectIdentity = ObjectIdentity
asr4508SFMco = _Asr4508SFMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 40)
)
_Asr4516SFMco_ObjectIdentity = ObjectIdentity
asr4516SFMco = _Asr4516SFMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 41)
)
_Asr4524SFMco_ObjectIdentity = ObjectIdentity
asr4524SFMco = _Asr4524SFMco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 42)
)
_Asr4608SFSco_ObjectIdentity = ObjectIdentity
asr4608SFSco = _Asr4608SFSco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 43)
)
_Asr4616SFSco_ObjectIdentity = ObjectIdentity
asr4616SFSco = _Asr4616SFSco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 44)
)
_Asr4624SFSco_ObjectIdentity = ObjectIdentity
asr4624SFSco = _Asr4624SFSco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 45)
)
_Asr4708SFLco_ObjectIdentity = ObjectIdentity
asr4708SFLco = _Asr4708SFLco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 46)
)
_Asr4716SFLco_ObjectIdentity = ObjectIdentity
asr4716SFLco = _Asr4716SFLco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 47)
)
_Asr4724SFLco_ObjectIdentity = ObjectIdentity
asr4724SFLco = _Asr4724SFLco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 48)
)
_Asr10132co_ObjectIdentity = ObjectIdentity
asr10132co = _Asr10132co_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 49)
)
_Asr5124Cacco_ObjectIdentity = ObjectIdentity
asr5124Cacco = _Asr5124Cacco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 50)
)
_Asr5124Cdcco_ObjectIdentity = ObjectIdentity
asr5124Cdcco = _Asr5124Cdcco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 51)
)
_Asr5224FMacco_ObjectIdentity = ObjectIdentity
asr5224FMacco = _Asr5224FMacco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 52)
)
_Asr5224FMdcco_ObjectIdentity = ObjectIdentity
asr5224FMdcco = _Asr5224FMdcco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 53)
)
_Asr5624FSacco_ObjectIdentity = ObjectIdentity
asr5624FSacco = _Asr5624FSacco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 54)
)
_Asr5624FSdcco_ObjectIdentity = ObjectIdentity
asr5624FSdcco = _Asr5624FSdcco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 55)
)
_Asr5724FLacco_ObjectIdentity = ObjectIdentity
asr5724FLacco = _Asr5724FLacco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 56)
)
_Asr5724FLdcco_ObjectIdentity = ObjectIdentity
asr5724FLdcco = _Asr5724FLdcco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 1, 57)
)
_Ipd_ObjectIdentity = ObjectIdentity
ipd = _Ipd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 2)
)
if mibBuilder.loadTexts:
    ipd.setStatus("current")
_Ipd1116C_ObjectIdentity = ObjectIdentity
ipd1116C = _Ipd1116C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 2, 1)
)
_Drg_ObjectIdentity = ObjectIdentity
drg = _Drg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3)
)
if mibBuilder.loadTexts:
    drg.setStatus("current")
_Drg100_ObjectIdentity = ObjectIdentity
drg100 = _Drg100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 1)
)
_Drg340_ObjectIdentity = ObjectIdentity
drg340 = _Drg340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 2)
)
_Drg560_ObjectIdentity = ObjectIdentity
drg560 = _Drg560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 3)
)
_Drg580_ObjectIdentity = ObjectIdentity
drg580 = _Drg580_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 4)
)
_Evm01_ObjectIdentity = ObjectIdentity
evm01 = _Evm01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 5)
)
_Drg600Access_ObjectIdentity = ObjectIdentity
drg600Access = _Drg600Access_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 6)
)
_Drg600Telephony_ObjectIdentity = ObjectIdentity
drg600Telephony = _Drg600Telephony_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 7)
)
_Drg615_ObjectIdentity = ObjectIdentity
drg615 = _Drg615_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 7)
)
_Drg600Wifi_ObjectIdentity = ObjectIdentity
drg600Wifi = _Drg600Wifi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 8)
)
_Drg635_ObjectIdentity = ObjectIdentity
drg635 = _Drg635_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 8)
)
_Drg701_ObjectIdentity = ObjectIdentity
drg701 = _Drg701_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 9)
)
_Drg702_ObjectIdentity = ObjectIdentity
drg702 = _Drg702_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 10)
)
_Drg703_ObjectIdentity = ObjectIdentity
drg703 = _Drg703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 11)
)
_Drg711_ObjectIdentity = ObjectIdentity
drg711 = _Drg711_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 12)
)
_Drg712_ObjectIdentity = ObjectIdentity
drg712 = _Drg712_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 13)
)
_Drg714_ObjectIdentity = ObjectIdentity
drg714 = _Drg714_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 14)
)
_Drg716_ObjectIdentity = ObjectIdentity
drg716 = _Drg716_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 15)
)
_Drg718_ObjectIdentity = ObjectIdentity
drg718 = _Drg718_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 16)
)
_Drg719_ObjectIdentity = ObjectIdentity
drg719 = _Drg719_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 3, 17)
)
_Se_ObjectIdentity = ObjectIdentity
se = _Se_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 4)
)
if mibBuilder.loadTexts:
    se.setStatus("current")
_Ms_ObjectIdentity = ObjectIdentity
ms = _Ms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5)
)
if mibBuilder.loadTexts:
    ms.setStatus("current")
_Ms2016ac_ObjectIdentity = ObjectIdentity
ms2016ac = _Ms2016ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 1)
)
_Ms2016dc_ObjectIdentity = ObjectIdentity
ms2016dc = _Ms2016dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 2)
)
_Ms3028ac_ObjectIdentity = ObjectIdentity
ms3028ac = _Ms3028ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 3)
)
_Ms3028dc_ObjectIdentity = ObjectIdentity
ms3028dc = _Ms3028dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 4)
)
_Ms3128ac_ObjectIdentity = ObjectIdentity
ms3128ac = _Ms3128ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 5)
)
_Ms3128dc_ObjectIdentity = ObjectIdentity
ms3128dc = _Ms3128dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1, 5, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETFRONT-PRODUCTS-MIB",
    **{"asr": asr,
       "asr4108C": asr4108C,
       "asr4116C": asr4116C,
       "asr4124C": asr4124C,
       "asr4208FM": asr4208FM,
       "asr4216FM": asr4216FM,
       "asr4224FM": asr4224FM,
       "asr4308FV": asr4308FV,
       "asr4316FV": asr4316FV,
       "asr4324FV": asr4324FV,
       "asr4408SFV": asr4408SFV,
       "asr4416SFV": asr4416SFV,
       "asr4424SFV": asr4424SFV,
       "asr4508SFM": asr4508SFM,
       "asr4516SFM": asr4516SFM,
       "asr4524SFM": asr4524SFM,
       "asr4608SFS": asr4608SFS,
       "asr4616SFS": asr4616SFS,
       "asr4624SFS": asr4624SFS,
       "asr3108VDSL": asr3108VDSL,
       "asr3116VDSL": asr3116VDSL,
       "asr3124VDSL": asr3124VDSL,
       "asr3208VDSL": asr3208VDSL,
       "asr3216VDSL": asr3216VDSL,
       "asr3224VDSL": asr3224VDSL,
       "asr3308VDSL": asr3308VDSL,
       "asr3316VDSL": asr3316VDSL,
       "asr3324VDSL": asr3324VDSL,
       "asr4708SFL": asr4708SFL,
       "asr4716SFL": asr4716SFL,
       "asr4724SFL": asr4724SFL,
       "asr4108Cco": asr4108Cco,
       "asr4116Cco": asr4116Cco,
       "asr4124Cco": asr4124Cco,
       "asr4208FMco": asr4208FMco,
       "asr4216FMco": asr4216FMco,
       "asr4224FMco": asr4224FMco,
       "asr4308FVco": asr4308FVco,
       "asr4316FVco": asr4316FVco,
       "asr4324FVco": asr4324FVco,
       "asr4508SFMco": asr4508SFMco,
       "asr4516SFMco": asr4516SFMco,
       "asr4524SFMco": asr4524SFMco,
       "asr4608SFSco": asr4608SFSco,
       "asr4616SFSco": asr4616SFSco,
       "asr4624SFSco": asr4624SFSco,
       "asr4708SFLco": asr4708SFLco,
       "asr4716SFLco": asr4716SFLco,
       "asr4724SFLco": asr4724SFLco,
       "asr10132co": asr10132co,
       "asr5124Cacco": asr5124Cacco,
       "asr5124Cdcco": asr5124Cdcco,
       "asr5224FMacco": asr5224FMacco,
       "asr5224FMdcco": asr5224FMdcco,
       "asr5624FSacco": asr5624FSacco,
       "asr5624FSdcco": asr5624FSdcco,
       "asr5724FLacco": asr5724FLacco,
       "asr5724FLdcco": asr5724FLdcco,
       "ipd": ipd,
       "ipd1116C": ipd1116C,
       "drg": drg,
       "drg100": drg100,
       "drg340": drg340,
       "drg560": drg560,
       "drg580": drg580,
       "evm01": evm01,
       "drg600Access": drg600Access,
       "drg600Telephony": drg600Telephony,
       "drg615": drg615,
       "drg600Wifi": drg600Wifi,
       "drg635": drg635,
       "drg701": drg701,
       "drg702": drg702,
       "drg703": drg703,
       "drg711": drg711,
       "drg712": drg712,
       "drg714": drg714,
       "drg716": drg716,
       "drg718": drg718,
       "drg719": drg719,
       "se": se,
       "ms": ms,
       "ms2016ac": ms2016ac,
       "ms2016dc": ms2016dc,
       "ms3028ac": ms3028ac,
       "ms3028dc": ms3028dc,
       "ms3128ac": ms3128ac,
       "ms3128dc": ms3128dc,
       "pfProductsMIB": pfProductsMIB}
)
