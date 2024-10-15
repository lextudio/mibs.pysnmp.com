# SNMP MIB module (CTRON-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:35 2024
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(ctBridge,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctBridge")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtBridgeStp_ObjectIdentity = ObjectIdentity
ctBridgeStp = _CtBridgeStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2)
)


class _CtBridgeStpProtocolSpecification_Type(Integer32):
    """Custom type ctBridgeStpProtocolSpecification based on Integer32"""
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
          ("none", 1))
    )


_CtBridgeStpProtocolSpecification_Type.__name__ = "Integer32"
_CtBridgeStpProtocolSpecification_Object = MibScalar
ctBridgeStpProtocolSpecification = _CtBridgeStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 1),
    _CtBridgeStpProtocolSpecification_Type()
)
ctBridgeStpProtocolSpecification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeStpProtocolSpecification.setStatus("mandatory")
_CtBridgePvst_ObjectIdentity = ObjectIdentity
ctBridgePvst = _CtBridgePvst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2)
)


class _CtPvstStpMode_Type(Integer32):
    """Custom type ctPvstStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1qMode", 1),
          ("pvstMode", 2))
    )


_CtPvstStpMode_Type.__name__ = "Integer32"
_CtPvstStpMode_Object = MibScalar
ctPvstStpMode = _CtPvstStpMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 1),
    _CtPvstStpMode_Type()
)
ctPvstStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPvstStpMode.setStatus("deprecated")


class _CtPvstMaxNumStp_Type(Integer32):
    """Custom type ctPvstMaxNumStp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CtPvstMaxNumStp_Type.__name__ = "Integer32"
_CtPvstMaxNumStp_Object = MibScalar
ctPvstMaxNumStp = _CtPvstMaxNumStp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 2),
    _CtPvstMaxNumStp_Type()
)
ctPvstMaxNumStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstMaxNumStp.setStatus("deprecated")


class _CtPvstNumStps_Type(Integer32):
    """Custom type ctPvstNumStps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CtPvstNumStps_Type.__name__ = "Integer32"
_CtPvstNumStps_Object = MibScalar
ctPvstNumStps = _CtPvstNumStps_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 3),
    _CtPvstNumStps_Type()
)
ctPvstNumStps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPvstNumStps.setStatus("deprecated")
_CtPvstLastTopologyChange_Type = TimeTicks
_CtPvstLastTopologyChange_Object = MibScalar
ctPvstLastTopologyChange = _CtPvstLastTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 4),
    _CtPvstLastTopologyChange_Type()
)
ctPvstLastTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstLastTopologyChange.setStatus("deprecated")
_CtPvstStpTable_Object = MibTable
ctPvstStpTable = _CtPvstStpTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5)
)
if mibBuilder.loadTexts:
    ctPvstStpTable.setStatus("deprecated")
_CtPvstStpEntry_Object = MibTableRow
ctPvstStpEntry = _CtPvstStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1)
)
ctPvstStpEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctPvstStpVlanId"),
)
if mibBuilder.loadTexts:
    ctPvstStpEntry.setStatus("deprecated")


class _CtPvstStpVlanId_Type(Integer32):
    """Custom type ctPvstStpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CtPvstStpVlanId_Type.__name__ = "Integer32"
_CtPvstStpVlanId_Object = MibTableColumn
ctPvstStpVlanId = _CtPvstStpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 1),
    _CtPvstStpVlanId_Type()
)
ctPvstStpVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPvstStpVlanId.setStatus("deprecated")


class _CtPvstStpProtocolSpecification_Type(Integer32):
    """Custom type ctPvstStpProtocolSpecification based on Integer32"""
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


_CtPvstStpProtocolSpecification_Type.__name__ = "Integer32"
_CtPvstStpProtocolSpecification_Object = MibTableColumn
ctPvstStpProtocolSpecification = _CtPvstStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 2),
    _CtPvstStpProtocolSpecification_Type()
)
ctPvstStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpProtocolSpecification.setStatus("deprecated")


class _CtPvstStpPriority_Type(Integer32):
    """Custom type ctPvstStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtPvstStpPriority_Type.__name__ = "Integer32"
_CtPvstStpPriority_Object = MibTableColumn
ctPvstStpPriority = _CtPvstStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 3),
    _CtPvstStpPriority_Type()
)
ctPvstStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPvstStpPriority.setStatus("deprecated")
_CtPvstStpTimeSinceTopologyChange_Type = TimeTicks
_CtPvstStpTimeSinceTopologyChange_Object = MibTableColumn
ctPvstStpTimeSinceTopologyChange = _CtPvstStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 4),
    _CtPvstStpTimeSinceTopologyChange_Type()
)
ctPvstStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpTimeSinceTopologyChange.setStatus("deprecated")
_CtPvstStpTopChanges_Type = Counter32
_CtPvstStpTopChanges_Object = MibTableColumn
ctPvstStpTopChanges = _CtPvstStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 5),
    _CtPvstStpTopChanges_Type()
)
ctPvstStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpTopChanges.setStatus("deprecated")
_CtPvstStpDesignatedRoot_Type = BridgeId
_CtPvstStpDesignatedRoot_Object = MibTableColumn
ctPvstStpDesignatedRoot = _CtPvstStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 6),
    _CtPvstStpDesignatedRoot_Type()
)
ctPvstStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpDesignatedRoot.setStatus("deprecated")
_CtPvstStpRootCost_Type = Integer32
_CtPvstStpRootCost_Object = MibTableColumn
ctPvstStpRootCost = _CtPvstStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 7),
    _CtPvstStpRootCost_Type()
)
ctPvstStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpRootCost.setStatus("deprecated")
_CtPvstStpRootPort_Type = Integer32
_CtPvstStpRootPort_Object = MibTableColumn
ctPvstStpRootPort = _CtPvstStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 8),
    _CtPvstStpRootPort_Type()
)
ctPvstStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpRootPort.setStatus("deprecated")
_CtPvstStpMaxAge_Type = Integer32
_CtPvstStpMaxAge_Object = MibTableColumn
ctPvstStpMaxAge = _CtPvstStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 9),
    _CtPvstStpMaxAge_Type()
)
ctPvstStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpMaxAge.setStatus("deprecated")
_CtPvstStpHelloTime_Type = Integer32
_CtPvstStpHelloTime_Object = MibTableColumn
ctPvstStpHelloTime = _CtPvstStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 10),
    _CtPvstStpHelloTime_Type()
)
ctPvstStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpHelloTime.setStatus("deprecated")
_CtPvstStpHoldTime_Type = Integer32
_CtPvstStpHoldTime_Object = MibTableColumn
ctPvstStpHoldTime = _CtPvstStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 11),
    _CtPvstStpHoldTime_Type()
)
ctPvstStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpHoldTime.setStatus("deprecated")
_CtPvstStpForwardDelay_Type = Integer32
_CtPvstStpForwardDelay_Object = MibTableColumn
ctPvstStpForwardDelay = _CtPvstStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 12),
    _CtPvstStpForwardDelay_Type()
)
ctPvstStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpForwardDelay.setStatus("deprecated")


class _CtPvstStpBridgeMaxAge_Type(Integer32):
    """Custom type ctPvstStpBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_CtPvstStpBridgeMaxAge_Type.__name__ = "Integer32"
_CtPvstStpBridgeMaxAge_Object = MibTableColumn
ctPvstStpBridgeMaxAge = _CtPvstStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 13),
    _CtPvstStpBridgeMaxAge_Type()
)
ctPvstStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPvstStpBridgeMaxAge.setStatus("deprecated")


class _CtPvstStpBridgeHelloTime_Type(Integer32):
    """Custom type ctPvstStpBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CtPvstStpBridgeHelloTime_Type.__name__ = "Integer32"
_CtPvstStpBridgeHelloTime_Object = MibTableColumn
ctPvstStpBridgeHelloTime = _CtPvstStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 14),
    _CtPvstStpBridgeHelloTime_Type()
)
ctPvstStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPvstStpBridgeHelloTime.setStatus("deprecated")


class _CtPvstStpBridgeForwardDelay_Type(Integer32):
    """Custom type ctPvstStpBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_CtPvstStpBridgeForwardDelay_Type.__name__ = "Integer32"
_CtPvstStpBridgeForwardDelay_Object = MibTableColumn
ctPvstStpBridgeForwardDelay = _CtPvstStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 15),
    _CtPvstStpBridgeForwardDelay_Type()
)
ctPvstStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPvstStpBridgeForwardDelay.setStatus("deprecated")
_CtPvstStpPortTable_Object = MibTable
ctPvstStpPortTable = _CtPvstStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6)
)
if mibBuilder.loadTexts:
    ctPvstStpPortTable.setStatus("deprecated")
_CtPvstStpPortEntry_Object = MibTableRow
ctPvstStpPortEntry = _CtPvstStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1)
)
ctPvstStpPortEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctPvstStpVlanId"),
    (0, "CTRON-BRIDGE-MIB", "ctPvstStpPort"),
)
if mibBuilder.loadTexts:
    ctPvstStpPortEntry.setStatus("deprecated")


class _CtPvstStpPortVlanId_Type(Integer32):
    """Custom type ctPvstStpPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CtPvstStpPortVlanId_Type.__name__ = "Integer32"
_CtPvstStpPortVlanId_Object = MibTableColumn
ctPvstStpPortVlanId = _CtPvstStpPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 1),
    _CtPvstStpPortVlanId_Type()
)
ctPvstStpPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpPortVlanId.setStatus("deprecated")


class _CtPvstStpPort_Type(Integer32):
    """Custom type ctPvstStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtPvstStpPort_Type.__name__ = "Integer32"
_CtPvstStpPort_Object = MibTableColumn
ctPvstStpPort = _CtPvstStpPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 2),
    _CtPvstStpPort_Type()
)
ctPvstStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpPort.setStatus("deprecated")


class _CtPvstStpPortPriority_Type(Integer32):
    """Custom type ctPvstStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtPvstStpPortPriority_Type.__name__ = "Integer32"
_CtPvstStpPortPriority_Object = MibTableColumn
ctPvstStpPortPriority = _CtPvstStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 3),
    _CtPvstStpPortPriority_Type()
)
ctPvstStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPvstStpPortPriority.setStatus("deprecated")


class _CtPvstStpPortState_Type(Integer32):
    """Custom type ctPvstStpPortState based on Integer32"""
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


_CtPvstStpPortState_Type.__name__ = "Integer32"
_CtPvstStpPortState_Object = MibTableColumn
ctPvstStpPortState = _CtPvstStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 4),
    _CtPvstStpPortState_Type()
)
ctPvstStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpPortState.setStatus("deprecated")


class _CtPvstStpPortEnable_Type(Integer32):
    """Custom type ctPvstStpPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtPvstStpPortEnable_Type.__name__ = "Integer32"
_CtPvstStpPortEnable_Object = MibTableColumn
ctPvstStpPortEnable = _CtPvstStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 5),
    _CtPvstStpPortEnable_Type()
)
ctPvstStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPvstStpPortEnable.setStatus("deprecated")


class _CtPvstStpPortPathCost_Type(Integer32):
    """Custom type ctPvstStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtPvstStpPortPathCost_Type.__name__ = "Integer32"
_CtPvstStpPortPathCost_Object = MibTableColumn
ctPvstStpPortPathCost = _CtPvstStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 6),
    _CtPvstStpPortPathCost_Type()
)
ctPvstStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPvstStpPortPathCost.setStatus("deprecated")
_CtPvstStpPortDesignatedRoot_Type = BridgeId
_CtPvstStpPortDesignatedRoot_Object = MibTableColumn
ctPvstStpPortDesignatedRoot = _CtPvstStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 7),
    _CtPvstStpPortDesignatedRoot_Type()
)
ctPvstStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpPortDesignatedRoot.setStatus("deprecated")
_CtPvstStpPortDesignatedCost_Type = Integer32
_CtPvstStpPortDesignatedCost_Object = MibTableColumn
ctPvstStpPortDesignatedCost = _CtPvstStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 8),
    _CtPvstStpPortDesignatedCost_Type()
)
ctPvstStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpPortDesignatedCost.setStatus("deprecated")
_CtPvstStpPortDesignatedBridge_Type = BridgeId
_CtPvstStpPortDesignatedBridge_Object = MibTableColumn
ctPvstStpPortDesignatedBridge = _CtPvstStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 9),
    _CtPvstStpPortDesignatedBridge_Type()
)
ctPvstStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpPortDesignatedBridge.setStatus("deprecated")


class _CtPvstStpPortDesignatedPort_Type(OctetString):
    """Custom type ctPvstStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CtPvstStpPortDesignatedPort_Type.__name__ = "OctetString"
_CtPvstStpPortDesignatedPort_Object = MibTableColumn
ctPvstStpPortDesignatedPort = _CtPvstStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 10),
    _CtPvstStpPortDesignatedPort_Type()
)
ctPvstStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpPortDesignatedPort.setStatus("deprecated")
_CtPvstStpPortForwardTransitions_Type = Counter32
_CtPvstStpPortForwardTransitions_Object = MibTableColumn
ctPvstStpPortForwardTransitions = _CtPvstStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 11),
    _CtPvstStpPortForwardTransitions_Type()
)
ctPvstStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPvstStpPortForwardTransitions.setStatus("deprecated")
_CtBridgeSr_ObjectIdentity = ObjectIdentity
ctBridgeSr = _CtBridgeSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3)
)
_CtBridgeSrPortPairTable_Object = MibTable
ctBridgeSrPortPairTable = _CtBridgeSrPortPairTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ctBridgeSrPortPairTable.setStatus("mandatory")
_CtBridgeSrPortPairEntry_Object = MibTableRow
ctBridgeSrPortPairEntry = _CtBridgeSrPortPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1, 1)
)
ctBridgeSrPortPairEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeSrPortPairSrcPort"),
    (0, "CTRON-BRIDGE-MIB", "ctBridgeSrPortPairDestPort"),
)
if mibBuilder.loadTexts:
    ctBridgeSrPortPairEntry.setStatus("mandatory")
_CtBridgeSrPortPairSrcPort_Type = Integer32
_CtBridgeSrPortPairSrcPort_Object = MibTableColumn
ctBridgeSrPortPairSrcPort = _CtBridgeSrPortPairSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1, 1, 1),
    _CtBridgeSrPortPairSrcPort_Type()
)
ctBridgeSrPortPairSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSrPortPairSrcPort.setStatus("mandatory")
_CtBridgeSrPortPairDestPort_Type = Integer32
_CtBridgeSrPortPairDestPort_Object = MibTableColumn
ctBridgeSrPortPairDestPort = _CtBridgeSrPortPairDestPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1, 1, 2),
    _CtBridgeSrPortPairDestPort_Type()
)
ctBridgeSrPortPairDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSrPortPairDestPort.setStatus("mandatory")
_CtBridgeSrPortPairPackets_Type = Counter32
_CtBridgeSrPortPairPackets_Object = MibTableColumn
ctBridgeSrPortPairPackets = _CtBridgeSrPortPairPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1, 1, 3),
    _CtBridgeSrPortPairPackets_Type()
)
ctBridgeSrPortPairPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSrPortPairPackets.setStatus("mandatory")


class _CtBridgeSrPortPairState_Type(Integer32):
    """Custom type ctBridgeSrPortPairState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeSrPortPairState_Type.__name__ = "Integer32"
_CtBridgeSrPortPairState_Object = MibTableColumn
ctBridgeSrPortPairState = _CtBridgeSrPortPairState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1, 1, 4),
    _CtBridgeSrPortPairState_Type()
)
ctBridgeSrPortPairState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSrPortPairState.setStatus("mandatory")


class _CtBridgeSrConfigPortType_Type(Integer32):
    """Custom type ctBridgeSrConfigPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sourcerouteonly", 2),
          ("srt", 3),
          ("transparentonly", 1))
    )


_CtBridgeSrConfigPortType_Type.__name__ = "Integer32"
_CtBridgeSrConfigPortType_Object = MibScalar
ctBridgeSrConfigPortType = _CtBridgeSrConfigPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 2),
    _CtBridgeSrConfigPortType_Type()
)
ctBridgeSrConfigPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSrConfigPortType.setStatus("mandatory")
_CtBridgeTp_ObjectIdentity = ObjectIdentity
ctBridgeTp = _CtBridgeTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4)
)
_CtBridgeTpPortPairTable_Object = MibTable
ctBridgeTpPortPairTable = _CtBridgeTpPortPairTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    ctBridgeTpPortPairTable.setStatus("mandatory")
_CtBridgeTpPortPairEntry_Object = MibTableRow
ctBridgeTpPortPairEntry = _CtBridgeTpPortPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1, 1)
)
ctBridgeTpPortPairEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeTpPortPairSrcPort"),
    (0, "CTRON-BRIDGE-MIB", "ctBridgeTpPortPairDestPort"),
)
if mibBuilder.loadTexts:
    ctBridgeTpPortPairEntry.setStatus("mandatory")
_CtBridgeTpPortPairSrcPort_Type = Integer32
_CtBridgeTpPortPairSrcPort_Object = MibTableColumn
ctBridgeTpPortPairSrcPort = _CtBridgeTpPortPairSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1, 1, 1),
    _CtBridgeTpPortPairSrcPort_Type()
)
ctBridgeTpPortPairSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeTpPortPairSrcPort.setStatus("mandatory")
_CtBridgeTpPortPairDestPort_Type = Integer32
_CtBridgeTpPortPairDestPort_Object = MibTableColumn
ctBridgeTpPortPairDestPort = _CtBridgeTpPortPairDestPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1, 1, 2),
    _CtBridgeTpPortPairDestPort_Type()
)
ctBridgeTpPortPairDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeTpPortPairDestPort.setStatus("mandatory")
_CtBridgeTpPortPairPackets_Type = Counter32
_CtBridgeTpPortPairPackets_Object = MibTableColumn
ctBridgeTpPortPairPackets = _CtBridgeTpPortPairPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1, 1, 3),
    _CtBridgeTpPortPairPackets_Type()
)
ctBridgeTpPortPairPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeTpPortPairPackets.setStatus("mandatory")


class _CtBridgeTpPortPairState_Type(Integer32):
    """Custom type ctBridgeTpPortPairState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeTpPortPairState_Type.__name__ = "Integer32"
_CtBridgeTpPortPairState_Object = MibTableColumn
ctBridgeTpPortPairState = _CtBridgeTpPortPairState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1, 1, 4),
    _CtBridgeTpPortPairState_Type()
)
ctBridgeTpPortPairState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTpPortPairState.setStatus("mandatory")
_CtBridgeSdbEnet_ObjectIdentity = ObjectIdentity
ctBridgeSdbEnet = _CtBridgeSdbEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5)
)
_CtBridgeSdbEnetTotFtrs_Type = Integer32
_CtBridgeSdbEnetTotFtrs_Object = MibScalar
ctBridgeSdbEnetTotFtrs = _CtBridgeSdbEnetTotFtrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 1),
    _CtBridgeSdbEnetTotFtrs_Type()
)
ctBridgeSdbEnetTotFtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSdbEnetTotFtrs.setStatus("mandatory")


class _CtBridgeSdbEnetNoMatch_Type(Integer32):
    """Custom type ctBridgeSdbEnetNoMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2),
          ("searchFDB", 3))
    )


_CtBridgeSdbEnetNoMatch_Type.__name__ = "Integer32"
_CtBridgeSdbEnetNoMatch_Object = MibScalar
ctBridgeSdbEnetNoMatch = _CtBridgeSdbEnetNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 2),
    _CtBridgeSdbEnetNoMatch_Type()
)
ctBridgeSdbEnetNoMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbEnetNoMatch.setStatus("mandatory")
_CtBridgeSdbEnetTable_Object = MibTable
ctBridgeSdbEnetTable = _CtBridgeSdbEnetTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3)
)
if mibBuilder.loadTexts:
    ctBridgeSdbEnetTable.setStatus("mandatory")
_CtBridgeSdbEnetEntry_Object = MibTableRow
ctBridgeSdbEnetEntry = _CtBridgeSdbEnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3, 1)
)
ctBridgeSdbEnetEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbEnetFtrNo"),
)
if mibBuilder.loadTexts:
    ctBridgeSdbEnetEntry.setStatus("mandatory")
_CtBridgeSdbEnetFtrNo_Type = Integer32
_CtBridgeSdbEnetFtrNo_Object = MibTableColumn
ctBridgeSdbEnetFtrNo = _CtBridgeSdbEnetFtrNo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3, 1, 1),
    _CtBridgeSdbEnetFtrNo_Type()
)
ctBridgeSdbEnetFtrNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSdbEnetFtrNo.setStatus("mandatory")


class _CtBridgeSdbEnetState_Type(Integer32):
    """Custom type ctBridgeSdbEnetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeSdbEnetState_Type.__name__ = "Integer32"
_CtBridgeSdbEnetState_Object = MibTableColumn
ctBridgeSdbEnetState = _CtBridgeSdbEnetState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3, 1, 2),
    _CtBridgeSdbEnetState_Type()
)
ctBridgeSdbEnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbEnetState.setStatus("mandatory")


class _CtBridgeSdbEnetFtrData_Type(DisplayString):
    """Custom type ctBridgeSdbEnetFtrData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 78),
    )


_CtBridgeSdbEnetFtrData_Type.__name__ = "DisplayString"
_CtBridgeSdbEnetFtrData_Object = MibTableColumn
ctBridgeSdbEnetFtrData = _CtBridgeSdbEnetFtrData_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3, 1, 3),
    _CtBridgeSdbEnetFtrData_Type()
)
ctBridgeSdbEnetFtrData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbEnetFtrData.setStatus("mandatory")
_CtBridgeSdbEnetDataOffset_Type = Integer32
_CtBridgeSdbEnetDataOffset_Object = MibTableColumn
ctBridgeSdbEnetDataOffset = _CtBridgeSdbEnetDataOffset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3, 1, 4),
    _CtBridgeSdbEnetDataOffset_Type()
)
ctBridgeSdbEnetDataOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbEnetDataOffset.setStatus("mandatory")
_CtBridgeSdbEnetIOTable_Object = MibTable
ctBridgeSdbEnetIOTable = _CtBridgeSdbEnetIOTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4)
)
if mibBuilder.loadTexts:
    ctBridgeSdbEnetIOTable.setStatus("mandatory")
_CtBridgeSdbEnetIOEntry_Object = MibTableRow
ctBridgeSdbEnetIOEntry = _CtBridgeSdbEnetIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4, 1)
)
ctBridgeSdbEnetIOEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbEnetIOFtrNo"),
    (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbEnetIORcvPort"),
)
if mibBuilder.loadTexts:
    ctBridgeSdbEnetIOEntry.setStatus("mandatory")
_CtBridgeSdbEnetIOFtrNo_Type = Integer32
_CtBridgeSdbEnetIOFtrNo_Object = MibTableColumn
ctBridgeSdbEnetIOFtrNo = _CtBridgeSdbEnetIOFtrNo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4, 1, 1),
    _CtBridgeSdbEnetIOFtrNo_Type()
)
ctBridgeSdbEnetIOFtrNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSdbEnetIOFtrNo.setStatus("mandatory")
_CtBridgeSdbEnetIORcvPort_Type = Integer32
_CtBridgeSdbEnetIORcvPort_Object = MibTableColumn
ctBridgeSdbEnetIORcvPort = _CtBridgeSdbEnetIORcvPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4, 1, 2),
    _CtBridgeSdbEnetIORcvPort_Type()
)
ctBridgeSdbEnetIORcvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbEnetIORcvPort.setStatus("mandatory")
_CtBridgeSdbEnetIOAllowedToGoTo_Type = OctetString
_CtBridgeSdbEnetIOAllowedToGoTo_Object = MibTableColumn
ctBridgeSdbEnetIOAllowedToGoTo = _CtBridgeSdbEnetIOAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4, 1, 3),
    _CtBridgeSdbEnetIOAllowedToGoTo_Type()
)
ctBridgeSdbEnetIOAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbEnetIOAllowedToGoTo.setStatus("mandatory")


class _CtBridgeSdbEnetIODelEntry_Type(Integer32):
    """Custom type ctBridgeSdbEnetIODelEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deleteEntry", 1)
    )


_CtBridgeSdbEnetIODelEntry_Type.__name__ = "Integer32"
_CtBridgeSdbEnetIODelEntry_Object = MibTableColumn
ctBridgeSdbEnetIODelEntry = _CtBridgeSdbEnetIODelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4, 1, 4),
    _CtBridgeSdbEnetIODelEntry_Type()
)
ctBridgeSdbEnetIODelEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbEnetIODelEntry.setStatus("mandatory")
_CtBridgeSdbTr_ObjectIdentity = ObjectIdentity
ctBridgeSdbTr = _CtBridgeSdbTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6)
)
_CtBridgeSdbTrTotFtrs_Type = Integer32
_CtBridgeSdbTrTotFtrs_Object = MibScalar
ctBridgeSdbTrTotFtrs = _CtBridgeSdbTrTotFtrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 1),
    _CtBridgeSdbTrTotFtrs_Type()
)
ctBridgeSdbTrTotFtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSdbTrTotFtrs.setStatus("mandatory")


class _CtBridgeSdbTrNoMatch_Type(Integer32):
    """Custom type ctBridgeSdbTrNoMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2),
          ("searchFDB", 3))
    )


_CtBridgeSdbTrNoMatch_Type.__name__ = "Integer32"
_CtBridgeSdbTrNoMatch_Object = MibScalar
ctBridgeSdbTrNoMatch = _CtBridgeSdbTrNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 2),
    _CtBridgeSdbTrNoMatch_Type()
)
ctBridgeSdbTrNoMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbTrNoMatch.setStatus("mandatory")
_CtBridgeSdbTrTable_Object = MibTable
ctBridgeSdbTrTable = _CtBridgeSdbTrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3)
)
if mibBuilder.loadTexts:
    ctBridgeSdbTrTable.setStatus("mandatory")
_CtBridgeSdbTrEntry_Object = MibTableRow
ctBridgeSdbTrEntry = _CtBridgeSdbTrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3, 1)
)
ctBridgeSdbTrEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbTrFtrNo"),
)
if mibBuilder.loadTexts:
    ctBridgeSdbTrEntry.setStatus("mandatory")
_CtBridgeSdbTrFtrNo_Type = Integer32
_CtBridgeSdbTrFtrNo_Object = MibTableColumn
ctBridgeSdbTrFtrNo = _CtBridgeSdbTrFtrNo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3, 1, 1),
    _CtBridgeSdbTrFtrNo_Type()
)
ctBridgeSdbTrFtrNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSdbTrFtrNo.setStatus("mandatory")


class _CtBridgeSdbTrState_Type(Integer32):
    """Custom type ctBridgeSdbTrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeSdbTrState_Type.__name__ = "Integer32"
_CtBridgeSdbTrState_Object = MibTableColumn
ctBridgeSdbTrState = _CtBridgeSdbTrState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3, 1, 2),
    _CtBridgeSdbTrState_Type()
)
ctBridgeSdbTrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbTrState.setStatus("mandatory")


class _CtBridgeSdbTrFtrData_Type(DisplayString):
    """Custom type ctBridgeSdbTrFtrData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 78),
    )


_CtBridgeSdbTrFtrData_Type.__name__ = "DisplayString"
_CtBridgeSdbTrFtrData_Object = MibTableColumn
ctBridgeSdbTrFtrData = _CtBridgeSdbTrFtrData_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3, 1, 3),
    _CtBridgeSdbTrFtrData_Type()
)
ctBridgeSdbTrFtrData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbTrFtrData.setStatus("mandatory")
_CtBridgeSdbTrDataOffset_Type = Integer32
_CtBridgeSdbTrDataOffset_Object = MibTableColumn
ctBridgeSdbTrDataOffset = _CtBridgeSdbTrDataOffset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3, 1, 4),
    _CtBridgeSdbTrDataOffset_Type()
)
ctBridgeSdbTrDataOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbTrDataOffset.setStatus("mandatory")
_CtBridgeSdbTrIOTable_Object = MibTable
ctBridgeSdbTrIOTable = _CtBridgeSdbTrIOTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4)
)
if mibBuilder.loadTexts:
    ctBridgeSdbTrIOTable.setStatus("mandatory")
_CtBridgeSdbTrIOEntry_Object = MibTableRow
ctBridgeSdbTrIOEntry = _CtBridgeSdbTrIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4, 1)
)
ctBridgeSdbTrIOEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbTrIOFtrNo"),
    (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbTrIORcvPort"),
)
if mibBuilder.loadTexts:
    ctBridgeSdbTrIOEntry.setStatus("mandatory")
_CtBridgeSdbTrIOFtrNo_Type = Integer32
_CtBridgeSdbTrIOFtrNo_Object = MibTableColumn
ctBridgeSdbTrIOFtrNo = _CtBridgeSdbTrIOFtrNo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4, 1, 1),
    _CtBridgeSdbTrIOFtrNo_Type()
)
ctBridgeSdbTrIOFtrNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSdbTrIOFtrNo.setStatus("mandatory")
_CtBridgeSdbTrIORcvPort_Type = Integer32
_CtBridgeSdbTrIORcvPort_Object = MibTableColumn
ctBridgeSdbTrIORcvPort = _CtBridgeSdbTrIORcvPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4, 1, 2),
    _CtBridgeSdbTrIORcvPort_Type()
)
ctBridgeSdbTrIORcvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbTrIORcvPort.setStatus("mandatory")
_CtBridgeSdbTrIOAllowedToGoTo_Type = OctetString
_CtBridgeSdbTrIOAllowedToGoTo_Object = MibTableColumn
ctBridgeSdbTrIOAllowedToGoTo = _CtBridgeSdbTrIOAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4, 1, 3),
    _CtBridgeSdbTrIOAllowedToGoTo_Type()
)
ctBridgeSdbTrIOAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbTrIOAllowedToGoTo.setStatus("mandatory")


class _CtBridgeSdbTrIODelEntry_Type(Integer32):
    """Custom type ctBridgeSdbTrIODelEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deleteEntry", 1)
    )


_CtBridgeSdbTrIODelEntry_Type.__name__ = "Integer32"
_CtBridgeSdbTrIODelEntry_Object = MibTableColumn
ctBridgeSdbTrIODelEntry = _CtBridgeSdbTrIODelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4, 1, 4),
    _CtBridgeSdbTrIODelEntry_Type()
)
ctBridgeSdbTrIODelEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbTrIODelEntry.setStatus("mandatory")
_CtBridgeTransTrEnet_ObjectIdentity = ObjectIdentity
ctBridgeTransTrEnet = _CtBridgeTransTrEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7)
)


class _CtBridgeTransTrEnetAutoMode_Type(Integer32):
    """Custom type ctBridgeTransTrEnetAutoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeTransTrEnetAutoMode_Type.__name__ = "Integer32"
_CtBridgeTransTrEnetAutoMode_Object = MibScalar
ctBridgeTransTrEnetAutoMode = _CtBridgeTransTrEnetAutoMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 1),
    _CtBridgeTransTrEnetAutoMode_Type()
)
ctBridgeTransTrEnetAutoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetAutoMode.setStatus("mandatory")


class _CtBridgeTransTrEnetDualMode_Type(Integer32):
    """Custom type ctBridgeTransTrEnetDualMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeTransTrEnetDualMode_Type.__name__ = "Integer32"
_CtBridgeTransTrEnetDualMode_Object = MibScalar
ctBridgeTransTrEnetDualMode = _CtBridgeTransTrEnetDualMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 2),
    _CtBridgeTransTrEnetDualMode_Type()
)
ctBridgeTransTrEnetDualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetDualMode.setStatus("mandatory")


class _CtBridgeTransTrEnetNovell_Type(Integer32):
    """Custom type ctBridgeTransTrEnetNovell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8023snap", 2))
    )


_CtBridgeTransTrEnetNovell_Type.__name__ = "Integer32"
_CtBridgeTransTrEnetNovell_Object = MibScalar
ctBridgeTransTrEnetNovell = _CtBridgeTransTrEnetNovell_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 3),
    _CtBridgeTransTrEnetNovell_Type()
)
ctBridgeTransTrEnetNovell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetNovell.setStatus("mandatory")


class _CtBridgeTransTrEnetIP_Type(Integer32):
    """Custom type ctBridgeTransTrEnetIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8023snap", 2))
    )


_CtBridgeTransTrEnetIP_Type.__name__ = "Integer32"
_CtBridgeTransTrEnetIP_Object = MibScalar
ctBridgeTransTrEnetIP = _CtBridgeTransTrEnetIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 4),
    _CtBridgeTransTrEnetIP_Type()
)
ctBridgeTransTrEnetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetIP.setStatus("mandatory")


class _CtBridgeTransTrEnetAARP_Type(Integer32):
    """Custom type ctBridgeTransTrEnetAARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8023snap", 2))
    )


_CtBridgeTransTrEnetAARP_Type.__name__ = "Integer32"
_CtBridgeTransTrEnetAARP_Object = MibScalar
ctBridgeTransTrEnetAARP = _CtBridgeTransTrEnetAARP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 5),
    _CtBridgeTransTrEnetAARP_Type()
)
ctBridgeTransTrEnetAARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetAARP.setStatus("mandatory")


class _CtBridgeTransTrEnetNovAdd_Type(Integer32):
    """Custom type ctBridgeTransTrEnetNovAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lsb", 2),
          ("msb", 1))
    )


_CtBridgeTransTrEnetNovAdd_Type.__name__ = "Integer32"
_CtBridgeTransTrEnetNovAdd_Object = MibScalar
ctBridgeTransTrEnetNovAdd = _CtBridgeTransTrEnetNovAdd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 6),
    _CtBridgeTransTrEnetNovAdd_Type()
)
ctBridgeTransTrEnetNovAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetNovAdd.setStatus("mandatory")
_CtBridgeTransTrEnetIBMTable_Object = MibTable
ctBridgeTransTrEnetIBMTable = _CtBridgeTransTrEnetIBMTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 7)
)
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetIBMTable.setStatus("mandatory")
_CtBridgeTransTrEnetIBMEntry_Object = MibTableRow
ctBridgeTransTrEnetIBMEntry = _CtBridgeTransTrEnetIBMEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 7, 1)
)
ctBridgeTransTrEnetIBMEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeTransTrEnetIBMIndex"),
)
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetIBMEntry.setStatus("mandatory")
_CtBridgeTransTrEnetIBMIndex_Type = Integer32
_CtBridgeTransTrEnetIBMIndex_Object = MibTableColumn
ctBridgeTransTrEnetIBMIndex = _CtBridgeTransTrEnetIBMIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 7, 1, 1),
    _CtBridgeTransTrEnetIBMIndex_Type()
)
ctBridgeTransTrEnetIBMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetIBMIndex.setStatus("mandatory")
_CtBridgeTransTrEnetIBMSap_Type = OctetString
_CtBridgeTransTrEnetIBMSap_Object = MibTableColumn
ctBridgeTransTrEnetIBMSap = _CtBridgeTransTrEnetIBMSap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 7, 1, 2),
    _CtBridgeTransTrEnetIBMSap_Type()
)
ctBridgeTransTrEnetIBMSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetIBMSap.setStatus("mandatory")


class _CtBridgeTransTrEnetIBMState_Type(Integer32):
    """Custom type ctBridgeTransTrEnetIBMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeTransTrEnetIBMState_Type.__name__ = "Integer32"
_CtBridgeTransTrEnetIBMState_Object = MibTableColumn
ctBridgeTransTrEnetIBMState = _CtBridgeTransTrEnetIBMState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 7, 1, 3),
    _CtBridgeTransTrEnetIBMState_Type()
)
ctBridgeTransTrEnetIBMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetIBMState.setStatus("mandatory")


class _CtBridgeTransTrEnetSnapFormat_Type(Integer32):
    """Custom type ctBridgeTransTrEnetSnapFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8023snap", 2))
    )


_CtBridgeTransTrEnetSnapFormat_Type.__name__ = "Integer32"
_CtBridgeTransTrEnetSnapFormat_Object = MibScalar
ctBridgeTransTrEnetSnapFormat = _CtBridgeTransTrEnetSnapFormat_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 8),
    _CtBridgeTransTrEnetSnapFormat_Type()
)
ctBridgeTransTrEnetSnapFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetSnapFormat.setStatus("mandatory")
_CtBridgeTransTrEnetSnapTable_Object = MibTable
ctBridgeTransTrEnetSnapTable = _CtBridgeTransTrEnetSnapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 9)
)
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetSnapTable.setStatus("mandatory")
_CtBridgeTransTrEnetSnapEntry_Object = MibTableRow
ctBridgeTransTrEnetSnapEntry = _CtBridgeTransTrEnetSnapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 9, 1)
)
ctBridgeTransTrEnetSnapEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeTransTrEnetSnapIndex"),
)
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetSnapEntry.setStatus("mandatory")
_CtBridgeTransTrEnetSnapIndex_Type = Integer32
_CtBridgeTransTrEnetSnapIndex_Object = MibTableColumn
ctBridgeTransTrEnetSnapIndex = _CtBridgeTransTrEnetSnapIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 9, 1, 1),
    _CtBridgeTransTrEnetSnapIndex_Type()
)
ctBridgeTransTrEnetSnapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetSnapIndex.setStatus("mandatory")
_CtBridgeTransTrEnetSnapType_Type = OctetString
_CtBridgeTransTrEnetSnapType_Object = MibTableColumn
ctBridgeTransTrEnetSnapType = _CtBridgeTransTrEnetSnapType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 9, 1, 2),
    _CtBridgeTransTrEnetSnapType_Type()
)
ctBridgeTransTrEnetSnapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetSnapType.setStatus("mandatory")


class _CtBridgeTransTrEnetSnapState_Type(Integer32):
    """Custom type ctBridgeTransTrEnetSnapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeTransTrEnetSnapState_Type.__name__ = "Integer32"
_CtBridgeTransTrEnetSnapState_Object = MibTableColumn
ctBridgeTransTrEnetSnapState = _CtBridgeTransTrEnetSnapState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 9, 1, 3),
    _CtBridgeTransTrEnetSnapState_Type()
)
ctBridgeTransTrEnetSnapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeTransTrEnetSnapState.setStatus("mandatory")
_CtBridgeExtendedControl_ObjectIdentity = ObjectIdentity
ctBridgeExtendedControl = _CtBridgeExtendedControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 8)
)


class _CtBridgeBaseChassisMgr_Type(Integer32):
    """Custom type ctBridgeBaseChassisMgr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("managementDisabled", 2),
          ("managementEnabled", 3),
          ("notSupported", 1))
    )


_CtBridgeBaseChassisMgr_Type.__name__ = "Integer32"
_CtBridgeBaseChassisMgr_Object = MibScalar
ctBridgeBaseChassisMgr = _CtBridgeBaseChassisMgr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 8, 1),
    _CtBridgeBaseChassisMgr_Type()
)
ctBridgeBaseChassisMgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeBaseChassisMgr.setStatus("mandatory")
_CtBridgeSdbGeneric_ObjectIdentity = ObjectIdentity
ctBridgeSdbGeneric = _CtBridgeSdbGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9)
)
_CtBridgeSdbGenericTotFtrs_Type = Integer32
_CtBridgeSdbGenericTotFtrs_Object = MibScalar
ctBridgeSdbGenericTotFtrs = _CtBridgeSdbGenericTotFtrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 1),
    _CtBridgeSdbGenericTotFtrs_Type()
)
ctBridgeSdbGenericTotFtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSdbGenericTotFtrs.setStatus("mandatory")


class _CtBridgeSdbGenericNoMatch_Type(Integer32):
    """Custom type ctBridgeSdbGenericNoMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("forward", 2),
          ("searchFDB", 3))
    )


_CtBridgeSdbGenericNoMatch_Type.__name__ = "Integer32"
_CtBridgeSdbGenericNoMatch_Object = MibScalar
ctBridgeSdbGenericNoMatch = _CtBridgeSdbGenericNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 2),
    _CtBridgeSdbGenericNoMatch_Type()
)
ctBridgeSdbGenericNoMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbGenericNoMatch.setStatus("mandatory")
_CtBridgeSdbGenericTable_Object = MibTable
ctBridgeSdbGenericTable = _CtBridgeSdbGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3)
)
if mibBuilder.loadTexts:
    ctBridgeSdbGenericTable.setStatus("mandatory")
_CtBridgeSdbGenericEntry_Object = MibTableRow
ctBridgeSdbGenericEntry = _CtBridgeSdbGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1)
)
ctBridgeSdbGenericEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbGenericFtrNo"),
)
if mibBuilder.loadTexts:
    ctBridgeSdbGenericEntry.setStatus("mandatory")
_CtBridgeSdbGenericFtrNo_Type = Integer32
_CtBridgeSdbGenericFtrNo_Object = MibTableColumn
ctBridgeSdbGenericFtrNo = _CtBridgeSdbGenericFtrNo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1, 1),
    _CtBridgeSdbGenericFtrNo_Type()
)
ctBridgeSdbGenericFtrNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSdbGenericFtrNo.setStatus("mandatory")


class _CtBridgeSdbGenericState_Type(Integer32):
    """Custom type ctBridgeSdbGenericState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeSdbGenericState_Type.__name__ = "Integer32"
_CtBridgeSdbGenericState_Object = MibTableColumn
ctBridgeSdbGenericState = _CtBridgeSdbGenericState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1, 2),
    _CtBridgeSdbGenericState_Type()
)
ctBridgeSdbGenericState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbGenericState.setStatus("mandatory")


class _CtBridgeSdbGenericFtrData_Type(DisplayString):
    """Custom type ctBridgeSdbGenericFtrData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 78),
    )


_CtBridgeSdbGenericFtrData_Type.__name__ = "DisplayString"
_CtBridgeSdbGenericFtrData_Object = MibTableColumn
ctBridgeSdbGenericFtrData = _CtBridgeSdbGenericFtrData_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1, 3),
    _CtBridgeSdbGenericFtrData_Type()
)
ctBridgeSdbGenericFtrData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbGenericFtrData.setStatus("mandatory")
_CtBridgeSdbGenericDataOffset_Type = Integer32
_CtBridgeSdbGenericDataOffset_Object = MibTableColumn
ctBridgeSdbGenericDataOffset = _CtBridgeSdbGenericDataOffset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1, 4),
    _CtBridgeSdbGenericDataOffset_Type()
)
ctBridgeSdbGenericDataOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbGenericDataOffset.setStatus("mandatory")
_CtBridgeSdbGenericFilterType_Type = Integer32
_CtBridgeSdbGenericFilterType_Object = MibTableColumn
ctBridgeSdbGenericFilterType = _CtBridgeSdbGenericFilterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1, 5),
    _CtBridgeSdbGenericFilterType_Type()
)
ctBridgeSdbGenericFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbGenericFilterType.setStatus("mandatory")
_CtBridgeSdbGenericIOTable_Object = MibTable
ctBridgeSdbGenericIOTable = _CtBridgeSdbGenericIOTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4)
)
if mibBuilder.loadTexts:
    ctBridgeSdbGenericIOTable.setStatus("mandatory")
_CtBridgeSdbGenericIOEntry_Object = MibTableRow
ctBridgeSdbGenericIOEntry = _CtBridgeSdbGenericIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4, 1)
)
ctBridgeSdbGenericIOEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbGenericIOFtrNo"),
    (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbGenericIORcvPort"),
)
if mibBuilder.loadTexts:
    ctBridgeSdbGenericIOEntry.setStatus("mandatory")
_CtBridgeSdbGenericIOFtrNo_Type = Integer32
_CtBridgeSdbGenericIOFtrNo_Object = MibTableColumn
ctBridgeSdbGenericIOFtrNo = _CtBridgeSdbGenericIOFtrNo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4, 1, 1),
    _CtBridgeSdbGenericIOFtrNo_Type()
)
ctBridgeSdbGenericIOFtrNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeSdbGenericIOFtrNo.setStatus("mandatory")
_CtBridgeSdbGenericIORcvPort_Type = Integer32
_CtBridgeSdbGenericIORcvPort_Object = MibTableColumn
ctBridgeSdbGenericIORcvPort = _CtBridgeSdbGenericIORcvPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4, 1, 2),
    _CtBridgeSdbGenericIORcvPort_Type()
)
ctBridgeSdbGenericIORcvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbGenericIORcvPort.setStatus("mandatory")
_CtBridgeSdbGenericIOAllowedToGoTo_Type = OctetString
_CtBridgeSdbGenericIOAllowedToGoTo_Object = MibTableColumn
ctBridgeSdbGenericIOAllowedToGoTo = _CtBridgeSdbGenericIOAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4, 1, 3),
    _CtBridgeSdbGenericIOAllowedToGoTo_Type()
)
ctBridgeSdbGenericIOAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbGenericIOAllowedToGoTo.setStatus("mandatory")


class _CtBridgeSdbGenericIODelEntry_Type(Integer32):
    """Custom type ctBridgeSdbGenericIODelEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deleteEntry", 1)
    )


_CtBridgeSdbGenericIODelEntry_Type.__name__ = "Integer32"
_CtBridgeSdbGenericIODelEntry_Object = MibTableColumn
ctBridgeSdbGenericIODelEntry = _CtBridgeSdbGenericIODelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4, 1, 4),
    _CtBridgeSdbGenericIODelEntry_Type()
)
ctBridgeSdbGenericIODelEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeSdbGenericIODelEntry.setStatus("mandatory")
_CtBridgeLoadShare_ObjectIdentity = ObjectIdentity
ctBridgeLoadShare = _CtBridgeLoadShare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10)
)
_CtBridgeLoadShareInstanceTable_Object = MibTable
ctBridgeLoadShareInstanceTable = _CtBridgeLoadShareInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 1)
)
if mibBuilder.loadTexts:
    ctBridgeLoadShareInstanceTable.setStatus("mandatory")
_CtBridgeLoadShareInstanceEntry_Object = MibTableRow
ctBridgeLoadShareInstanceEntry = _CtBridgeLoadShareInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 1, 1)
)
ctBridgeLoadShareInstanceEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeLoadShareInstanceId"),
)
if mibBuilder.loadTexts:
    ctBridgeLoadShareInstanceEntry.setStatus("mandatory")
_CtBridgeLoadShareInstanceId_Type = Integer32
_CtBridgeLoadShareInstanceId_Object = MibTableColumn
ctBridgeLoadShareInstanceId = _CtBridgeLoadShareInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 1, 1, 1),
    _CtBridgeLoadShareInstanceId_Type()
)
ctBridgeLoadShareInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeLoadShareInstanceId.setStatus("mandatory")


class _CtBridgeLoadShareAdminStatus_Type(Integer32):
    """Custom type ctBridgeLoadShareAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeLoadShareAdminStatus_Type.__name__ = "Integer32"
_CtBridgeLoadShareAdminStatus_Object = MibTableColumn
ctBridgeLoadShareAdminStatus = _CtBridgeLoadShareAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 1, 1, 2),
    _CtBridgeLoadShareAdminStatus_Type()
)
ctBridgeLoadShareAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeLoadShareAdminStatus.setStatus("mandatory")


class _CtBridgeLoadShareOperStatus_Type(Integer32):
    """Custom type ctBridgeLoadShareOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeLoadShareOperStatus_Type.__name__ = "Integer32"
_CtBridgeLoadShareOperStatus_Object = MibTableColumn
ctBridgeLoadShareOperStatus = _CtBridgeLoadShareOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 1, 1, 3),
    _CtBridgeLoadShareOperStatus_Type()
)
ctBridgeLoadShareOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeLoadShareOperStatus.setStatus("mandatory")
_CtBridgeLoadSharePortTable_Object = MibTable
ctBridgeLoadSharePortTable = _CtBridgeLoadSharePortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2)
)
if mibBuilder.loadTexts:
    ctBridgeLoadSharePortTable.setStatus("mandatory")
_CtBridgeLoadSharePortEntry_Object = MibTableRow
ctBridgeLoadSharePortEntry = _CtBridgeLoadSharePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1)
)
ctBridgeLoadSharePortEntry.setIndexNames(
    (0, "CTRON-BRIDGE-MIB", "ctBridgeLoadSharePortInstanceId"),
    (0, "CTRON-BRIDGE-MIB", "ctBridgeLoadSharePortNum"),
)
if mibBuilder.loadTexts:
    ctBridgeLoadSharePortEntry.setStatus("mandatory")
_CtBridgeLoadSharePortNum_Type = Integer32
_CtBridgeLoadSharePortNum_Object = MibTableColumn
ctBridgeLoadSharePortNum = _CtBridgeLoadSharePortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 1),
    _CtBridgeLoadSharePortNum_Type()
)
ctBridgeLoadSharePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeLoadSharePortNum.setStatus("mandatory")
_CtBridgeLoadSharePortInstanceId_Type = Integer32
_CtBridgeLoadSharePortInstanceId_Object = MibTableColumn
ctBridgeLoadSharePortInstanceId = _CtBridgeLoadSharePortInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 2),
    _CtBridgeLoadSharePortInstanceId_Type()
)
ctBridgeLoadSharePortInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeLoadSharePortInstanceId.setStatus("mandatory")


class _CtBridgeLoadSharePortAdminStatus_Type(Integer32):
    """Custom type ctBridgeLoadSharePortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeLoadSharePortAdminStatus_Type.__name__ = "Integer32"
_CtBridgeLoadSharePortAdminStatus_Object = MibTableColumn
ctBridgeLoadSharePortAdminStatus = _CtBridgeLoadSharePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 3),
    _CtBridgeLoadSharePortAdminStatus_Type()
)
ctBridgeLoadSharePortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBridgeLoadSharePortAdminStatus.setStatus("mandatory")


class _CtBridgeLoadSharePortOperStatus_Type(Integer32):
    """Custom type ctBridgeLoadSharePortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtBridgeLoadSharePortOperStatus_Type.__name__ = "Integer32"
_CtBridgeLoadSharePortOperStatus_Object = MibTableColumn
ctBridgeLoadSharePortOperStatus = _CtBridgeLoadSharePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 4),
    _CtBridgeLoadSharePortOperStatus_Type()
)
ctBridgeLoadSharePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeLoadSharePortOperStatus.setStatus("mandatory")
_CtBridgeLoadSharePortForwardMask_Type = Integer32
_CtBridgeLoadSharePortForwardMask_Object = MibTableColumn
ctBridgeLoadSharePortForwardMask = _CtBridgeLoadSharePortForwardMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 5),
    _CtBridgeLoadSharePortForwardMask_Type()
)
ctBridgeLoadSharePortForwardMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeLoadSharePortForwardMask.setStatus("mandatory")
_CtBridgeLoadSharePortForwardInstance_Type = Integer32
_CtBridgeLoadSharePortForwardInstance_Object = MibTableColumn
ctBridgeLoadSharePortForwardInstance = _CtBridgeLoadSharePortForwardInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 6),
    _CtBridgeLoadSharePortForwardInstance_Type()
)
ctBridgeLoadSharePortForwardInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeLoadSharePortForwardInstance.setStatus("mandatory")
_CtBridgeLoadSharePortNumPorts_Type = Integer32
_CtBridgeLoadSharePortNumPorts_Object = MibTableColumn
ctBridgeLoadSharePortNumPorts = _CtBridgeLoadSharePortNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 7),
    _CtBridgeLoadSharePortNumPorts_Type()
)
ctBridgeLoadSharePortNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBridgeLoadSharePortNumPorts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-BRIDGE-MIB",
    **{"ctBridgeStp": ctBridgeStp,
       "ctBridgeStpProtocolSpecification": ctBridgeStpProtocolSpecification,
       "ctBridgePvst": ctBridgePvst,
       "ctPvstStpMode": ctPvstStpMode,
       "ctPvstMaxNumStp": ctPvstMaxNumStp,
       "ctPvstNumStps": ctPvstNumStps,
       "ctPvstLastTopologyChange": ctPvstLastTopologyChange,
       "ctPvstStpTable": ctPvstStpTable,
       "ctPvstStpEntry": ctPvstStpEntry,
       "ctPvstStpVlanId": ctPvstStpVlanId,
       "ctPvstStpProtocolSpecification": ctPvstStpProtocolSpecification,
       "ctPvstStpPriority": ctPvstStpPriority,
       "ctPvstStpTimeSinceTopologyChange": ctPvstStpTimeSinceTopologyChange,
       "ctPvstStpTopChanges": ctPvstStpTopChanges,
       "ctPvstStpDesignatedRoot": ctPvstStpDesignatedRoot,
       "ctPvstStpRootCost": ctPvstStpRootCost,
       "ctPvstStpRootPort": ctPvstStpRootPort,
       "ctPvstStpMaxAge": ctPvstStpMaxAge,
       "ctPvstStpHelloTime": ctPvstStpHelloTime,
       "ctPvstStpHoldTime": ctPvstStpHoldTime,
       "ctPvstStpForwardDelay": ctPvstStpForwardDelay,
       "ctPvstStpBridgeMaxAge": ctPvstStpBridgeMaxAge,
       "ctPvstStpBridgeHelloTime": ctPvstStpBridgeHelloTime,
       "ctPvstStpBridgeForwardDelay": ctPvstStpBridgeForwardDelay,
       "ctPvstStpPortTable": ctPvstStpPortTable,
       "ctPvstStpPortEntry": ctPvstStpPortEntry,
       "ctPvstStpPortVlanId": ctPvstStpPortVlanId,
       "ctPvstStpPort": ctPvstStpPort,
       "ctPvstStpPortPriority": ctPvstStpPortPriority,
       "ctPvstStpPortState": ctPvstStpPortState,
       "ctPvstStpPortEnable": ctPvstStpPortEnable,
       "ctPvstStpPortPathCost": ctPvstStpPortPathCost,
       "ctPvstStpPortDesignatedRoot": ctPvstStpPortDesignatedRoot,
       "ctPvstStpPortDesignatedCost": ctPvstStpPortDesignatedCost,
       "ctPvstStpPortDesignatedBridge": ctPvstStpPortDesignatedBridge,
       "ctPvstStpPortDesignatedPort": ctPvstStpPortDesignatedPort,
       "ctPvstStpPortForwardTransitions": ctPvstStpPortForwardTransitions,
       "ctBridgeSr": ctBridgeSr,
       "ctBridgeSrPortPairTable": ctBridgeSrPortPairTable,
       "ctBridgeSrPortPairEntry": ctBridgeSrPortPairEntry,
       "ctBridgeSrPortPairSrcPort": ctBridgeSrPortPairSrcPort,
       "ctBridgeSrPortPairDestPort": ctBridgeSrPortPairDestPort,
       "ctBridgeSrPortPairPackets": ctBridgeSrPortPairPackets,
       "ctBridgeSrPortPairState": ctBridgeSrPortPairState,
       "ctBridgeSrConfigPortType": ctBridgeSrConfigPortType,
       "ctBridgeTp": ctBridgeTp,
       "ctBridgeTpPortPairTable": ctBridgeTpPortPairTable,
       "ctBridgeTpPortPairEntry": ctBridgeTpPortPairEntry,
       "ctBridgeTpPortPairSrcPort": ctBridgeTpPortPairSrcPort,
       "ctBridgeTpPortPairDestPort": ctBridgeTpPortPairDestPort,
       "ctBridgeTpPortPairPackets": ctBridgeTpPortPairPackets,
       "ctBridgeTpPortPairState": ctBridgeTpPortPairState,
       "ctBridgeSdbEnet": ctBridgeSdbEnet,
       "ctBridgeSdbEnetTotFtrs": ctBridgeSdbEnetTotFtrs,
       "ctBridgeSdbEnetNoMatch": ctBridgeSdbEnetNoMatch,
       "ctBridgeSdbEnetTable": ctBridgeSdbEnetTable,
       "ctBridgeSdbEnetEntry": ctBridgeSdbEnetEntry,
       "ctBridgeSdbEnetFtrNo": ctBridgeSdbEnetFtrNo,
       "ctBridgeSdbEnetState": ctBridgeSdbEnetState,
       "ctBridgeSdbEnetFtrData": ctBridgeSdbEnetFtrData,
       "ctBridgeSdbEnetDataOffset": ctBridgeSdbEnetDataOffset,
       "ctBridgeSdbEnetIOTable": ctBridgeSdbEnetIOTable,
       "ctBridgeSdbEnetIOEntry": ctBridgeSdbEnetIOEntry,
       "ctBridgeSdbEnetIOFtrNo": ctBridgeSdbEnetIOFtrNo,
       "ctBridgeSdbEnetIORcvPort": ctBridgeSdbEnetIORcvPort,
       "ctBridgeSdbEnetIOAllowedToGoTo": ctBridgeSdbEnetIOAllowedToGoTo,
       "ctBridgeSdbEnetIODelEntry": ctBridgeSdbEnetIODelEntry,
       "ctBridgeSdbTr": ctBridgeSdbTr,
       "ctBridgeSdbTrTotFtrs": ctBridgeSdbTrTotFtrs,
       "ctBridgeSdbTrNoMatch": ctBridgeSdbTrNoMatch,
       "ctBridgeSdbTrTable": ctBridgeSdbTrTable,
       "ctBridgeSdbTrEntry": ctBridgeSdbTrEntry,
       "ctBridgeSdbTrFtrNo": ctBridgeSdbTrFtrNo,
       "ctBridgeSdbTrState": ctBridgeSdbTrState,
       "ctBridgeSdbTrFtrData": ctBridgeSdbTrFtrData,
       "ctBridgeSdbTrDataOffset": ctBridgeSdbTrDataOffset,
       "ctBridgeSdbTrIOTable": ctBridgeSdbTrIOTable,
       "ctBridgeSdbTrIOEntry": ctBridgeSdbTrIOEntry,
       "ctBridgeSdbTrIOFtrNo": ctBridgeSdbTrIOFtrNo,
       "ctBridgeSdbTrIORcvPort": ctBridgeSdbTrIORcvPort,
       "ctBridgeSdbTrIOAllowedToGoTo": ctBridgeSdbTrIOAllowedToGoTo,
       "ctBridgeSdbTrIODelEntry": ctBridgeSdbTrIODelEntry,
       "ctBridgeTransTrEnet": ctBridgeTransTrEnet,
       "ctBridgeTransTrEnetAutoMode": ctBridgeTransTrEnetAutoMode,
       "ctBridgeTransTrEnetDualMode": ctBridgeTransTrEnetDualMode,
       "ctBridgeTransTrEnetNovell": ctBridgeTransTrEnetNovell,
       "ctBridgeTransTrEnetIP": ctBridgeTransTrEnetIP,
       "ctBridgeTransTrEnetAARP": ctBridgeTransTrEnetAARP,
       "ctBridgeTransTrEnetNovAdd": ctBridgeTransTrEnetNovAdd,
       "ctBridgeTransTrEnetIBMTable": ctBridgeTransTrEnetIBMTable,
       "ctBridgeTransTrEnetIBMEntry": ctBridgeTransTrEnetIBMEntry,
       "ctBridgeTransTrEnetIBMIndex": ctBridgeTransTrEnetIBMIndex,
       "ctBridgeTransTrEnetIBMSap": ctBridgeTransTrEnetIBMSap,
       "ctBridgeTransTrEnetIBMState": ctBridgeTransTrEnetIBMState,
       "ctBridgeTransTrEnetSnapFormat": ctBridgeTransTrEnetSnapFormat,
       "ctBridgeTransTrEnetSnapTable": ctBridgeTransTrEnetSnapTable,
       "ctBridgeTransTrEnetSnapEntry": ctBridgeTransTrEnetSnapEntry,
       "ctBridgeTransTrEnetSnapIndex": ctBridgeTransTrEnetSnapIndex,
       "ctBridgeTransTrEnetSnapType": ctBridgeTransTrEnetSnapType,
       "ctBridgeTransTrEnetSnapState": ctBridgeTransTrEnetSnapState,
       "ctBridgeExtendedControl": ctBridgeExtendedControl,
       "ctBridgeBaseChassisMgr": ctBridgeBaseChassisMgr,
       "ctBridgeSdbGeneric": ctBridgeSdbGeneric,
       "ctBridgeSdbGenericTotFtrs": ctBridgeSdbGenericTotFtrs,
       "ctBridgeSdbGenericNoMatch": ctBridgeSdbGenericNoMatch,
       "ctBridgeSdbGenericTable": ctBridgeSdbGenericTable,
       "ctBridgeSdbGenericEntry": ctBridgeSdbGenericEntry,
       "ctBridgeSdbGenericFtrNo": ctBridgeSdbGenericFtrNo,
       "ctBridgeSdbGenericState": ctBridgeSdbGenericState,
       "ctBridgeSdbGenericFtrData": ctBridgeSdbGenericFtrData,
       "ctBridgeSdbGenericDataOffset": ctBridgeSdbGenericDataOffset,
       "ctBridgeSdbGenericFilterType": ctBridgeSdbGenericFilterType,
       "ctBridgeSdbGenericIOTable": ctBridgeSdbGenericIOTable,
       "ctBridgeSdbGenericIOEntry": ctBridgeSdbGenericIOEntry,
       "ctBridgeSdbGenericIOFtrNo": ctBridgeSdbGenericIOFtrNo,
       "ctBridgeSdbGenericIORcvPort": ctBridgeSdbGenericIORcvPort,
       "ctBridgeSdbGenericIOAllowedToGoTo": ctBridgeSdbGenericIOAllowedToGoTo,
       "ctBridgeSdbGenericIODelEntry": ctBridgeSdbGenericIODelEntry,
       "ctBridgeLoadShare": ctBridgeLoadShare,
       "ctBridgeLoadShareInstanceTable": ctBridgeLoadShareInstanceTable,
       "ctBridgeLoadShareInstanceEntry": ctBridgeLoadShareInstanceEntry,
       "ctBridgeLoadShareInstanceId": ctBridgeLoadShareInstanceId,
       "ctBridgeLoadShareAdminStatus": ctBridgeLoadShareAdminStatus,
       "ctBridgeLoadShareOperStatus": ctBridgeLoadShareOperStatus,
       "ctBridgeLoadSharePortTable": ctBridgeLoadSharePortTable,
       "ctBridgeLoadSharePortEntry": ctBridgeLoadSharePortEntry,
       "ctBridgeLoadSharePortNum": ctBridgeLoadSharePortNum,
       "ctBridgeLoadSharePortInstanceId": ctBridgeLoadSharePortInstanceId,
       "ctBridgeLoadSharePortAdminStatus": ctBridgeLoadSharePortAdminStatus,
       "ctBridgeLoadSharePortOperStatus": ctBridgeLoadSharePortOperStatus,
       "ctBridgeLoadSharePortForwardMask": ctBridgeLoadSharePortForwardMask,
       "ctBridgeLoadSharePortForwardInstance": ctBridgeLoadSharePortForwardInstance,
       "ctBridgeLoadSharePortNumPorts": ctBridgeLoadSharePortNumPorts}
)
