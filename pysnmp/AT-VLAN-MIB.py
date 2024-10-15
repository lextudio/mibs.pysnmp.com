# SNMP MIB module (AT-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:38 2024
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

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "sysinfo")

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

atVlanInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16)
)
atVlanInfo.setRevisions(
        ("2010-09-07 00:00",
         "2010-06-15 00:15",
         "2009-06-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtVlanStatistics_ObjectIdentity = ObjectIdentity
atVlanStatistics = _AtVlanStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1)
)
_AtVlanStatNumCollections_Type = Integer32
_AtVlanStatNumCollections_Object = MibScalar
atVlanStatNumCollections = _AtVlanStatNumCollections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 1),
    _AtVlanStatNumCollections_Type()
)
atVlanStatNumCollections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVlanStatNumCollections.setStatus("current")
_AtVlanStatCollectionTable_Object = MibTable
atVlanStatCollectionTable = _AtVlanStatCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2)
)
if mibBuilder.loadTexts:
    atVlanStatCollectionTable.setStatus("current")
_AtVlanStatCollectionEntry_Object = MibTableRow
atVlanStatCollectionEntry = _AtVlanStatCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1)
)
atVlanStatCollectionEntry.setIndexNames(
    (0, "AT-VLAN-MIB", "atVlanStatCollectionName"),
)
if mibBuilder.loadTexts:
    atVlanStatCollectionEntry.setStatus("current")
_AtVlanStatCollectionName_Type = DisplayString
_AtVlanStatCollectionName_Object = MibTableColumn
atVlanStatCollectionName = _AtVlanStatCollectionName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 1),
    _AtVlanStatCollectionName_Type()
)
atVlanStatCollectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVlanStatCollectionName.setStatus("current")
_AtVlanStatCollectionVlanId_Type = Gauge32
_AtVlanStatCollectionVlanId_Object = MibTableColumn
atVlanStatCollectionVlanId = _AtVlanStatCollectionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 2),
    _AtVlanStatCollectionVlanId_Type()
)
atVlanStatCollectionVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVlanStatCollectionVlanId.setStatus("current")
_AtVlanStatCollectionPortMap_Type = OctetString
_AtVlanStatCollectionPortMap_Object = MibTableColumn
atVlanStatCollectionPortMap = _AtVlanStatCollectionPortMap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 3),
    _AtVlanStatCollectionPortMap_Type()
)
atVlanStatCollectionPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVlanStatCollectionPortMap.setStatus("current")
_AtVlanStatCollectionIngressPkts_Type = Counter64
_AtVlanStatCollectionIngressPkts_Object = MibTableColumn
atVlanStatCollectionIngressPkts = _AtVlanStatCollectionIngressPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 4),
    _AtVlanStatCollectionIngressPkts_Type()
)
atVlanStatCollectionIngressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVlanStatCollectionIngressPkts.setStatus("current")
_AtVlanStatCollectionIngressOctets_Type = Counter64
_AtVlanStatCollectionIngressOctets_Object = MibTableColumn
atVlanStatCollectionIngressOctets = _AtVlanStatCollectionIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 5),
    _AtVlanStatCollectionIngressOctets_Type()
)
atVlanStatCollectionIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVlanStatCollectionIngressOctets.setStatus("current")
_AtVlanStatCollectionResetStats_Type = TruthValue
_AtVlanStatCollectionResetStats_Object = MibTableColumn
atVlanStatCollectionResetStats = _AtVlanStatCollectionResetStats_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 16, 1, 2, 1, 6),
    _AtVlanStatCollectionResetStats_Type()
)
atVlanStatCollectionResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atVlanStatCollectionResetStats.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-VLAN-MIB",
    **{"atVlanInfo": atVlanInfo,
       "atVlanStatistics": atVlanStatistics,
       "atVlanStatNumCollections": atVlanStatNumCollections,
       "atVlanStatCollectionTable": atVlanStatCollectionTable,
       "atVlanStatCollectionEntry": atVlanStatCollectionEntry,
       "atVlanStatCollectionName": atVlanStatCollectionName,
       "atVlanStatCollectionVlanId": atVlanStatCollectionVlanId,
       "atVlanStatCollectionPortMap": atVlanStatCollectionPortMap,
       "atVlanStatCollectionIngressPkts": atVlanStatCollectionIngressPkts,
       "atVlanStatCollectionIngressOctets": atVlanStatCollectionIngressOctets,
       "atVlanStatCollectionResetStats": atVlanStatCollectionResetStats}
)
