# SNMP MIB module (HP-ICF-INST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-INST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:31 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfInstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45)
)
hpicfInstMIB.setRevisions(
        ("2007-09-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfInstObjects_ObjectIdentity = ObjectIdentity
hpicfInstObjects = _HpicfInstObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1)
)


class _HpicfInstEnable_Type(TruthValue):
    """Custom type hpicfInstEnable based on TruthValue"""


_HpicfInstEnable_Object = MibScalar
hpicfInstEnable = _HpicfInstEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 1),
    _HpicfInstEnable_Type()
)
hpicfInstEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInstEnable.setStatus("current")


class _HpicfInstMaxMemMB_Type(Integer32):
    """Custom type hpicfInstMaxMemMB based on Integer32"""
    defaultValue = 2


_HpicfInstMaxMemMB_Object = MibScalar
hpicfInstMaxMemMB = _HpicfInstMaxMemMB_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 2),
    _HpicfInstMaxMemMB_Type()
)
hpicfInstMaxMemMB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfInstMaxMemMB.setStatus("current")
_HpicfInstParameterTable_Object = MibTable
hpicfInstParameterTable = _HpicfInstParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfInstParameterTable.setStatus("current")
_HpicfInstParameterEntry_Object = MibTableRow
hpicfInstParameterEntry = _HpicfInstParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 3, 1)
)
hpicfInstParameterEntry.setIndexNames(
    (0, "HP-ICF-INST-MIB", "hpicfInstParameterIndex"),
    (0, "HP-ICF-INST-MIB", "hpicfInstInterfaceIndex"),
    (0, "HP-ICF-INST-MIB", "hpicfInstIntervalIndex"),
)
if mibBuilder.loadTexts:
    hpicfInstParameterEntry.setStatus("current")


class _HpicfInstParameterIndex_Type(Integer32):
    """Custom type hpicfInstParameterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfInstParameterIndex_Type.__name__ = "Integer32"
_HpicfInstParameterIndex_Object = MibTableColumn
hpicfInstParameterIndex = _HpicfInstParameterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 3, 1, 1),
    _HpicfInstParameterIndex_Type()
)
hpicfInstParameterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfInstParameterIndex.setStatus("current")


class _HpicfInstInterfaceIndex_Type(Integer32):
    """Custom type hpicfInstInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfInstInterfaceIndex_Type.__name__ = "Integer32"
_HpicfInstInterfaceIndex_Object = MibTableColumn
hpicfInstInterfaceIndex = _HpicfInstInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 3, 1, 2),
    _HpicfInstInterfaceIndex_Type()
)
hpicfInstInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfInstInterfaceIndex.setStatus("current")


class _HpicfInstIntervalIndex_Type(Integer32):
    """Custom type hpicfInstIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfInstIntervalIndex_Type.__name__ = "Integer32"
_HpicfInstIntervalIndex_Object = MibTableColumn
hpicfInstIntervalIndex = _HpicfInstIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 3, 1, 3),
    _HpicfInstIntervalIndex_Type()
)
hpicfInstIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfInstIntervalIndex.setStatus("current")


class _HpicfInstParameterName_Type(DisplayString):
    """Custom type hpicfInstParameterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HpicfInstParameterName_Type.__name__ = "DisplayString"
_HpicfInstParameterName_Object = MibTableColumn
hpicfInstParameterName = _HpicfInstParameterName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 3, 1, 4),
    _HpicfInstParameterName_Type()
)
hpicfInstParameterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInstParameterName.setStatus("current")


class _HpicfInstIntervalName_Type(DisplayString):
    """Custom type hpicfInstIntervalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HpicfInstIntervalName_Type.__name__ = "DisplayString"
_HpicfInstIntervalName_Object = MibTableColumn
hpicfInstIntervalName = _HpicfInstIntervalName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 3, 1, 5),
    _HpicfInstIntervalName_Type()
)
hpicfInstIntervalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInstIntervalName.setStatus("current")
_HpicfInstParameterValue_Type = Unsigned32
_HpicfInstParameterValue_Object = MibTableColumn
hpicfInstParameterValue = _HpicfInstParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 3, 1, 6),
    _HpicfInstParameterValue_Type()
)
hpicfInstParameterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInstParameterValue.setStatus("current")
_HpicfInstParamValMin_Type = Unsigned32
_HpicfInstParamValMin_Object = MibTableColumn
hpicfInstParamValMin = _HpicfInstParamValMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 3, 1, 7),
    _HpicfInstParamValMin_Type()
)
hpicfInstParamValMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInstParamValMin.setStatus("current")
_HpicfInstParamValMax_Type = Unsigned32
_HpicfInstParamValMax_Object = MibTableColumn
hpicfInstParamValMax = _HpicfInstParamValMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 1, 3, 1, 8),
    _HpicfInstParamValMax_Type()
)
hpicfInstParamValMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInstParamValMax.setStatus("current")
_HpicfInstConformance_ObjectIdentity = ObjectIdentity
hpicfInstConformance = _HpicfInstConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 2)
)
_HpicfInstGroups_ObjectIdentity = ObjectIdentity
hpicfInstGroups = _HpicfInstGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 2, 1)
)
_HpicfInstCompliances_ObjectIdentity = ObjectIdentity
hpicfInstCompliances = _HpicfInstCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 2, 2)
)

# Managed Objects groups

hpicfInstBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 2, 1, 2)
)
hpicfInstBaseGroup.setObjects(
      *(("HP-ICF-INST-MIB", "hpicfInstEnable"),
        ("HP-ICF-INST-MIB", "hpicfInstMaxMemMB"),
        ("HP-ICF-INST-MIB", "hpicfInstParameterName"),
        ("HP-ICF-INST-MIB", "hpicfInstIntervalName"),
        ("HP-ICF-INST-MIB", "hpicfInstParameterValue"),
        ("HP-ICF-INST-MIB", "hpicfInstParamValMin"),
        ("HP-ICF-INST-MIB", "hpicfInstParamValMax"))
)
if mibBuilder.loadTexts:
    hpicfInstBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfInstBaseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfInstBaseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-INST-MIB",
    **{"hpicfInstMIB": hpicfInstMIB,
       "hpicfInstObjects": hpicfInstObjects,
       "hpicfInstEnable": hpicfInstEnable,
       "hpicfInstMaxMemMB": hpicfInstMaxMemMB,
       "hpicfInstParameterTable": hpicfInstParameterTable,
       "hpicfInstParameterEntry": hpicfInstParameterEntry,
       "hpicfInstParameterIndex": hpicfInstParameterIndex,
       "hpicfInstInterfaceIndex": hpicfInstInterfaceIndex,
       "hpicfInstIntervalIndex": hpicfInstIntervalIndex,
       "hpicfInstParameterName": hpicfInstParameterName,
       "hpicfInstIntervalName": hpicfInstIntervalName,
       "hpicfInstParameterValue": hpicfInstParameterValue,
       "hpicfInstParamValMin": hpicfInstParamValMin,
       "hpicfInstParamValMax": hpicfInstParamValMax,
       "hpicfInstConformance": hpicfInstConformance,
       "hpicfInstGroups": hpicfInstGroups,
       "hpicfInstBaseGroup": hpicfInstBaseGroup,
       "hpicfInstCompliances": hpicfInstCompliances,
       "hpicfInstBaseCompliance": hpicfInstBaseCompliance}
)
