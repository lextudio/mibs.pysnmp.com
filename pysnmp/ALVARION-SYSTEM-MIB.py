# SNMP MIB module (ALVARION-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:39 2024
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

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

(AlvarionAuthenticationMode,
 AlvarionNotificationEnable,
 AlvarionProfileIndexOrZero) = mibBuilder.importSymbols(
    "ALVARION-TC",
    "AlvarionAuthenticationMode",
    "AlvarionNotificationEnable",
    "AlvarionProfileIndexOrZero")

(ifInErrors,
 ifInUcastPkts,
 ifOutErrors,
 ifOutUcastPkts) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifInErrors",
    "ifInUcastPkts",
    "ifOutErrors",
    "ifOutUcastPkts")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alvarionSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionSystemMIBObjects_ObjectIdentity = ObjectIdentity
alvarionSystemMIBObjects = _AlvarionSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1)
)
_SystemInfo_ObjectIdentity = ObjectIdentity
systemInfo = _SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1)
)
_SystemProductName_Type = DisplayString
_SystemProductName_Object = MibScalar
systemProductName = _SystemProductName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1, 1),
    _SystemProductName_Type()
)
systemProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProductName.setStatus("current")
_SystemFirmwareRevision_Type = DisplayString
_SystemFirmwareRevision_Object = MibScalar
systemFirmwareRevision = _SystemFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1, 2),
    _SystemFirmwareRevision_Type()
)
systemFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFirmwareRevision.setStatus("current")
_SystemBootRevision_Type = DisplayString
_SystemBootRevision_Object = MibScalar
systemBootRevision = _SystemBootRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1, 3),
    _SystemBootRevision_Type()
)
systemBootRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBootRevision.setStatus("current")
_SystemHardwareRevision_Type = DisplayString
_SystemHardwareRevision_Object = MibScalar
systemHardwareRevision = _SystemHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1, 4),
    _SystemHardwareRevision_Type()
)
systemHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHardwareRevision.setStatus("current")
_SystemSerialNumber_Type = DisplayString
_SystemSerialNumber_Object = MibScalar
systemSerialNumber = _SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1, 5),
    _SystemSerialNumber_Type()
)
systemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSerialNumber.setStatus("current")
_SystemConfigurationVersion_Type = DisplayString
_SystemConfigurationVersion_Object = MibScalar
systemConfigurationVersion = _SystemConfigurationVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1, 6),
    _SystemConfigurationVersion_Type()
)
systemConfigurationVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigurationVersion.setStatus("current")
_SystemUpTime_Type = Counter32
_SystemUpTime_Object = MibScalar
systemUpTime = _SystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1, 7),
    _SystemUpTime_Type()
)
systemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTime.setStatus("current")
if mibBuilder.loadTexts:
    systemUpTime.setUnits("seconds")
_SystemMacAddress_Type = MacAddress
_SystemMacAddress_Object = MibScalar
systemMacAddress = _SystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1, 8),
    _SystemMacAddress_Type()
)
systemMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemMacAddress.setStatus("current")
_SystemWanPortIpAddress_Type = IpAddress
_SystemWanPortIpAddress_Object = MibScalar
systemWanPortIpAddress = _SystemWanPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1, 9),
    _SystemWanPortIpAddress_Type()
)
systemWanPortIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemWanPortIpAddress.setStatus("current")
_SystemProductFlavor_Type = DisplayString
_SystemProductFlavor_Object = MibScalar
systemProductFlavor = _SystemProductFlavor_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1, 10),
    _SystemProductFlavor_Type()
)
systemProductFlavor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProductFlavor.setStatus("current")
_SystemDeviceIdentification_Type = MacAddress
_SystemDeviceIdentification_Object = MibScalar
systemDeviceIdentification = _SystemDeviceIdentification_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 1, 11),
    _SystemDeviceIdentification_Type()
)
systemDeviceIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDeviceIdentification.setStatus("current")
_SystemTime_ObjectIdentity = ObjectIdentity
systemTime = _SystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2)
)


class _SystemTimeUpdateMode_Type(Integer32):
    """Custom type systemTimeUpdateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("sntpUdp", 2),
          ("tp", 3))
    )


_SystemTimeUpdateMode_Type.__name__ = "Integer32"
_SystemTimeUpdateMode_Object = MibScalar
systemTimeUpdateMode = _SystemTimeUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2, 1),
    _SystemTimeUpdateMode_Type()
)
systemTimeUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTimeUpdateMode.setStatus("current")
_SystemTimeLostWhenRebooting_Type = TruthValue
_SystemTimeLostWhenRebooting_Object = MibScalar
systemTimeLostWhenRebooting = _SystemTimeLostWhenRebooting_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2, 2),
    _SystemTimeLostWhenRebooting_Type()
)
systemTimeLostWhenRebooting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTimeLostWhenRebooting.setStatus("current")
_SystemTimeDSTOn_Type = TruthValue
_SystemTimeDSTOn_Object = MibScalar
systemTimeDSTOn = _SystemTimeDSTOn_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2, 3),
    _SystemTimeDSTOn_Type()
)
systemTimeDSTOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTimeDSTOn.setStatus("current")


class _SystemDate_Type(OctetString):
    """Custom type systemDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_SystemDate_Type.__name__ = "OctetString"
_SystemDate_Object = MibScalar
systemDate = _SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2, 4),
    _SystemDate_Type()
)
systemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDate.setStatus("current")


class _SystemTimeOfDay_Type(OctetString):
    """Custom type systemTimeOfDay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SystemTimeOfDay_Type.__name__ = "OctetString"
_SystemTimeOfDay_Object = MibScalar
systemTimeOfDay = _SystemTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2, 5),
    _SystemTimeOfDay_Type()
)
systemTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTimeOfDay.setStatus("current")


class _SystemTimeZone_Type(OctetString):
    """Custom type systemTimeZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SystemTimeZone_Type.__name__ = "OctetString"
_SystemTimeZone_Object = MibScalar
systemTimeZone = _SystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2, 6),
    _SystemTimeZone_Type()
)
systemTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTimeZone.setStatus("current")
_SystemTimeServerTable_Object = MibTable
systemTimeServerTable = _SystemTimeServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2, 7)
)
if mibBuilder.loadTexts:
    systemTimeServerTable.setStatus("current")
_SystemTimeServerEntry_Object = MibTableRow
systemTimeServerEntry = _SystemTimeServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2, 7, 1)
)
systemTimeServerEntry.setIndexNames(
    (0, "ALVARION-SYSTEM-MIB", "systemTimeServerIndex"),
)
if mibBuilder.loadTexts:
    systemTimeServerEntry.setStatus("current")


class _SystemTimeServerIndex_Type(Integer32):
    """Custom type systemTimeServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SystemTimeServerIndex_Type.__name__ = "Integer32"
_SystemTimeServerIndex_Object = MibTableColumn
systemTimeServerIndex = _SystemTimeServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2, 7, 1, 1),
    _SystemTimeServerIndex_Type()
)
systemTimeServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemTimeServerIndex.setStatus("current")
_SystemTimeServerAddress_Type = DisplayString
_SystemTimeServerAddress_Object = MibTableColumn
systemTimeServerAddress = _SystemTimeServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2, 7, 1, 2),
    _SystemTimeServerAddress_Type()
)
systemTimeServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTimeServerAddress.setStatus("current")
_SystemTimeServerNotificationEnabled_Type = AlvarionNotificationEnable
_SystemTimeServerNotificationEnabled_Object = MibScalar
systemTimeServerNotificationEnabled = _SystemTimeServerNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 2, 8),
    _SystemTimeServerNotificationEnabled_Type()
)
systemTimeServerNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTimeServerNotificationEnabled.setStatus("current")
_AdminAccess_ObjectIdentity = ObjectIdentity
adminAccess = _AdminAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3)
)
_AdminAccessAuthenMode_Type = AlvarionAuthenticationMode
_AdminAccessAuthenMode_Object = MibScalar
adminAccessAuthenMode = _AdminAccessAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 1),
    _AdminAccessAuthenMode_Type()
)
adminAccessAuthenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAccessAuthenMode.setStatus("current")
_AdminAccessAuthenProfileIndex_Type = AlvarionProfileIndexOrZero
_AdminAccessAuthenProfileIndex_Object = MibScalar
adminAccessAuthenProfileIndex = _AdminAccessAuthenProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 2),
    _AdminAccessAuthenProfileIndex_Type()
)
adminAccessAuthenProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAccessAuthenProfileIndex.setStatus("current")


class _AdminAccessMaxLoginAttempts_Type(Integer32):
    """Custom type adminAccessMaxLoginAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AdminAccessMaxLoginAttempts_Type.__name__ = "Integer32"
_AdminAccessMaxLoginAttempts_Object = MibScalar
adminAccessMaxLoginAttempts = _AdminAccessMaxLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 3),
    _AdminAccessMaxLoginAttempts_Type()
)
adminAccessMaxLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAccessMaxLoginAttempts.setStatus("current")


class _AdminAccessLockOutPeriod_Type(Integer32):
    """Custom type adminAccessLockOutPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AdminAccessLockOutPeriod_Type.__name__ = "Integer32"
_AdminAccessLockOutPeriod_Object = MibScalar
adminAccessLockOutPeriod = _AdminAccessLockOutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 4),
    _AdminAccessLockOutPeriod_Type()
)
adminAccessLockOutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAccessLockOutPeriod.setStatus("current")
if mibBuilder.loadTexts:
    adminAccessLockOutPeriod.setUnits("minutes")


class _AdminAccessLoginNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type adminAccessLoginNotificationEnabled based on AlvarionNotificationEnable"""


_AdminAccessLoginNotificationEnabled_Object = MibScalar
adminAccessLoginNotificationEnabled = _AdminAccessLoginNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 5),
    _AdminAccessLoginNotificationEnabled_Type()
)
adminAccessLoginNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAccessLoginNotificationEnabled.setStatus("current")


class _AdminAccessAuthFailureNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type adminAccessAuthFailureNotificationEnabled based on AlvarionNotificationEnable"""


_AdminAccessAuthFailureNotificationEnabled_Object = MibScalar
adminAccessAuthFailureNotificationEnabled = _AdminAccessAuthFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 6),
    _AdminAccessAuthFailureNotificationEnabled_Type()
)
adminAccessAuthFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAccessAuthFailureNotificationEnabled.setStatus("current")
_AdminAccessInfo_Type = DisplayString
_AdminAccessInfo_Object = MibScalar
adminAccessInfo = _AdminAccessInfo_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 7),
    _AdminAccessInfo_Type()
)
adminAccessInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adminAccessInfo.setStatus("current")
_AdminAccessProfileTable_Object = MibTable
adminAccessProfileTable = _AdminAccessProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 8)
)
if mibBuilder.loadTexts:
    adminAccessProfileTable.setStatus("current")
_AdminAccessProfileEntry_Object = MibTableRow
adminAccessProfileEntry = _AdminAccessProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 8, 1)
)
adminAccessProfileEntry.setIndexNames(
    (0, "ALVARION-SYSTEM-MIB", "adminAccessProfileIndex"),
)
if mibBuilder.loadTexts:
    adminAccessProfileEntry.setStatus("current")


class _AdminAccessProfileIndex_Type(Integer32):
    """Custom type adminAccessProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdminAccessProfileIndex_Type.__name__ = "Integer32"
_AdminAccessProfileIndex_Object = MibTableColumn
adminAccessProfileIndex = _AdminAccessProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 8, 1, 1),
    _AdminAccessProfileIndex_Type()
)
adminAccessProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminAccessProfileIndex.setStatus("current")


class _AdminAccessUserName_Type(OctetString):
    """Custom type adminAccessUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_AdminAccessUserName_Type.__name__ = "OctetString"
_AdminAccessUserName_Object = MibTableColumn
adminAccessUserName = _AdminAccessUserName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 8, 1, 2),
    _AdminAccessUserName_Type()
)
adminAccessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminAccessUserName.setStatus("current")


class _AdminAccessAdministrativeRights_Type(Integer32):
    """Custom type adminAccessAdministrativeRights based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_AdminAccessAdministrativeRights_Type.__name__ = "Integer32"
_AdminAccessAdministrativeRights_Object = MibTableColumn
adminAccessAdministrativeRights = _AdminAccessAdministrativeRights_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 8, 1, 3),
    _AdminAccessAdministrativeRights_Type()
)
adminAccessAdministrativeRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminAccessAdministrativeRights.setStatus("current")


class _AdminAccessLogoutNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type adminAccessLogoutNotificationEnabled based on AlvarionNotificationEnable"""


_AdminAccessLogoutNotificationEnabled_Object = MibScalar
adminAccessLogoutNotificationEnabled = _AdminAccessLogoutNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 3, 9),
    _AdminAccessLogoutNotificationEnabled_Type()
)
adminAccessLogoutNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAccessLogoutNotificationEnabled.setStatus("current")
_Heartbeat_ObjectIdentity = ObjectIdentity
heartbeat = _Heartbeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 4)
)


class _HeartbeatPeriod_Type(Integer32):
    """Custom type heartbeatPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 31536000),
    )


_HeartbeatPeriod_Type.__name__ = "Integer32"
_HeartbeatPeriod_Object = MibScalar
heartbeatPeriod = _HeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 4, 1),
    _HeartbeatPeriod_Type()
)
heartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heartbeatPeriod.setStatus("current")
if mibBuilder.loadTexts:
    heartbeatPeriod.setUnits("seconds")


class _HeartbeatNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type heartbeatNotificationEnabled based on AlvarionNotificationEnable"""


_HeartbeatNotificationEnabled_Object = MibScalar
heartbeatNotificationEnabled = _HeartbeatNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 1, 4, 2),
    _HeartbeatNotificationEnabled_Type()
)
heartbeatNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heartbeatNotificationEnabled.setStatus("current")
_AlvarionSystemMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
alvarionSystemMIBNotificationPrefix = _AlvarionSystemMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 2)
)
_AlvarionSystemMIBNotifications_ObjectIdentity = ObjectIdentity
alvarionSystemMIBNotifications = _AlvarionSystemMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 2, 0)
)
_AlvarionSystemMIBConformance_ObjectIdentity = ObjectIdentity
alvarionSystemMIBConformance = _AlvarionSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 3)
)
_AlvarionSystemMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionSystemMIBCompliances = _AlvarionSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 3, 1)
)
_AlvarionSystemMIBGroups_ObjectIdentity = ObjectIdentity
alvarionSystemMIBGroups = _AlvarionSystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 3, 2)
)

# Managed Objects groups

alvarionSystemMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 3, 2, 1)
)
alvarionSystemMIBGroup.setObjects(
      *(("ALVARION-SYSTEM-MIB", "systemProductName"),
        ("ALVARION-SYSTEM-MIB", "systemFirmwareRevision"),
        ("ALVARION-SYSTEM-MIB", "systemBootRevision"),
        ("ALVARION-SYSTEM-MIB", "systemHardwareRevision"),
        ("ALVARION-SYSTEM-MIB", "systemSerialNumber"),
        ("ALVARION-SYSTEM-MIB", "systemConfigurationVersion"),
        ("ALVARION-SYSTEM-MIB", "systemUpTime"),
        ("ALVARION-SYSTEM-MIB", "systemMacAddress"),
        ("ALVARION-SYSTEM-MIB", "systemWanPortIpAddress"),
        ("ALVARION-SYSTEM-MIB", "systemProductFlavor"),
        ("ALVARION-SYSTEM-MIB", "systemDeviceIdentification"),
        ("ALVARION-SYSTEM-MIB", "systemTimeUpdateMode"),
        ("ALVARION-SYSTEM-MIB", "systemTimeLostWhenRebooting"),
        ("ALVARION-SYSTEM-MIB", "systemTimeDSTOn"),
        ("ALVARION-SYSTEM-MIB", "systemDate"),
        ("ALVARION-SYSTEM-MIB", "systemTimeOfDay"),
        ("ALVARION-SYSTEM-MIB", "systemTimeZone"),
        ("ALVARION-SYSTEM-MIB", "systemTimeServerAddress"),
        ("ALVARION-SYSTEM-MIB", "systemTimeServerNotificationEnabled"),
        ("ALVARION-SYSTEM-MIB", "heartbeatPeriod"),
        ("ALVARION-SYSTEM-MIB", "heartbeatNotificationEnabled"))
)
if mibBuilder.loadTexts:
    alvarionSystemMIBGroup.setStatus("current")

alvarionAdminAccessProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 3, 2, 2)
)
alvarionAdminAccessProfileGroup.setObjects(
      *(("ALVARION-SYSTEM-MIB", "adminAccessAuthenMode"),
        ("ALVARION-SYSTEM-MIB", "adminAccessMaxLoginAttempts"),
        ("ALVARION-SYSTEM-MIB", "adminAccessLockOutPeriod"),
        ("ALVARION-SYSTEM-MIB", "adminAccessLoginNotificationEnabled"),
        ("ALVARION-SYSTEM-MIB", "adminAccessAuthFailureNotificationEnabled"),
        ("ALVARION-SYSTEM-MIB", "adminAccessAuthenProfileIndex"),
        ("ALVARION-SYSTEM-MIB", "adminAccessInfo"),
        ("ALVARION-SYSTEM-MIB", "adminAccessUserName"),
        ("ALVARION-SYSTEM-MIB", "adminAccessAdministrativeRights"),
        ("ALVARION-SYSTEM-MIB", "adminAccessLogoutNotificationEnabled"))
)
if mibBuilder.loadTexts:
    alvarionAdminAccessProfileGroup.setStatus("current")


# Notification objects

adminAccessAuthFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 2, 0, 1)
)
adminAccessAuthFailureNotification.setObjects(
    ("ALVARION-SYSTEM-MIB", "adminAccessInfo")
)
if mibBuilder.loadTexts:
    adminAccessAuthFailureNotification.setStatus(
        "current"
    )

adminAccessLoginNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 2, 0, 2)
)
if mibBuilder.loadTexts:
    adminAccessLoginNotification.setStatus(
        "current"
    )

systemColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 2, 0, 3)
)
systemColdStart.setObjects(
      *(("ALVARION-SYSTEM-MIB", "systemProductName"),
        ("ALVARION-SYSTEM-MIB", "systemFirmwareRevision"),
        ("ALVARION-SYSTEM-MIB", "systemConfigurationVersion"),
        ("ALVARION-SYSTEM-MIB", "systemSerialNumber"))
)
if mibBuilder.loadTexts:
    systemColdStart.setStatus(
        "current"
    )

systemHeartbeatNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 2, 0, 4)
)
systemHeartbeatNotification.setObjects(
      *(("ALVARION-SYSTEM-MIB", "systemSerialNumber"),
        ("ALVARION-SYSTEM-MIB", "systemMacAddress"),
        ("ALVARION-SYSTEM-MIB", "systemWanPortIpAddress"),
        ("ALVARION-SYSTEM-MIB", "systemUpTime"),
        ("IF-MIB", "ifOutUcastPkts"),
        ("IF-MIB", "ifInUcastPkts"),
        ("IF-MIB", "ifOutErrors"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutUcastPkts"),
        ("IF-MIB", "ifInUcastPkts"),
        ("IF-MIB", "ifOutErrors"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutUcastPkts"),
        ("IF-MIB", "ifInUcastPkts"),
        ("IF-MIB", "ifOutErrors"),
        ("IF-MIB", "ifInErrors"))
)
if mibBuilder.loadTexts:
    systemHeartbeatNotification.setStatus(
        "current"
    )

adminAccessLogoutNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 2, 0, 5)
)
adminAccessLogoutNotification.setObjects(
    ("ALVARION-SYSTEM-MIB", "adminAccessInfo")
)
if mibBuilder.loadTexts:
    adminAccessLogoutNotification.setStatus(
        "current"
    )

timeServerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 2, 0, 6)
)
timeServerFailure.setObjects(
    ("ALVARION-SYSTEM-MIB", "systemTimeServerAddress")
)
if mibBuilder.loadTexts:
    timeServerFailure.setStatus(
        "current"
    )


# Notifications groups

alvarionSystemNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 3, 2, 3)
)
alvarionSystemNotificationGroup.setObjects(
      *(("ALVARION-SYSTEM-MIB", "systemColdStart"),
        ("ALVARION-SYSTEM-MIB", "systemHeartbeatNotification"))
)
if mibBuilder.loadTexts:
    alvarionSystemNotificationGroup.setStatus(
        "current"
    )

alvarionAdminAccessNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 3, 2, 4)
)
alvarionAdminAccessNotificationGroup.setObjects(
      *(("ALVARION-SYSTEM-MIB", "adminAccessAuthFailureNotification"),
        ("ALVARION-SYSTEM-MIB", "adminAccessLoginNotification"),
        ("ALVARION-SYSTEM-MIB", "adminAccessLogoutNotification"))
)
if mibBuilder.loadTexts:
    alvarionAdminAccessNotificationGroup.setStatus(
        "current"
    )

alvarionTimeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 3, 2, 5)
)
alvarionTimeNotificationGroup.setObjects(
    ("ALVARION-SYSTEM-MIB", "timeServerFailure")
)
if mibBuilder.loadTexts:
    alvarionTimeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alvarionSystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionSystemMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-SYSTEM-MIB",
    **{"alvarionSystemMIB": alvarionSystemMIB,
       "alvarionSystemMIBObjects": alvarionSystemMIBObjects,
       "systemInfo": systemInfo,
       "systemProductName": systemProductName,
       "systemFirmwareRevision": systemFirmwareRevision,
       "systemBootRevision": systemBootRevision,
       "systemHardwareRevision": systemHardwareRevision,
       "systemSerialNumber": systemSerialNumber,
       "systemConfigurationVersion": systemConfigurationVersion,
       "systemUpTime": systemUpTime,
       "systemMacAddress": systemMacAddress,
       "systemWanPortIpAddress": systemWanPortIpAddress,
       "systemProductFlavor": systemProductFlavor,
       "systemDeviceIdentification": systemDeviceIdentification,
       "systemTime": systemTime,
       "systemTimeUpdateMode": systemTimeUpdateMode,
       "systemTimeLostWhenRebooting": systemTimeLostWhenRebooting,
       "systemTimeDSTOn": systemTimeDSTOn,
       "systemDate": systemDate,
       "systemTimeOfDay": systemTimeOfDay,
       "systemTimeZone": systemTimeZone,
       "systemTimeServerTable": systemTimeServerTable,
       "systemTimeServerEntry": systemTimeServerEntry,
       "systemTimeServerIndex": systemTimeServerIndex,
       "systemTimeServerAddress": systemTimeServerAddress,
       "systemTimeServerNotificationEnabled": systemTimeServerNotificationEnabled,
       "adminAccess": adminAccess,
       "adminAccessAuthenMode": adminAccessAuthenMode,
       "adminAccessAuthenProfileIndex": adminAccessAuthenProfileIndex,
       "adminAccessMaxLoginAttempts": adminAccessMaxLoginAttempts,
       "adminAccessLockOutPeriod": adminAccessLockOutPeriod,
       "adminAccessLoginNotificationEnabled": adminAccessLoginNotificationEnabled,
       "adminAccessAuthFailureNotificationEnabled": adminAccessAuthFailureNotificationEnabled,
       "adminAccessInfo": adminAccessInfo,
       "adminAccessProfileTable": adminAccessProfileTable,
       "adminAccessProfileEntry": adminAccessProfileEntry,
       "adminAccessProfileIndex": adminAccessProfileIndex,
       "adminAccessUserName": adminAccessUserName,
       "adminAccessAdministrativeRights": adminAccessAdministrativeRights,
       "adminAccessLogoutNotificationEnabled": adminAccessLogoutNotificationEnabled,
       "heartbeat": heartbeat,
       "heartbeatPeriod": heartbeatPeriod,
       "heartbeatNotificationEnabled": heartbeatNotificationEnabled,
       "alvarionSystemMIBNotificationPrefix": alvarionSystemMIBNotificationPrefix,
       "alvarionSystemMIBNotifications": alvarionSystemMIBNotifications,
       "adminAccessAuthFailureNotification": adminAccessAuthFailureNotification,
       "adminAccessLoginNotification": adminAccessLoginNotification,
       "systemColdStart": systemColdStart,
       "systemHeartbeatNotification": systemHeartbeatNotification,
       "adminAccessLogoutNotification": adminAccessLogoutNotification,
       "timeServerFailure": timeServerFailure,
       "alvarionSystemMIBConformance": alvarionSystemMIBConformance,
       "alvarionSystemMIBCompliances": alvarionSystemMIBCompliances,
       "alvarionSystemMIBCompliance": alvarionSystemMIBCompliance,
       "alvarionSystemMIBGroups": alvarionSystemMIBGroups,
       "alvarionSystemMIBGroup": alvarionSystemMIBGroup,
       "alvarionAdminAccessProfileGroup": alvarionAdminAccessProfileGroup,
       "alvarionSystemNotificationGroup": alvarionSystemNotificationGroup,
       "alvarionAdminAccessNotificationGroup": alvarionAdminAccessNotificationGroup,
       "alvarionTimeNotificationGroup": alvarionTimeNotificationGroup}
)
