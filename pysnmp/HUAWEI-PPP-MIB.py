# SNMP MIB module (HUAWEI-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:36 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwPppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwPppObjects_ObjectIdentity = ObjectIdentity
hwPppObjects = _HwPppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1)
)
_HwPppConfigTable_Object = MibTable
hwPppConfigTable = _HwPppConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 1)
)
if mibBuilder.loadTexts:
    hwPppConfigTable.setStatus("current")
_HwPppConfigEntry_Object = MibTableRow
hwPppConfigEntry = _HwPppConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 1, 1)
)
hwPppConfigEntry.setIndexNames(
    (0, "HUAWEI-PPP-MIB", "hwPppIfIndex"),
)
if mibBuilder.loadTexts:
    hwPppConfigEntry.setStatus("current")
_HwPppIfIndex_Type = InterfaceIndex
_HwPppIfIndex_Object = MibTableColumn
hwPppIfIndex = _HwPppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 1, 1, 1),
    _HwPppIfIndex_Type()
)
hwPppIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPppIfIndex.setStatus("current")


class _HwPppMruNegType_Type(Integer32):
    """Custom type hwPppMruNegType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_HwPppMruNegType_Type.__name__ = "Integer32"
_HwPppMruNegType_Object = MibTableColumn
hwPppMruNegType = _HwPppMruNegType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 1, 1, 11),
    _HwPppMruNegType_Type()
)
hwPppMruNegType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppMruNegType.setStatus("current")
_HwPppMpIfIndex_Type = Integer32
_HwPppMpIfIndex_Object = MibTableColumn
hwPppMpIfIndex = _HwPppMpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 1, 1, 12),
    _HwPppMpIfIndex_Type()
)
hwPppMpIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppMpIfIndex.setStatus("current")
_HwPppAuthenticateTable_Object = MibTable
hwPppAuthenticateTable = _HwPppAuthenticateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2)
)
if mibBuilder.loadTexts:
    hwPppAuthenticateTable.setStatus("current")
_HwPppAuthenticateEntry_Object = MibTableRow
hwPppAuthenticateEntry = _HwPppAuthenticateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1)
)
hwPppAuthenticateEntry.setIndexNames(
    (0, "HUAWEI-PPP-MIB", "hwPppIfIndex"),
)
if mibBuilder.loadTexts:
    hwPppAuthenticateEntry.setStatus("current")


class _HwPppAuthenticateMode_Type(Integer32):
    """Custom type hwPppAuthenticateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("chappap", 3),
          ("pap", 2))
    )


_HwPppAuthenticateMode_Type.__name__ = "Integer32"
_HwPppAuthenticateMode_Object = MibTableColumn
hwPppAuthenticateMode = _HwPppAuthenticateMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 11),
    _HwPppAuthenticateMode_Type()
)
hwPppAuthenticateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppAuthenticateMode.setStatus("current")


class _HwPppAuthenticateChapUserName_Type(OctetString):
    """Custom type hwPppAuthenticateChapUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwPppAuthenticateChapUserName_Type.__name__ = "OctetString"
_HwPppAuthenticateChapUserName_Object = MibTableColumn
hwPppAuthenticateChapUserName = _HwPppAuthenticateChapUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 12),
    _HwPppAuthenticateChapUserName_Type()
)
hwPppAuthenticateChapUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppAuthenticateChapUserName.setStatus("current")


class _HwPppAuthenticateChapPwType_Type(Integer32):
    """Custom type hwPppAuthenticateChapPwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 1),
          ("simple", 2))
    )


_HwPppAuthenticateChapPwType_Type.__name__ = "Integer32"
_HwPppAuthenticateChapPwType_Object = MibTableColumn
hwPppAuthenticateChapPwType = _HwPppAuthenticateChapPwType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 13),
    _HwPppAuthenticateChapPwType_Type()
)
hwPppAuthenticateChapPwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppAuthenticateChapPwType.setStatus("current")


class _HwPppAuthenticateChapPw_Type(OctetString):
    """Custom type hwPppAuthenticateChapPw based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
        ValueSizeConstraint(24, 24),
    )


_HwPppAuthenticateChapPw_Type.__name__ = "OctetString"
_HwPppAuthenticateChapPw_Object = MibTableColumn
hwPppAuthenticateChapPw = _HwPppAuthenticateChapPw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 14),
    _HwPppAuthenticateChapPw_Type()
)
hwPppAuthenticateChapPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppAuthenticateChapPw.setStatus("current")


class _HwPppAuthenticatePapUserName_Type(OctetString):
    """Custom type hwPppAuthenticatePapUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwPppAuthenticatePapUserName_Type.__name__ = "OctetString"
_HwPppAuthenticatePapUserName_Object = MibTableColumn
hwPppAuthenticatePapUserName = _HwPppAuthenticatePapUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 15),
    _HwPppAuthenticatePapUserName_Type()
)
hwPppAuthenticatePapUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppAuthenticatePapUserName.setStatus("current")


class _HwPppAuthenticatePapPwType_Type(Integer32):
    """Custom type hwPppAuthenticatePapPwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 1),
          ("simple", 2))
    )


_HwPppAuthenticatePapPwType_Type.__name__ = "Integer32"
_HwPppAuthenticatePapPwType_Object = MibTableColumn
hwPppAuthenticatePapPwType = _HwPppAuthenticatePapPwType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 16),
    _HwPppAuthenticatePapPwType_Type()
)
hwPppAuthenticatePapPwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppAuthenticatePapPwType.setStatus("current")


class _HwPppAuthenticatePapPw_Type(OctetString):
    """Custom type hwPppAuthenticatePapPw based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
        ValueSizeConstraint(24, 24),
    )


_HwPppAuthenticatePapPw_Type.__name__ = "OctetString"
_HwPppAuthenticatePapPw_Object = MibTableColumn
hwPppAuthenticatePapPw = _HwPppAuthenticatePapPw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 17),
    _HwPppAuthenticatePapPw_Type()
)
hwPppAuthenticatePapPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppAuthenticatePapPw.setStatus("current")
_HwPppConformance_ObjectIdentity = ObjectIdentity
hwPppConformance = _HwPppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11)
)
_HwPppCompliances_ObjectIdentity = ObjectIdentity
hwPppCompliances = _HwPppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11, 1)
)
_HwPppGroups_ObjectIdentity = ObjectIdentity
hwPppGroups = _HwPppGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11, 2)
)

# Managed Objects groups

hwPppConfigObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11, 2, 1)
)
hwPppConfigObjectGroup.setObjects(
      *(("HUAWEI-PPP-MIB", "hwPppMruNegType"),
        ("HUAWEI-PPP-MIB", "hwPppMpIfIndex"))
)
if mibBuilder.loadTexts:
    hwPppConfigObjectGroup.setStatus("current")

hwPppAuthenticateObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11, 2, 2)
)
hwPppAuthenticateObjectGroup.setObjects(
      *(("HUAWEI-PPP-MIB", "hwPppAuthenticateMode"),
        ("HUAWEI-PPP-MIB", "hwPppAuthenticateChapUserName"),
        ("HUAWEI-PPP-MIB", "hwPppAuthenticateChapPwType"),
        ("HUAWEI-PPP-MIB", "hwPppAuthenticateChapPw"),
        ("HUAWEI-PPP-MIB", "hwPppAuthenticatePapUserName"),
        ("HUAWEI-PPP-MIB", "hwPppAuthenticatePapPwType"),
        ("HUAWEI-PPP-MIB", "hwPppAuthenticatePapPw"))
)
if mibBuilder.loadTexts:
    hwPppAuthenticateObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwPppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11, 1, 1)
)
if mibBuilder.loadTexts:
    hwPppCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PPP-MIB",
    **{"hwPppMIB": hwPppMIB,
       "hwPppObjects": hwPppObjects,
       "hwPppConfigTable": hwPppConfigTable,
       "hwPppConfigEntry": hwPppConfigEntry,
       "hwPppIfIndex": hwPppIfIndex,
       "hwPppMruNegType": hwPppMruNegType,
       "hwPppMpIfIndex": hwPppMpIfIndex,
       "hwPppAuthenticateTable": hwPppAuthenticateTable,
       "hwPppAuthenticateEntry": hwPppAuthenticateEntry,
       "hwPppAuthenticateMode": hwPppAuthenticateMode,
       "hwPppAuthenticateChapUserName": hwPppAuthenticateChapUserName,
       "hwPppAuthenticateChapPwType": hwPppAuthenticateChapPwType,
       "hwPppAuthenticateChapPw": hwPppAuthenticateChapPw,
       "hwPppAuthenticatePapUserName": hwPppAuthenticatePapUserName,
       "hwPppAuthenticatePapPwType": hwPppAuthenticatePapPwType,
       "hwPppAuthenticatePapPw": hwPppAuthenticatePapPw,
       "hwPppConformance": hwPppConformance,
       "hwPppCompliances": hwPppCompliances,
       "hwPppCompliance": hwPppCompliance,
       "hwPppGroups": hwPppGroups,
       "hwPppConfigObjectGroup": hwPppConfigObjectGroup,
       "hwPppAuthenticateObjectGroup": hwPppAuthenticateObjectGroup}
)
