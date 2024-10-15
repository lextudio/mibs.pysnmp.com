# SNMP MIB module (DATA-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DATA-DOMAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:15 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

dataDomainMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19746)
)


# Types definitions



class EnclosureID(Integer32):
    """Custom type EnclosureID based on Integer32"""




class Temperature(Integer32):
    """Custom type Temperature based on Integer32"""




class Minutes(Integer32):
    """Custom type Minutes based on Integer32"""




class Percentage(Integer32):
    """Custom type Percentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )





class KBytesPerSecond(Counter32):
    """Custom type KBytesPerSecond based on Counter32"""




class OpsPerSecond(Counter32):
    """Custom type OpsPerSecond based on Counter32"""




class ErrorCount(Counter32):
    """Custom type ErrorCount based on Counter32"""




class PowerModuleIndex(Integer32):
    """Custom type PowerModuleIndex based on Integer32"""




class PowerModuleStatus(Integer32):
    """Custom type PowerModuleStatus based on Integer32"""
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
          ("ok", 1),
          ("unknown", 2))
    )





class TempSensorIndex(Integer32):
    """Custom type TempSensorIndex based on Integer32"""




class TempSensorDescription(DisplayString):
    """Custom type TempSensorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class TempSensorStatus(Integer32):
    """Custom type TempSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("notfound", 2),
          ("ok", 1))
    )





class FanIndex(Integer32):
    """Custom type FanIndex based on Integer32"""




class FanDescription(DisplayString):
    """Custom type FanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class FanLevel(Integer32):
    """Custom type FanLevel based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("normal", 2),
          ("unknown", 0))
    )





class FanStatus(Integer32):
    """Custom type FanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("notfound", 0),
          ("ok", 1))
    )





class NvramMemorySize(Integer32):
    """Custom type NvramMemorySize based on Integer32"""




class NvramWindowSize(Integer32):
    """Custom type NvramWindowSize based on Integer32"""




class NvramBytesTransferred(Integer32):
    """Custom type NvramBytesTransferred based on Integer32"""




class NvramBatteryIndex(Integer32):
    """Custom type NvramBatteryIndex based on Integer32"""




class NvramBatteryStatus(Integer32):
    """Custom type NvramBatteryStatus based on Integer32"""
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
        *(("disabled", 2),
          ("discharged", 3),
          ("ok", 1),
          ("softdisabled", 5),
          ("unknown", 4))
    )





class DiskIndex(Integer32):
    """Custom type DiskIndex based on Integer32"""




class DiskModel(DisplayString):
    """Custom type DiskModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class DiskFirmwareVersion(DisplayString):
    """Custom type DiskFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class DiskSerialNumber(DisplayString):
    """Custom type DiskSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class DiskCapacity(DisplayString):
    """Custom type DiskCapacity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )





class DiskState(Integer32):
    """Custom type DiskState based on Integer32"""
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
        *(("absent", 3),
          ("failed", 4),
          ("ok", 1),
          ("unknown", 2))
    )





class DiskSectorsPerSecond(Counter32):
    """Custom type DiskSectorsPerSecond based on Counter32"""




class FileSystemStatus(Integer32):
    """Custom type FileSystemStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("running", 3),
          ("unknown", 4))
    )





class FileSystemResourceIndex(Integer32):
    """Custom type FileSystemResourceIndex based on Integer32"""




class FileSystemResourceName(DisplayString):
    """Custom type FileSystemResourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class FileSystemSpaceUnit(Counter32):
    """Custom type FileSystemSpaceUnit based on Counter32"""




class AlertIndex(Integer32):
    """Custom type AlertIndex based on Integer32"""




class AlertTimestamp(DisplayString):
    """Custom type AlertTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class AlertDescription(DisplayString):
    """Custom type AlertDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class SystemStatsIndex(Integer32):
    """Custom type SystemStatsIndex based on Integer32"""




class RaidDiskState(Integer32):
    """Custom type RaidDiskState based on Integer32"""
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
        *(("absent", 4),
          ("failed", 5),
          ("inuse", 1),
          ("notinuse", 2),
          ("spare", 3),
          ("unknown", 6))
    )





class RaidDiskStatus(Integer32):
    """Custom type RaidDiskStatus based on Integer32"""
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
        *(("ok", 1),
          ("reconstructing", 2),
          ("resynching", 3),
          ("unknown", 4))
    )





class RaidDiskGroup(DisplayString):
    """Custom type RaidDiskGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )





class ReplicationState(Integer32):
    """Custom type ReplicationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledNeedsResync", 3),
          ("enabled", 1))
    )





class ReplicationStatus(Integer32):
    """Custom type ReplicationStatus based on Integer32"""
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
        *(("connected", 1),
          ("disconnected", 2),
          ("migrating", 3),
          ("neverConnected", 5),
          ("suspended", 4))
    )





class ReplicationConnectTime(Integer32):
    """Custom type ReplicationConnectTime based on Integer32"""




class ReplicationPath(DisplayString):
    """Custom type ReplicationPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )





class ReplicationLag(Integer32):
    """Custom type ReplicationLag based on Integer32"""




class ReplicationTraffic(Integer32):
    """Custom type ReplicationTraffic based on Integer32"""




class ReplicationThrottle(Integer32):
    """Custom type ReplicationThrottle based on Integer32"""




class ReplicationSyncedTime(Integer32):
    """Custom type ReplicationSyncedTime based on Integer32"""




class ReplicationContext(Integer32):
    """Custom type ReplicationContext based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DataDomainMibConformance_ObjectIdentity = ObjectIdentity
dataDomainMibConformance = _DataDomainMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 0)
)
_DataDomainMibCompliances_ObjectIdentity = ObjectIdentity
dataDomainMibCompliances = _DataDomainMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 0, 1)
)
_DataDomainMibGroups_ObjectIdentity = ObjectIdentity
dataDomainMibGroups = _DataDomainMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2)
)
_DataDomainMibObjects_ObjectIdentity = ObjectIdentity
dataDomainMibObjects = _DataDomainMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1)
)
_Environmentals_ObjectIdentity = ObjectIdentity
environmentals = _Environmentals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1)
)
_Power_ObjectIdentity = ObjectIdentity
power = _Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1)
)
_PowerModules_ObjectIdentity = ObjectIdentity
powerModules = _PowerModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1)
)
_PowerModuleTable_Object = MibTable
powerModuleTable = _PowerModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    powerModuleTable.setStatus("mandatory")
_PowerModuleEntry_Object = MibTableRow
powerModuleEntry = _PowerModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1)
)
powerModuleEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "powerEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "powerModuleIndex"),
)
if mibBuilder.loadTexts:
    powerModuleEntry.setStatus("mandatory")
_PowerEnclosureID_Type = EnclosureID
_PowerEnclosureID_Object = MibTableColumn
powerEnclosureID = _PowerEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 1),
    _PowerEnclosureID_Type()
)
powerEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerEnclosureID.setStatus("mandatory")
_PowerModuleIndex_Type = PowerModuleIndex
_PowerModuleIndex_Object = MibTableColumn
powerModuleIndex = _PowerModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 2),
    _PowerModuleIndex_Type()
)
powerModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerModuleIndex.setStatus("mandatory")
_PowerModuleStatus_Type = PowerModuleStatus
_PowerModuleStatus_Object = MibTableColumn
powerModuleStatus = _PowerModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 3),
    _PowerModuleStatus_Type()
)
powerModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerModuleStatus.setStatus("mandatory")
_Temperatures_ObjectIdentity = ObjectIdentity
temperatures = _Temperatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2)
)
_TemperatureSensors_ObjectIdentity = ObjectIdentity
temperatureSensors = _TemperatureSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1)
)
_TemperatureSensorTable_Object = MibTable
temperatureSensorTable = _TemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    temperatureSensorTable.setStatus("mandatory")
_TemperatureSensorEntry_Object = MibTableRow
temperatureSensorEntry = _TemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1)
)
temperatureSensorEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "tempEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "tempSensorIndex"),
)
if mibBuilder.loadTexts:
    temperatureSensorEntry.setStatus("mandatory")
_TempEnclosureID_Type = EnclosureID
_TempEnclosureID_Object = MibTableColumn
tempEnclosureID = _TempEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 1),
    _TempEnclosureID_Type()
)
tempEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempEnclosureID.setStatus("mandatory")
_TempSensorIndex_Type = TempSensorIndex
_TempSensorIndex_Object = MibTableColumn
tempSensorIndex = _TempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 2),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("mandatory")
_TempSensorDescription_Type = TempSensorDescription
_TempSensorDescription_Object = MibTableColumn
tempSensorDescription = _TempSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 3),
    _TempSensorDescription_Type()
)
tempSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorDescription.setStatus("mandatory")
_TempSensorCurrentValue_Type = Temperature
_TempSensorCurrentValue_Object = MibTableColumn
tempSensorCurrentValue = _TempSensorCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 4),
    _TempSensorCurrentValue_Type()
)
tempSensorCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorCurrentValue.setStatus("mandatory")
_TempSensorStatus_Type = TempSensorStatus
_TempSensorStatus_Object = MibTableColumn
tempSensorStatus = _TempSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 5),
    _TempSensorStatus_Type()
)
tempSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorStatus.setStatus("mandatory")
_Fans_ObjectIdentity = ObjectIdentity
fans = _Fans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3)
)
_FanProperties_ObjectIdentity = ObjectIdentity
fanProperties = _FanProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1)
)
_FanPropertiesTable_Object = MibTable
fanPropertiesTable = _FanPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fanPropertiesTable.setStatus("mandatory")
_FanPropertiesEntry_Object = MibTableRow
fanPropertiesEntry = _FanPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1)
)
fanPropertiesEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "fanEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanPropertiesEntry.setStatus("mandatory")
_FanEnclosureID_Type = EnclosureID
_FanEnclosureID_Object = MibTableColumn
fanEnclosureID = _FanEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 1),
    _FanEnclosureID_Type()
)
fanEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanEnclosureID.setStatus("mandatory")
_FanIndex_Type = FanIndex
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 2),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanIndex.setStatus("mandatory")
_FanDescription_Type = FanDescription
_FanDescription_Object = MibTableColumn
fanDescription = _FanDescription_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 3),
    _FanDescription_Type()
)
fanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDescription.setStatus("mandatory")
_FanLevel_Type = FanLevel
_FanLevel_Object = MibTableColumn
fanLevel = _FanLevel_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 4),
    _FanLevel_Type()
)
fanLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanLevel.setStatus("mandatory")
_FanStatus_Type = FanStatus
_FanStatus_Object = MibTableColumn
fanStatus = _FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 5),
    _FanStatus_Type()
)
fanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStatus.setStatus("mandatory")
_Nvram_ObjectIdentity = ObjectIdentity
nvram = _Nvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2)
)
_NvramProperties_ObjectIdentity = ObjectIdentity
nvramProperties = _NvramProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 1)
)
_NvramMemorySize_Type = NvramMemorySize
_NvramMemorySize_Object = MibScalar
nvramMemorySize = _NvramMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1),
    _NvramMemorySize_Type()
)
nvramMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramMemorySize.setStatus("mandatory")
_NvramWindowSize_Type = NvramWindowSize
_NvramWindowSize_Object = MibScalar
nvramWindowSize = _NvramWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 2),
    _NvramWindowSize_Type()
)
nvramWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramWindowSize.setStatus("mandatory")
_NvramStats_ObjectIdentity = ObjectIdentity
nvramStats = _NvramStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 2)
)
_NvramPCIErrorCount_Type = ErrorCount
_NvramPCIErrorCount_Object = MibScalar
nvramPCIErrorCount = _NvramPCIErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1),
    _NvramPCIErrorCount_Type()
)
nvramPCIErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramPCIErrorCount.setStatus("mandatory")
_NvramMemoryErrorCount_Type = ErrorCount
_NvramMemoryErrorCount_Object = MibScalar
nvramMemoryErrorCount = _NvramMemoryErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 2),
    _NvramMemoryErrorCount_Type()
)
nvramMemoryErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramMemoryErrorCount.setStatus("mandatory")
_NvramBatteries_ObjectIdentity = ObjectIdentity
nvramBatteries = _NvramBatteries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3)
)
_NvramBatteryTable_Object = MibTable
nvramBatteryTable = _NvramBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    nvramBatteryTable.setStatus("mandatory")
_NvramBatteryEntry_Object = MibTableRow
nvramBatteryEntry = _NvramBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1)
)
nvramBatteryEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "nvramBatteryIndex"),
)
if mibBuilder.loadTexts:
    nvramBatteryEntry.setStatus("mandatory")
_NvramBatteryIndex_Type = NvramBatteryIndex
_NvramBatteryIndex_Object = MibTableColumn
nvramBatteryIndex = _NvramBatteryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 1),
    _NvramBatteryIndex_Type()
)
nvramBatteryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramBatteryIndex.setStatus("mandatory")
_NvramBatteryStatus_Type = NvramBatteryStatus
_NvramBatteryStatus_Object = MibTableColumn
nvramBatteryStatus = _NvramBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 2),
    _NvramBatteryStatus_Type()
)
nvramBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramBatteryStatus.setStatus("mandatory")
_NvramBatteryCharge_Type = Percentage
_NvramBatteryCharge_Object = MibTableColumn
nvramBatteryCharge = _NvramBatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 3),
    _NvramBatteryCharge_Type()
)
nvramBatteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramBatteryCharge.setStatus("mandatory")
_FileSystem_ObjectIdentity = ObjectIdentity
fileSystem = _FileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3)
)
_FileSystemProperties_ObjectIdentity = ObjectIdentity
fileSystemProperties = _FileSystemProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 1)
)
_FileSystemStatus_Type = FileSystemStatus
_FileSystemStatus_Object = MibScalar
fileSystemStatus = _FileSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 1),
    _FileSystemStatus_Type()
)
fileSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemStatus.setStatus("mandatory")
_FileSystemVirtualSpace_Type = FileSystemSpaceUnit
_FileSystemVirtualSpace_Object = MibScalar
fileSystemVirtualSpace = _FileSystemVirtualSpace_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 2),
    _FileSystemVirtualSpace_Type()
)
fileSystemVirtualSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemVirtualSpace.setStatus("mandatory")
_FileSystemSpace_ObjectIdentity = ObjectIdentity
fileSystemSpace = _FileSystemSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2)
)
_FileSystemSpaceTable_Object = MibTable
fileSystemSpaceTable = _FileSystemSpaceTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fileSystemSpaceTable.setStatus("mandatory")
_FileSystemSpaceEntry_Object = MibTableRow
fileSystemSpaceEntry = _FileSystemSpaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1)
)
fileSystemSpaceEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "fileSystemResourceIndex"),
)
if mibBuilder.loadTexts:
    fileSystemSpaceEntry.setStatus("mandatory")
_FileSystemResourceIndex_Type = FileSystemResourceIndex
_FileSystemResourceIndex_Object = MibTableColumn
fileSystemResourceIndex = _FileSystemResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 1),
    _FileSystemResourceIndex_Type()
)
fileSystemResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemResourceIndex.setStatus("mandatory")
_FileSystemResourceName_Type = FileSystemResourceName
_FileSystemResourceName_Object = MibTableColumn
fileSystemResourceName = _FileSystemResourceName_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 2),
    _FileSystemResourceName_Type()
)
fileSystemResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemResourceName.setStatus("mandatory")
_FileSystemSpaceSize_Type = FileSystemSpaceUnit
_FileSystemSpaceSize_Object = MibTableColumn
fileSystemSpaceSize = _FileSystemSpaceSize_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 3),
    _FileSystemSpaceSize_Type()
)
fileSystemSpaceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemSpaceSize.setStatus("mandatory")
_FileSystemSpaceUsed_Type = FileSystemSpaceUnit
_FileSystemSpaceUsed_Object = MibTableColumn
fileSystemSpaceUsed = _FileSystemSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 4),
    _FileSystemSpaceUsed_Type()
)
fileSystemSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemSpaceUsed.setStatus("mandatory")
_FileSystemSpaceAvail_Type = FileSystemSpaceUnit
_FileSystemSpaceAvail_Object = MibTableColumn
fileSystemSpaceAvail = _FileSystemSpaceAvail_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 5),
    _FileSystemSpaceAvail_Type()
)
fileSystemSpaceAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemSpaceAvail.setStatus("mandatory")
_FileSystemPercentUsed_Type = Percentage
_FileSystemPercentUsed_Object = MibTableColumn
fileSystemPercentUsed = _FileSystemPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 6),
    _FileSystemPercentUsed_Type()
)
fileSystemPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemPercentUsed.setStatus("mandatory")
_Alerts_ObjectIdentity = ObjectIdentity
alerts = _Alerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4)
)
_CurrentAlerts_ObjectIdentity = ObjectIdentity
currentAlerts = _CurrentAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1)
)
_CurrentAlertTable_Object = MibTable
currentAlertTable = _CurrentAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    currentAlertTable.setStatus("mandatory")
_CurrentAlertEntry_Object = MibTableRow
currentAlertEntry = _CurrentAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1)
)
currentAlertEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "currentAlertIndex"),
)
if mibBuilder.loadTexts:
    currentAlertEntry.setStatus("mandatory")
_CurrentAlertIndex_Type = AlertIndex
_CurrentAlertIndex_Object = MibTableColumn
currentAlertIndex = _CurrentAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 1),
    _CurrentAlertIndex_Type()
)
currentAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlertIndex.setStatus("mandatory")
_CurrentAlertTimestamp_Type = AlertTimestamp
_CurrentAlertTimestamp_Object = MibTableColumn
currentAlertTimestamp = _CurrentAlertTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 2),
    _CurrentAlertTimestamp_Type()
)
currentAlertTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlertTimestamp.setStatus("mandatory")
_CurrentAlertDescription_Type = AlertDescription
_CurrentAlertDescription_Object = MibTableColumn
currentAlertDescription = _CurrentAlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 3),
    _CurrentAlertDescription_Type()
)
currentAlertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlertDescription.setStatus("mandatory")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5)
)
_SystemStats_ObjectIdentity = ObjectIdentity
systemStats = _SystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1)
)
_SystemStatsTable_Object = MibTable
systemStatsTable = _SystemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    systemStatsTable.setStatus("mandatory")
_SystemStatsEntry_Object = MibTableRow
systemStatsEntry = _SystemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1)
)
systemStatsEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "systemStatsIndex"),
)
if mibBuilder.loadTexts:
    systemStatsEntry.setStatus("mandatory")
_SystemStatsIndex_Type = SystemStatsIndex
_SystemStatsIndex_Object = MibTableColumn
systemStatsIndex = _SystemStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 1),
    _SystemStatsIndex_Type()
)
systemStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatsIndex.setStatus("mandatory")
_Cpu0PercentageBusy_Type = Percentage
_Cpu0PercentageBusy_Object = MibTableColumn
cpu0PercentageBusy = _Cpu0PercentageBusy_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 2),
    _Cpu0PercentageBusy_Type()
)
cpu0PercentageBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu0PercentageBusy.setStatus("mandatory")
_Cpu1PercentageBusy_Type = Percentage
_Cpu1PercentageBusy_Object = MibTableColumn
cpu1PercentageBusy = _Cpu1PercentageBusy_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 3),
    _Cpu1PercentageBusy_Type()
)
cpu1PercentageBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu1PercentageBusy.setStatus("mandatory")
_NfsOpsPerSecond_Type = OpsPerSecond
_NfsOpsPerSecond_Object = MibTableColumn
nfsOpsPerSecond = _NfsOpsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 4),
    _NfsOpsPerSecond_Type()
)
nfsOpsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsOpsPerSecond.setStatus("mandatory")
_NfsIdlePercentage_Type = Percentage
_NfsIdlePercentage_Object = MibTableColumn
nfsIdlePercentage = _NfsIdlePercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 5),
    _NfsIdlePercentage_Type()
)
nfsIdlePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsIdlePercentage.setStatus("mandatory")
_NfsProcPercentage_Type = Percentage
_NfsProcPercentage_Object = MibTableColumn
nfsProcPercentage = _NfsProcPercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 6),
    _NfsProcPercentage_Type()
)
nfsProcPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsProcPercentage.setStatus("mandatory")
_NfsSendPercentage_Type = Percentage
_NfsSendPercentage_Object = MibTableColumn
nfsSendPercentage = _NfsSendPercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 7),
    _NfsSendPercentage_Type()
)
nfsSendPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsSendPercentage.setStatus("mandatory")
_NfsReceivePercentage_Type = Percentage
_NfsReceivePercentage_Object = MibTableColumn
nfsReceivePercentage = _NfsReceivePercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 8),
    _NfsReceivePercentage_Type()
)
nfsReceivePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsReceivePercentage.setStatus("mandatory")
_CifsOpsPerSecond_Type = OpsPerSecond
_CifsOpsPerSecond_Object = MibTableColumn
cifsOpsPerSecond = _CifsOpsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 9),
    _CifsOpsPerSecond_Type()
)
cifsOpsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifsOpsPerSecond.setStatus("mandatory")
_DiskReadKBytesPerSecond_Type = KBytesPerSecond
_DiskReadKBytesPerSecond_Object = MibTableColumn
diskReadKBytesPerSecond = _DiskReadKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 10),
    _DiskReadKBytesPerSecond_Type()
)
diskReadKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReadKBytesPerSecond.setStatus("mandatory")
_DiskWriteKBytesPerSecond_Type = KBytesPerSecond
_DiskWriteKBytesPerSecond_Object = MibTableColumn
diskWriteKBytesPerSecond = _DiskWriteKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 11),
    _DiskWriteKBytesPerSecond_Type()
)
diskWriteKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskWriteKBytesPerSecond.setStatus("mandatory")
_DiskBusyPercentage_Type = Percentage
_DiskBusyPercentage_Object = MibTableColumn
diskBusyPercentage = _DiskBusyPercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 12),
    _DiskBusyPercentage_Type()
)
diskBusyPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskBusyPercentage.setStatus("mandatory")
_NvramReadKBytesPerSecond_Type = KBytesPerSecond
_NvramReadKBytesPerSecond_Object = MibTableColumn
nvramReadKBytesPerSecond = _NvramReadKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 13),
    _NvramReadKBytesPerSecond_Type()
)
nvramReadKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramReadKBytesPerSecond.setStatus("mandatory")
_NvramWriteKBytesPerSecond_Type = KBytesPerSecond
_NvramWriteKBytesPerSecond_Object = MibTableColumn
nvramWriteKBytesPerSecond = _NvramWriteKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 14),
    _NvramWriteKBytesPerSecond_Type()
)
nvramWriteKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramWriteKBytesPerSecond.setStatus("mandatory")
_ReplInKBytesPerSecond_Type = KBytesPerSecond
_ReplInKBytesPerSecond_Object = MibTableColumn
replInKBytesPerSecond = _ReplInKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 15),
    _ReplInKBytesPerSecond_Type()
)
replInKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replInKBytesPerSecond.setStatus("mandatory")
_ReplOutKBytesPerSecond_Type = KBytesPerSecond
_ReplOutKBytesPerSecond_Object = MibTableColumn
replOutKBytesPerSecond = _ReplOutKBytesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 16),
    _ReplOutKBytesPerSecond_Type()
)
replOutKBytesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replOutKBytesPerSecond.setStatus("mandatory")
_DiskStorage_ObjectIdentity = ObjectIdentity
diskStorage = _DiskStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6)
)
_DiskProperties_ObjectIdentity = ObjectIdentity
diskProperties = _DiskProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1)
)
_DiskPropertiesTable_Object = MibTable
diskPropertiesTable = _DiskPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    diskPropertiesTable.setStatus("mandatory")
_DiskPropertiesEntry_Object = MibTableRow
diskPropertiesEntry = _DiskPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1)
)
diskPropertiesEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "diskPropEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "diskPropIndex"),
)
if mibBuilder.loadTexts:
    diskPropertiesEntry.setStatus("mandatory")
_DiskPropEnclosureID_Type = EnclosureID
_DiskPropEnclosureID_Object = MibTableColumn
diskPropEnclosureID = _DiskPropEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 1),
    _DiskPropEnclosureID_Type()
)
diskPropEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPropEnclosureID.setStatus("mandatory")
_DiskPropIndex_Type = DiskIndex
_DiskPropIndex_Object = MibTableColumn
diskPropIndex = _DiskPropIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 2),
    _DiskPropIndex_Type()
)
diskPropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPropIndex.setStatus("mandatory")
_DiskModel_Type = DiskModel
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 3),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("mandatory")
_DiskFirmwareVersion_Type = DiskFirmwareVersion
_DiskFirmwareVersion_Object = MibTableColumn
diskFirmwareVersion = _DiskFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 4),
    _DiskFirmwareVersion_Type()
)
diskFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFirmwareVersion.setStatus("mandatory")
_DiskSerialNumber_Type = DiskSerialNumber
_DiskSerialNumber_Object = MibTableColumn
diskSerialNumber = _DiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 5),
    _DiskSerialNumber_Type()
)
diskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSerialNumber.setStatus("mandatory")
_DiskCapacity_Type = DiskCapacity
_DiskCapacity_Object = MibTableColumn
diskCapacity = _DiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 6),
    _DiskCapacity_Type()
)
diskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskCapacity.setStatus("mandatory")
_DiskPropState_Type = DiskState
_DiskPropState_Object = MibTableColumn
diskPropState = _DiskPropState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 7),
    _DiskPropState_Type()
)
diskPropState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPropState.setStatus("mandatory")
_DiskPerformance_ObjectIdentity = ObjectIdentity
diskPerformance = _DiskPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2)
)
_DiskPerformanceTable_Object = MibTable
diskPerformanceTable = _DiskPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    diskPerformanceTable.setStatus("mandatory")
_DiskPerformanceEntry_Object = MibTableRow
diskPerformanceEntry = _DiskPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1)
)
diskPerformanceEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "diskPerfEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "diskPerfIndex"),
)
if mibBuilder.loadTexts:
    diskPerformanceEntry.setStatus("mandatory")
_DiskPerfEnclosureID_Type = EnclosureID
_DiskPerfEnclosureID_Object = MibTableColumn
diskPerfEnclosureID = _DiskPerfEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 1),
    _DiskPerfEnclosureID_Type()
)
diskPerfEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPerfEnclosureID.setStatus("mandatory")
_DiskPerfIndex_Type = DiskIndex
_DiskPerfIndex_Object = MibTableColumn
diskPerfIndex = _DiskPerfIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 2),
    _DiskPerfIndex_Type()
)
diskPerfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPerfIndex.setStatus("mandatory")
_DiskSectorsRead_Type = DiskSectorsPerSecond
_DiskSectorsRead_Object = MibTableColumn
diskSectorsRead = _DiskSectorsRead_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 3),
    _DiskSectorsRead_Type()
)
diskSectorsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSectorsRead.setStatus("mandatory")
_DiskSectorsWritten_Type = DiskSectorsPerSecond
_DiskSectorsWritten_Object = MibTableColumn
diskSectorsWritten = _DiskSectorsWritten_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 4),
    _DiskSectorsWritten_Type()
)
diskSectorsWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSectorsWritten.setStatus("mandatory")
_DiskTotalKBytes_Type = KBytesPerSecond
_DiskTotalKBytes_Object = MibTableColumn
diskTotalKBytes = _DiskTotalKBytes_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 5),
    _DiskTotalKBytes_Type()
)
diskTotalKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotalKBytes.setStatus("mandatory")
_DiskBusy_Type = Percentage
_DiskBusy_Object = MibTableColumn
diskBusy = _DiskBusy_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 6),
    _DiskBusy_Type()
)
diskBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskBusy.setStatus("mandatory")
_DiskPerfState_Type = DiskState
_DiskPerfState_Object = MibTableColumn
diskPerfState = _DiskPerfState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 7),
    _DiskPerfState_Type()
)
diskPerfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPerfState.setStatus("mandatory")
_DiskReliability_ObjectIdentity = ObjectIdentity
diskReliability = _DiskReliability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3)
)
_DiskReliabilityTable_Object = MibTable
diskReliabilityTable = _DiskReliabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    diskReliabilityTable.setStatus("mandatory")
_DiskReliabilityEntry_Object = MibTableRow
diskReliabilityEntry = _DiskReliabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1)
)
diskReliabilityEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "diskErrEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "diskErrIndex"),
)
if mibBuilder.loadTexts:
    diskReliabilityEntry.setStatus("mandatory")
_DiskErrEnclosureID_Type = EnclosureID
_DiskErrEnclosureID_Object = MibTableColumn
diskErrEnclosureID = _DiskErrEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 1),
    _DiskErrEnclosureID_Type()
)
diskErrEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskErrEnclosureID.setStatus("mandatory")
_DiskErrIndex_Type = DiskIndex
_DiskErrIndex_Object = MibTableColumn
diskErrIndex = _DiskErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 2),
    _DiskErrIndex_Type()
)
diskErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskErrIndex.setStatus("mandatory")
_DiskTemperature_Type = Temperature
_DiskTemperature_Object = MibTableColumn
diskTemperature = _DiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 3),
    _DiskTemperature_Type()
)
diskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTemperature.setStatus("mandatory")
_DiskTimeoutCount_Type = ErrorCount
_DiskTimeoutCount_Object = MibTableColumn
diskTimeoutCount = _DiskTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 4),
    _DiskTimeoutCount_Type()
)
diskTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTimeoutCount.setStatus("mandatory")
_DiskReadFailCount_Type = ErrorCount
_DiskReadFailCount_Object = MibTableColumn
diskReadFailCount = _DiskReadFailCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 5),
    _DiskReadFailCount_Type()
)
diskReadFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReadFailCount.setStatus("mandatory")
_DiskWriteFailCount_Type = ErrorCount
_DiskWriteFailCount_Object = MibTableColumn
diskWriteFailCount = _DiskWriteFailCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 6),
    _DiskWriteFailCount_Type()
)
diskWriteFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskWriteFailCount.setStatus("mandatory")
_DiskMiscFailCount_Type = ErrorCount
_DiskMiscFailCount_Object = MibTableColumn
diskMiscFailCount = _DiskMiscFailCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 7),
    _DiskMiscFailCount_Type()
)
diskMiscFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskMiscFailCount.setStatus("mandatory")
_DiskOffTrackErrCount_Type = ErrorCount
_DiskOffTrackErrCount_Object = MibTableColumn
diskOffTrackErrCount = _DiskOffTrackErrCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 8),
    _DiskOffTrackErrCount_Type()
)
diskOffTrackErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskOffTrackErrCount.setStatus("mandatory")
_DiskSoftEccCount_Type = ErrorCount
_DiskSoftEccCount_Object = MibTableColumn
diskSoftEccCount = _DiskSoftEccCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 9),
    _DiskSoftEccCount_Type()
)
diskSoftEccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSoftEccCount.setStatus("mandatory")
_DiskCrcErrCount_Type = ErrorCount
_DiskCrcErrCount_Object = MibTableColumn
diskCrcErrCount = _DiskCrcErrCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 10),
    _DiskCrcErrCount_Type()
)
diskCrcErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskCrcErrCount.setStatus("mandatory")
_DiskProbationalCount_Type = ErrorCount
_DiskProbationalCount_Object = MibTableColumn
diskProbationalCount = _DiskProbationalCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 11),
    _DiskProbationalCount_Type()
)
diskProbationalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskProbationalCount.setStatus("mandatory")
_DiskReallocCount_Type = ErrorCount
_DiskReallocCount_Object = MibTableColumn
diskReallocCount = _DiskReallocCount_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 12),
    _DiskReallocCount_Type()
)
diskReallocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskReallocCount.setStatus("mandatory")
_DiskErrState_Type = DiskState
_DiskErrState_Object = MibTableColumn
diskErrState = _DiskErrState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 13),
    _DiskErrState_Type()
)
diskErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskErrState.setStatus("mandatory")
_Raid_ObjectIdentity = ObjectIdentity
raid = _Raid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7)
)
_RaidInfo_ObjectIdentity = ObjectIdentity
raidInfo = _RaidInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1)
)
_RaidInfoTable_Object = MibTable
raidInfoTable = _RaidInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    raidInfoTable.setStatus("mandatory")
_RaidInfoEntry_Object = MibTableRow
raidInfoEntry = _RaidInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1)
)
raidInfoEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "raidDiskEnclosureID"),
    (0, "DATA-DOMAIN-MIB", "raidDiskIndex"),
)
if mibBuilder.loadTexts:
    raidInfoEntry.setStatus("mandatory")
_RaidDiskEnclosureID_Type = EnclosureID
_RaidDiskEnclosureID_Object = MibTableColumn
raidDiskEnclosureID = _RaidDiskEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 1),
    _RaidDiskEnclosureID_Type()
)
raidDiskEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskEnclosureID.setStatus("mandatory")
_RaidDiskIndex_Type = DiskIndex
_RaidDiskIndex_Object = MibTableColumn
raidDiskIndex = _RaidDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 2),
    _RaidDiskIndex_Type()
)
raidDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskIndex.setStatus("mandatory")
_RaidDiskState_Type = RaidDiskState
_RaidDiskState_Object = MibTableColumn
raidDiskState = _RaidDiskState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 3),
    _RaidDiskState_Type()
)
raidDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskState.setStatus("mandatory")
_RaidDiskGroup_Type = RaidDiskGroup
_RaidDiskGroup_Object = MibTableColumn
raidDiskGroup = _RaidDiskGroup_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 4),
    _RaidDiskGroup_Type()
)
raidDiskGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskGroup.setStatus("mandatory")
_RaidDiskStatus_Type = RaidDiskStatus
_RaidDiskStatus_Object = MibTableColumn
raidDiskStatus = _RaidDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 5),
    _RaidDiskStatus_Type()
)
raidDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskStatus.setStatus("mandatory")
_RaidDiskReconPercentage_Type = Percentage
_RaidDiskReconPercentage_Object = MibTableColumn
raidDiskReconPercentage = _RaidDiskReconPercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 6),
    _RaidDiskReconPercentage_Type()
)
raidDiskReconPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskReconPercentage.setStatus("mandatory")
_RaidDiskReconMinutes_Type = Minutes
_RaidDiskReconMinutes_Object = MibTableColumn
raidDiskReconMinutes = _RaidDiskReconMinutes_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 7),
    _RaidDiskReconMinutes_Type()
)
raidDiskReconMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskReconMinutes.setStatus("mandatory")
_RaidDiskResynchPercentage_Type = Percentage
_RaidDiskResynchPercentage_Object = MibTableColumn
raidDiskResynchPercentage = _RaidDiskResynchPercentage_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 8),
    _RaidDiskResynchPercentage_Type()
)
raidDiskResynchPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskResynchPercentage.setStatus("mandatory")
_RaidDiskResynchMinutes_Type = Minutes
_RaidDiskResynchMinutes_Object = MibTableColumn
raidDiskResynchMinutes = _RaidDiskResynchMinutes_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 9),
    _RaidDiskResynchMinutes_Type()
)
raidDiskResynchMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskResynchMinutes.setStatus("mandatory")
_Replication_ObjectIdentity = ObjectIdentity
replication = _Replication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8)
)
_ReplicationInfo_ObjectIdentity = ObjectIdentity
replicationInfo = _ReplicationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1)
)
_ReplicationInfoTable_Object = MibTable
replicationInfoTable = _ReplicationInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    replicationInfoTable.setStatus("mandatory")
_ReplicationInfoEntry_Object = MibTableRow
replicationInfoEntry = _ReplicationInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1)
)
replicationInfoEntry.setIndexNames(
    (0, "DATA-DOMAIN-MIB", "replContext"),
)
if mibBuilder.loadTexts:
    replicationInfoEntry.setStatus("mandatory")
_ReplContext_Type = ReplicationContext
_ReplContext_Object = MibTableColumn
replContext = _ReplContext_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 1),
    _ReplContext_Type()
)
replContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replContext.setStatus("mandatory")
_ReplState_Type = ReplicationState
_ReplState_Object = MibTableColumn
replState = _ReplState_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 2),
    _ReplState_Type()
)
replState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replState.setStatus("mandatory")
_ReplStatus_Type = ReplicationStatus
_ReplStatus_Object = MibTableColumn
replStatus = _ReplStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 3),
    _ReplStatus_Type()
)
replStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replStatus.setStatus("mandatory")
_ReplFileSysStatus_Type = FileSystemStatus
_ReplFileSysStatus_Object = MibTableColumn
replFileSysStatus = _ReplFileSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 4),
    _ReplFileSysStatus_Type()
)
replFileSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replFileSysStatus.setStatus("mandatory")
_ReplConnTime_Type = ReplicationConnectTime
_ReplConnTime_Object = MibTableColumn
replConnTime = _ReplConnTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 5),
    _ReplConnTime_Type()
)
replConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replConnTime.setStatus("mandatory")
_ReplSource_Type = ReplicationPath
_ReplSource_Object = MibTableColumn
replSource = _ReplSource_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 6),
    _ReplSource_Type()
)
replSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replSource.setStatus("mandatory")
_ReplDestination_Type = ReplicationPath
_ReplDestination_Object = MibTableColumn
replDestination = _ReplDestination_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 7),
    _ReplDestination_Type()
)
replDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replDestination.setStatus("mandatory")
_ReplLag_Type = ReplicationLag
_ReplLag_Object = MibTableColumn
replLag = _ReplLag_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 8),
    _ReplLag_Type()
)
replLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replLag.setStatus("mandatory")
_ReplPreCompBytesSent_Type = ReplicationTraffic
_ReplPreCompBytesSent_Object = MibTableColumn
replPreCompBytesSent = _ReplPreCompBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 9),
    _ReplPreCompBytesSent_Type()
)
replPreCompBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPreCompBytesSent.setStatus("mandatory")
_ReplPostCompBytesSent_Type = ReplicationTraffic
_ReplPostCompBytesSent_Object = MibTableColumn
replPostCompBytesSent = _ReplPostCompBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 10),
    _ReplPostCompBytesSent_Type()
)
replPostCompBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPostCompBytesSent.setStatus("mandatory")
_ReplPreCompBytesRemaining_Type = ReplicationTraffic
_ReplPreCompBytesRemaining_Object = MibTableColumn
replPreCompBytesRemaining = _ReplPreCompBytesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 11),
    _ReplPreCompBytesRemaining_Type()
)
replPreCompBytesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPreCompBytesRemaining.setStatus("mandatory")
_ReplPostCompBytesReceived_Type = ReplicationTraffic
_ReplPostCompBytesReceived_Object = MibTableColumn
replPostCompBytesReceived = _ReplPostCompBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 12),
    _ReplPostCompBytesReceived_Type()
)
replPostCompBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replPostCompBytesReceived.setStatus("mandatory")
_ReplThrottle_Type = ReplicationThrottle
_ReplThrottle_Object = MibTableColumn
replThrottle = _ReplThrottle_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 13),
    _ReplThrottle_Type()
)
replThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replThrottle.setStatus("mandatory")
_ReplSyncedAsOfTime_Type = ReplicationSyncedTime
_ReplSyncedAsOfTime_Object = MibTableColumn
replSyncedAsOfTime = _ReplSyncedAsOfTime_Object(
    (1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 14),
    _ReplSyncedAsOfTime_Type()
)
replSyncedAsOfTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replSyncedAsOfTime.setStatus("mandatory")
_DataDomainMibNotifications_ObjectIdentity = ObjectIdentity
dataDomainMibNotifications = _DataDomainMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 2)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3)
)
_Restorer_ObjectIdentity = ObjectIdentity
restorer = _Restorer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1)
)
_Dd200_ObjectIdentity = ObjectIdentity
dd200 = _Dd200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 1)
)
_Dd200Proto_ObjectIdentity = ObjectIdentity
dd200Proto = _Dd200Proto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 2)
)
_Dd410_ObjectIdentity = ObjectIdentity
dd410 = _Dd410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 3)
)
_Dd430_ObjectIdentity = ObjectIdentity
dd430 = _Dd430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 4)
)
_Dd460_ObjectIdentity = ObjectIdentity
dd460 = _Dd460_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 5)
)
_Dd400g_ObjectIdentity = ObjectIdentity
dd400g = _Dd400g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 6)
)
_Dd460g_ObjectIdentity = ObjectIdentity
dd460g = _Dd460g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 7)
)
_Dd560_ObjectIdentity = ObjectIdentity
dd560 = _Dd560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 8)
)
_Dd560g_ObjectIdentity = ObjectIdentity
dd560g = _Dd560g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 9)
)
_Dd580_ObjectIdentity = ObjectIdentity
dd580 = _Dd580_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 10)
)
_Dd580g_ObjectIdentity = ObjectIdentity
dd580g = _Dd580g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 11)
)
_Dd565_ObjectIdentity = ObjectIdentity
dd565 = _Dd565_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 12)
)
_Dd530_ObjectIdentity = ObjectIdentity
dd530 = _Dd530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 13)
)
_Dd510_ObjectIdentity = ObjectIdentity
dd510 = _Dd510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 14)
)
_Dd120_ObjectIdentity = ObjectIdentity
dd120 = _Dd120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 15)
)
_Dd590_ObjectIdentity = ObjectIdentity
dd590 = _Dd590_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 16)
)
_Dd590g_ObjectIdentity = ObjectIdentity
dd590g = _Dd590g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 17)
)
_DdModelUnsupported_ObjectIdentity = ObjectIdentity
ddModelUnsupported = _DdModelUnsupported_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19746, 3, 1, 9999)
)

# Managed Objects groups

environmentalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 1)
)
environmentalsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "powerEnclosureID"),
        ("DATA-DOMAIN-MIB", "powerModuleIndex"),
        ("DATA-DOMAIN-MIB", "powerModuleStatus"),
        ("DATA-DOMAIN-MIB", "tempEnclosureID"),
        ("DATA-DOMAIN-MIB", "tempSensorIndex"),
        ("DATA-DOMAIN-MIB", "tempSensorDescription"),
        ("DATA-DOMAIN-MIB", "tempSensorCurrentValue"),
        ("DATA-DOMAIN-MIB", "tempSensorStatus"),
        ("DATA-DOMAIN-MIB", "fanEnclosureID"),
        ("DATA-DOMAIN-MIB", "fanIndex"),
        ("DATA-DOMAIN-MIB", "fanDescription"),
        ("DATA-DOMAIN-MIB", "fanLevel"),
        ("DATA-DOMAIN-MIB", "fanStatus"))
)
if mibBuilder.loadTexts:
    environmentalsGroup.setStatus("current")

nvramGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 2)
)
nvramGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "nvramMemorySize"),
        ("DATA-DOMAIN-MIB", "nvramWindowSize"),
        ("DATA-DOMAIN-MIB", "nvramPCIErrorCount"),
        ("DATA-DOMAIN-MIB", "nvramMemoryErrorCount"),
        ("DATA-DOMAIN-MIB", "nvramBatteryIndex"),
        ("DATA-DOMAIN-MIB", "nvramBatteryStatus"),
        ("DATA-DOMAIN-MIB", "nvramBatteryCharge"))
)
if mibBuilder.loadTexts:
    nvramGroup.setStatus("current")

fileSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 3)
)
fileSystemGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "fileSystemStatus"),
        ("DATA-DOMAIN-MIB", "fileSystemVirtualSpace"),
        ("DATA-DOMAIN-MIB", "fileSystemResourceIndex"),
        ("DATA-DOMAIN-MIB", "fileSystemResourceName"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceSize"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"),
        ("DATA-DOMAIN-MIB", "fileSystemSpaceAvail"),
        ("DATA-DOMAIN-MIB", "fileSystemPercentUsed"))
)
if mibBuilder.loadTexts:
    fileSystemGroup.setStatus("current")

alertsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 4)
)
alertsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "currentAlertIndex"),
        ("DATA-DOMAIN-MIB", "currentAlertTimestamp"),
        ("DATA-DOMAIN-MIB", "currentAlertDescription"))
)
if mibBuilder.loadTexts:
    alertsGroup.setStatus("current")

statisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 5)
)
statisticsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "systemStatsIndex"),
        ("DATA-DOMAIN-MIB", "cpu0PercentageBusy"),
        ("DATA-DOMAIN-MIB", "cpu1PercentageBusy"),
        ("DATA-DOMAIN-MIB", "nfsOpsPerSecond"),
        ("DATA-DOMAIN-MIB", "nfsIdlePercentage"),
        ("DATA-DOMAIN-MIB", "nfsProcPercentage"),
        ("DATA-DOMAIN-MIB", "nfsSendPercentage"),
        ("DATA-DOMAIN-MIB", "nfsReceivePercentage"),
        ("DATA-DOMAIN-MIB", "cifsOpsPerSecond"),
        ("DATA-DOMAIN-MIB", "diskReadKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "diskWriteKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "diskBusyPercentage"),
        ("DATA-DOMAIN-MIB", "nvramReadKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "nvramWriteKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "replInKBytesPerSecond"),
        ("DATA-DOMAIN-MIB", "replOutKBytesPerSecond"))
)
if mibBuilder.loadTexts:
    statisticsGroup.setStatus("current")

raidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 6)
)
raidGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "raidDiskEnclosureID"),
        ("DATA-DOMAIN-MIB", "raidDiskIndex"),
        ("DATA-DOMAIN-MIB", "raidDiskState"),
        ("DATA-DOMAIN-MIB", "raidDiskGroup"),
        ("DATA-DOMAIN-MIB", "raidDiskStatus"),
        ("DATA-DOMAIN-MIB", "raidDiskReconPercentage"),
        ("DATA-DOMAIN-MIB", "raidDiskReconMinutes"),
        ("DATA-DOMAIN-MIB", "raidDiskResynchPercentage"),
        ("DATA-DOMAIN-MIB", "raidDiskResynchMinutes"))
)
if mibBuilder.loadTexts:
    raidGroup.setStatus("current")

internalDiskStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 7)
)
internalDiskStorageGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "diskPropEnclosureID"),
        ("DATA-DOMAIN-MIB", "diskPropIndex"),
        ("DATA-DOMAIN-MIB", "diskModel"),
        ("DATA-DOMAIN-MIB", "diskFirmwareVersion"),
        ("DATA-DOMAIN-MIB", "diskSerialNumber"),
        ("DATA-DOMAIN-MIB", "diskCapacity"),
        ("DATA-DOMAIN-MIB", "diskPropState"),
        ("DATA-DOMAIN-MIB", "diskPerfEnclosureID"),
        ("DATA-DOMAIN-MIB", "diskPerfIndex"),
        ("DATA-DOMAIN-MIB", "diskSectorsRead"),
        ("DATA-DOMAIN-MIB", "diskSectorsWritten"),
        ("DATA-DOMAIN-MIB", "diskTotalKBytes"),
        ("DATA-DOMAIN-MIB", "diskBusy"),
        ("DATA-DOMAIN-MIB", "diskPerfState"),
        ("DATA-DOMAIN-MIB", "diskErrEnclosureID"),
        ("DATA-DOMAIN-MIB", "diskErrIndex"),
        ("DATA-DOMAIN-MIB", "diskTemperature"),
        ("DATA-DOMAIN-MIB", "diskTimeoutCount"),
        ("DATA-DOMAIN-MIB", "diskReadFailCount"),
        ("DATA-DOMAIN-MIB", "diskWriteFailCount"),
        ("DATA-DOMAIN-MIB", "diskMiscFailCount"),
        ("DATA-DOMAIN-MIB", "diskOffTrackErrCount"),
        ("DATA-DOMAIN-MIB", "diskSoftEccCount"),
        ("DATA-DOMAIN-MIB", "diskCrcErrCount"),
        ("DATA-DOMAIN-MIB", "diskProbationalCount"),
        ("DATA-DOMAIN-MIB", "diskReallocCount"),
        ("DATA-DOMAIN-MIB", "diskErrState"))
)
if mibBuilder.loadTexts:
    internalDiskStorageGroup.setStatus("current")

externalUnmanagedDiskStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 8)
)
externalUnmanagedDiskStorageGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "diskPropEnclosureID"),
        ("DATA-DOMAIN-MIB", "diskPropIndex"),
        ("DATA-DOMAIN-MIB", "diskModel"),
        ("DATA-DOMAIN-MIB", "diskFirmwareVersion"),
        ("DATA-DOMAIN-MIB", "diskSerialNumber"),
        ("DATA-DOMAIN-MIB", "diskCapacity"),
        ("DATA-DOMAIN-MIB", "diskPropState"),
        ("DATA-DOMAIN-MIB", "diskPerfIndex"),
        ("DATA-DOMAIN-MIB", "diskSectorsRead"),
        ("DATA-DOMAIN-MIB", "diskSectorsWritten"),
        ("DATA-DOMAIN-MIB", "diskTotalKBytes"),
        ("DATA-DOMAIN-MIB", "diskBusy"),
        ("DATA-DOMAIN-MIB", "diskPerfState"))
)
if mibBuilder.loadTexts:
    externalUnmanagedDiskStorageGroup.setStatus("current")

replGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 11)
)
replGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "replContext"),
        ("DATA-DOMAIN-MIB", "replState"),
        ("DATA-DOMAIN-MIB", "replStatus"),
        ("DATA-DOMAIN-MIB", "replFileSysStatus"),
        ("DATA-DOMAIN-MIB", "replConnTime"),
        ("DATA-DOMAIN-MIB", "replSource"),
        ("DATA-DOMAIN-MIB", "replDestination"),
        ("DATA-DOMAIN-MIB", "replLag"),
        ("DATA-DOMAIN-MIB", "replPreCompBytesSent"),
        ("DATA-DOMAIN-MIB", "replPostCompBytesSent"),
        ("DATA-DOMAIN-MIB", "replPreCompBytesRemaining"),
        ("DATA-DOMAIN-MIB", "replPostCompBytesReceived"),
        ("DATA-DOMAIN-MIB", "replThrottle"))
)
if mibBuilder.loadTexts:
    replGroup.setStatus("current")


# Notification objects

powerSupplyFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 1)
)
if mibBuilder.loadTexts:
    powerSupplyFailedAlarm.setStatus(
        "current"
    )

systemOverheatWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 2)
)
systemOverheatWarningAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "tempSensorIndex")
)
if mibBuilder.loadTexts:
    systemOverheatWarningAlarm.setStatus(
        "current"
    )

systemOverheatAlertAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 3)
)
systemOverheatAlertAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "tempSensorIndex")
)
if mibBuilder.loadTexts:
    systemOverheatAlertAlarm.setStatus(
        "current"
    )

systemOverheatShutdowntAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 4)
)
systemOverheatShutdowntAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "tempSensorIndex")
)
if mibBuilder.loadTexts:
    systemOverheatShutdowntAlarm.setStatus(
        "current"
    )

fanModuleFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 5)
)
fanModuleFailedAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "fanIndex")
)
if mibBuilder.loadTexts:
    fanModuleFailedAlarm.setStatus(
        "current"
    )

nvramFailingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 6)
)
if mibBuilder.loadTexts:
    nvramFailingAlarm.setStatus(
        "current"
    )

fileSystemFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 7)
)
if mibBuilder.loadTexts:
    fileSystemFailedAlarm.setStatus(
        "current"
    )

fileSpaceMaintenanceAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 8)
)
fileSpaceMaintenanceAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "fileSystemResourceIndex")
)
if mibBuilder.loadTexts:
    fileSpaceMaintenanceAlarm.setStatus(
        "current"
    )

fileSpaceWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 9)
)
fileSpaceWarningAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "fileSystemResourceIndex")
)
if mibBuilder.loadTexts:
    fileSpaceWarningAlarm.setStatus(
        "current"
    )

fileSpaceSevereAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 10)
)
fileSpaceSevereAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "fileSystemResourceIndex")
)
if mibBuilder.loadTexts:
    fileSpaceSevereAlarm.setStatus(
        "current"
    )

fileSpaceCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 11)
)
fileSpaceCriticalAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "fileSystemResourceIndex")
)
if mibBuilder.loadTexts:
    fileSpaceCriticalAlarm.setStatus(
        "current"
    )

diskFailingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 12)
)
diskFailingAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskPropIndex")
)
if mibBuilder.loadTexts:
    diskFailingAlarm.setStatus(
        "current"
    )

diskFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 13)
)
diskFailedAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskPropIndex")
)
if mibBuilder.loadTexts:
    diskFailedAlarm.setStatus(
        "current"
    )

diskOverheatWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 14)
)
diskOverheatWarningAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskErrIndex")
)
if mibBuilder.loadTexts:
    diskOverheatWarningAlarm.setStatus(
        "current"
    )

diskOverheatAlertAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 15)
)
diskOverheatAlertAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskErrIndex")
)
if mibBuilder.loadTexts:
    diskOverheatAlertAlarm.setStatus(
        "current"
    )

diskOverheatShutdowntAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 16)
)
diskOverheatShutdowntAlarm.setObjects(
    ("DATA-DOMAIN-MIB", "diskErrIndex")
)
if mibBuilder.loadTexts:
    diskOverheatShutdowntAlarm.setStatus(
        "current"
    )

raidReconSevereAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 17)
)
if mibBuilder.loadTexts:
    raidReconSevereAlarm.setStatus(
        "current"
    )

raidReconCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 18)
)
if mibBuilder.loadTexts:
    raidReconCriticalAlarm.setStatus(
        "current"
    )

raidReconCriticalShutdownAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 19746, 2, 19)
)
if mibBuilder.loadTexts:
    raidReconCriticalShutdownAlarm.setStatus(
        "current"
    )


# Notifications groups

basicNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 9)
)
basicNotificationsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "powerSupplyFailedAlarm"),
        ("DATA-DOMAIN-MIB", "systemOverheatWarningAlarm"),
        ("DATA-DOMAIN-MIB", "systemOverheatAlertAlarm"),
        ("DATA-DOMAIN-MIB", "systemOverheatShutdowntAlarm"),
        ("DATA-DOMAIN-MIB", "fanModuleFailedAlarm"),
        ("DATA-DOMAIN-MIB", "nvramFailingAlarm"),
        ("DATA-DOMAIN-MIB", "fileSystemFailedAlarm"),
        ("DATA-DOMAIN-MIB", "fileSpaceMaintenanceAlarm"),
        ("DATA-DOMAIN-MIB", "fileSpaceWarningAlarm"),
        ("DATA-DOMAIN-MIB", "fileSpaceSevereAlarm"),
        ("DATA-DOMAIN-MIB", "fileSpaceCriticalAlarm"),
        ("DATA-DOMAIN-MIB", "raidReconSevereAlarm"),
        ("DATA-DOMAIN-MIB", "raidReconCriticalAlarm"),
        ("DATA-DOMAIN-MIB", "raidReconCriticalShutdownAlarm"))
)
if mibBuilder.loadTexts:
    basicNotificationsGroup.setStatus(
        "current"
    )

internalDiskStorageNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19746, 0, 2, 10)
)
internalDiskStorageNotificationsGroup.setObjects(
      *(("DATA-DOMAIN-MIB", "diskFailingAlarm"),
        ("DATA-DOMAIN-MIB", "diskFailedAlarm"),
        ("DATA-DOMAIN-MIB", "diskOverheatWarningAlarm"),
        ("DATA-DOMAIN-MIB", "diskOverheatAlertAlarm"),
        ("DATA-DOMAIN-MIB", "diskOverheatShutdowntAlarm"))
)
if mibBuilder.loadTexts:
    internalDiskStorageNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dataDomainMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 19746, 0, 1, 1)
)
if mibBuilder.loadTexts:
    dataDomainMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATA-DOMAIN-MIB",
    **{"EnclosureID": EnclosureID,
       "Temperature": Temperature,
       "Minutes": Minutes,
       "Percentage": Percentage,
       "KBytesPerSecond": KBytesPerSecond,
       "OpsPerSecond": OpsPerSecond,
       "ErrorCount": ErrorCount,
       "PowerModuleIndex": PowerModuleIndex,
       "PowerModuleStatus": PowerModuleStatus,
       "TempSensorIndex": TempSensorIndex,
       "TempSensorDescription": TempSensorDescription,
       "TempSensorStatus": TempSensorStatus,
       "FanIndex": FanIndex,
       "FanDescription": FanDescription,
       "FanLevel": FanLevel,
       "FanStatus": FanStatus,
       "NvramMemorySize": NvramMemorySize,
       "NvramWindowSize": NvramWindowSize,
       "NvramBytesTransferred": NvramBytesTransferred,
       "NvramBatteryIndex": NvramBatteryIndex,
       "NvramBatteryStatus": NvramBatteryStatus,
       "DiskIndex": DiskIndex,
       "DiskModel": DiskModel,
       "DiskFirmwareVersion": DiskFirmwareVersion,
       "DiskSerialNumber": DiskSerialNumber,
       "DiskCapacity": DiskCapacity,
       "DiskState": DiskState,
       "DiskSectorsPerSecond": DiskSectorsPerSecond,
       "FileSystemStatus": FileSystemStatus,
       "FileSystemResourceIndex": FileSystemResourceIndex,
       "FileSystemResourceName": FileSystemResourceName,
       "FileSystemSpaceUnit": FileSystemSpaceUnit,
       "AlertIndex": AlertIndex,
       "AlertTimestamp": AlertTimestamp,
       "AlertDescription": AlertDescription,
       "SystemStatsIndex": SystemStatsIndex,
       "RaidDiskState": RaidDiskState,
       "RaidDiskStatus": RaidDiskStatus,
       "RaidDiskGroup": RaidDiskGroup,
       "ReplicationState": ReplicationState,
       "ReplicationStatus": ReplicationStatus,
       "ReplicationConnectTime": ReplicationConnectTime,
       "ReplicationPath": ReplicationPath,
       "ReplicationLag": ReplicationLag,
       "ReplicationTraffic": ReplicationTraffic,
       "ReplicationThrottle": ReplicationThrottle,
       "ReplicationSyncedTime": ReplicationSyncedTime,
       "ReplicationContext": ReplicationContext,
       "dataDomainMib": dataDomainMib,
       "dataDomainMibConformance": dataDomainMibConformance,
       "dataDomainMibCompliances": dataDomainMibCompliances,
       "dataDomainMibCompliance": dataDomainMibCompliance,
       "dataDomainMibGroups": dataDomainMibGroups,
       "environmentalsGroup": environmentalsGroup,
       "nvramGroup": nvramGroup,
       "fileSystemGroup": fileSystemGroup,
       "alertsGroup": alertsGroup,
       "statisticsGroup": statisticsGroup,
       "raidGroup": raidGroup,
       "internalDiskStorageGroup": internalDiskStorageGroup,
       "externalUnmanagedDiskStorageGroup": externalUnmanagedDiskStorageGroup,
       "basicNotificationsGroup": basicNotificationsGroup,
       "internalDiskStorageNotificationsGroup": internalDiskStorageNotificationsGroup,
       "replGroup": replGroup,
       "dataDomainMibObjects": dataDomainMibObjects,
       "environmentals": environmentals,
       "power": power,
       "powerModules": powerModules,
       "powerModuleTable": powerModuleTable,
       "powerModuleEntry": powerModuleEntry,
       "powerEnclosureID": powerEnclosureID,
       "powerModuleIndex": powerModuleIndex,
       "powerModuleStatus": powerModuleStatus,
       "temperatures": temperatures,
       "temperatureSensors": temperatureSensors,
       "temperatureSensorTable": temperatureSensorTable,
       "temperatureSensorEntry": temperatureSensorEntry,
       "tempEnclosureID": tempEnclosureID,
       "tempSensorIndex": tempSensorIndex,
       "tempSensorDescription": tempSensorDescription,
       "tempSensorCurrentValue": tempSensorCurrentValue,
       "tempSensorStatus": tempSensorStatus,
       "fans": fans,
       "fanProperties": fanProperties,
       "fanPropertiesTable": fanPropertiesTable,
       "fanPropertiesEntry": fanPropertiesEntry,
       "fanEnclosureID": fanEnclosureID,
       "fanIndex": fanIndex,
       "fanDescription": fanDescription,
       "fanLevel": fanLevel,
       "fanStatus": fanStatus,
       "nvram": nvram,
       "nvramProperties": nvramProperties,
       "nvramMemorySize": nvramMemorySize,
       "nvramWindowSize": nvramWindowSize,
       "nvramStats": nvramStats,
       "nvramPCIErrorCount": nvramPCIErrorCount,
       "nvramMemoryErrorCount": nvramMemoryErrorCount,
       "nvramBatteries": nvramBatteries,
       "nvramBatteryTable": nvramBatteryTable,
       "nvramBatteryEntry": nvramBatteryEntry,
       "nvramBatteryIndex": nvramBatteryIndex,
       "nvramBatteryStatus": nvramBatteryStatus,
       "nvramBatteryCharge": nvramBatteryCharge,
       "fileSystem": fileSystem,
       "fileSystemProperties": fileSystemProperties,
       "fileSystemStatus": fileSystemStatus,
       "fileSystemVirtualSpace": fileSystemVirtualSpace,
       "fileSystemSpace": fileSystemSpace,
       "fileSystemSpaceTable": fileSystemSpaceTable,
       "fileSystemSpaceEntry": fileSystemSpaceEntry,
       "fileSystemResourceIndex": fileSystemResourceIndex,
       "fileSystemResourceName": fileSystemResourceName,
       "fileSystemSpaceSize": fileSystemSpaceSize,
       "fileSystemSpaceUsed": fileSystemSpaceUsed,
       "fileSystemSpaceAvail": fileSystemSpaceAvail,
       "fileSystemPercentUsed": fileSystemPercentUsed,
       "alerts": alerts,
       "currentAlerts": currentAlerts,
       "currentAlertTable": currentAlertTable,
       "currentAlertEntry": currentAlertEntry,
       "currentAlertIndex": currentAlertIndex,
       "currentAlertTimestamp": currentAlertTimestamp,
       "currentAlertDescription": currentAlertDescription,
       "statistics": statistics,
       "systemStats": systemStats,
       "systemStatsTable": systemStatsTable,
       "systemStatsEntry": systemStatsEntry,
       "systemStatsIndex": systemStatsIndex,
       "cpu0PercentageBusy": cpu0PercentageBusy,
       "cpu1PercentageBusy": cpu1PercentageBusy,
       "nfsOpsPerSecond": nfsOpsPerSecond,
       "nfsIdlePercentage": nfsIdlePercentage,
       "nfsProcPercentage": nfsProcPercentage,
       "nfsSendPercentage": nfsSendPercentage,
       "nfsReceivePercentage": nfsReceivePercentage,
       "cifsOpsPerSecond": cifsOpsPerSecond,
       "diskReadKBytesPerSecond": diskReadKBytesPerSecond,
       "diskWriteKBytesPerSecond": diskWriteKBytesPerSecond,
       "diskBusyPercentage": diskBusyPercentage,
       "nvramReadKBytesPerSecond": nvramReadKBytesPerSecond,
       "nvramWriteKBytesPerSecond": nvramWriteKBytesPerSecond,
       "replInKBytesPerSecond": replInKBytesPerSecond,
       "replOutKBytesPerSecond": replOutKBytesPerSecond,
       "diskStorage": diskStorage,
       "diskProperties": diskProperties,
       "diskPropertiesTable": diskPropertiesTable,
       "diskPropertiesEntry": diskPropertiesEntry,
       "diskPropEnclosureID": diskPropEnclosureID,
       "diskPropIndex": diskPropIndex,
       "diskModel": diskModel,
       "diskFirmwareVersion": diskFirmwareVersion,
       "diskSerialNumber": diskSerialNumber,
       "diskCapacity": diskCapacity,
       "diskPropState": diskPropState,
       "diskPerformance": diskPerformance,
       "diskPerformanceTable": diskPerformanceTable,
       "diskPerformanceEntry": diskPerformanceEntry,
       "diskPerfEnclosureID": diskPerfEnclosureID,
       "diskPerfIndex": diskPerfIndex,
       "diskSectorsRead": diskSectorsRead,
       "diskSectorsWritten": diskSectorsWritten,
       "diskTotalKBytes": diskTotalKBytes,
       "diskBusy": diskBusy,
       "diskPerfState": diskPerfState,
       "diskReliability": diskReliability,
       "diskReliabilityTable": diskReliabilityTable,
       "diskReliabilityEntry": diskReliabilityEntry,
       "diskErrEnclosureID": diskErrEnclosureID,
       "diskErrIndex": diskErrIndex,
       "diskTemperature": diskTemperature,
       "diskTimeoutCount": diskTimeoutCount,
       "diskReadFailCount": diskReadFailCount,
       "diskWriteFailCount": diskWriteFailCount,
       "diskMiscFailCount": diskMiscFailCount,
       "diskOffTrackErrCount": diskOffTrackErrCount,
       "diskSoftEccCount": diskSoftEccCount,
       "diskCrcErrCount": diskCrcErrCount,
       "diskProbationalCount": diskProbationalCount,
       "diskReallocCount": diskReallocCount,
       "diskErrState": diskErrState,
       "raid": raid,
       "raidInfo": raidInfo,
       "raidInfoTable": raidInfoTable,
       "raidInfoEntry": raidInfoEntry,
       "raidDiskEnclosureID": raidDiskEnclosureID,
       "raidDiskIndex": raidDiskIndex,
       "raidDiskState": raidDiskState,
       "raidDiskGroup": raidDiskGroup,
       "raidDiskStatus": raidDiskStatus,
       "raidDiskReconPercentage": raidDiskReconPercentage,
       "raidDiskReconMinutes": raidDiskReconMinutes,
       "raidDiskResynchPercentage": raidDiskResynchPercentage,
       "raidDiskResynchMinutes": raidDiskResynchMinutes,
       "replication": replication,
       "replicationInfo": replicationInfo,
       "replicationInfoTable": replicationInfoTable,
       "replicationInfoEntry": replicationInfoEntry,
       "replContext": replContext,
       "replState": replState,
       "replStatus": replStatus,
       "replFileSysStatus": replFileSysStatus,
       "replConnTime": replConnTime,
       "replSource": replSource,
       "replDestination": replDestination,
       "replLag": replLag,
       "replPreCompBytesSent": replPreCompBytesSent,
       "replPostCompBytesSent": replPostCompBytesSent,
       "replPreCompBytesRemaining": replPreCompBytesRemaining,
       "replPostCompBytesReceived": replPostCompBytesReceived,
       "replThrottle": replThrottle,
       "replSyncedAsOfTime": replSyncedAsOfTime,
       "dataDomainMibNotifications": dataDomainMibNotifications,
       "powerSupplyFailedAlarm": powerSupplyFailedAlarm,
       "systemOverheatWarningAlarm": systemOverheatWarningAlarm,
       "systemOverheatAlertAlarm": systemOverheatAlertAlarm,
       "systemOverheatShutdowntAlarm": systemOverheatShutdowntAlarm,
       "fanModuleFailedAlarm": fanModuleFailedAlarm,
       "nvramFailingAlarm": nvramFailingAlarm,
       "fileSystemFailedAlarm": fileSystemFailedAlarm,
       "fileSpaceMaintenanceAlarm": fileSpaceMaintenanceAlarm,
       "fileSpaceWarningAlarm": fileSpaceWarningAlarm,
       "fileSpaceSevereAlarm": fileSpaceSevereAlarm,
       "fileSpaceCriticalAlarm": fileSpaceCriticalAlarm,
       "diskFailingAlarm": diskFailingAlarm,
       "diskFailedAlarm": diskFailedAlarm,
       "diskOverheatWarningAlarm": diskOverheatWarningAlarm,
       "diskOverheatAlertAlarm": diskOverheatAlertAlarm,
       "diskOverheatShutdowntAlarm": diskOverheatShutdowntAlarm,
       "raidReconSevereAlarm": raidReconSevereAlarm,
       "raidReconCriticalAlarm": raidReconCriticalAlarm,
       "raidReconCriticalShutdownAlarm": raidReconCriticalShutdownAlarm,
       "products": products,
       "restorer": restorer,
       "dd200": dd200,
       "dd200Proto": dd200Proto,
       "dd410": dd410,
       "dd430": dd430,
       "dd460": dd460,
       "dd400g": dd400g,
       "dd460g": dd460g,
       "dd560": dd560,
       "dd560g": dd560g,
       "dd580": dd580,
       "dd580g": dd580g,
       "dd565": dd565,
       "dd530": dd530,
       "dd510": dd510,
       "dd120": dd120,
       "dd590": dd590,
       "dd590g": dd590g,
       "ddModelUnsupported": ddModelUnsupported}
)
