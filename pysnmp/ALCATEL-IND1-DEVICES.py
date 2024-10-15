# SNMP MIB module (ALCATEL-IND1-DEVICES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-DEVICES
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:50 2024
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

(hardwareIND1Devices,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "hardwareIND1Devices")

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

alcatelIND1DevicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1)
)
alcatelIND1DevicesMIB.setRevisions(
        ("2011-08-04 00:00",
         "2010-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FamilyOmniSwitch10000_ObjectIdentity = ObjectIdentity
familyOmniSwitch10000 = _FamilyOmniSwitch10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    familyOmniSwitch10000.setStatus("current")
_ChassisOmniSwitch10000_ObjectIdentity = ObjectIdentity
chassisOmniSwitch10000 = _ChassisOmniSwitch10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch10000.setStatus("current")
_DeviceOmniSwitch10000_ObjectIdentity = ObjectIdentity
deviceOmniSwitch10000 = _DeviceOmniSwitch10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch10000.setStatus("current")
_FansOmniSwitch10000_ObjectIdentity = ObjectIdentity
fansOmniSwitch10000 = _FansOmniSwitch10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch10000.setStatus("current")
_FansOmniSwitch10000FT_ObjectIdentity = ObjectIdentity
fansOmniSwitch10000FT = _FansOmniSwitch10000FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    fansOmniSwitch10000FT.setStatus("current")
_PowersOmniSwitch10000_ObjectIdentity = ObjectIdentity
powersOmniSwitch10000 = _PowersOmniSwitch10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch10000.setStatus("current")
_PowersOmniSwitch10000AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch10000AC = _PowersOmniSwitch10000AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch10000AC.setStatus("current")
_PowersOmniSwitch10000DC_ObjectIdentity = ObjectIdentity
powersOmniSwitch10000DC = _PowersOmniSwitch10000DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    powersOmniSwitch10000DC.setStatus("current")
_ModulesOmniSwitch10000_ObjectIdentity = ObjectIdentity
modulesOmniSwitch10000 = _ModulesOmniSwitch10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch10000.setStatus("current")
_ModulesOmniSwitch10000CM_ObjectIdentity = ObjectIdentity
modulesOmniSwitch10000CM = _ModulesOmniSwitch10000CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 1)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch10000CM.setStatus("current")
_CmmOmniSwitch10000_ObjectIdentity = ObjectIdentity
cmmOmniSwitch10000 = _CmmOmniSwitch10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch10000.setStatus("current")
_CmmOmniSwitch10000PROC_ObjectIdentity = ObjectIdentity
cmmOmniSwitch10000PROC = _CmmOmniSwitch10000PROC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmmOmniSwitch10000PROC.setStatus("current")
_ModulesOmniSwitch10000NI_ObjectIdentity = ObjectIdentity
modulesOmniSwitch10000NI = _ModulesOmniSwitch10000NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch10000NI.setStatus("current")
_NiOmniSwitch10000GNI_ObjectIdentity = ObjectIdentity
niOmniSwitch10000GNI = _NiOmniSwitch10000GNI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 1)
)
if mibBuilder.loadTexts:
    niOmniSwitch10000GNI.setStatus("current")
_GniOmniSwitch10000C48_ObjectIdentity = ObjectIdentity
gniOmniSwitch10000C48 = _GniOmniSwitch10000C48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    gniOmniSwitch10000C48.setStatus("current")
_GniOmniSwitch10000U48_ObjectIdentity = ObjectIdentity
gniOmniSwitch10000U48 = _GniOmniSwitch10000U48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gniOmniSwitch10000U48.setStatus("current")
_NiOmniSwitch10000XNI_ObjectIdentity = ObjectIdentity
niOmniSwitch10000XNI = _NiOmniSwitch10000XNI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 2)
)
if mibBuilder.loadTexts:
    niOmniSwitch10000XNI.setStatus("current")
_GniOmniSwitch10000X16M_ObjectIdentity = ObjectIdentity
gniOmniSwitch10000X16M = _GniOmniSwitch10000X16M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gniOmniSwitch10000X16M.setStatus("current")
_GniOmniSwitch10000X32M_ObjectIdentity = ObjectIdentity
gniOmniSwitch10000X32M = _GniOmniSwitch10000X32M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gniOmniSwitch10000X32M.setStatus("current")
_GniOmniSwitch10000X16E_ObjectIdentity = ObjectIdentity
gniOmniSwitch10000X16E = _GniOmniSwitch10000X16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    gniOmniSwitch10000X16E.setStatus("current")
_GniOmniSwitch10000X16L_ObjectIdentity = ObjectIdentity
gniOmniSwitch10000X16L = _GniOmniSwitch10000X16L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 2, 4)
)
if mibBuilder.loadTexts:
    gniOmniSwitch10000X16L.setStatus("current")
_GniOmniSwitch10000X32E_ObjectIdentity = ObjectIdentity
gniOmniSwitch10000X32E = _GniOmniSwitch10000X32E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 2, 5)
)
if mibBuilder.loadTexts:
    gniOmniSwitch10000X32E.setStatus("current")
_NiOmniSwitch10000QNI_ObjectIdentity = ObjectIdentity
niOmniSwitch10000QNI = _NiOmniSwitch10000QNI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 3)
)
if mibBuilder.loadTexts:
    niOmniSwitch10000QNI.setStatus("current")
_GniOmniSwitch10000Q8_ObjectIdentity = ObjectIdentity
gniOmniSwitch10000Q8 = _GniOmniSwitch10000Q8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    gniOmniSwitch10000Q8.setStatus("current")
_GniOmniSwitch10000Q4_ObjectIdentity = ObjectIdentity
gniOmniSwitch10000Q4 = _GniOmniSwitch10000Q4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    gniOmniSwitch10000Q4.setStatus("current")
_CfmOmniSwitch10000_ObjectIdentity = ObjectIdentity
cfmOmniSwitch10000 = _CfmOmniSwitch10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 3)
)
if mibBuilder.loadTexts:
    cfmOmniSwitch10000.setStatus("current")
_CfmOmniSwitch10000CFM_ObjectIdentity = ObjectIdentity
cfmOmniSwitch10000CFM = _CfmOmniSwitch10000CFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cfmOmniSwitch10000CFM.setStatus("current")
_CfmOmniSwitch10000CFMOnly_ObjectIdentity = ObjectIdentity
cfmOmniSwitch10000CFMOnly = _CfmOmniSwitch10000CFMOnly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 9, 4, 3, 2)
)
if mibBuilder.loadTexts:
    cfmOmniSwitch10000CFMOnly.setStatus("current")
_FamilyOmniSwitch6900_ObjectIdentity = ObjectIdentity
familyOmniSwitch6900 = _FamilyOmniSwitch6900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    familyOmniSwitch6900.setStatus("current")
_ChassisOmniSwitch6900_ObjectIdentity = ObjectIdentity
chassisOmniSwitch6900 = _ChassisOmniSwitch6900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch6900.setStatus("current")
_DeviceOmniSwitch6900X20_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6900X20 = _DeviceOmniSwitch6900X20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6900X20.setStatus("current")
_DeviceOmniSwitch6900X40_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6900X40 = _DeviceOmniSwitch6900X40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6900X40.setStatus("current")
_DeviceOmniSwitch6900T20_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6900T20 = _DeviceOmniSwitch6900T20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6900T20.setStatus("current")
_DeviceOmniSwitch6900T40_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6900T40 = _DeviceOmniSwitch6900T40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6900T40.setStatus("current")
_FansOmniSwitch6900_ObjectIdentity = ObjectIdentity
fansOmniSwitch6900 = _FansOmniSwitch6900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch6900.setStatus("current")
_PowersOmniSwitch6900_ObjectIdentity = ObjectIdentity
powersOmniSwitch6900 = _PowersOmniSwitch6900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6900.setStatus("current")
_PowersOmniSwitch6900AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch6900AC = _PowersOmniSwitch6900AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6900AC.setStatus("current")
_PowersOmniSwitch6900DC_ObjectIdentity = ObjectIdentity
powersOmniSwitch6900DC = _PowersOmniSwitch6900DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 3, 2)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6900DC.setStatus("current")
_PowersOmniSwitch6900ACRF_ObjectIdentity = ObjectIdentity
powersOmniSwitch6900ACRF = _PowersOmniSwitch6900ACRF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 3, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6900ACRF.setStatus("current")
_PowersOmniSwitch6900DCRF_ObjectIdentity = ObjectIdentity
powersOmniSwitch6900DCRF = _PowersOmniSwitch6900DCRF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 3, 4)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6900DCRF.setStatus("current")
_ModulesOmniSwitch6900_ObjectIdentity = ObjectIdentity
modulesOmniSwitch6900 = _ModulesOmniSwitch6900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch6900.setStatus("current")
_DaughterBoardOmniSwitch6900_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6900 = _DaughterBoardOmniSwitch6900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 5)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6900.setStatus("current")
_DaughterBoardOmniSwitch6900XNI_U12_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6900XNI_U12 = _DaughterBoardOmniSwitch6900XNI_U12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 5, 1)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6900XNI_U12.setStatus("current")
_DaughterBoardOmniSwitch6900XNI_U4_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6900XNI_U4 = _DaughterBoardOmniSwitch6900XNI_U4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 5, 2)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6900XNI_U4.setStatus("current")
_DaughterBoardOmniSwitch6900QNI_U3_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6900QNI_U3 = _DaughterBoardOmniSwitch6900QNI_U3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 5, 3)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6900QNI_U3.setStatus("current")
_DaughterBoardOmniSwitch6900HNI_U6_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6900HNI_U6 = _DaughterBoardOmniSwitch6900HNI_U6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 5, 4)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6900HNI_U6.setStatus("current")
_DaughterBoardOmniSwitch6900XNI_T8_ObjectIdentity = ObjectIdentity
daughterBoardOmniSwitch6900XNI_T8 = _DaughterBoardOmniSwitch6900XNI_T8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 10, 5, 5)
)
if mibBuilder.loadTexts:
    daughterBoardOmniSwitch6900XNI_T8.setStatus("current")
_FamilyOmniSwitch6860_ObjectIdentity = ObjectIdentity
familyOmniSwitch6860 = _FamilyOmniSwitch6860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    familyOmniSwitch6860.setStatus("current")
_ChassisOmniSwitch6860_ObjectIdentity = ObjectIdentity
chassisOmniSwitch6860 = _ChassisOmniSwitch6860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    chassisOmniSwitch6860.setStatus("current")
_DeviceOmniSwitch6860_24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6860_24 = _DeviceOmniSwitch6860_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6860_24.setStatus("current")
_DeviceOmniSwitch6860_P24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6860_P24 = _DeviceOmniSwitch6860_P24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6860_P24.setStatus("current")
_DeviceOmniSwitch6860_48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6860_48 = _DeviceOmniSwitch6860_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6860_48.setStatus("current")
_DeviceOmniSwitch6860_P48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6860_P48 = _DeviceOmniSwitch6860_P48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6860_P48.setStatus("current")
_DeviceOmniSwitch6860E_24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6860E_24 = _DeviceOmniSwitch6860E_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6860E_24.setStatus("current")
_DeviceOmniSwitch6860E_P24_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6860E_P24 = _DeviceOmniSwitch6860E_P24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 1, 6)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6860E_P24.setStatus("current")
_DeviceOmniSwitch6860E_48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6860E_48 = _DeviceOmniSwitch6860E_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 1, 7)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6860E_48.setStatus("current")
_DeviceOmniSwitch6860E_P48_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6860E_P48 = _DeviceOmniSwitch6860E_P48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 1, 8)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6860E_P48.setStatus("current")
_DeviceOmniSwitch6860U_28_ObjectIdentity = ObjectIdentity
deviceOmniSwitch6860U_28 = _DeviceOmniSwitch6860U_28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 1, 9)
)
if mibBuilder.loadTexts:
    deviceOmniSwitch6860U_28.setStatus("current")
_FansOmniSwitch6860_ObjectIdentity = ObjectIdentity
fansOmniSwitch6860 = _FansOmniSwitch6860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 2)
)
if mibBuilder.loadTexts:
    fansOmniSwitch6860.setStatus("current")
_PowersOmniSwitch6860_ObjectIdentity = ObjectIdentity
powersOmniSwitch6860 = _PowersOmniSwitch6860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6860.setStatus("current")
_PowersOmniSwitch6860AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch6860AC = _PowersOmniSwitch6860AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6860AC.setStatus("current")
_PowersOmniSwitch6860DC_ObjectIdentity = ObjectIdentity
powersOmniSwitch6860DC = _PowersOmniSwitch6860DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 3, 2)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6860DC.setStatus("current")
_PowersOmniSwitch6860POE600_AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch6860POE600_AC = _PowersOmniSwitch6860POE600_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 3, 3)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6860POE600_AC.setStatus("current")
_PowersOmniSwitch6860POE920_AC_ObjectIdentity = ObjectIdentity
powersOmniSwitch6860POE920_AC = _PowersOmniSwitch6860POE920_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 3, 4)
)
if mibBuilder.loadTexts:
    powersOmniSwitch6860POE920_AC.setStatus("current")
_ModulesOmniSwitch6860_ObjectIdentity = ObjectIdentity
modulesOmniSwitch6860 = _ModulesOmniSwitch6860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 4)
)
if mibBuilder.loadTexts:
    modulesOmniSwitch6860.setStatus("current")
_ExternBoardOmniSwitch6860_ObjectIdentity = ObjectIdentity
externBoardOmniSwitch6860 = _ExternBoardOmniSwitch6860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 5)
)
if mibBuilder.loadTexts:
    externBoardOmniSwitch6860.setStatus("current")
_ExternBoardOmniSwitch6860CPU_ObjectIdentity = ObjectIdentity
externBoardOmniSwitch6860CPU = _ExternBoardOmniSwitch6860CPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2, 1, 11, 5, 1)
)
if mibBuilder.loadTexts:
    externBoardOmniSwitch6860CPU.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DEVICES",
    **{"alcatelIND1DevicesMIB": alcatelIND1DevicesMIB,
       "familyOmniSwitch10000": familyOmniSwitch10000,
       "chassisOmniSwitch10000": chassisOmniSwitch10000,
       "deviceOmniSwitch10000": deviceOmniSwitch10000,
       "fansOmniSwitch10000": fansOmniSwitch10000,
       "fansOmniSwitch10000FT": fansOmniSwitch10000FT,
       "powersOmniSwitch10000": powersOmniSwitch10000,
       "powersOmniSwitch10000AC": powersOmniSwitch10000AC,
       "powersOmniSwitch10000DC": powersOmniSwitch10000DC,
       "modulesOmniSwitch10000": modulesOmniSwitch10000,
       "modulesOmniSwitch10000CM": modulesOmniSwitch10000CM,
       "cmmOmniSwitch10000": cmmOmniSwitch10000,
       "cmmOmniSwitch10000PROC": cmmOmniSwitch10000PROC,
       "modulesOmniSwitch10000NI": modulesOmniSwitch10000NI,
       "niOmniSwitch10000GNI": niOmniSwitch10000GNI,
       "gniOmniSwitch10000C48": gniOmniSwitch10000C48,
       "gniOmniSwitch10000U48": gniOmniSwitch10000U48,
       "niOmniSwitch10000XNI": niOmniSwitch10000XNI,
       "gniOmniSwitch10000X16M": gniOmniSwitch10000X16M,
       "gniOmniSwitch10000X32M": gniOmniSwitch10000X32M,
       "gniOmniSwitch10000X16E": gniOmniSwitch10000X16E,
       "gniOmniSwitch10000X16L": gniOmniSwitch10000X16L,
       "gniOmniSwitch10000X32E": gniOmniSwitch10000X32E,
       "niOmniSwitch10000QNI": niOmniSwitch10000QNI,
       "gniOmniSwitch10000Q8": gniOmniSwitch10000Q8,
       "gniOmniSwitch10000Q4": gniOmniSwitch10000Q4,
       "cfmOmniSwitch10000": cfmOmniSwitch10000,
       "cfmOmniSwitch10000CFM": cfmOmniSwitch10000CFM,
       "cfmOmniSwitch10000CFMOnly": cfmOmniSwitch10000CFMOnly,
       "familyOmniSwitch6900": familyOmniSwitch6900,
       "chassisOmniSwitch6900": chassisOmniSwitch6900,
       "deviceOmniSwitch6900X20": deviceOmniSwitch6900X20,
       "deviceOmniSwitch6900X40": deviceOmniSwitch6900X40,
       "deviceOmniSwitch6900T20": deviceOmniSwitch6900T20,
       "deviceOmniSwitch6900T40": deviceOmniSwitch6900T40,
       "fansOmniSwitch6900": fansOmniSwitch6900,
       "powersOmniSwitch6900": powersOmniSwitch6900,
       "powersOmniSwitch6900AC": powersOmniSwitch6900AC,
       "powersOmniSwitch6900DC": powersOmniSwitch6900DC,
       "powersOmniSwitch6900ACRF": powersOmniSwitch6900ACRF,
       "powersOmniSwitch6900DCRF": powersOmniSwitch6900DCRF,
       "modulesOmniSwitch6900": modulesOmniSwitch6900,
       "daughterBoardOmniSwitch6900": daughterBoardOmniSwitch6900,
       "daughterBoardOmniSwitch6900XNI-U12": daughterBoardOmniSwitch6900XNI_U12,
       "daughterBoardOmniSwitch6900XNI-U4": daughterBoardOmniSwitch6900XNI_U4,
       "daughterBoardOmniSwitch6900QNI-U3": daughterBoardOmniSwitch6900QNI_U3,
       "daughterBoardOmniSwitch6900HNI-U6": daughterBoardOmniSwitch6900HNI_U6,
       "daughterBoardOmniSwitch6900XNI-T8": daughterBoardOmniSwitch6900XNI_T8,
       "familyOmniSwitch6860": familyOmniSwitch6860,
       "chassisOmniSwitch6860": chassisOmniSwitch6860,
       "deviceOmniSwitch6860-24": deviceOmniSwitch6860_24,
       "deviceOmniSwitch6860-P24": deviceOmniSwitch6860_P24,
       "deviceOmniSwitch6860-48": deviceOmniSwitch6860_48,
       "deviceOmniSwitch6860-P48": deviceOmniSwitch6860_P48,
       "deviceOmniSwitch6860E-24": deviceOmniSwitch6860E_24,
       "deviceOmniSwitch6860E-P24": deviceOmniSwitch6860E_P24,
       "deviceOmniSwitch6860E-48": deviceOmniSwitch6860E_48,
       "deviceOmniSwitch6860E-P48": deviceOmniSwitch6860E_P48,
       "deviceOmniSwitch6860U-28": deviceOmniSwitch6860U_28,
       "fansOmniSwitch6860": fansOmniSwitch6860,
       "powersOmniSwitch6860": powersOmniSwitch6860,
       "powersOmniSwitch6860AC": powersOmniSwitch6860AC,
       "powersOmniSwitch6860DC": powersOmniSwitch6860DC,
       "powersOmniSwitch6860POE600-AC": powersOmniSwitch6860POE600_AC,
       "powersOmniSwitch6860POE920-AC": powersOmniSwitch6860POE920_AC,
       "modulesOmniSwitch6860": modulesOmniSwitch6860,
       "externBoardOmniSwitch6860": externBoardOmniSwitch6860,
       "externBoardOmniSwitch6860CPU": externBoardOmniSwitch6860CPU}
)
