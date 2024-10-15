# SNMP MIB module (ADTRAN-AOS-VQM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-VQM
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:15 2024
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

(adGenAOSConformance,
 adGenAOSVoice) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSVoice")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenAOSVQMMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MOSvalue(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
        ValueRangeConstraint(65535, 65535),
    )



class Percentage(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
        ValueRangeConstraint(65535, 65535),
    )



class MsecValue(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_AdVQM_ObjectIdentity = ObjectIdentity
adVQM = _AdVQM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3)
)
_AdVQMTrap_ObjectIdentity = ObjectIdentity
adVQMTrap = _AdVQMTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 0)
)
_AdVQMTrapControl_ObjectIdentity = ObjectIdentity
adVQMTrapControl = _AdVQMTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 1)
)


class _AdVqmTrapState_Type(Integer32):
    """Custom type adVqmTrapState based on Integer32"""
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


_AdVqmTrapState_Type.__name__ = "Integer32"
_AdVqmTrapState_Object = MibScalar
adVqmTrapState = _AdVqmTrapState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 1, 1),
    _AdVqmTrapState_Type()
)
adVqmTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adVqmTrapState.setStatus("current")


class _AdVqmTrapCfgSeverityLevel_Type(Integer32):
    """Custom type adVqmTrapCfgSeverityLevel based on Integer32"""
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
        *(("error", 1),
          ("info", 4),
          ("notice", 3),
          ("warning", 2))
    )


_AdVqmTrapCfgSeverityLevel_Type.__name__ = "Integer32"
_AdVqmTrapCfgSeverityLevel_Object = MibScalar
adVqmTrapCfgSeverityLevel = _AdVqmTrapCfgSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 1, 2),
    _AdVqmTrapCfgSeverityLevel_Type()
)
adVqmTrapCfgSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adVqmTrapCfgSeverityLevel.setStatus("current")


class _AdVqmTrapEventType_Type(Bits):
    """Custom type adVqmTrapEventType based on Bits"""
    namedValues = NamedValues(
        *(("jitter", 4),
          ("lQMos", 0),
          ("loss", 2),
          ("outOfOrder", 3),
          ("pQMos", 1))
    )

_AdVqmTrapEventType_Type.__name__ = "Bits"
_AdVqmTrapEventType_Object = MibScalar
adVqmTrapEventType = _AdVqmTrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 1, 3),
    _AdVqmTrapEventType_Type()
)
adVqmTrapEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmTrapEventType.setStatus("current")
_AdVQMCfg_ObjectIdentity = ObjectIdentity
adVQMCfg = _AdVQMCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2)
)


class _AdVqmCfgEnable_Type(Integer32):
    """Custom type adVqmCfgEnable based on Integer32"""
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


_AdVqmCfgEnable_Type.__name__ = "Integer32"
_AdVqmCfgEnable_Object = MibScalar
adVqmCfgEnable = _AdVqmCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 1),
    _AdVqmCfgEnable_Type()
)
adVqmCfgEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgEnable.setStatus("current")


class _AdVqmCfgSipEnable_Type(Integer32):
    """Custom type adVqmCfgSipEnable based on Integer32"""
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


_AdVqmCfgSipEnable_Type.__name__ = "Integer32"
_AdVqmCfgSipEnable_Object = MibScalar
adVqmCfgSipEnable = _AdVqmCfgSipEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 2),
    _AdVqmCfgSipEnable_Type()
)
adVqmCfgSipEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgSipEnable.setStatus("current")


class _AdVqmCfgUdpEnable_Type(Integer32):
    """Custom type adVqmCfgUdpEnable based on Integer32"""
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


_AdVqmCfgUdpEnable_Type.__name__ = "Integer32"
_AdVqmCfgUdpEnable_Object = MibScalar
adVqmCfgUdpEnable = _AdVqmCfgUdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 3),
    _AdVqmCfgUdpEnable_Type()
)
adVqmCfgUdpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgUdpEnable.setStatus("current")


class _AdVqmCfgInternationalCode_Type(Integer32):
    """Custom type adVqmCfgInternationalCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("japan", 5),
          ("none", 1))
    )


_AdVqmCfgInternationalCode_Type.__name__ = "Integer32"
_AdVqmCfgInternationalCode_Object = MibScalar
adVqmCfgInternationalCode = _AdVqmCfgInternationalCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 4),
    _AdVqmCfgInternationalCode_Type()
)
adVqmCfgInternationalCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgInternationalCode.setStatus("current")


class _AdVqmCfgJitterBufferType_Type(Integer32):
    """Custom type adVqmCfgJitterBufferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("jitterBufferAdaptive", 2),
          ("jitterBufferFixed", 1),
          ("jitterBufferUnknown", 3))
    )


_AdVqmCfgJitterBufferType_Type.__name__ = "Integer32"
_AdVqmCfgJitterBufferType_Object = MibScalar
adVqmCfgJitterBufferType = _AdVqmCfgJitterBufferType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 5),
    _AdVqmCfgJitterBufferType_Type()
)
adVqmCfgJitterBufferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgJitterBufferType.setStatus("current")
_AdVqmCfgJitterBufferAdaptiveMin_Type = Unsigned32
_AdVqmCfgJitterBufferAdaptiveMin_Object = MibScalar
adVqmCfgJitterBufferAdaptiveMin = _AdVqmCfgJitterBufferAdaptiveMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 6),
    _AdVqmCfgJitterBufferAdaptiveMin_Type()
)
adVqmCfgJitterBufferAdaptiveMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgJitterBufferAdaptiveMin.setStatus("current")
_AdVqmCfgJitterBufferAdaptiveNominal_Type = Unsigned32
_AdVqmCfgJitterBufferAdaptiveNominal_Object = MibScalar
adVqmCfgJitterBufferAdaptiveNominal = _AdVqmCfgJitterBufferAdaptiveNominal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 7),
    _AdVqmCfgJitterBufferAdaptiveNominal_Type()
)
adVqmCfgJitterBufferAdaptiveNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgJitterBufferAdaptiveNominal.setStatus("current")
_AdVqmCfgJitterBufferAdaptiveMax_Type = Unsigned32
_AdVqmCfgJitterBufferAdaptiveMax_Object = MibScalar
adVqmCfgJitterBufferAdaptiveMax = _AdVqmCfgJitterBufferAdaptiveMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 8),
    _AdVqmCfgJitterBufferAdaptiveMax_Type()
)
adVqmCfgJitterBufferAdaptiveMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgJitterBufferAdaptiveMax.setStatus("current")
_AdVqmCfgJitterBufferFixedNominal_Type = Unsigned32
_AdVqmCfgJitterBufferFixedNominal_Object = MibScalar
adVqmCfgJitterBufferFixedNominal = _AdVqmCfgJitterBufferFixedNominal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 9),
    _AdVqmCfgJitterBufferFixedNominal_Type()
)
adVqmCfgJitterBufferFixedNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgJitterBufferFixedNominal.setStatus("current")
_AdVqmCfgJitterBufferFixedSize_Type = Unsigned32
_AdVqmCfgJitterBufferFixedSize_Object = MibScalar
adVqmCfgJitterBufferFixedSize = _AdVqmCfgJitterBufferFixedSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 10),
    _AdVqmCfgJitterBufferFixedSize_Type()
)
adVqmCfgJitterBufferFixedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgJitterBufferFixedSize.setStatus("current")
_AdVqmCfgJitterBufferThresholdEarlyMs_Type = Unsigned32
_AdVqmCfgJitterBufferThresholdEarlyMs_Object = MibScalar
adVqmCfgJitterBufferThresholdEarlyMs = _AdVqmCfgJitterBufferThresholdEarlyMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 11),
    _AdVqmCfgJitterBufferThresholdEarlyMs_Type()
)
adVqmCfgJitterBufferThresholdEarlyMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgJitterBufferThresholdEarlyMs.setStatus("current")
_AdVqmCfgJitterBufferThresholdLateMs_Type = Unsigned32
_AdVqmCfgJitterBufferThresholdLateMs_Object = MibScalar
adVqmCfgJitterBufferThresholdLateMs = _AdVqmCfgJitterBufferThresholdLateMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 12),
    _AdVqmCfgJitterBufferThresholdLateMs_Type()
)
adVqmCfgJitterBufferThresholdLateMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgJitterBufferThresholdLateMs.setStatus("current")


class _AdVqmCfgRoundTripPingEnabled_Type(Integer32):
    """Custom type adVqmCfgRoundTripPingEnabled based on Integer32"""
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


_AdVqmCfgRoundTripPingEnabled_Type.__name__ = "Integer32"
_AdVqmCfgRoundTripPingEnabled_Object = MibScalar
adVqmCfgRoundTripPingEnabled = _AdVqmCfgRoundTripPingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 13),
    _AdVqmCfgRoundTripPingEnabled_Type()
)
adVqmCfgRoundTripPingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgRoundTripPingEnabled.setStatus("current")


class _AdVqmCfgRoundTripPingType_Type(Integer32):
    """Custom type adVqmCfgRoundTripPingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ping", 1),
          ("timestamp", 2))
    )


_AdVqmCfgRoundTripPingType_Type.__name__ = "Integer32"
_AdVqmCfgRoundTripPingType_Object = MibScalar
adVqmCfgRoundTripPingType = _AdVqmCfgRoundTripPingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 14),
    _AdVqmCfgRoundTripPingType_Type()
)
adVqmCfgRoundTripPingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgRoundTripPingType.setStatus("current")
_AdVqmCfgCallHistorySize_Type = Unsigned32
_AdVqmCfgCallHistorySize_Object = MibScalar
adVqmCfgCallHistorySize = _AdVqmCfgCallHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 15),
    _AdVqmCfgCallHistorySize_Type()
)
adVqmCfgCallHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgCallHistorySize.setStatus("current")
_AdVqmCfgHistoryThresholdLqmos_Type = MOSvalue
_AdVqmCfgHistoryThresholdLqmos_Object = MibScalar
adVqmCfgHistoryThresholdLqmos = _AdVqmCfgHistoryThresholdLqmos_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 16),
    _AdVqmCfgHistoryThresholdLqmos_Type()
)
adVqmCfgHistoryThresholdLqmos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgHistoryThresholdLqmos.setStatus("current")
_AdVqmCfgHistoryThresholdCqmos_Type = MOSvalue
_AdVqmCfgHistoryThresholdCqmos_Object = MibScalar
adVqmCfgHistoryThresholdCqmos = _AdVqmCfgHistoryThresholdCqmos_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 17),
    _AdVqmCfgHistoryThresholdCqmos_Type()
)
adVqmCfgHistoryThresholdCqmos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgHistoryThresholdCqmos.setStatus("current")
_AdVqmCfgHistoryThresholdPqmos_Type = MOSvalue
_AdVqmCfgHistoryThresholdPqmos_Object = MibScalar
adVqmCfgHistoryThresholdPqmos = _AdVqmCfgHistoryThresholdPqmos_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 18),
    _AdVqmCfgHistoryThresholdPqmos_Type()
)
adVqmCfgHistoryThresholdPqmos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgHistoryThresholdPqmos.setStatus("current")
_AdVqmCfgHistoryThresholdLoss_Type = Unsigned32
_AdVqmCfgHistoryThresholdLoss_Object = MibScalar
adVqmCfgHistoryThresholdLoss = _AdVqmCfgHistoryThresholdLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 19),
    _AdVqmCfgHistoryThresholdLoss_Type()
)
adVqmCfgHistoryThresholdLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgHistoryThresholdLoss.setStatus("current")
_AdVqmCfgHistoryThresholdOutOfOrder_Type = Unsigned32
_AdVqmCfgHistoryThresholdOutOfOrder_Object = MibScalar
adVqmCfgHistoryThresholdOutOfOrder = _AdVqmCfgHistoryThresholdOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 20),
    _AdVqmCfgHistoryThresholdOutOfOrder_Type()
)
adVqmCfgHistoryThresholdOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgHistoryThresholdOutOfOrder.setStatus("current")
_AdVqmCfgHistoryThresholdJitter_Type = Unsigned32
_AdVqmCfgHistoryThresholdJitter_Object = MibScalar
adVqmCfgHistoryThresholdJitter = _AdVqmCfgHistoryThresholdJitter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 21),
    _AdVqmCfgHistoryThresholdJitter_Type()
)
adVqmCfgHistoryThresholdJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCfgHistoryThresholdJitter.setStatus("current")


class _AdVqmCfgClear_Type(Integer32):
    """Custom type adVqmCfgClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdVqmCfgClear_Type.__name__ = "Integer32"
_AdVqmCfgClear_Object = MibScalar
adVqmCfgClear = _AdVqmCfgClear_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 22),
    _AdVqmCfgClear_Type()
)
adVqmCfgClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adVqmCfgClear.setStatus("current")


class _AdVqmCfgClearCallHistory_Type(Integer32):
    """Custom type adVqmCfgClearCallHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdVqmCfgClearCallHistory_Type.__name__ = "Integer32"
_AdVqmCfgClearCallHistory_Object = MibScalar
adVqmCfgClearCallHistory = _AdVqmCfgClearCallHistory_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 2, 23),
    _AdVqmCfgClearCallHistory_Type()
)
adVqmCfgClearCallHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adVqmCfgClearCallHistory.setStatus("current")
_AdVQMThreshold_ObjectIdentity = ObjectIdentity
adVQMThreshold = _AdVQMThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3)
)
_AdVqmThresholdLqmosInfo_Type = MOSvalue
_AdVqmThresholdLqmosInfo_Object = MibScalar
adVqmThresholdLqmosInfo = _AdVqmThresholdLqmosInfo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 1),
    _AdVqmThresholdLqmosInfo_Type()
)
adVqmThresholdLqmosInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdLqmosInfo.setStatus("current")
_AdVqmThresholdLqmosNotice_Type = MOSvalue
_AdVqmThresholdLqmosNotice_Object = MibScalar
adVqmThresholdLqmosNotice = _AdVqmThresholdLqmosNotice_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 2),
    _AdVqmThresholdLqmosNotice_Type()
)
adVqmThresholdLqmosNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdLqmosNotice.setStatus("current")
_AdVqmThresholdLqmosWarning_Type = MOSvalue
_AdVqmThresholdLqmosWarning_Object = MibScalar
adVqmThresholdLqmosWarning = _AdVqmThresholdLqmosWarning_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 3),
    _AdVqmThresholdLqmosWarning_Type()
)
adVqmThresholdLqmosWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdLqmosWarning.setStatus("current")
_AdVqmThresholdLqmosError_Type = MOSvalue
_AdVqmThresholdLqmosError_Object = MibScalar
adVqmThresholdLqmosError = _AdVqmThresholdLqmosError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 4),
    _AdVqmThresholdLqmosError_Type()
)
adVqmThresholdLqmosError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdLqmosError.setStatus("current")
_AdVqmThresholdPqmosInfo_Type = MOSvalue
_AdVqmThresholdPqmosInfo_Object = MibScalar
adVqmThresholdPqmosInfo = _AdVqmThresholdPqmosInfo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 5),
    _AdVqmThresholdPqmosInfo_Type()
)
adVqmThresholdPqmosInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdPqmosInfo.setStatus("current")
_AdVqmThresholdPqmosNotice_Type = MOSvalue
_AdVqmThresholdPqmosNotice_Object = MibScalar
adVqmThresholdPqmosNotice = _AdVqmThresholdPqmosNotice_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 6),
    _AdVqmThresholdPqmosNotice_Type()
)
adVqmThresholdPqmosNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdPqmosNotice.setStatus("current")
_AdVqmThresholdPqmosWarning_Type = MOSvalue
_AdVqmThresholdPqmosWarning_Object = MibScalar
adVqmThresholdPqmosWarning = _AdVqmThresholdPqmosWarning_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 7),
    _AdVqmThresholdPqmosWarning_Type()
)
adVqmThresholdPqmosWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdPqmosWarning.setStatus("current")
_AdVqmThresholdPqmosError_Type = MOSvalue
_AdVqmThresholdPqmosError_Object = MibScalar
adVqmThresholdPqmosError = _AdVqmThresholdPqmosError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 8),
    _AdVqmThresholdPqmosError_Type()
)
adVqmThresholdPqmosError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdPqmosError.setStatus("current")
_AdVqmThresholdOutOfOrderInfo_Type = Unsigned32
_AdVqmThresholdOutOfOrderInfo_Object = MibScalar
adVqmThresholdOutOfOrderInfo = _AdVqmThresholdOutOfOrderInfo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 9),
    _AdVqmThresholdOutOfOrderInfo_Type()
)
adVqmThresholdOutOfOrderInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdOutOfOrderInfo.setStatus("current")
_AdVqmThresholdOutOfOrderNotice_Type = Unsigned32
_AdVqmThresholdOutOfOrderNotice_Object = MibScalar
adVqmThresholdOutOfOrderNotice = _AdVqmThresholdOutOfOrderNotice_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 10),
    _AdVqmThresholdOutOfOrderNotice_Type()
)
adVqmThresholdOutOfOrderNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdOutOfOrderNotice.setStatus("current")
_AdVqmThresholdOutOfOrderWarning_Type = Unsigned32
_AdVqmThresholdOutOfOrderWarning_Object = MibScalar
adVqmThresholdOutOfOrderWarning = _AdVqmThresholdOutOfOrderWarning_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 11),
    _AdVqmThresholdOutOfOrderWarning_Type()
)
adVqmThresholdOutOfOrderWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdOutOfOrderWarning.setStatus("current")
_AdVqmThresholdOutOfOrderError_Type = Unsigned32
_AdVqmThresholdOutOfOrderError_Object = MibScalar
adVqmThresholdOutOfOrderError = _AdVqmThresholdOutOfOrderError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 12),
    _AdVqmThresholdOutOfOrderError_Type()
)
adVqmThresholdOutOfOrderError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdOutOfOrderError.setStatus("current")
_AdVqmThresholdLossInfo_Type = Unsigned32
_AdVqmThresholdLossInfo_Object = MibScalar
adVqmThresholdLossInfo = _AdVqmThresholdLossInfo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 13),
    _AdVqmThresholdLossInfo_Type()
)
adVqmThresholdLossInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdLossInfo.setStatus("current")
_AdVqmThresholdLossNotice_Type = Unsigned32
_AdVqmThresholdLossNotice_Object = MibScalar
adVqmThresholdLossNotice = _AdVqmThresholdLossNotice_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 14),
    _AdVqmThresholdLossNotice_Type()
)
adVqmThresholdLossNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdLossNotice.setStatus("current")
_AdVqmThresholdLossWarning_Type = Unsigned32
_AdVqmThresholdLossWarning_Object = MibScalar
adVqmThresholdLossWarning = _AdVqmThresholdLossWarning_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 15),
    _AdVqmThresholdLossWarning_Type()
)
adVqmThresholdLossWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdLossWarning.setStatus("current")
_AdVqmThresholdLossError_Type = Unsigned32
_AdVqmThresholdLossError_Object = MibScalar
adVqmThresholdLossError = _AdVqmThresholdLossError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 16),
    _AdVqmThresholdLossError_Type()
)
adVqmThresholdLossError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdLossError.setStatus("current")
_AdVqmThresholdJitterInfo_Type = Unsigned32
_AdVqmThresholdJitterInfo_Object = MibScalar
adVqmThresholdJitterInfo = _AdVqmThresholdJitterInfo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 17),
    _AdVqmThresholdJitterInfo_Type()
)
adVqmThresholdJitterInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdJitterInfo.setStatus("current")
_AdVqmThresholdJitterNotice_Type = Unsigned32
_AdVqmThresholdJitterNotice_Object = MibScalar
adVqmThresholdJitterNotice = _AdVqmThresholdJitterNotice_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 18),
    _AdVqmThresholdJitterNotice_Type()
)
adVqmThresholdJitterNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdJitterNotice.setStatus("current")
_AdVqmThresholdJitterWarning_Type = Unsigned32
_AdVqmThresholdJitterWarning_Object = MibScalar
adVqmThresholdJitterWarning = _AdVqmThresholdJitterWarning_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 19),
    _AdVqmThresholdJitterWarning_Type()
)
adVqmThresholdJitterWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdJitterWarning.setStatus("current")
_AdVqmThresholdJitterError_Type = Unsigned32
_AdVqmThresholdJitterError_Object = MibScalar
adVqmThresholdJitterError = _AdVqmThresholdJitterError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 3, 20),
    _AdVqmThresholdJitterError_Type()
)
adVqmThresholdJitterError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmThresholdJitterError.setStatus("current")
_AdVQMSysPerf_ObjectIdentity = ObjectIdentity
adVQMSysPerf = _AdVQMSysPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4)
)
_AdVqmSysActiveCalls_Type = Counter32
_AdVqmSysActiveCalls_Object = MibScalar
adVqmSysActiveCalls = _AdVqmSysActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 1),
    _AdVqmSysActiveCalls_Type()
)
adVqmSysActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysActiveCalls.setStatus("current")
_AdVqmSysActiveExcellent_Type = Counter32
_AdVqmSysActiveExcellent_Object = MibScalar
adVqmSysActiveExcellent = _AdVqmSysActiveExcellent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 2),
    _AdVqmSysActiveExcellent_Type()
)
adVqmSysActiveExcellent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysActiveExcellent.setStatus("current")
_AdVqmSysActiveGood_Type = Counter32
_AdVqmSysActiveGood_Object = MibScalar
adVqmSysActiveGood = _AdVqmSysActiveGood_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 3),
    _AdVqmSysActiveGood_Type()
)
adVqmSysActiveGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysActiveGood.setStatus("current")
_AdVqmSysActiveFair_Type = Counter32
_AdVqmSysActiveFair_Object = MibScalar
adVqmSysActiveFair = _AdVqmSysActiveFair_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 4),
    _AdVqmSysActiveFair_Type()
)
adVqmSysActiveFair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysActiveFair.setStatus("current")
_AdVqmSysActivePoor_Type = Counter32
_AdVqmSysActivePoor_Object = MibScalar
adVqmSysActivePoor = _AdVqmSysActivePoor_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 5),
    _AdVqmSysActivePoor_Type()
)
adVqmSysActivePoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysActivePoor.setStatus("current")
_AdVqmSysCallHistoryCalls_Type = Counter32
_AdVqmSysCallHistoryCalls_Object = MibScalar
adVqmSysCallHistoryCalls = _AdVqmSysCallHistoryCalls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 6),
    _AdVqmSysCallHistoryCalls_Type()
)
adVqmSysCallHistoryCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysCallHistoryCalls.setStatus("current")
_AdVqmSysCallHistoryExcellent_Type = Counter32
_AdVqmSysCallHistoryExcellent_Object = MibScalar
adVqmSysCallHistoryExcellent = _AdVqmSysCallHistoryExcellent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 7),
    _AdVqmSysCallHistoryExcellent_Type()
)
adVqmSysCallHistoryExcellent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysCallHistoryExcellent.setStatus("current")
_AdVqmSysCallHistoryGood_Type = Counter32
_AdVqmSysCallHistoryGood_Object = MibScalar
adVqmSysCallHistoryGood = _AdVqmSysCallHistoryGood_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 8),
    _AdVqmSysCallHistoryGood_Type()
)
adVqmSysCallHistoryGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysCallHistoryGood.setStatus("current")
_AdVqmSysCallHistoryFair_Type = Counter32
_AdVqmSysCallHistoryFair_Object = MibScalar
adVqmSysCallHistoryFair = _AdVqmSysCallHistoryFair_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 9),
    _AdVqmSysCallHistoryFair_Type()
)
adVqmSysCallHistoryFair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysCallHistoryFair.setStatus("current")
_AdVqmSysCallHistoryPoor_Type = Counter32
_AdVqmSysCallHistoryPoor_Object = MibScalar
adVqmSysCallHistoryPoor = _AdVqmSysCallHistoryPoor_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 10),
    _AdVqmSysCallHistoryPoor_Type()
)
adVqmSysCallHistoryPoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysCallHistoryPoor.setStatus("current")
_AdVqmSysAllCallsExcellent_Type = Counter32
_AdVqmSysAllCallsExcellent_Object = MibScalar
adVqmSysAllCallsExcellent = _AdVqmSysAllCallsExcellent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 11),
    _AdVqmSysAllCallsExcellent_Type()
)
adVqmSysAllCallsExcellent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysAllCallsExcellent.setStatus("current")
_AdVqmSysAllCallsGood_Type = Counter32
_AdVqmSysAllCallsGood_Object = MibScalar
adVqmSysAllCallsGood = _AdVqmSysAllCallsGood_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 12),
    _AdVqmSysAllCallsGood_Type()
)
adVqmSysAllCallsGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysAllCallsGood.setStatus("current")
_AdVqmSysAllCallsFair_Type = Counter32
_AdVqmSysAllCallsFair_Object = MibScalar
adVqmSysAllCallsFair = _AdVqmSysAllCallsFair_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 13),
    _AdVqmSysAllCallsFair_Type()
)
adVqmSysAllCallsFair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysAllCallsFair.setStatus("current")
_AdVqmSysAllCallsPoor_Type = Counter32
_AdVqmSysAllCallsPoor_Object = MibScalar
adVqmSysAllCallsPoor = _AdVqmSysAllCallsPoor_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 4, 14),
    _AdVqmSysAllCallsPoor_Type()
)
adVqmSysAllCallsPoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmSysAllCallsPoor.setStatus("current")
_AdVQMInterface_ObjectIdentity = ObjectIdentity
adVQMInterface = _AdVQMInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5)
)
_AdVQMInterfaceTable_Object = MibTable
adVQMInterfaceTable = _AdVQMInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1)
)
if mibBuilder.loadTexts:
    adVQMInterfaceTable.setStatus("current")
_AdVQMInterfaceEntry_Object = MibTableRow
adVQMInterfaceEntry = _AdVQMInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1)
)
adVQMInterfaceEntry.setIndexNames(
    (0, "ADTRAN-AOS-VQM", "adVqmIfcId"),
)
if mibBuilder.loadTexts:
    adVQMInterfaceEntry.setStatus("current")
_AdVqmIfcId_Type = Unsigned32
_AdVqmIfcId_Object = MibTableColumn
adVqmIfcId = _AdVqmIfcId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 1),
    _AdVqmIfcId_Type()
)
adVqmIfcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcId.setStatus("current")
_AdVqmIfcName_Type = DisplayString
_AdVqmIfcName_Object = MibTableColumn
adVqmIfcName = _AdVqmIfcName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 2),
    _AdVqmIfcName_Type()
)
adVqmIfcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcName.setStatus("current")
_AdVqmIfcPktsRx_Type = Counter64
_AdVqmIfcPktsRx_Object = MibTableColumn
adVqmIfcPktsRx = _AdVqmIfcPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 3),
    _AdVqmIfcPktsRx_Type()
)
adVqmIfcPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcPktsRx.setStatus("current")
_AdVqmIfcPktsLost_Type = Counter64
_AdVqmIfcPktsLost_Object = MibTableColumn
adVqmIfcPktsLost = _AdVqmIfcPktsLost_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 4),
    _AdVqmIfcPktsLost_Type()
)
adVqmIfcPktsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcPktsLost.setStatus("current")
_AdVqmIfcPktsOoo_Type = Counter64
_AdVqmIfcPktsOoo_Object = MibTableColumn
adVqmIfcPktsOoo = _AdVqmIfcPktsOoo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 5),
    _AdVqmIfcPktsOoo_Type()
)
adVqmIfcPktsOoo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcPktsOoo.setStatus("current")
_AdVqmIfcPktsDiscarded_Type = Counter64
_AdVqmIfcPktsDiscarded_Object = MibTableColumn
adVqmIfcPktsDiscarded = _AdVqmIfcPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 6),
    _AdVqmIfcPktsDiscarded_Type()
)
adVqmIfcPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcPktsDiscarded.setStatus("current")
_AdVqmIfcNumberActiveCalls_Type = Counter32
_AdVqmIfcNumberActiveCalls_Object = MibTableColumn
adVqmIfcNumberActiveCalls = _AdVqmIfcNumberActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 7),
    _AdVqmIfcNumberActiveCalls_Type()
)
adVqmIfcNumberActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcNumberActiveCalls.setStatus("current")
_AdVqmIfcTerminatedCalls_Type = Counter32
_AdVqmIfcTerminatedCalls_Object = MibTableColumn
adVqmIfcTerminatedCalls = _AdVqmIfcTerminatedCalls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 8),
    _AdVqmIfcTerminatedCalls_Type()
)
adVqmIfcTerminatedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcTerminatedCalls.setStatus("current")
_AdVqmIfcRLqMinimum_Type = Unsigned32
_AdVqmIfcRLqMinimum_Object = MibTableColumn
adVqmIfcRLqMinimum = _AdVqmIfcRLqMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 9),
    _AdVqmIfcRLqMinimum_Type()
)
adVqmIfcRLqMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcRLqMinimum.setStatus("current")
_AdVqmIfcRLqAverage_Type = Unsigned32
_AdVqmIfcRLqAverage_Object = MibTableColumn
adVqmIfcRLqAverage = _AdVqmIfcRLqAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 10),
    _AdVqmIfcRLqAverage_Type()
)
adVqmIfcRLqAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcRLqAverage.setStatus("current")
_AdVqmIfcRLqMaximum_Type = Unsigned32
_AdVqmIfcRLqMaximum_Object = MibTableColumn
adVqmIfcRLqMaximum = _AdVqmIfcRLqMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 11),
    _AdVqmIfcRLqMaximum_Type()
)
adVqmIfcRLqMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcRLqMaximum.setStatus("current")
_AdVqmIfcRCqMinimum_Type = Unsigned32
_AdVqmIfcRCqMinimum_Object = MibTableColumn
adVqmIfcRCqMinimum = _AdVqmIfcRCqMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 12),
    _AdVqmIfcRCqMinimum_Type()
)
adVqmIfcRCqMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcRCqMinimum.setStatus("current")
_AdVqmIfcRCqAverage_Type = Unsigned32
_AdVqmIfcRCqAverage_Object = MibTableColumn
adVqmIfcRCqAverage = _AdVqmIfcRCqAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 13),
    _AdVqmIfcRCqAverage_Type()
)
adVqmIfcRCqAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcRCqAverage.setStatus("current")
_AdVqmIfcRCqMaximum_Type = Unsigned32
_AdVqmIfcRCqMaximum_Object = MibTableColumn
adVqmIfcRCqMaximum = _AdVqmIfcRCqMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 14),
    _AdVqmIfcRCqMaximum_Type()
)
adVqmIfcRCqMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcRCqMaximum.setStatus("current")
_AdVqmIfcRG107Minimum_Type = Unsigned32
_AdVqmIfcRG107Minimum_Object = MibTableColumn
adVqmIfcRG107Minimum = _AdVqmIfcRG107Minimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 15),
    _AdVqmIfcRG107Minimum_Type()
)
adVqmIfcRG107Minimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcRG107Minimum.setStatus("current")
_AdVqmIfcRG107Average_Type = Unsigned32
_AdVqmIfcRG107Average_Object = MibTableColumn
adVqmIfcRG107Average = _AdVqmIfcRG107Average_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 16),
    _AdVqmIfcRG107Average_Type()
)
adVqmIfcRG107Average.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcRG107Average.setStatus("current")
_AdVqmIfcRG107Maximum_Type = Unsigned32
_AdVqmIfcRG107Maximum_Object = MibTableColumn
adVqmIfcRG107Maximum = _AdVqmIfcRG107Maximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 17),
    _AdVqmIfcRG107Maximum_Type()
)
adVqmIfcRG107Maximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcRG107Maximum.setStatus("current")
_AdVqmIfcMosLqMinimum_Type = MOSvalue
_AdVqmIfcMosLqMinimum_Object = MibTableColumn
adVqmIfcMosLqMinimum = _AdVqmIfcMosLqMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 18),
    _AdVqmIfcMosLqMinimum_Type()
)
adVqmIfcMosLqMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcMosLqMinimum.setStatus("current")
_AdVqmIfcMosLqAverage_Type = MOSvalue
_AdVqmIfcMosLqAverage_Object = MibTableColumn
adVqmIfcMosLqAverage = _AdVqmIfcMosLqAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 19),
    _AdVqmIfcMosLqAverage_Type()
)
adVqmIfcMosLqAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcMosLqAverage.setStatus("current")
_AdVqmIfcMosLqMaximum_Type = MOSvalue
_AdVqmIfcMosLqMaximum_Object = MibTableColumn
adVqmIfcMosLqMaximum = _AdVqmIfcMosLqMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 20),
    _AdVqmIfcMosLqMaximum_Type()
)
adVqmIfcMosLqMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcMosLqMaximum.setStatus("current")
_AdVqmIfcMosCqMinimum_Type = MOSvalue
_AdVqmIfcMosCqMinimum_Object = MibTableColumn
adVqmIfcMosCqMinimum = _AdVqmIfcMosCqMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 21),
    _AdVqmIfcMosCqMinimum_Type()
)
adVqmIfcMosCqMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcMosCqMinimum.setStatus("current")
_AdVqmIfcMosCqAverage_Type = MOSvalue
_AdVqmIfcMosCqAverage_Object = MibTableColumn
adVqmIfcMosCqAverage = _AdVqmIfcMosCqAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 22),
    _AdVqmIfcMosCqAverage_Type()
)
adVqmIfcMosCqAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcMosCqAverage.setStatus("current")
_AdVqmIfcMosCqMaximum_Type = MOSvalue
_AdVqmIfcMosCqMaximum_Object = MibTableColumn
adVqmIfcMosCqMaximum = _AdVqmIfcMosCqMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 23),
    _AdVqmIfcMosCqMaximum_Type()
)
adVqmIfcMosCqMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcMosCqMaximum.setStatus("current")
_AdVqmIfcMosPqMinimum_Type = MOSvalue
_AdVqmIfcMosPqMinimum_Object = MibTableColumn
adVqmIfcMosPqMinimum = _AdVqmIfcMosPqMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 24),
    _AdVqmIfcMosPqMinimum_Type()
)
adVqmIfcMosPqMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcMosPqMinimum.setStatus("current")
_AdVqmIfcMosPqAverage_Type = MOSvalue
_AdVqmIfcMosPqAverage_Object = MibTableColumn
adVqmIfcMosPqAverage = _AdVqmIfcMosPqAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 25),
    _AdVqmIfcMosPqAverage_Type()
)
adVqmIfcMosPqAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcMosPqAverage.setStatus("current")
_AdVqmIfcMosPqMaximum_Type = MOSvalue
_AdVqmIfcMosPqMaximum_Object = MibTableColumn
adVqmIfcMosPqMaximum = _AdVqmIfcMosPqMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 26),
    _AdVqmIfcMosPqMaximum_Type()
)
adVqmIfcMosPqMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcMosPqMaximum.setStatus("current")
_AdVqmIfcLossMinimum_Type = Unsigned32
_AdVqmIfcLossMinimum_Object = MibTableColumn
adVqmIfcLossMinimum = _AdVqmIfcLossMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 27),
    _AdVqmIfcLossMinimum_Type()
)
adVqmIfcLossMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcLossMinimum.setStatus("current")
_AdVqmIfcLossAverage_Type = Unsigned32
_AdVqmIfcLossAverage_Object = MibTableColumn
adVqmIfcLossAverage = _AdVqmIfcLossAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 28),
    _AdVqmIfcLossAverage_Type()
)
adVqmIfcLossAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcLossAverage.setStatus("current")
_AdVqmIfcLossMaximum_Type = Unsigned32
_AdVqmIfcLossMaximum_Object = MibTableColumn
adVqmIfcLossMaximum = _AdVqmIfcLossMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 29),
    _AdVqmIfcLossMaximum_Type()
)
adVqmIfcLossMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcLossMaximum.setStatus("current")
_AdVqmIfcDiscardsMinimum_Type = Unsigned32
_AdVqmIfcDiscardsMinimum_Object = MibTableColumn
adVqmIfcDiscardsMinimum = _AdVqmIfcDiscardsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 30),
    _AdVqmIfcDiscardsMinimum_Type()
)
adVqmIfcDiscardsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcDiscardsMinimum.setStatus("current")
_AdVqmIfcDiscardsAverage_Type = Unsigned32
_AdVqmIfcDiscardsAverage_Object = MibTableColumn
adVqmIfcDiscardsAverage = _AdVqmIfcDiscardsAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 31),
    _AdVqmIfcDiscardsAverage_Type()
)
adVqmIfcDiscardsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcDiscardsAverage.setStatus("current")
_AdVqmIfcDiscardsMaximum_Type = Unsigned32
_AdVqmIfcDiscardsMaximum_Object = MibTableColumn
adVqmIfcDiscardsMaximum = _AdVqmIfcDiscardsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 32),
    _AdVqmIfcDiscardsMaximum_Type()
)
adVqmIfcDiscardsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcDiscardsMaximum.setStatus("current")
_AdVqmIfcPdvAverageMs_Type = Integer32
_AdVqmIfcPdvAverageMs_Object = MibTableColumn
adVqmIfcPdvAverageMs = _AdVqmIfcPdvAverageMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 33),
    _AdVqmIfcPdvAverageMs_Type()
)
adVqmIfcPdvAverageMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcPdvAverageMs.setStatus("current")
_AdVqmIfcPdvMaximumMs_Type = Integer32
_AdVqmIfcPdvMaximumMs_Object = MibTableColumn
adVqmIfcPdvMaximumMs = _AdVqmIfcPdvMaximumMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 34),
    _AdVqmIfcPdvMaximumMs_Type()
)
adVqmIfcPdvMaximumMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcPdvMaximumMs.setStatus("current")
_AdVqmIfcDelayMinMsec_Type = Unsigned32
_AdVqmIfcDelayMinMsec_Object = MibTableColumn
adVqmIfcDelayMinMsec = _AdVqmIfcDelayMinMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 35),
    _AdVqmIfcDelayMinMsec_Type()
)
adVqmIfcDelayMinMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcDelayMinMsec.setStatus("current")
_AdVqmIfcDelayAvgMsec_Type = Unsigned32
_AdVqmIfcDelayAvgMsec_Object = MibTableColumn
adVqmIfcDelayAvgMsec = _AdVqmIfcDelayAvgMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 36),
    _AdVqmIfcDelayAvgMsec_Type()
)
adVqmIfcDelayAvgMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcDelayAvgMsec.setStatus("current")
_AdVqmIfcDelayMaxMsec_Type = Unsigned32
_AdVqmIfcDelayMaxMsec_Object = MibTableColumn
adVqmIfcDelayMaxMsec = _AdVqmIfcDelayMaxMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 37),
    _AdVqmIfcDelayMaxMsec_Type()
)
adVqmIfcDelayMaxMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcDelayMaxMsec.setStatus("current")
_AdVqmIfcNumberStreamsExcellent_Type = Counter32
_AdVqmIfcNumberStreamsExcellent_Object = MibTableColumn
adVqmIfcNumberStreamsExcellent = _AdVqmIfcNumberStreamsExcellent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 38),
    _AdVqmIfcNumberStreamsExcellent_Type()
)
adVqmIfcNumberStreamsExcellent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcNumberStreamsExcellent.setStatus("current")
_AdVqmIfcNumberStreamsGood_Type = Counter32
_AdVqmIfcNumberStreamsGood_Object = MibTableColumn
adVqmIfcNumberStreamsGood = _AdVqmIfcNumberStreamsGood_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 39),
    _AdVqmIfcNumberStreamsGood_Type()
)
adVqmIfcNumberStreamsGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcNumberStreamsGood.setStatus("current")
_AdVqmIfcNumberStreamsFair_Type = Counter32
_AdVqmIfcNumberStreamsFair_Object = MibTableColumn
adVqmIfcNumberStreamsFair = _AdVqmIfcNumberStreamsFair_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 40),
    _AdVqmIfcNumberStreamsFair_Type()
)
adVqmIfcNumberStreamsFair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcNumberStreamsFair.setStatus("current")
_AdVqmIfcNumberStreamsPoor_Type = Counter32
_AdVqmIfcNumberStreamsPoor_Object = MibTableColumn
adVqmIfcNumberStreamsPoor = _AdVqmIfcNumberStreamsPoor_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 41),
    _AdVqmIfcNumberStreamsPoor_Type()
)
adVqmIfcNumberStreamsPoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmIfcNumberStreamsPoor.setStatus("current")


class _AdVqmIfcClear_Type(Integer32):
    """Custom type adVqmIfcClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdVqmIfcClear_Type.__name__ = "Integer32"
_AdVqmIfcClear_Object = MibTableColumn
adVqmIfcClear = _AdVqmIfcClear_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 5, 1, 1, 42),
    _AdVqmIfcClear_Type()
)
adVqmIfcClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adVqmIfcClear.setStatus("current")
_AdVQMEndPoint_ObjectIdentity = ObjectIdentity
adVQMEndPoint = _AdVQMEndPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6)
)
_AdVQMEndPointTable_Object = MibTable
adVQMEndPointTable = _AdVQMEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1)
)
if mibBuilder.loadTexts:
    adVQMEndPointTable.setStatus("current")
_AdVQMEndPointEntry_Object = MibTableRow
adVQMEndPointEntry = _AdVQMEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1)
)
adVQMEndPointEntry.setIndexNames(
    (0, "ADTRAN-AOS-VQM", "adVqmEndPointRtpSourceIp"),
)
if mibBuilder.loadTexts:
    adVQMEndPointEntry.setStatus("current")
_AdVqmEndPointRtpSourceIp_Type = IpAddress
_AdVqmEndPointRtpSourceIp_Object = MibTableColumn
adVqmEndPointRtpSourceIp = _AdVqmEndPointRtpSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 1),
    _AdVqmEndPointRtpSourceIp_Type()
)
adVqmEndPointRtpSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointRtpSourceIp.setStatus("current")
_AdVqmEndPointNumberCompletedCalls_Type = Counter32
_AdVqmEndPointNumberCompletedCalls_Object = MibTableColumn
adVqmEndPointNumberCompletedCalls = _AdVqmEndPointNumberCompletedCalls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 2),
    _AdVqmEndPointNumberCompletedCalls_Type()
)
adVqmEndPointNumberCompletedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointNumberCompletedCalls.setStatus("current")
_AdVqmEndPointInterfaceId_Type = Unsigned32
_AdVqmEndPointInterfaceId_Object = MibTableColumn
adVqmEndPointInterfaceId = _AdVqmEndPointInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 3),
    _AdVqmEndPointInterfaceId_Type()
)
adVqmEndPointInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointInterfaceId.setStatus("current")
_AdVqmEndPointInterfaceName_Type = DisplayString
_AdVqmEndPointInterfaceName_Object = MibTableColumn
adVqmEndPointInterfaceName = _AdVqmEndPointInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 4),
    _AdVqmEndPointInterfaceName_Type()
)
adVqmEndPointInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointInterfaceName.setStatus("current")
_AdVqmEndPointMosLqMinimum_Type = MOSvalue
_AdVqmEndPointMosLqMinimum_Object = MibTableColumn
adVqmEndPointMosLqMinimum = _AdVqmEndPointMosLqMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 5),
    _AdVqmEndPointMosLqMinimum_Type()
)
adVqmEndPointMosLqMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointMosLqMinimum.setStatus("current")
_AdVqmEndPointMosLqAverage_Type = MOSvalue
_AdVqmEndPointMosLqAverage_Object = MibTableColumn
adVqmEndPointMosLqAverage = _AdVqmEndPointMosLqAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 6),
    _AdVqmEndPointMosLqAverage_Type()
)
adVqmEndPointMosLqAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointMosLqAverage.setStatus("current")
_AdVqmEndPointMosLqMaximum_Type = MOSvalue
_AdVqmEndPointMosLqMaximum_Object = MibTableColumn
adVqmEndPointMosLqMaximum = _AdVqmEndPointMosLqMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 7),
    _AdVqmEndPointMosLqMaximum_Type()
)
adVqmEndPointMosLqMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointMosLqMaximum.setStatus("current")
_AdVqmEndPointMosPqMinimum_Type = MOSvalue
_AdVqmEndPointMosPqMinimum_Object = MibTableColumn
adVqmEndPointMosPqMinimum = _AdVqmEndPointMosPqMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 8),
    _AdVqmEndPointMosPqMinimum_Type()
)
adVqmEndPointMosPqMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointMosPqMinimum.setStatus("current")
_AdVqmEndPointMosPqAverage_Type = MOSvalue
_AdVqmEndPointMosPqAverage_Object = MibTableColumn
adVqmEndPointMosPqAverage = _AdVqmEndPointMosPqAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 9),
    _AdVqmEndPointMosPqAverage_Type()
)
adVqmEndPointMosPqAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointMosPqAverage.setStatus("current")
_AdVqmEndPointMosPqMaximum_Type = MOSvalue
_AdVqmEndPointMosPqMaximum_Object = MibTableColumn
adVqmEndPointMosPqMaximum = _AdVqmEndPointMosPqMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 10),
    _AdVqmEndPointMosPqMaximum_Type()
)
adVqmEndPointMosPqMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointMosPqMaximum.setStatus("current")
_AdVqmEndPointPktsLostTotal_Type = Counter32
_AdVqmEndPointPktsLostTotal_Object = MibTableColumn
adVqmEndPointPktsLostTotal = _AdVqmEndPointPktsLostTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 11),
    _AdVqmEndPointPktsLostTotal_Type()
)
adVqmEndPointPktsLostTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointPktsLostTotal.setStatus("current")
_AdVqmEndPointPktsOutOfOrder_Type = Counter32
_AdVqmEndPointPktsOutOfOrder_Object = MibTableColumn
adVqmEndPointPktsOutOfOrder = _AdVqmEndPointPktsOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 12),
    _AdVqmEndPointPktsOutOfOrder_Type()
)
adVqmEndPointPktsOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointPktsOutOfOrder.setStatus("current")
_AdVqmEndPointJitterMaximum_Type = Unsigned32
_AdVqmEndPointJitterMaximum_Object = MibTableColumn
adVqmEndPointJitterMaximum = _AdVqmEndPointJitterMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 13),
    _AdVqmEndPointJitterMaximum_Type()
)
adVqmEndPointJitterMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointJitterMaximum.setStatus("current")
_AdVqmEndPointNumberStreamsExcellent_Type = Counter32
_AdVqmEndPointNumberStreamsExcellent_Object = MibTableColumn
adVqmEndPointNumberStreamsExcellent = _AdVqmEndPointNumberStreamsExcellent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 14),
    _AdVqmEndPointNumberStreamsExcellent_Type()
)
adVqmEndPointNumberStreamsExcellent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointNumberStreamsExcellent.setStatus("current")
_AdVqmEndPointNumberStreamsGood_Type = Counter32
_AdVqmEndPointNumberStreamsGood_Object = MibTableColumn
adVqmEndPointNumberStreamsGood = _AdVqmEndPointNumberStreamsGood_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 15),
    _AdVqmEndPointNumberStreamsGood_Type()
)
adVqmEndPointNumberStreamsGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointNumberStreamsGood.setStatus("current")
_AdVqmEndPointNumberStreamsFair_Type = Counter32
_AdVqmEndPointNumberStreamsFair_Object = MibTableColumn
adVqmEndPointNumberStreamsFair = _AdVqmEndPointNumberStreamsFair_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 16),
    _AdVqmEndPointNumberStreamsFair_Type()
)
adVqmEndPointNumberStreamsFair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointNumberStreamsFair.setStatus("current")
_AdVqmEndPointNumberStreamsPoor_Type = Counter32
_AdVqmEndPointNumberStreamsPoor_Object = MibTableColumn
adVqmEndPointNumberStreamsPoor = _AdVqmEndPointNumberStreamsPoor_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 6, 1, 1, 17),
    _AdVqmEndPointNumberStreamsPoor_Type()
)
adVqmEndPointNumberStreamsPoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmEndPointNumberStreamsPoor.setStatus("current")
_AdVQMHistory_ObjectIdentity = ObjectIdentity
adVQMHistory = _AdVQMHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7)
)
_AdVQMCallHistoryTable_Object = MibTable
adVQMCallHistoryTable = _AdVQMCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1)
)
if mibBuilder.loadTexts:
    adVQMCallHistoryTable.setStatus("current")
_AdVQMCallHistoryEntry_Object = MibTableRow
adVQMCallHistoryEntry = _AdVQMCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1)
)
adVQMCallHistoryEntry.setIndexNames(
    (0, "ADTRAN-AOS-VQM", "adVqmCallHistRtpSourceIp"),
    (0, "ADTRAN-AOS-VQM", "adVqmCallHistRtpSourcePort"),
    (0, "ADTRAN-AOS-VQM", "adVqmCallHistRtpDestIp"),
    (0, "ADTRAN-AOS-VQM", "adVqmCallHistRtpDestPort"),
    (0, "ADTRAN-AOS-VQM", "adVqmCallHistSsrcid"),
)
if mibBuilder.loadTexts:
    adVQMCallHistoryEntry.setStatus("current")
_AdVqmCallHistRtpSourceIp_Type = IpAddress
_AdVqmCallHistRtpSourceIp_Object = MibTableColumn
adVqmCallHistRtpSourceIp = _AdVqmCallHistRtpSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 1),
    _AdVqmCallHistRtpSourceIp_Type()
)
adVqmCallHistRtpSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRtpSourceIp.setStatus("current")
_AdVqmCallHistRtpSourcePort_Type = Unsigned32
_AdVqmCallHistRtpSourcePort_Object = MibTableColumn
adVqmCallHistRtpSourcePort = _AdVqmCallHistRtpSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 2),
    _AdVqmCallHistRtpSourcePort_Type()
)
adVqmCallHistRtpSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRtpSourcePort.setStatus("current")
_AdVqmCallHistRtpDestIp_Type = IpAddress
_AdVqmCallHistRtpDestIp_Object = MibTableColumn
adVqmCallHistRtpDestIp = _AdVqmCallHistRtpDestIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 3),
    _AdVqmCallHistRtpDestIp_Type()
)
adVqmCallHistRtpDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRtpDestIp.setStatus("current")
_AdVqmCallHistRtpDestPort_Type = Unsigned32
_AdVqmCallHistRtpDestPort_Object = MibTableColumn
adVqmCallHistRtpDestPort = _AdVqmCallHistRtpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 4),
    _AdVqmCallHistRtpDestPort_Type()
)
adVqmCallHistRtpDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRtpDestPort.setStatus("current")
_AdVqmCallHistSsrcid_Type = Unsigned32
_AdVqmCallHistSsrcid_Object = MibTableColumn
adVqmCallHistSsrcid = _AdVqmCallHistSsrcid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 5),
    _AdVqmCallHistSsrcid_Type()
)
adVqmCallHistSsrcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistSsrcid.setStatus("current")
_AdVqmCallHistTo_Type = DisplayString
_AdVqmCallHistTo_Object = MibTableColumn
adVqmCallHistTo = _AdVqmCallHistTo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 6),
    _AdVqmCallHistTo_Type()
)
adVqmCallHistTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistTo.setStatus("current")
_AdVqmCallHistFrom_Type = DisplayString
_AdVqmCallHistFrom_Object = MibTableColumn
adVqmCallHistFrom = _AdVqmCallHistFrom_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 7),
    _AdVqmCallHistFrom_Type()
)
adVqmCallHistFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistFrom.setStatus("current")
_AdVqmCallHistRtpSourceUri_Type = DisplayString
_AdVqmCallHistRtpSourceUri_Object = MibTableColumn
adVqmCallHistRtpSourceUri = _AdVqmCallHistRtpSourceUri_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 8),
    _AdVqmCallHistRtpSourceUri_Type()
)
adVqmCallHistRtpSourceUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRtpSourceUri.setStatus("current")
_AdVqmCallHistCallid_Type = DisplayString
_AdVqmCallHistCallid_Object = MibTableColumn
adVqmCallHistCallid = _AdVqmCallHistCallid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 9),
    _AdVqmCallHistCallid_Type()
)
adVqmCallHistCallid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistCallid.setStatus("current")
_AdVqmCallHistCcmid_Type = Unsigned32
_AdVqmCallHistCcmid_Object = MibTableColumn
adVqmCallHistCcmid = _AdVqmCallHistCcmid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 10),
    _AdVqmCallHistCcmid_Type()
)
adVqmCallHistCcmid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistCcmid.setStatus("current")
_AdVqmCallHistSourceIntName_Type = DisplayString
_AdVqmCallHistSourceIntName_Object = MibTableColumn
adVqmCallHistSourceIntName = _AdVqmCallHistSourceIntName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 11),
    _AdVqmCallHistSourceIntName_Type()
)
adVqmCallHistSourceIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistSourceIntName.setStatus("current")
_AdVqmCallHistDestIntName_Type = DisplayString
_AdVqmCallHistDestIntName_Object = MibTableColumn
adVqmCallHistDestIntName = _AdVqmCallHistDestIntName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 12),
    _AdVqmCallHistDestIntName_Type()
)
adVqmCallHistDestIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDestIntName.setStatus("current")
_AdVqmCallHistSourceIntDescription_Type = DisplayString
_AdVqmCallHistSourceIntDescription_Object = MibTableColumn
adVqmCallHistSourceIntDescription = _AdVqmCallHistSourceIntDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 13),
    _AdVqmCallHistSourceIntDescription_Type()
)
adVqmCallHistSourceIntDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistSourceIntDescription.setStatus("current")
_AdVqmCallHistDestIntDescription_Type = DisplayString
_AdVqmCallHistDestIntDescription_Object = MibTableColumn
adVqmCallHistDestIntDescription = _AdVqmCallHistDestIntDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 14),
    _AdVqmCallHistDestIntDescription_Type()
)
adVqmCallHistDestIntDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDestIntDescription.setStatus("current")
_AdVqmCallHistCallStart_Type = DisplayString
_AdVqmCallHistCallStart_Object = MibTableColumn
adVqmCallHistCallStart = _AdVqmCallHistCallStart_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 15),
    _AdVqmCallHistCallStart_Type()
)
adVqmCallHistCallStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistCallStart.setStatus("current")
_AdVqmCallHistCallDurationMs_Type = Unsigned32
_AdVqmCallHistCallDurationMs_Object = MibTableColumn
adVqmCallHistCallDurationMs = _AdVqmCallHistCallDurationMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 16),
    _AdVqmCallHistCallDurationMs_Type()
)
adVqmCallHistCallDurationMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistCallDurationMs.setStatus("current")


class _AdVqmCallHistCodec_Type(Integer32):
    """Custom type adVqmCallHistCodec based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89)
        )
    )
    namedValues = NamedValues(
        *(("amrnb10k2", 61),
          ("amrnb12k2", 60),
          ("amrnb4k75", 67),
          ("amrnb5k15", 66),
          ("amrnb5k9", 65),
          ("amrnb6k7", 64),
          ("amrnb7k4", 63),
          ("amrnb7k95", 62),
          ("deprecated1", 5),
          ("deprecated2", 7),
          ("deprecated3", 9),
          ("deprecated4", 11),
          ("deprecated5", 13),
          ("deprecated6", 25),
          ("evrc", 55),
          ("g711A", 23),
          ("g711A56k", 72),
          ("g711APLC", 24),
          ("g711APLC56k", 73),
          ("g711U", 2),
          ("g711UPLC", 3),
          ("g711u56k", 70),
          ("g711uPLC56k", 71),
          ("g7221at24k", 43),
          ("g7221at32k", 42),
          ("g7222at12k85", 50),
          ("g7222at14k25", 49),
          ("g7222at15k85", 48),
          ("g7222at18k25", 47),
          ("g7222at19k85", 46),
          ("g7222at23k05", 45),
          ("g7222at23k85", 44),
          ("g7222at6k6", 52),
          ("g7222at8k85", 51),
          ("g722at48k", 41),
          ("g722at56k", 40),
          ("g722at64k", 39),
          ("g723153K", 4),
          ("g723163K", 6),
          ("g7231C", 74),
          ("g72616K", 26),
          ("g72624K", 27),
          ("g72632K", 28),
          ("g72640K", 29),
          ("g728", 8),
          ("g729", 10),
          ("g729A", 12),
          ("g729E11k8", 36),
          ("g729E8K0", 35),
          ("gipse711A", 31),
          ("gipse711U", 30),
          ("gipsilbc", 32),
          ("gipsipcmwb", 34),
          ("gipsisac", 33),
          ("gsmefr", 20),
          ("gsmfr", 18),
          ("ilbc13k3", 68),
          ("ilbc15k2", 69),
          ("qcelp13", 54),
          ("qcelp8", 53),
          ("reservedgsmhr", 19),
          ("smv395", 59),
          ("smv444", 58),
          ("smv579", 57),
          ("smv812", 56),
          ("speeX11k", 78),
          ("speeX12k8", 83),
          ("speeX15k", 79),
          ("speeX16k8", 84),
          ("speeX18k2", 80),
          ("speeX20k6", 85),
          ("speeX23k8", 86),
          ("speeX24k6", 81),
          ("speeX27k8", 87),
          ("speeX34k2", 88),
          ("speeX3k95", 82),
          ("speeX42k2", 89),
          ("speeX8k", 77),
          ("speex2k15", 75),
          ("speex5k95", 76),
          ("sx7300", 21),
          ("sx9600", 22),
          ("unknown", 1),
          ("user1", 14),
          ("user2", 15),
          ("user3", 16),
          ("user4", 17),
          ("wblinearpcm", 37),
          ("wblinearpcmPlc", 38))
    )


_AdVqmCallHistCodec_Type.__name__ = "Integer32"
_AdVqmCallHistCodec_Object = MibTableColumn
adVqmCallHistCodec = _AdVqmCallHistCodec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 17),
    _AdVqmCallHistCodec_Type()
)
adVqmCallHistCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistCodec.setStatus("current")


class _AdVqmCallHistCodecClass_Type(Integer32):
    """Custom type adVqmCallHistCodecClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("wideband", 1))
    )


_AdVqmCallHistCodecClass_Type.__name__ = "Integer32"
_AdVqmCallHistCodecClass_Object = MibTableColumn
adVqmCallHistCodecClass = _AdVqmCallHistCodecClass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 18),
    _AdVqmCallHistCodecClass_Type()
)
adVqmCallHistCodecClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistCodecClass.setStatus("current")
_AdVqmCallHistDscp_Type = Unsigned32
_AdVqmCallHistDscp_Object = MibTableColumn
adVqmCallHistDscp = _AdVqmCallHistDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 19),
    _AdVqmCallHistDscp_Type()
)
adVqmCallHistDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDscp.setStatus("current")
_AdVqmCallHistPktsRcvdTotal_Type = Counter32
_AdVqmCallHistPktsRcvdTotal_Object = MibTableColumn
adVqmCallHistPktsRcvdTotal = _AdVqmCallHistPktsRcvdTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 20),
    _AdVqmCallHistPktsRcvdTotal_Type()
)
adVqmCallHistPktsRcvdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistPktsRcvdTotal.setStatus("current")
_AdVqmCallHistPktsLostTotal_Type = Counter32
_AdVqmCallHistPktsLostTotal_Object = MibTableColumn
adVqmCallHistPktsLostTotal = _AdVqmCallHistPktsLostTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 21),
    _AdVqmCallHistPktsLostTotal_Type()
)
adVqmCallHistPktsLostTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistPktsLostTotal.setStatus("current")
_AdVqmCallHistPktsDiscardedTotal_Type = Counter32
_AdVqmCallHistPktsDiscardedTotal_Object = MibTableColumn
adVqmCallHistPktsDiscardedTotal = _AdVqmCallHistPktsDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 22),
    _AdVqmCallHistPktsDiscardedTotal_Type()
)
adVqmCallHistPktsDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistPktsDiscardedTotal.setStatus("current")
_AdVqmCallHistOutOfOrder_Type = Counter32
_AdVqmCallHistOutOfOrder_Object = MibTableColumn
adVqmCallHistOutOfOrder = _AdVqmCallHistOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 23),
    _AdVqmCallHistOutOfOrder_Type()
)
adVqmCallHistOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistOutOfOrder.setStatus("current")
_AdVqmCallHistPdvAverageMs_Type = Unsigned32
_AdVqmCallHistPdvAverageMs_Object = MibTableColumn
adVqmCallHistPdvAverageMs = _AdVqmCallHistPdvAverageMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 24),
    _AdVqmCallHistPdvAverageMs_Type()
)
adVqmCallHistPdvAverageMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistPdvAverageMs.setStatus("current")
_AdVqmCallHistPdvMaximumMs_Type = Unsigned32
_AdVqmCallHistPdvMaximumMs_Object = MibTableColumn
adVqmCallHistPdvMaximumMs = _AdVqmCallHistPdvMaximumMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 25),
    _AdVqmCallHistPdvMaximumMs_Type()
)
adVqmCallHistPdvMaximumMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistPdvMaximumMs.setStatus("current")
_AdVqmCallHistRtDelayInst_Type = Integer32
_AdVqmCallHistRtDelayInst_Object = MibTableColumn
adVqmCallHistRtDelayInst = _AdVqmCallHistRtDelayInst_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 26),
    _AdVqmCallHistRtDelayInst_Type()
)
adVqmCallHistRtDelayInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRtDelayInst.setStatus("current")
_AdVqmCallHistRtDelayAverage_Type = Integer32
_AdVqmCallHistRtDelayAverage_Object = MibTableColumn
adVqmCallHistRtDelayAverage = _AdVqmCallHistRtDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 27),
    _AdVqmCallHistRtDelayAverage_Type()
)
adVqmCallHistRtDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRtDelayAverage.setStatus("current")
_AdVqmCallHistRtDelayMaximum_Type = Integer32
_AdVqmCallHistRtDelayMaximum_Object = MibTableColumn
adVqmCallHistRtDelayMaximum = _AdVqmCallHistRtDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 28),
    _AdVqmCallHistRtDelayMaximum_Type()
)
adVqmCallHistRtDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRtDelayMaximum.setStatus("current")
_AdVqmCallHistOnewayDelayInst_Type = Integer32
_AdVqmCallHistOnewayDelayInst_Object = MibTableColumn
adVqmCallHistOnewayDelayInst = _AdVqmCallHistOnewayDelayInst_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 29),
    _AdVqmCallHistOnewayDelayInst_Type()
)
adVqmCallHistOnewayDelayInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistOnewayDelayInst.setStatus("current")
_AdVqmCallHistOnewayDelayAverage_Type = Integer32
_AdVqmCallHistOnewayDelayAverage_Object = MibTableColumn
adVqmCallHistOnewayDelayAverage = _AdVqmCallHistOnewayDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 30),
    _AdVqmCallHistOnewayDelayAverage_Type()
)
adVqmCallHistOnewayDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistOnewayDelayAverage.setStatus("current")
_AdVqmCallHistOnewayDelayMaximum_Type = Integer32
_AdVqmCallHistOnewayDelayMaximum_Object = MibTableColumn
adVqmCallHistOnewayDelayMaximum = _AdVqmCallHistOnewayDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 31),
    _AdVqmCallHistOnewayDelayMaximum_Type()
)
adVqmCallHistOnewayDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistOnewayDelayMaximum.setStatus("current")
_AdVqmCallHistOrigDelayInst_Type = Integer32
_AdVqmCallHistOrigDelayInst_Object = MibTableColumn
adVqmCallHistOrigDelayInst = _AdVqmCallHistOrigDelayInst_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 32),
    _AdVqmCallHistOrigDelayInst_Type()
)
adVqmCallHistOrigDelayInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistOrigDelayInst.setStatus("current")
_AdVqmCallHistOrigDelayAverage_Type = Integer32
_AdVqmCallHistOrigDelayAverage_Object = MibTableColumn
adVqmCallHistOrigDelayAverage = _AdVqmCallHistOrigDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 33),
    _AdVqmCallHistOrigDelayAverage_Type()
)
adVqmCallHistOrigDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistOrigDelayAverage.setStatus("current")
_AdVqmCallHistOrigDelayMaximum_Type = Integer32
_AdVqmCallHistOrigDelayMaximum_Object = MibTableColumn
adVqmCallHistOrigDelayMaximum = _AdVqmCallHistOrigDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 34),
    _AdVqmCallHistOrigDelayMaximum_Type()
)
adVqmCallHistOrigDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistOrigDelayMaximum.setStatus("current")
_AdVqmCallHistTermDelayMinimum_Type = Integer32
_AdVqmCallHistTermDelayMinimum_Object = MibTableColumn
adVqmCallHistTermDelayMinimum = _AdVqmCallHistTermDelayMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 35),
    _AdVqmCallHistTermDelayMinimum_Type()
)
adVqmCallHistTermDelayMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistTermDelayMinimum.setStatus("current")
_AdVqmCallHistTermDelayAverage_Type = Integer32
_AdVqmCallHistTermDelayAverage_Object = MibTableColumn
adVqmCallHistTermDelayAverage = _AdVqmCallHistTermDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 36),
    _AdVqmCallHistTermDelayAverage_Type()
)
adVqmCallHistTermDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistTermDelayAverage.setStatus("current")
_AdVqmCallHistTermDelayMaximum_Type = Integer32
_AdVqmCallHistTermDelayMaximum_Object = MibTableColumn
adVqmCallHistTermDelayMaximum = _AdVqmCallHistTermDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 37),
    _AdVqmCallHistTermDelayMaximum_Type()
)
adVqmCallHistTermDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistTermDelayMaximum.setStatus("current")
_AdVqmCallHistRLq_Type = Unsigned32
_AdVqmCallHistRLq_Object = MibTableColumn
adVqmCallHistRLq = _AdVqmCallHistRLq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 38),
    _AdVqmCallHistRLq_Type()
)
adVqmCallHistRLq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRLq.setStatus("current")
_AdVqmCallHistRCq_Type = Unsigned32
_AdVqmCallHistRCq_Object = MibTableColumn
adVqmCallHistRCq = _AdVqmCallHistRCq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 39),
    _AdVqmCallHistRCq_Type()
)
adVqmCallHistRCq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRCq.setStatus("current")
_AdVqmCallHistRNominal_Type = Unsigned32
_AdVqmCallHistRNominal_Object = MibTableColumn
adVqmCallHistRNominal = _AdVqmCallHistRNominal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 40),
    _AdVqmCallHistRNominal_Type()
)
adVqmCallHistRNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRNominal.setStatus("current")
_AdVqmCallHistRG107_Type = Unsigned32
_AdVqmCallHistRG107_Object = MibTableColumn
adVqmCallHistRG107 = _AdVqmCallHistRG107_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 41),
    _AdVqmCallHistRG107_Type()
)
adVqmCallHistRG107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistRG107.setStatus("current")
_AdVqmCallHistMosLq_Type = MOSvalue
_AdVqmCallHistMosLq_Object = MibTableColumn
adVqmCallHistMosLq = _AdVqmCallHistMosLq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 42),
    _AdVqmCallHistMosLq_Type()
)
adVqmCallHistMosLq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistMosLq.setStatus("current")
_AdVqmCallHistMosCq_Type = MOSvalue
_AdVqmCallHistMosCq_Object = MibTableColumn
adVqmCallHistMosCq = _AdVqmCallHistMosCq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 43),
    _AdVqmCallHistMosCq_Type()
)
adVqmCallHistMosCq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistMosCq.setStatus("current")
_AdVqmCallHistMosPq_Type = MOSvalue
_AdVqmCallHistMosPq_Object = MibTableColumn
adVqmCallHistMosPq = _AdVqmCallHistMosPq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 44),
    _AdVqmCallHistMosPq_Type()
)
adVqmCallHistMosPq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistMosPq.setStatus("current")
_AdVqmCallHistMosNominal_Type = MOSvalue
_AdVqmCallHistMosNominal_Object = MibTableColumn
adVqmCallHistMosNominal = _AdVqmCallHistMosNominal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 45),
    _AdVqmCallHistMosNominal_Type()
)
adVqmCallHistMosNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistMosNominal.setStatus("current")
_AdVqmCallHistDegLoss_Type = Percentage
_AdVqmCallHistDegLoss_Object = MibTableColumn
adVqmCallHistDegLoss = _AdVqmCallHistDegLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 46),
    _AdVqmCallHistDegLoss_Type()
)
adVqmCallHistDegLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDegLoss.setStatus("current")
_AdVqmCallHistDegDiscard_Type = Percentage
_AdVqmCallHistDegDiscard_Object = MibTableColumn
adVqmCallHistDegDiscard = _AdVqmCallHistDegDiscard_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 47),
    _AdVqmCallHistDegDiscard_Type()
)
adVqmCallHistDegDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDegDiscard.setStatus("current")
_AdVqmCallHistDegVocoder_Type = Percentage
_AdVqmCallHistDegVocoder_Object = MibTableColumn
adVqmCallHistDegVocoder = _AdVqmCallHistDegVocoder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 48),
    _AdVqmCallHistDegVocoder_Type()
)
adVqmCallHistDegVocoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDegVocoder.setStatus("current")
_AdVqmCallHistDegRecency_Type = Percentage
_AdVqmCallHistDegRecency_Object = MibTableColumn
adVqmCallHistDegRecency = _AdVqmCallHistDegRecency_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 49),
    _AdVqmCallHistDegRecency_Type()
)
adVqmCallHistDegRecency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDegRecency.setStatus("current")
_AdVqmCallHistDegDelay_Type = Percentage
_AdVqmCallHistDegDelay_Object = MibTableColumn
adVqmCallHistDegDelay = _AdVqmCallHistDegDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 50),
    _AdVqmCallHistDegDelay_Type()
)
adVqmCallHistDegDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDegDelay.setStatus("current")
_AdVqmCallHistDegSiglvl_Type = Percentage
_AdVqmCallHistDegSiglvl_Object = MibTableColumn
adVqmCallHistDegSiglvl = _AdVqmCallHistDegSiglvl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 51),
    _AdVqmCallHistDegSiglvl_Type()
)
adVqmCallHistDegSiglvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDegSiglvl.setStatus("current")
_AdVqmCallHistDegNoiselvl_Type = Percentage
_AdVqmCallHistDegNoiselvl_Object = MibTableColumn
adVqmCallHistDegNoiselvl = _AdVqmCallHistDegNoiselvl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 52),
    _AdVqmCallHistDegNoiselvl_Type()
)
adVqmCallHistDegNoiselvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDegNoiselvl.setStatus("current")
_AdVqmCallHistDegEcholvl_Type = Percentage
_AdVqmCallHistDegEcholvl_Object = MibTableColumn
adVqmCallHistDegEcholvl = _AdVqmCallHistDegEcholvl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 53),
    _AdVqmCallHistDegEcholvl_Type()
)
adVqmCallHistDegEcholvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDegEcholvl.setStatus("current")
_AdVqmCallHistBurstRLq_Type = Unsigned32
_AdVqmCallHistBurstRLq_Object = MibTableColumn
adVqmCallHistBurstRLq = _AdVqmCallHistBurstRLq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 54),
    _AdVqmCallHistBurstRLq_Type()
)
adVqmCallHistBurstRLq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistBurstRLq.setStatus("current")
_AdVqmCallHistBurstCount_Type = Counter32
_AdVqmCallHistBurstCount_Object = MibTableColumn
adVqmCallHistBurstCount = _AdVqmCallHistBurstCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 55),
    _AdVqmCallHistBurstCount_Type()
)
adVqmCallHistBurstCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistBurstCount.setStatus("current")
_AdVqmCallHistBurstRateAvg_Type = Percentage
_AdVqmCallHistBurstRateAvg_Object = MibTableColumn
adVqmCallHistBurstRateAvg = _AdVqmCallHistBurstRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 56),
    _AdVqmCallHistBurstRateAvg_Type()
)
adVqmCallHistBurstRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistBurstRateAvg.setStatus("current")
_AdVqmCallHistBurstLenAvgPkts_Type = Unsigned32
_AdVqmCallHistBurstLenAvgPkts_Object = MibTableColumn
adVqmCallHistBurstLenAvgPkts = _AdVqmCallHistBurstLenAvgPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 57),
    _AdVqmCallHistBurstLenAvgPkts_Type()
)
adVqmCallHistBurstLenAvgPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistBurstLenAvgPkts.setStatus("current")
_AdVqmCallHistBurstLenAvgMsec_Type = Unsigned32
_AdVqmCallHistBurstLenAvgMsec_Object = MibTableColumn
adVqmCallHistBurstLenAvgMsec = _AdVqmCallHistBurstLenAvgMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 58),
    _AdVqmCallHistBurstLenAvgMsec_Type()
)
adVqmCallHistBurstLenAvgMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistBurstLenAvgMsec.setStatus("current")
_AdVqmCallHistGapR_Type = Unsigned32
_AdVqmCallHistGapR_Object = MibTableColumn
adVqmCallHistGapR = _AdVqmCallHistGapR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 59),
    _AdVqmCallHistGapR_Type()
)
adVqmCallHistGapR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistGapR.setStatus("current")
_AdVqmCallHistGapCount_Type = Counter32
_AdVqmCallHistGapCount_Object = MibTableColumn
adVqmCallHistGapCount = _AdVqmCallHistGapCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 60),
    _AdVqmCallHistGapCount_Type()
)
adVqmCallHistGapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistGapCount.setStatus("current")
_AdVqmCallHistGapLossRateAvg_Type = Percentage
_AdVqmCallHistGapLossRateAvg_Object = MibTableColumn
adVqmCallHistGapLossRateAvg = _AdVqmCallHistGapLossRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 61),
    _AdVqmCallHistGapLossRateAvg_Type()
)
adVqmCallHistGapLossRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistGapLossRateAvg.setStatus("current")
_AdVqmCallHistGapLenPkts_Type = Unsigned32
_AdVqmCallHistGapLenPkts_Object = MibTableColumn
adVqmCallHistGapLenPkts = _AdVqmCallHistGapLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 62),
    _AdVqmCallHistGapLenPkts_Type()
)
adVqmCallHistGapLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistGapLenPkts.setStatus("current")
_AdVqmCallHistGapLenMsec_Type = Unsigned32
_AdVqmCallHistGapLenMsec_Object = MibTableColumn
adVqmCallHistGapLenMsec = _AdVqmCallHistGapLenMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 63),
    _AdVqmCallHistGapLenMsec_Type()
)
adVqmCallHistGapLenMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistGapLenMsec.setStatus("current")
_AdVqmCallHistLossRateAvg_Type = Percentage
_AdVqmCallHistLossRateAvg_Object = MibTableColumn
adVqmCallHistLossRateAvg = _AdVqmCallHistLossRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 64),
    _AdVqmCallHistLossRateAvg_Type()
)
adVqmCallHistLossRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistLossRateAvg.setStatus("current")
_AdVqmCallHistNetworkLossAvg_Type = Percentage
_AdVqmCallHistNetworkLossAvg_Object = MibTableColumn
adVqmCallHistNetworkLossAvg = _AdVqmCallHistNetworkLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 65),
    _AdVqmCallHistNetworkLossAvg_Type()
)
adVqmCallHistNetworkLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistNetworkLossAvg.setStatus("current")
_AdVqmCallHistDiscardRateAvg_Type = Percentage
_AdVqmCallHistDiscardRateAvg_Object = MibTableColumn
adVqmCallHistDiscardRateAvg = _AdVqmCallHistDiscardRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 66),
    _AdVqmCallHistDiscardRateAvg_Type()
)
adVqmCallHistDiscardRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDiscardRateAvg.setStatus("current")
_AdVqmCallHistExcessBurst_Type = Unsigned32
_AdVqmCallHistExcessBurst_Object = MibTableColumn
adVqmCallHistExcessBurst = _AdVqmCallHistExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 67),
    _AdVqmCallHistExcessBurst_Type()
)
adVqmCallHistExcessBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistExcessBurst.setStatus("current")
_AdVqmCallHistExcessGap_Type = Unsigned32
_AdVqmCallHistExcessGap_Object = MibTableColumn
adVqmCallHistExcessGap = _AdVqmCallHistExcessGap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 68),
    _AdVqmCallHistExcessGap_Type()
)
adVqmCallHistExcessGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistExcessGap.setStatus("current")
_AdVqmCallHistPpdvMsec_Type = MsecValue
_AdVqmCallHistPpdvMsec_Object = MibTableColumn
adVqmCallHistPpdvMsec = _AdVqmCallHistPpdvMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 69),
    _AdVqmCallHistPpdvMsec_Type()
)
adVqmCallHistPpdvMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistPpdvMsec.setStatus("current")
_AdVqmCallHistLateThresholdMs_Type = MsecValue
_AdVqmCallHistLateThresholdMs_Object = MibTableColumn
adVqmCallHistLateThresholdMs = _AdVqmCallHistLateThresholdMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 70),
    _AdVqmCallHistLateThresholdMs_Type()
)
adVqmCallHistLateThresholdMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistLateThresholdMs.setStatus("current")
_AdVqmCallHistLateThresholdPc_Type = Percentage
_AdVqmCallHistLateThresholdPc_Object = MibTableColumn
adVqmCallHistLateThresholdPc = _AdVqmCallHistLateThresholdPc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 71),
    _AdVqmCallHistLateThresholdPc_Type()
)
adVqmCallHistLateThresholdPc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistLateThresholdPc.setStatus("current")
_AdVqmCallHistLateUnderThresh_Type = Counter32
_AdVqmCallHistLateUnderThresh_Object = MibTableColumn
adVqmCallHistLateUnderThresh = _AdVqmCallHistLateUnderThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 72),
    _AdVqmCallHistLateUnderThresh_Type()
)
adVqmCallHistLateUnderThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistLateUnderThresh.setStatus("current")
_AdVqmCallHistLateTotalCount_Type = Counter32
_AdVqmCallHistLateTotalCount_Object = MibTableColumn
adVqmCallHistLateTotalCount = _AdVqmCallHistLateTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 73),
    _AdVqmCallHistLateTotalCount_Type()
)
adVqmCallHistLateTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistLateTotalCount.setStatus("current")
_AdVqmCallHistLatePeakJitterMs_Type = MsecValue
_AdVqmCallHistLatePeakJitterMs_Object = MibTableColumn
adVqmCallHistLatePeakJitterMs = _AdVqmCallHistLatePeakJitterMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 74),
    _AdVqmCallHistLatePeakJitterMs_Type()
)
adVqmCallHistLatePeakJitterMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistLatePeakJitterMs.setStatus("current")
_AdVqmCallHistEarlyThreshMs_Type = MsecValue
_AdVqmCallHistEarlyThreshMs_Object = MibTableColumn
adVqmCallHistEarlyThreshMs = _AdVqmCallHistEarlyThreshMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 75),
    _AdVqmCallHistEarlyThreshMs_Type()
)
adVqmCallHistEarlyThreshMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistEarlyThreshMs.setStatus("current")
_AdVqmCallHistEarlyThreshPc_Type = Percentage
_AdVqmCallHistEarlyThreshPc_Object = MibTableColumn
adVqmCallHistEarlyThreshPc = _AdVqmCallHistEarlyThreshPc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 76),
    _AdVqmCallHistEarlyThreshPc_Type()
)
adVqmCallHistEarlyThreshPc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistEarlyThreshPc.setStatus("current")
_AdVqmCallHistEarlyUnderThresh_Type = Counter32
_AdVqmCallHistEarlyUnderThresh_Object = MibTableColumn
adVqmCallHistEarlyUnderThresh = _AdVqmCallHistEarlyUnderThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 77),
    _AdVqmCallHistEarlyUnderThresh_Type()
)
adVqmCallHistEarlyUnderThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistEarlyUnderThresh.setStatus("current")
_AdVqmCallHistEarlyTotalCount_Type = Counter32
_AdVqmCallHistEarlyTotalCount_Object = MibTableColumn
adVqmCallHistEarlyTotalCount = _AdVqmCallHistEarlyTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 78),
    _AdVqmCallHistEarlyTotalCount_Type()
)
adVqmCallHistEarlyTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistEarlyTotalCount.setStatus("current")
_AdVqmCallHistEarlyPeakJitterMs_Type = MsecValue
_AdVqmCallHistEarlyPeakJitterMs_Object = MibTableColumn
adVqmCallHistEarlyPeakJitterMs = _AdVqmCallHistEarlyPeakJitterMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 79),
    _AdVqmCallHistEarlyPeakJitterMs_Type()
)
adVqmCallHistEarlyPeakJitterMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistEarlyPeakJitterMs.setStatus("current")
_AdVqmCallHistDelayIncreaseCount_Type = Counter32
_AdVqmCallHistDelayIncreaseCount_Object = MibTableColumn
adVqmCallHistDelayIncreaseCount = _AdVqmCallHistDelayIncreaseCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 80),
    _AdVqmCallHistDelayIncreaseCount_Type()
)
adVqmCallHistDelayIncreaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDelayIncreaseCount.setStatus("current")
_AdVqmCallHistDelayDecreaseCount_Type = Counter32
_AdVqmCallHistDelayDecreaseCount_Object = MibTableColumn
adVqmCallHistDelayDecreaseCount = _AdVqmCallHistDelayDecreaseCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 81),
    _AdVqmCallHistDelayDecreaseCount_Type()
)
adVqmCallHistDelayDecreaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDelayDecreaseCount.setStatus("current")
_AdVqmCallHistResyncCount_Type = Counter32
_AdVqmCallHistResyncCount_Object = MibTableColumn
adVqmCallHistResyncCount = _AdVqmCallHistResyncCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 82),
    _AdVqmCallHistResyncCount_Type()
)
adVqmCallHistResyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistResyncCount.setStatus("current")


class _AdVqmCallHistJitterBufferType_Type(Integer32):
    """Custom type adVqmCallHistJitterBufferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1),
          ("unknown", 3))
    )


_AdVqmCallHistJitterBufferType_Type.__name__ = "Integer32"
_AdVqmCallHistJitterBufferType_Object = MibTableColumn
adVqmCallHistJitterBufferType = _AdVqmCallHistJitterBufferType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 83),
    _AdVqmCallHistJitterBufferType_Type()
)
adVqmCallHistJitterBufferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistJitterBufferType.setStatus("current")
_AdVqmCallHistJbCfgMin_Type = Unsigned32
_AdVqmCallHistJbCfgMin_Object = MibTableColumn
adVqmCallHistJbCfgMin = _AdVqmCallHistJbCfgMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 84),
    _AdVqmCallHistJbCfgMin_Type()
)
adVqmCallHistJbCfgMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistJbCfgMin.setStatus("current")
_AdVqmCallHistJbCfgNom_Type = Unsigned32
_AdVqmCallHistJbCfgNom_Object = MibTableColumn
adVqmCallHistJbCfgNom = _AdVqmCallHistJbCfgNom_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 85),
    _AdVqmCallHistJbCfgNom_Type()
)
adVqmCallHistJbCfgNom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistJbCfgNom.setStatus("current")
_AdVqmCallHistJbCfgMax_Type = Unsigned32
_AdVqmCallHistJbCfgMax_Object = MibTableColumn
adVqmCallHistJbCfgMax = _AdVqmCallHistJbCfgMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 86),
    _AdVqmCallHistJbCfgMax_Type()
)
adVqmCallHistJbCfgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistJbCfgMax.setStatus("current")
_AdVqmCallHistDuplicatePkts_Type = Counter32
_AdVqmCallHistDuplicatePkts_Object = MibTableColumn
adVqmCallHistDuplicatePkts = _AdVqmCallHistDuplicatePkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 87),
    _AdVqmCallHistDuplicatePkts_Type()
)
adVqmCallHistDuplicatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDuplicatePkts.setStatus("current")
_AdVqmCallHistEarlyPkts_Type = Counter32
_AdVqmCallHistEarlyPkts_Object = MibTableColumn
adVqmCallHistEarlyPkts = _AdVqmCallHistEarlyPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 88),
    _AdVqmCallHistEarlyPkts_Type()
)
adVqmCallHistEarlyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistEarlyPkts.setStatus("current")
_AdVqmCallHistLatePkts_Type = Counter32
_AdVqmCallHistLatePkts_Object = MibTableColumn
adVqmCallHistLatePkts = _AdVqmCallHistLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 89),
    _AdVqmCallHistLatePkts_Type()
)
adVqmCallHistLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistLatePkts.setStatus("current")
_AdVqmCallHistOverrunDiscardPkts_Type = Counter32
_AdVqmCallHistOverrunDiscardPkts_Object = MibTableColumn
adVqmCallHistOverrunDiscardPkts = _AdVqmCallHistOverrunDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 90),
    _AdVqmCallHistOverrunDiscardPkts_Type()
)
adVqmCallHistOverrunDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistOverrunDiscardPkts.setStatus("current")
_AdVqmCallHistUnderrunDiscardPkts_Type = Counter32
_AdVqmCallHistUnderrunDiscardPkts_Object = MibTableColumn
adVqmCallHistUnderrunDiscardPkts = _AdVqmCallHistUnderrunDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 91),
    _AdVqmCallHistUnderrunDiscardPkts_Type()
)
adVqmCallHistUnderrunDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistUnderrunDiscardPkts.setStatus("current")
_AdVqmCallHistDelayMinMsec_Type = Unsigned32
_AdVqmCallHistDelayMinMsec_Object = MibTableColumn
adVqmCallHistDelayMinMsec = _AdVqmCallHistDelayMinMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 92),
    _AdVqmCallHistDelayMinMsec_Type()
)
adVqmCallHistDelayMinMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDelayMinMsec.setStatus("current")
_AdVqmCallHistDelayAvgMsec_Type = Unsigned32
_AdVqmCallHistDelayAvgMsec_Object = MibTableColumn
adVqmCallHistDelayAvgMsec = _AdVqmCallHistDelayAvgMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 93),
    _AdVqmCallHistDelayAvgMsec_Type()
)
adVqmCallHistDelayAvgMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDelayAvgMsec.setStatus("current")
_AdVqmCallHistDelayMaxMsec_Type = Unsigned32
_AdVqmCallHistDelayMaxMsec_Object = MibTableColumn
adVqmCallHistDelayMaxMsec = _AdVqmCallHistDelayMaxMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 94),
    _AdVqmCallHistDelayMaxMsec_Type()
)
adVqmCallHistDelayMaxMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDelayMaxMsec.setStatus("current")
_AdVqmCallHistDelayCurrentMsec_Type = Unsigned32
_AdVqmCallHistDelayCurrentMsec_Object = MibTableColumn
adVqmCallHistDelayCurrentMsec = _AdVqmCallHistDelayCurrentMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 95),
    _AdVqmCallHistDelayCurrentMsec_Type()
)
adVqmCallHistDelayCurrentMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistDelayCurrentMsec.setStatus("current")
_AdVqmCallHistExtRLqIn_Type = Integer32
_AdVqmCallHistExtRLqIn_Object = MibTableColumn
adVqmCallHistExtRLqIn = _AdVqmCallHistExtRLqIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 96),
    _AdVqmCallHistExtRLqIn_Type()
)
adVqmCallHistExtRLqIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistExtRLqIn.setStatus("current")
_AdVqmCallHistExtRLqOut_Type = Integer32
_AdVqmCallHistExtRLqOut_Object = MibTableColumn
adVqmCallHistExtRLqOut = _AdVqmCallHistExtRLqOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 97),
    _AdVqmCallHistExtRLqOut_Type()
)
adVqmCallHistExtRLqOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistExtRLqOut.setStatus("current")
_AdVqmCallHistExtRCqIn_Type = Integer32
_AdVqmCallHistExtRCqIn_Object = MibTableColumn
adVqmCallHistExtRCqIn = _AdVqmCallHistExtRCqIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 98),
    _AdVqmCallHistExtRCqIn_Type()
)
adVqmCallHistExtRCqIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistExtRCqIn.setStatus("current")
_AdVqmCallHistExtRCqOut_Type = Integer32
_AdVqmCallHistExtRCqOut_Object = MibTableColumn
adVqmCallHistExtRCqOut = _AdVqmCallHistExtRCqOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 99),
    _AdVqmCallHistExtRCqOut_Type()
)
adVqmCallHistExtRCqOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistExtRCqOut.setStatus("current")
_AdVqmCallHistThroughPutIndex_Type = Unsigned32
_AdVqmCallHistThroughPutIndex_Object = MibTableColumn
adVqmCallHistThroughPutIndex = _AdVqmCallHistThroughPutIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 100),
    _AdVqmCallHistThroughPutIndex_Type()
)
adVqmCallHistThroughPutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistThroughPutIndex.setStatus("current")
_AdVqmCallHistReliabilityIndex_Type = Unsigned32
_AdVqmCallHistReliabilityIndex_Object = MibTableColumn
adVqmCallHistReliabilityIndex = _AdVqmCallHistReliabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 101),
    _AdVqmCallHistReliabilityIndex_Type()
)
adVqmCallHistReliabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistReliabilityIndex.setStatus("current")
_AdVqmCallHistBitrate_Type = Unsigned32
_AdVqmCallHistBitrate_Object = MibTableColumn
adVqmCallHistBitrate = _AdVqmCallHistBitrate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 7, 1, 1, 102),
    _AdVqmCallHistBitrate_Type()
)
adVqmCallHistBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmCallHistBitrate.setStatus("current")
_AdVQMActive_ObjectIdentity = ObjectIdentity
adVQMActive = _AdVQMActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8)
)
_AdVQMActiveCallTable_Object = MibTable
adVQMActiveCallTable = _AdVQMActiveCallTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1)
)
if mibBuilder.loadTexts:
    adVQMActiveCallTable.setStatus("current")
_AdVQMActiveCallEntry_Object = MibTableRow
adVQMActiveCallEntry = _AdVQMActiveCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1)
)
adVQMActiveCallEntry.setIndexNames(
    (0, "ADTRAN-AOS-VQM", "adVqmActCallRtpSourceIp"),
    (0, "ADTRAN-AOS-VQM", "adVqmActCallRtpSourcePort"),
    (0, "ADTRAN-AOS-VQM", "adVqmActCallRtpDestIp"),
    (0, "ADTRAN-AOS-VQM", "adVqmActCallRtpDestPort"),
    (0, "ADTRAN-AOS-VQM", "adVqmActCallSsrcid"),
)
if mibBuilder.loadTexts:
    adVQMActiveCallEntry.setStatus("current")
_AdVqmActCallRtpSourceIp_Type = IpAddress
_AdVqmActCallRtpSourceIp_Object = MibTableColumn
adVqmActCallRtpSourceIp = _AdVqmActCallRtpSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 1),
    _AdVqmActCallRtpSourceIp_Type()
)
adVqmActCallRtpSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRtpSourceIp.setStatus("current")
_AdVqmActCallRtpSourcePort_Type = Unsigned32
_AdVqmActCallRtpSourcePort_Object = MibTableColumn
adVqmActCallRtpSourcePort = _AdVqmActCallRtpSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 2),
    _AdVqmActCallRtpSourcePort_Type()
)
adVqmActCallRtpSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRtpSourcePort.setStatus("current")
_AdVqmActCallRtpDestIp_Type = IpAddress
_AdVqmActCallRtpDestIp_Object = MibTableColumn
adVqmActCallRtpDestIp = _AdVqmActCallRtpDestIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 3),
    _AdVqmActCallRtpDestIp_Type()
)
adVqmActCallRtpDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRtpDestIp.setStatus("current")
_AdVqmActCallRtpDestPort_Type = Unsigned32
_AdVqmActCallRtpDestPort_Object = MibTableColumn
adVqmActCallRtpDestPort = _AdVqmActCallRtpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 4),
    _AdVqmActCallRtpDestPort_Type()
)
adVqmActCallRtpDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRtpDestPort.setStatus("current")
_AdVqmActCallSsrcid_Type = Unsigned32
_AdVqmActCallSsrcid_Object = MibTableColumn
adVqmActCallSsrcid = _AdVqmActCallSsrcid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 5),
    _AdVqmActCallSsrcid_Type()
)
adVqmActCallSsrcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallSsrcid.setStatus("current")
_AdVqmActCallTo_Type = DisplayString
_AdVqmActCallTo_Object = MibTableColumn
adVqmActCallTo = _AdVqmActCallTo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 6),
    _AdVqmActCallTo_Type()
)
adVqmActCallTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallTo.setStatus("current")
_AdVqmActCallFrom_Type = DisplayString
_AdVqmActCallFrom_Object = MibTableColumn
adVqmActCallFrom = _AdVqmActCallFrom_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 7),
    _AdVqmActCallFrom_Type()
)
adVqmActCallFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallFrom.setStatus("current")
_AdVqmActCallRtpSourceUri_Type = DisplayString
_AdVqmActCallRtpSourceUri_Object = MibTableColumn
adVqmActCallRtpSourceUri = _AdVqmActCallRtpSourceUri_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 8),
    _AdVqmActCallRtpSourceUri_Type()
)
adVqmActCallRtpSourceUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRtpSourceUri.setStatus("current")
_AdVqmActCallCallid_Type = DisplayString
_AdVqmActCallCallid_Object = MibTableColumn
adVqmActCallCallid = _AdVqmActCallCallid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 9),
    _AdVqmActCallCallid_Type()
)
adVqmActCallCallid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallCallid.setStatus("current")
_AdVqmActCallCcmid_Type = Unsigned32
_AdVqmActCallCcmid_Object = MibTableColumn
adVqmActCallCcmid = _AdVqmActCallCcmid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 10),
    _AdVqmActCallCcmid_Type()
)
adVqmActCallCcmid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallCcmid.setStatus("current")
_AdVqmActCallSourceIntName_Type = DisplayString
_AdVqmActCallSourceIntName_Object = MibTableColumn
adVqmActCallSourceIntName = _AdVqmActCallSourceIntName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 11),
    _AdVqmActCallSourceIntName_Type()
)
adVqmActCallSourceIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallSourceIntName.setStatus("current")
_AdVqmActCallDestIntName_Type = DisplayString
_AdVqmActCallDestIntName_Object = MibTableColumn
adVqmActCallDestIntName = _AdVqmActCallDestIntName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 12),
    _AdVqmActCallDestIntName_Type()
)
adVqmActCallDestIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDestIntName.setStatus("current")
_AdVqmActCallSourceIntDescription_Type = DisplayString
_AdVqmActCallSourceIntDescription_Object = MibTableColumn
adVqmActCallSourceIntDescription = _AdVqmActCallSourceIntDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 13),
    _AdVqmActCallSourceIntDescription_Type()
)
adVqmActCallSourceIntDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallSourceIntDescription.setStatus("current")
_AdVqmActCallDestIntDescription_Type = DisplayString
_AdVqmActCallDestIntDescription_Object = MibTableColumn
adVqmActCallDestIntDescription = _AdVqmActCallDestIntDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 14),
    _AdVqmActCallDestIntDescription_Type()
)
adVqmActCallDestIntDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDestIntDescription.setStatus("current")
_AdVqmActCallCallStart_Type = DisplayString
_AdVqmActCallCallStart_Object = MibTableColumn
adVqmActCallCallStart = _AdVqmActCallCallStart_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 15),
    _AdVqmActCallCallStart_Type()
)
adVqmActCallCallStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallCallStart.setStatus("current")
_AdVqmActCallCallDurationMs_Type = Unsigned32
_AdVqmActCallCallDurationMs_Object = MibTableColumn
adVqmActCallCallDurationMs = _AdVqmActCallCallDurationMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 16),
    _AdVqmActCallCallDurationMs_Type()
)
adVqmActCallCallDurationMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallCallDurationMs.setStatus("current")


class _AdVqmActCallCodec_Type(Integer32):
    """Custom type adVqmActCallCodec based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89)
        )
    )
    namedValues = NamedValues(
        *(("amrnb10k2", 61),
          ("amrnb12k2", 60),
          ("amrnb4k75", 67),
          ("amrnb5k15", 66),
          ("amrnb5k9", 65),
          ("amrnb6k7", 64),
          ("amrnb7k4", 63),
          ("amrnb7k95", 62),
          ("deprecated1", 5),
          ("deprecated2", 7),
          ("deprecated3", 9),
          ("deprecated4", 11),
          ("deprecated5", 13),
          ("deprecated6", 25),
          ("evrc", 55),
          ("g711A", 23),
          ("g711A56k", 72),
          ("g711APLC", 24),
          ("g711APLC56k", 73),
          ("g711U", 2),
          ("g711UPLC", 3),
          ("g711u56k", 70),
          ("g711uPLC56k", 71),
          ("g7221at24k", 43),
          ("g7221at32k", 42),
          ("g7222at12k85", 50),
          ("g7222at14k25", 49),
          ("g7222at15k85", 48),
          ("g7222at18k25", 47),
          ("g7222at19k85", 46),
          ("g7222at23k05", 45),
          ("g7222at23k85", 44),
          ("g7222at6k6", 52),
          ("g7222at8k85", 51),
          ("g722at48k", 41),
          ("g722at56k", 40),
          ("g722at64k", 39),
          ("g723153K", 4),
          ("g723163K", 6),
          ("g7231C", 74),
          ("g72616K", 26),
          ("g72624K", 27),
          ("g72632K", 28),
          ("g72640K", 29),
          ("g728", 8),
          ("g729", 10),
          ("g729A", 12),
          ("g729E11k8", 36),
          ("g729E8K0", 35),
          ("gipse711A", 31),
          ("gipse711U", 30),
          ("gipsilbc", 32),
          ("gipsipcmwb", 34),
          ("gipsisac", 33),
          ("gsmefr", 20),
          ("gsmfr", 18),
          ("ilbc13k3", 68),
          ("ilbc15k2", 69),
          ("qcelp13", 54),
          ("qcelp8", 53),
          ("reservedgsmhr", 19),
          ("smv395", 59),
          ("smv444", 58),
          ("smv579", 57),
          ("smv812", 56),
          ("speeX11k", 78),
          ("speeX12k8", 83),
          ("speeX15k", 79),
          ("speeX16k8", 84),
          ("speeX18k2", 80),
          ("speeX20k6", 85),
          ("speeX23k8", 86),
          ("speeX24k6", 81),
          ("speeX27k8", 87),
          ("speeX34k2", 88),
          ("speeX3k95", 82),
          ("speeX42k2", 89),
          ("speeX8k", 77),
          ("speex2k15", 75),
          ("speex5k95", 76),
          ("sx7300", 21),
          ("sx9600", 22),
          ("unknown", 1),
          ("user1", 14),
          ("user2", 15),
          ("user3", 16),
          ("user4", 17),
          ("wblinearpcm", 37),
          ("wblinearpcmPlc", 38))
    )


_AdVqmActCallCodec_Type.__name__ = "Integer32"
_AdVqmActCallCodec_Object = MibTableColumn
adVqmActCallCodec = _AdVqmActCallCodec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 17),
    _AdVqmActCallCodec_Type()
)
adVqmActCallCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallCodec.setStatus("current")


class _AdVqmActCallCodecClass_Type(Integer32):
    """Custom type adVqmActCallCodecClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("wideband", 1))
    )


_AdVqmActCallCodecClass_Type.__name__ = "Integer32"
_AdVqmActCallCodecClass_Object = MibTableColumn
adVqmActCallCodecClass = _AdVqmActCallCodecClass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 18),
    _AdVqmActCallCodecClass_Type()
)
adVqmActCallCodecClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallCodecClass.setStatus("current")
_AdVqmActCallDscp_Type = Unsigned32
_AdVqmActCallDscp_Object = MibTableColumn
adVqmActCallDscp = _AdVqmActCallDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 19),
    _AdVqmActCallDscp_Type()
)
adVqmActCallDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDscp.setStatus("current")
_AdVqmActCallPktsRcvdTotal_Type = Counter32
_AdVqmActCallPktsRcvdTotal_Object = MibTableColumn
adVqmActCallPktsRcvdTotal = _AdVqmActCallPktsRcvdTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 20),
    _AdVqmActCallPktsRcvdTotal_Type()
)
adVqmActCallPktsRcvdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallPktsRcvdTotal.setStatus("current")
_AdVqmActCallPktsLostTotal_Type = Counter32
_AdVqmActCallPktsLostTotal_Object = MibTableColumn
adVqmActCallPktsLostTotal = _AdVqmActCallPktsLostTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 21),
    _AdVqmActCallPktsLostTotal_Type()
)
adVqmActCallPktsLostTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallPktsLostTotal.setStatus("current")
_AdVqmActCallPktsDiscardedTotal_Type = Counter32
_AdVqmActCallPktsDiscardedTotal_Object = MibTableColumn
adVqmActCallPktsDiscardedTotal = _AdVqmActCallPktsDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 22),
    _AdVqmActCallPktsDiscardedTotal_Type()
)
adVqmActCallPktsDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallPktsDiscardedTotal.setStatus("current")
_AdVqmActCallOutOfOrder_Type = Counter32
_AdVqmActCallOutOfOrder_Object = MibTableColumn
adVqmActCallOutOfOrder = _AdVqmActCallOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 23),
    _AdVqmActCallOutOfOrder_Type()
)
adVqmActCallOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallOutOfOrder.setStatus("current")
_AdVqmActCallPdvAverageMs_Type = Unsigned32
_AdVqmActCallPdvAverageMs_Object = MibTableColumn
adVqmActCallPdvAverageMs = _AdVqmActCallPdvAverageMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 24),
    _AdVqmActCallPdvAverageMs_Type()
)
adVqmActCallPdvAverageMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallPdvAverageMs.setStatus("current")
_AdVqmActCallPdvMaximumMs_Type = Unsigned32
_AdVqmActCallPdvMaximumMs_Object = MibTableColumn
adVqmActCallPdvMaximumMs = _AdVqmActCallPdvMaximumMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 25),
    _AdVqmActCallPdvMaximumMs_Type()
)
adVqmActCallPdvMaximumMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallPdvMaximumMs.setStatus("current")
_AdVqmActCallRtDelayInst_Type = Integer32
_AdVqmActCallRtDelayInst_Object = MibTableColumn
adVqmActCallRtDelayInst = _AdVqmActCallRtDelayInst_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 26),
    _AdVqmActCallRtDelayInst_Type()
)
adVqmActCallRtDelayInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRtDelayInst.setStatus("current")
_AdVqmActCallRtDelayAverage_Type = Integer32
_AdVqmActCallRtDelayAverage_Object = MibTableColumn
adVqmActCallRtDelayAverage = _AdVqmActCallRtDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 27),
    _AdVqmActCallRtDelayAverage_Type()
)
adVqmActCallRtDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRtDelayAverage.setStatus("current")
_AdVqmActCallRtDelayMaximum_Type = Integer32
_AdVqmActCallRtDelayMaximum_Object = MibTableColumn
adVqmActCallRtDelayMaximum = _AdVqmActCallRtDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 28),
    _AdVqmActCallRtDelayMaximum_Type()
)
adVqmActCallRtDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRtDelayMaximum.setStatus("current")
_AdVqmActCallOnewayDelayInst_Type = Integer32
_AdVqmActCallOnewayDelayInst_Object = MibTableColumn
adVqmActCallOnewayDelayInst = _AdVqmActCallOnewayDelayInst_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 29),
    _AdVqmActCallOnewayDelayInst_Type()
)
adVqmActCallOnewayDelayInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallOnewayDelayInst.setStatus("current")
_AdVqmActCallOnewayDelayAverage_Type = Integer32
_AdVqmActCallOnewayDelayAverage_Object = MibTableColumn
adVqmActCallOnewayDelayAverage = _AdVqmActCallOnewayDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 30),
    _AdVqmActCallOnewayDelayAverage_Type()
)
adVqmActCallOnewayDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallOnewayDelayAverage.setStatus("current")
_AdVqmActCallOnewayDelayMaximum_Type = Integer32
_AdVqmActCallOnewayDelayMaximum_Object = MibTableColumn
adVqmActCallOnewayDelayMaximum = _AdVqmActCallOnewayDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 31),
    _AdVqmActCallOnewayDelayMaximum_Type()
)
adVqmActCallOnewayDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallOnewayDelayMaximum.setStatus("current")
_AdVqmActCallOrigDelayInst_Type = Integer32
_AdVqmActCallOrigDelayInst_Object = MibTableColumn
adVqmActCallOrigDelayInst = _AdVqmActCallOrigDelayInst_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 32),
    _AdVqmActCallOrigDelayInst_Type()
)
adVqmActCallOrigDelayInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallOrigDelayInst.setStatus("current")
_AdVqmActCallOrigDelayAverage_Type = Integer32
_AdVqmActCallOrigDelayAverage_Object = MibTableColumn
adVqmActCallOrigDelayAverage = _AdVqmActCallOrigDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 33),
    _AdVqmActCallOrigDelayAverage_Type()
)
adVqmActCallOrigDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallOrigDelayAverage.setStatus("current")
_AdVqmActCallOrigDelayMaximum_Type = Integer32
_AdVqmActCallOrigDelayMaximum_Object = MibTableColumn
adVqmActCallOrigDelayMaximum = _AdVqmActCallOrigDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 34),
    _AdVqmActCallOrigDelayMaximum_Type()
)
adVqmActCallOrigDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallOrigDelayMaximum.setStatus("current")
_AdVqmActCallTermDelayMinimum_Type = Integer32
_AdVqmActCallTermDelayMinimum_Object = MibTableColumn
adVqmActCallTermDelayMinimum = _AdVqmActCallTermDelayMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 35),
    _AdVqmActCallTermDelayMinimum_Type()
)
adVqmActCallTermDelayMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallTermDelayMinimum.setStatus("current")
_AdVqmActCallTermDelayAverage_Type = Integer32
_AdVqmActCallTermDelayAverage_Object = MibTableColumn
adVqmActCallTermDelayAverage = _AdVqmActCallTermDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 36),
    _AdVqmActCallTermDelayAverage_Type()
)
adVqmActCallTermDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallTermDelayAverage.setStatus("current")
_AdVqmActCallTermDelayMaximum_Type = Integer32
_AdVqmActCallTermDelayMaximum_Object = MibTableColumn
adVqmActCallTermDelayMaximum = _AdVqmActCallTermDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 37),
    _AdVqmActCallTermDelayMaximum_Type()
)
adVqmActCallTermDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallTermDelayMaximum.setStatus("current")
_AdVqmActCallRLq_Type = Unsigned32
_AdVqmActCallRLq_Object = MibTableColumn
adVqmActCallRLq = _AdVqmActCallRLq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 38),
    _AdVqmActCallRLq_Type()
)
adVqmActCallRLq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRLq.setStatus("current")
_AdVqmActCallRCq_Type = Unsigned32
_AdVqmActCallRCq_Object = MibTableColumn
adVqmActCallRCq = _AdVqmActCallRCq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 39),
    _AdVqmActCallRCq_Type()
)
adVqmActCallRCq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRCq.setStatus("current")
_AdVqmActCallRNominal_Type = Unsigned32
_AdVqmActCallRNominal_Object = MibTableColumn
adVqmActCallRNominal = _AdVqmActCallRNominal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 40),
    _AdVqmActCallRNominal_Type()
)
adVqmActCallRNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRNominal.setStatus("current")
_AdVqmActCallRG107_Type = Unsigned32
_AdVqmActCallRG107_Object = MibTableColumn
adVqmActCallRG107 = _AdVqmActCallRG107_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 41),
    _AdVqmActCallRG107_Type()
)
adVqmActCallRG107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallRG107.setStatus("current")
_AdVqmActCallMosLq_Type = MOSvalue
_AdVqmActCallMosLq_Object = MibTableColumn
adVqmActCallMosLq = _AdVqmActCallMosLq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 42),
    _AdVqmActCallMosLq_Type()
)
adVqmActCallMosLq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallMosLq.setStatus("current")
_AdVqmActCallMosCq_Type = MOSvalue
_AdVqmActCallMosCq_Object = MibTableColumn
adVqmActCallMosCq = _AdVqmActCallMosCq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 43),
    _AdVqmActCallMosCq_Type()
)
adVqmActCallMosCq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallMosCq.setStatus("current")
_AdVqmActCallMosPq_Type = MOSvalue
_AdVqmActCallMosPq_Object = MibTableColumn
adVqmActCallMosPq = _AdVqmActCallMosPq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 44),
    _AdVqmActCallMosPq_Type()
)
adVqmActCallMosPq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallMosPq.setStatus("current")
_AdVqmActCallMosNominal_Type = MOSvalue
_AdVqmActCallMosNominal_Object = MibTableColumn
adVqmActCallMosNominal = _AdVqmActCallMosNominal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 45),
    _AdVqmActCallMosNominal_Type()
)
adVqmActCallMosNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallMosNominal.setStatus("current")
_AdVqmActCallDegLoss_Type = Percentage
_AdVqmActCallDegLoss_Object = MibTableColumn
adVqmActCallDegLoss = _AdVqmActCallDegLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 46),
    _AdVqmActCallDegLoss_Type()
)
adVqmActCallDegLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDegLoss.setStatus("current")
_AdVqmActCallDegDiscard_Type = Percentage
_AdVqmActCallDegDiscard_Object = MibTableColumn
adVqmActCallDegDiscard = _AdVqmActCallDegDiscard_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 47),
    _AdVqmActCallDegDiscard_Type()
)
adVqmActCallDegDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDegDiscard.setStatus("current")
_AdVqmActCallDegVocoder_Type = Percentage
_AdVqmActCallDegVocoder_Object = MibTableColumn
adVqmActCallDegVocoder = _AdVqmActCallDegVocoder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 48),
    _AdVqmActCallDegVocoder_Type()
)
adVqmActCallDegVocoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDegVocoder.setStatus("current")
_AdVqmActCallDegRecency_Type = Percentage
_AdVqmActCallDegRecency_Object = MibTableColumn
adVqmActCallDegRecency = _AdVqmActCallDegRecency_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 49),
    _AdVqmActCallDegRecency_Type()
)
adVqmActCallDegRecency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDegRecency.setStatus("current")
_AdVqmActCallDegDelay_Type = Percentage
_AdVqmActCallDegDelay_Object = MibTableColumn
adVqmActCallDegDelay = _AdVqmActCallDegDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 50),
    _AdVqmActCallDegDelay_Type()
)
adVqmActCallDegDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDegDelay.setStatus("current")
_AdVqmActCallDegSiglvl_Type = Percentage
_AdVqmActCallDegSiglvl_Object = MibTableColumn
adVqmActCallDegSiglvl = _AdVqmActCallDegSiglvl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 51),
    _AdVqmActCallDegSiglvl_Type()
)
adVqmActCallDegSiglvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDegSiglvl.setStatus("current")
_AdVqmActCallDegNoiselvl_Type = Percentage
_AdVqmActCallDegNoiselvl_Object = MibTableColumn
adVqmActCallDegNoiselvl = _AdVqmActCallDegNoiselvl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 52),
    _AdVqmActCallDegNoiselvl_Type()
)
adVqmActCallDegNoiselvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDegNoiselvl.setStatus("current")
_AdVqmActCallDegEcholvl_Type = Percentage
_AdVqmActCallDegEcholvl_Object = MibTableColumn
adVqmActCallDegEcholvl = _AdVqmActCallDegEcholvl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 53),
    _AdVqmActCallDegEcholvl_Type()
)
adVqmActCallDegEcholvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDegEcholvl.setStatus("current")
_AdVqmActCallBurstRLq_Type = Unsigned32
_AdVqmActCallBurstRLq_Object = MibTableColumn
adVqmActCallBurstRLq = _AdVqmActCallBurstRLq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 54),
    _AdVqmActCallBurstRLq_Type()
)
adVqmActCallBurstRLq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallBurstRLq.setStatus("current")
_AdVqmActCallBurstCount_Type = Counter32
_AdVqmActCallBurstCount_Object = MibTableColumn
adVqmActCallBurstCount = _AdVqmActCallBurstCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 55),
    _AdVqmActCallBurstCount_Type()
)
adVqmActCallBurstCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallBurstCount.setStatus("current")
_AdVqmActCallBurstRateAvg_Type = Percentage
_AdVqmActCallBurstRateAvg_Object = MibTableColumn
adVqmActCallBurstRateAvg = _AdVqmActCallBurstRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 56),
    _AdVqmActCallBurstRateAvg_Type()
)
adVqmActCallBurstRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallBurstRateAvg.setStatus("current")
_AdVqmActCallBurstLenAvgPkts_Type = Unsigned32
_AdVqmActCallBurstLenAvgPkts_Object = MibTableColumn
adVqmActCallBurstLenAvgPkts = _AdVqmActCallBurstLenAvgPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 57),
    _AdVqmActCallBurstLenAvgPkts_Type()
)
adVqmActCallBurstLenAvgPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallBurstLenAvgPkts.setStatus("current")
_AdVqmActCallBurstLenAvgMsec_Type = Unsigned32
_AdVqmActCallBurstLenAvgMsec_Object = MibTableColumn
adVqmActCallBurstLenAvgMsec = _AdVqmActCallBurstLenAvgMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 58),
    _AdVqmActCallBurstLenAvgMsec_Type()
)
adVqmActCallBurstLenAvgMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallBurstLenAvgMsec.setStatus("current")
_AdVqmActCallGapR_Type = Unsigned32
_AdVqmActCallGapR_Object = MibTableColumn
adVqmActCallGapR = _AdVqmActCallGapR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 59),
    _AdVqmActCallGapR_Type()
)
adVqmActCallGapR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallGapR.setStatus("current")
_AdVqmActCallGapCount_Type = Counter32
_AdVqmActCallGapCount_Object = MibTableColumn
adVqmActCallGapCount = _AdVqmActCallGapCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 60),
    _AdVqmActCallGapCount_Type()
)
adVqmActCallGapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallGapCount.setStatus("current")
_AdVqmActCallGapLossRateAvg_Type = Percentage
_AdVqmActCallGapLossRateAvg_Object = MibTableColumn
adVqmActCallGapLossRateAvg = _AdVqmActCallGapLossRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 61),
    _AdVqmActCallGapLossRateAvg_Type()
)
adVqmActCallGapLossRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallGapLossRateAvg.setStatus("current")
_AdVqmActCallGapLenPkts_Type = Unsigned32
_AdVqmActCallGapLenPkts_Object = MibTableColumn
adVqmActCallGapLenPkts = _AdVqmActCallGapLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 62),
    _AdVqmActCallGapLenPkts_Type()
)
adVqmActCallGapLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallGapLenPkts.setStatus("current")
_AdVqmActCallGapLenMsec_Type = Unsigned32
_AdVqmActCallGapLenMsec_Object = MibTableColumn
adVqmActCallGapLenMsec = _AdVqmActCallGapLenMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 63),
    _AdVqmActCallGapLenMsec_Type()
)
adVqmActCallGapLenMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallGapLenMsec.setStatus("current")
_AdVqmActCallLossRateAvg_Type = Percentage
_AdVqmActCallLossRateAvg_Object = MibTableColumn
adVqmActCallLossRateAvg = _AdVqmActCallLossRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 64),
    _AdVqmActCallLossRateAvg_Type()
)
adVqmActCallLossRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallLossRateAvg.setStatus("current")
_AdVqmActCallNetworkLossAvg_Type = Percentage
_AdVqmActCallNetworkLossAvg_Object = MibTableColumn
adVqmActCallNetworkLossAvg = _AdVqmActCallNetworkLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 65),
    _AdVqmActCallNetworkLossAvg_Type()
)
adVqmActCallNetworkLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallNetworkLossAvg.setStatus("current")
_AdVqmActCallDiscardRateAvg_Type = Percentage
_AdVqmActCallDiscardRateAvg_Object = MibTableColumn
adVqmActCallDiscardRateAvg = _AdVqmActCallDiscardRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 66),
    _AdVqmActCallDiscardRateAvg_Type()
)
adVqmActCallDiscardRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDiscardRateAvg.setStatus("current")
_AdVqmActCallExcessBurst_Type = Unsigned32
_AdVqmActCallExcessBurst_Object = MibTableColumn
adVqmActCallExcessBurst = _AdVqmActCallExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 67),
    _AdVqmActCallExcessBurst_Type()
)
adVqmActCallExcessBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallExcessBurst.setStatus("current")
_AdVqmActCallExcessGap_Type = Unsigned32
_AdVqmActCallExcessGap_Object = MibTableColumn
adVqmActCallExcessGap = _AdVqmActCallExcessGap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 68),
    _AdVqmActCallExcessGap_Type()
)
adVqmActCallExcessGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallExcessGap.setStatus("current")
_AdVqmActCallPpdvMsec_Type = MsecValue
_AdVqmActCallPpdvMsec_Object = MibTableColumn
adVqmActCallPpdvMsec = _AdVqmActCallPpdvMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 69),
    _AdVqmActCallPpdvMsec_Type()
)
adVqmActCallPpdvMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallPpdvMsec.setStatus("current")
_AdVqmActCallLateThresholdMs_Type = MsecValue
_AdVqmActCallLateThresholdMs_Object = MibTableColumn
adVqmActCallLateThresholdMs = _AdVqmActCallLateThresholdMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 70),
    _AdVqmActCallLateThresholdMs_Type()
)
adVqmActCallLateThresholdMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallLateThresholdMs.setStatus("current")
_AdVqmActCallLateThresholdPc_Type = Percentage
_AdVqmActCallLateThresholdPc_Object = MibTableColumn
adVqmActCallLateThresholdPc = _AdVqmActCallLateThresholdPc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 71),
    _AdVqmActCallLateThresholdPc_Type()
)
adVqmActCallLateThresholdPc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallLateThresholdPc.setStatus("current")
_AdVqmActCallLateUnderThresh_Type = Counter32
_AdVqmActCallLateUnderThresh_Object = MibTableColumn
adVqmActCallLateUnderThresh = _AdVqmActCallLateUnderThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 72),
    _AdVqmActCallLateUnderThresh_Type()
)
adVqmActCallLateUnderThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallLateUnderThresh.setStatus("current")
_AdVqmActCallLateTotalCount_Type = Counter32
_AdVqmActCallLateTotalCount_Object = MibTableColumn
adVqmActCallLateTotalCount = _AdVqmActCallLateTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 73),
    _AdVqmActCallLateTotalCount_Type()
)
adVqmActCallLateTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallLateTotalCount.setStatus("current")
_AdVqmActCallLatePeakJitterMs_Type = MsecValue
_AdVqmActCallLatePeakJitterMs_Object = MibTableColumn
adVqmActCallLatePeakJitterMs = _AdVqmActCallLatePeakJitterMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 74),
    _AdVqmActCallLatePeakJitterMs_Type()
)
adVqmActCallLatePeakJitterMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallLatePeakJitterMs.setStatus("current")
_AdVqmActCallEarlyThreshMs_Type = MsecValue
_AdVqmActCallEarlyThreshMs_Object = MibTableColumn
adVqmActCallEarlyThreshMs = _AdVqmActCallEarlyThreshMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 75),
    _AdVqmActCallEarlyThreshMs_Type()
)
adVqmActCallEarlyThreshMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallEarlyThreshMs.setStatus("current")
_AdVqmActCallEarlyThreshPc_Type = Percentage
_AdVqmActCallEarlyThreshPc_Object = MibTableColumn
adVqmActCallEarlyThreshPc = _AdVqmActCallEarlyThreshPc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 76),
    _AdVqmActCallEarlyThreshPc_Type()
)
adVqmActCallEarlyThreshPc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallEarlyThreshPc.setStatus("current")
_AdVqmActCallEarlyUnderThresh_Type = Counter32
_AdVqmActCallEarlyUnderThresh_Object = MibTableColumn
adVqmActCallEarlyUnderThresh = _AdVqmActCallEarlyUnderThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 77),
    _AdVqmActCallEarlyUnderThresh_Type()
)
adVqmActCallEarlyUnderThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallEarlyUnderThresh.setStatus("current")
_AdVqmActCallEarlyTotalCount_Type = Counter32
_AdVqmActCallEarlyTotalCount_Object = MibTableColumn
adVqmActCallEarlyTotalCount = _AdVqmActCallEarlyTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 78),
    _AdVqmActCallEarlyTotalCount_Type()
)
adVqmActCallEarlyTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallEarlyTotalCount.setStatus("current")
_AdVqmActCallEarlyPeakJitterMs_Type = MsecValue
_AdVqmActCallEarlyPeakJitterMs_Object = MibTableColumn
adVqmActCallEarlyPeakJitterMs = _AdVqmActCallEarlyPeakJitterMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 79),
    _AdVqmActCallEarlyPeakJitterMs_Type()
)
adVqmActCallEarlyPeakJitterMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallEarlyPeakJitterMs.setStatus("current")
_AdVqmActCallDelayIncreaseCount_Type = Counter32
_AdVqmActCallDelayIncreaseCount_Object = MibTableColumn
adVqmActCallDelayIncreaseCount = _AdVqmActCallDelayIncreaseCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 80),
    _AdVqmActCallDelayIncreaseCount_Type()
)
adVqmActCallDelayIncreaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDelayIncreaseCount.setStatus("current")
_AdVqmActCallDelayDecreaseCount_Type = Counter32
_AdVqmActCallDelayDecreaseCount_Object = MibTableColumn
adVqmActCallDelayDecreaseCount = _AdVqmActCallDelayDecreaseCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 81),
    _AdVqmActCallDelayDecreaseCount_Type()
)
adVqmActCallDelayDecreaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDelayDecreaseCount.setStatus("current")
_AdVqmActCallResyncCount_Type = Counter32
_AdVqmActCallResyncCount_Object = MibTableColumn
adVqmActCallResyncCount = _AdVqmActCallResyncCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 82),
    _AdVqmActCallResyncCount_Type()
)
adVqmActCallResyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallResyncCount.setStatus("current")


class _AdVqmActCallJitterBufferType_Type(Integer32):
    """Custom type adVqmActCallJitterBufferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1),
          ("unknown", 3))
    )


_AdVqmActCallJitterBufferType_Type.__name__ = "Integer32"
_AdVqmActCallJitterBufferType_Object = MibTableColumn
adVqmActCallJitterBufferType = _AdVqmActCallJitterBufferType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 83),
    _AdVqmActCallJitterBufferType_Type()
)
adVqmActCallJitterBufferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallJitterBufferType.setStatus("current")
_AdVqmActCallJbCfgMin_Type = Unsigned32
_AdVqmActCallJbCfgMin_Object = MibTableColumn
adVqmActCallJbCfgMin = _AdVqmActCallJbCfgMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 84),
    _AdVqmActCallJbCfgMin_Type()
)
adVqmActCallJbCfgMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallJbCfgMin.setStatus("current")
_AdVqmActCallJbCfgNom_Type = Unsigned32
_AdVqmActCallJbCfgNom_Object = MibTableColumn
adVqmActCallJbCfgNom = _AdVqmActCallJbCfgNom_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 85),
    _AdVqmActCallJbCfgNom_Type()
)
adVqmActCallJbCfgNom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallJbCfgNom.setStatus("current")
_AdVqmActCallJbCfgMax_Type = Unsigned32
_AdVqmActCallJbCfgMax_Object = MibTableColumn
adVqmActCallJbCfgMax = _AdVqmActCallJbCfgMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 86),
    _AdVqmActCallJbCfgMax_Type()
)
adVqmActCallJbCfgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallJbCfgMax.setStatus("current")
_AdVqmActCallDuplicatePkts_Type = Counter32
_AdVqmActCallDuplicatePkts_Object = MibTableColumn
adVqmActCallDuplicatePkts = _AdVqmActCallDuplicatePkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 87),
    _AdVqmActCallDuplicatePkts_Type()
)
adVqmActCallDuplicatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDuplicatePkts.setStatus("current")
_AdVqmActCallEarlyPkts_Type = Counter32
_AdVqmActCallEarlyPkts_Object = MibTableColumn
adVqmActCallEarlyPkts = _AdVqmActCallEarlyPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 88),
    _AdVqmActCallEarlyPkts_Type()
)
adVqmActCallEarlyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallEarlyPkts.setStatus("current")
_AdVqmActCallLatePkts_Type = Counter32
_AdVqmActCallLatePkts_Object = MibTableColumn
adVqmActCallLatePkts = _AdVqmActCallLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 89),
    _AdVqmActCallLatePkts_Type()
)
adVqmActCallLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallLatePkts.setStatus("current")
_AdVqmActCallOverrunDiscardPkts_Type = Counter32
_AdVqmActCallOverrunDiscardPkts_Object = MibTableColumn
adVqmActCallOverrunDiscardPkts = _AdVqmActCallOverrunDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 90),
    _AdVqmActCallOverrunDiscardPkts_Type()
)
adVqmActCallOverrunDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallOverrunDiscardPkts.setStatus("current")
_AdVqmActCallUnderrunDiscardPkts_Type = Counter32
_AdVqmActCallUnderrunDiscardPkts_Object = MibTableColumn
adVqmActCallUnderrunDiscardPkts = _AdVqmActCallUnderrunDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 91),
    _AdVqmActCallUnderrunDiscardPkts_Type()
)
adVqmActCallUnderrunDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallUnderrunDiscardPkts.setStatus("current")
_AdVqmActCallDelayMinMsec_Type = Unsigned32
_AdVqmActCallDelayMinMsec_Object = MibTableColumn
adVqmActCallDelayMinMsec = _AdVqmActCallDelayMinMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 92),
    _AdVqmActCallDelayMinMsec_Type()
)
adVqmActCallDelayMinMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDelayMinMsec.setStatus("current")
_AdVqmActCallDelayAvgMsec_Type = Unsigned32
_AdVqmActCallDelayAvgMsec_Object = MibTableColumn
adVqmActCallDelayAvgMsec = _AdVqmActCallDelayAvgMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 93),
    _AdVqmActCallDelayAvgMsec_Type()
)
adVqmActCallDelayAvgMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDelayAvgMsec.setStatus("current")
_AdVqmActCallDelayMaxMsec_Type = Unsigned32
_AdVqmActCallDelayMaxMsec_Object = MibTableColumn
adVqmActCallDelayMaxMsec = _AdVqmActCallDelayMaxMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 94),
    _AdVqmActCallDelayMaxMsec_Type()
)
adVqmActCallDelayMaxMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDelayMaxMsec.setStatus("current")
_AdVqmActCallDelayCurrentMsec_Type = Unsigned32
_AdVqmActCallDelayCurrentMsec_Object = MibTableColumn
adVqmActCallDelayCurrentMsec = _AdVqmActCallDelayCurrentMsec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 95),
    _AdVqmActCallDelayCurrentMsec_Type()
)
adVqmActCallDelayCurrentMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallDelayCurrentMsec.setStatus("current")
_AdVqmActCallExtRLqIn_Type = Integer32
_AdVqmActCallExtRLqIn_Object = MibTableColumn
adVqmActCallExtRLqIn = _AdVqmActCallExtRLqIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 96),
    _AdVqmActCallExtRLqIn_Type()
)
adVqmActCallExtRLqIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallExtRLqIn.setStatus("current")
_AdVqmActCallExtRLqOut_Type = Integer32
_AdVqmActCallExtRLqOut_Object = MibTableColumn
adVqmActCallExtRLqOut = _AdVqmActCallExtRLqOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 97),
    _AdVqmActCallExtRLqOut_Type()
)
adVqmActCallExtRLqOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallExtRLqOut.setStatus("current")
_AdVqmActCallExtRCqIn_Type = Integer32
_AdVqmActCallExtRCqIn_Object = MibTableColumn
adVqmActCallExtRCqIn = _AdVqmActCallExtRCqIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 98),
    _AdVqmActCallExtRCqIn_Type()
)
adVqmActCallExtRCqIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallExtRCqIn.setStatus("current")
_AdVqmActCallExtRCqOut_Type = Integer32
_AdVqmActCallExtRCqOut_Object = MibTableColumn
adVqmActCallExtRCqOut = _AdVqmActCallExtRCqOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 99),
    _AdVqmActCallExtRCqOut_Type()
)
adVqmActCallExtRCqOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallExtRCqOut.setStatus("current")
_AdVqmActCallThroughPutIndex_Type = Unsigned32
_AdVqmActCallThroughPutIndex_Object = MibTableColumn
adVqmActCallThroughPutIndex = _AdVqmActCallThroughPutIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 100),
    _AdVqmActCallThroughPutIndex_Type()
)
adVqmActCallThroughPutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallThroughPutIndex.setStatus("current")
_AdVqmActCallReliabilityIndex_Type = Unsigned32
_AdVqmActCallReliabilityIndex_Object = MibTableColumn
adVqmActCallReliabilityIndex = _AdVqmActCallReliabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 101),
    _AdVqmActCallReliabilityIndex_Type()
)
adVqmActCallReliabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallReliabilityIndex.setStatus("current")
_AdVqmActCallBitrate_Type = Unsigned32
_AdVqmActCallBitrate_Object = MibTableColumn
adVqmActCallBitrate = _AdVqmActCallBitrate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 8, 1, 1, 102),
    _AdVqmActCallBitrate_Type()
)
adVqmActCallBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adVqmActCallBitrate.setStatus("current")
_AdGenAOSVqmConformance_ObjectIdentity = ObjectIdentity
adGenAOSVqmConformance = _AdGenAOSVqmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10)
)
_AdGenAOSVqmGroups_ObjectIdentity = ObjectIdentity
adGenAOSVqmGroups = _AdGenAOSVqmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1)
)
_AdGenAOSVqmCompliances_ObjectIdentity = ObjectIdentity
adGenAOSVqmCompliances = _AdGenAOSVqmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 2)
)

# Managed Objects groups

adVQMCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 1)
)
adVQMCfgGroup.setObjects(
      *(("ADTRAN-AOS-VQM", "adVqmCfgEnable"),
        ("ADTRAN-AOS-VQM", "adVqmCfgSipEnable"),
        ("ADTRAN-AOS-VQM", "adVqmCfgUdpEnable"),
        ("ADTRAN-AOS-VQM", "adVqmCfgInternationalCode"),
        ("ADTRAN-AOS-VQM", "adVqmCfgJitterBufferType"),
        ("ADTRAN-AOS-VQM", "adVqmCfgJitterBufferAdaptiveMin"),
        ("ADTRAN-AOS-VQM", "adVqmCfgJitterBufferAdaptiveNominal"),
        ("ADTRAN-AOS-VQM", "adVqmCfgJitterBufferAdaptiveMax"),
        ("ADTRAN-AOS-VQM", "adVqmCfgJitterBufferFixedNominal"),
        ("ADTRAN-AOS-VQM", "adVqmCfgJitterBufferFixedSize"),
        ("ADTRAN-AOS-VQM", "adVqmCfgJitterBufferThresholdEarlyMs"),
        ("ADTRAN-AOS-VQM", "adVqmCfgJitterBufferThresholdLateMs"),
        ("ADTRAN-AOS-VQM", "adVqmCfgRoundTripPingEnabled"),
        ("ADTRAN-AOS-VQM", "adVqmCfgRoundTripPingType"),
        ("ADTRAN-AOS-VQM", "adVqmCfgCallHistorySize"),
        ("ADTRAN-AOS-VQM", "adVqmCfgHistoryThresholdLqmos"),
        ("ADTRAN-AOS-VQM", "adVqmCfgHistoryThresholdCqmos"),
        ("ADTRAN-AOS-VQM", "adVqmCfgHistoryThresholdPqmos"),
        ("ADTRAN-AOS-VQM", "adVqmCfgHistoryThresholdLoss"),
        ("ADTRAN-AOS-VQM", "adVqmCfgHistoryThresholdOutOfOrder"),
        ("ADTRAN-AOS-VQM", "adVqmCfgHistoryThresholdJitter"),
        ("ADTRAN-AOS-VQM", "adVqmCfgClear"),
        ("ADTRAN-AOS-VQM", "adVqmCfgClearCallHistory"))
)
if mibBuilder.loadTexts:
    adVQMCfgGroup.setStatus("current")

adVQMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 2)
)
adVQMThresholdGroup.setObjects(
      *(("ADTRAN-AOS-VQM", "adVqmThresholdLqmosInfo"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdLqmosNotice"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdLqmosWarning"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdLqmosError"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdPqmosInfo"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdPqmosNotice"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdPqmosWarning"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdPqmosError"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdOutOfOrderInfo"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdOutOfOrderNotice"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdOutOfOrderWarning"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdOutOfOrderError"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdLossInfo"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdLossNotice"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdLossWarning"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdLossError"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdJitterInfo"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdJitterNotice"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdJitterWarning"),
        ("ADTRAN-AOS-VQM", "adVqmThresholdJitterError"))
)
if mibBuilder.loadTexts:
    adVQMThresholdGroup.setStatus("current")

adVQMSysPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 3)
)
adVQMSysPerfGroup.setObjects(
      *(("ADTRAN-AOS-VQM", "adVqmSysActiveCalls"),
        ("ADTRAN-AOS-VQM", "adVqmSysActiveExcellent"),
        ("ADTRAN-AOS-VQM", "adVqmSysActiveGood"),
        ("ADTRAN-AOS-VQM", "adVqmSysActiveFair"),
        ("ADTRAN-AOS-VQM", "adVqmSysActivePoor"),
        ("ADTRAN-AOS-VQM", "adVqmSysCallHistoryCalls"),
        ("ADTRAN-AOS-VQM", "adVqmSysCallHistoryExcellent"),
        ("ADTRAN-AOS-VQM", "adVqmSysCallHistoryGood"),
        ("ADTRAN-AOS-VQM", "adVqmSysCallHistoryFair"),
        ("ADTRAN-AOS-VQM", "adVqmSysCallHistoryPoor"),
        ("ADTRAN-AOS-VQM", "adVqmSysAllCallsExcellent"),
        ("ADTRAN-AOS-VQM", "adVqmSysAllCallsGood"),
        ("ADTRAN-AOS-VQM", "adVqmSysAllCallsFair"),
        ("ADTRAN-AOS-VQM", "adVqmSysAllCallsPoor"))
)
if mibBuilder.loadTexts:
    adVQMSysPerfGroup.setStatus("current")

adVQMInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 4)
)
adVQMInterfaceGroup.setObjects(
      *(("ADTRAN-AOS-VQM", "adVqmIfcId"),
        ("ADTRAN-AOS-VQM", "adVqmIfcName"),
        ("ADTRAN-AOS-VQM", "adVqmIfcPktsRx"),
        ("ADTRAN-AOS-VQM", "adVqmIfcPktsLost"),
        ("ADTRAN-AOS-VQM", "adVqmIfcPktsOoo"),
        ("ADTRAN-AOS-VQM", "adVqmIfcPktsDiscarded"),
        ("ADTRAN-AOS-VQM", "adVqmIfcNumberActiveCalls"),
        ("ADTRAN-AOS-VQM", "adVqmIfcTerminatedCalls"),
        ("ADTRAN-AOS-VQM", "adVqmIfcRLqMinimum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcRLqAverage"),
        ("ADTRAN-AOS-VQM", "adVqmIfcRLqMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcRCqMinimum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcRCqAverage"),
        ("ADTRAN-AOS-VQM", "adVqmIfcRCqMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcRG107Minimum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcRG107Average"),
        ("ADTRAN-AOS-VQM", "adVqmIfcRG107Maximum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcMosLqMinimum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcMosLqAverage"),
        ("ADTRAN-AOS-VQM", "adVqmIfcMosLqMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcMosCqMinimum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcMosCqAverage"),
        ("ADTRAN-AOS-VQM", "adVqmIfcMosCqMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcMosPqMinimum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcMosPqAverage"),
        ("ADTRAN-AOS-VQM", "adVqmIfcMosPqMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcLossMinimum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcLossAverage"),
        ("ADTRAN-AOS-VQM", "adVqmIfcLossMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcDiscardsMinimum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcDiscardsAverage"),
        ("ADTRAN-AOS-VQM", "adVqmIfcDiscardsMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmIfcPdvAverageMs"),
        ("ADTRAN-AOS-VQM", "adVqmIfcPdvMaximumMs"),
        ("ADTRAN-AOS-VQM", "adVqmIfcDelayMinMsec"),
        ("ADTRAN-AOS-VQM", "adVqmIfcDelayAvgMsec"),
        ("ADTRAN-AOS-VQM", "adVqmIfcDelayMaxMsec"),
        ("ADTRAN-AOS-VQM", "adVqmIfcNumberStreamsExcellent"),
        ("ADTRAN-AOS-VQM", "adVqmIfcNumberStreamsGood"),
        ("ADTRAN-AOS-VQM", "adVqmIfcNumberStreamsFair"),
        ("ADTRAN-AOS-VQM", "adVqmIfcNumberStreamsPoor"),
        ("ADTRAN-AOS-VQM", "adVqmIfcClear"))
)
if mibBuilder.loadTexts:
    adVQMInterfaceGroup.setStatus("current")

adVQMEndPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 5)
)
adVQMEndPointGroup.setObjects(
      *(("ADTRAN-AOS-VQM", "adVqmEndPointRtpSourceIp"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointNumberCompletedCalls"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointInterfaceId"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointInterfaceName"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointMosLqMinimum"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointMosLqAverage"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointMosLqMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointMosPqMinimum"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointMosPqAverage"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointMosPqMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointPktsLostTotal"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointPktsOutOfOrder"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointJitterMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointNumberStreamsExcellent"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointNumberStreamsGood"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointNumberStreamsFair"),
        ("ADTRAN-AOS-VQM", "adVqmEndPointNumberStreamsPoor"))
)
if mibBuilder.loadTexts:
    adVQMEndPointGroup.setStatus("current")

adVQMCallHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 6)
)
adVQMCallHistoryGroup.setObjects(
      *(("ADTRAN-AOS-VQM", "adVqmCallHistRtpSourceIp"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistRtpSourcePort"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistRtpDestIp"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistRtpDestPort"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistSsrcid"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistTo"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistFrom"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistRtpSourceUri"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistCallid"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistCcmid"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistSourceIntName"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDestIntName"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistSourceIntDescription"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDestIntDescription"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistCallStart"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistCallDurationMs"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistCodec"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistCodecClass"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDscp"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistPktsRcvdTotal"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistPktsLostTotal"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistPktsDiscardedTotal"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistOutOfOrder"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistPdvAverageMs"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistPdvMaximumMs"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistRtDelayInst"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistRtDelayAverage"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistRtDelayMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistOnewayDelayInst"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistOnewayDelayAverage"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistOnewayDelayMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistOrigDelayInst"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistOrigDelayAverage"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistOrigDelayMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistTermDelayMinimum"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistTermDelayAverage"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistTermDelayMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistRLq"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistRCq"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistRNominal"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistRG107"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistMosLq"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistMosCq"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistMosPq"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistMosNominal"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDegLoss"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDegDiscard"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDegVocoder"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDegRecency"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDegDelay"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDegSiglvl"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDegNoiselvl"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDegEcholvl"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistBurstRLq"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistBurstCount"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistBurstRateAvg"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistBurstLenAvgPkts"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistBurstLenAvgMsec"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistGapR"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistGapCount"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistGapLossRateAvg"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistGapLenPkts"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistGapLenMsec"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistLossRateAvg"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistNetworkLossAvg"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDiscardRateAvg"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistExcessBurst"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistExcessGap"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistPpdvMsec"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistLateThresholdMs"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistLateThresholdPc"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistLateUnderThresh"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistLateTotalCount"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistLatePeakJitterMs"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistEarlyThreshMs"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistEarlyThreshPc"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistEarlyUnderThresh"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistEarlyTotalCount"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistEarlyPeakJitterMs"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDelayIncreaseCount"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDelayDecreaseCount"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistResyncCount"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistJitterBufferType"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistJbCfgMin"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistJbCfgNom"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistJbCfgMax"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDuplicatePkts"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistEarlyPkts"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistLatePkts"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistOverrunDiscardPkts"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistUnderrunDiscardPkts"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDelayMinMsec"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDelayAvgMsec"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDelayMaxMsec"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistDelayCurrentMsec"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistExtRLqIn"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistExtRLqOut"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistExtRCqIn"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistExtRCqOut"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistThroughPutIndex"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistReliabilityIndex"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistBitrate"))
)
if mibBuilder.loadTexts:
    adVQMCallHistoryGroup.setStatus("current")

adVQMActiveCallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 7)
)
adVQMActiveCallGroup.setObjects(
      *(("ADTRAN-AOS-VQM", "adVqmActCallRtpSourceIp"),
        ("ADTRAN-AOS-VQM", "adVqmActCallRtpSourcePort"),
        ("ADTRAN-AOS-VQM", "adVqmActCallRtpDestIp"),
        ("ADTRAN-AOS-VQM", "adVqmActCallRtpDestPort"),
        ("ADTRAN-AOS-VQM", "adVqmActCallSsrcid"),
        ("ADTRAN-AOS-VQM", "adVqmActCallTo"),
        ("ADTRAN-AOS-VQM", "adVqmActCallFrom"),
        ("ADTRAN-AOS-VQM", "adVqmActCallRtpSourceUri"),
        ("ADTRAN-AOS-VQM", "adVqmActCallCallid"),
        ("ADTRAN-AOS-VQM", "adVqmActCallCcmid"),
        ("ADTRAN-AOS-VQM", "adVqmActCallSourceIntName"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDestIntName"),
        ("ADTRAN-AOS-VQM", "adVqmActCallSourceIntDescription"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDestIntDescription"),
        ("ADTRAN-AOS-VQM", "adVqmActCallCallStart"),
        ("ADTRAN-AOS-VQM", "adVqmActCallCallDurationMs"),
        ("ADTRAN-AOS-VQM", "adVqmActCallCodec"),
        ("ADTRAN-AOS-VQM", "adVqmActCallCodecClass"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDscp"),
        ("ADTRAN-AOS-VQM", "adVqmActCallPktsRcvdTotal"),
        ("ADTRAN-AOS-VQM", "adVqmActCallPktsLostTotal"),
        ("ADTRAN-AOS-VQM", "adVqmActCallPktsDiscardedTotal"),
        ("ADTRAN-AOS-VQM", "adVqmActCallOutOfOrder"),
        ("ADTRAN-AOS-VQM", "adVqmActCallPdvAverageMs"),
        ("ADTRAN-AOS-VQM", "adVqmActCallPdvMaximumMs"),
        ("ADTRAN-AOS-VQM", "adVqmActCallRtDelayInst"),
        ("ADTRAN-AOS-VQM", "adVqmActCallRtDelayAverage"),
        ("ADTRAN-AOS-VQM", "adVqmActCallRtDelayMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmActCallOnewayDelayInst"),
        ("ADTRAN-AOS-VQM", "adVqmActCallOnewayDelayAverage"),
        ("ADTRAN-AOS-VQM", "adVqmActCallOnewayDelayMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmActCallOrigDelayInst"),
        ("ADTRAN-AOS-VQM", "adVqmActCallOrigDelayAverage"),
        ("ADTRAN-AOS-VQM", "adVqmActCallOrigDelayMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmActCallTermDelayMinimum"),
        ("ADTRAN-AOS-VQM", "adVqmActCallTermDelayAverage"),
        ("ADTRAN-AOS-VQM", "adVqmActCallTermDelayMaximum"),
        ("ADTRAN-AOS-VQM", "adVqmActCallRLq"),
        ("ADTRAN-AOS-VQM", "adVqmActCallRCq"),
        ("ADTRAN-AOS-VQM", "adVqmActCallRNominal"),
        ("ADTRAN-AOS-VQM", "adVqmActCallRG107"),
        ("ADTRAN-AOS-VQM", "adVqmActCallMosLq"),
        ("ADTRAN-AOS-VQM", "adVqmActCallMosCq"),
        ("ADTRAN-AOS-VQM", "adVqmActCallMosPq"),
        ("ADTRAN-AOS-VQM", "adVqmActCallMosNominal"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDegLoss"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDegDiscard"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDegVocoder"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDegRecency"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDegDelay"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDegSiglvl"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDegNoiselvl"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDegEcholvl"),
        ("ADTRAN-AOS-VQM", "adVqmActCallBurstRLq"),
        ("ADTRAN-AOS-VQM", "adVqmActCallBurstCount"),
        ("ADTRAN-AOS-VQM", "adVqmActCallBurstRateAvg"),
        ("ADTRAN-AOS-VQM", "adVqmActCallBurstLenAvgPkts"),
        ("ADTRAN-AOS-VQM", "adVqmActCallBurstLenAvgMsec"),
        ("ADTRAN-AOS-VQM", "adVqmActCallGapR"),
        ("ADTRAN-AOS-VQM", "adVqmActCallGapCount"),
        ("ADTRAN-AOS-VQM", "adVqmActCallGapLossRateAvg"),
        ("ADTRAN-AOS-VQM", "adVqmActCallGapLenPkts"),
        ("ADTRAN-AOS-VQM", "adVqmActCallGapLenMsec"),
        ("ADTRAN-AOS-VQM", "adVqmActCallLossRateAvg"),
        ("ADTRAN-AOS-VQM", "adVqmActCallNetworkLossAvg"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDiscardRateAvg"),
        ("ADTRAN-AOS-VQM", "adVqmActCallExcessBurst"),
        ("ADTRAN-AOS-VQM", "adVqmActCallExcessGap"),
        ("ADTRAN-AOS-VQM", "adVqmActCallPpdvMsec"),
        ("ADTRAN-AOS-VQM", "adVqmActCallLateThresholdMs"),
        ("ADTRAN-AOS-VQM", "adVqmActCallLateThresholdPc"),
        ("ADTRAN-AOS-VQM", "adVqmActCallLateUnderThresh"),
        ("ADTRAN-AOS-VQM", "adVqmActCallLateTotalCount"),
        ("ADTRAN-AOS-VQM", "adVqmActCallLatePeakJitterMs"),
        ("ADTRAN-AOS-VQM", "adVqmActCallEarlyThreshMs"),
        ("ADTRAN-AOS-VQM", "adVqmActCallEarlyThreshPc"),
        ("ADTRAN-AOS-VQM", "adVqmActCallEarlyUnderThresh"),
        ("ADTRAN-AOS-VQM", "adVqmActCallEarlyTotalCount"),
        ("ADTRAN-AOS-VQM", "adVqmActCallEarlyPeakJitterMs"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDelayIncreaseCount"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDelayDecreaseCount"),
        ("ADTRAN-AOS-VQM", "adVqmActCallResyncCount"),
        ("ADTRAN-AOS-VQM", "adVqmActCallJitterBufferType"),
        ("ADTRAN-AOS-VQM", "adVqmActCallJbCfgMin"),
        ("ADTRAN-AOS-VQM", "adVqmActCallJbCfgNom"),
        ("ADTRAN-AOS-VQM", "adVqmActCallJbCfgMax"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDuplicatePkts"),
        ("ADTRAN-AOS-VQM", "adVqmActCallEarlyPkts"),
        ("ADTRAN-AOS-VQM", "adVqmActCallLatePkts"),
        ("ADTRAN-AOS-VQM", "adVqmActCallOverrunDiscardPkts"),
        ("ADTRAN-AOS-VQM", "adVqmActCallUnderrunDiscardPkts"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDelayMinMsec"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDelayAvgMsec"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDelayMaxMsec"),
        ("ADTRAN-AOS-VQM", "adVqmActCallDelayCurrentMsec"),
        ("ADTRAN-AOS-VQM", "adVqmActCallExtRLqIn"),
        ("ADTRAN-AOS-VQM", "adVqmActCallExtRLqOut"),
        ("ADTRAN-AOS-VQM", "adVqmActCallExtRCqIn"),
        ("ADTRAN-AOS-VQM", "adVqmActCallExtRCqOut"),
        ("ADTRAN-AOS-VQM", "adVqmActCallThroughPutIndex"),
        ("ADTRAN-AOS-VQM", "adVqmActCallReliabilityIndex"),
        ("ADTRAN-AOS-VQM", "adVqmActCallBitrate"))
)
if mibBuilder.loadTexts:
    adVQMActiveCallGroup.setStatus("current")

adVQMTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 8)
)
adVQMTrapGroup.setObjects(
      *(("ADTRAN-AOS-VQM", "adVqmTrapState"),
        ("ADTRAN-AOS-VQM", "adVqmTrapCfgSeverityLevel"),
        ("ADTRAN-AOS-VQM", "adVqmTrapEventType"))
)
if mibBuilder.loadTexts:
    adVQMTrapGroup.setStatus("current")


# Notification objects

adVQMEndOfCallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 3, 0, 1)
)
adVQMEndOfCallTrap.setObjects(
      *(("ADTRAN-AOS-VQM", "adVqmTrapEventType"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistMosLq"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistMosPq"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistPktsLostTotal"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistOutOfOrder"),
        ("ADTRAN-AOS-VQM", "adVqmCallHistPdvAverageMs"))
)
if mibBuilder.loadTexts:
    adVQMEndOfCallTrap.setStatus(
        "current"
    )


# Notifications groups

adVQMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 9)
)
adVQMNotificationGroup.setObjects(
    ("ADTRAN-AOS-VQM", "adVQMEndOfCallTrap")
)
if mibBuilder.loadTexts:
    adVQMNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adGenAOSVqmFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOSVqmFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-VQM",
    **{"MOSvalue": MOSvalue,
       "Percentage": Percentage,
       "MsecValue": MsecValue,
       "adVQM": adVQM,
       "adVQMTrap": adVQMTrap,
       "adVQMEndOfCallTrap": adVQMEndOfCallTrap,
       "adVQMTrapControl": adVQMTrapControl,
       "adVqmTrapState": adVqmTrapState,
       "adVqmTrapCfgSeverityLevel": adVqmTrapCfgSeverityLevel,
       "adVqmTrapEventType": adVqmTrapEventType,
       "adVQMCfg": adVQMCfg,
       "adVqmCfgEnable": adVqmCfgEnable,
       "adVqmCfgSipEnable": adVqmCfgSipEnable,
       "adVqmCfgUdpEnable": adVqmCfgUdpEnable,
       "adVqmCfgInternationalCode": adVqmCfgInternationalCode,
       "adVqmCfgJitterBufferType": adVqmCfgJitterBufferType,
       "adVqmCfgJitterBufferAdaptiveMin": adVqmCfgJitterBufferAdaptiveMin,
       "adVqmCfgJitterBufferAdaptiveNominal": adVqmCfgJitterBufferAdaptiveNominal,
       "adVqmCfgJitterBufferAdaptiveMax": adVqmCfgJitterBufferAdaptiveMax,
       "adVqmCfgJitterBufferFixedNominal": adVqmCfgJitterBufferFixedNominal,
       "adVqmCfgJitterBufferFixedSize": adVqmCfgJitterBufferFixedSize,
       "adVqmCfgJitterBufferThresholdEarlyMs": adVqmCfgJitterBufferThresholdEarlyMs,
       "adVqmCfgJitterBufferThresholdLateMs": adVqmCfgJitterBufferThresholdLateMs,
       "adVqmCfgRoundTripPingEnabled": adVqmCfgRoundTripPingEnabled,
       "adVqmCfgRoundTripPingType": adVqmCfgRoundTripPingType,
       "adVqmCfgCallHistorySize": adVqmCfgCallHistorySize,
       "adVqmCfgHistoryThresholdLqmos": adVqmCfgHistoryThresholdLqmos,
       "adVqmCfgHistoryThresholdCqmos": adVqmCfgHistoryThresholdCqmos,
       "adVqmCfgHistoryThresholdPqmos": adVqmCfgHistoryThresholdPqmos,
       "adVqmCfgHistoryThresholdLoss": adVqmCfgHistoryThresholdLoss,
       "adVqmCfgHistoryThresholdOutOfOrder": adVqmCfgHistoryThresholdOutOfOrder,
       "adVqmCfgHistoryThresholdJitter": adVqmCfgHistoryThresholdJitter,
       "adVqmCfgClear": adVqmCfgClear,
       "adVqmCfgClearCallHistory": adVqmCfgClearCallHistory,
       "adVQMThreshold": adVQMThreshold,
       "adVqmThresholdLqmosInfo": adVqmThresholdLqmosInfo,
       "adVqmThresholdLqmosNotice": adVqmThresholdLqmosNotice,
       "adVqmThresholdLqmosWarning": adVqmThresholdLqmosWarning,
       "adVqmThresholdLqmosError": adVqmThresholdLqmosError,
       "adVqmThresholdPqmosInfo": adVqmThresholdPqmosInfo,
       "adVqmThresholdPqmosNotice": adVqmThresholdPqmosNotice,
       "adVqmThresholdPqmosWarning": adVqmThresholdPqmosWarning,
       "adVqmThresholdPqmosError": adVqmThresholdPqmosError,
       "adVqmThresholdOutOfOrderInfo": adVqmThresholdOutOfOrderInfo,
       "adVqmThresholdOutOfOrderNotice": adVqmThresholdOutOfOrderNotice,
       "adVqmThresholdOutOfOrderWarning": adVqmThresholdOutOfOrderWarning,
       "adVqmThresholdOutOfOrderError": adVqmThresholdOutOfOrderError,
       "adVqmThresholdLossInfo": adVqmThresholdLossInfo,
       "adVqmThresholdLossNotice": adVqmThresholdLossNotice,
       "adVqmThresholdLossWarning": adVqmThresholdLossWarning,
       "adVqmThresholdLossError": adVqmThresholdLossError,
       "adVqmThresholdJitterInfo": adVqmThresholdJitterInfo,
       "adVqmThresholdJitterNotice": adVqmThresholdJitterNotice,
       "adVqmThresholdJitterWarning": adVqmThresholdJitterWarning,
       "adVqmThresholdJitterError": adVqmThresholdJitterError,
       "adVQMSysPerf": adVQMSysPerf,
       "adVqmSysActiveCalls": adVqmSysActiveCalls,
       "adVqmSysActiveExcellent": adVqmSysActiveExcellent,
       "adVqmSysActiveGood": adVqmSysActiveGood,
       "adVqmSysActiveFair": adVqmSysActiveFair,
       "adVqmSysActivePoor": adVqmSysActivePoor,
       "adVqmSysCallHistoryCalls": adVqmSysCallHistoryCalls,
       "adVqmSysCallHistoryExcellent": adVqmSysCallHistoryExcellent,
       "adVqmSysCallHistoryGood": adVqmSysCallHistoryGood,
       "adVqmSysCallHistoryFair": adVqmSysCallHistoryFair,
       "adVqmSysCallHistoryPoor": adVqmSysCallHistoryPoor,
       "adVqmSysAllCallsExcellent": adVqmSysAllCallsExcellent,
       "adVqmSysAllCallsGood": adVqmSysAllCallsGood,
       "adVqmSysAllCallsFair": adVqmSysAllCallsFair,
       "adVqmSysAllCallsPoor": adVqmSysAllCallsPoor,
       "adVQMInterface": adVQMInterface,
       "adVQMInterfaceTable": adVQMInterfaceTable,
       "adVQMInterfaceEntry": adVQMInterfaceEntry,
       "adVqmIfcId": adVqmIfcId,
       "adVqmIfcName": adVqmIfcName,
       "adVqmIfcPktsRx": adVqmIfcPktsRx,
       "adVqmIfcPktsLost": adVqmIfcPktsLost,
       "adVqmIfcPktsOoo": adVqmIfcPktsOoo,
       "adVqmIfcPktsDiscarded": adVqmIfcPktsDiscarded,
       "adVqmIfcNumberActiveCalls": adVqmIfcNumberActiveCalls,
       "adVqmIfcTerminatedCalls": adVqmIfcTerminatedCalls,
       "adVqmIfcRLqMinimum": adVqmIfcRLqMinimum,
       "adVqmIfcRLqAverage": adVqmIfcRLqAverage,
       "adVqmIfcRLqMaximum": adVqmIfcRLqMaximum,
       "adVqmIfcRCqMinimum": adVqmIfcRCqMinimum,
       "adVqmIfcRCqAverage": adVqmIfcRCqAverage,
       "adVqmIfcRCqMaximum": adVqmIfcRCqMaximum,
       "adVqmIfcRG107Minimum": adVqmIfcRG107Minimum,
       "adVqmIfcRG107Average": adVqmIfcRG107Average,
       "adVqmIfcRG107Maximum": adVqmIfcRG107Maximum,
       "adVqmIfcMosLqMinimum": adVqmIfcMosLqMinimum,
       "adVqmIfcMosLqAverage": adVqmIfcMosLqAverage,
       "adVqmIfcMosLqMaximum": adVqmIfcMosLqMaximum,
       "adVqmIfcMosCqMinimum": adVqmIfcMosCqMinimum,
       "adVqmIfcMosCqAverage": adVqmIfcMosCqAverage,
       "adVqmIfcMosCqMaximum": adVqmIfcMosCqMaximum,
       "adVqmIfcMosPqMinimum": adVqmIfcMosPqMinimum,
       "adVqmIfcMosPqAverage": adVqmIfcMosPqAverage,
       "adVqmIfcMosPqMaximum": adVqmIfcMosPqMaximum,
       "adVqmIfcLossMinimum": adVqmIfcLossMinimum,
       "adVqmIfcLossAverage": adVqmIfcLossAverage,
       "adVqmIfcLossMaximum": adVqmIfcLossMaximum,
       "adVqmIfcDiscardsMinimum": adVqmIfcDiscardsMinimum,
       "adVqmIfcDiscardsAverage": adVqmIfcDiscardsAverage,
       "adVqmIfcDiscardsMaximum": adVqmIfcDiscardsMaximum,
       "adVqmIfcPdvAverageMs": adVqmIfcPdvAverageMs,
       "adVqmIfcPdvMaximumMs": adVqmIfcPdvMaximumMs,
       "adVqmIfcDelayMinMsec": adVqmIfcDelayMinMsec,
       "adVqmIfcDelayAvgMsec": adVqmIfcDelayAvgMsec,
       "adVqmIfcDelayMaxMsec": adVqmIfcDelayMaxMsec,
       "adVqmIfcNumberStreamsExcellent": adVqmIfcNumberStreamsExcellent,
       "adVqmIfcNumberStreamsGood": adVqmIfcNumberStreamsGood,
       "adVqmIfcNumberStreamsFair": adVqmIfcNumberStreamsFair,
       "adVqmIfcNumberStreamsPoor": adVqmIfcNumberStreamsPoor,
       "adVqmIfcClear": adVqmIfcClear,
       "adVQMEndPoint": adVQMEndPoint,
       "adVQMEndPointTable": adVQMEndPointTable,
       "adVQMEndPointEntry": adVQMEndPointEntry,
       "adVqmEndPointRtpSourceIp": adVqmEndPointRtpSourceIp,
       "adVqmEndPointNumberCompletedCalls": adVqmEndPointNumberCompletedCalls,
       "adVqmEndPointInterfaceId": adVqmEndPointInterfaceId,
       "adVqmEndPointInterfaceName": adVqmEndPointInterfaceName,
       "adVqmEndPointMosLqMinimum": adVqmEndPointMosLqMinimum,
       "adVqmEndPointMosLqAverage": adVqmEndPointMosLqAverage,
       "adVqmEndPointMosLqMaximum": adVqmEndPointMosLqMaximum,
       "adVqmEndPointMosPqMinimum": adVqmEndPointMosPqMinimum,
       "adVqmEndPointMosPqAverage": adVqmEndPointMosPqAverage,
       "adVqmEndPointMosPqMaximum": adVqmEndPointMosPqMaximum,
       "adVqmEndPointPktsLostTotal": adVqmEndPointPktsLostTotal,
       "adVqmEndPointPktsOutOfOrder": adVqmEndPointPktsOutOfOrder,
       "adVqmEndPointJitterMaximum": adVqmEndPointJitterMaximum,
       "adVqmEndPointNumberStreamsExcellent": adVqmEndPointNumberStreamsExcellent,
       "adVqmEndPointNumberStreamsGood": adVqmEndPointNumberStreamsGood,
       "adVqmEndPointNumberStreamsFair": adVqmEndPointNumberStreamsFair,
       "adVqmEndPointNumberStreamsPoor": adVqmEndPointNumberStreamsPoor,
       "adVQMHistory": adVQMHistory,
       "adVQMCallHistoryTable": adVQMCallHistoryTable,
       "adVQMCallHistoryEntry": adVQMCallHistoryEntry,
       "adVqmCallHistRtpSourceIp": adVqmCallHistRtpSourceIp,
       "adVqmCallHistRtpSourcePort": adVqmCallHistRtpSourcePort,
       "adVqmCallHistRtpDestIp": adVqmCallHistRtpDestIp,
       "adVqmCallHistRtpDestPort": adVqmCallHistRtpDestPort,
       "adVqmCallHistSsrcid": adVqmCallHistSsrcid,
       "adVqmCallHistTo": adVqmCallHistTo,
       "adVqmCallHistFrom": adVqmCallHistFrom,
       "adVqmCallHistRtpSourceUri": adVqmCallHistRtpSourceUri,
       "adVqmCallHistCallid": adVqmCallHistCallid,
       "adVqmCallHistCcmid": adVqmCallHistCcmid,
       "adVqmCallHistSourceIntName": adVqmCallHistSourceIntName,
       "adVqmCallHistDestIntName": adVqmCallHistDestIntName,
       "adVqmCallHistSourceIntDescription": adVqmCallHistSourceIntDescription,
       "adVqmCallHistDestIntDescription": adVqmCallHistDestIntDescription,
       "adVqmCallHistCallStart": adVqmCallHistCallStart,
       "adVqmCallHistCallDurationMs": adVqmCallHistCallDurationMs,
       "adVqmCallHistCodec": adVqmCallHistCodec,
       "adVqmCallHistCodecClass": adVqmCallHistCodecClass,
       "adVqmCallHistDscp": adVqmCallHistDscp,
       "adVqmCallHistPktsRcvdTotal": adVqmCallHistPktsRcvdTotal,
       "adVqmCallHistPktsLostTotal": adVqmCallHistPktsLostTotal,
       "adVqmCallHistPktsDiscardedTotal": adVqmCallHistPktsDiscardedTotal,
       "adVqmCallHistOutOfOrder": adVqmCallHistOutOfOrder,
       "adVqmCallHistPdvAverageMs": adVqmCallHistPdvAverageMs,
       "adVqmCallHistPdvMaximumMs": adVqmCallHistPdvMaximumMs,
       "adVqmCallHistRtDelayInst": adVqmCallHistRtDelayInst,
       "adVqmCallHistRtDelayAverage": adVqmCallHistRtDelayAverage,
       "adVqmCallHistRtDelayMaximum": adVqmCallHistRtDelayMaximum,
       "adVqmCallHistOnewayDelayInst": adVqmCallHistOnewayDelayInst,
       "adVqmCallHistOnewayDelayAverage": adVqmCallHistOnewayDelayAverage,
       "adVqmCallHistOnewayDelayMaximum": adVqmCallHistOnewayDelayMaximum,
       "adVqmCallHistOrigDelayInst": adVqmCallHistOrigDelayInst,
       "adVqmCallHistOrigDelayAverage": adVqmCallHistOrigDelayAverage,
       "adVqmCallHistOrigDelayMaximum": adVqmCallHistOrigDelayMaximum,
       "adVqmCallHistTermDelayMinimum": adVqmCallHistTermDelayMinimum,
       "adVqmCallHistTermDelayAverage": adVqmCallHistTermDelayAverage,
       "adVqmCallHistTermDelayMaximum": adVqmCallHistTermDelayMaximum,
       "adVqmCallHistRLq": adVqmCallHistRLq,
       "adVqmCallHistRCq": adVqmCallHistRCq,
       "adVqmCallHistRNominal": adVqmCallHistRNominal,
       "adVqmCallHistRG107": adVqmCallHistRG107,
       "adVqmCallHistMosLq": adVqmCallHistMosLq,
       "adVqmCallHistMosCq": adVqmCallHistMosCq,
       "adVqmCallHistMosPq": adVqmCallHistMosPq,
       "adVqmCallHistMosNominal": adVqmCallHistMosNominal,
       "adVqmCallHistDegLoss": adVqmCallHistDegLoss,
       "adVqmCallHistDegDiscard": adVqmCallHistDegDiscard,
       "adVqmCallHistDegVocoder": adVqmCallHistDegVocoder,
       "adVqmCallHistDegRecency": adVqmCallHistDegRecency,
       "adVqmCallHistDegDelay": adVqmCallHistDegDelay,
       "adVqmCallHistDegSiglvl": adVqmCallHistDegSiglvl,
       "adVqmCallHistDegNoiselvl": adVqmCallHistDegNoiselvl,
       "adVqmCallHistDegEcholvl": adVqmCallHistDegEcholvl,
       "adVqmCallHistBurstRLq": adVqmCallHistBurstRLq,
       "adVqmCallHistBurstCount": adVqmCallHistBurstCount,
       "adVqmCallHistBurstRateAvg": adVqmCallHistBurstRateAvg,
       "adVqmCallHistBurstLenAvgPkts": adVqmCallHistBurstLenAvgPkts,
       "adVqmCallHistBurstLenAvgMsec": adVqmCallHistBurstLenAvgMsec,
       "adVqmCallHistGapR": adVqmCallHistGapR,
       "adVqmCallHistGapCount": adVqmCallHistGapCount,
       "adVqmCallHistGapLossRateAvg": adVqmCallHistGapLossRateAvg,
       "adVqmCallHistGapLenPkts": adVqmCallHistGapLenPkts,
       "adVqmCallHistGapLenMsec": adVqmCallHistGapLenMsec,
       "adVqmCallHistLossRateAvg": adVqmCallHistLossRateAvg,
       "adVqmCallHistNetworkLossAvg": adVqmCallHistNetworkLossAvg,
       "adVqmCallHistDiscardRateAvg": adVqmCallHistDiscardRateAvg,
       "adVqmCallHistExcessBurst": adVqmCallHistExcessBurst,
       "adVqmCallHistExcessGap": adVqmCallHistExcessGap,
       "adVqmCallHistPpdvMsec": adVqmCallHistPpdvMsec,
       "adVqmCallHistLateThresholdMs": adVqmCallHistLateThresholdMs,
       "adVqmCallHistLateThresholdPc": adVqmCallHistLateThresholdPc,
       "adVqmCallHistLateUnderThresh": adVqmCallHistLateUnderThresh,
       "adVqmCallHistLateTotalCount": adVqmCallHistLateTotalCount,
       "adVqmCallHistLatePeakJitterMs": adVqmCallHistLatePeakJitterMs,
       "adVqmCallHistEarlyThreshMs": adVqmCallHistEarlyThreshMs,
       "adVqmCallHistEarlyThreshPc": adVqmCallHistEarlyThreshPc,
       "adVqmCallHistEarlyUnderThresh": adVqmCallHistEarlyUnderThresh,
       "adVqmCallHistEarlyTotalCount": adVqmCallHistEarlyTotalCount,
       "adVqmCallHistEarlyPeakJitterMs": adVqmCallHistEarlyPeakJitterMs,
       "adVqmCallHistDelayIncreaseCount": adVqmCallHistDelayIncreaseCount,
       "adVqmCallHistDelayDecreaseCount": adVqmCallHistDelayDecreaseCount,
       "adVqmCallHistResyncCount": adVqmCallHistResyncCount,
       "adVqmCallHistJitterBufferType": adVqmCallHistJitterBufferType,
       "adVqmCallHistJbCfgMin": adVqmCallHistJbCfgMin,
       "adVqmCallHistJbCfgNom": adVqmCallHistJbCfgNom,
       "adVqmCallHistJbCfgMax": adVqmCallHistJbCfgMax,
       "adVqmCallHistDuplicatePkts": adVqmCallHistDuplicatePkts,
       "adVqmCallHistEarlyPkts": adVqmCallHistEarlyPkts,
       "adVqmCallHistLatePkts": adVqmCallHistLatePkts,
       "adVqmCallHistOverrunDiscardPkts": adVqmCallHistOverrunDiscardPkts,
       "adVqmCallHistUnderrunDiscardPkts": adVqmCallHistUnderrunDiscardPkts,
       "adVqmCallHistDelayMinMsec": adVqmCallHistDelayMinMsec,
       "adVqmCallHistDelayAvgMsec": adVqmCallHistDelayAvgMsec,
       "adVqmCallHistDelayMaxMsec": adVqmCallHistDelayMaxMsec,
       "adVqmCallHistDelayCurrentMsec": adVqmCallHistDelayCurrentMsec,
       "adVqmCallHistExtRLqIn": adVqmCallHistExtRLqIn,
       "adVqmCallHistExtRLqOut": adVqmCallHistExtRLqOut,
       "adVqmCallHistExtRCqIn": adVqmCallHistExtRCqIn,
       "adVqmCallHistExtRCqOut": adVqmCallHistExtRCqOut,
       "adVqmCallHistThroughPutIndex": adVqmCallHistThroughPutIndex,
       "adVqmCallHistReliabilityIndex": adVqmCallHistReliabilityIndex,
       "adVqmCallHistBitrate": adVqmCallHistBitrate,
       "adVQMActive": adVQMActive,
       "adVQMActiveCallTable": adVQMActiveCallTable,
       "adVQMActiveCallEntry": adVQMActiveCallEntry,
       "adVqmActCallRtpSourceIp": adVqmActCallRtpSourceIp,
       "adVqmActCallRtpSourcePort": adVqmActCallRtpSourcePort,
       "adVqmActCallRtpDestIp": adVqmActCallRtpDestIp,
       "adVqmActCallRtpDestPort": adVqmActCallRtpDestPort,
       "adVqmActCallSsrcid": adVqmActCallSsrcid,
       "adVqmActCallTo": adVqmActCallTo,
       "adVqmActCallFrom": adVqmActCallFrom,
       "adVqmActCallRtpSourceUri": adVqmActCallRtpSourceUri,
       "adVqmActCallCallid": adVqmActCallCallid,
       "adVqmActCallCcmid": adVqmActCallCcmid,
       "adVqmActCallSourceIntName": adVqmActCallSourceIntName,
       "adVqmActCallDestIntName": adVqmActCallDestIntName,
       "adVqmActCallSourceIntDescription": adVqmActCallSourceIntDescription,
       "adVqmActCallDestIntDescription": adVqmActCallDestIntDescription,
       "adVqmActCallCallStart": adVqmActCallCallStart,
       "adVqmActCallCallDurationMs": adVqmActCallCallDurationMs,
       "adVqmActCallCodec": adVqmActCallCodec,
       "adVqmActCallCodecClass": adVqmActCallCodecClass,
       "adVqmActCallDscp": adVqmActCallDscp,
       "adVqmActCallPktsRcvdTotal": adVqmActCallPktsRcvdTotal,
       "adVqmActCallPktsLostTotal": adVqmActCallPktsLostTotal,
       "adVqmActCallPktsDiscardedTotal": adVqmActCallPktsDiscardedTotal,
       "adVqmActCallOutOfOrder": adVqmActCallOutOfOrder,
       "adVqmActCallPdvAverageMs": adVqmActCallPdvAverageMs,
       "adVqmActCallPdvMaximumMs": adVqmActCallPdvMaximumMs,
       "adVqmActCallRtDelayInst": adVqmActCallRtDelayInst,
       "adVqmActCallRtDelayAverage": adVqmActCallRtDelayAverage,
       "adVqmActCallRtDelayMaximum": adVqmActCallRtDelayMaximum,
       "adVqmActCallOnewayDelayInst": adVqmActCallOnewayDelayInst,
       "adVqmActCallOnewayDelayAverage": adVqmActCallOnewayDelayAverage,
       "adVqmActCallOnewayDelayMaximum": adVqmActCallOnewayDelayMaximum,
       "adVqmActCallOrigDelayInst": adVqmActCallOrigDelayInst,
       "adVqmActCallOrigDelayAverage": adVqmActCallOrigDelayAverage,
       "adVqmActCallOrigDelayMaximum": adVqmActCallOrigDelayMaximum,
       "adVqmActCallTermDelayMinimum": adVqmActCallTermDelayMinimum,
       "adVqmActCallTermDelayAverage": adVqmActCallTermDelayAverage,
       "adVqmActCallTermDelayMaximum": adVqmActCallTermDelayMaximum,
       "adVqmActCallRLq": adVqmActCallRLq,
       "adVqmActCallRCq": adVqmActCallRCq,
       "adVqmActCallRNominal": adVqmActCallRNominal,
       "adVqmActCallRG107": adVqmActCallRG107,
       "adVqmActCallMosLq": adVqmActCallMosLq,
       "adVqmActCallMosCq": adVqmActCallMosCq,
       "adVqmActCallMosPq": adVqmActCallMosPq,
       "adVqmActCallMosNominal": adVqmActCallMosNominal,
       "adVqmActCallDegLoss": adVqmActCallDegLoss,
       "adVqmActCallDegDiscard": adVqmActCallDegDiscard,
       "adVqmActCallDegVocoder": adVqmActCallDegVocoder,
       "adVqmActCallDegRecency": adVqmActCallDegRecency,
       "adVqmActCallDegDelay": adVqmActCallDegDelay,
       "adVqmActCallDegSiglvl": adVqmActCallDegSiglvl,
       "adVqmActCallDegNoiselvl": adVqmActCallDegNoiselvl,
       "adVqmActCallDegEcholvl": adVqmActCallDegEcholvl,
       "adVqmActCallBurstRLq": adVqmActCallBurstRLq,
       "adVqmActCallBurstCount": adVqmActCallBurstCount,
       "adVqmActCallBurstRateAvg": adVqmActCallBurstRateAvg,
       "adVqmActCallBurstLenAvgPkts": adVqmActCallBurstLenAvgPkts,
       "adVqmActCallBurstLenAvgMsec": adVqmActCallBurstLenAvgMsec,
       "adVqmActCallGapR": adVqmActCallGapR,
       "adVqmActCallGapCount": adVqmActCallGapCount,
       "adVqmActCallGapLossRateAvg": adVqmActCallGapLossRateAvg,
       "adVqmActCallGapLenPkts": adVqmActCallGapLenPkts,
       "adVqmActCallGapLenMsec": adVqmActCallGapLenMsec,
       "adVqmActCallLossRateAvg": adVqmActCallLossRateAvg,
       "adVqmActCallNetworkLossAvg": adVqmActCallNetworkLossAvg,
       "adVqmActCallDiscardRateAvg": adVqmActCallDiscardRateAvg,
       "adVqmActCallExcessBurst": adVqmActCallExcessBurst,
       "adVqmActCallExcessGap": adVqmActCallExcessGap,
       "adVqmActCallPpdvMsec": adVqmActCallPpdvMsec,
       "adVqmActCallLateThresholdMs": adVqmActCallLateThresholdMs,
       "adVqmActCallLateThresholdPc": adVqmActCallLateThresholdPc,
       "adVqmActCallLateUnderThresh": adVqmActCallLateUnderThresh,
       "adVqmActCallLateTotalCount": adVqmActCallLateTotalCount,
       "adVqmActCallLatePeakJitterMs": adVqmActCallLatePeakJitterMs,
       "adVqmActCallEarlyThreshMs": adVqmActCallEarlyThreshMs,
       "adVqmActCallEarlyThreshPc": adVqmActCallEarlyThreshPc,
       "adVqmActCallEarlyUnderThresh": adVqmActCallEarlyUnderThresh,
       "adVqmActCallEarlyTotalCount": adVqmActCallEarlyTotalCount,
       "adVqmActCallEarlyPeakJitterMs": adVqmActCallEarlyPeakJitterMs,
       "adVqmActCallDelayIncreaseCount": adVqmActCallDelayIncreaseCount,
       "adVqmActCallDelayDecreaseCount": adVqmActCallDelayDecreaseCount,
       "adVqmActCallResyncCount": adVqmActCallResyncCount,
       "adVqmActCallJitterBufferType": adVqmActCallJitterBufferType,
       "adVqmActCallJbCfgMin": adVqmActCallJbCfgMin,
       "adVqmActCallJbCfgNom": adVqmActCallJbCfgNom,
       "adVqmActCallJbCfgMax": adVqmActCallJbCfgMax,
       "adVqmActCallDuplicatePkts": adVqmActCallDuplicatePkts,
       "adVqmActCallEarlyPkts": adVqmActCallEarlyPkts,
       "adVqmActCallLatePkts": adVqmActCallLatePkts,
       "adVqmActCallOverrunDiscardPkts": adVqmActCallOverrunDiscardPkts,
       "adVqmActCallUnderrunDiscardPkts": adVqmActCallUnderrunDiscardPkts,
       "adVqmActCallDelayMinMsec": adVqmActCallDelayMinMsec,
       "adVqmActCallDelayAvgMsec": adVqmActCallDelayAvgMsec,
       "adVqmActCallDelayMaxMsec": adVqmActCallDelayMaxMsec,
       "adVqmActCallDelayCurrentMsec": adVqmActCallDelayCurrentMsec,
       "adVqmActCallExtRLqIn": adVqmActCallExtRLqIn,
       "adVqmActCallExtRLqOut": adVqmActCallExtRLqOut,
       "adVqmActCallExtRCqIn": adVqmActCallExtRCqIn,
       "adVqmActCallExtRCqOut": adVqmActCallExtRCqOut,
       "adVqmActCallThroughPutIndex": adVqmActCallThroughPutIndex,
       "adVqmActCallReliabilityIndex": adVqmActCallReliabilityIndex,
       "adVqmActCallBitrate": adVqmActCallBitrate,
       "adGenAOSVqmConformance": adGenAOSVqmConformance,
       "adGenAOSVqmGroups": adGenAOSVqmGroups,
       "adVQMCfgGroup": adVQMCfgGroup,
       "adVQMThresholdGroup": adVQMThresholdGroup,
       "adVQMSysPerfGroup": adVQMSysPerfGroup,
       "adVQMInterfaceGroup": adVQMInterfaceGroup,
       "adVQMEndPointGroup": adVQMEndPointGroup,
       "adVQMCallHistoryGroup": adVQMCallHistoryGroup,
       "adVQMActiveCallGroup": adVQMActiveCallGroup,
       "adVQMTrapGroup": adVQMTrapGroup,
       "adVQMNotificationGroup": adVQMNotificationGroup,
       "adGenAOSVqmCompliances": adGenAOSVqmCompliances,
       "adGenAOSVqmFullCompliance": adGenAOSVqmFullCompliance,
       "adGenAOSVQMMib": adGenAOSVQMMib}
)
