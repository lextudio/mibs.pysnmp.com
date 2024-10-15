# SNMP MIB module (ZHNSYSMON) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHNSYSMON
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:03 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")


# MODULE-IDENTITY

zhnSysMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1)
)
zhnSysMon.setRevisions(
        ("2010-09-24 00:00",
         "2010-06-21 00:00",
         "2009-12-14 00:00",
         "2009-05-20 00:00",
         "2009-04-06 00:00",
         "2009-01-06 00:00",
         "2008-05-21 00:00",
         "2007-11-26 00:00",
         "2006-12-26 00:00",
         "2006-12-12 00:00",
         "2006-11-17 00:00",
         "2006-08-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhnSysMonNotifications_ObjectIdentity = ObjectIdentity
zhnSysMonNotifications = _ZhnSysMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0)
)
_ZhnSysMonObjects_ObjectIdentity = ObjectIdentity
zhnSysMonObjects = _ZhnSysMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1)
)
_ZhnSysMonAlarmTable_Object = MibTable
zhnSysMonAlarmTable = _ZhnSysMonAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zhnSysMonAlarmTable.setStatus("current")
_ZhnSysMonAlarmEntry_Object = MibTableRow
zhnSysMonAlarmEntry = _ZhnSysMonAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1)
)
zhnSysMonAlarmEntry.setIndexNames(
    (0, "ZHNSYSMON", "zhnSysMonAlarmType"),
    (0, "ZHNSYSMON", "zhnSysMonAlarmSeverity"),
    (0, "ZHNSYSMON", "zhnSysMonAlarmInterfaceName"),
)
if mibBuilder.loadTexts:
    zhnSysMonAlarmEntry.setStatus("current")


class _ZhnSysMonAlarmType_Type(Integer32):
    """Custom type zhnSysMonAlarmType based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("batteryPowerLow", 30),
          ("batteryPowerLow2", 34),
          ("batteryRemoved", 32),
          ("batteryRemoved2", 36),
          ("doorOpened", 37),
          ("dsx1LoopbackState", 21),
          ("dsx1LossOfFrame", 19),
          ("dsx1LossOfSignal", 20),
          ("dsx1RcvAIS", 17),
          ("dsx1RcvYellow", 15),
          ("dsx1TestingState", 22),
          ("dsx1XmtAIS", 18),
          ("dsx1XmtYellow", 16),
          ("interfaceDown", 6),
          ("lowPowerMode", 4),
          ("mainPowerLoss", 2),
          ("onBatteryPower", 29),
          ("onBatteryPower2", 33),
          ("other", 99),
          ("processFailed", 7),
          ("pwClockHoldover", 24),
          ("pwClockStability", 23),
          ("pwClockStabilityAcquisition", 26),
          ("pwClockStabilityIdle", 25),
          ("pwClockStabilityRecovery", 28),
          ("pwClockStabilityTracking1", 27),
          ("pwDeleted", 9),
          ("pwDown", 8),
          ("pwJitterBufferOverrun", 14),
          ("pwLOP", 11),
          ("pwLateFrame", 12),
          ("pwMalformedFrame", 13),
          ("pwMisconnected", 10),
          ("replaceBattery", 31),
          ("replaceBattery2", 35),
          ("secondaryPowerLoss", 3),
          ("selftestFailed", 5),
          ("tempThresholdExceeded", 1))
    )


_ZhnSysMonAlarmType_Type.__name__ = "Integer32"
_ZhnSysMonAlarmType_Object = MibTableColumn
zhnSysMonAlarmType = _ZhnSysMonAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1, 1),
    _ZhnSysMonAlarmType_Type()
)
zhnSysMonAlarmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonAlarmType.setStatus("current")


class _ZhnSysMonAlarmSeverity_Type(Integer32):
    """Custom type zhnSysMonAlarmSeverity based on Integer32"""
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
        *(("critical", 3),
          ("major", 2),
          ("minor", 1),
          ("wanData", 4))
    )


_ZhnSysMonAlarmSeverity_Type.__name__ = "Integer32"
_ZhnSysMonAlarmSeverity_Object = MibTableColumn
zhnSysMonAlarmSeverity = _ZhnSysMonAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1, 2),
    _ZhnSysMonAlarmSeverity_Type()
)
zhnSysMonAlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonAlarmSeverity.setStatus("current")


class _ZhnSysMonAlarmInterfaceName_Type(DisplayString):
    """Custom type zhnSysMonAlarmInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ZhnSysMonAlarmInterfaceName_Type.__name__ = "DisplayString"
_ZhnSysMonAlarmInterfaceName_Object = MibTableColumn
zhnSysMonAlarmInterfaceName = _ZhnSysMonAlarmInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1, 3),
    _ZhnSysMonAlarmInterfaceName_Type()
)
zhnSysMonAlarmInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonAlarmInterfaceName.setStatus("current")


class _ZhnSysMonAlarmDescription_Type(DisplayString):
    """Custom type zhnSysMonAlarmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ZhnSysMonAlarmDescription_Type.__name__ = "DisplayString"
_ZhnSysMonAlarmDescription_Object = MibTableColumn
zhnSysMonAlarmDescription = _ZhnSysMonAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1, 4),
    _ZhnSysMonAlarmDescription_Type()
)
zhnSysMonAlarmDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonAlarmDescription.setStatus("current")
_ZhnSysMonAlarmRowStatus_Type = RowStatus
_ZhnSysMonAlarmRowStatus_Object = MibTableColumn
zhnSysMonAlarmRowStatus = _ZhnSysMonAlarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1, 5),
    _ZhnSysMonAlarmRowStatus_Type()
)
zhnSysMonAlarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonAlarmRowStatus.setStatus("current")
_ZhnSysMonTestTable_Object = MibTable
zhnSysMonTestTable = _ZhnSysMonTestTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zhnSysMonTestTable.setStatus("current")
_ZhnSysMonTestEntry_Object = MibTableRow
zhnSysMonTestEntry = _ZhnSysMonTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 2, 1)
)
zhnSysMonTestEntry.setIndexNames(
    (0, "ZHNSYSMON", "zhnSysMonTestType"),
    (0, "ZHNSYSMON", "zhnSysMonTestInterfaceName"),
)
if mibBuilder.loadTexts:
    zhnSysMonTestEntry.setStatus("current")


class _ZhnSysMonTestType_Type(Integer32):
    """Custom type zhnSysMonTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("led", 2),
          ("loopback", 1))
    )


_ZhnSysMonTestType_Type.__name__ = "Integer32"
_ZhnSysMonTestType_Object = MibTableColumn
zhnSysMonTestType = _ZhnSysMonTestType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 2, 1, 1),
    _ZhnSysMonTestType_Type()
)
zhnSysMonTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonTestType.setStatus("current")


class _ZhnSysMonTestInterfaceName_Type(DisplayString):
    """Custom type zhnSysMonTestInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ZhnSysMonTestInterfaceName_Type.__name__ = "DisplayString"
_ZhnSysMonTestInterfaceName_Object = MibTableColumn
zhnSysMonTestInterfaceName = _ZhnSysMonTestInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 2, 1, 2),
    _ZhnSysMonTestInterfaceName_Type()
)
zhnSysMonTestInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonTestInterfaceName.setStatus("current")
_ZhnSysMonTestRowStatus_Type = RowStatus
_ZhnSysMonTestRowStatus_Object = MibTableColumn
zhnSysMonTestRowStatus = _ZhnSysMonTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 2, 1, 3),
    _ZhnSysMonTestRowStatus_Type()
)
zhnSysMonTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonTestRowStatus.setStatus("current")
_ZhnSysMonTempSensorTable_Object = MibTable
zhnSysMonTempSensorTable = _ZhnSysMonTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    zhnSysMonTempSensorTable.setStatus("current")
_ZhnSysMonTempSensorEntry_Object = MibTableRow
zhnSysMonTempSensorEntry = _ZhnSysMonTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1)
)
zhnSysMonTempSensorEntry.setIndexNames(
    (0, "ZHNSYSMON", "zhnSysMonTempSensorId"),
)
if mibBuilder.loadTexts:
    zhnSysMonTempSensorEntry.setStatus("current")


class _ZhnSysMonTempSensorId_Type(Unsigned32):
    """Custom type zhnSysMonTempSensorId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_ZhnSysMonTempSensorId_Type.__name__ = "Unsigned32"
_ZhnSysMonTempSensorId_Object = MibTableColumn
zhnSysMonTempSensorId = _ZhnSysMonTempSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 1),
    _ZhnSysMonTempSensorId_Type()
)
zhnSysMonTempSensorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonTempSensorId.setStatus("current")
_ZhnSysMonTempSensorRowStatus_Type = RowStatus
_ZhnSysMonTempSensorRowStatus_Object = MibTableColumn
zhnSysMonTempSensorRowStatus = _ZhnSysMonTempSensorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 2),
    _ZhnSysMonTempSensorRowStatus_Type()
)
zhnSysMonTempSensorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonTempSensorRowStatus.setStatus("current")


class _ZhnSysMonTempSensorCurr_Type(DisplayString):
    """Custom type zhnSysMonTempSensorCurr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZhnSysMonTempSensorCurr_Type.__name__ = "DisplayString"
_ZhnSysMonTempSensorCurr_Object = MibTableColumn
zhnSysMonTempSensorCurr = _ZhnSysMonTempSensorCurr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 3),
    _ZhnSysMonTempSensorCurr_Type()
)
zhnSysMonTempSensorCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnSysMonTempSensorCurr.setStatus("current")


class _ZhnSysMonTempSensorOS_Type(DisplayString):
    """Custom type zhnSysMonTempSensorOS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZhnSysMonTempSensorOS_Type.__name__ = "DisplayString"
_ZhnSysMonTempSensorOS_Object = MibTableColumn
zhnSysMonTempSensorOS = _ZhnSysMonTempSensorOS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 4),
    _ZhnSysMonTempSensorOS_Type()
)
zhnSysMonTempSensorOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnSysMonTempSensorOS.setStatus("current")


class _ZhnSysMonTempSensorHyst_Type(DisplayString):
    """Custom type zhnSysMonTempSensorHyst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZhnSysMonTempSensorHyst_Type.__name__ = "DisplayString"
_ZhnSysMonTempSensorHyst_Object = MibTableColumn
zhnSysMonTempSensorHyst = _ZhnSysMonTempSensorHyst_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 5),
    _ZhnSysMonTempSensorHyst_Type()
)
zhnSysMonTempSensorHyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnSysMonTempSensorHyst.setStatus("current")


class _ZhnSysMonTempSensorName_Type(DisplayString):
    """Custom type zhnSysMonTempSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZhnSysMonTempSensorName_Type.__name__ = "DisplayString"
_ZhnSysMonTempSensorName_Object = MibTableColumn
zhnSysMonTempSensorName = _ZhnSysMonTempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 6),
    _ZhnSysMonTempSensorName_Type()
)
zhnSysMonTempSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnSysMonTempSensorName.setStatus("current")
_ZhnSysMonLinePowerTable_Object = MibTable
zhnSysMonLinePowerTable = _ZhnSysMonLinePowerTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    zhnSysMonLinePowerTable.setStatus("current")
_ZhnSysMonLinePowerEntry_Object = MibTableRow
zhnSysMonLinePowerEntry = _ZhnSysMonLinePowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 4, 1)
)
zhnSysMonLinePowerEntry.setIndexNames(
    (0, "ZHNSYSMON", "zhnSysMonLinePowerLineNumber"),
)
if mibBuilder.loadTexts:
    zhnSysMonLinePowerEntry.setStatus("current")


class _ZhnSysMonLinePowerLineNumber_Type(Unsigned32):
    """Custom type zhnSysMonLinePowerLineNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_ZhnSysMonLinePowerLineNumber_Type.__name__ = "Unsigned32"
_ZhnSysMonLinePowerLineNumber_Object = MibTableColumn
zhnSysMonLinePowerLineNumber = _ZhnSysMonLinePowerLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 4, 1, 1),
    _ZhnSysMonLinePowerLineNumber_Type()
)
zhnSysMonLinePowerLineNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonLinePowerLineNumber.setStatus("current")


class _ZhnSysMonLinePowerStatus_Type(Integer32):
    """Custom type zhnSysMonLinePowerStatus based on Integer32"""
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


_ZhnSysMonLinePowerStatus_Type.__name__ = "Integer32"
_ZhnSysMonLinePowerStatus_Object = MibTableColumn
zhnSysMonLinePowerStatus = _ZhnSysMonLinePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 4, 1, 2),
    _ZhnSysMonLinePowerStatus_Type()
)
zhnSysMonLinePowerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonLinePowerStatus.setStatus("current")
_ZhnSysMonLinePowerRowStatus_Type = RowStatus
_ZhnSysMonLinePowerRowStatus_Object = MibTableColumn
zhnSysMonLinePowerRowStatus = _ZhnSysMonLinePowerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 4, 1, 3),
    _ZhnSysMonLinePowerRowStatus_Type()
)
zhnSysMonLinePowerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnSysMonLinePowerRowStatus.setStatus("current")
_ZhnSysMonConformance_ObjectIdentity = ObjectIdentity
zhnSysMonConformance = _ZhnSysMonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 2)
)

# Managed Objects groups


# Notification objects

zhnSysMonAlarmSetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 1)
)
zhnSysMonAlarmSetEvent.setObjects(
      *(("ZHNSYSMON", "zhnSysMonAlarmType"),
        ("ZHNSYSMON", "zhnSysMonAlarmSeverity"),
        ("ZHNSYSMON", "zhnSysMonAlarmInterfaceName"),
        ("ZHNSYSMON", "zhnSysMonAlarmDescription"))
)
if mibBuilder.loadTexts:
    zhnSysMonAlarmSetEvent.setStatus(
        "current"
    )

zhnSysMonAlarmClearEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 2)
)
zhnSysMonAlarmClearEvent.setObjects(
      *(("ZHNSYSMON", "zhnSysMonAlarmType"),
        ("ZHNSYSMON", "zhnSysMonAlarmSeverity"),
        ("ZHNSYSMON", "zhnSysMonAlarmInterfaceName"),
        ("ZHNSYSMON", "zhnSysMonAlarmDescription"))
)
if mibBuilder.loadTexts:
    zhnSysMonAlarmClearEvent.setStatus(
        "current"
    )

zhnSysMonTestStartEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 3)
)
zhnSysMonTestStartEvent.setObjects(
      *(("ZHNSYSMON", "zhnSysMonTestType"),
        ("ZHNSYSMON", "zhnSysMonTestInterfaceName"))
)
if mibBuilder.loadTexts:
    zhnSysMonTestStartEvent.setStatus(
        "current"
    )

zhnSysMonTestStopEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 4)
)
zhnSysMonTestStopEvent.setObjects(
      *(("ZHNSYSMON", "zhnSysMonTestType"),
        ("ZHNSYSMON", "zhnSysMonTestInterfaceName"))
)
if mibBuilder.loadTexts:
    zhnSysMonTestStopEvent.setStatus(
        "current"
    )

zhnSysMonTempSensorCfgUpdateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 5)
)
zhnSysMonTempSensorCfgUpdateEvent.setObjects(
      *(("ZHNSYSMON", "zhnSysMonTempSensorId"),
        ("ZHNSYSMON", "zhnSysMonTempSensorOS"),
        ("ZHNSYSMON", "zhnSysMonTempSensorHyst"))
)
if mibBuilder.loadTexts:
    zhnSysMonTempSensorCfgUpdateEvent.setStatus(
        "current"
    )

zhnSysMonLinePowerCfgUpdateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 6)
)
zhnSysMonLinePowerCfgUpdateEvent.setObjects(
      *(("ZHNSYSMON", "zhnSysMonLinePowerLineNumber"),
        ("ZHNSYSMON", "zhnSysMonLinePowerStatus"))
)
if mibBuilder.loadTexts:
    zhnSysMonLinePowerCfgUpdateEvent.setStatus(
        "current"
    )

zhnSysMonReadyEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 7)
)
if mibBuilder.loadTexts:
    zhnSysMonReadyEvent.setStatus(
        "current"
    )

zhnSysMonConfigChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 8)
)
if mibBuilder.loadTexts:
    zhnSysMonConfigChangeEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNSYSMON",
    **{"zhnSysMon": zhnSysMon,
       "zhnSysMonNotifications": zhnSysMonNotifications,
       "zhnSysMonAlarmSetEvent": zhnSysMonAlarmSetEvent,
       "zhnSysMonAlarmClearEvent": zhnSysMonAlarmClearEvent,
       "zhnSysMonTestStartEvent": zhnSysMonTestStartEvent,
       "zhnSysMonTestStopEvent": zhnSysMonTestStopEvent,
       "zhnSysMonTempSensorCfgUpdateEvent": zhnSysMonTempSensorCfgUpdateEvent,
       "zhnSysMonLinePowerCfgUpdateEvent": zhnSysMonLinePowerCfgUpdateEvent,
       "zhnSysMonReadyEvent": zhnSysMonReadyEvent,
       "zhnSysMonConfigChangeEvent": zhnSysMonConfigChangeEvent,
       "zhnSysMonObjects": zhnSysMonObjects,
       "zhnSysMonAlarmTable": zhnSysMonAlarmTable,
       "zhnSysMonAlarmEntry": zhnSysMonAlarmEntry,
       "zhnSysMonAlarmType": zhnSysMonAlarmType,
       "zhnSysMonAlarmSeverity": zhnSysMonAlarmSeverity,
       "zhnSysMonAlarmInterfaceName": zhnSysMonAlarmInterfaceName,
       "zhnSysMonAlarmDescription": zhnSysMonAlarmDescription,
       "zhnSysMonAlarmRowStatus": zhnSysMonAlarmRowStatus,
       "zhnSysMonTestTable": zhnSysMonTestTable,
       "zhnSysMonTestEntry": zhnSysMonTestEntry,
       "zhnSysMonTestType": zhnSysMonTestType,
       "zhnSysMonTestInterfaceName": zhnSysMonTestInterfaceName,
       "zhnSysMonTestRowStatus": zhnSysMonTestRowStatus,
       "zhnSysMonTempSensorTable": zhnSysMonTempSensorTable,
       "zhnSysMonTempSensorEntry": zhnSysMonTempSensorEntry,
       "zhnSysMonTempSensorId": zhnSysMonTempSensorId,
       "zhnSysMonTempSensorRowStatus": zhnSysMonTempSensorRowStatus,
       "zhnSysMonTempSensorCurr": zhnSysMonTempSensorCurr,
       "zhnSysMonTempSensorOS": zhnSysMonTempSensorOS,
       "zhnSysMonTempSensorHyst": zhnSysMonTempSensorHyst,
       "zhnSysMonTempSensorName": zhnSysMonTempSensorName,
       "zhnSysMonLinePowerTable": zhnSysMonLinePowerTable,
       "zhnSysMonLinePowerEntry": zhnSysMonLinePowerEntry,
       "zhnSysMonLinePowerLineNumber": zhnSysMonLinePowerLineNumber,
       "zhnSysMonLinePowerStatus": zhnSysMonLinePowerStatus,
       "zhnSysMonLinePowerRowStatus": zhnSysMonLinePowerRowStatus,
       "zhnSysMonConformance": zhnSysMonConformance}
)
