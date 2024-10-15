# SNMP MIB module (Juniper-CBF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-CBF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:51 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex")

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


# MODULE-IDENTITY

juniCbfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52)
)
juniCbfMIB.setRevisions(
        ("2002-09-16 21:44",
         "2001-03-30 16:27")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniCbfObjects_ObjectIdentity = ObjectIdentity
juniCbfObjects = _JuniCbfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1)
)
_JuniCbfInterface_ObjectIdentity = ObjectIdentity
juniCbfInterface = _JuniCbfInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1)
)
_JuniCbfNextIfIndex_Type = JuniNextIfIndex
_JuniCbfNextIfIndex_Object = MibScalar
juniCbfNextIfIndex = _JuniCbfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 1),
    _JuniCbfNextIfIndex_Type()
)
juniCbfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCbfNextIfIndex.setStatus("current")
_JuniCbfIfTable_Object = MibTable
juniCbfIfTable = _JuniCbfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniCbfIfTable.setStatus("current")
_JuniCbfIfEntry_Object = MibTableRow
juniCbfIfEntry = _JuniCbfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1)
)
juniCbfIfEntry.setIndexNames(
    (0, "Juniper-CBF-MIB", "juniCbfIfIndex"),
)
if mibBuilder.loadTexts:
    juniCbfIfEntry.setStatus("current")
_JuniCbfIfIndex_Type = InterfaceIndex
_JuniCbfIfIndex_Object = MibTableColumn
juniCbfIfIndex = _JuniCbfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1, 1),
    _JuniCbfIfIndex_Type()
)
juniCbfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniCbfIfIndex.setStatus("current")
_JuniCbfIfRowStatus_Type = RowStatus
_JuniCbfIfRowStatus_Object = MibTableColumn
juniCbfIfRowStatus = _JuniCbfIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1, 2),
    _JuniCbfIfRowStatus_Type()
)
juniCbfIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniCbfIfRowStatus.setStatus("current")
_JuniCbfIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniCbfIfLowerIfIndex_Object = MibTableColumn
juniCbfIfLowerIfIndex = _JuniCbfIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1, 3),
    _JuniCbfIfLowerIfIndex_Type()
)
juniCbfIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniCbfIfLowerIfIndex.setStatus("current")
_JuniCbfIfConnTable_Object = MibTable
juniCbfIfConnTable = _JuniCbfIfConnTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniCbfIfConnTable.setStatus("current")
_JuniCbfIfConnEntry_Object = MibTableRow
juniCbfIfConnEntry = _JuniCbfIfConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1)
)
juniCbfIfConnEntry.setIndexNames(
    (0, "Juniper-CBF-MIB", "juniCbfIfIngressIfIndex"),
)
if mibBuilder.loadTexts:
    juniCbfIfConnEntry.setStatus("current")
_JuniCbfIfIngressIfIndex_Type = InterfaceIndex
_JuniCbfIfIngressIfIndex_Object = MibTableColumn
juniCbfIfIngressIfIndex = _JuniCbfIfIngressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1, 1),
    _JuniCbfIfIngressIfIndex_Type()
)
juniCbfIfIngressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniCbfIfIngressIfIndex.setStatus("current")
_JuniCbfIfConnRowStatus_Type = RowStatus
_JuniCbfIfConnRowStatus_Object = MibTableColumn
juniCbfIfConnRowStatus = _JuniCbfIfConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1, 2),
    _JuniCbfIfConnRowStatus_Type()
)
juniCbfIfConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniCbfIfConnRowStatus.setStatus("current")
_JuniCbfIfEgressIfIndex_Type = InterfaceIndex
_JuniCbfIfEgressIfIndex_Object = MibTableColumn
juniCbfIfEgressIfIndex = _JuniCbfIfEgressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1, 3),
    _JuniCbfIfEgressIfIndex_Type()
)
juniCbfIfEgressIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniCbfIfEgressIfIndex.setStatus("current")
_JuniCbfConformance_ObjectIdentity = ObjectIdentity
juniCbfConformance = _JuniCbfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4)
)
_JuniCbfCompliances_ObjectIdentity = ObjectIdentity
juniCbfCompliances = _JuniCbfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 1)
)
_JuniCbfGroups_ObjectIdentity = ObjectIdentity
juniCbfGroups = _JuniCbfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 2)
)

# Managed Objects groups

juniCbfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 2, 1)
)
juniCbfGroup.setObjects(
      *(("Juniper-CBF-MIB", "juniCbfNextIfIndex"),
        ("Juniper-CBF-MIB", "juniCbfIfRowStatus"),
        ("Juniper-CBF-MIB", "juniCbfIfLowerIfIndex"),
        ("Juniper-CBF-MIB", "juniCbfIfConnRowStatus"),
        ("Juniper-CBF-MIB", "juniCbfIfEgressIfIndex"))
)
if mibBuilder.loadTexts:
    juniCbfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniCbfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniCbfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-CBF-MIB",
    **{"juniCbfMIB": juniCbfMIB,
       "juniCbfObjects": juniCbfObjects,
       "juniCbfInterface": juniCbfInterface,
       "juniCbfNextIfIndex": juniCbfNextIfIndex,
       "juniCbfIfTable": juniCbfIfTable,
       "juniCbfIfEntry": juniCbfIfEntry,
       "juniCbfIfIndex": juniCbfIfIndex,
       "juniCbfIfRowStatus": juniCbfIfRowStatus,
       "juniCbfIfLowerIfIndex": juniCbfIfLowerIfIndex,
       "juniCbfIfConnTable": juniCbfIfConnTable,
       "juniCbfIfConnEntry": juniCbfIfConnEntry,
       "juniCbfIfIngressIfIndex": juniCbfIfIngressIfIndex,
       "juniCbfIfConnRowStatus": juniCbfIfConnRowStatus,
       "juniCbfIfEgressIfIndex": juniCbfIfEgressIfIndex,
       "juniCbfConformance": juniCbfConformance,
       "juniCbfCompliances": juniCbfCompliances,
       "juniCbfCompliance": juniCbfCompliance,
       "juniCbfGroups": juniCbfGroups,
       "juniCbfGroup": juniCbfGroup}
)
