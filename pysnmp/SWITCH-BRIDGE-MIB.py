# SNMP MIB module (SWITCH-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWITCH-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:14 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(vLanNumber,) = mibBuilder.importSymbols(
    "SWITCH-VLAN-MIB",
    "vLanNumber")

(bridgeModule,) = mibBuilder.importSymbols(
    "TELESYN-ATI-TC",
    "bridgeModule")


# MODULE-IDENTITY

switchBridgeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5)
)
switchBridgeMib.setRevisions(
        ("1997-04-18 22:00",
         "1996-05-31 22:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BridgeId(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class Timeout(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_SwitchBridgeBase_ObjectIdentity = ObjectIdentity
switchBridgeBase = _SwitchBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1)
)
_SwitchBridgeBaseTable_Object = MibTable
switchBridgeBaseTable = _SwitchBridgeBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    switchBridgeBaseTable.setStatus("current")
_SwitchBridgeBaseEntry_Object = MibTableRow
switchBridgeBaseEntry = _SwitchBridgeBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 1, 1)
)
switchBridgeBaseEntry.setIndexNames(
    (0, "SWITCH-VLAN-MIB", "vLanNumber"),
)
if mibBuilder.loadTexts:
    switchBridgeBaseEntry.setStatus("current")
_SwitchBridgeBaseAddress_Type = MacAddress
_SwitchBridgeBaseAddress_Object = MibTableColumn
switchBridgeBaseAddress = _SwitchBridgeBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 1, 1, 1),
    _SwitchBridgeBaseAddress_Type()
)
switchBridgeBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeBaseAddress.setStatus("current")
_SwitchBridgeBaseNumPorts_Type = Integer32
_SwitchBridgeBaseNumPorts_Object = MibTableColumn
switchBridgeBaseNumPorts = _SwitchBridgeBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 1, 1, 2),
    _SwitchBridgeBaseNumPorts_Type()
)
switchBridgeBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeBaseNumPorts.setStatus("current")


class _SwitchBridgeBaseType_Type(Integer32):
    """Custom type switchBridgeBaseType based on Integer32"""
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
        *(("sourceRouteOnly", 3),
          ("srt", 4),
          ("transparentOnly", 2),
          ("unknown", 1))
    )


_SwitchBridgeBaseType_Type.__name__ = "Integer32"
_SwitchBridgeBaseType_Object = MibTableColumn
switchBridgeBaseType = _SwitchBridgeBaseType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 1, 1, 3),
    _SwitchBridgeBaseType_Type()
)
switchBridgeBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeBaseType.setStatus("current")
_SwitchBridgeBasePortTable_Object = MibTable
switchBridgeBasePortTable = _SwitchBridgeBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    switchBridgeBasePortTable.setStatus("current")
_SwitchBridgeBasePortEntry_Object = MibTableRow
switchBridgeBasePortEntry = _SwitchBridgeBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 2, 1)
)
switchBridgeBasePortEntry.setIndexNames(
    (0, "SWITCH-VLAN-MIB", "vLanNumber"),
    (0, "SWITCH-BRIDGE-MIB", "switchBridgeBasePort"),
)
if mibBuilder.loadTexts:
    switchBridgeBasePortEntry.setStatus("current")


class _SwitchBridgeBasePort_Type(Integer32):
    """Custom type switchBridgeBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SwitchBridgeBasePort_Type.__name__ = "Integer32"
_SwitchBridgeBasePort_Object = MibTableColumn
switchBridgeBasePort = _SwitchBridgeBasePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 2, 1, 1),
    _SwitchBridgeBasePort_Type()
)
switchBridgeBasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchBridgeBasePort.setStatus("current")
_SwitchBridgeBasePortIfIndex_Type = InterfaceIndex
_SwitchBridgeBasePortIfIndex_Object = MibTableColumn
switchBridgeBasePortIfIndex = _SwitchBridgeBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 2, 1, 2),
    _SwitchBridgeBasePortIfIndex_Type()
)
switchBridgeBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeBasePortIfIndex.setStatus("current")
_SwitchBridgeBasePortCircuit_Type = ObjectIdentifier
_SwitchBridgeBasePortCircuit_Object = MibTableColumn
switchBridgeBasePortCircuit = _SwitchBridgeBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 2, 1, 3),
    _SwitchBridgeBasePortCircuit_Type()
)
switchBridgeBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeBasePortCircuit.setStatus("current")
_SwitchBridgeBasePortDelayExceededDiscards_Type = Counter32
_SwitchBridgeBasePortDelayExceededDiscards_Object = MibTableColumn
switchBridgeBasePortDelayExceededDiscards = _SwitchBridgeBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 2, 1, 4),
    _SwitchBridgeBasePortDelayExceededDiscards_Type()
)
switchBridgeBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeBasePortDelayExceededDiscards.setStatus("current")
_SwitchBridgeBasePortMtuExceededDiscards_Type = Counter32
_SwitchBridgeBasePortMtuExceededDiscards_Object = MibTableColumn
switchBridgeBasePortMtuExceededDiscards = _SwitchBridgeBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 1, 2, 1, 5),
    _SwitchBridgeBasePortMtuExceededDiscards_Type()
)
switchBridgeBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeBasePortMtuExceededDiscards.setStatus("current")
_SwitchBridgeStp_ObjectIdentity = ObjectIdentity
switchBridgeStp = _SwitchBridgeStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2)
)
_SwitchBridgeStpTable_Object = MibTable
switchBridgeStpTable = _SwitchBridgeStpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    switchBridgeStpTable.setStatus("current")
_SwitchBridgeStpEntry_Object = MibTableRow
switchBridgeStpEntry = _SwitchBridgeStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1)
)
switchBridgeStpEntry.setIndexNames(
    (0, "SWITCH-VLAN-MIB", "vLanNumber"),
)
if mibBuilder.loadTexts:
    switchBridgeStpEntry.setStatus("current")


class _SwitchBridgeStpProtocolSpecification_Type(Integer32):
    """Custom type switchBridgeStpProtocolSpecification based on Integer32"""
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


_SwitchBridgeStpProtocolSpecification_Type.__name__ = "Integer32"
_SwitchBridgeStpProtocolSpecification_Object = MibTableColumn
switchBridgeStpProtocolSpecification = _SwitchBridgeStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 1),
    _SwitchBridgeStpProtocolSpecification_Type()
)
switchBridgeStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpProtocolSpecification.setStatus("current")


class _SwitchBridgeStpPriority_Type(Integer32):
    """Custom type switchBridgeStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwitchBridgeStpPriority_Type.__name__ = "Integer32"
_SwitchBridgeStpPriority_Object = MibTableColumn
switchBridgeStpPriority = _SwitchBridgeStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 2),
    _SwitchBridgeStpPriority_Type()
)
switchBridgeStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchBridgeStpPriority.setStatus("current")
_SwitchBridgeStpTimeSinceTopologyChange_Type = TimeTicks
_SwitchBridgeStpTimeSinceTopologyChange_Object = MibTableColumn
switchBridgeStpTimeSinceTopologyChange = _SwitchBridgeStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 3),
    _SwitchBridgeStpTimeSinceTopologyChange_Type()
)
switchBridgeStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpTimeSinceTopologyChange.setStatus("current")
_SwitchBridgeStpTopChanges_Type = Counter32
_SwitchBridgeStpTopChanges_Object = MibTableColumn
switchBridgeStpTopChanges = _SwitchBridgeStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 4),
    _SwitchBridgeStpTopChanges_Type()
)
switchBridgeStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpTopChanges.setStatus("current")
_SwitchBridgeStpDesignatedRoot_Type = BridgeId
_SwitchBridgeStpDesignatedRoot_Object = MibTableColumn
switchBridgeStpDesignatedRoot = _SwitchBridgeStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 5),
    _SwitchBridgeStpDesignatedRoot_Type()
)
switchBridgeStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpDesignatedRoot.setStatus("current")
_SwitchBridgeStpRootCost_Type = Integer32
_SwitchBridgeStpRootCost_Object = MibTableColumn
switchBridgeStpRootCost = _SwitchBridgeStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 6),
    _SwitchBridgeStpRootCost_Type()
)
switchBridgeStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpRootCost.setStatus("current")
_SwitchBridgeStpRootPort_Type = Integer32
_SwitchBridgeStpRootPort_Object = MibTableColumn
switchBridgeStpRootPort = _SwitchBridgeStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 7),
    _SwitchBridgeStpRootPort_Type()
)
switchBridgeStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpRootPort.setStatus("current")
_SwitchBridgeStpMaxAge_Type = Timeout
_SwitchBridgeStpMaxAge_Object = MibTableColumn
switchBridgeStpMaxAge = _SwitchBridgeStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 8),
    _SwitchBridgeStpMaxAge_Type()
)
switchBridgeStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpMaxAge.setStatus("current")
_SwitchBridgeStpHelloTime_Type = Timeout
_SwitchBridgeStpHelloTime_Object = MibTableColumn
switchBridgeStpHelloTime = _SwitchBridgeStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 9),
    _SwitchBridgeStpHelloTime_Type()
)
switchBridgeStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpHelloTime.setStatus("current")
_SwitchBridgeStpHoldTime_Type = Integer32
_SwitchBridgeStpHoldTime_Object = MibTableColumn
switchBridgeStpHoldTime = _SwitchBridgeStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 10),
    _SwitchBridgeStpHoldTime_Type()
)
switchBridgeStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpHoldTime.setStatus("current")
_SwitchBridgeStpForwardDelay_Type = Timeout
_SwitchBridgeStpForwardDelay_Object = MibTableColumn
switchBridgeStpForwardDelay = _SwitchBridgeStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 11),
    _SwitchBridgeStpForwardDelay_Type()
)
switchBridgeStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpForwardDelay.setStatus("current")


class _SwitchBridgeStpBridgeMaxAge_Type(Timeout):
    """Custom type switchBridgeStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_SwitchBridgeStpBridgeMaxAge_Type.__name__ = "Timeout"
_SwitchBridgeStpBridgeMaxAge_Object = MibTableColumn
switchBridgeStpBridgeMaxAge = _SwitchBridgeStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 12),
    _SwitchBridgeStpBridgeMaxAge_Type()
)
switchBridgeStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchBridgeStpBridgeMaxAge.setStatus("current")


class _SwitchBridgeStpBridgeHelloTime_Type(Timeout):
    """Custom type switchBridgeStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SwitchBridgeStpBridgeHelloTime_Type.__name__ = "Timeout"
_SwitchBridgeStpBridgeHelloTime_Object = MibTableColumn
switchBridgeStpBridgeHelloTime = _SwitchBridgeStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 13),
    _SwitchBridgeStpBridgeHelloTime_Type()
)
switchBridgeStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchBridgeStpBridgeHelloTime.setStatus("current")


class _SwitchBridgeStpBridgeForwardDelay_Type(Timeout):
    """Custom type switchBridgeStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_SwitchBridgeStpBridgeForwardDelay_Type.__name__ = "Timeout"
_SwitchBridgeStpBridgeForwardDelay_Object = MibTableColumn
switchBridgeStpBridgeForwardDelay = _SwitchBridgeStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 1, 1, 14),
    _SwitchBridgeStpBridgeForwardDelay_Type()
)
switchBridgeStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchBridgeStpBridgeForwardDelay.setStatus("current")
_SwitchBridgeStpPortTable_Object = MibTable
switchBridgeStpPortTable = _SwitchBridgeStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15)
)
if mibBuilder.loadTexts:
    switchBridgeStpPortTable.setStatus("current")
_SwitchBridgeStpPortEntry_Object = MibTableRow
switchBridgeStpPortEntry = _SwitchBridgeStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15, 1)
)
switchBridgeStpPortEntry.setIndexNames(
    (0, "SWITCH-VLAN-MIB", "vLanNumber"),
    (0, "SWITCH-BRIDGE-MIB", "switchBridgeStpPort"),
)
if mibBuilder.loadTexts:
    switchBridgeStpPortEntry.setStatus("current")


class _SwitchBridgeStpPort_Type(Integer32):
    """Custom type switchBridgeStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SwitchBridgeStpPort_Type.__name__ = "Integer32"
_SwitchBridgeStpPort_Object = MibTableColumn
switchBridgeStpPort = _SwitchBridgeStpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15, 1, 1),
    _SwitchBridgeStpPort_Type()
)
switchBridgeStpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchBridgeStpPort.setStatus("current")


class _SwitchBridgeStpPortPriority_Type(Integer32):
    """Custom type switchBridgeStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwitchBridgeStpPortPriority_Type.__name__ = "Integer32"
_SwitchBridgeStpPortPriority_Object = MibTableColumn
switchBridgeStpPortPriority = _SwitchBridgeStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15, 1, 2),
    _SwitchBridgeStpPortPriority_Type()
)
switchBridgeStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchBridgeStpPortPriority.setStatus("current")


class _SwitchBridgeStpPortState_Type(Integer32):
    """Custom type switchBridgeStpPortState based on Integer32"""
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


_SwitchBridgeStpPortState_Type.__name__ = "Integer32"
_SwitchBridgeStpPortState_Object = MibTableColumn
switchBridgeStpPortState = _SwitchBridgeStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15, 1, 3),
    _SwitchBridgeStpPortState_Type()
)
switchBridgeStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpPortState.setStatus("current")


class _SwitchBridgeStpPortEnable_Type(Integer32):
    """Custom type switchBridgeStpPortEnable based on Integer32"""
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


_SwitchBridgeStpPortEnable_Type.__name__ = "Integer32"
_SwitchBridgeStpPortEnable_Object = MibTableColumn
switchBridgeStpPortEnable = _SwitchBridgeStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15, 1, 4),
    _SwitchBridgeStpPortEnable_Type()
)
switchBridgeStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchBridgeStpPortEnable.setStatus("current")


class _SwitchBridgeStpPortPathCost_Type(Integer32):
    """Custom type switchBridgeStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchBridgeStpPortPathCost_Type.__name__ = "Integer32"
_SwitchBridgeStpPortPathCost_Object = MibTableColumn
switchBridgeStpPortPathCost = _SwitchBridgeStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15, 1, 5),
    _SwitchBridgeStpPortPathCost_Type()
)
switchBridgeStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchBridgeStpPortPathCost.setStatus("current")
_SwitchBridgeStpPortDesignatedRoot_Type = BridgeId
_SwitchBridgeStpPortDesignatedRoot_Object = MibTableColumn
switchBridgeStpPortDesignatedRoot = _SwitchBridgeStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15, 1, 6),
    _SwitchBridgeStpPortDesignatedRoot_Type()
)
switchBridgeStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpPortDesignatedRoot.setStatus("current")
_SwitchBridgeStpPortDesignatedCost_Type = Integer32
_SwitchBridgeStpPortDesignatedCost_Object = MibTableColumn
switchBridgeStpPortDesignatedCost = _SwitchBridgeStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15, 1, 7),
    _SwitchBridgeStpPortDesignatedCost_Type()
)
switchBridgeStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpPortDesignatedCost.setStatus("current")
_SwitchBridgeStpPortDesignatedBridge_Type = BridgeId
_SwitchBridgeStpPortDesignatedBridge_Object = MibTableColumn
switchBridgeStpPortDesignatedBridge = _SwitchBridgeStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15, 1, 8),
    _SwitchBridgeStpPortDesignatedBridge_Type()
)
switchBridgeStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpPortDesignatedBridge.setStatus("current")


class _SwitchBridgeStpPortDesignatedPort_Type(OctetString):
    """Custom type switchBridgeStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwitchBridgeStpPortDesignatedPort_Type.__name__ = "OctetString"
_SwitchBridgeStpPortDesignatedPort_Object = MibTableColumn
switchBridgeStpPortDesignatedPort = _SwitchBridgeStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15, 1, 9),
    _SwitchBridgeStpPortDesignatedPort_Type()
)
switchBridgeStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpPortDesignatedPort.setStatus("current")
_SwitchBridgeStpPortForwardTransitions_Type = Counter32
_SwitchBridgeStpPortForwardTransitions_Object = MibTableColumn
switchBridgeStpPortForwardTransitions = _SwitchBridgeStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 2, 15, 1, 10),
    _SwitchBridgeStpPortForwardTransitions_Type()
)
switchBridgeStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStpPortForwardTransitions.setStatus("current")
_SwitchBridgeSr_ObjectIdentity = ObjectIdentity
switchBridgeSr = _SwitchBridgeSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 3)
)
_SwitchBridgeTp_ObjectIdentity = ObjectIdentity
switchBridgeTp = _SwitchBridgeTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4)
)
_SwitchBridgeTpLearnedEntryDiscards_Type = Counter32
_SwitchBridgeTpLearnedEntryDiscards_Object = MibScalar
switchBridgeTpLearnedEntryDiscards = _SwitchBridgeTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 1),
    _SwitchBridgeTpLearnedEntryDiscards_Type()
)
switchBridgeTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeTpLearnedEntryDiscards.setStatus("current")
_SwitchBridgeTpBaseTable_Object = MibTable
switchBridgeTpBaseTable = _SwitchBridgeTpBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 2)
)
if mibBuilder.loadTexts:
    switchBridgeTpBaseTable.setStatus("current")
_SwitchBridgeTpBaseEntry_Object = MibTableRow
switchBridgeTpBaseEntry = _SwitchBridgeTpBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 2, 1)
)
switchBridgeTpBaseEntry.setIndexNames(
    (0, "SWITCH-VLAN-MIB", "vLanNumber"),
)
if mibBuilder.loadTexts:
    switchBridgeTpBaseEntry.setStatus("current")


class _SwitchBridgeTpAgingTime_Type(Integer32):
    """Custom type switchBridgeTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_SwitchBridgeTpAgingTime_Type.__name__ = "Integer32"
_SwitchBridgeTpAgingTime_Object = MibTableColumn
switchBridgeTpAgingTime = _SwitchBridgeTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 2, 1, 2),
    _SwitchBridgeTpAgingTime_Type()
)
switchBridgeTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchBridgeTpAgingTime.setStatus("current")
_SwitchBridgeTpFdbTable_Object = MibTable
switchBridgeTpFdbTable = _SwitchBridgeTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 3)
)
if mibBuilder.loadTexts:
    switchBridgeTpFdbTable.setStatus("current")
_SwitchBridgeTpFdbEntry_Object = MibTableRow
switchBridgeTpFdbEntry = _SwitchBridgeTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 3, 1)
)
switchBridgeTpFdbEntry.setIndexNames(
    (0, "SWITCH-BRIDGE-MIB", "switchBridgeStpPort"),
    (0, "SWITCH-BRIDGE-MIB", "switchBridgeTpFdbAddress"),
)
if mibBuilder.loadTexts:
    switchBridgeTpFdbEntry.setStatus("current")
_SwitchBridgeTpFdbAddress_Type = MacAddress
_SwitchBridgeTpFdbAddress_Object = MibTableColumn
switchBridgeTpFdbAddress = _SwitchBridgeTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 3, 1, 1),
    _SwitchBridgeTpFdbAddress_Type()
)
switchBridgeTpFdbAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchBridgeTpFdbAddress.setStatus("current")


class _SwitchBridgeTpFdbPort_Type(Integer32):
    """Custom type switchBridgeTpFdbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SwitchBridgeTpFdbPort_Type.__name__ = "Integer32"
_SwitchBridgeTpFdbPort_Object = MibTableColumn
switchBridgeTpFdbPort = _SwitchBridgeTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 3, 1, 2),
    _SwitchBridgeTpFdbPort_Type()
)
switchBridgeTpFdbPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchBridgeTpFdbPort.setStatus("obsolete")


class _SwitchBridgeTpFdbStatus_Type(Integer32):
    """Custom type switchBridgeTpFdbStatus based on Integer32"""
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


_SwitchBridgeTpFdbStatus_Type.__name__ = "Integer32"
_SwitchBridgeTpFdbStatus_Object = MibTableColumn
switchBridgeTpFdbStatus = _SwitchBridgeTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 3, 1, 3),
    _SwitchBridgeTpFdbStatus_Type()
)
switchBridgeTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeTpFdbStatus.setStatus("current")
_SwitchBridgeTpPortTable_Object = MibTable
switchBridgeTpPortTable = _SwitchBridgeTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 4)
)
if mibBuilder.loadTexts:
    switchBridgeTpPortTable.setStatus("current")
_SwitchBridgeTpPortEntry_Object = MibTableRow
switchBridgeTpPortEntry = _SwitchBridgeTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 4, 1)
)
switchBridgeTpPortEntry.setIndexNames(
    (0, "SWITCH-VLAN-MIB", "vLanNumber"),
    (0, "SWITCH-BRIDGE-MIB", "switchBridgeTpPort"),
)
if mibBuilder.loadTexts:
    switchBridgeTpPortEntry.setStatus("current")


class _SwitchBridgeTpPort_Type(Integer32):
    """Custom type switchBridgeTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SwitchBridgeTpPort_Type.__name__ = "Integer32"
_SwitchBridgeTpPort_Object = MibTableColumn
switchBridgeTpPort = _SwitchBridgeTpPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 4, 1, 1),
    _SwitchBridgeTpPort_Type()
)
switchBridgeTpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchBridgeTpPort.setStatus("current")


class _SwitchBridgeTpPortMaxInfo_Type(Integer32):
    """Custom type switchBridgeTpPortMaxInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwitchBridgeTpPortMaxInfo_Type.__name__ = "Integer32"
_SwitchBridgeTpPortMaxInfo_Object = MibTableColumn
switchBridgeTpPortMaxInfo = _SwitchBridgeTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 4, 1, 2),
    _SwitchBridgeTpPortMaxInfo_Type()
)
switchBridgeTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeTpPortMaxInfo.setStatus("current")
_SwitchBridgeTpPortInFrames_Type = Counter32
_SwitchBridgeTpPortInFrames_Object = MibTableColumn
switchBridgeTpPortInFrames = _SwitchBridgeTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 4, 1, 3),
    _SwitchBridgeTpPortInFrames_Type()
)
switchBridgeTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeTpPortInFrames.setStatus("current")
_SwitchBridgeTpPortOutFrames_Type = Counter32
_SwitchBridgeTpPortOutFrames_Object = MibTableColumn
switchBridgeTpPortOutFrames = _SwitchBridgeTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 4, 1, 4),
    _SwitchBridgeTpPortOutFrames_Type()
)
switchBridgeTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeTpPortOutFrames.setStatus("current")
_SwitchBridgeTpPortInDiscards_Type = Counter32
_SwitchBridgeTpPortInDiscards_Object = MibTableColumn
switchBridgeTpPortInDiscards = _SwitchBridgeTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 4, 4, 1, 5),
    _SwitchBridgeTpPortInDiscards_Type()
)
switchBridgeTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeTpPortInDiscards.setStatus("current")
_SwitchBridgeStatic_ObjectIdentity = ObjectIdentity
switchBridgeStatic = _SwitchBridgeStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 5)
)
_SwitchBridgeStaticTable_Object = MibTable
switchBridgeStaticTable = _SwitchBridgeStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    switchBridgeStaticTable.setStatus("current")
_SwitchBridgeStaticEntry_Object = MibTableRow
switchBridgeStaticEntry = _SwitchBridgeStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 5, 1, 1)
)
switchBridgeStaticEntry.setIndexNames(
    (0, "SWITCH-BRIDGE-MIB", "switchBridgeStpPort"),
    (0, "SWITCH-BRIDGE-MIB", "switchBridgeStaticAddress"),
)
if mibBuilder.loadTexts:
    switchBridgeStaticEntry.setStatus("current")
_SwitchBridgeStaticAddress_Type = MacAddress
_SwitchBridgeStaticAddress_Object = MibTableColumn
switchBridgeStaticAddress = _SwitchBridgeStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 5, 1, 1, 1),
    _SwitchBridgeStaticAddress_Type()
)
switchBridgeStaticAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchBridgeStaticAddress.setStatus("current")


class _SwitchBridgeStaticReceivePort_Type(Integer32):
    """Custom type switchBridgeStaticReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SwitchBridgeStaticReceivePort_Type.__name__ = "Integer32"
_SwitchBridgeStaticReceivePort_Object = MibTableColumn
switchBridgeStaticReceivePort = _SwitchBridgeStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 5, 1, 1, 2),
    _SwitchBridgeStaticReceivePort_Type()
)
switchBridgeStaticReceivePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    switchBridgeStaticReceivePort.setStatus("obsolete")


class _SwitchBridgeStaticAllowedToGoTo_Type(OctetString):
    """Custom type switchBridgeStaticAllowedToGoTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwitchBridgeStaticAllowedToGoTo_Type.__name__ = "OctetString"
_SwitchBridgeStaticAllowedToGoTo_Object = MibTableColumn
switchBridgeStaticAllowedToGoTo = _SwitchBridgeStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 5, 1, 1, 3),
    _SwitchBridgeStaticAllowedToGoTo_Type()
)
switchBridgeStaticAllowedToGoTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchBridgeStaticAllowedToGoTo.setStatus("current")


class _SwitchBridgeStaticStatus_Type(Integer32):
    """Custom type switchBridgeStaticStatus based on Integer32"""
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


_SwitchBridgeStaticStatus_Type.__name__ = "Integer32"
_SwitchBridgeStaticStatus_Object = MibTableColumn
switchBridgeStaticStatus = _SwitchBridgeStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 5, 1, 1, 4),
    _SwitchBridgeStaticStatus_Type()
)
switchBridgeStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    switchBridgeStaticStatus.setStatus("current")
_SwitchBridgeTrapsGroup_ObjectIdentity = ObjectIdentity
switchBridgeTrapsGroup = _SwitchBridgeTrapsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 6)
)
_SwitchBridgeTraps_ObjectIdentity = ObjectIdentity
switchBridgeTraps = _SwitchBridgeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 6, 0)
)

# Managed Objects groups


# Notification objects

switchNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 6, 0, 1)
)
switchNewRoot.setObjects(
    ("SWITCH-BRIDGE-MIB", "switchBridgeStpDesignatedRoot")
)
if mibBuilder.loadTexts:
    switchNewRoot.setStatus(
        "current"
    )

switchTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 2, 5, 6, 0, 2)
)
switchTopologyChange.setObjects(
    ("SWITCH-BRIDGE-MIB", "switchBridgeStpPortState")
)
if mibBuilder.loadTexts:
    switchTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-BRIDGE-MIB",
    **{"BridgeId": BridgeId,
       "Timeout": Timeout,
       "switchBridgeMib": switchBridgeMib,
       "switchBridgeBase": switchBridgeBase,
       "switchBridgeBaseTable": switchBridgeBaseTable,
       "switchBridgeBaseEntry": switchBridgeBaseEntry,
       "switchBridgeBaseAddress": switchBridgeBaseAddress,
       "switchBridgeBaseNumPorts": switchBridgeBaseNumPorts,
       "switchBridgeBaseType": switchBridgeBaseType,
       "switchBridgeBasePortTable": switchBridgeBasePortTable,
       "switchBridgeBasePortEntry": switchBridgeBasePortEntry,
       "switchBridgeBasePort": switchBridgeBasePort,
       "switchBridgeBasePortIfIndex": switchBridgeBasePortIfIndex,
       "switchBridgeBasePortCircuit": switchBridgeBasePortCircuit,
       "switchBridgeBasePortDelayExceededDiscards": switchBridgeBasePortDelayExceededDiscards,
       "switchBridgeBasePortMtuExceededDiscards": switchBridgeBasePortMtuExceededDiscards,
       "switchBridgeStp": switchBridgeStp,
       "switchBridgeStpTable": switchBridgeStpTable,
       "switchBridgeStpEntry": switchBridgeStpEntry,
       "switchBridgeStpProtocolSpecification": switchBridgeStpProtocolSpecification,
       "switchBridgeStpPriority": switchBridgeStpPriority,
       "switchBridgeStpTimeSinceTopologyChange": switchBridgeStpTimeSinceTopologyChange,
       "switchBridgeStpTopChanges": switchBridgeStpTopChanges,
       "switchBridgeStpDesignatedRoot": switchBridgeStpDesignatedRoot,
       "switchBridgeStpRootCost": switchBridgeStpRootCost,
       "switchBridgeStpRootPort": switchBridgeStpRootPort,
       "switchBridgeStpMaxAge": switchBridgeStpMaxAge,
       "switchBridgeStpHelloTime": switchBridgeStpHelloTime,
       "switchBridgeStpHoldTime": switchBridgeStpHoldTime,
       "switchBridgeStpForwardDelay": switchBridgeStpForwardDelay,
       "switchBridgeStpBridgeMaxAge": switchBridgeStpBridgeMaxAge,
       "switchBridgeStpBridgeHelloTime": switchBridgeStpBridgeHelloTime,
       "switchBridgeStpBridgeForwardDelay": switchBridgeStpBridgeForwardDelay,
       "switchBridgeStpPortTable": switchBridgeStpPortTable,
       "switchBridgeStpPortEntry": switchBridgeStpPortEntry,
       "switchBridgeStpPort": switchBridgeStpPort,
       "switchBridgeStpPortPriority": switchBridgeStpPortPriority,
       "switchBridgeStpPortState": switchBridgeStpPortState,
       "switchBridgeStpPortEnable": switchBridgeStpPortEnable,
       "switchBridgeStpPortPathCost": switchBridgeStpPortPathCost,
       "switchBridgeStpPortDesignatedRoot": switchBridgeStpPortDesignatedRoot,
       "switchBridgeStpPortDesignatedCost": switchBridgeStpPortDesignatedCost,
       "switchBridgeStpPortDesignatedBridge": switchBridgeStpPortDesignatedBridge,
       "switchBridgeStpPortDesignatedPort": switchBridgeStpPortDesignatedPort,
       "switchBridgeStpPortForwardTransitions": switchBridgeStpPortForwardTransitions,
       "switchBridgeSr": switchBridgeSr,
       "switchBridgeTp": switchBridgeTp,
       "switchBridgeTpLearnedEntryDiscards": switchBridgeTpLearnedEntryDiscards,
       "switchBridgeTpBaseTable": switchBridgeTpBaseTable,
       "switchBridgeTpBaseEntry": switchBridgeTpBaseEntry,
       "switchBridgeTpAgingTime": switchBridgeTpAgingTime,
       "switchBridgeTpFdbTable": switchBridgeTpFdbTable,
       "switchBridgeTpFdbEntry": switchBridgeTpFdbEntry,
       "switchBridgeTpFdbAddress": switchBridgeTpFdbAddress,
       "switchBridgeTpFdbPort": switchBridgeTpFdbPort,
       "switchBridgeTpFdbStatus": switchBridgeTpFdbStatus,
       "switchBridgeTpPortTable": switchBridgeTpPortTable,
       "switchBridgeTpPortEntry": switchBridgeTpPortEntry,
       "switchBridgeTpPort": switchBridgeTpPort,
       "switchBridgeTpPortMaxInfo": switchBridgeTpPortMaxInfo,
       "switchBridgeTpPortInFrames": switchBridgeTpPortInFrames,
       "switchBridgeTpPortOutFrames": switchBridgeTpPortOutFrames,
       "switchBridgeTpPortInDiscards": switchBridgeTpPortInDiscards,
       "switchBridgeStatic": switchBridgeStatic,
       "switchBridgeStaticTable": switchBridgeStaticTable,
       "switchBridgeStaticEntry": switchBridgeStaticEntry,
       "switchBridgeStaticAddress": switchBridgeStaticAddress,
       "switchBridgeStaticReceivePort": switchBridgeStaticReceivePort,
       "switchBridgeStaticAllowedToGoTo": switchBridgeStaticAllowedToGoTo,
       "switchBridgeStaticStatus": switchBridgeStaticStatus,
       "switchBridgeTrapsGroup": switchBridgeTrapsGroup,
       "switchBridgeTraps": switchBridgeTraps,
       "switchNewRoot": switchNewRoot,
       "switchTopologyChange": switchTopologyChange}
)
