# SNMP MIB module (IEEE8021-SPANNING-TREE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-SPANNING-TREE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:39 2024
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
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

(IEEE8021BridgePortNumber,
 IEEE8021PbbComponentIdentifier,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021PbbComponentIdentifier",
    "ieee802dot1mibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021SpanningTreeMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 3)
)
ieee8021SpanningTreeMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2011-03-24 00:00",
         "2008-10-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021SpanningTreeNotifications_ObjectIdentity = ObjectIdentity
ieee8021SpanningTreeNotifications = _Ieee8021SpanningTreeNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 3, 0)
)
_Ieee8021SpanningTreeObjects_ObjectIdentity = ObjectIdentity
ieee8021SpanningTreeObjects = _Ieee8021SpanningTreeObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 3, 1)
)
_Ieee8021SpanningTreeTable_Object = MibTable
ieee8021SpanningTreeTable = _Ieee8021SpanningTreeTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreeTable.setStatus("current")
_Ieee8021SpanningTreeEntry_Object = MibTableRow
ieee8021SpanningTreeEntry = _Ieee8021SpanningTreeEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1)
)
ieee8021SpanningTreeEntry.setIndexNames(
    (0, "IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeComponentId"),
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreeEntry.setStatus("current")
_Ieee8021SpanningTreeComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021SpanningTreeComponentId_Object = MibTableColumn
ieee8021SpanningTreeComponentId = _Ieee8021SpanningTreeComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 1),
    _Ieee8021SpanningTreeComponentId_Type()
)
ieee8021SpanningTreeComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeComponentId.setStatus("current")


class _Ieee8021SpanningTreeProtocolSpecification_Type(Integer32):
    """Custom type ieee8021SpanningTreeProtocolSpecification based on Integer32"""
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
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("ieee8021q", 4),
          ("unknown", 1))
    )


_Ieee8021SpanningTreeProtocolSpecification_Type.__name__ = "Integer32"
_Ieee8021SpanningTreeProtocolSpecification_Object = MibTableColumn
ieee8021SpanningTreeProtocolSpecification = _Ieee8021SpanningTreeProtocolSpecification_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 2),
    _Ieee8021SpanningTreeProtocolSpecification_Type()
)
ieee8021SpanningTreeProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeProtocolSpecification.setStatus("current")


class _Ieee8021SpanningTreePriority_Type(Integer32):
    """Custom type ieee8021SpanningTreePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021SpanningTreePriority_Type.__name__ = "Integer32"
_Ieee8021SpanningTreePriority_Object = MibTableColumn
ieee8021SpanningTreePriority = _Ieee8021SpanningTreePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 3),
    _Ieee8021SpanningTreePriority_Type()
)
ieee8021SpanningTreePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePriority.setStatus("current")
_Ieee8021SpanningTreeTimeSinceTopologyChange_Type = TimeTicks
_Ieee8021SpanningTreeTimeSinceTopologyChange_Object = MibTableColumn
ieee8021SpanningTreeTimeSinceTopologyChange = _Ieee8021SpanningTreeTimeSinceTopologyChange_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 4),
    _Ieee8021SpanningTreeTimeSinceTopologyChange_Type()
)
ieee8021SpanningTreeTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeTimeSinceTopologyChange.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeTimeSinceTopologyChange.setUnits("centi-seconds")
_Ieee8021SpanningTreeTopChanges_Type = Counter64
_Ieee8021SpanningTreeTopChanges_Object = MibTableColumn
ieee8021SpanningTreeTopChanges = _Ieee8021SpanningTreeTopChanges_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 5),
    _Ieee8021SpanningTreeTopChanges_Type()
)
ieee8021SpanningTreeTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeTopChanges.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeTopChanges.setUnits("topology changes")
_Ieee8021SpanningTreeDesignatedRoot_Type = BridgeId
_Ieee8021SpanningTreeDesignatedRoot_Object = MibTableColumn
ieee8021SpanningTreeDesignatedRoot = _Ieee8021SpanningTreeDesignatedRoot_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 6),
    _Ieee8021SpanningTreeDesignatedRoot_Type()
)
ieee8021SpanningTreeDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeDesignatedRoot.setStatus("current")
_Ieee8021SpanningTreeRootCost_Type = Integer32
_Ieee8021SpanningTreeRootCost_Object = MibTableColumn
ieee8021SpanningTreeRootCost = _Ieee8021SpanningTreeRootCost_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 7),
    _Ieee8021SpanningTreeRootCost_Type()
)
ieee8021SpanningTreeRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRootCost.setStatus("current")
_Ieee8021SpanningTreeRootPort_Type = IEEE8021BridgePortNumber
_Ieee8021SpanningTreeRootPort_Object = MibTableColumn
ieee8021SpanningTreeRootPort = _Ieee8021SpanningTreeRootPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 8),
    _Ieee8021SpanningTreeRootPort_Type()
)
ieee8021SpanningTreeRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRootPort.setStatus("current")
_Ieee8021SpanningTreeMaxAge_Type = Timeout
_Ieee8021SpanningTreeMaxAge_Object = MibTableColumn
ieee8021SpanningTreeMaxAge = _Ieee8021SpanningTreeMaxAge_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 9),
    _Ieee8021SpanningTreeMaxAge_Type()
)
ieee8021SpanningTreeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeMaxAge.setUnits("centi-seconds")
_Ieee8021SpanningTreeHelloTime_Type = Timeout
_Ieee8021SpanningTreeHelloTime_Object = MibTableColumn
ieee8021SpanningTreeHelloTime = _Ieee8021SpanningTreeHelloTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 10),
    _Ieee8021SpanningTreeHelloTime_Type()
)
ieee8021SpanningTreeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeHelloTime.setUnits("centi-seconds")
_Ieee8021SpanningTreeHoldTime_Type = Integer32
_Ieee8021SpanningTreeHoldTime_Object = MibTableColumn
ieee8021SpanningTreeHoldTime = _Ieee8021SpanningTreeHoldTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 11),
    _Ieee8021SpanningTreeHoldTime_Type()
)
ieee8021SpanningTreeHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeHoldTime.setUnits("centi-seconds")
_Ieee8021SpanningTreeForwardDelay_Type = Timeout
_Ieee8021SpanningTreeForwardDelay_Object = MibTableColumn
ieee8021SpanningTreeForwardDelay = _Ieee8021SpanningTreeForwardDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 12),
    _Ieee8021SpanningTreeForwardDelay_Type()
)
ieee8021SpanningTreeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeForwardDelay.setUnits("centi-seconds")


class _Ieee8021SpanningTreeBridgeMaxAge_Type(Timeout):
    """Custom type ieee8021SpanningTreeBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_Ieee8021SpanningTreeBridgeMaxAge_Type.__name__ = "Timeout"
_Ieee8021SpanningTreeBridgeMaxAge_Object = MibTableColumn
ieee8021SpanningTreeBridgeMaxAge = _Ieee8021SpanningTreeBridgeMaxAge_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 13),
    _Ieee8021SpanningTreeBridgeMaxAge_Type()
)
ieee8021SpanningTreeBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeBridgeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeBridgeMaxAge.setUnits("centi-seconds")


class _Ieee8021SpanningTreeBridgeHelloTime_Type(Timeout):
    """Custom type ieee8021SpanningTreeBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_Ieee8021SpanningTreeBridgeHelloTime_Type.__name__ = "Timeout"
_Ieee8021SpanningTreeBridgeHelloTime_Object = MibTableColumn
ieee8021SpanningTreeBridgeHelloTime = _Ieee8021SpanningTreeBridgeHelloTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 14),
    _Ieee8021SpanningTreeBridgeHelloTime_Type()
)
ieee8021SpanningTreeBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeBridgeHelloTime.setUnits("centi-seconds")


class _Ieee8021SpanningTreeBridgeForwardDelay_Type(Timeout):
    """Custom type ieee8021SpanningTreeBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_Ieee8021SpanningTreeBridgeForwardDelay_Type.__name__ = "Timeout"
_Ieee8021SpanningTreeBridgeForwardDelay_Object = MibTableColumn
ieee8021SpanningTreeBridgeForwardDelay = _Ieee8021SpanningTreeBridgeForwardDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 15),
    _Ieee8021SpanningTreeBridgeForwardDelay_Type()
)
ieee8021SpanningTreeBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeBridgeForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeBridgeForwardDelay.setUnits("centi-seconds")


class _Ieee8021SpanningTreeVersion_Type(Integer32):
    """Custom type ieee8021SpanningTreeVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stp", 0))
    )


_Ieee8021SpanningTreeVersion_Type.__name__ = "Integer32"
_Ieee8021SpanningTreeVersion_Object = MibTableColumn
ieee8021SpanningTreeVersion = _Ieee8021SpanningTreeVersion_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 16),
    _Ieee8021SpanningTreeVersion_Type()
)
ieee8021SpanningTreeVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeVersion.setStatus("current")


class _Ieee8021SpanningTreeRstpTxHoldCount_Type(Integer32):
    """Custom type ieee8021SpanningTreeRstpTxHoldCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Ieee8021SpanningTreeRstpTxHoldCount_Type.__name__ = "Integer32"
_Ieee8021SpanningTreeRstpTxHoldCount_Object = MibTableColumn
ieee8021SpanningTreeRstpTxHoldCount = _Ieee8021SpanningTreeRstpTxHoldCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 1, 1, 17),
    _Ieee8021SpanningTreeRstpTxHoldCount_Type()
)
ieee8021SpanningTreeRstpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpTxHoldCount.setStatus("current")
_Ieee8021SpanningTreePortTable_Object = MibTable
ieee8021SpanningTreePortTable = _Ieee8021SpanningTreePortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortTable.setStatus("current")
_Ieee8021SpanningTreePortEntry_Object = MibTableRow
ieee8021SpanningTreePortEntry = _Ieee8021SpanningTreePortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1)
)
ieee8021SpanningTreePortEntry.setIndexNames(
    (0, "IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortComponentId"),
    (0, "IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePort"),
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortEntry.setStatus("current")
_Ieee8021SpanningTreePortComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021SpanningTreePortComponentId_Object = MibTableColumn
ieee8021SpanningTreePortComponentId = _Ieee8021SpanningTreePortComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 1),
    _Ieee8021SpanningTreePortComponentId_Type()
)
ieee8021SpanningTreePortComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortComponentId.setStatus("current")
_Ieee8021SpanningTreePort_Type = IEEE8021BridgePortNumber
_Ieee8021SpanningTreePort_Object = MibTableColumn
ieee8021SpanningTreePort = _Ieee8021SpanningTreePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 2),
    _Ieee8021SpanningTreePort_Type()
)
ieee8021SpanningTreePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePort.setStatus("current")


class _Ieee8021SpanningTreePortPriority_Type(Integer32):
    """Custom type ieee8021SpanningTreePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ieee8021SpanningTreePortPriority_Type.__name__ = "Integer32"
_Ieee8021SpanningTreePortPriority_Object = MibTableColumn
ieee8021SpanningTreePortPriority = _Ieee8021SpanningTreePortPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 3),
    _Ieee8021SpanningTreePortPriority_Type()
)
ieee8021SpanningTreePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortPriority.setStatus("current")


class _Ieee8021SpanningTreePortState_Type(Integer32):
    """Custom type ieee8021SpanningTreePortState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_Ieee8021SpanningTreePortState_Type.__name__ = "Integer32"
_Ieee8021SpanningTreePortState_Object = MibTableColumn
ieee8021SpanningTreePortState = _Ieee8021SpanningTreePortState_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 4),
    _Ieee8021SpanningTreePortState_Type()
)
ieee8021SpanningTreePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortState.setStatus("current")
_Ieee8021SpanningTreePortEnabled_Type = TruthValue
_Ieee8021SpanningTreePortEnabled_Object = MibTableColumn
ieee8021SpanningTreePortEnabled = _Ieee8021SpanningTreePortEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 5),
    _Ieee8021SpanningTreePortEnabled_Type()
)
ieee8021SpanningTreePortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortEnabled.setStatus("current")


class _Ieee8021SpanningTreePortPathCost_Type(Integer32):
    """Custom type ieee8021SpanningTreePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Ieee8021SpanningTreePortPathCost_Type.__name__ = "Integer32"
_Ieee8021SpanningTreePortPathCost_Object = MibTableColumn
ieee8021SpanningTreePortPathCost = _Ieee8021SpanningTreePortPathCost_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 6),
    _Ieee8021SpanningTreePortPathCost_Type()
)
ieee8021SpanningTreePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortPathCost.setStatus("current")
_Ieee8021SpanningTreePortDesignatedRoot_Type = BridgeId
_Ieee8021SpanningTreePortDesignatedRoot_Object = MibTableColumn
ieee8021SpanningTreePortDesignatedRoot = _Ieee8021SpanningTreePortDesignatedRoot_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 7),
    _Ieee8021SpanningTreePortDesignatedRoot_Type()
)
ieee8021SpanningTreePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortDesignatedRoot.setStatus("current")
_Ieee8021SpanningTreePortDesignatedCost_Type = Integer32
_Ieee8021SpanningTreePortDesignatedCost_Object = MibTableColumn
ieee8021SpanningTreePortDesignatedCost = _Ieee8021SpanningTreePortDesignatedCost_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 8),
    _Ieee8021SpanningTreePortDesignatedCost_Type()
)
ieee8021SpanningTreePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortDesignatedCost.setStatus("current")
_Ieee8021SpanningTreePortDesignatedBridge_Type = BridgeId
_Ieee8021SpanningTreePortDesignatedBridge_Object = MibTableColumn
ieee8021SpanningTreePortDesignatedBridge = _Ieee8021SpanningTreePortDesignatedBridge_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 9),
    _Ieee8021SpanningTreePortDesignatedBridge_Type()
)
ieee8021SpanningTreePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortDesignatedBridge.setStatus("current")


class _Ieee8021SpanningTreePortDesignatedPort_Type(OctetString):
    """Custom type ieee8021SpanningTreePortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Ieee8021SpanningTreePortDesignatedPort_Type.__name__ = "OctetString"
_Ieee8021SpanningTreePortDesignatedPort_Object = MibTableColumn
ieee8021SpanningTreePortDesignatedPort = _Ieee8021SpanningTreePortDesignatedPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 10),
    _Ieee8021SpanningTreePortDesignatedPort_Type()
)
ieee8021SpanningTreePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortDesignatedPort.setStatus("current")
_Ieee8021SpanningTreePortForwardTransitions_Type = Counter64
_Ieee8021SpanningTreePortForwardTransitions_Object = MibTableColumn
ieee8021SpanningTreePortForwardTransitions = _Ieee8021SpanningTreePortForwardTransitions_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 11),
    _Ieee8021SpanningTreePortForwardTransitions_Type()
)
ieee8021SpanningTreePortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortForwardTransitions.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortForwardTransitions.setUnits("forwarding transitions")
_Ieee8021SpanningTreeRstpPortProtocolMigration_Type = TruthValue
_Ieee8021SpanningTreeRstpPortProtocolMigration_Object = MibTableColumn
ieee8021SpanningTreeRstpPortProtocolMigration = _Ieee8021SpanningTreeRstpPortProtocolMigration_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 12),
    _Ieee8021SpanningTreeRstpPortProtocolMigration_Type()
)
ieee8021SpanningTreeRstpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpPortProtocolMigration.setStatus("current")
_Ieee8021SpanningTreeRstpPortAdminEdgePort_Type = TruthValue
_Ieee8021SpanningTreeRstpPortAdminEdgePort_Object = MibTableColumn
ieee8021SpanningTreeRstpPortAdminEdgePort = _Ieee8021SpanningTreeRstpPortAdminEdgePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 13),
    _Ieee8021SpanningTreeRstpPortAdminEdgePort_Type()
)
ieee8021SpanningTreeRstpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpPortAdminEdgePort.setStatus("current")
_Ieee8021SpanningTreeRstpPortOperEdgePort_Type = TruthValue
_Ieee8021SpanningTreeRstpPortOperEdgePort_Object = MibTableColumn
ieee8021SpanningTreeRstpPortOperEdgePort = _Ieee8021SpanningTreeRstpPortOperEdgePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 14),
    _Ieee8021SpanningTreeRstpPortOperEdgePort_Type()
)
ieee8021SpanningTreeRstpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpPortOperEdgePort.setStatus("current")


class _Ieee8021SpanningTreeRstpPortAdminPathCost_Type(Integer32):
    """Custom type ieee8021SpanningTreeRstpPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Ieee8021SpanningTreeRstpPortAdminPathCost_Type.__name__ = "Integer32"
_Ieee8021SpanningTreeRstpPortAdminPathCost_Object = MibTableColumn
ieee8021SpanningTreeRstpPortAdminPathCost = _Ieee8021SpanningTreeRstpPortAdminPathCost_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 2, 1, 15),
    _Ieee8021SpanningTreeRstpPortAdminPathCost_Type()
)
ieee8021SpanningTreeRstpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpPortAdminPathCost.setStatus("current")
_Ieee8021SpanningTreePortExtensionTable_Object = MibTable
ieee8021SpanningTreePortExtensionTable = _Ieee8021SpanningTreePortExtensionTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortExtensionTable.setStatus("current")
_Ieee8021SpanningTreePortExtensionEntry_Object = MibTableRow
ieee8021SpanningTreePortExtensionEntry = _Ieee8021SpanningTreePortExtensionEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortExtensionEntry.setStatus("current")
_Ieee8021SpanningTreeRstpPortAutoEdgePort_Type = TruthValue
_Ieee8021SpanningTreeRstpPortAutoEdgePort_Object = MibTableColumn
ieee8021SpanningTreeRstpPortAutoEdgePort = _Ieee8021SpanningTreeRstpPortAutoEdgePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 3, 1, 1),
    _Ieee8021SpanningTreeRstpPortAutoEdgePort_Type()
)
ieee8021SpanningTreeRstpPortAutoEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpPortAutoEdgePort.setStatus("current")
_Ieee8021SpanningTreeRstpPortAutoIsolatePort_Type = TruthValue
_Ieee8021SpanningTreeRstpPortAutoIsolatePort_Object = MibTableColumn
ieee8021SpanningTreeRstpPortAutoIsolatePort = _Ieee8021SpanningTreeRstpPortAutoIsolatePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 3, 1, 2),
    _Ieee8021SpanningTreeRstpPortAutoIsolatePort_Type()
)
ieee8021SpanningTreeRstpPortAutoIsolatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpPortAutoIsolatePort.setStatus("current")
_Ieee8021SpanningTreeRstpPortIsolatePort_Type = TruthValue
_Ieee8021SpanningTreeRstpPortIsolatePort_Object = MibTableColumn
ieee8021SpanningTreeRstpPortIsolatePort = _Ieee8021SpanningTreeRstpPortIsolatePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 3, 1, 3, 1, 3),
    _Ieee8021SpanningTreeRstpPortIsolatePort_Type()
)
ieee8021SpanningTreeRstpPortIsolatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpPortIsolatePort.setStatus("current")
_Ieee8021SpanningTreeConformance_ObjectIdentity = ObjectIdentity
ieee8021SpanningTreeConformance = _Ieee8021SpanningTreeConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 3, 2)
)
_Ieee8021SpanningTreeCompliances_ObjectIdentity = ObjectIdentity
ieee8021SpanningTreeCompliances = _Ieee8021SpanningTreeCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 3, 2, 1)
)
_Ieee8021SpanningTreeGroups_ObjectIdentity = ObjectIdentity
ieee8021SpanningTreeGroups = _Ieee8021SpanningTreeGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 3, 2, 2)
)
ieee8021SpanningTreePortEntry.registerAugmentions(
    ("IEEE8021-SPANNING-TREE-MIB",
     "ieee8021SpanningTreePortExtensionEntry")
)
ieee8021SpanningTreePortExtensionEntry.setIndexNames(*ieee8021SpanningTreePortEntry.getIndexNames())

# Managed Objects groups

ieee8021SpanningTreeGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 1)
)
ieee8021SpanningTreeGroup.setObjects(
      *(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeProtocolSpecification"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePriority"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeTimeSinceTopologyChange"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeTopChanges"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeDesignatedRoot"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRootCost"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRootPort"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeMaxAge"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeHelloTime"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeHoldTime"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeForwardDelay"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeBridgeMaxAge"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeBridgeHelloTime"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeBridgeForwardDelay"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeVersion"))
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreeGroup.setStatus("current")

ieee8021SpanningTreeRstpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 2)
)
ieee8021SpanningTreeRstpGroup.setObjects(
    ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpTxHoldCount")
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpGroup.setStatus("current")

ieee8021SpanningTreePortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 3)
)
ieee8021SpanningTreePortGroup.setObjects(
      *(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortPriority"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortState"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortEnabled"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortPathCost"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortDesignatedRoot"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortDesignatedCost"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortDesignatedBridge"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortDesignatedPort"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreePortForwardTransitions"))
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreePortGroup.setStatus("current")

ieee8021SpanningTreeRstpPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 4)
)
ieee8021SpanningTreeRstpPortGroup.setObjects(
      *(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortProtocolMigration"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortAdminEdgePort"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortOperEdgePort"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortAdminPathCost"))
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpPortGroup.setStatus("current")

ieee8021SpanningTreeRstpFragileGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 6)
)
ieee8021SpanningTreeRstpFragileGroup.setObjects(
      *(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortAutoEdgePort"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortAutoIsolatePort"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeRstpPortIsolatePort"))
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpFragileGroup.setStatus("current")


# Notification objects

ieee8021SpanningTreeNewRoot = NotificationType(
    (1, 3, 111, 2, 802, 1, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreeNewRoot.setStatus(
        "current"
    )

ieee8021SpanningTreeTopologyChange = NotificationType(
    (1, 3, 111, 2, 802, 1, 1, 3, 0, 2)
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreeTopologyChange.setStatus(
        "current"
    )


# Notifications groups

ieee8021SpanningTreeNotificationGroup = NotificationGroup(
    (1, 3, 111, 2, 802, 1, 1, 3, 2, 2, 5)
)
ieee8021SpanningTreeNotificationGroup.setObjects(
      *(("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeNewRoot"),
        ("IEEE8021-SPANNING-TREE-MIB", "ieee8021SpanningTreeTopologyChange"))
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ieee8021SpanningTreeCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreeCompliance.setStatus(
        "current"
    )

ieee8021SpanningTreeRstpCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021SpanningTreeRstpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-SPANNING-TREE-MIB",
    **{"ieee8021SpanningTreeMib": ieee8021SpanningTreeMib,
       "ieee8021SpanningTreeNotifications": ieee8021SpanningTreeNotifications,
       "ieee8021SpanningTreeNewRoot": ieee8021SpanningTreeNewRoot,
       "ieee8021SpanningTreeTopologyChange": ieee8021SpanningTreeTopologyChange,
       "ieee8021SpanningTreeObjects": ieee8021SpanningTreeObjects,
       "ieee8021SpanningTreeTable": ieee8021SpanningTreeTable,
       "ieee8021SpanningTreeEntry": ieee8021SpanningTreeEntry,
       "ieee8021SpanningTreeComponentId": ieee8021SpanningTreeComponentId,
       "ieee8021SpanningTreeProtocolSpecification": ieee8021SpanningTreeProtocolSpecification,
       "ieee8021SpanningTreePriority": ieee8021SpanningTreePriority,
       "ieee8021SpanningTreeTimeSinceTopologyChange": ieee8021SpanningTreeTimeSinceTopologyChange,
       "ieee8021SpanningTreeTopChanges": ieee8021SpanningTreeTopChanges,
       "ieee8021SpanningTreeDesignatedRoot": ieee8021SpanningTreeDesignatedRoot,
       "ieee8021SpanningTreeRootCost": ieee8021SpanningTreeRootCost,
       "ieee8021SpanningTreeRootPort": ieee8021SpanningTreeRootPort,
       "ieee8021SpanningTreeMaxAge": ieee8021SpanningTreeMaxAge,
       "ieee8021SpanningTreeHelloTime": ieee8021SpanningTreeHelloTime,
       "ieee8021SpanningTreeHoldTime": ieee8021SpanningTreeHoldTime,
       "ieee8021SpanningTreeForwardDelay": ieee8021SpanningTreeForwardDelay,
       "ieee8021SpanningTreeBridgeMaxAge": ieee8021SpanningTreeBridgeMaxAge,
       "ieee8021SpanningTreeBridgeHelloTime": ieee8021SpanningTreeBridgeHelloTime,
       "ieee8021SpanningTreeBridgeForwardDelay": ieee8021SpanningTreeBridgeForwardDelay,
       "ieee8021SpanningTreeVersion": ieee8021SpanningTreeVersion,
       "ieee8021SpanningTreeRstpTxHoldCount": ieee8021SpanningTreeRstpTxHoldCount,
       "ieee8021SpanningTreePortTable": ieee8021SpanningTreePortTable,
       "ieee8021SpanningTreePortEntry": ieee8021SpanningTreePortEntry,
       "ieee8021SpanningTreePortComponentId": ieee8021SpanningTreePortComponentId,
       "ieee8021SpanningTreePort": ieee8021SpanningTreePort,
       "ieee8021SpanningTreePortPriority": ieee8021SpanningTreePortPriority,
       "ieee8021SpanningTreePortState": ieee8021SpanningTreePortState,
       "ieee8021SpanningTreePortEnabled": ieee8021SpanningTreePortEnabled,
       "ieee8021SpanningTreePortPathCost": ieee8021SpanningTreePortPathCost,
       "ieee8021SpanningTreePortDesignatedRoot": ieee8021SpanningTreePortDesignatedRoot,
       "ieee8021SpanningTreePortDesignatedCost": ieee8021SpanningTreePortDesignatedCost,
       "ieee8021SpanningTreePortDesignatedBridge": ieee8021SpanningTreePortDesignatedBridge,
       "ieee8021SpanningTreePortDesignatedPort": ieee8021SpanningTreePortDesignatedPort,
       "ieee8021SpanningTreePortForwardTransitions": ieee8021SpanningTreePortForwardTransitions,
       "ieee8021SpanningTreeRstpPortProtocolMigration": ieee8021SpanningTreeRstpPortProtocolMigration,
       "ieee8021SpanningTreeRstpPortAdminEdgePort": ieee8021SpanningTreeRstpPortAdminEdgePort,
       "ieee8021SpanningTreeRstpPortOperEdgePort": ieee8021SpanningTreeRstpPortOperEdgePort,
       "ieee8021SpanningTreeRstpPortAdminPathCost": ieee8021SpanningTreeRstpPortAdminPathCost,
       "ieee8021SpanningTreePortExtensionTable": ieee8021SpanningTreePortExtensionTable,
       "ieee8021SpanningTreePortExtensionEntry": ieee8021SpanningTreePortExtensionEntry,
       "ieee8021SpanningTreeRstpPortAutoEdgePort": ieee8021SpanningTreeRstpPortAutoEdgePort,
       "ieee8021SpanningTreeRstpPortAutoIsolatePort": ieee8021SpanningTreeRstpPortAutoIsolatePort,
       "ieee8021SpanningTreeRstpPortIsolatePort": ieee8021SpanningTreeRstpPortIsolatePort,
       "ieee8021SpanningTreeConformance": ieee8021SpanningTreeConformance,
       "ieee8021SpanningTreeCompliances": ieee8021SpanningTreeCompliances,
       "ieee8021SpanningTreeCompliance": ieee8021SpanningTreeCompliance,
       "ieee8021SpanningTreeRstpCompliance": ieee8021SpanningTreeRstpCompliance,
       "ieee8021SpanningTreeGroups": ieee8021SpanningTreeGroups,
       "ieee8021SpanningTreeGroup": ieee8021SpanningTreeGroup,
       "ieee8021SpanningTreeRstpGroup": ieee8021SpanningTreeRstpGroup,
       "ieee8021SpanningTreePortGroup": ieee8021SpanningTreePortGroup,
       "ieee8021SpanningTreeRstpPortGroup": ieee8021SpanningTreeRstpPortGroup,
       "ieee8021SpanningTreeNotificationGroup": ieee8021SpanningTreeNotificationGroup,
       "ieee8021SpanningTreeRstpFragileGroup": ieee8021SpanningTreeRstpFragileGroup}
)
