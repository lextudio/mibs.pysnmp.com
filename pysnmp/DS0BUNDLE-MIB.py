# SNMP MIB module (DS0BUNDLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DS0BUNDLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:30 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

ds0Bundle = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 82)
)
ds0Bundle.setRevisions(
        ("1998-05-24 20:10",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx0BondingTable_Object = MibTable
dsx0BondingTable = _Dsx0BondingTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 1)
)
if mibBuilder.loadTexts:
    dsx0BondingTable.setStatus("current")
_Dsx0BondingEntry_Object = MibTableRow
dsx0BondingEntry = _Dsx0BondingEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 1, 1)
)
dsx0BondingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsx0BondingEntry.setStatus("current")


class _Dsx0BondMode_Type(Integer32):
    """Custom type dsx0BondMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("mode0", 3),
          ("mode1", 4),
          ("mode2", 5),
          ("mode3", 6),
          ("none", 1),
          ("other", 2))
    )


_Dsx0BondMode_Type.__name__ = "Integer32"
_Dsx0BondMode_Object = MibTableColumn
dsx0BondMode = _Dsx0BondMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 1, 1, 1),
    _Dsx0BondMode_Type()
)
dsx0BondMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsx0BondMode.setStatus("current")


class _Dsx0BondStatus_Type(Integer32):
    """Custom type dsx0BondStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("callSetup", 2),
          ("dataTransfer", 3),
          ("idle", 1))
    )


_Dsx0BondStatus_Type.__name__ = "Integer32"
_Dsx0BondStatus_Object = MibTableColumn
dsx0BondStatus = _Dsx0BondStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 1, 1, 2),
    _Dsx0BondStatus_Type()
)
dsx0BondStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx0BondStatus.setStatus("current")
_Dsx0BondRowStatus_Type = RowStatus
_Dsx0BondRowStatus_Object = MibTableColumn
dsx0BondRowStatus = _Dsx0BondRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 1, 1, 3),
    _Dsx0BondRowStatus_Type()
)
dsx0BondRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsx0BondRowStatus.setStatus("current")
_Dsx0BundleNextIndex_Type = TestAndIncr
_Dsx0BundleNextIndex_Object = MibScalar
dsx0BundleNextIndex = _Dsx0BundleNextIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 2),
    _Dsx0BundleNextIndex_Type()
)
dsx0BundleNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx0BundleNextIndex.setStatus("current")
_Dsx0BundleTable_Object = MibTable
dsx0BundleTable = _Dsx0BundleTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 3)
)
if mibBuilder.loadTexts:
    dsx0BundleTable.setStatus("current")
_Dsx0BundleEntry_Object = MibTableRow
dsx0BundleEntry = _Dsx0BundleEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 3, 1)
)
dsx0BundleEntry.setIndexNames(
    (0, "DS0BUNDLE-MIB", "dsx0BundleIndex"),
)
if mibBuilder.loadTexts:
    dsx0BundleEntry.setStatus("current")


class _Dsx0BundleIndex_Type(Integer32):
    """Custom type dsx0BundleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx0BundleIndex_Type.__name__ = "Integer32"
_Dsx0BundleIndex_Object = MibTableColumn
dsx0BundleIndex = _Dsx0BundleIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 3, 1, 1),
    _Dsx0BundleIndex_Type()
)
dsx0BundleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsx0BundleIndex.setStatus("current")
_Dsx0BundleIfIndex_Type = InterfaceIndex
_Dsx0BundleIfIndex_Object = MibTableColumn
dsx0BundleIfIndex = _Dsx0BundleIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 3, 1, 2),
    _Dsx0BundleIfIndex_Type()
)
dsx0BundleIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx0BundleIfIndex.setStatus("current")


class _Dsx0BundleCircuitIdentifier_Type(DisplayString):
    """Custom type dsx0BundleCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Dsx0BundleCircuitIdentifier_Type.__name__ = "DisplayString"
_Dsx0BundleCircuitIdentifier_Object = MibTableColumn
dsx0BundleCircuitIdentifier = _Dsx0BundleCircuitIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 3, 1, 3),
    _Dsx0BundleCircuitIdentifier_Type()
)
dsx0BundleCircuitIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsx0BundleCircuitIdentifier.setStatus("current")
_Dsx0BundleRowStatus_Type = RowStatus
_Dsx0BundleRowStatus_Object = MibTableColumn
dsx0BundleRowStatus = _Dsx0BundleRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 82, 3, 1, 4),
    _Dsx0BundleRowStatus_Type()
)
dsx0BundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsx0BundleRowStatus.setStatus("current")
_Ds0BundleConformance_ObjectIdentity = ObjectIdentity
ds0BundleConformance = _Ds0BundleConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 82, 4)
)
_Ds0BundleGroups_ObjectIdentity = ObjectIdentity
ds0BundleGroups = _Ds0BundleGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 82, 4, 1)
)
_Ds0BundleCompliances_ObjectIdentity = ObjectIdentity
ds0BundleCompliances = _Ds0BundleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 82, 4, 2)
)

# Managed Objects groups

ds0BondingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 82, 4, 1, 1)
)
ds0BondingGroup.setObjects(
      *(("DS0BUNDLE-MIB", "dsx0BondMode"),
        ("DS0BUNDLE-MIB", "dsx0BondStatus"),
        ("DS0BUNDLE-MIB", "dsx0BondRowStatus"))
)
if mibBuilder.loadTexts:
    ds0BondingGroup.setStatus("current")

ds0BundleConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 82, 4, 1, 2)
)
ds0BundleConfigGroup.setObjects(
      *(("DS0BUNDLE-MIB", "dsx0BundleNextIndex"),
        ("DS0BUNDLE-MIB", "dsx0BundleIfIndex"),
        ("DS0BUNDLE-MIB", "dsx0BundleCircuitIdentifier"),
        ("DS0BUNDLE-MIB", "dsx0BundleRowStatus"))
)
if mibBuilder.loadTexts:
    ds0BundleConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ds0BundleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 82, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ds0BundleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DS0BUNDLE-MIB",
    **{"ds0Bundle": ds0Bundle,
       "dsx0BondingTable": dsx0BondingTable,
       "dsx0BondingEntry": dsx0BondingEntry,
       "dsx0BondMode": dsx0BondMode,
       "dsx0BondStatus": dsx0BondStatus,
       "dsx0BondRowStatus": dsx0BondRowStatus,
       "dsx0BundleNextIndex": dsx0BundleNextIndex,
       "dsx0BundleTable": dsx0BundleTable,
       "dsx0BundleEntry": dsx0BundleEntry,
       "dsx0BundleIndex": dsx0BundleIndex,
       "dsx0BundleIfIndex": dsx0BundleIfIndex,
       "dsx0BundleCircuitIdentifier": dsx0BundleCircuitIdentifier,
       "dsx0BundleRowStatus": dsx0BundleRowStatus,
       "ds0BundleConformance": ds0BundleConformance,
       "ds0BundleGroups": ds0BundleGroups,
       "ds0BondingGroup": ds0BondingGroup,
       "ds0BundleConfigGroup": ds0BundleConfigGroup,
       "ds0BundleCompliances": ds0BundleCompliances,
       "ds0BundleCompliance": ds0BundleCompliance}
)
