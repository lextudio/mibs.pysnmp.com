# SNMP MIB module (TIMETRA-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:54 2024
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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(THPolCIRRateOverride,
 THPolPIRRateOverride,
 THsmdaPIRMRateOverride,
 THsmdaWeightOverride,
 TIngPolicerId,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPerPacketOffsetOvr,
 TPlcrBurstSizeBytesOverride,
 TmnxActionType,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxIngPolicerStatMode,
 TmnxIngPolicerStatModeOverride,
 TmnxIpSecIsaOperFlags,
 TmnxOperState,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "THPolCIRRateOverride",
    "THPolPIRRateOverride",
    "THsmdaPIRMRateOverride",
    "THsmdaWeightOverride",
    "TIngPolicerId",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPerPacketOffsetOvr",
    "TPlcrBurstSizeBytesOverride",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxIngPolicerStatMode",
    "TmnxIngPolicerStatModeOverride",
    "TmnxIpSecIsaOperFlags",
    "TmnxOperState",
    "TmnxPortID")


# MODULE-IDENTITY

tmnxChassisMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 2)
)
tmnxChassisMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1909-02-28 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-16 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1900-08-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxAlarmState(Integer32, TextualConvention):
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
        *(("alarmActive", 1),
          ("alarmCleared", 2),
          ("unknown", 0))
    )



class TmnxChassisIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class TmnxChassisIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )



class TmnxHwIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class TmnxHwIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class TmnxHwClass(Integer32, TextualConvention):
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
              14,
              15,
              16,
              30)
        )
    )
    namedValues = NamedValues(
        *(("alarmInputModule", 16),
          ("ccm", 15),
          ("chassis", 3),
          ("container", 4),
          ("cpmModule", 9),
          ("fabricModule", 10),
          ("fan", 6),
          ("flashDiskModule", 12),
          ("ioModule", 8),
          ("mcm", 14),
          ("mdaModule", 11),
          ("other", 1),
          ("port", 13),
          ("powerSupply", 5),
          ("sensor", 7),
          ("unknown", 2),
          ("vwmShelfModule", 30))
    )



class TmnxCardType(Unsigned32, TextualConvention):
    status = "current"


class TmnxCardSuppType(Bits, TextualConvention):
    status = "current"


class TmnxFabricType(Unsigned32, TextualConvention):
    status = "current"


class TmnxFabricSuppType(Bits, TextualConvention):
    status = "current"


class TmnxCardRebootType(Integer32, TextualConvention):
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
        *(("cardPowerCycle", 3),
          ("cardReset", 1),
          ("notApplicable", 2))
    )



class TmnxChassisType(Unsigned32, TextualConvention):
    status = "current"


class TmnxDeviceState(Integer32, TextualConvention):
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
        *(("deviceNotEquipped", 2),
          ("deviceStateFailed", 4),
          ("deviceStateOk", 3),
          ("deviceStateOutOfService", 5),
          ("deviceStateUnknown", 1))
    )



class TmnxLEDState(Integer32, TextualConvention):
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
        *(("ledAmber", 3),
          ("ledAmberBlink", 6),
          ("ledGreen", 5),
          ("ledGreenBlink", 8),
          ("ledOff", 1),
          ("ledRed", 2),
          ("ledYellow", 4),
          ("ledYellowBlink", 7))
    )



class TmnxMdaType(Unsigned32, TextualConvention):
    status = "current"


class TmnxMDASuppType(Bits, TextualConvention):
    status = "current"


class TmnxMDAChanType(Integer32, TextualConvention):
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
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("pdhDs0Grp", 18),
          ("pdhDs1", 16),
          ("pdhDs3", 14),
          ("pdhE1", 17),
          ("pdhE3", 15),
          ("pdhTu3", 13),
          ("sdhTug3", 7),
          ("sonetSts1", 6),
          ("sonetSts12", 4),
          ("sonetSts192", 2),
          ("sonetSts3", 5),
          ("sonetSts48", 3),
          ("sonetSts768", 1),
          ("sonetVt15", 9),
          ("sonetVt2", 10),
          ("sonetVt3", 11),
          ("sonetVt6", 12),
          ("sonetVtg", 8),
          ("unknown", 0))
    )



class TmnxMdaAtmMode(Integer32, TextualConvention):
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
        *(("max16kVc", 2),
          ("max8kVc", 1),
          ("notApplicable", 0))
    )



class TmnxCcmType(Unsigned32, TextualConvention):
    status = "current"


class TmnxMcmType(Unsigned32, TextualConvention):
    status = "current"


class TmnxSlotNum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class TmnxSlotNumOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



class TmnxPortAdminStatus(Integer32, TextualConvention):
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
        *(("diagnose", 4),
          ("inService", 2),
          ("noop", 1),
          ("outOfService", 3))
    )



class TmnxChassisMode(Integer32, TextualConvention):
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
        *(("modeA", 1),
          ("modeB", 2),
          ("modeC", 3),
          ("modeD", 4))
    )



class TmnxSETSRefSource(Integer32, TextualConvention):
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
        *(("bits1", 3),
          ("bits2", 4),
          ("noReference", 6),
          ("otherCPM", 0),
          ("ptp", 5),
          ("reference1", 1),
          ("reference2", 2))
    )



class TmnxSETSRefQualified(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-qualified", 2),
          ("qualified", 1))
    )



class TmnxSETSRefAlarm(Bits, TextualConvention):
    status = "current"


class TmnxBITSIfType(Integer32, TextualConvention):
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
        *(("e1-pcm30crc", 3),
          ("e1-pcm31crc", 4),
          ("none", 0),
          ("t1-esf", 1),
          ("t1-sf", 2))
    )



class TmnxSSMQualityLevel(Integer32, TextualConvention):
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



class TmnxRefInState(Integer32, TextualConvention):
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
        *(("ais", 7),
          ("disabled", 0),
          ("fer", 13),
          ("ghost", 8),
          ("lof", 6),
          ("lowQuality", 5),
          ("previousFailure", 4),
          ("ptpAdminDisabled", 17),
          ("ptpNoParentClock", 19),
          ("ptpOperDown", 18),
          ("reserved-10", 10),
          ("reserved-11", 11),
          ("reserved-12", 12),
          ("reserved-14", 14),
          ("reserved-15", 15),
          ("reserved-16", 16),
          ("standby", 2),
          ("unqualified", 1),
          ("up", 3),
          ("validating", 9))
    )



class TmnxBITSOutSource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalClock", 2),
          ("lineRef", 1))
    )



class TmnxCcagId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TmnxCcagRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class TmnxCcagRateOption(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 1),
          ("cca", 2))
    )



class TmnxChassisPemType(Integer32, TextualConvention):
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
        *(("not-applicable", 0),
          ("pem", 2),
          ("pem-3", 3),
          ("peq", 4),
          ("unknown", 1))
    )



class TmnxCardSlotBitMap(Bits, TextualConvention):
    status = "current"


class TmnxTunnelGroupId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class TmnxTunnelGroupIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxHwConformance_ObjectIdentity = ObjectIdentity
tmnxHwConformance = _TmnxHwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2)
)
_TmnxChassisConformance_ObjectIdentity = ObjectIdentity
tmnxChassisConformance = _TmnxChassisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1)
)
_TmnxChassisCompliances_ObjectIdentity = ObjectIdentity
tmnxChassisCompliances = _TmnxChassisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1)
)
_TmnxChassisComp7710_ObjectIdentity = ObjectIdentity
tmnxChassisComp7710 = _TmnxChassisComp7710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 5)
)
_TmnxChassisGroups_ObjectIdentity = ObjectIdentity
tmnxChassisGroups = _TmnxChassisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2)
)
_TmnxHwObjs_ObjectIdentity = ObjectIdentity
tmnxHwObjs = _TmnxHwObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2)
)
_TmnxChassisObjs_ObjectIdentity = ObjectIdentity
tmnxChassisObjs = _TmnxChassisObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1)
)


class _TmnxChassisTotalNumber_Type(Integer32):
    """Custom type tmnxChassisTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TmnxChassisTotalNumber_Type.__name__ = "Integer32"
_TmnxChassisTotalNumber_Object = MibScalar
tmnxChassisTotalNumber = _TmnxChassisTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 1),
    _TmnxChassisTotalNumber_Type()
)
tmnxChassisTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisTotalNumber.setStatus("current")
_TmnxChassisLastChange_Type = TimeStamp
_TmnxChassisLastChange_Object = MibScalar
tmnxChassisLastChange = _TmnxChassisLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 2),
    _TmnxChassisLastChange_Type()
)
tmnxChassisLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisLastChange.setStatus("current")
_TmnxChassisTable_Object = MibTable
tmnxChassisTable = _TmnxChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxChassisTable.setStatus("current")
_TmnxChassisEntry_Object = MibTableRow
tmnxChassisEntry = _TmnxChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1)
)
tmnxChassisEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
)
if mibBuilder.loadTexts:
    tmnxChassisEntry.setStatus("current")
_TmnxChassisIndex_Type = TmnxChassisIndex
_TmnxChassisIndex_Object = MibTableColumn
tmnxChassisIndex = _TmnxChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 1),
    _TmnxChassisIndex_Type()
)
tmnxChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxChassisIndex.setStatus("current")
_TmnxChassisRowStatus_Type = RowStatus
_TmnxChassisRowStatus_Object = MibTableColumn
tmnxChassisRowStatus = _TmnxChassisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 2),
    _TmnxChassisRowStatus_Type()
)
tmnxChassisRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisRowStatus.setStatus("current")


class _TmnxChassisName_Type(TNamedItemOrEmpty):
    """Custom type tmnxChassisName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxChassisName_Object = MibTableColumn
tmnxChassisName = _TmnxChassisName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 3),
    _TmnxChassisName_Type()
)
tmnxChassisName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisName.setStatus("current")
_TmnxChassisType_Type = TmnxChassisType
_TmnxChassisType_Object = MibTableColumn
tmnxChassisType = _TmnxChassisType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 4),
    _TmnxChassisType_Type()
)
tmnxChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisType.setStatus("current")


class _TmnxChassisLocation_Type(TItemDescription):
    """Custom type tmnxChassisLocation based on TItemDescription"""
    defaultHexValue = ""


_TmnxChassisLocation_Object = MibTableColumn
tmnxChassisLocation = _TmnxChassisLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 5),
    _TmnxChassisLocation_Type()
)
tmnxChassisLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisLocation.setStatus("current")


class _TmnxChassisCoordinates_Type(TItemDescription):
    """Custom type tmnxChassisCoordinates based on TItemDescription"""
    defaultHexValue = ""


_TmnxChassisCoordinates_Object = MibTableColumn
tmnxChassisCoordinates = _TmnxChassisCoordinates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 6),
    _TmnxChassisCoordinates_Type()
)
tmnxChassisCoordinates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisCoordinates.setStatus("current")
_TmnxChassisNumSlots_Type = Unsigned32
_TmnxChassisNumSlots_Object = MibTableColumn
tmnxChassisNumSlots = _TmnxChassisNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 7),
    _TmnxChassisNumSlots_Type()
)
tmnxChassisNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisNumSlots.setStatus("current")
_TmnxChassisNumPorts_Type = Unsigned32
_TmnxChassisNumPorts_Object = MibTableColumn
tmnxChassisNumPorts = _TmnxChassisNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 8),
    _TmnxChassisNumPorts_Type()
)
tmnxChassisNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisNumPorts.setStatus("current")
_TmnxChassisNumPwrSupplies_Type = Unsigned32
_TmnxChassisNumPwrSupplies_Object = MibTableColumn
tmnxChassisNumPwrSupplies = _TmnxChassisNumPwrSupplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 9),
    _TmnxChassisNumPwrSupplies_Type()
)
tmnxChassisNumPwrSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisNumPwrSupplies.setStatus("current")
_TmnxChassisNumFanTrays_Type = Unsigned32
_TmnxChassisNumFanTrays_Object = MibTableColumn
tmnxChassisNumFanTrays = _TmnxChassisNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 10),
    _TmnxChassisNumFanTrays_Type()
)
tmnxChassisNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisNumFanTrays.setStatus("current")
_TmnxChassisNumFans_Type = Unsigned32
_TmnxChassisNumFans_Object = MibTableColumn
tmnxChassisNumFans = _TmnxChassisNumFans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 11),
    _TmnxChassisNumFans_Type()
)
tmnxChassisNumFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisNumFans.setStatus("current")
_TmnxChassisCriticalLEDState_Type = TmnxLEDState
_TmnxChassisCriticalLEDState_Object = MibTableColumn
tmnxChassisCriticalLEDState = _TmnxChassisCriticalLEDState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 12),
    _TmnxChassisCriticalLEDState_Type()
)
tmnxChassisCriticalLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisCriticalLEDState.setStatus("current")
_TmnxChassisMajorLEDState_Type = TmnxLEDState
_TmnxChassisMajorLEDState_Object = MibTableColumn
tmnxChassisMajorLEDState = _TmnxChassisMajorLEDState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 13),
    _TmnxChassisMajorLEDState_Type()
)
tmnxChassisMajorLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisMajorLEDState.setStatus("current")
_TmnxChassisMinorLEDState_Type = TmnxLEDState
_TmnxChassisMinorLEDState_Object = MibTableColumn
tmnxChassisMinorLEDState = _TmnxChassisMinorLEDState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 14),
    _TmnxChassisMinorLEDState_Type()
)
tmnxChassisMinorLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisMinorLEDState.setStatus("current")
_TmnxChassisBaseMacAddress_Type = MacAddress
_TmnxChassisBaseMacAddress_Object = MibTableColumn
tmnxChassisBaseMacAddress = _TmnxChassisBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 15),
    _TmnxChassisBaseMacAddress_Type()
)
tmnxChassisBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisBaseMacAddress.setStatus("current")
_TmnxChassisCLLICode_Type = DisplayString
_TmnxChassisCLLICode_Object = MibTableColumn
tmnxChassisCLLICode = _TmnxChassisCLLICode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 16),
    _TmnxChassisCLLICode_Type()
)
tmnxChassisCLLICode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisCLLICode.setStatus("current")


class _TmnxChassisReboot_Type(TmnxActionType):
    """Custom type tmnxChassisReboot based on TmnxActionType"""


_TmnxChassisReboot_Object = MibTableColumn
tmnxChassisReboot = _TmnxChassisReboot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 17),
    _TmnxChassisReboot_Type()
)
tmnxChassisReboot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisReboot.setStatus("current")


class _TmnxChassisUpgrade_Type(TmnxActionType):
    """Custom type tmnxChassisUpgrade based on TmnxActionType"""


_TmnxChassisUpgrade_Object = MibTableColumn
tmnxChassisUpgrade = _TmnxChassisUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 18),
    _TmnxChassisUpgrade_Type()
)
tmnxChassisUpgrade.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisUpgrade.setStatus("current")


class _TmnxChassisAdminMode_Type(TmnxChassisMode):
    """Custom type tmnxChassisAdminMode based on TmnxChassisMode"""


_TmnxChassisAdminMode_Object = MibTableColumn
tmnxChassisAdminMode = _TmnxChassisAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 19),
    _TmnxChassisAdminMode_Type()
)
tmnxChassisAdminMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisAdminMode.setStatus("current")
_TmnxChassisOperMode_Type = TmnxChassisMode
_TmnxChassisOperMode_Object = MibTableColumn
tmnxChassisOperMode = _TmnxChassisOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 20),
    _TmnxChassisOperMode_Type()
)
tmnxChassisOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisOperMode.setStatus("current")


class _TmnxChassisModeForce_Type(TmnxActionType):
    """Custom type tmnxChassisModeForce based on TmnxActionType"""


_TmnxChassisModeForce_Object = MibTableColumn
tmnxChassisModeForce = _TmnxChassisModeForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 21),
    _TmnxChassisModeForce_Type()
)
tmnxChassisModeForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisModeForce.setStatus("current")


class _TmnxChassisUpdateWaitTime_Type(Unsigned32):
    """Custom type tmnxChassisUpdateWaitTime based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_TmnxChassisUpdateWaitTime_Type.__name__ = "Unsigned32"
_TmnxChassisUpdateWaitTime_Object = MibTableColumn
tmnxChassisUpdateWaitTime = _TmnxChassisUpdateWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 22),
    _TmnxChassisUpdateWaitTime_Type()
)
tmnxChassisUpdateWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisUpdateWaitTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxChassisUpdateWaitTime.setUnits("seconds")
_TmnxChassisUpdateTimeLeft_Type = Unsigned32
_TmnxChassisUpdateTimeLeft_Object = MibTableColumn
tmnxChassisUpdateTimeLeft = _TmnxChassisUpdateTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 23),
    _TmnxChassisUpdateTimeLeft_Type()
)
tmnxChassisUpdateTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisUpdateTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxChassisUpdateTimeLeft.setUnits("seconds")


class _TmnxChassisOverTempState_Type(Integer32):
    """Custom type tmnxChassisOverTempState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateOk", 1),
          ("stateOverTemp", 2))
    )


_TmnxChassisOverTempState_Type.__name__ = "Integer32"
_TmnxChassisOverTempState_Object = MibTableColumn
tmnxChassisOverTempState = _TmnxChassisOverTempState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 24),
    _TmnxChassisOverTempState_Type()
)
tmnxChassisOverTempState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisOverTempState.setStatus("current")


class _TmnxChassisMixedModeIomAdminMode_Type(TmnxEnabledDisabled):
    """Custom type tmnxChassisMixedModeIomAdminMode based on TmnxEnabledDisabled"""


_TmnxChassisMixedModeIomAdminMode_Object = MibTableColumn
tmnxChassisMixedModeIomAdminMode = _TmnxChassisMixedModeIomAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 25),
    _TmnxChassisMixedModeIomAdminMode_Type()
)
tmnxChassisMixedModeIomAdminMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisMixedModeIomAdminMode.setStatus("current")


class _TmnxChassisMixedModeIomUpgrList_Type(Bits):
    """Custom type tmnxChassisMixedModeIomUpgrList based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("iomSlot1", 0),
          ("iomSlot10", 9),
          ("iomSlot2", 1),
          ("iomSlot3", 2),
          ("iomSlot4", 3),
          ("iomSlot5", 4),
          ("iomSlot6", 5),
          ("iomSlot7", 6),
          ("iomSlot8", 7),
          ("iomSlot9", 8))
    )

_TmnxChassisMixedModeIomUpgrList_Type.__name__ = "Bits"
_TmnxChassisMixedModeIomUpgrList_Object = MibTableColumn
tmnxChassisMixedModeIomUpgrList = _TmnxChassisMixedModeIomUpgrList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 26),
    _TmnxChassisMixedModeIomUpgrList_Type()
)
tmnxChassisMixedModeIomUpgrList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisMixedModeIomUpgrList.setStatus("current")


class _TmnxChassisRedForcedSingleSfm_Type(TruthValue):
    """Custom type tmnxChassisRedForcedSingleSfm based on TruthValue"""


_TmnxChassisRedForcedSingleSfm_Object = MibTableColumn
tmnxChassisRedForcedSingleSfm = _TmnxChassisRedForcedSingleSfm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 3, 1, 27),
    _TmnxChassisRedForcedSingleSfm_Type()
)
tmnxChassisRedForcedSingleSfm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisRedForcedSingleSfm.setStatus("current")
_TmnxChassisFanTable_Object = MibTable
tmnxChassisFanTable = _TmnxChassisFanTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxChassisFanTable.setStatus("current")
_TmnxChassisFanEntry_Object = MibTableRow
tmnxChassisFanEntry = _TmnxChassisFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 4, 1)
)
tmnxChassisFanEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisFanIndex"),
)
if mibBuilder.loadTexts:
    tmnxChassisFanEntry.setStatus("current")


class _TmnxChassisFanIndex_Type(Unsigned32):
    """Custom type tmnxChassisFanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TmnxChassisFanIndex_Type.__name__ = "Unsigned32"
_TmnxChassisFanIndex_Object = MibTableColumn
tmnxChassisFanIndex = _TmnxChassisFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 4, 1, 1),
    _TmnxChassisFanIndex_Type()
)
tmnxChassisFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxChassisFanIndex.setStatus("current")
_TmnxChassisFanOperStatus_Type = TmnxDeviceState
_TmnxChassisFanOperStatus_Object = MibTableColumn
tmnxChassisFanOperStatus = _TmnxChassisFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 4, 1, 2),
    _TmnxChassisFanOperStatus_Type()
)
tmnxChassisFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisFanOperStatus.setStatus("current")


class _TmnxChassisFanSpeed_Type(Integer32):
    """Custom type tmnxChassisFanSpeed based on Integer32"""
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
        *(("fullSpeed", 3),
          ("halfSpeed", 2),
          ("lowSpeed", 4),
          ("notApplicable", 0),
          ("unknown", 1))
    )


_TmnxChassisFanSpeed_Type.__name__ = "Integer32"
_TmnxChassisFanSpeed_Object = MibTableColumn
tmnxChassisFanSpeed = _TmnxChassisFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 4, 1, 3),
    _TmnxChassisFanSpeed_Type()
)
tmnxChassisFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisFanSpeed.setStatus("current")


class _TmnxChassisFanRevision_Type(Integer32):
    """Custom type tmnxChassisFanRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fan1", 1),
          ("hfFan2", 2),
          ("unknown", 0))
    )


_TmnxChassisFanRevision_Type.__name__ = "Integer32"
_TmnxChassisFanRevision_Object = MibTableColumn
tmnxChassisFanRevision = _TmnxChassisFanRevision_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 4, 1, 4),
    _TmnxChassisFanRevision_Type()
)
tmnxChassisFanRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisFanRevision.setStatus("current")
_TmnxChassisPowerSupplyTable_Object = MibTable
tmnxChassisPowerSupplyTable = _TmnxChassisPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyTable.setStatus("current")
_TmnxChassisPowerSupplyEntry_Object = MibTableRow
tmnxChassisPowerSupplyEntry = _TmnxChassisPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1)
)
tmnxChassisPowerSupplyEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyId"),
)
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyEntry.setStatus("current")


class _TmnxChassisPowerSupplyId_Type(Unsigned32):
    """Custom type tmnxChassisPowerSupplyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TmnxChassisPowerSupplyId_Type.__name__ = "Unsigned32"
_TmnxChassisPowerSupplyId_Object = MibTableColumn
tmnxChassisPowerSupplyId = _TmnxChassisPowerSupplyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1, 1),
    _TmnxChassisPowerSupplyId_Type()
)
tmnxChassisPowerSupplyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyId.setStatus("current")
_TmnxChassisPowerSupplyACStatus_Type = TmnxDeviceState
_TmnxChassisPowerSupplyACStatus_Object = MibTableColumn
tmnxChassisPowerSupplyACStatus = _TmnxChassisPowerSupplyACStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1, 2),
    _TmnxChassisPowerSupplyACStatus_Type()
)
tmnxChassisPowerSupplyACStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyACStatus.setStatus("current")
_TmnxChassisPowerSupplyDCStatus_Type = TmnxDeviceState
_TmnxChassisPowerSupplyDCStatus_Object = MibTableColumn
tmnxChassisPowerSupplyDCStatus = _TmnxChassisPowerSupplyDCStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1, 3),
    _TmnxChassisPowerSupplyDCStatus_Type()
)
tmnxChassisPowerSupplyDCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyDCStatus.setStatus("current")
_TmnxChassisPowerSupplyTempStatus_Type = TmnxDeviceState
_TmnxChassisPowerSupplyTempStatus_Object = MibTableColumn
tmnxChassisPowerSupplyTempStatus = _TmnxChassisPowerSupplyTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1, 4),
    _TmnxChassisPowerSupplyTempStatus_Type()
)
tmnxChassisPowerSupplyTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyTempStatus.setStatus("current")
_TmnxChassisPowerSupplyTempThreshold_Type = Integer32
_TmnxChassisPowerSupplyTempThreshold_Object = MibTableColumn
tmnxChassisPowerSupplyTempThreshold = _TmnxChassisPowerSupplyTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1, 5),
    _TmnxChassisPowerSupplyTempThreshold_Type()
)
tmnxChassisPowerSupplyTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyTempThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyTempThreshold.setUnits("degrees celsius")
_TmnxChassisPowerSupply1Status_Type = TmnxDeviceState
_TmnxChassisPowerSupply1Status_Object = MibTableColumn
tmnxChassisPowerSupply1Status = _TmnxChassisPowerSupply1Status_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1, 6),
    _TmnxChassisPowerSupply1Status_Type()
)
tmnxChassisPowerSupply1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupply1Status.setStatus("current")
_TmnxChassisPowerSupply2Status_Type = TmnxDeviceState
_TmnxChassisPowerSupply2Status_Object = MibTableColumn
tmnxChassisPowerSupply2Status = _TmnxChassisPowerSupply2Status_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1, 7),
    _TmnxChassisPowerSupply2Status_Type()
)
tmnxChassisPowerSupply2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupply2Status.setStatus("current")


class _TmnxChassisPowerSupplyAssignedType_Type(Integer32):
    """Custom type tmnxChassisPowerSupplyAssignedType based on Integer32"""
    defaultValue = 4

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
        *(("acMultiple", 3),
          ("acSingle", 2),
          ("dc", 1),
          ("default", 4),
          ("none", 0))
    )


_TmnxChassisPowerSupplyAssignedType_Type.__name__ = "Integer32"
_TmnxChassisPowerSupplyAssignedType_Object = MibTableColumn
tmnxChassisPowerSupplyAssignedType = _TmnxChassisPowerSupplyAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1, 8),
    _TmnxChassisPowerSupplyAssignedType_Type()
)
tmnxChassisPowerSupplyAssignedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyAssignedType.setStatus("current")
_TmnxChassisPowerSupplyInputStatus_Type = TmnxDeviceState
_TmnxChassisPowerSupplyInputStatus_Object = MibTableColumn
tmnxChassisPowerSupplyInputStatus = _TmnxChassisPowerSupplyInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1, 9),
    _TmnxChassisPowerSupplyInputStatus_Type()
)
tmnxChassisPowerSupplyInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyInputStatus.setStatus("current")
_TmnxChassisPowerSupplyOutputStatus_Type = TmnxDeviceState
_TmnxChassisPowerSupplyOutputStatus_Object = MibTableColumn
tmnxChassisPowerSupplyOutputStatus = _TmnxChassisPowerSupplyOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1, 10),
    _TmnxChassisPowerSupplyOutputStatus_Type()
)
tmnxChassisPowerSupplyOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyOutputStatus.setStatus("current")
_TmnxChassisPowerSupplyPemType_Type = TmnxChassisPemType
_TmnxChassisPowerSupplyPemType_Object = MibTableColumn
tmnxChassisPowerSupplyPemType = _TmnxChassisPowerSupplyPemType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 5, 1, 11),
    _TmnxChassisPowerSupplyPemType_Type()
)
tmnxChassisPowerSupplyPemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisPowerSupplyPemType.setStatus("current")
_TmnxChassisTypeTable_Object = MibTable
tmnxChassisTypeTable = _TmnxChassisTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxChassisTypeTable.setStatus("current")
_TmnxChassisTypeEntry_Object = MibTableRow
tmnxChassisTypeEntry = _TmnxChassisTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 6, 1)
)
tmnxChassisTypeEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxChassisTypeEntry.setStatus("current")
_TmnxChassisTypeIndex_Type = TmnxChassisType
_TmnxChassisTypeIndex_Object = MibTableColumn
tmnxChassisTypeIndex = _TmnxChassisTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 6, 1, 1),
    _TmnxChassisTypeIndex_Type()
)
tmnxChassisTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxChassisTypeIndex.setStatus("current")
_TmnxChassisTypeName_Type = TNamedItemOrEmpty
_TmnxChassisTypeName_Object = MibTableColumn
tmnxChassisTypeName = _TmnxChassisTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 6, 1, 2),
    _TmnxChassisTypeName_Type()
)
tmnxChassisTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisTypeName.setStatus("current")
_TmnxChassisTypeDescription_Type = TItemDescription
_TmnxChassisTypeDescription_Object = MibTableColumn
tmnxChassisTypeDescription = _TmnxChassisTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 6, 1, 3),
    _TmnxChassisTypeDescription_Type()
)
tmnxChassisTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisTypeDescription.setStatus("current")
_TmnxChassisTypeStatus_Type = TruthValue
_TmnxChassisTypeStatus_Object = MibTableColumn
tmnxChassisTypeStatus = _TmnxChassisTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 6, 1, 4),
    _TmnxChassisTypeStatus_Type()
)
tmnxChassisTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisTypeStatus.setStatus("current")
_TmnxHwLastChange_Type = TimeStamp
_TmnxHwLastChange_Object = MibScalar
tmnxHwLastChange = _TmnxHwLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 7),
    _TmnxHwLastChange_Type()
)
tmnxHwLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwLastChange.setStatus("current")
_TmnxHwTable_Object = MibTable
tmnxHwTable = _TmnxHwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxHwTable.setStatus("current")
_TmnxHwEntry_Object = MibTableRow
tmnxHwEntry = _TmnxHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1)
)
tmnxHwEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxHwIndex"),
)
if mibBuilder.loadTexts:
    tmnxHwEntry.setStatus("current")
_TmnxHwIndex_Type = TmnxHwIndex
_TmnxHwIndex_Object = MibTableColumn
tmnxHwIndex = _TmnxHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 1),
    _TmnxHwIndex_Type()
)
tmnxHwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxHwIndex.setStatus("current")
_TmnxHwID_Type = RowPointer
_TmnxHwID_Object = MibTableColumn
tmnxHwID = _TmnxHwID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 2),
    _TmnxHwID_Type()
)
tmnxHwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwID.setStatus("current")


class _TmnxHwMfgString_Type(SnmpAdminString):
    """Custom type tmnxHwMfgString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_TmnxHwMfgString_Type.__name__ = "SnmpAdminString"
_TmnxHwMfgString_Object = MibTableColumn
tmnxHwMfgString = _TmnxHwMfgString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 3),
    _TmnxHwMfgString_Type()
)
tmnxHwMfgString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwMfgString.setStatus("current")


class _TmnxHwMfgBoardNumber_Type(OctetString):
    """Custom type tmnxHwMfgBoardNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxHwMfgBoardNumber_Type.__name__ = "OctetString"
_TmnxHwMfgBoardNumber_Object = MibTableColumn
tmnxHwMfgBoardNumber = _TmnxHwMfgBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 4),
    _TmnxHwMfgBoardNumber_Type()
)
tmnxHwMfgBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwMfgBoardNumber.setStatus("current")


class _TmnxHwSerialNumber_Type(SnmpAdminString):
    """Custom type tmnxHwSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxHwSerialNumber_Type.__name__ = "SnmpAdminString"
_TmnxHwSerialNumber_Object = MibTableColumn
tmnxHwSerialNumber = _TmnxHwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 5),
    _TmnxHwSerialNumber_Type()
)
tmnxHwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwSerialNumber.setStatus("current")


class _TmnxHwManufactureDate_Type(SnmpAdminString):
    """Custom type tmnxHwManufactureDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_TmnxHwManufactureDate_Type.__name__ = "SnmpAdminString"
_TmnxHwManufactureDate_Object = MibTableColumn
tmnxHwManufactureDate = _TmnxHwManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 6),
    _TmnxHwManufactureDate_Type()
)
tmnxHwManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwManufactureDate.setStatus("current")
_TmnxHwClass_Type = TmnxHwClass
_TmnxHwClass_Object = MibTableColumn
tmnxHwClass = _TmnxHwClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 7),
    _TmnxHwClass_Type()
)
tmnxHwClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwClass.setStatus("current")
_TmnxHwName_Type = TNamedItemOrEmpty
_TmnxHwName_Object = MibTableColumn
tmnxHwName = _TmnxHwName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 8),
    _TmnxHwName_Type()
)
tmnxHwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwName.setStatus("current")


class _TmnxHwAlias_Type(TNamedItemOrEmpty):
    """Custom type tmnxHwAlias based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxHwAlias_Object = MibTableColumn
tmnxHwAlias = _TmnxHwAlias_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 9),
    _TmnxHwAlias_Type()
)
tmnxHwAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxHwAlias.setStatus("current")


class _TmnxHwAssetID_Type(SnmpAdminString):
    """Custom type tmnxHwAssetID based on SnmpAdminString"""
    defaultHexValue = ""


_TmnxHwAssetID_Object = MibTableColumn
tmnxHwAssetID = _TmnxHwAssetID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 10),
    _TmnxHwAssetID_Type()
)
tmnxHwAssetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxHwAssetID.setStatus("current")


class _TmnxHwCLEI_Type(SnmpAdminString):
    """Custom type tmnxHwCLEI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_TmnxHwCLEI_Type.__name__ = "SnmpAdminString"
_TmnxHwCLEI_Object = MibTableColumn
tmnxHwCLEI = _TmnxHwCLEI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 11),
    _TmnxHwCLEI_Type()
)
tmnxHwCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwCLEI.setStatus("current")
_TmnxHwIsFRU_Type = TruthValue
_TmnxHwIsFRU_Object = MibTableColumn
tmnxHwIsFRU = _TmnxHwIsFRU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 12),
    _TmnxHwIsFRU_Type()
)
tmnxHwIsFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwIsFRU.setStatus("current")


class _TmnxHwContainedIn_Type(Integer32):
    """Custom type tmnxHwContainedIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxHwContainedIn_Type.__name__ = "Integer32"
_TmnxHwContainedIn_Object = MibTableColumn
tmnxHwContainedIn = _TmnxHwContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 13),
    _TmnxHwContainedIn_Type()
)
tmnxHwContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwContainedIn.setStatus("current")


class _TmnxHwParentRelPos_Type(Integer32):
    """Custom type tmnxHwParentRelPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_TmnxHwParentRelPos_Type.__name__ = "Integer32"
_TmnxHwParentRelPos_Object = MibTableColumn
tmnxHwParentRelPos = _TmnxHwParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 14),
    _TmnxHwParentRelPos_Type()
)
tmnxHwParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwParentRelPos.setStatus("current")


class _TmnxHwAdminState_Type(Integer32):
    """Custom type tmnxHwAdminState based on Integer32"""
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
        *(("diagnose", 4),
          ("inService", 2),
          ("noop", 1),
          ("operateSwitch", 5),
          ("outOfService", 3))
    )


_TmnxHwAdminState_Type.__name__ = "Integer32"
_TmnxHwAdminState_Object = MibTableColumn
tmnxHwAdminState = _TmnxHwAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 15),
    _TmnxHwAdminState_Type()
)
tmnxHwAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxHwAdminState.setStatus("current")


class _TmnxHwOperState_Type(Integer32):
    """Custom type tmnxHwOperState based on Integer32"""
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
        *(("booting", 6),
          ("diagnosing", 4),
          ("downgrade", 11),
          ("empty", 7),
          ("failed", 5),
          ("inService", 2),
          ("inServiceDowngrade", 13),
          ("inServiceUpgrade", 12),
          ("outOfService", 3),
          ("provisioned", 8),
          ("resetPending", 14),
          ("softReset", 15),
          ("unknown", 1),
          ("unprovisioned", 9),
          ("upgrade", 10))
    )


_TmnxHwOperState_Type.__name__ = "Integer32"
_TmnxHwOperState_Object = MibTableColumn
tmnxHwOperState = _TmnxHwOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 16),
    _TmnxHwOperState_Type()
)
tmnxHwOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwOperState.setStatus("current")
_TmnxHwTempSensor_Type = TruthValue
_TmnxHwTempSensor_Object = MibTableColumn
tmnxHwTempSensor = _TmnxHwTempSensor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 17),
    _TmnxHwTempSensor_Type()
)
tmnxHwTempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwTempSensor.setStatus("current")
_TmnxHwTemperature_Type = Integer32
_TmnxHwTemperature_Object = MibTableColumn
tmnxHwTemperature = _TmnxHwTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 18),
    _TmnxHwTemperature_Type()
)
tmnxHwTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHwTemperature.setUnits("degrees celsius")
_TmnxHwTempThreshold_Type = Integer32
_TmnxHwTempThreshold_Object = MibTableColumn
tmnxHwTempThreshold = _TmnxHwTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 19),
    _TmnxHwTempThreshold_Type()
)
tmnxHwTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwTempThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxHwTempThreshold.setUnits("degrees celsius")
_TmnxHwBootCodeVersion_Type = DisplayString
_TmnxHwBootCodeVersion_Object = MibTableColumn
tmnxHwBootCodeVersion = _TmnxHwBootCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 20),
    _TmnxHwBootCodeVersion_Type()
)
tmnxHwBootCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwBootCodeVersion.setStatus("current")
_TmnxHwSoftwareCodeVersion_Type = DisplayString
_TmnxHwSoftwareCodeVersion_Object = MibTableColumn
tmnxHwSoftwareCodeVersion = _TmnxHwSoftwareCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 21),
    _TmnxHwSoftwareCodeVersion_Type()
)
tmnxHwSoftwareCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwSoftwareCodeVersion.setStatus("current")
_TmnxHwSwLastBoot_Type = DateAndTime
_TmnxHwSwLastBoot_Object = MibTableColumn
tmnxHwSwLastBoot = _TmnxHwSwLastBoot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 22),
    _TmnxHwSwLastBoot_Type()
)
tmnxHwSwLastBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwSwLastBoot.setStatus("current")


class _TmnxHwSwState_Type(Integer32):
    """Custom type tmnxHwSwState based on Integer32"""
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
        *(("hwFailure", 1),
          ("hwInitting", 3),
          ("swDownloading", 4),
          ("swFailure", 2),
          ("swInitted", 6),
          ("swInitting", 5),
          ("swRunning", 7),
          ("unknown", 0))
    )


_TmnxHwSwState_Type.__name__ = "Integer32"
_TmnxHwSwState_Object = MibTableColumn
tmnxHwSwState = _TmnxHwSwState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 23),
    _TmnxHwSwState_Type()
)
tmnxHwSwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwSwState.setStatus("obsolete")
_TmnxHwAlarmState_Type = TmnxAlarmState
_TmnxHwAlarmState_Object = MibTableColumn
tmnxHwAlarmState = _TmnxHwAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 24),
    _TmnxHwAlarmState_Type()
)
tmnxHwAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwAlarmState.setStatus("current")
_TmnxHwLastAlarmEvent_Type = RowPointer
_TmnxHwLastAlarmEvent_Object = MibTableColumn
tmnxHwLastAlarmEvent = _TmnxHwLastAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 25),
    _TmnxHwLastAlarmEvent_Type()
)
tmnxHwLastAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwLastAlarmEvent.setStatus("current")


class _TmnxHwClearAlarms_Type(TmnxActionType):
    """Custom type tmnxHwClearAlarms based on TmnxActionType"""


_TmnxHwClearAlarms_Object = MibTableColumn
tmnxHwClearAlarms = _TmnxHwClearAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 26),
    _TmnxHwClearAlarms_Type()
)
tmnxHwClearAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxHwClearAlarms.setStatus("current")


class _TmnxHwSwImageSource_Type(Integer32):
    """Custom type tmnxHwSwImageSource based on Integer32"""
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
        *(("primary", 1),
          ("secondary", 2),
          ("tertiary", 3),
          ("unknown", 0))
    )


_TmnxHwSwImageSource_Type.__name__ = "Integer32"
_TmnxHwSwImageSource_Object = MibTableColumn
tmnxHwSwImageSource = _TmnxHwSwImageSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 27),
    _TmnxHwSwImageSource_Type()
)
tmnxHwSwImageSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwSwImageSource.setStatus("current")
_TmnxHwMfgDeviations_Type = SnmpAdminString
_TmnxHwMfgDeviations_Object = MibTableColumn
tmnxHwMfgDeviations = _TmnxHwMfgDeviations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 28),
    _TmnxHwMfgDeviations_Type()
)
tmnxHwMfgDeviations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwMfgDeviations.setStatus("current")
_TmnxHwBaseMacAddress_Type = MacAddress
_TmnxHwBaseMacAddress_Object = MibTableColumn
tmnxHwBaseMacAddress = _TmnxHwBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 29),
    _TmnxHwBaseMacAddress_Type()
)
tmnxHwBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwBaseMacAddress.setStatus("current")
_TmnxHwFailureReason_Type = DisplayString
_TmnxHwFailureReason_Object = MibTableColumn
tmnxHwFailureReason = _TmnxHwFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 30),
    _TmnxHwFailureReason_Type()
)
tmnxHwFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwFailureReason.setStatus("current")


class _TmnxHwEquippedPlatform_Type(Integer32):
    """Custom type tmnxHwEquippedPlatform based on Integer32"""
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
        *(("pf7450", 2),
          ("pf7710", 3),
          ("pf7750", 1),
          ("pfUnknown", 0))
    )


_TmnxHwEquippedPlatform_Type.__name__ = "Integer32"
_TmnxHwEquippedPlatform_Object = MibTableColumn
tmnxHwEquippedPlatform = _TmnxHwEquippedPlatform_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 31),
    _TmnxHwEquippedPlatform_Type()
)
tmnxHwEquippedPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwEquippedPlatform.setStatus("current")


class _TmnxHwMfgAssemblyNumber_Type(SnmpAdminString):
    """Custom type tmnxHwMfgAssemblyNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxHwMfgAssemblyNumber_Type.__name__ = "SnmpAdminString"
_TmnxHwMfgAssemblyNumber_Object = MibTableColumn
tmnxHwMfgAssemblyNumber = _TmnxHwMfgAssemblyNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 32),
    _TmnxHwMfgAssemblyNumber_Type()
)
tmnxHwMfgAssemblyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwMfgAssemblyNumber.setStatus("current")
_TmnxHwFirmwareCodeVersion_Type = DisplayString
_TmnxHwFirmwareCodeVersion_Object = MibTableColumn
tmnxHwFirmwareCodeVersion = _TmnxHwFirmwareCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 8, 1, 33),
    _TmnxHwFirmwareCodeVersion_Type()
)
tmnxHwFirmwareCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwFirmwareCodeVersion.setStatus("current")
_TmnxHwContainsTable_Object = MibTable
tmnxHwContainsTable = _TmnxHwContainsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxHwContainsTable.setStatus("current")
_TmnxHwContainsEntry_Object = MibTableRow
tmnxHwContainsEntry = _TmnxHwContainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 9, 1)
)
tmnxHwContainsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxHwIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxHwContainedIndex"),
)
if mibBuilder.loadTexts:
    tmnxHwContainsEntry.setStatus("current")
_TmnxHwContainedIndex_Type = TmnxHwIndex
_TmnxHwContainedIndex_Object = MibTableColumn
tmnxHwContainedIndex = _TmnxHwContainedIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 9, 1, 1),
    _TmnxHwContainedIndex_Type()
)
tmnxHwContainedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwContainedIndex.setStatus("current")
_TmnxCcmTable_Object = MibTable
tmnxCcmTable = _TmnxCcmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxCcmTable.setStatus("current")
_TmnxCcmEntry_Object = MibTableRow
tmnxCcmEntry = _TmnxCcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 10, 1)
)
tmnxCcmEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCcmIndex"),
)
if mibBuilder.loadTexts:
    tmnxCcmEntry.setStatus("current")


class _TmnxCcmIndex_Type(Unsigned32):
    """Custom type tmnxCcmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxCcmIndex_Type.__name__ = "Unsigned32"
_TmnxCcmIndex_Object = MibTableColumn
tmnxCcmIndex = _TmnxCcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 10, 1, 1),
    _TmnxCcmIndex_Type()
)
tmnxCcmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCcmIndex.setStatus("current")
_TmnxCcmOperStatus_Type = TmnxDeviceState
_TmnxCcmOperStatus_Object = MibTableColumn
tmnxCcmOperStatus = _TmnxCcmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 10, 1, 2),
    _TmnxCcmOperStatus_Type()
)
tmnxCcmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcmOperStatus.setStatus("current")
_TmnxCcmHwIndex_Type = TmnxHwIndex
_TmnxCcmHwIndex_Object = MibTableColumn
tmnxCcmHwIndex = _TmnxCcmHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 10, 1, 3),
    _TmnxCcmHwIndex_Type()
)
tmnxCcmHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcmHwIndex.setStatus("current")
_TmnxCcmEquippedType_Type = TmnxCcmType
_TmnxCcmEquippedType_Object = MibTableColumn
tmnxCcmEquippedType = _TmnxCcmEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 10, 1, 4),
    _TmnxCcmEquippedType_Type()
)
tmnxCcmEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcmEquippedType.setStatus("current")
_TmnxCcmTypeTable_Object = MibTable
tmnxCcmTypeTable = _TmnxCcmTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxCcmTypeTable.setStatus("current")
_TmnxCcmTypeEntry_Object = MibTableRow
tmnxCcmTypeEntry = _TmnxCcmTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 11, 1)
)
tmnxCcmTypeEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCcmTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxCcmTypeEntry.setStatus("current")
_TmnxCcmTypeIndex_Type = TmnxCcmType
_TmnxCcmTypeIndex_Object = MibTableColumn
tmnxCcmTypeIndex = _TmnxCcmTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 11, 1, 1),
    _TmnxCcmTypeIndex_Type()
)
tmnxCcmTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCcmTypeIndex.setStatus("current")
_TmnxCcmTypeName_Type = TNamedItemOrEmpty
_TmnxCcmTypeName_Object = MibTableColumn
tmnxCcmTypeName = _TmnxCcmTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 11, 1, 2),
    _TmnxCcmTypeName_Type()
)
tmnxCcmTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcmTypeName.setStatus("current")
_TmnxCcmTypeDescription_Type = TItemDescription
_TmnxCcmTypeDescription_Object = MibTableColumn
tmnxCcmTypeDescription = _TmnxCcmTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 11, 1, 3),
    _TmnxCcmTypeDescription_Type()
)
tmnxCcmTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcmTypeDescription.setStatus("current")
_TmnxCcmTypeStatus_Type = TruthValue
_TmnxCcmTypeStatus_Object = MibTableColumn
tmnxCcmTypeStatus = _TmnxCcmTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 11, 1, 4),
    _TmnxCcmTypeStatus_Type()
)
tmnxCcmTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcmTypeStatus.setStatus("current")
_TmnxFanTrayComponentTable_Object = MibTable
tmnxFanTrayComponentTable = _TmnxFanTrayComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxFanTrayComponentTable.setStatus("current")
_TmnxFanTrayComponentEntry_Object = MibTableRow
tmnxFanTrayComponentEntry = _TmnxFanTrayComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 12, 1)
)
tmnxFanTrayComponentEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisFanIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFanTrayCompIndex"),
)
if mibBuilder.loadTexts:
    tmnxFanTrayComponentEntry.setStatus("current")
_TmnxFanTrayCompIndex_Type = Unsigned32
_TmnxFanTrayCompIndex_Object = MibTableColumn
tmnxFanTrayCompIndex = _TmnxFanTrayCompIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 12, 1, 1),
    _TmnxFanTrayCompIndex_Type()
)
tmnxFanTrayCompIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFanTrayCompIndex.setStatus("current")


class _TmnxFanTrayCompSpeed_Type(Gauge32):
    """Custom type tmnxFanTrayCompSpeed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxFanTrayCompSpeed_Type.__name__ = "Gauge32"
_TmnxFanTrayCompSpeed_Object = MibTableColumn
tmnxFanTrayCompSpeed = _TmnxFanTrayCompSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 12, 1, 2),
    _TmnxFanTrayCompSpeed_Type()
)
tmnxFanTrayCompSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFanTrayCompSpeed.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFanTrayCompSpeed.setUnits("percent")
_TmnxHwResourceTable_Object = MibTable
tmnxHwResourceTable = _TmnxHwResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxHwResourceTable.setStatus("current")
_TmnxHwResourceEntry_Object = MibTableRow
tmnxHwResourceEntry = _TmnxHwResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1)
)
tmnxHwResourceEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxHwIndex"),
)
if mibBuilder.loadTexts:
    tmnxHwResourceEntry.setStatus("current")
_TmnxHwResourceCurrentVoltage_Type = Integer32
_TmnxHwResourceCurrentVoltage_Object = MibTableColumn
tmnxHwResourceCurrentVoltage = _TmnxHwResourceCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 1),
    _TmnxHwResourceCurrentVoltage_Type()
)
tmnxHwResourceCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourceCurrentVoltage.setStatus("current")
_TmnxHwResourcePeakVoltage_Type = Integer32
_TmnxHwResourcePeakVoltage_Object = MibTableColumn
tmnxHwResourcePeakVoltage = _TmnxHwResourcePeakVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 2),
    _TmnxHwResourcePeakVoltage_Type()
)
tmnxHwResourcePeakVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourcePeakVoltage.setStatus("current")
_TmnxHwResourcePeakVoltageTime_Type = TimeStamp
_TmnxHwResourcePeakVoltageTime_Object = MibTableColumn
tmnxHwResourcePeakVoltageTime = _TmnxHwResourcePeakVoltageTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 3),
    _TmnxHwResourcePeakVoltageTime_Type()
)
tmnxHwResourcePeakVoltageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourcePeakVoltageTime.setStatus("current")
_TmnxHwResourceMinVoltage_Type = Integer32
_TmnxHwResourceMinVoltage_Object = MibTableColumn
tmnxHwResourceMinVoltage = _TmnxHwResourceMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 4),
    _TmnxHwResourceMinVoltage_Type()
)
tmnxHwResourceMinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourceMinVoltage.setStatus("current")
_TmnxHwResourceMinVoltageTime_Type = TimeStamp
_TmnxHwResourceMinVoltageTime_Object = MibTableColumn
tmnxHwResourceMinVoltageTime = _TmnxHwResourceMinVoltageTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 5),
    _TmnxHwResourceMinVoltageTime_Type()
)
tmnxHwResourceMinVoltageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourceMinVoltageTime.setStatus("current")
_TmnxHwResourceCurrentWattage_Type = Integer32
_TmnxHwResourceCurrentWattage_Object = MibTableColumn
tmnxHwResourceCurrentWattage = _TmnxHwResourceCurrentWattage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 6),
    _TmnxHwResourceCurrentWattage_Type()
)
tmnxHwResourceCurrentWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourceCurrentWattage.setStatus("current")
_TmnxHwResourcePeakWattage_Type = Integer32
_TmnxHwResourcePeakWattage_Object = MibTableColumn
tmnxHwResourcePeakWattage = _TmnxHwResourcePeakWattage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 7),
    _TmnxHwResourcePeakWattage_Type()
)
tmnxHwResourcePeakWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourcePeakWattage.setStatus("current")
_TmnxHwResourcePeakWattageTime_Type = TimeStamp
_TmnxHwResourcePeakWattageTime_Object = MibTableColumn
tmnxHwResourcePeakWattageTime = _TmnxHwResourcePeakWattageTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 8),
    _TmnxHwResourcePeakWattageTime_Type()
)
tmnxHwResourcePeakWattageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourcePeakWattageTime.setStatus("current")
_TmnxHwResourceMinWattage_Type = Integer32
_TmnxHwResourceMinWattage_Object = MibTableColumn
tmnxHwResourceMinWattage = _TmnxHwResourceMinWattage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 9),
    _TmnxHwResourceMinWattage_Type()
)
tmnxHwResourceMinWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourceMinWattage.setStatus("current")
_TmnxHwResourceMinWattageTime_Type = TimeStamp
_TmnxHwResourceMinWattageTime_Object = MibTableColumn
tmnxHwResourceMinWattageTime = _TmnxHwResourceMinWattageTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 10),
    _TmnxHwResourceMinWattageTime_Type()
)
tmnxHwResourceMinWattageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourceMinWattageTime.setStatus("current")
_TmnxHwResourceCurrentAmperage_Type = Integer32
_TmnxHwResourceCurrentAmperage_Object = MibTableColumn
tmnxHwResourceCurrentAmperage = _TmnxHwResourceCurrentAmperage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 11),
    _TmnxHwResourceCurrentAmperage_Type()
)
tmnxHwResourceCurrentAmperage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourceCurrentAmperage.setStatus("current")
_TmnxHwResourcePeakAmperage_Type = Integer32
_TmnxHwResourcePeakAmperage_Object = MibTableColumn
tmnxHwResourcePeakAmperage = _TmnxHwResourcePeakAmperage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 12),
    _TmnxHwResourcePeakAmperage_Type()
)
tmnxHwResourcePeakAmperage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourcePeakAmperage.setStatus("current")
_TmnxHwResourcePeakAmperageTime_Type = TimeStamp
_TmnxHwResourcePeakAmperageTime_Object = MibTableColumn
tmnxHwResourcePeakAmperageTime = _TmnxHwResourcePeakAmperageTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 13),
    _TmnxHwResourcePeakAmperageTime_Type()
)
tmnxHwResourcePeakAmperageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourcePeakAmperageTime.setStatus("current")
_TmnxHwResourceMinAmperage_Type = Integer32
_TmnxHwResourceMinAmperage_Object = MibTableColumn
tmnxHwResourceMinAmperage = _TmnxHwResourceMinAmperage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 14),
    _TmnxHwResourceMinAmperage_Type()
)
tmnxHwResourceMinAmperage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourceMinAmperage.setStatus("current")
_TmnxHwResourceMinAmperageTime_Type = TimeStamp
_TmnxHwResourceMinAmperageTime_Object = MibTableColumn
tmnxHwResourceMinAmperageTime = _TmnxHwResourceMinAmperageTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 1, 13, 1, 15),
    _TmnxHwResourceMinAmperageTime_Type()
)
tmnxHwResourceMinAmperageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHwResourceMinAmperageTime.setStatus("current")
_TmnxSlotObjs_ObjectIdentity = ObjectIdentity
tmnxSlotObjs = _TmnxSlotObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 2)
)
_TmnxCardObjs_ObjectIdentity = ObjectIdentity
tmnxCardObjs = _TmnxCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3)
)
_TmnxCardLastChange_Type = TimeStamp
_TmnxCardLastChange_Object = MibScalar
tmnxCardLastChange = _TmnxCardLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 1),
    _TmnxCardLastChange_Type()
)
tmnxCardLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardLastChange.setStatus("current")
_TmnxCardTable_Object = MibTable
tmnxCardTable = _TmnxCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxCardTable.setStatus("current")
_TmnxCardEntry_Object = MibTableRow
tmnxCardEntry = _TmnxCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1)
)
tmnxCardEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxCardEntry.setStatus("current")
_TmnxCardSlotNum_Type = TmnxSlotNum
_TmnxCardSlotNum_Object = MibTableColumn
tmnxCardSlotNum = _TmnxCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 1),
    _TmnxCardSlotNum_Type()
)
tmnxCardSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCardSlotNum.setStatus("current")
_TmnxCardSupportedTypes_Type = TmnxCardSuppType
_TmnxCardSupportedTypes_Object = MibTableColumn
tmnxCardSupportedTypes = _TmnxCardSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 2),
    _TmnxCardSupportedTypes_Type()
)
tmnxCardSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardSupportedTypes.setStatus("current")
_TmnxCardAllowedTypes_Type = TmnxCardType
_TmnxCardAllowedTypes_Object = MibTableColumn
tmnxCardAllowedTypes = _TmnxCardAllowedTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 3),
    _TmnxCardAllowedTypes_Type()
)
tmnxCardAllowedTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardAllowedTypes.setStatus("obsolete")


class _TmnxCardAssignedType_Type(TmnxCardType):
    """Custom type tmnxCardAssignedType based on TmnxCardType"""
    defaultValue = 1


_TmnxCardAssignedType_Object = MibTableColumn
tmnxCardAssignedType = _TmnxCardAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 4),
    _TmnxCardAssignedType_Type()
)
tmnxCardAssignedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardAssignedType.setStatus("current")
_TmnxCardEquippedType_Type = TmnxCardType
_TmnxCardEquippedType_Object = MibTableColumn
tmnxCardEquippedType = _TmnxCardEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 5),
    _TmnxCardEquippedType_Type()
)
tmnxCardEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardEquippedType.setStatus("current")
_TmnxCardHwIndex_Type = TmnxHwIndex
_TmnxCardHwIndex_Object = MibTableColumn
tmnxCardHwIndex = _TmnxCardHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 6),
    _TmnxCardHwIndex_Type()
)
tmnxCardHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardHwIndex.setStatus("current")
_TmnxCardClockSource_Type = TItemDescription
_TmnxCardClockSource_Object = MibTableColumn
tmnxCardClockSource = _TmnxCardClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 10),
    _TmnxCardClockSource_Type()
)
tmnxCardClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardClockSource.setStatus("current")
_TmnxCardNumMdaSlots_Type = Unsigned32
_TmnxCardNumMdaSlots_Object = MibTableColumn
tmnxCardNumMdaSlots = _TmnxCardNumMdaSlots_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 11),
    _TmnxCardNumMdaSlots_Type()
)
tmnxCardNumMdaSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardNumMdaSlots.setStatus("current")
_TmnxCardNumMdas_Type = Unsigned32
_TmnxCardNumMdas_Object = MibTableColumn
tmnxCardNumMdas = _TmnxCardNumMdas_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 12),
    _TmnxCardNumMdas_Type()
)
tmnxCardNumMdas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardNumMdas.setStatus("current")


class _TmnxCardReboot_Type(TmnxCardRebootType):
    """Custom type tmnxCardReboot based on TmnxCardRebootType"""


_TmnxCardReboot_Object = MibTableColumn
tmnxCardReboot = _TmnxCardReboot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 13),
    _TmnxCardReboot_Type()
)
tmnxCardReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardReboot.setStatus("current")
_TmnxCardMemorySize_Type = Unsigned32
_TmnxCardMemorySize_Object = MibTableColumn
tmnxCardMemorySize = _TmnxCardMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 14),
    _TmnxCardMemorySize_Type()
)
tmnxCardMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCardMemorySize.setUnits("Mega-bytes")


class _TmnxCardNamedPoolAdminMode_Type(TmnxAdminState):
    """Custom type tmnxCardNamedPoolAdminMode based on TmnxAdminState"""


_TmnxCardNamedPoolAdminMode_Object = MibTableColumn
tmnxCardNamedPoolAdminMode = _TmnxCardNamedPoolAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 15),
    _TmnxCardNamedPoolAdminMode_Type()
)
tmnxCardNamedPoolAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardNamedPoolAdminMode.setStatus("current")


class _TmnxCardNamedPoolOperMode_Type(TmnxAdminState):
    """Custom type tmnxCardNamedPoolOperMode based on TmnxAdminState"""


_TmnxCardNamedPoolOperMode_Object = MibTableColumn
tmnxCardNamedPoolOperMode = _TmnxCardNamedPoolOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 16),
    _TmnxCardNamedPoolOperMode_Type()
)
tmnxCardNamedPoolOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardNamedPoolOperMode.setStatus("current")


class _TmnxCardSoftReset_Type(TmnxActionType):
    """Custom type tmnxCardSoftReset based on TmnxActionType"""


_TmnxCardSoftReset_Object = MibTableColumn
tmnxCardSoftReset = _TmnxCardSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 17),
    _TmnxCardSoftReset_Type()
)
tmnxCardSoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardSoftReset.setStatus("current")


class _TmnxCardLastBootupReason_Type(Integer32):
    """Custom type tmnxCardLastBootupReason based on Integer32"""
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
        *(("activitySwitch", 4),
          ("bootFail", 7),
          ("ccmFail", 12),
          ("clearCard", 3),
          ("configChange", 5),
          ("hardReboot", 0),
          ("issuHardReboot", 11),
          ("issuTimeout", 9),
          ("powerCycle", 2),
          ("reinserted", 10),
          ("runtimeFail", 6),
          ("softReset", 1),
          ("unexpected", 8))
    )


_TmnxCardLastBootupReason_Type.__name__ = "Integer32"
_TmnxCardLastBootupReason_Object = MibTableColumn
tmnxCardLastBootupReason = _TmnxCardLastBootupReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 18),
    _TmnxCardLastBootupReason_Type()
)
tmnxCardLastBootupReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardLastBootupReason.setStatus("current")
_TmnxCardCmplx1IngrFcsOccur_Type = Counter32
_TmnxCardCmplx1IngrFcsOccur_Object = MibTableColumn
tmnxCardCmplx1IngrFcsOccur = _TmnxCardCmplx1IngrFcsOccur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 19),
    _TmnxCardCmplx1IngrFcsOccur_Type()
)
tmnxCardCmplx1IngrFcsOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx1IngrFcsOccur.setStatus("current")
_TmnxCardCmplx1IngrFcsOccurTime_Type = TimeStamp
_TmnxCardCmplx1IngrFcsOccurTime_Object = MibTableColumn
tmnxCardCmplx1IngrFcsOccurTime = _TmnxCardCmplx1IngrFcsOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 20),
    _TmnxCardCmplx1IngrFcsOccurTime_Type()
)
tmnxCardCmplx1IngrFcsOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx1IngrFcsOccurTime.setStatus("current")
_TmnxCardCmplx1EgrFcsOccur_Type = Counter32
_TmnxCardCmplx1EgrFcsOccur_Object = MibTableColumn
tmnxCardCmplx1EgrFcsOccur = _TmnxCardCmplx1EgrFcsOccur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 21),
    _TmnxCardCmplx1EgrFcsOccur_Type()
)
tmnxCardCmplx1EgrFcsOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx1EgrFcsOccur.setStatus("current")
_TmnxCardCmplx1EgrFcsOccurTime_Type = TimeStamp
_TmnxCardCmplx1EgrFcsOccurTime_Object = MibTableColumn
tmnxCardCmplx1EgrFcsOccurTime = _TmnxCardCmplx1EgrFcsOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 22),
    _TmnxCardCmplx1EgrFcsOccurTime_Type()
)
tmnxCardCmplx1EgrFcsOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx1EgrFcsOccurTime.setStatus("current")
_TmnxCardCmplx2IngrFcsOccur_Type = Counter32
_TmnxCardCmplx2IngrFcsOccur_Object = MibTableColumn
tmnxCardCmplx2IngrFcsOccur = _TmnxCardCmplx2IngrFcsOccur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 23),
    _TmnxCardCmplx2IngrFcsOccur_Type()
)
tmnxCardCmplx2IngrFcsOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx2IngrFcsOccur.setStatus("current")
_TmnxCardCmplx2IngrFcsOccurTime_Type = TimeStamp
_TmnxCardCmplx2IngrFcsOccurTime_Object = MibTableColumn
tmnxCardCmplx2IngrFcsOccurTime = _TmnxCardCmplx2IngrFcsOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 24),
    _TmnxCardCmplx2IngrFcsOccurTime_Type()
)
tmnxCardCmplx2IngrFcsOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx2IngrFcsOccurTime.setStatus("current")
_TmnxCardCmplx2EgrFcsOccur_Type = Counter32
_TmnxCardCmplx2EgrFcsOccur_Object = MibTableColumn
tmnxCardCmplx2EgrFcsOccur = _TmnxCardCmplx2EgrFcsOccur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 25),
    _TmnxCardCmplx2EgrFcsOccur_Type()
)
tmnxCardCmplx2EgrFcsOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx2EgrFcsOccur.setStatus("current")
_TmnxCardCmplx2EgrFcsOccurTime_Type = TimeStamp
_TmnxCardCmplx2EgrFcsOccurTime_Object = MibTableColumn
tmnxCardCmplx2EgrFcsOccurTime = _TmnxCardCmplx2EgrFcsOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 26),
    _TmnxCardCmplx2EgrFcsOccurTime_Type()
)
tmnxCardCmplx2EgrFcsOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx2EgrFcsOccurTime.setStatus("current")
_TmnxCardCmplx1MemParityOccur_Type = Counter32
_TmnxCardCmplx1MemParityOccur_Object = MibTableColumn
tmnxCardCmplx1MemParityOccur = _TmnxCardCmplx1MemParityOccur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 27),
    _TmnxCardCmplx1MemParityOccur_Type()
)
tmnxCardCmplx1MemParityOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx1MemParityOccur.setStatus("current")
_TmnxCardCmplx1MemParityOccurTime_Type = TimeStamp
_TmnxCardCmplx1MemParityOccurTime_Object = MibTableColumn
tmnxCardCmplx1MemParityOccurTime = _TmnxCardCmplx1MemParityOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 28),
    _TmnxCardCmplx1MemParityOccurTime_Type()
)
tmnxCardCmplx1MemParityOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx1MemParityOccurTime.setStatus("current")
_TmnxCardCmplx2MemParityOccur_Type = Counter32
_TmnxCardCmplx2MemParityOccur_Object = MibTableColumn
tmnxCardCmplx2MemParityOccur = _TmnxCardCmplx2MemParityOccur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 29),
    _TmnxCardCmplx2MemParityOccur_Type()
)
tmnxCardCmplx2MemParityOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx2MemParityOccur.setStatus("current")
_TmnxCardCmplx2MemParityOccurTime_Type = TimeStamp
_TmnxCardCmplx2MemParityOccurTime_Object = MibTableColumn
tmnxCardCmplx2MemParityOccurTime = _TmnxCardCmplx2MemParityOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 30),
    _TmnxCardCmplx2MemParityOccurTime_Type()
)
tmnxCardCmplx2MemParityOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx2MemParityOccurTime.setStatus("current")


class _TmnxCardCapability_Type(Bits):
    """Custom type tmnxCardCapability based on Bits"""
    namedValues = NamedValues(
        ("sr", 0)
    )

_TmnxCardCapability_Type.__name__ = "Bits"
_TmnxCardCapability_Object = MibTableColumn
tmnxCardCapability = _TmnxCardCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 31),
    _TmnxCardCapability_Type()
)
tmnxCardCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardCapability.setStatus("current")
_TmnxCardCmplx1CAMErrorOccur_Type = Counter32
_TmnxCardCmplx1CAMErrorOccur_Object = MibTableColumn
tmnxCardCmplx1CAMErrorOccur = _TmnxCardCmplx1CAMErrorOccur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 32),
    _TmnxCardCmplx1CAMErrorOccur_Type()
)
tmnxCardCmplx1CAMErrorOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx1CAMErrorOccur.setStatus("current")
_TmnxCardCmplx1CAMErrorOccurTime_Type = TimeStamp
_TmnxCardCmplx1CAMErrorOccurTime_Object = MibTableColumn
tmnxCardCmplx1CAMErrorOccurTime = _TmnxCardCmplx1CAMErrorOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 33),
    _TmnxCardCmplx1CAMErrorOccurTime_Type()
)
tmnxCardCmplx1CAMErrorOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx1CAMErrorOccurTime.setStatus("current")
_TmnxCardCmplx2CAMErrorOccur_Type = Counter32
_TmnxCardCmplx2CAMErrorOccur_Object = MibTableColumn
tmnxCardCmplx2CAMErrorOccur = _TmnxCardCmplx2CAMErrorOccur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 34),
    _TmnxCardCmplx2CAMErrorOccur_Type()
)
tmnxCardCmplx2CAMErrorOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx2CAMErrorOccur.setStatus("current")
_TmnxCardCmplx2CAMErrorOccurTime_Type = TimeStamp
_TmnxCardCmplx2CAMErrorOccurTime_Object = MibTableColumn
tmnxCardCmplx2CAMErrorOccurTime = _TmnxCardCmplx2CAMErrorOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 35),
    _TmnxCardCmplx2CAMErrorOccurTime_Type()
)
tmnxCardCmplx2CAMErrorOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx2CAMErrorOccurTime.setStatus("current")


class _TmnxCardFailOnError_Type(Bits):
    """Custom type tmnxCardFailOnError based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("memoryEventGroupA", 0)
    )

_TmnxCardFailOnError_Type.__name__ = "Bits"
_TmnxCardFailOnError_Object = MibTableColumn
tmnxCardFailOnError = _TmnxCardFailOnError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 36),
    _TmnxCardFailOnError_Type()
)
tmnxCardFailOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardFailOnError.setStatus("current")
_TmnxCardCmplx1EgrFcsSrcSlots_Type = TmnxCardSlotBitMap
_TmnxCardCmplx1EgrFcsSrcSlots_Object = MibTableColumn
tmnxCardCmplx1EgrFcsSrcSlots = _TmnxCardCmplx1EgrFcsSrcSlots_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 37),
    _TmnxCardCmplx1EgrFcsSrcSlots_Type()
)
tmnxCardCmplx1EgrFcsSrcSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx1EgrFcsSrcSlots.setStatus("current")
_TmnxCardCmplx2EgrFcsSrcSlots_Type = TmnxCardSlotBitMap
_TmnxCardCmplx2EgrFcsSrcSlots_Object = MibTableColumn
tmnxCardCmplx2EgrFcsSrcSlots = _TmnxCardCmplx2EgrFcsSrcSlots_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 38),
    _TmnxCardCmplx2EgrFcsSrcSlots_Type()
)
tmnxCardCmplx2EgrFcsSrcSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardCmplx2EgrFcsSrcSlots.setStatus("current")


class _TmnxCardHardResetUnsupMdas_Type(TruthValue):
    """Custom type tmnxCardHardResetUnsupMdas based on TruthValue"""


_TmnxCardHardResetUnsupMdas_Object = MibTableColumn
tmnxCardHardResetUnsupMdas = _TmnxCardHardResetUnsupMdas_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 2, 1, 39),
    _TmnxCardHardResetUnsupMdas_Type()
)
tmnxCardHardResetUnsupMdas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardHardResetUnsupMdas.setStatus("current")
_TmnxCpmCardLastChange_Type = TimeStamp
_TmnxCpmCardLastChange_Object = MibScalar
tmnxCpmCardLastChange = _TmnxCpmCardLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 3),
    _TmnxCpmCardLastChange_Type()
)
tmnxCpmCardLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardLastChange.setStatus("current")
_TmnxCpmCardTable_Object = MibTable
tmnxCpmCardTable = _TmnxCpmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxCpmCardTable.setStatus("current")
_TmnxCpmCardEntry_Object = MibTableRow
tmnxCpmCardEntry = _TmnxCpmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1)
)
tmnxCpmCardEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCpmCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCpmCardNum"),
)
if mibBuilder.loadTexts:
    tmnxCpmCardEntry.setStatus("current")
_TmnxCpmCardSlotNum_Type = TmnxSlotNum
_TmnxCpmCardSlotNum_Object = MibTableColumn
tmnxCpmCardSlotNum = _TmnxCpmCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 1),
    _TmnxCpmCardSlotNum_Type()
)
tmnxCpmCardSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmCardSlotNum.setStatus("current")
_TmnxCpmCardNum_Type = Unsigned32
_TmnxCpmCardNum_Object = MibTableColumn
tmnxCpmCardNum = _TmnxCpmCardNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 2),
    _TmnxCpmCardNum_Type()
)
tmnxCpmCardNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmCardNum.setStatus("current")
_TmnxCpmCardSupportedTypes_Type = TmnxCardSuppType
_TmnxCpmCardSupportedTypes_Object = MibTableColumn
tmnxCpmCardSupportedTypes = _TmnxCpmCardSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 3),
    _TmnxCpmCardSupportedTypes_Type()
)
tmnxCpmCardSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardSupportedTypes.setStatus("current")
_TmnxCpmCardAllowedTypes_Type = TmnxCardType
_TmnxCpmCardAllowedTypes_Object = MibTableColumn
tmnxCpmCardAllowedTypes = _TmnxCpmCardAllowedTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 4),
    _TmnxCpmCardAllowedTypes_Type()
)
tmnxCpmCardAllowedTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmCardAllowedTypes.setStatus("obsolete")


class _TmnxCpmCardAssignedType_Type(TmnxCardType):
    """Custom type tmnxCpmCardAssignedType based on TmnxCardType"""
    defaultValue = 1


_TmnxCpmCardAssignedType_Object = MibTableColumn
tmnxCpmCardAssignedType = _TmnxCpmCardAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 5),
    _TmnxCpmCardAssignedType_Type()
)
tmnxCpmCardAssignedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmCardAssignedType.setStatus("current")
_TmnxCpmCardEquippedType_Type = TmnxCardType
_TmnxCpmCardEquippedType_Object = MibTableColumn
tmnxCpmCardEquippedType = _TmnxCpmCardEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 6),
    _TmnxCpmCardEquippedType_Type()
)
tmnxCpmCardEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardEquippedType.setStatus("current")
_TmnxCpmCardHwIndex_Type = TmnxHwIndex
_TmnxCpmCardHwIndex_Object = MibTableColumn
tmnxCpmCardHwIndex = _TmnxCpmCardHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 7),
    _TmnxCpmCardHwIndex_Type()
)
tmnxCpmCardHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardHwIndex.setStatus("current")
_TmnxCpmCardBootOptionVersion_Type = TItemDescription
_TmnxCpmCardBootOptionVersion_Object = MibTableColumn
tmnxCpmCardBootOptionVersion = _TmnxCpmCardBootOptionVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 8),
    _TmnxCpmCardBootOptionVersion_Type()
)
tmnxCpmCardBootOptionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardBootOptionVersion.setStatus("current")
_TmnxCpmCardBootOptionLastModified_Type = DateAndTime
_TmnxCpmCardBootOptionLastModified_Object = MibTableColumn
tmnxCpmCardBootOptionLastModified = _TmnxCpmCardBootOptionLastModified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 9),
    _TmnxCpmCardBootOptionLastModified_Type()
)
tmnxCpmCardBootOptionLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardBootOptionLastModified.setStatus("current")
_TmnxCpmCardConfigBootedVersion_Type = TItemDescription
_TmnxCpmCardConfigBootedVersion_Object = MibTableColumn
tmnxCpmCardConfigBootedVersion = _TmnxCpmCardConfigBootedVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 10),
    _TmnxCpmCardConfigBootedVersion_Type()
)
tmnxCpmCardConfigBootedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardConfigBootedVersion.setStatus("current")
_TmnxCpmCardIndexBootedVersion_Type = TItemDescription
_TmnxCpmCardIndexBootedVersion_Object = MibTableColumn
tmnxCpmCardIndexBootedVersion = _TmnxCpmCardIndexBootedVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 11),
    _TmnxCpmCardIndexBootedVersion_Type()
)
tmnxCpmCardIndexBootedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardIndexBootedVersion.setStatus("current")
_TmnxCpmCardConfigLastModified_Type = DateAndTime
_TmnxCpmCardConfigLastModified_Object = MibTableColumn
tmnxCpmCardConfigLastModified = _TmnxCpmCardConfigLastModified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 12),
    _TmnxCpmCardConfigLastModified_Type()
)
tmnxCpmCardConfigLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardConfigLastModified.setStatus("current")
_TmnxCpmCardConfigLastSaved_Type = DateAndTime
_TmnxCpmCardConfigLastSaved_Object = MibTableColumn
tmnxCpmCardConfigLastSaved = _TmnxCpmCardConfigLastSaved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 13),
    _TmnxCpmCardConfigLastSaved_Type()
)
tmnxCpmCardConfigLastSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardConfigLastSaved.setStatus("current")


class _TmnxCpmCardRedundant_Type(Integer32):
    """Custom type tmnxCpmCardRedundant based on Integer32"""
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
        *(("redundantActive", 2),
          ("redundantDisabled", 5),
          ("redundantSplit", 4),
          ("redundantStandby", 3),
          ("redundantSyncing", 6),
          ("singleton", 1))
    )


_TmnxCpmCardRedundant_Type.__name__ = "Integer32"
_TmnxCpmCardRedundant_Object = MibTableColumn
tmnxCpmCardRedundant = _TmnxCpmCardRedundant_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 14),
    _TmnxCpmCardRedundant_Type()
)
tmnxCpmCardRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardRedundant.setStatus("current")
_TmnxCpmCardClockSource_Type = TItemDescription
_TmnxCpmCardClockSource_Object = MibTableColumn
tmnxCpmCardClockSource = _TmnxCpmCardClockSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 15),
    _TmnxCpmCardClockSource_Type()
)
tmnxCpmCardClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardClockSource.setStatus("current")
_TmnxCpmCardNumCpus_Type = Unsigned32
_TmnxCpmCardNumCpus_Object = MibTableColumn
tmnxCpmCardNumCpus = _TmnxCpmCardNumCpus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 16),
    _TmnxCpmCardNumCpus_Type()
)
tmnxCpmCardNumCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardNumCpus.setStatus("current")


class _TmnxCpmCardCpuType_Type(Integer32):
    """Custom type tmnxCpmCardCpuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mips", 2),
          ("pentium-pc", 3),
          ("unknown", 1))
    )


_TmnxCpmCardCpuType_Type.__name__ = "Integer32"
_TmnxCpmCardCpuType_Object = MibTableColumn
tmnxCpmCardCpuType = _TmnxCpmCardCpuType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 17),
    _TmnxCpmCardCpuType_Type()
)
tmnxCpmCardCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardCpuType.setStatus("current")
_TmnxCpmCardMemorySize_Type = Unsigned32
_TmnxCpmCardMemorySize_Object = MibTableColumn
tmnxCpmCardMemorySize = _TmnxCpmCardMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 18),
    _TmnxCpmCardMemorySize_Type()
)
tmnxCpmCardMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCpmCardMemorySize.setUnits("Mega-bytes")


class _TmnxCpmCardSwitchToRedundantCard_Type(TmnxActionType):
    """Custom type tmnxCpmCardSwitchToRedundantCard based on TmnxActionType"""


_TmnxCpmCardSwitchToRedundantCard_Object = MibTableColumn
tmnxCpmCardSwitchToRedundantCard = _TmnxCpmCardSwitchToRedundantCard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 19),
    _TmnxCpmCardSwitchToRedundantCard_Type()
)
tmnxCpmCardSwitchToRedundantCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmCardSwitchToRedundantCard.setStatus("current")


class _TmnxCpmCardReboot_Type(TmnxActionType):
    """Custom type tmnxCpmCardReboot based on TmnxActionType"""


_TmnxCpmCardReboot_Object = MibTableColumn
tmnxCpmCardReboot = _TmnxCpmCardReboot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 20),
    _TmnxCpmCardReboot_Type()
)
tmnxCpmCardReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmCardReboot.setStatus("current")


class _TmnxCpmCardRereadBootOptions_Type(TmnxActionType):
    """Custom type tmnxCpmCardRereadBootOptions based on TmnxActionType"""


_TmnxCpmCardRereadBootOptions_Object = MibTableColumn
tmnxCpmCardRereadBootOptions = _TmnxCpmCardRereadBootOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 21),
    _TmnxCpmCardRereadBootOptions_Type()
)
tmnxCpmCardRereadBootOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmCardRereadBootOptions.setStatus("current")
_TmnxCpmCardConfigFileLastBooted_Type = DisplayString
_TmnxCpmCardConfigFileLastBooted_Object = MibTableColumn
tmnxCpmCardConfigFileLastBooted = _TmnxCpmCardConfigFileLastBooted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 22),
    _TmnxCpmCardConfigFileLastBooted_Type()
)
tmnxCpmCardConfigFileLastBooted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardConfigFileLastBooted.setStatus("current")
_TmnxCpmCardConfigFileLastSaved_Type = DisplayString
_TmnxCpmCardConfigFileLastSaved_Object = MibTableColumn
tmnxCpmCardConfigFileLastSaved = _TmnxCpmCardConfigFileLastSaved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 23),
    _TmnxCpmCardConfigFileLastSaved_Type()
)
tmnxCpmCardConfigFileLastSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardConfigFileLastSaved.setStatus("current")


class _TmnxCpmCardConfigFileLastBootedHeader_Type(OctetString):
    """Custom type tmnxCpmCardConfigFileLastBootedHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TmnxCpmCardConfigFileLastBootedHeader_Type.__name__ = "OctetString"
_TmnxCpmCardConfigFileLastBootedHeader_Object = MibTableColumn
tmnxCpmCardConfigFileLastBootedHeader = _TmnxCpmCardConfigFileLastBootedHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 24),
    _TmnxCpmCardConfigFileLastBootedHeader_Type()
)
tmnxCpmCardConfigFileLastBootedHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardConfigFileLastBootedHeader.setStatus("current")


class _TmnxCpmCardIndexFileLastBootedHeader_Type(OctetString):
    """Custom type tmnxCpmCardIndexFileLastBootedHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TmnxCpmCardIndexFileLastBootedHeader_Type.__name__ = "OctetString"
_TmnxCpmCardIndexFileLastBootedHeader_Object = MibTableColumn
tmnxCpmCardIndexFileLastBootedHeader = _TmnxCpmCardIndexFileLastBootedHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 25),
    _TmnxCpmCardIndexFileLastBootedHeader_Type()
)
tmnxCpmCardIndexFileLastBootedHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardIndexFileLastBootedHeader.setStatus("current")
_TmnxCpmCardBootOptionSource_Type = DisplayString
_TmnxCpmCardBootOptionSource_Object = MibTableColumn
tmnxCpmCardBootOptionSource = _TmnxCpmCardBootOptionSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 26),
    _TmnxCpmCardBootOptionSource_Type()
)
tmnxCpmCardBootOptionSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardBootOptionSource.setStatus("current")


class _TmnxCpmCardConfigSource_Type(Integer32):
    """Custom type tmnxCpmCardConfigSource based on Integer32"""
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
        *(("primary", 1),
          ("secondary", 2),
          ("tertiary", 3),
          ("unknown", 0))
    )


_TmnxCpmCardConfigSource_Type.__name__ = "Integer32"
_TmnxCpmCardConfigSource_Object = MibTableColumn
tmnxCpmCardConfigSource = _TmnxCpmCardConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 27),
    _TmnxCpmCardConfigSource_Type()
)
tmnxCpmCardConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardConfigSource.setStatus("current")
_TmnxCpmCardBootOptionLastSaved_Type = DateAndTime
_TmnxCpmCardBootOptionLastSaved_Object = MibTableColumn
tmnxCpmCardBootOptionLastSaved = _TmnxCpmCardBootOptionLastSaved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 28),
    _TmnxCpmCardBootOptionLastSaved_Type()
)
tmnxCpmCardBootOptionLastSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardBootOptionLastSaved.setStatus("current")


class _TmnxCpmCardMasterSlaveRefState_Type(Integer32):
    """Custom type tmnxCpmCardMasterSlaveRefState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInitialized", 3),
          ("primaryRef", 1),
          ("secondaryRef", 2))
    )


_TmnxCpmCardMasterSlaveRefState_Type.__name__ = "Integer32"
_TmnxCpmCardMasterSlaveRefState_Object = MibTableColumn
tmnxCpmCardMasterSlaveRefState = _TmnxCpmCardMasterSlaveRefState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 30),
    _TmnxCpmCardMasterSlaveRefState_Type()
)
tmnxCpmCardMasterSlaveRefState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardMasterSlaveRefState.setStatus("current")


class _TmnxCpmCardConfigUserLastModified_Type(SnmpAdminString):
    """Custom type tmnxCpmCardConfigUserLastModified based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxCpmCardConfigUserLastModified_Type.__name__ = "SnmpAdminString"
_TmnxCpmCardConfigUserLastModified_Object = MibTableColumn
tmnxCpmCardConfigUserLastModified = _TmnxCpmCardConfigUserLastModified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 31),
    _TmnxCpmCardConfigUserLastModified_Type()
)
tmnxCpmCardConfigUserLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardConfigUserLastModified.setStatus("current")
_TmnxCpmCardCmplxCAMErrOccur_Type = Counter32
_TmnxCpmCardCmplxCAMErrOccur_Object = MibTableColumn
tmnxCpmCardCmplxCAMErrOccur = _TmnxCpmCardCmplxCAMErrOccur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 32),
    _TmnxCpmCardCmplxCAMErrOccur_Type()
)
tmnxCpmCardCmplxCAMErrOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardCmplxCAMErrOccur.setStatus("current")
_TmnxCpmCardCmplxCAMErrOccurTime_Type = TimeStamp
_TmnxCpmCardCmplxCAMErrOccurTime_Object = MibTableColumn
tmnxCpmCardCmplxCAMErrOccurTime = _TmnxCpmCardCmplxCAMErrOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 33),
    _TmnxCpmCardCmplxCAMErrOccurTime_Type()
)
tmnxCpmCardCmplxCAMErrOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardCmplxCAMErrOccurTime.setStatus("current")


class _TmnxCpmCardOscillatorType_Type(Integer32):
    """Custom type tmnxCpmCardOscillatorType based on Integer32"""
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
          ("ocxo", 3),
          ("tcxo", 2))
    )


_TmnxCpmCardOscillatorType_Type.__name__ = "Integer32"
_TmnxCpmCardOscillatorType_Object = MibTableColumn
tmnxCpmCardOscillatorType = _TmnxCpmCardOscillatorType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 4, 1, 34),
    _TmnxCpmCardOscillatorType_Type()
)
tmnxCpmCardOscillatorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmCardOscillatorType.setStatus("current")
_TmnxFabricLastChange_Type = TimeStamp
_TmnxFabricLastChange_Object = MibScalar
tmnxFabricLastChange = _TmnxFabricLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 5),
    _TmnxFabricLastChange_Type()
)
tmnxFabricLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFabricLastChange.setStatus("current")
_TmnxFabricTable_Object = MibTable
tmnxFabricTable = _TmnxFabricTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxFabricTable.setStatus("current")
_TmnxFabricEntry_Object = MibTableRow
tmnxFabricEntry = _TmnxFabricEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 6, 1)
)
tmnxFabricEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFabricSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxFabricEntry.setStatus("current")


class _TmnxFabricSlotNum_Type(Unsigned32):
    """Custom type tmnxFabricSlotNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxFabricSlotNum_Type.__name__ = "Unsigned32"
_TmnxFabricSlotNum_Object = MibTableColumn
tmnxFabricSlotNum = _TmnxFabricSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 6, 1, 1),
    _TmnxFabricSlotNum_Type()
)
tmnxFabricSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFabricSlotNum.setStatus("current")


class _TmnxFabricAssignedType_Type(TmnxFabricType):
    """Custom type tmnxFabricAssignedType based on TmnxFabricType"""
    defaultValue = 2


_TmnxFabricAssignedType_Object = MibTableColumn
tmnxFabricAssignedType = _TmnxFabricAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 6, 1, 2),
    _TmnxFabricAssignedType_Type()
)
tmnxFabricAssignedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFabricAssignedType.setStatus("current")
_TmnxFabricEquippedType_Type = TmnxFabricType
_TmnxFabricEquippedType_Object = MibTableColumn
tmnxFabricEquippedType = _TmnxFabricEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 6, 1, 3),
    _TmnxFabricEquippedType_Type()
)
tmnxFabricEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFabricEquippedType.setStatus("current")
_TmnxFabricHwIndex_Type = TmnxHwIndex
_TmnxFabricHwIndex_Object = MibTableColumn
tmnxFabricHwIndex = _TmnxFabricHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 6, 1, 4),
    _TmnxFabricHwIndex_Type()
)
tmnxFabricHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFabricHwIndex.setStatus("current")
_TmnxFabricSupportedTypes_Type = TmnxFabricSuppType
_TmnxFabricSupportedTypes_Object = MibTableColumn
tmnxFabricSupportedTypes = _TmnxFabricSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 6, 1, 5),
    _TmnxFabricSupportedTypes_Type()
)
tmnxFabricSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFabricSupportedTypes.setStatus("current")


class _TmnxFabricReboot_Type(TmnxActionType):
    """Custom type tmnxFabricReboot based on TmnxActionType"""


_TmnxFabricReboot_Object = MibTableColumn
tmnxFabricReboot = _TmnxFabricReboot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 6, 1, 6),
    _TmnxFabricReboot_Type()
)
tmnxFabricReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFabricReboot.setStatus("current")
_TmnxCpmFlashTable_Object = MibTable
tmnxCpmFlashTable = _TmnxCpmFlashTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 7)
)
if mibBuilder.loadTexts:
    tmnxCpmFlashTable.setStatus("current")
_TmnxCpmFlashEntry_Object = MibTableRow
tmnxCpmFlashEntry = _TmnxCpmFlashEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 7, 1)
)
tmnxCpmFlashEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCpmFlashId"),
)
if mibBuilder.loadTexts:
    tmnxCpmFlashEntry.setStatus("current")


class _TmnxCpmFlashId_Type(Unsigned32):
    """Custom type tmnxCpmFlashId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TmnxCpmFlashId_Type.__name__ = "Unsigned32"
_TmnxCpmFlashId_Object = MibTableColumn
tmnxCpmFlashId = _TmnxCpmFlashId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 7, 1, 1),
    _TmnxCpmFlashId_Type()
)
tmnxCpmFlashId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmFlashId.setStatus("current")
_TmnxCpmFlashOperStatus_Type = TmnxDeviceState
_TmnxCpmFlashOperStatus_Object = MibTableColumn
tmnxCpmFlashOperStatus = _TmnxCpmFlashOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 7, 1, 2),
    _TmnxCpmFlashOperStatus_Type()
)
tmnxCpmFlashOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmFlashOperStatus.setStatus("current")
_TmnxCpmFlashSerialNumber_Type = TItemDescription
_TmnxCpmFlashSerialNumber_Object = MibTableColumn
tmnxCpmFlashSerialNumber = _TmnxCpmFlashSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 7, 1, 3),
    _TmnxCpmFlashSerialNumber_Type()
)
tmnxCpmFlashSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmFlashSerialNumber.setStatus("current")
_TmnxCpmFlashFirmwareRevision_Type = TItemDescription
_TmnxCpmFlashFirmwareRevision_Object = MibTableColumn
tmnxCpmFlashFirmwareRevision = _TmnxCpmFlashFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 7, 1, 4),
    _TmnxCpmFlashFirmwareRevision_Type()
)
tmnxCpmFlashFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmFlashFirmwareRevision.setStatus("current")
_TmnxCpmFlashModelNumber_Type = TItemDescription
_TmnxCpmFlashModelNumber_Object = MibTableColumn
tmnxCpmFlashModelNumber = _TmnxCpmFlashModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 7, 1, 5),
    _TmnxCpmFlashModelNumber_Type()
)
tmnxCpmFlashModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmFlashModelNumber.setStatus("current")
_TmnxCpmFlashCapacity_Type = Unsigned32
_TmnxCpmFlashCapacity_Object = MibTableColumn
tmnxCpmFlashCapacity = _TmnxCpmFlashCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 7, 1, 6),
    _TmnxCpmFlashCapacity_Type()
)
tmnxCpmFlashCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmFlashCapacity.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCpmFlashCapacity.setUnits("sectors")
_TmnxCpmFlashUsed_Type = Unsigned32
_TmnxCpmFlashUsed_Object = MibTableColumn
tmnxCpmFlashUsed = _TmnxCpmFlashUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 7, 1, 7),
    _TmnxCpmFlashUsed_Type()
)
tmnxCpmFlashUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmFlashUsed.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCpmFlashUsed.setUnits("sectors")
_TmnxCpmFlashHwIndex_Type = TmnxHwIndex
_TmnxCpmFlashHwIndex_Object = MibTableColumn
tmnxCpmFlashHwIndex = _TmnxCpmFlashHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 7, 1, 8),
    _TmnxCpmFlashHwIndex_Type()
)
tmnxCpmFlashHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmFlashHwIndex.setStatus("current")
_TmnxMDATable_Object = MibTable
tmnxMDATable = _TmnxMDATable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxMDATable.setStatus("current")
_TmnxMDAEntry_Object = MibTableRow
tmnxMDAEntry = _TmnxMDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1)
)
tmnxMDAEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMDAEntry.setStatus("current")


class _TmnxMDASlotNum_Type(Unsigned32):
    """Custom type tmnxMDASlotNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TmnxMDASlotNum_Type.__name__ = "Unsigned32"
_TmnxMDASlotNum_Object = MibTableColumn
tmnxMDASlotNum = _TmnxMDASlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 1),
    _TmnxMDASlotNum_Type()
)
tmnxMDASlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMDASlotNum.setStatus("current")
_TmnxMDASupportedTypes_Type = TmnxMDASuppType
_TmnxMDASupportedTypes_Object = MibTableColumn
tmnxMDASupportedTypes = _TmnxMDASupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 2),
    _TmnxMDASupportedTypes_Type()
)
tmnxMDASupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDASupportedTypes.setStatus("current")
_TmnxMDAAllowedTypes_Type = TmnxMdaType
_TmnxMDAAllowedTypes_Object = MibTableColumn
tmnxMDAAllowedTypes = _TmnxMDAAllowedTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 3),
    _TmnxMDAAllowedTypes_Type()
)
tmnxMDAAllowedTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAAllowedTypes.setStatus("obsolete")


class _TmnxMDAAssignedType_Type(TmnxMdaType):
    """Custom type tmnxMDAAssignedType based on TmnxMdaType"""
    defaultValue = 1


_TmnxMDAAssignedType_Object = MibTableColumn
tmnxMDAAssignedType = _TmnxMDAAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 4),
    _TmnxMDAAssignedType_Type()
)
tmnxMDAAssignedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAAssignedType.setStatus("current")
_TmnxMDAEquippedType_Type = TmnxMdaType
_TmnxMDAEquippedType_Object = MibTableColumn
tmnxMDAEquippedType = _TmnxMDAEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 5),
    _TmnxMDAEquippedType_Type()
)
tmnxMDAEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAEquippedType.setStatus("current")
_TmnxMDAHwIndex_Type = TmnxHwIndex
_TmnxMDAHwIndex_Object = MibTableColumn
tmnxMDAHwIndex = _TmnxMDAHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 6),
    _TmnxMDAHwIndex_Type()
)
tmnxMDAHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAHwIndex.setStatus("current")


class _TmnxMDAMaxPorts_Type(Integer32):
    """Custom type tmnxMDAMaxPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxMDAMaxPorts_Type.__name__ = "Integer32"
_TmnxMDAMaxPorts_Object = MibTableColumn
tmnxMDAMaxPorts = _TmnxMDAMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 7),
    _TmnxMDAMaxPorts_Type()
)
tmnxMDAMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMaxPorts.setStatus("current")
_TmnxMDAEquippedPorts_Type = Unsigned32
_TmnxMDAEquippedPorts_Object = MibTableColumn
tmnxMDAEquippedPorts = _TmnxMDAEquippedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 8),
    _TmnxMDAEquippedPorts_Type()
)
tmnxMDAEquippedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAEquippedPorts.setStatus("current")


class _TmnxMDATxTimingSelected_Type(Integer32):
    """Custom type tmnxMDATxTimingSelected based on Integer32"""
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
        *(("cpm-card-A", 1),
          ("cpm-card-B", 2),
          ("holdover", 4),
          ("local", 3),
          ("not-applicable", 5))
    )


_TmnxMDATxTimingSelected_Type.__name__ = "Integer32"
_TmnxMDATxTimingSelected_Object = MibTableColumn
tmnxMDATxTimingSelected = _TmnxMDATxTimingSelected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 10),
    _TmnxMDATxTimingSelected_Type()
)
tmnxMDATxTimingSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDATxTimingSelected.setStatus("current")


class _TmnxMDASyncIfTimingStatus_Type(Integer32):
    """Custom type tmnxMDASyncIfTimingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 3),
          ("not-qualified", 2),
          ("qualified", 1))
    )


_TmnxMDASyncIfTimingStatus_Type.__name__ = "Integer32"
_TmnxMDASyncIfTimingStatus_Object = MibTableColumn
tmnxMDASyncIfTimingStatus = _TmnxMDASyncIfTimingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 11),
    _TmnxMDASyncIfTimingStatus_Type()
)
tmnxMDASyncIfTimingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDASyncIfTimingStatus.setStatus("current")


class _TmnxMDANetworkIngQueues_Type(TNamedItem):
    """Custom type tmnxMDANetworkIngQueues based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxMDANetworkIngQueues_Object = MibTableColumn
tmnxMDANetworkIngQueues = _TmnxMDANetworkIngQueues_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 12),
    _TmnxMDANetworkIngQueues_Type()
)
tmnxMDANetworkIngQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDANetworkIngQueues.setStatus("current")


class _TmnxMDACapabilities_Type(Bits):
    """Custom type tmnxMDACapabilities based on Bits"""
    namedValues = NamedValues(
        *(("isCMA", 7),
          ("isEthernet", 0),
          ("isSonet", 1),
          ("isTDM", 2),
          ("supportsATM", 5),
          ("supportsCEM", 8),
          ("supportsFR", 4),
          ("supportsPPP", 3),
          ("supportscHDLC", 6))
    )

_TmnxMDACapabilities_Type.__name__ = "Bits"
_TmnxMDACapabilities_Object = MibTableColumn
tmnxMDACapabilities = _TmnxMDACapabilities_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 13),
    _TmnxMDACapabilities_Type()
)
tmnxMDACapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDACapabilities.setStatus("current")
_TmnxMDAMinChannelization_Type = TmnxMDAChanType
_TmnxMDAMinChannelization_Object = MibTableColumn
tmnxMDAMinChannelization = _TmnxMDAMinChannelization_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 14),
    _TmnxMDAMinChannelization_Type()
)
tmnxMDAMinChannelization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMinChannelization.setStatus("current")
_TmnxMDAMaxChannelization_Type = TmnxMDAChanType
_TmnxMDAMaxChannelization_Object = MibTableColumn
tmnxMDAMaxChannelization = _TmnxMDAMaxChannelization_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 15),
    _TmnxMDAMaxChannelization_Type()
)
tmnxMDAMaxChannelization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMaxChannelization.setStatus("current")
_TmnxMDAMaxChannels_Type = Unsigned32
_TmnxMDAMaxChannels_Object = MibTableColumn
tmnxMDAMaxChannels = _TmnxMDAMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 16),
    _TmnxMDAMaxChannels_Type()
)
tmnxMDAMaxChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMaxChannels.setStatus("current")
_TmnxMDAChannelsInUse_Type = Unsigned32
_TmnxMDAChannelsInUse_Object = MibTableColumn
tmnxMDAChannelsInUse = _TmnxMDAChannelsInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 17),
    _TmnxMDAChannelsInUse_Type()
)
tmnxMDAChannelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAChannelsInUse.setStatus("current")


class _TmnxMDACcagId_Type(TmnxCcagId):
    """Custom type tmnxMDACcagId based on TmnxCcagId"""
    defaultValue = 0


_TmnxMDACcagId_Object = MibTableColumn
tmnxMDACcagId = _TmnxMDACcagId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 18),
    _TmnxMDACcagId_Type()
)
tmnxMDACcagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDACcagId.setStatus("current")


class _TmnxMDAReboot_Type(TmnxActionType):
    """Custom type tmnxMDAReboot based on TmnxActionType"""


_TmnxMDAReboot_Object = MibTableColumn
tmnxMDAReboot = _TmnxMDAReboot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 19),
    _TmnxMDAReboot_Type()
)
tmnxMDAReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAReboot.setStatus("current")


class _TmnxMDAHiBwMcastSource_Type(TruthValue):
    """Custom type tmnxMDAHiBwMcastSource based on TruthValue"""


_TmnxMDAHiBwMcastSource_Object = MibTableColumn
tmnxMDAHiBwMcastSource = _TmnxMDAHiBwMcastSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 20),
    _TmnxMDAHiBwMcastSource_Type()
)
tmnxMDAHiBwMcastSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAHiBwMcastSource.setStatus("current")


class _TmnxMDAHiBwMcastAlarm_Type(TruthValue):
    """Custom type tmnxMDAHiBwMcastAlarm based on TruthValue"""


_TmnxMDAHiBwMcastAlarm_Object = MibTableColumn
tmnxMDAHiBwMcastAlarm = _TmnxMDAHiBwMcastAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 21),
    _TmnxMDAHiBwMcastAlarm_Type()
)
tmnxMDAHiBwMcastAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAHiBwMcastAlarm.setStatus("current")
_TmnxMDAHiBwMcastTapCount_Type = Gauge32
_TmnxMDAHiBwMcastTapCount_Object = MibTableColumn
tmnxMDAHiBwMcastTapCount = _TmnxMDAHiBwMcastTapCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 22),
    _TmnxMDAHiBwMcastTapCount_Type()
)
tmnxMDAHiBwMcastTapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAHiBwMcastTapCount.setStatus("current")


class _TmnxMDAHiBwMcastGroup_Type(Unsigned32):
    """Custom type tmnxMDAHiBwMcastGroup based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxMDAHiBwMcastGroup_Type.__name__ = "Unsigned32"
_TmnxMDAHiBwMcastGroup_Object = MibTableColumn
tmnxMDAHiBwMcastGroup = _TmnxMDAHiBwMcastGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 23),
    _TmnxMDAHiBwMcastGroup_Type()
)
tmnxMDAHiBwMcastGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAHiBwMcastGroup.setStatus("current")


class _TmnxMDAClockMode_Type(Integer32):
    """Custom type tmnxMDAClockMode based on Integer32"""
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
        *(("adaptive", 1),
          ("differential", 2),
          ("notApplicable", 0))
    )


_TmnxMDAClockMode_Type.__name__ = "Integer32"
_TmnxMDAClockMode_Object = MibTableColumn
tmnxMDAClockMode = _TmnxMDAClockMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 24),
    _TmnxMDAClockMode_Type()
)
tmnxMDAClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAClockMode.setStatus("current")


class _TmnxMDADiffTimestampFreq_Type(Unsigned32):
    """Custom type tmnxMDADiffTimestampFreq based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(19440, 19440),
        ValueRangeConstraint(77760, 77760),
        ValueRangeConstraint(103680, 103680),
    )


_TmnxMDADiffTimestampFreq_Type.__name__ = "Unsigned32"
_TmnxMDADiffTimestampFreq_Object = MibTableColumn
tmnxMDADiffTimestampFreq = _TmnxMDADiffTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 25),
    _TmnxMDADiffTimestampFreq_Type()
)
tmnxMDADiffTimestampFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDADiffTimestampFreq.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMDADiffTimestampFreq.setUnits("kilohertz")
_TmnxMDAIngHsmdaSchedPolicy_Type = TNamedItemOrEmpty
_TmnxMDAIngHsmdaSchedPolicy_Object = MibTableColumn
tmnxMDAIngHsmdaSchedPolicy = _TmnxMDAIngHsmdaSchedPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 26),
    _TmnxMDAIngHsmdaSchedPolicy_Type()
)
tmnxMDAIngHsmdaSchedPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAIngHsmdaSchedPolicy.setStatus("obsolete")


class _TmnxMDAMcPathMgmtBwPlcyName_Type(TNamedItem):
    """Custom type tmnxMDAMcPathMgmtBwPlcyName based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxMDAMcPathMgmtBwPlcyName_Object = MibTableColumn
tmnxMDAMcPathMgmtBwPlcyName = _TmnxMDAMcPathMgmtBwPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 27),
    _TmnxMDAMcPathMgmtBwPlcyName_Type()
)
tmnxMDAMcPathMgmtBwPlcyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtBwPlcyName.setStatus("current")


class _TmnxMDAMcPathMgmtPriPathLimit_Type(Unsigned32):
    """Custom type tmnxMDAMcPathMgmtPriPathLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2000),
    )


_TmnxMDAMcPathMgmtPriPathLimit_Type.__name__ = "Unsigned32"
_TmnxMDAMcPathMgmtPriPathLimit_Object = MibTableColumn
tmnxMDAMcPathMgmtPriPathLimit = _TmnxMDAMcPathMgmtPriPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 28),
    _TmnxMDAMcPathMgmtPriPathLimit_Type()
)
tmnxMDAMcPathMgmtPriPathLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtPriPathLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtPriPathLimit.setUnits("mega-bits-per-second")


class _TmnxMDAMcPathMgmtSecPathLimit_Type(Unsigned32):
    """Custom type tmnxMDAMcPathMgmtSecPathLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2000),
    )


_TmnxMDAMcPathMgmtSecPathLimit_Type.__name__ = "Unsigned32"
_TmnxMDAMcPathMgmtSecPathLimit_Object = MibTableColumn
tmnxMDAMcPathMgmtSecPathLimit = _TmnxMDAMcPathMgmtSecPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 29),
    _TmnxMDAMcPathMgmtSecPathLimit_Type()
)
tmnxMDAMcPathMgmtSecPathLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtSecPathLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtSecPathLimit.setUnits("mega-bits-per-second")


class _TmnxMDAMcPathMgmtAncPathLimit_Type(Unsigned32):
    """Custom type tmnxMDAMcPathMgmtAncPathLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 5000),
    )


_TmnxMDAMcPathMgmtAncPathLimit_Type.__name__ = "Unsigned32"
_TmnxMDAMcPathMgmtAncPathLimit_Object = MibTableColumn
tmnxMDAMcPathMgmtAncPathLimit = _TmnxMDAMcPathMgmtAncPathLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 30),
    _TmnxMDAMcPathMgmtAncPathLimit_Type()
)
tmnxMDAMcPathMgmtAncPathLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtAncPathLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtAncPathLimit.setUnits("mega-bits-per-second")


class _TmnxMDAMcPathMgmtAdminState_Type(TmnxAdminState):
    """Custom type tmnxMDAMcPathMgmtAdminState based on TmnxAdminState"""


_TmnxMDAMcPathMgmtAdminState_Object = MibTableColumn
tmnxMDAMcPathMgmtAdminState = _TmnxMDAMcPathMgmtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 31),
    _TmnxMDAMcPathMgmtAdminState_Type()
)
tmnxMDAMcPathMgmtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtAdminState.setStatus("current")


class _TmnxMDAIngNamedPoolPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxMDAIngNamedPoolPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMDAIngNamedPoolPolicy_Object = MibTableColumn
tmnxMDAIngNamedPoolPolicy = _TmnxMDAIngNamedPoolPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 32),
    _TmnxMDAIngNamedPoolPolicy_Type()
)
tmnxMDAIngNamedPoolPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAIngNamedPoolPolicy.setStatus("current")


class _TmnxMDAEgrNamedPoolPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxMDAEgrNamedPoolPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMDAEgrNamedPoolPolicy_Object = MibTableColumn
tmnxMDAEgrNamedPoolPolicy = _TmnxMDAEgrNamedPoolPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 33),
    _TmnxMDAEgrNamedPoolPolicy_Type()
)
tmnxMDAEgrNamedPoolPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAEgrNamedPoolPolicy.setStatus("current")
_TmnxMDAIngHsmdaPoolPolicy_Type = TNamedItemOrEmpty
_TmnxMDAIngHsmdaPoolPolicy_Object = MibTableColumn
tmnxMDAIngHsmdaPoolPolicy = _TmnxMDAIngHsmdaPoolPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 34),
    _TmnxMDAIngHsmdaPoolPolicy_Type()
)
tmnxMDAIngHsmdaPoolPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAIngHsmdaPoolPolicy.setStatus("obsolete")
_TmnxMDAEgrHsmdaPoolPolicy_Type = TNamedItemOrEmpty
_TmnxMDAEgrHsmdaPoolPolicy_Object = MibTableColumn
tmnxMDAEgrHsmdaPoolPolicy = _TmnxMDAEgrHsmdaPoolPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 35),
    _TmnxMDAEgrHsmdaPoolPolicy_Type()
)
tmnxMDAEgrHsmdaPoolPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAEgrHsmdaPoolPolicy.setStatus("current")
_TmnxMDAMcPathMgmtPriInUseBw_Type = Gauge32
_TmnxMDAMcPathMgmtPriInUseBw_Object = MibTableColumn
tmnxMDAMcPathMgmtPriInUseBw = _TmnxMDAMcPathMgmtPriInUseBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 36),
    _TmnxMDAMcPathMgmtPriInUseBw_Type()
)
tmnxMDAMcPathMgmtPriInUseBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtPriInUseBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtPriInUseBw.setUnits("Kbps")
_TmnxMDAMcPathMgmtSecInUseBw_Type = Gauge32
_TmnxMDAMcPathMgmtSecInUseBw_Object = MibTableColumn
tmnxMDAMcPathMgmtSecInUseBw = _TmnxMDAMcPathMgmtSecInUseBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 37),
    _TmnxMDAMcPathMgmtSecInUseBw_Type()
)
tmnxMDAMcPathMgmtSecInUseBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtSecInUseBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtSecInUseBw.setUnits("Kbps")
_TmnxMDAMcPathMgmtAncInUseBw_Type = Gauge32
_TmnxMDAMcPathMgmtAncInUseBw_Object = MibTableColumn
tmnxMDAMcPathMgmtAncInUseBw = _TmnxMDAMcPathMgmtAncInUseBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 38),
    _TmnxMDAMcPathMgmtAncInUseBw_Type()
)
tmnxMDAMcPathMgmtAncInUseBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtAncInUseBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtAncInUseBw.setUnits("Kbps")
_TmnxMDAMcPathMgmtBlkHoleInUseBw_Type = Gauge32
_TmnxMDAMcPathMgmtBlkHoleInUseBw_Object = MibTableColumn
tmnxMDAMcPathMgmtBlkHoleInUseBw = _TmnxMDAMcPathMgmtBlkHoleInUseBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 39),
    _TmnxMDAMcPathMgmtBlkHoleInUseBw_Type()
)
tmnxMDAMcPathMgmtBlkHoleInUseBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtBlkHoleInUseBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtBlkHoleInUseBw.setUnits("Kbps")


class _TmnxMDASynchronousEthernet_Type(Integer32):
    """Custom type tmnxMDASynchronousEthernet based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-applicable", 0))
    )


_TmnxMDASynchronousEthernet_Type.__name__ = "Integer32"
_TmnxMDASynchronousEthernet_Object = MibTableColumn
tmnxMDASynchronousEthernet = _TmnxMDASynchronousEthernet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 40),
    _TmnxMDASynchronousEthernet_Type()
)
tmnxMDASynchronousEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDASynchronousEthernet.setStatus("current")
_TmnxMDAXplErrorTime_Type = TimeStamp
_TmnxMDAXplErrorTime_Object = MibTableColumn
tmnxMDAXplErrorTime = _TmnxMDAXplErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 41),
    _TmnxMDAXplErrorTime_Type()
)
tmnxMDAXplErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAXplErrorTime.setStatus("current")
_TmnxMDAXplFailedCount_Type = Gauge32
_TmnxMDAXplFailedCount_Object = MibTableColumn
tmnxMDAXplFailedCount = _TmnxMDAXplFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 42),
    _TmnxMDAXplFailedCount_Type()
)
tmnxMDAXplFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAXplFailedCount.setStatus("current")
_TmnxMDAAtmMode_Type = TmnxMdaAtmMode
_TmnxMDAAtmMode_Object = MibTableColumn
tmnxMDAAtmMode = _TmnxMDAAtmMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 43),
    _TmnxMDAAtmMode_Type()
)
tmnxMDAAtmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAAtmMode.setStatus("current")


class _TmnxMDAEgrHsmdaThrshLoBrstMult_Type(Integer32):
    """Custom type tmnxMDAEgrHsmdaThrshLoBrstMult based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 65536),
    )


_TmnxMDAEgrHsmdaThrshLoBrstMult_Type.__name__ = "Integer32"
_TmnxMDAEgrHsmdaThrshLoBrstMult_Object = MibTableColumn
tmnxMDAEgrHsmdaThrshLoBrstMult = _TmnxMDAEgrHsmdaThrshLoBrstMult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 44),
    _TmnxMDAEgrHsmdaThrshLoBrstMult_Type()
)
tmnxMDAEgrHsmdaThrshLoBrstMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAEgrHsmdaThrshLoBrstMult.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMDAEgrHsmdaThrshLoBrstMult.setUnits("bytes per megabit of rate")


class _TmnxMDAEgrHsmdaThrshHiBrstInc_Type(Integer32):
    """Custom type tmnxMDAEgrHsmdaThrshHiBrstInc based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65536),
    )


_TmnxMDAEgrHsmdaThrshHiBrstInc_Type.__name__ = "Integer32"
_TmnxMDAEgrHsmdaThrshHiBrstInc_Object = MibTableColumn
tmnxMDAEgrHsmdaThrshHiBrstInc = _TmnxMDAEgrHsmdaThrshHiBrstInc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 45),
    _TmnxMDAEgrHsmdaThrshHiBrstInc_Type()
)
tmnxMDAEgrHsmdaThrshHiBrstInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAEgrHsmdaThrshHiBrstInc.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMDAEgrHsmdaThrshHiBrstInc.setUnits("bytes")


class _TmnxMDAIsaTunnelGroup_Type(TmnxTunnelGroupIdOrZero):
    """Custom type tmnxMDAIsaTunnelGroup based on TmnxTunnelGroupIdOrZero"""
    defaultValue = 0


_TmnxMDAIsaTunnelGroup_Object = MibTableColumn
tmnxMDAIsaTunnelGroup = _TmnxMDAIsaTunnelGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 46),
    _TmnxMDAIsaTunnelGroup_Type()
)
tmnxMDAIsaTunnelGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMDAIsaTunnelGroup.setStatus("current")
_TmnxMDAIsaTunnelGroupInUse_Type = TruthValue
_TmnxMDAIsaTunnelGroupInUse_Object = MibTableColumn
tmnxMDAIsaTunnelGroupInUse = _TmnxMDAIsaTunnelGroupInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 47),
    _TmnxMDAIsaTunnelGroupInUse_Type()
)
tmnxMDAIsaTunnelGroupInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAIsaTunnelGroupInUse.setStatus("current")
_TmnxCardTypeTable_Object = MibTable
tmnxCardTypeTable = _TmnxCardTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 9)
)
if mibBuilder.loadTexts:
    tmnxCardTypeTable.setStatus("current")
_TmnxCardTypeEntry_Object = MibTableRow
tmnxCardTypeEntry = _TmnxCardTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 9, 1)
)
tmnxCardTypeEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxCardTypeEntry.setStatus("current")
_TmnxCardTypeIndex_Type = TmnxCardType
_TmnxCardTypeIndex_Object = MibTableColumn
tmnxCardTypeIndex = _TmnxCardTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 9, 1, 1),
    _TmnxCardTypeIndex_Type()
)
tmnxCardTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCardTypeIndex.setStatus("current")
_TmnxCardTypeName_Type = TNamedItemOrEmpty
_TmnxCardTypeName_Object = MibTableColumn
tmnxCardTypeName = _TmnxCardTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 9, 1, 2),
    _TmnxCardTypeName_Type()
)
tmnxCardTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardTypeName.setStatus("current")
_TmnxCardTypeDescription_Type = TItemDescription
_TmnxCardTypeDescription_Object = MibTableColumn
tmnxCardTypeDescription = _TmnxCardTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 9, 1, 3),
    _TmnxCardTypeDescription_Type()
)
tmnxCardTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardTypeDescription.setStatus("current")
_TmnxCardTypeStatus_Type = TruthValue
_TmnxCardTypeStatus_Object = MibTableColumn
tmnxCardTypeStatus = _TmnxCardTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 9, 1, 4),
    _TmnxCardTypeStatus_Type()
)
tmnxCardTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCardTypeStatus.setStatus("current")
_TmnxMdaTypeTable_Object = MibTable
tmnxMdaTypeTable = _TmnxMdaTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 10)
)
if mibBuilder.loadTexts:
    tmnxMdaTypeTable.setStatus("current")
_TmnxMdaTypeEntry_Object = MibTableRow
tmnxMdaTypeEntry = _TmnxMdaTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 10, 1)
)
tmnxMdaTypeEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMdaTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxMdaTypeEntry.setStatus("current")
_TmnxMdaTypeIndex_Type = TmnxMdaType
_TmnxMdaTypeIndex_Object = MibTableColumn
tmnxMdaTypeIndex = _TmnxMdaTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 10, 1, 1),
    _TmnxMdaTypeIndex_Type()
)
tmnxMdaTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMdaTypeIndex.setStatus("current")
_TmnxMdaTypeName_Type = TNamedItemOrEmpty
_TmnxMdaTypeName_Object = MibTableColumn
tmnxMdaTypeName = _TmnxMdaTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 10, 1, 2),
    _TmnxMdaTypeName_Type()
)
tmnxMdaTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMdaTypeName.setStatus("current")
_TmnxMdaTypeDescription_Type = TItemDescription
_TmnxMdaTypeDescription_Object = MibTableColumn
tmnxMdaTypeDescription = _TmnxMdaTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 10, 1, 3),
    _TmnxMdaTypeDescription_Type()
)
tmnxMdaTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMdaTypeDescription.setStatus("current")
_TmnxMdaTypeStatus_Type = TruthValue
_TmnxMdaTypeStatus_Object = MibTableColumn
tmnxMdaTypeStatus = _TmnxMdaTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 10, 1, 4),
    _TmnxMdaTypeStatus_Type()
)
tmnxMdaTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMdaTypeStatus.setStatus("current")
_TmnxSyncIfTimingTable_Object = MibTable
tmnxSyncIfTimingTable = _TmnxSyncIfTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11)
)
if mibBuilder.loadTexts:
    tmnxSyncIfTimingTable.setStatus("current")
_TmnxSyncIfTimingEntry_Object = MibTableRow
tmnxSyncIfTimingEntry = _TmnxSyncIfTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxSyncIfTimingEntry.setStatus("current")
_TmnxSyncIfTimingRevert_Type = TruthValue
_TmnxSyncIfTimingRevert_Object = MibTableColumn
tmnxSyncIfTimingRevert = _TmnxSyncIfTimingRevert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 1),
    _TmnxSyncIfTimingRevert_Type()
)
tmnxSyncIfTimingRevert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRevert.setStatus("current")
_TmnxSyncIfTimingRefOrder1_Type = TmnxSETSRefSource
_TmnxSyncIfTimingRefOrder1_Object = MibTableColumn
tmnxSyncIfTimingRefOrder1 = _TmnxSyncIfTimingRefOrder1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 2),
    _TmnxSyncIfTimingRefOrder1_Type()
)
tmnxSyncIfTimingRefOrder1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRefOrder1.setStatus("current")
_TmnxSyncIfTimingRefOrder2_Type = TmnxSETSRefSource
_TmnxSyncIfTimingRefOrder2_Object = MibTableColumn
tmnxSyncIfTimingRefOrder2 = _TmnxSyncIfTimingRefOrder2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 3),
    _TmnxSyncIfTimingRefOrder2_Type()
)
tmnxSyncIfTimingRefOrder2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRefOrder2.setStatus("current")
_TmnxSyncIfTimingRef1SrcPort_Type = TmnxPortID
_TmnxSyncIfTimingRef1SrcPort_Object = MibTableColumn
tmnxSyncIfTimingRef1SrcPort = _TmnxSyncIfTimingRef1SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 4),
    _TmnxSyncIfTimingRef1SrcPort_Type()
)
tmnxSyncIfTimingRef1SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef1SrcPort.setStatus("current")
_TmnxSyncIfTimingRef1AdminStatus_Type = TmnxPortAdminStatus
_TmnxSyncIfTimingRef1AdminStatus_Object = MibTableColumn
tmnxSyncIfTimingRef1AdminStatus = _TmnxSyncIfTimingRef1AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 5),
    _TmnxSyncIfTimingRef1AdminStatus_Type()
)
tmnxSyncIfTimingRef1AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef1AdminStatus.setStatus("current")
_TmnxSyncIfTimingRef1InUse_Type = TruthValue
_TmnxSyncIfTimingRef1InUse_Object = MibTableColumn
tmnxSyncIfTimingRef1InUse = _TmnxSyncIfTimingRef1InUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 6),
    _TmnxSyncIfTimingRef1InUse_Type()
)
tmnxSyncIfTimingRef1InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef1InUse.setStatus("current")
_TmnxSyncIfTimingRef1Qualified_Type = TmnxSETSRefQualified
_TmnxSyncIfTimingRef1Qualified_Object = MibTableColumn
tmnxSyncIfTimingRef1Qualified = _TmnxSyncIfTimingRef1Qualified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 7),
    _TmnxSyncIfTimingRef1Qualified_Type()
)
tmnxSyncIfTimingRef1Qualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef1Qualified.setStatus("current")
_TmnxSyncIfTimingRef1Alarm_Type = TmnxSETSRefAlarm
_TmnxSyncIfTimingRef1Alarm_Object = MibTableColumn
tmnxSyncIfTimingRef1Alarm = _TmnxSyncIfTimingRef1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 8),
    _TmnxSyncIfTimingRef1Alarm_Type()
)
tmnxSyncIfTimingRef1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef1Alarm.setStatus("current")
_TmnxSyncIfTimingRef2SrcPort_Type = TmnxPortID
_TmnxSyncIfTimingRef2SrcPort_Object = MibTableColumn
tmnxSyncIfTimingRef2SrcPort = _TmnxSyncIfTimingRef2SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 9),
    _TmnxSyncIfTimingRef2SrcPort_Type()
)
tmnxSyncIfTimingRef2SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef2SrcPort.setStatus("current")
_TmnxSyncIfTimingRef2AdminStatus_Type = TmnxPortAdminStatus
_TmnxSyncIfTimingRef2AdminStatus_Object = MibTableColumn
tmnxSyncIfTimingRef2AdminStatus = _TmnxSyncIfTimingRef2AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 10),
    _TmnxSyncIfTimingRef2AdminStatus_Type()
)
tmnxSyncIfTimingRef2AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef2AdminStatus.setStatus("current")
_TmnxSyncIfTimingRef2InUse_Type = TruthValue
_TmnxSyncIfTimingRef2InUse_Object = MibTableColumn
tmnxSyncIfTimingRef2InUse = _TmnxSyncIfTimingRef2InUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 11),
    _TmnxSyncIfTimingRef2InUse_Type()
)
tmnxSyncIfTimingRef2InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef2InUse.setStatus("current")
_TmnxSyncIfTimingRef2Qualified_Type = TmnxSETSRefQualified
_TmnxSyncIfTimingRef2Qualified_Object = MibTableColumn
tmnxSyncIfTimingRef2Qualified = _TmnxSyncIfTimingRef2Qualified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 12),
    _TmnxSyncIfTimingRef2Qualified_Type()
)
tmnxSyncIfTimingRef2Qualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef2Qualified.setStatus("current")
_TmnxSyncIfTimingRef2Alarm_Type = TmnxSETSRefAlarm
_TmnxSyncIfTimingRef2Alarm_Object = MibTableColumn
tmnxSyncIfTimingRef2Alarm = _TmnxSyncIfTimingRef2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 13),
    _TmnxSyncIfTimingRef2Alarm_Type()
)
tmnxSyncIfTimingRef2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef2Alarm.setStatus("current")
_TmnxSyncIfTimingFreqOffset_Type = Integer32
_TmnxSyncIfTimingFreqOffset_Object = MibTableColumn
tmnxSyncIfTimingFreqOffset = _TmnxSyncIfTimingFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 14),
    _TmnxSyncIfTimingFreqOffset_Type()
)
tmnxSyncIfTimingFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingFreqOffset.setUnits("parts-per-million")


class _TmnxSyncIfTimingStatus_Type(Integer32):
    """Custom type tmnxSyncIfTimingStatus based on Integer32"""
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
        *(("acquiring", 6),
          ("master-freerun", 2),
          ("master-holdover", 3),
          ("master-locked", 4),
          ("not-present", 1),
          ("slave", 5))
    )


_TmnxSyncIfTimingStatus_Type.__name__ = "Integer32"
_TmnxSyncIfTimingStatus_Object = MibTableColumn
tmnxSyncIfTimingStatus = _TmnxSyncIfTimingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 15),
    _TmnxSyncIfTimingStatus_Type()
)
tmnxSyncIfTimingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingStatus.setStatus("current")
_TmnxSyncIfTimingRefOrder3_Type = TmnxSETSRefSource
_TmnxSyncIfTimingRefOrder3_Object = MibTableColumn
tmnxSyncIfTimingRefOrder3 = _TmnxSyncIfTimingRefOrder3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 16),
    _TmnxSyncIfTimingRefOrder3_Type()
)
tmnxSyncIfTimingRefOrder3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRefOrder3.setStatus("current")
_TmnxSyncIfTimingBITSIfType_Type = TmnxBITSIfType
_TmnxSyncIfTimingBITSIfType_Object = MibTableColumn
tmnxSyncIfTimingBITSIfType = _TmnxSyncIfTimingBITSIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 17),
    _TmnxSyncIfTimingBITSIfType_Type()
)
tmnxSyncIfTimingBITSIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSIfType.setStatus("current")
_TmnxSyncIfTimingBITSAdminStatus_Type = TmnxPortAdminStatus
_TmnxSyncIfTimingBITSAdminStatus_Object = MibTableColumn
tmnxSyncIfTimingBITSAdminStatus = _TmnxSyncIfTimingBITSAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 18),
    _TmnxSyncIfTimingBITSAdminStatus_Type()
)
tmnxSyncIfTimingBITSAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSAdminStatus.setStatus("current")
_TmnxSyncIfTimingBITSInUse_Type = TruthValue
_TmnxSyncIfTimingBITSInUse_Object = MibTableColumn
tmnxSyncIfTimingBITSInUse = _TmnxSyncIfTimingBITSInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 19),
    _TmnxSyncIfTimingBITSInUse_Type()
)
tmnxSyncIfTimingBITSInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSInUse.setStatus("current")
_TmnxSyncIfTimingBITSQualified_Type = TmnxSETSRefQualified
_TmnxSyncIfTimingBITSQualified_Object = MibTableColumn
tmnxSyncIfTimingBITSQualified = _TmnxSyncIfTimingBITSQualified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 20),
    _TmnxSyncIfTimingBITSQualified_Type()
)
tmnxSyncIfTimingBITSQualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSQualified.setStatus("current")
_TmnxSyncIfTimingBITSAlarm_Type = TmnxSETSRefAlarm
_TmnxSyncIfTimingBITSAlarm_Object = MibTableColumn
tmnxSyncIfTimingBITSAlarm = _TmnxSyncIfTimingBITSAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 21),
    _TmnxSyncIfTimingBITSAlarm_Type()
)
tmnxSyncIfTimingBITSAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSAlarm.setStatus("current")
_TmnxSyncIfTimingRef1SrcHw_Type = TmnxHwIndexOrZero
_TmnxSyncIfTimingRef1SrcHw_Object = MibTableColumn
tmnxSyncIfTimingRef1SrcHw = _TmnxSyncIfTimingRef1SrcHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 22),
    _TmnxSyncIfTimingRef1SrcHw_Type()
)
tmnxSyncIfTimingRef1SrcHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef1SrcHw.setStatus("current")
_TmnxSyncIfTimingRef1BITSIfType_Type = TmnxBITSIfType
_TmnxSyncIfTimingRef1BITSIfType_Object = MibTableColumn
tmnxSyncIfTimingRef1BITSIfType = _TmnxSyncIfTimingRef1BITSIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 23),
    _TmnxSyncIfTimingRef1BITSIfType_Type()
)
tmnxSyncIfTimingRef1BITSIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef1BITSIfType.setStatus("current")
_TmnxSyncIfTimingRef2SrcHw_Type = TmnxHwIndexOrZero
_TmnxSyncIfTimingRef2SrcHw_Object = MibTableColumn
tmnxSyncIfTimingRef2SrcHw = _TmnxSyncIfTimingRef2SrcHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 24),
    _TmnxSyncIfTimingRef2SrcHw_Type()
)
tmnxSyncIfTimingRef2SrcHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef2SrcHw.setStatus("current")
_TmnxSyncIfTimingRef2BITSIfType_Type = TmnxBITSIfType
_TmnxSyncIfTimingRef2BITSIfType_Object = MibTableColumn
tmnxSyncIfTimingRef2BITSIfType = _TmnxSyncIfTimingRef2BITSIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 25),
    _TmnxSyncIfTimingRef2BITSIfType_Type()
)
tmnxSyncIfTimingRef2BITSIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef2BITSIfType.setStatus("current")
_TmnxSyncIfTimingBITSOutAdmStatus_Type = TmnxPortAdminStatus
_TmnxSyncIfTimingBITSOutAdmStatus_Object = MibTableColumn
tmnxSyncIfTimingBITSOutAdmStatus = _TmnxSyncIfTimingBITSOutAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 26),
    _TmnxSyncIfTimingBITSOutAdmStatus_Type()
)
tmnxSyncIfTimingBITSOutAdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSOutAdmStatus.setStatus("current")


class _TmnxSyncIfTimingBITSOutLineLen_Type(Integer32):
    """Custom type tmnxSyncIfTimingBITSOutLineLen based on Integer32"""
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
        *(("length0To110", 1),
          ("length110To220", 2),
          ("length220To330", 3),
          ("length330To440", 4),
          ("length440To550", 5),
          ("length550To660", 6),
          ("lengthNotApplicable", 0))
    )


_TmnxSyncIfTimingBITSOutLineLen_Type.__name__ = "Integer32"
_TmnxSyncIfTimingBITSOutLineLen_Object = MibTableColumn
tmnxSyncIfTimingBITSOutLineLen = _TmnxSyncIfTimingBITSOutLineLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 27),
    _TmnxSyncIfTimingBITSOutLineLen_Type()
)
tmnxSyncIfTimingBITSOutLineLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSOutLineLen.setStatus("current")
_TmnxSyncIfTimingRef1CfgQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingRef1CfgQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingRef1CfgQltyLevel = _TmnxSyncIfTimingRef1CfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 28),
    _TmnxSyncIfTimingRef1CfgQltyLevel_Type()
)
tmnxSyncIfTimingRef1CfgQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef1CfgQltyLevel.setStatus("current")
_TmnxSyncIfTimingRef1RxQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingRef1RxQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingRef1RxQltyLevel = _TmnxSyncIfTimingRef1RxQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 29),
    _TmnxSyncIfTimingRef1RxQltyLevel_Type()
)
tmnxSyncIfTimingRef1RxQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef1RxQltyLevel.setStatus("current")
_TmnxSyncIfTimingRef2CfgQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingRef2CfgQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingRef2CfgQltyLevel = _TmnxSyncIfTimingRef2CfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 30),
    _TmnxSyncIfTimingRef2CfgQltyLevel_Type()
)
tmnxSyncIfTimingRef2CfgQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef2CfgQltyLevel.setStatus("current")
_TmnxSyncIfTimingRef2RxQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingRef2RxQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingRef2RxQltyLevel = _TmnxSyncIfTimingRef2RxQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 31),
    _TmnxSyncIfTimingRef2RxQltyLevel_Type()
)
tmnxSyncIfTimingRef2RxQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef2RxQltyLevel.setStatus("current")
_TmnxSyncIfTimingBITSCfgQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingBITSCfgQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingBITSCfgQltyLevel = _TmnxSyncIfTimingBITSCfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 32),
    _TmnxSyncIfTimingBITSCfgQltyLevel_Type()
)
tmnxSyncIfTimingBITSCfgQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSCfgQltyLevel.setStatus("current")
_TmnxSyncIfTimingBITSRxQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingBITSRxQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingBITSRxQltyLevel = _TmnxSyncIfTimingBITSRxQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 33),
    _TmnxSyncIfTimingBITSRxQltyLevel_Type()
)
tmnxSyncIfTimingBITSRxQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSRxQltyLevel.setStatus("current")
_TmnxSyncIfTimingBITS2InUse_Type = TruthValue
_TmnxSyncIfTimingBITS2InUse_Object = MibTableColumn
tmnxSyncIfTimingBITS2InUse = _TmnxSyncIfTimingBITS2InUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 34),
    _TmnxSyncIfTimingBITS2InUse_Type()
)
tmnxSyncIfTimingBITS2InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITS2InUse.setStatus("current")
_TmnxSyncIfTimingBITS2Qualified_Type = TmnxSETSRefQualified
_TmnxSyncIfTimingBITS2Qualified_Object = MibTableColumn
tmnxSyncIfTimingBITS2Qualified = _TmnxSyncIfTimingBITS2Qualified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 35),
    _TmnxSyncIfTimingBITS2Qualified_Type()
)
tmnxSyncIfTimingBITS2Qualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITS2Qualified.setStatus("current")
_TmnxSyncIfTimingBITS2Alarm_Type = TmnxSETSRefAlarm
_TmnxSyncIfTimingBITS2Alarm_Object = MibTableColumn
tmnxSyncIfTimingBITS2Alarm = _TmnxSyncIfTimingBITS2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 36),
    _TmnxSyncIfTimingBITS2Alarm_Type()
)
tmnxSyncIfTimingBITS2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITS2Alarm.setStatus("current")
_TmnxSyncIfTimingBITS2RxQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingBITS2RxQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingBITS2RxQltyLevel = _TmnxSyncIfTimingBITS2RxQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 37),
    _TmnxSyncIfTimingBITS2RxQltyLevel_Type()
)
tmnxSyncIfTimingBITS2RxQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITS2RxQltyLevel.setStatus("current")
_TmnxSyncIfTimingRef1State_Type = TmnxRefInState
_TmnxSyncIfTimingRef1State_Object = MibTableColumn
tmnxSyncIfTimingRef1State = _TmnxSyncIfTimingRef1State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 38),
    _TmnxSyncIfTimingRef1State_Type()
)
tmnxSyncIfTimingRef1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef1State.setStatus("current")
_TmnxSyncIfTimingRef2State_Type = TmnxRefInState
_TmnxSyncIfTimingRef2State_Object = MibTableColumn
tmnxSyncIfTimingRef2State = _TmnxSyncIfTimingRef2State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 39),
    _TmnxSyncIfTimingRef2State_Type()
)
tmnxSyncIfTimingRef2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef2State.setStatus("current")
_TmnxSyncIfTimingBITSState_Type = TmnxRefInState
_TmnxSyncIfTimingBITSState_Object = MibTableColumn
tmnxSyncIfTimingBITSState = _TmnxSyncIfTimingBITSState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 40),
    _TmnxSyncIfTimingBITSState_Type()
)
tmnxSyncIfTimingBITSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSState.setStatus("current")
_TmnxSyncIfTimingBITS2State_Type = TmnxRefInState
_TmnxSyncIfTimingBITS2State_Object = MibTableColumn
tmnxSyncIfTimingBITS2State = _TmnxSyncIfTimingBITS2State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 41),
    _TmnxSyncIfTimingBITS2State_Type()
)
tmnxSyncIfTimingBITS2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITS2State.setStatus("current")


class _TmnxSyncIfTimingRef1NationalUse_Type(Unsigned32):
    """Custom type tmnxSyncIfTimingRef1NationalUse based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_TmnxSyncIfTimingRef1NationalUse_Type.__name__ = "Unsigned32"
_TmnxSyncIfTimingRef1NationalUse_Object = MibTableColumn
tmnxSyncIfTimingRef1NationalUse = _TmnxSyncIfTimingRef1NationalUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 42),
    _TmnxSyncIfTimingRef1NationalUse_Type()
)
tmnxSyncIfTimingRef1NationalUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef1NationalUse.setStatus("current")


class _TmnxSyncIfTimingRef2NationalUse_Type(Unsigned32):
    """Custom type tmnxSyncIfTimingRef2NationalUse based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_TmnxSyncIfTimingRef2NationalUse_Type.__name__ = "Unsigned32"
_TmnxSyncIfTimingRef2NationalUse_Object = MibTableColumn
tmnxSyncIfTimingRef2NationalUse = _TmnxSyncIfTimingRef2NationalUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 43),
    _TmnxSyncIfTimingRef2NationalUse_Type()
)
tmnxSyncIfTimingRef2NationalUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRef2NationalUse.setStatus("current")


class _TmnxSyncIfTimingBITSNationalUse_Type(Unsigned32):
    """Custom type tmnxSyncIfTimingBITSNationalUse based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_TmnxSyncIfTimingBITSNationalUse_Type.__name__ = "Unsigned32"
_TmnxSyncIfTimingBITSNationalUse_Object = MibTableColumn
tmnxSyncIfTimingBITSNationalUse = _TmnxSyncIfTimingBITSNationalUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 44),
    _TmnxSyncIfTimingBITSNationalUse_Type()
)
tmnxSyncIfTimingBITSNationalUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSNationalUse.setStatus("current")
_TmnxSyncIfTimingQLSelection_Type = TmnxEnabledDisabled
_TmnxSyncIfTimingQLSelection_Object = MibTableColumn
tmnxSyncIfTimingQLSelection = _TmnxSyncIfTimingQLSelection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 45),
    _TmnxSyncIfTimingQLSelection_Type()
)
tmnxSyncIfTimingQLSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingQLSelection.setStatus("current")


class _TmnxSyncIfTimingOtherCPMInUse_Type(TruthValue):
    """Custom type tmnxSyncIfTimingOtherCPMInUse based on TruthValue"""


_TmnxSyncIfTimingOtherCPMInUse_Object = MibTableColumn
tmnxSyncIfTimingOtherCPMInUse = _TmnxSyncIfTimingOtherCPMInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 46),
    _TmnxSyncIfTimingOtherCPMInUse_Type()
)
tmnxSyncIfTimingOtherCPMInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingOtherCPMInUse.setStatus("current")


class _TmnxSyncIfTimingOtherCPMQual_Type(TmnxSETSRefQualified):
    """Custom type tmnxSyncIfTimingOtherCPMQual based on TmnxSETSRefQualified"""


_TmnxSyncIfTimingOtherCPMQual_Object = MibTableColumn
tmnxSyncIfTimingOtherCPMQual = _TmnxSyncIfTimingOtherCPMQual_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 47),
    _TmnxSyncIfTimingOtherCPMQual_Type()
)
tmnxSyncIfTimingOtherCPMQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingOtherCPMQual.setStatus("current")


class _TmnxSyncIfTimingOtherCPMAlarm_Type(TmnxSETSRefAlarm):
    """Custom type tmnxSyncIfTimingOtherCPMAlarm based on TmnxSETSRefAlarm"""
    defaultBinValue = "0"


_TmnxSyncIfTimingOtherCPMAlarm_Object = MibTableColumn
tmnxSyncIfTimingOtherCPMAlarm = _TmnxSyncIfTimingOtherCPMAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 48),
    _TmnxSyncIfTimingOtherCPMAlarm_Type()
)
tmnxSyncIfTimingOtherCPMAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingOtherCPMAlarm.setStatus("current")


class _TmnxSyncIfTimingOtherCPMState_Type(TmnxRefInState):
    """Custom type tmnxSyncIfTimingOtherCPMState based on TmnxRefInState"""


_TmnxSyncIfTimingOtherCPMState_Object = MibTableColumn
tmnxSyncIfTimingOtherCPMState = _TmnxSyncIfTimingOtherCPMState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 49),
    _TmnxSyncIfTimingOtherCPMState_Type()
)
tmnxSyncIfTimingOtherCPMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingOtherCPMState.setStatus("current")


class _TmnxSyncIfTimingBITSOutRefSel_Type(TmnxSETSRefSource):
    """Custom type tmnxSyncIfTimingBITSOutRefSel based on TmnxSETSRefSource"""


_TmnxSyncIfTimingBITSOutRefSel_Object = MibTableColumn
tmnxSyncIfTimingBITSOutRefSel = _TmnxSyncIfTimingBITSOutRefSel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 50),
    _TmnxSyncIfTimingBITSOutRefSel_Type()
)
tmnxSyncIfTimingBITSOutRefSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSOutRefSel.setStatus("current")
_TmnxSyncIfTimingBITSTxQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingBITSTxQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingBITSTxQltyLevel = _TmnxSyncIfTimingBITSTxQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 51),
    _TmnxSyncIfTimingBITSTxQltyLevel_Type()
)
tmnxSyncIfTimingBITSTxQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSTxQltyLevel.setStatus("current")
_TmnxSyncIfTimingBITS2AdminStatus_Type = TmnxPortAdminStatus
_TmnxSyncIfTimingBITS2AdminStatus_Object = MibTableColumn
tmnxSyncIfTimingBITS2AdminStatus = _TmnxSyncIfTimingBITS2AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 52),
    _TmnxSyncIfTimingBITS2AdminStatus_Type()
)
tmnxSyncIfTimingBITS2AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITS2AdminStatus.setStatus("current")
_TmnxSyncIfTimingSystemQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingSystemQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingSystemQltyLevel = _TmnxSyncIfTimingSystemQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 53),
    _TmnxSyncIfTimingSystemQltyLevel_Type()
)
tmnxSyncIfTimingSystemQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingSystemQltyLevel.setStatus("current")
_TmnxSyncIfTimingRefOrder4_Type = TmnxSETSRefSource
_TmnxSyncIfTimingRefOrder4_Object = MibTableColumn
tmnxSyncIfTimingRefOrder4 = _TmnxSyncIfTimingRefOrder4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 54),
    _TmnxSyncIfTimingRefOrder4_Type()
)
tmnxSyncIfTimingRefOrder4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRefOrder4.setStatus("current")
_TmnxSyncIfTimingPTPAdminStatus_Type = TmnxPortAdminStatus
_TmnxSyncIfTimingPTPAdminStatus_Object = MibTableColumn
tmnxSyncIfTimingPTPAdminStatus = _TmnxSyncIfTimingPTPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 55),
    _TmnxSyncIfTimingPTPAdminStatus_Type()
)
tmnxSyncIfTimingPTPAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingPTPAdminStatus.setStatus("current")
_TmnxSyncIfTimingPTPInUse_Type = TruthValue
_TmnxSyncIfTimingPTPInUse_Object = MibTableColumn
tmnxSyncIfTimingPTPInUse = _TmnxSyncIfTimingPTPInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 56),
    _TmnxSyncIfTimingPTPInUse_Type()
)
tmnxSyncIfTimingPTPInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingPTPInUse.setStatus("current")
_TmnxSyncIfTimingPTPQualified_Type = TmnxSETSRefQualified
_TmnxSyncIfTimingPTPQualified_Object = MibTableColumn
tmnxSyncIfTimingPTPQualified = _TmnxSyncIfTimingPTPQualified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 57),
    _TmnxSyncIfTimingPTPQualified_Type()
)
tmnxSyncIfTimingPTPQualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingPTPQualified.setStatus("current")
_TmnxSyncIfTimingPTPAlarm_Type = TmnxSETSRefAlarm
_TmnxSyncIfTimingPTPAlarm_Object = MibTableColumn
tmnxSyncIfTimingPTPAlarm = _TmnxSyncIfTimingPTPAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 58),
    _TmnxSyncIfTimingPTPAlarm_Type()
)
tmnxSyncIfTimingPTPAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingPTPAlarm.setStatus("current")
_TmnxSyncIfTimingPTPCfgQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingPTPCfgQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingPTPCfgQltyLevel = _TmnxSyncIfTimingPTPCfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 59),
    _TmnxSyncIfTimingPTPCfgQltyLevel_Type()
)
tmnxSyncIfTimingPTPCfgQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingPTPCfgQltyLevel.setStatus("current")
_TmnxSyncIfTimingPTPRxQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingPTPRxQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingPTPRxQltyLevel = _TmnxSyncIfTimingPTPRxQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 60),
    _TmnxSyncIfTimingPTPRxQltyLevel_Type()
)
tmnxSyncIfTimingPTPRxQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingPTPRxQltyLevel.setStatus("current")
_TmnxSyncIfTimingPTPState_Type = TmnxRefInState
_TmnxSyncIfTimingPTPState_Object = MibTableColumn
tmnxSyncIfTimingPTPState = _TmnxSyncIfTimingPTPState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 61),
    _TmnxSyncIfTimingPTPState_Type()
)
tmnxSyncIfTimingPTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingPTPState.setStatus("current")
_TmnxSyncIfTimingBITSOutSource_Type = TmnxBITSOutSource
_TmnxSyncIfTimingBITSOutSource_Object = MibTableColumn
tmnxSyncIfTimingBITSOutSource = _TmnxSyncIfTimingBITSOutSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 62),
    _TmnxSyncIfTimingBITSOutSource_Type()
)
tmnxSyncIfTimingBITSOutSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITSOutSource.setStatus("current")
_TmnxSyncIfTimingRefOrder5_Type = TmnxSETSRefSource
_TmnxSyncIfTimingRefOrder5_Object = MibTableColumn
tmnxSyncIfTimingRefOrder5 = _TmnxSyncIfTimingRefOrder5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 70),
    _TmnxSyncIfTimingRefOrder5_Type()
)
tmnxSyncIfTimingRefOrder5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingRefOrder5.setStatus("current")
_TmnxSyncIfTimingBITS2InAdminStatus_Type = TmnxPortAdminStatus
_TmnxSyncIfTimingBITS2InAdminStatus_Object = MibTableColumn
tmnxSyncIfTimingBITS2InAdminStatus = _TmnxSyncIfTimingBITS2InAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 71),
    _TmnxSyncIfTimingBITS2InAdminStatus_Type()
)
tmnxSyncIfTimingBITS2InAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITS2InAdminStatus.setStatus("current")
_TmnxSyncIfTimingBITS2OutAdminStatus_Type = TmnxPortAdminStatus
_TmnxSyncIfTimingBITS2OutAdminStatus_Object = MibTableColumn
tmnxSyncIfTimingBITS2OutAdminStatus = _TmnxSyncIfTimingBITS2OutAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 72),
    _TmnxSyncIfTimingBITS2OutAdminStatus_Type()
)
tmnxSyncIfTimingBITS2OutAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITS2OutAdminStatus.setStatus("current")
_TmnxSyncIfTimingBITS2TxQltyLevel_Type = TmnxSSMQualityLevel
_TmnxSyncIfTimingBITS2TxQltyLevel_Object = MibTableColumn
tmnxSyncIfTimingBITS2TxQltyLevel = _TmnxSyncIfTimingBITS2TxQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 11, 1, 73),
    _TmnxSyncIfTimingBITS2TxQltyLevel_Type()
)
tmnxSyncIfTimingBITS2TxQltyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingBITS2TxQltyLevel.setStatus("current")
_TmnxCcagTable_Object = MibTable
tmnxCcagTable = _TmnxCcagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 12)
)
if mibBuilder.loadTexts:
    tmnxCcagTable.setStatus("current")
_TmnxCcagEntry_Object = MibTableRow
tmnxCcagEntry = _TmnxCcagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 12, 1)
)
tmnxCcagEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCcagId"),
)
if mibBuilder.loadTexts:
    tmnxCcagEntry.setStatus("current")
_TmnxCcagId_Type = TmnxCcagId
_TmnxCcagId_Object = MibTableColumn
tmnxCcagId = _TmnxCcagId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 12, 1, 1),
    _TmnxCcagId_Type()
)
tmnxCcagId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCcagId.setStatus("current")
_TmnxCcagRowStatus_Type = RowStatus
_TmnxCcagRowStatus_Object = MibTableColumn
tmnxCcagRowStatus = _TmnxCcagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 12, 1, 2),
    _TmnxCcagRowStatus_Type()
)
tmnxCcagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagRowStatus.setStatus("current")
_TmnxCcagLastChanged_Type = TimeStamp
_TmnxCcagLastChanged_Object = MibTableColumn
tmnxCcagLastChanged = _TmnxCcagLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 12, 1, 3),
    _TmnxCcagLastChanged_Type()
)
tmnxCcagLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcagLastChanged.setStatus("current")


class _TmnxCcagDescription_Type(DisplayString):
    """Custom type tmnxCcagDescription based on DisplayString"""
    defaultHexValue = ""


_TmnxCcagDescription_Object = MibTableColumn
tmnxCcagDescription = _TmnxCcagDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 12, 1, 4),
    _TmnxCcagDescription_Type()
)
tmnxCcagDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagDescription.setStatus("current")


class _TmnxCcagAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxCcagAdminStatus based on TmnxAdminState"""


_TmnxCcagAdminStatus_Object = MibTableColumn
tmnxCcagAdminStatus = _TmnxCcagAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 12, 1, 5),
    _TmnxCcagAdminStatus_Type()
)
tmnxCcagAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagAdminStatus.setStatus("current")
_TmnxCcagOperStatus_Type = TmnxOperState
_TmnxCcagOperStatus_Object = MibTableColumn
tmnxCcagOperStatus = _TmnxCcagOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 12, 1, 6),
    _TmnxCcagOperStatus_Type()
)
tmnxCcagOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcagOperStatus.setStatus("current")


class _TmnxCcagCcaRate_Type(TmnxCcagRate):
    """Custom type tmnxCcagCcaRate based on TmnxCcagRate"""
    defaultValue = -1


_TmnxCcagCcaRate_Object = MibTableColumn
tmnxCcagCcaRate = _TmnxCcagCcaRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 12, 1, 7),
    _TmnxCcagCcaRate_Type()
)
tmnxCcagCcaRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagCcaRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCcagCcaRate.setUnits("kilobits per second")


class _TmnxCcagAccessAdaptQos_Type(Integer32):
    """Custom type tmnxCcagAccessAdaptQos based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("distribute", 2),
          ("link", 1))
    )


_TmnxCcagAccessAdaptQos_Type.__name__ = "Integer32"
_TmnxCcagAccessAdaptQos_Object = MibTableColumn
tmnxCcagAccessAdaptQos = _TmnxCcagAccessAdaptQos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 12, 1, 8),
    _TmnxCcagAccessAdaptQos_Type()
)
tmnxCcagAccessAdaptQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagAccessAdaptQos.setStatus("current")
_TmnxCcagPathTable_Object = MibTable
tmnxCcagPathTable = _TmnxCcagPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 13)
)
if mibBuilder.loadTexts:
    tmnxCcagPathTable.setStatus("current")
_TmnxCcagPathEntry_Object = MibTableRow
tmnxCcagPathEntry = _TmnxCcagPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 13, 1)
)
tmnxCcagPathEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCcagId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCcagPathId"),
)
if mibBuilder.loadTexts:
    tmnxCcagPathEntry.setStatus("current")


class _TmnxCcagPathId_Type(Integer32):
    """Custom type tmnxCcagPathId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alpha", 1),
          ("beta", 2))
    )


_TmnxCcagPathId_Type.__name__ = "Integer32"
_TmnxCcagPathId_Object = MibTableColumn
tmnxCcagPathId = _TmnxCcagPathId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 13, 1, 1),
    _TmnxCcagPathId_Type()
)
tmnxCcagPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCcagPathId.setStatus("current")
_TmnxCcagPathLastChanged_Type = TimeStamp
_TmnxCcagPathLastChanged_Object = MibTableColumn
tmnxCcagPathLastChanged = _TmnxCcagPathLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 13, 1, 2),
    _TmnxCcagPathLastChanged_Type()
)
tmnxCcagPathLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcagPathLastChanged.setStatus("current")


class _TmnxCcagPathRate_Type(TmnxCcagRate):
    """Custom type tmnxCcagPathRate based on TmnxCcagRate"""
    defaultValue = -1


_TmnxCcagPathRate_Object = MibTableColumn
tmnxCcagPathRate = _TmnxCcagPathRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 13, 1, 3),
    _TmnxCcagPathRate_Type()
)
tmnxCcagPathRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCcagPathRate.setUnits("kilobits per second")


class _TmnxCcagPathRateOption_Type(TmnxCcagRateOption):
    """Custom type tmnxCcagPathRateOption based on TmnxCcagRateOption"""


_TmnxCcagPathRateOption_Object = MibTableColumn
tmnxCcagPathRateOption = _TmnxCcagPathRateOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 13, 1, 4),
    _TmnxCcagPathRateOption_Type()
)
tmnxCcagPathRateOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathRateOption.setStatus("current")


class _TmnxCcagPathWeight_Type(Unsigned32):
    """Custom type tmnxCcagPathWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxCcagPathWeight_Type.__name__ = "Unsigned32"
_TmnxCcagPathWeight_Object = MibTableColumn
tmnxCcagPathWeight = _TmnxCcagPathWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 13, 1, 5),
    _TmnxCcagPathWeight_Type()
)
tmnxCcagPathWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathWeight.setStatus("current")
_TmnxCcagPathCcTable_Object = MibTable
tmnxCcagPathCcTable = _TmnxCcagPathCcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14)
)
if mibBuilder.loadTexts:
    tmnxCcagPathCcTable.setStatus("current")
_TmnxCcagPathCcEntry_Object = MibTableRow
tmnxCcagPathCcEntry = _TmnxCcagPathCcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1)
)
tmnxCcagPathCcEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCcagId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCcagPathId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcType"),
)
if mibBuilder.loadTexts:
    tmnxCcagPathCcEntry.setStatus("current")


class _TmnxCcagPathCcType_Type(Integer32):
    """Custom type tmnxCcagPathCcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("netsap", 3),
          ("sapnet", 2),
          ("sapsap", 1))
    )


_TmnxCcagPathCcType_Type.__name__ = "Integer32"
_TmnxCcagPathCcType_Object = MibTableColumn
tmnxCcagPathCcType = _TmnxCcagPathCcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 1),
    _TmnxCcagPathCcType_Type()
)
tmnxCcagPathCcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCcagPathCcType.setStatus("current")
_TmnxCcagPathCcLastChanged_Type = TimeStamp
_TmnxCcagPathCcLastChanged_Object = MibTableColumn
tmnxCcagPathCcLastChanged = _TmnxCcagPathCcLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 2),
    _TmnxCcagPathCcLastChanged_Type()
)
tmnxCcagPathCcLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcagPathCcLastChanged.setStatus("current")


class _TmnxCcagPathCcEgrPoolResvCbs_Type(Integer32):
    """Custom type tmnxCcagPathCcEgrPoolResvCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_TmnxCcagPathCcEgrPoolResvCbs_Type.__name__ = "Integer32"
_TmnxCcagPathCcEgrPoolResvCbs_Object = MibTableColumn
tmnxCcagPathCcEgrPoolResvCbs = _TmnxCcagPathCcEgrPoolResvCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 3),
    _TmnxCcagPathCcEgrPoolResvCbs_Type()
)
tmnxCcagPathCcEgrPoolResvCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathCcEgrPoolResvCbs.setStatus("current")


class _TmnxCcagPathCcEgrPoolSlpPlcy_Type(TNamedItem):
    """Custom type tmnxCcagPathCcEgrPoolSlpPlcy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxCcagPathCcEgrPoolSlpPlcy_Object = MibTableColumn
tmnxCcagPathCcEgrPoolSlpPlcy = _TmnxCcagPathCcEgrPoolSlpPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 4),
    _TmnxCcagPathCcEgrPoolSlpPlcy_Type()
)
tmnxCcagPathCcEgrPoolSlpPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathCcEgrPoolSlpPlcy.setStatus("current")


class _TmnxCcagPathCcIngPoolResvCbs_Type(Integer32):
    """Custom type tmnxCcagPathCcIngPoolResvCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_TmnxCcagPathCcIngPoolResvCbs_Type.__name__ = "Integer32"
_TmnxCcagPathCcIngPoolResvCbs_Object = MibTableColumn
tmnxCcagPathCcIngPoolResvCbs = _TmnxCcagPathCcIngPoolResvCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 5),
    _TmnxCcagPathCcIngPoolResvCbs_Type()
)
tmnxCcagPathCcIngPoolResvCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathCcIngPoolResvCbs.setStatus("current")


class _TmnxCcagPathCcIngPoolSlpPlcy_Type(TNamedItem):
    """Custom type tmnxCcagPathCcIngPoolSlpPlcy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxCcagPathCcIngPoolSlpPlcy_Object = MibTableColumn
tmnxCcagPathCcIngPoolSlpPlcy = _TmnxCcagPathCcIngPoolSlpPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 6),
    _TmnxCcagPathCcIngPoolSlpPlcy_Type()
)
tmnxCcagPathCcIngPoolSlpPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathCcIngPoolSlpPlcy.setStatus("current")


class _TmnxCcagPathCcAcctPolicyId_Type(Unsigned32):
    """Custom type tmnxCcagPathCcAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxCcagPathCcAcctPolicyId_Type.__name__ = "Unsigned32"
_TmnxCcagPathCcAcctPolicyId_Object = MibTableColumn
tmnxCcagPathCcAcctPolicyId = _TmnxCcagPathCcAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 7),
    _TmnxCcagPathCcAcctPolicyId_Type()
)
tmnxCcagPathCcAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathCcAcctPolicyId.setStatus("current")


class _TmnxCcagPathCcCollectStats_Type(TruthValue):
    """Custom type tmnxCcagPathCcCollectStats based on TruthValue"""


_TmnxCcagPathCcCollectStats_Object = MibTableColumn
tmnxCcagPathCcCollectStats = _TmnxCcagPathCcCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 8),
    _TmnxCcagPathCcCollectStats_Type()
)
tmnxCcagPathCcCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathCcCollectStats.setStatus("current")


class _TmnxCcagPathCcQueuePlcy_Type(TNamedItem):
    """Custom type tmnxCcagPathCcQueuePlcy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxCcagPathCcQueuePlcy_Object = MibTableColumn
tmnxCcagPathCcQueuePlcy = _TmnxCcagPathCcQueuePlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 9),
    _TmnxCcagPathCcQueuePlcy_Type()
)
tmnxCcagPathCcQueuePlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathCcQueuePlcy.setStatus("current")


class _TmnxCcagPathCcMac_Type(MacAddress):
    """Custom type tmnxCcagPathCcMac based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxCcagPathCcMac_Object = MibTableColumn
tmnxCcagPathCcMac = _TmnxCcagPathCcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 10),
    _TmnxCcagPathCcMac_Type()
)
tmnxCcagPathCcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathCcMac.setStatus("current")


class _TmnxCcagPathCcMtu_Type(Unsigned32):
    """Custom type tmnxCcagPathCcMtu based on Unsigned32"""
    defaultValue = 0


_TmnxCcagPathCcMtu_Object = MibTableColumn
tmnxCcagPathCcMtu = _TmnxCcagPathCcMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 11),
    _TmnxCcagPathCcMtu_Type()
)
tmnxCcagPathCcMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCcagPathCcMtu.setStatus("current")


class _TmnxCcagPathCcUserAssignedMac_Type(TruthValue):
    """Custom type tmnxCcagPathCcUserAssignedMac based on TruthValue"""


_TmnxCcagPathCcUserAssignedMac_Object = MibTableColumn
tmnxCcagPathCcUserAssignedMac = _TmnxCcagPathCcUserAssignedMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 12),
    _TmnxCcagPathCcUserAssignedMac_Type()
)
tmnxCcagPathCcUserAssignedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcagPathCcUserAssignedMac.setStatus("current")
_TmnxCcagPathCcHwMac_Type = MacAddress
_TmnxCcagPathCcHwMac_Object = MibTableColumn
tmnxCcagPathCcHwMac = _TmnxCcagPathCcHwMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 14, 1, 13),
    _TmnxCcagPathCcHwMac_Type()
)
tmnxCcagPathCcHwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCcagPathCcHwMac.setStatus("current")
_TmnxMcmTable_Object = MibTable
tmnxMcmTable = _TmnxMcmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 15)
)
if mibBuilder.loadTexts:
    tmnxMcmTable.setStatus("current")
_TmnxMcmEntry_Object = MibTableRow
tmnxMcmEntry = _TmnxMcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 15, 1)
)
tmnxMcmEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMcmSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMcmEntry.setStatus("current")


class _TmnxMcmSlotNum_Type(Unsigned32):
    """Custom type tmnxMcmSlotNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TmnxMcmSlotNum_Type.__name__ = "Unsigned32"
_TmnxMcmSlotNum_Object = MibTableColumn
tmnxMcmSlotNum = _TmnxMcmSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 15, 1, 1),
    _TmnxMcmSlotNum_Type()
)
tmnxMcmSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcmSlotNum.setStatus("current")
_TmnxMcmSupportedTypes_Type = TmnxMcmType
_TmnxMcmSupportedTypes_Object = MibTableColumn
tmnxMcmSupportedTypes = _TmnxMcmSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 15, 1, 2),
    _TmnxMcmSupportedTypes_Type()
)
tmnxMcmSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcmSupportedTypes.setStatus("current")


class _TmnxMcmAssignedType_Type(TmnxMcmType):
    """Custom type tmnxMcmAssignedType based on TmnxMcmType"""
    defaultValue = 1


_TmnxMcmAssignedType_Object = MibTableColumn
tmnxMcmAssignedType = _TmnxMcmAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 15, 1, 3),
    _TmnxMcmAssignedType_Type()
)
tmnxMcmAssignedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcmAssignedType.setStatus("current")
_TmnxMcmEquippedType_Type = TmnxMcmType
_TmnxMcmEquippedType_Object = MibTableColumn
tmnxMcmEquippedType = _TmnxMcmEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 15, 1, 4),
    _TmnxMcmEquippedType_Type()
)
tmnxMcmEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcmEquippedType.setStatus("current")
_TmnxMcmHwIndex_Type = TmnxHwIndex
_TmnxMcmHwIndex_Object = MibTableColumn
tmnxMcmHwIndex = _TmnxMcmHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 15, 1, 5),
    _TmnxMcmHwIndex_Type()
)
tmnxMcmHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcmHwIndex.setStatus("current")
_TmnxMcmTypeTable_Object = MibTable
tmnxMcmTypeTable = _TmnxMcmTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    tmnxMcmTypeTable.setStatus("current")
_TmnxMcmTypeEntry_Object = MibTableRow
tmnxMcmTypeEntry = _TmnxMcmTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 16, 1)
)
tmnxMcmTypeEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMcmTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxMcmTypeEntry.setStatus("current")
_TmnxMcmTypeIndex_Type = TmnxMcmType
_TmnxMcmTypeIndex_Object = MibTableColumn
tmnxMcmTypeIndex = _TmnxMcmTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 16, 1, 1),
    _TmnxMcmTypeIndex_Type()
)
tmnxMcmTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcmTypeIndex.setStatus("current")
_TmnxMcmTypeName_Type = TNamedItemOrEmpty
_TmnxMcmTypeName_Object = MibTableColumn
tmnxMcmTypeName = _TmnxMcmTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 16, 1, 2),
    _TmnxMcmTypeName_Type()
)
tmnxMcmTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcmTypeName.setStatus("current")
_TmnxMcmTypeDescription_Type = TItemDescription
_TmnxMcmTypeDescription_Object = MibTableColumn
tmnxMcmTypeDescription = _TmnxMcmTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 16, 1, 3),
    _TmnxMcmTypeDescription_Type()
)
tmnxMcmTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcmTypeDescription.setStatus("current")
_TmnxMcmTypeStatus_Type = TruthValue
_TmnxMcmTypeStatus_Object = MibTableColumn
tmnxMcmTypeStatus = _TmnxMcmTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 16, 1, 4),
    _TmnxMcmTypeStatus_Type()
)
tmnxMcmTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcmTypeStatus.setStatus("current")
_TmnxIPsecIsaGrpTableLastChanged_Type = TimeStamp
_TmnxIPsecIsaGrpTableLastChanged_Object = MibScalar
tmnxIPsecIsaGrpTableLastChanged = _TmnxIPsecIsaGrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 17),
    _TmnxIPsecIsaGrpTableLastChanged_Type()
)
tmnxIPsecIsaGrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpTableLastChanged.setStatus("current")
_TmnxIPsecIsaGrpTable_Object = MibTable
tmnxIPsecIsaGrpTable = _TmnxIPsecIsaGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18)
)
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpTable.setStatus("current")
_TmnxIPsecIsaGrpEntry_Object = MibTableRow
tmnxIPsecIsaGrpEntry = _TmnxIPsecIsaGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1)
)
tmnxIPsecIsaGrpEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpId"),
)
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpEntry.setStatus("current")
_TmnxIPsecIsaGrpId_Type = TmnxTunnelGroupId
_TmnxIPsecIsaGrpId_Object = MibTableColumn
tmnxIPsecIsaGrpId = _TmnxIPsecIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 1),
    _TmnxIPsecIsaGrpId_Type()
)
tmnxIPsecIsaGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpId.setStatus("current")
_TmnxIPsecIsaGrpRowStatus_Type = RowStatus
_TmnxIPsecIsaGrpRowStatus_Object = MibTableColumn
tmnxIPsecIsaGrpRowStatus = _TmnxIPsecIsaGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 2),
    _TmnxIPsecIsaGrpRowStatus_Type()
)
tmnxIPsecIsaGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpRowStatus.setStatus("current")
_TmnxIPsecIsaGrpLastChanged_Type = TimeStamp
_TmnxIPsecIsaGrpLastChanged_Object = MibTableColumn
tmnxIPsecIsaGrpLastChanged = _TmnxIPsecIsaGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 3),
    _TmnxIPsecIsaGrpLastChanged_Type()
)
tmnxIPsecIsaGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpLastChanged.setStatus("current")
_TmnxIPsecIsaGrpDescription_Type = TItemDescription
_TmnxIPsecIsaGrpDescription_Object = MibTableColumn
tmnxIPsecIsaGrpDescription = _TmnxIPsecIsaGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 4),
    _TmnxIPsecIsaGrpDescription_Type()
)
tmnxIPsecIsaGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpDescription.setStatus("current")


class _TmnxIPsecIsaGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxIPsecIsaGrpAdminState based on TmnxAdminState"""


_TmnxIPsecIsaGrpAdminState_Object = MibTableColumn
tmnxIPsecIsaGrpAdminState = _TmnxIPsecIsaGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 5),
    _TmnxIPsecIsaGrpAdminState_Type()
)
tmnxIPsecIsaGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpAdminState.setStatus("current")
_TmnxIPsecIsaGrpOperState_Type = TmnxOperState
_TmnxIPsecIsaGrpOperState_Object = MibTableColumn
tmnxIPsecIsaGrpOperState = _TmnxIPsecIsaGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 6),
    _TmnxIPsecIsaGrpOperState_Type()
)
tmnxIPsecIsaGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpOperState.setStatus("current")


class _TmnxIPsecIsaGrpIsaChassis_Type(TmnxChassisIndex):
    """Custom type tmnxIPsecIsaGrpIsaChassis based on TmnxChassisIndex"""
    defaultValue = 1


_TmnxIPsecIsaGrpIsaChassis_Object = MibTableColumn
tmnxIPsecIsaGrpIsaChassis = _TmnxIPsecIsaGrpIsaChassis_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 7),
    _TmnxIPsecIsaGrpIsaChassis_Type()
)
tmnxIPsecIsaGrpIsaChassis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpIsaChassis.setStatus("current")


class _TmnxIPsecIsaGrpPrimaryIsa_Type(TmnxHwIndexOrZero):
    """Custom type tmnxIPsecIsaGrpPrimaryIsa based on TmnxHwIndexOrZero"""
    defaultValue = 0


_TmnxIPsecIsaGrpPrimaryIsa_Object = MibTableColumn
tmnxIPsecIsaGrpPrimaryIsa = _TmnxIPsecIsaGrpPrimaryIsa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 8),
    _TmnxIPsecIsaGrpPrimaryIsa_Type()
)
tmnxIPsecIsaGrpPrimaryIsa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpPrimaryIsa.setStatus("current")


class _TmnxIPsecIsaGrpBackupIsa_Type(TmnxHwIndexOrZero):
    """Custom type tmnxIPsecIsaGrpBackupIsa based on TmnxHwIndexOrZero"""
    defaultValue = 0


_TmnxIPsecIsaGrpBackupIsa_Object = MibTableColumn
tmnxIPsecIsaGrpBackupIsa = _TmnxIPsecIsaGrpBackupIsa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 9),
    _TmnxIPsecIsaGrpBackupIsa_Type()
)
tmnxIPsecIsaGrpBackupIsa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpBackupIsa.setStatus("current")
_TmnxIPsecIsaGrpActiveIsa_Type = TmnxHwIndexOrZero
_TmnxIPsecIsaGrpActiveIsa_Object = MibTableColumn
tmnxIPsecIsaGrpActiveIsa = _TmnxIPsecIsaGrpActiveIsa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 10),
    _TmnxIPsecIsaGrpActiveIsa_Type()
)
tmnxIPsecIsaGrpActiveIsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpActiveIsa.setStatus("current")
_TmnxIPsecIsaGrpTunnels_Type = Unsigned32
_TmnxIPsecIsaGrpTunnels_Object = MibTableColumn
tmnxIPsecIsaGrpTunnels = _TmnxIPsecIsaGrpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 11),
    _TmnxIPsecIsaGrpTunnels_Type()
)
tmnxIPsecIsaGrpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpTunnels.setStatus("current")
_TmnxIPsecIsaGrpMaxTunnels_Type = Unsigned32
_TmnxIPsecIsaGrpMaxTunnels_Object = MibTableColumn
tmnxIPsecIsaGrpMaxTunnels = _TmnxIPsecIsaGrpMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 12),
    _TmnxIPsecIsaGrpMaxTunnels_Type()
)
tmnxIPsecIsaGrpMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpMaxTunnels.setStatus("current")


class _TmnxIPsecIsaGrpTunnelReassembly_Type(Integer32):
    """Custom type tmnxIPsecIsaGrpTunnelReassembly based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_TmnxIPsecIsaGrpTunnelReassembly_Type.__name__ = "Integer32"
_TmnxIPsecIsaGrpTunnelReassembly_Object = MibTableColumn
tmnxIPsecIsaGrpTunnelReassembly = _TmnxIPsecIsaGrpTunnelReassembly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 13),
    _TmnxIPsecIsaGrpTunnelReassembly_Type()
)
tmnxIPsecIsaGrpTunnelReassembly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpTunnelReassembly.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpTunnelReassembly.setUnits("milli-seconds")
_TmnxIPsecIsaGrpOperFlags_Type = TmnxIpSecIsaOperFlags
_TmnxIPsecIsaGrpOperFlags_Object = MibTableColumn
tmnxIPsecIsaGrpOperFlags = _TmnxIPsecIsaGrpOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 14),
    _TmnxIPsecIsaGrpOperFlags_Type()
)
tmnxIPsecIsaGrpOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpOperFlags.setStatus("current")


class _TmnxIPsecIsaGrpMultiActive_Type(TruthValue):
    """Custom type tmnxIPsecIsaGrpMultiActive based on TruthValue"""


_TmnxIPsecIsaGrpMultiActive_Object = MibTableColumn
tmnxIPsecIsaGrpMultiActive = _TmnxIPsecIsaGrpMultiActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 15),
    _TmnxIPsecIsaGrpMultiActive_Type()
)
tmnxIPsecIsaGrpMultiActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpMultiActive.setStatus("current")


class _TmnxIPsecIsaGrpActiveMda_Type(Unsigned32):
    """Custom type tmnxIPsecIsaGrpActiveMda based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxIPsecIsaGrpActiveMda_Type.__name__ = "Unsigned32"
_TmnxIPsecIsaGrpActiveMda_Object = MibTableColumn
tmnxIPsecIsaGrpActiveMda = _TmnxIPsecIsaGrpActiveMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 16),
    _TmnxIPsecIsaGrpActiveMda_Type()
)
tmnxIPsecIsaGrpActiveMda.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpActiveMda.setStatus("current")
_TmnxIPsecIsaGrpIpTunnels_Type = Unsigned32
_TmnxIPsecIsaGrpIpTunnels_Object = MibTableColumn
tmnxIPsecIsaGrpIpTunnels = _TmnxIPsecIsaGrpIpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 17),
    _TmnxIPsecIsaGrpIpTunnels_Type()
)
tmnxIPsecIsaGrpIpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpIpTunnels.setStatus("current")
_TmnxIPsecIsaGrpIpMaxTunnels_Type = Unsigned32
_TmnxIPsecIsaGrpIpMaxTunnels_Object = MibTableColumn
tmnxIPsecIsaGrpIpMaxTunnels = _TmnxIPsecIsaGrpIpMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 18, 1, 18),
    _TmnxIPsecIsaGrpIpMaxTunnels_Type()
)
tmnxIPsecIsaGrpIpMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpIpMaxTunnels.setStatus("current")
_TmnxHsmdaMdaSchOvrTblLastChangd_Type = TimeStamp
_TmnxHsmdaMdaSchOvrTblLastChangd_Object = MibScalar
tmnxHsmdaMdaSchOvrTblLastChangd = _TmnxHsmdaMdaSchOvrTblLastChangd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 19),
    _TmnxHsmdaMdaSchOvrTblLastChangd_Type()
)
tmnxHsmdaMdaSchOvrTblLastChangd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrTblLastChangd.setStatus("obsolete")
_TmnxHsmdaMdaSchOvrTable_Object = MibTable
tmnxHsmdaMdaSchOvrTable = _TmnxHsmdaMdaSchOvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20)
)
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrTable.setStatus("obsolete")
_TmnxHsmdaMdaSchOvrEntry_Object = MibTableRow
tmnxHsmdaMdaSchOvrEntry = _TmnxHsmdaMdaSchOvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1)
)
tmnxHsmdaMdaSchOvrEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrEntry.setStatus("obsolete")
_TmnxHsmdaMdaSchOvrRowStatus_Type = RowStatus
_TmnxHsmdaMdaSchOvrRowStatus_Object = MibTableColumn
tmnxHsmdaMdaSchOvrRowStatus = _TmnxHsmdaMdaSchOvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 1),
    _TmnxHsmdaMdaSchOvrRowStatus_Type()
)
tmnxHsmdaMdaSchOvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrRowStatus.setStatus("obsolete")
_TmnxHsmdaMdaSchOvrLastChanged_Type = TimeStamp
_TmnxHsmdaMdaSchOvrLastChanged_Object = MibTableColumn
tmnxHsmdaMdaSchOvrLastChanged = _TmnxHsmdaMdaSchOvrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 2),
    _TmnxHsmdaMdaSchOvrLastChanged_Type()
)
tmnxHsmdaMdaSchOvrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrLastChanged.setStatus("obsolete")


class _TmnxHsmdaMdaSchOvrMaxRate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaMdaSchOvrMaxRate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrMaxRate_Object = MibTableColumn
tmnxHsmdaMdaSchOvrMaxRate = _TmnxHsmdaMdaSchOvrMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 3),
    _TmnxHsmdaMdaSchOvrMaxRate_Type()
)
tmnxHsmdaMdaSchOvrMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrMaxRate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrMaxRate.setUnits("Mbps")


class _TmnxHsmdaMdaSchOvrGrp1Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaMdaSchOvrGrp1Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrGrp1Rate_Object = MibTableColumn
tmnxHsmdaMdaSchOvrGrp1Rate = _TmnxHsmdaMdaSchOvrGrp1Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 4),
    _TmnxHsmdaMdaSchOvrGrp1Rate_Type()
)
tmnxHsmdaMdaSchOvrGrp1Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrGrp1Rate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrGrp1Rate.setUnits("Mbps")


class _TmnxHsmdaMdaSchOvrGrp2Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaMdaSchOvrGrp2Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrGrp2Rate_Object = MibTableColumn
tmnxHsmdaMdaSchOvrGrp2Rate = _TmnxHsmdaMdaSchOvrGrp2Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 5),
    _TmnxHsmdaMdaSchOvrGrp2Rate_Type()
)
tmnxHsmdaMdaSchOvrGrp2Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrGrp2Rate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrGrp2Rate.setUnits("Mbps")


class _TmnxHsmdaMdaSchOvrClass1Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass1Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass1Rate_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass1Rate = _TmnxHsmdaMdaSchOvrClass1Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 6),
    _TmnxHsmdaMdaSchOvrClass1Rate_Type()
)
tmnxHsmdaMdaSchOvrClass1Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass1Rate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass1Rate.setUnits("Mbps")


class _TmnxHsmdaMdaSchOvrClass1WtInGrp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass1WtInGrp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass1WtInGrp_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass1WtInGrp = _TmnxHsmdaMdaSchOvrClass1WtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 7),
    _TmnxHsmdaMdaSchOvrClass1WtInGrp_Type()
)
tmnxHsmdaMdaSchOvrClass1WtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass1WtInGrp.setStatus("obsolete")


class _TmnxHsmdaMdaSchOvrClass2Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass2Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass2Rate_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass2Rate = _TmnxHsmdaMdaSchOvrClass2Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 8),
    _TmnxHsmdaMdaSchOvrClass2Rate_Type()
)
tmnxHsmdaMdaSchOvrClass2Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass2Rate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass2Rate.setUnits("Mbps")


class _TmnxHsmdaMdaSchOvrClass2WtInGrp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass2WtInGrp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass2WtInGrp_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass2WtInGrp = _TmnxHsmdaMdaSchOvrClass2WtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 9),
    _TmnxHsmdaMdaSchOvrClass2WtInGrp_Type()
)
tmnxHsmdaMdaSchOvrClass2WtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass2WtInGrp.setStatus("obsolete")


class _TmnxHsmdaMdaSchOvrClass3Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass3Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass3Rate_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass3Rate = _TmnxHsmdaMdaSchOvrClass3Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 10),
    _TmnxHsmdaMdaSchOvrClass3Rate_Type()
)
tmnxHsmdaMdaSchOvrClass3Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass3Rate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass3Rate.setUnits("Mbps")


class _TmnxHsmdaMdaSchOvrClass3WtInGrp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass3WtInGrp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass3WtInGrp_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass3WtInGrp = _TmnxHsmdaMdaSchOvrClass3WtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 11),
    _TmnxHsmdaMdaSchOvrClass3WtInGrp_Type()
)
tmnxHsmdaMdaSchOvrClass3WtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass3WtInGrp.setStatus("obsolete")


class _TmnxHsmdaMdaSchOvrClass4Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass4Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass4Rate_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass4Rate = _TmnxHsmdaMdaSchOvrClass4Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 12),
    _TmnxHsmdaMdaSchOvrClass4Rate_Type()
)
tmnxHsmdaMdaSchOvrClass4Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass4Rate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass4Rate.setUnits("Mbps")


class _TmnxHsmdaMdaSchOvrClass4WtInGrp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass4WtInGrp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass4WtInGrp_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass4WtInGrp = _TmnxHsmdaMdaSchOvrClass4WtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 13),
    _TmnxHsmdaMdaSchOvrClass4WtInGrp_Type()
)
tmnxHsmdaMdaSchOvrClass4WtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass4WtInGrp.setStatus("obsolete")


class _TmnxHsmdaMdaSchOvrClass5Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass5Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass5Rate_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass5Rate = _TmnxHsmdaMdaSchOvrClass5Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 14),
    _TmnxHsmdaMdaSchOvrClass5Rate_Type()
)
tmnxHsmdaMdaSchOvrClass5Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass5Rate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass5Rate.setUnits("Mbps")


class _TmnxHsmdaMdaSchOvrClass5WtInGrp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass5WtInGrp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass5WtInGrp_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass5WtInGrp = _TmnxHsmdaMdaSchOvrClass5WtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 15),
    _TmnxHsmdaMdaSchOvrClass5WtInGrp_Type()
)
tmnxHsmdaMdaSchOvrClass5WtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass5WtInGrp.setStatus("obsolete")


class _TmnxHsmdaMdaSchOvrClass6Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass6Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass6Rate_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass6Rate = _TmnxHsmdaMdaSchOvrClass6Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 16),
    _TmnxHsmdaMdaSchOvrClass6Rate_Type()
)
tmnxHsmdaMdaSchOvrClass6Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass6Rate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass6Rate.setUnits("Mbps")


class _TmnxHsmdaMdaSchOvrClass6WtInGrp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass6WtInGrp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass6WtInGrp_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass6WtInGrp = _TmnxHsmdaMdaSchOvrClass6WtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 17),
    _TmnxHsmdaMdaSchOvrClass6WtInGrp_Type()
)
tmnxHsmdaMdaSchOvrClass6WtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass6WtInGrp.setStatus("obsolete")


class _TmnxHsmdaMdaSchOvrClass7Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass7Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass7Rate_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass7Rate = _TmnxHsmdaMdaSchOvrClass7Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 18),
    _TmnxHsmdaMdaSchOvrClass7Rate_Type()
)
tmnxHsmdaMdaSchOvrClass7Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass7Rate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass7Rate.setUnits("Mbps")


class _TmnxHsmdaMdaSchOvrClass7WtInGrp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass7WtInGrp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass7WtInGrp_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass7WtInGrp = _TmnxHsmdaMdaSchOvrClass7WtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 19),
    _TmnxHsmdaMdaSchOvrClass7WtInGrp_Type()
)
tmnxHsmdaMdaSchOvrClass7WtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass7WtInGrp.setStatus("obsolete")


class _TmnxHsmdaMdaSchOvrClass8Rate_Type(THsmdaPIRMRateOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass8Rate based on THsmdaPIRMRateOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass8Rate_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass8Rate = _TmnxHsmdaMdaSchOvrClass8Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 20),
    _TmnxHsmdaMdaSchOvrClass8Rate_Type()
)
tmnxHsmdaMdaSchOvrClass8Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass8Rate.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass8Rate.setUnits("Mbps")


class _TmnxHsmdaMdaSchOvrClass8WtInGrp_Type(THsmdaWeightOverride):
    """Custom type tmnxHsmdaMdaSchOvrClass8WtInGrp based on THsmdaWeightOverride"""
    defaultValue = -2


_TmnxHsmdaMdaSchOvrClass8WtInGrp_Object = MibTableColumn
tmnxHsmdaMdaSchOvrClass8WtInGrp = _TmnxHsmdaMdaSchOvrClass8WtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 20, 1, 21),
    _TmnxHsmdaMdaSchOvrClass8WtInGrp_Type()
)
tmnxHsmdaMdaSchOvrClass8WtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxHsmdaMdaSchOvrClass8WtInGrp.setStatus("obsolete")
_TmnxFPTable_Object = MibTable
tmnxFPTable = _TmnxFPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21)
)
if mibBuilder.loadTexts:
    tmnxFPTable.setStatus("current")
_TmnxFPEntry_Object = MibTableRow
tmnxFPEntry = _TmnxFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1)
)
tmnxFPEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNum"),
)
if mibBuilder.loadTexts:
    tmnxFPEntry.setStatus("current")
_TmnxFPNum_Type = Unsigned32
_TmnxFPNum_Object = MibTableColumn
tmnxFPNum = _TmnxFPNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 1),
    _TmnxFPNum_Type()
)
tmnxFPNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFPNum.setStatus("current")


class _TmnxFPMcPathMgmtBwPlcyName_Type(TNamedItem):
    """Custom type tmnxFPMcPathMgmtBwPlcyName based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxFPMcPathMgmtBwPlcyName_Object = MibTableColumn
tmnxFPMcPathMgmtBwPlcyName = _TmnxFPMcPathMgmtBwPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 2),
    _TmnxFPMcPathMgmtBwPlcyName_Type()
)
tmnxFPMcPathMgmtBwPlcyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPMcPathMgmtBwPlcyName.setStatus("current")


class _TmnxFPMcPathMgmtAdminState_Type(TmnxAdminState):
    """Custom type tmnxFPMcPathMgmtAdminState based on TmnxAdminState"""


_TmnxFPMcPathMgmtAdminState_Object = MibTableColumn
tmnxFPMcPathMgmtAdminState = _TmnxFPMcPathMgmtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 3),
    _TmnxFPMcPathMgmtAdminState_Type()
)
tmnxFPMcPathMgmtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPMcPathMgmtAdminState.setStatus("current")
_TmnxFPLastChanged_Type = TimeStamp
_TmnxFPLastChanged_Object = MibTableColumn
tmnxFPLastChanged = _TmnxFPLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 4),
    _TmnxFPLastChanged_Type()
)
tmnxFPLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPLastChanged.setStatus("current")


class _TmnxFPHiBwMcastSource_Type(TruthValue):
    """Custom type tmnxFPHiBwMcastSource based on TruthValue"""


_TmnxFPHiBwMcastSource_Object = MibTableColumn
tmnxFPHiBwMcastSource = _TmnxFPHiBwMcastSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 5),
    _TmnxFPHiBwMcastSource_Type()
)
tmnxFPHiBwMcastSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPHiBwMcastSource.setStatus("current")


class _TmnxFPHiBwMcastAlarm_Type(TruthValue):
    """Custom type tmnxFPHiBwMcastAlarm based on TruthValue"""


_TmnxFPHiBwMcastAlarm_Object = MibTableColumn
tmnxFPHiBwMcastAlarm = _TmnxFPHiBwMcastAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 6),
    _TmnxFPHiBwMcastAlarm_Type()
)
tmnxFPHiBwMcastAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPHiBwMcastAlarm.setStatus("current")
_TmnxFPHiBwMcastTapCount_Type = Gauge32
_TmnxFPHiBwMcastTapCount_Object = MibTableColumn
tmnxFPHiBwMcastTapCount = _TmnxFPHiBwMcastTapCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 7),
    _TmnxFPHiBwMcastTapCount_Type()
)
tmnxFPHiBwMcastTapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPHiBwMcastTapCount.setStatus("current")


class _TmnxFPHiBwMcastGroup_Type(Unsigned32):
    """Custom type tmnxFPHiBwMcastGroup based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxFPHiBwMcastGroup_Type.__name__ = "Unsigned32"
_TmnxFPHiBwMcastGroup_Object = MibTableColumn
tmnxFPHiBwMcastGroup = _TmnxFPHiBwMcastGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 8),
    _TmnxFPHiBwMcastGroup_Type()
)
tmnxFPHiBwMcastGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPHiBwMcastGroup.setStatus("current")


class _TmnxFPWredBufAllocMin_Type(Unsigned32):
    """Custom type tmnxFPWredBufAllocMin based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_TmnxFPWredBufAllocMin_Type.__name__ = "Unsigned32"
_TmnxFPWredBufAllocMin_Object = MibTableColumn
tmnxFPWredBufAllocMin = _TmnxFPWredBufAllocMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 9),
    _TmnxFPWredBufAllocMin_Type()
)
tmnxFPWredBufAllocMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPWredBufAllocMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFPWredBufAllocMin.setUnits("Hundredths of a percent")


class _TmnxFPWredBufAllocMax_Type(Unsigned32):
    """Custom type tmnxFPWredBufAllocMax based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_TmnxFPWredBufAllocMax_Type.__name__ = "Unsigned32"
_TmnxFPWredBufAllocMax_Object = MibTableColumn
tmnxFPWredBufAllocMax = _TmnxFPWredBufAllocMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 10),
    _TmnxFPWredBufAllocMax_Type()
)
tmnxFPWredBufAllocMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPWredBufAllocMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFPWredBufAllocMax.setUnits("Hundredths of a percent")


class _TmnxFPWredResvCbsMin_Type(Unsigned32):
    """Custom type tmnxFPWredResvCbsMin based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_TmnxFPWredResvCbsMin_Type.__name__ = "Unsigned32"
_TmnxFPWredResvCbsMin_Object = MibTableColumn
tmnxFPWredResvCbsMin = _TmnxFPWredResvCbsMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 11),
    _TmnxFPWredResvCbsMin_Type()
)
tmnxFPWredResvCbsMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPWredResvCbsMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFPWredResvCbsMin.setUnits("Hundredths of a percent")


class _TmnxFPWredResvCbsMax_Type(Unsigned32):
    """Custom type tmnxFPWredResvCbsMax based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_TmnxFPWredResvCbsMax_Type.__name__ = "Unsigned32"
_TmnxFPWredResvCbsMax_Object = MibTableColumn
tmnxFPWredResvCbsMax = _TmnxFPWredResvCbsMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 12),
    _TmnxFPWredResvCbsMax_Type()
)
tmnxFPWredResvCbsMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPWredResvCbsMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxFPWredResvCbsMax.setUnits("Hundredths of a percent")


class _TmnxFPWredSlopePolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxFPWredSlopePolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("default")


_TmnxFPWredSlopePolicy_Object = MibTableColumn
tmnxFPWredSlopePolicy = _TmnxFPWredSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 13),
    _TmnxFPWredSlopePolicy_Type()
)
tmnxFPWredSlopePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPWredSlopePolicy.setStatus("current")


class _TmnxFPWredAdminState_Type(TmnxAdminState):
    """Custom type tmnxFPWredAdminState based on TmnxAdminState"""


_TmnxFPWredAdminState_Object = MibTableColumn
tmnxFPWredAdminState = _TmnxFPWredAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 14),
    _TmnxFPWredAdminState_Type()
)
tmnxFPWredAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPWredAdminState.setStatus("current")


class _TmnxFPHiBwMcastDefaultPathsOnly_Type(TruthValue):
    """Custom type tmnxFPHiBwMcastDefaultPathsOnly based on TruthValue"""


_TmnxFPHiBwMcastDefaultPathsOnly_Object = MibTableColumn
tmnxFPHiBwMcastDefaultPathsOnly = _TmnxFPHiBwMcastDefaultPathsOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 21, 1, 15),
    _TmnxFPHiBwMcastDefaultPathsOnly_Type()
)
tmnxFPHiBwMcastDefaultPathsOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFPHiBwMcastDefaultPathsOnly.setStatus("current")
_TmnxFPAccIngQGrpTableLastChgd_Type = TimeStamp
_TmnxFPAccIngQGrpTableLastChgd_Object = MibScalar
tmnxFPAccIngQGrpTableLastChgd = _TmnxFPAccIngQGrpTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 22),
    _TmnxFPAccIngQGrpTableLastChgd_Type()
)
tmnxFPAccIngQGrpTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpTableLastChgd.setStatus("current")
_TmnxFPAccIngQGrpTable_Object = MibTable
tmnxFPAccIngQGrpTable = _TmnxFPAccIngQGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 23)
)
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpTable.setStatus("current")
_TmnxFPAccIngQGrpEntry_Object = MibTableRow
tmnxFPAccIngQGrpEntry = _TmnxFPAccIngQGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 23, 1)
)
tmnxFPAccIngQGrpEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpName"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpInstanceId"),
)
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpEntry.setStatus("current")
_TmnxFPAccIngQGrpName_Type = TNamedItem
_TmnxFPAccIngQGrpName_Object = MibTableColumn
tmnxFPAccIngQGrpName = _TmnxFPAccIngQGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 23, 1, 1),
    _TmnxFPAccIngQGrpName_Type()
)
tmnxFPAccIngQGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpName.setStatus("current")


class _TmnxFPAccIngQGrpInstanceId_Type(Unsigned32):
    """Custom type tmnxFPAccIngQGrpInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxFPAccIngQGrpInstanceId_Type.__name__ = "Unsigned32"
_TmnxFPAccIngQGrpInstanceId_Object = MibTableColumn
tmnxFPAccIngQGrpInstanceId = _TmnxFPAccIngQGrpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 23, 1, 2),
    _TmnxFPAccIngQGrpInstanceId_Type()
)
tmnxFPAccIngQGrpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpInstanceId.setStatus("current")
_TmnxFPAccIngQGrpRowStatus_Type = RowStatus
_TmnxFPAccIngQGrpRowStatus_Object = MibTableColumn
tmnxFPAccIngQGrpRowStatus = _TmnxFPAccIngQGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 23, 1, 3),
    _TmnxFPAccIngQGrpRowStatus_Type()
)
tmnxFPAccIngQGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpRowStatus.setStatus("current")
_TmnxFPAccIngQGrpLastChgd_Type = TimeStamp
_TmnxFPAccIngQGrpLastChgd_Object = MibTableColumn
tmnxFPAccIngQGrpLastChgd = _TmnxFPAccIngQGrpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 23, 1, 4),
    _TmnxFPAccIngQGrpLastChgd_Type()
)
tmnxFPAccIngQGrpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpLastChgd.setStatus("current")


class _TmnxFPAccIngQGrpAcctgPolId_Type(Unsigned32):
    """Custom type tmnxFPAccIngQGrpAcctgPolId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxFPAccIngQGrpAcctgPolId_Type.__name__ = "Unsigned32"
_TmnxFPAccIngQGrpAcctgPolId_Object = MibTableColumn
tmnxFPAccIngQGrpAcctgPolId = _TmnxFPAccIngQGrpAcctgPolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 23, 1, 5),
    _TmnxFPAccIngQGrpAcctgPolId_Type()
)
tmnxFPAccIngQGrpAcctgPolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpAcctgPolId.setStatus("current")


class _TmnxFPAccIngQGrpCollectStats_Type(TruthValue):
    """Custom type tmnxFPAccIngQGrpCollectStats based on TruthValue"""


_TmnxFPAccIngQGrpCollectStats_Object = MibTableColumn
tmnxFPAccIngQGrpCollectStats = _TmnxFPAccIngQGrpCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 23, 1, 6),
    _TmnxFPAccIngQGrpCollectStats_Type()
)
tmnxFPAccIngQGrpCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpCollectStats.setStatus("current")


class _TmnxFPAccIngQGrpDescr_Type(TItemDescription):
    """Custom type tmnxFPAccIngQGrpDescr based on TItemDescription"""
    defaultHexValue = ""


_TmnxFPAccIngQGrpDescr_Object = MibTableColumn
tmnxFPAccIngQGrpDescr = _TmnxFPAccIngQGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 23, 1, 7),
    _TmnxFPAccIngQGrpDescr_Type()
)
tmnxFPAccIngQGrpDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpDescr.setStatus("current")


class _TmnxFPAccIngQGrpPolicerPol_Type(TNamedItemOrEmpty):
    """Custom type tmnxFPAccIngQGrpPolicerPol based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxFPAccIngQGrpPolicerPol_Object = MibTableColumn
tmnxFPAccIngQGrpPolicerPol = _TmnxFPAccIngQGrpPolicerPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 23, 1, 8),
    _TmnxFPAccIngQGrpPolicerPol_Type()
)
tmnxFPAccIngQGrpPolicerPol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpPolicerPol.setStatus("current")
_TmnxFPNetIngQGrpTableLastChgd_Type = TimeStamp
_TmnxFPNetIngQGrpTableLastChgd_Object = MibScalar
tmnxFPNetIngQGrpTableLastChgd = _TmnxFPNetIngQGrpTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 24),
    _TmnxFPNetIngQGrpTableLastChgd_Type()
)
tmnxFPNetIngQGrpTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpTableLastChgd.setStatus("current")
_TmnxFPNetIngQGrpTable_Object = MibTable
tmnxFPNetIngQGrpTable = _TmnxFPNetIngQGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 25)
)
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpTable.setStatus("current")
_TmnxFPNetIngQGrpEntry_Object = MibTableRow
tmnxFPNetIngQGrpEntry = _TmnxFPNetIngQGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 25, 1)
)
tmnxFPNetIngQGrpEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpName"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpInstanceId"),
)
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpEntry.setStatus("current")
_TmnxFPNetIngQGrpName_Type = TNamedItem
_TmnxFPNetIngQGrpName_Object = MibTableColumn
tmnxFPNetIngQGrpName = _TmnxFPNetIngQGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 25, 1, 1),
    _TmnxFPNetIngQGrpName_Type()
)
tmnxFPNetIngQGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpName.setStatus("current")


class _TmnxFPNetIngQGrpInstanceId_Type(Unsigned32):
    """Custom type tmnxFPNetIngQGrpInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxFPNetIngQGrpInstanceId_Type.__name__ = "Unsigned32"
_TmnxFPNetIngQGrpInstanceId_Object = MibTableColumn
tmnxFPNetIngQGrpInstanceId = _TmnxFPNetIngQGrpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 25, 1, 2),
    _TmnxFPNetIngQGrpInstanceId_Type()
)
tmnxFPNetIngQGrpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpInstanceId.setStatus("current")
_TmnxFPNetIngQGrpRowStatus_Type = RowStatus
_TmnxFPNetIngQGrpRowStatus_Object = MibTableColumn
tmnxFPNetIngQGrpRowStatus = _TmnxFPNetIngQGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 25, 1, 3),
    _TmnxFPNetIngQGrpRowStatus_Type()
)
tmnxFPNetIngQGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpRowStatus.setStatus("current")
_TmnxFPNetIngQGrpLastChgd_Type = TimeStamp
_TmnxFPNetIngQGrpLastChgd_Object = MibTableColumn
tmnxFPNetIngQGrpLastChgd = _TmnxFPNetIngQGrpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 25, 1, 4),
    _TmnxFPNetIngQGrpLastChgd_Type()
)
tmnxFPNetIngQGrpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpLastChgd.setStatus("current")


class _TmnxFPNetIngQGrpAcctgPolId_Type(Unsigned32):
    """Custom type tmnxFPNetIngQGrpAcctgPolId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxFPNetIngQGrpAcctgPolId_Type.__name__ = "Unsigned32"
_TmnxFPNetIngQGrpAcctgPolId_Object = MibTableColumn
tmnxFPNetIngQGrpAcctgPolId = _TmnxFPNetIngQGrpAcctgPolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 25, 1, 5),
    _TmnxFPNetIngQGrpAcctgPolId_Type()
)
tmnxFPNetIngQGrpAcctgPolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpAcctgPolId.setStatus("current")


class _TmnxFPNetIngQGrpCollectStats_Type(TruthValue):
    """Custom type tmnxFPNetIngQGrpCollectStats based on TruthValue"""


_TmnxFPNetIngQGrpCollectStats_Object = MibTableColumn
tmnxFPNetIngQGrpCollectStats = _TmnxFPNetIngQGrpCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 25, 1, 6),
    _TmnxFPNetIngQGrpCollectStats_Type()
)
tmnxFPNetIngQGrpCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpCollectStats.setStatus("current")


class _TmnxFPNetIngQGrpDescr_Type(TItemDescription):
    """Custom type tmnxFPNetIngQGrpDescr based on TItemDescription"""
    defaultHexValue = ""


_TmnxFPNetIngQGrpDescr_Object = MibTableColumn
tmnxFPNetIngQGrpDescr = _TmnxFPNetIngQGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 25, 1, 7),
    _TmnxFPNetIngQGrpDescr_Type()
)
tmnxFPNetIngQGrpDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpDescr.setStatus("current")


class _TmnxFPNetIngQGrpPolicerPol_Type(TNamedItemOrEmpty):
    """Custom type tmnxFPNetIngQGrpPolicerPol based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxFPNetIngQGrpPolicerPol_Object = MibTableColumn
tmnxFPNetIngQGrpPolicerPol = _TmnxFPNetIngQGrpPolicerPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 25, 1, 8),
    _TmnxFPNetIngQGrpPolicerPol_Type()
)
tmnxFPNetIngQGrpPolicerPol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpPolicerPol.setStatus("current")
_TmnxFabricTypeTable_Object = MibTable
tmnxFabricTypeTable = _TmnxFabricTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 26)
)
if mibBuilder.loadTexts:
    tmnxFabricTypeTable.setStatus("current")
_TmnxFabricTypeEntry_Object = MibTableRow
tmnxFabricTypeEntry = _TmnxFabricTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 26, 1)
)
tmnxFabricTypeEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFabricTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxFabricTypeEntry.setStatus("current")
_TmnxFabricTypeIndex_Type = TmnxFabricType
_TmnxFabricTypeIndex_Object = MibTableColumn
tmnxFabricTypeIndex = _TmnxFabricTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 26, 1, 1),
    _TmnxFabricTypeIndex_Type()
)
tmnxFabricTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFabricTypeIndex.setStatus("current")
_TmnxFabricTypeName_Type = TNamedItemOrEmpty
_TmnxFabricTypeName_Object = MibTableColumn
tmnxFabricTypeName = _TmnxFabricTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 26, 1, 2),
    _TmnxFabricTypeName_Type()
)
tmnxFabricTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFabricTypeName.setStatus("current")
_TmnxFabricTypeDescription_Type = TItemDescription
_TmnxFabricTypeDescription_Object = MibTableColumn
tmnxFabricTypeDescription = _TmnxFabricTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 26, 1, 3),
    _TmnxFabricTypeDescription_Type()
)
tmnxFabricTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFabricTypeDescription.setStatus("current")
_TmnxFabricTypeStatus_Type = TruthValue
_TmnxFabricTypeStatus_Object = MibTableColumn
tmnxFabricTypeStatus = _TmnxFabricTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 26, 1, 4),
    _TmnxFabricTypeStatus_Type()
)
tmnxFabricTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFabricTypeStatus.setStatus("current")
_TmnxFPNetIngQGrpPStatTable_Object = MibTable
tmnxFPNetIngQGrpPStatTable = _TmnxFPNetIngQGrpPStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27)
)
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpPStatTable.setStatus("current")
_TmnxFPNetIngQGrpPStatEntry_Object = MibTableRow
tmnxFPNetIngQGrpPStatEntry = _TmnxFPNetIngQGrpPStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1)
)
tmnxFPNetIngQGrpPStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpName"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpInstanceId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpPStatPolicerId"),
)
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpPStatEntry.setStatus("current")
_TmnxFPNetIngQGrpPStatPolicerId_Type = TIngPolicerId
_TmnxFPNetIngQGrpPStatPolicerId_Object = MibTableColumn
tmnxFPNetIngQGrpPStatPolicerId = _TmnxFPNetIngQGrpPStatPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 1),
    _TmnxFPNetIngQGrpPStatPolicerId_Type()
)
tmnxFPNetIngQGrpPStatPolicerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpPStatPolicerId.setStatus("current")
_TmnxFPNetIngQGrpPStatMode_Type = TmnxIngPolicerStatMode
_TmnxFPNetIngQGrpPStatMode_Object = MibTableColumn
tmnxFPNetIngQGrpPStatMode = _TmnxFPNetIngQGrpPStatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 2),
    _TmnxFPNetIngQGrpPStatMode_Type()
)
tmnxFPNetIngQGrpPStatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQGrpPStatMode.setStatus("current")
_TmnxFPNetIngQgPStOffHPrioPkts_Type = Counter64
_TmnxFPNetIngQgPStOffHPrioPkts_Object = MibTableColumn
tmnxFPNetIngQgPStOffHPrioPkts = _TmnxFPNetIngQgPStOffHPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 3),
    _TmnxFPNetIngQgPStOffHPrioPkts_Type()
)
tmnxFPNetIngQgPStOffHPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffHPrioPkts.setStatus("current")
_TmnxFPNetIngQgPStOffHPrioPktsL_Type = Counter32
_TmnxFPNetIngQgPStOffHPrioPktsL_Object = MibTableColumn
tmnxFPNetIngQgPStOffHPrioPktsL = _TmnxFPNetIngQgPStOffHPrioPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 4),
    _TmnxFPNetIngQgPStOffHPrioPktsL_Type()
)
tmnxFPNetIngQgPStOffHPrioPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffHPrioPktsL.setStatus("current")
_TmnxFPNetIngQgPStOffHPrioPktsH_Type = Counter32
_TmnxFPNetIngQgPStOffHPrioPktsH_Object = MibTableColumn
tmnxFPNetIngQgPStOffHPrioPktsH = _TmnxFPNetIngQgPStOffHPrioPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 5),
    _TmnxFPNetIngQgPStOffHPrioPktsH_Type()
)
tmnxFPNetIngQgPStOffHPrioPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffHPrioPktsH.setStatus("current")
_TmnxFPNetIngQgPStDrpHPrioPkts_Type = Counter64
_TmnxFPNetIngQgPStDrpHPrioPkts_Object = MibTableColumn
tmnxFPNetIngQgPStDrpHPrioPkts = _TmnxFPNetIngQgPStDrpHPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 6),
    _TmnxFPNetIngQgPStDrpHPrioPkts_Type()
)
tmnxFPNetIngQgPStDrpHPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpHPrioPkts.setStatus("current")
_TmnxFPNetIngQgPStDrpHPrioPktsL_Type = Counter32
_TmnxFPNetIngQgPStDrpHPrioPktsL_Object = MibTableColumn
tmnxFPNetIngQgPStDrpHPrioPktsL = _TmnxFPNetIngQgPStDrpHPrioPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 7),
    _TmnxFPNetIngQgPStDrpHPrioPktsL_Type()
)
tmnxFPNetIngQgPStDrpHPrioPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpHPrioPktsL.setStatus("current")
_TmnxFPNetIngQgPStDrpHPrioPktsH_Type = Counter32
_TmnxFPNetIngQgPStDrpHPrioPktsH_Object = MibTableColumn
tmnxFPNetIngQgPStDrpHPrioPktsH = _TmnxFPNetIngQgPStDrpHPrioPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 8),
    _TmnxFPNetIngQgPStDrpHPrioPktsH_Type()
)
tmnxFPNetIngQgPStDrpHPrioPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpHPrioPktsH.setStatus("current")
_TmnxFPNetIngQgPStOffLPrioPkts_Type = Counter64
_TmnxFPNetIngQgPStOffLPrioPkts_Object = MibTableColumn
tmnxFPNetIngQgPStOffLPrioPkts = _TmnxFPNetIngQgPStOffLPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 9),
    _TmnxFPNetIngQgPStOffLPrioPkts_Type()
)
tmnxFPNetIngQgPStOffLPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffLPrioPkts.setStatus("current")
_TmnxFPNetIngQgPStOffLPrioPktsL_Type = Counter32
_TmnxFPNetIngQgPStOffLPrioPktsL_Object = MibTableColumn
tmnxFPNetIngQgPStOffLPrioPktsL = _TmnxFPNetIngQgPStOffLPrioPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 10),
    _TmnxFPNetIngQgPStOffLPrioPktsL_Type()
)
tmnxFPNetIngQgPStOffLPrioPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffLPrioPktsL.setStatus("current")
_TmnxFPNetIngQgPStOffLPrioPktsH_Type = Counter32
_TmnxFPNetIngQgPStOffLPrioPktsH_Object = MibTableColumn
tmnxFPNetIngQgPStOffLPrioPktsH = _TmnxFPNetIngQgPStOffLPrioPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 11),
    _TmnxFPNetIngQgPStOffLPrioPktsH_Type()
)
tmnxFPNetIngQgPStOffLPrioPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffLPrioPktsH.setStatus("current")
_TmnxFPNetIngQgPStDrpLPrioPkts_Type = Counter64
_TmnxFPNetIngQgPStDrpLPrioPkts_Object = MibTableColumn
tmnxFPNetIngQgPStDrpLPrioPkts = _TmnxFPNetIngQgPStDrpLPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 12),
    _TmnxFPNetIngQgPStDrpLPrioPkts_Type()
)
tmnxFPNetIngQgPStDrpLPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpLPrioPkts.setStatus("current")
_TmnxFPNetIngQgPStDrpLPrioPktsL_Type = Counter32
_TmnxFPNetIngQgPStDrpLPrioPktsL_Object = MibTableColumn
tmnxFPNetIngQgPStDrpLPrioPktsL = _TmnxFPNetIngQgPStDrpLPrioPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 13),
    _TmnxFPNetIngQgPStDrpLPrioPktsL_Type()
)
tmnxFPNetIngQgPStDrpLPrioPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpLPrioPktsL.setStatus("current")
_TmnxFPNetIngQgPStDrpLPrioPktsH_Type = Counter32
_TmnxFPNetIngQgPStDrpLPrioPktsH_Object = MibTableColumn
tmnxFPNetIngQgPStDrpLPrioPktsH = _TmnxFPNetIngQgPStDrpLPrioPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 14),
    _TmnxFPNetIngQgPStDrpLPrioPktsH_Type()
)
tmnxFPNetIngQgPStDrpLPrioPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpLPrioPktsH.setStatus("current")
_TmnxFPNetIngQgPStOffHPrioOcts_Type = Counter64
_TmnxFPNetIngQgPStOffHPrioOcts_Object = MibTableColumn
tmnxFPNetIngQgPStOffHPrioOcts = _TmnxFPNetIngQgPStOffHPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 15),
    _TmnxFPNetIngQgPStOffHPrioOcts_Type()
)
tmnxFPNetIngQgPStOffHPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffHPrioOcts.setStatus("current")
_TmnxFPNetIngQgPStOffHPrioOctsL_Type = Counter32
_TmnxFPNetIngQgPStOffHPrioOctsL_Object = MibTableColumn
tmnxFPNetIngQgPStOffHPrioOctsL = _TmnxFPNetIngQgPStOffHPrioOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 16),
    _TmnxFPNetIngQgPStOffHPrioOctsL_Type()
)
tmnxFPNetIngQgPStOffHPrioOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffHPrioOctsL.setStatus("current")
_TmnxFPNetIngQgPStOffHPrioOctsH_Type = Counter32
_TmnxFPNetIngQgPStOffHPrioOctsH_Object = MibTableColumn
tmnxFPNetIngQgPStOffHPrioOctsH = _TmnxFPNetIngQgPStOffHPrioOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 17),
    _TmnxFPNetIngQgPStOffHPrioOctsH_Type()
)
tmnxFPNetIngQgPStOffHPrioOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffHPrioOctsH.setStatus("current")
_TmnxFPNetIngQgPStDrpHPrioOcts_Type = Counter64
_TmnxFPNetIngQgPStDrpHPrioOcts_Object = MibTableColumn
tmnxFPNetIngQgPStDrpHPrioOcts = _TmnxFPNetIngQgPStDrpHPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 18),
    _TmnxFPNetIngQgPStDrpHPrioOcts_Type()
)
tmnxFPNetIngQgPStDrpHPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpHPrioOcts.setStatus("current")
_TmnxFPNetIngQgPStDrpHPrioOctsL_Type = Counter32
_TmnxFPNetIngQgPStDrpHPrioOctsL_Object = MibTableColumn
tmnxFPNetIngQgPStDrpHPrioOctsL = _TmnxFPNetIngQgPStDrpHPrioOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 19),
    _TmnxFPNetIngQgPStDrpHPrioOctsL_Type()
)
tmnxFPNetIngQgPStDrpHPrioOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpHPrioOctsL.setStatus("current")
_TmnxFPNetIngQgPStDrpHPrioOctsH_Type = Counter32
_TmnxFPNetIngQgPStDrpHPrioOctsH_Object = MibTableColumn
tmnxFPNetIngQgPStDrpHPrioOctsH = _TmnxFPNetIngQgPStDrpHPrioOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 20),
    _TmnxFPNetIngQgPStDrpHPrioOctsH_Type()
)
tmnxFPNetIngQgPStDrpHPrioOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpHPrioOctsH.setStatus("current")
_TmnxFPNetIngQgPStOffLPrioOcts_Type = Counter64
_TmnxFPNetIngQgPStOffLPrioOcts_Object = MibTableColumn
tmnxFPNetIngQgPStOffLPrioOcts = _TmnxFPNetIngQgPStOffLPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 21),
    _TmnxFPNetIngQgPStOffLPrioOcts_Type()
)
tmnxFPNetIngQgPStOffLPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffLPrioOcts.setStatus("current")
_TmnxFPNetIngQgPStOffLPrioOctsL_Type = Counter32
_TmnxFPNetIngQgPStOffLPrioOctsL_Object = MibTableColumn
tmnxFPNetIngQgPStOffLPrioOctsL = _TmnxFPNetIngQgPStOffLPrioOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 22),
    _TmnxFPNetIngQgPStOffLPrioOctsL_Type()
)
tmnxFPNetIngQgPStOffLPrioOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffLPrioOctsL.setStatus("current")
_TmnxFPNetIngQgPStOffLPrioOctsH_Type = Counter32
_TmnxFPNetIngQgPStOffLPrioOctsH_Object = MibTableColumn
tmnxFPNetIngQgPStOffLPrioOctsH = _TmnxFPNetIngQgPStOffLPrioOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 23),
    _TmnxFPNetIngQgPStOffLPrioOctsH_Type()
)
tmnxFPNetIngQgPStOffLPrioOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStOffLPrioOctsH.setStatus("current")
_TmnxFPNetIngQgPStDrpLPrioOcts_Type = Counter64
_TmnxFPNetIngQgPStDrpLPrioOcts_Object = MibTableColumn
tmnxFPNetIngQgPStDrpLPrioOcts = _TmnxFPNetIngQgPStDrpLPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 24),
    _TmnxFPNetIngQgPStDrpLPrioOcts_Type()
)
tmnxFPNetIngQgPStDrpLPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpLPrioOcts.setStatus("current")
_TmnxFPNetIngQgPStDrpLPrioOctsL_Type = Counter32
_TmnxFPNetIngQgPStDrpLPrioOctsL_Object = MibTableColumn
tmnxFPNetIngQgPStDrpLPrioOctsL = _TmnxFPNetIngQgPStDrpLPrioOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 25),
    _TmnxFPNetIngQgPStDrpLPrioOctsL_Type()
)
tmnxFPNetIngQgPStDrpLPrioOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpLPrioOctsL.setStatus("current")
_TmnxFPNetIngQgPStDrpLPrioOctsH_Type = Counter32
_TmnxFPNetIngQgPStDrpLPrioOctsH_Object = MibTableColumn
tmnxFPNetIngQgPStDrpLPrioOctsH = _TmnxFPNetIngQgPStDrpLPrioOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 26),
    _TmnxFPNetIngQgPStDrpLPrioOctsH_Type()
)
tmnxFPNetIngQgPStDrpLPrioOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStDrpLPrioOctsH.setStatus("current")
_TmnxFPNetIngQgPStFwdInProfPkts_Type = Counter64
_TmnxFPNetIngQgPStFwdInProfPkts_Object = MibTableColumn
tmnxFPNetIngQgPStFwdInProfPkts = _TmnxFPNetIngQgPStFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 27),
    _TmnxFPNetIngQgPStFwdInProfPkts_Type()
)
tmnxFPNetIngQgPStFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdInProfPkts.setStatus("current")
_TmnxFPNetIngQgPStFwdInProfPktsL_Type = Counter32
_TmnxFPNetIngQgPStFwdInProfPktsL_Object = MibTableColumn
tmnxFPNetIngQgPStFwdInProfPktsL = _TmnxFPNetIngQgPStFwdInProfPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 28),
    _TmnxFPNetIngQgPStFwdInProfPktsL_Type()
)
tmnxFPNetIngQgPStFwdInProfPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdInProfPktsL.setStatus("current")
_TmnxFPNetIngQgPStFwdInProfPktsH_Type = Counter32
_TmnxFPNetIngQgPStFwdInProfPktsH_Object = MibTableColumn
tmnxFPNetIngQgPStFwdInProfPktsH = _TmnxFPNetIngQgPStFwdInProfPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 29),
    _TmnxFPNetIngQgPStFwdInProfPktsH_Type()
)
tmnxFPNetIngQgPStFwdInProfPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdInProfPktsH.setStatus("current")
_TmnxFPNetIngQgPStFwdOutProfPkts_Type = Counter64
_TmnxFPNetIngQgPStFwdOutProfPkts_Object = MibTableColumn
tmnxFPNetIngQgPStFwdOutProfPkts = _TmnxFPNetIngQgPStFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 30),
    _TmnxFPNetIngQgPStFwdOutProfPkts_Type()
)
tmnxFPNetIngQgPStFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdOutProfPkts.setStatus("current")
_TmnxFPNetIngQgPStFwdOutProfPktsL_Type = Counter32
_TmnxFPNetIngQgPStFwdOutProfPktsL_Object = MibTableColumn
tmnxFPNetIngQgPStFwdOutProfPktsL = _TmnxFPNetIngQgPStFwdOutProfPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 31),
    _TmnxFPNetIngQgPStFwdOutProfPktsL_Type()
)
tmnxFPNetIngQgPStFwdOutProfPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdOutProfPktsL.setStatus("current")
_TmnxFPNetIngQgPStFwdOutProfPktsH_Type = Counter32
_TmnxFPNetIngQgPStFwdOutProfPktsH_Object = MibTableColumn
tmnxFPNetIngQgPStFwdOutProfPktsH = _TmnxFPNetIngQgPStFwdOutProfPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 32),
    _TmnxFPNetIngQgPStFwdOutProfPktsH_Type()
)
tmnxFPNetIngQgPStFwdOutProfPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdOutProfPktsH.setStatus("current")
_TmnxFPNetIngQgPStFwdInProfOcts_Type = Counter64
_TmnxFPNetIngQgPStFwdInProfOcts_Object = MibTableColumn
tmnxFPNetIngQgPStFwdInProfOcts = _TmnxFPNetIngQgPStFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 33),
    _TmnxFPNetIngQgPStFwdInProfOcts_Type()
)
tmnxFPNetIngQgPStFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdInProfOcts.setStatus("current")
_TmnxFPNetIngQgPStFwdInProfOctsL_Type = Counter32
_TmnxFPNetIngQgPStFwdInProfOctsL_Object = MibTableColumn
tmnxFPNetIngQgPStFwdInProfOctsL = _TmnxFPNetIngQgPStFwdInProfOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 34),
    _TmnxFPNetIngQgPStFwdInProfOctsL_Type()
)
tmnxFPNetIngQgPStFwdInProfOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdInProfOctsL.setStatus("current")
_TmnxFPNetIngQgPStFwdInProfOctsH_Type = Counter32
_TmnxFPNetIngQgPStFwdInProfOctsH_Object = MibTableColumn
tmnxFPNetIngQgPStFwdInProfOctsH = _TmnxFPNetIngQgPStFwdInProfOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 35),
    _TmnxFPNetIngQgPStFwdInProfOctsH_Type()
)
tmnxFPNetIngQgPStFwdInProfOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdInProfOctsH.setStatus("current")
_TmnxFPNetIngQgPStFwdOutProfOcts_Type = Counter64
_TmnxFPNetIngQgPStFwdOutProfOcts_Object = MibTableColumn
tmnxFPNetIngQgPStFwdOutProfOcts = _TmnxFPNetIngQgPStFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 36),
    _TmnxFPNetIngQgPStFwdOutProfOcts_Type()
)
tmnxFPNetIngQgPStFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdOutProfOcts.setStatus("current")
_TmnxFPNetIngQgPStFwdOutProfOctsL_Type = Counter32
_TmnxFPNetIngQgPStFwdOutProfOctsL_Object = MibTableColumn
tmnxFPNetIngQgPStFwdOutProfOctsL = _TmnxFPNetIngQgPStFwdOutProfOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 37),
    _TmnxFPNetIngQgPStFwdOutProfOctsL_Type()
)
tmnxFPNetIngQgPStFwdOutProfOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdOutProfOctsL.setStatus("current")
_TmnxFPNetIngQgPStFwdOutProfOctsH_Type = Counter32
_TmnxFPNetIngQgPStFwdOutProfOctsH_Object = MibTableColumn
tmnxFPNetIngQgPStFwdOutProfOctsH = _TmnxFPNetIngQgPStFwdOutProfOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 38),
    _TmnxFPNetIngQgPStFwdOutProfOctsH_Type()
)
tmnxFPNetIngQgPStFwdOutProfOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStFwdOutProfOctsH.setStatus("current")
_TmnxFPNetIngQgPStUncolPktsOff_Type = Counter64
_TmnxFPNetIngQgPStUncolPktsOff_Object = MibTableColumn
tmnxFPNetIngQgPStUncolPktsOff = _TmnxFPNetIngQgPStUncolPktsOff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 39),
    _TmnxFPNetIngQgPStUncolPktsOff_Type()
)
tmnxFPNetIngQgPStUncolPktsOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStUncolPktsOff.setStatus("current")
_TmnxFPNetIngQgPStUncolPktsOffL_Type = Counter32
_TmnxFPNetIngQgPStUncolPktsOffL_Object = MibTableColumn
tmnxFPNetIngQgPStUncolPktsOffL = _TmnxFPNetIngQgPStUncolPktsOffL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 40),
    _TmnxFPNetIngQgPStUncolPktsOffL_Type()
)
tmnxFPNetIngQgPStUncolPktsOffL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStUncolPktsOffL.setStatus("current")
_TmnxFPNetIngQgPStUncolPktsOffH_Type = Counter32
_TmnxFPNetIngQgPStUncolPktsOffH_Object = MibTableColumn
tmnxFPNetIngQgPStUncolPktsOffH = _TmnxFPNetIngQgPStUncolPktsOffH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 41),
    _TmnxFPNetIngQgPStUncolPktsOffH_Type()
)
tmnxFPNetIngQgPStUncolPktsOffH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStUncolPktsOffH.setStatus("current")
_TmnxFPNetIngQgPStUncolOctsOff_Type = Counter64
_TmnxFPNetIngQgPStUncolOctsOff_Object = MibTableColumn
tmnxFPNetIngQgPStUncolOctsOff = _TmnxFPNetIngQgPStUncolOctsOff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 42),
    _TmnxFPNetIngQgPStUncolOctsOff_Type()
)
tmnxFPNetIngQgPStUncolOctsOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStUncolOctsOff.setStatus("current")
_TmnxFPNetIngQgPStUncolOctsOffL_Type = Counter32
_TmnxFPNetIngQgPStUncolOctsOffL_Object = MibTableColumn
tmnxFPNetIngQgPStUncolOctsOffL = _TmnxFPNetIngQgPStUncolOctsOffL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 43),
    _TmnxFPNetIngQgPStUncolOctsOffL_Type()
)
tmnxFPNetIngQgPStUncolOctsOffL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStUncolOctsOffL.setStatus("current")
_TmnxFPNetIngQgPStUncolOctsOffH_Type = Counter32
_TmnxFPNetIngQgPStUncolOctsOffH_Object = MibTableColumn
tmnxFPNetIngQgPStUncolOctsOffH = _TmnxFPNetIngQgPStUncolOctsOffH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 27, 1, 44),
    _TmnxFPNetIngQgPStUncolOctsOffH_Type()
)
tmnxFPNetIngQgPStUncolOctsOffH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPNetIngQgPStUncolOctsOffH.setStatus("current")
_TmnxFPAccIngQGrpPStatTable_Object = MibTable
tmnxFPAccIngQGrpPStatTable = _TmnxFPAccIngQGrpPStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28)
)
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpPStatTable.setStatus("current")
_TmnxFPAccIngQGrpPStatEntry_Object = MibTableRow
tmnxFPAccIngQGrpPStatEntry = _TmnxFPAccIngQGrpPStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1)
)
tmnxFPAccIngQGrpPStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpName"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpInstanceId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpPStatPolicerId"),
)
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpPStatEntry.setStatus("current")
_TmnxFPAccIngQGrpPStatPolicerId_Type = TIngPolicerId
_TmnxFPAccIngQGrpPStatPolicerId_Object = MibTableColumn
tmnxFPAccIngQGrpPStatPolicerId = _TmnxFPAccIngQGrpPStatPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 1),
    _TmnxFPAccIngQGrpPStatPolicerId_Type()
)
tmnxFPAccIngQGrpPStatPolicerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpPStatPolicerId.setStatus("current")
_TmnxFPAccIngQGrpPStatMode_Type = TmnxIngPolicerStatMode
_TmnxFPAccIngQGrpPStatMode_Object = MibTableColumn
tmnxFPAccIngQGrpPStatMode = _TmnxFPAccIngQGrpPStatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 2),
    _TmnxFPAccIngQGrpPStatMode_Type()
)
tmnxFPAccIngQGrpPStatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQGrpPStatMode.setStatus("current")
_TmnxFPAccIngQgPStOffHPrioPkts_Type = Counter64
_TmnxFPAccIngQgPStOffHPrioPkts_Object = MibTableColumn
tmnxFPAccIngQgPStOffHPrioPkts = _TmnxFPAccIngQgPStOffHPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 3),
    _TmnxFPAccIngQgPStOffHPrioPkts_Type()
)
tmnxFPAccIngQgPStOffHPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffHPrioPkts.setStatus("current")
_TmnxFPAccIngQgPStOffHPrioPktsL_Type = Counter32
_TmnxFPAccIngQgPStOffHPrioPktsL_Object = MibTableColumn
tmnxFPAccIngQgPStOffHPrioPktsL = _TmnxFPAccIngQgPStOffHPrioPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 4),
    _TmnxFPAccIngQgPStOffHPrioPktsL_Type()
)
tmnxFPAccIngQgPStOffHPrioPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffHPrioPktsL.setStatus("current")
_TmnxFPAccIngQgPStOffHPrioPktsH_Type = Counter32
_TmnxFPAccIngQgPStOffHPrioPktsH_Object = MibTableColumn
tmnxFPAccIngQgPStOffHPrioPktsH = _TmnxFPAccIngQgPStOffHPrioPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 5),
    _TmnxFPAccIngQgPStOffHPrioPktsH_Type()
)
tmnxFPAccIngQgPStOffHPrioPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffHPrioPktsH.setStatus("current")
_TmnxFPAccIngQgPStDrpHPrioPkts_Type = Counter64
_TmnxFPAccIngQgPStDrpHPrioPkts_Object = MibTableColumn
tmnxFPAccIngQgPStDrpHPrioPkts = _TmnxFPAccIngQgPStDrpHPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 6),
    _TmnxFPAccIngQgPStDrpHPrioPkts_Type()
)
tmnxFPAccIngQgPStDrpHPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpHPrioPkts.setStatus("current")
_TmnxFPAccIngQgPStDrpHPrioPktsL_Type = Counter32
_TmnxFPAccIngQgPStDrpHPrioPktsL_Object = MibTableColumn
tmnxFPAccIngQgPStDrpHPrioPktsL = _TmnxFPAccIngQgPStDrpHPrioPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 7),
    _TmnxFPAccIngQgPStDrpHPrioPktsL_Type()
)
tmnxFPAccIngQgPStDrpHPrioPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpHPrioPktsL.setStatus("current")
_TmnxFPAccIngQgPStDrpHPrioPktsH_Type = Counter32
_TmnxFPAccIngQgPStDrpHPrioPktsH_Object = MibTableColumn
tmnxFPAccIngQgPStDrpHPrioPktsH = _TmnxFPAccIngQgPStDrpHPrioPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 8),
    _TmnxFPAccIngQgPStDrpHPrioPktsH_Type()
)
tmnxFPAccIngQgPStDrpHPrioPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpHPrioPktsH.setStatus("current")
_TmnxFPAccIngQgPStOffLPrioPkts_Type = Counter64
_TmnxFPAccIngQgPStOffLPrioPkts_Object = MibTableColumn
tmnxFPAccIngQgPStOffLPrioPkts = _TmnxFPAccIngQgPStOffLPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 9),
    _TmnxFPAccIngQgPStOffLPrioPkts_Type()
)
tmnxFPAccIngQgPStOffLPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffLPrioPkts.setStatus("current")
_TmnxFPAccIngQgPStOffLPrioPktsL_Type = Counter32
_TmnxFPAccIngQgPStOffLPrioPktsL_Object = MibTableColumn
tmnxFPAccIngQgPStOffLPrioPktsL = _TmnxFPAccIngQgPStOffLPrioPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 10),
    _TmnxFPAccIngQgPStOffLPrioPktsL_Type()
)
tmnxFPAccIngQgPStOffLPrioPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffLPrioPktsL.setStatus("current")
_TmnxFPAccIngQgPStOffLPrioPktsH_Type = Counter32
_TmnxFPAccIngQgPStOffLPrioPktsH_Object = MibTableColumn
tmnxFPAccIngQgPStOffLPrioPktsH = _TmnxFPAccIngQgPStOffLPrioPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 11),
    _TmnxFPAccIngQgPStOffLPrioPktsH_Type()
)
tmnxFPAccIngQgPStOffLPrioPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffLPrioPktsH.setStatus("current")
_TmnxFPAccIngQgPStDrpLPrioPkts_Type = Counter64
_TmnxFPAccIngQgPStDrpLPrioPkts_Object = MibTableColumn
tmnxFPAccIngQgPStDrpLPrioPkts = _TmnxFPAccIngQgPStDrpLPrioPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 12),
    _TmnxFPAccIngQgPStDrpLPrioPkts_Type()
)
tmnxFPAccIngQgPStDrpLPrioPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpLPrioPkts.setStatus("current")
_TmnxFPAccIngQgPStDrpLPrioPktsL_Type = Counter32
_TmnxFPAccIngQgPStDrpLPrioPktsL_Object = MibTableColumn
tmnxFPAccIngQgPStDrpLPrioPktsL = _TmnxFPAccIngQgPStDrpLPrioPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 13),
    _TmnxFPAccIngQgPStDrpLPrioPktsL_Type()
)
tmnxFPAccIngQgPStDrpLPrioPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpLPrioPktsL.setStatus("current")
_TmnxFPAccIngQgPStDrpLPrioPktsH_Type = Counter32
_TmnxFPAccIngQgPStDrpLPrioPktsH_Object = MibTableColumn
tmnxFPAccIngQgPStDrpLPrioPktsH = _TmnxFPAccIngQgPStDrpLPrioPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 14),
    _TmnxFPAccIngQgPStDrpLPrioPktsH_Type()
)
tmnxFPAccIngQgPStDrpLPrioPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpLPrioPktsH.setStatus("current")
_TmnxFPAccIngQgPStOffHPrioOcts_Type = Counter64
_TmnxFPAccIngQgPStOffHPrioOcts_Object = MibTableColumn
tmnxFPAccIngQgPStOffHPrioOcts = _TmnxFPAccIngQgPStOffHPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 15),
    _TmnxFPAccIngQgPStOffHPrioOcts_Type()
)
tmnxFPAccIngQgPStOffHPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffHPrioOcts.setStatus("current")
_TmnxFPAccIngQgPStOffHPrioOctsL_Type = Counter32
_TmnxFPAccIngQgPStOffHPrioOctsL_Object = MibTableColumn
tmnxFPAccIngQgPStOffHPrioOctsL = _TmnxFPAccIngQgPStOffHPrioOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 16),
    _TmnxFPAccIngQgPStOffHPrioOctsL_Type()
)
tmnxFPAccIngQgPStOffHPrioOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffHPrioOctsL.setStatus("current")
_TmnxFPAccIngQgPStOffHPrioOctsH_Type = Counter32
_TmnxFPAccIngQgPStOffHPrioOctsH_Object = MibTableColumn
tmnxFPAccIngQgPStOffHPrioOctsH = _TmnxFPAccIngQgPStOffHPrioOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 17),
    _TmnxFPAccIngQgPStOffHPrioOctsH_Type()
)
tmnxFPAccIngQgPStOffHPrioOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffHPrioOctsH.setStatus("current")
_TmnxFPAccIngQgPStDrpHPrioOcts_Type = Counter64
_TmnxFPAccIngQgPStDrpHPrioOcts_Object = MibTableColumn
tmnxFPAccIngQgPStDrpHPrioOcts = _TmnxFPAccIngQgPStDrpHPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 18),
    _TmnxFPAccIngQgPStDrpHPrioOcts_Type()
)
tmnxFPAccIngQgPStDrpHPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpHPrioOcts.setStatus("current")
_TmnxFPAccIngQgPStDrpHPrioOctsL_Type = Counter32
_TmnxFPAccIngQgPStDrpHPrioOctsL_Object = MibTableColumn
tmnxFPAccIngQgPStDrpHPrioOctsL = _TmnxFPAccIngQgPStDrpHPrioOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 19),
    _TmnxFPAccIngQgPStDrpHPrioOctsL_Type()
)
tmnxFPAccIngQgPStDrpHPrioOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpHPrioOctsL.setStatus("current")
_TmnxFPAccIngQgPStDrpHPrioOctsH_Type = Counter32
_TmnxFPAccIngQgPStDrpHPrioOctsH_Object = MibTableColumn
tmnxFPAccIngQgPStDrpHPrioOctsH = _TmnxFPAccIngQgPStDrpHPrioOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 20),
    _TmnxFPAccIngQgPStDrpHPrioOctsH_Type()
)
tmnxFPAccIngQgPStDrpHPrioOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpHPrioOctsH.setStatus("current")
_TmnxFPAccIngQgPStOffLPrioOcts_Type = Counter64
_TmnxFPAccIngQgPStOffLPrioOcts_Object = MibTableColumn
tmnxFPAccIngQgPStOffLPrioOcts = _TmnxFPAccIngQgPStOffLPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 21),
    _TmnxFPAccIngQgPStOffLPrioOcts_Type()
)
tmnxFPAccIngQgPStOffLPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffLPrioOcts.setStatus("current")
_TmnxFPAccIngQgPStOffLPrioOctsL_Type = Counter32
_TmnxFPAccIngQgPStOffLPrioOctsL_Object = MibTableColumn
tmnxFPAccIngQgPStOffLPrioOctsL = _TmnxFPAccIngQgPStOffLPrioOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 22),
    _TmnxFPAccIngQgPStOffLPrioOctsL_Type()
)
tmnxFPAccIngQgPStOffLPrioOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffLPrioOctsL.setStatus("current")
_TmnxFPAccIngQgPStOffLPrioOctsH_Type = Counter32
_TmnxFPAccIngQgPStOffLPrioOctsH_Object = MibTableColumn
tmnxFPAccIngQgPStOffLPrioOctsH = _TmnxFPAccIngQgPStOffLPrioOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 23),
    _TmnxFPAccIngQgPStOffLPrioOctsH_Type()
)
tmnxFPAccIngQgPStOffLPrioOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStOffLPrioOctsH.setStatus("current")
_TmnxFPAccIngQgPStDrpLPrioOcts_Type = Counter64
_TmnxFPAccIngQgPStDrpLPrioOcts_Object = MibTableColumn
tmnxFPAccIngQgPStDrpLPrioOcts = _TmnxFPAccIngQgPStDrpLPrioOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 24),
    _TmnxFPAccIngQgPStDrpLPrioOcts_Type()
)
tmnxFPAccIngQgPStDrpLPrioOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpLPrioOcts.setStatus("current")
_TmnxFPAccIngQgPStDrpLPrioOctsL_Type = Counter32
_TmnxFPAccIngQgPStDrpLPrioOctsL_Object = MibTableColumn
tmnxFPAccIngQgPStDrpLPrioOctsL = _TmnxFPAccIngQgPStDrpLPrioOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 25),
    _TmnxFPAccIngQgPStDrpLPrioOctsL_Type()
)
tmnxFPAccIngQgPStDrpLPrioOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpLPrioOctsL.setStatus("current")
_TmnxFPAccIngQgPStDrpLPrioOctsH_Type = Counter32
_TmnxFPAccIngQgPStDrpLPrioOctsH_Object = MibTableColumn
tmnxFPAccIngQgPStDrpLPrioOctsH = _TmnxFPAccIngQgPStDrpLPrioOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 26),
    _TmnxFPAccIngQgPStDrpLPrioOctsH_Type()
)
tmnxFPAccIngQgPStDrpLPrioOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStDrpLPrioOctsH.setStatus("current")
_TmnxFPAccIngQgPStFwdInProfPkts_Type = Counter64
_TmnxFPAccIngQgPStFwdInProfPkts_Object = MibTableColumn
tmnxFPAccIngQgPStFwdInProfPkts = _TmnxFPAccIngQgPStFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 27),
    _TmnxFPAccIngQgPStFwdInProfPkts_Type()
)
tmnxFPAccIngQgPStFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdInProfPkts.setStatus("current")
_TmnxFPAccIngQgPStFwdInProfPktsL_Type = Counter32
_TmnxFPAccIngQgPStFwdInProfPktsL_Object = MibTableColumn
tmnxFPAccIngQgPStFwdInProfPktsL = _TmnxFPAccIngQgPStFwdInProfPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 28),
    _TmnxFPAccIngQgPStFwdInProfPktsL_Type()
)
tmnxFPAccIngQgPStFwdInProfPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdInProfPktsL.setStatus("current")
_TmnxFPAccIngQgPStFwdInProfPktsH_Type = Counter32
_TmnxFPAccIngQgPStFwdInProfPktsH_Object = MibTableColumn
tmnxFPAccIngQgPStFwdInProfPktsH = _TmnxFPAccIngQgPStFwdInProfPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 29),
    _TmnxFPAccIngQgPStFwdInProfPktsH_Type()
)
tmnxFPAccIngQgPStFwdInProfPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdInProfPktsH.setStatus("current")
_TmnxFPAccIngQgPStFwdOutProfPkts_Type = Counter64
_TmnxFPAccIngQgPStFwdOutProfPkts_Object = MibTableColumn
tmnxFPAccIngQgPStFwdOutProfPkts = _TmnxFPAccIngQgPStFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 30),
    _TmnxFPAccIngQgPStFwdOutProfPkts_Type()
)
tmnxFPAccIngQgPStFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdOutProfPkts.setStatus("current")
_TmnxFPAccIngQgPStFwdOutProfPktsL_Type = Counter32
_TmnxFPAccIngQgPStFwdOutProfPktsL_Object = MibTableColumn
tmnxFPAccIngQgPStFwdOutProfPktsL = _TmnxFPAccIngQgPStFwdOutProfPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 31),
    _TmnxFPAccIngQgPStFwdOutProfPktsL_Type()
)
tmnxFPAccIngQgPStFwdOutProfPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdOutProfPktsL.setStatus("current")
_TmnxFPAccIngQgPStFwdOutProfPktsH_Type = Counter32
_TmnxFPAccIngQgPStFwdOutProfPktsH_Object = MibTableColumn
tmnxFPAccIngQgPStFwdOutProfPktsH = _TmnxFPAccIngQgPStFwdOutProfPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 32),
    _TmnxFPAccIngQgPStFwdOutProfPktsH_Type()
)
tmnxFPAccIngQgPStFwdOutProfPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdOutProfPktsH.setStatus("current")
_TmnxFPAccIngQgPStFwdInProfOcts_Type = Counter64
_TmnxFPAccIngQgPStFwdInProfOcts_Object = MibTableColumn
tmnxFPAccIngQgPStFwdInProfOcts = _TmnxFPAccIngQgPStFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 33),
    _TmnxFPAccIngQgPStFwdInProfOcts_Type()
)
tmnxFPAccIngQgPStFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdInProfOcts.setStatus("current")
_TmnxFPAccIngQgPStFwdInProfOctsL_Type = Counter32
_TmnxFPAccIngQgPStFwdInProfOctsL_Object = MibTableColumn
tmnxFPAccIngQgPStFwdInProfOctsL = _TmnxFPAccIngQgPStFwdInProfOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 34),
    _TmnxFPAccIngQgPStFwdInProfOctsL_Type()
)
tmnxFPAccIngQgPStFwdInProfOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdInProfOctsL.setStatus("current")
_TmnxFPAccIngQgPStFwdInProfOctsH_Type = Counter32
_TmnxFPAccIngQgPStFwdInProfOctsH_Object = MibTableColumn
tmnxFPAccIngQgPStFwdInProfOctsH = _TmnxFPAccIngQgPStFwdInProfOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 35),
    _TmnxFPAccIngQgPStFwdInProfOctsH_Type()
)
tmnxFPAccIngQgPStFwdInProfOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdInProfOctsH.setStatus("current")
_TmnxFPAccIngQgPStFwdOutProfOcts_Type = Counter64
_TmnxFPAccIngQgPStFwdOutProfOcts_Object = MibTableColumn
tmnxFPAccIngQgPStFwdOutProfOcts = _TmnxFPAccIngQgPStFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 36),
    _TmnxFPAccIngQgPStFwdOutProfOcts_Type()
)
tmnxFPAccIngQgPStFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdOutProfOcts.setStatus("current")
_TmnxFPAccIngQgPStFwdOutProfOctsL_Type = Counter32
_TmnxFPAccIngQgPStFwdOutProfOctsL_Object = MibTableColumn
tmnxFPAccIngQgPStFwdOutProfOctsL = _TmnxFPAccIngQgPStFwdOutProfOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 37),
    _TmnxFPAccIngQgPStFwdOutProfOctsL_Type()
)
tmnxFPAccIngQgPStFwdOutProfOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdOutProfOctsL.setStatus("current")
_TmnxFPAccIngQgPStFwdOutProfOctsH_Type = Counter32
_TmnxFPAccIngQgPStFwdOutProfOctsH_Object = MibTableColumn
tmnxFPAccIngQgPStFwdOutProfOctsH = _TmnxFPAccIngQgPStFwdOutProfOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 38),
    _TmnxFPAccIngQgPStFwdOutProfOctsH_Type()
)
tmnxFPAccIngQgPStFwdOutProfOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStFwdOutProfOctsH.setStatus("current")
_TmnxFPAccIngQgPStUncolPktsOff_Type = Counter64
_TmnxFPAccIngQgPStUncolPktsOff_Object = MibTableColumn
tmnxFPAccIngQgPStUncolPktsOff = _TmnxFPAccIngQgPStUncolPktsOff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 39),
    _TmnxFPAccIngQgPStUncolPktsOff_Type()
)
tmnxFPAccIngQgPStUncolPktsOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStUncolPktsOff.setStatus("current")
_TmnxFPAccIngQgPStUncolPktsOffL_Type = Counter32
_TmnxFPAccIngQgPStUncolPktsOffL_Object = MibTableColumn
tmnxFPAccIngQgPStUncolPktsOffL = _TmnxFPAccIngQgPStUncolPktsOffL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 40),
    _TmnxFPAccIngQgPStUncolPktsOffL_Type()
)
tmnxFPAccIngQgPStUncolPktsOffL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStUncolPktsOffL.setStatus("current")
_TmnxFPAccIngQgPStUncolPktsOffH_Type = Counter32
_TmnxFPAccIngQgPStUncolPktsOffH_Object = MibTableColumn
tmnxFPAccIngQgPStUncolPktsOffH = _TmnxFPAccIngQgPStUncolPktsOffH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 41),
    _TmnxFPAccIngQgPStUncolPktsOffH_Type()
)
tmnxFPAccIngQgPStUncolPktsOffH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStUncolPktsOffH.setStatus("current")
_TmnxFPAccIngQgPStUncolOctsOff_Type = Counter64
_TmnxFPAccIngQgPStUncolOctsOff_Object = MibTableColumn
tmnxFPAccIngQgPStUncolOctsOff = _TmnxFPAccIngQgPStUncolOctsOff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 42),
    _TmnxFPAccIngQgPStUncolOctsOff_Type()
)
tmnxFPAccIngQgPStUncolOctsOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStUncolOctsOff.setStatus("current")
_TmnxFPAccIngQgPStUncolOctsOffL_Type = Counter32
_TmnxFPAccIngQgPStUncolOctsOffL_Object = MibTableColumn
tmnxFPAccIngQgPStUncolOctsOffL = _TmnxFPAccIngQgPStUncolOctsOffL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 43),
    _TmnxFPAccIngQgPStUncolOctsOffL_Type()
)
tmnxFPAccIngQgPStUncolOctsOffL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStUncolOctsOffL.setStatus("current")
_TmnxFPAccIngQgPStUncolOctsOffH_Type = Counter32
_TmnxFPAccIngQgPStUncolOctsOffH_Object = MibTableColumn
tmnxFPAccIngQgPStUncolOctsOffH = _TmnxFPAccIngQgPStUncolOctsOffH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 28, 1, 44),
    _TmnxFPAccIngQgPStUncolOctsOffH_Type()
)
tmnxFPAccIngQgPStUncolOctsOffH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFPAccIngQgPStUncolOctsOffH.setStatus("current")
_TFPAccIngQGrpPlcrOvrTblLstChgd_Type = TimeStamp
_TFPAccIngQGrpPlcrOvrTblLstChgd_Object = MibScalar
tFPAccIngQGrpPlcrOvrTblLstChgd = _TFPAccIngQGrpPlcrOvrTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 29),
    _TFPAccIngQGrpPlcrOvrTblLstChgd_Type()
)
tFPAccIngQGrpPlcrOvrTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrTblLstChgd.setStatus("current")
_TFPAccIngQGrpPlcrOvrTable_Object = MibTable
tFPAccIngQGrpPlcrOvrTable = _TFPAccIngQGrpPlcrOvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 30)
)
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrTable.setStatus("current")
_TFPAccIngQGrpPlcrOvrEntry_Object = MibTableRow
tFPAccIngQGrpPlcrOvrEntry = _TFPAccIngQGrpPlcrOvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 30, 1)
)
tFPAccIngQGrpPlcrOvrEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpName"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpInstanceId"),
    (0, "TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpPlcrOvrPolicerId"),
)
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrEntry.setStatus("current")
_TFPAccIngQGrpPlcrOvrPolicerId_Type = TIngPolicerId
_TFPAccIngQGrpPlcrOvrPolicerId_Object = MibTableColumn
tFPAccIngQGrpPlcrOvrPolicerId = _TFPAccIngQGrpPlcrOvrPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 30, 1, 1),
    _TFPAccIngQGrpPlcrOvrPolicerId_Type()
)
tFPAccIngQGrpPlcrOvrPolicerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrPolicerId.setStatus("current")
_TFPAccIngQGrpPlcrOvrRowStatus_Type = RowStatus
_TFPAccIngQGrpPlcrOvrRowStatus_Object = MibTableColumn
tFPAccIngQGrpPlcrOvrRowStatus = _TFPAccIngQGrpPlcrOvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 30, 1, 2),
    _TFPAccIngQGrpPlcrOvrRowStatus_Type()
)
tFPAccIngQGrpPlcrOvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrRowStatus.setStatus("current")
_TFPAccIngQGrpPlcrOvrLastChgd_Type = TimeStamp
_TFPAccIngQGrpPlcrOvrLastChgd_Object = MibTableColumn
tFPAccIngQGrpPlcrOvrLastChgd = _TFPAccIngQGrpPlcrOvrLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 30, 1, 3),
    _TFPAccIngQGrpPlcrOvrLastChgd_Type()
)
tFPAccIngQGrpPlcrOvrLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrLastChgd.setStatus("current")


class _TFPAccIngQGrpPlcrOvrAdminPIR_Type(THPolPIRRateOverride):
    """Custom type tFPAccIngQGrpPlcrOvrAdminPIR based on THPolPIRRateOverride"""
    defaultValue = -2


_TFPAccIngQGrpPlcrOvrAdminPIR_Object = MibTableColumn
tFPAccIngQGrpPlcrOvrAdminPIR = _TFPAccIngQGrpPlcrOvrAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 30, 1, 4),
    _TFPAccIngQGrpPlcrOvrAdminPIR_Type()
)
tFPAccIngQGrpPlcrOvrAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrAdminPIR.setUnits("kbps")


class _TFPAccIngQGrpPlcrOvrAdminCIR_Type(THPolCIRRateOverride):
    """Custom type tFPAccIngQGrpPlcrOvrAdminCIR based on THPolCIRRateOverride"""
    defaultValue = -2


_TFPAccIngQGrpPlcrOvrAdminCIR_Object = MibTableColumn
tFPAccIngQGrpPlcrOvrAdminCIR = _TFPAccIngQGrpPlcrOvrAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 30, 1, 5),
    _TFPAccIngQGrpPlcrOvrAdminCIR_Type()
)
tFPAccIngQGrpPlcrOvrAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrAdminCIR.setUnits("kbps")


class _TFPAccIngQGrpPlcrOvrStatMode_Type(TmnxIngPolicerStatModeOverride):
    """Custom type tFPAccIngQGrpPlcrOvrStatMode based on TmnxIngPolicerStatModeOverride"""


_TFPAccIngQGrpPlcrOvrStatMode_Object = MibTableColumn
tFPAccIngQGrpPlcrOvrStatMode = _TFPAccIngQGrpPlcrOvrStatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 30, 1, 6),
    _TFPAccIngQGrpPlcrOvrStatMode_Type()
)
tFPAccIngQGrpPlcrOvrStatMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrStatMode.setStatus("current")


class _TFPAccIngQGrpPlcrOvrMBS_Type(TPlcrBurstSizeBytesOverride):
    """Custom type tFPAccIngQGrpPlcrOvrMBS based on TPlcrBurstSizeBytesOverride"""
    defaultValue = -2


_TFPAccIngQGrpPlcrOvrMBS_Object = MibTableColumn
tFPAccIngQGrpPlcrOvrMBS = _TFPAccIngQGrpPlcrOvrMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 30, 1, 7),
    _TFPAccIngQGrpPlcrOvrMBS_Type()
)
tFPAccIngQGrpPlcrOvrMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrMBS.setStatus("current")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrMBS.setUnits("bytes")


class _TFPAccIngQGrpPlcrOvrCBS_Type(TPlcrBurstSizeBytesOverride):
    """Custom type tFPAccIngQGrpPlcrOvrCBS based on TPlcrBurstSizeBytesOverride"""
    defaultValue = -2


_TFPAccIngQGrpPlcrOvrCBS_Object = MibTableColumn
tFPAccIngQGrpPlcrOvrCBS = _TFPAccIngQGrpPlcrOvrCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 30, 1, 8),
    _TFPAccIngQGrpPlcrOvrCBS_Type()
)
tFPAccIngQGrpPlcrOvrCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrCBS.setStatus("current")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrCBS.setUnits("bytes")


class _TFPAccIngQGrpPlcrOvrPktOffset_Type(TPerPacketOffsetOvr):
    """Custom type tFPAccIngQGrpPlcrOvrPktOffset based on TPerPacketOffsetOvr"""
    defaultValue = -128


_TFPAccIngQGrpPlcrOvrPktOffset_Object = MibTableColumn
tFPAccIngQGrpPlcrOvrPktOffset = _TFPAccIngQGrpPlcrOvrPktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 30, 1, 9),
    _TFPAccIngQGrpPlcrOvrPktOffset_Type()
)
tFPAccIngQGrpPlcrOvrPktOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrPktOffset.setStatus("current")
if mibBuilder.loadTexts:
    tFPAccIngQGrpPlcrOvrPktOffset.setUnits("bytes")
_TFPAccIngQGrpArbitStatTable_Object = MibTable
tFPAccIngQGrpArbitStatTable = _TFPAccIngQGrpArbitStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 31)
)
if mibBuilder.loadTexts:
    tFPAccIngQGrpArbitStatTable.setStatus("current")
_TFPAccIngQGrpArbitStatEntry_Object = MibTableRow
tFPAccIngQGrpArbitStatEntry = _TFPAccIngQGrpArbitStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 31, 1)
)
tFPAccIngQGrpArbitStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpName"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpInstanceId"),
    (0, "TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpArbitStatName"),
)
if mibBuilder.loadTexts:
    tFPAccIngQGrpArbitStatEntry.setStatus("current")
_TFPAccIngQGrpArbitStatName_Type = TNamedItem
_TFPAccIngQGrpArbitStatName_Object = MibTableColumn
tFPAccIngQGrpArbitStatName = _TFPAccIngQGrpArbitStatName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 31, 1, 1),
    _TFPAccIngQGrpArbitStatName_Type()
)
tFPAccIngQGrpArbitStatName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFPAccIngQGrpArbitStatName.setStatus("current")
_TFPAccIngQGrpArbitStatFwdPkts_Type = Counter64
_TFPAccIngQGrpArbitStatFwdPkts_Object = MibTableColumn
tFPAccIngQGrpArbitStatFwdPkts = _TFPAccIngQGrpArbitStatFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 31, 1, 2),
    _TFPAccIngQGrpArbitStatFwdPkts_Type()
)
tFPAccIngQGrpArbitStatFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPAccIngQGrpArbitStatFwdPkts.setStatus("current")
_TFPAccIngQGrpArbitStatFwdPktsL_Type = Counter32
_TFPAccIngQGrpArbitStatFwdPktsL_Object = MibTableColumn
tFPAccIngQGrpArbitStatFwdPktsL = _TFPAccIngQGrpArbitStatFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 31, 1, 3),
    _TFPAccIngQGrpArbitStatFwdPktsL_Type()
)
tFPAccIngQGrpArbitStatFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPAccIngQGrpArbitStatFwdPktsL.setStatus("current")
_TFPAccIngQGrpArbitStatFwdPktsH_Type = Counter32
_TFPAccIngQGrpArbitStatFwdPktsH_Object = MibTableColumn
tFPAccIngQGrpArbitStatFwdPktsH = _TFPAccIngQGrpArbitStatFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 31, 1, 4),
    _TFPAccIngQGrpArbitStatFwdPktsH_Type()
)
tFPAccIngQGrpArbitStatFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPAccIngQGrpArbitStatFwdPktsH.setStatus("current")
_TFPAccIngQGrpArbitStatFwdOcts_Type = Counter64
_TFPAccIngQGrpArbitStatFwdOcts_Object = MibTableColumn
tFPAccIngQGrpArbitStatFwdOcts = _TFPAccIngQGrpArbitStatFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 31, 1, 5),
    _TFPAccIngQGrpArbitStatFwdOcts_Type()
)
tFPAccIngQGrpArbitStatFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPAccIngQGrpArbitStatFwdOcts.setStatus("current")
_TFPAccIngQGrpArbitStatFwdOctsL_Type = Counter32
_TFPAccIngQGrpArbitStatFwdOctsL_Object = MibTableColumn
tFPAccIngQGrpArbitStatFwdOctsL = _TFPAccIngQGrpArbitStatFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 31, 1, 6),
    _TFPAccIngQGrpArbitStatFwdOctsL_Type()
)
tFPAccIngQGrpArbitStatFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPAccIngQGrpArbitStatFwdOctsL.setStatus("current")
_TFPAccIngQGrpArbitStatFwdOctsH_Type = Counter32
_TFPAccIngQGrpArbitStatFwdOctsH_Object = MibTableColumn
tFPAccIngQGrpArbitStatFwdOctsH = _TFPAccIngQGrpArbitStatFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 31, 1, 7),
    _TFPAccIngQGrpArbitStatFwdOctsH_Type()
)
tFPAccIngQGrpArbitStatFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPAccIngQGrpArbitStatFwdOctsH.setStatus("current")
_TFPNetIngQGrpArbitStatTable_Object = MibTable
tFPNetIngQGrpArbitStatTable = _TFPNetIngQGrpArbitStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 32)
)
if mibBuilder.loadTexts:
    tFPNetIngQGrpArbitStatTable.setStatus("current")
_TFPNetIngQGrpArbitStatEntry_Object = MibTableRow
tFPNetIngQGrpArbitStatEntry = _TFPNetIngQGrpArbitStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 32, 1)
)
tFPNetIngQGrpArbitStatEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpName"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpInstanceId"),
    (0, "TIMETRA-CHASSIS-MIB", "tFPNetIngQGrpArbitStatName"),
)
if mibBuilder.loadTexts:
    tFPNetIngQGrpArbitStatEntry.setStatus("current")
_TFPNetIngQGrpArbitStatName_Type = TNamedItem
_TFPNetIngQGrpArbitStatName_Object = MibTableColumn
tFPNetIngQGrpArbitStatName = _TFPNetIngQGrpArbitStatName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 32, 1, 1),
    _TFPNetIngQGrpArbitStatName_Type()
)
tFPNetIngQGrpArbitStatName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFPNetIngQGrpArbitStatName.setStatus("current")
_TFPNetIngQGrpArbitStatFwdPkts_Type = Counter64
_TFPNetIngQGrpArbitStatFwdPkts_Object = MibTableColumn
tFPNetIngQGrpArbitStatFwdPkts = _TFPNetIngQGrpArbitStatFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 32, 1, 2),
    _TFPNetIngQGrpArbitStatFwdPkts_Type()
)
tFPNetIngQGrpArbitStatFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPNetIngQGrpArbitStatFwdPkts.setStatus("current")
_TFPNetIngQGrpArbitStatFwdPktsL_Type = Counter32
_TFPNetIngQGrpArbitStatFwdPktsL_Object = MibTableColumn
tFPNetIngQGrpArbitStatFwdPktsL = _TFPNetIngQGrpArbitStatFwdPktsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 32, 1, 3),
    _TFPNetIngQGrpArbitStatFwdPktsL_Type()
)
tFPNetIngQGrpArbitStatFwdPktsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPNetIngQGrpArbitStatFwdPktsL.setStatus("current")
_TFPNetIngQGrpArbitStatFwdPktsH_Type = Counter32
_TFPNetIngQGrpArbitStatFwdPktsH_Object = MibTableColumn
tFPNetIngQGrpArbitStatFwdPktsH = _TFPNetIngQGrpArbitStatFwdPktsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 32, 1, 4),
    _TFPNetIngQGrpArbitStatFwdPktsH_Type()
)
tFPNetIngQGrpArbitStatFwdPktsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPNetIngQGrpArbitStatFwdPktsH.setStatus("current")
_TFPNetIngQGrpArbitStatFwdOcts_Type = Counter64
_TFPNetIngQGrpArbitStatFwdOcts_Object = MibTableColumn
tFPNetIngQGrpArbitStatFwdOcts = _TFPNetIngQGrpArbitStatFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 32, 1, 5),
    _TFPNetIngQGrpArbitStatFwdOcts_Type()
)
tFPNetIngQGrpArbitStatFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPNetIngQGrpArbitStatFwdOcts.setStatus("current")
_TFPNetIngQGrpArbitStatFwdOctsL_Type = Counter32
_TFPNetIngQGrpArbitStatFwdOctsL_Object = MibTableColumn
tFPNetIngQGrpArbitStatFwdOctsL = _TFPNetIngQGrpArbitStatFwdOctsL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 32, 1, 6),
    _TFPNetIngQGrpArbitStatFwdOctsL_Type()
)
tFPNetIngQGrpArbitStatFwdOctsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPNetIngQGrpArbitStatFwdOctsL.setStatus("current")
_TFPNetIngQGrpArbitStatFwdOctsH_Type = Counter32
_TFPNetIngQGrpArbitStatFwdOctsH_Object = MibTableColumn
tFPNetIngQGrpArbitStatFwdOctsH = _TFPNetIngQGrpArbitStatFwdOctsH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 32, 1, 7),
    _TFPNetIngQGrpArbitStatFwdOctsH_Type()
)
tFPNetIngQGrpArbitStatFwdOctsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFPNetIngQGrpArbitStatFwdOctsH.setStatus("current")
_TmnxVirtualSchedulerAdjTable_Object = MibTable
tmnxVirtualSchedulerAdjTable = _TmnxVirtualSchedulerAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 33)
)
if mibBuilder.loadTexts:
    tmnxVirtualSchedulerAdjTable.setStatus("current")
_TmnxVirtualSchedulerAdjEntry_Object = MibTableRow
tmnxVirtualSchedulerAdjEntry = _TmnxVirtualSchedulerAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 33, 1)
)
if mibBuilder.loadTexts:
    tmnxVirtualSchedulerAdjEntry.setStatus("current")


class _TmnxCardRateCalcFastQueue_Type(Unsigned32):
    """Custom type tmnxCardRateCalcFastQueue based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxCardRateCalcFastQueue_Type.__name__ = "Unsigned32"
_TmnxCardRateCalcFastQueue_Object = MibTableColumn
tmnxCardRateCalcFastQueue = _TmnxCardRateCalcFastQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 33, 1, 1),
    _TmnxCardRateCalcFastQueue_Type()
)
tmnxCardRateCalcFastQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardRateCalcFastQueue.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCardRateCalcFastQueue.setUnits("thousandths of a percent")


class _TmnxCardRateCalcSlowQueue_Type(Unsigned32):
    """Custom type tmnxCardRateCalcSlowQueue based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxCardRateCalcSlowQueue_Type.__name__ = "Unsigned32"
_TmnxCardRateCalcSlowQueue_Object = MibTableColumn
tmnxCardRateCalcSlowQueue = _TmnxCardRateCalcSlowQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 33, 1, 2),
    _TmnxCardRateCalcSlowQueue_Type()
)
tmnxCardRateCalcSlowQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardRateCalcSlowQueue.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCardRateCalcSlowQueue.setUnits("thousandths of a percent")


class _TmnxCardSchedRun_Type(Unsigned32):
    """Custom type tmnxCardSchedRun based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxCardSchedRun_Type.__name__ = "Unsigned32"
_TmnxCardSchedRun_Object = MibTableColumn
tmnxCardSchedRun = _TmnxCardSchedRun_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 33, 1, 3),
    _TmnxCardSchedRun_Type()
)
tmnxCardSchedRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardSchedRun.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCardSchedRun.setUnits("thousandths of a percent")


class _TmnxCardTaskScheduling_Type(Unsigned32):
    """Custom type tmnxCardTaskScheduling based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxCardTaskScheduling_Type.__name__ = "Unsigned32"
_TmnxCardTaskScheduling_Object = MibTableColumn
tmnxCardTaskScheduling = _TmnxCardTaskScheduling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 33, 1, 4),
    _TmnxCardTaskScheduling_Type()
)
tmnxCardTaskScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardTaskScheduling.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCardTaskScheduling.setUnits("thousandths of a percent")


class _TmnxCardSlowQueueThresh_Type(Integer32):
    """Custom type tmnxCardSlowQueueThresh based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TmnxCardSlowQueueThresh_Type.__name__ = "Integer32"
_TmnxCardSlowQueueThresh_Object = MibTableColumn
tmnxCardSlowQueueThresh = _TmnxCardSlowQueueThresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 33, 1, 5),
    _TmnxCardSlowQueueThresh_Type()
)
tmnxCardSlowQueueThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCardSlowQueueThresh.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCardSlowQueueThresh.setUnits("kbps")
_TmnxChassisNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxChassisNotificationObjects = _TmnxChassisNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6)
)
_TmnxEqNotificationRow_Type = RowPointer
_TmnxEqNotificationRow_Object = MibScalar
tmnxEqNotificationRow = _TmnxEqNotificationRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 1),
    _TmnxEqNotificationRow_Type()
)
tmnxEqNotificationRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxEqNotificationRow.setStatus("current")
_TmnxEqTypeNotificationRow_Type = RowPointer
_TmnxEqTypeNotificationRow_Object = MibScalar
tmnxEqTypeNotificationRow = _TmnxEqTypeNotificationRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 2),
    _TmnxEqTypeNotificationRow_Type()
)
tmnxEqTypeNotificationRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxEqTypeNotificationRow.setStatus("current")
_TmnxChassisNotifyChassisId_Type = TmnxChassisIndex
_TmnxChassisNotifyChassisId_Object = MibScalar
tmnxChassisNotifyChassisId = _TmnxChassisNotifyChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 3),
    _TmnxChassisNotifyChassisId_Type()
)
tmnxChassisNotifyChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxChassisNotifyChassisId.setStatus("current")
_TmnxChassisNotifyHwIndex_Type = TmnxHwIndex
_TmnxChassisNotifyHwIndex_Object = MibScalar
tmnxChassisNotifyHwIndex = _TmnxChassisNotifyHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 4),
    _TmnxChassisNotifyHwIndex_Type()
)
tmnxChassisNotifyHwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxChassisNotifyHwIndex.setStatus("current")


class _TmnxRedSecondaryCPMStatus_Type(Integer32):
    """Custom type tmnxRedSecondaryCPMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("offline", 2),
          ("online", 1))
    )


_TmnxRedSecondaryCPMStatus_Type.__name__ = "Integer32"
_TmnxRedSecondaryCPMStatus_Object = MibScalar
tmnxRedSecondaryCPMStatus = _TmnxRedSecondaryCPMStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 5),
    _TmnxRedSecondaryCPMStatus_Type()
)
tmnxRedSecondaryCPMStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRedSecondaryCPMStatus.setStatus("current")
_TmnxChassisNotifyOID_Type = ObjectIdentifier
_TmnxChassisNotifyOID_Object = MibScalar
tmnxChassisNotifyOID = _TmnxChassisNotifyOID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 6),
    _TmnxChassisNotifyOID_Type()
)
tmnxChassisNotifyOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxChassisNotifyOID.setStatus("current")


class _TmnxSyncIfTimingNotifyAlarm_Type(Integer32):
    """Custom type tmnxSyncIfTimingNotifyAlarm based on Integer32"""
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
        *(("los", 1),
          ("notUsed", 0),
          ("oof", 2),
          ("oopir", 3))
    )


_TmnxSyncIfTimingNotifyAlarm_Type.__name__ = "Integer32"
_TmnxSyncIfTimingNotifyAlarm_Object = MibScalar
tmnxSyncIfTimingNotifyAlarm = _TmnxSyncIfTimingNotifyAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 7),
    _TmnxSyncIfTimingNotifyAlarm_Type()
)
tmnxSyncIfTimingNotifyAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSyncIfTimingNotifyAlarm.setStatus("current")
_TmnxChassisNotifyMismatchedVer_Type = DisplayString
_TmnxChassisNotifyMismatchedVer_Object = MibScalar
tmnxChassisNotifyMismatchedVer = _TmnxChassisNotifyMismatchedVer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 8),
    _TmnxChassisNotifyMismatchedVer_Type()
)
tmnxChassisNotifyMismatchedVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxChassisNotifyMismatchedVer.setStatus("current")
_TmnxChassisNotifySoftwareLocation_Type = DisplayString
_TmnxChassisNotifySoftwareLocation_Object = MibScalar
tmnxChassisNotifySoftwareLocation = _TmnxChassisNotifySoftwareLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 9),
    _TmnxChassisNotifySoftwareLocation_Type()
)
tmnxChassisNotifySoftwareLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxChassisNotifySoftwareLocation.setStatus("current")
_TmnxChassisNotifyCardFailureReason_Type = DisplayString
_TmnxChassisNotifyCardFailureReason_Object = MibScalar
tmnxChassisNotifyCardFailureReason = _TmnxChassisNotifyCardFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 10),
    _TmnxChassisNotifyCardFailureReason_Type()
)
tmnxChassisNotifyCardFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxChassisNotifyCardFailureReason.setStatus("current")


class _TmnxChassisNotifyCardName_Type(DisplayString):
    """Custom type tmnxChassisNotifyCardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxChassisNotifyCardName_Type.__name__ = "DisplayString"
_TmnxChassisNotifyCardName_Object = MibScalar
tmnxChassisNotifyCardName = _TmnxChassisNotifyCardName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 11),
    _TmnxChassisNotifyCardName_Type()
)
tmnxChassisNotifyCardName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxChassisNotifyCardName.setStatus("current")
_TmnxChassisNotifyCardSyncFile_Type = DisplayString
_TmnxChassisNotifyCardSyncFile_Object = MibScalar
tmnxChassisNotifyCardSyncFile = _TmnxChassisNotifyCardSyncFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 12),
    _TmnxChassisNotifyCardSyncFile_Type()
)
tmnxChassisNotifyCardSyncFile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxChassisNotifyCardSyncFile.setStatus("current")
_TmnxCardComplexNumber_Type = Unsigned32
_TmnxCardComplexNumber_Object = MibScalar
tmnxCardComplexNumber = _TmnxCardComplexNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 13),
    _TmnxCardComplexNumber_Type()
)
tmnxCardComplexNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCardComplexNumber.setStatus("current")


class _TmnxCardFwdDirection_Type(Integer32):
    """Custom type tmnxCardFwdDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_TmnxCardFwdDirection_Type.__name__ = "Integer32"
_TmnxCardFwdDirection_Object = MibScalar
tmnxCardFwdDirection = _TmnxCardFwdDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 14),
    _TmnxCardFwdDirection_Type()
)
tmnxCardFwdDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCardFwdDirection.setStatus("current")


class _TmnxCardSoftResetState_Type(Integer32):
    """Custom type tmnxCardSoftResetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 2),
          ("complete", 3),
          ("initiated", 1))
    )


_TmnxCardSoftResetState_Type.__name__ = "Integer32"
_TmnxCardSoftResetState_Object = MibScalar
tmnxCardSoftResetState = _TmnxCardSoftResetState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 15),
    _TmnxCardSoftResetState_Type()
)
tmnxCardSoftResetState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCardSoftResetState.setStatus("current")
_TmnxMdaNotifyType_Type = TmnxMdaType
_TmnxMdaNotifyType_Object = MibScalar
tmnxMdaNotifyType = _TmnxMdaNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 16),
    _TmnxMdaNotifyType_Type()
)
tmnxMdaNotifyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMdaNotifyType.setStatus("current")
_TmnxCardSrcSlotBitmap_Type = TmnxCardSlotBitMap
_TmnxCardSrcSlotBitmap_Object = MibScalar
tmnxCardSrcSlotBitmap = _TmnxCardSrcSlotBitmap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 6, 17),
    _TmnxCardSrcSlotBitmap_Type()
)
tmnxCardSrcSlotBitmap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCardSrcSlotBitmap.setStatus("current")
_TmnxChassisAdminObjects_ObjectIdentity = ObjectIdentity
tmnxChassisAdminObjects = _TmnxChassisAdminObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8)
)
_TmnxChassisAdminCtrlObjs_ObjectIdentity = ObjectIdentity
tmnxChassisAdminCtrlObjs = _TmnxChassisAdminCtrlObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 1)
)
_TmnxChassisAdminOwner_Type = SnmpAdminString
_TmnxChassisAdminOwner_Object = MibScalar
tmnxChassisAdminOwner = _TmnxChassisAdminOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 1, 1),
    _TmnxChassisAdminOwner_Type()
)
tmnxChassisAdminOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxChassisAdminOwner.setStatus("current")


class _TmnxChassisAdminControlApply_Type(Integer32):
    """Custom type tmnxChassisAdminControlApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commit", 3),
          ("initialize", 2),
          ("none", 1))
    )


_TmnxChassisAdminControlApply_Type.__name__ = "Integer32"
_TmnxChassisAdminControlApply_Object = MibScalar
tmnxChassisAdminControlApply = _TmnxChassisAdminControlApply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 1, 2),
    _TmnxChassisAdminControlApply_Type()
)
tmnxChassisAdminControlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxChassisAdminControlApply.setStatus("current")
_TmnxChassisAdminLastSetTimer_Type = TimeInterval
_TmnxChassisAdminLastSetTimer_Object = MibScalar
tmnxChassisAdminLastSetTimer = _TmnxChassisAdminLastSetTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 1, 3),
    _TmnxChassisAdminLastSetTimer_Type()
)
tmnxChassisAdminLastSetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxChassisAdminLastSetTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxChassisAdminLastSetTimer.setUnits("centiseconds")


class _TmnxChassisAdminLastSetTimeout_Type(TimeInterval):
    """Custom type tmnxChassisAdminLastSetTimeout based on TimeInterval"""
    defaultValue = 180000


_TmnxChassisAdminLastSetTimeout_Object = MibScalar
tmnxChassisAdminLastSetTimeout = _TmnxChassisAdminLastSetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 1, 4),
    _TmnxChassisAdminLastSetTimeout_Type()
)
tmnxChassisAdminLastSetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxChassisAdminLastSetTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxChassisAdminLastSetTimeout.setUnits("centiseconds")
_TmnxChassisAdminValueObjs_ObjectIdentity = ObjectIdentity
tmnxChassisAdminValueObjs = _TmnxChassisAdminValueObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2)
)
_TSyncIfTimingAdmTable_Object = MibTable
tSyncIfTimingAdmTable = _TSyncIfTimingAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    tSyncIfTimingAdmTable.setStatus("current")
_TSyncIfTimingAdmEntry_Object = MibTableRow
tSyncIfTimingAdmEntry = _TSyncIfTimingAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1)
)
tSyncIfTimingAdmEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCpmCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCpmCardNum"),
)
if mibBuilder.loadTexts:
    tSyncIfTimingAdmEntry.setStatus("current")


class _TSyncIfTimingAdmRevert_Type(TruthValue):
    """Custom type tSyncIfTimingAdmRevert based on TruthValue"""


_TSyncIfTimingAdmRevert_Object = MibTableColumn
tSyncIfTimingAdmRevert = _TSyncIfTimingAdmRevert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 1),
    _TSyncIfTimingAdmRevert_Type()
)
tSyncIfTimingAdmRevert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRevert.setStatus("current")


class _TSyncIfTimingAdmRefOrder1_Type(TmnxSETSRefSource):
    """Custom type tSyncIfTimingAdmRefOrder1 based on TmnxSETSRefSource"""


_TSyncIfTimingAdmRefOrder1_Object = MibTableColumn
tSyncIfTimingAdmRefOrder1 = _TSyncIfTimingAdmRefOrder1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 2),
    _TSyncIfTimingAdmRefOrder1_Type()
)
tSyncIfTimingAdmRefOrder1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRefOrder1.setStatus("current")


class _TSyncIfTimingAdmRefOrder2_Type(TmnxSETSRefSource):
    """Custom type tSyncIfTimingAdmRefOrder2 based on TmnxSETSRefSource"""


_TSyncIfTimingAdmRefOrder2_Object = MibTableColumn
tSyncIfTimingAdmRefOrder2 = _TSyncIfTimingAdmRefOrder2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 3),
    _TSyncIfTimingAdmRefOrder2_Type()
)
tSyncIfTimingAdmRefOrder2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRefOrder2.setStatus("current")


class _TSyncIfTimingAdmRef1SrcPort_Type(TmnxPortID):
    """Custom type tSyncIfTimingAdmRef1SrcPort based on TmnxPortID"""
    defaultHexValue = 503316480


_TSyncIfTimingAdmRef1SrcPort_Object = MibTableColumn
tSyncIfTimingAdmRef1SrcPort = _TSyncIfTimingAdmRef1SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 4),
    _TSyncIfTimingAdmRef1SrcPort_Type()
)
tSyncIfTimingAdmRef1SrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef1SrcPort.setStatus("current")


class _TSyncIfTimingAdmRef1AdminStatus_Type(TmnxPortAdminStatus):
    """Custom type tSyncIfTimingAdmRef1AdminStatus based on TmnxPortAdminStatus"""


_TSyncIfTimingAdmRef1AdminStatus_Object = MibTableColumn
tSyncIfTimingAdmRef1AdminStatus = _TSyncIfTimingAdmRef1AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 5),
    _TSyncIfTimingAdmRef1AdminStatus_Type()
)
tSyncIfTimingAdmRef1AdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef1AdminStatus.setStatus("current")


class _TSyncIfTimingAdmRef2SrcPort_Type(TmnxPortID):
    """Custom type tSyncIfTimingAdmRef2SrcPort based on TmnxPortID"""
    defaultHexValue = 503316480


_TSyncIfTimingAdmRef2SrcPort_Object = MibTableColumn
tSyncIfTimingAdmRef2SrcPort = _TSyncIfTimingAdmRef2SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 6),
    _TSyncIfTimingAdmRef2SrcPort_Type()
)
tSyncIfTimingAdmRef2SrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef2SrcPort.setStatus("current")


class _TSyncIfTimingAdmRef2AdminStatus_Type(TmnxPortAdminStatus):
    """Custom type tSyncIfTimingAdmRef2AdminStatus based on TmnxPortAdminStatus"""


_TSyncIfTimingAdmRef2AdminStatus_Object = MibTableColumn
tSyncIfTimingAdmRef2AdminStatus = _TSyncIfTimingAdmRef2AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 7),
    _TSyncIfTimingAdmRef2AdminStatus_Type()
)
tSyncIfTimingAdmRef2AdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef2AdminStatus.setStatus("current")
_TSyncIfTimingAdmChanged_Type = Unsigned32
_TSyncIfTimingAdmChanged_Object = MibTableColumn
tSyncIfTimingAdmChanged = _TSyncIfTimingAdmChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 8),
    _TSyncIfTimingAdmChanged_Type()
)
tSyncIfTimingAdmChanged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmChanged.setStatus("current")


class _TSyncIfTimingAdmRefOrder3_Type(TmnxSETSRefSource):
    """Custom type tSyncIfTimingAdmRefOrder3 based on TmnxSETSRefSource"""


_TSyncIfTimingAdmRefOrder3_Object = MibTableColumn
tSyncIfTimingAdmRefOrder3 = _TSyncIfTimingAdmRefOrder3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 9),
    _TSyncIfTimingAdmRefOrder3_Type()
)
tSyncIfTimingAdmRefOrder3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRefOrder3.setStatus("current")


class _TSyncIfTimingAdmBITSIfType_Type(TmnxBITSIfType):
    """Custom type tSyncIfTimingAdmBITSIfType based on TmnxBITSIfType"""


_TSyncIfTimingAdmBITSIfType_Object = MibTableColumn
tSyncIfTimingAdmBITSIfType = _TSyncIfTimingAdmBITSIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 10),
    _TSyncIfTimingAdmBITSIfType_Type()
)
tSyncIfTimingAdmBITSIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmBITSIfType.setStatus("current")


class _TSyncIfTimingAdmBITSAdminStatus_Type(TmnxPortAdminStatus):
    """Custom type tSyncIfTimingAdmBITSAdminStatus based on TmnxPortAdminStatus"""


_TSyncIfTimingAdmBITSAdminStatus_Object = MibTableColumn
tSyncIfTimingAdmBITSAdminStatus = _TSyncIfTimingAdmBITSAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 11),
    _TSyncIfTimingAdmBITSAdminStatus_Type()
)
tSyncIfTimingAdmBITSAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmBITSAdminStatus.setStatus("current")


class _TSyncIfTimingAdmRef1SrcHw_Type(TmnxHwIndexOrZero):
    """Custom type tSyncIfTimingAdmRef1SrcHw based on TmnxHwIndexOrZero"""
    defaultValue = 0


_TSyncIfTimingAdmRef1SrcHw_Object = MibTableColumn
tSyncIfTimingAdmRef1SrcHw = _TSyncIfTimingAdmRef1SrcHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 12),
    _TSyncIfTimingAdmRef1SrcHw_Type()
)
tSyncIfTimingAdmRef1SrcHw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef1SrcHw.setStatus("current")


class _TSyncIfTimingAdmRef1BITSIfType_Type(TmnxBITSIfType):
    """Custom type tSyncIfTimingAdmRef1BITSIfType based on TmnxBITSIfType"""


_TSyncIfTimingAdmRef1BITSIfType_Object = MibTableColumn
tSyncIfTimingAdmRef1BITSIfType = _TSyncIfTimingAdmRef1BITSIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 13),
    _TSyncIfTimingAdmRef1BITSIfType_Type()
)
tSyncIfTimingAdmRef1BITSIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef1BITSIfType.setStatus("current")


class _TSyncIfTimingAdmRef2SrcHw_Type(TmnxHwIndexOrZero):
    """Custom type tSyncIfTimingAdmRef2SrcHw based on TmnxHwIndexOrZero"""
    defaultValue = 0


_TSyncIfTimingAdmRef2SrcHw_Object = MibTableColumn
tSyncIfTimingAdmRef2SrcHw = _TSyncIfTimingAdmRef2SrcHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 14),
    _TSyncIfTimingAdmRef2SrcHw_Type()
)
tSyncIfTimingAdmRef2SrcHw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef2SrcHw.setStatus("current")


class _TSyncIfTimingAdmRef2BITSIfType_Type(TmnxBITSIfType):
    """Custom type tSyncIfTimingAdmRef2BITSIfType based on TmnxBITSIfType"""


_TSyncIfTimingAdmRef2BITSIfType_Object = MibTableColumn
tSyncIfTimingAdmRef2BITSIfType = _TSyncIfTimingAdmRef2BITSIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 15),
    _TSyncIfTimingAdmRef2BITSIfType_Type()
)
tSyncIfTimingAdmRef2BITSIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef2BITSIfType.setStatus("current")


class _TSyncIfTimingAdmBITSOutAdmStatus_Type(TmnxPortAdminStatus):
    """Custom type tSyncIfTimingAdmBITSOutAdmStatus based on TmnxPortAdminStatus"""


_TSyncIfTimingAdmBITSOutAdmStatus_Object = MibTableColumn
tSyncIfTimingAdmBITSOutAdmStatus = _TSyncIfTimingAdmBITSOutAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 16),
    _TSyncIfTimingAdmBITSOutAdmStatus_Type()
)
tSyncIfTimingAdmBITSOutAdmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmBITSOutAdmStatus.setStatus("current")


class _TSyncIfTimingAdmBITSOutLineLen_Type(Integer32):
    """Custom type tSyncIfTimingAdmBITSOutLineLen based on Integer32"""
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("length0To110", 1),
          ("length110To220", 2),
          ("length220To330", 3),
          ("length330To440", 4),
          ("length440To550", 5),
          ("length550To660", 6),
          ("lengthNotApplicable", 0))
    )


_TSyncIfTimingAdmBITSOutLineLen_Type.__name__ = "Integer32"
_TSyncIfTimingAdmBITSOutLineLen_Object = MibTableColumn
tSyncIfTimingAdmBITSOutLineLen = _TSyncIfTimingAdmBITSOutLineLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 17),
    _TSyncIfTimingAdmBITSOutLineLen_Type()
)
tSyncIfTimingAdmBITSOutLineLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmBITSOutLineLen.setStatus("current")


class _TSyncIfTimingAdmRef1CfgQltyLevel_Type(TmnxSSMQualityLevel):
    """Custom type tSyncIfTimingAdmRef1CfgQltyLevel based on TmnxSSMQualityLevel"""


_TSyncIfTimingAdmRef1CfgQltyLevel_Object = MibTableColumn
tSyncIfTimingAdmRef1CfgQltyLevel = _TSyncIfTimingAdmRef1CfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 18),
    _TSyncIfTimingAdmRef1CfgQltyLevel_Type()
)
tSyncIfTimingAdmRef1CfgQltyLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef1CfgQltyLevel.setStatus("current")


class _TSyncIfTimingAdmRef2CfgQltyLevel_Type(TmnxSSMQualityLevel):
    """Custom type tSyncIfTimingAdmRef2CfgQltyLevel based on TmnxSSMQualityLevel"""


_TSyncIfTimingAdmRef2CfgQltyLevel_Object = MibTableColumn
tSyncIfTimingAdmRef2CfgQltyLevel = _TSyncIfTimingAdmRef2CfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 19),
    _TSyncIfTimingAdmRef2CfgQltyLevel_Type()
)
tSyncIfTimingAdmRef2CfgQltyLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef2CfgQltyLevel.setStatus("current")


class _TSyncIfTimingAdmBITSCfgQltyLevel_Type(TmnxSSMQualityLevel):
    """Custom type tSyncIfTimingAdmBITSCfgQltyLevel based on TmnxSSMQualityLevel"""


_TSyncIfTimingAdmBITSCfgQltyLevel_Object = MibTableColumn
tSyncIfTimingAdmBITSCfgQltyLevel = _TSyncIfTimingAdmBITSCfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 20),
    _TSyncIfTimingAdmBITSCfgQltyLevel_Type()
)
tSyncIfTimingAdmBITSCfgQltyLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmBITSCfgQltyLevel.setStatus("current")


class _TSyncIfTimingAdmRef1NationalUse_Type(Unsigned32):
    """Custom type tSyncIfTimingAdmRef1NationalUse based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_TSyncIfTimingAdmRef1NationalUse_Type.__name__ = "Unsigned32"
_TSyncIfTimingAdmRef1NationalUse_Object = MibTableColumn
tSyncIfTimingAdmRef1NationalUse = _TSyncIfTimingAdmRef1NationalUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 21),
    _TSyncIfTimingAdmRef1NationalUse_Type()
)
tSyncIfTimingAdmRef1NationalUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef1NationalUse.setStatus("current")


class _TSyncIfTimingAdmRef2NationalUse_Type(Unsigned32):
    """Custom type tSyncIfTimingAdmRef2NationalUse based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_TSyncIfTimingAdmRef2NationalUse_Type.__name__ = "Unsigned32"
_TSyncIfTimingAdmRef2NationalUse_Object = MibTableColumn
tSyncIfTimingAdmRef2NationalUse = _TSyncIfTimingAdmRef2NationalUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 22),
    _TSyncIfTimingAdmRef2NationalUse_Type()
)
tSyncIfTimingAdmRef2NationalUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRef2NationalUse.setStatus("current")


class _TSyncIfTimingAdmBITSNationalUse_Type(Unsigned32):
    """Custom type tSyncIfTimingAdmBITSNationalUse based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_TSyncIfTimingAdmBITSNationalUse_Type.__name__ = "Unsigned32"
_TSyncIfTimingAdmBITSNationalUse_Object = MibTableColumn
tSyncIfTimingAdmBITSNationalUse = _TSyncIfTimingAdmBITSNationalUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 23),
    _TSyncIfTimingAdmBITSNationalUse_Type()
)
tSyncIfTimingAdmBITSNationalUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmBITSNationalUse.setStatus("current")


class _TSyncIfTimingAdmQLSelection_Type(TmnxEnabledDisabled):
    """Custom type tSyncIfTimingAdmQLSelection based on TmnxEnabledDisabled"""


_TSyncIfTimingAdmQLSelection_Object = MibTableColumn
tSyncIfTimingAdmQLSelection = _TSyncIfTimingAdmQLSelection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 24),
    _TSyncIfTimingAdmQLSelection_Type()
)
tSyncIfTimingAdmQLSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmQLSelection.setStatus("current")


class _TSyncIfTimingAdmRefOrder4_Type(TmnxSETSRefSource):
    """Custom type tSyncIfTimingAdmRefOrder4 based on TmnxSETSRefSource"""


_TSyncIfTimingAdmRefOrder4_Object = MibTableColumn
tSyncIfTimingAdmRefOrder4 = _TSyncIfTimingAdmRefOrder4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 25),
    _TSyncIfTimingAdmRefOrder4_Type()
)
tSyncIfTimingAdmRefOrder4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRefOrder4.setStatus("current")


class _TSyncIfTimingAdmPTPAdminStatus_Type(TmnxPortAdminStatus):
    """Custom type tSyncIfTimingAdmPTPAdminStatus based on TmnxPortAdminStatus"""


_TSyncIfTimingAdmPTPAdminStatus_Object = MibTableColumn
tSyncIfTimingAdmPTPAdminStatus = _TSyncIfTimingAdmPTPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 26),
    _TSyncIfTimingAdmPTPAdminStatus_Type()
)
tSyncIfTimingAdmPTPAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmPTPAdminStatus.setStatus("current")


class _TSyncIfTimingAdmPTPCfgQltyLevel_Type(TmnxSSMQualityLevel):
    """Custom type tSyncIfTimingAdmPTPCfgQltyLevel based on TmnxSSMQualityLevel"""


_TSyncIfTimingAdmPTPCfgQltyLevel_Object = MibTableColumn
tSyncIfTimingAdmPTPCfgQltyLevel = _TSyncIfTimingAdmPTPCfgQltyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 27),
    _TSyncIfTimingAdmPTPCfgQltyLevel_Type()
)
tSyncIfTimingAdmPTPCfgQltyLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmPTPCfgQltyLevel.setStatus("current")


class _TSyncIfTimingAdmBITSOutSource_Type(TmnxBITSOutSource):
    """Custom type tSyncIfTimingAdmBITSOutSource based on TmnxBITSOutSource"""


_TSyncIfTimingAdmBITSOutSource_Object = MibTableColumn
tSyncIfTimingAdmBITSOutSource = _TSyncIfTimingAdmBITSOutSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 28),
    _TSyncIfTimingAdmBITSOutSource_Type()
)
tSyncIfTimingAdmBITSOutSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmBITSOutSource.setStatus("current")


class _TSyncIfTimingAdmRefOrder5_Type(TmnxSETSRefSource):
    """Custom type tSyncIfTimingAdmRefOrder5 based on TmnxSETSRefSource"""


_TSyncIfTimingAdmRefOrder5_Object = MibTableColumn
tSyncIfTimingAdmRefOrder5 = _TSyncIfTimingAdmRefOrder5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 50),
    _TSyncIfTimingAdmRefOrder5_Type()
)
tSyncIfTimingAdmRefOrder5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmRefOrder5.setStatus("current")


class _TSyncIfTimingAdmBITS2InAdminStatus_Type(TmnxPortAdminStatus):
    """Custom type tSyncIfTimingAdmBITS2InAdminStatus based on TmnxPortAdminStatus"""


_TSyncIfTimingAdmBITS2InAdminStatus_Object = MibTableColumn
tSyncIfTimingAdmBITS2InAdminStatus = _TSyncIfTimingAdmBITS2InAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 51),
    _TSyncIfTimingAdmBITS2InAdminStatus_Type()
)
tSyncIfTimingAdmBITS2InAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmBITS2InAdminStatus.setStatus("current")


class _TSyncIfTimingAdmBITS2OutAdminStatus_Type(TmnxPortAdminStatus):
    """Custom type tSyncIfTimingAdmBITS2OutAdminStatus based on TmnxPortAdminStatus"""


_TSyncIfTimingAdmBITS2OutAdminStatus_Object = MibTableColumn
tSyncIfTimingAdmBITS2OutAdminStatus = _TSyncIfTimingAdmBITS2OutAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 8, 2, 1, 1, 52),
    _TSyncIfTimingAdmBITS2OutAdminStatus_Type()
)
tSyncIfTimingAdmBITS2OutAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSyncIfTimingAdmBITS2OutAdminStatus.setStatus("current")
_TmnxHwNotification_ObjectIdentity = ObjectIdentity
tmnxHwNotification = _TmnxHwNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2)
)
_TmnxChassisNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxChassisNotifyPrefix = _TmnxChassisNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1)
)
_TmnxChassisNotification_ObjectIdentity = ObjectIdentity
tmnxChassisNotification = _TmnxChassisNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0)
)
tmnxCpmCardEntry.registerAugmentions(
    ("TIMETRA-CHASSIS-MIB",
     "tmnxSyncIfTimingEntry")
)
tmnxSyncIfTimingEntry.setIndexNames(*tmnxCpmCardEntry.getIndexNames())
tmnxCardEntry.registerAugmentions(
    ("TIMETRA-CHASSIS-MIB",
     "tmnxVirtualSchedulerAdjEntry")
)
tmnxVirtualSchedulerAdjEntry.setIndexNames(*tmnxCardEntry.getIndexNames())

# Managed Objects groups

tmnxChassisNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 4)
)
tmnxChassisNotifyObjsGroup.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxEqNotificationRow"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqTypeNotificationRow"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxRedSecondaryCPMStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyOID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyMismatchedVer"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifySoftwareLocation"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotifyObjsGroup.setStatus("current")

tmnxChassisV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 9)
)
tmnxChassisV3v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisTotalNumber"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisLastChange"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisRowStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisLocation"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisCoordinates"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNumSlots"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNumPorts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNumPwrSupplies"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNumFanTrays"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNumFans"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisCriticalLEDState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisMajorLEDState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisMinorLEDState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisBaseMacAddress"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisCLLICode"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisReboot"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpgrade"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisAdminMode"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisOperMode"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisModeForce"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpdateWaitTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpdateTimeLeft"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisFanOperStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisFanSpeed"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyACStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyDCStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempThreshold"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply1Status"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply2Status"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyAssignedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisTypeName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisTypeDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisTypeStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwLastChange"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwMfgString"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwMfgBoardNumber"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSerialNumber"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwManufactureDate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwAlias"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwAssetID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwCLEI"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwIsFRU"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwContainedIn"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwParentRelPos"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwAdminState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwOperState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwTempSensor"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwTemperature"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwTempThreshold"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwBootCodeVersion"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSwLastBoot"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwAlarmState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwLastAlarmEvent"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClearAlarms"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSwImageSource"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwMfgDeviations"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwBaseMacAddress"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwFailureReason"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwContainedIndex"))
)
if mibBuilder.loadTexts:
    tmnxChassisV3v0Group.setStatus("obsolete")

tmnxMDAV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 10)
)
tmnxMDAV3v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDASupportedTypes"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAAssignedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAEquippedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMaxPorts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAEquippedPorts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDATxTimingSelected"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDASyncIfTimingStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDANetworkIngQueues"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDACapabilities"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMinChannelization"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMaxChannelization"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMaxChannels"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAChannelsInUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDACcagId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaTypeName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaTypeDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaTypeStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagRowStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagAdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagOperStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagCcaRate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagAccessAdaptQos"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathRate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathRateOption"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathWeight"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcEgrPoolResvCbs"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcEgrPoolSlpPlcy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcIngPoolResvCbs"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcIngPoolSlpPlcy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcAcctPolicyId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcCollectStats"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcQueuePlcy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcMac"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcMtu"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcHwMac"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcUserAssignedMac"))
)
if mibBuilder.loadTexts:
    tmnxMDAV3v0Group.setStatus("obsolete")

tmnxChassisObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 11)
)
tmnxChassisObsoleteGroup.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwSwState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardAllowedTypes"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardAllowedTypes"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAAllowedTypes"))
)
if mibBuilder.loadTexts:
    tmnxChassisObsoleteGroup.setStatus("current")

tmnxCardV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 12)
)
tmnxCardV3v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxCardLastChange"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardTypeName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardTypeDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardTypeStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardSupportedTypes"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardAssignedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardEquippedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardClockSource"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardNumMdaSlots"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardNumMdas"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardReboot"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardMemorySize"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardLastChange"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardSupportedTypes"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardAssignedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardEquippedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardBootOptionVersion"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardBootOptionLastModified"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigBootedVersion"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardIndexBootedVersion"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigLastModified"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigLastSaved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardRedundant"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardClockSource"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardNumCpus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardCpuType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardMemorySize"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardSwitchToRedundantCard"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardReboot"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardRereadBootOptions"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigFileLastBooted"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigFileLastSaved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigFileLastBootedHeader"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardIndexFileLastBootedHeader"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardBootOptionSource"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigSource"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardBootOptionLastSaved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFabricLastChange"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFabricAssignedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFabricEquippedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFabricHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmFlashOperStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmFlashSerialNumber"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmFlashFirmwareRevision"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmFlashModelNumber"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmFlashCapacity"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmFlashUsed"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmFlashHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRevert"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRefOrder1"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRefOrder2"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1SrcPort"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1AdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1InUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1Qualified"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2SrcPort"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2AdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2InUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2Qualified"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingFreqOffset"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRefOrder3"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSIfType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSAdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSInUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSQualified"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRevert"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRefOrder1"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRefOrder2"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef1SrcPort"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef1AdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef2SrcPort"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef2AdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmChanged"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRefOrder3"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmBITSIfType"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmBITSAdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisAdminOwner"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisAdminControlApply"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisAdminLastSetTimer"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisAdminLastSetTimeout"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITS2InAdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITS2OutAdminStatus"))
)
if mibBuilder.loadTexts:
    tmnxCardV3v0Group.setStatus("current")

tmnxMDAV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 13)
)
tmnxMDAV4v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDASupportedTypes"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAAssignedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAEquippedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMaxPorts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAEquippedPorts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDATxTimingSelected"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDASyncIfTimingStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDANetworkIngQueues"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDACapabilities"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMinChannelization"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMaxChannelization"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMaxChannels"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAChannelsInUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDACcagId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaTypeName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaTypeDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaTypeStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAReboot"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagRowStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagAdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagOperStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagCcaRate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagAccessAdaptQos"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathRate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathRateOption"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathWeight"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcEgrPoolResvCbs"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcEgrPoolSlpPlcy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcIngPoolResvCbs"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcIngPoolSlpPlcy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcAcctPolicyId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcCollectStats"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcQueuePlcy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcMac"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcMtu"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcHwMac"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcUserAssignedMac"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastSource"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastTapCount"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastGroup"))
)
if mibBuilder.loadTexts:
    tmnxMDAV4v0Group.setStatus("obsolete")

tmnx7710HwV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 15)
)
tmnx7710HwV3v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisOverTempState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardMasterSlaveRefState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcmOperStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcmHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcmEquippedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcmTypeName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcmTypeDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcmTypeStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMcmSupportedTypes"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMcmAssignedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMcmEquippedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMcmHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMcmTypeName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMcmTypeDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMcmTypeStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyInputStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyOutputStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAReboot"))
)
if mibBuilder.loadTexts:
    tmnx7710HwV3v0Group.setStatus("current")

tmnxChassisV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 16)
)
tmnxChassisV5v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisTotalNumber"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisLastChange"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisRowStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisLocation"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisCoordinates"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNumSlots"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNumPorts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNumPwrSupplies"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNumFanTrays"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNumFans"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisCriticalLEDState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisMajorLEDState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisMinorLEDState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisBaseMacAddress"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisCLLICode"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisReboot"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpgrade"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisAdminMode"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisOperMode"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisModeForce"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpdateTimeLeft"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisFanOperStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisFanSpeed"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyACStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyDCStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempThreshold"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply1Status"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply2Status"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyAssignedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisTypeName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisTypeDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisTypeStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwLastChange"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwMfgString"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwMfgBoardNumber"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSerialNumber"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwManufactureDate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwAlias"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwAssetID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwCLEI"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwIsFRU"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwContainedIn"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwParentRelPos"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwAdminState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwOperState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwTempSensor"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwTemperature"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwTempThreshold"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwBootCodeVersion"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSwLastBoot"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwAlarmState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwLastAlarmEvent"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClearAlarms"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSwImageSource"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwMfgDeviations"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwBaseMacAddress"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwFailureReason"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwContainedIndex"))
)
if mibBuilder.loadTexts:
    tmnxChassisV5v0Group.setStatus("current")

tmnxChassisV5v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 17)
)
tmnxChassisV5v0ObsoleteGroup.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpdateWaitTime")
)
if mibBuilder.loadTexts:
    tmnxChassisV5v0ObsoleteGroup.setStatus("current")

tmnx77x0CESMDAV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 18)
)
tmnx77x0CESMDAV6v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDAClockMode"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDADiffTimestampFreq"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAIngNamedPoolPolicy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAEgrNamedPoolPolicy"))
)
if mibBuilder.loadTexts:
    tmnx77x0CESMDAV6v0Group.setStatus("current")

tmnxIPsecIsaGrpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 19)
)
tmnxIPsecIsaGrpV6v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpTableLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpRowStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpAdminState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpOperState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpIsaChassis"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpPrimaryIsa"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpBackupIsa"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpActiveIsa"))
)
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpV6v0Group.setStatus("current")

tmnx7710SETSRefSrcHwV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 22)
)
tmnx7710SETSRefSrcHwV6v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1SrcHw"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1BITSIfType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2SrcHw"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2BITSIfType"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef1SrcHw"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef1BITSIfType"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef2SrcHw"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef2BITSIfType"))
)
if mibBuilder.loadTexts:
    tmnx7710SETSRefSrcHwV6v0Group.setStatus("current")

tmnxChassisHsmdaV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 23)
)
tmnxChassisHsmdaV6v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDAIngHsmdaSchedPolicy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrTblLastChangd"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrRowStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrMaxRate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrGrp1Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrGrp2Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass1Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass1WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass2Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass2WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass3Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass3WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass4Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass4WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass5Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass5WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass6Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass6WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass7Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass7WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass8Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass8WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAIngHsmdaPoolPolicy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAEgrHsmdaPoolPolicy"))
)
if mibBuilder.loadTexts:
    tmnxChassisHsmdaV6v0Group.setStatus("obsolete")

tmnxMDAMcPathMgmtV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 24)
)
tmnxMDAMcPathMgmtV6v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtBwPlcyName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtPriPathLimit"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtSecPathLimit"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtAncPathLimit"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtAdminState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtPriInUseBw"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtSecInUseBw"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtAncInUseBw"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtBlkHoleInUseBw"))
)
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtV6v0Group.setStatus("current")

tmnxCardV6v0NamedPoolPlcyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 25)
)
tmnxCardV6v0NamedPoolPlcyGroup.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxCardNamedPoolAdminMode"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardNamedPoolOperMode"))
)
if mibBuilder.loadTexts:
    tmnxCardV6v0NamedPoolPlcyGroup.setStatus("current")

tmnxChassisNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 26)
)
tmnxChassisNotifyObjsV6v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardSyncFile"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotifyObjsV6v0Group.setStatus("current")

tmnxChassisV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 27)
)
tmnxChassisV6v1Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyPemType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardSoftReset"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardLastBootupReason"))
)
if mibBuilder.loadTexts:
    tmnxChassisV6v1Group.setStatus("current")

tmnxFPMcPathMgmtV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 28)
)
tmnxFPMcPathMgmtV6v1Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxFPMcPathMgmtBwPlcyName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPMcPathMgmtAdminState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPHiBwMcastSource"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPHiBwMcastAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPHiBwMcastTapCount"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPHiBwMcastGroup"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPHiBwMcastDefaultPathsOnly"))
)
if mibBuilder.loadTexts:
    tmnxFPMcPathMgmtV6v1Group.setStatus("current")

tmnxMDAV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 29)
)
tmnxMDAV6v1Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDASupportedTypes"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAAssignedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAEquippedType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMaxPorts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAEquippedPorts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDATxTimingSelected"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDASyncIfTimingStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDANetworkIngQueues"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDACapabilities"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMinChannelization"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMaxChannelization"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAMaxChannels"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAChannelsInUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaTypeName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaTypeDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaTypeStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAReboot"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastSource"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastTapCount"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastGroup"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDASynchronousEthernet"))
)
if mibBuilder.loadTexts:
    tmnxMDAV6v1Group.setStatus("current")

tmnxMDACcagV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 30)
)
tmnxMDACcagV6v1Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDACcagId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagRowStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagAdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagOperStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagCcaRate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagAccessAdaptQos"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathRate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathRateOption"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathWeight"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcEgrPoolResvCbs"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcEgrPoolSlpPlcy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcIngPoolResvCbs"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcIngPoolSlpPlcy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcAcctPolicyId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcCollectStats"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcQueuePlcy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcMac"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcMtu"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcHwMac"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcUserAssignedMac"))
)
if mibBuilder.loadTexts:
    tmnxMDACcagV6v1Group.setStatus("current")

tmnxMdaXplV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 31)
)
tmnxMdaXplV5v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDAXplErrorTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAXplFailedCount"))
)
if mibBuilder.loadTexts:
    tmnxMdaXplV5v0Group.setStatus("current")

tmnxChassisNotifyObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 32)
)
tmnxChassisNotifyObjsV5v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxCardComplexNumber"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardFwdDirection"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotifyObjsV5v0Group.setStatus("current")

tmnxChassisNotifyObjsV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 35)
)
tmnxChassisNotifyObjsV6v1Group.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxCardSoftResetState")
)
if mibBuilder.loadTexts:
    tmnxChassisNotifyObjsV6v1Group.setStatus("current")

tmnxChassisUserModV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 37)
)
tmnxChassisUserModV7v0Group.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigUserLastModified")
)
if mibBuilder.loadTexts:
    tmnxChassisUserModV7v0Group.setStatus("current")

tmnxCardPchipV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 38)
)
tmnxCardPchipV5v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx1IngrFcsOccur"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx1IngrFcsOccurTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx1EgrFcsOccur"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx1EgrFcsOccurTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx2IngrFcsOccur"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx2IngrFcsOccurTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx2EgrFcsOccur"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx2EgrFcsOccurTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx1MemParityOccur"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx1MemParityOccurTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx2MemParityOccur"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx2MemParityOccurTime"))
)
if mibBuilder.loadTexts:
    tmnxCardPchipV5v0Group.setStatus("current")

tmnxFPWredV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 39)
)
tmnxFPWredV7v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxFPWredBufAllocMin"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPWredBufAllocMax"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPWredResvCbsMin"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPWredResvCbsMax"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPWredSlopePolicy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPWredAdminState"))
)
if mibBuilder.loadTexts:
    tmnxFPWredV7v0Group.setStatus("current")

tmnxChassisV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 40)
)
tmnxChassisV7v0Group.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxChassisFanRevision")
)
if mibBuilder.loadTexts:
    tmnxChassisV7v0Group.setStatus("current")

tmnxIPsecV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 41)
)
tmnxIPsecV7v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpTunnels"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpMaxTunnels"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV7v0Group.setStatus("current")

tmnxSyncV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 43)
)
tmnxSyncV6v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1State"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2State"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSState"))
)
if mibBuilder.loadTexts:
    tmnxSyncV6v0Group.setStatus("current")

tmnxSyncIfTimingV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 44)
)
tmnxSyncIfTimingV8v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSOutAdmStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSOutLineLen"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1CfgQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1RxQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2CfgQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2RxQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSCfgQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSRxQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITS2InUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITS2Qualified"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITS2Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITS2RxQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITS2State"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1NationalUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2NationalUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSNationalUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingQLSelection"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingOtherCPMInUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingOtherCPMQual"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingOtherCPMAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingOtherCPMState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSOutRefSel"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSTxQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITS2AdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingSystemQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmBITSOutAdmStatus"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmBITSOutLineLen"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef1CfgQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef2CfgQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmBITSCfgQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef1NationalUse"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef2NationalUse"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmBITSNationalUse"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmQLSelection"))
)
if mibBuilder.loadTexts:
    tmnxSyncIfTimingV8v0Group.setStatus("current")

tmnxChassisV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 46)
)
tmnxChassisV8v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwEquippedPlatform"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisRedForcedSingleSfm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCapability"))
)
if mibBuilder.loadTexts:
    tmnxChassisV8v0Group.setStatus("current")

tmnxChassisMixedModeIomV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 47)
)
tmnxChassisMixedModeIomV8v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisMixedModeIomAdminMode"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisMixedModeIomUpgrList"))
)
if mibBuilder.loadTexts:
    tmnxChassisMixedModeIomV8v0Group.setStatus("current")

tmnxCardCamErrorV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 48)
)
tmnxCardCamErrorV6v1Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx1CAMErrorOccur"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx1CAMErrorOccurTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx2CAMErrorOccur"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx2CAMErrorOccurTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardCmplxCAMErrOccur"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardCmplxCAMErrOccurTime"))
)
if mibBuilder.loadTexts:
    tmnxCardCamErrorV6v1Group.setStatus("current")

tmnxChassisV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 49)
)
tmnxChassisV6v0Group.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxCardLastBootupReason")
)
if mibBuilder.loadTexts:
    tmnxChassisV6v0Group.setStatus("obsolete")

tmnxCardV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 50)
)
tmnxCardV7v0Group.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxCardFailOnError")
)
if mibBuilder.loadTexts:
    tmnxCardV7v0Group.setStatus("current")

tmnxAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 51)
)
tmnxAtmGroup.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxMDAAtmMode")
)
if mibBuilder.loadTexts:
    tmnxAtmGroup.setStatus("current")

tmnxChassisHwV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 52)
)
tmnxChassisHwV6v1Group.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwMfgAssemblyNumber")
)
if mibBuilder.loadTexts:
    tmnxChassisHwV6v1Group.setStatus("current")

tmnxChassisHwV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 53)
)
tmnxChassisHwV9v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxCpmCardOscillatorType"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwFirmwareCodeVersion"))
)
if mibBuilder.loadTexts:
    tmnxChassisHwV9v0Group.setStatus("current")

tmnxSyncIfTimingV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 54)
)
tmnxSyncIfTimingV9v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRefOrder4"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingPTPAdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingPTPInUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingPTPQualified"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingPTPAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingPTPCfgQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingPTPRxQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingPTPState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSOutSource"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRefOrder4"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmPTPAdminStatus"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmPTPCfgQltyLevel"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmBITSOutSource"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRefOrder5"),
        ("TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRefOrder5"))
)
if mibBuilder.loadTexts:
    tmnxSyncIfTimingV9v0Group.setStatus("current")

tmnxChassisNotifyObjsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 56)
)
tmnxChassisNotifyObjsV9v0Group.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxMdaNotifyType")
)
if mibBuilder.loadTexts:
    tmnxChassisNotifyObjsV9v0Group.setStatus("current")

tmnxMDAV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 57)
)
tmnxMDAV9v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDAEgrHsmdaThrshLoBrstMult"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAEgrHsmdaThrshHiBrstInc"))
)
if mibBuilder.loadTexts:
    tmnxMDAV9v0Group.setStatus("current")

tmnxCardPchipV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 58)
)
tmnxCardPchipV8v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx1EgrFcsSrcSlots"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardCmplx2EgrFcsSrcSlots"))
)
if mibBuilder.loadTexts:
    tmnxCardPchipV8v0Group.setStatus("current")

tmnxChassisNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 59)
)
tmnxChassisNotifyObjsV8v0Group.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxCardSrcSlotBitmap")
)
if mibBuilder.loadTexts:
    tmnxChassisNotifyObjsV8v0Group.setStatus("current")

tmnxFPQGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 60)
)
tmnxFPQGrpGroup.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpAcctgPolId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpCollectStats"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpDescr"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpLastChgd"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpRowStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpPolicerPol"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpTableLastChgd"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpAcctgPolId"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpCollectStats"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpDescr"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpLastChgd"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpRowStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpPolicerPol"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpTableLastChgd"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQGrpPStatMode"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffHPrioPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffHPrioPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffHPrioPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpHPrioPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpHPrioPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpHPrioPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffLPrioPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffLPrioPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffLPrioPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpLPrioPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpLPrioPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpLPrioPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffHPrioOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffHPrioOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffHPrioOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpHPrioOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpHPrioOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpHPrioOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffLPrioOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffLPrioOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStOffLPrioOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpLPrioOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpLPrioOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStDrpLPrioOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdInProfPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdInProfPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdInProfPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdOutProfPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdOutProfPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdOutProfPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdInProfOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdInProfOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdInProfOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdOutProfOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdOutProfOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStFwdOutProfOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStUncolPktsOff"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStUncolPktsOffL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStUncolPktsOffH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStUncolOctsOff"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStUncolOctsOffL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPNetIngQgPStUncolOctsOffH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQGrpPStatMode"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffHPrioPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffHPrioPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffHPrioPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpHPrioPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpHPrioPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpHPrioPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffLPrioPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffLPrioPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffLPrioPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpLPrioPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpLPrioPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpLPrioPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffHPrioOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffHPrioOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffHPrioOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpHPrioOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpHPrioOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpHPrioOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffLPrioOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffLPrioOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStOffLPrioOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpLPrioOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpLPrioOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStDrpLPrioOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdInProfPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdInProfPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdInProfPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdOutProfPkts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdOutProfPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdOutProfPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdInProfOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdInProfOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdInProfOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdOutProfOcts"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdOutProfOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStFwdOutProfOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStUncolPktsOff"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStUncolPktsOffL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStUncolPktsOffH"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStUncolOctsOff"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStUncolOctsOffL"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFPAccIngQgPStUncolOctsOffH"),
        ("TIMETRA-CHASSIS-MIB", "tFPNetIngQGrpArbitStatFwdPkts"),
        ("TIMETRA-CHASSIS-MIB", "tFPNetIngQGrpArbitStatFwdPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tFPNetIngQGrpArbitStatFwdPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tFPNetIngQGrpArbitStatFwdOcts"),
        ("TIMETRA-CHASSIS-MIB", "tFPNetIngQGrpArbitStatFwdOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tFPNetIngQGrpArbitStatFwdOctsH"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpArbitStatFwdPkts"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpArbitStatFwdPktsL"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpArbitStatFwdPktsH"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpArbitStatFwdOcts"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpArbitStatFwdOctsL"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpArbitStatFwdOctsH"))
)
if mibBuilder.loadTexts:
    tmnxFPQGrpGroup.setStatus("current")

tmnxCardV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 61)
)
tmnxCardV10v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxCardHardResetUnsupMdas"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardRateCalcFastQueue"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardRateCalcSlowQueue"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardSchedRun"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardTaskScheduling"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardSlowQueueThresh"))
)
if mibBuilder.loadTexts:
    tmnxCardV10v0Group.setStatus("current")

tmnxIpsecV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 62)
)
tmnxIpsecV10v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpTunnelReassembly"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpOperFlags"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpIpTunnels"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpIpMaxTunnels"))
)
if mibBuilder.loadTexts:
    tmnxIpsecV10v0Group.setStatus("current")

tmnxChassisV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 63)
)
tmnxChassisV10v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxFanTrayCompSpeed"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFabricSupportedTypes"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFabricReboot"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFabricTypeName"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFabricTypeDescription"),
        ("TIMETRA-CHASSIS-MIB", "tmnxFabricTypeStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourceCurrentVoltage"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourcePeakVoltage"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourcePeakVoltageTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourceMinVoltage"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourceMinVoltageTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourceCurrentWattage"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourcePeakWattage"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourcePeakWattageTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourceMinWattage"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourceMinWattageTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourceCurrentAmperage"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourcePeakAmperage"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourcePeakAmperageTime"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourceMinAmperage"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwResourceMinAmperageTime"))
)
if mibBuilder.loadTexts:
    tmnxChassisV10v0Group.setStatus("current")

tmnxFPQGrpV10v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 65)
)
tmnxFPQGrpV10v0R4Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpPlcrOvrTblLstChgd"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpPlcrOvrRowStatus"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpPlcrOvrLastChgd"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpPlcrOvrAdminPIR"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpPlcrOvrAdminCIR"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpPlcrOvrStatMode"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpPlcrOvrMBS"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpPlcrOvrCBS"),
        ("TIMETRA-CHASSIS-MIB", "tFPAccIngQGrpPlcrOvrPktOffset"))
)
if mibBuilder.loadTexts:
    tmnxFPQGrpV10v0R4Group.setStatus("current")

tmnxMdaV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 66)
)
tmnxMdaV10v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDAIsaTunnelGroup"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpMultiActive"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpActiveMda"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAIsaTunnelGroupInUse"))
)
if mibBuilder.loadTexts:
    tmnxMdaV10v0Group.setStatus("current")

tmnxMdaObsoletedV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 67)
)
tmnxMdaObsoletedV10v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDAIngHsmdaSchedPolicy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAIngHsmdaPoolPolicy"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrTblLastChangd"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrRowStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrLastChanged"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrMaxRate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrGrp1Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrGrp2Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass1Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass1WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass2Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass2WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass3Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass3WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass4Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass4WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass5Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass5WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass6Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass6WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass7Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass7WtInGrp"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass8Rate"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHsmdaMdaSchOvrClass8WtInGrp"))
)
if mibBuilder.loadTexts:
    tmnxMdaObsoletedV10v0Group.setStatus("current")

tmnxMdaHsmdaPoolV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 70)
)
tmnxMdaHsmdaPoolV10v0Group.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxMDAEgrHsmdaPoolPolicy")
)
if mibBuilder.loadTexts:
    tmnxMdaHsmdaPoolV10v0Group.setStatus("current")


# Notification objects

tmnxHwConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 1)
)
tmnxHwConfigChange.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxHwConfigChange.setStatus(
        "obsolete"
    )

tmnxEnvTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 2)
)
tmnxEnvTempTooHigh.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwTemperature"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwTempThreshold"))
)
if mibBuilder.loadTexts:
    tmnxEnvTempTooHigh.setStatus(
        "current"
    )

tmnxEqPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 3)
)
tmnxEqPowerSupplyFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyACStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyDCStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempThreshold"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply1Status"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply2Status"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyInputStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyOutputStatus"))
)
if mibBuilder.loadTexts:
    tmnxEqPowerSupplyFailure.setStatus(
        "current"
    )

tmnxEqPowerSupplyInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 4)
)
tmnxEqPowerSupplyInserted.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqPowerSupplyInserted.setStatus(
        "current"
    )

tmnxEqPowerSupplyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 5)
)
tmnxEqPowerSupplyRemoved.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqPowerSupplyRemoved.setStatus(
        "current"
    )

tmnxEqFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 6)
)
tmnxEqFanFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisFanOperStatus"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisFanSpeed"))
)
if mibBuilder.loadTexts:
    tmnxEqFanFailure.setStatus(
        "current"
    )

tmnxEqCardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 7)
)
tmnxEqCardFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwOperState"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxEqCardFailure.setStatus(
        "current"
    )

tmnxEqCardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 8)
)
tmnxEqCardInserted.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardName"))
)
if mibBuilder.loadTexts:
    tmnxEqCardInserted.setStatus(
        "current"
    )

tmnxEqCardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 9)
)
tmnxEqCardRemoved.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardName"))
)
if mibBuilder.loadTexts:
    tmnxEqCardRemoved.setStatus(
        "current"
    )

tmnxEqWrongCard = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 10)
)
tmnxEqWrongCard.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqWrongCard.setStatus(
        "current"
    )

tmnxEqCpuFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 11)
)
tmnxEqCpuFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqCpuFailure.setStatus(
        "obsolete"
    )

tmnxEqMemoryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 12)
)
tmnxEqMemoryFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqMemoryFailure.setStatus(
        "obsolete"
    )

tmnxEqBackdoorBusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 13)
)
tmnxEqBackdoorBusFailure.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId")
)
if mibBuilder.loadTexts:
    tmnxEqBackdoorBusFailure.setStatus(
        "obsolete"
    )

tmnxPeSoftwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 14)
)
tmnxPeSoftwareError.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeSoftwareError.setStatus(
        "obsolete"
    )

tmnxPeSoftwareAbnormalHalt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 15)
)
tmnxPeSoftwareAbnormalHalt.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeSoftwareAbnormalHalt.setStatus(
        "obsolete"
    )

tmnxPeSoftwareVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 16)
)
tmnxPeSoftwareVersionMismatch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyMismatchedVer"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"))
)
if mibBuilder.loadTexts:
    tmnxPeSoftwareVersionMismatch.setStatus(
        "current"
    )

tmnxPeOutOfMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 17)
)
tmnxPeOutOfMemory.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeOutOfMemory.setStatus(
        "obsolete"
    )

tmnxPeConfigurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 18)
)
tmnxPeConfigurationError.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeConfigurationError.setStatus(
        "obsolete"
    )

tmnxPeStorageProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 19)
)
tmnxPeStorageProblem.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeStorageProblem.setStatus(
        "obsolete"
    )

tmnxPeCpuCyclesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 20)
)
tmnxPeCpuCyclesExceeded.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeCpuCyclesExceeded.setStatus(
        "obsolete"
    )

tmnxRedPrimaryCPMFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 21)
)
tmnxRedPrimaryCPMFail.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxRedPrimaryCPMFail.setStatus(
        "current"
    )

tmnxRedSecondaryCPMStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 22)
)
tmnxRedSecondaryCPMStatusChange.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxRedSecondaryCPMStatus"))
)
if mibBuilder.loadTexts:
    tmnxRedSecondaryCPMStatusChange.setStatus(
        "obsolete"
    )

tmnxRedRestoreSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 23)
)
tmnxRedRestoreSuccess.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxRedRestoreSuccess.setStatus(
        "obsolete"
    )

tmnxRedRestoreFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 24)
)
tmnxRedRestoreFail.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxRedRestoreFail.setStatus(
        "obsolete"
    )

tmnxChassisNotificationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 25)
)
tmnxChassisNotificationClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyOID"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationClear.setStatus(
        "current"
    )

tmnxEqSyncIfTimingHoldover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 26)
)
tmnxEqSyncIfTimingHoldover.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingHoldover.setStatus(
        "current"
    )

tmnxEqSyncIfTimingHoldoverClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 27)
)
tmnxEqSyncIfTimingHoldoverClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingHoldoverClear.setStatus(
        "current"
    )

tmnxEqSyncIfTimingRef1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 28)
)
tmnxEqSyncIfTimingRef1Alarm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingRef1Alarm.setStatus(
        "current"
    )

tmnxEqSyncIfTimingRef1AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 29)
)
tmnxEqSyncIfTimingRef1AlarmClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingRef1AlarmClear.setStatus(
        "current"
    )

tmnxEqSyncIfTimingRef2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 30)
)
tmnxEqSyncIfTimingRef2Alarm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingRef2Alarm.setStatus(
        "current"
    )

tmnxEqSyncIfTimingRef2AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 31)
)
tmnxEqSyncIfTimingRef2AlarmClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingRef2AlarmClear.setStatus(
        "current"
    )

tmnxEqFlashDataLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 32)
)
tmnxEqFlashDataLoss.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwOperState"))
)
if mibBuilder.loadTexts:
    tmnxEqFlashDataLoss.setStatus(
        "current"
    )

tmnxEqFlashDiskFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 33)
)
tmnxEqFlashDiskFull.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwOperState"))
)
if mibBuilder.loadTexts:
    tmnxEqFlashDiskFull.setStatus(
        "current"
    )

tmnxPeSoftwareLoadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 34)
)
tmnxPeSoftwareLoadFailed.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifySoftwareLocation"))
)
if mibBuilder.loadTexts:
    tmnxPeSoftwareLoadFailed.setStatus(
        "current"
    )

tmnxPeBootloaderVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 35)
)
tmnxPeBootloaderVersionMismatch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyMismatchedVer"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"))
)
if mibBuilder.loadTexts:
    tmnxPeBootloaderVersionMismatch.setStatus(
        "current"
    )

tmnxPeBootromVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 36)
)
tmnxPeBootromVersionMismatch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyMismatchedVer"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"))
)
if mibBuilder.loadTexts:
    tmnxPeBootromVersionMismatch.setStatus(
        "current"
    )

tmnxPeFPGAVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 37)
)
tmnxPeFPGAVersionMismatch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyMismatchedVer"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"))
)
if mibBuilder.loadTexts:
    tmnxPeFPGAVersionMismatch.setStatus(
        "current"
    )

tmnxEqSyncIfTimingBITSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 38)
)
tmnxEqSyncIfTimingBITSAlarm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingBITSAlarm.setStatus(
        "current"
    )

tmnxEqSyncIfTimingBITSAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 39)
)
tmnxEqSyncIfTimingBITSAlarmClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingBITSAlarmClear.setStatus(
        "current"
    )

tmnxEqCardFirmwareUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 40)
)
tmnxEqCardFirmwareUpgraded.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqCardFirmwareUpgraded.setStatus(
        "current"
    )

tmnxChassisUpgradeInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 41)
)
tmnxChassisUpgradeInProgress.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxChassisUpgradeInProgress.setStatus(
        "current"
    )

tmnxChassisUpgradeComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 42)
)
tmnxChassisUpgradeComplete.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxChassisUpgradeComplete.setStatus(
        "current"
    )

tmnxChassisHiBwMcastAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 43)
)
tmnxChassisHiBwMcastAlarm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxChassisHiBwMcastAlarm.setStatus(
        "current"
    )

tmnxEqMdaCfgNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 44)
)
tmnxEqMdaCfgNotCompatible.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaNotifyType"))
)
if mibBuilder.loadTexts:
    tmnxEqMdaCfgNotCompatible.setStatus(
        "current"
    )

tmnxCpmCardSyncFileNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 45)
)
tmnxCpmCardSyncFileNotPresent.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardSyncFile"))
)
if mibBuilder.loadTexts:
    tmnxCpmCardSyncFileNotPresent.setStatus(
        "current"
    )

tmnxEqMdaXplError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 46)
)
tmnxEqMdaXplError.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxMDAXplFailedCount")
)
if mibBuilder.loadTexts:
    tmnxEqMdaXplError.setStatus(
        "current"
    )

tmnxEqCardPChipError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 47)
)
tmnxEqCardPChipError.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardComplexNumber"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardFwdDirection"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardSrcSlotBitmap"))
)
if mibBuilder.loadTexts:
    tmnxEqCardPChipError.setStatus(
        "current"
    )

tmnxEqCardSoftResetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 48)
)
tmnxEqCardSoftResetAlarm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardSoftResetState"))
)
if mibBuilder.loadTexts:
    tmnxEqCardSoftResetAlarm.setStatus(
        "current"
    )

tmnxEqMdaSyncENotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 49)
)
tmnxEqMdaSyncENotCompatible.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMdaNotifyType"))
)
if mibBuilder.loadTexts:
    tmnxEqMdaSyncENotCompatible.setStatus(
        "current"
    )

tmnxIPsecIsaGrpActiveIsaChgd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 50)
)
tmnxIPsecIsaGrpActiveIsaChgd.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpPrimaryIsa"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpBackupIsa"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpActiveIsa"))
)
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpActiveIsaChgd.setStatus(
        "current"
    )

tmnxEqCardPChipMemoryEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 51)
)
tmnxEqCardPChipMemoryEvent.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardComplexNumber"))
)
if mibBuilder.loadTexts:
    tmnxEqCardPChipMemoryEvent.setStatus(
        "current"
    )

tmnxIPsecIsaGrpUnableToSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 52)
)
tmnxIPsecIsaGrpUnableToSwitch.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpActiveIsa")
)
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpUnableToSwitch.setStatus(
        "current"
    )

tmnxIPsecIsaGrpTnlLowWMark = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 53)
)
tmnxIPsecIsaGrpTnlLowWMark.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpTunnels"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpMaxTunnels"))
)
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpTnlLowWMark.setStatus(
        "current"
    )

tmnxIPsecIsaGrpTnlHighWMark = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 54)
)
tmnxIPsecIsaGrpTnlHighWMark.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpTunnels"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpMaxTunnels"))
)
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpTnlHighWMark.setStatus(
        "current"
    )

tmnxIPsecIsaGrpTnlMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 55)
)
tmnxIPsecIsaGrpTnlMax.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpTunnels"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpMaxTunnels"))
)
if mibBuilder.loadTexts:
    tmnxIPsecIsaGrpTnlMax.setStatus(
        "current"
    )

tmnxEqSyncIfTimingRef1Quality = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 56)
)
tmnxEqSyncIfTimingRef1Quality.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1RxQltyLevel")
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingRef1Quality.setStatus(
        "current"
    )

tmnxEqSyncIfTimingRef2Quality = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 57)
)
tmnxEqSyncIfTimingRef2Quality.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2RxQltyLevel")
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingRef2Quality.setStatus(
        "current"
    )

tmnxEqSyncIfTimingBITSQuality = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 58)
)
tmnxEqSyncIfTimingBITSQuality.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSRxQltyLevel")
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingBITSQuality.setStatus(
        "current"
    )

tmnxEqSyncIfTimingBITS2Quality = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 59)
)
tmnxEqSyncIfTimingBITS2Quality.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITS2RxQltyLevel")
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingBITS2Quality.setStatus(
        "current"
    )

tmnxEqSyncIfTimingRefSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 60)
)
tmnxEqSyncIfTimingRefSwitch.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1InUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2InUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSInUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITS2InUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingPTPInUse"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingRefSwitch.setStatus(
        "current"
    )

tmnxEqSyncIfTimingBITS2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 61)
)
tmnxEqSyncIfTimingBITS2Alarm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingBITS2Alarm.setStatus(
        "current"
    )

tmnxEqSyncIfTimingBITS2AlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 62)
)
tmnxEqSyncIfTimingBITS2AlarmClr.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingBITS2AlarmClr.setStatus(
        "current"
    )

tmnxEqSyncIfTimingBITSOutRefChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 63)
)
tmnxEqSyncIfTimingBITSOutRefChg.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSOutRefSel")
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingBITSOutRefChg.setStatus(
        "current"
    )

tmnxEqCardPChipCamEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 64)
)
tmnxEqCardPChipCamEvent.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCardComplexNumber"))
)
if mibBuilder.loadTexts:
    tmnxEqCardPChipCamEvent.setStatus(
        "current"
    )

tmnxEqSyncIfTimingSystemQuality = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 65)
)
tmnxEqSyncIfTimingSystemQuality.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingSystemQltyLevel")
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingSystemQuality.setStatus(
        "current"
    )

tmnxEqHwEnhancedCapability = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 66)
)
tmnxEqHwEnhancedCapability.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqHwEnhancedCapability.setStatus(
        "current"
    )

tmnxEqSyncIfTimingPTPQuality = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 67)
)
tmnxEqSyncIfTimingPTPQuality.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingPTPRxQltyLevel")
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingPTPQuality.setStatus(
        "current"
    )

tmnxEqSyncIfTimingPTPAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 68)
)
tmnxEqSyncIfTimingPTPAlarm.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingPTPAlarm.setStatus(
        "current"
    )

tmnxEqSyncIfTimingPTPAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 69)
)
tmnxEqSyncIfTimingPTPAlarmClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingPTPAlarmClear.setStatus(
        "current"
    )

tmnxPeFirmwareVersionWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 70)
)
tmnxPeFirmwareVersionWarning.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxHwFirmwareCodeVersion"))
)
if mibBuilder.loadTexts:
    tmnxPeFirmwareVersionWarning.setStatus(
        "current"
    )

tmnxMDAIsaTunnelGroupChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 71)
)
tmnxMDAIsaTunnelGroupChange.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxMDAIsaTunnelGroupInUse"),
        ("TIMETRA-CHASSIS-MIB", "tmnxMDAIsaTunnelGroup"))
)
if mibBuilder.loadTexts:
    tmnxMDAIsaTunnelGroupChange.setStatus(
        "current"
    )


# Notifications groups

tmnxChassisNotifyObsoleteGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 7)
)
tmnxChassisNotifyObsoleteGroup.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwConfigChange"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCpuFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqMemoryFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqBackdoorBusFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareError"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareAbnormalHalt"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeOutOfMemory"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeConfigurationError"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeStorageProblem"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeCpuCyclesExceeded"),
        ("TIMETRA-CHASSIS-MIB", "tmnxRedSecondaryCPMStatusChange"),
        ("TIMETRA-CHASSIS-MIB", "tmnxRedRestoreSuccess"),
        ("TIMETRA-CHASSIS-MIB", "tmnxRedRestoreFail"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotifyObsoleteGroup.setStatus(
        "current"
    )

tmnxChassisNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 14)
)
tmnxChassisNotificationV4v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxEnvTempTooHigh"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyInserted"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyRemoved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFanFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardInserted"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardRemoved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqWrongCard"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxRedPrimaryCPMFail"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotificationClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldover"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldoverClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1AlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2AlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFlashDataLoss"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFlashDiskFull"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareLoadFailed"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeBootloaderVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeBootromVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeFPGAVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardFirmwareUpgraded"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeInProgress"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeComplete"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisHiBwMcastAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqMdaCfgNotCompatible"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationV4v0Group.setStatus(
        "obsolete"
    )

tmnxChassisNotificationV3v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 20)
)
tmnxChassisNotificationV3v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxEnvTempTooHigh"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyInserted"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyRemoved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFanFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardInserted"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardRemoved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqWrongCard"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxRedPrimaryCPMFail"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotificationClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldover"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldoverClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1AlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2AlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFlashDataLoss"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFlashDiskFull"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareLoadFailed"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeBootloaderVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeBootromVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeFPGAVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardFirmwareUpgraded"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqMdaCfgNotCompatible"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationV3v0Group.setStatus(
        "obsolete"
    )

tmnxChassisNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 21)
)
tmnxChassisNotificationV6v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxEnvTempTooHigh"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyInserted"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyRemoved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFanFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardInserted"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardRemoved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqWrongCard"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxRedPrimaryCPMFail"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotificationClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldover"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldoverClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1AlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2AlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFlashDataLoss"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFlashDiskFull"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareLoadFailed"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeBootloaderVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeBootromVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeFPGAVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardFirmwareUpgraded"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeInProgress"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeComplete"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisHiBwMcastAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqMdaCfgNotCompatible"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardSyncFileNotPresent"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqMdaXplError"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardPChipError"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardPChipMemoryEvent"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationV6v0Group.setStatus(
        "obsolete"
    )

tmnxChassisNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 33)
)
tmnxChassisNotificationV5v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxEqMdaXplError"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardPChipError"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardPChipMemoryEvent"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationV5v0Group.setStatus(
        "obsolete"
    )

tmnxChassisNotificationV6v1Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 34)
)
tmnxChassisNotificationV6v1Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxEnvTempTooHigh"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyInserted"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyRemoved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFanFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardInserted"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardRemoved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqWrongCard"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxRedPrimaryCPMFail"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotificationClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldover"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldoverClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1AlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2AlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFlashDataLoss"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFlashDiskFull"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareLoadFailed"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeBootloaderVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeBootromVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeFPGAVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardFirmwareUpgraded"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeInProgress"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeComplete"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisHiBwMcastAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqMdaCfgNotCompatible"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardSyncFileNotPresent"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqMdaXplError"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardPChipError"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardSoftResetAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardPChipMemoryEvent"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardPChipCamEvent"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationV6v1Group.setStatus(
        "obsolete"
    )

tmnxChassisNotificationV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 36)
)
tmnxChassisNotificationV7v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxEnvTempTooHigh"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyInserted"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyRemoved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFanFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardFailure"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardInserted"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardRemoved"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqWrongCard"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxRedPrimaryCPMFail"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotificationClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldover"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldoverClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1AlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2AlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFlashDataLoss"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqFlashDiskFull"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareLoadFailed"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeBootloaderVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeBootromVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxPeFPGAVersionMismatch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarmClear"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardFirmwareUpgraded"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeInProgress"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeComplete"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisHiBwMcastAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqMdaCfgNotCompatible"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmCardSyncFileNotPresent"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqMdaXplError"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardPChipError"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardSoftResetAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqMdaSyncENotCompatible"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpActiveIsaChgd"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardPChipMemoryEvent"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpUnableToSwitch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqCardPChipCamEvent"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqHwEnhancedCapability"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationV7v0Group.setStatus(
        "current"
    )

tmnxIPsecNotifV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 42)
)
tmnxIPsecNotifV7v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpTnlLowWMark"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpTnlHighWMark"),
        ("TIMETRA-CHASSIS-MIB", "tmnxIPsecIsaGrpTnlMax"))
)
if mibBuilder.loadTexts:
    tmnxIPsecNotifV7v0Group.setStatus(
        "current"
    )

tmnxSyncIfTimingNotifV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 45)
)
tmnxSyncIfTimingNotifV8v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1Quality"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2Quality"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSQuality"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITS2Quality"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRefSwitch"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITS2Alarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITS2AlarmClr"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSOutRefChg"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingSystemQuality"))
)
if mibBuilder.loadTexts:
    tmnxSyncIfTimingNotifV8v0Group.setStatus(
        "current"
    )

tmnxSyncIfTimingNotifyV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 55)
)
tmnxSyncIfTimingNotifyV9v0Group.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingPTPQuality"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingPTPAlarm"),
        ("TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingPTPAlarmClear"))
)
if mibBuilder.loadTexts:
    tmnxSyncIfTimingNotifyV9v0Group.setStatus(
        "current"
    )

tmnxChassisNotificationV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 64)
)
tmnxChassisNotificationV9v0Group.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxPeFirmwareVersionWarning")
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationV9v0Group.setStatus(
        "current"
    )

tmnxChassisNotifyV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 69)
)
tmnxChassisNotifyV10v0Group.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxMDAIsaTunnelGroupChange")
)
if mibBuilder.loadTexts:
    tmnxChassisNotifyV10v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxChassisV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxChassisV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxChassisComp7710V3v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxChassisComp7710V3v0.setStatus(
        "obsolete"
    )

tmnxChassisComp7710V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxChassisComp7710V5v0.setStatus(
        "obsolete"
    )

tmnxChassisComp7710V6v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    tmnxChassisComp7710V6v0.setStatus(
        "obsolete"
    )

tmnxChassisComp7710V6v1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    tmnxChassisComp7710V6v1.setStatus(
        "obsolete"
    )

tmnxChassisComp7710V7v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    tmnxChassisComp7710V7v0.setStatus(
        "obsolete"
    )

tmnxChassisComp7710V8v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 5, 6)
)
if mibBuilder.loadTexts:
    tmnxChassisComp7710V8v0.setStatus(
        "obsolete"
    )

tmnxChassisV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxChassisV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxChassis7750V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxChassis7750V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxChassis7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxChassis7450V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxChassis7750V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxChassis7750V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxChassis7450V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxChassis7450V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxChassis7750V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxChassis7750V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxChassis7450V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxChassis7450V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxChassis7x50V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxChassis7x50V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxChassisV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxChassisV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxChassisV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxChassisV10v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-CHASSIS-MIB",
    **{"TmnxAlarmState": TmnxAlarmState,
       "TmnxChassisIndex": TmnxChassisIndex,
       "TmnxChassisIndexOrZero": TmnxChassisIndexOrZero,
       "TmnxHwIndex": TmnxHwIndex,
       "TmnxHwIndexOrZero": TmnxHwIndexOrZero,
       "TmnxHwClass": TmnxHwClass,
       "TmnxCardType": TmnxCardType,
       "TmnxCardSuppType": TmnxCardSuppType,
       "TmnxFabricType": TmnxFabricType,
       "TmnxFabricSuppType": TmnxFabricSuppType,
       "TmnxCardRebootType": TmnxCardRebootType,
       "TmnxChassisType": TmnxChassisType,
       "TmnxDeviceState": TmnxDeviceState,
       "TmnxLEDState": TmnxLEDState,
       "TmnxMdaType": TmnxMdaType,
       "TmnxMDASuppType": TmnxMDASuppType,
       "TmnxMDAChanType": TmnxMDAChanType,
       "TmnxMdaAtmMode": TmnxMdaAtmMode,
       "TmnxCcmType": TmnxCcmType,
       "TmnxMcmType": TmnxMcmType,
       "TmnxSlotNum": TmnxSlotNum,
       "TmnxSlotNumOrZero": TmnxSlotNumOrZero,
       "TmnxPortAdminStatus": TmnxPortAdminStatus,
       "TmnxChassisMode": TmnxChassisMode,
       "TmnxSETSRefSource": TmnxSETSRefSource,
       "TmnxSETSRefQualified": TmnxSETSRefQualified,
       "TmnxSETSRefAlarm": TmnxSETSRefAlarm,
       "TmnxBITSIfType": TmnxBITSIfType,
       "TmnxSSMQualityLevel": TmnxSSMQualityLevel,
       "TmnxRefInState": TmnxRefInState,
       "TmnxBITSOutSource": TmnxBITSOutSource,
       "TmnxCcagId": TmnxCcagId,
       "TmnxCcagRate": TmnxCcagRate,
       "TmnxCcagRateOption": TmnxCcagRateOption,
       "TmnxChassisPemType": TmnxChassisPemType,
       "TmnxCardSlotBitMap": TmnxCardSlotBitMap,
       "TmnxTunnelGroupId": TmnxTunnelGroupId,
       "TmnxTunnelGroupIdOrZero": TmnxTunnelGroupIdOrZero,
       "tmnxChassisMIBModule": tmnxChassisMIBModule,
       "tmnxHwConformance": tmnxHwConformance,
       "tmnxChassisConformance": tmnxChassisConformance,
       "tmnxChassisCompliances": tmnxChassisCompliances,
       "tmnxChassisV4v0Compliance": tmnxChassisV4v0Compliance,
       "tmnxChassisComp7710": tmnxChassisComp7710,
       "tmnxChassisComp7710V3v0": tmnxChassisComp7710V3v0,
       "tmnxChassisComp7710V5v0": tmnxChassisComp7710V5v0,
       "tmnxChassisComp7710V6v0": tmnxChassisComp7710V6v0,
       "tmnxChassisComp7710V6v1": tmnxChassisComp7710V6v1,
       "tmnxChassisComp7710V7v0": tmnxChassisComp7710V7v0,
       "tmnxChassisComp7710V8v0": tmnxChassisComp7710V8v0,
       "tmnxChassisV5v0Compliance": tmnxChassisV5v0Compliance,
       "tmnxChassis7750V6v0Compliance": tmnxChassis7750V6v0Compliance,
       "tmnxChassis7450V6v0Compliance": tmnxChassis7450V6v0Compliance,
       "tmnxChassis7750V6v1Compliance": tmnxChassis7750V6v1Compliance,
       "tmnxChassis7450V6v1Compliance": tmnxChassis7450V6v1Compliance,
       "tmnxChassis7750V7v0Compliance": tmnxChassis7750V7v0Compliance,
       "tmnxChassis7450V7v0Compliance": tmnxChassis7450V7v0Compliance,
       "tmnxChassis7x50V8v0Compliance": tmnxChassis7x50V8v0Compliance,
       "tmnxChassisV9v0Compliance": tmnxChassisV9v0Compliance,
       "tmnxChassisV10v0Compliance": tmnxChassisV10v0Compliance,
       "tmnxChassisGroups": tmnxChassisGroups,
       "tmnxChassisNotifyObjsGroup": tmnxChassisNotifyObjsGroup,
       "tmnxChassisNotifyObsoleteGroup": tmnxChassisNotifyObsoleteGroup,
       "tmnxChassisV3v0Group": tmnxChassisV3v0Group,
       "tmnxMDAV3v0Group": tmnxMDAV3v0Group,
       "tmnxChassisObsoleteGroup": tmnxChassisObsoleteGroup,
       "tmnxCardV3v0Group": tmnxCardV3v0Group,
       "tmnxMDAV4v0Group": tmnxMDAV4v0Group,
       "tmnxChassisNotificationV4v0Group": tmnxChassisNotificationV4v0Group,
       "tmnx7710HwV3v0Group": tmnx7710HwV3v0Group,
       "tmnxChassisV5v0Group": tmnxChassisV5v0Group,
       "tmnxChassisV5v0ObsoleteGroup": tmnxChassisV5v0ObsoleteGroup,
       "tmnx77x0CESMDAV6v0Group": tmnx77x0CESMDAV6v0Group,
       "tmnxIPsecIsaGrpV6v0Group": tmnxIPsecIsaGrpV6v0Group,
       "tmnxChassisNotificationV3v0Group": tmnxChassisNotificationV3v0Group,
       "tmnxChassisNotificationV6v0Group": tmnxChassisNotificationV6v0Group,
       "tmnx7710SETSRefSrcHwV6v0Group": tmnx7710SETSRefSrcHwV6v0Group,
       "tmnxChassisHsmdaV6v0Group": tmnxChassisHsmdaV6v0Group,
       "tmnxMDAMcPathMgmtV6v0Group": tmnxMDAMcPathMgmtV6v0Group,
       "tmnxCardV6v0NamedPoolPlcyGroup": tmnxCardV6v0NamedPoolPlcyGroup,
       "tmnxChassisNotifyObjsV6v0Group": tmnxChassisNotifyObjsV6v0Group,
       "tmnxChassisV6v1Group": tmnxChassisV6v1Group,
       "tmnxFPMcPathMgmtV6v1Group": tmnxFPMcPathMgmtV6v1Group,
       "tmnxMDAV6v1Group": tmnxMDAV6v1Group,
       "tmnxMDACcagV6v1Group": tmnxMDACcagV6v1Group,
       "tmnxMdaXplV5v0Group": tmnxMdaXplV5v0Group,
       "tmnxChassisNotifyObjsV5v0Group": tmnxChassisNotifyObjsV5v0Group,
       "tmnxChassisNotificationV5v0Group": tmnxChassisNotificationV5v0Group,
       "tmnxChassisNotificationV6v1Group": tmnxChassisNotificationV6v1Group,
       "tmnxChassisNotifyObjsV6v1Group": tmnxChassisNotifyObjsV6v1Group,
       "tmnxChassisNotificationV7v0Group": tmnxChassisNotificationV7v0Group,
       "tmnxChassisUserModV7v0Group": tmnxChassisUserModV7v0Group,
       "tmnxCardPchipV5v0Group": tmnxCardPchipV5v0Group,
       "tmnxFPWredV7v0Group": tmnxFPWredV7v0Group,
       "tmnxChassisV7v0Group": tmnxChassisV7v0Group,
       "tmnxIPsecV7v0Group": tmnxIPsecV7v0Group,
       "tmnxIPsecNotifV7v0Group": tmnxIPsecNotifV7v0Group,
       "tmnxSyncV6v0Group": tmnxSyncV6v0Group,
       "tmnxSyncIfTimingV8v0Group": tmnxSyncIfTimingV8v0Group,
       "tmnxSyncIfTimingNotifV8v0Group": tmnxSyncIfTimingNotifV8v0Group,
       "tmnxChassisV8v0Group": tmnxChassisV8v0Group,
       "tmnxChassisMixedModeIomV8v0Group": tmnxChassisMixedModeIomV8v0Group,
       "tmnxCardCamErrorV6v1Group": tmnxCardCamErrorV6v1Group,
       "tmnxChassisV6v0Group": tmnxChassisV6v0Group,
       "tmnxCardV7v0Group": tmnxCardV7v0Group,
       "tmnxAtmGroup": tmnxAtmGroup,
       "tmnxChassisHwV6v1Group": tmnxChassisHwV6v1Group,
       "tmnxChassisHwV9v0Group": tmnxChassisHwV9v0Group,
       "tmnxSyncIfTimingV9v0Group": tmnxSyncIfTimingV9v0Group,
       "tmnxSyncIfTimingNotifyV9v0Group": tmnxSyncIfTimingNotifyV9v0Group,
       "tmnxChassisNotifyObjsV9v0Group": tmnxChassisNotifyObjsV9v0Group,
       "tmnxMDAV9v0Group": tmnxMDAV9v0Group,
       "tmnxCardPchipV8v0Group": tmnxCardPchipV8v0Group,
       "tmnxChassisNotifyObjsV8v0Group": tmnxChassisNotifyObjsV8v0Group,
       "tmnxFPQGrpGroup": tmnxFPQGrpGroup,
       "tmnxCardV10v0Group": tmnxCardV10v0Group,
       "tmnxIpsecV10v0Group": tmnxIpsecV10v0Group,
       "tmnxChassisV10v0Group": tmnxChassisV10v0Group,
       "tmnxChassisNotificationV9v0Group": tmnxChassisNotificationV9v0Group,
       "tmnxFPQGrpV10v0R4Group": tmnxFPQGrpV10v0R4Group,
       "tmnxMdaV10v0Group": tmnxMdaV10v0Group,
       "tmnxMdaObsoletedV10v0Group": tmnxMdaObsoletedV10v0Group,
       "tmnxChassisNotifyV10v0Group": tmnxChassisNotifyV10v0Group,
       "tmnxMdaHsmdaPoolV10v0Group": tmnxMdaHsmdaPoolV10v0Group,
       "tmnxHwObjs": tmnxHwObjs,
       "tmnxChassisObjs": tmnxChassisObjs,
       "tmnxChassisTotalNumber": tmnxChassisTotalNumber,
       "tmnxChassisLastChange": tmnxChassisLastChange,
       "tmnxChassisTable": tmnxChassisTable,
       "tmnxChassisEntry": tmnxChassisEntry,
       "tmnxChassisIndex": tmnxChassisIndex,
       "tmnxChassisRowStatus": tmnxChassisRowStatus,
       "tmnxChassisName": tmnxChassisName,
       "tmnxChassisType": tmnxChassisType,
       "tmnxChassisLocation": tmnxChassisLocation,
       "tmnxChassisCoordinates": tmnxChassisCoordinates,
       "tmnxChassisNumSlots": tmnxChassisNumSlots,
       "tmnxChassisNumPorts": tmnxChassisNumPorts,
       "tmnxChassisNumPwrSupplies": tmnxChassisNumPwrSupplies,
       "tmnxChassisNumFanTrays": tmnxChassisNumFanTrays,
       "tmnxChassisNumFans": tmnxChassisNumFans,
       "tmnxChassisCriticalLEDState": tmnxChassisCriticalLEDState,
       "tmnxChassisMajorLEDState": tmnxChassisMajorLEDState,
       "tmnxChassisMinorLEDState": tmnxChassisMinorLEDState,
       "tmnxChassisBaseMacAddress": tmnxChassisBaseMacAddress,
       "tmnxChassisCLLICode": tmnxChassisCLLICode,
       "tmnxChassisReboot": tmnxChassisReboot,
       "tmnxChassisUpgrade": tmnxChassisUpgrade,
       "tmnxChassisAdminMode": tmnxChassisAdminMode,
       "tmnxChassisOperMode": tmnxChassisOperMode,
       "tmnxChassisModeForce": tmnxChassisModeForce,
       "tmnxChassisUpdateWaitTime": tmnxChassisUpdateWaitTime,
       "tmnxChassisUpdateTimeLeft": tmnxChassisUpdateTimeLeft,
       "tmnxChassisOverTempState": tmnxChassisOverTempState,
       "tmnxChassisMixedModeIomAdminMode": tmnxChassisMixedModeIomAdminMode,
       "tmnxChassisMixedModeIomUpgrList": tmnxChassisMixedModeIomUpgrList,
       "tmnxChassisRedForcedSingleSfm": tmnxChassisRedForcedSingleSfm,
       "tmnxChassisFanTable": tmnxChassisFanTable,
       "tmnxChassisFanEntry": tmnxChassisFanEntry,
       "tmnxChassisFanIndex": tmnxChassisFanIndex,
       "tmnxChassisFanOperStatus": tmnxChassisFanOperStatus,
       "tmnxChassisFanSpeed": tmnxChassisFanSpeed,
       "tmnxChassisFanRevision": tmnxChassisFanRevision,
       "tmnxChassisPowerSupplyTable": tmnxChassisPowerSupplyTable,
       "tmnxChassisPowerSupplyEntry": tmnxChassisPowerSupplyEntry,
       "tmnxChassisPowerSupplyId": tmnxChassisPowerSupplyId,
       "tmnxChassisPowerSupplyACStatus": tmnxChassisPowerSupplyACStatus,
       "tmnxChassisPowerSupplyDCStatus": tmnxChassisPowerSupplyDCStatus,
       "tmnxChassisPowerSupplyTempStatus": tmnxChassisPowerSupplyTempStatus,
       "tmnxChassisPowerSupplyTempThreshold": tmnxChassisPowerSupplyTempThreshold,
       "tmnxChassisPowerSupply1Status": tmnxChassisPowerSupply1Status,
       "tmnxChassisPowerSupply2Status": tmnxChassisPowerSupply2Status,
       "tmnxChassisPowerSupplyAssignedType": tmnxChassisPowerSupplyAssignedType,
       "tmnxChassisPowerSupplyInputStatus": tmnxChassisPowerSupplyInputStatus,
       "tmnxChassisPowerSupplyOutputStatus": tmnxChassisPowerSupplyOutputStatus,
       "tmnxChassisPowerSupplyPemType": tmnxChassisPowerSupplyPemType,
       "tmnxChassisTypeTable": tmnxChassisTypeTable,
       "tmnxChassisTypeEntry": tmnxChassisTypeEntry,
       "tmnxChassisTypeIndex": tmnxChassisTypeIndex,
       "tmnxChassisTypeName": tmnxChassisTypeName,
       "tmnxChassisTypeDescription": tmnxChassisTypeDescription,
       "tmnxChassisTypeStatus": tmnxChassisTypeStatus,
       "tmnxHwLastChange": tmnxHwLastChange,
       "tmnxHwTable": tmnxHwTable,
       "tmnxHwEntry": tmnxHwEntry,
       "tmnxHwIndex": tmnxHwIndex,
       "tmnxHwID": tmnxHwID,
       "tmnxHwMfgString": tmnxHwMfgString,
       "tmnxHwMfgBoardNumber": tmnxHwMfgBoardNumber,
       "tmnxHwSerialNumber": tmnxHwSerialNumber,
       "tmnxHwManufactureDate": tmnxHwManufactureDate,
       "tmnxHwClass": tmnxHwClass,
       "tmnxHwName": tmnxHwName,
       "tmnxHwAlias": tmnxHwAlias,
       "tmnxHwAssetID": tmnxHwAssetID,
       "tmnxHwCLEI": tmnxHwCLEI,
       "tmnxHwIsFRU": tmnxHwIsFRU,
       "tmnxHwContainedIn": tmnxHwContainedIn,
       "tmnxHwParentRelPos": tmnxHwParentRelPos,
       "tmnxHwAdminState": tmnxHwAdminState,
       "tmnxHwOperState": tmnxHwOperState,
       "tmnxHwTempSensor": tmnxHwTempSensor,
       "tmnxHwTemperature": tmnxHwTemperature,
       "tmnxHwTempThreshold": tmnxHwTempThreshold,
       "tmnxHwBootCodeVersion": tmnxHwBootCodeVersion,
       "tmnxHwSoftwareCodeVersion": tmnxHwSoftwareCodeVersion,
       "tmnxHwSwLastBoot": tmnxHwSwLastBoot,
       "tmnxHwSwState": tmnxHwSwState,
       "tmnxHwAlarmState": tmnxHwAlarmState,
       "tmnxHwLastAlarmEvent": tmnxHwLastAlarmEvent,
       "tmnxHwClearAlarms": tmnxHwClearAlarms,
       "tmnxHwSwImageSource": tmnxHwSwImageSource,
       "tmnxHwMfgDeviations": tmnxHwMfgDeviations,
       "tmnxHwBaseMacAddress": tmnxHwBaseMacAddress,
       "tmnxHwFailureReason": tmnxHwFailureReason,
       "tmnxHwEquippedPlatform": tmnxHwEquippedPlatform,
       "tmnxHwMfgAssemblyNumber": tmnxHwMfgAssemblyNumber,
       "tmnxHwFirmwareCodeVersion": tmnxHwFirmwareCodeVersion,
       "tmnxHwContainsTable": tmnxHwContainsTable,
       "tmnxHwContainsEntry": tmnxHwContainsEntry,
       "tmnxHwContainedIndex": tmnxHwContainedIndex,
       "tmnxCcmTable": tmnxCcmTable,
       "tmnxCcmEntry": tmnxCcmEntry,
       "tmnxCcmIndex": tmnxCcmIndex,
       "tmnxCcmOperStatus": tmnxCcmOperStatus,
       "tmnxCcmHwIndex": tmnxCcmHwIndex,
       "tmnxCcmEquippedType": tmnxCcmEquippedType,
       "tmnxCcmTypeTable": tmnxCcmTypeTable,
       "tmnxCcmTypeEntry": tmnxCcmTypeEntry,
       "tmnxCcmTypeIndex": tmnxCcmTypeIndex,
       "tmnxCcmTypeName": tmnxCcmTypeName,
       "tmnxCcmTypeDescription": tmnxCcmTypeDescription,
       "tmnxCcmTypeStatus": tmnxCcmTypeStatus,
       "tmnxFanTrayComponentTable": tmnxFanTrayComponentTable,
       "tmnxFanTrayComponentEntry": tmnxFanTrayComponentEntry,
       "tmnxFanTrayCompIndex": tmnxFanTrayCompIndex,
       "tmnxFanTrayCompSpeed": tmnxFanTrayCompSpeed,
       "tmnxHwResourceTable": tmnxHwResourceTable,
       "tmnxHwResourceEntry": tmnxHwResourceEntry,
       "tmnxHwResourceCurrentVoltage": tmnxHwResourceCurrentVoltage,
       "tmnxHwResourcePeakVoltage": tmnxHwResourcePeakVoltage,
       "tmnxHwResourcePeakVoltageTime": tmnxHwResourcePeakVoltageTime,
       "tmnxHwResourceMinVoltage": tmnxHwResourceMinVoltage,
       "tmnxHwResourceMinVoltageTime": tmnxHwResourceMinVoltageTime,
       "tmnxHwResourceCurrentWattage": tmnxHwResourceCurrentWattage,
       "tmnxHwResourcePeakWattage": tmnxHwResourcePeakWattage,
       "tmnxHwResourcePeakWattageTime": tmnxHwResourcePeakWattageTime,
       "tmnxHwResourceMinWattage": tmnxHwResourceMinWattage,
       "tmnxHwResourceMinWattageTime": tmnxHwResourceMinWattageTime,
       "tmnxHwResourceCurrentAmperage": tmnxHwResourceCurrentAmperage,
       "tmnxHwResourcePeakAmperage": tmnxHwResourcePeakAmperage,
       "tmnxHwResourcePeakAmperageTime": tmnxHwResourcePeakAmperageTime,
       "tmnxHwResourceMinAmperage": tmnxHwResourceMinAmperage,
       "tmnxHwResourceMinAmperageTime": tmnxHwResourceMinAmperageTime,
       "tmnxSlotObjs": tmnxSlotObjs,
       "tmnxCardObjs": tmnxCardObjs,
       "tmnxCardLastChange": tmnxCardLastChange,
       "tmnxCardTable": tmnxCardTable,
       "tmnxCardEntry": tmnxCardEntry,
       "tmnxCardSlotNum": tmnxCardSlotNum,
       "tmnxCardSupportedTypes": tmnxCardSupportedTypes,
       "tmnxCardAllowedTypes": tmnxCardAllowedTypes,
       "tmnxCardAssignedType": tmnxCardAssignedType,
       "tmnxCardEquippedType": tmnxCardEquippedType,
       "tmnxCardHwIndex": tmnxCardHwIndex,
       "tmnxCardClockSource": tmnxCardClockSource,
       "tmnxCardNumMdaSlots": tmnxCardNumMdaSlots,
       "tmnxCardNumMdas": tmnxCardNumMdas,
       "tmnxCardReboot": tmnxCardReboot,
       "tmnxCardMemorySize": tmnxCardMemorySize,
       "tmnxCardNamedPoolAdminMode": tmnxCardNamedPoolAdminMode,
       "tmnxCardNamedPoolOperMode": tmnxCardNamedPoolOperMode,
       "tmnxCardSoftReset": tmnxCardSoftReset,
       "tmnxCardLastBootupReason": tmnxCardLastBootupReason,
       "tmnxCardCmplx1IngrFcsOccur": tmnxCardCmplx1IngrFcsOccur,
       "tmnxCardCmplx1IngrFcsOccurTime": tmnxCardCmplx1IngrFcsOccurTime,
       "tmnxCardCmplx1EgrFcsOccur": tmnxCardCmplx1EgrFcsOccur,
       "tmnxCardCmplx1EgrFcsOccurTime": tmnxCardCmplx1EgrFcsOccurTime,
       "tmnxCardCmplx2IngrFcsOccur": tmnxCardCmplx2IngrFcsOccur,
       "tmnxCardCmplx2IngrFcsOccurTime": tmnxCardCmplx2IngrFcsOccurTime,
       "tmnxCardCmplx2EgrFcsOccur": tmnxCardCmplx2EgrFcsOccur,
       "tmnxCardCmplx2EgrFcsOccurTime": tmnxCardCmplx2EgrFcsOccurTime,
       "tmnxCardCmplx1MemParityOccur": tmnxCardCmplx1MemParityOccur,
       "tmnxCardCmplx1MemParityOccurTime": tmnxCardCmplx1MemParityOccurTime,
       "tmnxCardCmplx2MemParityOccur": tmnxCardCmplx2MemParityOccur,
       "tmnxCardCmplx2MemParityOccurTime": tmnxCardCmplx2MemParityOccurTime,
       "tmnxCardCapability": tmnxCardCapability,
       "tmnxCardCmplx1CAMErrorOccur": tmnxCardCmplx1CAMErrorOccur,
       "tmnxCardCmplx1CAMErrorOccurTime": tmnxCardCmplx1CAMErrorOccurTime,
       "tmnxCardCmplx2CAMErrorOccur": tmnxCardCmplx2CAMErrorOccur,
       "tmnxCardCmplx2CAMErrorOccurTime": tmnxCardCmplx2CAMErrorOccurTime,
       "tmnxCardFailOnError": tmnxCardFailOnError,
       "tmnxCardCmplx1EgrFcsSrcSlots": tmnxCardCmplx1EgrFcsSrcSlots,
       "tmnxCardCmplx2EgrFcsSrcSlots": tmnxCardCmplx2EgrFcsSrcSlots,
       "tmnxCardHardResetUnsupMdas": tmnxCardHardResetUnsupMdas,
       "tmnxCpmCardLastChange": tmnxCpmCardLastChange,
       "tmnxCpmCardTable": tmnxCpmCardTable,
       "tmnxCpmCardEntry": tmnxCpmCardEntry,
       "tmnxCpmCardSlotNum": tmnxCpmCardSlotNum,
       "tmnxCpmCardNum": tmnxCpmCardNum,
       "tmnxCpmCardSupportedTypes": tmnxCpmCardSupportedTypes,
       "tmnxCpmCardAllowedTypes": tmnxCpmCardAllowedTypes,
       "tmnxCpmCardAssignedType": tmnxCpmCardAssignedType,
       "tmnxCpmCardEquippedType": tmnxCpmCardEquippedType,
       "tmnxCpmCardHwIndex": tmnxCpmCardHwIndex,
       "tmnxCpmCardBootOptionVersion": tmnxCpmCardBootOptionVersion,
       "tmnxCpmCardBootOptionLastModified": tmnxCpmCardBootOptionLastModified,
       "tmnxCpmCardConfigBootedVersion": tmnxCpmCardConfigBootedVersion,
       "tmnxCpmCardIndexBootedVersion": tmnxCpmCardIndexBootedVersion,
       "tmnxCpmCardConfigLastModified": tmnxCpmCardConfigLastModified,
       "tmnxCpmCardConfigLastSaved": tmnxCpmCardConfigLastSaved,
       "tmnxCpmCardRedundant": tmnxCpmCardRedundant,
       "tmnxCpmCardClockSource": tmnxCpmCardClockSource,
       "tmnxCpmCardNumCpus": tmnxCpmCardNumCpus,
       "tmnxCpmCardCpuType": tmnxCpmCardCpuType,
       "tmnxCpmCardMemorySize": tmnxCpmCardMemorySize,
       "tmnxCpmCardSwitchToRedundantCard": tmnxCpmCardSwitchToRedundantCard,
       "tmnxCpmCardReboot": tmnxCpmCardReboot,
       "tmnxCpmCardRereadBootOptions": tmnxCpmCardRereadBootOptions,
       "tmnxCpmCardConfigFileLastBooted": tmnxCpmCardConfigFileLastBooted,
       "tmnxCpmCardConfigFileLastSaved": tmnxCpmCardConfigFileLastSaved,
       "tmnxCpmCardConfigFileLastBootedHeader": tmnxCpmCardConfigFileLastBootedHeader,
       "tmnxCpmCardIndexFileLastBootedHeader": tmnxCpmCardIndexFileLastBootedHeader,
       "tmnxCpmCardBootOptionSource": tmnxCpmCardBootOptionSource,
       "tmnxCpmCardConfigSource": tmnxCpmCardConfigSource,
       "tmnxCpmCardBootOptionLastSaved": tmnxCpmCardBootOptionLastSaved,
       "tmnxCpmCardMasterSlaveRefState": tmnxCpmCardMasterSlaveRefState,
       "tmnxCpmCardConfigUserLastModified": tmnxCpmCardConfigUserLastModified,
       "tmnxCpmCardCmplxCAMErrOccur": tmnxCpmCardCmplxCAMErrOccur,
       "tmnxCpmCardCmplxCAMErrOccurTime": tmnxCpmCardCmplxCAMErrOccurTime,
       "tmnxCpmCardOscillatorType": tmnxCpmCardOscillatorType,
       "tmnxFabricLastChange": tmnxFabricLastChange,
       "tmnxFabricTable": tmnxFabricTable,
       "tmnxFabricEntry": tmnxFabricEntry,
       "tmnxFabricSlotNum": tmnxFabricSlotNum,
       "tmnxFabricAssignedType": tmnxFabricAssignedType,
       "tmnxFabricEquippedType": tmnxFabricEquippedType,
       "tmnxFabricHwIndex": tmnxFabricHwIndex,
       "tmnxFabricSupportedTypes": tmnxFabricSupportedTypes,
       "tmnxFabricReboot": tmnxFabricReboot,
       "tmnxCpmFlashTable": tmnxCpmFlashTable,
       "tmnxCpmFlashEntry": tmnxCpmFlashEntry,
       "tmnxCpmFlashId": tmnxCpmFlashId,
       "tmnxCpmFlashOperStatus": tmnxCpmFlashOperStatus,
       "tmnxCpmFlashSerialNumber": tmnxCpmFlashSerialNumber,
       "tmnxCpmFlashFirmwareRevision": tmnxCpmFlashFirmwareRevision,
       "tmnxCpmFlashModelNumber": tmnxCpmFlashModelNumber,
       "tmnxCpmFlashCapacity": tmnxCpmFlashCapacity,
       "tmnxCpmFlashUsed": tmnxCpmFlashUsed,
       "tmnxCpmFlashHwIndex": tmnxCpmFlashHwIndex,
       "tmnxMDATable": tmnxMDATable,
       "tmnxMDAEntry": tmnxMDAEntry,
       "tmnxMDASlotNum": tmnxMDASlotNum,
       "tmnxMDASupportedTypes": tmnxMDASupportedTypes,
       "tmnxMDAAllowedTypes": tmnxMDAAllowedTypes,
       "tmnxMDAAssignedType": tmnxMDAAssignedType,
       "tmnxMDAEquippedType": tmnxMDAEquippedType,
       "tmnxMDAHwIndex": tmnxMDAHwIndex,
       "tmnxMDAMaxPorts": tmnxMDAMaxPorts,
       "tmnxMDAEquippedPorts": tmnxMDAEquippedPorts,
       "tmnxMDATxTimingSelected": tmnxMDATxTimingSelected,
       "tmnxMDASyncIfTimingStatus": tmnxMDASyncIfTimingStatus,
       "tmnxMDANetworkIngQueues": tmnxMDANetworkIngQueues,
       "tmnxMDACapabilities": tmnxMDACapabilities,
       "tmnxMDAMinChannelization": tmnxMDAMinChannelization,
       "tmnxMDAMaxChannelization": tmnxMDAMaxChannelization,
       "tmnxMDAMaxChannels": tmnxMDAMaxChannels,
       "tmnxMDAChannelsInUse": tmnxMDAChannelsInUse,
       "tmnxMDACcagId": tmnxMDACcagId,
       "tmnxMDAReboot": tmnxMDAReboot,
       "tmnxMDAHiBwMcastSource": tmnxMDAHiBwMcastSource,
       "tmnxMDAHiBwMcastAlarm": tmnxMDAHiBwMcastAlarm,
       "tmnxMDAHiBwMcastTapCount": tmnxMDAHiBwMcastTapCount,
       "tmnxMDAHiBwMcastGroup": tmnxMDAHiBwMcastGroup,
       "tmnxMDAClockMode": tmnxMDAClockMode,
       "tmnxMDADiffTimestampFreq": tmnxMDADiffTimestampFreq,
       "tmnxMDAIngHsmdaSchedPolicy": tmnxMDAIngHsmdaSchedPolicy,
       "tmnxMDAMcPathMgmtBwPlcyName": tmnxMDAMcPathMgmtBwPlcyName,
       "tmnxMDAMcPathMgmtPriPathLimit": tmnxMDAMcPathMgmtPriPathLimit,
       "tmnxMDAMcPathMgmtSecPathLimit": tmnxMDAMcPathMgmtSecPathLimit,
       "tmnxMDAMcPathMgmtAncPathLimit": tmnxMDAMcPathMgmtAncPathLimit,
       "tmnxMDAMcPathMgmtAdminState": tmnxMDAMcPathMgmtAdminState,
       "tmnxMDAIngNamedPoolPolicy": tmnxMDAIngNamedPoolPolicy,
       "tmnxMDAEgrNamedPoolPolicy": tmnxMDAEgrNamedPoolPolicy,
       "tmnxMDAIngHsmdaPoolPolicy": tmnxMDAIngHsmdaPoolPolicy,
       "tmnxMDAEgrHsmdaPoolPolicy": tmnxMDAEgrHsmdaPoolPolicy,
       "tmnxMDAMcPathMgmtPriInUseBw": tmnxMDAMcPathMgmtPriInUseBw,
       "tmnxMDAMcPathMgmtSecInUseBw": tmnxMDAMcPathMgmtSecInUseBw,
       "tmnxMDAMcPathMgmtAncInUseBw": tmnxMDAMcPathMgmtAncInUseBw,
       "tmnxMDAMcPathMgmtBlkHoleInUseBw": tmnxMDAMcPathMgmtBlkHoleInUseBw,
       "tmnxMDASynchronousEthernet": tmnxMDASynchronousEthernet,
       "tmnxMDAXplErrorTime": tmnxMDAXplErrorTime,
       "tmnxMDAXplFailedCount": tmnxMDAXplFailedCount,
       "tmnxMDAAtmMode": tmnxMDAAtmMode,
       "tmnxMDAEgrHsmdaThrshLoBrstMult": tmnxMDAEgrHsmdaThrshLoBrstMult,
       "tmnxMDAEgrHsmdaThrshHiBrstInc": tmnxMDAEgrHsmdaThrshHiBrstInc,
       "tmnxMDAIsaTunnelGroup": tmnxMDAIsaTunnelGroup,
       "tmnxMDAIsaTunnelGroupInUse": tmnxMDAIsaTunnelGroupInUse,
       "tmnxCardTypeTable": tmnxCardTypeTable,
       "tmnxCardTypeEntry": tmnxCardTypeEntry,
       "tmnxCardTypeIndex": tmnxCardTypeIndex,
       "tmnxCardTypeName": tmnxCardTypeName,
       "tmnxCardTypeDescription": tmnxCardTypeDescription,
       "tmnxCardTypeStatus": tmnxCardTypeStatus,
       "tmnxMdaTypeTable": tmnxMdaTypeTable,
       "tmnxMdaTypeEntry": tmnxMdaTypeEntry,
       "tmnxMdaTypeIndex": tmnxMdaTypeIndex,
       "tmnxMdaTypeName": tmnxMdaTypeName,
       "tmnxMdaTypeDescription": tmnxMdaTypeDescription,
       "tmnxMdaTypeStatus": tmnxMdaTypeStatus,
       "tmnxSyncIfTimingTable": tmnxSyncIfTimingTable,
       "tmnxSyncIfTimingEntry": tmnxSyncIfTimingEntry,
       "tmnxSyncIfTimingRevert": tmnxSyncIfTimingRevert,
       "tmnxSyncIfTimingRefOrder1": tmnxSyncIfTimingRefOrder1,
       "tmnxSyncIfTimingRefOrder2": tmnxSyncIfTimingRefOrder2,
       "tmnxSyncIfTimingRef1SrcPort": tmnxSyncIfTimingRef1SrcPort,
       "tmnxSyncIfTimingRef1AdminStatus": tmnxSyncIfTimingRef1AdminStatus,
       "tmnxSyncIfTimingRef1InUse": tmnxSyncIfTimingRef1InUse,
       "tmnxSyncIfTimingRef1Qualified": tmnxSyncIfTimingRef1Qualified,
       "tmnxSyncIfTimingRef1Alarm": tmnxSyncIfTimingRef1Alarm,
       "tmnxSyncIfTimingRef2SrcPort": tmnxSyncIfTimingRef2SrcPort,
       "tmnxSyncIfTimingRef2AdminStatus": tmnxSyncIfTimingRef2AdminStatus,
       "tmnxSyncIfTimingRef2InUse": tmnxSyncIfTimingRef2InUse,
       "tmnxSyncIfTimingRef2Qualified": tmnxSyncIfTimingRef2Qualified,
       "tmnxSyncIfTimingRef2Alarm": tmnxSyncIfTimingRef2Alarm,
       "tmnxSyncIfTimingFreqOffset": tmnxSyncIfTimingFreqOffset,
       "tmnxSyncIfTimingStatus": tmnxSyncIfTimingStatus,
       "tmnxSyncIfTimingRefOrder3": tmnxSyncIfTimingRefOrder3,
       "tmnxSyncIfTimingBITSIfType": tmnxSyncIfTimingBITSIfType,
       "tmnxSyncIfTimingBITSAdminStatus": tmnxSyncIfTimingBITSAdminStatus,
       "tmnxSyncIfTimingBITSInUse": tmnxSyncIfTimingBITSInUse,
       "tmnxSyncIfTimingBITSQualified": tmnxSyncIfTimingBITSQualified,
       "tmnxSyncIfTimingBITSAlarm": tmnxSyncIfTimingBITSAlarm,
       "tmnxSyncIfTimingRef1SrcHw": tmnxSyncIfTimingRef1SrcHw,
       "tmnxSyncIfTimingRef1BITSIfType": tmnxSyncIfTimingRef1BITSIfType,
       "tmnxSyncIfTimingRef2SrcHw": tmnxSyncIfTimingRef2SrcHw,
       "tmnxSyncIfTimingRef2BITSIfType": tmnxSyncIfTimingRef2BITSIfType,
       "tmnxSyncIfTimingBITSOutAdmStatus": tmnxSyncIfTimingBITSOutAdmStatus,
       "tmnxSyncIfTimingBITSOutLineLen": tmnxSyncIfTimingBITSOutLineLen,
       "tmnxSyncIfTimingRef1CfgQltyLevel": tmnxSyncIfTimingRef1CfgQltyLevel,
       "tmnxSyncIfTimingRef1RxQltyLevel": tmnxSyncIfTimingRef1RxQltyLevel,
       "tmnxSyncIfTimingRef2CfgQltyLevel": tmnxSyncIfTimingRef2CfgQltyLevel,
       "tmnxSyncIfTimingRef2RxQltyLevel": tmnxSyncIfTimingRef2RxQltyLevel,
       "tmnxSyncIfTimingBITSCfgQltyLevel": tmnxSyncIfTimingBITSCfgQltyLevel,
       "tmnxSyncIfTimingBITSRxQltyLevel": tmnxSyncIfTimingBITSRxQltyLevel,
       "tmnxSyncIfTimingBITS2InUse": tmnxSyncIfTimingBITS2InUse,
       "tmnxSyncIfTimingBITS2Qualified": tmnxSyncIfTimingBITS2Qualified,
       "tmnxSyncIfTimingBITS2Alarm": tmnxSyncIfTimingBITS2Alarm,
       "tmnxSyncIfTimingBITS2RxQltyLevel": tmnxSyncIfTimingBITS2RxQltyLevel,
       "tmnxSyncIfTimingRef1State": tmnxSyncIfTimingRef1State,
       "tmnxSyncIfTimingRef2State": tmnxSyncIfTimingRef2State,
       "tmnxSyncIfTimingBITSState": tmnxSyncIfTimingBITSState,
       "tmnxSyncIfTimingBITS2State": tmnxSyncIfTimingBITS2State,
       "tmnxSyncIfTimingRef1NationalUse": tmnxSyncIfTimingRef1NationalUse,
       "tmnxSyncIfTimingRef2NationalUse": tmnxSyncIfTimingRef2NationalUse,
       "tmnxSyncIfTimingBITSNationalUse": tmnxSyncIfTimingBITSNationalUse,
       "tmnxSyncIfTimingQLSelection": tmnxSyncIfTimingQLSelection,
       "tmnxSyncIfTimingOtherCPMInUse": tmnxSyncIfTimingOtherCPMInUse,
       "tmnxSyncIfTimingOtherCPMQual": tmnxSyncIfTimingOtherCPMQual,
       "tmnxSyncIfTimingOtherCPMAlarm": tmnxSyncIfTimingOtherCPMAlarm,
       "tmnxSyncIfTimingOtherCPMState": tmnxSyncIfTimingOtherCPMState,
       "tmnxSyncIfTimingBITSOutRefSel": tmnxSyncIfTimingBITSOutRefSel,
       "tmnxSyncIfTimingBITSTxQltyLevel": tmnxSyncIfTimingBITSTxQltyLevel,
       "tmnxSyncIfTimingBITS2AdminStatus": tmnxSyncIfTimingBITS2AdminStatus,
       "tmnxSyncIfTimingSystemQltyLevel": tmnxSyncIfTimingSystemQltyLevel,
       "tmnxSyncIfTimingRefOrder4": tmnxSyncIfTimingRefOrder4,
       "tmnxSyncIfTimingPTPAdminStatus": tmnxSyncIfTimingPTPAdminStatus,
       "tmnxSyncIfTimingPTPInUse": tmnxSyncIfTimingPTPInUse,
       "tmnxSyncIfTimingPTPQualified": tmnxSyncIfTimingPTPQualified,
       "tmnxSyncIfTimingPTPAlarm": tmnxSyncIfTimingPTPAlarm,
       "tmnxSyncIfTimingPTPCfgQltyLevel": tmnxSyncIfTimingPTPCfgQltyLevel,
       "tmnxSyncIfTimingPTPRxQltyLevel": tmnxSyncIfTimingPTPRxQltyLevel,
       "tmnxSyncIfTimingPTPState": tmnxSyncIfTimingPTPState,
       "tmnxSyncIfTimingBITSOutSource": tmnxSyncIfTimingBITSOutSource,
       "tmnxSyncIfTimingRefOrder5": tmnxSyncIfTimingRefOrder5,
       "tmnxSyncIfTimingBITS2InAdminStatus": tmnxSyncIfTimingBITS2InAdminStatus,
       "tmnxSyncIfTimingBITS2OutAdminStatus": tmnxSyncIfTimingBITS2OutAdminStatus,
       "tmnxSyncIfTimingBITS2TxQltyLevel": tmnxSyncIfTimingBITS2TxQltyLevel,
       "tmnxCcagTable": tmnxCcagTable,
       "tmnxCcagEntry": tmnxCcagEntry,
       "tmnxCcagId": tmnxCcagId,
       "tmnxCcagRowStatus": tmnxCcagRowStatus,
       "tmnxCcagLastChanged": tmnxCcagLastChanged,
       "tmnxCcagDescription": tmnxCcagDescription,
       "tmnxCcagAdminStatus": tmnxCcagAdminStatus,
       "tmnxCcagOperStatus": tmnxCcagOperStatus,
       "tmnxCcagCcaRate": tmnxCcagCcaRate,
       "tmnxCcagAccessAdaptQos": tmnxCcagAccessAdaptQos,
       "tmnxCcagPathTable": tmnxCcagPathTable,
       "tmnxCcagPathEntry": tmnxCcagPathEntry,
       "tmnxCcagPathId": tmnxCcagPathId,
       "tmnxCcagPathLastChanged": tmnxCcagPathLastChanged,
       "tmnxCcagPathRate": tmnxCcagPathRate,
       "tmnxCcagPathRateOption": tmnxCcagPathRateOption,
       "tmnxCcagPathWeight": tmnxCcagPathWeight,
       "tmnxCcagPathCcTable": tmnxCcagPathCcTable,
       "tmnxCcagPathCcEntry": tmnxCcagPathCcEntry,
       "tmnxCcagPathCcType": tmnxCcagPathCcType,
       "tmnxCcagPathCcLastChanged": tmnxCcagPathCcLastChanged,
       "tmnxCcagPathCcEgrPoolResvCbs": tmnxCcagPathCcEgrPoolResvCbs,
       "tmnxCcagPathCcEgrPoolSlpPlcy": tmnxCcagPathCcEgrPoolSlpPlcy,
       "tmnxCcagPathCcIngPoolResvCbs": tmnxCcagPathCcIngPoolResvCbs,
       "tmnxCcagPathCcIngPoolSlpPlcy": tmnxCcagPathCcIngPoolSlpPlcy,
       "tmnxCcagPathCcAcctPolicyId": tmnxCcagPathCcAcctPolicyId,
       "tmnxCcagPathCcCollectStats": tmnxCcagPathCcCollectStats,
       "tmnxCcagPathCcQueuePlcy": tmnxCcagPathCcQueuePlcy,
       "tmnxCcagPathCcMac": tmnxCcagPathCcMac,
       "tmnxCcagPathCcMtu": tmnxCcagPathCcMtu,
       "tmnxCcagPathCcUserAssignedMac": tmnxCcagPathCcUserAssignedMac,
       "tmnxCcagPathCcHwMac": tmnxCcagPathCcHwMac,
       "tmnxMcmTable": tmnxMcmTable,
       "tmnxMcmEntry": tmnxMcmEntry,
       "tmnxMcmSlotNum": tmnxMcmSlotNum,
       "tmnxMcmSupportedTypes": tmnxMcmSupportedTypes,
       "tmnxMcmAssignedType": tmnxMcmAssignedType,
       "tmnxMcmEquippedType": tmnxMcmEquippedType,
       "tmnxMcmHwIndex": tmnxMcmHwIndex,
       "tmnxMcmTypeTable": tmnxMcmTypeTable,
       "tmnxMcmTypeEntry": tmnxMcmTypeEntry,
       "tmnxMcmTypeIndex": tmnxMcmTypeIndex,
       "tmnxMcmTypeName": tmnxMcmTypeName,
       "tmnxMcmTypeDescription": tmnxMcmTypeDescription,
       "tmnxMcmTypeStatus": tmnxMcmTypeStatus,
       "tmnxIPsecIsaGrpTableLastChanged": tmnxIPsecIsaGrpTableLastChanged,
       "tmnxIPsecIsaGrpTable": tmnxIPsecIsaGrpTable,
       "tmnxIPsecIsaGrpEntry": tmnxIPsecIsaGrpEntry,
       "tmnxIPsecIsaGrpId": tmnxIPsecIsaGrpId,
       "tmnxIPsecIsaGrpRowStatus": tmnxIPsecIsaGrpRowStatus,
       "tmnxIPsecIsaGrpLastChanged": tmnxIPsecIsaGrpLastChanged,
       "tmnxIPsecIsaGrpDescription": tmnxIPsecIsaGrpDescription,
       "tmnxIPsecIsaGrpAdminState": tmnxIPsecIsaGrpAdminState,
       "tmnxIPsecIsaGrpOperState": tmnxIPsecIsaGrpOperState,
       "tmnxIPsecIsaGrpIsaChassis": tmnxIPsecIsaGrpIsaChassis,
       "tmnxIPsecIsaGrpPrimaryIsa": tmnxIPsecIsaGrpPrimaryIsa,
       "tmnxIPsecIsaGrpBackupIsa": tmnxIPsecIsaGrpBackupIsa,
       "tmnxIPsecIsaGrpActiveIsa": tmnxIPsecIsaGrpActiveIsa,
       "tmnxIPsecIsaGrpTunnels": tmnxIPsecIsaGrpTunnels,
       "tmnxIPsecIsaGrpMaxTunnels": tmnxIPsecIsaGrpMaxTunnels,
       "tmnxIPsecIsaGrpTunnelReassembly": tmnxIPsecIsaGrpTunnelReassembly,
       "tmnxIPsecIsaGrpOperFlags": tmnxIPsecIsaGrpOperFlags,
       "tmnxIPsecIsaGrpMultiActive": tmnxIPsecIsaGrpMultiActive,
       "tmnxIPsecIsaGrpActiveMda": tmnxIPsecIsaGrpActiveMda,
       "tmnxIPsecIsaGrpIpTunnels": tmnxIPsecIsaGrpIpTunnels,
       "tmnxIPsecIsaGrpIpMaxTunnels": tmnxIPsecIsaGrpIpMaxTunnels,
       "tmnxHsmdaMdaSchOvrTblLastChangd": tmnxHsmdaMdaSchOvrTblLastChangd,
       "tmnxHsmdaMdaSchOvrTable": tmnxHsmdaMdaSchOvrTable,
       "tmnxHsmdaMdaSchOvrEntry": tmnxHsmdaMdaSchOvrEntry,
       "tmnxHsmdaMdaSchOvrRowStatus": tmnxHsmdaMdaSchOvrRowStatus,
       "tmnxHsmdaMdaSchOvrLastChanged": tmnxHsmdaMdaSchOvrLastChanged,
       "tmnxHsmdaMdaSchOvrMaxRate": tmnxHsmdaMdaSchOvrMaxRate,
       "tmnxHsmdaMdaSchOvrGrp1Rate": tmnxHsmdaMdaSchOvrGrp1Rate,
       "tmnxHsmdaMdaSchOvrGrp2Rate": tmnxHsmdaMdaSchOvrGrp2Rate,
       "tmnxHsmdaMdaSchOvrClass1Rate": tmnxHsmdaMdaSchOvrClass1Rate,
       "tmnxHsmdaMdaSchOvrClass1WtInGrp": tmnxHsmdaMdaSchOvrClass1WtInGrp,
       "tmnxHsmdaMdaSchOvrClass2Rate": tmnxHsmdaMdaSchOvrClass2Rate,
       "tmnxHsmdaMdaSchOvrClass2WtInGrp": tmnxHsmdaMdaSchOvrClass2WtInGrp,
       "tmnxHsmdaMdaSchOvrClass3Rate": tmnxHsmdaMdaSchOvrClass3Rate,
       "tmnxHsmdaMdaSchOvrClass3WtInGrp": tmnxHsmdaMdaSchOvrClass3WtInGrp,
       "tmnxHsmdaMdaSchOvrClass4Rate": tmnxHsmdaMdaSchOvrClass4Rate,
       "tmnxHsmdaMdaSchOvrClass4WtInGrp": tmnxHsmdaMdaSchOvrClass4WtInGrp,
       "tmnxHsmdaMdaSchOvrClass5Rate": tmnxHsmdaMdaSchOvrClass5Rate,
       "tmnxHsmdaMdaSchOvrClass5WtInGrp": tmnxHsmdaMdaSchOvrClass5WtInGrp,
       "tmnxHsmdaMdaSchOvrClass6Rate": tmnxHsmdaMdaSchOvrClass6Rate,
       "tmnxHsmdaMdaSchOvrClass6WtInGrp": tmnxHsmdaMdaSchOvrClass6WtInGrp,
       "tmnxHsmdaMdaSchOvrClass7Rate": tmnxHsmdaMdaSchOvrClass7Rate,
       "tmnxHsmdaMdaSchOvrClass7WtInGrp": tmnxHsmdaMdaSchOvrClass7WtInGrp,
       "tmnxHsmdaMdaSchOvrClass8Rate": tmnxHsmdaMdaSchOvrClass8Rate,
       "tmnxHsmdaMdaSchOvrClass8WtInGrp": tmnxHsmdaMdaSchOvrClass8WtInGrp,
       "tmnxFPTable": tmnxFPTable,
       "tmnxFPEntry": tmnxFPEntry,
       "tmnxFPNum": tmnxFPNum,
       "tmnxFPMcPathMgmtBwPlcyName": tmnxFPMcPathMgmtBwPlcyName,
       "tmnxFPMcPathMgmtAdminState": tmnxFPMcPathMgmtAdminState,
       "tmnxFPLastChanged": tmnxFPLastChanged,
       "tmnxFPHiBwMcastSource": tmnxFPHiBwMcastSource,
       "tmnxFPHiBwMcastAlarm": tmnxFPHiBwMcastAlarm,
       "tmnxFPHiBwMcastTapCount": tmnxFPHiBwMcastTapCount,
       "tmnxFPHiBwMcastGroup": tmnxFPHiBwMcastGroup,
       "tmnxFPWredBufAllocMin": tmnxFPWredBufAllocMin,
       "tmnxFPWredBufAllocMax": tmnxFPWredBufAllocMax,
       "tmnxFPWredResvCbsMin": tmnxFPWredResvCbsMin,
       "tmnxFPWredResvCbsMax": tmnxFPWredResvCbsMax,
       "tmnxFPWredSlopePolicy": tmnxFPWredSlopePolicy,
       "tmnxFPWredAdminState": tmnxFPWredAdminState,
       "tmnxFPHiBwMcastDefaultPathsOnly": tmnxFPHiBwMcastDefaultPathsOnly,
       "tmnxFPAccIngQGrpTableLastChgd": tmnxFPAccIngQGrpTableLastChgd,
       "tmnxFPAccIngQGrpTable": tmnxFPAccIngQGrpTable,
       "tmnxFPAccIngQGrpEntry": tmnxFPAccIngQGrpEntry,
       "tmnxFPAccIngQGrpName": tmnxFPAccIngQGrpName,
       "tmnxFPAccIngQGrpInstanceId": tmnxFPAccIngQGrpInstanceId,
       "tmnxFPAccIngQGrpRowStatus": tmnxFPAccIngQGrpRowStatus,
       "tmnxFPAccIngQGrpLastChgd": tmnxFPAccIngQGrpLastChgd,
       "tmnxFPAccIngQGrpAcctgPolId": tmnxFPAccIngQGrpAcctgPolId,
       "tmnxFPAccIngQGrpCollectStats": tmnxFPAccIngQGrpCollectStats,
       "tmnxFPAccIngQGrpDescr": tmnxFPAccIngQGrpDescr,
       "tmnxFPAccIngQGrpPolicerPol": tmnxFPAccIngQGrpPolicerPol,
       "tmnxFPNetIngQGrpTableLastChgd": tmnxFPNetIngQGrpTableLastChgd,
       "tmnxFPNetIngQGrpTable": tmnxFPNetIngQGrpTable,
       "tmnxFPNetIngQGrpEntry": tmnxFPNetIngQGrpEntry,
       "tmnxFPNetIngQGrpName": tmnxFPNetIngQGrpName,
       "tmnxFPNetIngQGrpInstanceId": tmnxFPNetIngQGrpInstanceId,
       "tmnxFPNetIngQGrpRowStatus": tmnxFPNetIngQGrpRowStatus,
       "tmnxFPNetIngQGrpLastChgd": tmnxFPNetIngQGrpLastChgd,
       "tmnxFPNetIngQGrpAcctgPolId": tmnxFPNetIngQGrpAcctgPolId,
       "tmnxFPNetIngQGrpCollectStats": tmnxFPNetIngQGrpCollectStats,
       "tmnxFPNetIngQGrpDescr": tmnxFPNetIngQGrpDescr,
       "tmnxFPNetIngQGrpPolicerPol": tmnxFPNetIngQGrpPolicerPol,
       "tmnxFabricTypeTable": tmnxFabricTypeTable,
       "tmnxFabricTypeEntry": tmnxFabricTypeEntry,
       "tmnxFabricTypeIndex": tmnxFabricTypeIndex,
       "tmnxFabricTypeName": tmnxFabricTypeName,
       "tmnxFabricTypeDescription": tmnxFabricTypeDescription,
       "tmnxFabricTypeStatus": tmnxFabricTypeStatus,
       "tmnxFPNetIngQGrpPStatTable": tmnxFPNetIngQGrpPStatTable,
       "tmnxFPNetIngQGrpPStatEntry": tmnxFPNetIngQGrpPStatEntry,
       "tmnxFPNetIngQGrpPStatPolicerId": tmnxFPNetIngQGrpPStatPolicerId,
       "tmnxFPNetIngQGrpPStatMode": tmnxFPNetIngQGrpPStatMode,
       "tmnxFPNetIngQgPStOffHPrioPkts": tmnxFPNetIngQgPStOffHPrioPkts,
       "tmnxFPNetIngQgPStOffHPrioPktsL": tmnxFPNetIngQgPStOffHPrioPktsL,
       "tmnxFPNetIngQgPStOffHPrioPktsH": tmnxFPNetIngQgPStOffHPrioPktsH,
       "tmnxFPNetIngQgPStDrpHPrioPkts": tmnxFPNetIngQgPStDrpHPrioPkts,
       "tmnxFPNetIngQgPStDrpHPrioPktsL": tmnxFPNetIngQgPStDrpHPrioPktsL,
       "tmnxFPNetIngQgPStDrpHPrioPktsH": tmnxFPNetIngQgPStDrpHPrioPktsH,
       "tmnxFPNetIngQgPStOffLPrioPkts": tmnxFPNetIngQgPStOffLPrioPkts,
       "tmnxFPNetIngQgPStOffLPrioPktsL": tmnxFPNetIngQgPStOffLPrioPktsL,
       "tmnxFPNetIngQgPStOffLPrioPktsH": tmnxFPNetIngQgPStOffLPrioPktsH,
       "tmnxFPNetIngQgPStDrpLPrioPkts": tmnxFPNetIngQgPStDrpLPrioPkts,
       "tmnxFPNetIngQgPStDrpLPrioPktsL": tmnxFPNetIngQgPStDrpLPrioPktsL,
       "tmnxFPNetIngQgPStDrpLPrioPktsH": tmnxFPNetIngQgPStDrpLPrioPktsH,
       "tmnxFPNetIngQgPStOffHPrioOcts": tmnxFPNetIngQgPStOffHPrioOcts,
       "tmnxFPNetIngQgPStOffHPrioOctsL": tmnxFPNetIngQgPStOffHPrioOctsL,
       "tmnxFPNetIngQgPStOffHPrioOctsH": tmnxFPNetIngQgPStOffHPrioOctsH,
       "tmnxFPNetIngQgPStDrpHPrioOcts": tmnxFPNetIngQgPStDrpHPrioOcts,
       "tmnxFPNetIngQgPStDrpHPrioOctsL": tmnxFPNetIngQgPStDrpHPrioOctsL,
       "tmnxFPNetIngQgPStDrpHPrioOctsH": tmnxFPNetIngQgPStDrpHPrioOctsH,
       "tmnxFPNetIngQgPStOffLPrioOcts": tmnxFPNetIngQgPStOffLPrioOcts,
       "tmnxFPNetIngQgPStOffLPrioOctsL": tmnxFPNetIngQgPStOffLPrioOctsL,
       "tmnxFPNetIngQgPStOffLPrioOctsH": tmnxFPNetIngQgPStOffLPrioOctsH,
       "tmnxFPNetIngQgPStDrpLPrioOcts": tmnxFPNetIngQgPStDrpLPrioOcts,
       "tmnxFPNetIngQgPStDrpLPrioOctsL": tmnxFPNetIngQgPStDrpLPrioOctsL,
       "tmnxFPNetIngQgPStDrpLPrioOctsH": tmnxFPNetIngQgPStDrpLPrioOctsH,
       "tmnxFPNetIngQgPStFwdInProfPkts": tmnxFPNetIngQgPStFwdInProfPkts,
       "tmnxFPNetIngQgPStFwdInProfPktsL": tmnxFPNetIngQgPStFwdInProfPktsL,
       "tmnxFPNetIngQgPStFwdInProfPktsH": tmnxFPNetIngQgPStFwdInProfPktsH,
       "tmnxFPNetIngQgPStFwdOutProfPkts": tmnxFPNetIngQgPStFwdOutProfPkts,
       "tmnxFPNetIngQgPStFwdOutProfPktsL": tmnxFPNetIngQgPStFwdOutProfPktsL,
       "tmnxFPNetIngQgPStFwdOutProfPktsH": tmnxFPNetIngQgPStFwdOutProfPktsH,
       "tmnxFPNetIngQgPStFwdInProfOcts": tmnxFPNetIngQgPStFwdInProfOcts,
       "tmnxFPNetIngQgPStFwdInProfOctsL": tmnxFPNetIngQgPStFwdInProfOctsL,
       "tmnxFPNetIngQgPStFwdInProfOctsH": tmnxFPNetIngQgPStFwdInProfOctsH,
       "tmnxFPNetIngQgPStFwdOutProfOcts": tmnxFPNetIngQgPStFwdOutProfOcts,
       "tmnxFPNetIngQgPStFwdOutProfOctsL": tmnxFPNetIngQgPStFwdOutProfOctsL,
       "tmnxFPNetIngQgPStFwdOutProfOctsH": tmnxFPNetIngQgPStFwdOutProfOctsH,
       "tmnxFPNetIngQgPStUncolPktsOff": tmnxFPNetIngQgPStUncolPktsOff,
       "tmnxFPNetIngQgPStUncolPktsOffL": tmnxFPNetIngQgPStUncolPktsOffL,
       "tmnxFPNetIngQgPStUncolPktsOffH": tmnxFPNetIngQgPStUncolPktsOffH,
       "tmnxFPNetIngQgPStUncolOctsOff": tmnxFPNetIngQgPStUncolOctsOff,
       "tmnxFPNetIngQgPStUncolOctsOffL": tmnxFPNetIngQgPStUncolOctsOffL,
       "tmnxFPNetIngQgPStUncolOctsOffH": tmnxFPNetIngQgPStUncolOctsOffH,
       "tmnxFPAccIngQGrpPStatTable": tmnxFPAccIngQGrpPStatTable,
       "tmnxFPAccIngQGrpPStatEntry": tmnxFPAccIngQGrpPStatEntry,
       "tmnxFPAccIngQGrpPStatPolicerId": tmnxFPAccIngQGrpPStatPolicerId,
       "tmnxFPAccIngQGrpPStatMode": tmnxFPAccIngQGrpPStatMode,
       "tmnxFPAccIngQgPStOffHPrioPkts": tmnxFPAccIngQgPStOffHPrioPkts,
       "tmnxFPAccIngQgPStOffHPrioPktsL": tmnxFPAccIngQgPStOffHPrioPktsL,
       "tmnxFPAccIngQgPStOffHPrioPktsH": tmnxFPAccIngQgPStOffHPrioPktsH,
       "tmnxFPAccIngQgPStDrpHPrioPkts": tmnxFPAccIngQgPStDrpHPrioPkts,
       "tmnxFPAccIngQgPStDrpHPrioPktsL": tmnxFPAccIngQgPStDrpHPrioPktsL,
       "tmnxFPAccIngQgPStDrpHPrioPktsH": tmnxFPAccIngQgPStDrpHPrioPktsH,
       "tmnxFPAccIngQgPStOffLPrioPkts": tmnxFPAccIngQgPStOffLPrioPkts,
       "tmnxFPAccIngQgPStOffLPrioPktsL": tmnxFPAccIngQgPStOffLPrioPktsL,
       "tmnxFPAccIngQgPStOffLPrioPktsH": tmnxFPAccIngQgPStOffLPrioPktsH,
       "tmnxFPAccIngQgPStDrpLPrioPkts": tmnxFPAccIngQgPStDrpLPrioPkts,
       "tmnxFPAccIngQgPStDrpLPrioPktsL": tmnxFPAccIngQgPStDrpLPrioPktsL,
       "tmnxFPAccIngQgPStDrpLPrioPktsH": tmnxFPAccIngQgPStDrpLPrioPktsH,
       "tmnxFPAccIngQgPStOffHPrioOcts": tmnxFPAccIngQgPStOffHPrioOcts,
       "tmnxFPAccIngQgPStOffHPrioOctsL": tmnxFPAccIngQgPStOffHPrioOctsL,
       "tmnxFPAccIngQgPStOffHPrioOctsH": tmnxFPAccIngQgPStOffHPrioOctsH,
       "tmnxFPAccIngQgPStDrpHPrioOcts": tmnxFPAccIngQgPStDrpHPrioOcts,
       "tmnxFPAccIngQgPStDrpHPrioOctsL": tmnxFPAccIngQgPStDrpHPrioOctsL,
       "tmnxFPAccIngQgPStDrpHPrioOctsH": tmnxFPAccIngQgPStDrpHPrioOctsH,
       "tmnxFPAccIngQgPStOffLPrioOcts": tmnxFPAccIngQgPStOffLPrioOcts,
       "tmnxFPAccIngQgPStOffLPrioOctsL": tmnxFPAccIngQgPStOffLPrioOctsL,
       "tmnxFPAccIngQgPStOffLPrioOctsH": tmnxFPAccIngQgPStOffLPrioOctsH,
       "tmnxFPAccIngQgPStDrpLPrioOcts": tmnxFPAccIngQgPStDrpLPrioOcts,
       "tmnxFPAccIngQgPStDrpLPrioOctsL": tmnxFPAccIngQgPStDrpLPrioOctsL,
       "tmnxFPAccIngQgPStDrpLPrioOctsH": tmnxFPAccIngQgPStDrpLPrioOctsH,
       "tmnxFPAccIngQgPStFwdInProfPkts": tmnxFPAccIngQgPStFwdInProfPkts,
       "tmnxFPAccIngQgPStFwdInProfPktsL": tmnxFPAccIngQgPStFwdInProfPktsL,
       "tmnxFPAccIngQgPStFwdInProfPktsH": tmnxFPAccIngQgPStFwdInProfPktsH,
       "tmnxFPAccIngQgPStFwdOutProfPkts": tmnxFPAccIngQgPStFwdOutProfPkts,
       "tmnxFPAccIngQgPStFwdOutProfPktsL": tmnxFPAccIngQgPStFwdOutProfPktsL,
       "tmnxFPAccIngQgPStFwdOutProfPktsH": tmnxFPAccIngQgPStFwdOutProfPktsH,
       "tmnxFPAccIngQgPStFwdInProfOcts": tmnxFPAccIngQgPStFwdInProfOcts,
       "tmnxFPAccIngQgPStFwdInProfOctsL": tmnxFPAccIngQgPStFwdInProfOctsL,
       "tmnxFPAccIngQgPStFwdInProfOctsH": tmnxFPAccIngQgPStFwdInProfOctsH,
       "tmnxFPAccIngQgPStFwdOutProfOcts": tmnxFPAccIngQgPStFwdOutProfOcts,
       "tmnxFPAccIngQgPStFwdOutProfOctsL": tmnxFPAccIngQgPStFwdOutProfOctsL,
       "tmnxFPAccIngQgPStFwdOutProfOctsH": tmnxFPAccIngQgPStFwdOutProfOctsH,
       "tmnxFPAccIngQgPStUncolPktsOff": tmnxFPAccIngQgPStUncolPktsOff,
       "tmnxFPAccIngQgPStUncolPktsOffL": tmnxFPAccIngQgPStUncolPktsOffL,
       "tmnxFPAccIngQgPStUncolPktsOffH": tmnxFPAccIngQgPStUncolPktsOffH,
       "tmnxFPAccIngQgPStUncolOctsOff": tmnxFPAccIngQgPStUncolOctsOff,
       "tmnxFPAccIngQgPStUncolOctsOffL": tmnxFPAccIngQgPStUncolOctsOffL,
       "tmnxFPAccIngQgPStUncolOctsOffH": tmnxFPAccIngQgPStUncolOctsOffH,
       "tFPAccIngQGrpPlcrOvrTblLstChgd": tFPAccIngQGrpPlcrOvrTblLstChgd,
       "tFPAccIngQGrpPlcrOvrTable": tFPAccIngQGrpPlcrOvrTable,
       "tFPAccIngQGrpPlcrOvrEntry": tFPAccIngQGrpPlcrOvrEntry,
       "tFPAccIngQGrpPlcrOvrPolicerId": tFPAccIngQGrpPlcrOvrPolicerId,
       "tFPAccIngQGrpPlcrOvrRowStatus": tFPAccIngQGrpPlcrOvrRowStatus,
       "tFPAccIngQGrpPlcrOvrLastChgd": tFPAccIngQGrpPlcrOvrLastChgd,
       "tFPAccIngQGrpPlcrOvrAdminPIR": tFPAccIngQGrpPlcrOvrAdminPIR,
       "tFPAccIngQGrpPlcrOvrAdminCIR": tFPAccIngQGrpPlcrOvrAdminCIR,
       "tFPAccIngQGrpPlcrOvrStatMode": tFPAccIngQGrpPlcrOvrStatMode,
       "tFPAccIngQGrpPlcrOvrMBS": tFPAccIngQGrpPlcrOvrMBS,
       "tFPAccIngQGrpPlcrOvrCBS": tFPAccIngQGrpPlcrOvrCBS,
       "tFPAccIngQGrpPlcrOvrPktOffset": tFPAccIngQGrpPlcrOvrPktOffset,
       "tFPAccIngQGrpArbitStatTable": tFPAccIngQGrpArbitStatTable,
       "tFPAccIngQGrpArbitStatEntry": tFPAccIngQGrpArbitStatEntry,
       "tFPAccIngQGrpArbitStatName": tFPAccIngQGrpArbitStatName,
       "tFPAccIngQGrpArbitStatFwdPkts": tFPAccIngQGrpArbitStatFwdPkts,
       "tFPAccIngQGrpArbitStatFwdPktsL": tFPAccIngQGrpArbitStatFwdPktsL,
       "tFPAccIngQGrpArbitStatFwdPktsH": tFPAccIngQGrpArbitStatFwdPktsH,
       "tFPAccIngQGrpArbitStatFwdOcts": tFPAccIngQGrpArbitStatFwdOcts,
       "tFPAccIngQGrpArbitStatFwdOctsL": tFPAccIngQGrpArbitStatFwdOctsL,
       "tFPAccIngQGrpArbitStatFwdOctsH": tFPAccIngQGrpArbitStatFwdOctsH,
       "tFPNetIngQGrpArbitStatTable": tFPNetIngQGrpArbitStatTable,
       "tFPNetIngQGrpArbitStatEntry": tFPNetIngQGrpArbitStatEntry,
       "tFPNetIngQGrpArbitStatName": tFPNetIngQGrpArbitStatName,
       "tFPNetIngQGrpArbitStatFwdPkts": tFPNetIngQGrpArbitStatFwdPkts,
       "tFPNetIngQGrpArbitStatFwdPktsL": tFPNetIngQGrpArbitStatFwdPktsL,
       "tFPNetIngQGrpArbitStatFwdPktsH": tFPNetIngQGrpArbitStatFwdPktsH,
       "tFPNetIngQGrpArbitStatFwdOcts": tFPNetIngQGrpArbitStatFwdOcts,
       "tFPNetIngQGrpArbitStatFwdOctsL": tFPNetIngQGrpArbitStatFwdOctsL,
       "tFPNetIngQGrpArbitStatFwdOctsH": tFPNetIngQGrpArbitStatFwdOctsH,
       "tmnxVirtualSchedulerAdjTable": tmnxVirtualSchedulerAdjTable,
       "tmnxVirtualSchedulerAdjEntry": tmnxVirtualSchedulerAdjEntry,
       "tmnxCardRateCalcFastQueue": tmnxCardRateCalcFastQueue,
       "tmnxCardRateCalcSlowQueue": tmnxCardRateCalcSlowQueue,
       "tmnxCardSchedRun": tmnxCardSchedRun,
       "tmnxCardTaskScheduling": tmnxCardTaskScheduling,
       "tmnxCardSlowQueueThresh": tmnxCardSlowQueueThresh,
       "tmnxChassisNotificationObjects": tmnxChassisNotificationObjects,
       "tmnxEqNotificationRow": tmnxEqNotificationRow,
       "tmnxEqTypeNotificationRow": tmnxEqTypeNotificationRow,
       "tmnxChassisNotifyChassisId": tmnxChassisNotifyChassisId,
       "tmnxChassisNotifyHwIndex": tmnxChassisNotifyHwIndex,
       "tmnxRedSecondaryCPMStatus": tmnxRedSecondaryCPMStatus,
       "tmnxChassisNotifyOID": tmnxChassisNotifyOID,
       "tmnxSyncIfTimingNotifyAlarm": tmnxSyncIfTimingNotifyAlarm,
       "tmnxChassisNotifyMismatchedVer": tmnxChassisNotifyMismatchedVer,
       "tmnxChassisNotifySoftwareLocation": tmnxChassisNotifySoftwareLocation,
       "tmnxChassisNotifyCardFailureReason": tmnxChassisNotifyCardFailureReason,
       "tmnxChassisNotifyCardName": tmnxChassisNotifyCardName,
       "tmnxChassisNotifyCardSyncFile": tmnxChassisNotifyCardSyncFile,
       "tmnxCardComplexNumber": tmnxCardComplexNumber,
       "tmnxCardFwdDirection": tmnxCardFwdDirection,
       "tmnxCardSoftResetState": tmnxCardSoftResetState,
       "tmnxMdaNotifyType": tmnxMdaNotifyType,
       "tmnxCardSrcSlotBitmap": tmnxCardSrcSlotBitmap,
       "tmnxChassisAdminObjects": tmnxChassisAdminObjects,
       "tmnxChassisAdminCtrlObjs": tmnxChassisAdminCtrlObjs,
       "tmnxChassisAdminOwner": tmnxChassisAdminOwner,
       "tmnxChassisAdminControlApply": tmnxChassisAdminControlApply,
       "tmnxChassisAdminLastSetTimer": tmnxChassisAdminLastSetTimer,
       "tmnxChassisAdminLastSetTimeout": tmnxChassisAdminLastSetTimeout,
       "tmnxChassisAdminValueObjs": tmnxChassisAdminValueObjs,
       "tSyncIfTimingAdmTable": tSyncIfTimingAdmTable,
       "tSyncIfTimingAdmEntry": tSyncIfTimingAdmEntry,
       "tSyncIfTimingAdmRevert": tSyncIfTimingAdmRevert,
       "tSyncIfTimingAdmRefOrder1": tSyncIfTimingAdmRefOrder1,
       "tSyncIfTimingAdmRefOrder2": tSyncIfTimingAdmRefOrder2,
       "tSyncIfTimingAdmRef1SrcPort": tSyncIfTimingAdmRef1SrcPort,
       "tSyncIfTimingAdmRef1AdminStatus": tSyncIfTimingAdmRef1AdminStatus,
       "tSyncIfTimingAdmRef2SrcPort": tSyncIfTimingAdmRef2SrcPort,
       "tSyncIfTimingAdmRef2AdminStatus": tSyncIfTimingAdmRef2AdminStatus,
       "tSyncIfTimingAdmChanged": tSyncIfTimingAdmChanged,
       "tSyncIfTimingAdmRefOrder3": tSyncIfTimingAdmRefOrder3,
       "tSyncIfTimingAdmBITSIfType": tSyncIfTimingAdmBITSIfType,
       "tSyncIfTimingAdmBITSAdminStatus": tSyncIfTimingAdmBITSAdminStatus,
       "tSyncIfTimingAdmRef1SrcHw": tSyncIfTimingAdmRef1SrcHw,
       "tSyncIfTimingAdmRef1BITSIfType": tSyncIfTimingAdmRef1BITSIfType,
       "tSyncIfTimingAdmRef2SrcHw": tSyncIfTimingAdmRef2SrcHw,
       "tSyncIfTimingAdmRef2BITSIfType": tSyncIfTimingAdmRef2BITSIfType,
       "tSyncIfTimingAdmBITSOutAdmStatus": tSyncIfTimingAdmBITSOutAdmStatus,
       "tSyncIfTimingAdmBITSOutLineLen": tSyncIfTimingAdmBITSOutLineLen,
       "tSyncIfTimingAdmRef1CfgQltyLevel": tSyncIfTimingAdmRef1CfgQltyLevel,
       "tSyncIfTimingAdmRef2CfgQltyLevel": tSyncIfTimingAdmRef2CfgQltyLevel,
       "tSyncIfTimingAdmBITSCfgQltyLevel": tSyncIfTimingAdmBITSCfgQltyLevel,
       "tSyncIfTimingAdmRef1NationalUse": tSyncIfTimingAdmRef1NationalUse,
       "tSyncIfTimingAdmRef2NationalUse": tSyncIfTimingAdmRef2NationalUse,
       "tSyncIfTimingAdmBITSNationalUse": tSyncIfTimingAdmBITSNationalUse,
       "tSyncIfTimingAdmQLSelection": tSyncIfTimingAdmQLSelection,
       "tSyncIfTimingAdmRefOrder4": tSyncIfTimingAdmRefOrder4,
       "tSyncIfTimingAdmPTPAdminStatus": tSyncIfTimingAdmPTPAdminStatus,
       "tSyncIfTimingAdmPTPCfgQltyLevel": tSyncIfTimingAdmPTPCfgQltyLevel,
       "tSyncIfTimingAdmBITSOutSource": tSyncIfTimingAdmBITSOutSource,
       "tSyncIfTimingAdmRefOrder5": tSyncIfTimingAdmRefOrder5,
       "tSyncIfTimingAdmBITS2InAdminStatus": tSyncIfTimingAdmBITS2InAdminStatus,
       "tSyncIfTimingAdmBITS2OutAdminStatus": tSyncIfTimingAdmBITS2OutAdminStatus,
       "tmnxHwNotification": tmnxHwNotification,
       "tmnxChassisNotifyPrefix": tmnxChassisNotifyPrefix,
       "tmnxChassisNotification": tmnxChassisNotification,
       "tmnxHwConfigChange": tmnxHwConfigChange,
       "tmnxEnvTempTooHigh": tmnxEnvTempTooHigh,
       "tmnxEqPowerSupplyFailure": tmnxEqPowerSupplyFailure,
       "tmnxEqPowerSupplyInserted": tmnxEqPowerSupplyInserted,
       "tmnxEqPowerSupplyRemoved": tmnxEqPowerSupplyRemoved,
       "tmnxEqFanFailure": tmnxEqFanFailure,
       "tmnxEqCardFailure": tmnxEqCardFailure,
       "tmnxEqCardInserted": tmnxEqCardInserted,
       "tmnxEqCardRemoved": tmnxEqCardRemoved,
       "tmnxEqWrongCard": tmnxEqWrongCard,
       "tmnxEqCpuFailure": tmnxEqCpuFailure,
       "tmnxEqMemoryFailure": tmnxEqMemoryFailure,
       "tmnxEqBackdoorBusFailure": tmnxEqBackdoorBusFailure,
       "tmnxPeSoftwareError": tmnxPeSoftwareError,
       "tmnxPeSoftwareAbnormalHalt": tmnxPeSoftwareAbnormalHalt,
       "tmnxPeSoftwareVersionMismatch": tmnxPeSoftwareVersionMismatch,
       "tmnxPeOutOfMemory": tmnxPeOutOfMemory,
       "tmnxPeConfigurationError": tmnxPeConfigurationError,
       "tmnxPeStorageProblem": tmnxPeStorageProblem,
       "tmnxPeCpuCyclesExceeded": tmnxPeCpuCyclesExceeded,
       "tmnxRedPrimaryCPMFail": tmnxRedPrimaryCPMFail,
       "tmnxRedSecondaryCPMStatusChange": tmnxRedSecondaryCPMStatusChange,
       "tmnxRedRestoreSuccess": tmnxRedRestoreSuccess,
       "tmnxRedRestoreFail": tmnxRedRestoreFail,
       "tmnxChassisNotificationClear": tmnxChassisNotificationClear,
       "tmnxEqSyncIfTimingHoldover": tmnxEqSyncIfTimingHoldover,
       "tmnxEqSyncIfTimingHoldoverClear": tmnxEqSyncIfTimingHoldoverClear,
       "tmnxEqSyncIfTimingRef1Alarm": tmnxEqSyncIfTimingRef1Alarm,
       "tmnxEqSyncIfTimingRef1AlarmClear": tmnxEqSyncIfTimingRef1AlarmClear,
       "tmnxEqSyncIfTimingRef2Alarm": tmnxEqSyncIfTimingRef2Alarm,
       "tmnxEqSyncIfTimingRef2AlarmClear": tmnxEqSyncIfTimingRef2AlarmClear,
       "tmnxEqFlashDataLoss": tmnxEqFlashDataLoss,
       "tmnxEqFlashDiskFull": tmnxEqFlashDiskFull,
       "tmnxPeSoftwareLoadFailed": tmnxPeSoftwareLoadFailed,
       "tmnxPeBootloaderVersionMismatch": tmnxPeBootloaderVersionMismatch,
       "tmnxPeBootromVersionMismatch": tmnxPeBootromVersionMismatch,
       "tmnxPeFPGAVersionMismatch": tmnxPeFPGAVersionMismatch,
       "tmnxEqSyncIfTimingBITSAlarm": tmnxEqSyncIfTimingBITSAlarm,
       "tmnxEqSyncIfTimingBITSAlarmClear": tmnxEqSyncIfTimingBITSAlarmClear,
       "tmnxEqCardFirmwareUpgraded": tmnxEqCardFirmwareUpgraded,
       "tmnxChassisUpgradeInProgress": tmnxChassisUpgradeInProgress,
       "tmnxChassisUpgradeComplete": tmnxChassisUpgradeComplete,
       "tmnxChassisHiBwMcastAlarm": tmnxChassisHiBwMcastAlarm,
       "tmnxEqMdaCfgNotCompatible": tmnxEqMdaCfgNotCompatible,
       "tmnxCpmCardSyncFileNotPresent": tmnxCpmCardSyncFileNotPresent,
       "tmnxEqMdaXplError": tmnxEqMdaXplError,
       "tmnxEqCardPChipError": tmnxEqCardPChipError,
       "tmnxEqCardSoftResetAlarm": tmnxEqCardSoftResetAlarm,
       "tmnxEqMdaSyncENotCompatible": tmnxEqMdaSyncENotCompatible,
       "tmnxIPsecIsaGrpActiveIsaChgd": tmnxIPsecIsaGrpActiveIsaChgd,
       "tmnxEqCardPChipMemoryEvent": tmnxEqCardPChipMemoryEvent,
       "tmnxIPsecIsaGrpUnableToSwitch": tmnxIPsecIsaGrpUnableToSwitch,
       "tmnxIPsecIsaGrpTnlLowWMark": tmnxIPsecIsaGrpTnlLowWMark,
       "tmnxIPsecIsaGrpTnlHighWMark": tmnxIPsecIsaGrpTnlHighWMark,
       "tmnxIPsecIsaGrpTnlMax": tmnxIPsecIsaGrpTnlMax,
       "tmnxEqSyncIfTimingRef1Quality": tmnxEqSyncIfTimingRef1Quality,
       "tmnxEqSyncIfTimingRef2Quality": tmnxEqSyncIfTimingRef2Quality,
       "tmnxEqSyncIfTimingBITSQuality": tmnxEqSyncIfTimingBITSQuality,
       "tmnxEqSyncIfTimingBITS2Quality": tmnxEqSyncIfTimingBITS2Quality,
       "tmnxEqSyncIfTimingRefSwitch": tmnxEqSyncIfTimingRefSwitch,
       "tmnxEqSyncIfTimingBITS2Alarm": tmnxEqSyncIfTimingBITS2Alarm,
       "tmnxEqSyncIfTimingBITS2AlarmClr": tmnxEqSyncIfTimingBITS2AlarmClr,
       "tmnxEqSyncIfTimingBITSOutRefChg": tmnxEqSyncIfTimingBITSOutRefChg,
       "tmnxEqCardPChipCamEvent": tmnxEqCardPChipCamEvent,
       "tmnxEqSyncIfTimingSystemQuality": tmnxEqSyncIfTimingSystemQuality,
       "tmnxEqHwEnhancedCapability": tmnxEqHwEnhancedCapability,
       "tmnxEqSyncIfTimingPTPQuality": tmnxEqSyncIfTimingPTPQuality,
       "tmnxEqSyncIfTimingPTPAlarm": tmnxEqSyncIfTimingPTPAlarm,
       "tmnxEqSyncIfTimingPTPAlarmClear": tmnxEqSyncIfTimingPTPAlarmClear,
       "tmnxPeFirmwareVersionWarning": tmnxPeFirmwareVersionWarning,
       "tmnxMDAIsaTunnelGroupChange": tmnxMDAIsaTunnelGroupChange}
)
