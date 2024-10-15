# SNMP MIB module (INTEL-CSU-HW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-CSU-HW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:33 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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
 iso,
 private) = mibBuilder.importSymbols(
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
    "iso",
    "private")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Csudsu_ObjectIdentity = ObjectIdentity
csudsu = _Csudsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 36)
)
_Csu_ObjectIdentity = ObjectIdentity
csu = _Csu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1)
)
_CsuInfoTable_Object = MibTable
csuInfoTable = _CsuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1)
)
if mibBuilder.loadTexts:
    csuInfoTable.setStatus("mandatory")
_CsuInfoEntry_Object = MibTableRow
csuInfoEntry = _CsuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1)
)
csuInfoEntry.setIndexNames(
    (0, "INTEL-CSU-HW-MIB", "csuInfoLineIndex"),
)
if mibBuilder.loadTexts:
    csuInfoEntry.setStatus("mandatory")


class _CsuInfoLineIndex_Type(Integer32):
    """Custom type csuInfoLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CsuInfoLineIndex_Type.__name__ = "Integer32"
_CsuInfoLineIndex_Object = MibTableColumn
csuInfoLineIndex = _CsuInfoLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 1),
    _CsuInfoLineIndex_Type()
)
csuInfoLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuInfoLineIndex.setStatus("mandatory")


class _CsuAlarm_Type(Integer32):
    """Custom type csuAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("csuAlarmBLUE", 4),
          ("csuAlarmNone", 1),
          ("csuAlarmOUTOFFRAMING", 16),
          ("csuAlarmRED", 2),
          ("csuAlarmYELLOW", 8))
    )


_CsuAlarm_Type.__name__ = "Integer32"
_CsuAlarm_Object = MibTableColumn
csuAlarm = _CsuAlarm_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 2),
    _CsuAlarm_Type()
)
csuAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuAlarm.setStatus("mandatory")


class _CsuReceiveLevel_Type(Integer32):
    """Custom type csuReceiveLevel based on Integer32"""
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
        *(("csuReceiveLevelLessThanMinus22Point5", 4),
          ("csuReceiveLevelMinus15ToMinus22point5", 3),
          ("csuReceiveLevelMinus7Point5ToMinus15", 2),
          ("csuReceiveLevelPlus2ToMinus7Point5", 1))
    )


_CsuReceiveLevel_Type.__name__ = "Integer32"
_CsuReceiveLevel_Object = MibTableColumn
csuReceiveLevel = _CsuReceiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 3),
    _CsuReceiveLevel_Type()
)
csuReceiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuReceiveLevel.setStatus("mandatory")


class _CsuLoopbackState_Type(Integer32):
    """Custom type csuLoopbackState based on Integer32"""
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
        *(("csuLoopbackLocalChannel", 4),
          ("csuLoopbackLocalLine", 3),
          ("csuLoopbackLocalPayload", 2),
          ("csuLoopbackNone", 1),
          ("csuLoopbackRemoteChannel", 7),
          ("csuLoopbackRemoteLine", 6),
          ("csuLoopbackRemotePayload", 5))
    )


_CsuLoopbackState_Type.__name__ = "Integer32"
_CsuLoopbackState_Object = MibTableColumn
csuLoopbackState = _CsuLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 4),
    _CsuLoopbackState_Type()
)
csuLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuLoopbackState.setStatus("mandatory")
_CsuLossofsynchronization_Type = Counter32
_CsuLossofsynchronization_Object = MibTableColumn
csuLossofsynchronization = _CsuLossofsynchronization_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 5),
    _CsuLossofsynchronization_Type()
)
csuLossofsynchronization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuLossofsynchronization.setStatus("mandatory")
_CsuChangeofFrameAlignment_Type = Counter32
_CsuChangeofFrameAlignment_Object = MibTableColumn
csuChangeofFrameAlignment = _CsuChangeofFrameAlignment_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 6),
    _CsuChangeofFrameAlignment_Type()
)
csuChangeofFrameAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuChangeofFrameAlignment.setStatus("mandatory")
_CsuEightZeroDetect_Type = Counter32
_CsuEightZeroDetect_Object = MibTableColumn
csuEightZeroDetect = _CsuEightZeroDetect_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 7),
    _CsuEightZeroDetect_Type()
)
csuEightZeroDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuEightZeroDetect.setStatus("mandatory")
_CsuSixteenZeroDetect_Type = Counter32
_CsuSixteenZeroDetect_Object = MibTableColumn
csuSixteenZeroDetect = _CsuSixteenZeroDetect_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 8),
    _CsuSixteenZeroDetect_Type()
)
csuSixteenZeroDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuSixteenZeroDetect.setStatus("mandatory")
_CsuSeverelyErroredFramingEvent_Type = Counter32
_CsuSeverelyErroredFramingEvent_Object = MibTableColumn
csuSeverelyErroredFramingEvent = _CsuSeverelyErroredFramingEvent_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 9),
    _CsuSeverelyErroredFramingEvent_Type()
)
csuSeverelyErroredFramingEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuSeverelyErroredFramingEvent.setStatus("mandatory")
_CsuB8ZSCodeWordDetect_Type = Counter32
_CsuB8ZSCodeWordDetect_Object = MibTableColumn
csuB8ZSCodeWordDetect = _CsuB8ZSCodeWordDetect_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 10),
    _CsuB8ZSCodeWordDetect_Type()
)
csuB8ZSCodeWordDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuB8ZSCodeWordDetect.setStatus("mandatory")
_CsuFrameBitError_Type = Counter32
_CsuFrameBitError_Object = MibTableColumn
csuFrameBitError = _CsuFrameBitError_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 11),
    _CsuFrameBitError_Type()
)
csuFrameBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFrameBitError.setStatus("mandatory")
_CsuReceivePulseDensityViolation_Type = Counter32
_CsuReceivePulseDensityViolation_Object = MibTableColumn
csuReceivePulseDensityViolation = _CsuReceivePulseDensityViolation_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 12),
    _CsuReceivePulseDensityViolation_Type()
)
csuReceivePulseDensityViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuReceivePulseDensityViolation.setStatus("mandatory")
_CsuTransmitPulseDensityViolation_Type = Counter32
_CsuTransmitPulseDensityViolation_Object = MibTableColumn
csuTransmitPulseDensityViolation = _CsuTransmitPulseDensityViolation_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 13),
    _CsuTransmitPulseDensityViolation_Type()
)
csuTransmitPulseDensityViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuTransmitPulseDensityViolation.setStatus("mandatory")
_CsuJitterAttenuatorLimitTrip_Type = Counter32
_CsuJitterAttenuatorLimitTrip_Object = MibTableColumn
csuJitterAttenuatorLimitTrip = _CsuJitterAttenuatorLimitTrip_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 14),
    _CsuJitterAttenuatorLimitTrip_Type()
)
csuJitterAttenuatorLimitTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuJitterAttenuatorLimitTrip.setStatus("mandatory")
_CsuLossofReceiveClock_Type = Counter32
_CsuLossofReceiveClock_Object = MibTableColumn
csuLossofReceiveClock = _CsuLossofReceiveClock_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 15),
    _CsuLossofReceiveClock_Type()
)
csuLossofReceiveClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuLossofReceiveClock.setStatus("mandatory")
_CsuFramerReceiveCarrierLoss_Type = Counter32
_CsuFramerReceiveCarrierLoss_Object = MibTableColumn
csuFramerReceiveCarrierLoss = _CsuFramerReceiveCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 16),
    _CsuFramerReceiveCarrierLoss_Type()
)
csuFramerReceiveCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFramerReceiveCarrierLoss.setStatus("mandatory")
_CsuLineCodeViolationCount_Type = Counter32
_CsuLineCodeViolationCount_Object = MibTableColumn
csuLineCodeViolationCount = _CsuLineCodeViolationCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 17),
    _CsuLineCodeViolationCount_Type()
)
csuLineCodeViolationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuLineCodeViolationCount.setStatus("mandatory")
_CsuPathCodeViolationCount_Type = Counter32
_CsuPathCodeViolationCount_Object = MibTableColumn
csuPathCodeViolationCount = _CsuPathCodeViolationCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 18),
    _CsuPathCodeViolationCount_Type()
)
csuPathCodeViolationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuPathCodeViolationCount.setStatus("mandatory")
_CsuMultiframesOutofSyncCount_Type = Counter32
_CsuMultiframesOutofSyncCount_Object = MibTableColumn
csuMultiframesOutofSyncCount = _CsuMultiframesOutofSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 19),
    _CsuMultiframesOutofSyncCount_Type()
)
csuMultiframesOutofSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuMultiframesOutofSyncCount.setStatus("mandatory")
_CsuCRC6errors_Type = Counter32
_CsuCRC6errors_Object = MibTableColumn
csuCRC6errors = _CsuCRC6errors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 20),
    _CsuCRC6errors_Type()
)
csuCRC6errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuCRC6errors.setStatus("mandatory")


class _CsuErrorRate_Type(DisplayString):
    """Custom type csuErrorRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsuErrorRate_Type.__name__ = "DisplayString"
_CsuErrorRate_Object = MibTableColumn
csuErrorRate = _CsuErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 21),
    _CsuErrorRate_Type()
)
csuErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuErrorRate.setStatus("mandatory")


class _CsuLinkState_Type(Integer32):
    """Custom type csuLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuLinkStateDown", 2),
          ("csuLinkStateUp", 1))
    )


_CsuLinkState_Type.__name__ = "Integer32"
_CsuLinkState_Object = MibTableColumn
csuLinkState = _CsuLinkState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 22),
    _CsuLinkState_Type()
)
csuLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuLinkState.setStatus("mandatory")
_CsuErrorsThisSecond_Type = Counter32
_CsuErrorsThisSecond_Object = MibTableColumn
csuErrorsThisSecond = _CsuErrorsThisSecond_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 23),
    _CsuErrorsThisSecond_Type()
)
csuErrorsThisSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuErrorsThisSecond.setStatus("mandatory")
_CsuPercentEFS_Type = Integer32
_CsuPercentEFS_Object = MibTableColumn
csuPercentEFS = _CsuPercentEFS_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 24),
    _CsuPercentEFS_Type()
)
csuPercentEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuPercentEFS.setStatus("mandatory")


class _CsuTXChannelPayload_Type(DisplayString):
    """Custom type csuTXChannelPayload based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsuTXChannelPayload_Type.__name__ = "DisplayString"
_CsuTXChannelPayload_Object = MibTableColumn
csuTXChannelPayload = _CsuTXChannelPayload_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 25),
    _CsuTXChannelPayload_Type()
)
csuTXChannelPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuTXChannelPayload.setStatus("mandatory")


class _CsuRXChannelPayload_Type(DisplayString):
    """Custom type csuRXChannelPayload based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsuRXChannelPayload_Type.__name__ = "DisplayString"
_CsuRXChannelPayload_Object = MibTableColumn
csuRXChannelPayload = _CsuRXChannelPayload_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 26),
    _CsuRXChannelPayload_Type()
)
csuRXChannelPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuRXChannelPayload.setStatus("mandatory")


class _CsuDetectedChannelMap_Type(DisplayString):
    """Custom type csuDetectedChannelMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsuDetectedChannelMap_Type.__name__ = "DisplayString"
_CsuDetectedChannelMap_Object = MibTableColumn
csuDetectedChannelMap = _CsuDetectedChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 27),
    _CsuDetectedChannelMap_Type()
)
csuDetectedChannelMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuDetectedChannelMap.setStatus("mandatory")
_CsuYellowAlarmCount_Type = Counter32
_CsuYellowAlarmCount_Object = MibTableColumn
csuYellowAlarmCount = _CsuYellowAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 28),
    _CsuYellowAlarmCount_Type()
)
csuYellowAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuYellowAlarmCount.setStatus("mandatory")
_CsuAISDefects_Type = Counter32
_CsuAISDefects_Object = MibTableColumn
csuAISDefects = _CsuAISDefects_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 1, 1, 29),
    _CsuAISDefects_Type()
)
csuAISDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuAISDefects.setStatus("mandatory")
_CsuConfigTable_Object = MibTable
csuConfigTable = _CsuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2)
)
if mibBuilder.loadTexts:
    csuConfigTable.setStatus("mandatory")
_CsuConfigEntry_Object = MibTableRow
csuConfigEntry = _CsuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1)
)
csuConfigEntry.setIndexNames(
    (0, "INTEL-CSU-HW-MIB", "csuConfigLineIndex"),
)
if mibBuilder.loadTexts:
    csuConfigEntry.setStatus("mandatory")


class _CsuConfigLineIndex_Type(Integer32):
    """Custom type csuConfigLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CsuConfigLineIndex_Type.__name__ = "Integer32"
_CsuConfigLineIndex_Object = MibTableColumn
csuConfigLineIndex = _CsuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 1),
    _CsuConfigLineIndex_Type()
)
csuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuConfigLineIndex.setStatus("mandatory")


class _CsuChannelBandwidth_Type(Integer32):
    """Custom type csuChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csu56kbps", 2),
          ("csu64kbps", 1),
          ("csuAutoBandwidth", 3))
    )


_CsuChannelBandwidth_Type.__name__ = "Integer32"
_CsuChannelBandwidth_Object = MibTableColumn
csuChannelBandwidth = _CsuChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 2),
    _CsuChannelBandwidth_Type()
)
csuChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuChannelBandwidth.setStatus("mandatory")


class _CsuDataInversion_Type(Integer32):
    """Custom type csuDataInversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csuAutoInverted", 3),
          ("csuInverted", 2),
          ("csuNotInverted", 1))
    )


_CsuDataInversion_Type.__name__ = "Integer32"
_CsuDataInversion_Object = MibTableColumn
csuDataInversion = _CsuDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 3),
    _CsuDataInversion_Type()
)
csuDataInversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuDataInversion.setStatus("mandatory")


class _CsuDataCoding_Type(Integer32):
    """Custom type csuDataCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuNRZ", 1),
          ("csuNRZI", 2))
    )


_CsuDataCoding_Type.__name__ = "Integer32"
_CsuDataCoding_Object = MibTableColumn
csuDataCoding = _CsuDataCoding_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 4),
    _CsuDataCoding_Type()
)
csuDataCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuDataCoding.setStatus("mandatory")


class _CsuTimingMode_Type(Integer32):
    """Custom type csuTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuLoopTiming", 2),
          ("csuNetworkTiming", 1))
    )


_CsuTimingMode_Type.__name__ = "Integer32"
_CsuTimingMode_Object = MibTableColumn
csuTimingMode = _CsuTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 5),
    _CsuTimingMode_Type()
)
csuTimingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuTimingMode.setStatus("mandatory")


class _CsuLineBuildOut_Type(Integer32):
    """Custom type csuLineBuildOut based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("csu0DB", 1),
          ("csu0to133", 5),
          ("csu133to266", 6),
          ("csu15DB", 3),
          ("csu225DB", 4),
          ("csu266to399", 7),
          ("csu399to533", 8),
          ("csu533to655", 9),
          ("csu75DB", 2))
    )


_CsuLineBuildOut_Type.__name__ = "Integer32"
_CsuLineBuildOut_Object = MibTableColumn
csuLineBuildOut = _CsuLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 6),
    _CsuLineBuildOut_Type()
)
csuLineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuLineBuildOut.setStatus("mandatory")


class _CsuLineCode_Type(Integer32):
    """Custom type csuLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csuAMI", 2),
          ("csuAutoLineCoding", 3),
          ("csuB8ZS", 1))
    )


_CsuLineCode_Type.__name__ = "Integer32"
_CsuLineCode_Object = MibTableColumn
csuLineCode = _CsuLineCode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 7),
    _CsuLineCode_Type()
)
csuLineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuLineCode.setStatus("mandatory")


class _CsuPulseDensityEnforcer_Type(Integer32):
    """Custom type csuPulseDensityEnforcer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuPDEnforceOFF", 1),
          ("csuPDEnforceON", 2))
    )


_CsuPulseDensityEnforcer_Type.__name__ = "Integer32"
_CsuPulseDensityEnforcer_Object = MibTableColumn
csuPulseDensityEnforcer = _CsuPulseDensityEnforcer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 8),
    _CsuPulseDensityEnforcer_Type()
)
csuPulseDensityEnforcer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuPulseDensityEnforcer.setStatus("mandatory")


class _CsuFramingFormat_Type(Integer32):
    """Custom type csuFramingFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csuAutoFraming", 3),
          ("csuD4", 2),
          ("csuESF", 1))
    )


_CsuFramingFormat_Type.__name__ = "Integer32"
_CsuFramingFormat_Object = MibTableColumn
csuFramingFormat = _CsuFramingFormat_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 9),
    _CsuFramingFormat_Type()
)
csuFramingFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFramingFormat.setStatus("mandatory")


class _CsuJapaneseCRC6_Type(Integer32):
    """Custom type csuJapaneseCRC6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csuAutoBandwidth", 3),
          ("csuJapanCRCDisable", 1),
          ("csuJapanCRCEnable", 2))
    )


_CsuJapaneseCRC6_Type.__name__ = "Integer32"
_CsuJapaneseCRC6_Object = MibTableColumn
csuJapaneseCRC6 = _CsuJapaneseCRC6_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 10),
    _CsuJapaneseCRC6_Type()
)
csuJapaneseCRC6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuJapaneseCRC6.setStatus("mandatory")


class _CsuReceiverSensitivity_Type(Integer32):
    """Custom type csuReceiverSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuSensitivityExtended", 1),
          ("csuSensitivityNormal", 2))
    )


_CsuReceiverSensitivity_Type.__name__ = "Integer32"
_CsuReceiverSensitivity_Object = MibTableColumn
csuReceiverSensitivity = _CsuReceiverSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 11),
    _CsuReceiverSensitivity_Type()
)
csuReceiverSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuReceiverSensitivity.setStatus("mandatory")


class _CsuFDLidleCode_Type(Integer32):
    """Custom type csuFDLidleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuFDLIdleIsFlags", 1),
          ("csuFdlIdleIsIdles", 2))
    )


_CsuFDLidleCode_Type.__name__ = "Integer32"
_CsuFDLidleCode_Object = MibTableColumn
csuFDLidleCode = _CsuFDLidleCode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 12),
    _CsuFDLidleCode_Type()
)
csuFDLidleCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFDLidleCode.setStatus("mandatory")


class _CsuANSIPRMEnable_Type(Integer32):
    """Custom type csuANSIPRMEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuANSIPRMDisabled", 2),
          ("csuANSIPRMEnabled", 1))
    )


_CsuANSIPRMEnable_Type.__name__ = "Integer32"
_CsuANSIPRMEnable_Object = MibTableColumn
csuANSIPRMEnable = _CsuANSIPRMEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 13),
    _CsuANSIPRMEnable_Type()
)
csuANSIPRMEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuANSIPRMEnable.setStatus("mandatory")


class _CsuANSIPRMaddress_Type(Integer32):
    """Custom type csuANSIPRMaddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuANSIPrm0x38", 1),
          ("csuANSIPrm0x3a", 2))
    )


_CsuANSIPRMaddress_Type.__name__ = "Integer32"
_CsuANSIPRMaddress_Object = MibTableColumn
csuANSIPRMaddress = _CsuANSIPRMaddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 14),
    _CsuANSIPRMaddress_Type()
)
csuANSIPRMaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuANSIPRMaddress.setStatus("mandatory")


class _CsuATTresponseEnable_Type(Integer32):
    """Custom type csuATTresponseEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuATTResponseDisabled", 2),
          ("csuATTResponseEnabled", 1))
    )


_CsuATTresponseEnable_Type.__name__ = "Integer32"
_CsuATTresponseEnable_Object = MibTableColumn
csuATTresponseEnable = _CsuATTresponseEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 15),
    _CsuATTresponseEnable_Type()
)
csuATTresponseEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuATTresponseEnable.setStatus("mandatory")


class _CsuATTresponseaddress_Type(Integer32):
    """Custom type csuATTresponseaddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csuATTResponseBoth", 1),
          ("csuATTResponseCSU", 2),
          ("csuATTResponseDSU", 3))
    )


_CsuATTresponseaddress_Type.__name__ = "Integer32"
_CsuATTresponseaddress_Object = MibTableColumn
csuATTresponseaddress = _CsuATTresponseaddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 16),
    _CsuATTresponseaddress_Type()
)
csuATTresponseaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuATTresponseaddress.setStatus("mandatory")


class _CsuAllocatedChannelMap_Type(DisplayString):
    """Custom type csuAllocatedChannelMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsuAllocatedChannelMap_Type.__name__ = "DisplayString"
_CsuAllocatedChannelMap_Object = MibTableColumn
csuAllocatedChannelMap = _CsuAllocatedChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 2, 1, 17),
    _CsuAllocatedChannelMap_Type()
)
csuAllocatedChannelMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuAllocatedChannelMap.setStatus("mandatory")
_CsuFracTable_Object = MibTable
csuFracTable = _CsuFracTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 3)
)
if mibBuilder.loadTexts:
    csuFracTable.setStatus("mandatory")
_CsuFracEntry_Object = MibTableRow
csuFracEntry = _CsuFracEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 3, 1)
)
csuFracEntry.setIndexNames(
    (0, "INTEL-CSU-HW-MIB", "csuFracLineIndex"),
    (0, "INTEL-CSU-HW-MIB", "csuFracNumber"),
)
if mibBuilder.loadTexts:
    csuFracEntry.setStatus("mandatory")


class _CsuFracLineIndex_Type(Integer32):
    """Custom type csuFracLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CsuFracLineIndex_Type.__name__ = "Integer32"
_CsuFracLineIndex_Object = MibTableColumn
csuFracLineIndex = _CsuFracLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 3, 1, 1),
    _CsuFracLineIndex_Type()
)
csuFracLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFracLineIndex.setStatus("mandatory")


class _CsuFracNumber_Type(Integer32):
    """Custom type csuFracNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CsuFracNumber_Type.__name__ = "Integer32"
_CsuFracNumber_Object = MibTableColumn
csuFracNumber = _CsuFracNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 3, 1, 2),
    _CsuFracNumber_Type()
)
csuFracNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFracNumber.setStatus("mandatory")


class _CsuFracInUse_Type(Integer32):
    """Custom type csuFracInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuChannelInUse", 1),
          ("csuChannelNotInUse", 2))
    )


_CsuFracInUse_Type.__name__ = "Integer32"
_CsuFracInUse_Object = MibTableColumn
csuFracInUse = _CsuFracInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 3, 1, 3),
    _CsuFracInUse_Type()
)
csuFracInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFracInUse.setStatus("mandatory")


class _CsuFracDetected_Type(Integer32):
    """Custom type csuFracDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csuChannelInUse", 1),
          ("csuChannelNotInUse", 2),
          ("csuChannelUnknown", 3))
    )


_CsuFracDetected_Type.__name__ = "Integer32"
_CsuFracDetected_Object = MibTableColumn
csuFracDetected = _CsuFracDetected_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 36, 1, 3, 1, 4),
    _CsuFracDetected_Type()
)
csuFracDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFracDetected.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-CSU-HW-MIB",
    **{"csudsu": csudsu,
       "csu": csu,
       "csuInfoTable": csuInfoTable,
       "csuInfoEntry": csuInfoEntry,
       "csuInfoLineIndex": csuInfoLineIndex,
       "csuAlarm": csuAlarm,
       "csuReceiveLevel": csuReceiveLevel,
       "csuLoopbackState": csuLoopbackState,
       "csuLossofsynchronization": csuLossofsynchronization,
       "csuChangeofFrameAlignment": csuChangeofFrameAlignment,
       "csuEightZeroDetect": csuEightZeroDetect,
       "csuSixteenZeroDetect": csuSixteenZeroDetect,
       "csuSeverelyErroredFramingEvent": csuSeverelyErroredFramingEvent,
       "csuB8ZSCodeWordDetect": csuB8ZSCodeWordDetect,
       "csuFrameBitError": csuFrameBitError,
       "csuReceivePulseDensityViolation": csuReceivePulseDensityViolation,
       "csuTransmitPulseDensityViolation": csuTransmitPulseDensityViolation,
       "csuJitterAttenuatorLimitTrip": csuJitterAttenuatorLimitTrip,
       "csuLossofReceiveClock": csuLossofReceiveClock,
       "csuFramerReceiveCarrierLoss": csuFramerReceiveCarrierLoss,
       "csuLineCodeViolationCount": csuLineCodeViolationCount,
       "csuPathCodeViolationCount": csuPathCodeViolationCount,
       "csuMultiframesOutofSyncCount": csuMultiframesOutofSyncCount,
       "csuCRC6errors": csuCRC6errors,
       "csuErrorRate": csuErrorRate,
       "csuLinkState": csuLinkState,
       "csuErrorsThisSecond": csuErrorsThisSecond,
       "csuPercentEFS": csuPercentEFS,
       "csuTXChannelPayload": csuTXChannelPayload,
       "csuRXChannelPayload": csuRXChannelPayload,
       "csuDetectedChannelMap": csuDetectedChannelMap,
       "csuYellowAlarmCount": csuYellowAlarmCount,
       "csuAISDefects": csuAISDefects,
       "csuConfigTable": csuConfigTable,
       "csuConfigEntry": csuConfigEntry,
       "csuConfigLineIndex": csuConfigLineIndex,
       "csuChannelBandwidth": csuChannelBandwidth,
       "csuDataInversion": csuDataInversion,
       "csuDataCoding": csuDataCoding,
       "csuTimingMode": csuTimingMode,
       "csuLineBuildOut": csuLineBuildOut,
       "csuLineCode": csuLineCode,
       "csuPulseDensityEnforcer": csuPulseDensityEnforcer,
       "csuFramingFormat": csuFramingFormat,
       "csuJapaneseCRC6": csuJapaneseCRC6,
       "csuReceiverSensitivity": csuReceiverSensitivity,
       "csuFDLidleCode": csuFDLidleCode,
       "csuANSIPRMEnable": csuANSIPRMEnable,
       "csuANSIPRMaddress": csuANSIPRMaddress,
       "csuATTresponseEnable": csuATTresponseEnable,
       "csuATTresponseaddress": csuATTresponseaddress,
       "csuAllocatedChannelMap": csuAllocatedChannelMap,
       "csuFracTable": csuFracTable,
       "csuFracEntry": csuFracEntry,
       "csuFracLineIndex": csuFracLineIndex,
       "csuFracNumber": csuFracNumber,
       "csuFracInUse": csuFracInUse,
       "csuFracDetected": csuFracDetected}
)
