# SNMP MIB module (CENTILLION-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:59 2024
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

(EnableIndicator,
 extensions) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "EnableIndicator",
    "extensions")

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

_Cndot1dBridge_ObjectIdentity = ObjectIdentity
cndot1dBridge = _Cndot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 17)
)
_Cndot1dBase_ObjectIdentity = ObjectIdentity
cndot1dBase = _Cndot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 1)
)
_Cndot1dBaseBridgeAddress_Type = MacAddress
_Cndot1dBaseBridgeAddress_Object = MibScalar
cndot1dBaseBridgeAddress = _Cndot1dBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 1, 1),
    _Cndot1dBaseBridgeAddress_Type()
)
cndot1dBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dBaseBridgeAddress.setStatus("mandatory")
_Cndot1dBaseNumPorts_Type = Integer32
_Cndot1dBaseNumPorts_Object = MibScalar
cndot1dBaseNumPorts = _Cndot1dBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 1, 2),
    _Cndot1dBaseNumPorts_Type()
)
cndot1dBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dBaseNumPorts.setStatus("mandatory")


class _Cndot1dBaseType_Type(Integer32):
    """Custom type cndot1dBaseType based on Integer32"""
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


_Cndot1dBaseType_Type.__name__ = "Integer32"
_Cndot1dBaseType_Object = MibScalar
cndot1dBaseType = _Cndot1dBaseType_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 1, 3),
    _Cndot1dBaseType_Type()
)
cndot1dBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dBaseType.setStatus("mandatory")
_Cndot1dBasePortTable_Object = MibTable
cndot1dBasePortTable = _Cndot1dBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 1, 4)
)
if mibBuilder.loadTexts:
    cndot1dBasePortTable.setStatus("mandatory")
_Cndot1dBasePortEntry_Object = MibTableRow
cndot1dBasePortEntry = _Cndot1dBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 1, 4, 1)
)
cndot1dBasePortEntry.setIndexNames(
    (0, "CENTILLION-BRIDGE-MIB", "cndot1dBasePort"),
)
if mibBuilder.loadTexts:
    cndot1dBasePortEntry.setStatus("mandatory")
_Cndot1dBasePort_Type = Integer32
_Cndot1dBasePort_Object = MibTableColumn
cndot1dBasePort = _Cndot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 1, 4, 1, 1),
    _Cndot1dBasePort_Type()
)
cndot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dBasePort.setStatus("mandatory")
_Cndot1dBasePortIfIndex_Type = Integer32
_Cndot1dBasePortIfIndex_Object = MibTableColumn
cndot1dBasePortIfIndex = _Cndot1dBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 1, 4, 1, 2),
    _Cndot1dBasePortIfIndex_Type()
)
cndot1dBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dBasePortIfIndex.setStatus("mandatory")
_Cndot1dBasePortCircuit_Type = ObjectIdentifier
_Cndot1dBasePortCircuit_Object = MibTableColumn
cndot1dBasePortCircuit = _Cndot1dBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 1, 4, 1, 3),
    _Cndot1dBasePortCircuit_Type()
)
cndot1dBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dBasePortCircuit.setStatus("mandatory")
_Cndot1dStp_ObjectIdentity = ObjectIdentity
cndot1dStp = _Cndot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2)
)


class _Cndot1dStpProtocolSpecification_Type(Integer32):
    """Custom type cndot1dStpProtocolSpecification based on Integer32"""
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


_Cndot1dStpProtocolSpecification_Type.__name__ = "Integer32"
_Cndot1dStpProtocolSpecification_Object = MibScalar
cndot1dStpProtocolSpecification = _Cndot1dStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 1),
    _Cndot1dStpProtocolSpecification_Type()
)
cndot1dStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpProtocolSpecification.setStatus("mandatory")


class _Cndot1dStpPriority_Type(Integer32):
    """Custom type cndot1dStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cndot1dStpPriority_Type.__name__ = "Integer32"
_Cndot1dStpPriority_Object = MibScalar
cndot1dStpPriority = _Cndot1dStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 2),
    _Cndot1dStpPriority_Type()
)
cndot1dStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dStpPriority.setStatus("mandatory")
_Cndot1dStpTimeSinceTopologyChange_Type = TimeTicks
_Cndot1dStpTimeSinceTopologyChange_Object = MibScalar
cndot1dStpTimeSinceTopologyChange = _Cndot1dStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 3),
    _Cndot1dStpTimeSinceTopologyChange_Type()
)
cndot1dStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpTimeSinceTopologyChange.setStatus("mandatory")
_Cndot1dStpTopChanges_Type = Counter32
_Cndot1dStpTopChanges_Object = MibScalar
cndot1dStpTopChanges = _Cndot1dStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 4),
    _Cndot1dStpTopChanges_Type()
)
cndot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpTopChanges.setStatus("mandatory")
_Cndot1dStpDesignatedRoot_Type = BridgeId
_Cndot1dStpDesignatedRoot_Object = MibScalar
cndot1dStpDesignatedRoot = _Cndot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 5),
    _Cndot1dStpDesignatedRoot_Type()
)
cndot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpDesignatedRoot.setStatus("mandatory")
_Cndot1dStpRootCost_Type = Integer32
_Cndot1dStpRootCost_Object = MibScalar
cndot1dStpRootCost = _Cndot1dStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 6),
    _Cndot1dStpRootCost_Type()
)
cndot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpRootCost.setStatus("mandatory")
_Cndot1dStpRootPort_Type = Integer32
_Cndot1dStpRootPort_Object = MibScalar
cndot1dStpRootPort = _Cndot1dStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 7),
    _Cndot1dStpRootPort_Type()
)
cndot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpRootPort.setStatus("mandatory")
_Cndot1dStpMaxAge_Type = Timeout
_Cndot1dStpMaxAge_Object = MibScalar
cndot1dStpMaxAge = _Cndot1dStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 8),
    _Cndot1dStpMaxAge_Type()
)
cndot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpMaxAge.setStatus("mandatory")
_Cndot1dStpHelloTime_Type = Timeout
_Cndot1dStpHelloTime_Object = MibScalar
cndot1dStpHelloTime = _Cndot1dStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 9),
    _Cndot1dStpHelloTime_Type()
)
cndot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpHelloTime.setStatus("mandatory")
_Cndot1dStpHoldTime_Type = Integer32
_Cndot1dStpHoldTime_Object = MibScalar
cndot1dStpHoldTime = _Cndot1dStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 10),
    _Cndot1dStpHoldTime_Type()
)
cndot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpHoldTime.setStatus("mandatory")
_Cndot1dStpForwardDelay_Type = Timeout
_Cndot1dStpForwardDelay_Object = MibScalar
cndot1dStpForwardDelay = _Cndot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 11),
    _Cndot1dStpForwardDelay_Type()
)
cndot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpForwardDelay.setStatus("mandatory")


class _Cndot1dStpBridgeMaxAge_Type(Timeout):
    """Custom type cndot1dStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_Cndot1dStpBridgeMaxAge_Type.__name__ = "Timeout"
_Cndot1dStpBridgeMaxAge_Object = MibScalar
cndot1dStpBridgeMaxAge = _Cndot1dStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 12),
    _Cndot1dStpBridgeMaxAge_Type()
)
cndot1dStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dStpBridgeMaxAge.setStatus("mandatory")


class _Cndot1dStpBridgeHelloTime_Type(Timeout):
    """Custom type cndot1dStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_Cndot1dStpBridgeHelloTime_Type.__name__ = "Timeout"
_Cndot1dStpBridgeHelloTime_Object = MibScalar
cndot1dStpBridgeHelloTime = _Cndot1dStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 13),
    _Cndot1dStpBridgeHelloTime_Type()
)
cndot1dStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dStpBridgeHelloTime.setStatus("mandatory")


class _Cndot1dStpBridgeForwardDelay_Type(Timeout):
    """Custom type cndot1dStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_Cndot1dStpBridgeForwardDelay_Type.__name__ = "Timeout"
_Cndot1dStpBridgeForwardDelay_Object = MibScalar
cndot1dStpBridgeForwardDelay = _Cndot1dStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 14),
    _Cndot1dStpBridgeForwardDelay_Type()
)
cndot1dStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dStpBridgeForwardDelay.setStatus("mandatory")
_Cndot1dStpPortTable_Object = MibTable
cndot1dStpPortTable = _Cndot1dStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15)
)
if mibBuilder.loadTexts:
    cndot1dStpPortTable.setStatus("mandatory")
_Cndot1dStpPortEntry_Object = MibTableRow
cndot1dStpPortEntry = _Cndot1dStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15, 1)
)
cndot1dStpPortEntry.setIndexNames(
    (0, "CENTILLION-BRIDGE-MIB", "cndot1dStpPort"),
)
if mibBuilder.loadTexts:
    cndot1dStpPortEntry.setStatus("mandatory")


class _Cndot1dStpPort_Type(Integer32):
    """Custom type cndot1dStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cndot1dStpPort_Type.__name__ = "Integer32"
_Cndot1dStpPort_Object = MibTableColumn
cndot1dStpPort = _Cndot1dStpPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15, 1, 1),
    _Cndot1dStpPort_Type()
)
cndot1dStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpPort.setStatus("mandatory")


class _Cndot1dStpPortPriority_Type(Integer32):
    """Custom type cndot1dStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cndot1dStpPortPriority_Type.__name__ = "Integer32"
_Cndot1dStpPortPriority_Object = MibTableColumn
cndot1dStpPortPriority = _Cndot1dStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15, 1, 2),
    _Cndot1dStpPortPriority_Type()
)
cndot1dStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dStpPortPriority.setStatus("mandatory")


class _Cndot1dStpPortState_Type(Integer32):
    """Custom type cndot1dStpPortState based on Integer32"""
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


_Cndot1dStpPortState_Type.__name__ = "Integer32"
_Cndot1dStpPortState_Object = MibTableColumn
cndot1dStpPortState = _Cndot1dStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15, 1, 3),
    _Cndot1dStpPortState_Type()
)
cndot1dStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpPortState.setStatus("mandatory")


class _Cndot1dStpPortEnable_Type(Integer32):
    """Custom type cndot1dStpPortEnable based on Integer32"""
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


_Cndot1dStpPortEnable_Type.__name__ = "Integer32"
_Cndot1dStpPortEnable_Object = MibTableColumn
cndot1dStpPortEnable = _Cndot1dStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15, 1, 4),
    _Cndot1dStpPortEnable_Type()
)
cndot1dStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dStpPortEnable.setStatus("mandatory")


class _Cndot1dStpPortPathCost_Type(Integer32):
    """Custom type cndot1dStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cndot1dStpPortPathCost_Type.__name__ = "Integer32"
_Cndot1dStpPortPathCost_Object = MibTableColumn
cndot1dStpPortPathCost = _Cndot1dStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15, 1, 5),
    _Cndot1dStpPortPathCost_Type()
)
cndot1dStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dStpPortPathCost.setStatus("mandatory")
_Cndot1dStpPortDesignatedRoot_Type = BridgeId
_Cndot1dStpPortDesignatedRoot_Object = MibTableColumn
cndot1dStpPortDesignatedRoot = _Cndot1dStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15, 1, 6),
    _Cndot1dStpPortDesignatedRoot_Type()
)
cndot1dStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpPortDesignatedRoot.setStatus("mandatory")
_Cndot1dStpPortDesignatedCost_Type = Integer32
_Cndot1dStpPortDesignatedCost_Object = MibTableColumn
cndot1dStpPortDesignatedCost = _Cndot1dStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15, 1, 7),
    _Cndot1dStpPortDesignatedCost_Type()
)
cndot1dStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpPortDesignatedCost.setStatus("mandatory")
_Cndot1dStpPortDesignatedBridge_Type = BridgeId
_Cndot1dStpPortDesignatedBridge_Object = MibTableColumn
cndot1dStpPortDesignatedBridge = _Cndot1dStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15, 1, 8),
    _Cndot1dStpPortDesignatedBridge_Type()
)
cndot1dStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpPortDesignatedBridge.setStatus("mandatory")


class _Cndot1dStpPortDesignatedPort_Type(OctetString):
    """Custom type cndot1dStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Cndot1dStpPortDesignatedPort_Type.__name__ = "OctetString"
_Cndot1dStpPortDesignatedPort_Object = MibTableColumn
cndot1dStpPortDesignatedPort = _Cndot1dStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15, 1, 9),
    _Cndot1dStpPortDesignatedPort_Type()
)
cndot1dStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpPortDesignatedPort.setStatus("mandatory")
_Cndot1dStpPortForwardTransitions_Type = Counter32
_Cndot1dStpPortForwardTransitions_Object = MibTableColumn
cndot1dStpPortForwardTransitions = _Cndot1dStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 2, 15, 1, 10),
    _Cndot1dStpPortForwardTransitions_Type()
)
cndot1dStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cndot1dStpPortForwardTransitions.setStatus("mandatory")
_Cndot1dSr_ObjectIdentity = ObjectIdentity
cndot1dSr = _Cndot1dSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 3)
)
_Cndot1dTp_ObjectIdentity = ObjectIdentity
cndot1dTp = _Cndot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 4)
)
_Cndot1dTpSrFrameForward_Type = EnableIndicator
_Cndot1dTpSrFrameForward_Object = MibScalar
cndot1dTpSrFrameForward = _Cndot1dTpSrFrameForward_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 17, 4, 5),
    _Cndot1dTpSrFrameForward_Type()
)
cndot1dTpSrFrameForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cndot1dTpSrFrameForward.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-BRIDGE-MIB",
    **{"MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "cndot1dBridge": cndot1dBridge,
       "cndot1dBase": cndot1dBase,
       "cndot1dBaseBridgeAddress": cndot1dBaseBridgeAddress,
       "cndot1dBaseNumPorts": cndot1dBaseNumPorts,
       "cndot1dBaseType": cndot1dBaseType,
       "cndot1dBasePortTable": cndot1dBasePortTable,
       "cndot1dBasePortEntry": cndot1dBasePortEntry,
       "cndot1dBasePort": cndot1dBasePort,
       "cndot1dBasePortIfIndex": cndot1dBasePortIfIndex,
       "cndot1dBasePortCircuit": cndot1dBasePortCircuit,
       "cndot1dStp": cndot1dStp,
       "cndot1dStpProtocolSpecification": cndot1dStpProtocolSpecification,
       "cndot1dStpPriority": cndot1dStpPriority,
       "cndot1dStpTimeSinceTopologyChange": cndot1dStpTimeSinceTopologyChange,
       "cndot1dStpTopChanges": cndot1dStpTopChanges,
       "cndot1dStpDesignatedRoot": cndot1dStpDesignatedRoot,
       "cndot1dStpRootCost": cndot1dStpRootCost,
       "cndot1dStpRootPort": cndot1dStpRootPort,
       "cndot1dStpMaxAge": cndot1dStpMaxAge,
       "cndot1dStpHelloTime": cndot1dStpHelloTime,
       "cndot1dStpHoldTime": cndot1dStpHoldTime,
       "cndot1dStpForwardDelay": cndot1dStpForwardDelay,
       "cndot1dStpBridgeMaxAge": cndot1dStpBridgeMaxAge,
       "cndot1dStpBridgeHelloTime": cndot1dStpBridgeHelloTime,
       "cndot1dStpBridgeForwardDelay": cndot1dStpBridgeForwardDelay,
       "cndot1dStpPortTable": cndot1dStpPortTable,
       "cndot1dStpPortEntry": cndot1dStpPortEntry,
       "cndot1dStpPort": cndot1dStpPort,
       "cndot1dStpPortPriority": cndot1dStpPortPriority,
       "cndot1dStpPortState": cndot1dStpPortState,
       "cndot1dStpPortEnable": cndot1dStpPortEnable,
       "cndot1dStpPortPathCost": cndot1dStpPortPathCost,
       "cndot1dStpPortDesignatedRoot": cndot1dStpPortDesignatedRoot,
       "cndot1dStpPortDesignatedCost": cndot1dStpPortDesignatedCost,
       "cndot1dStpPortDesignatedBridge": cndot1dStpPortDesignatedBridge,
       "cndot1dStpPortDesignatedPort": cndot1dStpPortDesignatedPort,
       "cndot1dStpPortForwardTransitions": cndot1dStpPortForwardTransitions,
       "cndot1dSr": cndot1dSr,
       "cndot1dTp": cndot1dTp,
       "cndot1dTpSrFrameForward": cndot1dTpSrFrameForward}
)
