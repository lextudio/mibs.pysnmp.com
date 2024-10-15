# SNMP MIB module (HIRSCHMANN-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIRSCHMANN-PIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:47 2024
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

(hmPlatform4Multicast,) = mibBuilder.importSymbols(
    "HIRSCHMANN-MULTICAST-MIB",
    "hmPlatform4Multicast")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ipMRouteGroup,
 ipMRouteNextHopAddress,
 ipMRouteNextHopGroup,
 ipMRouteNextHopIfIndex,
 ipMRouteNextHopSource,
 ipMRouteNextHopSourceMask,
 ipMRouteSource,
 ipMRouteSourceMask) = mibBuilder.importSymbols(
    "IPMROUTE-STD-MIB",
    "ipMRouteGroup",
    "ipMRouteNextHopAddress",
    "ipMRouteNextHopGroup",
    "ipMRouteNextHopIfIndex",
    "ipMRouteNextHopSource",
    "ipMRouteNextHopSourceMask",
    "ipMRouteSource",
    "ipMRouteSourceMask")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hmPIMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99)
)
hmPIMMIB.setRevisions(
        ("2006-02-06 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmPIMMIBObjects_ObjectIdentity = ObjectIdentity
hmPIMMIBObjects = _HmPIMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1)
)
_HmPIMTraps_ObjectIdentity = ObjectIdentity
hmPIMTraps = _HmPIMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 0)
)
_HmPIM_ObjectIdentity = ObjectIdentity
hmPIM = _HmPIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1)
)
_HmPIMJoinPruneInterval_Type = Integer32
_HmPIMJoinPruneInterval_Object = MibScalar
hmPIMJoinPruneInterval = _HmPIMJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 1),
    _HmPIMJoinPruneInterval_Type()
)
hmPIMJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPIMJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    hmPIMJoinPruneInterval.setUnits("seconds")
_HmPIMInterfaceTable_Object = MibTable
hmPIMInterfaceTable = _HmPIMInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hmPIMInterfaceTable.setStatus("current")
_HmPIMInterfaceEntry_Object = MibTableRow
hmPIMInterfaceEntry = _HmPIMInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1)
)
hmPIMInterfaceEntry.setIndexNames(
    (0, "HIRSCHMANN-PIM-MIB", "hmPIMInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hmPIMInterfaceEntry.setStatus("current")
_HmPIMInterfaceIfIndex_Type = InterfaceIndex
_HmPIMInterfaceIfIndex_Object = MibTableColumn
hmPIMInterfaceIfIndex = _HmPIMInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 1),
    _HmPIMInterfaceIfIndex_Type()
)
hmPIMInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmPIMInterfaceIfIndex.setStatus("current")
_HmPIMInterfaceAddress_Type = IpAddress
_HmPIMInterfaceAddress_Object = MibTableColumn
hmPIMInterfaceAddress = _HmPIMInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 2),
    _HmPIMInterfaceAddress_Type()
)
hmPIMInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMInterfaceAddress.setStatus("current")
_HmPIMInterfaceNetMask_Type = IpAddress
_HmPIMInterfaceNetMask_Object = MibTableColumn
hmPIMInterfaceNetMask = _HmPIMInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 3),
    _HmPIMInterfaceNetMask_Type()
)
hmPIMInterfaceNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMInterfaceNetMask.setStatus("current")


class _HmPIMInterfaceMode_Type(Integer32):
    """Custom type hmPIMInterfaceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2),
          ("sparseDense", 3))
    )


_HmPIMInterfaceMode_Type.__name__ = "Integer32"
_HmPIMInterfaceMode_Object = MibTableColumn
hmPIMInterfaceMode = _HmPIMInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 4),
    _HmPIMInterfaceMode_Type()
)
hmPIMInterfaceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmPIMInterfaceMode.setStatus("current")
_HmPIMInterfaceDR_Type = IpAddress
_HmPIMInterfaceDR_Object = MibTableColumn
hmPIMInterfaceDR = _HmPIMInterfaceDR_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 5),
    _HmPIMInterfaceDR_Type()
)
hmPIMInterfaceDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMInterfaceDR.setStatus("current")


class _HmPIMInterfaceHelloInterval_Type(Integer32):
    """Custom type hmPIMInterfaceHelloInterval based on Integer32"""
    defaultValue = 30


_HmPIMInterfaceHelloInterval_Object = MibTableColumn
hmPIMInterfaceHelloInterval = _HmPIMInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 6),
    _HmPIMInterfaceHelloInterval_Type()
)
hmPIMInterfaceHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmPIMInterfaceHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    hmPIMInterfaceHelloInterval.setUnits("seconds")
_HmPIMInterfaceStatus_Type = RowStatus
_HmPIMInterfaceStatus_Object = MibTableColumn
hmPIMInterfaceStatus = _HmPIMInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 7),
    _HmPIMInterfaceStatus_Type()
)
hmPIMInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmPIMInterfaceStatus.setStatus("current")
_HmPIMInterfaceJoinPruneInterval_Type = Integer32
_HmPIMInterfaceJoinPruneInterval_Object = MibTableColumn
hmPIMInterfaceJoinPruneInterval = _HmPIMInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 8),
    _HmPIMInterfaceJoinPruneInterval_Type()
)
hmPIMInterfaceJoinPruneInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmPIMInterfaceJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    hmPIMInterfaceJoinPruneInterval.setUnits("seconds")


class _HmPIMInterfaceCBSRPreference_Type(Integer32):
    """Custom type hmPIMInterfaceCBSRPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_HmPIMInterfaceCBSRPreference_Type.__name__ = "Integer32"
_HmPIMInterfaceCBSRPreference_Object = MibTableColumn
hmPIMInterfaceCBSRPreference = _HmPIMInterfaceCBSRPreference_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 9),
    _HmPIMInterfaceCBSRPreference_Type()
)
hmPIMInterfaceCBSRPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmPIMInterfaceCBSRPreference.setStatus("current")
_HmPIMNeighborTable_Object = MibTable
hmPIMNeighborTable = _HmPIMNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hmPIMNeighborTable.setStatus("current")
_HmPIMNeighborEntry_Object = MibTableRow
hmPIMNeighborEntry = _HmPIMNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1)
)
hmPIMNeighborEntry.setIndexNames(
    (0, "HIRSCHMANN-PIM-MIB", "hmPIMNeighborAddress"),
)
if mibBuilder.loadTexts:
    hmPIMNeighborEntry.setStatus("current")
_HmPIMNeighborAddress_Type = IpAddress
_HmPIMNeighborAddress_Object = MibTableColumn
hmPIMNeighborAddress = _HmPIMNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1, 1),
    _HmPIMNeighborAddress_Type()
)
hmPIMNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmPIMNeighborAddress.setStatus("current")
_HmPIMNeighborIfIndex_Type = InterfaceIndex
_HmPIMNeighborIfIndex_Object = MibTableColumn
hmPIMNeighborIfIndex = _HmPIMNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1, 2),
    _HmPIMNeighborIfIndex_Type()
)
hmPIMNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMNeighborIfIndex.setStatus("current")
_HmPIMNeighborUpTime_Type = TimeTicks
_HmPIMNeighborUpTime_Object = MibTableColumn
hmPIMNeighborUpTime = _HmPIMNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1, 3),
    _HmPIMNeighborUpTime_Type()
)
hmPIMNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMNeighborUpTime.setStatus("current")
_HmPIMNeighborExpiryTime_Type = TimeTicks
_HmPIMNeighborExpiryTime_Object = MibTableColumn
hmPIMNeighborExpiryTime = _HmPIMNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1, 4),
    _HmPIMNeighborExpiryTime_Type()
)
hmPIMNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMNeighborExpiryTime.setStatus("current")


class _HmPIMNeighborMode_Type(Integer32):
    """Custom type hmPIMNeighborMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2))
    )


_HmPIMNeighborMode_Type.__name__ = "Integer32"
_HmPIMNeighborMode_Object = MibTableColumn
hmPIMNeighborMode = _HmPIMNeighborMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1, 5),
    _HmPIMNeighborMode_Type()
)
hmPIMNeighborMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMNeighborMode.setStatus("deprecated")
_HmPIMIpMRouteTable_Object = MibTable
hmPIMIpMRouteTable = _HmPIMIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hmPIMIpMRouteTable.setStatus("current")
_HmPIMIpMRouteEntry_Object = MibTableRow
hmPIMIpMRouteEntry = _HmPIMIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1)
)
hmPIMIpMRouteEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    hmPIMIpMRouteEntry.setStatus("current")
_HmPIMIpMRouteUpstreamAssertTimer_Type = TimeTicks
_HmPIMIpMRouteUpstreamAssertTimer_Object = MibTableColumn
hmPIMIpMRouteUpstreamAssertTimer = _HmPIMIpMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1, 1),
    _HmPIMIpMRouteUpstreamAssertTimer_Type()
)
hmPIMIpMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMIpMRouteUpstreamAssertTimer.setStatus("current")
_HmPIMIpMRouteAssertMetric_Type = Integer32
_HmPIMIpMRouteAssertMetric_Object = MibTableColumn
hmPIMIpMRouteAssertMetric = _HmPIMIpMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1, 2),
    _HmPIMIpMRouteAssertMetric_Type()
)
hmPIMIpMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMIpMRouteAssertMetric.setStatus("current")
_HmPIMIpMRouteAssertMetricPref_Type = Integer32
_HmPIMIpMRouteAssertMetricPref_Object = MibTableColumn
hmPIMIpMRouteAssertMetricPref = _HmPIMIpMRouteAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1, 3),
    _HmPIMIpMRouteAssertMetricPref_Type()
)
hmPIMIpMRouteAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMIpMRouteAssertMetricPref.setStatus("current")
_HmPIMIpMRouteAssertRPTBit_Type = TruthValue
_HmPIMIpMRouteAssertRPTBit_Object = MibTableColumn
hmPIMIpMRouteAssertRPTBit = _HmPIMIpMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1, 4),
    _HmPIMIpMRouteAssertRPTBit_Type()
)
hmPIMIpMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMIpMRouteAssertRPTBit.setStatus("current")


class _HmPIMIpMRouteFlags_Type(Bits):
    """Custom type hmPIMIpMRouteFlags based on Bits"""
    namedValues = NamedValues(
        *(("rpt", 0),
          ("spt", 1))
    )

_HmPIMIpMRouteFlags_Type.__name__ = "Bits"
_HmPIMIpMRouteFlags_Object = MibTableColumn
hmPIMIpMRouteFlags = _HmPIMIpMRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1, 5),
    _HmPIMIpMRouteFlags_Type()
)
hmPIMIpMRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMIpMRouteFlags.setStatus("current")
_HmPIMRPTable_Object = MibTable
hmPIMRPTable = _HmPIMRPTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hmPIMRPTable.setStatus("deprecated")
_HmPIMRPEntry_Object = MibTableRow
hmPIMRPEntry = _HmPIMRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1)
)
hmPIMRPEntry.setIndexNames(
    (0, "HIRSCHMANN-PIM-MIB", "hmPIMRPGroupAddress"),
    (0, "HIRSCHMANN-PIM-MIB", "hmPIMRPAddress"),
)
if mibBuilder.loadTexts:
    hmPIMRPEntry.setStatus("deprecated")
_HmPIMRPGroupAddress_Type = IpAddress
_HmPIMRPGroupAddress_Object = MibTableColumn
hmPIMRPGroupAddress = _HmPIMRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 1),
    _HmPIMRPGroupAddress_Type()
)
hmPIMRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmPIMRPGroupAddress.setStatus("deprecated")
_HmPIMRPAddress_Type = IpAddress
_HmPIMRPAddress_Object = MibTableColumn
hmPIMRPAddress = _HmPIMRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 2),
    _HmPIMRPAddress_Type()
)
hmPIMRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmPIMRPAddress.setStatus("deprecated")


class _HmPIMRPState_Type(Integer32):
    """Custom type hmPIMRPState based on Integer32"""
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


_HmPIMRPState_Type.__name__ = "Integer32"
_HmPIMRPState_Object = MibTableColumn
hmPIMRPState = _HmPIMRPState_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 3),
    _HmPIMRPState_Type()
)
hmPIMRPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMRPState.setStatus("deprecated")
_HmPIMRPStateTimer_Type = TimeTicks
_HmPIMRPStateTimer_Object = MibTableColumn
hmPIMRPStateTimer = _HmPIMRPStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 4),
    _HmPIMRPStateTimer_Type()
)
hmPIMRPStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMRPStateTimer.setStatus("deprecated")
_HmPIMRPLastChange_Type = TimeTicks
_HmPIMRPLastChange_Object = MibTableColumn
hmPIMRPLastChange = _HmPIMRPLastChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 5),
    _HmPIMRPLastChange_Type()
)
hmPIMRPLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMRPLastChange.setStatus("deprecated")
_HmPIMRPRowStatus_Type = RowStatus
_HmPIMRPRowStatus_Object = MibTableColumn
hmPIMRPRowStatus = _HmPIMRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 6),
    _HmPIMRPRowStatus_Type()
)
hmPIMRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmPIMRPRowStatus.setStatus("deprecated")
_HmPIMRPSetTable_Object = MibTable
hmPIMRPSetTable = _HmPIMRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hmPIMRPSetTable.setStatus("current")
_HmPIMRPSetEntry_Object = MibTableRow
hmPIMRPSetEntry = _HmPIMRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1)
)
hmPIMRPSetEntry.setIndexNames(
    (0, "HIRSCHMANN-PIM-MIB", "hmPIMRPSetComponent"),
    (0, "HIRSCHMANN-PIM-MIB", "hmPIMRPSetGroupAddress"),
    (0, "HIRSCHMANN-PIM-MIB", "hmPIMRPSetGroupMask"),
    (0, "HIRSCHMANN-PIM-MIB", "hmPIMRPSetAddress"),
)
if mibBuilder.loadTexts:
    hmPIMRPSetEntry.setStatus("current")
_HmPIMRPSetGroupAddress_Type = IpAddress
_HmPIMRPSetGroupAddress_Object = MibTableColumn
hmPIMRPSetGroupAddress = _HmPIMRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 1),
    _HmPIMRPSetGroupAddress_Type()
)
hmPIMRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmPIMRPSetGroupAddress.setStatus("current")
_HmPIMRPSetGroupMask_Type = IpAddress
_HmPIMRPSetGroupMask_Object = MibTableColumn
hmPIMRPSetGroupMask = _HmPIMRPSetGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 2),
    _HmPIMRPSetGroupMask_Type()
)
hmPIMRPSetGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmPIMRPSetGroupMask.setStatus("current")
_HmPIMRPSetAddress_Type = IpAddress
_HmPIMRPSetAddress_Object = MibTableColumn
hmPIMRPSetAddress = _HmPIMRPSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 3),
    _HmPIMRPSetAddress_Type()
)
hmPIMRPSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmPIMRPSetAddress.setStatus("current")


class _HmPIMRPSetHoldTime_Type(Integer32):
    """Custom type hmPIMRPSetHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmPIMRPSetHoldTime_Type.__name__ = "Integer32"
_HmPIMRPSetHoldTime_Object = MibTableColumn
hmPIMRPSetHoldTime = _HmPIMRPSetHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 4),
    _HmPIMRPSetHoldTime_Type()
)
hmPIMRPSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMRPSetHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    hmPIMRPSetHoldTime.setUnits("seconds")
_HmPIMRPSetExpiryTime_Type = TimeTicks
_HmPIMRPSetExpiryTime_Object = MibTableColumn
hmPIMRPSetExpiryTime = _HmPIMRPSetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 5),
    _HmPIMRPSetExpiryTime_Type()
)
hmPIMRPSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMRPSetExpiryTime.setStatus("current")


class _HmPIMRPSetComponent_Type(Integer32):
    """Custom type hmPIMRPSetComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmPIMRPSetComponent_Type.__name__ = "Integer32"
_HmPIMRPSetComponent_Object = MibTableColumn
hmPIMRPSetComponent = _HmPIMRPSetComponent_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 6),
    _HmPIMRPSetComponent_Type()
)
hmPIMRPSetComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmPIMRPSetComponent.setStatus("current")
_HmPIMIpMRouteNextHopTable_Object = MibTable
hmPIMIpMRouteNextHopTable = _HmPIMIpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hmPIMIpMRouteNextHopTable.setStatus("current")
_HmPIMIpMRouteNextHopEntry_Object = MibTableRow
hmPIMIpMRouteNextHopEntry = _HmPIMIpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 7, 1)
)
hmPIMIpMRouteNextHopEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSourceMask"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopIfIndex"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    hmPIMIpMRouteNextHopEntry.setStatus("current")


class _HmPIMIpMRouteNextHopPruneReason_Type(Integer32):
    """Custom type hmPIMIpMRouteNextHopPruneReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assert", 3),
          ("other", 1),
          ("prune", 2))
    )


_HmPIMIpMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_HmPIMIpMRouteNextHopPruneReason_Object = MibTableColumn
hmPIMIpMRouteNextHopPruneReason = _HmPIMIpMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 7, 1, 2),
    _HmPIMIpMRouteNextHopPruneReason_Type()
)
hmPIMIpMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMIpMRouteNextHopPruneReason.setStatus("current")
_HmPIMCandidateRPTable_Object = MibTable
hmPIMCandidateRPTable = _HmPIMCandidateRPTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11)
)
if mibBuilder.loadTexts:
    hmPIMCandidateRPTable.setStatus("current")
_HmPIMCandidateRPEntry_Object = MibTableRow
hmPIMCandidateRPEntry = _HmPIMCandidateRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11, 1)
)
hmPIMCandidateRPEntry.setIndexNames(
    (0, "HIRSCHMANN-PIM-MIB", "hmPIMCandidateRPGroupAddress"),
    (0, "HIRSCHMANN-PIM-MIB", "hmPIMCandidateRPGroupMask"),
)
if mibBuilder.loadTexts:
    hmPIMCandidateRPEntry.setStatus("current")
_HmPIMCandidateRPGroupAddress_Type = IpAddress
_HmPIMCandidateRPGroupAddress_Object = MibTableColumn
hmPIMCandidateRPGroupAddress = _HmPIMCandidateRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11, 1, 1),
    _HmPIMCandidateRPGroupAddress_Type()
)
hmPIMCandidateRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmPIMCandidateRPGroupAddress.setStatus("current")
_HmPIMCandidateRPGroupMask_Type = IpAddress
_HmPIMCandidateRPGroupMask_Object = MibTableColumn
hmPIMCandidateRPGroupMask = _HmPIMCandidateRPGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11, 1, 2),
    _HmPIMCandidateRPGroupMask_Type()
)
hmPIMCandidateRPGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmPIMCandidateRPGroupMask.setStatus("current")
_HmPIMCandidateRPAddress_Type = IpAddress
_HmPIMCandidateRPAddress_Object = MibTableColumn
hmPIMCandidateRPAddress = _HmPIMCandidateRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11, 1, 3),
    _HmPIMCandidateRPAddress_Type()
)
hmPIMCandidateRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmPIMCandidateRPAddress.setStatus("current")
_HmPIMCandidateRPRowStatus_Type = RowStatus
_HmPIMCandidateRPRowStatus_Object = MibTableColumn
hmPIMCandidateRPRowStatus = _HmPIMCandidateRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11, 1, 4),
    _HmPIMCandidateRPRowStatus_Type()
)
hmPIMCandidateRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmPIMCandidateRPRowStatus.setStatus("current")
_HmPIMComponentTable_Object = MibTable
hmPIMComponentTable = _HmPIMComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hmPIMComponentTable.setStatus("current")
_HmPIMComponentEntry_Object = MibTableRow
hmPIMComponentEntry = _HmPIMComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1)
)
hmPIMComponentEntry.setIndexNames(
    (0, "HIRSCHMANN-PIM-MIB", "hmPIMComponentIndex"),
)
if mibBuilder.loadTexts:
    hmPIMComponentEntry.setStatus("current")


class _HmPIMComponentIndex_Type(Integer32):
    """Custom type hmPIMComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmPIMComponentIndex_Type.__name__ = "Integer32"
_HmPIMComponentIndex_Object = MibTableColumn
hmPIMComponentIndex = _HmPIMComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1, 1),
    _HmPIMComponentIndex_Type()
)
hmPIMComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmPIMComponentIndex.setStatus("current")
_HmPIMComponentBSRAddress_Type = IpAddress
_HmPIMComponentBSRAddress_Object = MibTableColumn
hmPIMComponentBSRAddress = _HmPIMComponentBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1, 2),
    _HmPIMComponentBSRAddress_Type()
)
hmPIMComponentBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMComponentBSRAddress.setStatus("current")
_HmPIMComponentBSRExpiryTime_Type = TimeTicks
_HmPIMComponentBSRExpiryTime_Object = MibTableColumn
hmPIMComponentBSRExpiryTime = _HmPIMComponentBSRExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1, 3),
    _HmPIMComponentBSRExpiryTime_Type()
)
hmPIMComponentBSRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPIMComponentBSRExpiryTime.setStatus("current")


class _HmPIMComponentCRPHoldTime_Type(Integer32):
    """Custom type hmPIMComponentCRPHoldTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmPIMComponentCRPHoldTime_Type.__name__ = "Integer32"
_HmPIMComponentCRPHoldTime_Object = MibTableColumn
hmPIMComponentCRPHoldTime = _HmPIMComponentCRPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1, 4),
    _HmPIMComponentCRPHoldTime_Type()
)
hmPIMComponentCRPHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmPIMComponentCRPHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    hmPIMComponentCRPHoldTime.setUnits("seconds")
_HmPIMComponentStatus_Type = RowStatus
_HmPIMComponentStatus_Object = MibTableColumn
hmPIMComponentStatus = _HmPIMComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1, 5),
    _HmPIMComponentStatus_Type()
)
hmPIMComponentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmPIMComponentStatus.setStatus("current")
_HmPIMMIBConformance_ObjectIdentity = ObjectIdentity
hmPIMMIBConformance = _HmPIMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2)
)
_HmPIMMIBCompliances_ObjectIdentity = ObjectIdentity
hmPIMMIBCompliances = _HmPIMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 1)
)
_HmPIMMIBGroups_ObjectIdentity = ObjectIdentity
hmPIMMIBGroups = _HmPIMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2)
)

# Managed Objects groups

hmPIMV2MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 2)
)
hmPIMV2MIBGroup.setObjects(
      *(("HIRSCHMANN-PIM-MIB", "hmPIMJoinPruneInterval"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborIfIndex"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborUpTime"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborExpiryTime"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceAddress"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceNetMask"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceDR"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceHelloInterval"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceStatus"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceJoinPruneInterval"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceCBSRPreference"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceMode"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMRPSetHoldTime"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMRPSetExpiryTime"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMComponentBSRAddress"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMComponentBSRExpiryTime"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMComponentCRPHoldTime"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMComponentStatus"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteFlags"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteUpstreamAssertTimer"))
)
if mibBuilder.loadTexts:
    hmPIMV2MIBGroup.setStatus("current")

hmPIMV2CandidateRPMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 3)
)
hmPIMV2CandidateRPMIBGroup.setObjects(
      *(("HIRSCHMANN-PIM-MIB", "hmPIMCandidateRPAddress"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMCandidateRPRowStatus"))
)
if mibBuilder.loadTexts:
    hmPIMV2CandidateRPMIBGroup.setStatus("current")

hmPIMV1MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 4)
)
hmPIMV1MIBGroup.setObjects(
      *(("HIRSCHMANN-PIM-MIB", "hmPIMJoinPruneInterval"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborIfIndex"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborUpTime"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborExpiryTime"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborMode"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceAddress"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceNetMask"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceJoinPruneInterval"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceStatus"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceMode"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceDR"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceHelloInterval"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMRPState"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMRPStateTimer"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMRPLastChange"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMRPRowStatus"))
)
if mibBuilder.loadTexts:
    hmPIMV1MIBGroup.setStatus("deprecated")

hmPIMDenseV2MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 5)
)
hmPIMDenseV2MIBGroup.setObjects(
      *(("HIRSCHMANN-PIM-MIB", "hmPIMNeighborIfIndex"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborUpTime"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborExpiryTime"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceAddress"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceNetMask"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceDR"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceHelloInterval"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceStatus"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceMode"))
)
if mibBuilder.loadTexts:
    hmPIMDenseV2MIBGroup.setStatus("current")

hmPIMNextHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 6)
)
hmPIMNextHopGroup.setObjects(
    ("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteNextHopPruneReason")
)
if mibBuilder.loadTexts:
    hmPIMNextHopGroup.setStatus("current")

hmPIMAssertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 7)
)
hmPIMAssertGroup.setObjects(
      *(("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteAssertMetric"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteAssertMetricPref"),
        ("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteAssertRPTBit"))
)
if mibBuilder.loadTexts:
    hmPIMAssertGroup.setStatus("current")


# Notification objects

hmPIMNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 0, 1)
)
hmPIMNeighborLoss.setObjects(
    ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborIfIndex")
)
if mibBuilder.loadTexts:
    hmPIMNeighborLoss.setStatus(
        "current"
    )


# Notifications groups

hmPIMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 1)
)
hmPIMNotificationGroup.setObjects(
    ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborLoss")
)
if mibBuilder.loadTexts:
    hmPIMNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hmPIMV1MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hmPIMV1MIBCompliance.setStatus(
        "deprecated"
    )

hmPIMSparseV2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hmPIMSparseV2MIBCompliance.setStatus(
        "current"
    )

hmPIMDenseV2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hmPIMDenseV2MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-PIM-MIB",
    **{"hmPIMMIB": hmPIMMIB,
       "hmPIMMIBObjects": hmPIMMIBObjects,
       "hmPIMTraps": hmPIMTraps,
       "hmPIMNeighborLoss": hmPIMNeighborLoss,
       "hmPIM": hmPIM,
       "hmPIMJoinPruneInterval": hmPIMJoinPruneInterval,
       "hmPIMInterfaceTable": hmPIMInterfaceTable,
       "hmPIMInterfaceEntry": hmPIMInterfaceEntry,
       "hmPIMInterfaceIfIndex": hmPIMInterfaceIfIndex,
       "hmPIMInterfaceAddress": hmPIMInterfaceAddress,
       "hmPIMInterfaceNetMask": hmPIMInterfaceNetMask,
       "hmPIMInterfaceMode": hmPIMInterfaceMode,
       "hmPIMInterfaceDR": hmPIMInterfaceDR,
       "hmPIMInterfaceHelloInterval": hmPIMInterfaceHelloInterval,
       "hmPIMInterfaceStatus": hmPIMInterfaceStatus,
       "hmPIMInterfaceJoinPruneInterval": hmPIMInterfaceJoinPruneInterval,
       "hmPIMInterfaceCBSRPreference": hmPIMInterfaceCBSRPreference,
       "hmPIMNeighborTable": hmPIMNeighborTable,
       "hmPIMNeighborEntry": hmPIMNeighborEntry,
       "hmPIMNeighborAddress": hmPIMNeighborAddress,
       "hmPIMNeighborIfIndex": hmPIMNeighborIfIndex,
       "hmPIMNeighborUpTime": hmPIMNeighborUpTime,
       "hmPIMNeighborExpiryTime": hmPIMNeighborExpiryTime,
       "hmPIMNeighborMode": hmPIMNeighborMode,
       "hmPIMIpMRouteTable": hmPIMIpMRouteTable,
       "hmPIMIpMRouteEntry": hmPIMIpMRouteEntry,
       "hmPIMIpMRouteUpstreamAssertTimer": hmPIMIpMRouteUpstreamAssertTimer,
       "hmPIMIpMRouteAssertMetric": hmPIMIpMRouteAssertMetric,
       "hmPIMIpMRouteAssertMetricPref": hmPIMIpMRouteAssertMetricPref,
       "hmPIMIpMRouteAssertRPTBit": hmPIMIpMRouteAssertRPTBit,
       "hmPIMIpMRouteFlags": hmPIMIpMRouteFlags,
       "hmPIMRPTable": hmPIMRPTable,
       "hmPIMRPEntry": hmPIMRPEntry,
       "hmPIMRPGroupAddress": hmPIMRPGroupAddress,
       "hmPIMRPAddress": hmPIMRPAddress,
       "hmPIMRPState": hmPIMRPState,
       "hmPIMRPStateTimer": hmPIMRPStateTimer,
       "hmPIMRPLastChange": hmPIMRPLastChange,
       "hmPIMRPRowStatus": hmPIMRPRowStatus,
       "hmPIMRPSetTable": hmPIMRPSetTable,
       "hmPIMRPSetEntry": hmPIMRPSetEntry,
       "hmPIMRPSetGroupAddress": hmPIMRPSetGroupAddress,
       "hmPIMRPSetGroupMask": hmPIMRPSetGroupMask,
       "hmPIMRPSetAddress": hmPIMRPSetAddress,
       "hmPIMRPSetHoldTime": hmPIMRPSetHoldTime,
       "hmPIMRPSetExpiryTime": hmPIMRPSetExpiryTime,
       "hmPIMRPSetComponent": hmPIMRPSetComponent,
       "hmPIMIpMRouteNextHopTable": hmPIMIpMRouteNextHopTable,
       "hmPIMIpMRouteNextHopEntry": hmPIMIpMRouteNextHopEntry,
       "hmPIMIpMRouteNextHopPruneReason": hmPIMIpMRouteNextHopPruneReason,
       "hmPIMCandidateRPTable": hmPIMCandidateRPTable,
       "hmPIMCandidateRPEntry": hmPIMCandidateRPEntry,
       "hmPIMCandidateRPGroupAddress": hmPIMCandidateRPGroupAddress,
       "hmPIMCandidateRPGroupMask": hmPIMCandidateRPGroupMask,
       "hmPIMCandidateRPAddress": hmPIMCandidateRPAddress,
       "hmPIMCandidateRPRowStatus": hmPIMCandidateRPRowStatus,
       "hmPIMComponentTable": hmPIMComponentTable,
       "hmPIMComponentEntry": hmPIMComponentEntry,
       "hmPIMComponentIndex": hmPIMComponentIndex,
       "hmPIMComponentBSRAddress": hmPIMComponentBSRAddress,
       "hmPIMComponentBSRExpiryTime": hmPIMComponentBSRExpiryTime,
       "hmPIMComponentCRPHoldTime": hmPIMComponentCRPHoldTime,
       "hmPIMComponentStatus": hmPIMComponentStatus,
       "hmPIMMIBConformance": hmPIMMIBConformance,
       "hmPIMMIBCompliances": hmPIMMIBCompliances,
       "hmPIMV1MIBCompliance": hmPIMV1MIBCompliance,
       "hmPIMSparseV2MIBCompliance": hmPIMSparseV2MIBCompliance,
       "hmPIMDenseV2MIBCompliance": hmPIMDenseV2MIBCompliance,
       "hmPIMMIBGroups": hmPIMMIBGroups,
       "hmPIMNotificationGroup": hmPIMNotificationGroup,
       "hmPIMV2MIBGroup": hmPIMV2MIBGroup,
       "hmPIMV2CandidateRPMIBGroup": hmPIMV2CandidateRPMIBGroup,
       "hmPIMV1MIBGroup": hmPIMV1MIBGroup,
       "hmPIMDenseV2MIBGroup": hmPIMDenseV2MIBGroup,
       "hmPIMNextHopGroup": hmPIMNextHopGroup,
       "hmPIMAssertGroup": hmPIMAssertGroup}
)
