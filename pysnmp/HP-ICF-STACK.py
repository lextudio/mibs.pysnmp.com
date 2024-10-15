# SNMP MIB module (HP-ICF-STACK) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-STACK
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:14 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hpicfCommon,
 hpicfObjectModules) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon",
    "hpicfObjectModules")

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

hpicfStackMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6)
)
hpicfStackMib.setRevisions(
        ("2000-11-03 22:25",
         "1996-09-06 22:28")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfStackConformance_ObjectIdentity = ObjectIdentity
hpicfStackConformance = _HpicfStackConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6, 1)
)
_HpicfStackCompliances_ObjectIdentity = ObjectIdentity
hpicfStackCompliances = _HpicfStackCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6, 1, 1)
)
_HpicfStackGroups_ObjectIdentity = ObjectIdentity
hpicfStackGroups = _HpicfStackGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6, 1, 2)
)
_HpicfStack_ObjectIdentity = ObjectIdentity
hpicfStack = _HpicfStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5)
)
_HpicfStackBoxTable_Object = MibTable
hpicfStackBoxTable = _HpicfStackBoxTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfStackBoxTable.setStatus("current")
_HpicfStackBoxEntry_Object = MibTableRow
hpicfStackBoxEntry = _HpicfStackBoxEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 1, 1)
)
hpicfStackBoxEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfStackBoxEntry.setStatus("current")


class _HpicfStackBoxId_Type(OctetString):
    """Custom type hpicfStackBoxId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_HpicfStackBoxId_Type.__name__ = "OctetString"
_HpicfStackBoxId_Object = MibTableColumn
hpicfStackBoxId = _HpicfStackBoxId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 1, 1, 1),
    _HpicfStackBoxId_Type()
)
hpicfStackBoxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfStackBoxId.setStatus("current")


class _HpicfStackBoxName_Type(DisplayString):
    """Custom type hpicfStackBoxName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HpicfStackBoxName_Type.__name__ = "DisplayString"
_HpicfStackBoxName_Object = MibTableColumn
hpicfStackBoxName = _HpicfStackBoxName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 1, 1, 2),
    _HpicfStackBoxName_Type()
)
hpicfStackBoxName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfStackBoxName.setStatus("current")
_HpicfStackAgentTable_Object = MibTable
hpicfStackAgentTable = _HpicfStackAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hpicfStackAgentTable.setStatus("current")
_HpicfStackAgentEntry_Object = MibTableRow
hpicfStackAgentEntry = _HpicfStackAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 2, 1)
)
hpicfStackAgentEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfStackAgentEntry.setStatus("current")


class _HpicfStackAgentBoxId_Type(OctetString):
    """Custom type hpicfStackAgentBoxId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_HpicfStackAgentBoxId_Type.__name__ = "OctetString"
_HpicfStackAgentBoxId_Object = MibTableColumn
hpicfStackAgentBoxId = _HpicfStackAgentBoxId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 2, 1, 1),
    _HpicfStackAgentBoxId_Type()
)
hpicfStackAgentBoxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfStackAgentBoxId.setStatus("current")
_HpicfStackActiveAgent_Type = Integer32
_HpicfStackActiveAgent_Object = MibScalar
hpicfStackActiveAgent = _HpicfStackActiveAgent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 3),
    _HpicfStackActiveAgent_Type()
)
hpicfStackActiveAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfStackActiveAgent.setStatus("current")
_HpicfStackAgentForced_Type = TruthValue
_HpicfStackAgentForced_Object = MibScalar
hpicfStackAgentForced = _HpicfStackAgentForced_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5, 4),
    _HpicfStackAgentForced_Type()
)
hpicfStackAgentForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfStackAgentForced.setStatus("current")

# Managed Objects groups

hpicfStackBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6, 1, 2, 1)
)
hpicfStackBasicGroup.setObjects(
      *(("HP-ICF-STACK", "hpicfStackBoxId"),
        ("HP-ICF-STACK", "hpicfStackBoxName"))
)
if mibBuilder.loadTexts:
    hpicfStackBasicGroup.setStatus("current")

hpicfStackMultiAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6, 1, 2, 2)
)
hpicfStackMultiAgentGroup.setObjects(
      *(("HP-ICF-STACK", "hpicfStackAgentBoxId"),
        ("HP-ICF-STACK", "hpicfStackActiveAgent"),
        ("HP-ICF-STACK", "hpicfStackAgentForced"))
)
if mibBuilder.loadTexts:
    hpicfStackMultiAgentGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfStackCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfStackCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-STACK",
    **{"hpicfStackMib": hpicfStackMib,
       "hpicfStackConformance": hpicfStackConformance,
       "hpicfStackCompliances": hpicfStackCompliances,
       "hpicfStackCompliance": hpicfStackCompliance,
       "hpicfStackGroups": hpicfStackGroups,
       "hpicfStackBasicGroup": hpicfStackBasicGroup,
       "hpicfStackMultiAgentGroup": hpicfStackMultiAgentGroup,
       "hpicfStack": hpicfStack,
       "hpicfStackBoxTable": hpicfStackBoxTable,
       "hpicfStackBoxEntry": hpicfStackBoxEntry,
       "hpicfStackBoxId": hpicfStackBoxId,
       "hpicfStackBoxName": hpicfStackBoxName,
       "hpicfStackAgentTable": hpicfStackAgentTable,
       "hpicfStackAgentEntry": hpicfStackAgentEntry,
       "hpicfStackAgentBoxId": hpicfStackAgentBoxId,
       "hpicfStackActiveAgent": hpicfStackActiveAgent,
       "hpicfStackAgentForced": hpicfStackAgentForced}
)
