# SNMP MIB module (RBN-STACKEDVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-STACKEDVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:25 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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

rbnStackedVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40)
)
rbnStackedVlanMIB.setRevisions(
        ("2007-02-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnStackedVlanMIBObjects_ObjectIdentity = ObjectIdentity
rbnStackedVlanMIBObjects = _RbnStackedVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1)
)
_RbnStackedVlanAggrStatsTable_Object = MibTable
rbnStackedVlanAggrStatsTable = _RbnStackedVlanAggrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1, 1)
)
if mibBuilder.loadTexts:
    rbnStackedVlanAggrStatsTable.setStatus("current")
_RbnStackedVlanAggrStatsEntry_Object = MibTableRow
rbnStackedVlanAggrStatsEntry = _RbnStackedVlanAggrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1, 1, 1)
)
rbnStackedVlanAggrStatsEntry.setIndexNames(
    (0, "RBN-STACKEDVLAN-MIB", "rbnStackedVlanIndex"),
)
if mibBuilder.loadTexts:
    rbnStackedVlanAggrStatsEntry.setStatus("current")
_RbnStackedVlanIndex_Type = InterfaceIndex
_RbnStackedVlanIndex_Object = MibTableColumn
rbnStackedVlanIndex = _RbnStackedVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1, 1, 1, 1),
    _RbnStackedVlanIndex_Type()
)
rbnStackedVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnStackedVlanIndex.setStatus("current")
_RbnStackedVlanHCInOctets_Type = Counter64
_RbnStackedVlanHCInOctets_Object = MibTableColumn
rbnStackedVlanHCInOctets = _RbnStackedVlanHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1, 1, 1, 2),
    _RbnStackedVlanHCInOctets_Type()
)
rbnStackedVlanHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnStackedVlanHCInOctets.setStatus("current")
_RbnStackedVlanHCInUcastPkts_Type = Counter64
_RbnStackedVlanHCInUcastPkts_Object = MibTableColumn
rbnStackedVlanHCInUcastPkts = _RbnStackedVlanHCInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1, 1, 1, 3),
    _RbnStackedVlanHCInUcastPkts_Type()
)
rbnStackedVlanHCInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnStackedVlanHCInUcastPkts.setStatus("current")
_RbnStackedVlanHCInMulticastPkts_Type = Counter64
_RbnStackedVlanHCInMulticastPkts_Object = MibTableColumn
rbnStackedVlanHCInMulticastPkts = _RbnStackedVlanHCInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1, 1, 1, 4),
    _RbnStackedVlanHCInMulticastPkts_Type()
)
rbnStackedVlanHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnStackedVlanHCInMulticastPkts.setStatus("current")
_RbnStackedVlanHCInBroadcastPkts_Type = Counter64
_RbnStackedVlanHCInBroadcastPkts_Object = MibTableColumn
rbnStackedVlanHCInBroadcastPkts = _RbnStackedVlanHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1, 1, 1, 5),
    _RbnStackedVlanHCInBroadcastPkts_Type()
)
rbnStackedVlanHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnStackedVlanHCInBroadcastPkts.setStatus("current")
_RbnStackedVlanHCOutOctets_Type = Counter64
_RbnStackedVlanHCOutOctets_Object = MibTableColumn
rbnStackedVlanHCOutOctets = _RbnStackedVlanHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1, 1, 1, 6),
    _RbnStackedVlanHCOutOctets_Type()
)
rbnStackedVlanHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnStackedVlanHCOutOctets.setStatus("current")
_RbnStackedVlanHCOutUcastPkts_Type = Counter64
_RbnStackedVlanHCOutUcastPkts_Object = MibTableColumn
rbnStackedVlanHCOutUcastPkts = _RbnStackedVlanHCOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1, 1, 1, 7),
    _RbnStackedVlanHCOutUcastPkts_Type()
)
rbnStackedVlanHCOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnStackedVlanHCOutUcastPkts.setStatus("current")
_RbnStackedVlanHCOutMulticastPkts_Type = Counter64
_RbnStackedVlanHCOutMulticastPkts_Object = MibTableColumn
rbnStackedVlanHCOutMulticastPkts = _RbnStackedVlanHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1, 1, 1, 8),
    _RbnStackedVlanHCOutMulticastPkts_Type()
)
rbnStackedVlanHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnStackedVlanHCOutMulticastPkts.setStatus("current")
_RbnStackedVlanHCOutBroadcastPkts_Type = Counter64
_RbnStackedVlanHCOutBroadcastPkts_Object = MibTableColumn
rbnStackedVlanHCOutBroadcastPkts = _RbnStackedVlanHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 1, 1, 1, 9),
    _RbnStackedVlanHCOutBroadcastPkts_Type()
)
rbnStackedVlanHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnStackedVlanHCOutBroadcastPkts.setStatus("current")
_RbnStackedVlanMIBConformance_ObjectIdentity = ObjectIdentity
rbnStackedVlanMIBConformance = _RbnStackedVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 2)
)
_RbnStackedVlanMIBGroups_ObjectIdentity = ObjectIdentity
rbnStackedVlanMIBGroups = _RbnStackedVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 2, 1)
)
_RbnStackedVlanMIBCompliances_ObjectIdentity = ObjectIdentity
rbnStackedVlanMIBCompliances = _RbnStackedVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 2, 2)
)

# Managed Objects groups

rbnStackedVlanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 2, 1, 1)
)
rbnStackedVlanMIBGroup.setObjects(
      *(("RBN-STACKEDVLAN-MIB", "rbnStackedVlanHCInOctets"),
        ("RBN-STACKEDVLAN-MIB", "rbnStackedVlanHCInUcastPkts"),
        ("RBN-STACKEDVLAN-MIB", "rbnStackedVlanHCInMulticastPkts"),
        ("RBN-STACKEDVLAN-MIB", "rbnStackedVlanHCInBroadcastPkts"),
        ("RBN-STACKEDVLAN-MIB", "rbnStackedVlanHCOutOctets"),
        ("RBN-STACKEDVLAN-MIB", "rbnStackedVlanHCOutUcastPkts"),
        ("RBN-STACKEDVLAN-MIB", "rbnStackedVlanHCOutMulticastPkts"),
        ("RBN-STACKEDVLAN-MIB", "rbnStackedVlanHCOutBroadcastPkts"))
)
if mibBuilder.loadTexts:
    rbnStackedVlanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnStackedVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnStackedVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-STACKEDVLAN-MIB",
    **{"rbnStackedVlanMIB": rbnStackedVlanMIB,
       "rbnStackedVlanMIBObjects": rbnStackedVlanMIBObjects,
       "rbnStackedVlanAggrStatsTable": rbnStackedVlanAggrStatsTable,
       "rbnStackedVlanAggrStatsEntry": rbnStackedVlanAggrStatsEntry,
       "rbnStackedVlanIndex": rbnStackedVlanIndex,
       "rbnStackedVlanHCInOctets": rbnStackedVlanHCInOctets,
       "rbnStackedVlanHCInUcastPkts": rbnStackedVlanHCInUcastPkts,
       "rbnStackedVlanHCInMulticastPkts": rbnStackedVlanHCInMulticastPkts,
       "rbnStackedVlanHCInBroadcastPkts": rbnStackedVlanHCInBroadcastPkts,
       "rbnStackedVlanHCOutOctets": rbnStackedVlanHCOutOctets,
       "rbnStackedVlanHCOutUcastPkts": rbnStackedVlanHCOutUcastPkts,
       "rbnStackedVlanHCOutMulticastPkts": rbnStackedVlanHCOutMulticastPkts,
       "rbnStackedVlanHCOutBroadcastPkts": rbnStackedVlanHCOutBroadcastPkts,
       "rbnStackedVlanMIBConformance": rbnStackedVlanMIBConformance,
       "rbnStackedVlanMIBGroups": rbnStackedVlanMIBGroups,
       "rbnStackedVlanMIBGroup": rbnStackedVlanMIBGroup,
       "rbnStackedVlanMIBCompliances": rbnStackedVlanMIBCompliances,
       "rbnStackedVlanMIBCompliance": rbnStackedVlanMIBCompliance}
)
