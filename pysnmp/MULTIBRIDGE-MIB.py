# SNMP MIB module (MULTIBRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MULTIBRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:06 2024
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

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtensions")

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

nncExtMultiBridge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 43)
)


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

_MBrdgBase_ObjectIdentity = ObjectIdentity
mBrdgBase = _MBrdgBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1)
)
_MBrdgBaseTable_Object = MibTable
mBrdgBaseTable = _MBrdgBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 1)
)
if mibBuilder.loadTexts:
    mBrdgBaseTable.setStatus("current")
_MBrdgBaseEntry_Object = MibTableRow
mBrdgBaseEntry = _MBrdgBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 1, 1)
)
mBrdgBaseEntry.setIndexNames(
    (0, "MULTIBRIDGE-MIB", "mBrdgBaseBridgeAddress"),
)
if mibBuilder.loadTexts:
    mBrdgBaseEntry.setStatus("current")
_MBrdgBaseBridgeAddress_Type = MacAddress
_MBrdgBaseBridgeAddress_Object = MibTableColumn
mBrdgBaseBridgeAddress = _MBrdgBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 1, 1, 1),
    _MBrdgBaseBridgeAddress_Type()
)
mBrdgBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgBaseBridgeAddress.setStatus("current")
_MBrdgBaseNumPorts_Type = Integer32
_MBrdgBaseNumPorts_Object = MibTableColumn
mBrdgBaseNumPorts = _MBrdgBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 1, 1, 2),
    _MBrdgBaseNumPorts_Type()
)
mBrdgBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgBaseNumPorts.setStatus("current")


class _MBrdgBaseType_Type(Integer32):
    """Custom type mBrdgBaseType based on Integer32"""
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
        *(("sourcerouteOnly", 3),
          ("srt", 4),
          ("transparentOnly", 2),
          ("unknown", 1))
    )


_MBrdgBaseType_Type.__name__ = "Integer32"
_MBrdgBaseType_Object = MibTableColumn
mBrdgBaseType = _MBrdgBaseType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 1, 1, 3),
    _MBrdgBaseType_Type()
)
mBrdgBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgBaseType.setStatus("current")
_MBrdgBasePortTable_Object = MibTable
mBrdgBasePortTable = _MBrdgBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2)
)
if mibBuilder.loadTexts:
    mBrdgBasePortTable.setStatus("current")
_MBrdgBasePortEntry_Object = MibTableRow
mBrdgBasePortEntry = _MBrdgBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1)
)
mBrdgBasePortEntry.setIndexNames(
    (0, "MULTIBRIDGE-MIB", "mBrdgBasePortBridgeIndex"),
    (0, "MULTIBRIDGE-MIB", "mBrdgBasePort"),
)
if mibBuilder.loadTexts:
    mBrdgBasePortEntry.setStatus("current")


class _MBrdgBasePort_Type(Integer32):
    """Custom type mBrdgBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgBasePort_Type.__name__ = "Integer32"
_MBrdgBasePort_Object = MibTableColumn
mBrdgBasePort = _MBrdgBasePort_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 1),
    _MBrdgBasePort_Type()
)
mBrdgBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgBasePort.setStatus("current")
_MBrdgBasePortIfIndex_Type = Integer32
_MBrdgBasePortIfIndex_Object = MibTableColumn
mBrdgBasePortIfIndex = _MBrdgBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 2),
    _MBrdgBasePortIfIndex_Type()
)
mBrdgBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgBasePortIfIndex.setStatus("current")
_MBrdgBasePortCircuit_Type = ObjectIdentifier
_MBrdgBasePortCircuit_Object = MibTableColumn
mBrdgBasePortCircuit = _MBrdgBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 3),
    _MBrdgBasePortCircuit_Type()
)
mBrdgBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgBasePortCircuit.setStatus("current")
_MBrdgBasePortDelayExceededDiscards_Type = Counter32
_MBrdgBasePortDelayExceededDiscards_Object = MibTableColumn
mBrdgBasePortDelayExceededDiscards = _MBrdgBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 4),
    _MBrdgBasePortDelayExceededDiscards_Type()
)
mBrdgBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgBasePortDelayExceededDiscards.setStatus("current")
_MBrdgBasePortMtuExceededDiscards_Type = Counter32
_MBrdgBasePortMtuExceededDiscards_Object = MibTableColumn
mBrdgBasePortMtuExceededDiscards = _MBrdgBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 5),
    _MBrdgBasePortMtuExceededDiscards_Type()
)
mBrdgBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgBasePortMtuExceededDiscards.setStatus("current")


class _MBrdgBasePortBridgeIndex_Type(Integer32):
    """Custom type mBrdgBasePortBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgBasePortBridgeIndex_Type.__name__ = "Integer32"
_MBrdgBasePortBridgeIndex_Object = MibTableColumn
mBrdgBasePortBridgeIndex = _MBrdgBasePortBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 6),
    _MBrdgBasePortBridgeIndex_Type()
)
mBrdgBasePortBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgBasePortBridgeIndex.setStatus("current")
_MBrdgStp_ObjectIdentity = ObjectIdentity
mBrdgStp = _MBrdgStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2)
)
_MBrdgStpTable_Object = MibTable
mBrdgStpTable = _MBrdgStpTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1)
)
if mibBuilder.loadTexts:
    mBrdgStpTable.setStatus("current")
_MBrdgStpEntry_Object = MibTableRow
mBrdgStpEntry = _MBrdgStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1)
)
mBrdgStpEntry.setIndexNames(
    (0, "MULTIBRIDGE-MIB", "mBrdgStpBridgeIndex"),
)
if mibBuilder.loadTexts:
    mBrdgStpEntry.setStatus("current")


class _MBrdgStpProtocolSpecification_Type(Integer32):
    """Custom type mBrdgStpProtocolSpecification based on Integer32"""
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


_MBrdgStpProtocolSpecification_Type.__name__ = "Integer32"
_MBrdgStpProtocolSpecification_Object = MibTableColumn
mBrdgStpProtocolSpecification = _MBrdgStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 1),
    _MBrdgStpProtocolSpecification_Type()
)
mBrdgStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpProtocolSpecification.setStatus("current")


class _MBrdgStpPriority_Type(Integer32):
    """Custom type mBrdgStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MBrdgStpPriority_Type.__name__ = "Integer32"
_MBrdgStpPriority_Object = MibTableColumn
mBrdgStpPriority = _MBrdgStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 2),
    _MBrdgStpPriority_Type()
)
mBrdgStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStpPriority.setStatus("current")
_MBrdgStpTimeSinceTopologyChange_Type = TimeTicks
_MBrdgStpTimeSinceTopologyChange_Object = MibTableColumn
mBrdgStpTimeSinceTopologyChange = _MBrdgStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 3),
    _MBrdgStpTimeSinceTopologyChange_Type()
)
mBrdgStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpTimeSinceTopologyChange.setStatus("current")
_MBrdgStpTopChanges_Type = Counter32
_MBrdgStpTopChanges_Object = MibTableColumn
mBrdgStpTopChanges = _MBrdgStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 4),
    _MBrdgStpTopChanges_Type()
)
mBrdgStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpTopChanges.setStatus("current")
_MBrdgStpDesignatedRoot_Type = BridgeId
_MBrdgStpDesignatedRoot_Object = MibTableColumn
mBrdgStpDesignatedRoot = _MBrdgStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 5),
    _MBrdgStpDesignatedRoot_Type()
)
mBrdgStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpDesignatedRoot.setStatus("current")
_MBrdgStpRootCost_Type = Integer32
_MBrdgStpRootCost_Object = MibTableColumn
mBrdgStpRootCost = _MBrdgStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 6),
    _MBrdgStpRootCost_Type()
)
mBrdgStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpRootCost.setStatus("current")
_MBrdgStpRootPort_Type = Integer32
_MBrdgStpRootPort_Object = MibTableColumn
mBrdgStpRootPort = _MBrdgStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 7),
    _MBrdgStpRootPort_Type()
)
mBrdgStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpRootPort.setStatus("current")
_MBrdgStpMaxAge_Type = Timeout
_MBrdgStpMaxAge_Object = MibTableColumn
mBrdgStpMaxAge = _MBrdgStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 8),
    _MBrdgStpMaxAge_Type()
)
mBrdgStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpMaxAge.setStatus("current")
_MBrdgStpHelloTime_Type = Timeout
_MBrdgStpHelloTime_Object = MibTableColumn
mBrdgStpHelloTime = _MBrdgStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 9),
    _MBrdgStpHelloTime_Type()
)
mBrdgStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpHelloTime.setStatus("current")
_MBrdgStpHoldTime_Type = Integer32
_MBrdgStpHoldTime_Object = MibTableColumn
mBrdgStpHoldTime = _MBrdgStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 10),
    _MBrdgStpHoldTime_Type()
)
mBrdgStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpHoldTime.setStatus("current")
_MBrdgStpForwardDelay_Type = Timeout
_MBrdgStpForwardDelay_Object = MibTableColumn
mBrdgStpForwardDelay = _MBrdgStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 11),
    _MBrdgStpForwardDelay_Type()
)
mBrdgStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpForwardDelay.setStatus("current")


class _MBrdgStpBridgeMaxAge_Type(Timeout):
    """Custom type mBrdgStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MBrdgStpBridgeMaxAge_Type.__name__ = "Timeout"
_MBrdgStpBridgeMaxAge_Object = MibTableColumn
mBrdgStpBridgeMaxAge = _MBrdgStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 12),
    _MBrdgStpBridgeMaxAge_Type()
)
mBrdgStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStpBridgeMaxAge.setStatus("current")


class _MBrdgStpBridgeHelloTime_Type(Timeout):
    """Custom type mBrdgStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MBrdgStpBridgeHelloTime_Type.__name__ = "Timeout"
_MBrdgStpBridgeHelloTime_Object = MibTableColumn
mBrdgStpBridgeHelloTime = _MBrdgStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 13),
    _MBrdgStpBridgeHelloTime_Type()
)
mBrdgStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStpBridgeHelloTime.setStatus("current")


class _MBrdgStpBridgeForwardDelay_Type(Timeout):
    """Custom type mBrdgStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MBrdgStpBridgeForwardDelay_Type.__name__ = "Timeout"
_MBrdgStpBridgeForwardDelay_Object = MibTableColumn
mBrdgStpBridgeForwardDelay = _MBrdgStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 14),
    _MBrdgStpBridgeForwardDelay_Type()
)
mBrdgStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStpBridgeForwardDelay.setStatus("current")


class _MBrdgStpEnable_Type(Integer32):
    """Custom type mBrdgStpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unavailable", 3))
    )


_MBrdgStpEnable_Type.__name__ = "Integer32"
_MBrdgStpEnable_Object = MibTableColumn
mBrdgStpEnable = _MBrdgStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 15),
    _MBrdgStpEnable_Type()
)
mBrdgStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStpEnable.setStatus("current")


class _MBrdgStpBridgeIndex_Type(Integer32):
    """Custom type mBrdgStpBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgStpBridgeIndex_Type.__name__ = "Integer32"
_MBrdgStpBridgeIndex_Object = MibTableColumn
mBrdgStpBridgeIndex = _MBrdgStpBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 16),
    _MBrdgStpBridgeIndex_Type()
)
mBrdgStpBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpBridgeIndex.setStatus("current")
_MBrdgStpPortTable_Object = MibTable
mBrdgStpPortTable = _MBrdgStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2)
)
if mibBuilder.loadTexts:
    mBrdgStpPortTable.setStatus("current")
_MBrdgStpPortEntry_Object = MibTableRow
mBrdgStpPortEntry = _MBrdgStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1)
)
mBrdgStpPortEntry.setIndexNames(
    (0, "MULTIBRIDGE-MIB", "mBrdgStpPortBridgeIndex"),
    (0, "MULTIBRIDGE-MIB", "mBrdgStpPort"),
)
if mibBuilder.loadTexts:
    mBrdgStpPortEntry.setStatus("current")


class _MBrdgStpPort_Type(Integer32):
    """Custom type mBrdgStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgStpPort_Type.__name__ = "Integer32"
_MBrdgStpPort_Object = MibTableColumn
mBrdgStpPort = _MBrdgStpPort_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 1),
    _MBrdgStpPort_Type()
)
mBrdgStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpPort.setStatus("current")


class _MBrdgStpPortPriority_Type(Integer32):
    """Custom type mBrdgStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MBrdgStpPortPriority_Type.__name__ = "Integer32"
_MBrdgStpPortPriority_Object = MibTableColumn
mBrdgStpPortPriority = _MBrdgStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 2),
    _MBrdgStpPortPriority_Type()
)
mBrdgStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStpPortPriority.setStatus("current")


class _MBrdgStpPortState_Type(Integer32):
    """Custom type mBrdgStpPortState based on Integer32"""
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


_MBrdgStpPortState_Type.__name__ = "Integer32"
_MBrdgStpPortState_Object = MibTableColumn
mBrdgStpPortState = _MBrdgStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 3),
    _MBrdgStpPortState_Type()
)
mBrdgStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpPortState.setStatus("current")


class _MBrdgStpPortEnable_Type(Integer32):
    """Custom type mBrdgStpPortEnable based on Integer32"""
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


_MBrdgStpPortEnable_Type.__name__ = "Integer32"
_MBrdgStpPortEnable_Object = MibTableColumn
mBrdgStpPortEnable = _MBrdgStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 4),
    _MBrdgStpPortEnable_Type()
)
mBrdgStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStpPortEnable.setStatus("current")


class _MBrdgStpPortPathCost_Type(Integer32):
    """Custom type mBrdgStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgStpPortPathCost_Type.__name__ = "Integer32"
_MBrdgStpPortPathCost_Object = MibTableColumn
mBrdgStpPortPathCost = _MBrdgStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 5),
    _MBrdgStpPortPathCost_Type()
)
mBrdgStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStpPortPathCost.setStatus("current")
_MBrdgStpPortDesignatedRoot_Type = BridgeId
_MBrdgStpPortDesignatedRoot_Object = MibTableColumn
mBrdgStpPortDesignatedRoot = _MBrdgStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 6),
    _MBrdgStpPortDesignatedRoot_Type()
)
mBrdgStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpPortDesignatedRoot.setStatus("current")
_MBrdgStpPortDesignatedCost_Type = Integer32
_MBrdgStpPortDesignatedCost_Object = MibTableColumn
mBrdgStpPortDesignatedCost = _MBrdgStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 7),
    _MBrdgStpPortDesignatedCost_Type()
)
mBrdgStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpPortDesignatedCost.setStatus("current")
_MBrdgStpPortDesignatedBridge_Type = BridgeId
_MBrdgStpPortDesignatedBridge_Object = MibTableColumn
mBrdgStpPortDesignatedBridge = _MBrdgStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 8),
    _MBrdgStpPortDesignatedBridge_Type()
)
mBrdgStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpPortDesignatedBridge.setStatus("current")


class _MBrdgStpPortDesignatedPort_Type(OctetString):
    """Custom type mBrdgStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MBrdgStpPortDesignatedPort_Type.__name__ = "OctetString"
_MBrdgStpPortDesignatedPort_Object = MibTableColumn
mBrdgStpPortDesignatedPort = _MBrdgStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 9),
    _MBrdgStpPortDesignatedPort_Type()
)
mBrdgStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpPortDesignatedPort.setStatus("current")
_MBrdgStpPortForwardTransitions_Type = Counter32
_MBrdgStpPortForwardTransitions_Object = MibTableColumn
mBrdgStpPortForwardTransitions = _MBrdgStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 10),
    _MBrdgStpPortForwardTransitions_Type()
)
mBrdgStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpPortForwardTransitions.setStatus("current")
_MBrdgStpPortStatsTxBPDUCount_Type = Counter32
_MBrdgStpPortStatsTxBPDUCount_Object = MibTableColumn
mBrdgStpPortStatsTxBPDUCount = _MBrdgStpPortStatsTxBPDUCount_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 11),
    _MBrdgStpPortStatsTxBPDUCount_Type()
)
mBrdgStpPortStatsTxBPDUCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStpPortStatsTxBPDUCount.setStatus("current")
_MBrdgStpPortStatsRxBPDUCount_Type = Counter32
_MBrdgStpPortStatsRxBPDUCount_Object = MibTableColumn
mBrdgStpPortStatsRxBPDUCount = _MBrdgStpPortStatsRxBPDUCount_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 12),
    _MBrdgStpPortStatsRxBPDUCount_Type()
)
mBrdgStpPortStatsRxBPDUCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStpPortStatsRxBPDUCount.setStatus("current")


class _MBrdgStpPortBridgeIndex_Type(Integer32):
    """Custom type mBrdgStpPortBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgStpPortBridgeIndex_Type.__name__ = "Integer32"
_MBrdgStpPortBridgeIndex_Object = MibTableColumn
mBrdgStpPortBridgeIndex = _MBrdgStpPortBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 13),
    _MBrdgStpPortBridgeIndex_Type()
)
mBrdgStpPortBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStpPortBridgeIndex.setStatus("current")
_MBrdgTp_ObjectIdentity = ObjectIdentity
mBrdgTp = _MBrdgTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3)
)
_MBrdgTpTable_Object = MibTable
mBrdgTpTable = _MBrdgTpTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1)
)
if mibBuilder.loadTexts:
    mBrdgTpTable.setStatus("current")
_MBrdgTpEntry_Object = MibTableRow
mBrdgTpEntry = _MBrdgTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1)
)
mBrdgTpEntry.setIndexNames(
    (0, "MULTIBRIDGE-MIB", "mBrdgTpBridgeIndex"),
)
if mibBuilder.loadTexts:
    mBrdgTpEntry.setStatus("current")
_MBrdgTpLearnedEntryDiscards_Type = Counter32
_MBrdgTpLearnedEntryDiscards_Object = MibTableColumn
mBrdgTpLearnedEntryDiscards = _MBrdgTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 1),
    _MBrdgTpLearnedEntryDiscards_Type()
)
mBrdgTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpLearnedEntryDiscards.setStatus("current")


class _MBrdgTpAgingTime_Type(Integer32):
    """Custom type mBrdgTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_MBrdgTpAgingTime_Type.__name__ = "Integer32"
_MBrdgTpAgingTime_Object = MibTableColumn
mBrdgTpAgingTime = _MBrdgTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 2),
    _MBrdgTpAgingTime_Type()
)
mBrdgTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgTpAgingTime.setStatus("current")


class _MBrdgTpLearningEnable_Type(Integer32):
    """Custom type mBrdgTpLearningEnable based on Integer32"""
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


_MBrdgTpLearningEnable_Type.__name__ = "Integer32"
_MBrdgTpLearningEnable_Object = MibTableColumn
mBrdgTpLearningEnable = _MBrdgTpLearningEnable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 3),
    _MBrdgTpLearningEnable_Type()
)
mBrdgTpLearningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgTpLearningEnable.setStatus("current")
_MBrdgTpFdbNumLearnedEntries_Type = Integer32
_MBrdgTpFdbNumLearnedEntries_Object = MibTableColumn
mBrdgTpFdbNumLearnedEntries = _MBrdgTpFdbNumLearnedEntries_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 4),
    _MBrdgTpFdbNumLearnedEntries_Type()
)
mBrdgTpFdbNumLearnedEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgTpFdbNumLearnedEntries.setStatus("current")
_MBrdgTpFdbNumEntries_Type = Integer32
_MBrdgTpFdbNumEntries_Object = MibTableColumn
mBrdgTpFdbNumEntries = _MBrdgTpFdbNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 5),
    _MBrdgTpFdbNumEntries_Type()
)
mBrdgTpFdbNumEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgTpFdbNumEntries.setStatus("current")


class _MBrdgTpBridgeIndex_Type(Integer32):
    """Custom type mBrdgTpBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgTpBridgeIndex_Type.__name__ = "Integer32"
_MBrdgTpBridgeIndex_Object = MibTableColumn
mBrdgTpBridgeIndex = _MBrdgTpBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 6),
    _MBrdgTpBridgeIndex_Type()
)
mBrdgTpBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpBridgeIndex.setStatus("current")
_MBrdgTpFdbTable_Object = MibTable
mBrdgTpFdbTable = _MBrdgTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2)
)
if mibBuilder.loadTexts:
    mBrdgTpFdbTable.setStatus("current")
_MBrdgTpFdbEntry_Object = MibTableRow
mBrdgTpFdbEntry = _MBrdgTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2, 1)
)
mBrdgTpFdbEntry.setIndexNames(
    (0, "MULTIBRIDGE-MIB", "mBrdgTpFdbBridgeIndex"),
    (0, "MULTIBRIDGE-MIB", "mBrdgTpFdbAddress"),
)
if mibBuilder.loadTexts:
    mBrdgTpFdbEntry.setStatus("current")
_MBrdgTpFdbAddress_Type = MacAddress
_MBrdgTpFdbAddress_Object = MibTableColumn
mBrdgTpFdbAddress = _MBrdgTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2, 1, 1),
    _MBrdgTpFdbAddress_Type()
)
mBrdgTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpFdbAddress.setStatus("current")
_MBrdgTpFdbPort_Type = Integer32
_MBrdgTpFdbPort_Object = MibTableColumn
mBrdgTpFdbPort = _MBrdgTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2, 1, 2),
    _MBrdgTpFdbPort_Type()
)
mBrdgTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpFdbPort.setStatus("current")


class _MBrdgTpFdbStatus_Type(Integer32):
    """Custom type mBrdgTpFdbStatus based on Integer32"""
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


_MBrdgTpFdbStatus_Type.__name__ = "Integer32"
_MBrdgTpFdbStatus_Object = MibTableColumn
mBrdgTpFdbStatus = _MBrdgTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2, 1, 3),
    _MBrdgTpFdbStatus_Type()
)
mBrdgTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpFdbStatus.setStatus("current")


class _MBrdgTpFdbBridgeIndex_Type(Integer32):
    """Custom type mBrdgTpFdbBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgTpFdbBridgeIndex_Type.__name__ = "Integer32"
_MBrdgTpFdbBridgeIndex_Object = MibTableColumn
mBrdgTpFdbBridgeIndex = _MBrdgTpFdbBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2, 1, 4),
    _MBrdgTpFdbBridgeIndex_Type()
)
mBrdgTpFdbBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpFdbBridgeIndex.setStatus("current")
_MBrdgTpPortTable_Object = MibTable
mBrdgTpPortTable = _MBrdgTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3)
)
if mibBuilder.loadTexts:
    mBrdgTpPortTable.setStatus("current")
_MBrdgTpPortEntry_Object = MibTableRow
mBrdgTpPortEntry = _MBrdgTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1)
)
mBrdgTpPortEntry.setIndexNames(
    (0, "MULTIBRIDGE-MIB", "mBrdgTpPortBridgeIndex"),
    (0, "MULTIBRIDGE-MIB", "mBrdgTpPort"),
)
if mibBuilder.loadTexts:
    mBrdgTpPortEntry.setStatus("current")


class _MBrdgTpPort_Type(Integer32):
    """Custom type mBrdgTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgTpPort_Type.__name__ = "Integer32"
_MBrdgTpPort_Object = MibTableColumn
mBrdgTpPort = _MBrdgTpPort_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 1),
    _MBrdgTpPort_Type()
)
mBrdgTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpPort.setStatus("current")
_MBrdgTpPortMaxInfo_Type = Integer32
_MBrdgTpPortMaxInfo_Object = MibTableColumn
mBrdgTpPortMaxInfo = _MBrdgTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 2),
    _MBrdgTpPortMaxInfo_Type()
)
mBrdgTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpPortMaxInfo.setStatus("current")
_MBrdgTpPortInFrames_Type = Counter32
_MBrdgTpPortInFrames_Object = MibTableColumn
mBrdgTpPortInFrames = _MBrdgTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 3),
    _MBrdgTpPortInFrames_Type()
)
mBrdgTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpPortInFrames.setStatus("current")
_MBrdgTpPortOutFrames_Type = Counter32
_MBrdgTpPortOutFrames_Object = MibTableColumn
mBrdgTpPortOutFrames = _MBrdgTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 4),
    _MBrdgTpPortOutFrames_Type()
)
mBrdgTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpPortOutFrames.setStatus("current")
_MBrdgTpPortInDiscards_Type = Counter32
_MBrdgTpPortInDiscards_Object = MibTableColumn
mBrdgTpPortInDiscards = _MBrdgTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 5),
    _MBrdgTpPortInDiscards_Type()
)
mBrdgTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpPortInDiscards.setStatus("current")


class _MBrdgTpPortBridgeIndex_Type(Integer32):
    """Custom type mBrdgTpPortBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgTpPortBridgeIndex_Type.__name__ = "Integer32"
_MBrdgTpPortBridgeIndex_Object = MibTableColumn
mBrdgTpPortBridgeIndex = _MBrdgTpPortBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 6),
    _MBrdgTpPortBridgeIndex_Type()
)
mBrdgTpPortBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgTpPortBridgeIndex.setStatus("current")
_MBrdgStatic_ObjectIdentity = ObjectIdentity
mBrdgStatic = _MBrdgStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 4)
)
_MBrdgStaticTable_Object = MibTable
mBrdgStaticTable = _MBrdgStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1)
)
if mibBuilder.loadTexts:
    mBrdgStaticTable.setStatus("current")
_MBrdgStaticEntry_Object = MibTableRow
mBrdgStaticEntry = _MBrdgStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1)
)
mBrdgStaticEntry.setIndexNames(
    (0, "MULTIBRIDGE-MIB", "mBrdgStaticBridgeIndex"),
    (0, "MULTIBRIDGE-MIB", "mBrdgStaticAddress"),
    (0, "MULTIBRIDGE-MIB", "mBrdgStaticReceivePort"),
)
if mibBuilder.loadTexts:
    mBrdgStaticEntry.setStatus("current")
_MBrdgStaticAddress_Type = MacAddress
_MBrdgStaticAddress_Object = MibTableColumn
mBrdgStaticAddress = _MBrdgStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1, 1),
    _MBrdgStaticAddress_Type()
)
mBrdgStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStaticAddress.setStatus("current")
_MBrdgStaticReceivePort_Type = Integer32
_MBrdgStaticReceivePort_Object = MibTableColumn
mBrdgStaticReceivePort = _MBrdgStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1, 2),
    _MBrdgStaticReceivePort_Type()
)
mBrdgStaticReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStaticReceivePort.setStatus("current")
_MBrdgStaticAllowedToGoTo_Type = OctetString
_MBrdgStaticAllowedToGoTo_Object = MibTableColumn
mBrdgStaticAllowedToGoTo = _MBrdgStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1, 3),
    _MBrdgStaticAllowedToGoTo_Type()
)
mBrdgStaticAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStaticAllowedToGoTo.setStatus("current")


class _MBrdgStaticStatus_Type(Integer32):
    """Custom type mBrdgStaticStatus based on Integer32"""
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


_MBrdgStaticStatus_Type.__name__ = "Integer32"
_MBrdgStaticStatus_Object = MibTableColumn
mBrdgStaticStatus = _MBrdgStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1, 4),
    _MBrdgStaticStatus_Type()
)
mBrdgStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgStaticStatus.setStatus("current")


class _MBrdgStaticBridgeIndex_Type(Integer32):
    """Custom type mBrdgStaticBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgStaticBridgeIndex_Type.__name__ = "Integer32"
_MBrdgStaticBridgeIndex_Object = MibTableColumn
mBrdgStaticBridgeIndex = _MBrdgStaticBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1, 7),
    _MBrdgStaticBridgeIndex_Type()
)
mBrdgStaticBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgStaticBridgeIndex.setStatus("current")
_MBrdgConfig_ObjectIdentity = ObjectIdentity
mBrdgConfig = _MBrdgConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 5)
)
_MBrdgConfigTable_Object = MibTable
mBrdgConfigTable = _MBrdgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 5, 1)
)
if mibBuilder.loadTexts:
    mBrdgConfigTable.setStatus("current")
_MBrdgConfigEntry_Object = MibTableRow
mBrdgConfigEntry = _MBrdgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 5, 1, 1)
)
mBrdgConfigEntry.setIndexNames(
    (0, "MULTIBRIDGE-MIB", "mBrdgConfigBridgeIndex"),
)
if mibBuilder.loadTexts:
    mBrdgConfigEntry.setStatus("current")


class _MBrdgConfigBridgeIndex_Type(Integer32):
    """Custom type mBrdgConfigBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MBrdgConfigBridgeIndex_Type.__name__ = "Integer32"
_MBrdgConfigBridgeIndex_Object = MibTableColumn
mBrdgConfigBridgeIndex = _MBrdgConfigBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 5, 1, 1, 1),
    _MBrdgConfigBridgeIndex_Type()
)
mBrdgConfigBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mBrdgConfigBridgeIndex.setStatus("current")


class _MBrdgConfigBridgeName_Type(OctetString):
    """Custom type mBrdgConfigBridgeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MBrdgConfigBridgeName_Type.__name__ = "OctetString"
_MBrdgConfigBridgeName_Object = MibTableColumn
mBrdgConfigBridgeName = _MBrdgConfigBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 5, 1, 1, 2),
    _MBrdgConfigBridgeName_Type()
)
mBrdgConfigBridgeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgConfigBridgeName.setStatus("current")


class _MBrdgConfigBridgePeakRate_Type(Integer32):
    """Custom type mBrdgConfigBridgePeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MBrdgConfigBridgePeakRate_Type.__name__ = "Integer32"
_MBrdgConfigBridgePeakRate_Object = MibTableColumn
mBrdgConfigBridgePeakRate = _MBrdgConfigBridgePeakRate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 43, 5, 1, 1, 3),
    _MBrdgConfigBridgePeakRate_Type()
)
mBrdgConfigBridgePeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mBrdgConfigBridgePeakRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MULTIBRIDGE-MIB",
    **{"MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "nncExtMultiBridge": nncExtMultiBridge,
       "mBrdgBase": mBrdgBase,
       "mBrdgBaseTable": mBrdgBaseTable,
       "mBrdgBaseEntry": mBrdgBaseEntry,
       "mBrdgBaseBridgeAddress": mBrdgBaseBridgeAddress,
       "mBrdgBaseNumPorts": mBrdgBaseNumPorts,
       "mBrdgBaseType": mBrdgBaseType,
       "mBrdgBasePortTable": mBrdgBasePortTable,
       "mBrdgBasePortEntry": mBrdgBasePortEntry,
       "mBrdgBasePort": mBrdgBasePort,
       "mBrdgBasePortIfIndex": mBrdgBasePortIfIndex,
       "mBrdgBasePortCircuit": mBrdgBasePortCircuit,
       "mBrdgBasePortDelayExceededDiscards": mBrdgBasePortDelayExceededDiscards,
       "mBrdgBasePortMtuExceededDiscards": mBrdgBasePortMtuExceededDiscards,
       "mBrdgBasePortBridgeIndex": mBrdgBasePortBridgeIndex,
       "mBrdgStp": mBrdgStp,
       "mBrdgStpTable": mBrdgStpTable,
       "mBrdgStpEntry": mBrdgStpEntry,
       "mBrdgStpProtocolSpecification": mBrdgStpProtocolSpecification,
       "mBrdgStpPriority": mBrdgStpPriority,
       "mBrdgStpTimeSinceTopologyChange": mBrdgStpTimeSinceTopologyChange,
       "mBrdgStpTopChanges": mBrdgStpTopChanges,
       "mBrdgStpDesignatedRoot": mBrdgStpDesignatedRoot,
       "mBrdgStpRootCost": mBrdgStpRootCost,
       "mBrdgStpRootPort": mBrdgStpRootPort,
       "mBrdgStpMaxAge": mBrdgStpMaxAge,
       "mBrdgStpHelloTime": mBrdgStpHelloTime,
       "mBrdgStpHoldTime": mBrdgStpHoldTime,
       "mBrdgStpForwardDelay": mBrdgStpForwardDelay,
       "mBrdgStpBridgeMaxAge": mBrdgStpBridgeMaxAge,
       "mBrdgStpBridgeHelloTime": mBrdgStpBridgeHelloTime,
       "mBrdgStpBridgeForwardDelay": mBrdgStpBridgeForwardDelay,
       "mBrdgStpEnable": mBrdgStpEnable,
       "mBrdgStpBridgeIndex": mBrdgStpBridgeIndex,
       "mBrdgStpPortTable": mBrdgStpPortTable,
       "mBrdgStpPortEntry": mBrdgStpPortEntry,
       "mBrdgStpPort": mBrdgStpPort,
       "mBrdgStpPortPriority": mBrdgStpPortPriority,
       "mBrdgStpPortState": mBrdgStpPortState,
       "mBrdgStpPortEnable": mBrdgStpPortEnable,
       "mBrdgStpPortPathCost": mBrdgStpPortPathCost,
       "mBrdgStpPortDesignatedRoot": mBrdgStpPortDesignatedRoot,
       "mBrdgStpPortDesignatedCost": mBrdgStpPortDesignatedCost,
       "mBrdgStpPortDesignatedBridge": mBrdgStpPortDesignatedBridge,
       "mBrdgStpPortDesignatedPort": mBrdgStpPortDesignatedPort,
       "mBrdgStpPortForwardTransitions": mBrdgStpPortForwardTransitions,
       "mBrdgStpPortStatsTxBPDUCount": mBrdgStpPortStatsTxBPDUCount,
       "mBrdgStpPortStatsRxBPDUCount": mBrdgStpPortStatsRxBPDUCount,
       "mBrdgStpPortBridgeIndex": mBrdgStpPortBridgeIndex,
       "mBrdgTp": mBrdgTp,
       "mBrdgTpTable": mBrdgTpTable,
       "mBrdgTpEntry": mBrdgTpEntry,
       "mBrdgTpLearnedEntryDiscards": mBrdgTpLearnedEntryDiscards,
       "mBrdgTpAgingTime": mBrdgTpAgingTime,
       "mBrdgTpLearningEnable": mBrdgTpLearningEnable,
       "mBrdgTpFdbNumLearnedEntries": mBrdgTpFdbNumLearnedEntries,
       "mBrdgTpFdbNumEntries": mBrdgTpFdbNumEntries,
       "mBrdgTpBridgeIndex": mBrdgTpBridgeIndex,
       "mBrdgTpFdbTable": mBrdgTpFdbTable,
       "mBrdgTpFdbEntry": mBrdgTpFdbEntry,
       "mBrdgTpFdbAddress": mBrdgTpFdbAddress,
       "mBrdgTpFdbPort": mBrdgTpFdbPort,
       "mBrdgTpFdbStatus": mBrdgTpFdbStatus,
       "mBrdgTpFdbBridgeIndex": mBrdgTpFdbBridgeIndex,
       "mBrdgTpPortTable": mBrdgTpPortTable,
       "mBrdgTpPortEntry": mBrdgTpPortEntry,
       "mBrdgTpPort": mBrdgTpPort,
       "mBrdgTpPortMaxInfo": mBrdgTpPortMaxInfo,
       "mBrdgTpPortInFrames": mBrdgTpPortInFrames,
       "mBrdgTpPortOutFrames": mBrdgTpPortOutFrames,
       "mBrdgTpPortInDiscards": mBrdgTpPortInDiscards,
       "mBrdgTpPortBridgeIndex": mBrdgTpPortBridgeIndex,
       "mBrdgStatic": mBrdgStatic,
       "mBrdgStaticTable": mBrdgStaticTable,
       "mBrdgStaticEntry": mBrdgStaticEntry,
       "mBrdgStaticAddress": mBrdgStaticAddress,
       "mBrdgStaticReceivePort": mBrdgStaticReceivePort,
       "mBrdgStaticAllowedToGoTo": mBrdgStaticAllowedToGoTo,
       "mBrdgStaticStatus": mBrdgStaticStatus,
       "mBrdgStaticBridgeIndex": mBrdgStaticBridgeIndex,
       "mBrdgConfig": mBrdgConfig,
       "mBrdgConfigTable": mBrdgConfigTable,
       "mBrdgConfigEntry": mBrdgConfigEntry,
       "mBrdgConfigBridgeIndex": mBrdgConfigBridgeIndex,
       "mBrdgConfigBridgeName": mBrdgConfigBridgeName,
       "mBrdgConfigBridgePeakRate": mBrdgConfigBridgePeakRate}
)
