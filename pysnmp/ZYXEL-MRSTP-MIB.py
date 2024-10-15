# SNMP MIB module (ZYXEL-MRSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-MRSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:23 2024
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
 dot1dBasePort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelMrstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMrstpSetup_ObjectIdentity = ObjectIdentity
zyxelMrstpSetup = _ZyxelMrstpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1)
)
_ZyxelMrstpBridgeTable_Object = MibTable
zyxelMrstpBridgeTable = _ZyxelMrstpBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelMrstpBridgeTable.setStatus("current")
_ZyxelMrstpBridgeEntry_Object = MibTableRow
zyxelMrstpBridgeEntry = _ZyxelMrstpBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1)
)
zyxelMrstpBridgeEntry.setIndexNames(
    (0, "ZYXEL-MRSTP-MIB", "zyMrstpBridgeIndex"),
)
if mibBuilder.loadTexts:
    zyxelMrstpBridgeEntry.setStatus("current")
_ZyMrstpBridgeIndex_Type = Integer32
_ZyMrstpBridgeIndex_Object = MibTableColumn
zyMrstpBridgeIndex = _ZyMrstpBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 1),
    _ZyMrstpBridgeIndex_Type()
)
zyMrstpBridgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMrstpBridgeIndex.setStatus("current")
_ZyMrstpBridgeState_Type = EnabledStatus
_ZyMrstpBridgeState_Object = MibTableColumn
zyMrstpBridgeState = _ZyMrstpBridgeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 2),
    _ZyMrstpBridgeState_Type()
)
zyMrstpBridgeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpBridgeState.setStatus("current")


class _ZyMrstpBridgePriority_Type(Integer32):
    """Custom type zyMrstpBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZyMrstpBridgePriority_Type.__name__ = "Integer32"
_ZyMrstpBridgePriority_Object = MibTableColumn
zyMrstpBridgePriority = _ZyMrstpBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 3),
    _ZyMrstpBridgePriority_Type()
)
zyMrstpBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpBridgePriority.setStatus("current")


class _ZyMrstpBridgeRootMaxAge_Type(Timeout):
    """Custom type zyMrstpBridgeRootMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_ZyMrstpBridgeRootMaxAge_Type.__name__ = "Timeout"
_ZyMrstpBridgeRootMaxAge_Object = MibTableColumn
zyMrstpBridgeRootMaxAge = _ZyMrstpBridgeRootMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 4),
    _ZyMrstpBridgeRootMaxAge_Type()
)
zyMrstpBridgeRootMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpBridgeRootMaxAge.setStatus("current")


class _ZyMrstpBridgeRootHelloTime_Type(Timeout):
    """Custom type zyMrstpBridgeRootHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_ZyMrstpBridgeRootHelloTime_Type.__name__ = "Timeout"
_ZyMrstpBridgeRootHelloTime_Object = MibTableColumn
zyMrstpBridgeRootHelloTime = _ZyMrstpBridgeRootHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 5),
    _ZyMrstpBridgeRootHelloTime_Type()
)
zyMrstpBridgeRootHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpBridgeRootHelloTime.setStatus("current")


class _ZyMrstpBridgeRootForwardDelay_Type(Timeout):
    """Custom type zyMrstpBridgeRootForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_ZyMrstpBridgeRootForwardDelay_Type.__name__ = "Timeout"
_ZyMrstpBridgeRootForwardDelay_Object = MibTableColumn
zyMrstpBridgeRootForwardDelay = _ZyMrstpBridgeRootForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 6),
    _ZyMrstpBridgeRootForwardDelay_Type()
)
zyMrstpBridgeRootForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpBridgeRootForwardDelay.setStatus("current")
_ZyxelMrstpPortTable_Object = MibTable
zyxelMrstpPortTable = _ZyxelMrstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelMrstpPortTable.setStatus("current")
_ZyxelMrstpPortEntry_Object = MibTableRow
zyxelMrstpPortEntry = _ZyxelMrstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1)
)
zyxelMrstpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMrstpPortEntry.setStatus("current")


class _ZyMrstpPortPriority_Type(Integer32):
    """Custom type zyMrstpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZyMrstpPortPriority_Type.__name__ = "Integer32"
_ZyMrstpPortPriority_Object = MibTableColumn
zyMrstpPortPriority = _ZyMrstpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1, 1),
    _ZyMrstpPortPriority_Type()
)
zyMrstpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpPortPriority.setStatus("current")
_ZyMrstpPortEnable_Type = EnabledStatus
_ZyMrstpPortEnable_Object = MibTableColumn
zyMrstpPortEnable = _ZyMrstpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1, 2),
    _ZyMrstpPortEnable_Type()
)
zyMrstpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpPortEnable.setStatus("current")


class _ZyMrstpPortPathCost_Type(Integer32):
    """Custom type zyMrstpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZyMrstpPortPathCost_Type.__name__ = "Integer32"
_ZyMrstpPortPathCost_Object = MibTableColumn
zyMrstpPortPathCost = _ZyMrstpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1, 3),
    _ZyMrstpPortPathCost_Type()
)
zyMrstpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpPortPathCost.setStatus("current")
_ZyMrstpPortOnBridgeIndex_Type = Integer32
_ZyMrstpPortOnBridgeIndex_Object = MibTableColumn
zyMrstpPortOnBridgeIndex = _ZyMrstpPortOnBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1, 4),
    _ZyMrstpPortOnBridgeIndex_Type()
)
zyMrstpPortOnBridgeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpPortOnBridgeIndex.setStatus("current")


class _ZyMrstpPortAdminEdgePort_Type(Integer32):
    """Custom type zyMrstpPortAdminEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ZyMrstpPortAdminEdgePort_Type.__name__ = "Integer32"
_ZyMrstpPortAdminEdgePort_Object = MibTableColumn
zyMrstpPortAdminEdgePort = _ZyMrstpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1, 5),
    _ZyMrstpPortAdminEdgePort_Type()
)
zyMrstpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpPortAdminEdgePort.setStatus("current")
_ZyxelMrstpStatus_ObjectIdentity = ObjectIdentity
zyxelMrstpStatus = _ZyxelMrstpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2)
)
_ZyxelMrstpBridgeInfoTable_Object = MibTable
zyxelMrstpBridgeInfoTable = _ZyxelMrstpBridgeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelMrstpBridgeInfoTable.setStatus("current")
_ZyxelMrstpBridgeInfoEntry_Object = MibTableRow
zyxelMrstpBridgeInfoEntry = _ZyxelMrstpBridgeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1)
)
zyxelMrstpBridgeInfoEntry.setIndexNames(
    (0, "ZYXEL-MRSTP-MIB", "zyMrstpBridgeInfoIndex"),
)
if mibBuilder.loadTexts:
    zyxelMrstpBridgeInfoEntry.setStatus("current")
_ZyMrstpBridgeInfoIndex_Type = Integer32
_ZyMrstpBridgeInfoIndex_Object = MibTableColumn
zyMrstpBridgeInfoIndex = _ZyMrstpBridgeInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 1),
    _ZyMrstpBridgeInfoIndex_Type()
)
zyMrstpBridgeInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoIndex.setStatus("current")


class _ZyMrstpBridgeInfoProtocolSpecification_Type(Integer32):
    """Custom type zyMrstpBridgeInfoProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_ZyMrstpBridgeInfoProtocolSpecification_Type.__name__ = "Integer32"
_ZyMrstpBridgeInfoProtocolSpecification_Object = MibTableColumn
zyMrstpBridgeInfoProtocolSpecification = _ZyMrstpBridgeInfoProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 2),
    _ZyMrstpBridgeInfoProtocolSpecification_Type()
)
zyMrstpBridgeInfoProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoProtocolSpecification.setStatus("current")
_ZyMrstpBridgeInfoTimeSinceTopologyChange_Type = TimeTicks
_ZyMrstpBridgeInfoTimeSinceTopologyChange_Object = MibTableColumn
zyMrstpBridgeInfoTimeSinceTopologyChange = _ZyMrstpBridgeInfoTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 3),
    _ZyMrstpBridgeInfoTimeSinceTopologyChange_Type()
)
zyMrstpBridgeInfoTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoTimeSinceTopologyChange.setStatus("current")
_ZyMrstpBridgeInfoTopologyChanges_Type = Counter32
_ZyMrstpBridgeInfoTopologyChanges_Object = MibTableColumn
zyMrstpBridgeInfoTopologyChanges = _ZyMrstpBridgeInfoTopologyChanges_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 4),
    _ZyMrstpBridgeInfoTopologyChanges_Type()
)
zyMrstpBridgeInfoTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoTopologyChanges.setStatus("current")
_ZyMrstpBridgeInfoDesignatedRoot_Type = BridgeId
_ZyMrstpBridgeInfoDesignatedRoot_Object = MibTableColumn
zyMrstpBridgeInfoDesignatedRoot = _ZyMrstpBridgeInfoDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 5),
    _ZyMrstpBridgeInfoDesignatedRoot_Type()
)
zyMrstpBridgeInfoDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoDesignatedRoot.setStatus("current")
_ZyMrstpBridgeInfoRootCost_Type = Integer32
_ZyMrstpBridgeInfoRootCost_Object = MibTableColumn
zyMrstpBridgeInfoRootCost = _ZyMrstpBridgeInfoRootCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 6),
    _ZyMrstpBridgeInfoRootCost_Type()
)
zyMrstpBridgeInfoRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoRootCost.setStatus("current")
_ZyMrstpBridgeInfoRootPort_Type = Integer32
_ZyMrstpBridgeInfoRootPort_Object = MibTableColumn
zyMrstpBridgeInfoRootPort = _ZyMrstpBridgeInfoRootPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 7),
    _ZyMrstpBridgeInfoRootPort_Type()
)
zyMrstpBridgeInfoRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoRootPort.setStatus("current")
_ZyMrstpBridgeInfoMaxAge_Type = Timeout
_ZyMrstpBridgeInfoMaxAge_Object = MibTableColumn
zyMrstpBridgeInfoMaxAge = _ZyMrstpBridgeInfoMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 8),
    _ZyMrstpBridgeInfoMaxAge_Type()
)
zyMrstpBridgeInfoMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoMaxAge.setStatus("current")
_ZyMrstpBridgeInfoHelloTime_Type = Timeout
_ZyMrstpBridgeInfoHelloTime_Object = MibTableColumn
zyMrstpBridgeInfoHelloTime = _ZyMrstpBridgeInfoHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 9),
    _ZyMrstpBridgeInfoHelloTime_Type()
)
zyMrstpBridgeInfoHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoHelloTime.setStatus("current")
_ZyMrstpBridgeInfoHoldTime_Type = Integer32
_ZyMrstpBridgeInfoHoldTime_Object = MibTableColumn
zyMrstpBridgeInfoHoldTime = _ZyMrstpBridgeInfoHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 10),
    _ZyMrstpBridgeInfoHoldTime_Type()
)
zyMrstpBridgeInfoHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoHoldTime.setStatus("current")
_ZyMrstpBridgeInfoForwardDelay_Type = Timeout
_ZyMrstpBridgeInfoForwardDelay_Object = MibTableColumn
zyMrstpBridgeInfoForwardDelay = _ZyMrstpBridgeInfoForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 11),
    _ZyMrstpBridgeInfoForwardDelay_Type()
)
zyMrstpBridgeInfoForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoForwardDelay.setStatus("current")


class _ZyMrstpBridgeInfoRootMaxAge_Type(Timeout):
    """Custom type zyMrstpBridgeInfoRootMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_ZyMrstpBridgeInfoRootMaxAge_Type.__name__ = "Timeout"
_ZyMrstpBridgeInfoRootMaxAge_Object = MibTableColumn
zyMrstpBridgeInfoRootMaxAge = _ZyMrstpBridgeInfoRootMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 12),
    _ZyMrstpBridgeInfoRootMaxAge_Type()
)
zyMrstpBridgeInfoRootMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoRootMaxAge.setStatus("current")


class _ZyMrstpBridgeInfoRootHelloTime_Type(Timeout):
    """Custom type zyMrstpBridgeInfoRootHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_ZyMrstpBridgeInfoRootHelloTime_Type.__name__ = "Timeout"
_ZyMrstpBridgeInfoRootHelloTime_Object = MibTableColumn
zyMrstpBridgeInfoRootHelloTime = _ZyMrstpBridgeInfoRootHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 13),
    _ZyMrstpBridgeInfoRootHelloTime_Type()
)
zyMrstpBridgeInfoRootHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoRootHelloTime.setStatus("current")


class _ZyMrstpBridgeInfoRootForwardDelay_Type(Timeout):
    """Custom type zyMrstpBridgeInfoRootForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_ZyMrstpBridgeInfoRootForwardDelay_Type.__name__ = "Timeout"
_ZyMrstpBridgeInfoRootForwardDelay_Object = MibTableColumn
zyMrstpBridgeInfoRootForwardDelay = _ZyMrstpBridgeInfoRootForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 14),
    _ZyMrstpBridgeInfoRootForwardDelay_Type()
)
zyMrstpBridgeInfoRootForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMrstpBridgeInfoRootForwardDelay.setStatus("current")
_ZyxelMrstpPortInfoTable_Object = MibTable
zyxelMrstpPortInfoTable = _ZyxelMrstpPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelMrstpPortInfoTable.setStatus("current")
_ZyxelMrstpPortInfoEntry_Object = MibTableRow
zyxelMrstpPortInfoEntry = _ZyxelMrstpPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1)
)
zyxelMrstpPortInfoEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMrstpPortInfoEntry.setStatus("current")


class _ZyMrstpPortInfoState_Type(Integer32):
    """Custom type zyMrstpPortInfoState based on Integer32"""
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


_ZyMrstpPortInfoState_Type.__name__ = "Integer32"
_ZyMrstpPortInfoState_Object = MibTableColumn
zyMrstpPortInfoState = _ZyMrstpPortInfoState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 1),
    _ZyMrstpPortInfoState_Type()
)
zyMrstpPortInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpPortInfoState.setStatus("current")
_ZyMrstpPortInfoDesignatedRoot_Type = BridgeId
_ZyMrstpPortInfoDesignatedRoot_Object = MibTableColumn
zyMrstpPortInfoDesignatedRoot = _ZyMrstpPortInfoDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 2),
    _ZyMrstpPortInfoDesignatedRoot_Type()
)
zyMrstpPortInfoDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpPortInfoDesignatedRoot.setStatus("current")
_ZyMrstpPortInfoDesignatedCost_Type = Integer32
_ZyMrstpPortInfoDesignatedCost_Object = MibTableColumn
zyMrstpPortInfoDesignatedCost = _ZyMrstpPortInfoDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 3),
    _ZyMrstpPortInfoDesignatedCost_Type()
)
zyMrstpPortInfoDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpPortInfoDesignatedCost.setStatus("current")
_ZyMrstpPortInfoDesignatedBridge_Type = BridgeId
_ZyMrstpPortInfoDesignatedBridge_Object = MibTableColumn
zyMrstpPortInfoDesignatedBridge = _ZyMrstpPortInfoDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 4),
    _ZyMrstpPortInfoDesignatedBridge_Type()
)
zyMrstpPortInfoDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpPortInfoDesignatedBridge.setStatus("current")


class _ZyMrstpPortInfoDesignatedPort_Type(OctetString):
    """Custom type zyMrstpPortInfoDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ZyMrstpPortInfoDesignatedPort_Type.__name__ = "OctetString"
_ZyMrstpPortInfoDesignatedPort_Object = MibTableColumn
zyMrstpPortInfoDesignatedPort = _ZyMrstpPortInfoDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 5),
    _ZyMrstpPortInfoDesignatedPort_Type()
)
zyMrstpPortInfoDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpPortInfoDesignatedPort.setStatus("current")
_ZyMrstpPortInfoForwardTransitions_Type = Counter32
_ZyMrstpPortInfoForwardTransitions_Object = MibTableColumn
zyMrstpPortInfoForwardTransitions = _ZyMrstpPortInfoForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 6),
    _ZyMrstpPortInfoForwardTransitions_Type()
)
zyMrstpPortInfoForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpPortInfoForwardTransitions.setStatus("current")


class _ZyMrstpPortInfoOperEdgePort_Type(Integer32):
    """Custom type zyMrstpPortInfoOperEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ZyMrstpPortInfoOperEdgePort_Type.__name__ = "Integer32"
_ZyMrstpPortInfoOperEdgePort_Object = MibTableColumn
zyMrstpPortInfoOperEdgePort = _ZyMrstpPortInfoOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 7),
    _ZyMrstpPortInfoOperEdgePort_Type()
)
zyMrstpPortInfoOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMrstpPortInfoOperEdgePort.setStatus("current")
_ZyxelMrstpNotifications_ObjectIdentity = ObjectIdentity
zyxelMrstpNotifications = _ZyxelMrstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 3)
)

# Managed Objects groups


# Notification objects

zyMrstpNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 3, 1)
)
zyMrstpNewRoot.setObjects(
    ("ZYXEL-MRSTP-MIB", "zyMrstpBridgeIndex")
)
if mibBuilder.loadTexts:
    zyMrstpNewRoot.setStatus(
        "current"
    )

zyMrstpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 3, 2)
)
zyMrstpTopologyChange.setObjects(
    ("ZYXEL-MRSTP-MIB", "zyMrstpBridgeIndex")
)
if mibBuilder.loadTexts:
    zyMrstpTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MRSTP-MIB",
    **{"zyxelMrstp": zyxelMrstp,
       "zyxelMrstpSetup": zyxelMrstpSetup,
       "zyxelMrstpBridgeTable": zyxelMrstpBridgeTable,
       "zyxelMrstpBridgeEntry": zyxelMrstpBridgeEntry,
       "zyMrstpBridgeIndex": zyMrstpBridgeIndex,
       "zyMrstpBridgeState": zyMrstpBridgeState,
       "zyMrstpBridgePriority": zyMrstpBridgePriority,
       "zyMrstpBridgeRootMaxAge": zyMrstpBridgeRootMaxAge,
       "zyMrstpBridgeRootHelloTime": zyMrstpBridgeRootHelloTime,
       "zyMrstpBridgeRootForwardDelay": zyMrstpBridgeRootForwardDelay,
       "zyxelMrstpPortTable": zyxelMrstpPortTable,
       "zyxelMrstpPortEntry": zyxelMrstpPortEntry,
       "zyMrstpPortPriority": zyMrstpPortPriority,
       "zyMrstpPortEnable": zyMrstpPortEnable,
       "zyMrstpPortPathCost": zyMrstpPortPathCost,
       "zyMrstpPortOnBridgeIndex": zyMrstpPortOnBridgeIndex,
       "zyMrstpPortAdminEdgePort": zyMrstpPortAdminEdgePort,
       "zyxelMrstpStatus": zyxelMrstpStatus,
       "zyxelMrstpBridgeInfoTable": zyxelMrstpBridgeInfoTable,
       "zyxelMrstpBridgeInfoEntry": zyxelMrstpBridgeInfoEntry,
       "zyMrstpBridgeInfoIndex": zyMrstpBridgeInfoIndex,
       "zyMrstpBridgeInfoProtocolSpecification": zyMrstpBridgeInfoProtocolSpecification,
       "zyMrstpBridgeInfoTimeSinceTopologyChange": zyMrstpBridgeInfoTimeSinceTopologyChange,
       "zyMrstpBridgeInfoTopologyChanges": zyMrstpBridgeInfoTopologyChanges,
       "zyMrstpBridgeInfoDesignatedRoot": zyMrstpBridgeInfoDesignatedRoot,
       "zyMrstpBridgeInfoRootCost": zyMrstpBridgeInfoRootCost,
       "zyMrstpBridgeInfoRootPort": zyMrstpBridgeInfoRootPort,
       "zyMrstpBridgeInfoMaxAge": zyMrstpBridgeInfoMaxAge,
       "zyMrstpBridgeInfoHelloTime": zyMrstpBridgeInfoHelloTime,
       "zyMrstpBridgeInfoHoldTime": zyMrstpBridgeInfoHoldTime,
       "zyMrstpBridgeInfoForwardDelay": zyMrstpBridgeInfoForwardDelay,
       "zyMrstpBridgeInfoRootMaxAge": zyMrstpBridgeInfoRootMaxAge,
       "zyMrstpBridgeInfoRootHelloTime": zyMrstpBridgeInfoRootHelloTime,
       "zyMrstpBridgeInfoRootForwardDelay": zyMrstpBridgeInfoRootForwardDelay,
       "zyxelMrstpPortInfoTable": zyxelMrstpPortInfoTable,
       "zyxelMrstpPortInfoEntry": zyxelMrstpPortInfoEntry,
       "zyMrstpPortInfoState": zyMrstpPortInfoState,
       "zyMrstpPortInfoDesignatedRoot": zyMrstpPortInfoDesignatedRoot,
       "zyMrstpPortInfoDesignatedCost": zyMrstpPortInfoDesignatedCost,
       "zyMrstpPortInfoDesignatedBridge": zyMrstpPortInfoDesignatedBridge,
       "zyMrstpPortInfoDesignatedPort": zyMrstpPortInfoDesignatedPort,
       "zyMrstpPortInfoForwardTransitions": zyMrstpPortInfoForwardTransitions,
       "zyMrstpPortInfoOperEdgePort": zyMrstpPortInfoOperEdgePort,
       "zyxelMrstpNotifications": zyxelMrstpNotifications,
       "zyMrstpNewRoot": zyMrstpNewRoot,
       "zyMrstpTopologyChange": zyMrstpTopologyChange}
)
