# SNMP MIB module (Wellfleet-ATM-LE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-ATM-LE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:49 2024
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

(wfAtmLeGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfAtmLeGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfAtmLecConfigTable_Object = MibTable
wfAtmLecConfigTable = _WfAtmLecConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1)
)
if mibBuilder.loadTexts:
    wfAtmLecConfigTable.setStatus("mandatory")
_WfAtmLecConfigEntry_Object = MibTableRow
wfAtmLecConfigEntry = _WfAtmLecConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1)
)
wfAtmLecConfigEntry.setIndexNames(
    (0, "Wellfleet-ATM-LE-MIB", "wflecConfigCct"),
)
if mibBuilder.loadTexts:
    wfAtmLecConfigEntry.setStatus("mandatory")


class _WflecConfDelete_Type(Integer32):
    """Custom type wflecConfDelete based on Integer32"""
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


_WflecConfDelete_Type.__name__ = "Integer32"
_WflecConfDelete_Object = MibTableColumn
wflecConfDelete = _WflecConfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 1),
    _WflecConfDelete_Type()
)
wflecConfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecConfDelete.setStatus("mandatory")


class _WflecRowStatus_Type(Integer32):
    """Custom type wflecRowStatus based on Integer32"""
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


_WflecRowStatus_Type.__name__ = "Integer32"
_WflecRowStatus_Object = MibTableColumn
wflecRowStatus = _WflecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 2),
    _WflecRowStatus_Type()
)
wflecRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecRowStatus.setStatus("mandatory")
_WflecConfigCct_Type = Integer32
_WflecConfigCct_Object = MibTableColumn
wflecConfigCct = _WflecConfigCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 3),
    _WflecConfigCct_Type()
)
wflecConfigCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecConfigCct.setStatus("mandatory")
_WflecOwner_Type = DisplayString
_WflecOwner_Object = MibTableColumn
wflecOwner = _WflecOwner_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 4),
    _WflecOwner_Type()
)
wflecOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecOwner.setStatus("mandatory")


class _WflecConfigMode_Type(Integer32):
    """Custom type wflecConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autocfg", 1),
          ("mancfg", 2))
    )


_WflecConfigMode_Type.__name__ = "Integer32"
_WflecConfigMode_Object = MibTableColumn
wflecConfigMode = _WflecConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 5),
    _WflecConfigMode_Type()
)
wflecConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecConfigMode.setStatus("mandatory")


class _WflecConfigLanType_Type(Integer32):
    """Custom type wflecConfigLanType based on Integer32"""
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
        *(("ieee8023", 2),
          ("ieee8025", 3),
          ("unspecified", 1))
    )


_WflecConfigLanType_Type.__name__ = "Integer32"
_WflecConfigLanType_Object = MibTableColumn
wflecConfigLanType = _WflecConfigLanType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 6),
    _WflecConfigLanType_Type()
)
wflecConfigLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecConfigLanType.setStatus("mandatory")


class _WflecConfigMaxDataFrameSize_Type(Integer32):
    """Custom type wflecConfigMaxDataFrameSize based on Integer32"""
    defaultValue = 1

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
        *(("size1516", 2),
          ("size18190", 5),
          ("size4544", 3),
          ("size9234", 4),
          ("unspec", 1))
    )


_WflecConfigMaxDataFrameSize_Type.__name__ = "Integer32"
_WflecConfigMaxDataFrameSize_Object = MibTableColumn
wflecConfigMaxDataFrameSize = _WflecConfigMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 7),
    _WflecConfigMaxDataFrameSize_Type()
)
wflecConfigMaxDataFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecConfigMaxDataFrameSize.setStatus("mandatory")
_WflecConfigLanName_Type = DisplayString
_WflecConfigLanName_Object = MibTableColumn
wflecConfigLanName = _WflecConfigLanName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 8),
    _WflecConfigLanName_Type()
)
wflecConfigLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecConfigLanName.setStatus("mandatory")
_WflecConfigLesAtmAddress_Type = OctetString
_WflecConfigLesAtmAddress_Object = MibTableColumn
wflecConfigLesAtmAddress = _WflecConfigLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 9),
    _WflecConfigLesAtmAddress_Type()
)
wflecConfigLesAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecConfigLesAtmAddress.setStatus("mandatory")


class _WflecControlTimeout_Type(Integer32):
    """Custom type wflecControlTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_WflecControlTimeout_Type.__name__ = "Integer32"
_WflecControlTimeout_Object = MibTableColumn
wflecControlTimeout = _WflecControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 10),
    _WflecControlTimeout_Type()
)
wflecControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecControlTimeout.setStatus("mandatory")


class _WflecMaxUnknownFrameCount_Type(Integer32):
    """Custom type wflecMaxUnknownFrameCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WflecMaxUnknownFrameCount_Type.__name__ = "Integer32"
_WflecMaxUnknownFrameCount_Object = MibTableColumn
wflecMaxUnknownFrameCount = _WflecMaxUnknownFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 11),
    _WflecMaxUnknownFrameCount_Type()
)
wflecMaxUnknownFrameCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecMaxUnknownFrameCount.setStatus("mandatory")


class _WflecMaxUnknownFrameTime_Type(Integer32):
    """Custom type wflecMaxUnknownFrameTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WflecMaxUnknownFrameTime_Type.__name__ = "Integer32"
_WflecMaxUnknownFrameTime_Object = MibTableColumn
wflecMaxUnknownFrameTime = _WflecMaxUnknownFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 12),
    _WflecMaxUnknownFrameTime_Type()
)
wflecMaxUnknownFrameTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecMaxUnknownFrameTime.setStatus("mandatory")


class _WflecVccTimeoutPeriod_Type(Integer32):
    """Custom type wflecVccTimeoutPeriod based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1200
        )
    )
    namedValues = NamedValues(
        ("vcctmodef", 1200)
    )


_WflecVccTimeoutPeriod_Type.__name__ = "Integer32"
_WflecVccTimeoutPeriod_Object = MibTableColumn
wflecVccTimeoutPeriod = _WflecVccTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 13),
    _WflecVccTimeoutPeriod_Type()
)
wflecVccTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecVccTimeoutPeriod.setStatus("mandatory")


class _WflecMaxRetryCount_Type(Integer32):
    """Custom type wflecMaxRetryCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WflecMaxRetryCount_Type.__name__ = "Integer32"
_WflecMaxRetryCount_Object = MibTableColumn
wflecMaxRetryCount = _WflecMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 14),
    _WflecMaxRetryCount_Type()
)
wflecMaxRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecMaxRetryCount.setStatus("mandatory")


class _WflecAgingTime_Type(Integer32):
    """Custom type wflecAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_WflecAgingTime_Type.__name__ = "Integer32"
_WflecAgingTime_Object = MibTableColumn
wflecAgingTime = _WflecAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 15),
    _WflecAgingTime_Type()
)
wflecAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecAgingTime.setStatus("mandatory")


class _WflecForwardDelayTime_Type(Integer32):
    """Custom type wflecForwardDelayTime based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_WflecForwardDelayTime_Type.__name__ = "Integer32"
_WflecForwardDelayTime_Object = MibTableColumn
wflecForwardDelayTime = _WflecForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 16),
    _WflecForwardDelayTime_Type()
)
wflecForwardDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecForwardDelayTime.setStatus("mandatory")


class _WflecExpectedArpResponseTime_Type(Integer32):
    """Custom type wflecExpectedArpResponseTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WflecExpectedArpResponseTime_Type.__name__ = "Integer32"
_WflecExpectedArpResponseTime_Object = MibTableColumn
wflecExpectedArpResponseTime = _WflecExpectedArpResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 17),
    _WflecExpectedArpResponseTime_Type()
)
wflecExpectedArpResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecExpectedArpResponseTime.setStatus("mandatory")


class _WflecFlushTimeOut_Type(Integer32):
    """Custom type wflecFlushTimeOut based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WflecFlushTimeOut_Type.__name__ = "Integer32"
_WflecFlushTimeOut_Object = MibTableColumn
wflecFlushTimeOut = _WflecFlushTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 18),
    _WflecFlushTimeOut_Type()
)
wflecFlushTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecFlushTimeOut.setStatus("mandatory")


class _WflecPathSwitchingDelay_Type(Integer32):
    """Custom type wflecPathSwitchingDelay based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WflecPathSwitchingDelay_Type.__name__ = "Integer32"
_WflecPathSwitchingDelay_Object = MibTableColumn
wflecPathSwitchingDelay = _WflecPathSwitchingDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 19),
    _WflecPathSwitchingDelay_Type()
)
wflecPathSwitchingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecPathSwitchingDelay.setStatus("mandatory")


class _WflecLocalSegmentID_Type(Integer32):
    """Custom type wflecLocalSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WflecLocalSegmentID_Type.__name__ = "Integer32"
_WflecLocalSegmentID_Object = MibTableColumn
wflecLocalSegmentID = _WflecLocalSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 20),
    _WflecLocalSegmentID_Type()
)
wflecLocalSegmentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecLocalSegmentID.setStatus("mandatory")


class _WflecMulticastSendType_Type(Integer32):
    """Custom type wflecMulticastSendType based on Integer32"""
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
        *(("abr", 1),
          ("cbr", 3),
          ("vbr", 2))
    )


_WflecMulticastSendType_Type.__name__ = "Integer32"
_WflecMulticastSendType_Object = MibTableColumn
wflecMulticastSendType = _WflecMulticastSendType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 21),
    _WflecMulticastSendType_Type()
)
wflecMulticastSendType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecMulticastSendType.setStatus("mandatory")
_WflecMulticastSendAvgRate_Type = Integer32
_WflecMulticastSendAvgRate_Object = MibTableColumn
wflecMulticastSendAvgRate = _WflecMulticastSendAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 22),
    _WflecMulticastSendAvgRate_Type()
)
wflecMulticastSendAvgRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecMulticastSendAvgRate.setStatus("mandatory")
_WflecMulticastSendPeakRate_Type = Integer32
_WflecMulticastSendPeakRate_Object = MibTableColumn
wflecMulticastSendPeakRate = _WflecMulticastSendPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 23),
    _WflecMulticastSendPeakRate_Type()
)
wflecMulticastSendPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecMulticastSendPeakRate.setStatus("mandatory")


class _WflecConnectionCompleteTimer_Type(Integer32):
    """Custom type wflecConnectionCompleteTimer based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WflecConnectionCompleteTimer_Type.__name__ = "Integer32"
_WflecConnectionCompleteTimer_Object = MibTableColumn
wflecConnectionCompleteTimer = _WflecConnectionCompleteTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 24),
    _WflecConnectionCompleteTimer_Type()
)
wflecConnectionCompleteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecConnectionCompleteTimer.setStatus("mandatory")


class _WflecFlushEnable_Type(Integer32):
    """Custom type wflecFlushEnable based on Integer32"""
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


_WflecFlushEnable_Type.__name__ = "Integer32"
_WflecFlushEnable_Object = MibTableColumn
wflecFlushEnable = _WflecFlushEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 25),
    _WflecFlushEnable_Type()
)
wflecFlushEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecFlushEnable.setStatus("mandatory")
_WflecConfigRetry_Type = Integer32
_WflecConfigRetry_Object = MibTableColumn
wflecConfigRetry = _WflecConfigRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 26),
    _WflecConfigRetry_Type()
)
wflecConfigRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecConfigRetry.setStatus("mandatory")


class _WflecMulticastFwdTimeout_Type(Integer32):
    """Custom type wflecMulticastFwdTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("mcsfwdtmodef", 5)
    )


_WflecMulticastFwdTimeout_Type.__name__ = "Integer32"
_WflecMulticastFwdTimeout_Object = MibTableColumn
wflecMulticastFwdTimeout = _WflecMulticastFwdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 27),
    _WflecMulticastFwdTimeout_Type()
)
wflecMulticastFwdTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecMulticastFwdTimeout.setStatus("mandatory")


class _WflecMulticastFwdRetry_Type(Integer32):
    """Custom type wflecMulticastFwdRetry based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("mcsfwdrtrydef", 10)
    )


_WflecMulticastFwdRetry_Type.__name__ = "Integer32"
_WflecMulticastFwdRetry_Object = MibTableColumn
wflecMulticastFwdRetry = _WflecMulticastFwdRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 28),
    _WflecMulticastFwdRetry_Type()
)
wflecMulticastFwdRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecMulticastFwdRetry.setStatus("mandatory")


class _WflecDebugLevel_Type(Integer32):
    """Custom type wflecDebugLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WflecDebugLevel_Type.__name__ = "Integer32"
_WflecDebugLevel_Object = MibTableColumn
wflecDebugLevel = _WflecDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 29),
    _WflecDebugLevel_Type()
)
wflecDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecDebugLevel.setStatus("mandatory")
_WflecConfigLECSAtmAddress_Type = OctetString
_WflecConfigLECSAtmAddress_Object = MibTableColumn
wflecConfigLECSAtmAddress = _WflecConfigLECSAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 30),
    _WflecConfigLECSAtmAddress_Type()
)
wflecConfigLECSAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecConfigLECSAtmAddress.setStatus("mandatory")


class _WflecConfigV2Capable_Type(Integer32):
    """Custom type wflecConfigV2Capable based on Integer32"""
    defaultValue = 2

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


_WflecConfigV2Capable_Type.__name__ = "Integer32"
_WflecConfigV2Capable_Object = MibTableColumn
wflecConfigV2Capable = _WflecConfigV2Capable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 1, 1, 31),
    _WflecConfigV2Capable_Type()
)
wflecConfigV2Capable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecConfigV2Capable.setStatus("mandatory")
_WfAtmLecStatusTable_Object = MibTable
wfAtmLecStatusTable = _WfAtmLecStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2)
)
if mibBuilder.loadTexts:
    wfAtmLecStatusTable.setStatus("mandatory")
_WfAtmLecStatusEntry_Object = MibTableRow
wfAtmLecStatusEntry = _WfAtmLecStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1)
)
wfAtmLecStatusEntry.setIndexNames(
    (0, "Wellfleet-ATM-LE-MIB", "wflecStatusCct"),
)
if mibBuilder.loadTexts:
    wfAtmLecStatusEntry.setStatus("mandatory")
_WflecStatusCct_Type = Integer32
_WflecStatusCct_Object = MibTableColumn
wflecStatusCct = _WflecStatusCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 1),
    _WflecStatusCct_Type()
)
wflecStatusCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecStatusCct.setStatus("mandatory")
_WflecPrimaryAtmAddress_Type = OctetString
_WflecPrimaryAtmAddress_Object = MibTableColumn
wflecPrimaryAtmAddress = _WflecPrimaryAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 2),
    _WflecPrimaryAtmAddress_Type()
)
wflecPrimaryAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecPrimaryAtmAddress.setStatus("mandatory")
_WflecID_Type = Integer32
_WflecID_Object = MibTableColumn
wflecID = _WflecID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 3),
    _WflecID_Type()
)
wflecID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecID.setStatus("mandatory")


class _WflecInterfaceState_Type(Integer32):
    """Custom type wflecInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("busconnect", 6),
          ("configure", 3),
          ("initial", 1),
          ("join", 4),
          ("lecsconnect", 2),
          ("operational", 7),
          ("reg", 5))
    )


_WflecInterfaceState_Type.__name__ = "Integer32"
_WflecInterfaceState_Object = MibTableColumn
wflecInterfaceState = _WflecInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 4),
    _WflecInterfaceState_Type()
)
wflecInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecInterfaceState.setStatus("mandatory")


class _WflecLastFailureRespCode_Type(Integer32):
    """Custom type wflecLastFailureRespCode based on Integer32"""
    defaultValue = 1

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("accdenied", 9),
          ("dupatmadr", 7),
          ("dupdst", 6),
          ("insufinfo", 15),
          ("insufres", 8),
          ("invatmadr", 12),
          ("invdst", 11),
          ("invreq", 5),
          ("invreqid", 10),
          ("lecfgerr", 14),
          ("nocfg", 13),
          ("none", 1),
          ("tmo", 2),
          ("undef", 3),
          ("vrsnotsup", 4))
    )


_WflecLastFailureRespCode_Type.__name__ = "Integer32"
_WflecLastFailureRespCode_Object = MibTableColumn
wflecLastFailureRespCode = _WflecLastFailureRespCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 5),
    _WflecLastFailureRespCode_Type()
)
wflecLastFailureRespCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecLastFailureRespCode.setStatus("mandatory")
_WflecLastFailureState_Type = Integer32
_WflecLastFailureState_Object = MibTableColumn
wflecLastFailureState = _WflecLastFailureState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 6),
    _WflecLastFailureState_Type()
)
wflecLastFailureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecLastFailureState.setStatus("mandatory")


class _WflecProtocol_Type(Integer32):
    """Custom type wflecProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("prot1", 1)
    )


_WflecProtocol_Type.__name__ = "Integer32"
_WflecProtocol_Object = MibTableColumn
wflecProtocol = _WflecProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 7),
    _WflecProtocol_Type()
)
wflecProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecProtocol.setStatus("mandatory")
_WflecVersion_Type = Integer32
_WflecVersion_Object = MibTableColumn
wflecVersion = _WflecVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 8),
    _WflecVersion_Type()
)
wflecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecVersion.setStatus("mandatory")
_WflecTopologyChange_Type = Integer32
_WflecTopologyChange_Object = MibTableColumn
wflecTopologyChange = _WflecTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 9),
    _WflecTopologyChange_Type()
)
wflecTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecTopologyChange.setStatus("mandatory")
_WflecConfigServerAtmAddress_Type = OctetString
_WflecConfigServerAtmAddress_Object = MibTableColumn
wflecConfigServerAtmAddress = _WflecConfigServerAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 10),
    _WflecConfigServerAtmAddress_Type()
)
wflecConfigServerAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecConfigServerAtmAddress.setStatus("mandatory")


class _WflecConfigSource_Type(Integer32):
    """Custom type wflecConfigSource based on Integer32"""
    defaultValue = 4

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
        *(("cfgpvc", 3),
          ("knownadr", 2),
          ("nolecs", 4),
          ("viailmi", 1))
    )


_WflecConfigSource_Type.__name__ = "Integer32"
_WflecConfigSource_Object = MibTableColumn
wflecConfigSource = _WflecConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 11),
    _WflecConfigSource_Type()
)
wflecConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecConfigSource.setStatus("mandatory")


class _WflecActualLanType_Type(Integer32):
    """Custom type wflecActualLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8023", 2),
          ("ieee8025", 3),
          ("unspecified", 1))
    )


_WflecActualLanType_Type.__name__ = "Integer32"
_WflecActualLanType_Object = MibTableColumn
wflecActualLanType = _WflecActualLanType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 12),
    _WflecActualLanType_Type()
)
wflecActualLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecActualLanType.setStatus("mandatory")


class _WflecActualMaxDataFrameSize_Type(Integer32):
    """Custom type wflecActualMaxDataFrameSize based on Integer32"""
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
        *(("size1516", 2),
          ("size18190", 5),
          ("size4544", 3),
          ("size9234", 4),
          ("unspec", 1))
    )


_WflecActualMaxDataFrameSize_Type.__name__ = "Integer32"
_WflecActualMaxDataFrameSize_Object = MibTableColumn
wflecActualMaxDataFrameSize = _WflecActualMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 13),
    _WflecActualMaxDataFrameSize_Type()
)
wflecActualMaxDataFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecActualMaxDataFrameSize.setStatus("mandatory")
_WflecActualLanName_Type = DisplayString
_WflecActualLanName_Object = MibTableColumn
wflecActualLanName = _WflecActualLanName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 14),
    _WflecActualLanName_Type()
)
wflecActualLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecActualLanName.setStatus("mandatory")
_WflecActualLesAtmAddress_Type = OctetString
_WflecActualLesAtmAddress_Object = MibTableColumn
wflecActualLesAtmAddress = _WflecActualLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 15),
    _WflecActualLesAtmAddress_Type()
)
wflecActualLesAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecActualLesAtmAddress.setStatus("mandatory")
_WflecProxyClient_Type = Integer32
_WflecProxyClient_Object = MibTableColumn
wflecProxyClient = _WflecProxyClient_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 2, 1, 16),
    _WflecProxyClient_Type()
)
wflecProxyClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecProxyClient.setStatus("mandatory")
_WfAtmLecOperConfigTable_Object = MibTable
wfAtmLecOperConfigTable = _WfAtmLecOperConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3)
)
if mibBuilder.loadTexts:
    wfAtmLecOperConfigTable.setStatus("mandatory")
_WfAtmLecOperConfigEntry_Object = MibTableRow
wfAtmLecOperConfigEntry = _WfAtmLecOperConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1)
)
wfAtmLecOperConfigEntry.setIndexNames(
    (0, "Wellfleet-ATM-LE-MIB", "wflecOperConfigCct"),
)
if mibBuilder.loadTexts:
    wfAtmLecOperConfigEntry.setStatus("mandatory")
_WflecOperConfigCct_Type = Integer32
_WflecOperConfigCct_Object = MibTableColumn
wflecOperConfigCct = _WflecOperConfigCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 1),
    _WflecOperConfigCct_Type()
)
wflecOperConfigCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigCct.setStatus("mandatory")
_WflecOperConfigControlTimeout_Type = Integer32
_WflecOperConfigControlTimeout_Object = MibTableColumn
wflecOperConfigControlTimeout = _WflecOperConfigControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 2),
    _WflecOperConfigControlTimeout_Type()
)
wflecOperConfigControlTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigControlTimeout.setStatus("mandatory")
_WflecOperConfigMaxUnknownFrameCount_Type = Integer32
_WflecOperConfigMaxUnknownFrameCount_Object = MibTableColumn
wflecOperConfigMaxUnknownFrameCount = _WflecOperConfigMaxUnknownFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 3),
    _WflecOperConfigMaxUnknownFrameCount_Type()
)
wflecOperConfigMaxUnknownFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigMaxUnknownFrameCount.setStatus("mandatory")
_WflecOperConfigMaxUnknownFrameTime_Type = Integer32
_WflecOperConfigMaxUnknownFrameTime_Object = MibTableColumn
wflecOperConfigMaxUnknownFrameTime = _WflecOperConfigMaxUnknownFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 4),
    _WflecOperConfigMaxUnknownFrameTime_Type()
)
wflecOperConfigMaxUnknownFrameTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigMaxUnknownFrameTime.setStatus("mandatory")
_WflecOperConfigVccTimeoutPeriod_Type = Integer32
_WflecOperConfigVccTimeoutPeriod_Object = MibTableColumn
wflecOperConfigVccTimeoutPeriod = _WflecOperConfigVccTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 5),
    _WflecOperConfigVccTimeoutPeriod_Type()
)
wflecOperConfigVccTimeoutPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigVccTimeoutPeriod.setStatus("mandatory")
_WflecOperConfigMaxRetryCount_Type = Integer32
_WflecOperConfigMaxRetryCount_Object = MibTableColumn
wflecOperConfigMaxRetryCount = _WflecOperConfigMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 6),
    _WflecOperConfigMaxRetryCount_Type()
)
wflecOperConfigMaxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigMaxRetryCount.setStatus("mandatory")
_WflecOperConfigAgingTime_Type = Integer32
_WflecOperConfigAgingTime_Object = MibTableColumn
wflecOperConfigAgingTime = _WflecOperConfigAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 7),
    _WflecOperConfigAgingTime_Type()
)
wflecOperConfigAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigAgingTime.setStatus("mandatory")
_WflecOperConfigForwardDelayTime_Type = Integer32
_WflecOperConfigForwardDelayTime_Object = MibTableColumn
wflecOperConfigForwardDelayTime = _WflecOperConfigForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 8),
    _WflecOperConfigForwardDelayTime_Type()
)
wflecOperConfigForwardDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigForwardDelayTime.setStatus("mandatory")
_WflecOperConfigTopologyChange_Type = Integer32
_WflecOperConfigTopologyChange_Object = MibTableColumn
wflecOperConfigTopologyChange = _WflecOperConfigTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 9),
    _WflecOperConfigTopologyChange_Type()
)
wflecOperConfigTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigTopologyChange.setStatus("mandatory")
_WflecOperConfigExpectedArpResponseTime_Type = Integer32
_WflecOperConfigExpectedArpResponseTime_Object = MibTableColumn
wflecOperConfigExpectedArpResponseTime = _WflecOperConfigExpectedArpResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 10),
    _WflecOperConfigExpectedArpResponseTime_Type()
)
wflecOperConfigExpectedArpResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigExpectedArpResponseTime.setStatus("mandatory")
_WflecOperConfigFlushTimeOut_Type = Integer32
_WflecOperConfigFlushTimeOut_Object = MibTableColumn
wflecOperConfigFlushTimeOut = _WflecOperConfigFlushTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 11),
    _WflecOperConfigFlushTimeOut_Type()
)
wflecOperConfigFlushTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigFlushTimeOut.setStatus("mandatory")
_WflecOperConfigPathSwitchingDelay_Type = Integer32
_WflecOperConfigPathSwitchingDelay_Object = MibTableColumn
wflecOperConfigPathSwitchingDelay = _WflecOperConfigPathSwitchingDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 12),
    _WflecOperConfigPathSwitchingDelay_Type()
)
wflecOperConfigPathSwitchingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigPathSwitchingDelay.setStatus("mandatory")
_WflecOperConfigLocalSegmentID_Type = Integer32
_WflecOperConfigLocalSegmentID_Object = MibTableColumn
wflecOperConfigLocalSegmentID = _WflecOperConfigLocalSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 13),
    _WflecOperConfigLocalSegmentID_Type()
)
wflecOperConfigLocalSegmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigLocalSegmentID.setStatus("mandatory")
_WflecOperConfigMulticastSendType_Type = Integer32
_WflecOperConfigMulticastSendType_Object = MibTableColumn
wflecOperConfigMulticastSendType = _WflecOperConfigMulticastSendType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 14),
    _WflecOperConfigMulticastSendType_Type()
)
wflecOperConfigMulticastSendType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigMulticastSendType.setStatus("mandatory")
_WflecOperConfigMulticastSendAvgRate_Type = Integer32
_WflecOperConfigMulticastSendAvgRate_Object = MibTableColumn
wflecOperConfigMulticastSendAvgRate = _WflecOperConfigMulticastSendAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 15),
    _WflecOperConfigMulticastSendAvgRate_Type()
)
wflecOperConfigMulticastSendAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigMulticastSendAvgRate.setStatus("mandatory")
_WflecOperConfigMulticastSendPeakRate_Type = Integer32
_WflecOperConfigMulticastSendPeakRate_Object = MibTableColumn
wflecOperConfigMulticastSendPeakRate = _WflecOperConfigMulticastSendPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 16),
    _WflecOperConfigMulticastSendPeakRate_Type()
)
wflecOperConfigMulticastSendPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigMulticastSendPeakRate.setStatus("mandatory")
_WflecOperConfigConnectionCompleteTimer_Type = Integer32
_WflecOperConfigConnectionCompleteTimer_Object = MibTableColumn
wflecOperConfigConnectionCompleteTimer = _WflecOperConfigConnectionCompleteTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 3, 1, 17),
    _WflecOperConfigConnectionCompleteTimer_Type()
)
wflecOperConfigConnectionCompleteTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOperConfigConnectionCompleteTimer.setStatus("mandatory")
_WfAtmLecStatisticsTable_Object = MibTable
wfAtmLecStatisticsTable = _WfAtmLecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4)
)
if mibBuilder.loadTexts:
    wfAtmLecStatisticsTable.setStatus("mandatory")
_WfAtmLecStatisticsEntry_Object = MibTableRow
wfAtmLecStatisticsEntry = _WfAtmLecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1)
)
wfAtmLecStatisticsEntry.setIndexNames(
    (0, "Wellfleet-ATM-LE-MIB", "wflecStatisticsCct"),
)
if mibBuilder.loadTexts:
    wfAtmLecStatisticsEntry.setStatus("mandatory")
_WflecArpRequestsOut_Type = Counter32
_WflecArpRequestsOut_Object = MibTableColumn
wflecArpRequestsOut = _WflecArpRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 1),
    _WflecArpRequestsOut_Type()
)
wflecArpRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecArpRequestsOut.setStatus("mandatory")
_WflecArpRequestsIn_Type = Counter32
_WflecArpRequestsIn_Object = MibTableColumn
wflecArpRequestsIn = _WflecArpRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 2),
    _WflecArpRequestsIn_Type()
)
wflecArpRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecArpRequestsIn.setStatus("mandatory")
_WflecArpRepliesOut_Type = Counter32
_WflecArpRepliesOut_Object = MibTableColumn
wflecArpRepliesOut = _WflecArpRepliesOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 3),
    _WflecArpRepliesOut_Type()
)
wflecArpRepliesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecArpRepliesOut.setStatus("mandatory")
_WflecArpRepliesIn_Type = Counter32
_WflecArpRepliesIn_Object = MibTableColumn
wflecArpRepliesIn = _WflecArpRepliesIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 4),
    _WflecArpRepliesIn_Type()
)
wflecArpRepliesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecArpRepliesIn.setStatus("mandatory")
_WflecControlFramesOut_Type = Counter32
_WflecControlFramesOut_Object = MibTableColumn
wflecControlFramesOut = _WflecControlFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 5),
    _WflecControlFramesOut_Type()
)
wflecControlFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecControlFramesOut.setStatus("mandatory")
_WflecControlFramesIn_Type = Counter32
_WflecControlFramesIn_Object = MibTableColumn
wflecControlFramesIn = _WflecControlFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 6),
    _WflecControlFramesIn_Type()
)
wflecControlFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecControlFramesIn.setStatus("mandatory")
_WflecSvcFailures_Type = Counter32
_WflecSvcFailures_Object = MibTableColumn
wflecSvcFailures = _WflecSvcFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 7),
    _WflecSvcFailures_Type()
)
wflecSvcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecSvcFailures.setStatus("mandatory")
_WflecStatisticsCct_Type = Integer32
_WflecStatisticsCct_Object = MibTableColumn
wflecStatisticsCct = _WflecStatisticsCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 8),
    _WflecStatisticsCct_Type()
)
wflecStatisticsCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecStatisticsCct.setStatus("mandatory")
_WflecUnknownFramesDropped_Type = Counter32
_WflecUnknownFramesDropped_Object = MibTableColumn
wflecUnknownFramesDropped = _WflecUnknownFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 9),
    _WflecUnknownFramesDropped_Type()
)
wflecUnknownFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecUnknownFramesDropped.setStatus("mandatory")
_WflecInDataFrames_Type = Counter32
_WflecInDataFrames_Object = MibTableColumn
wflecInDataFrames = _WflecInDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 10),
    _WflecInDataFrames_Type()
)
wflecInDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecInDataFrames.setStatus("mandatory")
_WflecInUnicastFrames_Type = Counter32
_WflecInUnicastFrames_Object = MibTableColumn
wflecInUnicastFrames = _WflecInUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 11),
    _WflecInUnicastFrames_Type()
)
wflecInUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecInUnicastFrames.setStatus("mandatory")
_WflecInUnicastOctets_Type = Counter32
_WflecInUnicastOctets_Object = MibTableColumn
wflecInUnicastOctets = _WflecInUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 12),
    _WflecInUnicastOctets_Type()
)
wflecInUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecInUnicastOctets.setStatus("mandatory")
_WflecInMulticastFrames_Type = Counter32
_WflecInMulticastFrames_Object = MibTableColumn
wflecInMulticastFrames = _WflecInMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 13),
    _WflecInMulticastFrames_Type()
)
wflecInMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecInMulticastFrames.setStatus("mandatory")
_WflecInMulticastOctets_Type = Counter32
_WflecInMulticastOctets_Object = MibTableColumn
wflecInMulticastOctets = _WflecInMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 14),
    _WflecInMulticastOctets_Type()
)
wflecInMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecInMulticastOctets.setStatus("mandatory")
_WflecInBroadcastFrames_Type = Counter32
_WflecInBroadcastFrames_Object = MibTableColumn
wflecInBroadcastFrames = _WflecInBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 15),
    _WflecInBroadcastFrames_Type()
)
wflecInBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecInBroadcastFrames.setStatus("mandatory")
_WflecInBroadcastOctets_Type = Counter32
_WflecInBroadcastOctets_Object = MibTableColumn
wflecInBroadcastOctets = _WflecInBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 16),
    _WflecInBroadcastOctets_Type()
)
wflecInBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecInBroadcastOctets.setStatus("mandatory")
_WflecOutDataFrames_Type = Counter32
_WflecOutDataFrames_Object = MibTableColumn
wflecOutDataFrames = _WflecOutDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 17),
    _WflecOutDataFrames_Type()
)
wflecOutDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOutDataFrames.setStatus("mandatory")
_WflecOutUnknownFrames_Type = Counter32
_WflecOutUnknownFrames_Object = MibTableColumn
wflecOutUnknownFrames = _WflecOutUnknownFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 18),
    _WflecOutUnknownFrames_Type()
)
wflecOutUnknownFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOutUnknownFrames.setStatus("mandatory")
_WflecOutUnknownOctets_Type = Counter32
_WflecOutUnknownOctets_Object = MibTableColumn
wflecOutUnknownOctets = _WflecOutUnknownOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 19),
    _WflecOutUnknownOctets_Type()
)
wflecOutUnknownOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOutUnknownOctets.setStatus("mandatory")
_WflecOutMulticastFrames_Type = Counter32
_WflecOutMulticastFrames_Object = MibTableColumn
wflecOutMulticastFrames = _WflecOutMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 20),
    _WflecOutMulticastFrames_Type()
)
wflecOutMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOutMulticastFrames.setStatus("mandatory")
_WflecOutMulticastOctets_Type = Counter32
_WflecOutMulticastOctets_Object = MibTableColumn
wflecOutMulticastOctets = _WflecOutMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 21),
    _WflecOutMulticastOctets_Type()
)
wflecOutMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOutMulticastOctets.setStatus("mandatory")
_WflecOutBroadcastFrames_Type = Counter32
_WflecOutBroadcastFrames_Object = MibTableColumn
wflecOutBroadcastFrames = _WflecOutBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 22),
    _WflecOutBroadcastFrames_Type()
)
wflecOutBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOutBroadcastFrames.setStatus("mandatory")
_WflecOutBroadcastOctets_Type = Counter32
_WflecOutBroadcastOctets_Object = MibTableColumn
wflecOutBroadcastOctets = _WflecOutBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 23),
    _WflecOutBroadcastOctets_Type()
)
wflecOutBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOutBroadcastOctets.setStatus("mandatory")
_WflecOutUnicastFrames_Type = Counter32
_WflecOutUnicastFrames_Object = MibTableColumn
wflecOutUnicastFrames = _WflecOutUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 24),
    _WflecOutUnicastFrames_Type()
)
wflecOutUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOutUnicastFrames.setStatus("mandatory")
_WflecOutUnicastOctets_Type = Counter32
_WflecOutUnicastOctets_Object = MibTableColumn
wflecOutUnicastOctets = _WflecOutUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 4, 1, 25),
    _WflecOutUnicastOctets_Type()
)
wflecOutUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecOutUnicastOctets.setStatus("mandatory")
_WfAtmLecServerVccTable_Object = MibTable
wfAtmLecServerVccTable = _WfAtmLecServerVccTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5)
)
if mibBuilder.loadTexts:
    wfAtmLecServerVccTable.setStatus("mandatory")
_WfAtmLecServerVccEntry_Object = MibTableRow
wfAtmLecServerVccEntry = _WfAtmLecServerVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1)
)
wfAtmLecServerVccEntry.setIndexNames(
    (0, "Wellfleet-ATM-LE-MIB", "wflecServerVccCct"),
)
if mibBuilder.loadTexts:
    wfAtmLecServerVccEntry.setStatus("mandatory")
_WflecConfigDirectInterface_Type = Integer32
_WflecConfigDirectInterface_Object = MibTableColumn
wflecConfigDirectInterface = _WflecConfigDirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 1),
    _WflecConfigDirectInterface_Type()
)
wflecConfigDirectInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecConfigDirectInterface.setStatus("mandatory")
_WflecConfigDirectVpi_Type = Integer32
_WflecConfigDirectVpi_Object = MibTableColumn
wflecConfigDirectVpi = _WflecConfigDirectVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 2),
    _WflecConfigDirectVpi_Type()
)
wflecConfigDirectVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecConfigDirectVpi.setStatus("mandatory")
_WflecConfigDirectVci_Type = Integer32
_WflecConfigDirectVci_Object = MibTableColumn
wflecConfigDirectVci = _WflecConfigDirectVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 3),
    _WflecConfigDirectVci_Type()
)
wflecConfigDirectVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecConfigDirectVci.setStatus("mandatory")
_WflecControlDirectInterface_Type = Integer32
_WflecControlDirectInterface_Object = MibTableColumn
wflecControlDirectInterface = _WflecControlDirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 4),
    _WflecControlDirectInterface_Type()
)
wflecControlDirectInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecControlDirectInterface.setStatus("mandatory")
_WflecControlDirectVpi_Type = Integer32
_WflecControlDirectVpi_Object = MibTableColumn
wflecControlDirectVpi = _WflecControlDirectVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 5),
    _WflecControlDirectVpi_Type()
)
wflecControlDirectVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecControlDirectVpi.setStatus("mandatory")
_WflecControlDirectVci_Type = Integer32
_WflecControlDirectVci_Object = MibTableColumn
wflecControlDirectVci = _WflecControlDirectVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 6),
    _WflecControlDirectVci_Type()
)
wflecControlDirectVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecControlDirectVci.setStatus("mandatory")
_WflecControlDistributeInterface_Type = Integer32
_WflecControlDistributeInterface_Object = MibTableColumn
wflecControlDistributeInterface = _WflecControlDistributeInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 7),
    _WflecControlDistributeInterface_Type()
)
wflecControlDistributeInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecControlDistributeInterface.setStatus("mandatory")
_WflecControlDistributeVpi_Type = Integer32
_WflecControlDistributeVpi_Object = MibTableColumn
wflecControlDistributeVpi = _WflecControlDistributeVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 8),
    _WflecControlDistributeVpi_Type()
)
wflecControlDistributeVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecControlDistributeVpi.setStatus("mandatory")
_WflecControlDistributeVci_Type = Integer32
_WflecControlDistributeVci_Object = MibTableColumn
wflecControlDistributeVci = _WflecControlDistributeVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 9),
    _WflecControlDistributeVci_Type()
)
wflecControlDistributeVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecControlDistributeVci.setStatus("mandatory")
_WflecMulticastSendInterface_Type = Integer32
_WflecMulticastSendInterface_Object = MibTableColumn
wflecMulticastSendInterface = _WflecMulticastSendInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 10),
    _WflecMulticastSendInterface_Type()
)
wflecMulticastSendInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecMulticastSendInterface.setStatus("mandatory")
_WflecMulticastSendVpi_Type = Integer32
_WflecMulticastSendVpi_Object = MibTableColumn
wflecMulticastSendVpi = _WflecMulticastSendVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 11),
    _WflecMulticastSendVpi_Type()
)
wflecMulticastSendVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecMulticastSendVpi.setStatus("mandatory")
_WflecMulticastSendVci_Type = Integer32
_WflecMulticastSendVci_Object = MibTableColumn
wflecMulticastSendVci = _WflecMulticastSendVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 12),
    _WflecMulticastSendVci_Type()
)
wflecMulticastSendVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecMulticastSendVci.setStatus("mandatory")
_WflecMulticastForwardInterface_Type = Integer32
_WflecMulticastForwardInterface_Object = MibTableColumn
wflecMulticastForwardInterface = _WflecMulticastForwardInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 13),
    _WflecMulticastForwardInterface_Type()
)
wflecMulticastForwardInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecMulticastForwardInterface.setStatus("mandatory")
_WflecMulticastForwardVpi_Type = Integer32
_WflecMulticastForwardVpi_Object = MibTableColumn
wflecMulticastForwardVpi = _WflecMulticastForwardVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 14),
    _WflecMulticastForwardVpi_Type()
)
wflecMulticastForwardVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecMulticastForwardVpi.setStatus("mandatory")
_WflecMulticastForwardVci_Type = Integer32
_WflecMulticastForwardVci_Object = MibTableColumn
wflecMulticastForwardVci = _WflecMulticastForwardVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 15),
    _WflecMulticastForwardVci_Type()
)
wflecMulticastForwardVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecMulticastForwardVci.setStatus("mandatory")
_WflecServerVccCct_Type = Integer32
_WflecServerVccCct_Object = MibTableColumn
wflecServerVccCct = _WflecServerVccCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 5, 1, 16),
    _WflecServerVccCct_Type()
)
wflecServerVccCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecServerVccCct.setStatus("mandatory")
_WfAtmLecAtmAddressTable_Object = MibTable
wfAtmLecAtmAddressTable = _WfAtmLecAtmAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 6)
)
if mibBuilder.loadTexts:
    wfAtmLecAtmAddressTable.setStatus("mandatory")
_WfAtmLecAtmAddressEntry_Object = MibTableRow
wfAtmLecAtmAddressEntry = _WfAtmLecAtmAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 6, 1)
)
wfAtmLecAtmAddressEntry.setIndexNames(
    (0, "Wellfleet-ATM-LE-MIB", "wflecAtmAddressCct"),
    (0, "Wellfleet-ATM-LE-MIB", "wflecAtmAddress"),
)
if mibBuilder.loadTexts:
    wfAtmLecAtmAddressEntry.setStatus("mandatory")


class _WflecAtmAddress_Type(OctetString):
    """Custom type wflecAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_WflecAtmAddress_Type.__name__ = "OctetString"
_WflecAtmAddress_Object = MibTableColumn
wflecAtmAddress = _WflecAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 6, 1, 1),
    _WflecAtmAddress_Type()
)
wflecAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecAtmAddress.setStatus("mandatory")


class _WflecAtmAddressStatus_Type(Integer32):
    """Custom type wflecAtmAddressStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsbl", 2),
          ("enbl", 1))
    )


_WflecAtmAddressStatus_Type.__name__ = "Integer32"
_WflecAtmAddressStatus_Object = MibTableColumn
wflecAtmAddressStatus = _WflecAtmAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 6, 1, 2),
    _WflecAtmAddressStatus_Type()
)
wflecAtmAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wflecAtmAddressStatus.setStatus("mandatory")
_WflecAtmAddressCct_Type = Integer32
_WflecAtmAddressCct_Object = MibTableColumn
wflecAtmAddressCct = _WflecAtmAddressCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 6, 1, 3),
    _WflecAtmAddressCct_Type()
)
wflecAtmAddressCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecAtmAddressCct.setStatus("mandatory")
_WfAtmLecMacAddressTable_Object = MibTable
wfAtmLecMacAddressTable = _WfAtmLecMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 7)
)
if mibBuilder.loadTexts:
    wfAtmLecMacAddressTable.setStatus("mandatory")
_WfAtmLecMacAddressEntry_Object = MibTableRow
wfAtmLecMacAddressEntry = _WfAtmLecMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 7, 1)
)
wfAtmLecMacAddressEntry.setIndexNames(
    (0, "Wellfleet-ATM-LE-MIB", "wflecMacAddressCct"),
    (0, "Wellfleet-ATM-LE-MIB", "wflecMacAddress"),
)
if mibBuilder.loadTexts:
    wfAtmLecMacAddressEntry.setStatus("mandatory")


class _WflecMacAddress_Type(OctetString):
    """Custom type wflecMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WflecMacAddress_Type.__name__ = "OctetString"
_WflecMacAddress_Object = MibTableColumn
wflecMacAddress = _WflecMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 7, 1, 1),
    _WflecMacAddress_Type()
)
wflecMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecMacAddress.setStatus("mandatory")
_WflecMacAddressAtmBinding_Type = OctetString
_WflecMacAddressAtmBinding_Object = MibTableColumn
wflecMacAddressAtmBinding = _WflecMacAddressAtmBinding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 7, 1, 2),
    _WflecMacAddressAtmBinding_Type()
)
wflecMacAddressAtmBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecMacAddressAtmBinding.setStatus("mandatory")
_WflecMacAddressCct_Type = Integer32
_WflecMacAddressCct_Object = MibTableColumn
wflecMacAddressCct = _WflecMacAddressCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 7, 1, 3),
    _WflecMacAddressCct_Type()
)
wflecMacAddressCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wflecMacAddressCct.setStatus("mandatory")
_WfAtmLeArpTable_Object = MibTable
wfAtmLeArpTable = _WfAtmLeArpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 8)
)
if mibBuilder.loadTexts:
    wfAtmLeArpTable.setStatus("mandatory")
_WfAtmLeArpEntry_Object = MibTableRow
wfAtmLeArpEntry = _WfAtmLeArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 8, 1)
)
wfAtmLeArpEntry.setIndexNames(
    (0, "Wellfleet-ATM-LE-MIB", "wfleArpCct"),
    (0, "Wellfleet-ATM-LE-MIB", "wfleArpMacAddress"),
)
if mibBuilder.loadTexts:
    wfAtmLeArpEntry.setStatus("mandatory")


class _WfleArpMacAddress_Type(OctetString):
    """Custom type wfleArpMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfleArpMacAddress_Type.__name__ = "OctetString"
_WfleArpMacAddress_Object = MibTableColumn
wfleArpMacAddress = _WfleArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 8, 1, 1),
    _WfleArpMacAddress_Type()
)
wfleArpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleArpMacAddress.setStatus("mandatory")
_WfleArpAtmAddress_Type = OctetString
_WfleArpAtmAddress_Object = MibTableColumn
wfleArpAtmAddress = _WfleArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 8, 1, 2),
    _WfleArpAtmAddress_Type()
)
wfleArpAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleArpAtmAddress.setStatus("mandatory")


class _WfleArpIsRemoteAddress_Type(Integer32):
    """Custom type wfleArpIsRemoteAddress based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfleArpIsRemoteAddress_Type.__name__ = "Integer32"
_WfleArpIsRemoteAddress_Object = MibTableColumn
wfleArpIsRemoteAddress = _WfleArpIsRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 8, 1, 3),
    _WfleArpIsRemoteAddress_Type()
)
wfleArpIsRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleArpIsRemoteAddress.setStatus("mandatory")


class _WfleArpEntryType_Type(Integer32):
    """Custom type wfleArpEntryType based on Integer32"""
    defaultValue = 4

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
        *(("ctrl", 2),
          ("data", 3),
          ("nonvol", 5),
          ("other", 1),
          ("vol", 4))
    )


_WfleArpEntryType_Type.__name__ = "Integer32"
_WfleArpEntryType_Object = MibTableColumn
wfleArpEntryType = _WfleArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 8, 1, 4),
    _WfleArpEntryType_Type()
)
wfleArpEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleArpEntryType.setStatus("mandatory")


class _WfleArpRowStatus_Type(Integer32):
    """Custom type wfleArpRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsbl", 2),
          ("enbl", 1))
    )


_WfleArpRowStatus_Type.__name__ = "Integer32"
_WfleArpRowStatus_Object = MibTableColumn
wfleArpRowStatus = _WfleArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 8, 1, 5),
    _WfleArpRowStatus_Type()
)
wfleArpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfleArpRowStatus.setStatus("mandatory")
_WfleArpCct_Type = Integer32
_WfleArpCct_Object = MibTableColumn
wfleArpCct = _WfleArpCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 8, 1, 6),
    _WfleArpCct_Type()
)
wfleArpCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleArpCct.setStatus("mandatory")
_WfleArpVpi_Type = Integer32
_WfleArpVpi_Object = MibTableColumn
wfleArpVpi = _WfleArpVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 8, 1, 7),
    _WfleArpVpi_Type()
)
wfleArpVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleArpVpi.setStatus("mandatory")
_WfleArpVci_Type = Integer32
_WfleArpVci_Object = MibTableColumn
wfleArpVci = _WfleArpVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 8, 1, 8),
    _WfleArpVci_Type()
)
wfleArpVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleArpVci.setStatus("mandatory")
_WfAtmLeRDArpTable_Object = MibTable
wfAtmLeRDArpTable = _WfAtmLeRDArpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 9)
)
if mibBuilder.loadTexts:
    wfAtmLeRDArpTable.setStatus("mandatory")
_WfAtmLeRDArpEntry_Object = MibTableRow
wfAtmLeRDArpEntry = _WfAtmLeRDArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 9, 1)
)
wfAtmLeRDArpEntry.setIndexNames(
    (0, "Wellfleet-ATM-LE-MIB", "wfleRDArpCct"),
    (0, "Wellfleet-ATM-LE-MIB", "wfleRDArpSegmentID"),
    (0, "Wellfleet-ATM-LE-MIB", "wfleRDArpBridgeNumber"),
)
if mibBuilder.loadTexts:
    wfAtmLeRDArpEntry.setStatus("mandatory")


class _WfleRDArpSegmentID_Type(Integer32):
    """Custom type wfleRDArpSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WfleRDArpSegmentID_Type.__name__ = "Integer32"
_WfleRDArpSegmentID_Object = MibTableColumn
wfleRDArpSegmentID = _WfleRDArpSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 9, 1, 1),
    _WfleRDArpSegmentID_Type()
)
wfleRDArpSegmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleRDArpSegmentID.setStatus("mandatory")


class _WfleRDArpBridgeNumber_Type(Integer32):
    """Custom type wfleRDArpBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfleRDArpBridgeNumber_Type.__name__ = "Integer32"
_WfleRDArpBridgeNumber_Object = MibTableColumn
wfleRDArpBridgeNumber = _WfleRDArpBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 9, 1, 2),
    _WfleRDArpBridgeNumber_Type()
)
wfleRDArpBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleRDArpBridgeNumber.setStatus("mandatory")
_WfleRDArpAtmAddress_Type = OctetString
_WfleRDArpAtmAddress_Object = MibTableColumn
wfleRDArpAtmAddress = _WfleRDArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 9, 1, 3),
    _WfleRDArpAtmAddress_Type()
)
wfleRDArpAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleRDArpAtmAddress.setStatus("mandatory")


class _WfleRDArpEntryType_Type(Integer32):
    """Custom type wfleRDArpEntryType based on Integer32"""
    defaultValue = 4

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
        *(("ctrl", 2),
          ("data", 3),
          ("nonvol", 5),
          ("other", 1),
          ("vol", 4))
    )


_WfleRDArpEntryType_Type.__name__ = "Integer32"
_WfleRDArpEntryType_Object = MibTableColumn
wfleRDArpEntryType = _WfleRDArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 9, 1, 4),
    _WfleRDArpEntryType_Type()
)
wfleRDArpEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleRDArpEntryType.setStatus("mandatory")


class _WfleRDArpRowStatus_Type(Integer32):
    """Custom type wfleRDArpRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsbl", 2),
          ("enbl", 1))
    )


_WfleRDArpRowStatus_Type.__name__ = "Integer32"
_WfleRDArpRowStatus_Object = MibTableColumn
wfleRDArpRowStatus = _WfleRDArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 9, 1, 5),
    _WfleRDArpRowStatus_Type()
)
wfleRDArpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfleRDArpRowStatus.setStatus("mandatory")
_WfleRDArpCct_Type = Integer32
_WfleRDArpCct_Object = MibTableColumn
wfleRDArpCct = _WfleRDArpCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 9, 1, 6),
    _WfleRDArpCct_Type()
)
wfleRDArpCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleRDArpCct.setStatus("mandatory")
_WfleRDArpVpi_Type = Integer32
_WfleRDArpVpi_Object = MibTableColumn
wfleRDArpVpi = _WfleRDArpVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 9, 1, 7),
    _WfleRDArpVpi_Type()
)
wfleRDArpVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleRDArpVpi.setStatus("mandatory")
_WfleRDArpVci_Type = Integer32
_WfleRDArpVci_Object = MibTableColumn
wfleRDArpVci = _WfleRDArpVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 9, 1, 8),
    _WfleRDArpVci_Type()
)
wfleRDArpVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfleRDArpVci.setStatus("mandatory")
_WfAtmLecConfigLesTable_Object = MibTable
wfAtmLecConfigLesTable = _WfAtmLecConfigLesTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 10)
)
if mibBuilder.loadTexts:
    wfAtmLecConfigLesTable.setStatus("mandatory")
_WfAtmLecConfigLesEntry_Object = MibTableRow
wfAtmLecConfigLesEntry = _WfAtmLecConfigLesEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 10, 1)
)
wfAtmLecConfigLesEntry.setIndexNames(
    (0, "Wellfleet-ATM-LE-MIB", "wfAtmLecConfigLesCct"),
    (0, "Wellfleet-ATM-LE-MIB", "wfAtmLecConfigLesIndex"),
)
if mibBuilder.loadTexts:
    wfAtmLecConfigLesEntry.setStatus("mandatory")


class _WfAtmLecConfigLesDelete_Type(Integer32):
    """Custom type wfAtmLecConfigLesDelete based on Integer32"""
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


_WfAtmLecConfigLesDelete_Type.__name__ = "Integer32"
_WfAtmLecConfigLesDelete_Object = MibTableColumn
wfAtmLecConfigLesDelete = _WfAtmLecConfigLesDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 10, 1, 1),
    _WfAtmLecConfigLesDelete_Type()
)
wfAtmLecConfigLesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmLecConfigLesDelete.setStatus("mandatory")


class _WfAtmLecConfigLesEnable_Type(Integer32):
    """Custom type wfAtmLecConfigLesEnable based on Integer32"""
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


_WfAtmLecConfigLesEnable_Type.__name__ = "Integer32"
_WfAtmLecConfigLesEnable_Object = MibTableColumn
wfAtmLecConfigLesEnable = _WfAtmLecConfigLesEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 10, 1, 2),
    _WfAtmLecConfigLesEnable_Type()
)
wfAtmLecConfigLesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmLecConfigLesEnable.setStatus("mandatory")


class _WfAtmLecConfigLesCct_Type(Integer32):
    """Custom type wfAtmLecConfigLesCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfAtmLecConfigLesCct_Type.__name__ = "Integer32"
_WfAtmLecConfigLesCct_Object = MibTableColumn
wfAtmLecConfigLesCct = _WfAtmLecConfigLesCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 10, 1, 3),
    _WfAtmLecConfigLesCct_Type()
)
wfAtmLecConfigLesCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmLecConfigLesCct.setStatus("mandatory")


class _WfAtmLecConfigLesIndex_Type(Integer32):
    """Custom type wfAtmLecConfigLesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfAtmLecConfigLesIndex_Type.__name__ = "Integer32"
_WfAtmLecConfigLesIndex_Object = MibTableColumn
wfAtmLecConfigLesIndex = _WfAtmLecConfigLesIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 10, 1, 4),
    _WfAtmLecConfigLesIndex_Type()
)
wfAtmLecConfigLesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmLecConfigLesIndex.setStatus("mandatory")
_WfAtmLecConfigLesAddress_Type = OctetString
_WfAtmLecConfigLesAddress_Object = MibTableColumn
wfAtmLecConfigLesAddress = _WfAtmLecConfigLesAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 10, 1, 5),
    _WfAtmLecConfigLesAddress_Type()
)
wfAtmLecConfigLesAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmLecConfigLesAddress.setStatus("mandatory")
_WfAtmLecConfigLesName_Type = DisplayString
_WfAtmLecConfigLesName_Object = MibTableColumn
wfAtmLecConfigLesName = _WfAtmLecConfigLesName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20, 10, 1, 6),
    _WfAtmLecConfigLesName_Type()
)
wfAtmLecConfigLesName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmLecConfigLesName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-ATM-LE-MIB",
    **{"wfAtmLecConfigTable": wfAtmLecConfigTable,
       "wfAtmLecConfigEntry": wfAtmLecConfigEntry,
       "wflecConfDelete": wflecConfDelete,
       "wflecRowStatus": wflecRowStatus,
       "wflecConfigCct": wflecConfigCct,
       "wflecOwner": wflecOwner,
       "wflecConfigMode": wflecConfigMode,
       "wflecConfigLanType": wflecConfigLanType,
       "wflecConfigMaxDataFrameSize": wflecConfigMaxDataFrameSize,
       "wflecConfigLanName": wflecConfigLanName,
       "wflecConfigLesAtmAddress": wflecConfigLesAtmAddress,
       "wflecControlTimeout": wflecControlTimeout,
       "wflecMaxUnknownFrameCount": wflecMaxUnknownFrameCount,
       "wflecMaxUnknownFrameTime": wflecMaxUnknownFrameTime,
       "wflecVccTimeoutPeriod": wflecVccTimeoutPeriod,
       "wflecMaxRetryCount": wflecMaxRetryCount,
       "wflecAgingTime": wflecAgingTime,
       "wflecForwardDelayTime": wflecForwardDelayTime,
       "wflecExpectedArpResponseTime": wflecExpectedArpResponseTime,
       "wflecFlushTimeOut": wflecFlushTimeOut,
       "wflecPathSwitchingDelay": wflecPathSwitchingDelay,
       "wflecLocalSegmentID": wflecLocalSegmentID,
       "wflecMulticastSendType": wflecMulticastSendType,
       "wflecMulticastSendAvgRate": wflecMulticastSendAvgRate,
       "wflecMulticastSendPeakRate": wflecMulticastSendPeakRate,
       "wflecConnectionCompleteTimer": wflecConnectionCompleteTimer,
       "wflecFlushEnable": wflecFlushEnable,
       "wflecConfigRetry": wflecConfigRetry,
       "wflecMulticastFwdTimeout": wflecMulticastFwdTimeout,
       "wflecMulticastFwdRetry": wflecMulticastFwdRetry,
       "wflecDebugLevel": wflecDebugLevel,
       "wflecConfigLECSAtmAddress": wflecConfigLECSAtmAddress,
       "wflecConfigV2Capable": wflecConfigV2Capable,
       "wfAtmLecStatusTable": wfAtmLecStatusTable,
       "wfAtmLecStatusEntry": wfAtmLecStatusEntry,
       "wflecStatusCct": wflecStatusCct,
       "wflecPrimaryAtmAddress": wflecPrimaryAtmAddress,
       "wflecID": wflecID,
       "wflecInterfaceState": wflecInterfaceState,
       "wflecLastFailureRespCode": wflecLastFailureRespCode,
       "wflecLastFailureState": wflecLastFailureState,
       "wflecProtocol": wflecProtocol,
       "wflecVersion": wflecVersion,
       "wflecTopologyChange": wflecTopologyChange,
       "wflecConfigServerAtmAddress": wflecConfigServerAtmAddress,
       "wflecConfigSource": wflecConfigSource,
       "wflecActualLanType": wflecActualLanType,
       "wflecActualMaxDataFrameSize": wflecActualMaxDataFrameSize,
       "wflecActualLanName": wflecActualLanName,
       "wflecActualLesAtmAddress": wflecActualLesAtmAddress,
       "wflecProxyClient": wflecProxyClient,
       "wfAtmLecOperConfigTable": wfAtmLecOperConfigTable,
       "wfAtmLecOperConfigEntry": wfAtmLecOperConfigEntry,
       "wflecOperConfigCct": wflecOperConfigCct,
       "wflecOperConfigControlTimeout": wflecOperConfigControlTimeout,
       "wflecOperConfigMaxUnknownFrameCount": wflecOperConfigMaxUnknownFrameCount,
       "wflecOperConfigMaxUnknownFrameTime": wflecOperConfigMaxUnknownFrameTime,
       "wflecOperConfigVccTimeoutPeriod": wflecOperConfigVccTimeoutPeriod,
       "wflecOperConfigMaxRetryCount": wflecOperConfigMaxRetryCount,
       "wflecOperConfigAgingTime": wflecOperConfigAgingTime,
       "wflecOperConfigForwardDelayTime": wflecOperConfigForwardDelayTime,
       "wflecOperConfigTopologyChange": wflecOperConfigTopologyChange,
       "wflecOperConfigExpectedArpResponseTime": wflecOperConfigExpectedArpResponseTime,
       "wflecOperConfigFlushTimeOut": wflecOperConfigFlushTimeOut,
       "wflecOperConfigPathSwitchingDelay": wflecOperConfigPathSwitchingDelay,
       "wflecOperConfigLocalSegmentID": wflecOperConfigLocalSegmentID,
       "wflecOperConfigMulticastSendType": wflecOperConfigMulticastSendType,
       "wflecOperConfigMulticastSendAvgRate": wflecOperConfigMulticastSendAvgRate,
       "wflecOperConfigMulticastSendPeakRate": wflecOperConfigMulticastSendPeakRate,
       "wflecOperConfigConnectionCompleteTimer": wflecOperConfigConnectionCompleteTimer,
       "wfAtmLecStatisticsTable": wfAtmLecStatisticsTable,
       "wfAtmLecStatisticsEntry": wfAtmLecStatisticsEntry,
       "wflecArpRequestsOut": wflecArpRequestsOut,
       "wflecArpRequestsIn": wflecArpRequestsIn,
       "wflecArpRepliesOut": wflecArpRepliesOut,
       "wflecArpRepliesIn": wflecArpRepliesIn,
       "wflecControlFramesOut": wflecControlFramesOut,
       "wflecControlFramesIn": wflecControlFramesIn,
       "wflecSvcFailures": wflecSvcFailures,
       "wflecStatisticsCct": wflecStatisticsCct,
       "wflecUnknownFramesDropped": wflecUnknownFramesDropped,
       "wflecInDataFrames": wflecInDataFrames,
       "wflecInUnicastFrames": wflecInUnicastFrames,
       "wflecInUnicastOctets": wflecInUnicastOctets,
       "wflecInMulticastFrames": wflecInMulticastFrames,
       "wflecInMulticastOctets": wflecInMulticastOctets,
       "wflecInBroadcastFrames": wflecInBroadcastFrames,
       "wflecInBroadcastOctets": wflecInBroadcastOctets,
       "wflecOutDataFrames": wflecOutDataFrames,
       "wflecOutUnknownFrames": wflecOutUnknownFrames,
       "wflecOutUnknownOctets": wflecOutUnknownOctets,
       "wflecOutMulticastFrames": wflecOutMulticastFrames,
       "wflecOutMulticastOctets": wflecOutMulticastOctets,
       "wflecOutBroadcastFrames": wflecOutBroadcastFrames,
       "wflecOutBroadcastOctets": wflecOutBroadcastOctets,
       "wflecOutUnicastFrames": wflecOutUnicastFrames,
       "wflecOutUnicastOctets": wflecOutUnicastOctets,
       "wfAtmLecServerVccTable": wfAtmLecServerVccTable,
       "wfAtmLecServerVccEntry": wfAtmLecServerVccEntry,
       "wflecConfigDirectInterface": wflecConfigDirectInterface,
       "wflecConfigDirectVpi": wflecConfigDirectVpi,
       "wflecConfigDirectVci": wflecConfigDirectVci,
       "wflecControlDirectInterface": wflecControlDirectInterface,
       "wflecControlDirectVpi": wflecControlDirectVpi,
       "wflecControlDirectVci": wflecControlDirectVci,
       "wflecControlDistributeInterface": wflecControlDistributeInterface,
       "wflecControlDistributeVpi": wflecControlDistributeVpi,
       "wflecControlDistributeVci": wflecControlDistributeVci,
       "wflecMulticastSendInterface": wflecMulticastSendInterface,
       "wflecMulticastSendVpi": wflecMulticastSendVpi,
       "wflecMulticastSendVci": wflecMulticastSendVci,
       "wflecMulticastForwardInterface": wflecMulticastForwardInterface,
       "wflecMulticastForwardVpi": wflecMulticastForwardVpi,
       "wflecMulticastForwardVci": wflecMulticastForwardVci,
       "wflecServerVccCct": wflecServerVccCct,
       "wfAtmLecAtmAddressTable": wfAtmLecAtmAddressTable,
       "wfAtmLecAtmAddressEntry": wfAtmLecAtmAddressEntry,
       "wflecAtmAddress": wflecAtmAddress,
       "wflecAtmAddressStatus": wflecAtmAddressStatus,
       "wflecAtmAddressCct": wflecAtmAddressCct,
       "wfAtmLecMacAddressTable": wfAtmLecMacAddressTable,
       "wfAtmLecMacAddressEntry": wfAtmLecMacAddressEntry,
       "wflecMacAddress": wflecMacAddress,
       "wflecMacAddressAtmBinding": wflecMacAddressAtmBinding,
       "wflecMacAddressCct": wflecMacAddressCct,
       "wfAtmLeArpTable": wfAtmLeArpTable,
       "wfAtmLeArpEntry": wfAtmLeArpEntry,
       "wfleArpMacAddress": wfleArpMacAddress,
       "wfleArpAtmAddress": wfleArpAtmAddress,
       "wfleArpIsRemoteAddress": wfleArpIsRemoteAddress,
       "wfleArpEntryType": wfleArpEntryType,
       "wfleArpRowStatus": wfleArpRowStatus,
       "wfleArpCct": wfleArpCct,
       "wfleArpVpi": wfleArpVpi,
       "wfleArpVci": wfleArpVci,
       "wfAtmLeRDArpTable": wfAtmLeRDArpTable,
       "wfAtmLeRDArpEntry": wfAtmLeRDArpEntry,
       "wfleRDArpSegmentID": wfleRDArpSegmentID,
       "wfleRDArpBridgeNumber": wfleRDArpBridgeNumber,
       "wfleRDArpAtmAddress": wfleRDArpAtmAddress,
       "wfleRDArpEntryType": wfleRDArpEntryType,
       "wfleRDArpRowStatus": wfleRDArpRowStatus,
       "wfleRDArpCct": wfleRDArpCct,
       "wfleRDArpVpi": wfleRDArpVpi,
       "wfleRDArpVci": wfleRDArpVci,
       "wfAtmLecConfigLesTable": wfAtmLecConfigLesTable,
       "wfAtmLecConfigLesEntry": wfAtmLecConfigLesEntry,
       "wfAtmLecConfigLesDelete": wfAtmLecConfigLesDelete,
       "wfAtmLecConfigLesEnable": wfAtmLecConfigLesEnable,
       "wfAtmLecConfigLesCct": wfAtmLecConfigLesCct,
       "wfAtmLecConfigLesIndex": wfAtmLecConfigLesIndex,
       "wfAtmLecConfigLesAddress": wfAtmLecConfigLesAddress,
       "wfAtmLecConfigLesName": wfAtmLecConfigLesName}
)
