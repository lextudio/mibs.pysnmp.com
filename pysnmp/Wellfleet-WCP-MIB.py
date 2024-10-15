# SNMP MIB module (Wellfleet-WCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-WCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:28 2024
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

(wfCompressionGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfCompressionGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfWcpLineTable_Object = MibTable
wfWcpLineTable = _WfWcpLineTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1)
)
if mibBuilder.loadTexts:
    wfWcpLineTable.setStatus("mandatory")
_WfWcpLineEntry_Object = MibTableRow
wfWcpLineEntry = _WfWcpLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1)
)
wfWcpLineEntry.setIndexNames(
    (0, "Wellfleet-WCP-MIB", "wfWcpLineLineNumber"),
    (0, "Wellfleet-WCP-MIB", "wfWcpLineLLIndex"),
)
if mibBuilder.loadTexts:
    wfWcpLineEntry.setStatus("mandatory")


class _WfWcpLineDelete_Type(Integer32):
    """Custom type wfWcpLineDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfWcpLineDelete_Type.__name__ = "Integer32"
_WfWcpLineDelete_Object = MibTableColumn
wfWcpLineDelete = _WfWcpLineDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 1),
    _WfWcpLineDelete_Type()
)
wfWcpLineDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpLineDelete.setStatus("mandatory")


class _WfWcpLineDisable_Type(Integer32):
    """Custom type wfWcpLineDisable based on Integer32"""
    defaultValue = 1

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


_WfWcpLineDisable_Type.__name__ = "Integer32"
_WfWcpLineDisable_Object = MibTableColumn
wfWcpLineDisable = _WfWcpLineDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 2),
    _WfWcpLineDisable_Type()
)
wfWcpLineDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpLineDisable.setStatus("mandatory")
_WfWcpLineLineNumber_Type = Integer32
_WfWcpLineLineNumber_Object = MibTableColumn
wfWcpLineLineNumber = _WfWcpLineLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 3),
    _WfWcpLineLineNumber_Type()
)
wfWcpLineLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpLineLineNumber.setStatus("mandatory")
_WfWcpLineLLIndex_Type = Integer32
_WfWcpLineLLIndex_Object = MibTableColumn
wfWcpLineLLIndex = _WfWcpLineLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 4),
    _WfWcpLineLLIndex_Type()
)
wfWcpLineLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpLineLLIndex.setStatus("mandatory")


class _WfWcpLineCompressionMode_Type(Integer32):
    """Custom type wfWcpLineCompressionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpc", 1),
          ("ppc", 2))
    )


_WfWcpLineCompressionMode_Type.__name__ = "Integer32"
_WfWcpLineCompressionMode_Object = MibTableColumn
wfWcpLineCompressionMode = _WfWcpLineCompressionMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 5),
    _WfWcpLineCompressionMode_Type()
)
wfWcpLineCompressionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpLineCompressionMode.setStatus("mandatory")


class _WfWcpLineHistorySize_Type(Integer32):
    """Custom type wfWcpLineHistorySize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("k32", 1),
          ("k8", 2))
    )


_WfWcpLineHistorySize_Type.__name__ = "Integer32"
_WfWcpLineHistorySize_Object = MibTableColumn
wfWcpLineHistorySize = _WfWcpLineHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 6),
    _WfWcpLineHistorySize_Type()
)
wfWcpLineHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpLineHistorySize.setStatus("mandatory")


class _WfWcpLineBufferSize_Type(Integer32):
    """Custom type wfWcpLineBufferSize based on Integer32"""
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
        *(("large", 2),
          ("none", 4),
          ("normal", 3),
          ("verylarge", 1))
    )


_WfWcpLineBufferSize_Type.__name__ = "Integer32"
_WfWcpLineBufferSize_Object = MibTableColumn
wfWcpLineBufferSize = _WfWcpLineBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 7),
    _WfWcpLineBufferSize_Type()
)
wfWcpLineBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpLineBufferSize.setStatus("mandatory")


class _WfWcpLineEngineType_Type(Integer32):
    """Custom type wfWcpLineEngineType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_WfWcpLineEngineType_Type.__name__ = "Integer32"
_WfWcpLineEngineType_Object = MibTableColumn
wfWcpLineEngineType = _WfWcpLineEngineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 8),
    _WfWcpLineEngineType_Type()
)
wfWcpLineEngineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpLineEngineType.setStatus("mandatory")


class _WfWcpLineSearchDepth_Type(Integer32):
    """Custom type wfWcpLineSearchDepth based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfWcpLineSearchDepth_Type.__name__ = "Integer32"
_WfWcpLineSearchDepth_Object = MibTableColumn
wfWcpLineSearchDepth = _WfWcpLineSearchDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 9),
    _WfWcpLineSearchDepth_Type()
)
wfWcpLineSearchDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpLineSearchDepth.setStatus("mandatory")


class _WfWcpLineFallbackCompressionMode_Type(Integer32):
    """Custom type wfWcpLineFallbackCompressionMode based on Integer32"""
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
        *(("hardwareppc", 2),
          ("none", 3),
          ("softwarecpc", 1))
    )


_WfWcpLineFallbackCompressionMode_Type.__name__ = "Integer32"
_WfWcpLineFallbackCompressionMode_Object = MibTableColumn
wfWcpLineFallbackCompressionMode = _WfWcpLineFallbackCompressionMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 10),
    _WfWcpLineFallbackCompressionMode_Type()
)
wfWcpLineFallbackCompressionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpLineFallbackCompressionMode.setStatus("mandatory")


class _WfWcpLineClientCompressorRingSize_Type(Integer32):
    """Custom type wfWcpLineClientCompressorRingSize based on Integer32"""
    defaultValue = 0


_WfWcpLineClientCompressorRingSize_Object = MibTableColumn
wfWcpLineClientCompressorRingSize = _WfWcpLineClientCompressorRingSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 11),
    _WfWcpLineClientCompressorRingSize_Type()
)
wfWcpLineClientCompressorRingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpLineClientCompressorRingSize.setStatus("mandatory")


class _WfWcpLineClientDecompressorRingSize_Type(Integer32):
    """Custom type wfWcpLineClientDecompressorRingSize based on Integer32"""
    defaultValue = 0


_WfWcpLineClientDecompressorRingSize_Object = MibTableColumn
wfWcpLineClientDecompressorRingSize = _WfWcpLineClientDecompressorRingSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 1, 1, 12),
    _WfWcpLineClientDecompressorRingSize_Type()
)
wfWcpLineClientDecompressorRingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpLineClientDecompressorRingSize.setStatus("mandatory")
_WfWcpCircuitTable_Object = MibTable
wfWcpCircuitTable = _WfWcpCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 2)
)
if mibBuilder.loadTexts:
    wfWcpCircuitTable.setStatus("mandatory")
_WfWcpCircuitEntry_Object = MibTableRow
wfWcpCircuitEntry = _WfWcpCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 2, 1)
)
wfWcpCircuitEntry.setIndexNames(
    (0, "Wellfleet-WCP-MIB", "wfWcpCircuitId"),
)
if mibBuilder.loadTexts:
    wfWcpCircuitEntry.setStatus("mandatory")


class _WfWcpCircuitDelete_Type(Integer32):
    """Custom type wfWcpCircuitDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfWcpCircuitDelete_Type.__name__ = "Integer32"
_WfWcpCircuitDelete_Object = MibTableColumn
wfWcpCircuitDelete = _WfWcpCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 2, 1, 1),
    _WfWcpCircuitDelete_Type()
)
wfWcpCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpCircuitDelete.setStatus("mandatory")


class _WfWcpCircuitDisable_Type(Integer32):
    """Custom type wfWcpCircuitDisable based on Integer32"""
    defaultValue = 1

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


_WfWcpCircuitDisable_Type.__name__ = "Integer32"
_WfWcpCircuitDisable_Object = MibTableColumn
wfWcpCircuitDisable = _WfWcpCircuitDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 2, 1, 2),
    _WfWcpCircuitDisable_Type()
)
wfWcpCircuitDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpCircuitDisable.setStatus("mandatory")
_WfWcpCircuitId_Type = Integer32
_WfWcpCircuitId_Object = MibTableColumn
wfWcpCircuitId = _WfWcpCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 2, 1, 3),
    _WfWcpCircuitId_Type()
)
wfWcpCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpCircuitId.setStatus("mandatory")


class _WfWcpCircuitCompressionMode_Type(Integer32):
    """Custom type wfWcpCircuitCompressionMode based on Integer32"""
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
        *(("cpc", 1),
          ("inherit", 3),
          ("ppc", 2))
    )


_WfWcpCircuitCompressionMode_Type.__name__ = "Integer32"
_WfWcpCircuitCompressionMode_Object = MibTableColumn
wfWcpCircuitCompressionMode = _WfWcpCircuitCompressionMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 2, 1, 4),
    _WfWcpCircuitCompressionMode_Type()
)
wfWcpCircuitCompressionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpCircuitCompressionMode.setStatus("mandatory")


class _WfWcpCircuitHistorySize_Type(Integer32):
    """Custom type wfWcpCircuitHistorySize based on Integer32"""
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
        *(("inherit", 3),
          ("k32", 1),
          ("k8", 2))
    )


_WfWcpCircuitHistorySize_Type.__name__ = "Integer32"
_WfWcpCircuitHistorySize_Object = MibTableColumn
wfWcpCircuitHistorySize = _WfWcpCircuitHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 2, 1, 5),
    _WfWcpCircuitHistorySize_Type()
)
wfWcpCircuitHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpCircuitHistorySize.setStatus("mandatory")


class _WfWcpCircuitEngineType_Type(Integer32):
    """Custom type wfWcpCircuitEngineType based on Integer32"""
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
        *(("hardware", 2),
          ("inherit", 3),
          ("software", 1))
    )


_WfWcpCircuitEngineType_Type.__name__ = "Integer32"
_WfWcpCircuitEngineType_Object = MibTableColumn
wfWcpCircuitEngineType = _WfWcpCircuitEngineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 2, 1, 6),
    _WfWcpCircuitEngineType_Type()
)
wfWcpCircuitEngineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpCircuitEngineType.setStatus("mandatory")


class _WfWcpCircuitSearchDepth_Type(Integer32):
    """Custom type wfWcpCircuitSearchDepth based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WfWcpCircuitSearchDepth_Type.__name__ = "Integer32"
_WfWcpCircuitSearchDepth_Object = MibTableColumn
wfWcpCircuitSearchDepth = _WfWcpCircuitSearchDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 2, 1, 7),
    _WfWcpCircuitSearchDepth_Type()
)
wfWcpCircuitSearchDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfWcpCircuitSearchDepth.setStatus("mandatory")
_WfWcpCircuitCompressorOutBytes_Type = Counter32
_WfWcpCircuitCompressorOutBytes_Object = MibTableColumn
wfWcpCircuitCompressorOutBytes = _WfWcpCircuitCompressorOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 2, 1, 8),
    _WfWcpCircuitCompressorOutBytes_Type()
)
wfWcpCircuitCompressorOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpCircuitCompressorOutBytes.setStatus("mandatory")
_WfWcpCircuitDecompressorOutBytes_Type = Counter32
_WfWcpCircuitDecompressorOutBytes_Object = MibTableColumn
wfWcpCircuitDecompressorOutBytes = _WfWcpCircuitDecompressorOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 2, 1, 9),
    _WfWcpCircuitDecompressorOutBytes_Type()
)
wfWcpCircuitDecompressorOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpCircuitDecompressorOutBytes.setStatus("mandatory")
_WfWcpVcTable_Object = MibTable
wfWcpVcTable = _WfWcpVcTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3)
)
if mibBuilder.loadTexts:
    wfWcpVcTable.setStatus("mandatory")
_WfWcpVcEntry_Object = MibTableRow
wfWcpVcEntry = _WfWcpVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1)
)
wfWcpVcEntry.setIndexNames(
    (0, "Wellfleet-WCP-MIB", "wfWcpVcLineNumber"),
    (0, "Wellfleet-WCP-MIB", "wfWcpVcLLIndex"),
    (0, "Wellfleet-WCP-MIB", "wfWcpVcCircuitId"),
    (0, "Wellfleet-WCP-MIB", "wfWcpVcId"),
)
if mibBuilder.loadTexts:
    wfWcpVcEntry.setStatus("mandatory")


class _WfWcpVcCompressorState_Type(Integer32):
    """Custom type wfWcpVcCompressorState based on Integer32"""
    defaultValue = 3

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
        *(("data", 1),
          ("disabled", 2),
          ("disconnected", 3),
          ("init", 4),
          ("nak", 5))
    )


_WfWcpVcCompressorState_Type.__name__ = "Integer32"
_WfWcpVcCompressorState_Object = MibTableColumn
wfWcpVcCompressorState = _WfWcpVcCompressorState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 1),
    _WfWcpVcCompressorState_Type()
)
wfWcpVcCompressorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcCompressorState.setStatus("mandatory")


class _WfWcpVcDecompressorState_Type(Integer32):
    """Custom type wfWcpVcDecompressorState based on Integer32"""
    defaultValue = 3

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 7),
          ("data", 1),
          ("disabled", 2),
          ("disconnected", 3),
          ("disconnecting", 8),
          ("init", 4),
          ("reset", 6),
          ("rexmit", 5))
    )


_WfWcpVcDecompressorState_Type.__name__ = "Integer32"
_WfWcpVcDecompressorState_Object = MibTableColumn
wfWcpVcDecompressorState = _WfWcpVcDecompressorState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 2),
    _WfWcpVcDecompressorState_Type()
)
wfWcpVcDecompressorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcDecompressorState.setStatus("mandatory")
_WfWcpVcLineNumber_Type = Integer32
_WfWcpVcLineNumber_Object = MibTableColumn
wfWcpVcLineNumber = _WfWcpVcLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 3),
    _WfWcpVcLineNumber_Type()
)
wfWcpVcLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcLineNumber.setStatus("mandatory")
_WfWcpVcLLIndex_Type = Integer32
_WfWcpVcLLIndex_Object = MibTableColumn
wfWcpVcLLIndex = _WfWcpVcLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 4),
    _WfWcpVcLLIndex_Type()
)
wfWcpVcLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcLLIndex.setStatus("mandatory")
_WfWcpVcCircuitId_Type = Integer32
_WfWcpVcCircuitId_Object = MibTableColumn
wfWcpVcCircuitId = _WfWcpVcCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 5),
    _WfWcpVcCircuitId_Type()
)
wfWcpVcCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcCircuitId.setStatus("mandatory")
_WfWcpVcId_Type = Integer32
_WfWcpVcId_Object = MibTableColumn
wfWcpVcId = _WfWcpVcId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 6),
    _WfWcpVcId_Type()
)
wfWcpVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcId.setStatus("mandatory")


class _WfWcpVcCompressionMode_Type(Integer32):
    """Custom type wfWcpVcCompressionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpc", 1),
          ("ppc", 2))
    )


_WfWcpVcCompressionMode_Type.__name__ = "Integer32"
_WfWcpVcCompressionMode_Object = MibTableColumn
wfWcpVcCompressionMode = _WfWcpVcCompressionMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 7),
    _WfWcpVcCompressionMode_Type()
)
wfWcpVcCompressionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcCompressionMode.setStatus("mandatory")


class _WfWcpVcHistorySize_Type(Integer32):
    """Custom type wfWcpVcHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("k32", 1),
          ("k8", 2))
    )


_WfWcpVcHistorySize_Type.__name__ = "Integer32"
_WfWcpVcHistorySize_Object = MibTableColumn
wfWcpVcHistorySize = _WfWcpVcHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 8),
    _WfWcpVcHistorySize_Type()
)
wfWcpVcHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcHistorySize.setStatus("mandatory")
_WfWcpVcCompressorInBytes_Type = Counter32
_WfWcpVcCompressorInBytes_Object = MibTableColumn
wfWcpVcCompressorInBytes = _WfWcpVcCompressorInBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 9),
    _WfWcpVcCompressorInBytes_Type()
)
wfWcpVcCompressorInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcCompressorInBytes.setStatus("mandatory")
_WfWcpVcCompressorOutBytes_Type = Counter32
_WfWcpVcCompressorOutBytes_Object = MibTableColumn
wfWcpVcCompressorOutBytes = _WfWcpVcCompressorOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 10),
    _WfWcpVcCompressorOutBytes_Type()
)
wfWcpVcCompressorOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcCompressorOutBytes.setStatus("mandatory")
_WfWcpVcDecompressorInBytes_Type = Counter32
_WfWcpVcDecompressorInBytes_Object = MibTableColumn
wfWcpVcDecompressorInBytes = _WfWcpVcDecompressorInBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 11),
    _WfWcpVcDecompressorInBytes_Type()
)
wfWcpVcDecompressorInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcDecompressorInBytes.setStatus("mandatory")
_WfWcpVcDecompressorOutBytes_Type = Counter32
_WfWcpVcDecompressorOutBytes_Object = MibTableColumn
wfWcpVcDecompressorOutBytes = _WfWcpVcDecompressorOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 12),
    _WfWcpVcDecompressorOutBytes_Type()
)
wfWcpVcDecompressorOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcDecompressorOutBytes.setStatus("mandatory")
_WfWcpVcTxCPCPackets_Type = Counter32
_WfWcpVcTxCPCPackets_Object = MibTableColumn
wfWcpVcTxCPCPackets = _WfWcpVcTxCPCPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 13),
    _WfWcpVcTxCPCPackets_Type()
)
wfWcpVcTxCPCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcTxCPCPackets.setStatus("mandatory")
_WfWcpVcRxCPCPackets_Type = Counter32
_WfWcpVcRxCPCPackets_Object = MibTableColumn
wfWcpVcRxCPCPackets = _WfWcpVcRxCPCPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 14),
    _WfWcpVcRxCPCPackets_Type()
)
wfWcpVcRxCPCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcRxCPCPackets.setStatus("mandatory")
_WfWcpVcTxPPCPackets_Type = Counter32
_WfWcpVcTxPPCPackets_Object = MibTableColumn
wfWcpVcTxPPCPackets = _WfWcpVcTxPPCPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 15),
    _WfWcpVcTxPPCPackets_Type()
)
wfWcpVcTxPPCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcTxPPCPackets.setStatus("mandatory")
_WfWcpVcRxPPCPackets_Type = Counter32
_WfWcpVcRxPPCPackets_Object = MibTableColumn
wfWcpVcRxPPCPackets = _WfWcpVcRxPPCPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 16),
    _WfWcpVcRxPPCPackets_Type()
)
wfWcpVcRxPPCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcRxPPCPackets.setStatus("mandatory")
_WfWcpVcTxAntiExpPackets_Type = Counter32
_WfWcpVcTxAntiExpPackets_Object = MibTableColumn
wfWcpVcTxAntiExpPackets = _WfWcpVcTxAntiExpPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 17),
    _WfWcpVcTxAntiExpPackets_Type()
)
wfWcpVcTxAntiExpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcTxAntiExpPackets.setStatus("mandatory")
_WfWcpVcRxAntiExpPackets_Type = Counter32
_WfWcpVcRxAntiExpPackets_Object = MibTableColumn
wfWcpVcRxAntiExpPackets = _WfWcpVcRxAntiExpPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 18),
    _WfWcpVcRxAntiExpPackets_Type()
)
wfWcpVcRxAntiExpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcRxAntiExpPackets.setStatus("mandatory")
_WfWcpVcTxResetReqs_Type = Counter32
_WfWcpVcTxResetReqs_Object = MibTableColumn
wfWcpVcTxResetReqs = _WfWcpVcTxResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 19),
    _WfWcpVcTxResetReqs_Type()
)
wfWcpVcTxResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcTxResetReqs.setStatus("mandatory")
_WfWcpVcRxResetReqs_Type = Counter32
_WfWcpVcRxResetReqs_Object = MibTableColumn
wfWcpVcRxResetReqs = _WfWcpVcRxResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 20),
    _WfWcpVcRxResetReqs_Type()
)
wfWcpVcRxResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcRxResetReqs.setStatus("mandatory")
_WfWcpVcTxRexmitReqs_Type = Counter32
_WfWcpVcTxRexmitReqs_Object = MibTableColumn
wfWcpVcTxRexmitReqs = _WfWcpVcTxRexmitReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 21),
    _WfWcpVcTxRexmitReqs_Type()
)
wfWcpVcTxRexmitReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcTxRexmitReqs.setStatus("mandatory")
_WfWcpVcRxRexmitReqs_Type = Counter32
_WfWcpVcRxRexmitReqs_Object = MibTableColumn
wfWcpVcRxRexmitReqs = _WfWcpVcRxRexmitReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 22),
    _WfWcpVcRxRexmitReqs_Type()
)
wfWcpVcRxRexmitReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcRxRexmitReqs.setStatus("mandatory")
_WfWcpVcTxRexmitNaks_Type = Counter32
_WfWcpVcTxRexmitNaks_Object = MibTableColumn
wfWcpVcTxRexmitNaks = _WfWcpVcTxRexmitNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 23),
    _WfWcpVcTxRexmitNaks_Type()
)
wfWcpVcTxRexmitNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcTxRexmitNaks.setStatus("mandatory")
_WfWcpVcRxRexmitNaks_Type = Counter32
_WfWcpVcRxRexmitNaks_Object = MibTableColumn
wfWcpVcRxRexmitNaks = _WfWcpVcRxRexmitNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 24),
    _WfWcpVcRxRexmitNaks_Type()
)
wfWcpVcRxRexmitNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcRxRexmitNaks.setStatus("mandatory")
_WfWcpVcDataOutOfSeqs_Type = Counter32
_WfWcpVcDataOutOfSeqs_Object = MibTableColumn
wfWcpVcDataOutOfSeqs = _WfWcpVcDataOutOfSeqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 25),
    _WfWcpVcDataOutOfSeqs_Type()
)
wfWcpVcDataOutOfSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcDataOutOfSeqs.setStatus("mandatory")
_WfWcpVcRexmitOutOfSeqs_Type = Counter32
_WfWcpVcRexmitOutOfSeqs_Object = MibTableColumn
wfWcpVcRexmitOutOfSeqs = _WfWcpVcRexmitOutOfSeqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 26),
    _WfWcpVcRexmitOutOfSeqs_Type()
)
wfWcpVcRexmitOutOfSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcRexmitOutOfSeqs.setStatus("mandatory")
_WfWcpVcRexmitTimeouts_Type = Counter32
_WfWcpVcRexmitTimeouts_Object = MibTableColumn
wfWcpVcRexmitTimeouts = _WfWcpVcRexmitTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 27),
    _WfWcpVcRexmitTimeouts_Type()
)
wfWcpVcRexmitTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcRexmitTimeouts.setStatus("mandatory")
_WfWcpVcExceededKs_Type = Counter32
_WfWcpVcExceededKs_Object = MibTableColumn
wfWcpVcExceededKs = _WfWcpVcExceededKs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 28),
    _WfWcpVcExceededKs_Type()
)
wfWcpVcExceededKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcExceededKs.setStatus("mandatory")
_WfWcpVcInvalidOpCodes_Type = Counter32
_WfWcpVcInvalidOpCodes_Object = MibTableColumn
wfWcpVcInvalidOpCodes = _WfWcpVcInvalidOpCodes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 29),
    _WfWcpVcInvalidOpCodes_Type()
)
wfWcpVcInvalidOpCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcInvalidOpCodes.setStatus("mandatory")


class _WfWcpVcEngineType_Type(Integer32):
    """Custom type wfWcpVcEngineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("none", 3),
          ("software", 1))
    )


_WfWcpVcEngineType_Type.__name__ = "Integer32"
_WfWcpVcEngineType_Object = MibTableColumn
wfWcpVcEngineType = _WfWcpVcEngineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 30),
    _WfWcpVcEngineType_Type()
)
wfWcpVcEngineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcEngineType.setStatus("mandatory")
_WfWcpVcSearchDepth_Type = Integer32
_WfWcpVcSearchDepth_Object = MibTableColumn
wfWcpVcSearchDepth = _WfWcpVcSearchDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 3, 1, 31),
    _WfWcpVcSearchDepth_Type()
)
wfWcpVcSearchDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfWcpVcSearchDepth.setStatus("mandatory")
_WfHwCompTable_Object = MibTable
wfHwCompTable = _WfHwCompTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4)
)
if mibBuilder.loadTexts:
    wfHwCompTable.setStatus("mandatory")
_WfHwCompEntry_Object = MibTableRow
wfHwCompEntry = _WfHwCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1)
)
wfHwCompEntry.setIndexNames(
    (0, "Wellfleet-WCP-MIB", "wfHwCompSlot"),
    (0, "Wellfleet-WCP-MIB", "wfHwCompModule"),
    (0, "Wellfleet-WCP-MIB", "wfHwCompEngineNumber"),
)
if mibBuilder.loadTexts:
    wfHwCompEntry.setStatus("mandatory")


class _WfHwCompState_Type(Integer32):
    """Custom type wfHwCompState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfHwCompState_Type.__name__ = "Integer32"
_WfHwCompState_Object = MibTableColumn
wfHwCompState = _WfHwCompState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 1),
    _WfHwCompState_Type()
)
wfHwCompState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompState.setStatus("mandatory")
_WfHwCompSlot_Type = Integer32
_WfHwCompSlot_Object = MibTableColumn
wfHwCompSlot = _WfHwCompSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 2),
    _WfHwCompSlot_Type()
)
wfHwCompSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompSlot.setStatus("mandatory")
_WfHwCompModule_Type = Integer32
_WfHwCompModule_Object = MibTableColumn
wfHwCompModule = _WfHwCompModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 3),
    _WfHwCompModule_Type()
)
wfHwCompModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompModule.setStatus("mandatory")
_WfHwCompEngineNumber_Type = Integer32
_WfHwCompEngineNumber_Object = MibTableColumn
wfHwCompEngineNumber = _WfHwCompEngineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 4),
    _WfHwCompEngineNumber_Type()
)
wfHwCompEngineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompEngineNumber.setStatus("mandatory")
_WfHwCompCompressionHistoryTotal_Type = Integer32
_WfHwCompCompressionHistoryTotal_Object = MibTableColumn
wfHwCompCompressionHistoryTotal = _WfHwCompCompressionHistoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 5),
    _WfHwCompCompressionHistoryTotal_Type()
)
wfHwCompCompressionHistoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionHistoryTotal.setStatus("mandatory")
_WfHwCompCompressionHashTblSize_Type = Integer32
_WfHwCompCompressionHashTblSize_Object = MibTableColumn
wfHwCompCompressionHashTblSize = _WfHwCompCompressionHashTblSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 6),
    _WfHwCompCompressionHashTblSize_Type()
)
wfHwCompCompressionHashTblSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionHashTblSize.setStatus("mandatory")
_WfHwCompDecompressionHistoryTotal_Type = Integer32
_WfHwCompDecompressionHistoryTotal_Object = MibTableColumn
wfHwCompDecompressionHistoryTotal = _WfHwCompDecompressionHistoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 7),
    _WfHwCompDecompressionHistoryTotal_Type()
)
wfHwCompDecompressionHistoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompDecompressionHistoryTotal.setStatus("mandatory")
_WfHwComp8kContextsTotal_Type = Integer32
_WfHwComp8kContextsTotal_Object = MibTableColumn
wfHwComp8kContextsTotal = _WfHwComp8kContextsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 8),
    _WfHwComp8kContextsTotal_Type()
)
wfHwComp8kContextsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwComp8kContextsTotal.setStatus("mandatory")
_WfHwComp32kContextsTotal_Type = Integer32
_WfHwComp32kContextsTotal_Object = MibTableColumn
wfHwComp32kContextsTotal = _WfHwComp32kContextsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 9),
    _WfHwComp32kContextsTotal_Type()
)
wfHwComp32kContextsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwComp32kContextsTotal.setStatus("mandatory")
_WfHwComp8kCpcContextsInUse_Type = Integer32
_WfHwComp8kCpcContextsInUse_Object = MibTableColumn
wfHwComp8kCpcContextsInUse = _WfHwComp8kCpcContextsInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 10),
    _WfHwComp8kCpcContextsInUse_Type()
)
wfHwComp8kCpcContextsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwComp8kCpcContextsInUse.setStatus("mandatory")
_WfHwComp8kPpcContextsInUse_Type = Integer32
_WfHwComp8kPpcContextsInUse_Object = MibTableColumn
wfHwComp8kPpcContextsInUse = _WfHwComp8kPpcContextsInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 11),
    _WfHwComp8kPpcContextsInUse_Type()
)
wfHwComp8kPpcContextsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwComp8kPpcContextsInUse.setStatus("mandatory")
_WfHwComp32kContextsInUse_Type = Integer32
_WfHwComp32kContextsInUse_Object = MibTableColumn
wfHwComp32kContextsInUse = _WfHwComp32kContextsInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 12),
    _WfHwComp32kContextsInUse_Type()
)
wfHwComp32kContextsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwComp32kContextsInUse.setStatus("mandatory")
_WfHwComp8kContextsAvailable_Type = Integer32
_WfHwComp8kContextsAvailable_Object = MibTableColumn
wfHwComp8kContextsAvailable = _WfHwComp8kContextsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 13),
    _WfHwComp8kContextsAvailable_Type()
)
wfHwComp8kContextsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwComp8kContextsAvailable.setStatus("mandatory")
_WfHwComp32kContextsAvailable_Type = Integer32
_WfHwComp32kContextsAvailable_Object = MibTableColumn
wfHwComp32kContextsAvailable = _WfHwComp32kContextsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 14),
    _WfHwComp32kContextsAvailable_Type()
)
wfHwComp32kContextsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwComp32kContextsAvailable.setStatus("mandatory")
_WfHwCompCpcContextsRegistered_Type = Integer32
_WfHwCompCpcContextsRegistered_Object = MibTableColumn
wfHwCompCpcContextsRegistered = _WfHwCompCpcContextsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 15),
    _WfHwCompCpcContextsRegistered_Type()
)
wfHwCompCpcContextsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCpcContextsRegistered.setStatus("mandatory")
_WfHwCompPpcContextsRegistered_Type = Integer32
_WfHwCompPpcContextsRegistered_Object = MibTableColumn
wfHwCompPpcContextsRegistered = _WfHwCompPpcContextsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 16),
    _WfHwCompPpcContextsRegistered_Type()
)
wfHwCompPpcContextsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompPpcContextsRegistered.setStatus("mandatory")
_WfHwCompCompressionTotalRingSize_Type = Integer32
_WfHwCompCompressionTotalRingSize_Object = MibTableColumn
wfHwCompCompressionTotalRingSize = _WfHwCompCompressionTotalRingSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 17),
    _WfHwCompCompressionTotalRingSize_Type()
)
wfHwCompCompressionTotalRingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionTotalRingSize.setStatus("mandatory")
_WfHwCompDecompressionTotalRingSize_Type = Integer32
_WfHwCompDecompressionTotalRingSize_Object = MibTableColumn
wfHwCompDecompressionTotalRingSize = _WfHwCompDecompressionTotalRingSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 18),
    _WfHwCompDecompressionTotalRingSize_Type()
)
wfHwCompDecompressionTotalRingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompDecompressionTotalRingSize.setStatus("mandatory")
_WfHwCompCompressionCurrentQueued_Type = Integer32
_WfHwCompCompressionCurrentQueued_Object = MibTableColumn
wfHwCompCompressionCurrentQueued = _WfHwCompCompressionCurrentQueued_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 19),
    _WfHwCompCompressionCurrentQueued_Type()
)
wfHwCompCompressionCurrentQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionCurrentQueued.setStatus("mandatory")
_WfHwCompDecompressionCurrentQueued_Type = Integer32
_WfHwCompDecompressionCurrentQueued_Object = MibTableColumn
wfHwCompDecompressionCurrentQueued = _WfHwCompDecompressionCurrentQueued_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 20),
    _WfHwCompDecompressionCurrentQueued_Type()
)
wfHwCompDecompressionCurrentQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompDecompressionCurrentQueued.setStatus("mandatory")
_WfHwCompCompressionQHiWatermark_Type = Integer32
_WfHwCompCompressionQHiWatermark_Object = MibTableColumn
wfHwCompCompressionQHiWatermark = _WfHwCompCompressionQHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 21),
    _WfHwCompCompressionQHiWatermark_Type()
)
wfHwCompCompressionQHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionQHiWatermark.setStatus("mandatory")
_WfHwCompDecompressionQHiWatermark_Type = Integer32
_WfHwCompDecompressionQHiWatermark_Object = MibTableColumn
wfHwCompDecompressionQHiWatermark = _WfHwCompDecompressionQHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 22),
    _WfHwCompDecompressionQHiWatermark_Type()
)
wfHwCompDecompressionQHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompDecompressionQHiWatermark.setStatus("mandatory")
_WfHwCompCompressionPkts_Type = Counter32
_WfHwCompCompressionPkts_Object = MibTableColumn
wfHwCompCompressionPkts = _WfHwCompCompressionPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 23),
    _WfHwCompCompressionPkts_Type()
)
wfHwCompCompressionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionPkts.setStatus("mandatory")
_WfHwCompDecompressionPkts_Type = Counter32
_WfHwCompDecompressionPkts_Object = MibTableColumn
wfHwCompDecompressionPkts = _WfHwCompDecompressionPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 24),
    _WfHwCompDecompressionPkts_Type()
)
wfHwCompDecompressionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompDecompressionPkts.setStatus("mandatory")
_WfHwCompTxExpandedPkts_Type = Counter32
_WfHwCompTxExpandedPkts_Object = MibTableColumn
wfHwCompTxExpandedPkts = _WfHwCompTxExpandedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 25),
    _WfHwCompTxExpandedPkts_Type()
)
wfHwCompTxExpandedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompTxExpandedPkts.setStatus("mandatory")
_WfHwCompTxNonCompressedPkts_Type = Counter32
_WfHwCompTxNonCompressedPkts_Object = MibTableColumn
wfHwCompTxNonCompressedPkts = _WfHwCompTxNonCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 26),
    _WfHwCompTxNonCompressedPkts_Type()
)
wfHwCompTxNonCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompTxNonCompressedPkts.setStatus("mandatory")
_WfHwCompRxNonCompressedPkts_Type = Counter32
_WfHwCompRxNonCompressedPkts_Object = MibTableColumn
wfHwCompRxNonCompressedPkts = _WfHwCompRxNonCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 27),
    _WfHwCompRxNonCompressedPkts_Type()
)
wfHwCompRxNonCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompRxNonCompressedPkts.setStatus("mandatory")
_WfHwCompRxDroppedPkts_Type = Counter32
_WfHwCompRxDroppedPkts_Object = MibTableColumn
wfHwCompRxDroppedPkts = _WfHwCompRxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 28),
    _WfHwCompRxDroppedPkts_Type()
)
wfHwCompRxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompRxDroppedPkts.setStatus("mandatory")
_WfHwCompRxLcbMismatches_Type = Counter32
_WfHwCompRxLcbMismatches_Object = MibTableColumn
wfHwCompRxLcbMismatches = _WfHwCompRxLcbMismatches_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 29),
    _WfHwCompRxLcbMismatches_Type()
)
wfHwCompRxLcbMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompRxLcbMismatches.setStatus("mandatory")
_WfHwCompCompressionRingOverflows_Type = Counter32
_WfHwCompCompressionRingOverflows_Object = MibTableColumn
wfHwCompCompressionRingOverflows = _WfHwCompCompressionRingOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 30),
    _WfHwCompCompressionRingOverflows_Type()
)
wfHwCompCompressionRingOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionRingOverflows.setStatus("mandatory")
_WfHwCompDecompressionRingOverflows_Type = Counter32
_WfHwCompDecompressionRingOverflows_Object = MibTableColumn
wfHwCompDecompressionRingOverflows = _WfHwCompDecompressionRingOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 31),
    _WfHwCompDecompressionRingOverflows_Type()
)
wfHwCompDecompressionRingOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompDecompressionRingOverflows.setStatus("mandatory")
_WfHwCompCompressionErrors_Type = Counter32
_WfHwCompCompressionErrors_Object = MibTableColumn
wfHwCompCompressionErrors = _WfHwCompCompressionErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 32),
    _WfHwCompCompressionErrors_Type()
)
wfHwCompCompressionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionErrors.setStatus("mandatory")
_WfHwCompDecompressionErrors_Type = Counter32
_WfHwCompDecompressionErrors_Object = MibTableColumn
wfHwCompDecompressionErrors = _WfHwCompDecompressionErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 33),
    _WfHwCompDecompressionErrors_Type()
)
wfHwCompDecompressionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompDecompressionErrors.setStatus("mandatory")
_WfHwCompCompressionSrcPktLenErrors_Type = Counter32
_WfHwCompCompressionSrcPktLenErrors_Object = MibTableColumn
wfHwCompCompressionSrcPktLenErrors = _WfHwCompCompressionSrcPktLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 34),
    _WfHwCompCompressionSrcPktLenErrors_Type()
)
wfHwCompCompressionSrcPktLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionSrcPktLenErrors.setStatus("mandatory")
_WfHwCompCompressionCcbFormatErrors_Type = Counter32
_WfHwCompCompressionCcbFormatErrors_Object = MibTableColumn
wfHwCompCompressionCcbFormatErrors = _WfHwCompCompressionCcbFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 35),
    _WfHwCompCompressionCcbFormatErrors_Type()
)
wfHwCompCompressionCcbFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionCcbFormatErrors.setStatus("mandatory")
_WfHwCompCompressionDescFormatErrors_Type = Counter32
_WfHwCompCompressionDescFormatErrors_Object = MibTableColumn
wfHwCompCompressionDescFormatErrors = _WfHwCompCompressionDescFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 36),
    _WfHwCompCompressionDescFormatErrors_Type()
)
wfHwCompCompressionDescFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionDescFormatErrors.setStatus("mandatory")
_WfHwCompCompressionInternalErrors_Type = Counter32
_WfHwCompCompressionInternalErrors_Object = MibTableColumn
wfHwCompCompressionInternalErrors = _WfHwCompCompressionInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 37),
    _WfHwCompCompressionInternalErrors_Type()
)
wfHwCompCompressionInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompCompressionInternalErrors.setStatus("mandatory")
_WfHwCompDecompressionSrcPktLenErrors_Type = Counter32
_WfHwCompDecompressionSrcPktLenErrors_Object = MibTableColumn
wfHwCompDecompressionSrcPktLenErrors = _WfHwCompDecompressionSrcPktLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 38),
    _WfHwCompDecompressionSrcPktLenErrors_Type()
)
wfHwCompDecompressionSrcPktLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompDecompressionSrcPktLenErrors.setStatus("mandatory")
_WfHwCompDecompressionCcbFormatErrors_Type = Counter32
_WfHwCompDecompressionCcbFormatErrors_Object = MibTableColumn
wfHwCompDecompressionCcbFormatErrors = _WfHwCompDecompressionCcbFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 39),
    _WfHwCompDecompressionCcbFormatErrors_Type()
)
wfHwCompDecompressionCcbFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompDecompressionCcbFormatErrors.setStatus("mandatory")
_WfHwCompDecompressionDescFormatErrors_Type = Counter32
_WfHwCompDecompressionDescFormatErrors_Object = MibTableColumn
wfHwCompDecompressionDescFormatErrors = _WfHwCompDecompressionDescFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 40),
    _WfHwCompDecompressionDescFormatErrors_Type()
)
wfHwCompDecompressionDescFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompDecompressionDescFormatErrors.setStatus("mandatory")
_WfHwCompDecompressionInternalErrors_Type = Counter32
_WfHwCompDecompressionInternalErrors_Object = MibTableColumn
wfHwCompDecompressionInternalErrors = _WfHwCompDecompressionInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 41),
    _WfHwCompDecompressionInternalErrors_Type()
)
wfHwCompDecompressionInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompDecompressionInternalErrors.setStatus("mandatory")


class _WfHwCompChipType_Type(Integer32):
    """Custom type wfHwCompChipType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("itcs", 2),
          ("magna", 1))
    )


_WfHwCompChipType_Type.__name__ = "Integer32"
_WfHwCompChipType_Object = MibTableColumn
wfHwCompChipType = _WfHwCompChipType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 42),
    _WfHwCompChipType_Type()
)
wfHwCompChipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompChipType.setStatus("mandatory")
_WfHwCompMsaCpcContextsRegistered_Type = Integer32
_WfHwCompMsaCpcContextsRegistered_Object = MibTableColumn
wfHwCompMsaCpcContextsRegistered = _WfHwCompMsaCpcContextsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 43),
    _WfHwCompMsaCpcContextsRegistered_Type()
)
wfHwCompMsaCpcContextsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompMsaCpcContextsRegistered.setStatus("mandatory")
_WfHwCompMsaPpcContextsRegistered_Type = Integer32
_WfHwCompMsaPpcContextsRegistered_Object = MibTableColumn
wfHwCompMsaPpcContextsRegistered = _WfHwCompMsaPpcContextsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 44),
    _WfHwCompMsaPpcContextsRegistered_Type()
)
wfHwCompMsaPpcContextsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompMsaPpcContextsRegistered.setStatus("mandatory")
_WfHwCompMsa8KContextsGuaranteed_Type = Integer32
_WfHwCompMsa8KContextsGuaranteed_Object = MibTableColumn
wfHwCompMsa8KContextsGuaranteed = _WfHwCompMsa8KContextsGuaranteed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 45),
    _WfHwCompMsa8KContextsGuaranteed_Type()
)
wfHwCompMsa8KContextsGuaranteed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompMsa8KContextsGuaranteed.setStatus("mandatory")
_WfHwCompStacContextsTotal_Type = Integer32
_WfHwCompStacContextsTotal_Object = MibTableColumn
wfHwCompStacContextsTotal = _WfHwCompStacContextsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 46),
    _WfHwCompStacContextsTotal_Type()
)
wfHwCompStacContextsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompStacContextsTotal.setStatus("mandatory")
_WfHwCompStacCpcContextsRegistered_Type = Integer32
_WfHwCompStacCpcContextsRegistered_Object = MibTableColumn
wfHwCompStacCpcContextsRegistered = _WfHwCompStacCpcContextsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 47),
    _WfHwCompStacCpcContextsRegistered_Type()
)
wfHwCompStacCpcContextsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompStacCpcContextsRegistered.setStatus("mandatory")
_WfHwCompStacPpcContextsRegistered_Type = Integer32
_WfHwCompStacPpcContextsRegistered_Object = MibTableColumn
wfHwCompStacPpcContextsRegistered = _WfHwCompStacPpcContextsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 48),
    _WfHwCompStacPpcContextsRegistered_Type()
)
wfHwCompStacPpcContextsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompStacPpcContextsRegistered.setStatus("mandatory")
_WfHwCompStacPpcContextsInUse_Type = Integer32
_WfHwCompStacPpcContextsInUse_Object = MibTableColumn
wfHwCompStacPpcContextsInUse = _WfHwCompStacPpcContextsInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 49),
    _WfHwCompStacPpcContextsInUse_Type()
)
wfHwCompStacPpcContextsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompStacPpcContextsInUse.setStatus("mandatory")
_WfHwCompStacContextsAvailable_Type = Integer32
_WfHwCompStacContextsAvailable_Object = MibTableColumn
wfHwCompStacContextsAvailable = _WfHwCompStacContextsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 50),
    _WfHwCompStacContextsAvailable_Type()
)
wfHwCompStacContextsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompStacContextsAvailable.setStatus("mandatory")
_WfHwCompStacContextsGuaranteed_Type = Integer32
_WfHwCompStacContextsGuaranteed_Object = MibTableColumn
wfHwCompStacContextsGuaranteed = _WfHwCompStacContextsGuaranteed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 51),
    _WfHwCompStacContextsGuaranteed_Type()
)
wfHwCompStacContextsGuaranteed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompStacContextsGuaranteed.setStatus("mandatory")
_WfHwCompMsaCompressedPkts_Type = Counter32
_WfHwCompMsaCompressedPkts_Object = MibTableColumn
wfHwCompMsaCompressedPkts = _WfHwCompMsaCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 52),
    _WfHwCompMsaCompressedPkts_Type()
)
wfHwCompMsaCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompMsaCompressedPkts.setStatus("mandatory")
_WfHwCompStacCompressedPkts_Type = Counter32
_WfHwCompStacCompressedPkts_Object = MibTableColumn
wfHwCompStacCompressedPkts = _WfHwCompStacCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 53),
    _WfHwCompStacCompressedPkts_Type()
)
wfHwCompStacCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompStacCompressedPkts.setStatus("mandatory")
_WfHwCompMsaDecompressedPkts_Type = Counter32
_WfHwCompMsaDecompressedPkts_Object = MibTableColumn
wfHwCompMsaDecompressedPkts = _WfHwCompMsaDecompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 54),
    _WfHwCompMsaDecompressedPkts_Type()
)
wfHwCompMsaDecompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompMsaDecompressedPkts.setStatus("mandatory")
_WfHwCompStacDecompressedPkts_Type = Counter32
_WfHwCompStacDecompressedPkts_Object = MibTableColumn
wfHwCompStacDecompressedPkts = _WfHwCompStacDecompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 55),
    _WfHwCompStacDecompressedPkts_Type()
)
wfHwCompStacDecompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompStacDecompressedPkts.setStatus("mandatory")
_WfHwCompMsaTxExpandedPkts_Type = Counter32
_WfHwCompMsaTxExpandedPkts_Object = MibTableColumn
wfHwCompMsaTxExpandedPkts = _WfHwCompMsaTxExpandedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 56),
    _WfHwCompMsaTxExpandedPkts_Type()
)
wfHwCompMsaTxExpandedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompMsaTxExpandedPkts.setStatus("mandatory")
_WfHwCompStacTxExpandedPkts_Type = Counter32
_WfHwCompStacTxExpandedPkts_Object = MibTableColumn
wfHwCompStacTxExpandedPkts = _WfHwCompStacTxExpandedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 57),
    _WfHwCompStacTxExpandedPkts_Type()
)
wfHwCompStacTxExpandedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompStacTxExpandedPkts.setStatus("mandatory")
_WfHwCompMsaTxNonCompressedPkts_Type = Counter32
_WfHwCompMsaTxNonCompressedPkts_Object = MibTableColumn
wfHwCompMsaTxNonCompressedPkts = _WfHwCompMsaTxNonCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 58),
    _WfHwCompMsaTxNonCompressedPkts_Type()
)
wfHwCompMsaTxNonCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompMsaTxNonCompressedPkts.setStatus("mandatory")
_WfHwCompStacTxNonCompressedPkts_Type = Counter32
_WfHwCompStacTxNonCompressedPkts_Object = MibTableColumn
wfHwCompStacTxNonCompressedPkts = _WfHwCompStacTxNonCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 59),
    _WfHwCompStacTxNonCompressedPkts_Type()
)
wfHwCompStacTxNonCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompStacTxNonCompressedPkts.setStatus("mandatory")
_WfHwCompMsaRxNonCompressedPkts_Type = Counter32
_WfHwCompMsaRxNonCompressedPkts_Object = MibTableColumn
wfHwCompMsaRxNonCompressedPkts = _WfHwCompMsaRxNonCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 60),
    _WfHwCompMsaRxNonCompressedPkts_Type()
)
wfHwCompMsaRxNonCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompMsaRxNonCompressedPkts.setStatus("mandatory")
_WfHwCompStacRxNonCompressedPkts_Type = Counter32
_WfHwCompStacRxNonCompressedPkts_Object = MibTableColumn
wfHwCompStacRxNonCompressedPkts = _WfHwCompStacRxNonCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 4, 1, 61),
    _WfHwCompStacRxNonCompressedPkts_Type()
)
wfHwCompStacRxNonCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCompStacRxNonCompressedPkts.setStatus("mandatory")
_WfStacCircuitTable_Object = MibTable
wfStacCircuitTable = _WfStacCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6)
)
if mibBuilder.loadTexts:
    wfStacCircuitTable.setStatus("mandatory")
_WfStacCircuitEntry_Object = MibTableRow
wfStacCircuitEntry = _WfStacCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1)
)
wfStacCircuitEntry.setIndexNames(
    (0, "Wellfleet-WCP-MIB", "wfStacCircuitId"),
)
if mibBuilder.loadTexts:
    wfStacCircuitEntry.setStatus("mandatory")


class _WfStacCircuitDelete_Type(Integer32):
    """Custom type wfStacCircuitDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfStacCircuitDelete_Type.__name__ = "Integer32"
_WfStacCircuitDelete_Object = MibTableColumn
wfStacCircuitDelete = _WfStacCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 1),
    _WfStacCircuitDelete_Type()
)
wfStacCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStacCircuitDelete.setStatus("mandatory")


class _WfStacCircuitDisable_Type(Integer32):
    """Custom type wfStacCircuitDisable based on Integer32"""
    defaultValue = 1

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


_WfStacCircuitDisable_Type.__name__ = "Integer32"
_WfStacCircuitDisable_Object = MibTableColumn
wfStacCircuitDisable = _WfStacCircuitDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 2),
    _WfStacCircuitDisable_Type()
)
wfStacCircuitDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStacCircuitDisable.setStatus("mandatory")
_WfStacCircuitId_Type = Integer32
_WfStacCircuitId_Object = MibTableColumn
wfStacCircuitId = _WfStacCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 3),
    _WfStacCircuitId_Type()
)
wfStacCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStacCircuitId.setStatus("mandatory")


class _WfStacCircuitEngineType_Type(Integer32):
    """Custom type wfStacCircuitEngineType based on Integer32"""
    defaultValue = 1

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
        *(("hardware", 2),
          ("inherit", 3),
          ("none", 4),
          ("software", 1))
    )


_WfStacCircuitEngineType_Type.__name__ = "Integer32"
_WfStacCircuitEngineType_Object = MibTableColumn
wfStacCircuitEngineType = _WfStacCircuitEngineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 4),
    _WfStacCircuitEngineType_Type()
)
wfStacCircuitEngineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStacCircuitEngineType.setStatus("mandatory")


class _WfStacCircuitCompressionMode_Type(Integer32):
    """Custom type wfStacCircuitCompressionMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mode0", 1),
          ("mode3", 4))
    )


_WfStacCircuitCompressionMode_Type.__name__ = "Integer32"
_WfStacCircuitCompressionMode_Object = MibTableColumn
wfStacCircuitCompressionMode = _WfStacCircuitCompressionMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 5),
    _WfStacCircuitCompressionMode_Type()
)
wfStacCircuitCompressionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStacCircuitCompressionMode.setStatus("mandatory")


class _WfStacCircuitCompressorState_Type(Integer32):
    """Custom type wfStacCircuitCompressorState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("disabled", 2))
    )


_WfStacCircuitCompressorState_Type.__name__ = "Integer32"
_WfStacCircuitCompressorState_Object = MibTableColumn
wfStacCircuitCompressorState = _WfStacCircuitCompressorState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 6),
    _WfStacCircuitCompressorState_Type()
)
wfStacCircuitCompressorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitCompressorState.setStatus("mandatory")


class _WfStacCircuitDecompressorState_Type(Integer32):
    """Custom type wfStacCircuitDecompressorState based on Integer32"""
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
        *(("data", 1),
          ("disabled", 2),
          ("reset", 3))
    )


_WfStacCircuitDecompressorState_Type.__name__ = "Integer32"
_WfStacCircuitDecompressorState_Object = MibTableColumn
wfStacCircuitDecompressorState = _WfStacCircuitDecompressorState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 7),
    _WfStacCircuitDecompressorState_Type()
)
wfStacCircuitDecompressorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitDecompressorState.setStatus("mandatory")


class _WfStacCircuitFallBackCompressionMode_Type(Integer32):
    """Custom type wfStacCircuitFallBackCompressionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("softwarecpc", 1))
    )


_WfStacCircuitFallBackCompressionMode_Type.__name__ = "Integer32"
_WfStacCircuitFallBackCompressionMode_Object = MibTableColumn
wfStacCircuitFallBackCompressionMode = _WfStacCircuitFallBackCompressionMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 8),
    _WfStacCircuitFallBackCompressionMode_Type()
)
wfStacCircuitFallBackCompressionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStacCircuitFallBackCompressionMode.setStatus("mandatory")
_WfStacCircuitCompressorInBytes_Type = Counter32
_WfStacCircuitCompressorInBytes_Object = MibTableColumn
wfStacCircuitCompressorInBytes = _WfStacCircuitCompressorInBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 9),
    _WfStacCircuitCompressorInBytes_Type()
)
wfStacCircuitCompressorInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitCompressorInBytes.setStatus("mandatory")
_WfStacCircuitCompressorOutBytes_Type = Counter32
_WfStacCircuitCompressorOutBytes_Object = MibTableColumn
wfStacCircuitCompressorOutBytes = _WfStacCircuitCompressorOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 10),
    _WfStacCircuitCompressorOutBytes_Type()
)
wfStacCircuitCompressorOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitCompressorOutBytes.setStatus("mandatory")
_WfStacCircuitDecompressorInBytes_Type = Counter32
_WfStacCircuitDecompressorInBytes_Object = MibTableColumn
wfStacCircuitDecompressorInBytes = _WfStacCircuitDecompressorInBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 11),
    _WfStacCircuitDecompressorInBytes_Type()
)
wfStacCircuitDecompressorInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitDecompressorInBytes.setStatus("mandatory")
_WfStacCircuitDecompressorOutBytes_Type = Counter32
_WfStacCircuitDecompressorOutBytes_Object = MibTableColumn
wfStacCircuitDecompressorOutBytes = _WfStacCircuitDecompressorOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 12),
    _WfStacCircuitDecompressorOutBytes_Type()
)
wfStacCircuitDecompressorOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitDecompressorOutBytes.setStatus("mandatory")
_WfStacCircuitTxMode0Packets_Type = Counter32
_WfStacCircuitTxMode0Packets_Object = MibTableColumn
wfStacCircuitTxMode0Packets = _WfStacCircuitTxMode0Packets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 13),
    _WfStacCircuitTxMode0Packets_Type()
)
wfStacCircuitTxMode0Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitTxMode0Packets.setStatus("mandatory")
_WfStacCircuitRxMode0Packets_Type = Counter32
_WfStacCircuitRxMode0Packets_Object = MibTableColumn
wfStacCircuitRxMode0Packets = _WfStacCircuitRxMode0Packets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 14),
    _WfStacCircuitRxMode0Packets_Type()
)
wfStacCircuitRxMode0Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitRxMode0Packets.setStatus("mandatory")
_WfStacCircuitTxMode3Packets_Type = Counter32
_WfStacCircuitTxMode3Packets_Object = MibTableColumn
wfStacCircuitTxMode3Packets = _WfStacCircuitTxMode3Packets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 15),
    _WfStacCircuitTxMode3Packets_Type()
)
wfStacCircuitTxMode3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitTxMode3Packets.setStatus("mandatory")
_WfStacCircuitRxMode3Packets_Type = Counter32
_WfStacCircuitRxMode3Packets_Object = MibTableColumn
wfStacCircuitRxMode3Packets = _WfStacCircuitRxMode3Packets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 16),
    _WfStacCircuitRxMode3Packets_Type()
)
wfStacCircuitRxMode3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitRxMode3Packets.setStatus("mandatory")
_WfStacCircuitTxExpPackets_Type = Counter32
_WfStacCircuitTxExpPackets_Object = MibTableColumn
wfStacCircuitTxExpPackets = _WfStacCircuitTxExpPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 17),
    _WfStacCircuitTxExpPackets_Type()
)
wfStacCircuitTxExpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitTxExpPackets.setStatus("mandatory")
_WfStacCircuitRxExpPackets_Type = Counter32
_WfStacCircuitRxExpPackets_Object = MibTableColumn
wfStacCircuitRxExpPackets = _WfStacCircuitRxExpPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 18),
    _WfStacCircuitRxExpPackets_Type()
)
wfStacCircuitRxExpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitRxExpPackets.setStatus("mandatory")
_WfStacCircuitTxResetReqs_Type = Counter32
_WfStacCircuitTxResetReqs_Object = MibTableColumn
wfStacCircuitTxResetReqs = _WfStacCircuitTxResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 19),
    _WfStacCircuitTxResetReqs_Type()
)
wfStacCircuitTxResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitTxResetReqs.setStatus("mandatory")
_WfStacCircuitRxResetReqs_Type = Counter32
_WfStacCircuitRxResetReqs_Object = MibTableColumn
wfStacCircuitRxResetReqs = _WfStacCircuitRxResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22, 6, 1, 20),
    _WfStacCircuitRxResetReqs_Type()
)
wfStacCircuitRxResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStacCircuitRxResetReqs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-WCP-MIB",
    **{"wfWcpLineTable": wfWcpLineTable,
       "wfWcpLineEntry": wfWcpLineEntry,
       "wfWcpLineDelete": wfWcpLineDelete,
       "wfWcpLineDisable": wfWcpLineDisable,
       "wfWcpLineLineNumber": wfWcpLineLineNumber,
       "wfWcpLineLLIndex": wfWcpLineLLIndex,
       "wfWcpLineCompressionMode": wfWcpLineCompressionMode,
       "wfWcpLineHistorySize": wfWcpLineHistorySize,
       "wfWcpLineBufferSize": wfWcpLineBufferSize,
       "wfWcpLineEngineType": wfWcpLineEngineType,
       "wfWcpLineSearchDepth": wfWcpLineSearchDepth,
       "wfWcpLineFallbackCompressionMode": wfWcpLineFallbackCompressionMode,
       "wfWcpLineClientCompressorRingSize": wfWcpLineClientCompressorRingSize,
       "wfWcpLineClientDecompressorRingSize": wfWcpLineClientDecompressorRingSize,
       "wfWcpCircuitTable": wfWcpCircuitTable,
       "wfWcpCircuitEntry": wfWcpCircuitEntry,
       "wfWcpCircuitDelete": wfWcpCircuitDelete,
       "wfWcpCircuitDisable": wfWcpCircuitDisable,
       "wfWcpCircuitId": wfWcpCircuitId,
       "wfWcpCircuitCompressionMode": wfWcpCircuitCompressionMode,
       "wfWcpCircuitHistorySize": wfWcpCircuitHistorySize,
       "wfWcpCircuitEngineType": wfWcpCircuitEngineType,
       "wfWcpCircuitSearchDepth": wfWcpCircuitSearchDepth,
       "wfWcpCircuitCompressorOutBytes": wfWcpCircuitCompressorOutBytes,
       "wfWcpCircuitDecompressorOutBytes": wfWcpCircuitDecompressorOutBytes,
       "wfWcpVcTable": wfWcpVcTable,
       "wfWcpVcEntry": wfWcpVcEntry,
       "wfWcpVcCompressorState": wfWcpVcCompressorState,
       "wfWcpVcDecompressorState": wfWcpVcDecompressorState,
       "wfWcpVcLineNumber": wfWcpVcLineNumber,
       "wfWcpVcLLIndex": wfWcpVcLLIndex,
       "wfWcpVcCircuitId": wfWcpVcCircuitId,
       "wfWcpVcId": wfWcpVcId,
       "wfWcpVcCompressionMode": wfWcpVcCompressionMode,
       "wfWcpVcHistorySize": wfWcpVcHistorySize,
       "wfWcpVcCompressorInBytes": wfWcpVcCompressorInBytes,
       "wfWcpVcCompressorOutBytes": wfWcpVcCompressorOutBytes,
       "wfWcpVcDecompressorInBytes": wfWcpVcDecompressorInBytes,
       "wfWcpVcDecompressorOutBytes": wfWcpVcDecompressorOutBytes,
       "wfWcpVcTxCPCPackets": wfWcpVcTxCPCPackets,
       "wfWcpVcRxCPCPackets": wfWcpVcRxCPCPackets,
       "wfWcpVcTxPPCPackets": wfWcpVcTxPPCPackets,
       "wfWcpVcRxPPCPackets": wfWcpVcRxPPCPackets,
       "wfWcpVcTxAntiExpPackets": wfWcpVcTxAntiExpPackets,
       "wfWcpVcRxAntiExpPackets": wfWcpVcRxAntiExpPackets,
       "wfWcpVcTxResetReqs": wfWcpVcTxResetReqs,
       "wfWcpVcRxResetReqs": wfWcpVcRxResetReqs,
       "wfWcpVcTxRexmitReqs": wfWcpVcTxRexmitReqs,
       "wfWcpVcRxRexmitReqs": wfWcpVcRxRexmitReqs,
       "wfWcpVcTxRexmitNaks": wfWcpVcTxRexmitNaks,
       "wfWcpVcRxRexmitNaks": wfWcpVcRxRexmitNaks,
       "wfWcpVcDataOutOfSeqs": wfWcpVcDataOutOfSeqs,
       "wfWcpVcRexmitOutOfSeqs": wfWcpVcRexmitOutOfSeqs,
       "wfWcpVcRexmitTimeouts": wfWcpVcRexmitTimeouts,
       "wfWcpVcExceededKs": wfWcpVcExceededKs,
       "wfWcpVcInvalidOpCodes": wfWcpVcInvalidOpCodes,
       "wfWcpVcEngineType": wfWcpVcEngineType,
       "wfWcpVcSearchDepth": wfWcpVcSearchDepth,
       "wfHwCompTable": wfHwCompTable,
       "wfHwCompEntry": wfHwCompEntry,
       "wfHwCompState": wfHwCompState,
       "wfHwCompSlot": wfHwCompSlot,
       "wfHwCompModule": wfHwCompModule,
       "wfHwCompEngineNumber": wfHwCompEngineNumber,
       "wfHwCompCompressionHistoryTotal": wfHwCompCompressionHistoryTotal,
       "wfHwCompCompressionHashTblSize": wfHwCompCompressionHashTblSize,
       "wfHwCompDecompressionHistoryTotal": wfHwCompDecompressionHistoryTotal,
       "wfHwComp8kContextsTotal": wfHwComp8kContextsTotal,
       "wfHwComp32kContextsTotal": wfHwComp32kContextsTotal,
       "wfHwComp8kCpcContextsInUse": wfHwComp8kCpcContextsInUse,
       "wfHwComp8kPpcContextsInUse": wfHwComp8kPpcContextsInUse,
       "wfHwComp32kContextsInUse": wfHwComp32kContextsInUse,
       "wfHwComp8kContextsAvailable": wfHwComp8kContextsAvailable,
       "wfHwComp32kContextsAvailable": wfHwComp32kContextsAvailable,
       "wfHwCompCpcContextsRegistered": wfHwCompCpcContextsRegistered,
       "wfHwCompPpcContextsRegistered": wfHwCompPpcContextsRegistered,
       "wfHwCompCompressionTotalRingSize": wfHwCompCompressionTotalRingSize,
       "wfHwCompDecompressionTotalRingSize": wfHwCompDecompressionTotalRingSize,
       "wfHwCompCompressionCurrentQueued": wfHwCompCompressionCurrentQueued,
       "wfHwCompDecompressionCurrentQueued": wfHwCompDecompressionCurrentQueued,
       "wfHwCompCompressionQHiWatermark": wfHwCompCompressionQHiWatermark,
       "wfHwCompDecompressionQHiWatermark": wfHwCompDecompressionQHiWatermark,
       "wfHwCompCompressionPkts": wfHwCompCompressionPkts,
       "wfHwCompDecompressionPkts": wfHwCompDecompressionPkts,
       "wfHwCompTxExpandedPkts": wfHwCompTxExpandedPkts,
       "wfHwCompTxNonCompressedPkts": wfHwCompTxNonCompressedPkts,
       "wfHwCompRxNonCompressedPkts": wfHwCompRxNonCompressedPkts,
       "wfHwCompRxDroppedPkts": wfHwCompRxDroppedPkts,
       "wfHwCompRxLcbMismatches": wfHwCompRxLcbMismatches,
       "wfHwCompCompressionRingOverflows": wfHwCompCompressionRingOverflows,
       "wfHwCompDecompressionRingOverflows": wfHwCompDecompressionRingOverflows,
       "wfHwCompCompressionErrors": wfHwCompCompressionErrors,
       "wfHwCompDecompressionErrors": wfHwCompDecompressionErrors,
       "wfHwCompCompressionSrcPktLenErrors": wfHwCompCompressionSrcPktLenErrors,
       "wfHwCompCompressionCcbFormatErrors": wfHwCompCompressionCcbFormatErrors,
       "wfHwCompCompressionDescFormatErrors": wfHwCompCompressionDescFormatErrors,
       "wfHwCompCompressionInternalErrors": wfHwCompCompressionInternalErrors,
       "wfHwCompDecompressionSrcPktLenErrors": wfHwCompDecompressionSrcPktLenErrors,
       "wfHwCompDecompressionCcbFormatErrors": wfHwCompDecompressionCcbFormatErrors,
       "wfHwCompDecompressionDescFormatErrors": wfHwCompDecompressionDescFormatErrors,
       "wfHwCompDecompressionInternalErrors": wfHwCompDecompressionInternalErrors,
       "wfHwCompChipType": wfHwCompChipType,
       "wfHwCompMsaCpcContextsRegistered": wfHwCompMsaCpcContextsRegistered,
       "wfHwCompMsaPpcContextsRegistered": wfHwCompMsaPpcContextsRegistered,
       "wfHwCompMsa8KContextsGuaranteed": wfHwCompMsa8KContextsGuaranteed,
       "wfHwCompStacContextsTotal": wfHwCompStacContextsTotal,
       "wfHwCompStacCpcContextsRegistered": wfHwCompStacCpcContextsRegistered,
       "wfHwCompStacPpcContextsRegistered": wfHwCompStacPpcContextsRegistered,
       "wfHwCompStacPpcContextsInUse": wfHwCompStacPpcContextsInUse,
       "wfHwCompStacContextsAvailable": wfHwCompStacContextsAvailable,
       "wfHwCompStacContextsGuaranteed": wfHwCompStacContextsGuaranteed,
       "wfHwCompMsaCompressedPkts": wfHwCompMsaCompressedPkts,
       "wfHwCompStacCompressedPkts": wfHwCompStacCompressedPkts,
       "wfHwCompMsaDecompressedPkts": wfHwCompMsaDecompressedPkts,
       "wfHwCompStacDecompressedPkts": wfHwCompStacDecompressedPkts,
       "wfHwCompMsaTxExpandedPkts": wfHwCompMsaTxExpandedPkts,
       "wfHwCompStacTxExpandedPkts": wfHwCompStacTxExpandedPkts,
       "wfHwCompMsaTxNonCompressedPkts": wfHwCompMsaTxNonCompressedPkts,
       "wfHwCompStacTxNonCompressedPkts": wfHwCompStacTxNonCompressedPkts,
       "wfHwCompMsaRxNonCompressedPkts": wfHwCompMsaRxNonCompressedPkts,
       "wfHwCompStacRxNonCompressedPkts": wfHwCompStacRxNonCompressedPkts,
       "wfStacCircuitTable": wfStacCircuitTable,
       "wfStacCircuitEntry": wfStacCircuitEntry,
       "wfStacCircuitDelete": wfStacCircuitDelete,
       "wfStacCircuitDisable": wfStacCircuitDisable,
       "wfStacCircuitId": wfStacCircuitId,
       "wfStacCircuitEngineType": wfStacCircuitEngineType,
       "wfStacCircuitCompressionMode": wfStacCircuitCompressionMode,
       "wfStacCircuitCompressorState": wfStacCircuitCompressorState,
       "wfStacCircuitDecompressorState": wfStacCircuitDecompressorState,
       "wfStacCircuitFallBackCompressionMode": wfStacCircuitFallBackCompressionMode,
       "wfStacCircuitCompressorInBytes": wfStacCircuitCompressorInBytes,
       "wfStacCircuitCompressorOutBytes": wfStacCircuitCompressorOutBytes,
       "wfStacCircuitDecompressorInBytes": wfStacCircuitDecompressorInBytes,
       "wfStacCircuitDecompressorOutBytes": wfStacCircuitDecompressorOutBytes,
       "wfStacCircuitTxMode0Packets": wfStacCircuitTxMode0Packets,
       "wfStacCircuitRxMode0Packets": wfStacCircuitRxMode0Packets,
       "wfStacCircuitTxMode3Packets": wfStacCircuitTxMode3Packets,
       "wfStacCircuitRxMode3Packets": wfStacCircuitRxMode3Packets,
       "wfStacCircuitTxExpPackets": wfStacCircuitTxExpPackets,
       "wfStacCircuitRxExpPackets": wfStacCircuitRxExpPackets,
       "wfStacCircuitTxResetReqs": wfStacCircuitTxResetReqs,
       "wfStacCircuitRxResetReqs": wfStacCircuitRxResetReqs}
)
