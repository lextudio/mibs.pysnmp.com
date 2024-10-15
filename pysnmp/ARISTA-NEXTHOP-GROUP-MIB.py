# SNMP MIB module (ARISTA-NEXTHOP-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-NEXTHOP-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:23 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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

aristaNexthopGroupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21)
)
aristaNexthopGroupMIB.setRevisions(
        ("2016-04-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NexthopGroupName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class NexthopGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("gre", 2),
          ("invalid", 0),
          ("ip", 4),
          ("ipInIp", 1),
          ("mpls", 3),
          ("mplsOverGre", 5))
    )



# MIB Managed Objects in the order of their OIDs

_AristaNexthopGroupMibObjects_ObjectIdentity = ObjectIdentity
aristaNexthopGroupMibObjects = _AristaNexthopGroupMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1)
)
_AristaNexthopGroupTable_Object = MibTable
aristaNexthopGroupTable = _AristaNexthopGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1)
)
if mibBuilder.loadTexts:
    aristaNexthopGroupTable.setStatus("current")
_AristaNexthopGroupEntry_Object = MibTableRow
aristaNexthopGroupEntry = _AristaNexthopGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1)
)
aristaNexthopGroupEntry.setIndexNames(
    (0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupId"),
)
if mibBuilder.loadTexts:
    aristaNexthopGroupEntry.setStatus("current")
_AristaNexthopGroupId_Type = Unsigned32
_AristaNexthopGroupId_Object = MibTableColumn
aristaNexthopGroupId = _AristaNexthopGroupId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 1),
    _AristaNexthopGroupId_Type()
)
aristaNexthopGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaNexthopGroupId.setStatus("current")
_AristaNexthopGroupName_Type = NexthopGroupName
_AristaNexthopGroupName_Object = MibTableColumn
aristaNexthopGroupName = _AristaNexthopGroupName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 2),
    _AristaNexthopGroupName_Type()
)
aristaNexthopGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaNexthopGroupName.setStatus("current")
_AristaNexthopGroupType_Type = NexthopGroupType
_AristaNexthopGroupType_Object = MibTableColumn
aristaNexthopGroupType = _AristaNexthopGroupType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 3),
    _AristaNexthopGroupType_Type()
)
aristaNexthopGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaNexthopGroupType.setStatus("current")
_AristaNexthopGroupCounterTable_Object = MibTable
aristaNexthopGroupCounterTable = _AristaNexthopGroupCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2)
)
if mibBuilder.loadTexts:
    aristaNexthopGroupCounterTable.setStatus("current")
_AristaNexthopGroupCounterEntry_Object = MibTableRow
aristaNexthopGroupCounterEntry = _AristaNexthopGroupCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1)
)
aristaNexthopGroupCounterEntry.setIndexNames(
    (0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupId"),
    (0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupEntryIndex"),
)
if mibBuilder.loadTexts:
    aristaNexthopGroupCounterEntry.setStatus("current")
_AristaNexthopGroupEntryIndex_Type = Unsigned32
_AristaNexthopGroupEntryIndex_Object = MibTableColumn
aristaNexthopGroupEntryIndex = _AristaNexthopGroupEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 1),
    _AristaNexthopGroupEntryIndex_Type()
)
aristaNexthopGroupEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaNexthopGroupEntryIndex.setStatus("current")
_AristaNexthopGroupCounterIndex_Type = Unsigned32
_AristaNexthopGroupCounterIndex_Object = MibTableColumn
aristaNexthopGroupCounterIndex = _AristaNexthopGroupCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 2),
    _AristaNexthopGroupCounterIndex_Type()
)
aristaNexthopGroupCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaNexthopGroupCounterIndex.setStatus("current")
_AristaNexthopGroupCounterPacketCount_Type = Counter64
_AristaNexthopGroupCounterPacketCount_Object = MibTableColumn
aristaNexthopGroupCounterPacketCount = _AristaNexthopGroupCounterPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 3),
    _AristaNexthopGroupCounterPacketCount_Type()
)
aristaNexthopGroupCounterPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaNexthopGroupCounterPacketCount.setStatus("current")
_AristaNexthopGroupCounterByteCount_Type = Counter64
_AristaNexthopGroupCounterByteCount_Object = MibTableColumn
aristaNexthopGroupCounterByteCount = _AristaNexthopGroupCounterByteCount_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 4),
    _AristaNexthopGroupCounterByteCount_Type()
)
aristaNexthopGroupCounterByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaNexthopGroupCounterByteCount.setStatus("current")
_AristaNexthopGroupMibConformance_ObjectIdentity = ObjectIdentity
aristaNexthopGroupMibConformance = _AristaNexthopGroupMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 2)
)
_AristaNexthopGroupMibCompliances_ObjectIdentity = ObjectIdentity
aristaNexthopGroupMibCompliances = _AristaNexthopGroupMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 1)
)
_AristaNexthopGroupMibGroups_ObjectIdentity = ObjectIdentity
aristaNexthopGroupMibGroups = _AristaNexthopGroupMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2)
)

# Managed Objects groups

aristaNexthopGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2, 1)
)
aristaNexthopGroupGroup.setObjects(
      *(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupName"),
        ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupType"))
)
if mibBuilder.loadTexts:
    aristaNexthopGroupGroup.setStatus("current")

aristaNexthopGroupCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2, 2)
)
aristaNexthopGroupCounterGroup.setObjects(
      *(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterIndex"),
        ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterPacketCount"),
        ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterByteCount"))
)
if mibBuilder.loadTexts:
    aristaNexthopGroupCounterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaNexthopGroupMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aristaNexthopGroupMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-NEXTHOP-GROUP-MIB",
    **{"NexthopGroupName": NexthopGroupName,
       "NexthopGroupType": NexthopGroupType,
       "aristaNexthopGroupMIB": aristaNexthopGroupMIB,
       "aristaNexthopGroupMibObjects": aristaNexthopGroupMibObjects,
       "aristaNexthopGroupTable": aristaNexthopGroupTable,
       "aristaNexthopGroupEntry": aristaNexthopGroupEntry,
       "aristaNexthopGroupId": aristaNexthopGroupId,
       "aristaNexthopGroupName": aristaNexthopGroupName,
       "aristaNexthopGroupType": aristaNexthopGroupType,
       "aristaNexthopGroupCounterTable": aristaNexthopGroupCounterTable,
       "aristaNexthopGroupCounterEntry": aristaNexthopGroupCounterEntry,
       "aristaNexthopGroupEntryIndex": aristaNexthopGroupEntryIndex,
       "aristaNexthopGroupCounterIndex": aristaNexthopGroupCounterIndex,
       "aristaNexthopGroupCounterPacketCount": aristaNexthopGroupCounterPacketCount,
       "aristaNexthopGroupCounterByteCount": aristaNexthopGroupCounterByteCount,
       "aristaNexthopGroupMibConformance": aristaNexthopGroupMibConformance,
       "aristaNexthopGroupMibCompliances": aristaNexthopGroupMibCompliances,
       "aristaNexthopGroupMibCompliance": aristaNexthopGroupMibCompliance,
       "aristaNexthopGroupMibGroups": aristaNexthopGroupMibGroups,
       "aristaNexthopGroupGroup": aristaNexthopGroupGroup,
       "aristaNexthopGroupCounterGroup": aristaNexthopGroupCounterGroup}
)
