# SNMP MIB module (ALCATEL-IND1-TIMETRA-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TIMETRA-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:10 2024
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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxOperState,
 TmnxPortID) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxOperState",
    "TmnxPortID")

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


# MODULE-IDENTITY

tmnxChassisMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 2)
)
tmnxChassisMIBModule.setRevisions(
        ("1908-01-01 00:00",
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("ccm", 15),
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
          ("unknown", 2))
    )



class TmnxCardType(Unsigned32, TextualConvention):
    status = "current"


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
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeA", 1),
          ("modeB", 2),
          ("modeC", 3))
    )



class TmnxSETSRefSource(Integer32, TextualConvention):
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
        *(("bits", 3),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisFanIndex"),
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullSpeed", 3),
          ("halfSpeed", 2),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyId"),
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
        *(("acMultiple", 3),
          ("acSingle", 2),
          ("dc", 1),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisTypeIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwIndex"),
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
              14)
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwContainedIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcmIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcmTypeIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
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
_TmnxCardSupportedTypes_Type = TmnxCardType
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


class _TmnxCardReboot_Type(TmnxActionType):
    """Custom type tmnxCardReboot based on TmnxActionType"""


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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardSlotNum"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardNum"),
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
_TmnxCpmCardSupportedTypes_Type = TmnxCardType
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
          ("redundantSynching", 6),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxFabricSlotNum"),
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


class _TmnxFabricAssignedType_Type(TmnxCardType):
    """Custom type tmnxFabricAssignedType based on TmnxCardType"""
    defaultValue = 2


_TmnxFabricAssignedType_Object = MibTableColumn
tmnxFabricAssignedType = _TmnxFabricAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 6, 1, 2),
    _TmnxFabricAssignedType_Type()
)
tmnxFabricAssignedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFabricAssignedType.setStatus("current")
_TmnxFabricEquippedType_Type = TmnxCardType
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmFlashId"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
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
_TmnxMDAMcPathMgmtPriInUseBw_Type = Gauge32
_TmnxMDAMcPathMgmtPriInUseBw_Object = MibTableColumn
tmnxMDAMcPathMgmtPriInUseBw = _TmnxMDAMcPathMgmtPriInUseBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 36),
    _TmnxMDAMcPathMgmtPriInUseBw_Type()
)
tmnxMDAMcPathMgmtPriInUseBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtPriInUseBw.setStatus("current")
_TmnxMDAMcPathMgmtSecInUseBw_Type = Gauge32
_TmnxMDAMcPathMgmtSecInUseBw_Object = MibTableColumn
tmnxMDAMcPathMgmtSecInUseBw = _TmnxMDAMcPathMgmtSecInUseBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 37),
    _TmnxMDAMcPathMgmtSecInUseBw_Type()
)
tmnxMDAMcPathMgmtSecInUseBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtSecInUseBw.setStatus("current")
_TmnxMDAMcPathMgmtAncInUseBw_Type = Gauge32
_TmnxMDAMcPathMgmtAncInUseBw_Object = MibTableColumn
tmnxMDAMcPathMgmtAncInUseBw = _TmnxMDAMcPathMgmtAncInUseBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 38),
    _TmnxMDAMcPathMgmtAncInUseBw_Type()
)
tmnxMDAMcPathMgmtAncInUseBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtAncInUseBw.setStatus("current")
_TmnxMDAMcPathMgmtBlkHoleInUseBw_Type = Gauge32
_TmnxMDAMcPathMgmtBlkHoleInUseBw_Object = MibTableColumn
tmnxMDAMcPathMgmtBlkHoleInUseBw = _TmnxMDAMcPathMgmtBlkHoleInUseBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 3, 8, 1, 39),
    _TmnxMDAMcPathMgmtBlkHoleInUseBw_Type()
)
tmnxMDAMcPathMgmtBlkHoleInUseBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtBlkHoleInUseBw.setStatus("current")
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardTypeIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMdaTypeIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagId"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagId"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathId"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagId"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathId"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcType"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMcmSlotNum"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMcmTypeIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardSlotNum"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardNum"),
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
    ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB",
     "tmnxSyncIfTimingEntry")
)
tmnxSyncIfTimingEntry.setIndexNames(*tmnxCpmCardEntry.getIndexNames())

# Managed Objects groups

tmnxChassisNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 4)
)
tmnxChassisNotifyObjsGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqNotificationRow"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqTypeNotificationRow"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxRedSecondaryCPMStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyOID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyMismatchedVer"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifySoftwareLocation"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotifyObjsGroup.setStatus("current")

tmnxChassisV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 9)
)
tmnxChassisV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisTotalNumber"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisLastChange"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisRowStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisLocation"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisCoordinates"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNumSlots"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNumPorts"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNumPwrSupplies"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNumFanTrays"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNumFans"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisCriticalLEDState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisMajorLEDState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisMinorLEDState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisBaseMacAddress"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisCLLICode"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisReboot"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisUpgrade"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisAdminMode"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisOperMode"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisModeForce"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisUpdateWaitTime"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisUpdateTimeLeft"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisFanOperStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisFanSpeed"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyACStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyDCStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempThreshold"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply1Status"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply2Status"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyAssignedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisTypeName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwLastChange"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwMfgString"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwMfgBoardNumber"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSerialNumber"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwManufactureDate"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwAlias"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwAssetID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwCLEI"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwIsFRU"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwContainedIn"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwParentRelPos"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwAdminState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwOperState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwTempSensor"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwTemperature"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwTempThreshold"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwBootCodeVersion"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSwLastBoot"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwAlarmState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwLastAlarmEvent"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClearAlarms"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSwImageSource"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwMfgDeviations"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwBaseMacAddress"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwFailureReason"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwContainedIndex"))
)
if mibBuilder.loadTexts:
    tmnxChassisV3v0Group.setStatus("obsolete")

tmnxMDAV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 10)
)
tmnxMDAV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDASupportedTypes"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAAssignedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAEquippedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMaxPorts"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAEquippedPorts"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDATxTimingSelected"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDASyncIfTimingStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDANetworkIngQueues"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDACapabilities"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMinChannelization"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMaxChannelization"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMaxChannels"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAChannelsInUse"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDACcagId"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMdaTypeName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMdaTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMdaTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagRowStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagDescription"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagOperStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagCcaRate"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagLastChanged"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagAccessAdaptQos"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathLastChanged"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathRate"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathRateOption"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathWeight"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcLastChanged"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcEgrPoolResvCbs"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcEgrPoolSlpPlcy"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcIngPoolResvCbs"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcIngPoolSlpPlcy"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcAcctPolicyId"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcCollectStats"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcQueuePlcy"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcMac"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcMtu"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcHwMac"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcUserAssignedMac"))
)
if mibBuilder.loadTexts:
    tmnxMDAV3v0Group.setStatus("obsolete")

tmnxChassisObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 11)
)
tmnxChassisObsoleteGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSwState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardAllowedTypes"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardAllowedTypes"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAAllowedTypes"))
)
if mibBuilder.loadTexts:
    tmnxChassisObsoleteGroup.setStatus("current")

tmnxCardV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 12)
)
tmnxCardV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardLastChange"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardTypeName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardSupportedTypes"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardAssignedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardEquippedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardClockSource"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardNumMdaSlots"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardNumMdas"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardReboot"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardMemorySize"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardLastChange"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardSupportedTypes"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardAssignedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardEquippedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardBootOptionVersion"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardBootOptionLastModified"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigBootedVersion"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardIndexBootedVersion"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigLastModified"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigLastSaved"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardRedundant"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardClockSource"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardNumCpus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardCpuType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardMemorySize"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardSwitchToRedundantCard"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardReboot"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardRereadBootOptions"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigFileLastBooted"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigFileLastSaved"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigFileLastBootedHeader"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardIndexFileLastBootedHeader"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardBootOptionSource"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardConfigSource"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardBootOptionLastSaved"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxFabricLastChange"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxFabricAssignedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxFabricEquippedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxFabricHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmFlashOperStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmFlashSerialNumber"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmFlashFirmwareRevision"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmFlashModelNumber"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmFlashCapacity"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmFlashUsed"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmFlashHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRevert"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRefOrder1"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRefOrder2"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1SrcPort"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1AdminStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1InUse"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1Qualified"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1Alarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2SrcPort"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2AdminStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2InUse"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2Qualified"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2Alarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingFreqOffset"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRefOrder3"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSIfType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSInUse"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSQualified"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingBITSAlarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRevert"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRefOrder1"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRefOrder2"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef1SrcPort"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef1AdminStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef2SrcPort"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef2AdminStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmChanged"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRefOrder3"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmBITSIfType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmBITSAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisAdminOwner"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisAdminControlApply"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisAdminLastSetTimer"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisAdminLastSetTimeout"))
)
if mibBuilder.loadTexts:
    tmnxCardV3v0Group.setStatus("current")

tmnxMDAV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 13)
)
tmnxMDAV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDASupportedTypes"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAAssignedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAEquippedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMaxPorts"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAEquippedPorts"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDATxTimingSelected"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDASyncIfTimingStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDANetworkIngQueues"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDACapabilities"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMinChannelization"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMaxChannelization"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMaxChannels"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAChannelsInUse"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDACcagId"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMdaTypeName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMdaTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMdaTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAReboot"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagRowStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagDescription"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagOperStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagCcaRate"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagLastChanged"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagAccessAdaptQos"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathLastChanged"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathRate"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathRateOption"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathWeight"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcLastChanged"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcEgrPoolResvCbs"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcEgrPoolSlpPlcy"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcIngPoolResvCbs"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcIngPoolSlpPlcy"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcAcctPolicyId"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcCollectStats"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcQueuePlcy"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcMac"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcMtu"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcHwMac"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcagPathCcUserAssignedMac"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastSource"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastAlarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastTapCount"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAHiBwMcastGroup"))
)
if mibBuilder.loadTexts:
    tmnxMDAV4v0Group.setStatus("current")

tmnx7710HwV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 15)
)
tmnx7710HwV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisOverTempState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCpmCardMasterSlaveRefState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcmOperStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcmHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcmEquippedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcmTypeName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcmTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCcmTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMcmSupportedTypes"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMcmAssignedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMcmEquippedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMcmHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMcmTypeName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMcmTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMcmTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyInputStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyOutputStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAReboot"))
)
if mibBuilder.loadTexts:
    tmnx7710HwV3v0Group.setStatus("current")

tmnxChassisV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 16)
)
tmnxChassisV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisTotalNumber"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisLastChange"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisRowStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisLocation"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisCoordinates"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNumSlots"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNumPorts"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNumPwrSupplies"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNumFanTrays"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNumFans"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisCriticalLEDState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisMajorLEDState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisMinorLEDState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisBaseMacAddress"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisCLLICode"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisReboot"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisUpgrade"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisAdminMode"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisOperMode"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisModeForce"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisUpdateTimeLeft"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisFanOperStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisFanSpeed"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyACStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyDCStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempThreshold"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply1Status"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply2Status"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyAssignedType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisTypeName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisTypeDescription"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisTypeStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwLastChange"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwMfgString"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwMfgBoardNumber"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSerialNumber"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwManufactureDate"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwAlias"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwAssetID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwCLEI"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwIsFRU"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwContainedIn"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwParentRelPos"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwAdminState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwOperState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwTempSensor"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwTemperature"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwTempThreshold"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwBootCodeVersion"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSwLastBoot"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwAlarmState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwLastAlarmEvent"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClearAlarms"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSwImageSource"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwMfgDeviations"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwBaseMacAddress"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwFailureReason"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwContainedIndex"))
)
if mibBuilder.loadTexts:
    tmnxChassisV5v0Group.setStatus("current")

tmnxChassisV5v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 17)
)
tmnxChassisV5v0ObsoleteGroup.setObjects(
    ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisUpdateWaitTime")
)
if mibBuilder.loadTexts:
    tmnxChassisV5v0ObsoleteGroup.setStatus("current")

tmnx77x0CESMDAV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 18)
)
tmnx77x0CESMDAV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAClockMode"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDADiffTimestampFreq"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAIngNamedPoolPolicy"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAEgrNamedPoolPolicy"))
)
if mibBuilder.loadTexts:
    tmnx77x0CESMDAV6v0Group.setStatus("current")

tmnx7710SETSRefSrcHwV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 22)
)
tmnx7710SETSRefSrcHwV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1SrcHw"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef1BITSIfType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2SrcHw"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingRef2BITSIfType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef1SrcHw"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef1BITSIfType"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef2SrcHw"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tSyncIfTimingAdmRef2BITSIfType"))
)
if mibBuilder.loadTexts:
    tmnx7710SETSRefSrcHwV6v0Group.setStatus("current")

tmnxMDAMcPathMgmtV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 24)
)
tmnxMDAMcPathMgmtV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtBwPlcyName"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtPriPathLimit"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtSecPathLimit"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtAncPathLimit"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtAdminState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtPriInUseBw"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtSecInUseBw"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtAncInUseBw"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDAMcPathMgmtBlkHoleInUseBw"))
)
if mibBuilder.loadTexts:
    tmnxMDAMcPathMgmtV6v0Group.setStatus("current")

tmnxCardV6v0NamedPoolPlcyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 25)
)
tmnxCardV6v0NamedPoolPlcyGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardNamedPoolAdminMode"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardNamedPoolOperMode"))
)
if mibBuilder.loadTexts:
    tmnxCardV6v0NamedPoolPlcyGroup.setStatus("current")

tmnxChassisNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 26)
)
tmnxChassisNotifyObjsV6v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardName")
)
if mibBuilder.loadTexts:
    tmnxChassisNotifyObjsV6v0Group.setStatus("current")


# Notification objects

tmnxHwConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 1)
)
tmnxHwConfigChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxHwConfigChange.setStatus(
        "obsolete"
    )

tmnxEnvTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 2)
)
tmnxEnvTempTooHigh.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwTemperature"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwTempThreshold"))
)
if mibBuilder.loadTexts:
    tmnxEnvTempTooHigh.setStatus(
        "current"
    )

tmnxEqPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 3)
)
tmnxEqPowerSupplyFailure.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyACStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyDCStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyTempThreshold"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply1Status"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupply2Status"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyInputStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisPowerSupplyOutputStatus"))
)
if mibBuilder.loadTexts:
    tmnxEqPowerSupplyFailure.setStatus(
        "current"
    )

tmnxEqPowerSupplyInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 4)
)
tmnxEqPowerSupplyInserted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqPowerSupplyInserted.setStatus(
        "current"
    )

tmnxEqPowerSupplyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 5)
)
tmnxEqPowerSupplyRemoved.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqPowerSupplyRemoved.setStatus(
        "current"
    )

tmnxEqFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 6)
)
tmnxEqFanFailure.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisFanOperStatus"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisFanSpeed"))
)
if mibBuilder.loadTexts:
    tmnxEqFanFailure.setStatus(
        "current"
    )

tmnxEqCardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 7)
)
tmnxEqCardFailure.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwOperState"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxEqCardFailure.setStatus(
        "current"
    )

tmnxEqCardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 8)
)
tmnxEqCardInserted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardName"))
)
if mibBuilder.loadTexts:
    tmnxEqCardInserted.setStatus(
        "current"
    )

tmnxEqCardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 9)
)
tmnxEqCardRemoved.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCardName"))
)
if mibBuilder.loadTexts:
    tmnxEqCardRemoved.setStatus(
        "current"
    )

tmnxEqWrongCard = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 10)
)
tmnxEqWrongCard.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqWrongCard.setStatus(
        "current"
    )

tmnxEqCpuFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 11)
)
tmnxEqCpuFailure.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqCpuFailure.setStatus(
        "obsolete"
    )

tmnxEqMemoryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 12)
)
tmnxEqMemoryFailure.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqMemoryFailure.setStatus(
        "obsolete"
    )

tmnxEqBackdoorBusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 13)
)
tmnxEqBackdoorBusFailure.setObjects(
    ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId")
)
if mibBuilder.loadTexts:
    tmnxEqBackdoorBusFailure.setStatus(
        "obsolete"
    )

tmnxPeSoftwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 14)
)
tmnxPeSoftwareError.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeSoftwareError.setStatus(
        "obsolete"
    )

tmnxPeSoftwareAbnormalHalt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 15)
)
tmnxPeSoftwareAbnormalHalt.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeSoftwareAbnormalHalt.setStatus(
        "obsolete"
    )

tmnxPeSoftwareVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 16)
)
tmnxPeSoftwareVersionMismatch.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyMismatchedVer"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"))
)
if mibBuilder.loadTexts:
    tmnxPeSoftwareVersionMismatch.setStatus(
        "current"
    )

tmnxPeOutOfMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 17)
)
tmnxPeOutOfMemory.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeOutOfMemory.setStatus(
        "obsolete"
    )

tmnxPeConfigurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 18)
)
tmnxPeConfigurationError.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeConfigurationError.setStatus(
        "obsolete"
    )

tmnxPeStorageProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 19)
)
tmnxPeStorageProblem.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeStorageProblem.setStatus(
        "obsolete"
    )

tmnxPeCpuCyclesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 20)
)
tmnxPeCpuCyclesExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxPeCpuCyclesExceeded.setStatus(
        "obsolete"
    )

tmnxRedPrimaryCPMFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 21)
)
tmnxRedPrimaryCPMFail.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxRedPrimaryCPMFail.setStatus(
        "current"
    )

tmnxRedSecondaryCPMStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 22)
)
tmnxRedSecondaryCPMStatusChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxRedSecondaryCPMStatus"))
)
if mibBuilder.loadTexts:
    tmnxRedSecondaryCPMStatusChange.setStatus(
        "obsolete"
    )

tmnxRedRestoreSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 23)
)
tmnxRedRestoreSuccess.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxRedRestoreSuccess.setStatus(
        "obsolete"
    )

tmnxRedRestoreFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 24)
)
tmnxRedRestoreFail.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxRedRestoreFail.setStatus(
        "obsolete"
    )

tmnxChassisNotificationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 25)
)
tmnxChassisNotificationClear.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyOID"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationClear.setStatus(
        "current"
    )

tmnxEqSyncIfTimingHoldover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 26)
)
tmnxEqSyncIfTimingHoldover.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingHoldover.setStatus(
        "current"
    )

tmnxEqSyncIfTimingHoldoverClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 27)
)
tmnxEqSyncIfTimingHoldoverClear.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingHoldoverClear.setStatus(
        "current"
    )

tmnxEqSyncIfTimingRef1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 28)
)
tmnxEqSyncIfTimingRef1Alarm.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingRef1Alarm.setStatus(
        "current"
    )

tmnxEqSyncIfTimingRef1AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 29)
)
tmnxEqSyncIfTimingRef1AlarmClear.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingRef1AlarmClear.setStatus(
        "current"
    )

tmnxEqSyncIfTimingRef2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 30)
)
tmnxEqSyncIfTimingRef2Alarm.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingRef2Alarm.setStatus(
        "current"
    )

tmnxEqSyncIfTimingRef2AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 31)
)
tmnxEqSyncIfTimingRef2AlarmClear.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingRef2AlarmClear.setStatus(
        "current"
    )

tmnxEqFlashDataLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 32)
)
tmnxEqFlashDataLoss.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwOperState"))
)
if mibBuilder.loadTexts:
    tmnxEqFlashDataLoss.setStatus(
        "current"
    )

tmnxEqFlashDiskFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 33)
)
tmnxEqFlashDiskFull.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwOperState"))
)
if mibBuilder.loadTexts:
    tmnxEqFlashDiskFull.setStatus(
        "current"
    )

tmnxPeSoftwareLoadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 34)
)
tmnxPeSoftwareLoadFailed.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifySoftwareLocation"))
)
if mibBuilder.loadTexts:
    tmnxPeSoftwareLoadFailed.setStatus(
        "current"
    )

tmnxPeBootloaderVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 35)
)
tmnxPeBootloaderVersionMismatch.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyMismatchedVer"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"))
)
if mibBuilder.loadTexts:
    tmnxPeBootloaderVersionMismatch.setStatus(
        "current"
    )

tmnxPeBootromVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 36)
)
tmnxPeBootromVersionMismatch.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyMismatchedVer"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"))
)
if mibBuilder.loadTexts:
    tmnxPeBootromVersionMismatch.setStatus(
        "current"
    )

tmnxPeFPGAVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 37)
)
tmnxPeFPGAVersionMismatch.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyMismatchedVer"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwSoftwareCodeVersion"))
)
if mibBuilder.loadTexts:
    tmnxPeFPGAVersionMismatch.setStatus(
        "current"
    )

tmnxEqSyncIfTimingBITSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 38)
)
tmnxEqSyncIfTimingBITSAlarm.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingBITSAlarm.setStatus(
        "current"
    )

tmnxEqSyncIfTimingBITSAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 39)
)
tmnxEqSyncIfTimingBITSAlarmClear.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxSyncIfTimingNotifyAlarm"))
)
if mibBuilder.loadTexts:
    tmnxEqSyncIfTimingBITSAlarmClear.setStatus(
        "current"
    )

tmnxEqCardFirmwareUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 40)
)
tmnxEqCardFirmwareUpgraded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqCardFirmwareUpgraded.setStatus(
        "current"
    )

tmnxChassisUpgradeInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 41)
)
tmnxChassisUpgradeInProgress.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxChassisUpgradeInProgress.setStatus(
        "current"
    )

tmnxChassisUpgradeComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 42)
)
tmnxChassisUpgradeComplete.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxChassisUpgradeComplete.setStatus(
        "current"
    )

tmnxChassisHiBwMcastAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 43)
)
tmnxChassisHiBwMcastAlarm.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxChassisHiBwMcastAlarm.setStatus(
        "current"
    )

tmnxEqMdaCfgNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 1, 0, 44)
)
tmnxEqMdaCfgNotCompatible.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyHwIndex"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwID"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwClass"))
)
if mibBuilder.loadTexts:
    tmnxEqMdaCfgNotCompatible.setStatus(
        "current"
    )


# Notifications groups

tmnxChassisNotifyObsoleteGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 7)
)
tmnxChassisNotifyObsoleteGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxHwConfigChange"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCpuFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqMemoryFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqBackdoorBusFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareError"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareAbnormalHalt"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeOutOfMemory"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeConfigurationError"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeStorageProblem"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeCpuCyclesExceeded"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxRedSecondaryCPMStatusChange"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxRedRestoreSuccess"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxRedRestoreFail"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotifyObsoleteGroup.setStatus(
        "current"
    )

tmnxChassisNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 14)
)
tmnxChassisNotificationV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEnvTempTooHigh"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyInserted"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyRemoved"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqFanFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardInserted"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardRemoved"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqWrongCard"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxRedPrimaryCPMFail"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotificationClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldover"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldoverClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1Alarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2Alarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqFlashDataLoss"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqFlashDiskFull"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareLoadFailed"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeBootloaderVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeBootromVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeFPGAVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardFirmwareUpgraded"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeInProgress"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeComplete"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisHiBwMcastAlarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqMdaCfgNotCompatible"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationV4v0Group.setStatus(
        "obsolete"
    )

tmnxChassisNotificationV3v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 20)
)
tmnxChassisNotificationV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEnvTempTooHigh"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyInserted"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyRemoved"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqFanFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardInserted"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardRemoved"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqWrongCard"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxRedPrimaryCPMFail"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotificationClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldover"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldoverClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1Alarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2Alarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqFlashDataLoss"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqFlashDiskFull"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareLoadFailed"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeBootloaderVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeBootromVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeFPGAVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardFirmwareUpgraded"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqMdaCfgNotCompatible"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationV3v0Group.setStatus(
        "obsolete"
    )

tmnxChassisNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 2, 21)
)
tmnxChassisNotificationV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEnvTempTooHigh"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyInserted"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqPowerSupplyRemoved"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqFanFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardFailure"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardInserted"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardRemoved"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqWrongCard"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxRedPrimaryCPMFail"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisNotificationClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldover"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingHoldoverClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1Alarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef1AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2Alarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingRef2AlarmClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqFlashDataLoss"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqFlashDiskFull"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeSoftwareLoadFailed"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeBootloaderVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeBootromVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxPeFPGAVersionMismatch"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqSyncIfTimingBITSAlarmClear"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqCardFirmwareUpgraded"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeInProgress"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisUpgradeComplete"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisHiBwMcastAlarm"),
        ("ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxEqMdaCfgNotCompatible"))
)
if mibBuilder.loadTexts:
    tmnxChassisNotificationV6v0Group.setStatus(
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
        "current"
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
        "current"
    )

tmnxChassis7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxChassis7450V6v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-CHASSIS-MIB",
    **{"TmnxAlarmState": TmnxAlarmState,
       "TmnxChassisIndex": TmnxChassisIndex,
       "TmnxHwIndex": TmnxHwIndex,
       "TmnxHwIndexOrZero": TmnxHwIndexOrZero,
       "TmnxHwClass": TmnxHwClass,
       "TmnxCardType": TmnxCardType,
       "TmnxChassisType": TmnxChassisType,
       "TmnxDeviceState": TmnxDeviceState,
       "TmnxLEDState": TmnxLEDState,
       "TmnxMdaType": TmnxMdaType,
       "TmnxMDASuppType": TmnxMDASuppType,
       "TmnxMDAChanType": TmnxMDAChanType,
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
       "TmnxCcagId": TmnxCcagId,
       "TmnxCcagRate": TmnxCcagRate,
       "TmnxCcagRateOption": TmnxCcagRateOption,
       "tmnxChassisMIBModule": tmnxChassisMIBModule,
       "tmnxHwConformance": tmnxHwConformance,
       "tmnxChassisConformance": tmnxChassisConformance,
       "tmnxChassisCompliances": tmnxChassisCompliances,
       "tmnxChassisV4v0Compliance": tmnxChassisV4v0Compliance,
       "tmnxChassisComp7710": tmnxChassisComp7710,
       "tmnxChassisComp7710V3v0": tmnxChassisComp7710V3v0,
       "tmnxChassisComp7710V5v0": tmnxChassisComp7710V5v0,
       "tmnxChassisComp7710V6v0": tmnxChassisComp7710V6v0,
       "tmnxChassisV5v0Compliance": tmnxChassisV5v0Compliance,
       "tmnxChassis7750V6v0Compliance": tmnxChassis7750V6v0Compliance,
       "tmnxChassis7450V6v0Compliance": tmnxChassis7450V6v0Compliance,
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
       "tmnxChassisNotificationV3v0Group": tmnxChassisNotificationV3v0Group,
       "tmnxChassisNotificationV6v0Group": tmnxChassisNotificationV6v0Group,
       "tmnx7710SETSRefSrcHwV6v0Group": tmnx7710SETSRefSrcHwV6v0Group,
       "tmnxMDAMcPathMgmtV6v0Group": tmnxMDAMcPathMgmtV6v0Group,
       "tmnxCardV6v0NamedPoolPlcyGroup": tmnxCardV6v0NamedPoolPlcyGroup,
       "tmnxChassisNotifyObjsV6v0Group": tmnxChassisNotifyObjsV6v0Group,
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
       "tmnxChassisFanTable": tmnxChassisFanTable,
       "tmnxChassisFanEntry": tmnxChassisFanEntry,
       "tmnxChassisFanIndex": tmnxChassisFanIndex,
       "tmnxChassisFanOperStatus": tmnxChassisFanOperStatus,
       "tmnxChassisFanSpeed": tmnxChassisFanSpeed,
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
       "tmnxFabricLastChange": tmnxFabricLastChange,
       "tmnxFabricTable": tmnxFabricTable,
       "tmnxFabricEntry": tmnxFabricEntry,
       "tmnxFabricSlotNum": tmnxFabricSlotNum,
       "tmnxFabricAssignedType": tmnxFabricAssignedType,
       "tmnxFabricEquippedType": tmnxFabricEquippedType,
       "tmnxFabricHwIndex": tmnxFabricHwIndex,
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
       "tmnxMDAMcPathMgmtBwPlcyName": tmnxMDAMcPathMgmtBwPlcyName,
       "tmnxMDAMcPathMgmtPriPathLimit": tmnxMDAMcPathMgmtPriPathLimit,
       "tmnxMDAMcPathMgmtSecPathLimit": tmnxMDAMcPathMgmtSecPathLimit,
       "tmnxMDAMcPathMgmtAncPathLimit": tmnxMDAMcPathMgmtAncPathLimit,
       "tmnxMDAMcPathMgmtAdminState": tmnxMDAMcPathMgmtAdminState,
       "tmnxMDAIngNamedPoolPolicy": tmnxMDAIngNamedPoolPolicy,
       "tmnxMDAEgrNamedPoolPolicy": tmnxMDAEgrNamedPoolPolicy,
       "tmnxMDAMcPathMgmtPriInUseBw": tmnxMDAMcPathMgmtPriInUseBw,
       "tmnxMDAMcPathMgmtSecInUseBw": tmnxMDAMcPathMgmtSecInUseBw,
       "tmnxMDAMcPathMgmtAncInUseBw": tmnxMDAMcPathMgmtAncInUseBw,
       "tmnxMDAMcPathMgmtBlkHoleInUseBw": tmnxMDAMcPathMgmtBlkHoleInUseBw,
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
       "tmnxEqMdaCfgNotCompatible": tmnxEqMdaCfgNotCompatible}
)
