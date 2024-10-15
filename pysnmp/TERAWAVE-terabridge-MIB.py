# SNMP MIB module (TERAWAVE-terabridge-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-terabridge-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:22 2024
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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_Tera1dBridge_ObjectIdentity = ObjectIdentity
tera1dBridge = _Tera1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 3)
)
_TeraDot1dStpTable_Object = MibTable
teraDot1dStpTable = _TeraDot1dStpTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1)
)
if mibBuilder.loadTexts:
    teraDot1dStpTable.setStatus("mandatory")
_TeraDot1dStpTableEntry_Object = MibTableRow
teraDot1dStpTableEntry = _TeraDot1dStpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1)
)
teraDot1dStpTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "teraStpId"),
)
if mibBuilder.loadTexts:
    teraDot1dStpTableEntry.setStatus("mandatory")


class _TeraStpId_Type(Integer32):
    """Custom type teraStpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TeraStpId_Type.__name__ = "Integer32"
_TeraStpId_Object = MibTableColumn
teraStpId = _TeraStpId_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 1),
    _TeraStpId_Type()
)
teraStpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraStpId.setStatus("mandatory")


class _TeraDot1dStpProtocolSpecification_Type(Integer32):
    """Custom type teraDot1dStpProtocolSpecification based on Integer32"""
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


_TeraDot1dStpProtocolSpecification_Type.__name__ = "Integer32"
_TeraDot1dStpProtocolSpecification_Object = MibTableColumn
teraDot1dStpProtocolSpecification = _TeraDot1dStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 2),
    _TeraDot1dStpProtocolSpecification_Type()
)
teraDot1dStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStpProtocolSpecification.setStatus("mandatory")


class _TeraDot1dStpPriority_Type(Integer32):
    """Custom type teraDot1dStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TeraDot1dStpPriority_Type.__name__ = "Integer32"
_TeraDot1dStpPriority_Object = MibTableColumn
teraDot1dStpPriority = _TeraDot1dStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 3),
    _TeraDot1dStpPriority_Type()
)
teraDot1dStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dStpPriority.setStatus("mandatory")
_TeraDot1dStpTimeSinceTopologyChange_Type = TimeTicks
_TeraDot1dStpTimeSinceTopologyChange_Object = MibTableColumn
teraDot1dStpTimeSinceTopologyChange = _TeraDot1dStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 4),
    _TeraDot1dStpTimeSinceTopologyChange_Type()
)
teraDot1dStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStpTimeSinceTopologyChange.setStatus("mandatory")
_TeraDot1dStpTopChanges_Type = Counter32
_TeraDot1dStpTopChanges_Object = MibTableColumn
teraDot1dStpTopChanges = _TeraDot1dStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 5),
    _TeraDot1dStpTopChanges_Type()
)
teraDot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStpTopChanges.setStatus("mandatory")
_TeraDot1dStpDesignatedRoot_Type = OctetString
_TeraDot1dStpDesignatedRoot_Object = MibTableColumn
teraDot1dStpDesignatedRoot = _TeraDot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 6),
    _TeraDot1dStpDesignatedRoot_Type()
)
teraDot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStpDesignatedRoot.setStatus("mandatory")
_TeraDot1dStpRootCost_Type = Integer32
_TeraDot1dStpRootCost_Object = MibTableColumn
teraDot1dStpRootCost = _TeraDot1dStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 7),
    _TeraDot1dStpRootCost_Type()
)
teraDot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStpRootCost.setStatus("mandatory")
_TeraDot1dStpRootPort_Type = Integer32
_TeraDot1dStpRootPort_Object = MibTableColumn
teraDot1dStpRootPort = _TeraDot1dStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 8),
    _TeraDot1dStpRootPort_Type()
)
teraDot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStpRootPort.setStatus("mandatory")
_TeraDot1dStpMaxAge_Type = TimeTicks
_TeraDot1dStpMaxAge_Object = MibTableColumn
teraDot1dStpMaxAge = _TeraDot1dStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 9),
    _TeraDot1dStpMaxAge_Type()
)
teraDot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStpMaxAge.setStatus("mandatory")
_TeraDot1dStpHelloTime_Type = TimeTicks
_TeraDot1dStpHelloTime_Object = MibTableColumn
teraDot1dStpHelloTime = _TeraDot1dStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 10),
    _TeraDot1dStpHelloTime_Type()
)
teraDot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStpHelloTime.setStatus("mandatory")
_TeraDot1dStpHoldTime_Type = TimeTicks
_TeraDot1dStpHoldTime_Object = MibTableColumn
teraDot1dStpHoldTime = _TeraDot1dStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 11),
    _TeraDot1dStpHoldTime_Type()
)
teraDot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStpHoldTime.setStatus("mandatory")
_TeraDot1dStpForwardDelay_Type = TimeTicks
_TeraDot1dStpForwardDelay_Object = MibTableColumn
teraDot1dStpForwardDelay = _TeraDot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 12),
    _TeraDot1dStpForwardDelay_Type()
)
teraDot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStpForwardDelay.setStatus("mandatory")


class _TeraDot1dStpBridgeMaxAge_Type(TimeTicks):
    """Custom type teraDot1dStpBridgeMaxAge based on TimeTicks"""
    subtypeSpec = TimeTicks.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_TeraDot1dStpBridgeMaxAge_Type.__name__ = "TimeTicks"
_TeraDot1dStpBridgeMaxAge_Object = MibTableColumn
teraDot1dStpBridgeMaxAge = _TeraDot1dStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 13),
    _TeraDot1dStpBridgeMaxAge_Type()
)
teraDot1dStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dStpBridgeMaxAge.setStatus("mandatory")


class _TeraDot1dStpBridgeHelloTime_Type(TimeTicks):
    """Custom type teraDot1dStpBridgeHelloTime based on TimeTicks"""
    subtypeSpec = TimeTicks.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_TeraDot1dStpBridgeHelloTime_Type.__name__ = "TimeTicks"
_TeraDot1dStpBridgeHelloTime_Object = MibTableColumn
teraDot1dStpBridgeHelloTime = _TeraDot1dStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 14),
    _TeraDot1dStpBridgeHelloTime_Type()
)
teraDot1dStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dStpBridgeHelloTime.setStatus("mandatory")


class _TeraDot1dStpBridgeForwardDelay_Type(TimeTicks):
    """Custom type teraDot1dStpBridgeForwardDelay based on TimeTicks"""
    subtypeSpec = TimeTicks.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_TeraDot1dStpBridgeForwardDelay_Type.__name__ = "TimeTicks"
_TeraDot1dStpBridgeForwardDelay_Object = MibTableColumn
teraDot1dStpBridgeForwardDelay = _TeraDot1dStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 15),
    _TeraDot1dStpBridgeForwardDelay_Type()
)
teraDot1dStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dStpBridgeForwardDelay.setStatus("mandatory")
_TeraDot1dStpBridgeGroupList_Type = OctetString
_TeraDot1dStpBridgeGroupList_Object = MibTableColumn
teraDot1dStpBridgeGroupList = _TeraDot1dStpBridgeGroupList_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 16),
    _TeraDot1dStpBridgeGroupList_Type()
)
teraDot1dStpBridgeGroupList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dStpBridgeGroupList.setStatus("mandatory")


class _TeraDot1dStpState_Type(Integer32):
    """Custom type teraDot1dStpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_TeraDot1dStpState_Type.__name__ = "Integer32"
_TeraDot1dStpState_Object = MibTableColumn
teraDot1dStpState = _TeraDot1dStpState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 1, 1, 17),
    _TeraDot1dStpState_Type()
)
teraDot1dStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dStpState.setStatus("mandatory")
_TeraBridgePVCPortTable_Object = MibTable
teraBridgePVCPortTable = _TeraBridgePVCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 3)
)
if mibBuilder.loadTexts:
    teraBridgePVCPortTable.setStatus("mandatory")
_TeraBridgePVCPortTableEntry_Object = MibTableRow
teraBridgePVCPortTableEntry = _TeraBridgePVCPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 3, 1)
)
teraBridgePVCPortTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    teraBridgePVCPortTableEntry.setStatus("mandatory")


class _TeraBridgeEncapsulation_Type(Integer32):
    """Custom type teraBridgeEncapsulation based on Integer32"""
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
        *(("llcBrNoFCS", 2),
          ("other", 4),
          ("raw", 1),
          ("vcMuxBrNoFCS", 3))
    )


_TeraBridgeEncapsulation_Type.__name__ = "Integer32"
_TeraBridgeEncapsulation_Object = MibTableColumn
teraBridgeEncapsulation = _TeraBridgeEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 3, 1, 1),
    _TeraBridgeEncapsulation_Type()
)
teraBridgeEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraBridgeEncapsulation.setStatus("mandatory")


class _TeraBridgePriority_Type(Integer32):
    """Custom type teraBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TeraBridgePriority_Type.__name__ = "Integer32"
_TeraBridgePriority_Object = MibTableColumn
teraBridgePriority = _TeraBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 3, 1, 2),
    _TeraBridgePriority_Type()
)
teraBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraBridgePriority.setStatus("mandatory")


class _TeraPVCPortLocalHostFilter_Type(Integer32):
    """Custom type teraPVCPortLocalHostFilter based on Integer32"""
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


_TeraPVCPortLocalHostFilter_Type.__name__ = "Integer32"
_TeraPVCPortLocalHostFilter_Object = MibTableColumn
teraPVCPortLocalHostFilter = _TeraPVCPortLocalHostFilter_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 3, 1, 3),
    _TeraPVCPortLocalHostFilter_Type()
)
teraPVCPortLocalHostFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraPVCPortLocalHostFilter.setStatus("mandatory")


class _TeraPVCPortTrunkFrameType_Type(Integer32):
    """Custom type teraPVCPortTrunkFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sendAll", 3),
          ("sendOnlyUntagged", 1),
          ("sendOnlyVlanTagged", 2))
    )


_TeraPVCPortTrunkFrameType_Type.__name__ = "Integer32"
_TeraPVCPortTrunkFrameType_Object = MibTableColumn
teraPVCPortTrunkFrameType = _TeraPVCPortTrunkFrameType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 3, 1, 4),
    _TeraPVCPortTrunkFrameType_Type()
)
teraPVCPortTrunkFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraPVCPortTrunkFrameType.setStatus("mandatory")


class _TeraPVCPortTrunkTagSwap_Type(Integer32):
    """Custom type teraPVCPortTrunkTagSwap based on Integer32"""
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


_TeraPVCPortTrunkTagSwap_Type.__name__ = "Integer32"
_TeraPVCPortTrunkTagSwap_Object = MibTableColumn
teraPVCPortTrunkTagSwap = _TeraPVCPortTrunkTagSwap_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 3, 1, 5),
    _TeraPVCPortTrunkTagSwap_Type()
)
teraPVCPortTrunkTagSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraPVCPortTrunkTagSwap.setStatus("mandatory")
_TeraDot1dTpPortTable_Object = MibTable
teraDot1dTpPortTable = _TeraDot1dTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 4)
)
if mibBuilder.loadTexts:
    teraDot1dTpPortTable.setStatus("mandatory")
_TeraDot1dTpPortTableEntry_Object = MibTableRow
teraDot1dTpPortTableEntry = _TeraDot1dTpPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 4, 1)
)
teraDot1dTpPortTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dTpPort"),
)
if mibBuilder.loadTexts:
    teraDot1dTpPortTableEntry.setStatus("mandatory")


class _TeraDot1dTpPort_Type(Integer32):
    """Custom type teraDot1dTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraDot1dTpPort_Type.__name__ = "Integer32"
_TeraDot1dTpPort_Object = MibTableColumn
teraDot1dTpPort = _TeraDot1dTpPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 4, 1, 1),
    _TeraDot1dTpPort_Type()
)
teraDot1dTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dTpPort.setStatus("mandatory")


class _TeraDot1dFFType_Type(Integer32):
    """Custom type teraDot1dFFType based on Integer32"""
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
        *(("combined", 2),
          ("dynamic", 3),
          ("static", 1),
          ("vlanTag", 4))
    )


_TeraDot1dFFType_Type.__name__ = "Integer32"
_TeraDot1dFFType_Object = MibTableColumn
teraDot1dFFType = _TeraDot1dFFType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 4, 1, 2),
    _TeraDot1dFFType_Type()
)
teraDot1dFFType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dFFType.setStatus("mandatory")


class _TeraDot1dLoopback_Type(Integer32):
    """Custom type teraDot1dLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("facility", 2),
          ("none", 0),
          ("terminal", 1))
    )


_TeraDot1dLoopback_Type.__name__ = "Integer32"
_TeraDot1dLoopback_Object = MibTableColumn
teraDot1dLoopback = _TeraDot1dLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 4, 1, 3),
    _TeraDot1dLoopback_Type()
)
teraDot1dLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dLoopback.setStatus("mandatory")


class _TeraDot1dTpUseDefaultFwd_Type(Integer32):
    """Custom type teraDot1dTpUseDefaultFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_TeraDot1dTpUseDefaultFwd_Type.__name__ = "Integer32"
_TeraDot1dTpUseDefaultFwd_Object = MibTableColumn
teraDot1dTpUseDefaultFwd = _TeraDot1dTpUseDefaultFwd_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 4, 1, 4),
    _TeraDot1dTpUseDefaultFwd_Type()
)
teraDot1dTpUseDefaultFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dTpUseDefaultFwd.setStatus("mandatory")


class _TeraDot1dTpDefaultFwdPort_Type(Integer32):
    """Custom type teraDot1dTpDefaultFwdPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 89),
    )


_TeraDot1dTpDefaultFwdPort_Type.__name__ = "Integer32"
_TeraDot1dTpDefaultFwdPort_Object = MibTableColumn
teraDot1dTpDefaultFwdPort = _TeraDot1dTpDefaultFwdPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 4, 1, 5),
    _TeraDot1dTpDefaultFwdPort_Type()
)
teraDot1dTpDefaultFwdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dTpDefaultFwdPort.setStatus("mandatory")
_TeraDot1dStaticTable_Object = MibTable
teraDot1dStaticTable = _TeraDot1dStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 5)
)
if mibBuilder.loadTexts:
    teraDot1dStaticTable.setStatus("mandatory")
_TeraDot1dStaticTableEntry_Object = MibTableRow
teraDot1dStaticTableEntry = _TeraDot1dStaticTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 5, 1)
)
teraDot1dStaticTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dStaticReceivePort"),
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dStaticAddress"),
)
if mibBuilder.loadTexts:
    teraDot1dStaticTableEntry.setStatus("mandatory")
_TeraDot1dStaticReceivePort_Type = Integer32
_TeraDot1dStaticReceivePort_Object = MibTableColumn
teraDot1dStaticReceivePort = _TeraDot1dStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 5, 1, 1),
    _TeraDot1dStaticReceivePort_Type()
)
teraDot1dStaticReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStaticReceivePort.setStatus("mandatory")
_TeraDot1dStaticAddress_Type = MacAddress
_TeraDot1dStaticAddress_Object = MibTableColumn
teraDot1dStaticAddress = _TeraDot1dStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 5, 1, 2),
    _TeraDot1dStaticAddress_Type()
)
teraDot1dStaticAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dStaticAddress.setStatus("mandatory")
_TeraDot1dStaticAllowedToGoTo_Type = OctetString
_TeraDot1dStaticAllowedToGoTo_Object = MibTableColumn
teraDot1dStaticAllowedToGoTo = _TeraDot1dStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 5, 1, 3),
    _TeraDot1dStaticAllowedToGoTo_Type()
)
teraDot1dStaticAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dStaticAllowedToGoTo.setStatus("mandatory")


class _TeraDot1dStaticStatus_Type(Integer32):
    """Custom type teraDot1dStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("delete", 3),
          ("disallowed", 2))
    )


_TeraDot1dStaticStatus_Type.__name__ = "Integer32"
_TeraDot1dStaticStatus_Object = MibTableColumn
teraDot1dStaticStatus = _TeraDot1dStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 5, 1, 4),
    _TeraDot1dStaticStatus_Type()
)
teraDot1dStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dStaticStatus.setStatus("mandatory")
_TeraDot1dBasePortTable_Object = MibTable
teraDot1dBasePortTable = _TeraDot1dBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 6)
)
if mibBuilder.loadTexts:
    teraDot1dBasePortTable.setStatus("mandatory")
_TeraDot1dBasePortTableEntry_Object = MibTableRow
teraDot1dBasePortTableEntry = _TeraDot1dBasePortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 6, 1)
)
teraDot1dBasePortTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dBaseInternalVPI"),
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dBaseInternalVCI"),
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dBaseParentPortIfIndex"),
)
if mibBuilder.loadTexts:
    teraDot1dBasePortTableEntry.setStatus("mandatory")


class _TeraDot1dBasePort_Type(Integer32):
    """Custom type teraDot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraDot1dBasePort_Type.__name__ = "Integer32"
_TeraDot1dBasePort_Object = MibTableColumn
teraDot1dBasePort = _TeraDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 6, 1, 1),
    _TeraDot1dBasePort_Type()
)
teraDot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dBasePort.setStatus("mandatory")
_TeraDot1dBaseParentPortIfIndex_Type = Integer32
_TeraDot1dBaseParentPortIfIndex_Object = MibTableColumn
teraDot1dBaseParentPortIfIndex = _TeraDot1dBaseParentPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 6, 1, 2),
    _TeraDot1dBaseParentPortIfIndex_Type()
)
teraDot1dBaseParentPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dBaseParentPortIfIndex.setStatus("mandatory")


class _TeraDot1dBaseInternalVPI_Type(Integer32):
    """Custom type teraDot1dBaseInternalVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TeraDot1dBaseInternalVPI_Type.__name__ = "Integer32"
_TeraDot1dBaseInternalVPI_Object = MibTableColumn
teraDot1dBaseInternalVPI = _TeraDot1dBaseInternalVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 6, 1, 3),
    _TeraDot1dBaseInternalVPI_Type()
)
teraDot1dBaseInternalVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dBaseInternalVPI.setStatus("mandatory")


class _TeraDot1dBaseInternalVCI_Type(Integer32):
    """Custom type teraDot1dBaseInternalVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraDot1dBaseInternalVCI_Type.__name__ = "Integer32"
_TeraDot1dBaseInternalVCI_Object = MibTableColumn
teraDot1dBaseInternalVCI = _TeraDot1dBaseInternalVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 6, 1, 4),
    _TeraDot1dBaseInternalVCI_Type()
)
teraDot1dBaseInternalVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dBaseInternalVCI.setStatus("mandatory")


class _TeraDot1dBaseParentVPI_Type(Integer32):
    """Custom type teraDot1dBaseParentVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TeraDot1dBaseParentVPI_Type.__name__ = "Integer32"
_TeraDot1dBaseParentVPI_Object = MibTableColumn
teraDot1dBaseParentVPI = _TeraDot1dBaseParentVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 6, 1, 5),
    _TeraDot1dBaseParentVPI_Type()
)
teraDot1dBaseParentVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dBaseParentVPI.setStatus("mandatory")


class _TeraDot1dBaseParentVCI_Type(Integer32):
    """Custom type teraDot1dBaseParentVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraDot1dBaseParentVCI_Type.__name__ = "Integer32"
_TeraDot1dBaseParentVCI_Object = MibTableColumn
teraDot1dBaseParentVCI = _TeraDot1dBaseParentVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 6, 1, 6),
    _TeraDot1dBaseParentVCI_Type()
)
teraDot1dBaseParentVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dBaseParentVCI.setStatus("mandatory")
_TeraVlanPortGroupTable_Object = MibTable
teraVlanPortGroupTable = _TeraVlanPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 7)
)
if mibBuilder.loadTexts:
    teraVlanPortGroupTable.setStatus("mandatory")
_TeraVlanPortGroupTableEntry_Object = MibTableRow
teraVlanPortGroupTableEntry = _TeraVlanPortGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 7, 1)
)
teraVlanPortGroupTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    teraVlanPortGroupTableEntry.setStatus("mandatory")


class _Dot1qVlanIndex_Type(Integer32):
    """Custom type dot1qVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot1qVlanIndex_Type.__name__ = "Integer32"
_Dot1qVlanIndex_Object = MibTableColumn
dot1qVlanIndex = _Dot1qVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 7, 1, 1),
    _Dot1qVlanIndex_Type()
)
dot1qVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanIndex.setStatus("mandatory")
_TeraVlanPorts_Type = OctetString
_TeraVlanPorts_Object = MibTableColumn
teraVlanPorts = _TeraVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 7, 1, 2),
    _TeraVlanPorts_Type()
)
teraVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraVlanPorts.setStatus("mandatory")


class _TeraVlanPortGroupTableAction_Type(Integer32):
    """Custom type teraVlanPortGroupTableAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("ok", 1))
    )


_TeraVlanPortGroupTableAction_Type.__name__ = "Integer32"
_TeraVlanPortGroupTableAction_Object = MibTableColumn
teraVlanPortGroupTableAction = _TeraVlanPortGroupTableAction_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 7, 1, 3),
    _TeraVlanPortGroupTableAction_Type()
)
teraVlanPortGroupTableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraVlanPortGroupTableAction.setStatus("mandatory")
_TeraDot1qVlanPortTable_Object = MibTable
teraDot1qVlanPortTable = _TeraDot1qVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 8)
)
if mibBuilder.loadTexts:
    teraDot1qVlanPortTable.setStatus("mandatory")
_TeraDot1qVlanPortTableEntry_Object = MibTableRow
teraDot1qVlanPortTableEntry = _TeraDot1qVlanPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 8, 1)
)
teraDot1qVlanPortTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "teraDot1qVlanPort"),
)
if mibBuilder.loadTexts:
    teraDot1qVlanPortTableEntry.setStatus("mandatory")


class _TeraDot1qVlanPort_Type(Integer32):
    """Custom type teraDot1qVlanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 81),
    )


_TeraDot1qVlanPort_Type.__name__ = "Integer32"
_TeraDot1qVlanPort_Object = MibTableColumn
teraDot1qVlanPort = _TeraDot1qVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 8, 1, 1),
    _TeraDot1qVlanPort_Type()
)
teraDot1qVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1qVlanPort.setStatus("mandatory")


class _TeraDot1qVlanPortIngressFrameTypes_Type(Integer32):
    """Custom type teraDot1qVlanPortIngressFrameTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitOnlyUntagged", 3),
          ("admitOnlyVlanTagged", 2))
    )


_TeraDot1qVlanPortIngressFrameTypes_Type.__name__ = "Integer32"
_TeraDot1qVlanPortIngressFrameTypes_Object = MibTableColumn
teraDot1qVlanPortIngressFrameTypes = _TeraDot1qVlanPortIngressFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 8, 1, 2),
    _TeraDot1qVlanPortIngressFrameTypes_Type()
)
teraDot1qVlanPortIngressFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1qVlanPortIngressFrameTypes.setStatus("mandatory")


class _TeraDot1qVlanPortIngressFiltering_Type(Integer32):
    """Custom type teraDot1qVlanPortIngressFiltering based on Integer32"""
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


_TeraDot1qVlanPortIngressFiltering_Type.__name__ = "Integer32"
_TeraDot1qVlanPortIngressFiltering_Object = MibTableColumn
teraDot1qVlanPortIngressFiltering = _TeraDot1qVlanPortIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 8, 1, 3),
    _TeraDot1qVlanPortIngressFiltering_Type()
)
teraDot1qVlanPortIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1qVlanPortIngressFiltering.setStatus("mandatory")


class _TeraDot1qVlanPortEgressFrameType_Type(Integer32):
    """Custom type teraDot1qVlanPortEgressFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sendAll", 3),
          ("sendOnlyUntagged", 1),
          ("sendOnlyVlanTagged", 2))
    )


_TeraDot1qVlanPortEgressFrameType_Type.__name__ = "Integer32"
_TeraDot1qVlanPortEgressFrameType_Object = MibTableColumn
teraDot1qVlanPortEgressFrameType = _TeraDot1qVlanPortEgressFrameType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 8, 1, 4),
    _TeraDot1qVlanPortEgressFrameType_Type()
)
teraDot1qVlanPortEgressFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1qVlanPortEgressFrameType.setStatus("mandatory")


class _TeraDot1qVlanPortEgressTagSwap_Type(Integer32):
    """Custom type teraDot1qVlanPortEgressTagSwap based on Integer32"""
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


_TeraDot1qVlanPortEgressTagSwap_Type.__name__ = "Integer32"
_TeraDot1qVlanPortEgressTagSwap_Object = MibTableColumn
teraDot1qVlanPortEgressTagSwap = _TeraDot1qVlanPortEgressTagSwap_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 8, 1, 5),
    _TeraDot1qVlanPortEgressTagSwap_Type()
)
teraDot1qVlanPortEgressTagSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1qVlanPortEgressTagSwap.setStatus("mandatory")


class _TeraDot1qVlanPortDisUntaggedBcast_Type(Integer32):
    """Custom type teraDot1qVlanPortDisUntaggedBcast based on Integer32"""
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


_TeraDot1qVlanPortDisUntaggedBcast_Type.__name__ = "Integer32"
_TeraDot1qVlanPortDisUntaggedBcast_Object = MibTableColumn
teraDot1qVlanPortDisUntaggedBcast = _TeraDot1qVlanPortDisUntaggedBcast_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 8, 1, 6),
    _TeraDot1qVlanPortDisUntaggedBcast_Type()
)
teraDot1qVlanPortDisUntaggedBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1qVlanPortDisUntaggedBcast.setStatus("mandatory")
_TeraDot1dTp_Object = MibTable
teraDot1dTp = _TeraDot1dTp_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 9)
)
if mibBuilder.loadTexts:
    teraDot1dTp.setStatus("mandatory")
_TeraDot1dTpEntry_Object = MibTableRow
teraDot1dTpEntry = _TeraDot1dTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 9, 1)
)
teraDot1dTpEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dTpSlot"),
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dTpProcessor"),
)
if mibBuilder.loadTexts:
    teraDot1dTpEntry.setStatus("mandatory")


class _TeraDot1dTpSlot_Type(Integer32):
    """Custom type teraDot1dTpSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TeraDot1dTpSlot_Type.__name__ = "Integer32"
_TeraDot1dTpSlot_Object = MibTableColumn
teraDot1dTpSlot = _TeraDot1dTpSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 9, 1, 1),
    _TeraDot1dTpSlot_Type()
)
teraDot1dTpSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dTpSlot.setStatus("mandatory")


class _TeraDot1dTpProcessor_Type(Integer32):
    """Custom type teraDot1dTpProcessor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TeraDot1dTpProcessor_Type.__name__ = "Integer32"
_TeraDot1dTpProcessor_Object = MibTableColumn
teraDot1dTpProcessor = _TeraDot1dTpProcessor_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 9, 1, 2),
    _TeraDot1dTpProcessor_Type()
)
teraDot1dTpProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dTpProcessor.setStatus("mandatory")
_TeraDot1dTpLearnedEntryDiscards_Type = Counter32
_TeraDot1dTpLearnedEntryDiscards_Object = MibTableColumn
teraDot1dTpLearnedEntryDiscards = _TeraDot1dTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 9, 1, 3),
    _TeraDot1dTpLearnedEntryDiscards_Type()
)
teraDot1dTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dTpLearnedEntryDiscards.setStatus("mandatory")


class _TeraDot1dTpAgingTime_Type(Integer32):
    """Custom type teraDot1dTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_TeraDot1dTpAgingTime_Type.__name__ = "Integer32"
_TeraDot1dTpAgingTime_Object = MibTableColumn
teraDot1dTpAgingTime = _TeraDot1dTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 9, 1, 4),
    _TeraDot1dTpAgingTime_Type()
)
teraDot1dTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dTpAgingTime.setStatus("mandatory")
_TeraDot1qFdbTable_Object = MibTable
teraDot1qFdbTable = _TeraDot1qFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 10)
)
if mibBuilder.loadTexts:
    teraDot1qFdbTable.setStatus("mandatory")
_TeraDot1qFdbTableEntry_Object = MibTableRow
teraDot1qFdbTableEntry = _TeraDot1qFdbTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 10, 1)
)
teraDot1qFdbTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dTpSlot"),
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dTpProcessor"),
    (0, "TERAWAVE-terabridge-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    teraDot1qFdbTableEntry.setStatus("mandatory")
_TeraDot1qFdbDynamicCount_Type = Counter32
_TeraDot1qFdbDynamicCount_Object = MibTableColumn
teraDot1qFdbDynamicCount = _TeraDot1qFdbDynamicCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 10, 1, 1),
    _TeraDot1qFdbDynamicCount_Type()
)
teraDot1qFdbDynamicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1qFdbDynamicCount.setStatus("mandatory")
_TeraDot1qTpFdbTable_Object = MibTable
teraDot1qTpFdbTable = _TeraDot1qTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 11)
)
if mibBuilder.loadTexts:
    teraDot1qTpFdbTable.setStatus("mandatory")
_TeraDot1qTpFdbTableEntry_Object = MibTableRow
teraDot1qTpFdbTableEntry = _TeraDot1qTpFdbTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 11, 1)
)
teraDot1qTpFdbTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dTpSlot"),
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dTpProcessor"),
    (0, "TERAWAVE-terabridge-MIB", "dot1qFdbId"),
    (0, "TERAWAVE-terabridge-MIB", "teraDot1qTpFdbAddress"),
)
if mibBuilder.loadTexts:
    teraDot1qTpFdbTableEntry.setStatus("mandatory")
_TeraDot1qTpFdbAddress_Type = MacAddress
_TeraDot1qTpFdbAddress_Object = MibTableColumn
teraDot1qTpFdbAddress = _TeraDot1qTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 11, 1, 1),
    _TeraDot1qTpFdbAddress_Type()
)
teraDot1qTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1qTpFdbAddress.setStatus("mandatory")


class _TeraDot1qTpFdbPort_Type(Integer32):
    """Custom type teraDot1qTpFdbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TeraDot1qTpFdbPort_Type.__name__ = "Integer32"
_TeraDot1qTpFdbPort_Object = MibTableColumn
teraDot1qTpFdbPort = _TeraDot1qTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 11, 1, 2),
    _TeraDot1qTpFdbPort_Type()
)
teraDot1qTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1qTpFdbPort.setStatus("mandatory")


class _TeraDot1qTpFdbStatus_Type(Integer32):
    """Custom type teraDot1qTpFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_TeraDot1qTpFdbStatus_Type.__name__ = "Integer32"
_TeraDot1qTpFdbStatus_Object = MibTableColumn
teraDot1qTpFdbStatus = _TeraDot1qTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 11, 1, 3),
    _TeraDot1qTpFdbStatus_Type()
)
teraDot1qTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1qTpFdbStatus.setStatus("mandatory")
_TeraDot1dPvcStatTable_Object = MibTable
teraDot1dPvcStatTable = _TeraDot1dPvcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12)
)
if mibBuilder.loadTexts:
    teraDot1dPvcStatTable.setStatus("mandatory")
_TeraDot1dPvcStatTableEntry_Object = MibTableRow
teraDot1dPvcStatTableEntry = _TeraDot1dPvcStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1)
)
teraDot1dPvcStatTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dTpPort"),
)
if mibBuilder.loadTexts:
    teraDot1dPvcStatTableEntry.setStatus("mandatory")
_TeraDot1dPvcStatTxPktCount_Type = Counter32
_TeraDot1dPvcStatTxPktCount_Object = MibTableColumn
teraDot1dPvcStatTxPktCount = _TeraDot1dPvcStatTxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 1),
    _TeraDot1dPvcStatTxPktCount_Type()
)
teraDot1dPvcStatTxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dPvcStatTxPktCount.setStatus("mandatory")
_TeraDot1dPvcStatTxOverrun_Type = Counter32
_TeraDot1dPvcStatTxOverrun_Object = MibTableColumn
teraDot1dPvcStatTxOverrun = _TeraDot1dPvcStatTxOverrun_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 2),
    _TeraDot1dPvcStatTxOverrun_Type()
)
teraDot1dPvcStatTxOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dPvcStatTxOverrun.setStatus("mandatory")
_TeraDot1dPvcStatTxUnderrun_Type = Counter32
_TeraDot1dPvcStatTxUnderrun_Object = MibTableColumn
teraDot1dPvcStatTxUnderrun = _TeraDot1dPvcStatTxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 3),
    _TeraDot1dPvcStatTxUnderrun_Type()
)
teraDot1dPvcStatTxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dPvcStatTxUnderrun.setStatus("mandatory")
_TeraDot1dPvcStatRxPktCount_Type = Counter32
_TeraDot1dPvcStatRxPktCount_Object = MibTableColumn
teraDot1dPvcStatRxPktCount = _TeraDot1dPvcStatRxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 4),
    _TeraDot1dPvcStatRxPktCount_Type()
)
teraDot1dPvcStatRxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dPvcStatRxPktCount.setStatus("mandatory")
_TeraDot1dPvcStatRxOverrun_Type = Counter32
_TeraDot1dPvcStatRxOverrun_Object = MibTableColumn
teraDot1dPvcStatRxOverrun = _TeraDot1dPvcStatRxOverrun_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 5),
    _TeraDot1dPvcStatRxOverrun_Type()
)
teraDot1dPvcStatRxOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dPvcStatRxOverrun.setStatus("mandatory")
_TeraDot1dPvcStatRxUnderrun_Type = Counter32
_TeraDot1dPvcStatRxUnderrun_Object = MibTableColumn
teraDot1dPvcStatRxUnderrun = _TeraDot1dPvcStatRxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 6),
    _TeraDot1dPvcStatRxUnderrun_Type()
)
teraDot1dPvcStatRxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dPvcStatRxUnderrun.setStatus("mandatory")
_TeraDot1dPvcStatRxCrcError_Type = Counter32
_TeraDot1dPvcStatRxCrcError_Object = MibTableColumn
teraDot1dPvcStatRxCrcError = _TeraDot1dPvcStatRxCrcError_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 7),
    _TeraDot1dPvcStatRxCrcError_Type()
)
teraDot1dPvcStatRxCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dPvcStatRxCrcError.setStatus("mandatory")
_TeraDot1dPvcStatRxLengthError_Type = Counter32
_TeraDot1dPvcStatRxLengthError_Object = MibTableColumn
teraDot1dPvcStatRxLengthError = _TeraDot1dPvcStatRxLengthError_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 8),
    _TeraDot1dPvcStatRxLengthError_Type()
)
teraDot1dPvcStatRxLengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dPvcStatRxLengthError.setStatus("mandatory")
_TeraDot1dPvcStatRxAbort_Type = Counter32
_TeraDot1dPvcStatRxAbort_Object = MibTableColumn
teraDot1dPvcStatRxAbort = _TeraDot1dPvcStatRxAbort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 9),
    _TeraDot1dPvcStatRxAbort_Type()
)
teraDot1dPvcStatRxAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dPvcStatRxAbort.setStatus("mandatory")
_TeraDot1dPvcStatRxSlip_Type = Counter32
_TeraDot1dPvcStatRxSlip_Object = MibTableColumn
teraDot1dPvcStatRxSlip = _TeraDot1dPvcStatRxSlip_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 10),
    _TeraDot1dPvcStatRxSlip_Type()
)
teraDot1dPvcStatRxSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dPvcStatRxSlip.setStatus("mandatory")
_TeraDot1dPvcStatRxNoBuffer_Type = Counter32
_TeraDot1dPvcStatRxNoBuffer_Object = MibTableColumn
teraDot1dPvcStatRxNoBuffer = _TeraDot1dPvcStatRxNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 11),
    _TeraDot1dPvcStatRxNoBuffer_Type()
)
teraDot1dPvcStatRxNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDot1dPvcStatRxNoBuffer.setStatus("mandatory")


class _TeraDot1dPvcStatState_Type(Integer32):
    """Custom type teraDot1dPvcStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_TeraDot1dPvcStatState_Type.__name__ = "Integer32"
_TeraDot1dPvcStatState_Object = MibTableColumn
teraDot1dPvcStatState = _TeraDot1dPvcStatState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 12, 1, 12),
    _TeraDot1dPvcStatState_Type()
)
teraDot1dPvcStatState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDot1dPvcStatState.setStatus("mandatory")
_TeraBridgeConnIdTable_Object = MibTable
teraBridgeConnIdTable = _TeraBridgeConnIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 13)
)
if mibBuilder.loadTexts:
    teraBridgeConnIdTable.setStatus("mandatory")
_TeraBridgeConnIdTableEntry_Object = MibTableRow
teraBridgeConnIdTableEntry = _TeraBridgeConnIdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 13, 1)
)
teraBridgeConnIdTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "teraPvcLogPortId"),
)
if mibBuilder.loadTexts:
    teraBridgeConnIdTableEntry.setStatus("mandatory")
_TeraPvcLogPortId_Type = Integer32
_TeraPvcLogPortId_Object = MibTableColumn
teraPvcLogPortId = _TeraPvcLogPortId_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 13, 1, 1),
    _TeraPvcLogPortId_Type()
)
teraPvcLogPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraPvcLogPortId.setStatus("mandatory")
_TeraConnId_Type = Counter32
_TeraConnId_Object = MibTableColumn
teraConnId = _TeraConnId_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 13, 1, 2),
    _TeraConnId_Type()
)
teraConnId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraConnId.setStatus("mandatory")
_TeraVlanStatTable_Object = MibTable
teraVlanStatTable = _TeraVlanStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14)
)
if mibBuilder.loadTexts:
    teraVlanStatTable.setStatus("mandatory")
_TeraVlanStatTableEntry_Object = MibTableRow
teraVlanStatTableEntry = _TeraVlanStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1)
)
teraVlanStatTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "dot1dBasePort"),
    (0, "TERAWAVE-terabridge-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    teraVlanStatTableEntry.setStatus("mandatory")


class _TeraVlanStatState_Type(Integer32):
    """Custom type teraVlanStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_TeraVlanStatState_Type.__name__ = "Integer32"
_TeraVlanStatState_Object = MibTableColumn
teraVlanStatState = _TeraVlanStatState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 1),
    _TeraVlanStatState_Type()
)
teraVlanStatState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraVlanStatState.setStatus("mandatory")
_TeraVlanStatRxMcastSrcAddr_Type = Counter32
_TeraVlanStatRxMcastSrcAddr_Object = MibTableColumn
teraVlanStatRxMcastSrcAddr = _TeraVlanStatRxMcastSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 2),
    _TeraVlanStatRxMcastSrcAddr_Type()
)
teraVlanStatRxMcastSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxMcastSrcAddr.setStatus("mandatory")
_TeraVlanStatRxInvalidVlanId_Type = Counter32
_TeraVlanStatRxInvalidVlanId_Object = MibTableColumn
teraVlanStatRxInvalidVlanId = _TeraVlanStatRxInvalidVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 3),
    _TeraVlanStatRxInvalidVlanId_Type()
)
teraVlanStatRxInvalidVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxInvalidVlanId.setStatus("mandatory")
_TeraVlanStatRxMacAddrNotInStaticTbl_Type = Counter32
_TeraVlanStatRxMacAddrNotInStaticTbl_Object = MibTableColumn
teraVlanStatRxMacAddrNotInStaticTbl = _TeraVlanStatRxMacAddrNotInStaticTbl_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 4),
    _TeraVlanStatRxMacAddrNotInStaticTbl_Type()
)
teraVlanStatRxMacAddrNotInStaticTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxMacAddrNotInStaticTbl.setStatus("mandatory")
_TeraVlanStatRxMacAddrInStaticTbl_Type = Counter32
_TeraVlanStatRxMacAddrInStaticTbl_Object = MibTableColumn
teraVlanStatRxMacAddrInStaticTbl = _TeraVlanStatRxMacAddrInStaticTbl_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 5),
    _TeraVlanStatRxMacAddrInStaticTbl_Type()
)
teraVlanStatRxMacAddrInStaticTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxMacAddrInStaticTbl.setStatus("mandatory")
_TeraVlanStatRxInvalidOutPort_Type = Counter32
_TeraVlanStatRxInvalidOutPort_Object = MibTableColumn
teraVlanStatRxInvalidOutPort = _TeraVlanStatRxInvalidOutPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 6),
    _TeraVlanStatRxInvalidOutPort_Type()
)
teraVlanStatRxInvalidOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxInvalidOutPort.setStatus("mandatory")
_TeraVlanStatRxInvalidInPort_Type = Counter32
_TeraVlanStatRxInvalidInPort_Object = MibTableColumn
teraVlanStatRxInvalidInPort = _TeraVlanStatRxInvalidInPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 7),
    _TeraVlanStatRxInvalidInPort_Type()
)
teraVlanStatRxInvalidInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxInvalidInPort.setStatus("mandatory")
_TeraVlanStatRxDestMacAddrDisallowed_Type = Counter32
_TeraVlanStatRxDestMacAddrDisallowed_Object = MibTableColumn
teraVlanStatRxDestMacAddrDisallowed = _TeraVlanStatRxDestMacAddrDisallowed_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 8),
    _TeraVlanStatRxDestMacAddrDisallowed_Type()
)
teraVlanStatRxDestMacAddrDisallowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxDestMacAddrDisallowed.setStatus("mandatory")
_TeraVlanStatRxPortBlocked_Type = Counter32
_TeraVlanStatRxPortBlocked_Object = MibTableColumn
teraVlanStatRxPortBlocked = _TeraVlanStatRxPortBlocked_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 9),
    _TeraVlanStatRxPortBlocked_Type()
)
teraVlanStatRxPortBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxPortBlocked.setStatus("mandatory")
_TeraVlanStatRxDiscardTaggedFrame_Type = Counter32
_TeraVlanStatRxDiscardTaggedFrame_Object = MibTableColumn
teraVlanStatRxDiscardTaggedFrame = _TeraVlanStatRxDiscardTaggedFrame_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 10),
    _TeraVlanStatRxDiscardTaggedFrame_Type()
)
teraVlanStatRxDiscardTaggedFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxDiscardTaggedFrame.setStatus("mandatory")
_TeraVlanStatRxDiscardUntaggedFrame_Type = Counter32
_TeraVlanStatRxDiscardUntaggedFrame_Object = MibTableColumn
teraVlanStatRxDiscardUntaggedFrame = _TeraVlanStatRxDiscardUntaggedFrame_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 11),
    _TeraVlanStatRxDiscardUntaggedFrame_Type()
)
teraVlanStatRxDiscardUntaggedFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxDiscardUntaggedFrame.setStatus("mandatory")
_TeraVlanStatRxDiscardBcastBlocked_Type = Counter32
_TeraVlanStatRxDiscardBcastBlocked_Object = MibTableColumn
teraVlanStatRxDiscardBcastBlocked = _TeraVlanStatRxDiscardBcastBlocked_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 12),
    _TeraVlanStatRxDiscardBcastBlocked_Type()
)
teraVlanStatRxDiscardBcastBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxDiscardBcastBlocked.setStatus("mandatory")
_TeraVlanStatRxDiscardLocalDest_Type = Counter32
_TeraVlanStatRxDiscardLocalDest_Object = MibTableColumn
teraVlanStatRxDiscardLocalDest = _TeraVlanStatRxDiscardLocalDest_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 13),
    _TeraVlanStatRxDiscardLocalDest_Type()
)
teraVlanStatRxDiscardLocalDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxDiscardLocalDest.setStatus("mandatory")
_TeraVlanStatRxFFTypeMismatch_Type = Counter32
_TeraVlanStatRxFFTypeMismatch_Object = MibTableColumn
teraVlanStatRxFFTypeMismatch = _TeraVlanStatRxFFTypeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 14),
    _TeraVlanStatRxFFTypeMismatch_Type()
)
teraVlanStatRxFFTypeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxFFTypeMismatch.setStatus("mandatory")
_TeraVlanStatRxNoBuffer_Type = Counter32
_TeraVlanStatRxNoBuffer_Object = MibTableColumn
teraVlanStatRxNoBuffer = _TeraVlanStatRxNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 15),
    _TeraVlanStatRxNoBuffer_Type()
)
teraVlanStatRxNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxNoBuffer.setStatus("mandatory")
_TeraVlanStatRxTxFail_Type = Counter32
_TeraVlanStatRxTxFail_Object = MibTableColumn
teraVlanStatRxTxFail = _TeraVlanStatRxTxFail_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 16),
    _TeraVlanStatRxTxFail_Type()
)
teraVlanStatRxTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxTxFail.setStatus("mandatory")
_TeraVlanStatRxInvalidEncap_Type = Counter32
_TeraVlanStatRxInvalidEncap_Object = MibTableColumn
teraVlanStatRxInvalidEncap = _TeraVlanStatRxInvalidEncap_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 14, 1, 17),
    _TeraVlanStatRxInvalidEncap_Type()
)
teraVlanStatRxInvalidEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraVlanStatRxInvalidEncap.setStatus("mandatory")
_TeraEtherStatTable_Object = MibTable
teraEtherStatTable = _TeraEtherStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15)
)
if mibBuilder.loadTexts:
    teraEtherStatTable.setStatus("mandatory")
_TeraEtherStatTableEntry_Object = MibTableRow
teraEtherStatTableEntry = _TeraEtherStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1)
)
teraEtherStatTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "etherStatsIndex"),
)
if mibBuilder.loadTexts:
    teraEtherStatTableEntry.setStatus("mandatory")
_TeraEtherStatRxTotalFrames_Type = Counter32
_TeraEtherStatRxTotalFrames_Object = MibTableColumn
teraEtherStatRxTotalFrames = _TeraEtherStatRxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 1),
    _TeraEtherStatRxTotalFrames_Type()
)
teraEtherStatRxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxTotalFrames.setStatus("mandatory")
_TeraEtherStatRxGoodFrames_Type = Counter32
_TeraEtherStatRxGoodFrames_Object = MibTableColumn
teraEtherStatRxGoodFrames = _TeraEtherStatRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 2),
    _TeraEtherStatRxGoodFrames_Type()
)
teraEtherStatRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxGoodFrames.setStatus("mandatory")
_TeraEtherStatRxForwardFrames_Type = Counter32
_TeraEtherStatRxForwardFrames_Object = MibTableColumn
teraEtherStatRxForwardFrames = _TeraEtherStatRxForwardFrames_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 3),
    _TeraEtherStatRxForwardFrames_Type()
)
teraEtherStatRxForwardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxForwardFrames.setStatus("mandatory")
_TeraEtherStatRxForwardOctets_Type = Counter32
_TeraEtherStatRxForwardOctets_Object = MibTableColumn
teraEtherStatRxForwardOctets = _TeraEtherStatRxForwardOctets_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 4),
    _TeraEtherStatRxForwardOctets_Type()
)
teraEtherStatRxForwardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxForwardOctets.setStatus("mandatory")
_TeraEtherStatRxPause_Type = Counter32
_TeraEtherStatRxPause_Object = MibTableColumn
teraEtherStatRxPause = _TeraEtherStatRxPause_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 5),
    _TeraEtherStatRxPause_Type()
)
teraEtherStatRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxPause.setStatus("mandatory")
_TeraEtherStatRxTotalDiscard_Type = Counter32
_TeraEtherStatRxTotalDiscard_Object = MibTableColumn
teraEtherStatRxTotalDiscard = _TeraEtherStatRxTotalDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 6),
    _TeraEtherStatRxTotalDiscard_Type()
)
teraEtherStatRxTotalDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxTotalDiscard.setStatus("mandatory")
_TeraEtherStatRxNoBuffer_Type = Counter32
_TeraEtherStatRxNoBuffer_Object = MibTableColumn
teraEtherStatRxNoBuffer = _TeraEtherStatRxNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 7),
    _TeraEtherStatRxNoBuffer_Type()
)
teraEtherStatRxNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxNoBuffer.setStatus("mandatory")
_TeraEtherStatRxTotalBadFrames_Type = Counter32
_TeraEtherStatRxTotalBadFrames_Object = MibTableColumn
teraEtherStatRxTotalBadFrames = _TeraEtherStatRxTotalBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 8),
    _TeraEtherStatRxTotalBadFrames_Type()
)
teraEtherStatRxTotalBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxTotalBadFrames.setStatus("mandatory")
_TeraEtherStatRxBadFrameLenViolation_Type = Counter32
_TeraEtherStatRxBadFrameLenViolation_Object = MibTableColumn
teraEtherStatRxBadFrameLenViolation = _TeraEtherStatRxBadFrameLenViolation_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 9),
    _TeraEtherStatRxBadFrameLenViolation_Type()
)
teraEtherStatRxBadFrameLenViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxBadFrameLenViolation.setStatus("mandatory")
_TeraEtherStatRxBadFrameNotAlign_Type = Counter32
_TeraEtherStatRxBadFrameNotAlign_Object = MibTableColumn
teraEtherStatRxBadFrameNotAlign = _TeraEtherStatRxBadFrameNotAlign_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 10),
    _TeraEtherStatRxBadFrameNotAlign_Type()
)
teraEtherStatRxBadFrameNotAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxBadFrameNotAlign.setStatus("mandatory")
_TeraEtherStatRxBadFrameTooShort_Type = Counter32
_TeraEtherStatRxBadFrameTooShort_Object = MibTableColumn
teraEtherStatRxBadFrameTooShort = _TeraEtherStatRxBadFrameTooShort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 11),
    _TeraEtherStatRxBadFrameTooShort_Type()
)
teraEtherStatRxBadFrameTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxBadFrameTooShort.setStatus("mandatory")
_TeraEtherStatRxBadFrameCRC_Type = Counter32
_TeraEtherStatRxBadFrameCRC_Object = MibTableColumn
teraEtherStatRxBadFrameCRC = _TeraEtherStatRxBadFrameCRC_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 12),
    _TeraEtherStatRxBadFrameCRC_Type()
)
teraEtherStatRxBadFrameCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxBadFrameCRC.setStatus("mandatory")
_TeraEtherStatRxBadFrameOverrun_Type = Counter32
_TeraEtherStatRxBadFrameOverrun_Object = MibTableColumn
teraEtherStatRxBadFrameOverrun = _TeraEtherStatRxBadFrameOverrun_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 13),
    _TeraEtherStatRxBadFrameOverrun_Type()
)
teraEtherStatRxBadFrameOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxBadFrameOverrun.setStatus("mandatory")
_TeraEtherStatRxBadFrameCollision_Type = Counter32
_TeraEtherStatRxBadFrameCollision_Object = MibTableColumn
teraEtherStatRxBadFrameCollision = _TeraEtherStatRxBadFrameCollision_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 14),
    _TeraEtherStatRxBadFrameCollision_Type()
)
teraEtherStatRxBadFrameCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatRxBadFrameCollision.setStatus("mandatory")
_TeraEtherStatTxTotalFrames_Type = Counter32
_TeraEtherStatTxTotalFrames_Object = MibTableColumn
teraEtherStatTxTotalFrames = _TeraEtherStatTxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 15),
    _TeraEtherStatTxTotalFrames_Type()
)
teraEtherStatTxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxTotalFrames.setStatus("mandatory")
_TeraEtherStatTxGoodFrames_Type = Counter32
_TeraEtherStatTxGoodFrames_Object = MibTableColumn
teraEtherStatTxGoodFrames = _TeraEtherStatTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 16),
    _TeraEtherStatTxGoodFrames_Type()
)
teraEtherStatTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxGoodFrames.setStatus("mandatory")
_TeraEtherStatTxFramesSentOut_Type = Counter32
_TeraEtherStatTxFramesSentOut_Object = MibTableColumn
teraEtherStatTxFramesSentOut = _TeraEtherStatTxFramesSentOut_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 17),
    _TeraEtherStatTxFramesSentOut_Type()
)
teraEtherStatTxFramesSentOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxFramesSentOut.setStatus("mandatory")
_TeraEtherStatTxOctets_Type = Counter32
_TeraEtherStatTxOctets_Object = MibTableColumn
teraEtherStatTxOctets = _TeraEtherStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 18),
    _TeraEtherStatTxOctets_Type()
)
teraEtherStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxOctets.setStatus("mandatory")
_TeraEtherStatTxPause_Type = Counter32
_TeraEtherStatTxPause_Object = MibTableColumn
teraEtherStatTxPause = _TeraEtherStatTxPause_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 19),
    _TeraEtherStatTxPause_Type()
)
teraEtherStatTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxPause.setStatus("mandatory")
_TeraEtherStatTxQueueOverflow_Type = Counter32
_TeraEtherStatTxQueueOverflow_Object = MibTableColumn
teraEtherStatTxQueueOverflow = _TeraEtherStatTxQueueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 20),
    _TeraEtherStatTxQueueOverflow_Type()
)
teraEtherStatTxQueueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxQueueOverflow.setStatus("mandatory")
_TeraEtherStatTxTotalBadFrames_Type = Counter32
_TeraEtherStatTxTotalBadFrames_Object = MibTableColumn
teraEtherStatTxTotalBadFrames = _TeraEtherStatTxTotalBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 21),
    _TeraEtherStatTxTotalBadFrames_Type()
)
teraEtherStatTxTotalBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxTotalBadFrames.setStatus("mandatory")
_TeraEtherStatTxBadFrameCarrierLost_Type = Counter32
_TeraEtherStatTxBadFrameCarrierLost_Object = MibTableColumn
teraEtherStatTxBadFrameCarrierLost = _TeraEtherStatTxBadFrameCarrierLost_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 22),
    _TeraEtherStatTxBadFrameCarrierLost_Type()
)
teraEtherStatTxBadFrameCarrierLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxBadFrameCarrierLost.setStatus("mandatory")
_TeraEtherStatTxBadFrameUnderrun_Type = Counter32
_TeraEtherStatTxBadFrameUnderrun_Object = MibTableColumn
teraEtherStatTxBadFrameUnderrun = _TeraEtherStatTxBadFrameUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 23),
    _TeraEtherStatTxBadFrameUnderrun_Type()
)
teraEtherStatTxBadFrameUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxBadFrameUnderrun.setStatus("mandatory")
_TeraEtherStatTxBadFrameRexmitLimit_Type = Counter32
_TeraEtherStatTxBadFrameRexmitLimit_Object = MibTableColumn
teraEtherStatTxBadFrameRexmitLimit = _TeraEtherStatTxBadFrameRexmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 24),
    _TeraEtherStatTxBadFrameRexmitLimit_Type()
)
teraEtherStatTxBadFrameRexmitLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxBadFrameRexmitLimit.setStatus("mandatory")
_TeraEtherStatTxBadFrameLateCollision_Type = Counter32
_TeraEtherStatTxBadFrameLateCollision_Object = MibTableColumn
teraEtherStatTxBadFrameLateCollision = _TeraEtherStatTxBadFrameLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 25),
    _TeraEtherStatTxBadFrameLateCollision_Type()
)
teraEtherStatTxBadFrameLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxBadFrameLateCollision.setStatus("mandatory")
_TeraEtherStatTxBadFrameTxErr_Type = Counter32
_TeraEtherStatTxBadFrameTxErr_Object = MibTableColumn
teraEtherStatTxBadFrameTxErr = _TeraEtherStatTxBadFrameTxErr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 26),
    _TeraEtherStatTxBadFrameTxErr_Type()
)
teraEtherStatTxBadFrameTxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxBadFrameTxErr.setStatus("mandatory")
_TeraEtherStatTxBadFrameReset1_Type = Counter32
_TeraEtherStatTxBadFrameReset1_Object = MibTableColumn
teraEtherStatTxBadFrameReset1 = _TeraEtherStatTxBadFrameReset1_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 27),
    _TeraEtherStatTxBadFrameReset1_Type()
)
teraEtherStatTxBadFrameReset1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxBadFrameReset1.setStatus("mandatory")
_TeraEtherStatTxBadFrameReset2_Type = Counter32
_TeraEtherStatTxBadFrameReset2_Object = MibTableColumn
teraEtherStatTxBadFrameReset2 = _TeraEtherStatTxBadFrameReset2_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 28),
    _TeraEtherStatTxBadFrameReset2_Type()
)
teraEtherStatTxBadFrameReset2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxBadFrameReset2.setStatus("mandatory")
_TeraEtherStatTxBadFramePortDisable_Type = Counter32
_TeraEtherStatTxBadFramePortDisable_Object = MibTableColumn
teraEtherStatTxBadFramePortDisable = _TeraEtherStatTxBadFramePortDisable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 29),
    _TeraEtherStatTxBadFramePortDisable_Type()
)
teraEtherStatTxBadFramePortDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEtherStatTxBadFramePortDisable.setStatus("mandatory")


class _TeraEtherStatState_Type(Integer32):
    """Custom type teraEtherStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_TeraEtherStatState_Type.__name__ = "Integer32"
_TeraEtherStatState_Object = MibTableColumn
teraEtherStatState = _TeraEtherStatState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 15, 1, 30),
    _TeraEtherStatState_Type()
)
teraEtherStatState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEtherStatState.setStatus("mandatory")
_TeraLanPolicingTable_Object = MibTable
teraLanPolicingTable = _TeraLanPolicingTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 16)
)
if mibBuilder.loadTexts:
    teraLanPolicingTable.setStatus("mandatory")
_TeraLanPolicingTableEntry_Object = MibTableRow
teraLanPolicingTableEntry = _TeraLanPolicingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 16, 1)
)
teraLanPolicingTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "etherStatsIndex"),
)
if mibBuilder.loadTexts:
    teraLanPolicingTableEntry.setStatus("mandatory")


class _TeraLanIngPolicing_Type(Integer32):
    """Custom type teraLanIngPolicing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_TeraLanIngPolicing_Type.__name__ = "Integer32"
_TeraLanIngPolicing_Object = MibTableColumn
teraLanIngPolicing = _TeraLanIngPolicing_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 16, 1, 1),
    _TeraLanIngPolicing_Type()
)
teraLanIngPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanIngPolicing.setStatus("mandatory")


class _TeraLanIngPolicingInterval_Type(Counter32):
    """Custom type teraLanIngPolicingInterval based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_TeraLanIngPolicingInterval_Type.__name__ = "Counter32"
_TeraLanIngPolicingInterval_Object = MibTableColumn
teraLanIngPolicingInterval = _TeraLanIngPolicingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 16, 1, 2),
    _TeraLanIngPolicingInterval_Type()
)
teraLanIngPolicingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanIngPolicingInterval.setStatus("mandatory")


class _TeraLanIngPolicingRate_Type(Counter32):
    """Custom type teraLanIngPolicingRate based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TeraLanIngPolicingRate_Type.__name__ = "Counter32"
_TeraLanIngPolicingRate_Object = MibTableColumn
teraLanIngPolicingRate = _TeraLanIngPolicingRate_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 16, 1, 3),
    _TeraLanIngPolicingRate_Type()
)
teraLanIngPolicingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanIngPolicingRate.setStatus("mandatory")


class _TeraLanIngPolicingMaxAccr_Type(Counter32):
    """Custom type teraLanIngPolicingMaxAccr based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_TeraLanIngPolicingMaxAccr_Type.__name__ = "Counter32"
_TeraLanIngPolicingMaxAccr_Object = MibTableColumn
teraLanIngPolicingMaxAccr = _TeraLanIngPolicingMaxAccr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 16, 1, 4),
    _TeraLanIngPolicingMaxAccr_Type()
)
teraLanIngPolicingMaxAccr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanIngPolicingMaxAccr.setStatus("mandatory")


class _TeraLanEgrShaping_Type(Integer32):
    """Custom type teraLanEgrShaping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_TeraLanEgrShaping_Type.__name__ = "Integer32"
_TeraLanEgrShaping_Object = MibTableColumn
teraLanEgrShaping = _TeraLanEgrShaping_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 16, 1, 5),
    _TeraLanEgrShaping_Type()
)
teraLanEgrShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanEgrShaping.setStatus("mandatory")


class _TeraLanEgrShapingInterval_Type(Counter32):
    """Custom type teraLanEgrShapingInterval based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_TeraLanEgrShapingInterval_Type.__name__ = "Counter32"
_TeraLanEgrShapingInterval_Object = MibTableColumn
teraLanEgrShapingInterval = _TeraLanEgrShapingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 16, 1, 6),
    _TeraLanEgrShapingInterval_Type()
)
teraLanEgrShapingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanEgrShapingInterval.setStatus("mandatory")


class _TeraLanEgrShapingRate_Type(Counter32):
    """Custom type teraLanEgrShapingRate based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TeraLanEgrShapingRate_Type.__name__ = "Counter32"
_TeraLanEgrShapingRate_Object = MibTableColumn
teraLanEgrShapingRate = _TeraLanEgrShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 16, 1, 7),
    _TeraLanEgrShapingRate_Type()
)
teraLanEgrShapingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanEgrShapingRate.setStatus("mandatory")
_TeraLanUsageHistoryControlTable_Object = MibTable
teraLanUsageHistoryControlTable = _TeraLanUsageHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 17)
)
if mibBuilder.loadTexts:
    teraLanUsageHistoryControlTable.setStatus("mandatory")
_TeraLanUsageHistoryControlTableEntry_Object = MibTableRow
teraLanUsageHistoryControlTableEntry = _TeraLanUsageHistoryControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 17, 1)
)
teraLanUsageHistoryControlTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    teraLanUsageHistoryControlTableEntry.setStatus("mandatory")


class _TeraLanUsageHistoryControlBucketsRequested_Type(Integer32):
    """Custom type teraLanUsageHistoryControlBucketsRequested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraLanUsageHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_TeraLanUsageHistoryControlBucketsRequested_Object = MibTableColumn
teraLanUsageHistoryControlBucketsRequested = _TeraLanUsageHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 17, 1, 1),
    _TeraLanUsageHistoryControlBucketsRequested_Type()
)
teraLanUsageHistoryControlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanUsageHistoryControlBucketsRequested.setStatus("mandatory")


class _TeraLanUsageHistoryControlBucketsGranted_Type(Integer32):
    """Custom type teraLanUsageHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraLanUsageHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_TeraLanUsageHistoryControlBucketsGranted_Object = MibTableColumn
teraLanUsageHistoryControlBucketsGranted = _TeraLanUsageHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 17, 1, 2),
    _TeraLanUsageHistoryControlBucketsGranted_Type()
)
teraLanUsageHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLanUsageHistoryControlBucketsGranted.setStatus("mandatory")


class _TeraLanUsageHistoryControlInterval_Type(Integer32):
    """Custom type teraLanUsageHistoryControlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TeraLanUsageHistoryControlInterval_Type.__name__ = "Integer32"
_TeraLanUsageHistoryControlInterval_Object = MibTableColumn
teraLanUsageHistoryControlInterval = _TeraLanUsageHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 17, 1, 3),
    _TeraLanUsageHistoryControlInterval_Type()
)
teraLanUsageHistoryControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanUsageHistoryControlInterval.setStatus("mandatory")


class _TeraLanUsageHistoryControlStatus_Type(Integer32):
    """Custom type teraLanUsageHistoryControlStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_TeraLanUsageHistoryControlStatus_Type.__name__ = "Integer32"
_TeraLanUsageHistoryControlStatus_Object = MibTableColumn
teraLanUsageHistoryControlStatus = _TeraLanUsageHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 17, 1, 4),
    _TeraLanUsageHistoryControlStatus_Type()
)
teraLanUsageHistoryControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanUsageHistoryControlStatus.setStatus("mandatory")
_TeraLanUsageTable_Object = MibTable
teraLanUsageTable = _TeraLanUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 18)
)
if mibBuilder.loadTexts:
    teraLanUsageTable.setStatus("mandatory")
_TeraLanUsageTableEntry_Object = MibTableRow
teraLanUsageTableEntry = _TeraLanUsageTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 18, 1)
)
teraLanUsageTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    teraLanUsageTableEntry.setStatus("mandatory")
_TeraLanUsageIngRcvBytes_Type = Counter32
_TeraLanUsageIngRcvBytes_Object = MibTableColumn
teraLanUsageIngRcvBytes = _TeraLanUsageIngRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 18, 1, 1),
    _TeraLanUsageIngRcvBytes_Type()
)
teraLanUsageIngRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLanUsageIngRcvBytes.setStatus("mandatory")
_TeraLanUsageIngPolicingDropBytes_Type = Counter32
_TeraLanUsageIngPolicingDropBytes_Object = MibTableColumn
teraLanUsageIngPolicingDropBytes = _TeraLanUsageIngPolicingDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 18, 1, 2),
    _TeraLanUsageIngPolicingDropBytes_Type()
)
teraLanUsageIngPolicingDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLanUsageIngPolicingDropBytes.setStatus("mandatory")
_TeraLanUsageEgrRcvBytes_Type = Counter32
_TeraLanUsageEgrRcvBytes_Object = MibTableColumn
teraLanUsageEgrRcvBytes = _TeraLanUsageEgrRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 18, 1, 3),
    _TeraLanUsageEgrRcvBytes_Type()
)
teraLanUsageEgrRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLanUsageEgrRcvBytes.setStatus("mandatory")
_TeraLanUsageEgrSentBytes_Type = Counter32
_TeraLanUsageEgrSentBytes_Object = MibTableColumn
teraLanUsageEgrSentBytes = _TeraLanUsageEgrSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 18, 1, 4),
    _TeraLanUsageEgrSentBytes_Type()
)
teraLanUsageEgrSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLanUsageEgrSentBytes.setStatus("mandatory")


class _TeraLanUsageStatus_Type(Integer32):
    """Custom type teraLanUsageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_TeraLanUsageStatus_Type.__name__ = "Integer32"
_TeraLanUsageStatus_Object = MibTableColumn
teraLanUsageStatus = _TeraLanUsageStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 18, 1, 5),
    _TeraLanUsageStatus_Type()
)
teraLanUsageStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanUsageStatus.setStatus("mandatory")
_TeraLanUsageHistoryTable_Object = MibTable
teraLanUsageHistoryTable = _TeraLanUsageHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 19)
)
if mibBuilder.loadTexts:
    teraLanUsageHistoryTable.setStatus("mandatory")
_TeraLanUsageHistoryTableEntry_Object = MibTableRow
teraLanUsageHistoryTableEntry = _TeraLanUsageHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 19, 1)
)
teraLanUsageHistoryTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "dot1dBasePort"),
    (0, "TERAWAVE-terabridge-MIB", "teraLanUsageHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    teraLanUsageHistoryTableEntry.setStatus("mandatory")


class _TeraLanUsageHistorySampleIndex_Type(Integer32):
    """Custom type teraLanUsageHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TeraLanUsageHistorySampleIndex_Type.__name__ = "Integer32"
_TeraLanUsageHistorySampleIndex_Object = MibTableColumn
teraLanUsageHistorySampleIndex = _TeraLanUsageHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 19, 1, 1),
    _TeraLanUsageHistorySampleIndex_Type()
)
teraLanUsageHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLanUsageHistorySampleIndex.setStatus("mandatory")
_TeraLanUsageHistoryIntervalStart_Type = Integer32
_TeraLanUsageHistoryIntervalStart_Object = MibTableColumn
teraLanUsageHistoryIntervalStart = _TeraLanUsageHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 19, 1, 2),
    _TeraLanUsageHistoryIntervalStart_Type()
)
teraLanUsageHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLanUsageHistoryIntervalStart.setStatus("mandatory")
_TeraLanUsageHistoryIngRcvBytes_Type = Counter32
_TeraLanUsageHistoryIngRcvBytes_Object = MibTableColumn
teraLanUsageHistoryIngRcvBytes = _TeraLanUsageHistoryIngRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 19, 1, 3),
    _TeraLanUsageHistoryIngRcvBytes_Type()
)
teraLanUsageHistoryIngRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLanUsageHistoryIngRcvBytes.setStatus("mandatory")
_TeraLanUsageHistoryIngPolicingDropBytes_Type = Counter32
_TeraLanUsageHistoryIngPolicingDropBytes_Object = MibTableColumn
teraLanUsageHistoryIngPolicingDropBytes = _TeraLanUsageHistoryIngPolicingDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 19, 1, 4),
    _TeraLanUsageHistoryIngPolicingDropBytes_Type()
)
teraLanUsageHistoryIngPolicingDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLanUsageHistoryIngPolicingDropBytes.setStatus("mandatory")
_TeraLanUsageHistoryEgrRcvBytes_Type = Counter32
_TeraLanUsageHistoryEgrRcvBytes_Object = MibTableColumn
teraLanUsageHistoryEgrRcvBytes = _TeraLanUsageHistoryEgrRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 19, 1, 5),
    _TeraLanUsageHistoryEgrRcvBytes_Type()
)
teraLanUsageHistoryEgrRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLanUsageHistoryEgrRcvBytes.setStatus("mandatory")
_TeraLanUsageHistoryEgrSentBytes_Type = Counter32
_TeraLanUsageHistoryEgrSentBytes_Object = MibTableColumn
teraLanUsageHistoryEgrSentBytes = _TeraLanUsageHistoryEgrSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 19, 1, 6),
    _TeraLanUsageHistoryEgrSentBytes_Type()
)
teraLanUsageHistoryEgrSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLanUsageHistoryEgrSentBytes.setStatus("mandatory")
_TeraLanCardModeTable_Object = MibTable
teraLanCardModeTable = _TeraLanCardModeTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 20)
)
if mibBuilder.loadTexts:
    teraLanCardModeTable.setStatus("mandatory")
_TeraLanCardModeTableEntry_Object = MibTableRow
teraLanCardModeTableEntry = _TeraLanCardModeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 20, 1)
)
teraLanCardModeTableEntry.setIndexNames(
    (0, "TERAWAVE-terabridge-MIB", "teraDot1dTpSlot"),
)
if mibBuilder.loadTexts:
    teraLanCardModeTableEntry.setStatus("mandatory")


class _TeraLanCardMode_Type(Integer32):
    """Custom type teraLanCardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-2", 1),
          ("port-4", 2))
    )


_TeraLanCardMode_Type.__name__ = "Integer32"
_TeraLanCardMode_Object = MibTableColumn
teraLanCardMode = _TeraLanCardMode_Object(
    (1, 3, 6, 1, 4, 1, 4513, 3, 20, 1, 1),
    _TeraLanCardMode_Type()
)
teraLanCardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraLanCardMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-terabridge-MIB",
    **{"terawave": terawave,
       "tera1dBridge": tera1dBridge,
       "teraDot1dStpTable": teraDot1dStpTable,
       "teraDot1dStpTableEntry": teraDot1dStpTableEntry,
       "teraStpId": teraStpId,
       "teraDot1dStpProtocolSpecification": teraDot1dStpProtocolSpecification,
       "teraDot1dStpPriority": teraDot1dStpPriority,
       "teraDot1dStpTimeSinceTopologyChange": teraDot1dStpTimeSinceTopologyChange,
       "teraDot1dStpTopChanges": teraDot1dStpTopChanges,
       "teraDot1dStpDesignatedRoot": teraDot1dStpDesignatedRoot,
       "teraDot1dStpRootCost": teraDot1dStpRootCost,
       "teraDot1dStpRootPort": teraDot1dStpRootPort,
       "teraDot1dStpMaxAge": teraDot1dStpMaxAge,
       "teraDot1dStpHelloTime": teraDot1dStpHelloTime,
       "teraDot1dStpHoldTime": teraDot1dStpHoldTime,
       "teraDot1dStpForwardDelay": teraDot1dStpForwardDelay,
       "teraDot1dStpBridgeMaxAge": teraDot1dStpBridgeMaxAge,
       "teraDot1dStpBridgeHelloTime": teraDot1dStpBridgeHelloTime,
       "teraDot1dStpBridgeForwardDelay": teraDot1dStpBridgeForwardDelay,
       "teraDot1dStpBridgeGroupList": teraDot1dStpBridgeGroupList,
       "teraDot1dStpState": teraDot1dStpState,
       "teraBridgePVCPortTable": teraBridgePVCPortTable,
       "teraBridgePVCPortTableEntry": teraBridgePVCPortTableEntry,
       "teraBridgeEncapsulation": teraBridgeEncapsulation,
       "teraBridgePriority": teraBridgePriority,
       "teraPVCPortLocalHostFilter": teraPVCPortLocalHostFilter,
       "teraPVCPortTrunkFrameType": teraPVCPortTrunkFrameType,
       "teraPVCPortTrunkTagSwap": teraPVCPortTrunkTagSwap,
       "teraDot1dTpPortTable": teraDot1dTpPortTable,
       "teraDot1dTpPortTableEntry": teraDot1dTpPortTableEntry,
       "teraDot1dTpPort": teraDot1dTpPort,
       "teraDot1dFFType": teraDot1dFFType,
       "teraDot1dLoopback": teraDot1dLoopback,
       "teraDot1dTpUseDefaultFwd": teraDot1dTpUseDefaultFwd,
       "teraDot1dTpDefaultFwdPort": teraDot1dTpDefaultFwdPort,
       "teraDot1dStaticTable": teraDot1dStaticTable,
       "teraDot1dStaticTableEntry": teraDot1dStaticTableEntry,
       "teraDot1dStaticReceivePort": teraDot1dStaticReceivePort,
       "teraDot1dStaticAddress": teraDot1dStaticAddress,
       "teraDot1dStaticAllowedToGoTo": teraDot1dStaticAllowedToGoTo,
       "teraDot1dStaticStatus": teraDot1dStaticStatus,
       "teraDot1dBasePortTable": teraDot1dBasePortTable,
       "teraDot1dBasePortTableEntry": teraDot1dBasePortTableEntry,
       "teraDot1dBasePort": teraDot1dBasePort,
       "teraDot1dBaseParentPortIfIndex": teraDot1dBaseParentPortIfIndex,
       "teraDot1dBaseInternalVPI": teraDot1dBaseInternalVPI,
       "teraDot1dBaseInternalVCI": teraDot1dBaseInternalVCI,
       "teraDot1dBaseParentVPI": teraDot1dBaseParentVPI,
       "teraDot1dBaseParentVCI": teraDot1dBaseParentVCI,
       "teraVlanPortGroupTable": teraVlanPortGroupTable,
       "teraVlanPortGroupTableEntry": teraVlanPortGroupTableEntry,
       "dot1qVlanIndex": dot1qVlanIndex,
       "teraVlanPorts": teraVlanPorts,
       "teraVlanPortGroupTableAction": teraVlanPortGroupTableAction,
       "teraDot1qVlanPortTable": teraDot1qVlanPortTable,
       "teraDot1qVlanPortTableEntry": teraDot1qVlanPortTableEntry,
       "teraDot1qVlanPort": teraDot1qVlanPort,
       "teraDot1qVlanPortIngressFrameTypes": teraDot1qVlanPortIngressFrameTypes,
       "teraDot1qVlanPortIngressFiltering": teraDot1qVlanPortIngressFiltering,
       "teraDot1qVlanPortEgressFrameType": teraDot1qVlanPortEgressFrameType,
       "teraDot1qVlanPortEgressTagSwap": teraDot1qVlanPortEgressTagSwap,
       "teraDot1qVlanPortDisUntaggedBcast": teraDot1qVlanPortDisUntaggedBcast,
       "teraDot1dTp": teraDot1dTp,
       "teraDot1dTpEntry": teraDot1dTpEntry,
       "teraDot1dTpSlot": teraDot1dTpSlot,
       "teraDot1dTpProcessor": teraDot1dTpProcessor,
       "teraDot1dTpLearnedEntryDiscards": teraDot1dTpLearnedEntryDiscards,
       "teraDot1dTpAgingTime": teraDot1dTpAgingTime,
       "teraDot1qFdbTable": teraDot1qFdbTable,
       "teraDot1qFdbTableEntry": teraDot1qFdbTableEntry,
       "teraDot1qFdbDynamicCount": teraDot1qFdbDynamicCount,
       "teraDot1qTpFdbTable": teraDot1qTpFdbTable,
       "teraDot1qTpFdbTableEntry": teraDot1qTpFdbTableEntry,
       "teraDot1qTpFdbAddress": teraDot1qTpFdbAddress,
       "teraDot1qTpFdbPort": teraDot1qTpFdbPort,
       "teraDot1qTpFdbStatus": teraDot1qTpFdbStatus,
       "teraDot1dPvcStatTable": teraDot1dPvcStatTable,
       "teraDot1dPvcStatTableEntry": teraDot1dPvcStatTableEntry,
       "teraDot1dPvcStatTxPktCount": teraDot1dPvcStatTxPktCount,
       "teraDot1dPvcStatTxOverrun": teraDot1dPvcStatTxOverrun,
       "teraDot1dPvcStatTxUnderrun": teraDot1dPvcStatTxUnderrun,
       "teraDot1dPvcStatRxPktCount": teraDot1dPvcStatRxPktCount,
       "teraDot1dPvcStatRxOverrun": teraDot1dPvcStatRxOverrun,
       "teraDot1dPvcStatRxUnderrun": teraDot1dPvcStatRxUnderrun,
       "teraDot1dPvcStatRxCrcError": teraDot1dPvcStatRxCrcError,
       "teraDot1dPvcStatRxLengthError": teraDot1dPvcStatRxLengthError,
       "teraDot1dPvcStatRxAbort": teraDot1dPvcStatRxAbort,
       "teraDot1dPvcStatRxSlip": teraDot1dPvcStatRxSlip,
       "teraDot1dPvcStatRxNoBuffer": teraDot1dPvcStatRxNoBuffer,
       "teraDot1dPvcStatState": teraDot1dPvcStatState,
       "teraBridgeConnIdTable": teraBridgeConnIdTable,
       "teraBridgeConnIdTableEntry": teraBridgeConnIdTableEntry,
       "teraPvcLogPortId": teraPvcLogPortId,
       "teraConnId": teraConnId,
       "teraVlanStatTable": teraVlanStatTable,
       "teraVlanStatTableEntry": teraVlanStatTableEntry,
       "teraVlanStatState": teraVlanStatState,
       "teraVlanStatRxMcastSrcAddr": teraVlanStatRxMcastSrcAddr,
       "teraVlanStatRxInvalidVlanId": teraVlanStatRxInvalidVlanId,
       "teraVlanStatRxMacAddrNotInStaticTbl": teraVlanStatRxMacAddrNotInStaticTbl,
       "teraVlanStatRxMacAddrInStaticTbl": teraVlanStatRxMacAddrInStaticTbl,
       "teraVlanStatRxInvalidOutPort": teraVlanStatRxInvalidOutPort,
       "teraVlanStatRxInvalidInPort": teraVlanStatRxInvalidInPort,
       "teraVlanStatRxDestMacAddrDisallowed": teraVlanStatRxDestMacAddrDisallowed,
       "teraVlanStatRxPortBlocked": teraVlanStatRxPortBlocked,
       "teraVlanStatRxDiscardTaggedFrame": teraVlanStatRxDiscardTaggedFrame,
       "teraVlanStatRxDiscardUntaggedFrame": teraVlanStatRxDiscardUntaggedFrame,
       "teraVlanStatRxDiscardBcastBlocked": teraVlanStatRxDiscardBcastBlocked,
       "teraVlanStatRxDiscardLocalDest": teraVlanStatRxDiscardLocalDest,
       "teraVlanStatRxFFTypeMismatch": teraVlanStatRxFFTypeMismatch,
       "teraVlanStatRxNoBuffer": teraVlanStatRxNoBuffer,
       "teraVlanStatRxTxFail": teraVlanStatRxTxFail,
       "teraVlanStatRxInvalidEncap": teraVlanStatRxInvalidEncap,
       "teraEtherStatTable": teraEtherStatTable,
       "teraEtherStatTableEntry": teraEtherStatTableEntry,
       "teraEtherStatRxTotalFrames": teraEtherStatRxTotalFrames,
       "teraEtherStatRxGoodFrames": teraEtherStatRxGoodFrames,
       "teraEtherStatRxForwardFrames": teraEtherStatRxForwardFrames,
       "teraEtherStatRxForwardOctets": teraEtherStatRxForwardOctets,
       "teraEtherStatRxPause": teraEtherStatRxPause,
       "teraEtherStatRxTotalDiscard": teraEtherStatRxTotalDiscard,
       "teraEtherStatRxNoBuffer": teraEtherStatRxNoBuffer,
       "teraEtherStatRxTotalBadFrames": teraEtherStatRxTotalBadFrames,
       "teraEtherStatRxBadFrameLenViolation": teraEtherStatRxBadFrameLenViolation,
       "teraEtherStatRxBadFrameNotAlign": teraEtherStatRxBadFrameNotAlign,
       "teraEtherStatRxBadFrameTooShort": teraEtherStatRxBadFrameTooShort,
       "teraEtherStatRxBadFrameCRC": teraEtherStatRxBadFrameCRC,
       "teraEtherStatRxBadFrameOverrun": teraEtherStatRxBadFrameOverrun,
       "teraEtherStatRxBadFrameCollision": teraEtherStatRxBadFrameCollision,
       "teraEtherStatTxTotalFrames": teraEtherStatTxTotalFrames,
       "teraEtherStatTxGoodFrames": teraEtherStatTxGoodFrames,
       "teraEtherStatTxFramesSentOut": teraEtherStatTxFramesSentOut,
       "teraEtherStatTxOctets": teraEtherStatTxOctets,
       "teraEtherStatTxPause": teraEtherStatTxPause,
       "teraEtherStatTxQueueOverflow": teraEtherStatTxQueueOverflow,
       "teraEtherStatTxTotalBadFrames": teraEtherStatTxTotalBadFrames,
       "teraEtherStatTxBadFrameCarrierLost": teraEtherStatTxBadFrameCarrierLost,
       "teraEtherStatTxBadFrameUnderrun": teraEtherStatTxBadFrameUnderrun,
       "teraEtherStatTxBadFrameRexmitLimit": teraEtherStatTxBadFrameRexmitLimit,
       "teraEtherStatTxBadFrameLateCollision": teraEtherStatTxBadFrameLateCollision,
       "teraEtherStatTxBadFrameTxErr": teraEtherStatTxBadFrameTxErr,
       "teraEtherStatTxBadFrameReset1": teraEtherStatTxBadFrameReset1,
       "teraEtherStatTxBadFrameReset2": teraEtherStatTxBadFrameReset2,
       "teraEtherStatTxBadFramePortDisable": teraEtherStatTxBadFramePortDisable,
       "teraEtherStatState": teraEtherStatState,
       "teraLanPolicingTable": teraLanPolicingTable,
       "teraLanPolicingTableEntry": teraLanPolicingTableEntry,
       "teraLanIngPolicing": teraLanIngPolicing,
       "teraLanIngPolicingInterval": teraLanIngPolicingInterval,
       "teraLanIngPolicingRate": teraLanIngPolicingRate,
       "teraLanIngPolicingMaxAccr": teraLanIngPolicingMaxAccr,
       "teraLanEgrShaping": teraLanEgrShaping,
       "teraLanEgrShapingInterval": teraLanEgrShapingInterval,
       "teraLanEgrShapingRate": teraLanEgrShapingRate,
       "teraLanUsageHistoryControlTable": teraLanUsageHistoryControlTable,
       "teraLanUsageHistoryControlTableEntry": teraLanUsageHistoryControlTableEntry,
       "teraLanUsageHistoryControlBucketsRequested": teraLanUsageHistoryControlBucketsRequested,
       "teraLanUsageHistoryControlBucketsGranted": teraLanUsageHistoryControlBucketsGranted,
       "teraLanUsageHistoryControlInterval": teraLanUsageHistoryControlInterval,
       "teraLanUsageHistoryControlStatus": teraLanUsageHistoryControlStatus,
       "teraLanUsageTable": teraLanUsageTable,
       "teraLanUsageTableEntry": teraLanUsageTableEntry,
       "teraLanUsageIngRcvBytes": teraLanUsageIngRcvBytes,
       "teraLanUsageIngPolicingDropBytes": teraLanUsageIngPolicingDropBytes,
       "teraLanUsageEgrRcvBytes": teraLanUsageEgrRcvBytes,
       "teraLanUsageEgrSentBytes": teraLanUsageEgrSentBytes,
       "teraLanUsageStatus": teraLanUsageStatus,
       "teraLanUsageHistoryTable": teraLanUsageHistoryTable,
       "teraLanUsageHistoryTableEntry": teraLanUsageHistoryTableEntry,
       "teraLanUsageHistorySampleIndex": teraLanUsageHistorySampleIndex,
       "teraLanUsageHistoryIntervalStart": teraLanUsageHistoryIntervalStart,
       "teraLanUsageHistoryIngRcvBytes": teraLanUsageHistoryIngRcvBytes,
       "teraLanUsageHistoryIngPolicingDropBytes": teraLanUsageHistoryIngPolicingDropBytes,
       "teraLanUsageHistoryEgrRcvBytes": teraLanUsageHistoryEgrRcvBytes,
       "teraLanUsageHistoryEgrSentBytes": teraLanUsageHistoryEgrSentBytes,
       "teraLanCardModeTable": teraLanCardModeTable,
       "teraLanCardModeTableEntry": teraLanCardModeTableEntry,
       "teraLanCardMode": teraLanCardMode}
)
