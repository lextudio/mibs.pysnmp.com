# SNMP MIB module (CXDataScope-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXDataScope-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:19 2024
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

(cxDataScope,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxDataScope")

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

_DsControl_ObjectIdentity = ObjectIdentity
dsControl = _DsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1)
)
_DsDataBaseVersion_Type = OctetString
_DsDataBaseVersion_Object = MibScalar
dsDataBaseVersion = _DsDataBaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 1),
    _DsDataBaseVersion_Type()
)
dsDataBaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsDataBaseVersion.setStatus("mandatory")


class _DsDataBaseSize_Type(Integer32):
    """Custom type dsDataBaseSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsDataBaseSize_Type.__name__ = "Integer32"
_DsDataBaseSize_Object = MibScalar
dsDataBaseSize = _DsDataBaseSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 2),
    _DsDataBaseSize_Type()
)
dsDataBaseSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsDataBaseSize.setStatus("mandatory")


class _DsDataBaseReady_Type(Integer32):
    """Custom type dsDataBaseReady based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ready", 1),
          ("ready", 2))
    )


_DsDataBaseReady_Type.__name__ = "Integer32"
_DsDataBaseReady_Object = MibScalar
dsDataBaseReady = _DsDataBaseReady_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 3),
    _DsDataBaseReady_Type()
)
dsDataBaseReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsDataBaseReady.setStatus("mandatory")
_DsRTTYIpAddress_Type = IpAddress
_DsRTTYIpAddress_Object = MibScalar
dsRTTYIpAddress = _DsRTTYIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 4),
    _DsRTTYIpAddress_Type()
)
dsRTTYIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRTTYIpAddress.setStatus("mandatory")
_DsOutLostCounter1_Type = Counter32
_DsOutLostCounter1_Object = MibScalar
dsOutLostCounter1 = _DsOutLostCounter1_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 5),
    _DsOutLostCounter1_Type()
)
dsOutLostCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsOutLostCounter1.setStatus("mandatory")
_DsOutLostCounter2_Type = Counter32
_DsOutLostCounter2_Object = MibScalar
dsOutLostCounter2 = _DsOutLostCounter2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 6),
    _DsOutLostCounter2_Type()
)
dsOutLostCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsOutLostCounter2.setStatus("mandatory")
_DsOutLostCounter3_Type = Counter32
_DsOutLostCounter3_Object = MibScalar
dsOutLostCounter3 = _DsOutLostCounter3_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 7),
    _DsOutLostCounter3_Type()
)
dsOutLostCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsOutLostCounter3.setStatus("mandatory")
_DsDataBase_ObjectIdentity = ObjectIdentity
dsDataBase = _DsDataBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2)
)


class _DsOperationMode_Type(Integer32):
    """Custom type dsOperationMode based on Integer32"""
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
        *(("read-mode", 3),
          ("stop-mode", 1),
          ("write-mode", 2))
    )


_DsOperationMode_Type.__name__ = "Integer32"
_DsOperationMode_Object = MibScalar
dsOperationMode = _DsOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 1),
    _DsOperationMode_Type()
)
dsOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsOperationMode.setStatus("mandatory")
_DsTotalRecord_Type = Counter32
_DsTotalRecord_Object = MibScalar
dsTotalRecord = _DsTotalRecord_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 2),
    _DsTotalRecord_Type()
)
dsTotalRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsTotalRecord.setStatus("mandatory")
_DsOverwrittenRecord_Type = Counter32
_DsOverwrittenRecord_Object = MibScalar
dsOverwrittenRecord = _DsOverwrittenRecord_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 3),
    _DsOverwrittenRecord_Type()
)
dsOverwrittenRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsOverwrittenRecord.setStatus("mandatory")


class _DsReadNumberRecord_Type(Integer32):
    """Custom type dsReadNumberRecord based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsReadNumberRecord_Type.__name__ = "Integer32"
_DsReadNumberRecord_Object = MibScalar
dsReadNumberRecord = _DsReadNumberRecord_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 4),
    _DsReadNumberRecord_Type()
)
dsReadNumberRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsReadNumberRecord.setStatus("mandatory")


class _DsReadOutputDir_Type(Integer32):
    """Custom type dsReadOutputDir based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("to-RTTY-console", 2),
          ("to-local-console", 1))
    )


_DsReadOutputDir_Type.__name__ = "Integer32"
_DsReadOutputDir_Object = MibScalar
dsReadOutputDir = _DsReadOutputDir_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 5),
    _DsReadOutputDir_Type()
)
dsReadOutputDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsReadOutputDir.setStatus("mandatory")


class _DsDBControl_Type(Integer32):
    """Custom type dsDBControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_DsDBControl_Type.__name__ = "Integer32"
_DsDBControl_Object = MibScalar
dsDBControl = _DsDBControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 6),
    _DsDBControl_Type()
)
dsDBControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dsDBControl.setStatus("mandatory")


class _DsReadFormat_Type(Integer32):
    """Custom type dsReadFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii-format", 1),
          ("binary-format", 2))
    )


_DsReadFormat_Type.__name__ = "Integer32"
_DsReadFormat_Object = MibScalar
dsReadFormat = _DsReadFormat_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 7),
    _DsReadFormat_Type()
)
dsReadFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsReadFormat.setStatus("mandatory")
_DsRegistryTable_Object = MibTable
dsRegistryTable = _DsRegistryTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3)
)
if mibBuilder.loadTexts:
    dsRegistryTable.setStatus("mandatory")
_DsRegistryEntry_Object = MibTableRow
dsRegistryEntry = _DsRegistryEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1)
)
dsRegistryEntry.setIndexNames(
    (0, "CXDataScope-MIB", "dsRegAppID"),
)
if mibBuilder.loadTexts:
    dsRegistryEntry.setStatus("mandatory")
_DsRegAppID_Type = Integer32
_DsRegAppID_Object = MibTableColumn
dsRegAppID = _DsRegAppID_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 1),
    _DsRegAppID_Type()
)
dsRegAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRegAppID.setStatus("mandatory")
_DsRegTrafficType_Type = Integer32
_DsRegTrafficType_Object = MibTableColumn
dsRegTrafficType = _DsRegTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 2),
    _DsRegTrafficType_Type()
)
dsRegTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRegTrafficType.setStatus("mandatory")
_DsRegIFIndex_Type = Integer32
_DsRegIFIndex_Object = MibTableColumn
dsRegIFIndex = _DsRegIFIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 3),
    _DsRegIFIndex_Type()
)
dsRegIFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRegIFIndex.setStatus("mandatory")


class _DsRegDirFilter_Type(Integer32):
    """Custom type dsRegDirFilter based on Integer32"""
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
        *(("rx-only", 3),
          ("tx-and-rx", 1),
          ("tx-only", 2))
    )


_DsRegDirFilter_Type.__name__ = "Integer32"
_DsRegDirFilter_Object = MibTableColumn
dsRegDirFilter = _DsRegDirFilter_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 4),
    _DsRegDirFilter_Type()
)
dsRegDirFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegDirFilter.setStatus("mandatory")


class _DsRegState_Type(Integer32):
    """Custom type dsRegState based on Integer32"""
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


_DsRegState_Type.__name__ = "Integer32"
_DsRegState_Object = MibTableColumn
dsRegState = _DsRegState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 5),
    _DsRegState_Type()
)
dsRegState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegState.setStatus("mandatory")


class _DsRegDfMask_Type(OctetString):
    """Custom type dsRegDfMask based on OctetString"""
    defaultValue = OctetString("00000000")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DsRegDfMask_Type.__name__ = "OctetString"
_DsRegDfMask_Object = MibTableColumn
dsRegDfMask = _DsRegDfMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 6),
    _DsRegDfMask_Type()
)
dsRegDfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegDfMask.setStatus("mandatory")


class _DsRegDfValue_Type(OctetString):
    """Custom type dsRegDfValue based on OctetString"""
    defaultValue = OctetString("00000000")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DsRegDfValue_Type.__name__ = "OctetString"
_DsRegDfValue_Object = MibTableColumn
dsRegDfValue = _DsRegDfValue_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 7),
    _DsRegDfValue_Type()
)
dsRegDfValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegDfValue.setStatus("mandatory")


class _DsRegDfCriteria_Type(Integer32):
    """Custom type dsRegDfCriteria based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("not-equal", 2))
    )


_DsRegDfCriteria_Type.__name__ = "Integer32"
_DsRegDfCriteria_Object = MibTableColumn
dsRegDfCriteria = _DsRegDfCriteria_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 8),
    _DsRegDfCriteria_Type()
)
dsRegDfCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegDfCriteria.setStatus("mandatory")


class _DsRegDfOffset_Type(Integer32):
    """Custom type dsRegDfOffset based on Integer32"""
    defaultValue = 0


_DsRegDfOffset_Object = MibTableColumn
dsRegDfOffset = _DsRegDfOffset_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 9),
    _DsRegDfOffset_Type()
)
dsRegDfOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegDfOffset.setStatus("mandatory")


class _DsRegStartMask_Type(OctetString):
    """Custom type dsRegStartMask based on OctetString"""
    defaultValue = OctetString("00000000")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DsRegStartMask_Type.__name__ = "OctetString"
_DsRegStartMask_Object = MibTableColumn
dsRegStartMask = _DsRegStartMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 20),
    _DsRegStartMask_Type()
)
dsRegStartMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegStartMask.setStatus("mandatory")


class _DsRegStartValue_Type(OctetString):
    """Custom type dsRegStartValue based on OctetString"""
    defaultValue = OctetString("00000000")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DsRegStartValue_Type.__name__ = "OctetString"
_DsRegStartValue_Object = MibTableColumn
dsRegStartValue = _DsRegStartValue_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 21),
    _DsRegStartValue_Type()
)
dsRegStartValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegStartValue.setStatus("mandatory")


class _DsRegStartCriteria_Type(Integer32):
    """Custom type dsRegStartCriteria based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("not-equal", 2))
    )


_DsRegStartCriteria_Type.__name__ = "Integer32"
_DsRegStartCriteria_Object = MibTableColumn
dsRegStartCriteria = _DsRegStartCriteria_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 22),
    _DsRegStartCriteria_Type()
)
dsRegStartCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegStartCriteria.setStatus("mandatory")


class _DsRegStartOffset_Type(Integer32):
    """Custom type dsRegStartOffset based on Integer32"""
    defaultValue = 0


_DsRegStartOffset_Object = MibTableColumn
dsRegStartOffset = _DsRegStartOffset_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 23),
    _DsRegStartOffset_Type()
)
dsRegStartOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegStartOffset.setStatus("mandatory")


class _DsRegStopMask_Type(OctetString):
    """Custom type dsRegStopMask based on OctetString"""
    defaultValue = OctetString("00000000")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DsRegStopMask_Type.__name__ = "OctetString"
_DsRegStopMask_Object = MibTableColumn
dsRegStopMask = _DsRegStopMask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 24),
    _DsRegStopMask_Type()
)
dsRegStopMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegStopMask.setStatus("mandatory")


class _DsRegStopValue_Type(OctetString):
    """Custom type dsRegStopValue based on OctetString"""
    defaultValue = OctetString("00000000")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DsRegStopValue_Type.__name__ = "OctetString"
_DsRegStopValue_Object = MibTableColumn
dsRegStopValue = _DsRegStopValue_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 25),
    _DsRegStopValue_Type()
)
dsRegStopValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegStopValue.setStatus("mandatory")


class _DsRegStopCriteria_Type(Integer32):
    """Custom type dsRegStopCriteria based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("not-equal", 2))
    )


_DsRegStopCriteria_Type.__name__ = "Integer32"
_DsRegStopCriteria_Object = MibTableColumn
dsRegStopCriteria = _DsRegStopCriteria_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 26),
    _DsRegStopCriteria_Type()
)
dsRegStopCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegStopCriteria.setStatus("mandatory")


class _DsRegStopOffset_Type(Integer32):
    """Custom type dsRegStopOffset based on Integer32"""
    defaultValue = 0


_DsRegStopOffset_Object = MibTableColumn
dsRegStopOffset = _DsRegStopOffset_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 27),
    _DsRegStopOffset_Type()
)
dsRegStopOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegStopOffset.setStatus("mandatory")


class _DsRegStatus_Type(Integer32):
    """Custom type dsRegStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-recording", 1),
          ("recording", 2))
    )


_DsRegStatus_Type.__name__ = "Integer32"
_DsRegStatus_Object = MibTableColumn
dsRegStatus = _DsRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 41),
    _DsRegStatus_Type()
)
dsRegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRegStatus.setStatus("mandatory")


class _DsRegDataLength_Type(Integer32):
    """Custom type dsRegDataLength based on Integer32"""
    defaultValue = 0


_DsRegDataLength_Object = MibTableColumn
dsRegDataLength = _DsRegDataLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 42),
    _DsRegDataLength_Type()
)
dsRegDataLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegDataLength.setStatus("mandatory")


class _DsRegDataOffset_Type(Integer32):
    """Custom type dsRegDataOffset based on Integer32"""
    defaultValue = 0


_DsRegDataOffset_Object = MibTableColumn
dsRegDataOffset = _DsRegDataOffset_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 43),
    _DsRegDataOffset_Type()
)
dsRegDataOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegDataOffset.setStatus("mandatory")
_DsRegOutputDir_Type = Integer32
_DsRegOutputDir_Object = MibTableColumn
dsRegOutputDir = _DsRegOutputDir_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 44),
    _DsRegOutputDir_Type()
)
dsRegOutputDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegOutputDir.setStatus("mandatory")


class _DsRegOutputFormat_Type(Integer32):
    """Custom type dsRegOutputFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii-format", 1),
          ("binary-format", 2))
    )


_DsRegOutputFormat_Type.__name__ = "Integer32"
_DsRegOutputFormat_Object = MibTableColumn
dsRegOutputFormat = _DsRegOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 45),
    _DsRegOutputFormat_Type()
)
dsRegOutputFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRegOutputFormat.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXDataScope-MIB",
    **{"dsControl": dsControl,
       "dsDataBaseVersion": dsDataBaseVersion,
       "dsDataBaseSize": dsDataBaseSize,
       "dsDataBaseReady": dsDataBaseReady,
       "dsRTTYIpAddress": dsRTTYIpAddress,
       "dsOutLostCounter1": dsOutLostCounter1,
       "dsOutLostCounter2": dsOutLostCounter2,
       "dsOutLostCounter3": dsOutLostCounter3,
       "dsDataBase": dsDataBase,
       "dsOperationMode": dsOperationMode,
       "dsTotalRecord": dsTotalRecord,
       "dsOverwrittenRecord": dsOverwrittenRecord,
       "dsReadNumberRecord": dsReadNumberRecord,
       "dsReadOutputDir": dsReadOutputDir,
       "dsDBControl": dsDBControl,
       "dsReadFormat": dsReadFormat,
       "dsRegistryTable": dsRegistryTable,
       "dsRegistryEntry": dsRegistryEntry,
       "dsRegAppID": dsRegAppID,
       "dsRegTrafficType": dsRegTrafficType,
       "dsRegIFIndex": dsRegIFIndex,
       "dsRegDirFilter": dsRegDirFilter,
       "dsRegState": dsRegState,
       "dsRegDfMask": dsRegDfMask,
       "dsRegDfValue": dsRegDfValue,
       "dsRegDfCriteria": dsRegDfCriteria,
       "dsRegDfOffset": dsRegDfOffset,
       "dsRegStartMask": dsRegStartMask,
       "dsRegStartValue": dsRegStartValue,
       "dsRegStartCriteria": dsRegStartCriteria,
       "dsRegStartOffset": dsRegStartOffset,
       "dsRegStopMask": dsRegStopMask,
       "dsRegStopValue": dsRegStopValue,
       "dsRegStopCriteria": dsRegStopCriteria,
       "dsRegStopOffset": dsRegStopOffset,
       "dsRegStatus": dsRegStatus,
       "dsRegDataLength": dsRegDataLength,
       "dsRegDataOffset": dsRegDataOffset,
       "dsRegOutputDir": dsRegOutputDir,
       "dsRegOutputFormat": dsRegOutputFormat}
)
