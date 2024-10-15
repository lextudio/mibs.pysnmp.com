# SNMP MIB module (PRIVATE-FEL2Mod-SW24-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PRIVATE-FEL2Mod-SW24-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:43 2024
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

privatetech = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5205)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2)
)
_FeL2ModSW24ProductID_ObjectIdentity = ObjectIdentity
feL2ModSW24ProductID = _FeL2ModSW24ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19)
)
_FeL2ModSW24Produces_ObjectIdentity = ObjectIdentity
feL2ModSW24Produces = _FeL2ModSW24Produces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1)
)
_FeL2ModSW24System_ObjectIdentity = ObjectIdentity
feL2ModSW24System = _FeL2ModSW24System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1)
)
_FeL2ModSW24CommonSys_ObjectIdentity = ObjectIdentity
feL2ModSW24CommonSys = _FeL2ModSW24CommonSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 1)
)


class _FeL2ModSW24Reboot_Type(Integer32):
    """Custom type feL2ModSW24Reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_FeL2ModSW24Reboot_Type.__name__ = "Integer32"
_FeL2ModSW24Reboot_Object = MibScalar
feL2ModSW24Reboot = _FeL2ModSW24Reboot_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 1, 1),
    _FeL2ModSW24Reboot_Type()
)
feL2ModSW24Reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24Reboot.setStatus("current")
_FeL2ModSW24BiosVsersion_Type = DisplayString
_FeL2ModSW24BiosVsersion_Object = MibScalar
feL2ModSW24BiosVsersion = _FeL2ModSW24BiosVsersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 1, 2),
    _FeL2ModSW24BiosVsersion_Type()
)
feL2ModSW24BiosVsersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24BiosVsersion.setStatus("current")
_FeL2ModSW24FirmwareVersion_Type = DisplayString
_FeL2ModSW24FirmwareVersion_Object = MibScalar
feL2ModSW24FirmwareVersion = _FeL2ModSW24FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 1, 3),
    _FeL2ModSW24FirmwareVersion_Type()
)
feL2ModSW24FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24FirmwareVersion.setStatus("current")
_FeL2ModSW24HardwareVersion_Type = DisplayString
_FeL2ModSW24HardwareVersion_Object = MibScalar
feL2ModSW24HardwareVersion = _FeL2ModSW24HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 1, 4),
    _FeL2ModSW24HardwareVersion_Type()
)
feL2ModSW24HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24HardwareVersion.setStatus("current")
_FeL2ModSW24MechanicalVersion_Type = DisplayString
_FeL2ModSW24MechanicalVersion_Object = MibScalar
feL2ModSW24MechanicalVersion = _FeL2ModSW24MechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 1, 5),
    _FeL2ModSW24MechanicalVersion_Type()
)
feL2ModSW24MechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24MechanicalVersion.setStatus("current")
_FeL2ModSW24SerialNumber_Type = DisplayString
_FeL2ModSW24SerialNumber_Object = MibScalar
feL2ModSW24SerialNumber = _FeL2ModSW24SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 1, 6),
    _FeL2ModSW24SerialNumber_Type()
)
feL2ModSW24SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SerialNumber.setStatus("current")
_FeL2ModSW24HostMacAddress_Type = DisplayString
_FeL2ModSW24HostMacAddress_Object = MibScalar
feL2ModSW24HostMacAddress = _FeL2ModSW24HostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 1, 7),
    _FeL2ModSW24HostMacAddress_Type()
)
feL2ModSW24HostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24HostMacAddress.setStatus("current")
_FeL2ModSW24DevicePort_Type = DisplayString
_FeL2ModSW24DevicePort_Object = MibScalar
feL2ModSW24DevicePort = _FeL2ModSW24DevicePort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 1, 8),
    _FeL2ModSW24DevicePort_Type()
)
feL2ModSW24DevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24DevicePort.setStatus("current")
_FeL2ModSW24RamSize_Type = DisplayString
_FeL2ModSW24RamSize_Object = MibScalar
feL2ModSW24RamSize = _FeL2ModSW24RamSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 1, 9),
    _FeL2ModSW24RamSize_Type()
)
feL2ModSW24RamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24RamSize.setStatus("current")
_FeL2ModSW24FlashSize_Type = DisplayString
_FeL2ModSW24FlashSize_Object = MibScalar
feL2ModSW24FlashSize = _FeL2ModSW24FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 1, 10),
    _FeL2ModSW24FlashSize_Type()
)
feL2ModSW24FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24FlashSize.setStatus("current")
_FeL2ModSW24IP_ObjectIdentity = ObjectIdentity
feL2ModSW24IP = _FeL2ModSW24IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 2)
)


class _FeL2ModSW24DhcpSetting_Type(Integer32):
    """Custom type feL2ModSW24DhcpSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24DhcpSetting_Type.__name__ = "Integer32"
_FeL2ModSW24DhcpSetting_Object = MibScalar
feL2ModSW24DhcpSetting = _FeL2ModSW24DhcpSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 2, 1),
    _FeL2ModSW24DhcpSetting_Type()
)
feL2ModSW24DhcpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24DhcpSetting.setStatus("current")
_FeL2ModSW24IPAddress_Type = IpAddress
_FeL2ModSW24IPAddress_Object = MibScalar
feL2ModSW24IPAddress = _FeL2ModSW24IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 2, 2),
    _FeL2ModSW24IPAddress_Type()
)
feL2ModSW24IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24IPAddress.setStatus("current")
_FeL2ModSW24NetMask_Type = IpAddress
_FeL2ModSW24NetMask_Object = MibScalar
feL2ModSW24NetMask = _FeL2ModSW24NetMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 2, 3),
    _FeL2ModSW24NetMask_Type()
)
feL2ModSW24NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24NetMask.setStatus("current")
_FeL2ModSW24DefaultGateway_Type = IpAddress
_FeL2ModSW24DefaultGateway_Object = MibScalar
feL2ModSW24DefaultGateway = _FeL2ModSW24DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 2, 4),
    _FeL2ModSW24DefaultGateway_Type()
)
feL2ModSW24DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24DefaultGateway.setStatus("current")


class _FeL2ModSW24DnsSetting_Type(Integer32):
    """Custom type feL2ModSW24DnsSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24DnsSetting_Type.__name__ = "Integer32"
_FeL2ModSW24DnsSetting_Object = MibScalar
feL2ModSW24DnsSetting = _FeL2ModSW24DnsSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 2, 5),
    _FeL2ModSW24DnsSetting_Type()
)
feL2ModSW24DnsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24DnsSetting.setStatus("current")
_FeL2ModSW24DnsServer_Type = IpAddress
_FeL2ModSW24DnsServer_Object = MibScalar
feL2ModSW24DnsServer = _FeL2ModSW24DnsServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 2, 6),
    _FeL2ModSW24DnsServer_Type()
)
feL2ModSW24DnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24DnsServer.setStatus("current")
_FeL2ModSW24Time_ObjectIdentity = ObjectIdentity
feL2ModSW24Time = _FeL2ModSW24Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 3)
)
_FeL2ModSW24SystemCurrentTime_Type = DisplayString
_FeL2ModSW24SystemCurrentTime_Object = MibScalar
feL2ModSW24SystemCurrentTime = _FeL2ModSW24SystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 3, 1),
    _FeL2ModSW24SystemCurrentTime_Type()
)
feL2ModSW24SystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SystemCurrentTime.setStatus("current")
_FeL2ModSW24ManualTimeSetting_Type = DisplayString
_FeL2ModSW24ManualTimeSetting_Object = MibScalar
feL2ModSW24ManualTimeSetting = _FeL2ModSW24ManualTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 3, 2),
    _FeL2ModSW24ManualTimeSetting_Type()
)
feL2ModSW24ManualTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24ManualTimeSetting.setStatus("current")
_FeL2ModSW24NTPServer_Type = DisplayString
_FeL2ModSW24NTPServer_Object = MibScalar
feL2ModSW24NTPServer = _FeL2ModSW24NTPServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 3, 3),
    _FeL2ModSW24NTPServer_Type()
)
feL2ModSW24NTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24NTPServer.setStatus("current")


class _FeL2ModSW24NTPTimeZone_Type(Integer32):
    """Custom type feL2ModSW24NTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_FeL2ModSW24NTPTimeZone_Type.__name__ = "Integer32"
_FeL2ModSW24NTPTimeZone_Object = MibScalar
feL2ModSW24NTPTimeZone = _FeL2ModSW24NTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 3, 4),
    _FeL2ModSW24NTPTimeZone_Type()
)
feL2ModSW24NTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24NTPTimeZone.setStatus("current")


class _FeL2ModSW24NTPTimeSync_Type(Integer32):
    """Custom type feL2ModSW24NTPTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24NTPTimeSync_Type.__name__ = "Integer32"
_FeL2ModSW24NTPTimeSync_Object = MibScalar
feL2ModSW24NTPTimeSync = _FeL2ModSW24NTPTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 3, 5),
    _FeL2ModSW24NTPTimeSync_Type()
)
feL2ModSW24NTPTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24NTPTimeSync.setStatus("current")


class _FeL2ModSW24DaylightSavingTime_Type(Integer32):
    """Custom type feL2ModSW24DaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_FeL2ModSW24DaylightSavingTime_Type.__name__ = "Integer32"
_FeL2ModSW24DaylightSavingTime_Object = MibScalar
feL2ModSW24DaylightSavingTime = _FeL2ModSW24DaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 3, 6),
    _FeL2ModSW24DaylightSavingTime_Type()
)
feL2ModSW24DaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24DaylightSavingTime.setStatus("current")
_FeL2ModSW24DaylightStartTime_Type = DisplayString
_FeL2ModSW24DaylightStartTime_Object = MibScalar
feL2ModSW24DaylightStartTime = _FeL2ModSW24DaylightStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 3, 7),
    _FeL2ModSW24DaylightStartTime_Type()
)
feL2ModSW24DaylightStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24DaylightStartTime.setStatus("current")
_FeL2ModSW24DaylightEndTime_Type = DisplayString
_FeL2ModSW24DaylightEndTime_Object = MibScalar
feL2ModSW24DaylightEndTime = _FeL2ModSW24DaylightEndTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 3, 8),
    _FeL2ModSW24DaylightEndTime_Type()
)
feL2ModSW24DaylightEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24DaylightEndTime.setStatus("current")
_FeL2ModSW24Account_ObjectIdentity = ObjectIdentity
feL2ModSW24Account = _FeL2ModSW24Account_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4)
)


class _FeL2ModSW24AccountNumber_Type(Integer32):
    """Custom type feL2ModSW24AccountNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FeL2ModSW24AccountNumber_Type.__name__ = "Integer32"
_FeL2ModSW24AccountNumber_Object = MibScalar
feL2ModSW24AccountNumber = _FeL2ModSW24AccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4, 1),
    _FeL2ModSW24AccountNumber_Type()
)
feL2ModSW24AccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24AccountNumber.setStatus("current")
_FeL2ModSW24AccountTable_Object = MibTable
feL2ModSW24AccountTable = _FeL2ModSW24AccountTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    feL2ModSW24AccountTable.setStatus("current")
_FeL2ModSW24AccountEntry_Object = MibTableRow
feL2ModSW24AccountEntry = _FeL2ModSW24AccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4, 2, 1)
)
feL2ModSW24AccountEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24AccountIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24AccountEntry.setStatus("current")


class _FeL2ModSW24AccountIndex_Type(Integer32):
    """Custom type feL2ModSW24AccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FeL2ModSW24AccountIndex_Type.__name__ = "Integer32"
_FeL2ModSW24AccountIndex_Object = MibTableColumn
feL2ModSW24AccountIndex = _FeL2ModSW24AccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4, 2, 1, 1),
    _FeL2ModSW24AccountIndex_Type()
)
feL2ModSW24AccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24AccountIndex.setStatus("current")
_FeL2ModSW24AccountAuthorization_Type = DisplayString
_FeL2ModSW24AccountAuthorization_Object = MibTableColumn
feL2ModSW24AccountAuthorization = _FeL2ModSW24AccountAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4, 2, 1, 2),
    _FeL2ModSW24AccountAuthorization_Type()
)
feL2ModSW24AccountAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24AccountAuthorization.setStatus("current")
_FeL2ModSW24AccountName_Type = DisplayString
_FeL2ModSW24AccountName_Object = MibTableColumn
feL2ModSW24AccountName = _FeL2ModSW24AccountName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4, 2, 1, 3),
    _FeL2ModSW24AccountName_Type()
)
feL2ModSW24AccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24AccountName.setStatus("current")
_FeL2ModSW24AccountPassword_Type = DisplayString
_FeL2ModSW24AccountPassword_Object = MibTableColumn
feL2ModSW24AccountPassword = _FeL2ModSW24AccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4, 2, 1, 4),
    _FeL2ModSW24AccountPassword_Type()
)
feL2ModSW24AccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24AccountPassword.setStatus("current")
_FeL2ModSW24AccountAddName_Type = DisplayString
_FeL2ModSW24AccountAddName_Object = MibScalar
feL2ModSW24AccountAddName = _FeL2ModSW24AccountAddName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4, 3),
    _FeL2ModSW24AccountAddName_Type()
)
feL2ModSW24AccountAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24AccountAddName.setStatus("current")
_FeL2ModSW24AccountAddPassword_Type = DisplayString
_FeL2ModSW24AccountAddPassword_Object = MibScalar
feL2ModSW24AccountAddPassword = _FeL2ModSW24AccountAddPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4, 4),
    _FeL2ModSW24AccountAddPassword_Type()
)
feL2ModSW24AccountAddPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24AccountAddPassword.setStatus("current")


class _FeL2ModSW24DoAccountAdd_Type(Integer32):
    """Custom type feL2ModSW24DoAccountAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24DoAccountAdd_Type.__name__ = "Integer32"
_FeL2ModSW24DoAccountAdd_Object = MibScalar
feL2ModSW24DoAccountAdd = _FeL2ModSW24DoAccountAdd_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4, 5),
    _FeL2ModSW24DoAccountAdd_Type()
)
feL2ModSW24DoAccountAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24DoAccountAdd.setStatus("current")


class _FeL2ModSW24AccountDel_Type(Integer32):
    """Custom type feL2ModSW24AccountDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_FeL2ModSW24AccountDel_Type.__name__ = "Integer32"
_FeL2ModSW24AccountDel_Object = MibScalar
feL2ModSW24AccountDel = _FeL2ModSW24AccountDel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 1, 4, 6),
    _FeL2ModSW24AccountDel_Type()
)
feL2ModSW24AccountDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24AccountDel.setStatus("current")
_FeL2ModSW24Snmp_ObjectIdentity = ObjectIdentity
feL2ModSW24Snmp = _FeL2ModSW24Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 2)
)
_FeL2ModSW24GetCommunity_Type = DisplayString
_FeL2ModSW24GetCommunity_Object = MibScalar
feL2ModSW24GetCommunity = _FeL2ModSW24GetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 2, 1),
    _FeL2ModSW24GetCommunity_Type()
)
feL2ModSW24GetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24GetCommunity.setStatus("current")
_FeL2ModSW24SetCommunity_Type = DisplayString
_FeL2ModSW24SetCommunity_Object = MibScalar
feL2ModSW24SetCommunity = _FeL2ModSW24SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 2, 2),
    _FeL2ModSW24SetCommunity_Type()
)
feL2ModSW24SetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24SetCommunity.setStatus("current")


class _FeL2ModSW24TrapHostNumber_Type(Integer32):
    """Custom type feL2ModSW24TrapHostNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeL2ModSW24TrapHostNumber_Type.__name__ = "Integer32"
_FeL2ModSW24TrapHostNumber_Object = MibScalar
feL2ModSW24TrapHostNumber = _FeL2ModSW24TrapHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 2, 3),
    _FeL2ModSW24TrapHostNumber_Type()
)
feL2ModSW24TrapHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24TrapHostNumber.setStatus("current")
_FeL2ModSW24TrapHostTable_Object = MibTable
feL2ModSW24TrapHostTable = _FeL2ModSW24TrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 2, 4)
)
if mibBuilder.loadTexts:
    feL2ModSW24TrapHostTable.setStatus("current")
_FeL2ModSW24TrapHostEntry_Object = MibTableRow
feL2ModSW24TrapHostEntry = _FeL2ModSW24TrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 2, 4, 1)
)
feL2ModSW24TrapHostEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24TrapHostIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24TrapHostEntry.setStatus("current")


class _FeL2ModSW24TrapHostIndex_Type(Integer32):
    """Custom type feL2ModSW24TrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeL2ModSW24TrapHostIndex_Type.__name__ = "Integer32"
_FeL2ModSW24TrapHostIndex_Object = MibTableColumn
feL2ModSW24TrapHostIndex = _FeL2ModSW24TrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 2, 4, 1, 1),
    _FeL2ModSW24TrapHostIndex_Type()
)
feL2ModSW24TrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24TrapHostIndex.setStatus("current")
_FeL2ModSW24TrapHostIP_Type = IpAddress
_FeL2ModSW24TrapHostIP_Object = MibTableColumn
feL2ModSW24TrapHostIP = _FeL2ModSW24TrapHostIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 2, 4, 1, 2),
    _FeL2ModSW24TrapHostIP_Type()
)
feL2ModSW24TrapHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24TrapHostIP.setStatus("current")


class _FeL2ModSW24TrapHostPort_Type(Integer32):
    """Custom type feL2ModSW24TrapHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FeL2ModSW24TrapHostPort_Type.__name__ = "Integer32"
_FeL2ModSW24TrapHostPort_Object = MibTableColumn
feL2ModSW24TrapHostPort = _FeL2ModSW24TrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 2, 4, 1, 3),
    _FeL2ModSW24TrapHostPort_Type()
)
feL2ModSW24TrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24TrapHostPort.setStatus("current")
_FeL2ModSW24TrapHostCommunity_Type = DisplayString
_FeL2ModSW24TrapHostCommunity_Object = MibTableColumn
feL2ModSW24TrapHostCommunity = _FeL2ModSW24TrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 2, 4, 1, 4),
    _FeL2ModSW24TrapHostCommunity_Type()
)
feL2ModSW24TrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24TrapHostCommunity.setStatus("current")
_FeL2ModSW24Alarm_ObjectIdentity = ObjectIdentity
feL2ModSW24Alarm = _FeL2ModSW24Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3)
)
_FeL2ModSW24Event_ObjectIdentity = ObjectIdentity
feL2ModSW24Event = _FeL2ModSW24Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 1)
)


class _FeL2ModSW24EventNumber_Type(Integer32):
    """Custom type feL2ModSW24EventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24EventNumber_Type.__name__ = "Integer32"
_FeL2ModSW24EventNumber_Object = MibScalar
feL2ModSW24EventNumber = _FeL2ModSW24EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 1, 1),
    _FeL2ModSW24EventNumber_Type()
)
feL2ModSW24EventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24EventNumber.setStatus("current")
_FeL2ModSW24EventTable_Object = MibTable
feL2ModSW24EventTable = _FeL2ModSW24EventTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    feL2ModSW24EventTable.setStatus("current")
_FeL2ModSW24EventEntry_Object = MibTableRow
feL2ModSW24EventEntry = _FeL2ModSW24EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 1, 2, 1)
)
feL2ModSW24EventEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24EventIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24EventEntry.setStatus("current")


class _FeL2ModSW24EventIndex_Type(Integer32):
    """Custom type feL2ModSW24EventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24EventIndex_Type.__name__ = "Integer32"
_FeL2ModSW24EventIndex_Object = MibTableColumn
feL2ModSW24EventIndex = _FeL2ModSW24EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 1, 2, 1, 1),
    _FeL2ModSW24EventIndex_Type()
)
feL2ModSW24EventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24EventIndex.setStatus("current")
_FeL2ModSW24EventName_Type = DisplayString
_FeL2ModSW24EventName_Object = MibTableColumn
feL2ModSW24EventName = _FeL2ModSW24EventName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 1, 2, 1, 2),
    _FeL2ModSW24EventName_Type()
)
feL2ModSW24EventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24EventName.setStatus("current")


class _FeL2ModSW24EventSendEmail_Type(Integer32):
    """Custom type feL2ModSW24EventSendEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24EventSendEmail_Type.__name__ = "Integer32"
_FeL2ModSW24EventSendEmail_Object = MibTableColumn
feL2ModSW24EventSendEmail = _FeL2ModSW24EventSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 1, 2, 1, 3),
    _FeL2ModSW24EventSendEmail_Type()
)
feL2ModSW24EventSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24EventSendEmail.setStatus("current")


class _FeL2ModSW24EventSendSMS_Type(Integer32):
    """Custom type feL2ModSW24EventSendSMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24EventSendSMS_Type.__name__ = "Integer32"
_FeL2ModSW24EventSendSMS_Object = MibTableColumn
feL2ModSW24EventSendSMS = _FeL2ModSW24EventSendSMS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 1, 2, 1, 4),
    _FeL2ModSW24EventSendSMS_Type()
)
feL2ModSW24EventSendSMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24EventSendSMS.setStatus("current")


class _FeL2ModSW24EventSendTrap_Type(Integer32):
    """Custom type feL2ModSW24EventSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24EventSendTrap_Type.__name__ = "Integer32"
_FeL2ModSW24EventSendTrap_Object = MibTableColumn
feL2ModSW24EventSendTrap = _FeL2ModSW24EventSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 1, 2, 1, 5),
    _FeL2ModSW24EventSendTrap_Type()
)
feL2ModSW24EventSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24EventSendTrap.setStatus("current")
_FeL2ModSW24Email_ObjectIdentity = ObjectIdentity
feL2ModSW24Email = _FeL2ModSW24Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 2)
)
_FeL2ModSW24EmailServer_Type = DisplayString
_FeL2ModSW24EmailServer_Object = MibScalar
feL2ModSW24EmailServer = _FeL2ModSW24EmailServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 2, 1),
    _FeL2ModSW24EmailServer_Type()
)
feL2ModSW24EmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24EmailServer.setStatus("current")
_FeL2ModSW24EmailUsername_Type = DisplayString
_FeL2ModSW24EmailUsername_Object = MibScalar
feL2ModSW24EmailUsername = _FeL2ModSW24EmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 2, 2),
    _FeL2ModSW24EmailUsername_Type()
)
feL2ModSW24EmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24EmailUsername.setStatus("current")
_FeL2ModSW24EmailPassword_Type = DisplayString
_FeL2ModSW24EmailPassword_Object = MibScalar
feL2ModSW24EmailPassword = _FeL2ModSW24EmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 2, 3),
    _FeL2ModSW24EmailPassword_Type()
)
feL2ModSW24EmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24EmailPassword.setStatus("current")


class _FeL2ModSW24EmailUserNumber_Type(Integer32):
    """Custom type feL2ModSW24EmailUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeL2ModSW24EmailUserNumber_Type.__name__ = "Integer32"
_FeL2ModSW24EmailUserNumber_Object = MibScalar
feL2ModSW24EmailUserNumber = _FeL2ModSW24EmailUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 2, 4),
    _FeL2ModSW24EmailUserNumber_Type()
)
feL2ModSW24EmailUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24EmailUserNumber.setStatus("current")
_FeL2ModSW24EmailUserTable_Object = MibTable
feL2ModSW24EmailUserTable = _FeL2ModSW24EmailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    feL2ModSW24EmailUserTable.setStatus("current")
_FeL2ModSW24EmailUserEntry_Object = MibTableRow
feL2ModSW24EmailUserEntry = _FeL2ModSW24EmailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 2, 5, 1)
)
feL2ModSW24EmailUserEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24EmailUserIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24EmailUserEntry.setStatus("current")


class _FeL2ModSW24EmailUserIndex_Type(Integer32):
    """Custom type feL2ModSW24EmailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeL2ModSW24EmailUserIndex_Type.__name__ = "Integer32"
_FeL2ModSW24EmailUserIndex_Object = MibTableColumn
feL2ModSW24EmailUserIndex = _FeL2ModSW24EmailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 2, 5, 1, 1),
    _FeL2ModSW24EmailUserIndex_Type()
)
feL2ModSW24EmailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24EmailUserIndex.setStatus("current")
_FeL2ModSW24EmailUserAddress_Type = DisplayString
_FeL2ModSW24EmailUserAddress_Object = MibTableColumn
feL2ModSW24EmailUserAddress = _FeL2ModSW24EmailUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 2, 5, 1, 2),
    _FeL2ModSW24EmailUserAddress_Type()
)
feL2ModSW24EmailUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24EmailUserAddress.setStatus("current")
_FeL2ModSW24SMS_ObjectIdentity = ObjectIdentity
feL2ModSW24SMS = _FeL2ModSW24SMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 3)
)
_FeL2ModSW24SMSServer_Type = DisplayString
_FeL2ModSW24SMSServer_Object = MibScalar
feL2ModSW24SMSServer = _FeL2ModSW24SMSServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 3, 1),
    _FeL2ModSW24SMSServer_Type()
)
feL2ModSW24SMSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24SMSServer.setStatus("current")
_FeL2ModSW24SMSUsername_Type = DisplayString
_FeL2ModSW24SMSUsername_Object = MibScalar
feL2ModSW24SMSUsername = _FeL2ModSW24SMSUsername_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 3, 2),
    _FeL2ModSW24SMSUsername_Type()
)
feL2ModSW24SMSUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24SMSUsername.setStatus("current")
_FeL2ModSW24SMSPassword_Type = DisplayString
_FeL2ModSW24SMSPassword_Object = MibScalar
feL2ModSW24SMSPassword = _FeL2ModSW24SMSPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 3, 3),
    _FeL2ModSW24SMSPassword_Type()
)
feL2ModSW24SMSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24SMSPassword.setStatus("current")


class _FeL2ModSW24SMSUserNumber_Type(Integer32):
    """Custom type feL2ModSW24SMSUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeL2ModSW24SMSUserNumber_Type.__name__ = "Integer32"
_FeL2ModSW24SMSUserNumber_Object = MibScalar
feL2ModSW24SMSUserNumber = _FeL2ModSW24SMSUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 3, 4),
    _FeL2ModSW24SMSUserNumber_Type()
)
feL2ModSW24SMSUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SMSUserNumber.setStatus("current")
_FeL2ModSW24SMSUserTable_Object = MibTable
feL2ModSW24SMSUserTable = _FeL2ModSW24SMSUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    feL2ModSW24SMSUserTable.setStatus("current")
_FeL2ModSW24SMSUserEntry_Object = MibTableRow
feL2ModSW24SMSUserEntry = _FeL2ModSW24SMSUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 3, 5, 1)
)
feL2ModSW24SMSUserEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24SMSUserIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24SMSUserEntry.setStatus("current")


class _FeL2ModSW24SMSUserIndex_Type(Integer32):
    """Custom type feL2ModSW24SMSUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeL2ModSW24SMSUserIndex_Type.__name__ = "Integer32"
_FeL2ModSW24SMSUserIndex_Object = MibTableColumn
feL2ModSW24SMSUserIndex = _FeL2ModSW24SMSUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 3, 5, 1, 1),
    _FeL2ModSW24SMSUserIndex_Type()
)
feL2ModSW24SMSUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SMSUserIndex.setStatus("current")
_FeL2ModSW24SMSUserMobilePhone_Type = DisplayString
_FeL2ModSW24SMSUserMobilePhone_Object = MibTableColumn
feL2ModSW24SMSUserMobilePhone = _FeL2ModSW24SMSUserMobilePhone_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 3, 3, 5, 1, 2),
    _FeL2ModSW24SMSUserMobilePhone_Type()
)
feL2ModSW24SMSUserMobilePhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24SMSUserMobilePhone.setStatus("current")
_FeL2ModSW24Tftp_ObjectIdentity = ObjectIdentity
feL2ModSW24Tftp = _FeL2ModSW24Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 4)
)
_FeL2ModSW24TftpServer_Type = IpAddress
_FeL2ModSW24TftpServer_Object = MibScalar
feL2ModSW24TftpServer = _FeL2ModSW24TftpServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 4, 1),
    _FeL2ModSW24TftpServer_Type()
)
feL2ModSW24TftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24TftpServer.setStatus("current")
_FeL2ModSW24Configuration_ObjectIdentity = ObjectIdentity
feL2ModSW24Configuration = _FeL2ModSW24Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 5)
)
_FeL2ModSW24SaveRestore_ObjectIdentity = ObjectIdentity
feL2ModSW24SaveRestore = _FeL2ModSW24SaveRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 5, 1)
)


class _FeL2ModSW24SaveStart_Type(Integer32):
    """Custom type feL2ModSW24SaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24SaveStart_Type.__name__ = "Integer32"
_FeL2ModSW24SaveStart_Object = MibScalar
feL2ModSW24SaveStart = _FeL2ModSW24SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 5, 1, 1),
    _FeL2ModSW24SaveStart_Type()
)
feL2ModSW24SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24SaveStart.setStatus("current")


class _FeL2ModSW24SaveUser_Type(Integer32):
    """Custom type feL2ModSW24SaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24SaveUser_Type.__name__ = "Integer32"
_FeL2ModSW24SaveUser_Object = MibScalar
feL2ModSW24SaveUser = _FeL2ModSW24SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 5, 1, 2),
    _FeL2ModSW24SaveUser_Type()
)
feL2ModSW24SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24SaveUser.setStatus("current")


class _FeL2ModSW24RestoreDefault_Type(Integer32):
    """Custom type feL2ModSW24RestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_FeL2ModSW24RestoreDefault_Type.__name__ = "Integer32"
_FeL2ModSW24RestoreDefault_Object = MibScalar
feL2ModSW24RestoreDefault = _FeL2ModSW24RestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 5, 1, 3),
    _FeL2ModSW24RestoreDefault_Type()
)
feL2ModSW24RestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24RestoreDefault.setStatus("current")


class _FeL2ModSW24RestoreUser_Type(Integer32):
    """Custom type feL2ModSW24RestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24RestoreUser_Type.__name__ = "Integer32"
_FeL2ModSW24RestoreUser_Object = MibScalar
feL2ModSW24RestoreUser = _FeL2ModSW24RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 5, 1, 4),
    _FeL2ModSW24RestoreUser_Type()
)
feL2ModSW24RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24RestoreUser.setStatus("current")
_FeL2ModSW24ConfigFile_ObjectIdentity = ObjectIdentity
feL2ModSW24ConfigFile = _FeL2ModSW24ConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 5, 2)
)
_FeL2ModSW24ExportConfigName_Type = DisplayString
_FeL2ModSW24ExportConfigName_Object = MibScalar
feL2ModSW24ExportConfigName = _FeL2ModSW24ExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 5, 2, 1),
    _FeL2ModSW24ExportConfigName_Type()
)
feL2ModSW24ExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24ExportConfigName.setStatus("current")


class _FeL2ModSW24DoExportConfig_Type(Integer32):
    """Custom type feL2ModSW24DoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_FeL2ModSW24DoExportConfig_Type.__name__ = "Integer32"
_FeL2ModSW24DoExportConfig_Object = MibScalar
feL2ModSW24DoExportConfig = _FeL2ModSW24DoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 5, 2, 2),
    _FeL2ModSW24DoExportConfig_Type()
)
feL2ModSW24DoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24DoExportConfig.setStatus("current")
_FeL2ModSW24ImportConfigName_Type = DisplayString
_FeL2ModSW24ImportConfigName_Object = MibScalar
feL2ModSW24ImportConfigName = _FeL2ModSW24ImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 5, 2, 3),
    _FeL2ModSW24ImportConfigName_Type()
)
feL2ModSW24ImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24ImportConfigName.setStatus("current")


class _FeL2ModSW24DoImportConfig_Type(Integer32):
    """Custom type feL2ModSW24DoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_FeL2ModSW24DoImportConfig_Type.__name__ = "Integer32"
_FeL2ModSW24DoImportConfig_Object = MibScalar
feL2ModSW24DoImportConfig = _FeL2ModSW24DoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 5, 2, 4),
    _FeL2ModSW24DoImportConfig_Type()
)
feL2ModSW24DoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24DoImportConfig.setStatus("current")
_FeL2ModSW24Diagnostic_ObjectIdentity = ObjectIdentity
feL2ModSW24Diagnostic = _FeL2ModSW24Diagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 6)
)
_FeL2ModSW24EEPROMTest_Type = DisplayString
_FeL2ModSW24EEPROMTest_Object = MibScalar
feL2ModSW24EEPROMTest = _FeL2ModSW24EEPROMTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 6, 1),
    _FeL2ModSW24EEPROMTest_Type()
)
feL2ModSW24EEPROMTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24EEPROMTest.setStatus("current")
_FeL2ModSW24UartTest_Type = DisplayString
_FeL2ModSW24UartTest_Object = MibScalar
feL2ModSW24UartTest = _FeL2ModSW24UartTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 6, 2),
    _FeL2ModSW24UartTest_Type()
)
feL2ModSW24UartTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24UartTest.setStatus("current")
_FeL2ModSW24DramTest_Type = DisplayString
_FeL2ModSW24DramTest_Object = MibScalar
feL2ModSW24DramTest = _FeL2ModSW24DramTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 6, 3),
    _FeL2ModSW24DramTest_Type()
)
feL2ModSW24DramTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24DramTest.setStatus("current")
_FeL2ModSW24FlashTest_Type = DisplayString
_FeL2ModSW24FlashTest_Object = MibScalar
feL2ModSW24FlashTest = _FeL2ModSW24FlashTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 6, 4),
    _FeL2ModSW24FlashTest_Type()
)
feL2ModSW24FlashTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24FlashTest.setStatus("current")
_FeL2ModSW24InternalLoopbackTest_Type = DisplayString
_FeL2ModSW24InternalLoopbackTest_Object = MibScalar
feL2ModSW24InternalLoopbackTest = _FeL2ModSW24InternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 6, 5),
    _FeL2ModSW24InternalLoopbackTest_Type()
)
feL2ModSW24InternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24InternalLoopbackTest.setStatus("current")
_FeL2ModSW24ExternalLoopbackTest_Type = DisplayString
_FeL2ModSW24ExternalLoopbackTest_Object = MibScalar
feL2ModSW24ExternalLoopbackTest = _FeL2ModSW24ExternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 6, 6),
    _FeL2ModSW24ExternalLoopbackTest_Type()
)
feL2ModSW24ExternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24ExternalLoopbackTest.setStatus("current")
_FeL2ModSW24PingTest_Type = DisplayString
_FeL2ModSW24PingTest_Object = MibScalar
feL2ModSW24PingTest = _FeL2ModSW24PingTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 6, 7),
    _FeL2ModSW24PingTest_Type()
)
feL2ModSW24PingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24PingTest.setStatus("current")
_FeL2ModSW24Log_ObjectIdentity = ObjectIdentity
feL2ModSW24Log = _FeL2ModSW24Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 7)
)


class _FeL2ModSW24ClearLog_Type(Integer32):
    """Custom type feL2ModSW24ClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24ClearLog_Type.__name__ = "Integer32"
_FeL2ModSW24ClearLog_Object = MibScalar
feL2ModSW24ClearLog = _FeL2ModSW24ClearLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 7, 1),
    _FeL2ModSW24ClearLog_Type()
)
feL2ModSW24ClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24ClearLog.setStatus("current")


class _FeL2ModSW24UploadLog_Type(Integer32):
    """Custom type feL2ModSW24UploadLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24UploadLog_Type.__name__ = "Integer32"
_FeL2ModSW24UploadLog_Object = MibScalar
feL2ModSW24UploadLog = _FeL2ModSW24UploadLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 7, 2),
    _FeL2ModSW24UploadLog_Type()
)
feL2ModSW24UploadLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24UploadLog.setStatus("current")


class _FeL2ModSW24AutoUploadLogState_Type(Integer32):
    """Custom type feL2ModSW24AutoUploadLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24AutoUploadLogState_Type.__name__ = "Integer32"
_FeL2ModSW24AutoUploadLogState_Object = MibScalar
feL2ModSW24AutoUploadLogState = _FeL2ModSW24AutoUploadLogState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 7, 3),
    _FeL2ModSW24AutoUploadLogState_Type()
)
feL2ModSW24AutoUploadLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24AutoUploadLogState.setStatus("current")


class _FeL2ModSW24LogNumber_Type(Integer32):
    """Custom type feL2ModSW24LogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_FeL2ModSW24LogNumber_Type.__name__ = "Integer32"
_FeL2ModSW24LogNumber_Object = MibScalar
feL2ModSW24LogNumber = _FeL2ModSW24LogNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 7, 4),
    _FeL2ModSW24LogNumber_Type()
)
feL2ModSW24LogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24LogNumber.setStatus("current")
_FeL2ModSW24LogTable_Object = MibTable
feL2ModSW24LogTable = _FeL2ModSW24LogTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 7, 5)
)
if mibBuilder.loadTexts:
    feL2ModSW24LogTable.setStatus("current")
_FeL2ModSW24LogEntry_Object = MibTableRow
feL2ModSW24LogEntry = _FeL2ModSW24LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 7, 5, 1)
)
feL2ModSW24LogEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24LogIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24LogEntry.setStatus("current")


class _FeL2ModSW24LogIndex_Type(Integer32):
    """Custom type feL2ModSW24LogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_FeL2ModSW24LogIndex_Type.__name__ = "Integer32"
_FeL2ModSW24LogIndex_Object = MibTableColumn
feL2ModSW24LogIndex = _FeL2ModSW24LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 7, 5, 1, 1),
    _FeL2ModSW24LogIndex_Type()
)
feL2ModSW24LogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24LogIndex.setStatus("current")
_FeL2ModSW24LogEvent_Type = DisplayString
_FeL2ModSW24LogEvent_Object = MibTableColumn
feL2ModSW24LogEvent = _FeL2ModSW24LogEvent_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 7, 5, 1, 2),
    _FeL2ModSW24LogEvent_Type()
)
feL2ModSW24LogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24LogEvent.setStatus("current")
_FeL2ModSW24Firmware_ObjectIdentity = ObjectIdentity
feL2ModSW24Firmware = _FeL2ModSW24Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 8)
)
_FeL2ModSW24FirmwareFileName_Type = DisplayString
_FeL2ModSW24FirmwareFileName_Object = MibScalar
feL2ModSW24FirmwareFileName = _FeL2ModSW24FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 8, 1),
    _FeL2ModSW24FirmwareFileName_Type()
)
feL2ModSW24FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24FirmwareFileName.setStatus("current")


class _FeL2ModSW24DoFirmwareUpgrade_Type(Integer32):
    """Custom type feL2ModSW24DoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24DoFirmwareUpgrade_Type.__name__ = "Integer32"
_FeL2ModSW24DoFirmwareUpgrade_Object = MibScalar
feL2ModSW24DoFirmwareUpgrade = _FeL2ModSW24DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 8, 2),
    _FeL2ModSW24DoFirmwareUpgrade_Type()
)
feL2ModSW24DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24DoFirmwareUpgrade.setStatus("current")
_FeL2ModSW24Port_ObjectIdentity = ObjectIdentity
feL2ModSW24Port = _FeL2ModSW24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9)
)
_FeL2ModSW24PortStatus_ObjectIdentity = ObjectIdentity
feL2ModSW24PortStatus = _FeL2ModSW24PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1)
)


class _FeL2ModSW24PortStatusNumber_Type(Integer32):
    """Custom type feL2ModSW24PortStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24PortStatusNumber_Type.__name__ = "Integer32"
_FeL2ModSW24PortStatusNumber_Object = MibScalar
feL2ModSW24PortStatusNumber = _FeL2ModSW24PortStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1, 1),
    _FeL2ModSW24PortStatusNumber_Type()
)
feL2ModSW24PortStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24PortStatusNumber.setStatus("current")
_FeL2ModSW24PortStatusTable_Object = MibTable
feL2ModSW24PortStatusTable = _FeL2ModSW24PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    feL2ModSW24PortStatusTable.setStatus("current")
_FeL2ModSW24PortStatusEntry_Object = MibTableRow
feL2ModSW24PortStatusEntry = _FeL2ModSW24PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1, 2, 1)
)
feL2ModSW24PortStatusEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24PortStatusIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24PortStatusEntry.setStatus("current")


class _FeL2ModSW24PortStatusIndex_Type(Integer32):
    """Custom type feL2ModSW24PortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24PortStatusIndex_Type.__name__ = "Integer32"
_FeL2ModSW24PortStatusIndex_Object = MibTableColumn
feL2ModSW24PortStatusIndex = _FeL2ModSW24PortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1, 2, 1, 1),
    _FeL2ModSW24PortStatusIndex_Type()
)
feL2ModSW24PortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24PortStatusIndex.setStatus("current")
_FeL2ModSW24PortStatusMedia_Type = DisplayString
_FeL2ModSW24PortStatusMedia_Object = MibTableColumn
feL2ModSW24PortStatusMedia = _FeL2ModSW24PortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1, 2, 1, 2),
    _FeL2ModSW24PortStatusMedia_Type()
)
feL2ModSW24PortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24PortStatusMedia.setStatus("current")
_FeL2ModSW24PortStatusLink_Type = DisplayString
_FeL2ModSW24PortStatusLink_Object = MibTableColumn
feL2ModSW24PortStatusLink = _FeL2ModSW24PortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1, 2, 1, 3),
    _FeL2ModSW24PortStatusLink_Type()
)
feL2ModSW24PortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24PortStatusLink.setStatus("current")
_FeL2ModSW24PortStatusPortState_Type = DisplayString
_FeL2ModSW24PortStatusPortState_Object = MibTableColumn
feL2ModSW24PortStatusPortState = _FeL2ModSW24PortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1, 2, 1, 4),
    _FeL2ModSW24PortStatusPortState_Type()
)
feL2ModSW24PortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24PortStatusPortState.setStatus("current")
_FeL2ModSW24PortStatusAutoNego_Type = DisplayString
_FeL2ModSW24PortStatusAutoNego_Object = MibTableColumn
feL2ModSW24PortStatusAutoNego = _FeL2ModSW24PortStatusAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1, 2, 1, 5),
    _FeL2ModSW24PortStatusAutoNego_Type()
)
feL2ModSW24PortStatusAutoNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24PortStatusAutoNego.setStatus("current")
_FeL2ModSW24PortStatusSpdDpx_Type = DisplayString
_FeL2ModSW24PortStatusSpdDpx_Object = MibTableColumn
feL2ModSW24PortStatusSpdDpx = _FeL2ModSW24PortStatusSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1, 2, 1, 6),
    _FeL2ModSW24PortStatusSpdDpx_Type()
)
feL2ModSW24PortStatusSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24PortStatusSpdDpx.setStatus("current")
_FeL2ModSW24PortStatusFlwCtrl_Type = DisplayString
_FeL2ModSW24PortStatusFlwCtrl_Object = MibTableColumn
feL2ModSW24PortStatusFlwCtrl = _FeL2ModSW24PortStatusFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1, 2, 1, 7),
    _FeL2ModSW24PortStatusFlwCtrl_Type()
)
feL2ModSW24PortStatusFlwCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24PortStatusFlwCtrl.setStatus("current")
_FeL2ModSW24PortStatuDescription_Type = DisplayString
_FeL2ModSW24PortStatuDescription_Object = MibTableColumn
feL2ModSW24PortStatuDescription = _FeL2ModSW24PortStatuDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 1, 2, 1, 8),
    _FeL2ModSW24PortStatuDescription_Type()
)
feL2ModSW24PortStatuDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24PortStatuDescription.setStatus("current")
_FeL2ModSW24PortConf_ObjectIdentity = ObjectIdentity
feL2ModSW24PortConf = _FeL2ModSW24PortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 2)
)


class _FeL2ModSW24PortConfNumber_Type(Integer32):
    """Custom type feL2ModSW24PortConfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24PortConfNumber_Type.__name__ = "Integer32"
_FeL2ModSW24PortConfNumber_Object = MibScalar
feL2ModSW24PortConfNumber = _FeL2ModSW24PortConfNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 2, 1),
    _FeL2ModSW24PortConfNumber_Type()
)
feL2ModSW24PortConfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24PortConfNumber.setStatus("current")
_FeL2ModSW24PortConfTable_Object = MibTable
feL2ModSW24PortConfTable = _FeL2ModSW24PortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    feL2ModSW24PortConfTable.setStatus("current")
_FeL2ModSW24PortConfEntry_Object = MibTableRow
feL2ModSW24PortConfEntry = _FeL2ModSW24PortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 2, 2, 1)
)
feL2ModSW24PortConfEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24PortConfIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24PortConfEntry.setStatus("current")


class _FeL2ModSW24PortConfIndex_Type(Integer32):
    """Custom type feL2ModSW24PortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24PortConfIndex_Type.__name__ = "Integer32"
_FeL2ModSW24PortConfIndex_Object = MibTableColumn
feL2ModSW24PortConfIndex = _FeL2ModSW24PortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 2, 2, 1, 1),
    _FeL2ModSW24PortConfIndex_Type()
)
feL2ModSW24PortConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24PortConfIndex.setStatus("current")


class _FeL2ModSW24PortConfPortState_Type(Integer32):
    """Custom type feL2ModSW24PortConfPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24PortConfPortState_Type.__name__ = "Integer32"
_FeL2ModSW24PortConfPortState_Object = MibTableColumn
feL2ModSW24PortConfPortState = _FeL2ModSW24PortConfPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 2, 2, 1, 2),
    _FeL2ModSW24PortConfPortState_Type()
)
feL2ModSW24PortConfPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24PortConfPortState.setStatus("current")


class _FeL2ModSW24PortConfSpdDpx_Type(Integer32):
    """Custom type feL2ModSW24PortConfSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_FeL2ModSW24PortConfSpdDpx_Type.__name__ = "Integer32"
_FeL2ModSW24PortConfSpdDpx_Object = MibTableColumn
feL2ModSW24PortConfSpdDpx = _FeL2ModSW24PortConfSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 2, 2, 1, 3),
    _FeL2ModSW24PortConfSpdDpx_Type()
)
feL2ModSW24PortConfSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24PortConfSpdDpx.setStatus("current")


class _FeL2ModSW24PortConfFlwCtrl_Type(Integer32):
    """Custom type feL2ModSW24PortConfFlwCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24PortConfFlwCtrl_Type.__name__ = "Integer32"
_FeL2ModSW24PortConfFlwCtrl_Object = MibTableColumn
feL2ModSW24PortConfFlwCtrl = _FeL2ModSW24PortConfFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 2, 2, 1, 4),
    _FeL2ModSW24PortConfFlwCtrl_Type()
)
feL2ModSW24PortConfFlwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24PortConfFlwCtrl.setStatus("current")
_FeL2ModSW24PortConfDescription_Type = DisplayString
_FeL2ModSW24PortConfDescription_Object = MibTableColumn
feL2ModSW24PortConfDescription = _FeL2ModSW24PortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 9, 2, 2, 1, 5),
    _FeL2ModSW24PortConfDescription_Type()
)
feL2ModSW24PortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24PortConfDescription.setStatus("current")
_FeL2ModSW24Mirror_ObjectIdentity = ObjectIdentity
feL2ModSW24Mirror = _FeL2ModSW24Mirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 10)
)


class _FeL2ModSW24MirrorMode_Type(Integer32):
    """Custom type feL2ModSW24MirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24MirrorMode_Type.__name__ = "Integer32"
_FeL2ModSW24MirrorMode_Object = MibScalar
feL2ModSW24MirrorMode = _FeL2ModSW24MirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 10, 1),
    _FeL2ModSW24MirrorMode_Type()
)
feL2ModSW24MirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24MirrorMode.setStatus("current")


class _FeL2ModSW24MirroringPort_Type(Integer32):
    """Custom type feL2ModSW24MirroringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24MirroringPort_Type.__name__ = "Integer32"
_FeL2ModSW24MirroringPort_Object = MibScalar
feL2ModSW24MirroringPort = _FeL2ModSW24MirroringPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 10, 2),
    _FeL2ModSW24MirroringPort_Type()
)
feL2ModSW24MirroringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24MirroringPort.setStatus("current")
_FeL2ModSW24MirroredPorts_Type = DisplayString
_FeL2ModSW24MirroredPorts_Object = MibScalar
feL2ModSW24MirroredPorts = _FeL2ModSW24MirroredPorts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 10, 3),
    _FeL2ModSW24MirroredPorts_Type()
)
feL2ModSW24MirroredPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24MirroredPorts.setStatus("current")
_FeL2ModSW24MaxPktLen_ObjectIdentity = ObjectIdentity
feL2ModSW24MaxPktLen = _FeL2ModSW24MaxPktLen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 11)
)
_FeL2ModSW24MaxPktLen1_ObjectIdentity = ObjectIdentity
feL2ModSW24MaxPktLen1 = _FeL2ModSW24MaxPktLen1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 11, 1)
)


class _FeL2ModSW24MaxPktLenPortNumber_Type(Integer32):
    """Custom type feL2ModSW24MaxPktLenPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24MaxPktLenPortNumber_Type.__name__ = "Integer32"
_FeL2ModSW24MaxPktLenPortNumber_Object = MibScalar
feL2ModSW24MaxPktLenPortNumber = _FeL2ModSW24MaxPktLenPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 11, 1, 1),
    _FeL2ModSW24MaxPktLenPortNumber_Type()
)
feL2ModSW24MaxPktLenPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24MaxPktLenPortNumber.setStatus("current")
_FeL2ModSW24MaxPktLenConfTable_Object = MibTable
feL2ModSW24MaxPktLenConfTable = _FeL2ModSW24MaxPktLenConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    feL2ModSW24MaxPktLenConfTable.setStatus("current")
_FeL2ModSW24MaxPktLenConfEntry_Object = MibTableRow
feL2ModSW24MaxPktLenConfEntry = _FeL2ModSW24MaxPktLenConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 11, 1, 2, 1)
)
feL2ModSW24MaxPktLenConfEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24MaxPktLenConfIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24MaxPktLenConfEntry.setStatus("current")


class _FeL2ModSW24MaxPktLenConfIndex_Type(Integer32):
    """Custom type feL2ModSW24MaxPktLenConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24MaxPktLenConfIndex_Type.__name__ = "Integer32"
_FeL2ModSW24MaxPktLenConfIndex_Object = MibTableColumn
feL2ModSW24MaxPktLenConfIndex = _FeL2ModSW24MaxPktLenConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 11, 1, 2, 1, 1),
    _FeL2ModSW24MaxPktLenConfIndex_Type()
)
feL2ModSW24MaxPktLenConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24MaxPktLenConfIndex.setStatus("current")


class _FeL2ModSW24MaxPktLenConfSetting_Type(Integer32):
    """Custom type feL2ModSW24MaxPktLenConfSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 1518),
        ValueRangeConstraint(1532, 1532),
        ValueRangeConstraint(9216, 9216),
    )


_FeL2ModSW24MaxPktLenConfSetting_Type.__name__ = "Integer32"
_FeL2ModSW24MaxPktLenConfSetting_Object = MibTableColumn
feL2ModSW24MaxPktLenConfSetting = _FeL2ModSW24MaxPktLenConfSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 11, 1, 2, 1, 2),
    _FeL2ModSW24MaxPktLenConfSetting_Type()
)
feL2ModSW24MaxPktLenConfSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24MaxPktLenConfSetting.setStatus("current")
_FeL2ModSW24Bandwidth_ObjectIdentity = ObjectIdentity
feL2ModSW24Bandwidth = _FeL2ModSW24Bandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12)
)
_FeL2ModSW24Bandwidth1_ObjectIdentity = ObjectIdentity
feL2ModSW24Bandwidth1 = _FeL2ModSW24Bandwidth1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12, 1)
)


class _FeL2ModSW24BandwidthPortNumber_Type(Integer32):
    """Custom type feL2ModSW24BandwidthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24BandwidthPortNumber_Type.__name__ = "Integer32"
_FeL2ModSW24BandwidthPortNumber_Object = MibScalar
feL2ModSW24BandwidthPortNumber = _FeL2ModSW24BandwidthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12, 1, 1),
    _FeL2ModSW24BandwidthPortNumber_Type()
)
feL2ModSW24BandwidthPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24BandwidthPortNumber.setStatus("current")
_FeL2ModSW24BandwidthConfTable_Object = MibTable
feL2ModSW24BandwidthConfTable = _FeL2ModSW24BandwidthConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    feL2ModSW24BandwidthConfTable.setStatus("current")
_FeL2ModSW24BandwidthConfEntry_Object = MibTableRow
feL2ModSW24BandwidthConfEntry = _FeL2ModSW24BandwidthConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12, 1, 2, 1)
)
feL2ModSW24BandwidthConfEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24BandwidthConfIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24BandwidthConfEntry.setStatus("current")


class _FeL2ModSW24BandwidthConfIndex_Type(Integer32):
    """Custom type feL2ModSW24BandwidthConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24BandwidthConfIndex_Type.__name__ = "Integer32"
_FeL2ModSW24BandwidthConfIndex_Object = MibTableColumn
feL2ModSW24BandwidthConfIndex = _FeL2ModSW24BandwidthConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12, 1, 2, 1, 1),
    _FeL2ModSW24BandwidthConfIndex_Type()
)
feL2ModSW24BandwidthConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24BandwidthConfIndex.setStatus("current")


class _FeL2ModSW24BandwidthConfIngressState_Type(Integer32):
    """Custom type feL2ModSW24BandwidthConfIngressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24BandwidthConfIngressState_Type.__name__ = "Integer32"
_FeL2ModSW24BandwidthConfIngressState_Object = MibTableColumn
feL2ModSW24BandwidthConfIngressState = _FeL2ModSW24BandwidthConfIngressState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12, 1, 2, 1, 2),
    _FeL2ModSW24BandwidthConfIngressState_Type()
)
feL2ModSW24BandwidthConfIngressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24BandwidthConfIngressState.setStatus("current")


class _FeL2ModSW24BandwidthConfIngressBW_Type(Integer32):
    """Custom type feL2ModSW24BandwidthConfIngressBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FeL2ModSW24BandwidthConfIngressBW_Type.__name__ = "Integer32"
_FeL2ModSW24BandwidthConfIngressBW_Object = MibTableColumn
feL2ModSW24BandwidthConfIngressBW = _FeL2ModSW24BandwidthConfIngressBW_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12, 1, 2, 1, 3),
    _FeL2ModSW24BandwidthConfIngressBW_Type()
)
feL2ModSW24BandwidthConfIngressBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24BandwidthConfIngressBW.setStatus("current")


class _FeL2ModSW24BandwidthConfStormState_Type(Integer32):
    """Custom type feL2ModSW24BandwidthConfStormState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24BandwidthConfStormState_Type.__name__ = "Integer32"
_FeL2ModSW24BandwidthConfStormState_Object = MibTableColumn
feL2ModSW24BandwidthConfStormState = _FeL2ModSW24BandwidthConfStormState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12, 1, 2, 1, 4),
    _FeL2ModSW24BandwidthConfStormState_Type()
)
feL2ModSW24BandwidthConfStormState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24BandwidthConfStormState.setStatus("current")


class _FeL2ModSW24BandwidthConfStormBW_Type(Integer32):
    """Custom type feL2ModSW24BandwidthConfStormBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FeL2ModSW24BandwidthConfStormBW_Type.__name__ = "Integer32"
_FeL2ModSW24BandwidthConfStormBW_Object = MibTableColumn
feL2ModSW24BandwidthConfStormBW = _FeL2ModSW24BandwidthConfStormBW_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12, 1, 2, 1, 5),
    _FeL2ModSW24BandwidthConfStormBW_Type()
)
feL2ModSW24BandwidthConfStormBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24BandwidthConfStormBW.setStatus("current")


class _FeL2ModSW24BandwidthConfEgressState_Type(Integer32):
    """Custom type feL2ModSW24BandwidthConfEgressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24BandwidthConfEgressState_Type.__name__ = "Integer32"
_FeL2ModSW24BandwidthConfEgressState_Object = MibTableColumn
feL2ModSW24BandwidthConfEgressState = _FeL2ModSW24BandwidthConfEgressState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12, 1, 2, 1, 6),
    _FeL2ModSW24BandwidthConfEgressState_Type()
)
feL2ModSW24BandwidthConfEgressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24BandwidthConfEgressState.setStatus("current")


class _FeL2ModSW24BandwidthConfEgressBW_Type(Integer32):
    """Custom type feL2ModSW24BandwidthConfEgressBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FeL2ModSW24BandwidthConfEgressBW_Type.__name__ = "Integer32"
_FeL2ModSW24BandwidthConfEgressBW_Object = MibTableColumn
feL2ModSW24BandwidthConfEgressBW = _FeL2ModSW24BandwidthConfEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 12, 1, 2, 1, 7),
    _FeL2ModSW24BandwidthConfEgressBW_Type()
)
feL2ModSW24BandwidthConfEgressBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24BandwidthConfEgressBW.setStatus("current")
_FeL2ModSW24LoopDetectedConf_ObjectIdentity = ObjectIdentity
feL2ModSW24LoopDetectedConf = _FeL2ModSW24LoopDetectedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 13)
)


class _FeL2ModSW24LoopDetectedNumber_Type(Integer32):
    """Custom type feL2ModSW24LoopDetectedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24LoopDetectedNumber_Type.__name__ = "Integer32"
_FeL2ModSW24LoopDetectedNumber_Object = MibScalar
feL2ModSW24LoopDetectedNumber = _FeL2ModSW24LoopDetectedNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 13, 1),
    _FeL2ModSW24LoopDetectedNumber_Type()
)
feL2ModSW24LoopDetectedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24LoopDetectedNumber.setStatus("current")
_FeL2ModSW24LoopDetectedTable_Object = MibTable
feL2ModSW24LoopDetectedTable = _FeL2ModSW24LoopDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 13, 2)
)
if mibBuilder.loadTexts:
    feL2ModSW24LoopDetectedTable.setStatus("current")
_FeL2ModSW24LoopDetectedEntry_Object = MibTableRow
feL2ModSW24LoopDetectedEntry = _FeL2ModSW24LoopDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 13, 2, 1)
)
feL2ModSW24LoopDetectedEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24LoopDetectedfIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24LoopDetectedEntry.setStatus("current")


class _FeL2ModSW24LoopDetectedfIndex_Type(Integer32):
    """Custom type feL2ModSW24LoopDetectedfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24LoopDetectedfIndex_Type.__name__ = "Integer32"
_FeL2ModSW24LoopDetectedfIndex_Object = MibTableColumn
feL2ModSW24LoopDetectedfIndex = _FeL2ModSW24LoopDetectedfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 13, 2, 1, 1),
    _FeL2ModSW24LoopDetectedfIndex_Type()
)
feL2ModSW24LoopDetectedfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24LoopDetectedfIndex.setStatus("current")


class _FeL2ModSW24LoopDetectedStateEbl_Type(Integer32):
    """Custom type feL2ModSW24LoopDetectedStateEbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24LoopDetectedStateEbl_Type.__name__ = "Integer32"
_FeL2ModSW24LoopDetectedStateEbl_Object = MibTableColumn
feL2ModSW24LoopDetectedStateEbl = _FeL2ModSW24LoopDetectedStateEbl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 13, 2, 1, 2),
    _FeL2ModSW24LoopDetectedStateEbl_Type()
)
feL2ModSW24LoopDetectedStateEbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24LoopDetectedStateEbl.setStatus("current")


class _FeL2ModSW24LoopDetectedCurrentStatus_Type(Integer32):
    """Custom type feL2ModSW24LoopDetectedCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24LoopDetectedCurrentStatus_Type.__name__ = "Integer32"
_FeL2ModSW24LoopDetectedCurrentStatus_Object = MibTableColumn
feL2ModSW24LoopDetectedCurrentStatus = _FeL2ModSW24LoopDetectedCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 13, 2, 1, 3),
    _FeL2ModSW24LoopDetectedCurrentStatus_Type()
)
feL2ModSW24LoopDetectedCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24LoopDetectedCurrentStatus.setStatus("current")


class _FeL2ModSW24LoopDetectedResumed_Type(Integer32):
    """Custom type feL2ModSW24LoopDetectedResumed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24LoopDetectedResumed_Type.__name__ = "Integer32"
_FeL2ModSW24LoopDetectedResumed_Object = MibTableColumn
feL2ModSW24LoopDetectedResumed = _FeL2ModSW24LoopDetectedResumed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 13, 2, 1, 4),
    _FeL2ModSW24LoopDetectedResumed_Type()
)
feL2ModSW24LoopDetectedResumed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24LoopDetectedResumed.setStatus("current")


class _FeL2ModSW24LoopDetectedAction_Type(Integer32):
    """Custom type feL2ModSW24LoopDetectedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeL2ModSW24LoopDetectedAction_Type.__name__ = "Integer32"
_FeL2ModSW24LoopDetectedAction_Object = MibScalar
feL2ModSW24LoopDetectedAction = _FeL2ModSW24LoopDetectedAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 13, 3),
    _FeL2ModSW24LoopDetectedAction_Type()
)
feL2ModSW24LoopDetectedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feL2ModSW24LoopDetectedAction.setStatus("current")
_FeL2ModSW24SFPInfo_ObjectIdentity = ObjectIdentity
feL2ModSW24SFPInfo = _FeL2ModSW24SFPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14)
)


class _FeL2ModSW24SFPInfoNumber_Type(Integer32):
    """Custom type feL2ModSW24SFPInfoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24SFPInfoNumber_Type.__name__ = "Integer32"
_FeL2ModSW24SFPInfoNumber_Object = MibScalar
feL2ModSW24SFPInfoNumber = _FeL2ModSW24SFPInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 1),
    _FeL2ModSW24SFPInfoNumber_Type()
)
feL2ModSW24SFPInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPInfoNumber.setStatus("current")
_FeL2ModSW24SFPInfoTable_Object = MibTable
feL2ModSW24SFPInfoTable = _FeL2ModSW24SFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2)
)
if mibBuilder.loadTexts:
    feL2ModSW24SFPInfoTable.setStatus("current")
_FeL2ModSW24SFPInfoEntry_Object = MibTableRow
feL2ModSW24SFPInfoEntry = _FeL2ModSW24SFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1)
)
feL2ModSW24SFPInfoEntry.setIndexNames(
    (0, "PRIVATE-FEL2Mod-SW24-MIB", "feL2ModSW24SFPInfoIndex"),
)
if mibBuilder.loadTexts:
    feL2ModSW24SFPInfoEntry.setStatus("current")


class _FeL2ModSW24SFPInfoIndex_Type(Integer32):
    """Custom type feL2ModSW24SFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeL2ModSW24SFPInfoIndex_Type.__name__ = "Integer32"
_FeL2ModSW24SFPInfoIndex_Object = MibTableColumn
feL2ModSW24SFPInfoIndex = _FeL2ModSW24SFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 1),
    _FeL2ModSW24SFPInfoIndex_Type()
)
feL2ModSW24SFPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPInfoIndex.setStatus("current")
_FeL2ModSW24SFPConnectorType_Type = DisplayString
_FeL2ModSW24SFPConnectorType_Object = MibTableColumn
feL2ModSW24SFPConnectorType = _FeL2ModSW24SFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 2),
    _FeL2ModSW24SFPConnectorType_Type()
)
feL2ModSW24SFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPConnectorType.setStatus("current")
_FeL2ModSW24SFPFiberType_Type = DisplayString
_FeL2ModSW24SFPFiberType_Object = MibTableColumn
feL2ModSW24SFPFiberType = _FeL2ModSW24SFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 3),
    _FeL2ModSW24SFPFiberType_Type()
)
feL2ModSW24SFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPFiberType.setStatus("current")
_FeL2ModSW24SFPWavelength_Type = DisplayString
_FeL2ModSW24SFPWavelength_Object = MibTableColumn
feL2ModSW24SFPWavelength = _FeL2ModSW24SFPWavelength_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 4),
    _FeL2ModSW24SFPWavelength_Type()
)
feL2ModSW24SFPWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPWavelength.setStatus("current")
_FeL2ModSW24SFPBaudRate_Type = DisplayString
_FeL2ModSW24SFPBaudRate_Object = MibTableColumn
feL2ModSW24SFPBaudRate = _FeL2ModSW24SFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 5),
    _FeL2ModSW24SFPBaudRate_Type()
)
feL2ModSW24SFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPBaudRate.setStatus("current")
_FeL2ModSW24SFPVendorOUI_Type = DisplayString
_FeL2ModSW24SFPVendorOUI_Object = MibTableColumn
feL2ModSW24SFPVendorOUI = _FeL2ModSW24SFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 6),
    _FeL2ModSW24SFPVendorOUI_Type()
)
feL2ModSW24SFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPVendorOUI.setStatus("current")
_FeL2ModSW24SFPVendorName_Type = DisplayString
_FeL2ModSW24SFPVendorName_Object = MibTableColumn
feL2ModSW24SFPVendorName = _FeL2ModSW24SFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 7),
    _FeL2ModSW24SFPVendorName_Type()
)
feL2ModSW24SFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPVendorName.setStatus("current")
_FeL2ModSW24SFPVendorPN_Type = DisplayString
_FeL2ModSW24SFPVendorPN_Object = MibTableColumn
feL2ModSW24SFPVendorPN = _FeL2ModSW24SFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 8),
    _FeL2ModSW24SFPVendorPN_Type()
)
feL2ModSW24SFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPVendorPN.setStatus("current")
_FeL2ModSW24SFPVendorRev_Type = DisplayString
_FeL2ModSW24SFPVendorRev_Object = MibTableColumn
feL2ModSW24SFPVendorRev = _FeL2ModSW24SFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 9),
    _FeL2ModSW24SFPVendorRev_Type()
)
feL2ModSW24SFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPVendorRev.setStatus("current")
_FeL2ModSW24SFPVendorSN_Type = DisplayString
_FeL2ModSW24SFPVendorSN_Object = MibTableColumn
feL2ModSW24SFPVendorSN = _FeL2ModSW24SFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 10),
    _FeL2ModSW24SFPVendorSN_Type()
)
feL2ModSW24SFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPVendorSN.setStatus("current")
_FeL2ModSW24SFPDateCode_Type = DisplayString
_FeL2ModSW24SFPDateCode_Object = MibTableColumn
feL2ModSW24SFPDateCode = _FeL2ModSW24SFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 11),
    _FeL2ModSW24SFPDateCode_Type()
)
feL2ModSW24SFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPDateCode.setStatus("current")
_FeL2ModSW24SFPTemperature_Type = DisplayString
_FeL2ModSW24SFPTemperature_Object = MibTableColumn
feL2ModSW24SFPTemperature = _FeL2ModSW24SFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 12),
    _FeL2ModSW24SFPTemperature_Type()
)
feL2ModSW24SFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPTemperature.setStatus("current")
_FeL2ModSW24SFPVcc_Type = DisplayString
_FeL2ModSW24SFPVcc_Object = MibTableColumn
feL2ModSW24SFPVcc = _FeL2ModSW24SFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 13),
    _FeL2ModSW24SFPVcc_Type()
)
feL2ModSW24SFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPVcc.setStatus("current")
_FeL2ModSW24SFPTxBias_Type = DisplayString
_FeL2ModSW24SFPTxBias_Object = MibTableColumn
feL2ModSW24SFPTxBias = _FeL2ModSW24SFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 14),
    _FeL2ModSW24SFPTxBias_Type()
)
feL2ModSW24SFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPTxBias.setStatus("current")
_FeL2ModSW24SFPTxPWR_Type = DisplayString
_FeL2ModSW24SFPTxPWR_Object = MibTableColumn
feL2ModSW24SFPTxPWR = _FeL2ModSW24SFPTxPWR_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 15),
    _FeL2ModSW24SFPTxPWR_Type()
)
feL2ModSW24SFPTxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPTxPWR.setStatus("current")
_FeL2ModSW24SFPRxPWR_Type = DisplayString
_FeL2ModSW24SFPRxPWR_Object = MibTableColumn
feL2ModSW24SFPRxPWR = _FeL2ModSW24SFPRxPWR_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 14, 2, 1, 16),
    _FeL2ModSW24SFPRxPWR_Type()
)
feL2ModSW24SFPRxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feL2ModSW24SFPRxPWR.setStatus("current")
_FeL2ModSW24TrapEntry_ObjectIdentity = ObjectIdentity
feL2ModSW24TrapEntry = _FeL2ModSW24TrapEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20)
)
_FeL2ModSW24TrapVariable_ObjectIdentity = ObjectIdentity
feL2ModSW24TrapVariable = _FeL2ModSW24TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 21)
)
_Username_Type = DisplayString
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 21, 1),
    _Username_Type()
)
username.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    username.setStatus("current")


class _GroupId_Type(Integer32):
    """Custom type groupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_GroupId_Type.__name__ = "Integer32"
_GroupId_Object = MibScalar
groupId = _GroupId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 21, 2),
    _GroupId_Type()
)
groupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupId.setStatus("current")


class _Actorkey_Type(Integer32):
    """Custom type actorkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Actorkey_Type.__name__ = "Integer32"
_Actorkey_Object = MibScalar
actorkey = _Actorkey_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 21, 3),
    _Actorkey_Type()
)
actorkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorkey.setStatus("current")


class _Partnerkey_Type(Integer32):
    """Custom type partnerkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Partnerkey_Type.__name__ = "Integer32"
_Partnerkey_Object = MibScalar
partnerkey = _Partnerkey_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 21, 4),
    _Partnerkey_Type()
)
partnerkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerkey.setStatus("current")
_Uplink_Type = DisplayString
_Uplink_Object = MibScalar
uplink = _Uplink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 21, 5),
    _Uplink_Type()
)
uplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplink.setStatus("current")

# Managed Objects groups


# Notification objects

feL2ModSW24ModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 1)
)
feL2ModSW24ModuleInserted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    feL2ModSW24ModuleInserted.setStatus(
        "current"
    )

feL2ModSW24ModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 2)
)
feL2ModSW24ModuleRemoved.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    feL2ModSW24ModuleRemoved.setStatus(
        "current"
    )

feL2ModSW24LoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 5)
)
feL2ModSW24LoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    feL2ModSW24LoopDetected.setStatus(
        "current"
    )

feL2ModSW24StpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 100)
)
if mibBuilder.loadTexts:
    feL2ModSW24StpStateDisabled.setStatus(
        "current"
    )

feL2ModSW24StpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 101)
)
if mibBuilder.loadTexts:
    feL2ModSW24StpStateEnabled.setStatus(
        "current"
    )

feL2ModSW24StpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 102)
)
feL2ModSW24StpTopologyChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    feL2ModSW24StpTopologyChanged.setStatus(
        "current"
    )

feL2ModSW24LacpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 120)
)
feL2ModSW24LacpStateDisabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-FEL2Mod-SW24-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    feL2ModSW24LacpStateDisabled.setStatus(
        "current"
    )

feL2ModSW24LacpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 121)
)
feL2ModSW24LacpStateEnabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-FEL2Mod-SW24-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    feL2ModSW24LacpStateEnabled.setStatus(
        "current"
    )

feL2ModSW24LacpPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 123)
)
feL2ModSW24LacpPortAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-FEL2Mod-SW24-MIB", "actorkey"),
        ("PRIVATE-FEL2Mod-SW24-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    feL2ModSW24LacpPortAdded.setStatus(
        "current"
    )

feL2ModSW24LacpPortTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 124)
)
feL2ModSW24LacpPortTrunkFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-FEL2Mod-SW24-MIB", "actorkey"),
        ("PRIVATE-FEL2Mod-SW24-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    feL2ModSW24LacpPortTrunkFailure.setStatus(
        "current"
    )

feL2ModSW24GvrpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 140)
)
if mibBuilder.loadTexts:
    feL2ModSW24GvrpStateDisabled.setStatus(
        "current"
    )

feL2ModSW24GvrpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 141)
)
if mibBuilder.loadTexts:
    feL2ModSW24GvrpStateEnabled.setStatus(
        "current"
    )

feL2ModSW24VlanStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 150)
)
if mibBuilder.loadTexts:
    feL2ModSW24VlanStateDisabled.setStatus(
        "current"
    )

feL2ModSW24VlanPortBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 151)
)
if mibBuilder.loadTexts:
    feL2ModSW24VlanPortBaseEnabled.setStatus(
        "current"
    )

feL2ModSW24VlanTagBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 152)
)
if mibBuilder.loadTexts:
    feL2ModSW24VlanTagBaseEnabled.setStatus(
        "current"
    )

feL2ModSW24VlanMetroModeEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 153)
)
feL2ModSW24VlanMetroModeEnabled.setObjects(
    ("PRIVATE-FEL2Mod-SW24-MIB", "uplink")
)
if mibBuilder.loadTexts:
    feL2ModSW24VlanMetroModeEnabled.setStatus(
        "current"
    )

feL2ModSW24VlanDoubleTagEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 154)
)
if mibBuilder.loadTexts:
    feL2ModSW24VlanDoubleTagEnabled.setStatus(
        "current"
    )

feL2ModSW24UserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 200)
)
feL2ModSW24UserLogin.setObjects(
    ("PRIVATE-FEL2Mod-SW24-MIB", "username")
)
if mibBuilder.loadTexts:
    feL2ModSW24UserLogin.setStatus(
        "current"
    )

feL2ModSW24UserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 19, 1, 20, 201)
)
feL2ModSW24UserLogout.setObjects(
    ("PRIVATE-FEL2Mod-SW24-MIB", "username")
)
if mibBuilder.loadTexts:
    feL2ModSW24UserLogout.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRIVATE-FEL2Mod-SW24-MIB",
    **{"privatetech": privatetech,
       "switch": switch,
       "feL2ModSW24ProductID": feL2ModSW24ProductID,
       "feL2ModSW24Produces": feL2ModSW24Produces,
       "feL2ModSW24System": feL2ModSW24System,
       "feL2ModSW24CommonSys": feL2ModSW24CommonSys,
       "feL2ModSW24Reboot": feL2ModSW24Reboot,
       "feL2ModSW24BiosVsersion": feL2ModSW24BiosVsersion,
       "feL2ModSW24FirmwareVersion": feL2ModSW24FirmwareVersion,
       "feL2ModSW24HardwareVersion": feL2ModSW24HardwareVersion,
       "feL2ModSW24MechanicalVersion": feL2ModSW24MechanicalVersion,
       "feL2ModSW24SerialNumber": feL2ModSW24SerialNumber,
       "feL2ModSW24HostMacAddress": feL2ModSW24HostMacAddress,
       "feL2ModSW24DevicePort": feL2ModSW24DevicePort,
       "feL2ModSW24RamSize": feL2ModSW24RamSize,
       "feL2ModSW24FlashSize": feL2ModSW24FlashSize,
       "feL2ModSW24IP": feL2ModSW24IP,
       "feL2ModSW24DhcpSetting": feL2ModSW24DhcpSetting,
       "feL2ModSW24IPAddress": feL2ModSW24IPAddress,
       "feL2ModSW24NetMask": feL2ModSW24NetMask,
       "feL2ModSW24DefaultGateway": feL2ModSW24DefaultGateway,
       "feL2ModSW24DnsSetting": feL2ModSW24DnsSetting,
       "feL2ModSW24DnsServer": feL2ModSW24DnsServer,
       "feL2ModSW24Time": feL2ModSW24Time,
       "feL2ModSW24SystemCurrentTime": feL2ModSW24SystemCurrentTime,
       "feL2ModSW24ManualTimeSetting": feL2ModSW24ManualTimeSetting,
       "feL2ModSW24NTPServer": feL2ModSW24NTPServer,
       "feL2ModSW24NTPTimeZone": feL2ModSW24NTPTimeZone,
       "feL2ModSW24NTPTimeSync": feL2ModSW24NTPTimeSync,
       "feL2ModSW24DaylightSavingTime": feL2ModSW24DaylightSavingTime,
       "feL2ModSW24DaylightStartTime": feL2ModSW24DaylightStartTime,
       "feL2ModSW24DaylightEndTime": feL2ModSW24DaylightEndTime,
       "feL2ModSW24Account": feL2ModSW24Account,
       "feL2ModSW24AccountNumber": feL2ModSW24AccountNumber,
       "feL2ModSW24AccountTable": feL2ModSW24AccountTable,
       "feL2ModSW24AccountEntry": feL2ModSW24AccountEntry,
       "feL2ModSW24AccountIndex": feL2ModSW24AccountIndex,
       "feL2ModSW24AccountAuthorization": feL2ModSW24AccountAuthorization,
       "feL2ModSW24AccountName": feL2ModSW24AccountName,
       "feL2ModSW24AccountPassword": feL2ModSW24AccountPassword,
       "feL2ModSW24AccountAddName": feL2ModSW24AccountAddName,
       "feL2ModSW24AccountAddPassword": feL2ModSW24AccountAddPassword,
       "feL2ModSW24DoAccountAdd": feL2ModSW24DoAccountAdd,
       "feL2ModSW24AccountDel": feL2ModSW24AccountDel,
       "feL2ModSW24Snmp": feL2ModSW24Snmp,
       "feL2ModSW24GetCommunity": feL2ModSW24GetCommunity,
       "feL2ModSW24SetCommunity": feL2ModSW24SetCommunity,
       "feL2ModSW24TrapHostNumber": feL2ModSW24TrapHostNumber,
       "feL2ModSW24TrapHostTable": feL2ModSW24TrapHostTable,
       "feL2ModSW24TrapHostEntry": feL2ModSW24TrapHostEntry,
       "feL2ModSW24TrapHostIndex": feL2ModSW24TrapHostIndex,
       "feL2ModSW24TrapHostIP": feL2ModSW24TrapHostIP,
       "feL2ModSW24TrapHostPort": feL2ModSW24TrapHostPort,
       "feL2ModSW24TrapHostCommunity": feL2ModSW24TrapHostCommunity,
       "feL2ModSW24Alarm": feL2ModSW24Alarm,
       "feL2ModSW24Event": feL2ModSW24Event,
       "feL2ModSW24EventNumber": feL2ModSW24EventNumber,
       "feL2ModSW24EventTable": feL2ModSW24EventTable,
       "feL2ModSW24EventEntry": feL2ModSW24EventEntry,
       "feL2ModSW24EventIndex": feL2ModSW24EventIndex,
       "feL2ModSW24EventName": feL2ModSW24EventName,
       "feL2ModSW24EventSendEmail": feL2ModSW24EventSendEmail,
       "feL2ModSW24EventSendSMS": feL2ModSW24EventSendSMS,
       "feL2ModSW24EventSendTrap": feL2ModSW24EventSendTrap,
       "feL2ModSW24Email": feL2ModSW24Email,
       "feL2ModSW24EmailServer": feL2ModSW24EmailServer,
       "feL2ModSW24EmailUsername": feL2ModSW24EmailUsername,
       "feL2ModSW24EmailPassword": feL2ModSW24EmailPassword,
       "feL2ModSW24EmailUserNumber": feL2ModSW24EmailUserNumber,
       "feL2ModSW24EmailUserTable": feL2ModSW24EmailUserTable,
       "feL2ModSW24EmailUserEntry": feL2ModSW24EmailUserEntry,
       "feL2ModSW24EmailUserIndex": feL2ModSW24EmailUserIndex,
       "feL2ModSW24EmailUserAddress": feL2ModSW24EmailUserAddress,
       "feL2ModSW24SMS": feL2ModSW24SMS,
       "feL2ModSW24SMSServer": feL2ModSW24SMSServer,
       "feL2ModSW24SMSUsername": feL2ModSW24SMSUsername,
       "feL2ModSW24SMSPassword": feL2ModSW24SMSPassword,
       "feL2ModSW24SMSUserNumber": feL2ModSW24SMSUserNumber,
       "feL2ModSW24SMSUserTable": feL2ModSW24SMSUserTable,
       "feL2ModSW24SMSUserEntry": feL2ModSW24SMSUserEntry,
       "feL2ModSW24SMSUserIndex": feL2ModSW24SMSUserIndex,
       "feL2ModSW24SMSUserMobilePhone": feL2ModSW24SMSUserMobilePhone,
       "feL2ModSW24Tftp": feL2ModSW24Tftp,
       "feL2ModSW24TftpServer": feL2ModSW24TftpServer,
       "feL2ModSW24Configuration": feL2ModSW24Configuration,
       "feL2ModSW24SaveRestore": feL2ModSW24SaveRestore,
       "feL2ModSW24SaveStart": feL2ModSW24SaveStart,
       "feL2ModSW24SaveUser": feL2ModSW24SaveUser,
       "feL2ModSW24RestoreDefault": feL2ModSW24RestoreDefault,
       "feL2ModSW24RestoreUser": feL2ModSW24RestoreUser,
       "feL2ModSW24ConfigFile": feL2ModSW24ConfigFile,
       "feL2ModSW24ExportConfigName": feL2ModSW24ExportConfigName,
       "feL2ModSW24DoExportConfig": feL2ModSW24DoExportConfig,
       "feL2ModSW24ImportConfigName": feL2ModSW24ImportConfigName,
       "feL2ModSW24DoImportConfig": feL2ModSW24DoImportConfig,
       "feL2ModSW24Diagnostic": feL2ModSW24Diagnostic,
       "feL2ModSW24EEPROMTest": feL2ModSW24EEPROMTest,
       "feL2ModSW24UartTest": feL2ModSW24UartTest,
       "feL2ModSW24DramTest": feL2ModSW24DramTest,
       "feL2ModSW24FlashTest": feL2ModSW24FlashTest,
       "feL2ModSW24InternalLoopbackTest": feL2ModSW24InternalLoopbackTest,
       "feL2ModSW24ExternalLoopbackTest": feL2ModSW24ExternalLoopbackTest,
       "feL2ModSW24PingTest": feL2ModSW24PingTest,
       "feL2ModSW24Log": feL2ModSW24Log,
       "feL2ModSW24ClearLog": feL2ModSW24ClearLog,
       "feL2ModSW24UploadLog": feL2ModSW24UploadLog,
       "feL2ModSW24AutoUploadLogState": feL2ModSW24AutoUploadLogState,
       "feL2ModSW24LogNumber": feL2ModSW24LogNumber,
       "feL2ModSW24LogTable": feL2ModSW24LogTable,
       "feL2ModSW24LogEntry": feL2ModSW24LogEntry,
       "feL2ModSW24LogIndex": feL2ModSW24LogIndex,
       "feL2ModSW24LogEvent": feL2ModSW24LogEvent,
       "feL2ModSW24Firmware": feL2ModSW24Firmware,
       "feL2ModSW24FirmwareFileName": feL2ModSW24FirmwareFileName,
       "feL2ModSW24DoFirmwareUpgrade": feL2ModSW24DoFirmwareUpgrade,
       "feL2ModSW24Port": feL2ModSW24Port,
       "feL2ModSW24PortStatus": feL2ModSW24PortStatus,
       "feL2ModSW24PortStatusNumber": feL2ModSW24PortStatusNumber,
       "feL2ModSW24PortStatusTable": feL2ModSW24PortStatusTable,
       "feL2ModSW24PortStatusEntry": feL2ModSW24PortStatusEntry,
       "feL2ModSW24PortStatusIndex": feL2ModSW24PortStatusIndex,
       "feL2ModSW24PortStatusMedia": feL2ModSW24PortStatusMedia,
       "feL2ModSW24PortStatusLink": feL2ModSW24PortStatusLink,
       "feL2ModSW24PortStatusPortState": feL2ModSW24PortStatusPortState,
       "feL2ModSW24PortStatusAutoNego": feL2ModSW24PortStatusAutoNego,
       "feL2ModSW24PortStatusSpdDpx": feL2ModSW24PortStatusSpdDpx,
       "feL2ModSW24PortStatusFlwCtrl": feL2ModSW24PortStatusFlwCtrl,
       "feL2ModSW24PortStatuDescription": feL2ModSW24PortStatuDescription,
       "feL2ModSW24PortConf": feL2ModSW24PortConf,
       "feL2ModSW24PortConfNumber": feL2ModSW24PortConfNumber,
       "feL2ModSW24PortConfTable": feL2ModSW24PortConfTable,
       "feL2ModSW24PortConfEntry": feL2ModSW24PortConfEntry,
       "feL2ModSW24PortConfIndex": feL2ModSW24PortConfIndex,
       "feL2ModSW24PortConfPortState": feL2ModSW24PortConfPortState,
       "feL2ModSW24PortConfSpdDpx": feL2ModSW24PortConfSpdDpx,
       "feL2ModSW24PortConfFlwCtrl": feL2ModSW24PortConfFlwCtrl,
       "feL2ModSW24PortConfDescription": feL2ModSW24PortConfDescription,
       "feL2ModSW24Mirror": feL2ModSW24Mirror,
       "feL2ModSW24MirrorMode": feL2ModSW24MirrorMode,
       "feL2ModSW24MirroringPort": feL2ModSW24MirroringPort,
       "feL2ModSW24MirroredPorts": feL2ModSW24MirroredPorts,
       "feL2ModSW24MaxPktLen": feL2ModSW24MaxPktLen,
       "feL2ModSW24MaxPktLen1": feL2ModSW24MaxPktLen1,
       "feL2ModSW24MaxPktLenPortNumber": feL2ModSW24MaxPktLenPortNumber,
       "feL2ModSW24MaxPktLenConfTable": feL2ModSW24MaxPktLenConfTable,
       "feL2ModSW24MaxPktLenConfEntry": feL2ModSW24MaxPktLenConfEntry,
       "feL2ModSW24MaxPktLenConfIndex": feL2ModSW24MaxPktLenConfIndex,
       "feL2ModSW24MaxPktLenConfSetting": feL2ModSW24MaxPktLenConfSetting,
       "feL2ModSW24Bandwidth": feL2ModSW24Bandwidth,
       "feL2ModSW24Bandwidth1": feL2ModSW24Bandwidth1,
       "feL2ModSW24BandwidthPortNumber": feL2ModSW24BandwidthPortNumber,
       "feL2ModSW24BandwidthConfTable": feL2ModSW24BandwidthConfTable,
       "feL2ModSW24BandwidthConfEntry": feL2ModSW24BandwidthConfEntry,
       "feL2ModSW24BandwidthConfIndex": feL2ModSW24BandwidthConfIndex,
       "feL2ModSW24BandwidthConfIngressState": feL2ModSW24BandwidthConfIngressState,
       "feL2ModSW24BandwidthConfIngressBW": feL2ModSW24BandwidthConfIngressBW,
       "feL2ModSW24BandwidthConfStormState": feL2ModSW24BandwidthConfStormState,
       "feL2ModSW24BandwidthConfStormBW": feL2ModSW24BandwidthConfStormBW,
       "feL2ModSW24BandwidthConfEgressState": feL2ModSW24BandwidthConfEgressState,
       "feL2ModSW24BandwidthConfEgressBW": feL2ModSW24BandwidthConfEgressBW,
       "feL2ModSW24LoopDetectedConf": feL2ModSW24LoopDetectedConf,
       "feL2ModSW24LoopDetectedNumber": feL2ModSW24LoopDetectedNumber,
       "feL2ModSW24LoopDetectedTable": feL2ModSW24LoopDetectedTable,
       "feL2ModSW24LoopDetectedEntry": feL2ModSW24LoopDetectedEntry,
       "feL2ModSW24LoopDetectedfIndex": feL2ModSW24LoopDetectedfIndex,
       "feL2ModSW24LoopDetectedStateEbl": feL2ModSW24LoopDetectedStateEbl,
       "feL2ModSW24LoopDetectedCurrentStatus": feL2ModSW24LoopDetectedCurrentStatus,
       "feL2ModSW24LoopDetectedResumed": feL2ModSW24LoopDetectedResumed,
       "feL2ModSW24LoopDetectedAction": feL2ModSW24LoopDetectedAction,
       "feL2ModSW24SFPInfo": feL2ModSW24SFPInfo,
       "feL2ModSW24SFPInfoNumber": feL2ModSW24SFPInfoNumber,
       "feL2ModSW24SFPInfoTable": feL2ModSW24SFPInfoTable,
       "feL2ModSW24SFPInfoEntry": feL2ModSW24SFPInfoEntry,
       "feL2ModSW24SFPInfoIndex": feL2ModSW24SFPInfoIndex,
       "feL2ModSW24SFPConnectorType": feL2ModSW24SFPConnectorType,
       "feL2ModSW24SFPFiberType": feL2ModSW24SFPFiberType,
       "feL2ModSW24SFPWavelength": feL2ModSW24SFPWavelength,
       "feL2ModSW24SFPBaudRate": feL2ModSW24SFPBaudRate,
       "feL2ModSW24SFPVendorOUI": feL2ModSW24SFPVendorOUI,
       "feL2ModSW24SFPVendorName": feL2ModSW24SFPVendorName,
       "feL2ModSW24SFPVendorPN": feL2ModSW24SFPVendorPN,
       "feL2ModSW24SFPVendorRev": feL2ModSW24SFPVendorRev,
       "feL2ModSW24SFPVendorSN": feL2ModSW24SFPVendorSN,
       "feL2ModSW24SFPDateCode": feL2ModSW24SFPDateCode,
       "feL2ModSW24SFPTemperature": feL2ModSW24SFPTemperature,
       "feL2ModSW24SFPVcc": feL2ModSW24SFPVcc,
       "feL2ModSW24SFPTxBias": feL2ModSW24SFPTxBias,
       "feL2ModSW24SFPTxPWR": feL2ModSW24SFPTxPWR,
       "feL2ModSW24SFPRxPWR": feL2ModSW24SFPRxPWR,
       "feL2ModSW24TrapEntry": feL2ModSW24TrapEntry,
       "feL2ModSW24ModuleInserted": feL2ModSW24ModuleInserted,
       "feL2ModSW24ModuleRemoved": feL2ModSW24ModuleRemoved,
       "feL2ModSW24LoopDetected": feL2ModSW24LoopDetected,
       "feL2ModSW24StpStateDisabled": feL2ModSW24StpStateDisabled,
       "feL2ModSW24StpStateEnabled": feL2ModSW24StpStateEnabled,
       "feL2ModSW24StpTopologyChanged": feL2ModSW24StpTopologyChanged,
       "feL2ModSW24LacpStateDisabled": feL2ModSW24LacpStateDisabled,
       "feL2ModSW24LacpStateEnabled": feL2ModSW24LacpStateEnabled,
       "feL2ModSW24LacpPortAdded": feL2ModSW24LacpPortAdded,
       "feL2ModSW24LacpPortTrunkFailure": feL2ModSW24LacpPortTrunkFailure,
       "feL2ModSW24GvrpStateDisabled": feL2ModSW24GvrpStateDisabled,
       "feL2ModSW24GvrpStateEnabled": feL2ModSW24GvrpStateEnabled,
       "feL2ModSW24VlanStateDisabled": feL2ModSW24VlanStateDisabled,
       "feL2ModSW24VlanPortBaseEnabled": feL2ModSW24VlanPortBaseEnabled,
       "feL2ModSW24VlanTagBaseEnabled": feL2ModSW24VlanTagBaseEnabled,
       "feL2ModSW24VlanMetroModeEnabled": feL2ModSW24VlanMetroModeEnabled,
       "feL2ModSW24VlanDoubleTagEnabled": feL2ModSW24VlanDoubleTagEnabled,
       "feL2ModSW24UserLogin": feL2ModSW24UserLogin,
       "feL2ModSW24UserLogout": feL2ModSW24UserLogout,
       "feL2ModSW24TrapVariable": feL2ModSW24TrapVariable,
       "username": username,
       "groupId": groupId,
       "actorkey": actorkey,
       "partnerkey": partnerkey,
       "uplink": uplink}
)
