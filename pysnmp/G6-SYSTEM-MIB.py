# SNMP MIB module (G6-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/G6-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:33 2024
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1)
)
device.setRevisions(
        ("2015-05-22 10:59",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30)
)
_SystemShowTimeDate_Type = DisplayString
_SystemShowTimeDate_Object = MibScalar
systemShowTimeDate = _SystemShowTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 1),
    _SystemShowTimeDate_Type()
)
systemShowTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemShowTimeDate.setStatus("current")
_SystemSetTime_Type = DisplayString
_SystemSetTime_Object = MibScalar
systemSetTime = _SystemSetTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 2),
    _SystemSetTime_Type()
)
systemSetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSetTime.setStatus("current")
_SystemSetDate_Type = DisplayString
_SystemSetDate_Object = MibScalar
systemSetDate = _SystemSetDate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 3),
    _SystemSetDate_Type()
)
systemSetDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSetDate.setStatus("current")
_SystemShowUtilization_Type = DisplayString
_SystemShowUtilization_Object = MibScalar
systemShowUtilization = _SystemShowUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 4),
    _SystemShowUtilization_Type()
)
systemShowUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemShowUtilization.setStatus("current")
_SystemRebootDevice_Type = DisplayString
_SystemRebootDevice_Object = MibScalar
systemRebootDevice = _SystemRebootDevice_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 5),
    _SystemRebootDevice_Type()
)
systemRebootDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemRebootDevice.setStatus("current")
_SystemCreateSnapshot_Type = DisplayString
_SystemCreateSnapshot_Object = MibScalar
systemCreateSnapshot = _SystemCreateSnapshot_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 6),
    _SystemCreateSnapshot_Type()
)
systemCreateSnapshot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemCreateSnapshot.setStatus("current")
_SystemSendWakeOnLanPacket_Type = DisplayString
_SystemSendWakeOnLanPacket_Object = MibScalar
systemSendWakeOnLanPacket = _SystemSendWakeOnLanPacket_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 7),
    _SystemSendWakeOnLanPacket_Type()
)
systemSendWakeOnLanPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSendWakeOnLanPacket.setStatus("current")
_SystemAlternativeMacAddress_Type = MacAddress
_SystemAlternativeMacAddress_Object = MibScalar
systemAlternativeMacAddress = _SystemAlternativeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 8),
    _SystemAlternativeMacAddress_Type()
)
systemAlternativeMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAlternativeMacAddress.setStatus("current")


class _SystemBootPreference_Type(Integer32):
    """Custom type systemBootPreference based on Integer32"""
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
        *(("internalFirst", 1),
          ("internalOnly", 3),
          ("sdCardFirst", 0),
          ("sdCardOnly", 2))
    )


_SystemBootPreference_Type.__name__ = "Integer32"
_SystemBootPreference_Object = MibScalar
systemBootPreference = _SystemBootPreference_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 9),
    _SystemBootPreference_Type()
)
systemBootPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemBootPreference.setStatus("current")
_SystemInventory_Type = DisplayString
_SystemInventory_Object = MibScalar
systemInventory = _SystemInventory_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 10),
    _SystemInventory_Type()
)
systemInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemInventory.setStatus("current")
_SystemAutorunCliScript_Type = DisplayString
_SystemAutorunCliScript_Object = MibScalar
systemAutorunCliScript = _SystemAutorunCliScript_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 11),
    _SystemAutorunCliScript_Type()
)
systemAutorunCliScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAutorunCliScript.setStatus("current")


class _SystemLocalConsole_Type(Integer32):
    """Custom type systemLocalConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemLocalConsole_Type.__name__ = "Integer32"
_SystemLocalConsole_Object = MibScalar
systemLocalConsole = _SystemLocalConsole_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 12),
    _SystemLocalConsole_Type()
)
systemLocalConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocalConsole.setStatus("current")


class _SystemPermitDebugAccess_Type(Integer32):
    """Custom type systemPermitDebugAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemPermitDebugAccess_Type.__name__ = "Integer32"
_SystemPermitDebugAccess_Object = MibScalar
systemPermitDebugAccess = _SystemPermitDebugAccess_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 13),
    _SystemPermitDebugAccess_Type()
)
systemPermitDebugAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPermitDebugAccess.setStatus("current")


class _SystemPermitIncomingAlerts_Type(Integer32):
    """Custom type systemPermitIncomingAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SystemPermitIncomingAlerts_Type.__name__ = "Integer32"
_SystemPermitIncomingAlerts_Object = MibScalar
systemPermitIncomingAlerts = _SystemPermitIncomingAlerts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 14),
    _SystemPermitIncomingAlerts_Type()
)
systemPermitIncomingAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPermitIncomingAlerts.setStatus("current")
_ScriptScheduleTable_Object = MibTable
scriptScheduleTable = _ScriptScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15)
)
if mibBuilder.loadTexts:
    scriptScheduleTable.setStatus("current")
_ScriptScheduleEntry_Object = MibTableRow
scriptScheduleEntry = _ScriptScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1)
)
scriptScheduleEntry.setIndexNames(
    (0, "G6-SYSTEM-MIB", "scriptScheduleIndex"),
)
if mibBuilder.loadTexts:
    scriptScheduleEntry.setStatus("current")


class _ScriptScheduleIndex_Type(Integer32):
    """Custom type scriptScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ScriptScheduleIndex_Type.__name__ = "Integer32"
_ScriptScheduleIndex_Object = MibTableColumn
scriptScheduleIndex = _ScriptScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 1),
    _ScriptScheduleIndex_Type()
)
scriptScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scriptScheduleIndex.setStatus("current")
_ScriptScheduleName_Type = DisplayString
_ScriptScheduleName_Object = MibTableColumn
scriptScheduleName = _ScriptScheduleName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 2),
    _ScriptScheduleName_Type()
)
scriptScheduleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleName.setStatus("current")


class _ScriptScheduleMode_Type(Integer32):
    """Custom type scriptScheduleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ScriptScheduleMode_Type.__name__ = "Integer32"
_ScriptScheduleMode_Object = MibTableColumn
scriptScheduleMode = _ScriptScheduleMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 3),
    _ScriptScheduleMode_Type()
)
scriptScheduleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleMode.setStatus("current")
_ScriptScheduleCliScript_Type = DisplayString
_ScriptScheduleCliScript_Object = MibTableColumn
scriptScheduleCliScript = _ScriptScheduleCliScript_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 4),
    _ScriptScheduleCliScript_Type()
)
scriptScheduleCliScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleCliScript.setStatus("current")
_ScriptScheduleMinutes_Type = DisplayString
_ScriptScheduleMinutes_Object = MibTableColumn
scriptScheduleMinutes = _ScriptScheduleMinutes_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 5),
    _ScriptScheduleMinutes_Type()
)
scriptScheduleMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleMinutes.setStatus("current")
_ScriptScheduleHours_Type = DisplayString
_ScriptScheduleHours_Object = MibTableColumn
scriptScheduleHours = _ScriptScheduleHours_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 6),
    _ScriptScheduleHours_Type()
)
scriptScheduleHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleHours.setStatus("current")
_ScriptScheduleDays_Type = DisplayString
_ScriptScheduleDays_Object = MibTableColumn
scriptScheduleDays = _ScriptScheduleDays_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 7),
    _ScriptScheduleDays_Type()
)
scriptScheduleDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleDays.setStatus("current")
_ScriptScheduleMonths_Type = DisplayString
_ScriptScheduleMonths_Object = MibTableColumn
scriptScheduleMonths = _ScriptScheduleMonths_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 8),
    _ScriptScheduleMonths_Type()
)
scriptScheduleMonths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleMonths.setStatus("current")
_ScriptScheduleWeekdays_Type = DisplayString
_ScriptScheduleWeekdays_Object = MibTableColumn
scriptScheduleWeekdays = _ScriptScheduleWeekdays_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 15, 1, 9),
    _ScriptScheduleWeekdays_Type()
)
scriptScheduleWeekdays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptScheduleWeekdays.setStatus("current")
_SystemLastBootTime_Type = DisplayString
_SystemLastBootTime_Object = MibScalar
systemLastBootTime = _SystemLastBootTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 100),
    _SystemLastBootTime_Type()
)
systemLastBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLastBootTime.setStatus("current")
_SystemUptime_Type = Counter32
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 101),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_SystemUsedMacAddress_Type = MacAddress
_SystemUsedMacAddress_Object = MibScalar
systemUsedMacAddress = _SystemUsedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 102),
    _SystemUsedMacAddress_Type()
)
systemUsedMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUsedMacAddress.setStatus("current")


class _SystemUsedBootMedia_Type(Integer32):
    """Custom type systemUsedBootMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalMemory", 1),
          ("nfs", 2),
          ("sdCard", 0))
    )


_SystemUsedBootMedia_Type.__name__ = "Integer32"
_SystemUsedBootMedia_Object = MibScalar
systemUsedBootMedia = _SystemUsedBootMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 103),
    _SystemUsedBootMedia_Type()
)
systemUsedBootMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUsedBootMedia.setStatus("current")


class _SystemTemperature_Type(Integer32):
    """Custom type systemTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemTemperature_Type.__name__ = "Integer32"
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 104),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("current")


class _SystemClimateLevel_Type(Integer32):
    """Custom type systemClimateLevel based on Integer32"""
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
        *(("criticalHigh", 6),
          ("criticalLow", 1),
          ("high", 5),
          ("increased", 4),
          ("low", 2),
          ("normal", 3),
          ("shutdown", 7),
          ("unknown", 0))
    )


_SystemClimateLevel_Type.__name__ = "Integer32"
_SystemClimateLevel_Object = MibScalar
systemClimateLevel = _SystemClimateLevel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 105),
    _SystemClimateLevel_Type()
)
systemClimateLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemClimateLevel.setStatus("current")
_FirmwareTable_Object = MibTable
firmwareTable = _FirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106)
)
if mibBuilder.loadTexts:
    firmwareTable.setStatus("current")
_FirmwareEntry_Object = MibTableRow
firmwareEntry = _FirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1)
)
firmwareEntry.setIndexNames(
    (0, "G6-SYSTEM-MIB", "firmwareIndex"),
)
if mibBuilder.loadTexts:
    firmwareEntry.setStatus("current")


class _FirmwareIndex_Type(Integer32):
    """Custom type firmwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_FirmwareIndex_Type.__name__ = "Integer32"
_FirmwareIndex_Object = MibTableColumn
firmwareIndex = _FirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 1),
    _FirmwareIndex_Type()
)
firmwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    firmwareIndex.setStatus("current")
_FirmwareRunningVersion_Type = DisplayString
_FirmwareRunningVersion_Object = MibTableColumn
firmwareRunningVersion = _FirmwareRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 2),
    _FirmwareRunningVersion_Type()
)
firmwareRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareRunningVersion.setStatus("current")
_FirmwareBuildDate_Type = DisplayString
_FirmwareBuildDate_Object = MibTableColumn
firmwareBuildDate = _FirmwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 3),
    _FirmwareBuildDate_Type()
)
firmwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareBuildDate.setStatus("current")
_FirmwareBuildNumber_Type = Unsigned32
_FirmwareBuildNumber_Object = MibTableColumn
firmwareBuildNumber = _FirmwareBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 106, 1, 4),
    _FirmwareBuildNumber_Type()
)
firmwareBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareBuildNumber.setStatus("current")
_SaveInfoTable_Object = MibTable
saveInfoTable = _SaveInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107)
)
if mibBuilder.loadTexts:
    saveInfoTable.setStatus("current")
_SaveInfoEntry_Object = MibTableRow
saveInfoEntry = _SaveInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1)
)
saveInfoEntry.setIndexNames(
    (0, "G6-SYSTEM-MIB", "saveInfoIndex"),
)
if mibBuilder.loadTexts:
    saveInfoEntry.setStatus("current")


class _SaveInfoIndex_Type(Integer32):
    """Custom type saveInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_SaveInfoIndex_Type.__name__ = "Integer32"
_SaveInfoIndex_Object = MibTableColumn
saveInfoIndex = _SaveInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 1),
    _SaveInfoIndex_Type()
)
saveInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saveInfoIndex.setStatus("current")
_SaveInfoLastSavedParameter_Type = DisplayString
_SaveInfoLastSavedParameter_Object = MibTableColumn
saveInfoLastSavedParameter = _SaveInfoLastSavedParameter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 2),
    _SaveInfoLastSavedParameter_Type()
)
saveInfoLastSavedParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saveInfoLastSavedParameter.setStatus("current")


class _SaveInfoWriteStatus_Type(Integer32):
    """Custom type saveInfoWriteStatus based on Integer32"""
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
        *(("nothingToSave", 0),
          ("processing", 1),
          ("savedToRam", 2),
          ("savedToSdcard", 3))
    )


_SaveInfoWriteStatus_Type.__name__ = "Integer32"
_SaveInfoWriteStatus_Object = MibTableColumn
saveInfoWriteStatus = _SaveInfoWriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 3),
    _SaveInfoWriteStatus_Type()
)
saveInfoWriteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saveInfoWriteStatus.setStatus("current")
_SaveInfoTimeStamp_Type = Counter32
_SaveInfoTimeStamp_Object = MibTableColumn
saveInfoTimeStamp = _SaveInfoTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 30, 107, 1, 4),
    _SaveInfoTimeStamp_Type()
)
saveInfoTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saveInfoTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-SYSTEM-MIB",
    **{"device": device,
       "system": system,
       "systemShowTimeDate": systemShowTimeDate,
       "systemSetTime": systemSetTime,
       "systemSetDate": systemSetDate,
       "systemShowUtilization": systemShowUtilization,
       "systemRebootDevice": systemRebootDevice,
       "systemCreateSnapshot": systemCreateSnapshot,
       "systemSendWakeOnLanPacket": systemSendWakeOnLanPacket,
       "systemAlternativeMacAddress": systemAlternativeMacAddress,
       "systemBootPreference": systemBootPreference,
       "systemInventory": systemInventory,
       "systemAutorunCliScript": systemAutorunCliScript,
       "systemLocalConsole": systemLocalConsole,
       "systemPermitDebugAccess": systemPermitDebugAccess,
       "systemPermitIncomingAlerts": systemPermitIncomingAlerts,
       "scriptScheduleTable": scriptScheduleTable,
       "scriptScheduleEntry": scriptScheduleEntry,
       "scriptScheduleIndex": scriptScheduleIndex,
       "scriptScheduleName": scriptScheduleName,
       "scriptScheduleMode": scriptScheduleMode,
       "scriptScheduleCliScript": scriptScheduleCliScript,
       "scriptScheduleMinutes": scriptScheduleMinutes,
       "scriptScheduleHours": scriptScheduleHours,
       "scriptScheduleDays": scriptScheduleDays,
       "scriptScheduleMonths": scriptScheduleMonths,
       "scriptScheduleWeekdays": scriptScheduleWeekdays,
       "systemLastBootTime": systemLastBootTime,
       "systemUptime": systemUptime,
       "systemUsedMacAddress": systemUsedMacAddress,
       "systemUsedBootMedia": systemUsedBootMedia,
       "systemTemperature": systemTemperature,
       "systemClimateLevel": systemClimateLevel,
       "firmwareTable": firmwareTable,
       "firmwareEntry": firmwareEntry,
       "firmwareIndex": firmwareIndex,
       "firmwareRunningVersion": firmwareRunningVersion,
       "firmwareBuildDate": firmwareBuildDate,
       "firmwareBuildNumber": firmwareBuildNumber,
       "saveInfoTable": saveInfoTable,
       "saveInfoEntry": saveInfoEntry,
       "saveInfoIndex": saveInfoIndex,
       "saveInfoLastSavedParameter": saveInfoLastSavedParameter,
       "saveInfoWriteStatus": saveInfoWriteStatus,
       "saveInfoTimeStamp": saveInfoTimeStamp}
)
