# SNMP MIB module (X25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/X25-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:37 2024
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

(rs232PortIndex,) = mibBuilder.importSymbols(
    "RS232-MIB",
    "rs232PortIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class X25CallParamIndex(Integer32):
    """Custom type X25CallParamIndex based on Integer32"""




class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""




class X121Address(OctetString):
    """Custom type X121Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ngcan_ObjectIdentity = ObjectIdentity
ngcan = _Ngcan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978)
)
_Tiger_ObjectIdentity = ObjectIdentity
tiger = _Tiger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2)
)
_X25MIB_ObjectIdentity = ObjectIdentity
x25MIB = _X25MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14)
)
_X25L3_ObjectIdentity = ObjectIdentity
x25L3 = _X25L3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1)
)
_X25AdmnTable_Object = MibTable
x25AdmnTable = _X25AdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    x25AdmnTable.setStatus("mandatory")
_X25AdmnEntry_Object = MibTableRow
x25AdmnEntry = _X25AdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1)
)
x25AdmnEntry.setIndexNames(
    (0, "X25-MIB", "x25AdmnIndex"),
)
if mibBuilder.loadTexts:
    x25AdmnEntry.setStatus("mandatory")
_X25AdmnIndex_Type = InterfaceIndex
_X25AdmnIndex_Object = MibTableColumn
x25AdmnIndex = _X25AdmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 1),
    _X25AdmnIndex_Type()
)
x25AdmnIndex.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 2),
    _X25AdmnInterfaceMode_Type()
)
x25AdmnInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnInterfaceMode.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 3),
    _X25AdmnPacketSequencing_Type()
)
x25AdmnPacketSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnPacketSequencing.setStatus("mandatory")


class _X25AdmnRestartTimer_Type(Integer32):
    """Custom type x25AdmnRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320000),
    )


_X25AdmnRestartTimer_Type.__name__ = "Integer32"
_X25AdmnRestartTimer_Object = MibTableColumn
x25AdmnRestartTimer = _X25AdmnRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 4),
    _X25AdmnRestartTimer_Type()
)
x25AdmnRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRestartTimer.setStatus("mandatory")


class _X25AdmnCallTimer_Type(Integer32):
    """Custom type x25AdmnCallTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320000),
    )


_X25AdmnCallTimer_Type.__name__ = "Integer32"
_X25AdmnCallTimer_Object = MibTableColumn
x25AdmnCallTimer = _X25AdmnCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 5),
    _X25AdmnCallTimer_Type()
)
x25AdmnCallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnCallTimer.setStatus("mandatory")


class _X25AdmnResetTimer_Type(Integer32):
    """Custom type x25AdmnResetTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320000),
    )


_X25AdmnResetTimer_Type.__name__ = "Integer32"
_X25AdmnResetTimer_Object = MibTableColumn
x25AdmnResetTimer = _X25AdmnResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 6),
    _X25AdmnResetTimer_Type()
)
x25AdmnResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnResetTimer.setStatus("mandatory")


class _X25AdmnClearTimer_Type(Integer32):
    """Custom type x25AdmnClearTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320000),
    )


_X25AdmnClearTimer_Type.__name__ = "Integer32"
_X25AdmnClearTimer_Object = MibTableColumn
x25AdmnClearTimer = _X25AdmnClearTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 7),
    _X25AdmnClearTimer_Type()
)
x25AdmnClearTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnClearTimer.setStatus("mandatory")


class _X25AdmnWindowTimer_Type(Integer32):
    """Custom type x25AdmnWindowTimer based on Integer32"""
    defaultValue = 60000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320000),
    )


_X25AdmnWindowTimer_Type.__name__ = "Integer32"
_X25AdmnWindowTimer_Object = MibTableColumn
x25AdmnWindowTimer = _X25AdmnWindowTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 8),
    _X25AdmnWindowTimer_Type()
)
x25AdmnWindowTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnWindowTimer.setStatus("mandatory")


class _X25AdmnDataRxmtTimer_Type(Integer32):
    """Custom type x25AdmnDataRxmtTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320000),
    )


_X25AdmnDataRxmtTimer_Type.__name__ = "Integer32"
_X25AdmnDataRxmtTimer_Object = MibTableColumn
x25AdmnDataRxmtTimer = _X25AdmnDataRxmtTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 9),
    _X25AdmnDataRxmtTimer_Type()
)
x25AdmnDataRxmtTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnDataRxmtTimer.setStatus("mandatory")


class _X25AdmnInterruptTimer_Type(Integer32):
    """Custom type x25AdmnInterruptTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320000),
    )


_X25AdmnInterruptTimer_Type.__name__ = "Integer32"
_X25AdmnInterruptTimer_Object = MibTableColumn
x25AdmnInterruptTimer = _X25AdmnInterruptTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 10),
    _X25AdmnInterruptTimer_Type()
)
x25AdmnInterruptTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnInterruptTimer.setStatus("mandatory")


class _X25AdmnRejectTimer_Type(Integer32):
    """Custom type x25AdmnRejectTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320000),
    )


_X25AdmnRejectTimer_Type.__name__ = "Integer32"
_X25AdmnRejectTimer_Object = MibTableColumn
x25AdmnRejectTimer = _X25AdmnRejectTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 11),
    _X25AdmnRejectTimer_Type()
)
x25AdmnRejectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRejectTimer.setStatus("mandatory")


class _X25AdmnRegistrationRequestTimer_Type(Integer32):
    """Custom type x25AdmnRegistrationRequestTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320000),
    )


_X25AdmnRegistrationRequestTimer_Type.__name__ = "Integer32"
_X25AdmnRegistrationRequestTimer_Object = MibTableColumn
x25AdmnRegistrationRequestTimer = _X25AdmnRegistrationRequestTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 12),
    _X25AdmnRegistrationRequestTimer_Type()
)
x25AdmnRegistrationRequestTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRegistrationRequestTimer.setStatus("mandatory")


class _X25AdmnRestartCount_Type(Integer32):
    """Custom type x25AdmnRestartCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_X25AdmnRestartCount_Type.__name__ = "Integer32"
_X25AdmnRestartCount_Object = MibTableColumn
x25AdmnRestartCount = _X25AdmnRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 13),
    _X25AdmnRestartCount_Type()
)
x25AdmnRestartCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRestartCount.setStatus("mandatory")


class _X25AdmnResetCount_Type(Integer32):
    """Custom type x25AdmnResetCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_X25AdmnResetCount_Type.__name__ = "Integer32"
_X25AdmnResetCount_Object = MibTableColumn
x25AdmnResetCount = _X25AdmnResetCount_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 14),
    _X25AdmnResetCount_Type()
)
x25AdmnResetCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnResetCount.setStatus("mandatory")


class _X25AdmnClearCount_Type(Integer32):
    """Custom type x25AdmnClearCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_X25AdmnClearCount_Type.__name__ = "Integer32"
_X25AdmnClearCount_Object = MibTableColumn
x25AdmnClearCount = _X25AdmnClearCount_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 15),
    _X25AdmnClearCount_Type()
)
x25AdmnClearCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnClearCount.setStatus("mandatory")


class _X25AdmnDataRxmtCount_Type(Integer32):
    """Custom type x25AdmnDataRxmtCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_X25AdmnDataRxmtCount_Type.__name__ = "Integer32"
_X25AdmnDataRxmtCount_Object = MibTableColumn
x25AdmnDataRxmtCount = _X25AdmnDataRxmtCount_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 16),
    _X25AdmnDataRxmtCount_Type()
)
x25AdmnDataRxmtCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnDataRxmtCount.setStatus("mandatory")


class _X25AdmnRejectCount_Type(Integer32):
    """Custom type x25AdmnRejectCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_X25AdmnRejectCount_Type.__name__ = "Integer32"
_X25AdmnRejectCount_Object = MibTableColumn
x25AdmnRejectCount = _X25AdmnRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 17),
    _X25AdmnRejectCount_Type()
)
x25AdmnRejectCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRejectCount.setStatus("mandatory")


class _X25AdmnRegistrationRequestCount_Type(Integer32):
    """Custom type x25AdmnRegistrationRequestCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_X25AdmnRegistrationRequestCount_Type.__name__ = "Integer32"
_X25AdmnRegistrationRequestCount_Object = MibTableColumn
x25AdmnRegistrationRequestCount = _X25AdmnRegistrationRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 19),
    _X25AdmnNumberPVCs_Type()
)
x25AdmnNumberPVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnNumberPVCs.setStatus("mandatory")
_X25AdmnDefCallParamId_Type = X25CallParamIndex
_X25AdmnDefCallParamId_Object = MibTableColumn
x25AdmnDefCallParamId = _X25AdmnDefCallParamId_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 20),
    _X25AdmnDefCallParamId_Type()
)
x25AdmnDefCallParamId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnDefCallParamId.setStatus("mandatory")


class _X25AdmnProtocolVersionSupported_Type(Integer32):
    """Custom type x25AdmnProtocolVersionSupported based on Integer32"""
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
        *(("ccitt-1976", 1),
          ("ccitt-1980", 2),
          ("ccitt-1984", 3),
          ("ccitt-1988", 4),
          ("ccitt-1992", 5),
          ("qllc", 6))
    )


_X25AdmnProtocolVersionSupported_Type.__name__ = "Integer32"
_X25AdmnProtocolVersionSupported_Object = MibTableColumn
x25AdmnProtocolVersionSupported = _X25AdmnProtocolVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 21),
    _X25AdmnProtocolVersionSupported_Type()
)
x25AdmnProtocolVersionSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnProtocolVersionSupported.setStatus("mandatory")


class _X25AdmnRegistrationMode_Type(Integer32):
    """Custom type x25AdmnRegistrationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("none", 1),
          ("user", 3))
    )


_X25AdmnRegistrationMode_Type.__name__ = "Integer32"
_X25AdmnRegistrationMode_Object = MibTableColumn
x25AdmnRegistrationMode = _X25AdmnRegistrationMode_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 22),
    _X25AdmnRegistrationMode_Type()
)
x25AdmnRegistrationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRegistrationMode.setStatus("mandatory")


class _X25AdmnDiagnosticMode_Type(Integer32):
    """Custom type x25AdmnDiagnosticMode based on Integer32"""
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
        *(("off", 3),
          ("on", 2),
          ("standard", 1))
    )


_X25AdmnDiagnosticMode_Type.__name__ = "Integer32"
_X25AdmnDiagnosticMode_Object = MibTableColumn
x25AdmnDiagnosticMode = _X25AdmnDiagnosticMode_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 23),
    _X25AdmnDiagnosticMode_Type()
)
x25AdmnDiagnosticMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnDiagnosticMode.setStatus("mandatory")


class _X25AdmnInterruptSize_Type(Integer32):
    """Custom type x25AdmnInterruptSize based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_X25AdmnInterruptSize_Type.__name__ = "Integer32"
_X25AdmnInterruptSize_Object = MibTableColumn
x25AdmnInterruptSize = _X25AdmnInterruptSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 24),
    _X25AdmnInterruptSize_Type()
)
x25AdmnInterruptSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnInterruptSize.setStatus("mandatory")


class _X25AdmnMaxTxWindow_Type(Integer32):
    """Custom type x25AdmnMaxTxWindow based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_X25AdmnMaxTxWindow_Type.__name__ = "Integer32"
_X25AdmnMaxTxWindow_Object = MibTableColumn
x25AdmnMaxTxWindow = _X25AdmnMaxTxWindow_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 25),
    _X25AdmnMaxTxWindow_Type()
)
x25AdmnMaxTxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnMaxTxWindow.setStatus("mandatory")


class _X25AdmnMaxRxWindow_Type(Integer32):
    """Custom type x25AdmnMaxRxWindow based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_X25AdmnMaxRxWindow_Type.__name__ = "Integer32"
_X25AdmnMaxRxWindow_Object = MibTableColumn
x25AdmnMaxRxWindow = _X25AdmnMaxRxWindow_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 26),
    _X25AdmnMaxRxWindow_Type()
)
x25AdmnMaxRxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnMaxRxWindow.setStatus("mandatory")


class _X25AdmnFacilityLength_Type(Integer32):
    """Custom type x25AdmnFacilityLength based on Integer32"""
    defaultValue = 109

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25AdmnFacilityLength_Type.__name__ = "Integer32"
_X25AdmnFacilityLength_Object = MibTableColumn
x25AdmnFacilityLength = _X25AdmnFacilityLength_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 27),
    _X25AdmnFacilityLength_Type()
)
x25AdmnFacilityLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnFacilityLength.setStatus("mandatory")


class _X25AdmnCallDataSize_Type(Integer32):
    """Custom type x25AdmnCallDataSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25AdmnCallDataSize_Type.__name__ = "Integer32"
_X25AdmnCallDataSize_Object = MibTableColumn
x25AdmnCallDataSize = _X25AdmnCallDataSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 28),
    _X25AdmnCallDataSize_Type()
)
x25AdmnCallDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnCallDataSize.setStatus("mandatory")


class _X25AdmnFastSelectCallDataSize_Type(Integer32):
    """Custom type x25AdmnFastSelectCallDataSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25AdmnFastSelectCallDataSize_Type.__name__ = "Integer32"
_X25AdmnFastSelectCallDataSize_Object = MibTableColumn
x25AdmnFastSelectCallDataSize = _X25AdmnFastSelectCallDataSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 29),
    _X25AdmnFastSelectCallDataSize_Type()
)
x25AdmnFastSelectCallDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnFastSelectCallDataSize.setStatus("mandatory")


class _X25AdmnExtendedClear_Type(Integer32):
    """Custom type x25AdmnExtendedClear based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("convert", 3),
          ("off", 1),
          ("on", 2))
    )


_X25AdmnExtendedClear_Type.__name__ = "Integer32"
_X25AdmnExtendedClear_Object = MibTableColumn
x25AdmnExtendedClear = _X25AdmnExtendedClear_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 30),
    _X25AdmnExtendedClear_Type()
)
x25AdmnExtendedClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnExtendedClear.setStatus("mandatory")


class _X25AdmnCause_Type(Integer32):
    """Custom type x25AdmnCause based on Integer32"""
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
        *(("asis", 1),
          ("ccitt-80", 2),
          ("ccitt-84", 3),
          ("clear", 4))
    )


_X25AdmnCause_Type.__name__ = "Integer32"
_X25AdmnCause_Object = MibTableColumn
x25AdmnCause = _X25AdmnCause_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 31),
    _X25AdmnCause_Type()
)
x25AdmnCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnCause.setStatus("mandatory")


class _X25AdmnABit_Type(Integer32):
    """Custom type x25AdmnABit based on Integer32"""
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
        *(("off", 2),
          ("ok", 3),
          ("on", 1))
    )


_X25AdmnABit_Type.__name__ = "Integer32"
_X25AdmnABit_Object = MibTableColumn
x25AdmnABit = _X25AdmnABit_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 32),
    _X25AdmnABit_Type()
)
x25AdmnABit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnABit.setStatus("mandatory")


class _X25AdmnRRTrigger_Type(Integer32):
    """Custom type x25AdmnRRTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_X25AdmnRRTrigger_Type.__name__ = "Integer32"
_X25AdmnRRTrigger_Object = MibTableColumn
x25AdmnRRTrigger = _X25AdmnRRTrigger_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 33),
    _X25AdmnRRTrigger_Type()
)
x25AdmnRRTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRRTrigger.setStatus("mandatory")


class _X25AdmnRRTimer_Type(Integer32):
    """Custom type x25AdmnRRTimer based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320000),
    )


_X25AdmnRRTimer_Type.__name__ = "Integer32"
_X25AdmnRRTimer_Object = MibTableColumn
x25AdmnRRTimer = _X25AdmnRRTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 34),
    _X25AdmnRRTimer_Type()
)
x25AdmnRRTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRRTimer.setStatus("mandatory")


class _X25AdmnRRPiggy_Type(Integer32):
    """Custom type x25AdmnRRPiggy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_X25AdmnRRPiggy_Type.__name__ = "Integer32"
_X25AdmnRRPiggy_Object = MibTableColumn
x25AdmnRRPiggy = _X25AdmnRRPiggy_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 35),
    _X25AdmnRRPiggy_Type()
)
x25AdmnRRPiggy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRRPiggy.setStatus("mandatory")


class _X25AdmnTxRejectMode_Type(Integer32):
    """Custom type x25AdmnTxRejectMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rejectReset", 2),
          ("reset", 1),
          ("sendAlways", 3))
    )


_X25AdmnTxRejectMode_Type.__name__ = "Integer32"
_X25AdmnTxRejectMode_Object = MibTableColumn
x25AdmnTxRejectMode = _X25AdmnTxRejectMode_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 36),
    _X25AdmnTxRejectMode_Type()
)
x25AdmnTxRejectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnTxRejectMode.setStatus("mandatory")


class _X25AdmnRxRejectMode_Type(Integer32):
    """Custom type x25AdmnRxRejectMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("retxAlways", 3),
          ("retxReset", 2))
    )


_X25AdmnRxRejectMode_Type.__name__ = "Integer32"
_X25AdmnRxRejectMode_Object = MibTableColumn
x25AdmnRxRejectMode = _X25AdmnRxRejectMode_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 37),
    _X25AdmnRxRejectMode_Type()
)
x25AdmnRxRejectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnRxRejectMode.setStatus("mandatory")


class _X25AdmnDBit_Type(Integer32):
    """Custom type x25AdmnDBit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bill", 3),
          ("no", 1),
          ("ok", 2))
    )


_X25AdmnDBit_Type.__name__ = "Integer32"
_X25AdmnDBit_Object = MibTableColumn
x25AdmnDBit = _X25AdmnDBit_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 38),
    _X25AdmnDBit_Type()
)
x25AdmnDBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnDBit.setStatus("mandatory")


class _X25AdmnR28Action_Type(Integer32):
    """Custom type x25AdmnR28Action based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("ignore", 2))
    )


_X25AdmnR28Action_Type.__name__ = "Integer32"
_X25AdmnR28Action_Object = MibTableColumn
x25AdmnR28Action = _X25AdmnR28Action_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 39),
    _X25AdmnR28Action_Type()
)
x25AdmnR28Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdmnR28Action.setStatus("mandatory")


class _X25ChannelLIC_Type(Integer32):
    """Custom type x25ChannelLIC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelLIC_Type.__name__ = "Integer32"
_X25ChannelLIC_Object = MibTableColumn
x25ChannelLIC = _X25ChannelLIC_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 40),
    _X25ChannelLIC_Type()
)
x25ChannelLIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelLIC.setStatus("mandatory")


class _X25ChannelHIC_Type(Integer32):
    """Custom type x25ChannelHIC based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelHIC_Type.__name__ = "Integer32"
_X25ChannelHIC_Object = MibTableColumn
x25ChannelHIC = _X25ChannelHIC_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 41),
    _X25ChannelHIC_Type()
)
x25ChannelHIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelHIC.setStatus("mandatory")


class _X25ChannelLTC_Type(Integer32):
    """Custom type x25ChannelLTC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelLTC_Type.__name__ = "Integer32"
_X25ChannelLTC_Object = MibTableColumn
x25ChannelLTC = _X25ChannelLTC_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 42),
    _X25ChannelLTC_Type()
)
x25ChannelLTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelLTC.setStatus("mandatory")


class _X25ChannelHTC_Type(Integer32):
    """Custom type x25ChannelHTC based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelHTC_Type.__name__ = "Integer32"
_X25ChannelHTC_Object = MibTableColumn
x25ChannelHTC = _X25ChannelHTC_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 43),
    _X25ChannelHTC_Type()
)
x25ChannelHTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelHTC.setStatus("mandatory")


class _X25ChannelLOC_Type(Integer32):
    """Custom type x25ChannelLOC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelLOC_Type.__name__ = "Integer32"
_X25ChannelLOC_Object = MibTableColumn
x25ChannelLOC = _X25ChannelLOC_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 44),
    _X25ChannelLOC_Type()
)
x25ChannelLOC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelLOC.setStatus("mandatory")


class _X25ChannelHOC_Type(Integer32):
    """Custom type x25ChannelHOC based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25ChannelHOC_Type.__name__ = "Integer32"
_X25ChannelHOC_Object = MibTableColumn
x25ChannelHOC = _X25ChannelHOC_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 45),
    _X25ChannelHOC_Type()
)
x25ChannelHOC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ChannelHOC.setStatus("mandatory")
_X25StatInCalls_Type = Counter32
_X25StatInCalls_Object = MibTableColumn
x25StatInCalls = _X25StatInCalls_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 46),
    _X25StatInCalls_Type()
)
x25StatInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInCalls.setStatus("mandatory")
_X25StatInCallRefusals_Type = Counter32
_X25StatInCallRefusals_Object = MibTableColumn
x25StatInCallRefusals = _X25StatInCallRefusals_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 47),
    _X25StatInCallRefusals_Type()
)
x25StatInCallRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInCallRefusals.setStatus("mandatory")
_X25StatInProviderInitiatedClears_Type = Counter32
_X25StatInProviderInitiatedClears_Object = MibTableColumn
x25StatInProviderInitiatedClears = _X25StatInProviderInitiatedClears_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 48),
    _X25StatInProviderInitiatedClears_Type()
)
x25StatInProviderInitiatedClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInProviderInitiatedClears.setStatus("mandatory")
_X25StatInRemotelyInitiatedResets_Type = Counter32
_X25StatInRemotelyInitiatedResets_Object = MibTableColumn
x25StatInRemotelyInitiatedResets = _X25StatInRemotelyInitiatedResets_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 49),
    _X25StatInRemotelyInitiatedResets_Type()
)
x25StatInRemotelyInitiatedResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInRemotelyInitiatedResets.setStatus("mandatory")
_X25StatInProviderInitiatedResets_Type = Counter32
_X25StatInProviderInitiatedResets_Object = MibTableColumn
x25StatInProviderInitiatedResets = _X25StatInProviderInitiatedResets_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 50),
    _X25StatInProviderInitiatedResets_Type()
)
x25StatInProviderInitiatedResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInProviderInitiatedResets.setStatus("mandatory")
_X25StatInRestarts_Type = Counter32
_X25StatInRestarts_Object = MibTableColumn
x25StatInRestarts = _X25StatInRestarts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 51),
    _X25StatInRestarts_Type()
)
x25StatInRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInRestarts.setStatus("mandatory")
_X25StatInDataPackets_Type = Counter32
_X25StatInDataPackets_Object = MibTableColumn
x25StatInDataPackets = _X25StatInDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 52),
    _X25StatInDataPackets_Type()
)
x25StatInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInDataPackets.setStatus("mandatory")
_X25StatInAccusedOfProtocolErrors_Type = Counter32
_X25StatInAccusedOfProtocolErrors_Object = MibTableColumn
x25StatInAccusedOfProtocolErrors = _X25StatInAccusedOfProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 53),
    _X25StatInAccusedOfProtocolErrors_Type()
)
x25StatInAccusedOfProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInAccusedOfProtocolErrors.setStatus("mandatory")
_X25StatInInterrupts_Type = Counter32
_X25StatInInterrupts_Object = MibTableColumn
x25StatInInterrupts = _X25StatInInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 54),
    _X25StatInInterrupts_Type()
)
x25StatInInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInInterrupts.setStatus("mandatory")
_X25StatOutCallAttempts_Type = Counter32
_X25StatOutCallAttempts_Object = MibTableColumn
x25StatOutCallAttempts = _X25StatOutCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 55),
    _X25StatOutCallAttempts_Type()
)
x25StatOutCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatOutCallAttempts.setStatus("mandatory")
_X25StatOutCallFailures_Type = Counter32
_X25StatOutCallFailures_Object = MibTableColumn
x25StatOutCallFailures = _X25StatOutCallFailures_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 56),
    _X25StatOutCallFailures_Type()
)
x25StatOutCallFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatOutCallFailures.setStatus("mandatory")
_X25StatOutInterrupts_Type = Counter32
_X25StatOutInterrupts_Object = MibTableColumn
x25StatOutInterrupts = _X25StatOutInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 57),
    _X25StatOutInterrupts_Type()
)
x25StatOutInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatOutInterrupts.setStatus("mandatory")
_X25StatOutDataPackets_Type = Counter32
_X25StatOutDataPackets_Object = MibTableColumn
x25StatOutDataPackets = _X25StatOutDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 58),
    _X25StatOutDataPackets_Type()
)
x25StatOutDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatOutDataPackets.setStatus("mandatory")
_X25StatPVCCircuits_Type = Counter32
_X25StatPVCCircuits_Object = MibTableColumn
x25StatPVCCircuits = _X25StatPVCCircuits_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 59),
    _X25StatPVCCircuits_Type()
)
x25StatPVCCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatPVCCircuits.setStatus("mandatory")
_X25StatSVCCircuits_Type = Counter32
_X25StatSVCCircuits_Object = MibTableColumn
x25StatSVCCircuits = _X25StatSVCCircuits_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 60),
    _X25StatSVCCircuits_Type()
)
x25StatSVCCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatSVCCircuits.setStatus("mandatory")
_X25StatRestartTimeouts_Type = Counter32
_X25StatRestartTimeouts_Object = MibTableColumn
x25StatRestartTimeouts = _X25StatRestartTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 61),
    _X25StatRestartTimeouts_Type()
)
x25StatRestartTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatRestartTimeouts.setStatus("mandatory")
_X25StatCallTimeouts_Type = Counter32
_X25StatCallTimeouts_Object = MibTableColumn
x25StatCallTimeouts = _X25StatCallTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 62),
    _X25StatCallTimeouts_Type()
)
x25StatCallTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatCallTimeouts.setStatus("mandatory")
_X25StatResetTimeouts_Type = Counter32
_X25StatResetTimeouts_Object = MibTableColumn
x25StatResetTimeouts = _X25StatResetTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 63),
    _X25StatResetTimeouts_Type()
)
x25StatResetTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatResetTimeouts.setStatus("mandatory")
_X25StatClearTimeouts_Type = Counter32
_X25StatClearTimeouts_Object = MibTableColumn
x25StatClearTimeouts = _X25StatClearTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 64),
    _X25StatClearTimeouts_Type()
)
x25StatClearTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatClearTimeouts.setStatus("mandatory")
_X25StatDataRxmtTimeouts_Type = Counter32
_X25StatDataRxmtTimeouts_Object = MibTableColumn
x25StatDataRxmtTimeouts = _X25StatDataRxmtTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 65),
    _X25StatDataRxmtTimeouts_Type()
)
x25StatDataRxmtTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatDataRxmtTimeouts.setStatus("mandatory")
_X25StatInterruptTimeouts_Type = Counter32
_X25StatInterruptTimeouts_Object = MibTableColumn
x25StatInterruptTimeouts = _X25StatInterruptTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 66),
    _X25StatInterruptTimeouts_Type()
)
x25StatInterruptTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatInterruptTimeouts.setStatus("mandatory")
_X25StatRetryCountExceededs_Type = Counter32
_X25StatRetryCountExceededs_Object = MibTableColumn
x25StatRetryCountExceededs = _X25StatRetryCountExceededs_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 67),
    _X25StatRetryCountExceededs_Type()
)
x25StatRetryCountExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatRetryCountExceededs.setStatus("mandatory")
_X25StatClearCountExceededs_Type = Counter32
_X25StatClearCountExceededs_Object = MibTableColumn
x25StatClearCountExceededs = _X25StatClearCountExceededs_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 68),
    _X25StatClearCountExceededs_Type()
)
x25StatClearCountExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatClearCountExceededs.setStatus("mandatory")


class _X25AdminTrapControl_Type(Integer32):
    """Custom type x25AdminTrapControl based on Integer32"""
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


_X25AdminTrapControl_Type.__name__ = "Integer32"
_X25AdminTrapControl_Object = MibTableColumn
x25AdminTrapControl = _X25AdminTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1, 69),
    _X25AdminTrapControl_Type()
)
x25AdminTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AdminTrapControl.setStatus("mandatory")
_X25CircuitTable_Object = MibTable
x25CircuitTable = _X25CircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    x25CircuitTable.setStatus("mandatory")
_X25CircuitEntry_Object = MibTableRow
x25CircuitEntry = _X25CircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1)
)
x25CircuitEntry.setIndexNames(
    (0, "X25-MIB", "x25CircuitIndex"),
    (0, "X25-MIB", "x25CircuitChannel"),
)
if mibBuilder.loadTexts:
    x25CircuitEntry.setStatus("mandatory")
_X25CircuitIndex_Type = InterfaceIndex
_X25CircuitIndex_Object = MibTableColumn
x25CircuitIndex = _X25CircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 2),
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("call-collision", 6),
          ("data", 9),
          ("data-unused", 5),
          ("inactive", 1),
          ("received-call", 3),
          ("sent-call", 4),
          ("sent-net-clear", 8),
          ("sent-net-reset", 11),
          ("sent-user-clear", 7),
          ("sent-user-reset", 10),
          ("wait-for-setup", 2))
    )


_X25CircuitStatus_Type.__name__ = "Integer32"
_X25CircuitStatus_Object = MibTableColumn
x25CircuitStatus = _X25CircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 3),
    _X25CircuitStatus_Type()
)
x25CircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitStatus.setStatus("mandatory")
_X25CircuitEstablishTime_Type = TimeTicks
_X25CircuitEstablishTime_Object = MibTableColumn
x25CircuitEstablishTime = _X25CircuitEstablishTime_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 5),
    _X25CircuitDirection_Type()
)
x25CircuitDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitDirection.setStatus("mandatory")
_X25CircuitInOctets_Type = Counter32
_X25CircuitInOctets_Object = MibTableColumn
x25CircuitInOctets = _X25CircuitInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 6),
    _X25CircuitInOctets_Type()
)
x25CircuitInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInOctets.setStatus("mandatory")
_X25CircuitInPdus_Type = Counter32
_X25CircuitInPdus_Object = MibTableColumn
x25CircuitInPdus = _X25CircuitInPdus_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 7),
    _X25CircuitInPdus_Type()
)
x25CircuitInPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInPdus.setStatus("mandatory")
_X25CircuitInRemotelyInitiatedResets_Type = Counter32
_X25CircuitInRemotelyInitiatedResets_Object = MibTableColumn
x25CircuitInRemotelyInitiatedResets = _X25CircuitInRemotelyInitiatedResets_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 8),
    _X25CircuitInRemotelyInitiatedResets_Type()
)
x25CircuitInRemotelyInitiatedResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInRemotelyInitiatedResets.setStatus("mandatory")
_X25CircuitInProviderInitiatedResets_Type = Counter32
_X25CircuitInProviderInitiatedResets_Object = MibTableColumn
x25CircuitInProviderInitiatedResets = _X25CircuitInProviderInitiatedResets_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 9),
    _X25CircuitInProviderInitiatedResets_Type()
)
x25CircuitInProviderInitiatedResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInProviderInitiatedResets.setStatus("mandatory")
_X25CircuitInInterrupts_Type = Counter32
_X25CircuitInInterrupts_Object = MibTableColumn
x25CircuitInInterrupts = _X25CircuitInInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 10),
    _X25CircuitInInterrupts_Type()
)
x25CircuitInInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInInterrupts.setStatus("mandatory")
_X25CircuitOutOctets_Type = Counter32
_X25CircuitOutOctets_Object = MibTableColumn
x25CircuitOutOctets = _X25CircuitOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 11),
    _X25CircuitOutOctets_Type()
)
x25CircuitOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitOutOctets.setStatus("mandatory")
_X25CircuitOutPdus_Type = Counter32
_X25CircuitOutPdus_Object = MibTableColumn
x25CircuitOutPdus = _X25CircuitOutPdus_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 12),
    _X25CircuitOutPdus_Type()
)
x25CircuitOutPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitOutPdus.setStatus("mandatory")
_X25CircuitOutInterrupts_Type = Counter32
_X25CircuitOutInterrupts_Object = MibTableColumn
x25CircuitOutInterrupts = _X25CircuitOutInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 13),
    _X25CircuitOutInterrupts_Type()
)
x25CircuitOutInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitOutInterrupts.setStatus("mandatory")
_X25CircuitDataRetransmissionTimeouts_Type = Counter32
_X25CircuitDataRetransmissionTimeouts_Object = MibTableColumn
x25CircuitDataRetransmissionTimeouts = _X25CircuitDataRetransmissionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 14),
    _X25CircuitDataRetransmissionTimeouts_Type()
)
x25CircuitDataRetransmissionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitDataRetransmissionTimeouts.setStatus("mandatory")
_X25CircuitResetTimeouts_Type = Counter32
_X25CircuitResetTimeouts_Object = MibTableColumn
x25CircuitResetTimeouts = _X25CircuitResetTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 15),
    _X25CircuitResetTimeouts_Type()
)
x25CircuitResetTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitResetTimeouts.setStatus("mandatory")
_X25CircuitInterruptTimeouts_Type = Counter32
_X25CircuitInterruptTimeouts_Object = MibTableColumn
x25CircuitInterruptTimeouts = _X25CircuitInterruptTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 16),
    _X25CircuitInterruptTimeouts_Type()
)
x25CircuitInterruptTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitInterruptTimeouts.setStatus("mandatory")
_X25CircuitCallParamId_Type = Integer32
_X25CircuitCallParamId_Object = MibTableColumn
x25CircuitCallParamId = _X25CircuitCallParamId_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 17),
    _X25CircuitCallParamId_Type()
)
x25CircuitCallParamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitCallParamId.setStatus("mandatory")


class _X25CircuitCalledAddress_Type(X121Address):
    """Custom type x25CircuitCalledAddress based on X121Address"""
    defaultHexValue = ""


_X25CircuitCalledAddress_Object = MibTableColumn
x25CircuitCalledAddress = _X25CircuitCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 18),
    _X25CircuitCalledAddress_Type()
)
x25CircuitCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitCalledAddress.setStatus("mandatory")


class _X25CircuitCallingAddress_Type(X121Address):
    """Custom type x25CircuitCallingAddress based on X121Address"""
    defaultHexValue = ""


_X25CircuitCallingAddress_Object = MibTableColumn
x25CircuitCallingAddress = _X25CircuitCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 19),
    _X25CircuitCallingAddress_Type()
)
x25CircuitCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitCallingAddress.setStatus("mandatory")


class _X25CircuitOriginallyCalledAddress_Type(X121Address):
    """Custom type x25CircuitOriginallyCalledAddress based on X121Address"""
    defaultHexValue = ""


_X25CircuitOriginallyCalledAddress_Object = MibTableColumn
x25CircuitOriginallyCalledAddress = _X25CircuitOriginallyCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 20),
    _X25CircuitOriginallyCalledAddress_Type()
)
x25CircuitOriginallyCalledAddress.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 21),
    _X25CircuitDescr_Type()
)
x25CircuitDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CircuitDescr.setStatus("mandatory")


class _X25CircuitRNRReceive_Type(Integer32):
    """Custom type x25CircuitRNRReceive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-rnr", 1),
          ("rnr", 2))
    )


_X25CircuitRNRReceive_Type.__name__ = "Integer32"
_X25CircuitRNRReceive_Object = MibTableColumn
x25CircuitRNRReceive = _X25CircuitRNRReceive_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 22),
    _X25CircuitRNRReceive_Type()
)
x25CircuitRNRReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitRNRReceive.setStatus("mandatory")


class _X25CircuitRNRSent_Type(Integer32):
    """Custom type x25CircuitRNRSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-rnr", 1),
          ("rnr", 2))
    )


_X25CircuitRNRSent_Type.__name__ = "Integer32"
_X25CircuitRNRSent_Object = MibTableColumn
x25CircuitRNRSent = _X25CircuitRNRSent_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 23),
    _X25CircuitRNRSent_Type()
)
x25CircuitRNRSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitRNRSent.setStatus("mandatory")


class _X25CircuitTrapType_Type(Integer32):
    """Custom type x25CircuitTrapType based on Integer32"""
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
        *(("clear", 2),
          ("recv-rnr2rr", 6),
          ("recv-rr2rnr", 5),
          ("reset", 1),
          ("sent-rnr2rr", 4),
          ("sent-rr2rnr", 3))
    )


_X25CircuitTrapType_Type.__name__ = "Integer32"
_X25CircuitTrapType_Object = MibTableColumn
x25CircuitTrapType = _X25CircuitTrapType_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 24),
    _X25CircuitTrapType_Type()
)
x25CircuitTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitTrapType.setStatus("mandatory")


class _X25CircuitTrapCause_Type(Integer32):
    """Custom type x25CircuitTrapCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_X25CircuitTrapCause_Type.__name__ = "Integer32"
_X25CircuitTrapCause_Object = MibTableColumn
x25CircuitTrapCause = _X25CircuitTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 25),
    _X25CircuitTrapCause_Type()
)
x25CircuitTrapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitTrapCause.setStatus("mandatory")


class _X25CircuitTrapDiagnostic_Type(Integer32):
    """Custom type x25CircuitTrapDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_X25CircuitTrapDiagnostic_Type.__name__ = "Integer32"
_X25CircuitTrapDiagnostic_Object = MibTableColumn
x25CircuitTrapDiagnostic = _X25CircuitTrapDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 2, 1, 26),
    _X25CircuitTrapDiagnostic_Type()
)
x25CircuitTrapDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CircuitTrapDiagnostic.setStatus("mandatory")
_X25CallParmTable_Object = MibTable
x25CallParmTable = _X25CallParmTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3)
)
if mibBuilder.loadTexts:
    x25CallParmTable.setStatus("mandatory")
_X25CallParmEntry_Object = MibTableRow
x25CallParmEntry = _X25CallParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1)
)
x25CallParmEntry.setIndexNames(
    (0, "X25-MIB", "x25CallParmIndex"),
)
if mibBuilder.loadTexts:
    x25CallParmEntry.setStatus("mandatory")
_X25CallParmIndex_Type = Integer32
_X25CallParmIndex_Object = MibTableColumn
x25CallParmIndex = _X25CallParmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 1),
    _X25CallParmIndex_Type()
)
x25CallParmIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmIndex.setStatus("mandatory")
_X25CallParmStatus_Type = RowStatus
_X25CallParmStatus_Object = MibTableColumn
x25CallParmStatus = _X25CallParmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 2),
    _X25CallParmStatus_Type()
)
x25CallParmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmStatus.setStatus("mandatory")
_X25CallParmRefCount_Type = Integer32
_X25CallParmRefCount_Object = MibTableColumn
x25CallParmRefCount = _X25CallParmRefCount_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 3),
    _X25CallParmRefCount_Type()
)
x25CallParmRefCount.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 7),
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
        *(("alwaysAccept", 2),
          ("alwaysRefuse", 3),
          ("default", 1),
          ("onlyIfNotBilled", 4))
    )


_X25CallParmAcceptReverseCharging_Type.__name__ = "Integer32"
_X25CallParmAcceptReverseCharging_Object = MibTableColumn
x25CallParmAcceptReverseCharging = _X25CallParmAcceptReverseCharging_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 9),
    _X25CallParmProposeReverseCharging_Type()
)
x25CallParmProposeReverseCharging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmProposeReverseCharging.setStatus("mandatory")


class _X25CallParmFastSelect_Type(Integer32):
    """Custom type x25CallParmFastSelect based on Integer32"""
    defaultValue = 2

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
        *(("alwaysAccept", 5),
          ("alwaysReject", 2),
          ("default", 1),
          ("onlyIfNotBilled", 6),
          ("onlyIncomming", 3),
          ("onlyOutgoing", 4))
    )


_X25CallParmFastSelect_Type.__name__ = "Integer32"
_X25CallParmFastSelect_Object = MibTableColumn
x25CallParmFastSelect = _X25CallParmFastSelect_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 22),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 25),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 26),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 27),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 28),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 29),
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
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 30),
    _X25CallParmCalledNetworkFacilities_Type()
)
x25CallParmCalledNetworkFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmCalledNetworkFacilities.setStatus("mandatory")


class _X25CallParmInMaxPktSize_Type(Integer32):
    """Custom type x25CallParmInMaxPktSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_X25CallParmInMaxPktSize_Type.__name__ = "Integer32"
_X25CallParmInMaxPktSize_Object = MibTableColumn
x25CallParmInMaxPktSize = _X25CallParmInMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 31),
    _X25CallParmInMaxPktSize_Type()
)
x25CallParmInMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmInMaxPktSize.setStatus("mandatory")


class _X25CallParmOutMaxPktSize_Type(Integer32):
    """Custom type x25CallParmOutMaxPktSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_X25CallParmOutMaxPktSize_Type.__name__ = "Integer32"
_X25CallParmOutMaxPktSize_Object = MibTableColumn
x25CallParmOutMaxPktSize = _X25CallParmOutMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 3, 1, 32),
    _X25CallParmOutMaxPktSize_Type()
)
x25CallParmOutMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CallParmOutMaxPktSize.setStatus("mandatory")
_X25Traps_ObjectIdentity = ObjectIdentity
x25Traps = _X25Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 2)
)
_X25L3Traps_ObjectIdentity = ObjectIdentity
x25L3Traps = _X25L3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 2, 1)
)

# Managed Objects groups


# Notification objects

x25Restart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 2, 1, 0, 1)
)
x25Restart.setObjects(
      *(("X25-MIB", "x25AdmnIndex"),
        ("RS232-MIB", "rs232PortIndex"))
)
if mibBuilder.loadTexts:
    x25Restart.setStatus(
        ""
    )

x25VC = NotificationType(
    (1, 3, 6, 1, 4, 1, 1978, 2, 14, 2, 1, 0, 2)
)
x25VC.setObjects(
      *(("X25-MIB", "x25CircuitIndex"),
        ("X25-MIB", "x25CircuitChannel"),
        ("X25-MIB", "x25CircuitTrapType"),
        ("X25-MIB", "x25CircuitTrapCause"),
        ("X25-MIB", "x25CircuitTrapDiagnostic"),
        ("RS232-MIB", "rs232PortIndex"))
)
if mibBuilder.loadTexts:
    x25VC.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "X25-MIB",
    **{"X25CallParamIndex": X25CallParamIndex,
       "InterfaceIndex": InterfaceIndex,
       "X121Address": X121Address,
       "ngcan": ngcan,
       "tiger": tiger,
       "x25MIB": x25MIB,
       "x25L3": x25L3,
       "x25AdmnTable": x25AdmnTable,
       "x25AdmnEntry": x25AdmnEntry,
       "x25AdmnIndex": x25AdmnIndex,
       "x25AdmnInterfaceMode": x25AdmnInterfaceMode,
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
       "x25AdmnRestartCount": x25AdmnRestartCount,
       "x25AdmnResetCount": x25AdmnResetCount,
       "x25AdmnClearCount": x25AdmnClearCount,
       "x25AdmnDataRxmtCount": x25AdmnDataRxmtCount,
       "x25AdmnRejectCount": x25AdmnRejectCount,
       "x25AdmnRegistrationRequestCount": x25AdmnRegistrationRequestCount,
       "x25AdmnNumberPVCs": x25AdmnNumberPVCs,
       "x25AdmnDefCallParamId": x25AdmnDefCallParamId,
       "x25AdmnProtocolVersionSupported": x25AdmnProtocolVersionSupported,
       "x25AdmnRegistrationMode": x25AdmnRegistrationMode,
       "x25AdmnDiagnosticMode": x25AdmnDiagnosticMode,
       "x25AdmnInterruptSize": x25AdmnInterruptSize,
       "x25AdmnMaxTxWindow": x25AdmnMaxTxWindow,
       "x25AdmnMaxRxWindow": x25AdmnMaxRxWindow,
       "x25AdmnFacilityLength": x25AdmnFacilityLength,
       "x25AdmnCallDataSize": x25AdmnCallDataSize,
       "x25AdmnFastSelectCallDataSize": x25AdmnFastSelectCallDataSize,
       "x25AdmnExtendedClear": x25AdmnExtendedClear,
       "x25AdmnCause": x25AdmnCause,
       "x25AdmnABit": x25AdmnABit,
       "x25AdmnRRTrigger": x25AdmnRRTrigger,
       "x25AdmnRRTimer": x25AdmnRRTimer,
       "x25AdmnRRPiggy": x25AdmnRRPiggy,
       "x25AdmnTxRejectMode": x25AdmnTxRejectMode,
       "x25AdmnRxRejectMode": x25AdmnRxRejectMode,
       "x25AdmnDBit": x25AdmnDBit,
       "x25AdmnR28Action": x25AdmnR28Action,
       "x25ChannelLIC": x25ChannelLIC,
       "x25ChannelHIC": x25ChannelHIC,
       "x25ChannelLTC": x25ChannelLTC,
       "x25ChannelHTC": x25ChannelHTC,
       "x25ChannelLOC": x25ChannelLOC,
       "x25ChannelHOC": x25ChannelHOC,
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
       "x25StatPVCCircuits": x25StatPVCCircuits,
       "x25StatSVCCircuits": x25StatSVCCircuits,
       "x25StatRestartTimeouts": x25StatRestartTimeouts,
       "x25StatCallTimeouts": x25StatCallTimeouts,
       "x25StatResetTimeouts": x25StatResetTimeouts,
       "x25StatClearTimeouts": x25StatClearTimeouts,
       "x25StatDataRxmtTimeouts": x25StatDataRxmtTimeouts,
       "x25StatInterruptTimeouts": x25StatInterruptTimeouts,
       "x25StatRetryCountExceededs": x25StatRetryCountExceededs,
       "x25StatClearCountExceededs": x25StatClearCountExceededs,
       "x25AdminTrapControl": x25AdminTrapControl,
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
       "x25CircuitCalledAddress": x25CircuitCalledAddress,
       "x25CircuitCallingAddress": x25CircuitCallingAddress,
       "x25CircuitOriginallyCalledAddress": x25CircuitOriginallyCalledAddress,
       "x25CircuitDescr": x25CircuitDescr,
       "x25CircuitRNRReceive": x25CircuitRNRReceive,
       "x25CircuitRNRSent": x25CircuitRNRSent,
       "x25CircuitTrapType": x25CircuitTrapType,
       "x25CircuitTrapCause": x25CircuitTrapCause,
       "x25CircuitTrapDiagnostic": x25CircuitTrapDiagnostic,
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
       "x25CallParmInMaxPktSize": x25CallParmInMaxPktSize,
       "x25CallParmOutMaxPktSize": x25CallParmOutMaxPktSize,
       "x25Traps": x25Traps,
       "x25L3Traps": x25L3Traps,
       "x25Restart": x25Restart,
       "x25VC": x25VC}
)
