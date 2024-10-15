# SNMP MIB module (ITOUCH-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:06 2024
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

(MacAddress,
 dot1dTpFdbAddress) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress",
    "dot1dTpFdbAddress")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(iTouch,) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "iTouch")

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

_BridgeDep_ObjectIdentity = ObjectIdentity
bridgeDep = _BridgeDep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 5)
)
_XBridge_ObjectIdentity = ObjectIdentity
xBridge = _XBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 19)
)
_XBridgeSystem_ObjectIdentity = ObjectIdentity
xBridgeSystem = _XBridgeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 19, 1)
)


class _BridgeState_Type(Integer32):
    """Custom type bridgeState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BridgeState_Type.__name__ = "Integer32"
_BridgeState_Object = MibScalar
bridgeState = _BridgeState_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 1, 1),
    _BridgeState_Type()
)
bridgeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeState.setStatus("mandatory")


class _BridgeEarlyLoopState_Type(Integer32):
    """Custom type bridgeEarlyLoopState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BridgeEarlyLoopState_Type.__name__ = "Integer32"
_BridgeEarlyLoopState_Object = MibScalar
bridgeEarlyLoopState = _BridgeEarlyLoopState_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 1, 2),
    _BridgeEarlyLoopState_Type()
)
bridgeEarlyLoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEarlyLoopState.setStatus("mandatory")
_BridgeEarlyLoopCount_Type = Counter32
_BridgeEarlyLoopCount_Object = MibScalar
bridgeEarlyLoopCount = _BridgeEarlyLoopCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 1, 3),
    _BridgeEarlyLoopCount_Type()
)
bridgeEarlyLoopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEarlyLoopCount.setStatus("mandatory")
_BridgeEarlyLoopAddress_Type = MacAddress
_BridgeEarlyLoopAddress_Object = MibScalar
bridgeEarlyLoopAddress = _BridgeEarlyLoopAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 1, 4),
    _BridgeEarlyLoopAddress_Type()
)
bridgeEarlyLoopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEarlyLoopAddress.setStatus("mandatory")


class _BridgeSpanningTreeState_Type(Integer32):
    """Custom type bridgeSpanningTreeState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BridgeSpanningTreeState_Type.__name__ = "Integer32"
_BridgeSpanningTreeState_Object = MibScalar
bridgeSpanningTreeState = _BridgeSpanningTreeState_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 1, 5),
    _BridgeSpanningTreeState_Type()
)
bridgeSpanningTreeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeSpanningTreeState.setStatus("mandatory")


class _BridgeFilterDiscardTimeout_Type(Integer32):
    """Custom type bridgeFilterDiscardTimeout based on Integer32"""
    defaultValue = 43200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgeFilterDiscardTimeout_Type.__name__ = "Integer32"
_BridgeFilterDiscardTimeout_Object = MibScalar
bridgeFilterDiscardTimeout = _BridgeFilterDiscardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 1, 6),
    _BridgeFilterDiscardTimeout_Type()
)
bridgeFilterDiscardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeFilterDiscardTimeout.setStatus("mandatory")


class _BridgeTopologyState_Type(Integer32):
    """Custom type bridgeTopologyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changing", 2),
          ("stable", 1))
    )


_BridgeTopologyState_Type.__name__ = "Integer32"
_BridgeTopologyState_Object = MibScalar
bridgeTopologyState = _BridgeTopologyState_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 1, 7),
    _BridgeTopologyState_Type()
)
bridgeTopologyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTopologyState.setStatus("mandatory")
_BridgeTopologyChangeAddr_Type = MacAddress
_BridgeTopologyChangeAddr_Object = MibScalar
bridgeTopologyChangeAddr = _BridgeTopologyChangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 1, 8),
    _BridgeTopologyChangeAddr_Type()
)
bridgeTopologyChangeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTopologyChangeAddr.setStatus("mandatory")
_XBridgeProtocol_ObjectIdentity = ObjectIdentity
xBridgeProtocol = _XBridgeProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 19, 3)
)


class _BridgeProtocolFilterState_Type(Integer32):
    """Custom type bridgeProtocolFilterState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BridgeProtocolFilterState_Type.__name__ = "Integer32"
_BridgeProtocolFilterState_Object = MibScalar
bridgeProtocolFilterState = _BridgeProtocolFilterState_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 3, 1),
    _BridgeProtocolFilterState_Type()
)
bridgeProtocolFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeProtocolFilterState.setStatus("mandatory")


class _BridgeProtocolDefaultPriority_Type(Integer32):
    """Custom type bridgeProtocolDefaultPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              101)
        )
    )
    namedValues = NamedValues(
        *(("discard", 101),
          ("high", 5),
          ("low", 1),
          ("medium", 3))
    )


_BridgeProtocolDefaultPriority_Type.__name__ = "Integer32"
_BridgeProtocolDefaultPriority_Object = MibScalar
bridgeProtocolDefaultPriority = _BridgeProtocolDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 3, 2),
    _BridgeProtocolDefaultPriority_Type()
)
bridgeProtocolDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeProtocolDefaultPriority.setStatus("mandatory")
_BridgeProtocolTable_Object = MibTable
bridgeProtocolTable = _BridgeProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 3, 3)
)
if mibBuilder.loadTexts:
    bridgeProtocolTable.setStatus("mandatory")
_BridgeProtocolEntry_Object = MibTableRow
bridgeProtocolEntry = _BridgeProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 3, 3, 1)
)
bridgeProtocolEntry.setIndexNames(
    (0, "ITOUCH-BRIDGE-MIB", "bridgeProtocolProtocol"),
)
if mibBuilder.loadTexts:
    bridgeProtocolEntry.setStatus("mandatory")


class _BridgeProtocolProtocol_Type(OctetString):
    """Custom type bridgeProtocolProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BridgeProtocolProtocol_Type.__name__ = "OctetString"
_BridgeProtocolProtocol_Object = MibTableColumn
bridgeProtocolProtocol = _BridgeProtocolProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 3, 3, 1, 1),
    _BridgeProtocolProtocol_Type()
)
bridgeProtocolProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeProtocolProtocol.setStatus("mandatory")


class _BridgeProtocolName_Type(DisplayString):
    """Custom type bridgeProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_BridgeProtocolName_Type.__name__ = "DisplayString"
_BridgeProtocolName_Object = MibTableColumn
bridgeProtocolName = _BridgeProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 3, 3, 1, 2),
    _BridgeProtocolName_Type()
)
bridgeProtocolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeProtocolName.setStatus("mandatory")


class _BridgeProtocolPriority_Type(Integer32):
    """Custom type bridgeProtocolPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              101)
        )
    )
    namedValues = NamedValues(
        *(("discard", 101),
          ("high", 5),
          ("low", 1),
          ("medium", 3))
    )


_BridgeProtocolPriority_Type.__name__ = "Integer32"
_BridgeProtocolPriority_Object = MibTableColumn
bridgeProtocolPriority = _BridgeProtocolPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 3, 3, 1, 3),
    _BridgeProtocolPriority_Type()
)
bridgeProtocolPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeProtocolPriority.setStatus("mandatory")
_BridgeProtocolUses_Type = Counter32
_BridgeProtocolUses_Object = MibTableColumn
bridgeProtocolUses = _BridgeProtocolUses_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 3, 3, 1, 4),
    _BridgeProtocolUses_Type()
)
bridgeProtocolUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeProtocolUses.setStatus("mandatory")


class _BridgeProtocolStatus_Type(Integer32):
    """Custom type bridgeProtocolStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_BridgeProtocolStatus_Type.__name__ = "Integer32"
_BridgeProtocolStatus_Object = MibTableColumn
bridgeProtocolStatus = _BridgeProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 3, 3, 1, 5),
    _BridgeProtocolStatus_Type()
)
bridgeProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeProtocolStatus.setStatus("mandatory")
_XBridgeFilter_ObjectIdentity = ObjectIdentity
xBridgeFilter = _XBridgeFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 19, 4)
)
_BridgeFilterTable_Object = MibTable
bridgeFilterTable = _BridgeFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 4, 1)
)
if mibBuilder.loadTexts:
    bridgeFilterTable.setStatus("mandatory")
_BridgeFilterEntry_Object = MibTableRow
bridgeFilterEntry = _BridgeFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 4, 1, 1)
)
bridgeFilterEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dTpFdbAddress"),
)
if mibBuilder.loadTexts:
    bridgeFilterEntry.setStatus("mandatory")


class _BridgeFilterForwardSubPort_Type(Integer32):
    """Custom type bridgeFilterForwardSubPort based on Integer32"""
    defaultValue = 0


_BridgeFilterForwardSubPort_Object = MibTableColumn
bridgeFilterForwardSubPort = _BridgeFilterForwardSubPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 4, 1, 1, 1),
    _BridgeFilterForwardSubPort_Type()
)
bridgeFilterForwardSubPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeFilterForwardSubPort.setStatus("mandatory")
_BridgeFilterUses_Type = Counter32
_BridgeFilterUses_Object = MibTableColumn
bridgeFilterUses = _BridgeFilterUses_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 4, 1, 1, 2),
    _BridgeFilterUses_Type()
)
bridgeFilterUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeFilterUses.setStatus("mandatory")
_BridgeFilterAge_Type = Integer32
_BridgeFilterAge_Object = MibTableColumn
bridgeFilterAge = _BridgeFilterAge_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 4, 1, 1, 3),
    _BridgeFilterAge_Type()
)
bridgeFilterAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeFilterAge.setStatus("mandatory")
_BridgeFilterLinkTable_Object = MibTable
bridgeFilterLinkTable = _BridgeFilterLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 4, 2)
)
if mibBuilder.loadTexts:
    bridgeFilterLinkTable.setStatus("mandatory")
_BridgeFilterLinkEntry_Object = MibTableRow
bridgeFilterLinkEntry = _BridgeFilterLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 4, 2, 1)
)
bridgeFilterLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bridgeFilterLinkEntry.setStatus("mandatory")
_BridgeFilterLinkOverflowCam_Type = Integer32
_BridgeFilterLinkOverflowCam_Object = MibTableColumn
bridgeFilterLinkOverflowCam = _BridgeFilterLinkOverflowCam_Object(
    (1, 3, 6, 1, 4, 1, 33, 19, 4, 2, 1, 1),
    _BridgeFilterLinkOverflowCam_Type()
)
bridgeFilterLinkOverflowCam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeFilterLinkOverflowCam.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-BRIDGE-MIB",
    **{"bridgeDep": bridgeDep,
       "xBridge": xBridge,
       "xBridgeSystem": xBridgeSystem,
       "bridgeState": bridgeState,
       "bridgeEarlyLoopState": bridgeEarlyLoopState,
       "bridgeEarlyLoopCount": bridgeEarlyLoopCount,
       "bridgeEarlyLoopAddress": bridgeEarlyLoopAddress,
       "bridgeSpanningTreeState": bridgeSpanningTreeState,
       "bridgeFilterDiscardTimeout": bridgeFilterDiscardTimeout,
       "bridgeTopologyState": bridgeTopologyState,
       "bridgeTopologyChangeAddr": bridgeTopologyChangeAddr,
       "xBridgeProtocol": xBridgeProtocol,
       "bridgeProtocolFilterState": bridgeProtocolFilterState,
       "bridgeProtocolDefaultPriority": bridgeProtocolDefaultPriority,
       "bridgeProtocolTable": bridgeProtocolTable,
       "bridgeProtocolEntry": bridgeProtocolEntry,
       "bridgeProtocolProtocol": bridgeProtocolProtocol,
       "bridgeProtocolName": bridgeProtocolName,
       "bridgeProtocolPriority": bridgeProtocolPriority,
       "bridgeProtocolUses": bridgeProtocolUses,
       "bridgeProtocolStatus": bridgeProtocolStatus,
       "xBridgeFilter": xBridgeFilter,
       "bridgeFilterTable": bridgeFilterTable,
       "bridgeFilterEntry": bridgeFilterEntry,
       "bridgeFilterForwardSubPort": bridgeFilterForwardSubPort,
       "bridgeFilterUses": bridgeFilterUses,
       "bridgeFilterAge": bridgeFilterAge,
       "bridgeFilterLinkTable": bridgeFilterLinkTable,
       "bridgeFilterLinkEntry": bridgeFilterLinkEntry,
       "bridgeFilterLinkOverflowCam": bridgeFilterLinkOverflowCam}
)
