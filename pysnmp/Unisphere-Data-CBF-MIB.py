# SNMP MIB module (Unisphere-Data-CBF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-CBF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:25 2024
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
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdNextIfIndex,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdCbfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52)
)
usdCbfMIB.setRevisions(
        ("2001-03-30 16:27",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdCbfObjects_ObjectIdentity = ObjectIdentity
usdCbfObjects = _UsdCbfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1)
)
_UsdCbfInterface_ObjectIdentity = ObjectIdentity
usdCbfInterface = _UsdCbfInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1)
)
_UsdCbfNextIfIndex_Type = UsdNextIfIndex
_UsdCbfNextIfIndex_Object = MibScalar
usdCbfNextIfIndex = _UsdCbfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 1),
    _UsdCbfNextIfIndex_Type()
)
usdCbfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCbfNextIfIndex.setStatus("current")
_UsdCbfIfTable_Object = MibTable
usdCbfIfTable = _UsdCbfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdCbfIfTable.setStatus("current")
_UsdCbfIfEntry_Object = MibTableRow
usdCbfIfEntry = _UsdCbfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1)
)
usdCbfIfEntry.setIndexNames(
    (0, "Unisphere-Data-CBF-MIB", "usdCbfIfIndex"),
)
if mibBuilder.loadTexts:
    usdCbfIfEntry.setStatus("current")
_UsdCbfIfIndex_Type = InterfaceIndex
_UsdCbfIfIndex_Object = MibTableColumn
usdCbfIfIndex = _UsdCbfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1, 1),
    _UsdCbfIfIndex_Type()
)
usdCbfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdCbfIfIndex.setStatus("current")
_UsdCbfIfRowStatus_Type = RowStatus
_UsdCbfIfRowStatus_Object = MibTableColumn
usdCbfIfRowStatus = _UsdCbfIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1, 2),
    _UsdCbfIfRowStatus_Type()
)
usdCbfIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdCbfIfRowStatus.setStatus("current")
_UsdCbfIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdCbfIfLowerIfIndex_Object = MibTableColumn
usdCbfIfLowerIfIndex = _UsdCbfIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1, 3),
    _UsdCbfIfLowerIfIndex_Type()
)
usdCbfIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdCbfIfLowerIfIndex.setStatus("current")
_UsdCbfIfConnTable_Object = MibTable
usdCbfIfConnTable = _UsdCbfIfConnTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4)
)
if mibBuilder.loadTexts:
    usdCbfIfConnTable.setStatus("current")
_UsdCbfIfConnEntry_Object = MibTableRow
usdCbfIfConnEntry = _UsdCbfIfConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1)
)
usdCbfIfConnEntry.setIndexNames(
    (0, "Unisphere-Data-CBF-MIB", "usdCbfIfIngressIfIndex"),
)
if mibBuilder.loadTexts:
    usdCbfIfConnEntry.setStatus("current")
_UsdCbfIfIngressIfIndex_Type = InterfaceIndex
_UsdCbfIfIngressIfIndex_Object = MibTableColumn
usdCbfIfIngressIfIndex = _UsdCbfIfIngressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1, 1),
    _UsdCbfIfIngressIfIndex_Type()
)
usdCbfIfIngressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdCbfIfIngressIfIndex.setStatus("current")
_UsdCbfIfConnRowStatus_Type = RowStatus
_UsdCbfIfConnRowStatus_Object = MibTableColumn
usdCbfIfConnRowStatus = _UsdCbfIfConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1, 2),
    _UsdCbfIfConnRowStatus_Type()
)
usdCbfIfConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdCbfIfConnRowStatus.setStatus("current")
_UsdCbfIfEgressIfIndex_Type = InterfaceIndex
_UsdCbfIfEgressIfIndex_Object = MibTableColumn
usdCbfIfEgressIfIndex = _UsdCbfIfEgressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1, 3),
    _UsdCbfIfEgressIfIndex_Type()
)
usdCbfIfEgressIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdCbfIfEgressIfIndex.setStatus("current")
_UsdCbfConformance_ObjectIdentity = ObjectIdentity
usdCbfConformance = _UsdCbfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4)
)
_UsdCbfCompliances_ObjectIdentity = ObjectIdentity
usdCbfCompliances = _UsdCbfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 1)
)
_UsdCbfGroups_ObjectIdentity = ObjectIdentity
usdCbfGroups = _UsdCbfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 2)
)

# Managed Objects groups

usdCbfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 2, 1)
)
usdCbfGroup.setObjects(
      *(("Unisphere-Data-CBF-MIB", "usdCbfNextIfIndex"),
        ("Unisphere-Data-CBF-MIB", "usdCbfIfRowStatus"),
        ("Unisphere-Data-CBF-MIB", "usdCbfIfLowerIfIndex"),
        ("Unisphere-Data-CBF-MIB", "usdCbfIfConnRowStatus"),
        ("Unisphere-Data-CBF-MIB", "usdCbfIfEgressIfIndex"))
)
if mibBuilder.loadTexts:
    usdCbfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdCbfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdCbfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-CBF-MIB",
    **{"usdCbfMIB": usdCbfMIB,
       "usdCbfObjects": usdCbfObjects,
       "usdCbfInterface": usdCbfInterface,
       "usdCbfNextIfIndex": usdCbfNextIfIndex,
       "usdCbfIfTable": usdCbfIfTable,
       "usdCbfIfEntry": usdCbfIfEntry,
       "usdCbfIfIndex": usdCbfIfIndex,
       "usdCbfIfRowStatus": usdCbfIfRowStatus,
       "usdCbfIfLowerIfIndex": usdCbfIfLowerIfIndex,
       "usdCbfIfConnTable": usdCbfIfConnTable,
       "usdCbfIfConnEntry": usdCbfIfConnEntry,
       "usdCbfIfIngressIfIndex": usdCbfIfIngressIfIndex,
       "usdCbfIfConnRowStatus": usdCbfIfConnRowStatus,
       "usdCbfIfEgressIfIndex": usdCbfIfEgressIfIndex,
       "usdCbfConformance": usdCbfConformance,
       "usdCbfCompliances": usdCbfCompliances,
       "usdCbfCompliance": usdCbfCompliance,
       "usdCbfGroups": usdCbfGroups,
       "usdCbfGroup": usdCbfGroup}
)
