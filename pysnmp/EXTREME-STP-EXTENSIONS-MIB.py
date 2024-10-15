# SNMP MIB module (EXTREME-STP-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(BridgeId,
 Timeout,
 dot1dStpPort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dStpPort")

(PortList,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "PortList",
    "extremeAgent")

(extremeVlanIfIndex,) = mibBuilder.importSymbols(
    "EXTREME-VLAN-MIB",
    "extremeVlanIfIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeStp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeStpDomainTable_Object = MibTable
extremeStpDomainTable = _ExtremeStpDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1)
)
if mibBuilder.loadTexts:
    extremeStpDomainTable.setStatus("current")
_ExtremeStpDomainEntry_Object = MibTableRow
extremeStpDomainEntry = _ExtremeStpDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1)
)
extremeStpDomainEntry.setIndexNames(
    (0, "EXTREME-STP-EXTENSIONS-MIB", "extremeStpDomainStpdInstance"),
)
if mibBuilder.loadTexts:
    extremeStpDomainEntry.setStatus("current")
_ExtremeStpDomainStpdInstance_Type = Integer32
_ExtremeStpDomainStpdInstance_Object = MibTableColumn
extremeStpDomainStpdInstance = _ExtremeStpDomainStpdInstance_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 1),
    _ExtremeStpDomainStpdInstance_Type()
)
extremeStpDomainStpdInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeStpDomainStpdInstance.setStatus("current")


class _ExtremeStpDomainStpdName_Type(DisplayString):
    """Custom type extremeStpDomainStpdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtremeStpDomainStpdName_Type.__name__ = "DisplayString"
_ExtremeStpDomainStpdName_Object = MibTableColumn
extremeStpDomainStpdName = _ExtremeStpDomainStpdName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 2),
    _ExtremeStpDomainStpdName_Type()
)
extremeStpDomainStpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainStpdName.setStatus("current")
_ExtremeStpDomainStpEnabled_Type = TruthValue
_ExtremeStpDomainStpEnabled_Object = MibTableColumn
extremeStpDomainStpEnabled = _ExtremeStpDomainStpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 3),
    _ExtremeStpDomainStpEnabled_Type()
)
extremeStpDomainStpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainStpEnabled.setStatus("current")
_ExtremeStpDomainRstpEnabled_Type = TruthValue
_ExtremeStpDomainRstpEnabled_Object = MibTableColumn
extremeStpDomainRstpEnabled = _ExtremeStpDomainRstpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 4),
    _ExtremeStpDomainRstpEnabled_Type()
)
extremeStpDomainRstpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainRstpEnabled.setStatus("current")


class _ExtremeStpDomainStpdTag_Type(Integer32):
    """Custom type extremeStpDomainStpdTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ExtremeStpDomainStpdTag_Type.__name__ = "Integer32"
_ExtremeStpDomainStpdTag_Object = MibTableColumn
extremeStpDomainStpdTag = _ExtremeStpDomainStpdTag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 5),
    _ExtremeStpDomainStpdTag_Type()
)
extremeStpDomainStpdTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainStpdTag.setStatus("current")
_ExtremeStpDomainNumPorts_Type = Integer32
_ExtremeStpDomainNumPorts_Object = MibTableColumn
extremeStpDomainNumPorts = _ExtremeStpDomainNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 6),
    _ExtremeStpDomainNumPorts_Type()
)
extremeStpDomainNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainNumPorts.setStatus("current")
_ExtremeStpDomainBridgeId_Type = BridgeId
_ExtremeStpDomainBridgeId_Object = MibTableColumn
extremeStpDomainBridgeId = _ExtremeStpDomainBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 7),
    _ExtremeStpDomainBridgeId_Type()
)
extremeStpDomainBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainBridgeId.setStatus("current")


class _ExtremeStpDomainBridgePriority_Type(Integer32):
    """Custom type extremeStpDomainBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeStpDomainBridgePriority_Type.__name__ = "Integer32"
_ExtremeStpDomainBridgePriority_Object = MibTableColumn
extremeStpDomainBridgePriority = _ExtremeStpDomainBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 8),
    _ExtremeStpDomainBridgePriority_Type()
)
extremeStpDomainBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainBridgePriority.setStatus("current")
_ExtremeStpDomainDesignatedRoot_Type = BridgeId
_ExtremeStpDomainDesignatedRoot_Object = MibTableColumn
extremeStpDomainDesignatedRoot = _ExtremeStpDomainDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 9),
    _ExtremeStpDomainDesignatedRoot_Type()
)
extremeStpDomainDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainDesignatedRoot.setStatus("current")
_ExtremeStpDomainRootPortIfIndex_Type = Integer32
_ExtremeStpDomainRootPortIfIndex_Object = MibTableColumn
extremeStpDomainRootPortIfIndex = _ExtremeStpDomainRootPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 10),
    _ExtremeStpDomainRootPortIfIndex_Type()
)
extremeStpDomainRootPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainRootPortIfIndex.setStatus("current")
_ExtremeStpDomainRootCost_Type = Integer32
_ExtremeStpDomainRootCost_Object = MibTableColumn
extremeStpDomainRootCost = _ExtremeStpDomainRootCost_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 11),
    _ExtremeStpDomainRootCost_Type()
)
extremeStpDomainRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainRootCost.setStatus("current")
_ExtremeStpDomainRRFailoverEnabled_Type = TruthValue
_ExtremeStpDomainRRFailoverEnabled_Object = MibTableColumn
extremeStpDomainRRFailoverEnabled = _ExtremeStpDomainRRFailoverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 12),
    _ExtremeStpDomainRRFailoverEnabled_Type()
)
extremeStpDomainRRFailoverEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainRRFailoverEnabled.setStatus("current")
_ExtremeStpDomainMaxAge_Type = Timeout
_ExtremeStpDomainMaxAge_Object = MibTableColumn
extremeStpDomainMaxAge = _ExtremeStpDomainMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 13),
    _ExtremeStpDomainMaxAge_Type()
)
extremeStpDomainMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainMaxAge.setStatus("current")
_ExtremeStpDomainHelloTime_Type = Timeout
_ExtremeStpDomainHelloTime_Object = MibTableColumn
extremeStpDomainHelloTime = _ExtremeStpDomainHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 14),
    _ExtremeStpDomainHelloTime_Type()
)
extremeStpDomainHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainHelloTime.setStatus("current")
_ExtremeStpDomainForwardDelay_Type = Timeout
_ExtremeStpDomainForwardDelay_Object = MibTableColumn
extremeStpDomainForwardDelay = _ExtremeStpDomainForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 15),
    _ExtremeStpDomainForwardDelay_Type()
)
extremeStpDomainForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainForwardDelay.setStatus("current")


class _ExtremeStpDomainBridgeMaxAge_Type(Timeout):
    """Custom type extremeStpDomainBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_ExtremeStpDomainBridgeMaxAge_Type.__name__ = "Timeout"
_ExtremeStpDomainBridgeMaxAge_Object = MibTableColumn
extremeStpDomainBridgeMaxAge = _ExtremeStpDomainBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 16),
    _ExtremeStpDomainBridgeMaxAge_Type()
)
extremeStpDomainBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainBridgeMaxAge.setStatus("current")


class _ExtremeStpDomainBridgeHelloTime_Type(Timeout):
    """Custom type extremeStpDomainBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_ExtremeStpDomainBridgeHelloTime_Type.__name__ = "Timeout"
_ExtremeStpDomainBridgeHelloTime_Object = MibTableColumn
extremeStpDomainBridgeHelloTime = _ExtremeStpDomainBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 17),
    _ExtremeStpDomainBridgeHelloTime_Type()
)
extremeStpDomainBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainBridgeHelloTime.setStatus("current")


class _ExtremeStpDomainBridgeForwardDelay_Type(Timeout):
    """Custom type extremeStpDomainBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_ExtremeStpDomainBridgeForwardDelay_Type.__name__ = "Timeout"
_ExtremeStpDomainBridgeForwardDelay_Object = MibTableColumn
extremeStpDomainBridgeForwardDelay = _ExtremeStpDomainBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 18),
    _ExtremeStpDomainBridgeForwardDelay_Type()
)
extremeStpDomainBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainBridgeForwardDelay.setStatus("current")
_ExtremeStpDomainHoldTime_Type = Timeout
_ExtremeStpDomainHoldTime_Object = MibTableColumn
extremeStpDomainHoldTime = _ExtremeStpDomainHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 19),
    _ExtremeStpDomainHoldTime_Type()
)
extremeStpDomainHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainHoldTime.setStatus("current")
_ExtremeStpDomainTopChanges_Type = Counter32
_ExtremeStpDomainTopChanges_Object = MibTableColumn
extremeStpDomainTopChanges = _ExtremeStpDomainTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 20),
    _ExtremeStpDomainTopChanges_Type()
)
extremeStpDomainTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainTopChanges.setStatus("current")
_ExtremeStpDomainTimeSinceTopologyChange_Type = TimeTicks
_ExtremeStpDomainTimeSinceTopologyChange_Object = MibTableColumn
extremeStpDomainTimeSinceTopologyChange = _ExtremeStpDomainTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 21),
    _ExtremeStpDomainTimeSinceTopologyChange_Type()
)
extremeStpDomainTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainTimeSinceTopologyChange.setStatus("current")
_ExtremeStpDomainRowStatus_Type = RowStatus
_ExtremeStpDomainRowStatus_Object = MibTableColumn
extremeStpDomainRowStatus = _ExtremeStpDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 1, 1, 22),
    _ExtremeStpDomainRowStatus_Type()
)
extremeStpDomainRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpDomainRowStatus.setStatus("current")
_ExtremeStpPortTable_Object = MibTable
extremeStpPortTable = _ExtremeStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2)
)
if mibBuilder.loadTexts:
    extremeStpPortTable.setStatus("current")
_ExtremeStpPortEntry_Object = MibTableRow
extremeStpPortEntry = _ExtremeStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1)
)
extremeStpPortEntry.setIndexNames(
    (0, "EXTREME-STP-EXTENSIONS-MIB", "extremeStpDomainStpdInstance"),
    (0, "EXTREME-STP-EXTENSIONS-MIB", "extremeStpPortPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeStpPortEntry.setStatus("current")
_ExtremeStpPortPortIfIndex_Type = Integer32
_ExtremeStpPortPortIfIndex_Object = MibTableColumn
extremeStpPortPortIfIndex = _ExtremeStpPortPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 1),
    _ExtremeStpPortPortIfIndex_Type()
)
extremeStpPortPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeStpPortPortIfIndex.setStatus("current")
_ExtremeStpPortStpEnabled_Type = TruthValue
_ExtremeStpPortStpEnabled_Object = MibTableColumn
extremeStpPortStpEnabled = _ExtremeStpPortStpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 2),
    _ExtremeStpPortStpEnabled_Type()
)
extremeStpPortStpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpPortStpEnabled.setStatus("current")


class _ExtremeStpPortPortMode_Type(Integer32):
    """Custom type extremeStpPortPortMode based on Integer32"""
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
        *(("dot1d", 1),
          ("dot1w", 4),
          ("emistp", 2),
          ("pvstp", 3))
    )


_ExtremeStpPortPortMode_Type.__name__ = "Integer32"
_ExtremeStpPortPortMode_Object = MibTableColumn
extremeStpPortPortMode = _ExtremeStpPortPortMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 3),
    _ExtremeStpPortPortMode_Type()
)
extremeStpPortPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpPortPortMode.setStatus("current")


class _ExtremeStpPortPortState_Type(Integer32):
    """Custom type extremeStpPortPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_ExtremeStpPortPortState_Type.__name__ = "Integer32"
_ExtremeStpPortPortState_Object = MibTableColumn
extremeStpPortPortState = _ExtremeStpPortPortState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 4),
    _ExtremeStpPortPortState_Type()
)
extremeStpPortPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpPortPortState.setStatus("current")


class _ExtremeStpPortPortPriority_Type(Integer32):
    """Custom type extremeStpPortPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ExtremeStpPortPortPriority_Type.__name__ = "Integer32"
_ExtremeStpPortPortPriority_Object = MibTableColumn
extremeStpPortPortPriority = _ExtremeStpPortPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 5),
    _ExtremeStpPortPortPriority_Type()
)
extremeStpPortPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpPortPortPriority.setStatus("current")


class _ExtremeStpPortPortId_Type(OctetString):
    """Custom type extremeStpPortPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ExtremeStpPortPortId_Type.__name__ = "OctetString"
_ExtremeStpPortPortId_Object = MibTableColumn
extremeStpPortPortId = _ExtremeStpPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 6),
    _ExtremeStpPortPortId_Type()
)
extremeStpPortPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpPortPortId.setStatus("current")


class _ExtremeStpPortPathCost_Type(Integer32):
    """Custom type extremeStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeStpPortPathCost_Type.__name__ = "Integer32"
_ExtremeStpPortPathCost_Object = MibTableColumn
extremeStpPortPathCost = _ExtremeStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 7),
    _ExtremeStpPortPathCost_Type()
)
extremeStpPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpPortPathCost.setStatus("current")
_ExtremeStpPortDesignatedCost_Type = Integer32
_ExtremeStpPortDesignatedCost_Object = MibTableColumn
extremeStpPortDesignatedCost = _ExtremeStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 8),
    _ExtremeStpPortDesignatedCost_Type()
)
extremeStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpPortDesignatedCost.setStatus("current")
_ExtremeStpPortDesignatedRoot_Type = BridgeId
_ExtremeStpPortDesignatedRoot_Object = MibTableColumn
extremeStpPortDesignatedRoot = _ExtremeStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 9),
    _ExtremeStpPortDesignatedRoot_Type()
)
extremeStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpPortDesignatedRoot.setStatus("current")
_ExtremeStpPortDesignatedBridge_Type = BridgeId
_ExtremeStpPortDesignatedBridge_Object = MibTableColumn
extremeStpPortDesignatedBridge = _ExtremeStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 10),
    _ExtremeStpPortDesignatedBridge_Type()
)
extremeStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpPortDesignatedBridge.setStatus("current")


class _ExtremeStpPortDesignatedPort_Type(OctetString):
    """Custom type extremeStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ExtremeStpPortDesignatedPort_Type.__name__ = "OctetString"
_ExtremeStpPortDesignatedPort_Object = MibTableColumn
extremeStpPortDesignatedPort = _ExtremeStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 11),
    _ExtremeStpPortDesignatedPort_Type()
)
extremeStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpPortDesignatedPort.setStatus("current")
_ExtremeStpPortRowStatus_Type = RowStatus
_ExtremeStpPortRowStatus_Object = MibTableColumn
extremeStpPortRowStatus = _ExtremeStpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 2, 1, 12),
    _ExtremeStpPortRowStatus_Type()
)
extremeStpPortRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpPortRowStatus.setStatus("current")
_ExtremeStpVlanPortTable_Object = MibTable
extremeStpVlanPortTable = _ExtremeStpVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 3)
)
if mibBuilder.loadTexts:
    extremeStpVlanPortTable.setStatus("current")
_ExtremeStpVlanPortEntry_Object = MibTableRow
extremeStpVlanPortEntry = _ExtremeStpVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 3, 1)
)
extremeStpVlanPortEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
    (0, "EXTREME-STP-EXTENSIONS-MIB", "extremeStpDomainStpdInstance"),
)
if mibBuilder.loadTexts:
    extremeStpVlanPortEntry.setStatus("current")
_ExtremeStpVlanPortPortMask_Type = PortList
_ExtremeStpVlanPortPortMask_Object = MibTableColumn
extremeStpVlanPortPortMask = _ExtremeStpVlanPortPortMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 3, 1, 1),
    _ExtremeStpVlanPortPortMask_Type()
)
extremeStpVlanPortPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpVlanPortPortMask.setStatus("current")
_ExtremeStpVlanPortRowStatus_Type = RowStatus
_ExtremeStpVlanPortRowStatus_Object = MibTableColumn
extremeStpVlanPortRowStatus = _ExtremeStpVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 3, 1, 2),
    _ExtremeStpVlanPortRowStatus_Type()
)
extremeStpVlanPortRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeStpVlanPortRowStatus.setStatus("current")
_ExtremeStpTraps_ObjectIdentity = ObjectIdentity
extremeStpTraps = _ExtremeStpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 4)
)
_ExtremeStpTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeStpTrapsPrefix = _ExtremeStpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 4, 0)
)

# Managed Objects groups


# Notification objects

extremeStpEdgePortBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17, 4, 0, 1)
)
extremeStpEdgePortBlocked.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    extremeStpEdgePortBlocked.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-STP-EXTENSIONS-MIB",
    **{"extremeStp": extremeStp,
       "extremeStpDomainTable": extremeStpDomainTable,
       "extremeStpDomainEntry": extremeStpDomainEntry,
       "extremeStpDomainStpdInstance": extremeStpDomainStpdInstance,
       "extremeStpDomainStpdName": extremeStpDomainStpdName,
       "extremeStpDomainStpEnabled": extremeStpDomainStpEnabled,
       "extremeStpDomainRstpEnabled": extremeStpDomainRstpEnabled,
       "extremeStpDomainStpdTag": extremeStpDomainStpdTag,
       "extremeStpDomainNumPorts": extremeStpDomainNumPorts,
       "extremeStpDomainBridgeId": extremeStpDomainBridgeId,
       "extremeStpDomainBridgePriority": extremeStpDomainBridgePriority,
       "extremeStpDomainDesignatedRoot": extremeStpDomainDesignatedRoot,
       "extremeStpDomainRootPortIfIndex": extremeStpDomainRootPortIfIndex,
       "extremeStpDomainRootCost": extremeStpDomainRootCost,
       "extremeStpDomainRRFailoverEnabled": extremeStpDomainRRFailoverEnabled,
       "extremeStpDomainMaxAge": extremeStpDomainMaxAge,
       "extremeStpDomainHelloTime": extremeStpDomainHelloTime,
       "extremeStpDomainForwardDelay": extremeStpDomainForwardDelay,
       "extremeStpDomainBridgeMaxAge": extremeStpDomainBridgeMaxAge,
       "extremeStpDomainBridgeHelloTime": extremeStpDomainBridgeHelloTime,
       "extremeStpDomainBridgeForwardDelay": extremeStpDomainBridgeForwardDelay,
       "extremeStpDomainHoldTime": extremeStpDomainHoldTime,
       "extremeStpDomainTopChanges": extremeStpDomainTopChanges,
       "extremeStpDomainTimeSinceTopologyChange": extremeStpDomainTimeSinceTopologyChange,
       "extremeStpDomainRowStatus": extremeStpDomainRowStatus,
       "extremeStpPortTable": extremeStpPortTable,
       "extremeStpPortEntry": extremeStpPortEntry,
       "extremeStpPortPortIfIndex": extremeStpPortPortIfIndex,
       "extremeStpPortStpEnabled": extremeStpPortStpEnabled,
       "extremeStpPortPortMode": extremeStpPortPortMode,
       "extremeStpPortPortState": extremeStpPortPortState,
       "extremeStpPortPortPriority": extremeStpPortPortPriority,
       "extremeStpPortPortId": extremeStpPortPortId,
       "extremeStpPortPathCost": extremeStpPortPathCost,
       "extremeStpPortDesignatedCost": extremeStpPortDesignatedCost,
       "extremeStpPortDesignatedRoot": extremeStpPortDesignatedRoot,
       "extremeStpPortDesignatedBridge": extremeStpPortDesignatedBridge,
       "extremeStpPortDesignatedPort": extremeStpPortDesignatedPort,
       "extremeStpPortRowStatus": extremeStpPortRowStatus,
       "extremeStpVlanPortTable": extremeStpVlanPortTable,
       "extremeStpVlanPortEntry": extremeStpVlanPortEntry,
       "extremeStpVlanPortPortMask": extremeStpVlanPortPortMask,
       "extremeStpVlanPortRowStatus": extremeStpVlanPortRowStatus,
       "extremeStpTraps": extremeStpTraps,
       "extremeStpTrapsPrefix": extremeStpTrapsPrefix,
       "extremeStpEdgePortBlocked": extremeStpEdgePortBlocked}
)
