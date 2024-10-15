# SNMP MIB module (RFC1286-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1286-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:10 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17)
)
_Dot1dBase_ObjectIdentity = ObjectIdentity
dot1dBase = _Dot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 1)
)
_Dot1dBaseBridgeAddress_Type = MacAddress
_Dot1dBaseBridgeAddress_Object = MibScalar
dot1dBaseBridgeAddress = _Dot1dBaseBridgeAddress_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 1),
    _Dot1dBaseBridgeAddress_Type()
)
dot1dBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseBridgeAddress.setStatus("mandatory")
_Dot1dBaseNumPorts_Type = Integer32
_Dot1dBaseNumPorts_Object = MibScalar
dot1dBaseNumPorts = _Dot1dBaseNumPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 2),
    _Dot1dBaseNumPorts_Type()
)
dot1dBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseNumPorts.setStatus("mandatory")


class _Dot1dBaseType_Type(Integer32):
    """Custom type dot1dBaseType based on Integer32"""
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
        *(("sourceroute-only", 3),
          ("srt", 4),
          ("transparent-only", 2),
          ("unknown", 1))
    )


_Dot1dBaseType_Type.__name__ = "Integer32"
_Dot1dBaseType_Object = MibScalar
dot1dBaseType = _Dot1dBaseType_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 3),
    _Dot1dBaseType_Type()
)
dot1dBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseType.setStatus("mandatory")
_Dot1dBasePortTable_Object = MibTable
dot1dBasePortTable = _Dot1dBasePortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4)
)
if mibBuilder.loadTexts:
    dot1dBasePortTable.setStatus("mandatory")
_Dot1dBasePortEntry_Object = MibTableRow
dot1dBasePortEntry = _Dot1dBasePortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1)
)
dot1dBasePortEntry.setIndexNames(
    (0, "RFC1286-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dot1dBasePortEntry.setStatus("mandatory")
_Dot1dBasePort_Type = Integer32
_Dot1dBasePort_Object = MibTableColumn
dot1dBasePort = _Dot1dBasePort_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 1),
    _Dot1dBasePort_Type()
)
dot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePort.setStatus("mandatory")
_Dot1dBasePortIfIndex_Type = Integer32
_Dot1dBasePortIfIndex_Object = MibTableColumn
dot1dBasePortIfIndex = _Dot1dBasePortIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 2),
    _Dot1dBasePortIfIndex_Type()
)
dot1dBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortIfIndex.setStatus("mandatory")
_Dot1dBasePortCircuit_Type = ObjectIdentifier
_Dot1dBasePortCircuit_Object = MibTableColumn
dot1dBasePortCircuit = _Dot1dBasePortCircuit_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 3),
    _Dot1dBasePortCircuit_Type()
)
dot1dBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortCircuit.setStatus("mandatory")
_Dot1dBasePortDelayExceededDiscards_Type = Counter32
_Dot1dBasePortDelayExceededDiscards_Object = MibTableColumn
dot1dBasePortDelayExceededDiscards = _Dot1dBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 4),
    _Dot1dBasePortDelayExceededDiscards_Type()
)
dot1dBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortDelayExceededDiscards.setStatus("mandatory")
_Dot1dBasePortMtuExceededDiscards_Type = Counter32
_Dot1dBasePortMtuExceededDiscards_Object = MibTableColumn
dot1dBasePortMtuExceededDiscards = _Dot1dBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 5),
    _Dot1dBasePortMtuExceededDiscards_Type()
)
dot1dBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortMtuExceededDiscards.setStatus("mandatory")
_Dot1dStp_ObjectIdentity = ObjectIdentity
dot1dStp = _Dot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 2)
)


class _Dot1dStpProtocolSpecification_Type(Integer32):
    """Custom type dot1dStpProtocolSpecification based on Integer32"""
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


_Dot1dStpProtocolSpecification_Type.__name__ = "Integer32"
_Dot1dStpProtocolSpecification_Object = MibScalar
dot1dStpProtocolSpecification = _Dot1dStpProtocolSpecification_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 1),
    _Dot1dStpProtocolSpecification_Type()
)
dot1dStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpProtocolSpecification.setStatus("mandatory")


class _Dot1dStpPriority_Type(Integer32):
    """Custom type dot1dStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1dStpPriority_Type.__name__ = "Integer32"
_Dot1dStpPriority_Object = MibScalar
dot1dStpPriority = _Dot1dStpPriority_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 2),
    _Dot1dStpPriority_Type()
)
dot1dStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPriority.setStatus("mandatory")
_Dot1dStpTimeSinceTopologyChange_Type = TimeTicks
_Dot1dStpTimeSinceTopologyChange_Object = MibScalar
dot1dStpTimeSinceTopologyChange = _Dot1dStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 3),
    _Dot1dStpTimeSinceTopologyChange_Type()
)
dot1dStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpTimeSinceTopologyChange.setStatus("mandatory")
_Dot1dStpTopChanges_Type = Counter32
_Dot1dStpTopChanges_Object = MibScalar
dot1dStpTopChanges = _Dot1dStpTopChanges_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 4),
    _Dot1dStpTopChanges_Type()
)
dot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpTopChanges.setStatus("mandatory")
_Dot1dStpDesignatedRoot_Type = BridgeId
_Dot1dStpDesignatedRoot_Object = MibScalar
dot1dStpDesignatedRoot = _Dot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 5),
    _Dot1dStpDesignatedRoot_Type()
)
dot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpDesignatedRoot.setStatus("mandatory")
_Dot1dStpRootCost_Type = Integer32
_Dot1dStpRootCost_Object = MibScalar
dot1dStpRootCost = _Dot1dStpRootCost_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 6),
    _Dot1dStpRootCost_Type()
)
dot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpRootCost.setStatus("mandatory")
_Dot1dStpRootPort_Type = Integer32
_Dot1dStpRootPort_Object = MibScalar
dot1dStpRootPort = _Dot1dStpRootPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 7),
    _Dot1dStpRootPort_Type()
)
dot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpRootPort.setStatus("mandatory")
_Dot1dStpMaxAge_Type = Timeout
_Dot1dStpMaxAge_Object = MibScalar
dot1dStpMaxAge = _Dot1dStpMaxAge_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 8),
    _Dot1dStpMaxAge_Type()
)
dot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpMaxAge.setStatus("mandatory")
_Dot1dStpHelloTime_Type = Timeout
_Dot1dStpHelloTime_Object = MibScalar
dot1dStpHelloTime = _Dot1dStpHelloTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 9),
    _Dot1dStpHelloTime_Type()
)
dot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpHelloTime.setStatus("mandatory")
_Dot1dStpHoldTime_Type = Integer32
_Dot1dStpHoldTime_Object = MibScalar
dot1dStpHoldTime = _Dot1dStpHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 10),
    _Dot1dStpHoldTime_Type()
)
dot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpHoldTime.setStatus("mandatory")
_Dot1dStpForwardDelay_Type = Timeout
_Dot1dStpForwardDelay_Object = MibScalar
dot1dStpForwardDelay = _Dot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 11),
    _Dot1dStpForwardDelay_Type()
)
dot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpForwardDelay.setStatus("mandatory")


class _Dot1dStpBridgeMaxAge_Type(Timeout):
    """Custom type dot1dStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_Dot1dStpBridgeMaxAge_Type.__name__ = "Timeout"
_Dot1dStpBridgeMaxAge_Object = MibScalar
dot1dStpBridgeMaxAge = _Dot1dStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 12),
    _Dot1dStpBridgeMaxAge_Type()
)
dot1dStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeMaxAge.setStatus("mandatory")


class _Dot1dStpBridgeHelloTime_Type(Timeout):
    """Custom type dot1dStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_Dot1dStpBridgeHelloTime_Type.__name__ = "Timeout"
_Dot1dStpBridgeHelloTime_Object = MibScalar
dot1dStpBridgeHelloTime = _Dot1dStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 13),
    _Dot1dStpBridgeHelloTime_Type()
)
dot1dStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeHelloTime.setStatus("mandatory")


class _Dot1dStpBridgeForwardDelay_Type(Timeout):
    """Custom type dot1dStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_Dot1dStpBridgeForwardDelay_Type.__name__ = "Timeout"
_Dot1dStpBridgeForwardDelay_Object = MibScalar
dot1dStpBridgeForwardDelay = _Dot1dStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 14),
    _Dot1dStpBridgeForwardDelay_Type()
)
dot1dStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeForwardDelay.setStatus("mandatory")
_Dot1dStpPortTable_Object = MibTable
dot1dStpPortTable = _Dot1dStpPortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15)
)
if mibBuilder.loadTexts:
    dot1dStpPortTable.setStatus("mandatory")
_Dot1dStpPortEntry_Object = MibTableRow
dot1dStpPortEntry = _Dot1dStpPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1)
)
dot1dStpPortEntry.setIndexNames(
    (0, "RFC1286-MIB", "dot1dStpPort"),
)
if mibBuilder.loadTexts:
    dot1dStpPortEntry.setStatus("mandatory")
_Dot1dStpPort_Type = Integer32
_Dot1dStpPort_Object = MibTableColumn
dot1dStpPort = _Dot1dStpPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 1),
    _Dot1dStpPort_Type()
)
dot1dStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPort.setStatus("mandatory")


class _Dot1dStpPortPriority_Type(Integer32):
    """Custom type dot1dStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1dStpPortPriority_Type.__name__ = "Integer32"
_Dot1dStpPortPriority_Object = MibTableColumn
dot1dStpPortPriority = _Dot1dStpPortPriority_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 2),
    _Dot1dStpPortPriority_Type()
)
dot1dStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortPriority.setStatus("mandatory")


class _Dot1dStpPortState_Type(Integer32):
    """Custom type dot1dStpPortState based on Integer32"""
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


_Dot1dStpPortState_Type.__name__ = "Integer32"
_Dot1dStpPortState_Object = MibTableColumn
dot1dStpPortState = _Dot1dStpPortState_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 3),
    _Dot1dStpPortState_Type()
)
dot1dStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortState.setStatus("mandatory")


class _Dot1dStpPortEnable_Type(Integer32):
    """Custom type dot1dStpPortEnable based on Integer32"""
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


_Dot1dStpPortEnable_Type.__name__ = "Integer32"
_Dot1dStpPortEnable_Object = MibTableColumn
dot1dStpPortEnable = _Dot1dStpPortEnable_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 4),
    _Dot1dStpPortEnable_Type()
)
dot1dStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortEnable.setStatus("mandatory")


class _Dot1dStpPortPathCost_Type(Integer32):
    """Custom type dot1dStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dStpPortPathCost_Type.__name__ = "Integer32"
_Dot1dStpPortPathCost_Object = MibTableColumn
dot1dStpPortPathCost = _Dot1dStpPortPathCost_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 5),
    _Dot1dStpPortPathCost_Type()
)
dot1dStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortPathCost.setStatus("mandatory")
_Dot1dStpPortDesignatedRoot_Type = BridgeId
_Dot1dStpPortDesignatedRoot_Object = MibTableColumn
dot1dStpPortDesignatedRoot = _Dot1dStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 6),
    _Dot1dStpPortDesignatedRoot_Type()
)
dot1dStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedRoot.setStatus("mandatory")
_Dot1dStpPortDesignatedCost_Type = Integer32
_Dot1dStpPortDesignatedCost_Object = MibTableColumn
dot1dStpPortDesignatedCost = _Dot1dStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 7),
    _Dot1dStpPortDesignatedCost_Type()
)
dot1dStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedCost.setStatus("mandatory")
_Dot1dStpPortDesignatedBridge_Type = BridgeId
_Dot1dStpPortDesignatedBridge_Object = MibTableColumn
dot1dStpPortDesignatedBridge = _Dot1dStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 8),
    _Dot1dStpPortDesignatedBridge_Type()
)
dot1dStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedBridge.setStatus("mandatory")


class _Dot1dStpPortDesignatedPort_Type(OctetString):
    """Custom type dot1dStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Dot1dStpPortDesignatedPort_Type.__name__ = "OctetString"
_Dot1dStpPortDesignatedPort_Object = MibTableColumn
dot1dStpPortDesignatedPort = _Dot1dStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 9),
    _Dot1dStpPortDesignatedPort_Type()
)
dot1dStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedPort.setStatus("mandatory")
_Dot1dStpPortForwardTransitions_Type = Counter32
_Dot1dStpPortForwardTransitions_Object = MibTableColumn
dot1dStpPortForwardTransitions = _Dot1dStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 10),
    _Dot1dStpPortForwardTransitions_Type()
)
dot1dStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortForwardTransitions.setStatus("mandatory")
_Dot1dSr_ObjectIdentity = ObjectIdentity
dot1dSr = _Dot1dSr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 3)
)
_Dot1dSrPortTable_Object = MibTable
dot1dSrPortTable = _Dot1dSrPortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    dot1dSrPortTable.setStatus("mandatory")
_Dot1dSrPortEntry_Object = MibTableRow
dot1dSrPortEntry = _Dot1dSrPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1)
)
dot1dSrPortEntry.setIndexNames(
    (0, "RFC1286-MIB", "dot1dSrPort"),
)
if mibBuilder.loadTexts:
    dot1dSrPortEntry.setStatus("mandatory")
_Dot1dSrPort_Type = Integer32
_Dot1dSrPort_Object = MibTableColumn
dot1dSrPort = _Dot1dSrPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 1),
    _Dot1dSrPort_Type()
)
dot1dSrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPort.setStatus("mandatory")
_Dot1dSrPortHopCount_Type = Integer32
_Dot1dSrPortHopCount_Object = MibTableColumn
dot1dSrPortHopCount = _Dot1dSrPortHopCount_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 2),
    _Dot1dSrPortHopCount_Type()
)
dot1dSrPortHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortHopCount.setStatus("mandatory")
_Dot1dSrPortLocalSegment_Type = Integer32
_Dot1dSrPortLocalSegment_Object = MibTableColumn
dot1dSrPortLocalSegment = _Dot1dSrPortLocalSegment_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 3),
    _Dot1dSrPortLocalSegment_Type()
)
dot1dSrPortLocalSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortLocalSegment.setStatus("mandatory")
_Dot1dSrPortBridgeNum_Type = Integer32
_Dot1dSrPortBridgeNum_Object = MibTableColumn
dot1dSrPortBridgeNum = _Dot1dSrPortBridgeNum_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 4),
    _Dot1dSrPortBridgeNum_Type()
)
dot1dSrPortBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortBridgeNum.setStatus("mandatory")
_Dot1dSrPortTargetSegment_Type = Integer32
_Dot1dSrPortTargetSegment_Object = MibTableColumn
dot1dSrPortTargetSegment = _Dot1dSrPortTargetSegment_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 5),
    _Dot1dSrPortTargetSegment_Type()
)
dot1dSrPortTargetSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortTargetSegment.setStatus("mandatory")


class _Dot1dSrPortLargestFrame_Type(Integer32):
    """Custom type dot1dSrPortLargestFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(516,
              1500,
              2052,
              4472,
              8144,
              11407,
              17800,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("dot1dSrMtu11407", 11407),
          ("dot1dSrMtu1500", 1500),
          ("dot1dSrMtu17800", 17800),
          ("dot1dSrMtu2052", 2052),
          ("dot1dSrMtu4472", 4472),
          ("dot1dSrMtu516", 516),
          ("dot1dSrMtu65535", 65535),
          ("dot1dSrMtu8144", 8144))
    )


_Dot1dSrPortLargestFrame_Type.__name__ = "Integer32"
_Dot1dSrPortLargestFrame_Object = MibTableColumn
dot1dSrPortLargestFrame = _Dot1dSrPortLargestFrame_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 6),
    _Dot1dSrPortLargestFrame_Type()
)
dot1dSrPortLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortLargestFrame.setStatus("mandatory")


class _Dot1dSrPortSTESpanMode_Type(Integer32):
    """Custom type dot1dSrPortSTESpanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-span", 1),
          ("disabled", 2),
          ("forced", 3))
    )


_Dot1dSrPortSTESpanMode_Type.__name__ = "Integer32"
_Dot1dSrPortSTESpanMode_Object = MibTableColumn
dot1dSrPortSTESpanMode = _Dot1dSrPortSTESpanMode_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 7),
    _Dot1dSrPortSTESpanMode_Type()
)
dot1dSrPortSTESpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortSTESpanMode.setStatus("mandatory")
_Dot1dSrPortSpecInFrames_Type = Counter32
_Dot1dSrPortSpecInFrames_Object = MibTableColumn
dot1dSrPortSpecInFrames = _Dot1dSrPortSpecInFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 8),
    _Dot1dSrPortSpecInFrames_Type()
)
dot1dSrPortSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortSpecInFrames.setStatus("mandatory")
_Dot1dSrPortSpecOutFrames_Type = Counter32
_Dot1dSrPortSpecOutFrames_Object = MibTableColumn
dot1dSrPortSpecOutFrames = _Dot1dSrPortSpecOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 9),
    _Dot1dSrPortSpecOutFrames_Type()
)
dot1dSrPortSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortSpecOutFrames.setStatus("mandatory")
_Dot1dSrPortApeInFrames_Type = Counter32
_Dot1dSrPortApeInFrames_Object = MibTableColumn
dot1dSrPortApeInFrames = _Dot1dSrPortApeInFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 10),
    _Dot1dSrPortApeInFrames_Type()
)
dot1dSrPortApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortApeInFrames.setStatus("mandatory")
_Dot1dSrPortApeOutFrames_Type = Counter32
_Dot1dSrPortApeOutFrames_Object = MibTableColumn
dot1dSrPortApeOutFrames = _Dot1dSrPortApeOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 11),
    _Dot1dSrPortApeOutFrames_Type()
)
dot1dSrPortApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortApeOutFrames.setStatus("mandatory")
_Dot1dSrPortSteInFrames_Type = Counter32
_Dot1dSrPortSteInFrames_Object = MibTableColumn
dot1dSrPortSteInFrames = _Dot1dSrPortSteInFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 12),
    _Dot1dSrPortSteInFrames_Type()
)
dot1dSrPortSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortSteInFrames.setStatus("mandatory")
_Dot1dSrPortSteOutFrames_Type = Counter32
_Dot1dSrPortSteOutFrames_Object = MibTableColumn
dot1dSrPortSteOutFrames = _Dot1dSrPortSteOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 13),
    _Dot1dSrPortSteOutFrames_Type()
)
dot1dSrPortSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortSteOutFrames.setStatus("mandatory")
_Dot1dSrPortSegmentMismatchDiscards_Type = Counter32
_Dot1dSrPortSegmentMismatchDiscards_Object = MibTableColumn
dot1dSrPortSegmentMismatchDiscards = _Dot1dSrPortSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 14),
    _Dot1dSrPortSegmentMismatchDiscards_Type()
)
dot1dSrPortSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortSegmentMismatchDiscards.setStatus("mandatory")
_Dot1dSrPortDuplicateSegmentDiscards_Type = Counter32
_Dot1dSrPortDuplicateSegmentDiscards_Object = MibTableColumn
dot1dSrPortDuplicateSegmentDiscards = _Dot1dSrPortDuplicateSegmentDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 15),
    _Dot1dSrPortDuplicateSegmentDiscards_Type()
)
dot1dSrPortDuplicateSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortDuplicateSegmentDiscards.setStatus("mandatory")
_Dot1dSrPortHopCountExceededDiscards_Type = Counter32
_Dot1dSrPortHopCountExceededDiscards_Object = MibTableColumn
dot1dSrPortHopCountExceededDiscards = _Dot1dSrPortHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 16),
    _Dot1dSrPortHopCountExceededDiscards_Type()
)
dot1dSrPortHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortHopCountExceededDiscards.setStatus("mandatory")
_Dot1dTp_ObjectIdentity = ObjectIdentity
dot1dTp = _Dot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 4)
)
_Dot1dTpLearnedEntryDiscards_Type = Counter32
_Dot1dTpLearnedEntryDiscards_Object = MibScalar
dot1dTpLearnedEntryDiscards = _Dot1dTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 1),
    _Dot1dTpLearnedEntryDiscards_Type()
)
dot1dTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpLearnedEntryDiscards.setStatus("mandatory")
_Dot1dTpAgingTime_Type = Integer32
_Dot1dTpAgingTime_Object = MibScalar
dot1dTpAgingTime = _Dot1dTpAgingTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 2),
    _Dot1dTpAgingTime_Type()
)
dot1dTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dTpAgingTime.setStatus("mandatory")
_Dot1dTpFdbTable_Object = MibTable
dot1dTpFdbTable = _Dot1dTpFdbTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 3)
)
if mibBuilder.loadTexts:
    dot1dTpFdbTable.setStatus("mandatory")
_Dot1dTpFdbEntry_Object = MibTableRow
dot1dTpFdbEntry = _Dot1dTpFdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1)
)
dot1dTpFdbEntry.setIndexNames(
    (0, "RFC1286-MIB", "dot1dTpFdbAddress"),
)
if mibBuilder.loadTexts:
    dot1dTpFdbEntry.setStatus("mandatory")
_Dot1dTpFdbAddress_Type = MacAddress
_Dot1dTpFdbAddress_Object = MibTableColumn
dot1dTpFdbAddress = _Dot1dTpFdbAddress_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 1),
    _Dot1dTpFdbAddress_Type()
)
dot1dTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpFdbAddress.setStatus("mandatory")
_Dot1dTpFdbPort_Type = Integer32
_Dot1dTpFdbPort_Object = MibTableColumn
dot1dTpFdbPort = _Dot1dTpFdbPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 2),
    _Dot1dTpFdbPort_Type()
)
dot1dTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpFdbPort.setStatus("mandatory")


class _Dot1dTpFdbStatus_Type(Integer32):
    """Custom type dot1dTpFdbStatus based on Integer32"""
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


_Dot1dTpFdbStatus_Type.__name__ = "Integer32"
_Dot1dTpFdbStatus_Object = MibTableColumn
dot1dTpFdbStatus = _Dot1dTpFdbStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 3),
    _Dot1dTpFdbStatus_Type()
)
dot1dTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpFdbStatus.setStatus("mandatory")
_Dot1dTpPortTable_Object = MibTable
dot1dTpPortTable = _Dot1dTpPortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4)
)
if mibBuilder.loadTexts:
    dot1dTpPortTable.setStatus("mandatory")
_Dot1dTpPortEntry_Object = MibTableRow
dot1dTpPortEntry = _Dot1dTpPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1)
)
dot1dTpPortEntry.setIndexNames(
    (0, "RFC1286-MIB", "dot1dTpPort"),
)
if mibBuilder.loadTexts:
    dot1dTpPortEntry.setStatus("mandatory")
_Dot1dTpPort_Type = Integer32
_Dot1dTpPort_Object = MibTableColumn
dot1dTpPort = _Dot1dTpPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 1),
    _Dot1dTpPort_Type()
)
dot1dTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPort.setStatus("mandatory")
_Dot1dTpPortMaxInfo_Type = Integer32
_Dot1dTpPortMaxInfo_Object = MibTableColumn
dot1dTpPortMaxInfo = _Dot1dTpPortMaxInfo_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 2),
    _Dot1dTpPortMaxInfo_Type()
)
dot1dTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortMaxInfo.setStatus("mandatory")
_Dot1dTpPortInFrames_Type = Counter32
_Dot1dTpPortInFrames_Object = MibTableColumn
dot1dTpPortInFrames = _Dot1dTpPortInFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 3),
    _Dot1dTpPortInFrames_Type()
)
dot1dTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInFrames.setStatus("mandatory")
_Dot1dTpPortOutFrames_Type = Counter32
_Dot1dTpPortOutFrames_Object = MibTableColumn
dot1dTpPortOutFrames = _Dot1dTpPortOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 4),
    _Dot1dTpPortOutFrames_Type()
)
dot1dTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortOutFrames.setStatus("mandatory")
_Dot1dTpPortInDiscards_Type = Counter32
_Dot1dTpPortInDiscards_Object = MibTableColumn
dot1dTpPortInDiscards = _Dot1dTpPortInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 5),
    _Dot1dTpPortInDiscards_Type()
)
dot1dTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInDiscards.setStatus("mandatory")
_Dot1dStatic_ObjectIdentity = ObjectIdentity
dot1dStatic = _Dot1dStatic_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 5)
)
_Dot1dStaticTable_Object = MibTable
dot1dStaticTable = _Dot1dStaticTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1)
)
if mibBuilder.loadTexts:
    dot1dStaticTable.setStatus("mandatory")
_Dot1dStaticEntry_Object = MibTableRow
dot1dStaticEntry = _Dot1dStaticEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1)
)
dot1dStaticEntry.setIndexNames(
    (0, "RFC1286-MIB", "dot1dStaticAddress"),
    (0, "RFC1286-MIB", "dot1dStaticReceivePort"),
)
if mibBuilder.loadTexts:
    dot1dStaticEntry.setStatus("mandatory")
_Dot1dStaticAddress_Type = MacAddress
_Dot1dStaticAddress_Object = MibTableColumn
dot1dStaticAddress = _Dot1dStaticAddress_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 1),
    _Dot1dStaticAddress_Type()
)
dot1dStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStaticAddress.setStatus("mandatory")
_Dot1dStaticReceivePort_Type = Integer32
_Dot1dStaticReceivePort_Object = MibTableColumn
dot1dStaticReceivePort = _Dot1dStaticReceivePort_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 2),
    _Dot1dStaticReceivePort_Type()
)
dot1dStaticReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStaticReceivePort.setStatus("mandatory")
_Dot1dStaticAllowedToGoTo_Type = OctetString
_Dot1dStaticAllowedToGoTo_Object = MibTableColumn
dot1dStaticAllowedToGoTo = _Dot1dStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 3),
    _Dot1dStaticAllowedToGoTo_Type()
)
dot1dStaticAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStaticAllowedToGoTo.setStatus("mandatory")


class _Dot1dStaticStatus_Type(Integer32):
    """Custom type dot1dStaticStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_Dot1dStaticStatus_Type.__name__ = "Integer32"
_Dot1dStaticStatus_Object = MibTableColumn
dot1dStaticStatus = _Dot1dStaticStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 4),
    _Dot1dStaticStatus_Type()
)
dot1dStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStaticStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

newRoot = NotificationType(
    (1, 3, 6, 1, 2, 1, 17, 0, 1)
)
if mibBuilder.loadTexts:
    newRoot.setStatus(
        ""
    )

topologyChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 17, 0, 2)
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1286-MIB",
    **{"MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "dot1dBridge": dot1dBridge,
       "newRoot": newRoot,
       "topologyChange": topologyChange,
       "dot1dBase": dot1dBase,
       "dot1dBaseBridgeAddress": dot1dBaseBridgeAddress,
       "dot1dBaseNumPorts": dot1dBaseNumPorts,
       "dot1dBaseType": dot1dBaseType,
       "dot1dBasePortTable": dot1dBasePortTable,
       "dot1dBasePortEntry": dot1dBasePortEntry,
       "dot1dBasePort": dot1dBasePort,
       "dot1dBasePortIfIndex": dot1dBasePortIfIndex,
       "dot1dBasePortCircuit": dot1dBasePortCircuit,
       "dot1dBasePortDelayExceededDiscards": dot1dBasePortDelayExceededDiscards,
       "dot1dBasePortMtuExceededDiscards": dot1dBasePortMtuExceededDiscards,
       "dot1dStp": dot1dStp,
       "dot1dStpProtocolSpecification": dot1dStpProtocolSpecification,
       "dot1dStpPriority": dot1dStpPriority,
       "dot1dStpTimeSinceTopologyChange": dot1dStpTimeSinceTopologyChange,
       "dot1dStpTopChanges": dot1dStpTopChanges,
       "dot1dStpDesignatedRoot": dot1dStpDesignatedRoot,
       "dot1dStpRootCost": dot1dStpRootCost,
       "dot1dStpRootPort": dot1dStpRootPort,
       "dot1dStpMaxAge": dot1dStpMaxAge,
       "dot1dStpHelloTime": dot1dStpHelloTime,
       "dot1dStpHoldTime": dot1dStpHoldTime,
       "dot1dStpForwardDelay": dot1dStpForwardDelay,
       "dot1dStpBridgeMaxAge": dot1dStpBridgeMaxAge,
       "dot1dStpBridgeHelloTime": dot1dStpBridgeHelloTime,
       "dot1dStpBridgeForwardDelay": dot1dStpBridgeForwardDelay,
       "dot1dStpPortTable": dot1dStpPortTable,
       "dot1dStpPortEntry": dot1dStpPortEntry,
       "dot1dStpPort": dot1dStpPort,
       "dot1dStpPortPriority": dot1dStpPortPriority,
       "dot1dStpPortState": dot1dStpPortState,
       "dot1dStpPortEnable": dot1dStpPortEnable,
       "dot1dStpPortPathCost": dot1dStpPortPathCost,
       "dot1dStpPortDesignatedRoot": dot1dStpPortDesignatedRoot,
       "dot1dStpPortDesignatedCost": dot1dStpPortDesignatedCost,
       "dot1dStpPortDesignatedBridge": dot1dStpPortDesignatedBridge,
       "dot1dStpPortDesignatedPort": dot1dStpPortDesignatedPort,
       "dot1dStpPortForwardTransitions": dot1dStpPortForwardTransitions,
       "dot1dSr": dot1dSr,
       "dot1dSrPortTable": dot1dSrPortTable,
       "dot1dSrPortEntry": dot1dSrPortEntry,
       "dot1dSrPort": dot1dSrPort,
       "dot1dSrPortHopCount": dot1dSrPortHopCount,
       "dot1dSrPortLocalSegment": dot1dSrPortLocalSegment,
       "dot1dSrPortBridgeNum": dot1dSrPortBridgeNum,
       "dot1dSrPortTargetSegment": dot1dSrPortTargetSegment,
       "dot1dSrPortLargestFrame": dot1dSrPortLargestFrame,
       "dot1dSrPortSTESpanMode": dot1dSrPortSTESpanMode,
       "dot1dSrPortSpecInFrames": dot1dSrPortSpecInFrames,
       "dot1dSrPortSpecOutFrames": dot1dSrPortSpecOutFrames,
       "dot1dSrPortApeInFrames": dot1dSrPortApeInFrames,
       "dot1dSrPortApeOutFrames": dot1dSrPortApeOutFrames,
       "dot1dSrPortSteInFrames": dot1dSrPortSteInFrames,
       "dot1dSrPortSteOutFrames": dot1dSrPortSteOutFrames,
       "dot1dSrPortSegmentMismatchDiscards": dot1dSrPortSegmentMismatchDiscards,
       "dot1dSrPortDuplicateSegmentDiscards": dot1dSrPortDuplicateSegmentDiscards,
       "dot1dSrPortHopCountExceededDiscards": dot1dSrPortHopCountExceededDiscards,
       "dot1dTp": dot1dTp,
       "dot1dTpLearnedEntryDiscards": dot1dTpLearnedEntryDiscards,
       "dot1dTpAgingTime": dot1dTpAgingTime,
       "dot1dTpFdbTable": dot1dTpFdbTable,
       "dot1dTpFdbEntry": dot1dTpFdbEntry,
       "dot1dTpFdbAddress": dot1dTpFdbAddress,
       "dot1dTpFdbPort": dot1dTpFdbPort,
       "dot1dTpFdbStatus": dot1dTpFdbStatus,
       "dot1dTpPortTable": dot1dTpPortTable,
       "dot1dTpPortEntry": dot1dTpPortEntry,
       "dot1dTpPort": dot1dTpPort,
       "dot1dTpPortMaxInfo": dot1dTpPortMaxInfo,
       "dot1dTpPortInFrames": dot1dTpPortInFrames,
       "dot1dTpPortOutFrames": dot1dTpPortOutFrames,
       "dot1dTpPortInDiscards": dot1dTpPortInDiscards,
       "dot1dStatic": dot1dStatic,
       "dot1dStaticTable": dot1dStaticTable,
       "dot1dStaticEntry": dot1dStaticEntry,
       "dot1dStaticAddress": dot1dStaticAddress,
       "dot1dStaticReceivePort": dot1dStaticReceivePort,
       "dot1dStaticAllowedToGoTo": dot1dStaticAllowedToGoTo,
       "dot1dStaticStatus": dot1dStaticStatus}
)
