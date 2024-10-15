# SNMP MIB module (TERAWAVE-teraSonet-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraSonet-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:19 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraSonetGroup_ObjectIdentity = ObjectIdentity
teraSonetGroup = _TeraSonetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 10)
)
_TeraSonetMediumTable_Object = MibTable
teraSonetMediumTable = _TeraSonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 1)
)
if mibBuilder.loadTexts:
    teraSonetMediumTable.setStatus("mandatory")
_TeraSonetMediumTableEntry_Object = MibTableRow
teraSonetMediumTableEntry = _TeraSonetMediumTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 1, 1)
)
teraSonetMediumTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetMediumTableEntry.setStatus("mandatory")


class _TeraSonetMode_Type(Integer32):
    """Custom type teraSonetMode based on Integer32"""
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
        *(("sts12STM4", 4),
          ("sts12cSTM4", 5),
          ("sts1STM0", 1),
          ("sts3STM1", 2),
          ("sts3cSTM1", 3),
          ("sts48cSTM16", 6))
    )


_TeraSonetMode_Type.__name__ = "Integer32"
_TeraSonetMode_Object = MibTableColumn
teraSonetMode = _TeraSonetMode_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 1, 1, 1),
    _TeraSonetMode_Type()
)
teraSonetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetMode.setStatus("mandatory")


class _TeraSonetStm1Mapping_Type(Integer32):
    """Custom type teraSonetStm1Mapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("au3", 1),
          ("au4", 2),
          ("none", 0))
    )


_TeraSonetStm1Mapping_Type.__name__ = "Integer32"
_TeraSonetStm1Mapping_Object = MibTableColumn
teraSonetStm1Mapping = _TeraSonetStm1Mapping_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 1, 1, 2),
    _TeraSonetStm1Mapping_Type()
)
teraSonetStm1Mapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetStm1Mapping.setStatus("mandatory")


class _TeraSonetSDThreshold_Type(Integer32):
    """Custom type teraSonetSDThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_TeraSonetSDThreshold_Type.__name__ = "Integer32"
_TeraSonetSDThreshold_Object = MibTableColumn
teraSonetSDThreshold = _TeraSonetSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 1, 1, 3),
    _TeraSonetSDThreshold_Type()
)
teraSonetSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetSDThreshold.setStatus("mandatory")


class _TeraSonetSFThreshold_Type(Integer32):
    """Custom type teraSonetSFThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_TeraSonetSFThreshold_Type.__name__ = "Integer32"
_TeraSonetSFThreshold_Object = MibTableColumn
teraSonetSFThreshold = _TeraSonetSFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 1, 1, 4),
    _TeraSonetSFThreshold_Type()
)
teraSonetSFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetSFThreshold.setStatus("mandatory")


class _TeraSonetMediumTotalTimeElapsed_Type(Integer32):
    """Custom type teraSonetMediumTotalTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_TeraSonetMediumTotalTimeElapsed_Type.__name__ = "Integer32"
_TeraSonetMediumTotalTimeElapsed_Object = MibTableColumn
teraSonetMediumTotalTimeElapsed = _TeraSonetMediumTotalTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 1, 1, 5),
    _TeraSonetMediumTotalTimeElapsed_Type()
)
teraSonetMediumTotalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetMediumTotalTimeElapsed.setStatus("mandatory")


class _TeraSonetMediumValidTotalIntervals_Type(Integer32):
    """Custom type teraSonetMediumValidTotalIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TeraSonetMediumValidTotalIntervals_Type.__name__ = "Integer32"
_TeraSonetMediumValidTotalIntervals_Object = MibTableColumn
teraSonetMediumValidTotalIntervals = _TeraSonetMediumValidTotalIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 1, 1, 6),
    _TeraSonetMediumValidTotalIntervals_Type()
)
teraSonetMediumValidTotalIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetMediumValidTotalIntervals.setStatus("mandatory")


class _TeraSonetMediumInvalidTotalIntervals_Type(Integer32):
    """Custom type teraSonetMediumInvalidTotalIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TeraSonetMediumInvalidTotalIntervals_Type.__name__ = "Integer32"
_TeraSonetMediumInvalidTotalIntervals_Object = MibTableColumn
teraSonetMediumInvalidTotalIntervals = _TeraSonetMediumInvalidTotalIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 1, 1, 7),
    _TeraSonetMediumInvalidTotalIntervals_Type()
)
teraSonetMediumInvalidTotalIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetMediumInvalidTotalIntervals.setStatus("mandatory")
_TeraSonetSectionTable_Object = MibTable
teraSonetSectionTable = _TeraSonetSectionTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 2)
)
if mibBuilder.loadTexts:
    teraSonetSectionTable.setStatus("mandatory")
_TeraSonetSectionTableEntry_Object = MibTableRow
teraSonetSectionTableEntry = _TeraSonetSectionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 2, 1)
)
teraSonetSectionTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetSectionTableEntry.setStatus("mandatory")


class _TeraSonetSectionTraceLenTx_Type(Integer32):
    """Custom type teraSonetSectionTraceLenTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("number-16", 1),
          ("number-64", 2))
    )


_TeraSonetSectionTraceLenTx_Type.__name__ = "Integer32"
_TeraSonetSectionTraceLenTx_Object = MibTableColumn
teraSonetSectionTraceLenTx = _TeraSonetSectionTraceLenTx_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 2, 1, 1),
    _TeraSonetSectionTraceLenTx_Type()
)
teraSonetSectionTraceLenTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetSectionTraceLenTx.setStatus("mandatory")
_TeraSonetSectionTraceTx_Type = OctetString
_TeraSonetSectionTraceTx_Object = MibTableColumn
teraSonetSectionTraceTx = _TeraSonetSectionTraceTx_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 2, 1, 2),
    _TeraSonetSectionTraceTx_Type()
)
teraSonetSectionTraceTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetSectionTraceTx.setStatus("mandatory")


class _TeraSonetSectionTraceLenRx_Type(Integer32):
    """Custom type teraSonetSectionTraceLenRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("number-16", 1),
          ("number-64", 2))
    )


_TeraSonetSectionTraceLenRx_Type.__name__ = "Integer32"
_TeraSonetSectionTraceLenRx_Object = MibTableColumn
teraSonetSectionTraceLenRx = _TeraSonetSectionTraceLenRx_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 2, 1, 3),
    _TeraSonetSectionTraceLenRx_Type()
)
teraSonetSectionTraceLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionTraceLenRx.setStatus("mandatory")
_TeraSonetSectionTraceRx_Type = OctetString
_TeraSonetSectionTraceRx_Object = MibTableColumn
teraSonetSectionTraceRx = _TeraSonetSectionTraceRx_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 2, 1, 4),
    _TeraSonetSectionTraceRx_Type()
)
teraSonetSectionTraceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionTraceRx.setStatus("mandatory")
_TeraSonetPathOverheadTable_Object = MibTable
teraSonetPathOverheadTable = _TeraSonetPathOverheadTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 3)
)
if mibBuilder.loadTexts:
    teraSonetPathOverheadTable.setStatus("mandatory")
_TeraSonetPathOverheadTableEntry_Object = MibTableRow
teraSonetPathOverheadTableEntry = _TeraSonetPathOverheadTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 3, 1)
)
teraSonetPathOverheadTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetPathOverheadTableEntry.setStatus("mandatory")


class _TeraSonetPathSigLabelTx_Type(Integer32):
    """Custom type teraSonetPathSigLabelTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TeraSonetPathSigLabelTx_Type.__name__ = "Integer32"
_TeraSonetPathSigLabelTx_Object = MibTableColumn
teraSonetPathSigLabelTx = _TeraSonetPathSigLabelTx_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 3, 1, 1),
    _TeraSonetPathSigLabelTx_Type()
)
teraSonetPathSigLabelTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetPathSigLabelTx.setStatus("mandatory")


class _TeraSonetPathTraceLenTx_Type(Integer32):
    """Custom type teraSonetPathTraceLenTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("number-16", 1),
          ("number-64", 2))
    )


_TeraSonetPathTraceLenTx_Type.__name__ = "Integer32"
_TeraSonetPathTraceLenTx_Object = MibTableColumn
teraSonetPathTraceLenTx = _TeraSonetPathTraceLenTx_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 3, 1, 2),
    _TeraSonetPathTraceLenTx_Type()
)
teraSonetPathTraceLenTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetPathTraceLenTx.setStatus("mandatory")
_TeraSonetPathTraceTx_Type = OctetString
_TeraSonetPathTraceTx_Object = MibTableColumn
teraSonetPathTraceTx = _TeraSonetPathTraceTx_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 3, 1, 3),
    _TeraSonetPathTraceTx_Type()
)
teraSonetPathTraceTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetPathTraceTx.setStatus("mandatory")


class _TeraSonetPathSigLabelRx_Type(Integer32):
    """Custom type teraSonetPathSigLabelRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TeraSonetPathSigLabelRx_Type.__name__ = "Integer32"
_TeraSonetPathSigLabelRx_Object = MibTableColumn
teraSonetPathSigLabelRx = _TeraSonetPathSigLabelRx_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 3, 1, 4),
    _TeraSonetPathSigLabelRx_Type()
)
teraSonetPathSigLabelRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathSigLabelRx.setStatus("mandatory")


class _TeraSonetPathTraceLenRx_Type(Integer32):
    """Custom type teraSonetPathTraceLenRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("number-16", 1),
          ("number-64", 2))
    )


_TeraSonetPathTraceLenRx_Type.__name__ = "Integer32"
_TeraSonetPathTraceLenRx_Object = MibTableColumn
teraSonetPathTraceLenRx = _TeraSonetPathTraceLenRx_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 3, 1, 5),
    _TeraSonetPathTraceLenRx_Type()
)
teraSonetPathTraceLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathTraceLenRx.setStatus("mandatory")
_TeraSonetPathTraceRx_Type = OctetString
_TeraSonetPathTraceRx_Object = MibTableColumn
teraSonetPathTraceRx = _TeraSonetPathTraceRx_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 3, 1, 6),
    _TeraSonetPathTraceRx_Type()
)
teraSonetPathTraceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathTraceRx.setStatus("mandatory")
_TeraSonetMapperConfigTable_Object = MibTable
teraSonetMapperConfigTable = _TeraSonetMapperConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 4)
)
if mibBuilder.loadTexts:
    teraSonetMapperConfigTable.setStatus("mandatory")
_TeraSonetMapperConfigTableEntry_Object = MibTableRow
teraSonetMapperConfigTableEntry = _TeraSonetMapperConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 4, 1)
)
teraSonetMapperConfigTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetMapperConfigTableEntry.setStatus("mandatory")


class _TeraSonetMapperType_Type(Integer32):
    """Custom type teraSonetMapperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 1),
          ("none", 0),
          ("vc12", 2),
          ("vt1-5", 3))
    )


_TeraSonetMapperType_Type.__name__ = "Integer32"
_TeraSonetMapperType_Object = MibTableColumn
teraSonetMapperType = _TeraSonetMapperType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 4, 1, 1),
    _TeraSonetMapperType_Type()
)
teraSonetMapperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetMapperType.setStatus("mandatory")


class _TeraSonetMapperLoopbackConfig_Type(Integer32):
    """Custom type teraSonetMapperLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_TeraSonetMapperLoopbackConfig_Type.__name__ = "Integer32"
_TeraSonetMapperLoopbackConfig_Object = MibTableColumn
teraSonetMapperLoopbackConfig = _TeraSonetMapperLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 4, 1, 2),
    _TeraSonetMapperLoopbackConfig_Type()
)
teraSonetMapperLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetMapperLoopbackConfig.setStatus("mandatory")
_TeraSonetPathIdTable_Object = MibTable
teraSonetPathIdTable = _TeraSonetPathIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 5)
)
if mibBuilder.loadTexts:
    teraSonetPathIdTable.setStatus("mandatory")
_TeraSonetPathIdTableEntry_Object = MibTableRow
teraSonetPathIdTableEntry = _TeraSonetPathIdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 5, 1)
)
teraSonetPathIdTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
    (0, "TERAWAVE-teraSonet-MIB", "teraSonetPathIdSTS1"),
)
if mibBuilder.loadTexts:
    teraSonetPathIdTableEntry.setStatus("mandatory")


class _TeraSonetPathIdSTS1_Type(Integer32):
    """Custom type teraSonetPathIdSTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TeraSonetPathIdSTS1_Type.__name__ = "Integer32"
_TeraSonetPathIdSTS1_Object = MibTableColumn
teraSonetPathIdSTS1 = _TeraSonetPathIdSTS1_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 5, 1, 1),
    _TeraSonetPathIdSTS1_Type()
)
teraSonetPathIdSTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathIdSTS1.setStatus("mandatory")


class _TeraSonetPathIdIfIndex_Type(Integer32):
    """Custom type teraSonetPathIdIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraSonetPathIdIfIndex_Type.__name__ = "Integer32"
_TeraSonetPathIdIfIndex_Object = MibTableColumn
teraSonetPathIdIfIndex = _TeraSonetPathIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 5, 1, 2),
    _TeraSonetPathIdIfIndex_Type()
)
teraSonetPathIdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathIdIfIndex.setStatus("mandatory")
_TeraSonetVTIdTable_Object = MibTable
teraSonetVTIdTable = _TeraSonetVTIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 6)
)
if mibBuilder.loadTexts:
    teraSonetVTIdTable.setStatus("mandatory")
_TeraSonetVTIdTableEntry_Object = MibTableRow
teraSonetVTIdTableEntry = _TeraSonetVTIdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 6, 1)
)
teraSonetVTIdTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
    (0, "TERAWAVE-teraSonet-MIB", "teraSonetVTIdSTS1"),
    (0, "TERAWAVE-teraSonet-MIB", "teraSonetVTIdVTG"),
    (0, "TERAWAVE-teraSonet-MIB", "teraSonetVTIdVT"),
)
if mibBuilder.loadTexts:
    teraSonetVTIdTableEntry.setStatus("mandatory")


class _TeraSonetVTIdSTS1_Type(Integer32):
    """Custom type teraSonetVTIdSTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TeraSonetVTIdSTS1_Type.__name__ = "Integer32"
_TeraSonetVTIdSTS1_Object = MibTableColumn
teraSonetVTIdSTS1 = _TeraSonetVTIdSTS1_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 6, 1, 1),
    _TeraSonetVTIdSTS1_Type()
)
teraSonetVTIdSTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetVTIdSTS1.setStatus("mandatory")


class _TeraSonetVTIdVTG_Type(Integer32):
    """Custom type teraSonetVTIdVTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraSonetVTIdVTG_Type.__name__ = "Integer32"
_TeraSonetVTIdVTG_Object = MibTableColumn
teraSonetVTIdVTG = _TeraSonetVTIdVTG_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 6, 1, 2),
    _TeraSonetVTIdVTG_Type()
)
teraSonetVTIdVTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetVTIdVTG.setStatus("mandatory")


class _TeraSonetVTIdVT_Type(Integer32):
    """Custom type teraSonetVTIdVT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TeraSonetVTIdVT_Type.__name__ = "Integer32"
_TeraSonetVTIdVT_Object = MibTableColumn
teraSonetVTIdVT = _TeraSonetVTIdVT_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 6, 1, 3),
    _TeraSonetVTIdVT_Type()
)
teraSonetVTIdVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetVTIdVT.setStatus("mandatory")


class _TeraSonetVTIdIfIndex_Type(Integer32):
    """Custom type teraSonetVTIdIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraSonetVTIdIfIndex_Type.__name__ = "Integer32"
_TeraSonetVTIdIfIndex_Object = MibTableColumn
teraSonetVTIdIfIndex = _TeraSonetVTIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 6, 1, 4),
    _TeraSonetVTIdIfIndex_Type()
)
teraSonetVTIdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTIdIfIndex.setStatus("mandatory")
_TeraSonetSectionCurrTotalTable_Object = MibTable
teraSonetSectionCurrTotalTable = _TeraSonetSectionCurrTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 7)
)
if mibBuilder.loadTexts:
    teraSonetSectionCurrTotalTable.setStatus("mandatory")
_TeraSonetSectionCurrTotalTableEntry_Object = MibTableRow
teraSonetSectionCurrTotalTableEntry = _TeraSonetSectionCurrTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 7, 1)
)
teraSonetSectionCurrTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetSectionCurrTotalTableEntry.setStatus("mandatory")


class _TeraSonetSectionCurrTotalStatus_Type(Integer32):
    """Custom type teraSonetSectionCurrTotalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_TeraSonetSectionCurrTotalStatus_Type.__name__ = "Integer32"
_TeraSonetSectionCurrTotalStatus_Object = MibTableColumn
teraSonetSectionCurrTotalStatus = _TeraSonetSectionCurrTotalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 7, 1, 1),
    _TeraSonetSectionCurrTotalStatus_Type()
)
teraSonetSectionCurrTotalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionCurrTotalStatus.setStatus("mandatory")
_TeraSonetSectionCurrTotalESs_Type = Gauge32
_TeraSonetSectionCurrTotalESs_Object = MibTableColumn
teraSonetSectionCurrTotalESs = _TeraSonetSectionCurrTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 7, 1, 2),
    _TeraSonetSectionCurrTotalESs_Type()
)
teraSonetSectionCurrTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionCurrTotalESs.setStatus("mandatory")
_TeraSonetSectionCurrTotalSESs_Type = Gauge32
_TeraSonetSectionCurrTotalSESs_Object = MibTableColumn
teraSonetSectionCurrTotalSESs = _TeraSonetSectionCurrTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 7, 1, 3),
    _TeraSonetSectionCurrTotalSESs_Type()
)
teraSonetSectionCurrTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionCurrTotalSESs.setStatus("mandatory")
_TeraSonetSectionCurrTotalSEFSs_Type = Gauge32
_TeraSonetSectionCurrTotalSEFSs_Object = MibTableColumn
teraSonetSectionCurrTotalSEFSs = _TeraSonetSectionCurrTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 7, 1, 4),
    _TeraSonetSectionCurrTotalSEFSs_Type()
)
teraSonetSectionCurrTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionCurrTotalSEFSs.setStatus("mandatory")
_TeraSonetSectionCurrTotalCVs_Type = Gauge32
_TeraSonetSectionCurrTotalCVs_Object = MibTableColumn
teraSonetSectionCurrTotalCVs = _TeraSonetSectionCurrTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 7, 1, 5),
    _TeraSonetSectionCurrTotalCVs_Type()
)
teraSonetSectionCurrTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionCurrTotalCVs.setStatus("mandatory")


class _TeraSonetTotalPerfStat_Type(Integer32):
    """Custom type teraSonetTotalPerfStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_TeraSonetTotalPerfStat_Type.__name__ = "Integer32"
_TeraSonetTotalPerfStat_Object = MibTableColumn
teraSonetTotalPerfStat = _TeraSonetTotalPerfStat_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 7, 1, 6),
    _TeraSonetTotalPerfStat_Type()
)
teraSonetTotalPerfStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetTotalPerfStat.setStatus("mandatory")
_TeraSonetSectionTotalTable_Object = MibTable
teraSonetSectionTotalTable = _TeraSonetSectionTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 8)
)
if mibBuilder.loadTexts:
    teraSonetSectionTotalTable.setStatus("mandatory")
_TeraSonetSectionTotalTableEntry_Object = MibTableRow
teraSonetSectionTotalTableEntry = _TeraSonetSectionTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 8, 1)
)
teraSonetSectionTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
    (0, "TERAWAVE-teraSonet-MIB", "teraSonetSectionTotalNumber"),
)
if mibBuilder.loadTexts:
    teraSonetSectionTotalTableEntry.setStatus("mandatory")


class _TeraSonetSectionTotalNumber_Type(Integer32):
    """Custom type teraSonetSectionTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraSonetSectionTotalNumber_Type.__name__ = "Integer32"
_TeraSonetSectionTotalNumber_Object = MibTableColumn
teraSonetSectionTotalNumber = _TeraSonetSectionTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 8, 1, 1),
    _TeraSonetSectionTotalNumber_Type()
)
teraSonetSectionTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionTotalNumber.setStatus("mandatory")
_TeraSonetSectionTotalESs_Type = Gauge32
_TeraSonetSectionTotalESs_Object = MibTableColumn
teraSonetSectionTotalESs = _TeraSonetSectionTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 8, 1, 2),
    _TeraSonetSectionTotalESs_Type()
)
teraSonetSectionTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionTotalESs.setStatus("mandatory")
_TeraSonetSectionTotalSESs_Type = Gauge32
_TeraSonetSectionTotalSESs_Object = MibTableColumn
teraSonetSectionTotalSESs = _TeraSonetSectionTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 8, 1, 3),
    _TeraSonetSectionTotalSESs_Type()
)
teraSonetSectionTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionTotalSESs.setStatus("mandatory")
_TeraSonetSectionTotalSEFSs_Type = Gauge32
_TeraSonetSectionTotalSEFSs_Object = MibTableColumn
teraSonetSectionTotalSEFSs = _TeraSonetSectionTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 8, 1, 4),
    _TeraSonetSectionTotalSEFSs_Type()
)
teraSonetSectionTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionTotalSEFSs.setStatus("mandatory")
_TeraSonetSectionTotalCVs_Type = Gauge32
_TeraSonetSectionTotalCVs_Object = MibTableColumn
teraSonetSectionTotalCVs = _TeraSonetSectionTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 8, 1, 5),
    _TeraSonetSectionTotalCVs_Type()
)
teraSonetSectionTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionTotalCVs.setStatus("mandatory")
_TeraSonetSectionTotalValidData_Type = Integer32
_TeraSonetSectionTotalValidData_Object = MibTableColumn
teraSonetSectionTotalValidData = _TeraSonetSectionTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 8, 1, 6),
    _TeraSonetSectionTotalValidData_Type()
)
teraSonetSectionTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetSectionTotalValidData.setStatus("mandatory")
_TeraSonetLineCurrTotalTable_Object = MibTable
teraSonetLineCurrTotalTable = _TeraSonetLineCurrTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 9)
)
if mibBuilder.loadTexts:
    teraSonetLineCurrTotalTable.setStatus("mandatory")
_TeraSonetLineCurrTotalTableEntry_Object = MibTableRow
teraSonetLineCurrTotalTableEntry = _TeraSonetLineCurrTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 9, 1)
)
teraSonetLineCurrTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetLineCurrTotalTableEntry.setStatus("mandatory")


class _TeraSonetLineCurrTotalStatus_Type(Integer32):
    """Custom type teraSonetLineCurrTotalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_TeraSonetLineCurrTotalStatus_Type.__name__ = "Integer32"
_TeraSonetLineCurrTotalStatus_Object = MibTableColumn
teraSonetLineCurrTotalStatus = _TeraSonetLineCurrTotalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 9, 1, 1),
    _TeraSonetLineCurrTotalStatus_Type()
)
teraSonetLineCurrTotalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetLineCurrTotalStatus.setStatus("mandatory")
_TeraSonetLineCurrTotalESs_Type = Gauge32
_TeraSonetLineCurrTotalESs_Object = MibTableColumn
teraSonetLineCurrTotalESs = _TeraSonetLineCurrTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 9, 1, 2),
    _TeraSonetLineCurrTotalESs_Type()
)
teraSonetLineCurrTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetLineCurrTotalESs.setStatus("mandatory")
_TeraSonetLineCurrTotalSESs_Type = Gauge32
_TeraSonetLineCurrTotalSESs_Object = MibTableColumn
teraSonetLineCurrTotalSESs = _TeraSonetLineCurrTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 9, 1, 3),
    _TeraSonetLineCurrTotalSESs_Type()
)
teraSonetLineCurrTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetLineCurrTotalSESs.setStatus("mandatory")
_TeraSonetLineCurrTotalCVs_Type = Gauge32
_TeraSonetLineCurrTotalCVs_Object = MibTableColumn
teraSonetLineCurrTotalCVs = _TeraSonetLineCurrTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 9, 1, 4),
    _TeraSonetLineCurrTotalCVs_Type()
)
teraSonetLineCurrTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetLineCurrTotalCVs.setStatus("mandatory")
_TeraSonetLineCurrTotalUASs_Type = Gauge32
_TeraSonetLineCurrTotalUASs_Object = MibTableColumn
teraSonetLineCurrTotalUASs = _TeraSonetLineCurrTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 9, 1, 5),
    _TeraSonetLineCurrTotalUASs_Type()
)
teraSonetLineCurrTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetLineCurrTotalUASs.setStatus("mandatory")
_TeraSonetLineTotalTable_Object = MibTable
teraSonetLineTotalTable = _TeraSonetLineTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 10)
)
if mibBuilder.loadTexts:
    teraSonetLineTotalTable.setStatus("mandatory")
_TeraSonetLineTotalTableEntry_Object = MibTableRow
teraSonetLineTotalTableEntry = _TeraSonetLineTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 10, 1)
)
teraSonetLineTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
    (0, "TERAWAVE-teraSonet-MIB", "teraSonetLineTotalNumber"),
)
if mibBuilder.loadTexts:
    teraSonetLineTotalTableEntry.setStatus("mandatory")


class _TeraSonetLineTotalNumber_Type(Integer32):
    """Custom type teraSonetLineTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraSonetLineTotalNumber_Type.__name__ = "Integer32"
_TeraSonetLineTotalNumber_Object = MibTableColumn
teraSonetLineTotalNumber = _TeraSonetLineTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 10, 1, 1),
    _TeraSonetLineTotalNumber_Type()
)
teraSonetLineTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetLineTotalNumber.setStatus("mandatory")
_TeraSonetLineTotalESs_Type = Gauge32
_TeraSonetLineTotalESs_Object = MibTableColumn
teraSonetLineTotalESs = _TeraSonetLineTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 10, 1, 2),
    _TeraSonetLineTotalESs_Type()
)
teraSonetLineTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetLineTotalESs.setStatus("mandatory")
_TeraSonetLineTotalSESs_Type = Gauge32
_TeraSonetLineTotalSESs_Object = MibTableColumn
teraSonetLineTotalSESs = _TeraSonetLineTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 10, 1, 3),
    _TeraSonetLineTotalSESs_Type()
)
teraSonetLineTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetLineTotalSESs.setStatus("mandatory")
_TeraSonetLineTotalCVs_Type = Gauge32
_TeraSonetLineTotalCVs_Object = MibTableColumn
teraSonetLineTotalCVs = _TeraSonetLineTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 10, 1, 4),
    _TeraSonetLineTotalCVs_Type()
)
teraSonetLineTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetLineTotalCVs.setStatus("mandatory")
_TeraSonetLineTotalUASs_Type = Gauge32
_TeraSonetLineTotalUASs_Object = MibTableColumn
teraSonetLineTotalUASs = _TeraSonetLineTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 10, 1, 5),
    _TeraSonetLineTotalUASs_Type()
)
teraSonetLineTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetLineTotalUASs.setStatus("mandatory")
_TeraSonetLineTotalValidData_Type = Integer32
_TeraSonetLineTotalValidData_Object = MibTableColumn
teraSonetLineTotalValidData = _TeraSonetLineTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 10, 1, 6),
    _TeraSonetLineTotalValidData_Type()
)
teraSonetLineTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetLineTotalValidData.setStatus("mandatory")
_TeraSonetFarEndLineCurrTotalTable_Object = MibTable
teraSonetFarEndLineCurrTotalTable = _TeraSonetFarEndLineCurrTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 11)
)
if mibBuilder.loadTexts:
    teraSonetFarEndLineCurrTotalTable.setStatus("mandatory")
_TeraSonetFarEndLineCurrTotalTableEntry_Object = MibTableRow
teraSonetFarEndLineCurrTotalTableEntry = _TeraSonetFarEndLineCurrTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 11, 1)
)
teraSonetFarEndLineCurrTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetFarEndLineCurrTotalTableEntry.setStatus("mandatory")
_TeraSonetFarEndLineCurrTotalESs_Type = Gauge32
_TeraSonetFarEndLineCurrTotalESs_Object = MibTableColumn
teraSonetFarEndLineCurrTotalESs = _TeraSonetFarEndLineCurrTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 11, 1, 1),
    _TeraSonetFarEndLineCurrTotalESs_Type()
)
teraSonetFarEndLineCurrTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndLineCurrTotalESs.setStatus("mandatory")
_TeraSonetFarEndLineCurrTotalSESs_Type = Gauge32
_TeraSonetFarEndLineCurrTotalSESs_Object = MibTableColumn
teraSonetFarEndLineCurrTotalSESs = _TeraSonetFarEndLineCurrTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 11, 1, 2),
    _TeraSonetFarEndLineCurrTotalSESs_Type()
)
teraSonetFarEndLineCurrTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndLineCurrTotalSESs.setStatus("mandatory")
_TeraSonetFarEndLineCurrTotalCVs_Type = Gauge32
_TeraSonetFarEndLineCurrTotalCVs_Object = MibTableColumn
teraSonetFarEndLineCurrTotalCVs = _TeraSonetFarEndLineCurrTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 11, 1, 3),
    _TeraSonetFarEndLineCurrTotalCVs_Type()
)
teraSonetFarEndLineCurrTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndLineCurrTotalCVs.setStatus("mandatory")
_TeraSonetFarEndLineCurrTotalUASs_Type = Gauge32
_TeraSonetFarEndLineCurrTotalUASs_Object = MibTableColumn
teraSonetFarEndLineCurrTotalUASs = _TeraSonetFarEndLineCurrTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 11, 1, 4),
    _TeraSonetFarEndLineCurrTotalUASs_Type()
)
teraSonetFarEndLineCurrTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndLineCurrTotalUASs.setStatus("mandatory")
_TeraSonetFarEndLineTotalTable_Object = MibTable
teraSonetFarEndLineTotalTable = _TeraSonetFarEndLineTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 12)
)
if mibBuilder.loadTexts:
    teraSonetFarEndLineTotalTable.setStatus("mandatory")
_TeraSonetFarEndLineTotalTableEntry_Object = MibTableRow
teraSonetFarEndLineTotalTableEntry = _TeraSonetFarEndLineTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 12, 1)
)
teraSonetFarEndLineTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
    (0, "TERAWAVE-teraSonet-MIB", "teraSonetFarEndLineTotalNumber"),
)
if mibBuilder.loadTexts:
    teraSonetFarEndLineTotalTableEntry.setStatus("mandatory")


class _TeraSonetFarEndLineTotalNumber_Type(Integer32):
    """Custom type teraSonetFarEndLineTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraSonetFarEndLineTotalNumber_Type.__name__ = "Integer32"
_TeraSonetFarEndLineTotalNumber_Object = MibTableColumn
teraSonetFarEndLineTotalNumber = _TeraSonetFarEndLineTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 12, 1, 1),
    _TeraSonetFarEndLineTotalNumber_Type()
)
teraSonetFarEndLineTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndLineTotalNumber.setStatus("mandatory")
_TeraSonetFarEndLineTotalESs_Type = Gauge32
_TeraSonetFarEndLineTotalESs_Object = MibTableColumn
teraSonetFarEndLineTotalESs = _TeraSonetFarEndLineTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 12, 1, 2),
    _TeraSonetFarEndLineTotalESs_Type()
)
teraSonetFarEndLineTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndLineTotalESs.setStatus("mandatory")
_TeraSonetFarEndLineTotalSESs_Type = Gauge32
_TeraSonetFarEndLineTotalSESs_Object = MibTableColumn
teraSonetFarEndLineTotalSESs = _TeraSonetFarEndLineTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 12, 1, 3),
    _TeraSonetFarEndLineTotalSESs_Type()
)
teraSonetFarEndLineTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndLineTotalSESs.setStatus("mandatory")
_TeraSonetFarEndLineTotalCVs_Type = Gauge32
_TeraSonetFarEndLineTotalCVs_Object = MibTableColumn
teraSonetFarEndLineTotalCVs = _TeraSonetFarEndLineTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 12, 1, 4),
    _TeraSonetFarEndLineTotalCVs_Type()
)
teraSonetFarEndLineTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndLineTotalCVs.setStatus("mandatory")
_TeraSonetFarEndLineTotalUASs_Type = Gauge32
_TeraSonetFarEndLineTotalUASs_Object = MibTableColumn
teraSonetFarEndLineTotalUASs = _TeraSonetFarEndLineTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 12, 1, 5),
    _TeraSonetFarEndLineTotalUASs_Type()
)
teraSonetFarEndLineTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndLineTotalUASs.setStatus("mandatory")
_TeraSonetFarEndLineTotalValidData_Type = Integer32
_TeraSonetFarEndLineTotalValidData_Object = MibTableColumn
teraSonetFarEndLineTotalValidData = _TeraSonetFarEndLineTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 12, 1, 6),
    _TeraSonetFarEndLineTotalValidData_Type()
)
teraSonetFarEndLineTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndLineTotalValidData.setStatus("mandatory")
_TeraSonetPathCurrTotalTable_Object = MibTable
teraSonetPathCurrTotalTable = _TeraSonetPathCurrTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 13)
)
if mibBuilder.loadTexts:
    teraSonetPathCurrTotalTable.setStatus("mandatory")
_TeraSonetPathCurrTotalTableEntry_Object = MibTableRow
teraSonetPathCurrTotalTableEntry = _TeraSonetPathCurrTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 13, 1)
)
teraSonetPathCurrTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetPathCurrTotalTableEntry.setStatus("mandatory")


class _TeraSonetPathCurrTotalWidth_Type(Integer32):
    """Custom type teraSonetPathCurrTotalWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("sts1", 1),
          ("sts12cSTM4", 3),
          ("sts3cSTM1", 2),
          ("sts48cSTM16", 5))
    )


_TeraSonetPathCurrTotalWidth_Type.__name__ = "Integer32"
_TeraSonetPathCurrTotalWidth_Object = MibTableColumn
teraSonetPathCurrTotalWidth = _TeraSonetPathCurrTotalWidth_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 13, 1, 1),
    _TeraSonetPathCurrTotalWidth_Type()
)
teraSonetPathCurrTotalWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathCurrTotalWidth.setStatus("mandatory")


class _TeraSonetPathCurrTotalStatus_Type(Integer32):
    """Custom type teraSonetPathCurrTotalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 62),
    )


_TeraSonetPathCurrTotalStatus_Type.__name__ = "Integer32"
_TeraSonetPathCurrTotalStatus_Object = MibTableColumn
teraSonetPathCurrTotalStatus = _TeraSonetPathCurrTotalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 13, 1, 2),
    _TeraSonetPathCurrTotalStatus_Type()
)
teraSonetPathCurrTotalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathCurrTotalStatus.setStatus("mandatory")
_TeraSonetPathCurrTotalESs_Type = Gauge32
_TeraSonetPathCurrTotalESs_Object = MibTableColumn
teraSonetPathCurrTotalESs = _TeraSonetPathCurrTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 13, 1, 3),
    _TeraSonetPathCurrTotalESs_Type()
)
teraSonetPathCurrTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathCurrTotalESs.setStatus("mandatory")
_TeraSonetPathCurrTotalSESs_Type = Gauge32
_TeraSonetPathCurrTotalSESs_Object = MibTableColumn
teraSonetPathCurrTotalSESs = _TeraSonetPathCurrTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 13, 1, 4),
    _TeraSonetPathCurrTotalSESs_Type()
)
teraSonetPathCurrTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathCurrTotalSESs.setStatus("mandatory")
_TeraSonetPathCurrTotalCVs_Type = Gauge32
_TeraSonetPathCurrTotalCVs_Object = MibTableColumn
teraSonetPathCurrTotalCVs = _TeraSonetPathCurrTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 13, 1, 5),
    _TeraSonetPathCurrTotalCVs_Type()
)
teraSonetPathCurrTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathCurrTotalCVs.setStatus("mandatory")
_TeraSonetPathCurrTotalUASs_Type = Gauge32
_TeraSonetPathCurrTotalUASs_Object = MibTableColumn
teraSonetPathCurrTotalUASs = _TeraSonetPathCurrTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 13, 1, 6),
    _TeraSonetPathCurrTotalUASs_Type()
)
teraSonetPathCurrTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathCurrTotalUASs.setStatus("mandatory")
_TeraSonetPathTotalTable_Object = MibTable
teraSonetPathTotalTable = _TeraSonetPathTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 14)
)
if mibBuilder.loadTexts:
    teraSonetPathTotalTable.setStatus("mandatory")
_TeraSonetPathTotalTableEntry_Object = MibTableRow
teraSonetPathTotalTableEntry = _TeraSonetPathTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 14, 1)
)
teraSonetPathTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
    (0, "TERAWAVE-teraSonet-MIB", "teraSonetPathTotalNumber"),
)
if mibBuilder.loadTexts:
    teraSonetPathTotalTableEntry.setStatus("mandatory")


class _TeraSonetPathTotalNumber_Type(Integer32):
    """Custom type teraSonetPathTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraSonetPathTotalNumber_Type.__name__ = "Integer32"
_TeraSonetPathTotalNumber_Object = MibTableColumn
teraSonetPathTotalNumber = _TeraSonetPathTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 14, 1, 1),
    _TeraSonetPathTotalNumber_Type()
)
teraSonetPathTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathTotalNumber.setStatus("mandatory")
_TeraSonetPathTotalESs_Type = Gauge32
_TeraSonetPathTotalESs_Object = MibTableColumn
teraSonetPathTotalESs = _TeraSonetPathTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 14, 1, 2),
    _TeraSonetPathTotalESs_Type()
)
teraSonetPathTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathTotalESs.setStatus("mandatory")
_TeraSonetPathTotalSESs_Type = Gauge32
_TeraSonetPathTotalSESs_Object = MibTableColumn
teraSonetPathTotalSESs = _TeraSonetPathTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 14, 1, 3),
    _TeraSonetPathTotalSESs_Type()
)
teraSonetPathTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathTotalSESs.setStatus("mandatory")
_TeraSonetPathTotalCVs_Type = Gauge32
_TeraSonetPathTotalCVs_Object = MibTableColumn
teraSonetPathTotalCVs = _TeraSonetPathTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 14, 1, 4),
    _TeraSonetPathTotalCVs_Type()
)
teraSonetPathTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathTotalCVs.setStatus("mandatory")
_TeraSonetPathTotalUASs_Type = Gauge32
_TeraSonetPathTotalUASs_Object = MibTableColumn
teraSonetPathTotalUASs = _TeraSonetPathTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 14, 1, 5),
    _TeraSonetPathTotalUASs_Type()
)
teraSonetPathTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathTotalUASs.setStatus("mandatory")
_TeraSonetPathTotalValidData_Type = Integer32
_TeraSonetPathTotalValidData_Object = MibTableColumn
teraSonetPathTotalValidData = _TeraSonetPathTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 14, 1, 6),
    _TeraSonetPathTotalValidData_Type()
)
teraSonetPathTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetPathTotalValidData.setStatus("mandatory")
_TeraSonetFarEndPathCurrTotalTable_Object = MibTable
teraSonetFarEndPathCurrTotalTable = _TeraSonetFarEndPathCurrTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 15)
)
if mibBuilder.loadTexts:
    teraSonetFarEndPathCurrTotalTable.setStatus("mandatory")
_TeraSonetFarEndPathCurrTotalTableEntry_Object = MibTableRow
teraSonetFarEndPathCurrTotalTableEntry = _TeraSonetFarEndPathCurrTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 15, 1)
)
teraSonetFarEndPathCurrTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetFarEndPathCurrTotalTableEntry.setStatus("mandatory")
_TeraSonetFarEndPathCurrTotalESs_Type = Gauge32
_TeraSonetFarEndPathCurrTotalESs_Object = MibTableColumn
teraSonetFarEndPathCurrTotalESs = _TeraSonetFarEndPathCurrTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 15, 1, 1),
    _TeraSonetFarEndPathCurrTotalESs_Type()
)
teraSonetFarEndPathCurrTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndPathCurrTotalESs.setStatus("mandatory")
_TeraSonetFarEndPathCurrTotalSESs_Type = Gauge32
_TeraSonetFarEndPathCurrTotalSESs_Object = MibTableColumn
teraSonetFarEndPathCurrTotalSESs = _TeraSonetFarEndPathCurrTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 15, 1, 2),
    _TeraSonetFarEndPathCurrTotalSESs_Type()
)
teraSonetFarEndPathCurrTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndPathCurrTotalSESs.setStatus("mandatory")
_TeraSonetFarEndPathCurrTotalCVs_Type = Gauge32
_TeraSonetFarEndPathCurrTotalCVs_Object = MibTableColumn
teraSonetFarEndPathCurrTotalCVs = _TeraSonetFarEndPathCurrTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 15, 1, 3),
    _TeraSonetFarEndPathCurrTotalCVs_Type()
)
teraSonetFarEndPathCurrTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndPathCurrTotalCVs.setStatus("mandatory")
_TeraSonetFarEndPathCurrTotalUASs_Type = Gauge32
_TeraSonetFarEndPathCurrTotalUASs_Object = MibTableColumn
teraSonetFarEndPathCurrTotalUASs = _TeraSonetFarEndPathCurrTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 15, 1, 4),
    _TeraSonetFarEndPathCurrTotalUASs_Type()
)
teraSonetFarEndPathCurrTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndPathCurrTotalUASs.setStatus("mandatory")
_TeraSonetFarEndPathTotalTable_Object = MibTable
teraSonetFarEndPathTotalTable = _TeraSonetFarEndPathTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 16)
)
if mibBuilder.loadTexts:
    teraSonetFarEndPathTotalTable.setStatus("mandatory")
_TeraSonetFarEndPathTotalTableEntry_Object = MibTableRow
teraSonetFarEndPathTotalTableEntry = _TeraSonetFarEndPathTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 16, 1)
)
teraSonetFarEndPathTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
    (0, "TERAWAVE-teraSonet-MIB", "teraSonetFarEndPathTotalNumber"),
)
if mibBuilder.loadTexts:
    teraSonetFarEndPathTotalTableEntry.setStatus("mandatory")


class _TeraSonetFarEndPathTotalNumber_Type(Integer32):
    """Custom type teraSonetFarEndPathTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraSonetFarEndPathTotalNumber_Type.__name__ = "Integer32"
_TeraSonetFarEndPathTotalNumber_Object = MibTableColumn
teraSonetFarEndPathTotalNumber = _TeraSonetFarEndPathTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 16, 1, 1),
    _TeraSonetFarEndPathTotalNumber_Type()
)
teraSonetFarEndPathTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndPathTotalNumber.setStatus("mandatory")
_TeraSonetFarEndPathTotalESs_Type = Gauge32
_TeraSonetFarEndPathTotalESs_Object = MibTableColumn
teraSonetFarEndPathTotalESs = _TeraSonetFarEndPathTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 16, 1, 2),
    _TeraSonetFarEndPathTotalESs_Type()
)
teraSonetFarEndPathTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndPathTotalESs.setStatus("mandatory")
_TeraSonetFarEndPathTotalSESs_Type = Gauge32
_TeraSonetFarEndPathTotalSESs_Object = MibTableColumn
teraSonetFarEndPathTotalSESs = _TeraSonetFarEndPathTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 16, 1, 3),
    _TeraSonetFarEndPathTotalSESs_Type()
)
teraSonetFarEndPathTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndPathTotalSESs.setStatus("mandatory")
_TeraSonetFarEndPathTotalCVs_Type = Gauge32
_TeraSonetFarEndPathTotalCVs_Object = MibTableColumn
teraSonetFarEndPathTotalCVs = _TeraSonetFarEndPathTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 16, 1, 4),
    _TeraSonetFarEndPathTotalCVs_Type()
)
teraSonetFarEndPathTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndPathTotalCVs.setStatus("mandatory")
_TeraSonetFarEndPathTotalUASs_Type = Gauge32
_TeraSonetFarEndPathTotalUASs_Object = MibTableColumn
teraSonetFarEndPathTotalUASs = _TeraSonetFarEndPathTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 16, 1, 5),
    _TeraSonetFarEndPathTotalUASs_Type()
)
teraSonetFarEndPathTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndPathTotalUASs.setStatus("mandatory")
_TeraSonetFarEndPathTotalValidData_Type = Integer32
_TeraSonetFarEndPathTotalValidData_Object = MibTableColumn
teraSonetFarEndPathTotalValidData = _TeraSonetFarEndPathTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 16, 1, 6),
    _TeraSonetFarEndPathTotalValidData_Type()
)
teraSonetFarEndPathTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndPathTotalValidData.setStatus("mandatory")
_TeraSonetVTCurrTotalTable_Object = MibTable
teraSonetVTCurrTotalTable = _TeraSonetVTCurrTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 17)
)
if mibBuilder.loadTexts:
    teraSonetVTCurrTotalTable.setStatus("mandatory")
_TeraSonetVTCurrTotalTableEntry_Object = MibTableRow
teraSonetVTCurrTotalTableEntry = _TeraSonetVTCurrTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 17, 1)
)
teraSonetVTCurrTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetVTCurrTotalTableEntry.setStatus("mandatory")


class _TeraSonetVTCurrTotalWidth_Type(Integer32):
    """Custom type teraSonetVTCurrTotalWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vtWidth15VC11", 1),
          ("vtWidth2VC12", 2))
    )


_TeraSonetVTCurrTotalWidth_Type.__name__ = "Integer32"
_TeraSonetVTCurrTotalWidth_Object = MibTableColumn
teraSonetVTCurrTotalWidth = _TeraSonetVTCurrTotalWidth_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 17, 1, 1),
    _TeraSonetVTCurrTotalWidth_Type()
)
teraSonetVTCurrTotalWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTCurrTotalWidth.setStatus("mandatory")


class _TeraSonetVTCurrTotalStatus_Type(Integer32):
    """Custom type teraSonetVTCurrTotalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_TeraSonetVTCurrTotalStatus_Type.__name__ = "Integer32"
_TeraSonetVTCurrTotalStatus_Object = MibTableColumn
teraSonetVTCurrTotalStatus = _TeraSonetVTCurrTotalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 17, 1, 2),
    _TeraSonetVTCurrTotalStatus_Type()
)
teraSonetVTCurrTotalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTCurrTotalStatus.setStatus("mandatory")
_TeraSonetVTCurrTotalESs_Type = Gauge32
_TeraSonetVTCurrTotalESs_Object = MibTableColumn
teraSonetVTCurrTotalESs = _TeraSonetVTCurrTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 17, 1, 3),
    _TeraSonetVTCurrTotalESs_Type()
)
teraSonetVTCurrTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTCurrTotalESs.setStatus("mandatory")
_TeraSonetVTCurrTotalSESs_Type = Gauge32
_TeraSonetVTCurrTotalSESs_Object = MibTableColumn
teraSonetVTCurrTotalSESs = _TeraSonetVTCurrTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 17, 1, 4),
    _TeraSonetVTCurrTotalSESs_Type()
)
teraSonetVTCurrTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTCurrTotalSESs.setStatus("mandatory")
_TeraSonetVTCurrTotalCVs_Type = Gauge32
_TeraSonetVTCurrTotalCVs_Object = MibTableColumn
teraSonetVTCurrTotalCVs = _TeraSonetVTCurrTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 17, 1, 5),
    _TeraSonetVTCurrTotalCVs_Type()
)
teraSonetVTCurrTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTCurrTotalCVs.setStatus("mandatory")
_TeraSonetVTCurrTotalUASs_Type = Gauge32
_TeraSonetVTCurrTotalUASs_Object = MibTableColumn
teraSonetVTCurrTotalUASs = _TeraSonetVTCurrTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 17, 1, 6),
    _TeraSonetVTCurrTotalUASs_Type()
)
teraSonetVTCurrTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTCurrTotalUASs.setStatus("mandatory")


class _TeraSonetVTCurrTotalPerfStat_Type(Integer32):
    """Custom type teraSonetVTCurrTotalPerfStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("clrall", 3),
          ("ok", 1))
    )


_TeraSonetVTCurrTotalPerfStat_Type.__name__ = "Integer32"
_TeraSonetVTCurrTotalPerfStat_Object = MibTableColumn
teraSonetVTCurrTotalPerfStat = _TeraSonetVTCurrTotalPerfStat_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 17, 1, 7),
    _TeraSonetVTCurrTotalPerfStat_Type()
)
teraSonetVTCurrTotalPerfStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetVTCurrTotalPerfStat.setStatus("mandatory")
_TeraSonetVTTotalTable_Object = MibTable
teraSonetVTTotalTable = _TeraSonetVTTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 18)
)
if mibBuilder.loadTexts:
    teraSonetVTTotalTable.setStatus("mandatory")
_TeraSonetVTTotalTableEntry_Object = MibTableRow
teraSonetVTTotalTableEntry = _TeraSonetVTTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 18, 1)
)
teraSonetVTTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
    (0, "TERAWAVE-teraSonet-MIB", "teraSonetVTTotalNumber"),
)
if mibBuilder.loadTexts:
    teraSonetVTTotalTableEntry.setStatus("mandatory")


class _TeraSonetVTTotalNumber_Type(Integer32):
    """Custom type teraSonetVTTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraSonetVTTotalNumber_Type.__name__ = "Integer32"
_TeraSonetVTTotalNumber_Object = MibTableColumn
teraSonetVTTotalNumber = _TeraSonetVTTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 18, 1, 1),
    _TeraSonetVTTotalNumber_Type()
)
teraSonetVTTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTTotalNumber.setStatus("mandatory")
_TeraSonetVTTotalESs_Type = Gauge32
_TeraSonetVTTotalESs_Object = MibTableColumn
teraSonetVTTotalESs = _TeraSonetVTTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 18, 1, 2),
    _TeraSonetVTTotalESs_Type()
)
teraSonetVTTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTTotalESs.setStatus("mandatory")
_TeraSonetVTTotalSESs_Type = Gauge32
_TeraSonetVTTotalSESs_Object = MibTableColumn
teraSonetVTTotalSESs = _TeraSonetVTTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 18, 1, 3),
    _TeraSonetVTTotalSESs_Type()
)
teraSonetVTTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTTotalSESs.setStatus("mandatory")
_TeraSonetVTTotalCVs_Type = Gauge32
_TeraSonetVTTotalCVs_Object = MibTableColumn
teraSonetVTTotalCVs = _TeraSonetVTTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 18, 1, 4),
    _TeraSonetVTTotalCVs_Type()
)
teraSonetVTTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTTotalCVs.setStatus("mandatory")
_TeraSonetVTTotalUASs_Type = Gauge32
_TeraSonetVTTotalUASs_Object = MibTableColumn
teraSonetVTTotalUASs = _TeraSonetVTTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 18, 1, 5),
    _TeraSonetVTTotalUASs_Type()
)
teraSonetVTTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTTotalUASs.setStatus("mandatory")
_TeraSonetVTTotalValidData_Type = Integer32
_TeraSonetVTTotalValidData_Object = MibTableColumn
teraSonetVTTotalValidData = _TeraSonetVTTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 18, 1, 6),
    _TeraSonetVTTotalValidData_Type()
)
teraSonetVTTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetVTTotalValidData.setStatus("mandatory")
_TeraSonetFarEndVTCurrTotalTable_Object = MibTable
teraSonetFarEndVTCurrTotalTable = _TeraSonetFarEndVTCurrTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 19)
)
if mibBuilder.loadTexts:
    teraSonetFarEndVTCurrTotalTable.setStatus("mandatory")
_TeraSonetFarEndVTCurrTotalTableEntry_Object = MibTableRow
teraSonetFarEndVTCurrTotalTableEntry = _TeraSonetFarEndVTCurrTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 19, 1)
)
teraSonetFarEndVTCurrTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetFarEndVTCurrTotalTableEntry.setStatus("mandatory")
_TeraSonetFarEndVTCurrTotalESs_Type = Gauge32
_TeraSonetFarEndVTCurrTotalESs_Object = MibTableColumn
teraSonetFarEndVTCurrTotalESs = _TeraSonetFarEndVTCurrTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 19, 1, 1),
    _TeraSonetFarEndVTCurrTotalESs_Type()
)
teraSonetFarEndVTCurrTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndVTCurrTotalESs.setStatus("mandatory")
_TeraSonetFarEndVTCurrTotalSES_Type = Gauge32
_TeraSonetFarEndVTCurrTotalSES_Object = MibTableColumn
teraSonetFarEndVTCurrTotalSES = _TeraSonetFarEndVTCurrTotalSES_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 19, 1, 2),
    _TeraSonetFarEndVTCurrTotalSES_Type()
)
teraSonetFarEndVTCurrTotalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndVTCurrTotalSES.setStatus("mandatory")
_TeraSonetFarEndVTCurrTotalCVs_Type = Gauge32
_TeraSonetFarEndVTCurrTotalCVs_Object = MibTableColumn
teraSonetFarEndVTCurrTotalCVs = _TeraSonetFarEndVTCurrTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 19, 1, 3),
    _TeraSonetFarEndVTCurrTotalCVs_Type()
)
teraSonetFarEndVTCurrTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndVTCurrTotalCVs.setStatus("mandatory")
_TeraSonetFarEndVTCurrTotalUASs_Type = Gauge32
_TeraSonetFarEndVTCurrTotalUASs_Object = MibTableColumn
teraSonetFarEndVTCurrTotalUASs = _TeraSonetFarEndVTCurrTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 19, 1, 4),
    _TeraSonetFarEndVTCurrTotalUASs_Type()
)
teraSonetFarEndVTCurrTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndVTCurrTotalUASs.setStatus("mandatory")
_TeraSonetFarEndVTTotalTable_Object = MibTable
teraSonetFarEndVTTotalTable = _TeraSonetFarEndVTTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 20)
)
if mibBuilder.loadTexts:
    teraSonetFarEndVTTotalTable.setStatus("mandatory")
_TeraSonetFarEndVTTotalTableEntry_Object = MibTableRow
teraSonetFarEndVTTotalTableEntry = _TeraSonetFarEndVTTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 20, 1)
)
teraSonetFarEndVTTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
    (0, "TERAWAVE-teraSonet-MIB", "teraSonetFarEndVTTotalNumber"),
)
if mibBuilder.loadTexts:
    teraSonetFarEndVTTotalTableEntry.setStatus("mandatory")


class _TeraSonetFarEndVTTotalNumber_Type(Integer32):
    """Custom type teraSonetFarEndVTTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TeraSonetFarEndVTTotalNumber_Type.__name__ = "Integer32"
_TeraSonetFarEndVTTotalNumber_Object = MibTableColumn
teraSonetFarEndVTTotalNumber = _TeraSonetFarEndVTTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 20, 1, 1),
    _TeraSonetFarEndVTTotalNumber_Type()
)
teraSonetFarEndVTTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndVTTotalNumber.setStatus("mandatory")
_TeraSonetFarEndVTTotalESs_Type = Gauge32
_TeraSonetFarEndVTTotalESs_Object = MibTableColumn
teraSonetFarEndVTTotalESs = _TeraSonetFarEndVTTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 20, 1, 2),
    _TeraSonetFarEndVTTotalESs_Type()
)
teraSonetFarEndVTTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndVTTotalESs.setStatus("mandatory")
_TeraSonetFarEndVTTotalSESs_Type = Gauge32
_TeraSonetFarEndVTTotalSESs_Object = MibTableColumn
teraSonetFarEndVTTotalSESs = _TeraSonetFarEndVTTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 20, 1, 3),
    _TeraSonetFarEndVTTotalSESs_Type()
)
teraSonetFarEndVTTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndVTTotalSESs.setStatus("mandatory")
_TeraSonetFarEndVTTotalCVs_Type = Gauge32
_TeraSonetFarEndVTTotalCVs_Object = MibTableColumn
teraSonetFarEndVTTotalCVs = _TeraSonetFarEndVTTotalCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 20, 1, 4),
    _TeraSonetFarEndVTTotalCVs_Type()
)
teraSonetFarEndVTTotalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndVTTotalCVs.setStatus("mandatory")
_TeraSonetFarEndVTTotalUASs_Type = Gauge32
_TeraSonetFarEndVTTotalUASs_Object = MibTableColumn
teraSonetFarEndVTTotalUASs = _TeraSonetFarEndVTTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 20, 1, 5),
    _TeraSonetFarEndVTTotalUASs_Type()
)
teraSonetFarEndVTTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndVTTotalUASs.setStatus("mandatory")
_TeraSonetFarEndVTTotalValidData_Type = Integer32
_TeraSonetFarEndVTTotalValidData_Object = MibTableColumn
teraSonetFarEndVTTotalValidData = _TeraSonetFarEndVTTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 20, 1, 6),
    _TeraSonetFarEndVTTotalValidData_Type()
)
teraSonetFarEndVTTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSonetFarEndVTTotalValidData.setStatus("mandatory")
_TeraSonetVTConfigTable_Object = MibTable
teraSonetVTConfigTable = _TeraSonetVTConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 21)
)
if mibBuilder.loadTexts:
    teraSonetVTConfigTable.setStatus("mandatory")
_TeraSonetVTConfigTableEntry_Object = MibTableRow
teraSonetVTConfigTableEntry = _TeraSonetVTConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 21, 1)
)
teraSonetVTConfigTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSonet-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraSonetVTConfigTableEntry.setStatus("mandatory")


class _TeraSonetVTConfigERDIEnable_Type(Integer32):
    """Custom type teraSonetVTConfigERDIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TeraSonetVTConfigERDIEnable_Type.__name__ = "Integer32"
_TeraSonetVTConfigERDIEnable_Object = MibTableColumn
teraSonetVTConfigERDIEnable = _TeraSonetVTConfigERDIEnable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 21, 1, 1),
    _TeraSonetVTConfigERDIEnable_Type()
)
teraSonetVTConfigERDIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetVTConfigERDIEnable.setStatus("mandatory")


class _TeraSonetVTLoopbackConfig_Type(Integer32):
    """Custom type teraSonetVTLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diagLoop", 3),
          ("lineLoop", 2),
          ("noLoop", 1))
    )


_TeraSonetVTLoopbackConfig_Type.__name__ = "Integer32"
_TeraSonetVTLoopbackConfig_Object = MibTableColumn
teraSonetVTLoopbackConfig = _TeraSonetVTLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 4513, 10, 21, 1, 2),
    _TeraSonetVTLoopbackConfig_Type()
)
teraSonetVTLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraSonetVTLoopbackConfig.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraSonet-MIB",
    **{"terawave": terawave,
       "teraSonetGroup": teraSonetGroup,
       "teraSonetMediumTable": teraSonetMediumTable,
       "teraSonetMediumTableEntry": teraSonetMediumTableEntry,
       "teraSonetMode": teraSonetMode,
       "teraSonetStm1Mapping": teraSonetStm1Mapping,
       "teraSonetSDThreshold": teraSonetSDThreshold,
       "teraSonetSFThreshold": teraSonetSFThreshold,
       "teraSonetMediumTotalTimeElapsed": teraSonetMediumTotalTimeElapsed,
       "teraSonetMediumValidTotalIntervals": teraSonetMediumValidTotalIntervals,
       "teraSonetMediumInvalidTotalIntervals": teraSonetMediumInvalidTotalIntervals,
       "teraSonetSectionTable": teraSonetSectionTable,
       "teraSonetSectionTableEntry": teraSonetSectionTableEntry,
       "teraSonetSectionTraceLenTx": teraSonetSectionTraceLenTx,
       "teraSonetSectionTraceTx": teraSonetSectionTraceTx,
       "teraSonetSectionTraceLenRx": teraSonetSectionTraceLenRx,
       "teraSonetSectionTraceRx": teraSonetSectionTraceRx,
       "teraSonetPathOverheadTable": teraSonetPathOverheadTable,
       "teraSonetPathOverheadTableEntry": teraSonetPathOverheadTableEntry,
       "teraSonetPathSigLabelTx": teraSonetPathSigLabelTx,
       "teraSonetPathTraceLenTx": teraSonetPathTraceLenTx,
       "teraSonetPathTraceTx": teraSonetPathTraceTx,
       "teraSonetPathSigLabelRx": teraSonetPathSigLabelRx,
       "teraSonetPathTraceLenRx": teraSonetPathTraceLenRx,
       "teraSonetPathTraceRx": teraSonetPathTraceRx,
       "teraSonetMapperConfigTable": teraSonetMapperConfigTable,
       "teraSonetMapperConfigTableEntry": teraSonetMapperConfigTableEntry,
       "teraSonetMapperType": teraSonetMapperType,
       "teraSonetMapperLoopbackConfig": teraSonetMapperLoopbackConfig,
       "teraSonetPathIdTable": teraSonetPathIdTable,
       "teraSonetPathIdTableEntry": teraSonetPathIdTableEntry,
       "teraSonetPathIdSTS1": teraSonetPathIdSTS1,
       "teraSonetPathIdIfIndex": teraSonetPathIdIfIndex,
       "teraSonetVTIdTable": teraSonetVTIdTable,
       "teraSonetVTIdTableEntry": teraSonetVTIdTableEntry,
       "teraSonetVTIdSTS1": teraSonetVTIdSTS1,
       "teraSonetVTIdVTG": teraSonetVTIdVTG,
       "teraSonetVTIdVT": teraSonetVTIdVT,
       "teraSonetVTIdIfIndex": teraSonetVTIdIfIndex,
       "teraSonetSectionCurrTotalTable": teraSonetSectionCurrTotalTable,
       "teraSonetSectionCurrTotalTableEntry": teraSonetSectionCurrTotalTableEntry,
       "teraSonetSectionCurrTotalStatus": teraSonetSectionCurrTotalStatus,
       "teraSonetSectionCurrTotalESs": teraSonetSectionCurrTotalESs,
       "teraSonetSectionCurrTotalSESs": teraSonetSectionCurrTotalSESs,
       "teraSonetSectionCurrTotalSEFSs": teraSonetSectionCurrTotalSEFSs,
       "teraSonetSectionCurrTotalCVs": teraSonetSectionCurrTotalCVs,
       "teraSonetTotalPerfStat": teraSonetTotalPerfStat,
       "teraSonetSectionTotalTable": teraSonetSectionTotalTable,
       "teraSonetSectionTotalTableEntry": teraSonetSectionTotalTableEntry,
       "teraSonetSectionTotalNumber": teraSonetSectionTotalNumber,
       "teraSonetSectionTotalESs": teraSonetSectionTotalESs,
       "teraSonetSectionTotalSESs": teraSonetSectionTotalSESs,
       "teraSonetSectionTotalSEFSs": teraSonetSectionTotalSEFSs,
       "teraSonetSectionTotalCVs": teraSonetSectionTotalCVs,
       "teraSonetSectionTotalValidData": teraSonetSectionTotalValidData,
       "teraSonetLineCurrTotalTable": teraSonetLineCurrTotalTable,
       "teraSonetLineCurrTotalTableEntry": teraSonetLineCurrTotalTableEntry,
       "teraSonetLineCurrTotalStatus": teraSonetLineCurrTotalStatus,
       "teraSonetLineCurrTotalESs": teraSonetLineCurrTotalESs,
       "teraSonetLineCurrTotalSESs": teraSonetLineCurrTotalSESs,
       "teraSonetLineCurrTotalCVs": teraSonetLineCurrTotalCVs,
       "teraSonetLineCurrTotalUASs": teraSonetLineCurrTotalUASs,
       "teraSonetLineTotalTable": teraSonetLineTotalTable,
       "teraSonetLineTotalTableEntry": teraSonetLineTotalTableEntry,
       "teraSonetLineTotalNumber": teraSonetLineTotalNumber,
       "teraSonetLineTotalESs": teraSonetLineTotalESs,
       "teraSonetLineTotalSESs": teraSonetLineTotalSESs,
       "teraSonetLineTotalCVs": teraSonetLineTotalCVs,
       "teraSonetLineTotalUASs": teraSonetLineTotalUASs,
       "teraSonetLineTotalValidData": teraSonetLineTotalValidData,
       "teraSonetFarEndLineCurrTotalTable": teraSonetFarEndLineCurrTotalTable,
       "teraSonetFarEndLineCurrTotalTableEntry": teraSonetFarEndLineCurrTotalTableEntry,
       "teraSonetFarEndLineCurrTotalESs": teraSonetFarEndLineCurrTotalESs,
       "teraSonetFarEndLineCurrTotalSESs": teraSonetFarEndLineCurrTotalSESs,
       "teraSonetFarEndLineCurrTotalCVs": teraSonetFarEndLineCurrTotalCVs,
       "teraSonetFarEndLineCurrTotalUASs": teraSonetFarEndLineCurrTotalUASs,
       "teraSonetFarEndLineTotalTable": teraSonetFarEndLineTotalTable,
       "teraSonetFarEndLineTotalTableEntry": teraSonetFarEndLineTotalTableEntry,
       "teraSonetFarEndLineTotalNumber": teraSonetFarEndLineTotalNumber,
       "teraSonetFarEndLineTotalESs": teraSonetFarEndLineTotalESs,
       "teraSonetFarEndLineTotalSESs": teraSonetFarEndLineTotalSESs,
       "teraSonetFarEndLineTotalCVs": teraSonetFarEndLineTotalCVs,
       "teraSonetFarEndLineTotalUASs": teraSonetFarEndLineTotalUASs,
       "teraSonetFarEndLineTotalValidData": teraSonetFarEndLineTotalValidData,
       "teraSonetPathCurrTotalTable": teraSonetPathCurrTotalTable,
       "teraSonetPathCurrTotalTableEntry": teraSonetPathCurrTotalTableEntry,
       "teraSonetPathCurrTotalWidth": teraSonetPathCurrTotalWidth,
       "teraSonetPathCurrTotalStatus": teraSonetPathCurrTotalStatus,
       "teraSonetPathCurrTotalESs": teraSonetPathCurrTotalESs,
       "teraSonetPathCurrTotalSESs": teraSonetPathCurrTotalSESs,
       "teraSonetPathCurrTotalCVs": teraSonetPathCurrTotalCVs,
       "teraSonetPathCurrTotalUASs": teraSonetPathCurrTotalUASs,
       "teraSonetPathTotalTable": teraSonetPathTotalTable,
       "teraSonetPathTotalTableEntry": teraSonetPathTotalTableEntry,
       "teraSonetPathTotalNumber": teraSonetPathTotalNumber,
       "teraSonetPathTotalESs": teraSonetPathTotalESs,
       "teraSonetPathTotalSESs": teraSonetPathTotalSESs,
       "teraSonetPathTotalCVs": teraSonetPathTotalCVs,
       "teraSonetPathTotalUASs": teraSonetPathTotalUASs,
       "teraSonetPathTotalValidData": teraSonetPathTotalValidData,
       "teraSonetFarEndPathCurrTotalTable": teraSonetFarEndPathCurrTotalTable,
       "teraSonetFarEndPathCurrTotalTableEntry": teraSonetFarEndPathCurrTotalTableEntry,
       "teraSonetFarEndPathCurrTotalESs": teraSonetFarEndPathCurrTotalESs,
       "teraSonetFarEndPathCurrTotalSESs": teraSonetFarEndPathCurrTotalSESs,
       "teraSonetFarEndPathCurrTotalCVs": teraSonetFarEndPathCurrTotalCVs,
       "teraSonetFarEndPathCurrTotalUASs": teraSonetFarEndPathCurrTotalUASs,
       "teraSonetFarEndPathTotalTable": teraSonetFarEndPathTotalTable,
       "teraSonetFarEndPathTotalTableEntry": teraSonetFarEndPathTotalTableEntry,
       "teraSonetFarEndPathTotalNumber": teraSonetFarEndPathTotalNumber,
       "teraSonetFarEndPathTotalESs": teraSonetFarEndPathTotalESs,
       "teraSonetFarEndPathTotalSESs": teraSonetFarEndPathTotalSESs,
       "teraSonetFarEndPathTotalCVs": teraSonetFarEndPathTotalCVs,
       "teraSonetFarEndPathTotalUASs": teraSonetFarEndPathTotalUASs,
       "teraSonetFarEndPathTotalValidData": teraSonetFarEndPathTotalValidData,
       "teraSonetVTCurrTotalTable": teraSonetVTCurrTotalTable,
       "teraSonetVTCurrTotalTableEntry": teraSonetVTCurrTotalTableEntry,
       "teraSonetVTCurrTotalWidth": teraSonetVTCurrTotalWidth,
       "teraSonetVTCurrTotalStatus": teraSonetVTCurrTotalStatus,
       "teraSonetVTCurrTotalESs": teraSonetVTCurrTotalESs,
       "teraSonetVTCurrTotalSESs": teraSonetVTCurrTotalSESs,
       "teraSonetVTCurrTotalCVs": teraSonetVTCurrTotalCVs,
       "teraSonetVTCurrTotalUASs": teraSonetVTCurrTotalUASs,
       "teraSonetVTCurrTotalPerfStat": teraSonetVTCurrTotalPerfStat,
       "teraSonetVTTotalTable": teraSonetVTTotalTable,
       "teraSonetVTTotalTableEntry": teraSonetVTTotalTableEntry,
       "teraSonetVTTotalNumber": teraSonetVTTotalNumber,
       "teraSonetVTTotalESs": teraSonetVTTotalESs,
       "teraSonetVTTotalSESs": teraSonetVTTotalSESs,
       "teraSonetVTTotalCVs": teraSonetVTTotalCVs,
       "teraSonetVTTotalUASs": teraSonetVTTotalUASs,
       "teraSonetVTTotalValidData": teraSonetVTTotalValidData,
       "teraSonetFarEndVTCurrTotalTable": teraSonetFarEndVTCurrTotalTable,
       "teraSonetFarEndVTCurrTotalTableEntry": teraSonetFarEndVTCurrTotalTableEntry,
       "teraSonetFarEndVTCurrTotalESs": teraSonetFarEndVTCurrTotalESs,
       "teraSonetFarEndVTCurrTotalSES": teraSonetFarEndVTCurrTotalSES,
       "teraSonetFarEndVTCurrTotalCVs": teraSonetFarEndVTCurrTotalCVs,
       "teraSonetFarEndVTCurrTotalUASs": teraSonetFarEndVTCurrTotalUASs,
       "teraSonetFarEndVTTotalTable": teraSonetFarEndVTTotalTable,
       "teraSonetFarEndVTTotalTableEntry": teraSonetFarEndVTTotalTableEntry,
       "teraSonetFarEndVTTotalNumber": teraSonetFarEndVTTotalNumber,
       "teraSonetFarEndVTTotalESs": teraSonetFarEndVTTotalESs,
       "teraSonetFarEndVTTotalSESs": teraSonetFarEndVTTotalSESs,
       "teraSonetFarEndVTTotalCVs": teraSonetFarEndVTTotalCVs,
       "teraSonetFarEndVTTotalUASs": teraSonetFarEndVTTotalUASs,
       "teraSonetFarEndVTTotalValidData": teraSonetFarEndVTTotalValidData,
       "teraSonetVTConfigTable": teraSonetVTConfigTable,
       "teraSonetVTConfigTableEntry": teraSonetVTConfigTableEntry,
       "teraSonetVTConfigERDIEnable": teraSonetVTConfigERDIEnable,
       "teraSonetVTLoopbackConfig": teraSonetVTLoopbackConfig}
)
