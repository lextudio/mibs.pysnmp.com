# SNMP MIB module (ELTEX-LTP8X-STANDALONE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-LTP8X-STANDALONE
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:17 2024
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

(ltp8x,) = mibBuilder.importSymbols(
    "ELTEX-LTP8X",
    "ltp8x")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ltp8xStandalone = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1)
)
ltp8xStandalone.setRevisions(
        ("2010-07-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ltp8xSystem_ObjectIdentity = ObjectIdentity
ltp8xSystem = _Ltp8xSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1)
)
_Ltp8xHostName_Type = DisplayString
_Ltp8xHostName_Object = MibScalar
ltp8xHostName = _Ltp8xHostName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 1),
    _Ltp8xHostName_Type()
)
ltp8xHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xHostName.setStatus("current")
_Ltp8xIPAddress_Type = IpAddress
_Ltp8xIPAddress_Object = MibScalar
ltp8xIPAddress = _Ltp8xIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 2),
    _Ltp8xIPAddress_Type()
)
ltp8xIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xIPAddress.setStatus("current")
_Ltp8xNetMask_Type = IpAddress
_Ltp8xNetMask_Object = MibScalar
ltp8xNetMask = _Ltp8xNetMask_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 3),
    _Ltp8xNetMask_Type()
)
ltp8xNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xNetMask.setStatus("current")
_Ltp8xGateway_Type = IpAddress
_Ltp8xGateway_Object = MibScalar
ltp8xGateway = _Ltp8xGateway_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 4),
    _Ltp8xGateway_Type()
)
ltp8xGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xGateway.setStatus("current")
_Ltp8xVLAN_Type = Unsigned32
_Ltp8xVLAN_Object = MibScalar
ltp8xVLAN = _Ltp8xVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 5),
    _Ltp8xVLAN_Type()
)
ltp8xVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xVLAN.setStatus("current")
_Ltp8xFirmwareRevision_Type = DisplayString
_Ltp8xFirmwareRevision_Object = MibScalar
ltp8xFirmwareRevision = _Ltp8xFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 6),
    _Ltp8xFirmwareRevision_Type()
)
ltp8xFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xFirmwareRevision.setStatus("current")
_Ltp8xSystemUptime_Type = Unsigned32
_Ltp8xSystemUptime_Object = MibScalar
ltp8xSystemUptime = _Ltp8xSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 7),
    _Ltp8xSystemUptime_Type()
)
ltp8xSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSystemUptime.setStatus("current")
_Ltp8xSystemHardwareRevision_Type = DisplayString
_Ltp8xSystemHardwareRevision_Object = MibScalar
ltp8xSystemHardwareRevision = _Ltp8xSystemHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 8),
    _Ltp8xSystemHardwareRevision_Type()
)
ltp8xSystemHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSystemHardwareRevision.setStatus("current")
_Ltp8xSystemMacAddress_Type = DisplayString
_Ltp8xSystemMacAddress_Object = MibScalar
ltp8xSystemMacAddress = _Ltp8xSystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 9),
    _Ltp8xSystemMacAddress_Type()
)
ltp8xSystemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSystemMacAddress.setStatus("current")
_Ltp8xSystemDeviceName_Type = DisplayString
_Ltp8xSystemDeviceName_Object = MibScalar
ltp8xSystemDeviceName = _Ltp8xSystemDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 10),
    _Ltp8xSystemDeviceName_Type()
)
ltp8xSystemDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSystemDeviceName.setStatus("current")
_Ltp8xServicesControlTable_Object = MibTable
ltp8xServicesControlTable = _Ltp8xServicesControlTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2)
)
if mibBuilder.loadTexts:
    ltp8xServicesControlTable.setStatus("current")
_Ltp8xServicesControlEntry_Object = MibTableRow
ltp8xServicesControlEntry = _Ltp8xServicesControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1)
)
ltp8xServicesControlEntry.setIndexNames(
    (0, "ELTEX-LTP8X-STANDALONE", "ltp8xServicesControlIndex"),
)
if mibBuilder.loadTexts:
    ltp8xServicesControlEntry.setStatus("current")
_Ltp8xServicesControlIndex_Type = Unsigned32
_Ltp8xServicesControlIndex_Object = MibTableColumn
ltp8xServicesControlIndex = _Ltp8xServicesControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1, 1),
    _Ltp8xServicesControlIndex_Type()
)
ltp8xServicesControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xServicesControlIndex.setStatus("current")
_Ltp8xServicesControlName_Type = DisplayString
_Ltp8xServicesControlName_Object = MibTableColumn
ltp8xServicesControlName = _Ltp8xServicesControlName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1, 2),
    _Ltp8xServicesControlName_Type()
)
ltp8xServicesControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xServicesControlName.setStatus("current")
_Ltp8xServicesControlEnabled_Type = TruthValue
_Ltp8xServicesControlEnabled_Object = MibTableColumn
ltp8xServicesControlEnabled = _Ltp8xServicesControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1, 3),
    _Ltp8xServicesControlEnabled_Type()
)
ltp8xServicesControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xServicesControlEnabled.setStatus("current")
_Ltp8xBoardStatus_ObjectIdentity = ObjectIdentity
ltp8xBoardStatus = _Ltp8xBoardStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10)
)
_Ltp8xDiskFreeSpace_Type = Unsigned32
_Ltp8xDiskFreeSpace_Object = MibScalar
ltp8xDiskFreeSpace = _Ltp8xDiskFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 1),
    _Ltp8xDiskFreeSpace_Type()
)
ltp8xDiskFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xDiskFreeSpace.setStatus("current")
_Ltp8xRAMFree_Type = Unsigned32
_Ltp8xRAMFree_Object = MibScalar
ltp8xRAMFree = _Ltp8xRAMFree_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 2),
    _Ltp8xRAMFree_Type()
)
ltp8xRAMFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xRAMFree.setStatus("current")
_Ltp8xCPULoadAverage1Minute_Type = Unsigned32
_Ltp8xCPULoadAverage1Minute_Object = MibScalar
ltp8xCPULoadAverage1Minute = _Ltp8xCPULoadAverage1Minute_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 3),
    _Ltp8xCPULoadAverage1Minute_Type()
)
ltp8xCPULoadAverage1Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xCPULoadAverage1Minute.setStatus("current")
_Ltp8xCPULoadAverage5Minutes_Type = Unsigned32
_Ltp8xCPULoadAverage5Minutes_Object = MibScalar
ltp8xCPULoadAverage5Minutes = _Ltp8xCPULoadAverage5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 4),
    _Ltp8xCPULoadAverage5Minutes_Type()
)
ltp8xCPULoadAverage5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xCPULoadAverage5Minutes.setStatus("current")
_Ltp8xCPULoadAverage15Minutes_Type = Unsigned32
_Ltp8xCPULoadAverage15Minutes_Object = MibScalar
ltp8xCPULoadAverage15Minutes = _Ltp8xCPULoadAverage15Minutes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 5),
    _Ltp8xCPULoadAverage15Minutes_Type()
)
ltp8xCPULoadAverage15Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xCPULoadAverage15Minutes.setStatus("current")
_Ltp8xFan0Active_Type = TruthValue
_Ltp8xFan0Active_Object = MibScalar
ltp8xFan0Active = _Ltp8xFan0Active_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 6),
    _Ltp8xFan0Active_Type()
)
ltp8xFan0Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xFan0Active.setStatus("current")
_Ltp8xFan0RPM_Type = Unsigned32
_Ltp8xFan0RPM_Object = MibScalar
ltp8xFan0RPM = _Ltp8xFan0RPM_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 7),
    _Ltp8xFan0RPM_Type()
)
ltp8xFan0RPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xFan0RPM.setStatus("current")
_Ltp8xFan1Active_Type = TruthValue
_Ltp8xFan1Active_Object = MibScalar
ltp8xFan1Active = _Ltp8xFan1Active_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 8),
    _Ltp8xFan1Active_Type()
)
ltp8xFan1Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xFan1Active.setStatus("current")
_Ltp8xFan1RPM_Type = Unsigned32
_Ltp8xFan1RPM_Object = MibScalar
ltp8xFan1RPM = _Ltp8xFan1RPM_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 9),
    _Ltp8xFan1RPM_Type()
)
ltp8xFan1RPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xFan1RPM.setStatus("current")
_Ltp8xSensor1Temperature_Type = Unsigned32
_Ltp8xSensor1Temperature_Object = MibScalar
ltp8xSensor1Temperature = _Ltp8xSensor1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 10),
    _Ltp8xSensor1Temperature_Type()
)
ltp8xSensor1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSensor1Temperature.setStatus("current")
_Ltp8xSensor2Temperature_Type = Unsigned32
_Ltp8xSensor2Temperature_Object = MibScalar
ltp8xSensor2Temperature = _Ltp8xSensor2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 11),
    _Ltp8xSensor2Temperature_Type()
)
ltp8xSensor2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSensor2Temperature.setStatus("current")


class _Ltp8xSensor1TemperatureExt_Type(Integer32):
    """Custom type ltp8xSensor1TemperatureExt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("notValid", 65535)
    )


_Ltp8xSensor1TemperatureExt_Type.__name__ = "Integer32"
_Ltp8xSensor1TemperatureExt_Object = MibScalar
ltp8xSensor1TemperatureExt = _Ltp8xSensor1TemperatureExt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 12),
    _Ltp8xSensor1TemperatureExt_Type()
)
ltp8xSensor1TemperatureExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSensor1TemperatureExt.setStatus("current")


class _Ltp8xSensor2TemperatureExt_Type(Integer32):
    """Custom type ltp8xSensor2TemperatureExt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("notValid", 65535)
    )


_Ltp8xSensor2TemperatureExt_Type.__name__ = "Integer32"
_Ltp8xSensor2TemperatureExt_Object = MibScalar
ltp8xSensor2TemperatureExt = _Ltp8xSensor2TemperatureExt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 13),
    _Ltp8xSensor2TemperatureExt_Type()
)
ltp8xSensor2TemperatureExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xSensor2TemperatureExt.setStatus("current")
_Ltp8xFanMinRPM_Type = Unsigned32
_Ltp8xFanMinRPM_Object = MibScalar
ltp8xFanMinRPM = _Ltp8xFanMinRPM_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 20),
    _Ltp8xFanMinRPM_Type()
)
ltp8xFanMinRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xFanMinRPM.setStatus("current")
_Ltp8xFanMaxRPM_Type = Unsigned32
_Ltp8xFanMaxRPM_Object = MibScalar
ltp8xFanMaxRPM = _Ltp8xFanMaxRPM_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 21),
    _Ltp8xFanMaxRPM_Type()
)
ltp8xFanMaxRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xFanMaxRPM.setStatus("current")
_Ltp8xUsers_ObjectIdentity = ObjectIdentity
ltp8xUsers = _Ltp8xUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11)
)
_Ltp8xUsersTable_Object = MibTable
ltp8xUsersTable = _Ltp8xUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1)
)
if mibBuilder.loadTexts:
    ltp8xUsersTable.setStatus("current")
_Ltp8xUsersEntry_Object = MibTableRow
ltp8xUsersEntry = _Ltp8xUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1)
)
ltp8xUsersEntry.setIndexNames(
    (0, "ELTEX-LTP8X-STANDALONE", "ltp8xUsersName"),
)
if mibBuilder.loadTexts:
    ltp8xUsersEntry.setStatus("current")


class _Ltp8xUsersName_Type(DisplayString):
    """Custom type ltp8xUsersName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ltp8xUsersName_Type.__name__ = "DisplayString"
_Ltp8xUsersName_Object = MibTableColumn
ltp8xUsersName = _Ltp8xUsersName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 1),
    _Ltp8xUsersName_Type()
)
ltp8xUsersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xUsersName.setStatus("current")


class _Ltp8xUsersGroups_Type(OctetString):
    """Custom type ltp8xUsersGroups based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Ltp8xUsersGroups_Type.__name__ = "OctetString"
_Ltp8xUsersGroups_Object = MibTableColumn
ltp8xUsersGroups = _Ltp8xUsersGroups_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 2),
    _Ltp8xUsersGroups_Type()
)
ltp8xUsersGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xUsersGroups.setStatus("current")
_Ltp8xUsersOldPassword_Type = DisplayString
_Ltp8xUsersOldPassword_Object = MibTableColumn
ltp8xUsersOldPassword = _Ltp8xUsersOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 3),
    _Ltp8xUsersOldPassword_Type()
)
ltp8xUsersOldPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xUsersOldPassword.setStatus("current")
_Ltp8xUsersNewPassword_Type = DisplayString
_Ltp8xUsersNewPassword_Object = MibTableColumn
ltp8xUsersNewPassword = _Ltp8xUsersNewPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 4),
    _Ltp8xUsersNewPassword_Type()
)
ltp8xUsersNewPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xUsersNewPassword.setStatus("current")
_Ltp8xUsersRowStatus_Type = RowStatus
_Ltp8xUsersRowStatus_Object = MibTableColumn
ltp8xUsersRowStatus = _Ltp8xUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 5),
    _Ltp8xUsersRowStatus_Type()
)
ltp8xUsersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xUsersRowStatus.setStatus("current")
_Ltp8xUsersPriority_Type = Unsigned32
_Ltp8xUsersPriority_Object = MibTableColumn
ltp8xUsersPriority = _Ltp8xUsersPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 6),
    _Ltp8xUsersPriority_Type()
)
ltp8xUsersPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xUsersPriority.setStatus("current")
_Ltp8xUsersGroupsTable_Object = MibTable
ltp8xUsersGroupsTable = _Ltp8xUsersGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2)
)
if mibBuilder.loadTexts:
    ltp8xUsersGroupsTable.setStatus("current")
_Ltp8xUsersGroupsEntry_Object = MibTableRow
ltp8xUsersGroupsEntry = _Ltp8xUsersGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2, 1)
)
ltp8xUsersGroupsEntry.setIndexNames(
    (0, "ELTEX-LTP8X-STANDALONE", "ltp8xUsersGroupsID"),
)
if mibBuilder.loadTexts:
    ltp8xUsersGroupsEntry.setStatus("current")
_Ltp8xUsersGroupsID_Type = Unsigned32
_Ltp8xUsersGroupsID_Object = MibTableColumn
ltp8xUsersGroupsID = _Ltp8xUsersGroupsID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2, 1, 1),
    _Ltp8xUsersGroupsID_Type()
)
ltp8xUsersGroupsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xUsersGroupsID.setStatus("current")
_Ltp8xUsersGroupsName_Type = DisplayString
_Ltp8xUsersGroupsName_Object = MibTableColumn
ltp8xUsersGroupsName = _Ltp8xUsersGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2, 1, 2),
    _Ltp8xUsersGroupsName_Type()
)
ltp8xUsersGroupsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xUsersGroupsName.setStatus("current")
_Ltp8xPrivilegesNamesTable_Object = MibTable
ltp8xPrivilegesNamesTable = _Ltp8xPrivilegesNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3)
)
if mibBuilder.loadTexts:
    ltp8xPrivilegesNamesTable.setStatus("current")
_Ltp8xPrivilegesNamesEntry_Object = MibTableRow
ltp8xPrivilegesNamesEntry = _Ltp8xPrivilegesNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3, 1)
)
ltp8xPrivilegesNamesEntry.setIndexNames(
    (0, "ELTEX-LTP8X-STANDALONE", "ltp8xPrivilegesNamesIndex"),
)
if mibBuilder.loadTexts:
    ltp8xPrivilegesNamesEntry.setStatus("current")
_Ltp8xPrivilegesNamesIndex_Type = Unsigned32
_Ltp8xPrivilegesNamesIndex_Object = MibTableColumn
ltp8xPrivilegesNamesIndex = _Ltp8xPrivilegesNamesIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3, 1, 1),
    _Ltp8xPrivilegesNamesIndex_Type()
)
ltp8xPrivilegesNamesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xPrivilegesNamesIndex.setStatus("current")
_Ltp8xPrivilegesNamesName_Type = DisplayString
_Ltp8xPrivilegesNamesName_Object = MibTableColumn
ltp8xPrivilegesNamesName = _Ltp8xPrivilegesNamesName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3, 1, 2),
    _Ltp8xPrivilegesNamesName_Type()
)
ltp8xPrivilegesNamesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPrivilegesNamesName.setStatus("current")
_Ltp8xPrivilegesLevelsTable_Object = MibTable
ltp8xPrivilegesLevelsTable = _Ltp8xPrivilegesLevelsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4)
)
if mibBuilder.loadTexts:
    ltp8xPrivilegesLevelsTable.setStatus("current")
_Ltp8xPrivilegesLevelsEntry_Object = MibTableRow
ltp8xPrivilegesLevelsEntry = _Ltp8xPrivilegesLevelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4, 1)
)
ltp8xPrivilegesLevelsEntry.setIndexNames(
    (0, "ELTEX-LTP8X-STANDALONE", "ltp8xPrivilegesLevelsLevel"),
)
if mibBuilder.loadTexts:
    ltp8xPrivilegesLevelsEntry.setStatus("current")
_Ltp8xPrivilegesLevelsLevel_Type = Unsigned32
_Ltp8xPrivilegesLevelsLevel_Object = MibTableColumn
ltp8xPrivilegesLevelsLevel = _Ltp8xPrivilegesLevelsLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4, 1, 1),
    _Ltp8xPrivilegesLevelsLevel_Type()
)
ltp8xPrivilegesLevelsLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xPrivilegesLevelsLevel.setStatus("current")


class _Ltp8xPrivilegesLevelsAllowed_Type(OctetString):
    """Custom type ltp8xPrivilegesLevelsAllowed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Ltp8xPrivilegesLevelsAllowed_Type.__name__ = "OctetString"
_Ltp8xPrivilegesLevelsAllowed_Object = MibTableColumn
ltp8xPrivilegesLevelsAllowed = _Ltp8xPrivilegesLevelsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4, 1, 2),
    _Ltp8xPrivilegesLevelsAllowed_Type()
)
ltp8xPrivilegesLevelsAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xPrivilegesLevelsAllowed.setStatus("current")
_Ltp8xLogSubmodulesTable_Object = MibTable
ltp8xLogSubmodulesTable = _Ltp8xLogSubmodulesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12)
)
if mibBuilder.loadTexts:
    ltp8xLogSubmodulesTable.setStatus("current")
_Ltp8xLogSubmodulesEntry_Object = MibTableRow
ltp8xLogSubmodulesEntry = _Ltp8xLogSubmodulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1)
)
ltp8xLogSubmodulesEntry.setIndexNames(
    (0, "ELTEX-LTP8X-STANDALONE", "ltp8xLogSubmodulesID"),
)
if mibBuilder.loadTexts:
    ltp8xLogSubmodulesEntry.setStatus("current")


class _Ltp8xLogSubmodulesID_Type(Integer32):
    """Custom type ltp8xLogSubmodulesID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ltp8xLogSubmodulesID_Type.__name__ = "Integer32"
_Ltp8xLogSubmodulesID_Object = MibTableColumn
ltp8xLogSubmodulesID = _Ltp8xLogSubmodulesID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 1),
    _Ltp8xLogSubmodulesID_Type()
)
ltp8xLogSubmodulesID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xLogSubmodulesID.setStatus("current")


class _Ltp8xLogSubmodulesName_Type(DisplayString):
    """Custom type ltp8xLogSubmodulesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ltp8xLogSubmodulesName_Type.__name__ = "DisplayString"
_Ltp8xLogSubmodulesName_Object = MibTableColumn
ltp8xLogSubmodulesName = _Ltp8xLogSubmodulesName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 2),
    _Ltp8xLogSubmodulesName_Type()
)
ltp8xLogSubmodulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xLogSubmodulesName.setStatus("current")


class _Ltp8xLogSubmodulesLevel_Type(Integer32):
    """Custom type ltp8xLogSubmodulesLevel based on Integer32"""
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
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("none", 8),
          ("notice", 5),
          ("warning", 4))
    )


_Ltp8xLogSubmodulesLevel_Type.__name__ = "Integer32"
_Ltp8xLogSubmodulesLevel_Object = MibTableColumn
ltp8xLogSubmodulesLevel = _Ltp8xLogSubmodulesLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 3),
    _Ltp8xLogSubmodulesLevel_Type()
)
ltp8xLogSubmodulesLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xLogSubmodulesLevel.setStatus("current")


class _Ltp8xLogSubmodulesDestination_Type(Integer32):
    """Custom type ltp8xLogSubmodulesDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("syslog", 0),
          ("telnet", 2))
    )


_Ltp8xLogSubmodulesDestination_Type.__name__ = "Integer32"
_Ltp8xLogSubmodulesDestination_Object = MibTableColumn
ltp8xLogSubmodulesDestination = _Ltp8xLogSubmodulesDestination_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 4),
    _Ltp8xLogSubmodulesDestination_Type()
)
ltp8xLogSubmodulesDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xLogSubmodulesDestination.setStatus("current")
_Ltp8xLogSubmodulesShowProgName_Type = TruthValue
_Ltp8xLogSubmodulesShowProgName_Object = MibTableColumn
ltp8xLogSubmodulesShowProgName = _Ltp8xLogSubmodulesShowProgName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 5),
    _Ltp8xLogSubmodulesShowProgName_Type()
)
ltp8xLogSubmodulesShowProgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xLogSubmodulesShowProgName.setStatus("current")
_Ltp8xLogSubmodulesShowSubmoduleName_Type = TruthValue
_Ltp8xLogSubmodulesShowSubmoduleName_Object = MibTableColumn
ltp8xLogSubmodulesShowSubmoduleName = _Ltp8xLogSubmodulesShowSubmoduleName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 6),
    _Ltp8xLogSubmodulesShowSubmoduleName_Type()
)
ltp8xLogSubmodulesShowSubmoduleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xLogSubmodulesShowSubmoduleName.setStatus("current")
_Ltp8xLogSubmodulesShowLevel_Type = TruthValue
_Ltp8xLogSubmodulesShowLevel_Object = MibTableColumn
ltp8xLogSubmodulesShowLevel = _Ltp8xLogSubmodulesShowLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 7),
    _Ltp8xLogSubmodulesShowLevel_Type()
)
ltp8xLogSubmodulesShowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xLogSubmodulesShowLevel.setStatus("current")
_Ltp8xLogSubmodulesShowTime_Type = TruthValue
_Ltp8xLogSubmodulesShowTime_Object = MibTableColumn
ltp8xLogSubmodulesShowTime = _Ltp8xLogSubmodulesShowTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 8),
    _Ltp8xLogSubmodulesShowTime_Type()
)
ltp8xLogSubmodulesShowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xLogSubmodulesShowTime.setStatus("current")
_Ltp8xActivationAuthModeTable_Object = MibTable
ltp8xActivationAuthModeTable = _Ltp8xActivationAuthModeTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13)
)
if mibBuilder.loadTexts:
    ltp8xActivationAuthModeTable.setStatus("current")
_Ltp8xActivationAuthModeEntry_Object = MibTableRow
ltp8xActivationAuthModeEntry = _Ltp8xActivationAuthModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13, 1)
)
ltp8xActivationAuthModeEntry.setIndexNames(
    (0, "ELTEX-LTP8X-STANDALONE", "ltp8xActivationAuthModeChannel"),
)
if mibBuilder.loadTexts:
    ltp8xActivationAuthModeEntry.setStatus("current")
_Ltp8xActivationAuthModeChannel_Type = Unsigned32
_Ltp8xActivationAuthModeChannel_Object = MibTableColumn
ltp8xActivationAuthModeChannel = _Ltp8xActivationAuthModeChannel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13, 1, 1),
    _Ltp8xActivationAuthModeChannel_Type()
)
ltp8xActivationAuthModeChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xActivationAuthModeChannel.setStatus("current")
_Ltp8xActivationAuthModeHostControlledLumpedSN_Type = TruthValue
_Ltp8xActivationAuthModeHostControlledLumpedSN_Object = MibTableColumn
ltp8xActivationAuthModeHostControlledLumpedSN = _Ltp8xActivationAuthModeHostControlledLumpedSN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13, 1, 2),
    _Ltp8xActivationAuthModeHostControlledLumpedSN_Type()
)
ltp8xActivationAuthModeHostControlledLumpedSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xActivationAuthModeHostControlledLumpedSN.setStatus("current")
_Ltp8xLoggingDestinationsTable_Object = MibTable
ltp8xLoggingDestinationsTable = _Ltp8xLoggingDestinationsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14)
)
if mibBuilder.loadTexts:
    ltp8xLoggingDestinationsTable.setStatus("current")
_Ltp8xLoggingDestinationsEntry_Object = MibTableRow
ltp8xLoggingDestinationsEntry = _Ltp8xLoggingDestinationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1)
)
ltp8xLoggingDestinationsEntry.setIndexNames(
    (0, "ELTEX-LTP8X-STANDALONE", "ltp8xLoggingDestinationsId"),
)
if mibBuilder.loadTexts:
    ltp8xLoggingDestinationsEntry.setStatus("current")
_Ltp8xLoggingDestinationsId_Type = Unsigned32
_Ltp8xLoggingDestinationsId_Object = MibTableColumn
ltp8xLoggingDestinationsId = _Ltp8xLoggingDestinationsId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1, 1),
    _Ltp8xLoggingDestinationsId_Type()
)
ltp8xLoggingDestinationsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xLoggingDestinationsId.setStatus("current")
_Ltp8xLoggingDestinationsName_Type = DisplayString
_Ltp8xLoggingDestinationsName_Object = MibTableColumn
ltp8xLoggingDestinationsName = _Ltp8xLoggingDestinationsName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1, 2),
    _Ltp8xLoggingDestinationsName_Type()
)
ltp8xLoggingDestinationsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xLoggingDestinationsName.setStatus("current")


class _Ltp8xLoggingDestinationsLevel_Type(Integer32):
    """Custom type ltp8xLoggingDestinationsLevel based on Integer32"""
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
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("none", 8),
          ("notice", 5),
          ("warning", 4))
    )


_Ltp8xLoggingDestinationsLevel_Type.__name__ = "Integer32"
_Ltp8xLoggingDestinationsLevel_Object = MibTableColumn
ltp8xLoggingDestinationsLevel = _Ltp8xLoggingDestinationsLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1, 3),
    _Ltp8xLoggingDestinationsLevel_Type()
)
ltp8xLoggingDestinationsLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xLoggingDestinationsLevel.setStatus("current")
_Ltp8xInterfaceStatusTable_Object = MibTable
ltp8xInterfaceStatusTable = _Ltp8xInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15)
)
if mibBuilder.loadTexts:
    ltp8xInterfaceStatusTable.setStatus("current")
_Ltp8xInterfaceStatusEntry_Object = MibTableRow
ltp8xInterfaceStatusEntry = _Ltp8xInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1)
)
ltp8xInterfaceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ltp8xInterfaceStatusEntry.setStatus("current")
_Ltp8xInterfaceStatusError_Type = TruthValue
_Ltp8xInterfaceStatusError_Object = MibTableColumn
ltp8xInterfaceStatusError = _Ltp8xInterfaceStatusError_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1, 1),
    _Ltp8xInterfaceStatusError_Type()
)
ltp8xInterfaceStatusError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xInterfaceStatusError.setStatus("current")


class _Ltp8xInterfaceStatusDuplex_Type(Integer32):
    """Custom type ltp8xInterfaceStatusDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 0))
    )


_Ltp8xInterfaceStatusDuplex_Type.__name__ = "Integer32"
_Ltp8xInterfaceStatusDuplex_Object = MibTableColumn
ltp8xInterfaceStatusDuplex = _Ltp8xInterfaceStatusDuplex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1, 2),
    _Ltp8xInterfaceStatusDuplex_Type()
)
ltp8xInterfaceStatusDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xInterfaceStatusDuplex.setStatus("current")
_Ltp8xInterfaceStatusFlowControlEnabled_Type = TruthValue
_Ltp8xInterfaceStatusFlowControlEnabled_Object = MibTableColumn
ltp8xInterfaceStatusFlowControlEnabled = _Ltp8xInterfaceStatusFlowControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1, 3),
    _Ltp8xInterfaceStatusFlowControlEnabled_Type()
)
ltp8xInterfaceStatusFlowControlEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xInterfaceStatusFlowControlEnabled.setStatus("current")
_Ltp8xFanControl_ObjectIdentity = ObjectIdentity
ltp8xFanControl = _Ltp8xFanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 16)
)


class _Ltp8xFanSpeed_Type(Integer32):
    """Custom type ltp8xFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("auto", -1)
    )


_Ltp8xFanSpeed_Type.__name__ = "Integer32"
_Ltp8xFanSpeed_Object = MibScalar
ltp8xFanSpeed = _Ltp8xFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 16, 1),
    _Ltp8xFanSpeed_Type()
)
ltp8xFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xFanSpeed.setStatus("current")
_Ltp8xFanMinSpeed_Type = Unsigned32
_Ltp8xFanMinSpeed_Object = MibScalar
ltp8xFanMinSpeed = _Ltp8xFanMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 16, 2),
    _Ltp8xFanMinSpeed_Type()
)
ltp8xFanMinSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xFanMinSpeed.setStatus("current")
_Ltp8xPowerSupplyTable_Object = MibTable
ltp8xPowerSupplyTable = _Ltp8xPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17)
)
if mibBuilder.loadTexts:
    ltp8xPowerSupplyTable.setStatus("current")
_Ltp8xPowerSupplyEntry_Object = MibTableRow
ltp8xPowerSupplyEntry = _Ltp8xPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1)
)
ltp8xPowerSupplyEntry.setIndexNames(
    (0, "ELTEX-LTP8X-STANDALONE", "ltp8xPowerSupplyModuleId"),
)
if mibBuilder.loadTexts:
    ltp8xPowerSupplyEntry.setStatus("current")
_Ltp8xPowerSupplyModuleId_Type = Unsigned32
_Ltp8xPowerSupplyModuleId_Object = MibTableColumn
ltp8xPowerSupplyModuleId = _Ltp8xPowerSupplyModuleId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 1),
    _Ltp8xPowerSupplyModuleId_Type()
)
ltp8xPowerSupplyModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ltp8xPowerSupplyModuleId.setStatus("current")
_Ltp8xPowerSupplyModulePresent_Type = TruthValue
_Ltp8xPowerSupplyModulePresent_Object = MibTableColumn
ltp8xPowerSupplyModulePresent = _Ltp8xPowerSupplyModulePresent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 2),
    _Ltp8xPowerSupplyModulePresent_Type()
)
ltp8xPowerSupplyModulePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPowerSupplyModulePresent.setStatus("current")
_Ltp8xPowerSupplyModuleName_Type = DisplayString
_Ltp8xPowerSupplyModuleName_Object = MibTableColumn
ltp8xPowerSupplyModuleName = _Ltp8xPowerSupplyModuleName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 3),
    _Ltp8xPowerSupplyModuleName_Type()
)
ltp8xPowerSupplyModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPowerSupplyModuleName.setStatus("current")


class _Ltp8xPowerSupplyModuleType_Type(Integer32):
    """Custom type ltp8xPowerSupplyModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alternateCurrent", 1),
          ("directCurrent", 0))
    )


_Ltp8xPowerSupplyModuleType_Type.__name__ = "Integer32"
_Ltp8xPowerSupplyModuleType_Object = MibTableColumn
ltp8xPowerSupplyModuleType = _Ltp8xPowerSupplyModuleType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 4),
    _Ltp8xPowerSupplyModuleType_Type()
)
ltp8xPowerSupplyModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPowerSupplyModuleType.setStatus("current")
_Ltp8xPowerSupplyModuleIntact_Type = TruthValue
_Ltp8xPowerSupplyModuleIntact_Object = MibTableColumn
ltp8xPowerSupplyModuleIntact = _Ltp8xPowerSupplyModuleIntact_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 5),
    _Ltp8xPowerSupplyModuleIntact_Type()
)
ltp8xPowerSupplyModuleIntact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xPowerSupplyModuleIntact.setStatus("current")
_Ltp8xLicense_ObjectIdentity = ObjectIdentity
ltp8xLicense = _Ltp8xLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18)
)
_Ltp8xLicenseInstalled_Type = TruthValue
_Ltp8xLicenseInstalled_Object = MibScalar
ltp8xLicenseInstalled = _Ltp8xLicenseInstalled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 1),
    _Ltp8xLicenseInstalled_Type()
)
ltp8xLicenseInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xLicenseInstalled.setStatus("current")
_Ltp8xLicenseValid_Type = TruthValue
_Ltp8xLicenseValid_Object = MibScalar
ltp8xLicenseValid = _Ltp8xLicenseValid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 2),
    _Ltp8xLicenseValid_Type()
)
ltp8xLicenseValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xLicenseValid.setStatus("current")


class _Ltp8xLicenseVersion_Type(Integer32):
    """Custom type ltp8xLicenseVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1v0", 0),
          ("version1v1", 1),
          ("version1v2", 2))
    )


_Ltp8xLicenseVersion_Type.__name__ = "Integer32"
_Ltp8xLicenseVersion_Object = MibScalar
ltp8xLicenseVersion = _Ltp8xLicenseVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 3),
    _Ltp8xLicenseVersion_Type()
)
ltp8xLicenseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xLicenseVersion.setStatus("current")
_Ltp8xLicenseBoardSN_Type = DisplayString
_Ltp8xLicenseBoardSN_Object = MibScalar
ltp8xLicenseBoardSN = _Ltp8xLicenseBoardSN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 4),
    _Ltp8xLicenseBoardSN_Type()
)
ltp8xLicenseBoardSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xLicenseBoardSN.setStatus("current")
_Ltp8xLicenseVendor_Type = DisplayString
_Ltp8xLicenseVendor_Object = MibScalar
ltp8xLicenseVendor = _Ltp8xLicenseVendor_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 5),
    _Ltp8xLicenseVendor_Type()
)
ltp8xLicenseVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xLicenseVendor.setStatus("current")


class _Ltp8xLicenseONTCount_Type(Integer32):
    """Custom type ltp8xLicenseONTCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", -1),
          ("unlimited", 2147483647))
    )


_Ltp8xLicenseONTCount_Type.__name__ = "Integer32"
_Ltp8xLicenseONTCount_Object = MibScalar
ltp8xLicenseONTCount = _Ltp8xLicenseONTCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 6),
    _Ltp8xLicenseONTCount_Type()
)
ltp8xLicenseONTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xLicenseONTCount.setStatus("current")


class _Ltp8xLicenseActiveONTCount_Type(Integer32):
    """Custom type ltp8xLicenseActiveONTCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("notAvailable", -1)
    )


_Ltp8xLicenseActiveONTCount_Type.__name__ = "Integer32"
_Ltp8xLicenseActiveONTCount_Object = MibScalar
ltp8xLicenseActiveONTCount = _Ltp8xLicenseActiveONTCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 7),
    _Ltp8xLicenseActiveONTCount_Type()
)
ltp8xLicenseActiveONTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xLicenseActiveONTCount.setStatus("current")
_Ltp8xLogSize_Type = Unsigned32
_Ltp8xLogSize_Object = MibScalar
ltp8xLogSize = _Ltp8xLogSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 20),
    _Ltp8xLogSize_Type()
)
ltp8xLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xLogSize.setStatus("current")
_Ltp8xExternalFirmwareIP_Type = IpAddress
_Ltp8xExternalFirmwareIP_Object = MibScalar
ltp8xExternalFirmwareIP = _Ltp8xExternalFirmwareIP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 21),
    _Ltp8xExternalFirmwareIP_Type()
)
ltp8xExternalFirmwareIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xExternalFirmwareIP.setStatus("current")
_Ltp8xExternalFirmwarePort_Type = Unsigned32
_Ltp8xExternalFirmwarePort_Object = MibScalar
ltp8xExternalFirmwarePort = _Ltp8xExternalFirmwarePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 22),
    _Ltp8xExternalFirmwarePort_Type()
)
ltp8xExternalFirmwarePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xExternalFirmwarePort.setStatus("current")
_Ltp8xNTPDaylightSaving_Type = TruthValue
_Ltp8xNTPDaylightSaving_Object = MibScalar
ltp8xNTPDaylightSaving = _Ltp8xNTPDaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 25),
    _Ltp8xNTPDaylightSaving_Type()
)
ltp8xNTPDaylightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xNTPDaylightSaving.setStatus("current")
_Ltp8xONTFwAutoUpdateEnabled_Type = TruthValue
_Ltp8xONTFwAutoUpdateEnabled_Object = MibScalar
ltp8xONTFwAutoUpdateEnabled = _Ltp8xONTFwAutoUpdateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 26),
    _Ltp8xONTFwAutoUpdateEnabled_Type()
)
ltp8xONTFwAutoUpdateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xONTFwAutoUpdateEnabled.setStatus("current")
_Ltp8xConfigChangeCounter_Type = Unsigned32
_Ltp8xConfigChangeCounter_Object = MibScalar
ltp8xConfigChangeCounter = _Ltp8xConfigChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 40),
    _Ltp8xConfigChangeCounter_Type()
)
ltp8xConfigChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltp8xConfigChangeCounter.setStatus("current")
_Ltp8xRereadConfig_Type = Unsigned32
_Ltp8xRereadConfig_Object = MibScalar
ltp8xRereadConfig = _Ltp8xRereadConfig_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 49),
    _Ltp8xRereadConfig_Type()
)
ltp8xRereadConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xRereadConfig.setStatus("current")
_Ltp8xSaveConfig_Type = Unsigned32
_Ltp8xSaveConfig_Object = MibScalar
ltp8xSaveConfig = _Ltp8xSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 50),
    _Ltp8xSaveConfig_Type()
)
ltp8xSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xSaveConfig.setStatus("current")
_Ltp8xRebootTimeout_Type = Unsigned32
_Ltp8xRebootTimeout_Object = MibScalar
ltp8xRebootTimeout = _Ltp8xRebootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 51),
    _Ltp8xRebootTimeout_Type()
)
ltp8xRebootTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltp8xRebootTimeout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-LTP8X-STANDALONE",
    **{"ltp8xStandalone": ltp8xStandalone,
       "ltp8xSystem": ltp8xSystem,
       "ltp8xHostName": ltp8xHostName,
       "ltp8xIPAddress": ltp8xIPAddress,
       "ltp8xNetMask": ltp8xNetMask,
       "ltp8xGateway": ltp8xGateway,
       "ltp8xVLAN": ltp8xVLAN,
       "ltp8xFirmwareRevision": ltp8xFirmwareRevision,
       "ltp8xSystemUptime": ltp8xSystemUptime,
       "ltp8xSystemHardwareRevision": ltp8xSystemHardwareRevision,
       "ltp8xSystemMacAddress": ltp8xSystemMacAddress,
       "ltp8xSystemDeviceName": ltp8xSystemDeviceName,
       "ltp8xServicesControlTable": ltp8xServicesControlTable,
       "ltp8xServicesControlEntry": ltp8xServicesControlEntry,
       "ltp8xServicesControlIndex": ltp8xServicesControlIndex,
       "ltp8xServicesControlName": ltp8xServicesControlName,
       "ltp8xServicesControlEnabled": ltp8xServicesControlEnabled,
       "ltp8xBoardStatus": ltp8xBoardStatus,
       "ltp8xDiskFreeSpace": ltp8xDiskFreeSpace,
       "ltp8xRAMFree": ltp8xRAMFree,
       "ltp8xCPULoadAverage1Minute": ltp8xCPULoadAverage1Minute,
       "ltp8xCPULoadAverage5Minutes": ltp8xCPULoadAverage5Minutes,
       "ltp8xCPULoadAverage15Minutes": ltp8xCPULoadAverage15Minutes,
       "ltp8xFan0Active": ltp8xFan0Active,
       "ltp8xFan0RPM": ltp8xFan0RPM,
       "ltp8xFan1Active": ltp8xFan1Active,
       "ltp8xFan1RPM": ltp8xFan1RPM,
       "ltp8xSensor1Temperature": ltp8xSensor1Temperature,
       "ltp8xSensor2Temperature": ltp8xSensor2Temperature,
       "ltp8xSensor1TemperatureExt": ltp8xSensor1TemperatureExt,
       "ltp8xSensor2TemperatureExt": ltp8xSensor2TemperatureExt,
       "ltp8xFanMinRPM": ltp8xFanMinRPM,
       "ltp8xFanMaxRPM": ltp8xFanMaxRPM,
       "ltp8xUsers": ltp8xUsers,
       "ltp8xUsersTable": ltp8xUsersTable,
       "ltp8xUsersEntry": ltp8xUsersEntry,
       "ltp8xUsersName": ltp8xUsersName,
       "ltp8xUsersGroups": ltp8xUsersGroups,
       "ltp8xUsersOldPassword": ltp8xUsersOldPassword,
       "ltp8xUsersNewPassword": ltp8xUsersNewPassword,
       "ltp8xUsersRowStatus": ltp8xUsersRowStatus,
       "ltp8xUsersPriority": ltp8xUsersPriority,
       "ltp8xUsersGroupsTable": ltp8xUsersGroupsTable,
       "ltp8xUsersGroupsEntry": ltp8xUsersGroupsEntry,
       "ltp8xUsersGroupsID": ltp8xUsersGroupsID,
       "ltp8xUsersGroupsName": ltp8xUsersGroupsName,
       "ltp8xPrivilegesNamesTable": ltp8xPrivilegesNamesTable,
       "ltp8xPrivilegesNamesEntry": ltp8xPrivilegesNamesEntry,
       "ltp8xPrivilegesNamesIndex": ltp8xPrivilegesNamesIndex,
       "ltp8xPrivilegesNamesName": ltp8xPrivilegesNamesName,
       "ltp8xPrivilegesLevelsTable": ltp8xPrivilegesLevelsTable,
       "ltp8xPrivilegesLevelsEntry": ltp8xPrivilegesLevelsEntry,
       "ltp8xPrivilegesLevelsLevel": ltp8xPrivilegesLevelsLevel,
       "ltp8xPrivilegesLevelsAllowed": ltp8xPrivilegesLevelsAllowed,
       "ltp8xLogSubmodulesTable": ltp8xLogSubmodulesTable,
       "ltp8xLogSubmodulesEntry": ltp8xLogSubmodulesEntry,
       "ltp8xLogSubmodulesID": ltp8xLogSubmodulesID,
       "ltp8xLogSubmodulesName": ltp8xLogSubmodulesName,
       "ltp8xLogSubmodulesLevel": ltp8xLogSubmodulesLevel,
       "ltp8xLogSubmodulesDestination": ltp8xLogSubmodulesDestination,
       "ltp8xLogSubmodulesShowProgName": ltp8xLogSubmodulesShowProgName,
       "ltp8xLogSubmodulesShowSubmoduleName": ltp8xLogSubmodulesShowSubmoduleName,
       "ltp8xLogSubmodulesShowLevel": ltp8xLogSubmodulesShowLevel,
       "ltp8xLogSubmodulesShowTime": ltp8xLogSubmodulesShowTime,
       "ltp8xActivationAuthModeTable": ltp8xActivationAuthModeTable,
       "ltp8xActivationAuthModeEntry": ltp8xActivationAuthModeEntry,
       "ltp8xActivationAuthModeChannel": ltp8xActivationAuthModeChannel,
       "ltp8xActivationAuthModeHostControlledLumpedSN": ltp8xActivationAuthModeHostControlledLumpedSN,
       "ltp8xLoggingDestinationsTable": ltp8xLoggingDestinationsTable,
       "ltp8xLoggingDestinationsEntry": ltp8xLoggingDestinationsEntry,
       "ltp8xLoggingDestinationsId": ltp8xLoggingDestinationsId,
       "ltp8xLoggingDestinationsName": ltp8xLoggingDestinationsName,
       "ltp8xLoggingDestinationsLevel": ltp8xLoggingDestinationsLevel,
       "ltp8xInterfaceStatusTable": ltp8xInterfaceStatusTable,
       "ltp8xInterfaceStatusEntry": ltp8xInterfaceStatusEntry,
       "ltp8xInterfaceStatusError": ltp8xInterfaceStatusError,
       "ltp8xInterfaceStatusDuplex": ltp8xInterfaceStatusDuplex,
       "ltp8xInterfaceStatusFlowControlEnabled": ltp8xInterfaceStatusFlowControlEnabled,
       "ltp8xFanControl": ltp8xFanControl,
       "ltp8xFanSpeed": ltp8xFanSpeed,
       "ltp8xFanMinSpeed": ltp8xFanMinSpeed,
       "ltp8xPowerSupplyTable": ltp8xPowerSupplyTable,
       "ltp8xPowerSupplyEntry": ltp8xPowerSupplyEntry,
       "ltp8xPowerSupplyModuleId": ltp8xPowerSupplyModuleId,
       "ltp8xPowerSupplyModulePresent": ltp8xPowerSupplyModulePresent,
       "ltp8xPowerSupplyModuleName": ltp8xPowerSupplyModuleName,
       "ltp8xPowerSupplyModuleType": ltp8xPowerSupplyModuleType,
       "ltp8xPowerSupplyModuleIntact": ltp8xPowerSupplyModuleIntact,
       "ltp8xLicense": ltp8xLicense,
       "ltp8xLicenseInstalled": ltp8xLicenseInstalled,
       "ltp8xLicenseValid": ltp8xLicenseValid,
       "ltp8xLicenseVersion": ltp8xLicenseVersion,
       "ltp8xLicenseBoardSN": ltp8xLicenseBoardSN,
       "ltp8xLicenseVendor": ltp8xLicenseVendor,
       "ltp8xLicenseONTCount": ltp8xLicenseONTCount,
       "ltp8xLicenseActiveONTCount": ltp8xLicenseActiveONTCount,
       "ltp8xLogSize": ltp8xLogSize,
       "ltp8xExternalFirmwareIP": ltp8xExternalFirmwareIP,
       "ltp8xExternalFirmwarePort": ltp8xExternalFirmwarePort,
       "ltp8xNTPDaylightSaving": ltp8xNTPDaylightSaving,
       "ltp8xONTFwAutoUpdateEnabled": ltp8xONTFwAutoUpdateEnabled,
       "ltp8xConfigChangeCounter": ltp8xConfigChangeCounter,
       "ltp8xRereadConfig": ltp8xRereadConfig,
       "ltp8xSaveConfig": ltp8xSaveConfig,
       "ltp8xRebootTimeout": ltp8xRebootTimeout}
)
