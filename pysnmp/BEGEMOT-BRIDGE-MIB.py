# SNMP MIB module (BEGEMOT-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BEGEMOT-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:41 2024
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

(begemot,) = mibBuilder.importSymbols(
    "BEGEMOT-MIB",
    "begemot")

(BridgeId,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

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
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

begemotBridge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205)
)
begemotBridge.setRevisions(
        ("2007-08-06 00:00",
         "2006-11-21 00:00",
         "2006-07-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BridgeIfName(OctetString, TextualConvention):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class BridgeIfNameOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class BridgePortId(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x.1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



# MIB Managed Objects in the order of their OIDs

_BegemotBridgeNotifications_ObjectIdentity = ObjectIdentity
begemotBridgeNotifications = _BegemotBridgeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 0)
)
_BegemotBridgeBase_ObjectIdentity = ObjectIdentity
begemotBridgeBase = _BegemotBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1)
)
_BegemotBridgeBaseTable_Object = MibTable
begemotBridgeBaseTable = _BegemotBridgeBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1)
)
if mibBuilder.loadTexts:
    begemotBridgeBaseTable.setStatus("current")
_BegemotBridgeBaseEntry_Object = MibTableRow
begemotBridgeBaseEntry = _BegemotBridgeBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1)
)
begemotBridgeBaseEntry.setIndexNames(
    (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"),
)
if mibBuilder.loadTexts:
    begemotBridgeBaseEntry.setStatus("current")
_BegemotBridgeBaseName_Type = BridgeIfName
_BegemotBridgeBaseName_Object = MibTableColumn
begemotBridgeBaseName = _BegemotBridgeBaseName_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1, 1),
    _BegemotBridgeBaseName_Type()
)
begemotBridgeBaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeBaseName.setStatus("current")
_BegemotBridgeBaseAddress_Type = MacAddress
_BegemotBridgeBaseAddress_Object = MibTableColumn
begemotBridgeBaseAddress = _BegemotBridgeBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1, 2),
    _BegemotBridgeBaseAddress_Type()
)
begemotBridgeBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeBaseAddress.setStatus("current")
_BegemotBridgeBaseNumPorts_Type = Integer32
_BegemotBridgeBaseNumPorts_Object = MibTableColumn
begemotBridgeBaseNumPorts = _BegemotBridgeBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1, 3),
    _BegemotBridgeBaseNumPorts_Type()
)
begemotBridgeBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeBaseNumPorts.setStatus("current")


class _BegemotBridgeBaseType_Type(Integer32):
    """Custom type begemotBridgeBaseType based on Integer32"""
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


_BegemotBridgeBaseType_Type.__name__ = "Integer32"
_BegemotBridgeBaseType_Object = MibTableColumn
begemotBridgeBaseType = _BegemotBridgeBaseType_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1, 4),
    _BegemotBridgeBaseType_Type()
)
begemotBridgeBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeBaseType.setStatus("current")
_BegemotBridgeBaseStatus_Type = RowStatus
_BegemotBridgeBaseStatus_Object = MibTableColumn
begemotBridgeBaseStatus = _BegemotBridgeBaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1, 5),
    _BegemotBridgeBaseStatus_Type()
)
begemotBridgeBaseStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    begemotBridgeBaseStatus.setStatus("current")
_BegemotBridgeBasePortTable_Object = MibTable
begemotBridgeBasePortTable = _BegemotBridgeBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2)
)
if mibBuilder.loadTexts:
    begemotBridgeBasePortTable.setStatus("current")
_BegemotBridgeBasePortEntry_Object = MibTableRow
begemotBridgeBasePortEntry = _BegemotBridgeBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1)
)
begemotBridgeBasePortEntry.setIndexNames(
    (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"),
    (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBasePortIfIndex"),
)
if mibBuilder.loadTexts:
    begemotBridgeBasePortEntry.setStatus("current")


class _BegemotBridgeBasePort_Type(Integer32):
    """Custom type begemotBridgeBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BegemotBridgeBasePort_Type.__name__ = "Integer32"
_BegemotBridgeBasePort_Object = MibTableColumn
begemotBridgeBasePort = _BegemotBridgeBasePort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 1),
    _BegemotBridgeBasePort_Type()
)
begemotBridgeBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeBasePort.setStatus("current")
_BegemotBridgeBasePortIfIndex_Type = InterfaceIndex
_BegemotBridgeBasePortIfIndex_Object = MibTableColumn
begemotBridgeBasePortIfIndex = _BegemotBridgeBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 2),
    _BegemotBridgeBasePortIfIndex_Type()
)
begemotBridgeBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeBasePortIfIndex.setStatus("current")


class _BegemotBridgeBaseSpanEnabled_Type(Integer32):
    """Custom type begemotBridgeBaseSpanEnabled based on Integer32"""
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


_BegemotBridgeBaseSpanEnabled_Type.__name__ = "Integer32"
_BegemotBridgeBaseSpanEnabled_Object = MibTableColumn
begemotBridgeBaseSpanEnabled = _BegemotBridgeBaseSpanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 3),
    _BegemotBridgeBaseSpanEnabled_Type()
)
begemotBridgeBaseSpanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeBaseSpanEnabled.setStatus("current")
_BegemotBridgeBasePortDelayExceededDiscards_Type = Counter32
_BegemotBridgeBasePortDelayExceededDiscards_Object = MibTableColumn
begemotBridgeBasePortDelayExceededDiscards = _BegemotBridgeBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 4),
    _BegemotBridgeBasePortDelayExceededDiscards_Type()
)
begemotBridgeBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeBasePortDelayExceededDiscards.setStatus("current")
_BegemotBridgeBasePortMtuExceededDiscards_Type = Counter32
_BegemotBridgeBasePortMtuExceededDiscards_Object = MibTableColumn
begemotBridgeBasePortMtuExceededDiscards = _BegemotBridgeBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 5),
    _BegemotBridgeBasePortMtuExceededDiscards_Type()
)
begemotBridgeBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeBasePortMtuExceededDiscards.setStatus("current")
_BegemotBridgeBasePortStatus_Type = RowStatus
_BegemotBridgeBasePortStatus_Object = MibTableColumn
begemotBridgeBasePortStatus = _BegemotBridgeBasePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 6),
    _BegemotBridgeBasePortStatus_Type()
)
begemotBridgeBasePortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    begemotBridgeBasePortStatus.setStatus("current")
_BegemotBridgeBasePortPrivate_Type = TruthValue
_BegemotBridgeBasePortPrivate_Object = MibTableColumn
begemotBridgeBasePortPrivate = _BegemotBridgeBasePortPrivate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 7),
    _BegemotBridgeBasePortPrivate_Type()
)
begemotBridgeBasePortPrivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeBasePortPrivate.setStatus("current")
_BegemotBridgeStp_ObjectIdentity = ObjectIdentity
begemotBridgeStp = _BegemotBridgeStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2)
)
_BegemotBridgeStpTable_Object = MibTable
begemotBridgeStpTable = _BegemotBridgeStpTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1)
)
if mibBuilder.loadTexts:
    begemotBridgeStpTable.setStatus("current")
_BegemotBridgeStpEntry_Object = MibTableRow
begemotBridgeStpEntry = _BegemotBridgeStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1)
)
if mibBuilder.loadTexts:
    begemotBridgeStpEntry.setStatus("current")


class _BegemotBridgeStpProtocolSpecification_Type(Integer32):
    """Custom type begemotBridgeStpProtocolSpecification based on Integer32"""
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


_BegemotBridgeStpProtocolSpecification_Type.__name__ = "Integer32"
_BegemotBridgeStpProtocolSpecification_Object = MibTableColumn
begemotBridgeStpProtocolSpecification = _BegemotBridgeStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 1),
    _BegemotBridgeStpProtocolSpecification_Type()
)
begemotBridgeStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpProtocolSpecification.setStatus("current")


class _BegemotBridgeStpPriority_Type(Integer32):
    """Custom type begemotBridgeStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BegemotBridgeStpPriority_Type.__name__ = "Integer32"
_BegemotBridgeStpPriority_Object = MibTableColumn
begemotBridgeStpPriority = _BegemotBridgeStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 2),
    _BegemotBridgeStpPriority_Type()
)
begemotBridgeStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpPriority.setStatus("current")
_BegemotBridgeStpTimeSinceTopologyChange_Type = TimeTicks
_BegemotBridgeStpTimeSinceTopologyChange_Object = MibTableColumn
begemotBridgeStpTimeSinceTopologyChange = _BegemotBridgeStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 3),
    _BegemotBridgeStpTimeSinceTopologyChange_Type()
)
begemotBridgeStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpTimeSinceTopologyChange.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeStpTimeSinceTopologyChange.setUnits("centi-seconds")
_BegemotBridgeStpTopChanges_Type = Counter32
_BegemotBridgeStpTopChanges_Object = MibTableColumn
begemotBridgeStpTopChanges = _BegemotBridgeStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 4),
    _BegemotBridgeStpTopChanges_Type()
)
begemotBridgeStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpTopChanges.setStatus("current")
_BegemotBridgeStpDesignatedRoot_Type = BridgeId
_BegemotBridgeStpDesignatedRoot_Object = MibTableColumn
begemotBridgeStpDesignatedRoot = _BegemotBridgeStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 5),
    _BegemotBridgeStpDesignatedRoot_Type()
)
begemotBridgeStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpDesignatedRoot.setStatus("current")
_BegemotBridgeStpRootCost_Type = Integer32
_BegemotBridgeStpRootCost_Object = MibTableColumn
begemotBridgeStpRootCost = _BegemotBridgeStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 6),
    _BegemotBridgeStpRootCost_Type()
)
begemotBridgeStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpRootCost.setStatus("current")
_BegemotBridgeStpRootPort_Type = Integer32
_BegemotBridgeStpRootPort_Object = MibTableColumn
begemotBridgeStpRootPort = _BegemotBridgeStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 7),
    _BegemotBridgeStpRootPort_Type()
)
begemotBridgeStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpRootPort.setStatus("current")
_BegemotBridgeStpMaxAge_Type = Timeout
_BegemotBridgeStpMaxAge_Object = MibTableColumn
begemotBridgeStpMaxAge = _BegemotBridgeStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 8),
    _BegemotBridgeStpMaxAge_Type()
)
begemotBridgeStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeStpMaxAge.setUnits("centi-seconds")
_BegemotBridgeStpHelloTime_Type = Timeout
_BegemotBridgeStpHelloTime_Object = MibTableColumn
begemotBridgeStpHelloTime = _BegemotBridgeStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 9),
    _BegemotBridgeStpHelloTime_Type()
)
begemotBridgeStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeStpHelloTime.setUnits("centi-seconds")
_BegemotBridgeStpHoldTime_Type = Integer32
_BegemotBridgeStpHoldTime_Object = MibTableColumn
begemotBridgeStpHoldTime = _BegemotBridgeStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 10),
    _BegemotBridgeStpHoldTime_Type()
)
begemotBridgeStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeStpHoldTime.setUnits("centi-seconds")
_BegemotBridgeStpForwardDelay_Type = Timeout
_BegemotBridgeStpForwardDelay_Object = MibTableColumn
begemotBridgeStpForwardDelay = _BegemotBridgeStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 11),
    _BegemotBridgeStpForwardDelay_Type()
)
begemotBridgeStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeStpForwardDelay.setUnits("centi-seconds")


class _BegemotBridgeStpBridgeMaxAge_Type(Timeout):
    """Custom type begemotBridgeStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_BegemotBridgeStpBridgeMaxAge_Type.__name__ = "Timeout"
_BegemotBridgeStpBridgeMaxAge_Object = MibTableColumn
begemotBridgeStpBridgeMaxAge = _BegemotBridgeStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 12),
    _BegemotBridgeStpBridgeMaxAge_Type()
)
begemotBridgeStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpBridgeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeStpBridgeMaxAge.setUnits("centi-seconds")


class _BegemotBridgeStpBridgeHelloTime_Type(Timeout):
    """Custom type begemotBridgeStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_BegemotBridgeStpBridgeHelloTime_Type.__name__ = "Timeout"
_BegemotBridgeStpBridgeHelloTime_Object = MibTableColumn
begemotBridgeStpBridgeHelloTime = _BegemotBridgeStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 13),
    _BegemotBridgeStpBridgeHelloTime_Type()
)
begemotBridgeStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeStpBridgeHelloTime.setUnits("centi-seconds")


class _BegemotBridgeStpBridgeForwardDelay_Type(Timeout):
    """Custom type begemotBridgeStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_BegemotBridgeStpBridgeForwardDelay_Type.__name__ = "Timeout"
_BegemotBridgeStpBridgeForwardDelay_Object = MibTableColumn
begemotBridgeStpBridgeForwardDelay = _BegemotBridgeStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 14),
    _BegemotBridgeStpBridgeForwardDelay_Type()
)
begemotBridgeStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpBridgeForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeStpBridgeForwardDelay.setUnits("centi-seconds")


class _BegemotBridgeStpVersion_Type(Integer32):
    """Custom type begemotBridgeStpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stpCompatible", 0))
    )


_BegemotBridgeStpVersion_Type.__name__ = "Integer32"
_BegemotBridgeStpVersion_Object = MibTableColumn
begemotBridgeStpVersion = _BegemotBridgeStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 15),
    _BegemotBridgeStpVersion_Type()
)
begemotBridgeStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpVersion.setStatus("current")


class _BegemotBridgeStpTxHoldCount_Type(Integer32):
    """Custom type begemotBridgeStpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BegemotBridgeStpTxHoldCount_Type.__name__ = "Integer32"
_BegemotBridgeStpTxHoldCount_Object = MibTableColumn
begemotBridgeStpTxHoldCount = _BegemotBridgeStpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 16),
    _BegemotBridgeStpTxHoldCount_Type()
)
begemotBridgeStpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpTxHoldCount.setStatus("current")
_BegemotBridgeStpPortTable_Object = MibTable
begemotBridgeStpPortTable = _BegemotBridgeStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2)
)
if mibBuilder.loadTexts:
    begemotBridgeStpPortTable.setStatus("current")
_BegemotBridgeStpPortEntry_Object = MibTableRow
begemotBridgeStpPortEntry = _BegemotBridgeStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1)
)
begemotBridgeStpPortEntry.setIndexNames(
    (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"),
    (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBasePortIfIndex"),
)
if mibBuilder.loadTexts:
    begemotBridgeStpPortEntry.setStatus("current")


class _BegemotBridgeStpPort_Type(Integer32):
    """Custom type begemotBridgeStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BegemotBridgeStpPort_Type.__name__ = "Integer32"
_BegemotBridgeStpPort_Object = MibTableColumn
begemotBridgeStpPort = _BegemotBridgeStpPort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 1),
    _BegemotBridgeStpPort_Type()
)
begemotBridgeStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpPort.setStatus("current")


class _BegemotBridgeStpPortPriority_Type(Integer32):
    """Custom type begemotBridgeStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BegemotBridgeStpPortPriority_Type.__name__ = "Integer32"
_BegemotBridgeStpPortPriority_Object = MibTableColumn
begemotBridgeStpPortPriority = _BegemotBridgeStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 2),
    _BegemotBridgeStpPortPriority_Type()
)
begemotBridgeStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpPortPriority.setStatus("current")


class _BegemotBridgeStpPortState_Type(Integer32):
    """Custom type begemotBridgeStpPortState based on Integer32"""
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


_BegemotBridgeStpPortState_Type.__name__ = "Integer32"
_BegemotBridgeStpPortState_Object = MibTableColumn
begemotBridgeStpPortState = _BegemotBridgeStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 3),
    _BegemotBridgeStpPortState_Type()
)
begemotBridgeStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpPortState.setStatus("current")


class _BegemotBridgeStpPortEnable_Type(Integer32):
    """Custom type begemotBridgeStpPortEnable based on Integer32"""
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


_BegemotBridgeStpPortEnable_Type.__name__ = "Integer32"
_BegemotBridgeStpPortEnable_Object = MibTableColumn
begemotBridgeStpPortEnable = _BegemotBridgeStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 4),
    _BegemotBridgeStpPortEnable_Type()
)
begemotBridgeStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpPortEnable.setStatus("current")


class _BegemotBridgeStpPortPathCost_Type(Integer32):
    """Custom type begemotBridgeStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BegemotBridgeStpPortPathCost_Type.__name__ = "Integer32"
_BegemotBridgeStpPortPathCost_Object = MibTableColumn
begemotBridgeStpPortPathCost = _BegemotBridgeStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 5),
    _BegemotBridgeStpPortPathCost_Type()
)
begemotBridgeStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpPortPathCost.setStatus("current")
_BegemotBridgeStpPortDesignatedRoot_Type = BridgeId
_BegemotBridgeStpPortDesignatedRoot_Object = MibTableColumn
begemotBridgeStpPortDesignatedRoot = _BegemotBridgeStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 6),
    _BegemotBridgeStpPortDesignatedRoot_Type()
)
begemotBridgeStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpPortDesignatedRoot.setStatus("current")
_BegemotBridgeStpPortDesignatedCost_Type = Integer32
_BegemotBridgeStpPortDesignatedCost_Object = MibTableColumn
begemotBridgeStpPortDesignatedCost = _BegemotBridgeStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 7),
    _BegemotBridgeStpPortDesignatedCost_Type()
)
begemotBridgeStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpPortDesignatedCost.setStatus("current")
_BegemotBridgeStpPortDesignatedBridge_Type = BridgeId
_BegemotBridgeStpPortDesignatedBridge_Object = MibTableColumn
begemotBridgeStpPortDesignatedBridge = _BegemotBridgeStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 8),
    _BegemotBridgeStpPortDesignatedBridge_Type()
)
begemotBridgeStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpPortDesignatedBridge.setStatus("current")
_BegemotBridgeStpPortDesignatedPort_Type = BridgePortId
_BegemotBridgeStpPortDesignatedPort_Object = MibTableColumn
begemotBridgeStpPortDesignatedPort = _BegemotBridgeStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 9),
    _BegemotBridgeStpPortDesignatedPort_Type()
)
begemotBridgeStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpPortDesignatedPort.setStatus("current")
_BegemotBridgeStpPortForwardTransitions_Type = Counter32
_BegemotBridgeStpPortForwardTransitions_Object = MibTableColumn
begemotBridgeStpPortForwardTransitions = _BegemotBridgeStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 10),
    _BegemotBridgeStpPortForwardTransitions_Type()
)
begemotBridgeStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpPortForwardTransitions.setStatus("current")
_BegemotBridgeStpExtPortTable_Object = MibTable
begemotBridgeStpExtPortTable = _BegemotBridgeStpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3)
)
if mibBuilder.loadTexts:
    begemotBridgeStpExtPortTable.setStatus("current")
_BegemotBridgeStpExtPortEntry_Object = MibTableRow
begemotBridgeStpExtPortEntry = _BegemotBridgeStpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1)
)
if mibBuilder.loadTexts:
    begemotBridgeStpExtPortEntry.setStatus("current")
_BegemotBridgeStpPortProtocolMigration_Type = TruthValue
_BegemotBridgeStpPortProtocolMigration_Object = MibTableColumn
begemotBridgeStpPortProtocolMigration = _BegemotBridgeStpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 1),
    _BegemotBridgeStpPortProtocolMigration_Type()
)
begemotBridgeStpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpPortProtocolMigration.setStatus("current")
_BegemotBridgeStpPortAdminEdgePort_Type = TruthValue
_BegemotBridgeStpPortAdminEdgePort_Object = MibTableColumn
begemotBridgeStpPortAdminEdgePort = _BegemotBridgeStpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 2),
    _BegemotBridgeStpPortAdminEdgePort_Type()
)
begemotBridgeStpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpPortAdminEdgePort.setStatus("current")
_BegemotBridgeStpPortOperEdgePort_Type = TruthValue
_BegemotBridgeStpPortOperEdgePort_Object = MibTableColumn
begemotBridgeStpPortOperEdgePort = _BegemotBridgeStpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 3),
    _BegemotBridgeStpPortOperEdgePort_Type()
)
begemotBridgeStpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpPortOperEdgePort.setStatus("current")


class _BegemotBridgeStpPortAdminPointToPoint_Type(Integer32):
    """Custom type begemotBridgeStpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_BegemotBridgeStpPortAdminPointToPoint_Type.__name__ = "Integer32"
_BegemotBridgeStpPortAdminPointToPoint_Object = MibTableColumn
begemotBridgeStpPortAdminPointToPoint = _BegemotBridgeStpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 4),
    _BegemotBridgeStpPortAdminPointToPoint_Type()
)
begemotBridgeStpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpPortAdminPointToPoint.setStatus("current")
_BegemotBridgeStpPortOperPointToPoint_Type = TruthValue
_BegemotBridgeStpPortOperPointToPoint_Object = MibTableColumn
begemotBridgeStpPortOperPointToPoint = _BegemotBridgeStpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 5),
    _BegemotBridgeStpPortOperPointToPoint_Type()
)
begemotBridgeStpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeStpPortOperPointToPoint.setStatus("current")


class _BegemotBridgeStpPortAdminPathCost_Type(Integer32):
    """Custom type begemotBridgeStpPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_BegemotBridgeStpPortAdminPathCost_Type.__name__ = "Integer32"
_BegemotBridgeStpPortAdminPathCost_Object = MibTableColumn
begemotBridgeStpPortAdminPathCost = _BegemotBridgeStpPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 6),
    _BegemotBridgeStpPortAdminPathCost_Type()
)
begemotBridgeStpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeStpPortAdminPathCost.setStatus("current")
_BegemotBridgeTp_ObjectIdentity = ObjectIdentity
begemotBridgeTp = _BegemotBridgeTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3)
)
_BegemotBridgeTpTable_Object = MibTable
begemotBridgeTpTable = _BegemotBridgeTpTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 1)
)
if mibBuilder.loadTexts:
    begemotBridgeTpTable.setStatus("current")
_BegemotBridgeTpEntry_Object = MibTableRow
begemotBridgeTpEntry = _BegemotBridgeTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 1, 1)
)
if mibBuilder.loadTexts:
    begemotBridgeTpEntry.setStatus("current")
_BegemotBridgeTpLearnedEntryDiscards_Type = Counter32
_BegemotBridgeTpLearnedEntryDiscards_Object = MibTableColumn
begemotBridgeTpLearnedEntryDiscards = _BegemotBridgeTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 1, 1, 1),
    _BegemotBridgeTpLearnedEntryDiscards_Type()
)
begemotBridgeTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeTpLearnedEntryDiscards.setStatus("current")


class _BegemotBridgeTpAgingTime_Type(Integer32):
    """Custom type begemotBridgeTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_BegemotBridgeTpAgingTime_Type.__name__ = "Integer32"
_BegemotBridgeTpAgingTime_Object = MibTableColumn
begemotBridgeTpAgingTime = _BegemotBridgeTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 1, 1, 2),
    _BegemotBridgeTpAgingTime_Type()
)
begemotBridgeTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeTpAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeTpAgingTime.setUnits("seconds")


class _BegemotBridgeTpMaxAddresses_Type(Integer32):
    """Custom type begemotBridgeTpMaxAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_BegemotBridgeTpMaxAddresses_Type.__name__ = "Integer32"
_BegemotBridgeTpMaxAddresses_Object = MibTableColumn
begemotBridgeTpMaxAddresses = _BegemotBridgeTpMaxAddresses_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 1, 1, 3),
    _BegemotBridgeTpMaxAddresses_Type()
)
begemotBridgeTpMaxAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeTpMaxAddresses.setStatus("current")
_BegemotBridgeTpFdbTable_Object = MibTable
begemotBridgeTpFdbTable = _BegemotBridgeTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 2)
)
if mibBuilder.loadTexts:
    begemotBridgeTpFdbTable.setStatus("current")
_BegemotBridgeTpFdbEntry_Object = MibTableRow
begemotBridgeTpFdbEntry = _BegemotBridgeTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 2, 1)
)
begemotBridgeTpFdbEntry.setIndexNames(
    (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"),
    (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeTpFdbAddress"),
)
if mibBuilder.loadTexts:
    begemotBridgeTpFdbEntry.setStatus("current")
_BegemotBridgeTpFdbAddress_Type = MacAddress
_BegemotBridgeTpFdbAddress_Object = MibTableColumn
begemotBridgeTpFdbAddress = _BegemotBridgeTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 2, 1, 1),
    _BegemotBridgeTpFdbAddress_Type()
)
begemotBridgeTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeTpFdbAddress.setStatus("current")
_BegemotBridgeTpFdbPort_Type = Integer32
_BegemotBridgeTpFdbPort_Object = MibTableColumn
begemotBridgeTpFdbPort = _BegemotBridgeTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 2, 1, 2),
    _BegemotBridgeTpFdbPort_Type()
)
begemotBridgeTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeTpFdbPort.setStatus("current")


class _BegemotBridgeTpFdbStatus_Type(Integer32):
    """Custom type begemotBridgeTpFdbStatus based on Integer32"""
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


_BegemotBridgeTpFdbStatus_Type.__name__ = "Integer32"
_BegemotBridgeTpFdbStatus_Object = MibTableColumn
begemotBridgeTpFdbStatus = _BegemotBridgeTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 2, 1, 3),
    _BegemotBridgeTpFdbStatus_Type()
)
begemotBridgeTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeTpFdbStatus.setStatus("current")
_BegemotBridgeTpPortTable_Object = MibTable
begemotBridgeTpPortTable = _BegemotBridgeTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3)
)
if mibBuilder.loadTexts:
    begemotBridgeTpPortTable.setStatus("current")
_BegemotBridgeTpPortEntry_Object = MibTableRow
begemotBridgeTpPortEntry = _BegemotBridgeTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1)
)
begemotBridgeTpPortEntry.setIndexNames(
    (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"),
    (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBasePortIfIndex"),
)
if mibBuilder.loadTexts:
    begemotBridgeTpPortEntry.setStatus("current")


class _BegemotBridgeTpPort_Type(Integer32):
    """Custom type begemotBridgeTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BegemotBridgeTpPort_Type.__name__ = "Integer32"
_BegemotBridgeTpPort_Object = MibTableColumn
begemotBridgeTpPort = _BegemotBridgeTpPort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1, 1),
    _BegemotBridgeTpPort_Type()
)
begemotBridgeTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeTpPort.setStatus("current")
_BegemotBridgeTpPortMaxInfo_Type = Integer32
_BegemotBridgeTpPortMaxInfo_Object = MibTableColumn
begemotBridgeTpPortMaxInfo = _BegemotBridgeTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1, 2),
    _BegemotBridgeTpPortMaxInfo_Type()
)
begemotBridgeTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeTpPortMaxInfo.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeTpPortMaxInfo.setUnits("bytes")
_BegemotBridgeTpPortInFrames_Type = Counter32
_BegemotBridgeTpPortInFrames_Object = MibTableColumn
begemotBridgeTpPortInFrames = _BegemotBridgeTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1, 3),
    _BegemotBridgeTpPortInFrames_Type()
)
begemotBridgeTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeTpPortInFrames.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeTpPortInFrames.setUnits("frames")
_BegemotBridgeTpPortOutFrames_Type = Counter32
_BegemotBridgeTpPortOutFrames_Object = MibTableColumn
begemotBridgeTpPortOutFrames = _BegemotBridgeTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1, 4),
    _BegemotBridgeTpPortOutFrames_Type()
)
begemotBridgeTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeTpPortOutFrames.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeTpPortOutFrames.setUnits("frames")
_BegemotBridgeTpPortInDiscards_Type = Counter32
_BegemotBridgeTpPortInDiscards_Object = MibTableColumn
begemotBridgeTpPortInDiscards = _BegemotBridgeTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1, 5),
    _BegemotBridgeTpPortInDiscards_Type()
)
begemotBridgeTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotBridgeTpPortInDiscards.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeTpPortInDiscards.setUnits("frames")
_BegemotBridgePf_ObjectIdentity = ObjectIdentity
begemotBridgePf = _BegemotBridgePf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 4)
)
_BegemotBridgePfilStatus_Type = TruthValue
_BegemotBridgePfilStatus_Object = MibScalar
begemotBridgePfilStatus = _BegemotBridgePfilStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 4, 1),
    _BegemotBridgePfilStatus_Type()
)
begemotBridgePfilStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgePfilStatus.setStatus("current")
_BegemotBridgePfilMembers_Type = TruthValue
_BegemotBridgePfilMembers_Object = MibScalar
begemotBridgePfilMembers = _BegemotBridgePfilMembers_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 4, 2),
    _BegemotBridgePfilMembers_Type()
)
begemotBridgePfilMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgePfilMembers.setStatus("current")
_BegemotBridgePfilIpOnly_Type = TruthValue
_BegemotBridgePfilIpOnly_Object = MibScalar
begemotBridgePfilIpOnly = _BegemotBridgePfilIpOnly_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 4, 3),
    _BegemotBridgePfilIpOnly_Type()
)
begemotBridgePfilIpOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgePfilIpOnly.setStatus("current")


class _BegemotBridgeLayer2PfStatus_Type(Integer32):
    """Custom type begemotBridgeLayer2PfStatus based on Integer32"""
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


_BegemotBridgeLayer2PfStatus_Type.__name__ = "Integer32"
_BegemotBridgeLayer2PfStatus_Object = MibScalar
begemotBridgeLayer2PfStatus = _BegemotBridgeLayer2PfStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 4, 4),
    _BegemotBridgeLayer2PfStatus_Type()
)
begemotBridgeLayer2PfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeLayer2PfStatus.setStatus("current")
_BegemotBridgeConfigObjects_ObjectIdentity = ObjectIdentity
begemotBridgeConfigObjects = _BegemotBridgeConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 5)
)


class _BegemotBridgeDefaultBridgeIf_Type(BridgeIfNameOrEmpty):
    """Custom type begemotBridgeDefaultBridgeIf based on BridgeIfNameOrEmpty"""
    defaultValue = OctetString("bridge0")


_BegemotBridgeDefaultBridgeIf_Object = MibScalar
begemotBridgeDefaultBridgeIf = _BegemotBridgeDefaultBridgeIf_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 5, 1),
    _BegemotBridgeDefaultBridgeIf_Type()
)
begemotBridgeDefaultBridgeIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeDefaultBridgeIf.setStatus("current")


class _BegemotBridgeDataUpdate_Type(Timeout):
    """Custom type begemotBridgeDataUpdate based on Timeout"""
    defaultValue = 10

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_BegemotBridgeDataUpdate_Type.__name__ = "Timeout"
_BegemotBridgeDataUpdate_Object = MibScalar
begemotBridgeDataUpdate = _BegemotBridgeDataUpdate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 5, 2),
    _BegemotBridgeDataUpdate_Type()
)
begemotBridgeDataUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeDataUpdate.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeDataUpdate.setUnits("seconds")


class _BegemotBridgeDataPoll_Type(Timeout):
    """Custom type begemotBridgeDataPoll based on Timeout"""
    defaultValue = 300

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_BegemotBridgeDataPoll_Type.__name__ = "Timeout"
_BegemotBridgeDataPoll_Object = MibScalar
begemotBridgeDataPoll = _BegemotBridgeDataPoll_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 5, 3),
    _BegemotBridgeDataPoll_Type()
)
begemotBridgeDataPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotBridgeDataPoll.setStatus("current")
if mibBuilder.loadTexts:
    begemotBridgeDataPoll.setUnits("seconds")
begemotBridgeBaseEntry.registerAugmentions(
    ("BEGEMOT-BRIDGE-MIB",
     "begemotBridgeStpEntry")
)
begemotBridgeStpEntry.setIndexNames(*begemotBridgeBaseEntry.getIndexNames())
begemotBridgeStpPortEntry.registerAugmentions(
    ("BEGEMOT-BRIDGE-MIB",
     "begemotBridgeStpExtPortEntry")
)
begemotBridgeStpExtPortEntry.setIndexNames(*begemotBridgeStpPortEntry.getIndexNames())
begemotBridgeBaseEntry.registerAugmentions(
    ("BEGEMOT-BRIDGE-MIB",
     "begemotBridgeTpEntry")
)
begemotBridgeTpEntry.setIndexNames(*begemotBridgeBaseEntry.getIndexNames())

# Managed Objects groups


# Notification objects

begemotBridgeNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 0, 1)
)
begemotBridgeNewRoot.setObjects(
    ("BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName")
)
if mibBuilder.loadTexts:
    begemotBridgeNewRoot.setStatus(
        "current"
    )

begemotBridgeTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12325, 1, 205, 0, 2)
)
begemotBridgeTopologyChange.setObjects(
    ("BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName")
)
if mibBuilder.loadTexts:
    begemotBridgeTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-BRIDGE-MIB",
    **{"BridgeIfName": BridgeIfName,
       "BridgeIfNameOrEmpty": BridgeIfNameOrEmpty,
       "BridgePortId": BridgePortId,
       "begemotBridge": begemotBridge,
       "begemotBridgeNotifications": begemotBridgeNotifications,
       "begemotBridgeNewRoot": begemotBridgeNewRoot,
       "begemotBridgeTopologyChange": begemotBridgeTopologyChange,
       "begemotBridgeBase": begemotBridgeBase,
       "begemotBridgeBaseTable": begemotBridgeBaseTable,
       "begemotBridgeBaseEntry": begemotBridgeBaseEntry,
       "begemotBridgeBaseName": begemotBridgeBaseName,
       "begemotBridgeBaseAddress": begemotBridgeBaseAddress,
       "begemotBridgeBaseNumPorts": begemotBridgeBaseNumPorts,
       "begemotBridgeBaseType": begemotBridgeBaseType,
       "begemotBridgeBaseStatus": begemotBridgeBaseStatus,
       "begemotBridgeBasePortTable": begemotBridgeBasePortTable,
       "begemotBridgeBasePortEntry": begemotBridgeBasePortEntry,
       "begemotBridgeBasePort": begemotBridgeBasePort,
       "begemotBridgeBasePortIfIndex": begemotBridgeBasePortIfIndex,
       "begemotBridgeBaseSpanEnabled": begemotBridgeBaseSpanEnabled,
       "begemotBridgeBasePortDelayExceededDiscards": begemotBridgeBasePortDelayExceededDiscards,
       "begemotBridgeBasePortMtuExceededDiscards": begemotBridgeBasePortMtuExceededDiscards,
       "begemotBridgeBasePortStatus": begemotBridgeBasePortStatus,
       "begemotBridgeBasePortPrivate": begemotBridgeBasePortPrivate,
       "begemotBridgeStp": begemotBridgeStp,
       "begemotBridgeStpTable": begemotBridgeStpTable,
       "begemotBridgeStpEntry": begemotBridgeStpEntry,
       "begemotBridgeStpProtocolSpecification": begemotBridgeStpProtocolSpecification,
       "begemotBridgeStpPriority": begemotBridgeStpPriority,
       "begemotBridgeStpTimeSinceTopologyChange": begemotBridgeStpTimeSinceTopologyChange,
       "begemotBridgeStpTopChanges": begemotBridgeStpTopChanges,
       "begemotBridgeStpDesignatedRoot": begemotBridgeStpDesignatedRoot,
       "begemotBridgeStpRootCost": begemotBridgeStpRootCost,
       "begemotBridgeStpRootPort": begemotBridgeStpRootPort,
       "begemotBridgeStpMaxAge": begemotBridgeStpMaxAge,
       "begemotBridgeStpHelloTime": begemotBridgeStpHelloTime,
       "begemotBridgeStpHoldTime": begemotBridgeStpHoldTime,
       "begemotBridgeStpForwardDelay": begemotBridgeStpForwardDelay,
       "begemotBridgeStpBridgeMaxAge": begemotBridgeStpBridgeMaxAge,
       "begemotBridgeStpBridgeHelloTime": begemotBridgeStpBridgeHelloTime,
       "begemotBridgeStpBridgeForwardDelay": begemotBridgeStpBridgeForwardDelay,
       "begemotBridgeStpVersion": begemotBridgeStpVersion,
       "begemotBridgeStpTxHoldCount": begemotBridgeStpTxHoldCount,
       "begemotBridgeStpPortTable": begemotBridgeStpPortTable,
       "begemotBridgeStpPortEntry": begemotBridgeStpPortEntry,
       "begemotBridgeStpPort": begemotBridgeStpPort,
       "begemotBridgeStpPortPriority": begemotBridgeStpPortPriority,
       "begemotBridgeStpPortState": begemotBridgeStpPortState,
       "begemotBridgeStpPortEnable": begemotBridgeStpPortEnable,
       "begemotBridgeStpPortPathCost": begemotBridgeStpPortPathCost,
       "begemotBridgeStpPortDesignatedRoot": begemotBridgeStpPortDesignatedRoot,
       "begemotBridgeStpPortDesignatedCost": begemotBridgeStpPortDesignatedCost,
       "begemotBridgeStpPortDesignatedBridge": begemotBridgeStpPortDesignatedBridge,
       "begemotBridgeStpPortDesignatedPort": begemotBridgeStpPortDesignatedPort,
       "begemotBridgeStpPortForwardTransitions": begemotBridgeStpPortForwardTransitions,
       "begemotBridgeStpExtPortTable": begemotBridgeStpExtPortTable,
       "begemotBridgeStpExtPortEntry": begemotBridgeStpExtPortEntry,
       "begemotBridgeStpPortProtocolMigration": begemotBridgeStpPortProtocolMigration,
       "begemotBridgeStpPortAdminEdgePort": begemotBridgeStpPortAdminEdgePort,
       "begemotBridgeStpPortOperEdgePort": begemotBridgeStpPortOperEdgePort,
       "begemotBridgeStpPortAdminPointToPoint": begemotBridgeStpPortAdminPointToPoint,
       "begemotBridgeStpPortOperPointToPoint": begemotBridgeStpPortOperPointToPoint,
       "begemotBridgeStpPortAdminPathCost": begemotBridgeStpPortAdminPathCost,
       "begemotBridgeTp": begemotBridgeTp,
       "begemotBridgeTpTable": begemotBridgeTpTable,
       "begemotBridgeTpEntry": begemotBridgeTpEntry,
       "begemotBridgeTpLearnedEntryDiscards": begemotBridgeTpLearnedEntryDiscards,
       "begemotBridgeTpAgingTime": begemotBridgeTpAgingTime,
       "begemotBridgeTpMaxAddresses": begemotBridgeTpMaxAddresses,
       "begemotBridgeTpFdbTable": begemotBridgeTpFdbTable,
       "begemotBridgeTpFdbEntry": begemotBridgeTpFdbEntry,
       "begemotBridgeTpFdbAddress": begemotBridgeTpFdbAddress,
       "begemotBridgeTpFdbPort": begemotBridgeTpFdbPort,
       "begemotBridgeTpFdbStatus": begemotBridgeTpFdbStatus,
       "begemotBridgeTpPortTable": begemotBridgeTpPortTable,
       "begemotBridgeTpPortEntry": begemotBridgeTpPortEntry,
       "begemotBridgeTpPort": begemotBridgeTpPort,
       "begemotBridgeTpPortMaxInfo": begemotBridgeTpPortMaxInfo,
       "begemotBridgeTpPortInFrames": begemotBridgeTpPortInFrames,
       "begemotBridgeTpPortOutFrames": begemotBridgeTpPortOutFrames,
       "begemotBridgeTpPortInDiscards": begemotBridgeTpPortInDiscards,
       "begemotBridgePf": begemotBridgePf,
       "begemotBridgePfilStatus": begemotBridgePfilStatus,
       "begemotBridgePfilMembers": begemotBridgePfilMembers,
       "begemotBridgePfilIpOnly": begemotBridgePfilIpOnly,
       "begemotBridgeLayer2PfStatus": begemotBridgeLayer2PfStatus,
       "begemotBridgeConfigObjects": begemotBridgeConfigObjects,
       "begemotBridgeDefaultBridgeIf": begemotBridgeDefaultBridgeIf,
       "begemotBridgeDataUpdate": begemotBridgeDataUpdate,
       "begemotBridgeDataPoll": begemotBridgeDataPoll}
)
