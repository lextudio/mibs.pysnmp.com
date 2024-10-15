# SNMP MIB module (AIBRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIBRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:07 2024
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

(aii,) = mibBuilder.importSymbols(
    "AIMIB",
    "aii")

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

_AiDot1dBridge_ObjectIdentity = ObjectIdentity
aiDot1dBridge = _AiDot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 30)
)
_AiDot1dBase_ObjectIdentity = ObjectIdentity
aiDot1dBase = _AiDot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 30, 1)
)
_AiDot1dBaseInfoTable_Object = MibTable
aiDot1dBaseInfoTable = _AiDot1dBaseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 1)
)
if mibBuilder.loadTexts:
    aiDot1dBaseInfoTable.setStatus("mandatory")
_AiDot1dBaseInfoEntry_Object = MibTableRow
aiDot1dBaseInfoEntry = _AiDot1dBaseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 1, 1)
)
aiDot1dBaseInfoEntry.setIndexNames(
    (0, "AIBRIDGE-MIB", "aiDot1dBaseInfoSTPIndex"),
)
if mibBuilder.loadTexts:
    aiDot1dBaseInfoEntry.setStatus("mandatory")


class _AiDot1dBaseInfoSTPIndex_Type(Integer32):
    """Custom type aiDot1dBaseInfoSTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiDot1dBaseInfoSTPIndex_Type.__name__ = "Integer32"
_AiDot1dBaseInfoSTPIndex_Object = MibTableColumn
aiDot1dBaseInfoSTPIndex = _AiDot1dBaseInfoSTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 1, 1, 1),
    _AiDot1dBaseInfoSTPIndex_Type()
)
aiDot1dBaseInfoSTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dBaseInfoSTPIndex.setStatus("mandatory")
_AiDot1dBaseBridgeAddress_Type = MacAddress
_AiDot1dBaseBridgeAddress_Object = MibTableColumn
aiDot1dBaseBridgeAddress = _AiDot1dBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 1, 1, 2),
    _AiDot1dBaseBridgeAddress_Type()
)
aiDot1dBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dBaseBridgeAddress.setStatus("mandatory")
_AiDot1dBaseNumPorts_Type = Integer32
_AiDot1dBaseNumPorts_Object = MibTableColumn
aiDot1dBaseNumPorts = _AiDot1dBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 1, 1, 3),
    _AiDot1dBaseNumPorts_Type()
)
aiDot1dBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dBaseNumPorts.setStatus("mandatory")


class _AiDot1dBaseType_Type(Integer32):
    """Custom type aiDot1dBaseType based on Integer32"""
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


_AiDot1dBaseType_Type.__name__ = "Integer32"
_AiDot1dBaseType_Object = MibTableColumn
aiDot1dBaseType = _AiDot1dBaseType_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 1, 1, 4),
    _AiDot1dBaseType_Type()
)
aiDot1dBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dBaseType.setStatus("mandatory")
_AiDot1dBasePortTable_Object = MibTable
aiDot1dBasePortTable = _AiDot1dBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 2)
)
if mibBuilder.loadTexts:
    aiDot1dBasePortTable.setStatus("mandatory")
_AiDot1dBasePortEntry_Object = MibTableRow
aiDot1dBasePortEntry = _AiDot1dBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 2, 1)
)
aiDot1dBasePortEntry.setIndexNames(
    (0, "AIBRIDGE-MIB", "aiDot1dBasePortStpIndex"),
    (0, "AIBRIDGE-MIB", "aiDot1dBasePort"),
)
if mibBuilder.loadTexts:
    aiDot1dBasePortEntry.setStatus("mandatory")


class _AiDot1dBasePortStpIndex_Type(Integer32):
    """Custom type aiDot1dBasePortStpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiDot1dBasePortStpIndex_Type.__name__ = "Integer32"
_AiDot1dBasePortStpIndex_Object = MibTableColumn
aiDot1dBasePortStpIndex = _AiDot1dBasePortStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 2, 1, 1),
    _AiDot1dBasePortStpIndex_Type()
)
aiDot1dBasePortStpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dBasePortStpIndex.setStatus("mandatory")


class _AiDot1dBasePort_Type(Integer32):
    """Custom type aiDot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiDot1dBasePort_Type.__name__ = "Integer32"
_AiDot1dBasePort_Object = MibTableColumn
aiDot1dBasePort = _AiDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 2, 1, 2),
    _AiDot1dBasePort_Type()
)
aiDot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dBasePort.setStatus("mandatory")
_AiDot1dBasePortIfIndex_Type = Integer32
_AiDot1dBasePortIfIndex_Object = MibTableColumn
aiDot1dBasePortIfIndex = _AiDot1dBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 2, 1, 3),
    _AiDot1dBasePortIfIndex_Type()
)
aiDot1dBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dBasePortIfIndex.setStatus("mandatory")
_AiDot1dBasePortCircuit_Type = ObjectIdentifier
_AiDot1dBasePortCircuit_Object = MibTableColumn
aiDot1dBasePortCircuit = _AiDot1dBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 2, 1, 4),
    _AiDot1dBasePortCircuit_Type()
)
aiDot1dBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dBasePortCircuit.setStatus("mandatory")
_AiDot1dBasePortDelayExceededDiscards_Type = Counter32
_AiDot1dBasePortDelayExceededDiscards_Object = MibTableColumn
aiDot1dBasePortDelayExceededDiscards = _AiDot1dBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 2, 1, 5),
    _AiDot1dBasePortDelayExceededDiscards_Type()
)
aiDot1dBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dBasePortDelayExceededDiscards.setStatus("mandatory")
_AiDot1dBasePortMtuExceededDiscards_Type = Counter32
_AiDot1dBasePortMtuExceededDiscards_Object = MibTableColumn
aiDot1dBasePortMtuExceededDiscards = _AiDot1dBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 1, 2, 1, 6),
    _AiDot1dBasePortMtuExceededDiscards_Type()
)
aiDot1dBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dBasePortMtuExceededDiscards.setStatus("mandatory")
_AiDot1dStp_ObjectIdentity = ObjectIdentity
aiDot1dStp = _AiDot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 30, 2)
)
_AiDot1dStpInfoTable_Object = MibTable
aiDot1dStpInfoTable = _AiDot1dStpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1)
)
if mibBuilder.loadTexts:
    aiDot1dStpInfoTable.setStatus("mandatory")
_AiDot1dStpInfoEntry_Object = MibTableRow
aiDot1dStpInfoEntry = _AiDot1dStpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1)
)
aiDot1dStpInfoEntry.setIndexNames(
    (0, "AIBRIDGE-MIB", "aiDot1dStpStpIndex"),
)
if mibBuilder.loadTexts:
    aiDot1dStpInfoEntry.setStatus("mandatory")


class _AiDot1dStpStpIndex_Type(Integer32):
    """Custom type aiDot1dStpStpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiDot1dStpStpIndex_Type.__name__ = "Integer32"
_AiDot1dStpStpIndex_Object = MibTableColumn
aiDot1dStpStpIndex = _AiDot1dStpStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 1),
    _AiDot1dStpStpIndex_Type()
)
aiDot1dStpStpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpStpIndex.setStatus("mandatory")


class _AiDot1dStpProtocolSpecification_Type(Integer32):
    """Custom type aiDot1dStpProtocolSpecification based on Integer32"""
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


_AiDot1dStpProtocolSpecification_Type.__name__ = "Integer32"
_AiDot1dStpProtocolSpecification_Object = MibTableColumn
aiDot1dStpProtocolSpecification = _AiDot1dStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 2),
    _AiDot1dStpProtocolSpecification_Type()
)
aiDot1dStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpProtocolSpecification.setStatus("mandatory")


class _AiDot1dStpPriority_Type(Integer32):
    """Custom type aiDot1dStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AiDot1dStpPriority_Type.__name__ = "Integer32"
_AiDot1dStpPriority_Object = MibTableColumn
aiDot1dStpPriority = _AiDot1dStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 3),
    _AiDot1dStpPriority_Type()
)
aiDot1dStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDot1dStpPriority.setStatus("mandatory")
_AiDot1dStpTimeSinceTopologyChange_Type = TimeTicks
_AiDot1dStpTimeSinceTopologyChange_Object = MibTableColumn
aiDot1dStpTimeSinceTopologyChange = _AiDot1dStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 4),
    _AiDot1dStpTimeSinceTopologyChange_Type()
)
aiDot1dStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpTimeSinceTopologyChange.setStatus("mandatory")
_AiDot1dStpTopChanges_Type = Counter32
_AiDot1dStpTopChanges_Object = MibTableColumn
aiDot1dStpTopChanges = _AiDot1dStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 5),
    _AiDot1dStpTopChanges_Type()
)
aiDot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpTopChanges.setStatus("mandatory")
_AiDot1dStpDesignatedRoot_Type = BridgeId
_AiDot1dStpDesignatedRoot_Object = MibTableColumn
aiDot1dStpDesignatedRoot = _AiDot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 6),
    _AiDot1dStpDesignatedRoot_Type()
)
aiDot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpDesignatedRoot.setStatus("mandatory")
_AiDot1dStpRootCost_Type = Integer32
_AiDot1dStpRootCost_Object = MibTableColumn
aiDot1dStpRootCost = _AiDot1dStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 7),
    _AiDot1dStpRootCost_Type()
)
aiDot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpRootCost.setStatus("mandatory")
_AiDot1dStpRootPort_Type = Integer32
_AiDot1dStpRootPort_Object = MibTableColumn
aiDot1dStpRootPort = _AiDot1dStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 8),
    _AiDot1dStpRootPort_Type()
)
aiDot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpRootPort.setStatus("mandatory")
_AiDot1dStpMaxAge_Type = Timeout
_AiDot1dStpMaxAge_Object = MibTableColumn
aiDot1dStpMaxAge = _AiDot1dStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 9),
    _AiDot1dStpMaxAge_Type()
)
aiDot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpMaxAge.setStatus("mandatory")
_AiDot1dStpHelloTime_Type = Timeout
_AiDot1dStpHelloTime_Object = MibTableColumn
aiDot1dStpHelloTime = _AiDot1dStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 10),
    _AiDot1dStpHelloTime_Type()
)
aiDot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpHelloTime.setStatus("mandatory")
_AiDot1dStpHoldTime_Type = Integer32
_AiDot1dStpHoldTime_Object = MibTableColumn
aiDot1dStpHoldTime = _AiDot1dStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 11),
    _AiDot1dStpHoldTime_Type()
)
aiDot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpHoldTime.setStatus("mandatory")
_AiDot1dStpForwardDelay_Type = Timeout
_AiDot1dStpForwardDelay_Object = MibTableColumn
aiDot1dStpForwardDelay = _AiDot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 12),
    _AiDot1dStpForwardDelay_Type()
)
aiDot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpForwardDelay.setStatus("mandatory")


class _AiDot1dStpBridgeMaxAge_Type(Timeout):
    """Custom type aiDot1dStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_AiDot1dStpBridgeMaxAge_Type.__name__ = "Timeout"
_AiDot1dStpBridgeMaxAge_Object = MibTableColumn
aiDot1dStpBridgeMaxAge = _AiDot1dStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 13),
    _AiDot1dStpBridgeMaxAge_Type()
)
aiDot1dStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDot1dStpBridgeMaxAge.setStatus("mandatory")


class _AiDot1dStpBridgeHelloTime_Type(Timeout):
    """Custom type aiDot1dStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_AiDot1dStpBridgeHelloTime_Type.__name__ = "Timeout"
_AiDot1dStpBridgeHelloTime_Object = MibTableColumn
aiDot1dStpBridgeHelloTime = _AiDot1dStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 14),
    _AiDot1dStpBridgeHelloTime_Type()
)
aiDot1dStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDot1dStpBridgeHelloTime.setStatus("mandatory")


class _AiDot1dStpBridgeForwardDelay_Type(Timeout):
    """Custom type aiDot1dStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_AiDot1dStpBridgeForwardDelay_Type.__name__ = "Timeout"
_AiDot1dStpBridgeForwardDelay_Object = MibTableColumn
aiDot1dStpBridgeForwardDelay = _AiDot1dStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 15),
    _AiDot1dStpBridgeForwardDelay_Type()
)
aiDot1dStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDot1dStpBridgeForwardDelay.setStatus("mandatory")


class _AiDot1dStpEnabled_Type(Integer32):
    """Custom type aiDot1dStpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stpDisabled", 2),
          ("stpEnabled", 1))
    )


_AiDot1dStpEnabled_Type.__name__ = "Integer32"
_AiDot1dStpEnabled_Object = MibTableColumn
aiDot1dStpEnabled = _AiDot1dStpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 1, 1, 16),
    _AiDot1dStpEnabled_Type()
)
aiDot1dStpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDot1dStpEnabled.setStatus("mandatory")
_AiDot1dStpPortTable_Object = MibTable
aiDot1dStpPortTable = _AiDot1dStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15)
)
if mibBuilder.loadTexts:
    aiDot1dStpPortTable.setStatus("mandatory")
_AiDot1dStpPortEntry_Object = MibTableRow
aiDot1dStpPortEntry = _AiDot1dStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1)
)
aiDot1dStpPortEntry.setIndexNames(
    (0, "AIBRIDGE-MIB", "aiDot1dStpPortStpIndex"),
    (0, "AIBRIDGE-MIB", "aiDot1dStpPort"),
)
if mibBuilder.loadTexts:
    aiDot1dStpPortEntry.setStatus("mandatory")


class _AiDot1dStpPortStpIndex_Type(Integer32):
    """Custom type aiDot1dStpPortStpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiDot1dStpPortStpIndex_Type.__name__ = "Integer32"
_AiDot1dStpPortStpIndex_Object = MibTableColumn
aiDot1dStpPortStpIndex = _AiDot1dStpPortStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1, 1),
    _AiDot1dStpPortStpIndex_Type()
)
aiDot1dStpPortStpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpPortStpIndex.setStatus("mandatory")


class _AiDot1dStpPort_Type(Integer32):
    """Custom type aiDot1dStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiDot1dStpPort_Type.__name__ = "Integer32"
_AiDot1dStpPort_Object = MibTableColumn
aiDot1dStpPort = _AiDot1dStpPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1, 2),
    _AiDot1dStpPort_Type()
)
aiDot1dStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpPort.setStatus("mandatory")


class _AiDot1dStpPortPriority_Type(Integer32):
    """Custom type aiDot1dStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiDot1dStpPortPriority_Type.__name__ = "Integer32"
_AiDot1dStpPortPriority_Object = MibTableColumn
aiDot1dStpPortPriority = _AiDot1dStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1, 3),
    _AiDot1dStpPortPriority_Type()
)
aiDot1dStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDot1dStpPortPriority.setStatus("mandatory")


class _AiDot1dStpPortState_Type(Integer32):
    """Custom type aiDot1dStpPortState based on Integer32"""
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


_AiDot1dStpPortState_Type.__name__ = "Integer32"
_AiDot1dStpPortState_Object = MibTableColumn
aiDot1dStpPortState = _AiDot1dStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1, 4),
    _AiDot1dStpPortState_Type()
)
aiDot1dStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpPortState.setStatus("mandatory")


class _AiDot1dStpPortEnable_Type(Integer32):
    """Custom type aiDot1dStpPortEnable based on Integer32"""
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


_AiDot1dStpPortEnable_Type.__name__ = "Integer32"
_AiDot1dStpPortEnable_Object = MibTableColumn
aiDot1dStpPortEnable = _AiDot1dStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1, 5),
    _AiDot1dStpPortEnable_Type()
)
aiDot1dStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDot1dStpPortEnable.setStatus("mandatory")


class _AiDot1dStpPortPathCost_Type(Integer32):
    """Custom type aiDot1dStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AiDot1dStpPortPathCost_Type.__name__ = "Integer32"
_AiDot1dStpPortPathCost_Object = MibTableColumn
aiDot1dStpPortPathCost = _AiDot1dStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1, 6),
    _AiDot1dStpPortPathCost_Type()
)
aiDot1dStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiDot1dStpPortPathCost.setStatus("mandatory")
_AiDot1dStpPortDesignatedRoot_Type = BridgeId
_AiDot1dStpPortDesignatedRoot_Object = MibTableColumn
aiDot1dStpPortDesignatedRoot = _AiDot1dStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1, 7),
    _AiDot1dStpPortDesignatedRoot_Type()
)
aiDot1dStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpPortDesignatedRoot.setStatus("mandatory")
_AiDot1dStpPortDesignatedCost_Type = Integer32
_AiDot1dStpPortDesignatedCost_Object = MibTableColumn
aiDot1dStpPortDesignatedCost = _AiDot1dStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1, 8),
    _AiDot1dStpPortDesignatedCost_Type()
)
aiDot1dStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpPortDesignatedCost.setStatus("mandatory")
_AiDot1dStpPortDesignatedBridge_Type = BridgeId
_AiDot1dStpPortDesignatedBridge_Object = MibTableColumn
aiDot1dStpPortDesignatedBridge = _AiDot1dStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1, 9),
    _AiDot1dStpPortDesignatedBridge_Type()
)
aiDot1dStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpPortDesignatedBridge.setStatus("mandatory")


class _AiDot1dStpPortDesignatedPort_Type(OctetString):
    """Custom type aiDot1dStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AiDot1dStpPortDesignatedPort_Type.__name__ = "OctetString"
_AiDot1dStpPortDesignatedPort_Object = MibTableColumn
aiDot1dStpPortDesignatedPort = _AiDot1dStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1, 10),
    _AiDot1dStpPortDesignatedPort_Type()
)
aiDot1dStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpPortDesignatedPort.setStatus("mandatory")
_AiDot1dStpPortForwardTransitions_Type = Counter32
_AiDot1dStpPortForwardTransitions_Object = MibTableColumn
aiDot1dStpPortForwardTransitions = _AiDot1dStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 539, 30, 2, 15, 1, 11),
    _AiDot1dStpPortForwardTransitions_Type()
)
aiDot1dStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiDot1dStpPortForwardTransitions.setStatus("mandatory")
_AiDot1dSr_ObjectIdentity = ObjectIdentity
aiDot1dSr = _AiDot1dSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 30, 3)
)
_AiDot1dTp_ObjectIdentity = ObjectIdentity
aiDot1dTp = _AiDot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 30, 4)
)
_AiDot1dStatic_ObjectIdentity = ObjectIdentity
aiDot1dStatic = _AiDot1dStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 30, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIBRIDGE-MIB",
    **{"MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "aiDot1dBridge": aiDot1dBridge,
       "aiDot1dBase": aiDot1dBase,
       "aiDot1dBaseInfoTable": aiDot1dBaseInfoTable,
       "aiDot1dBaseInfoEntry": aiDot1dBaseInfoEntry,
       "aiDot1dBaseInfoSTPIndex": aiDot1dBaseInfoSTPIndex,
       "aiDot1dBaseBridgeAddress": aiDot1dBaseBridgeAddress,
       "aiDot1dBaseNumPorts": aiDot1dBaseNumPorts,
       "aiDot1dBaseType": aiDot1dBaseType,
       "aiDot1dBasePortTable": aiDot1dBasePortTable,
       "aiDot1dBasePortEntry": aiDot1dBasePortEntry,
       "aiDot1dBasePortStpIndex": aiDot1dBasePortStpIndex,
       "aiDot1dBasePort": aiDot1dBasePort,
       "aiDot1dBasePortIfIndex": aiDot1dBasePortIfIndex,
       "aiDot1dBasePortCircuit": aiDot1dBasePortCircuit,
       "aiDot1dBasePortDelayExceededDiscards": aiDot1dBasePortDelayExceededDiscards,
       "aiDot1dBasePortMtuExceededDiscards": aiDot1dBasePortMtuExceededDiscards,
       "aiDot1dStp": aiDot1dStp,
       "aiDot1dStpInfoTable": aiDot1dStpInfoTable,
       "aiDot1dStpInfoEntry": aiDot1dStpInfoEntry,
       "aiDot1dStpStpIndex": aiDot1dStpStpIndex,
       "aiDot1dStpProtocolSpecification": aiDot1dStpProtocolSpecification,
       "aiDot1dStpPriority": aiDot1dStpPriority,
       "aiDot1dStpTimeSinceTopologyChange": aiDot1dStpTimeSinceTopologyChange,
       "aiDot1dStpTopChanges": aiDot1dStpTopChanges,
       "aiDot1dStpDesignatedRoot": aiDot1dStpDesignatedRoot,
       "aiDot1dStpRootCost": aiDot1dStpRootCost,
       "aiDot1dStpRootPort": aiDot1dStpRootPort,
       "aiDot1dStpMaxAge": aiDot1dStpMaxAge,
       "aiDot1dStpHelloTime": aiDot1dStpHelloTime,
       "aiDot1dStpHoldTime": aiDot1dStpHoldTime,
       "aiDot1dStpForwardDelay": aiDot1dStpForwardDelay,
       "aiDot1dStpBridgeMaxAge": aiDot1dStpBridgeMaxAge,
       "aiDot1dStpBridgeHelloTime": aiDot1dStpBridgeHelloTime,
       "aiDot1dStpBridgeForwardDelay": aiDot1dStpBridgeForwardDelay,
       "aiDot1dStpEnabled": aiDot1dStpEnabled,
       "aiDot1dStpPortTable": aiDot1dStpPortTable,
       "aiDot1dStpPortEntry": aiDot1dStpPortEntry,
       "aiDot1dStpPortStpIndex": aiDot1dStpPortStpIndex,
       "aiDot1dStpPort": aiDot1dStpPort,
       "aiDot1dStpPortPriority": aiDot1dStpPortPriority,
       "aiDot1dStpPortState": aiDot1dStpPortState,
       "aiDot1dStpPortEnable": aiDot1dStpPortEnable,
       "aiDot1dStpPortPathCost": aiDot1dStpPortPathCost,
       "aiDot1dStpPortDesignatedRoot": aiDot1dStpPortDesignatedRoot,
       "aiDot1dStpPortDesignatedCost": aiDot1dStpPortDesignatedCost,
       "aiDot1dStpPortDesignatedBridge": aiDot1dStpPortDesignatedBridge,
       "aiDot1dStpPortDesignatedPort": aiDot1dStpPortDesignatedPort,
       "aiDot1dStpPortForwardTransitions": aiDot1dStpPortForwardTransitions,
       "aiDot1dSr": aiDot1dSr,
       "aiDot1dTp": aiDot1dTp,
       "aiDot1dStatic": aiDot1dStatic}
)
