# SNMP MIB module (CISCO-OPTICAL-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OPTICAL-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:24 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoOpticalMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 264)
)
ciscoOpticalMonitorMIB.setRevisions(
        ("2007-01-02 00:00",
         "2002-05-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OpticalParameterType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("acPower", 2),
          ("ambientTemp", 3),
          ("biasCurrent", 5),
          ("laserTemp", 4),
          ("peltierCurrent", 6),
          ("power", 1),
          ("xcvrVoltage", 7))
    )



class OpticalParameterValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )



class OpticalIfDirection(Integer32, TextualConvention):
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
        *(("notApplicable", 3),
          ("receive", 1),
          ("transmit", 2))
    )



class OpticalIfMonLocation(Integer32, TextualConvention):
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
        *(("afterAdjustment", 2),
          ("beforeAdjustment", 1),
          ("notApplicable", 3))
    )



class OpticalAlarmStatus(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class OpticalAlarmSeverity(Integer32, TextualConvention):
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
        *(("cleared", 6),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("notAlarmed", 4),
          ("notReported", 5))
    )



class OpticalAlarmSeverityOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )



class OpticalPMPeriod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMin", 1),
          ("twentyFourHour", 2))
    )



# MIB Managed Objects in the order of their OIDs

_COpticalMonitorMIBObjects_ObjectIdentity = ObjectIdentity
cOpticalMonitorMIBObjects = _COpticalMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1)
)
_COpticalMonGroup_ObjectIdentity = ObjectIdentity
cOpticalMonGroup = _COpticalMonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1)
)
_COpticalMonTable_Object = MibTable
cOpticalMonTable = _COpticalMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cOpticalMonTable.setStatus("current")
_COpticalMonEntry_Object = MibTableRow
cOpticalMonEntry = _COpticalMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1)
)
cOpticalMonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonDirection"),
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonLocation"),
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonParameterType"),
)
if mibBuilder.loadTexts:
    cOpticalMonEntry.setStatus("current")
_COpticalMonDirection_Type = OpticalIfDirection
_COpticalMonDirection_Object = MibTableColumn
cOpticalMonDirection = _COpticalMonDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 1),
    _COpticalMonDirection_Type()
)
cOpticalMonDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalMonDirection.setStatus("current")
_COpticalMonLocation_Type = OpticalIfMonLocation
_COpticalMonLocation_Object = MibTableColumn
cOpticalMonLocation = _COpticalMonLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 2),
    _COpticalMonLocation_Type()
)
cOpticalMonLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalMonLocation.setStatus("current")
_COpticalMonParameterType_Type = OpticalParameterType
_COpticalMonParameterType_Object = MibTableColumn
cOpticalMonParameterType = _COpticalMonParameterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 3),
    _COpticalMonParameterType_Type()
)
cOpticalMonParameterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalMonParameterType.setStatus("current")
_COpticalParameterValue_Type = OpticalParameterValue
_COpticalParameterValue_Object = MibTableColumn
cOpticalParameterValue = _COpticalParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 4),
    _COpticalParameterValue_Type()
)
cOpticalParameterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalParameterValue.setStatus("current")
_COpticalParamHighAlarmThresh_Type = OpticalParameterValue
_COpticalParamHighAlarmThresh_Object = MibTableColumn
cOpticalParamHighAlarmThresh = _COpticalParamHighAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 5),
    _COpticalParamHighAlarmThresh_Type()
)
cOpticalParamHighAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamHighAlarmThresh.setStatus("current")
_COpticalParamHighAlarmSev_Type = OpticalAlarmSeverity
_COpticalParamHighAlarmSev_Object = MibTableColumn
cOpticalParamHighAlarmSev = _COpticalParamHighAlarmSev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 6),
    _COpticalParamHighAlarmSev_Type()
)
cOpticalParamHighAlarmSev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamHighAlarmSev.setStatus("current")
_COpticalParamHighWarningThresh_Type = OpticalParameterValue
_COpticalParamHighWarningThresh_Object = MibTableColumn
cOpticalParamHighWarningThresh = _COpticalParamHighWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 7),
    _COpticalParamHighWarningThresh_Type()
)
cOpticalParamHighWarningThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamHighWarningThresh.setStatus("current")
_COpticalParamHighWarningSev_Type = OpticalAlarmSeverity
_COpticalParamHighWarningSev_Object = MibTableColumn
cOpticalParamHighWarningSev = _COpticalParamHighWarningSev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 8),
    _COpticalParamHighWarningSev_Type()
)
cOpticalParamHighWarningSev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamHighWarningSev.setStatus("current")
_COpticalParamLowAlarmThresh_Type = OpticalParameterValue
_COpticalParamLowAlarmThresh_Object = MibTableColumn
cOpticalParamLowAlarmThresh = _COpticalParamLowAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 9),
    _COpticalParamLowAlarmThresh_Type()
)
cOpticalParamLowAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamLowAlarmThresh.setStatus("current")
_COpticalParamLowAlarmSev_Type = OpticalAlarmSeverity
_COpticalParamLowAlarmSev_Object = MibTableColumn
cOpticalParamLowAlarmSev = _COpticalParamLowAlarmSev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 10),
    _COpticalParamLowAlarmSev_Type()
)
cOpticalParamLowAlarmSev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamLowAlarmSev.setStatus("current")
_COpticalParamLowWarningThresh_Type = OpticalParameterValue
_COpticalParamLowWarningThresh_Object = MibTableColumn
cOpticalParamLowWarningThresh = _COpticalParamLowWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 11),
    _COpticalParamLowWarningThresh_Type()
)
cOpticalParamLowWarningThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamLowWarningThresh.setStatus("current")
_COpticalParamLowWarningSev_Type = OpticalAlarmSeverity
_COpticalParamLowWarningSev_Object = MibTableColumn
cOpticalParamLowWarningSev = _COpticalParamLowWarningSev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 12),
    _COpticalParamLowWarningSev_Type()
)
cOpticalParamLowWarningSev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamLowWarningSev.setStatus("current")
_COpticalParamAlarmStatus_Type = OpticalAlarmStatus
_COpticalParamAlarmStatus_Object = MibTableColumn
cOpticalParamAlarmStatus = _COpticalParamAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 13),
    _COpticalParamAlarmStatus_Type()
)
cOpticalParamAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalParamAlarmStatus.setStatus("current")
_COpticalParamAlarmCurMaxThresh_Type = OpticalParameterValue
_COpticalParamAlarmCurMaxThresh_Object = MibTableColumn
cOpticalParamAlarmCurMaxThresh = _COpticalParamAlarmCurMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 14),
    _COpticalParamAlarmCurMaxThresh_Type()
)
cOpticalParamAlarmCurMaxThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalParamAlarmCurMaxThresh.setStatus("current")
_COpticalParamAlarmCurMaxSev_Type = OpticalAlarmSeverity
_COpticalParamAlarmCurMaxSev_Object = MibTableColumn
cOpticalParamAlarmCurMaxSev = _COpticalParamAlarmCurMaxSev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 15),
    _COpticalParamAlarmCurMaxSev_Type()
)
cOpticalParamAlarmCurMaxSev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalParamAlarmCurMaxSev.setStatus("current")
_COpticalParamAlarmLastChange_Type = TimeStamp
_COpticalParamAlarmLastChange_Object = MibTableColumn
cOpticalParamAlarmLastChange = _COpticalParamAlarmLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 16),
    _COpticalParamAlarmLastChange_Type()
)
cOpticalParamAlarmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalParamAlarmLastChange.setStatus("current")


class _COpticalMon15MinValidIntervals_Type(Unsigned32):
    """Custom type cOpticalMon15MinValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_COpticalMon15MinValidIntervals_Type.__name__ = "Unsigned32"
_COpticalMon15MinValidIntervals_Object = MibTableColumn
cOpticalMon15MinValidIntervals = _COpticalMon15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 17),
    _COpticalMon15MinValidIntervals_Type()
)
cOpticalMon15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalMon15MinValidIntervals.setStatus("current")


class _COpticalMon24HrValidIntervals_Type(Unsigned32):
    """Custom type cOpticalMon24HrValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_COpticalMon24HrValidIntervals_Type.__name__ = "Unsigned32"
_COpticalMon24HrValidIntervals_Object = MibTableColumn
cOpticalMon24HrValidIntervals = _COpticalMon24HrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 18),
    _COpticalMon24HrValidIntervals_Type()
)
cOpticalMon24HrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalMon24HrValidIntervals.setStatus("current")


class _COpticalParamThreshSource_Type(Bits):
    """Custom type cOpticalParamThreshSource based on Bits"""
    namedValues = NamedValues(
        *(("highAlarmDefThresh", 0),
          ("highWarnDefThresh", 1),
          ("lowAlarmDefThresh", 2),
          ("lowWarnDefThresh", 3))
    )

_COpticalParamThreshSource_Type.__name__ = "Bits"
_COpticalParamThreshSource_Object = MibTableColumn
cOpticalParamThreshSource = _COpticalParamThreshSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 19),
    _COpticalParamThreshSource_Type()
)
cOpticalParamThreshSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalParamThreshSource.setStatus("current")


class _COpticalNotifyEnable_Type(OpticalAlarmSeverityOrZero):
    """Custom type cOpticalNotifyEnable based on OpticalAlarmSeverityOrZero"""
    defaultValue = 0


_COpticalNotifyEnable_Object = MibScalar
cOpticalNotifyEnable = _COpticalNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 2),
    _COpticalNotifyEnable_Type()
)
cOpticalNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalNotifyEnable.setStatus("current")


class _COpticalMonEnable_Type(Bits):
    """Custom type cOpticalMonEnable based on Bits"""
    namedValues = NamedValues(
        ("all", 0)
    )

_COpticalMonEnable_Type.__name__ = "Bits"
_COpticalMonEnable_Object = MibScalar
cOpticalMonEnable = _COpticalMonEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 3),
    _COpticalMonEnable_Type()
)
cOpticalMonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalMonEnable.setStatus("current")
_COpticalMonPollInterval_Type = Unsigned32
_COpticalMonPollInterval_Object = MibScalar
cOpticalMonPollInterval = _COpticalMonPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 4),
    _COpticalMonPollInterval_Type()
)
cOpticalMonPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOpticalMonPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    cOpticalMonPollInterval.setUnits("minutes")
_COpticalMonIfTable_Object = MibTable
cOpticalMonIfTable = _COpticalMonIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cOpticalMonIfTable.setStatus("current")
_COpticalMonIfEntry_Object = MibTableRow
cOpticalMonIfEntry = _COpticalMonIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 5, 1)
)
cOpticalMonIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cOpticalMonIfEntry.setStatus("current")
_COpticalMonIfTimeInSlot_Type = Unsigned32
_COpticalMonIfTimeInSlot_Object = MibTableColumn
cOpticalMonIfTimeInSlot = _COpticalMonIfTimeInSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 5, 1, 1),
    _COpticalMonIfTimeInSlot_Type()
)
cOpticalMonIfTimeInSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalMonIfTimeInSlot.setStatus("current")
if mibBuilder.loadTexts:
    cOpticalMonIfTimeInSlot.setUnits("seconds")
_COpticalPMGroup_ObjectIdentity = ObjectIdentity
cOpticalPMGroup = _COpticalPMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2)
)
_COpticalPMCurrentTable_Object = MibTable
cOpticalPMCurrentTable = _COpticalPMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cOpticalPMCurrentTable.setStatus("current")
_COpticalPMCurrentEntry_Object = MibTableRow
cOpticalPMCurrentEntry = _COpticalPMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1)
)
cOpticalPMCurrentEntry.setIndexNames(
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentPeriod"),
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentDirection"),
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentLocation"),
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentParamType"),
)
if mibBuilder.loadTexts:
    cOpticalPMCurrentEntry.setStatus("current")
_COpticalPMCurrentPeriod_Type = OpticalPMPeriod
_COpticalPMCurrentPeriod_Object = MibTableColumn
cOpticalPMCurrentPeriod = _COpticalPMCurrentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 1),
    _COpticalPMCurrentPeriod_Type()
)
cOpticalPMCurrentPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMCurrentPeriod.setStatus("current")
_COpticalPMCurrentDirection_Type = OpticalIfDirection
_COpticalPMCurrentDirection_Object = MibTableColumn
cOpticalPMCurrentDirection = _COpticalPMCurrentDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 2),
    _COpticalPMCurrentDirection_Type()
)
cOpticalPMCurrentDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMCurrentDirection.setStatus("current")
_COpticalPMCurrentLocation_Type = OpticalIfMonLocation
_COpticalPMCurrentLocation_Object = MibTableColumn
cOpticalPMCurrentLocation = _COpticalPMCurrentLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 3),
    _COpticalPMCurrentLocation_Type()
)
cOpticalPMCurrentLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMCurrentLocation.setStatus("current")
_COpticalPMCurrentParamType_Type = OpticalParameterType
_COpticalPMCurrentParamType_Object = MibTableColumn
cOpticalPMCurrentParamType = _COpticalPMCurrentParamType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 4),
    _COpticalPMCurrentParamType_Type()
)
cOpticalPMCurrentParamType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMCurrentParamType.setStatus("current")
_COpticalPMCurrentMaxParam_Type = OpticalParameterValue
_COpticalPMCurrentMaxParam_Object = MibTableColumn
cOpticalPMCurrentMaxParam = _COpticalPMCurrentMaxParam_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 5),
    _COpticalPMCurrentMaxParam_Type()
)
cOpticalPMCurrentMaxParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMCurrentMaxParam.setStatus("current")
_COpticalPMCurrentMinParam_Type = OpticalParameterValue
_COpticalPMCurrentMinParam_Object = MibTableColumn
cOpticalPMCurrentMinParam = _COpticalPMCurrentMinParam_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 6),
    _COpticalPMCurrentMinParam_Type()
)
cOpticalPMCurrentMinParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMCurrentMinParam.setStatus("current")
_COpticalPMCurrentMeanParam_Type = OpticalParameterValue
_COpticalPMCurrentMeanParam_Object = MibTableColumn
cOpticalPMCurrentMeanParam = _COpticalPMCurrentMeanParam_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 7),
    _COpticalPMCurrentMeanParam_Type()
)
cOpticalPMCurrentMeanParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMCurrentMeanParam.setStatus("current")


class _COpticalPMCurrentUnavailSecs_Type(Integer32):
    """Custom type cOpticalPMCurrentUnavailSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_COpticalPMCurrentUnavailSecs_Type.__name__ = "Integer32"
_COpticalPMCurrentUnavailSecs_Object = MibTableColumn
cOpticalPMCurrentUnavailSecs = _COpticalPMCurrentUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 8),
    _COpticalPMCurrentUnavailSecs_Type()
)
cOpticalPMCurrentUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMCurrentUnavailSecs.setStatus("current")
_COpticalPMIntervalTable_Object = MibTable
cOpticalPMIntervalTable = _COpticalPMIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cOpticalPMIntervalTable.setStatus("current")
_COpticalPMIntervalEntry_Object = MibTableRow
cOpticalPMIntervalEntry = _COpticalPMIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1)
)
cOpticalPMIntervalEntry.setIndexNames(
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalPeriod"),
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalNumber"),
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalDirection"),
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalLocation"),
    (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalParamType"),
)
if mibBuilder.loadTexts:
    cOpticalPMIntervalEntry.setStatus("current")
_COpticalPMIntervalPeriod_Type = OpticalPMPeriod
_COpticalPMIntervalPeriod_Object = MibTableColumn
cOpticalPMIntervalPeriod = _COpticalPMIntervalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 1),
    _COpticalPMIntervalPeriod_Type()
)
cOpticalPMIntervalPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMIntervalPeriod.setStatus("current")


class _COpticalPMIntervalNumber_Type(Integer32):
    """Custom type cOpticalPMIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_COpticalPMIntervalNumber_Type.__name__ = "Integer32"
_COpticalPMIntervalNumber_Object = MibTableColumn
cOpticalPMIntervalNumber = _COpticalPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 2),
    _COpticalPMIntervalNumber_Type()
)
cOpticalPMIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMIntervalNumber.setStatus("current")
_COpticalPMIntervalDirection_Type = OpticalIfDirection
_COpticalPMIntervalDirection_Object = MibTableColumn
cOpticalPMIntervalDirection = _COpticalPMIntervalDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 3),
    _COpticalPMIntervalDirection_Type()
)
cOpticalPMIntervalDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMIntervalDirection.setStatus("current")
_COpticalPMIntervalLocation_Type = OpticalIfMonLocation
_COpticalPMIntervalLocation_Object = MibTableColumn
cOpticalPMIntervalLocation = _COpticalPMIntervalLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 4),
    _COpticalPMIntervalLocation_Type()
)
cOpticalPMIntervalLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMIntervalLocation.setStatus("current")
_COpticalPMIntervalParamType_Type = OpticalParameterType
_COpticalPMIntervalParamType_Object = MibTableColumn
cOpticalPMIntervalParamType = _COpticalPMIntervalParamType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 5),
    _COpticalPMIntervalParamType_Type()
)
cOpticalPMIntervalParamType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOpticalPMIntervalParamType.setStatus("current")
_COpticalPMIntervalMaxParam_Type = OpticalParameterValue
_COpticalPMIntervalMaxParam_Object = MibTableColumn
cOpticalPMIntervalMaxParam = _COpticalPMIntervalMaxParam_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 6),
    _COpticalPMIntervalMaxParam_Type()
)
cOpticalPMIntervalMaxParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMIntervalMaxParam.setStatus("current")
_COpticalPMIntervalMinParam_Type = OpticalParameterValue
_COpticalPMIntervalMinParam_Object = MibTableColumn
cOpticalPMIntervalMinParam = _COpticalPMIntervalMinParam_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 7),
    _COpticalPMIntervalMinParam_Type()
)
cOpticalPMIntervalMinParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMIntervalMinParam.setStatus("current")
_COpticalPMIntervalMeanParam_Type = OpticalParameterValue
_COpticalPMIntervalMeanParam_Object = MibTableColumn
cOpticalPMIntervalMeanParam = _COpticalPMIntervalMeanParam_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 8),
    _COpticalPMIntervalMeanParam_Type()
)
cOpticalPMIntervalMeanParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMIntervalMeanParam.setStatus("current")


class _COpticalPMIntervalUnavailSecs_Type(Integer32):
    """Custom type cOpticalPMIntervalUnavailSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_COpticalPMIntervalUnavailSecs_Type.__name__ = "Integer32"
_COpticalPMIntervalUnavailSecs_Object = MibTableColumn
cOpticalPMIntervalUnavailSecs = _COpticalPMIntervalUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 9),
    _COpticalPMIntervalUnavailSecs_Type()
)
cOpticalPMIntervalUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOpticalPMIntervalUnavailSecs.setStatus("current")
_COpticalMonitorMIBNotifications_ObjectIdentity = ObjectIdentity
cOpticalMonitorMIBNotifications = _COpticalMonitorMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 2)
)
_COpticalMonNotificationPrefix_ObjectIdentity = ObjectIdentity
cOpticalMonNotificationPrefix = _COpticalMonNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 2, 0)
)
_COpticalMonitorMIBConformance_ObjectIdentity = ObjectIdentity
cOpticalMonitorMIBConformance = _COpticalMonitorMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3)
)
_COpticalMonitorMIBCompliances_ObjectIdentity = ObjectIdentity
cOpticalMonitorMIBCompliances = _COpticalMonitorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 1)
)
_COpticalMonitorMIBGroups_ObjectIdentity = ObjectIdentity
cOpticalMonitorMIBGroups = _COpticalMonitorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2)
)

# Managed Objects groups

cOpticalMIBMonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 1)
)
cOpticalMIBMonGroup.setObjects(
    ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParameterValue")
)
if mibBuilder.loadTexts:
    cOpticalMIBMonGroup.setStatus("current")

cOpticalMIBThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 2)
)
cOpticalMIBThresholdGroup.setObjects(
      *(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighAlarmThresh"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighWarningThresh"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowAlarmThresh"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowWarningThresh"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmStatus"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxThresh"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmLastChange"))
)
if mibBuilder.loadTexts:
    cOpticalMIBThresholdGroup.setStatus("current")

cOpticalMIBSeverityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 3)
)
cOpticalMIBSeverityGroup.setObjects(
      *(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighAlarmSev"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighWarningSev"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowAlarmSev"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowWarningSev"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxSev"))
)
if mibBuilder.loadTexts:
    cOpticalMIBSeverityGroup.setStatus("current")

cOpticalMIBPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 4)
)
cOpticalMIBPMGroup.setObjects(
      *(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMon15MinValidIntervals"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMon24HrValidIntervals"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMaxParam"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMinParam"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMeanParam"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentUnavailSecs"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMaxParam"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMinParam"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMeanParam"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalUnavailSecs"))
)
if mibBuilder.loadTexts:
    cOpticalMIBPMGroup.setStatus("current")

cOpticalMIBNotifyEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 5)
)
cOpticalMIBNotifyEnableGroup.setObjects(
    ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalNotifyEnable")
)
if mibBuilder.loadTexts:
    cOpticalMIBNotifyEnableGroup.setStatus("current")

cOpticalMonIfTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 7)
)
cOpticalMonIfTimeGroup.setObjects(
    ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonIfTimeInSlot")
)
if mibBuilder.loadTexts:
    cOpticalMonIfTimeGroup.setStatus("current")

cOpticalMIBEnableConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 8)
)
cOpticalMIBEnableConfigGroup.setObjects(
    ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonEnable")
)
if mibBuilder.loadTexts:
    cOpticalMIBEnableConfigGroup.setStatus("current")

cOpticalMIBIntervalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 9)
)
cOpticalMIBIntervalConfigGroup.setObjects(
    ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonPollInterval")
)
if mibBuilder.loadTexts:
    cOpticalMIBIntervalConfigGroup.setStatus("current")

cOpticalMonThreshSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 10)
)
cOpticalMonThreshSourceGroup.setObjects(
    ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamThreshSource")
)
if mibBuilder.loadTexts:
    cOpticalMonThreshSourceGroup.setStatus("current")


# Notification objects

cOpticalMonParameterStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 2, 0, 1)
)
cOpticalMonParameterStatus.setObjects(
      *(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParameterValue"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmStatus"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxThresh"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxSev"),
        ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmLastChange"))
)
if mibBuilder.loadTexts:
    cOpticalMonParameterStatus.setStatus(
        "current"
    )


# Notifications groups

cOpticalMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 6)
)
cOpticalMIBNotifGroup.setObjects(
    ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonParameterStatus")
)
if mibBuilder.loadTexts:
    cOpticalMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cOpticalMonitorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cOpticalMonitorMIBCompliance.setStatus(
        "deprecated"
    )

cOpticalMonitorMIBComplianceRev = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cOpticalMonitorMIBComplianceRev.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OPTICAL-MONITOR-MIB",
    **{"OpticalParameterType": OpticalParameterType,
       "OpticalParameterValue": OpticalParameterValue,
       "OpticalIfDirection": OpticalIfDirection,
       "OpticalIfMonLocation": OpticalIfMonLocation,
       "OpticalAlarmStatus": OpticalAlarmStatus,
       "OpticalAlarmSeverity": OpticalAlarmSeverity,
       "OpticalAlarmSeverityOrZero": OpticalAlarmSeverityOrZero,
       "OpticalPMPeriod": OpticalPMPeriod,
       "ciscoOpticalMonitorMIB": ciscoOpticalMonitorMIB,
       "cOpticalMonitorMIBObjects": cOpticalMonitorMIBObjects,
       "cOpticalMonGroup": cOpticalMonGroup,
       "cOpticalMonTable": cOpticalMonTable,
       "cOpticalMonEntry": cOpticalMonEntry,
       "cOpticalMonDirection": cOpticalMonDirection,
       "cOpticalMonLocation": cOpticalMonLocation,
       "cOpticalMonParameterType": cOpticalMonParameterType,
       "cOpticalParameterValue": cOpticalParameterValue,
       "cOpticalParamHighAlarmThresh": cOpticalParamHighAlarmThresh,
       "cOpticalParamHighAlarmSev": cOpticalParamHighAlarmSev,
       "cOpticalParamHighWarningThresh": cOpticalParamHighWarningThresh,
       "cOpticalParamHighWarningSev": cOpticalParamHighWarningSev,
       "cOpticalParamLowAlarmThresh": cOpticalParamLowAlarmThresh,
       "cOpticalParamLowAlarmSev": cOpticalParamLowAlarmSev,
       "cOpticalParamLowWarningThresh": cOpticalParamLowWarningThresh,
       "cOpticalParamLowWarningSev": cOpticalParamLowWarningSev,
       "cOpticalParamAlarmStatus": cOpticalParamAlarmStatus,
       "cOpticalParamAlarmCurMaxThresh": cOpticalParamAlarmCurMaxThresh,
       "cOpticalParamAlarmCurMaxSev": cOpticalParamAlarmCurMaxSev,
       "cOpticalParamAlarmLastChange": cOpticalParamAlarmLastChange,
       "cOpticalMon15MinValidIntervals": cOpticalMon15MinValidIntervals,
       "cOpticalMon24HrValidIntervals": cOpticalMon24HrValidIntervals,
       "cOpticalParamThreshSource": cOpticalParamThreshSource,
       "cOpticalNotifyEnable": cOpticalNotifyEnable,
       "cOpticalMonEnable": cOpticalMonEnable,
       "cOpticalMonPollInterval": cOpticalMonPollInterval,
       "cOpticalMonIfTable": cOpticalMonIfTable,
       "cOpticalMonIfEntry": cOpticalMonIfEntry,
       "cOpticalMonIfTimeInSlot": cOpticalMonIfTimeInSlot,
       "cOpticalPMGroup": cOpticalPMGroup,
       "cOpticalPMCurrentTable": cOpticalPMCurrentTable,
       "cOpticalPMCurrentEntry": cOpticalPMCurrentEntry,
       "cOpticalPMCurrentPeriod": cOpticalPMCurrentPeriod,
       "cOpticalPMCurrentDirection": cOpticalPMCurrentDirection,
       "cOpticalPMCurrentLocation": cOpticalPMCurrentLocation,
       "cOpticalPMCurrentParamType": cOpticalPMCurrentParamType,
       "cOpticalPMCurrentMaxParam": cOpticalPMCurrentMaxParam,
       "cOpticalPMCurrentMinParam": cOpticalPMCurrentMinParam,
       "cOpticalPMCurrentMeanParam": cOpticalPMCurrentMeanParam,
       "cOpticalPMCurrentUnavailSecs": cOpticalPMCurrentUnavailSecs,
       "cOpticalPMIntervalTable": cOpticalPMIntervalTable,
       "cOpticalPMIntervalEntry": cOpticalPMIntervalEntry,
       "cOpticalPMIntervalPeriod": cOpticalPMIntervalPeriod,
       "cOpticalPMIntervalNumber": cOpticalPMIntervalNumber,
       "cOpticalPMIntervalDirection": cOpticalPMIntervalDirection,
       "cOpticalPMIntervalLocation": cOpticalPMIntervalLocation,
       "cOpticalPMIntervalParamType": cOpticalPMIntervalParamType,
       "cOpticalPMIntervalMaxParam": cOpticalPMIntervalMaxParam,
       "cOpticalPMIntervalMinParam": cOpticalPMIntervalMinParam,
       "cOpticalPMIntervalMeanParam": cOpticalPMIntervalMeanParam,
       "cOpticalPMIntervalUnavailSecs": cOpticalPMIntervalUnavailSecs,
       "cOpticalMonitorMIBNotifications": cOpticalMonitorMIBNotifications,
       "cOpticalMonNotificationPrefix": cOpticalMonNotificationPrefix,
       "cOpticalMonParameterStatus": cOpticalMonParameterStatus,
       "cOpticalMonitorMIBConformance": cOpticalMonitorMIBConformance,
       "cOpticalMonitorMIBCompliances": cOpticalMonitorMIBCompliances,
       "cOpticalMonitorMIBCompliance": cOpticalMonitorMIBCompliance,
       "cOpticalMonitorMIBComplianceRev": cOpticalMonitorMIBComplianceRev,
       "cOpticalMonitorMIBGroups": cOpticalMonitorMIBGroups,
       "cOpticalMIBMonGroup": cOpticalMIBMonGroup,
       "cOpticalMIBThresholdGroup": cOpticalMIBThresholdGroup,
       "cOpticalMIBSeverityGroup": cOpticalMIBSeverityGroup,
       "cOpticalMIBPMGroup": cOpticalMIBPMGroup,
       "cOpticalMIBNotifyEnableGroup": cOpticalMIBNotifyEnableGroup,
       "cOpticalMIBNotifGroup": cOpticalMIBNotifGroup,
       "cOpticalMonIfTimeGroup": cOpticalMonIfTimeGroup,
       "cOpticalMIBEnableConfigGroup": cOpticalMIBEnableConfigGroup,
       "cOpticalMIBIntervalConfigGroup": cOpticalMIBIntervalConfigGroup,
       "cOpticalMonThreshSourceGroup": cOpticalMonThreshSourceGroup}
)
