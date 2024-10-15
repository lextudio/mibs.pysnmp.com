# SNMP MIB module (REDSTONE-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:43 2024
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

(ospfIfEntry,) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfIfEntry")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rsOspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14)
)
rsOspfMIB.setRevisions(
        ("1998-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsOspfObjects_ObjectIdentity = ObjectIdentity
rsOspfObjects = _RsOspfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 1)
)
_RsOspfGeneralGroup_ObjectIdentity = ObjectIdentity
rsOspfGeneralGroup = _RsOspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 1)
)


class _RsOspfProcessId_Type(Integer32):
    """Custom type rsOspfProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsOspfProcessId_Type.__name__ = "Integer32"
_RsOspfProcessId_Object = MibScalar
rsOspfProcessId = _RsOspfProcessId_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 1, 1),
    _RsOspfProcessId_Type()
)
rsOspfProcessId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsOspfProcessId.setStatus("current")


class _RsOspfMaxPathSplits_Type(Integer32):
    """Custom type rsOspfMaxPathSplits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RsOspfMaxPathSplits_Type.__name__ = "Integer32"
_RsOspfMaxPathSplits_Object = MibScalar
rsOspfMaxPathSplits = _RsOspfMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 1, 2),
    _RsOspfMaxPathSplits_Type()
)
rsOspfMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsOspfMaxPathSplits.setStatus("current")


class _RsOspfSpfHoldInterval_Type(Integer32):
    """Custom type rsOspfSpfHoldInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RsOspfSpfHoldInterval_Type.__name__ = "Integer32"
_RsOspfSpfHoldInterval_Object = MibScalar
rsOspfSpfHoldInterval = _RsOspfSpfHoldInterval_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 1, 3),
    _RsOspfSpfHoldInterval_Type()
)
rsOspfSpfHoldInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsOspfSpfHoldInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsOspfSpfHoldInterval.setUnits("seconds")
_RsOspfIfTable_Object = MibTable
rsOspfIfTable = _RsOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    rsOspfIfTable.setStatus("current")
_RsOspfIfEntry_Object = MibTableRow
rsOspfIfEntry = _RsOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rsOspfIfEntry.setStatus("current")


class _RsOspfIfCost_Type(Integer32):
    """Custom type rsOspfIfCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RsOspfIfCost_Type.__name__ = "Integer32"
_RsOspfIfCost_Object = MibTableColumn
rsOspfIfCost = _RsOspfIfCost_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 1, 2, 1, 1),
    _RsOspfIfCost_Type()
)
rsOspfIfCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsOspfIfCost.setStatus("current")
_RsOspfConformance_ObjectIdentity = ObjectIdentity
rsOspfConformance = _RsOspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 4)
)
_RsOspfCompliances_ObjectIdentity = ObjectIdentity
rsOspfCompliances = _RsOspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 4, 1)
)
_RsOspfGroups_ObjectIdentity = ObjectIdentity
rsOspfGroups = _RsOspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 4, 2)
)
ospfIfEntry.registerAugmentions(
    ("REDSTONE-OSPF-MIB",
     "rsOspfIfEntry")
)
rsOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())

# Managed Objects groups

rsOspfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 4, 2, 1)
)
rsOspfBasicGroup.setObjects(
      *(("REDSTONE-OSPF-MIB", "rsOspfProcessId"),
        ("REDSTONE-OSPF-MIB", "rsOspfMaxPathSplits"),
        ("REDSTONE-OSPF-MIB", "rsOspfSpfHoldInterval"))
)
if mibBuilder.loadTexts:
    rsOspfBasicGroup.setStatus("current")

rsOspfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 4, 2, 2)
)
rsOspfIfGroup.setObjects(
    ("REDSTONE-OSPF-MIB", "rsOspfIfCost")
)
if mibBuilder.loadTexts:
    rsOspfIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsOspfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 14, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsOspfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-OSPF-MIB",
    **{"rsOspfMIB": rsOspfMIB,
       "rsOspfObjects": rsOspfObjects,
       "rsOspfGeneralGroup": rsOspfGeneralGroup,
       "rsOspfProcessId": rsOspfProcessId,
       "rsOspfMaxPathSplits": rsOspfMaxPathSplits,
       "rsOspfSpfHoldInterval": rsOspfSpfHoldInterval,
       "rsOspfIfTable": rsOspfIfTable,
       "rsOspfIfEntry": rsOspfIfEntry,
       "rsOspfIfCost": rsOspfIfCost,
       "rsOspfConformance": rsOspfConformance,
       "rsOspfCompliances": rsOspfCompliances,
       "rsOspfCompliance": rsOspfCompliance,
       "rsOspfGroups": rsOspfGroups,
       "rsOspfBasicGroup": rsOspfBasicGroup,
       "rsOspfIfGroup": rsOspfIfGroup}
)
