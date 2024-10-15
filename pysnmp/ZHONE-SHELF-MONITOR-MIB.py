# SNMP MIB module (ZHONE-SHELF-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-SHELF-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:46 2024
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(zhoneModules,
 zhoneShelf,
 zhoneShelfIndex,
 zhoneSlotIndex) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhoneShelf",
    "zhoneShelfIndex",
    "zhoneSlotIndex")

(ZhoneAdminString,
 ZhoneCardLineType,
 ZhoneCardType) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneCardLineType",
    "ZhoneCardType")


# MODULE-IDENTITY

zhoneShelfMonitorModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 7)
)
zhoneShelfMonitorModule.setRevisions(
        ("2011-12-02 11:14",
         "2011-05-24 10:25",
         "2010-08-10 15:08",
         "2006-08-31 10:58",
         "2004-05-11 22:03",
         "2003-10-28 15:31",
         "2003-09-17 18:56",
         "2003-07-16 16:30",
         "2002-08-19 10:02",
         "2002-07-09 10:36",
         "2002-05-28 18:08",
         "2002-02-12 09:54",
         "2001-09-10 18:34",
         "2001-09-10 16:16",
         "2000-10-24 16:18",
         "2000-10-13 16:42",
         "2000-09-27 16:25",
         "2000-09-12 11:26")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ShelfDataTable_Object = MibTable
shelfDataTable = _ShelfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1)
)
if mibBuilder.loadTexts:
    shelfDataTable.setStatus("current")
_ShelfDataEntry_Object = MibTableRow
shelfDataEntry = _ShelfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1)
)
shelfDataEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
)
if mibBuilder.loadTexts:
    shelfDataEntry.setStatus("current")
_ShelfMfgCLEICode_Type = ZhoneAdminString
_ShelfMfgCLEICode_Object = MibTableColumn
shelfMfgCLEICode = _ShelfMfgCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1, 1),
    _ShelfMfgCLEICode_Type()
)
shelfMfgCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfMfgCLEICode.setStatus("current")
_ShelfMonitorSerialNumber_Type = ZhoneAdminString
_ShelfMonitorSerialNumber_Object = MibTableColumn
shelfMonitorSerialNumber = _ShelfMonitorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1, 2),
    _ShelfMonitorSerialNumber_Type()
)
shelfMonitorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfMonitorSerialNumber.setStatus("current")
_ShelfMonitorRevisionCode_Type = ZhoneAdminString
_ShelfMonitorRevisionCode_Object = MibTableColumn
shelfMonitorRevisionCode = _ShelfMonitorRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1, 3),
    _ShelfMonitorRevisionCode_Type()
)
shelfMonitorRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfMonitorRevisionCode.setStatus("current")
_ShelfBkplaneSerialNumber_Type = ZhoneAdminString
_ShelfBkplaneSerialNumber_Object = MibTableColumn
shelfBkplaneSerialNumber = _ShelfBkplaneSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1, 4),
    _ShelfBkplaneSerialNumber_Type()
)
shelfBkplaneSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBkplaneSerialNumber.setStatus("current")
_ShelfBkplaneRevisionCode_Type = ZhoneAdminString
_ShelfBkplaneRevisionCode_Object = MibTableColumn
shelfBkplaneRevisionCode = _ShelfBkplaneRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1, 5),
    _ShelfBkplaneRevisionCode_Type()
)
shelfBkplaneRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBkplaneRevisionCode.setStatus("current")
_ShelfFanTraySerialNumber_Type = ZhoneAdminString
_ShelfFanTraySerialNumber_Object = MibTableColumn
shelfFanTraySerialNumber = _ShelfFanTraySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1, 6),
    _ShelfFanTraySerialNumber_Type()
)
shelfFanTraySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFanTraySerialNumber.setStatus("current")
_ShelfFanTrayRevisionCode_Type = ZhoneAdminString
_ShelfFanTrayRevisionCode_Object = MibTableColumn
shelfFanTrayRevisionCode = _ShelfFanTrayRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1, 7),
    _ShelfFanTrayRevisionCode_Type()
)
shelfFanTrayRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFanTrayRevisionCode.setStatus("current")
_ShelfSlotCount_Type = Integer32
_ShelfSlotCount_Object = MibTableColumn
shelfSlotCount = _ShelfSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1, 8),
    _ShelfSlotCount_Type()
)
shelfSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSlotCount.setStatus("current")


class _ShelfFeatureBits_Type(OctetString):
    """Custom type shelfFeatureBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ShelfFeatureBits_Type.__name__ = "OctetString"
_ShelfFeatureBits_Object = MibTableColumn
shelfFeatureBits = _ShelfFeatureBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1, 9),
    _ShelfFeatureBits_Type()
)
shelfFeatureBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFeatureBits.setStatus("current")
_ShelfFanTrayType_Type = ZhoneCardType
_ShelfFanTrayType_Object = MibTableColumn
shelfFanTrayType = _ShelfFanTrayType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1, 10),
    _ShelfFanTrayType_Type()
)
shelfFanTrayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFanTrayType.setStatus("current")
_ShelfIOAlarmBoardPresent_Type = TruthValue
_ShelfIOAlarmBoardPresent_Object = MibTableColumn
shelfIOAlarmBoardPresent = _ShelfIOAlarmBoardPresent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 1, 1, 11),
    _ShelfIOAlarmBoardPresent_Type()
)
shelfIOAlarmBoardPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfIOAlarmBoardPresent.setStatus("current")
_ShelfStatusTable_Object = MibTable
shelfStatusTable = _ShelfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2)
)
if mibBuilder.loadTexts:
    shelfStatusTable.setStatus("current")
_ShelfStatusEntry_Object = MibTableRow
shelfStatusEntry = _ShelfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1)
)
shelfStatusEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
)
if mibBuilder.loadTexts:
    shelfStatusEntry.setStatus("current")


class _ShelfAPowerStatus_Type(Integer32):
    """Custom type shelfAPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerNotOk", 2),
          ("powerOk", 1))
    )


_ShelfAPowerStatus_Type.__name__ = "Integer32"
_ShelfAPowerStatus_Object = MibTableColumn
shelfAPowerStatus = _ShelfAPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 1),
    _ShelfAPowerStatus_Type()
)
shelfAPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfAPowerStatus.setStatus("current")


class _ShelfBPowerStatus_Type(Integer32):
    """Custom type shelfBPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerNotOk", 2),
          ("powerOk", 1))
    )


_ShelfBPowerStatus_Type.__name__ = "Integer32"
_ShelfBPowerStatus_Object = MibTableColumn
shelfBPowerStatus = _ShelfBPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 2),
    _ShelfBPowerStatus_Type()
)
shelfBPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBPowerStatus.setStatus("current")


class _ShelfTemperatureStatus_Type(Integer32):
    """Custom type shelfTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aboveNormal", 2),
          ("belowNormal", 3),
          ("normal", 1))
    )


_ShelfTemperatureStatus_Type.__name__ = "Integer32"
_ShelfTemperatureStatus_Object = MibTableColumn
shelfTemperatureStatus = _ShelfTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 3),
    _ShelfTemperatureStatus_Type()
)
shelfTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTemperatureStatus.setStatus("current")


class _ShelfFanTrayStatus_Type(Integer32):
    """Custom type shelfFanTrayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 3),
          ("operational", 1),
          ("partiallyOperational", 2))
    )


_ShelfFanTrayStatus_Type.__name__ = "Integer32"
_ShelfFanTrayStatus_Object = MibTableColumn
shelfFanTrayStatus = _ShelfFanTrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 4),
    _ShelfFanTrayStatus_Type()
)
shelfFanTrayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFanTrayStatus.setStatus("current")


class _ShelfAlarmContactsStatus_Type(Bits):
    """Custom type shelfAlarmContactsStatus based on Bits"""
    namedValues = NamedValues(
        *(("contactAlarm0", 0),
          ("contactAlarm1", 1),
          ("contactAlarm2", 2),
          ("contactAlarm3", 3))
    )

_ShelfAlarmContactsStatus_Type.__name__ = "Bits"
_ShelfAlarmContactsStatus_Object = MibTableColumn
shelfAlarmContactsStatus = _ShelfAlarmContactsStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 5),
    _ShelfAlarmContactsStatus_Type()
)
shelfAlarmContactsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfAlarmContactsStatus.setStatus("current")
_ShelfCardStatus_Type = OctetString
_ShelfCardStatus_Object = MibTableColumn
shelfCardStatus = _ShelfCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 6),
    _ShelfCardStatus_Type()
)
shelfCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardStatus.setStatus("current")


class _ShelfLedStatus_Type(Bits):
    """Custom type shelfLedStatus based on Bits"""
    namedValues = NamedValues(
        *(("battAPower", 0),
          ("battBPower", 1),
          ("criticalAlarm", 5),
          ("fanAlarm", 2),
          ("majorAlarm", 4),
          ("minorAlarm", 3))
    )

_ShelfLedStatus_Type.__name__ = "Bits"
_ShelfLedStatus_Object = MibTableColumn
shelfLedStatus = _ShelfLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 7),
    _ShelfLedStatus_Type()
)
shelfLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfLedStatus.setStatus("current")
_ShelfAdminResets_Type = Gauge32
_ShelfAdminResets_Object = MibTableColumn
shelfAdminResets = _ShelfAdminResets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 8),
    _ShelfAdminResets_Type()
)
shelfAdminResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfAdminResets.setStatus("current")
_ShelfFaultResets_Type = Gauge32
_ShelfFaultResets_Object = MibTableColumn
shelfFaultResets = _ShelfFaultResets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 9),
    _ShelfFaultResets_Type()
)
shelfFaultResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFaultResets.setStatus("current")
_ShelfPowerResets_Type = Gauge32
_ShelfPowerResets_Object = MibTableColumn
shelfPowerResets = _ShelfPowerResets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 10),
    _ShelfPowerResets_Type()
)
shelfPowerResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfPowerResets.setStatus("current")


class _ShelfCPowerStatus_Type(Integer32):
    """Custom type shelfCPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerNotOk", 2),
          ("powerOk", 1))
    )


_ShelfCPowerStatus_Type.__name__ = "Integer32"
_ShelfCPowerStatus_Object = MibTableColumn
shelfCPowerStatus = _ShelfCPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 11),
    _ShelfCPowerStatus_Type()
)
shelfCPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCPowerStatus.setStatus("current")


class _ShelfDPowerStatus_Type(Integer32):
    """Custom type shelfDPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerNotOk", 2),
          ("powerOk", 1))
    )


_ShelfDPowerStatus_Type.__name__ = "Integer32"
_ShelfDPowerStatus_Object = MibTableColumn
shelfDPowerStatus = _ShelfDPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 12),
    _ShelfDPowerStatus_Type()
)
shelfDPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfDPowerStatus.setStatus("current")
_ShelfBatteryAVoltage_Type = ZhoneAdminString
_ShelfBatteryAVoltage_Object = MibTableColumn
shelfBatteryAVoltage = _ShelfBatteryAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 13),
    _ShelfBatteryAVoltage_Type()
)
shelfBatteryAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBatteryAVoltage.setStatus("current")
_ShelfBatteryBVoltage_Type = ZhoneAdminString
_ShelfBatteryBVoltage_Object = MibTableColumn
shelfBatteryBVoltage = _ShelfBatteryBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 14),
    _ShelfBatteryBVoltage_Type()
)
shelfBatteryBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBatteryBVoltage.setStatus("current")
_ShelfChassisReturnVoltage_Type = ZhoneAdminString
_ShelfChassisReturnVoltage_Object = MibTableColumn
shelfChassisReturnVoltage = _ShelfChassisReturnVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 2, 1, 15),
    _ShelfChassisReturnVoltage_Type()
)
shelfChassisReturnVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfChassisReturnVoltage.setStatus("current")
_ShelfFanTable_Object = MibTable
shelfFanTable = _ShelfFanTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 3)
)
if mibBuilder.loadTexts:
    shelfFanTable.setStatus("current")
_ShelfFanEntry_Object = MibTableRow
shelfFanEntry = _ShelfFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 3, 1)
)
shelfFanEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "ZHONE-SHELF-MONITOR-MIB", "shelfFanIndex"),
)
if mibBuilder.loadTexts:
    shelfFanEntry.setStatus("current")


class _ShelfFanIndex_Type(Integer32):
    """Custom type shelfFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ShelfFanIndex_Type.__name__ = "Integer32"
_ShelfFanIndex_Object = MibTableColumn
shelfFanIndex = _ShelfFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 3, 1, 1),
    _ShelfFanIndex_Type()
)
shelfFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfFanIndex.setStatus("current")
_ShelfFanSpeed_Type = Integer32
_ShelfFanSpeed_Object = MibTableColumn
shelfFanSpeed = _ShelfFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 3, 1, 2),
    _ShelfFanSpeed_Type()
)
shelfFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFanSpeed.setStatus("current")
_ShelfFanLocation_Type = ZhoneAdminString
_ShelfFanLocation_Object = MibTableColumn
shelfFanLocation = _ShelfFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 3, 1, 3),
    _ShelfFanLocation_Type()
)
shelfFanLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFanLocation.setStatus("current")
_ShelfFanLowSpeedThreshold_Type = Integer32
_ShelfFanLowSpeedThreshold_Object = MibTableColumn
shelfFanLowSpeedThreshold = _ShelfFanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 3, 1, 4),
    _ShelfFanLowSpeedThreshold_Type()
)
shelfFanLowSpeedThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfFanLowSpeedThreshold.setStatus("current")
_ShelfTemperatureTable_Object = MibTable
shelfTemperatureTable = _ShelfTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 4)
)
if mibBuilder.loadTexts:
    shelfTemperatureTable.setStatus("current")
_ShelfTemperatureEntry_Object = MibTableRow
shelfTemperatureEntry = _ShelfTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 4, 1)
)
shelfTemperatureEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "ZHONE-SHELF-MONITOR-MIB", "shelfTemperatureIndex"),
)
if mibBuilder.loadTexts:
    shelfTemperatureEntry.setStatus("current")


class _ShelfTemperatureIndex_Type(Integer32):
    """Custom type shelfTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ShelfTemperatureIndex_Type.__name__ = "Integer32"
_ShelfTemperatureIndex_Object = MibTableColumn
shelfTemperatureIndex = _ShelfTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 4, 1, 1),
    _ShelfTemperatureIndex_Type()
)
shelfTemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfTemperatureIndex.setStatus("current")
_ShelfTemperature_Type = Integer32
_ShelfTemperature_Object = MibTableColumn
shelfTemperature = _ShelfTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 4, 1, 2),
    _ShelfTemperature_Type()
)
shelfTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTemperature.setStatus("current")
_ShelfTemperatureLocation_Type = ZhoneAdminString
_ShelfTemperatureLocation_Object = MibTableColumn
shelfTemperatureLocation = _ShelfTemperatureLocation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 4, 1, 3),
    _ShelfTemperatureLocation_Type()
)
shelfTemperatureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTemperatureLocation.setStatus("current")
_ShelfTemperatureHighThreshold_Type = Integer32
_ShelfTemperatureHighThreshold_Object = MibTableColumn
shelfTemperatureHighThreshold = _ShelfTemperatureHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 4, 1, 4),
    _ShelfTemperatureHighThreshold_Type()
)
shelfTemperatureHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTemperatureHighThreshold.setStatus("current")
_ShelfTemperatureLowThreshold_Type = Integer32
_ShelfTemperatureLowThreshold_Object = MibTableColumn
shelfTemperatureLowThreshold = _ShelfTemperatureLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 4, 1, 5),
    _ShelfTemperatureLowThreshold_Type()
)
shelfTemperatureLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTemperatureLowThreshold.setStatus("current")
_ShelfCardTable_Object = MibTable
shelfCardTable = _ShelfCardTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5)
)
if mibBuilder.loadTexts:
    shelfCardTable.setStatus("current")
_ShelfCardEntry_Object = MibTableRow
shelfCardEntry = _ShelfCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1)
)
shelfCardEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    shelfCardEntry.setStatus("current")
_CardType_Type = ZhoneCardType
_CardType_Object = MibTableColumn
cardType = _CardType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 1),
    _CardType_Type()
)
cardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardType.setStatus("current")
_CardSubType_Type = ZhoneCardType
_CardSubType_Object = MibTableColumn
cardSubType = _CardSubType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 2),
    _CardSubType_Type()
)
cardSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSubType.setStatus("current")
_CardLineType_Type = ZhoneCardLineType
_CardLineType_Object = MibTableColumn
cardLineType = _CardLineType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 3),
    _CardLineType_Type()
)
cardLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLineType.setStatus("current")
_CardVersion_Type = ZhoneAdminString
_CardVersion_Object = MibTableColumn
cardVersion = _CardVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 4),
    _CardVersion_Type()
)
cardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardVersion.setStatus("current")
_CardEepromVersion_Type = ZhoneAdminString
_CardEepromVersion_Object = MibTableColumn
cardEepromVersion = _CardEepromVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 5),
    _CardEepromVersion_Type()
)
cardEepromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardEepromVersion.setStatus("current")
_CardSerialNumber_Type = ZhoneAdminString
_CardSerialNumber_Object = MibTableColumn
cardSerialNumber = _CardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 6),
    _CardSerialNumber_Type()
)
cardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSerialNumber.setStatus("current")
_CardCLEICode_Type = ZhoneAdminString
_CardCLEICode_Object = MibTableColumn
cardCLEICode = _CardCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 7),
    _CardCLEICode_Type()
)
cardCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCLEICode.setStatus("current")


class _CardFeatureBits_Type(OctetString):
    """Custom type cardFeatureBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CardFeatureBits_Type.__name__ = "OctetString"
_CardFeatureBits_Object = MibTableColumn
cardFeatureBits = _CardFeatureBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 8),
    _CardFeatureBits_Type()
)
cardFeatureBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFeatureBits.setStatus("current")


class _CardState_Type(Integer32):
    """Custom type cardState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("cardNotPresent", 10),
          ("cardNotProvisioned", 11),
          ("cardStateBooting", 1),
          ("cardStateConfiguring", 4),
          ("cardStateDumping", 7),
          ("cardStateFault", 8),
          ("cardStateLoading", 3),
          ("cardStateNone", 0),
          ("cardStatePost", 2),
          ("cardStateReset", 9),
          ("cardStateResetHold", 6),
          ("cardStateRunning", 5))
    )


_CardState_Type.__name__ = "Integer32"
_CardState_Object = MibTableColumn
cardState = _CardState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 9),
    _CardState_Type()
)
cardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardState.setStatus("current")
_CardAdminResets_Type = Gauge32
_CardAdminResets_Object = MibTableColumn
cardAdminResets = _CardAdminResets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 10),
    _CardAdminResets_Type()
)
cardAdminResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardAdminResets.setStatus("current")
_CardFaultResets_Type = Gauge32
_CardFaultResets_Object = MibTableColumn
cardFaultResets = _CardFaultResets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 11),
    _CardFaultResets_Type()
)
cardFaultResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFaultResets.setStatus("current")
_CardReboot_Type = TruthValue
_CardReboot_Object = MibTableColumn
cardReboot = _CardReboot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 5, 1, 12),
    _CardReboot_Type()
)
cardReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardReboot.setStatus("current")


class _ZhoneShelfStatus_Type(Integer32):
    """Custom type zhoneShelfStatus based on Integer32"""
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
              35)
        )
    )
    namedValues = NamedValues(
        *(("fanAFailure", 21),
          ("fanAOK", 22),
          ("fanBFailure", 23),
          ("fanBOK", 24),
          ("fanCFailure", 30),
          ("fanCOK", 31),
          ("fanDFailure", 32),
          ("fanDOK", 33),
          ("fanEFailure", 34),
          ("fanEOK", 35),
          ("fanPowerSupplyAFailure", 14),
          ("fanPowerSupplyAOK", 15),
          ("fanPowerSupplyBFailure", 16),
          ("fanPowerSupplyBOK", 17),
          ("fanPowerSupplyCFailure", 25),
          ("fanPowerSupplyCOK", 26),
          ("fanPowerSupplyDFailure", 27),
          ("fanPowerSupplyDOK", 28),
          ("fanSpeedError", 9),
          ("fanSpeedOK", 20),
          ("fanTrayAdded", 18),
          ("fanTrayRemoved", 19),
          ("leftOutletTempNormal", 2),
          ("leftOutletTempOverLimit", 1),
          ("powerSupplyAFailure", 5),
          ("powerSupplyAOK", 6),
          ("powerSupplyBFailure", 7),
          ("powerSupplyBOK", 8),
          ("rightOutletTempNormal", 4),
          ("rightOutletTempOverLimit", 3),
          ("shelfControllerCleared", 29),
          ("shelfControllerFault", 10),
          ("tempNormal", 13),
          ("tempOverLimit", 11),
          ("tempUnderLimit", 12))
    )


_ZhoneShelfStatus_Type.__name__ = "Integer32"
_ZhoneShelfStatus_Object = MibScalar
zhoneShelfStatus = _ZhoneShelfStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 7),
    _ZhoneShelfStatus_Type()
)
zhoneShelfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneShelfStatus.setStatus("current")


class _ZhoneCardStatus_Type(Integer32):
    """Custom type zhoneCardStatus based on Integer32"""
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
        *(("cardAdded", 2),
          ("cardFaultError", 4),
          ("cardRemoved", 1),
          ("cardReset", 5),
          ("cardRunning", 6),
          ("cardTimeoutError", 3))
    )


_ZhoneCardStatus_Type.__name__ = "Integer32"
_ZhoneCardStatus_Object = MibScalar
zhoneCardStatus = _ZhoneCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 8),
    _ZhoneCardStatus_Type()
)
zhoneCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCardStatus.setStatus("current")
_ZhoneShelfStatusLastChange_Type = TimeStamp
_ZhoneShelfStatusLastChange_Object = MibScalar
zhoneShelfStatusLastChange = _ZhoneShelfStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 10),
    _ZhoneShelfStatusLastChange_Type()
)
zhoneShelfStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneShelfStatusLastChange.setStatus("current")
_ZhoneCardStatusLastChange_Type = TimeStamp
_ZhoneCardStatusLastChange_Object = MibScalar
zhoneCardStatusLastChange = _ZhoneCardStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 11),
    _ZhoneCardStatusLastChange_Type()
)
zhoneCardStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCardStatusLastChange.setStatus("current")
_ZhoneTrapShelfMonitorV2Traps_ObjectIdentity = ObjectIdentity
zhoneTrapShelfMonitorV2Traps = _ZhoneTrapShelfMonitorV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 12)
)
if mibBuilder.loadTexts:
    zhoneTrapShelfMonitorV2Traps.setStatus("current")


class _ZhoneFlashCardStatusChange_Type(Integer32):
    """Custom type zhoneFlashCardStatusChange based on Integer32"""
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
        *(("flashCardPort1Installed", 1),
          ("flashCardPort1Removed", 2),
          ("flashCardPort2Installed", 3),
          ("flashCardPort2Removed", 4))
    )


_ZhoneFlashCardStatusChange_Type.__name__ = "Integer32"
_ZhoneFlashCardStatusChange_Object = MibScalar
zhoneFlashCardStatusChange = _ZhoneFlashCardStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 16),
    _ZhoneFlashCardStatusChange_Type()
)
zhoneFlashCardStatusChange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneFlashCardStatusChange.setStatus("current")


class _ZhoneCardLinkToBkplaneStatus_Type(Integer32):
    """Custom type zhoneCardLinkToBkplaneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cardToBkpLinkNotPresent", 1),
          ("cardToBkpLinkPresent", 2))
    )


_ZhoneCardLinkToBkplaneStatus_Type.__name__ = "Integer32"
_ZhoneCardLinkToBkplaneStatus_Object = MibScalar
zhoneCardLinkToBkplaneStatus = _ZhoneCardLinkToBkplaneStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 17),
    _ZhoneCardLinkToBkplaneStatus_Type()
)
zhoneCardLinkToBkplaneStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zhoneCardLinkToBkplaneStatus.setStatus("current")

# Managed Objects groups

zhoneShelfStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 13)
)
zhoneShelfStatusGroup.setObjects(
      *(("ZHONE-SHELF-MONITOR-MIB", "shelfMfgCLEICode"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfMonitorSerialNumber"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfMonitorRevisionCode"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfBkplaneSerialNumber"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfBkplaneRevisionCode"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfFanTraySerialNumber"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfFanTrayRevisionCode"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfSlotCount"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfFeatureBits"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfAPowerStatus"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfBPowerStatus"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfFanTrayStatus"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfAlarmContactsStatus"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfCardStatus"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfLedStatus"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfAdminResets"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfFaultResets"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfPowerResets"),
        ("ZHONE-SHELF-MONITOR-MIB", "zhoneShelfStatus"),
        ("ZHONE-SHELF-MONITOR-MIB", "zhoneCardStatus"),
        ("ZHONE-SHELF-MONITOR-MIB", "zhoneShelfStatusLastChange"),
        ("ZHONE-SHELF-MONITOR-MIB", "zhoneCardStatusLastChange"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfFanSpeed"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfFanLocation"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfFanLowSpeedThreshold"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfTemperature"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfTemperatureLocation"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfTemperatureHighThreshold"),
        ("ZHONE-SHELF-MONITOR-MIB", "zhoneFlashCardStatusChange"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfTemperatureLowThreshold"),
        ("ZHONE-SHELF-MONITOR-MIB", "shelfTemperatureStatus"))
)
if mibBuilder.loadTexts:
    zhoneShelfStatusGroup.setStatus("current")

zhoneStatusLastChangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 14)
)
zhoneStatusLastChangeGroup.setObjects(
      *(("ZHONE-SHELF-MONITOR-MIB", "zhoneShelfStatusLastChange"),
        ("ZHONE-SHELF-MONITOR-MIB", "zhoneCardStatusLastChange"))
)
if mibBuilder.loadTexts:
    zhoneStatusLastChangeGroup.setStatus("current")

zhoneCardStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 15)
)
zhoneCardStatusGroup.setObjects(
      *(("ZHONE-SHELF-MONITOR-MIB", "cardType"),
        ("ZHONE-SHELF-MONITOR-MIB", "cardSubType"),
        ("ZHONE-SHELF-MONITOR-MIB", "cardLineType"),
        ("ZHONE-SHELF-MONITOR-MIB", "cardVersion"),
        ("ZHONE-SHELF-MONITOR-MIB", "cardEepromVersion"),
        ("ZHONE-SHELF-MONITOR-MIB", "cardSerialNumber"),
        ("ZHONE-SHELF-MONITOR-MIB", "cardCLEICode"),
        ("ZHONE-SHELF-MONITOR-MIB", "cardFeatureBits"),
        ("ZHONE-SHELF-MONITOR-MIB", "cardState"),
        ("ZHONE-SHELF-MONITOR-MIB", "cardAdminResets"),
        ("ZHONE-SHELF-MONITOR-MIB", "cardFaultResets"),
        ("ZHONE-SHELF-MONITOR-MIB", "cardReboot"))
)
if mibBuilder.loadTexts:
    zhoneCardStatusGroup.setStatus("current")


# Notification objects

zhoneTrapShelfStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 12, 2)
)
zhoneTrapShelfStatusChange.setObjects(
    ("ZHONE-SHELF-MONITOR-MIB", "zhoneShelfStatus")
)
if mibBuilder.loadTexts:
    zhoneTrapShelfStatusChange.setStatus(
        "current"
    )

zhoneTrapCardStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 12, 3)
)
zhoneTrapCardStatusChange.setObjects(
    ("ZHONE-SHELF-MONITOR-MIB", "zhoneCardStatus")
)
if mibBuilder.loadTexts:
    zhoneTrapCardStatusChange.setStatus(
        "current"
    )

zhoneTrapCardVersionCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 12, 4)
)
zhoneTrapCardVersionCheck.setObjects(
    ("ZHONE-SHELF-MONITOR-MIB", "cardVersion")
)
if mibBuilder.loadTexts:
    zhoneTrapCardVersionCheck.setStatus(
        "current"
    )

zhoneTrapFlashCardStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 12, 5)
)
zhoneTrapFlashCardStatusChange.setObjects(
    ("ZHONE-SHELF-MONITOR-MIB", "zhoneFlashCardStatusChange")
)
if mibBuilder.loadTexts:
    zhoneTrapFlashCardStatusChange.setStatus(
        "current"
    )

zhoneTrapCardToBkplaneStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 12, 6)
)
zhoneTrapCardToBkplaneStatusChange.setObjects(
    ("ZHONE-SHELF-MONITOR-MIB", "zhoneCardLinkToBkplaneStatus")
)
if mibBuilder.loadTexts:
    zhoneTrapCardToBkplaneStatusChange.setStatus(
        "current"
    )


# Notifications groups

zhoneTrapShelfMonitorGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 2, 12, 1)
)
zhoneTrapShelfMonitorGroup.setObjects(
      *(("ZHONE-SHELF-MONITOR-MIB", "zhoneTrapShelfStatusChange"),
        ("ZHONE-SHELF-MONITOR-MIB", "zhoneTrapCardStatusChange"),
        ("ZHONE-SHELF-MONITOR-MIB", "zhoneTrapCardVersionCheck"),
        ("ZHONE-SHELF-MONITOR-MIB", "zhoneTrapFlashCardStatusChange"))
)
if mibBuilder.loadTexts:
    zhoneTrapShelfMonitorGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-SHELF-MONITOR-MIB",
    **{"shelfDataTable": shelfDataTable,
       "shelfDataEntry": shelfDataEntry,
       "shelfMfgCLEICode": shelfMfgCLEICode,
       "shelfMonitorSerialNumber": shelfMonitorSerialNumber,
       "shelfMonitorRevisionCode": shelfMonitorRevisionCode,
       "shelfBkplaneSerialNumber": shelfBkplaneSerialNumber,
       "shelfBkplaneRevisionCode": shelfBkplaneRevisionCode,
       "shelfFanTraySerialNumber": shelfFanTraySerialNumber,
       "shelfFanTrayRevisionCode": shelfFanTrayRevisionCode,
       "shelfSlotCount": shelfSlotCount,
       "shelfFeatureBits": shelfFeatureBits,
       "shelfFanTrayType": shelfFanTrayType,
       "shelfIOAlarmBoardPresent": shelfIOAlarmBoardPresent,
       "shelfStatusTable": shelfStatusTable,
       "shelfStatusEntry": shelfStatusEntry,
       "shelfAPowerStatus": shelfAPowerStatus,
       "shelfBPowerStatus": shelfBPowerStatus,
       "shelfTemperatureStatus": shelfTemperatureStatus,
       "shelfFanTrayStatus": shelfFanTrayStatus,
       "shelfAlarmContactsStatus": shelfAlarmContactsStatus,
       "shelfCardStatus": shelfCardStatus,
       "shelfLedStatus": shelfLedStatus,
       "shelfAdminResets": shelfAdminResets,
       "shelfFaultResets": shelfFaultResets,
       "shelfPowerResets": shelfPowerResets,
       "shelfCPowerStatus": shelfCPowerStatus,
       "shelfDPowerStatus": shelfDPowerStatus,
       "shelfBatteryAVoltage": shelfBatteryAVoltage,
       "shelfBatteryBVoltage": shelfBatteryBVoltage,
       "shelfChassisReturnVoltage": shelfChassisReturnVoltage,
       "shelfFanTable": shelfFanTable,
       "shelfFanEntry": shelfFanEntry,
       "shelfFanIndex": shelfFanIndex,
       "shelfFanSpeed": shelfFanSpeed,
       "shelfFanLocation": shelfFanLocation,
       "shelfFanLowSpeedThreshold": shelfFanLowSpeedThreshold,
       "shelfTemperatureTable": shelfTemperatureTable,
       "shelfTemperatureEntry": shelfTemperatureEntry,
       "shelfTemperatureIndex": shelfTemperatureIndex,
       "shelfTemperature": shelfTemperature,
       "shelfTemperatureLocation": shelfTemperatureLocation,
       "shelfTemperatureHighThreshold": shelfTemperatureHighThreshold,
       "shelfTemperatureLowThreshold": shelfTemperatureLowThreshold,
       "shelfCardTable": shelfCardTable,
       "shelfCardEntry": shelfCardEntry,
       "cardType": cardType,
       "cardSubType": cardSubType,
       "cardLineType": cardLineType,
       "cardVersion": cardVersion,
       "cardEepromVersion": cardEepromVersion,
       "cardSerialNumber": cardSerialNumber,
       "cardCLEICode": cardCLEICode,
       "cardFeatureBits": cardFeatureBits,
       "cardState": cardState,
       "cardAdminResets": cardAdminResets,
       "cardFaultResets": cardFaultResets,
       "cardReboot": cardReboot,
       "zhoneShelfStatus": zhoneShelfStatus,
       "zhoneCardStatus": zhoneCardStatus,
       "zhoneShelfStatusLastChange": zhoneShelfStatusLastChange,
       "zhoneCardStatusLastChange": zhoneCardStatusLastChange,
       "zhoneTrapShelfMonitorV2Traps": zhoneTrapShelfMonitorV2Traps,
       "zhoneTrapShelfMonitorGroup": zhoneTrapShelfMonitorGroup,
       "zhoneTrapShelfStatusChange": zhoneTrapShelfStatusChange,
       "zhoneTrapCardStatusChange": zhoneTrapCardStatusChange,
       "zhoneTrapCardVersionCheck": zhoneTrapCardVersionCheck,
       "zhoneTrapFlashCardStatusChange": zhoneTrapFlashCardStatusChange,
       "zhoneTrapCardToBkplaneStatusChange": zhoneTrapCardToBkplaneStatusChange,
       "zhoneShelfStatusGroup": zhoneShelfStatusGroup,
       "zhoneStatusLastChangeGroup": zhoneStatusLastChangeGroup,
       "zhoneCardStatusGroup": zhoneCardStatusGroup,
       "zhoneFlashCardStatusChange": zhoneFlashCardStatusChange,
       "zhoneCardLinkToBkplaneStatus": zhoneCardLinkToBkplaneStatus,
       "zhoneShelfMonitorModule": zhoneShelfMonitorModule}
)
