# SNMP MIB module (PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:27 2024
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
 experimental,
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
    "experimental",
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

pimMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 61)
)
pimMIB.setRevisions(
        ("2000-09-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PimMIBObjects_ObjectIdentity = ObjectIdentity
pimMIBObjects = _PimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 61, 1)
)
_PimTraps_ObjectIdentity = ObjectIdentity
pimTraps = _PimTraps_ObjectIdentity(
    (1, 3, 6, 1, 3, 61, 1, 0)
)
_Pim_ObjectIdentity = ObjectIdentity
pim = _Pim_ObjectIdentity(
    (1, 3, 6, 1, 3, 61, 1, 1)
)
_PimJoinPruneInterval_Type = Integer32
_PimJoinPruneInterval_Object = MibScalar
pimJoinPruneInterval = _PimJoinPruneInterval_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 1),
    _PimJoinPruneInterval_Type()
)
pimJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    pimJoinPruneInterval.setUnits("seconds")
_PimInterfaceTable_Object = MibTable
pimInterfaceTable = _PimInterfaceTable_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pimInterfaceTable.setStatus("current")
_PimInterfaceEntry_Object = MibTableRow
pimInterfaceEntry = _PimInterfaceEntry_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 2, 1)
)
pimInterfaceEntry.setIndexNames(
    (0, "PIM-MIB", "pimInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    pimInterfaceEntry.setStatus("current")
_PimInterfaceIfIndex_Type = InterfaceIndex
_PimInterfaceIfIndex_Object = MibTableColumn
pimInterfaceIfIndex = _PimInterfaceIfIndex_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 1),
    _PimInterfaceIfIndex_Type()
)
pimInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimInterfaceIfIndex.setStatus("current")
_PimInterfaceAddress_Type = IpAddress
_PimInterfaceAddress_Object = MibTableColumn
pimInterfaceAddress = _PimInterfaceAddress_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 2),
    _PimInterfaceAddress_Type()
)
pimInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceAddress.setStatus("current")
_PimInterfaceNetMask_Type = IpAddress
_PimInterfaceNetMask_Object = MibTableColumn
pimInterfaceNetMask = _PimInterfaceNetMask_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 3),
    _PimInterfaceNetMask_Type()
)
pimInterfaceNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceNetMask.setStatus("current")


class _PimInterfaceMode_Type(Integer32):
    """Custom type pimInterfaceMode based on Integer32"""
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


_PimInterfaceMode_Type.__name__ = "Integer32"
_PimInterfaceMode_Object = MibTableColumn
pimInterfaceMode = _PimInterfaceMode_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 4),
    _PimInterfaceMode_Type()
)
pimInterfaceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceMode.setStatus("current")
_PimInterfaceDR_Type = IpAddress
_PimInterfaceDR_Object = MibTableColumn
pimInterfaceDR = _PimInterfaceDR_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 5),
    _PimInterfaceDR_Type()
)
pimInterfaceDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceDR.setStatus("current")


class _PimInterfaceHelloInterval_Type(Integer32):
    """Custom type pimInterfaceHelloInterval based on Integer32"""
    defaultValue = 30


_PimInterfaceHelloInterval_Object = MibTableColumn
pimInterfaceHelloInterval = _PimInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 6),
    _PimInterfaceHelloInterval_Type()
)
pimInterfaceHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceHelloInterval.setUnits("seconds")
_PimInterfaceStatus_Type = RowStatus
_PimInterfaceStatus_Object = MibTableColumn
pimInterfaceStatus = _PimInterfaceStatus_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 7),
    _PimInterfaceStatus_Type()
)
pimInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceStatus.setStatus("current")
_PimInterfaceJoinPruneInterval_Type = Integer32
_PimInterfaceJoinPruneInterval_Object = MibTableColumn
pimInterfaceJoinPruneInterval = _PimInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 8),
    _PimInterfaceJoinPruneInterval_Type()
)
pimInterfaceJoinPruneInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceJoinPruneInterval.setUnits("seconds")


class _PimInterfaceCBSRPreference_Type(Integer32):
    """Custom type pimInterfaceCBSRPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_PimInterfaceCBSRPreference_Type.__name__ = "Integer32"
_PimInterfaceCBSRPreference_Object = MibTableColumn
pimInterfaceCBSRPreference = _PimInterfaceCBSRPreference_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 9),
    _PimInterfaceCBSRPreference_Type()
)
pimInterfaceCBSRPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceCBSRPreference.setStatus("current")
_PimNeighborTable_Object = MibTable
pimNeighborTable = _PimNeighborTable_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pimNeighborTable.setStatus("current")
_PimNeighborEntry_Object = MibTableRow
pimNeighborEntry = _PimNeighborEntry_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 3, 1)
)
pimNeighborEntry.setIndexNames(
    (0, "PIM-MIB", "pimNeighborAddress"),
)
if mibBuilder.loadTexts:
    pimNeighborEntry.setStatus("current")
_PimNeighborAddress_Type = IpAddress
_PimNeighborAddress_Object = MibTableColumn
pimNeighborAddress = _PimNeighborAddress_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 1),
    _PimNeighborAddress_Type()
)
pimNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimNeighborAddress.setStatus("current")
_PimNeighborIfIndex_Type = InterfaceIndex
_PimNeighborIfIndex_Object = MibTableColumn
pimNeighborIfIndex = _PimNeighborIfIndex_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 2),
    _PimNeighborIfIndex_Type()
)
pimNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborIfIndex.setStatus("current")
_PimNeighborUpTime_Type = TimeTicks
_PimNeighborUpTime_Object = MibTableColumn
pimNeighborUpTime = _PimNeighborUpTime_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 3),
    _PimNeighborUpTime_Type()
)
pimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborUpTime.setStatus("current")
_PimNeighborExpiryTime_Type = TimeTicks
_PimNeighborExpiryTime_Object = MibTableColumn
pimNeighborExpiryTime = _PimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 4),
    _PimNeighborExpiryTime_Type()
)
pimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborExpiryTime.setStatus("current")


class _PimNeighborMode_Type(Integer32):
    """Custom type pimNeighborMode based on Integer32"""
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


_PimNeighborMode_Type.__name__ = "Integer32"
_PimNeighborMode_Object = MibTableColumn
pimNeighborMode = _PimNeighborMode_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 5),
    _PimNeighborMode_Type()
)
pimNeighborMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborMode.setStatus("deprecated")
_PimIpMRouteTable_Object = MibTable
pimIpMRouteTable = _PimIpMRouteTable_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pimIpMRouteTable.setStatus("current")
_PimIpMRouteEntry_Object = MibTableRow
pimIpMRouteEntry = _PimIpMRouteEntry_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 4, 1)
)
pimIpMRouteEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    pimIpMRouteEntry.setStatus("current")
_PimIpMRouteUpstreamAssertTimer_Type = TimeTicks
_PimIpMRouteUpstreamAssertTimer_Object = MibTableColumn
pimIpMRouteUpstreamAssertTimer = _PimIpMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 1),
    _PimIpMRouteUpstreamAssertTimer_Type()
)
pimIpMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimIpMRouteUpstreamAssertTimer.setStatus("current")
_PimIpMRouteAssertMetric_Type = Integer32
_PimIpMRouteAssertMetric_Object = MibTableColumn
pimIpMRouteAssertMetric = _PimIpMRouteAssertMetric_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 2),
    _PimIpMRouteAssertMetric_Type()
)
pimIpMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimIpMRouteAssertMetric.setStatus("current")
_PimIpMRouteAssertMetricPref_Type = Integer32
_PimIpMRouteAssertMetricPref_Object = MibTableColumn
pimIpMRouteAssertMetricPref = _PimIpMRouteAssertMetricPref_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 3),
    _PimIpMRouteAssertMetricPref_Type()
)
pimIpMRouteAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimIpMRouteAssertMetricPref.setStatus("current")
_PimIpMRouteAssertRPTBit_Type = TruthValue
_PimIpMRouteAssertRPTBit_Object = MibTableColumn
pimIpMRouteAssertRPTBit = _PimIpMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 4),
    _PimIpMRouteAssertRPTBit_Type()
)
pimIpMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimIpMRouteAssertRPTBit.setStatus("current")


class _PimIpMRouteFlags_Type(Bits):
    """Custom type pimIpMRouteFlags based on Bits"""
    namedValues = NamedValues(
        *(("rpt", 0),
          ("spt", 1))
    )

_PimIpMRouteFlags_Type.__name__ = "Bits"
_PimIpMRouteFlags_Object = MibTableColumn
pimIpMRouteFlags = _PimIpMRouteFlags_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 5),
    _PimIpMRouteFlags_Type()
)
pimIpMRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimIpMRouteFlags.setStatus("current")
_PimRPTable_Object = MibTable
pimRPTable = _PimRPTable_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 5)
)
if mibBuilder.loadTexts:
    pimRPTable.setStatus("deprecated")
_PimRPEntry_Object = MibTableRow
pimRPEntry = _PimRPEntry_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 5, 1)
)
pimRPEntry.setIndexNames(
    (0, "PIM-MIB", "pimRPGroupAddress"),
    (0, "PIM-MIB", "pimRPAddress"),
)
if mibBuilder.loadTexts:
    pimRPEntry.setStatus("deprecated")
_PimRPGroupAddress_Type = IpAddress
_PimRPGroupAddress_Object = MibTableColumn
pimRPGroupAddress = _PimRPGroupAddress_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 1),
    _PimRPGroupAddress_Type()
)
pimRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimRPGroupAddress.setStatus("deprecated")
_PimRPAddress_Type = IpAddress
_PimRPAddress_Object = MibTableColumn
pimRPAddress = _PimRPAddress_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 2),
    _PimRPAddress_Type()
)
pimRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimRPAddress.setStatus("deprecated")


class _PimRPState_Type(Integer32):
    """Custom type pimRPState based on Integer32"""
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


_PimRPState_Type.__name__ = "Integer32"
_PimRPState_Object = MibTableColumn
pimRPState = _PimRPState_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 3),
    _PimRPState_Type()
)
pimRPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimRPState.setStatus("deprecated")
_PimRPStateTimer_Type = TimeTicks
_PimRPStateTimer_Object = MibTableColumn
pimRPStateTimer = _PimRPStateTimer_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 4),
    _PimRPStateTimer_Type()
)
pimRPStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimRPStateTimer.setStatus("deprecated")
_PimRPLastChange_Type = TimeTicks
_PimRPLastChange_Object = MibTableColumn
pimRPLastChange = _PimRPLastChange_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 5),
    _PimRPLastChange_Type()
)
pimRPLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimRPLastChange.setStatus("deprecated")
_PimRPRowStatus_Type = RowStatus
_PimRPRowStatus_Object = MibTableColumn
pimRPRowStatus = _PimRPRowStatus_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 6),
    _PimRPRowStatus_Type()
)
pimRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimRPRowStatus.setStatus("deprecated")
_PimRPSetTable_Object = MibTable
pimRPSetTable = _PimRPSetTable_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 6)
)
if mibBuilder.loadTexts:
    pimRPSetTable.setStatus("current")
_PimRPSetEntry_Object = MibTableRow
pimRPSetEntry = _PimRPSetEntry_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 6, 1)
)
pimRPSetEntry.setIndexNames(
    (0, "PIM-MIB", "pimRPSetComponent"),
    (0, "PIM-MIB", "pimRPSetGroupAddress"),
    (0, "PIM-MIB", "pimRPSetGroupMask"),
    (0, "PIM-MIB", "pimRPSetAddress"),
)
if mibBuilder.loadTexts:
    pimRPSetEntry.setStatus("current")
_PimRPSetGroupAddress_Type = IpAddress
_PimRPSetGroupAddress_Object = MibTableColumn
pimRPSetGroupAddress = _PimRPSetGroupAddress_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 1),
    _PimRPSetGroupAddress_Type()
)
pimRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimRPSetGroupAddress.setStatus("current")
_PimRPSetGroupMask_Type = IpAddress
_PimRPSetGroupMask_Object = MibTableColumn
pimRPSetGroupMask = _PimRPSetGroupMask_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 2),
    _PimRPSetGroupMask_Type()
)
pimRPSetGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimRPSetGroupMask.setStatus("current")
_PimRPSetAddress_Type = IpAddress
_PimRPSetAddress_Object = MibTableColumn
pimRPSetAddress = _PimRPSetAddress_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 3),
    _PimRPSetAddress_Type()
)
pimRPSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimRPSetAddress.setStatus("current")


class _PimRPSetHoldTime_Type(Integer32):
    """Custom type pimRPSetHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PimRPSetHoldTime_Type.__name__ = "Integer32"
_PimRPSetHoldTime_Object = MibTableColumn
pimRPSetHoldTime = _PimRPSetHoldTime_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 4),
    _PimRPSetHoldTime_Type()
)
pimRPSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimRPSetHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    pimRPSetHoldTime.setUnits("seconds")
_PimRPSetExpiryTime_Type = TimeTicks
_PimRPSetExpiryTime_Object = MibTableColumn
pimRPSetExpiryTime = _PimRPSetExpiryTime_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 5),
    _PimRPSetExpiryTime_Type()
)
pimRPSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimRPSetExpiryTime.setStatus("current")


class _PimRPSetComponent_Type(Integer32):
    """Custom type pimRPSetComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PimRPSetComponent_Type.__name__ = "Integer32"
_PimRPSetComponent_Object = MibTableColumn
pimRPSetComponent = _PimRPSetComponent_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 6),
    _PimRPSetComponent_Type()
)
pimRPSetComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimRPSetComponent.setStatus("current")
_PimIpMRouteNextHopTable_Object = MibTable
pimIpMRouteNextHopTable = _PimIpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 7)
)
if mibBuilder.loadTexts:
    pimIpMRouteNextHopTable.setStatus("current")
_PimIpMRouteNextHopEntry_Object = MibTableRow
pimIpMRouteNextHopEntry = _PimIpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 7, 1)
)
pimIpMRouteNextHopEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSourceMask"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopIfIndex"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    pimIpMRouteNextHopEntry.setStatus("current")


class _PimIpMRouteNextHopPruneReason_Type(Integer32):
    """Custom type pimIpMRouteNextHopPruneReason based on Integer32"""
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


_PimIpMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_PimIpMRouteNextHopPruneReason_Object = MibTableColumn
pimIpMRouteNextHopPruneReason = _PimIpMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 7, 1, 2),
    _PimIpMRouteNextHopPruneReason_Type()
)
pimIpMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimIpMRouteNextHopPruneReason.setStatus("current")
_PimCandidateRPTable_Object = MibTable
pimCandidateRPTable = _PimCandidateRPTable_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 11)
)
if mibBuilder.loadTexts:
    pimCandidateRPTable.setStatus("current")
_PimCandidateRPEntry_Object = MibTableRow
pimCandidateRPEntry = _PimCandidateRPEntry_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 11, 1)
)
pimCandidateRPEntry.setIndexNames(
    (0, "PIM-MIB", "pimCandidateRPGroupAddress"),
    (0, "PIM-MIB", "pimCandidateRPGroupMask"),
)
if mibBuilder.loadTexts:
    pimCandidateRPEntry.setStatus("current")
_PimCandidateRPGroupAddress_Type = IpAddress
_PimCandidateRPGroupAddress_Object = MibTableColumn
pimCandidateRPGroupAddress = _PimCandidateRPGroupAddress_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 1),
    _PimCandidateRPGroupAddress_Type()
)
pimCandidateRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimCandidateRPGroupAddress.setStatus("current")
_PimCandidateRPGroupMask_Type = IpAddress
_PimCandidateRPGroupMask_Object = MibTableColumn
pimCandidateRPGroupMask = _PimCandidateRPGroupMask_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 2),
    _PimCandidateRPGroupMask_Type()
)
pimCandidateRPGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimCandidateRPGroupMask.setStatus("current")
_PimCandidateRPAddress_Type = IpAddress
_PimCandidateRPAddress_Object = MibTableColumn
pimCandidateRPAddress = _PimCandidateRPAddress_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 3),
    _PimCandidateRPAddress_Type()
)
pimCandidateRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimCandidateRPAddress.setStatus("current")
_PimCandidateRPRowStatus_Type = RowStatus
_PimCandidateRPRowStatus_Object = MibTableColumn
pimCandidateRPRowStatus = _PimCandidateRPRowStatus_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 4),
    _PimCandidateRPRowStatus_Type()
)
pimCandidateRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimCandidateRPRowStatus.setStatus("current")
_PimComponentTable_Object = MibTable
pimComponentTable = _PimComponentTable_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 12)
)
if mibBuilder.loadTexts:
    pimComponentTable.setStatus("current")
_PimComponentEntry_Object = MibTableRow
pimComponentEntry = _PimComponentEntry_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 12, 1)
)
pimComponentEntry.setIndexNames(
    (0, "PIM-MIB", "pimComponentIndex"),
)
if mibBuilder.loadTexts:
    pimComponentEntry.setStatus("current")


class _PimComponentIndex_Type(Integer32):
    """Custom type pimComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PimComponentIndex_Type.__name__ = "Integer32"
_PimComponentIndex_Object = MibTableColumn
pimComponentIndex = _PimComponentIndex_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 1),
    _PimComponentIndex_Type()
)
pimComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimComponentIndex.setStatus("current")
_PimComponentBSRAddress_Type = IpAddress
_PimComponentBSRAddress_Object = MibTableColumn
pimComponentBSRAddress = _PimComponentBSRAddress_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 2),
    _PimComponentBSRAddress_Type()
)
pimComponentBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimComponentBSRAddress.setStatus("current")
_PimComponentBSRExpiryTime_Type = TimeTicks
_PimComponentBSRExpiryTime_Object = MibTableColumn
pimComponentBSRExpiryTime = _PimComponentBSRExpiryTime_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 3),
    _PimComponentBSRExpiryTime_Type()
)
pimComponentBSRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimComponentBSRExpiryTime.setStatus("current")


class _PimComponentCRPHoldTime_Type(Integer32):
    """Custom type pimComponentCRPHoldTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PimComponentCRPHoldTime_Type.__name__ = "Integer32"
_PimComponentCRPHoldTime_Object = MibTableColumn
pimComponentCRPHoldTime = _PimComponentCRPHoldTime_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 4),
    _PimComponentCRPHoldTime_Type()
)
pimComponentCRPHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimComponentCRPHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    pimComponentCRPHoldTime.setUnits("seconds")
_PimComponentStatus_Type = RowStatus
_PimComponentStatus_Object = MibTableColumn
pimComponentStatus = _PimComponentStatus_Object(
    (1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 5),
    _PimComponentStatus_Type()
)
pimComponentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimComponentStatus.setStatus("current")
_PimMIBConformance_ObjectIdentity = ObjectIdentity
pimMIBConformance = _PimMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 61, 2)
)
_PimMIBCompliances_ObjectIdentity = ObjectIdentity
pimMIBCompliances = _PimMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 61, 2, 1)
)
_PimMIBGroups_ObjectIdentity = ObjectIdentity
pimMIBGroups = _PimMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 61, 2, 2)
)

# Managed Objects groups

pimV2MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 61, 2, 2, 2)
)
pimV2MIBGroup.setObjects(
      *(("PIM-MIB", "pimJoinPruneInterval"),
        ("PIM-MIB", "pimNeighborIfIndex"),
        ("PIM-MIB", "pimNeighborUpTime"),
        ("PIM-MIB", "pimNeighborExpiryTime"),
        ("PIM-MIB", "pimInterfaceAddress"),
        ("PIM-MIB", "pimInterfaceNetMask"),
        ("PIM-MIB", "pimInterfaceDR"),
        ("PIM-MIB", "pimInterfaceHelloInterval"),
        ("PIM-MIB", "pimInterfaceStatus"),
        ("PIM-MIB", "pimInterfaceJoinPruneInterval"),
        ("PIM-MIB", "pimInterfaceCBSRPreference"),
        ("PIM-MIB", "pimInterfaceMode"),
        ("PIM-MIB", "pimRPSetHoldTime"),
        ("PIM-MIB", "pimRPSetExpiryTime"),
        ("PIM-MIB", "pimComponentBSRAddress"),
        ("PIM-MIB", "pimComponentBSRExpiryTime"),
        ("PIM-MIB", "pimComponentCRPHoldTime"),
        ("PIM-MIB", "pimComponentStatus"),
        ("PIM-MIB", "pimIpMRouteFlags"),
        ("PIM-MIB", "pimIpMRouteUpstreamAssertTimer"))
)
if mibBuilder.loadTexts:
    pimV2MIBGroup.setStatus("current")

pimV2CandidateRPMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 61, 2, 2, 3)
)
pimV2CandidateRPMIBGroup.setObjects(
      *(("PIM-MIB", "pimCandidateRPAddress"),
        ("PIM-MIB", "pimCandidateRPRowStatus"))
)
if mibBuilder.loadTexts:
    pimV2CandidateRPMIBGroup.setStatus("current")

pimV1MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 61, 2, 2, 4)
)
pimV1MIBGroup.setObjects(
      *(("PIM-MIB", "pimJoinPruneInterval"),
        ("PIM-MIB", "pimNeighborIfIndex"),
        ("PIM-MIB", "pimNeighborUpTime"),
        ("PIM-MIB", "pimNeighborExpiryTime"),
        ("PIM-MIB", "pimNeighborMode"),
        ("PIM-MIB", "pimInterfaceAddress"),
        ("PIM-MIB", "pimInterfaceNetMask"),
        ("PIM-MIB", "pimInterfaceJoinPruneInterval"),
        ("PIM-MIB", "pimInterfaceStatus"),
        ("PIM-MIB", "pimInterfaceMode"),
        ("PIM-MIB", "pimInterfaceDR"),
        ("PIM-MIB", "pimInterfaceHelloInterval"),
        ("PIM-MIB", "pimRPState"),
        ("PIM-MIB", "pimRPStateTimer"),
        ("PIM-MIB", "pimRPLastChange"),
        ("PIM-MIB", "pimRPRowStatus"))
)
if mibBuilder.loadTexts:
    pimV1MIBGroup.setStatus("deprecated")

pimDenseV2MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 61, 2, 2, 5)
)
pimDenseV2MIBGroup.setObjects(
      *(("PIM-MIB", "pimNeighborIfIndex"),
        ("PIM-MIB", "pimNeighborUpTime"),
        ("PIM-MIB", "pimNeighborExpiryTime"),
        ("PIM-MIB", "pimInterfaceAddress"),
        ("PIM-MIB", "pimInterfaceNetMask"),
        ("PIM-MIB", "pimInterfaceDR"),
        ("PIM-MIB", "pimInterfaceHelloInterval"),
        ("PIM-MIB", "pimInterfaceStatus"),
        ("PIM-MIB", "pimInterfaceMode"))
)
if mibBuilder.loadTexts:
    pimDenseV2MIBGroup.setStatus("current")

pimNextHopGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 61, 2, 2, 6)
)
pimNextHopGroup.setObjects(
    ("PIM-MIB", "pimIpMRouteNextHopPruneReason")
)
if mibBuilder.loadTexts:
    pimNextHopGroup.setStatus("current")

pimAssertGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 61, 2, 2, 7)
)
pimAssertGroup.setObjects(
      *(("PIM-MIB", "pimIpMRouteAssertMetric"),
        ("PIM-MIB", "pimIpMRouteAssertMetricPref"),
        ("PIM-MIB", "pimIpMRouteAssertRPTBit"))
)
if mibBuilder.loadTexts:
    pimAssertGroup.setStatus("current")


# Notification objects

pimNeighborLoss = NotificationType(
    (1, 3, 6, 1, 3, 61, 1, 0, 1)
)
pimNeighborLoss.setObjects(
    ("PIM-MIB", "pimNeighborIfIndex")
)
if mibBuilder.loadTexts:
    pimNeighborLoss.setStatus(
        "current"
    )


# Notifications groups

pimNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 61, 2, 2, 1)
)
pimNotificationGroup.setObjects(
    ("PIM-MIB", "pimNeighborLoss")
)
if mibBuilder.loadTexts:
    pimNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pimV1MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 61, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pimV1MIBCompliance.setStatus(
        "deprecated"
    )

pimSparseV2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 61, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pimSparseV2MIBCompliance.setStatus(
        "current"
    )

pimDenseV2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 61, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pimDenseV2MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PIM-MIB",
    **{"pimMIB": pimMIB,
       "pimMIBObjects": pimMIBObjects,
       "pimTraps": pimTraps,
       "pimNeighborLoss": pimNeighborLoss,
       "pim": pim,
       "pimJoinPruneInterval": pimJoinPruneInterval,
       "pimInterfaceTable": pimInterfaceTable,
       "pimInterfaceEntry": pimInterfaceEntry,
       "pimInterfaceIfIndex": pimInterfaceIfIndex,
       "pimInterfaceAddress": pimInterfaceAddress,
       "pimInterfaceNetMask": pimInterfaceNetMask,
       "pimInterfaceMode": pimInterfaceMode,
       "pimInterfaceDR": pimInterfaceDR,
       "pimInterfaceHelloInterval": pimInterfaceHelloInterval,
       "pimInterfaceStatus": pimInterfaceStatus,
       "pimInterfaceJoinPruneInterval": pimInterfaceJoinPruneInterval,
       "pimInterfaceCBSRPreference": pimInterfaceCBSRPreference,
       "pimNeighborTable": pimNeighborTable,
       "pimNeighborEntry": pimNeighborEntry,
       "pimNeighborAddress": pimNeighborAddress,
       "pimNeighborIfIndex": pimNeighborIfIndex,
       "pimNeighborUpTime": pimNeighborUpTime,
       "pimNeighborExpiryTime": pimNeighborExpiryTime,
       "pimNeighborMode": pimNeighborMode,
       "pimIpMRouteTable": pimIpMRouteTable,
       "pimIpMRouteEntry": pimIpMRouteEntry,
       "pimIpMRouteUpstreamAssertTimer": pimIpMRouteUpstreamAssertTimer,
       "pimIpMRouteAssertMetric": pimIpMRouteAssertMetric,
       "pimIpMRouteAssertMetricPref": pimIpMRouteAssertMetricPref,
       "pimIpMRouteAssertRPTBit": pimIpMRouteAssertRPTBit,
       "pimIpMRouteFlags": pimIpMRouteFlags,
       "pimRPTable": pimRPTable,
       "pimRPEntry": pimRPEntry,
       "pimRPGroupAddress": pimRPGroupAddress,
       "pimRPAddress": pimRPAddress,
       "pimRPState": pimRPState,
       "pimRPStateTimer": pimRPStateTimer,
       "pimRPLastChange": pimRPLastChange,
       "pimRPRowStatus": pimRPRowStatus,
       "pimRPSetTable": pimRPSetTable,
       "pimRPSetEntry": pimRPSetEntry,
       "pimRPSetGroupAddress": pimRPSetGroupAddress,
       "pimRPSetGroupMask": pimRPSetGroupMask,
       "pimRPSetAddress": pimRPSetAddress,
       "pimRPSetHoldTime": pimRPSetHoldTime,
       "pimRPSetExpiryTime": pimRPSetExpiryTime,
       "pimRPSetComponent": pimRPSetComponent,
       "pimIpMRouteNextHopTable": pimIpMRouteNextHopTable,
       "pimIpMRouteNextHopEntry": pimIpMRouteNextHopEntry,
       "pimIpMRouteNextHopPruneReason": pimIpMRouteNextHopPruneReason,
       "pimCandidateRPTable": pimCandidateRPTable,
       "pimCandidateRPEntry": pimCandidateRPEntry,
       "pimCandidateRPGroupAddress": pimCandidateRPGroupAddress,
       "pimCandidateRPGroupMask": pimCandidateRPGroupMask,
       "pimCandidateRPAddress": pimCandidateRPAddress,
       "pimCandidateRPRowStatus": pimCandidateRPRowStatus,
       "pimComponentTable": pimComponentTable,
       "pimComponentEntry": pimComponentEntry,
       "pimComponentIndex": pimComponentIndex,
       "pimComponentBSRAddress": pimComponentBSRAddress,
       "pimComponentBSRExpiryTime": pimComponentBSRExpiryTime,
       "pimComponentCRPHoldTime": pimComponentCRPHoldTime,
       "pimComponentStatus": pimComponentStatus,
       "pimMIBConformance": pimMIBConformance,
       "pimMIBCompliances": pimMIBCompliances,
       "pimV1MIBCompliance": pimV1MIBCompliance,
       "pimSparseV2MIBCompliance": pimSparseV2MIBCompliance,
       "pimDenseV2MIBCompliance": pimDenseV2MIBCompliance,
       "pimMIBGroups": pimMIBGroups,
       "pimNotificationGroup": pimNotificationGroup,
       "pimV2MIBGroup": pimV2MIBGroup,
       "pimV2CandidateRPMIBGroup": pimV2CandidateRPMIBGroup,
       "pimV1MIBGroup": pimV1MIBGroup,
       "pimDenseV2MIBGroup": pimDenseV2MIBGroup,
       "pimNextHopGroup": pimNextHopGroup,
       "pimAssertGroup": pimAssertGroup}
)
