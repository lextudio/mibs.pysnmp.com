# SNMP MIB module (HUAWEI-BRAS-PPPoX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-PPPoX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:03 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwBRASPPPoX = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwPPPoXMibObjects_ObjectIdentity = ObjectIdentity
hwPPPoXMibObjects = _HwPPPoXMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1)
)
_HwPppConfigTable_Object = MibTable
hwPppConfigTable = _HwPppConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwPppConfigTable.setStatus("current")
_HwPppConfigEntry_Object = MibTableRow
hwPppConfigEntry = _HwPppConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1)
)
hwPppConfigEntry.setIndexNames(
    (0, "HUAWEI-BRAS-PPPoX-MIB", "hwVtIndex"),
)
if mibBuilder.loadTexts:
    hwPppConfigEntry.setStatus("current")


class _HwVtIndex_Type(Integer32):
    """Custom type hwVtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwVtIndex_Type.__name__ = "Integer32"
_HwVtIndex_Object = MibTableColumn
hwVtIndex = _HwVtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 1),
    _HwVtIndex_Type()
)
hwVtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVtIndex.setStatus("current")


class _HwPppAuthMode_Type(Integer32):
    """Custom type hwPppAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("chap", 1),
          ("mschapv1", 3),
          ("mschapv2", 4),
          ("pap", 0))
    )


_HwPppAuthMode_Type.__name__ = "Integer32"
_HwPppAuthMode_Object = MibTableColumn
hwPppAuthMode = _HwPppAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 2),
    _HwPppAuthMode_Type()
)
hwPppAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppAuthMode.setStatus("current")


class _HwPppNegTimeout_Type(Integer32):
    """Custom type hwPppNegTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwPppNegTimeout_Type.__name__ = "Integer32"
_HwPppNegTimeout_Object = MibTableColumn
hwPppNegTimeout = _HwPppNegTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 3),
    _HwPppNegTimeout_Type()
)
hwPppNegTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppNegTimeout.setStatus("current")


class _HwPppKeepInterval_Type(Integer32):
    """Custom type hwPppKeepInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPppKeepInterval_Type.__name__ = "Integer32"
_HwPppKeepInterval_Object = MibTableColumn
hwPppKeepInterval = _HwPppKeepInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 4),
    _HwPppKeepInterval_Type()
)
hwPppKeepInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppKeepInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwPppKeepInterval.setUnits("seconds")


class _HwPppKeepRetransmit_Type(Integer32):
    """Custom type hwPppKeepRetransmit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwPppKeepRetransmit_Type.__name__ = "Integer32"
_HwPppKeepRetransmit_Object = MibTableColumn
hwPppKeepRetransmit = _HwPppKeepRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 5),
    _HwPppKeepRetransmit_Type()
)
hwPppKeepRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppKeepRetransmit.setStatus("current")


class _HwPppCHAPUserName_Type(OctetString):
    """Custom type hwPppCHAPUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_HwPppCHAPUserName_Type.__name__ = "OctetString"
_HwPppCHAPUserName_Object = MibTableColumn
hwPppCHAPUserName = _HwPppCHAPUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 6),
    _HwPppCHAPUserName_Type()
)
hwPppCHAPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppCHAPUserName.setStatus("current")


class _HwPppCHAPUserPassword_Type(OctetString):
    """Custom type hwPppCHAPUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwPppCHAPUserPassword_Type.__name__ = "OctetString"
_HwPppCHAPUserPassword_Object = MibTableColumn
hwPppCHAPUserPassword = _HwPppCHAPUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 7),
    _HwPppCHAPUserPassword_Type()
)
hwPppCHAPUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppCHAPUserPassword.setStatus("current")


class _HwPppPAPUserName_Type(OctetString):
    """Custom type hwPppPAPUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_HwPppPAPUserName_Type.__name__ = "OctetString"
_HwPppPAPUserName_Object = MibTableColumn
hwPppPAPUserName = _HwPppPAPUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 8),
    _HwPppPAPUserName_Type()
)
hwPppPAPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppPAPUserName.setStatus("current")


class _HwPppPAPUserPassword_Type(OctetString):
    """Custom type hwPppPAPUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwPppPAPUserPassword_Type.__name__ = "OctetString"
_HwPppPAPUserPassword_Object = MibTableColumn
hwPppPAPUserPassword = _HwPppPAPUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 9),
    _HwPppPAPUserPassword_Type()
)
hwPppPAPUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppPAPUserPassword.setStatus("current")


class _HwPppServiceName1_Type(OctetString):
    """Custom type hwPppServiceName1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPppServiceName1_Type.__name__ = "OctetString"
_HwPppServiceName1_Object = MibTableColumn
hwPppServiceName1 = _HwPppServiceName1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 10),
    _HwPppServiceName1_Type()
)
hwPppServiceName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppServiceName1.setStatus("current")


class _HwPppServiceName2_Type(OctetString):
    """Custom type hwPppServiceName2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPppServiceName2_Type.__name__ = "OctetString"
_HwPppServiceName2_Object = MibTableColumn
hwPppServiceName2 = _HwPppServiceName2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 11),
    _HwPppServiceName2_Type()
)
hwPppServiceName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppServiceName2.setStatus("current")


class _HwPppServiceName3_Type(OctetString):
    """Custom type hwPppServiceName3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPppServiceName3_Type.__name__ = "OctetString"
_HwPppServiceName3_Object = MibTableColumn
hwPppServiceName3 = _HwPppServiceName3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 12),
    _HwPppServiceName3_Type()
)
hwPppServiceName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppServiceName3.setStatus("current")


class _HwPppServiceName4_Type(OctetString):
    """Custom type hwPppServiceName4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPppServiceName4_Type.__name__ = "OctetString"
_HwPppServiceName4_Object = MibTableColumn
hwPppServiceName4 = _HwPppServiceName4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 13),
    _HwPppServiceName4_Type()
)
hwPppServiceName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppServiceName4.setStatus("current")


class _HwPppServiceName5_Type(OctetString):
    """Custom type hwPppServiceName5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPppServiceName5_Type.__name__ = "OctetString"
_HwPppServiceName5_Object = MibTableColumn
hwPppServiceName5 = _HwPppServiceName5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 14),
    _HwPppServiceName5_Type()
)
hwPppServiceName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppServiceName5.setStatus("current")


class _HwPppServiceName6_Type(OctetString):
    """Custom type hwPppServiceName6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPppServiceName6_Type.__name__ = "OctetString"
_HwPppServiceName6_Object = MibTableColumn
hwPppServiceName6 = _HwPppServiceName6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 15),
    _HwPppServiceName6_Type()
)
hwPppServiceName6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppServiceName6.setStatus("current")


class _HwPppServiceName7_Type(OctetString):
    """Custom type hwPppServiceName7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPppServiceName7_Type.__name__ = "OctetString"
_HwPppServiceName7_Object = MibTableColumn
hwPppServiceName7 = _HwPppServiceName7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 16),
    _HwPppServiceName7_Type()
)
hwPppServiceName7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppServiceName7.setStatus("current")


class _HwPppServiceName8_Type(OctetString):
    """Custom type hwPppServiceName8 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPppServiceName8_Type.__name__ = "OctetString"
_HwPppServiceName8_Object = MibTableColumn
hwPppServiceName8 = _HwPppServiceName8_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 17),
    _HwPppServiceName8_Type()
)
hwPppServiceName8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppServiceName8.setStatus("current")


class _HwPppServiceNameType_Type(Integer32):
    """Custom type hwPppServiceNameType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exactMatch", 1),
          ("normalMatch", 2))
    )


_HwPppServiceNameType_Type.__name__ = "Integer32"
_HwPppServiceNameType_Object = MibTableColumn
hwPppServiceNameType = _HwPppServiceNameType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 18),
    _HwPppServiceNameType_Type()
)
hwPppServiceNameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppServiceNameType.setStatus("current")


class _HwPppAcName_Type(OctetString):
    """Custom type hwPppAcName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPppAcName_Type.__name__ = "OctetString"
_HwPppAcName_Object = MibTableColumn
hwPppAcName = _HwPppAcName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 1, 1, 19),
    _HwPppAcName_Type()
)
hwPppAcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPppAcName.setStatus("current")
_HwPppVTBindTable_Object = MibTable
hwPppVTBindTable = _HwPppVTBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwPppVTBindTable.setStatus("current")
_HwPppVTBindEntry_Object = MibTableRow
hwPppVTBindEntry = _HwPppVTBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 2, 1)
)
hwPppVTBindEntry.setIndexNames(
    (0, "HUAWEI-BRAS-PPPoX-MIB", "hwPppVTBindIfIndex"),
)
if mibBuilder.loadTexts:
    hwPppVTBindEntry.setStatus("current")
_HwPppVTBindIfIndex_Type = InterfaceIndex
_HwPppVTBindIfIndex_Object = MibTableColumn
hwPppVTBindIfIndex = _HwPppVTBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 2, 1, 1),
    _HwPppVTBindIfIndex_Type()
)
hwPppVTBindIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPppVTBindIfIndex.setStatus("current")


class _HwVtNumber_Type(Integer32):
    """Custom type hwVtNumber based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
        ValueRangeConstraint(65535, 65535),
    )


_HwVtNumber_Type.__name__ = "Integer32"
_HwVtNumber_Object = MibTableColumn
hwVtNumber = _HwVtNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 1, 2, 1, 2),
    _HwVtNumber_Type()
)
hwVtNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVtNumber.setStatus("current")
_HwPppConformance_ObjectIdentity = ObjectIdentity
hwPppConformance = _HwPppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 2)
)
_HwPppCompliances_ObjectIdentity = ObjectIdentity
hwPppCompliances = _HwPppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 2, 1)
)
_HwPppGroups_ObjectIdentity = ObjectIdentity
hwPppGroups = _HwPppGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 2, 2)
)

# Managed Objects groups

hwPppConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 2, 2, 1)
)
hwPppConfigGroup.setObjects(
      *(("HUAWEI-BRAS-PPPoX-MIB", "hwVtIndex"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppAuthMode"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppNegTimeout"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppKeepInterval"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppKeepRetransmit"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppCHAPUserName"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppCHAPUserPassword"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppPAPUserName"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppPAPUserPassword"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppServiceName1"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppServiceName2"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppServiceName3"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppServiceName4"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppServiceName5"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppServiceName6"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppServiceName7"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppServiceName8"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppServiceNameType"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwPppAcName"))
)
if mibBuilder.loadTexts:
    hwPppConfigGroup.setStatus("current")

hwPppVTBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 2, 2, 2)
)
hwPppVTBindGroup.setObjects(
      *(("HUAWEI-BRAS-PPPoX-MIB", "hwPppVTBindIfIndex"),
        ("HUAWEI-BRAS-PPPoX-MIB", "hwVtNumber"))
)
if mibBuilder.loadTexts:
    hwPppVTBindGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwPppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwPppCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-PPPoX-MIB",
    **{"hwBRASPPPoX": hwBRASPPPoX,
       "hwPPPoXMibObjects": hwPPPoXMibObjects,
       "hwPppConfigTable": hwPppConfigTable,
       "hwPppConfigEntry": hwPppConfigEntry,
       "hwVtIndex": hwVtIndex,
       "hwPppAuthMode": hwPppAuthMode,
       "hwPppNegTimeout": hwPppNegTimeout,
       "hwPppKeepInterval": hwPppKeepInterval,
       "hwPppKeepRetransmit": hwPppKeepRetransmit,
       "hwPppCHAPUserName": hwPppCHAPUserName,
       "hwPppCHAPUserPassword": hwPppCHAPUserPassword,
       "hwPppPAPUserName": hwPppPAPUserName,
       "hwPppPAPUserPassword": hwPppPAPUserPassword,
       "hwPppServiceName1": hwPppServiceName1,
       "hwPppServiceName2": hwPppServiceName2,
       "hwPppServiceName3": hwPppServiceName3,
       "hwPppServiceName4": hwPppServiceName4,
       "hwPppServiceName5": hwPppServiceName5,
       "hwPppServiceName6": hwPppServiceName6,
       "hwPppServiceName7": hwPppServiceName7,
       "hwPppServiceName8": hwPppServiceName8,
       "hwPppServiceNameType": hwPppServiceNameType,
       "hwPppAcName": hwPppAcName,
       "hwPppVTBindTable": hwPppVTBindTable,
       "hwPppVTBindEntry": hwPppVTBindEntry,
       "hwPppVTBindIfIndex": hwPppVTBindIfIndex,
       "hwVtNumber": hwVtNumber,
       "hwPppConformance": hwPppConformance,
       "hwPppCompliances": hwPppCompliances,
       "hwPppCompliance": hwPppCompliance,
       "hwPppGroups": hwPppGroups,
       "hwPppConfigGroup": hwPppConfigGroup,
       "hwPppVTBindGroup": hwPppVTBindGroup}
)
