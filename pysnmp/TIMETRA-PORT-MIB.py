# SNMP MIB module (TIMETRA-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:02:00 2024
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

(AtmTrafficDescrParamIndex,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmTrafficDescrParamIndex",
    "AtmVpIdentifier")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(TmnxAlarmState,
 TmnxMDAChanType,
 TmnxPortAdminStatus,
 tmnxChassisIndex,
 tmnxChassisNotifyChassisId,
 tmnxHwConformance,
 tmnxHwNotification,
 tmnxHwObjs,
 tmnxMdaNotifyType) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxAlarmState",
    "TmnxMDAChanType",
    "TmnxPortAdminStatus",
    "tmnxChassisIndex",
    "tmnxChassisNotifyChassisId",
    "tmnxHwConformance",
    "tmnxHwNotification",
    "tmnxHwObjs",
    "tmnxMdaNotifyType")

(timetraSRMIBModules,) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules")

(TAdaptationRuleOverride,
 TBurstPercentOrDefaultOverride,
 TBurstSizeBytesOverride,
 TBurstSizeOverride,
 TCIRPercentOverride,
 TCIRRateOverride,
 TClassBurstLimit,
 TEgrPolicerId,
 TEgressQueueId,
 TExpSecondaryShaperClassRate,
 TExpSecondaryShaperPIRRate,
 TFCName,
 THsmdaPIRMRateOverride,
 THsmdaWeightOverride,
 TIngressQueueId,
 TItemDescription,
 TItemLongDescription,
 TMcFrQoSProfileId,
 TMlpppQoSProfileId,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRPercentOverride,
 TPIRRateOverride,
 TPortSchedulerCIR,
 TPortSchedulerPIR,
 TPortSchedulerPIRRate,
 TQueueId,
 TRateType,
 TSecondaryShaper10GPIRRate,
 TmnxActionType,
 TmnxEgrPolicerStatMode,
 TmnxEnabledDisabled,
 TmnxOperState,
 TmnxPortID,
 TmnxSubIdentStringOrEmpty,
 TmnxSubMgtIntDestId,
 TmnxSubMgtOrgStrOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TAdaptationRuleOverride",
    "TBurstPercentOrDefaultOverride",
    "TBurstSizeBytesOverride",
    "TBurstSizeOverride",
    "TCIRPercentOverride",
    "TCIRRateOverride",
    "TClassBurstLimit",
    "TEgrPolicerId",
    "TEgressQueueId",
    "TExpSecondaryShaperClassRate",
    "TExpSecondaryShaperPIRRate",
    "TFCName",
    "THsmdaPIRMRateOverride",
    "THsmdaWeightOverride",
    "TIngressQueueId",
    "TItemDescription",
    "TItemLongDescription",
    "TMcFrQoSProfileId",
    "TMlpppQoSProfileId",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRPercentOverride",
    "TPIRRateOverride",
    "TPortSchedulerCIR",
    "TPortSchedulerPIR",
    "TPortSchedulerPIRRate",
    "TQueueId",
    "TRateType",
    "TSecondaryShaper10GPIRRate",
    "TmnxActionType",
    "TmnxEgrPolicerStatMode",
    "TmnxEnabledDisabled",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxSubIdentStringOrEmpty",
    "TmnxSubMgtIntDestId",
    "TmnxSubMgtOrgStrOrZero")


# MODULE-IDENTITY

tmnxPortMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 25)
)
tmnxPortMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1909-02-28 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-16 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPortOperStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("diagnosing", 4),
          ("failed", 5),
          ("inService", 2),
          ("outOfService", 3),
          ("unknown", 1))
    )



class TmnxPortEtherReportValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("duplicateLane", 8),
          ("highBer", 5),
          ("localFault", 3),
          ("noAmLock", 7),
          ("noBlockLock", 6),
          ("noFrameLock", 4),
          ("notUsed", 0),
          ("remoteFault", 2),
          ("signalFailure", 1))
    )



class TmnxPortEtherReportStatus(Bits, TextualConvention):
    status = "current"


class TmnxPortEtherCrcMonReportValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noFault", 0),
          ("sdThresholdExceeded", 1),
          ("sfThresholdExceeded", 2))
    )



class TmnxPortEtherCrcMonReportStatus(Bits, TextualConvention):
    status = "current"


class TmnxPortClass(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("cgige", 11),
          ("faste", 2),
          ("gige", 3),
          ("none", 1),
          ("sonet", 5),
          ("tdm", 9),
          ("unused", 7),
          ("vport", 6),
          ("vsme", 12),
          ("xcme", 8),
          ("xgige", 4),
          ("xlgige", 10))
    )



class TmnxPortConnectorType(Unsigned32, TextualConvention):
    status = "current"


class TmnxPortState(Integer32, TextualConvention):
    status = "current"
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
        *(("diagnose", 6),
          ("ghost", 2),
          ("linkDown", 3),
          ("linkUp", 4),
          ("none", 1),
          ("up", 5))
    )



class TmnxPortType(Unsigned32, TextualConvention):
    status = "current"


class TmnxPortEncapType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("atmEncap", 9),
          ("bcpDot1qEncap", 5),
          ("bcpNullEncap", 4),
          ("cemEncap", 13),
          ("ciscoHDLCEncap", 12),
          ("frEncap", 7),
          ("ipcpEncap", 6),
          ("mplsEncap", 3),
          ("nullEncap", 1),
          ("pppAutoEncap", 8),
          ("qEncap", 2),
          ("qinqEncap", 10),
          ("unknown", 0),
          ("wanMirrorEncap", 11))
    )



class TmnxDs0ChannelList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TmnxBundleID(Unsigned32, TextualConvention):
    status = "current"


class TmnxDSXBertPattern(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("alternating", 3),
          ("none", 0),
          ("ones", 1),
          ("twoexp11", 8),
          ("twoexp15", 6),
          ("twoexp20", 7),
          ("twoexp20q", 9),
          ("twoexp23", 10),
          ("twoexp3", 4),
          ("twoexp9", 5),
          ("zeros", 2))
    )



class TmnxDSXBertOperStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 1),
          ("idle", 2),
          ("noMdaResources", 3),
          ("none", 0))
    )



class TmnxDSXIdleCycleFlags(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flags", 1),
          ("none", 0),
          ("ones", 2))
    )



class TmnxDSXIdleFillType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 1),
          ("notApplicable", 0),
          ("userDefinedPattern", 2))
    )



class TmnxDSXLoopback(Integer32, TextualConvention):
    status = "obsolete"
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
        *(("internal", 2),
          ("line", 1),
          ("none", 0),
          ("remote", 3))
    )



class TmnxDSXReportAlarm(Bits, TextualConvention):
    status = "current"


class TmnxDSXClockSource(Integer32, TextualConvention):
    status = "current"
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
        *(("adaptive", 3),
          ("differential", 4),
          ("loopTimed", 1),
          ("nodeTimed", 2))
    )



class TmnxDSXClockSyncState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("freeRun", 3),
          ("freqTracking", 5),
          ("holdOver", 2),
          ("normal", 1),
          ("phaseTracking", 4),
          ("unknown", 0))
    )



class TmnxDS1Loopback(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fdlAnsi", 3),
          ("fdlBellcore", 4),
          ("inbandAnsi", 6),
          ("inbandBellcore", 7),
          ("internal", 2),
          ("line", 1),
          ("none", 0),
          ("payloadAnsi", 5))
    )



class TmnxDS3Loopback(Integer32, TextualConvention):
    status = "current"
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
        *(("internal", 2),
          ("line", 1),
          ("none", 0),
          ("remote", 3))
    )



class TmnxImaGrpState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("blocked", 8),
          ("configAbortIncompatibleSymmetry", 5),
          ("configAbortOther", 6),
          ("configAbortUnsupportedImaVersion", 10),
          ("configAbortUnsupportedM", 4),
          ("insufficientLinks", 7),
          ("invalid", 0),
          ("notConfigured", 1),
          ("operational", 9),
          ("startUp", 2),
          ("startUpAck", 3))
    )



class TmnxImaGrpFailState(Integer32, TextualConvention):
    status = "current"
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("blockedFe", 11),
          ("blockedNe", 10),
          ("failedAssymetricFe", 7),
          ("failedAssymetricNe", 6),
          ("insufficientLinksFe", 9),
          ("insufficientLinksNe", 8),
          ("invalidImaVersionFe", 14),
          ("invalidImaVersionNe", 13),
          ("invalidMValueFe", 5),
          ("invalidMValueNe", 4),
          ("noFailure", 1),
          ("otherFailure", 12),
          ("startUpFe", 3),
          ("startUpNe", 2))
    )



class TmnxImaLnkState(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 8),
          ("notInGroup", 1),
          ("unusableFailed", 6),
          ("unusableFault", 3),
          ("unusableInhibited", 5),
          ("unusableMisconnected", 4),
          ("unusableNoGivenReason", 2),
          ("usable", 7))
    )



class TmnxImaLnkFailState(Integer32, TextualConvention):
    status = "current"
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
        *(("blocked", 6),
          ("farEndRxLinkUnusable", 9),
          ("farEndTxLinkUnusable", 8),
          ("fault", 7),
          ("imaLinkFailure", 2),
          ("lifFailure", 3),
          ("lodsFailure", 4),
          ("misConnected", 5),
          ("noFailure", 1))
    )



class TmnxImaTestState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("failed", 3),
          ("operating", 2))
    )



class TmnxImaGrpClockModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 1),
          ("itc", 2))
    )



class TmnxImaGrpVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneDotOne", 2),
          ("oneDotZero", 1))
    )



class TmnxMcMlpppClassIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class TmnxMlpppEndpointIdClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot1GlobalMacAddress", 3),
          ("ipAddress", 2),
          ("localAddress", 1),
          ("nullClass", 0),
          ("pppMagicNumberBlock", 4),
          ("publicSwitchedNetworkDirNumber", 5))
    )



class TmnxMlfrLinkDownReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("linkReset", 9),
          ("loopback", 3),
          ("negotiating", 4),
          ("noRxHelloAck", 5),
          ("none", 0),
          ("outOfService", 1),
          ("redDiffDelayExceeded", 2),
          ("rxCause", 7),
          ("txCause", 8))
    )



class TmnxWaveTrackerAlarm(Bits, TextualConvention):
    status = "current"


class TmnxOpticalAmpAlarm(Bits, TextualConvention):
    status = "current"


class TmnxOpticalTdcmAlarm(Bits, TextualConvention):
    status = "current"


class TmnxOpticalTdcmCtrlMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("manual", 1))
    )



class TmnxOpticalAmpCtrlState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("adjusting", 2),
          ("converged", 4),
          ("lossOfsignal", 1),
          ("paused", 3),
          ("unknown", 0))
    )



class TmnxOpticalTdcmCtrlState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("converged", 6),
          ("disabled", 1),
          ("fineTuning", 5),
          ("sweeping", 3),
          ("unknown", 0),
          ("waiting", 2),
          ("zoneIn", 4))
    )



class TmnxOpticalDwdmChannel(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(17, 61),
        ValueRangeConstraint(170, 610),
    )



class TmnxDigitalDiagnosticFailureBits(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_TmnxPortConformance_ObjectIdentity = ObjectIdentity
tmnxPortConformance = _TmnxPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2)
)
_TmnxPortCompliances_ObjectIdentity = ObjectIdentity
tmnxPortCompliances = _TmnxPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1)
)
_TmnxPortComp7750_ObjectIdentity = ObjectIdentity
tmnxPortComp7750 = _TmnxPortComp7750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3)
)
_TmnxPortComp7450_ObjectIdentity = ObjectIdentity
tmnxPortComp7450 = _TmnxPortComp7450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 4)
)
_TmnxPortComp7710_ObjectIdentity = ObjectIdentity
tmnxPortComp7710 = _TmnxPortComp7710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 5)
)
_TmnxPortGroups_ObjectIdentity = ObjectIdentity
tmnxPortGroups = _TmnxPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2)
)
_TmnxPortObjs_ObjectIdentity = ObjectIdentity
tmnxPortObjs = _TmnxPortObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4)
)
_TmnxPortTableLastChange_Type = TimeStamp
_TmnxPortTableLastChange_Object = MibScalar
tmnxPortTableLastChange = _TmnxPortTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 1),
    _TmnxPortTableLastChange_Type()
)
tmnxPortTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTableLastChange.setStatus("current")
_TmnxPortTable_Object = MibTable
tmnxPortTable = _TmnxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxPortTable.setStatus("current")
_TmnxPortEntry_Object = MibTableRow
tmnxPortEntry = _TmnxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1)
)
tmnxPortEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxPortEntry.setStatus("current")
_TmnxPortPortID_Type = TmnxPortID
_TmnxPortPortID_Object = MibTableColumn
tmnxPortPortID = _TmnxPortPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 1),
    _TmnxPortPortID_Type()
)
tmnxPortPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortPortID.setStatus("current")
_TmnxPortLastChangeTime_Type = TimeStamp
_TmnxPortLastChangeTime_Object = MibTableColumn
tmnxPortLastChangeTime = _TmnxPortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 2),
    _TmnxPortLastChangeTime_Type()
)
tmnxPortLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortLastChangeTime.setStatus("current")
_TmnxPortType_Type = TmnxPortType
_TmnxPortType_Object = MibTableColumn
tmnxPortType = _TmnxPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 3),
    _TmnxPortType_Type()
)
tmnxPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortType.setStatus("current")
_TmnxPortClass_Type = TmnxPortClass
_TmnxPortClass_Object = MibTableColumn
tmnxPortClass = _TmnxPortClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 4),
    _TmnxPortClass_Type()
)
tmnxPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortClass.setStatus("current")


class _TmnxPortDescription_Type(TItemLongDescription):
    """Custom type tmnxPortDescription based on TItemLongDescription"""
    defaultHexValue = ""


_TmnxPortDescription_Object = MibTableColumn
tmnxPortDescription = _TmnxPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 5),
    _TmnxPortDescription_Type()
)
tmnxPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortDescription.setStatus("current")
_TmnxPortName_Type = TNamedItemOrEmpty
_TmnxPortName_Object = MibTableColumn
tmnxPortName = _TmnxPortName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 6),
    _TmnxPortName_Type()
)
tmnxPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortName.setStatus("current")


class _TmnxPortAlias_Type(TNamedItemOrEmpty):
    """Custom type tmnxPortAlias based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPortAlias_Object = MibTableColumn
tmnxPortAlias = _TmnxPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 7),
    _TmnxPortAlias_Type()
)
tmnxPortAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortAlias.setStatus("current")


class _TmnxPortUserAssignedMac_Type(TruthValue):
    """Custom type tmnxPortUserAssignedMac based on TruthValue"""


_TmnxPortUserAssignedMac_Object = MibTableColumn
tmnxPortUserAssignedMac = _TmnxPortUserAssignedMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 8),
    _TmnxPortUserAssignedMac_Type()
)
tmnxPortUserAssignedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortUserAssignedMac.setStatus("current")


class _TmnxPortMacAddress_Type(MacAddress):
    """Custom type tmnxPortMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxPortMacAddress_Object = MibTableColumn
tmnxPortMacAddress = _TmnxPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 9),
    _TmnxPortMacAddress_Type()
)
tmnxPortMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortMacAddress.setStatus("current")
_TmnxPortHwMacAddress_Type = MacAddress
_TmnxPortHwMacAddress_Object = MibTableColumn
tmnxPortHwMacAddress = _TmnxPortHwMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 10),
    _TmnxPortHwMacAddress_Type()
)
tmnxPortHwMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortHwMacAddress.setStatus("current")


class _TmnxPortMode_Type(Integer32):
    """Custom type tmnxPortMode based on Integer32"""
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
        *(("access", 1),
          ("hybrid", 3),
          ("network", 2),
          ("undefined", 0))
    )


_TmnxPortMode_Type.__name__ = "Integer32"
_TmnxPortMode_Object = MibTableColumn
tmnxPortMode = _TmnxPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 11),
    _TmnxPortMode_Type()
)
tmnxPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortMode.setStatus("current")
_TmnxPortEncapType_Type = TmnxPortEncapType
_TmnxPortEncapType_Object = MibTableColumn
tmnxPortEncapType = _TmnxPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 12),
    _TmnxPortEncapType_Type()
)
tmnxPortEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEncapType.setStatus("current")


class _TmnxPortLagId_Type(Unsigned32):
    """Custom type tmnxPortLagId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TmnxPortLagId_Type.__name__ = "Unsigned32"
_TmnxPortLagId_Object = MibTableColumn
tmnxPortLagId = _TmnxPortLagId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 13),
    _TmnxPortLagId_Type()
)
tmnxPortLagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortLagId.setStatus("current")


class _TmnxPortHoldTimeUp_Type(Unsigned32):
    """Custom type tmnxPortHoldTimeUp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90000),
    )


_TmnxPortHoldTimeUp_Type.__name__ = "Unsigned32"
_TmnxPortHoldTimeUp_Object = MibTableColumn
tmnxPortHoldTimeUp = _TmnxPortHoldTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 14),
    _TmnxPortHoldTimeUp_Type()
)
tmnxPortHoldTimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortHoldTimeUp.setStatus("current")


class _TmnxPortHoldTimeDown_Type(Unsigned32):
    """Custom type tmnxPortHoldTimeDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90000),
    )


_TmnxPortHoldTimeDown_Type.__name__ = "Unsigned32"
_TmnxPortHoldTimeDown_Object = MibTableColumn
tmnxPortHoldTimeDown = _TmnxPortHoldTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 15),
    _TmnxPortHoldTimeDown_Type()
)
tmnxPortHoldTimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortHoldTimeDown.setStatus("current")


class _TmnxPortUpProtocols_Type(Bits):
    """Custom type tmnxPortUpProtocols based on Bits"""
    namedValues = NamedValues(
        *(("portUpAtm", 5),
          ("portUpBcp", 2),
          ("portUpChdlc", 6),
          ("portUpFr", 4),
          ("portUpIma", 7),
          ("portUpIpv4", 0),
          ("portUpIpv6", 8),
          ("portUpIso", 3),
          ("portUpMpls", 1))
    )

_TmnxPortUpProtocols_Type.__name__ = "Bits"
_TmnxPortUpProtocols_Object = MibTableColumn
tmnxPortUpProtocols = _TmnxPortUpProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 16),
    _TmnxPortUpProtocols_Type()
)
tmnxPortUpProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortUpProtocols.setStatus("current")
_TmnxPortConnectorType_Type = TmnxPortConnectorType
_TmnxPortConnectorType_Object = MibTableColumn
tmnxPortConnectorType = _TmnxPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 17),
    _TmnxPortConnectorType_Type()
)
tmnxPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortConnectorType.setStatus("current")


class _TmnxPortTransceiverType_Type(Integer32):
    """Custom type tmnxPortTransceiverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("cfpTransceiver", 14),
          ("dwdmSfpTransceiver", 11),
          ("gbic", 1),
          ("moduleConnectorSolderedToMotherboard", 2),
          ("qsfpPlusTransceiver", 13),
          ("qsfpTransceiver", 12),
          ("sfpTransceiver", 3),
          ("unknown", 0),
          ("x2Transceiver", 10),
          ("xbiTransceiver", 4),
          ("xenpakTransceiver", 5),
          ("xffTransceiver", 7),
          ("xfpTransceiver", 6),
          ("xfpeTransceiver", 8),
          ("xpakTransceiver", 9))
    )


_TmnxPortTransceiverType_Type.__name__ = "Integer32"
_TmnxPortTransceiverType_Object = MibTableColumn
tmnxPortTransceiverType = _TmnxPortTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 25),
    _TmnxPortTransceiverType_Type()
)
tmnxPortTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTransceiverType.setStatus("current")


class _TmnxPortTransceiverCode_Type(Bits):
    """Custom type tmnxPortTransceiverCode based on Bits"""
    namedValues = NamedValues(
        *(("faste-100base-mm-fx", 14),
          ("faste-100base-sm-fx", 15),
          ("gige-1000base-cx", 11),
          ("gige-1000base-lx", 12),
          ("gige-1000base-sx", 13),
          ("gige-1000base-t", 10),
          ("oc12-multimodeshortreach", 6),
          ("oc12-singlemodeinterreach", 5),
          ("oc12-singlemodelongreach", 4),
          ("oc3-multi-modeshortreach", 9),
          ("oc3-singlemodeinterreach", 8),
          ("oc3-singlemodelongreach", 7),
          ("oc48-intermediatereach", 2),
          ("oc48-longreach", 1),
          ("oc48-shortreach", 3),
          ("unknown", 0),
          ("xgige-10gbase-er", 18),
          ("xgige-10gbase-ew", 21),
          ("xgige-10gbase-lr", 17),
          ("xgige-10gbase-lw", 20),
          ("xgige-10gbase-sr", 16),
          ("xgige-10gbase-sw", 19))
    )

_TmnxPortTransceiverCode_Type.__name__ = "Bits"
_TmnxPortTransceiverCode_Object = MibTableColumn
tmnxPortTransceiverCode = _TmnxPortTransceiverCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 26),
    _TmnxPortTransceiverCode_Type()
)
tmnxPortTransceiverCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTransceiverCode.setStatus("obsolete")
_TmnxPortTransceiverLaserWaveLen_Type = Unsigned32
_TmnxPortTransceiverLaserWaveLen_Object = MibTableColumn
tmnxPortTransceiverLaserWaveLen = _TmnxPortTransceiverLaserWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 27),
    _TmnxPortTransceiverLaserWaveLen_Type()
)
tmnxPortTransceiverLaserWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTransceiverLaserWaveLen.setStatus("current")


class _TmnxPortTransceiverDiagCapable_Type(Integer32):
    """Custom type tmnxPortTransceiverDiagCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notApplicable", 0),
          ("true", 1))
    )


_TmnxPortTransceiverDiagCapable_Type.__name__ = "Integer32"
_TmnxPortTransceiverDiagCapable_Object = MibTableColumn
tmnxPortTransceiverDiagCapable = _TmnxPortTransceiverDiagCapable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 28),
    _TmnxPortTransceiverDiagCapable_Type()
)
tmnxPortTransceiverDiagCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTransceiverDiagCapable.setStatus("current")
_TmnxPortTransceiverModelNumber_Type = TNamedItemOrEmpty
_TmnxPortTransceiverModelNumber_Object = MibTableColumn
tmnxPortTransceiverModelNumber = _TmnxPortTransceiverModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 29),
    _TmnxPortTransceiverModelNumber_Type()
)
tmnxPortTransceiverModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTransceiverModelNumber.setStatus("current")


class _TmnxPortSFPConnectorCode_Type(Integer32):
    """Custom type tmnxPortSFPConnectorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              32,
              33,
              128)
        )
    )
    namedValues = NamedValues(
        *(("bncortnc", 4),
          ("copperGigE", 128),
          ("copperPigtail", 33),
          ("fiberChannel-Style1-CopperConnector", 2),
          ("fiberChannel-Style2-CopperConnector", 3),
          ("fiberChannelCoaxialHeaders", 5),
          ("fiberJack", 6),
          ("hssdcII", 32),
          ("lc", 7),
          ("mt-rj", 8),
          ("mu", 9),
          ("opticalPigtail", 11),
          ("sc", 1),
          ("sg", 10),
          ("unknown", 0))
    )


_TmnxPortSFPConnectorCode_Type.__name__ = "Integer32"
_TmnxPortSFPConnectorCode_Object = MibTableColumn
tmnxPortSFPConnectorCode = _TmnxPortSFPConnectorCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 30),
    _TmnxPortSFPConnectorCode_Type()
)
tmnxPortSFPConnectorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPConnectorCode.setStatus("current")
_TmnxPortSFPVendorOUI_Type = Unsigned32
_TmnxPortSFPVendorOUI_Object = MibTableColumn
tmnxPortSFPVendorOUI = _TmnxPortSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 31),
    _TmnxPortSFPVendorOUI_Type()
)
tmnxPortSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPVendorOUI.setStatus("current")
_TmnxPortSFPVendorManufactureDate_Type = DateAndTime
_TmnxPortSFPVendorManufactureDate_Object = MibTableColumn
tmnxPortSFPVendorManufactureDate = _TmnxPortSFPVendorManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 32),
    _TmnxPortSFPVendorManufactureDate_Type()
)
tmnxPortSFPVendorManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPVendorManufactureDate.setStatus("current")


class _TmnxPortSFPMedia_Type(Integer32):
    """Custom type tmnxPortSFPMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("notApplicable", 0),
          ("sonetsdh", 2))
    )


_TmnxPortSFPMedia_Type.__name__ = "Integer32"
_TmnxPortSFPMedia_Object = MibTableColumn
tmnxPortSFPMedia = _TmnxPortSFPMedia_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 33),
    _TmnxPortSFPMedia_Type()
)
tmnxPortSFPMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPMedia.setStatus("current")
_TmnxPortSFPEquipped_Type = TruthValue
_TmnxPortSFPEquipped_Object = MibTableColumn
tmnxPortSFPEquipped = _TmnxPortSFPEquipped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 34),
    _TmnxPortSFPEquipped_Type()
)
tmnxPortSFPEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPEquipped.setStatus("current")
_TmnxPortEquipped_Type = TruthValue
_TmnxPortEquipped_Object = MibTableColumn
tmnxPortEquipped = _TmnxPortEquipped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 35),
    _TmnxPortEquipped_Type()
)
tmnxPortEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEquipped.setStatus("current")
_TmnxPortLinkStatus_Type = TruthValue
_TmnxPortLinkStatus_Object = MibTableColumn
tmnxPortLinkStatus = _TmnxPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 36),
    _TmnxPortLinkStatus_Type()
)
tmnxPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortLinkStatus.setStatus("current")


class _TmnxPortAdminStatus_Type(TmnxPortAdminStatus):
    """Custom type tmnxPortAdminStatus based on TmnxPortAdminStatus"""


_TmnxPortAdminStatus_Object = MibTableColumn
tmnxPortAdminStatus = _TmnxPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 37),
    _TmnxPortAdminStatus_Type()
)
tmnxPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortAdminStatus.setStatus("current")
_TmnxPortOperStatus_Type = TmnxPortOperStatus
_TmnxPortOperStatus_Object = MibTableColumn
tmnxPortOperStatus = _TmnxPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 38),
    _TmnxPortOperStatus_Type()
)
tmnxPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortOperStatus.setStatus("current")
_TmnxPortState_Type = TmnxPortState
_TmnxPortState_Object = MibTableColumn
tmnxPortState = _TmnxPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 39),
    _TmnxPortState_Type()
)
tmnxPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortState.setStatus("current")
_TmnxPortPrevState_Type = TmnxPortState
_TmnxPortPrevState_Object = MibTableColumn
tmnxPortPrevState = _TmnxPortPrevState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 40),
    _TmnxPortPrevState_Type()
)
tmnxPortPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortPrevState.setStatus("current")
_TmnxPortNumAlarms_Type = Unsigned32
_TmnxPortNumAlarms_Object = MibTableColumn
tmnxPortNumAlarms = _TmnxPortNumAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 41),
    _TmnxPortNumAlarms_Type()
)
tmnxPortNumAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNumAlarms.setStatus("current")
_TmnxPortAlarmState_Type = TmnxAlarmState
_TmnxPortAlarmState_Object = MibTableColumn
tmnxPortAlarmState = _TmnxPortAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 42),
    _TmnxPortAlarmState_Type()
)
tmnxPortAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortAlarmState.setStatus("current")
_TmnxPortLastAlarmEvent_Type = RowPointer
_TmnxPortLastAlarmEvent_Object = MibTableColumn
tmnxPortLastAlarmEvent = _TmnxPortLastAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 43),
    _TmnxPortLastAlarmEvent_Type()
)
tmnxPortLastAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortLastAlarmEvent.setStatus("current")


class _TmnxPortClearAlarms_Type(TmnxActionType):
    """Custom type tmnxPortClearAlarms based on TmnxActionType"""


_TmnxPortClearAlarms_Object = MibTableColumn
tmnxPortClearAlarms = _TmnxPortClearAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 44),
    _TmnxPortClearAlarms_Type()
)
tmnxPortClearAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortClearAlarms.setStatus("current")
_TmnxPortSFPVendorSerialNum_Type = TNamedItemOrEmpty
_TmnxPortSFPVendorSerialNum_Object = MibTableColumn
tmnxPortSFPVendorSerialNum = _TmnxPortSFPVendorSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 45),
    _TmnxPortSFPVendorSerialNum_Type()
)
tmnxPortSFPVendorSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPVendorSerialNum.setStatus("current")
_TmnxPortSFPVendorPartNum_Type = TNamedItemOrEmpty
_TmnxPortSFPVendorPartNum_Object = MibTableColumn
tmnxPortSFPVendorPartNum = _TmnxPortSFPVendorPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 46),
    _TmnxPortSFPVendorPartNum_Type()
)
tmnxPortSFPVendorPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPVendorPartNum.setStatus("current")
_TmnxPortLastStateChanged_Type = TimeStamp
_TmnxPortLastStateChanged_Object = MibTableColumn
tmnxPortLastStateChanged = _TmnxPortLastStateChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 48),
    _TmnxPortLastStateChanged_Type()
)
tmnxPortLastStateChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortLastStateChanged.setStatus("current")
_TmnxPortNumChannels_Type = Unsigned32
_TmnxPortNumChannels_Object = MibTableColumn
tmnxPortNumChannels = _TmnxPortNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 49),
    _TmnxPortNumChannels_Type()
)
tmnxPortNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNumChannels.setStatus("current")
_TmnxPortNetworkEgrQueues_Type = TNamedItemOrEmpty
_TmnxPortNetworkEgrQueues_Object = MibTableColumn
tmnxPortNetworkEgrQueues = _TmnxPortNetworkEgrQueues_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 50),
    _TmnxPortNetworkEgrQueues_Type()
)
tmnxPortNetworkEgrQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortNetworkEgrQueues.setStatus("current")


class _TmnxPortBundleNumber_Type(Integer32):
    """Custom type tmnxPortBundleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_TmnxPortBundleNumber_Type.__name__ = "Integer32"
_TmnxPortBundleNumber_Object = MibTableColumn
tmnxPortBundleNumber = _TmnxPortBundleNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 51),
    _TmnxPortBundleNumber_Type()
)
tmnxPortBundleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortBundleNumber.setStatus("current")
_TmnxPortIsLeaf_Type = TruthValue
_TmnxPortIsLeaf_Object = MibTableColumn
tmnxPortIsLeaf = _TmnxPortIsLeaf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 52),
    _TmnxPortIsLeaf_Type()
)
tmnxPortIsLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIsLeaf.setStatus("current")
_TmnxPortChanType_Type = TmnxMDAChanType
_TmnxPortChanType_Object = MibTableColumn
tmnxPortChanType = _TmnxPortChanType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 53),
    _TmnxPortChanType_Type()
)
tmnxPortChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortChanType.setStatus("current")
_TmnxPortParentPortID_Type = TmnxPortID
_TmnxPortParentPortID_Object = MibTableColumn
tmnxPortParentPortID = _TmnxPortParentPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 54),
    _TmnxPortParentPortID_Type()
)
tmnxPortParentPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortParentPortID.setStatus("current")


class _TmnxPortOpticalCompliance_Type(OctetString):
    """Custom type tmnxPortOpticalCompliance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_TmnxPortOpticalCompliance_Type.__name__ = "OctetString"
_TmnxPortOpticalCompliance_Object = MibTableColumn
tmnxPortOpticalCompliance = _TmnxPortOpticalCompliance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 55),
    _TmnxPortOpticalCompliance_Type()
)
tmnxPortOpticalCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortOpticalCompliance.setStatus("current")


class _TmnxPortLoadBalanceAlgorithm_Type(Integer32):
    """Custom type tmnxPortLoadBalanceAlgorithm based on Integer32"""
    defaultValue = 1

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
        *(("default", 1),
          ("excludeL4", 3),
          ("includeL4", 2),
          ("notApplicable", 0))
    )


_TmnxPortLoadBalanceAlgorithm_Type.__name__ = "Integer32"
_TmnxPortLoadBalanceAlgorithm_Object = MibTableColumn
tmnxPortLoadBalanceAlgorithm = _TmnxPortLoadBalanceAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 56),
    _TmnxPortLoadBalanceAlgorithm_Type()
)
tmnxPortLoadBalanceAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortLoadBalanceAlgorithm.setStatus("current")
_TmnxPortEgrPortSchedPlcy_Type = TNamedItemOrEmpty
_TmnxPortEgrPortSchedPlcy_Object = MibTableColumn
tmnxPortEgrPortSchedPlcy = _TmnxPortEgrPortSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 57),
    _TmnxPortEgrPortSchedPlcy_Type()
)
tmnxPortEgrPortSchedPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEgrPortSchedPlcy.setStatus("current")
_TmnxPortLastClearedTime_Type = TimeStamp
_TmnxPortLastClearedTime_Object = MibTableColumn
tmnxPortLastClearedTime = _TmnxPortLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 58),
    _TmnxPortLastClearedTime_Type()
)
tmnxPortLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortLastClearedTime.setStatus("current")
_TmnxPortEgrHsmdaSchedPlcy_Type = TNamedItemOrEmpty
_TmnxPortEgrHsmdaSchedPlcy_Object = MibTableColumn
tmnxPortEgrHsmdaSchedPlcy = _TmnxPortEgrHsmdaSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 59),
    _TmnxPortEgrHsmdaSchedPlcy_Type()
)
tmnxPortEgrHsmdaSchedPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEgrHsmdaSchedPlcy.setStatus("current")


class _TmnxPortIngNamedPoolPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxPortIngNamedPoolPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPortIngNamedPoolPlcy_Object = MibTableColumn
tmnxPortIngNamedPoolPlcy = _TmnxPortIngNamedPoolPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 60),
    _TmnxPortIngNamedPoolPlcy_Type()
)
tmnxPortIngNamedPoolPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortIngNamedPoolPlcy.setStatus("current")


class _TmnxPortEgrNamedPoolPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxPortEgrNamedPoolPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPortEgrNamedPoolPlcy_Object = MibTableColumn
tmnxPortEgrNamedPoolPlcy = _TmnxPortEgrNamedPoolPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 61),
    _TmnxPortEgrNamedPoolPlcy_Type()
)
tmnxPortEgrNamedPoolPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEgrNamedPoolPlcy.setStatus("current")


class _TmnxPortIngPoolPercentRate_Type(Unsigned32):
    """Custom type tmnxPortIngPoolPercentRate based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxPortIngPoolPercentRate_Type.__name__ = "Unsigned32"
_TmnxPortIngPoolPercentRate_Object = MibTableColumn
tmnxPortIngPoolPercentRate = _TmnxPortIngPoolPercentRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 62),
    _TmnxPortIngPoolPercentRate_Type()
)
tmnxPortIngPoolPercentRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortIngPoolPercentRate.setStatus("current")


class _TmnxPortEgrPoolPercentRate_Type(Unsigned32):
    """Custom type tmnxPortEgrPoolPercentRate based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxPortEgrPoolPercentRate_Type.__name__ = "Unsigned32"
_TmnxPortEgrPoolPercentRate_Object = MibTableColumn
tmnxPortEgrPoolPercentRate = _TmnxPortEgrPoolPercentRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 63),
    _TmnxPortEgrPoolPercentRate_Type()
)
tmnxPortEgrPoolPercentRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEgrPoolPercentRate.setStatus("current")


class _TmnxPortDDMEventSuppression_Type(TruthValue):
    """Custom type tmnxPortDDMEventSuppression based on TruthValue"""


_TmnxPortDDMEventSuppression_Object = MibTableColumn
tmnxPortDDMEventSuppression = _TmnxPortDDMEventSuppression_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 64),
    _TmnxPortDDMEventSuppression_Type()
)
tmnxPortDDMEventSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortDDMEventSuppression.setStatus("current")


class _TmnxPortSFPStatus_Type(Integer32):
    """Custom type tmnxPortSFPStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("data-corrupt", 3),
          ("ddm-corrupt", 4),
          ("not-equipped", 0),
          ("operational", 1),
          ("read-error", 2),
          ("unsupported", 5))
    )


_TmnxPortSFPStatus_Type.__name__ = "Integer32"
_TmnxPortSFPStatus_Object = MibTableColumn
tmnxPortSFPStatus = _TmnxPortSFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 65),
    _TmnxPortSFPStatus_Type()
)
tmnxPortSFPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPStatus.setStatus("current")


class _TmnxPortReasonDownFlags_Type(Bits):
    """Custom type tmnxPortReasonDownFlags based on Bits"""
    namedValues = NamedValues(
        *(("channelNotConfigured", 6),
          ("channelOutOfRange", 5),
          ("crcError", 7),
          ("ethCfmFault", 3),
          ("internalMacTxError", 8),
          ("lagMemberPortStandby", 2),
          ("linklossFwd", 1),
          ("noServicePort", 9),
          ("opticalTuning", 4),
          ("unknown", 0))
    )

_TmnxPortReasonDownFlags_Type.__name__ = "Bits"
_TmnxPortReasonDownFlags_Object = MibTableColumn
tmnxPortReasonDownFlags = _TmnxPortReasonDownFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 66),
    _TmnxPortReasonDownFlags_Type()
)
tmnxPortReasonDownFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortReasonDownFlags.setStatus("current")


class _TmnxPortSSMRxQualityLevel_Type(Integer32):
    """Custom type tmnxPortSSMRxQualityLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 14),
          ("dus", 9),
          ("eec1", 17),
          ("eec2", 18),
          ("failed", 19),
          ("inv", 15),
          ("pno", 16),
          ("prc", 10),
          ("prs", 1),
          ("sec", 13),
          ("smc", 7),
          ("ssua", 11),
          ("ssub", 12),
          ("st2", 3),
          ("st3", 6),
          ("st3e", 5),
          ("st4", 8),
          ("stu", 2),
          ("tnc", 4),
          ("unknown", 0))
    )


_TmnxPortSSMRxQualityLevel_Type.__name__ = "Integer32"
_TmnxPortSSMRxQualityLevel_Object = MibTableColumn
tmnxPortSSMRxQualityLevel = _TmnxPortSSMRxQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 67),
    _TmnxPortSSMRxQualityLevel_Type()
)
tmnxPortSSMRxQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSSMRxQualityLevel.setStatus("current")


class _TmnxPortDwdmLaserChannel_Type(TmnxOpticalDwdmChannel):
    """Custom type tmnxPortDwdmLaserChannel based on TmnxOpticalDwdmChannel"""
    defaultValue = 0


_TmnxPortDwdmLaserChannel_Object = MibTableColumn
tmnxPortDwdmLaserChannel = _TmnxPortDwdmLaserChannel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 68),
    _TmnxPortDwdmLaserChannel_Type()
)
tmnxPortDwdmLaserChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortDwdmLaserChannel.setStatus("current")
_TmnxPortOtuCapable_Type = TruthValue
_TmnxPortOtuCapable_Object = MibTableColumn
tmnxPortOtuCapable = _TmnxPortOtuCapable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 69),
    _TmnxPortOtuCapable_Type()
)
tmnxPortOtuCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortOtuCapable.setStatus("current")
_TmnxPortWaveTrackerCapable_Type = TruthValue
_TmnxPortWaveTrackerCapable_Object = MibTableColumn
tmnxPortWaveTrackerCapable = _TmnxPortWaveTrackerCapable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 70),
    _TmnxPortWaveTrackerCapable_Type()
)
tmnxPortWaveTrackerCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortWaveTrackerCapable.setStatus("current")


class _TmnxPortHybridIngAccessWeight_Type(Unsigned32):
    """Custom type tmnxPortHybridIngAccessWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxPortHybridIngAccessWeight_Type.__name__ = "Unsigned32"
_TmnxPortHybridIngAccessWeight_Object = MibTableColumn
tmnxPortHybridIngAccessWeight = _TmnxPortHybridIngAccessWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 71),
    _TmnxPortHybridIngAccessWeight_Type()
)
tmnxPortHybridIngAccessWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortHybridIngAccessWeight.setStatus("current")


class _TmnxPortHybridIngNetworkWeight_Type(Unsigned32):
    """Custom type tmnxPortHybridIngNetworkWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxPortHybridIngNetworkWeight_Type.__name__ = "Unsigned32"
_TmnxPortHybridIngNetworkWeight_Object = MibTableColumn
tmnxPortHybridIngNetworkWeight = _TmnxPortHybridIngNetworkWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 72),
    _TmnxPortHybridIngNetworkWeight_Type()
)
tmnxPortHybridIngNetworkWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortHybridIngNetworkWeight.setStatus("current")


class _TmnxPortHybridEgrAccessWeight_Type(Unsigned32):
    """Custom type tmnxPortHybridEgrAccessWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxPortHybridEgrAccessWeight_Type.__name__ = "Unsigned32"
_TmnxPortHybridEgrAccessWeight_Object = MibTableColumn
tmnxPortHybridEgrAccessWeight = _TmnxPortHybridEgrAccessWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 73),
    _TmnxPortHybridEgrAccessWeight_Type()
)
tmnxPortHybridEgrAccessWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortHybridEgrAccessWeight.setStatus("current")


class _TmnxPortHybridEgrNetworkWeight_Type(Unsigned32):
    """Custom type tmnxPortHybridEgrNetworkWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxPortHybridEgrNetworkWeight_Type.__name__ = "Unsigned32"
_TmnxPortHybridEgrNetworkWeight_Object = MibTableColumn
tmnxPortHybridEgrNetworkWeight = _TmnxPortHybridEgrNetworkWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 74),
    _TmnxPortHybridEgrNetworkWeight_Type()
)
tmnxPortHybridEgrNetworkWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortHybridEgrNetworkWeight.setStatus("current")


class _TmnxPortDwdmRxDtvAdjustEnable_Type(TruthValue):
    """Custom type tmnxPortDwdmRxDtvAdjustEnable based on TruthValue"""


_TmnxPortDwdmRxDtvAdjustEnable_Object = MibTableColumn
tmnxPortDwdmRxDtvAdjustEnable = _TmnxPortDwdmRxDtvAdjustEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 75),
    _TmnxPortDwdmRxDtvAdjustEnable_Type()
)
tmnxPortDwdmRxDtvAdjustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortDwdmRxDtvAdjustEnable.setStatus("current")


class _TmnxPortDwdmRxDtvDacPercent_Type(Unsigned32):
    """Custom type tmnxPortDwdmRxDtvDacPercent based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TmnxPortDwdmRxDtvDacPercent_Type.__name__ = "Unsigned32"
_TmnxPortDwdmRxDtvDacPercent_Object = MibTableColumn
tmnxPortDwdmRxDtvDacPercent = _TmnxPortDwdmRxDtvDacPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 76),
    _TmnxPortDwdmRxDtvDacPercent_Type()
)
tmnxPortDwdmRxDtvDacPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortDwdmRxDtvDacPercent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortDwdmRxDtvDacPercent.setUnits("Hundredths of a percent")
_TmnxPortInterfaceGroupHandlerIdx_Type = Unsigned32
_TmnxPortInterfaceGroupHandlerIdx_Object = MibTableColumn
tmnxPortInterfaceGroupHandlerIdx = _TmnxPortInterfaceGroupHandlerIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 77),
    _TmnxPortInterfaceGroupHandlerIdx_Type()
)
tmnxPortInterfaceGroupHandlerIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortInterfaceGroupHandlerIdx.setStatus("current")


class _TmnxPortHoldTimeUnits_Type(Integer32):
    """Custom type tmnxPortHoldTimeUnits based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("centiseconds", 1),
          ("seconds", 0))
    )


_TmnxPortHoldTimeUnits_Type.__name__ = "Integer32"
_TmnxPortHoldTimeUnits_Object = MibTableColumn
tmnxPortHoldTimeUnits = _TmnxPortHoldTimeUnits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 78),
    _TmnxPortHoldTimeUnits_Type()
)
tmnxPortHoldTimeUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortHoldTimeUnits.setStatus("current")


class _TmnxPortLinkLengthInfo_Type(OctetString):
    """Custom type tmnxPortLinkLengthInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TmnxPortLinkLengthInfo_Type.__name__ = "OctetString"
_TmnxPortLinkLengthInfo_Object = MibTableColumn
tmnxPortLinkLengthInfo = _TmnxPortLinkLengthInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 79),
    _TmnxPortLinkLengthInfo_Type()
)
tmnxPortLinkLengthInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortLinkLengthInfo.setStatus("current")
_TmnxPortSFPNumLanes_Type = Unsigned32
_TmnxPortSFPNumLanes_Object = MibTableColumn
tmnxPortSFPNumLanes = _TmnxPortSFPNumLanes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 80),
    _TmnxPortSFPNumLanes_Type()
)
tmnxPortSFPNumLanes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSFPNumLanes.setStatus("current")
_TmnxPortPhysStateChangeCount_Type = Counter32
_TmnxPortPhysStateChangeCount_Object = MibTableColumn
tmnxPortPhysStateChangeCount = _TmnxPortPhysStateChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 2, 1, 81),
    _TmnxPortPhysStateChangeCount_Type()
)
tmnxPortPhysStateChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortPhysStateChangeCount.setStatus("current")
_TmnxPortTestTable_Object = MibTable
tmnxPortTestTable = _TmnxPortTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    tmnxPortTestTable.setStatus("current")
_TmnxPortTestEntry_Object = MibTableRow
tmnxPortTestEntry = _TmnxPortTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxPortTestEntry.setStatus("current")


class _TmnxPortTestState_Type(Integer32):
    """Custom type tmnxPortTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inTest", 2),
          ("notInTest", 1))
    )


_TmnxPortTestState_Type.__name__ = "Integer32"
_TmnxPortTestState_Object = MibTableColumn
tmnxPortTestState = _TmnxPortTestState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 1),
    _TmnxPortTestState_Type()
)
tmnxPortTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTestState.setStatus("current")


class _TmnxPortTestMode_Type(Integer32):
    """Custom type tmnxPortTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("loopback1", 1),
          ("loopback2", 2),
          ("loopback3", 3),
          ("notApplicable", 0),
          ("singalInsertion", 4))
    )


_TmnxPortTestMode_Type.__name__ = "Integer32"
_TmnxPortTestMode_Object = MibTableColumn
tmnxPortTestMode = _TmnxPortTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 2),
    _TmnxPortTestMode_Type()
)
tmnxPortTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortTestMode.setStatus("current")
_TmnxPortTestParameter_Type = Unsigned32
_TmnxPortTestParameter_Object = MibTableColumn
tmnxPortTestParameter = _TmnxPortTestParameter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 3),
    _TmnxPortTestParameter_Type()
)
tmnxPortTestParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortTestParameter.setStatus("current")


class _TmnxPortTestLastResult_Type(Integer32):
    """Custom type tmnxPortTestLastResult based on Integer32"""
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
        *(("failure", 2),
          ("notApplicable", 0),
          ("success", 1),
          ("timeout", 3))
    )


_TmnxPortTestLastResult_Type.__name__ = "Integer32"
_TmnxPortTestLastResult_Object = MibTableColumn
tmnxPortTestLastResult = _TmnxPortTestLastResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 4),
    _TmnxPortTestLastResult_Type()
)
tmnxPortTestLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTestLastResult.setStatus("current")
_TmnxPortTestStartTime_Type = DateAndTime
_TmnxPortTestStartTime_Object = MibTableColumn
tmnxPortTestStartTime = _TmnxPortTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 5),
    _TmnxPortTestStartTime_Type()
)
tmnxPortTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTestStartTime.setStatus("current")
_TmnxPortTestEndTime_Type = DateAndTime
_TmnxPortTestEndTime_Object = MibTableColumn
tmnxPortTestEndTime = _TmnxPortTestEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 6),
    _TmnxPortTestEndTime_Type()
)
tmnxPortTestEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTestEndTime.setStatus("current")


class _TmnxPortTestDuration_Type(Integer32):
    """Custom type tmnxPortTestDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TmnxPortTestDuration_Type.__name__ = "Integer32"
_TmnxPortTestDuration_Object = MibTableColumn
tmnxPortTestDuration = _TmnxPortTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 7),
    _TmnxPortTestDuration_Type()
)
tmnxPortTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortTestDuration.setStatus("current")


class _TmnxPortTestAction_Type(Integer32):
    """Custom type tmnxPortTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("startTest", 2),
          ("stopTest", 3))
    )


_TmnxPortTestAction_Type.__name__ = "Integer32"
_TmnxPortTestAction_Object = MibTableColumn
tmnxPortTestAction = _TmnxPortTestAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 3, 1, 8),
    _TmnxPortTestAction_Type()
)
tmnxPortTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortTestAction.setStatus("current")
_TmnxPortEtherTable_Object = MibTable
tmnxPortEtherTable = _TmnxPortEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    tmnxPortEtherTable.setStatus("current")
_TmnxPortEtherEntry_Object = MibTableRow
tmnxPortEtherEntry = _TmnxPortEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1)
)
tmnxPortEtherEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxPortEtherEntry.setStatus("current")


class _TmnxPortEtherMTU_Type(Unsigned32):
    """Custom type tmnxPortEtherMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9212),
    )


_TmnxPortEtherMTU_Type.__name__ = "Unsigned32"
_TmnxPortEtherMTU_Object = MibTableColumn
tmnxPortEtherMTU = _TmnxPortEtherMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 1),
    _TmnxPortEtherMTU_Type()
)
tmnxPortEtherMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherMTU.setUnits("bytes")


class _TmnxPortEtherDuplex_Type(Integer32):
    """Custom type tmnxPortEtherDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("notApplicable", 0))
    )


_TmnxPortEtherDuplex_Type.__name__ = "Integer32"
_TmnxPortEtherDuplex_Object = MibTableColumn
tmnxPortEtherDuplex = _TmnxPortEtherDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 2),
    _TmnxPortEtherDuplex_Type()
)
tmnxPortEtherDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDuplex.setStatus("current")


class _TmnxPortEtherSpeed_Type(Integer32):
    """Custom type tmnxPortEtherSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3),
          ("speed10000", 4),
          ("speed100000", 6),
          ("speed25000", 7),
          ("speed40000", 5))
    )


_TmnxPortEtherSpeed_Type.__name__ = "Integer32"
_TmnxPortEtherSpeed_Object = MibTableColumn
tmnxPortEtherSpeed = _TmnxPortEtherSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 3),
    _TmnxPortEtherSpeed_Type()
)
tmnxPortEtherSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherSpeed.setStatus("current")


class _TmnxPortEtherAutoNegotiate_Type(Integer32):
    """Custom type tmnxPortEtherAutoNegotiate based on Integer32"""
    defaultValue = 1

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
        *(("false", 2),
          ("limited", 3),
          ("notApplicable", 0),
          ("true", 1))
    )


_TmnxPortEtherAutoNegotiate_Type.__name__ = "Integer32"
_TmnxPortEtherAutoNegotiate_Object = MibTableColumn
tmnxPortEtherAutoNegotiate = _TmnxPortEtherAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 4),
    _TmnxPortEtherAutoNegotiate_Type()
)
tmnxPortEtherAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherAutoNegotiate.setStatus("current")


class _TmnxPortEtherOperDuplex_Type(Integer32):
    """Custom type tmnxPortEtherOperDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("notApplicable", 0))
    )


_TmnxPortEtherOperDuplex_Type.__name__ = "Integer32"
_TmnxPortEtherOperDuplex_Object = MibTableColumn
tmnxPortEtherOperDuplex = _TmnxPortEtherOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 5),
    _TmnxPortEtherOperDuplex_Type()
)
tmnxPortEtherOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherOperDuplex.setStatus("current")
_TmnxPortEtherOperSpeed_Type = Unsigned32
_TmnxPortEtherOperSpeed_Object = MibTableColumn
tmnxPortEtherOperSpeed = _TmnxPortEtherOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 6),
    _TmnxPortEtherOperSpeed_Type()
)
tmnxPortEtherOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherOperSpeed.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherOperSpeed.setUnits("mega-bits per second")


class _TmnxPortEtherAcctPolicyId_Type(Unsigned32):
    """Custom type tmnxPortEtherAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxPortEtherAcctPolicyId_Type.__name__ = "Unsigned32"
_TmnxPortEtherAcctPolicyId_Object = MibTableColumn
tmnxPortEtherAcctPolicyId = _TmnxPortEtherAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 7),
    _TmnxPortEtherAcctPolicyId_Type()
)
tmnxPortEtherAcctPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherAcctPolicyId.setStatus("current")


class _TmnxPortEtherCollectStats_Type(TruthValue):
    """Custom type tmnxPortEtherCollectStats based on TruthValue"""


_TmnxPortEtherCollectStats_Object = MibTableColumn
tmnxPortEtherCollectStats = _TmnxPortEtherCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 8),
    _TmnxPortEtherCollectStats_Type()
)
tmnxPortEtherCollectStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherCollectStats.setStatus("current")


class _TmnxPortEtherMDIMDIX_Type(Integer32):
    """Custom type tmnxPortEtherMDIMDIX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2),
          ("unknown", 0))
    )


_TmnxPortEtherMDIMDIX_Type.__name__ = "Integer32"
_TmnxPortEtherMDIMDIX_Object = MibTableColumn
tmnxPortEtherMDIMDIX = _TmnxPortEtherMDIMDIX_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 9),
    _TmnxPortEtherMDIMDIX_Type()
)
tmnxPortEtherMDIMDIX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherMDIMDIX.setStatus("current")


class _TmnxPortEtherXGigMode_Type(Integer32):
    """Custom type tmnxPortEtherXGigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("notApplicable", 0),
          ("wan", 2))
    )


_TmnxPortEtherXGigMode_Type.__name__ = "Integer32"
_TmnxPortEtherXGigMode_Object = MibTableColumn
tmnxPortEtherXGigMode = _TmnxPortEtherXGigMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 10),
    _TmnxPortEtherXGigMode_Type()
)
tmnxPortEtherXGigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherXGigMode.setStatus("current")


class _TmnxPortEtherEgressRate_Type(Integer32):
    """Custom type tmnxPortEtherEgressRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )


_TmnxPortEtherEgressRate_Type.__name__ = "Integer32"
_TmnxPortEtherEgressRate_Object = MibTableColumn
tmnxPortEtherEgressRate = _TmnxPortEtherEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 11),
    _TmnxPortEtherEgressRate_Type()
)
tmnxPortEtherEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherEgressRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherEgressRate.setUnits("kilo-bits per second")


class _TmnxPortEtherDot1qEtype_Type(Unsigned32):
    """Custom type tmnxPortEtherDot1qEtype based on Unsigned32"""
    defaultHexValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TmnxPortEtherDot1qEtype_Type.__name__ = "Unsigned32"
_TmnxPortEtherDot1qEtype_Object = MibTableColumn
tmnxPortEtherDot1qEtype = _TmnxPortEtherDot1qEtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 12),
    _TmnxPortEtherDot1qEtype_Type()
)
tmnxPortEtherDot1qEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDot1qEtype.setStatus("current")


class _TmnxPortEtherQinqEtype_Type(Unsigned32):
    """Custom type tmnxPortEtherQinqEtype based on Unsigned32"""
    defaultHexValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TmnxPortEtherQinqEtype_Type.__name__ = "Unsigned32"
_TmnxPortEtherQinqEtype_Object = MibTableColumn
tmnxPortEtherQinqEtype = _TmnxPortEtherQinqEtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 13),
    _TmnxPortEtherQinqEtype_Type()
)
tmnxPortEtherQinqEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherQinqEtype.setStatus("current")


class _TmnxPortEtherIngressRate_Type(Integer32):
    """Custom type tmnxPortEtherIngressRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000),
    )


_TmnxPortEtherIngressRate_Type.__name__ = "Integer32"
_TmnxPortEtherIngressRate_Object = MibTableColumn
tmnxPortEtherIngressRate = _TmnxPortEtherIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 14),
    _TmnxPortEtherIngressRate_Type()
)
tmnxPortEtherIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherIngressRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherIngressRate.setUnits("mega-bits per second")


class _TmnxPortEtherReportAlarm_Type(TmnxPortEtherReportStatus):
    """Custom type tmnxPortEtherReportAlarm based on TmnxPortEtherReportStatus"""
    defaultBinValue = "0011"


_TmnxPortEtherReportAlarm_Object = MibTableColumn
tmnxPortEtherReportAlarm = _TmnxPortEtherReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 15),
    _TmnxPortEtherReportAlarm_Type()
)
tmnxPortEtherReportAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherReportAlarm.setStatus("current")
_TmnxPortEtherReportAlarmStatus_Type = TmnxPortEtherReportStatus
_TmnxPortEtherReportAlarmStatus_Object = MibTableColumn
tmnxPortEtherReportAlarmStatus = _TmnxPortEtherReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 16),
    _TmnxPortEtherReportAlarmStatus_Type()
)
tmnxPortEtherReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherReportAlarmStatus.setStatus("current")
_TmnxPortEtherPkts1519toMax_Type = Counter32
_TmnxPortEtherPkts1519toMax_Object = MibTableColumn
tmnxPortEtherPkts1519toMax = _TmnxPortEtherPkts1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 17),
    _TmnxPortEtherPkts1519toMax_Type()
)
tmnxPortEtherPkts1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherPkts1519toMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherPkts1519toMax.setUnits("Packets")
_TmnxPortEtherHCOverPkts1519toMax_Type = Counter32
_TmnxPortEtherHCOverPkts1519toMax_Object = MibTableColumn
tmnxPortEtherHCOverPkts1519toMax = _TmnxPortEtherHCOverPkts1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 18),
    _TmnxPortEtherHCOverPkts1519toMax_Type()
)
tmnxPortEtherHCOverPkts1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherHCOverPkts1519toMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherHCOverPkts1519toMax.setUnits("Packets")
_TmnxPortEtherHCPkts1519toMax_Type = Counter64
_TmnxPortEtherHCPkts1519toMax_Object = MibTableColumn
tmnxPortEtherHCPkts1519toMax = _TmnxPortEtherHCPkts1519toMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 19),
    _TmnxPortEtherHCPkts1519toMax_Type()
)
tmnxPortEtherHCPkts1519toMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherHCPkts1519toMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherHCPkts1519toMax.setUnits("Packets")


class _TmnxPortEtherLacpTunnel_Type(TruthValue):
    """Custom type tmnxPortEtherLacpTunnel based on TruthValue"""


_TmnxPortEtherLacpTunnel_Object = MibTableColumn
tmnxPortEtherLacpTunnel = _TmnxPortEtherLacpTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 20),
    _TmnxPortEtherLacpTunnel_Type()
)
tmnxPortEtherLacpTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherLacpTunnel.setStatus("current")


class _TmnxPortEtherDownWhenLoopedEnabled_Type(TruthValue):
    """Custom type tmnxPortEtherDownWhenLoopedEnabled based on TruthValue"""


_TmnxPortEtherDownWhenLoopedEnabled_Object = MibTableColumn
tmnxPortEtherDownWhenLoopedEnabled = _TmnxPortEtherDownWhenLoopedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 21),
    _TmnxPortEtherDownWhenLoopedEnabled_Type()
)
tmnxPortEtherDownWhenLoopedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedEnabled.setStatus("current")


class _TmnxPortEtherDownWhenLoopedKeepAlive_Type(Unsigned32):
    """Custom type tmnxPortEtherDownWhenLoopedKeepAlive based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_TmnxPortEtherDownWhenLoopedKeepAlive_Type.__name__ = "Unsigned32"
_TmnxPortEtherDownWhenLoopedKeepAlive_Object = MibTableColumn
tmnxPortEtherDownWhenLoopedKeepAlive = _TmnxPortEtherDownWhenLoopedKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 22),
    _TmnxPortEtherDownWhenLoopedKeepAlive_Type()
)
tmnxPortEtherDownWhenLoopedKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedKeepAlive.setUnits("seconds")


class _TmnxPortEtherDownWhenLoopedRetry_Type(Unsigned32):
    """Custom type tmnxPortEtherDownWhenLoopedRetry based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 160),
    )


_TmnxPortEtherDownWhenLoopedRetry_Type.__name__ = "Unsigned32"
_TmnxPortEtherDownWhenLoopedRetry_Object = MibTableColumn
tmnxPortEtherDownWhenLoopedRetry = _TmnxPortEtherDownWhenLoopedRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 23),
    _TmnxPortEtherDownWhenLoopedRetry_Type()
)
tmnxPortEtherDownWhenLoopedRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedRetry.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedRetry.setUnits("seconds")


class _TmnxPortEtherDownWhenLoopedState_Type(Integer32):
    """Custom type tmnxPortEtherDownWhenLoopedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopDetected", 2),
          ("noLoopDetected", 1))
    )


_TmnxPortEtherDownWhenLoopedState_Type.__name__ = "Integer32"
_TmnxPortEtherDownWhenLoopedState_Object = MibTableColumn
tmnxPortEtherDownWhenLoopedState = _TmnxPortEtherDownWhenLoopedState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 24),
    _TmnxPortEtherDownWhenLoopedState_Type()
)
tmnxPortEtherDownWhenLoopedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherDownWhenLoopedState.setStatus("current")


class _TmnxPortEtherPBBEtype_Type(Unsigned32):
    """Custom type tmnxPortEtherPBBEtype based on Unsigned32"""
    defaultHexValue = 35047

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TmnxPortEtherPBBEtype_Type.__name__ = "Unsigned32"
_TmnxPortEtherPBBEtype_Object = MibTableColumn
tmnxPortEtherPBBEtype = _TmnxPortEtherPBBEtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 25),
    _TmnxPortEtherPBBEtype_Type()
)
tmnxPortEtherPBBEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherPBBEtype.setStatus("current")


class _TmnxPortEtherReasonDownFlags_Type(Bits):
    """Custom type tmnxPortEtherReasonDownFlags based on Bits"""
    namedValues = NamedValues(
        *(("lagMemberPortStandby", 2),
          ("linklossFwd", 1),
          ("unknown", 0))
    )

_TmnxPortEtherReasonDownFlags_Type.__name__ = "Bits"
_TmnxPortEtherReasonDownFlags_Object = MibTableColumn
tmnxPortEtherReasonDownFlags = _TmnxPortEtherReasonDownFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 26),
    _TmnxPortEtherReasonDownFlags_Type()
)
tmnxPortEtherReasonDownFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherReasonDownFlags.setStatus("obsolete")


class _TmnxPortEtherSingleFiber_Type(TruthValue):
    """Custom type tmnxPortEtherSingleFiber based on TruthValue"""


_TmnxPortEtherSingleFiber_Object = MibTableColumn
tmnxPortEtherSingleFiber = _TmnxPortEtherSingleFiber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 27),
    _TmnxPortEtherSingleFiber_Type()
)
tmnxPortEtherSingleFiber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherSingleFiber.setStatus("current")


class _TmnxPortEtherSSM_Type(TruthValue):
    """Custom type tmnxPortEtherSSM based on TruthValue"""


_TmnxPortEtherSSM_Object = MibTableColumn
tmnxPortEtherSSM = _TmnxPortEtherSSM_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 28),
    _TmnxPortEtherSSM_Type()
)
tmnxPortEtherSSM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherSSM.setStatus("current")


class _TmnxPortEtherDWLUseBroadcastAddr_Type(TruthValue):
    """Custom type tmnxPortEtherDWLUseBroadcastAddr based on TruthValue"""


_TmnxPortEtherDWLUseBroadcastAddr_Object = MibTableColumn
tmnxPortEtherDWLUseBroadcastAddr = _TmnxPortEtherDWLUseBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 29),
    _TmnxPortEtherDWLUseBroadcastAddr_Type()
)
tmnxPortEtherDWLUseBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDWLUseBroadcastAddr.setStatus("current")


class _TmnxPortEtherSSMCodeType_Type(Integer32):
    """Custom type tmnxPortEtherSSMCodeType based on Integer32"""
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
        *(("sdh", 3),
          ("sonet", 2),
          ("unknown", 1))
    )


_TmnxPortEtherSSMCodeType_Type.__name__ = "Integer32"
_TmnxPortEtherSSMCodeType_Object = MibTableColumn
tmnxPortEtherSSMCodeType = _TmnxPortEtherSSMCodeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 30),
    _TmnxPortEtherSSMCodeType_Type()
)
tmnxPortEtherSSMCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherSSMCodeType.setStatus("current")


class _TmnxPortEtherSSMTxDus_Type(TruthValue):
    """Custom type tmnxPortEtherSSMTxDus based on TruthValue"""


_TmnxPortEtherSSMTxDus_Object = MibTableColumn
tmnxPortEtherSSMTxDus = _TmnxPortEtherSSMTxDus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 31),
    _TmnxPortEtherSSMTxDus_Type()
)
tmnxPortEtherSSMTxDus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherSSMTxDus.setStatus("current")


class _TmnxPortEtherSSMRxEsmc_Type(Unsigned32):
    """Custom type tmnxPortEtherSSMRxEsmc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxPortEtherSSMRxEsmc_Type.__name__ = "Unsigned32"
_TmnxPortEtherSSMRxEsmc_Object = MibTableColumn
tmnxPortEtherSSMRxEsmc = _TmnxPortEtherSSMRxEsmc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 32),
    _TmnxPortEtherSSMRxEsmc_Type()
)
tmnxPortEtherSSMRxEsmc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherSSMRxEsmc.setStatus("current")


class _TmnxPortEtherSSMTxQualityLevel_Type(Integer32):
    """Custom type tmnxPortEtherSSMTxQualityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 14),
          ("dus", 9),
          ("eec1", 17),
          ("eec2", 18),
          ("pno", 16),
          ("prc", 10),
          ("prs", 1),
          ("reserved0", 0),
          ("reserved13", 13),
          ("reserved15", 15),
          ("reserved19", 19),
          ("reserved6", 6),
          ("reserved8", 8),
          ("smc", 7),
          ("ssua", 11),
          ("ssub", 12),
          ("st2", 3),
          ("st3e", 5),
          ("stu", 2),
          ("tnc", 4))
    )


_TmnxPortEtherSSMTxQualityLevel_Type.__name__ = "Integer32"
_TmnxPortEtherSSMTxQualityLevel_Object = MibTableColumn
tmnxPortEtherSSMTxQualityLevel = _TmnxPortEtherSSMTxQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 33),
    _TmnxPortEtherSSMTxQualityLevel_Type()
)
tmnxPortEtherSSMTxQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherSSMTxQualityLevel.setStatus("current")


class _TmnxPortEtherCrcMonSdThreshold_Type(Unsigned32):
    """Custom type tmnxPortEtherCrcMonSdThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_TmnxPortEtherCrcMonSdThreshold_Type.__name__ = "Unsigned32"
_TmnxPortEtherCrcMonSdThreshold_Object = MibTableColumn
tmnxPortEtherCrcMonSdThreshold = _TmnxPortEtherCrcMonSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 34),
    _TmnxPortEtherCrcMonSdThreshold_Type()
)
tmnxPortEtherCrcMonSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherCrcMonSdThreshold.setStatus("current")


class _TmnxPortEtherCrcMonSdTMultiplier_Type(Unsigned32):
    """Custom type tmnxPortEtherCrcMonSdTMultiplier based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TmnxPortEtherCrcMonSdTMultiplier_Type.__name__ = "Unsigned32"
_TmnxPortEtherCrcMonSdTMultiplier_Object = MibTableColumn
tmnxPortEtherCrcMonSdTMultiplier = _TmnxPortEtherCrcMonSdTMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 35),
    _TmnxPortEtherCrcMonSdTMultiplier_Type()
)
tmnxPortEtherCrcMonSdTMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherCrcMonSdTMultiplier.setStatus("current")


class _TmnxPortEtherCrcMonSfThreshold_Type(Unsigned32):
    """Custom type tmnxPortEtherCrcMonSfThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_TmnxPortEtherCrcMonSfThreshold_Type.__name__ = "Unsigned32"
_TmnxPortEtherCrcMonSfThreshold_Object = MibTableColumn
tmnxPortEtherCrcMonSfThreshold = _TmnxPortEtherCrcMonSfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 36),
    _TmnxPortEtherCrcMonSfThreshold_Type()
)
tmnxPortEtherCrcMonSfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherCrcMonSfThreshold.setStatus("current")


class _TmnxPortEtherCrcMonSfTMultiplier_Type(Unsigned32):
    """Custom type tmnxPortEtherCrcMonSfTMultiplier based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TmnxPortEtherCrcMonSfTMultiplier_Type.__name__ = "Unsigned32"
_TmnxPortEtherCrcMonSfTMultiplier_Object = MibTableColumn
tmnxPortEtherCrcMonSfTMultiplier = _TmnxPortEtherCrcMonSfTMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 37),
    _TmnxPortEtherCrcMonSfTMultiplier_Type()
)
tmnxPortEtherCrcMonSfTMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherCrcMonSfTMultiplier.setStatus("current")


class _TmnxPortEtherCrcMonWindowSize_Type(Unsigned32):
    """Custom type tmnxPortEtherCrcMonWindowSize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_TmnxPortEtherCrcMonWindowSize_Type.__name__ = "Unsigned32"
_TmnxPortEtherCrcMonWindowSize_Object = MibTableColumn
tmnxPortEtherCrcMonWindowSize = _TmnxPortEtherCrcMonWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 38),
    _TmnxPortEtherCrcMonWindowSize_Type()
)
tmnxPortEtherCrcMonWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherCrcMonWindowSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherCrcMonWindowSize.setUnits("seconds")
_TmnxPortEtherCrcAlarmReason_Type = TmnxPortEtherCrcMonReportStatus
_TmnxPortEtherCrcAlarmReason_Object = MibTableColumn
tmnxPortEtherCrcAlarmReason = _TmnxPortEtherCrcAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 39),
    _TmnxPortEtherCrcAlarmReason_Type()
)
tmnxPortEtherCrcAlarmReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherCrcAlarmReason.setStatus("current")


class _TmnxPortEtherDownOnInternalError_Type(TruthValue):
    """Custom type tmnxPortEtherDownOnInternalError based on TruthValue"""


_TmnxPortEtherDownOnInternalError_Object = MibTableColumn
tmnxPortEtherDownOnInternalError = _TmnxPortEtherDownOnInternalError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 40),
    _TmnxPortEtherDownOnInternalError_Type()
)
tmnxPortEtherDownOnInternalError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDownOnInternalError.setStatus("current")


class _TmnxPortEtherMinFrameLength_Type(Unsigned32):
    """Custom type tmnxPortEtherMinFrameLength based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(68, 68),
    )


_TmnxPortEtherMinFrameLength_Type.__name__ = "Unsigned32"
_TmnxPortEtherMinFrameLength_Object = MibTableColumn
tmnxPortEtherMinFrameLength = _TmnxPortEtherMinFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 4, 1, 41),
    _TmnxPortEtherMinFrameLength_Type()
)
tmnxPortEtherMinFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherMinFrameLength.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherMinFrameLength.setUnits("Bytes")
_TmnxSonetTable_Object = MibTable
tmnxSonetTable = _TmnxSonetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    tmnxSonetTable.setStatus("current")
_TmnxSonetEntry_Object = MibTableRow
tmnxSonetEntry = _TmnxSonetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1)
)
tmnxSonetEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxSonetEntry.setStatus("current")


class _TmnxSonetSpeed_Type(Integer32):
    """Custom type tmnxSonetSpeed based on Integer32"""
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
        *(("oc1", 6),
          ("oc12", 2),
          ("oc192", 4),
          ("oc3", 1),
          ("oc48", 3),
          ("oc768", 5))
    )


_TmnxSonetSpeed_Type.__name__ = "Integer32"
_TmnxSonetSpeed_Object = MibTableColumn
tmnxSonetSpeed = _TmnxSonetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 1),
    _TmnxSonetSpeed_Type()
)
tmnxSonetSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetSpeed.setStatus("current")


class _TmnxSonetClockSource_Type(Integer32):
    """Custom type tmnxSonetClockSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopTimed", 1),
          ("nodeTimed", 2))
    )


_TmnxSonetClockSource_Type.__name__ = "Integer32"
_TmnxSonetClockSource_Object = MibTableColumn
tmnxSonetClockSource = _TmnxSonetClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 2),
    _TmnxSonetClockSource_Type()
)
tmnxSonetClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetClockSource.setStatus("current")


class _TmnxSonetFraming_Type(Integer32):
    """Custom type tmnxSonetFraming based on Integer32"""
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
        *(("sdh", 3),
          ("sonet", 2),
          ("unknown", 1))
    )


_TmnxSonetFraming_Type.__name__ = "Integer32"
_TmnxSonetFraming_Object = MibTableColumn
tmnxSonetFraming = _TmnxSonetFraming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 3),
    _TmnxSonetFraming_Type()
)
tmnxSonetFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetFraming.setStatus("current")


class _TmnxSonetReportAlarm_Type(Bits):
    """Custom type tmnxSonetReportAlarm based on Bits"""
    defaultBinValue = "0101000111"

    namedValues = NamedValues(
        *(("lais", 2),
          ("lb2erSd", 6),
          ("lb2erSf", 7),
          ("loc", 1),
          ("lrdi", 3),
          ("lrei", 12),
          ("notUsed", 0),
          ("sb1err", 5),
          ("slof", 8),
          ("slos", 9),
          ("srxptr", 11),
          ("ss1f", 4),
          ("stxptr", 10))
    )

_TmnxSonetReportAlarm_Type.__name__ = "Bits"
_TmnxSonetReportAlarm_Object = MibTableColumn
tmnxSonetReportAlarm = _TmnxSonetReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 4),
    _TmnxSonetReportAlarm_Type()
)
tmnxSonetReportAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetReportAlarm.setStatus("current")


class _TmnxSonetBerSdThreshold_Type(Unsigned32):
    """Custom type tmnxSonetBerSdThreshold based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_TmnxSonetBerSdThreshold_Type.__name__ = "Unsigned32"
_TmnxSonetBerSdThreshold_Object = MibTableColumn
tmnxSonetBerSdThreshold = _TmnxSonetBerSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 5),
    _TmnxSonetBerSdThreshold_Type()
)
tmnxSonetBerSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetBerSdThreshold.setStatus("current")


class _TmnxSonetBerSfThreshold_Type(Unsigned32):
    """Custom type tmnxSonetBerSfThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 6),
    )


_TmnxSonetBerSfThreshold_Type.__name__ = "Unsigned32"
_TmnxSonetBerSfThreshold_Object = MibTableColumn
tmnxSonetBerSfThreshold = _TmnxSonetBerSfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 6),
    _TmnxSonetBerSfThreshold_Type()
)
tmnxSonetBerSfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetBerSfThreshold.setStatus("current")


class _TmnxSonetAps_Type(TruthValue):
    """Custom type tmnxSonetAps based on TruthValue"""


_TmnxSonetAps_Object = MibTableColumn
tmnxSonetAps = _TmnxSonetAps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 7),
    _TmnxSonetAps_Type()
)
tmnxSonetAps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetAps.setStatus("obsolete")


class _TmnxSonetApsAdminStatus_Type(TmnxPortAdminStatus):
    """Custom type tmnxSonetApsAdminStatus based on TmnxPortAdminStatus"""


_TmnxSonetApsAdminStatus_Object = MibTableColumn
tmnxSonetApsAdminStatus = _TmnxSonetApsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 8),
    _TmnxSonetApsAdminStatus_Type()
)
tmnxSonetApsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetApsAdminStatus.setStatus("obsolete")
_TmnxSonetApsOperStatus_Type = TmnxPortOperStatus
_TmnxSonetApsOperStatus_Object = MibTableColumn
tmnxSonetApsOperStatus = _TmnxSonetApsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 9),
    _TmnxSonetApsOperStatus_Type()
)
tmnxSonetApsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetApsOperStatus.setStatus("obsolete")


class _TmnxSonetApsAuthKey_Type(OctetString):
    """Custom type tmnxSonetApsAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxSonetApsAuthKey_Type.__name__ = "OctetString"
_TmnxSonetApsAuthKey_Object = MibTableColumn
tmnxSonetApsAuthKey = _TmnxSonetApsAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 10),
    _TmnxSonetApsAuthKey_Type()
)
tmnxSonetApsAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetApsAuthKey.setStatus("obsolete")


class _TmnxSonetApsNeighborAddr_Type(IpAddress):
    """Custom type tmnxSonetApsNeighborAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxSonetApsNeighborAddr_Object = MibTableColumn
tmnxSonetApsNeighborAddr = _TmnxSonetApsNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 11),
    _TmnxSonetApsNeighborAddr_Type()
)
tmnxSonetApsNeighborAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetApsNeighborAddr.setStatus("obsolete")


class _TmnxSonetApsAdvertiseInterval_Type(TimeInterval):
    """Custom type tmnxSonetApsAdvertiseInterval based on TimeInterval"""
    defaultValue = 1000


_TmnxSonetApsAdvertiseInterval_Object = MibTableColumn
tmnxSonetApsAdvertiseInterval = _TmnxSonetApsAdvertiseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 12),
    _TmnxSonetApsAdvertiseInterval_Type()
)
tmnxSonetApsAdvertiseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetApsAdvertiseInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxSonetApsAdvertiseInterval.setUnits("milliseconds")
_TmnxSonetApsAdvertiseTimeLeft_Type = TimeInterval
_TmnxSonetApsAdvertiseTimeLeft_Object = MibTableColumn
tmnxSonetApsAdvertiseTimeLeft = _TmnxSonetApsAdvertiseTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 13),
    _TmnxSonetApsAdvertiseTimeLeft_Type()
)
tmnxSonetApsAdvertiseTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetApsAdvertiseTimeLeft.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxSonetApsAdvertiseTimeLeft.setUnits("milliseconds")


class _TmnxSonetApsHoldTime_Type(TimeInterval):
    """Custom type tmnxSonetApsHoldTime based on TimeInterval"""
    defaultValue = 3000


_TmnxSonetApsHoldTime_Object = MibTableColumn
tmnxSonetApsHoldTime = _TmnxSonetApsHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 14),
    _TmnxSonetApsHoldTime_Type()
)
tmnxSonetApsHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetApsHoldTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxSonetApsHoldTime.setUnits("milliseconds")
_TmnxSonetApsHoldTimeLeft_Type = TimeInterval
_TmnxSonetApsHoldTimeLeft_Object = MibTableColumn
tmnxSonetApsHoldTimeLeft = _TmnxSonetApsHoldTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 15),
    _TmnxSonetApsHoldTimeLeft_Type()
)
tmnxSonetApsHoldTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetApsHoldTimeLeft.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxSonetApsHoldTimeLeft.setUnits("milliseconds")


class _TmnxSonetLoopback_Type(Integer32):
    """Custom type tmnxSonetLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("line", 1),
          ("none", 0))
    )


_TmnxSonetLoopback_Type.__name__ = "Integer32"
_TmnxSonetLoopback_Object = MibTableColumn
tmnxSonetLoopback = _TmnxSonetLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 16),
    _TmnxSonetLoopback_Type()
)
tmnxSonetLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetLoopback.setStatus("current")


class _TmnxSonetReportAlarmStatus_Type(Bits):
    """Custom type tmnxSonetReportAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("lais", 2),
          ("lb2erSd", 6),
          ("lb2erSf", 7),
          ("loc", 1),
          ("lrdi", 3),
          ("lrei", 12),
          ("notUsed", 0),
          ("sb1err", 5),
          ("slof", 8),
          ("slos", 9),
          ("srxptr", 11),
          ("ss1f", 4),
          ("stxptr", 10))
    )

_TmnxSonetReportAlarmStatus_Type.__name__ = "Bits"
_TmnxSonetReportAlarmStatus_Object = MibTableColumn
tmnxSonetReportAlarmStatus = _TmnxSonetReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 17),
    _TmnxSonetReportAlarmStatus_Type()
)
tmnxSonetReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetReportAlarmStatus.setStatus("current")


class _TmnxSonetSectionTraceMode_Type(Integer32):
    """Custom type tmnxSonetSectionTraceMode based on Integer32"""
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
        *(("byte", 2),
          ("increment-z0", 1),
          ("string", 3))
    )


_TmnxSonetSectionTraceMode_Type.__name__ = "Integer32"
_TmnxSonetSectionTraceMode_Object = MibTableColumn
tmnxSonetSectionTraceMode = _TmnxSonetSectionTraceMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 18),
    _TmnxSonetSectionTraceMode_Type()
)
tmnxSonetSectionTraceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetSectionTraceMode.setStatus("current")


class _TmnxSonetJ0String_Type(OctetString):
    """Custom type tmnxSonetJ0String based on OctetString"""
    defaultHexValue = "01"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxSonetJ0String_Type.__name__ = "OctetString"
_TmnxSonetJ0String_Object = MibTableColumn
tmnxSonetJ0String = _TmnxSonetJ0String_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 19),
    _TmnxSonetJ0String_Type()
)
tmnxSonetJ0String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetJ0String.setStatus("current")


class _TmnxSonetMonS1Byte_Type(Unsigned32):
    """Custom type tmnxSonetMonS1Byte based on Unsigned32"""
    defaultHexValue = 204

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxSonetMonS1Byte_Type.__name__ = "Unsigned32"
_TmnxSonetMonS1Byte_Object = MibTableColumn
tmnxSonetMonS1Byte = _TmnxSonetMonS1Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 20),
    _TmnxSonetMonS1Byte_Type()
)
tmnxSonetMonS1Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetMonS1Byte.setStatus("current")


class _TmnxSonetMonJ0String_Type(OctetString):
    """Custom type tmnxSonetMonJ0String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxSonetMonJ0String_Type.__name__ = "OctetString"
_TmnxSonetMonJ0String_Object = MibTableColumn
tmnxSonetMonJ0String = _TmnxSonetMonJ0String_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 21),
    _TmnxSonetMonJ0String_Type()
)
tmnxSonetMonJ0String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetMonJ0String.setStatus("current")


class _TmnxSonetMonK1Byte_Type(Unsigned32):
    """Custom type tmnxSonetMonK1Byte based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxSonetMonK1Byte_Type.__name__ = "Unsigned32"
_TmnxSonetMonK1Byte_Object = MibTableColumn
tmnxSonetMonK1Byte = _TmnxSonetMonK1Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 22),
    _TmnxSonetMonK1Byte_Type()
)
tmnxSonetMonK1Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetMonK1Byte.setStatus("current")


class _TmnxSonetMonK2Byte_Type(Unsigned32):
    """Custom type tmnxSonetMonK2Byte based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxSonetMonK2Byte_Type.__name__ = "Unsigned32"
_TmnxSonetMonK2Byte_Object = MibTableColumn
tmnxSonetMonK2Byte = _TmnxSonetMonK2Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 23),
    _TmnxSonetMonK2Byte_Type()
)
tmnxSonetMonK2Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetMonK2Byte.setStatus("current")


class _TmnxSonetSingleFiber_Type(TruthValue):
    """Custom type tmnxSonetSingleFiber based on TruthValue"""


_TmnxSonetSingleFiber_Object = MibTableColumn
tmnxSonetSingleFiber = _TmnxSonetSingleFiber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 24),
    _TmnxSonetSingleFiber_Type()
)
tmnxSonetSingleFiber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetSingleFiber.setStatus("current")


class _TmnxSonetHoldTimeUp_Type(Unsigned32):
    """Custom type tmnxSonetHoldTimeUp based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxSonetHoldTimeUp_Type.__name__ = "Unsigned32"
_TmnxSonetHoldTimeUp_Object = MibTableColumn
tmnxSonetHoldTimeUp = _TmnxSonetHoldTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 25),
    _TmnxSonetHoldTimeUp_Type()
)
tmnxSonetHoldTimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetHoldTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSonetHoldTimeUp.setUnits("100s of milliseconds")


class _TmnxSonetHoldTimeDown_Type(Unsigned32):
    """Custom type tmnxSonetHoldTimeDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxSonetHoldTimeDown_Type.__name__ = "Unsigned32"
_TmnxSonetHoldTimeDown_Object = MibTableColumn
tmnxSonetHoldTimeDown = _TmnxSonetHoldTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 26),
    _TmnxSonetHoldTimeDown_Type()
)
tmnxSonetHoldTimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetHoldTimeDown.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSonetHoldTimeDown.setUnits("100s of milliseconds")


class _TmnxSonetSuppressLoOrderAlarm_Type(TruthValue):
    """Custom type tmnxSonetSuppressLoOrderAlarm based on TruthValue"""


_TmnxSonetSuppressLoOrderAlarm_Object = MibTableColumn
tmnxSonetSuppressLoOrderAlarm = _TmnxSonetSuppressLoOrderAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 27),
    _TmnxSonetSuppressLoOrderAlarm_Type()
)
tmnxSonetSuppressLoOrderAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetSuppressLoOrderAlarm.setStatus("current")


class _TmnxSonetTxDus_Type(TruthValue):
    """Custom type tmnxSonetTxDus based on TruthValue"""


_TmnxSonetTxDus_Object = MibTableColumn
tmnxSonetTxDus = _TmnxSonetTxDus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 28),
    _TmnxSonetTxDus_Type()
)
tmnxSonetTxDus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetTxDus.setStatus("current")
_TmnxSonetTxS1Byte_Type = Unsigned32
_TmnxSonetTxS1Byte_Object = MibTableColumn
tmnxSonetTxS1Byte = _TmnxSonetTxS1Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 5, 1, 29),
    _TmnxSonetTxS1Byte_Type()
)
tmnxSonetTxS1Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetTxS1Byte.setStatus("current")
_TmnxSonetPathTable_Object = MibTable
tmnxSonetPathTable = _TmnxSonetPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6)
)
if mibBuilder.loadTexts:
    tmnxSonetPathTable.setStatus("current")
_TmnxSonetPathEntry_Object = MibTableRow
tmnxSonetPathEntry = _TmnxSonetPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1)
)
tmnxSonetPathEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxSonetPathEntry.setStatus("current")
_TmnxSonetPathRowStatus_Type = RowStatus
_TmnxSonetPathRowStatus_Object = MibTableColumn
tmnxSonetPathRowStatus = _TmnxSonetPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 1),
    _TmnxSonetPathRowStatus_Type()
)
tmnxSonetPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathRowStatus.setStatus("current")
_TmnxSonetPathLastChangeTime_Type = TimeStamp
_TmnxSonetPathLastChangeTime_Object = MibTableColumn
tmnxSonetPathLastChangeTime = _TmnxSonetPathLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 2),
    _TmnxSonetPathLastChangeTime_Type()
)
tmnxSonetPathLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathLastChangeTime.setStatus("current")


class _TmnxSonetPathMTU_Type(Unsigned32):
    """Custom type tmnxSonetPathMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9208),
    )


_TmnxSonetPathMTU_Type.__name__ = "Unsigned32"
_TmnxSonetPathMTU_Object = MibTableColumn
tmnxSonetPathMTU = _TmnxSonetPathMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 3),
    _TmnxSonetPathMTU_Type()
)
tmnxSonetPathMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSonetPathMTU.setUnits("bytes")
_TmnxSonetPathScramble_Type = TruthValue
_TmnxSonetPathScramble_Object = MibTableColumn
tmnxSonetPathScramble = _TmnxSonetPathScramble_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 4),
    _TmnxSonetPathScramble_Type()
)
tmnxSonetPathScramble.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathScramble.setStatus("current")


class _TmnxSonetPathC2Byte_Type(Unsigned32):
    """Custom type tmnxSonetPathC2Byte based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TmnxSonetPathC2Byte_Type.__name__ = "Unsigned32"
_TmnxSonetPathC2Byte_Object = MibTableColumn
tmnxSonetPathC2Byte = _TmnxSonetPathC2Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 5),
    _TmnxSonetPathC2Byte_Type()
)
tmnxSonetPathC2Byte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathC2Byte.setStatus("current")


class _TmnxSonetPathJ1String_Type(OctetString):
    """Custom type tmnxSonetPathJ1String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_TmnxSonetPathJ1String_Type.__name__ = "OctetString"
_TmnxSonetPathJ1String_Object = MibTableColumn
tmnxSonetPathJ1String = _TmnxSonetPathJ1String_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 6),
    _TmnxSonetPathJ1String_Type()
)
tmnxSonetPathJ1String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathJ1String.setStatus("current")


class _TmnxSonetPathCRC_Type(Integer32):
    """Custom type tmnxSonetPathCRC based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_TmnxSonetPathCRC_Type.__name__ = "Integer32"
_TmnxSonetPathCRC_Object = MibTableColumn
tmnxSonetPathCRC = _TmnxSonetPathCRC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 7),
    _TmnxSonetPathCRC_Type()
)
tmnxSonetPathCRC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathCRC.setStatus("current")
_TmnxSonetPathOperMTU_Type = Unsigned32
_TmnxSonetPathOperMTU_Object = MibTableColumn
tmnxSonetPathOperMTU = _TmnxSonetPathOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 8),
    _TmnxSonetPathOperMTU_Type()
)
tmnxSonetPathOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathOperMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSonetPathOperMTU.setUnits("bytes")
_TmnxSonetPathOperMRU_Type = Unsigned32
_TmnxSonetPathOperMRU_Object = MibTableColumn
tmnxSonetPathOperMRU = _TmnxSonetPathOperMRU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 9),
    _TmnxSonetPathOperMRU_Type()
)
tmnxSonetPathOperMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathOperMRU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSonetPathOperMRU.setUnits("bytes")


class _TmnxSonetPathReportAlarm_Type(Bits):
    """Custom type tmnxSonetPathReportAlarm based on Bits"""
    defaultBinValue = "00100101"

    namedValues = NamedValues(
        *(("notUsed", 0),
          ("pais", 1),
          ("pb3err", 4),
          ("plcd", 8),
          ("plop", 2),
          ("pplm", 5),
          ("prdi", 3),
          ("prei", 6),
          ("puneq", 7))
    )

_TmnxSonetPathReportAlarm_Type.__name__ = "Bits"
_TmnxSonetPathReportAlarm_Object = MibTableColumn
tmnxSonetPathReportAlarm = _TmnxSonetPathReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 10),
    _TmnxSonetPathReportAlarm_Type()
)
tmnxSonetPathReportAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathReportAlarm.setStatus("current")


class _TmnxSonetPathAcctPolicyId_Type(Unsigned32):
    """Custom type tmnxSonetPathAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxSonetPathAcctPolicyId_Type.__name__ = "Unsigned32"
_TmnxSonetPathAcctPolicyId_Object = MibTableColumn
tmnxSonetPathAcctPolicyId = _TmnxSonetPathAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 11),
    _TmnxSonetPathAcctPolicyId_Type()
)
tmnxSonetPathAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathAcctPolicyId.setStatus("current")


class _TmnxSonetPathCollectStats_Type(TruthValue):
    """Custom type tmnxSonetPathCollectStats based on TruthValue"""


_TmnxSonetPathCollectStats_Object = MibTableColumn
tmnxSonetPathCollectStats = _TmnxSonetPathCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 12),
    _TmnxSonetPathCollectStats_Type()
)
tmnxSonetPathCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathCollectStats.setStatus("current")


class _TmnxSonetPathReportAlarmStatus_Type(Bits):
    """Custom type tmnxSonetPathReportAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("pais", 1),
          ("pb3err", 4),
          ("plcd", 8),
          ("plop", 2),
          ("pplm", 5),
          ("prdi", 3),
          ("prei", 6),
          ("puneq", 7))
    )

_TmnxSonetPathReportAlarmStatus_Type.__name__ = "Bits"
_TmnxSonetPathReportAlarmStatus_Object = MibTableColumn
tmnxSonetPathReportAlarmStatus = _TmnxSonetPathReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 13),
    _TmnxSonetPathReportAlarmStatus_Type()
)
tmnxSonetPathReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathReportAlarmStatus.setStatus("current")


class _TmnxSonetPathMonC2Byte_Type(Unsigned32):
    """Custom type tmnxSonetPathMonC2Byte based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxSonetPathMonC2Byte_Type.__name__ = "Unsigned32"
_TmnxSonetPathMonC2Byte_Object = MibTableColumn
tmnxSonetPathMonC2Byte = _TmnxSonetPathMonC2Byte_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 14),
    _TmnxSonetPathMonC2Byte_Type()
)
tmnxSonetPathMonC2Byte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathMonC2Byte.setStatus("current")


class _TmnxSonetPathMonJ1String_Type(OctetString):
    """Custom type tmnxSonetPathMonJ1String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxSonetPathMonJ1String_Type.__name__ = "OctetString"
_TmnxSonetPathMonJ1String_Object = MibTableColumn
tmnxSonetPathMonJ1String = _TmnxSonetPathMonJ1String_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 15),
    _TmnxSonetPathMonJ1String_Type()
)
tmnxSonetPathMonJ1String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetPathMonJ1String.setStatus("current")


class _TmnxSonetPathType_Type(Integer32):
    """Custom type tmnxSonetPathType based on Integer32"""
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
        *(("ds3", 1),
          ("e3", 2),
          ("tug-2", 4),
          ("tug-3", 5),
          ("vtg", 3))
    )


_TmnxSonetPathType_Type.__name__ = "Integer32"
_TmnxSonetPathType_Object = MibTableColumn
tmnxSonetPathType = _TmnxSonetPathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 16),
    _TmnxSonetPathType_Type()
)
tmnxSonetPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathType.setStatus("obsolete")
_TmnxSonetPathChildType_Type = TmnxMDAChanType
_TmnxSonetPathChildType_Object = MibTableColumn
tmnxSonetPathChildType = _TmnxSonetPathChildType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 6, 1, 17),
    _TmnxSonetPathChildType_Type()
)
tmnxSonetPathChildType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSonetPathChildType.setStatus("current")
_TmnxPortTypeTable_Object = MibTable
tmnxPortTypeTable = _TmnxPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7)
)
if mibBuilder.loadTexts:
    tmnxPortTypeTable.setStatus("current")
_TmnxPortTypeEntry_Object = MibTableRow
tmnxPortTypeEntry = _TmnxPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7, 1)
)
tmnxPortTypeEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortTypeEntry.setStatus("current")
_TmnxPortTypeIndex_Type = TmnxPortType
_TmnxPortTypeIndex_Object = MibTableColumn
tmnxPortTypeIndex = _TmnxPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7, 1, 1),
    _TmnxPortTypeIndex_Type()
)
tmnxPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortTypeIndex.setStatus("current")
_TmnxPortTypeName_Type = TNamedItemOrEmpty
_TmnxPortTypeName_Object = MibTableColumn
tmnxPortTypeName = _TmnxPortTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7, 1, 2),
    _TmnxPortTypeName_Type()
)
tmnxPortTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTypeName.setStatus("current")
_TmnxPortTypeDescription_Type = TItemDescription
_TmnxPortTypeDescription_Object = MibTableColumn
tmnxPortTypeDescription = _TmnxPortTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7, 1, 3),
    _TmnxPortTypeDescription_Type()
)
tmnxPortTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTypeDescription.setStatus("current")
_TmnxPortTypeStatus_Type = TruthValue
_TmnxPortTypeStatus_Object = MibTableColumn
tmnxPortTypeStatus = _TmnxPortTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 7, 1, 4),
    _TmnxPortTypeStatus_Type()
)
tmnxPortTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortTypeStatus.setStatus("current")
_TmnxPortConnectTypeTable_Object = MibTable
tmnxPortConnectTypeTable = _TmnxPortConnectTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8)
)
if mibBuilder.loadTexts:
    tmnxPortConnectTypeTable.setStatus("current")
_TmnxPortConnectTypeEntry_Object = MibTableRow
tmnxPortConnectTypeEntry = _TmnxPortConnectTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8, 1)
)
tmnxPortConnectTypeEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortConnectTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortConnectTypeEntry.setStatus("current")
_TmnxPortConnectTypeIndex_Type = TmnxPortConnectorType
_TmnxPortConnectTypeIndex_Object = MibTableColumn
tmnxPortConnectTypeIndex = _TmnxPortConnectTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8, 1, 1),
    _TmnxPortConnectTypeIndex_Type()
)
tmnxPortConnectTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortConnectTypeIndex.setStatus("current")
_TmnxPortConnectTypeName_Type = TNamedItemOrEmpty
_TmnxPortConnectTypeName_Object = MibTableColumn
tmnxPortConnectTypeName = _TmnxPortConnectTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8, 1, 2),
    _TmnxPortConnectTypeName_Type()
)
tmnxPortConnectTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortConnectTypeName.setStatus("current")
_TmnxPortConnectTypeDescription_Type = TItemDescription
_TmnxPortConnectTypeDescription_Object = MibTableColumn
tmnxPortConnectTypeDescription = _TmnxPortConnectTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8, 1, 3),
    _TmnxPortConnectTypeDescription_Type()
)
tmnxPortConnectTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortConnectTypeDescription.setStatus("current")
_TmnxPortConnectTypeStatus_Type = TruthValue
_TmnxPortConnectTypeStatus_Object = MibTableColumn
tmnxPortConnectTypeStatus = _TmnxPortConnectTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 8, 1, 4),
    _TmnxPortConnectTypeStatus_Type()
)
tmnxPortConnectTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortConnectTypeStatus.setStatus("current")
_TmnxPortFCStatsTable_Object = MibTable
tmnxPortFCStatsTable = _TmnxPortFCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9)
)
if mibBuilder.loadTexts:
    tmnxPortFCStatsTable.setStatus("obsolete")
_TmnxPortFCStatsEntry_Object = MibTableRow
tmnxPortFCStatsEntry = _TmnxPortFCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1)
)
tmnxPortFCStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortFCStatsIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortFCStatsEntry.setStatus("obsolete")
_TmnxPortFCStatsIndex_Type = TFCName
_TmnxPortFCStatsIndex_Object = MibTableColumn
tmnxPortFCStatsIndex = _TmnxPortFCStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 1),
    _TmnxPortFCStatsIndex_Type()
)
tmnxPortFCStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIndex.setStatus("obsolete")
_TmnxPortFCStatsIngFwdInProfPkts_Type = Counter64
_TmnxPortFCStatsIngFwdInProfPkts_Object = MibTableColumn
tmnxPortFCStatsIngFwdInProfPkts = _TmnxPortFCStatsIngFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 2),
    _TmnxPortFCStatsIngFwdInProfPkts_Type()
)
tmnxPortFCStatsIngFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngFwdInProfPkts.setStatus("obsolete")
_TmnxPortFCStatsIngFwdOutProfPkts_Type = Counter64
_TmnxPortFCStatsIngFwdOutProfPkts_Object = MibTableColumn
tmnxPortFCStatsIngFwdOutProfPkts = _TmnxPortFCStatsIngFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 3),
    _TmnxPortFCStatsIngFwdOutProfPkts_Type()
)
tmnxPortFCStatsIngFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngFwdOutProfPkts.setStatus("obsolete")
_TmnxPortFCStatsIngFwdInProfOcts_Type = Counter64
_TmnxPortFCStatsIngFwdInProfOcts_Object = MibTableColumn
tmnxPortFCStatsIngFwdInProfOcts = _TmnxPortFCStatsIngFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 4),
    _TmnxPortFCStatsIngFwdInProfOcts_Type()
)
tmnxPortFCStatsIngFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngFwdInProfOcts.setStatus("obsolete")
_TmnxPortFCStatsIngFwdOutProfOcts_Type = Counter64
_TmnxPortFCStatsIngFwdOutProfOcts_Object = MibTableColumn
tmnxPortFCStatsIngFwdOutProfOcts = _TmnxPortFCStatsIngFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 5),
    _TmnxPortFCStatsIngFwdOutProfOcts_Type()
)
tmnxPortFCStatsIngFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngFwdOutProfOcts.setStatus("obsolete")
_TmnxPortFCStatsIngDroInProfPkts_Type = Counter64
_TmnxPortFCStatsIngDroInProfPkts_Object = MibTableColumn
tmnxPortFCStatsIngDroInProfPkts = _TmnxPortFCStatsIngDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 6),
    _TmnxPortFCStatsIngDroInProfPkts_Type()
)
tmnxPortFCStatsIngDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngDroInProfPkts.setStatus("obsolete")
_TmnxPortFCStatsIngDroOutProfPkts_Type = Counter64
_TmnxPortFCStatsIngDroOutProfPkts_Object = MibTableColumn
tmnxPortFCStatsIngDroOutProfPkts = _TmnxPortFCStatsIngDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 7),
    _TmnxPortFCStatsIngDroOutProfPkts_Type()
)
tmnxPortFCStatsIngDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngDroOutProfPkts.setStatus("obsolete")
_TmnxPortFCStatsIngDroInProfOcts_Type = Counter64
_TmnxPortFCStatsIngDroInProfOcts_Object = MibTableColumn
tmnxPortFCStatsIngDroInProfOcts = _TmnxPortFCStatsIngDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 8),
    _TmnxPortFCStatsIngDroInProfOcts_Type()
)
tmnxPortFCStatsIngDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngDroInProfOcts.setStatus("obsolete")
_TmnxPortFCStatsIngDroOutProfOcts_Type = Counter64
_TmnxPortFCStatsIngDroOutProfOcts_Object = MibTableColumn
tmnxPortFCStatsIngDroOutProfOcts = _TmnxPortFCStatsIngDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 9),
    _TmnxPortFCStatsIngDroOutProfOcts_Type()
)
tmnxPortFCStatsIngDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsIngDroOutProfOcts.setStatus("obsolete")
_TmnxPortFCStatsEgrFwdInProfPkts_Type = Counter64
_TmnxPortFCStatsEgrFwdInProfPkts_Object = MibTableColumn
tmnxPortFCStatsEgrFwdInProfPkts = _TmnxPortFCStatsEgrFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 10),
    _TmnxPortFCStatsEgrFwdInProfPkts_Type()
)
tmnxPortFCStatsEgrFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrFwdInProfPkts.setStatus("obsolete")
_TmnxPortFCStatsEgrFwdOutProfPkts_Type = Counter64
_TmnxPortFCStatsEgrFwdOutProfPkts_Object = MibTableColumn
tmnxPortFCStatsEgrFwdOutProfPkts = _TmnxPortFCStatsEgrFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 11),
    _TmnxPortFCStatsEgrFwdOutProfPkts_Type()
)
tmnxPortFCStatsEgrFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrFwdOutProfPkts.setStatus("obsolete")
_TmnxPortFCStatsEgrFwdInProfOcts_Type = Counter64
_TmnxPortFCStatsEgrFwdInProfOcts_Object = MibTableColumn
tmnxPortFCStatsEgrFwdInProfOcts = _TmnxPortFCStatsEgrFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 12),
    _TmnxPortFCStatsEgrFwdInProfOcts_Type()
)
tmnxPortFCStatsEgrFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrFwdInProfOcts.setStatus("obsolete")
_TmnxPortFCStatsEgrFwdOutProfOcts_Type = Counter64
_TmnxPortFCStatsEgrFwdOutProfOcts_Object = MibTableColumn
tmnxPortFCStatsEgrFwdOutProfOcts = _TmnxPortFCStatsEgrFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 13),
    _TmnxPortFCStatsEgrFwdOutProfOcts_Type()
)
tmnxPortFCStatsEgrFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrFwdOutProfOcts.setStatus("obsolete")
_TmnxPortFCStatsEgrDroInProfPkts_Type = Counter64
_TmnxPortFCStatsEgrDroInProfPkts_Object = MibTableColumn
tmnxPortFCStatsEgrDroInProfPkts = _TmnxPortFCStatsEgrDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 14),
    _TmnxPortFCStatsEgrDroInProfPkts_Type()
)
tmnxPortFCStatsEgrDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrDroInProfPkts.setStatus("obsolete")
_TmnxPortFCStatsEgrDroOutProfPkts_Type = Counter64
_TmnxPortFCStatsEgrDroOutProfPkts_Object = MibTableColumn
tmnxPortFCStatsEgrDroOutProfPkts = _TmnxPortFCStatsEgrDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 15),
    _TmnxPortFCStatsEgrDroOutProfPkts_Type()
)
tmnxPortFCStatsEgrDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrDroOutProfPkts.setStatus("obsolete")
_TmnxPortFCStatsEgrDroInProfOcts_Type = Counter64
_TmnxPortFCStatsEgrDroInProfOcts_Object = MibTableColumn
tmnxPortFCStatsEgrDroInProfOcts = _TmnxPortFCStatsEgrDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 16),
    _TmnxPortFCStatsEgrDroInProfOcts_Type()
)
tmnxPortFCStatsEgrDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrDroInProfOcts.setStatus("obsolete")
_TmnxPortFCStatsEgrDroOutProfOcts_Type = Counter64
_TmnxPortFCStatsEgrDroOutProfOcts_Object = MibTableColumn
tmnxPortFCStatsEgrDroOutProfOcts = _TmnxPortFCStatsEgrDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 9, 1, 17),
    _TmnxPortFCStatsEgrDroOutProfOcts_Type()
)
tmnxPortFCStatsEgrDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortFCStatsEgrDroOutProfOcts.setStatus("obsolete")
_TmnxDS3Table_Object = MibTable
tmnxDS3Table = _TmnxDS3Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 10)
)
if mibBuilder.loadTexts:
    tmnxDS3Table.setStatus("current")
_TmnxDS3Entry_Object = MibTableRow
tmnxDS3Entry = _TmnxDS3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 10, 1)
)
tmnxDS3Entry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDS3Entry.setStatus("current")


class _TmnxDS3Buildout_Type(Integer32):
    """Custom type tmnxDS3Buildout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_TmnxDS3Buildout_Type.__name__ = "Integer32"
_TmnxDS3Buildout_Object = MibTableColumn
tmnxDS3Buildout = _TmnxDS3Buildout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 10, 1, 1),
    _TmnxDS3Buildout_Type()
)
tmnxDS3Buildout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3Buildout.setStatus("current")
_TmnxDS3LastChangeTime_Type = TimeStamp
_TmnxDS3LastChangeTime_Object = MibTableColumn
tmnxDS3LastChangeTime = _TmnxDS3LastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 10, 1, 2),
    _TmnxDS3LastChangeTime_Type()
)
tmnxDS3LastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3LastChangeTime.setStatus("current")


class _TmnxDS3Type_Type(Integer32):
    """Custom type tmnxDS3Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 1),
          ("e3", 2))
    )


_TmnxDS3Type_Type.__name__ = "Integer32"
_TmnxDS3Type_Object = MibTableColumn
tmnxDS3Type = _TmnxDS3Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 10, 1, 3),
    _TmnxDS3Type_Type()
)
tmnxDS3Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3Type.setStatus("current")
_TmnxDS3ChannelTable_Object = MibTable
tmnxDS3ChannelTable = _TmnxDS3ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11)
)
if mibBuilder.loadTexts:
    tmnxDS3ChannelTable.setStatus("current")
_TmnxDS3ChannelEntry_Object = MibTableRow
tmnxDS3ChannelEntry = _TmnxDS3ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1)
)
tmnxDS3ChannelEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDS3ChannelEntry.setStatus("current")
_TmnxDS3ChannelRowStatus_Type = RowStatus
_TmnxDS3ChannelRowStatus_Object = MibTableColumn
tmnxDS3ChannelRowStatus = _TmnxDS3ChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 1),
    _TmnxDS3ChannelRowStatus_Type()
)
tmnxDS3ChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelRowStatus.setStatus("current")


class _TmnxDS3ChannelType_Type(Integer32):
    """Custom type tmnxDS3ChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 1),
          ("e3", 2))
    )


_TmnxDS3ChannelType_Type.__name__ = "Integer32"
_TmnxDS3ChannelType_Object = MibTableColumn
tmnxDS3ChannelType = _TmnxDS3ChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 2),
    _TmnxDS3ChannelType_Type()
)
tmnxDS3ChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelType.setStatus("current")


class _TmnxDS3ChannelFraming_Type(Integer32):
    """Custom type tmnxDS3ChannelFraming based on Integer32"""
    defaultValue = 1

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
        *(("cbit", 1),
          ("ds3-unframed", 6),
          ("e3-unframed", 5),
          ("g751", 3),
          ("g832", 4),
          ("m23", 2))
    )


_TmnxDS3ChannelFraming_Type.__name__ = "Integer32"
_TmnxDS3ChannelFraming_Object = MibTableColumn
tmnxDS3ChannelFraming = _TmnxDS3ChannelFraming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 3),
    _TmnxDS3ChannelFraming_Type()
)
tmnxDS3ChannelFraming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelFraming.setStatus("current")


class _TmnxDS3ChannelClockSource_Type(TmnxDSXClockSource):
    """Custom type tmnxDS3ChannelClockSource based on TmnxDSXClockSource"""


_TmnxDS3ChannelClockSource_Object = MibTableColumn
tmnxDS3ChannelClockSource = _TmnxDS3ChannelClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 4),
    _TmnxDS3ChannelClockSource_Type()
)
tmnxDS3ChannelClockSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelClockSource.setStatus("current")


class _TmnxDS3ChannelChannelized_Type(Integer32):
    """Custom type tmnxDS3ChannelChannelized based on Integer32"""
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
        *(("ds1", 2),
          ("e1", 3),
          ("j1", 4),
          ("none", 1))
    )


_TmnxDS3ChannelChannelized_Type.__name__ = "Integer32"
_TmnxDS3ChannelChannelized_Object = MibTableColumn
tmnxDS3ChannelChannelized = _TmnxDS3ChannelChannelized_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 5),
    _TmnxDS3ChannelChannelized_Type()
)
tmnxDS3ChannelChannelized.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelChannelized.setStatus("current")


class _TmnxDS3ChannelSubrateCSUMode_Type(Integer32):
    """Custom type tmnxDS3ChannelSubrateCSUMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("digital-link", 1),
          ("notUsed", 0))
    )


_TmnxDS3ChannelSubrateCSUMode_Type.__name__ = "Integer32"
_TmnxDS3ChannelSubrateCSUMode_Object = MibTableColumn
tmnxDS3ChannelSubrateCSUMode = _TmnxDS3ChannelSubrateCSUMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 6),
    _TmnxDS3ChannelSubrateCSUMode_Type()
)
tmnxDS3ChannelSubrateCSUMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelSubrateCSUMode.setStatus("current")
_TmnxDS3ChannelSubrate_Type = Unsigned32
_TmnxDS3ChannelSubrate_Object = MibTableColumn
tmnxDS3ChannelSubrate = _TmnxDS3ChannelSubrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 7),
    _TmnxDS3ChannelSubrate_Type()
)
tmnxDS3ChannelSubrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelSubrate.setStatus("current")


class _TmnxDS3ChannelIdleCycleFlags_Type(TmnxDSXIdleCycleFlags):
    """Custom type tmnxDS3ChannelIdleCycleFlags based on TmnxDSXIdleCycleFlags"""


_TmnxDS3ChannelIdleCycleFlags_Object = MibTableColumn
tmnxDS3ChannelIdleCycleFlags = _TmnxDS3ChannelIdleCycleFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 8),
    _TmnxDS3ChannelIdleCycleFlags_Type()
)
tmnxDS3ChannelIdleCycleFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelIdleCycleFlags.setStatus("current")


class _TmnxDS3ChannelLoopback_Type(TmnxDS3Loopback):
    """Custom type tmnxDS3ChannelLoopback based on TmnxDS3Loopback"""


_TmnxDS3ChannelLoopback_Object = MibTableColumn
tmnxDS3ChannelLoopback = _TmnxDS3ChannelLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 9),
    _TmnxDS3ChannelLoopback_Type()
)
tmnxDS3ChannelLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelLoopback.setStatus("current")


class _TmnxDS3ChannelBitErrorInsertionRate_Type(Integer32):
    """Custom type tmnxDS3ChannelBitErrorInsertionRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 7),
    )


_TmnxDS3ChannelBitErrorInsertionRate_Type.__name__ = "Integer32"
_TmnxDS3ChannelBitErrorInsertionRate_Object = MibTableColumn
tmnxDS3ChannelBitErrorInsertionRate = _TmnxDS3ChannelBitErrorInsertionRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 10),
    _TmnxDS3ChannelBitErrorInsertionRate_Type()
)
tmnxDS3ChannelBitErrorInsertionRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBitErrorInsertionRate.setStatus("current")


class _TmnxDS3ChannelBERTPattern_Type(TmnxDSXBertPattern):
    """Custom type tmnxDS3ChannelBERTPattern based on TmnxDSXBertPattern"""


_TmnxDS3ChannelBERTPattern_Object = MibTableColumn
tmnxDS3ChannelBERTPattern = _TmnxDS3ChannelBERTPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 11),
    _TmnxDS3ChannelBERTPattern_Type()
)
tmnxDS3ChannelBERTPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTPattern.setStatus("current")


class _TmnxDS3ChannelBERTDuration_Type(Unsigned32):
    """Custom type tmnxDS3ChannelBERTDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxDS3ChannelBERTDuration_Type.__name__ = "Unsigned32"
_TmnxDS3ChannelBERTDuration_Object = MibTableColumn
tmnxDS3ChannelBERTDuration = _TmnxDS3ChannelBERTDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 12),
    _TmnxDS3ChannelBERTDuration_Type()
)
tmnxDS3ChannelBERTDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTDuration.setUnits("seconds")


class _TmnxDS3ChannelMDLEicString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLEicString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TmnxDS3ChannelMDLEicString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLEicString_Object = MibTableColumn
tmnxDS3ChannelMDLEicString = _TmnxDS3ChannelMDLEicString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 13),
    _TmnxDS3ChannelMDLEicString_Type()
)
tmnxDS3ChannelMDLEicString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLEicString.setStatus("current")


class _TmnxDS3ChannelMDLLicString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLLicString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_TmnxDS3ChannelMDLLicString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLLicString_Object = MibTableColumn
tmnxDS3ChannelMDLLicString = _TmnxDS3ChannelMDLLicString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 14),
    _TmnxDS3ChannelMDLLicString_Type()
)
tmnxDS3ChannelMDLLicString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLLicString.setStatus("current")


class _TmnxDS3ChannelMDLFicString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLFicString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TmnxDS3ChannelMDLFicString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLFicString_Object = MibTableColumn
tmnxDS3ChannelMDLFicString = _TmnxDS3ChannelMDLFicString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 15),
    _TmnxDS3ChannelMDLFicString_Type()
)
tmnxDS3ChannelMDLFicString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLFicString.setStatus("current")


class _TmnxDS3ChannelMDLUnitString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLUnitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_TmnxDS3ChannelMDLUnitString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLUnitString_Object = MibTableColumn
tmnxDS3ChannelMDLUnitString = _TmnxDS3ChannelMDLUnitString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 16),
    _TmnxDS3ChannelMDLUnitString_Type()
)
tmnxDS3ChannelMDLUnitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLUnitString.setStatus("current")


class _TmnxDS3ChannelMDLPfiString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLPfiString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_TmnxDS3ChannelMDLPfiString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLPfiString_Object = MibTableColumn
tmnxDS3ChannelMDLPfiString = _TmnxDS3ChannelMDLPfiString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 17),
    _TmnxDS3ChannelMDLPfiString_Type()
)
tmnxDS3ChannelMDLPfiString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLPfiString.setStatus("current")


class _TmnxDS3ChannelMDLPortString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLPortString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_TmnxDS3ChannelMDLPortString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLPortString_Object = MibTableColumn
tmnxDS3ChannelMDLPortString = _TmnxDS3ChannelMDLPortString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 18),
    _TmnxDS3ChannelMDLPortString_Type()
)
tmnxDS3ChannelMDLPortString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLPortString.setStatus("current")


class _TmnxDS3ChannelMDLGenString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLGenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_TmnxDS3ChannelMDLGenString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLGenString_Object = MibTableColumn
tmnxDS3ChannelMDLGenString = _TmnxDS3ChannelMDLGenString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 19),
    _TmnxDS3ChannelMDLGenString_Type()
)
tmnxDS3ChannelMDLGenString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLGenString.setStatus("current")


class _TmnxDS3ChannelMDLMessageType_Type(Bits):
    """Custom type tmnxDS3ChannelMDLMessageType based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("ds3Path", 1),
          ("idleSignal", 2),
          ("none", 0),
          ("testSignal", 3))
    )

_TmnxDS3ChannelMDLMessageType_Type.__name__ = "Bits"
_TmnxDS3ChannelMDLMessageType_Object = MibTableColumn
tmnxDS3ChannelMDLMessageType = _TmnxDS3ChannelMDLMessageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 20),
    _TmnxDS3ChannelMDLMessageType_Type()
)
tmnxDS3ChannelMDLMessageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLMessageType.setStatus("current")


class _TmnxDS3ChannelFEACLoopRespond_Type(TruthValue):
    """Custom type tmnxDS3ChannelFEACLoopRespond based on TruthValue"""


_TmnxDS3ChannelFEACLoopRespond_Object = MibTableColumn
tmnxDS3ChannelFEACLoopRespond = _TmnxDS3ChannelFEACLoopRespond_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 21),
    _TmnxDS3ChannelFEACLoopRespond_Type()
)
tmnxDS3ChannelFEACLoopRespond.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelFEACLoopRespond.setStatus("current")


class _TmnxDS3ChannelCRC_Type(Integer32):
    """Custom type tmnxDS3ChannelCRC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_TmnxDS3ChannelCRC_Type.__name__ = "Integer32"
_TmnxDS3ChannelCRC_Object = MibTableColumn
tmnxDS3ChannelCRC = _TmnxDS3ChannelCRC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 22),
    _TmnxDS3ChannelCRC_Type()
)
tmnxDS3ChannelCRC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelCRC.setStatus("current")


class _TmnxDS3ChannelMTU_Type(Unsigned32):
    """Custom type tmnxDS3ChannelMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9208),
    )


_TmnxDS3ChannelMTU_Type.__name__ = "Unsigned32"
_TmnxDS3ChannelMTU_Object = MibTableColumn
tmnxDS3ChannelMTU = _TmnxDS3ChannelMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 23),
    _TmnxDS3ChannelMTU_Type()
)
tmnxDS3ChannelMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMTU.setUnits("bytes")
_TmnxDS3ChannelOperMTU_Type = Unsigned32
_TmnxDS3ChannelOperMTU_Object = MibTableColumn
tmnxDS3ChannelOperMTU = _TmnxDS3ChannelOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 24),
    _TmnxDS3ChannelOperMTU_Type()
)
tmnxDS3ChannelOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelOperMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS3ChannelOperMTU.setUnits("bytes")


class _TmnxDS3ChannelReportAlarm_Type(TmnxDSXReportAlarm):
    """Custom type tmnxDS3ChannelReportAlarm based on TmnxDSXReportAlarm"""
    defaultBinValue = "011"


_TmnxDS3ChannelReportAlarm_Object = MibTableColumn
tmnxDS3ChannelReportAlarm = _TmnxDS3ChannelReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 25),
    _TmnxDS3ChannelReportAlarm_Type()
)
tmnxDS3ChannelReportAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelReportAlarm.setStatus("current")
_TmnxDS3ChannelReportAlarmStatus_Type = TmnxDSXReportAlarm
_TmnxDS3ChannelReportAlarmStatus_Object = MibTableColumn
tmnxDS3ChannelReportAlarmStatus = _TmnxDS3ChannelReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 26),
    _TmnxDS3ChannelReportAlarmStatus_Type()
)
tmnxDS3ChannelReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelReportAlarmStatus.setStatus("current")
_TmnxDS3ChannelLastChangeTime_Type = TimeStamp
_TmnxDS3ChannelLastChangeTime_Object = MibTableColumn
tmnxDS3ChannelLastChangeTime = _TmnxDS3ChannelLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 27),
    _TmnxDS3ChannelLastChangeTime_Type()
)
tmnxDS3ChannelLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelLastChangeTime.setStatus("current")
_TmnxDS3ChannelInFEACLoop_Type = TruthValue
_TmnxDS3ChannelInFEACLoop_Object = MibTableColumn
tmnxDS3ChannelInFEACLoop = _TmnxDS3ChannelInFEACLoop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 28),
    _TmnxDS3ChannelInFEACLoop_Type()
)
tmnxDS3ChannelInFEACLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelInFEACLoop.setStatus("current")


class _TmnxDS3ChannelMDLMonPortString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLMonPortString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_TmnxDS3ChannelMDLMonPortString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLMonPortString_Object = MibTableColumn
tmnxDS3ChannelMDLMonPortString = _TmnxDS3ChannelMDLMonPortString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 29),
    _TmnxDS3ChannelMDLMonPortString_Type()
)
tmnxDS3ChannelMDLMonPortString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLMonPortString.setStatus("current")


class _TmnxDS3ChannelMDLMonGenString_Type(DisplayString):
    """Custom type tmnxDS3ChannelMDLMonGenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_TmnxDS3ChannelMDLMonGenString_Type.__name__ = "DisplayString"
_TmnxDS3ChannelMDLMonGenString_Object = MibTableColumn
tmnxDS3ChannelMDLMonGenString = _TmnxDS3ChannelMDLMonGenString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 30),
    _TmnxDS3ChannelMDLMonGenString_Type()
)
tmnxDS3ChannelMDLMonGenString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelMDLMonGenString.setStatus("current")
_TmnxDS3ChannelBERTOperStatus_Type = TmnxDSXBertOperStatus
_TmnxDS3ChannelBERTOperStatus_Object = MibTableColumn
tmnxDS3ChannelBERTOperStatus = _TmnxDS3ChannelBERTOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 31),
    _TmnxDS3ChannelBERTOperStatus_Type()
)
tmnxDS3ChannelBERTOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTOperStatus.setStatus("current")
_TmnxDS3ChannelBERTSynched_Type = Unsigned32
_TmnxDS3ChannelBERTSynched_Object = MibTableColumn
tmnxDS3ChannelBERTSynched = _TmnxDS3ChannelBERTSynched_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 32),
    _TmnxDS3ChannelBERTSynched_Type()
)
tmnxDS3ChannelBERTSynched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTSynched.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTSynched.setUnits("seconds")
_TmnxDS3ChannelBERTErrors_Type = Counter64
_TmnxDS3ChannelBERTErrors_Object = MibTableColumn
tmnxDS3ChannelBERTErrors = _TmnxDS3ChannelBERTErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 33),
    _TmnxDS3ChannelBERTErrors_Type()
)
tmnxDS3ChannelBERTErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTErrors.setStatus("current")
_TmnxDS3ChannelBERTTotalBits_Type = Counter64
_TmnxDS3ChannelBERTTotalBits_Object = MibTableColumn
tmnxDS3ChannelBERTTotalBits = _TmnxDS3ChannelBERTTotalBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 34),
    _TmnxDS3ChannelBERTTotalBits_Type()
)
tmnxDS3ChannelBERTTotalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelBERTTotalBits.setStatus("current")
_TmnxDS3ChannelScramble_Type = TruthValue
_TmnxDS3ChannelScramble_Object = MibTableColumn
tmnxDS3ChannelScramble = _TmnxDS3ChannelScramble_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 35),
    _TmnxDS3ChannelScramble_Type()
)
tmnxDS3ChannelScramble.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelScramble.setStatus("current")


class _TmnxDS3ChannelAcctPolicyId_Type(Unsigned32):
    """Custom type tmnxDS3ChannelAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxDS3ChannelAcctPolicyId_Type.__name__ = "Unsigned32"
_TmnxDS3ChannelAcctPolicyId_Object = MibTableColumn
tmnxDS3ChannelAcctPolicyId = _TmnxDS3ChannelAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 36),
    _TmnxDS3ChannelAcctPolicyId_Type()
)
tmnxDS3ChannelAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelAcctPolicyId.setStatus("current")


class _TmnxDS3ChannelCollectStats_Type(TruthValue):
    """Custom type tmnxDS3ChannelCollectStats based on TruthValue"""


_TmnxDS3ChannelCollectStats_Object = MibTableColumn
tmnxDS3ChannelCollectStats = _TmnxDS3ChannelCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 37),
    _TmnxDS3ChannelCollectStats_Type()
)
tmnxDS3ChannelCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS3ChannelCollectStats.setStatus("current")
_TmnxDS3ChannelClockSyncState_Type = TmnxDSXClockSyncState
_TmnxDS3ChannelClockSyncState_Object = MibTableColumn
tmnxDS3ChannelClockSyncState = _TmnxDS3ChannelClockSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 38),
    _TmnxDS3ChannelClockSyncState_Type()
)
tmnxDS3ChannelClockSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelClockSyncState.setStatus("current")
_TmnxDS3ChannelClockMasterPortId_Type = TmnxPortID
_TmnxDS3ChannelClockMasterPortId_Object = MibTableColumn
tmnxDS3ChannelClockMasterPortId = _TmnxDS3ChannelClockMasterPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 11, 1, 39),
    _TmnxDS3ChannelClockMasterPortId_Type()
)
tmnxDS3ChannelClockMasterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS3ChannelClockMasterPortId.setStatus("current")
_TmnxDS1Table_Object = MibTable
tmnxDS1Table = _TmnxDS1Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12)
)
if mibBuilder.loadTexts:
    tmnxDS1Table.setStatus("current")
_TmnxDS1Entry_Object = MibTableRow
tmnxDS1Entry = _TmnxDS1Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1)
)
tmnxDS1Entry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDS1Entry.setStatus("current")
_TmnxDS1RowStatus_Type = RowStatus
_TmnxDS1RowStatus_Object = MibTableColumn
tmnxDS1RowStatus = _TmnxDS1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 1),
    _TmnxDS1RowStatus_Type()
)
tmnxDS1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1RowStatus.setStatus("current")


class _TmnxDS1Type_Type(Integer32):
    """Custom type tmnxDS1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 1),
          ("e1", 2),
          ("j1", 3))
    )


_TmnxDS1Type_Type.__name__ = "Integer32"
_TmnxDS1Type_Object = MibTableColumn
tmnxDS1Type = _TmnxDS1Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 2),
    _TmnxDS1Type_Type()
)
tmnxDS1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1Type.setStatus("current")


class _TmnxDS1Framing_Type(Integer32):
    """Custom type tmnxDS1Framing based on Integer32"""
    defaultValue = 1

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
        *(("ds1-unframed", 6),
          ("e1-unframed", 5),
          ("esf", 1),
          ("g704", 4),
          ("g704-no-crc", 3),
          ("sf", 2))
    )


_TmnxDS1Framing_Type.__name__ = "Integer32"
_TmnxDS1Framing_Object = MibTableColumn
tmnxDS1Framing = _TmnxDS1Framing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 3),
    _TmnxDS1Framing_Type()
)
tmnxDS1Framing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1Framing.setStatus("current")


class _TmnxDS1IdleCycleFlags_Type(TmnxDSXIdleCycleFlags):
    """Custom type tmnxDS1IdleCycleFlags based on TmnxDSXIdleCycleFlags"""


_TmnxDS1IdleCycleFlags_Object = MibTableColumn
tmnxDS1IdleCycleFlags = _TmnxDS1IdleCycleFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 4),
    _TmnxDS1IdleCycleFlags_Type()
)
tmnxDS1IdleCycleFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1IdleCycleFlags.setStatus("obsolete")


class _TmnxDS1Loopback_Type(TmnxDS1Loopback):
    """Custom type tmnxDS1Loopback based on TmnxDS1Loopback"""


_TmnxDS1Loopback_Object = MibTableColumn
tmnxDS1Loopback = _TmnxDS1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 5),
    _TmnxDS1Loopback_Type()
)
tmnxDS1Loopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1Loopback.setStatus("current")


class _TmnxDS1InvertData_Type(TruthValue):
    """Custom type tmnxDS1InvertData based on TruthValue"""


_TmnxDS1InvertData_Object = MibTableColumn
tmnxDS1InvertData = _TmnxDS1InvertData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 6),
    _TmnxDS1InvertData_Type()
)
tmnxDS1InvertData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1InvertData.setStatus("current")


class _TmnxDS1BitErrorInsertionRate_Type(Integer32):
    """Custom type tmnxDS1BitErrorInsertionRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 7),
    )


_TmnxDS1BitErrorInsertionRate_Type.__name__ = "Integer32"
_TmnxDS1BitErrorInsertionRate_Object = MibTableColumn
tmnxDS1BitErrorInsertionRate = _TmnxDS1BitErrorInsertionRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 7),
    _TmnxDS1BitErrorInsertionRate_Type()
)
tmnxDS1BitErrorInsertionRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1BitErrorInsertionRate.setStatus("current")


class _TmnxDS1BERTPattern_Type(TmnxDSXBertPattern):
    """Custom type tmnxDS1BERTPattern based on TmnxDSXBertPattern"""


_TmnxDS1BERTPattern_Object = MibTableColumn
tmnxDS1BERTPattern = _TmnxDS1BERTPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 8),
    _TmnxDS1BERTPattern_Type()
)
tmnxDS1BERTPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1BERTPattern.setStatus("current")


class _TmnxDS1BERTDuration_Type(Unsigned32):
    """Custom type tmnxDS1BERTDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxDS1BERTDuration_Type.__name__ = "Unsigned32"
_TmnxDS1BERTDuration_Object = MibTableColumn
tmnxDS1BERTDuration = _TmnxDS1BERTDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 9),
    _TmnxDS1BERTDuration_Type()
)
tmnxDS1BERTDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1BERTDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS1BERTDuration.setUnits("seconds")


class _TmnxDS1ReportAlarm_Type(TmnxDSXReportAlarm):
    """Custom type tmnxDS1ReportAlarm based on TmnxDSXReportAlarm"""
    defaultBinValue = "011"


_TmnxDS1ReportAlarm_Object = MibTableColumn
tmnxDS1ReportAlarm = _TmnxDS1ReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 10),
    _TmnxDS1ReportAlarm_Type()
)
tmnxDS1ReportAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1ReportAlarm.setStatus("current")
_TmnxDS1ReportAlarmStatus_Type = TmnxDSXReportAlarm
_TmnxDS1ReportAlarmStatus_Object = MibTableColumn
tmnxDS1ReportAlarmStatus = _TmnxDS1ReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 11),
    _TmnxDS1ReportAlarmStatus_Type()
)
tmnxDS1ReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1ReportAlarmStatus.setStatus("current")
_TmnxDS1LastChangeTime_Type = TimeStamp
_TmnxDS1LastChangeTime_Object = MibTableColumn
tmnxDS1LastChangeTime = _TmnxDS1LastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 12),
    _TmnxDS1LastChangeTime_Type()
)
tmnxDS1LastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1LastChangeTime.setStatus("current")


class _TmnxDS1ClockSource_Type(TmnxDSXClockSource):
    """Custom type tmnxDS1ClockSource based on TmnxDSXClockSource"""


_TmnxDS1ClockSource_Object = MibTableColumn
tmnxDS1ClockSource = _TmnxDS1ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 13),
    _TmnxDS1ClockSource_Type()
)
tmnxDS1ClockSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1ClockSource.setStatus("current")
_TmnxDS1BERTOperStatus_Type = TmnxDSXBertOperStatus
_TmnxDS1BERTOperStatus_Object = MibTableColumn
tmnxDS1BERTOperStatus = _TmnxDS1BERTOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 14),
    _TmnxDS1BERTOperStatus_Type()
)
tmnxDS1BERTOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1BERTOperStatus.setStatus("current")
_TmnxDS1BERTSynched_Type = Unsigned32
_TmnxDS1BERTSynched_Object = MibTableColumn
tmnxDS1BERTSynched = _TmnxDS1BERTSynched_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 15),
    _TmnxDS1BERTSynched_Type()
)
tmnxDS1BERTSynched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1BERTSynched.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS1BERTSynched.setUnits("seconds")
_TmnxDS1BERTErrors_Type = Counter64
_TmnxDS1BERTErrors_Object = MibTableColumn
tmnxDS1BERTErrors = _TmnxDS1BERTErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 16),
    _TmnxDS1BERTErrors_Type()
)
tmnxDS1BERTErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1BERTErrors.setStatus("current")
_TmnxDS1BERTTotalBits_Type = Counter64
_TmnxDS1BERTTotalBits_Object = MibTableColumn
tmnxDS1BERTTotalBits = _TmnxDS1BERTTotalBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 17),
    _TmnxDS1BERTTotalBits_Type()
)
tmnxDS1BERTTotalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1BERTTotalBits.setStatus("current")


class _TmnxDS1RemoteLoopRespond_Type(TruthValue):
    """Custom type tmnxDS1RemoteLoopRespond based on TruthValue"""


_TmnxDS1RemoteLoopRespond_Object = MibTableColumn
tmnxDS1RemoteLoopRespond = _TmnxDS1RemoteLoopRespond_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 18),
    _TmnxDS1RemoteLoopRespond_Type()
)
tmnxDS1RemoteLoopRespond.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1RemoteLoopRespond.setStatus("current")
_TmnxDS1InRemoteLoop_Type = TruthValue
_TmnxDS1InRemoteLoop_Object = MibTableColumn
tmnxDS1InRemoteLoop = _TmnxDS1InRemoteLoop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 19),
    _TmnxDS1InRemoteLoop_Type()
)
tmnxDS1InRemoteLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1InRemoteLoop.setStatus("current")
_TmnxDS1InsertSingleBitError_Type = TmnxActionType
_TmnxDS1InsertSingleBitError_Object = MibTableColumn
tmnxDS1InsertSingleBitError = _TmnxDS1InsertSingleBitError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 20),
    _TmnxDS1InsertSingleBitError_Type()
)
tmnxDS1InsertSingleBitError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1InsertSingleBitError.setStatus("current")


class _TmnxDS1SignalMode_Type(Integer32):
    """Custom type tmnxDS1SignalMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cas", 2),
          ("none", 1))
    )


_TmnxDS1SignalMode_Type.__name__ = "Integer32"
_TmnxDS1SignalMode_Object = MibTableColumn
tmnxDS1SignalMode = _TmnxDS1SignalMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 21),
    _TmnxDS1SignalMode_Type()
)
tmnxDS1SignalMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1SignalMode.setStatus("current")
_TmnxDS1ClockSyncState_Type = TmnxDSXClockSyncState
_TmnxDS1ClockSyncState_Object = MibTableColumn
tmnxDS1ClockSyncState = _TmnxDS1ClockSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 22),
    _TmnxDS1ClockSyncState_Type()
)
tmnxDS1ClockSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1ClockSyncState.setStatus("current")
_TmnxDS1ClockMasterPortId_Type = TmnxPortID
_TmnxDS1ClockMasterPortId_Object = MibTableColumn
tmnxDS1ClockMasterPortId = _TmnxDS1ClockMasterPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 23),
    _TmnxDS1ClockMasterPortId_Type()
)
tmnxDS1ClockMasterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1ClockMasterPortId.setStatus("current")


class _TmnxDS1BerSdThreshold_Type(Unsigned32):
    """Custom type tmnxDS1BerSdThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(100, 100),
    )


_TmnxDS1BerSdThreshold_Type.__name__ = "Unsigned32"
_TmnxDS1BerSdThreshold_Object = MibTableColumn
tmnxDS1BerSdThreshold = _TmnxDS1BerSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 24),
    _TmnxDS1BerSdThreshold_Type()
)
tmnxDS1BerSdThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1BerSdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS1BerSdThreshold.setUnits("error bits in million bits received")


class _TmnxDS1BerSfThreshold_Type(Unsigned32):
    """Custom type tmnxDS1BerSfThreshold based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(100, 100),
    )


_TmnxDS1BerSfThreshold_Type.__name__ = "Unsigned32"
_TmnxDS1BerSfThreshold_Object = MibTableColumn
tmnxDS1BerSfThreshold = _TmnxDS1BerSfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 25),
    _TmnxDS1BerSfThreshold_Type()
)
tmnxDS1BerSfThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1BerSfThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS1BerSfThreshold.setUnits("error bits in million bits received")


class _TmnxDS1NationalUseBits_Type(Bits):
    """Custom type tmnxDS1NationalUseBits based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("sa4", 0),
          ("sa5", 1),
          ("sa6", 2),
          ("sa7", 3),
          ("sa8", 4))
    )

_TmnxDS1NationalUseBits_Type.__name__ = "Bits"
_TmnxDS1NationalUseBits_Object = MibTableColumn
tmnxDS1NationalUseBits = _TmnxDS1NationalUseBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 12, 1, 26),
    _TmnxDS1NationalUseBits_Type()
)
tmnxDS1NationalUseBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1NationalUseBits.setStatus("current")
_TmnxDS0ChanGroupTable_Object = MibTable
tmnxDS0ChanGroupTable = _TmnxDS0ChanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13)
)
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupTable.setStatus("current")
_TmnxDS0ChanGroupEntry_Object = MibTableRow
tmnxDS0ChanGroupEntry = _TmnxDS0ChanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1)
)
tmnxDS0ChanGroupEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupEntry.setStatus("current")
_TmnxDS0ChanGroupRowStatus_Type = RowStatus
_TmnxDS0ChanGroupRowStatus_Object = MibTableColumn
tmnxDS0ChanGroupRowStatus = _TmnxDS0ChanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 1),
    _TmnxDS0ChanGroupRowStatus_Type()
)
tmnxDS0ChanGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupRowStatus.setStatus("current")
_TmnxDS0ChanGroupTimeSlots_Type = TmnxDs0ChannelList
_TmnxDS0ChanGroupTimeSlots_Object = MibTableColumn
tmnxDS0ChanGroupTimeSlots = _TmnxDS0ChanGroupTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 2),
    _TmnxDS0ChanGroupTimeSlots_Type()
)
tmnxDS0ChanGroupTimeSlots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupTimeSlots.setStatus("current")


class _TmnxDS0ChanGroupSpeed_Type(Integer32):
    """Custom type tmnxDS0ChanGroupSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed-56", 1),
          ("speed-64", 2))
    )


_TmnxDS0ChanGroupSpeed_Type.__name__ = "Integer32"
_TmnxDS0ChanGroupSpeed_Object = MibTableColumn
tmnxDS0ChanGroupSpeed = _TmnxDS0ChanGroupSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 3),
    _TmnxDS0ChanGroupSpeed_Type()
)
tmnxDS0ChanGroupSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupSpeed.setStatus("current")


class _TmnxDS0ChanGroupCRC_Type(Integer32):
    """Custom type tmnxDS0ChanGroupCRC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_TmnxDS0ChanGroupCRC_Type.__name__ = "Integer32"
_TmnxDS0ChanGroupCRC_Object = MibTableColumn
tmnxDS0ChanGroupCRC = _TmnxDS0ChanGroupCRC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 4),
    _TmnxDS0ChanGroupCRC_Type()
)
tmnxDS0ChanGroupCRC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupCRC.setStatus("current")


class _TmnxDS0ChanGroupMTU_Type(Unsigned32):
    """Custom type tmnxDS0ChanGroupMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9208),
    )


_TmnxDS0ChanGroupMTU_Type.__name__ = "Unsigned32"
_TmnxDS0ChanGroupMTU_Object = MibTableColumn
tmnxDS0ChanGroupMTU = _TmnxDS0ChanGroupMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 5),
    _TmnxDS0ChanGroupMTU_Type()
)
tmnxDS0ChanGroupMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupMTU.setUnits("bytes")
_TmnxDS0ChanGroupOperMTU_Type = Unsigned32
_TmnxDS0ChanGroupOperMTU_Object = MibTableColumn
tmnxDS0ChanGroupOperMTU = _TmnxDS0ChanGroupOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 6),
    _TmnxDS0ChanGroupOperMTU_Type()
)
tmnxDS0ChanGroupOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupOperMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupOperMTU.setUnits("bytes")
_TmnxDS0ChanGroupLastChangeTime_Type = TimeStamp
_TmnxDS0ChanGroupLastChangeTime_Object = MibTableColumn
tmnxDS0ChanGroupLastChangeTime = _TmnxDS0ChanGroupLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 7),
    _TmnxDS0ChanGroupLastChangeTime_Type()
)
tmnxDS0ChanGroupLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupLastChangeTime.setStatus("current")


class _TmnxDS0ChanGroupIdleCycleFlags_Type(TmnxDSXIdleCycleFlags):
    """Custom type tmnxDS0ChanGroupIdleCycleFlags based on TmnxDSXIdleCycleFlags"""


_TmnxDS0ChanGroupIdleCycleFlags_Object = MibTableColumn
tmnxDS0ChanGroupIdleCycleFlags = _TmnxDS0ChanGroupIdleCycleFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 8),
    _TmnxDS0ChanGroupIdleCycleFlags_Type()
)
tmnxDS0ChanGroupIdleCycleFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupIdleCycleFlags.setStatus("current")
_TmnxDS0ChanGroupScramble_Type = TruthValue
_TmnxDS0ChanGroupScramble_Object = MibTableColumn
tmnxDS0ChanGroupScramble = _TmnxDS0ChanGroupScramble_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 9),
    _TmnxDS0ChanGroupScramble_Type()
)
tmnxDS0ChanGroupScramble.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupScramble.setStatus("current")


class _TmnxDS0ChanGroupAcctPolicyId_Type(Unsigned32):
    """Custom type tmnxDS0ChanGroupAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxDS0ChanGroupAcctPolicyId_Type.__name__ = "Unsigned32"
_TmnxDS0ChanGroupAcctPolicyId_Object = MibTableColumn
tmnxDS0ChanGroupAcctPolicyId = _TmnxDS0ChanGroupAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 10),
    _TmnxDS0ChanGroupAcctPolicyId_Type()
)
tmnxDS0ChanGroupAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupAcctPolicyId.setStatus("current")


class _TmnxDS0ChanGroupCollectStats_Type(TruthValue):
    """Custom type tmnxDS0ChanGroupCollectStats based on TruthValue"""


_TmnxDS0ChanGroupCollectStats_Object = MibTableColumn
tmnxDS0ChanGroupCollectStats = _TmnxDS0ChanGroupCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 11),
    _TmnxDS0ChanGroupCollectStats_Type()
)
tmnxDS0ChanGroupCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupCollectStats.setStatus("current")


class _TmnxDS0ChanGroupPayloadFillType_Type(TmnxDSXIdleFillType):
    """Custom type tmnxDS0ChanGroupPayloadFillType based on TmnxDSXIdleFillType"""


_TmnxDS0ChanGroupPayloadFillType_Object = MibTableColumn
tmnxDS0ChanGroupPayloadFillType = _TmnxDS0ChanGroupPayloadFillType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 12),
    _TmnxDS0ChanGroupPayloadFillType_Type()
)
tmnxDS0ChanGroupPayloadFillType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupPayloadFillType.setStatus("current")


class _TmnxDS0ChanGroupPayloadPattern_Type(Unsigned32):
    """Custom type tmnxDS0ChanGroupPayloadPattern based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxDS0ChanGroupPayloadPattern_Type.__name__ = "Unsigned32"
_TmnxDS0ChanGroupPayloadPattern_Object = MibTableColumn
tmnxDS0ChanGroupPayloadPattern = _TmnxDS0ChanGroupPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 13),
    _TmnxDS0ChanGroupPayloadPattern_Type()
)
tmnxDS0ChanGroupPayloadPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupPayloadPattern.setStatus("current")


class _TmnxDS0ChanGroupSignalFillType_Type(TmnxDSXIdleFillType):
    """Custom type tmnxDS0ChanGroupSignalFillType based on TmnxDSXIdleFillType"""


_TmnxDS0ChanGroupSignalFillType_Object = MibTableColumn
tmnxDS0ChanGroupSignalFillType = _TmnxDS0ChanGroupSignalFillType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 14),
    _TmnxDS0ChanGroupSignalFillType_Type()
)
tmnxDS0ChanGroupSignalFillType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupSignalFillType.setStatus("current")


class _TmnxDS0ChanGroupSignalPattern_Type(Unsigned32):
    """Custom type tmnxDS0ChanGroupSignalPattern based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TmnxDS0ChanGroupSignalPattern_Type.__name__ = "Unsigned32"
_TmnxDS0ChanGroupSignalPattern_Object = MibTableColumn
tmnxDS0ChanGroupSignalPattern = _TmnxDS0ChanGroupSignalPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 15),
    _TmnxDS0ChanGroupSignalPattern_Type()
)
tmnxDS0ChanGroupSignalPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupSignalPattern.setStatus("current")


class _TmnxDS0ChanGroupBerSfLinkDown_Type(TruthValue):
    """Custom type tmnxDS0ChanGroupBerSfLinkDown based on TruthValue"""


_TmnxDS0ChanGroupBerSfLinkDown_Object = MibTableColumn
tmnxDS0ChanGroupBerSfLinkDown = _TmnxDS0ChanGroupBerSfLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 13, 1, 16),
    _TmnxDS0ChanGroupBerSfLinkDown_Type()
)
tmnxDS0ChanGroupBerSfLinkDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS0ChanGroupBerSfLinkDown.setStatus("current")
_TmnxBundleTable_Object = MibTable
tmnxBundleTable = _TmnxBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14)
)
if mibBuilder.loadTexts:
    tmnxBundleTable.setStatus("current")
_TmnxBundleEntry_Object = MibTableRow
tmnxBundleEntry = _TmnxBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1)
)
tmnxBundleEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
)
if mibBuilder.loadTexts:
    tmnxBundleEntry.setStatus("current")
_TmnxBundleBundleID_Type = TmnxBundleID
_TmnxBundleBundleID_Object = MibTableColumn
tmnxBundleBundleID = _TmnxBundleBundleID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 1),
    _TmnxBundleBundleID_Type()
)
tmnxBundleBundleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBundleBundleID.setStatus("current")
_TmnxBundleRowStatus_Type = RowStatus
_TmnxBundleRowStatus_Object = MibTableColumn
tmnxBundleRowStatus = _TmnxBundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 2),
    _TmnxBundleRowStatus_Type()
)
tmnxBundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleRowStatus.setStatus("current")


class _TmnxBundleType_Type(Integer32):
    """Custom type tmnxBundleType based on Integer32"""
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
        *(("imagrp", 3),
          ("mlfr", 2),
          ("mlppp", 1))
    )


_TmnxBundleType_Type.__name__ = "Integer32"
_TmnxBundleType_Object = MibTableColumn
tmnxBundleType = _TmnxBundleType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 3),
    _TmnxBundleType_Type()
)
tmnxBundleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleType.setStatus("current")


class _TmnxBundleMinimumLinks_Type(Unsigned32):
    """Custom type tmnxBundleMinimumLinks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxBundleMinimumLinks_Type.__name__ = "Unsigned32"
_TmnxBundleMinimumLinks_Object = MibTableColumn
tmnxBundleMinimumLinks = _TmnxBundleMinimumLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 4),
    _TmnxBundleMinimumLinks_Type()
)
tmnxBundleMinimumLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMinimumLinks.setStatus("current")
_TmnxBundleNumLinks_Type = Unsigned32
_TmnxBundleNumLinks_Object = MibTableColumn
tmnxBundleNumLinks = _TmnxBundleNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 5),
    _TmnxBundleNumLinks_Type()
)
tmnxBundleNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleNumLinks.setStatus("current")
_TmnxBundleNumActiveLinks_Type = Unsigned32
_TmnxBundleNumActiveLinks_Object = MibTableColumn
tmnxBundleNumActiveLinks = _TmnxBundleNumActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 6),
    _TmnxBundleNumActiveLinks_Type()
)
tmnxBundleNumActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleNumActiveLinks.setStatus("current")


class _TmnxBundleMRRU_Type(Unsigned32):
    """Custom type tmnxBundleMRRU based on Unsigned32"""
    defaultValue = 1524

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1500, 9206),
    )


_TmnxBundleMRRU_Type.__name__ = "Unsigned32"
_TmnxBundleMRRU_Object = MibTableColumn
tmnxBundleMRRU = _TmnxBundleMRRU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 7),
    _TmnxBundleMRRU_Type()
)
tmnxBundleMRRU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMRRU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleMRRU.setUnits("bytes")
_TmnxBundleOperMRRU_Type = Unsigned32
_TmnxBundleOperMRRU_Object = MibTableColumn
tmnxBundleOperMRRU = _TmnxBundleOperMRRU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 8),
    _TmnxBundleOperMRRU_Type()
)
tmnxBundleOperMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleOperMRRU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleOperMRRU.setUnits("bytes")
_TmnxBundlePeerMRRU_Type = Unsigned32
_TmnxBundlePeerMRRU_Object = MibTableColumn
tmnxBundlePeerMRRU = _TmnxBundlePeerMRRU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 9),
    _TmnxBundlePeerMRRU_Type()
)
tmnxBundlePeerMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundlePeerMRRU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundlePeerMRRU.setUnits("bytes")
_TmnxBundleOperMTU_Type = Unsigned32
_TmnxBundleOperMTU_Object = MibTableColumn
tmnxBundleOperMTU = _TmnxBundleOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 10),
    _TmnxBundleOperMTU_Type()
)
tmnxBundleOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleOperMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleOperMTU.setUnits("bytes")


class _TmnxBundleRedDiffDelay_Type(Unsigned32):
    """Custom type tmnxBundleRedDiffDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
        ValueRangeConstraint(0, 50),
    )


_TmnxBundleRedDiffDelay_Type.__name__ = "Unsigned32"
_TmnxBundleRedDiffDelay_Object = MibTableColumn
tmnxBundleRedDiffDelay = _TmnxBundleRedDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 11),
    _TmnxBundleRedDiffDelay_Type()
)
tmnxBundleRedDiffDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleRedDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleRedDiffDelay.setUnits("milliseconds")


class _TmnxBundleRedDiffDelayAction_Type(Integer32):
    """Custom type tmnxBundleRedDiffDelayAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("none", 0))
    )


_TmnxBundleRedDiffDelayAction_Type.__name__ = "Integer32"
_TmnxBundleRedDiffDelayAction_Object = MibTableColumn
tmnxBundleRedDiffDelayAction = _TmnxBundleRedDiffDelayAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 12),
    _TmnxBundleRedDiffDelayAction_Type()
)
tmnxBundleRedDiffDelayAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleRedDiffDelayAction.setStatus("current")


class _TmnxBundleYellowDiffDelay_Type(Unsigned32):
    """Custom type tmnxBundleYellowDiffDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_TmnxBundleYellowDiffDelay_Type.__name__ = "Unsigned32"
_TmnxBundleYellowDiffDelay_Object = MibTableColumn
tmnxBundleYellowDiffDelay = _TmnxBundleYellowDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 13),
    _TmnxBundleYellowDiffDelay_Type()
)
tmnxBundleYellowDiffDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleYellowDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleYellowDiffDelay.setUnits("milliseconds")


class _TmnxBundleShortSequence_Type(TruthValue):
    """Custom type tmnxBundleShortSequence based on TruthValue"""


_TmnxBundleShortSequence_Object = MibTableColumn
tmnxBundleShortSequence = _TmnxBundleShortSequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 14),
    _TmnxBundleShortSequence_Type()
)
tmnxBundleShortSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleShortSequence.setStatus("current")
_TmnxBundleLastChangeTime_Type = TimeStamp
_TmnxBundleLastChangeTime_Object = MibTableColumn
tmnxBundleLastChangeTime = _TmnxBundleLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 15),
    _TmnxBundleLastChangeTime_Type()
)
tmnxBundleLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleLastChangeTime.setStatus("current")


class _TmnxBundleFragmentThreshold_Type(Unsigned32):
    """Custom type tmnxBundleFragmentThreshold based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 512),
    )


_TmnxBundleFragmentThreshold_Type.__name__ = "Unsigned32"
_TmnxBundleFragmentThreshold_Object = MibTableColumn
tmnxBundleFragmentThreshold = _TmnxBundleFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 16),
    _TmnxBundleFragmentThreshold_Type()
)
tmnxBundleFragmentThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleFragmentThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleFragmentThreshold.setUnits("bytes")
_TmnxBundleUpTime_Type = Unsigned32
_TmnxBundleUpTime_Object = MibTableColumn
tmnxBundleUpTime = _TmnxBundleUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 17),
    _TmnxBundleUpTime_Type()
)
tmnxBundleUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleUpTime.setUnits("seconds")
_TmnxBundleInputDiscards_Type = Counter32
_TmnxBundleInputDiscards_Object = MibTableColumn
tmnxBundleInputDiscards = _TmnxBundleInputDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 18),
    _TmnxBundleInputDiscards_Type()
)
tmnxBundleInputDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleInputDiscards.setStatus("current")
_TmnxBundlePrimaryMemberPortID_Type = TmnxPortID
_TmnxBundlePrimaryMemberPortID_Object = MibTableColumn
tmnxBundlePrimaryMemberPortID = _TmnxBundlePrimaryMemberPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 19),
    _TmnxBundlePrimaryMemberPortID_Type()
)
tmnxBundlePrimaryMemberPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundlePrimaryMemberPortID.setStatus("current")


class _TmnxBundleLFI_Type(TruthValue):
    """Custom type tmnxBundleLFI based on TruthValue"""


_TmnxBundleLFI_Object = MibTableColumn
tmnxBundleLFI = _TmnxBundleLFI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 20),
    _TmnxBundleLFI_Type()
)
tmnxBundleLFI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleLFI.setStatus("current")


class _TmnxBundleProtectedType_Type(Integer32):
    """Custom type tmnxBundleProtectedType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("protection", 2),
          ("working", 1))
    )


_TmnxBundleProtectedType_Type.__name__ = "Integer32"
_TmnxBundleProtectedType_Object = MibTableColumn
tmnxBundleProtectedType = _TmnxBundleProtectedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 21),
    _TmnxBundleProtectedType_Type()
)
tmnxBundleProtectedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleProtectedType.setStatus("current")


class _TmnxBundleParentBundle_Type(TmnxBundleID):
    """Custom type tmnxBundleParentBundle based on TmnxBundleID"""
    defaultValue = 0


_TmnxBundleParentBundle_Object = MibTableColumn
tmnxBundleParentBundle = _TmnxBundleParentBundle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 14, 1, 22),
    _TmnxBundleParentBundle_Type()
)
tmnxBundleParentBundle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleParentBundle.setStatus("current")
_TmnxBundleMemberTable_Object = MibTable
tmnxBundleMemberTable = _TmnxBundleMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15)
)
if mibBuilder.loadTexts:
    tmnxBundleMemberTable.setStatus("current")
_TmnxBundleMemberEntry_Object = MibTableRow
tmnxBundleMemberEntry = _TmnxBundleMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15, 1)
)
tmnxBundleMemberEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxBundleMemberEntry.setStatus("current")
_TmnxBundleMemberRowStatus_Type = RowStatus
_TmnxBundleMemberRowStatus_Object = MibTableColumn
tmnxBundleMemberRowStatus = _TmnxBundleMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15, 1, 1),
    _TmnxBundleMemberRowStatus_Type()
)
tmnxBundleMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMemberRowStatus.setStatus("current")
_TmnxBundleMemberActive_Type = TruthValue
_TmnxBundleMemberActive_Object = MibTableColumn
tmnxBundleMemberActive = _TmnxBundleMemberActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15, 1, 2),
    _TmnxBundleMemberActive_Type()
)
tmnxBundleMemberActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberActive.setStatus("current")


class _TmnxBundleMemberDownReason_Type(Integer32):
    """Custom type tmnxBundleMemberDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("mismatchEndPtDiscriminator", 3),
          ("none", 0),
          ("other", 7),
          ("outOfService", 1),
          ("peerInvalidMlHdrFmt", 6),
          ("peerNotBundleMember", 4),
          ("redDiffDelayExceeded", 2),
          ("underNegotiation", 5))
    )


_TmnxBundleMemberDownReason_Type.__name__ = "Integer32"
_TmnxBundleMemberDownReason_Object = MibTableColumn
tmnxBundleMemberDownReason = _TmnxBundleMemberDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15, 1, 3),
    _TmnxBundleMemberDownReason_Type()
)
tmnxBundleMemberDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberDownReason.setStatus("current")
_TmnxBundleMemberUpTime_Type = Unsigned32
_TmnxBundleMemberUpTime_Object = MibTableColumn
tmnxBundleMemberUpTime = _TmnxBundleMemberUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 15, 1, 4),
    _TmnxBundleMemberUpTime_Type()
)
tmnxBundleMemberUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleMemberUpTime.setUnits("seconds")
_TmnxPortToChannelTable_Object = MibTable
tmnxPortToChannelTable = _TmnxPortToChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 16)
)
if mibBuilder.loadTexts:
    tmnxPortToChannelTable.setStatus("current")
_TmnxPortToChannelEntry_Object = MibTableRow
tmnxPortToChannelEntry = _TmnxPortToChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 16, 1)
)
tmnxPortToChannelEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tmnxChannelIdxString"),
)
if mibBuilder.loadTexts:
    tmnxPortToChannelEntry.setStatus("current")
_TmnxChannelIdxString_Type = DisplayString
_TmnxChannelIdxString_Object = MibTableColumn
tmnxChannelIdxString = _TmnxChannelIdxString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 16, 1, 1),
    _TmnxChannelIdxString_Type()
)
tmnxChannelIdxString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxChannelIdxString.setStatus("current")
_TmnxChannelPortID_Type = TmnxPortID
_TmnxChannelPortID_Object = MibTableColumn
tmnxChannelPortID = _TmnxChannelPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 16, 1, 2),
    _TmnxChannelPortID_Type()
)
tmnxChannelPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChannelPortID.setStatus("current")
_TmnxPortIngrMdaQosStatTable_Object = MibTable
tmnxPortIngrMdaQosStatTable = _TmnxPortIngrMdaQosStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17)
)
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQosStatTable.setStatus("current")
_TmnxPortIngrMdaQosStatEntry_Object = MibTableRow
tmnxPortIngrMdaQosStatEntry = _TmnxPortIngrMdaQosStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1)
)
tmnxPortIngrMdaQosStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQosStatEntry.setStatus("current")
_TmnxPortIngrMdaQos00StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos00StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos00StatDropPkts = _TmnxPortIngrMdaQos00StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 1),
    _TmnxPortIngrMdaQos00StatDropPkts_Type()
)
tmnxPortIngrMdaQos00StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos00StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos00StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos00StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos00StatDropOcts = _TmnxPortIngrMdaQos00StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 2),
    _TmnxPortIngrMdaQos00StatDropOcts_Type()
)
tmnxPortIngrMdaQos00StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos00StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos01StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos01StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos01StatDropPkts = _TmnxPortIngrMdaQos01StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 3),
    _TmnxPortIngrMdaQos01StatDropPkts_Type()
)
tmnxPortIngrMdaQos01StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos01StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos01StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos01StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos01StatDropOcts = _TmnxPortIngrMdaQos01StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 4),
    _TmnxPortIngrMdaQos01StatDropOcts_Type()
)
tmnxPortIngrMdaQos01StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos01StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos02StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos02StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos02StatDropPkts = _TmnxPortIngrMdaQos02StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 5),
    _TmnxPortIngrMdaQos02StatDropPkts_Type()
)
tmnxPortIngrMdaQos02StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos02StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos02StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos02StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos02StatDropOcts = _TmnxPortIngrMdaQos02StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 6),
    _TmnxPortIngrMdaQos02StatDropOcts_Type()
)
tmnxPortIngrMdaQos02StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos02StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos03StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos03StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos03StatDropPkts = _TmnxPortIngrMdaQos03StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 7),
    _TmnxPortIngrMdaQos03StatDropPkts_Type()
)
tmnxPortIngrMdaQos03StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos03StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos03StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos03StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos03StatDropOcts = _TmnxPortIngrMdaQos03StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 8),
    _TmnxPortIngrMdaQos03StatDropOcts_Type()
)
tmnxPortIngrMdaQos03StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos03StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos04StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos04StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos04StatDropPkts = _TmnxPortIngrMdaQos04StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 9),
    _TmnxPortIngrMdaQos04StatDropPkts_Type()
)
tmnxPortIngrMdaQos04StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos04StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos04StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos04StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos04StatDropOcts = _TmnxPortIngrMdaQos04StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 10),
    _TmnxPortIngrMdaQos04StatDropOcts_Type()
)
tmnxPortIngrMdaQos04StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos04StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos05StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos05StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos05StatDropPkts = _TmnxPortIngrMdaQos05StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 11),
    _TmnxPortIngrMdaQos05StatDropPkts_Type()
)
tmnxPortIngrMdaQos05StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos05StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos05StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos05StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos05StatDropOcts = _TmnxPortIngrMdaQos05StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 12),
    _TmnxPortIngrMdaQos05StatDropOcts_Type()
)
tmnxPortIngrMdaQos05StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos05StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos06StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos06StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos06StatDropPkts = _TmnxPortIngrMdaQos06StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 13),
    _TmnxPortIngrMdaQos06StatDropPkts_Type()
)
tmnxPortIngrMdaQos06StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos06StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos06StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos06StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos06StatDropOcts = _TmnxPortIngrMdaQos06StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 14),
    _TmnxPortIngrMdaQos06StatDropOcts_Type()
)
tmnxPortIngrMdaQos06StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos06StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos07StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos07StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos07StatDropPkts = _TmnxPortIngrMdaQos07StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 15),
    _TmnxPortIngrMdaQos07StatDropPkts_Type()
)
tmnxPortIngrMdaQos07StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos07StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos07StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos07StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos07StatDropOcts = _TmnxPortIngrMdaQos07StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 16),
    _TmnxPortIngrMdaQos07StatDropOcts_Type()
)
tmnxPortIngrMdaQos07StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos07StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos08StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos08StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos08StatDropPkts = _TmnxPortIngrMdaQos08StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 17),
    _TmnxPortIngrMdaQos08StatDropPkts_Type()
)
tmnxPortIngrMdaQos08StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos08StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos08StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos08StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos08StatDropOcts = _TmnxPortIngrMdaQos08StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 18),
    _TmnxPortIngrMdaQos08StatDropOcts_Type()
)
tmnxPortIngrMdaQos08StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos08StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos09StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos09StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos09StatDropPkts = _TmnxPortIngrMdaQos09StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 19),
    _TmnxPortIngrMdaQos09StatDropPkts_Type()
)
tmnxPortIngrMdaQos09StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos09StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos09StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos09StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos09StatDropOcts = _TmnxPortIngrMdaQos09StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 20),
    _TmnxPortIngrMdaQos09StatDropOcts_Type()
)
tmnxPortIngrMdaQos09StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos09StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos10StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos10StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos10StatDropPkts = _TmnxPortIngrMdaQos10StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 21),
    _TmnxPortIngrMdaQos10StatDropPkts_Type()
)
tmnxPortIngrMdaQos10StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos10StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos10StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos10StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos10StatDropOcts = _TmnxPortIngrMdaQos10StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 22),
    _TmnxPortIngrMdaQos10StatDropOcts_Type()
)
tmnxPortIngrMdaQos10StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos10StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos11StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos11StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos11StatDropPkts = _TmnxPortIngrMdaQos11StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 23),
    _TmnxPortIngrMdaQos11StatDropPkts_Type()
)
tmnxPortIngrMdaQos11StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos11StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos11StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos11StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos11StatDropOcts = _TmnxPortIngrMdaQos11StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 24),
    _TmnxPortIngrMdaQos11StatDropOcts_Type()
)
tmnxPortIngrMdaQos11StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos11StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos12StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos12StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos12StatDropPkts = _TmnxPortIngrMdaQos12StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 25),
    _TmnxPortIngrMdaQos12StatDropPkts_Type()
)
tmnxPortIngrMdaQos12StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos12StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos12StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos12StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos12StatDropOcts = _TmnxPortIngrMdaQos12StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 26),
    _TmnxPortIngrMdaQos12StatDropOcts_Type()
)
tmnxPortIngrMdaQos12StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos12StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos13StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos13StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos13StatDropPkts = _TmnxPortIngrMdaQos13StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 27),
    _TmnxPortIngrMdaQos13StatDropPkts_Type()
)
tmnxPortIngrMdaQos13StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos13StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos13StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos13StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos13StatDropOcts = _TmnxPortIngrMdaQos13StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 28),
    _TmnxPortIngrMdaQos13StatDropOcts_Type()
)
tmnxPortIngrMdaQos13StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos13StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos14StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos14StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos14StatDropPkts = _TmnxPortIngrMdaQos14StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 29),
    _TmnxPortIngrMdaQos14StatDropPkts_Type()
)
tmnxPortIngrMdaQos14StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos14StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos14StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos14StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos14StatDropOcts = _TmnxPortIngrMdaQos14StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 30),
    _TmnxPortIngrMdaQos14StatDropOcts_Type()
)
tmnxPortIngrMdaQos14StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos14StatDropOcts.setStatus("current")
_TmnxPortIngrMdaQos15StatDropPkts_Type = Counter64
_TmnxPortIngrMdaQos15StatDropPkts_Object = MibTableColumn
tmnxPortIngrMdaQos15StatDropPkts = _TmnxPortIngrMdaQos15StatDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 31),
    _TmnxPortIngrMdaQos15StatDropPkts_Type()
)
tmnxPortIngrMdaQos15StatDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos15StatDropPkts.setStatus("current")
_TmnxPortIngrMdaQos15StatDropOcts_Type = Counter64
_TmnxPortIngrMdaQos15StatDropOcts_Object = MibTableColumn
tmnxPortIngrMdaQos15StatDropOcts = _TmnxPortIngrMdaQos15StatDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 17, 1, 32),
    _TmnxPortIngrMdaQos15StatDropOcts_Type()
)
tmnxPortIngrMdaQos15StatDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQos15StatDropOcts.setStatus("current")
_TmnxSonetGroupTable_Object = MibTable
tmnxSonetGroupTable = _TmnxSonetGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18)
)
if mibBuilder.loadTexts:
    tmnxSonetGroupTable.setStatus("current")
_TmnxSonetGroupEntry_Object = MibTableRow
tmnxSonetGroupEntry = _TmnxSonetGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18, 1)
)
tmnxSonetGroupEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxSonetGroupEntry.setStatus("current")
_TmnxSonetGroupType_Type = TmnxMDAChanType
_TmnxSonetGroupType_Object = MibTableColumn
tmnxSonetGroupType = _TmnxSonetGroupType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18, 1, 1),
    _TmnxSonetGroupType_Type()
)
tmnxSonetGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetGroupType.setStatus("current")
_TmnxSonetGroupParentPortID_Type = TmnxPortID
_TmnxSonetGroupParentPortID_Object = MibTableColumn
tmnxSonetGroupParentPortID = _TmnxSonetGroupParentPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18, 1, 2),
    _TmnxSonetGroupParentPortID_Type()
)
tmnxSonetGroupParentPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetGroupParentPortID.setStatus("current")
_TmnxSonetGroupChildType_Type = TmnxMDAChanType
_TmnxSonetGroupChildType_Object = MibTableColumn
tmnxSonetGroupChildType = _TmnxSonetGroupChildType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18, 1, 3),
    _TmnxSonetGroupChildType_Type()
)
tmnxSonetGroupChildType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSonetGroupChildType.setStatus("current")
_TmnxSonetGroupName_Type = TNamedItemOrEmpty
_TmnxSonetGroupName_Object = MibTableColumn
tmnxSonetGroupName = _TmnxSonetGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 18, 1, 4),
    _TmnxSonetGroupName_Type()
)
tmnxSonetGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSonetGroupName.setStatus("current")
_TmnxPortScalarObjs_ObjectIdentity = ObjectIdentity
tmnxPortScalarObjs = _TmnxPortScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 19)
)


class _TmnxL4LoadBalancing_Type(TruthValue):
    """Custom type tmnxL4LoadBalancing based on TruthValue"""


_TmnxL4LoadBalancing_Object = MibScalar
tmnxL4LoadBalancing = _TmnxL4LoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 19, 1),
    _TmnxL4LoadBalancing_Type()
)
tmnxL4LoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxL4LoadBalancing.setStatus("current")


class _TmnxLsrIpLoadBalancing_Type(Integer32):
    """Custom type tmnxLsrIpLoadBalancing based on Integer32"""
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
        *(("ip-only", 3),
          ("label-ip", 2),
          ("label-only", 1))
    )


_TmnxLsrIpLoadBalancing_Type.__name__ = "Integer32"
_TmnxLsrIpLoadBalancing_Object = MibScalar
tmnxLsrIpLoadBalancing = _TmnxLsrIpLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 19, 2),
    _TmnxLsrIpLoadBalancing_Type()
)
tmnxLsrIpLoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLsrIpLoadBalancing.setStatus("current")


class _TmnxIpLoadBalancing_Type(Integer32):
    """Custom type tmnxIpLoadBalancing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("systemIp", 2))
    )


_TmnxIpLoadBalancing_Type.__name__ = "Integer32"
_TmnxIpLoadBalancing_Object = MibScalar
tmnxIpLoadBalancing = _TmnxIpLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 19, 3),
    _TmnxIpLoadBalancing_Type()
)
tmnxIpLoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIpLoadBalancing.setStatus("current")
_TmnxCiscoHDLCTable_Object = MibTable
tmnxCiscoHDLCTable = _TmnxCiscoHDLCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20)
)
if mibBuilder.loadTexts:
    tmnxCiscoHDLCTable.setStatus("current")
_TmnxCiscoHDLCEntry_Object = MibTableRow
tmnxCiscoHDLCEntry = _TmnxCiscoHDLCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20, 1)
)
tmnxCiscoHDLCEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxCiscoHDLCEntry.setStatus("current")


class _TmnxCiscoHDLCKeepAliveInt_Type(Unsigned32):
    """Custom type tmnxCiscoHDLCKeepAliveInt based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TmnxCiscoHDLCKeepAliveInt_Type.__name__ = "Unsigned32"
_TmnxCiscoHDLCKeepAliveInt_Object = MibTableColumn
tmnxCiscoHDLCKeepAliveInt = _TmnxCiscoHDLCKeepAliveInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20, 1, 1),
    _TmnxCiscoHDLCKeepAliveInt_Type()
)
tmnxCiscoHDLCKeepAliveInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCKeepAliveInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCKeepAliveInt.setUnits("seconds")


class _TmnxCiscoHDLCUpCount_Type(Unsigned32):
    """Custom type tmnxCiscoHDLCUpCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TmnxCiscoHDLCUpCount_Type.__name__ = "Unsigned32"
_TmnxCiscoHDLCUpCount_Object = MibTableColumn
tmnxCiscoHDLCUpCount = _TmnxCiscoHDLCUpCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20, 1, 2),
    _TmnxCiscoHDLCUpCount_Type()
)
tmnxCiscoHDLCUpCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCUpCount.setStatus("current")


class _TmnxCiscoHDLCDownCount_Type(Unsigned32):
    """Custom type tmnxCiscoHDLCDownCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_TmnxCiscoHDLCDownCount_Type.__name__ = "Unsigned32"
_TmnxCiscoHDLCDownCount_Object = MibTableColumn
tmnxCiscoHDLCDownCount = _TmnxCiscoHDLCDownCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20, 1, 3),
    _TmnxCiscoHDLCDownCount_Type()
)
tmnxCiscoHDLCDownCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCDownCount.setStatus("current")
_TmnxCiscoHDLCOperState_Type = TmnxOperState
_TmnxCiscoHDLCOperState_Object = MibTableColumn
tmnxCiscoHDLCOperState = _TmnxCiscoHDLCOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 20, 1, 4),
    _TmnxCiscoHDLCOperState_Type()
)
tmnxCiscoHDLCOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCOperState.setStatus("current")
_TmnxBundleImaGrpTable_Object = MibTable
tmnxBundleImaGrpTable = _TmnxBundleImaGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21)
)
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTable.setStatus("current")
_TmnxBundleImaGrpEntry_Object = MibTableRow
tmnxBundleImaGrpEntry = _TmnxBundleImaGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1)
)
tmnxBundleImaGrpEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
)
if mibBuilder.loadTexts:
    tmnxBundleImaGrpEntry.setStatus("current")


class _TmnxBundleImaGrpLnkActTimer_Type(Unsigned32):
    """Custom type tmnxBundleImaGrpLnkActTimer based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30000),
    )


_TmnxBundleImaGrpLnkActTimer_Type.__name__ = "Unsigned32"
_TmnxBundleImaGrpLnkActTimer_Object = MibTableColumn
tmnxBundleImaGrpLnkActTimer = _TmnxBundleImaGrpLnkActTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 1),
    _TmnxBundleImaGrpLnkActTimer_Type()
)
tmnxBundleImaGrpLnkActTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLnkActTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLnkActTimer.setUnits("milliseconds")


class _TmnxBundleImaGrpLnkDeactTimer_Type(Unsigned32):
    """Custom type tmnxBundleImaGrpLnkDeactTimer based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30000),
    )


_TmnxBundleImaGrpLnkDeactTimer_Type.__name__ = "Unsigned32"
_TmnxBundleImaGrpLnkDeactTimer_Object = MibTableColumn
tmnxBundleImaGrpLnkDeactTimer = _TmnxBundleImaGrpLnkDeactTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 2),
    _TmnxBundleImaGrpLnkDeactTimer_Type()
)
tmnxBundleImaGrpLnkDeactTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLnkDeactTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLnkDeactTimer.setUnits("milliseconds")


class _TmnxBundleImaGrpSymmetryMode_Type(Integer32):
    """Custom type tmnxBundleImaGrpSymmetryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("symmetric", 1)
    )


_TmnxBundleImaGrpSymmetryMode_Type.__name__ = "Integer32"
_TmnxBundleImaGrpSymmetryMode_Object = MibTableColumn
tmnxBundleImaGrpSymmetryMode = _TmnxBundleImaGrpSymmetryMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 3),
    _TmnxBundleImaGrpSymmetryMode_Type()
)
tmnxBundleImaGrpSymmetryMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSymmetryMode.setStatus("current")
_TmnxBundleImaGrpTxId_Type = Integer32
_TmnxBundleImaGrpTxId_Object = MibTableColumn
tmnxBundleImaGrpTxId = _TmnxBundleImaGrpTxId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 4),
    _TmnxBundleImaGrpTxId_Type()
)
tmnxBundleImaGrpTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTxId.setStatus("current")
_TmnxBundleImaGrpRxId_Type = Integer32
_TmnxBundleImaGrpRxId_Object = MibTableColumn
tmnxBundleImaGrpRxId = _TmnxBundleImaGrpRxId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 5),
    _TmnxBundleImaGrpRxId_Type()
)
tmnxBundleImaGrpRxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpRxId.setStatus("current")
_TmnxBundleImaGrpTxRefLnk_Type = TmnxPortID
_TmnxBundleImaGrpTxRefLnk_Object = MibTableColumn
tmnxBundleImaGrpTxRefLnk = _TmnxBundleImaGrpTxRefLnk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 6),
    _TmnxBundleImaGrpTxRefLnk_Type()
)
tmnxBundleImaGrpTxRefLnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTxRefLnk.setStatus("current")
_TmnxBundleImaGrpRxRefLnk_Type = TmnxPortID
_TmnxBundleImaGrpRxRefLnk_Object = MibTableColumn
tmnxBundleImaGrpRxRefLnk = _TmnxBundleImaGrpRxRefLnk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 7),
    _TmnxBundleImaGrpRxRefLnk_Type()
)
tmnxBundleImaGrpRxRefLnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpRxRefLnk.setStatus("current")
_TmnxBundleImaGrpSmNeState_Type = TmnxImaGrpState
_TmnxBundleImaGrpSmNeState_Object = MibTableColumn
tmnxBundleImaGrpSmNeState = _TmnxBundleImaGrpSmNeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 8),
    _TmnxBundleImaGrpSmNeState_Type()
)
tmnxBundleImaGrpSmNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSmNeState.setStatus("current")
_TmnxBundleImaGrpSmFeState_Type = TmnxImaGrpState
_TmnxBundleImaGrpSmFeState_Object = MibTableColumn
tmnxBundleImaGrpSmFeState = _TmnxBundleImaGrpSmFeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 9),
    _TmnxBundleImaGrpSmFeState_Type()
)
tmnxBundleImaGrpSmFeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSmFeState.setStatus("current")
_TmnxBundleImaGrpSmFailState_Type = TmnxImaGrpFailState
_TmnxBundleImaGrpSmFailState_Object = MibTableColumn
tmnxBundleImaGrpSmFailState = _TmnxBundleImaGrpSmFailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 10),
    _TmnxBundleImaGrpSmFailState_Type()
)
tmnxBundleImaGrpSmFailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSmFailState.setStatus("current")
_TmnxBundleImaGrpSmDownSecs_Type = Counter32
_TmnxBundleImaGrpSmDownSecs_Object = MibTableColumn
tmnxBundleImaGrpSmDownSecs = _TmnxBundleImaGrpSmDownSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 11),
    _TmnxBundleImaGrpSmDownSecs_Type()
)
tmnxBundleImaGrpSmDownSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSmDownSecs.setStatus("current")
_TmnxBundleImaGrpSmOperSecs_Type = Counter32
_TmnxBundleImaGrpSmOperSecs_Object = MibTableColumn
tmnxBundleImaGrpSmOperSecs = _TmnxBundleImaGrpSmOperSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 12),
    _TmnxBundleImaGrpSmOperSecs_Type()
)
tmnxBundleImaGrpSmOperSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpSmOperSecs.setStatus("current")
_TmnxBundleImaGrpAvailTxCR_Type = Gauge32
_TmnxBundleImaGrpAvailTxCR_Object = MibTableColumn
tmnxBundleImaGrpAvailTxCR = _TmnxBundleImaGrpAvailTxCR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 13),
    _TmnxBundleImaGrpAvailTxCR_Type()
)
tmnxBundleImaGrpAvailTxCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpAvailTxCR.setStatus("current")
_TmnxBundleImaGrpAvailRxCR_Type = Gauge32
_TmnxBundleImaGrpAvailRxCR_Object = MibTableColumn
tmnxBundleImaGrpAvailRxCR = _TmnxBundleImaGrpAvailRxCR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 14),
    _TmnxBundleImaGrpAvailRxCR_Type()
)
tmnxBundleImaGrpAvailRxCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpAvailRxCR.setStatus("current")
_TmnxBundleImaGrpNeFails_Type = Counter32
_TmnxBundleImaGrpNeFails_Object = MibTableColumn
tmnxBundleImaGrpNeFails = _TmnxBundleImaGrpNeFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 15),
    _TmnxBundleImaGrpNeFails_Type()
)
tmnxBundleImaGrpNeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpNeFails.setStatus("current")
_TmnxBundleImaGrpFeFails_Type = Counter32
_TmnxBundleImaGrpFeFails_Object = MibTableColumn
tmnxBundleImaGrpFeFails = _TmnxBundleImaGrpFeFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 16),
    _TmnxBundleImaGrpFeFails_Type()
)
tmnxBundleImaGrpFeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpFeFails.setStatus("current")
_TmnxBundleImaGrpTxIcpCells_Type = Counter32
_TmnxBundleImaGrpTxIcpCells_Object = MibTableColumn
tmnxBundleImaGrpTxIcpCells = _TmnxBundleImaGrpTxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 17),
    _TmnxBundleImaGrpTxIcpCells_Type()
)
tmnxBundleImaGrpTxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTxIcpCells.setStatus("current")
_TmnxBundleImaGrpRxIcpCells_Type = Counter32
_TmnxBundleImaGrpRxIcpCells_Object = MibTableColumn
tmnxBundleImaGrpRxIcpCells = _TmnxBundleImaGrpRxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 18),
    _TmnxBundleImaGrpRxIcpCells_Type()
)
tmnxBundleImaGrpRxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpRxIcpCells.setStatus("current")
_TmnxBundleImaGrpErrorIcpCells_Type = Counter32
_TmnxBundleImaGrpErrorIcpCells_Object = MibTableColumn
tmnxBundleImaGrpErrorIcpCells = _TmnxBundleImaGrpErrorIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 19),
    _TmnxBundleImaGrpErrorIcpCells_Type()
)
tmnxBundleImaGrpErrorIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpErrorIcpCells.setStatus("current")
_TmnxBundleImaGrpLostRxIcpCells_Type = Counter32
_TmnxBundleImaGrpLostRxIcpCells_Object = MibTableColumn
tmnxBundleImaGrpLostRxIcpCells = _TmnxBundleImaGrpLostRxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 20),
    _TmnxBundleImaGrpLostRxIcpCells_Type()
)
tmnxBundleImaGrpLostRxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLostRxIcpCells.setStatus("current")
_TmnxBundleImaGrpTxOamLablVal_Type = Integer32
_TmnxBundleImaGrpTxOamLablVal_Object = MibTableColumn
tmnxBundleImaGrpTxOamLablVal = _TmnxBundleImaGrpTxOamLablVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 21),
    _TmnxBundleImaGrpTxOamLablVal_Type()
)
tmnxBundleImaGrpTxOamLablVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTxOamLablVal.setStatus("current")
_TmnxBundleImaGrpRxOamLablVal_Type = Integer32
_TmnxBundleImaGrpRxOamLablVal_Object = MibTableColumn
tmnxBundleImaGrpRxOamLablVal = _TmnxBundleImaGrpRxOamLablVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 22),
    _TmnxBundleImaGrpRxOamLablVal_Type()
)
tmnxBundleImaGrpRxOamLablVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpRxOamLablVal.setStatus("current")


class _TmnxBundleImaGrpAlphaValue_Type(Integer32):
    """Custom type tmnxBundleImaGrpAlphaValue based on Integer32"""
    defaultValue = 2


_TmnxBundleImaGrpAlphaValue_Object = MibTableColumn
tmnxBundleImaGrpAlphaValue = _TmnxBundleImaGrpAlphaValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 23),
    _TmnxBundleImaGrpAlphaValue_Type()
)
tmnxBundleImaGrpAlphaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpAlphaValue.setStatus("current")


class _TmnxBundleImaGrpBetaValue_Type(Integer32):
    """Custom type tmnxBundleImaGrpBetaValue based on Integer32"""
    defaultValue = 2


_TmnxBundleImaGrpBetaValue_Object = MibTableColumn
tmnxBundleImaGrpBetaValue = _TmnxBundleImaGrpBetaValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 24),
    _TmnxBundleImaGrpBetaValue_Type()
)
tmnxBundleImaGrpBetaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpBetaValue.setStatus("current")


class _TmnxBundleImaGrpGammaValue_Type(Integer32):
    """Custom type tmnxBundleImaGrpGammaValue based on Integer32"""
    defaultValue = 1


_TmnxBundleImaGrpGammaValue_Object = MibTableColumn
tmnxBundleImaGrpGammaValue = _TmnxBundleImaGrpGammaValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 25),
    _TmnxBundleImaGrpGammaValue_Type()
)
tmnxBundleImaGrpGammaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpGammaValue.setStatus("current")


class _TmnxBundleImaGrpNeClockMode_Type(TmnxImaGrpClockModes):
    """Custom type tmnxBundleImaGrpNeClockMode based on TmnxImaGrpClockModes"""


_TmnxBundleImaGrpNeClockMode_Object = MibTableColumn
tmnxBundleImaGrpNeClockMode = _TmnxBundleImaGrpNeClockMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 26),
    _TmnxBundleImaGrpNeClockMode_Type()
)
tmnxBundleImaGrpNeClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpNeClockMode.setStatus("current")


class _TmnxBundleImaGrpFeClockMode_Type(TmnxImaGrpClockModes):
    """Custom type tmnxBundleImaGrpFeClockMode based on TmnxImaGrpClockModes"""


_TmnxBundleImaGrpFeClockMode_Object = MibTableColumn
tmnxBundleImaGrpFeClockMode = _TmnxBundleImaGrpFeClockMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 27),
    _TmnxBundleImaGrpFeClockMode_Type()
)
tmnxBundleImaGrpFeClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpFeClockMode.setStatus("current")


class _TmnxBundleImaGrpVersion_Type(TmnxImaGrpVersion):
    """Custom type tmnxBundleImaGrpVersion based on TmnxImaGrpVersion"""


_TmnxBundleImaGrpVersion_Object = MibTableColumn
tmnxBundleImaGrpVersion = _TmnxBundleImaGrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 28),
    _TmnxBundleImaGrpVersion_Type()
)
tmnxBundleImaGrpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpVersion.setStatus("current")


class _TmnxBundleImaGrpMaxConfBw_Type(Unsigned32):
    """Custom type tmnxBundleImaGrpMaxConfBw based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxBundleImaGrpMaxConfBw_Type.__name__ = "Unsigned32"
_TmnxBundleImaGrpMaxConfBw_Object = MibTableColumn
tmnxBundleImaGrpMaxConfBw = _TmnxBundleImaGrpMaxConfBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 29),
    _TmnxBundleImaGrpMaxConfBw_Type()
)
tmnxBundleImaGrpMaxConfBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpMaxConfBw.setStatus("current")


class _TmnxBundleImaGrpTestState_Type(TmnxImaTestState):
    """Custom type tmnxBundleImaGrpTestState based on TmnxImaTestState"""


_TmnxBundleImaGrpTestState_Object = MibTableColumn
tmnxBundleImaGrpTestState = _TmnxBundleImaGrpTestState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 30),
    _TmnxBundleImaGrpTestState_Type()
)
tmnxBundleImaGrpTestState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTestState.setStatus("current")


class _TmnxBundleImaGrpTestMember_Type(TmnxPortID):
    """Custom type tmnxBundleImaGrpTestMember based on TmnxPortID"""
    defaultValue = 0


_TmnxBundleImaGrpTestMember_Object = MibTableColumn
tmnxBundleImaGrpTestMember = _TmnxBundleImaGrpTestMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 31),
    _TmnxBundleImaGrpTestMember_Type()
)
tmnxBundleImaGrpTestMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTestMember.setStatus("current")


class _TmnxBundleImaGrpTestPattern_Type(Integer32):
    """Custom type tmnxBundleImaGrpTestPattern based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxBundleImaGrpTestPattern_Type.__name__ = "Integer32"
_TmnxBundleImaGrpTestPattern_Object = MibTableColumn
tmnxBundleImaGrpTestPattern = _TmnxBundleImaGrpTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 32),
    _TmnxBundleImaGrpTestPattern_Type()
)
tmnxBundleImaGrpTestPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpTestPattern.setStatus("current")
_TmnxBundleImaGrpDiffDelayMaxObs_Type = Unsigned32
_TmnxBundleImaGrpDiffDelayMaxObs_Object = MibTableColumn
tmnxBundleImaGrpDiffDelayMaxObs = _TmnxBundleImaGrpDiffDelayMaxObs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 33),
    _TmnxBundleImaGrpDiffDelayMaxObs_Type()
)
tmnxBundleImaGrpDiffDelayMaxObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpDiffDelayMaxObs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpDiffDelayMaxObs.setUnits("milliseconds")
_TmnxBundleImaGrpLeastDelayLink_Type = Unsigned32
_TmnxBundleImaGrpLeastDelayLink_Object = MibTableColumn
tmnxBundleImaGrpLeastDelayLink = _TmnxBundleImaGrpLeastDelayLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 21, 1, 34),
    _TmnxBundleImaGrpLeastDelayLink_Type()
)
tmnxBundleImaGrpLeastDelayLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLeastDelayLink.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleImaGrpLeastDelayLink.setUnits("milliseconds")
_TmnxBundleMemberImaTable_Object = MibTable
tmnxBundleMemberImaTable = _TmnxBundleMemberImaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22)
)
if mibBuilder.loadTexts:
    tmnxBundleMemberImaTable.setStatus("current")
_TmnxBundleMemberImaEntry_Object = MibTableRow
tmnxBundleMemberImaEntry = _TmnxBundleMemberImaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1)
)
tmnxBundleMemberImaEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxBundleMemberImaEntry.setStatus("current")
_TmnxBundleMemberImaNeTxState_Type = TmnxImaLnkState
_TmnxBundleMemberImaNeTxState_Object = MibTableColumn
tmnxBundleMemberImaNeTxState = _TmnxBundleMemberImaNeTxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 1),
    _TmnxBundleMemberImaNeTxState_Type()
)
tmnxBundleMemberImaNeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeTxState.setStatus("current")
_TmnxBundleMemberImaNeRxState_Type = TmnxImaLnkState
_TmnxBundleMemberImaNeRxState_Object = MibTableColumn
tmnxBundleMemberImaNeRxState = _TmnxBundleMemberImaNeRxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 2),
    _TmnxBundleMemberImaNeRxState_Type()
)
tmnxBundleMemberImaNeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeRxState.setStatus("current")
_TmnxBundleMemberImaFeTxState_Type = TmnxImaLnkState
_TmnxBundleMemberImaFeTxState_Object = MibTableColumn
tmnxBundleMemberImaFeTxState = _TmnxBundleMemberImaFeTxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 3),
    _TmnxBundleMemberImaFeTxState_Type()
)
tmnxBundleMemberImaFeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeTxState.setStatus("current")
_TmnxBundleMemberImaFeRxState_Type = TmnxImaLnkState
_TmnxBundleMemberImaFeRxState_Object = MibTableColumn
tmnxBundleMemberImaFeRxState = _TmnxBundleMemberImaFeRxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 4),
    _TmnxBundleMemberImaFeRxState_Type()
)
tmnxBundleMemberImaFeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeRxState.setStatus("current")
_TmnxBundleMemberImaNeRxFailState_Type = TmnxImaLnkFailState
_TmnxBundleMemberImaNeRxFailState_Object = MibTableColumn
tmnxBundleMemberImaNeRxFailState = _TmnxBundleMemberImaNeRxFailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 5),
    _TmnxBundleMemberImaNeRxFailState_Type()
)
tmnxBundleMemberImaNeRxFailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeRxFailState.setStatus("current")
_TmnxBundleMemberImaFeRxFailState_Type = TmnxImaLnkFailState
_TmnxBundleMemberImaFeRxFailState_Object = MibTableColumn
tmnxBundleMemberImaFeRxFailState = _TmnxBundleMemberImaFeRxFailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 6),
    _TmnxBundleMemberImaFeRxFailState_Type()
)
tmnxBundleMemberImaFeRxFailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeRxFailState.setStatus("current")
_TmnxBundleMemberImaTxLid_Type = Integer32
_TmnxBundleMemberImaTxLid_Object = MibTableColumn
tmnxBundleMemberImaTxLid = _TmnxBundleMemberImaTxLid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 7),
    _TmnxBundleMemberImaTxLid_Type()
)
tmnxBundleMemberImaTxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaTxLid.setStatus("current")
_TmnxBundleMemberImaRxLid_Type = Integer32
_TmnxBundleMemberImaRxLid_Object = MibTableColumn
tmnxBundleMemberImaRxLid = _TmnxBundleMemberImaRxLid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 8),
    _TmnxBundleMemberImaRxLid_Type()
)
tmnxBundleMemberImaRxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRxLid.setStatus("current")
_TmnxBundleMemberImaViolations_Type = Counter32
_TmnxBundleMemberImaViolations_Object = MibTableColumn
tmnxBundleMemberImaViolations = _TmnxBundleMemberImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 9),
    _TmnxBundleMemberImaViolations_Type()
)
tmnxBundleMemberImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaViolations.setStatus("current")
_TmnxBundleMemberImaNeSevErrSecs_Type = Counter32
_TmnxBundleMemberImaNeSevErrSecs_Object = MibTableColumn
tmnxBundleMemberImaNeSevErrSecs = _TmnxBundleMemberImaNeSevErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 10),
    _TmnxBundleMemberImaNeSevErrSecs_Type()
)
tmnxBundleMemberImaNeSevErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeSevErrSecs.setStatus("current")
_TmnxBundleMemberImaFeSevErrSecs_Type = Counter32
_TmnxBundleMemberImaFeSevErrSecs_Object = MibTableColumn
tmnxBundleMemberImaFeSevErrSecs = _TmnxBundleMemberImaFeSevErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 11),
    _TmnxBundleMemberImaFeSevErrSecs_Type()
)
tmnxBundleMemberImaFeSevErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeSevErrSecs.setStatus("current")
_TmnxBundleMemberImaNeUnavailSecs_Type = Counter32
_TmnxBundleMemberImaNeUnavailSecs_Object = MibTableColumn
tmnxBundleMemberImaNeUnavailSecs = _TmnxBundleMemberImaNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 12),
    _TmnxBundleMemberImaNeUnavailSecs_Type()
)
tmnxBundleMemberImaNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeUnavailSecs.setStatus("current")
_TmnxBundleMemberImaFeUnavailSecs_Type = Counter32
_TmnxBundleMemberImaFeUnavailSecs_Object = MibTableColumn
tmnxBundleMemberImaFeUnavailSecs = _TmnxBundleMemberImaFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 13),
    _TmnxBundleMemberImaFeUnavailSecs_Type()
)
tmnxBundleMemberImaFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeUnavailSecs.setStatus("current")
_TmnxBundleMemberImaNeTxUnuseSecs_Type = Counter32
_TmnxBundleMemberImaNeTxUnuseSecs_Object = MibTableColumn
tmnxBundleMemberImaNeTxUnuseSecs = _TmnxBundleMemberImaNeTxUnuseSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 14),
    _TmnxBundleMemberImaNeTxUnuseSecs_Type()
)
tmnxBundleMemberImaNeTxUnuseSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeTxUnuseSecs.setStatus("current")
_TmnxBundleMemberImaNeRxUnuseSecs_Type = Counter32
_TmnxBundleMemberImaNeRxUnuseSecs_Object = MibTableColumn
tmnxBundleMemberImaNeRxUnuseSecs = _TmnxBundleMemberImaNeRxUnuseSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 15),
    _TmnxBundleMemberImaNeRxUnuseSecs_Type()
)
tmnxBundleMemberImaNeRxUnuseSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeRxUnuseSecs.setStatus("current")
_TmnxBundleMemberImaFeTxUnuseSecs_Type = Counter32
_TmnxBundleMemberImaFeTxUnuseSecs_Object = MibTableColumn
tmnxBundleMemberImaFeTxUnuseSecs = _TmnxBundleMemberImaFeTxUnuseSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 16),
    _TmnxBundleMemberImaFeTxUnuseSecs_Type()
)
tmnxBundleMemberImaFeTxUnuseSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeTxUnuseSecs.setStatus("current")
_TmnxBundleMemberImaFeRxUnuseSecs_Type = Counter32
_TmnxBundleMemberImaFeRxUnuseSecs_Object = MibTableColumn
tmnxBundleMemberImaFeRxUnuseSecs = _TmnxBundleMemberImaFeRxUnuseSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 17),
    _TmnxBundleMemberImaFeRxUnuseSecs_Type()
)
tmnxBundleMemberImaFeRxUnuseSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeRxUnuseSecs.setStatus("current")
_TmnxBundleMemberImaNeTxNumFails_Type = Counter32
_TmnxBundleMemberImaNeTxNumFails_Object = MibTableColumn
tmnxBundleMemberImaNeTxNumFails = _TmnxBundleMemberImaNeTxNumFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 18),
    _TmnxBundleMemberImaNeTxNumFails_Type()
)
tmnxBundleMemberImaNeTxNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeTxNumFails.setStatus("current")
_TmnxBundleMemberImaNeRxNumFails_Type = Counter32
_TmnxBundleMemberImaNeRxNumFails_Object = MibTableColumn
tmnxBundleMemberImaNeRxNumFails = _TmnxBundleMemberImaNeRxNumFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 19),
    _TmnxBundleMemberImaNeRxNumFails_Type()
)
tmnxBundleMemberImaNeRxNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaNeRxNumFails.setStatus("current")
_TmnxBundleMemberImaFeTxNumFails_Type = Counter32
_TmnxBundleMemberImaFeTxNumFails_Object = MibTableColumn
tmnxBundleMemberImaFeTxNumFails = _TmnxBundleMemberImaFeTxNumFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 20),
    _TmnxBundleMemberImaFeTxNumFails_Type()
)
tmnxBundleMemberImaFeTxNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeTxNumFails.setStatus("current")
_TmnxBundleMemberImaFeRxNumFails_Type = Counter32
_TmnxBundleMemberImaFeRxNumFails_Object = MibTableColumn
tmnxBundleMemberImaFeRxNumFails = _TmnxBundleMemberImaFeRxNumFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 21),
    _TmnxBundleMemberImaFeRxNumFails_Type()
)
tmnxBundleMemberImaFeRxNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaFeRxNumFails.setStatus("current")
_TmnxBundleMemberImaTxIcpCells_Type = Counter32
_TmnxBundleMemberImaTxIcpCells_Object = MibTableColumn
tmnxBundleMemberImaTxIcpCells = _TmnxBundleMemberImaTxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 22),
    _TmnxBundleMemberImaTxIcpCells_Type()
)
tmnxBundleMemberImaTxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaTxIcpCells.setStatus("current")
_TmnxBundleMemberImaRxIcpCells_Type = Counter32
_TmnxBundleMemberImaRxIcpCells_Object = MibTableColumn
tmnxBundleMemberImaRxIcpCells = _TmnxBundleMemberImaRxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 23),
    _TmnxBundleMemberImaRxIcpCells_Type()
)
tmnxBundleMemberImaRxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRxIcpCells.setStatus("current")
_TmnxBundleMemberImaErrorIcpCells_Type = Counter32
_TmnxBundleMemberImaErrorIcpCells_Object = MibTableColumn
tmnxBundleMemberImaErrorIcpCells = _TmnxBundleMemberImaErrorIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 24),
    _TmnxBundleMemberImaErrorIcpCells_Type()
)
tmnxBundleMemberImaErrorIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaErrorIcpCells.setStatus("current")
_TmnxBundleMemberImaLstRxIcpCells_Type = Counter32
_TmnxBundleMemberImaLstRxIcpCells_Object = MibTableColumn
tmnxBundleMemberImaLstRxIcpCells = _TmnxBundleMemberImaLstRxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 25),
    _TmnxBundleMemberImaLstRxIcpCells_Type()
)
tmnxBundleMemberImaLstRxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaLstRxIcpCells.setStatus("current")
_TmnxBundleMemberImaOifAnomalies_Type = Counter32
_TmnxBundleMemberImaOifAnomalies_Object = MibTableColumn
tmnxBundleMemberImaOifAnomalies = _TmnxBundleMemberImaOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 26),
    _TmnxBundleMemberImaOifAnomalies_Type()
)
tmnxBundleMemberImaOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaOifAnomalies.setStatus("current")
_TmnxBundleMemberImaRxTestState_Type = TmnxImaTestState
_TmnxBundleMemberImaRxTestState_Object = MibTableColumn
tmnxBundleMemberImaRxTestState = _TmnxBundleMemberImaRxTestState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 27),
    _TmnxBundleMemberImaRxTestState_Type()
)
tmnxBundleMemberImaRxTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRxTestState.setStatus("current")


class _TmnxBundleMemberImaRxTestPattern_Type(Integer32):
    """Custom type tmnxBundleMemberImaRxTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxBundleMemberImaRxTestPattern_Type.__name__ = "Integer32"
_TmnxBundleMemberImaRxTestPattern_Object = MibTableColumn
tmnxBundleMemberImaRxTestPattern = _TmnxBundleMemberImaRxTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 28),
    _TmnxBundleMemberImaRxTestPattern_Type()
)
tmnxBundleMemberImaRxTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRxTestPattern.setStatus("current")
_TmnxBundleMemberImaRelDelay_Type = Unsigned32
_TmnxBundleMemberImaRelDelay_Object = MibTableColumn
tmnxBundleMemberImaRelDelay = _TmnxBundleMemberImaRelDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 22, 1, 29),
    _TmnxBundleMemberImaRelDelay_Type()
)
tmnxBundleMemberImaRelDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRelDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleMemberImaRelDelay.setUnits("milliseconds")
_TmnxDS1PortTable_Object = MibTable
tmnxDS1PortTable = _TmnxDS1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23)
)
if mibBuilder.loadTexts:
    tmnxDS1PortTable.setStatus("current")
_TmnxDS1PortEntry_Object = MibTableRow
tmnxDS1PortEntry = _TmnxDS1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1)
)
tmnxDS1PortEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDS1PortEntry.setStatus("current")


class _TmnxDS1PortBuildout_Type(Integer32):
    """Custom type tmnxDS1PortBuildout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_TmnxDS1PortBuildout_Type.__name__ = "Integer32"
_TmnxDS1PortBuildout_Object = MibTableColumn
tmnxDS1PortBuildout = _TmnxDS1PortBuildout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 1),
    _TmnxDS1PortBuildout_Type()
)
tmnxDS1PortBuildout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1PortBuildout.setStatus("current")
_TmnxDS1PortLastChangeTime_Type = TimeStamp
_TmnxDS1PortLastChangeTime_Object = MibTableColumn
tmnxDS1PortLastChangeTime = _TmnxDS1PortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 2),
    _TmnxDS1PortLastChangeTime_Type()
)
tmnxDS1PortLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1PortLastChangeTime.setStatus("current")


class _TmnxDS1PortType_Type(Integer32):
    """Custom type tmnxDS1PortType based on Integer32"""
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
        *(("ds1", 1),
          ("e1", 2),
          ("j1", 3))
    )


_TmnxDS1PortType_Type.__name__ = "Integer32"
_TmnxDS1PortType_Object = MibTableColumn
tmnxDS1PortType = _TmnxDS1PortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 3),
    _TmnxDS1PortType_Type()
)
tmnxDS1PortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1PortType.setStatus("current")


class _TmnxDS1PortLineLength_Type(Integer32):
    """Custom type tmnxDS1PortLineLength based on Integer32"""
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
        *(("length0To133", 2),
          ("length134To266", 3),
          ("length267To399", 4),
          ("length400To533", 5),
          ("length534To655", 6),
          ("lengthNotApplicable", 1))
    )


_TmnxDS1PortLineLength_Type.__name__ = "Integer32"
_TmnxDS1PortLineLength_Object = MibTableColumn
tmnxDS1PortLineLength = _TmnxDS1PortLineLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 4),
    _TmnxDS1PortLineLength_Type()
)
tmnxDS1PortLineLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1PortLineLength.setStatus("current")


class _TmnxDS1PortLbo_Type(Integer32):
    """Custom type tmnxDS1PortLbo based on Integer32"""
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
        *(("lbo0dB", 2),
          ("lboNeg15p0dB", 4),
          ("lboNeg22p5dB", 5),
          ("lboNeg7p5dB", 3),
          ("lboNotApplicable", 1))
    )


_TmnxDS1PortLbo_Type.__name__ = "Integer32"
_TmnxDS1PortLbo_Object = MibTableColumn
tmnxDS1PortLbo = _TmnxDS1PortLbo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 5),
    _TmnxDS1PortLbo_Type()
)
tmnxDS1PortLbo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDS1PortLbo.setStatus("current")
_TmnxDS1PortDbGain_Type = Integer32
_TmnxDS1PortDbGain_Object = MibTableColumn
tmnxDS1PortDbGain = _TmnxDS1PortDbGain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 23, 1, 6),
    _TmnxDS1PortDbGain_Type()
)
tmnxDS1PortDbGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDS1PortDbGain.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDS1PortDbGain.setUnits("db")
_TmnxPortSchedOverrideTable_Object = MibTable
tmnxPortSchedOverrideTable = _TmnxPortSchedOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24)
)
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideTable.setStatus("current")
_TmnxPortSchedOverrideEntry_Object = MibTableRow
tmnxPortSchedOverrideEntry = _TmnxPortSchedOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1)
)
tmnxPortSchedOverrideEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideEntry.setStatus("current")
_TmnxPortSchedOverrideRowStatus_Type = RowStatus
_TmnxPortSchedOverrideRowStatus_Object = MibTableColumn
tmnxPortSchedOverrideRowStatus = _TmnxPortSchedOverrideRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 1),
    _TmnxPortSchedOverrideRowStatus_Type()
)
tmnxPortSchedOverrideRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideRowStatus.setStatus("current")
_TmnxPortSchedOverrideSchedName_Type = DisplayString
_TmnxPortSchedOverrideSchedName_Object = MibTableColumn
tmnxPortSchedOverrideSchedName = _TmnxPortSchedOverrideSchedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 2),
    _TmnxPortSchedOverrideSchedName_Type()
)
tmnxPortSchedOverrideSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideSchedName.setStatus("current")
_TmnxPortSchedOverrideLastChanged_Type = TimeStamp
_TmnxPortSchedOverrideLastChanged_Object = MibTableColumn
tmnxPortSchedOverrideLastChanged = _TmnxPortSchedOverrideLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 3),
    _TmnxPortSchedOverrideLastChanged_Type()
)
tmnxPortSchedOverrideLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLastChanged.setStatus("current")


class _TmnxPortSchedOverrideMaxRate_Type(TPortSchedulerPIRRate):
    """Custom type tmnxPortSchedOverrideMaxRate based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TmnxPortSchedOverrideMaxRate_Object = MibTableColumn
tmnxPortSchedOverrideMaxRate = _TmnxPortSchedOverrideMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 4),
    _TmnxPortSchedOverrideMaxRate_Type()
)
tmnxPortSchedOverrideMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideMaxRate.setUnits("kbps")


class _TmnxPortSchedOverrideLvl1PIR_Type(TPortSchedulerPIRRate):
    """Custom type tmnxPortSchedOverrideLvl1PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl1PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl1PIR = _TmnxPortSchedOverrideLvl1PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 5),
    _TmnxPortSchedOverrideLvl1PIR_Type()
)
tmnxPortSchedOverrideLvl1PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl1PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl1PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl1CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl1CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl1CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl1CIR = _TmnxPortSchedOverrideLvl1CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 6),
    _TmnxPortSchedOverrideLvl1CIR_Type()
)
tmnxPortSchedOverrideLvl1CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl1CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl1CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl2PIR_Type(TPortSchedulerPIRRate):
    """Custom type tmnxPortSchedOverrideLvl2PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl2PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl2PIR = _TmnxPortSchedOverrideLvl2PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 7),
    _TmnxPortSchedOverrideLvl2PIR_Type()
)
tmnxPortSchedOverrideLvl2PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl2PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl2PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl2CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl2CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl2CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl2CIR = _TmnxPortSchedOverrideLvl2CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 8),
    _TmnxPortSchedOverrideLvl2CIR_Type()
)
tmnxPortSchedOverrideLvl2CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl2CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl2CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl3PIR_Type(TPortSchedulerPIRRate):
    """Custom type tmnxPortSchedOverrideLvl3PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl3PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl3PIR = _TmnxPortSchedOverrideLvl3PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 9),
    _TmnxPortSchedOverrideLvl3PIR_Type()
)
tmnxPortSchedOverrideLvl3PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl3PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl3PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl3CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl3CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl3CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl3CIR = _TmnxPortSchedOverrideLvl3CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 10),
    _TmnxPortSchedOverrideLvl3CIR_Type()
)
tmnxPortSchedOverrideLvl3CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl3CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl3CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl4PIR_Type(TPortSchedulerPIRRate):
    """Custom type tmnxPortSchedOverrideLvl4PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl4PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl4PIR = _TmnxPortSchedOverrideLvl4PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 11),
    _TmnxPortSchedOverrideLvl4PIR_Type()
)
tmnxPortSchedOverrideLvl4PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl4PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl4PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl4CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl4CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl4CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl4CIR = _TmnxPortSchedOverrideLvl4CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 12),
    _TmnxPortSchedOverrideLvl4CIR_Type()
)
tmnxPortSchedOverrideLvl4CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl4CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl4CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl5PIR_Type(TPortSchedulerPIRRate):
    """Custom type tmnxPortSchedOverrideLvl5PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl5PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl5PIR = _TmnxPortSchedOverrideLvl5PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 13),
    _TmnxPortSchedOverrideLvl5PIR_Type()
)
tmnxPortSchedOverrideLvl5PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl5PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl5PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl5CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl5CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl5CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl5CIR = _TmnxPortSchedOverrideLvl5CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 14),
    _TmnxPortSchedOverrideLvl5CIR_Type()
)
tmnxPortSchedOverrideLvl5CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl5CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl5CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl6PIR_Type(TPortSchedulerPIRRate):
    """Custom type tmnxPortSchedOverrideLvl6PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl6PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl6PIR = _TmnxPortSchedOverrideLvl6PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 15),
    _TmnxPortSchedOverrideLvl6PIR_Type()
)
tmnxPortSchedOverrideLvl6PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl6PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl6PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl6CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl6CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl6CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl6CIR = _TmnxPortSchedOverrideLvl6CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 16),
    _TmnxPortSchedOverrideLvl6CIR_Type()
)
tmnxPortSchedOverrideLvl6CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl6CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl6CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl7PIR_Type(TPortSchedulerPIRRate):
    """Custom type tmnxPortSchedOverrideLvl7PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl7PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl7PIR = _TmnxPortSchedOverrideLvl7PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 17),
    _TmnxPortSchedOverrideLvl7PIR_Type()
)
tmnxPortSchedOverrideLvl7PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl7PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl7PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl7CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl7CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl7CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl7CIR = _TmnxPortSchedOverrideLvl7CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 18),
    _TmnxPortSchedOverrideLvl7CIR_Type()
)
tmnxPortSchedOverrideLvl7CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl7CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl7CIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl8PIR_Type(TPortSchedulerPIRRate):
    """Custom type tmnxPortSchedOverrideLvl8PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl8PIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl8PIR = _TmnxPortSchedOverrideLvl8PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 19),
    _TmnxPortSchedOverrideLvl8PIR_Type()
)
tmnxPortSchedOverrideLvl8PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl8PIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl8PIR.setUnits("kbps")


class _TmnxPortSchedOverrideLvl8CIR_Type(TPortSchedulerCIR):
    """Custom type tmnxPortSchedOverrideLvl8CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TmnxPortSchedOverrideLvl8CIR_Object = MibTableColumn
tmnxPortSchedOverrideLvl8CIR = _TmnxPortSchedOverrideLvl8CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 20),
    _TmnxPortSchedOverrideLvl8CIR_Type()
)
tmnxPortSchedOverrideLvl8CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl8CIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideLvl8CIR.setUnits("kbps")


class _TmnxPortSchedOverrideFlags_Type(Bits):
    """Custom type tmnxPortSchedOverrideFlags based on Bits"""
    namedValues = NamedValues(
        *(("lvl1CIR", 2),
          ("lvl1PIR", 1),
          ("lvl2CIR", 4),
          ("lvl2PIR", 3),
          ("lvl3CIR", 6),
          ("lvl3PIR", 5),
          ("lvl4CIR", 8),
          ("lvl4PIR", 7),
          ("lvl5CIR", 10),
          ("lvl5PIR", 9),
          ("lvl6CIR", 12),
          ("lvl6PIR", 11),
          ("lvl7CIR", 14),
          ("lvl7PIR", 13),
          ("lvl8CIR", 16),
          ("lvl8PIR", 15),
          ("maxRate", 0))
    )

_TmnxPortSchedOverrideFlags_Type.__name__ = "Bits"
_TmnxPortSchedOverrideFlags_Object = MibTableColumn
tmnxPortSchedOverrideFlags = _TmnxPortSchedOverrideFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 24, 1, 21),
    _TmnxPortSchedOverrideFlags_Type()
)
tmnxPortSchedOverrideFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortSchedOverrideFlags.setStatus("current")
_TmnxBPGrpAssocTable_Object = MibTable
tmnxBPGrpAssocTable = _TmnxBPGrpAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 25)
)
if mibBuilder.loadTexts:
    tmnxBPGrpAssocTable.setStatus("current")
_TmnxBPGrpAssocEntry_Object = MibTableRow
tmnxBPGrpAssocEntry = _TmnxBPGrpAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 25, 1)
)
tmnxBPGrpAssocEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
)
if mibBuilder.loadTexts:
    tmnxBPGrpAssocEntry.setStatus("current")
_TmnxBPGrpAssocWorkingBundleID_Type = TmnxBundleID
_TmnxBPGrpAssocWorkingBundleID_Object = MibTableColumn
tmnxBPGrpAssocWorkingBundleID = _TmnxBPGrpAssocWorkingBundleID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 25, 1, 1),
    _TmnxBPGrpAssocWorkingBundleID_Type()
)
tmnxBPGrpAssocWorkingBundleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBPGrpAssocWorkingBundleID.setStatus("current")
_TmnxBPGrpAssocProtectBundleID_Type = TmnxBundleID
_TmnxBPGrpAssocProtectBundleID_Object = MibTableColumn
tmnxBPGrpAssocProtectBundleID = _TmnxBPGrpAssocProtectBundleID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 25, 1, 2),
    _TmnxBPGrpAssocProtectBundleID_Type()
)
tmnxBPGrpAssocProtectBundleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBPGrpAssocProtectBundleID.setStatus("current")
_TmnxBPGrpAssocActiveBundleID_Type = TmnxBundleID
_TmnxBPGrpAssocActiveBundleID_Object = MibTableColumn
tmnxBPGrpAssocActiveBundleID = _TmnxBPGrpAssocActiveBundleID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 25, 1, 3),
    _TmnxBPGrpAssocActiveBundleID_Type()
)
tmnxBPGrpAssocActiveBundleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBPGrpAssocActiveBundleID.setStatus("current")
_TmnxBundleMlpppTable_Object = MibTable
tmnxBundleMlpppTable = _TmnxBundleMlpppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26)
)
if mibBuilder.loadTexts:
    tmnxBundleMlpppTable.setStatus("current")
_TmnxBundleMlpppEntry_Object = MibTableRow
tmnxBundleMlpppEntry = _TmnxBundleMlpppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1)
)
tmnxBundleMlpppEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
)
if mibBuilder.loadTexts:
    tmnxBundleMlpppEntry.setStatus("current")


class _TmnxBundleMlpppEndpointID_Type(OctetString):
    """Custom type tmnxBundleMlpppEndpointID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxBundleMlpppEndpointID_Type.__name__ = "OctetString"
_TmnxBundleMlpppEndpointID_Object = MibTableColumn
tmnxBundleMlpppEndpointID = _TmnxBundleMlpppEndpointID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 1),
    _TmnxBundleMlpppEndpointID_Type()
)
tmnxBundleMlpppEndpointID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppEndpointID.setStatus("current")
_TmnxBundleMlpppEndpointIDClass_Type = TmnxMlpppEndpointIdClass
_TmnxBundleMlpppEndpointIDClass_Object = MibTableColumn
tmnxBundleMlpppEndpointIDClass = _TmnxBundleMlpppEndpointIDClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 2),
    _TmnxBundleMlpppEndpointIDClass_Type()
)
tmnxBundleMlpppEndpointIDClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppEndpointIDClass.setStatus("current")


class _TmnxBundleMlpppClassCount_Type(Integer32):
    """Custom type tmnxBundleMlpppClassCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TmnxBundleMlpppClassCount_Type.__name__ = "Integer32"
_TmnxBundleMlpppClassCount_Object = MibTableColumn
tmnxBundleMlpppClassCount = _TmnxBundleMlpppClassCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 3),
    _TmnxBundleMlpppClassCount_Type()
)
tmnxBundleMlpppClassCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppClassCount.setStatus("current")


class _TmnxBundleMlpppIngQoSProfId_Type(TMlpppQoSProfileId):
    """Custom type tmnxBundleMlpppIngQoSProfId based on TMlpppQoSProfileId"""
    defaultValue = 0


_TmnxBundleMlpppIngQoSProfId_Object = MibTableColumn
tmnxBundleMlpppIngQoSProfId = _TmnxBundleMlpppIngQoSProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 4),
    _TmnxBundleMlpppIngQoSProfId_Type()
)
tmnxBundleMlpppIngQoSProfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppIngQoSProfId.setStatus("current")


class _TmnxBundleMlpppEgrQoSProfId_Type(TMlpppQoSProfileId):
    """Custom type tmnxBundleMlpppEgrQoSProfId based on TMlpppQoSProfileId"""
    defaultValue = 0


_TmnxBundleMlpppEgrQoSProfId_Object = MibTableColumn
tmnxBundleMlpppEgrQoSProfId = _TmnxBundleMlpppEgrQoSProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 5),
    _TmnxBundleMlpppEgrQoSProfId_Type()
)
tmnxBundleMlpppEgrQoSProfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppEgrQoSProfId.setStatus("current")


class _TmnxBundleMlpppMagicNumber_Type(TmnxEnabledDisabled):
    """Custom type tmnxBundleMlpppMagicNumber based on TmnxEnabledDisabled"""


_TmnxBundleMlpppMagicNumber_Object = MibTableColumn
tmnxBundleMlpppMagicNumber = _TmnxBundleMlpppMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 6),
    _TmnxBundleMlpppMagicNumber_Type()
)
tmnxBundleMlpppMagicNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppMagicNumber.setStatus("current")


class _TmnxBundleMlpppStatelessApsSwo_Type(TmnxEnabledDisabled):
    """Custom type tmnxBundleMlpppStatelessApsSwo based on TmnxEnabledDisabled"""


_TmnxBundleMlpppStatelessApsSwo_Object = MibTableColumn
tmnxBundleMlpppStatelessApsSwo = _TmnxBundleMlpppStatelessApsSwo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 26, 1, 7),
    _TmnxBundleMlpppStatelessApsSwo_Type()
)
tmnxBundleMlpppStatelessApsSwo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlpppStatelessApsSwo.setStatus("current")
_TmnxHsmdaPortSchOvrTblLastChngd_Type = TimeStamp
_TmnxHsmdaPortSchOvrTblLastChngd_Object = MibScalar
tmnxHsmdaPortSchOvrTblLastChngd = _TmnxHsmdaPortSchOvrTblLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 27),
    _TmnxHsmdaPortSchOvrTblLastChngd_Type()
)
tmnxHsmdaPortSchOvrTblLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrTblLastChngd.setStatus("current")
_TmnxHsmdaPortSchOvrTable_Object = MibTable
tmnxHsmdaPortSchOvrTable = _TmnxHsmdaPortSchOvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28)
)
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrTable.setStatus("current")
_TmnxHsmdaPortSchOvrEntry_Object = MibTableRow
tmnxHsmdaPortSchOvrEntry = _TmnxHsmdaPortSchOvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1)
)
tmnxHsmdaPortSchOvrEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrEntry.setStatus("current")
_TmnxHsmdaPortSchOvrRowStatus_Type = RowStatus
_TmnxHsmdaPortSchOvrRowStatus_Object = MibTableColumn
tmnxHsmdaPortSchOvrRowStatus = _TmnxHsmdaPortSchOvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 1),
    _TmnxHsmdaPortSchOvrRowStatus_Type()
)
tmnxHsmdaPortSchOvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrRowStatus.setStatus("current")
_TmnxHsmdaPortSchOvrLastChanged_Type = TimeStamp
_TmnxHsmdaPortSchOvrLastChanged_Object = MibTableColumn
tmnxHsmdaPortSchOvrLastChanged = _TmnxHsmdaPortSchOvrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 2),
    _TmnxHsmdaPortSchOvrLastChanged_Type()
)
tmnxHsmdaPortSchOvrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrLastChanged.setStatus("current")


class _TmnxHsmdaPortSchOvrMaxRate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaPortSchOvrMaxRate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrMaxRate_Object = MibTableColumn
tmnxHsmdaPortSchOvrMaxRate = _TmnxHsmdaPortSchOvrMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 3),
    _TmnxHsmdaPortSchOvrMaxRate_Type()
)
tmnxHsmdaPortSchOvrMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrMaxRate.setUnits("Mbps")


class _TmnxHsmdaPortSchOvrGrp1Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaPortSchOvrGrp1Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrGrp1Rate_Object = MibTableColumn
tmnxHsmdaPortSchOvrGrp1Rate = _TmnxHsmdaPortSchOvrGrp1Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 4),
    _TmnxHsmdaPortSchOvrGrp1Rate_Type()
)
tmnxHsmdaPortSchOvrGrp1Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrGrp1Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrGrp1Rate.setUnits("Mbps")


class _TmnxHsmdaPortSchOvrGrp2Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaPortSchOvrGrp2Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrGrp2Rate_Object = MibTableColumn
tmnxHsmdaPortSchOvrGrp2Rate = _TmnxHsmdaPortSchOvrGrp2Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 5),
    _TmnxHsmdaPortSchOvrGrp2Rate_Type()
)
tmnxHsmdaPortSchOvrGrp2Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrGrp2Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrGrp2Rate.setUnits("Mbps")


class _TmnxHsmdaPortSchOvrClass1Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaPortSchOvrClass1Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass1Rate_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass1Rate = _TmnxHsmdaPortSchOvrClass1Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 6),
    _TmnxHsmdaPortSchOvrClass1Rate_Type()
)
tmnxHsmdaPortSchOvrClass1Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass1Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass1Rate.setUnits("Mbps")


class _TmnxHsmdaPortSchOvrClass1WtInGp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaPortSchOvrClass1WtInGp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass1WtInGp_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass1WtInGp = _TmnxHsmdaPortSchOvrClass1WtInGp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 7),
    _TmnxHsmdaPortSchOvrClass1WtInGp_Type()
)
tmnxHsmdaPortSchOvrClass1WtInGp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass1WtInGp.setStatus("current")


class _TmnxHsmdaPortSchOvrClass2Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaPortSchOvrClass2Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass2Rate_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass2Rate = _TmnxHsmdaPortSchOvrClass2Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 8),
    _TmnxHsmdaPortSchOvrClass2Rate_Type()
)
tmnxHsmdaPortSchOvrClass2Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass2Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass2Rate.setUnits("Mbps")


class _TmnxHsmdaPortSchOvrClass2WtInGp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaPortSchOvrClass2WtInGp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass2WtInGp_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass2WtInGp = _TmnxHsmdaPortSchOvrClass2WtInGp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 9),
    _TmnxHsmdaPortSchOvrClass2WtInGp_Type()
)
tmnxHsmdaPortSchOvrClass2WtInGp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass2WtInGp.setStatus("current")


class _TmnxHsmdaPortSchOvrClass3Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaPortSchOvrClass3Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass3Rate_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass3Rate = _TmnxHsmdaPortSchOvrClass3Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 10),
    _TmnxHsmdaPortSchOvrClass3Rate_Type()
)
tmnxHsmdaPortSchOvrClass3Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass3Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass3Rate.setUnits("Mbps")


class _TmnxHsmdaPortSchOvrClass3WtInGp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaPortSchOvrClass3WtInGp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass3WtInGp_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass3WtInGp = _TmnxHsmdaPortSchOvrClass3WtInGp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 11),
    _TmnxHsmdaPortSchOvrClass3WtInGp_Type()
)
tmnxHsmdaPortSchOvrClass3WtInGp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass3WtInGp.setStatus("current")


class _TmnxHsmdaPortSchOvrClass4Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaPortSchOvrClass4Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass4Rate_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass4Rate = _TmnxHsmdaPortSchOvrClass4Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 12),
    _TmnxHsmdaPortSchOvrClass4Rate_Type()
)
tmnxHsmdaPortSchOvrClass4Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass4Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass4Rate.setUnits("Mbps")


class _TmnxHsmdaPortSchOvrClass4WtInGp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaPortSchOvrClass4WtInGp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass4WtInGp_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass4WtInGp = _TmnxHsmdaPortSchOvrClass4WtInGp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 13),
    _TmnxHsmdaPortSchOvrClass4WtInGp_Type()
)
tmnxHsmdaPortSchOvrClass4WtInGp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass4WtInGp.setStatus("current")


class _TmnxHsmdaPortSchOvrClass5Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaPortSchOvrClass5Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass5Rate_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass5Rate = _TmnxHsmdaPortSchOvrClass5Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 14),
    _TmnxHsmdaPortSchOvrClass5Rate_Type()
)
tmnxHsmdaPortSchOvrClass5Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass5Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass5Rate.setUnits("Mbps")


class _TmnxHsmdaPortSchOvrClass5WtInGp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaPortSchOvrClass5WtInGp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass5WtInGp_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass5WtInGp = _TmnxHsmdaPortSchOvrClass5WtInGp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 15),
    _TmnxHsmdaPortSchOvrClass5WtInGp_Type()
)
tmnxHsmdaPortSchOvrClass5WtInGp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass5WtInGp.setStatus("current")


class _TmnxHsmdaPortSchOvrClass6Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaPortSchOvrClass6Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass6Rate_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass6Rate = _TmnxHsmdaPortSchOvrClass6Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 16),
    _TmnxHsmdaPortSchOvrClass6Rate_Type()
)
tmnxHsmdaPortSchOvrClass6Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass6Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass6Rate.setUnits("Mbps")


class _TmnxHsmdaPortSchOvrClass6WtInGp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaPortSchOvrClass6WtInGp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass6WtInGp_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass6WtInGp = _TmnxHsmdaPortSchOvrClass6WtInGp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 17),
    _TmnxHsmdaPortSchOvrClass6WtInGp_Type()
)
tmnxHsmdaPortSchOvrClass6WtInGp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass6WtInGp.setStatus("current")


class _TmnxHsmdaPortSchOvrClass7Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaPortSchOvrClass7Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass7Rate_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass7Rate = _TmnxHsmdaPortSchOvrClass7Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 18),
    _TmnxHsmdaPortSchOvrClass7Rate_Type()
)
tmnxHsmdaPortSchOvrClass7Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass7Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass7Rate.setUnits("Mbps")


class _TmnxHsmdaPortSchOvrClass7WtInGp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaPortSchOvrClass7WtInGp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass7WtInGp_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass7WtInGp = _TmnxHsmdaPortSchOvrClass7WtInGp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 19),
    _TmnxHsmdaPortSchOvrClass7WtInGp_Type()
)
tmnxHsmdaPortSchOvrClass7WtInGp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass7WtInGp.setStatus("current")


class _TmnxHsmdaPortSchOvrClass8Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaPortSchOvrClass8Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass8Rate_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass8Rate = _TmnxHsmdaPortSchOvrClass8Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 20),
    _TmnxHsmdaPortSchOvrClass8Rate_Type()
)
tmnxHsmdaPortSchOvrClass8Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass8Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass8Rate.setUnits("Mbps")


class _TmnxHsmdaPortSchOvrClass8WtInGp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaPortSchOvrClass8WtInGp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaPortSchOvrClass8WtInGp_Object = MibTableColumn
tmnxHsmdaPortSchOvrClass8WtInGp = _TmnxHsmdaPortSchOvrClass8WtInGp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 28, 1, 21),
    _TmnxHsmdaPortSchOvrClass8WtInGp_Type()
)
tmnxHsmdaPortSchOvrClass8WtInGp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaPortSchOvrClass8WtInGp.setStatus("current")
_TmnxPortEgrShaperTblLastChanged_Type = TimeStamp
_TmnxPortEgrShaperTblLastChanged_Object = MibScalar
tmnxPortEgrShaperTblLastChanged = _TmnxPortEgrShaperTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 29),
    _TmnxPortEgrShaperTblLastChanged_Type()
)
tmnxPortEgrShaperTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrShaperTblLastChanged.setStatus("obsolete")
_TmnxPortEgrShaperTable_Object = MibTable
tmnxPortEgrShaperTable = _TmnxPortEgrShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 30)
)
if mibBuilder.loadTexts:
    tmnxPortEgrShaperTable.setStatus("obsolete")
_TmnxPortEgrShaperEntry_Object = MibTableRow
tmnxPortEgrShaperEntry = _TmnxPortEgrShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 30, 1)
)
tmnxPortEgrShaperEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortEgrShaperName"),
)
if mibBuilder.loadTexts:
    tmnxPortEgrShaperEntry.setStatus("obsolete")
_TmnxPortEgrShaperName_Type = TNamedItem
_TmnxPortEgrShaperName_Object = MibTableColumn
tmnxPortEgrShaperName = _TmnxPortEgrShaperName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 30, 1, 1),
    _TmnxPortEgrShaperName_Type()
)
tmnxPortEgrShaperName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortEgrShaperName.setStatus("obsolete")
_TmnxPortEgrShaperRowStatus_Type = RowStatus
_TmnxPortEgrShaperRowStatus_Object = MibTableColumn
tmnxPortEgrShaperRowStatus = _TmnxPortEgrShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 30, 1, 2),
    _TmnxPortEgrShaperRowStatus_Type()
)
tmnxPortEgrShaperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrShaperRowStatus.setStatus("obsolete")
_TmnxPortEgrShaperLastChanged_Type = TimeStamp
_TmnxPortEgrShaperLastChanged_Object = MibTableColumn
tmnxPortEgrShaperLastChanged = _TmnxPortEgrShaperLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 30, 1, 3),
    _TmnxPortEgrShaperLastChanged_Type()
)
tmnxPortEgrShaperLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrShaperLastChanged.setStatus("obsolete")


class _TmnxPortEgrShaperRate_Type(TSecondaryShaper10GPIRRate):
    """Custom type tmnxPortEgrShaperRate based on TSecondaryShaper10GPIRRate"""
    defaultValue = -1


_TmnxPortEgrShaperRate_Object = MibTableColumn
tmnxPortEgrShaperRate = _TmnxPortEgrShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 30, 1, 4),
    _TmnxPortEgrShaperRate_Type()
)
tmnxPortEgrShaperRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrShaperRate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxPortEgrShaperRate.setUnits("Mbps")
_TmnxDigitalDiagMonitorTable_Object = MibTable
tmnxDigitalDiagMonitorTable = _TmnxDigitalDiagMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31)
)
if mibBuilder.loadTexts:
    tmnxDigitalDiagMonitorTable.setStatus("current")
_TmnxDigitalDiagMonitorEntry_Object = MibTableRow
tmnxDigitalDiagMonitorEntry = _TmnxDigitalDiagMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1)
)
tmnxDigitalDiagMonitorEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxDigitalDiagMonitorEntry.setStatus("current")
_TmnxDDMTemperature_Type = Integer32
_TmnxDDMTemperature_Object = MibTableColumn
tmnxDDMTemperature = _TmnxDDMTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 1),
    _TmnxDDMTemperature_Type()
)
tmnxDDMTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTemperature.setStatus("current")
_TmnxDDMTempLowWarning_Type = Integer32
_TmnxDDMTempLowWarning_Object = MibTableColumn
tmnxDDMTempLowWarning = _TmnxDDMTempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 2),
    _TmnxDDMTempLowWarning_Type()
)
tmnxDDMTempLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTempLowWarning.setStatus("current")
_TmnxDDMTempLowAlarm_Type = Integer32
_TmnxDDMTempLowAlarm_Object = MibTableColumn
tmnxDDMTempLowAlarm = _TmnxDDMTempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 3),
    _TmnxDDMTempLowAlarm_Type()
)
tmnxDDMTempLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTempLowAlarm.setStatus("current")
_TmnxDDMTempHiWarning_Type = Integer32
_TmnxDDMTempHiWarning_Object = MibTableColumn
tmnxDDMTempHiWarning = _TmnxDDMTempHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 4),
    _TmnxDDMTempHiWarning_Type()
)
tmnxDDMTempHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTempHiWarning.setStatus("current")
_TmnxDDMTempHiAlarm_Type = Integer32
_TmnxDDMTempHiAlarm_Object = MibTableColumn
tmnxDDMTempHiAlarm = _TmnxDDMTempHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 5),
    _TmnxDDMTempHiAlarm_Type()
)
tmnxDDMTempHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTempHiAlarm.setStatus("current")
_TmnxDDMSupplyVoltage_Type = Integer32
_TmnxDDMSupplyVoltage_Object = MibTableColumn
tmnxDDMSupplyVoltage = _TmnxDDMSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 6),
    _TmnxDDMSupplyVoltage_Type()
)
tmnxDDMSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMSupplyVoltage.setStatus("current")
_TmnxDDMSupplyVoltageLowWarning_Type = Integer32
_TmnxDDMSupplyVoltageLowWarning_Object = MibTableColumn
tmnxDDMSupplyVoltageLowWarning = _TmnxDDMSupplyVoltageLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 7),
    _TmnxDDMSupplyVoltageLowWarning_Type()
)
tmnxDDMSupplyVoltageLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMSupplyVoltageLowWarning.setStatus("current")
_TmnxDDMSupplyVoltageLowAlarm_Type = Integer32
_TmnxDDMSupplyVoltageLowAlarm_Object = MibTableColumn
tmnxDDMSupplyVoltageLowAlarm = _TmnxDDMSupplyVoltageLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 8),
    _TmnxDDMSupplyVoltageLowAlarm_Type()
)
tmnxDDMSupplyVoltageLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMSupplyVoltageLowAlarm.setStatus("current")
_TmnxDDMSupplyVoltageHiWarning_Type = Integer32
_TmnxDDMSupplyVoltageHiWarning_Object = MibTableColumn
tmnxDDMSupplyVoltageHiWarning = _TmnxDDMSupplyVoltageHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 9),
    _TmnxDDMSupplyVoltageHiWarning_Type()
)
tmnxDDMSupplyVoltageHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMSupplyVoltageHiWarning.setStatus("current")
_TmnxDDMSupplyVoltageHiAlarm_Type = Integer32
_TmnxDDMSupplyVoltageHiAlarm_Object = MibTableColumn
tmnxDDMSupplyVoltageHiAlarm = _TmnxDDMSupplyVoltageHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 10),
    _TmnxDDMSupplyVoltageHiAlarm_Type()
)
tmnxDDMSupplyVoltageHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMSupplyVoltageHiAlarm.setStatus("current")
_TmnxDDMTxBiasCurrent_Type = Integer32
_TmnxDDMTxBiasCurrent_Object = MibTableColumn
tmnxDDMTxBiasCurrent = _TmnxDDMTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 11),
    _TmnxDDMTxBiasCurrent_Type()
)
tmnxDDMTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxBiasCurrent.setStatus("current")
_TmnxDDMTxBiasCurrentLowWarning_Type = Integer32
_TmnxDDMTxBiasCurrentLowWarning_Object = MibTableColumn
tmnxDDMTxBiasCurrentLowWarning = _TmnxDDMTxBiasCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 12),
    _TmnxDDMTxBiasCurrentLowWarning_Type()
)
tmnxDDMTxBiasCurrentLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxBiasCurrentLowWarning.setStatus("current")
_TmnxDDMTxBiasCurrentLowAlarm_Type = Integer32
_TmnxDDMTxBiasCurrentLowAlarm_Object = MibTableColumn
tmnxDDMTxBiasCurrentLowAlarm = _TmnxDDMTxBiasCurrentLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 13),
    _TmnxDDMTxBiasCurrentLowAlarm_Type()
)
tmnxDDMTxBiasCurrentLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxBiasCurrentLowAlarm.setStatus("current")
_TmnxDDMTxBiasCurrentHiWarning_Type = Integer32
_TmnxDDMTxBiasCurrentHiWarning_Object = MibTableColumn
tmnxDDMTxBiasCurrentHiWarning = _TmnxDDMTxBiasCurrentHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 14),
    _TmnxDDMTxBiasCurrentHiWarning_Type()
)
tmnxDDMTxBiasCurrentHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxBiasCurrentHiWarning.setStatus("current")
_TmnxDDMTxBiasCurrentHiAlarm_Type = Integer32
_TmnxDDMTxBiasCurrentHiAlarm_Object = MibTableColumn
tmnxDDMTxBiasCurrentHiAlarm = _TmnxDDMTxBiasCurrentHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 15),
    _TmnxDDMTxBiasCurrentHiAlarm_Type()
)
tmnxDDMTxBiasCurrentHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxBiasCurrentHiAlarm.setStatus("current")
_TmnxDDMTxOutputPower_Type = Integer32
_TmnxDDMTxOutputPower_Object = MibTableColumn
tmnxDDMTxOutputPower = _TmnxDDMTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 16),
    _TmnxDDMTxOutputPower_Type()
)
tmnxDDMTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxOutputPower.setStatus("current")
_TmnxDDMTxOutputPowerLowWarning_Type = Integer32
_TmnxDDMTxOutputPowerLowWarning_Object = MibTableColumn
tmnxDDMTxOutputPowerLowWarning = _TmnxDDMTxOutputPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 17),
    _TmnxDDMTxOutputPowerLowWarning_Type()
)
tmnxDDMTxOutputPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxOutputPowerLowWarning.setStatus("current")
_TmnxDDMTxOutputPowerLowAlarm_Type = Integer32
_TmnxDDMTxOutputPowerLowAlarm_Object = MibTableColumn
tmnxDDMTxOutputPowerLowAlarm = _TmnxDDMTxOutputPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 18),
    _TmnxDDMTxOutputPowerLowAlarm_Type()
)
tmnxDDMTxOutputPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxOutputPowerLowAlarm.setStatus("current")
_TmnxDDMTxOutputPowerHiWarning_Type = Integer32
_TmnxDDMTxOutputPowerHiWarning_Object = MibTableColumn
tmnxDDMTxOutputPowerHiWarning = _TmnxDDMTxOutputPowerHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 19),
    _TmnxDDMTxOutputPowerHiWarning_Type()
)
tmnxDDMTxOutputPowerHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxOutputPowerHiWarning.setStatus("current")
_TmnxDDMTxOutputPowerHiAlarm_Type = Integer32
_TmnxDDMTxOutputPowerHiAlarm_Object = MibTableColumn
tmnxDDMTxOutputPowerHiAlarm = _TmnxDDMTxOutputPowerHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 20),
    _TmnxDDMTxOutputPowerHiAlarm_Type()
)
tmnxDDMTxOutputPowerHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMTxOutputPowerHiAlarm.setStatus("current")
_TmnxDDMRxOpticalPower_Type = Integer32
_TmnxDDMRxOpticalPower_Object = MibTableColumn
tmnxDDMRxOpticalPower = _TmnxDDMRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 21),
    _TmnxDDMRxOpticalPower_Type()
)
tmnxDDMRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPower.setStatus("current")
_TmnxDDMRxOpticalPowerLowWarning_Type = Integer32
_TmnxDDMRxOpticalPowerLowWarning_Object = MibTableColumn
tmnxDDMRxOpticalPowerLowWarning = _TmnxDDMRxOpticalPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 22),
    _TmnxDDMRxOpticalPowerLowWarning_Type()
)
tmnxDDMRxOpticalPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPowerLowWarning.setStatus("current")
_TmnxDDMRxOpticalPowerLowAlarm_Type = Integer32
_TmnxDDMRxOpticalPowerLowAlarm_Object = MibTableColumn
tmnxDDMRxOpticalPowerLowAlarm = _TmnxDDMRxOpticalPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 23),
    _TmnxDDMRxOpticalPowerLowAlarm_Type()
)
tmnxDDMRxOpticalPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPowerLowAlarm.setStatus("current")
_TmnxDDMRxOpticalPowerHiWarning_Type = Integer32
_TmnxDDMRxOpticalPowerHiWarning_Object = MibTableColumn
tmnxDDMRxOpticalPowerHiWarning = _TmnxDDMRxOpticalPowerHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 24),
    _TmnxDDMRxOpticalPowerHiWarning_Type()
)
tmnxDDMRxOpticalPowerHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPowerHiWarning.setStatus("current")
_TmnxDDMRxOpticalPowerHiAlarm_Type = Integer32
_TmnxDDMRxOpticalPowerHiAlarm_Object = MibTableColumn
tmnxDDMRxOpticalPowerHiAlarm = _TmnxDDMRxOpticalPowerHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 25),
    _TmnxDDMRxOpticalPowerHiAlarm_Type()
)
tmnxDDMRxOpticalPowerHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPowerHiAlarm.setStatus("current")


class _TmnxDDMRxOpticalPowerType_Type(Integer32):
    """Custom type tmnxDDMRxOpticalPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("average", 1),
          ("oma", 0))
    )


_TmnxDDMRxOpticalPowerType_Type.__name__ = "Integer32"
_TmnxDDMRxOpticalPowerType_Object = MibTableColumn
tmnxDDMRxOpticalPowerType = _TmnxDDMRxOpticalPowerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 26),
    _TmnxDDMRxOpticalPowerType_Type()
)
tmnxDDMRxOpticalPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMRxOpticalPowerType.setStatus("current")
_TmnxDDMAux1_Type = Integer32
_TmnxDDMAux1_Object = MibTableColumn
tmnxDDMAux1 = _TmnxDDMAux1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 27),
    _TmnxDDMAux1_Type()
)
tmnxDDMAux1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1.setStatus("current")
_TmnxDDMAux1LowWarning_Type = Integer32
_TmnxDDMAux1LowWarning_Object = MibTableColumn
tmnxDDMAux1LowWarning = _TmnxDDMAux1LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 28),
    _TmnxDDMAux1LowWarning_Type()
)
tmnxDDMAux1LowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1LowWarning.setStatus("current")
_TmnxDDMAux1LowAlarm_Type = Integer32
_TmnxDDMAux1LowAlarm_Object = MibTableColumn
tmnxDDMAux1LowAlarm = _TmnxDDMAux1LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 29),
    _TmnxDDMAux1LowAlarm_Type()
)
tmnxDDMAux1LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1LowAlarm.setStatus("current")
_TmnxDDMAux1HiWarning_Type = Integer32
_TmnxDDMAux1HiWarning_Object = MibTableColumn
tmnxDDMAux1HiWarning = _TmnxDDMAux1HiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 30),
    _TmnxDDMAux1HiWarning_Type()
)
tmnxDDMAux1HiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1HiWarning.setStatus("current")
_TmnxDDMAux1HiAlarm_Type = Integer32
_TmnxDDMAux1HiAlarm_Object = MibTableColumn
tmnxDDMAux1HiAlarm = _TmnxDDMAux1HiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 31),
    _TmnxDDMAux1HiAlarm_Type()
)
tmnxDDMAux1HiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1HiAlarm.setStatus("current")


class _TmnxDDMAux1Type_Type(Integer32):
    """Custom type tmnxDDMAux1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("adp-bias-voltage", 1),
          ("current-18", 14),
          ("current-33", 13),
          ("current-50", 10),
          ("current-52", 15),
          ("laser-temp", 4),
          ("laser-wavelength", 5),
          ("none", 0),
          ("reserved-11", 11),
          ("reserved-12", 12),
          ("reserved-2", 2),
          ("tec-current", 3),
          ("voltage-18", 8),
          ("voltage-33", 7),
          ("voltage-50", 6),
          ("voltage-52", 9))
    )


_TmnxDDMAux1Type_Type.__name__ = "Integer32"
_TmnxDDMAux1Type_Object = MibTableColumn
tmnxDDMAux1Type = _TmnxDDMAux1Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 32),
    _TmnxDDMAux1Type_Type()
)
tmnxDDMAux1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux1Type.setStatus("current")
_TmnxDDMAux2_Type = Integer32
_TmnxDDMAux2_Object = MibTableColumn
tmnxDDMAux2 = _TmnxDDMAux2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 33),
    _TmnxDDMAux2_Type()
)
tmnxDDMAux2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2.setStatus("current")
_TmnxDDMAux2LowWarning_Type = Integer32
_TmnxDDMAux2LowWarning_Object = MibTableColumn
tmnxDDMAux2LowWarning = _TmnxDDMAux2LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 34),
    _TmnxDDMAux2LowWarning_Type()
)
tmnxDDMAux2LowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2LowWarning.setStatus("current")
_TmnxDDMAux2LowAlarm_Type = Integer32
_TmnxDDMAux2LowAlarm_Object = MibTableColumn
tmnxDDMAux2LowAlarm = _TmnxDDMAux2LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 35),
    _TmnxDDMAux2LowAlarm_Type()
)
tmnxDDMAux2LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2LowAlarm.setStatus("current")
_TmnxDDMAux2HiWarning_Type = Integer32
_TmnxDDMAux2HiWarning_Object = MibTableColumn
tmnxDDMAux2HiWarning = _TmnxDDMAux2HiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 36),
    _TmnxDDMAux2HiWarning_Type()
)
tmnxDDMAux2HiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2HiWarning.setStatus("current")
_TmnxDDMAux2HiAlarm_Type = Integer32
_TmnxDDMAux2HiAlarm_Object = MibTableColumn
tmnxDDMAux2HiAlarm = _TmnxDDMAux2HiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 37),
    _TmnxDDMAux2HiAlarm_Type()
)
tmnxDDMAux2HiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2HiAlarm.setStatus("current")


class _TmnxDDMAux2Type_Type(Integer32):
    """Custom type tmnxDDMAux2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("adp-bias-voltage", 1),
          ("current-18", 14),
          ("current-33", 13),
          ("current-50", 10),
          ("current-52", 15),
          ("laser-temp", 4),
          ("laser-wavelength", 5),
          ("none", 0),
          ("reserved-11", 11),
          ("reserved-12", 12),
          ("reserved-2", 2),
          ("tec-current", 3),
          ("voltage-18", 8),
          ("voltage-33", 7),
          ("voltage-50", 6),
          ("voltage-52", 9))
    )


_TmnxDDMAux2Type_Type.__name__ = "Integer32"
_TmnxDDMAux2Type_Object = MibTableColumn
tmnxDDMAux2Type = _TmnxDDMAux2Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 38),
    _TmnxDDMAux2Type_Type()
)
tmnxDDMAux2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMAux2Type.setStatus("current")
_TmnxDDMFailedThresholds_Type = TmnxDigitalDiagnosticFailureBits
_TmnxDDMFailedThresholds_Object = MibTableColumn
tmnxDDMFailedThresholds = _TmnxDDMFailedThresholds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 39),
    _TmnxDDMFailedThresholds_Type()
)
tmnxDDMFailedThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMFailedThresholds.setStatus("current")
_TmnxDDMExternallyCalibrated_Type = TruthValue
_TmnxDDMExternallyCalibrated_Object = MibTableColumn
tmnxDDMExternallyCalibrated = _TmnxDDMExternallyCalibrated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 40),
    _TmnxDDMExternallyCalibrated_Type()
)
tmnxDDMExternallyCalibrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExternallyCalibrated.setStatus("current")
_TmnxDDMExtCalRxPower4_Type = Unsigned32
_TmnxDDMExtCalRxPower4_Object = MibTableColumn
tmnxDDMExtCalRxPower4 = _TmnxDDMExtCalRxPower4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 41),
    _TmnxDDMExtCalRxPower4_Type()
)
tmnxDDMExtCalRxPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalRxPower4.setStatus("current")
_TmnxDDMExtCalRxPower3_Type = Unsigned32
_TmnxDDMExtCalRxPower3_Object = MibTableColumn
tmnxDDMExtCalRxPower3 = _TmnxDDMExtCalRxPower3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 42),
    _TmnxDDMExtCalRxPower3_Type()
)
tmnxDDMExtCalRxPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalRxPower3.setStatus("current")
_TmnxDDMExtCalRxPower2_Type = Unsigned32
_TmnxDDMExtCalRxPower2_Object = MibTableColumn
tmnxDDMExtCalRxPower2 = _TmnxDDMExtCalRxPower2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 43),
    _TmnxDDMExtCalRxPower2_Type()
)
tmnxDDMExtCalRxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalRxPower2.setStatus("current")
_TmnxDDMExtCalRxPower1_Type = Unsigned32
_TmnxDDMExtCalRxPower1_Object = MibTableColumn
tmnxDDMExtCalRxPower1 = _TmnxDDMExtCalRxPower1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 44),
    _TmnxDDMExtCalRxPower1_Type()
)
tmnxDDMExtCalRxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalRxPower1.setStatus("current")
_TmnxDDMExtCalRxPower0_Type = Unsigned32
_TmnxDDMExtCalRxPower0_Object = MibTableColumn
tmnxDDMExtCalRxPower0 = _TmnxDDMExtCalRxPower0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 45),
    _TmnxDDMExtCalRxPower0_Type()
)
tmnxDDMExtCalRxPower0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalRxPower0.setStatus("current")


class _TmnxDDMExtCalTxLaserBiasSlope_Type(Unsigned32):
    """Custom type tmnxDDMExtCalTxLaserBiasSlope based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxDDMExtCalTxLaserBiasSlope_Type.__name__ = "Unsigned32"
_TmnxDDMExtCalTxLaserBiasSlope_Object = MibTableColumn
tmnxDDMExtCalTxLaserBiasSlope = _TmnxDDMExtCalTxLaserBiasSlope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 46),
    _TmnxDDMExtCalTxLaserBiasSlope_Type()
)
tmnxDDMExtCalTxLaserBiasSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTxLaserBiasSlope.setStatus("current")


class _TmnxDDMExtCalTxLaserBiasOffset_Type(Integer32):
    """Custom type tmnxDDMExtCalTxLaserBiasOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TmnxDDMExtCalTxLaserBiasOffset_Type.__name__ = "Integer32"
_TmnxDDMExtCalTxLaserBiasOffset_Object = MibTableColumn
tmnxDDMExtCalTxLaserBiasOffset = _TmnxDDMExtCalTxLaserBiasOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 47),
    _TmnxDDMExtCalTxLaserBiasOffset_Type()
)
tmnxDDMExtCalTxLaserBiasOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTxLaserBiasOffset.setStatus("current")


class _TmnxDDMExtCalTxPowerSlope_Type(Unsigned32):
    """Custom type tmnxDDMExtCalTxPowerSlope based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxDDMExtCalTxPowerSlope_Type.__name__ = "Unsigned32"
_TmnxDDMExtCalTxPowerSlope_Object = MibTableColumn
tmnxDDMExtCalTxPowerSlope = _TmnxDDMExtCalTxPowerSlope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 48),
    _TmnxDDMExtCalTxPowerSlope_Type()
)
tmnxDDMExtCalTxPowerSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTxPowerSlope.setStatus("current")


class _TmnxDDMExtCalTxPowerOffset_Type(Integer32):
    """Custom type tmnxDDMExtCalTxPowerOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TmnxDDMExtCalTxPowerOffset_Type.__name__ = "Integer32"
_TmnxDDMExtCalTxPowerOffset_Object = MibTableColumn
tmnxDDMExtCalTxPowerOffset = _TmnxDDMExtCalTxPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 49),
    _TmnxDDMExtCalTxPowerOffset_Type()
)
tmnxDDMExtCalTxPowerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTxPowerOffset.setStatus("current")


class _TmnxDDMExtCalTemperatureSlope_Type(Unsigned32):
    """Custom type tmnxDDMExtCalTemperatureSlope based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxDDMExtCalTemperatureSlope_Type.__name__ = "Unsigned32"
_TmnxDDMExtCalTemperatureSlope_Object = MibTableColumn
tmnxDDMExtCalTemperatureSlope = _TmnxDDMExtCalTemperatureSlope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 50),
    _TmnxDDMExtCalTemperatureSlope_Type()
)
tmnxDDMExtCalTemperatureSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTemperatureSlope.setStatus("current")


class _TmnxDDMExtCalTemperatureOffset_Type(Integer32):
    """Custom type tmnxDDMExtCalTemperatureOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TmnxDDMExtCalTemperatureOffset_Type.__name__ = "Integer32"
_TmnxDDMExtCalTemperatureOffset_Object = MibTableColumn
tmnxDDMExtCalTemperatureOffset = _TmnxDDMExtCalTemperatureOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 51),
    _TmnxDDMExtCalTemperatureOffset_Type()
)
tmnxDDMExtCalTemperatureOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalTemperatureOffset.setStatus("current")


class _TmnxDDMExtCalVoltageSlope_Type(Unsigned32):
    """Custom type tmnxDDMExtCalVoltageSlope based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxDDMExtCalVoltageSlope_Type.__name__ = "Unsigned32"
_TmnxDDMExtCalVoltageSlope_Object = MibTableColumn
tmnxDDMExtCalVoltageSlope = _TmnxDDMExtCalVoltageSlope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 52),
    _TmnxDDMExtCalVoltageSlope_Type()
)
tmnxDDMExtCalVoltageSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalVoltageSlope.setStatus("current")


class _TmnxDDMExtCalVoltageOffset_Type(Integer32):
    """Custom type tmnxDDMExtCalVoltageOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TmnxDDMExtCalVoltageOffset_Type.__name__ = "Integer32"
_TmnxDDMExtCalVoltageOffset_Object = MibTableColumn
tmnxDDMExtCalVoltageOffset = _TmnxDDMExtCalVoltageOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 31, 1, 53),
    _TmnxDDMExtCalVoltageOffset_Type()
)
tmnxDDMExtCalVoltageOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMExtCalVoltageOffset.setStatus("current")
_TPortAccIngQGrpTableLastChgd_Type = TimeStamp
_TPortAccIngQGrpTableLastChgd_Object = MibScalar
tPortAccIngQGrpTableLastChgd = _TPortAccIngQGrpTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 32),
    _TPortAccIngQGrpTableLastChgd_Type()
)
tPortAccIngQGrpTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccIngQGrpTableLastChgd.setStatus("current")
_TPortAccIngQGrpTable_Object = MibTable
tPortAccIngQGrpTable = _TPortAccIngQGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 33)
)
if mibBuilder.loadTexts:
    tPortAccIngQGrpTable.setStatus("current")
_TPortAccIngQGrpEntry_Object = MibTableRow
tPortAccIngQGrpEntry = _TPortAccIngQGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 33, 1)
)
tPortAccIngQGrpEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortAccIngQGrpName"),
)
if mibBuilder.loadTexts:
    tPortAccIngQGrpEntry.setStatus("current")
_TPortAccIngQGrpName_Type = TNamedItem
_TPortAccIngQGrpName_Object = MibTableColumn
tPortAccIngQGrpName = _TPortAccIngQGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 33, 1, 1),
    _TPortAccIngQGrpName_Type()
)
tPortAccIngQGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortAccIngQGrpName.setStatus("current")
_TPortAccIngQGrpRowStatus_Type = RowStatus
_TPortAccIngQGrpRowStatus_Object = MibTableColumn
tPortAccIngQGrpRowStatus = _TPortAccIngQGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 33, 1, 2),
    _TPortAccIngQGrpRowStatus_Type()
)
tPortAccIngQGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQGrpRowStatus.setStatus("current")
_TPortAccIngQGrpLastChgd_Type = TimeStamp
_TPortAccIngQGrpLastChgd_Object = MibTableColumn
tPortAccIngQGrpLastChgd = _TPortAccIngQGrpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 33, 1, 3),
    _TPortAccIngQGrpLastChgd_Type()
)
tPortAccIngQGrpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccIngQGrpLastChgd.setStatus("current")


class _TPortAccIngQGrpSchedPol_Type(TNamedItemOrEmpty):
    """Custom type tPortAccIngQGrpSchedPol based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortAccIngQGrpSchedPol_Object = MibTableColumn
tPortAccIngQGrpSchedPol = _TPortAccIngQGrpSchedPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 33, 1, 4),
    _TPortAccIngQGrpSchedPol_Type()
)
tPortAccIngQGrpSchedPol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQGrpSchedPol.setStatus("current")


class _TPortAccIngQGrpAcctgPolId_Type(Unsigned32):
    """Custom type tPortAccIngQGrpAcctgPolId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TPortAccIngQGrpAcctgPolId_Type.__name__ = "Unsigned32"
_TPortAccIngQGrpAcctgPolId_Object = MibTableColumn
tPortAccIngQGrpAcctgPolId = _TPortAccIngQGrpAcctgPolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 33, 1, 5),
    _TPortAccIngQGrpAcctgPolId_Type()
)
tPortAccIngQGrpAcctgPolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQGrpAcctgPolId.setStatus("current")


class _TPortAccIngQGrpCollectStats_Type(TruthValue):
    """Custom type tPortAccIngQGrpCollectStats based on TruthValue"""


_TPortAccIngQGrpCollectStats_Object = MibTableColumn
tPortAccIngQGrpCollectStats = _TPortAccIngQGrpCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 33, 1, 6),
    _TPortAccIngQGrpCollectStats_Type()
)
tPortAccIngQGrpCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQGrpCollectStats.setStatus("current")


class _TPortAccIngQGrpDescr_Type(TItemDescription):
    """Custom type tPortAccIngQGrpDescr based on TItemDescription"""
    defaultHexValue = ""


_TPortAccIngQGrpDescr_Object = MibTableColumn
tPortAccIngQGrpDescr = _TPortAccIngQGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 33, 1, 7),
    _TPortAccIngQGrpDescr_Type()
)
tPortAccIngQGrpDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQGrpDescr.setStatus("current")
_TPortAccIngQOverTableLastChgd_Type = TimeStamp
_TPortAccIngQOverTableLastChgd_Object = MibScalar
tPortAccIngQOverTableLastChgd = _TPortAccIngQOverTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 34),
    _TPortAccIngQOverTableLastChgd_Type()
)
tPortAccIngQOverTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccIngQOverTableLastChgd.setStatus("current")
_TPortAccIngQOverTable_Object = MibTable
tPortAccIngQOverTable = _TPortAccIngQOverTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35)
)
if mibBuilder.loadTexts:
    tPortAccIngQOverTable.setStatus("current")
_TPortAccIngQOverEntry_Object = MibTableRow
tPortAccIngQOverEntry = _TPortAccIngQOverEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1)
)
tPortAccIngQOverEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortAccIngQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tPortAccIngQOverQueue"),
)
if mibBuilder.loadTexts:
    tPortAccIngQOverEntry.setStatus("current")


class _TPortAccIngQOverQueue_Type(TIngressQueueId):
    """Custom type tPortAccIngQOverQueue based on TIngressQueueId"""
    subtypeSpec = TIngressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TPortAccIngQOverQueue_Type.__name__ = "TIngressQueueId"
_TPortAccIngQOverQueue_Object = MibTableColumn
tPortAccIngQOverQueue = _TPortAccIngQOverQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1, 1),
    _TPortAccIngQOverQueue_Type()
)
tPortAccIngQOverQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortAccIngQOverQueue.setStatus("current")
_TPortAccIngQOverRowStatus_Type = RowStatus
_TPortAccIngQOverRowStatus_Object = MibTableColumn
tPortAccIngQOverRowStatus = _TPortAccIngQOverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1, 2),
    _TPortAccIngQOverRowStatus_Type()
)
tPortAccIngQOverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQOverRowStatus.setStatus("current")
_TPortAccIngQOverLastChanged_Type = TimeStamp
_TPortAccIngQOverLastChanged_Object = MibTableColumn
tPortAccIngQOverLastChanged = _TPortAccIngQOverLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1, 3),
    _TPortAccIngQOverLastChanged_Type()
)
tPortAccIngQOverLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccIngQOverLastChanged.setStatus("current")


class _TPortAccIngQOverCBS_Type(TBurstSizeOverride):
    """Custom type tPortAccIngQOverCBS based on TBurstSizeOverride"""
    defaultValue = -2


_TPortAccIngQOverCBS_Object = MibTableColumn
tPortAccIngQOverCBS = _TPortAccIngQOverCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1, 4),
    _TPortAccIngQOverCBS_Type()
)
tPortAccIngQOverCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQOverCBS.setStatus("current")
if mibBuilder.loadTexts:
    tPortAccIngQOverCBS.setUnits("kilo-bytes")


class _TPortAccIngQOverMBS_Type(TBurstSizeOverride):
    """Custom type tPortAccIngQOverMBS based on TBurstSizeOverride"""
    defaultValue = -2


_TPortAccIngQOverMBS_Object = MibTableColumn
tPortAccIngQOverMBS = _TPortAccIngQOverMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1, 5),
    _TPortAccIngQOverMBS_Type()
)
tPortAccIngQOverMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQOverMBS.setStatus("obsolete")
if mibBuilder.loadTexts:
    tPortAccIngQOverMBS.setUnits("kilo-bytes")


class _TPortAccIngQOverHiPrioOnly_Type(TBurstPercentOrDefaultOverride):
    """Custom type tPortAccIngQOverHiPrioOnly based on TBurstPercentOrDefaultOverride"""
    defaultValue = -2


_TPortAccIngQOverHiPrioOnly_Object = MibTableColumn
tPortAccIngQOverHiPrioOnly = _TPortAccIngQOverHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1, 6),
    _TPortAccIngQOverHiPrioOnly_Type()
)
tPortAccIngQOverHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQOverHiPrioOnly.setStatus("current")


class _TPortAccIngQOverAdminPIR_Type(TPIRRateOverride):
    """Custom type tPortAccIngQOverAdminPIR based on TPIRRateOverride"""
    defaultValue = -2


_TPortAccIngQOverAdminPIR_Object = MibTableColumn
tPortAccIngQOverAdminPIR = _TPortAccIngQOverAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1, 7),
    _TPortAccIngQOverAdminPIR_Type()
)
tPortAccIngQOverAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQOverAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortAccIngQOverAdminPIR.setUnits("kbps")


class _TPortAccIngQOverAdminCIR_Type(TCIRRateOverride):
    """Custom type tPortAccIngQOverAdminCIR based on TCIRRateOverride"""
    defaultValue = -2


_TPortAccIngQOverAdminCIR_Object = MibTableColumn
tPortAccIngQOverAdminCIR = _TPortAccIngQOverAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1, 8),
    _TPortAccIngQOverAdminCIR_Type()
)
tPortAccIngQOverAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQOverAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortAccIngQOverAdminCIR.setUnits("kbps")


class _TPortAccIngQOverPIRAdaptation_Type(TAdaptationRuleOverride):
    """Custom type tPortAccIngQOverPIRAdaptation based on TAdaptationRuleOverride"""


_TPortAccIngQOverPIRAdaptation_Object = MibTableColumn
tPortAccIngQOverPIRAdaptation = _TPortAccIngQOverPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1, 9),
    _TPortAccIngQOverPIRAdaptation_Type()
)
tPortAccIngQOverPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQOverPIRAdaptation.setStatus("current")


class _TPortAccIngQOverCIRAdaptation_Type(TAdaptationRuleOverride):
    """Custom type tPortAccIngQOverCIRAdaptation based on TAdaptationRuleOverride"""


_TPortAccIngQOverCIRAdaptation_Object = MibTableColumn
tPortAccIngQOverCIRAdaptation = _TPortAccIngQOverCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1, 10),
    _TPortAccIngQOverCIRAdaptation_Type()
)
tPortAccIngQOverCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQOverCIRAdaptation.setStatus("current")


class _TPortAccIngQOverMBSBytes_Type(TBurstSizeBytesOverride):
    """Custom type tPortAccIngQOverMBSBytes based on TBurstSizeBytesOverride"""
    defaultValue = -2


_TPortAccIngQOverMBSBytes_Object = MibTableColumn
tPortAccIngQOverMBSBytes = _TPortAccIngQOverMBSBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 35, 1, 11),
    _TPortAccIngQOverMBSBytes_Type()
)
tPortAccIngQOverMBSBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccIngQOverMBSBytes.setStatus("current")
if mibBuilder.loadTexts:
    tPortAccIngQOverMBSBytes.setUnits("bytes")
_TPortAccEgrQGrpTableLastChgd_Type = TimeStamp
_TPortAccEgrQGrpTableLastChgd_Object = MibScalar
tPortAccEgrQGrpTableLastChgd = _TPortAccEgrQGrpTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 36),
    _TPortAccEgrQGrpTableLastChgd_Type()
)
tPortAccEgrQGrpTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpTableLastChgd.setStatus("current")
_TPortAccEgrQGrpTable_Object = MibTable
tPortAccEgrQGrpTable = _TPortAccEgrQGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 37)
)
if mibBuilder.loadTexts:
    tPortAccEgrQGrpTable.setStatus("current")
_TPortAccEgrQGrpEntry_Object = MibTableRow
tPortAccEgrQGrpEntry = _TPortAccEgrQGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 37, 1)
)
tPortAccEgrQGrpEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortAccEgrQGrpName"),
)
if mibBuilder.loadTexts:
    tPortAccEgrQGrpEntry.setStatus("current")
_TPortAccEgrQGrpName_Type = TNamedItem
_TPortAccEgrQGrpName_Object = MibTableColumn
tPortAccEgrQGrpName = _TPortAccEgrQGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 37, 1, 1),
    _TPortAccEgrQGrpName_Type()
)
tPortAccEgrQGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpName.setStatus("current")
_TPortAccEgrQGrpRowStatus_Type = RowStatus
_TPortAccEgrQGrpRowStatus_Object = MibTableColumn
tPortAccEgrQGrpRowStatus = _TPortAccEgrQGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 37, 1, 2),
    _TPortAccEgrQGrpRowStatus_Type()
)
tPortAccEgrQGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpRowStatus.setStatus("current")
_TPortAccEgrQGrpLastChgd_Type = TimeStamp
_TPortAccEgrQGrpLastChgd_Object = MibTableColumn
tPortAccEgrQGrpLastChgd = _TPortAccEgrQGrpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 37, 1, 3),
    _TPortAccEgrQGrpLastChgd_Type()
)
tPortAccEgrQGrpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpLastChgd.setStatus("current")


class _TPortAccEgrQGrpSchedPol_Type(TNamedItemOrEmpty):
    """Custom type tPortAccEgrQGrpSchedPol based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortAccEgrQGrpSchedPol_Object = MibTableColumn
tPortAccEgrQGrpSchedPol = _TPortAccEgrQGrpSchedPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 37, 1, 4),
    _TPortAccEgrQGrpSchedPol_Type()
)
tPortAccEgrQGrpSchedPol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpSchedPol.setStatus("current")


class _TPortAccEgrQGrpAggRateLimit_Type(TPortSchedulerPIR):
    """Custom type tPortAccEgrQGrpAggRateLimit based on TPortSchedulerPIR"""
    defaultValue = -1


_TPortAccEgrQGrpAggRateLimit_Object = MibTableColumn
tPortAccEgrQGrpAggRateLimit = _TPortAccEgrQGrpAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 37, 1, 5),
    _TPortAccEgrQGrpAggRateLimit_Type()
)
tPortAccEgrQGrpAggRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpAggRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpAggRateLimit.setUnits("kbps")


class _TPortAccEgrQGrpAcctgPolId_Type(Unsigned32):
    """Custom type tPortAccEgrQGrpAcctgPolId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TPortAccEgrQGrpAcctgPolId_Type.__name__ = "Unsigned32"
_TPortAccEgrQGrpAcctgPolId_Object = MibTableColumn
tPortAccEgrQGrpAcctgPolId = _TPortAccEgrQGrpAcctgPolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 37, 1, 6),
    _TPortAccEgrQGrpAcctgPolId_Type()
)
tPortAccEgrQGrpAcctgPolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpAcctgPolId.setStatus("current")


class _TPortAccEgrQGrpCollectStats_Type(TruthValue):
    """Custom type tPortAccEgrQGrpCollectStats based on TruthValue"""


_TPortAccEgrQGrpCollectStats_Object = MibTableColumn
tPortAccEgrQGrpCollectStats = _TPortAccEgrQGrpCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 37, 1, 7),
    _TPortAccEgrQGrpCollectStats_Type()
)
tPortAccEgrQGrpCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpCollectStats.setStatus("current")


class _TPortAccEgrQGrpFrameBaseActg_Type(TruthValue):
    """Custom type tPortAccEgrQGrpFrameBaseActg based on TruthValue"""


_TPortAccEgrQGrpFrameBaseActg_Object = MibTableColumn
tPortAccEgrQGrpFrameBaseActg = _TPortAccEgrQGrpFrameBaseActg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 37, 1, 8),
    _TPortAccEgrQGrpFrameBaseActg_Type()
)
tPortAccEgrQGrpFrameBaseActg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpFrameBaseActg.setStatus("current")


class _TPortAccEgrQGrpDescr_Type(TItemDescription):
    """Custom type tPortAccEgrQGrpDescr based on TItemDescription"""
    defaultHexValue = ""


_TPortAccEgrQGrpDescr_Object = MibTableColumn
tPortAccEgrQGrpDescr = _TPortAccEgrQGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 37, 1, 9),
    _TPortAccEgrQGrpDescr_Type()
)
tPortAccEgrQGrpDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpDescr.setStatus("current")
_TPortAccEgrQOverTableLastChgd_Type = TimeStamp
_TPortAccEgrQOverTableLastChgd_Object = MibScalar
tPortAccEgrQOverTableLastChgd = _TPortAccEgrQOverTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 38),
    _TPortAccEgrQOverTableLastChgd_Type()
)
tPortAccEgrQOverTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrQOverTableLastChgd.setStatus("current")
_TPortAccEgrQOverTable_Object = MibTable
tPortAccEgrQOverTable = _TPortAccEgrQOverTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39)
)
if mibBuilder.loadTexts:
    tPortAccEgrQOverTable.setStatus("current")
_TPortAccEgrQOverEntry_Object = MibTableRow
tPortAccEgrQOverEntry = _TPortAccEgrQOverEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1)
)
tPortAccEgrQOverEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortAccEgrQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tPortAccEgrQOverQueue"),
)
if mibBuilder.loadTexts:
    tPortAccEgrQOverEntry.setStatus("current")


class _TPortAccEgrQOverQueue_Type(TEgressQueueId):
    """Custom type tPortAccEgrQOverQueue based on TEgressQueueId"""
    subtypeSpec = TEgressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TPortAccEgrQOverQueue_Type.__name__ = "TEgressQueueId"
_TPortAccEgrQOverQueue_Object = MibTableColumn
tPortAccEgrQOverQueue = _TPortAccEgrQOverQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 1),
    _TPortAccEgrQOverQueue_Type()
)
tPortAccEgrQOverQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortAccEgrQOverQueue.setStatus("current")
_TPortAccEgrQOverRowStatus_Type = RowStatus
_TPortAccEgrQOverRowStatus_Object = MibTableColumn
tPortAccEgrQOverRowStatus = _TPortAccEgrQOverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 2),
    _TPortAccEgrQOverRowStatus_Type()
)
tPortAccEgrQOverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverRowStatus.setStatus("current")
_TPortAccEgrQOverLastChanged_Type = TimeStamp
_TPortAccEgrQOverLastChanged_Object = MibTableColumn
tPortAccEgrQOverLastChanged = _TPortAccEgrQOverLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 3),
    _TPortAccEgrQOverLastChanged_Type()
)
tPortAccEgrQOverLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrQOverLastChanged.setStatus("current")


class _TPortAccEgrQOverCBS_Type(TBurstSizeOverride):
    """Custom type tPortAccEgrQOverCBS based on TBurstSizeOverride"""
    defaultValue = -2


_TPortAccEgrQOverCBS_Object = MibTableColumn
tPortAccEgrQOverCBS = _TPortAccEgrQOverCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 4),
    _TPortAccEgrQOverCBS_Type()
)
tPortAccEgrQOverCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverCBS.setStatus("current")
if mibBuilder.loadTexts:
    tPortAccEgrQOverCBS.setUnits("kilo-bytes")


class _TPortAccEgrQOverMBS_Type(TBurstSizeOverride):
    """Custom type tPortAccEgrQOverMBS based on TBurstSizeOverride"""
    defaultValue = -2


_TPortAccEgrQOverMBS_Object = MibTableColumn
tPortAccEgrQOverMBS = _TPortAccEgrQOverMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 5),
    _TPortAccEgrQOverMBS_Type()
)
tPortAccEgrQOverMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverMBS.setStatus("obsolete")
if mibBuilder.loadTexts:
    tPortAccEgrQOverMBS.setUnits("kilo-bytes")


class _TPortAccEgrQOverHiPrioOnly_Type(TBurstPercentOrDefaultOverride):
    """Custom type tPortAccEgrQOverHiPrioOnly based on TBurstPercentOrDefaultOverride"""
    defaultValue = -2


_TPortAccEgrQOverHiPrioOnly_Object = MibTableColumn
tPortAccEgrQOverHiPrioOnly = _TPortAccEgrQOverHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 6),
    _TPortAccEgrQOverHiPrioOnly_Type()
)
tPortAccEgrQOverHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverHiPrioOnly.setStatus("current")


class _TPortAccEgrQOverAdminPIR_Type(TPIRRateOverride):
    """Custom type tPortAccEgrQOverAdminPIR based on TPIRRateOverride"""
    defaultValue = -2


_TPortAccEgrQOverAdminPIR_Object = MibTableColumn
tPortAccEgrQOverAdminPIR = _TPortAccEgrQOverAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 7),
    _TPortAccEgrQOverAdminPIR_Type()
)
tPortAccEgrQOverAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortAccEgrQOverAdminPIR.setUnits("kbps")


class _TPortAccEgrQOverAdminCIR_Type(TCIRRateOverride):
    """Custom type tPortAccEgrQOverAdminCIR based on TCIRRateOverride"""
    defaultValue = -2


_TPortAccEgrQOverAdminCIR_Object = MibTableColumn
tPortAccEgrQOverAdminCIR = _TPortAccEgrQOverAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 8),
    _TPortAccEgrQOverAdminCIR_Type()
)
tPortAccEgrQOverAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortAccEgrQOverAdminCIR.setUnits("kbps")


class _TPortAccEgrQOverPIRAdaptation_Type(TAdaptationRuleOverride):
    """Custom type tPortAccEgrQOverPIRAdaptation based on TAdaptationRuleOverride"""


_TPortAccEgrQOverPIRAdaptation_Object = MibTableColumn
tPortAccEgrQOverPIRAdaptation = _TPortAccEgrQOverPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 9),
    _TPortAccEgrQOverPIRAdaptation_Type()
)
tPortAccEgrQOverPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverPIRAdaptation.setStatus("current")


class _TPortAccEgrQOverCIRAdaptation_Type(TAdaptationRuleOverride):
    """Custom type tPortAccEgrQOverCIRAdaptation based on TAdaptationRuleOverride"""


_TPortAccEgrQOverCIRAdaptation_Object = MibTableColumn
tPortAccEgrQOverCIRAdaptation = _TPortAccEgrQOverCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 10),
    _TPortAccEgrQOverCIRAdaptation_Type()
)
tPortAccEgrQOverCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverCIRAdaptation.setStatus("current")


class _TPortAccEgrQOverMBSBytes_Type(TBurstSizeBytesOverride):
    """Custom type tPortAccEgrQOverMBSBytes based on TBurstSizeBytesOverride"""
    defaultValue = -2


_TPortAccEgrQOverMBSBytes_Object = MibTableColumn
tPortAccEgrQOverMBSBytes = _TPortAccEgrQOverMBSBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 11),
    _TPortAccEgrQOverMBSBytes_Type()
)
tPortAccEgrQOverMBSBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverMBSBytes.setStatus("current")
if mibBuilder.loadTexts:
    tPortAccEgrQOverMBSBytes.setUnits("bytes")


class _TPortAccEgrQOverAdminPIRPercent_Type(TPIRPercentOverride):
    """Custom type tPortAccEgrQOverAdminPIRPercent based on TPIRPercentOverride"""
    defaultValue = -2


_TPortAccEgrQOverAdminPIRPercent_Object = MibTableColumn
tPortAccEgrQOverAdminPIRPercent = _TPortAccEgrQOverAdminPIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 12),
    _TPortAccEgrQOverAdminPIRPercent_Type()
)
tPortAccEgrQOverAdminPIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverAdminPIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tPortAccEgrQOverAdminPIRPercent.setUnits("hundredths of a percent")


class _TPortAccEgrQOverAdminCIRPercent_Type(TCIRPercentOverride):
    """Custom type tPortAccEgrQOverAdminCIRPercent based on TCIRPercentOverride"""
    defaultValue = -2


_TPortAccEgrQOverAdminCIRPercent_Object = MibTableColumn
tPortAccEgrQOverAdminCIRPercent = _TPortAccEgrQOverAdminCIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 13),
    _TPortAccEgrQOverAdminCIRPercent_Type()
)
tPortAccEgrQOverAdminCIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverAdminCIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tPortAccEgrQOverAdminCIRPercent.setUnits("hundredths of a percent")


class _TPortAccEgrQOverRateType_Type(TRateType):
    """Custom type tPortAccEgrQOverRateType based on TRateType"""


_TPortAccEgrQOverRateType_Object = MibTableColumn
tPortAccEgrQOverRateType = _TPortAccEgrQOverRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 39, 1, 14),
    _TPortAccEgrQOverRateType_Type()
)
tPortAccEgrQOverRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQOverRateType.setStatus("current")
_TPortNetEgrQGrpTableLastChgd_Type = TimeStamp
_TPortNetEgrQGrpTableLastChgd_Object = MibScalar
tPortNetEgrQGrpTableLastChgd = _TPortNetEgrQGrpTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 40),
    _TPortNetEgrQGrpTableLastChgd_Type()
)
tPortNetEgrQGrpTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpTableLastChgd.setStatus("current")
_TPortNetEgrQGrpTable_Object = MibTable
tPortNetEgrQGrpTable = _TPortNetEgrQGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41)
)
if mibBuilder.loadTexts:
    tPortNetEgrQGrpTable.setStatus("current")
_TPortNetEgrQGrpEntry_Object = MibTableRow
tPortNetEgrQGrpEntry = _TPortNetEgrQGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1)
)
tPortNetEgrQGrpEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpInstanceId"),
)
if mibBuilder.loadTexts:
    tPortNetEgrQGrpEntry.setStatus("current")
_TPortNetEgrQGrpName_Type = TNamedItem
_TPortNetEgrQGrpName_Object = MibTableColumn
tPortNetEgrQGrpName = _TPortNetEgrQGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1, 1),
    _TPortNetEgrQGrpName_Type()
)
tPortNetEgrQGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpName.setStatus("current")
_TPortNetEgrQGrpRowStatus_Type = RowStatus
_TPortNetEgrQGrpRowStatus_Object = MibTableColumn
tPortNetEgrQGrpRowStatus = _TPortNetEgrQGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1, 2),
    _TPortNetEgrQGrpRowStatus_Type()
)
tPortNetEgrQGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpRowStatus.setStatus("current")
_TPortNetEgrQGrpLastChgd_Type = TimeStamp
_TPortNetEgrQGrpLastChgd_Object = MibTableColumn
tPortNetEgrQGrpLastChgd = _TPortNetEgrQGrpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1, 3),
    _TPortNetEgrQGrpLastChgd_Type()
)
tPortNetEgrQGrpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpLastChgd.setStatus("current")


class _TPortNetEgrQGrpSchedPol_Type(TNamedItemOrEmpty):
    """Custom type tPortNetEgrQGrpSchedPol based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortNetEgrQGrpSchedPol_Object = MibTableColumn
tPortNetEgrQGrpSchedPol = _TPortNetEgrQGrpSchedPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1, 4),
    _TPortNetEgrQGrpSchedPol_Type()
)
tPortNetEgrQGrpSchedPol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpSchedPol.setStatus("current")


class _TPortNetEgrQGrpAggRateLimit_Type(TPortSchedulerPIR):
    """Custom type tPortNetEgrQGrpAggRateLimit based on TPortSchedulerPIR"""
    defaultValue = -1


_TPortNetEgrQGrpAggRateLimit_Object = MibTableColumn
tPortNetEgrQGrpAggRateLimit = _TPortNetEgrQGrpAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1, 5),
    _TPortNetEgrQGrpAggRateLimit_Type()
)
tPortNetEgrQGrpAggRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpAggRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpAggRateLimit.setUnits("kbps")


class _TPortNetEgrQGrpAcctgPolId_Type(Unsigned32):
    """Custom type tPortNetEgrQGrpAcctgPolId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TPortNetEgrQGrpAcctgPolId_Type.__name__ = "Unsigned32"
_TPortNetEgrQGrpAcctgPolId_Object = MibTableColumn
tPortNetEgrQGrpAcctgPolId = _TPortNetEgrQGrpAcctgPolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1, 6),
    _TPortNetEgrQGrpAcctgPolId_Type()
)
tPortNetEgrQGrpAcctgPolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpAcctgPolId.setStatus("current")


class _TPortNetEgrQGrpCollectStats_Type(TruthValue):
    """Custom type tPortNetEgrQGrpCollectStats based on TruthValue"""


_TPortNetEgrQGrpCollectStats_Object = MibTableColumn
tPortNetEgrQGrpCollectStats = _TPortNetEgrQGrpCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1, 7),
    _TPortNetEgrQGrpCollectStats_Type()
)
tPortNetEgrQGrpCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpCollectStats.setStatus("current")


class _TPortNetEgrQGrpFrameBaseActg_Type(TruthValue):
    """Custom type tPortNetEgrQGrpFrameBaseActg based on TruthValue"""


_TPortNetEgrQGrpFrameBaseActg_Object = MibTableColumn
tPortNetEgrQGrpFrameBaseActg = _TPortNetEgrQGrpFrameBaseActg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1, 8),
    _TPortNetEgrQGrpFrameBaseActg_Type()
)
tPortNetEgrQGrpFrameBaseActg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpFrameBaseActg.setStatus("current")


class _TPortNetEgrQGrpDescr_Type(TItemDescription):
    """Custom type tPortNetEgrQGrpDescr based on TItemDescription"""
    defaultHexValue = ""


_TPortNetEgrQGrpDescr_Object = MibTableColumn
tPortNetEgrQGrpDescr = _TPortNetEgrQGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1, 9),
    _TPortNetEgrQGrpDescr_Type()
)
tPortNetEgrQGrpDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpDescr.setStatus("current")


class _TPortNetEgrQGrpPlcrCntrlPolicy_Type(TNamedItemOrEmpty):
    """Custom type tPortNetEgrQGrpPlcrCntrlPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortNetEgrQGrpPlcrCntrlPolicy_Object = MibTableColumn
tPortNetEgrQGrpPlcrCntrlPolicy = _TPortNetEgrQGrpPlcrCntrlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1, 10),
    _TPortNetEgrQGrpPlcrCntrlPolicy_Type()
)
tPortNetEgrQGrpPlcrCntrlPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPlcrCntrlPolicy.setStatus("current")


class _TPortNetEgrQGrpInstanceId_Type(Unsigned32):
    """Custom type tPortNetEgrQGrpInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TPortNetEgrQGrpInstanceId_Type.__name__ = "Unsigned32"
_TPortNetEgrQGrpInstanceId_Object = MibTableColumn
tPortNetEgrQGrpInstanceId = _TPortNetEgrQGrpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 41, 1, 11),
    _TPortNetEgrQGrpInstanceId_Type()
)
tPortNetEgrQGrpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpInstanceId.setStatus("current")
_TPortNetEgrQOverTableLastChgd_Type = TimeStamp
_TPortNetEgrQOverTableLastChgd_Object = MibScalar
tPortNetEgrQOverTableLastChgd = _TPortNetEgrQOverTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 42),
    _TPortNetEgrQOverTableLastChgd_Type()
)
tPortNetEgrQOverTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQOverTableLastChgd.setStatus("current")
_TPortNetEgrQOverTable_Object = MibTable
tPortNetEgrQOverTable = _TPortNetEgrQOverTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43)
)
if mibBuilder.loadTexts:
    tPortNetEgrQOverTable.setStatus("current")
_TPortNetEgrQOverEntry_Object = MibTableRow
tPortNetEgrQOverEntry = _TPortNetEgrQOverEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1)
)
tPortNetEgrQOverEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpInstanceId"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQOverQueue"),
)
if mibBuilder.loadTexts:
    tPortNetEgrQOverEntry.setStatus("current")


class _TPortNetEgrQOverQueue_Type(TEgressQueueId):
    """Custom type tPortNetEgrQOverQueue based on TEgressQueueId"""
    subtypeSpec = TEgressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TPortNetEgrQOverQueue_Type.__name__ = "TEgressQueueId"
_TPortNetEgrQOverQueue_Object = MibTableColumn
tPortNetEgrQOverQueue = _TPortNetEgrQOverQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 1),
    _TPortNetEgrQOverQueue_Type()
)
tPortNetEgrQOverQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortNetEgrQOverQueue.setStatus("current")
_TPortNetEgrQOverRowStatus_Type = RowStatus
_TPortNetEgrQOverRowStatus_Object = MibTableColumn
tPortNetEgrQOverRowStatus = _TPortNetEgrQOverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 2),
    _TPortNetEgrQOverRowStatus_Type()
)
tPortNetEgrQOverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverRowStatus.setStatus("current")
_TPortNetEgrQOverLastChanged_Type = TimeStamp
_TPortNetEgrQOverLastChanged_Object = MibTableColumn
tPortNetEgrQOverLastChanged = _TPortNetEgrQOverLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 3),
    _TPortNetEgrQOverLastChanged_Type()
)
tPortNetEgrQOverLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQOverLastChanged.setStatus("current")


class _TPortNetEgrQOverCBS_Type(TBurstSizeOverride):
    """Custom type tPortNetEgrQOverCBS based on TBurstSizeOverride"""
    defaultValue = -2


_TPortNetEgrQOverCBS_Object = MibTableColumn
tPortNetEgrQOverCBS = _TPortNetEgrQOverCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 4),
    _TPortNetEgrQOverCBS_Type()
)
tPortNetEgrQOverCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverCBS.setStatus("current")
if mibBuilder.loadTexts:
    tPortNetEgrQOverCBS.setUnits("kilo-bytes")


class _TPortNetEgrQOverMBS_Type(TBurstSizeOverride):
    """Custom type tPortNetEgrQOverMBS based on TBurstSizeOverride"""
    defaultValue = -2


_TPortNetEgrQOverMBS_Object = MibTableColumn
tPortNetEgrQOverMBS = _TPortNetEgrQOverMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 5),
    _TPortNetEgrQOverMBS_Type()
)
tPortNetEgrQOverMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverMBS.setStatus("obsolete")
if mibBuilder.loadTexts:
    tPortNetEgrQOverMBS.setUnits("kilo-bytes")


class _TPortNetEgrQOverHiPrioOnly_Type(TBurstPercentOrDefaultOverride):
    """Custom type tPortNetEgrQOverHiPrioOnly based on TBurstPercentOrDefaultOverride"""
    defaultValue = -2


_TPortNetEgrQOverHiPrioOnly_Object = MibTableColumn
tPortNetEgrQOverHiPrioOnly = _TPortNetEgrQOverHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 6),
    _TPortNetEgrQOverHiPrioOnly_Type()
)
tPortNetEgrQOverHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverHiPrioOnly.setStatus("current")


class _TPortNetEgrQOverAdminPIR_Type(TPIRRateOverride):
    """Custom type tPortNetEgrQOverAdminPIR based on TPIRRateOverride"""
    defaultValue = -2


_TPortNetEgrQOverAdminPIR_Object = MibTableColumn
tPortNetEgrQOverAdminPIR = _TPortNetEgrQOverAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 7),
    _TPortNetEgrQOverAdminPIR_Type()
)
tPortNetEgrQOverAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortNetEgrQOverAdminPIR.setUnits("kbps")


class _TPortNetEgrQOverAdminCIR_Type(TCIRRateOverride):
    """Custom type tPortNetEgrQOverAdminCIR based on TCIRRateOverride"""
    defaultValue = -2


_TPortNetEgrQOverAdminCIR_Object = MibTableColumn
tPortNetEgrQOverAdminCIR = _TPortNetEgrQOverAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 8),
    _TPortNetEgrQOverAdminCIR_Type()
)
tPortNetEgrQOverAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortNetEgrQOverAdminCIR.setUnits("kbps")


class _TPortNetEgrQOverPIRAdaptation_Type(TAdaptationRuleOverride):
    """Custom type tPortNetEgrQOverPIRAdaptation based on TAdaptationRuleOverride"""


_TPortNetEgrQOverPIRAdaptation_Object = MibTableColumn
tPortNetEgrQOverPIRAdaptation = _TPortNetEgrQOverPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 9),
    _TPortNetEgrQOverPIRAdaptation_Type()
)
tPortNetEgrQOverPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverPIRAdaptation.setStatus("current")


class _TPortNetEgrQOverCIRAdaptation_Type(TAdaptationRuleOverride):
    """Custom type tPortNetEgrQOverCIRAdaptation based on TAdaptationRuleOverride"""


_TPortNetEgrQOverCIRAdaptation_Object = MibTableColumn
tPortNetEgrQOverCIRAdaptation = _TPortNetEgrQOverCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 10),
    _TPortNetEgrQOverCIRAdaptation_Type()
)
tPortNetEgrQOverCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverCIRAdaptation.setStatus("current")


class _TPortNetEgrQOverMBSBytes_Type(TBurstSizeBytesOverride):
    """Custom type tPortNetEgrQOverMBSBytes based on TBurstSizeBytesOverride"""
    defaultValue = -2


_TPortNetEgrQOverMBSBytes_Object = MibTableColumn
tPortNetEgrQOverMBSBytes = _TPortNetEgrQOverMBSBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 11),
    _TPortNetEgrQOverMBSBytes_Type()
)
tPortNetEgrQOverMBSBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverMBSBytes.setStatus("current")
if mibBuilder.loadTexts:
    tPortNetEgrQOverMBSBytes.setUnits("bytes")


class _TPortNetEgrQOverAdminPIRPercent_Type(TPIRPercentOverride):
    """Custom type tPortNetEgrQOverAdminPIRPercent based on TPIRPercentOverride"""
    defaultValue = -2


_TPortNetEgrQOverAdminPIRPercent_Object = MibTableColumn
tPortNetEgrQOverAdminPIRPercent = _TPortNetEgrQOverAdminPIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 12),
    _TPortNetEgrQOverAdminPIRPercent_Type()
)
tPortNetEgrQOverAdminPIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverAdminPIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tPortNetEgrQOverAdminPIRPercent.setUnits("hundredths of a percent")


class _TPortNetEgrQOverAdminCIRPercent_Type(TCIRPercentOverride):
    """Custom type tPortNetEgrQOverAdminCIRPercent based on TCIRPercentOverride"""
    defaultValue = -2


_TPortNetEgrQOverAdminCIRPercent_Object = MibTableColumn
tPortNetEgrQOverAdminCIRPercent = _TPortNetEgrQOverAdminCIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 13),
    _TPortNetEgrQOverAdminCIRPercent_Type()
)
tPortNetEgrQOverAdminCIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverAdminCIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tPortNetEgrQOverAdminCIRPercent.setUnits("hundredths of a percent")


class _TPortNetEgrQOverRateType_Type(TRateType):
    """Custom type tPortNetEgrQOverRateType based on TRateType"""


_TPortNetEgrQOverRateType_Object = MibTableColumn
tPortNetEgrQOverRateType = _TPortNetEgrQOverRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 43, 1, 14),
    _TPortNetEgrQOverRateType_Type()
)
tPortNetEgrQOverRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortNetEgrQOverRateType.setStatus("current")
_TmnxBundleMlfrTable_Object = MibTable
tmnxBundleMlfrTable = _TmnxBundleMlfrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 44)
)
if mibBuilder.loadTexts:
    tmnxBundleMlfrTable.setStatus("current")
_TmnxBundleMlfrEntry_Object = MibTableRow
tmnxBundleMlfrEntry = _TmnxBundleMlfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 44, 1)
)
tmnxBundleMlfrEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
)
if mibBuilder.loadTexts:
    tmnxBundleMlfrEntry.setStatus("current")


class _TmnxBundleMlfrBundleId_Type(SnmpAdminString):
    """Custom type tmnxBundleMlfrBundleId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_TmnxBundleMlfrBundleId_Type.__name__ = "SnmpAdminString"
_TmnxBundleMlfrBundleId_Object = MibTableColumn
tmnxBundleMlfrBundleId = _TmnxBundleMlfrBundleId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 44, 1, 1),
    _TmnxBundleMlfrBundleId_Type()
)
tmnxBundleMlfrBundleId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlfrBundleId.setStatus("current")


class _TmnxBundleMlfrIngQoSProfId_Type(TMcFrQoSProfileId):
    """Custom type tmnxBundleMlfrIngQoSProfId based on TMcFrQoSProfileId"""
    defaultValue = 0


_TmnxBundleMlfrIngQoSProfId_Object = MibTableColumn
tmnxBundleMlfrIngQoSProfId = _TmnxBundleMlfrIngQoSProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 44, 1, 4),
    _TmnxBundleMlfrIngQoSProfId_Type()
)
tmnxBundleMlfrIngQoSProfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlfrIngQoSProfId.setStatus("current")


class _TmnxBundleMlfrEgrQoSProfId_Type(TMcFrQoSProfileId):
    """Custom type tmnxBundleMlfrEgrQoSProfId based on TMcFrQoSProfileId"""
    defaultValue = 0


_TmnxBundleMlfrEgrQoSProfId_Object = MibTableColumn
tmnxBundleMlfrEgrQoSProfId = _TmnxBundleMlfrEgrQoSProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 44, 1, 5),
    _TmnxBundleMlfrEgrQoSProfId_Type()
)
tmnxBundleMlfrEgrQoSProfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlfrEgrQoSProfId.setStatus("current")


class _TmnxBundleMlfrHelloTimer_Type(Unsigned32):
    """Custom type tmnxBundleMlfrHelloTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_TmnxBundleMlfrHelloTimer_Type.__name__ = "Unsigned32"
_TmnxBundleMlfrHelloTimer_Object = MibTableColumn
tmnxBundleMlfrHelloTimer = _TmnxBundleMlfrHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 44, 1, 6),
    _TmnxBundleMlfrHelloTimer_Type()
)
tmnxBundleMlfrHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlfrHelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleMlfrHelloTimer.setUnits("seconds")


class _TmnxBundleMlfrHelloRetryCount_Type(Unsigned32):
    """Custom type tmnxBundleMlfrHelloRetryCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxBundleMlfrHelloRetryCount_Type.__name__ = "Unsigned32"
_TmnxBundleMlfrHelloRetryCount_Object = MibTableColumn
tmnxBundleMlfrHelloRetryCount = _TmnxBundleMlfrHelloRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 44, 1, 7),
    _TmnxBundleMlfrHelloRetryCount_Type()
)
tmnxBundleMlfrHelloRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlfrHelloRetryCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleMlfrHelloRetryCount.setUnits("seconds")


class _TmnxBundleMlfrAckTimer_Type(Unsigned32):
    """Custom type tmnxBundleMlfrAckTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxBundleMlfrAckTimer_Type.__name__ = "Unsigned32"
_TmnxBundleMlfrAckTimer_Object = MibTableColumn
tmnxBundleMlfrAckTimer = _TmnxBundleMlfrAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 44, 1, 8),
    _TmnxBundleMlfrAckTimer_Type()
)
tmnxBundleMlfrAckTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBundleMlfrAckTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBundleMlfrAckTimer.setUnits("seconds")
_TmnxBundleMlfrLastChanged_Type = TimeStamp
_TmnxBundleMlfrLastChanged_Object = MibTableColumn
tmnxBundleMlfrLastChanged = _TmnxBundleMlfrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 44, 1, 9),
    _TmnxBundleMlfrLastChanged_Type()
)
tmnxBundleMlfrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMlfrLastChanged.setStatus("current")
_TmnxPortIngQosQStatTable_Object = MibTable
tmnxPortIngQosQStatTable = _TmnxPortIngQosQStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45)
)
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatTable.setStatus("current")
_TmnxPortIngQosQStatEntry_Object = MibTableRow
tmnxPortIngQosQStatEntry = _TmnxPortIngQosQStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1)
)
tmnxPortIngQosQStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortAccIngQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortIngQosQStatQueueId"),
)
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatEntry.setStatus("current")


class _TmnxPortIngQosQStatQueueId_Type(TIngressQueueId):
    """Custom type tmnxPortIngQosQStatQueueId based on TIngressQueueId"""
    subtypeSpec = TIngressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TmnxPortIngQosQStatQueueId_Type.__name__ = "TIngressQueueId"
_TmnxPortIngQosQStatQueueId_Object = MibTableColumn
tmnxPortIngQosQStatQueueId = _TmnxPortIngQosQStatQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 1),
    _TmnxPortIngQosQStatQueueId_Type()
)
tmnxPortIngQosQStatQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatQueueId.setStatus("current")
_TmnxPortIngQosQStatOffHiPrioPkts_Type = Counter64
_TmnxPortIngQosQStatOffHiPrioPkts_Object = MibTableColumn
tmnxPortIngQosQStatOffHiPrioPkts = _TmnxPortIngQosQStatOffHiPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 2),
    _TmnxPortIngQosQStatOffHiPrioPkts_Type()
)
tmnxPortIngQosQStatOffHiPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatOffHiPrioPkts.setStatus("current")
_TmnxPortIngQosQStatDpdHiPrioPkts_Type = Counter64
_TmnxPortIngQosQStatDpdHiPrioPkts_Object = MibTableColumn
tmnxPortIngQosQStatDpdHiPrioPkts = _TmnxPortIngQosQStatDpdHiPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 3),
    _TmnxPortIngQosQStatDpdHiPrioPkts_Type()
)
tmnxPortIngQosQStatDpdHiPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatDpdHiPrioPkts.setStatus("current")
_TmnxPortIngQosQStatOffLoPrioPkts_Type = Counter64
_TmnxPortIngQosQStatOffLoPrioPkts_Object = MibTableColumn
tmnxPortIngQosQStatOffLoPrioPkts = _TmnxPortIngQosQStatOffLoPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 4),
    _TmnxPortIngQosQStatOffLoPrioPkts_Type()
)
tmnxPortIngQosQStatOffLoPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatOffLoPrioPkts.setStatus("current")
_TmnxPortIngQosQStatDpdLoPrioPkts_Type = Counter64
_TmnxPortIngQosQStatDpdLoPrioPkts_Object = MibTableColumn
tmnxPortIngQosQStatDpdLoPrioPkts = _TmnxPortIngQosQStatDpdLoPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 5),
    _TmnxPortIngQosQStatDpdLoPrioPkts_Type()
)
tmnxPortIngQosQStatDpdLoPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatDpdLoPrioPkts.setStatus("current")
_TmnxPortIngQosQStatOffHiPrioOcts_Type = Counter64
_TmnxPortIngQosQStatOffHiPrioOcts_Object = MibTableColumn
tmnxPortIngQosQStatOffHiPrioOcts = _TmnxPortIngQosQStatOffHiPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 6),
    _TmnxPortIngQosQStatOffHiPrioOcts_Type()
)
tmnxPortIngQosQStatOffHiPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatOffHiPrioOcts.setStatus("current")
_TmnxPortIngQosQStatDpdHiPrioOcts_Type = Counter64
_TmnxPortIngQosQStatDpdHiPrioOcts_Object = MibTableColumn
tmnxPortIngQosQStatDpdHiPrioOcts = _TmnxPortIngQosQStatDpdHiPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 7),
    _TmnxPortIngQosQStatDpdHiPrioOcts_Type()
)
tmnxPortIngQosQStatDpdHiPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatDpdHiPrioOcts.setStatus("current")
_TmnxPortIngQosQStatOffLoPrioOcts_Type = Counter64
_TmnxPortIngQosQStatOffLoPrioOcts_Object = MibTableColumn
tmnxPortIngQosQStatOffLoPrioOcts = _TmnxPortIngQosQStatOffLoPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 8),
    _TmnxPortIngQosQStatOffLoPrioOcts_Type()
)
tmnxPortIngQosQStatOffLoPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatOffLoPrioOcts.setStatus("current")
_TmnxPortIngQosQStatDpdLoPrioOcts_Type = Counter64
_TmnxPortIngQosQStatDpdLoPrioOcts_Object = MibTableColumn
tmnxPortIngQosQStatDpdLoPrioOcts = _TmnxPortIngQosQStatDpdLoPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 9),
    _TmnxPortIngQosQStatDpdLoPrioOcts_Type()
)
tmnxPortIngQosQStatDpdLoPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatDpdLoPrioOcts.setStatus("current")
_TmnxPortIngQosQStatFwdInProfPkts_Type = Counter64
_TmnxPortIngQosQStatFwdInProfPkts_Object = MibTableColumn
tmnxPortIngQosQStatFwdInProfPkts = _TmnxPortIngQosQStatFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 10),
    _TmnxPortIngQosQStatFwdInProfPkts_Type()
)
tmnxPortIngQosQStatFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatFwdInProfPkts.setStatus("current")
_TmnxPortIngQosQStatFwdOutProfPkts_Type = Counter64
_TmnxPortIngQosQStatFwdOutProfPkts_Object = MibTableColumn
tmnxPortIngQosQStatFwdOutProfPkts = _TmnxPortIngQosQStatFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 11),
    _TmnxPortIngQosQStatFwdOutProfPkts_Type()
)
tmnxPortIngQosQStatFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatFwdOutProfPkts.setStatus("current")
_TmnxPortIngQosQStatFwdInProfOcts_Type = Counter64
_TmnxPortIngQosQStatFwdInProfOcts_Object = MibTableColumn
tmnxPortIngQosQStatFwdInProfOcts = _TmnxPortIngQosQStatFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 12),
    _TmnxPortIngQosQStatFwdInProfOcts_Type()
)
tmnxPortIngQosQStatFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatFwdInProfOcts.setStatus("current")
_TmnxPortIngQosQStatFwdOutProfOcts_Type = Counter64
_TmnxPortIngQosQStatFwdOutProfOcts_Object = MibTableColumn
tmnxPortIngQosQStatFwdOutProfOcts = _TmnxPortIngQosQStatFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 13),
    _TmnxPortIngQosQStatFwdOutProfOcts_Type()
)
tmnxPortIngQosQStatFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatFwdOutProfOcts.setStatus("current")
_TmnxPortIngQosQStatUncolPktsOff_Type = Counter64
_TmnxPortIngQosQStatUncolPktsOff_Object = MibTableColumn
tmnxPortIngQosQStatUncolPktsOff = _TmnxPortIngQosQStatUncolPktsOff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 14),
    _TmnxPortIngQosQStatUncolPktsOff_Type()
)
tmnxPortIngQosQStatUncolPktsOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatUncolPktsOff.setStatus("current")
_TmnxPortIngQosQStatUncolOctsOff_Type = Counter64
_TmnxPortIngQosQStatUncolOctsOff_Object = MibTableColumn
tmnxPortIngQosQStatUncolOctsOff = _TmnxPortIngQosQStatUncolOctsOff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 45, 1, 15),
    _TmnxPortIngQosQStatUncolOctsOff_Type()
)
tmnxPortIngQosQStatUncolOctsOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortIngQosQStatUncolOctsOff.setStatus("current")
_TmnxPortEgrQosQStatTable_Object = MibTable
tmnxPortEgrQosQStatTable = _TmnxPortEgrQosQStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 46)
)
if mibBuilder.loadTexts:
    tmnxPortEgrQosQStatTable.setStatus("current")
_TmnxPortEgrQosQStatEntry_Object = MibTableRow
tmnxPortEgrQosQStatEntry = _TmnxPortEgrQosQStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 46, 1)
)
tmnxPortEgrQosQStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortAccEgrQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortEgrQosQStatQueueId"),
)
if mibBuilder.loadTexts:
    tmnxPortEgrQosQStatEntry.setStatus("current")


class _TmnxPortEgrQosQStatQueueId_Type(TEgressQueueId):
    """Custom type tmnxPortEgrQosQStatQueueId based on TEgressQueueId"""
    subtypeSpec = TEgressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxPortEgrQosQStatQueueId_Type.__name__ = "TEgressQueueId"
_TmnxPortEgrQosQStatQueueId_Object = MibTableColumn
tmnxPortEgrQosQStatQueueId = _TmnxPortEgrQosQStatQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 46, 1, 1),
    _TmnxPortEgrQosQStatQueueId_Type()
)
tmnxPortEgrQosQStatQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortEgrQosQStatQueueId.setStatus("current")
_TmnxPortEgrQosQStatFwdInProfPkts_Type = Counter64
_TmnxPortEgrQosQStatFwdInProfPkts_Object = MibTableColumn
tmnxPortEgrQosQStatFwdInProfPkts = _TmnxPortEgrQosQStatFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 46, 1, 2),
    _TmnxPortEgrQosQStatFwdInProfPkts_Type()
)
tmnxPortEgrQosQStatFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrQosQStatFwdInProfPkts.setStatus("current")
_TmnxPortEgrQosQStatDpdInProfPkts_Type = Counter64
_TmnxPortEgrQosQStatDpdInProfPkts_Object = MibTableColumn
tmnxPortEgrQosQStatDpdInProfPkts = _TmnxPortEgrQosQStatDpdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 46, 1, 3),
    _TmnxPortEgrQosQStatDpdInProfPkts_Type()
)
tmnxPortEgrQosQStatDpdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrQosQStatDpdInProfPkts.setStatus("current")
_TmnxPortEgrQosQStatFwdOutProfPkts_Type = Counter64
_TmnxPortEgrQosQStatFwdOutProfPkts_Object = MibTableColumn
tmnxPortEgrQosQStatFwdOutProfPkts = _TmnxPortEgrQosQStatFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 46, 1, 4),
    _TmnxPortEgrQosQStatFwdOutProfPkts_Type()
)
tmnxPortEgrQosQStatFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrQosQStatFwdOutProfPkts.setStatus("current")
_TmnxPortEgrQosQStatDpdOutProfPkts_Type = Counter64
_TmnxPortEgrQosQStatDpdOutProfPkts_Object = MibTableColumn
tmnxPortEgrQosQStatDpdOutProfPkts = _TmnxPortEgrQosQStatDpdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 46, 1, 5),
    _TmnxPortEgrQosQStatDpdOutProfPkts_Type()
)
tmnxPortEgrQosQStatDpdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrQosQStatDpdOutProfPkts.setStatus("current")
_TmnxPortEgrQosQStatFwdInProfOcts_Type = Counter64
_TmnxPortEgrQosQStatFwdInProfOcts_Object = MibTableColumn
tmnxPortEgrQosQStatFwdInProfOcts = _TmnxPortEgrQosQStatFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 46, 1, 6),
    _TmnxPortEgrQosQStatFwdInProfOcts_Type()
)
tmnxPortEgrQosQStatFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrQosQStatFwdInProfOcts.setStatus("current")
_TmnxPortEgrQosQStatDpdInProfOcts_Type = Counter64
_TmnxPortEgrQosQStatDpdInProfOcts_Object = MibTableColumn
tmnxPortEgrQosQStatDpdInProfOcts = _TmnxPortEgrQosQStatDpdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 46, 1, 7),
    _TmnxPortEgrQosQStatDpdInProfOcts_Type()
)
tmnxPortEgrQosQStatDpdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrQosQStatDpdInProfOcts.setStatus("current")
_TmnxPortEgrQosQStatFwdOutProfOcts_Type = Counter64
_TmnxPortEgrQosQStatFwdOutProfOcts_Object = MibTableColumn
tmnxPortEgrQosQStatFwdOutProfOcts = _TmnxPortEgrQosQStatFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 46, 1, 8),
    _TmnxPortEgrQosQStatFwdOutProfOcts_Type()
)
tmnxPortEgrQosQStatFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrQosQStatFwdOutProfOcts.setStatus("current")
_TmnxPortEgrQosQStatDpdOutProfOcts_Type = Counter64
_TmnxPortEgrQosQStatDpdOutProfOcts_Object = MibTableColumn
tmnxPortEgrQosQStatDpdOutProfOcts = _TmnxPortEgrQosQStatDpdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 46, 1, 9),
    _TmnxPortEgrQosQStatDpdOutProfOcts_Type()
)
tmnxPortEgrQosQStatDpdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrQosQStatDpdOutProfOcts.setStatus("current")
_TmnxBundleMemberMlfrTable_Object = MibTable
tmnxBundleMemberMlfrTable = _TmnxBundleMemberMlfrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 47)
)
if mibBuilder.loadTexts:
    tmnxBundleMemberMlfrTable.setStatus("current")
_TmnxBundleMemberMlfrEntry_Object = MibTableRow
tmnxBundleMemberMlfrEntry = _TmnxBundleMemberMlfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 47, 1)
)
tmnxBundleMemberMlfrEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxBundleMemberMlfrEntry.setStatus("current")
_TmnxBundleMemberMlfrDownReason_Type = TmnxMlfrLinkDownReason
_TmnxBundleMemberMlfrDownReason_Object = MibTableColumn
tmnxBundleMemberMlfrDownReason = _TmnxBundleMemberMlfrDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 47, 1, 1),
    _TmnxBundleMemberMlfrDownReason_Type()
)
tmnxBundleMemberMlfrDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBundleMemberMlfrDownReason.setStatus("current")
_TmnxWaveTrackerTable_Object = MibTable
tmnxWaveTrackerTable = _TmnxWaveTrackerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48)
)
if mibBuilder.loadTexts:
    tmnxWaveTrackerTable.setStatus("current")
_TmnxWaveTrackerEntry_Object = MibTableRow
tmnxWaveTrackerEntry = _TmnxWaveTrackerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1)
)
tmnxWaveTrackerEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxWaveTrackerEntry.setStatus("current")


class _TmnxWaveTrackerPowerCtrlEnable_Type(TruthValue):
    """Custom type tmnxWaveTrackerPowerCtrlEnable based on TruthValue"""


_TmnxWaveTrackerPowerCtrlEnable_Object = MibTableColumn
tmnxWaveTrackerPowerCtrlEnable = _TmnxWaveTrackerPowerCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 1),
    _TmnxWaveTrackerPowerCtrlEnable_Type()
)
tmnxWaveTrackerPowerCtrlEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWaveTrackerPowerCtrlEnable.setStatus("current")


class _TmnxWaveTrackerEncodeEnable_Type(TruthValue):
    """Custom type tmnxWaveTrackerEncodeEnable based on TruthValue"""


_TmnxWaveTrackerEncodeEnable_Object = MibTableColumn
tmnxWaveTrackerEncodeEnable = _TmnxWaveTrackerEncodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 2),
    _TmnxWaveTrackerEncodeEnable_Type()
)
tmnxWaveTrackerEncodeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWaveTrackerEncodeEnable.setStatus("current")


class _TmnxWaveTrackerInUse_Type(TruthValue):
    """Custom type tmnxWaveTrackerInUse based on TruthValue"""


_TmnxWaveTrackerInUse_Object = MibTableColumn
tmnxWaveTrackerInUse = _TmnxWaveTrackerInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 3),
    _TmnxWaveTrackerInUse_Type()
)
tmnxWaveTrackerInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWaveTrackerInUse.setStatus("current")


class _TmnxWaveTrackerTargetPower_Type(Integer32):
    """Custom type tmnxWaveTrackerTargetPower based on Integer32"""
    defaultValue = -2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2200, 300),
    )


_TmnxWaveTrackerTargetPower_Type.__name__ = "Integer32"
_TmnxWaveTrackerTargetPower_Object = MibTableColumn
tmnxWaveTrackerTargetPower = _TmnxWaveTrackerTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 4),
    _TmnxWaveTrackerTargetPower_Type()
)
tmnxWaveTrackerTargetPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWaveTrackerTargetPower.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWaveTrackerTargetPower.setUnits("mBm")


class _TmnxWaveTrackerWaveKey1_Type(Unsigned32):
    """Custom type tmnxWaveTrackerWaveKey1 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TmnxWaveTrackerWaveKey1_Type.__name__ = "Unsigned32"
_TmnxWaveTrackerWaveKey1_Object = MibTableColumn
tmnxWaveTrackerWaveKey1 = _TmnxWaveTrackerWaveKey1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 5),
    _TmnxWaveTrackerWaveKey1_Type()
)
tmnxWaveTrackerWaveKey1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWaveTrackerWaveKey1.setStatus("current")


class _TmnxWaveTrackerWaveKey2_Type(Unsigned32):
    """Custom type tmnxWaveTrackerWaveKey2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TmnxWaveTrackerWaveKey2_Type.__name__ = "Unsigned32"
_TmnxWaveTrackerWaveKey2_Object = MibTableColumn
tmnxWaveTrackerWaveKey2 = _TmnxWaveTrackerWaveKey2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 6),
    _TmnxWaveTrackerWaveKey2_Type()
)
tmnxWaveTrackerWaveKey2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWaveTrackerWaveKey2.setStatus("current")


class _TmnxWaveTrackerTrailName_Type(SnmpAdminString):
    """Custom type tmnxWaveTrackerTrailName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxWaveTrackerTrailName_Type.__name__ = "SnmpAdminString"
_TmnxWaveTrackerTrailName_Object = MibTableColumn
tmnxWaveTrackerTrailName = _TmnxWaveTrackerTrailName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 7),
    _TmnxWaveTrackerTrailName_Type()
)
tmnxWaveTrackerTrailName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWaveTrackerTrailName.setStatus("current")


class _TmnxWaveTrackerCfgAlarms_Type(TmnxWaveTrackerAlarm):
    """Custom type tmnxWaveTrackerCfgAlarms based on TmnxWaveTrackerAlarm"""
    defaultBinValue = "111111"


_TmnxWaveTrackerCfgAlarms_Object = MibTableColumn
tmnxWaveTrackerCfgAlarms = _TmnxWaveTrackerCfgAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 8),
    _TmnxWaveTrackerCfgAlarms_Type()
)
tmnxWaveTrackerCfgAlarms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWaveTrackerCfgAlarms.setStatus("current")
_TmnxWaveTrackerAlarmState_Type = TmnxWaveTrackerAlarm
_TmnxWaveTrackerAlarmState_Object = MibTableColumn
tmnxWaveTrackerAlarmState = _TmnxWaveTrackerAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 9),
    _TmnxWaveTrackerAlarmState_Type()
)
tmnxWaveTrackerAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWaveTrackerAlarmState.setStatus("current")
_TmnxWaveTrackerMeasuredPower_Type = Integer32
_TmnxWaveTrackerMeasuredPower_Object = MibTableColumn
tmnxWaveTrackerMeasuredPower = _TmnxWaveTrackerMeasuredPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 10),
    _TmnxWaveTrackerMeasuredPower_Type()
)
tmnxWaveTrackerMeasuredPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWaveTrackerMeasuredPower.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWaveTrackerMeasuredPower.setUnits("mBm")
_TmnxWaveTrackerMaxAttainablePwr_Type = Integer32
_TmnxWaveTrackerMaxAttainablePwr_Object = MibTableColumn
tmnxWaveTrackerMaxAttainablePwr = _TmnxWaveTrackerMaxAttainablePwr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 11),
    _TmnxWaveTrackerMaxAttainablePwr_Type()
)
tmnxWaveTrackerMaxAttainablePwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWaveTrackerMaxAttainablePwr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWaveTrackerMaxAttainablePwr.setUnits("mBm")
_TmnxWaveTrackerMinAttainablePwr_Type = Integer32
_TmnxWaveTrackerMinAttainablePwr_Object = MibTableColumn
tmnxWaveTrackerMinAttainablePwr = _TmnxWaveTrackerMinAttainablePwr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 12),
    _TmnxWaveTrackerMinAttainablePwr_Type()
)
tmnxWaveTrackerMinAttainablePwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWaveTrackerMinAttainablePwr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWaveTrackerMinAttainablePwr.setUnits("mBm")
_TmnxWaveTrackerUpperPowerMargin_Type = Unsigned32
_TmnxWaveTrackerUpperPowerMargin_Object = MibTableColumn
tmnxWaveTrackerUpperPowerMargin = _TmnxWaveTrackerUpperPowerMargin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 13),
    _TmnxWaveTrackerUpperPowerMargin_Type()
)
tmnxWaveTrackerUpperPowerMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWaveTrackerUpperPowerMargin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWaveTrackerUpperPowerMargin.setUnits("mB")
_TmnxWaveTrackerLowerPowerMargin_Type = Unsigned32
_TmnxWaveTrackerLowerPowerMargin_Object = MibTableColumn
tmnxWaveTrackerLowerPowerMargin = _TmnxWaveTrackerLowerPowerMargin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 48, 1, 14),
    _TmnxWaveTrackerLowerPowerMargin_Type()
)
tmnxWaveTrackerLowerPowerMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWaveTrackerLowerPowerMargin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWaveTrackerLowerPowerMargin.setUnits("mB")
_TPortAccEgrQGrpHMTableLastChgd_Type = TimeStamp
_TPortAccEgrQGrpHMTableLastChgd_Object = MibScalar
tPortAccEgrQGrpHMTableLastChgd = _TPortAccEgrQGrpHMTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 49),
    _TPortAccEgrQGrpHMTableLastChgd_Type()
)
tPortAccEgrQGrpHMTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpHMTableLastChgd.setStatus("current")
_TPortAccEgrQGrpHostMatchTable_Object = MibTable
tPortAccEgrQGrpHostMatchTable = _TPortAccEgrQGrpHostMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 50)
)
if mibBuilder.loadTexts:
    tPortAccEgrQGrpHostMatchTable.setStatus("current")
_TPortAccEgrQGrpHostMatchEntry_Object = MibTableRow
tPortAccEgrQGrpHostMatchEntry = _TPortAccEgrQGrpHostMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 50, 1)
)
tPortAccEgrQGrpHostMatchEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortAccEgrQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tPortAccEgrQGrpHMIntDestId"),
    (0, "TIMETRA-PORT-MIB", "tPortAccEgrQGrpHMOrgString"),
)
if mibBuilder.loadTexts:
    tPortAccEgrQGrpHostMatchEntry.setStatus("current")
_TPortAccEgrQGrpHMIntDestId_Type = TmnxSubMgtIntDestId
_TPortAccEgrQGrpHMIntDestId_Object = MibTableColumn
tPortAccEgrQGrpHMIntDestId = _TPortAccEgrQGrpHMIntDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 50, 1, 1),
    _TPortAccEgrQGrpHMIntDestId_Type()
)
tPortAccEgrQGrpHMIntDestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpHMIntDestId.setStatus("current")
_TPortAccEgrQGrpHMOrgString_Type = TmnxSubMgtOrgStrOrZero
_TPortAccEgrQGrpHMOrgString_Object = MibTableColumn
tPortAccEgrQGrpHMOrgString = _TPortAccEgrQGrpHMOrgString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 50, 1, 2),
    _TPortAccEgrQGrpHMOrgString_Type()
)
tPortAccEgrQGrpHMOrgString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpHMOrgString.setStatus("current")
_TPortAccEgrQGrpHMRowStatus_Type = RowStatus
_TPortAccEgrQGrpHMRowStatus_Object = MibTableColumn
tPortAccEgrQGrpHMRowStatus = _TPortAccEgrQGrpHMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 50, 1, 3),
    _TPortAccEgrQGrpHMRowStatus_Type()
)
tPortAccEgrQGrpHMRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpHMRowStatus.setStatus("current")
_TPortAccEgrQGrpHMLastChgd_Type = TimeStamp
_TPortAccEgrQGrpHMLastChgd_Object = MibTableColumn
tPortAccEgrQGrpHMLastChgd = _TPortAccEgrQGrpHMLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 50, 1, 4),
    _TPortAccEgrQGrpHMLastChgd_Type()
)
tPortAccEgrQGrpHMLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrQGrpHMLastChgd.setStatus("current")
_TPortAccIngSchedStatTable_Object = MibTable
tPortAccIngSchedStatTable = _TPortAccIngSchedStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 51)
)
if mibBuilder.loadTexts:
    tPortAccIngSchedStatTable.setStatus("current")
_TPortAccIngSchedStatEntry_Object = MibTableRow
tPortAccIngSchedStatEntry = _TPortAccIngSchedStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 51, 1)
)
tPortAccIngSchedStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortAccIngQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tPortAccIngSchedStatName"),
)
if mibBuilder.loadTexts:
    tPortAccIngSchedStatEntry.setStatus("current")
_TPortAccIngSchedStatName_Type = TNamedItem
_TPortAccIngSchedStatName_Object = MibTableColumn
tPortAccIngSchedStatName = _TPortAccIngSchedStatName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 51, 1, 1),
    _TPortAccIngSchedStatName_Type()
)
tPortAccIngSchedStatName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortAccIngSchedStatName.setStatus("current")
_TPortAccIngSchedStatFwdPkts_Type = Counter64
_TPortAccIngSchedStatFwdPkts_Object = MibTableColumn
tPortAccIngSchedStatFwdPkts = _TPortAccIngSchedStatFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 51, 1, 2),
    _TPortAccIngSchedStatFwdPkts_Type()
)
tPortAccIngSchedStatFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccIngSchedStatFwdPkts.setStatus("current")
_TPortAccIngSchedStatFwdPktsHi_Type = Counter32
_TPortAccIngSchedStatFwdPktsHi_Object = MibTableColumn
tPortAccIngSchedStatFwdPktsHi = _TPortAccIngSchedStatFwdPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 51, 1, 3),
    _TPortAccIngSchedStatFwdPktsHi_Type()
)
tPortAccIngSchedStatFwdPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccIngSchedStatFwdPktsHi.setStatus("current")
_TPortAccIngSchedStatFwdPktsLo_Type = Counter32
_TPortAccIngSchedStatFwdPktsLo_Object = MibTableColumn
tPortAccIngSchedStatFwdPktsLo = _TPortAccIngSchedStatFwdPktsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 51, 1, 4),
    _TPortAccIngSchedStatFwdPktsLo_Type()
)
tPortAccIngSchedStatFwdPktsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccIngSchedStatFwdPktsLo.setStatus("current")
_TPortAccIngSchedStatFwdOcts_Type = Counter64
_TPortAccIngSchedStatFwdOcts_Object = MibTableColumn
tPortAccIngSchedStatFwdOcts = _TPortAccIngSchedStatFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 51, 1, 5),
    _TPortAccIngSchedStatFwdOcts_Type()
)
tPortAccIngSchedStatFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccIngSchedStatFwdOcts.setStatus("current")
_TPortAccIngSchedStatFwdOctsHi_Type = Counter32
_TPortAccIngSchedStatFwdOctsHi_Object = MibTableColumn
tPortAccIngSchedStatFwdOctsHi = _TPortAccIngSchedStatFwdOctsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 51, 1, 6),
    _TPortAccIngSchedStatFwdOctsHi_Type()
)
tPortAccIngSchedStatFwdOctsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccIngSchedStatFwdOctsHi.setStatus("current")
_TPortAccIngSchedStatFwdOctsLo_Type = Counter32
_TPortAccIngSchedStatFwdOctsLo_Object = MibTableColumn
tPortAccIngSchedStatFwdOctsLo = _TPortAccIngSchedStatFwdOctsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 51, 1, 7),
    _TPortAccIngSchedStatFwdOctsLo_Type()
)
tPortAccIngSchedStatFwdOctsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccIngSchedStatFwdOctsLo.setStatus("current")
_TPortAccEgrSchedStatTable_Object = MibTable
tPortAccEgrSchedStatTable = _TPortAccEgrSchedStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 52)
)
if mibBuilder.loadTexts:
    tPortAccEgrSchedStatTable.setStatus("current")
_TPortAccEgrSchedStatEntry_Object = MibTableRow
tPortAccEgrSchedStatEntry = _TPortAccEgrSchedStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 52, 1)
)
tPortAccEgrSchedStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortAccEgrQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tPortAccEgrSchedStatName"),
)
if mibBuilder.loadTexts:
    tPortAccEgrSchedStatEntry.setStatus("current")
_TPortAccEgrSchedStatName_Type = TNamedItem
_TPortAccEgrSchedStatName_Object = MibTableColumn
tPortAccEgrSchedStatName = _TPortAccEgrSchedStatName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 52, 1, 1),
    _TPortAccEgrSchedStatName_Type()
)
tPortAccEgrSchedStatName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortAccEgrSchedStatName.setStatus("current")
_TPortAccEgrSchedStatFwdPkts_Type = Counter64
_TPortAccEgrSchedStatFwdPkts_Object = MibTableColumn
tPortAccEgrSchedStatFwdPkts = _TPortAccEgrSchedStatFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 52, 1, 2),
    _TPortAccEgrSchedStatFwdPkts_Type()
)
tPortAccEgrSchedStatFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrSchedStatFwdPkts.setStatus("current")
_TPortAccEgrSchedStatFwdPktsHi_Type = Counter32
_TPortAccEgrSchedStatFwdPktsHi_Object = MibTableColumn
tPortAccEgrSchedStatFwdPktsHi = _TPortAccEgrSchedStatFwdPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 52, 1, 3),
    _TPortAccEgrSchedStatFwdPktsHi_Type()
)
tPortAccEgrSchedStatFwdPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrSchedStatFwdPktsHi.setStatus("current")
_TPortAccEgrSchedStatFwdPktsLo_Type = Counter32
_TPortAccEgrSchedStatFwdPktsLo_Object = MibTableColumn
tPortAccEgrSchedStatFwdPktsLo = _TPortAccEgrSchedStatFwdPktsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 52, 1, 4),
    _TPortAccEgrSchedStatFwdPktsLo_Type()
)
tPortAccEgrSchedStatFwdPktsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrSchedStatFwdPktsLo.setStatus("current")
_TPortAccEgrSchedStatFwdOcts_Type = Counter64
_TPortAccEgrSchedStatFwdOcts_Object = MibTableColumn
tPortAccEgrSchedStatFwdOcts = _TPortAccEgrSchedStatFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 52, 1, 5),
    _TPortAccEgrSchedStatFwdOcts_Type()
)
tPortAccEgrSchedStatFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrSchedStatFwdOcts.setStatus("current")
_TPortAccEgrSchedStatFwdOctsHi_Type = Counter32
_TPortAccEgrSchedStatFwdOctsHi_Object = MibTableColumn
tPortAccEgrSchedStatFwdOctsHi = _TPortAccEgrSchedStatFwdOctsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 52, 1, 6),
    _TPortAccEgrSchedStatFwdOctsHi_Type()
)
tPortAccEgrSchedStatFwdOctsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrSchedStatFwdOctsHi.setStatus("current")
_TPortAccEgrSchedStatFwdOctsLo_Type = Counter32
_TPortAccEgrSchedStatFwdOctsLo_Object = MibTableColumn
tPortAccEgrSchedStatFwdOctsLo = _TPortAccEgrSchedStatFwdOctsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 52, 1, 7),
    _TPortAccEgrSchedStatFwdOctsLo_Type()
)
tPortAccEgrSchedStatFwdOctsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortAccEgrSchedStatFwdOctsLo.setStatus("current")
_TPortNetEgrSchedStatTable_Object = MibTable
tPortNetEgrSchedStatTable = _TPortNetEgrSchedStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 53)
)
if mibBuilder.loadTexts:
    tPortNetEgrSchedStatTable.setStatus("current")
_TPortNetEgrSchedStatEntry_Object = MibTableRow
tPortNetEgrSchedStatEntry = _TPortNetEgrSchedStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 53, 1)
)
tPortNetEgrSchedStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpInstanceId"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrSchedStatName"),
)
if mibBuilder.loadTexts:
    tPortNetEgrSchedStatEntry.setStatus("current")
_TPortNetEgrSchedStatName_Type = TNamedItem
_TPortNetEgrSchedStatName_Object = MibTableColumn
tPortNetEgrSchedStatName = _TPortNetEgrSchedStatName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 53, 1, 1),
    _TPortNetEgrSchedStatName_Type()
)
tPortNetEgrSchedStatName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortNetEgrSchedStatName.setStatus("current")
_TPortNetEgrSchedStatFwdPkts_Type = Counter64
_TPortNetEgrSchedStatFwdPkts_Object = MibTableColumn
tPortNetEgrSchedStatFwdPkts = _TPortNetEgrSchedStatFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 53, 1, 2),
    _TPortNetEgrSchedStatFwdPkts_Type()
)
tPortNetEgrSchedStatFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrSchedStatFwdPkts.setStatus("current")
_TPortNetEgrSchedStatFwdPktsHi_Type = Counter32
_TPortNetEgrSchedStatFwdPktsHi_Object = MibTableColumn
tPortNetEgrSchedStatFwdPktsHi = _TPortNetEgrSchedStatFwdPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 53, 1, 3),
    _TPortNetEgrSchedStatFwdPktsHi_Type()
)
tPortNetEgrSchedStatFwdPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrSchedStatFwdPktsHi.setStatus("current")
_TPortNetEgrSchedStatFwdPktsLo_Type = Counter32
_TPortNetEgrSchedStatFwdPktsLo_Object = MibTableColumn
tPortNetEgrSchedStatFwdPktsLo = _TPortNetEgrSchedStatFwdPktsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 53, 1, 4),
    _TPortNetEgrSchedStatFwdPktsLo_Type()
)
tPortNetEgrSchedStatFwdPktsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrSchedStatFwdPktsLo.setStatus("current")
_TPortNetEgrSchedStatFwdOcts_Type = Counter64
_TPortNetEgrSchedStatFwdOcts_Object = MibTableColumn
tPortNetEgrSchedStatFwdOcts = _TPortNetEgrSchedStatFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 53, 1, 5),
    _TPortNetEgrSchedStatFwdOcts_Type()
)
tPortNetEgrSchedStatFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrSchedStatFwdOcts.setStatus("current")
_TPortNetEgrSchedStatFwdOctsHi_Type = Counter32
_TPortNetEgrSchedStatFwdOctsHi_Object = MibTableColumn
tPortNetEgrSchedStatFwdOctsHi = _TPortNetEgrSchedStatFwdOctsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 53, 1, 6),
    _TPortNetEgrSchedStatFwdOctsHi_Type()
)
tPortNetEgrSchedStatFwdOctsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrSchedStatFwdOctsHi.setStatus("current")
_TPortNetEgrSchedStatFwdOctsLo_Type = Counter32
_TPortNetEgrSchedStatFwdOctsLo_Object = MibTableColumn
tPortNetEgrSchedStatFwdOctsLo = _TPortNetEgrSchedStatFwdOctsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 53, 1, 7),
    _TPortNetEgrSchedStatFwdOctsLo_Type()
)
tPortNetEgrSchedStatFwdOctsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrSchedStatFwdOctsLo.setStatus("current")
_TPortEgrVPortTableLastChgd_Type = TimeStamp
_TPortEgrVPortTableLastChgd_Object = MibScalar
tPortEgrVPortTableLastChgd = _TPortEgrVPortTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 54),
    _TPortEgrVPortTableLastChgd_Type()
)
tPortEgrVPortTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPortTableLastChgd.setStatus("current")
_TPortEgrVPortTable_Object = MibTable
tPortEgrVPortTable = _TPortEgrVPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 55)
)
if mibBuilder.loadTexts:
    tPortEgrVPortTable.setStatus("current")
_TPortEgrVPortEntry_Object = MibTableRow
tPortEgrVPortEntry = _TPortEgrVPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 55, 1)
)
tPortEgrVPortEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortEgrVPortName"),
)
if mibBuilder.loadTexts:
    tPortEgrVPortEntry.setStatus("current")
_TPortEgrVPortName_Type = TNamedItem
_TPortEgrVPortName_Object = MibTableColumn
tPortEgrVPortName = _TPortEgrVPortName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 55, 1, 1),
    _TPortEgrVPortName_Type()
)
tPortEgrVPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortEgrVPortName.setStatus("current")
_TPortEgrVPortRowStatus_Type = RowStatus
_TPortEgrVPortRowStatus_Object = MibTableColumn
tPortEgrVPortRowStatus = _TPortEgrVPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 55, 1, 2),
    _TPortEgrVPortRowStatus_Type()
)
tPortEgrVPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortEgrVPortRowStatus.setStatus("current")
_TPortEgrVPortLastChanged_Type = TimeStamp
_TPortEgrVPortLastChanged_Object = MibTableColumn
tPortEgrVPortLastChanged = _TPortEgrVPortLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 55, 1, 3),
    _TPortEgrVPortLastChanged_Type()
)
tPortEgrVPortLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPortLastChanged.setStatus("current")


class _TPortEgrVPortDescr_Type(TItemDescription):
    """Custom type tPortEgrVPortDescr based on TItemDescription"""
    defaultHexValue = ""


_TPortEgrVPortDescr_Object = MibTableColumn
tPortEgrVPortDescr = _TPortEgrVPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 55, 1, 4),
    _TPortEgrVPortDescr_Type()
)
tPortEgrVPortDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortEgrVPortDescr.setStatus("current")


class _TPortEgrVPortSchedPol_Type(TNamedItemOrEmpty):
    """Custom type tPortEgrVPortSchedPol based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortEgrVPortSchedPol_Object = MibTableColumn
tPortEgrVPortSchedPol = _TPortEgrVPortSchedPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 55, 1, 5),
    _TPortEgrVPortSchedPol_Type()
)
tPortEgrVPortSchedPol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortEgrVPortSchedPol.setStatus("current")


class _TPortEgrVPortAggRateLimit_Type(TPortSchedulerPIR):
    """Custom type tPortEgrVPortAggRateLimit based on TPortSchedulerPIR"""
    defaultValue = -1


_TPortEgrVPortAggRateLimit_Object = MibTableColumn
tPortEgrVPortAggRateLimit = _TPortEgrVPortAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 55, 1, 6),
    _TPortEgrVPortAggRateLimit_Type()
)
tPortEgrVPortAggRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortEgrVPortAggRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tPortEgrVPortAggRateLimit.setUnits("kbps")
_TPortEgrVPortHMTableLastChgd_Type = TimeStamp
_TPortEgrVPortHMTableLastChgd_Object = MibScalar
tPortEgrVPortHMTableLastChgd = _TPortEgrVPortHMTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 56),
    _TPortEgrVPortHMTableLastChgd_Type()
)
tPortEgrVPortHMTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPortHMTableLastChgd.setStatus("current")
_TPortEgrVPortHostMatchTable_Object = MibTable
tPortEgrVPortHostMatchTable = _TPortEgrVPortHostMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 57)
)
if mibBuilder.loadTexts:
    tPortEgrVPortHostMatchTable.setStatus("current")
_TPortEgrVPortHostMatchEntry_Object = MibTableRow
tPortEgrVPortHostMatchEntry = _TPortEgrVPortHostMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 57, 1)
)
tPortEgrVPortHostMatchEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortEgrVPortName"),
    (0, "TIMETRA-PORT-MIB", "tPortEgrVPortHMIntDestId"),
    (0, "TIMETRA-PORT-MIB", "tPortEgrVPortHMOrgString"),
)
if mibBuilder.loadTexts:
    tPortEgrVPortHostMatchEntry.setStatus("current")
_TPortEgrVPortHMIntDestId_Type = TmnxSubMgtIntDestId
_TPortEgrVPortHMIntDestId_Object = MibTableColumn
tPortEgrVPortHMIntDestId = _TPortEgrVPortHMIntDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 57, 1, 1),
    _TPortEgrVPortHMIntDestId_Type()
)
tPortEgrVPortHMIntDestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortEgrVPortHMIntDestId.setStatus("current")
_TPortEgrVPortHMOrgString_Type = TmnxSubMgtOrgStrOrZero
_TPortEgrVPortHMOrgString_Object = MibTableColumn
tPortEgrVPortHMOrgString = _TPortEgrVPortHMOrgString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 57, 1, 2),
    _TPortEgrVPortHMOrgString_Type()
)
tPortEgrVPortHMOrgString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortEgrVPortHMOrgString.setStatus("current")
_TPortEgrVPortHMRowStatus_Type = RowStatus
_TPortEgrVPortHMRowStatus_Object = MibTableColumn
tPortEgrVPortHMRowStatus = _TPortEgrVPortHMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 57, 1, 3),
    _TPortEgrVPortHMRowStatus_Type()
)
tPortEgrVPortHMRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortEgrVPortHMRowStatus.setStatus("current")
_TPortEgrVPortHMLastChgd_Type = TimeStamp
_TPortEgrVPortHMLastChgd_Object = MibTableColumn
tPortEgrVPortHMLastChgd = _TPortEgrVPortHMLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 57, 1, 4),
    _TPortEgrVPortHMLastChgd_Type()
)
tPortEgrVPortHMLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPortHMLastChgd.setStatus("current")
_TmnxOpticalPortCfgTable_Object = MibTable
tmnxOpticalPortCfgTable = _TmnxOpticalPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 58)
)
if mibBuilder.loadTexts:
    tmnxOpticalPortCfgTable.setStatus("current")
_TmnxOpticalPortCfgEntry_Object = MibTableRow
tmnxOpticalPortCfgEntry = _TmnxOpticalPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 58, 1)
)
tmnxOpticalPortCfgEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxOpticalPortCfgEntry.setStatus("current")


class _TmnxOpticalPortAmpCfgAlarms_Type(TmnxOpticalAmpAlarm):
    """Custom type tmnxOpticalPortAmpCfgAlarms based on TmnxOpticalAmpAlarm"""
    defaultBinValue = "1111111"


_TmnxOpticalPortAmpCfgAlarms_Object = MibTableColumn
tmnxOpticalPortAmpCfgAlarms = _TmnxOpticalPortAmpCfgAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 58, 1, 1),
    _TmnxOpticalPortAmpCfgAlarms_Type()
)
tmnxOpticalPortAmpCfgAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpCfgAlarms.setStatus("current")


class _TmnxOpticalPortTdcmCtrlMode_Type(TmnxOpticalTdcmCtrlMode):
    """Custom type tmnxOpticalPortTdcmCtrlMode based on TmnxOpticalTdcmCtrlMode"""


_TmnxOpticalPortTdcmCtrlMode_Object = MibTableColumn
tmnxOpticalPortTdcmCtrlMode = _TmnxOpticalPortTdcmCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 58, 1, 2),
    _TmnxOpticalPortTdcmCtrlMode_Type()
)
tmnxOpticalPortTdcmCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmCtrlMode.setStatus("current")


class _TmnxOpticalPortTdcmManCfgDisp_Type(Integer32):
    """Custom type tmnxOpticalPortTdcmManCfgDisp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1200, 1200),
    )


_TmnxOpticalPortTdcmManCfgDisp_Type.__name__ = "Integer32"
_TmnxOpticalPortTdcmManCfgDisp_Object = MibTableColumn
tmnxOpticalPortTdcmManCfgDisp = _TmnxOpticalPortTdcmManCfgDisp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 58, 1, 3),
    _TmnxOpticalPortTdcmManCfgDisp_Type()
)
tmnxOpticalPortTdcmManCfgDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmManCfgDisp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmManCfgDisp.setUnits("picoseconds per nanometer")


class _TmnxOpticalPortTdcmCfgRxChan_Type(TmnxOpticalDwdmChannel):
    """Custom type tmnxOpticalPortTdcmCfgRxChan based on TmnxOpticalDwdmChannel"""
    defaultValue = 0


_TmnxOpticalPortTdcmCfgRxChan_Object = MibTableColumn
tmnxOpticalPortTdcmCfgRxChan = _TmnxOpticalPortTdcmCfgRxChan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 58, 1, 4),
    _TmnxOpticalPortTdcmCfgRxChan_Type()
)
tmnxOpticalPortTdcmCfgRxChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmCfgRxChan.setStatus("current")


class _TmnxOpticalPortTdcmCfgAlarms_Type(TmnxOpticalTdcmAlarm):
    """Custom type tmnxOpticalPortTdcmCfgAlarms based on TmnxOpticalTdcmAlarm"""
    defaultBinValue = "1111111"


_TmnxOpticalPortTdcmCfgAlarms_Object = MibTableColumn
tmnxOpticalPortTdcmCfgAlarms = _TmnxOpticalPortTdcmCfgAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 58, 1, 5),
    _TmnxOpticalPortTdcmCfgAlarms_Type()
)
tmnxOpticalPortTdcmCfgAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmCfgAlarms.setStatus("current")


class _TmnxOpticalPortTdcmDispSwpStart_Type(Integer32):
    """Custom type tmnxOpticalPortTdcmDispSwpStart based on Integer32"""
    defaultValue = -1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1200, 1200),
    )


_TmnxOpticalPortTdcmDispSwpStart_Type.__name__ = "Integer32"
_TmnxOpticalPortTdcmDispSwpStart_Object = MibTableColumn
tmnxOpticalPortTdcmDispSwpStart = _TmnxOpticalPortTdcmDispSwpStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 58, 1, 6),
    _TmnxOpticalPortTdcmDispSwpStart_Type()
)
tmnxOpticalPortTdcmDispSwpStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmDispSwpStart.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmDispSwpStart.setUnits("picoseconds per nanometer")


class _TmnxOpticalPortTdcmDispSwpEnd_Type(Integer32):
    """Custom type tmnxOpticalPortTdcmDispSwpEnd based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1200, 1200),
    )


_TmnxOpticalPortTdcmDispSwpEnd_Type.__name__ = "Integer32"
_TmnxOpticalPortTdcmDispSwpEnd_Object = MibTableColumn
tmnxOpticalPortTdcmDispSwpEnd = _TmnxOpticalPortTdcmDispSwpEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 58, 1, 7),
    _TmnxOpticalPortTdcmDispSwpEnd_Type()
)
tmnxOpticalPortTdcmDispSwpEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmDispSwpEnd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmDispSwpEnd.setUnits("picoseconds per nanometer")
_TmnxOpticalPortOperTable_Object = MibTable
tmnxOpticalPortOperTable = _TmnxOpticalPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59)
)
if mibBuilder.loadTexts:
    tmnxOpticalPortOperTable.setStatus("current")
_TmnxOpticalPortOperEntry_Object = MibTableRow
tmnxOpticalPortOperEntry = _TmnxOpticalPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1)
)
tmnxOpticalPortOperEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxOpticalPortOperEntry.setStatus("current")
_TmnxOpticalPortHasRxAmplifier_Type = TruthValue
_TmnxOpticalPortHasRxAmplifier_Object = MibTableColumn
tmnxOpticalPortHasRxAmplifier = _TmnxOpticalPortHasRxAmplifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 1),
    _TmnxOpticalPortHasRxAmplifier_Type()
)
tmnxOpticalPortHasRxAmplifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortHasRxAmplifier.setStatus("current")
_TmnxOpticalPortHasRxTdcm_Type = TruthValue
_TmnxOpticalPortHasRxTdcm_Object = MibTableColumn
tmnxOpticalPortHasRxTdcm = _TmnxOpticalPortHasRxTdcm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 2),
    _TmnxOpticalPortHasRxTdcm_Type()
)
tmnxOpticalPortHasRxTdcm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortHasRxTdcm.setStatus("current")
_TmnxOpticalPortAmpPowerIn_Type = Integer32
_TmnxOpticalPortAmpPowerIn_Object = MibTableColumn
tmnxOpticalPortAmpPowerIn = _TmnxOpticalPortAmpPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 3),
    _TmnxOpticalPortAmpPowerIn_Type()
)
tmnxOpticalPortAmpPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpPowerIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpPowerIn.setUnits("mBm")
_TmnxOpticalPortAmpGain_Type = Unsigned32
_TmnxOpticalPortAmpGain_Object = MibTableColumn
tmnxOpticalPortAmpGain = _TmnxOpticalPortAmpGain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 4),
    _TmnxOpticalPortAmpGain_Type()
)
tmnxOpticalPortAmpGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpGain.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpGain.setUnits("mB")
_TmnxOpticalPortAmpPowerOut_Type = Integer32
_TmnxOpticalPortAmpPowerOut_Object = MibTableColumn
tmnxOpticalPortAmpPowerOut = _TmnxOpticalPortAmpPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 5),
    _TmnxOpticalPortAmpPowerOut_Type()
)
tmnxOpticalPortAmpPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpPowerOut.setUnits("mBm")
_TmnxOpticalPortAmpPumpTemp_Type = Integer32
_TmnxOpticalPortAmpPumpTemp_Object = MibTableColumn
tmnxOpticalPortAmpPumpTemp = _TmnxOpticalPortAmpPumpTemp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 6),
    _TmnxOpticalPortAmpPumpTemp_Type()
)
tmnxOpticalPortAmpPumpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpPumpTemp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpPumpTemp.setUnits("millidegrees Celsius")
_TmnxOpticalPortAmpModuleTemp_Type = Integer32
_TmnxOpticalPortAmpModuleTemp_Object = MibTableColumn
tmnxOpticalPortAmpModuleTemp = _TmnxOpticalPortAmpModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 7),
    _TmnxOpticalPortAmpModuleTemp_Type()
)
tmnxOpticalPortAmpModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpModuleTemp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpModuleTemp.setUnits("millidegrees Celsius")
_TmnxOpticalPortAmpPumpCurrent_Type = Unsigned32
_TmnxOpticalPortAmpPumpCurrent_Object = MibTableColumn
tmnxOpticalPortAmpPumpCurrent = _TmnxOpticalPortAmpPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 8),
    _TmnxOpticalPortAmpPumpCurrent_Type()
)
tmnxOpticalPortAmpPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpPumpCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpPumpCurrent.setUnits("microAmperes")
_TmnxOpticalPortAmpAlarmState_Type = TmnxOpticalAmpAlarm
_TmnxOpticalPortAmpAlarmState_Object = MibTableColumn
tmnxOpticalPortAmpAlarmState = _TmnxOpticalPortAmpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 9),
    _TmnxOpticalPortAmpAlarmState_Type()
)
tmnxOpticalPortAmpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpAlarmState.setStatus("current")


class _TmnxOpticalPortAmpSerialNum_Type(SnmpAdminString):
    """Custom type tmnxOpticalPortAmpSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TmnxOpticalPortAmpSerialNum_Type.__name__ = "SnmpAdminString"
_TmnxOpticalPortAmpSerialNum_Object = MibTableColumn
tmnxOpticalPortAmpSerialNum = _TmnxOpticalPortAmpSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 10),
    _TmnxOpticalPortAmpSerialNum_Type()
)
tmnxOpticalPortAmpSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpSerialNum.setStatus("current")
_TmnxOpticalPortAmpCtrlState_Type = TmnxOpticalAmpCtrlState
_TmnxOpticalPortAmpCtrlState_Object = MibTableColumn
tmnxOpticalPortAmpCtrlState = _TmnxOpticalPortAmpCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 11),
    _TmnxOpticalPortAmpCtrlState_Type()
)
tmnxOpticalPortAmpCtrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortAmpCtrlState.setStatus("current")
_TmnxOpticalPortTdcmPowerIn_Type = Integer32
_TmnxOpticalPortTdcmPowerIn_Object = MibTableColumn
tmnxOpticalPortTdcmPowerIn = _TmnxOpticalPortTdcmPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 12),
    _TmnxOpticalPortTdcmPowerIn_Type()
)
tmnxOpticalPortTdcmPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmPowerIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmPowerIn.setUnits("mBm")
_TmnxOpticalPortTdcmLoss_Type = Unsigned32
_TmnxOpticalPortTdcmLoss_Object = MibTableColumn
tmnxOpticalPortTdcmLoss = _TmnxOpticalPortTdcmLoss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 13),
    _TmnxOpticalPortTdcmLoss_Type()
)
tmnxOpticalPortTdcmLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmLoss.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmLoss.setUnits("mB")
_TmnxOpticalPortTdcmPowerOut_Type = Integer32
_TmnxOpticalPortTdcmPowerOut_Object = MibTableColumn
tmnxOpticalPortTdcmPowerOut = _TmnxOpticalPortTdcmPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 14),
    _TmnxOpticalPortTdcmPowerOut_Type()
)
tmnxOpticalPortTdcmPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmPowerOut.setUnits("mBm")
_TmnxOpticalPortTdcmRtd1Temp_Type = Integer32
_TmnxOpticalPortTdcmRtd1Temp_Object = MibTableColumn
tmnxOpticalPortTdcmRtd1Temp = _TmnxOpticalPortTdcmRtd1Temp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 15),
    _TmnxOpticalPortTdcmRtd1Temp_Type()
)
tmnxOpticalPortTdcmRtd1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmRtd1Temp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmRtd1Temp.setUnits("millidegrees Celsius")
_TmnxOpticalPortTdcmRtd2Temp_Type = Integer32
_TmnxOpticalPortTdcmRtd2Temp_Object = MibTableColumn
tmnxOpticalPortTdcmRtd2Temp = _TmnxOpticalPortTdcmRtd2Temp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 16),
    _TmnxOpticalPortTdcmRtd2Temp_Type()
)
tmnxOpticalPortTdcmRtd2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmRtd2Temp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmRtd2Temp.setUnits("millidegrees Celsius")
_TmnxOpticalPortTdcmRtd3Temp_Type = Integer32
_TmnxOpticalPortTdcmRtd3Temp_Object = MibTableColumn
tmnxOpticalPortTdcmRtd3Temp = _TmnxOpticalPortTdcmRtd3Temp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 17),
    _TmnxOpticalPortTdcmRtd3Temp_Type()
)
tmnxOpticalPortTdcmRtd3Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmRtd3Temp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmRtd3Temp.setUnits("millidegrees Celsius")
_TmnxOpticalPortTdcmRtd4Temp_Type = Integer32
_TmnxOpticalPortTdcmRtd4Temp_Object = MibTableColumn
tmnxOpticalPortTdcmRtd4Temp = _TmnxOpticalPortTdcmRtd4Temp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 18),
    _TmnxOpticalPortTdcmRtd4Temp_Type()
)
tmnxOpticalPortTdcmRtd4Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmRtd4Temp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmRtd4Temp.setUnits("millidegrees Celsius")
_TmnxOpticalPortTdcmModuleTemp_Type = Integer32
_TmnxOpticalPortTdcmModuleTemp_Object = MibTableColumn
tmnxOpticalPortTdcmModuleTemp = _TmnxOpticalPortTdcmModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 19),
    _TmnxOpticalPortTdcmModuleTemp_Type()
)
tmnxOpticalPortTdcmModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmModuleTemp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmModuleTemp.setUnits("millidegrees Celsius")
_TmnxOpticalPortTdcmMinDisp_Type = Integer32
_TmnxOpticalPortTdcmMinDisp_Object = MibTableColumn
tmnxOpticalPortTdcmMinDisp = _TmnxOpticalPortTdcmMinDisp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 20),
    _TmnxOpticalPortTdcmMinDisp_Type()
)
tmnxOpticalPortTdcmMinDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmMinDisp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmMinDisp.setUnits("picoseconds per nanometer")
_TmnxOpticalPortTdcmMaxDisp_Type = Integer32
_TmnxOpticalPortTdcmMaxDisp_Object = MibTableColumn
tmnxOpticalPortTdcmMaxDisp = _TmnxOpticalPortTdcmMaxDisp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 21),
    _TmnxOpticalPortTdcmMaxDisp_Type()
)
tmnxOpticalPortTdcmMaxDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmMaxDisp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmMaxDisp.setUnits("picoseconds per nanometer")
_TmnxOpticalPortTdcmAutoDisp_Type = Integer32
_TmnxOpticalPortTdcmAutoDisp_Object = MibTableColumn
tmnxOpticalPortTdcmAutoDisp = _TmnxOpticalPortTdcmAutoDisp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 22),
    _TmnxOpticalPortTdcmAutoDisp_Type()
)
tmnxOpticalPortTdcmAutoDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmAutoDisp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmAutoDisp.setUnits("picoseconds per nanometer")
_TmnxOpticalPortTdcmMeasDisp_Type = Integer32
_TmnxOpticalPortTdcmMeasDisp_Object = MibTableColumn
tmnxOpticalPortTdcmMeasDisp = _TmnxOpticalPortTdcmMeasDisp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 23),
    _TmnxOpticalPortTdcmMeasDisp_Type()
)
tmnxOpticalPortTdcmMeasDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmMeasDisp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmMeasDisp.setUnits("picoseconds per nanometer")
_TmnxOpticalPortTdcmPresRxChan_Type = TmnxOpticalDwdmChannel
_TmnxOpticalPortTdcmPresRxChan_Object = MibTableColumn
tmnxOpticalPortTdcmPresRxChan = _TmnxOpticalPortTdcmPresRxChan_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 24),
    _TmnxOpticalPortTdcmPresRxChan_Type()
)
tmnxOpticalPortTdcmPresRxChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmPresRxChan.setStatus("current")
_TmnxOpticalPortTdcmAlarmState_Type = TmnxOpticalTdcmAlarm
_TmnxOpticalPortTdcmAlarmState_Object = MibTableColumn
tmnxOpticalPortTdcmAlarmState = _TmnxOpticalPortTdcmAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 25),
    _TmnxOpticalPortTdcmAlarmState_Type()
)
tmnxOpticalPortTdcmAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmAlarmState.setStatus("current")


class _TmnxOpticalPortTdcmSerialNum_Type(SnmpAdminString):
    """Custom type tmnxOpticalPortTdcmSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TmnxOpticalPortTdcmSerialNum_Type.__name__ = "SnmpAdminString"
_TmnxOpticalPortTdcmSerialNum_Object = MibTableColumn
tmnxOpticalPortTdcmSerialNum = _TmnxOpticalPortTdcmSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 26),
    _TmnxOpticalPortTdcmSerialNum_Type()
)
tmnxOpticalPortTdcmSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmSerialNum.setStatus("current")
_TmnxOpticalPortTdcmCtrlState_Type = TmnxOpticalTdcmCtrlState
_TmnxOpticalPortTdcmCtrlState_Object = MibTableColumn
tmnxOpticalPortTdcmCtrlState = _TmnxOpticalPortTdcmCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 27),
    _TmnxOpticalPortTdcmCtrlState_Type()
)
tmnxOpticalPortTdcmCtrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortTdcmCtrlState.setStatus("current")
_TmnxOpticalPortDwdmChannelMin_Type = TmnxOpticalDwdmChannel
_TmnxOpticalPortDwdmChannelMin_Object = MibTableColumn
tmnxOpticalPortDwdmChannelMin = _TmnxOpticalPortDwdmChannelMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 28),
    _TmnxOpticalPortDwdmChannelMin_Type()
)
tmnxOpticalPortDwdmChannelMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortDwdmChannelMin.setStatus("current")
_TmnxOpticalPortDwdmChannelMax_Type = TmnxOpticalDwdmChannel
_TmnxOpticalPortDwdmChannelMax_Object = MibTableColumn
tmnxOpticalPortDwdmChannelMax = _TmnxOpticalPortDwdmChannelMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 29),
    _TmnxOpticalPortDwdmChannelMax_Type()
)
tmnxOpticalPortDwdmChannelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortDwdmChannelMax.setStatus("current")


class _TmnxOpticalPortLaserTunability_Type(Integer32):
    """Custom type tmnxOpticalPortLaserTunability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullyTunable", 2),
          ("notTunable", 1),
          ("unequipped", 0))
    )


_TmnxOpticalPortLaserTunability_Type.__name__ = "Integer32"
_TmnxOpticalPortLaserTunability_Object = MibTableColumn
tmnxOpticalPortLaserTunability = _TmnxOpticalPortLaserTunability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 59, 1, 30),
    _TmnxOpticalPortLaserTunability_Type()
)
tmnxOpticalPortLaserTunability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOpticalPortLaserTunability.setStatus("current")
_TmnxPortEgrExpShaperTblLastChngd_Type = TimeStamp
_TmnxPortEgrExpShaperTblLastChngd_Object = MibScalar
tmnxPortEgrExpShaperTblLastChngd = _TmnxPortEgrExpShaperTblLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 60),
    _TmnxPortEgrExpShaperTblLastChngd_Type()
)
tmnxPortEgrExpShaperTblLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperTblLastChngd.setStatus("current")
_TmnxPortEgrExpShaperTable_Object = MibTable
tmnxPortEgrExpShaperTable = _TmnxPortEgrExpShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61)
)
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperTable.setStatus("current")
_TmnxPortEgrExpShaperEntry_Object = MibTableRow
tmnxPortEgrExpShaperEntry = _TmnxPortEgrExpShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1)
)
tmnxPortEgrExpShaperEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperName"),
)
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperEntry.setStatus("current")
_TmnxPortEgrExpShaperName_Type = TNamedItem
_TmnxPortEgrExpShaperName_Object = MibTableColumn
tmnxPortEgrExpShaperName = _TmnxPortEgrExpShaperName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 1),
    _TmnxPortEgrExpShaperName_Type()
)
tmnxPortEgrExpShaperName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperName.setStatus("current")
_TmnxPortEgrExpShaperRowStatus_Type = RowStatus
_TmnxPortEgrExpShaperRowStatus_Object = MibTableColumn
tmnxPortEgrExpShaperRowStatus = _TmnxPortEgrExpShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 2),
    _TmnxPortEgrExpShaperRowStatus_Type()
)
tmnxPortEgrExpShaperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperRowStatus.setStatus("current")


class _TmnxPortEgrExpShaperRate_Type(TExpSecondaryShaperPIRRate):
    """Custom type tmnxPortEgrExpShaperRate based on TExpSecondaryShaperPIRRate"""
    defaultValue = -1


_TmnxPortEgrExpShaperRate_Object = MibTableColumn
tmnxPortEgrExpShaperRate = _TmnxPortEgrExpShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 3),
    _TmnxPortEgrExpShaperRate_Type()
)
tmnxPortEgrExpShaperRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperRate.setUnits("Kbps")


class _TmnxPortEgrExpShaperClass1Rate_Type(TExpSecondaryShaperClassRate):
    """Custom type tmnxPortEgrExpShaperClass1Rate based on TExpSecondaryShaperClassRate"""
    defaultValue = -1


_TmnxPortEgrExpShaperClass1Rate_Object = MibTableColumn
tmnxPortEgrExpShaperClass1Rate = _TmnxPortEgrExpShaperClass1Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 4),
    _TmnxPortEgrExpShaperClass1Rate_Type()
)
tmnxPortEgrExpShaperClass1Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass1Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass1Rate.setUnits("Kbps")


class _TmnxPortEgrExpShaperClass2Rate_Type(TExpSecondaryShaperClassRate):
    """Custom type tmnxPortEgrExpShaperClass2Rate based on TExpSecondaryShaperClassRate"""
    defaultValue = -1


_TmnxPortEgrExpShaperClass2Rate_Object = MibTableColumn
tmnxPortEgrExpShaperClass2Rate = _TmnxPortEgrExpShaperClass2Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 5),
    _TmnxPortEgrExpShaperClass2Rate_Type()
)
tmnxPortEgrExpShaperClass2Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass2Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass2Rate.setUnits("Kbps")


class _TmnxPortEgrExpShaperClass3Rate_Type(TExpSecondaryShaperClassRate):
    """Custom type tmnxPortEgrExpShaperClass3Rate based on TExpSecondaryShaperClassRate"""
    defaultValue = -1


_TmnxPortEgrExpShaperClass3Rate_Object = MibTableColumn
tmnxPortEgrExpShaperClass3Rate = _TmnxPortEgrExpShaperClass3Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 6),
    _TmnxPortEgrExpShaperClass3Rate_Type()
)
tmnxPortEgrExpShaperClass3Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass3Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass3Rate.setUnits("Kbps")


class _TmnxPortEgrExpShaperClass4Rate_Type(TExpSecondaryShaperClassRate):
    """Custom type tmnxPortEgrExpShaperClass4Rate based on TExpSecondaryShaperClassRate"""
    defaultValue = -1


_TmnxPortEgrExpShaperClass4Rate_Object = MibTableColumn
tmnxPortEgrExpShaperClass4Rate = _TmnxPortEgrExpShaperClass4Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 7),
    _TmnxPortEgrExpShaperClass4Rate_Type()
)
tmnxPortEgrExpShaperClass4Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass4Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass4Rate.setUnits("Kbps")


class _TmnxPortEgrExpShaperClass5Rate_Type(TExpSecondaryShaperClassRate):
    """Custom type tmnxPortEgrExpShaperClass5Rate based on TExpSecondaryShaperClassRate"""
    defaultValue = -1


_TmnxPortEgrExpShaperClass5Rate_Object = MibTableColumn
tmnxPortEgrExpShaperClass5Rate = _TmnxPortEgrExpShaperClass5Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 8),
    _TmnxPortEgrExpShaperClass5Rate_Type()
)
tmnxPortEgrExpShaperClass5Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass5Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass5Rate.setUnits("Kbps")


class _TmnxPortEgrExpShaperClass6Rate_Type(TExpSecondaryShaperClassRate):
    """Custom type tmnxPortEgrExpShaperClass6Rate based on TExpSecondaryShaperClassRate"""
    defaultValue = -1


_TmnxPortEgrExpShaperClass6Rate_Object = MibTableColumn
tmnxPortEgrExpShaperClass6Rate = _TmnxPortEgrExpShaperClass6Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 9),
    _TmnxPortEgrExpShaperClass6Rate_Type()
)
tmnxPortEgrExpShaperClass6Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass6Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass6Rate.setUnits("Kbps")


class _TmnxPortEgrExpShaperClass7Rate_Type(TExpSecondaryShaperClassRate):
    """Custom type tmnxPortEgrExpShaperClass7Rate based on TExpSecondaryShaperClassRate"""
    defaultValue = -1


_TmnxPortEgrExpShaperClass7Rate_Object = MibTableColumn
tmnxPortEgrExpShaperClass7Rate = _TmnxPortEgrExpShaperClass7Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 10),
    _TmnxPortEgrExpShaperClass7Rate_Type()
)
tmnxPortEgrExpShaperClass7Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass7Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass7Rate.setUnits("Kbps")


class _TmnxPortEgrExpShaperClass8Rate_Type(TExpSecondaryShaperClassRate):
    """Custom type tmnxPortEgrExpShaperClass8Rate based on TExpSecondaryShaperClassRate"""
    defaultValue = -1


_TmnxPortEgrExpShaperClass8Rate_Object = MibTableColumn
tmnxPortEgrExpShaperClass8Rate = _TmnxPortEgrExpShaperClass8Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 11),
    _TmnxPortEgrExpShaperClass8Rate_Type()
)
tmnxPortEgrExpShaperClass8Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass8Rate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass8Rate.setUnits("Kbps")
_TmnxPortEgrExpShaperLastChanged_Type = TimeStamp
_TmnxPortEgrExpShaperLastChanged_Object = MibTableColumn
tmnxPortEgrExpShaperLastChanged = _TmnxPortEgrExpShaperLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 12),
    _TmnxPortEgrExpShaperLastChanged_Type()
)
tmnxPortEgrExpShaperLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperLastChanged.setStatus("current")


class _TmnxPortEgrExpShaperLoBrstMaxCls_Type(Unsigned32):
    """Custom type tmnxPortEgrExpShaperLoBrstMaxCls based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxPortEgrExpShaperLoBrstMaxCls_Type.__name__ = "Unsigned32"
_TmnxPortEgrExpShaperLoBrstMaxCls_Object = MibTableColumn
tmnxPortEgrExpShaperLoBrstMaxCls = _TmnxPortEgrExpShaperLoBrstMaxCls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 13),
    _TmnxPortEgrExpShaperLoBrstMaxCls_Type()
)
tmnxPortEgrExpShaperLoBrstMaxCls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperLoBrstMaxCls.setStatus("current")


class _TmnxPortEgrExpShaperClass1Thresh_Type(Integer32):
    """Custom type tmnxPortEgrExpShaperClass1Thresh based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8190),
    )


_TmnxPortEgrExpShaperClass1Thresh_Type.__name__ = "Integer32"
_TmnxPortEgrExpShaperClass1Thresh_Object = MibTableColumn
tmnxPortEgrExpShaperClass1Thresh = _TmnxPortEgrExpShaperClass1Thresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 14),
    _TmnxPortEgrExpShaperClass1Thresh_Type()
)
tmnxPortEgrExpShaperClass1Thresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass1Thresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass1Thresh.setUnits("kbytes")


class _TmnxPortEgrExpShaperClass2Thresh_Type(Integer32):
    """Custom type tmnxPortEgrExpShaperClass2Thresh based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8190),
    )


_TmnxPortEgrExpShaperClass2Thresh_Type.__name__ = "Integer32"
_TmnxPortEgrExpShaperClass2Thresh_Object = MibTableColumn
tmnxPortEgrExpShaperClass2Thresh = _TmnxPortEgrExpShaperClass2Thresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 15),
    _TmnxPortEgrExpShaperClass2Thresh_Type()
)
tmnxPortEgrExpShaperClass2Thresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass2Thresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass2Thresh.setUnits("kbytes")


class _TmnxPortEgrExpShaperClass3Thresh_Type(Integer32):
    """Custom type tmnxPortEgrExpShaperClass3Thresh based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8190),
    )


_TmnxPortEgrExpShaperClass3Thresh_Type.__name__ = "Integer32"
_TmnxPortEgrExpShaperClass3Thresh_Object = MibTableColumn
tmnxPortEgrExpShaperClass3Thresh = _TmnxPortEgrExpShaperClass3Thresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 16),
    _TmnxPortEgrExpShaperClass3Thresh_Type()
)
tmnxPortEgrExpShaperClass3Thresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass3Thresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass3Thresh.setUnits("kbytes")


class _TmnxPortEgrExpShaperClass4Thresh_Type(Integer32):
    """Custom type tmnxPortEgrExpShaperClass4Thresh based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8190),
    )


_TmnxPortEgrExpShaperClass4Thresh_Type.__name__ = "Integer32"
_TmnxPortEgrExpShaperClass4Thresh_Object = MibTableColumn
tmnxPortEgrExpShaperClass4Thresh = _TmnxPortEgrExpShaperClass4Thresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 17),
    _TmnxPortEgrExpShaperClass4Thresh_Type()
)
tmnxPortEgrExpShaperClass4Thresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass4Thresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass4Thresh.setUnits("kbytes")


class _TmnxPortEgrExpShaperClass5Thresh_Type(Integer32):
    """Custom type tmnxPortEgrExpShaperClass5Thresh based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8190),
    )


_TmnxPortEgrExpShaperClass5Thresh_Type.__name__ = "Integer32"
_TmnxPortEgrExpShaperClass5Thresh_Object = MibTableColumn
tmnxPortEgrExpShaperClass5Thresh = _TmnxPortEgrExpShaperClass5Thresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 18),
    _TmnxPortEgrExpShaperClass5Thresh_Type()
)
tmnxPortEgrExpShaperClass5Thresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass5Thresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass5Thresh.setUnits("kbytes")


class _TmnxPortEgrExpShaperClass6Thresh_Type(Integer32):
    """Custom type tmnxPortEgrExpShaperClass6Thresh based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8190),
    )


_TmnxPortEgrExpShaperClass6Thresh_Type.__name__ = "Integer32"
_TmnxPortEgrExpShaperClass6Thresh_Object = MibTableColumn
tmnxPortEgrExpShaperClass6Thresh = _TmnxPortEgrExpShaperClass6Thresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 19),
    _TmnxPortEgrExpShaperClass6Thresh_Type()
)
tmnxPortEgrExpShaperClass6Thresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass6Thresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass6Thresh.setUnits("kbytes")


class _TmnxPortEgrExpShaperClass7Thresh_Type(Integer32):
    """Custom type tmnxPortEgrExpShaperClass7Thresh based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8190),
    )


_TmnxPortEgrExpShaperClass7Thresh_Type.__name__ = "Integer32"
_TmnxPortEgrExpShaperClass7Thresh_Object = MibTableColumn
tmnxPortEgrExpShaperClass7Thresh = _TmnxPortEgrExpShaperClass7Thresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 20),
    _TmnxPortEgrExpShaperClass7Thresh_Type()
)
tmnxPortEgrExpShaperClass7Thresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass7Thresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass7Thresh.setUnits("kbytes")


class _TmnxPortEgrExpShaperClass8Thresh_Type(Integer32):
    """Custom type tmnxPortEgrExpShaperClass8Thresh based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8190),
    )


_TmnxPortEgrExpShaperClass8Thresh_Type.__name__ = "Integer32"
_TmnxPortEgrExpShaperClass8Thresh_Object = MibTableColumn
tmnxPortEgrExpShaperClass8Thresh = _TmnxPortEgrExpShaperClass8Thresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 21),
    _TmnxPortEgrExpShaperClass8Thresh_Type()
)
tmnxPortEgrExpShaperClass8Thresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass8Thresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperClass8Thresh.setUnits("kbytes")


class _TmnxPortEgrExpShaperThresh_Type(Integer32):
    """Custom type tmnxPortEgrExpShaperThresh based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 8190),
    )


_TmnxPortEgrExpShaperThresh_Type.__name__ = "Integer32"
_TmnxPortEgrExpShaperThresh_Object = MibTableColumn
tmnxPortEgrExpShaperThresh = _TmnxPortEgrExpShaperThresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 22),
    _TmnxPortEgrExpShaperThresh_Type()
)
tmnxPortEgrExpShaperThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperThresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperThresh.setUnits("kbytes")


class _TmnxPortEgrExpShaperLoBurstLimit_Type(TClassBurstLimit):
    """Custom type tmnxPortEgrExpShaperLoBurstLimit based on TClassBurstLimit"""
    defaultValue = -1


_TmnxPortEgrExpShaperLoBurstLimit_Object = MibTableColumn
tmnxPortEgrExpShaperLoBurstLimit = _TmnxPortEgrExpShaperLoBurstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 23),
    _TmnxPortEgrExpShaperLoBurstLimit_Type()
)
tmnxPortEgrExpShaperLoBurstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperLoBurstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperLoBurstLimit.setUnits("bytes")


class _TmnxPortEgrExpShaperHiBurstInc_Type(Integer32):
    """Custom type tmnxPortEgrExpShaperHiBurstInc based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65528),
    )


_TmnxPortEgrExpShaperHiBurstInc_Type.__name__ = "Integer32"
_TmnxPortEgrExpShaperHiBurstInc_Object = MibTableColumn
tmnxPortEgrExpShaperHiBurstInc = _TmnxPortEgrExpShaperHiBurstInc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 24),
    _TmnxPortEgrExpShaperHiBurstInc_Type()
)
tmnxPortEgrExpShaperHiBurstInc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperHiBurstInc.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperHiBurstInc.setUnits("bytes")


class _TmnxPortEgrExpShaperCl1BrstLimit_Type(TClassBurstLimit):
    """Custom type tmnxPortEgrExpShaperCl1BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_TmnxPortEgrExpShaperCl1BrstLimit_Object = MibTableColumn
tmnxPortEgrExpShaperCl1BrstLimit = _TmnxPortEgrExpShaperCl1BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 25),
    _TmnxPortEgrExpShaperCl1BrstLimit_Type()
)
tmnxPortEgrExpShaperCl1BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl1BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl1BrstLimit.setUnits("bytes")


class _TmnxPortEgrExpShaperCl2BrstLimit_Type(TClassBurstLimit):
    """Custom type tmnxPortEgrExpShaperCl2BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_TmnxPortEgrExpShaperCl2BrstLimit_Object = MibTableColumn
tmnxPortEgrExpShaperCl2BrstLimit = _TmnxPortEgrExpShaperCl2BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 26),
    _TmnxPortEgrExpShaperCl2BrstLimit_Type()
)
tmnxPortEgrExpShaperCl2BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl2BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl2BrstLimit.setUnits("bytes")


class _TmnxPortEgrExpShaperCl3BrstLimit_Type(TClassBurstLimit):
    """Custom type tmnxPortEgrExpShaperCl3BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_TmnxPortEgrExpShaperCl3BrstLimit_Object = MibTableColumn
tmnxPortEgrExpShaperCl3BrstLimit = _TmnxPortEgrExpShaperCl3BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 27),
    _TmnxPortEgrExpShaperCl3BrstLimit_Type()
)
tmnxPortEgrExpShaperCl3BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl3BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl3BrstLimit.setUnits("bytes")


class _TmnxPortEgrExpShaperCl4BrstLimit_Type(TClassBurstLimit):
    """Custom type tmnxPortEgrExpShaperCl4BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_TmnxPortEgrExpShaperCl4BrstLimit_Object = MibTableColumn
tmnxPortEgrExpShaperCl4BrstLimit = _TmnxPortEgrExpShaperCl4BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 28),
    _TmnxPortEgrExpShaperCl4BrstLimit_Type()
)
tmnxPortEgrExpShaperCl4BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl4BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl4BrstLimit.setUnits("bytes")


class _TmnxPortEgrExpShaperCl5BrstLimit_Type(TClassBurstLimit):
    """Custom type tmnxPortEgrExpShaperCl5BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_TmnxPortEgrExpShaperCl5BrstLimit_Object = MibTableColumn
tmnxPortEgrExpShaperCl5BrstLimit = _TmnxPortEgrExpShaperCl5BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 29),
    _TmnxPortEgrExpShaperCl5BrstLimit_Type()
)
tmnxPortEgrExpShaperCl5BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl5BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl5BrstLimit.setUnits("bytes")


class _TmnxPortEgrExpShaperCl6BrstLimit_Type(TClassBurstLimit):
    """Custom type tmnxPortEgrExpShaperCl6BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_TmnxPortEgrExpShaperCl6BrstLimit_Object = MibTableColumn
tmnxPortEgrExpShaperCl6BrstLimit = _TmnxPortEgrExpShaperCl6BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 30),
    _TmnxPortEgrExpShaperCl6BrstLimit_Type()
)
tmnxPortEgrExpShaperCl6BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl6BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl6BrstLimit.setUnits("bytes")


class _TmnxPortEgrExpShaperCl7BrstLimit_Type(TClassBurstLimit):
    """Custom type tmnxPortEgrExpShaperCl7BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_TmnxPortEgrExpShaperCl7BrstLimit_Object = MibTableColumn
tmnxPortEgrExpShaperCl7BrstLimit = _TmnxPortEgrExpShaperCl7BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 31),
    _TmnxPortEgrExpShaperCl7BrstLimit_Type()
)
tmnxPortEgrExpShaperCl7BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl7BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl7BrstLimit.setUnits("bytes")


class _TmnxPortEgrExpShaperCl8BrstLimit_Type(TClassBurstLimit):
    """Custom type tmnxPortEgrExpShaperCl8BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_TmnxPortEgrExpShaperCl8BrstLimit_Object = MibTableColumn
tmnxPortEgrExpShaperCl8BrstLimit = _TmnxPortEgrExpShaperCl8BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 61, 1, 32),
    _TmnxPortEgrExpShaperCl8BrstLimit_Type()
)
tmnxPortEgrExpShaperCl8BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl8BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperCl8BrstLimit.setUnits("bytes")
_TPortEgrExpShaperStatsTable_Object = MibTable
tPortEgrExpShaperStatsTable = _TPortEgrExpShaperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62)
)
if mibBuilder.loadTexts:
    tPortEgrExpShaperStatsTable.setStatus("current")
_TPortEgrExpShaperStatsEntry_Object = MibTableRow
tPortEgrExpShaperStatsEntry = _TPortEgrExpShaperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1)
)
tPortEgrExpShaperStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperName"),
)
if mibBuilder.loadTexts:
    tPortEgrExpShaperStatsEntry.setStatus("current")
_TPortEgrExpShaperStLstClrdTime_Type = TimeStamp
_TPortEgrExpShaperStLstClrdTime_Object = MibTableColumn
tPortEgrExpShaperStLstClrdTime = _TPortEgrExpShaperStLstClrdTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 1),
    _TPortEgrExpShaperStLstClrdTime_Type()
)
tPortEgrExpShaperStLstClrdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperStLstClrdTime.setStatus("current")
_TPortEgrExpShaperCls1StFwdPkts_Type = Counter64
_TPortEgrExpShaperCls1StFwdPkts_Object = MibTableColumn
tPortEgrExpShaperCls1StFwdPkts = _TPortEgrExpShaperCls1StFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 2),
    _TPortEgrExpShaperCls1StFwdPkts_Type()
)
tPortEgrExpShaperCls1StFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls1StFwdPkts.setStatus("current")
_TPortEgrExpShaperCls1StFwdOcts_Type = Counter64
_TPortEgrExpShaperCls1StFwdOcts_Object = MibTableColumn
tPortEgrExpShaperCls1StFwdOcts = _TPortEgrExpShaperCls1StFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 3),
    _TPortEgrExpShaperCls1StFwdOcts_Type()
)
tPortEgrExpShaperCls1StFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls1StFwdOcts.setStatus("current")
_TPortEgrExpShaperCls1StMonOvrOct_Type = Counter64
_TPortEgrExpShaperCls1StMonOvrOct_Object = MibTableColumn
tPortEgrExpShaperCls1StMonOvrOct = _TPortEgrExpShaperCls1StMonOvrOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 4),
    _TPortEgrExpShaperCls1StMonOvrOct_Type()
)
tPortEgrExpShaperCls1StMonOvrOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls1StMonOvrOct.setStatus("current")
_TPortEgrExpShaperCls2StFwdPkts_Type = Counter64
_TPortEgrExpShaperCls2StFwdPkts_Object = MibTableColumn
tPortEgrExpShaperCls2StFwdPkts = _TPortEgrExpShaperCls2StFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 5),
    _TPortEgrExpShaperCls2StFwdPkts_Type()
)
tPortEgrExpShaperCls2StFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls2StFwdPkts.setStatus("current")
_TPortEgrExpShaperCls2StFwdOcts_Type = Counter64
_TPortEgrExpShaperCls2StFwdOcts_Object = MibTableColumn
tPortEgrExpShaperCls2StFwdOcts = _TPortEgrExpShaperCls2StFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 6),
    _TPortEgrExpShaperCls2StFwdOcts_Type()
)
tPortEgrExpShaperCls2StFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls2StFwdOcts.setStatus("current")
_TPortEgrExpShaperCls2StMonOvrOct_Type = Counter64
_TPortEgrExpShaperCls2StMonOvrOct_Object = MibTableColumn
tPortEgrExpShaperCls2StMonOvrOct = _TPortEgrExpShaperCls2StMonOvrOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 7),
    _TPortEgrExpShaperCls2StMonOvrOct_Type()
)
tPortEgrExpShaperCls2StMonOvrOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls2StMonOvrOct.setStatus("current")
_TPortEgrExpShaperCls3StFwdPkts_Type = Counter64
_TPortEgrExpShaperCls3StFwdPkts_Object = MibTableColumn
tPortEgrExpShaperCls3StFwdPkts = _TPortEgrExpShaperCls3StFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 8),
    _TPortEgrExpShaperCls3StFwdPkts_Type()
)
tPortEgrExpShaperCls3StFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls3StFwdPkts.setStatus("current")
_TPortEgrExpShaperCls3StFwdOcts_Type = Counter64
_TPortEgrExpShaperCls3StFwdOcts_Object = MibTableColumn
tPortEgrExpShaperCls3StFwdOcts = _TPortEgrExpShaperCls3StFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 9),
    _TPortEgrExpShaperCls3StFwdOcts_Type()
)
tPortEgrExpShaperCls3StFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls3StFwdOcts.setStatus("current")
_TPortEgrExpShaperCls3StMonOvrOct_Type = Counter64
_TPortEgrExpShaperCls3StMonOvrOct_Object = MibTableColumn
tPortEgrExpShaperCls3StMonOvrOct = _TPortEgrExpShaperCls3StMonOvrOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 10),
    _TPortEgrExpShaperCls3StMonOvrOct_Type()
)
tPortEgrExpShaperCls3StMonOvrOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls3StMonOvrOct.setStatus("current")
_TPortEgrExpShaperCls4StFwdPkts_Type = Counter64
_TPortEgrExpShaperCls4StFwdPkts_Object = MibTableColumn
tPortEgrExpShaperCls4StFwdPkts = _TPortEgrExpShaperCls4StFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 11),
    _TPortEgrExpShaperCls4StFwdPkts_Type()
)
tPortEgrExpShaperCls4StFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls4StFwdPkts.setStatus("current")
_TPortEgrExpShaperCls4StFwdOcts_Type = Counter64
_TPortEgrExpShaperCls4StFwdOcts_Object = MibTableColumn
tPortEgrExpShaperCls4StFwdOcts = _TPortEgrExpShaperCls4StFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 12),
    _TPortEgrExpShaperCls4StFwdOcts_Type()
)
tPortEgrExpShaperCls4StFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls4StFwdOcts.setStatus("current")
_TPortEgrExpShaperCls4StMonOvrOct_Type = Counter64
_TPortEgrExpShaperCls4StMonOvrOct_Object = MibTableColumn
tPortEgrExpShaperCls4StMonOvrOct = _TPortEgrExpShaperCls4StMonOvrOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 13),
    _TPortEgrExpShaperCls4StMonOvrOct_Type()
)
tPortEgrExpShaperCls4StMonOvrOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls4StMonOvrOct.setStatus("current")
_TPortEgrExpShaperCls5StFwdPkts_Type = Counter64
_TPortEgrExpShaperCls5StFwdPkts_Object = MibTableColumn
tPortEgrExpShaperCls5StFwdPkts = _TPortEgrExpShaperCls5StFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 14),
    _TPortEgrExpShaperCls5StFwdPkts_Type()
)
tPortEgrExpShaperCls5StFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls5StFwdPkts.setStatus("current")
_TPortEgrExpShaperCls5StFwdOcts_Type = Counter64
_TPortEgrExpShaperCls5StFwdOcts_Object = MibTableColumn
tPortEgrExpShaperCls5StFwdOcts = _TPortEgrExpShaperCls5StFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 15),
    _TPortEgrExpShaperCls5StFwdOcts_Type()
)
tPortEgrExpShaperCls5StFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls5StFwdOcts.setStatus("current")
_TPortEgrExpShaperCls5StMonOvrOct_Type = Counter64
_TPortEgrExpShaperCls5StMonOvrOct_Object = MibTableColumn
tPortEgrExpShaperCls5StMonOvrOct = _TPortEgrExpShaperCls5StMonOvrOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 16),
    _TPortEgrExpShaperCls5StMonOvrOct_Type()
)
tPortEgrExpShaperCls5StMonOvrOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls5StMonOvrOct.setStatus("current")
_TPortEgrExpShaperCls6StFwdPkts_Type = Counter64
_TPortEgrExpShaperCls6StFwdPkts_Object = MibTableColumn
tPortEgrExpShaperCls6StFwdPkts = _TPortEgrExpShaperCls6StFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 17),
    _TPortEgrExpShaperCls6StFwdPkts_Type()
)
tPortEgrExpShaperCls6StFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls6StFwdPkts.setStatus("current")
_TPortEgrExpShaperCls6StFwdOcts_Type = Counter64
_TPortEgrExpShaperCls6StFwdOcts_Object = MibTableColumn
tPortEgrExpShaperCls6StFwdOcts = _TPortEgrExpShaperCls6StFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 18),
    _TPortEgrExpShaperCls6StFwdOcts_Type()
)
tPortEgrExpShaperCls6StFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls6StFwdOcts.setStatus("current")
_TPortEgrExpShaperCls6StMonOvrOct_Type = Counter64
_TPortEgrExpShaperCls6StMonOvrOct_Object = MibTableColumn
tPortEgrExpShaperCls6StMonOvrOct = _TPortEgrExpShaperCls6StMonOvrOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 19),
    _TPortEgrExpShaperCls6StMonOvrOct_Type()
)
tPortEgrExpShaperCls6StMonOvrOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls6StMonOvrOct.setStatus("current")
_TPortEgrExpShaperCls7StFwdPkts_Type = Counter64
_TPortEgrExpShaperCls7StFwdPkts_Object = MibTableColumn
tPortEgrExpShaperCls7StFwdPkts = _TPortEgrExpShaperCls7StFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 20),
    _TPortEgrExpShaperCls7StFwdPkts_Type()
)
tPortEgrExpShaperCls7StFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls7StFwdPkts.setStatus("current")
_TPortEgrExpShaperCls7StFwdOcts_Type = Counter64
_TPortEgrExpShaperCls7StFwdOcts_Object = MibTableColumn
tPortEgrExpShaperCls7StFwdOcts = _TPortEgrExpShaperCls7StFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 21),
    _TPortEgrExpShaperCls7StFwdOcts_Type()
)
tPortEgrExpShaperCls7StFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls7StFwdOcts.setStatus("current")
_TPortEgrExpShaperCls7StMonOvrOct_Type = Counter64
_TPortEgrExpShaperCls7StMonOvrOct_Object = MibTableColumn
tPortEgrExpShaperCls7StMonOvrOct = _TPortEgrExpShaperCls7StMonOvrOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 22),
    _TPortEgrExpShaperCls7StMonOvrOct_Type()
)
tPortEgrExpShaperCls7StMonOvrOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls7StMonOvrOct.setStatus("current")
_TPortEgrExpShaperCls8StFwdPkts_Type = Counter64
_TPortEgrExpShaperCls8StFwdPkts_Object = MibTableColumn
tPortEgrExpShaperCls8StFwdPkts = _TPortEgrExpShaperCls8StFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 23),
    _TPortEgrExpShaperCls8StFwdPkts_Type()
)
tPortEgrExpShaperCls8StFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls8StFwdPkts.setStatus("current")
_TPortEgrExpShaperCls8StFwdOcts_Type = Counter64
_TPortEgrExpShaperCls8StFwdOcts_Object = MibTableColumn
tPortEgrExpShaperCls8StFwdOcts = _TPortEgrExpShaperCls8StFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 24),
    _TPortEgrExpShaperCls8StFwdOcts_Type()
)
tPortEgrExpShaperCls8StFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls8StFwdOcts.setStatus("current")
_TPortEgrExpShaperCls8StMonOvrOct_Type = Counter64
_TPortEgrExpShaperCls8StMonOvrOct_Object = MibTableColumn
tPortEgrExpShaperCls8StMonOvrOct = _TPortEgrExpShaperCls8StMonOvrOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 25),
    _TPortEgrExpShaperCls8StMonOvrOct_Type()
)
tPortEgrExpShaperCls8StMonOvrOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls8StMonOvrOct.setStatus("current")
_TPortEgrExpShaperAggStFwdPkts_Type = Counter64
_TPortEgrExpShaperAggStFwdPkts_Object = MibTableColumn
tPortEgrExpShaperAggStFwdPkts = _TPortEgrExpShaperAggStFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 26),
    _TPortEgrExpShaperAggStFwdPkts_Type()
)
tPortEgrExpShaperAggStFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperAggStFwdPkts.setStatus("current")
_TPortEgrExpShaperAggStFwdOcts_Type = Counter64
_TPortEgrExpShaperAggStFwdOcts_Object = MibTableColumn
tPortEgrExpShaperAggStFwdOcts = _TPortEgrExpShaperAggStFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 27),
    _TPortEgrExpShaperAggStFwdOcts_Type()
)
tPortEgrExpShaperAggStFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperAggStFwdOcts.setStatus("current")
_TPortEgrExpShaperAggStMonOvrOct_Type = Counter64
_TPortEgrExpShaperAggStMonOvrOct_Object = MibTableColumn
tPortEgrExpShaperAggStMonOvrOct = _TPortEgrExpShaperAggStMonOvrOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 62, 1, 28),
    _TPortEgrExpShaperAggStMonOvrOct_Type()
)
tPortEgrExpShaperAggStMonOvrOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperAggStMonOvrOct.setStatus("current")
_TPortEgrExpShaperStatsHLTable_Object = MibTable
tPortEgrExpShaperStatsHLTable = _TPortEgrExpShaperStatsHLTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63)
)
if mibBuilder.loadTexts:
    tPortEgrExpShaperStatsHLTable.setStatus("current")
_TPortEgrExpShaperStatsHLEntry_Object = MibTableRow
tPortEgrExpShaperStatsHLEntry = _TPortEgrExpShaperStatsHLEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1)
)
tPortEgrExpShaperStatsHLEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperName"),
)
if mibBuilder.loadTexts:
    tPortEgrExpShaperStatsHLEntry.setStatus("current")
_TPortEgrExpShaperCls1StFwdPktsL_Type = Counter32
_TPortEgrExpShaperCls1StFwdPktsL_Object = MibTableColumn
tPortEgrExpShaperCls1StFwdPktsL = _TPortEgrExpShaperCls1StFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 1),
    _TPortEgrExpShaperCls1StFwdPktsL_Type()
)
tPortEgrExpShaperCls1StFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls1StFwdPktsL.setStatus("current")
_TPortEgrExpShaperCls1StFwdPktsH_Type = Counter32
_TPortEgrExpShaperCls1StFwdPktsH_Object = MibTableColumn
tPortEgrExpShaperCls1StFwdPktsH = _TPortEgrExpShaperCls1StFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 2),
    _TPortEgrExpShaperCls1StFwdPktsH_Type()
)
tPortEgrExpShaperCls1StFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls1StFwdPktsH.setStatus("current")
_TPortEgrExpShaperCls1StFwdOctsL_Type = Counter32
_TPortEgrExpShaperCls1StFwdOctsL_Object = MibTableColumn
tPortEgrExpShaperCls1StFwdOctsL = _TPortEgrExpShaperCls1StFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 3),
    _TPortEgrExpShaperCls1StFwdOctsL_Type()
)
tPortEgrExpShaperCls1StFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls1StFwdOctsL.setStatus("current")
_TPortEgrExpShaperCls1StFwdOctsH_Type = Counter32
_TPortEgrExpShaperCls1StFwdOctsH_Object = MibTableColumn
tPortEgrExpShaperCls1StFwdOctsH = _TPortEgrExpShaperCls1StFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 4),
    _TPortEgrExpShaperCls1StFwdOctsH_Type()
)
tPortEgrExpShaperCls1StFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls1StFwdOctsH.setStatus("current")
_TPortEgrExpShaperCls1StMonOvrOL_Type = Counter32
_TPortEgrExpShaperCls1StMonOvrOL_Object = MibTableColumn
tPortEgrExpShaperCls1StMonOvrOL = _TPortEgrExpShaperCls1StMonOvrOL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 5),
    _TPortEgrExpShaperCls1StMonOvrOL_Type()
)
tPortEgrExpShaperCls1StMonOvrOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls1StMonOvrOL.setStatus("current")
_TPortEgrExpShaperCls1StMonOvrOH_Type = Counter32
_TPortEgrExpShaperCls1StMonOvrOH_Object = MibTableColumn
tPortEgrExpShaperCls1StMonOvrOH = _TPortEgrExpShaperCls1StMonOvrOH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 6),
    _TPortEgrExpShaperCls1StMonOvrOH_Type()
)
tPortEgrExpShaperCls1StMonOvrOH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls1StMonOvrOH.setStatus("current")
_TPortEgrExpShaperCls2StFwdPktsL_Type = Counter32
_TPortEgrExpShaperCls2StFwdPktsL_Object = MibTableColumn
tPortEgrExpShaperCls2StFwdPktsL = _TPortEgrExpShaperCls2StFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 7),
    _TPortEgrExpShaperCls2StFwdPktsL_Type()
)
tPortEgrExpShaperCls2StFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls2StFwdPktsL.setStatus("current")
_TPortEgrExpShaperCls2StFwdPktsH_Type = Counter32
_TPortEgrExpShaperCls2StFwdPktsH_Object = MibTableColumn
tPortEgrExpShaperCls2StFwdPktsH = _TPortEgrExpShaperCls2StFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 8),
    _TPortEgrExpShaperCls2StFwdPktsH_Type()
)
tPortEgrExpShaperCls2StFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls2StFwdPktsH.setStatus("current")
_TPortEgrExpShaperCls2StFwdOctsL_Type = Counter32
_TPortEgrExpShaperCls2StFwdOctsL_Object = MibTableColumn
tPortEgrExpShaperCls2StFwdOctsL = _TPortEgrExpShaperCls2StFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 9),
    _TPortEgrExpShaperCls2StFwdOctsL_Type()
)
tPortEgrExpShaperCls2StFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls2StFwdOctsL.setStatus("current")
_TPortEgrExpShaperCls2StFwdOctsH_Type = Counter32
_TPortEgrExpShaperCls2StFwdOctsH_Object = MibTableColumn
tPortEgrExpShaperCls2StFwdOctsH = _TPortEgrExpShaperCls2StFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 10),
    _TPortEgrExpShaperCls2StFwdOctsH_Type()
)
tPortEgrExpShaperCls2StFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls2StFwdOctsH.setStatus("current")
_TPortEgrExpShaperCls2StMonOvrOL_Type = Counter32
_TPortEgrExpShaperCls2StMonOvrOL_Object = MibTableColumn
tPortEgrExpShaperCls2StMonOvrOL = _TPortEgrExpShaperCls2StMonOvrOL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 11),
    _TPortEgrExpShaperCls2StMonOvrOL_Type()
)
tPortEgrExpShaperCls2StMonOvrOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls2StMonOvrOL.setStatus("current")
_TPortEgrExpShaperCls2StMonOvrOH_Type = Counter32
_TPortEgrExpShaperCls2StMonOvrOH_Object = MibTableColumn
tPortEgrExpShaperCls2StMonOvrOH = _TPortEgrExpShaperCls2StMonOvrOH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 12),
    _TPortEgrExpShaperCls2StMonOvrOH_Type()
)
tPortEgrExpShaperCls2StMonOvrOH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls2StMonOvrOH.setStatus("current")
_TPortEgrExpShaperCls3StFwdPktsL_Type = Counter32
_TPortEgrExpShaperCls3StFwdPktsL_Object = MibTableColumn
tPortEgrExpShaperCls3StFwdPktsL = _TPortEgrExpShaperCls3StFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 13),
    _TPortEgrExpShaperCls3StFwdPktsL_Type()
)
tPortEgrExpShaperCls3StFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls3StFwdPktsL.setStatus("current")
_TPortEgrExpShaperCls3StFwdPktsH_Type = Counter32
_TPortEgrExpShaperCls3StFwdPktsH_Object = MibTableColumn
tPortEgrExpShaperCls3StFwdPktsH = _TPortEgrExpShaperCls3StFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 14),
    _TPortEgrExpShaperCls3StFwdPktsH_Type()
)
tPortEgrExpShaperCls3StFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls3StFwdPktsH.setStatus("current")
_TPortEgrExpShaperCls3StFwdOctsL_Type = Counter32
_TPortEgrExpShaperCls3StFwdOctsL_Object = MibTableColumn
tPortEgrExpShaperCls3StFwdOctsL = _TPortEgrExpShaperCls3StFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 15),
    _TPortEgrExpShaperCls3StFwdOctsL_Type()
)
tPortEgrExpShaperCls3StFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls3StFwdOctsL.setStatus("current")
_TPortEgrExpShaperCls3StFwdOctsH_Type = Counter32
_TPortEgrExpShaperCls3StFwdOctsH_Object = MibTableColumn
tPortEgrExpShaperCls3StFwdOctsH = _TPortEgrExpShaperCls3StFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 16),
    _TPortEgrExpShaperCls3StFwdOctsH_Type()
)
tPortEgrExpShaperCls3StFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls3StFwdOctsH.setStatus("current")
_TPortEgrExpShaperCls3StMonOvrOL_Type = Counter32
_TPortEgrExpShaperCls3StMonOvrOL_Object = MibTableColumn
tPortEgrExpShaperCls3StMonOvrOL = _TPortEgrExpShaperCls3StMonOvrOL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 17),
    _TPortEgrExpShaperCls3StMonOvrOL_Type()
)
tPortEgrExpShaperCls3StMonOvrOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls3StMonOvrOL.setStatus("current")
_TPortEgrExpShaperCls3StMonOvrOH_Type = Counter32
_TPortEgrExpShaperCls3StMonOvrOH_Object = MibTableColumn
tPortEgrExpShaperCls3StMonOvrOH = _TPortEgrExpShaperCls3StMonOvrOH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 18),
    _TPortEgrExpShaperCls3StMonOvrOH_Type()
)
tPortEgrExpShaperCls3StMonOvrOH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls3StMonOvrOH.setStatus("current")
_TPortEgrExpShaperCls4StFwdPktsL_Type = Counter32
_TPortEgrExpShaperCls4StFwdPktsL_Object = MibTableColumn
tPortEgrExpShaperCls4StFwdPktsL = _TPortEgrExpShaperCls4StFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 19),
    _TPortEgrExpShaperCls4StFwdPktsL_Type()
)
tPortEgrExpShaperCls4StFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls4StFwdPktsL.setStatus("current")
_TPortEgrExpShaperCls4StFwdPktsH_Type = Counter32
_TPortEgrExpShaperCls4StFwdPktsH_Object = MibTableColumn
tPortEgrExpShaperCls4StFwdPktsH = _TPortEgrExpShaperCls4StFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 20),
    _TPortEgrExpShaperCls4StFwdPktsH_Type()
)
tPortEgrExpShaperCls4StFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls4StFwdPktsH.setStatus("current")
_TPortEgrExpShaperCls4StFwdOctsL_Type = Counter32
_TPortEgrExpShaperCls4StFwdOctsL_Object = MibTableColumn
tPortEgrExpShaperCls4StFwdOctsL = _TPortEgrExpShaperCls4StFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 21),
    _TPortEgrExpShaperCls4StFwdOctsL_Type()
)
tPortEgrExpShaperCls4StFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls4StFwdOctsL.setStatus("current")
_TPortEgrExpShaperCls4StFwdOctsH_Type = Counter32
_TPortEgrExpShaperCls4StFwdOctsH_Object = MibTableColumn
tPortEgrExpShaperCls4StFwdOctsH = _TPortEgrExpShaperCls4StFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 22),
    _TPortEgrExpShaperCls4StFwdOctsH_Type()
)
tPortEgrExpShaperCls4StFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls4StFwdOctsH.setStatus("current")
_TPortEgrExpShaperCls4StMonOvrOL_Type = Counter32
_TPortEgrExpShaperCls4StMonOvrOL_Object = MibTableColumn
tPortEgrExpShaperCls4StMonOvrOL = _TPortEgrExpShaperCls4StMonOvrOL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 23),
    _TPortEgrExpShaperCls4StMonOvrOL_Type()
)
tPortEgrExpShaperCls4StMonOvrOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls4StMonOvrOL.setStatus("current")
_TPortEgrExpShaperCls4StMonOvrOH_Type = Counter32
_TPortEgrExpShaperCls4StMonOvrOH_Object = MibTableColumn
tPortEgrExpShaperCls4StMonOvrOH = _TPortEgrExpShaperCls4StMonOvrOH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 24),
    _TPortEgrExpShaperCls4StMonOvrOH_Type()
)
tPortEgrExpShaperCls4StMonOvrOH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls4StMonOvrOH.setStatus("current")
_TPortEgrExpShaperCls5StFwdPktsL_Type = Counter32
_TPortEgrExpShaperCls5StFwdPktsL_Object = MibTableColumn
tPortEgrExpShaperCls5StFwdPktsL = _TPortEgrExpShaperCls5StFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 25),
    _TPortEgrExpShaperCls5StFwdPktsL_Type()
)
tPortEgrExpShaperCls5StFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls5StFwdPktsL.setStatus("current")
_TPortEgrExpShaperCls5StFwdPktsH_Type = Counter32
_TPortEgrExpShaperCls5StFwdPktsH_Object = MibTableColumn
tPortEgrExpShaperCls5StFwdPktsH = _TPortEgrExpShaperCls5StFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 26),
    _TPortEgrExpShaperCls5StFwdPktsH_Type()
)
tPortEgrExpShaperCls5StFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls5StFwdPktsH.setStatus("current")
_TPortEgrExpShaperCls5StFwdOctsL_Type = Counter32
_TPortEgrExpShaperCls5StFwdOctsL_Object = MibTableColumn
tPortEgrExpShaperCls5StFwdOctsL = _TPortEgrExpShaperCls5StFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 27),
    _TPortEgrExpShaperCls5StFwdOctsL_Type()
)
tPortEgrExpShaperCls5StFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls5StFwdOctsL.setStatus("current")
_TPortEgrExpShaperCls5StFwdOctsH_Type = Counter32
_TPortEgrExpShaperCls5StFwdOctsH_Object = MibTableColumn
tPortEgrExpShaperCls5StFwdOctsH = _TPortEgrExpShaperCls5StFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 28),
    _TPortEgrExpShaperCls5StFwdOctsH_Type()
)
tPortEgrExpShaperCls5StFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls5StFwdOctsH.setStatus("current")
_TPortEgrExpShaperCls5StMonOvrOL_Type = Counter32
_TPortEgrExpShaperCls5StMonOvrOL_Object = MibTableColumn
tPortEgrExpShaperCls5StMonOvrOL = _TPortEgrExpShaperCls5StMonOvrOL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 29),
    _TPortEgrExpShaperCls5StMonOvrOL_Type()
)
tPortEgrExpShaperCls5StMonOvrOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls5StMonOvrOL.setStatus("current")
_TPortEgrExpShaperCls5StMonOvrOH_Type = Counter32
_TPortEgrExpShaperCls5StMonOvrOH_Object = MibTableColumn
tPortEgrExpShaperCls5StMonOvrOH = _TPortEgrExpShaperCls5StMonOvrOH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 30),
    _TPortEgrExpShaperCls5StMonOvrOH_Type()
)
tPortEgrExpShaperCls5StMonOvrOH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls5StMonOvrOH.setStatus("current")
_TPortEgrExpShaperCls6StFwdPktsL_Type = Counter32
_TPortEgrExpShaperCls6StFwdPktsL_Object = MibTableColumn
tPortEgrExpShaperCls6StFwdPktsL = _TPortEgrExpShaperCls6StFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 31),
    _TPortEgrExpShaperCls6StFwdPktsL_Type()
)
tPortEgrExpShaperCls6StFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls6StFwdPktsL.setStatus("current")
_TPortEgrExpShaperCls6StFwdPktsH_Type = Counter32
_TPortEgrExpShaperCls6StFwdPktsH_Object = MibTableColumn
tPortEgrExpShaperCls6StFwdPktsH = _TPortEgrExpShaperCls6StFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 32),
    _TPortEgrExpShaperCls6StFwdPktsH_Type()
)
tPortEgrExpShaperCls6StFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls6StFwdPktsH.setStatus("current")
_TPortEgrExpShaperCls6StFwdOctsL_Type = Counter32
_TPortEgrExpShaperCls6StFwdOctsL_Object = MibTableColumn
tPortEgrExpShaperCls6StFwdOctsL = _TPortEgrExpShaperCls6StFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 33),
    _TPortEgrExpShaperCls6StFwdOctsL_Type()
)
tPortEgrExpShaperCls6StFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls6StFwdOctsL.setStatus("current")
_TPortEgrExpShaperCls6StFwdOctsH_Type = Counter32
_TPortEgrExpShaperCls6StFwdOctsH_Object = MibTableColumn
tPortEgrExpShaperCls6StFwdOctsH = _TPortEgrExpShaperCls6StFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 34),
    _TPortEgrExpShaperCls6StFwdOctsH_Type()
)
tPortEgrExpShaperCls6StFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls6StFwdOctsH.setStatus("current")
_TPortEgrExpShaperCls6StMonOvrOL_Type = Counter32
_TPortEgrExpShaperCls6StMonOvrOL_Object = MibTableColumn
tPortEgrExpShaperCls6StMonOvrOL = _TPortEgrExpShaperCls6StMonOvrOL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 35),
    _TPortEgrExpShaperCls6StMonOvrOL_Type()
)
tPortEgrExpShaperCls6StMonOvrOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls6StMonOvrOL.setStatus("current")
_TPortEgrExpShaperCls6StMonOvrOH_Type = Counter32
_TPortEgrExpShaperCls6StMonOvrOH_Object = MibTableColumn
tPortEgrExpShaperCls6StMonOvrOH = _TPortEgrExpShaperCls6StMonOvrOH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 36),
    _TPortEgrExpShaperCls6StMonOvrOH_Type()
)
tPortEgrExpShaperCls6StMonOvrOH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls6StMonOvrOH.setStatus("current")
_TPortEgrExpShaperCls7StFwdPktsL_Type = Counter32
_TPortEgrExpShaperCls7StFwdPktsL_Object = MibTableColumn
tPortEgrExpShaperCls7StFwdPktsL = _TPortEgrExpShaperCls7StFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 37),
    _TPortEgrExpShaperCls7StFwdPktsL_Type()
)
tPortEgrExpShaperCls7StFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls7StFwdPktsL.setStatus("current")
_TPortEgrExpShaperCls7StFwdPktsH_Type = Counter32
_TPortEgrExpShaperCls7StFwdPktsH_Object = MibTableColumn
tPortEgrExpShaperCls7StFwdPktsH = _TPortEgrExpShaperCls7StFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 38),
    _TPortEgrExpShaperCls7StFwdPktsH_Type()
)
tPortEgrExpShaperCls7StFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls7StFwdPktsH.setStatus("current")
_TPortEgrExpShaperCls7StFwdOctsL_Type = Counter32
_TPortEgrExpShaperCls7StFwdOctsL_Object = MibTableColumn
tPortEgrExpShaperCls7StFwdOctsL = _TPortEgrExpShaperCls7StFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 39),
    _TPortEgrExpShaperCls7StFwdOctsL_Type()
)
tPortEgrExpShaperCls7StFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls7StFwdOctsL.setStatus("current")
_TPortEgrExpShaperCls7StFwdOctsH_Type = Counter32
_TPortEgrExpShaperCls7StFwdOctsH_Object = MibTableColumn
tPortEgrExpShaperCls7StFwdOctsH = _TPortEgrExpShaperCls7StFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 40),
    _TPortEgrExpShaperCls7StFwdOctsH_Type()
)
tPortEgrExpShaperCls7StFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls7StFwdOctsH.setStatus("current")
_TPortEgrExpShaperCls7StMonOvrOL_Type = Counter32
_TPortEgrExpShaperCls7StMonOvrOL_Object = MibTableColumn
tPortEgrExpShaperCls7StMonOvrOL = _TPortEgrExpShaperCls7StMonOvrOL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 41),
    _TPortEgrExpShaperCls7StMonOvrOL_Type()
)
tPortEgrExpShaperCls7StMonOvrOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls7StMonOvrOL.setStatus("current")
_TPortEgrExpShaperCls7StMonOvrOH_Type = Counter32
_TPortEgrExpShaperCls7StMonOvrOH_Object = MibTableColumn
tPortEgrExpShaperCls7StMonOvrOH = _TPortEgrExpShaperCls7StMonOvrOH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 42),
    _TPortEgrExpShaperCls7StMonOvrOH_Type()
)
tPortEgrExpShaperCls7StMonOvrOH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls7StMonOvrOH.setStatus("current")
_TPortEgrExpShaperCls8StFwdPktsL_Type = Counter32
_TPortEgrExpShaperCls8StFwdPktsL_Object = MibTableColumn
tPortEgrExpShaperCls8StFwdPktsL = _TPortEgrExpShaperCls8StFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 43),
    _TPortEgrExpShaperCls8StFwdPktsL_Type()
)
tPortEgrExpShaperCls8StFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls8StFwdPktsL.setStatus("current")
_TPortEgrExpShaperCls8StFwdPktsH_Type = Counter32
_TPortEgrExpShaperCls8StFwdPktsH_Object = MibTableColumn
tPortEgrExpShaperCls8StFwdPktsH = _TPortEgrExpShaperCls8StFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 44),
    _TPortEgrExpShaperCls8StFwdPktsH_Type()
)
tPortEgrExpShaperCls8StFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls8StFwdPktsH.setStatus("current")
_TPortEgrExpShaperCls8StFwdOctsL_Type = Counter32
_TPortEgrExpShaperCls8StFwdOctsL_Object = MibTableColumn
tPortEgrExpShaperCls8StFwdOctsL = _TPortEgrExpShaperCls8StFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 45),
    _TPortEgrExpShaperCls8StFwdOctsL_Type()
)
tPortEgrExpShaperCls8StFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls8StFwdOctsL.setStatus("current")
_TPortEgrExpShaperCls8StFwdOctsH_Type = Counter32
_TPortEgrExpShaperCls8StFwdOctsH_Object = MibTableColumn
tPortEgrExpShaperCls8StFwdOctsH = _TPortEgrExpShaperCls8StFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 46),
    _TPortEgrExpShaperCls8StFwdOctsH_Type()
)
tPortEgrExpShaperCls8StFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls8StFwdOctsH.setStatus("current")
_TPortEgrExpShaperCls8StMonOvrOL_Type = Counter32
_TPortEgrExpShaperCls8StMonOvrOL_Object = MibTableColumn
tPortEgrExpShaperCls8StMonOvrOL = _TPortEgrExpShaperCls8StMonOvrOL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 47),
    _TPortEgrExpShaperCls8StMonOvrOL_Type()
)
tPortEgrExpShaperCls8StMonOvrOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls8StMonOvrOL.setStatus("current")
_TPortEgrExpShaperCls8StMonOvrOH_Type = Counter32
_TPortEgrExpShaperCls8StMonOvrOH_Object = MibTableColumn
tPortEgrExpShaperCls8StMonOvrOH = _TPortEgrExpShaperCls8StMonOvrOH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 48),
    _TPortEgrExpShaperCls8StMonOvrOH_Type()
)
tPortEgrExpShaperCls8StMonOvrOH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperCls8StMonOvrOH.setStatus("current")
_TPortEgrExpShaperAggStFwdPktsL_Type = Counter32
_TPortEgrExpShaperAggStFwdPktsL_Object = MibTableColumn
tPortEgrExpShaperAggStFwdPktsL = _TPortEgrExpShaperAggStFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 49),
    _TPortEgrExpShaperAggStFwdPktsL_Type()
)
tPortEgrExpShaperAggStFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperAggStFwdPktsL.setStatus("current")
_TPortEgrExpShaperAggStFwdPktsH_Type = Counter32
_TPortEgrExpShaperAggStFwdPktsH_Object = MibTableColumn
tPortEgrExpShaperAggStFwdPktsH = _TPortEgrExpShaperAggStFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 50),
    _TPortEgrExpShaperAggStFwdPktsH_Type()
)
tPortEgrExpShaperAggStFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperAggStFwdPktsH.setStatus("current")
_TPortEgrExpShaperAggStFwdOctsL_Type = Counter32
_TPortEgrExpShaperAggStFwdOctsL_Object = MibTableColumn
tPortEgrExpShaperAggStFwdOctsL = _TPortEgrExpShaperAggStFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 51),
    _TPortEgrExpShaperAggStFwdOctsL_Type()
)
tPortEgrExpShaperAggStFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperAggStFwdOctsL.setStatus("current")
_TPortEgrExpShaperAggStFwdOctsH_Type = Counter32
_TPortEgrExpShaperAggStFwdOctsH_Object = MibTableColumn
tPortEgrExpShaperAggStFwdOctsH = _TPortEgrExpShaperAggStFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 52),
    _TPortEgrExpShaperAggStFwdOctsH_Type()
)
tPortEgrExpShaperAggStFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperAggStFwdOctsH.setStatus("current")
_TPortEgrExpShaperAggStMonOvrOL_Type = Counter32
_TPortEgrExpShaperAggStMonOvrOL_Object = MibTableColumn
tPortEgrExpShaperAggStMonOvrOL = _TPortEgrExpShaperAggStMonOvrOL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 53),
    _TPortEgrExpShaperAggStMonOvrOL_Type()
)
tPortEgrExpShaperAggStMonOvrOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperAggStMonOvrOL.setStatus("current")
_TPortEgrExpShaperAggStMonOvrOH_Type = Counter32
_TPortEgrExpShaperAggStMonOvrOH_Object = MibTableColumn
tPortEgrExpShaperAggStMonOvrOH = _TPortEgrExpShaperAggStMonOvrOH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 63, 1, 54),
    _TPortEgrExpShaperAggStMonOvrOH_Type()
)
tPortEgrExpShaperAggStMonOvrOH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrExpShaperAggStMonOvrOH.setStatus("current")
_TPortEgrVPortAggStatsTable_Object = MibTable
tPortEgrVPortAggStatsTable = _TPortEgrVPortAggStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 64)
)
if mibBuilder.loadTexts:
    tPortEgrVPortAggStatsTable.setStatus("current")
_TPortEgrVPortAggStatsEntry_Object = MibTableRow
tPortEgrVPortAggStatsEntry = _TPortEgrVPortAggStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 64, 1)
)
tPortEgrVPortAggStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortEgrVPortName"),
    (0, "TIMETRA-PORT-MIB", "tPortEgrVPStLvl"),
)
if mibBuilder.loadTexts:
    tPortEgrVPortAggStatsEntry.setStatus("current")


class _TPortEgrVPStLvl_Type(Unsigned32):
    """Custom type tPortEgrVPStLvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TPortEgrVPStLvl_Type.__name__ = "Unsigned32"
_TPortEgrVPStLvl_Object = MibTableColumn
tPortEgrVPStLvl = _TPortEgrVPStLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 64, 1, 1),
    _TPortEgrVPStLvl_Type()
)
tPortEgrVPStLvl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortEgrVPStLvl.setStatus("current")
_TPortEgrVPStLstClrdTime_Type = TimeStamp
_TPortEgrVPStLstClrdTime_Object = MibTableColumn
tPortEgrVPStLstClrdTime = _TPortEgrVPStLstClrdTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 64, 1, 2),
    _TPortEgrVPStLstClrdTime_Type()
)
tPortEgrVPStLstClrdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLstClrdTime.setStatus("current")
_TPortEgrVPStLvlFwdPkt_Type = Counter64
_TPortEgrVPStLvlFwdPkt_Object = MibTableColumn
tPortEgrVPStLvlFwdPkt = _TPortEgrVPStLvlFwdPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 64, 1, 3),
    _TPortEgrVPStLvlFwdPkt_Type()
)
tPortEgrVPStLvlFwdPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlFwdPkt.setStatus("current")
_TPortEgrVPStLvlFwdOct_Type = Counter64
_TPortEgrVPStLvlFwdOct_Object = MibTableColumn
tPortEgrVPStLvlFwdOct = _TPortEgrVPStLvlFwdOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 64, 1, 4),
    _TPortEgrVPStLvlFwdOct_Type()
)
tPortEgrVPStLvlFwdOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlFwdOct.setStatus("current")
_TPortEgrVPStLvlDpdPkt_Type = Counter64
_TPortEgrVPStLvlDpdPkt_Object = MibTableColumn
tPortEgrVPStLvlDpdPkt = _TPortEgrVPStLvlDpdPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 64, 1, 5),
    _TPortEgrVPStLvlDpdPkt_Type()
)
tPortEgrVPStLvlDpdPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlDpdPkt.setStatus("current")
_TPortEgrVPStLvlDpdOct_Type = Counter64
_TPortEgrVPStLvlDpdOct_Object = MibTableColumn
tPortEgrVPStLvlDpdOct = _TPortEgrVPStLvlDpdOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 64, 1, 6),
    _TPortEgrVPStLvlDpdOct_Type()
)
tPortEgrVPStLvlDpdOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlDpdOct.setStatus("current")
_TPortEgrVPortAggStatsHLTable_Object = MibTable
tPortEgrVPortAggStatsHLTable = _TPortEgrVPortAggStatsHLTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 65)
)
if mibBuilder.loadTexts:
    tPortEgrVPortAggStatsHLTable.setStatus("current")
_TPortEgrVPortAggStatsHLEntry_Object = MibTableRow
tPortEgrVPortAggStatsHLEntry = _TPortEgrVPortAggStatsHLEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 65, 1)
)
tPortEgrVPortAggStatsHLEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortEgrVPortName"),
    (0, "TIMETRA-PORT-MIB", "tPortEgrVPStLvl"),
)
if mibBuilder.loadTexts:
    tPortEgrVPortAggStatsHLEntry.setStatus("current")
_TPortEgrVPStLvlFwdPktL_Type = Counter32
_TPortEgrVPStLvlFwdPktL_Object = MibTableColumn
tPortEgrVPStLvlFwdPktL = _TPortEgrVPStLvlFwdPktL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 65, 1, 1),
    _TPortEgrVPStLvlFwdPktL_Type()
)
tPortEgrVPStLvlFwdPktL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlFwdPktL.setStatus("current")
_TPortEgrVPStLvlFwdPktH_Type = Counter32
_TPortEgrVPStLvlFwdPktH_Object = MibTableColumn
tPortEgrVPStLvlFwdPktH = _TPortEgrVPStLvlFwdPktH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 65, 1, 2),
    _TPortEgrVPStLvlFwdPktH_Type()
)
tPortEgrVPStLvlFwdPktH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlFwdPktH.setStatus("current")
_TPortEgrVPStLvlFwdOctL_Type = Counter32
_TPortEgrVPStLvlFwdOctL_Object = MibTableColumn
tPortEgrVPStLvlFwdOctL = _TPortEgrVPStLvlFwdOctL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 65, 1, 3),
    _TPortEgrVPStLvlFwdOctL_Type()
)
tPortEgrVPStLvlFwdOctL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlFwdOctL.setStatus("current")
_TPortEgrVPStLvlFwdOctH_Type = Counter32
_TPortEgrVPStLvlFwdOctH_Object = MibTableColumn
tPortEgrVPStLvlFwdOctH = _TPortEgrVPStLvlFwdOctH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 65, 1, 4),
    _TPortEgrVPStLvlFwdOctH_Type()
)
tPortEgrVPStLvlFwdOctH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlFwdOctH.setStatus("current")
_TPortEgrVPStLvlDpdPktL_Type = Counter32
_TPortEgrVPStLvlDpdPktL_Object = MibTableColumn
tPortEgrVPStLvlDpdPktL = _TPortEgrVPStLvlDpdPktL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 65, 1, 5),
    _TPortEgrVPStLvlDpdPktL_Type()
)
tPortEgrVPStLvlDpdPktL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlDpdPktL.setStatus("current")
_TPortEgrVPStLvlDpdPktH_Type = Counter32
_TPortEgrVPStLvlDpdPktH_Object = MibTableColumn
tPortEgrVPStLvlDpdPktH = _TPortEgrVPStLvlDpdPktH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 65, 1, 6),
    _TPortEgrVPStLvlDpdPktH_Type()
)
tPortEgrVPStLvlDpdPktH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlDpdPktH.setStatus("current")
_TPortEgrVPStLvlDpdOctL_Type = Counter32
_TPortEgrVPStLvlDpdOctL_Object = MibTableColumn
tPortEgrVPStLvlDpdOctL = _TPortEgrVPStLvlDpdOctL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 65, 1, 7),
    _TPortEgrVPStLvlDpdOctL_Type()
)
tPortEgrVPStLvlDpdOctL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlDpdOctL.setStatus("current")
_TPortEgrVPStLvlDpdOctH_Type = Counter32
_TPortEgrVPStLvlDpdOctH_Object = MibTableColumn
tPortEgrVPStLvlDpdOctH = _TPortEgrVPStLvlDpdOctH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 65, 1, 8),
    _TPortEgrVPStLvlDpdOctH_Type()
)
tPortEgrVPStLvlDpdOctH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortEgrVPStLvlDpdOctH.setStatus("current")
_TmnxDDMLaneTable_Object = MibTable
tmnxDDMLaneTable = _TmnxDDMLaneTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66)
)
if mibBuilder.loadTexts:
    tmnxDDMLaneTable.setStatus("current")
_TmnxDDMLaneEntry_Object = MibTableRow
tmnxDDMLaneEntry = _TmnxDDMLaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1)
)
tmnxDDMLaneEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tmnxDDMLaneId"),
)
if mibBuilder.loadTexts:
    tmnxDDMLaneEntry.setStatus("current")


class _TmnxDDMLaneId_Type(Unsigned32):
    """Custom type tmnxDDMLaneId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxDDMLaneId_Type.__name__ = "Unsigned32"
_TmnxDDMLaneId_Object = MibTableColumn
tmnxDDMLaneId = _TmnxDDMLaneId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 1),
    _TmnxDDMLaneId_Type()
)
tmnxDDMLaneId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDDMLaneId.setStatus("current")
_TmnxDDMLaneTemperature_Type = Integer32
_TmnxDDMLaneTemperature_Object = MibTableColumn
tmnxDDMLaneTemperature = _TmnxDDMLaneTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 2),
    _TmnxDDMLaneTemperature_Type()
)
tmnxDDMLaneTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTemperature.setStatus("current")
_TmnxDDMLaneTempLowWarn_Type = Integer32
_TmnxDDMLaneTempLowWarn_Object = MibTableColumn
tmnxDDMLaneTempLowWarn = _TmnxDDMLaneTempLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 3),
    _TmnxDDMLaneTempLowWarn_Type()
)
tmnxDDMLaneTempLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTempLowWarn.setStatus("current")
_TmnxDDMLaneTempLowAlarm_Type = Integer32
_TmnxDDMLaneTempLowAlarm_Object = MibTableColumn
tmnxDDMLaneTempLowAlarm = _TmnxDDMLaneTempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 4),
    _TmnxDDMLaneTempLowAlarm_Type()
)
tmnxDDMLaneTempLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTempLowAlarm.setStatus("current")
_TmnxDDMLaneTempHiWarn_Type = Integer32
_TmnxDDMLaneTempHiWarn_Object = MibTableColumn
tmnxDDMLaneTempHiWarn = _TmnxDDMLaneTempHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 5),
    _TmnxDDMLaneTempHiWarn_Type()
)
tmnxDDMLaneTempHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTempHiWarn.setStatus("current")
_TmnxDDMLaneTempHiAlarm_Type = Integer32
_TmnxDDMLaneTempHiAlarm_Object = MibTableColumn
tmnxDDMLaneTempHiAlarm = _TmnxDDMLaneTempHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 6),
    _TmnxDDMLaneTempHiAlarm_Type()
)
tmnxDDMLaneTempHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTempHiAlarm.setStatus("current")
_TmnxDDMLaneTxBiasCurrent_Type = Integer32
_TmnxDDMLaneTxBiasCurrent_Object = MibTableColumn
tmnxDDMLaneTxBiasCurrent = _TmnxDDMLaneTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 7),
    _TmnxDDMLaneTxBiasCurrent_Type()
)
tmnxDDMLaneTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTxBiasCurrent.setStatus("current")
_TmnxDDMLaneTxBiasCurrentLowWarn_Type = Integer32
_TmnxDDMLaneTxBiasCurrentLowWarn_Object = MibTableColumn
tmnxDDMLaneTxBiasCurrentLowWarn = _TmnxDDMLaneTxBiasCurrentLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 8),
    _TmnxDDMLaneTxBiasCurrentLowWarn_Type()
)
tmnxDDMLaneTxBiasCurrentLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTxBiasCurrentLowWarn.setStatus("current")
_TmnxDDMLaneTxBiasCurrentLowAlarm_Type = Integer32
_TmnxDDMLaneTxBiasCurrentLowAlarm_Object = MibTableColumn
tmnxDDMLaneTxBiasCurrentLowAlarm = _TmnxDDMLaneTxBiasCurrentLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 9),
    _TmnxDDMLaneTxBiasCurrentLowAlarm_Type()
)
tmnxDDMLaneTxBiasCurrentLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTxBiasCurrentLowAlarm.setStatus("current")
_TmnxDDMLaneTxBiasCurrentHiWarn_Type = Integer32
_TmnxDDMLaneTxBiasCurrentHiWarn_Object = MibTableColumn
tmnxDDMLaneTxBiasCurrentHiWarn = _TmnxDDMLaneTxBiasCurrentHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 10),
    _TmnxDDMLaneTxBiasCurrentHiWarn_Type()
)
tmnxDDMLaneTxBiasCurrentHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTxBiasCurrentHiWarn.setStatus("current")
_TmnxDDMLaneTxBiasCurrentHiAlarm_Type = Integer32
_TmnxDDMLaneTxBiasCurrentHiAlarm_Object = MibTableColumn
tmnxDDMLaneTxBiasCurrentHiAlarm = _TmnxDDMLaneTxBiasCurrentHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 11),
    _TmnxDDMLaneTxBiasCurrentHiAlarm_Type()
)
tmnxDDMLaneTxBiasCurrentHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTxBiasCurrentHiAlarm.setStatus("current")
_TmnxDDMLaneTxOutputPower_Type = Integer32
_TmnxDDMLaneTxOutputPower_Object = MibTableColumn
tmnxDDMLaneTxOutputPower = _TmnxDDMLaneTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 12),
    _TmnxDDMLaneTxOutputPower_Type()
)
tmnxDDMLaneTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTxOutputPower.setStatus("current")
_TmnxDDMLaneTxOutputPowerLowWarn_Type = Integer32
_TmnxDDMLaneTxOutputPowerLowWarn_Object = MibTableColumn
tmnxDDMLaneTxOutputPowerLowWarn = _TmnxDDMLaneTxOutputPowerLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 13),
    _TmnxDDMLaneTxOutputPowerLowWarn_Type()
)
tmnxDDMLaneTxOutputPowerLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTxOutputPowerLowWarn.setStatus("current")
_TmnxDDMLaneTxOutputPowerLowAlarm_Type = Integer32
_TmnxDDMLaneTxOutputPowerLowAlarm_Object = MibTableColumn
tmnxDDMLaneTxOutputPowerLowAlarm = _TmnxDDMLaneTxOutputPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 14),
    _TmnxDDMLaneTxOutputPowerLowAlarm_Type()
)
tmnxDDMLaneTxOutputPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTxOutputPowerLowAlarm.setStatus("current")
_TmnxDDMLaneTxOutputPowerHiWarn_Type = Integer32
_TmnxDDMLaneTxOutputPowerHiWarn_Object = MibTableColumn
tmnxDDMLaneTxOutputPowerHiWarn = _TmnxDDMLaneTxOutputPowerHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 15),
    _TmnxDDMLaneTxOutputPowerHiWarn_Type()
)
tmnxDDMLaneTxOutputPowerHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTxOutputPowerHiWarn.setStatus("current")
_TmnxDDMLaneTxOutputPowerHiAlarm_Type = Integer32
_TmnxDDMLaneTxOutputPowerHiAlarm_Object = MibTableColumn
tmnxDDMLaneTxOutputPowerHiAlarm = _TmnxDDMLaneTxOutputPowerHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 16),
    _TmnxDDMLaneTxOutputPowerHiAlarm_Type()
)
tmnxDDMLaneTxOutputPowerHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneTxOutputPowerHiAlarm.setStatus("current")
_TmnxDDMLaneRxOpticalPower_Type = Integer32
_TmnxDDMLaneRxOpticalPower_Object = MibTableColumn
tmnxDDMLaneRxOpticalPower = _TmnxDDMLaneRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 17),
    _TmnxDDMLaneRxOpticalPower_Type()
)
tmnxDDMLaneRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneRxOpticalPower.setStatus("current")
_TmnxDDMLaneRxOpticalPwrLowWarn_Type = Integer32
_TmnxDDMLaneRxOpticalPwrLowWarn_Object = MibTableColumn
tmnxDDMLaneRxOpticalPwrLowWarn = _TmnxDDMLaneRxOpticalPwrLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 18),
    _TmnxDDMLaneRxOpticalPwrLowWarn_Type()
)
tmnxDDMLaneRxOpticalPwrLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneRxOpticalPwrLowWarn.setStatus("current")
_TmnxDDMLaneRxOpticalPwrLowAlarm_Type = Integer32
_TmnxDDMLaneRxOpticalPwrLowAlarm_Object = MibTableColumn
tmnxDDMLaneRxOpticalPwrLowAlarm = _TmnxDDMLaneRxOpticalPwrLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 19),
    _TmnxDDMLaneRxOpticalPwrLowAlarm_Type()
)
tmnxDDMLaneRxOpticalPwrLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneRxOpticalPwrLowAlarm.setStatus("current")
_TmnxDDMLaneRxOpticalPwrHiWarn_Type = Integer32
_TmnxDDMLaneRxOpticalPwrHiWarn_Object = MibTableColumn
tmnxDDMLaneRxOpticalPwrHiWarn = _TmnxDDMLaneRxOpticalPwrHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 20),
    _TmnxDDMLaneRxOpticalPwrHiWarn_Type()
)
tmnxDDMLaneRxOpticalPwrHiWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneRxOpticalPwrHiWarn.setStatus("current")
_TmnxDDMLaneRxOpticalPwrHiAlarm_Type = Integer32
_TmnxDDMLaneRxOpticalPwrHiAlarm_Object = MibTableColumn
tmnxDDMLaneRxOpticalPwrHiAlarm = _TmnxDDMLaneRxOpticalPwrHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 21),
    _TmnxDDMLaneRxOpticalPwrHiAlarm_Type()
)
tmnxDDMLaneRxOpticalPwrHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneRxOpticalPwrHiAlarm.setStatus("current")


class _TmnxDDMLaneRxOpticalPowerType_Type(Integer32):
    """Custom type tmnxDDMLaneRxOpticalPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("average", 1),
          ("oma", 0))
    )


_TmnxDDMLaneRxOpticalPowerType_Type.__name__ = "Integer32"
_TmnxDDMLaneRxOpticalPowerType_Object = MibTableColumn
tmnxDDMLaneRxOpticalPowerType = _TmnxDDMLaneRxOpticalPowerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 22),
    _TmnxDDMLaneRxOpticalPowerType_Type()
)
tmnxDDMLaneRxOpticalPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneRxOpticalPowerType.setStatus("current")
_TmnxDDMLaneFailedThresholds_Type = TmnxDigitalDiagnosticFailureBits
_TmnxDDMLaneFailedThresholds_Object = MibTableColumn
tmnxDDMLaneFailedThresholds = _TmnxDDMLaneFailedThresholds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 66, 1, 23),
    _TmnxDDMLaneFailedThresholds_Type()
)
tmnxDDMLaneFailedThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDDMLaneFailedThresholds.setStatus("current")
_TmnxPortPlcyObjs_ObjectIdentity = ObjectIdentity
tmnxPortPlcyObjs = _TmnxPortPlcyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 67)
)
_TmnxPortPlcyTableLastCh_Type = TimeStamp
_TmnxPortPlcyTableLastCh_Object = MibScalar
tmnxPortPlcyTableLastCh = _TmnxPortPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 67, 1),
    _TmnxPortPlcyTableLastCh_Type()
)
tmnxPortPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortPlcyTableLastCh.setStatus("current")
_TmnxPortPlcyTable_Object = MibTable
tmnxPortPlcyTable = _TmnxPortPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 67, 2)
)
if mibBuilder.loadTexts:
    tmnxPortPlcyTable.setStatus("current")
_TmnxPortPlcyEntry_Object = MibTableRow
tmnxPortPlcyEntry = _TmnxPortPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 67, 2, 1)
)
tmnxPortPlcyEntry.setIndexNames(
    (1, "TIMETRA-PORT-MIB", "tmnxPortPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxPortPlcyEntry.setStatus("current")
_TmnxPortPlcyName_Type = TNamedItem
_TmnxPortPlcyName_Object = MibTableColumn
tmnxPortPlcyName = _TmnxPortPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 67, 2, 1, 1),
    _TmnxPortPlcyName_Type()
)
tmnxPortPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortPlcyName.setStatus("current")
_TmnxPortPlcyRowStatus_Type = RowStatus
_TmnxPortPlcyRowStatus_Object = MibTableColumn
tmnxPortPlcyRowStatus = _TmnxPortPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 67, 2, 1, 2),
    _TmnxPortPlcyRowStatus_Type()
)
tmnxPortPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortPlcyRowStatus.setStatus("current")
_TmnxPortPlcyLastCh_Type = TimeStamp
_TmnxPortPlcyLastCh_Object = MibTableColumn
tmnxPortPlcyLastCh = _TmnxPortPlcyLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 67, 2, 1, 3),
    _TmnxPortPlcyLastCh_Type()
)
tmnxPortPlcyLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortPlcyLastCh.setStatus("current")
_TmnxPortPlcyDescription_Type = TItemDescription
_TmnxPortPlcyDescription_Object = MibTableColumn
tmnxPortPlcyDescription = _TmnxPortPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 67, 2, 1, 4),
    _TmnxPortPlcyDescription_Type()
)
tmnxPortPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortPlcyDescription.setStatus("current")
_TmnxPortPlcyEgrPortSchedPlcy_Type = TNamedItemOrEmpty
_TmnxPortPlcyEgrPortSchedPlcy_Object = MibTableColumn
tmnxPortPlcyEgrPortSchedPlcy = _TmnxPortPlcyEgrPortSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 67, 2, 1, 5),
    _TmnxPortPlcyEgrPortSchedPlcy_Type()
)
tmnxPortPlcyEgrPortSchedPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortPlcyEgrPortSchedPlcy.setStatus("current")
_TPortNetEgrQGrpArbitStatTable_Object = MibTable
tPortNetEgrQGrpArbitStatTable = _TPortNetEgrQGrpArbitStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 68)
)
if mibBuilder.loadTexts:
    tPortNetEgrQGrpArbitStatTable.setStatus("current")
_TPortNetEgrQGrpArbitStatEntry_Object = MibTableRow
tPortNetEgrQGrpArbitStatEntry = _TPortNetEgrQGrpArbitStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 68, 1)
)
tPortNetEgrQGrpArbitStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpInstanceId"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpArbitStatName"),
)
if mibBuilder.loadTexts:
    tPortNetEgrQGrpArbitStatEntry.setStatus("current")
_TPortNetEgrQGrpArbitStatName_Type = TNamedItem
_TPortNetEgrQGrpArbitStatName_Object = MibTableColumn
tPortNetEgrQGrpArbitStatName = _TPortNetEgrQGrpArbitStatName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 68, 1, 1),
    _TPortNetEgrQGrpArbitStatName_Type()
)
tPortNetEgrQGrpArbitStatName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpArbitStatName.setStatus("current")
_TPortNetEgrQGrpArbitStatFwdPkts_Type = Counter64
_TPortNetEgrQGrpArbitStatFwdPkts_Object = MibTableColumn
tPortNetEgrQGrpArbitStatFwdPkts = _TPortNetEgrQGrpArbitStatFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 68, 1, 2),
    _TPortNetEgrQGrpArbitStatFwdPkts_Type()
)
tPortNetEgrQGrpArbitStatFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpArbitStatFwdPkts.setStatus("current")
_TPortNetEgrQGrpArbitStatFwdPktsL_Type = Counter32
_TPortNetEgrQGrpArbitStatFwdPktsL_Object = MibTableColumn
tPortNetEgrQGrpArbitStatFwdPktsL = _TPortNetEgrQGrpArbitStatFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 68, 1, 3),
    _TPortNetEgrQGrpArbitStatFwdPktsL_Type()
)
tPortNetEgrQGrpArbitStatFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpArbitStatFwdPktsL.setStatus("current")
_TPortNetEgrQGrpArbitStatFwdPktsH_Type = Counter32
_TPortNetEgrQGrpArbitStatFwdPktsH_Object = MibTableColumn
tPortNetEgrQGrpArbitStatFwdPktsH = _TPortNetEgrQGrpArbitStatFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 68, 1, 4),
    _TPortNetEgrQGrpArbitStatFwdPktsH_Type()
)
tPortNetEgrQGrpArbitStatFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpArbitStatFwdPktsH.setStatus("current")
_TPortNetEgrQGrpArbitStatFwdOcts_Type = Counter64
_TPortNetEgrQGrpArbitStatFwdOcts_Object = MibTableColumn
tPortNetEgrQGrpArbitStatFwdOcts = _TPortNetEgrQGrpArbitStatFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 68, 1, 5),
    _TPortNetEgrQGrpArbitStatFwdOcts_Type()
)
tPortNetEgrQGrpArbitStatFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpArbitStatFwdOcts.setStatus("current")
_TPortNetEgrQGrpArbitStatFwdOctsL_Type = Counter32
_TPortNetEgrQGrpArbitStatFwdOctsL_Object = MibTableColumn
tPortNetEgrQGrpArbitStatFwdOctsL = _TPortNetEgrQGrpArbitStatFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 68, 1, 6),
    _TPortNetEgrQGrpArbitStatFwdOctsL_Type()
)
tPortNetEgrQGrpArbitStatFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpArbitStatFwdOctsL.setStatus("current")
_TPortNetEgrQGrpArbitStatFwdOctsH_Type = Counter32
_TPortNetEgrQGrpArbitStatFwdOctsH_Object = MibTableColumn
tPortNetEgrQGrpArbitStatFwdOctsH = _TPortNetEgrQGrpArbitStatFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 68, 1, 7),
    _TPortNetEgrQGrpArbitStatFwdOctsH_Type()
)
tPortNetEgrQGrpArbitStatFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpArbitStatFwdOctsH.setStatus("current")
_TmnxPwPortTblLastChanged_Type = TimeStamp
_TmnxPwPortTblLastChanged_Object = MibScalar
tmnxPwPortTblLastChanged = _TmnxPwPortTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 69),
    _TmnxPwPortTblLastChanged_Type()
)
tmnxPwPortTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPwPortTblLastChanged.setStatus("current")
_TmnxPwPortTable_Object = MibTable
tmnxPwPortTable = _TmnxPwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 70)
)
if mibBuilder.loadTexts:
    tmnxPwPortTable.setStatus("current")
_TmnxPwPortEntry_Object = MibTableRow
tmnxPwPortEntry = _TmnxPwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 70, 1)
)
tmnxPwPortEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPwPortId"),
)
if mibBuilder.loadTexts:
    tmnxPwPortEntry.setStatus("current")


class _TmnxPwPortId_Type(Unsigned32):
    """Custom type tmnxPwPortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10239),
    )


_TmnxPwPortId_Type.__name__ = "Unsigned32"
_TmnxPwPortId_Object = MibTableColumn
tmnxPwPortId = _TmnxPwPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 70, 1, 1),
    _TmnxPwPortId_Type()
)
tmnxPwPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPwPortId.setStatus("current")
_TmnxPwPortRowStatus_Type = RowStatus
_TmnxPwPortRowStatus_Object = MibTableColumn
tmnxPwPortRowStatus = _TmnxPwPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 70, 1, 2),
    _TmnxPwPortRowStatus_Type()
)
tmnxPwPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPwPortRowStatus.setStatus("current")
_TmnxPwPortLastChgd_Type = TimeStamp
_TmnxPwPortLastChgd_Object = MibTableColumn
tmnxPwPortLastChgd = _TmnxPwPortLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 70, 1, 3),
    _TmnxPwPortLastChgd_Type()
)
tmnxPwPortLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPwPortLastChgd.setStatus("current")


class _TmnxPwPortEncapType_Type(Integer32):
    """Custom type tmnxPwPortEncapType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dot1q", 2),
          ("qinq", 10))
    )


_TmnxPwPortEncapType_Type.__name__ = "Integer32"
_TmnxPwPortEncapType_Object = MibTableColumn
tmnxPwPortEncapType = _TmnxPwPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 4, 70, 1, 4),
    _TmnxPwPortEncapType_Type()
)
tmnxPwPortEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPwPortEncapType.setStatus("current")
_TmnxPortNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxPortNotificationObjects = _TmnxPortNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7)
)
_TmnxPortNotifyPortId_Type = TmnxPortID
_TmnxPortNotifyPortId_Object = MibScalar
tmnxPortNotifyPortId = _TmnxPortNotifyPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 1),
    _TmnxPortNotifyPortId_Type()
)
tmnxPortNotifyPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyPortId.setStatus("current")


class _TmnxPortNotifySonetAlarmReason_Type(Integer32):
    """Custom type tmnxPortNotifySonetAlarmReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("lais", 2),
          ("lb2erSd", 6),
          ("lb2erSf", 7),
          ("loc", 1),
          ("lrdi", 3),
          ("lrei", 12),
          ("notUsed", 0),
          ("sb1err", 5),
          ("slof", 8),
          ("slos", 9),
          ("srxptr", 11),
          ("ss1f", 4),
          ("stxptr", 10))
    )


_TmnxPortNotifySonetAlarmReason_Type.__name__ = "Integer32"
_TmnxPortNotifySonetAlarmReason_Object = MibScalar
tmnxPortNotifySonetAlarmReason = _TmnxPortNotifySonetAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 2),
    _TmnxPortNotifySonetAlarmReason_Type()
)
tmnxPortNotifySonetAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifySonetAlarmReason.setStatus("current")


class _TmnxPortNotifySonetPathAlarmReason_Type(Integer32):
    """Custom type tmnxPortNotifySonetPathAlarmReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("notUsed", 0),
          ("pais", 1),
          ("pb3err", 4),
          ("plcd", 8),
          ("plop", 2),
          ("pplm", 5),
          ("prdi", 3),
          ("prei", 6),
          ("puneq", 7))
    )


_TmnxPortNotifySonetPathAlarmReason_Type.__name__ = "Integer32"
_TmnxPortNotifySonetPathAlarmReason_Object = MibScalar
tmnxPortNotifySonetPathAlarmReason = _TmnxPortNotifySonetPathAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 3),
    _TmnxPortNotifySonetPathAlarmReason_Type()
)
tmnxPortNotifySonetPathAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifySonetPathAlarmReason.setStatus("current")


class _TmnxPortNotifyError_Type(Integer32):
    """Custom type tmnxPortNotifyError based on Integer32"""
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
        *(("laserError", 4),
          ("miscError", 5),
          ("rxClockError", 2),
          ("txClockError", 1),
          ("txFifoError", 3))
    )


_TmnxPortNotifyError_Type.__name__ = "Integer32"
_TmnxPortNotifyError_Object = MibScalar
tmnxPortNotifyError = _TmnxPortNotifyError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 4),
    _TmnxPortNotifyError_Type()
)
tmnxPortNotifyError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyError.setStatus("current")


class _TmnxPortNotifyDS3AlarmReason_Type(Integer32):
    """Custom type tmnxPortNotifyDS3AlarmReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ais", 1),
          ("looped", 5),
          ("los", 2),
          ("notUsed", 0),
          ("oof", 3),
          ("rai", 4))
    )


_TmnxPortNotifyDS3AlarmReason_Type.__name__ = "Integer32"
_TmnxPortNotifyDS3AlarmReason_Object = MibScalar
tmnxPortNotifyDS3AlarmReason = _TmnxPortNotifyDS3AlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 5),
    _TmnxPortNotifyDS3AlarmReason_Type()
)
tmnxPortNotifyDS3AlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyDS3AlarmReason.setStatus("current")


class _TmnxPortNotifyDS1AlarmReason_Type(Integer32):
    """Custom type tmnxPortNotifyDS1AlarmReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ais", 1),
          ("berSd", 6),
          ("berSf", 7),
          ("looped", 5),
          ("los", 2),
          ("notUsed", 0),
          ("oof", 3),
          ("rai", 4))
    )


_TmnxPortNotifyDS1AlarmReason_Type.__name__ = "Integer32"
_TmnxPortNotifyDS1AlarmReason_Object = MibScalar
tmnxPortNotifyDS1AlarmReason = _TmnxPortNotifyDS1AlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 6),
    _TmnxPortNotifyDS1AlarmReason_Type()
)
tmnxPortNotifyDS1AlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyDS1AlarmReason.setStatus("current")
_TmnxPortNotifyBundleId_Type = TmnxBundleID
_TmnxPortNotifyBundleId_Object = MibScalar
tmnxPortNotifyBundleId = _TmnxPortNotifyBundleId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 7),
    _TmnxPortNotifyBundleId_Type()
)
tmnxPortNotifyBundleId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyBundleId.setStatus("current")
_TmnxPortNotifyEtherAlarmReason_Type = TmnxPortEtherReportValue
_TmnxPortNotifyEtherAlarmReason_Object = MibScalar
tmnxPortNotifyEtherAlarmReason = _TmnxPortNotifyEtherAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 8),
    _TmnxPortNotifyEtherAlarmReason_Type()
)
tmnxPortNotifyEtherAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyEtherAlarmReason.setStatus("current")


class _TmnxDDMFailedObject_Type(Integer32):
    """Custom type tmnxDDMFailedObject based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("aux1-high-alarm", 24),
          ("aux1-high-warning", 23),
          ("aux1-low-alarm", 22),
          ("aux1-low-warning", 21),
          ("aux2-high-alarm", 28),
          ("aux2-high-warning", 27),
          ("aux2-low-alarm", 26),
          ("aux2-low-warning", 25),
          ("rxOpticalPower-high-alarm", 20),
          ("rxOpticalPower-high-warning", 19),
          ("rxOpticalPower-low-alarm", 18),
          ("rxOpticalPower-low-warning", 17),
          ("supplyVoltage-high-alarm", 8),
          ("supplyVoltage-high-warning", 7),
          ("supplyVoltage-low-alarm", 6),
          ("supplyVoltage-low-warning", 5),
          ("temperature-high-alarm", 4),
          ("temperature-high-warning", 3),
          ("temperature-low-alarm", 2),
          ("temperature-low-warning", 1),
          ("txBiasCurrent-high-alarm", 12),
          ("txBiasCurrent-high-warning", 11),
          ("txBiasCurrent-low-alarm", 10),
          ("txBiasCurrent-low-warning", 9),
          ("txOutputPower-high-alarm", 16),
          ("txOutputPower-high-warning", 15),
          ("txOutputPower-low-alarm", 14),
          ("txOutputPower-low-warning", 13),
          ("unknown", 0))
    )


_TmnxDDMFailedObject_Type.__name__ = "Integer32"
_TmnxDDMFailedObject_Object = MibScalar
tmnxDDMFailedObject = _TmnxDDMFailedObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 9),
    _TmnxDDMFailedObject_Type()
)
tmnxDDMFailedObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDDMFailedObject.setStatus("current")
_TmnxDSXClockSyncStateObject_Type = TmnxDSXClockSyncState
_TmnxDSXClockSyncStateObject_Object = MibScalar
tmnxDSXClockSyncStateObject = _TmnxDSXClockSyncStateObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 10),
    _TmnxDSXClockSyncStateObject_Type()
)
tmnxDSXClockSyncStateObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDSXClockSyncStateObject.setStatus("current")
_TmnxPortNotifyDescription_Type = DisplayString
_TmnxPortNotifyDescription_Object = MibScalar
tmnxPortNotifyDescription = _TmnxPortNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 11),
    _TmnxPortNotifyDescription_Type()
)
tmnxPortNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyDescription.setStatus("current")


class _TmnxPortNotifyWTAlarmReason_Type(Integer32):
    """Custom type tmnxPortNotifyWTAlarmReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("encDegr", 2),
          ("encFail", 1),
          ("notUsed", 0),
          ("pwrDegr", 4),
          ("pwrFail", 3),
          ("pwrHigh", 5),
          ("pwrLow", 6))
    )


_TmnxPortNotifyWTAlarmReason_Type.__name__ = "Integer32"
_TmnxPortNotifyWTAlarmReason_Object = MibScalar
tmnxPortNotifyWTAlarmReason = _TmnxPortNotifyWTAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 12),
    _TmnxPortNotifyWTAlarmReason_Type()
)
tmnxPortNotifyWTAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyWTAlarmReason.setStatus("current")
_TmnxHostMatchNotifyIntDestId_Type = TmnxSubMgtIntDestId
_TmnxHostMatchNotifyIntDestId_Object = MibScalar
tmnxHostMatchNotifyIntDestId = _TmnxHostMatchNotifyIntDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 13),
    _TmnxHostMatchNotifyIntDestId_Type()
)
tmnxHostMatchNotifyIntDestId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxHostMatchNotifyIntDestId.setStatus("current")
_TmnxHostMatchNotifyOrgString_Type = TmnxSubMgtOrgStrOrZero
_TmnxHostMatchNotifyOrgString_Object = MibScalar
tmnxHostMatchNotifyOrgString = _TmnxHostMatchNotifyOrgString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 14),
    _TmnxHostMatchNotifyOrgString_Type()
)
tmnxHostMatchNotifyOrgString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxHostMatchNotifyOrgString.setStatus("current")
_TmnxHostMatchNotifySubIdent_Type = TmnxSubIdentStringOrEmpty
_TmnxHostMatchNotifySubIdent_Object = MibScalar
tmnxHostMatchNotifySubIdent = _TmnxHostMatchNotifySubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 15),
    _TmnxHostMatchNotifySubIdent_Type()
)
tmnxHostMatchNotifySubIdent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxHostMatchNotifySubIdent.setStatus("current")
_TmnxObjAppResvSize_Type = Unsigned32
_TmnxObjAppResvSize_Object = MibScalar
tmnxObjAppResvSize = _TmnxObjAppResvSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 16),
    _TmnxObjAppResvSize_Type()
)
tmnxObjAppResvSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxObjAppResvSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxObjAppResvSize.setUnits("kilo-bytes")
_TmnxObjAppResvCbsOld_Type = Unsigned32
_TmnxObjAppResvCbsOld_Object = MibScalar
tmnxObjAppResvCbsOld = _TmnxObjAppResvCbsOld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 17),
    _TmnxObjAppResvCbsOld_Type()
)
tmnxObjAppResvCbsOld.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxObjAppResvCbsOld.setStatus("current")
if mibBuilder.loadTexts:
    tmnxObjAppResvCbsOld.setUnits("percent")
_TmnxObjAppResvCbsNew_Type = Unsigned32
_TmnxObjAppResvCbsNew_Object = MibScalar
tmnxObjAppResvCbsNew = _TmnxObjAppResvCbsNew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 18),
    _TmnxObjAppResvCbsNew_Type()
)
tmnxObjAppResvCbsNew.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxObjAppResvCbsNew.setStatus("current")
if mibBuilder.loadTexts:
    tmnxObjAppResvCbsNew.setUnits("percent")
_TmnxObjAppSumOfQResvSize_Type = Unsigned32
_TmnxObjAppSumOfQResvSize_Object = MibScalar
tmnxObjAppSumOfQResvSize = _TmnxObjAppSumOfQResvSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 19),
    _TmnxObjAppSumOfQResvSize_Type()
)
tmnxObjAppSumOfQResvSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxObjAppSumOfQResvSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxObjAppSumOfQResvSize.setUnits("kilo-bytes")


class _TmnxObjType_Type(Integer32):
    """Custom type tmnxObjType based on Integer32"""
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
        *(("bundle", 4),
          ("mda", 1),
          ("port", 2),
          ("unused", 3))
    )


_TmnxObjType_Type.__name__ = "Integer32"
_TmnxObjType_Object = MibScalar
tmnxObjType = _TmnxObjType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 20),
    _TmnxObjType_Type()
)
tmnxObjType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxObjType.setStatus("current")
_TmnxObjPortId_Type = TmnxPortID
_TmnxObjPortId_Object = MibScalar
tmnxObjPortId = _TmnxObjPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 21),
    _TmnxObjPortId_Type()
)
tmnxObjPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxObjPortId.setStatus("current")
_TmnxObjMdaId_Type = TmnxPortID
_TmnxObjMdaId_Object = MibScalar
tmnxObjMdaId = _TmnxObjMdaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 22),
    _TmnxObjMdaId_Type()
)
tmnxObjMdaId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxObjMdaId.setStatus("current")


class _TmnxObjAppType_Type(Integer32):
    """Custom type tmnxObjAppType based on Integer32"""
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
        *(("accessEgress", 2),
          ("accessIngress", 1),
          ("egress", 6),
          ("ingress", 5),
          ("networkEgress", 4),
          ("networkIngress", 3))
    )


_TmnxObjAppType_Type.__name__ = "Integer32"
_TmnxObjAppType_Object = MibScalar
tmnxObjAppType = _TmnxObjAppType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 23),
    _TmnxObjAppType_Type()
)
tmnxObjAppType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxObjAppType.setStatus("current")
_TmnxObjAppPool_Type = TNamedItemOrEmpty
_TmnxObjAppPool_Object = MibScalar
tmnxObjAppPool = _TmnxObjAppPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 24),
    _TmnxObjAppPool_Type()
)
tmnxObjAppPool.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxObjAppPool.setStatus("current")
_TmnxObjNamedPoolPolicy_Type = TNamedItemOrEmpty
_TmnxObjNamedPoolPolicy_Object = MibScalar
tmnxObjNamedPoolPolicy = _TmnxObjNamedPoolPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 25),
    _TmnxObjNamedPoolPolicy_Type()
)
tmnxObjNamedPoolPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxObjNamedPoolPolicy.setStatus("current")
_TmnxPortNotifyEtherCrcThreshold_Type = Unsigned32
_TmnxPortNotifyEtherCrcThreshold_Object = MibScalar
tmnxPortNotifyEtherCrcThreshold = _TmnxPortNotifyEtherCrcThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 27),
    _TmnxPortNotifyEtherCrcThreshold_Type()
)
tmnxPortNotifyEtherCrcThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyEtherCrcThreshold.setStatus("current")
_TmnxPortNotifyEtherCrcMultiplier_Type = Unsigned32
_TmnxPortNotifyEtherCrcMultiplier_Object = MibScalar
tmnxPortNotifyEtherCrcMultiplier = _TmnxPortNotifyEtherCrcMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 28),
    _TmnxPortNotifyEtherCrcMultiplier_Type()
)
tmnxPortNotifyEtherCrcMultiplier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyEtherCrcMultiplier.setStatus("current")
_TmnxPortNotifyEtherCrcAlarmValue_Type = TmnxPortEtherCrcMonReportValue
_TmnxPortNotifyEtherCrcAlarmValue_Object = MibScalar
tmnxPortNotifyEtherCrcAlarmValue = _TmnxPortNotifyEtherCrcAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 29),
    _TmnxPortNotifyEtherCrcAlarmValue_Type()
)
tmnxPortNotifyEtherCrcAlarmValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxPortNotifyEtherCrcAlarmValue.setStatus("current")
_TmnxObjAppResvSizeOld_Type = Unsigned32
_TmnxObjAppResvSizeOld_Object = MibScalar
tmnxObjAppResvSizeOld = _TmnxObjAppResvSizeOld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 30),
    _TmnxObjAppResvSizeOld_Type()
)
tmnxObjAppResvSizeOld.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxObjAppResvSizeOld.setStatus("current")
if mibBuilder.loadTexts:
    tmnxObjAppResvSizeOld.setUnits("kilo-bytes")


class _TmnxDDMLaneIdOrModule_Type(Unsigned32):
    """Custom type tmnxDDMLaneIdOrModule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )


_TmnxDDMLaneIdOrModule_Type.__name__ = "Unsigned32"
_TmnxDDMLaneIdOrModule_Object = MibScalar
tmnxDDMLaneIdOrModule = _TmnxDDMLaneIdOrModule_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 7, 31),
    _TmnxDDMLaneIdOrModule_Type()
)
tmnxDDMLaneIdOrModule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDDMLaneIdOrModule.setStatus("current")
_TmnxFRObjs_ObjectIdentity = ObjectIdentity
tmnxFRObjs = _TmnxFRObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9)
)
_TmnxFRDlcmiTable_Object = MibTable
tmnxFRDlcmiTable = _TmnxFRDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxFRDlcmiTable.setStatus("current")
_TmnxFRDlcmiEntry_Object = MibTableRow
tmnxFRDlcmiEntry = _TmnxFRDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1)
)
tmnxFRDlcmiEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxFRDlcmiEntry.setStatus("current")


class _TmnxFRDlcmiMode_Type(Integer32):
    """Custom type tmnxFRDlcmiMode based on Integer32"""
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
        *(("bidir", 3),
          ("dce", 2),
          ("dte", 1))
    )


_TmnxFRDlcmiMode_Type.__name__ = "Integer32"
_TmnxFRDlcmiMode_Object = MibTableColumn
tmnxFRDlcmiMode = _TmnxFRDlcmiMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 1),
    _TmnxFRDlcmiMode_Type()
)
tmnxFRDlcmiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFRDlcmiMode.setStatus("current")


class _TmnxFRDlcmiN392Dce_Type(Integer32):
    """Custom type tmnxFRDlcmiN392Dce based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxFRDlcmiN392Dce_Type.__name__ = "Integer32"
_TmnxFRDlcmiN392Dce_Object = MibTableColumn
tmnxFRDlcmiN392Dce = _TmnxFRDlcmiN392Dce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 2),
    _TmnxFRDlcmiN392Dce_Type()
)
tmnxFRDlcmiN392Dce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFRDlcmiN392Dce.setStatus("current")


class _TmnxFRDlcmiN393Dce_Type(Integer32):
    """Custom type tmnxFRDlcmiN393Dce based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxFRDlcmiN393Dce_Type.__name__ = "Integer32"
_TmnxFRDlcmiN393Dce_Object = MibTableColumn
tmnxFRDlcmiN393Dce = _TmnxFRDlcmiN393Dce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 3),
    _TmnxFRDlcmiN393Dce_Type()
)
tmnxFRDlcmiN393Dce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFRDlcmiN393Dce.setStatus("current")


class _TmnxFRDlcmiT392Dce_Type(Integer32):
    """Custom type tmnxFRDlcmiT392Dce based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_TmnxFRDlcmiT392Dce_Type.__name__ = "Integer32"
_TmnxFRDlcmiT392Dce_Object = MibTableColumn
tmnxFRDlcmiT392Dce = _TmnxFRDlcmiT392Dce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 4),
    _TmnxFRDlcmiT392Dce_Type()
)
tmnxFRDlcmiT392Dce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFRDlcmiT392Dce.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiT392Dce.setUnits("seconds")
_TmnxFRDlcmiTxStatusEnqMsgs_Type = Counter32
_TmnxFRDlcmiTxStatusEnqMsgs_Object = MibTableColumn
tmnxFRDlcmiTxStatusEnqMsgs = _TmnxFRDlcmiTxStatusEnqMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 5),
    _TmnxFRDlcmiTxStatusEnqMsgs_Type()
)
tmnxFRDlcmiTxStatusEnqMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiTxStatusEnqMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiTxStatusEnqMsgs.setUnits("messages")
_TmnxFRDlcmiRxStatusEnqMsgs_Type = Counter32
_TmnxFRDlcmiRxStatusEnqMsgs_Object = MibTableColumn
tmnxFRDlcmiRxStatusEnqMsgs = _TmnxFRDlcmiRxStatusEnqMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 6),
    _TmnxFRDlcmiRxStatusEnqMsgs_Type()
)
tmnxFRDlcmiRxStatusEnqMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiRxStatusEnqMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiRxStatusEnqMsgs.setUnits("messages")
_TmnxFRDlcmiStatusEnqMsgTimeouts_Type = Counter32
_TmnxFRDlcmiStatusEnqMsgTimeouts_Object = MibTableColumn
tmnxFRDlcmiStatusEnqMsgTimeouts = _TmnxFRDlcmiStatusEnqMsgTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 7),
    _TmnxFRDlcmiStatusEnqMsgTimeouts_Type()
)
tmnxFRDlcmiStatusEnqMsgTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiStatusEnqMsgTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiStatusEnqMsgTimeouts.setUnits("messages")
_TmnxFRDlcmiTxStatusMsgs_Type = Counter32
_TmnxFRDlcmiTxStatusMsgs_Object = MibTableColumn
tmnxFRDlcmiTxStatusMsgs = _TmnxFRDlcmiTxStatusMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 8),
    _TmnxFRDlcmiTxStatusMsgs_Type()
)
tmnxFRDlcmiTxStatusMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiTxStatusMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiTxStatusMsgs.setUnits("messages")
_TmnxFRDlcmiRxStatusMsgs_Type = Counter32
_TmnxFRDlcmiRxStatusMsgs_Object = MibTableColumn
tmnxFRDlcmiRxStatusMsgs = _TmnxFRDlcmiRxStatusMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 9),
    _TmnxFRDlcmiRxStatusMsgs_Type()
)
tmnxFRDlcmiRxStatusMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiRxStatusMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiRxStatusMsgs.setUnits("messages")
_TmnxFRDlcmiStatusMsgTimeouts_Type = Counter32
_TmnxFRDlcmiStatusMsgTimeouts_Object = MibTableColumn
tmnxFRDlcmiStatusMsgTimeouts = _TmnxFRDlcmiStatusMsgTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 10),
    _TmnxFRDlcmiStatusMsgTimeouts_Type()
)
tmnxFRDlcmiStatusMsgTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiStatusMsgTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiStatusMsgTimeouts.setUnits("messages")
_TmnxFRDlcmiDiscardedMsgs_Type = Counter32
_TmnxFRDlcmiDiscardedMsgs_Object = MibTableColumn
tmnxFRDlcmiDiscardedMsgs = _TmnxFRDlcmiDiscardedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 11),
    _TmnxFRDlcmiDiscardedMsgs_Type()
)
tmnxFRDlcmiDiscardedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiDiscardedMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiDiscardedMsgs.setUnits("messages")
_TmnxFRDlcmiInvRxSeqNumMsgs_Type = Counter32
_TmnxFRDlcmiInvRxSeqNumMsgs_Object = MibTableColumn
tmnxFRDlcmiInvRxSeqNumMsgs = _TmnxFRDlcmiInvRxSeqNumMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 1, 1, 12),
    _TmnxFRDlcmiInvRxSeqNumMsgs_Type()
)
tmnxFRDlcmiInvRxSeqNumMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFRDlcmiInvRxSeqNumMsgs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFRDlcmiInvRxSeqNumMsgs.setUnits("messages")
_TmnxFrIntfTable_Object = MibTable
tmnxFrIntfTable = _TmnxFrIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 2)
)
if mibBuilder.loadTexts:
    tmnxFrIntfTable.setStatus("current")
_TmnxFrIntfEntry_Object = MibTableRow
tmnxFrIntfEntry = _TmnxFrIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 2, 1)
)
tmnxFrIntfEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxFrIntfEntry.setStatus("current")


class _TmnxFrIntfFrf12Mode_Type(TmnxEnabledDisabled):
    """Custom type tmnxFrIntfFrf12Mode based on TmnxEnabledDisabled"""


_TmnxFrIntfFrf12Mode_Object = MibTableColumn
tmnxFrIntfFrf12Mode = _TmnxFrIntfFrf12Mode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 2, 1, 1),
    _TmnxFrIntfFrf12Mode_Type()
)
tmnxFrIntfFrf12Mode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFrIntfFrf12Mode.setStatus("current")


class _TmnxFrIntfLinkId_Type(SnmpAdminString):
    """Custom type tmnxFrIntfLinkId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_TmnxFrIntfLinkId_Type.__name__ = "SnmpAdminString"
_TmnxFrIntfLinkId_Object = MibTableColumn
tmnxFrIntfLinkId = _TmnxFrIntfLinkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 2, 1, 2),
    _TmnxFrIntfLinkId_Type()
)
tmnxFrIntfLinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFrIntfLinkId.setStatus("current")
_TmnxFrIntfLastChanged_Type = TimeStamp
_TmnxFrIntfLastChanged_Object = MibTableColumn
tmnxFrIntfLastChanged = _TmnxFrIntfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 2, 1, 3),
    _TmnxFrIntfLastChanged_Type()
)
tmnxFrIntfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFrIntfLastChanged.setStatus("current")
_TmnxFrf12IntfTable_Object = MibTable
tmnxFrf12IntfTable = _TmnxFrf12IntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 3)
)
if mibBuilder.loadTexts:
    tmnxFrf12IntfTable.setStatus("current")
_TmnxFrf12IntfEntry_Object = MibTableRow
tmnxFrf12IntfEntry = _TmnxFrf12IntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 3, 1)
)
tmnxFrf12IntfEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxFrf12IntfEntry.setStatus("current")


class _TmnxFrf12IntfFragmentThreshold_Type(Unsigned32):
    """Custom type tmnxFrf12IntfFragmentThreshold based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 512),
    )


_TmnxFrf12IntfFragmentThreshold_Type.__name__ = "Unsigned32"
_TmnxFrf12IntfFragmentThreshold_Object = MibTableColumn
tmnxFrf12IntfFragmentThreshold = _TmnxFrf12IntfFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 3, 1, 1),
    _TmnxFrf12IntfFragmentThreshold_Type()
)
tmnxFrf12IntfFragmentThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFrf12IntfFragmentThreshold.setStatus("current")


class _TmnxFrf12IntfEgrQoSProfId_Type(TMcFrQoSProfileId):
    """Custom type tmnxFrf12IntfEgrQoSProfId based on TMcFrQoSProfileId"""
    defaultValue = 0


_TmnxFrf12IntfEgrQoSProfId_Object = MibTableColumn
tmnxFrf12IntfEgrQoSProfId = _TmnxFrf12IntfEgrQoSProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 3, 1, 2),
    _TmnxFrf12IntfEgrQoSProfId_Type()
)
tmnxFrf12IntfEgrQoSProfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFrf12IntfEgrQoSProfId.setStatus("current")
_TmnxFrf12IntfLastChanged_Type = TimeStamp
_TmnxFrf12IntfLastChanged_Object = MibTableColumn
tmnxFrf12IntfLastChanged = _TmnxFrf12IntfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 9, 3, 1, 3),
    _TmnxFrf12IntfLastChanged_Type()
)
tmnxFrf12IntfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFrf12IntfLastChanged.setStatus("current")
_TmnxQosAppObjs_ObjectIdentity = ObjectIdentity
tmnxQosAppObjs = _TmnxQosAppObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10)
)
_TmnxQosPoolAppTable_Object = MibTable
tmnxQosPoolAppTable = _TmnxQosPoolAppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2)
)
if mibBuilder.loadTexts:
    tmnxQosPoolAppTable.setStatus("current")
_TmnxQosPoolAppEntry_Object = MibTableRow
tmnxQosPoolAppEntry = _TmnxQosPoolAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1)
)
tmnxQosPoolAppEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxObjectType"),
    (0, "TIMETRA-PORT-MIB", "tmnxObjectId"),
    (0, "TIMETRA-PORT-MIB", "tmnxObjectAppType"),
    (0, "TIMETRA-PORT-MIB", "tmnxObjectAppPool"),
)
if mibBuilder.loadTexts:
    tmnxQosPoolAppEntry.setStatus("current")


class _TmnxObjectType_Type(Integer32):
    """Custom type tmnxObjectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              51)
        )
    )
    namedValues = NamedValues(
        *(("bundle", 4),
          ("mda", 1),
          ("mpointQueues", 51),
          ("port", 2),
          ("unused", 3))
    )


_TmnxObjectType_Type.__name__ = "Integer32"
_TmnxObjectType_Object = MibTableColumn
tmnxObjectType = _TmnxObjectType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 1),
    _TmnxObjectType_Type()
)
tmnxObjectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxObjectType.setStatus("current")
_TmnxObjectId_Type = TmnxPortID
_TmnxObjectId_Object = MibTableColumn
tmnxObjectId = _TmnxObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 2),
    _TmnxObjectId_Type()
)
tmnxObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxObjectId.setStatus("current")


class _TmnxObjectAppType_Type(Integer32):
    """Custom type tmnxObjectAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              51)
        )
    )
    namedValues = NamedValues(
        *(("accessEgress", 2),
          ("accessIngress", 1),
          ("networkEgress", 4),
          ("networkIngress", 3),
          ("system", 51))
    )


_TmnxObjectAppType_Type.__name__ = "Integer32"
_TmnxObjectAppType_Object = MibTableColumn
tmnxObjectAppType = _TmnxObjectAppType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 3),
    _TmnxObjectAppType_Type()
)
tmnxObjectAppType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxObjectAppType.setStatus("current")
_TmnxObjectAppPool_Type = TNamedItem
_TmnxObjectAppPool_Object = MibTableColumn
tmnxObjectAppPool = _TmnxObjectAppPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 4),
    _TmnxObjectAppPool_Type()
)
tmnxObjectAppPool.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxObjectAppPool.setStatus("current")
_TmnxObjectAppPoolRowStatus_Type = RowStatus
_TmnxObjectAppPoolRowStatus_Object = MibTableColumn
tmnxObjectAppPoolRowStatus = _TmnxObjectAppPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 5),
    _TmnxObjectAppPoolRowStatus_Type()
)
tmnxObjectAppPoolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxObjectAppPoolRowStatus.setStatus("current")


class _TmnxObjectAppResvCbs_Type(Integer32):
    """Custom type tmnxObjectAppResvCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_TmnxObjectAppResvCbs_Type.__name__ = "Integer32"
_TmnxObjectAppResvCbs_Object = MibTableColumn
tmnxObjectAppResvCbs = _TmnxObjectAppResvCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 6),
    _TmnxObjectAppResvCbs_Type()
)
tmnxObjectAppResvCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxObjectAppResvCbs.setStatus("current")


class _TmnxObjectAppSlopePolicy_Type(TNamedItem):
    """Custom type tmnxObjectAppSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxObjectAppSlopePolicy_Object = MibTableColumn
tmnxObjectAppSlopePolicy = _TmnxObjectAppSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 7),
    _TmnxObjectAppSlopePolicy_Type()
)
tmnxObjectAppSlopePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxObjectAppSlopePolicy.setStatus("current")


class _TmnxObjectAppPoolSize_Type(Integer32):
    """Custom type tmnxObjectAppPoolSize based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_TmnxObjectAppPoolSize_Type.__name__ = "Integer32"
_TmnxObjectAppPoolSize_Object = MibTableColumn
tmnxObjectAppPoolSize = _TmnxObjectAppPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 8),
    _TmnxObjectAppPoolSize_Type()
)
tmnxObjectAppPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxObjectAppPoolSize.setStatus("current")


class _TmnxObjectAppResvCbsAmbrAlrmStep_Type(Integer32):
    """Custom type tmnxObjectAppResvCbsAmbrAlrmStep based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxObjectAppResvCbsAmbrAlrmStep_Type.__name__ = "Integer32"
_TmnxObjectAppResvCbsAmbrAlrmStep_Object = MibTableColumn
tmnxObjectAppResvCbsAmbrAlrmStep = _TmnxObjectAppResvCbsAmbrAlrmStep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 9),
    _TmnxObjectAppResvCbsAmbrAlrmStep_Type()
)
tmnxObjectAppResvCbsAmbrAlrmStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxObjectAppResvCbsAmbrAlrmStep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxObjectAppResvCbsAmbrAlrmStep.setUnits("percent")


class _TmnxObjectAppResvCbsAmbrAlrmMax_Type(Integer32):
    """Custom type tmnxObjectAppResvCbsAmbrAlrmMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxObjectAppResvCbsAmbrAlrmMax_Type.__name__ = "Integer32"
_TmnxObjectAppResvCbsAmbrAlrmMax_Object = MibTableColumn
tmnxObjectAppResvCbsAmbrAlrmMax = _TmnxObjectAppResvCbsAmbrAlrmMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 10),
    _TmnxObjectAppResvCbsAmbrAlrmMax_Type()
)
tmnxObjectAppResvCbsAmbrAlrmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxObjectAppResvCbsAmbrAlrmMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxObjectAppResvCbsAmbrAlrmMax.setUnits("percent")


class _TmnxObjectAppAmbrAlrmThresh_Type(Integer32):
    """Custom type tmnxObjectAppAmbrAlrmThresh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxObjectAppAmbrAlrmThresh_Type.__name__ = "Integer32"
_TmnxObjectAppAmbrAlrmThresh_Object = MibTableColumn
tmnxObjectAppAmbrAlrmThresh = _TmnxObjectAppAmbrAlrmThresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 11),
    _TmnxObjectAppAmbrAlrmThresh_Type()
)
tmnxObjectAppAmbrAlrmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxObjectAppAmbrAlrmThresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxObjectAppAmbrAlrmThresh.setUnits("percent")


class _TmnxObjectAppRedAlrmThresh_Type(Integer32):
    """Custom type tmnxObjectAppRedAlrmThresh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxObjectAppRedAlrmThresh_Type.__name__ = "Integer32"
_TmnxObjectAppRedAlrmThresh_Object = MibTableColumn
tmnxObjectAppRedAlrmThresh = _TmnxObjectAppRedAlrmThresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 10, 2, 1, 12),
    _TmnxObjectAppRedAlrmThresh_Type()
)
tmnxObjectAppRedAlrmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxObjectAppRedAlrmThresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxObjectAppRedAlrmThresh.setUnits("percent")
_TmnxATMObjs_ObjectIdentity = ObjectIdentity
tmnxATMObjs = _TmnxATMObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11)
)
_TmnxATMIntfTable_Object = MibTable
tmnxATMIntfTable = _TmnxATMIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxATMIntfTable.setStatus("current")
_TmnxATMIntfEntry_Object = MibTableRow
tmnxATMIntfEntry = _TmnxATMIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1, 1)
)
tmnxATMIntfEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxATMIntfEntry.setStatus("current")


class _TmnxATMIntfCellFormat_Type(Integer32):
    """Custom type tmnxATMIntfCellFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_TmnxATMIntfCellFormat_Type.__name__ = "Integer32"
_TmnxATMIntfCellFormat_Object = MibTableColumn
tmnxATMIntfCellFormat = _TmnxATMIntfCellFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1, 1, 1),
    _TmnxATMIntfCellFormat_Type()
)
tmnxATMIntfCellFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxATMIntfCellFormat.setStatus("current")


class _TmnxATMIntfMinVpValue_Type(Integer32):
    """Custom type tmnxATMIntfMinVpValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TmnxATMIntfMinVpValue_Type.__name__ = "Integer32"
_TmnxATMIntfMinVpValue_Object = MibTableColumn
tmnxATMIntfMinVpValue = _TmnxATMIntfMinVpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1, 1, 2),
    _TmnxATMIntfMinVpValue_Type()
)
tmnxATMIntfMinVpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxATMIntfMinVpValue.setStatus("current")


class _TmnxATMIntfMapping_Type(Integer32):
    """Custom type tmnxATMIntfMapping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("plcp", 2))
    )


_TmnxATMIntfMapping_Type.__name__ = "Integer32"
_TmnxATMIntfMapping_Object = MibTableColumn
tmnxATMIntfMapping = _TmnxATMIntfMapping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1, 1, 3),
    _TmnxATMIntfMapping_Type()
)
tmnxATMIntfMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxATMIntfMapping.setStatus("current")


class _TmnxATMIntfCustomBufferMode_Type(TruthValue):
    """Custom type tmnxATMIntfCustomBufferMode based on TruthValue"""


_TmnxATMIntfCustomBufferMode_Object = MibTableColumn
tmnxATMIntfCustomBufferMode = _TmnxATMIntfCustomBufferMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1, 1, 4),
    _TmnxATMIntfCustomBufferMode_Type()
)
tmnxATMIntfCustomBufferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxATMIntfCustomBufferMode.setStatus("current")


class _TmnxATMIntfBufferPool_Type(Integer32):
    """Custom type tmnxATMIntfBufferPool based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxATMIntfBufferPool_Type.__name__ = "Integer32"
_TmnxATMIntfBufferPool_Object = MibTableColumn
tmnxATMIntfBufferPool = _TmnxATMIntfBufferPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1, 1, 5),
    _TmnxATMIntfBufferPool_Type()
)
tmnxATMIntfBufferPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxATMIntfBufferPool.setStatus("current")


class _TmnxATMIntfVcThreshold_Type(Integer32):
    """Custom type tmnxATMIntfVcThreshold based on Integer32"""
    defaultValue = 190

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(190, 117000),
    )


_TmnxATMIntfVcThreshold_Type.__name__ = "Integer32"
_TmnxATMIntfVcThreshold_Object = MibTableColumn
tmnxATMIntfVcThreshold = _TmnxATMIntfVcThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 1, 1, 6),
    _TmnxATMIntfVcThreshold_Type()
)
tmnxATMIntfVcThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxATMIntfVcThreshold.setStatus("current")
_TmnxPortATMVpShaperTblLastCh_Type = TimeStamp
_TmnxPortATMVpShaperTblLastCh_Object = MibScalar
tmnxPortATMVpShaperTblLastCh = _TmnxPortATMVpShaperTblLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 2),
    _TmnxPortATMVpShaperTblLastCh_Type()
)
tmnxPortATMVpShaperTblLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortATMVpShaperTblLastCh.setStatus("current")
_TmnxPortATMVpShaperTable_Object = MibTable
tmnxPortATMVpShaperTable = _TmnxPortATMVpShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 3)
)
if mibBuilder.loadTexts:
    tmnxPortATMVpShaperTable.setStatus("current")
_TmnxPortATMVpShaperEntry_Object = MibTableRow
tmnxPortATMVpShaperEntry = _TmnxPortATMVpShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 3, 1)
)
tmnxPortATMVpShaperEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortATMVpShaperVpi"),
)
if mibBuilder.loadTexts:
    tmnxPortATMVpShaperEntry.setStatus("current")
_TmnxPortATMVpShaperVpi_Type = AtmVpIdentifier
_TmnxPortATMVpShaperVpi_Object = MibTableColumn
tmnxPortATMVpShaperVpi = _TmnxPortATMVpShaperVpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 3, 1, 1),
    _TmnxPortATMVpShaperVpi_Type()
)
tmnxPortATMVpShaperVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortATMVpShaperVpi.setStatus("current")
_TmnxPortATMVpShaperRowStatus_Type = RowStatus
_TmnxPortATMVpShaperRowStatus_Object = MibTableColumn
tmnxPortATMVpShaperRowStatus = _TmnxPortATMVpShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 3, 1, 2),
    _TmnxPortATMVpShaperRowStatus_Type()
)
tmnxPortATMVpShaperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortATMVpShaperRowStatus.setStatus("current")
_TmnxPortATMVpShaperLastMgmtCh_Type = TimeStamp
_TmnxPortATMVpShaperLastMgmtCh_Object = MibTableColumn
tmnxPortATMVpShaperLastMgmtCh = _TmnxPortATMVpShaperLastMgmtCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 3, 1, 3),
    _TmnxPortATMVpShaperLastMgmtCh_Type()
)
tmnxPortATMVpShaperLastMgmtCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortATMVpShaperLastMgmtCh.setStatus("current")


class _TmnxPortATMVpShaperEgrAtd_Type(AtmTrafficDescrParamIndex):
    """Custom type tmnxPortATMVpShaperEgrAtd based on AtmTrafficDescrParamIndex"""
    subtypeSpec = AtmTrafficDescrParamIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxPortATMVpShaperEgrAtd_Type.__name__ = "AtmTrafficDescrParamIndex"
_TmnxPortATMVpShaperEgrAtd_Object = MibTableColumn
tmnxPortATMVpShaperEgrAtd = _TmnxPortATMVpShaperEgrAtd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 11, 3, 1, 4),
    _TmnxPortATMVpShaperEgrAtd_Type()
)
tmnxPortATMVpShaperEgrAtd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPortATMVpShaperEgrAtd.setStatus("current")
_TmnxPortStatsObjs_ObjectIdentity = ObjectIdentity
tmnxPortStatsObjs = _TmnxPortStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12)
)
_TmnxPortNetIngressStatsTable_Object = MibTable
tmnxPortNetIngressStatsTable = _TmnxPortNetIngressStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxPortNetIngressStatsTable.setStatus("current")
_TmnxPortNetIngressStatsEntry_Object = MibTableRow
tmnxPortNetIngressStatsEntry = _TmnxPortNetIngressStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1)
)
tmnxPortNetIngressStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortNetIngressQueueIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortNetIngressStatsEntry.setStatus("current")


class _TmnxPortNetIngressQueueIndex_Type(TQueueId):
    """Custom type tmnxPortNetIngressQueueIndex based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxPortNetIngressQueueIndex_Type.__name__ = "TQueueId"
_TmnxPortNetIngressQueueIndex_Object = MibTableColumn
tmnxPortNetIngressQueueIndex = _TmnxPortNetIngressQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 1),
    _TmnxPortNetIngressQueueIndex_Type()
)
tmnxPortNetIngressQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortNetIngressQueueIndex.setStatus("current")
_TmnxPortNetIngressFwdInProfPkts_Type = Counter64
_TmnxPortNetIngressFwdInProfPkts_Object = MibTableColumn
tmnxPortNetIngressFwdInProfPkts = _TmnxPortNetIngressFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 2),
    _TmnxPortNetIngressFwdInProfPkts_Type()
)
tmnxPortNetIngressFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressFwdInProfPkts.setStatus("current")
_TmnxPortNetIngressFwdOutProfPkts_Type = Counter64
_TmnxPortNetIngressFwdOutProfPkts_Object = MibTableColumn
tmnxPortNetIngressFwdOutProfPkts = _TmnxPortNetIngressFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 3),
    _TmnxPortNetIngressFwdOutProfPkts_Type()
)
tmnxPortNetIngressFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressFwdOutProfPkts.setStatus("current")
_TmnxPortNetIngressFwdInProfOcts_Type = Counter64
_TmnxPortNetIngressFwdInProfOcts_Object = MibTableColumn
tmnxPortNetIngressFwdInProfOcts = _TmnxPortNetIngressFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 4),
    _TmnxPortNetIngressFwdInProfOcts_Type()
)
tmnxPortNetIngressFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressFwdInProfOcts.setStatus("current")
_TmnxPortNetIngressFwdOutProfOcts_Type = Counter64
_TmnxPortNetIngressFwdOutProfOcts_Object = MibTableColumn
tmnxPortNetIngressFwdOutProfOcts = _TmnxPortNetIngressFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 5),
    _TmnxPortNetIngressFwdOutProfOcts_Type()
)
tmnxPortNetIngressFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressFwdOutProfOcts.setStatus("current")
_TmnxPortNetIngressDroInProfPkts_Type = Counter64
_TmnxPortNetIngressDroInProfPkts_Object = MibTableColumn
tmnxPortNetIngressDroInProfPkts = _TmnxPortNetIngressDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 6),
    _TmnxPortNetIngressDroInProfPkts_Type()
)
tmnxPortNetIngressDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressDroInProfPkts.setStatus("current")
_TmnxPortNetIngressDroOutProfPkts_Type = Counter64
_TmnxPortNetIngressDroOutProfPkts_Object = MibTableColumn
tmnxPortNetIngressDroOutProfPkts = _TmnxPortNetIngressDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 7),
    _TmnxPortNetIngressDroOutProfPkts_Type()
)
tmnxPortNetIngressDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressDroOutProfPkts.setStatus("current")
_TmnxPortNetIngressDroInProfOcts_Type = Counter64
_TmnxPortNetIngressDroInProfOcts_Object = MibTableColumn
tmnxPortNetIngressDroInProfOcts = _TmnxPortNetIngressDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 8),
    _TmnxPortNetIngressDroInProfOcts_Type()
)
tmnxPortNetIngressDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressDroInProfOcts.setStatus("current")
_TmnxPortNetIngressDroOutProfOcts_Type = Counter64
_TmnxPortNetIngressDroOutProfOcts_Object = MibTableColumn
tmnxPortNetIngressDroOutProfOcts = _TmnxPortNetIngressDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 1, 1, 9),
    _TmnxPortNetIngressDroOutProfOcts_Type()
)
tmnxPortNetIngressDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetIngressDroOutProfOcts.setStatus("current")
_TmnxPortNetEgressStatsTable_Object = MibTable
tmnxPortNetEgressStatsTable = _TmnxPortNetEgressStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2)
)
if mibBuilder.loadTexts:
    tmnxPortNetEgressStatsTable.setStatus("current")
_TmnxPortNetEgressStatsEntry_Object = MibTableRow
tmnxPortNetEgressStatsEntry = _TmnxPortNetEgressStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1)
)
tmnxPortNetEgressStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortNetEgressQueueIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortNetEgressStatsEntry.setStatus("current")


class _TmnxPortNetEgressQueueIndex_Type(TQueueId):
    """Custom type tmnxPortNetEgressQueueIndex based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxPortNetEgressQueueIndex_Type.__name__ = "TQueueId"
_TmnxPortNetEgressQueueIndex_Object = MibTableColumn
tmnxPortNetEgressQueueIndex = _TmnxPortNetEgressQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 1),
    _TmnxPortNetEgressQueueIndex_Type()
)
tmnxPortNetEgressQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueIndex.setStatus("current")
_TmnxPortNetEgressFwdInProfPkts_Type = Counter64
_TmnxPortNetEgressFwdInProfPkts_Object = MibTableColumn
tmnxPortNetEgressFwdInProfPkts = _TmnxPortNetEgressFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 2),
    _TmnxPortNetEgressFwdInProfPkts_Type()
)
tmnxPortNetEgressFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressFwdInProfPkts.setStatus("current")
_TmnxPortNetEgressFwdOutProfPkts_Type = Counter64
_TmnxPortNetEgressFwdOutProfPkts_Object = MibTableColumn
tmnxPortNetEgressFwdOutProfPkts = _TmnxPortNetEgressFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 3),
    _TmnxPortNetEgressFwdOutProfPkts_Type()
)
tmnxPortNetEgressFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressFwdOutProfPkts.setStatus("current")
_TmnxPortNetEgressFwdInProfOcts_Type = Counter64
_TmnxPortNetEgressFwdInProfOcts_Object = MibTableColumn
tmnxPortNetEgressFwdInProfOcts = _TmnxPortNetEgressFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 4),
    _TmnxPortNetEgressFwdInProfOcts_Type()
)
tmnxPortNetEgressFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressFwdInProfOcts.setStatus("current")
_TmnxPortNetEgressFwdOutProfOcts_Type = Counter64
_TmnxPortNetEgressFwdOutProfOcts_Object = MibTableColumn
tmnxPortNetEgressFwdOutProfOcts = _TmnxPortNetEgressFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 5),
    _TmnxPortNetEgressFwdOutProfOcts_Type()
)
tmnxPortNetEgressFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressFwdOutProfOcts.setStatus("current")
_TmnxPortNetEgressDroInProfPkts_Type = Counter64
_TmnxPortNetEgressDroInProfPkts_Object = MibTableColumn
tmnxPortNetEgressDroInProfPkts = _TmnxPortNetEgressDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 6),
    _TmnxPortNetEgressDroInProfPkts_Type()
)
tmnxPortNetEgressDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressDroInProfPkts.setStatus("current")
_TmnxPortNetEgressDroOutProfPkts_Type = Counter64
_TmnxPortNetEgressDroOutProfPkts_Object = MibTableColumn
tmnxPortNetEgressDroOutProfPkts = _TmnxPortNetEgressDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 7),
    _TmnxPortNetEgressDroOutProfPkts_Type()
)
tmnxPortNetEgressDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressDroOutProfPkts.setStatus("current")
_TmnxPortNetEgressDroInProfOcts_Type = Counter64
_TmnxPortNetEgressDroInProfOcts_Object = MibTableColumn
tmnxPortNetEgressDroInProfOcts = _TmnxPortNetEgressDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 8),
    _TmnxPortNetEgressDroInProfOcts_Type()
)
tmnxPortNetEgressDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressDroInProfOcts.setStatus("current")
_TmnxPortNetEgressDroOutProfOcts_Type = Counter64
_TmnxPortNetEgressDroOutProfOcts_Object = MibTableColumn
tmnxPortNetEgressDroOutProfOcts = _TmnxPortNetEgressDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 2, 1, 9),
    _TmnxPortNetEgressDroOutProfOcts_Type()
)
tmnxPortNetEgressDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressDroOutProfOcts.setStatus("current")
_TmnxCiscoHDLCStatsTable_Object = MibTable
tmnxCiscoHDLCStatsTable = _TmnxCiscoHDLCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3)
)
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatsTable.setStatus("current")
_TmnxCiscoHDLCStatsEntry_Object = MibTableRow
tmnxCiscoHDLCStatsEntry = _TmnxCiscoHDLCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatsEntry.setStatus("current")
_TmnxCiscoHDLCDiscardStatInPkts_Type = Unsigned32
_TmnxCiscoHDLCDiscardStatInPkts_Object = MibTableColumn
tmnxCiscoHDLCDiscardStatInPkts = _TmnxCiscoHDLCDiscardStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 1),
    _TmnxCiscoHDLCDiscardStatInPkts_Type()
)
tmnxCiscoHDLCDiscardStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCDiscardStatInPkts.setStatus("current")
_TmnxCiscoHDLCDiscardStatOutPkts_Type = Unsigned32
_TmnxCiscoHDLCDiscardStatOutPkts_Object = MibTableColumn
tmnxCiscoHDLCDiscardStatOutPkts = _TmnxCiscoHDLCDiscardStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 2),
    _TmnxCiscoHDLCDiscardStatOutPkts_Type()
)
tmnxCiscoHDLCDiscardStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCDiscardStatOutPkts.setStatus("current")
_TmnxCiscoHDLCStatInPkts_Type = Unsigned32
_TmnxCiscoHDLCStatInPkts_Object = MibTableColumn
tmnxCiscoHDLCStatInPkts = _TmnxCiscoHDLCStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 3),
    _TmnxCiscoHDLCStatInPkts_Type()
)
tmnxCiscoHDLCStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatInPkts.setStatus("current")
_TmnxCiscoHDLCStatOutPkts_Type = Unsigned32
_TmnxCiscoHDLCStatOutPkts_Object = MibTableColumn
tmnxCiscoHDLCStatOutPkts = _TmnxCiscoHDLCStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 4),
    _TmnxCiscoHDLCStatOutPkts_Type()
)
tmnxCiscoHDLCStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatOutPkts.setStatus("current")
_TmnxCiscoHDLCStatInOctets_Type = Unsigned32
_TmnxCiscoHDLCStatInOctets_Object = MibTableColumn
tmnxCiscoHDLCStatInOctets = _TmnxCiscoHDLCStatInOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 5),
    _TmnxCiscoHDLCStatInOctets_Type()
)
tmnxCiscoHDLCStatInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatInOctets.setStatus("current")
_TmnxCiscoHDLCStatOutOctets_Type = Unsigned32
_TmnxCiscoHDLCStatOutOctets_Object = MibTableColumn
tmnxCiscoHDLCStatOutOctets = _TmnxCiscoHDLCStatOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 3, 1, 6),
    _TmnxCiscoHDLCStatOutOctets_Type()
)
tmnxCiscoHDLCStatOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCiscoHDLCStatOutOctets.setStatus("current")
_TmnxMcMlpppStatsTable_Object = MibTable
tmnxMcMlpppStatsTable = _TmnxMcMlpppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4)
)
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsTable.setStatus("current")
_TmnxMcMlpppStatsEntry_Object = MibTableRow
tmnxMcMlpppStatsEntry = _TmnxMcMlpppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1)
)
tmnxMcMlpppStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxBundleBundleID"),
    (0, "TIMETRA-PORT-MIB", "tmnxMcMlpppClassIndex"),
)
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsEntry.setStatus("current")
_TmnxMcMlpppClassIndex_Type = TmnxMcMlpppClassIndex
_TmnxMcMlpppClassIndex_Object = MibTableColumn
tmnxMcMlpppClassIndex = _TmnxMcMlpppClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 1),
    _TmnxMcMlpppClassIndex_Type()
)
tmnxMcMlpppClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcMlpppClassIndex.setStatus("current")
_TmnxMcMlpppStatsIngressOct_Type = Counter32
_TmnxMcMlpppStatsIngressOct_Object = MibTableColumn
tmnxMcMlpppStatsIngressOct = _TmnxMcMlpppStatsIngressOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 2),
    _TmnxMcMlpppStatsIngressOct_Type()
)
tmnxMcMlpppStatsIngressOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsIngressOct.setStatus("current")
_TmnxMcMlpppStatsIngressPkt_Type = Counter32
_TmnxMcMlpppStatsIngressPkt_Object = MibTableColumn
tmnxMcMlpppStatsIngressPkt = _TmnxMcMlpppStatsIngressPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 3),
    _TmnxMcMlpppStatsIngressPkt_Type()
)
tmnxMcMlpppStatsIngressPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsIngressPkt.setStatus("current")
_TmnxMcMlpppStatsIngressErrPkt_Type = Counter32
_TmnxMcMlpppStatsIngressErrPkt_Object = MibTableColumn
tmnxMcMlpppStatsIngressErrPkt = _TmnxMcMlpppStatsIngressErrPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 4),
    _TmnxMcMlpppStatsIngressErrPkt_Type()
)
tmnxMcMlpppStatsIngressErrPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsIngressErrPkt.setStatus("current")
_TmnxMcMlpppStatsEgressOct_Type = Counter32
_TmnxMcMlpppStatsEgressOct_Object = MibTableColumn
tmnxMcMlpppStatsEgressOct = _TmnxMcMlpppStatsEgressOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 5),
    _TmnxMcMlpppStatsEgressOct_Type()
)
tmnxMcMlpppStatsEgressOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsEgressOct.setStatus("current")
_TmnxMcMlpppStatsEgressPkt_Type = Counter32
_TmnxMcMlpppStatsEgressPkt_Object = MibTableColumn
tmnxMcMlpppStatsEgressPkt = _TmnxMcMlpppStatsEgressPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 6),
    _TmnxMcMlpppStatsEgressPkt_Type()
)
tmnxMcMlpppStatsEgressPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsEgressPkt.setStatus("current")
_TmnxMcMlpppStatsEgressErrPkt_Type = Counter32
_TmnxMcMlpppStatsEgressErrPkt_Object = MibTableColumn
tmnxMcMlpppStatsEgressErrPkt = _TmnxMcMlpppStatsEgressErrPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 4, 1, 7),
    _TmnxMcMlpppStatsEgressErrPkt_Type()
)
tmnxMcMlpppStatsEgressErrPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcMlpppStatsEgressErrPkt.setStatus("current")
_TmnxPortNetEgrQStatTable_Object = MibTable
tmnxPortNetEgrQStatTable = _TmnxPortNetEgrQStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 5)
)
if mibBuilder.loadTexts:
    tmnxPortNetEgrQStatTable.setStatus("current")
_TmnxPortNetEgrQStatEntry_Object = MibTableRow
tmnxPortNetEgrQStatEntry = _TmnxPortNetEgrQStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 5, 1)
)
tmnxPortNetEgrQStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpInstanceId"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortEgrQosQStatQueueId"),
)
if mibBuilder.loadTexts:
    tmnxPortNetEgrQStatEntry.setStatus("current")
_TmnxPortNetEgrQFwdInProfPkts_Type = Counter64
_TmnxPortNetEgrQFwdInProfPkts_Object = MibTableColumn
tmnxPortNetEgrQFwdInProfPkts = _TmnxPortNetEgrQFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 5, 1, 1),
    _TmnxPortNetEgrQFwdInProfPkts_Type()
)
tmnxPortNetEgrQFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgrQFwdInProfPkts.setStatus("current")
_TmnxPortNetEgrQFwdOutProfPkts_Type = Counter64
_TmnxPortNetEgrQFwdOutProfPkts_Object = MibTableColumn
tmnxPortNetEgrQFwdOutProfPkts = _TmnxPortNetEgrQFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 5, 1, 2),
    _TmnxPortNetEgrQFwdOutProfPkts_Type()
)
tmnxPortNetEgrQFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgrQFwdOutProfPkts.setStatus("current")
_TmnxPortNetEgrQFwdInProfOcts_Type = Counter64
_TmnxPortNetEgrQFwdInProfOcts_Object = MibTableColumn
tmnxPortNetEgrQFwdInProfOcts = _TmnxPortNetEgrQFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 5, 1, 3),
    _TmnxPortNetEgrQFwdInProfOcts_Type()
)
tmnxPortNetEgrQFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgrQFwdInProfOcts.setStatus("current")
_TmnxPortNetEgrQFwdOutProfOcts_Type = Counter64
_TmnxPortNetEgrQFwdOutProfOcts_Object = MibTableColumn
tmnxPortNetEgrQFwdOutProfOcts = _TmnxPortNetEgrQFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 5, 1, 4),
    _TmnxPortNetEgrQFwdOutProfOcts_Type()
)
tmnxPortNetEgrQFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgrQFwdOutProfOcts.setStatus("current")
_TmnxPortNetEgrQDroInProfPkts_Type = Counter64
_TmnxPortNetEgrQDroInProfPkts_Object = MibTableColumn
tmnxPortNetEgrQDroInProfPkts = _TmnxPortNetEgrQDroInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 5, 1, 5),
    _TmnxPortNetEgrQDroInProfPkts_Type()
)
tmnxPortNetEgrQDroInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgrQDroInProfPkts.setStatus("current")
_TmnxPortNetEgrQDroOutProfPkts_Type = Counter64
_TmnxPortNetEgrQDroOutProfPkts_Object = MibTableColumn
tmnxPortNetEgrQDroOutProfPkts = _TmnxPortNetEgrQDroOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 5, 1, 6),
    _TmnxPortNetEgrQDroOutProfPkts_Type()
)
tmnxPortNetEgrQDroOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgrQDroOutProfPkts.setStatus("current")
_TmnxPortNetEgrQDroInProfOcts_Type = Counter64
_TmnxPortNetEgrQDroInProfOcts_Object = MibTableColumn
tmnxPortNetEgrQDroInProfOcts = _TmnxPortNetEgrQDroInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 5, 1, 7),
    _TmnxPortNetEgrQDroInProfOcts_Type()
)
tmnxPortNetEgrQDroInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgrQDroInProfOcts.setStatus("current")
_TmnxPortNetEgrQDroOutProfOcts_Type = Counter64
_TmnxPortNetEgrQDroOutProfOcts_Object = MibTableColumn
tmnxPortNetEgrQDroOutProfOcts = _TmnxPortNetEgrQDroOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 5, 1, 8),
    _TmnxPortNetEgrQDroOutProfOcts_Type()
)
tmnxPortNetEgrQDroOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgrQDroOutProfOcts.setStatus("current")
_TmnxPortCemStatsTable_Object = MibTable
tmnxPortCemStatsTable = _TmnxPortCemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6)
)
if mibBuilder.loadTexts:
    tmnxPortCemStatsTable.setStatus("current")
_TmnxPortCemStatsEntry_Object = MibTableRow
tmnxPortCemStatsEntry = _TmnxPortCemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1)
)
tmnxPortCemStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxPortCemStatsEntry.setStatus("current")


class _TmnxPortCemStatsReportAlarm_Type(Bits):
    """Custom type tmnxPortCemStatsReportAlarm based on Bits"""
    namedValues = NamedValues(
        *(("bfrOverrun", 4),
          ("bfrUnderrun", 5),
          ("malformedPkts", 2),
          ("notUsed", 0),
          ("pktLoss", 3),
          ("rmtFault", 7),
          ("rmtPktLoss", 6),
          ("rmtRdi", 8),
          ("strayPkts", 1))
    )

_TmnxPortCemStatsReportAlarm_Type.__name__ = "Bits"
_TmnxPortCemStatsReportAlarm_Object = MibTableColumn
tmnxPortCemStatsReportAlarm = _TmnxPortCemStatsReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 1),
    _TmnxPortCemStatsReportAlarm_Type()
)
tmnxPortCemStatsReportAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsReportAlarm.setStatus("current")
_TmnxPortCemStatsIgrForwardedPkts_Type = Counter32
_TmnxPortCemStatsIgrForwardedPkts_Object = MibTableColumn
tmnxPortCemStatsIgrForwardedPkts = _TmnxPortCemStatsIgrForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 2),
    _TmnxPortCemStatsIgrForwardedPkts_Type()
)
tmnxPortCemStatsIgrForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsIgrForwardedPkts.setStatus("current")
_TmnxPortCemStatsIgrDroppedPkts_Type = Counter32
_TmnxPortCemStatsIgrDroppedPkts_Object = MibTableColumn
tmnxPortCemStatsIgrDroppedPkts = _TmnxPortCemStatsIgrDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 3),
    _TmnxPortCemStatsIgrDroppedPkts_Type()
)
tmnxPortCemStatsIgrDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsIgrDroppedPkts.setStatus("current")
_TmnxPortCemStatsEgrForwardedPkts_Type = Counter32
_TmnxPortCemStatsEgrForwardedPkts_Object = MibTableColumn
tmnxPortCemStatsEgrForwardedPkts = _TmnxPortCemStatsEgrForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 4),
    _TmnxPortCemStatsEgrForwardedPkts_Type()
)
tmnxPortCemStatsEgrForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrForwardedPkts.setStatus("current")
_TmnxPortCemStatsEgrDroppedPkts_Type = Counter32
_TmnxPortCemStatsEgrDroppedPkts_Object = MibTableColumn
tmnxPortCemStatsEgrDroppedPkts = _TmnxPortCemStatsEgrDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 5),
    _TmnxPortCemStatsEgrDroppedPkts_Type()
)
tmnxPortCemStatsEgrDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrDroppedPkts.setStatus("current")
_TmnxPortCemStatsEgrMissingPkts_Type = Counter32
_TmnxPortCemStatsEgrMissingPkts_Object = MibTableColumn
tmnxPortCemStatsEgrMissingPkts = _TmnxPortCemStatsEgrMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 6),
    _TmnxPortCemStatsEgrMissingPkts_Type()
)
tmnxPortCemStatsEgrMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrMissingPkts.setStatus("current")
_TmnxPortCemStatsEgrPktsReOrder_Type = Counter32
_TmnxPortCemStatsEgrPktsReOrder_Object = MibTableColumn
tmnxPortCemStatsEgrPktsReOrder = _TmnxPortCemStatsEgrPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 7),
    _TmnxPortCemStatsEgrPktsReOrder_Type()
)
tmnxPortCemStatsEgrPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrPktsReOrder.setStatus("current")
_TmnxPortCemStatsEgrJtrBfrURun_Type = Counter32
_TmnxPortCemStatsEgrJtrBfrURun_Object = MibTableColumn
tmnxPortCemStatsEgrJtrBfrURun = _TmnxPortCemStatsEgrJtrBfrURun_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 8),
    _TmnxPortCemStatsEgrJtrBfrURun_Type()
)
tmnxPortCemStatsEgrJtrBfrURun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrJtrBfrURun.setStatus("current")
_TmnxPortCemStatsEgrJtrBfrORun_Type = Counter32
_TmnxPortCemStatsEgrJtrBfrORun_Object = MibTableColumn
tmnxPortCemStatsEgrJtrBfrORun = _TmnxPortCemStatsEgrJtrBfrORun_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 9),
    _TmnxPortCemStatsEgrJtrBfrORun_Type()
)
tmnxPortCemStatsEgrJtrBfrORun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrJtrBfrORun.setStatus("current")
_TmnxPortCemStatsEgrMisOrderDrop_Type = Counter32
_TmnxPortCemStatsEgrMisOrderDrop_Object = MibTableColumn
tmnxPortCemStatsEgrMisOrderDrop = _TmnxPortCemStatsEgrMisOrderDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 10),
    _TmnxPortCemStatsEgrMisOrderDrop_Type()
)
tmnxPortCemStatsEgrMisOrderDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrMisOrderDrop.setStatus("current")
_TmnxPortCemStatsEgrMalformedPkts_Type = Counter32
_TmnxPortCemStatsEgrMalformedPkts_Object = MibTableColumn
tmnxPortCemStatsEgrMalformedPkts = _TmnxPortCemStatsEgrMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 11),
    _TmnxPortCemStatsEgrMalformedPkts_Type()
)
tmnxPortCemStatsEgrMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrMalformedPkts.setStatus("current")
_TmnxPortCemStatsEgrLBitDrop_Type = Counter32
_TmnxPortCemStatsEgrLBitDrop_Object = MibTableColumn
tmnxPortCemStatsEgrLBitDrop = _TmnxPortCemStatsEgrLBitDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 12),
    _TmnxPortCemStatsEgrLBitDrop_Type()
)
tmnxPortCemStatsEgrLBitDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrLBitDrop.setStatus("current")
_TmnxPortCemStatsEgrMultipleDrop_Type = Counter32
_TmnxPortCemStatsEgrMultipleDrop_Object = MibTableColumn
tmnxPortCemStatsEgrMultipleDrop = _TmnxPortCemStatsEgrMultipleDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 13),
    _TmnxPortCemStatsEgrMultipleDrop_Type()
)
tmnxPortCemStatsEgrMultipleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrMultipleDrop.setStatus("current")
_TmnxPortCemStatsEgrESs_Type = Counter32
_TmnxPortCemStatsEgrESs_Object = MibTableColumn
tmnxPortCemStatsEgrESs = _TmnxPortCemStatsEgrESs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 14),
    _TmnxPortCemStatsEgrESs_Type()
)
tmnxPortCemStatsEgrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrESs.setStatus("current")
_TmnxPortCemStatsEgrSESs_Type = Counter32
_TmnxPortCemStatsEgrSESs_Object = MibTableColumn
tmnxPortCemStatsEgrSESs = _TmnxPortCemStatsEgrSESs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 15),
    _TmnxPortCemStatsEgrSESs_Type()
)
tmnxPortCemStatsEgrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrSESs.setStatus("current")
_TmnxPortCemStatsEgrUASs_Type = Counter32
_TmnxPortCemStatsEgrUASs_Object = MibTableColumn
tmnxPortCemStatsEgrUASs = _TmnxPortCemStatsEgrUASs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 16),
    _TmnxPortCemStatsEgrUASs_Type()
)
tmnxPortCemStatsEgrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrUASs.setStatus("current")
_TmnxPortCemStatsEgrFailureCounts_Type = Counter32
_TmnxPortCemStatsEgrFailureCounts_Object = MibTableColumn
tmnxPortCemStatsEgrFailureCounts = _TmnxPortCemStatsEgrFailureCounts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 17),
    _TmnxPortCemStatsEgrFailureCounts_Type()
)
tmnxPortCemStatsEgrFailureCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrFailureCounts.setStatus("current")
_TmnxPortCemStatsEgrURunCounts_Type = Counter32
_TmnxPortCemStatsEgrURunCounts_Object = MibTableColumn
tmnxPortCemStatsEgrURunCounts = _TmnxPortCemStatsEgrURunCounts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 18),
    _TmnxPortCemStatsEgrURunCounts_Type()
)
tmnxPortCemStatsEgrURunCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrURunCounts.setStatus("current")
_TmnxPortCemStatsEgrORunCounts_Type = Counter32
_TmnxPortCemStatsEgrORunCounts_Object = MibTableColumn
tmnxPortCemStatsEgrORunCounts = _TmnxPortCemStatsEgrORunCounts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 19),
    _TmnxPortCemStatsEgrORunCounts_Type()
)
tmnxPortCemStatsEgrORunCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrORunCounts.setStatus("current")
_TmnxPortCemStatsEgrJtrBfrDepth_Type = Gauge32
_TmnxPortCemStatsEgrJtrBfrDepth_Object = MibTableColumn
tmnxPortCemStatsEgrJtrBfrDepth = _TmnxPortCemStatsEgrJtrBfrDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 6, 1, 20),
    _TmnxPortCemStatsEgrJtrBfrDepth_Type()
)
tmnxPortCemStatsEgrJtrBfrDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortCemStatsEgrJtrBfrDepth.setStatus("current")
_TPortNetEgrQGrpPStatTable_Object = MibTable
tPortNetEgrQGrpPStatTable = _TPortNetEgrQGrpPStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7)
)
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStatTable.setStatus("current")
_TPortNetEgrQGrpPStatEntry_Object = MibTableRow
tPortNetEgrQGrpPStatEntry = _TPortNetEgrQGrpPStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1)
)
tPortNetEgrQGrpPStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpName"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpInstanceId"),
    (0, "TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStatQosPolicerId"),
)
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStatEntry.setStatus("current")
_TPortNetEgrQGrpPStatQosPolicerId_Type = TEgrPolicerId
_TPortNetEgrQGrpPStatQosPolicerId_Object = MibTableColumn
tPortNetEgrQGrpPStatQosPolicerId = _TPortNetEgrQGrpPStatQosPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 1),
    _TPortNetEgrQGrpPStatQosPolicerId_Type()
)
tPortNetEgrQGrpPStatQosPolicerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStatQosPolicerId.setStatus("current")
_TPortNetEgrQGrpPStatMode_Type = TmnxEgrPolicerStatMode
_TPortNetEgrQGrpPStatMode_Object = MibTableColumn
tPortNetEgrQGrpPStatMode = _TPortNetEgrQGrpPStatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 2),
    _TPortNetEgrQGrpPStatMode_Type()
)
tPortNetEgrQGrpPStatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStatMode.setStatus("current")
_TPortNetEgrQGrpPStOffInProfPkt_Type = Counter64
_TPortNetEgrQGrpPStOffInProfPkt_Object = MibTableColumn
tPortNetEgrQGrpPStOffInProfPkt = _TPortNetEgrQGrpPStOffInProfPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 3),
    _TPortNetEgrQGrpPStOffInProfPkt_Type()
)
tPortNetEgrQGrpPStOffInProfPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffInProfPkt.setStatus("current")
_TPortNetEgrQGrpPStOffInProfPktL_Type = Counter32
_TPortNetEgrQGrpPStOffInProfPktL_Object = MibTableColumn
tPortNetEgrQGrpPStOffInProfPktL = _TPortNetEgrQGrpPStOffInProfPktL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 4),
    _TPortNetEgrQGrpPStOffInProfPktL_Type()
)
tPortNetEgrQGrpPStOffInProfPktL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffInProfPktL.setStatus("current")
_TPortNetEgrQGrpPStOffInProfPktH_Type = Counter32
_TPortNetEgrQGrpPStOffInProfPktH_Object = MibTableColumn
tPortNetEgrQGrpPStOffInProfPktH = _TPortNetEgrQGrpPStOffInProfPktH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 5),
    _TPortNetEgrQGrpPStOffInProfPktH_Type()
)
tPortNetEgrQGrpPStOffInProfPktH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffInProfPktH.setStatus("current")
_TPortNetEgrQGrpPStFwdInProfPkt_Type = Counter64
_TPortNetEgrQGrpPStFwdInProfPkt_Object = MibTableColumn
tPortNetEgrQGrpPStFwdInProfPkt = _TPortNetEgrQGrpPStFwdInProfPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 6),
    _TPortNetEgrQGrpPStFwdInProfPkt_Type()
)
tPortNetEgrQGrpPStFwdInProfPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdInProfPkt.setStatus("current")
_TPortNetEgrQGrpPStFwdInProfPktL_Type = Counter32
_TPortNetEgrQGrpPStFwdInProfPktL_Object = MibTableColumn
tPortNetEgrQGrpPStFwdInProfPktL = _TPortNetEgrQGrpPStFwdInProfPktL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 7),
    _TPortNetEgrQGrpPStFwdInProfPktL_Type()
)
tPortNetEgrQGrpPStFwdInProfPktL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdInProfPktL.setStatus("current")
_TPortNetEgrQGrpPStFwdInProfPktH_Type = Counter32
_TPortNetEgrQGrpPStFwdInProfPktH_Object = MibTableColumn
tPortNetEgrQGrpPStFwdInProfPktH = _TPortNetEgrQGrpPStFwdInProfPktH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 8),
    _TPortNetEgrQGrpPStFwdInProfPktH_Type()
)
tPortNetEgrQGrpPStFwdInProfPktH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdInProfPktH.setStatus("current")
_TPortNetEgrQGrpPStDrpInProfPkt_Type = Counter64
_TPortNetEgrQGrpPStDrpInProfPkt_Object = MibTableColumn
tPortNetEgrQGrpPStDrpInProfPkt = _TPortNetEgrQGrpPStDrpInProfPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 9),
    _TPortNetEgrQGrpPStDrpInProfPkt_Type()
)
tPortNetEgrQGrpPStDrpInProfPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpInProfPkt.setStatus("current")
_TPortNetEgrQGrpPStDrpInProfPktL_Type = Counter32
_TPortNetEgrQGrpPStDrpInProfPktL_Object = MibTableColumn
tPortNetEgrQGrpPStDrpInProfPktL = _TPortNetEgrQGrpPStDrpInProfPktL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 10),
    _TPortNetEgrQGrpPStDrpInProfPktL_Type()
)
tPortNetEgrQGrpPStDrpInProfPktL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpInProfPktL.setStatus("current")
_TPortNetEgrQGrpPStDrpInProfPktH_Type = Counter32
_TPortNetEgrQGrpPStDrpInProfPktH_Object = MibTableColumn
tPortNetEgrQGrpPStDrpInProfPktH = _TPortNetEgrQGrpPStDrpInProfPktH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 11),
    _TPortNetEgrQGrpPStDrpInProfPktH_Type()
)
tPortNetEgrQGrpPStDrpInProfPktH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpInProfPktH.setStatus("current")
_TPortNetEgrQGrpPStOffOutProfPkt_Type = Counter64
_TPortNetEgrQGrpPStOffOutProfPkt_Object = MibTableColumn
tPortNetEgrQGrpPStOffOutProfPkt = _TPortNetEgrQGrpPStOffOutProfPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 12),
    _TPortNetEgrQGrpPStOffOutProfPkt_Type()
)
tPortNetEgrQGrpPStOffOutProfPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffOutProfPkt.setStatus("current")
_TPortNetEgrQGrpPStOffOutProfPktL_Type = Counter32
_TPortNetEgrQGrpPStOffOutProfPktL_Object = MibTableColumn
tPortNetEgrQGrpPStOffOutProfPktL = _TPortNetEgrQGrpPStOffOutProfPktL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 13),
    _TPortNetEgrQGrpPStOffOutProfPktL_Type()
)
tPortNetEgrQGrpPStOffOutProfPktL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffOutProfPktL.setStatus("current")
_TPortNetEgrQGrpPStOffOutProfPktH_Type = Counter32
_TPortNetEgrQGrpPStOffOutProfPktH_Object = MibTableColumn
tPortNetEgrQGrpPStOffOutProfPktH = _TPortNetEgrQGrpPStOffOutProfPktH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 14),
    _TPortNetEgrQGrpPStOffOutProfPktH_Type()
)
tPortNetEgrQGrpPStOffOutProfPktH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffOutProfPktH.setStatus("current")
_TPortNetEgrQGrpPStFwdOutProfPkt_Type = Counter64
_TPortNetEgrQGrpPStFwdOutProfPkt_Object = MibTableColumn
tPortNetEgrQGrpPStFwdOutProfPkt = _TPortNetEgrQGrpPStFwdOutProfPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 15),
    _TPortNetEgrQGrpPStFwdOutProfPkt_Type()
)
tPortNetEgrQGrpPStFwdOutProfPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdOutProfPkt.setStatus("current")
_TPortNetEgrQGrpPStFwdOutProfPktL_Type = Counter32
_TPortNetEgrQGrpPStFwdOutProfPktL_Object = MibTableColumn
tPortNetEgrQGrpPStFwdOutProfPktL = _TPortNetEgrQGrpPStFwdOutProfPktL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 16),
    _TPortNetEgrQGrpPStFwdOutProfPktL_Type()
)
tPortNetEgrQGrpPStFwdOutProfPktL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdOutProfPktL.setStatus("current")
_TPortNetEgrQGrpPStFwdOutProfPktH_Type = Counter32
_TPortNetEgrQGrpPStFwdOutProfPktH_Object = MibTableColumn
tPortNetEgrQGrpPStFwdOutProfPktH = _TPortNetEgrQGrpPStFwdOutProfPktH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 17),
    _TPortNetEgrQGrpPStFwdOutProfPktH_Type()
)
tPortNetEgrQGrpPStFwdOutProfPktH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdOutProfPktH.setStatus("current")
_TPortNetEgrQGrpPStDrpOutProfPkt_Type = Counter64
_TPortNetEgrQGrpPStDrpOutProfPkt_Object = MibTableColumn
tPortNetEgrQGrpPStDrpOutProfPkt = _TPortNetEgrQGrpPStDrpOutProfPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 18),
    _TPortNetEgrQGrpPStDrpOutProfPkt_Type()
)
tPortNetEgrQGrpPStDrpOutProfPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpOutProfPkt.setStatus("current")
_TPortNetEgrQGrpPStDrpOutProfPktL_Type = Counter32
_TPortNetEgrQGrpPStDrpOutProfPktL_Object = MibTableColumn
tPortNetEgrQGrpPStDrpOutProfPktL = _TPortNetEgrQGrpPStDrpOutProfPktL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 19),
    _TPortNetEgrQGrpPStDrpOutProfPktL_Type()
)
tPortNetEgrQGrpPStDrpOutProfPktL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpOutProfPktL.setStatus("current")
_TPortNetEgrQGrpPStDrpOutProfPktH_Type = Counter32
_TPortNetEgrQGrpPStDrpOutProfPktH_Object = MibTableColumn
tPortNetEgrQGrpPStDrpOutProfPktH = _TPortNetEgrQGrpPStDrpOutProfPktH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 20),
    _TPortNetEgrQGrpPStDrpOutProfPktH_Type()
)
tPortNetEgrQGrpPStDrpOutProfPktH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpOutProfPktH.setStatus("current")
_TPortNetEgrQGrpPStOffInProfOct_Type = Counter64
_TPortNetEgrQGrpPStOffInProfOct_Object = MibTableColumn
tPortNetEgrQGrpPStOffInProfOct = _TPortNetEgrQGrpPStOffInProfOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 21),
    _TPortNetEgrQGrpPStOffInProfOct_Type()
)
tPortNetEgrQGrpPStOffInProfOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffInProfOct.setStatus("current")
_TPortNetEgrQGrpPStOffInProfOctL_Type = Counter32
_TPortNetEgrQGrpPStOffInProfOctL_Object = MibTableColumn
tPortNetEgrQGrpPStOffInProfOctL = _TPortNetEgrQGrpPStOffInProfOctL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 22),
    _TPortNetEgrQGrpPStOffInProfOctL_Type()
)
tPortNetEgrQGrpPStOffInProfOctL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffInProfOctL.setStatus("current")
_TPortNetEgrQGrpPStOffInProfOctH_Type = Counter32
_TPortNetEgrQGrpPStOffInProfOctH_Object = MibTableColumn
tPortNetEgrQGrpPStOffInProfOctH = _TPortNetEgrQGrpPStOffInProfOctH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 23),
    _TPortNetEgrQGrpPStOffInProfOctH_Type()
)
tPortNetEgrQGrpPStOffInProfOctH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffInProfOctH.setStatus("current")
_TPortNetEgrQGrpPStFwdInProfOct_Type = Counter64
_TPortNetEgrQGrpPStFwdInProfOct_Object = MibTableColumn
tPortNetEgrQGrpPStFwdInProfOct = _TPortNetEgrQGrpPStFwdInProfOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 24),
    _TPortNetEgrQGrpPStFwdInProfOct_Type()
)
tPortNetEgrQGrpPStFwdInProfOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdInProfOct.setStatus("current")
_TPortNetEgrQGrpPStFwdInProfOctL_Type = Counter32
_TPortNetEgrQGrpPStFwdInProfOctL_Object = MibTableColumn
tPortNetEgrQGrpPStFwdInProfOctL = _TPortNetEgrQGrpPStFwdInProfOctL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 25),
    _TPortNetEgrQGrpPStFwdInProfOctL_Type()
)
tPortNetEgrQGrpPStFwdInProfOctL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdInProfOctL.setStatus("current")
_TPortNetEgrQGrpPStFwdInProfOctH_Type = Counter32
_TPortNetEgrQGrpPStFwdInProfOctH_Object = MibTableColumn
tPortNetEgrQGrpPStFwdInProfOctH = _TPortNetEgrQGrpPStFwdInProfOctH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 26),
    _TPortNetEgrQGrpPStFwdInProfOctH_Type()
)
tPortNetEgrQGrpPStFwdInProfOctH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdInProfOctH.setStatus("current")
_TPortNetEgrQGrpPStDrpInProfOct_Type = Counter64
_TPortNetEgrQGrpPStDrpInProfOct_Object = MibTableColumn
tPortNetEgrQGrpPStDrpInProfOct = _TPortNetEgrQGrpPStDrpInProfOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 27),
    _TPortNetEgrQGrpPStDrpInProfOct_Type()
)
tPortNetEgrQGrpPStDrpInProfOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpInProfOct.setStatus("current")
_TPortNetEgrQGrpPStDrpInProfOctL_Type = Counter32
_TPortNetEgrQGrpPStDrpInProfOctL_Object = MibTableColumn
tPortNetEgrQGrpPStDrpInProfOctL = _TPortNetEgrQGrpPStDrpInProfOctL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 28),
    _TPortNetEgrQGrpPStDrpInProfOctL_Type()
)
tPortNetEgrQGrpPStDrpInProfOctL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpInProfOctL.setStatus("current")
_TPortNetEgrQGrpPStDrpInProfOctH_Type = Counter32
_TPortNetEgrQGrpPStDrpInProfOctH_Object = MibTableColumn
tPortNetEgrQGrpPStDrpInProfOctH = _TPortNetEgrQGrpPStDrpInProfOctH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 29),
    _TPortNetEgrQGrpPStDrpInProfOctH_Type()
)
tPortNetEgrQGrpPStDrpInProfOctH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpInProfOctH.setStatus("current")
_TPortNetEgrQGrpPStOffOutProfOct_Type = Counter64
_TPortNetEgrQGrpPStOffOutProfOct_Object = MibTableColumn
tPortNetEgrQGrpPStOffOutProfOct = _TPortNetEgrQGrpPStOffOutProfOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 30),
    _TPortNetEgrQGrpPStOffOutProfOct_Type()
)
tPortNetEgrQGrpPStOffOutProfOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffOutProfOct.setStatus("current")
_TPortNetEgrQGrpPStOffOutProfOctL_Type = Counter32
_TPortNetEgrQGrpPStOffOutProfOctL_Object = MibTableColumn
tPortNetEgrQGrpPStOffOutProfOctL = _TPortNetEgrQGrpPStOffOutProfOctL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 31),
    _TPortNetEgrQGrpPStOffOutProfOctL_Type()
)
tPortNetEgrQGrpPStOffOutProfOctL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffOutProfOctL.setStatus("current")
_TPortNetEgrQGrpPStOffOutProfOctH_Type = Counter32
_TPortNetEgrQGrpPStOffOutProfOctH_Object = MibTableColumn
tPortNetEgrQGrpPStOffOutProfOctH = _TPortNetEgrQGrpPStOffOutProfOctH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 32),
    _TPortNetEgrQGrpPStOffOutProfOctH_Type()
)
tPortNetEgrQGrpPStOffOutProfOctH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStOffOutProfOctH.setStatus("current")
_TPortNetEgrQGrpPStFwdOutProfOct_Type = Counter64
_TPortNetEgrQGrpPStFwdOutProfOct_Object = MibTableColumn
tPortNetEgrQGrpPStFwdOutProfOct = _TPortNetEgrQGrpPStFwdOutProfOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 33),
    _TPortNetEgrQGrpPStFwdOutProfOct_Type()
)
tPortNetEgrQGrpPStFwdOutProfOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdOutProfOct.setStatus("current")
_TPortNetEgrQGrpPStFwdOutProfOctL_Type = Counter32
_TPortNetEgrQGrpPStFwdOutProfOctL_Object = MibTableColumn
tPortNetEgrQGrpPStFwdOutProfOctL = _TPortNetEgrQGrpPStFwdOutProfOctL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 34),
    _TPortNetEgrQGrpPStFwdOutProfOctL_Type()
)
tPortNetEgrQGrpPStFwdOutProfOctL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdOutProfOctL.setStatus("current")
_TPortNetEgrQGrpPStFwdOutProfOctH_Type = Counter32
_TPortNetEgrQGrpPStFwdOutProfOctH_Object = MibTableColumn
tPortNetEgrQGrpPStFwdOutProfOctH = _TPortNetEgrQGrpPStFwdOutProfOctH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 35),
    _TPortNetEgrQGrpPStFwdOutProfOctH_Type()
)
tPortNetEgrQGrpPStFwdOutProfOctH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStFwdOutProfOctH.setStatus("current")
_TPortNetEgrQGrpPStDrpOutProfOct_Type = Counter64
_TPortNetEgrQGrpPStDrpOutProfOct_Object = MibTableColumn
tPortNetEgrQGrpPStDrpOutProfOct = _TPortNetEgrQGrpPStDrpOutProfOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 36),
    _TPortNetEgrQGrpPStDrpOutProfOct_Type()
)
tPortNetEgrQGrpPStDrpOutProfOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpOutProfOct.setStatus("current")
_TPortNetEgrQGrpPStDrpOutProfOctL_Type = Counter32
_TPortNetEgrQGrpPStDrpOutProfOctL_Object = MibTableColumn
tPortNetEgrQGrpPStDrpOutProfOctL = _TPortNetEgrQGrpPStDrpOutProfOctL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 37),
    _TPortNetEgrQGrpPStDrpOutProfOctL_Type()
)
tPortNetEgrQGrpPStDrpOutProfOctL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpOutProfOctL.setStatus("current")
_TPortNetEgrQGrpPStDrpOutProfOctH_Type = Counter32
_TPortNetEgrQGrpPStDrpOutProfOctH_Object = MibTableColumn
tPortNetEgrQGrpPStDrpOutProfOctH = _TPortNetEgrQGrpPStDrpOutProfOctH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 38),
    _TPortNetEgrQGrpPStDrpOutProfOctH_Type()
)
tPortNetEgrQGrpPStDrpOutProfOctH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStDrpOutProfOctH.setStatus("current")
_TPortNetEgrQGrpPStUncolPktOff_Type = Counter64
_TPortNetEgrQGrpPStUncolPktOff_Object = MibTableColumn
tPortNetEgrQGrpPStUncolPktOff = _TPortNetEgrQGrpPStUncolPktOff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 39),
    _TPortNetEgrQGrpPStUncolPktOff_Type()
)
tPortNetEgrQGrpPStUncolPktOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStUncolPktOff.setStatus("current")
_TPortNetEgrQGrpPStUncolPktOffL_Type = Counter32
_TPortNetEgrQGrpPStUncolPktOffL_Object = MibTableColumn
tPortNetEgrQGrpPStUncolPktOffL = _TPortNetEgrQGrpPStUncolPktOffL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 40),
    _TPortNetEgrQGrpPStUncolPktOffL_Type()
)
tPortNetEgrQGrpPStUncolPktOffL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStUncolPktOffL.setStatus("current")
_TPortNetEgrQGrpPStUncolPktOffH_Type = Counter32
_TPortNetEgrQGrpPStUncolPktOffH_Object = MibTableColumn
tPortNetEgrQGrpPStUncolPktOffH = _TPortNetEgrQGrpPStUncolPktOffH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 41),
    _TPortNetEgrQGrpPStUncolPktOffH_Type()
)
tPortNetEgrQGrpPStUncolPktOffH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStUncolPktOffH.setStatus("current")
_TPortNetEgrQGrpPStUncolOctOff_Type = Counter64
_TPortNetEgrQGrpPStUncolOctOff_Object = MibTableColumn
tPortNetEgrQGrpPStUncolOctOff = _TPortNetEgrQGrpPStUncolOctOff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 42),
    _TPortNetEgrQGrpPStUncolOctOff_Type()
)
tPortNetEgrQGrpPStUncolOctOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStUncolOctOff.setStatus("current")
_TPortNetEgrQGrpPStUncolOctOffL_Type = Counter32
_TPortNetEgrQGrpPStUncolOctOffL_Object = MibTableColumn
tPortNetEgrQGrpPStUncolOctOffL = _TPortNetEgrQGrpPStUncolOctOffL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 43),
    _TPortNetEgrQGrpPStUncolOctOffL_Type()
)
tPortNetEgrQGrpPStUncolOctOffL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStUncolOctOffL.setStatus("current")
_TPortNetEgrQGrpPStUncolOctOffH_Type = Counter32
_TPortNetEgrQGrpPStUncolOctOffH_Object = MibTableColumn
tPortNetEgrQGrpPStUncolOctOffH = _TPortNetEgrQGrpPStUncolOctOffH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 12, 7, 1, 44),
    _TPortNetEgrQGrpPStUncolOctOffH_Type()
)
tPortNetEgrQGrpPStUncolOctOffH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortNetEgrQGrpPStUncolOctOffH.setStatus("current")
_TmnxPortNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPortNotifyPrefix = _TmnxPortNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2)
)
_TmnxPortNotification_ObjectIdentity = ObjectIdentity
tmnxPortNotification = _TmnxPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0)
)
tmnxPortEntry.registerAugmentions(
    ("TIMETRA-PORT-MIB",
     "tmnxPortTestEntry")
)
tmnxPortTestEntry.setIndexNames(*tmnxPortEntry.getIndexNames())
tmnxCiscoHDLCEntry.registerAugmentions(
    ("TIMETRA-PORT-MIB",
     "tmnxCiscoHDLCStatsEntry")
)
tmnxCiscoHDLCStatsEntry.setIndexNames(*tmnxCiscoHDLCEntry.getIndexNames())

# Managed Objects groups

tmnxPortFRGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 5)
)
tmnxPortFRGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxFRDlcmiMode"),
        ("TIMETRA-PORT-MIB", "tmnxFRDlcmiN392Dce"),
        ("TIMETRA-PORT-MIB", "tmnxFRDlcmiN393Dce"),
        ("TIMETRA-PORT-MIB", "tmnxFRDlcmiT392Dce"),
        ("TIMETRA-PORT-MIB", "tmnxFRDlcmiTxStatusEnqMsgs"),
        ("TIMETRA-PORT-MIB", "tmnxFRDlcmiRxStatusEnqMsgs"),
        ("TIMETRA-PORT-MIB", "tmnxFRDlcmiStatusEnqMsgTimeouts"),
        ("TIMETRA-PORT-MIB", "tmnxFRDlcmiTxStatusMsgs"),
        ("TIMETRA-PORT-MIB", "tmnxFRDlcmiRxStatusMsgs"),
        ("TIMETRA-PORT-MIB", "tmnxFRDlcmiStatusMsgTimeouts"),
        ("TIMETRA-PORT-MIB", "tmnxFRDlcmiDiscardedMsgs"),
        ("TIMETRA-PORT-MIB", "tmnxFRDlcmiInvRxSeqNumMsgs"))
)
if mibBuilder.loadTexts:
    tmnxPortFRGroup.setStatus("current")

tmnxQosAppObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 6)
)
tmnxQosAppObjsGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxObjectAppPoolRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxObjectAppResvCbs"),
        ("TIMETRA-PORT-MIB", "tmnxObjectAppSlopePolicy"),
        ("TIMETRA-PORT-MIB", "tmnxObjectAppPoolSize"))
)
if mibBuilder.loadTexts:
    tmnxQosAppObjsGroup.setStatus("current")

tmnxPortTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 7)
)
tmnxPortTestGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortTestState"),
        ("TIMETRA-PORT-MIB", "tmnxPortTestMode"),
        ("TIMETRA-PORT-MIB", "tmnxPortTestParameter"),
        ("TIMETRA-PORT-MIB", "tmnxPortTestLastResult"),
        ("TIMETRA-PORT-MIB", "tmnxPortTestStartTime"),
        ("TIMETRA-PORT-MIB", "tmnxPortTestEndTime"),
        ("TIMETRA-PORT-MIB", "tmnxPortTestDuration"),
        ("TIMETRA-PORT-MIB", "tmnxPortTestAction"))
)
if mibBuilder.loadTexts:
    tmnxPortTestGroup.setStatus("current")

tmnxPortObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 11)
)
tmnxPortObsoleteGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxDS1IdleCycleFlags"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathType"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsIngFwdInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsIngFwdOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsIngFwdInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsIngFwdOutProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsIngDroInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsIngDroOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsIngDroInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsIngDroOutProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrFwdInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrFwdOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrFwdInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrFwdOutProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrDroInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrDroOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrDroInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortFCStatsEgrDroOutProfOcts"))
)
if mibBuilder.loadTexts:
    tmnxPortObsoleteGroup.setStatus("current")

tmnxPortIngrMdaQosStatR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 14)
)
tmnxPortIngrMdaQosStatR2r1Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos00StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos00StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos01StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos01StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos02StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos02StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos03StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos03StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos04StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos04StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos05StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos05StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos06StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos06StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos07StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos07StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos08StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos08StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos09StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos09StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos10StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos10StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos11StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos11StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos12StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos12StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos13StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos13StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos14StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos14StatDropOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos15StatDropPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngrMdaQos15StatDropOcts"))
)
if mibBuilder.loadTexts:
    tmnxPortIngrMdaQosStatR2r1Group.setStatus("current")

tmnxPortStatsR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 16)
)
tmnxPortStatsR2r1Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNetIngressFwdInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetIngressFwdOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetIngressFwdInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetIngressFwdOutProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetIngressDroInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetIngressDroOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetIngressDroInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetIngressDroOutProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgressFwdInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgressFwdOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgressFwdInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgressFwdOutProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgressDroInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgressDroOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgressDroInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgressDroOutProfOcts"))
)
if mibBuilder.loadTexts:
    tmnxPortStatsR2r1Group.setStatus("current")

tmnxPortNotifyObjsGroupR2r1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 18)
)
tmnxPortNotifyObjsGroupR2r1.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifySonetAlarmReason"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifySonetPathAlarmReason"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyError"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyDS3AlarmReason"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyDS1AlarmReason"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyBundleId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyObjsGroupR2r1.setStatus("current")

tmnxPortSonetV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 21)
)
tmnxPortSonetV3v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxSonetSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxSonetClockSource"),
        ("TIMETRA-PORT-MIB", "tmnxSonetFraming"),
        ("TIMETRA-PORT-MIB", "tmnxSonetReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxSonetBerSdThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxSonetBerSfThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxSonetLoopback"),
        ("TIMETRA-PORT-MIB", "tmnxSonetReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxSonetSectionTraceMode"),
        ("TIMETRA-PORT-MIB", "tmnxSonetJ0String"),
        ("TIMETRA-PORT-MIB", "tmnxSonetMonS1Byte"),
        ("TIMETRA-PORT-MIB", "tmnxSonetMonJ0String"),
        ("TIMETRA-PORT-MIB", "tmnxSonetMonK1Byte"),
        ("TIMETRA-PORT-MIB", "tmnxSonetMonK2Byte"),
        ("TIMETRA-PORT-MIB", "tmnxSonetSingleFiber"),
        ("TIMETRA-PORT-MIB", "tmnxSonetHoldTimeUp"),
        ("TIMETRA-PORT-MIB", "tmnxSonetHoldTimeDown"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathMTU"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathScramble"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathC2Byte"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathJ1String"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathCRC"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathOperMRU"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathCollectStats"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathMonC2Byte"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathMonJ1String"),
        ("TIMETRA-PORT-MIB", "tmnxSonetPathChildType"),
        ("TIMETRA-PORT-MIB", "tmnxSonetGroupType"),
        ("TIMETRA-PORT-MIB", "tmnxSonetGroupParentPortID"),
        ("TIMETRA-PORT-MIB", "tmnxSonetGroupChildType"),
        ("TIMETRA-PORT-MIB", "tmnxSonetGroupName"))
)
if mibBuilder.loadTexts:
    tmnxPortSonetV3v0Group.setStatus("current")

tmnxPortTDMV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 22)
)
tmnxPortTDMV3v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxDS3Buildout"),
        ("TIMETRA-PORT-MIB", "tmnxDS3Type"),
        ("TIMETRA-PORT-MIB", "tmnxDS3LastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelType"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelFraming"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelClockSource"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelChannelized"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrateCSUMode"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrate"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelIdleCycleFlags"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBitErrorInsertionRate"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTPattern"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTDuration"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLEicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLLicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLFicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLUnitString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPfiString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPortString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLGenString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMessageType"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelFEACLoopRespond"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelCRC"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelInFEACLoop"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonPortString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonGenString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTSynched"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTErrors"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTTotalBits"),
        ("TIMETRA-PORT-MIB", "tmnxDS1RowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Type"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Framing"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Loopback"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InvertData"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BitErrorInsertionRate"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTPattern"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTDuration"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1LastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ClockSource"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTSynched"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTErrors"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTTotalBits"),
        ("TIMETRA-PORT-MIB", "tmnxDS1RemoteLoopRespond"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InRemoteLoop"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupTimeSlots"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCRC"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupIdleCycleFlags"))
)
if mibBuilder.loadTexts:
    tmnxPortTDMV3v0Group.setStatus("obsolete")

tmnxPortATMV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 23)
)
tmnxPortATMV3v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxATMIntfCellFormat"),
        ("TIMETRA-PORT-MIB", "tmnxATMIntfMinVpValue"))
)
if mibBuilder.loadTexts:
    tmnxPortATMV3v0Group.setStatus("obsolete")

tmnxScalarPortV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 24)
)
tmnxScalarPortV3v0Group.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxL4LoadBalancing")
)
if mibBuilder.loadTexts:
    tmnxScalarPortV3v0Group.setStatus("current")

tmnxPortV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 25)
)
tmnxPortV3v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortTableLastChange"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxPortType"),
        ("TIMETRA-PORT-MIB", "tmnxPortClass"),
        ("TIMETRA-PORT-MIB", "tmnxPortDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortName"),
        ("TIMETRA-PORT-MIB", "tmnxPortAlias"),
        ("TIMETRA-PORT-MIB", "tmnxPortUserAssignedMac"),
        ("TIMETRA-PORT-MIB", "tmnxPortMacAddress"),
        ("TIMETRA-PORT-MIB", "tmnxPortHwMacAddress"),
        ("TIMETRA-PORT-MIB", "tmnxPortMode"),
        ("TIMETRA-PORT-MIB", "tmnxPortEncapType"),
        ("TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("TIMETRA-PORT-MIB", "tmnxPortHoldTimeUp"),
        ("TIMETRA-PORT-MIB", "tmnxPortHoldTimeDown"),
        ("TIMETRA-PORT-MIB", "tmnxPortUpProtocols"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectorType"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverType"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverCode"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverLaserWaveLen"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverDiagCapable"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverModelNumber"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPConnectorCode"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorOUI"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorManufactureDate"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPMedia"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPEquipped"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorSerialNum"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorPartNum"),
        ("TIMETRA-PORT-MIB", "tmnxPortEquipped"),
        ("TIMETRA-PORT-MIB", "tmnxPortLinkStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortAdminStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortState"),
        ("TIMETRA-PORT-MIB", "tmnxPortPrevState"),
        ("TIMETRA-PORT-MIB", "tmnxPortNumAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxPortAlarmState"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastAlarmEvent"),
        ("TIMETRA-PORT-MIB", "tmnxPortClearAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastStateChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPortNumChannels"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetworkEgrQueues"),
        ("TIMETRA-PORT-MIB", "tmnxPortIsLeaf"),
        ("TIMETRA-PORT-MIB", "tmnxPortChanType"),
        ("TIMETRA-PORT-MIB", "tmnxPortParentPortID"),
        ("TIMETRA-PORT-MIB", "tmnxPortLoadBalanceAlgorithm"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeName"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeName"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeStatus"),
        ("TIMETRA-PORT-MIB", "tmnxChannelPortID"),
        ("TIMETRA-PORT-MIB", "tmnxPortOpticalCompliance"),
        ("TIMETRA-PORT-MIB", "tmnxL4LoadBalancing"))
)
if mibBuilder.loadTexts:
    tmnxPortV3v0Group.setStatus("obsolete")

tmnxCiscoHDLCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 26)
)
tmnxCiscoHDLCGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxCiscoHDLCKeepAliveInt"),
        ("TIMETRA-PORT-MIB", "tmnxCiscoHDLCUpCount"),
        ("TIMETRA-PORT-MIB", "tmnxCiscoHDLCDownCount"),
        ("TIMETRA-PORT-MIB", "tmnxCiscoHDLCOperState"),
        ("TIMETRA-PORT-MIB", "tmnxCiscoHDLCDiscardStatInPkts"),
        ("TIMETRA-PORT-MIB", "tmnxCiscoHDLCDiscardStatOutPkts"),
        ("TIMETRA-PORT-MIB", "tmnxCiscoHDLCStatInPkts"),
        ("TIMETRA-PORT-MIB", "tmnxCiscoHDLCStatOutPkts"),
        ("TIMETRA-PORT-MIB", "tmnxCiscoHDLCStatInOctets"),
        ("TIMETRA-PORT-MIB", "tmnxCiscoHDLCStatOutOctets"))
)
if mibBuilder.loadTexts:
    tmnxCiscoHDLCGroup.setStatus("current")

tmnxMlBundleV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 27)
)
tmnxMlBundleV3v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxBundleRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxBundleType"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMinimumLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleNumLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleNumActiveLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleOperMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundlePeerMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelay"),
        ("TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelayAction"),
        ("TIMETRA-PORT-MIB", "tmnxBundleYellowDiffDelay"),
        ("TIMETRA-PORT-MIB", "tmnxBundleShortSequence"),
        ("TIMETRA-PORT-MIB", "tmnxBundleLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleFragmentThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxBundleUpTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberActive"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberDownReason"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberUpTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleInputDiscards"),
        ("TIMETRA-PORT-MIB", "tmnxBundlePrimaryMemberPortID"),
        ("TIMETRA-PORT-MIB", "tmnxBundleLFI"),
        ("TIMETRA-PORT-MIB", "tmnxPortBundleNumber"))
)
if mibBuilder.loadTexts:
    tmnxMlBundleV3v0Group.setStatus("obsolete")

tmnxObsoleteGroupV3v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 28)
)
tmnxObsoleteGroupV3v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxSonetAps"),
        ("TIMETRA-PORT-MIB", "tmnxSonetApsAdminStatus"),
        ("TIMETRA-PORT-MIB", "tmnxSonetApsOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxSonetApsAuthKey"),
        ("TIMETRA-PORT-MIB", "tmnxSonetApsNeighborAddr"),
        ("TIMETRA-PORT-MIB", "tmnxSonetApsAdvertiseInterval"),
        ("TIMETRA-PORT-MIB", "tmnxSonetApsAdvertiseTimeLeft"),
        ("TIMETRA-PORT-MIB", "tmnxSonetApsHoldTime"),
        ("TIMETRA-PORT-MIB", "tmnxSonetApsHoldTimeLeft"))
)
if mibBuilder.loadTexts:
    tmnxObsoleteGroupV3v0.setStatus("current")

tmnxPortEthernetV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 29)
)
tmnxPortEthernetV3v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEtherMTU"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDuplex"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherAutoNegotiate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherOperDuplex"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherOperSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherCollectStats"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherMDIMDIX"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherXGigMode"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherEgressRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDot1qEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherQinqEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherIngressRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherHCOverPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherHCPkts1519toMax"))
)
if mibBuilder.loadTexts:
    tmnxPortEthernetV3v0Group.setStatus("obsolete")

tmnxPortTDMGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 30)
)
tmnxPortTDMGroupV4v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxDS3Buildout"),
        ("TIMETRA-PORT-MIB", "tmnxDS3Type"),
        ("TIMETRA-PORT-MIB", "tmnxDS3LastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelType"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelFraming"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelClockSource"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelChannelized"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrateCSUMode"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrate"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelIdleCycleFlags"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBitErrorInsertionRate"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTPattern"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTDuration"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLEicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLLicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLFicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLUnitString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPfiString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPortString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLGenString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMessageType"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelFEACLoopRespond"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelCRC"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelInFEACLoop"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonPortString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonGenString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTSynched"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTErrors"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTTotalBits"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelScramble"),
        ("TIMETRA-PORT-MIB", "tmnxDS1RowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Type"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Framing"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Loopback"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InvertData"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BitErrorInsertionRate"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTPattern"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTDuration"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1LastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ClockSource"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTSynched"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTErrors"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTTotalBits"),
        ("TIMETRA-PORT-MIB", "tmnxDS1RemoteLoopRespond"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InRemoteLoop"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupTimeSlots"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCRC"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupIdleCycleFlags"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupScramble"))
)
if mibBuilder.loadTexts:
    tmnxPortTDMGroupV4v0.setStatus("obsolete")

tmnxPortATMGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 31)
)
tmnxPortATMGroupV4v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxATMIntfCellFormat"),
        ("TIMETRA-PORT-MIB", "tmnxATMIntfMinVpValue"),
        ("TIMETRA-PORT-MIB", "tmnxATMIntfMapping"))
)
if mibBuilder.loadTexts:
    tmnxPortATMGroupV4v0.setStatus("obsolete")

tmnxMlBundleGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 32)
)
tmnxMlBundleGroupV4v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxBundleRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxBundleType"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMinimumLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleNumLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleNumActiveLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleOperMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundlePeerMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelay"),
        ("TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelayAction"),
        ("TIMETRA-PORT-MIB", "tmnxBundleYellowDiffDelay"),
        ("TIMETRA-PORT-MIB", "tmnxBundleShortSequence"),
        ("TIMETRA-PORT-MIB", "tmnxBundleLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleFragmentThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxBundleUpTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberActive"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberDownReason"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberUpTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleInputDiscards"),
        ("TIMETRA-PORT-MIB", "tmnxBundlePrimaryMemberPortID"),
        ("TIMETRA-PORT-MIB", "tmnxBundleLFI"),
        ("TIMETRA-PORT-MIB", "tmnxPortBundleNumber"))
)
if mibBuilder.loadTexts:
    tmnxMlBundleGroupV4v0.setStatus("obsolete")

tmnxMlImaBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 33)
)
tmnxMlImaBundleGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxBundleImaGrpLnkActTimer"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpLnkDeactTimer"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpSymmetryMode"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpTxId"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpRxId"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpTxRefLnk"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpRxRefLnk"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpSmNeState"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpSmFeState"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpSmFailState"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpSmDownSecs"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpSmOperSecs"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpAvailTxCR"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpAvailRxCR"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpNeFails"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpFeFails"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpTxIcpCells"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpRxIcpCells"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpErrorIcpCells"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpLostRxIcpCells"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpTxOamLablVal"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpRxOamLablVal"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpAlphaValue"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpBetaValue"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpGammaValue"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpNeClockMode"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpFeClockMode"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpVersion"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpMaxConfBw"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpTestState"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpTestMember"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpTestPattern"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpDiffDelayMaxObs"),
        ("TIMETRA-PORT-MIB", "tmnxBundleImaGrpLeastDelayLink"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeTxState"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeRxState"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeTxState"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeRxState"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeRxFailState"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeRxFailState"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaTxLid"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaRxLid"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaViolations"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeSevErrSecs"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeSevErrSecs"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeUnavailSecs"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeUnavailSecs"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeTxUnuseSecs"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeRxUnuseSecs"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeTxUnuseSecs"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeRxUnuseSecs"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeTxNumFails"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaNeRxNumFails"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeTxNumFails"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaFeRxNumFails"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaTxIcpCells"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaRxIcpCells"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaErrorIcpCells"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaLstRxIcpCells"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaOifAnomalies"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaRxTestState"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaRxTestPattern"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberImaRelDelay"))
)
if mibBuilder.loadTexts:
    tmnxMlImaBundleGroup.setStatus("current")

tmnx7710PortTDMGroupV3v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 34)
)
tmnx7710PortTDMGroupV3v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxDS3ChannelAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelCollectStats"),
        ("TIMETRA-PORT-MIB", "tmnxDS1PortBuildout"),
        ("TIMETRA-PORT-MIB", "tmnxDS1PortLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS1PortType"),
        ("TIMETRA-PORT-MIB", "tmnxDS1PortLineLength"),
        ("TIMETRA-PORT-MIB", "tmnxDS1PortLbo"),
        ("TIMETRA-PORT-MIB", "tmnxDS1PortDbGain"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InsertSingleBitError"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCollectStats"))
)
if mibBuilder.loadTexts:
    tmnx7710PortTDMGroupV3v0.setStatus("obsolete")

tmnxPortGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 35)
)
tmnxPortGroupV4v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortTableLastChange"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxPortType"),
        ("TIMETRA-PORT-MIB", "tmnxPortClass"),
        ("TIMETRA-PORT-MIB", "tmnxPortDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortName"),
        ("TIMETRA-PORT-MIB", "tmnxPortAlias"),
        ("TIMETRA-PORT-MIB", "tmnxPortUserAssignedMac"),
        ("TIMETRA-PORT-MIB", "tmnxPortMacAddress"),
        ("TIMETRA-PORT-MIB", "tmnxPortHwMacAddress"),
        ("TIMETRA-PORT-MIB", "tmnxPortMode"),
        ("TIMETRA-PORT-MIB", "tmnxPortEncapType"),
        ("TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("TIMETRA-PORT-MIB", "tmnxPortHoldTimeUp"),
        ("TIMETRA-PORT-MIB", "tmnxPortHoldTimeDown"),
        ("TIMETRA-PORT-MIB", "tmnxPortUpProtocols"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectorType"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverType"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverCode"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverLaserWaveLen"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverDiagCapable"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverModelNumber"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPConnectorCode"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorOUI"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorManufactureDate"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPMedia"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPEquipped"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorSerialNum"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorPartNum"),
        ("TIMETRA-PORT-MIB", "tmnxPortEquipped"),
        ("TIMETRA-PORT-MIB", "tmnxPortLinkStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortAdminStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortState"),
        ("TIMETRA-PORT-MIB", "tmnxPortPrevState"),
        ("TIMETRA-PORT-MIB", "tmnxPortNumAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxPortAlarmState"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastAlarmEvent"),
        ("TIMETRA-PORT-MIB", "tmnxPortClearAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastStateChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPortNumChannels"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetworkEgrQueues"),
        ("TIMETRA-PORT-MIB", "tmnxPortIsLeaf"),
        ("TIMETRA-PORT-MIB", "tmnxPortChanType"),
        ("TIMETRA-PORT-MIB", "tmnxPortParentPortID"),
        ("TIMETRA-PORT-MIB", "tmnxPortLoadBalanceAlgorithm"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeName"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeName"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeStatus"),
        ("TIMETRA-PORT-MIB", "tmnxChannelPortID"),
        ("TIMETRA-PORT-MIB", "tmnxPortOpticalCompliance"),
        ("TIMETRA-PORT-MIB", "tmnxL4LoadBalancing"))
)
if mibBuilder.loadTexts:
    tmnxPortGroupV4v0.setStatus("obsolete")

tmnxObsoleteGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 36)
)
tmnxObsoleteGroupV5v0.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortTransceiverCode")
)
if mibBuilder.loadTexts:
    tmnxObsoleteGroupV5v0.setStatus("current")

tmnxPortSchedV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 37)
)
tmnxPortSchedV5v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEgrPortSchedPlcy"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideSchedName"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLastChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideMaxRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl1PIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl1CIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl2PIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl2CIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl3PIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl3CIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl4PIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl4CIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl5PIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl5CIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl6PIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl6CIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl7PIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl7CIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl8PIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideLvl8CIR"),
        ("TIMETRA-PORT-MIB", "tmnxPortSchedOverrideFlags"))
)
if mibBuilder.loadTexts:
    tmnxPortSchedV5v0Group.setStatus("current")

tmnxPortEthernetV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 38)
)
tmnxPortEthernetV5v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEtherMTU"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDuplex"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherAutoNegotiate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherOperDuplex"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherOperSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherCollectStats"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherMDIMDIX"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherXGigMode"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherEgressRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDot1qEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherQinqEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherIngressRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherHCOverPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherHCPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherLacpTunnel"))
)
if mibBuilder.loadTexts:
    tmnxPortEthernetV5v0Group.setStatus("obsolete")

tmnxPortGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 39)
)
tmnxPortGroupV5v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortTableLastChange"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxPortType"),
        ("TIMETRA-PORT-MIB", "tmnxPortClass"),
        ("TIMETRA-PORT-MIB", "tmnxPortDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortName"),
        ("TIMETRA-PORT-MIB", "tmnxPortAlias"),
        ("TIMETRA-PORT-MIB", "tmnxPortUserAssignedMac"),
        ("TIMETRA-PORT-MIB", "tmnxPortMacAddress"),
        ("TIMETRA-PORT-MIB", "tmnxPortHwMacAddress"),
        ("TIMETRA-PORT-MIB", "tmnxPortMode"),
        ("TIMETRA-PORT-MIB", "tmnxPortEncapType"),
        ("TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("TIMETRA-PORT-MIB", "tmnxPortHoldTimeUp"),
        ("TIMETRA-PORT-MIB", "tmnxPortHoldTimeDown"),
        ("TIMETRA-PORT-MIB", "tmnxPortUpProtocols"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectorType"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverType"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverCode"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverLaserWaveLen"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverDiagCapable"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverModelNumber"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPConnectorCode"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorOUI"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorManufactureDate"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPMedia"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPEquipped"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorSerialNum"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorPartNum"),
        ("TIMETRA-PORT-MIB", "tmnxPortEquipped"),
        ("TIMETRA-PORT-MIB", "tmnxPortLinkStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortAdminStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortState"),
        ("TIMETRA-PORT-MIB", "tmnxPortPrevState"),
        ("TIMETRA-PORT-MIB", "tmnxPortNumAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxPortAlarmState"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastAlarmEvent"),
        ("TIMETRA-PORT-MIB", "tmnxPortClearAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastStateChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPortNumChannels"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetworkEgrQueues"),
        ("TIMETRA-PORT-MIB", "tmnxPortIsLeaf"),
        ("TIMETRA-PORT-MIB", "tmnxPortChanType"),
        ("TIMETRA-PORT-MIB", "tmnxPortParentPortID"),
        ("TIMETRA-PORT-MIB", "tmnxPortLoadBalanceAlgorithm"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeName"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeName"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeStatus"),
        ("TIMETRA-PORT-MIB", "tmnxChannelPortID"),
        ("TIMETRA-PORT-MIB", "tmnxPortOpticalCompliance"),
        ("TIMETRA-PORT-MIB", "tmnxL4LoadBalancing"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastClearedTime"))
)
if mibBuilder.loadTexts:
    tmnxPortGroupV5v0.setStatus("obsolete")

tmnxMlBundleGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 40)
)
tmnxMlBundleGroupV5v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxBundleRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxBundleType"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMinimumLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleNumLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleNumActiveLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleOperMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundlePeerMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelay"),
        ("TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelayAction"),
        ("TIMETRA-PORT-MIB", "tmnxBundleYellowDiffDelay"),
        ("TIMETRA-PORT-MIB", "tmnxBundleShortSequence"),
        ("TIMETRA-PORT-MIB", "tmnxBundleLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleFragmentThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxBundleUpTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberActive"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberDownReason"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberUpTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleInputDiscards"),
        ("TIMETRA-PORT-MIB", "tmnxBundlePrimaryMemberPortID"),
        ("TIMETRA-PORT-MIB", "tmnxBundleLFI"),
        ("TIMETRA-PORT-MIB", "tmnxPortBundleNumber"),
        ("TIMETRA-PORT-MIB", "tmnxBundleProtectedType"),
        ("TIMETRA-PORT-MIB", "tmnxBundleParentBundle"),
        ("TIMETRA-PORT-MIB", "tmnxBPGrpAssocWorkingBundleID"),
        ("TIMETRA-PORT-MIB", "tmnxBPGrpAssocProtectBundleID"),
        ("TIMETRA-PORT-MIB", "tmnxBPGrpAssocActiveBundleID"))
)
if mibBuilder.loadTexts:
    tmnxMlBundleGroupV5v0.setStatus("obsolete")

tmnxPortTDMGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 42)
)
tmnxPortTDMGroupV5v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxDS3ChannelAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelCollectStats"),
        ("TIMETRA-PORT-MIB", "tmnxDS3Buildout"),
        ("TIMETRA-PORT-MIB", "tmnxDS3Type"),
        ("TIMETRA-PORT-MIB", "tmnxDS3LastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelType"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelFraming"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelClockSource"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelChannelized"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrateCSUMode"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrate"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelIdleCycleFlags"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBitErrorInsertionRate"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTPattern"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTDuration"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLEicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLLicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLFicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLUnitString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPfiString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPortString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLGenString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMessageType"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelFEACLoopRespond"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelCRC"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelInFEACLoop"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonPortString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonGenString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTSynched"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTErrors"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTTotalBits"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelScramble"),
        ("TIMETRA-PORT-MIB", "tmnxDS1RowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Type"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Framing"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Loopback"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InvertData"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BitErrorInsertionRate"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTPattern"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTDuration"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1LastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ClockSource"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTSynched"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTErrors"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTTotalBits"),
        ("TIMETRA-PORT-MIB", "tmnxDS1RemoteLoopRespond"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InRemoteLoop"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupTimeSlots"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCRC"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupIdleCycleFlags"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupScramble"))
)
if mibBuilder.loadTexts:
    tmnxPortTDMGroupV5v0.setStatus("obsolete")

tmnx7710PortTDMGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 43)
)
tmnx7710PortTDMGroupV5v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxDS1PortBuildout"),
        ("TIMETRA-PORT-MIB", "tmnxDS1PortLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS1PortType"),
        ("TIMETRA-PORT-MIB", "tmnxDS1PortLineLength"),
        ("TIMETRA-PORT-MIB", "tmnxDS1PortLbo"),
        ("TIMETRA-PORT-MIB", "tmnxDS1PortDbGain"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InsertSingleBitError"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCollectStats"))
)
if mibBuilder.loadTexts:
    tmnx7710PortTDMGroupV5v0.setStatus("current")

tmnxPortCemGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 44)
)
tmnxPortCemGroupV6v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxDS3ChannelClockSyncState"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelClockMasterPortId"),
        ("TIMETRA-PORT-MIB", "tmnxDS1SignalMode"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ClockSyncState"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ClockMasterPortId"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupPayloadFillType"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupPayloadPattern"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSignalFillType"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSignalPattern"))
)
if mibBuilder.loadTexts:
    tmnxPortCemGroupV6v0.setStatus("current")

tmnxMcMlpppBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 45)
)
tmnxMcMlpppBundleGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxBundleMlpppClassCount"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMlpppIngQoSProfId"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMlpppEgrQoSProfId"),
        ("TIMETRA-PORT-MIB", "tmnxMcMlpppStatsIngressOct"),
        ("TIMETRA-PORT-MIB", "tmnxMcMlpppStatsIngressPkt"),
        ("TIMETRA-PORT-MIB", "tmnxMcMlpppStatsIngressErrPkt"),
        ("TIMETRA-PORT-MIB", "tmnxMcMlpppStatsEgressOct"),
        ("TIMETRA-PORT-MIB", "tmnxMcMlpppStatsEgressPkt"),
        ("TIMETRA-PORT-MIB", "tmnxMcMlpppStatsEgressErrPkt"))
)
if mibBuilder.loadTexts:
    tmnxMcMlpppBundleGroup.setStatus("current")

tmnxPortEthernetV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 47)
)
tmnxPortEthernetV6v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEtherMTU"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDuplex"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherAutoNegotiate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherOperDuplex"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherOperSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherCollectStats"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherMDIMDIX"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherXGigMode"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherEgressRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDot1qEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherQinqEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherIngressRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherHCOverPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherHCPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherLacpTunnel"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedEnabled"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedKeepAlive"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedRetry"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedState"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherPBBEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReasonDownFlags"))
)
if mibBuilder.loadTexts:
    tmnxPortEthernetV6v0Group.setStatus("obsolete")

tmnxMlBundleGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 48)
)
tmnxMlBundleGroupV6v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxBundleRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxBundleType"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMinimumLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleNumLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleNumActiveLinks"),
        ("TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelay"),
        ("TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelayAction"),
        ("TIMETRA-PORT-MIB", "tmnxBundleLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleFragmentThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxBundleUpTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberActive"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberDownReason"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberUpTime"),
        ("TIMETRA-PORT-MIB", "tmnxBundleInputDiscards"),
        ("TIMETRA-PORT-MIB", "tmnxBundlePrimaryMemberPortID"),
        ("TIMETRA-PORT-MIB", "tmnxPortBundleNumber"),
        ("TIMETRA-PORT-MIB", "tmnxBundleProtectedType"),
        ("TIMETRA-PORT-MIB", "tmnxBundleParentBundle"),
        ("TIMETRA-PORT-MIB", "tmnxBPGrpAssocWorkingBundleID"),
        ("TIMETRA-PORT-MIB", "tmnxBPGrpAssocProtectBundleID"),
        ("TIMETRA-PORT-MIB", "tmnxBPGrpAssocActiveBundleID"))
)
if mibBuilder.loadTexts:
    tmnxMlBundleGroupV6v0.setStatus("current")

tmnxMlpppBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 49)
)
tmnxMlpppBundleGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxBundleMlpppEndpointID"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMlpppEndpointIDClass"),
        ("TIMETRA-PORT-MIB", "tmnxBundleYellowDiffDelay"),
        ("TIMETRA-PORT-MIB", "tmnxBundleShortSequence"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleOperMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundlePeerMRRU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxBundleLFI"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMlpppMagicNumber"))
)
if mibBuilder.loadTexts:
    tmnxMlpppBundleGroup.setStatus("current")

tmnxHsmdaGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 51)
)
tmnxHsmdaGroupV6v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEgrHsmdaSchedPlcy"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrTblLastChngd"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrLastChanged"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrMaxRate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrGrp1Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrGrp2Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass1Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass1WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass2Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass2WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass3Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass3WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass4Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass4WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass5Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass5WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass6Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass6WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass7Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass7WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass8Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass8WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrShaperTblLastChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrShaperRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrShaperLastChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrShaperRate"))
)
if mibBuilder.loadTexts:
    tmnxHsmdaGroupV6v0.setStatus("obsolete")

tmnxPortTDMGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 52)
)
tmnxPortTDMGroupV6v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxDS3ChannelAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelCollectStats"),
        ("TIMETRA-PORT-MIB", "tmnxDS3Buildout"),
        ("TIMETRA-PORT-MIB", "tmnxDS3Type"),
        ("TIMETRA-PORT-MIB", "tmnxDS3LastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelType"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelFraming"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelClockSource"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelChannelized"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrateCSUMode"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrate"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelIdleCycleFlags"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBitErrorInsertionRate"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTPattern"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTDuration"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLEicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLLicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLFicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLUnitString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPfiString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPortString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLGenString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMessageType"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelFEACLoopRespond"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelCRC"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelInFEACLoop"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonPortString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonGenString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTSynched"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTErrors"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTTotalBits"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelScramble"),
        ("TIMETRA-PORT-MIB", "tmnxDS1RowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Type"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Framing"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Loopback"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InvertData"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BitErrorInsertionRate"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTPattern"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTDuration"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1LastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ClockSource"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTSynched"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTErrors"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTTotalBits"),
        ("TIMETRA-PORT-MIB", "tmnxDS1RemoteLoopRespond"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InRemoteLoop"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BerSdThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BerSfThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupTimeSlots"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCRC"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupIdleCycleFlags"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupScramble"))
)
if mibBuilder.loadTexts:
    tmnxPortTDMGroupV6v0.setStatus("obsolete")

tmnxDigitalDiagMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 53)
)
tmnxDigitalDiagMonitorGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxDDMTemperature"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTempLowWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTempLowAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTempHiWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTempHiAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMSupplyVoltage"),
        ("TIMETRA-PORT-MIB", "tmnxDDMSupplyVoltageLowWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMSupplyVoltageLowAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMSupplyVoltageHiWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMSupplyVoltageHiAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTxBiasCurrent"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTxBiasCurrentLowWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTxBiasCurrentLowAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTxBiasCurrentHiWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTxBiasCurrentHiAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTxOutputPower"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTxOutputPowerLowWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTxOutputPowerLowAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTxOutputPowerHiWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMTxOutputPowerHiAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPower"),
        ("TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPowerLowWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPowerLowAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPowerHiWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPowerHiAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMRxOpticalPowerType"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux1"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux1LowWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux1LowAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux1HiWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux1HiAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux1Type"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux2"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux2LowWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux2LowAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux2HiWarning"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux2HiAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMAux2Type"),
        ("TIMETRA-PORT-MIB", "tmnxDDMFailedThresholds"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExternallyCalibrated"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalRxPower4"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalRxPower3"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalRxPower2"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalRxPower1"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalRxPower0"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalTxLaserBiasSlope"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalTxLaserBiasOffset"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalTxPowerSlope"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalTxPowerOffset"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalTemperatureSlope"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalTemperatureOffset"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalVoltageSlope"),
        ("TIMETRA-PORT-MIB", "tmnxDDMExtCalVoltageOffset"))
)
if mibBuilder.loadTexts:
    tmnxDigitalDiagMonitorGroup.setStatus("current")

tmnxPortGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 54)
)
tmnxPortGroupV6v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortTableLastChange"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxPortType"),
        ("TIMETRA-PORT-MIB", "tmnxPortClass"),
        ("TIMETRA-PORT-MIB", "tmnxPortDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortName"),
        ("TIMETRA-PORT-MIB", "tmnxPortAlias"),
        ("TIMETRA-PORT-MIB", "tmnxPortUserAssignedMac"),
        ("TIMETRA-PORT-MIB", "tmnxPortMacAddress"),
        ("TIMETRA-PORT-MIB", "tmnxPortHwMacAddress"),
        ("TIMETRA-PORT-MIB", "tmnxPortMode"),
        ("TIMETRA-PORT-MIB", "tmnxPortEncapType"),
        ("TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("TIMETRA-PORT-MIB", "tmnxPortHoldTimeUp"),
        ("TIMETRA-PORT-MIB", "tmnxPortHoldTimeDown"),
        ("TIMETRA-PORT-MIB", "tmnxPortUpProtocols"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectorType"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverType"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverLaserWaveLen"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverDiagCapable"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverModelNumber"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPConnectorCode"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorOUI"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorManufactureDate"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPMedia"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPEquipped"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorSerialNum"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorPartNum"),
        ("TIMETRA-PORT-MIB", "tmnxPortEquipped"),
        ("TIMETRA-PORT-MIB", "tmnxPortLinkStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortAdminStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortState"),
        ("TIMETRA-PORT-MIB", "tmnxPortPrevState"),
        ("TIMETRA-PORT-MIB", "tmnxPortNumAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxPortAlarmState"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastAlarmEvent"),
        ("TIMETRA-PORT-MIB", "tmnxPortClearAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastStateChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPortNumChannels"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetworkEgrQueues"),
        ("TIMETRA-PORT-MIB", "tmnxPortIsLeaf"),
        ("TIMETRA-PORT-MIB", "tmnxPortChanType"),
        ("TIMETRA-PORT-MIB", "tmnxPortParentPortID"),
        ("TIMETRA-PORT-MIB", "tmnxPortLoadBalanceAlgorithm"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeName"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeName"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeStatus"),
        ("TIMETRA-PORT-MIB", "tmnxChannelPortID"),
        ("TIMETRA-PORT-MIB", "tmnxPortOpticalCompliance"),
        ("TIMETRA-PORT-MIB", "tmnxL4LoadBalancing"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastClearedTime"),
        ("TIMETRA-PORT-MIB", "tmnxPortDDMEventSuppression"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortReasonDownFlags"))
)
if mibBuilder.loadTexts:
    tmnxPortGroupV6v0.setStatus("obsolete")

tmnxNamedPoolGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 55)
)
tmnxNamedPoolGroupV6v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortIngNamedPoolPlcy"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrNamedPoolPlcy"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngPoolPercentRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrPoolPercentRate"))
)
if mibBuilder.loadTexts:
    tmnxNamedPoolGroupV6v0.setStatus("current")

tmnxPortEthernetV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 56)
)
tmnxPortEthernetV6v1Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEtherMTU"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDuplex"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherAutoNegotiate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherOperDuplex"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherOperSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherCollectStats"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherMDIMDIX"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherXGigMode"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherEgressRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDot1qEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherQinqEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherIngressRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherHCOverPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherHCPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherLacpTunnel"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedEnabled"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedKeepAlive"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedRetry"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedState"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherPBBEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReasonDownFlags"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSingleFiber"))
)
if mibBuilder.loadTexts:
    tmnxPortEthernetV6v1Group.setStatus("obsolete")

tmnxPortNotifyObjsGroupV6v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 57)
)
tmnxPortNotifyObjsGroupV6v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxDDMFailedObject"),
        ("TIMETRA-PORT-MIB", "tmnxDSXClockSyncStateObject"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyObjsGroupV6v0.setStatus("current")

tmnxPortQV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 58)
)
tmnxPortQV7v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tPortAccEgrQGrpAggRateLimit"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpSchedPol"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpAcctgPolId"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpCollectStats"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpFrameBaseActg"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverLastChanged"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverAdminCIR"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverAdminPIR"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverCBS"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverHiPrioOnly"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverMBS"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpSchedPol"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpAcctgPolId"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpCollectStats"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverLastChanged"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverAdminCIR"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverAdminPIR"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverCBS"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverHiPrioOnly"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverMBS"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpAcctgPolId"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpAggRateLimit"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpCollectStats"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpFrameBaseActg"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpSchedPol"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverAdminCIR"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverAdminPIR"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverCBS"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverHiPrioOnly"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverLastChanged"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverMBS"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverCIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverPIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverCIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverPIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverCIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverPIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpDescr"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpDescr"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpDescr"))
)
if mibBuilder.loadTexts:
    tmnxPortQV7v0Group.setStatus("obsolete")

tmnxMcMfrBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 59)
)
tmnxMcMfrBundleGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxBundleMlfrBundleId"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMlfrIngQoSProfId"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMlfrEgrQoSProfId"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMlfrHelloTimer"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMlfrHelloRetryCount"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMlfrAckTimer"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMlfrLastChanged"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberMlfrDownReason"))
)
if mibBuilder.loadTexts:
    tmnxMcMfrBundleGroup.setStatus("current")

tmnxFrIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 60)
)
tmnxFrIntfGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxFrIntfFrf12Mode"),
        ("TIMETRA-PORT-MIB", "tmnxFrIntfLinkId"),
        ("TIMETRA-PORT-MIB", "tmnxFrIntfLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxFrIntfGroup.setStatus("current")

tmnxFrf12IntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 61)
)
tmnxFrf12IntfGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxFrf12IntfFragmentThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxFrf12IntfEgrQoSProfId"),
        ("TIMETRA-PORT-MIB", "tmnxFrf12IntfLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxFrf12IntfGroup.setStatus("current")

tmnxPortQStatV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 62)
)
tmnxPortQStatV7v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEgrQosQStatDpdInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrQosQStatDpdInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrQosQStatDpdOutProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrQosQStatDpdOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrQosQStatFwdInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrQosQStatFwdInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrQosQStatFwdOutProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrQosQStatFwdOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatDpdHiPrioOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatDpdHiPrioPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatDpdLoPrioOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatDpdLoPrioPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatFwdInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatFwdInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatFwdOutProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatFwdOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatOffHiPrioOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatOffHiPrioPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatOffLoPrioOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatOffLoPrioPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatUncolOctsOff"),
        ("TIMETRA-PORT-MIB", "tmnxPortIngQosQStatUncolPktsOff"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgrQDroInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgrQDroInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgrQDroOutProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgrQDroOutProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgrQFwdInProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgrQFwdInProfPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgrQFwdOutProfOcts"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetEgrQFwdOutProfPkts"))
)
if mibBuilder.loadTexts:
    tmnxPortQStatV7v0Group.setStatus("current")

tmnxPortEthernetV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 63)
)
tmnxPortEthernetV7v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEtherMTU"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDuplex"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherAutoNegotiate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherOperDuplex"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherOperSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherCollectStats"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherMDIMDIX"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherXGigMode"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherEgressRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDot1qEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherQinqEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherIngressRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherHCOverPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherHCPkts1519toMax"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherLacpTunnel"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedEnabled"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedKeepAlive"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedRetry"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownWhenLoopedState"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherPBBEtype"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSingleFiber"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSSM"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDWLUseBroadcastAddr"))
)
if mibBuilder.loadTexts:
    tmnxPortEthernetV7v0Group.setStatus("current")

tmnxPortGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 64)
)
tmnxPortGroupV7v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortTableLastChange"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxPortType"),
        ("TIMETRA-PORT-MIB", "tmnxPortClass"),
        ("TIMETRA-PORT-MIB", "tmnxPortDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortName"),
        ("TIMETRA-PORT-MIB", "tmnxPortAlias"),
        ("TIMETRA-PORT-MIB", "tmnxPortUserAssignedMac"),
        ("TIMETRA-PORT-MIB", "tmnxPortMacAddress"),
        ("TIMETRA-PORT-MIB", "tmnxPortHwMacAddress"),
        ("TIMETRA-PORT-MIB", "tmnxPortMode"),
        ("TIMETRA-PORT-MIB", "tmnxPortEncapType"),
        ("TIMETRA-PORT-MIB", "tmnxPortLagId"),
        ("TIMETRA-PORT-MIB", "tmnxPortHoldTimeUp"),
        ("TIMETRA-PORT-MIB", "tmnxPortHoldTimeDown"),
        ("TIMETRA-PORT-MIB", "tmnxPortUpProtocols"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectorType"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverType"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverLaserWaveLen"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverDiagCapable"),
        ("TIMETRA-PORT-MIB", "tmnxPortTransceiverModelNumber"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPConnectorCode"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorOUI"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorManufactureDate"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPMedia"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPEquipped"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorSerialNum"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPVendorPartNum"),
        ("TIMETRA-PORT-MIB", "tmnxPortEquipped"),
        ("TIMETRA-PORT-MIB", "tmnxPortLinkStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortAdminStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortState"),
        ("TIMETRA-PORT-MIB", "tmnxPortPrevState"),
        ("TIMETRA-PORT-MIB", "tmnxPortNumAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxPortAlarmState"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastAlarmEvent"),
        ("TIMETRA-PORT-MIB", "tmnxPortClearAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastStateChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPortNumChannels"),
        ("TIMETRA-PORT-MIB", "tmnxPortNetworkEgrQueues"),
        ("TIMETRA-PORT-MIB", "tmnxPortIsLeaf"),
        ("TIMETRA-PORT-MIB", "tmnxPortChanType"),
        ("TIMETRA-PORT-MIB", "tmnxPortParentPortID"),
        ("TIMETRA-PORT-MIB", "tmnxPortLoadBalanceAlgorithm"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeName"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortTypeStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeName"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortConnectTypeStatus"),
        ("TIMETRA-PORT-MIB", "tmnxChannelPortID"),
        ("TIMETRA-PORT-MIB", "tmnxPortOpticalCompliance"),
        ("TIMETRA-PORT-MIB", "tmnxL4LoadBalancing"),
        ("TIMETRA-PORT-MIB", "tmnxLsrIpLoadBalancing"),
        ("TIMETRA-PORT-MIB", "tmnxPortLastClearedTime"),
        ("TIMETRA-PORT-MIB", "tmnxPortDDMEventSuppression"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortReasonDownFlags"),
        ("TIMETRA-PORT-MIB", "tmnxPortSSMRxQualityLevel"),
        ("TIMETRA-PORT-MIB", "tmnxPortDwdmLaserChannel"),
        ("TIMETRA-PORT-MIB", "tmnxPortOtuCapable"),
        ("TIMETRA-PORT-MIB", "tmnxSonetSuppressLoOrderAlarm"))
)
if mibBuilder.loadTexts:
    tmnxPortGroupV7v0.setStatus("current")

tmnxPortNotifyObjsGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 65)
)
tmnxPortNotifyObjsGroupV7v0.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyDescription")
)
if mibBuilder.loadTexts:
    tmnxPortNotifyObjsGroupV7v0.setStatus("current")

tmnxPortEtherObsoleteV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 67)
)
tmnxPortEtherObsoleteV7v0Group.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortEtherReasonDownFlags")
)
if mibBuilder.loadTexts:
    tmnxPortEtherObsoleteV7v0Group.setStatus("current")

tmnxPortTDMGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 68)
)
tmnxPortTDMGroupV7v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxDS3ChannelAcctPolicyId"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelCollectStats"),
        ("TIMETRA-PORT-MIB", "tmnxDS3Buildout"),
        ("TIMETRA-PORT-MIB", "tmnxDS3Type"),
        ("TIMETRA-PORT-MIB", "tmnxDS3LastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelType"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelFraming"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelClockSource"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelChannelized"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrateCSUMode"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelSubrate"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelIdleCycleFlags"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBitErrorInsertionRate"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTPattern"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTDuration"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLEicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLLicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLFicString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLUnitString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPfiString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLPortString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLGenString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMessageType"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelFEACLoopRespond"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelCRC"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelInFEACLoop"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonPortString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelMDLMonGenString"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTSynched"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTErrors"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelBERTTotalBits"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelScramble"),
        ("TIMETRA-PORT-MIB", "tmnxDS1RowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Type"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Framing"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Loopback"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InvertData"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BitErrorInsertionRate"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTPattern"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTDuration"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ReportAlarmStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1LastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS1ClockSource"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTSynched"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTErrors"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BERTTotalBits"),
        ("TIMETRA-PORT-MIB", "tmnxDS1RemoteLoopRespond"),
        ("TIMETRA-PORT-MIB", "tmnxDS1InRemoteLoop"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BerSdThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxDS1BerSfThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupTimeSlots"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupSpeed"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupCRC"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupOperMTU"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupLastChangeTime"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupIdleCycleFlags"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupScramble"),
        ("TIMETRA-PORT-MIB", "tmnxDS0ChanGroupBerSfLinkDown"))
)
if mibBuilder.loadTexts:
    tmnxPortTDMGroupV7v0.setStatus("current")

tmnxPortTDME1GroupV6v1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 69)
)
tmnxPortTDME1GroupV6v1.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxDS1NationalUseBits")
)
if mibBuilder.loadTexts:
    tmnxPortTDME1GroupV6v1.setStatus("current")

tmnxPortNotifyObjsGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 70)
)
tmnxPortNotifyObjsGroupV8v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyWTAlarmReason"),
        ("TIMETRA-PORT-MIB", "tmnxHostMatchNotifyIntDestId"),
        ("TIMETRA-PORT-MIB", "tmnxHostMatchNotifyOrgString"),
        ("TIMETRA-PORT-MIB", "tmnxHostMatchNotifySubIdent"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyObjsGroupV8v0.setStatus("current")

tmnxWaveTrackerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 71)
)
tmnxWaveTrackerGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortWaveTrackerCapable"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerAlarmState"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerCfgAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerEncodeEnable"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerInUse"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerLowerPowerMargin"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerMaxAttainablePwr"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerMeasuredPower"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerMinAttainablePwr"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerPowerCtrlEnable"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerTargetPower"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerTrailName"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerUpperPowerMargin"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerWaveKey1"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerWaveKey2"))
)
if mibBuilder.loadTexts:
    tmnxWaveTrackerGroup.setStatus("current")

tmnxPortGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 72)
)
tmnxPortGroupV8v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortHybridIngAccessWeight"),
        ("TIMETRA-PORT-MIB", "tmnxPortHybridIngNetworkWeight"),
        ("TIMETRA-PORT-MIB", "tmnxPortHybridEgrAccessWeight"),
        ("TIMETRA-PORT-MIB", "tmnxPortHybridEgrNetworkWeight"),
        ("TIMETRA-PORT-MIB", "tmnxPortInterfaceGroupHandlerIdx"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSSMCodeType"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSSMTxDus"),
        ("TIMETRA-PORT-MIB", "tmnxSonetTxDus"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverMBSBytes"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverMBSBytes"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverMBSBytes"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverAdminPIRPercent"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverAdminCIRPercent"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverRateType"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverAdminPIRPercent"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverAdminCIRPercent"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverRateType"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpHMTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpHMRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpHMLastChgd"),
        ("TIMETRA-PORT-MIB", "tmnxPortHoldTimeUnits"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortHMRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortHMLastChgd"),
        ("TIMETRA-PORT-MIB", "tmnxSonetTxS1Byte"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSSMRxEsmc"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSSMTxQualityLevel"))
)
if mibBuilder.loadTexts:
    tmnxPortGroupV8v0.setStatus("current")

tmnxPortDwdmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 73)
)
tmnxPortDwdmGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortDwdmLaserChannel"),
        ("TIMETRA-PORT-MIB", "tmnxPortDwdmRxDtvAdjustEnable"),
        ("TIMETRA-PORT-MIB", "tmnxPortDwdmRxDtvDacPercent"))
)
if mibBuilder.loadTexts:
    tmnxPortDwdmGroup.setStatus("current")

tmnxPortATMGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 74)
)
tmnxPortATMGroupV7v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxATMIntfCellFormat"),
        ("TIMETRA-PORT-MIB", "tmnxATMIntfMinVpValue"),
        ("TIMETRA-PORT-MIB", "tmnxATMIntfMapping"),
        ("TIMETRA-PORT-MIB", "tmnxATMIntfCustomBufferMode"),
        ("TIMETRA-PORT-MIB", "tmnxATMIntfBufferPool"),
        ("TIMETRA-PORT-MIB", "tmnxATMIntfVcThreshold"))
)
if mibBuilder.loadTexts:
    tmnxPortATMGroupV7v0.setStatus("current")

tmnxPortCEMGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 75)
)
tmnxPortCEMGroupV8v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortCemStatsReportAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsIgrForwardedPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsIgrDroppedPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrForwardedPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrDroppedPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrMissingPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrPktsReOrder"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrJtrBfrURun"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrJtrBfrORun"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrMisOrderDrop"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrMalformedPkts"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrLBitDrop"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrMultipleDrop"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrESs"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrSESs"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrUASs"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrFailureCounts"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrURunCounts"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrORunCounts"),
        ("TIMETRA-PORT-MIB", "tmnxPortCemStatsEgrJtrBfrDepth"))
)
if mibBuilder.loadTexts:
    tmnxPortCEMGroupV8v0.setStatus("current")

tmnxPortQV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 76)
)
tmnxPortQV8v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tPortAccEgrQGrpAggRateLimit"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpSchedPol"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpAcctgPolId"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpCollectStats"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpFrameBaseActg"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverLastChanged"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverAdminCIR"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverAdminPIR"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverCBS"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverHiPrioOnly"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpSchedPol"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpAcctgPolId"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpCollectStats"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverLastChanged"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverAdminCIR"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverAdminPIR"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverCBS"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverHiPrioOnly"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpAcctgPolId"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpAggRateLimit"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpCollectStats"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpFrameBaseActg"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpSchedPol"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverAdminCIR"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverAdminPIR"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverCBS"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverHiPrioOnly"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverLastChanged"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverCIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQOverPIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverCIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverPIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverCIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverPIRAdaptation"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQGrpDescr"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpDescr"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpDescr"))
)
if mibBuilder.loadTexts:
    tmnxPortQV8v0Group.setStatus("current")

tmnxPortQObsoleteV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 77)
)
tmnxPortQObsoleteV8v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tPortAccEgrQOverMBS"),
        ("TIMETRA-PORT-MIB", "tPortAccIngQOverMBS"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQOverMBS"))
)
if mibBuilder.loadTexts:
    tmnxPortQObsoleteV8v0Group.setStatus("current")

tmnxPortSchedStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 79)
)
tmnxPortSchedStatsGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tPortAccEgrSchedStatFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrSchedStatFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortAccIngSchedStatFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortAccIngSchedStatFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrSchedStatFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrSchedStatFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrSchedStatFwdOctsHi"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrSchedStatFwdOctsLo"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrSchedStatFwdPktsHi"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrSchedStatFwdPktsLo"),
        ("TIMETRA-PORT-MIB", "tPortAccIngSchedStatFwdOctsHi"),
        ("TIMETRA-PORT-MIB", "tPortAccIngSchedStatFwdOctsLo"),
        ("TIMETRA-PORT-MIB", "tPortAccIngSchedStatFwdPktsHi"),
        ("TIMETRA-PORT-MIB", "tPortAccIngSchedStatFwdPktsLo"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrSchedStatFwdOctsHi"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrSchedStatFwdOctsLo"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrSchedStatFwdPktsHi"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrSchedStatFwdPktsLo"))
)
if mibBuilder.loadTexts:
    tmnxPortSchedStatsGroup.setStatus("current")

tmnxPortVPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 80)
)
tmnxPortVPortGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tPortEgrVPortDescr"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortLastChanged"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortSchedPol"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortHMTableLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxPortVPortGroup.setStatus("obsolete")

tmnxMlpppBundleGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 81)
)
tmnxMlpppBundleGroupV7v0.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxBundleMlpppStatelessApsSwo")
)
if mibBuilder.loadTexts:
    tmnxMlpppBundleGroupV7v0.setStatus("current")

tmnxOpticalPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 82)
)
tmnxOpticalPortGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxOpticalPortAmpCfgAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmCtrlMode"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmManCfgDisp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmCfgRxChan"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmCfgAlarms"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortHasRxAmplifier"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortHasRxTdcm"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortAmpPowerIn"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortAmpGain"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortAmpPowerOut"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortAmpPumpTemp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortAmpModuleTemp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortAmpPumpCurrent"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortAmpAlarmState"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortAmpSerialNum"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortAmpCtrlState"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmPowerIn"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmLoss"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmPowerOut"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmRtd1Temp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmRtd2Temp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmRtd3Temp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmRtd4Temp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmModuleTemp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmMinDisp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmMaxDisp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmAutoDisp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmMeasDisp"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmPresRxChan"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmAlarmState"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmSerialNum"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmCtrlState"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmDispSwpStart"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmDispSwpEnd"))
)
if mibBuilder.loadTexts:
    tmnxOpticalPortGroup.setStatus("current")

tmnxPortATMGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 90)
)
tmnxPortATMGroupV9v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortATMVpShaperTblLastCh"),
        ("TIMETRA-PORT-MIB", "tmnxPortATMVpShaperRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortATMVpShaperLastMgmtCh"),
        ("TIMETRA-PORT-MIB", "tmnxPortATMVpShaperEgrAtd"))
)
if mibBuilder.loadTexts:
    tmnxPortATMGroupV9v0.setStatus("current")

tmnxPortVPortV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 91)
)
tmnxPortVPortV9v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tPortEgrVPortDescr"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortLastChanged"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortRowStatus"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortSchedPol"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortHMTableLastChgd"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortAggRateLimit"))
)
if mibBuilder.loadTexts:
    tmnxPortVPortV9v0Group.setStatus("current")

tmnxPortEgrExpShaperV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 92)
)
tmnxPortEgrExpShaperV9v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperTblLastChngd"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperRate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass1Rate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass2Rate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass3Rate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass4Rate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass5Rate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass6Rate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass7Rate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass8Rate"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperLastChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass1Thresh"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass2Thresh"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass3Thresh"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass4Thresh"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass5Thresh"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass6Thresh"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass7Thresh"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperClass8Thresh"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperLoBrstMaxCls"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls1StFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls1StFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls1StMonOvrOct"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls2StFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls2StFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls2StMonOvrOct"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls3StFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls3StFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls3StMonOvrOct"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls4StFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls4StFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls4StMonOvrOct"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls5StFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls5StFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls5StMonOvrOct"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls6StFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls6StFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls6StMonOvrOct"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls7StFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls7StFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls7StMonOvrOct"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls8StFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls8StFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls8StMonOvrOct"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperAggStFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperAggStFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperAggStMonOvrOct"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperStLstClrdTime"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls1StFwdPktsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls1StFwdPktsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls1StFwdOctsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls1StFwdOctsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls1StMonOvrOL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls1StMonOvrOH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls2StFwdPktsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls2StFwdPktsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls2StFwdOctsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls2StFwdOctsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls2StMonOvrOL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls2StMonOvrOH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls3StFwdPktsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls3StFwdPktsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls3StFwdOctsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls3StFwdOctsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls3StMonOvrOL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls3StMonOvrOH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls4StFwdPktsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls4StFwdPktsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls4StFwdOctsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls4StFwdOctsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls4StMonOvrOL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls4StMonOvrOH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls5StFwdPktsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls5StFwdPktsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls5StFwdOctsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls5StFwdOctsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls5StMonOvrOL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls5StMonOvrOH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls6StFwdPktsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls6StFwdPktsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls6StFwdOctsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls6StFwdOctsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls6StMonOvrOL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls6StMonOvrOH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls7StFwdPktsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls7StFwdPktsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls7StFwdOctsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls7StFwdOctsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls7StMonOvrOL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls7StMonOvrOH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls8StFwdPktsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls8StFwdPktsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls8StFwdOctsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls8StFwdOctsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls8StMonOvrOL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperCls8StMonOvrOH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperAggStFwdPktsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperAggStFwdPktsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperAggStFwdOctsL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperAggStFwdOctsH"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperAggStMonOvrOL"),
        ("TIMETRA-PORT-MIB", "tPortEgrExpShaperAggStMonOvrOH"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperThresh"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperLoBurstLimit"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperHiBurstInc"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperCl1BrstLimit"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperCl2BrstLimit"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperCl3BrstLimit"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperCl4BrstLimit"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperCl5BrstLimit"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperCl6BrstLimit"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperCl7BrstLimit"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrExpShaperCl8BrstLimit"))
)
if mibBuilder.loadTexts:
    tmnxPortEgrExpShaperV9v0Group.setStatus("current")

tmnxPortObjAppV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 94)
)
tmnxPortObjAppV9v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxObjectAppResvCbsAmbrAlrmStep"),
        ("TIMETRA-PORT-MIB", "tmnxObjectAppResvCbsAmbrAlrmMax"),
        ("TIMETRA-PORT-MIB", "tmnxObjectAppAmbrAlrmThresh"),
        ("TIMETRA-PORT-MIB", "tmnxObjectAppRedAlrmThresh"))
)
if mibBuilder.loadTexts:
    tmnxPortObjAppV9v0Group.setStatus("current")

tmnxOpticalPortGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 95)
)
tmnxOpticalPortGroupV9v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxOpticalPortDwdmChannelMin"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortDwdmChannelMax"),
        ("TIMETRA-PORT-MIB", "tmnxOpticalPortLaserTunability"))
)
if mibBuilder.loadTexts:
    tmnxOpticalPortGroupV9v0.setStatus("current")

tmnxPortNotifyObjsGroupV8v9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 96)
)
tmnxPortNotifyObjsGroupV8v9.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxObjType"),
        ("TIMETRA-PORT-MIB", "tmnxObjPortId"),
        ("TIMETRA-PORT-MIB", "tmnxObjMdaId"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppType"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppPool"),
        ("TIMETRA-PORT-MIB", "tmnxObjNamedPoolPolicy"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvSize"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppSumOfQResvSize"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvCbsOld"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvCbsNew"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvSizeOld"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyObjsGroupV8v9.setStatus("current")

tmnxPortEgrVPortStatsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 99)
)
tmnxPortEgrVPortStatsV9v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tPortEgrVPStLstClrdTime"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlFwdPkt"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlFwdOct"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlDpdPkt"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlDpdOct"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlFwdPktL"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlFwdPktH"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlFwdOctL"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlFwdOctH"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlDpdPktL"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlDpdPktH"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlDpdOctL"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPStLvlDpdOctH"))
)
if mibBuilder.loadTexts:
    tmnxPortEgrVPortStatsV9v0Group.setStatus("current")

tmnxPortNotifyObjsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 100)
)
tmnxPortNotifyObjsV9v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherCrcThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherCrcMultiplier"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherCrcAlarmValue"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyObjsV9v0Group.setStatus("current")

tmnxPortEtherV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 101)
)
tmnxPortEtherV9v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEtherCrcMonSdThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherCrcMonSdTMultiplier"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherCrcMonSfThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherCrcMonSfTMultiplier"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherCrcMonWindowSize"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherCrcAlarmReason"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDownOnInternalError"))
)
if mibBuilder.loadTexts:
    tmnxPortEtherV9v0Group.setStatus("current")

tmnxPortV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 103)
)
tmnxPortV9v0Group.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortLinkLengthInfo")
)
if mibBuilder.loadTexts:
    tmnxPortV9v0Group.setStatus("current")

tmnxPortNetEgrV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 104)
)
tmnxPortNetEgrV10v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPlcrCntrlPolicy"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStatMode"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffInProfPkt"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffInProfPktL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffInProfPktH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdInProfPkt"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdInProfPktL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdInProfPktH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpInProfPkt"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpInProfPktL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpInProfPktH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffOutProfPkt"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffOutProfPktL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffOutProfPktH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdOutProfPkt"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdOutProfPktL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdOutProfPktH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpOutProfPkt"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpOutProfPktL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpOutProfPktH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffInProfOct"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffInProfOctL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffInProfOctH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdInProfOct"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdInProfOctL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdInProfOctH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpInProfOct"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpInProfOctL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpInProfOctH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffOutProfOct"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffOutProfOctL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStOffOutProfOctH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdOutProfOct"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdOutProfOctL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStFwdOutProfOctH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpOutProfOct"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpOutProfOctL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStDrpOutProfOctH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStUncolPktOff"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStUncolPktOffL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStUncolPktOffH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStUncolOctOff"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStUncolOctOffL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpPStUncolOctOffH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpArbitStatFwdPkts"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpArbitStatFwdPktsL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpArbitStatFwdPktsH"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpArbitStatFwdOcts"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpArbitStatFwdOctsL"),
        ("TIMETRA-PORT-MIB", "tPortNetEgrQGrpArbitStatFwdOctsH"))
)
if mibBuilder.loadTexts:
    tmnxPortNetEgrV10v0Group.setStatus("current")

tmnxDDMLaneGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 105)
)
tmnxDDMLaneGroupV10v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortSFPNumLanes"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTemperature"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTempLowWarn"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTempLowAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTempHiWarn"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTempHiAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTxBiasCurrent"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTxBiasCurrentLowWarn"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTxBiasCurrentLowAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTxBiasCurrentHiWarn"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTxBiasCurrentHiAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTxOutputPower"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTxOutputPowerLowWarn"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTxOutputPowerLowAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTxOutputPowerHiWarn"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneTxOutputPowerHiAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneRxOpticalPower"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneRxOpticalPwrLowWarn"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneRxOpticalPwrLowAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneRxOpticalPwrHiWarn"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneRxOpticalPwrHiAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneRxOpticalPowerType"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneFailedThresholds"))
)
if mibBuilder.loadTexts:
    tmnxDDMLaneGroupV10v0.setStatus("current")

tmnxPortNotifyObjsGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 106)
)
tmnxPortNotifyObjsGroupV10v0.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxDDMLaneIdOrModule")
)
if mibBuilder.loadTexts:
    tmnxPortNotifyObjsGroupV10v0.setStatus("current")

tmnxPortPlcyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 107)
)
tmnxPortPlcyGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortPlcyTableLastCh"),
        ("TIMETRA-PORT-MIB", "tmnxPortPlcyRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortPlcyLastCh"),
        ("TIMETRA-PORT-MIB", "tmnxPortPlcyDescription"),
        ("TIMETRA-PORT-MIB", "tmnxPortPlcyEgrPortSchedPlcy"))
)
if mibBuilder.loadTexts:
    tmnxPortPlcyGroup.setStatus("current")

tmnxPortLoadBalGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 108)
)
tmnxPortLoadBalGroupV10v0.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxIpLoadBalancing")
)
if mibBuilder.loadTexts:
    tmnxPortLoadBalGroupV10v0.setStatus("current")

tmnxPortEthernetV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 109)
)
tmnxPortEthernetV10v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEtherMinFrameLength"),
        ("TIMETRA-PORT-MIB", "tmnxPortPhysStateChangeCount"))
)
if mibBuilder.loadTexts:
    tmnxPortEthernetV10v0Group.setStatus("current")

tmnxHsmdaGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 110)
)
tmnxHsmdaGroupV10v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEgrHsmdaSchedPlcy"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrTblLastChngd"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrLastChanged"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrMaxRate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrGrp1Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrGrp2Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass1Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass1WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass2Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass2WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass3Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass3WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass4Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass4WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass5Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass5WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass6Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass6WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass7Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass7WtInGp"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass8Rate"),
        ("TIMETRA-PORT-MIB", "tmnxHsmdaPortSchOvrClass8WtInGp"))
)
if mibBuilder.loadTexts:
    tmnxHsmdaGroupV10v0.setStatus("current")

tmnxPortObsoletedV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 111)
)
tmnxPortObsoletedV10v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortEgrShaperTblLastChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrShaperRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrShaperLastChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPortEgrShaperRate"))
)
if mibBuilder.loadTexts:
    tmnxPortObsoletedV10v0Group.setStatus("current")

tmnxPwPortV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 112)
)
tmnxPwPortV10v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPwPortTblLastChanged"),
        ("TIMETRA-PORT-MIB", "tmnxPwPortRowStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPwPortLastChgd"),
        ("TIMETRA-PORT-MIB", "tmnxPwPortEncapType"))
)
if mibBuilder.loadTexts:
    tmnxPwPortV10v0Group.setStatus("current")


# Notification objects

tmnxEqOobPortFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 1)
)
tmnxEqOobPortFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"))
)
if mibBuilder.loadTexts:
    tmnxEqOobPortFailure.setStatus(
        "obsolete"
    )

tmnxEqPortFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 2)
)
tmnxEqPortFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"))
)
if mibBuilder.loadTexts:
    tmnxEqPortFailure.setStatus(
        "obsolete"
    )

tmnxQosServiceDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 3)
)
tmnxQosServiceDegraded.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"))
)
if mibBuilder.loadTexts:
    tmnxQosServiceDegraded.setStatus(
        "obsolete"
    )

tmnxEqPortSonetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 4)
)
tmnxEqPortSonetAlarm.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifySonetAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSonetAlarm.setStatus(
        "current"
    )

tmnxEqPortSonetAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 5)
)
tmnxEqPortSonetAlarmClear.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifySonetAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSonetAlarmClear.setStatus(
        "current"
    )

tmnxEqPortSonetPathAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 6)
)
tmnxEqPortSonetPathAlarm.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifySonetPathAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSonetPathAlarm.setStatus(
        "current"
    )

tmnxEqPortSonetPathAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 7)
)
tmnxEqPortSonetPathAlarmClear.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifySonetPathAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSonetPathAlarmClear.setStatus(
        "current"
    )

tmnxEqPortSFPInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 8)
)
tmnxEqPortSFPInserted.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortSFPInserted.setStatus(
        "current"
    )

tmnxEqPortSFPRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 9)
)
tmnxEqPortSFPRemoved.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortSFPRemoved.setStatus(
        "current"
    )

tmnxEqPortWrongSFP = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 10)
)
tmnxEqPortWrongSFP.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortWrongSFP.setStatus(
        "obsolete"
    )

tmnxEqPortSFPCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 11)
)
tmnxEqPortSFPCorrupted.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortSFPCorrupted.setStatus(
        "obsolete"
    )

tmnxPortNotifyBerSdTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 12)
)
tmnxPortNotifyBerSdTca.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxSonetBerSdThreshold"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyBerSdTca.setStatus(
        "obsolete"
    )

tmnxPortNotifyBerSfTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 13)
)
tmnxPortNotifyBerSfTca.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxSonetBerSfThreshold"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyBerSfTca.setStatus(
        "obsolete"
    )

tmnxEqPortError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 14)
)
tmnxEqPortError.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyError"))
)
if mibBuilder.loadTexts:
    tmnxEqPortError.setStatus(
        "current"
    )

tmnxEqPortDS3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 15)
)
tmnxEqPortDS3Alarm.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyDS3AlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortDS3Alarm.setStatus(
        "current"
    )

tmnxEqPortDS3AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 16)
)
tmnxEqPortDS3AlarmClear.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyDS3AlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortDS3AlarmClear.setStatus(
        "current"
    )

tmnxEqPortDS1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 17)
)
tmnxEqPortDS1Alarm.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyDS1AlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortDS1Alarm.setStatus(
        "current"
    )

tmnxEqPortDS1AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 18)
)
tmnxEqPortDS1AlarmClear.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyDS1AlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortDS1AlarmClear.setStatus(
        "current"
    )

tmnxEqPortBndlYellowDiffExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 19)
)
tmnxEqPortBndlYellowDiffExceeded.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxBundleYellowDiffDelay"))
)
if mibBuilder.loadTexts:
    tmnxEqPortBndlYellowDiffExceeded.setStatus(
        "current"
    )

tmnxEqPortBndlRedDiffExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 20)
)
tmnxEqPortBndlRedDiffExceeded.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxBundleRedDiffDelay"))
)
if mibBuilder.loadTexts:
    tmnxEqPortBndlRedDiffExceeded.setStatus(
        "current"
    )

tmnxEqPortBndlBadEndPtDiscr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 21)
)
tmnxEqPortBndlBadEndPtDiscr.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxBundleMemberDownReason")
)
if mibBuilder.loadTexts:
    tmnxEqPortBndlBadEndPtDiscr.setStatus(
        "current"
    )

tmnxEqPortEtherAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 22)
)
tmnxEqPortEtherAlarm.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherAlarm.setStatus(
        "current"
    )

tmnxEqPortEtherAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 23)
)
tmnxEqPortEtherAlarmClear.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherAlarmReason"))
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherAlarmClear.setStatus(
        "current"
    )

tmnxDS1E1LoopbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 24)
)
tmnxDS1E1LoopbackStarted.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Loopback"))
)
if mibBuilder.loadTexts:
    tmnxDS1E1LoopbackStarted.setStatus(
        "current"
    )

tmnxDS1E1LoopbackStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 25)
)
tmnxDS1E1LoopbackStopped.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxDS1Loopback"))
)
if mibBuilder.loadTexts:
    tmnxDS1E1LoopbackStopped.setStatus(
        "current"
    )

tmnxDS3E3LoopbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 26)
)
tmnxDS3E3LoopbackStarted.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"))
)
if mibBuilder.loadTexts:
    tmnxDS3E3LoopbackStarted.setStatus(
        "current"
    )

tmnxDS3E3LoopbackStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 27)
)
tmnxDS3E3LoopbackStopped.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxDS3ChannelLoopback"))
)
if mibBuilder.loadTexts:
    tmnxDS3E3LoopbackStopped.setStatus(
        "current"
    )

tmnxSonetSDHLoopbackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 28)
)
tmnxSonetSDHLoopbackStarted.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxSonetLoopback"))
)
if mibBuilder.loadTexts:
    tmnxSonetSDHLoopbackStarted.setStatus(
        "current"
    )

tmnxSonetSDHLoopbackStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 29)
)
tmnxSonetSDHLoopbackStopped.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxSonetLoopback"))
)
if mibBuilder.loadTexts:
    tmnxSonetSDHLoopbackStopped.setStatus(
        "current"
    )

tmnxEqPortEtherLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 30)
)
tmnxEqPortEtherLoopDetected.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherLoopDetected.setStatus(
        "current"
    )

tmnxEqPortEtherLoopCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 31)
)
tmnxEqPortEtherLoopCleared.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherLoopCleared.setStatus(
        "current"
    )

tmnxEqPortSpeedCfgNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 32)
)
tmnxEqPortSpeedCfgNotCompatible.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherSpeed"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaNotifyType"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSpeedCfgNotCompatible.setStatus(
        "current"
    )

tmnxEqPortDuplexCfgNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 33)
)
tmnxEqPortDuplexCfgNotCompatible.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortEtherDuplex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaNotifyType"))
)
if mibBuilder.loadTexts:
    tmnxEqPortDuplexCfgNotCompatible.setStatus(
        "current"
    )

tmnxEqPortIngressRateCfgNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 34)
)
tmnxEqPortIngressRateCfgNotCompatible.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaNotifyType"))
)
if mibBuilder.loadTexts:
    tmnxEqPortIngressRateCfgNotCompatible.setStatus(
        "current"
    )

tmnxEqDigitalDiagMonitorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 35)
)
tmnxEqDigitalDiagMonitorFailure.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxDDMFailedObject"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneIdOrModule"))
)
if mibBuilder.loadTexts:
    tmnxEqDigitalDiagMonitorFailure.setStatus(
        "current"
    )

tmnxEqPortSFPStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 36)
)
tmnxEqPortSFPStatusFailure.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortSFPStatus"))
)
if mibBuilder.loadTexts:
    tmnxEqPortSFPStatusFailure.setStatus(
        "current"
    )

tmnxDSXClockSyncStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 37)
)
tmnxDSXClockSyncStateChange.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxDSXClockSyncStateObject"))
)
if mibBuilder.loadTexts:
    tmnxDSXClockSyncStateChange.setStatus(
        "current"
    )

tmnxPortUnsupportedFunction = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 38)
)
tmnxPortUnsupportedFunction.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxPortUnsupportedFunction.setStatus(
        "current"
    )

tmnxBundleMemberMlfrLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 39)
)
tmnxBundleMemberMlfrLoopback.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxBundleMemberMlfrDownReason")
)
if mibBuilder.loadTexts:
    tmnxBundleMemberMlfrLoopback.setStatus(
        "current"
    )

tmnxEqPortWaveTrackerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 40)
)
tmnxEqPortWaveTrackerAlarm.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyWTAlarmReason"),
        ("TIMETRA-PORT-MIB", "tmnxWaveTrackerAlarmState"))
)
if mibBuilder.loadTexts:
    tmnxEqPortWaveTrackerAlarm.setStatus(
        "current"
    )

tPortAccEgrQGrpHostMatchFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 41)
)
tPortAccEgrQGrpHostMatchFailure.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxHostMatchNotifyIntDestId"),
        ("TIMETRA-PORT-MIB", "tmnxHostMatchNotifyOrgString"),
        ("TIMETRA-PORT-MIB", "tmnxHostMatchNotifySubIdent"))
)
if mibBuilder.loadTexts:
    tPortAccEgrQGrpHostMatchFailure.setStatus(
        "current"
    )

tPortEgrVPortHostMatchFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 42)
)
tPortEgrVPortHostMatchFailure.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxHostMatchNotifyIntDestId"),
        ("TIMETRA-PORT-MIB", "tmnxHostMatchNotifyOrgString"),
        ("TIMETRA-PORT-MIB", "tmnxHostMatchNotifySubIdent"))
)
if mibBuilder.loadTexts:
    tPortEgrVPortHostMatchFailure.setStatus(
        "current"
    )

tmnxEqDigitalDiagMonitorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 43)
)
tmnxEqDigitalDiagMonitorClear.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxDDMFailedObject"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneIdOrModule"))
)
if mibBuilder.loadTexts:
    tmnxEqDigitalDiagMonitorClear.setStatus(
        "current"
    )

tmnxEqPortOpticalAmpAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 44)
)
tmnxEqPortOpticalAmpAlarm.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxOpticalPortAmpAlarmState")
)
if mibBuilder.loadTexts:
    tmnxEqPortOpticalAmpAlarm.setStatus(
        "current"
    )

tmnxEqPortOpticalTdcmAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 45)
)
tmnxEqPortOpticalTdcmAlarm.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxOpticalPortTdcmAlarmState")
)
if mibBuilder.loadTexts:
    tmnxEqPortOpticalTdcmAlarm.setStatus(
        "current"
    )

tmnxEqSonetClockSrcNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 46)
)
tmnxEqSonetClockSrcNotCompatible.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxSonetClockSource"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaNotifyType"))
)
if mibBuilder.loadTexts:
    tmnxEqSonetClockSrcNotCompatible.setStatus(
        "current"
    )

tmnxEqSonetSfThreshNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 47)
)
tmnxEqSonetSfThreshNotCompatible.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxSonetBerSfThreshold"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaNotifyType"))
)
if mibBuilder.loadTexts:
    tmnxEqSonetSfThreshNotCompatible.setStatus(
        "current"
    )

tmnxEqSonetFramingNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 48)
)
tmnxEqSonetFramingNotCompatible.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxSonetFraming"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaNotifyType"))
)
if mibBuilder.loadTexts:
    tmnxEqSonetFramingNotCompatible.setStatus(
        "current"
    )

tmnxResvCbsPoolThreshGreen = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 49)
)
tmnxResvCbsPoolThreshGreen.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxObjType"),
        ("TIMETRA-PORT-MIB", "tmnxObjPortId"),
        ("TIMETRA-PORT-MIB", "tmnxObjMdaId"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppType"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppPool"),
        ("TIMETRA-PORT-MIB", "tmnxObjNamedPoolPolicy"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvSize"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppSumOfQResvSize"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvCbsOld"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvCbsNew"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvSizeOld"))
)
if mibBuilder.loadTexts:
    tmnxResvCbsPoolThreshGreen.setStatus(
        "current"
    )

tmnxResvCbsPoolThreshAmber = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 50)
)
tmnxResvCbsPoolThreshAmber.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxObjType"),
        ("TIMETRA-PORT-MIB", "tmnxObjPortId"),
        ("TIMETRA-PORT-MIB", "tmnxObjMdaId"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppType"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppPool"),
        ("TIMETRA-PORT-MIB", "tmnxObjNamedPoolPolicy"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvSize"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppSumOfQResvSize"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvCbsOld"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvCbsNew"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvSizeOld"))
)
if mibBuilder.loadTexts:
    tmnxResvCbsPoolThreshAmber.setStatus(
        "current"
    )

tmnxResvCbsPoolThreshRed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 51)
)
tmnxResvCbsPoolThreshRed.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxObjType"),
        ("TIMETRA-PORT-MIB", "tmnxObjPortId"),
        ("TIMETRA-PORT-MIB", "tmnxObjMdaId"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppType"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppPool"),
        ("TIMETRA-PORT-MIB", "tmnxObjNamedPoolPolicy"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvSize"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppSumOfQResvSize"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvCbsOld"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvCbsNew"),
        ("TIMETRA-PORT-MIB", "tmnxObjAppResvSizeOld"))
)
if mibBuilder.loadTexts:
    tmnxResvCbsPoolThreshRed.setStatus(
        "current"
    )

tmnxEqPortEtherCrcAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 52)
)
tmnxEqPortEtherCrcAlarm.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherCrcThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherCrcMultiplier"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherCrcAlarmValue"))
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherCrcAlarm.setStatus(
        "current"
    )

tmnxEqPortEtherCrcAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 53)
)
tmnxEqPortEtherCrcAlarmClear.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherCrcThreshold"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherCrcMultiplier"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyEtherCrcAlarmValue"))
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherCrcAlarmClear.setStatus(
        "current"
    )

tmnxEqPortEtherInternalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 54)
)
tmnxEqPortEtherInternalAlarm.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherInternalAlarm.setStatus(
        "current"
    )

tmnxEqPortEtherInternalAlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 2, 0, 55)
)
tmnxEqPortEtherInternalAlarmClr.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxEqPortEtherInternalAlarmClr.setStatus(
        "current"
    )


# Notifications groups

tmnxPortNotificationGroupR2r1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 17)
)
tmnxPortNotificationGroupR2r1.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPInserted"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPRemoved"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPCorrupted"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortError"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlYellowDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlRedDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlBadEndPtDiscr"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarmClear"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupR2r1.setStatus(
        "obsolete"
    )

tmnxPortNotifyObsoleteGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 20)
)
tmnxPortNotifyObsoleteGroup.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxEqOobPortFailure"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortFailure"),
        ("TIMETRA-PORT-MIB", "tmnxQosServiceDegraded"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyBerSdTca"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyBerSfTca"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortWrongSFP"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPCorrupted"))
)
if mibBuilder.loadTexts:
    tmnxPortNotifyObsoleteGroup.setStatus(
        "current"
    )

tmnxPortNotificationGroupV5v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 41)
)
tmnxPortNotificationGroupV5v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPInserted"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPRemoved"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPCorrupted"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortError"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlYellowDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlRedDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlBadEndPtDiscr"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSpeedCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDuplexCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortIngressRateCfgNotCompatible"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupV5v0.setStatus(
        "obsolete"
    )

tmnxPortNotificationGroupV6v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 46)
)
tmnxPortNotificationGroupV6v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPInserted"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPRemoved"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortError"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlYellowDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlRedDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlBadEndPtDiscr"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherLoopDetected"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherLoopCleared"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSpeedCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDuplexCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortIngressRateCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqDigitalDiagMonitorFailure"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPStatusFailure"),
        ("TIMETRA-PORT-MIB", "tmnxDSXClockSyncStateChange"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupV6v0.setStatus(
        "obsolete"
    )

tmnxPortNotificationGroupV3v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 50)
)
tmnxPortNotificationGroupV3v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPInserted"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPRemoved"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPCorrupted"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortError"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlYellowDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlRedDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlBadEndPtDiscr"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSpeedCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDuplexCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortIngressRateCfgNotCompatible"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupV3v0.setStatus(
        "obsolete"
    )

tmnxPortNotificationGroupV7v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 66)
)
tmnxPortNotificationGroupV7v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPInserted"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPRemoved"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortError"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlYellowDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlRedDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlBadEndPtDiscr"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherLoopDetected"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherLoopCleared"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSpeedCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDuplexCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortIngressRateCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqDigitalDiagMonitorFailure"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPStatusFailure"),
        ("TIMETRA-PORT-MIB", "tmnxDSXClockSyncStateChange"),
        ("TIMETRA-PORT-MIB", "tmnxPortUnsupportedFunction"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberMlfrLoopback"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortWaveTrackerAlarm"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupV7v0.setStatus(
        "obsolete"
    )

tmnxPortNotificationGroupV8v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 78)
)
tmnxPortNotificationGroupV8v0.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSonetPathAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPInserted"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPRemoved"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortError"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS3AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1Alarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDS1AlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlYellowDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlRedDiffExceeded"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortBndlBadEndPtDiscr"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxDS1E1LoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxDS3E3LoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStarted"),
        ("TIMETRA-PORT-MIB", "tmnxSonetSDHLoopbackStopped"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherLoopDetected"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherLoopCleared"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSpeedCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortDuplexCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortIngressRateCfgNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqDigitalDiagMonitorFailure"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortSFPStatusFailure"),
        ("TIMETRA-PORT-MIB", "tmnxDSXClockSyncStateChange"),
        ("TIMETRA-PORT-MIB", "tmnxPortUnsupportedFunction"),
        ("TIMETRA-PORT-MIB", "tmnxBundleMemberMlfrLoopback"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortWaveTrackerAlarm"),
        ("TIMETRA-PORT-MIB", "tPortAccEgrQGrpHostMatchFailure"),
        ("TIMETRA-PORT-MIB", "tPortEgrVPortHostMatchFailure"),
        ("TIMETRA-PORT-MIB", "tmnxEqDigitalDiagMonitorClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortOpticalAmpAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortOpticalTdcmAlarm"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupV8v0.setStatus(
        "current"
    )

tmnxPortNotificationGroupV9v4 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 93)
)
tmnxPortNotificationGroupV9v4.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxEqSonetClockSrcNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqSonetSfThreshNotCompatible"),
        ("TIMETRA-PORT-MIB", "tmnxEqSonetFramingNotCompatible"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupV9v4.setStatus(
        "current"
    )

tmnxPortNotificationGroupV8v9 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 97)
)
tmnxPortNotificationGroupV8v9.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxResvCbsPoolThreshGreen"),
        ("TIMETRA-PORT-MIB", "tmnxResvCbsPoolThreshAmber"),
        ("TIMETRA-PORT-MIB", "tmnxResvCbsPoolThreshRed"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationGroupV8v9.setStatus(
        "current"
    )

tmnxPortNotificationV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 2, 102)
)
tmnxPortNotificationV9v0Group.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxEqPortEtherCrcAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherCrcAlarmClear"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherInternalAlarm"),
        ("TIMETRA-PORT-MIB", "tmnxEqPortEtherInternalAlarmClr"))
)
if mibBuilder.loadTexts:
    tmnxPortNotificationV9v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxPortComp7750V4v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxPortComp7750V4v0.setStatus(
        "obsolete"
    )

tmnxPortComp7750V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxPortComp7750V5v0.setStatus(
        "obsolete"
    )

tmnxPortComp7750V6v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxPortComp7750V6v0.setStatus(
        "obsolete"
    )

tmnxPortComp7750V6v1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxPortComp7750V6v1.setStatus(
        "obsolete"
    )

tmnxPortComp7750V7v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxPortComp7750V7v0.setStatus(
        "obsolete"
    )

tmnxPortComp7750V8v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    tmnxPortComp7750V8v0.setStatus(
        "obsolete"
    )

tmnxPortComp7750V9v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxPortComp7750V9v0.setStatus(
        "obsolete"
    )

tmnxPortComp7450V4v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxPortComp7450V4v0.setStatus(
        "obsolete"
    )

tmnxPortComp7450V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tmnxPortComp7450V5v0.setStatus(
        "obsolete"
    )

tmnxPortComp7450V6v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    tmnxPortComp7450V6v0.setStatus(
        "obsolete"
    )

tmnxPortComp7450V6v1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    tmnxPortComp7450V6v1.setStatus(
        "obsolete"
    )

tmnxPortComp7450V7v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    tmnxPortComp7450V7v0.setStatus(
        "obsolete"
    )

tmnxPortComp7450V8v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 4, 7)
)
if mibBuilder.loadTexts:
    tmnxPortComp7450V8v0.setStatus(
        "obsolete"
    )

tmnxPortComp7710V3v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxPortComp7710V3v0.setStatus(
        "obsolete"
    )

tmnxPortComp7710V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxPortComp7710V5v0.setStatus(
        "obsolete"
    )

tmnxPortComp7710V6v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    tmnxPortComp7710V6v0.setStatus(
        "obsolete"
    )

tmnxPortComp7710V6v1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    tmnxPortComp7710V6v1.setStatus(
        "obsolete"
    )

tmnxPortComp7710V7v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    tmnxPortComp7710V7v0.setStatus(
        "obsolete"
    )

tmnxPortComp7710V8v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 5, 6)
)
if mibBuilder.loadTexts:
    tmnxPortComp7710V8v0.setStatus(
        "obsolete"
    )

tmnxPortComplianceV9v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxPortComplianceV9v0.setStatus(
        "obsolete"
    )

tmnxPortComplianceV10v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxPortComplianceV10v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PORT-MIB",
    **{"TmnxPortOperStatus": TmnxPortOperStatus,
       "TmnxPortEtherReportValue": TmnxPortEtherReportValue,
       "TmnxPortEtherReportStatus": TmnxPortEtherReportStatus,
       "TmnxPortEtherCrcMonReportValue": TmnxPortEtherCrcMonReportValue,
       "TmnxPortEtherCrcMonReportStatus": TmnxPortEtherCrcMonReportStatus,
       "TmnxPortClass": TmnxPortClass,
       "TmnxPortConnectorType": TmnxPortConnectorType,
       "TmnxPortState": TmnxPortState,
       "TmnxPortType": TmnxPortType,
       "TmnxPortEncapType": TmnxPortEncapType,
       "TmnxDs0ChannelList": TmnxDs0ChannelList,
       "TmnxBundleID": TmnxBundleID,
       "TmnxDSXBertPattern": TmnxDSXBertPattern,
       "TmnxDSXBertOperStatus": TmnxDSXBertOperStatus,
       "TmnxDSXIdleCycleFlags": TmnxDSXIdleCycleFlags,
       "TmnxDSXIdleFillType": TmnxDSXIdleFillType,
       "TmnxDSXLoopback": TmnxDSXLoopback,
       "TmnxDSXReportAlarm": TmnxDSXReportAlarm,
       "TmnxDSXClockSource": TmnxDSXClockSource,
       "TmnxDSXClockSyncState": TmnxDSXClockSyncState,
       "TmnxDS1Loopback": TmnxDS1Loopback,
       "TmnxDS3Loopback": TmnxDS3Loopback,
       "TmnxImaGrpState": TmnxImaGrpState,
       "TmnxImaGrpFailState": TmnxImaGrpFailState,
       "TmnxImaLnkState": TmnxImaLnkState,
       "TmnxImaLnkFailState": TmnxImaLnkFailState,
       "TmnxImaTestState": TmnxImaTestState,
       "TmnxImaGrpClockModes": TmnxImaGrpClockModes,
       "TmnxImaGrpVersion": TmnxImaGrpVersion,
       "TmnxMcMlpppClassIndex": TmnxMcMlpppClassIndex,
       "TmnxMlpppEndpointIdClass": TmnxMlpppEndpointIdClass,
       "TmnxMlfrLinkDownReason": TmnxMlfrLinkDownReason,
       "TmnxWaveTrackerAlarm": TmnxWaveTrackerAlarm,
       "TmnxOpticalAmpAlarm": TmnxOpticalAmpAlarm,
       "TmnxOpticalTdcmAlarm": TmnxOpticalTdcmAlarm,
       "TmnxOpticalTdcmCtrlMode": TmnxOpticalTdcmCtrlMode,
       "TmnxOpticalAmpCtrlState": TmnxOpticalAmpCtrlState,
       "TmnxOpticalTdcmCtrlState": TmnxOpticalTdcmCtrlState,
       "TmnxOpticalDwdmChannel": TmnxOpticalDwdmChannel,
       "TmnxDigitalDiagnosticFailureBits": TmnxDigitalDiagnosticFailureBits,
       "tmnxPortMIBModule": tmnxPortMIBModule,
       "tmnxPortConformance": tmnxPortConformance,
       "tmnxPortCompliances": tmnxPortCompliances,
       "tmnxPortComp7750": tmnxPortComp7750,
       "tmnxPortComp7750V4v0": tmnxPortComp7750V4v0,
       "tmnxPortComp7750V5v0": tmnxPortComp7750V5v0,
       "tmnxPortComp7750V6v0": tmnxPortComp7750V6v0,
       "tmnxPortComp7750V6v1": tmnxPortComp7750V6v1,
       "tmnxPortComp7750V7v0": tmnxPortComp7750V7v0,
       "tmnxPortComp7750V8v0": tmnxPortComp7750V8v0,
       "tmnxPortComp7750V9v0": tmnxPortComp7750V9v0,
       "tmnxPortComp7450": tmnxPortComp7450,
       "tmnxPortComp7450V4v0": tmnxPortComp7450V4v0,
       "tmnxPortComp7450V5v0": tmnxPortComp7450V5v0,
       "tmnxPortComp7450V6v0": tmnxPortComp7450V6v0,
       "tmnxPortComp7450V6v1": tmnxPortComp7450V6v1,
       "tmnxPortComp7450V7v0": tmnxPortComp7450V7v0,
       "tmnxPortComp7450V8v0": tmnxPortComp7450V8v0,
       "tmnxPortComp7710": tmnxPortComp7710,
       "tmnxPortComp7710V3v0": tmnxPortComp7710V3v0,
       "tmnxPortComp7710V5v0": tmnxPortComp7710V5v0,
       "tmnxPortComp7710V6v0": tmnxPortComp7710V6v0,
       "tmnxPortComp7710V6v1": tmnxPortComp7710V6v1,
       "tmnxPortComp7710V7v0": tmnxPortComp7710V7v0,
       "tmnxPortComp7710V8v0": tmnxPortComp7710V8v0,
       "tmnxPortComplianceV9v0": tmnxPortComplianceV9v0,
       "tmnxPortComplianceV10v0": tmnxPortComplianceV10v0,
       "tmnxPortGroups": tmnxPortGroups,
       "tmnxPortFRGroup": tmnxPortFRGroup,
       "tmnxQosAppObjsGroup": tmnxQosAppObjsGroup,
       "tmnxPortTestGroup": tmnxPortTestGroup,
       "tmnxPortObsoleteGroup": tmnxPortObsoleteGroup,
       "tmnxPortIngrMdaQosStatR2r1Group": tmnxPortIngrMdaQosStatR2r1Group,
       "tmnxPortStatsR2r1Group": tmnxPortStatsR2r1Group,
       "tmnxPortNotificationGroupR2r1": tmnxPortNotificationGroupR2r1,
       "tmnxPortNotifyObjsGroupR2r1": tmnxPortNotifyObjsGroupR2r1,
       "tmnxPortNotifyObsoleteGroup": tmnxPortNotifyObsoleteGroup,
       "tmnxPortSonetV3v0Group": tmnxPortSonetV3v0Group,
       "tmnxPortTDMV3v0Group": tmnxPortTDMV3v0Group,
       "tmnxPortATMV3v0Group": tmnxPortATMV3v0Group,
       "tmnxScalarPortV3v0Group": tmnxScalarPortV3v0Group,
       "tmnxPortV3v0Group": tmnxPortV3v0Group,
       "tmnxCiscoHDLCGroup": tmnxCiscoHDLCGroup,
       "tmnxMlBundleV3v0Group": tmnxMlBundleV3v0Group,
       "tmnxObsoleteGroupV3v0": tmnxObsoleteGroupV3v0,
       "tmnxPortEthernetV3v0Group": tmnxPortEthernetV3v0Group,
       "tmnxPortTDMGroupV4v0": tmnxPortTDMGroupV4v0,
       "tmnxPortATMGroupV4v0": tmnxPortATMGroupV4v0,
       "tmnxMlBundleGroupV4v0": tmnxMlBundleGroupV4v0,
       "tmnxMlImaBundleGroup": tmnxMlImaBundleGroup,
       "tmnx7710PortTDMGroupV3v0": tmnx7710PortTDMGroupV3v0,
       "tmnxPortGroupV4v0": tmnxPortGroupV4v0,
       "tmnxObsoleteGroupV5v0": tmnxObsoleteGroupV5v0,
       "tmnxPortSchedV5v0Group": tmnxPortSchedV5v0Group,
       "tmnxPortEthernetV5v0Group": tmnxPortEthernetV5v0Group,
       "tmnxPortGroupV5v0": tmnxPortGroupV5v0,
       "tmnxMlBundleGroupV5v0": tmnxMlBundleGroupV5v0,
       "tmnxPortNotificationGroupV5v0": tmnxPortNotificationGroupV5v0,
       "tmnxPortTDMGroupV5v0": tmnxPortTDMGroupV5v0,
       "tmnx7710PortTDMGroupV5v0": tmnx7710PortTDMGroupV5v0,
       "tmnxPortCemGroupV6v0": tmnxPortCemGroupV6v0,
       "tmnxMcMlpppBundleGroup": tmnxMcMlpppBundleGroup,
       "tmnxPortNotificationGroupV6v0": tmnxPortNotificationGroupV6v0,
       "tmnxPortEthernetV6v0Group": tmnxPortEthernetV6v0Group,
       "tmnxMlBundleGroupV6v0": tmnxMlBundleGroupV6v0,
       "tmnxMlpppBundleGroup": tmnxMlpppBundleGroup,
       "tmnxPortNotificationGroupV3v0": tmnxPortNotificationGroupV3v0,
       "tmnxHsmdaGroupV6v0": tmnxHsmdaGroupV6v0,
       "tmnxPortTDMGroupV6v0": tmnxPortTDMGroupV6v0,
       "tmnxDigitalDiagMonitorGroup": tmnxDigitalDiagMonitorGroup,
       "tmnxPortGroupV6v0": tmnxPortGroupV6v0,
       "tmnxNamedPoolGroupV6v0": tmnxNamedPoolGroupV6v0,
       "tmnxPortEthernetV6v1Group": tmnxPortEthernetV6v1Group,
       "tmnxPortNotifyObjsGroupV6v0": tmnxPortNotifyObjsGroupV6v0,
       "tmnxPortQV7v0Group": tmnxPortQV7v0Group,
       "tmnxMcMfrBundleGroup": tmnxMcMfrBundleGroup,
       "tmnxFrIntfGroup": tmnxFrIntfGroup,
       "tmnxFrf12IntfGroup": tmnxFrf12IntfGroup,
       "tmnxPortQStatV7v0Group": tmnxPortQStatV7v0Group,
       "tmnxPortEthernetV7v0Group": tmnxPortEthernetV7v0Group,
       "tmnxPortGroupV7v0": tmnxPortGroupV7v0,
       "tmnxPortNotifyObjsGroupV7v0": tmnxPortNotifyObjsGroupV7v0,
       "tmnxPortNotificationGroupV7v0": tmnxPortNotificationGroupV7v0,
       "tmnxPortEtherObsoleteV7v0Group": tmnxPortEtherObsoleteV7v0Group,
       "tmnxPortTDMGroupV7v0": tmnxPortTDMGroupV7v0,
       "tmnxPortTDME1GroupV6v1": tmnxPortTDME1GroupV6v1,
       "tmnxPortNotifyObjsGroupV8v0": tmnxPortNotifyObjsGroupV8v0,
       "tmnxWaveTrackerGroup": tmnxWaveTrackerGroup,
       "tmnxPortGroupV8v0": tmnxPortGroupV8v0,
       "tmnxPortDwdmGroup": tmnxPortDwdmGroup,
       "tmnxPortATMGroupV7v0": tmnxPortATMGroupV7v0,
       "tmnxPortCEMGroupV8v0": tmnxPortCEMGroupV8v0,
       "tmnxPortQV8v0Group": tmnxPortQV8v0Group,
       "tmnxPortQObsoleteV8v0Group": tmnxPortQObsoleteV8v0Group,
       "tmnxPortNotificationGroupV8v0": tmnxPortNotificationGroupV8v0,
       "tmnxPortSchedStatsGroup": tmnxPortSchedStatsGroup,
       "tmnxPortVPortGroup": tmnxPortVPortGroup,
       "tmnxMlpppBundleGroupV7v0": tmnxMlpppBundleGroupV7v0,
       "tmnxOpticalPortGroup": tmnxOpticalPortGroup,
       "tmnxPortATMGroupV9v0": tmnxPortATMGroupV9v0,
       "tmnxPortVPortV9v0Group": tmnxPortVPortV9v0Group,
       "tmnxPortEgrExpShaperV9v0Group": tmnxPortEgrExpShaperV9v0Group,
       "tmnxPortNotificationGroupV9v4": tmnxPortNotificationGroupV9v4,
       "tmnxPortObjAppV9v0Group": tmnxPortObjAppV9v0Group,
       "tmnxOpticalPortGroupV9v0": tmnxOpticalPortGroupV9v0,
       "tmnxPortNotifyObjsGroupV8v9": tmnxPortNotifyObjsGroupV8v9,
       "tmnxPortNotificationGroupV8v9": tmnxPortNotificationGroupV8v9,
       "tmnxPortEgrVPortStatsV9v0Group": tmnxPortEgrVPortStatsV9v0Group,
       "tmnxPortNotifyObjsV9v0Group": tmnxPortNotifyObjsV9v0Group,
       "tmnxPortEtherV9v0Group": tmnxPortEtherV9v0Group,
       "tmnxPortNotificationV9v0Group": tmnxPortNotificationV9v0Group,
       "tmnxPortV9v0Group": tmnxPortV9v0Group,
       "tmnxPortNetEgrV10v0Group": tmnxPortNetEgrV10v0Group,
       "tmnxDDMLaneGroupV10v0": tmnxDDMLaneGroupV10v0,
       "tmnxPortNotifyObjsGroupV10v0": tmnxPortNotifyObjsGroupV10v0,
       "tmnxPortPlcyGroup": tmnxPortPlcyGroup,
       "tmnxPortLoadBalGroupV10v0": tmnxPortLoadBalGroupV10v0,
       "tmnxPortEthernetV10v0Group": tmnxPortEthernetV10v0Group,
       "tmnxHsmdaGroupV10v0": tmnxHsmdaGroupV10v0,
       "tmnxPortObsoletedV10v0Group": tmnxPortObsoletedV10v0Group,
       "tmnxPwPortV10v0Group": tmnxPwPortV10v0Group,
       "tmnxPortObjs": tmnxPortObjs,
       "tmnxPortTableLastChange": tmnxPortTableLastChange,
       "tmnxPortTable": tmnxPortTable,
       "tmnxPortEntry": tmnxPortEntry,
       "tmnxPortPortID": tmnxPortPortID,
       "tmnxPortLastChangeTime": tmnxPortLastChangeTime,
       "tmnxPortType": tmnxPortType,
       "tmnxPortClass": tmnxPortClass,
       "tmnxPortDescription": tmnxPortDescription,
       "tmnxPortName": tmnxPortName,
       "tmnxPortAlias": tmnxPortAlias,
       "tmnxPortUserAssignedMac": tmnxPortUserAssignedMac,
       "tmnxPortMacAddress": tmnxPortMacAddress,
       "tmnxPortHwMacAddress": tmnxPortHwMacAddress,
       "tmnxPortMode": tmnxPortMode,
       "tmnxPortEncapType": tmnxPortEncapType,
       "tmnxPortLagId": tmnxPortLagId,
       "tmnxPortHoldTimeUp": tmnxPortHoldTimeUp,
       "tmnxPortHoldTimeDown": tmnxPortHoldTimeDown,
       "tmnxPortUpProtocols": tmnxPortUpProtocols,
       "tmnxPortConnectorType": tmnxPortConnectorType,
       "tmnxPortTransceiverType": tmnxPortTransceiverType,
       "tmnxPortTransceiverCode": tmnxPortTransceiverCode,
       "tmnxPortTransceiverLaserWaveLen": tmnxPortTransceiverLaserWaveLen,
       "tmnxPortTransceiverDiagCapable": tmnxPortTransceiverDiagCapable,
       "tmnxPortTransceiverModelNumber": tmnxPortTransceiverModelNumber,
       "tmnxPortSFPConnectorCode": tmnxPortSFPConnectorCode,
       "tmnxPortSFPVendorOUI": tmnxPortSFPVendorOUI,
       "tmnxPortSFPVendorManufactureDate": tmnxPortSFPVendorManufactureDate,
       "tmnxPortSFPMedia": tmnxPortSFPMedia,
       "tmnxPortSFPEquipped": tmnxPortSFPEquipped,
       "tmnxPortEquipped": tmnxPortEquipped,
       "tmnxPortLinkStatus": tmnxPortLinkStatus,
       "tmnxPortAdminStatus": tmnxPortAdminStatus,
       "tmnxPortOperStatus": tmnxPortOperStatus,
       "tmnxPortState": tmnxPortState,
       "tmnxPortPrevState": tmnxPortPrevState,
       "tmnxPortNumAlarms": tmnxPortNumAlarms,
       "tmnxPortAlarmState": tmnxPortAlarmState,
       "tmnxPortLastAlarmEvent": tmnxPortLastAlarmEvent,
       "tmnxPortClearAlarms": tmnxPortClearAlarms,
       "tmnxPortSFPVendorSerialNum": tmnxPortSFPVendorSerialNum,
       "tmnxPortSFPVendorPartNum": tmnxPortSFPVendorPartNum,
       "tmnxPortLastStateChanged": tmnxPortLastStateChanged,
       "tmnxPortNumChannels": tmnxPortNumChannels,
       "tmnxPortNetworkEgrQueues": tmnxPortNetworkEgrQueues,
       "tmnxPortBundleNumber": tmnxPortBundleNumber,
       "tmnxPortIsLeaf": tmnxPortIsLeaf,
       "tmnxPortChanType": tmnxPortChanType,
       "tmnxPortParentPortID": tmnxPortParentPortID,
       "tmnxPortOpticalCompliance": tmnxPortOpticalCompliance,
       "tmnxPortLoadBalanceAlgorithm": tmnxPortLoadBalanceAlgorithm,
       "tmnxPortEgrPortSchedPlcy": tmnxPortEgrPortSchedPlcy,
       "tmnxPortLastClearedTime": tmnxPortLastClearedTime,
       "tmnxPortEgrHsmdaSchedPlcy": tmnxPortEgrHsmdaSchedPlcy,
       "tmnxPortIngNamedPoolPlcy": tmnxPortIngNamedPoolPlcy,
       "tmnxPortEgrNamedPoolPlcy": tmnxPortEgrNamedPoolPlcy,
       "tmnxPortIngPoolPercentRate": tmnxPortIngPoolPercentRate,
       "tmnxPortEgrPoolPercentRate": tmnxPortEgrPoolPercentRate,
       "tmnxPortDDMEventSuppression": tmnxPortDDMEventSuppression,
       "tmnxPortSFPStatus": tmnxPortSFPStatus,
       "tmnxPortReasonDownFlags": tmnxPortReasonDownFlags,
       "tmnxPortSSMRxQualityLevel": tmnxPortSSMRxQualityLevel,
       "tmnxPortDwdmLaserChannel": tmnxPortDwdmLaserChannel,
       "tmnxPortOtuCapable": tmnxPortOtuCapable,
       "tmnxPortWaveTrackerCapable": tmnxPortWaveTrackerCapable,
       "tmnxPortHybridIngAccessWeight": tmnxPortHybridIngAccessWeight,
       "tmnxPortHybridIngNetworkWeight": tmnxPortHybridIngNetworkWeight,
       "tmnxPortHybridEgrAccessWeight": tmnxPortHybridEgrAccessWeight,
       "tmnxPortHybridEgrNetworkWeight": tmnxPortHybridEgrNetworkWeight,
       "tmnxPortDwdmRxDtvAdjustEnable": tmnxPortDwdmRxDtvAdjustEnable,
       "tmnxPortDwdmRxDtvDacPercent": tmnxPortDwdmRxDtvDacPercent,
       "tmnxPortInterfaceGroupHandlerIdx": tmnxPortInterfaceGroupHandlerIdx,
       "tmnxPortHoldTimeUnits": tmnxPortHoldTimeUnits,
       "tmnxPortLinkLengthInfo": tmnxPortLinkLengthInfo,
       "tmnxPortSFPNumLanes": tmnxPortSFPNumLanes,
       "tmnxPortPhysStateChangeCount": tmnxPortPhysStateChangeCount,
       "tmnxPortTestTable": tmnxPortTestTable,
       "tmnxPortTestEntry": tmnxPortTestEntry,
       "tmnxPortTestState": tmnxPortTestState,
       "tmnxPortTestMode": tmnxPortTestMode,
       "tmnxPortTestParameter": tmnxPortTestParameter,
       "tmnxPortTestLastResult": tmnxPortTestLastResult,
       "tmnxPortTestStartTime": tmnxPortTestStartTime,
       "tmnxPortTestEndTime": tmnxPortTestEndTime,
       "tmnxPortTestDuration": tmnxPortTestDuration,
       "tmnxPortTestAction": tmnxPortTestAction,
       "tmnxPortEtherTable": tmnxPortEtherTable,
       "tmnxPortEtherEntry": tmnxPortEtherEntry,
       "tmnxPortEtherMTU": tmnxPortEtherMTU,
       "tmnxPortEtherDuplex": tmnxPortEtherDuplex,
       "tmnxPortEtherSpeed": tmnxPortEtherSpeed,
       "tmnxPortEtherAutoNegotiate": tmnxPortEtherAutoNegotiate,
       "tmnxPortEtherOperDuplex": tmnxPortEtherOperDuplex,
       "tmnxPortEtherOperSpeed": tmnxPortEtherOperSpeed,
       "tmnxPortEtherAcctPolicyId": tmnxPortEtherAcctPolicyId,
       "tmnxPortEtherCollectStats": tmnxPortEtherCollectStats,
       "tmnxPortEtherMDIMDIX": tmnxPortEtherMDIMDIX,
       "tmnxPortEtherXGigMode": tmnxPortEtherXGigMode,
       "tmnxPortEtherEgressRate": tmnxPortEtherEgressRate,
       "tmnxPortEtherDot1qEtype": tmnxPortEtherDot1qEtype,
       "tmnxPortEtherQinqEtype": tmnxPortEtherQinqEtype,
       "tmnxPortEtherIngressRate": tmnxPortEtherIngressRate,
       "tmnxPortEtherReportAlarm": tmnxPortEtherReportAlarm,
       "tmnxPortEtherReportAlarmStatus": tmnxPortEtherReportAlarmStatus,
       "tmnxPortEtherPkts1519toMax": tmnxPortEtherPkts1519toMax,
       "tmnxPortEtherHCOverPkts1519toMax": tmnxPortEtherHCOverPkts1519toMax,
       "tmnxPortEtherHCPkts1519toMax": tmnxPortEtherHCPkts1519toMax,
       "tmnxPortEtherLacpTunnel": tmnxPortEtherLacpTunnel,
       "tmnxPortEtherDownWhenLoopedEnabled": tmnxPortEtherDownWhenLoopedEnabled,
       "tmnxPortEtherDownWhenLoopedKeepAlive": tmnxPortEtherDownWhenLoopedKeepAlive,
       "tmnxPortEtherDownWhenLoopedRetry": tmnxPortEtherDownWhenLoopedRetry,
       "tmnxPortEtherDownWhenLoopedState": tmnxPortEtherDownWhenLoopedState,
       "tmnxPortEtherPBBEtype": tmnxPortEtherPBBEtype,
       "tmnxPortEtherReasonDownFlags": tmnxPortEtherReasonDownFlags,
       "tmnxPortEtherSingleFiber": tmnxPortEtherSingleFiber,
       "tmnxPortEtherSSM": tmnxPortEtherSSM,
       "tmnxPortEtherDWLUseBroadcastAddr": tmnxPortEtherDWLUseBroadcastAddr,
       "tmnxPortEtherSSMCodeType": tmnxPortEtherSSMCodeType,
       "tmnxPortEtherSSMTxDus": tmnxPortEtherSSMTxDus,
       "tmnxPortEtherSSMRxEsmc": tmnxPortEtherSSMRxEsmc,
       "tmnxPortEtherSSMTxQualityLevel": tmnxPortEtherSSMTxQualityLevel,
       "tmnxPortEtherCrcMonSdThreshold": tmnxPortEtherCrcMonSdThreshold,
       "tmnxPortEtherCrcMonSdTMultiplier": tmnxPortEtherCrcMonSdTMultiplier,
       "tmnxPortEtherCrcMonSfThreshold": tmnxPortEtherCrcMonSfThreshold,
       "tmnxPortEtherCrcMonSfTMultiplier": tmnxPortEtherCrcMonSfTMultiplier,
       "tmnxPortEtherCrcMonWindowSize": tmnxPortEtherCrcMonWindowSize,
       "tmnxPortEtherCrcAlarmReason": tmnxPortEtherCrcAlarmReason,
       "tmnxPortEtherDownOnInternalError": tmnxPortEtherDownOnInternalError,
       "tmnxPortEtherMinFrameLength": tmnxPortEtherMinFrameLength,
       "tmnxSonetTable": tmnxSonetTable,
       "tmnxSonetEntry": tmnxSonetEntry,
       "tmnxSonetSpeed": tmnxSonetSpeed,
       "tmnxSonetClockSource": tmnxSonetClockSource,
       "tmnxSonetFraming": tmnxSonetFraming,
       "tmnxSonetReportAlarm": tmnxSonetReportAlarm,
       "tmnxSonetBerSdThreshold": tmnxSonetBerSdThreshold,
       "tmnxSonetBerSfThreshold": tmnxSonetBerSfThreshold,
       "tmnxSonetAps": tmnxSonetAps,
       "tmnxSonetApsAdminStatus": tmnxSonetApsAdminStatus,
       "tmnxSonetApsOperStatus": tmnxSonetApsOperStatus,
       "tmnxSonetApsAuthKey": tmnxSonetApsAuthKey,
       "tmnxSonetApsNeighborAddr": tmnxSonetApsNeighborAddr,
       "tmnxSonetApsAdvertiseInterval": tmnxSonetApsAdvertiseInterval,
       "tmnxSonetApsAdvertiseTimeLeft": tmnxSonetApsAdvertiseTimeLeft,
       "tmnxSonetApsHoldTime": tmnxSonetApsHoldTime,
       "tmnxSonetApsHoldTimeLeft": tmnxSonetApsHoldTimeLeft,
       "tmnxSonetLoopback": tmnxSonetLoopback,
       "tmnxSonetReportAlarmStatus": tmnxSonetReportAlarmStatus,
       "tmnxSonetSectionTraceMode": tmnxSonetSectionTraceMode,
       "tmnxSonetJ0String": tmnxSonetJ0String,
       "tmnxSonetMonS1Byte": tmnxSonetMonS1Byte,
       "tmnxSonetMonJ0String": tmnxSonetMonJ0String,
       "tmnxSonetMonK1Byte": tmnxSonetMonK1Byte,
       "tmnxSonetMonK2Byte": tmnxSonetMonK2Byte,
       "tmnxSonetSingleFiber": tmnxSonetSingleFiber,
       "tmnxSonetHoldTimeUp": tmnxSonetHoldTimeUp,
       "tmnxSonetHoldTimeDown": tmnxSonetHoldTimeDown,
       "tmnxSonetSuppressLoOrderAlarm": tmnxSonetSuppressLoOrderAlarm,
       "tmnxSonetTxDus": tmnxSonetTxDus,
       "tmnxSonetTxS1Byte": tmnxSonetTxS1Byte,
       "tmnxSonetPathTable": tmnxSonetPathTable,
       "tmnxSonetPathEntry": tmnxSonetPathEntry,
       "tmnxSonetPathRowStatus": tmnxSonetPathRowStatus,
       "tmnxSonetPathLastChangeTime": tmnxSonetPathLastChangeTime,
       "tmnxSonetPathMTU": tmnxSonetPathMTU,
       "tmnxSonetPathScramble": tmnxSonetPathScramble,
       "tmnxSonetPathC2Byte": tmnxSonetPathC2Byte,
       "tmnxSonetPathJ1String": tmnxSonetPathJ1String,
       "tmnxSonetPathCRC": tmnxSonetPathCRC,
       "tmnxSonetPathOperMTU": tmnxSonetPathOperMTU,
       "tmnxSonetPathOperMRU": tmnxSonetPathOperMRU,
       "tmnxSonetPathReportAlarm": tmnxSonetPathReportAlarm,
       "tmnxSonetPathAcctPolicyId": tmnxSonetPathAcctPolicyId,
       "tmnxSonetPathCollectStats": tmnxSonetPathCollectStats,
       "tmnxSonetPathReportAlarmStatus": tmnxSonetPathReportAlarmStatus,
       "tmnxSonetPathMonC2Byte": tmnxSonetPathMonC2Byte,
       "tmnxSonetPathMonJ1String": tmnxSonetPathMonJ1String,
       "tmnxSonetPathType": tmnxSonetPathType,
       "tmnxSonetPathChildType": tmnxSonetPathChildType,
       "tmnxPortTypeTable": tmnxPortTypeTable,
       "tmnxPortTypeEntry": tmnxPortTypeEntry,
       "tmnxPortTypeIndex": tmnxPortTypeIndex,
       "tmnxPortTypeName": tmnxPortTypeName,
       "tmnxPortTypeDescription": tmnxPortTypeDescription,
       "tmnxPortTypeStatus": tmnxPortTypeStatus,
       "tmnxPortConnectTypeTable": tmnxPortConnectTypeTable,
       "tmnxPortConnectTypeEntry": tmnxPortConnectTypeEntry,
       "tmnxPortConnectTypeIndex": tmnxPortConnectTypeIndex,
       "tmnxPortConnectTypeName": tmnxPortConnectTypeName,
       "tmnxPortConnectTypeDescription": tmnxPortConnectTypeDescription,
       "tmnxPortConnectTypeStatus": tmnxPortConnectTypeStatus,
       "tmnxPortFCStatsTable": tmnxPortFCStatsTable,
       "tmnxPortFCStatsEntry": tmnxPortFCStatsEntry,
       "tmnxPortFCStatsIndex": tmnxPortFCStatsIndex,
       "tmnxPortFCStatsIngFwdInProfPkts": tmnxPortFCStatsIngFwdInProfPkts,
       "tmnxPortFCStatsIngFwdOutProfPkts": tmnxPortFCStatsIngFwdOutProfPkts,
       "tmnxPortFCStatsIngFwdInProfOcts": tmnxPortFCStatsIngFwdInProfOcts,
       "tmnxPortFCStatsIngFwdOutProfOcts": tmnxPortFCStatsIngFwdOutProfOcts,
       "tmnxPortFCStatsIngDroInProfPkts": tmnxPortFCStatsIngDroInProfPkts,
       "tmnxPortFCStatsIngDroOutProfPkts": tmnxPortFCStatsIngDroOutProfPkts,
       "tmnxPortFCStatsIngDroInProfOcts": tmnxPortFCStatsIngDroInProfOcts,
       "tmnxPortFCStatsIngDroOutProfOcts": tmnxPortFCStatsIngDroOutProfOcts,
       "tmnxPortFCStatsEgrFwdInProfPkts": tmnxPortFCStatsEgrFwdInProfPkts,
       "tmnxPortFCStatsEgrFwdOutProfPkts": tmnxPortFCStatsEgrFwdOutProfPkts,
       "tmnxPortFCStatsEgrFwdInProfOcts": tmnxPortFCStatsEgrFwdInProfOcts,
       "tmnxPortFCStatsEgrFwdOutProfOcts": tmnxPortFCStatsEgrFwdOutProfOcts,
       "tmnxPortFCStatsEgrDroInProfPkts": tmnxPortFCStatsEgrDroInProfPkts,
       "tmnxPortFCStatsEgrDroOutProfPkts": tmnxPortFCStatsEgrDroOutProfPkts,
       "tmnxPortFCStatsEgrDroInProfOcts": tmnxPortFCStatsEgrDroInProfOcts,
       "tmnxPortFCStatsEgrDroOutProfOcts": tmnxPortFCStatsEgrDroOutProfOcts,
       "tmnxDS3Table": tmnxDS3Table,
       "tmnxDS3Entry": tmnxDS3Entry,
       "tmnxDS3Buildout": tmnxDS3Buildout,
       "tmnxDS3LastChangeTime": tmnxDS3LastChangeTime,
       "tmnxDS3Type": tmnxDS3Type,
       "tmnxDS3ChannelTable": tmnxDS3ChannelTable,
       "tmnxDS3ChannelEntry": tmnxDS3ChannelEntry,
       "tmnxDS3ChannelRowStatus": tmnxDS3ChannelRowStatus,
       "tmnxDS3ChannelType": tmnxDS3ChannelType,
       "tmnxDS3ChannelFraming": tmnxDS3ChannelFraming,
       "tmnxDS3ChannelClockSource": tmnxDS3ChannelClockSource,
       "tmnxDS3ChannelChannelized": tmnxDS3ChannelChannelized,
       "tmnxDS3ChannelSubrateCSUMode": tmnxDS3ChannelSubrateCSUMode,
       "tmnxDS3ChannelSubrate": tmnxDS3ChannelSubrate,
       "tmnxDS3ChannelIdleCycleFlags": tmnxDS3ChannelIdleCycleFlags,
       "tmnxDS3ChannelLoopback": tmnxDS3ChannelLoopback,
       "tmnxDS3ChannelBitErrorInsertionRate": tmnxDS3ChannelBitErrorInsertionRate,
       "tmnxDS3ChannelBERTPattern": tmnxDS3ChannelBERTPattern,
       "tmnxDS3ChannelBERTDuration": tmnxDS3ChannelBERTDuration,
       "tmnxDS3ChannelMDLEicString": tmnxDS3ChannelMDLEicString,
       "tmnxDS3ChannelMDLLicString": tmnxDS3ChannelMDLLicString,
       "tmnxDS3ChannelMDLFicString": tmnxDS3ChannelMDLFicString,
       "tmnxDS3ChannelMDLUnitString": tmnxDS3ChannelMDLUnitString,
       "tmnxDS3ChannelMDLPfiString": tmnxDS3ChannelMDLPfiString,
       "tmnxDS3ChannelMDLPortString": tmnxDS3ChannelMDLPortString,
       "tmnxDS3ChannelMDLGenString": tmnxDS3ChannelMDLGenString,
       "tmnxDS3ChannelMDLMessageType": tmnxDS3ChannelMDLMessageType,
       "tmnxDS3ChannelFEACLoopRespond": tmnxDS3ChannelFEACLoopRespond,
       "tmnxDS3ChannelCRC": tmnxDS3ChannelCRC,
       "tmnxDS3ChannelMTU": tmnxDS3ChannelMTU,
       "tmnxDS3ChannelOperMTU": tmnxDS3ChannelOperMTU,
       "tmnxDS3ChannelReportAlarm": tmnxDS3ChannelReportAlarm,
       "tmnxDS3ChannelReportAlarmStatus": tmnxDS3ChannelReportAlarmStatus,
       "tmnxDS3ChannelLastChangeTime": tmnxDS3ChannelLastChangeTime,
       "tmnxDS3ChannelInFEACLoop": tmnxDS3ChannelInFEACLoop,
       "tmnxDS3ChannelMDLMonPortString": tmnxDS3ChannelMDLMonPortString,
       "tmnxDS3ChannelMDLMonGenString": tmnxDS3ChannelMDLMonGenString,
       "tmnxDS3ChannelBERTOperStatus": tmnxDS3ChannelBERTOperStatus,
       "tmnxDS3ChannelBERTSynched": tmnxDS3ChannelBERTSynched,
       "tmnxDS3ChannelBERTErrors": tmnxDS3ChannelBERTErrors,
       "tmnxDS3ChannelBERTTotalBits": tmnxDS3ChannelBERTTotalBits,
       "tmnxDS3ChannelScramble": tmnxDS3ChannelScramble,
       "tmnxDS3ChannelAcctPolicyId": tmnxDS3ChannelAcctPolicyId,
       "tmnxDS3ChannelCollectStats": tmnxDS3ChannelCollectStats,
       "tmnxDS3ChannelClockSyncState": tmnxDS3ChannelClockSyncState,
       "tmnxDS3ChannelClockMasterPortId": tmnxDS3ChannelClockMasterPortId,
       "tmnxDS1Table": tmnxDS1Table,
       "tmnxDS1Entry": tmnxDS1Entry,
       "tmnxDS1RowStatus": tmnxDS1RowStatus,
       "tmnxDS1Type": tmnxDS1Type,
       "tmnxDS1Framing": tmnxDS1Framing,
       "tmnxDS1IdleCycleFlags": tmnxDS1IdleCycleFlags,
       "tmnxDS1Loopback": tmnxDS1Loopback,
       "tmnxDS1InvertData": tmnxDS1InvertData,
       "tmnxDS1BitErrorInsertionRate": tmnxDS1BitErrorInsertionRate,
       "tmnxDS1BERTPattern": tmnxDS1BERTPattern,
       "tmnxDS1BERTDuration": tmnxDS1BERTDuration,
       "tmnxDS1ReportAlarm": tmnxDS1ReportAlarm,
       "tmnxDS1ReportAlarmStatus": tmnxDS1ReportAlarmStatus,
       "tmnxDS1LastChangeTime": tmnxDS1LastChangeTime,
       "tmnxDS1ClockSource": tmnxDS1ClockSource,
       "tmnxDS1BERTOperStatus": tmnxDS1BERTOperStatus,
       "tmnxDS1BERTSynched": tmnxDS1BERTSynched,
       "tmnxDS1BERTErrors": tmnxDS1BERTErrors,
       "tmnxDS1BERTTotalBits": tmnxDS1BERTTotalBits,
       "tmnxDS1RemoteLoopRespond": tmnxDS1RemoteLoopRespond,
       "tmnxDS1InRemoteLoop": tmnxDS1InRemoteLoop,
       "tmnxDS1InsertSingleBitError": tmnxDS1InsertSingleBitError,
       "tmnxDS1SignalMode": tmnxDS1SignalMode,
       "tmnxDS1ClockSyncState": tmnxDS1ClockSyncState,
       "tmnxDS1ClockMasterPortId": tmnxDS1ClockMasterPortId,
       "tmnxDS1BerSdThreshold": tmnxDS1BerSdThreshold,
       "tmnxDS1BerSfThreshold": tmnxDS1BerSfThreshold,
       "tmnxDS1NationalUseBits": tmnxDS1NationalUseBits,
       "tmnxDS0ChanGroupTable": tmnxDS0ChanGroupTable,
       "tmnxDS0ChanGroupEntry": tmnxDS0ChanGroupEntry,
       "tmnxDS0ChanGroupRowStatus": tmnxDS0ChanGroupRowStatus,
       "tmnxDS0ChanGroupTimeSlots": tmnxDS0ChanGroupTimeSlots,
       "tmnxDS0ChanGroupSpeed": tmnxDS0ChanGroupSpeed,
       "tmnxDS0ChanGroupCRC": tmnxDS0ChanGroupCRC,
       "tmnxDS0ChanGroupMTU": tmnxDS0ChanGroupMTU,
       "tmnxDS0ChanGroupOperMTU": tmnxDS0ChanGroupOperMTU,
       "tmnxDS0ChanGroupLastChangeTime": tmnxDS0ChanGroupLastChangeTime,
       "tmnxDS0ChanGroupIdleCycleFlags": tmnxDS0ChanGroupIdleCycleFlags,
       "tmnxDS0ChanGroupScramble": tmnxDS0ChanGroupScramble,
       "tmnxDS0ChanGroupAcctPolicyId": tmnxDS0ChanGroupAcctPolicyId,
       "tmnxDS0ChanGroupCollectStats": tmnxDS0ChanGroupCollectStats,
       "tmnxDS0ChanGroupPayloadFillType": tmnxDS0ChanGroupPayloadFillType,
       "tmnxDS0ChanGroupPayloadPattern": tmnxDS0ChanGroupPayloadPattern,
       "tmnxDS0ChanGroupSignalFillType": tmnxDS0ChanGroupSignalFillType,
       "tmnxDS0ChanGroupSignalPattern": tmnxDS0ChanGroupSignalPattern,
       "tmnxDS0ChanGroupBerSfLinkDown": tmnxDS0ChanGroupBerSfLinkDown,
       "tmnxBundleTable": tmnxBundleTable,
       "tmnxBundleEntry": tmnxBundleEntry,
       "tmnxBundleBundleID": tmnxBundleBundleID,
       "tmnxBundleRowStatus": tmnxBundleRowStatus,
       "tmnxBundleType": tmnxBundleType,
       "tmnxBundleMinimumLinks": tmnxBundleMinimumLinks,
       "tmnxBundleNumLinks": tmnxBundleNumLinks,
       "tmnxBundleNumActiveLinks": tmnxBundleNumActiveLinks,
       "tmnxBundleMRRU": tmnxBundleMRRU,
       "tmnxBundleOperMRRU": tmnxBundleOperMRRU,
       "tmnxBundlePeerMRRU": tmnxBundlePeerMRRU,
       "tmnxBundleOperMTU": tmnxBundleOperMTU,
       "tmnxBundleRedDiffDelay": tmnxBundleRedDiffDelay,
       "tmnxBundleRedDiffDelayAction": tmnxBundleRedDiffDelayAction,
       "tmnxBundleYellowDiffDelay": tmnxBundleYellowDiffDelay,
       "tmnxBundleShortSequence": tmnxBundleShortSequence,
       "tmnxBundleLastChangeTime": tmnxBundleLastChangeTime,
       "tmnxBundleFragmentThreshold": tmnxBundleFragmentThreshold,
       "tmnxBundleUpTime": tmnxBundleUpTime,
       "tmnxBundleInputDiscards": tmnxBundleInputDiscards,
       "tmnxBundlePrimaryMemberPortID": tmnxBundlePrimaryMemberPortID,
       "tmnxBundleLFI": tmnxBundleLFI,
       "tmnxBundleProtectedType": tmnxBundleProtectedType,
       "tmnxBundleParentBundle": tmnxBundleParentBundle,
       "tmnxBundleMemberTable": tmnxBundleMemberTable,
       "tmnxBundleMemberEntry": tmnxBundleMemberEntry,
       "tmnxBundleMemberRowStatus": tmnxBundleMemberRowStatus,
       "tmnxBundleMemberActive": tmnxBundleMemberActive,
       "tmnxBundleMemberDownReason": tmnxBundleMemberDownReason,
       "tmnxBundleMemberUpTime": tmnxBundleMemberUpTime,
       "tmnxPortToChannelTable": tmnxPortToChannelTable,
       "tmnxPortToChannelEntry": tmnxPortToChannelEntry,
       "tmnxChannelIdxString": tmnxChannelIdxString,
       "tmnxChannelPortID": tmnxChannelPortID,
       "tmnxPortIngrMdaQosStatTable": tmnxPortIngrMdaQosStatTable,
       "tmnxPortIngrMdaQosStatEntry": tmnxPortIngrMdaQosStatEntry,
       "tmnxPortIngrMdaQos00StatDropPkts": tmnxPortIngrMdaQos00StatDropPkts,
       "tmnxPortIngrMdaQos00StatDropOcts": tmnxPortIngrMdaQos00StatDropOcts,
       "tmnxPortIngrMdaQos01StatDropPkts": tmnxPortIngrMdaQos01StatDropPkts,
       "tmnxPortIngrMdaQos01StatDropOcts": tmnxPortIngrMdaQos01StatDropOcts,
       "tmnxPortIngrMdaQos02StatDropPkts": tmnxPortIngrMdaQos02StatDropPkts,
       "tmnxPortIngrMdaQos02StatDropOcts": tmnxPortIngrMdaQos02StatDropOcts,
       "tmnxPortIngrMdaQos03StatDropPkts": tmnxPortIngrMdaQos03StatDropPkts,
       "tmnxPortIngrMdaQos03StatDropOcts": tmnxPortIngrMdaQos03StatDropOcts,
       "tmnxPortIngrMdaQos04StatDropPkts": tmnxPortIngrMdaQos04StatDropPkts,
       "tmnxPortIngrMdaQos04StatDropOcts": tmnxPortIngrMdaQos04StatDropOcts,
       "tmnxPortIngrMdaQos05StatDropPkts": tmnxPortIngrMdaQos05StatDropPkts,
       "tmnxPortIngrMdaQos05StatDropOcts": tmnxPortIngrMdaQos05StatDropOcts,
       "tmnxPortIngrMdaQos06StatDropPkts": tmnxPortIngrMdaQos06StatDropPkts,
       "tmnxPortIngrMdaQos06StatDropOcts": tmnxPortIngrMdaQos06StatDropOcts,
       "tmnxPortIngrMdaQos07StatDropPkts": tmnxPortIngrMdaQos07StatDropPkts,
       "tmnxPortIngrMdaQos07StatDropOcts": tmnxPortIngrMdaQos07StatDropOcts,
       "tmnxPortIngrMdaQos08StatDropPkts": tmnxPortIngrMdaQos08StatDropPkts,
       "tmnxPortIngrMdaQos08StatDropOcts": tmnxPortIngrMdaQos08StatDropOcts,
       "tmnxPortIngrMdaQos09StatDropPkts": tmnxPortIngrMdaQos09StatDropPkts,
       "tmnxPortIngrMdaQos09StatDropOcts": tmnxPortIngrMdaQos09StatDropOcts,
       "tmnxPortIngrMdaQos10StatDropPkts": tmnxPortIngrMdaQos10StatDropPkts,
       "tmnxPortIngrMdaQos10StatDropOcts": tmnxPortIngrMdaQos10StatDropOcts,
       "tmnxPortIngrMdaQos11StatDropPkts": tmnxPortIngrMdaQos11StatDropPkts,
       "tmnxPortIngrMdaQos11StatDropOcts": tmnxPortIngrMdaQos11StatDropOcts,
       "tmnxPortIngrMdaQos12StatDropPkts": tmnxPortIngrMdaQos12StatDropPkts,
       "tmnxPortIngrMdaQos12StatDropOcts": tmnxPortIngrMdaQos12StatDropOcts,
       "tmnxPortIngrMdaQos13StatDropPkts": tmnxPortIngrMdaQos13StatDropPkts,
       "tmnxPortIngrMdaQos13StatDropOcts": tmnxPortIngrMdaQos13StatDropOcts,
       "tmnxPortIngrMdaQos14StatDropPkts": tmnxPortIngrMdaQos14StatDropPkts,
       "tmnxPortIngrMdaQos14StatDropOcts": tmnxPortIngrMdaQos14StatDropOcts,
       "tmnxPortIngrMdaQos15StatDropPkts": tmnxPortIngrMdaQos15StatDropPkts,
       "tmnxPortIngrMdaQos15StatDropOcts": tmnxPortIngrMdaQos15StatDropOcts,
       "tmnxSonetGroupTable": tmnxSonetGroupTable,
       "tmnxSonetGroupEntry": tmnxSonetGroupEntry,
       "tmnxSonetGroupType": tmnxSonetGroupType,
       "tmnxSonetGroupParentPortID": tmnxSonetGroupParentPortID,
       "tmnxSonetGroupChildType": tmnxSonetGroupChildType,
       "tmnxSonetGroupName": tmnxSonetGroupName,
       "tmnxPortScalarObjs": tmnxPortScalarObjs,
       "tmnxL4LoadBalancing": tmnxL4LoadBalancing,
       "tmnxLsrIpLoadBalancing": tmnxLsrIpLoadBalancing,
       "tmnxIpLoadBalancing": tmnxIpLoadBalancing,
       "tmnxCiscoHDLCTable": tmnxCiscoHDLCTable,
       "tmnxCiscoHDLCEntry": tmnxCiscoHDLCEntry,
       "tmnxCiscoHDLCKeepAliveInt": tmnxCiscoHDLCKeepAliveInt,
       "tmnxCiscoHDLCUpCount": tmnxCiscoHDLCUpCount,
       "tmnxCiscoHDLCDownCount": tmnxCiscoHDLCDownCount,
       "tmnxCiscoHDLCOperState": tmnxCiscoHDLCOperState,
       "tmnxBundleImaGrpTable": tmnxBundleImaGrpTable,
       "tmnxBundleImaGrpEntry": tmnxBundleImaGrpEntry,
       "tmnxBundleImaGrpLnkActTimer": tmnxBundleImaGrpLnkActTimer,
       "tmnxBundleImaGrpLnkDeactTimer": tmnxBundleImaGrpLnkDeactTimer,
       "tmnxBundleImaGrpSymmetryMode": tmnxBundleImaGrpSymmetryMode,
       "tmnxBundleImaGrpTxId": tmnxBundleImaGrpTxId,
       "tmnxBundleImaGrpRxId": tmnxBundleImaGrpRxId,
       "tmnxBundleImaGrpTxRefLnk": tmnxBundleImaGrpTxRefLnk,
       "tmnxBundleImaGrpRxRefLnk": tmnxBundleImaGrpRxRefLnk,
       "tmnxBundleImaGrpSmNeState": tmnxBundleImaGrpSmNeState,
       "tmnxBundleImaGrpSmFeState": tmnxBundleImaGrpSmFeState,
       "tmnxBundleImaGrpSmFailState": tmnxBundleImaGrpSmFailState,
       "tmnxBundleImaGrpSmDownSecs": tmnxBundleImaGrpSmDownSecs,
       "tmnxBundleImaGrpSmOperSecs": tmnxBundleImaGrpSmOperSecs,
       "tmnxBundleImaGrpAvailTxCR": tmnxBundleImaGrpAvailTxCR,
       "tmnxBundleImaGrpAvailRxCR": tmnxBundleImaGrpAvailRxCR,
       "tmnxBundleImaGrpNeFails": tmnxBundleImaGrpNeFails,
       "tmnxBundleImaGrpFeFails": tmnxBundleImaGrpFeFails,
       "tmnxBundleImaGrpTxIcpCells": tmnxBundleImaGrpTxIcpCells,
       "tmnxBundleImaGrpRxIcpCells": tmnxBundleImaGrpRxIcpCells,
       "tmnxBundleImaGrpErrorIcpCells": tmnxBundleImaGrpErrorIcpCells,
       "tmnxBundleImaGrpLostRxIcpCells": tmnxBundleImaGrpLostRxIcpCells,
       "tmnxBundleImaGrpTxOamLablVal": tmnxBundleImaGrpTxOamLablVal,
       "tmnxBundleImaGrpRxOamLablVal": tmnxBundleImaGrpRxOamLablVal,
       "tmnxBundleImaGrpAlphaValue": tmnxBundleImaGrpAlphaValue,
       "tmnxBundleImaGrpBetaValue": tmnxBundleImaGrpBetaValue,
       "tmnxBundleImaGrpGammaValue": tmnxBundleImaGrpGammaValue,
       "tmnxBundleImaGrpNeClockMode": tmnxBundleImaGrpNeClockMode,
       "tmnxBundleImaGrpFeClockMode": tmnxBundleImaGrpFeClockMode,
       "tmnxBundleImaGrpVersion": tmnxBundleImaGrpVersion,
       "tmnxBundleImaGrpMaxConfBw": tmnxBundleImaGrpMaxConfBw,
       "tmnxBundleImaGrpTestState": tmnxBundleImaGrpTestState,
       "tmnxBundleImaGrpTestMember": tmnxBundleImaGrpTestMember,
       "tmnxBundleImaGrpTestPattern": tmnxBundleImaGrpTestPattern,
       "tmnxBundleImaGrpDiffDelayMaxObs": tmnxBundleImaGrpDiffDelayMaxObs,
       "tmnxBundleImaGrpLeastDelayLink": tmnxBundleImaGrpLeastDelayLink,
       "tmnxBundleMemberImaTable": tmnxBundleMemberImaTable,
       "tmnxBundleMemberImaEntry": tmnxBundleMemberImaEntry,
       "tmnxBundleMemberImaNeTxState": tmnxBundleMemberImaNeTxState,
       "tmnxBundleMemberImaNeRxState": tmnxBundleMemberImaNeRxState,
       "tmnxBundleMemberImaFeTxState": tmnxBundleMemberImaFeTxState,
       "tmnxBundleMemberImaFeRxState": tmnxBundleMemberImaFeRxState,
       "tmnxBundleMemberImaNeRxFailState": tmnxBundleMemberImaNeRxFailState,
       "tmnxBundleMemberImaFeRxFailState": tmnxBundleMemberImaFeRxFailState,
       "tmnxBundleMemberImaTxLid": tmnxBundleMemberImaTxLid,
       "tmnxBundleMemberImaRxLid": tmnxBundleMemberImaRxLid,
       "tmnxBundleMemberImaViolations": tmnxBundleMemberImaViolations,
       "tmnxBundleMemberImaNeSevErrSecs": tmnxBundleMemberImaNeSevErrSecs,
       "tmnxBundleMemberImaFeSevErrSecs": tmnxBundleMemberImaFeSevErrSecs,
       "tmnxBundleMemberImaNeUnavailSecs": tmnxBundleMemberImaNeUnavailSecs,
       "tmnxBundleMemberImaFeUnavailSecs": tmnxBundleMemberImaFeUnavailSecs,
       "tmnxBundleMemberImaNeTxUnuseSecs": tmnxBundleMemberImaNeTxUnuseSecs,
       "tmnxBundleMemberImaNeRxUnuseSecs": tmnxBundleMemberImaNeRxUnuseSecs,
       "tmnxBundleMemberImaFeTxUnuseSecs": tmnxBundleMemberImaFeTxUnuseSecs,
       "tmnxBundleMemberImaFeRxUnuseSecs": tmnxBundleMemberImaFeRxUnuseSecs,
       "tmnxBundleMemberImaNeTxNumFails": tmnxBundleMemberImaNeTxNumFails,
       "tmnxBundleMemberImaNeRxNumFails": tmnxBundleMemberImaNeRxNumFails,
       "tmnxBundleMemberImaFeTxNumFails": tmnxBundleMemberImaFeTxNumFails,
       "tmnxBundleMemberImaFeRxNumFails": tmnxBundleMemberImaFeRxNumFails,
       "tmnxBundleMemberImaTxIcpCells": tmnxBundleMemberImaTxIcpCells,
       "tmnxBundleMemberImaRxIcpCells": tmnxBundleMemberImaRxIcpCells,
       "tmnxBundleMemberImaErrorIcpCells": tmnxBundleMemberImaErrorIcpCells,
       "tmnxBundleMemberImaLstRxIcpCells": tmnxBundleMemberImaLstRxIcpCells,
       "tmnxBundleMemberImaOifAnomalies": tmnxBundleMemberImaOifAnomalies,
       "tmnxBundleMemberImaRxTestState": tmnxBundleMemberImaRxTestState,
       "tmnxBundleMemberImaRxTestPattern": tmnxBundleMemberImaRxTestPattern,
       "tmnxBundleMemberImaRelDelay": tmnxBundleMemberImaRelDelay,
       "tmnxDS1PortTable": tmnxDS1PortTable,
       "tmnxDS1PortEntry": tmnxDS1PortEntry,
       "tmnxDS1PortBuildout": tmnxDS1PortBuildout,
       "tmnxDS1PortLastChangeTime": tmnxDS1PortLastChangeTime,
       "tmnxDS1PortType": tmnxDS1PortType,
       "tmnxDS1PortLineLength": tmnxDS1PortLineLength,
       "tmnxDS1PortLbo": tmnxDS1PortLbo,
       "tmnxDS1PortDbGain": tmnxDS1PortDbGain,
       "tmnxPortSchedOverrideTable": tmnxPortSchedOverrideTable,
       "tmnxPortSchedOverrideEntry": tmnxPortSchedOverrideEntry,
       "tmnxPortSchedOverrideRowStatus": tmnxPortSchedOverrideRowStatus,
       "tmnxPortSchedOverrideSchedName": tmnxPortSchedOverrideSchedName,
       "tmnxPortSchedOverrideLastChanged": tmnxPortSchedOverrideLastChanged,
       "tmnxPortSchedOverrideMaxRate": tmnxPortSchedOverrideMaxRate,
       "tmnxPortSchedOverrideLvl1PIR": tmnxPortSchedOverrideLvl1PIR,
       "tmnxPortSchedOverrideLvl1CIR": tmnxPortSchedOverrideLvl1CIR,
       "tmnxPortSchedOverrideLvl2PIR": tmnxPortSchedOverrideLvl2PIR,
       "tmnxPortSchedOverrideLvl2CIR": tmnxPortSchedOverrideLvl2CIR,
       "tmnxPortSchedOverrideLvl3PIR": tmnxPortSchedOverrideLvl3PIR,
       "tmnxPortSchedOverrideLvl3CIR": tmnxPortSchedOverrideLvl3CIR,
       "tmnxPortSchedOverrideLvl4PIR": tmnxPortSchedOverrideLvl4PIR,
       "tmnxPortSchedOverrideLvl4CIR": tmnxPortSchedOverrideLvl4CIR,
       "tmnxPortSchedOverrideLvl5PIR": tmnxPortSchedOverrideLvl5PIR,
       "tmnxPortSchedOverrideLvl5CIR": tmnxPortSchedOverrideLvl5CIR,
       "tmnxPortSchedOverrideLvl6PIR": tmnxPortSchedOverrideLvl6PIR,
       "tmnxPortSchedOverrideLvl6CIR": tmnxPortSchedOverrideLvl6CIR,
       "tmnxPortSchedOverrideLvl7PIR": tmnxPortSchedOverrideLvl7PIR,
       "tmnxPortSchedOverrideLvl7CIR": tmnxPortSchedOverrideLvl7CIR,
       "tmnxPortSchedOverrideLvl8PIR": tmnxPortSchedOverrideLvl8PIR,
       "tmnxPortSchedOverrideLvl8CIR": tmnxPortSchedOverrideLvl8CIR,
       "tmnxPortSchedOverrideFlags": tmnxPortSchedOverrideFlags,
       "tmnxBPGrpAssocTable": tmnxBPGrpAssocTable,
       "tmnxBPGrpAssocEntry": tmnxBPGrpAssocEntry,
       "tmnxBPGrpAssocWorkingBundleID": tmnxBPGrpAssocWorkingBundleID,
       "tmnxBPGrpAssocProtectBundleID": tmnxBPGrpAssocProtectBundleID,
       "tmnxBPGrpAssocActiveBundleID": tmnxBPGrpAssocActiveBundleID,
       "tmnxBundleMlpppTable": tmnxBundleMlpppTable,
       "tmnxBundleMlpppEntry": tmnxBundleMlpppEntry,
       "tmnxBundleMlpppEndpointID": tmnxBundleMlpppEndpointID,
       "tmnxBundleMlpppEndpointIDClass": tmnxBundleMlpppEndpointIDClass,
       "tmnxBundleMlpppClassCount": tmnxBundleMlpppClassCount,
       "tmnxBundleMlpppIngQoSProfId": tmnxBundleMlpppIngQoSProfId,
       "tmnxBundleMlpppEgrQoSProfId": tmnxBundleMlpppEgrQoSProfId,
       "tmnxBundleMlpppMagicNumber": tmnxBundleMlpppMagicNumber,
       "tmnxBundleMlpppStatelessApsSwo": tmnxBundleMlpppStatelessApsSwo,
       "tmnxHsmdaPortSchOvrTblLastChngd": tmnxHsmdaPortSchOvrTblLastChngd,
       "tmnxHsmdaPortSchOvrTable": tmnxHsmdaPortSchOvrTable,
       "tmnxHsmdaPortSchOvrEntry": tmnxHsmdaPortSchOvrEntry,
       "tmnxHsmdaPortSchOvrRowStatus": tmnxHsmdaPortSchOvrRowStatus,
       "tmnxHsmdaPortSchOvrLastChanged": tmnxHsmdaPortSchOvrLastChanged,
       "tmnxHsmdaPortSchOvrMaxRate": tmnxHsmdaPortSchOvrMaxRate,
       "tmnxHsmdaPortSchOvrGrp1Rate": tmnxHsmdaPortSchOvrGrp1Rate,
       "tmnxHsmdaPortSchOvrGrp2Rate": tmnxHsmdaPortSchOvrGrp2Rate,
       "tmnxHsmdaPortSchOvrClass1Rate": tmnxHsmdaPortSchOvrClass1Rate,
       "tmnxHsmdaPortSchOvrClass1WtInGp": tmnxHsmdaPortSchOvrClass1WtInGp,
       "tmnxHsmdaPortSchOvrClass2Rate": tmnxHsmdaPortSchOvrClass2Rate,
       "tmnxHsmdaPortSchOvrClass2WtInGp": tmnxHsmdaPortSchOvrClass2WtInGp,
       "tmnxHsmdaPortSchOvrClass3Rate": tmnxHsmdaPortSchOvrClass3Rate,
       "tmnxHsmdaPortSchOvrClass3WtInGp": tmnxHsmdaPortSchOvrClass3WtInGp,
       "tmnxHsmdaPortSchOvrClass4Rate": tmnxHsmdaPortSchOvrClass4Rate,
       "tmnxHsmdaPortSchOvrClass4WtInGp": tmnxHsmdaPortSchOvrClass4WtInGp,
       "tmnxHsmdaPortSchOvrClass5Rate": tmnxHsmdaPortSchOvrClass5Rate,
       "tmnxHsmdaPortSchOvrClass5WtInGp": tmnxHsmdaPortSchOvrClass5WtInGp,
       "tmnxHsmdaPortSchOvrClass6Rate": tmnxHsmdaPortSchOvrClass6Rate,
       "tmnxHsmdaPortSchOvrClass6WtInGp": tmnxHsmdaPortSchOvrClass6WtInGp,
       "tmnxHsmdaPortSchOvrClass7Rate": tmnxHsmdaPortSchOvrClass7Rate,
       "tmnxHsmdaPortSchOvrClass7WtInGp": tmnxHsmdaPortSchOvrClass7WtInGp,
       "tmnxHsmdaPortSchOvrClass8Rate": tmnxHsmdaPortSchOvrClass8Rate,
       "tmnxHsmdaPortSchOvrClass8WtInGp": tmnxHsmdaPortSchOvrClass8WtInGp,
       "tmnxPortEgrShaperTblLastChanged": tmnxPortEgrShaperTblLastChanged,
       "tmnxPortEgrShaperTable": tmnxPortEgrShaperTable,
       "tmnxPortEgrShaperEntry": tmnxPortEgrShaperEntry,
       "tmnxPortEgrShaperName": tmnxPortEgrShaperName,
       "tmnxPortEgrShaperRowStatus": tmnxPortEgrShaperRowStatus,
       "tmnxPortEgrShaperLastChanged": tmnxPortEgrShaperLastChanged,
       "tmnxPortEgrShaperRate": tmnxPortEgrShaperRate,
       "tmnxDigitalDiagMonitorTable": tmnxDigitalDiagMonitorTable,
       "tmnxDigitalDiagMonitorEntry": tmnxDigitalDiagMonitorEntry,
       "tmnxDDMTemperature": tmnxDDMTemperature,
       "tmnxDDMTempLowWarning": tmnxDDMTempLowWarning,
       "tmnxDDMTempLowAlarm": tmnxDDMTempLowAlarm,
       "tmnxDDMTempHiWarning": tmnxDDMTempHiWarning,
       "tmnxDDMTempHiAlarm": tmnxDDMTempHiAlarm,
       "tmnxDDMSupplyVoltage": tmnxDDMSupplyVoltage,
       "tmnxDDMSupplyVoltageLowWarning": tmnxDDMSupplyVoltageLowWarning,
       "tmnxDDMSupplyVoltageLowAlarm": tmnxDDMSupplyVoltageLowAlarm,
       "tmnxDDMSupplyVoltageHiWarning": tmnxDDMSupplyVoltageHiWarning,
       "tmnxDDMSupplyVoltageHiAlarm": tmnxDDMSupplyVoltageHiAlarm,
       "tmnxDDMTxBiasCurrent": tmnxDDMTxBiasCurrent,
       "tmnxDDMTxBiasCurrentLowWarning": tmnxDDMTxBiasCurrentLowWarning,
       "tmnxDDMTxBiasCurrentLowAlarm": tmnxDDMTxBiasCurrentLowAlarm,
       "tmnxDDMTxBiasCurrentHiWarning": tmnxDDMTxBiasCurrentHiWarning,
       "tmnxDDMTxBiasCurrentHiAlarm": tmnxDDMTxBiasCurrentHiAlarm,
       "tmnxDDMTxOutputPower": tmnxDDMTxOutputPower,
       "tmnxDDMTxOutputPowerLowWarning": tmnxDDMTxOutputPowerLowWarning,
       "tmnxDDMTxOutputPowerLowAlarm": tmnxDDMTxOutputPowerLowAlarm,
       "tmnxDDMTxOutputPowerHiWarning": tmnxDDMTxOutputPowerHiWarning,
       "tmnxDDMTxOutputPowerHiAlarm": tmnxDDMTxOutputPowerHiAlarm,
       "tmnxDDMRxOpticalPower": tmnxDDMRxOpticalPower,
       "tmnxDDMRxOpticalPowerLowWarning": tmnxDDMRxOpticalPowerLowWarning,
       "tmnxDDMRxOpticalPowerLowAlarm": tmnxDDMRxOpticalPowerLowAlarm,
       "tmnxDDMRxOpticalPowerHiWarning": tmnxDDMRxOpticalPowerHiWarning,
       "tmnxDDMRxOpticalPowerHiAlarm": tmnxDDMRxOpticalPowerHiAlarm,
       "tmnxDDMRxOpticalPowerType": tmnxDDMRxOpticalPowerType,
       "tmnxDDMAux1": tmnxDDMAux1,
       "tmnxDDMAux1LowWarning": tmnxDDMAux1LowWarning,
       "tmnxDDMAux1LowAlarm": tmnxDDMAux1LowAlarm,
       "tmnxDDMAux1HiWarning": tmnxDDMAux1HiWarning,
       "tmnxDDMAux1HiAlarm": tmnxDDMAux1HiAlarm,
       "tmnxDDMAux1Type": tmnxDDMAux1Type,
       "tmnxDDMAux2": tmnxDDMAux2,
       "tmnxDDMAux2LowWarning": tmnxDDMAux2LowWarning,
       "tmnxDDMAux2LowAlarm": tmnxDDMAux2LowAlarm,
       "tmnxDDMAux2HiWarning": tmnxDDMAux2HiWarning,
       "tmnxDDMAux2HiAlarm": tmnxDDMAux2HiAlarm,
       "tmnxDDMAux2Type": tmnxDDMAux2Type,
       "tmnxDDMFailedThresholds": tmnxDDMFailedThresholds,
       "tmnxDDMExternallyCalibrated": tmnxDDMExternallyCalibrated,
       "tmnxDDMExtCalRxPower4": tmnxDDMExtCalRxPower4,
       "tmnxDDMExtCalRxPower3": tmnxDDMExtCalRxPower3,
       "tmnxDDMExtCalRxPower2": tmnxDDMExtCalRxPower2,
       "tmnxDDMExtCalRxPower1": tmnxDDMExtCalRxPower1,
       "tmnxDDMExtCalRxPower0": tmnxDDMExtCalRxPower0,
       "tmnxDDMExtCalTxLaserBiasSlope": tmnxDDMExtCalTxLaserBiasSlope,
       "tmnxDDMExtCalTxLaserBiasOffset": tmnxDDMExtCalTxLaserBiasOffset,
       "tmnxDDMExtCalTxPowerSlope": tmnxDDMExtCalTxPowerSlope,
       "tmnxDDMExtCalTxPowerOffset": tmnxDDMExtCalTxPowerOffset,
       "tmnxDDMExtCalTemperatureSlope": tmnxDDMExtCalTemperatureSlope,
       "tmnxDDMExtCalTemperatureOffset": tmnxDDMExtCalTemperatureOffset,
       "tmnxDDMExtCalVoltageSlope": tmnxDDMExtCalVoltageSlope,
       "tmnxDDMExtCalVoltageOffset": tmnxDDMExtCalVoltageOffset,
       "tPortAccIngQGrpTableLastChgd": tPortAccIngQGrpTableLastChgd,
       "tPortAccIngQGrpTable": tPortAccIngQGrpTable,
       "tPortAccIngQGrpEntry": tPortAccIngQGrpEntry,
       "tPortAccIngQGrpName": tPortAccIngQGrpName,
       "tPortAccIngQGrpRowStatus": tPortAccIngQGrpRowStatus,
       "tPortAccIngQGrpLastChgd": tPortAccIngQGrpLastChgd,
       "tPortAccIngQGrpSchedPol": tPortAccIngQGrpSchedPol,
       "tPortAccIngQGrpAcctgPolId": tPortAccIngQGrpAcctgPolId,
       "tPortAccIngQGrpCollectStats": tPortAccIngQGrpCollectStats,
       "tPortAccIngQGrpDescr": tPortAccIngQGrpDescr,
       "tPortAccIngQOverTableLastChgd": tPortAccIngQOverTableLastChgd,
       "tPortAccIngQOverTable": tPortAccIngQOverTable,
       "tPortAccIngQOverEntry": tPortAccIngQOverEntry,
       "tPortAccIngQOverQueue": tPortAccIngQOverQueue,
       "tPortAccIngQOverRowStatus": tPortAccIngQOverRowStatus,
       "tPortAccIngQOverLastChanged": tPortAccIngQOverLastChanged,
       "tPortAccIngQOverCBS": tPortAccIngQOverCBS,
       "tPortAccIngQOverMBS": tPortAccIngQOverMBS,
       "tPortAccIngQOverHiPrioOnly": tPortAccIngQOverHiPrioOnly,
       "tPortAccIngQOverAdminPIR": tPortAccIngQOverAdminPIR,
       "tPortAccIngQOverAdminCIR": tPortAccIngQOverAdminCIR,
       "tPortAccIngQOverPIRAdaptation": tPortAccIngQOverPIRAdaptation,
       "tPortAccIngQOverCIRAdaptation": tPortAccIngQOverCIRAdaptation,
       "tPortAccIngQOverMBSBytes": tPortAccIngQOverMBSBytes,
       "tPortAccEgrQGrpTableLastChgd": tPortAccEgrQGrpTableLastChgd,
       "tPortAccEgrQGrpTable": tPortAccEgrQGrpTable,
       "tPortAccEgrQGrpEntry": tPortAccEgrQGrpEntry,
       "tPortAccEgrQGrpName": tPortAccEgrQGrpName,
       "tPortAccEgrQGrpRowStatus": tPortAccEgrQGrpRowStatus,
       "tPortAccEgrQGrpLastChgd": tPortAccEgrQGrpLastChgd,
       "tPortAccEgrQGrpSchedPol": tPortAccEgrQGrpSchedPol,
       "tPortAccEgrQGrpAggRateLimit": tPortAccEgrQGrpAggRateLimit,
       "tPortAccEgrQGrpAcctgPolId": tPortAccEgrQGrpAcctgPolId,
       "tPortAccEgrQGrpCollectStats": tPortAccEgrQGrpCollectStats,
       "tPortAccEgrQGrpFrameBaseActg": tPortAccEgrQGrpFrameBaseActg,
       "tPortAccEgrQGrpDescr": tPortAccEgrQGrpDescr,
       "tPortAccEgrQOverTableLastChgd": tPortAccEgrQOverTableLastChgd,
       "tPortAccEgrQOverTable": tPortAccEgrQOverTable,
       "tPortAccEgrQOverEntry": tPortAccEgrQOverEntry,
       "tPortAccEgrQOverQueue": tPortAccEgrQOverQueue,
       "tPortAccEgrQOverRowStatus": tPortAccEgrQOverRowStatus,
       "tPortAccEgrQOverLastChanged": tPortAccEgrQOverLastChanged,
       "tPortAccEgrQOverCBS": tPortAccEgrQOverCBS,
       "tPortAccEgrQOverMBS": tPortAccEgrQOverMBS,
       "tPortAccEgrQOverHiPrioOnly": tPortAccEgrQOverHiPrioOnly,
       "tPortAccEgrQOverAdminPIR": tPortAccEgrQOverAdminPIR,
       "tPortAccEgrQOverAdminCIR": tPortAccEgrQOverAdminCIR,
       "tPortAccEgrQOverPIRAdaptation": tPortAccEgrQOverPIRAdaptation,
       "tPortAccEgrQOverCIRAdaptation": tPortAccEgrQOverCIRAdaptation,
       "tPortAccEgrQOverMBSBytes": tPortAccEgrQOverMBSBytes,
       "tPortAccEgrQOverAdminPIRPercent": tPortAccEgrQOverAdminPIRPercent,
       "tPortAccEgrQOverAdminCIRPercent": tPortAccEgrQOverAdminCIRPercent,
       "tPortAccEgrQOverRateType": tPortAccEgrQOverRateType,
       "tPortNetEgrQGrpTableLastChgd": tPortNetEgrQGrpTableLastChgd,
       "tPortNetEgrQGrpTable": tPortNetEgrQGrpTable,
       "tPortNetEgrQGrpEntry": tPortNetEgrQGrpEntry,
       "tPortNetEgrQGrpName": tPortNetEgrQGrpName,
       "tPortNetEgrQGrpRowStatus": tPortNetEgrQGrpRowStatus,
       "tPortNetEgrQGrpLastChgd": tPortNetEgrQGrpLastChgd,
       "tPortNetEgrQGrpSchedPol": tPortNetEgrQGrpSchedPol,
       "tPortNetEgrQGrpAggRateLimit": tPortNetEgrQGrpAggRateLimit,
       "tPortNetEgrQGrpAcctgPolId": tPortNetEgrQGrpAcctgPolId,
       "tPortNetEgrQGrpCollectStats": tPortNetEgrQGrpCollectStats,
       "tPortNetEgrQGrpFrameBaseActg": tPortNetEgrQGrpFrameBaseActg,
       "tPortNetEgrQGrpDescr": tPortNetEgrQGrpDescr,
       "tPortNetEgrQGrpPlcrCntrlPolicy": tPortNetEgrQGrpPlcrCntrlPolicy,
       "tPortNetEgrQGrpInstanceId": tPortNetEgrQGrpInstanceId,
       "tPortNetEgrQOverTableLastChgd": tPortNetEgrQOverTableLastChgd,
       "tPortNetEgrQOverTable": tPortNetEgrQOverTable,
       "tPortNetEgrQOverEntry": tPortNetEgrQOverEntry,
       "tPortNetEgrQOverQueue": tPortNetEgrQOverQueue,
       "tPortNetEgrQOverRowStatus": tPortNetEgrQOverRowStatus,
       "tPortNetEgrQOverLastChanged": tPortNetEgrQOverLastChanged,
       "tPortNetEgrQOverCBS": tPortNetEgrQOverCBS,
       "tPortNetEgrQOverMBS": tPortNetEgrQOverMBS,
       "tPortNetEgrQOverHiPrioOnly": tPortNetEgrQOverHiPrioOnly,
       "tPortNetEgrQOverAdminPIR": tPortNetEgrQOverAdminPIR,
       "tPortNetEgrQOverAdminCIR": tPortNetEgrQOverAdminCIR,
       "tPortNetEgrQOverPIRAdaptation": tPortNetEgrQOverPIRAdaptation,
       "tPortNetEgrQOverCIRAdaptation": tPortNetEgrQOverCIRAdaptation,
       "tPortNetEgrQOverMBSBytes": tPortNetEgrQOverMBSBytes,
       "tPortNetEgrQOverAdminPIRPercent": tPortNetEgrQOverAdminPIRPercent,
       "tPortNetEgrQOverAdminCIRPercent": tPortNetEgrQOverAdminCIRPercent,
       "tPortNetEgrQOverRateType": tPortNetEgrQOverRateType,
       "tmnxBundleMlfrTable": tmnxBundleMlfrTable,
       "tmnxBundleMlfrEntry": tmnxBundleMlfrEntry,
       "tmnxBundleMlfrBundleId": tmnxBundleMlfrBundleId,
       "tmnxBundleMlfrIngQoSProfId": tmnxBundleMlfrIngQoSProfId,
       "tmnxBundleMlfrEgrQoSProfId": tmnxBundleMlfrEgrQoSProfId,
       "tmnxBundleMlfrHelloTimer": tmnxBundleMlfrHelloTimer,
       "tmnxBundleMlfrHelloRetryCount": tmnxBundleMlfrHelloRetryCount,
       "tmnxBundleMlfrAckTimer": tmnxBundleMlfrAckTimer,
       "tmnxBundleMlfrLastChanged": tmnxBundleMlfrLastChanged,
       "tmnxPortIngQosQStatTable": tmnxPortIngQosQStatTable,
       "tmnxPortIngQosQStatEntry": tmnxPortIngQosQStatEntry,
       "tmnxPortIngQosQStatQueueId": tmnxPortIngQosQStatQueueId,
       "tmnxPortIngQosQStatOffHiPrioPkts": tmnxPortIngQosQStatOffHiPrioPkts,
       "tmnxPortIngQosQStatDpdHiPrioPkts": tmnxPortIngQosQStatDpdHiPrioPkts,
       "tmnxPortIngQosQStatOffLoPrioPkts": tmnxPortIngQosQStatOffLoPrioPkts,
       "tmnxPortIngQosQStatDpdLoPrioPkts": tmnxPortIngQosQStatDpdLoPrioPkts,
       "tmnxPortIngQosQStatOffHiPrioOcts": tmnxPortIngQosQStatOffHiPrioOcts,
       "tmnxPortIngQosQStatDpdHiPrioOcts": tmnxPortIngQosQStatDpdHiPrioOcts,
       "tmnxPortIngQosQStatOffLoPrioOcts": tmnxPortIngQosQStatOffLoPrioOcts,
       "tmnxPortIngQosQStatDpdLoPrioOcts": tmnxPortIngQosQStatDpdLoPrioOcts,
       "tmnxPortIngQosQStatFwdInProfPkts": tmnxPortIngQosQStatFwdInProfPkts,
       "tmnxPortIngQosQStatFwdOutProfPkts": tmnxPortIngQosQStatFwdOutProfPkts,
       "tmnxPortIngQosQStatFwdInProfOcts": tmnxPortIngQosQStatFwdInProfOcts,
       "tmnxPortIngQosQStatFwdOutProfOcts": tmnxPortIngQosQStatFwdOutProfOcts,
       "tmnxPortIngQosQStatUncolPktsOff": tmnxPortIngQosQStatUncolPktsOff,
       "tmnxPortIngQosQStatUncolOctsOff": tmnxPortIngQosQStatUncolOctsOff,
       "tmnxPortEgrQosQStatTable": tmnxPortEgrQosQStatTable,
       "tmnxPortEgrQosQStatEntry": tmnxPortEgrQosQStatEntry,
       "tmnxPortEgrQosQStatQueueId": tmnxPortEgrQosQStatQueueId,
       "tmnxPortEgrQosQStatFwdInProfPkts": tmnxPortEgrQosQStatFwdInProfPkts,
       "tmnxPortEgrQosQStatDpdInProfPkts": tmnxPortEgrQosQStatDpdInProfPkts,
       "tmnxPortEgrQosQStatFwdOutProfPkts": tmnxPortEgrQosQStatFwdOutProfPkts,
       "tmnxPortEgrQosQStatDpdOutProfPkts": tmnxPortEgrQosQStatDpdOutProfPkts,
       "tmnxPortEgrQosQStatFwdInProfOcts": tmnxPortEgrQosQStatFwdInProfOcts,
       "tmnxPortEgrQosQStatDpdInProfOcts": tmnxPortEgrQosQStatDpdInProfOcts,
       "tmnxPortEgrQosQStatFwdOutProfOcts": tmnxPortEgrQosQStatFwdOutProfOcts,
       "tmnxPortEgrQosQStatDpdOutProfOcts": tmnxPortEgrQosQStatDpdOutProfOcts,
       "tmnxBundleMemberMlfrTable": tmnxBundleMemberMlfrTable,
       "tmnxBundleMemberMlfrEntry": tmnxBundleMemberMlfrEntry,
       "tmnxBundleMemberMlfrDownReason": tmnxBundleMemberMlfrDownReason,
       "tmnxWaveTrackerTable": tmnxWaveTrackerTable,
       "tmnxWaveTrackerEntry": tmnxWaveTrackerEntry,
       "tmnxWaveTrackerPowerCtrlEnable": tmnxWaveTrackerPowerCtrlEnable,
       "tmnxWaveTrackerEncodeEnable": tmnxWaveTrackerEncodeEnable,
       "tmnxWaveTrackerInUse": tmnxWaveTrackerInUse,
       "tmnxWaveTrackerTargetPower": tmnxWaveTrackerTargetPower,
       "tmnxWaveTrackerWaveKey1": tmnxWaveTrackerWaveKey1,
       "tmnxWaveTrackerWaveKey2": tmnxWaveTrackerWaveKey2,
       "tmnxWaveTrackerTrailName": tmnxWaveTrackerTrailName,
       "tmnxWaveTrackerCfgAlarms": tmnxWaveTrackerCfgAlarms,
       "tmnxWaveTrackerAlarmState": tmnxWaveTrackerAlarmState,
       "tmnxWaveTrackerMeasuredPower": tmnxWaveTrackerMeasuredPower,
       "tmnxWaveTrackerMaxAttainablePwr": tmnxWaveTrackerMaxAttainablePwr,
       "tmnxWaveTrackerMinAttainablePwr": tmnxWaveTrackerMinAttainablePwr,
       "tmnxWaveTrackerUpperPowerMargin": tmnxWaveTrackerUpperPowerMargin,
       "tmnxWaveTrackerLowerPowerMargin": tmnxWaveTrackerLowerPowerMargin,
       "tPortAccEgrQGrpHMTableLastChgd": tPortAccEgrQGrpHMTableLastChgd,
       "tPortAccEgrQGrpHostMatchTable": tPortAccEgrQGrpHostMatchTable,
       "tPortAccEgrQGrpHostMatchEntry": tPortAccEgrQGrpHostMatchEntry,
       "tPortAccEgrQGrpHMIntDestId": tPortAccEgrQGrpHMIntDestId,
       "tPortAccEgrQGrpHMOrgString": tPortAccEgrQGrpHMOrgString,
       "tPortAccEgrQGrpHMRowStatus": tPortAccEgrQGrpHMRowStatus,
       "tPortAccEgrQGrpHMLastChgd": tPortAccEgrQGrpHMLastChgd,
       "tPortAccIngSchedStatTable": tPortAccIngSchedStatTable,
       "tPortAccIngSchedStatEntry": tPortAccIngSchedStatEntry,
       "tPortAccIngSchedStatName": tPortAccIngSchedStatName,
       "tPortAccIngSchedStatFwdPkts": tPortAccIngSchedStatFwdPkts,
       "tPortAccIngSchedStatFwdPktsHi": tPortAccIngSchedStatFwdPktsHi,
       "tPortAccIngSchedStatFwdPktsLo": tPortAccIngSchedStatFwdPktsLo,
       "tPortAccIngSchedStatFwdOcts": tPortAccIngSchedStatFwdOcts,
       "tPortAccIngSchedStatFwdOctsHi": tPortAccIngSchedStatFwdOctsHi,
       "tPortAccIngSchedStatFwdOctsLo": tPortAccIngSchedStatFwdOctsLo,
       "tPortAccEgrSchedStatTable": tPortAccEgrSchedStatTable,
       "tPortAccEgrSchedStatEntry": tPortAccEgrSchedStatEntry,
       "tPortAccEgrSchedStatName": tPortAccEgrSchedStatName,
       "tPortAccEgrSchedStatFwdPkts": tPortAccEgrSchedStatFwdPkts,
       "tPortAccEgrSchedStatFwdPktsHi": tPortAccEgrSchedStatFwdPktsHi,
       "tPortAccEgrSchedStatFwdPktsLo": tPortAccEgrSchedStatFwdPktsLo,
       "tPortAccEgrSchedStatFwdOcts": tPortAccEgrSchedStatFwdOcts,
       "tPortAccEgrSchedStatFwdOctsHi": tPortAccEgrSchedStatFwdOctsHi,
       "tPortAccEgrSchedStatFwdOctsLo": tPortAccEgrSchedStatFwdOctsLo,
       "tPortNetEgrSchedStatTable": tPortNetEgrSchedStatTable,
       "tPortNetEgrSchedStatEntry": tPortNetEgrSchedStatEntry,
       "tPortNetEgrSchedStatName": tPortNetEgrSchedStatName,
       "tPortNetEgrSchedStatFwdPkts": tPortNetEgrSchedStatFwdPkts,
       "tPortNetEgrSchedStatFwdPktsHi": tPortNetEgrSchedStatFwdPktsHi,
       "tPortNetEgrSchedStatFwdPktsLo": tPortNetEgrSchedStatFwdPktsLo,
       "tPortNetEgrSchedStatFwdOcts": tPortNetEgrSchedStatFwdOcts,
       "tPortNetEgrSchedStatFwdOctsHi": tPortNetEgrSchedStatFwdOctsHi,
       "tPortNetEgrSchedStatFwdOctsLo": tPortNetEgrSchedStatFwdOctsLo,
       "tPortEgrVPortTableLastChgd": tPortEgrVPortTableLastChgd,
       "tPortEgrVPortTable": tPortEgrVPortTable,
       "tPortEgrVPortEntry": tPortEgrVPortEntry,
       "tPortEgrVPortName": tPortEgrVPortName,
       "tPortEgrVPortRowStatus": tPortEgrVPortRowStatus,
       "tPortEgrVPortLastChanged": tPortEgrVPortLastChanged,
       "tPortEgrVPortDescr": tPortEgrVPortDescr,
       "tPortEgrVPortSchedPol": tPortEgrVPortSchedPol,
       "tPortEgrVPortAggRateLimit": tPortEgrVPortAggRateLimit,
       "tPortEgrVPortHMTableLastChgd": tPortEgrVPortHMTableLastChgd,
       "tPortEgrVPortHostMatchTable": tPortEgrVPortHostMatchTable,
       "tPortEgrVPortHostMatchEntry": tPortEgrVPortHostMatchEntry,
       "tPortEgrVPortHMIntDestId": tPortEgrVPortHMIntDestId,
       "tPortEgrVPortHMOrgString": tPortEgrVPortHMOrgString,
       "tPortEgrVPortHMRowStatus": tPortEgrVPortHMRowStatus,
       "tPortEgrVPortHMLastChgd": tPortEgrVPortHMLastChgd,
       "tmnxOpticalPortCfgTable": tmnxOpticalPortCfgTable,
       "tmnxOpticalPortCfgEntry": tmnxOpticalPortCfgEntry,
       "tmnxOpticalPortAmpCfgAlarms": tmnxOpticalPortAmpCfgAlarms,
       "tmnxOpticalPortTdcmCtrlMode": tmnxOpticalPortTdcmCtrlMode,
       "tmnxOpticalPortTdcmManCfgDisp": tmnxOpticalPortTdcmManCfgDisp,
       "tmnxOpticalPortTdcmCfgRxChan": tmnxOpticalPortTdcmCfgRxChan,
       "tmnxOpticalPortTdcmCfgAlarms": tmnxOpticalPortTdcmCfgAlarms,
       "tmnxOpticalPortTdcmDispSwpStart": tmnxOpticalPortTdcmDispSwpStart,
       "tmnxOpticalPortTdcmDispSwpEnd": tmnxOpticalPortTdcmDispSwpEnd,
       "tmnxOpticalPortOperTable": tmnxOpticalPortOperTable,
       "tmnxOpticalPortOperEntry": tmnxOpticalPortOperEntry,
       "tmnxOpticalPortHasRxAmplifier": tmnxOpticalPortHasRxAmplifier,
       "tmnxOpticalPortHasRxTdcm": tmnxOpticalPortHasRxTdcm,
       "tmnxOpticalPortAmpPowerIn": tmnxOpticalPortAmpPowerIn,
       "tmnxOpticalPortAmpGain": tmnxOpticalPortAmpGain,
       "tmnxOpticalPortAmpPowerOut": tmnxOpticalPortAmpPowerOut,
       "tmnxOpticalPortAmpPumpTemp": tmnxOpticalPortAmpPumpTemp,
       "tmnxOpticalPortAmpModuleTemp": tmnxOpticalPortAmpModuleTemp,
       "tmnxOpticalPortAmpPumpCurrent": tmnxOpticalPortAmpPumpCurrent,
       "tmnxOpticalPortAmpAlarmState": tmnxOpticalPortAmpAlarmState,
       "tmnxOpticalPortAmpSerialNum": tmnxOpticalPortAmpSerialNum,
       "tmnxOpticalPortAmpCtrlState": tmnxOpticalPortAmpCtrlState,
       "tmnxOpticalPortTdcmPowerIn": tmnxOpticalPortTdcmPowerIn,
       "tmnxOpticalPortTdcmLoss": tmnxOpticalPortTdcmLoss,
       "tmnxOpticalPortTdcmPowerOut": tmnxOpticalPortTdcmPowerOut,
       "tmnxOpticalPortTdcmRtd1Temp": tmnxOpticalPortTdcmRtd1Temp,
       "tmnxOpticalPortTdcmRtd2Temp": tmnxOpticalPortTdcmRtd2Temp,
       "tmnxOpticalPortTdcmRtd3Temp": tmnxOpticalPortTdcmRtd3Temp,
       "tmnxOpticalPortTdcmRtd4Temp": tmnxOpticalPortTdcmRtd4Temp,
       "tmnxOpticalPortTdcmModuleTemp": tmnxOpticalPortTdcmModuleTemp,
       "tmnxOpticalPortTdcmMinDisp": tmnxOpticalPortTdcmMinDisp,
       "tmnxOpticalPortTdcmMaxDisp": tmnxOpticalPortTdcmMaxDisp,
       "tmnxOpticalPortTdcmAutoDisp": tmnxOpticalPortTdcmAutoDisp,
       "tmnxOpticalPortTdcmMeasDisp": tmnxOpticalPortTdcmMeasDisp,
       "tmnxOpticalPortTdcmPresRxChan": tmnxOpticalPortTdcmPresRxChan,
       "tmnxOpticalPortTdcmAlarmState": tmnxOpticalPortTdcmAlarmState,
       "tmnxOpticalPortTdcmSerialNum": tmnxOpticalPortTdcmSerialNum,
       "tmnxOpticalPortTdcmCtrlState": tmnxOpticalPortTdcmCtrlState,
       "tmnxOpticalPortDwdmChannelMin": tmnxOpticalPortDwdmChannelMin,
       "tmnxOpticalPortDwdmChannelMax": tmnxOpticalPortDwdmChannelMax,
       "tmnxOpticalPortLaserTunability": tmnxOpticalPortLaserTunability,
       "tmnxPortEgrExpShaperTblLastChngd": tmnxPortEgrExpShaperTblLastChngd,
       "tmnxPortEgrExpShaperTable": tmnxPortEgrExpShaperTable,
       "tmnxPortEgrExpShaperEntry": tmnxPortEgrExpShaperEntry,
       "tmnxPortEgrExpShaperName": tmnxPortEgrExpShaperName,
       "tmnxPortEgrExpShaperRowStatus": tmnxPortEgrExpShaperRowStatus,
       "tmnxPortEgrExpShaperRate": tmnxPortEgrExpShaperRate,
       "tmnxPortEgrExpShaperClass1Rate": tmnxPortEgrExpShaperClass1Rate,
       "tmnxPortEgrExpShaperClass2Rate": tmnxPortEgrExpShaperClass2Rate,
       "tmnxPortEgrExpShaperClass3Rate": tmnxPortEgrExpShaperClass3Rate,
       "tmnxPortEgrExpShaperClass4Rate": tmnxPortEgrExpShaperClass4Rate,
       "tmnxPortEgrExpShaperClass5Rate": tmnxPortEgrExpShaperClass5Rate,
       "tmnxPortEgrExpShaperClass6Rate": tmnxPortEgrExpShaperClass6Rate,
       "tmnxPortEgrExpShaperClass7Rate": tmnxPortEgrExpShaperClass7Rate,
       "tmnxPortEgrExpShaperClass8Rate": tmnxPortEgrExpShaperClass8Rate,
       "tmnxPortEgrExpShaperLastChanged": tmnxPortEgrExpShaperLastChanged,
       "tmnxPortEgrExpShaperLoBrstMaxCls": tmnxPortEgrExpShaperLoBrstMaxCls,
       "tmnxPortEgrExpShaperClass1Thresh": tmnxPortEgrExpShaperClass1Thresh,
       "tmnxPortEgrExpShaperClass2Thresh": tmnxPortEgrExpShaperClass2Thresh,
       "tmnxPortEgrExpShaperClass3Thresh": tmnxPortEgrExpShaperClass3Thresh,
       "tmnxPortEgrExpShaperClass4Thresh": tmnxPortEgrExpShaperClass4Thresh,
       "tmnxPortEgrExpShaperClass5Thresh": tmnxPortEgrExpShaperClass5Thresh,
       "tmnxPortEgrExpShaperClass6Thresh": tmnxPortEgrExpShaperClass6Thresh,
       "tmnxPortEgrExpShaperClass7Thresh": tmnxPortEgrExpShaperClass7Thresh,
       "tmnxPortEgrExpShaperClass8Thresh": tmnxPortEgrExpShaperClass8Thresh,
       "tmnxPortEgrExpShaperThresh": tmnxPortEgrExpShaperThresh,
       "tmnxPortEgrExpShaperLoBurstLimit": tmnxPortEgrExpShaperLoBurstLimit,
       "tmnxPortEgrExpShaperHiBurstInc": tmnxPortEgrExpShaperHiBurstInc,
       "tmnxPortEgrExpShaperCl1BrstLimit": tmnxPortEgrExpShaperCl1BrstLimit,
       "tmnxPortEgrExpShaperCl2BrstLimit": tmnxPortEgrExpShaperCl2BrstLimit,
       "tmnxPortEgrExpShaperCl3BrstLimit": tmnxPortEgrExpShaperCl3BrstLimit,
       "tmnxPortEgrExpShaperCl4BrstLimit": tmnxPortEgrExpShaperCl4BrstLimit,
       "tmnxPortEgrExpShaperCl5BrstLimit": tmnxPortEgrExpShaperCl5BrstLimit,
       "tmnxPortEgrExpShaperCl6BrstLimit": tmnxPortEgrExpShaperCl6BrstLimit,
       "tmnxPortEgrExpShaperCl7BrstLimit": tmnxPortEgrExpShaperCl7BrstLimit,
       "tmnxPortEgrExpShaperCl8BrstLimit": tmnxPortEgrExpShaperCl8BrstLimit,
       "tPortEgrExpShaperStatsTable": tPortEgrExpShaperStatsTable,
       "tPortEgrExpShaperStatsEntry": tPortEgrExpShaperStatsEntry,
       "tPortEgrExpShaperStLstClrdTime": tPortEgrExpShaperStLstClrdTime,
       "tPortEgrExpShaperCls1StFwdPkts": tPortEgrExpShaperCls1StFwdPkts,
       "tPortEgrExpShaperCls1StFwdOcts": tPortEgrExpShaperCls1StFwdOcts,
       "tPortEgrExpShaperCls1StMonOvrOct": tPortEgrExpShaperCls1StMonOvrOct,
       "tPortEgrExpShaperCls2StFwdPkts": tPortEgrExpShaperCls2StFwdPkts,
       "tPortEgrExpShaperCls2StFwdOcts": tPortEgrExpShaperCls2StFwdOcts,
       "tPortEgrExpShaperCls2StMonOvrOct": tPortEgrExpShaperCls2StMonOvrOct,
       "tPortEgrExpShaperCls3StFwdPkts": tPortEgrExpShaperCls3StFwdPkts,
       "tPortEgrExpShaperCls3StFwdOcts": tPortEgrExpShaperCls3StFwdOcts,
       "tPortEgrExpShaperCls3StMonOvrOct": tPortEgrExpShaperCls3StMonOvrOct,
       "tPortEgrExpShaperCls4StFwdPkts": tPortEgrExpShaperCls4StFwdPkts,
       "tPortEgrExpShaperCls4StFwdOcts": tPortEgrExpShaperCls4StFwdOcts,
       "tPortEgrExpShaperCls4StMonOvrOct": tPortEgrExpShaperCls4StMonOvrOct,
       "tPortEgrExpShaperCls5StFwdPkts": tPortEgrExpShaperCls5StFwdPkts,
       "tPortEgrExpShaperCls5StFwdOcts": tPortEgrExpShaperCls5StFwdOcts,
       "tPortEgrExpShaperCls5StMonOvrOct": tPortEgrExpShaperCls5StMonOvrOct,
       "tPortEgrExpShaperCls6StFwdPkts": tPortEgrExpShaperCls6StFwdPkts,
       "tPortEgrExpShaperCls6StFwdOcts": tPortEgrExpShaperCls6StFwdOcts,
       "tPortEgrExpShaperCls6StMonOvrOct": tPortEgrExpShaperCls6StMonOvrOct,
       "tPortEgrExpShaperCls7StFwdPkts": tPortEgrExpShaperCls7StFwdPkts,
       "tPortEgrExpShaperCls7StFwdOcts": tPortEgrExpShaperCls7StFwdOcts,
       "tPortEgrExpShaperCls7StMonOvrOct": tPortEgrExpShaperCls7StMonOvrOct,
       "tPortEgrExpShaperCls8StFwdPkts": tPortEgrExpShaperCls8StFwdPkts,
       "tPortEgrExpShaperCls8StFwdOcts": tPortEgrExpShaperCls8StFwdOcts,
       "tPortEgrExpShaperCls8StMonOvrOct": tPortEgrExpShaperCls8StMonOvrOct,
       "tPortEgrExpShaperAggStFwdPkts": tPortEgrExpShaperAggStFwdPkts,
       "tPortEgrExpShaperAggStFwdOcts": tPortEgrExpShaperAggStFwdOcts,
       "tPortEgrExpShaperAggStMonOvrOct": tPortEgrExpShaperAggStMonOvrOct,
       "tPortEgrExpShaperStatsHLTable": tPortEgrExpShaperStatsHLTable,
       "tPortEgrExpShaperStatsHLEntry": tPortEgrExpShaperStatsHLEntry,
       "tPortEgrExpShaperCls1StFwdPktsL": tPortEgrExpShaperCls1StFwdPktsL,
       "tPortEgrExpShaperCls1StFwdPktsH": tPortEgrExpShaperCls1StFwdPktsH,
       "tPortEgrExpShaperCls1StFwdOctsL": tPortEgrExpShaperCls1StFwdOctsL,
       "tPortEgrExpShaperCls1StFwdOctsH": tPortEgrExpShaperCls1StFwdOctsH,
       "tPortEgrExpShaperCls1StMonOvrOL": tPortEgrExpShaperCls1StMonOvrOL,
       "tPortEgrExpShaperCls1StMonOvrOH": tPortEgrExpShaperCls1StMonOvrOH,
       "tPortEgrExpShaperCls2StFwdPktsL": tPortEgrExpShaperCls2StFwdPktsL,
       "tPortEgrExpShaperCls2StFwdPktsH": tPortEgrExpShaperCls2StFwdPktsH,
       "tPortEgrExpShaperCls2StFwdOctsL": tPortEgrExpShaperCls2StFwdOctsL,
       "tPortEgrExpShaperCls2StFwdOctsH": tPortEgrExpShaperCls2StFwdOctsH,
       "tPortEgrExpShaperCls2StMonOvrOL": tPortEgrExpShaperCls2StMonOvrOL,
       "tPortEgrExpShaperCls2StMonOvrOH": tPortEgrExpShaperCls2StMonOvrOH,
       "tPortEgrExpShaperCls3StFwdPktsL": tPortEgrExpShaperCls3StFwdPktsL,
       "tPortEgrExpShaperCls3StFwdPktsH": tPortEgrExpShaperCls3StFwdPktsH,
       "tPortEgrExpShaperCls3StFwdOctsL": tPortEgrExpShaperCls3StFwdOctsL,
       "tPortEgrExpShaperCls3StFwdOctsH": tPortEgrExpShaperCls3StFwdOctsH,
       "tPortEgrExpShaperCls3StMonOvrOL": tPortEgrExpShaperCls3StMonOvrOL,
       "tPortEgrExpShaperCls3StMonOvrOH": tPortEgrExpShaperCls3StMonOvrOH,
       "tPortEgrExpShaperCls4StFwdPktsL": tPortEgrExpShaperCls4StFwdPktsL,
       "tPortEgrExpShaperCls4StFwdPktsH": tPortEgrExpShaperCls4StFwdPktsH,
       "tPortEgrExpShaperCls4StFwdOctsL": tPortEgrExpShaperCls4StFwdOctsL,
       "tPortEgrExpShaperCls4StFwdOctsH": tPortEgrExpShaperCls4StFwdOctsH,
       "tPortEgrExpShaperCls4StMonOvrOL": tPortEgrExpShaperCls4StMonOvrOL,
       "tPortEgrExpShaperCls4StMonOvrOH": tPortEgrExpShaperCls4StMonOvrOH,
       "tPortEgrExpShaperCls5StFwdPktsL": tPortEgrExpShaperCls5StFwdPktsL,
       "tPortEgrExpShaperCls5StFwdPktsH": tPortEgrExpShaperCls5StFwdPktsH,
       "tPortEgrExpShaperCls5StFwdOctsL": tPortEgrExpShaperCls5StFwdOctsL,
       "tPortEgrExpShaperCls5StFwdOctsH": tPortEgrExpShaperCls5StFwdOctsH,
       "tPortEgrExpShaperCls5StMonOvrOL": tPortEgrExpShaperCls5StMonOvrOL,
       "tPortEgrExpShaperCls5StMonOvrOH": tPortEgrExpShaperCls5StMonOvrOH,
       "tPortEgrExpShaperCls6StFwdPktsL": tPortEgrExpShaperCls6StFwdPktsL,
       "tPortEgrExpShaperCls6StFwdPktsH": tPortEgrExpShaperCls6StFwdPktsH,
       "tPortEgrExpShaperCls6StFwdOctsL": tPortEgrExpShaperCls6StFwdOctsL,
       "tPortEgrExpShaperCls6StFwdOctsH": tPortEgrExpShaperCls6StFwdOctsH,
       "tPortEgrExpShaperCls6StMonOvrOL": tPortEgrExpShaperCls6StMonOvrOL,
       "tPortEgrExpShaperCls6StMonOvrOH": tPortEgrExpShaperCls6StMonOvrOH,
       "tPortEgrExpShaperCls7StFwdPktsL": tPortEgrExpShaperCls7StFwdPktsL,
       "tPortEgrExpShaperCls7StFwdPktsH": tPortEgrExpShaperCls7StFwdPktsH,
       "tPortEgrExpShaperCls7StFwdOctsL": tPortEgrExpShaperCls7StFwdOctsL,
       "tPortEgrExpShaperCls7StFwdOctsH": tPortEgrExpShaperCls7StFwdOctsH,
       "tPortEgrExpShaperCls7StMonOvrOL": tPortEgrExpShaperCls7StMonOvrOL,
       "tPortEgrExpShaperCls7StMonOvrOH": tPortEgrExpShaperCls7StMonOvrOH,
       "tPortEgrExpShaperCls8StFwdPktsL": tPortEgrExpShaperCls8StFwdPktsL,
       "tPortEgrExpShaperCls8StFwdPktsH": tPortEgrExpShaperCls8StFwdPktsH,
       "tPortEgrExpShaperCls8StFwdOctsL": tPortEgrExpShaperCls8StFwdOctsL,
       "tPortEgrExpShaperCls8StFwdOctsH": tPortEgrExpShaperCls8StFwdOctsH,
       "tPortEgrExpShaperCls8StMonOvrOL": tPortEgrExpShaperCls8StMonOvrOL,
       "tPortEgrExpShaperCls8StMonOvrOH": tPortEgrExpShaperCls8StMonOvrOH,
       "tPortEgrExpShaperAggStFwdPktsL": tPortEgrExpShaperAggStFwdPktsL,
       "tPortEgrExpShaperAggStFwdPktsH": tPortEgrExpShaperAggStFwdPktsH,
       "tPortEgrExpShaperAggStFwdOctsL": tPortEgrExpShaperAggStFwdOctsL,
       "tPortEgrExpShaperAggStFwdOctsH": tPortEgrExpShaperAggStFwdOctsH,
       "tPortEgrExpShaperAggStMonOvrOL": tPortEgrExpShaperAggStMonOvrOL,
       "tPortEgrExpShaperAggStMonOvrOH": tPortEgrExpShaperAggStMonOvrOH,
       "tPortEgrVPortAggStatsTable": tPortEgrVPortAggStatsTable,
       "tPortEgrVPortAggStatsEntry": tPortEgrVPortAggStatsEntry,
       "tPortEgrVPStLvl": tPortEgrVPStLvl,
       "tPortEgrVPStLstClrdTime": tPortEgrVPStLstClrdTime,
       "tPortEgrVPStLvlFwdPkt": tPortEgrVPStLvlFwdPkt,
       "tPortEgrVPStLvlFwdOct": tPortEgrVPStLvlFwdOct,
       "tPortEgrVPStLvlDpdPkt": tPortEgrVPStLvlDpdPkt,
       "tPortEgrVPStLvlDpdOct": tPortEgrVPStLvlDpdOct,
       "tPortEgrVPortAggStatsHLTable": tPortEgrVPortAggStatsHLTable,
       "tPortEgrVPortAggStatsHLEntry": tPortEgrVPortAggStatsHLEntry,
       "tPortEgrVPStLvlFwdPktL": tPortEgrVPStLvlFwdPktL,
       "tPortEgrVPStLvlFwdPktH": tPortEgrVPStLvlFwdPktH,
       "tPortEgrVPStLvlFwdOctL": tPortEgrVPStLvlFwdOctL,
       "tPortEgrVPStLvlFwdOctH": tPortEgrVPStLvlFwdOctH,
       "tPortEgrVPStLvlDpdPktL": tPortEgrVPStLvlDpdPktL,
       "tPortEgrVPStLvlDpdPktH": tPortEgrVPStLvlDpdPktH,
       "tPortEgrVPStLvlDpdOctL": tPortEgrVPStLvlDpdOctL,
       "tPortEgrVPStLvlDpdOctH": tPortEgrVPStLvlDpdOctH,
       "tmnxDDMLaneTable": tmnxDDMLaneTable,
       "tmnxDDMLaneEntry": tmnxDDMLaneEntry,
       "tmnxDDMLaneId": tmnxDDMLaneId,
       "tmnxDDMLaneTemperature": tmnxDDMLaneTemperature,
       "tmnxDDMLaneTempLowWarn": tmnxDDMLaneTempLowWarn,
       "tmnxDDMLaneTempLowAlarm": tmnxDDMLaneTempLowAlarm,
       "tmnxDDMLaneTempHiWarn": tmnxDDMLaneTempHiWarn,
       "tmnxDDMLaneTempHiAlarm": tmnxDDMLaneTempHiAlarm,
       "tmnxDDMLaneTxBiasCurrent": tmnxDDMLaneTxBiasCurrent,
       "tmnxDDMLaneTxBiasCurrentLowWarn": tmnxDDMLaneTxBiasCurrentLowWarn,
       "tmnxDDMLaneTxBiasCurrentLowAlarm": tmnxDDMLaneTxBiasCurrentLowAlarm,
       "tmnxDDMLaneTxBiasCurrentHiWarn": tmnxDDMLaneTxBiasCurrentHiWarn,
       "tmnxDDMLaneTxBiasCurrentHiAlarm": tmnxDDMLaneTxBiasCurrentHiAlarm,
       "tmnxDDMLaneTxOutputPower": tmnxDDMLaneTxOutputPower,
       "tmnxDDMLaneTxOutputPowerLowWarn": tmnxDDMLaneTxOutputPowerLowWarn,
       "tmnxDDMLaneTxOutputPowerLowAlarm": tmnxDDMLaneTxOutputPowerLowAlarm,
       "tmnxDDMLaneTxOutputPowerHiWarn": tmnxDDMLaneTxOutputPowerHiWarn,
       "tmnxDDMLaneTxOutputPowerHiAlarm": tmnxDDMLaneTxOutputPowerHiAlarm,
       "tmnxDDMLaneRxOpticalPower": tmnxDDMLaneRxOpticalPower,
       "tmnxDDMLaneRxOpticalPwrLowWarn": tmnxDDMLaneRxOpticalPwrLowWarn,
       "tmnxDDMLaneRxOpticalPwrLowAlarm": tmnxDDMLaneRxOpticalPwrLowAlarm,
       "tmnxDDMLaneRxOpticalPwrHiWarn": tmnxDDMLaneRxOpticalPwrHiWarn,
       "tmnxDDMLaneRxOpticalPwrHiAlarm": tmnxDDMLaneRxOpticalPwrHiAlarm,
       "tmnxDDMLaneRxOpticalPowerType": tmnxDDMLaneRxOpticalPowerType,
       "tmnxDDMLaneFailedThresholds": tmnxDDMLaneFailedThresholds,
       "tmnxPortPlcyObjs": tmnxPortPlcyObjs,
       "tmnxPortPlcyTableLastCh": tmnxPortPlcyTableLastCh,
       "tmnxPortPlcyTable": tmnxPortPlcyTable,
       "tmnxPortPlcyEntry": tmnxPortPlcyEntry,
       "tmnxPortPlcyName": tmnxPortPlcyName,
       "tmnxPortPlcyRowStatus": tmnxPortPlcyRowStatus,
       "tmnxPortPlcyLastCh": tmnxPortPlcyLastCh,
       "tmnxPortPlcyDescription": tmnxPortPlcyDescription,
       "tmnxPortPlcyEgrPortSchedPlcy": tmnxPortPlcyEgrPortSchedPlcy,
       "tPortNetEgrQGrpArbitStatTable": tPortNetEgrQGrpArbitStatTable,
       "tPortNetEgrQGrpArbitStatEntry": tPortNetEgrQGrpArbitStatEntry,
       "tPortNetEgrQGrpArbitStatName": tPortNetEgrQGrpArbitStatName,
       "tPortNetEgrQGrpArbitStatFwdPkts": tPortNetEgrQGrpArbitStatFwdPkts,
       "tPortNetEgrQGrpArbitStatFwdPktsL": tPortNetEgrQGrpArbitStatFwdPktsL,
       "tPortNetEgrQGrpArbitStatFwdPktsH": tPortNetEgrQGrpArbitStatFwdPktsH,
       "tPortNetEgrQGrpArbitStatFwdOcts": tPortNetEgrQGrpArbitStatFwdOcts,
       "tPortNetEgrQGrpArbitStatFwdOctsL": tPortNetEgrQGrpArbitStatFwdOctsL,
       "tPortNetEgrQGrpArbitStatFwdOctsH": tPortNetEgrQGrpArbitStatFwdOctsH,
       "tmnxPwPortTblLastChanged": tmnxPwPortTblLastChanged,
       "tmnxPwPortTable": tmnxPwPortTable,
       "tmnxPwPortEntry": tmnxPwPortEntry,
       "tmnxPwPortId": tmnxPwPortId,
       "tmnxPwPortRowStatus": tmnxPwPortRowStatus,
       "tmnxPwPortLastChgd": tmnxPwPortLastChgd,
       "tmnxPwPortEncapType": tmnxPwPortEncapType,
       "tmnxPortNotificationObjects": tmnxPortNotificationObjects,
       "tmnxPortNotifyPortId": tmnxPortNotifyPortId,
       "tmnxPortNotifySonetAlarmReason": tmnxPortNotifySonetAlarmReason,
       "tmnxPortNotifySonetPathAlarmReason": tmnxPortNotifySonetPathAlarmReason,
       "tmnxPortNotifyError": tmnxPortNotifyError,
       "tmnxPortNotifyDS3AlarmReason": tmnxPortNotifyDS3AlarmReason,
       "tmnxPortNotifyDS1AlarmReason": tmnxPortNotifyDS1AlarmReason,
       "tmnxPortNotifyBundleId": tmnxPortNotifyBundleId,
       "tmnxPortNotifyEtherAlarmReason": tmnxPortNotifyEtherAlarmReason,
       "tmnxDDMFailedObject": tmnxDDMFailedObject,
       "tmnxDSXClockSyncStateObject": tmnxDSXClockSyncStateObject,
       "tmnxPortNotifyDescription": tmnxPortNotifyDescription,
       "tmnxPortNotifyWTAlarmReason": tmnxPortNotifyWTAlarmReason,
       "tmnxHostMatchNotifyIntDestId": tmnxHostMatchNotifyIntDestId,
       "tmnxHostMatchNotifyOrgString": tmnxHostMatchNotifyOrgString,
       "tmnxHostMatchNotifySubIdent": tmnxHostMatchNotifySubIdent,
       "tmnxObjAppResvSize": tmnxObjAppResvSize,
       "tmnxObjAppResvCbsOld": tmnxObjAppResvCbsOld,
       "tmnxObjAppResvCbsNew": tmnxObjAppResvCbsNew,
       "tmnxObjAppSumOfQResvSize": tmnxObjAppSumOfQResvSize,
       "tmnxObjType": tmnxObjType,
       "tmnxObjPortId": tmnxObjPortId,
       "tmnxObjMdaId": tmnxObjMdaId,
       "tmnxObjAppType": tmnxObjAppType,
       "tmnxObjAppPool": tmnxObjAppPool,
       "tmnxObjNamedPoolPolicy": tmnxObjNamedPoolPolicy,
       "tmnxPortNotifyEtherCrcThreshold": tmnxPortNotifyEtherCrcThreshold,
       "tmnxPortNotifyEtherCrcMultiplier": tmnxPortNotifyEtherCrcMultiplier,
       "tmnxPortNotifyEtherCrcAlarmValue": tmnxPortNotifyEtherCrcAlarmValue,
       "tmnxObjAppResvSizeOld": tmnxObjAppResvSizeOld,
       "tmnxDDMLaneIdOrModule": tmnxDDMLaneIdOrModule,
       "tmnxFRObjs": tmnxFRObjs,
       "tmnxFRDlcmiTable": tmnxFRDlcmiTable,
       "tmnxFRDlcmiEntry": tmnxFRDlcmiEntry,
       "tmnxFRDlcmiMode": tmnxFRDlcmiMode,
       "tmnxFRDlcmiN392Dce": tmnxFRDlcmiN392Dce,
       "tmnxFRDlcmiN393Dce": tmnxFRDlcmiN393Dce,
       "tmnxFRDlcmiT392Dce": tmnxFRDlcmiT392Dce,
       "tmnxFRDlcmiTxStatusEnqMsgs": tmnxFRDlcmiTxStatusEnqMsgs,
       "tmnxFRDlcmiRxStatusEnqMsgs": tmnxFRDlcmiRxStatusEnqMsgs,
       "tmnxFRDlcmiStatusEnqMsgTimeouts": tmnxFRDlcmiStatusEnqMsgTimeouts,
       "tmnxFRDlcmiTxStatusMsgs": tmnxFRDlcmiTxStatusMsgs,
       "tmnxFRDlcmiRxStatusMsgs": tmnxFRDlcmiRxStatusMsgs,
       "tmnxFRDlcmiStatusMsgTimeouts": tmnxFRDlcmiStatusMsgTimeouts,
       "tmnxFRDlcmiDiscardedMsgs": tmnxFRDlcmiDiscardedMsgs,
       "tmnxFRDlcmiInvRxSeqNumMsgs": tmnxFRDlcmiInvRxSeqNumMsgs,
       "tmnxFrIntfTable": tmnxFrIntfTable,
       "tmnxFrIntfEntry": tmnxFrIntfEntry,
       "tmnxFrIntfFrf12Mode": tmnxFrIntfFrf12Mode,
       "tmnxFrIntfLinkId": tmnxFrIntfLinkId,
       "tmnxFrIntfLastChanged": tmnxFrIntfLastChanged,
       "tmnxFrf12IntfTable": tmnxFrf12IntfTable,
       "tmnxFrf12IntfEntry": tmnxFrf12IntfEntry,
       "tmnxFrf12IntfFragmentThreshold": tmnxFrf12IntfFragmentThreshold,
       "tmnxFrf12IntfEgrQoSProfId": tmnxFrf12IntfEgrQoSProfId,
       "tmnxFrf12IntfLastChanged": tmnxFrf12IntfLastChanged,
       "tmnxQosAppObjs": tmnxQosAppObjs,
       "tmnxQosPoolAppTable": tmnxQosPoolAppTable,
       "tmnxQosPoolAppEntry": tmnxQosPoolAppEntry,
       "tmnxObjectType": tmnxObjectType,
       "tmnxObjectId": tmnxObjectId,
       "tmnxObjectAppType": tmnxObjectAppType,
       "tmnxObjectAppPool": tmnxObjectAppPool,
       "tmnxObjectAppPoolRowStatus": tmnxObjectAppPoolRowStatus,
       "tmnxObjectAppResvCbs": tmnxObjectAppResvCbs,
       "tmnxObjectAppSlopePolicy": tmnxObjectAppSlopePolicy,
       "tmnxObjectAppPoolSize": tmnxObjectAppPoolSize,
       "tmnxObjectAppResvCbsAmbrAlrmStep": tmnxObjectAppResvCbsAmbrAlrmStep,
       "tmnxObjectAppResvCbsAmbrAlrmMax": tmnxObjectAppResvCbsAmbrAlrmMax,
       "tmnxObjectAppAmbrAlrmThresh": tmnxObjectAppAmbrAlrmThresh,
       "tmnxObjectAppRedAlrmThresh": tmnxObjectAppRedAlrmThresh,
       "tmnxATMObjs": tmnxATMObjs,
       "tmnxATMIntfTable": tmnxATMIntfTable,
       "tmnxATMIntfEntry": tmnxATMIntfEntry,
       "tmnxATMIntfCellFormat": tmnxATMIntfCellFormat,
       "tmnxATMIntfMinVpValue": tmnxATMIntfMinVpValue,
       "tmnxATMIntfMapping": tmnxATMIntfMapping,
       "tmnxATMIntfCustomBufferMode": tmnxATMIntfCustomBufferMode,
       "tmnxATMIntfBufferPool": tmnxATMIntfBufferPool,
       "tmnxATMIntfVcThreshold": tmnxATMIntfVcThreshold,
       "tmnxPortATMVpShaperTblLastCh": tmnxPortATMVpShaperTblLastCh,
       "tmnxPortATMVpShaperTable": tmnxPortATMVpShaperTable,
       "tmnxPortATMVpShaperEntry": tmnxPortATMVpShaperEntry,
       "tmnxPortATMVpShaperVpi": tmnxPortATMVpShaperVpi,
       "tmnxPortATMVpShaperRowStatus": tmnxPortATMVpShaperRowStatus,
       "tmnxPortATMVpShaperLastMgmtCh": tmnxPortATMVpShaperLastMgmtCh,
       "tmnxPortATMVpShaperEgrAtd": tmnxPortATMVpShaperEgrAtd,
       "tmnxPortStatsObjs": tmnxPortStatsObjs,
       "tmnxPortNetIngressStatsTable": tmnxPortNetIngressStatsTable,
       "tmnxPortNetIngressStatsEntry": tmnxPortNetIngressStatsEntry,
       "tmnxPortNetIngressQueueIndex": tmnxPortNetIngressQueueIndex,
       "tmnxPortNetIngressFwdInProfPkts": tmnxPortNetIngressFwdInProfPkts,
       "tmnxPortNetIngressFwdOutProfPkts": tmnxPortNetIngressFwdOutProfPkts,
       "tmnxPortNetIngressFwdInProfOcts": tmnxPortNetIngressFwdInProfOcts,
       "tmnxPortNetIngressFwdOutProfOcts": tmnxPortNetIngressFwdOutProfOcts,
       "tmnxPortNetIngressDroInProfPkts": tmnxPortNetIngressDroInProfPkts,
       "tmnxPortNetIngressDroOutProfPkts": tmnxPortNetIngressDroOutProfPkts,
       "tmnxPortNetIngressDroInProfOcts": tmnxPortNetIngressDroInProfOcts,
       "tmnxPortNetIngressDroOutProfOcts": tmnxPortNetIngressDroOutProfOcts,
       "tmnxPortNetEgressStatsTable": tmnxPortNetEgressStatsTable,
       "tmnxPortNetEgressStatsEntry": tmnxPortNetEgressStatsEntry,
       "tmnxPortNetEgressQueueIndex": tmnxPortNetEgressQueueIndex,
       "tmnxPortNetEgressFwdInProfPkts": tmnxPortNetEgressFwdInProfPkts,
       "tmnxPortNetEgressFwdOutProfPkts": tmnxPortNetEgressFwdOutProfPkts,
       "tmnxPortNetEgressFwdInProfOcts": tmnxPortNetEgressFwdInProfOcts,
       "tmnxPortNetEgressFwdOutProfOcts": tmnxPortNetEgressFwdOutProfOcts,
       "tmnxPortNetEgressDroInProfPkts": tmnxPortNetEgressDroInProfPkts,
       "tmnxPortNetEgressDroOutProfPkts": tmnxPortNetEgressDroOutProfPkts,
       "tmnxPortNetEgressDroInProfOcts": tmnxPortNetEgressDroInProfOcts,
       "tmnxPortNetEgressDroOutProfOcts": tmnxPortNetEgressDroOutProfOcts,
       "tmnxCiscoHDLCStatsTable": tmnxCiscoHDLCStatsTable,
       "tmnxCiscoHDLCStatsEntry": tmnxCiscoHDLCStatsEntry,
       "tmnxCiscoHDLCDiscardStatInPkts": tmnxCiscoHDLCDiscardStatInPkts,
       "tmnxCiscoHDLCDiscardStatOutPkts": tmnxCiscoHDLCDiscardStatOutPkts,
       "tmnxCiscoHDLCStatInPkts": tmnxCiscoHDLCStatInPkts,
       "tmnxCiscoHDLCStatOutPkts": tmnxCiscoHDLCStatOutPkts,
       "tmnxCiscoHDLCStatInOctets": tmnxCiscoHDLCStatInOctets,
       "tmnxCiscoHDLCStatOutOctets": tmnxCiscoHDLCStatOutOctets,
       "tmnxMcMlpppStatsTable": tmnxMcMlpppStatsTable,
       "tmnxMcMlpppStatsEntry": tmnxMcMlpppStatsEntry,
       "tmnxMcMlpppClassIndex": tmnxMcMlpppClassIndex,
       "tmnxMcMlpppStatsIngressOct": tmnxMcMlpppStatsIngressOct,
       "tmnxMcMlpppStatsIngressPkt": tmnxMcMlpppStatsIngressPkt,
       "tmnxMcMlpppStatsIngressErrPkt": tmnxMcMlpppStatsIngressErrPkt,
       "tmnxMcMlpppStatsEgressOct": tmnxMcMlpppStatsEgressOct,
       "tmnxMcMlpppStatsEgressPkt": tmnxMcMlpppStatsEgressPkt,
       "tmnxMcMlpppStatsEgressErrPkt": tmnxMcMlpppStatsEgressErrPkt,
       "tmnxPortNetEgrQStatTable": tmnxPortNetEgrQStatTable,
       "tmnxPortNetEgrQStatEntry": tmnxPortNetEgrQStatEntry,
       "tmnxPortNetEgrQFwdInProfPkts": tmnxPortNetEgrQFwdInProfPkts,
       "tmnxPortNetEgrQFwdOutProfPkts": tmnxPortNetEgrQFwdOutProfPkts,
       "tmnxPortNetEgrQFwdInProfOcts": tmnxPortNetEgrQFwdInProfOcts,
       "tmnxPortNetEgrQFwdOutProfOcts": tmnxPortNetEgrQFwdOutProfOcts,
       "tmnxPortNetEgrQDroInProfPkts": tmnxPortNetEgrQDroInProfPkts,
       "tmnxPortNetEgrQDroOutProfPkts": tmnxPortNetEgrQDroOutProfPkts,
       "tmnxPortNetEgrQDroInProfOcts": tmnxPortNetEgrQDroInProfOcts,
       "tmnxPortNetEgrQDroOutProfOcts": tmnxPortNetEgrQDroOutProfOcts,
       "tmnxPortCemStatsTable": tmnxPortCemStatsTable,
       "tmnxPortCemStatsEntry": tmnxPortCemStatsEntry,
       "tmnxPortCemStatsReportAlarm": tmnxPortCemStatsReportAlarm,
       "tmnxPortCemStatsIgrForwardedPkts": tmnxPortCemStatsIgrForwardedPkts,
       "tmnxPortCemStatsIgrDroppedPkts": tmnxPortCemStatsIgrDroppedPkts,
       "tmnxPortCemStatsEgrForwardedPkts": tmnxPortCemStatsEgrForwardedPkts,
       "tmnxPortCemStatsEgrDroppedPkts": tmnxPortCemStatsEgrDroppedPkts,
       "tmnxPortCemStatsEgrMissingPkts": tmnxPortCemStatsEgrMissingPkts,
       "tmnxPortCemStatsEgrPktsReOrder": tmnxPortCemStatsEgrPktsReOrder,
       "tmnxPortCemStatsEgrJtrBfrURun": tmnxPortCemStatsEgrJtrBfrURun,
       "tmnxPortCemStatsEgrJtrBfrORun": tmnxPortCemStatsEgrJtrBfrORun,
       "tmnxPortCemStatsEgrMisOrderDrop": tmnxPortCemStatsEgrMisOrderDrop,
       "tmnxPortCemStatsEgrMalformedPkts": tmnxPortCemStatsEgrMalformedPkts,
       "tmnxPortCemStatsEgrLBitDrop": tmnxPortCemStatsEgrLBitDrop,
       "tmnxPortCemStatsEgrMultipleDrop": tmnxPortCemStatsEgrMultipleDrop,
       "tmnxPortCemStatsEgrESs": tmnxPortCemStatsEgrESs,
       "tmnxPortCemStatsEgrSESs": tmnxPortCemStatsEgrSESs,
       "tmnxPortCemStatsEgrUASs": tmnxPortCemStatsEgrUASs,
       "tmnxPortCemStatsEgrFailureCounts": tmnxPortCemStatsEgrFailureCounts,
       "tmnxPortCemStatsEgrURunCounts": tmnxPortCemStatsEgrURunCounts,
       "tmnxPortCemStatsEgrORunCounts": tmnxPortCemStatsEgrORunCounts,
       "tmnxPortCemStatsEgrJtrBfrDepth": tmnxPortCemStatsEgrJtrBfrDepth,
       "tPortNetEgrQGrpPStatTable": tPortNetEgrQGrpPStatTable,
       "tPortNetEgrQGrpPStatEntry": tPortNetEgrQGrpPStatEntry,
       "tPortNetEgrQGrpPStatQosPolicerId": tPortNetEgrQGrpPStatQosPolicerId,
       "tPortNetEgrQGrpPStatMode": tPortNetEgrQGrpPStatMode,
       "tPortNetEgrQGrpPStOffInProfPkt": tPortNetEgrQGrpPStOffInProfPkt,
       "tPortNetEgrQGrpPStOffInProfPktL": tPortNetEgrQGrpPStOffInProfPktL,
       "tPortNetEgrQGrpPStOffInProfPktH": tPortNetEgrQGrpPStOffInProfPktH,
       "tPortNetEgrQGrpPStFwdInProfPkt": tPortNetEgrQGrpPStFwdInProfPkt,
       "tPortNetEgrQGrpPStFwdInProfPktL": tPortNetEgrQGrpPStFwdInProfPktL,
       "tPortNetEgrQGrpPStFwdInProfPktH": tPortNetEgrQGrpPStFwdInProfPktH,
       "tPortNetEgrQGrpPStDrpInProfPkt": tPortNetEgrQGrpPStDrpInProfPkt,
       "tPortNetEgrQGrpPStDrpInProfPktL": tPortNetEgrQGrpPStDrpInProfPktL,
       "tPortNetEgrQGrpPStDrpInProfPktH": tPortNetEgrQGrpPStDrpInProfPktH,
       "tPortNetEgrQGrpPStOffOutProfPkt": tPortNetEgrQGrpPStOffOutProfPkt,
       "tPortNetEgrQGrpPStOffOutProfPktL": tPortNetEgrQGrpPStOffOutProfPktL,
       "tPortNetEgrQGrpPStOffOutProfPktH": tPortNetEgrQGrpPStOffOutProfPktH,
       "tPortNetEgrQGrpPStFwdOutProfPkt": tPortNetEgrQGrpPStFwdOutProfPkt,
       "tPortNetEgrQGrpPStFwdOutProfPktL": tPortNetEgrQGrpPStFwdOutProfPktL,
       "tPortNetEgrQGrpPStFwdOutProfPktH": tPortNetEgrQGrpPStFwdOutProfPktH,
       "tPortNetEgrQGrpPStDrpOutProfPkt": tPortNetEgrQGrpPStDrpOutProfPkt,
       "tPortNetEgrQGrpPStDrpOutProfPktL": tPortNetEgrQGrpPStDrpOutProfPktL,
       "tPortNetEgrQGrpPStDrpOutProfPktH": tPortNetEgrQGrpPStDrpOutProfPktH,
       "tPortNetEgrQGrpPStOffInProfOct": tPortNetEgrQGrpPStOffInProfOct,
       "tPortNetEgrQGrpPStOffInProfOctL": tPortNetEgrQGrpPStOffInProfOctL,
       "tPortNetEgrQGrpPStOffInProfOctH": tPortNetEgrQGrpPStOffInProfOctH,
       "tPortNetEgrQGrpPStFwdInProfOct": tPortNetEgrQGrpPStFwdInProfOct,
       "tPortNetEgrQGrpPStFwdInProfOctL": tPortNetEgrQGrpPStFwdInProfOctL,
       "tPortNetEgrQGrpPStFwdInProfOctH": tPortNetEgrQGrpPStFwdInProfOctH,
       "tPortNetEgrQGrpPStDrpInProfOct": tPortNetEgrQGrpPStDrpInProfOct,
       "tPortNetEgrQGrpPStDrpInProfOctL": tPortNetEgrQGrpPStDrpInProfOctL,
       "tPortNetEgrQGrpPStDrpInProfOctH": tPortNetEgrQGrpPStDrpInProfOctH,
       "tPortNetEgrQGrpPStOffOutProfOct": tPortNetEgrQGrpPStOffOutProfOct,
       "tPortNetEgrQGrpPStOffOutProfOctL": tPortNetEgrQGrpPStOffOutProfOctL,
       "tPortNetEgrQGrpPStOffOutProfOctH": tPortNetEgrQGrpPStOffOutProfOctH,
       "tPortNetEgrQGrpPStFwdOutProfOct": tPortNetEgrQGrpPStFwdOutProfOct,
       "tPortNetEgrQGrpPStFwdOutProfOctL": tPortNetEgrQGrpPStFwdOutProfOctL,
       "tPortNetEgrQGrpPStFwdOutProfOctH": tPortNetEgrQGrpPStFwdOutProfOctH,
       "tPortNetEgrQGrpPStDrpOutProfOct": tPortNetEgrQGrpPStDrpOutProfOct,
       "tPortNetEgrQGrpPStDrpOutProfOctL": tPortNetEgrQGrpPStDrpOutProfOctL,
       "tPortNetEgrQGrpPStDrpOutProfOctH": tPortNetEgrQGrpPStDrpOutProfOctH,
       "tPortNetEgrQGrpPStUncolPktOff": tPortNetEgrQGrpPStUncolPktOff,
       "tPortNetEgrQGrpPStUncolPktOffL": tPortNetEgrQGrpPStUncolPktOffL,
       "tPortNetEgrQGrpPStUncolPktOffH": tPortNetEgrQGrpPStUncolPktOffH,
       "tPortNetEgrQGrpPStUncolOctOff": tPortNetEgrQGrpPStUncolOctOff,
       "tPortNetEgrQGrpPStUncolOctOffL": tPortNetEgrQGrpPStUncolOctOffL,
       "tPortNetEgrQGrpPStUncolOctOffH": tPortNetEgrQGrpPStUncolOctOffH,
       "tmnxPortNotifyPrefix": tmnxPortNotifyPrefix,
       "tmnxPortNotification": tmnxPortNotification,
       "tmnxEqOobPortFailure": tmnxEqOobPortFailure,
       "tmnxEqPortFailure": tmnxEqPortFailure,
       "tmnxQosServiceDegraded": tmnxQosServiceDegraded,
       "tmnxEqPortSonetAlarm": tmnxEqPortSonetAlarm,
       "tmnxEqPortSonetAlarmClear": tmnxEqPortSonetAlarmClear,
       "tmnxEqPortSonetPathAlarm": tmnxEqPortSonetPathAlarm,
       "tmnxEqPortSonetPathAlarmClear": tmnxEqPortSonetPathAlarmClear,
       "tmnxEqPortSFPInserted": tmnxEqPortSFPInserted,
       "tmnxEqPortSFPRemoved": tmnxEqPortSFPRemoved,
       "tmnxEqPortWrongSFP": tmnxEqPortWrongSFP,
       "tmnxEqPortSFPCorrupted": tmnxEqPortSFPCorrupted,
       "tmnxPortNotifyBerSdTca": tmnxPortNotifyBerSdTca,
       "tmnxPortNotifyBerSfTca": tmnxPortNotifyBerSfTca,
       "tmnxEqPortError": tmnxEqPortError,
       "tmnxEqPortDS3Alarm": tmnxEqPortDS3Alarm,
       "tmnxEqPortDS3AlarmClear": tmnxEqPortDS3AlarmClear,
       "tmnxEqPortDS1Alarm": tmnxEqPortDS1Alarm,
       "tmnxEqPortDS1AlarmClear": tmnxEqPortDS1AlarmClear,
       "tmnxEqPortBndlYellowDiffExceeded": tmnxEqPortBndlYellowDiffExceeded,
       "tmnxEqPortBndlRedDiffExceeded": tmnxEqPortBndlRedDiffExceeded,
       "tmnxEqPortBndlBadEndPtDiscr": tmnxEqPortBndlBadEndPtDiscr,
       "tmnxEqPortEtherAlarm": tmnxEqPortEtherAlarm,
       "tmnxEqPortEtherAlarmClear": tmnxEqPortEtherAlarmClear,
       "tmnxDS1E1LoopbackStarted": tmnxDS1E1LoopbackStarted,
       "tmnxDS1E1LoopbackStopped": tmnxDS1E1LoopbackStopped,
       "tmnxDS3E3LoopbackStarted": tmnxDS3E3LoopbackStarted,
       "tmnxDS3E3LoopbackStopped": tmnxDS3E3LoopbackStopped,
       "tmnxSonetSDHLoopbackStarted": tmnxSonetSDHLoopbackStarted,
       "tmnxSonetSDHLoopbackStopped": tmnxSonetSDHLoopbackStopped,
       "tmnxEqPortEtherLoopDetected": tmnxEqPortEtherLoopDetected,
       "tmnxEqPortEtherLoopCleared": tmnxEqPortEtherLoopCleared,
       "tmnxEqPortSpeedCfgNotCompatible": tmnxEqPortSpeedCfgNotCompatible,
       "tmnxEqPortDuplexCfgNotCompatible": tmnxEqPortDuplexCfgNotCompatible,
       "tmnxEqPortIngressRateCfgNotCompatible": tmnxEqPortIngressRateCfgNotCompatible,
       "tmnxEqDigitalDiagMonitorFailure": tmnxEqDigitalDiagMonitorFailure,
       "tmnxEqPortSFPStatusFailure": tmnxEqPortSFPStatusFailure,
       "tmnxDSXClockSyncStateChange": tmnxDSXClockSyncStateChange,
       "tmnxPortUnsupportedFunction": tmnxPortUnsupportedFunction,
       "tmnxBundleMemberMlfrLoopback": tmnxBundleMemberMlfrLoopback,
       "tmnxEqPortWaveTrackerAlarm": tmnxEqPortWaveTrackerAlarm,
       "tPortAccEgrQGrpHostMatchFailure": tPortAccEgrQGrpHostMatchFailure,
       "tPortEgrVPortHostMatchFailure": tPortEgrVPortHostMatchFailure,
       "tmnxEqDigitalDiagMonitorClear": tmnxEqDigitalDiagMonitorClear,
       "tmnxEqPortOpticalAmpAlarm": tmnxEqPortOpticalAmpAlarm,
       "tmnxEqPortOpticalTdcmAlarm": tmnxEqPortOpticalTdcmAlarm,
       "tmnxEqSonetClockSrcNotCompatible": tmnxEqSonetClockSrcNotCompatible,
       "tmnxEqSonetSfThreshNotCompatible": tmnxEqSonetSfThreshNotCompatible,
       "tmnxEqSonetFramingNotCompatible": tmnxEqSonetFramingNotCompatible,
       "tmnxResvCbsPoolThreshGreen": tmnxResvCbsPoolThreshGreen,
       "tmnxResvCbsPoolThreshAmber": tmnxResvCbsPoolThreshAmber,
       "tmnxResvCbsPoolThreshRed": tmnxResvCbsPoolThreshRed,
       "tmnxEqPortEtherCrcAlarm": tmnxEqPortEtherCrcAlarm,
       "tmnxEqPortEtherCrcAlarmClear": tmnxEqPortEtherCrcAlarmClear,
       "tmnxEqPortEtherInternalAlarm": tmnxEqPortEtherInternalAlarm,
       "tmnxEqPortEtherInternalAlarmClr": tmnxEqPortEtherInternalAlarmClr}
)
