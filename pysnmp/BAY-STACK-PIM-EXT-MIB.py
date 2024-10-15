# SNMP MIB module (BAY-STACK-PIM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-PIM-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:18 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackPimExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 27)
)
bayStackPimExtMib.setRevisions(
        ("2009-02-27 00:00",
         "2009-02-10 00:00",
         "2007-11-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BspimeNotifications_ObjectIdentity = ObjectIdentity
bspimeNotifications = _BspimeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 0)
)
_BspimeObjects_ObjectIdentity = ObjectIdentity
bspimeObjects = _BspimeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1)
)
_BspimeScalars_ObjectIdentity = ObjectIdentity
bspimeScalars = _BspimeScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 1)
)
_BspimePimVirtualNeighborTable_Object = MibTable
bspimePimVirtualNeighborTable = _BspimePimVirtualNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 2)
)
if mibBuilder.loadTexts:
    bspimePimVirtualNeighborTable.setStatus("current")
_BspimePimVirtualNeighborEntry_Object = MibTableRow
bspimePimVirtualNeighborEntry = _BspimePimVirtualNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 2, 1)
)
bspimePimVirtualNeighborEntry.setIndexNames(
    (0, "BAY-STACK-PIM-EXT-MIB", "bspimePimVirtualNeighborIfIndex"),
    (0, "BAY-STACK-PIM-EXT-MIB", "bspimePimVirtualNeighborAddress"),
)
if mibBuilder.loadTexts:
    bspimePimVirtualNeighborEntry.setStatus("current")
_BspimePimVirtualNeighborIfIndex_Type = InterfaceIndex
_BspimePimVirtualNeighborIfIndex_Object = MibTableColumn
bspimePimVirtualNeighborIfIndex = _BspimePimVirtualNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 2, 1, 1),
    _BspimePimVirtualNeighborIfIndex_Type()
)
bspimePimVirtualNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bspimePimVirtualNeighborIfIndex.setStatus("current")
_BspimePimVirtualNeighborAddress_Type = IpAddress
_BspimePimVirtualNeighborAddress_Object = MibTableColumn
bspimePimVirtualNeighborAddress = _BspimePimVirtualNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 2, 1, 2),
    _BspimePimVirtualNeighborAddress_Type()
)
bspimePimVirtualNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bspimePimVirtualNeighborAddress.setStatus("current")
_BspimePimVirtualNeighborRowStatus_Type = RowStatus
_BspimePimVirtualNeighborRowStatus_Object = MibTableColumn
bspimePimVirtualNeighborRowStatus = _BspimePimVirtualNeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 2, 1, 3),
    _BspimePimVirtualNeighborRowStatus_Type()
)
bspimePimVirtualNeighborRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bspimePimVirtualNeighborRowStatus.setStatus("current")
_BspimePimGroupActiveRPMappingTable_Object = MibTable
bspimePimGroupActiveRPMappingTable = _BspimePimGroupActiveRPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 3)
)
if mibBuilder.loadTexts:
    bspimePimGroupActiveRPMappingTable.setStatus("current")
_BspimePimGroupActiveRPMappingEntry_Object = MibTableRow
bspimePimGroupActiveRPMappingEntry = _BspimePimGroupActiveRPMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 3, 1)
)
bspimePimGroupActiveRPMappingEntry.setIndexNames(
    (0, "BAY-STACK-PIM-EXT-MIB", "bspimePimGroupActiveRPMappingGroupAddress"),
    (0, "BAY-STACK-PIM-EXT-MIB", "bspimePimGroupActiveRPMappingGroupMask"),
    (0, "BAY-STACK-PIM-EXT-MIB", "bspimePimGroupActiveRPMappingActiveRP"),
)
if mibBuilder.loadTexts:
    bspimePimGroupActiveRPMappingEntry.setStatus("current")
_BspimePimGroupActiveRPMappingGroupAddress_Type = IpAddress
_BspimePimGroupActiveRPMappingGroupAddress_Object = MibTableColumn
bspimePimGroupActiveRPMappingGroupAddress = _BspimePimGroupActiveRPMappingGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 3, 1, 1),
    _BspimePimGroupActiveRPMappingGroupAddress_Type()
)
bspimePimGroupActiveRPMappingGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bspimePimGroupActiveRPMappingGroupAddress.setStatus("current")
_BspimePimGroupActiveRPMappingGroupMask_Type = IpAddress
_BspimePimGroupActiveRPMappingGroupMask_Object = MibTableColumn
bspimePimGroupActiveRPMappingGroupMask = _BspimePimGroupActiveRPMappingGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 3, 1, 2),
    _BspimePimGroupActiveRPMappingGroupMask_Type()
)
bspimePimGroupActiveRPMappingGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bspimePimGroupActiveRPMappingGroupMask.setStatus("current")
_BspimePimGroupActiveRPMappingActiveRP_Type = IpAddress
_BspimePimGroupActiveRPMappingActiveRP_Object = MibTableColumn
bspimePimGroupActiveRPMappingActiveRP = _BspimePimGroupActiveRPMappingActiveRP_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 3, 1, 3),
    _BspimePimGroupActiveRPMappingActiveRP_Type()
)
bspimePimGroupActiveRPMappingActiveRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bspimePimGroupActiveRPMappingActiveRP.setStatus("current")


class _BspimePimGroupActiveRPMappingPriority_Type(Integer32):
    """Custom type bspimePimGroupActiveRPMappingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BspimePimGroupActiveRPMappingPriority_Type.__name__ = "Integer32"
_BspimePimGroupActiveRPMappingPriority_Object = MibTableColumn
bspimePimGroupActiveRPMappingPriority = _BspimePimGroupActiveRPMappingPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 1, 3, 1, 4),
    _BspimePimGroupActiveRPMappingPriority_Type()
)
bspimePimGroupActiveRPMappingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bspimePimGroupActiveRPMappingPriority.setStatus("current")
_BspimeNotificationObjects_ObjectIdentity = ObjectIdentity
bspimeNotificationObjects = _BspimeNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 2)
)


class _BspimeNotifNeighborStatus_Type(Integer32):
    """Custom type bspimeNotifNeighborStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_BspimeNotifNeighborStatus_Type.__name__ = "Integer32"
_BspimeNotifNeighborStatus_Object = MibScalar
bspimeNotifNeighborStatus = _BspimeNotifNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 2, 1),
    _BspimeNotifNeighborStatus_Type()
)
bspimeNotifNeighborStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bspimeNotifNeighborStatus.setStatus("current")

# Managed Objects groups


# Notification objects

bspimeNeighborStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 27, 0, 1)
)
bspimeNeighborStateChanged.setObjects(
      *(("BAY-STACK-PIM-EXT-MIB", "rcPimNeighborIfIndex"),
        ("BAY-STACK-PIM-EXT-MIB", "bspimeNotifNeighborStatus"))
)
if mibBuilder.loadTexts:
    bspimeNeighborStateChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-PIM-EXT-MIB",
    **{"bayStackPimExtMib": bayStackPimExtMib,
       "bspimeNotifications": bspimeNotifications,
       "bspimeNeighborStateChanged": bspimeNeighborStateChanged,
       "bspimeObjects": bspimeObjects,
       "bspimeScalars": bspimeScalars,
       "bspimePimVirtualNeighborTable": bspimePimVirtualNeighborTable,
       "bspimePimVirtualNeighborEntry": bspimePimVirtualNeighborEntry,
       "bspimePimVirtualNeighborIfIndex": bspimePimVirtualNeighborIfIndex,
       "bspimePimVirtualNeighborAddress": bspimePimVirtualNeighborAddress,
       "bspimePimVirtualNeighborRowStatus": bspimePimVirtualNeighborRowStatus,
       "bspimePimGroupActiveRPMappingTable": bspimePimGroupActiveRPMappingTable,
       "bspimePimGroupActiveRPMappingEntry": bspimePimGroupActiveRPMappingEntry,
       "bspimePimGroupActiveRPMappingGroupAddress": bspimePimGroupActiveRPMappingGroupAddress,
       "bspimePimGroupActiveRPMappingGroupMask": bspimePimGroupActiveRPMappingGroupMask,
       "bspimePimGroupActiveRPMappingActiveRP": bspimePimGroupActiveRPMappingActiveRP,
       "bspimePimGroupActiveRPMappingPriority": bspimePimGroupActiveRPMappingPriority,
       "bspimeNotificationObjects": bspimeNotificationObjects,
       "bspimeNotifNeighborStatus": bspimeNotifNeighborStatus}
)
