# SNMP MIB module (CUMULUS-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CUMULUS-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:00 2024
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

(DateAndTime,
 DisplayString,
 cumulusMib) = mibBuilder.importSymbols(
    "CUMULUS-SNMP-MIB",
    "DateAndTime",
    "DisplayString",
    "cumulusMib")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ResourceUtilization_ObjectIdentity = ObjectIdentity
resourceUtilization = _ResourceUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 1)
)
_L3Tables_ObjectIdentity = ObjectIdentity
l3Tables = _L3Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1)
)
_L3HostTableCurrentEntries_Type = Integer32
_L3HostTableCurrentEntries_Object = MibScalar
l3HostTableCurrentEntries = _L3HostTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 1),
    _L3HostTableCurrentEntries_Type()
)
l3HostTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3HostTableCurrentEntries.setStatus("current")
_L3HostTableMaxEntries_Type = Integer32
_L3HostTableMaxEntries_Object = MibScalar
l3HostTableMaxEntries = _L3HostTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 2),
    _L3HostTableMaxEntries_Type()
)
l3HostTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3HostTableMaxEntries.setStatus("current")
_L3RoutingTableCurrentEntries_Type = Integer32
_L3RoutingTableCurrentEntries_Object = MibScalar
l3RoutingTableCurrentEntries = _L3RoutingTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 3),
    _L3RoutingTableCurrentEntries_Type()
)
l3RoutingTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3RoutingTableCurrentEntries.setStatus("current")
_L3RoutingTableMaxEntries_Type = Integer32
_L3RoutingTableMaxEntries_Object = MibScalar
l3RoutingTableMaxEntries = _L3RoutingTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 4),
    _L3RoutingTableMaxEntries_Type()
)
l3RoutingTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3RoutingTableMaxEntries.setStatus("current")
_L3NextHopTableCurrentEntries_Type = Integer32
_L3NextHopTableCurrentEntries_Object = MibScalar
l3NextHopTableCurrentEntries = _L3NextHopTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 5),
    _L3NextHopTableCurrentEntries_Type()
)
l3NextHopTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3NextHopTableCurrentEntries.setStatus("current")
_L3NextHopTableMaxEntries_Type = Integer32
_L3NextHopTableMaxEntries_Object = MibScalar
l3NextHopTableMaxEntries = _L3NextHopTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 6),
    _L3NextHopTableMaxEntries_Type()
)
l3NextHopTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3NextHopTableMaxEntries.setStatus("current")
_L3EcmpGroupTableCurrentEntries_Type = Integer32
_L3EcmpGroupTableCurrentEntries_Object = MibScalar
l3EcmpGroupTableCurrentEntries = _L3EcmpGroupTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 7),
    _L3EcmpGroupTableCurrentEntries_Type()
)
l3EcmpGroupTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3EcmpGroupTableCurrentEntries.setStatus("current")
_L3EcmpGroupTableMaxEntries_Type = Integer32
_L3EcmpGroupTableMaxEntries_Object = MibScalar
l3EcmpGroupTableMaxEntries = _L3EcmpGroupTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 8),
    _L3EcmpGroupTableMaxEntries_Type()
)
l3EcmpGroupTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3EcmpGroupTableMaxEntries.setStatus("current")
_L3EcmpNextHopTableCurrentEntries_Type = Integer32
_L3EcmpNextHopTableCurrentEntries_Object = MibScalar
l3EcmpNextHopTableCurrentEntries = _L3EcmpNextHopTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 9),
    _L3EcmpNextHopTableCurrentEntries_Type()
)
l3EcmpNextHopTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3EcmpNextHopTableCurrentEntries.setStatus("current")
_L3EcmpNextHopTableMaxEntries_Type = Integer32
_L3EcmpNextHopTableMaxEntries_Object = MibScalar
l3EcmpNextHopTableMaxEntries = _L3EcmpNextHopTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 1, 10),
    _L3EcmpNextHopTableMaxEntries_Type()
)
l3EcmpNextHopTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3EcmpNextHopTableMaxEntries.setStatus("current")
_L2Tables_ObjectIdentity = ObjectIdentity
l2Tables = _L2Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 1, 2)
)
_L2MacTableCurrentEntries_Type = Integer32
_L2MacTableCurrentEntries_Object = MibScalar
l2MacTableCurrentEntries = _L2MacTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 2, 1),
    _L2MacTableCurrentEntries_Type()
)
l2MacTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2MacTableCurrentEntries.setStatus("current")
_L2MacTableMaxEntries_Type = Integer32
_L2MacTableMaxEntries_Object = MibScalar
l2MacTableMaxEntries = _L2MacTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 2, 2),
    _L2MacTableMaxEntries_Type()
)
l2MacTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2MacTableMaxEntries.setStatus("current")
_L2CacheTableCurrentEntries_Type = Integer32
_L2CacheTableCurrentEntries_Object = MibScalar
l2CacheTableCurrentEntries = _L2CacheTableCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 2, 3),
    _L2CacheTableCurrentEntries_Type()
)
l2CacheTableCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2CacheTableCurrentEntries.setStatus("current")
_L2CacheTableMaxEntries_Type = Integer32
_L2CacheTableMaxEntries_Object = MibScalar
l2CacheTableMaxEntries = _L2CacheTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 2, 4),
    _L2CacheTableMaxEntries_Type()
)
l2CacheTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2CacheTableMaxEntries.setStatus("current")
_BufferUtilizn_ObjectIdentity = ObjectIdentity
bufferUtilizn = _BufferUtilizn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3)
)


class _BufUtiliznComputeTime_Type(DisplayString):
    """Custom type bufUtiliznComputeTime based on DisplayString"""
    defaultValue = OctetString("0")


_BufUtiliznComputeTime_Object = MibScalar
bufUtiliznComputeTime = _BufUtiliznComputeTime_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 1),
    _BufUtiliznComputeTime_Type()
)
bufUtiliznComputeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufUtiliznComputeTime.setStatus("current")
_BufUtiliznPollInterval_Type = Integer32
_BufUtiliznPollInterval_Object = MibScalar
bufUtiliznPollInterval = _BufUtiliznPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 2),
    _BufUtiliznPollInterval_Type()
)
bufUtiliznPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufUtiliznPollInterval.setStatus("current")
_BufUtiliznMeasureInterval_Type = Integer32
_BufUtiliznMeasureInterval_Object = MibScalar
bufUtiliznMeasureInterval = _BufUtiliznMeasureInterval_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 3),
    _BufUtiliznMeasureInterval_Type()
)
bufUtiliznMeasureInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufUtiliznMeasureInterval.setStatus("current")
_BufUtiliznTable_Object = MibTable
bufUtiliznTable = _BufUtiliznTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4)
)
if mibBuilder.loadTexts:
    bufUtiliznTable.setStatus("current")
_BufUtiliznEntry_Object = MibTableRow
bufUtiliznEntry = _BufUtiliznEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1)
)
bufUtiliznEntry.setIndexNames(
    (0, "CUMULUS-RESOURCES-MIB", "bufServicePoolID"),
)
if mibBuilder.loadTexts:
    bufUtiliznEntry.setStatus("current")


class _BufServicePoolID_Type(Integer32):
    """Custom type bufServicePoolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BufServicePoolID_Type.__name__ = "Integer32"
_BufServicePoolID_Object = MibTableColumn
bufServicePoolID = _BufServicePoolID_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 1),
    _BufServicePoolID_Type()
)
bufServicePoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufServicePoolID.setStatus("current")
_BufMin_Type = Integer32
_BufMin_Object = MibTableColumn
bufMin = _BufMin_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 2),
    _BufMin_Type()
)
bufMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufMin.setStatus("current")
_BufMax_Type = Integer32
_BufMax_Object = MibTableColumn
bufMax = _BufMax_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 3),
    _BufMax_Type()
)
bufMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufMax.setStatus("current")
_BufAvg_Type = DisplayString
_BufAvg_Object = MibTableColumn
bufAvg = _BufAvg_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 4),
    _BufAvg_Type()
)
bufAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufAvg.setStatus("current")
_BufVariance_Type = DisplayString
_BufVariance_Object = MibTableColumn
bufVariance = _BufVariance_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 5),
    _BufVariance_Type()
)
bufVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufVariance.setStatus("current")
_BufStdDev_Type = DisplayString
_BufStdDev_Object = MibTableColumn
bufStdDev = _BufStdDev_Object(
    (1, 3, 6, 1, 4, 1, 40310, 1, 3, 4, 1, 6),
    _BufStdDev_Type()
)
bufStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufStdDev.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CUMULUS-RESOURCES-MIB",
    **{"resourceUtilization": resourceUtilization,
       "l3Tables": l3Tables,
       "l3HostTableCurrentEntries": l3HostTableCurrentEntries,
       "l3HostTableMaxEntries": l3HostTableMaxEntries,
       "l3RoutingTableCurrentEntries": l3RoutingTableCurrentEntries,
       "l3RoutingTableMaxEntries": l3RoutingTableMaxEntries,
       "l3NextHopTableCurrentEntries": l3NextHopTableCurrentEntries,
       "l3NextHopTableMaxEntries": l3NextHopTableMaxEntries,
       "l3EcmpGroupTableCurrentEntries": l3EcmpGroupTableCurrentEntries,
       "l3EcmpGroupTableMaxEntries": l3EcmpGroupTableMaxEntries,
       "l3EcmpNextHopTableCurrentEntries": l3EcmpNextHopTableCurrentEntries,
       "l3EcmpNextHopTableMaxEntries": l3EcmpNextHopTableMaxEntries,
       "l2Tables": l2Tables,
       "l2MacTableCurrentEntries": l2MacTableCurrentEntries,
       "l2MacTableMaxEntries": l2MacTableMaxEntries,
       "l2CacheTableCurrentEntries": l2CacheTableCurrentEntries,
       "l2CacheTableMaxEntries": l2CacheTableMaxEntries,
       "bufferUtilizn": bufferUtilizn,
       "bufUtiliznComputeTime": bufUtiliznComputeTime,
       "bufUtiliznPollInterval": bufUtiliznPollInterval,
       "bufUtiliznMeasureInterval": bufUtiliznMeasureInterval,
       "bufUtiliznTable": bufUtiliznTable,
       "bufUtiliznEntry": bufUtiliznEntry,
       "bufServicePoolID": bufServicePoolID,
       "bufMin": bufMin,
       "bufMax": bufMax,
       "bufAvg": bufAvg,
       "bufVariance": bufVariance,
       "bufStdDev": bufStdDev}
)
