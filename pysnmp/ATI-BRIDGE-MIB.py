# SNMP MIB module (ATI-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATI-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:44 2024
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_AlliedTelesyn_ObjectIdentity = ObjectIdentity
alliedTelesyn = _AlliedTelesyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)
_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_SwitchMib_ObjectIdentity = ObjectIdentity
switchMib = _SwitchMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 5)
)
_AtiBridgeMib_ObjectIdentity = ObjectIdentity
atiBridgeMib = _AtiBridgeMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10)
)
_AtbrBase_ObjectIdentity = ObjectIdentity
atbrBase = _AtbrBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1)
)
_AtbrBaseTable_Object = MibTable
atbrBaseTable = _AtbrBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1)
)
if mibBuilder.loadTexts:
    atbrBaseTable.setStatus("mandatory")
_AtbrBaseEntry_Object = MibTableRow
atbrBaseEntry = _AtbrBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1, 1)
)
atbrBaseEntry.setIndexNames(
    (0, "ATI-BRIDGE-MIB", "atbrBaseLanId"),
)
if mibBuilder.loadTexts:
    atbrBaseEntry.setStatus("mandatory")
_AtbrBaseLanId_Type = Integer32
_AtbrBaseLanId_Object = MibTableColumn
atbrBaseLanId = _AtbrBaseLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1, 1, 1),
    _AtbrBaseLanId_Type()
)
atbrBaseLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrBaseLanId.setStatus("mandatory")
_AtbrBaseBridgeAddress_Type = MacAddress
_AtbrBaseBridgeAddress_Object = MibTableColumn
atbrBaseBridgeAddress = _AtbrBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1, 1, 2),
    _AtbrBaseBridgeAddress_Type()
)
atbrBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrBaseBridgeAddress.setStatus("mandatory")
_AtbrBaseNumPorts_Type = Integer32
_AtbrBaseNumPorts_Object = MibTableColumn
atbrBaseNumPorts = _AtbrBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1, 1, 3),
    _AtbrBaseNumPorts_Type()
)
atbrBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrBaseNumPorts.setStatus("mandatory")


class _AtbrBaseType_Type(Integer32):
    """Custom type atbrBaseType based on Integer32"""
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


_AtbrBaseType_Type.__name__ = "Integer32"
_AtbrBaseType_Object = MibTableColumn
atbrBaseType = _AtbrBaseType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 1, 1, 4),
    _AtbrBaseType_Type()
)
atbrBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrBaseType.setStatus("mandatory")
_AtbrBasePortTable_Object = MibTable
atbrBasePortTable = _AtbrBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4)
)
if mibBuilder.loadTexts:
    atbrBasePortTable.setStatus("mandatory")
_AtbrBasePortEntry_Object = MibTableRow
atbrBasePortEntry = _AtbrBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1)
)
atbrBasePortEntry.setIndexNames(
    (0, "ATI-BRIDGE-MIB", "atbrBasePortLanId"),
    (0, "ATI-BRIDGE-MIB", "atbrBasePort"),
)
if mibBuilder.loadTexts:
    atbrBasePortEntry.setStatus("mandatory")
_AtbrBasePortLanId_Type = Integer32
_AtbrBasePortLanId_Object = MibTableColumn
atbrBasePortLanId = _AtbrBasePortLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 1),
    _AtbrBasePortLanId_Type()
)
atbrBasePortLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrBasePortLanId.setStatus("mandatory")


class _AtbrBasePort_Type(Integer32):
    """Custom type atbrBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtbrBasePort_Type.__name__ = "Integer32"
_AtbrBasePort_Object = MibTableColumn
atbrBasePort = _AtbrBasePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 2),
    _AtbrBasePort_Type()
)
atbrBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrBasePort.setStatus("mandatory")
_AtbrBasePortIfIndex_Type = Integer32
_AtbrBasePortIfIndex_Object = MibTableColumn
atbrBasePortIfIndex = _AtbrBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 3),
    _AtbrBasePortIfIndex_Type()
)
atbrBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrBasePortIfIndex.setStatus("mandatory")
_AtbrBasePortCircuit_Type = ObjectIdentifier
_AtbrBasePortCircuit_Object = MibTableColumn
atbrBasePortCircuit = _AtbrBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 4),
    _AtbrBasePortCircuit_Type()
)
atbrBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrBasePortCircuit.setStatus("mandatory")
_AtbrBasePortDelayExceededDiscards_Type = Counter32
_AtbrBasePortDelayExceededDiscards_Object = MibTableColumn
atbrBasePortDelayExceededDiscards = _AtbrBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 5),
    _AtbrBasePortDelayExceededDiscards_Type()
)
atbrBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrBasePortDelayExceededDiscards.setStatus("mandatory")
_AtbrBasePortMtuExceededDiscards_Type = Counter32
_AtbrBasePortMtuExceededDiscards_Object = MibTableColumn
atbrBasePortMtuExceededDiscards = _AtbrBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 1, 4, 1, 6),
    _AtbrBasePortMtuExceededDiscards_Type()
)
atbrBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrBasePortMtuExceededDiscards.setStatus("mandatory")
_AtbrStp_ObjectIdentity = ObjectIdentity
atbrStp = _AtbrStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2)
)
_AtbrStpTable_Object = MibTable
atbrStpTable = _AtbrStpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1)
)
if mibBuilder.loadTexts:
    atbrStpTable.setStatus("mandatory")
_AtbrStpEntry_Object = MibTableRow
atbrStpEntry = _AtbrStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1)
)
atbrStpEntry.setIndexNames(
    (0, "ATI-BRIDGE-MIB", "atbrStpLanId"),
)
if mibBuilder.loadTexts:
    atbrStpEntry.setStatus("mandatory")
_AtbrStpLanId_Type = Integer32
_AtbrStpLanId_Object = MibTableColumn
atbrStpLanId = _AtbrStpLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 1),
    _AtbrStpLanId_Type()
)
atbrStpLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpLanId.setStatus("mandatory")


class _AtbrStpProtocolSpecification_Type(Integer32):
    """Custom type atbrStpProtocolSpecification based on Integer32"""
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


_AtbrStpProtocolSpecification_Type.__name__ = "Integer32"
_AtbrStpProtocolSpecification_Object = MibTableColumn
atbrStpProtocolSpecification = _AtbrStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 2),
    _AtbrStpProtocolSpecification_Type()
)
atbrStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpProtocolSpecification.setStatus("mandatory")


class _AtbrStpPriority_Type(Integer32):
    """Custom type atbrStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtbrStpPriority_Type.__name__ = "Integer32"
_AtbrStpPriority_Object = MibTableColumn
atbrStpPriority = _AtbrStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 3),
    _AtbrStpPriority_Type()
)
atbrStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrStpPriority.setStatus("mandatory")
_AtbrStpTimeSinceTopologyChange_Type = TimeTicks
_AtbrStpTimeSinceTopologyChange_Object = MibTableColumn
atbrStpTimeSinceTopologyChange = _AtbrStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 4),
    _AtbrStpTimeSinceTopologyChange_Type()
)
atbrStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpTimeSinceTopologyChange.setStatus("mandatory")
_AtbrStpTopChanges_Type = Counter32
_AtbrStpTopChanges_Object = MibTableColumn
atbrStpTopChanges = _AtbrStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 5),
    _AtbrStpTopChanges_Type()
)
atbrStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpTopChanges.setStatus("mandatory")
_AtbrStpDesignatedRoot_Type = BridgeId
_AtbrStpDesignatedRoot_Object = MibTableColumn
atbrStpDesignatedRoot = _AtbrStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 6),
    _AtbrStpDesignatedRoot_Type()
)
atbrStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpDesignatedRoot.setStatus("mandatory")
_AtbrStpRootCost_Type = Integer32
_AtbrStpRootCost_Object = MibTableColumn
atbrStpRootCost = _AtbrStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 7),
    _AtbrStpRootCost_Type()
)
atbrStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpRootCost.setStatus("mandatory")
_AtbrStpRootPort_Type = Integer32
_AtbrStpRootPort_Object = MibTableColumn
atbrStpRootPort = _AtbrStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 8),
    _AtbrStpRootPort_Type()
)
atbrStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpRootPort.setStatus("mandatory")
_AtbrStpMaxAge_Type = Timeout
_AtbrStpMaxAge_Object = MibTableColumn
atbrStpMaxAge = _AtbrStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 9),
    _AtbrStpMaxAge_Type()
)
atbrStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpMaxAge.setStatus("mandatory")
_AtbrStpHelloTime_Type = Timeout
_AtbrStpHelloTime_Object = MibTableColumn
atbrStpHelloTime = _AtbrStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 10),
    _AtbrStpHelloTime_Type()
)
atbrStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpHelloTime.setStatus("mandatory")
_AtbrStpHoldTime_Type = Integer32
_AtbrStpHoldTime_Object = MibTableColumn
atbrStpHoldTime = _AtbrStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 11),
    _AtbrStpHoldTime_Type()
)
atbrStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpHoldTime.setStatus("mandatory")
_AtbrStpForwardDelay_Type = Timeout
_AtbrStpForwardDelay_Object = MibTableColumn
atbrStpForwardDelay = _AtbrStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 12),
    _AtbrStpForwardDelay_Type()
)
atbrStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpForwardDelay.setStatus("mandatory")


class _AtbrStpBridgeMaxAge_Type(Timeout):
    """Custom type atbrStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_AtbrStpBridgeMaxAge_Type.__name__ = "Timeout"
_AtbrStpBridgeMaxAge_Object = MibTableColumn
atbrStpBridgeMaxAge = _AtbrStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 13),
    _AtbrStpBridgeMaxAge_Type()
)
atbrStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrStpBridgeMaxAge.setStatus("mandatory")


class _AtbrStpBridgeHelloTime_Type(Timeout):
    """Custom type atbrStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_AtbrStpBridgeHelloTime_Type.__name__ = "Timeout"
_AtbrStpBridgeHelloTime_Object = MibTableColumn
atbrStpBridgeHelloTime = _AtbrStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 14),
    _AtbrStpBridgeHelloTime_Type()
)
atbrStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrStpBridgeHelloTime.setStatus("mandatory")


class _AtbrStpBridgeForwardDelay_Type(Timeout):
    """Custom type atbrStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_AtbrStpBridgeForwardDelay_Type.__name__ = "Timeout"
_AtbrStpBridgeForwardDelay_Object = MibTableColumn
atbrStpBridgeForwardDelay = _AtbrStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 1, 1, 15),
    _AtbrStpBridgeForwardDelay_Type()
)
atbrStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrStpBridgeForwardDelay.setStatus("mandatory")
_AtbrStpPortTable_Object = MibTable
atbrStpPortTable = _AtbrStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15)
)
if mibBuilder.loadTexts:
    atbrStpPortTable.setStatus("mandatory")
_AtbrStpPortEntry_Object = MibTableRow
atbrStpPortEntry = _AtbrStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1)
)
atbrStpPortEntry.setIndexNames(
    (0, "ATI-BRIDGE-MIB", "atbrStpPortLanId"),
    (0, "ATI-BRIDGE-MIB", "atbrStpPort"),
)
if mibBuilder.loadTexts:
    atbrStpPortEntry.setStatus("mandatory")
_AtbrStpPortLanId_Type = Integer32
_AtbrStpPortLanId_Object = MibTableColumn
atbrStpPortLanId = _AtbrStpPortLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 1),
    _AtbrStpPortLanId_Type()
)
atbrStpPortLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpPortLanId.setStatus("mandatory")


class _AtbrStpPort_Type(Integer32):
    """Custom type atbrStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtbrStpPort_Type.__name__ = "Integer32"
_AtbrStpPort_Object = MibTableColumn
atbrStpPort = _AtbrStpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 2),
    _AtbrStpPort_Type()
)
atbrStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpPort.setStatus("mandatory")


class _AtbrStpPortPriority_Type(Integer32):
    """Custom type atbrStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtbrStpPortPriority_Type.__name__ = "Integer32"
_AtbrStpPortPriority_Object = MibTableColumn
atbrStpPortPriority = _AtbrStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 3),
    _AtbrStpPortPriority_Type()
)
atbrStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrStpPortPriority.setStatus("mandatory")


class _AtbrStpPortState_Type(Integer32):
    """Custom type atbrStpPortState based on Integer32"""
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


_AtbrStpPortState_Type.__name__ = "Integer32"
_AtbrStpPortState_Object = MibTableColumn
atbrStpPortState = _AtbrStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 4),
    _AtbrStpPortState_Type()
)
atbrStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpPortState.setStatus("mandatory")


class _AtbrStpPortEnable_Type(Integer32):
    """Custom type atbrStpPortEnable based on Integer32"""
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


_AtbrStpPortEnable_Type.__name__ = "Integer32"
_AtbrStpPortEnable_Object = MibTableColumn
atbrStpPortEnable = _AtbrStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 5),
    _AtbrStpPortEnable_Type()
)
atbrStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrStpPortEnable.setStatus("mandatory")


class _AtbrStpPortPathCost_Type(Integer32):
    """Custom type atbrStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtbrStpPortPathCost_Type.__name__ = "Integer32"
_AtbrStpPortPathCost_Object = MibTableColumn
atbrStpPortPathCost = _AtbrStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 6),
    _AtbrStpPortPathCost_Type()
)
atbrStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrStpPortPathCost.setStatus("mandatory")
_AtbrStpPortDesignatedRoot_Type = BridgeId
_AtbrStpPortDesignatedRoot_Object = MibTableColumn
atbrStpPortDesignatedRoot = _AtbrStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 7),
    _AtbrStpPortDesignatedRoot_Type()
)
atbrStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpPortDesignatedRoot.setStatus("mandatory")
_AtbrStpPortDesignatedCost_Type = Integer32
_AtbrStpPortDesignatedCost_Object = MibTableColumn
atbrStpPortDesignatedCost = _AtbrStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 8),
    _AtbrStpPortDesignatedCost_Type()
)
atbrStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpPortDesignatedCost.setStatus("mandatory")
_AtbrStpPortDesignatedBridge_Type = BridgeId
_AtbrStpPortDesignatedBridge_Object = MibTableColumn
atbrStpPortDesignatedBridge = _AtbrStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 9),
    _AtbrStpPortDesignatedBridge_Type()
)
atbrStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpPortDesignatedBridge.setStatus("mandatory")


class _AtbrStpPortDesignatedPort_Type(OctetString):
    """Custom type atbrStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AtbrStpPortDesignatedPort_Type.__name__ = "OctetString"
_AtbrStpPortDesignatedPort_Object = MibTableColumn
atbrStpPortDesignatedPort = _AtbrStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 10),
    _AtbrStpPortDesignatedPort_Type()
)
atbrStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpPortDesignatedPort.setStatus("mandatory")
_AtbrStpPortForwardTransitions_Type = Counter32
_AtbrStpPortForwardTransitions_Object = MibTableColumn
atbrStpPortForwardTransitions = _AtbrStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 2, 15, 1, 11),
    _AtbrStpPortForwardTransitions_Type()
)
atbrStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStpPortForwardTransitions.setStatus("mandatory")
_AtbrSr_ObjectIdentity = ObjectIdentity
atbrSr = _AtbrSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 3)
)
_AtbrTp_ObjectIdentity = ObjectIdentity
atbrTp = _AtbrTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4)
)
_AtbrTpTable_Object = MibTable
atbrTpTable = _AtbrTpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 1)
)
if mibBuilder.loadTexts:
    atbrTpTable.setStatus("mandatory")
_AtbrTpEntry_Object = MibTableRow
atbrTpEntry = _AtbrTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 1, 1)
)
atbrTpEntry.setIndexNames(
    (0, "ATI-BRIDGE-MIB", "atbrTpLanId"),
)
if mibBuilder.loadTexts:
    atbrTpEntry.setStatus("mandatory")
_AtbrTpLanId_Type = Integer32
_AtbrTpLanId_Object = MibTableColumn
atbrTpLanId = _AtbrTpLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 1, 1, 1),
    _AtbrTpLanId_Type()
)
atbrTpLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpLanId.setStatus("mandatory")
_AtbrTpLearnedEntryDiscards_Type = Counter32
_AtbrTpLearnedEntryDiscards_Object = MibTableColumn
atbrTpLearnedEntryDiscards = _AtbrTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 1, 1, 2),
    _AtbrTpLearnedEntryDiscards_Type()
)
atbrTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpLearnedEntryDiscards.setStatus("mandatory")


class _AtbrTpAgingTime_Type(Integer32):
    """Custom type atbrTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_AtbrTpAgingTime_Type.__name__ = "Integer32"
_AtbrTpAgingTime_Object = MibTableColumn
atbrTpAgingTime = _AtbrTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 1, 1, 3),
    _AtbrTpAgingTime_Type()
)
atbrTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrTpAgingTime.setStatus("mandatory")
_AtbrTpFdbTable_Object = MibTable
atbrTpFdbTable = _AtbrTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3)
)
if mibBuilder.loadTexts:
    atbrTpFdbTable.setStatus("mandatory")
_AtbrTpFdbEntry_Object = MibTableRow
atbrTpFdbEntry = _AtbrTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3, 1)
)
atbrTpFdbEntry.setIndexNames(
    (0, "ATI-BRIDGE-MIB", "atbrTpFdbLanId"),
    (0, "ATI-BRIDGE-MIB", "atbrTpFdbAddress"),
)
if mibBuilder.loadTexts:
    atbrTpFdbEntry.setStatus("mandatory")
_AtbrTpFdbLanId_Type = Integer32
_AtbrTpFdbLanId_Object = MibTableColumn
atbrTpFdbLanId = _AtbrTpFdbLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3, 1, 1),
    _AtbrTpFdbLanId_Type()
)
atbrTpFdbLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpFdbLanId.setStatus("mandatory")
_AtbrTpFdbAddress_Type = MacAddress
_AtbrTpFdbAddress_Object = MibTableColumn
atbrTpFdbAddress = _AtbrTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3, 1, 2),
    _AtbrTpFdbAddress_Type()
)
atbrTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpFdbAddress.setStatus("mandatory")
_AtbrTpFdbPort_Type = Integer32
_AtbrTpFdbPort_Object = MibTableColumn
atbrTpFdbPort = _AtbrTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3, 1, 3),
    _AtbrTpFdbPort_Type()
)
atbrTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpFdbPort.setStatus("mandatory")


class _AtbrTpFdbStatus_Type(Integer32):
    """Custom type atbrTpFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("inactive", 1),
          ("join-pending", 5),
          ("le-arp-pending", 2),
          ("other", 7),
          ("vcc-setup-pending", 3),
          ("vlan-resolve-pending", 4))
    )


_AtbrTpFdbStatus_Type.__name__ = "Integer32"
_AtbrTpFdbStatus_Object = MibTableColumn
atbrTpFdbStatus = _AtbrTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 3, 1, 4),
    _AtbrTpFdbStatus_Type()
)
atbrTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpFdbStatus.setStatus("mandatory")
_AtbrTpPortTable_Object = MibTable
atbrTpPortTable = _AtbrTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4)
)
if mibBuilder.loadTexts:
    atbrTpPortTable.setStatus("mandatory")
_AtbrTpPortEntry_Object = MibTableRow
atbrTpPortEntry = _AtbrTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1)
)
atbrTpPortEntry.setIndexNames(
    (0, "ATI-BRIDGE-MIB", "atbrTpPortLanId"),
    (0, "ATI-BRIDGE-MIB", "atbrTpPort"),
)
if mibBuilder.loadTexts:
    atbrTpPortEntry.setStatus("mandatory")
_AtbrTpPortLanId_Type = Integer32
_AtbrTpPortLanId_Object = MibTableColumn
atbrTpPortLanId = _AtbrTpPortLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 1),
    _AtbrTpPortLanId_Type()
)
atbrTpPortLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpPortLanId.setStatus("mandatory")


class _AtbrTpPort_Type(Integer32):
    """Custom type atbrTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtbrTpPort_Type.__name__ = "Integer32"
_AtbrTpPort_Object = MibTableColumn
atbrTpPort = _AtbrTpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 2),
    _AtbrTpPort_Type()
)
atbrTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpPort.setStatus("mandatory")
_AtbrTpPortMaxInfo_Type = Integer32
_AtbrTpPortMaxInfo_Object = MibTableColumn
atbrTpPortMaxInfo = _AtbrTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 3),
    _AtbrTpPortMaxInfo_Type()
)
atbrTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpPortMaxInfo.setStatus("mandatory")
_AtbrTpPortInFrames_Type = Counter32
_AtbrTpPortInFrames_Object = MibTableColumn
atbrTpPortInFrames = _AtbrTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 4),
    _AtbrTpPortInFrames_Type()
)
atbrTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpPortInFrames.setStatus("mandatory")
_AtbrTpPortOutFrames_Type = Counter32
_AtbrTpPortOutFrames_Object = MibTableColumn
atbrTpPortOutFrames = _AtbrTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 5),
    _AtbrTpPortOutFrames_Type()
)
atbrTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpPortOutFrames.setStatus("mandatory")
_AtbrTpPortInDiscards_Type = Counter32
_AtbrTpPortInDiscards_Object = MibTableColumn
atbrTpPortInDiscards = _AtbrTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 4, 4, 1, 6),
    _AtbrTpPortInDiscards_Type()
)
atbrTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrTpPortInDiscards.setStatus("mandatory")
_AtbrStatic_ObjectIdentity = ObjectIdentity
atbrStatic = _AtbrStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5)
)
_AtbrStaticTable_Object = MibTable
atbrStaticTable = _AtbrStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1)
)
if mibBuilder.loadTexts:
    atbrStaticTable.setStatus("mandatory")
_AtbrStaticEntry_Object = MibTableRow
atbrStaticEntry = _AtbrStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1)
)
atbrStaticEntry.setIndexNames(
    (0, "ATI-BRIDGE-MIB", "atbrStaticLanId"),
    (0, "ATI-BRIDGE-MIB", "atbrStaticAddress"),
    (0, "ATI-BRIDGE-MIB", "atbrStaticReceivePort"),
)
if mibBuilder.loadTexts:
    atbrStaticEntry.setStatus("mandatory")
_AtbrStaticLanId_Type = Integer32
_AtbrStaticLanId_Object = MibTableColumn
atbrStaticLanId = _AtbrStaticLanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1, 1),
    _AtbrStaticLanId_Type()
)
atbrStaticLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atbrStaticLanId.setStatus("mandatory")
_AtbrStaticAddress_Type = MacAddress
_AtbrStaticAddress_Object = MibTableColumn
atbrStaticAddress = _AtbrStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1, 2),
    _AtbrStaticAddress_Type()
)
atbrStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrStaticAddress.setStatus("mandatory")
_AtbrStaticReceivePort_Type = Integer32
_AtbrStaticReceivePort_Object = MibTableColumn
atbrStaticReceivePort = _AtbrStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1, 3),
    _AtbrStaticReceivePort_Type()
)
atbrStaticReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrStaticReceivePort.setStatus("mandatory")
_AtbrStaticAllowedToGoTo_Type = OctetString
_AtbrStaticAllowedToGoTo_Object = MibTableColumn
atbrStaticAllowedToGoTo = _AtbrStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1, 4),
    _AtbrStaticAllowedToGoTo_Type()
)
atbrStaticAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrStaticAllowedToGoTo.setStatus("mandatory")


class _AtbrStaticStatus_Type(Integer32):
    """Custom type atbrStaticStatus based on Integer32"""
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


_AtbrStaticStatus_Type.__name__ = "Integer32"
_AtbrStaticStatus_Object = MibTableColumn
atbrStaticStatus = _AtbrStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 5, 10, 5, 1, 1, 5),
    _AtbrStaticStatus_Type()
)
atbrStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atbrStaticStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

newRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 0, 101)
)
if mibBuilder.loadTexts:
    newRoot.setStatus(
        ""
    )

topologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 0, 102)
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
    "ATI-BRIDGE-MIB",
    **{"MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "alliedTelesyn": alliedTelesyn,
       "newRoot": newRoot,
       "topologyChange": topologyChange,
       "mibObject": mibObject,
       "switchMib": switchMib,
       "atiBridgeMib": atiBridgeMib,
       "atbrBase": atbrBase,
       "atbrBaseTable": atbrBaseTable,
       "atbrBaseEntry": atbrBaseEntry,
       "atbrBaseLanId": atbrBaseLanId,
       "atbrBaseBridgeAddress": atbrBaseBridgeAddress,
       "atbrBaseNumPorts": atbrBaseNumPorts,
       "atbrBaseType": atbrBaseType,
       "atbrBasePortTable": atbrBasePortTable,
       "atbrBasePortEntry": atbrBasePortEntry,
       "atbrBasePortLanId": atbrBasePortLanId,
       "atbrBasePort": atbrBasePort,
       "atbrBasePortIfIndex": atbrBasePortIfIndex,
       "atbrBasePortCircuit": atbrBasePortCircuit,
       "atbrBasePortDelayExceededDiscards": atbrBasePortDelayExceededDiscards,
       "atbrBasePortMtuExceededDiscards": atbrBasePortMtuExceededDiscards,
       "atbrStp": atbrStp,
       "atbrStpTable": atbrStpTable,
       "atbrStpEntry": atbrStpEntry,
       "atbrStpLanId": atbrStpLanId,
       "atbrStpProtocolSpecification": atbrStpProtocolSpecification,
       "atbrStpPriority": atbrStpPriority,
       "atbrStpTimeSinceTopologyChange": atbrStpTimeSinceTopologyChange,
       "atbrStpTopChanges": atbrStpTopChanges,
       "atbrStpDesignatedRoot": atbrStpDesignatedRoot,
       "atbrStpRootCost": atbrStpRootCost,
       "atbrStpRootPort": atbrStpRootPort,
       "atbrStpMaxAge": atbrStpMaxAge,
       "atbrStpHelloTime": atbrStpHelloTime,
       "atbrStpHoldTime": atbrStpHoldTime,
       "atbrStpForwardDelay": atbrStpForwardDelay,
       "atbrStpBridgeMaxAge": atbrStpBridgeMaxAge,
       "atbrStpBridgeHelloTime": atbrStpBridgeHelloTime,
       "atbrStpBridgeForwardDelay": atbrStpBridgeForwardDelay,
       "atbrStpPortTable": atbrStpPortTable,
       "atbrStpPortEntry": atbrStpPortEntry,
       "atbrStpPortLanId": atbrStpPortLanId,
       "atbrStpPort": atbrStpPort,
       "atbrStpPortPriority": atbrStpPortPriority,
       "atbrStpPortState": atbrStpPortState,
       "atbrStpPortEnable": atbrStpPortEnable,
       "atbrStpPortPathCost": atbrStpPortPathCost,
       "atbrStpPortDesignatedRoot": atbrStpPortDesignatedRoot,
       "atbrStpPortDesignatedCost": atbrStpPortDesignatedCost,
       "atbrStpPortDesignatedBridge": atbrStpPortDesignatedBridge,
       "atbrStpPortDesignatedPort": atbrStpPortDesignatedPort,
       "atbrStpPortForwardTransitions": atbrStpPortForwardTransitions,
       "atbrSr": atbrSr,
       "atbrTp": atbrTp,
       "atbrTpTable": atbrTpTable,
       "atbrTpEntry": atbrTpEntry,
       "atbrTpLanId": atbrTpLanId,
       "atbrTpLearnedEntryDiscards": atbrTpLearnedEntryDiscards,
       "atbrTpAgingTime": atbrTpAgingTime,
       "atbrTpFdbTable": atbrTpFdbTable,
       "atbrTpFdbEntry": atbrTpFdbEntry,
       "atbrTpFdbLanId": atbrTpFdbLanId,
       "atbrTpFdbAddress": atbrTpFdbAddress,
       "atbrTpFdbPort": atbrTpFdbPort,
       "atbrTpFdbStatus": atbrTpFdbStatus,
       "atbrTpPortTable": atbrTpPortTable,
       "atbrTpPortEntry": atbrTpPortEntry,
       "atbrTpPortLanId": atbrTpPortLanId,
       "atbrTpPort": atbrTpPort,
       "atbrTpPortMaxInfo": atbrTpPortMaxInfo,
       "atbrTpPortInFrames": atbrTpPortInFrames,
       "atbrTpPortOutFrames": atbrTpPortOutFrames,
       "atbrTpPortInDiscards": atbrTpPortInDiscards,
       "atbrStatic": atbrStatic,
       "atbrStaticTable": atbrStaticTable,
       "atbrStaticEntry": atbrStaticEntry,
       "atbrStaticLanId": atbrStaticLanId,
       "atbrStaticAddress": atbrStaticAddress,
       "atbrStaticReceivePort": atbrStaticReceivePort,
       "atbrStaticAllowedToGoTo": atbrStaticAllowedToGoTo,
       "atbrStaticStatus": atbrStaticStatus}
)
