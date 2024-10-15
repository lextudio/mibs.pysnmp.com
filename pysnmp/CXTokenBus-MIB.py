# SNMP MIB module (CXTokenBus-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXTokenBus-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:55 2024
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

(Alias,
 SapIndex,
 cxTokenBus) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxTokenBus")

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

_TbSapTable_Object = MibTable
tbSapTable = _TbSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1)
)
if mibBuilder.loadTexts:
    tbSapTable.setStatus("mandatory")
_TbSapEntry_Object = MibTableRow
tbSapEntry = _TbSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1)
)
tbSapEntry.setIndexNames(
    (0, "CXTokenBus-MIB", "tbSapNumber"),
)
if mibBuilder.loadTexts:
    tbSapEntry.setStatus("mandatory")
_TbSapNumber_Type = SapIndex
_TbSapNumber_Object = MibTableColumn
tbSapNumber = _TbSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 1),
    _TbSapNumber_Type()
)
tbSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbSapNumber.setStatus("mandatory")


class _TbSapRowStatus_Type(Integer32):
    """Custom type tbSapRowStatus based on Integer32"""
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


_TbSapRowStatus_Type.__name__ = "Integer32"
_TbSapRowStatus_Object = MibTableColumn
tbSapRowStatus = _TbSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 2),
    _TbSapRowStatus_Type()
)
tbSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbSapRowStatus.setStatus("mandatory")
_TbSapAlias_Type = Alias
_TbSapAlias_Object = MibTableColumn
tbSapAlias = _TbSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 3),
    _TbSapAlias_Type()
)
tbSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbSapAlias.setStatus("mandatory")


class _TbSapCompanionAlias_Type(Alias):
    """Custom type tbSapCompanionAlias based on Alias"""
    defaultHexValue = ""


_TbSapCompanionAlias_Object = MibTableColumn
tbSapCompanionAlias = _TbSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 4),
    _TbSapCompanionAlias_Type()
)
tbSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbSapCompanionAlias.setStatus("mandatory")


class _TbSapType_Type(Integer32):
    """Custom type tbSapType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("upper", 2)
    )


_TbSapType_Type.__name__ = "Integer32"
_TbSapType_Object = MibTableColumn
tbSapType = _TbSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 5),
    _TbSapType_Type()
)
tbSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbSapType.setStatus("mandatory")


class _TbSapStatGathering_Type(Integer32):
    """Custom type tbSapStatGathering based on Integer32"""
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


_TbSapStatGathering_Type.__name__ = "Integer32"
_TbSapStatGathering_Object = MibTableColumn
tbSapStatGathering = _TbSapStatGathering_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 6),
    _TbSapStatGathering_Type()
)
tbSapStatGathering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbSapStatGathering.setStatus("mandatory")
_TbSapStatRxUnitDataFrames_Type = Counter32
_TbSapStatRxUnitDataFrames_Object = MibTableColumn
tbSapStatRxUnitDataFrames = _TbSapStatRxUnitDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 7),
    _TbSapStatRxUnitDataFrames_Type()
)
tbSapStatRxUnitDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbSapStatRxUnitDataFrames.setStatus("mandatory")
_TbSapStatRxUnitDataOctets_Type = Counter32
_TbSapStatRxUnitDataOctets_Object = MibTableColumn
tbSapStatRxUnitDataOctets = _TbSapStatRxUnitDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 8),
    _TbSapStatRxUnitDataOctets_Type()
)
tbSapStatRxUnitDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbSapStatRxUnitDataOctets.setStatus("mandatory")
_TbSapStatRxDataAckFrames_Type = Counter32
_TbSapStatRxDataAckFrames_Object = MibTableColumn
tbSapStatRxDataAckFrames = _TbSapStatRxDataAckFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 9),
    _TbSapStatRxDataAckFrames_Type()
)
tbSapStatRxDataAckFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbSapStatRxDataAckFrames.setStatus("mandatory")
_TbSapStatRxDataAckOctets_Type = Counter32
_TbSapStatRxDataAckOctets_Object = MibTableColumn
tbSapStatRxDataAckOctets = _TbSapStatRxDataAckOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 10),
    _TbSapStatRxDataAckOctets_Type()
)
tbSapStatRxDataAckOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbSapStatRxDataAckOctets.setStatus("mandatory")
_TbSapStatTxUnitDataFrames_Type = Counter32
_TbSapStatTxUnitDataFrames_Object = MibTableColumn
tbSapStatTxUnitDataFrames = _TbSapStatTxUnitDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 11),
    _TbSapStatTxUnitDataFrames_Type()
)
tbSapStatTxUnitDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbSapStatTxUnitDataFrames.setStatus("mandatory")
_TbSapStatTxUnitDataOctets_Type = Counter32
_TbSapStatTxUnitDataOctets_Object = MibTableColumn
tbSapStatTxUnitDataOctets = _TbSapStatTxUnitDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 12),
    _TbSapStatTxUnitDataOctets_Type()
)
tbSapStatTxUnitDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbSapStatTxUnitDataOctets.setStatus("mandatory")
_TbSapStatTxDataAckFrames_Type = Counter32
_TbSapStatTxDataAckFrames_Object = MibTableColumn
tbSapStatTxDataAckFrames = _TbSapStatTxDataAckFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 13),
    _TbSapStatTxDataAckFrames_Type()
)
tbSapStatTxDataAckFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbSapStatTxDataAckFrames.setStatus("mandatory")
_TbSapStatTxDataAckOctets_Type = Counter32
_TbSapStatTxDataAckOctets_Object = MibTableColumn
tbSapStatTxDataAckOctets = _TbSapStatTxDataAckOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 14),
    _TbSapStatTxDataAckOctets_Type()
)
tbSapStatTxDataAckOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbSapStatTxDataAckOctets.setStatus("mandatory")
_TbDevice_ObjectIdentity = ObjectIdentity
tbDevice = _TbDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2)
)


class _TbDevPollingInterval_Type(Integer32):
    """Custom type tbDevPollingInterval based on Integer32"""
    defaultValue = 10


_TbDevPollingInterval_Object = MibScalar
tbDevPollingInterval = _TbDevPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 1),
    _TbDevPollingInterval_Type()
)
tbDevPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbDevPollingInterval.setStatus("mandatory")


class _TbRxFrameDescriptors_Type(Integer32):
    """Custom type tbRxFrameDescriptors based on Integer32"""
    defaultValue = 32


_TbRxFrameDescriptors_Object = MibScalar
tbRxFrameDescriptors = _TbRxFrameDescriptors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 2),
    _TbRxFrameDescriptors_Type()
)
tbRxFrameDescriptors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbRxFrameDescriptors.setStatus("mandatory")


class _TbRxBufferDescriptors_Type(Integer32):
    """Custom type tbRxBufferDescriptors based on Integer32"""
    defaultValue = 320


_TbRxBufferDescriptors_Object = MibScalar
tbRxBufferDescriptors = _TbRxBufferDescriptors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 3),
    _TbRxBufferDescriptors_Type()
)
tbRxBufferDescriptors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbRxBufferDescriptors.setStatus("mandatory")


class _TbTxFrameDescriptors_Type(Integer32):
    """Custom type tbTxFrameDescriptors based on Integer32"""
    defaultValue = 16


_TbTxFrameDescriptors_Object = MibScalar
tbTxFrameDescriptors = _TbTxFrameDescriptors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 4),
    _TbTxFrameDescriptors_Type()
)
tbTxFrameDescriptors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbTxFrameDescriptors.setStatus("mandatory")


class _TbTxBufferDescriptors_Type(Integer32):
    """Custom type tbTxBufferDescriptors based on Integer32"""
    defaultValue = 160


_TbTxBufferDescriptors_Object = MibScalar
tbTxBufferDescriptors = _TbTxBufferDescriptors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 5),
    _TbTxBufferDescriptors_Type()
)
tbTxBufferDescriptors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbTxBufferDescriptors.setStatus("mandatory")
_TbMaxFrameSizeClass6_Type = Integer32
_TbMaxFrameSizeClass6_Object = MibScalar
tbMaxFrameSizeClass6 = _TbMaxFrameSizeClass6_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 6),
    _TbMaxFrameSizeClass6_Type()
)
tbMaxFrameSizeClass6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbMaxFrameSizeClass6.setStatus("mandatory")
_TbMaxFrameSizeClass4_Type = Integer32
_TbMaxFrameSizeClass4_Object = MibScalar
tbMaxFrameSizeClass4 = _TbMaxFrameSizeClass4_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 7),
    _TbMaxFrameSizeClass4_Type()
)
tbMaxFrameSizeClass4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbMaxFrameSizeClass4.setStatus("mandatory")
_TbMaxFrameSizeClass2_Type = Integer32
_TbMaxFrameSizeClass2_Object = MibScalar
tbMaxFrameSizeClass2 = _TbMaxFrameSizeClass2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 8),
    _TbMaxFrameSizeClass2_Type()
)
tbMaxFrameSizeClass2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbMaxFrameSizeClass2.setStatus("mandatory")
_TbMaxFrameSizeClass0_Type = Integer32
_TbMaxFrameSizeClass0_Object = MibScalar
tbMaxFrameSizeClass0 = _TbMaxFrameSizeClass0_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 9),
    _TbMaxFrameSizeClass0_Type()
)
tbMaxFrameSizeClass0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbMaxFrameSizeClass0.setStatus("mandatory")


class _TbHiPriorityTokenHoldTime_Type(Integer32):
    """Custom type tbHiPriorityTokenHoldTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TbHiPriorityTokenHoldTime_Type.__name__ = "Integer32"
_TbHiPriorityTokenHoldTime_Object = MibScalar
tbHiPriorityTokenHoldTime = _TbHiPriorityTokenHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 10),
    _TbHiPriorityTokenHoldTime_Type()
)
tbHiPriorityTokenHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbHiPriorityTokenHoldTime.setStatus("mandatory")


class _TbTargetRotationTimeClass4_Type(Integer32):
    """Custom type tbTargetRotationTimeClass4 based on Integer32"""
    defaultValue = 480

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_TbTargetRotationTimeClass4_Type.__name__ = "Integer32"
_TbTargetRotationTimeClass4_Object = MibScalar
tbTargetRotationTimeClass4 = _TbTargetRotationTimeClass4_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 11),
    _TbTargetRotationTimeClass4_Type()
)
tbTargetRotationTimeClass4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbTargetRotationTimeClass4.setStatus("mandatory")


class _TbTargetRotationTimeClass2_Type(Integer32):
    """Custom type tbTargetRotationTimeClass2 based on Integer32"""
    defaultValue = 384

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_TbTargetRotationTimeClass2_Type.__name__ = "Integer32"
_TbTargetRotationTimeClass2_Object = MibScalar
tbTargetRotationTimeClass2 = _TbTargetRotationTimeClass2_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 12),
    _TbTargetRotationTimeClass2_Type()
)
tbTargetRotationTimeClass2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbTargetRotationTimeClass2.setStatus("mandatory")


class _TbTargetRotationTimeClass0_Type(Integer32):
    """Custom type tbTargetRotationTimeClass0 based on Integer32"""
    defaultValue = 288

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_TbTargetRotationTimeClass0_Type.__name__ = "Integer32"
_TbTargetRotationTimeClass0_Object = MibScalar
tbTargetRotationTimeClass0 = _TbTargetRotationTimeClass0_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 13),
    _TbTargetRotationTimeClass0_Type()
)
tbTargetRotationTimeClass0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbTargetRotationTimeClass0.setStatus("mandatory")


class _TbTargetRotationForMaintenance_Type(Integer32):
    """Custom type tbTargetRotationForMaintenance based on Integer32"""
    defaultValue = 288

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_TbTargetRotationForMaintenance_Type.__name__ = "Integer32"
_TbTargetRotationForMaintenance_Object = MibScalar
tbTargetRotationForMaintenance = _TbTargetRotationForMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 14),
    _TbTargetRotationForMaintenance_Type()
)
tbTargetRotationForMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbTargetRotationForMaintenance.setStatus("mandatory")


class _TbMaxInterSolicitCount_Type(Integer32):
    """Custom type tbMaxInterSolicitCount based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_TbMaxInterSolicitCount_Type.__name__ = "Integer32"
_TbMaxInterSolicitCount_Object = MibScalar
tbMaxInterSolicitCount = _TbMaxInterSolicitCount_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 15),
    _TbMaxInterSolicitCount_Type()
)
tbMaxInterSolicitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbMaxInterSolicitCount.setStatus("mandatory")


class _TbNonRwrMaxRetryLimit_Type(Integer32):
    """Custom type tbNonRwrMaxRetryLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TbNonRwrMaxRetryLimit_Type.__name__ = "Integer32"
_TbNonRwrMaxRetryLimit_Object = MibScalar
tbNonRwrMaxRetryLimit = _TbNonRwrMaxRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 16),
    _TbNonRwrMaxRetryLimit_Type()
)
tbNonRwrMaxRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbNonRwrMaxRetryLimit.setStatus("mandatory")


class _TbRwrMaxRetryLimit_Type(Integer32):
    """Custom type tbRwrMaxRetryLimit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TbRwrMaxRetryLimit_Type.__name__ = "Integer32"
_TbRwrMaxRetryLimit_Object = MibScalar
tbRwrMaxRetryLimit = _TbRwrMaxRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 17),
    _TbRwrMaxRetryLimit_Type()
)
tbRwrMaxRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbRwrMaxRetryLimit.setStatus("mandatory")


class _TbSlotTime_Type(Integer32):
    """Custom type tbSlotTime based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_TbSlotTime_Type.__name__ = "Integer32"
_TbSlotTime_Object = MibScalar
tbSlotTime = _TbSlotTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 18),
    _TbSlotTime_Type()
)
tbSlotTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tbSlotTime.setStatus("mandatory")
_TbTxNonRwrFailures_Type = Counter32
_TbTxNonRwrFailures_Object = MibScalar
tbTxNonRwrFailures = _TbTxNonRwrFailures_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 19),
    _TbTxNonRwrFailures_Type()
)
tbTxNonRwrFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbTxNonRwrFailures.setStatus("mandatory")
_TbTxRwrFailures_Type = Counter32
_TbTxRwrFailures_Object = MibScalar
tbTxRwrFailures = _TbTxRwrFailures_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 20),
    _TbTxRwrFailures_Type()
)
tbTxRwrFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbTxRwrFailures.setStatus("mandatory")
_TbUnexpectedFrame6s_Type = Counter32
_TbUnexpectedFrame6s_Object = MibScalar
tbUnexpectedFrame6s = _TbUnexpectedFrame6s_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 21),
    _TbUnexpectedFrame6s_Type()
)
tbUnexpectedFrame6s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbUnexpectedFrame6s.setStatus("mandatory")
_TbUnexpectedFrame10s_Type = Counter32
_TbUnexpectedFrame10s_Object = MibScalar
tbUnexpectedFrame10s = _TbUnexpectedFrame10s_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 22),
    _TbUnexpectedFrame10s_Type()
)
tbUnexpectedFrame10s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbUnexpectedFrame10s.setStatus("mandatory")
_TbNbUnderruns_Type = Counter32
_TbNbUnderruns_Object = MibScalar
tbNbUnderruns = _TbNbUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 23),
    _TbNbUnderruns_Type()
)
tbNbUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbNbUnderruns.setStatus("mandatory")
_TbRxRetryRwrFrames_Type = Counter32
_TbRxRetryRwrFrames_Object = MibScalar
tbRxRetryRwrFrames = _TbRxRetryRwrFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 24),
    _TbRxRetryRwrFrames_Type()
)
tbRxRetryRwrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbRxRetryRwrFrames.setStatus("mandatory")
_TbRxNullLsduRwrFrames_Type = Counter32
_TbRxNullLsduRwrFrames_Object = MibScalar
tbRxNullLsduRwrFrames = _TbRxNullLsduRwrFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 25),
    _TbRxNullLsduRwrFrames_Type()
)
tbRxNullLsduRwrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbRxNullLsduRwrFrames.setStatus("mandatory")
_TbNbPassedTokens_Type = Counter32
_TbNbPassedTokens_Object = MibScalar
tbNbPassedTokens = _TbNbPassedTokens_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 26),
    _TbNbPassedTokens_Type()
)
tbNbPassedTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbNbPassedTokens.setStatus("mandatory")
_TbNbHeardTokens_Type = Counter32
_TbNbHeardTokens_Object = MibScalar
tbNbHeardTokens = _TbNbHeardTokens_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 27),
    _TbNbHeardTokens_Type()
)
tbNbHeardTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbNbHeardTokens.setStatus("mandatory")
_TbNbNoSuccessor8Passes_Type = Counter32
_TbNbNoSuccessor8Passes_Object = MibScalar
tbNbNoSuccessor8Passes = _TbNbNoSuccessor8Passes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 28),
    _TbNbNoSuccessor8Passes_Type()
)
tbNbNoSuccessor8Passes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbNbNoSuccessor8Passes.setStatus("mandatory")
_TbNbWhoFollowsFrames_Type = Counter32
_TbNbWhoFollowsFrames_Object = MibScalar
tbNbWhoFollowsFrames = _TbNbWhoFollowsFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 29),
    _TbNbWhoFollowsFrames_Type()
)
tbNbWhoFollowsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbNbWhoFollowsFrames.setStatus("mandatory")
_TbNbTokenPassFailures_Type = Counter32
_TbNbTokenPassFailures_Object = MibScalar
tbNbTokenPassFailures = _TbNbTokenPassFailures_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 30),
    _TbNbTokenPassFailures_Type()
)
tbNbTokenPassFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbNbTokenPassFailures.setStatus("mandatory")
_TbRxPeriodNonSilences_Type = Counter32
_TbRxPeriodNonSilences_Object = MibScalar
tbRxPeriodNonSilences = _TbRxPeriodNonSilences_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 31),
    _TbRxPeriodNonSilences_Type()
)
tbRxPeriodNonSilences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbRxPeriodNonSilences.setStatus("mandatory")
_TbRxBadCrcFrames_Type = Counter32
_TbRxBadCrcFrames_Object = MibScalar
tbRxBadCrcFrames = _TbRxBadCrcFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 32),
    _TbRxBadCrcFrames_Type()
)
tbRxBadCrcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbRxBadCrcFrames.setStatus("mandatory")
_TbRxEBitSetFrames_Type = Counter32
_TbRxEBitSetFrames_Object = MibScalar
tbRxEBitSetFrames = _TbRxEBitSetFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 33),
    _TbRxEBitSetFrames_Type()
)
tbRxEBitSetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbRxEBitSetFrames.setStatus("mandatory")
_TbRxFrameFragments_Type = Counter32
_TbRxFrameFragments_Object = MibScalar
tbRxFrameFragments = _TbRxFrameFragments_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 34),
    _TbRxFrameFragments_Type()
)
tbRxFrameFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbRxFrameFragments.setStatus("mandatory")
_TbRxFrameTooLongs_Type = Counter32
_TbRxFrameTooLongs_Object = MibScalar
tbRxFrameTooLongs = _TbRxFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 35),
    _TbRxFrameTooLongs_Type()
)
tbRxFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbRxFrameTooLongs.setStatus("mandatory")
_TbNbNoFdBdErrors_Type = Counter32
_TbNbNoFdBdErrors_Object = MibScalar
tbNbNoFdBdErrors = _TbNbNoFdBdErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 36),
    _TbNbNoFdBdErrors_Type()
)
tbNbNoFdBdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbNbNoFdBdErrors.setStatus("mandatory")
_TbNbOverruns_Type = Counter32
_TbNbOverruns_Object = MibScalar
tbNbOverruns = _TbNbOverruns_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 37),
    _TbNbOverruns_Type()
)
tbNbOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tbNbOverruns.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXTokenBus-MIB",
    **{"tbSapTable": tbSapTable,
       "tbSapEntry": tbSapEntry,
       "tbSapNumber": tbSapNumber,
       "tbSapRowStatus": tbSapRowStatus,
       "tbSapAlias": tbSapAlias,
       "tbSapCompanionAlias": tbSapCompanionAlias,
       "tbSapType": tbSapType,
       "tbSapStatGathering": tbSapStatGathering,
       "tbSapStatRxUnitDataFrames": tbSapStatRxUnitDataFrames,
       "tbSapStatRxUnitDataOctets": tbSapStatRxUnitDataOctets,
       "tbSapStatRxDataAckFrames": tbSapStatRxDataAckFrames,
       "tbSapStatRxDataAckOctets": tbSapStatRxDataAckOctets,
       "tbSapStatTxUnitDataFrames": tbSapStatTxUnitDataFrames,
       "tbSapStatTxUnitDataOctets": tbSapStatTxUnitDataOctets,
       "tbSapStatTxDataAckFrames": tbSapStatTxDataAckFrames,
       "tbSapStatTxDataAckOctets": tbSapStatTxDataAckOctets,
       "tbDevice": tbDevice,
       "tbDevPollingInterval": tbDevPollingInterval,
       "tbRxFrameDescriptors": tbRxFrameDescriptors,
       "tbRxBufferDescriptors": tbRxBufferDescriptors,
       "tbTxFrameDescriptors": tbTxFrameDescriptors,
       "tbTxBufferDescriptors": tbTxBufferDescriptors,
       "tbMaxFrameSizeClass6": tbMaxFrameSizeClass6,
       "tbMaxFrameSizeClass4": tbMaxFrameSizeClass4,
       "tbMaxFrameSizeClass2": tbMaxFrameSizeClass2,
       "tbMaxFrameSizeClass0": tbMaxFrameSizeClass0,
       "tbHiPriorityTokenHoldTime": tbHiPriorityTokenHoldTime,
       "tbTargetRotationTimeClass4": tbTargetRotationTimeClass4,
       "tbTargetRotationTimeClass2": tbTargetRotationTimeClass2,
       "tbTargetRotationTimeClass0": tbTargetRotationTimeClass0,
       "tbTargetRotationForMaintenance": tbTargetRotationForMaintenance,
       "tbMaxInterSolicitCount": tbMaxInterSolicitCount,
       "tbNonRwrMaxRetryLimit": tbNonRwrMaxRetryLimit,
       "tbRwrMaxRetryLimit": tbRwrMaxRetryLimit,
       "tbSlotTime": tbSlotTime,
       "tbTxNonRwrFailures": tbTxNonRwrFailures,
       "tbTxRwrFailures": tbTxRwrFailures,
       "tbUnexpectedFrame6s": tbUnexpectedFrame6s,
       "tbUnexpectedFrame10s": tbUnexpectedFrame10s,
       "tbNbUnderruns": tbNbUnderruns,
       "tbRxRetryRwrFrames": tbRxRetryRwrFrames,
       "tbRxNullLsduRwrFrames": tbRxNullLsduRwrFrames,
       "tbNbPassedTokens": tbNbPassedTokens,
       "tbNbHeardTokens": tbNbHeardTokens,
       "tbNbNoSuccessor8Passes": tbNbNoSuccessor8Passes,
       "tbNbWhoFollowsFrames": tbNbWhoFollowsFrames,
       "tbNbTokenPassFailures": tbNbTokenPassFailures,
       "tbRxPeriodNonSilences": tbRxPeriodNonSilences,
       "tbRxBadCrcFrames": tbRxBadCrcFrames,
       "tbRxEBitSetFrames": tbRxEBitSetFrames,
       "tbRxFrameFragments": tbRxFrameFragments,
       "tbRxFrameTooLongs": tbRxFrameTooLongs,
       "tbNbNoFdBdErrors": tbNbNoFdBdErrors,
       "tbNbOverruns": tbNbOverruns}
)
