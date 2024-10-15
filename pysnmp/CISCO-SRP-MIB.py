# SNMP MIB module (CISCO-SRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:44 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscosrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 60)
)
ciscosrpMIB.setRevisions(
        ("2005-12-19 00:00",
         "2001-03-28 00:00",
         "2000-04-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceSide(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sideA", 1),
          ("sideB", 2))
    )



class IpsMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("forcedSwitch", 6),
          ("manualSwitch", 3),
          ("noRequest", 1),
          ("signalDegrade", 4),
          ("signalFail", 5),
          ("waitToRestore", 2))
    )



class PerfCurrentCount64(Counter64, TextualConvention):
    status = "current"


class PerfIntervalCount64(Counter64, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_SrpMAC_ObjectIdentity = ObjectIdentity
srpMAC = _SrpMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1)
)
_SrpIfTable_Object = MibTable
srpIfTable = _SrpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 1)
)
if mibBuilder.loadTexts:
    srpIfTable.setStatus("current")
_SrpIfEntry_Object = MibTableRow
srpIfEntry = _SrpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 1, 1)
)
srpIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    srpIfEntry.setStatus("current")
_SrpMACAddress_Type = MacAddress
_SrpMACAddress_Object = MibTableColumn
srpMACAddress = _SrpMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 1, 1, 1),
    _SrpMACAddress_Type()
)
srpMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACAddress.setStatus("current")


class _SrpPriorityThreshold_Type(Integer32):
    """Custom type srpPriorityThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SrpPriorityThreshold_Type.__name__ = "Integer32"
_SrpPriorityThreshold_Object = MibTableColumn
srpPriorityThreshold = _SrpPriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 1, 1, 2),
    _SrpPriorityThreshold_Type()
)
srpPriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpPriorityThreshold.setStatus("current")


class _SrpNodesOnTheRing_Type(Integer32):
    """Custom type srpNodesOnTheRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SrpNodesOnTheRing_Type.__name__ = "Integer32"
_SrpNodesOnTheRing_Object = MibTableColumn
srpNodesOnTheRing = _SrpNodesOnTheRing_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 1, 1, 3),
    _SrpNodesOnTheRing_Type()
)
srpNodesOnTheRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpNodesOnTheRing.setStatus("current")


class _SrpIpsState_Type(Integer32):
    """Custom type srpIpsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("passThrough", 2),
          ("wrapped", 3))
    )


_SrpIpsState_Type.__name__ = "Integer32"
_SrpIpsState_Object = MibTableColumn
srpIpsState = _SrpIpsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 1, 1, 4),
    _SrpIpsState_Type()
)
srpIpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpIpsState.setStatus("current")
_SrpIpsLockedOut_Type = TruthValue
_SrpIpsLockedOut_Object = MibTableColumn
srpIpsLockedOut = _SrpIpsLockedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 1, 1, 5),
    _SrpIpsLockedOut_Type()
)
srpIpsLockedOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpIpsLockedOut.setStatus("current")


class _SrpIpsWaitToRestoreTimer_Type(Integer32):
    """Custom type srpIpsWaitToRestoreTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_SrpIpsWaitToRestoreTimer_Type.__name__ = "Integer32"
_SrpIpsWaitToRestoreTimer_Object = MibTableColumn
srpIpsWaitToRestoreTimer = _SrpIpsWaitToRestoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 1, 1, 6),
    _SrpIpsWaitToRestoreTimer_Type()
)
srpIpsWaitToRestoreTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpIpsWaitToRestoreTimer.setStatus("current")
if mibBuilder.loadTexts:
    srpIpsWaitToRestoreTimer.setUnits("seconds")


class _SrpIfTimeElapsed_Type(Integer32):
    """Custom type srpIfTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_SrpIfTimeElapsed_Type.__name__ = "Integer32"
_SrpIfTimeElapsed_Object = MibTableColumn
srpIfTimeElapsed = _SrpIfTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 1, 1, 7),
    _SrpIfTimeElapsed_Type()
)
srpIfTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpIfTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    srpIfTimeElapsed.setUnits("seconds")


class _SrpIfValidIntervals_Type(Integer32):
    """Custom type srpIfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_SrpIfValidIntervals_Type.__name__ = "Integer32"
_SrpIfValidIntervals_Object = MibTableColumn
srpIfValidIntervals = _SrpIfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 1, 1, 8),
    _SrpIfValidIntervals_Type()
)
srpIfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpIfValidIntervals.setStatus("current")
_SrpMACSideTable_Object = MibTable
srpMACSideTable = _SrpMACSideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2)
)
if mibBuilder.loadTexts:
    srpMACSideTable.setStatus("current")
_SrpMACSideEntry_Object = MibTableRow
srpMACSideEntry = _SrpMACSideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1)
)
srpMACSideEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SRP-MIB", "srpMACInterfaceSide"),
)
if mibBuilder.loadTexts:
    srpMACSideEntry.setStatus("current")
_SrpMACInterfaceSide_Type = InterfaceSide
_SrpMACInterfaceSide_Object = MibTableColumn
srpMACInterfaceSide = _SrpMACInterfaceSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 1),
    _SrpMACInterfaceSide_Type()
)
srpMACInterfaceSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpMACInterfaceSide.setStatus("current")
_SrpMACNeighborAddress_Type = MacAddress
_SrpMACNeighborAddress_Object = MibTableColumn
srpMACNeighborAddress = _SrpMACNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 2),
    _SrpMACNeighborAddress_Type()
)
srpMACNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACNeighborAddress.setStatus("current")
_SrpMACSideWrapped_Type = TruthValue
_SrpMACSideWrapped_Object = MibTableColumn
srpMACSideWrapped = _SrpMACSideWrapped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 3),
    _SrpMACSideWrapped_Type()
)
srpMACSideWrapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACSideWrapped.setStatus("current")
_SrpMACIpsMgmtRequestedMode_Type = IpsMode
_SrpMACIpsMgmtRequestedMode_Object = MibTableColumn
srpMACIpsMgmtRequestedMode = _SrpMACIpsMgmtRequestedMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 4),
    _SrpMACIpsMgmtRequestedMode_Type()
)
srpMACIpsMgmtRequestedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpMACIpsMgmtRequestedMode.setStatus("current")
_SrpMACIpsAutoDetectMode_Type = IpsMode
_SrpMACIpsAutoDetectMode_Object = MibTableColumn
srpMACIpsAutoDetectMode = _SrpMACIpsAutoDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 5),
    _SrpMACIpsAutoDetectMode_Type()
)
srpMACIpsAutoDetectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACIpsAutoDetectMode.setStatus("current")
_SrpMACIpsRemoteMode_Type = IpsMode
_SrpMACIpsRemoteMode_Object = MibTableColumn
srpMACIpsRemoteMode = _SrpMACIpsRemoteMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 6),
    _SrpMACIpsRemoteMode_Type()
)
srpMACIpsRemoteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACIpsRemoteMode.setStatus("current")


class _SrpMACIpsRemoteType_Type(Integer32):
    """Custom type srpMACIpsRemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("longPath", 2),
          ("shortPath", 1))
    )


_SrpMACIpsRemoteType_Type.__name__ = "Integer32"
_SrpMACIpsRemoteType_Object = MibTableColumn
srpMACIpsRemoteType = _SrpMACIpsRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 7),
    _SrpMACIpsRemoteType_Type()
)
srpMACIpsRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACIpsRemoteType.setStatus("current")
_SrpMACIpsActiveMode_Type = IpsMode
_SrpMACIpsActiveMode_Object = MibTableColumn
srpMACIpsActiveMode = _SrpMACIpsActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 8),
    _SrpMACIpsActiveMode_Type()
)
srpMACIpsActiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACIpsActiveMode.setStatus("current")
_SrpMACIpsWrapCounter_Type = Counter32
_SrpMACIpsWrapCounter_Object = MibTableColumn
srpMACIpsWrapCounter = _SrpMACIpsWrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 9),
    _SrpMACIpsWrapCounter_Type()
)
srpMACIpsWrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACIpsWrapCounter.setStatus("current")
_SrpMACIpsLastWrapTimeStamp_Type = TimeStamp
_SrpMACIpsLastWrapTimeStamp_Object = MibTableColumn
srpMACIpsLastWrapTimeStamp = _SrpMACIpsLastWrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 10),
    _SrpMACIpsLastWrapTimeStamp_Type()
)
srpMACIpsLastWrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACIpsLastWrapTimeStamp.setStatus("current")
_SrpMACIpsLastUnWrapTimeStamp_Type = TimeStamp
_SrpMACIpsLastUnWrapTimeStamp_Object = MibTableColumn
srpMACIpsLastUnWrapTimeStamp = _SrpMACIpsLastUnWrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 11),
    _SrpMACIpsLastUnWrapTimeStamp_Type()
)
srpMACIpsLastUnWrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACIpsLastUnWrapTimeStamp.setStatus("current")


class _SrpMACClockSourceMode_Type(Integer32):
    """Custom type srpMACClockSourceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("line", 2))
    )


_SrpMACClockSourceMode_Type.__name__ = "Integer32"
_SrpMACClockSourceMode_Object = MibTableColumn
srpMACClockSourceMode = _SrpMACClockSourceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 12),
    _SrpMACClockSourceMode_Type()
)
srpMACClockSourceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpMACClockSourceMode.setStatus("current")


class _SrpMACTopologyTimer_Type(Integer32):
    """Custom type srpMACTopologyTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SrpMACTopologyTimer_Type.__name__ = "Integer32"
_SrpMACTopologyTimer_Object = MibTableColumn
srpMACTopologyTimer = _SrpMACTopologyTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 2, 1, 13),
    _SrpMACTopologyTimer_Type()
)
srpMACTopologyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpMACTopologyTimer.setStatus("current")
_SrpRingTopologyMapTable_Object = MibTable
srpRingTopologyMapTable = _SrpRingTopologyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 3)
)
if mibBuilder.loadTexts:
    srpRingTopologyMapTable.setStatus("current")
_SrpRingTopologyMapEntry_Object = MibTableRow
srpRingTopologyMapEntry = _SrpRingTopologyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 3, 1)
)
srpRingTopologyMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SRP-MIB", "srpNodeHopsNumber"),
)
if mibBuilder.loadTexts:
    srpRingTopologyMapEntry.setStatus("current")


class _SrpNodeHopsNumber_Type(Unsigned32):
    """Custom type srpNodeHopsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SrpNodeHopsNumber_Type.__name__ = "Unsigned32"
_SrpNodeHopsNumber_Object = MibTableColumn
srpNodeHopsNumber = _SrpNodeHopsNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 3, 1, 1),
    _SrpNodeHopsNumber_Type()
)
srpNodeHopsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpNodeHopsNumber.setStatus("current")
_SrpNodeMACAddress_Type = MacAddress
_SrpNodeMACAddress_Object = MibTableColumn
srpNodeMACAddress = _SrpNodeMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 3, 1, 2),
    _SrpNodeMACAddress_Type()
)
srpNodeMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpNodeMACAddress.setStatus("current")
_SrpNodeWrapped_Type = TruthValue
_SrpNodeWrapped_Object = MibTableColumn
srpNodeWrapped = _SrpNodeWrapped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 3, 1, 3),
    _SrpNodeWrapped_Type()
)
srpNodeWrapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpNodeWrapped.setStatus("current")


class _SrpNodeName_Type(DisplayString):
    """Custom type srpNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SrpNodeName_Type.__name__ = "DisplayString"
_SrpNodeName_Object = MibTableColumn
srpNodeName = _SrpNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 3, 1, 4),
    _SrpNodeName_Type()
)
srpNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpNodeName.setStatus("current")
_SrpMACCountersTable_Object = MibTable
srpMACCountersTable = _SrpMACCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6)
)
if mibBuilder.loadTexts:
    srpMACCountersTable.setStatus("deprecated")
_SrpMACCountersEntry_Object = MibTableRow
srpMACCountersEntry = _SrpMACCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1)
)
srpMACCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    srpMACCountersEntry.setStatus("deprecated")
_SrpMACCountPktsBySourceFlag_Type = TruthValue
_SrpMACCountPktsBySourceFlag_Object = MibTableColumn
srpMACCountPktsBySourceFlag = _SrpMACCountPktsBySourceFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 1),
    _SrpMACCountPktsBySourceFlag_Type()
)
srpMACCountPktsBySourceFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpMACCountPktsBySourceFlag.setStatus("deprecated")
_SrpMACCountPktsBySourceAddress_Type = MacAddress
_SrpMACCountPktsBySourceAddress_Object = MibTableColumn
srpMACCountPktsBySourceAddress = _SrpMACCountPktsBySourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 2),
    _SrpMACCountPktsBySourceAddress_Type()
)
srpMACCountPktsBySourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpMACCountPktsBySourceAddress.setStatus("deprecated")
_SrpMACSourceDiscontTimeStamp_Type = TimeStamp
_SrpMACSourceDiscontTimeStamp_Object = MibTableColumn
srpMACSourceDiscontTimeStamp = _SrpMACSourceDiscontTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 3),
    _SrpMACSourceDiscontTimeStamp_Type()
)
srpMACSourceDiscontTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACSourceDiscontTimeStamp.setStatus("deprecated")
_SrpMACCountPktsBySource_Type = Counter64
_SrpMACCountPktsBySource_Object = MibTableColumn
srpMACCountPktsBySource = _SrpMACCountPktsBySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 4),
    _SrpMACCountPktsBySource_Type()
)
srpMACCountPktsBySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACCountPktsBySource.setStatus("deprecated")
_SrpMACCountPktsByDestinationFlag_Type = TruthValue
_SrpMACCountPktsByDestinationFlag_Object = MibTableColumn
srpMACCountPktsByDestinationFlag = _SrpMACCountPktsByDestinationFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 5),
    _SrpMACCountPktsByDestinationFlag_Type()
)
srpMACCountPktsByDestinationFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpMACCountPktsByDestinationFlag.setStatus("deprecated")
_SrpMACCountPktsByDestAddress_Type = MacAddress
_SrpMACCountPktsByDestAddress_Object = MibTableColumn
srpMACCountPktsByDestAddress = _SrpMACCountPktsByDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 6),
    _SrpMACCountPktsByDestAddress_Type()
)
srpMACCountPktsByDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpMACCountPktsByDestAddress.setStatus("deprecated")
_SrpMACDestDiscontTimeStamp_Type = TimeStamp
_SrpMACDestDiscontTimeStamp_Object = MibTableColumn
srpMACDestDiscontTimeStamp = _SrpMACDestDiscontTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 7),
    _SrpMACDestDiscontTimeStamp_Type()
)
srpMACDestDiscontTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACDestDiscontTimeStamp.setStatus("deprecated")
_SrpMACCountPktsByDest_Type = Counter64
_SrpMACCountPktsByDest_Object = MibTableColumn
srpMACCountPktsByDest = _SrpMACCountPktsByDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 8),
    _SrpMACCountPktsByDest_Type()
)
srpMACCountPktsByDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpMACCountPktsByDest.setStatus("deprecated")
_SrpMACRejectPktsBySourceFlag_Type = TruthValue
_SrpMACRejectPktsBySourceFlag_Object = MibTableColumn
srpMACRejectPktsBySourceFlag = _SrpMACRejectPktsBySourceFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 9),
    _SrpMACRejectPktsBySourceFlag_Type()
)
srpMACRejectPktsBySourceFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpMACRejectPktsBySourceFlag.setStatus("deprecated")
_SrpMACRejectPktsBySourceAddress_Type = MacAddress
_SrpMACRejectPktsBySourceAddress_Object = MibTableColumn
srpMACRejectPktsBySourceAddress = _SrpMACRejectPktsBySourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 10),
    _SrpMACRejectPktsBySourceAddress_Type()
)
srpMACRejectPktsBySourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpMACRejectPktsBySourceAddress.setStatus("deprecated")
_SrpMACRejectPktsByDestFlag_Type = TruthValue
_SrpMACRejectPktsByDestFlag_Object = MibTableColumn
srpMACRejectPktsByDestFlag = _SrpMACRejectPktsByDestFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 11),
    _SrpMACRejectPktsByDestFlag_Type()
)
srpMACRejectPktsByDestFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpMACRejectPktsByDestFlag.setStatus("deprecated")
_SrpMACRejectPktsByDestAddress_Type = MacAddress
_SrpMACRejectPktsByDestAddress_Object = MibTableColumn
srpMACRejectPktsByDestAddress = _SrpMACRejectPktsByDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 1, 6, 1, 12),
    _SrpMACRejectPktsByDestAddress_Type()
)
srpMACRejectPktsByDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srpMACRejectPktsByDestAddress.setStatus("deprecated")
_SrpRingCounters_ObjectIdentity = ObjectIdentity
srpRingCounters = _SrpRingCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2)
)
_SrpRingCountersCurrentTable_Object = MibTable
srpRingCountersCurrentTable = _SrpRingCountersCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1)
)
if mibBuilder.loadTexts:
    srpRingCountersCurrentTable.setStatus("current")
_SrpRingCountersCurrentEntry_Object = MibTableRow
srpRingCountersCurrentEntry = _SrpRingCountersCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1)
)
srpRingCountersCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SRP-MIB", "srpRingInterfaceSide"),
)
if mibBuilder.loadTexts:
    srpRingCountersCurrentEntry.setStatus("current")
_SrpRingInterfaceSide_Type = InterfaceSide
_SrpRingInterfaceSide_Object = MibTableColumn
srpRingInterfaceSide = _SrpRingInterfaceSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 1),
    _SrpRingInterfaceSide_Type()
)
srpRingInterfaceSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpRingInterfaceSide.setStatus("current")
_SrpRingCurUcastLowPriPktsIn_Type = PerfCurrentCount64
_SrpRingCurUcastLowPriPktsIn_Object = MibTableColumn
srpRingCurUcastLowPriPktsIn = _SrpRingCurUcastLowPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 2),
    _SrpRingCurUcastLowPriPktsIn_Type()
)
srpRingCurUcastLowPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurUcastLowPriPktsIn.setStatus("current")
_SrpRingCurUcastLowPriOctetsIn_Type = PerfCurrentCount64
_SrpRingCurUcastLowPriOctetsIn_Object = MibTableColumn
srpRingCurUcastLowPriOctetsIn = _SrpRingCurUcastLowPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 3),
    _SrpRingCurUcastLowPriOctetsIn_Type()
)
srpRingCurUcastLowPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurUcastLowPriOctetsIn.setStatus("current")
_SrpRingCurMcastLowPriPktsIn_Type = PerfCurrentCount64
_SrpRingCurMcastLowPriPktsIn_Object = MibTableColumn
srpRingCurMcastLowPriPktsIn = _SrpRingCurMcastLowPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 4),
    _SrpRingCurMcastLowPriPktsIn_Type()
)
srpRingCurMcastLowPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurMcastLowPriPktsIn.setStatus("current")
_SrpRingCurMcastLowPriOctetsIn_Type = PerfCurrentCount64
_SrpRingCurMcastLowPriOctetsIn_Object = MibTableColumn
srpRingCurMcastLowPriOctetsIn = _SrpRingCurMcastLowPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 5),
    _SrpRingCurMcastLowPriOctetsIn_Type()
)
srpRingCurMcastLowPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurMcastLowPriOctetsIn.setStatus("current")
_SrpRingCurUcastHighPriPktsIn_Type = PerfCurrentCount64
_SrpRingCurUcastHighPriPktsIn_Object = MibTableColumn
srpRingCurUcastHighPriPktsIn = _SrpRingCurUcastHighPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 6),
    _SrpRingCurUcastHighPriPktsIn_Type()
)
srpRingCurUcastHighPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurUcastHighPriPktsIn.setStatus("current")
_SrpRingCurUcastHighPriOctetsIn_Type = PerfCurrentCount64
_SrpRingCurUcastHighPriOctetsIn_Object = MibTableColumn
srpRingCurUcastHighPriOctetsIn = _SrpRingCurUcastHighPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 7),
    _SrpRingCurUcastHighPriOctetsIn_Type()
)
srpRingCurUcastHighPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurUcastHighPriOctetsIn.setStatus("current")
_SrpRingCurMcastHighPriPktsIn_Type = PerfCurrentCount64
_SrpRingCurMcastHighPriPktsIn_Object = MibTableColumn
srpRingCurMcastHighPriPktsIn = _SrpRingCurMcastHighPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 8),
    _SrpRingCurMcastHighPriPktsIn_Type()
)
srpRingCurMcastHighPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurMcastHighPriPktsIn.setStatus("current")
_SrpRingCurMcastHighPriOctetsIn_Type = PerfCurrentCount64
_SrpRingCurMcastHighPriOctetsIn_Object = MibTableColumn
srpRingCurMcastHighPriOctetsIn = _SrpRingCurMcastHighPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 9),
    _SrpRingCurMcastHighPriOctetsIn_Type()
)
srpRingCurMcastHighPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurMcastHighPriOctetsIn.setStatus("current")
_SrpRingCurUcastLowPriPktsOut_Type = PerfCurrentCount64
_SrpRingCurUcastLowPriPktsOut_Object = MibTableColumn
srpRingCurUcastLowPriPktsOut = _SrpRingCurUcastLowPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 10),
    _SrpRingCurUcastLowPriPktsOut_Type()
)
srpRingCurUcastLowPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurUcastLowPriPktsOut.setStatus("current")
_SrpRingCurUcastLowPriOctetsOut_Type = PerfCurrentCount64
_SrpRingCurUcastLowPriOctetsOut_Object = MibTableColumn
srpRingCurUcastLowPriOctetsOut = _SrpRingCurUcastLowPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 11),
    _SrpRingCurUcastLowPriOctetsOut_Type()
)
srpRingCurUcastLowPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurUcastLowPriOctetsOut.setStatus("current")
_SrpRingCurMcastLowPriPktsOut_Type = PerfCurrentCount64
_SrpRingCurMcastLowPriPktsOut_Object = MibTableColumn
srpRingCurMcastLowPriPktsOut = _SrpRingCurMcastLowPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 12),
    _SrpRingCurMcastLowPriPktsOut_Type()
)
srpRingCurMcastLowPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurMcastLowPriPktsOut.setStatus("current")
_SrpRingCurMcastLowPriOctetsOut_Type = PerfCurrentCount64
_SrpRingCurMcastLowPriOctetsOut_Object = MibTableColumn
srpRingCurMcastLowPriOctetsOut = _SrpRingCurMcastLowPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 13),
    _SrpRingCurMcastLowPriOctetsOut_Type()
)
srpRingCurMcastLowPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurMcastLowPriOctetsOut.setStatus("current")
_SrpRingCurUcastHighPriPktsOut_Type = PerfCurrentCount64
_SrpRingCurUcastHighPriPktsOut_Object = MibTableColumn
srpRingCurUcastHighPriPktsOut = _SrpRingCurUcastHighPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 14),
    _SrpRingCurUcastHighPriPktsOut_Type()
)
srpRingCurUcastHighPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurUcastHighPriPktsOut.setStatus("current")
_SrpRingCurUcastHighPriOctetsOut_Type = PerfCurrentCount64
_SrpRingCurUcastHighPriOctetsOut_Object = MibTableColumn
srpRingCurUcastHighPriOctetsOut = _SrpRingCurUcastHighPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 15),
    _SrpRingCurUcastHighPriOctetsOut_Type()
)
srpRingCurUcastHighPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurUcastHighPriOctetsOut.setStatus("current")
_SrpRingCurMcastHighPriPktsOut_Type = PerfCurrentCount64
_SrpRingCurMcastHighPriPktsOut_Object = MibTableColumn
srpRingCurMcastHighPriPktsOut = _SrpRingCurMcastHighPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 16),
    _SrpRingCurMcastHighPriPktsOut_Type()
)
srpRingCurMcastHighPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurMcastHighPriPktsOut.setStatus("current")
_SrpRingCurMcastHighPriOctetsOut_Type = PerfCurrentCount64
_SrpRingCurMcastHighPriOctetsOut_Object = MibTableColumn
srpRingCurMcastHighPriOctetsOut = _SrpRingCurMcastHighPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 1, 1, 17),
    _SrpRingCurMcastHighPriOctetsOut_Type()
)
srpRingCurMcastHighPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurMcastHighPriOctetsOut.setStatus("current")
_SrpRingCountersIntervalTable_Object = MibTable
srpRingCountersIntervalTable = _SrpRingCountersIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2)
)
if mibBuilder.loadTexts:
    srpRingCountersIntervalTable.setStatus("current")
_SrpRingCountersIntervalEntry_Object = MibTableRow
srpRingCountersIntervalEntry = _SrpRingCountersIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1)
)
srpRingCountersIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SRP-MIB", "srpRingIntInterfaceSide"),
    (0, "CISCO-SRP-MIB", "srpRingIntNumber"),
)
if mibBuilder.loadTexts:
    srpRingCountersIntervalEntry.setStatus("current")
_SrpRingIntInterfaceSide_Type = InterfaceSide
_SrpRingIntInterfaceSide_Object = MibTableColumn
srpRingIntInterfaceSide = _SrpRingIntInterfaceSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 1),
    _SrpRingIntInterfaceSide_Type()
)
srpRingIntInterfaceSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpRingIntInterfaceSide.setStatus("current")


class _SrpRingIntNumber_Type(Integer32):
    """Custom type srpRingIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SrpRingIntNumber_Type.__name__ = "Integer32"
_SrpRingIntNumber_Object = MibTableColumn
srpRingIntNumber = _SrpRingIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 2),
    _SrpRingIntNumber_Type()
)
srpRingIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpRingIntNumber.setStatus("current")
_SrpRingIntWrapCounter_Type = Counter32
_SrpRingIntWrapCounter_Object = MibTableColumn
srpRingIntWrapCounter = _SrpRingIntWrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 3),
    _SrpRingIntWrapCounter_Type()
)
srpRingIntWrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntWrapCounter.setStatus("current")
_SrpRingIntUcastLowPriPktsIn_Type = PerfIntervalCount64
_SrpRingIntUcastLowPriPktsIn_Object = MibTableColumn
srpRingIntUcastLowPriPktsIn = _SrpRingIntUcastLowPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 4),
    _SrpRingIntUcastLowPriPktsIn_Type()
)
srpRingIntUcastLowPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntUcastLowPriPktsIn.setStatus("current")
_SrpRingIntUcastLowPriOctetsIn_Type = PerfIntervalCount64
_SrpRingIntUcastLowPriOctetsIn_Object = MibTableColumn
srpRingIntUcastLowPriOctetsIn = _SrpRingIntUcastLowPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 5),
    _SrpRingIntUcastLowPriOctetsIn_Type()
)
srpRingIntUcastLowPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntUcastLowPriOctetsIn.setStatus("current")
_SrpRingIntMcastLowPriPktsIn_Type = PerfIntervalCount64
_SrpRingIntMcastLowPriPktsIn_Object = MibTableColumn
srpRingIntMcastLowPriPktsIn = _SrpRingIntMcastLowPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 6),
    _SrpRingIntMcastLowPriPktsIn_Type()
)
srpRingIntMcastLowPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntMcastLowPriPktsIn.setStatus("current")
_SrpRingIntMcastLowPriOctetsIn_Type = PerfIntervalCount64
_SrpRingIntMcastLowPriOctetsIn_Object = MibTableColumn
srpRingIntMcastLowPriOctetsIn = _SrpRingIntMcastLowPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 7),
    _SrpRingIntMcastLowPriOctetsIn_Type()
)
srpRingIntMcastLowPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntMcastLowPriOctetsIn.setStatus("current")
_SrpRingIntUcastHighPriPktsIn_Type = PerfIntervalCount64
_SrpRingIntUcastHighPriPktsIn_Object = MibTableColumn
srpRingIntUcastHighPriPktsIn = _SrpRingIntUcastHighPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 8),
    _SrpRingIntUcastHighPriPktsIn_Type()
)
srpRingIntUcastHighPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntUcastHighPriPktsIn.setStatus("current")
_SrpRingIntUcastHighPriOctetsIn_Type = PerfIntervalCount64
_SrpRingIntUcastHighPriOctetsIn_Object = MibTableColumn
srpRingIntUcastHighPriOctetsIn = _SrpRingIntUcastHighPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 9),
    _SrpRingIntUcastHighPriOctetsIn_Type()
)
srpRingIntUcastHighPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntUcastHighPriOctetsIn.setStatus("current")
_SrpRingIntMcastHighPriPktsIn_Type = PerfIntervalCount64
_SrpRingIntMcastHighPriPktsIn_Object = MibTableColumn
srpRingIntMcastHighPriPktsIn = _SrpRingIntMcastHighPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 10),
    _SrpRingIntMcastHighPriPktsIn_Type()
)
srpRingIntMcastHighPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntMcastHighPriPktsIn.setStatus("current")
_SrpRingIntMcastHighPriOctetsIn_Type = PerfIntervalCount64
_SrpRingIntMcastHighPriOctetsIn_Object = MibTableColumn
srpRingIntMcastHighPriOctetsIn = _SrpRingIntMcastHighPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 11),
    _SrpRingIntMcastHighPriOctetsIn_Type()
)
srpRingIntMcastHighPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntMcastHighPriOctetsIn.setStatus("current")
_SrpRingIntUcastLowPriPktsOut_Type = PerfIntervalCount64
_SrpRingIntUcastLowPriPktsOut_Object = MibTableColumn
srpRingIntUcastLowPriPktsOut = _SrpRingIntUcastLowPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 12),
    _SrpRingIntUcastLowPriPktsOut_Type()
)
srpRingIntUcastLowPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntUcastLowPriPktsOut.setStatus("current")
_SrpRingIntUcastLowPriOctetsOut_Type = PerfIntervalCount64
_SrpRingIntUcastLowPriOctetsOut_Object = MibTableColumn
srpRingIntUcastLowPriOctetsOut = _SrpRingIntUcastLowPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 13),
    _SrpRingIntUcastLowPriOctetsOut_Type()
)
srpRingIntUcastLowPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntUcastLowPriOctetsOut.setStatus("current")
_SrpRingIntMcastLowPriPktsOut_Type = PerfIntervalCount64
_SrpRingIntMcastLowPriPktsOut_Object = MibTableColumn
srpRingIntMcastLowPriPktsOut = _SrpRingIntMcastLowPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 14),
    _SrpRingIntMcastLowPriPktsOut_Type()
)
srpRingIntMcastLowPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntMcastLowPriPktsOut.setStatus("current")
_SrpRingIntMcastLowPriOctetsOut_Type = PerfIntervalCount64
_SrpRingIntMcastLowPriOctetsOut_Object = MibTableColumn
srpRingIntMcastLowPriOctetsOut = _SrpRingIntMcastLowPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 15),
    _SrpRingIntMcastLowPriOctetsOut_Type()
)
srpRingIntMcastLowPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntMcastLowPriOctetsOut.setStatus("current")
_SrpRingIntUcastHighPriPktsOut_Type = PerfIntervalCount64
_SrpRingIntUcastHighPriPktsOut_Object = MibTableColumn
srpRingIntUcastHighPriPktsOut = _SrpRingIntUcastHighPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 16),
    _SrpRingIntUcastHighPriPktsOut_Type()
)
srpRingIntUcastHighPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntUcastHighPriPktsOut.setStatus("current")
_SrpRingIntUcastHighPriOctetsOut_Type = PerfIntervalCount64
_SrpRingIntUcastHighPriOctetsOut_Object = MibTableColumn
srpRingIntUcastHighPriOctetsOut = _SrpRingIntUcastHighPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 17),
    _SrpRingIntUcastHighPriOctetsOut_Type()
)
srpRingIntUcastHighPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntUcastHighPriOctetsOut.setStatus("current")
_SrpRingIntMcastHighPriPktsOut_Type = PerfIntervalCount64
_SrpRingIntMcastHighPriPktsOut_Object = MibTableColumn
srpRingIntMcastHighPriPktsOut = _SrpRingIntMcastHighPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 18),
    _SrpRingIntMcastHighPriPktsOut_Type()
)
srpRingIntMcastHighPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntMcastHighPriPktsOut.setStatus("current")
_SrpRingIntMcastHighPriOctetsOut_Type = PerfIntervalCount64
_SrpRingIntMcastHighPriOctetsOut_Object = MibTableColumn
srpRingIntMcastHighPriOctetsOut = _SrpRingIntMcastHighPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 2, 2, 1, 19),
    _SrpRingIntMcastHighPriOctetsOut_Type()
)
srpRingIntMcastHighPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntMcastHighPriOctetsOut.setStatus("current")
_SrpHostCounters_ObjectIdentity = ObjectIdentity
srpHostCounters = _SrpHostCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3)
)
_SrpHostCountersCurrentTable_Object = MibTable
srpHostCountersCurrentTable = _SrpHostCountersCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1)
)
if mibBuilder.loadTexts:
    srpHostCountersCurrentTable.setStatus("current")
_SrpHostCountersCurrentEntry_Object = MibTableRow
srpHostCountersCurrentEntry = _SrpHostCountersCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1)
)
srpHostCountersCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SRP-MIB", "srpHostInterfaceSide"),
)
if mibBuilder.loadTexts:
    srpHostCountersCurrentEntry.setStatus("current")
_SrpHostInterfaceSide_Type = InterfaceSide
_SrpHostInterfaceSide_Object = MibTableColumn
srpHostInterfaceSide = _SrpHostInterfaceSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 1),
    _SrpHostInterfaceSide_Type()
)
srpHostInterfaceSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpHostInterfaceSide.setStatus("current")
_SrpHostCurUcastLowPriPktsIn_Type = PerfCurrentCount64
_SrpHostCurUcastLowPriPktsIn_Object = MibTableColumn
srpHostCurUcastLowPriPktsIn = _SrpHostCurUcastLowPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 2),
    _SrpHostCurUcastLowPriPktsIn_Type()
)
srpHostCurUcastLowPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurUcastLowPriPktsIn.setStatus("current")
_SrpHostCurUcastLowPriOctetsIn_Type = PerfCurrentCount64
_SrpHostCurUcastLowPriOctetsIn_Object = MibTableColumn
srpHostCurUcastLowPriOctetsIn = _SrpHostCurUcastLowPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 3),
    _SrpHostCurUcastLowPriOctetsIn_Type()
)
srpHostCurUcastLowPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurUcastLowPriOctetsIn.setStatus("current")
_SrpHostCurMcastLowPriPktsIn_Type = PerfCurrentCount64
_SrpHostCurMcastLowPriPktsIn_Object = MibTableColumn
srpHostCurMcastLowPriPktsIn = _SrpHostCurMcastLowPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 4),
    _SrpHostCurMcastLowPriPktsIn_Type()
)
srpHostCurMcastLowPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurMcastLowPriPktsIn.setStatus("current")
_SrpHostCurMcastLowPriOctetsIn_Type = PerfCurrentCount64
_SrpHostCurMcastLowPriOctetsIn_Object = MibTableColumn
srpHostCurMcastLowPriOctetsIn = _SrpHostCurMcastLowPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 5),
    _SrpHostCurMcastLowPriOctetsIn_Type()
)
srpHostCurMcastLowPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurMcastLowPriOctetsIn.setStatus("current")
_SrpHostCurUcastHighPriPktsIn_Type = PerfCurrentCount64
_SrpHostCurUcastHighPriPktsIn_Object = MibTableColumn
srpHostCurUcastHighPriPktsIn = _SrpHostCurUcastHighPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 6),
    _SrpHostCurUcastHighPriPktsIn_Type()
)
srpHostCurUcastHighPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurUcastHighPriPktsIn.setStatus("current")
_SrpHostCurUcastHighPriOctetsIn_Type = PerfCurrentCount64
_SrpHostCurUcastHighPriOctetsIn_Object = MibTableColumn
srpHostCurUcastHighPriOctetsIn = _SrpHostCurUcastHighPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 7),
    _SrpHostCurUcastHighPriOctetsIn_Type()
)
srpHostCurUcastHighPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurUcastHighPriOctetsIn.setStatus("current")
_SrpHostCurMcastHighPriPktsIn_Type = PerfCurrentCount64
_SrpHostCurMcastHighPriPktsIn_Object = MibTableColumn
srpHostCurMcastHighPriPktsIn = _SrpHostCurMcastHighPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 8),
    _SrpHostCurMcastHighPriPktsIn_Type()
)
srpHostCurMcastHighPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurMcastHighPriPktsIn.setStatus("current")
_SrpHostCurMcastHighPriOctetsIn_Type = PerfCurrentCount64
_SrpHostCurMcastHighPriOctetsIn_Object = MibTableColumn
srpHostCurMcastHighPriOctetsIn = _SrpHostCurMcastHighPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 9),
    _SrpHostCurMcastHighPriOctetsIn_Type()
)
srpHostCurMcastHighPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurMcastHighPriOctetsIn.setStatus("current")
_SrpHostCurUcastLowPriPktsOut_Type = PerfCurrentCount64
_SrpHostCurUcastLowPriPktsOut_Object = MibTableColumn
srpHostCurUcastLowPriPktsOut = _SrpHostCurUcastLowPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 10),
    _SrpHostCurUcastLowPriPktsOut_Type()
)
srpHostCurUcastLowPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurUcastLowPriPktsOut.setStatus("current")
_SrpHostCurUcastLowPriOctetsOut_Type = PerfCurrentCount64
_SrpHostCurUcastLowPriOctetsOut_Object = MibTableColumn
srpHostCurUcastLowPriOctetsOut = _SrpHostCurUcastLowPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 11),
    _SrpHostCurUcastLowPriOctetsOut_Type()
)
srpHostCurUcastLowPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurUcastLowPriOctetsOut.setStatus("current")
_SrpHostCurMcastLowPriPktsOut_Type = PerfCurrentCount64
_SrpHostCurMcastLowPriPktsOut_Object = MibTableColumn
srpHostCurMcastLowPriPktsOut = _SrpHostCurMcastLowPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 12),
    _SrpHostCurMcastLowPriPktsOut_Type()
)
srpHostCurMcastLowPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurMcastLowPriPktsOut.setStatus("current")
_SrpHostCurMcastLowPriOctetsOut_Type = PerfCurrentCount64
_SrpHostCurMcastLowPriOctetsOut_Object = MibTableColumn
srpHostCurMcastLowPriOctetsOut = _SrpHostCurMcastLowPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 13),
    _SrpHostCurMcastLowPriOctetsOut_Type()
)
srpHostCurMcastLowPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurMcastLowPriOctetsOut.setStatus("current")
_SrpHostCurUcastHighPriPktsOut_Type = PerfCurrentCount64
_SrpHostCurUcastHighPriPktsOut_Object = MibTableColumn
srpHostCurUcastHighPriPktsOut = _SrpHostCurUcastHighPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 14),
    _SrpHostCurUcastHighPriPktsOut_Type()
)
srpHostCurUcastHighPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurUcastHighPriPktsOut.setStatus("current")
_SrpHostCurUcastHighPriOctetsOut_Type = PerfCurrentCount64
_SrpHostCurUcastHighPriOctetsOut_Object = MibTableColumn
srpHostCurUcastHighPriOctetsOut = _SrpHostCurUcastHighPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 15),
    _SrpHostCurUcastHighPriOctetsOut_Type()
)
srpHostCurUcastHighPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurUcastHighPriOctetsOut.setStatus("current")
_SrpHostCurMcastHighPriPktsOut_Type = PerfCurrentCount64
_SrpHostCurMcastHighPriPktsOut_Object = MibTableColumn
srpHostCurMcastHighPriPktsOut = _SrpHostCurMcastHighPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 16),
    _SrpHostCurMcastHighPriPktsOut_Type()
)
srpHostCurMcastHighPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurMcastHighPriPktsOut.setStatus("current")
_SrpHostCurMcastHighPriOctetsOut_Type = PerfCurrentCount64
_SrpHostCurMcastHighPriOctetsOut_Object = MibTableColumn
srpHostCurMcastHighPriOctetsOut = _SrpHostCurMcastHighPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 1, 1, 17),
    _SrpHostCurMcastHighPriOctetsOut_Type()
)
srpHostCurMcastHighPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurMcastHighPriOctetsOut.setStatus("current")
_SrpHostCountersIntervalTable_Object = MibTable
srpHostCountersIntervalTable = _SrpHostCountersIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2)
)
if mibBuilder.loadTexts:
    srpHostCountersIntervalTable.setStatus("current")
_SrpHostCountersIntervalEntry_Object = MibTableRow
srpHostCountersIntervalEntry = _SrpHostCountersIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1)
)
srpHostCountersIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SRP-MIB", "srpHostIntInterfaceSide"),
    (0, "CISCO-SRP-MIB", "srpHostIntNumber"),
)
if mibBuilder.loadTexts:
    srpHostCountersIntervalEntry.setStatus("current")
_SrpHostIntInterfaceSide_Type = InterfaceSide
_SrpHostIntInterfaceSide_Object = MibTableColumn
srpHostIntInterfaceSide = _SrpHostIntInterfaceSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 1),
    _SrpHostIntInterfaceSide_Type()
)
srpHostIntInterfaceSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpHostIntInterfaceSide.setStatus("current")


class _SrpHostIntNumber_Type(Integer32):
    """Custom type srpHostIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SrpHostIntNumber_Type.__name__ = "Integer32"
_SrpHostIntNumber_Object = MibTableColumn
srpHostIntNumber = _SrpHostIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 2),
    _SrpHostIntNumber_Type()
)
srpHostIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpHostIntNumber.setStatus("current")
_SrpHostIntUcastLowPriPktsIn_Type = PerfIntervalCount64
_SrpHostIntUcastLowPriPktsIn_Object = MibTableColumn
srpHostIntUcastLowPriPktsIn = _SrpHostIntUcastLowPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 3),
    _SrpHostIntUcastLowPriPktsIn_Type()
)
srpHostIntUcastLowPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntUcastLowPriPktsIn.setStatus("current")
_SrpHostIntUcastLowPriOctetsIn_Type = PerfIntervalCount64
_SrpHostIntUcastLowPriOctetsIn_Object = MibTableColumn
srpHostIntUcastLowPriOctetsIn = _SrpHostIntUcastLowPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 4),
    _SrpHostIntUcastLowPriOctetsIn_Type()
)
srpHostIntUcastLowPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntUcastLowPriOctetsIn.setStatus("current")
_SrpHostIntMcastLowPriPktsIn_Type = PerfIntervalCount64
_SrpHostIntMcastLowPriPktsIn_Object = MibTableColumn
srpHostIntMcastLowPriPktsIn = _SrpHostIntMcastLowPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 5),
    _SrpHostIntMcastLowPriPktsIn_Type()
)
srpHostIntMcastLowPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntMcastLowPriPktsIn.setStatus("current")
_SrpHostIntMcastLowPriOctetsIn_Type = PerfIntervalCount64
_SrpHostIntMcastLowPriOctetsIn_Object = MibTableColumn
srpHostIntMcastLowPriOctetsIn = _SrpHostIntMcastLowPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 6),
    _SrpHostIntMcastLowPriOctetsIn_Type()
)
srpHostIntMcastLowPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntMcastLowPriOctetsIn.setStatus("current")
_SrpHostIntUcastHighPriPktsIn_Type = PerfIntervalCount64
_SrpHostIntUcastHighPriPktsIn_Object = MibTableColumn
srpHostIntUcastHighPriPktsIn = _SrpHostIntUcastHighPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 7),
    _SrpHostIntUcastHighPriPktsIn_Type()
)
srpHostIntUcastHighPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntUcastHighPriPktsIn.setStatus("current")
_SrpHostIntUcastHighPriOctetsIn_Type = PerfIntervalCount64
_SrpHostIntUcastHighPriOctetsIn_Object = MibTableColumn
srpHostIntUcastHighPriOctetsIn = _SrpHostIntUcastHighPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 8),
    _SrpHostIntUcastHighPriOctetsIn_Type()
)
srpHostIntUcastHighPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntUcastHighPriOctetsIn.setStatus("current")
_SrpHostIntMcastHighPriPktsIn_Type = PerfIntervalCount64
_SrpHostIntMcastHighPriPktsIn_Object = MibTableColumn
srpHostIntMcastHighPriPktsIn = _SrpHostIntMcastHighPriPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 9),
    _SrpHostIntMcastHighPriPktsIn_Type()
)
srpHostIntMcastHighPriPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntMcastHighPriPktsIn.setStatus("current")
_SrpHostIntMcastHighPriOctetsIn_Type = PerfIntervalCount64
_SrpHostIntMcastHighPriOctetsIn_Object = MibTableColumn
srpHostIntMcastHighPriOctetsIn = _SrpHostIntMcastHighPriOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 10),
    _SrpHostIntMcastHighPriOctetsIn_Type()
)
srpHostIntMcastHighPriOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntMcastHighPriOctetsIn.setStatus("current")
_SrpHostIntUcastLowPriPktsOut_Type = PerfIntervalCount64
_SrpHostIntUcastLowPriPktsOut_Object = MibTableColumn
srpHostIntUcastLowPriPktsOut = _SrpHostIntUcastLowPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 11),
    _SrpHostIntUcastLowPriPktsOut_Type()
)
srpHostIntUcastLowPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntUcastLowPriPktsOut.setStatus("current")
_SrpHostIntUcastLowPriOctetsOut_Type = PerfIntervalCount64
_SrpHostIntUcastLowPriOctetsOut_Object = MibTableColumn
srpHostIntUcastLowPriOctetsOut = _SrpHostIntUcastLowPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 12),
    _SrpHostIntUcastLowPriOctetsOut_Type()
)
srpHostIntUcastLowPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntUcastLowPriOctetsOut.setStatus("current")
_SrpHostIntMcastLowPriPktsOut_Type = PerfIntervalCount64
_SrpHostIntMcastLowPriPktsOut_Object = MibTableColumn
srpHostIntMcastLowPriPktsOut = _SrpHostIntMcastLowPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 13),
    _SrpHostIntMcastLowPriPktsOut_Type()
)
srpHostIntMcastLowPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntMcastLowPriPktsOut.setStatus("current")
_SrpHostIntMcastLowPriOctetsOut_Type = PerfIntervalCount64
_SrpHostIntMcastLowPriOctetsOut_Object = MibTableColumn
srpHostIntMcastLowPriOctetsOut = _SrpHostIntMcastLowPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 14),
    _SrpHostIntMcastLowPriOctetsOut_Type()
)
srpHostIntMcastLowPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntMcastLowPriOctetsOut.setStatus("current")
_SrpHostIntUcastHighPriPktsOut_Type = PerfIntervalCount64
_SrpHostIntUcastHighPriPktsOut_Object = MibTableColumn
srpHostIntUcastHighPriPktsOut = _SrpHostIntUcastHighPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 15),
    _SrpHostIntUcastHighPriPktsOut_Type()
)
srpHostIntUcastHighPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntUcastHighPriPktsOut.setStatus("current")
_SrpHostIntUcastHighPriOctetsOut_Type = PerfIntervalCount64
_SrpHostIntUcastHighPriOctetsOut_Object = MibTableColumn
srpHostIntUcastHighPriOctetsOut = _SrpHostIntUcastHighPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 16),
    _SrpHostIntUcastHighPriOctetsOut_Type()
)
srpHostIntUcastHighPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntUcastHighPriOctetsOut.setStatus("current")
_SrpHostIntMcastHighPriPktsOut_Type = PerfIntervalCount64
_SrpHostIntMcastHighPriPktsOut_Object = MibTableColumn
srpHostIntMcastHighPriPktsOut = _SrpHostIntMcastHighPriPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 17),
    _SrpHostIntMcastHighPriPktsOut_Type()
)
srpHostIntMcastHighPriPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntMcastHighPriPktsOut.setStatus("current")
_SrpHostIntMcastHighPriOctetsOut_Type = PerfIntervalCount64
_SrpHostIntMcastHighPriOctetsOut_Object = MibTableColumn
srpHostIntMcastHighPriOctetsOut = _SrpHostIntMcastHighPriOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 3, 2, 1, 18),
    _SrpHostIntMcastHighPriOctetsOut_Type()
)
srpHostIntMcastHighPriOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntMcastHighPriOctetsOut.setStatus("current")
_SrpErrorsCounters_ObjectIdentity = ObjectIdentity
srpErrorsCounters = _SrpErrorsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4)
)
_SrpErrorsCountersCurrentTable_Object = MibTable
srpErrorsCountersCurrentTable = _SrpErrorsCountersCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1)
)
if mibBuilder.loadTexts:
    srpErrorsCountersCurrentTable.setStatus("deprecated")
_SrpErrorsCountersCurrentEntry_Object = MibTableRow
srpErrorsCountersCurrentEntry = _SrpErrorsCountersCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1, 1)
)
srpErrorsCountersCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SRP-MIB", "srpErrorsInterfaceSide"),
)
if mibBuilder.loadTexts:
    srpErrorsCountersCurrentEntry.setStatus("deprecated")
_SrpErrorsInterfaceSide_Type = InterfaceSide
_SrpErrorsInterfaceSide_Object = MibTableColumn
srpErrorsInterfaceSide = _SrpErrorsInterfaceSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1, 1, 1),
    _SrpErrorsInterfaceSide_Type()
)
srpErrorsInterfaceSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpErrorsInterfaceSide.setStatus("deprecated")
_SrpRingCurRxErrorsDataParity_Type = PerfCurrentCount64
_SrpRingCurRxErrorsDataParity_Object = MibTableColumn
srpRingCurRxErrorsDataParity = _SrpRingCurRxErrorsDataParity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1, 1, 2),
    _SrpRingCurRxErrorsDataParity_Type()
)
srpRingCurRxErrorsDataParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurRxErrorsDataParity.setStatus("deprecated")
_SrpRingCurRxErrorsShortPackets_Type = PerfCurrentCount64
_SrpRingCurRxErrorsShortPackets_Object = MibTableColumn
srpRingCurRxErrorsShortPackets = _SrpRingCurRxErrorsShortPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1, 1, 3),
    _SrpRingCurRxErrorsShortPackets_Type()
)
srpRingCurRxErrorsShortPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurRxErrorsShortPackets.setStatus("deprecated")
_SrpRingCurRxErrorsGiantPackets_Type = PerfCurrentCount64
_SrpRingCurRxErrorsGiantPackets_Object = MibTableColumn
srpRingCurRxErrorsGiantPackets = _SrpRingCurRxErrorsGiantPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1, 1, 4),
    _SrpRingCurRxErrorsGiantPackets_Type()
)
srpRingCurRxErrorsGiantPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurRxErrorsGiantPackets.setStatus("deprecated")
_SrpRingCurRxErrorsSideBadPackets_Type = PerfCurrentCount64
_SrpRingCurRxErrorsSideBadPackets_Object = MibTableColumn
srpRingCurRxErrorsSideBadPackets = _SrpRingCurRxErrorsSideBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1, 1, 5),
    _SrpRingCurRxErrorsSideBadPackets_Type()
)
srpRingCurRxErrorsSideBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurRxErrorsSideBadPackets.setStatus("deprecated")
_SrpRingCurRxErrorsCRC_Type = PerfCurrentCount64
_SrpRingCurRxErrorsCRC_Object = MibTableColumn
srpRingCurRxErrorsCRC = _SrpRingCurRxErrorsCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1, 1, 6),
    _SrpRingCurRxErrorsCRC_Type()
)
srpRingCurRxErrorsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingCurRxErrorsCRC.setStatus("deprecated")
_SrpHostCurRxErrorsDataParity_Type = PerfCurrentCount64
_SrpHostCurRxErrorsDataParity_Object = MibTableColumn
srpHostCurRxErrorsDataParity = _SrpHostCurRxErrorsDataParity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1, 1, 7),
    _SrpHostCurRxErrorsDataParity_Type()
)
srpHostCurRxErrorsDataParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurRxErrorsDataParity.setStatus("deprecated")
_SrpHostCurRxErrorsShortPackets_Type = PerfCurrentCount64
_SrpHostCurRxErrorsShortPackets_Object = MibTableColumn
srpHostCurRxErrorsShortPackets = _SrpHostCurRxErrorsShortPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1, 1, 8),
    _SrpHostCurRxErrorsShortPackets_Type()
)
srpHostCurRxErrorsShortPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurRxErrorsShortPackets.setStatus("deprecated")
_SrpHostCurRxErrorsGiantPackets_Type = PerfCurrentCount64
_SrpHostCurRxErrorsGiantPackets_Object = MibTableColumn
srpHostCurRxErrorsGiantPackets = _SrpHostCurRxErrorsGiantPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1, 1, 9),
    _SrpHostCurRxErrorsGiantPackets_Type()
)
srpHostCurRxErrorsGiantPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurRxErrorsGiantPackets.setStatus("deprecated")
_SrpHostCurRxErrorsSideBadPackets_Type = PerfCurrentCount64
_SrpHostCurRxErrorsSideBadPackets_Object = MibTableColumn
srpHostCurRxErrorsSideBadPackets = _SrpHostCurRxErrorsSideBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 1, 1, 10),
    _SrpHostCurRxErrorsSideBadPackets_Type()
)
srpHostCurRxErrorsSideBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostCurRxErrorsSideBadPackets.setStatus("deprecated")
_SrpErrorsCountersIntervalTable_Object = MibTable
srpErrorsCountersIntervalTable = _SrpErrorsCountersIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2)
)
if mibBuilder.loadTexts:
    srpErrorsCountersIntervalTable.setStatus("deprecated")
_SrpErrorsCountersIntervalEntry_Object = MibTableRow
srpErrorsCountersIntervalEntry = _SrpErrorsCountersIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1)
)
srpErrorsCountersIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SRP-MIB", "srpErrorsIntervalInterfaceSide"),
    (0, "CISCO-SRP-MIB", "srpErrorsIntervalNumber"),
)
if mibBuilder.loadTexts:
    srpErrorsCountersIntervalEntry.setStatus("deprecated")
_SrpErrorsIntervalInterfaceSide_Type = InterfaceSide
_SrpErrorsIntervalInterfaceSide_Object = MibTableColumn
srpErrorsIntervalInterfaceSide = _SrpErrorsIntervalInterfaceSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1, 1),
    _SrpErrorsIntervalInterfaceSide_Type()
)
srpErrorsIntervalInterfaceSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpErrorsIntervalInterfaceSide.setStatus("deprecated")


class _SrpErrorsIntervalNumber_Type(Integer32):
    """Custom type srpErrorsIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SrpErrorsIntervalNumber_Type.__name__ = "Integer32"
_SrpErrorsIntervalNumber_Object = MibTableColumn
srpErrorsIntervalNumber = _SrpErrorsIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1, 2),
    _SrpErrorsIntervalNumber_Type()
)
srpErrorsIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpErrorsIntervalNumber.setStatus("deprecated")
_SrpRingIntRxErrorsDataParity_Type = PerfIntervalCount64
_SrpRingIntRxErrorsDataParity_Object = MibTableColumn
srpRingIntRxErrorsDataParity = _SrpRingIntRxErrorsDataParity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1, 3),
    _SrpRingIntRxErrorsDataParity_Type()
)
srpRingIntRxErrorsDataParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntRxErrorsDataParity.setStatus("deprecated")
_SrpRingIntRxErrorsShortPackets_Type = PerfIntervalCount64
_SrpRingIntRxErrorsShortPackets_Object = MibTableColumn
srpRingIntRxErrorsShortPackets = _SrpRingIntRxErrorsShortPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1, 4),
    _SrpRingIntRxErrorsShortPackets_Type()
)
srpRingIntRxErrorsShortPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntRxErrorsShortPackets.setStatus("deprecated")
_SrpRingIntRxErrorsGiantPackets_Type = PerfIntervalCount64
_SrpRingIntRxErrorsGiantPackets_Object = MibTableColumn
srpRingIntRxErrorsGiantPackets = _SrpRingIntRxErrorsGiantPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1, 5),
    _SrpRingIntRxErrorsGiantPackets_Type()
)
srpRingIntRxErrorsGiantPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntRxErrorsGiantPackets.setStatus("deprecated")
_SrpRingIntRxErrorsSideBadPackets_Type = PerfIntervalCount64
_SrpRingIntRxErrorsSideBadPackets_Object = MibTableColumn
srpRingIntRxErrorsSideBadPackets = _SrpRingIntRxErrorsSideBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1, 6),
    _SrpRingIntRxErrorsSideBadPackets_Type()
)
srpRingIntRxErrorsSideBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntRxErrorsSideBadPackets.setStatus("deprecated")
_SrpRingIntRxErrorsCRC_Type = PerfIntervalCount64
_SrpRingIntRxErrorsCRC_Object = MibTableColumn
srpRingIntRxErrorsCRC = _SrpRingIntRxErrorsCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1, 7),
    _SrpRingIntRxErrorsCRC_Type()
)
srpRingIntRxErrorsCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpRingIntRxErrorsCRC.setStatus("deprecated")
_SrpHostIntRxErrorsDataParity_Type = PerfIntervalCount64
_SrpHostIntRxErrorsDataParity_Object = MibTableColumn
srpHostIntRxErrorsDataParity = _SrpHostIntRxErrorsDataParity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1, 8),
    _SrpHostIntRxErrorsDataParity_Type()
)
srpHostIntRxErrorsDataParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntRxErrorsDataParity.setStatus("deprecated")
_SrpHostIntRxErrorsShortPackets_Type = PerfIntervalCount64
_SrpHostIntRxErrorsShortPackets_Object = MibTableColumn
srpHostIntRxErrorsShortPackets = _SrpHostIntRxErrorsShortPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1, 9),
    _SrpHostIntRxErrorsShortPackets_Type()
)
srpHostIntRxErrorsShortPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntRxErrorsShortPackets.setStatus("deprecated")
_SrpHostIntRxErrorsGiantPackets_Type = PerfIntervalCount64
_SrpHostIntRxErrorsGiantPackets_Object = MibTableColumn
srpHostIntRxErrorsGiantPackets = _SrpHostIntRxErrorsGiantPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1, 10),
    _SrpHostIntRxErrorsGiantPackets_Type()
)
srpHostIntRxErrorsGiantPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntRxErrorsGiantPackets.setStatus("deprecated")
_SrpHostIntRxErrorsSideBadPackets_Type = PerfIntervalCount64
_SrpHostIntRxErrorsSideBadPackets_Object = MibTableColumn
srpHostIntRxErrorsSideBadPackets = _SrpHostIntRxErrorsSideBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 2, 1, 11),
    _SrpHostIntRxErrorsSideBadPackets_Type()
)
srpHostIntRxErrorsSideBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpHostIntRxErrorsSideBadPackets.setStatus("deprecated")
_SrpErrCntCurrTable_Object = MibTable
srpErrCntCurrTable = _SrpErrCntCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 3)
)
if mibBuilder.loadTexts:
    srpErrCntCurrTable.setStatus("current")
_SrpErrCntCurrEntry_Object = MibTableRow
srpErrCntCurrEntry = _SrpErrCntCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 3, 1)
)
srpErrCntCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SRP-MIB", "srpErrCntCurrInterfaceSide"),
)
if mibBuilder.loadTexts:
    srpErrCntCurrEntry.setStatus("current")
_SrpErrCntCurrInterfaceSide_Type = InterfaceSide
_SrpErrCntCurrInterfaceSide_Object = MibTableColumn
srpErrCntCurrInterfaceSide = _SrpErrCntCurrInterfaceSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 3, 1, 1),
    _SrpErrCntCurrInterfaceSide_Type()
)
srpErrCntCurrInterfaceSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpErrCntCurrInterfaceSide.setStatus("current")
_SrpErrCntCurrRingRxTtlExpPkts_Type = PerfCurrentCount64
_SrpErrCntCurrRingRxTtlExpPkts_Object = MibTableColumn
srpErrCntCurrRingRxTtlExpPkts = _SrpErrCntCurrRingRxTtlExpPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 3, 1, 2),
    _SrpErrCntCurrRingRxTtlExpPkts_Type()
)
srpErrCntCurrRingRxTtlExpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntCurrRingRxTtlExpPkts.setStatus("current")
_SrpErrCntCurrRingRxShortPkts_Type = PerfCurrentCount64
_SrpErrCntCurrRingRxShortPkts_Object = MibTableColumn
srpErrCntCurrRingRxShortPkts = _SrpErrCntCurrRingRxShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 3, 1, 3),
    _SrpErrCntCurrRingRxShortPkts_Type()
)
srpErrCntCurrRingRxShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntCurrRingRxShortPkts.setStatus("current")
_SrpErrCntCurrRingRxGiantPkts_Type = PerfCurrentCount64
_SrpErrCntCurrRingRxGiantPkts_Object = MibTableColumn
srpErrCntCurrRingRxGiantPkts = _SrpErrCntCurrRingRxGiantPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 3, 1, 4),
    _SrpErrCntCurrRingRxGiantPkts_Type()
)
srpErrCntCurrRingRxGiantPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntCurrRingRxGiantPkts.setStatus("current")
_SrpErrCntCurrRingRxAbortPkts_Type = PerfCurrentCount64
_SrpErrCntCurrRingRxAbortPkts_Object = MibTableColumn
srpErrCntCurrRingRxAbortPkts = _SrpErrCntCurrRingRxAbortPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 3, 1, 5),
    _SrpErrCntCurrRingRxAbortPkts_Type()
)
srpErrCntCurrRingRxAbortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntCurrRingRxAbortPkts.setStatus("current")
_SrpErrCntCurrRingRxCRC_Type = PerfCurrentCount64
_SrpErrCntCurrRingRxCRC_Object = MibTableColumn
srpErrCntCurrRingRxCRC = _SrpErrCntCurrRingRxCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 3, 1, 6),
    _SrpErrCntCurrRingRxCRC_Type()
)
srpErrCntCurrRingRxCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntCurrRingRxCRC.setStatus("current")
_SrpErrCntCurrHostRxDiscardPkts_Type = PerfCurrentCount64
_SrpErrCntCurrHostRxDiscardPkts_Object = MibTableColumn
srpErrCntCurrHostRxDiscardPkts = _SrpErrCntCurrHostRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 3, 1, 7),
    _SrpErrCntCurrHostRxDiscardPkts_Type()
)
srpErrCntCurrHostRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntCurrHostRxDiscardPkts.setStatus("current")
_SrpErrCntCurrHostRxShortPkts_Type = PerfCurrentCount64
_SrpErrCntCurrHostRxShortPkts_Object = MibTableColumn
srpErrCntCurrHostRxShortPkts = _SrpErrCntCurrHostRxShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 3, 1, 8),
    _SrpErrCntCurrHostRxShortPkts_Type()
)
srpErrCntCurrHostRxShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntCurrHostRxShortPkts.setStatus("current")
_SrpErrCntCurrHostRxGiantPkts_Type = PerfCurrentCount64
_SrpErrCntCurrHostRxGiantPkts_Object = MibTableColumn
srpErrCntCurrHostRxGiantPkts = _SrpErrCntCurrHostRxGiantPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 3, 1, 9),
    _SrpErrCntCurrHostRxGiantPkts_Type()
)
srpErrCntCurrHostRxGiantPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntCurrHostRxGiantPkts.setStatus("current")
_SrpErrCntIntTable_Object = MibTable
srpErrCntIntTable = _SrpErrCntIntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4)
)
if mibBuilder.loadTexts:
    srpErrCntIntTable.setStatus("current")
_SrpErrCntIntEntry_Object = MibTableRow
srpErrCntIntEntry = _SrpErrCntIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4, 1)
)
srpErrCntIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SRP-MIB", "srpErrCntIntInterfaceSide"),
    (0, "CISCO-SRP-MIB", "srpErrCntIntNumber"),
)
if mibBuilder.loadTexts:
    srpErrCntIntEntry.setStatus("current")
_SrpErrCntIntInterfaceSide_Type = InterfaceSide
_SrpErrCntIntInterfaceSide_Object = MibTableColumn
srpErrCntIntInterfaceSide = _SrpErrCntIntInterfaceSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4, 1, 1),
    _SrpErrCntIntInterfaceSide_Type()
)
srpErrCntIntInterfaceSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpErrCntIntInterfaceSide.setStatus("current")


class _SrpErrCntIntNumber_Type(Integer32):
    """Custom type srpErrCntIntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SrpErrCntIntNumber_Type.__name__ = "Integer32"
_SrpErrCntIntNumber_Object = MibTableColumn
srpErrCntIntNumber = _SrpErrCntIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4, 1, 2),
    _SrpErrCntIntNumber_Type()
)
srpErrCntIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srpErrCntIntNumber.setStatus("current")
_SrpErrCntIntRingRxTtlExpPkts_Type = PerfIntervalCount64
_SrpErrCntIntRingRxTtlExpPkts_Object = MibTableColumn
srpErrCntIntRingRxTtlExpPkts = _SrpErrCntIntRingRxTtlExpPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4, 1, 3),
    _SrpErrCntIntRingRxTtlExpPkts_Type()
)
srpErrCntIntRingRxTtlExpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntIntRingRxTtlExpPkts.setStatus("current")
_SrpErrCntIntRingRxShortPkts_Type = PerfIntervalCount64
_SrpErrCntIntRingRxShortPkts_Object = MibTableColumn
srpErrCntIntRingRxShortPkts = _SrpErrCntIntRingRxShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4, 1, 4),
    _SrpErrCntIntRingRxShortPkts_Type()
)
srpErrCntIntRingRxShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntIntRingRxShortPkts.setStatus("current")
_SrpErrCntIntRingRxGiantPkts_Type = PerfIntervalCount64
_SrpErrCntIntRingRxGiantPkts_Object = MibTableColumn
srpErrCntIntRingRxGiantPkts = _SrpErrCntIntRingRxGiantPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4, 1, 5),
    _SrpErrCntIntRingRxGiantPkts_Type()
)
srpErrCntIntRingRxGiantPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntIntRingRxGiantPkts.setStatus("current")
_SrpErrCntIntRingRxAbortPkts_Type = PerfIntervalCount64
_SrpErrCntIntRingRxAbortPkts_Object = MibTableColumn
srpErrCntIntRingRxAbortPkts = _SrpErrCntIntRingRxAbortPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4, 1, 6),
    _SrpErrCntIntRingRxAbortPkts_Type()
)
srpErrCntIntRingRxAbortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntIntRingRxAbortPkts.setStatus("current")
_SrpErrCntIntRingRxCRC_Type = PerfIntervalCount64
_SrpErrCntIntRingRxCRC_Object = MibTableColumn
srpErrCntIntRingRxCRC = _SrpErrCntIntRingRxCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4, 1, 7),
    _SrpErrCntIntRingRxCRC_Type()
)
srpErrCntIntRingRxCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntIntRingRxCRC.setStatus("current")
_SrpErrCntIntHostRxDiscardPkts_Type = PerfIntervalCount64
_SrpErrCntIntHostRxDiscardPkts_Object = MibTableColumn
srpErrCntIntHostRxDiscardPkts = _SrpErrCntIntHostRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4, 1, 8),
    _SrpErrCntIntHostRxDiscardPkts_Type()
)
srpErrCntIntHostRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntIntHostRxDiscardPkts.setStatus("current")
_SrpErrCntIntHostRxShortPkts_Type = PerfIntervalCount64
_SrpErrCntIntHostRxShortPkts_Object = MibTableColumn
srpErrCntIntHostRxShortPkts = _SrpErrCntIntHostRxShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4, 1, 9),
    _SrpErrCntIntHostRxShortPkts_Type()
)
srpErrCntIntHostRxShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntIntHostRxShortPkts.setStatus("current")
_SrpErrCntIntHostRxGiantPkts_Type = PerfIntervalCount64
_SrpErrCntIntHostRxGiantPkts_Object = MibTableColumn
srpErrCntIntHostRxGiantPkts = _SrpErrCntIntHostRxGiantPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 4, 4, 1, 10),
    _SrpErrCntIntHostRxGiantPkts_Type()
)
srpErrCntIntHostRxGiantPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srpErrCntIntHostRxGiantPkts.setStatus("current")
_SrpTrapsNotificationsPrefix_ObjectIdentity = ObjectIdentity
srpTrapsNotificationsPrefix = _SrpTrapsNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 5)
)
_SrpTrapsNotifications_ObjectIdentity = ObjectIdentity
srpTrapsNotifications = _SrpTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 5, 0)
)
_SrpConformance_ObjectIdentity = ObjectIdentity
srpConformance = _SrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6)
)
_SrpGroups_ObjectIdentity = ObjectIdentity
srpGroups = _SrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1)
)
_SrpCompliances_ObjectIdentity = ObjectIdentity
srpCompliances = _SrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 2)
)

# Managed Objects groups

srpIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 1)
)
srpIfGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpMACAddress"),
        ("CISCO-SRP-MIB", "srpPriorityThreshold"),
        ("CISCO-SRP-MIB", "srpNodesOnTheRing"),
        ("CISCO-SRP-MIB", "srpIpsState"),
        ("CISCO-SRP-MIB", "srpIpsLockedOut"),
        ("CISCO-SRP-MIB", "srpIpsWaitToRestoreTimer"),
        ("CISCO-SRP-MIB", "srpIfTimeElapsed"),
        ("CISCO-SRP-MIB", "srpIfValidIntervals"))
)
if mibBuilder.loadTexts:
    srpIfGroup.setStatus("current")

srpMACSideGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 2)
)
srpMACSideGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpMACNeighborAddress"),
        ("CISCO-SRP-MIB", "srpMACSideWrapped"),
        ("CISCO-SRP-MIB", "srpMACIpsMgmtRequestedMode"),
        ("CISCO-SRP-MIB", "srpMACIpsAutoDetectMode"),
        ("CISCO-SRP-MIB", "srpMACIpsRemoteMode"),
        ("CISCO-SRP-MIB", "srpMACIpsRemoteType"),
        ("CISCO-SRP-MIB", "srpMACIpsActiveMode"),
        ("CISCO-SRP-MIB", "srpMACIpsWrapCounter"),
        ("CISCO-SRP-MIB", "srpMACIpsLastWrapTimeStamp"),
        ("CISCO-SRP-MIB", "srpMACIpsLastUnWrapTimeStamp"),
        ("CISCO-SRP-MIB", "srpMACClockSourceMode"),
        ("CISCO-SRP-MIB", "srpMACTopologyTimer"))
)
if mibBuilder.loadTexts:
    srpMACSideGroup.setStatus("current")

srpRingTopologyMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 3)
)
srpRingTopologyMapGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpNodeMACAddress"),
        ("CISCO-SRP-MIB", "srpNodeWrapped"),
        ("CISCO-SRP-MIB", "srpNodeName"))
)
if mibBuilder.loadTexts:
    srpRingTopologyMapGroup.setStatus("current")

srpMACCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 4)
)
srpMACCountersGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpMACCountPktsBySourceFlag"),
        ("CISCO-SRP-MIB", "srpMACCountPktsBySourceAddress"),
        ("CISCO-SRP-MIB", "srpMACSourceDiscontTimeStamp"),
        ("CISCO-SRP-MIB", "srpMACCountPktsBySource"),
        ("CISCO-SRP-MIB", "srpMACCountPktsByDestinationFlag"),
        ("CISCO-SRP-MIB", "srpMACCountPktsByDestAddress"),
        ("CISCO-SRP-MIB", "srpMACDestDiscontTimeStamp"),
        ("CISCO-SRP-MIB", "srpMACCountPktsByDest"),
        ("CISCO-SRP-MIB", "srpMACRejectPktsBySourceFlag"),
        ("CISCO-SRP-MIB", "srpMACRejectPktsBySourceAddress"),
        ("CISCO-SRP-MIB", "srpMACRejectPktsByDestFlag"),
        ("CISCO-SRP-MIB", "srpMACRejectPktsByDestAddress"))
)
if mibBuilder.loadTexts:
    srpMACCountersGroup.setStatus("deprecated")

srpRingCountersCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 5)
)
srpRingCountersCurrentGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpRingCurUcastLowPriPktsIn"),
        ("CISCO-SRP-MIB", "srpRingCurUcastLowPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpRingCurMcastLowPriPktsIn"),
        ("CISCO-SRP-MIB", "srpRingCurMcastLowPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpRingCurUcastHighPriPktsIn"),
        ("CISCO-SRP-MIB", "srpRingCurUcastHighPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpRingCurMcastHighPriPktsIn"),
        ("CISCO-SRP-MIB", "srpRingCurMcastHighPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpRingCurUcastLowPriPktsOut"),
        ("CISCO-SRP-MIB", "srpRingCurUcastLowPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpRingCurMcastLowPriPktsOut"),
        ("CISCO-SRP-MIB", "srpRingCurMcastLowPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpRingCurUcastHighPriPktsOut"),
        ("CISCO-SRP-MIB", "srpRingCurUcastHighPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpRingCurMcastHighPriPktsOut"),
        ("CISCO-SRP-MIB", "srpRingCurMcastHighPriOctetsOut"))
)
if mibBuilder.loadTexts:
    srpRingCountersCurrentGroup.setStatus("current")

srpRingCountersIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 6)
)
srpRingCountersIntervalGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpRingIntWrapCounter"),
        ("CISCO-SRP-MIB", "srpRingIntUcastLowPriPktsIn"),
        ("CISCO-SRP-MIB", "srpRingIntUcastLowPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpRingIntMcastLowPriPktsIn"),
        ("CISCO-SRP-MIB", "srpRingIntMcastLowPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpRingIntUcastHighPriPktsIn"),
        ("CISCO-SRP-MIB", "srpRingIntUcastHighPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpRingIntMcastHighPriPktsIn"),
        ("CISCO-SRP-MIB", "srpRingIntMcastHighPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpRingIntUcastLowPriPktsOut"),
        ("CISCO-SRP-MIB", "srpRingIntUcastLowPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpRingIntMcastLowPriPktsOut"),
        ("CISCO-SRP-MIB", "srpRingIntMcastLowPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpRingIntUcastHighPriPktsOut"),
        ("CISCO-SRP-MIB", "srpRingIntUcastHighPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpRingIntMcastHighPriPktsOut"),
        ("CISCO-SRP-MIB", "srpRingIntMcastHighPriOctetsOut"))
)
if mibBuilder.loadTexts:
    srpRingCountersIntervalGroup.setStatus("current")

srpHostCountersCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 7)
)
srpHostCountersCurrentGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpHostCurUcastLowPriPktsIn"),
        ("CISCO-SRP-MIB", "srpHostCurUcastLowPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpHostCurMcastLowPriPktsIn"),
        ("CISCO-SRP-MIB", "srpHostCurMcastLowPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpHostCurUcastHighPriPktsIn"),
        ("CISCO-SRP-MIB", "srpHostCurUcastHighPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpHostCurMcastHighPriPktsIn"),
        ("CISCO-SRP-MIB", "srpHostCurMcastHighPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpHostCurUcastLowPriPktsOut"),
        ("CISCO-SRP-MIB", "srpHostCurUcastLowPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpHostCurMcastLowPriPktsOut"),
        ("CISCO-SRP-MIB", "srpHostCurMcastLowPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpHostCurUcastHighPriPktsOut"),
        ("CISCO-SRP-MIB", "srpHostCurUcastHighPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpHostCurMcastHighPriPktsOut"),
        ("CISCO-SRP-MIB", "srpHostCurMcastHighPriOctetsOut"))
)
if mibBuilder.loadTexts:
    srpHostCountersCurrentGroup.setStatus("current")

srpHostCountersIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 8)
)
srpHostCountersIntervalGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpHostIntUcastLowPriPktsIn"),
        ("CISCO-SRP-MIB", "srpHostIntUcastLowPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpHostIntMcastLowPriPktsIn"),
        ("CISCO-SRP-MIB", "srpHostIntMcastLowPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpHostIntUcastHighPriPktsIn"),
        ("CISCO-SRP-MIB", "srpHostIntUcastHighPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpHostIntMcastHighPriPktsIn"),
        ("CISCO-SRP-MIB", "srpHostIntMcastHighPriOctetsIn"),
        ("CISCO-SRP-MIB", "srpHostIntUcastLowPriPktsOut"),
        ("CISCO-SRP-MIB", "srpHostIntUcastLowPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpHostIntMcastLowPriPktsOut"),
        ("CISCO-SRP-MIB", "srpHostIntMcastLowPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpHostIntUcastHighPriPktsOut"),
        ("CISCO-SRP-MIB", "srpHostIntUcastHighPriOctetsOut"),
        ("CISCO-SRP-MIB", "srpHostIntMcastHighPriPktsOut"),
        ("CISCO-SRP-MIB", "srpHostIntMcastHighPriOctetsOut"))
)
if mibBuilder.loadTexts:
    srpHostCountersIntervalGroup.setStatus("current")

srpErrorsCountersCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 9)
)
srpErrorsCountersCurrentGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpRingCurRxErrorsDataParity"),
        ("CISCO-SRP-MIB", "srpRingCurRxErrorsShortPackets"),
        ("CISCO-SRP-MIB", "srpRingCurRxErrorsGiantPackets"),
        ("CISCO-SRP-MIB", "srpRingCurRxErrorsSideBadPackets"),
        ("CISCO-SRP-MIB", "srpRingCurRxErrorsCRC"),
        ("CISCO-SRP-MIB", "srpHostCurRxErrorsDataParity"),
        ("CISCO-SRP-MIB", "srpHostCurRxErrorsShortPackets"),
        ("CISCO-SRP-MIB", "srpHostCurRxErrorsGiantPackets"),
        ("CISCO-SRP-MIB", "srpHostCurRxErrorsSideBadPackets"))
)
if mibBuilder.loadTexts:
    srpErrorsCountersCurrentGroup.setStatus("deprecated")

srpErrorsCountersIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 10)
)
srpErrorsCountersIntervalGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpRingIntRxErrorsDataParity"),
        ("CISCO-SRP-MIB", "srpRingIntRxErrorsShortPackets"),
        ("CISCO-SRP-MIB", "srpRingIntRxErrorsGiantPackets"),
        ("CISCO-SRP-MIB", "srpRingIntRxErrorsSideBadPackets"),
        ("CISCO-SRP-MIB", "srpRingIntRxErrorsCRC"),
        ("CISCO-SRP-MIB", "srpHostIntRxErrorsDataParity"),
        ("CISCO-SRP-MIB", "srpHostIntRxErrorsShortPackets"),
        ("CISCO-SRP-MIB", "srpHostIntRxErrorsGiantPackets"),
        ("CISCO-SRP-MIB", "srpHostIntRxErrorsSideBadPackets"))
)
if mibBuilder.loadTexts:
    srpErrorsCountersIntervalGroup.setStatus("deprecated")

srpErrCntCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 11)
)
srpErrCntCurrGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpErrCntCurrRingRxTtlExpPkts"),
        ("CISCO-SRP-MIB", "srpErrCntCurrRingRxShortPkts"),
        ("CISCO-SRP-MIB", "srpErrCntCurrRingRxGiantPkts"),
        ("CISCO-SRP-MIB", "srpErrCntCurrRingRxAbortPkts"),
        ("CISCO-SRP-MIB", "srpErrCntCurrRingRxCRC"),
        ("CISCO-SRP-MIB", "srpErrCntCurrHostRxDiscardPkts"),
        ("CISCO-SRP-MIB", "srpErrCntCurrHostRxShortPkts"),
        ("CISCO-SRP-MIB", "srpErrCntCurrHostRxGiantPkts"))
)
if mibBuilder.loadTexts:
    srpErrCntCurrGroup.setStatus("current")

srpErrCntIntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 12)
)
srpErrCntIntGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpErrCntIntRingRxTtlExpPkts"),
        ("CISCO-SRP-MIB", "srpErrCntIntRingRxShortPkts"),
        ("CISCO-SRP-MIB", "srpErrCntIntRingRxGiantPkts"),
        ("CISCO-SRP-MIB", "srpErrCntIntRingRxAbortPkts"),
        ("CISCO-SRP-MIB", "srpErrCntIntRingRxCRC"),
        ("CISCO-SRP-MIB", "srpErrCntIntHostRxDiscardPkts"),
        ("CISCO-SRP-MIB", "srpErrCntIntHostRxShortPkts"),
        ("CISCO-SRP-MIB", "srpErrCntIntHostRxGiantPkts"))
)
if mibBuilder.loadTexts:
    srpErrCntIntGroup.setStatus("current")


# Notification objects

srpTrapRingWrapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 5, 0, 1)
)
srpTrapRingWrapped.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-SRP-MIB", "srpIpsState"),
        ("CISCO-SRP-MIB", "srpMACIpsAutoDetectMode"),
        ("CISCO-SRP-MIB", "srpMACIpsRemoteMode"),
        ("CISCO-SRP-MIB", "srpMACIpsRemoteType"),
        ("CISCO-SRP-MIB", "srpMACIpsActiveMode"),
        ("CISCO-SRP-MIB", "srpMACIpsWrapCounter"),
        ("CISCO-SRP-MIB", "srpMACIpsLastWrapTimeStamp"),
        ("CISCO-SRP-MIB", "srpMACIpsLastUnWrapTimeStamp"))
)
if mibBuilder.loadTexts:
    srpTrapRingWrapped.setStatus(
        "current"
    )

srpTrapRingRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 5, 0, 2)
)
srpTrapRingRestored.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-SRP-MIB", "srpIpsState"),
        ("CISCO-SRP-MIB", "srpMACIpsAutoDetectMode"),
        ("CISCO-SRP-MIB", "srpMACIpsRemoteMode"),
        ("CISCO-SRP-MIB", "srpMACIpsRemoteType"),
        ("CISCO-SRP-MIB", "srpMACIpsActiveMode"),
        ("CISCO-SRP-MIB", "srpMACIpsWrapCounter"),
        ("CISCO-SRP-MIB", "srpMACIpsLastWrapTimeStamp"),
        ("CISCO-SRP-MIB", "srpMACIpsLastUnWrapTimeStamp"))
)
if mibBuilder.loadTexts:
    srpTrapRingRestored.setStatus(
        "current"
    )


# Notifications groups

srpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 1, 13)
)
srpNotificationsGroup.setObjects(
      *(("CISCO-SRP-MIB", "srpTrapRingWrapped"),
        ("CISCO-SRP-MIB", "srpTrapRingRestored"))
)
if mibBuilder.loadTexts:
    srpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

srpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 2, 1)
)
if mibBuilder.loadTexts:
    srpCompliance.setStatus(
        "current"
    )

srpComplianceOld = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 60, 6, 2, 2)
)
if mibBuilder.loadTexts:
    srpComplianceOld.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SRP-MIB",
    **{"InterfaceSide": InterfaceSide,
       "IpsMode": IpsMode,
       "PerfCurrentCount64": PerfCurrentCount64,
       "PerfIntervalCount64": PerfIntervalCount64,
       "ciscosrpMIB": ciscosrpMIB,
       "srpMAC": srpMAC,
       "srpIfTable": srpIfTable,
       "srpIfEntry": srpIfEntry,
       "srpMACAddress": srpMACAddress,
       "srpPriorityThreshold": srpPriorityThreshold,
       "srpNodesOnTheRing": srpNodesOnTheRing,
       "srpIpsState": srpIpsState,
       "srpIpsLockedOut": srpIpsLockedOut,
       "srpIpsWaitToRestoreTimer": srpIpsWaitToRestoreTimer,
       "srpIfTimeElapsed": srpIfTimeElapsed,
       "srpIfValidIntervals": srpIfValidIntervals,
       "srpMACSideTable": srpMACSideTable,
       "srpMACSideEntry": srpMACSideEntry,
       "srpMACInterfaceSide": srpMACInterfaceSide,
       "srpMACNeighborAddress": srpMACNeighborAddress,
       "srpMACSideWrapped": srpMACSideWrapped,
       "srpMACIpsMgmtRequestedMode": srpMACIpsMgmtRequestedMode,
       "srpMACIpsAutoDetectMode": srpMACIpsAutoDetectMode,
       "srpMACIpsRemoteMode": srpMACIpsRemoteMode,
       "srpMACIpsRemoteType": srpMACIpsRemoteType,
       "srpMACIpsActiveMode": srpMACIpsActiveMode,
       "srpMACIpsWrapCounter": srpMACIpsWrapCounter,
       "srpMACIpsLastWrapTimeStamp": srpMACIpsLastWrapTimeStamp,
       "srpMACIpsLastUnWrapTimeStamp": srpMACIpsLastUnWrapTimeStamp,
       "srpMACClockSourceMode": srpMACClockSourceMode,
       "srpMACTopologyTimer": srpMACTopologyTimer,
       "srpRingTopologyMapTable": srpRingTopologyMapTable,
       "srpRingTopologyMapEntry": srpRingTopologyMapEntry,
       "srpNodeHopsNumber": srpNodeHopsNumber,
       "srpNodeMACAddress": srpNodeMACAddress,
       "srpNodeWrapped": srpNodeWrapped,
       "srpNodeName": srpNodeName,
       "srpMACCountersTable": srpMACCountersTable,
       "srpMACCountersEntry": srpMACCountersEntry,
       "srpMACCountPktsBySourceFlag": srpMACCountPktsBySourceFlag,
       "srpMACCountPktsBySourceAddress": srpMACCountPktsBySourceAddress,
       "srpMACSourceDiscontTimeStamp": srpMACSourceDiscontTimeStamp,
       "srpMACCountPktsBySource": srpMACCountPktsBySource,
       "srpMACCountPktsByDestinationFlag": srpMACCountPktsByDestinationFlag,
       "srpMACCountPktsByDestAddress": srpMACCountPktsByDestAddress,
       "srpMACDestDiscontTimeStamp": srpMACDestDiscontTimeStamp,
       "srpMACCountPktsByDest": srpMACCountPktsByDest,
       "srpMACRejectPktsBySourceFlag": srpMACRejectPktsBySourceFlag,
       "srpMACRejectPktsBySourceAddress": srpMACRejectPktsBySourceAddress,
       "srpMACRejectPktsByDestFlag": srpMACRejectPktsByDestFlag,
       "srpMACRejectPktsByDestAddress": srpMACRejectPktsByDestAddress,
       "srpRingCounters": srpRingCounters,
       "srpRingCountersCurrentTable": srpRingCountersCurrentTable,
       "srpRingCountersCurrentEntry": srpRingCountersCurrentEntry,
       "srpRingInterfaceSide": srpRingInterfaceSide,
       "srpRingCurUcastLowPriPktsIn": srpRingCurUcastLowPriPktsIn,
       "srpRingCurUcastLowPriOctetsIn": srpRingCurUcastLowPriOctetsIn,
       "srpRingCurMcastLowPriPktsIn": srpRingCurMcastLowPriPktsIn,
       "srpRingCurMcastLowPriOctetsIn": srpRingCurMcastLowPriOctetsIn,
       "srpRingCurUcastHighPriPktsIn": srpRingCurUcastHighPriPktsIn,
       "srpRingCurUcastHighPriOctetsIn": srpRingCurUcastHighPriOctetsIn,
       "srpRingCurMcastHighPriPktsIn": srpRingCurMcastHighPriPktsIn,
       "srpRingCurMcastHighPriOctetsIn": srpRingCurMcastHighPriOctetsIn,
       "srpRingCurUcastLowPriPktsOut": srpRingCurUcastLowPriPktsOut,
       "srpRingCurUcastLowPriOctetsOut": srpRingCurUcastLowPriOctetsOut,
       "srpRingCurMcastLowPriPktsOut": srpRingCurMcastLowPriPktsOut,
       "srpRingCurMcastLowPriOctetsOut": srpRingCurMcastLowPriOctetsOut,
       "srpRingCurUcastHighPriPktsOut": srpRingCurUcastHighPriPktsOut,
       "srpRingCurUcastHighPriOctetsOut": srpRingCurUcastHighPriOctetsOut,
       "srpRingCurMcastHighPriPktsOut": srpRingCurMcastHighPriPktsOut,
       "srpRingCurMcastHighPriOctetsOut": srpRingCurMcastHighPriOctetsOut,
       "srpRingCountersIntervalTable": srpRingCountersIntervalTable,
       "srpRingCountersIntervalEntry": srpRingCountersIntervalEntry,
       "srpRingIntInterfaceSide": srpRingIntInterfaceSide,
       "srpRingIntNumber": srpRingIntNumber,
       "srpRingIntWrapCounter": srpRingIntWrapCounter,
       "srpRingIntUcastLowPriPktsIn": srpRingIntUcastLowPriPktsIn,
       "srpRingIntUcastLowPriOctetsIn": srpRingIntUcastLowPriOctetsIn,
       "srpRingIntMcastLowPriPktsIn": srpRingIntMcastLowPriPktsIn,
       "srpRingIntMcastLowPriOctetsIn": srpRingIntMcastLowPriOctetsIn,
       "srpRingIntUcastHighPriPktsIn": srpRingIntUcastHighPriPktsIn,
       "srpRingIntUcastHighPriOctetsIn": srpRingIntUcastHighPriOctetsIn,
       "srpRingIntMcastHighPriPktsIn": srpRingIntMcastHighPriPktsIn,
       "srpRingIntMcastHighPriOctetsIn": srpRingIntMcastHighPriOctetsIn,
       "srpRingIntUcastLowPriPktsOut": srpRingIntUcastLowPriPktsOut,
       "srpRingIntUcastLowPriOctetsOut": srpRingIntUcastLowPriOctetsOut,
       "srpRingIntMcastLowPriPktsOut": srpRingIntMcastLowPriPktsOut,
       "srpRingIntMcastLowPriOctetsOut": srpRingIntMcastLowPriOctetsOut,
       "srpRingIntUcastHighPriPktsOut": srpRingIntUcastHighPriPktsOut,
       "srpRingIntUcastHighPriOctetsOut": srpRingIntUcastHighPriOctetsOut,
       "srpRingIntMcastHighPriPktsOut": srpRingIntMcastHighPriPktsOut,
       "srpRingIntMcastHighPriOctetsOut": srpRingIntMcastHighPriOctetsOut,
       "srpHostCounters": srpHostCounters,
       "srpHostCountersCurrentTable": srpHostCountersCurrentTable,
       "srpHostCountersCurrentEntry": srpHostCountersCurrentEntry,
       "srpHostInterfaceSide": srpHostInterfaceSide,
       "srpHostCurUcastLowPriPktsIn": srpHostCurUcastLowPriPktsIn,
       "srpHostCurUcastLowPriOctetsIn": srpHostCurUcastLowPriOctetsIn,
       "srpHostCurMcastLowPriPktsIn": srpHostCurMcastLowPriPktsIn,
       "srpHostCurMcastLowPriOctetsIn": srpHostCurMcastLowPriOctetsIn,
       "srpHostCurUcastHighPriPktsIn": srpHostCurUcastHighPriPktsIn,
       "srpHostCurUcastHighPriOctetsIn": srpHostCurUcastHighPriOctetsIn,
       "srpHostCurMcastHighPriPktsIn": srpHostCurMcastHighPriPktsIn,
       "srpHostCurMcastHighPriOctetsIn": srpHostCurMcastHighPriOctetsIn,
       "srpHostCurUcastLowPriPktsOut": srpHostCurUcastLowPriPktsOut,
       "srpHostCurUcastLowPriOctetsOut": srpHostCurUcastLowPriOctetsOut,
       "srpHostCurMcastLowPriPktsOut": srpHostCurMcastLowPriPktsOut,
       "srpHostCurMcastLowPriOctetsOut": srpHostCurMcastLowPriOctetsOut,
       "srpHostCurUcastHighPriPktsOut": srpHostCurUcastHighPriPktsOut,
       "srpHostCurUcastHighPriOctetsOut": srpHostCurUcastHighPriOctetsOut,
       "srpHostCurMcastHighPriPktsOut": srpHostCurMcastHighPriPktsOut,
       "srpHostCurMcastHighPriOctetsOut": srpHostCurMcastHighPriOctetsOut,
       "srpHostCountersIntervalTable": srpHostCountersIntervalTable,
       "srpHostCountersIntervalEntry": srpHostCountersIntervalEntry,
       "srpHostIntInterfaceSide": srpHostIntInterfaceSide,
       "srpHostIntNumber": srpHostIntNumber,
       "srpHostIntUcastLowPriPktsIn": srpHostIntUcastLowPriPktsIn,
       "srpHostIntUcastLowPriOctetsIn": srpHostIntUcastLowPriOctetsIn,
       "srpHostIntMcastLowPriPktsIn": srpHostIntMcastLowPriPktsIn,
       "srpHostIntMcastLowPriOctetsIn": srpHostIntMcastLowPriOctetsIn,
       "srpHostIntUcastHighPriPktsIn": srpHostIntUcastHighPriPktsIn,
       "srpHostIntUcastHighPriOctetsIn": srpHostIntUcastHighPriOctetsIn,
       "srpHostIntMcastHighPriPktsIn": srpHostIntMcastHighPriPktsIn,
       "srpHostIntMcastHighPriOctetsIn": srpHostIntMcastHighPriOctetsIn,
       "srpHostIntUcastLowPriPktsOut": srpHostIntUcastLowPriPktsOut,
       "srpHostIntUcastLowPriOctetsOut": srpHostIntUcastLowPriOctetsOut,
       "srpHostIntMcastLowPriPktsOut": srpHostIntMcastLowPriPktsOut,
       "srpHostIntMcastLowPriOctetsOut": srpHostIntMcastLowPriOctetsOut,
       "srpHostIntUcastHighPriPktsOut": srpHostIntUcastHighPriPktsOut,
       "srpHostIntUcastHighPriOctetsOut": srpHostIntUcastHighPriOctetsOut,
       "srpHostIntMcastHighPriPktsOut": srpHostIntMcastHighPriPktsOut,
       "srpHostIntMcastHighPriOctetsOut": srpHostIntMcastHighPriOctetsOut,
       "srpErrorsCounters": srpErrorsCounters,
       "srpErrorsCountersCurrentTable": srpErrorsCountersCurrentTable,
       "srpErrorsCountersCurrentEntry": srpErrorsCountersCurrentEntry,
       "srpErrorsInterfaceSide": srpErrorsInterfaceSide,
       "srpRingCurRxErrorsDataParity": srpRingCurRxErrorsDataParity,
       "srpRingCurRxErrorsShortPackets": srpRingCurRxErrorsShortPackets,
       "srpRingCurRxErrorsGiantPackets": srpRingCurRxErrorsGiantPackets,
       "srpRingCurRxErrorsSideBadPackets": srpRingCurRxErrorsSideBadPackets,
       "srpRingCurRxErrorsCRC": srpRingCurRxErrorsCRC,
       "srpHostCurRxErrorsDataParity": srpHostCurRxErrorsDataParity,
       "srpHostCurRxErrorsShortPackets": srpHostCurRxErrorsShortPackets,
       "srpHostCurRxErrorsGiantPackets": srpHostCurRxErrorsGiantPackets,
       "srpHostCurRxErrorsSideBadPackets": srpHostCurRxErrorsSideBadPackets,
       "srpErrorsCountersIntervalTable": srpErrorsCountersIntervalTable,
       "srpErrorsCountersIntervalEntry": srpErrorsCountersIntervalEntry,
       "srpErrorsIntervalInterfaceSide": srpErrorsIntervalInterfaceSide,
       "srpErrorsIntervalNumber": srpErrorsIntervalNumber,
       "srpRingIntRxErrorsDataParity": srpRingIntRxErrorsDataParity,
       "srpRingIntRxErrorsShortPackets": srpRingIntRxErrorsShortPackets,
       "srpRingIntRxErrorsGiantPackets": srpRingIntRxErrorsGiantPackets,
       "srpRingIntRxErrorsSideBadPackets": srpRingIntRxErrorsSideBadPackets,
       "srpRingIntRxErrorsCRC": srpRingIntRxErrorsCRC,
       "srpHostIntRxErrorsDataParity": srpHostIntRxErrorsDataParity,
       "srpHostIntRxErrorsShortPackets": srpHostIntRxErrorsShortPackets,
       "srpHostIntRxErrorsGiantPackets": srpHostIntRxErrorsGiantPackets,
       "srpHostIntRxErrorsSideBadPackets": srpHostIntRxErrorsSideBadPackets,
       "srpErrCntCurrTable": srpErrCntCurrTable,
       "srpErrCntCurrEntry": srpErrCntCurrEntry,
       "srpErrCntCurrInterfaceSide": srpErrCntCurrInterfaceSide,
       "srpErrCntCurrRingRxTtlExpPkts": srpErrCntCurrRingRxTtlExpPkts,
       "srpErrCntCurrRingRxShortPkts": srpErrCntCurrRingRxShortPkts,
       "srpErrCntCurrRingRxGiantPkts": srpErrCntCurrRingRxGiantPkts,
       "srpErrCntCurrRingRxAbortPkts": srpErrCntCurrRingRxAbortPkts,
       "srpErrCntCurrRingRxCRC": srpErrCntCurrRingRxCRC,
       "srpErrCntCurrHostRxDiscardPkts": srpErrCntCurrHostRxDiscardPkts,
       "srpErrCntCurrHostRxShortPkts": srpErrCntCurrHostRxShortPkts,
       "srpErrCntCurrHostRxGiantPkts": srpErrCntCurrHostRxGiantPkts,
       "srpErrCntIntTable": srpErrCntIntTable,
       "srpErrCntIntEntry": srpErrCntIntEntry,
       "srpErrCntIntInterfaceSide": srpErrCntIntInterfaceSide,
       "srpErrCntIntNumber": srpErrCntIntNumber,
       "srpErrCntIntRingRxTtlExpPkts": srpErrCntIntRingRxTtlExpPkts,
       "srpErrCntIntRingRxShortPkts": srpErrCntIntRingRxShortPkts,
       "srpErrCntIntRingRxGiantPkts": srpErrCntIntRingRxGiantPkts,
       "srpErrCntIntRingRxAbortPkts": srpErrCntIntRingRxAbortPkts,
       "srpErrCntIntRingRxCRC": srpErrCntIntRingRxCRC,
       "srpErrCntIntHostRxDiscardPkts": srpErrCntIntHostRxDiscardPkts,
       "srpErrCntIntHostRxShortPkts": srpErrCntIntHostRxShortPkts,
       "srpErrCntIntHostRxGiantPkts": srpErrCntIntHostRxGiantPkts,
       "srpTrapsNotificationsPrefix": srpTrapsNotificationsPrefix,
       "srpTrapsNotifications": srpTrapsNotifications,
       "srpTrapRingWrapped": srpTrapRingWrapped,
       "srpTrapRingRestored": srpTrapRingRestored,
       "srpConformance": srpConformance,
       "srpGroups": srpGroups,
       "srpIfGroup": srpIfGroup,
       "srpMACSideGroup": srpMACSideGroup,
       "srpRingTopologyMapGroup": srpRingTopologyMapGroup,
       "srpMACCountersGroup": srpMACCountersGroup,
       "srpRingCountersCurrentGroup": srpRingCountersCurrentGroup,
       "srpRingCountersIntervalGroup": srpRingCountersIntervalGroup,
       "srpHostCountersCurrentGroup": srpHostCountersCurrentGroup,
       "srpHostCountersIntervalGroup": srpHostCountersIntervalGroup,
       "srpErrorsCountersCurrentGroup": srpErrorsCountersCurrentGroup,
       "srpErrorsCountersIntervalGroup": srpErrorsCountersIntervalGroup,
       "srpErrCntCurrGroup": srpErrCntCurrGroup,
       "srpErrCntIntGroup": srpErrCntIntGroup,
       "srpNotificationsGroup": srpNotificationsGroup,
       "srpCompliances": srpCompliances,
       "srpCompliance": srpCompliance,
       "srpComplianceOld": srpComplianceOld}
)
