# SNMP MIB module (DATACOM-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DATACOM-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:15 2024
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

(datacomAccessDevices,
 datacomManagementCards,
 datacomModems,
 datacomModules) = mibBuilder.importSymbols(
    "DATACOM-SMI",
    "datacomAccessDevices",
    "datacomManagementCards",
    "datacomModems",
    "datacomModules")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DatacomRegistrationModule_ObjectIdentity = ObjectIdentity
datacomRegistrationModule = _DatacomRegistrationModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 1, 2)
)
_DatacomModemManagCardDMG20_ObjectIdentity = ObjectIdentity
datacomModemManagCardDMG20 = _DatacomModemManagCardDMG20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 1)
)
_DatacomDm705ManagCard_ObjectIdentity = ObjectIdentity
datacomDm705ManagCard = _DatacomDm705ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 3)
)
_DatacomDm16E1ManagCard_ObjectIdentity = ObjectIdentity
datacomDm16E1ManagCard = _DatacomDm16E1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 4)
)
_DatacomDm4E1ManagCard_ObjectIdentity = ObjectIdentity
datacomDm4E1ManagCard = _DatacomDm4E1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 5)
)
_DatacomDm706CManagCard_ObjectIdentity = ObjectIdentity
datacomDm706CManagCard = _DatacomDm706CManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 6)
)
_DatacomDmSTM1ManagCard_ObjectIdentity = ObjectIdentity
datacomDmSTM1ManagCard = _DatacomDmSTM1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 7)
)
_DatacomDm705CPU64ManagCard_ObjectIdentity = ObjectIdentity
datacomDm705CPU64ManagCard = _DatacomDm705CPU64ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 8)
)
_DatacomDm706CIPmuxE1RouterManagCard_ObjectIdentity = ObjectIdentity
datacomDm706CIPmuxE1RouterManagCard = _DatacomDm706CIPmuxE1RouterManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 9)
)
_DatacomDm706CIPmuxMultiPortRouterManagCard_ObjectIdentity = ObjectIdentity
datacomDm706CIPmuxMultiPortRouterManagCard = _DatacomDm706CIPmuxMultiPortRouterManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 10)
)
_DatacomDm706CMultiPortRouterManagCard_ObjectIdentity = ObjectIdentity
datacomDm706CMultiPortRouterManagCard = _DatacomDm706CMultiPortRouterManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 11)
)
_DatacomDm706CE1RouterManagCard_ObjectIdentity = ObjectIdentity
datacomDm706CE1RouterManagCard = _DatacomDm706CE1RouterManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 12)
)
_DatacomDmSwitch3224F1ManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch3224F1ManagCard = _DatacomDmSwitch3224F1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 13)
)
_DatacomDm300_8E1ManagCard_ObjectIdentity = ObjectIdentity
datacomDm300_8E1ManagCard = _DatacomDm300_8E1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 14)
)
_DatacomDm300_8E1BInvMuxManagCard_ObjectIdentity = ObjectIdentity
datacomDm300_8E1BInvMuxManagCard = _DatacomDm300_8E1BInvMuxManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 15)
)
_DatacomDm1801ManagCard_ObjectIdentity = ObjectIdentity
datacomDm1801ManagCard = _DatacomDm1801ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 16)
)
_DatacomDmSwitch3224F2ManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch3224F2ManagCard = _DatacomDmSwitch3224F2ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 17)
)
_DatacomDmSwitch3324F1ManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch3324F1ManagCard = _DatacomDmSwitch3324F1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 18)
)
_DatacomDmSwitch3324F2ManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch3324F2ManagCard = _DatacomDmSwitch3324F2ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 19)
)
_DatacomDm881ManagCard_ObjectIdentity = ObjectIdentity
datacomDm881ManagCard = _DatacomDm881ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 20)
)
_DatacomDm814ManagCard_ObjectIdentity = ObjectIdentity
datacomDm814ManagCard = _DatacomDm814ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 21)
)
_DatacomDm830ManagCard_ObjectIdentity = ObjectIdentity
datacomDm830ManagCard = _DatacomDm830ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 22)
)
_DatacomDm300_MCManagCard_ObjectIdentity = ObjectIdentity
datacomDm300_MCManagCard = _DatacomDm300_MCManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 23)
)
_DatacomDm300_8E1BManagCard_ObjectIdentity = ObjectIdentity
datacomDm300_8E1BManagCard = _DatacomDm300_8E1BManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 24)
)
_DatacomDm991CRManagCard_ObjectIdentity = ObjectIdentity
datacomDm991CRManagCard = _DatacomDm991CRManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 25)
)
_DatacomDm705CPU128ManagCard_ObjectIdentity = ObjectIdentity
datacomDm705CPU128ManagCard = _DatacomDm705CPU128ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 26)
)
_DatacomDm880ManagCard_ObjectIdentity = ObjectIdentity
datacomDm880ManagCard = _DatacomDm880ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 27)
)
_DatacomDmSwitch3224F3ManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch3224F3ManagCard = _DatacomDmSwitch3224F3ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 28)
)
_DatacomDmSwitch3324F3ManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch3324F3ManagCard = _DatacomDmSwitch3324F3ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 29)
)
_DatacomDm4000Mpu192ManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Mpu192ManagCard = _DatacomDm4000Mpu192ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 30)
)
_DatacomDm4000Eth24GxManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth24GxManagCard = _DatacomDm4000Eth24GxManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 31)
)
_DatacomDmSwitch2204G1ManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch2204G1ManagCard = _DatacomDmSwitch2204G1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 32)
)
_DatacomDmSwitch2304G1ManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch2304G1ManagCard = _DatacomDmSwitch2304G1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 33)
)
_DatacomDm4000Eth12GxManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth12GxManagCard = _DatacomDm4000Eth12GxManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 34)
)
_DatacomDm4000Eth2x10GxManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth2x10GxManagCard = _DatacomDm4000Eth2x10GxManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 35)
)
_DatacomDm4000Eth1x10GxManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth1x10GxManagCard = _DatacomDm4000Eth1x10GxManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 36)
)
_DatacomDm4000Eth12Gx1x10GxManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth12Gx1x10GxManagCard = _DatacomDm4000Eth12Gx1x10GxManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 37)
)
_DatacomDm4000Eth48GtManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth48GtManagCard = _DatacomDm4000Eth48GtManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 38)
)
_DatacomDm4000Eth24GtManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth24GtManagCard = _DatacomDm4000Eth24GtManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 39)
)
_DatacomDm4000Mpu384ManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Mpu384ManagCard = _DatacomDm4000Mpu384ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 40)
)
_DatacomDm16E1InvMuxManagCard_ObjectIdentity = ObjectIdentity
datacomDm16E1InvMuxManagCard = _DatacomDm16E1InvMuxManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 41)
)
_DatacomDm4E1InvMuxManagCard_ObjectIdentity = ObjectIdentity
datacomDm4E1InvMuxManagCard = _DatacomDm4E1InvMuxManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 42)
)
_DatacomDm16E1sIIManagCard_ObjectIdentity = ObjectIdentity
datacomDm16E1sIIManagCard = _DatacomDm16E1sIIManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 43)
)
_DatacomDm4E1sIIManagCard_ObjectIdentity = ObjectIdentity
datacomDm4E1sIIManagCard = _DatacomDm4E1sIIManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 44)
)
_DatacomDm706CRManagCard_ObjectIdentity = ObjectIdentity
datacomDm706CRManagCard = _DatacomDm706CRManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 45)
)
_DatacomDm991CSManagCard_ObjectIdentity = ObjectIdentity
datacomDm991CSManagCard = _DatacomDm991CSManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 46)
)
_DatacomDm706CSManagCard_ObjectIdentity = ObjectIdentity
datacomDm706CSManagCard = _DatacomDm706CSManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 47)
)
_DatacomDm706EManagCard_ObjectIdentity = ObjectIdentity
datacomDm706EManagCard = _DatacomDm706EManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 48)
)
_DatacomDm706M1ManagCard_ObjectIdentity = ObjectIdentity
datacomDm706M1ManagCard = _DatacomDm706M1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 49)
)
_DatacomDm706M2ManagCard_ObjectIdentity = ObjectIdentity
datacomDm706M2ManagCard = _DatacomDm706M2ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 50)
)
_DatacomDm706M4ManagCard_ObjectIdentity = ObjectIdentity
datacomDm706M4ManagCard = _DatacomDm706M4ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 51)
)
_DatacomDm706Pabxm1ManagCard_ObjectIdentity = ObjectIdentity
datacomDm706Pabxm1ManagCard = _DatacomDm706Pabxm1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 52)
)
_DatacomDm706Pabxd1ManagCard_ObjectIdentity = ObjectIdentity
datacomDm706Pabxd1ManagCard = _DatacomDm706Pabxd1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 53)
)
_DatacomDm706Pabxm2ManagCard_ObjectIdentity = ObjectIdentity
datacomDm706Pabxm2ManagCard = _DatacomDm706Pabxm2ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 54)
)
_DatacomDm706Pabxd2ManagCard_ObjectIdentity = ObjectIdentity
datacomDm706Pabxd2ManagCard = _DatacomDm706Pabxd2ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 55)
)
_DatacomDm706PabxmManagCard_ObjectIdentity = ObjectIdentity
datacomDm706PabxmManagCard = _DatacomDm706PabxmManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 56)
)
_DatacomDm706PabxdManagCard_ObjectIdentity = ObjectIdentity
datacomDm706PabxdManagCard = _DatacomDm706PabxdManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 57)
)
_DatacomDm4000Eth24GXx2Xx10GXManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth24GXx2Xx10GXManagCard = _DatacomDm4000Eth24GXx2Xx10GXManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 58)
)
_DatacomDm4000Eth48GXManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth48GXManagCard = _DatacomDm4000Eth48GXManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 59)
)
_DatacomDm4000Eth4x10GXHSeriesManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth4x10GXHSeriesManagCard = _DatacomDm4000Eth4x10GXHSeriesManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 60)
)
_DatacomDmSwitch2104G1_EddManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch2104G1_EddManagCard = _DatacomDmSwitch2104G1_EddManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 61)
)
_DatacomDmSwitch2104G2_EddManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch2104G2_EddManagCard = _DatacomDmSwitch2104G2_EddManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 62)
)
_DatacomDm810ManagCard_ObjectIdentity = ObjectIdentity
datacomDm810ManagCard = _DatacomDm810ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 63)
)
_DatacomDm4000Eth24GX2x10GXHSeriesManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth24GX2x10GXHSeriesManagCard = _DatacomDm4000Eth24GX2x10GXHSeriesManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 64)
)
_DatacomDm4000Eth48GXHSeriesManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth48GXHSeriesManagCard = _DatacomDm4000Eth48GXHSeriesManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 65)
)
_DatacomDm4000Eth10GX32E1ManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth10GX32E1ManagCard = _DatacomDm4000Eth10GX32E1ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 66)
)
_DatacomDm4000EthSceqManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000EthSceqManagCard = _DatacomDm4000EthSceqManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 67)
)
_DatacomDm4000Eth24GXHSeriesManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth24GXHSeriesManagCard = _DatacomDm4000Eth24GXHSeriesManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 68)
)
_DatacomDm705CPU34ManagCard_ObjectIdentity = ObjectIdentity
datacomDm705CPU34ManagCard = _DatacomDm705CPU34ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 69)
)
_DatacomDm4650ManagCard_ObjectIdentity = ObjectIdentity
datacomDm4650ManagCard = _DatacomDm4650ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 70)
)
_DatacomPabxManagCard_ObjectIdentity = ObjectIdentity
datacomPabxManagCard = _DatacomPabxManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 71)
)
_DatacomDm4000Eth2x10GxHSeriesManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth2x10GxHSeriesManagCard = _DatacomDm4000Eth2x10GxHSeriesManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 72)
)
_DatacomDmSwitch2104G2Wri_EddManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch2104G2Wri_EddManagCard = _DatacomDmSwitch2104G2Wri_EddManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 73)
)
_DatacomDm706EhkManagCard_ObjectIdentity = ObjectIdentity
datacomDm706EhkManagCard = _DatacomDm706EhkManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 74)
)
_DatacomDmSwitch2104G1SeriesII_EddManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch2104G1SeriesII_EddManagCard = _DatacomDmSwitch2104G1SeriesII_EddManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 75)
)
_DatacomDm2106_2GX_ManagCard_ObjectIdentity = ObjectIdentity
datacomDm2106_2GX_ManagCard = _DatacomDm2106_2GX_ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 76)
)
_DatacomDm2106_4GX_ManagCard_ObjectIdentity = ObjectIdentity
datacomDm2106_4GX_ManagCard = _DatacomDm2106_4GX_ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 77)
)
_DatacomDm2106_4GXx8E1_EddManagCard_ObjectIdentity = ObjectIdentity
datacomDm2106_4GXx8E1_EddManagCard = _DatacomDm2106_4GXx8E1_EddManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 78)
)
_DatacomDmSwitch2104G2_EDDxE1_EddManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch2104G2_EDDxE1_EddManagCard = _DatacomDmSwitch2104G2_EDDxE1_EddManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 79)
)
_DatacomDmSwitch2104G1_EDDSeriesII_EddManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch2104G1_EDDSeriesII_EddManagCard = _DatacomDmSwitch2104G1_EDDSeriesII_EddManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 81)
)
_DatacomDmSwitch2104G2_EDDxE1SeriesII_EddManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch2104G2_EDDxE1SeriesII_EddManagCard = _DatacomDmSwitch2104G2_EDDxE1SeriesII_EddManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 82)
)
_DatacomDm4000Eth24GxLSeriesManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Eth24GxLSeriesManagCard = _DatacomDm4000Eth24GxLSeriesManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 83)
)
_DatacomDm4000Mpu512ManagCard_ObjectIdentity = ObjectIdentity
datacomDm4000Mpu512ManagCard = _DatacomDm4000Mpu512ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 84)
)
_DatacomDmSwitch2104G2S3Wri_EddManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitch2104G2S3Wri_EddManagCard = _DatacomDmSwitch2104G2S3Wri_EddManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 85)
)
_DatacomDm4100Eth24GXx4GXManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth24GXx4GXManagCard = _DatacomDm4100Eth24GXx4GXManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 86)
)
_DatacomDm4100Eth24GXx2XXManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth24GXx2XXManagCard = _DatacomDm4100Eth24GXx2XXManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 87)
)
_DatacomDm4100Eth24GXxSManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth24GXxSManagCard = _DatacomDm4100Eth24GXxSManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 88)
)
_DatacomDm4100Eth24GXx2XXxSManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth24GXx2XXxSManagCard = _DatacomDm4100Eth24GXx2XXxSManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 89)
)
_DatacomDm4100Eth24GXx4XXManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth24GXx4XXManagCard = _DatacomDm4100Eth24GXx4XXManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 90)
)
_DatacomDm4100Eth20GTx4GCManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth20GTx4GCManagCard = _DatacomDm4100Eth20GTx4GCManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 91)
)
_DatacomDm4100Eth20GTx4GCx2XXManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth20GTx4GCx2XXManagCard = _DatacomDm4100Eth20GTx4GCx2XXManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 92)
)
_DatacomDm4100Eth20GTx4GCxSManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth20GTx4GCxSManagCard = _DatacomDm4100Eth20GTx4GCxSManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 93)
)
_DatacomDm4100Eth20GTx4GCx2XXxSManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth20GTx4GCx2XXxSManagCard = _DatacomDm4100Eth20GTx4GCx2XXxSManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 94)
)
_DatacomDm4100Eth20GTx4GCx4XXManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth20GTx4GCx4XXManagCard = _DatacomDm4100Eth20GTx4GCx4XXManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 95)
)
_DatacomDmSwitchEddE1S2ManagCard_ObjectIdentity = ObjectIdentity
datacomDmSwitchEddE1S2ManagCard = _DatacomDmSwitchEddE1S2ManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 96)
)
_DatacomDm4100Eth44GPx4GCManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth44GPx4GCManagCard = _DatacomDm4100Eth44GPx4GCManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 97)
)
_DatacomDm4100Eth44GTx4GCx2XXManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth44GTx4GCx2XXManagCard = _DatacomDm4100Eth44GTx4GCx2XXManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 98)
)
_DatacomDm4100Eth44GTx4GCxSManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth44GTx4GCxSManagCard = _DatacomDm4100Eth44GTx4GCxSManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 99)
)
_DatacomDm4100Eth44GTx4GCx2XXxSManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth44GTx4GCx2XXxSManagCard = _DatacomDm4100Eth44GTx4GCx2XXxSManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 100)
)
_DatacomDm4100Eth44GTx4GCx4XXManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth44GTx4GCx4XXManagCard = _DatacomDm4100Eth44GTx4GCx4XXManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 101)
)
_DatacomDm4100Eth44GTx4GCx2XSManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth44GTx4GCx2XSManagCard = _DatacomDm4100Eth44GTx4GCx2XSManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 102)
)
_DatacomDm4100Eth44GTx4GCx2XSxSManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth44GTx4GCx2XSxSManagCard = _DatacomDm4100Eth44GTx4GCx2XSxSManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 103)
)
_DatacomDm4100Eth44GTx4GCx4XSManagCard_ObjectIdentity = ObjectIdentity
datacomDm4100Eth44GTx4GCx4XSManagCard = _DatacomDm4100Eth44GTx4GCx4XSManagCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2, 104)
)
_DmModemNotRegistered_ObjectIdentity = ObjectIdentity
dmModemNotRegistered = _DmModemNotRegistered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 1)
)
_DmModemDatacom_ObjectIdentity = ObjectIdentity
dmModemDatacom = _DmModemDatacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 2)
)
_DmModemParks_ObjectIdentity = ObjectIdentity
dmModemParks = _DmModemParks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3)
)
_DmModemParksUP128F2_ObjectIdentity = ObjectIdentity
dmModemParksUP128F2 = _DmModemParksUP128F2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 1)
)
_DmModemParksUP128F4_ObjectIdentity = ObjectIdentity
dmModemParksUP128F4 = _DmModemParksUP128F4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 2)
)
_DmModemParksUP64_ObjectIdentity = ObjectIdentity
dmModemParksUP64 = _DmModemParksUP64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 3)
)
_DmModemParksUP128_ObjectIdentity = ObjectIdentity
dmModemParksUP128 = _DmModemParksUP128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 4)
)
_DmModemParksUP256_ObjectIdentity = ObjectIdentity
dmModemParksUP256 = _DmModemParksUP256_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 5)
)
_DmModemParksUP384_ObjectIdentity = ObjectIdentity
dmModemParksUP384 = _DmModemParksUP384_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 6)
)
_DmModemParksUP512_ObjectIdentity = ObjectIdentity
dmModemParksUP512 = _DmModemParksUP512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 7)
)
_DmModemParksUP2048HDSL_ObjectIdentity = ObjectIdentity
dmModemParksUP2048HDSL = _DmModemParksUP2048HDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 8)
)
_DmModemParksUP3420_ObjectIdentity = ObjectIdentity
dmModemParksUP3420 = _DmModemParksUP3420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 9)
)
_DmModemParksDuo2_ObjectIdentity = ObjectIdentity
dmModemParksDuo2 = _DmModemParksDuo2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 10)
)
_DmModemParksUP64F2_ObjectIdentity = ObjectIdentity
dmModemParksUP64F2 = _DmModemParksUP64F2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 11)
)
_DmModemParksUP64F4_ObjectIdentity = ObjectIdentity
dmModemParksUP64F4 = _DmModemParksUP64F4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 12)
)
_DmModemParksPower512MSDSL_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL = _DmModemParksPower512MSDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 13)
)
_DmModemParksFiber4E1_ObjectIdentity = ObjectIdentity
dmModemParksFiber4E1 = _DmModemParksFiber4E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 14)
)
_DmModemParksPower512MSDSL_S2_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_S2 = _DmModemParksPower512MSDSL_S2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 15)
)
_DmModemParksPower2048MSDSL_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL = _DmModemParksPower2048MSDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 16)
)
_DmModemParksPower2048HDSL_ObjectIdentity = ObjectIdentity
dmModemParksPower2048HDSL = _DmModemParksPower2048HDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 17)
)
_DmModemParksFiber16E1_ObjectIdentity = ObjectIdentity
dmModemParksFiber16E1 = _DmModemParksFiber16E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 18)
)
_DmModemParksPower512MSDSL_2F_GVCE_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_2F_GVCE = _DmModemParksPower512MSDSL_2F_GVCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 19)
)
_DmModemParksPower512MSDSL_2F_GVC_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_2F_GVC = _DmModemParksPower512MSDSL_2F_GVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 20)
)
_DmModemParksPower512MSDSL_2F_GV_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_2F_GV = _DmModemParksPower512MSDSL_2F_GV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 21)
)
_DmModemParksPower512MSDSL_2F_VC_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_2F_VC = _DmModemParksPower512MSDSL_2F_VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 22)
)
_DmModemParksPower512MSDSL_2F_E_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_2F_E = _DmModemParksPower512MSDSL_2F_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 23)
)
_DmModemParksPower512MSDSL_4F_GVCE_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_4F_GVCE = _DmModemParksPower512MSDSL_4F_GVCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 24)
)
_DmModemParksPower512MSDSL_4F_GVC_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_4F_GVC = _DmModemParksPower512MSDSL_4F_GVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 25)
)
_DmModemParksPower512MSDSL_4F_GV_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_4F_GV = _DmModemParksPower512MSDSL_4F_GV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 26)
)
_DmModemParksPower512MSDSL_4F_VC_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_4F_VC = _DmModemParksPower512MSDSL_4F_VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 27)
)
_DmModemParksPower512MSDSL_4F_E_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_4F_E = _DmModemParksPower512MSDSL_4F_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 28)
)
_DmModemParksPower512MSDSL_2F_GV_DM_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_2F_GV_DM = _DmModemParksPower512MSDSL_2F_GV_DM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 29)
)
_DmModemParksPower512MSDSL_4F_GV_DM_ObjectIdentity = ObjectIdentity
dmModemParksPower512MSDSL_4F_GV_DM = _DmModemParksPower512MSDSL_4F_GV_DM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 30)
)
_DmModemParksPower2048MSDSL_2F_GVCE_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_2F_GVCE = _DmModemParksPower2048MSDSL_2F_GVCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 31)
)
_DmModemParksPower2048MSDSL_2F_GV_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_2F_GV = _DmModemParksPower2048MSDSL_2F_GV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 32)
)
_DmModemParksPower2048MSDSL_2F_GVC_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_2F_GVC = _DmModemParksPower2048MSDSL_2F_GVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 33)
)
_DmModemParksPower2048MSDSL_2F_VC_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_2F_VC = _DmModemParksPower2048MSDSL_2F_VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 34)
)
_DmModemParksPower2048MSDSL_2F_E_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_2F_E = _DmModemParksPower2048MSDSL_2F_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 35)
)
_DmModemParksPower2048MSDSL_4F_GVCE_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_4F_GVCE = _DmModemParksPower2048MSDSL_4F_GVCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 36)
)
_DmModemParksPower2048MSDSL_4F_GV_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_4F_GV = _DmModemParksPower2048MSDSL_4F_GV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 37)
)
_DmModemParksPower2048MSDSL_4F_GVC_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_4F_GVC = _DmModemParksPower2048MSDSL_4F_GVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 38)
)
_DmModemParksPower2048MSDSL_4F_VC_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_4F_VC = _DmModemParksPower2048MSDSL_4F_VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 39)
)
_DmModemParksPower2048MSDSL_4F_E_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_4F_E = _DmModemParksPower2048MSDSL_4F_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 40)
)
_DmModemParksPower2048MSDSL_2F_GV_DM_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_2F_GV_DM = _DmModemParksPower2048MSDSL_2F_GV_DM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 41)
)
_DmModemParksPower2048MSDSL_4F_GV_DM_ObjectIdentity = ObjectIdentity
dmModemParksPower2048MSDSL_4F_GV_DM = _DmModemParksPower2048MSDSL_4F_GV_DM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 3, 42)
)
_DmModemDigitel_ObjectIdentity = ObjectIdentity
dmModemDigitel = _DmModemDigitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4)
)
_DmModemDigitelDT32B_ObjectIdentity = ObjectIdentity
dmModemDigitelDT32B = _DmModemDigitelDT32B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 1)
)
_DmModemDigitelDT34_ObjectIdentity = ObjectIdentity
dmModemDigitelDT34 = _DmModemDigitelDT34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 2)
)
_DmModemDigitelDT64MI_ObjectIdentity = ObjectIdentity
dmModemDigitelDT64MI = _DmModemDigitelDT64MI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 3)
)
_DmModemDigitelDT128MI_ObjectIdentity = ObjectIdentity
dmModemDigitelDT128MI = _DmModemDigitelDT128MI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 4)
)
_DmModemDigitelDT256MI_ObjectIdentity = ObjectIdentity
dmModemDigitelDT256MI = _DmModemDigitelDT256MI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 5)
)
_DmModemDigitelDT2048_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048 = _DmModemDigitelDT2048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 6)
)
_DmModemDigitelDT2048_MFO_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_MFO = _DmModemDigitelDT2048_MFO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 7)
)
_DmModemDigitelTRANSEND_THREE_ObjectIdentity = ObjectIdentity
dmModemDigitelTRANSEND_THREE = _DmModemDigitelTRANSEND_THREE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 8)
)
_DmModemDigitelDT2048_HXR_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_HXR = _DmModemDigitelDT2048_HXR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 9)
)
_DmModemDigitelDT2048_HDSL_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_HDSL = _DmModemDigitelDT2048_HDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 10)
)
_DmModemDigitelDT64MIa_ObjectIdentity = ObjectIdentity
dmModemDigitelDT64MIa = _DmModemDigitelDT64MIa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 11)
)
_DmModemDigitelDT128MIa_ObjectIdentity = ObjectIdentity
dmModemDigitelDT128MIa = _DmModemDigitelDT128MIa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 12)
)
_DmModemDigitelDT256MIa_ObjectIdentity = ObjectIdentity
dmModemDigitelDT256MIa = _DmModemDigitelDT256MIa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 13)
)
_DmModemDigitelDT2048_HDSLex_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_HDSLex = _DmModemDigitelDT2048_HDSLex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 14)
)
_DmModemDigitelDT8192_4E1_ObjectIdentity = ObjectIdentity
dmModemDigitelDT8192_4E1 = _DmModemDigitelDT8192_4E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 15)
)
_DmModemDigitelDT8192_ObjectIdentity = ObjectIdentity
dmModemDigitelDT8192 = _DmModemDigitelDT8192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 16)
)
_DmModemDigitelDT8192BK_ObjectIdentity = ObjectIdentity
dmModemDigitelDT8192BK = _DmModemDigitelDT8192BK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 17)
)
_DmModemDigitelDT1024MI_ObjectIdentity = ObjectIdentity
dmModemDigitelDT1024MI = _DmModemDigitelDT1024MI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 18)
)
_DmModemDigitelDT2048_MX2_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_MX2 = _DmModemDigitelDT2048_MX2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 19)
)
_DmModemDigitelDT256_MIDX_ObjectIdentity = ObjectIdentity
dmModemDigitelDT256_MIDX = _DmModemDigitelDT256_MIDX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 20)
)
_DmModemDigitelDT2048_HDSL_B_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_HDSL_B = _DmModemDigitelDT2048_HDSL_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 21)
)
_DmModemDigitelDT2048_MFO_R_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_MFO_R = _DmModemDigitelDT2048_MFO_R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 22)
)
_DmModemDigitelDT8192_4E1_R_ObjectIdentity = ObjectIdentity
dmModemDigitelDT8192_4E1_R = _DmModemDigitelDT8192_4E1_R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 23)
)
_DmModemDigitelDT8192_4E1_1_R_ObjectIdentity = ObjectIdentity
dmModemDigitelDT8192_4E1_1_R = _DmModemDigitelDT8192_4E1_1_R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 24)
)
_DmModemDigitelDT512_MIDX_ObjectIdentity = ObjectIdentity
dmModemDigitelDT512_MIDX = _DmModemDigitelDT512_MIDX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 25)
)
_DmModemDigitelDT1024_MIDX_ObjectIdentity = ObjectIdentity
dmModemDigitelDT1024_MIDX = _DmModemDigitelDT1024_MIDX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 26)
)
_DmModemDigitelDT2048_MFO_2E1_R_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_MFO_2E1_R = _DmModemDigitelDT2048_MFO_2E1_R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 27)
)
_DmModemDigitelDT2048_MFO_2E1_1_R_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_MFO_2E1_1_R = _DmModemDigitelDT2048_MFO_2E1_1_R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 28)
)
_DmModemDigitelDT2048_DX4_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_DX4 = _DmModemDigitelDT2048_DX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 29)
)
_DmModemDigitelDT2048_DX_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_DX = _DmModemDigitelDT2048_DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 30)
)
_DmModemDigitelDT2048_DX_G703_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_DX_G703 = _DmModemDigitelDT2048_DX_G703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 31)
)
_DmModemDigitelDT2048_HDSL_G703_ObjectIdentity = ObjectIdentity
dmModemDigitelDT2048_HDSL_G703 = _DmModemDigitelDT2048_HDSL_G703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 32)
)
_DmModemDigitelSHDSL_D_ObjectIdentity = ObjectIdentity
dmModemDigitelSHDSL_D = _DmModemDigitelSHDSL_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 33)
)
_DmModemDigitelSHDSL_S_ObjectIdentity = ObjectIdentity
dmModemDigitelSHDSL_S = _DmModemDigitelSHDSL_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 34)
)
_DmModemDigitelDT256_MIDX_B_ObjectIdentity = ObjectIdentity
dmModemDigitelDT256_MIDX_B = _DmModemDigitelDT256_MIDX_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 35)
)
_DmModemDigitelDT512_MIDX_B_ObjectIdentity = ObjectIdentity
dmModemDigitelDT512_MIDX_B = _DmModemDigitelDT512_MIDX_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 36)
)
_DmModemDigitelDT1024_MIDX_B_ObjectIdentity = ObjectIdentity
dmModemDigitelDT1024_MIDX_B = _DmModemDigitelDT1024_MIDX_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 4, 37)
)
_DmModemElebra_ObjectIdentity = ObjectIdentity
dmModemElebra = _DmModemElebra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 5)
)
_DmModemElebraEC256K_ObjectIdentity = ObjectIdentity
dmModemElebraEC256K = _DmModemElebraEC256K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 5, 1)
)
_DmModemElebraEC128K_ObjectIdentity = ObjectIdentity
dmModemElebraEC128K = _DmModemElebraEC128K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 5, 2)
)
_DmModemElebraEC512K_ObjectIdentity = ObjectIdentity
dmModemElebraEC512K = _DmModemElebraEC512K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 5, 3)
)
_DmModemElebraEC3465K_ObjectIdentity = ObjectIdentity
dmModemElebraEC3465K = _DmModemElebraEC3465K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3, 5, 4)
)
_DmAcDevNotRegistered_ObjectIdentity = ObjectIdentity
dmAcDevNotRegistered = _DmAcDevNotRegistered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 1)
)
_DmAdItfConverterDatacom_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacom = _DmAdItfConverterDatacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2)
)
_DmAdItfConverterDatacomDM704S_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S = _DmAdItfConverterDatacomDM704S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 1)
)
_DmAdItfConverterDatacomDM704SE_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704SE = _DmAdItfConverterDatacomDM704SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 2)
)
_DmAdItfConverterDatacomDM703_64S_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM703_64S = _DmAdItfConverterDatacomDM703_64S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 3)
)
_DmAdItfConverterDatacomDM703_64SE_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM703_64SE = _DmAdItfConverterDatacomDM703_64SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 4)
)
_DmAdItfConverterDatacomDM704S_a_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S_a = _DmAdItfConverterDatacomDM704S_a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 5)
)
_DmAdItfConverterDatacomDM703_2S_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM703_2S = _DmAdItfConverterDatacomDM703_2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 6)
)
_DmAdItfConverterDatacomDM704SE2_V10_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704SE2_V10 = _DmAdItfConverterDatacomDM704SE2_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 7)
)
_DmAdItfConverterDatacomDM704S2_V10_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V10 = _DmAdItfConverterDatacomDM704S2_V10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 8)
)
_DmAdItfConverterDatacomDM704S2_V11_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V11 = _DmAdItfConverterDatacomDM704S2_V11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 9)
)
_DmAdItfConverterDatacomDM704SE2_V20_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704SE2_V20 = _DmAdItfConverterDatacomDM704SE2_V20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 10)
)
_DmAdItfConverterDatacomDM704S2_V12_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V12 = _DmAdItfConverterDatacomDM704S2_V12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 11)
)
_DmAdItfConverterDatacomDM704S2_V13_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V13 = _DmAdItfConverterDatacomDM704S2_V13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 12)
)
_DmAdItfConverterDatacomDM704S2_V20_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V20 = _DmAdItfConverterDatacomDM704S2_V20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 13)
)
_DmAdItfConverterDatacomDM704S2_V21_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V21 = _DmAdItfConverterDatacomDM704S2_V21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 14)
)
_DmAdItfConverterDatacomDM704S2_V22_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V22 = _DmAdItfConverterDatacomDM704S2_V22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 15)
)
_DmAdItfConverterDatacomDM704S2_V23_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V23 = _DmAdItfConverterDatacomDM704S2_V23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 16)
)
_DmAdItfConverterDatacomDM704SE2_V30_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704SE2_V30 = _DmAdItfConverterDatacomDM704SE2_V30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 17)
)
_DmAdItfConverterDatacomDM704S2_V30_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V30 = _DmAdItfConverterDatacomDM704S2_V30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 18)
)
_DmAdItfConverterDatacomDM704S2_V31_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V31 = _DmAdItfConverterDatacomDM704S2_V31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 19)
)
_DmAdItfConverterDatacomDM704S2_V32_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V32 = _DmAdItfConverterDatacomDM704S2_V32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 20)
)
_DmAdItfConverterDatacomDM704S2_V33_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V33 = _DmAdItfConverterDatacomDM704S2_V33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 21)
)
_DmAdItfConverterDatacomDM704S2_V40_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V40 = _DmAdItfConverterDatacomDM704S2_V40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 22)
)
_DmAdItfConverterDatacomDM704S2_V41_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V41 = _DmAdItfConverterDatacomDM704S2_V41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 23)
)
_DmAdItfConverterDatacomDM704S2_V12B_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V12B = _DmAdItfConverterDatacomDM704S2_V12B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 24)
)
_DmAdItfConverterDatacomDM704S2_V21B_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V21B = _DmAdItfConverterDatacomDM704S2_V21B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 25)
)
_DmAdItfConverterDatacomDM704S2_V22B_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V22B = _DmAdItfConverterDatacomDM704S2_V22B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 26)
)
_DmAdItfConverterDatacomDM704S2_V42_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704S2_V42 = _DmAdItfConverterDatacomDM704S2_V42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 27)
)
_DmAdItfConverterDatacomDM704SE2_V40_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704SE2_V40 = _DmAdItfConverterDatacomDM704SE2_V40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 28)
)
_DmAdItfConverterDatacomDM704SE2_V50_ObjectIdentity = ObjectIdentity
dmAdItfConverterDatacomDM704SE2_V50 = _DmAdItfConverterDatacomDM704SE2_V50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 2, 29)
)
_DmAdMuxDatacom_ObjectIdentity = ObjectIdentity
dmAdMuxDatacom = _DmAdMuxDatacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3)
)
_DmAdMuxDatacomMuxDM705_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM705 = _DmAdMuxDatacomMuxDM705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 1)
)
_DmAdMuxDatacomMuxDM706C_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706C = _DmAdMuxDatacomMuxDM706C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 2)
)
_DmAdMuxDatacomMuxDM16E1_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM16E1 = _DmAdMuxDatacomMuxDM16E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 3)
)
_DmAdMuxDatacomMuxDM4E1_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM4E1 = _DmAdMuxDatacomMuxDM4E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 4)
)
_DmAdMuxDatacomMuxDM704S3_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM704S3 = _DmAdMuxDatacomMuxDM704S3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 5)
)
_DmAdMuxDatacomMuxDM704C3_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM704C3 = _DmAdMuxDatacomMuxDM704C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 6)
)
_DmAdMuxDatacomMuxDM704SE4_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM704SE4 = _DmAdMuxDatacomMuxDM704SE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 10)
)
_DmAdMuxDatacomMuxDM704CE4_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM704CE4 = _DmAdMuxDatacomMuxDM704CE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 11)
)
_DmAdMuxDatacomMuxDM991C_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM991C = _DmAdMuxDatacomMuxDM991C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 21)
)
_DmAdMuxDatacomMuxDM4E1S_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM4E1S = _DmAdMuxDatacomMuxDM4E1S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 22)
)
_DmAdMuxDatacomMuxDM991CVxx_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM991CVxx = _DmAdMuxDatacomMuxDM991CVxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 23)
)
_DmAdMuxDatacomMuxDM991S_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM991S = _DmAdMuxDatacomMuxDM991S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 24)
)
_DmAdMuxDatacomMuxDM991SVxx_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM991SVxx = _DmAdMuxDatacomMuxDM991SVxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 25)
)
_DmAdMuxDatacomMuxDM706C_IPmux_E1Router_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706C_IPmux_E1Router = _DmAdMuxDatacomMuxDM706C_IPmux_E1Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 26)
)
_DmAdMuxDatacomMuxDM706C_IPmux_MultiPortRouter_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706C_IPmux_MultiPortRouter = _DmAdMuxDatacomMuxDM706C_IPmux_MultiPortRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 27)
)
_DmAdMuxDatacomMuxDM706C_MultiPortRouter_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706C_MultiPortRouter = _DmAdMuxDatacomMuxDM706C_MultiPortRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 28)
)
_DmAdMuxDatacomMuxDM706C_E1Router_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706C_E1Router = _DmAdMuxDatacomMuxDM706C_E1Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 29)
)
_DmAdMuxDatacomMuxDM991SE4_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM991SE4 = _DmAdMuxDatacomMuxDM991SE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 31)
)
_DmAdMuxDatacomMuxDM991CE4_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM991CE4 = _DmAdMuxDatacomMuxDM991CE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 32)
)
_DmAdMuxDatacomMuxDM991CR_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM991CR = _DmAdMuxDatacomMuxDM991CR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 33)
)
_DmAdMuxDatacomMuxDM706CR_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706CR = _DmAdMuxDatacomMuxDM706CR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 34)
)
_DmAdMuxDatacomMuxDM300_8E1B_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM300_8E1B = _DmAdMuxDatacomMuxDM300_8E1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 35)
)
_DmAdMuxDatacomMuxDM300_8E1_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM300_8E1 = _DmAdMuxDatacomMuxDM300_8E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 36)
)
_DmAdMuxDatacomMuxDM300_8E1BInvMux_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM300_8E1BInvMux = _DmAdMuxDatacomMuxDM300_8E1BInvMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 37)
)
_DmAdMuxDatacomMuxDM1801_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM1801 = _DmAdMuxDatacomMuxDM1801_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 38)
)
_DmAdMuxDatacomMuxDM300_MC_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM300_MC = _DmAdMuxDatacomMuxDM300_MC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 39)
)
_DmAdMuxDatacomMuxDM991CS_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM991CS = _DmAdMuxDatacomMuxDM991CS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 40)
)
_DmAdMuxDatacomMuxDM706CS_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706CS = _DmAdMuxDatacomMuxDM706CS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 41)
)
_DmAdMuxDatacomMuxDM16E1sII_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM16E1sII = _DmAdMuxDatacomMuxDM16E1sII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 43)
)
_DmAdMuxDatacomMuxDM4E1sII_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM4E1sII = _DmAdMuxDatacomMuxDM4E1sII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 44)
)
_DmAdMuxDatacomMuxDM706PabxM1_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706PabxM1 = _DmAdMuxDatacomMuxDM706PabxM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 45)
)
_DmAdMuxDatacomMuxDM706PabxD1_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706PabxD1 = _DmAdMuxDatacomMuxDM706PabxD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 46)
)
_DmAdMuxDatacomMuxDM16E1InvMux_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM16E1InvMux = _DmAdMuxDatacomMuxDM16E1InvMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 47)
)
_DmAdMuxDatacomMuxDM4E1InvMux_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM4E1InvMux = _DmAdMuxDatacomMuxDM4E1InvMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 48)
)
_DmAdMuxDatacomMuxDM706PabxM2_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706PabxM2 = _DmAdMuxDatacomMuxDM706PabxM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 49)
)
_DmAdMuxDatacomMuxDM706PabxD2_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706PabxD2 = _DmAdMuxDatacomMuxDM706PabxD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 50)
)
_DmAdMuxDatacomMuxDM706E_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706E = _DmAdMuxDatacomMuxDM706E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 51)
)
_DmAdMuxDatacomMuxDM706M1_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706M1 = _DmAdMuxDatacomMuxDM706M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 52)
)
_DmAdMuxDatacomMuxDM706M2_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706M2 = _DmAdMuxDatacomMuxDM706M2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 53)
)
_DmAdMuxDatacomMuxDM706M4_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706M4 = _DmAdMuxDatacomMuxDM706M4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 54)
)
_DmAdMuxDatacomMuxDM706PabxM_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706PabxM = _DmAdMuxDatacomMuxDM706PabxM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 55)
)
_DmAdMuxDatacomMuxDM706PabxD_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706PabxD = _DmAdMuxDatacomMuxDM706PabxD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 56)
)
_DmAdMuxDatacomMuxDM706Ehk_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706Ehk = _DmAdMuxDatacomMuxDM706Ehk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 81)
)
_DmAdMuxDatacomMuxDM706M1hk_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706M1hk = _DmAdMuxDatacomMuxDM706M1hk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 82)
)
_DmAdMuxDatacomMuxDM706M2hk_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706M2hk = _DmAdMuxDatacomMuxDM706M2hk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 83)
)
_DmAdMuxDatacomMuxDM706M4hk_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706M4hk = _DmAdMuxDatacomMuxDM706M4hk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 84)
)
_DmAdMuxDatacomMuxDM706Ke_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706Ke = _DmAdMuxDatacomMuxDM706Ke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 85)
)
_DmAdMuxDatacomMuxDM706Km1_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706Km1 = _DmAdMuxDatacomMuxDM706Km1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 86)
)
_DmAdMuxDatacomMuxDM706Km2_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706Km2 = _DmAdMuxDatacomMuxDM706Km2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 87)
)
_DmAdMuxDatacomMuxDM706Km4_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM706Km4 = _DmAdMuxDatacomMuxDM706Km4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 88)
)
_DmAdMuxDatacomMuxDMSTM1_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDMSTM1 = _DmAdMuxDatacomMuxDMSTM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 101)
)
_DmAdMuxDatacomMuxDM705_CPU34_Sub_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM705_CPU34_Sub = _DmAdMuxDatacomMuxDM705_CPU34_Sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 109)
)
_DmAdMuxDatacomMuxDM705_CPU34_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM705_CPU34 = _DmAdMuxDatacomMuxDM705_CPU34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 110)
)
_DmAdMuxDatacomMuxDM705_CPU64_Sub_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM705_CPU64_Sub = _DmAdMuxDatacomMuxDM705_CPU64_Sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 111)
)
_DmAdMuxDatacomMuxDM705_CPU64_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM705_CPU64 = _DmAdMuxDatacomMuxDM705_CPU64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 112)
)
_DmAdMuxDatacomMuxDM705_CPU32_Sub_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM705_CPU32_Sub = _DmAdMuxDatacomMuxDM705_CPU32_Sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 113)
)
_DmAdMuxDatacomMuxDM705_CPU128_Sub_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM705_CPU128_Sub = _DmAdMuxDatacomMuxDM705_CPU128_Sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 114)
)
_DmAdMuxDatacomMuxDM881_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM881 = _DmAdMuxDatacomMuxDM881_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 116)
)
_DmAdMuxDatacomMuxDM814_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM814 = _DmAdMuxDatacomMuxDM814_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 117)
)
_DmAdMuxDatacomMuxDM830_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM830 = _DmAdMuxDatacomMuxDM830_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 118)
)
_DmAdMuxDatacomMuxDM880_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM880 = _DmAdMuxDatacomMuxDM880_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 119)
)
_DmAdMuxDatacomMuxDM810_ObjectIdentity = ObjectIdentity
dmAdMuxDatacomMuxDM810 = _DmAdMuxDatacomMuxDM810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5, 3, 120)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATACOM-REG",
    **{"datacomRegistrationModule": datacomRegistrationModule,
       "datacomModemManagCardDMG20": datacomModemManagCardDMG20,
       "datacomDm705ManagCard": datacomDm705ManagCard,
       "datacomDm16E1ManagCard": datacomDm16E1ManagCard,
       "datacomDm4E1ManagCard": datacomDm4E1ManagCard,
       "datacomDm706CManagCard": datacomDm706CManagCard,
       "datacomDmSTM1ManagCard": datacomDmSTM1ManagCard,
       "datacomDm705CPU64ManagCard": datacomDm705CPU64ManagCard,
       "datacomDm706CIPmuxE1RouterManagCard": datacomDm706CIPmuxE1RouterManagCard,
       "datacomDm706CIPmuxMultiPortRouterManagCard": datacomDm706CIPmuxMultiPortRouterManagCard,
       "datacomDm706CMultiPortRouterManagCard": datacomDm706CMultiPortRouterManagCard,
       "datacomDm706CE1RouterManagCard": datacomDm706CE1RouterManagCard,
       "datacomDmSwitch3224F1ManagCard": datacomDmSwitch3224F1ManagCard,
       "datacomDm300-8E1ManagCard": datacomDm300_8E1ManagCard,
       "datacomDm300-8E1BInvMuxManagCard": datacomDm300_8E1BInvMuxManagCard,
       "datacomDm1801ManagCard": datacomDm1801ManagCard,
       "datacomDmSwitch3224F2ManagCard": datacomDmSwitch3224F2ManagCard,
       "datacomDmSwitch3324F1ManagCard": datacomDmSwitch3324F1ManagCard,
       "datacomDmSwitch3324F2ManagCard": datacomDmSwitch3324F2ManagCard,
       "datacomDm881ManagCard": datacomDm881ManagCard,
       "datacomDm814ManagCard": datacomDm814ManagCard,
       "datacomDm830ManagCard": datacomDm830ManagCard,
       "datacomDm300-MCManagCard": datacomDm300_MCManagCard,
       "datacomDm300-8E1BManagCard": datacomDm300_8E1BManagCard,
       "datacomDm991CRManagCard": datacomDm991CRManagCard,
       "datacomDm705CPU128ManagCard": datacomDm705CPU128ManagCard,
       "datacomDm880ManagCard": datacomDm880ManagCard,
       "datacomDmSwitch3224F3ManagCard": datacomDmSwitch3224F3ManagCard,
       "datacomDmSwitch3324F3ManagCard": datacomDmSwitch3324F3ManagCard,
       "datacomDm4000Mpu192ManagCard": datacomDm4000Mpu192ManagCard,
       "datacomDm4000Eth24GxManagCard": datacomDm4000Eth24GxManagCard,
       "datacomDmSwitch2204G1ManagCard": datacomDmSwitch2204G1ManagCard,
       "datacomDmSwitch2304G1ManagCard": datacomDmSwitch2304G1ManagCard,
       "datacomDm4000Eth12GxManagCard": datacomDm4000Eth12GxManagCard,
       "datacomDm4000Eth2x10GxManagCard": datacomDm4000Eth2x10GxManagCard,
       "datacomDm4000Eth1x10GxManagCard": datacomDm4000Eth1x10GxManagCard,
       "datacomDm4000Eth12Gx1x10GxManagCard": datacomDm4000Eth12Gx1x10GxManagCard,
       "datacomDm4000Eth48GtManagCard": datacomDm4000Eth48GtManagCard,
       "datacomDm4000Eth24GtManagCard": datacomDm4000Eth24GtManagCard,
       "datacomDm4000Mpu384ManagCard": datacomDm4000Mpu384ManagCard,
       "datacomDm16E1InvMuxManagCard": datacomDm16E1InvMuxManagCard,
       "datacomDm4E1InvMuxManagCard": datacomDm4E1InvMuxManagCard,
       "datacomDm16E1sIIManagCard": datacomDm16E1sIIManagCard,
       "datacomDm4E1sIIManagCard": datacomDm4E1sIIManagCard,
       "datacomDm706CRManagCard": datacomDm706CRManagCard,
       "datacomDm991CSManagCard": datacomDm991CSManagCard,
       "datacomDm706CSManagCard": datacomDm706CSManagCard,
       "datacomDm706EManagCard": datacomDm706EManagCard,
       "datacomDm706M1ManagCard": datacomDm706M1ManagCard,
       "datacomDm706M2ManagCard": datacomDm706M2ManagCard,
       "datacomDm706M4ManagCard": datacomDm706M4ManagCard,
       "datacomDm706Pabxm1ManagCard": datacomDm706Pabxm1ManagCard,
       "datacomDm706Pabxd1ManagCard": datacomDm706Pabxd1ManagCard,
       "datacomDm706Pabxm2ManagCard": datacomDm706Pabxm2ManagCard,
       "datacomDm706Pabxd2ManagCard": datacomDm706Pabxd2ManagCard,
       "datacomDm706PabxmManagCard": datacomDm706PabxmManagCard,
       "datacomDm706PabxdManagCard": datacomDm706PabxdManagCard,
       "datacomDm4000Eth24GXx2Xx10GXManagCard": datacomDm4000Eth24GXx2Xx10GXManagCard,
       "datacomDm4000Eth48GXManagCard": datacomDm4000Eth48GXManagCard,
       "datacomDm4000Eth4x10GXHSeriesManagCard": datacomDm4000Eth4x10GXHSeriesManagCard,
       "datacomDmSwitch2104G1-EddManagCard": datacomDmSwitch2104G1_EddManagCard,
       "datacomDmSwitch2104G2-EddManagCard": datacomDmSwitch2104G2_EddManagCard,
       "datacomDm810ManagCard": datacomDm810ManagCard,
       "datacomDm4000Eth24GX2x10GXHSeriesManagCard": datacomDm4000Eth24GX2x10GXHSeriesManagCard,
       "datacomDm4000Eth48GXHSeriesManagCard": datacomDm4000Eth48GXHSeriesManagCard,
       "datacomDm4000Eth10GX32E1ManagCard": datacomDm4000Eth10GX32E1ManagCard,
       "datacomDm4000EthSceqManagCard": datacomDm4000EthSceqManagCard,
       "datacomDm4000Eth24GXHSeriesManagCard": datacomDm4000Eth24GXHSeriesManagCard,
       "datacomDm705CPU34ManagCard": datacomDm705CPU34ManagCard,
       "datacomDm4650ManagCard": datacomDm4650ManagCard,
       "datacomPabxManagCard": datacomPabxManagCard,
       "datacomDm4000Eth2x10GxHSeriesManagCard": datacomDm4000Eth2x10GxHSeriesManagCard,
       "datacomDmSwitch2104G2Wri-EddManagCard": datacomDmSwitch2104G2Wri_EddManagCard,
       "datacomDm706EhkManagCard": datacomDm706EhkManagCard,
       "datacomDmSwitch2104G1SeriesII-EddManagCard": datacomDmSwitch2104G1SeriesII_EddManagCard,
       "datacomDm2106-2GX-ManagCard": datacomDm2106_2GX_ManagCard,
       "datacomDm2106-4GX-ManagCard": datacomDm2106_4GX_ManagCard,
       "datacomDm2106-4GXx8E1-EddManagCard": datacomDm2106_4GXx8E1_EddManagCard,
       "datacomDmSwitch2104G2-EDDxE1-EddManagCard": datacomDmSwitch2104G2_EDDxE1_EddManagCard,
       "datacomDmSwitch2104G1-EDDSeriesII-EddManagCard": datacomDmSwitch2104G1_EDDSeriesII_EddManagCard,
       "datacomDmSwitch2104G2-EDDxE1SeriesII-EddManagCard": datacomDmSwitch2104G2_EDDxE1SeriesII_EddManagCard,
       "datacomDm4000Eth24GxLSeriesManagCard": datacomDm4000Eth24GxLSeriesManagCard,
       "datacomDm4000Mpu512ManagCard": datacomDm4000Mpu512ManagCard,
       "datacomDmSwitch2104G2S3Wri-EddManagCard": datacomDmSwitch2104G2S3Wri_EddManagCard,
       "datacomDm4100Eth24GXx4GXManagCard": datacomDm4100Eth24GXx4GXManagCard,
       "datacomDm4100Eth24GXx2XXManagCard": datacomDm4100Eth24GXx2XXManagCard,
       "datacomDm4100Eth24GXxSManagCard": datacomDm4100Eth24GXxSManagCard,
       "datacomDm4100Eth24GXx2XXxSManagCard": datacomDm4100Eth24GXx2XXxSManagCard,
       "datacomDm4100Eth24GXx4XXManagCard": datacomDm4100Eth24GXx4XXManagCard,
       "datacomDm4100Eth20GTx4GCManagCard": datacomDm4100Eth20GTx4GCManagCard,
       "datacomDm4100Eth20GTx4GCx2XXManagCard": datacomDm4100Eth20GTx4GCx2XXManagCard,
       "datacomDm4100Eth20GTx4GCxSManagCard": datacomDm4100Eth20GTx4GCxSManagCard,
       "datacomDm4100Eth20GTx4GCx2XXxSManagCard": datacomDm4100Eth20GTx4GCx2XXxSManagCard,
       "datacomDm4100Eth20GTx4GCx4XXManagCard": datacomDm4100Eth20GTx4GCx4XXManagCard,
       "datacomDmSwitchEddE1S2ManagCard": datacomDmSwitchEddE1S2ManagCard,
       "datacomDm4100Eth44GPx4GCManagCard": datacomDm4100Eth44GPx4GCManagCard,
       "datacomDm4100Eth44GTx4GCx2XXManagCard": datacomDm4100Eth44GTx4GCx2XXManagCard,
       "datacomDm4100Eth44GTx4GCxSManagCard": datacomDm4100Eth44GTx4GCxSManagCard,
       "datacomDm4100Eth44GTx4GCx2XXxSManagCard": datacomDm4100Eth44GTx4GCx2XXxSManagCard,
       "datacomDm4100Eth44GTx4GCx4XXManagCard": datacomDm4100Eth44GTx4GCx4XXManagCard,
       "datacomDm4100Eth44GTx4GCx2XSManagCard": datacomDm4100Eth44GTx4GCx2XSManagCard,
       "datacomDm4100Eth44GTx4GCx2XSxSManagCard": datacomDm4100Eth44GTx4GCx2XSxSManagCard,
       "datacomDm4100Eth44GTx4GCx4XSManagCard": datacomDm4100Eth44GTx4GCx4XSManagCard,
       "dmModemNotRegistered": dmModemNotRegistered,
       "dmModemDatacom": dmModemDatacom,
       "dmModemParks": dmModemParks,
       "dmModemParksUP128F2": dmModemParksUP128F2,
       "dmModemParksUP128F4": dmModemParksUP128F4,
       "dmModemParksUP64": dmModemParksUP64,
       "dmModemParksUP128": dmModemParksUP128,
       "dmModemParksUP256": dmModemParksUP256,
       "dmModemParksUP384": dmModemParksUP384,
       "dmModemParksUP512": dmModemParksUP512,
       "dmModemParksUP2048HDSL": dmModemParksUP2048HDSL,
       "dmModemParksUP3420": dmModemParksUP3420,
       "dmModemParksDuo2": dmModemParksDuo2,
       "dmModemParksUP64F2": dmModemParksUP64F2,
       "dmModemParksUP64F4": dmModemParksUP64F4,
       "dmModemParksPower512MSDSL": dmModemParksPower512MSDSL,
       "dmModemParksFiber4E1": dmModemParksFiber4E1,
       "dmModemParksPower512MSDSL-S2": dmModemParksPower512MSDSL_S2,
       "dmModemParksPower2048MSDSL": dmModemParksPower2048MSDSL,
       "dmModemParksPower2048HDSL": dmModemParksPower2048HDSL,
       "dmModemParksFiber16E1": dmModemParksFiber16E1,
       "dmModemParksPower512MSDSL-2F-GVCE": dmModemParksPower512MSDSL_2F_GVCE,
       "dmModemParksPower512MSDSL-2F-GVC": dmModemParksPower512MSDSL_2F_GVC,
       "dmModemParksPower512MSDSL-2F-GV": dmModemParksPower512MSDSL_2F_GV,
       "dmModemParksPower512MSDSL-2F-VC": dmModemParksPower512MSDSL_2F_VC,
       "dmModemParksPower512MSDSL-2F-E": dmModemParksPower512MSDSL_2F_E,
       "dmModemParksPower512MSDSL-4F-GVCE": dmModemParksPower512MSDSL_4F_GVCE,
       "dmModemParksPower512MSDSL-4F-GVC": dmModemParksPower512MSDSL_4F_GVC,
       "dmModemParksPower512MSDSL-4F-GV": dmModemParksPower512MSDSL_4F_GV,
       "dmModemParksPower512MSDSL-4F-VC": dmModemParksPower512MSDSL_4F_VC,
       "dmModemParksPower512MSDSL-4F-E": dmModemParksPower512MSDSL_4F_E,
       "dmModemParksPower512MSDSL-2F-GV-DM": dmModemParksPower512MSDSL_2F_GV_DM,
       "dmModemParksPower512MSDSL-4F-GV-DM": dmModemParksPower512MSDSL_4F_GV_DM,
       "dmModemParksPower2048MSDSL-2F-GVCE": dmModemParksPower2048MSDSL_2F_GVCE,
       "dmModemParksPower2048MSDSL-2F-GV": dmModemParksPower2048MSDSL_2F_GV,
       "dmModemParksPower2048MSDSL-2F-GVC": dmModemParksPower2048MSDSL_2F_GVC,
       "dmModemParksPower2048MSDSL-2F-VC": dmModemParksPower2048MSDSL_2F_VC,
       "dmModemParksPower2048MSDSL-2F-E": dmModemParksPower2048MSDSL_2F_E,
       "dmModemParksPower2048MSDSL-4F-GVCE": dmModemParksPower2048MSDSL_4F_GVCE,
       "dmModemParksPower2048MSDSL-4F-GV": dmModemParksPower2048MSDSL_4F_GV,
       "dmModemParksPower2048MSDSL-4F-GVC": dmModemParksPower2048MSDSL_4F_GVC,
       "dmModemParksPower2048MSDSL-4F-VC": dmModemParksPower2048MSDSL_4F_VC,
       "dmModemParksPower2048MSDSL-4F-E": dmModemParksPower2048MSDSL_4F_E,
       "dmModemParksPower2048MSDSL-2F-GV-DM": dmModemParksPower2048MSDSL_2F_GV_DM,
       "dmModemParksPower2048MSDSL-4F-GV-DM": dmModemParksPower2048MSDSL_4F_GV_DM,
       "dmModemDigitel": dmModemDigitel,
       "dmModemDigitelDT32B": dmModemDigitelDT32B,
       "dmModemDigitelDT34": dmModemDigitelDT34,
       "dmModemDigitelDT64MI": dmModemDigitelDT64MI,
       "dmModemDigitelDT128MI": dmModemDigitelDT128MI,
       "dmModemDigitelDT256MI": dmModemDigitelDT256MI,
       "dmModemDigitelDT2048": dmModemDigitelDT2048,
       "dmModemDigitelDT2048-MFO": dmModemDigitelDT2048_MFO,
       "dmModemDigitelTRANSEND-THREE": dmModemDigitelTRANSEND_THREE,
       "dmModemDigitelDT2048-HXR": dmModemDigitelDT2048_HXR,
       "dmModemDigitelDT2048-HDSL": dmModemDigitelDT2048_HDSL,
       "dmModemDigitelDT64MIa": dmModemDigitelDT64MIa,
       "dmModemDigitelDT128MIa": dmModemDigitelDT128MIa,
       "dmModemDigitelDT256MIa": dmModemDigitelDT256MIa,
       "dmModemDigitelDT2048-HDSLex": dmModemDigitelDT2048_HDSLex,
       "dmModemDigitelDT8192-4E1": dmModemDigitelDT8192_4E1,
       "dmModemDigitelDT8192": dmModemDigitelDT8192,
       "dmModemDigitelDT8192BK": dmModemDigitelDT8192BK,
       "dmModemDigitelDT1024MI": dmModemDigitelDT1024MI,
       "dmModemDigitelDT2048-MX2": dmModemDigitelDT2048_MX2,
       "dmModemDigitelDT256-MIDX": dmModemDigitelDT256_MIDX,
       "dmModemDigitelDT2048-HDSL-B": dmModemDigitelDT2048_HDSL_B,
       "dmModemDigitelDT2048-MFO-R": dmModemDigitelDT2048_MFO_R,
       "dmModemDigitelDT8192-4E1-R": dmModemDigitelDT8192_4E1_R,
       "dmModemDigitelDT8192-4E1-1-R": dmModemDigitelDT8192_4E1_1_R,
       "dmModemDigitelDT512-MIDX": dmModemDigitelDT512_MIDX,
       "dmModemDigitelDT1024-MIDX": dmModemDigitelDT1024_MIDX,
       "dmModemDigitelDT2048-MFO-2E1-R": dmModemDigitelDT2048_MFO_2E1_R,
       "dmModemDigitelDT2048-MFO-2E1-1-R": dmModemDigitelDT2048_MFO_2E1_1_R,
       "dmModemDigitelDT2048-DX4": dmModemDigitelDT2048_DX4,
       "dmModemDigitelDT2048-DX": dmModemDigitelDT2048_DX,
       "dmModemDigitelDT2048-DX-G703": dmModemDigitelDT2048_DX_G703,
       "dmModemDigitelDT2048-HDSL-G703": dmModemDigitelDT2048_HDSL_G703,
       "dmModemDigitelSHDSL-D": dmModemDigitelSHDSL_D,
       "dmModemDigitelSHDSL-S": dmModemDigitelSHDSL_S,
       "dmModemDigitelDT256-MIDX-B": dmModemDigitelDT256_MIDX_B,
       "dmModemDigitelDT512-MIDX-B": dmModemDigitelDT512_MIDX_B,
       "dmModemDigitelDT1024-MIDX-B": dmModemDigitelDT1024_MIDX_B,
       "dmModemElebra": dmModemElebra,
       "dmModemElebraEC256K": dmModemElebraEC256K,
       "dmModemElebraEC128K": dmModemElebraEC128K,
       "dmModemElebraEC512K": dmModemElebraEC512K,
       "dmModemElebraEC3465K": dmModemElebraEC3465K,
       "dmAcDevNotRegistered": dmAcDevNotRegistered,
       "dmAdItfConverterDatacom": dmAdItfConverterDatacom,
       "dmAdItfConverterDatacomDM704S": dmAdItfConverterDatacomDM704S,
       "dmAdItfConverterDatacomDM704SE": dmAdItfConverterDatacomDM704SE,
       "dmAdItfConverterDatacomDM703-64S": dmAdItfConverterDatacomDM703_64S,
       "dmAdItfConverterDatacomDM703-64SE": dmAdItfConverterDatacomDM703_64SE,
       "dmAdItfConverterDatacomDM704S-a": dmAdItfConverterDatacomDM704S_a,
       "dmAdItfConverterDatacomDM703-2S": dmAdItfConverterDatacomDM703_2S,
       "dmAdItfConverterDatacomDM704SE2-V10": dmAdItfConverterDatacomDM704SE2_V10,
       "dmAdItfConverterDatacomDM704S2-V10": dmAdItfConverterDatacomDM704S2_V10,
       "dmAdItfConverterDatacomDM704S2-V11": dmAdItfConverterDatacomDM704S2_V11,
       "dmAdItfConverterDatacomDM704SE2-V20": dmAdItfConverterDatacomDM704SE2_V20,
       "dmAdItfConverterDatacomDM704S2-V12": dmAdItfConverterDatacomDM704S2_V12,
       "dmAdItfConverterDatacomDM704S2-V13": dmAdItfConverterDatacomDM704S2_V13,
       "dmAdItfConverterDatacomDM704S2-V20": dmAdItfConverterDatacomDM704S2_V20,
       "dmAdItfConverterDatacomDM704S2-V21": dmAdItfConverterDatacomDM704S2_V21,
       "dmAdItfConverterDatacomDM704S2-V22": dmAdItfConverterDatacomDM704S2_V22,
       "dmAdItfConverterDatacomDM704S2-V23": dmAdItfConverterDatacomDM704S2_V23,
       "dmAdItfConverterDatacomDM704SE2-V30": dmAdItfConverterDatacomDM704SE2_V30,
       "dmAdItfConverterDatacomDM704S2-V30": dmAdItfConverterDatacomDM704S2_V30,
       "dmAdItfConverterDatacomDM704S2-V31": dmAdItfConverterDatacomDM704S2_V31,
       "dmAdItfConverterDatacomDM704S2-V32": dmAdItfConverterDatacomDM704S2_V32,
       "dmAdItfConverterDatacomDM704S2-V33": dmAdItfConverterDatacomDM704S2_V33,
       "dmAdItfConverterDatacomDM704S2-V40": dmAdItfConverterDatacomDM704S2_V40,
       "dmAdItfConverterDatacomDM704S2-V41": dmAdItfConverterDatacomDM704S2_V41,
       "dmAdItfConverterDatacomDM704S2-V12B": dmAdItfConverterDatacomDM704S2_V12B,
       "dmAdItfConverterDatacomDM704S2-V21B": dmAdItfConverterDatacomDM704S2_V21B,
       "dmAdItfConverterDatacomDM704S2-V22B": dmAdItfConverterDatacomDM704S2_V22B,
       "dmAdItfConverterDatacomDM704S2-V42": dmAdItfConverterDatacomDM704S2_V42,
       "dmAdItfConverterDatacomDM704SE2-V40": dmAdItfConverterDatacomDM704SE2_V40,
       "dmAdItfConverterDatacomDM704SE2-V50": dmAdItfConverterDatacomDM704SE2_V50,
       "dmAdMuxDatacom": dmAdMuxDatacom,
       "dmAdMuxDatacomMuxDM705": dmAdMuxDatacomMuxDM705,
       "dmAdMuxDatacomMuxDM706C": dmAdMuxDatacomMuxDM706C,
       "dmAdMuxDatacomMuxDM16E1": dmAdMuxDatacomMuxDM16E1,
       "dmAdMuxDatacomMuxDM4E1": dmAdMuxDatacomMuxDM4E1,
       "dmAdMuxDatacomMuxDM704S3": dmAdMuxDatacomMuxDM704S3,
       "dmAdMuxDatacomMuxDM704C3": dmAdMuxDatacomMuxDM704C3,
       "dmAdMuxDatacomMuxDM704SE4": dmAdMuxDatacomMuxDM704SE4,
       "dmAdMuxDatacomMuxDM704CE4": dmAdMuxDatacomMuxDM704CE4,
       "dmAdMuxDatacomMuxDM991C": dmAdMuxDatacomMuxDM991C,
       "dmAdMuxDatacomMuxDM4E1S": dmAdMuxDatacomMuxDM4E1S,
       "dmAdMuxDatacomMuxDM991CVxx": dmAdMuxDatacomMuxDM991CVxx,
       "dmAdMuxDatacomMuxDM991S": dmAdMuxDatacomMuxDM991S,
       "dmAdMuxDatacomMuxDM991SVxx": dmAdMuxDatacomMuxDM991SVxx,
       "dmAdMuxDatacomMuxDM706C-IPmux-E1Router": dmAdMuxDatacomMuxDM706C_IPmux_E1Router,
       "dmAdMuxDatacomMuxDM706C-IPmux-MultiPortRouter": dmAdMuxDatacomMuxDM706C_IPmux_MultiPortRouter,
       "dmAdMuxDatacomMuxDM706C-MultiPortRouter": dmAdMuxDatacomMuxDM706C_MultiPortRouter,
       "dmAdMuxDatacomMuxDM706C-E1Router": dmAdMuxDatacomMuxDM706C_E1Router,
       "dmAdMuxDatacomMuxDM991SE4": dmAdMuxDatacomMuxDM991SE4,
       "dmAdMuxDatacomMuxDM991CE4": dmAdMuxDatacomMuxDM991CE4,
       "dmAdMuxDatacomMuxDM991CR": dmAdMuxDatacomMuxDM991CR,
       "dmAdMuxDatacomMuxDM706CR": dmAdMuxDatacomMuxDM706CR,
       "dmAdMuxDatacomMuxDM300-8E1B": dmAdMuxDatacomMuxDM300_8E1B,
       "dmAdMuxDatacomMuxDM300-8E1": dmAdMuxDatacomMuxDM300_8E1,
       "dmAdMuxDatacomMuxDM300-8E1BInvMux": dmAdMuxDatacomMuxDM300_8E1BInvMux,
       "dmAdMuxDatacomMuxDM1801": dmAdMuxDatacomMuxDM1801,
       "dmAdMuxDatacomMuxDM300-MC": dmAdMuxDatacomMuxDM300_MC,
       "dmAdMuxDatacomMuxDM991CS": dmAdMuxDatacomMuxDM991CS,
       "dmAdMuxDatacomMuxDM706CS": dmAdMuxDatacomMuxDM706CS,
       "dmAdMuxDatacomMuxDM16E1sII": dmAdMuxDatacomMuxDM16E1sII,
       "dmAdMuxDatacomMuxDM4E1sII": dmAdMuxDatacomMuxDM4E1sII,
       "dmAdMuxDatacomMuxDM706PabxM1": dmAdMuxDatacomMuxDM706PabxM1,
       "dmAdMuxDatacomMuxDM706PabxD1": dmAdMuxDatacomMuxDM706PabxD1,
       "dmAdMuxDatacomMuxDM16E1InvMux": dmAdMuxDatacomMuxDM16E1InvMux,
       "dmAdMuxDatacomMuxDM4E1InvMux": dmAdMuxDatacomMuxDM4E1InvMux,
       "dmAdMuxDatacomMuxDM706PabxM2": dmAdMuxDatacomMuxDM706PabxM2,
       "dmAdMuxDatacomMuxDM706PabxD2": dmAdMuxDatacomMuxDM706PabxD2,
       "dmAdMuxDatacomMuxDM706E": dmAdMuxDatacomMuxDM706E,
       "dmAdMuxDatacomMuxDM706M1": dmAdMuxDatacomMuxDM706M1,
       "dmAdMuxDatacomMuxDM706M2": dmAdMuxDatacomMuxDM706M2,
       "dmAdMuxDatacomMuxDM706M4": dmAdMuxDatacomMuxDM706M4,
       "dmAdMuxDatacomMuxDM706PabxM": dmAdMuxDatacomMuxDM706PabxM,
       "dmAdMuxDatacomMuxDM706PabxD": dmAdMuxDatacomMuxDM706PabxD,
       "dmAdMuxDatacomMuxDM706Ehk": dmAdMuxDatacomMuxDM706Ehk,
       "dmAdMuxDatacomMuxDM706M1hk": dmAdMuxDatacomMuxDM706M1hk,
       "dmAdMuxDatacomMuxDM706M2hk": dmAdMuxDatacomMuxDM706M2hk,
       "dmAdMuxDatacomMuxDM706M4hk": dmAdMuxDatacomMuxDM706M4hk,
       "dmAdMuxDatacomMuxDM706Ke": dmAdMuxDatacomMuxDM706Ke,
       "dmAdMuxDatacomMuxDM706Km1": dmAdMuxDatacomMuxDM706Km1,
       "dmAdMuxDatacomMuxDM706Km2": dmAdMuxDatacomMuxDM706Km2,
       "dmAdMuxDatacomMuxDM706Km4": dmAdMuxDatacomMuxDM706Km4,
       "dmAdMuxDatacomMuxDMSTM1": dmAdMuxDatacomMuxDMSTM1,
       "dmAdMuxDatacomMuxDM705-CPU34-Sub": dmAdMuxDatacomMuxDM705_CPU34_Sub,
       "dmAdMuxDatacomMuxDM705-CPU34": dmAdMuxDatacomMuxDM705_CPU34,
       "dmAdMuxDatacomMuxDM705-CPU64-Sub": dmAdMuxDatacomMuxDM705_CPU64_Sub,
       "dmAdMuxDatacomMuxDM705-CPU64": dmAdMuxDatacomMuxDM705_CPU64,
       "dmAdMuxDatacomMuxDM705-CPU32-Sub": dmAdMuxDatacomMuxDM705_CPU32_Sub,
       "dmAdMuxDatacomMuxDM705-CPU128-Sub": dmAdMuxDatacomMuxDM705_CPU128_Sub,
       "dmAdMuxDatacomMuxDM881": dmAdMuxDatacomMuxDM881,
       "dmAdMuxDatacomMuxDM814": dmAdMuxDatacomMuxDM814,
       "dmAdMuxDatacomMuxDM830": dmAdMuxDatacomMuxDM830,
       "dmAdMuxDatacomMuxDM880": dmAdMuxDatacomMuxDM880,
       "dmAdMuxDatacomMuxDM810": dmAdMuxDatacomMuxDM810}
)
