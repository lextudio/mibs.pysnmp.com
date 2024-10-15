# SNMP MIB module (RFC1382-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1382-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:34 2024
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

(PositiveInteger,) = mibBuilder.importSymbols(
    "RFC1253-MIB",
    "PositiveInteger")

(EntryStatus,) = mibBuilder.importSymbols(
    "RFC1271-MIB",
    "EntryStatus")

(IfIndexType,) = mibBuilder.importSymbols(
    "RFC1381-MIB",
    "IfIndexType")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class X121Address(OctetString):
    """Custom type X121Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_X25_ObjectIdentity = ObjectIdentity
x25 = _X25_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 5)
)
_X25AdmnTable_Object = MibTable
x25AdmnTable = _X25AdmnTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1)
)
if mibBuilder.loadTexts:
    x25AdmnTable.setStatus("mandatory")
_X25AdmnEntry_Object = MibTableRow
x25AdmnEntry = _X25AdmnEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1)
)
x25AdmnEntry.setIndexNames(
    (0, "RFC1382-MIB", "x25AdmnIndex"),
)
if mibBuilder.loadTexts:
    x25AdmnEntry.setStatus("mandatory")
_X25AdmnIndex_Type = IfIndexType
_X25AdmnIndex_Object = MibTableColumn
x25AdmnIndex = _X25AdmnIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 1),
    _X25AdmnIndex_Type()
)
x25AdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25AdmnIndex.setStatus("mandatory")


class _X25AdmnInterfaceMode_Type(Integer32):
    """Custom type x25AdmnInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1),
          ("dxe", 3))
    )


_X25AdmnInterfaceMode_Type.__name__ = "Integer32"
_X25AdmnInterfaceMode_Object = MibTableColumn
x25AdmnInterfaceMode = _X25AdmnInterfaceMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 2),
    _X25AdmnInterfaceMode_Type()
)
x25AdmnInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnInterfaceMode.setStatus("mandatory")


class _X25AdmnMaxActiveCircuits_Type(Integer32):
    """Custom type x25AdmnMaxActiveCircuits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_X25AdmnMaxActiveCircuits_Type.__name__ = "Integer32"
_X25AdmnMaxActiveCircuits_Object = MibTableColumn
x25AdmnMaxActiveCircuits = _X25AdmnMaxActiveCircuits_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 3),
    _X25AdmnMaxActiveCircuits_Type()
)
x25AdmnMaxActiveCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnMaxActiveCircuits.setStatus("mandatory")


class _X25AdmnPacketSequencing_Type(Integer32):
    """Custom type x25AdmnPacketSequencing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_X25AdmnPacketSequencing_Type.__name__ = "Integer32"
_X25AdmnPacketSequencing_Object = MibTableColumn
x25AdmnPacketSequencing = _X25AdmnPacketSequencing_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 4),
    _X25AdmnPacketSequencing_Type()
)
x25AdmnPacketSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnPacketSequencing.setStatus("mandatory")
_X25AdmnRestartTimer_Type = PositiveInteger
_X25AdmnRestartTimer_Object = MibTableColumn
x25AdmnRestartTimer = _X25AdmnRestartTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 5),
    _X25AdmnRestartTimer_Type()
)
x25AdmnRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRestartTimer.setStatus("mandatory")
_X25AdmnCallTimer_Type = PositiveInteger
_X25AdmnCallTimer_Object = MibTableColumn
x25AdmnCallTimer = _X25AdmnCallTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 6),
    _X25AdmnCallTimer_Type()
)
x25AdmnCallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnCallTimer.setStatus("mandatory")
_X25AdmnResetTimer_Type = PositiveInteger
_X25AdmnResetTimer_Object = MibTableColumn
x25AdmnResetTimer = _X25AdmnResetTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 7),
    _X25AdmnResetTimer_Type()
)
x25AdmnResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnResetTimer.setStatus("mandatory")
_X25AdmnClearTimer_Type = PositiveInteger
_X25AdmnClearTimer_Object = MibTableColumn
x25AdmnClearTimer = _X25AdmnClearTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 8),
    _X25AdmnClearTimer_Type()
)
x25AdmnClearTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnClearTimer.setStatus("mandatory")
_X25AdmnWindowTimer_Type = PositiveInteger
_X25AdmnWindowTimer_Object = MibTableColumn
x25AdmnWindowTimer = _X25AdmnWindowTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 9),
    _X25AdmnWindowTimer_Type()
)
x25AdmnWindowTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnWindowTimer.setStatus("mandatory")
_X25AdmnDataRxmtTimer_Type = PositiveInteger
_X25AdmnDataRxmtTimer_Object = MibTableColumn
x25AdmnDataRxmtTimer = _X25AdmnDataRxmtTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 10),
    _X25AdmnDataRxmtTimer_Type()
)
x25AdmnDataRxmtTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnDataRxmtTimer.setStatus("mandatory")
_X25AdmnInterruptTimer_Type = PositiveInteger
_X25AdmnInterruptTimer_Object = MibTableColumn
x25AdmnInterruptTimer = _X25AdmnInterruptTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 11),
    _X25AdmnInterruptTimer_Type()
)
x25AdmnInterruptTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnInterruptTimer.setStatus("mandatory")
_X25AdmnRejectTimer_Type = PositiveInteger
_X25AdmnRejectTimer_Object = MibTableColumn
x25AdmnRejectTimer = _X25AdmnRejectTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 12),
    _X25AdmnRejectTimer_Type()
)
x25AdmnRejectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRejectTimer.setStatus("mandatory")
_X25AdmnRegistrationRequestTimer_Type = PositiveInteger
_X25AdmnRegistrationRequestTimer_Object = MibTableColumn
x25AdmnRegistrationRequestTimer = _X25AdmnRegistrationRequestTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 13),
    _X25AdmnRegistrationRequestTimer_Type()
)
x25AdmnRegistrationRequestTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRegistrationRequestTimer.setStatus("mandatory")
_X25AdmnMinimumRecallTimer_Type = PositiveInteger
_X25AdmnMinimumRecallTimer_Object = MibTableColumn
x25AdmnMinimumRecallTimer = _X25AdmnMinimumRecallTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 14),
    _X25AdmnMinimumRecallTimer_Type()
)
x25AdmnMinimumRecallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnMinimumRecallTimer.setStatus("mandatory")


class _X25AdmnRestartCount_Type(Integer32):
    """Custom type x25AdmnRestartCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25AdmnRestartCount_Type.__name__ = "Integer32"
_X25AdmnRestartCount_Object = MibTableColumn
x25AdmnRestartCount = _X25AdmnRestartCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 15),
    _X25AdmnRestartCount_Type()
)
x25AdmnRestartCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRestartCount.setStatus("mandatory")


class _X25AdmnResetCount_Type(Integer32):
    """Custom type x25AdmnResetCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25AdmnResetCount_Type.__name__ = "Integer32"
_X25AdmnResetCount_Object = MibTableColumn
x25AdmnResetCount = _X25AdmnResetCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 16),
    _X25AdmnResetCount_Type()
)
x25AdmnResetCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnResetCount.setStatus("mandatory")


class _X25AdmnClearCount_Type(Integer32):
    """Custom type x25AdmnClearCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25AdmnClearCount_Type.__name__ = "Integer32"
_X25AdmnClearCount_Object = MibTableColumn
x25AdmnClearCount = _X25AdmnClearCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 17),
    _X25AdmnClearCount_Type()
)
x25AdmnClearCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnClearCount.setStatus("mandatory")


class _X25AdmnDataRxmtCount_Type(Integer32):
    """Custom type x25AdmnDataRxmtCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25AdmnDataRxmtCount_Type.__name__ = "Integer32"
_X25AdmnDataRxmtCount_Object = MibTableColumn
x25AdmnDataRxmtCount = _X25AdmnDataRxmtCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 18),
    _X25AdmnDataRxmtCount_Type()
)
x25AdmnDataRxmtCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnDataRxmtCount.setStatus("mandatory")


class _X25AdmnRejectCount_Type(Integer32):
    """Custom type x25AdmnRejectCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25AdmnRejectCount_Type.__name__ = "Integer32"
_X25AdmnRejectCount_Object = MibTableColumn
x25AdmnRejectCount = _X25AdmnRejectCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 19),
    _X25AdmnRejectCount_Type()
)
x25AdmnRejectCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRejectCount.setStatus("mandatory")


class _X25AdmnRegistrationRequestCount_Type(Integer32):
    """Custom type x25AdmnRegistrationRequestCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25AdmnRegistrationRequestCount_Type.__name__ = "Integer32"
_X25AdmnRegistrationRequestCount_Object = MibTableColumn
x25AdmnRegistrationRequestCount = _X25AdmnRegistrationRequestCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 20),
    _X25AdmnRegistrationRequestCount_Type()
)
x25AdmnRegistrationRequestCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRegistrationRequestCount.setStatus("mandatory")


class _X25AdmnNumberPVCs_Type(Integer32):
    """Custom type x25AdmnNumberPVCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_X25AdmnNumberPVCs_Type.__name__ = "Integer32"
_X25AdmnNumberPVCs_Object = MibTableColumn
x25AdmnNumberPVCs = _X25AdmnNumberPVCs_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 21),
    _X25AdmnNumberPVCs_Type()
)
x25AdmnNumberPVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnNumberPVCs.setStatus("mandatory")
_X25AdmnDefCallParamId_Type = ObjectIdentifier
_X25AdmnDefCallParamId_Object = MibTableColumn
x25AdmnDefCallParamId = _X25AdmnDefCallParamId_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 22),
    _X25AdmnDefCallParamId_Type()
)
x25AdmnDefCallParamId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnDefCallParamId.setStatus("mandatory")
_X25AdmnLocalAddress_Type = X121Address
_X25AdmnLocalAddress_Object = MibTableColumn
x25AdmnLocalAddress = _X25AdmnLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 23),
    _X25AdmnLocalAddress_Type()
)
x25AdmnLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnLocalAddress.setStatus("mandatory")
_X25AdmnProtocolVersionSupported_Type = ObjectIdentifier
_X25AdmnProtocolVersionSupported_Object = MibTableColumn
x25AdmnProtocolVersionSupported = _X25AdmnProtocolVersionSupported_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 24),
    _X25AdmnProtocolVersionSupported_Type()
)
x25AdmnProtocolVersionSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnProtocolVersionSupported.setStatus("mandatory")
_X25OperTable_Object = MibTable
x25OperTable = _X25OperTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2)
)
if mibBuilder.loadTexts:
    x25OperTable.setStatus("mandatory")
_X25OperEntry_Object = MibTableRow
x25OperEntry = _X25OperEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1)
)
x25OperEntry.setIndexNames(
    (0, "RFC1382-MIB", "x25OperIndex"),
)
if mibBuilder.loadTexts:
    x25OperEntry.setStatus("mandatory")
_X25OperIndex_Type = IfIndexType
_X25OperIndex_Object = MibTableColumn
x25OperIndex = _X25OperIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 1),
    _X25OperIndex_Type()
)
x25OperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperIndex.setStatus("mandatory")


class _X25OperInterfaceMode_Type(Integer32):
    """Custom type x25OperInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1),
          ("dxe", 3))
    )


_X25OperInterfaceMode_Type.__name__ = "Integer32"
_X25OperInterfaceMode_Object = MibTableColumn
x25OperInterfaceMode = _X25OperInterfaceMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 2),
    _X25OperInterfaceMode_Type()
)
x25OperInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperInterfaceMode.setStatus("mandatory")


class _X25OperMaxActiveCircuits_Type(Integer32):
    """Custom type x25OperMaxActiveCircuits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_X25OperMaxActiveCircuits_Type.__name__ = "Integer32"
_X25OperMaxActiveCircuits_Object = MibTableColumn
x25OperMaxActiveCircuits = _X25OperMaxActiveCircuits_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 3),
    _X25OperMaxActiveCircuits_Type()
)
x25OperMaxActiveCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperMaxActiveCircuits.setStatus("mandatory")


class _X25OperPacketSequencing_Type(Integer32):
    """Custom type x25OperPacketSequencing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_X25OperPacketSequencing_Type.__name__ = "Integer32"
_X25OperPacketSequencing_Object = MibTableColumn
x25OperPacketSequencing = _X25OperPacketSequencing_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 4),
    _X25OperPacketSequencing_Type()
)
x25OperPacketSequencing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperPacketSequencing.setStatus("mandatory")
_X25OperRestartTimer_Type = PositiveInteger
_X25OperRestartTimer_Object = MibTableColumn
x25OperRestartTimer = _X25OperRestartTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 5),
    _X25OperRestartTimer_Type()
)
x25OperRestartTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperRestartTimer.setStatus("mandatory")
_X25OperCallTimer_Type = PositiveInteger
_X25OperCallTimer_Object = MibTableColumn
x25OperCallTimer = _X25OperCallTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 6),
    _X25OperCallTimer_Type()
)
x25OperCallTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperCallTimer.setStatus("mandatory")
_X25OperResetTimer_Type = PositiveInteger
_X25OperResetTimer_Object = MibTableColumn
x25OperResetTimer = _X25OperResetTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 7),
    _X25OperResetTimer_Type()
)
x25OperResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperResetTimer.setStatus("mandatory")
_X25OperClearTimer_Type = PositiveInteger
_X25OperClearTimer_Object = MibTableColumn
x25OperClearTimer = _X25OperClearTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 8),
    _X25OperClearTimer_Type()
)
x25OperClearTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperClearTimer.setStatus("mandatory")
_X25OperWindowTimer_Type = PositiveInteger
_X25OperWindowTimer_Object = MibTableColumn
x25OperWindowTimer = _X25OperWindowTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 9),
    _X25OperWindowTimer_Type()
)
x25OperWindowTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperWindowTimer.setStatus("mandatory")
_X25OperDataRxmtTimer_Type = PositiveInteger
_X25OperDataRxmtTimer_Object = MibTableColumn
x25OperDataRxmtTimer = _X25OperDataRxmtTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 10),
    _X25OperDataRxmtTimer_Type()
)
x25OperDataRxmtTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperDataRxmtTimer.setStatus("mandatory")
_X25OperInterruptTimer_Type = PositiveInteger
_X25OperInterruptTimer_Object = MibTableColumn
x25OperInterruptTimer = _X25OperInterruptTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 11),
    _X25OperInterruptTimer_Type()
)
x25OperInterruptTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperInterruptTimer.setStatus("mandatory")
_X25OperRejectTimer_Type = PositiveInteger
_X25OperRejectTimer_Object = MibTableColumn
x25OperRejectTimer = _X25OperRejectTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 12),
    _X25OperRejectTimer_Type()
)
x25OperRejectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperRejectTimer.setStatus("mandatory")
_X25OperRegistrationRequestTimer_Type = PositiveInteger
_X25OperRegistrationRequestTimer_Object = MibTableColumn
x25OperRegistrationRequestTimer = _X25OperRegistrationRequestTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 13),
    _X25OperRegistrationRequestTimer_Type()
)
x25OperRegistrationRequestTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperRegistrationRequestTimer.setStatus("mandatory")
_X25OperMinimumRecallTimer_Type = PositiveInteger
_X25OperMinimumRecallTimer_Object = MibTableColumn
x25OperMinimumRecallTimer = _X25OperMinimumRecallTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 14),
    _X25OperMinimumRecallTimer_Type()
)
x25OperMinimumRecallTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperMinimumRecallTimer.setStatus("mandatory")


class _X25OperRestartCount_Type(Integer32):
    """Custom type x25OperRestartCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25OperRestartCount_Type.__name__ = "Integer32"
_X25OperRestartCount_Object = MibTableColumn
x25OperRestartCount = _X25OperRestartCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 15),
    _X25OperRestartCount_Type()
)
x25OperRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperRestartCount.setStatus("mandatory")


class _X25OperResetCount_Type(Integer32):
    """Custom type x25OperResetCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25OperResetCount_Type.__name__ = "Integer32"
_X25OperResetCount_Object = MibTableColumn
x25OperResetCount = _X25OperResetCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 16),
    _X25OperResetCount_Type()
)
x25OperResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperResetCount.setStatus("mandatory")


class _X25OperClearCount_Type(Integer32):
    """Custom type x25OperClearCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25OperClearCount_Type.__name__ = "Integer32"
_X25OperClearCount_Object = MibTableColumn
x25OperClearCount = _X25OperClearCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 17),
    _X25OperClearCount_Type()
)
x25OperClearCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperClearCount.setStatus("mandatory")


class _X25OperDataRxmtCount_Type(Integer32):
    """Custom type x25OperDataRxmtCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25OperDataRxmtCount_Type.__name__ = "Integer32"
_X25OperDataRxmtCount_Object = MibTableColumn
x25OperDataRxmtCount = _X25OperDataRxmtCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 18),
    _X25OperDataRxmtCount_Type()
)
x25OperDataRxmtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperDataRxmtCount.setStatus("mandatory")


class _X25OperRejectCount_Type(Integer32):
    """Custom type x25OperRejectCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25OperRejectCount_Type.__name__ = "Integer32"
_X25OperRejectCount_Object = MibTableColumn
x25OperRejectCount = _X25OperRejectCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 19),
    _X25OperRejectCount_Type()
)
x25OperRejectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperRejectCount.setStatus("mandatory")


class _X25OperRegistrationRequestCount_Type(Integer32):
    """Custom type x25OperRegistrationRequestCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_X25OperRegistrationRequestCount_Type.__name__ = "Integer32"
_X25OperRegistrationRequestCount_Object = MibTableColumn
x25OperRegistrationRequestCount = _X25OperRegistrationRequestCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 20),
    _X25OperRegistrationRequestCount_Type()
)
x25OperRegistrationRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperRegistrationRequestCount.setStatus("mandatory")


class _X25OperNumberPVCs_Type(Integer32):
    """Custom type x25OperNumberPVCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_X25OperNumberPVCs_Type.__name__ = "Integer32"
_X25OperNumberPVCs_Object = MibTableColumn
x25OperNumberPVCs = _X25OperNumberPVCs_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 21),
    _X25OperNumberPVCs_Type()
)
x25OperNumberPVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperNumberPVCs.setStatus("mandatory")
_X25OperDefCallParamId_Type = ObjectIdentifier
_X25OperDefCallParamId_Object = MibTableColumn
x25OperDefCallParamId = _X25OperDefCallParamId_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 22),
    _X25OperDefCallParamId_Type()
)
x25OperDefCallParamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperDefCallParamId.setStatus("mandatory")
_X25OperLocalAddress_Type = X121Address
_X25OperLocalAddress_Object = MibTableColumn
x25OperLocalAddress = _X25OperLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 23),
    _X25OperLocalAddress_Type()
)
x25OperLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperLocalAddress.setStatus("mandatory")
_X25OperDataLinkId_Type = ObjectIdentifier
_X25OperDataLinkId_Object = MibTableColumn
x25OperDataLinkId = _X25OperDataLinkId_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 24),
    _X25OperDataLinkId_Type()
)
x25OperDataLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperDataLinkId.setStatus("mandatory")
_X25OperProtocolVersionSupported_Type = ObjectIdentifier
_X25OperProtocolVersionSupported_Object = MibTableColumn
x25OperProtocolVersionSupported = _X25OperProtocolVersionSupported_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 25),
    _X25OperProtocolVersionSupported_Type()
)
x25OperProtocolVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25OperProtocolVersionSupported.setStatus("mandatory")
_X25StatTable_Object = MibTable
x25StatTable = _X25StatTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3)
)
if mibBuilder.loadTexts:
    x25StatTable.setStatus("mandatory")
_X25StatEntry_Object = MibTableRow
x25StatEntry = _X25StatEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1)
)
x25StatEntry.setIndexNames(
    (0, "RFC1382-MIB", "x25StatIndex"),
)
if mibBuilder.loadTexts:
    x25StatEntry.setStatus("mandatory")
_X25StatIndex_Type = IfIndexType
_X25StatIndex_Object = MibTableColumn
x25StatIndex = _X25StatIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 1),
    _X25StatIndex_Type()
)
x25StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatIndex.setStatus("mandatory")
_X25StatInCalls_Type = Counter32
_X25StatInCalls_Object = MibTableColumn
x25StatInCalls = _X25StatInCalls_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 2),
    _X25StatInCalls_Type()
)
x25StatInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInCalls.setStatus("mandatory")
_X25StatInCallRefusals_Type = Counter32
_X25StatInCallRefusals_Object = MibTableColumn
x25StatInCallRefusals = _X25StatInCallRefusals_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 3),
    _X25StatInCallRefusals_Type()
)
x25StatInCallRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInCallRefusals.setStatus("mandatory")
_X25StatInProviderInitiatedClears_Type = Counter32
_X25StatInProviderInitiatedClears_Object = MibTableColumn
x25StatInProviderInitiatedClears = _X25StatInProviderInitiatedClears_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 4),
    _X25StatInProviderInitiatedClears_Type()
)
x25StatInProviderInitiatedClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInProviderInitiatedClears.setStatus("mandatory")
_X25StatInRemotelyInitiatedResets_Type = Counter32
_X25StatInRemotelyInitiatedResets_Object = MibTableColumn
x25StatInRemotelyInitiatedResets = _X25StatInRemotelyInitiatedResets_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 5),
    _X25StatInRemotelyInitiatedResets_Type()
)
x25StatInRemotelyInitiatedResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInRemotelyInitiatedResets.setStatus("mandatory")
_X25StatInProviderInitiatedResets_Type = Counter32
_X25StatInProviderInitiatedResets_Object = MibTableColumn
x25StatInProviderInitiatedResets = _X25StatInProviderInitiatedResets_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 6),
    _X25StatInProviderInitiatedResets_Type()
)
x25StatInProviderInitiatedResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInProviderInitiatedResets.setStatus("mandatory")
_X25StatInRestarts_Type = Counter32
_X25StatInRestarts_Object = MibTableColumn
x25StatInRestarts = _X25StatInRestarts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 7),
    _X25StatInRestarts_Type()
)
x25StatInRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInRestarts.setStatus("mandatory")
_X25StatInDataPackets_Type = Counter32
_X25StatInDataPackets_Object = MibTableColumn
x25StatInDataPackets = _X25StatInDataPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 8),
    _X25StatInDataPackets_Type()
)
x25StatInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInDataPackets.setStatus("mandatory")
_X25StatInAccusedOfProtocolErrors_Type = Counter32
_X25StatInAccusedOfProtocolErrors_Object = MibTableColumn
x25StatInAccusedOfProtocolErrors = _X25StatInAccusedOfProtocolErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 9),
    _X25StatInAccusedOfProtocolErrors_Type()
)
x25StatInAccusedOfProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInAccusedOfProtocolErrors.setStatus("mandatory")
_X25StatInInterrupts_Type = Counter32
_X25StatInInterrupts_Object = MibTableColumn
x25StatInInterrupts = _X25StatInInterrupts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 10),
    _X25StatInInterrupts_Type()
)
x25StatInInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInInterrupts.setStatus("mandatory")
_X25StatOutCallAttempts_Type = Counter32
_X25StatOutCallAttempts_Object = MibTableColumn
x25StatOutCallAttempts = _X25StatOutCallAttempts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 11),
    _X25StatOutCallAttempts_Type()
)
x25StatOutCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatOutCallAttempts.setStatus("mandatory")
_X25StatOutCallFailures_Type = Counter32
_X25StatOutCallFailures_Object = MibTableColumn
x25StatOutCallFailures = _X25StatOutCallFailures_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 12),
    _X25StatOutCallFailures_Type()
)
x25StatOutCallFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatOutCallFailures.setStatus("mandatory")
_X25StatOutInterrupts_Type = Counter32
_X25StatOutInterrupts_Object = MibTableColumn
x25StatOutInterrupts = _X25StatOutInterrupts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 13),
    _X25StatOutInterrupts_Type()
)
x25StatOutInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatOutInterrupts.setStatus("mandatory")
_X25StatOutDataPackets_Type = Counter32
_X25StatOutDataPackets_Object = MibTableColumn
x25StatOutDataPackets = _X25StatOutDataPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 14),
    _X25StatOutDataPackets_Type()
)
x25StatOutDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatOutDataPackets.setStatus("mandatory")
_X25StatOutgoingCircuits_Type = Gauge32
_X25StatOutgoingCircuits_Object = MibTableColumn
x25StatOutgoingCircuits = _X25StatOutgoingCircuits_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 15),
    _X25StatOutgoingCircuits_Type()
)
x25StatOutgoingCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatOutgoingCircuits.setStatus("mandatory")
_X25StatIncomingCircuits_Type = Gauge32
_X25StatIncomingCircuits_Object = MibTableColumn
x25StatIncomingCircuits = _X25StatIncomingCircuits_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 16),
    _X25StatIncomingCircuits_Type()
)
x25StatIncomingCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatIncomingCircuits.setStatus("mandatory")
_X25StatTwowayCircuits_Type = Gauge32
_X25StatTwowayCircuits_Object = MibTableColumn
x25StatTwowayCircuits = _X25StatTwowayCircuits_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 17),
    _X25StatTwowayCircuits_Type()
)
x25StatTwowayCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatTwowayCircuits.setStatus("mandatory")
_X25StatRestartTimeouts_Type = Counter32
_X25StatRestartTimeouts_Object = MibTableColumn
x25StatRestartTimeouts = _X25StatRestartTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 18),
    _X25StatRestartTimeouts_Type()
)
x25StatRestartTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatRestartTimeouts.setStatus("mandatory")
_X25StatCallTimeouts_Type = Counter32
_X25StatCallTimeouts_Object = MibTableColumn
x25StatCallTimeouts = _X25StatCallTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 19),
    _X25StatCallTimeouts_Type()
)
x25StatCallTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatCallTimeouts.setStatus("mandatory")
_X25StatResetTimeouts_Type = Counter32
_X25StatResetTimeouts_Object = MibTableColumn
x25StatResetTimeouts = _X25StatResetTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 20),
    _X25StatResetTimeouts_Type()
)
x25StatResetTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatResetTimeouts.setStatus("mandatory")
_X25StatClearTimeouts_Type = Counter32
_X25StatClearTimeouts_Object = MibTableColumn
x25StatClearTimeouts = _X25StatClearTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 21),
    _X25StatClearTimeouts_Type()
)
x25StatClearTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatClearTimeouts.setStatus("mandatory")
_X25StatDataRxmtTimeouts_Type = Counter32
_X25StatDataRxmtTimeouts_Object = MibTableColumn
x25StatDataRxmtTimeouts = _X25StatDataRxmtTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 22),
    _X25StatDataRxmtTimeouts_Type()
)
x25StatDataRxmtTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatDataRxmtTimeouts.setStatus("mandatory")
_X25StatInterruptTimeouts_Type = Counter32
_X25StatInterruptTimeouts_Object = MibTableColumn
x25StatInterruptTimeouts = _X25StatInterruptTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 23),
    _X25StatInterruptTimeouts_Type()
)
x25StatInterruptTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInterruptTimeouts.setStatus("mandatory")
_X25StatRetryCountExceededs_Type = Counter32
_X25StatRetryCountExceededs_Object = MibTableColumn
x25StatRetryCountExceededs = _X25StatRetryCountExceededs_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 24),
    _X25StatRetryCountExceededs_Type()
)
x25StatRetryCountExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatRetryCountExceededs.setStatus("mandatory")
_X25StatClearCountExceededs_Type = Counter32
_X25StatClearCountExceededs_Object = MibTableColumn
x25StatClearCountExceededs = _X25StatClearCountExceededs_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 25),
    _X25StatClearCountExceededs_Type()
)
x25StatClearCountExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatClearCountExceededs.setStatus("mandatory")
_X25ChannelTable_Object = MibTable
x25ChannelTable = _X25ChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 4)
)
if mibBuilder.loadTexts:
    x25ChannelTable.setStatus("mandatory")
_X25ChannelEntry_Object = MibTableRow
x25ChannelEntry = _X25ChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 4, 1)
)
x25ChannelEntry.setIndexNames(
    (0, "RFC1382-MIB", "x25ChannelIndex"),
)
if mibBuilder.loadTexts:
    x25ChannelEntry.setStatus("mandatory")
_X25ChannelIndex_Type = IfIndexType
_X25ChannelIndex_Object = MibTableColumn
x25ChannelIndex = _X25ChannelIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 1),
    _X25ChannelIndex_Type()
)
x25ChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ChannelIndex.setStatus("mandatory")


class _X25ChannelLIC_Type(Integer32):
    """Custom type x25ChannelLIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelLIC_Type.__name__ = "Integer32"
_X25ChannelLIC_Object = MibTableColumn
x25ChannelLIC = _X25ChannelLIC_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 2),
    _X25ChannelLIC_Type()
)
x25ChannelLIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelLIC.setStatus("mandatory")


class _X25ChannelHIC_Type(Integer32):
    """Custom type x25ChannelHIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelHIC_Type.__name__ = "Integer32"
_X25ChannelHIC_Object = MibTableColumn
x25ChannelHIC = _X25ChannelHIC_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 3),
    _X25ChannelHIC_Type()
)
x25ChannelHIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelHIC.setStatus("mandatory")


class _X25ChannelLTC_Type(Integer32):
    """Custom type x25ChannelLTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelLTC_Type.__name__ = "Integer32"
_X25ChannelLTC_Object = MibTableColumn
x25ChannelLTC = _X25ChannelLTC_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 4),
    _X25ChannelLTC_Type()
)
x25ChannelLTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelLTC.setStatus("mandatory")


class _X25ChannelHTC_Type(Integer32):
    """Custom type x25ChannelHTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelHTC_Type.__name__ = "Integer32"
_X25ChannelHTC_Object = MibTableColumn
x25ChannelHTC = _X25ChannelHTC_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 5),
    _X25ChannelHTC_Type()
)
x25ChannelHTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelHTC.setStatus("mandatory")


class _X25ChannelLOC_Type(Integer32):
    """Custom type x25ChannelLOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelLOC_Type.__name__ = "Integer32"
_X25ChannelLOC_Object = MibTableColumn
x25ChannelLOC = _X25ChannelLOC_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 6),
    _X25ChannelLOC_Type()
)
x25ChannelLOC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelLOC.setStatus("mandatory")


class _X25ChannelHOC_Type(Integer32):
    """Custom type x25ChannelHOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelHOC_Type.__name__ = "Integer32"
_X25ChannelHOC_Object = MibTableColumn
x25ChannelHOC = _X25ChannelHOC_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 7),
    _X25ChannelHOC_Type()
)
x25ChannelHOC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelHOC.setStatus("mandatory")
_X25CircuitTable_Object = MibTable
x25CircuitTable = _X25CircuitTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5)
)
if mibBuilder.loadTexts:
    x25CircuitTable.setStatus("mandatory")
_X25CircuitEntry_Object = MibTableRow
x25CircuitEntry = _X25CircuitEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1)
)
x25CircuitEntry.setIndexNames(
    (0, "RFC1382-MIB", "x25CircuitIndex"),
    (0, "RFC1382-MIB", "x25CircuitChannel"),
)
if mibBuilder.loadTexts:
    x25CircuitEntry.setStatus("mandatory")
_X25CircuitIndex_Type = IfIndexType
_X25CircuitIndex_Object = MibTableColumn
x25CircuitIndex = _X25CircuitIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 1),
    _X25CircuitIndex_Type()
)
x25CircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitIndex.setStatus("mandatory")


class _X25CircuitChannel_Type(Integer32):
    """Custom type x25CircuitChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25CircuitChannel_Type.__name__ = "Integer32"
_X25CircuitChannel_Object = MibTableColumn
x25CircuitChannel = _X25CircuitChannel_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 2),
    _X25CircuitChannel_Type()
)
x25CircuitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitChannel.setStatus("mandatory")


class _X25CircuitStatus_Type(Integer32):
    """Custom type x25CircuitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("calling", 3),
          ("clearing", 5),
          ("closed", 2),
          ("invalid", 1),
          ("open", 4),
          ("other", 10),
          ("pvc", 6),
          ("pvcResetting", 7),
          ("startClear", 8),
          ("startPvcResetting", 9))
    )


_X25CircuitStatus_Type.__name__ = "Integer32"
_X25CircuitStatus_Object = MibTableColumn
x25CircuitStatus = _X25CircuitStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 3),
    _X25CircuitStatus_Type()
)
x25CircuitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CircuitStatus.setStatus("mandatory")
_X25CircuitEstablishTime_Type = TimeTicks
_X25CircuitEstablishTime_Object = MibTableColumn
x25CircuitEstablishTime = _X25CircuitEstablishTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 4),
    _X25CircuitEstablishTime_Type()
)
x25CircuitEstablishTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitEstablishTime.setStatus("mandatory")


class _X25CircuitDirection_Type(Integer32):
    """Custom type x25CircuitDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2),
          ("pvc", 3))
    )


_X25CircuitDirection_Type.__name__ = "Integer32"
_X25CircuitDirection_Object = MibTableColumn
x25CircuitDirection = _X25CircuitDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 5),
    _X25CircuitDirection_Type()
)
x25CircuitDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CircuitDirection.setStatus("mandatory")
_X25CircuitInOctets_Type = Counter32
_X25CircuitInOctets_Object = MibTableColumn
x25CircuitInOctets = _X25CircuitInOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 6),
    _X25CircuitInOctets_Type()
)
x25CircuitInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInOctets.setStatus("mandatory")
_X25CircuitInPdus_Type = Counter32
_X25CircuitInPdus_Object = MibTableColumn
x25CircuitInPdus = _X25CircuitInPdus_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 7),
    _X25CircuitInPdus_Type()
)
x25CircuitInPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInPdus.setStatus("mandatory")
_X25CircuitInRemotelyInitiatedResets_Type = Counter32
_X25CircuitInRemotelyInitiatedResets_Object = MibTableColumn
x25CircuitInRemotelyInitiatedResets = _X25CircuitInRemotelyInitiatedResets_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 8),
    _X25CircuitInRemotelyInitiatedResets_Type()
)
x25CircuitInRemotelyInitiatedResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInRemotelyInitiatedResets.setStatus("mandatory")
_X25CircuitInProviderInitiatedResets_Type = Counter32
_X25CircuitInProviderInitiatedResets_Object = MibTableColumn
x25CircuitInProviderInitiatedResets = _X25CircuitInProviderInitiatedResets_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 9),
    _X25CircuitInProviderInitiatedResets_Type()
)
x25CircuitInProviderInitiatedResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInProviderInitiatedResets.setStatus("mandatory")
_X25CircuitInInterrupts_Type = Counter32
_X25CircuitInInterrupts_Object = MibTableColumn
x25CircuitInInterrupts = _X25CircuitInInterrupts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 10),
    _X25CircuitInInterrupts_Type()
)
x25CircuitInInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInInterrupts.setStatus("mandatory")
_X25CircuitOutOctets_Type = Counter32
_X25CircuitOutOctets_Object = MibTableColumn
x25CircuitOutOctets = _X25CircuitOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 11),
    _X25CircuitOutOctets_Type()
)
x25CircuitOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitOutOctets.setStatus("mandatory")
_X25CircuitOutPdus_Type = Counter32
_X25CircuitOutPdus_Object = MibTableColumn
x25CircuitOutPdus = _X25CircuitOutPdus_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 12),
    _X25CircuitOutPdus_Type()
)
x25CircuitOutPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitOutPdus.setStatus("mandatory")
_X25CircuitOutInterrupts_Type = Counter32
_X25CircuitOutInterrupts_Object = MibTableColumn
x25CircuitOutInterrupts = _X25CircuitOutInterrupts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 13),
    _X25CircuitOutInterrupts_Type()
)
x25CircuitOutInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitOutInterrupts.setStatus("mandatory")
_X25CircuitDataRetransmissionTimeouts_Type = Counter32
_X25CircuitDataRetransmissionTimeouts_Object = MibTableColumn
x25CircuitDataRetransmissionTimeouts = _X25CircuitDataRetransmissionTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 14),
    _X25CircuitDataRetransmissionTimeouts_Type()
)
x25CircuitDataRetransmissionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitDataRetransmissionTimeouts.setStatus("mandatory")
_X25CircuitResetTimeouts_Type = Counter32
_X25CircuitResetTimeouts_Object = MibTableColumn
x25CircuitResetTimeouts = _X25CircuitResetTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 15),
    _X25CircuitResetTimeouts_Type()
)
x25CircuitResetTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitResetTimeouts.setStatus("mandatory")
_X25CircuitInterruptTimeouts_Type = Counter32
_X25CircuitInterruptTimeouts_Object = MibTableColumn
x25CircuitInterruptTimeouts = _X25CircuitInterruptTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 16),
    _X25CircuitInterruptTimeouts_Type()
)
x25CircuitInterruptTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInterruptTimeouts.setStatus("mandatory")
_X25CircuitCallParamId_Type = ObjectIdentifier
_X25CircuitCallParamId_Object = MibTableColumn
x25CircuitCallParamId = _X25CircuitCallParamId_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 17),
    _X25CircuitCallParamId_Type()
)
x25CircuitCallParamId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CircuitCallParamId.setStatus("mandatory")


class _X25CircuitCalledDteAddress_Type(X121Address):
    """Custom type x25CircuitCalledDteAddress based on X121Address"""
    defaultHexValue = ""


_X25CircuitCalledDteAddress_Object = MibTableColumn
x25CircuitCalledDteAddress = _X25CircuitCalledDteAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 18),
    _X25CircuitCalledDteAddress_Type()
)
x25CircuitCalledDteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CircuitCalledDteAddress.setStatus("mandatory")


class _X25CircuitCallingDteAddress_Type(X121Address):
    """Custom type x25CircuitCallingDteAddress based on X121Address"""
    defaultHexValue = ""


_X25CircuitCallingDteAddress_Object = MibTableColumn
x25CircuitCallingDteAddress = _X25CircuitCallingDteAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 19),
    _X25CircuitCallingDteAddress_Type()
)
x25CircuitCallingDteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CircuitCallingDteAddress.setStatus("mandatory")


class _X25CircuitOriginallyCalledAddress_Type(X121Address):
    """Custom type x25CircuitOriginallyCalledAddress based on X121Address"""
    defaultHexValue = ""


_X25CircuitOriginallyCalledAddress_Object = MibTableColumn
x25CircuitOriginallyCalledAddress = _X25CircuitOriginallyCalledAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 20),
    _X25CircuitOriginallyCalledAddress_Type()
)
x25CircuitOriginallyCalledAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CircuitOriginallyCalledAddress.setStatus("mandatory")


class _X25CircuitDescr_Type(DisplayString):
    """Custom type x25CircuitDescr based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_X25CircuitDescr_Type.__name__ = "DisplayString"
_X25CircuitDescr_Object = MibTableColumn
x25CircuitDescr = _X25CircuitDescr_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 21),
    _X25CircuitDescr_Type()
)
x25CircuitDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CircuitDescr.setStatus("mandatory")
_X25ClearedCircuitEntriesRequested_Type = PositiveInteger
_X25ClearedCircuitEntriesRequested_Object = MibScalar
x25ClearedCircuitEntriesRequested = _X25ClearedCircuitEntriesRequested_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 6),
    _X25ClearedCircuitEntriesRequested_Type()
)
x25ClearedCircuitEntriesRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ClearedCircuitEntriesRequested.setStatus("mandatory")
_X25ClearedCircuitEntriesGranted_Type = PositiveInteger
_X25ClearedCircuitEntriesGranted_Object = MibScalar
x25ClearedCircuitEntriesGranted = _X25ClearedCircuitEntriesGranted_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 7),
    _X25ClearedCircuitEntriesGranted_Type()
)
x25ClearedCircuitEntriesGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitEntriesGranted.setStatus("mandatory")
_X25ClearedCircuitTable_Object = MibTable
x25ClearedCircuitTable = _X25ClearedCircuitTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8)
)
if mibBuilder.loadTexts:
    x25ClearedCircuitTable.setStatus("mandatory")
_X25ClearedCircuitEntry_Object = MibTableRow
x25ClearedCircuitEntry = _X25ClearedCircuitEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1)
)
x25ClearedCircuitEntry.setIndexNames(
    (0, "RFC1382-MIB", "x25ClearedCircuitIndex"),
)
if mibBuilder.loadTexts:
    x25ClearedCircuitEntry.setStatus("mandatory")
_X25ClearedCircuitIndex_Type = PositiveInteger
_X25ClearedCircuitIndex_Object = MibTableColumn
x25ClearedCircuitIndex = _X25ClearedCircuitIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 1),
    _X25ClearedCircuitIndex_Type()
)
x25ClearedCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitIndex.setStatus("mandatory")
_X25ClearedCircuitPleIndex_Type = IfIndexType
_X25ClearedCircuitPleIndex_Object = MibTableColumn
x25ClearedCircuitPleIndex = _X25ClearedCircuitPleIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 2),
    _X25ClearedCircuitPleIndex_Type()
)
x25ClearedCircuitPleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitPleIndex.setStatus("mandatory")
_X25ClearedCircuitTimeEstablished_Type = TimeTicks
_X25ClearedCircuitTimeEstablished_Object = MibTableColumn
x25ClearedCircuitTimeEstablished = _X25ClearedCircuitTimeEstablished_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 3),
    _X25ClearedCircuitTimeEstablished_Type()
)
x25ClearedCircuitTimeEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitTimeEstablished.setStatus("mandatory")
_X25ClearedCircuitTimeCleared_Type = TimeTicks
_X25ClearedCircuitTimeCleared_Object = MibTableColumn
x25ClearedCircuitTimeCleared = _X25ClearedCircuitTimeCleared_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 4),
    _X25ClearedCircuitTimeCleared_Type()
)
x25ClearedCircuitTimeCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitTimeCleared.setStatus("mandatory")


class _X25ClearedCircuitChannel_Type(Integer32):
    """Custom type x25ClearedCircuitChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ClearedCircuitChannel_Type.__name__ = "Integer32"
_X25ClearedCircuitChannel_Object = MibTableColumn
x25ClearedCircuitChannel = _X25ClearedCircuitChannel_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 5),
    _X25ClearedCircuitChannel_Type()
)
x25ClearedCircuitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitChannel.setStatus("mandatory")


class _X25ClearedCircuitClearingCause_Type(Integer32):
    """Custom type x25ClearedCircuitClearingCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25ClearedCircuitClearingCause_Type.__name__ = "Integer32"
_X25ClearedCircuitClearingCause_Object = MibTableColumn
x25ClearedCircuitClearingCause = _X25ClearedCircuitClearingCause_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 6),
    _X25ClearedCircuitClearingCause_Type()
)
x25ClearedCircuitClearingCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitClearingCause.setStatus("mandatory")


class _X25ClearedCircuitDiagnosticCode_Type(Integer32):
    """Custom type x25ClearedCircuitDiagnosticCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25ClearedCircuitDiagnosticCode_Type.__name__ = "Integer32"
_X25ClearedCircuitDiagnosticCode_Object = MibTableColumn
x25ClearedCircuitDiagnosticCode = _X25ClearedCircuitDiagnosticCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 7),
    _X25ClearedCircuitDiagnosticCode_Type()
)
x25ClearedCircuitDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitDiagnosticCode.setStatus("mandatory")
_X25ClearedCircuitInPdus_Type = Counter32
_X25ClearedCircuitInPdus_Object = MibTableColumn
x25ClearedCircuitInPdus = _X25ClearedCircuitInPdus_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 8),
    _X25ClearedCircuitInPdus_Type()
)
x25ClearedCircuitInPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitInPdus.setStatus("mandatory")
_X25ClearedCircuitOutPdus_Type = Counter32
_X25ClearedCircuitOutPdus_Object = MibTableColumn
x25ClearedCircuitOutPdus = _X25ClearedCircuitOutPdus_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 9),
    _X25ClearedCircuitOutPdus_Type()
)
x25ClearedCircuitOutPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitOutPdus.setStatus("mandatory")
_X25ClearedCircuitCalledAddress_Type = X121Address
_X25ClearedCircuitCalledAddress_Object = MibTableColumn
x25ClearedCircuitCalledAddress = _X25ClearedCircuitCalledAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 10),
    _X25ClearedCircuitCalledAddress_Type()
)
x25ClearedCircuitCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitCalledAddress.setStatus("mandatory")
_X25ClearedCircuitCallingAddress_Type = X121Address
_X25ClearedCircuitCallingAddress_Object = MibTableColumn
x25ClearedCircuitCallingAddress = _X25ClearedCircuitCallingAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 11),
    _X25ClearedCircuitCallingAddress_Type()
)
x25ClearedCircuitCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitCallingAddress.setStatus("mandatory")


class _X25ClearedCircuitClearFacilities_Type(OctetString):
    """Custom type x25ClearedCircuitClearFacilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 109),
    )


_X25ClearedCircuitClearFacilities_Type.__name__ = "OctetString"
_X25ClearedCircuitClearFacilities_Object = MibTableColumn
x25ClearedCircuitClearFacilities = _X25ClearedCircuitClearFacilities_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 12),
    _X25ClearedCircuitClearFacilities_Type()
)
x25ClearedCircuitClearFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ClearedCircuitClearFacilities.setStatus("mandatory")
_X25CallParmTable_Object = MibTable
x25CallParmTable = _X25CallParmTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9)
)
if mibBuilder.loadTexts:
    x25CallParmTable.setStatus("mandatory")
_X25CallParmEntry_Object = MibTableRow
x25CallParmEntry = _X25CallParmEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1)
)
x25CallParmEntry.setIndexNames(
    (0, "RFC1382-MIB", "x25CallParmIndex"),
)
if mibBuilder.loadTexts:
    x25CallParmEntry.setStatus("mandatory")
_X25CallParmIndex_Type = PositiveInteger
_X25CallParmIndex_Object = MibTableColumn
x25CallParmIndex = _X25CallParmIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 1),
    _X25CallParmIndex_Type()
)
x25CallParmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallParmIndex.setStatus("mandatory")
_X25CallParmStatus_Type = EntryStatus
_X25CallParmStatus_Object = MibTableColumn
x25CallParmStatus = _X25CallParmStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 2),
    _X25CallParmStatus_Type()
)
x25CallParmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmStatus.setStatus("mandatory")
_X25CallParmRefCount_Type = PositiveInteger
_X25CallParmRefCount_Object = MibTableColumn
x25CallParmRefCount = _X25CallParmRefCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 3),
    _X25CallParmRefCount_Type()
)
x25CallParmRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CallParmRefCount.setStatus("mandatory")


class _X25CallParmInPacketSize_Type(Integer32):
    """Custom type x25CallParmInPacketSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_X25CallParmInPacketSize_Type.__name__ = "Integer32"
_X25CallParmInPacketSize_Object = MibTableColumn
x25CallParmInPacketSize = _X25CallParmInPacketSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 4),
    _X25CallParmInPacketSize_Type()
)
x25CallParmInPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmInPacketSize.setStatus("mandatory")


class _X25CallParmOutPacketSize_Type(Integer32):
    """Custom type x25CallParmOutPacketSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_X25CallParmOutPacketSize_Type.__name__ = "Integer32"
_X25CallParmOutPacketSize_Object = MibTableColumn
x25CallParmOutPacketSize = _X25CallParmOutPacketSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 5),
    _X25CallParmOutPacketSize_Type()
)
x25CallParmOutPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmOutPacketSize.setStatus("mandatory")


class _X25CallParmInWindowSize_Type(Integer32):
    """Custom type x25CallParmInWindowSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25CallParmInWindowSize_Type.__name__ = "Integer32"
_X25CallParmInWindowSize_Object = MibTableColumn
x25CallParmInWindowSize = _X25CallParmInWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 6),
    _X25CallParmInWindowSize_Type()
)
x25CallParmInWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmInWindowSize.setStatus("mandatory")


class _X25CallParmOutWindowSize_Type(Integer32):
    """Custom type x25CallParmOutWindowSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25CallParmOutWindowSize_Type.__name__ = "Integer32"
_X25CallParmOutWindowSize_Object = MibTableColumn
x25CallParmOutWindowSize = _X25CallParmOutWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 7),
    _X25CallParmOutWindowSize_Type()
)
x25CallParmOutWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmOutWindowSize.setStatus("mandatory")


class _X25CallParmAcceptReverseCharging_Type(Integer32):
    """Custom type x25CallParmAcceptReverseCharging based on Integer32"""
    defaultValue = 3

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
        *(("accept", 2),
          ("default", 1),
          ("neverAccept", 4),
          ("refuse", 3))
    )


_X25CallParmAcceptReverseCharging_Type.__name__ = "Integer32"
_X25CallParmAcceptReverseCharging_Object = MibTableColumn
x25CallParmAcceptReverseCharging = _X25CallParmAcceptReverseCharging_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 8),
    _X25CallParmAcceptReverseCharging_Type()
)
x25CallParmAcceptReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmAcceptReverseCharging.setStatus("mandatory")


class _X25CallParmProposeReverseCharging_Type(Integer32):
    """Custom type x25CallParmProposeReverseCharging based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("local", 3),
          ("reverse", 2))
    )


_X25CallParmProposeReverseCharging_Type.__name__ = "Integer32"
_X25CallParmProposeReverseCharging_Object = MibTableColumn
x25CallParmProposeReverseCharging = _X25CallParmProposeReverseCharging_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 9),
    _X25CallParmProposeReverseCharging_Type()
)
x25CallParmProposeReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmProposeReverseCharging.setStatus("mandatory")


class _X25CallParmFastSelect_Type(Integer32):
    """Custom type x25CallParmFastSelect based on Integer32"""
    defaultValue = 5

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
        *(("default", 1),
          ("fastSelect", 3),
          ("noFastSelect", 5),
          ("noRestrictedFastResponse", 6),
          ("notSpecified", 2),
          ("restrictedFastResponse", 4))
    )


_X25CallParmFastSelect_Type.__name__ = "Integer32"
_X25CallParmFastSelect_Object = MibTableColumn
x25CallParmFastSelect = _X25CallParmFastSelect_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 10),
    _X25CallParmFastSelect_Type()
)
x25CallParmFastSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmFastSelect.setStatus("mandatory")


class _X25CallParmInThruPutClasSize_Type(Integer32):
    """Custom type x25CallParmInThruPutClasSize based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 7),
          ("tc150", 4),
          ("tc19200", 11),
          ("tc2400", 8),
          ("tc300", 5),
          ("tc4800", 9),
          ("tc48000", 12),
          ("tc600", 6),
          ("tc64000", 13),
          ("tc75", 3),
          ("tc9600", 10),
          ("tcDefault", 18),
          ("tcNone", 17),
          ("tcReserved0", 16),
          ("tcReserved1", 1),
          ("tcReserved14", 14),
          ("tcReserved15", 15),
          ("tcReserved2", 2))
    )


_X25CallParmInThruPutClasSize_Type.__name__ = "Integer32"
_X25CallParmInThruPutClasSize_Object = MibTableColumn
x25CallParmInThruPutClasSize = _X25CallParmInThruPutClasSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 11),
    _X25CallParmInThruPutClasSize_Type()
)
x25CallParmInThruPutClasSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmInThruPutClasSize.setStatus("mandatory")


class _X25CallParmOutThruPutClasSize_Type(Integer32):
    """Custom type x25CallParmOutThruPutClasSize based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("tc1200", 7),
          ("tc150", 4),
          ("tc19200", 11),
          ("tc2400", 8),
          ("tc300", 5),
          ("tc4800", 9),
          ("tc48000", 12),
          ("tc600", 6),
          ("tc64000", 13),
          ("tc75", 3),
          ("tc9600", 10),
          ("tcDefault", 18),
          ("tcNone", 17),
          ("tcReserved0", 16),
          ("tcReserved1", 1),
          ("tcReserved14", 14),
          ("tcReserved15", 15),
          ("tcReserved2", 2))
    )


_X25CallParmOutThruPutClasSize_Type.__name__ = "Integer32"
_X25CallParmOutThruPutClasSize_Object = MibTableColumn
x25CallParmOutThruPutClasSize = _X25CallParmOutThruPutClasSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 12),
    _X25CallParmOutThruPutClasSize_Type()
)
x25CallParmOutThruPutClasSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmOutThruPutClasSize.setStatus("mandatory")


class _X25CallParmCug_Type(DisplayString):
    """Custom type x25CallParmCug based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_X25CallParmCug_Type.__name__ = "DisplayString"
_X25CallParmCug_Object = MibTableColumn
x25CallParmCug = _X25CallParmCug_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 13),
    _X25CallParmCug_Type()
)
x25CallParmCug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmCug.setStatus("mandatory")


class _X25CallParmCugoa_Type(DisplayString):
    """Custom type x25CallParmCugoa based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_X25CallParmCugoa_Type.__name__ = "DisplayString"
_X25CallParmCugoa_Object = MibTableColumn
x25CallParmCugoa = _X25CallParmCugoa_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 14),
    _X25CallParmCugoa_Type()
)
x25CallParmCugoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmCugoa.setStatus("mandatory")


class _X25CallParmBcug_Type(DisplayString):
    """Custom type x25CallParmBcug based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_X25CallParmBcug_Type.__name__ = "DisplayString"
_X25CallParmBcug_Object = MibTableColumn
x25CallParmBcug = _X25CallParmBcug_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 15),
    _X25CallParmBcug_Type()
)
x25CallParmBcug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmBcug.setStatus("mandatory")


class _X25CallParmNui_Type(OctetString):
    """Custom type x25CallParmNui based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25CallParmNui_Type.__name__ = "OctetString"
_X25CallParmNui_Object = MibTableColumn
x25CallParmNui = _X25CallParmNui_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 16),
    _X25CallParmNui_Type()
)
x25CallParmNui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmNui.setStatus("mandatory")


class _X25CallParmChargingInfo_Type(Integer32):
    """Custom type x25CallParmChargingInfo based on Integer32"""
    defaultValue = 2

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
        *(("chargingInfo", 4),
          ("default", 1),
          ("noChargingInfo", 3),
          ("noFacility", 2))
    )


_X25CallParmChargingInfo_Type.__name__ = "Integer32"
_X25CallParmChargingInfo_Object = MibTableColumn
x25CallParmChargingInfo = _X25CallParmChargingInfo_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 17),
    _X25CallParmChargingInfo_Type()
)
x25CallParmChargingInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmChargingInfo.setStatus("mandatory")


class _X25CallParmRpoa_Type(DisplayString):
    """Custom type x25CallParmRpoa based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25CallParmRpoa_Type.__name__ = "DisplayString"
_X25CallParmRpoa_Object = MibTableColumn
x25CallParmRpoa = _X25CallParmRpoa_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 18),
    _X25CallParmRpoa_Type()
)
x25CallParmRpoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmRpoa.setStatus("mandatory")


class _X25CallParmTrnstDly_Type(Integer32):
    """Custom type x25CallParmTrnstDly based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65537),
    )


_X25CallParmTrnstDly_Type.__name__ = "Integer32"
_X25CallParmTrnstDly_Object = MibTableColumn
x25CallParmTrnstDly = _X25CallParmTrnstDly_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 19),
    _X25CallParmTrnstDly_Type()
)
x25CallParmTrnstDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmTrnstDly.setStatus("mandatory")


class _X25CallParmCallingExt_Type(DisplayString):
    """Custom type x25CallParmCallingExt based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_X25CallParmCallingExt_Type.__name__ = "DisplayString"
_X25CallParmCallingExt_Object = MibTableColumn
x25CallParmCallingExt = _X25CallParmCallingExt_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 20),
    _X25CallParmCallingExt_Type()
)
x25CallParmCallingExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmCallingExt.setStatus("mandatory")


class _X25CallParmCalledExt_Type(DisplayString):
    """Custom type x25CallParmCalledExt based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_X25CallParmCalledExt_Type.__name__ = "DisplayString"
_X25CallParmCalledExt_Object = MibTableColumn
x25CallParmCalledExt = _X25CallParmCalledExt_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 21),
    _X25CallParmCalledExt_Type()
)
x25CallParmCalledExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmCalledExt.setStatus("mandatory")


class _X25CallParmInMinThuPutCls_Type(Integer32):
    """Custom type x25CallParmInMinThuPutCls based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 17),
    )


_X25CallParmInMinThuPutCls_Type.__name__ = "Integer32"
_X25CallParmInMinThuPutCls_Object = MibTableColumn
x25CallParmInMinThuPutCls = _X25CallParmInMinThuPutCls_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 22),
    _X25CallParmInMinThuPutCls_Type()
)
x25CallParmInMinThuPutCls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmInMinThuPutCls.setStatus("mandatory")


class _X25CallParmOutMinThuPutCls_Type(Integer32):
    """Custom type x25CallParmOutMinThuPutCls based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 17),
    )


_X25CallParmOutMinThuPutCls_Type.__name__ = "Integer32"
_X25CallParmOutMinThuPutCls_Object = MibTableColumn
x25CallParmOutMinThuPutCls = _X25CallParmOutMinThuPutCls_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 23),
    _X25CallParmOutMinThuPutCls_Type()
)
x25CallParmOutMinThuPutCls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmOutMinThuPutCls.setStatus("mandatory")


class _X25CallParmEndTrnsDly_Type(OctetString):
    """Custom type x25CallParmEndTrnsDly based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_X25CallParmEndTrnsDly_Type.__name__ = "OctetString"
_X25CallParmEndTrnsDly_Object = MibTableColumn
x25CallParmEndTrnsDly = _X25CallParmEndTrnsDly_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 24),
    _X25CallParmEndTrnsDly_Type()
)
x25CallParmEndTrnsDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmEndTrnsDly.setStatus("mandatory")


class _X25CallParmPriority_Type(OctetString):
    """Custom type x25CallParmPriority based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_X25CallParmPriority_Type.__name__ = "OctetString"
_X25CallParmPriority_Object = MibTableColumn
x25CallParmPriority = _X25CallParmPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 25),
    _X25CallParmPriority_Type()
)
x25CallParmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmPriority.setStatus("mandatory")


class _X25CallParmProtection_Type(DisplayString):
    """Custom type x25CallParmProtection based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25CallParmProtection_Type.__name__ = "DisplayString"
_X25CallParmProtection_Object = MibTableColumn
x25CallParmProtection = _X25CallParmProtection_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 26),
    _X25CallParmProtection_Type()
)
x25CallParmProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmProtection.setStatus("mandatory")


class _X25CallParmExptData_Type(Integer32):
    """Custom type x25CallParmExptData based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("expeditedData", 3),
          ("noExpeditedData", 2))
    )


_X25CallParmExptData_Type.__name__ = "Integer32"
_X25CallParmExptData_Object = MibTableColumn
x25CallParmExptData = _X25CallParmExptData_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 27),
    _X25CallParmExptData_Type()
)
x25CallParmExptData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmExptData.setStatus("mandatory")


class _X25CallParmUserData_Type(OctetString):
    """Custom type x25CallParmUserData based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_X25CallParmUserData_Type.__name__ = "OctetString"
_X25CallParmUserData_Object = MibTableColumn
x25CallParmUserData = _X25CallParmUserData_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 28),
    _X25CallParmUserData_Type()
)
x25CallParmUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmUserData.setStatus("mandatory")


class _X25CallParmCallingNetworkFacilities_Type(OctetString):
    """Custom type x25CallParmCallingNetworkFacilities based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25CallParmCallingNetworkFacilities_Type.__name__ = "OctetString"
_X25CallParmCallingNetworkFacilities_Object = MibTableColumn
x25CallParmCallingNetworkFacilities = _X25CallParmCallingNetworkFacilities_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 29),
    _X25CallParmCallingNetworkFacilities_Type()
)
x25CallParmCallingNetworkFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmCallingNetworkFacilities.setStatus("mandatory")


class _X25CallParmCalledNetworkFacilities_Type(OctetString):
    """Custom type x25CallParmCalledNetworkFacilities based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_X25CallParmCalledNetworkFacilities_Type.__name__ = "OctetString"
_X25CallParmCalledNetworkFacilities_Object = MibTableColumn
x25CallParmCalledNetworkFacilities = _X25CallParmCalledNetworkFacilities_Object(
    (1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 30),
    _X25CallParmCalledNetworkFacilities_Type()
)
x25CallParmCalledNetworkFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmCalledNetworkFacilities.setStatus("mandatory")
_X25ProtocolVersion_ObjectIdentity = ObjectIdentity
x25ProtocolVersion = _X25ProtocolVersion_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 5, 10)
)
_X25protocolCcittV1976_ObjectIdentity = ObjectIdentity
x25protocolCcittV1976 = _X25protocolCcittV1976_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 5, 10, 1)
)
_X25protocolCcittV1980_ObjectIdentity = ObjectIdentity
x25protocolCcittV1980 = _X25protocolCcittV1980_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 5, 10, 2)
)
_X25protocolCcittV1984_ObjectIdentity = ObjectIdentity
x25protocolCcittV1984 = _X25protocolCcittV1984_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 5, 10, 3)
)
_X25protocolCcittV1988_ObjectIdentity = ObjectIdentity
x25protocolCcittV1988 = _X25protocolCcittV1988_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 5, 10, 4)
)
_X25protocolIso8208V1987_ObjectIdentity = ObjectIdentity
x25protocolIso8208V1987 = _X25protocolIso8208V1987_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 5, 10, 5)
)
_X25protocolIso8208V1989_ObjectIdentity = ObjectIdentity
x25protocolIso8208V1989 = _X25protocolIso8208V1989_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 5, 10, 6)
)

# Managed Objects groups


# Notification objects

x25Restart = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 5, 0, 1)
)
x25Restart.setObjects(
    ("RFC1382-MIB", "x25OperIndex")
)
if mibBuilder.loadTexts:
    x25Restart.setStatus(
        ""
    )

x25Reset = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 5, 0, 2)
)
x25Reset.setObjects(
      *(("RFC1382-MIB", "x25CircuitIndex"),
        ("RFC1382-MIB", "x25CircuitChannel"))
)
if mibBuilder.loadTexts:
    x25Reset.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1382-MIB",
    **{"X121Address": X121Address,
       "x25": x25,
       "x25Restart": x25Restart,
       "x25Reset": x25Reset,
       "x25AdmnTable": x25AdmnTable,
       "x25AdmnEntry": x25AdmnEntry,
       "x25AdmnIndex": x25AdmnIndex,
       "x25AdmnInterfaceMode": x25AdmnInterfaceMode,
       "x25AdmnMaxActiveCircuits": x25AdmnMaxActiveCircuits,
       "x25AdmnPacketSequencing": x25AdmnPacketSequencing,
       "x25AdmnRestartTimer": x25AdmnRestartTimer,
       "x25AdmnCallTimer": x25AdmnCallTimer,
       "x25AdmnResetTimer": x25AdmnResetTimer,
       "x25AdmnClearTimer": x25AdmnClearTimer,
       "x25AdmnWindowTimer": x25AdmnWindowTimer,
       "x25AdmnDataRxmtTimer": x25AdmnDataRxmtTimer,
       "x25AdmnInterruptTimer": x25AdmnInterruptTimer,
       "x25AdmnRejectTimer": x25AdmnRejectTimer,
       "x25AdmnRegistrationRequestTimer": x25AdmnRegistrationRequestTimer,
       "x25AdmnMinimumRecallTimer": x25AdmnMinimumRecallTimer,
       "x25AdmnRestartCount": x25AdmnRestartCount,
       "x25AdmnResetCount": x25AdmnResetCount,
       "x25AdmnClearCount": x25AdmnClearCount,
       "x25AdmnDataRxmtCount": x25AdmnDataRxmtCount,
       "x25AdmnRejectCount": x25AdmnRejectCount,
       "x25AdmnRegistrationRequestCount": x25AdmnRegistrationRequestCount,
       "x25AdmnNumberPVCs": x25AdmnNumberPVCs,
       "x25AdmnDefCallParamId": x25AdmnDefCallParamId,
       "x25AdmnLocalAddress": x25AdmnLocalAddress,
       "x25AdmnProtocolVersionSupported": x25AdmnProtocolVersionSupported,
       "x25OperTable": x25OperTable,
       "x25OperEntry": x25OperEntry,
       "x25OperIndex": x25OperIndex,
       "x25OperInterfaceMode": x25OperInterfaceMode,
       "x25OperMaxActiveCircuits": x25OperMaxActiveCircuits,
       "x25OperPacketSequencing": x25OperPacketSequencing,
       "x25OperRestartTimer": x25OperRestartTimer,
       "x25OperCallTimer": x25OperCallTimer,
       "x25OperResetTimer": x25OperResetTimer,
       "x25OperClearTimer": x25OperClearTimer,
       "x25OperWindowTimer": x25OperWindowTimer,
       "x25OperDataRxmtTimer": x25OperDataRxmtTimer,
       "x25OperInterruptTimer": x25OperInterruptTimer,
       "x25OperRejectTimer": x25OperRejectTimer,
       "x25OperRegistrationRequestTimer": x25OperRegistrationRequestTimer,
       "x25OperMinimumRecallTimer": x25OperMinimumRecallTimer,
       "x25OperRestartCount": x25OperRestartCount,
       "x25OperResetCount": x25OperResetCount,
       "x25OperClearCount": x25OperClearCount,
       "x25OperDataRxmtCount": x25OperDataRxmtCount,
       "x25OperRejectCount": x25OperRejectCount,
       "x25OperRegistrationRequestCount": x25OperRegistrationRequestCount,
       "x25OperNumberPVCs": x25OperNumberPVCs,
       "x25OperDefCallParamId": x25OperDefCallParamId,
       "x25OperLocalAddress": x25OperLocalAddress,
       "x25OperDataLinkId": x25OperDataLinkId,
       "x25OperProtocolVersionSupported": x25OperProtocolVersionSupported,
       "x25StatTable": x25StatTable,
       "x25StatEntry": x25StatEntry,
       "x25StatIndex": x25StatIndex,
       "x25StatInCalls": x25StatInCalls,
       "x25StatInCallRefusals": x25StatInCallRefusals,
       "x25StatInProviderInitiatedClears": x25StatInProviderInitiatedClears,
       "x25StatInRemotelyInitiatedResets": x25StatInRemotelyInitiatedResets,
       "x25StatInProviderInitiatedResets": x25StatInProviderInitiatedResets,
       "x25StatInRestarts": x25StatInRestarts,
       "x25StatInDataPackets": x25StatInDataPackets,
       "x25StatInAccusedOfProtocolErrors": x25StatInAccusedOfProtocolErrors,
       "x25StatInInterrupts": x25StatInInterrupts,
       "x25StatOutCallAttempts": x25StatOutCallAttempts,
       "x25StatOutCallFailures": x25StatOutCallFailures,
       "x25StatOutInterrupts": x25StatOutInterrupts,
       "x25StatOutDataPackets": x25StatOutDataPackets,
       "x25StatOutgoingCircuits": x25StatOutgoingCircuits,
       "x25StatIncomingCircuits": x25StatIncomingCircuits,
       "x25StatTwowayCircuits": x25StatTwowayCircuits,
       "x25StatRestartTimeouts": x25StatRestartTimeouts,
       "x25StatCallTimeouts": x25StatCallTimeouts,
       "x25StatResetTimeouts": x25StatResetTimeouts,
       "x25StatClearTimeouts": x25StatClearTimeouts,
       "x25StatDataRxmtTimeouts": x25StatDataRxmtTimeouts,
       "x25StatInterruptTimeouts": x25StatInterruptTimeouts,
       "x25StatRetryCountExceededs": x25StatRetryCountExceededs,
       "x25StatClearCountExceededs": x25StatClearCountExceededs,
       "x25ChannelTable": x25ChannelTable,
       "x25ChannelEntry": x25ChannelEntry,
       "x25ChannelIndex": x25ChannelIndex,
       "x25ChannelLIC": x25ChannelLIC,
       "x25ChannelHIC": x25ChannelHIC,
       "x25ChannelLTC": x25ChannelLTC,
       "x25ChannelHTC": x25ChannelHTC,
       "x25ChannelLOC": x25ChannelLOC,
       "x25ChannelHOC": x25ChannelHOC,
       "x25CircuitTable": x25CircuitTable,
       "x25CircuitEntry": x25CircuitEntry,
       "x25CircuitIndex": x25CircuitIndex,
       "x25CircuitChannel": x25CircuitChannel,
       "x25CircuitStatus": x25CircuitStatus,
       "x25CircuitEstablishTime": x25CircuitEstablishTime,
       "x25CircuitDirection": x25CircuitDirection,
       "x25CircuitInOctets": x25CircuitInOctets,
       "x25CircuitInPdus": x25CircuitInPdus,
       "x25CircuitInRemotelyInitiatedResets": x25CircuitInRemotelyInitiatedResets,
       "x25CircuitInProviderInitiatedResets": x25CircuitInProviderInitiatedResets,
       "x25CircuitInInterrupts": x25CircuitInInterrupts,
       "x25CircuitOutOctets": x25CircuitOutOctets,
       "x25CircuitOutPdus": x25CircuitOutPdus,
       "x25CircuitOutInterrupts": x25CircuitOutInterrupts,
       "x25CircuitDataRetransmissionTimeouts": x25CircuitDataRetransmissionTimeouts,
       "x25CircuitResetTimeouts": x25CircuitResetTimeouts,
       "x25CircuitInterruptTimeouts": x25CircuitInterruptTimeouts,
       "x25CircuitCallParamId": x25CircuitCallParamId,
       "x25CircuitCalledDteAddress": x25CircuitCalledDteAddress,
       "x25CircuitCallingDteAddress": x25CircuitCallingDteAddress,
       "x25CircuitOriginallyCalledAddress": x25CircuitOriginallyCalledAddress,
       "x25CircuitDescr": x25CircuitDescr,
       "x25ClearedCircuitEntriesRequested": x25ClearedCircuitEntriesRequested,
       "x25ClearedCircuitEntriesGranted": x25ClearedCircuitEntriesGranted,
       "x25ClearedCircuitTable": x25ClearedCircuitTable,
       "x25ClearedCircuitEntry": x25ClearedCircuitEntry,
       "x25ClearedCircuitIndex": x25ClearedCircuitIndex,
       "x25ClearedCircuitPleIndex": x25ClearedCircuitPleIndex,
       "x25ClearedCircuitTimeEstablished": x25ClearedCircuitTimeEstablished,
       "x25ClearedCircuitTimeCleared": x25ClearedCircuitTimeCleared,
       "x25ClearedCircuitChannel": x25ClearedCircuitChannel,
       "x25ClearedCircuitClearingCause": x25ClearedCircuitClearingCause,
       "x25ClearedCircuitDiagnosticCode": x25ClearedCircuitDiagnosticCode,
       "x25ClearedCircuitInPdus": x25ClearedCircuitInPdus,
       "x25ClearedCircuitOutPdus": x25ClearedCircuitOutPdus,
       "x25ClearedCircuitCalledAddress": x25ClearedCircuitCalledAddress,
       "x25ClearedCircuitCallingAddress": x25ClearedCircuitCallingAddress,
       "x25ClearedCircuitClearFacilities": x25ClearedCircuitClearFacilities,
       "x25CallParmTable": x25CallParmTable,
       "x25CallParmEntry": x25CallParmEntry,
       "x25CallParmIndex": x25CallParmIndex,
       "x25CallParmStatus": x25CallParmStatus,
       "x25CallParmRefCount": x25CallParmRefCount,
       "x25CallParmInPacketSize": x25CallParmInPacketSize,
       "x25CallParmOutPacketSize": x25CallParmOutPacketSize,
       "x25CallParmInWindowSize": x25CallParmInWindowSize,
       "x25CallParmOutWindowSize": x25CallParmOutWindowSize,
       "x25CallParmAcceptReverseCharging": x25CallParmAcceptReverseCharging,
       "x25CallParmProposeReverseCharging": x25CallParmProposeReverseCharging,
       "x25CallParmFastSelect": x25CallParmFastSelect,
       "x25CallParmInThruPutClasSize": x25CallParmInThruPutClasSize,
       "x25CallParmOutThruPutClasSize": x25CallParmOutThruPutClasSize,
       "x25CallParmCug": x25CallParmCug,
       "x25CallParmCugoa": x25CallParmCugoa,
       "x25CallParmBcug": x25CallParmBcug,
       "x25CallParmNui": x25CallParmNui,
       "x25CallParmChargingInfo": x25CallParmChargingInfo,
       "x25CallParmRpoa": x25CallParmRpoa,
       "x25CallParmTrnstDly": x25CallParmTrnstDly,
       "x25CallParmCallingExt": x25CallParmCallingExt,
       "x25CallParmCalledExt": x25CallParmCalledExt,
       "x25CallParmInMinThuPutCls": x25CallParmInMinThuPutCls,
       "x25CallParmOutMinThuPutCls": x25CallParmOutMinThuPutCls,
       "x25CallParmEndTrnsDly": x25CallParmEndTrnsDly,
       "x25CallParmPriority": x25CallParmPriority,
       "x25CallParmProtection": x25CallParmProtection,
       "x25CallParmExptData": x25CallParmExptData,
       "x25CallParmUserData": x25CallParmUserData,
       "x25CallParmCallingNetworkFacilities": x25CallParmCallingNetworkFacilities,
       "x25CallParmCalledNetworkFacilities": x25CallParmCalledNetworkFacilities,
       "x25ProtocolVersion": x25ProtocolVersion,
       "x25protocolCcittV1976": x25protocolCcittV1976,
       "x25protocolCcittV1980": x25protocolCcittV1980,
       "x25protocolCcittV1984": x25protocolCcittV1984,
       "x25protocolCcittV1988": x25protocolCcittV1988,
       "x25protocolIso8208V1987": x25protocolIso8208V1987,
       "x25protocolIso8208V1989": x25protocolIso8208V1989}
)
