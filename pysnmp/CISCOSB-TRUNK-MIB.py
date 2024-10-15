# SNMP MIB module (CISCOSB-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:05 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(dot3adAggIndex,
 dot3adAggPortIndex) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "dot3adAggIndex",
    "dot3adAggPortIndex")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlDot3adAgg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65)
)
rlDot3adAgg.setRevisions(
        ("2006-12-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDot3adAggMibVersion_Type = Integer32
_RlDot3adAggMibVersion_Object = MibScalar
rlDot3adAggMibVersion = _RlDot3adAggMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 1),
    _RlDot3adAggMibVersion_Type()
)
rlDot3adAggMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggMibVersion.setStatus("current")
_RlDot3adAggBalanceTable_Object = MibTable
rlDot3adAggBalanceTable = _RlDot3adAggBalanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2)
)
if mibBuilder.loadTexts:
    rlDot3adAggBalanceTable.setStatus("current")
_RlDot3adAggBalanceEntry_Object = MibTableRow
rlDot3adAggBalanceEntry = _RlDot3adAggBalanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1)
)
rlDot3adAggBalanceEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggIndex"),
    (0, "CISCOSB-TRUNK-MIB", "rlDot3adAggBalanceForwardType"),
)
if mibBuilder.loadTexts:
    rlDot3adAggBalanceEntry.setStatus("current")


class _RlDot3adAggBalanceForwardType_Type(Integer32):
    """Custom type rlDot3adAggBalanceForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 1),
          ("routing", 2))
    )


_RlDot3adAggBalanceForwardType_Type.__name__ = "Integer32"
_RlDot3adAggBalanceForwardType_Object = MibTableColumn
rlDot3adAggBalanceForwardType = _RlDot3adAggBalanceForwardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 1),
    _RlDot3adAggBalanceForwardType_Type()
)
rlDot3adAggBalanceForwardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggBalanceForwardType.setStatus("current")
_RlDot3adAggBalanceLayer_Type = Integer32
_RlDot3adAggBalanceLayer_Object = MibTableColumn
rlDot3adAggBalanceLayer = _RlDot3adAggBalanceLayer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 2),
    _RlDot3adAggBalanceLayer_Type()
)
rlDot3adAggBalanceLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggBalanceLayer.setStatus("current")


class _RlDot3adAggBalanceUsedAddresses_Type(Integer32):
    """Custom type rlDot3adAggBalanceUsedAddresses based on Integer32"""
    defaultValue = 1

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
        *(("dstAddr", 1),
          ("dstAndSrcAddr", 3),
          ("ethType", 5),
          ("notApplied", 0),
          ("srcAddr", 2),
          ("vlanId", 4))
    )


_RlDot3adAggBalanceUsedAddresses_Type.__name__ = "Integer32"
_RlDot3adAggBalanceUsedAddresses_Object = MibTableColumn
rlDot3adAggBalanceUsedAddresses = _RlDot3adAggBalanceUsedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 3),
    _RlDot3adAggBalanceUsedAddresses_Type()
)
rlDot3adAggBalanceUsedAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggBalanceUsedAddresses.setStatus("current")


class _RlDot3adAggBalanceBroadcastType_Type(Integer32):
    """Custom type rlDot3adAggBalanceBroadcastType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("common", 0),
          ("dedicated", 1))
    )


_RlDot3adAggBalanceBroadcastType_Type.__name__ = "Integer32"
_RlDot3adAggBalanceBroadcastType_Object = MibTableColumn
rlDot3adAggBalanceBroadcastType = _RlDot3adAggBalanceBroadcastType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 4),
    _RlDot3adAggBalanceBroadcastType_Type()
)
rlDot3adAggBalanceBroadcastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggBalanceBroadcastType.setStatus("current")
_RlDot3adAggNumOfTrunks_Type = Integer32
_RlDot3adAggNumOfTrunks_Object = MibScalar
rlDot3adAggNumOfTrunks = _RlDot3adAggNumOfTrunks_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 3),
    _RlDot3adAggNumOfTrunks_Type()
)
rlDot3adAggNumOfTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggNumOfTrunks.setStatus("current")
_RlDot3adAggMaxPortsInTrunks_Type = Integer32
_RlDot3adAggMaxPortsInTrunks_Object = MibScalar
rlDot3adAggMaxPortsInTrunks = _RlDot3adAggMaxPortsInTrunks_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 4),
    _RlDot3adAggMaxPortsInTrunks_Type()
)
rlDot3adAggMaxPortsInTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggMaxPortsInTrunks.setStatus("current")


class _RlDot3adAggTrunkCreationSupport_Type(Integer32):
    """Custom type rlDot3adAggTrunkCreationSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("supportsTrunkOrLacp", 1))
    )


_RlDot3adAggTrunkCreationSupport_Type.__name__ = "Integer32"
_RlDot3adAggTrunkCreationSupport_Object = MibScalar
rlDot3adAggTrunkCreationSupport = _RlDot3adAggTrunkCreationSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 5),
    _RlDot3adAggTrunkCreationSupport_Type()
)
rlDot3adAggTrunkCreationSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggTrunkCreationSupport.setStatus("current")
_RlDot3adAggCreationTable_Object = MibTable
rlDot3adAggCreationTable = _RlDot3adAggCreationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6)
)
if mibBuilder.loadTexts:
    rlDot3adAggCreationTable.setStatus("current")
_RlDot3adAggCreationEntry_Object = MibTableRow
rlDot3adAggCreationEntry = _RlDot3adAggCreationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6, 1)
)
rlDot3adAggCreationEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggIndex"),
)
if mibBuilder.loadTexts:
    rlDot3adAggCreationEntry.setStatus("current")
_RlDot3adAggCreationTrunk_Type = TruthValue
_RlDot3adAggCreationTrunk_Object = MibTableColumn
rlDot3adAggCreationTrunk = _RlDot3adAggCreationTrunk_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6, 1, 1),
    _RlDot3adAggCreationTrunk_Type()
)
rlDot3adAggCreationTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggCreationTrunk.setStatus("current")
_RlDot3adAggCreationLacp_Type = TruthValue
_RlDot3adAggCreationLacp_Object = MibTableColumn
rlDot3adAggCreationLacp = _RlDot3adAggCreationLacp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6, 1, 2),
    _RlDot3adAggCreationLacp_Type()
)
rlDot3adAggCreationLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggCreationLacp.setStatus("current")
_RlDot3adAggLoadBalancingPerTrunk_Type = TruthValue
_RlDot3adAggLoadBalancingPerTrunk_Object = MibScalar
rlDot3adAggLoadBalancingPerTrunk = _RlDot3adAggLoadBalancingPerTrunk_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 7),
    _RlDot3adAggLoadBalancingPerTrunk_Type()
)
rlDot3adAggLoadBalancingPerTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggLoadBalancingPerTrunk.setStatus("current")
_RlDot3adAggPortLacpTable_Object = MibTable
rlDot3adAggPortLacpTable = _RlDot3adAggPortLacpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8)
)
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpTable.setStatus("current")
_RlDot3adAggPortLacpEntry_Object = MibTableRow
rlDot3adAggPortLacpEntry = _RlDot3adAggPortLacpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1)
)
rlDot3adAggPortLacpEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggPortIndex"),
)
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpEntry.setStatus("current")
_RlDot3adAggPortLacpPdusRx_Type = Counter32
_RlDot3adAggPortLacpPdusRx_Object = MibTableColumn
rlDot3adAggPortLacpPdusRx = _RlDot3adAggPortLacpPdusRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 1),
    _RlDot3adAggPortLacpPdusRx_Type()
)
rlDot3adAggPortLacpPdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpPdusRx.setStatus("current")
_RlDot3adAggPortLacpPDUsTx_Type = Counter32
_RlDot3adAggPortLacpPDUsTx_Object = MibTableColumn
rlDot3adAggPortLacpPDUsTx = _RlDot3adAggPortLacpPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 2),
    _RlDot3adAggPortLacpPDUsTx_Type()
)
rlDot3adAggPortLacpPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpPDUsTx.setStatus("current")


class _RlDot3adAggPortLacpRxState_Type(Integer32):
    """Custom type rlDot3adAggPortLacpRxState based on Integer32"""
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
        *(("current", 1),
          ("defaulted", 3),
          ("expired", 2),
          ("initialize", 4),
          ("lacpDisabled", 6),
          ("portDisabled", 5))
    )


_RlDot3adAggPortLacpRxState_Type.__name__ = "Integer32"
_RlDot3adAggPortLacpRxState_Object = MibTableColumn
rlDot3adAggPortLacpRxState = _RlDot3adAggPortLacpRxState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 3),
    _RlDot3adAggPortLacpRxState_Type()
)
rlDot3adAggPortLacpRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpRxState.setStatus("current")


class _RlDot3adAggPortLacpMuxState_Type(Integer32):
    """Custom type rlDot3adAggPortLacpMuxState based on Integer32"""
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
        *(("attached", 3),
          ("collecting", 4),
          ("collectingDistributing", 6),
          ("detached", 1),
          ("distributing", 5),
          ("waiting", 2))
    )


_RlDot3adAggPortLacpMuxState_Type.__name__ = "Integer32"
_RlDot3adAggPortLacpMuxState_Object = MibTableColumn
rlDot3adAggPortLacpMuxState = _RlDot3adAggPortLacpMuxState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 4),
    _RlDot3adAggPortLacpMuxState_Type()
)
rlDot3adAggPortLacpMuxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpMuxState.setStatus("current")


class _RlDot3adAggPortLacpPeriodicState_Type(Integer32):
    """Custom type rlDot3adAggPortLacpPeriodicState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fastPeriodic", 2),
          ("noPeriodic", 1),
          ("periodicTx", 4),
          ("slowPeriodic", 3))
    )


_RlDot3adAggPortLacpPeriodicState_Type.__name__ = "Integer32"
_RlDot3adAggPortLacpPeriodicState_Object = MibTableColumn
rlDot3adAggPortLacpPeriodicState = _RlDot3adAggPortLacpPeriodicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 5),
    _RlDot3adAggPortLacpPeriodicState_Type()
)
rlDot3adAggPortLacpPeriodicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpPeriodicState.setStatus("current")


class _RlDot3adAggPortLacpSelected_Type(Integer32):
    """Custom type rlDot3adAggPortLacpSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("selected", 2),
          ("unselected", 1),
          ("waiting", 3))
    )


_RlDot3adAggPortLacpSelected_Type.__name__ = "Integer32"
_RlDot3adAggPortLacpSelected_Object = MibTableColumn
rlDot3adAggPortLacpSelected = _RlDot3adAggPortLacpSelected_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 6),
    _RlDot3adAggPortLacpSelected_Type()
)
rlDot3adAggPortLacpSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpSelected.setStatus("current")
_RlDot3adAggPortLacpReady_Type = TruthValue
_RlDot3adAggPortLacpReady_Object = MibTableColumn
rlDot3adAggPortLacpReady = _RlDot3adAggPortLacpReady_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 7),
    _RlDot3adAggPortLacpReady_Type()
)
rlDot3adAggPortLacpReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpReady.setStatus("current")
_RlDot3adAggPortLacpPortMoved_Type = TruthValue
_RlDot3adAggPortLacpPortMoved_Object = MibTableColumn
rlDot3adAggPortLacpPortMoved = _RlDot3adAggPortLacpPortMoved_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 8),
    _RlDot3adAggPortLacpPortMoved_Type()
)
rlDot3adAggPortLacpPortMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpPortMoved.setStatus("current")
_RlDot3adAggPortLacpNNT_Type = TruthValue
_RlDot3adAggPortLacpNNT_Object = MibTableColumn
rlDot3adAggPortLacpNNT = _RlDot3adAggPortLacpNNT_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 9),
    _RlDot3adAggPortLacpNNT_Type()
)
rlDot3adAggPortLacpNNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpNNT.setStatus("current")
_RlDot3adAggPortLacpPeriodicTxTimer_Type = Integer32
_RlDot3adAggPortLacpPeriodicTxTimer_Object = MibTableColumn
rlDot3adAggPortLacpPeriodicTxTimer = _RlDot3adAggPortLacpPeriodicTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 10),
    _RlDot3adAggPortLacpPeriodicTxTimer_Type()
)
rlDot3adAggPortLacpPeriodicTxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpPeriodicTxTimer.setStatus("current")
_RlDot3adAggPortLacpCurrentWhileTimer_Type = Integer32
_RlDot3adAggPortLacpCurrentWhileTimer_Object = MibTableColumn
rlDot3adAggPortLacpCurrentWhileTimer = _RlDot3adAggPortLacpCurrentWhileTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 11),
    _RlDot3adAggPortLacpCurrentWhileTimer_Type()
)
rlDot3adAggPortLacpCurrentWhileTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpCurrentWhileTimer.setStatus("current")
_RlDot3adAggPortLacpWaitWhileTimer_Type = Integer32
_RlDot3adAggPortLacpWaitWhileTimer_Object = MibTableColumn
rlDot3adAggPortLacpWaitWhileTimer = _RlDot3adAggPortLacpWaitWhileTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 12),
    _RlDot3adAggPortLacpWaitWhileTimer_Type()
)
rlDot3adAggPortLacpWaitWhileTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot3adAggPortLacpWaitWhileTimer.setStatus("current")
_RlDot3adAggLacpMembershipRestrictionsSupport_Type = TruthValue
_RlDot3adAggLacpMembershipRestrictionsSupport_Object = MibScalar
rlDot3adAggLacpMembershipRestrictionsSupport = _RlDot3adAggLacpMembershipRestrictionsSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 9),
    _RlDot3adAggLacpMembershipRestrictionsSupport_Type()
)
rlDot3adAggLacpMembershipRestrictionsSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggLacpMembershipRestrictionsSupport.setStatus("current")
_RlDot3adAggLacpMembershipRestrictionsTable_Object = MibTable
rlDot3adAggLacpMembershipRestrictionsTable = _RlDot3adAggLacpMembershipRestrictionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10)
)
if mibBuilder.loadTexts:
    rlDot3adAggLacpMembershipRestrictionsTable.setStatus("current")
_RlDot3adAggLacpMembershipRestrictionsEntry_Object = MibTableRow
rlDot3adAggLacpMembershipRestrictionsEntry = _RlDot3adAggLacpMembershipRestrictionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1)
)
rlDot3adAggLacpMembershipRestrictionsEntry.setIndexNames(
    (0, "IEEE8023-LAG-MIB", "dot3adAggIndex"),
)
if mibBuilder.loadTexts:
    rlDot3adAggLacpMembershipRestrictionsEntry.setStatus("current")


class _RlDot3adAggLacpMembershipRestrictionsPartnerAdminKey_Type(Unsigned32):
    """Custom type rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlDot3adAggLacpMembershipRestrictionsPartnerAdminKey_Type.__name__ = "Unsigned32"
_RlDot3adAggLacpMembershipRestrictionsPartnerAdminKey_Object = MibTableColumn
rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey = _RlDot3adAggLacpMembershipRestrictionsPartnerAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 1),
    _RlDot3adAggLacpMembershipRestrictionsPartnerAdminKey_Type()
)
rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey.setStatus("current")


class _RlDot3adAggLacpMembershipRestrictionsSpeedAdminMode_Type(Unsigned32):
    """Custom type rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode based on Unsigned32"""
    defaultValue = 0


_RlDot3adAggLacpMembershipRestrictionsSpeedAdminMode_Object = MibTableColumn
rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode = _RlDot3adAggLacpMembershipRestrictionsSpeedAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 2),
    _RlDot3adAggLacpMembershipRestrictionsSpeedAdminMode_Type()
)
rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode.setStatus("current")
_RlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId_Type = PhysAddress
_RlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId_Object = MibTableColumn
rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId = _RlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 3),
    _RlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId_Type()
)
rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId.setStatus("current")


class _RlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority_Type(Unsigned32):
    """Custom type rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority_Type.__name__ = "Unsigned32"
_RlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority_Object = MibTableColumn
rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority = _RlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 4),
    _RlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority_Type()
)
rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority.setStatus("current")


class _RlDot3adAggLacpMembershipRestrictionsIndividualAggregator_Type(TruthValue):
    """Custom type rlDot3adAggLacpMembershipRestrictionsIndividualAggregator based on TruthValue"""


_RlDot3adAggLacpMembershipRestrictionsIndividualAggregator_Object = MibTableColumn
rlDot3adAggLacpMembershipRestrictionsIndividualAggregator = _RlDot3adAggLacpMembershipRestrictionsIndividualAggregator_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 5),
    _RlDot3adAggLacpMembershipRestrictionsIndividualAggregator_Type()
)
rlDot3adAggLacpMembershipRestrictionsIndividualAggregator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDot3adAggLacpMembershipRestrictionsIndividualAggregator.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-TRUNK-MIB",
    **{"rlDot3adAgg": rlDot3adAgg,
       "rlDot3adAggMibVersion": rlDot3adAggMibVersion,
       "rlDot3adAggBalanceTable": rlDot3adAggBalanceTable,
       "rlDot3adAggBalanceEntry": rlDot3adAggBalanceEntry,
       "rlDot3adAggBalanceForwardType": rlDot3adAggBalanceForwardType,
       "rlDot3adAggBalanceLayer": rlDot3adAggBalanceLayer,
       "rlDot3adAggBalanceUsedAddresses": rlDot3adAggBalanceUsedAddresses,
       "rlDot3adAggBalanceBroadcastType": rlDot3adAggBalanceBroadcastType,
       "rlDot3adAggNumOfTrunks": rlDot3adAggNumOfTrunks,
       "rlDot3adAggMaxPortsInTrunks": rlDot3adAggMaxPortsInTrunks,
       "rlDot3adAggTrunkCreationSupport": rlDot3adAggTrunkCreationSupport,
       "rlDot3adAggCreationTable": rlDot3adAggCreationTable,
       "rlDot3adAggCreationEntry": rlDot3adAggCreationEntry,
       "rlDot3adAggCreationTrunk": rlDot3adAggCreationTrunk,
       "rlDot3adAggCreationLacp": rlDot3adAggCreationLacp,
       "rlDot3adAggLoadBalancingPerTrunk": rlDot3adAggLoadBalancingPerTrunk,
       "rlDot3adAggPortLacpTable": rlDot3adAggPortLacpTable,
       "rlDot3adAggPortLacpEntry": rlDot3adAggPortLacpEntry,
       "rlDot3adAggPortLacpPdusRx": rlDot3adAggPortLacpPdusRx,
       "rlDot3adAggPortLacpPDUsTx": rlDot3adAggPortLacpPDUsTx,
       "rlDot3adAggPortLacpRxState": rlDot3adAggPortLacpRxState,
       "rlDot3adAggPortLacpMuxState": rlDot3adAggPortLacpMuxState,
       "rlDot3adAggPortLacpPeriodicState": rlDot3adAggPortLacpPeriodicState,
       "rlDot3adAggPortLacpSelected": rlDot3adAggPortLacpSelected,
       "rlDot3adAggPortLacpReady": rlDot3adAggPortLacpReady,
       "rlDot3adAggPortLacpPortMoved": rlDot3adAggPortLacpPortMoved,
       "rlDot3adAggPortLacpNNT": rlDot3adAggPortLacpNNT,
       "rlDot3adAggPortLacpPeriodicTxTimer": rlDot3adAggPortLacpPeriodicTxTimer,
       "rlDot3adAggPortLacpCurrentWhileTimer": rlDot3adAggPortLacpCurrentWhileTimer,
       "rlDot3adAggPortLacpWaitWhileTimer": rlDot3adAggPortLacpWaitWhileTimer,
       "rlDot3adAggLacpMembershipRestrictionsSupport": rlDot3adAggLacpMembershipRestrictionsSupport,
       "rlDot3adAggLacpMembershipRestrictionsTable": rlDot3adAggLacpMembershipRestrictionsTable,
       "rlDot3adAggLacpMembershipRestrictionsEntry": rlDot3adAggLacpMembershipRestrictionsEntry,
       "rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey": rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey,
       "rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode": rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode,
       "rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId": rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId,
       "rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority": rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority,
       "rlDot3adAggLacpMembershipRestrictionsIndividualAggregator": rlDot3adAggLacpMembershipRestrictionsIndividualAggregator}
)
