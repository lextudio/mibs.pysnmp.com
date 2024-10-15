# SNMP MIB module (SIGNAMAX-SW0657851-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SIGNAMAX-SW0657851-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:19 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

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

signamax = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5205)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2)
)
_Sw0657851ProductID_ObjectIdentity = ObjectIdentity
sw0657851ProductID = _Sw0657851ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34)
)
_Sw0657851Produces_ObjectIdentity = ObjectIdentity
sw0657851Produces = _Sw0657851Produces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1)
)
_Sw0657851System_ObjectIdentity = ObjectIdentity
sw0657851System = _Sw0657851System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1)
)
_Sw0657851CommonSys_ObjectIdentity = ObjectIdentity
sw0657851CommonSys = _Sw0657851CommonSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1)
)


class _Sw0657851Reboot_Type(Integer32):
    """Custom type sw0657851Reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Sw0657851Reboot_Type.__name__ = "Integer32"
_Sw0657851Reboot_Object = MibScalar
sw0657851Reboot = _Sw0657851Reboot_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 1),
    _Sw0657851Reboot_Type()
)
sw0657851Reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Reboot.setStatus("current")
_Sw0657851BiosVsersion_Type = DisplayString
_Sw0657851BiosVsersion_Object = MibScalar
sw0657851BiosVsersion = _Sw0657851BiosVsersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 2),
    _Sw0657851BiosVsersion_Type()
)
sw0657851BiosVsersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851BiosVsersion.setStatus("current")
_Sw0657851FirmwareVersion_Type = DisplayString
_Sw0657851FirmwareVersion_Object = MibScalar
sw0657851FirmwareVersion = _Sw0657851FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 3),
    _Sw0657851FirmwareVersion_Type()
)
sw0657851FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851FirmwareVersion.setStatus("current")
_Sw0657851HardwareVersion_Type = DisplayString
_Sw0657851HardwareVersion_Object = MibScalar
sw0657851HardwareVersion = _Sw0657851HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 4),
    _Sw0657851HardwareVersion_Type()
)
sw0657851HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851HardwareVersion.setStatus("current")
_Sw0657851MechanicalVersion_Type = DisplayString
_Sw0657851MechanicalVersion_Object = MibScalar
sw0657851MechanicalVersion = _Sw0657851MechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 5),
    _Sw0657851MechanicalVersion_Type()
)
sw0657851MechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851MechanicalVersion.setStatus("current")
_Sw0657851SerialNumber_Type = DisplayString
_Sw0657851SerialNumber_Object = MibScalar
sw0657851SerialNumber = _Sw0657851SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 6),
    _Sw0657851SerialNumber_Type()
)
sw0657851SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SerialNumber.setStatus("current")
_Sw0657851HostMacAddress_Type = DisplayString
_Sw0657851HostMacAddress_Object = MibScalar
sw0657851HostMacAddress = _Sw0657851HostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 7),
    _Sw0657851HostMacAddress_Type()
)
sw0657851HostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851HostMacAddress.setStatus("current")
_Sw0657851DevicePort_Type = DisplayString
_Sw0657851DevicePort_Object = MibScalar
sw0657851DevicePort = _Sw0657851DevicePort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 8),
    _Sw0657851DevicePort_Type()
)
sw0657851DevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851DevicePort.setStatus("current")
_Sw0657851RamSize_Type = DisplayString
_Sw0657851RamSize_Object = MibScalar
sw0657851RamSize = _Sw0657851RamSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 9),
    _Sw0657851RamSize_Type()
)
sw0657851RamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851RamSize.setStatus("current")
_Sw0657851FlashSize_Type = DisplayString
_Sw0657851FlashSize_Object = MibScalar
sw0657851FlashSize = _Sw0657851FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 10),
    _Sw0657851FlashSize_Type()
)
sw0657851FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851FlashSize.setStatus("current")
_Sw0657851DeviceName_Type = DisplayString
_Sw0657851DeviceName_Object = MibScalar
sw0657851DeviceName = _Sw0657851DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 11),
    _Sw0657851DeviceName_Type()
)
sw0657851DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DeviceName.setStatus("current")
_Sw0657851SystemDescription_Type = DisplayString
_Sw0657851SystemDescription_Object = MibScalar
sw0657851SystemDescription = _Sw0657851SystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 1, 12),
    _Sw0657851SystemDescription_Type()
)
sw0657851SystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SystemDescription.setStatus("current")
_Sw0657851IP_ObjectIdentity = ObjectIdentity
sw0657851IP = _Sw0657851IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 2)
)


class _Sw0657851DhcpSetting_Type(Integer32):
    """Custom type sw0657851DhcpSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851DhcpSetting_Type.__name__ = "Integer32"
_Sw0657851DhcpSetting_Object = MibScalar
sw0657851DhcpSetting = _Sw0657851DhcpSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 2, 1),
    _Sw0657851DhcpSetting_Type()
)
sw0657851DhcpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DhcpSetting.setStatus("current")
_Sw0657851IPAddress_Type = IpAddress
_Sw0657851IPAddress_Object = MibScalar
sw0657851IPAddress = _Sw0657851IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 2, 2),
    _Sw0657851IPAddress_Type()
)
sw0657851IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IPAddress.setStatus("current")
_Sw0657851NetMask_Type = IpAddress
_Sw0657851NetMask_Object = MibScalar
sw0657851NetMask = _Sw0657851NetMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 2, 3),
    _Sw0657851NetMask_Type()
)
sw0657851NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851NetMask.setStatus("current")
_Sw0657851DefaultGateway_Type = IpAddress
_Sw0657851DefaultGateway_Object = MibScalar
sw0657851DefaultGateway = _Sw0657851DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 2, 4),
    _Sw0657851DefaultGateway_Type()
)
sw0657851DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DefaultGateway.setStatus("current")


class _Sw0657851DnsSetting_Type(Integer32):
    """Custom type sw0657851DnsSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851DnsSetting_Type.__name__ = "Integer32"
_Sw0657851DnsSetting_Object = MibScalar
sw0657851DnsSetting = _Sw0657851DnsSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 2, 5),
    _Sw0657851DnsSetting_Type()
)
sw0657851DnsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DnsSetting.setStatus("current")
_Sw0657851DnsServer_Type = IpAddress
_Sw0657851DnsServer_Object = MibScalar
sw0657851DnsServer = _Sw0657851DnsServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 2, 6),
    _Sw0657851DnsServer_Type()
)
sw0657851DnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DnsServer.setStatus("current")
_Sw0657851Time_ObjectIdentity = ObjectIdentity
sw0657851Time = _Sw0657851Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 3)
)
_Sw0657851SystemCurrentTime_Type = DisplayString
_Sw0657851SystemCurrentTime_Object = MibScalar
sw0657851SystemCurrentTime = _Sw0657851SystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 3, 1),
    _Sw0657851SystemCurrentTime_Type()
)
sw0657851SystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SystemCurrentTime.setStatus("current")
_Sw0657851ManualTimeSetting_Type = DisplayString
_Sw0657851ManualTimeSetting_Object = MibScalar
sw0657851ManualTimeSetting = _Sw0657851ManualTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 3, 2),
    _Sw0657851ManualTimeSetting_Type()
)
sw0657851ManualTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ManualTimeSetting.setStatus("current")
_Sw0657851NTPServer_Type = DisplayString
_Sw0657851NTPServer_Object = MibScalar
sw0657851NTPServer = _Sw0657851NTPServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 3, 3),
    _Sw0657851NTPServer_Type()
)
sw0657851NTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851NTPServer.setStatus("current")


class _Sw0657851NTPTimeZone_Type(Integer32):
    """Custom type sw0657851NTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_Sw0657851NTPTimeZone_Type.__name__ = "Integer32"
_Sw0657851NTPTimeZone_Object = MibScalar
sw0657851NTPTimeZone = _Sw0657851NTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 3, 4),
    _Sw0657851NTPTimeZone_Type()
)
sw0657851NTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851NTPTimeZone.setStatus("current")


class _Sw0657851NTPTimeSync_Type(Integer32):
    """Custom type sw0657851NTPTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851NTPTimeSync_Type.__name__ = "Integer32"
_Sw0657851NTPTimeSync_Object = MibScalar
sw0657851NTPTimeSync = _Sw0657851NTPTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 3, 5),
    _Sw0657851NTPTimeSync_Type()
)
sw0657851NTPTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851NTPTimeSync.setStatus("current")


class _Sw0657851DaylightSavingTime_Type(Integer32):
    """Custom type sw0657851DaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_Sw0657851DaylightSavingTime_Type.__name__ = "Integer32"
_Sw0657851DaylightSavingTime_Object = MibScalar
sw0657851DaylightSavingTime = _Sw0657851DaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 3, 6),
    _Sw0657851DaylightSavingTime_Type()
)
sw0657851DaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DaylightSavingTime.setStatus("current")
_Sw0657851DaylightStartTime_Type = DisplayString
_Sw0657851DaylightStartTime_Object = MibScalar
sw0657851DaylightStartTime = _Sw0657851DaylightStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 3, 7),
    _Sw0657851DaylightStartTime_Type()
)
sw0657851DaylightStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DaylightStartTime.setStatus("current")
_Sw0657851DaylightEndTime_Type = DisplayString
_Sw0657851DaylightEndTime_Object = MibScalar
sw0657851DaylightEndTime = _Sw0657851DaylightEndTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 3, 8),
    _Sw0657851DaylightEndTime_Type()
)
sw0657851DaylightEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DaylightEndTime.setStatus("current")
_Sw0657851Account_ObjectIdentity = ObjectIdentity
sw0657851Account = _Sw0657851Account_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4)
)


class _Sw0657851AccountNumber_Type(Integer32):
    """Custom type sw0657851AccountNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Sw0657851AccountNumber_Type.__name__ = "Integer32"
_Sw0657851AccountNumber_Object = MibScalar
sw0657851AccountNumber = _Sw0657851AccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4, 1),
    _Sw0657851AccountNumber_Type()
)
sw0657851AccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851AccountNumber.setStatus("current")
_Sw0657851AccountTable_Object = MibTable
sw0657851AccountTable = _Sw0657851AccountTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sw0657851AccountTable.setStatus("current")
_Sw0657851AccountEntry_Object = MibTableRow
sw0657851AccountEntry = _Sw0657851AccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4, 2, 1)
)
sw0657851AccountEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851AccountIndex"),
)
if mibBuilder.loadTexts:
    sw0657851AccountEntry.setStatus("current")


class _Sw0657851AccountIndex_Type(Integer32):
    """Custom type sw0657851AccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Sw0657851AccountIndex_Type.__name__ = "Integer32"
_Sw0657851AccountIndex_Object = MibTableColumn
sw0657851AccountIndex = _Sw0657851AccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4, 2, 1, 1),
    _Sw0657851AccountIndex_Type()
)
sw0657851AccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851AccountIndex.setStatus("current")
_Sw0657851AccountAuthorization_Type = DisplayString
_Sw0657851AccountAuthorization_Object = MibTableColumn
sw0657851AccountAuthorization = _Sw0657851AccountAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4, 2, 1, 2),
    _Sw0657851AccountAuthorization_Type()
)
sw0657851AccountAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851AccountAuthorization.setStatus("current")
_Sw0657851AccountName_Type = DisplayString
_Sw0657851AccountName_Object = MibTableColumn
sw0657851AccountName = _Sw0657851AccountName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4, 2, 1, 3),
    _Sw0657851AccountName_Type()
)
sw0657851AccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AccountName.setStatus("current")
_Sw0657851AccountPassword_Type = DisplayString
_Sw0657851AccountPassword_Object = MibTableColumn
sw0657851AccountPassword = _Sw0657851AccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4, 2, 1, 4),
    _Sw0657851AccountPassword_Type()
)
sw0657851AccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AccountPassword.setStatus("current")
_Sw0657851AccountAddName_Type = DisplayString
_Sw0657851AccountAddName_Object = MibScalar
sw0657851AccountAddName = _Sw0657851AccountAddName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4, 3),
    _Sw0657851AccountAddName_Type()
)
sw0657851AccountAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AccountAddName.setStatus("current")
_Sw0657851AccountAddPassword_Type = DisplayString
_Sw0657851AccountAddPassword_Object = MibScalar
sw0657851AccountAddPassword = _Sw0657851AccountAddPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4, 4),
    _Sw0657851AccountAddPassword_Type()
)
sw0657851AccountAddPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AccountAddPassword.setStatus("current")


class _Sw0657851DoAccountAdd_Type(Integer32):
    """Custom type sw0657851DoAccountAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851DoAccountAdd_Type.__name__ = "Integer32"
_Sw0657851DoAccountAdd_Object = MibScalar
sw0657851DoAccountAdd = _Sw0657851DoAccountAdd_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4, 5),
    _Sw0657851DoAccountAdd_Type()
)
sw0657851DoAccountAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DoAccountAdd.setStatus("current")


class _Sw0657851AccountDel_Type(Integer32):
    """Custom type sw0657851AccountDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_Sw0657851AccountDel_Type.__name__ = "Integer32"
_Sw0657851AccountDel_Object = MibScalar
sw0657851AccountDel = _Sw0657851AccountDel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 1, 4, 6),
    _Sw0657851AccountDel_Type()
)
sw0657851AccountDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AccountDel.setStatus("current")
_Sw0657851Snmp_ObjectIdentity = ObjectIdentity
sw0657851Snmp = _Sw0657851Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 2)
)
_Sw0657851GetCommunity_Type = DisplayString
_Sw0657851GetCommunity_Object = MibScalar
sw0657851GetCommunity = _Sw0657851GetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 2, 1),
    _Sw0657851GetCommunity_Type()
)
sw0657851GetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851GetCommunity.setStatus("current")
_Sw0657851SetCommunity_Type = DisplayString
_Sw0657851SetCommunity_Object = MibScalar
sw0657851SetCommunity = _Sw0657851SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 2, 2),
    _Sw0657851SetCommunity_Type()
)
sw0657851SetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851SetCommunity.setStatus("current")


class _Sw0657851TrapHostNumber_Type(Integer32):
    """Custom type sw0657851TrapHostNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sw0657851TrapHostNumber_Type.__name__ = "Integer32"
_Sw0657851TrapHostNumber_Object = MibScalar
sw0657851TrapHostNumber = _Sw0657851TrapHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 2, 3),
    _Sw0657851TrapHostNumber_Type()
)
sw0657851TrapHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851TrapHostNumber.setStatus("current")
_Sw0657851TrapHostTable_Object = MibTable
sw0657851TrapHostTable = _Sw0657851TrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 2, 4)
)
if mibBuilder.loadTexts:
    sw0657851TrapHostTable.setStatus("current")
_Sw0657851TrapHostEntry_Object = MibTableRow
sw0657851TrapHostEntry = _Sw0657851TrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 2, 4, 1)
)
sw0657851TrapHostEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851TrapHostIndex"),
)
if mibBuilder.loadTexts:
    sw0657851TrapHostEntry.setStatus("current")


class _Sw0657851TrapHostIndex_Type(Integer32):
    """Custom type sw0657851TrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sw0657851TrapHostIndex_Type.__name__ = "Integer32"
_Sw0657851TrapHostIndex_Object = MibTableColumn
sw0657851TrapHostIndex = _Sw0657851TrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 2, 4, 1, 1),
    _Sw0657851TrapHostIndex_Type()
)
sw0657851TrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851TrapHostIndex.setStatus("current")
_Sw0657851TrapHostIP_Type = IpAddress
_Sw0657851TrapHostIP_Object = MibTableColumn
sw0657851TrapHostIP = _Sw0657851TrapHostIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 2, 4, 1, 2),
    _Sw0657851TrapHostIP_Type()
)
sw0657851TrapHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TrapHostIP.setStatus("current")


class _Sw0657851TrapHostPort_Type(Integer32):
    """Custom type sw0657851TrapHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Sw0657851TrapHostPort_Type.__name__ = "Integer32"
_Sw0657851TrapHostPort_Object = MibTableColumn
sw0657851TrapHostPort = _Sw0657851TrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 2, 4, 1, 3),
    _Sw0657851TrapHostPort_Type()
)
sw0657851TrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TrapHostPort.setStatus("current")
_Sw0657851TrapHostCommunity_Type = DisplayString
_Sw0657851TrapHostCommunity_Object = MibTableColumn
sw0657851TrapHostCommunity = _Sw0657851TrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 2, 4, 1, 4),
    _Sw0657851TrapHostCommunity_Type()
)
sw0657851TrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TrapHostCommunity.setStatus("current")
_Sw0657851Alarm_ObjectIdentity = ObjectIdentity
sw0657851Alarm = _Sw0657851Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3)
)
_Sw0657851Event_ObjectIdentity = ObjectIdentity
sw0657851Event = _Sw0657851Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 1)
)


class _Sw0657851EventNumber_Type(Integer32):
    """Custom type sw0657851EventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657851EventNumber_Type.__name__ = "Integer32"
_Sw0657851EventNumber_Object = MibScalar
sw0657851EventNumber = _Sw0657851EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 1, 1),
    _Sw0657851EventNumber_Type()
)
sw0657851EventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851EventNumber.setStatus("current")
_Sw0657851EventTable_Object = MibTable
sw0657851EventTable = _Sw0657851EventTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sw0657851EventTable.setStatus("current")
_Sw0657851EventEntry_Object = MibTableRow
sw0657851EventEntry = _Sw0657851EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 1, 2, 1)
)
sw0657851EventEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851EventIndex"),
)
if mibBuilder.loadTexts:
    sw0657851EventEntry.setStatus("current")


class _Sw0657851EventIndex_Type(Integer32):
    """Custom type sw0657851EventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657851EventIndex_Type.__name__ = "Integer32"
_Sw0657851EventIndex_Object = MibTableColumn
sw0657851EventIndex = _Sw0657851EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 1, 2, 1, 1),
    _Sw0657851EventIndex_Type()
)
sw0657851EventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851EventIndex.setStatus("current")
_Sw0657851EventName_Type = DisplayString
_Sw0657851EventName_Object = MibTableColumn
sw0657851EventName = _Sw0657851EventName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 1, 2, 1, 2),
    _Sw0657851EventName_Type()
)
sw0657851EventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851EventName.setStatus("current")


class _Sw0657851EventSendEmail_Type(Integer32):
    """Custom type sw0657851EventSendEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851EventSendEmail_Type.__name__ = "Integer32"
_Sw0657851EventSendEmail_Object = MibTableColumn
sw0657851EventSendEmail = _Sw0657851EventSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 1, 2, 1, 3),
    _Sw0657851EventSendEmail_Type()
)
sw0657851EventSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851EventSendEmail.setStatus("current")


class _Sw0657851EventSendTrap_Type(Integer32):
    """Custom type sw0657851EventSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851EventSendTrap_Type.__name__ = "Integer32"
_Sw0657851EventSendTrap_Object = MibTableColumn
sw0657851EventSendTrap = _Sw0657851EventSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 1, 2, 1, 4),
    _Sw0657851EventSendTrap_Type()
)
sw0657851EventSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851EventSendTrap.setStatus("current")
_Sw0657851Email_ObjectIdentity = ObjectIdentity
sw0657851Email = _Sw0657851Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 2)
)
_Sw0657851EmailServer_Type = DisplayString
_Sw0657851EmailServer_Object = MibScalar
sw0657851EmailServer = _Sw0657851EmailServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 2, 1),
    _Sw0657851EmailServer_Type()
)
sw0657851EmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851EmailServer.setStatus("current")
_Sw0657851EmailUsername_Type = DisplayString
_Sw0657851EmailUsername_Object = MibScalar
sw0657851EmailUsername = _Sw0657851EmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 2, 2),
    _Sw0657851EmailUsername_Type()
)
sw0657851EmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851EmailUsername.setStatus("current")
_Sw0657851EmailPassword_Type = DisplayString
_Sw0657851EmailPassword_Object = MibScalar
sw0657851EmailPassword = _Sw0657851EmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 2, 3),
    _Sw0657851EmailPassword_Type()
)
sw0657851EmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851EmailPassword.setStatus("current")


class _Sw0657851EmailUserNumber_Type(Integer32):
    """Custom type sw0657851EmailUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sw0657851EmailUserNumber_Type.__name__ = "Integer32"
_Sw0657851EmailUserNumber_Object = MibScalar
sw0657851EmailUserNumber = _Sw0657851EmailUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 2, 4),
    _Sw0657851EmailUserNumber_Type()
)
sw0657851EmailUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851EmailUserNumber.setStatus("current")
_Sw0657851EmailUserTable_Object = MibTable
sw0657851EmailUserTable = _Sw0657851EmailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    sw0657851EmailUserTable.setStatus("current")
_Sw0657851EmailUserEntry_Object = MibTableRow
sw0657851EmailUserEntry = _Sw0657851EmailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 2, 5, 1)
)
sw0657851EmailUserEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851EmailUserIndex"),
)
if mibBuilder.loadTexts:
    sw0657851EmailUserEntry.setStatus("current")


class _Sw0657851EmailUserIndex_Type(Integer32):
    """Custom type sw0657851EmailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sw0657851EmailUserIndex_Type.__name__ = "Integer32"
_Sw0657851EmailUserIndex_Object = MibTableColumn
sw0657851EmailUserIndex = _Sw0657851EmailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 2, 5, 1, 1),
    _Sw0657851EmailUserIndex_Type()
)
sw0657851EmailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851EmailUserIndex.setStatus("current")
_Sw0657851EmailUserAddress_Type = DisplayString
_Sw0657851EmailUserAddress_Object = MibTableColumn
sw0657851EmailUserAddress = _Sw0657851EmailUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 3, 2, 5, 1, 2),
    _Sw0657851EmailUserAddress_Type()
)
sw0657851EmailUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851EmailUserAddress.setStatus("current")
_Sw0657851Configuration_ObjectIdentity = ObjectIdentity
sw0657851Configuration = _Sw0657851Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5)
)
_Sw0657851SaveRestore_ObjectIdentity = ObjectIdentity
sw0657851SaveRestore = _Sw0657851SaveRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5, 1)
)


class _Sw0657851SaveStart_Type(Integer32):
    """Custom type sw0657851SaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851SaveStart_Type.__name__ = "Integer32"
_Sw0657851SaveStart_Object = MibScalar
sw0657851SaveStart = _Sw0657851SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5, 1, 1),
    _Sw0657851SaveStart_Type()
)
sw0657851SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851SaveStart.setStatus("current")


class _Sw0657851SaveUser_Type(Integer32):
    """Custom type sw0657851SaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851SaveUser_Type.__name__ = "Integer32"
_Sw0657851SaveUser_Object = MibScalar
sw0657851SaveUser = _Sw0657851SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5, 1, 2),
    _Sw0657851SaveUser_Type()
)
sw0657851SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851SaveUser.setStatus("current")


class _Sw0657851RestoreDefault_Type(Integer32):
    """Custom type sw0657851RestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Sw0657851RestoreDefault_Type.__name__ = "Integer32"
_Sw0657851RestoreDefault_Object = MibScalar
sw0657851RestoreDefault = _Sw0657851RestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5, 1, 3),
    _Sw0657851RestoreDefault_Type()
)
sw0657851RestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851RestoreDefault.setStatus("current")


class _Sw0657851RestoreUser_Type(Integer32):
    """Custom type sw0657851RestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851RestoreUser_Type.__name__ = "Integer32"
_Sw0657851RestoreUser_Object = MibScalar
sw0657851RestoreUser = _Sw0657851RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5, 1, 4),
    _Sw0657851RestoreUser_Type()
)
sw0657851RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851RestoreUser.setStatus("current")
_Sw0657851ConfigFile_ObjectIdentity = ObjectIdentity
sw0657851ConfigFile = _Sw0657851ConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5, 2)
)
_Sw0657851ExportIpAddress_Type = IpAddress
_Sw0657851ExportIpAddress_Object = MibScalar
sw0657851ExportIpAddress = _Sw0657851ExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5, 2, 1),
    _Sw0657851ExportIpAddress_Type()
)
sw0657851ExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ExportIpAddress.setStatus("current")


class _Sw0657851DoExportConfig_Type(Integer32):
    """Custom type sw0657851DoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Sw0657851DoExportConfig_Type.__name__ = "Integer32"
_Sw0657851DoExportConfig_Object = MibScalar
sw0657851DoExportConfig = _Sw0657851DoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5, 2, 2),
    _Sw0657851DoExportConfig_Type()
)
sw0657851DoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DoExportConfig.setStatus("current")
_Sw0657851ImportIpAddress_Type = IpAddress
_Sw0657851ImportIpAddress_Object = MibScalar
sw0657851ImportIpAddress = _Sw0657851ImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5, 2, 3),
    _Sw0657851ImportIpAddress_Type()
)
sw0657851ImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ImportIpAddress.setStatus("current")
_Sw0657851ImportConfigName_Type = DisplayString
_Sw0657851ImportConfigName_Object = MibScalar
sw0657851ImportConfigName = _Sw0657851ImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5, 2, 4),
    _Sw0657851ImportConfigName_Type()
)
sw0657851ImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ImportConfigName.setStatus("current")


class _Sw0657851DoImportConfig_Type(Integer32):
    """Custom type sw0657851DoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Sw0657851DoImportConfig_Type.__name__ = "Integer32"
_Sw0657851DoImportConfig_Object = MibScalar
sw0657851DoImportConfig = _Sw0657851DoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 5, 2, 5),
    _Sw0657851DoImportConfig_Type()
)
sw0657851DoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DoImportConfig.setStatus("current")
_Sw0657851Log_ObjectIdentity = ObjectIdentity
sw0657851Log = _Sw0657851Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 7)
)


class _Sw0657851ClearLog_Type(Integer32):
    """Custom type sw0657851ClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851ClearLog_Type.__name__ = "Integer32"
_Sw0657851ClearLog_Object = MibScalar
sw0657851ClearLog = _Sw0657851ClearLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 7, 1),
    _Sw0657851ClearLog_Type()
)
sw0657851ClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ClearLog.setStatus("current")


class _Sw0657851LogNumber_Type(Integer32):
    """Custom type sw0657851LogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Sw0657851LogNumber_Type.__name__ = "Integer32"
_Sw0657851LogNumber_Object = MibScalar
sw0657851LogNumber = _Sw0657851LogNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 7, 4),
    _Sw0657851LogNumber_Type()
)
sw0657851LogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851LogNumber.setStatus("current")
_Sw0657851LogTable_Object = MibTable
sw0657851LogTable = _Sw0657851LogTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 7, 5)
)
if mibBuilder.loadTexts:
    sw0657851LogTable.setStatus("current")
_Sw0657851LogEntry_Object = MibTableRow
sw0657851LogEntry = _Sw0657851LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 7, 5, 1)
)
sw0657851LogEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851LogIndex"),
)
if mibBuilder.loadTexts:
    sw0657851LogEntry.setStatus("current")


class _Sw0657851LogIndex_Type(Integer32):
    """Custom type sw0657851LogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Sw0657851LogIndex_Type.__name__ = "Integer32"
_Sw0657851LogIndex_Object = MibTableColumn
sw0657851LogIndex = _Sw0657851LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 7, 5, 1, 1),
    _Sw0657851LogIndex_Type()
)
sw0657851LogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851LogIndex.setStatus("current")
_Sw0657851LogEvent_Type = DisplayString
_Sw0657851LogEvent_Object = MibTableColumn
sw0657851LogEvent = _Sw0657851LogEvent_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 7, 5, 1, 2),
    _Sw0657851LogEvent_Type()
)
sw0657851LogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851LogEvent.setStatus("current")
_Sw0657851Firmware_ObjectIdentity = ObjectIdentity
sw0657851Firmware = _Sw0657851Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 8)
)
_Sw0657851FirmwareIpAddress_Type = IpAddress
_Sw0657851FirmwareIpAddress_Object = MibScalar
sw0657851FirmwareIpAddress = _Sw0657851FirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 8, 1),
    _Sw0657851FirmwareIpAddress_Type()
)
sw0657851FirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851FirmwareIpAddress.setStatus("current")
_Sw0657851FirmwareFileName_Type = DisplayString
_Sw0657851FirmwareFileName_Object = MibScalar
sw0657851FirmwareFileName = _Sw0657851FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 8, 2),
    _Sw0657851FirmwareFileName_Type()
)
sw0657851FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851FirmwareFileName.setStatus("current")


class _Sw0657851DoFirmwareUpgrade_Type(Integer32):
    """Custom type sw0657851DoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851DoFirmwareUpgrade_Type.__name__ = "Integer32"
_Sw0657851DoFirmwareUpgrade_Object = MibScalar
sw0657851DoFirmwareUpgrade = _Sw0657851DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 8, 3),
    _Sw0657851DoFirmwareUpgrade_Type()
)
sw0657851DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851DoFirmwareUpgrade.setStatus("current")
_Sw0657851Port_ObjectIdentity = ObjectIdentity
sw0657851Port = _Sw0657851Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9)
)
_Sw0657851PortStatus_ObjectIdentity = ObjectIdentity
sw0657851PortStatus = _Sw0657851PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 1)
)


class _Sw0657851PortStatusNumber_Type(Integer32):
    """Custom type sw0657851PortStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657851PortStatusNumber_Type.__name__ = "Integer32"
_Sw0657851PortStatusNumber_Object = MibScalar
sw0657851PortStatusNumber = _Sw0657851PortStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 1, 1),
    _Sw0657851PortStatusNumber_Type()
)
sw0657851PortStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851PortStatusNumber.setStatus("current")
_Sw0657851PortStatusTable_Object = MibTable
sw0657851PortStatusTable = _Sw0657851PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    sw0657851PortStatusTable.setStatus("current")
_Sw0657851PortStatusEntry_Object = MibTableRow
sw0657851PortStatusEntry = _Sw0657851PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 1, 2, 1)
)
sw0657851PortStatusEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851PortStatusIndex"),
)
if mibBuilder.loadTexts:
    sw0657851PortStatusEntry.setStatus("current")


class _Sw0657851PortStatusIndex_Type(Integer32):
    """Custom type sw0657851PortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657851PortStatusIndex_Type.__name__ = "Integer32"
_Sw0657851PortStatusIndex_Object = MibTableColumn
sw0657851PortStatusIndex = _Sw0657851PortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 1, 2, 1, 1),
    _Sw0657851PortStatusIndex_Type()
)
sw0657851PortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851PortStatusIndex.setStatus("current")
_Sw0657851PortStatusMedia_Type = DisplayString
_Sw0657851PortStatusMedia_Object = MibTableColumn
sw0657851PortStatusMedia = _Sw0657851PortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 1, 2, 1, 2),
    _Sw0657851PortStatusMedia_Type()
)
sw0657851PortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851PortStatusMedia.setStatus("current")
_Sw0657851PortStatusLink_Type = DisplayString
_Sw0657851PortStatusLink_Object = MibTableColumn
sw0657851PortStatusLink = _Sw0657851PortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 1, 2, 1, 3),
    _Sw0657851PortStatusLink_Type()
)
sw0657851PortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851PortStatusLink.setStatus("current")
_Sw0657851PortStatusSpdDpx_Type = DisplayString
_Sw0657851PortStatusSpdDpx_Object = MibTableColumn
sw0657851PortStatusSpdDpx = _Sw0657851PortStatusSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 1, 2, 1, 4),
    _Sw0657851PortStatusSpdDpx_Type()
)
sw0657851PortStatusSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851PortStatusSpdDpx.setStatus("current")
_Sw0657851PortStatusFlwCtrlRx_Type = DisplayString
_Sw0657851PortStatusFlwCtrlRx_Object = MibTableColumn
sw0657851PortStatusFlwCtrlRx = _Sw0657851PortStatusFlwCtrlRx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 1, 2, 1, 5),
    _Sw0657851PortStatusFlwCtrlRx_Type()
)
sw0657851PortStatusFlwCtrlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851PortStatusFlwCtrlRx.setStatus("current")
_Sw0657851PortStatusFlwCtrlTx_Type = DisplayString
_Sw0657851PortStatusFlwCtrlTx_Object = MibTableColumn
sw0657851PortStatusFlwCtrlTx = _Sw0657851PortStatusFlwCtrlTx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 1, 2, 1, 6),
    _Sw0657851PortStatusFlwCtrlTx_Type()
)
sw0657851PortStatusFlwCtrlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851PortStatusFlwCtrlTx.setStatus("current")
_Sw0657851PortStatuDescription_Type = DisplayString
_Sw0657851PortStatuDescription_Object = MibTableColumn
sw0657851PortStatuDescription = _Sw0657851PortStatuDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 1, 2, 1, 7),
    _Sw0657851PortStatuDescription_Type()
)
sw0657851PortStatuDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851PortStatuDescription.setStatus("current")
_Sw0657851PortConf_ObjectIdentity = ObjectIdentity
sw0657851PortConf = _Sw0657851PortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 2)
)


class _Sw0657851PortConfNumber_Type(Integer32):
    """Custom type sw0657851PortConfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657851PortConfNumber_Type.__name__ = "Integer32"
_Sw0657851PortConfNumber_Object = MibScalar
sw0657851PortConfNumber = _Sw0657851PortConfNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 2, 1),
    _Sw0657851PortConfNumber_Type()
)
sw0657851PortConfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851PortConfNumber.setStatus("current")
_Sw0657851PortConfTable_Object = MibTable
sw0657851PortConfTable = _Sw0657851PortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    sw0657851PortConfTable.setStatus("current")
_Sw0657851PortConfEntry_Object = MibTableRow
sw0657851PortConfEntry = _Sw0657851PortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 2, 2, 1)
)
sw0657851PortConfEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851PortConfIndex"),
)
if mibBuilder.loadTexts:
    sw0657851PortConfEntry.setStatus("current")


class _Sw0657851PortConfIndex_Type(Integer32):
    """Custom type sw0657851PortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657851PortConfIndex_Type.__name__ = "Integer32"
_Sw0657851PortConfIndex_Object = MibTableColumn
sw0657851PortConfIndex = _Sw0657851PortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 2, 2, 1, 1),
    _Sw0657851PortConfIndex_Type()
)
sw0657851PortConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851PortConfIndex.setStatus("current")


class _Sw0657851PortConfPortState_Type(Integer32):
    """Custom type sw0657851PortConfPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851PortConfPortState_Type.__name__ = "Integer32"
_Sw0657851PortConfPortState_Object = MibTableColumn
sw0657851PortConfPortState = _Sw0657851PortConfPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 2, 2, 1, 2),
    _Sw0657851PortConfPortState_Type()
)
sw0657851PortConfPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851PortConfPortState.setStatus("current")


class _Sw0657851PortConfSpdDpx_Type(Integer32):
    """Custom type sw0657851PortConfSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Sw0657851PortConfSpdDpx_Type.__name__ = "Integer32"
_Sw0657851PortConfSpdDpx_Object = MibTableColumn
sw0657851PortConfSpdDpx = _Sw0657851PortConfSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 2, 2, 1, 3),
    _Sw0657851PortConfSpdDpx_Type()
)
sw0657851PortConfSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851PortConfSpdDpx.setStatus("current")


class _Sw0657851PortConfFlwCtrl_Type(Integer32):
    """Custom type sw0657851PortConfFlwCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851PortConfFlwCtrl_Type.__name__ = "Integer32"
_Sw0657851PortConfFlwCtrl_Object = MibTableColumn
sw0657851PortConfFlwCtrl = _Sw0657851PortConfFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 2, 2, 1, 4),
    _Sw0657851PortConfFlwCtrl_Type()
)
sw0657851PortConfFlwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851PortConfFlwCtrl.setStatus("current")


class _Sw0657851PortConfExcessiveCollisionMode_Type(Integer32):
    """Custom type sw0657851PortConfExcessiveCollisionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851PortConfExcessiveCollisionMode_Type.__name__ = "Integer32"
_Sw0657851PortConfExcessiveCollisionMode_Object = MibTableColumn
sw0657851PortConfExcessiveCollisionMode = _Sw0657851PortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 2, 2, 1, 5),
    _Sw0657851PortConfExcessiveCollisionMode_Type()
)
sw0657851PortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851PortConfExcessiveCollisionMode.setStatus("current")
_Sw0657851PortConfDescription_Type = DisplayString
_Sw0657851PortConfDescription_Object = MibTableColumn
sw0657851PortConfDescription = _Sw0657851PortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 2, 2, 1, 6),
    _Sw0657851PortConfDescription_Type()
)
sw0657851PortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851PortConfDescription.setStatus("current")
_Sw0657851SFPInfo_ObjectIdentity = ObjectIdentity
sw0657851SFPInfo = _Sw0657851SFPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3)
)


class _Sw0657851SFPInfoNumber_Type(Integer32):
    """Custom type sw0657851SFPInfoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657851SFPInfoNumber_Type.__name__ = "Integer32"
_Sw0657851SFPInfoNumber_Object = MibScalar
sw0657851SFPInfoNumber = _Sw0657851SFPInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 1),
    _Sw0657851SFPInfoNumber_Type()
)
sw0657851SFPInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPInfoNumber.setStatus("current")
_Sw0657851SFPInfoTable_Object = MibTable
sw0657851SFPInfoTable = _Sw0657851SFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    sw0657851SFPInfoTable.setStatus("current")
_Sw0657851SFPInfoEntry_Object = MibTableRow
sw0657851SFPInfoEntry = _Sw0657851SFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1)
)
sw0657851SFPInfoEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851SFPInfoIndex"),
)
if mibBuilder.loadTexts:
    sw0657851SFPInfoEntry.setStatus("current")


class _Sw0657851SFPInfoIndex_Type(Integer32):
    """Custom type sw0657851SFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657851SFPInfoIndex_Type.__name__ = "Integer32"
_Sw0657851SFPInfoIndex_Object = MibTableColumn
sw0657851SFPInfoIndex = _Sw0657851SFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 1),
    _Sw0657851SFPInfoIndex_Type()
)
sw0657851SFPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPInfoIndex.setStatus("current")
_Sw0657851SFPConnectorType_Type = DisplayString
_Sw0657851SFPConnectorType_Object = MibTableColumn
sw0657851SFPConnectorType = _Sw0657851SFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 2),
    _Sw0657851SFPConnectorType_Type()
)
sw0657851SFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPConnectorType.setStatus("current")
_Sw0657851SFPFiberType_Type = DisplayString
_Sw0657851SFPFiberType_Object = MibTableColumn
sw0657851SFPFiberType = _Sw0657851SFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 3),
    _Sw0657851SFPFiberType_Type()
)
sw0657851SFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPFiberType.setStatus("current")
_Sw0657851SFPWavelength_Type = DisplayString
_Sw0657851SFPWavelength_Object = MibTableColumn
sw0657851SFPWavelength = _Sw0657851SFPWavelength_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 4),
    _Sw0657851SFPWavelength_Type()
)
sw0657851SFPWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPWavelength.setStatus("current")
_Sw0657851SFPBaudRate_Type = DisplayString
_Sw0657851SFPBaudRate_Object = MibTableColumn
sw0657851SFPBaudRate = _Sw0657851SFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 5),
    _Sw0657851SFPBaudRate_Type()
)
sw0657851SFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPBaudRate.setStatus("current")
_Sw0657851SFPVendorOUI_Type = DisplayString
_Sw0657851SFPVendorOUI_Object = MibTableColumn
sw0657851SFPVendorOUI = _Sw0657851SFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 6),
    _Sw0657851SFPVendorOUI_Type()
)
sw0657851SFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPVendorOUI.setStatus("current")
_Sw0657851SFPVendorName_Type = DisplayString
_Sw0657851SFPVendorName_Object = MibTableColumn
sw0657851SFPVendorName = _Sw0657851SFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 7),
    _Sw0657851SFPVendorName_Type()
)
sw0657851SFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPVendorName.setStatus("current")
_Sw0657851SFPVendorPN_Type = DisplayString
_Sw0657851SFPVendorPN_Object = MibTableColumn
sw0657851SFPVendorPN = _Sw0657851SFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 8),
    _Sw0657851SFPVendorPN_Type()
)
sw0657851SFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPVendorPN.setStatus("current")
_Sw0657851SFPVendorRev_Type = DisplayString
_Sw0657851SFPVendorRev_Object = MibTableColumn
sw0657851SFPVendorRev = _Sw0657851SFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 9),
    _Sw0657851SFPVendorRev_Type()
)
sw0657851SFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPVendorRev.setStatus("current")
_Sw0657851SFPVendorSN_Type = DisplayString
_Sw0657851SFPVendorSN_Object = MibTableColumn
sw0657851SFPVendorSN = _Sw0657851SFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 10),
    _Sw0657851SFPVendorSN_Type()
)
sw0657851SFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPVendorSN.setStatus("current")
_Sw0657851SFPDateCode_Type = DisplayString
_Sw0657851SFPDateCode_Object = MibTableColumn
sw0657851SFPDateCode = _Sw0657851SFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 11),
    _Sw0657851SFPDateCode_Type()
)
sw0657851SFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPDateCode.setStatus("current")
_Sw0657851SFPTemperature_Type = DisplayString
_Sw0657851SFPTemperature_Object = MibTableColumn
sw0657851SFPTemperature = _Sw0657851SFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 12),
    _Sw0657851SFPTemperature_Type()
)
sw0657851SFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPTemperature.setStatus("current")
_Sw0657851SFPVcc_Type = DisplayString
_Sw0657851SFPVcc_Object = MibTableColumn
sw0657851SFPVcc = _Sw0657851SFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 13),
    _Sw0657851SFPVcc_Type()
)
sw0657851SFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPVcc.setStatus("current")
_Sw0657851SFPTxBias_Type = DisplayString
_Sw0657851SFPTxBias_Object = MibTableColumn
sw0657851SFPTxBias = _Sw0657851SFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 14),
    _Sw0657851SFPTxBias_Type()
)
sw0657851SFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPTxBias.setStatus("current")
_Sw0657851SFPTxPWR_Type = DisplayString
_Sw0657851SFPTxPWR_Object = MibTableColumn
sw0657851SFPTxPWR = _Sw0657851SFPTxPWR_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 15),
    _Sw0657851SFPTxPWR_Type()
)
sw0657851SFPTxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPTxPWR.setStatus("current")
_Sw0657851SFPRxPWR_Type = DisplayString
_Sw0657851SFPRxPWR_Object = MibTableColumn
sw0657851SFPRxPWR = _Sw0657851SFPRxPWR_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 9, 3, 2, 1, 16),
    _Sw0657851SFPRxPWR_Type()
)
sw0657851SFPRxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851SFPRxPWR.setStatus("current")
_Sw0657851Mirror_ObjectIdentity = ObjectIdentity
sw0657851Mirror = _Sw0657851Mirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 10)
)


class _Sw0657851MirroringPort_Type(Integer32):
    """Custom type sw0657851MirroringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Sw0657851MirroringPort_Type.__name__ = "Integer32"
_Sw0657851MirroringPort_Object = MibScalar
sw0657851MirroringPort = _Sw0657851MirroringPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 10, 1),
    _Sw0657851MirroringPort_Type()
)
sw0657851MirroringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MirroringPort.setStatus("current")
_Sw0657851MirroredPortsTable_Object = MibTable
sw0657851MirroredPortsTable = _Sw0657851MirroredPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 10, 2)
)
if mibBuilder.loadTexts:
    sw0657851MirroredPortsTable.setStatus("current")
_Sw0657851MirroredPortsEntry_Object = MibTableRow
sw0657851MirroredPortsEntry = _Sw0657851MirroredPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 10, 2, 1)
)
sw0657851MirroredPortsEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851MirroredPortIndex"),
)
if mibBuilder.loadTexts:
    sw0657851MirroredPortsEntry.setStatus("current")


class _Sw0657851MirroredPortIndex_Type(Integer32):
    """Custom type sw0657851MirroredPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851MirroredPortIndex_Type.__name__ = "Integer32"
_Sw0657851MirroredPortIndex_Object = MibTableColumn
sw0657851MirroredPortIndex = _Sw0657851MirroredPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 10, 2, 1, 1),
    _Sw0657851MirroredPortIndex_Type()
)
sw0657851MirroredPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851MirroredPortIndex.setStatus("current")


class _Sw0657851MirroredPortSrouceEnable_Type(Integer32):
    """Custom type sw0657851MirroredPortSrouceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851MirroredPortSrouceEnable_Type.__name__ = "Integer32"
_Sw0657851MirroredPortSrouceEnable_Object = MibTableColumn
sw0657851MirroredPortSrouceEnable = _Sw0657851MirroredPortSrouceEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 10, 2, 1, 2),
    _Sw0657851MirroredPortSrouceEnable_Type()
)
sw0657851MirroredPortSrouceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MirroredPortSrouceEnable.setStatus("current")


class _Sw0657851MirroredPortDestinationEnable_Type(Integer32):
    """Custom type sw0657851MirroredPortDestinationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851MirroredPortDestinationEnable_Type.__name__ = "Integer32"
_Sw0657851MirroredPortDestinationEnable_Object = MibTableColumn
sw0657851MirroredPortDestinationEnable = _Sw0657851MirroredPortDestinationEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 10, 2, 1, 3),
    _Sw0657851MirroredPortDestinationEnable_Type()
)
sw0657851MirroredPortDestinationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MirroredPortDestinationEnable.setStatus("current")
_Sw0657851MaxPktLen_ObjectIdentity = ObjectIdentity
sw0657851MaxPktLen = _Sw0657851MaxPktLen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 11)
)


class _Sw0657851MaxPktLenPortNumber_Type(Integer32):
    """Custom type sw0657851MaxPktLenPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851MaxPktLenPortNumber_Type.__name__ = "Integer32"
_Sw0657851MaxPktLenPortNumber_Object = MibScalar
sw0657851MaxPktLenPortNumber = _Sw0657851MaxPktLenPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 11, 1),
    _Sw0657851MaxPktLenPortNumber_Type()
)
sw0657851MaxPktLenPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851MaxPktLenPortNumber.setStatus("current")
_Sw0657851MaxPktLenConfTable_Object = MibTable
sw0657851MaxPktLenConfTable = _Sw0657851MaxPktLenConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 11, 2)
)
if mibBuilder.loadTexts:
    sw0657851MaxPktLenConfTable.setStatus("current")
_Sw0657851MaxPktLenConfEntry_Object = MibTableRow
sw0657851MaxPktLenConfEntry = _Sw0657851MaxPktLenConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 11, 2, 1)
)
sw0657851MaxPktLenConfEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851MaxPktLenConfIndex"),
)
if mibBuilder.loadTexts:
    sw0657851MaxPktLenConfEntry.setStatus("current")


class _Sw0657851MaxPktLenConfIndex_Type(Integer32):
    """Custom type sw0657851MaxPktLenConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851MaxPktLenConfIndex_Type.__name__ = "Integer32"
_Sw0657851MaxPktLenConfIndex_Object = MibTableColumn
sw0657851MaxPktLenConfIndex = _Sw0657851MaxPktLenConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 11, 2, 1, 1),
    _Sw0657851MaxPktLenConfIndex_Type()
)
sw0657851MaxPktLenConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851MaxPktLenConfIndex.setStatus("current")


class _Sw0657851MaxPktLenConfSetting_Type(Integer32):
    """Custom type sw0657851MaxPktLenConfSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Sw0657851MaxPktLenConfSetting_Type.__name__ = "Integer32"
_Sw0657851MaxPktLenConfSetting_Object = MibTableColumn
sw0657851MaxPktLenConfSetting = _Sw0657851MaxPktLenConfSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 11, 2, 1, 2),
    _Sw0657851MaxPktLenConfSetting_Type()
)
sw0657851MaxPktLenConfSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MaxPktLenConfSetting.setStatus("current")
_Sw0657851LoopDetectedConf_ObjectIdentity = ObjectIdentity
sw0657851LoopDetectedConf = _Sw0657851LoopDetectedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 12)
)


class _Sw0657851LoopDetectedNumber_Type(Integer32):
    """Custom type sw0657851LoopDetectedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657851LoopDetectedNumber_Type.__name__ = "Integer32"
_Sw0657851LoopDetectedNumber_Object = MibScalar
sw0657851LoopDetectedNumber = _Sw0657851LoopDetectedNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 12, 1),
    _Sw0657851LoopDetectedNumber_Type()
)
sw0657851LoopDetectedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851LoopDetectedNumber.setStatus("current")
_Sw0657851LoopDetectedTable_Object = MibTable
sw0657851LoopDetectedTable = _Sw0657851LoopDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 12, 2)
)
if mibBuilder.loadTexts:
    sw0657851LoopDetectedTable.setStatus("current")
_Sw0657851LoopDetectedEntry_Object = MibTableRow
sw0657851LoopDetectedEntry = _Sw0657851LoopDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 12, 2, 1)
)
sw0657851LoopDetectedEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851LoopDetectedfIndex"),
)
if mibBuilder.loadTexts:
    sw0657851LoopDetectedEntry.setStatus("current")


class _Sw0657851LoopDetectedfIndex_Type(Integer32):
    """Custom type sw0657851LoopDetectedfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657851LoopDetectedfIndex_Type.__name__ = "Integer32"
_Sw0657851LoopDetectedfIndex_Object = MibTableColumn
sw0657851LoopDetectedfIndex = _Sw0657851LoopDetectedfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 12, 2, 1, 1),
    _Sw0657851LoopDetectedfIndex_Type()
)
sw0657851LoopDetectedfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851LoopDetectedfIndex.setStatus("current")


class _Sw0657851LoopDetectedPort_Type(Integer32):
    """Custom type sw0657851LoopDetectedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851LoopDetectedPort_Type.__name__ = "Integer32"
_Sw0657851LoopDetectedPort_Object = MibTableColumn
sw0657851LoopDetectedPort = _Sw0657851LoopDetectedPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 12, 2, 1, 2),
    _Sw0657851LoopDetectedPort_Type()
)
sw0657851LoopDetectedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851LoopDetectedPort.setStatus("current")


class _Sw0657851LoopDetectedLockedPort_Type(Integer32):
    """Custom type sw0657851LoopDetectedLockedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851LoopDetectedLockedPort_Type.__name__ = "Integer32"
_Sw0657851LoopDetectedLockedPort_Object = MibTableColumn
sw0657851LoopDetectedLockedPort = _Sw0657851LoopDetectedLockedPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 12, 2, 1, 3),
    _Sw0657851LoopDetectedLockedPort_Type()
)
sw0657851LoopDetectedLockedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851LoopDetectedLockedPort.setStatus("current")
_Sw0657851ManagementPolicy_ObjectIdentity = ObjectIdentity
sw0657851ManagementPolicy = _Sw0657851ManagementPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13)
)


class _Sw0657851ManagementSecurityNumber_Type(Integer32):
    """Custom type sw0657851ManagementSecurityNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Sw0657851ManagementSecurityNumber_Type.__name__ = "Integer32"
_Sw0657851ManagementSecurityNumber_Object = MibScalar
sw0657851ManagementSecurityNumber = _Sw0657851ManagementSecurityNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13, 1),
    _Sw0657851ManagementSecurityNumber_Type()
)
sw0657851ManagementSecurityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851ManagementSecurityNumber.setStatus("current")


class _Sw0657851ManagementSecurityEntryCreate_Type(Integer32):
    """Custom type sw0657851ManagementSecurityEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Sw0657851ManagementSecurityEntryCreate_Type.__name__ = "Integer32"
_Sw0657851ManagementSecurityEntryCreate_Object = MibScalar
sw0657851ManagementSecurityEntryCreate = _Sw0657851ManagementSecurityEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13, 2),
    _Sw0657851ManagementSecurityEntryCreate_Type()
)
sw0657851ManagementSecurityEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ManagementSecurityEntryCreate.setStatus("current")
_Sw0657851ManagementSecurityTable_Object = MibTable
sw0657851ManagementSecurityTable = _Sw0657851ManagementSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13, 3)
)
if mibBuilder.loadTexts:
    sw0657851ManagementSecurityTable.setStatus("current")
_Sw0657851ManagementSecurityEntry_Object = MibTableRow
sw0657851ManagementSecurityEntry = _Sw0657851ManagementSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13, 3, 1)
)
sw0657851ManagementSecurityEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851ManagementSecurityIndex"),
)
if mibBuilder.loadTexts:
    sw0657851ManagementSecurityEntry.setStatus("current")


class _Sw0657851ManagementSecurityIndex_Type(Integer32):
    """Custom type sw0657851ManagementSecurityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Sw0657851ManagementSecurityIndex_Type.__name__ = "Integer32"
_Sw0657851ManagementSecurityIndex_Object = MibTableColumn
sw0657851ManagementSecurityIndex = _Sw0657851ManagementSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13, 3, 1, 1),
    _Sw0657851ManagementSecurityIndex_Type()
)
sw0657851ManagementSecurityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851ManagementSecurityIndex.setStatus("current")
_Sw0657851ManagementSecurityName_Type = DisplayString
_Sw0657851ManagementSecurityName_Object = MibTableColumn
sw0657851ManagementSecurityName = _Sw0657851ManagementSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13, 3, 1, 2),
    _Sw0657851ManagementSecurityName_Type()
)
sw0657851ManagementSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ManagementSecurityName.setStatus("current")
_Sw0657851ManagementSecurityIpRange_Type = DisplayString
_Sw0657851ManagementSecurityIpRange_Object = MibTableColumn
sw0657851ManagementSecurityIpRange = _Sw0657851ManagementSecurityIpRange_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13, 3, 1, 3),
    _Sw0657851ManagementSecurityIpRange_Type()
)
sw0657851ManagementSecurityIpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ManagementSecurityIpRange.setStatus("current")
_Sw0657851ManagementSecurityIncomigPort_Type = DisplayString
_Sw0657851ManagementSecurityIncomigPort_Object = MibTableColumn
sw0657851ManagementSecurityIncomigPort = _Sw0657851ManagementSecurityIncomigPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13, 3, 1, 4),
    _Sw0657851ManagementSecurityIncomigPort_Type()
)
sw0657851ManagementSecurityIncomigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ManagementSecurityIncomigPort.setStatus("current")
_Sw0657851ManagementSecurityAccessType_Type = DisplayString
_Sw0657851ManagementSecurityAccessType_Object = MibTableColumn
sw0657851ManagementSecurityAccessType = _Sw0657851ManagementSecurityAccessType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13, 3, 1, 5),
    _Sw0657851ManagementSecurityAccessType_Type()
)
sw0657851ManagementSecurityAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ManagementSecurityAccessType.setStatus("current")


class _Sw0657851ManagementSecurityAction_Type(Integer32):
    """Custom type sw0657851ManagementSecurityAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851ManagementSecurityAction_Type.__name__ = "Integer32"
_Sw0657851ManagementSecurityAction_Object = MibTableColumn
sw0657851ManagementSecurityAction = _Sw0657851ManagementSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13, 3, 1, 6),
    _Sw0657851ManagementSecurityAction_Type()
)
sw0657851ManagementSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ManagementSecurityAction.setStatus("current")


class _Sw0657851ManagementSecurityEntryAction_Type(Integer32):
    """Custom type sw0657851ManagementSecurityEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Sw0657851ManagementSecurityEntryAction_Type.__name__ = "Integer32"
_Sw0657851ManagementSecurityEntryAction_Object = MibTableColumn
sw0657851ManagementSecurityEntryAction = _Sw0657851ManagementSecurityEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 13, 3, 1, 7),
    _Sw0657851ManagementSecurityEntryAction_Type()
)
sw0657851ManagementSecurityEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ManagementSecurityEntryAction.setStatus("current")
_Sw0657851VLAN_ObjectIdentity = ObjectIdentity
sw0657851VLAN = _Sw0657851VLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14)
)
_Sw0657851VlanConf_ObjectIdentity = ObjectIdentity
sw0657851VlanConf = _Sw0657851VlanConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 1)
)


class _Sw0657851VlanMode_Type(Integer32):
    """Custom type sw0657851VlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851VlanMode_Type.__name__ = "Integer32"
_Sw0657851VlanMode_Object = MibScalar
sw0657851VlanMode = _Sw0657851VlanMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 1, 1),
    _Sw0657851VlanMode_Type()
)
sw0657851VlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851VlanMode.setStatus("current")


class _Sw0657851ManagementVlan_Type(Integer32):
    """Custom type sw0657851ManagementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851ManagementVlan_Type.__name__ = "Integer32"
_Sw0657851ManagementVlan_Object = MibScalar
sw0657851ManagementVlan = _Sw0657851ManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 1, 2),
    _Sw0657851ManagementVlan_Type()
)
sw0657851ManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851ManagementVlan.setStatus("current")
_Sw0657851PortIsolation_Type = DisplayString
_Sw0657851PortIsolation_Object = MibScalar
sw0657851PortIsolation = _Sw0657851PortIsolation_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 1, 3),
    _Sw0657851PortIsolation_Type()
)
sw0657851PortIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851PortIsolation.setStatus("current")
_Sw0657851TagBaseVlanGroup_ObjectIdentity = ObjectIdentity
sw0657851TagBaseVlanGroup = _Sw0657851TagBaseVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2)
)


class _Sw0657851TagBaseVlanNumber_Type(Integer32):
    """Custom type sw0657851TagBaseVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851TagBaseVlanNumber_Type.__name__ = "Integer32"
_Sw0657851TagBaseVlanNumber_Object = MibScalar
sw0657851TagBaseVlanNumber = _Sw0657851TagBaseVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2, 1),
    _Sw0657851TagBaseVlanNumber_Type()
)
sw0657851TagBaseVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TagBaseVlanNumber.setStatus("current")


class _Sw0657851TagBaseVlanGroupEntryCreate_Type(Integer32):
    """Custom type sw0657851TagBaseVlanGroupEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Sw0657851TagBaseVlanGroupEntryCreate_Type.__name__ = "Integer32"
_Sw0657851TagBaseVlanGroupEntryCreate_Object = MibScalar
sw0657851TagBaseVlanGroupEntryCreate = _Sw0657851TagBaseVlanGroupEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2, 2),
    _Sw0657851TagBaseVlanGroupEntryCreate_Type()
)
sw0657851TagBaseVlanGroupEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TagBaseVlanGroupEntryCreate.setStatus("current")
_Sw0657851TagBaseVlanGroupTable_Object = MibTable
sw0657851TagBaseVlanGroupTable = _Sw0657851TagBaseVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2, 3)
)
if mibBuilder.loadTexts:
    sw0657851TagBaseVlanGroupTable.setStatus("current")
_Sw0657851TagBaseVlanGroupEntry_Object = MibTableRow
sw0657851TagBaseVlanGroupEntry = _Sw0657851TagBaseVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2, 3, 1)
)
sw0657851TagBaseVlanGroupEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851TagBaseVlanVid"),
)
if mibBuilder.loadTexts:
    sw0657851TagBaseVlanGroupEntry.setStatus("current")


class _Sw0657851TagBaseVlanVid_Type(Integer32):
    """Custom type sw0657851TagBaseVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851TagBaseVlanVid_Type.__name__ = "Integer32"
_Sw0657851TagBaseVlanVid_Object = MibTableColumn
sw0657851TagBaseVlanVid = _Sw0657851TagBaseVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2, 3, 1, 1),
    _Sw0657851TagBaseVlanVid_Type()
)
sw0657851TagBaseVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851TagBaseVlanVid.setStatus("current")
_Sw0657851TagBaseVlanName_Type = DisplayString
_Sw0657851TagBaseVlanName_Object = MibTableColumn
sw0657851TagBaseVlanName = _Sw0657851TagBaseVlanName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2, 3, 1, 2),
    _Sw0657851TagBaseVlanName_Type()
)
sw0657851TagBaseVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TagBaseVlanName.setStatus("current")


class _Sw0657851TagBaseVlanIgmpProxy_Type(Integer32):
    """Custom type sw0657851TagBaseVlanIgmpProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851TagBaseVlanIgmpProxy_Type.__name__ = "Integer32"
_Sw0657851TagBaseVlanIgmpProxy_Object = MibTableColumn
sw0657851TagBaseVlanIgmpProxy = _Sw0657851TagBaseVlanIgmpProxy_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2, 3, 1, 3),
    _Sw0657851TagBaseVlanIgmpProxy_Type()
)
sw0657851TagBaseVlanIgmpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TagBaseVlanIgmpProxy.setStatus("current")


class _Sw0657851TagBaseVlanPrivateVlan_Type(Integer32):
    """Custom type sw0657851TagBaseVlanPrivateVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851TagBaseVlanPrivateVlan_Type.__name__ = "Integer32"
_Sw0657851TagBaseVlanPrivateVlan_Object = MibTableColumn
sw0657851TagBaseVlanPrivateVlan = _Sw0657851TagBaseVlanPrivateVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2, 3, 1, 4),
    _Sw0657851TagBaseVlanPrivateVlan_Type()
)
sw0657851TagBaseVlanPrivateVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TagBaseVlanPrivateVlan.setStatus("current")


class _Sw0657851TagBaseVlanGvrp_Type(Integer32):
    """Custom type sw0657851TagBaseVlanGvrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851TagBaseVlanGvrp_Type.__name__ = "Integer32"
_Sw0657851TagBaseVlanGvrp_Object = MibTableColumn
sw0657851TagBaseVlanGvrp = _Sw0657851TagBaseVlanGvrp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2, 3, 1, 5),
    _Sw0657851TagBaseVlanGvrp_Type()
)
sw0657851TagBaseVlanGvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TagBaseVlanGvrp.setStatus("current")
_Sw0657851TagBaseVlanMemberPort_Type = DisplayString
_Sw0657851TagBaseVlanMemberPort_Object = MibTableColumn
sw0657851TagBaseVlanMemberPort = _Sw0657851TagBaseVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2, 3, 1, 6),
    _Sw0657851TagBaseVlanMemberPort_Type()
)
sw0657851TagBaseVlanMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TagBaseVlanMemberPort.setStatus("current")


class _Sw0657851TagBaseVlanEntryAction_Type(Integer32):
    """Custom type sw0657851TagBaseVlanEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Sw0657851TagBaseVlanEntryAction_Type.__name__ = "Integer32"
_Sw0657851TagBaseVlanEntryAction_Object = MibTableColumn
sw0657851TagBaseVlanEntryAction = _Sw0657851TagBaseVlanEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 2, 3, 1, 7),
    _Sw0657851TagBaseVlanEntryAction_Type()
)
sw0657851TagBaseVlanEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TagBaseVlanEntryAction.setStatus("current")
_Sw0657851VlanPortConfTable_Object = MibTable
sw0657851VlanPortConfTable = _Sw0657851VlanPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 3)
)
if mibBuilder.loadTexts:
    sw0657851VlanPortConfTable.setStatus("current")
_Sw0657851VlanPortConfEntry_Object = MibTableRow
sw0657851VlanPortConfEntry = _Sw0657851VlanPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 3, 1)
)
sw0657851VlanPortConfEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851VlanPortConfIndex"),
)
if mibBuilder.loadTexts:
    sw0657851VlanPortConfEntry.setStatus("current")


class _Sw0657851VlanPortConfIndex_Type(Integer32):
    """Custom type sw0657851VlanPortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851VlanPortConfIndex_Type.__name__ = "Integer32"
_Sw0657851VlanPortConfIndex_Object = MibTableColumn
sw0657851VlanPortConfIndex = _Sw0657851VlanPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 3, 1, 1),
    _Sw0657851VlanPortConfIndex_Type()
)
sw0657851VlanPortConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851VlanPortConfIndex.setStatus("current")


class _Sw0657851VlanPortConfVlanAware_Type(Integer32):
    """Custom type sw0657851VlanPortConfVlanAware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851VlanPortConfVlanAware_Type.__name__ = "Integer32"
_Sw0657851VlanPortConfVlanAware_Object = MibTableColumn
sw0657851VlanPortConfVlanAware = _Sw0657851VlanPortConfVlanAware_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 3, 1, 2),
    _Sw0657851VlanPortConfVlanAware_Type()
)
sw0657851VlanPortConfVlanAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851VlanPortConfVlanAware.setStatus("current")


class _Sw0657851VlanPortConfIngressFiltering_Type(Integer32):
    """Custom type sw0657851VlanPortConfIngressFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851VlanPortConfIngressFiltering_Type.__name__ = "Integer32"
_Sw0657851VlanPortConfIngressFiltering_Object = MibTableColumn
sw0657851VlanPortConfIngressFiltering = _Sw0657851VlanPortConfIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 3, 1, 3),
    _Sw0657851VlanPortConfIngressFiltering_Type()
)
sw0657851VlanPortConfIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851VlanPortConfIngressFiltering.setStatus("current")


class _Sw0657851VlanPortConfFrameType_Type(Integer32):
    """Custom type sw0657851VlanPortConfFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851VlanPortConfFrameType_Type.__name__ = "Integer32"
_Sw0657851VlanPortConfFrameType_Object = MibTableColumn
sw0657851VlanPortConfFrameType = _Sw0657851VlanPortConfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 3, 1, 4),
    _Sw0657851VlanPortConfFrameType_Type()
)
sw0657851VlanPortConfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851VlanPortConfFrameType.setStatus("current")


class _Sw0657851VlanPortConfPvid_Type(Integer32):
    """Custom type sw0657851VlanPortConfPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851VlanPortConfPvid_Type.__name__ = "Integer32"
_Sw0657851VlanPortConfPvid_Object = MibTableColumn
sw0657851VlanPortConfPvid = _Sw0657851VlanPortConfPvid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 3, 1, 5),
    _Sw0657851VlanPortConfPvid_Type()
)
sw0657851VlanPortConfPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851VlanPortConfPvid.setStatus("current")


class _Sw0657851VlanPortConfRole_Type(Integer32):
    """Custom type sw0657851VlanPortConfRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Sw0657851VlanPortConfRole_Type.__name__ = "Integer32"
_Sw0657851VlanPortConfRole_Object = MibTableColumn
sw0657851VlanPortConfRole = _Sw0657851VlanPortConfRole_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 3, 1, 6),
    _Sw0657851VlanPortConfRole_Type()
)
sw0657851VlanPortConfRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851VlanPortConfRole.setStatus("current")


class _Sw0657851VlanPortConfUntagVid_Type(Integer32):
    """Custom type sw0657851VlanPortConfUntagVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851VlanPortConfUntagVid_Type.__name__ = "Integer32"
_Sw0657851VlanPortConfUntagVid_Object = MibTableColumn
sw0657851VlanPortConfUntagVid = _Sw0657851VlanPortConfUntagVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 3, 1, 7),
    _Sw0657851VlanPortConfUntagVid_Type()
)
sw0657851VlanPortConfUntagVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851VlanPortConfUntagVid.setStatus("current")


class _Sw0657851VlanPortConfDoubleTag_Type(Integer32):
    """Custom type sw0657851VlanPortConfDoubleTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Sw0657851VlanPortConfDoubleTag_Type.__name__ = "Integer32"
_Sw0657851VlanPortConfDoubleTag_Object = MibTableColumn
sw0657851VlanPortConfDoubleTag = _Sw0657851VlanPortConfDoubleTag_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 3, 1, 8),
    _Sw0657851VlanPortConfDoubleTag_Type()
)
sw0657851VlanPortConfDoubleTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851VlanPortConfDoubleTag.setStatus("current")
_Sw0657851PortBaseVlanGroup_ObjectIdentity = ObjectIdentity
sw0657851PortBaseVlanGroup = _Sw0657851PortBaseVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 4)
)


class _Sw0657851PortBaseVlanNumber_Type(Integer32):
    """Custom type sw0657851PortBaseVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851PortBaseVlanNumber_Type.__name__ = "Integer32"
_Sw0657851PortBaseVlanNumber_Object = MibScalar
sw0657851PortBaseVlanNumber = _Sw0657851PortBaseVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 4, 1),
    _Sw0657851PortBaseVlanNumber_Type()
)
sw0657851PortBaseVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851PortBaseVlanNumber.setStatus("current")


class _Sw0657851PortBaseVlanGroupEntryCreate_Type(Integer32):
    """Custom type sw0657851PortBaseVlanGroupEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Sw0657851PortBaseVlanGroupEntryCreate_Type.__name__ = "Integer32"
_Sw0657851PortBaseVlanGroupEntryCreate_Object = MibScalar
sw0657851PortBaseVlanGroupEntryCreate = _Sw0657851PortBaseVlanGroupEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 4, 2),
    _Sw0657851PortBaseVlanGroupEntryCreate_Type()
)
sw0657851PortBaseVlanGroupEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851PortBaseVlanGroupEntryCreate.setStatus("current")
_Sw0657851PortBaseVlanGroupTable_Object = MibTable
sw0657851PortBaseVlanGroupTable = _Sw0657851PortBaseVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 4, 3)
)
if mibBuilder.loadTexts:
    sw0657851PortBaseVlanGroupTable.setStatus("current")
_Sw0657851PortBaseVlanGroupEntry_Object = MibTableRow
sw0657851PortBaseVlanGroupEntry = _Sw0657851PortBaseVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 4, 3, 1)
)
sw0657851PortBaseVlanGroupEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851PortBaseVlanGroupIndex"),
)
if mibBuilder.loadTexts:
    sw0657851PortBaseVlanGroupEntry.setStatus("current")


class _Sw0657851PortBaseVlanGroupIndex_Type(Integer32):
    """Custom type sw0657851PortBaseVlanGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851PortBaseVlanGroupIndex_Type.__name__ = "Integer32"
_Sw0657851PortBaseVlanGroupIndex_Object = MibTableColumn
sw0657851PortBaseVlanGroupIndex = _Sw0657851PortBaseVlanGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 4, 3, 1, 1),
    _Sw0657851PortBaseVlanGroupIndex_Type()
)
sw0657851PortBaseVlanGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851PortBaseVlanGroupIndex.setStatus("current")
_Sw0657851PortBaseVlanGroupName_Type = DisplayString
_Sw0657851PortBaseVlanGroupName_Object = MibTableColumn
sw0657851PortBaseVlanGroupName = _Sw0657851PortBaseVlanGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 4, 3, 1, 2),
    _Sw0657851PortBaseVlanGroupName_Type()
)
sw0657851PortBaseVlanGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851PortBaseVlanGroupName.setStatus("current")
_Sw0657851PortBaseVlanGroupMembers_Type = DisplayString
_Sw0657851PortBaseVlanGroupMembers_Object = MibTableColumn
sw0657851PortBaseVlanGroupMembers = _Sw0657851PortBaseVlanGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 4, 3, 1, 3),
    _Sw0657851PortBaseVlanGroupMembers_Type()
)
sw0657851PortBaseVlanGroupMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851PortBaseVlanGroupMembers.setStatus("current")


class _Sw0657851PortBaseVlanGroupEntryAction_Type(Integer32):
    """Custom type sw0657851PortBaseVlanGroupEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Sw0657851PortBaseVlanGroupEntryAction_Type.__name__ = "Integer32"
_Sw0657851PortBaseVlanGroupEntryAction_Object = MibTableColumn
sw0657851PortBaseVlanGroupEntryAction = _Sw0657851PortBaseVlanGroupEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 14, 4, 3, 1, 4),
    _Sw0657851PortBaseVlanGroupEntryAction_Type()
)
sw0657851PortBaseVlanGroupEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851PortBaseVlanGroupEntryAction.setStatus("current")
_Sw0657851MacTableInfo_ObjectIdentity = ObjectIdentity
sw0657851MacTableInfo = _Sw0657851MacTableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15)
)
_Sw0657851MacTableConf_ObjectIdentity = ObjectIdentity
sw0657851MacTableConf = _Sw0657851MacTableConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 1)
)


class _Sw0657851MacAgeTime_Type(Integer32):
    """Custom type sw0657851MacAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Sw0657851MacAgeTime_Type.__name__ = "Integer32"
_Sw0657851MacAgeTime_Object = MibScalar
sw0657851MacAgeTime = _Sw0657851MacAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 1, 1),
    _Sw0657851MacAgeTime_Type()
)
sw0657851MacAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacAgeTime.setStatus("current")
_Sw0657851MacTableLearningConfTable_Object = MibTable
sw0657851MacTableLearningConfTable = _Sw0657851MacTableLearningConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    sw0657851MacTableLearningConfTable.setStatus("current")
_Sw0657851MacTableLearningConfEntry_Object = MibTableRow
sw0657851MacTableLearningConfEntry = _Sw0657851MacTableLearningConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 1, 2, 1)
)
sw0657851MacTableLearningConfEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851MacTableLearningConfIndex"),
)
if mibBuilder.loadTexts:
    sw0657851MacTableLearningConfEntry.setStatus("current")


class _Sw0657851MacTableLearningConfIndex_Type(Integer32):
    """Custom type sw0657851MacTableLearningConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851MacTableLearningConfIndex_Type.__name__ = "Integer32"
_Sw0657851MacTableLearningConfIndex_Object = MibTableColumn
sw0657851MacTableLearningConfIndex = _Sw0657851MacTableLearningConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 1, 2, 1, 1),
    _Sw0657851MacTableLearningConfIndex_Type()
)
sw0657851MacTableLearningConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851MacTableLearningConfIndex.setStatus("current")


class _Sw0657851MacTableLearningConfstate_Type(Integer32):
    """Custom type sw0657851MacTableLearningConfstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Sw0657851MacTableLearningConfstate_Type.__name__ = "Integer32"
_Sw0657851MacTableLearningConfstate_Object = MibTableColumn
sw0657851MacTableLearningConfstate = _Sw0657851MacTableLearningConfstate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 1, 2, 1, 2),
    _Sw0657851MacTableLearningConfstate_Type()
)
sw0657851MacTableLearningConfstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableLearningConfstate.setStatus("current")
_Sw0657851MacTableStaticFilter_ObjectIdentity = ObjectIdentity
sw0657851MacTableStaticFilter = _Sw0657851MacTableStaticFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 2)
)


class _Sw0657851MacTableStaticFilterNumber_Type(Integer32):
    """Custom type sw0657851MacTableStaticFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Sw0657851MacTableStaticFilterNumber_Type.__name__ = "Integer32"
_Sw0657851MacTableStaticFilterNumber_Object = MibScalar
sw0657851MacTableStaticFilterNumber = _Sw0657851MacTableStaticFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 2, 1),
    _Sw0657851MacTableStaticFilterNumber_Type()
)
sw0657851MacTableStaticFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticFilterNumber.setStatus("current")


class _Sw0657851MacTableStaticFilterEntryCreate_Type(Integer32):
    """Custom type sw0657851MacTableStaticFilterEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Sw0657851MacTableStaticFilterEntryCreate_Type.__name__ = "Integer32"
_Sw0657851MacTableStaticFilterEntryCreate_Object = MibScalar
sw0657851MacTableStaticFilterEntryCreate = _Sw0657851MacTableStaticFilterEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 2, 2),
    _Sw0657851MacTableStaticFilterEntryCreate_Type()
)
sw0657851MacTableStaticFilterEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticFilterEntryCreate.setStatus("current")
_Sw0657851MacTableStaticFilterTable_Object = MibTable
sw0657851MacTableStaticFilterTable = _Sw0657851MacTableStaticFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 2, 3)
)
if mibBuilder.loadTexts:
    sw0657851MacTableStaticFilterTable.setStatus("current")
_Sw0657851MacTableStaticFilterEntry_Object = MibTableRow
sw0657851MacTableStaticFilterEntry = _Sw0657851MacTableStaticFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 2, 3, 1)
)
sw0657851MacTableStaticFilterEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851MacTableStaticFilterIndex"),
)
if mibBuilder.loadTexts:
    sw0657851MacTableStaticFilterEntry.setStatus("current")


class _Sw0657851MacTableStaticFilterIndex_Type(Integer32):
    """Custom type sw0657851MacTableStaticFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Sw0657851MacTableStaticFilterIndex_Type.__name__ = "Integer32"
_Sw0657851MacTableStaticFilterIndex_Object = MibTableColumn
sw0657851MacTableStaticFilterIndex = _Sw0657851MacTableStaticFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 2, 3, 1, 1),
    _Sw0657851MacTableStaticFilterIndex_Type()
)
sw0657851MacTableStaticFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticFilterIndex.setStatus("current")
_Sw0657851MacTableStaticFilterMac_Type = DisplayString
_Sw0657851MacTableStaticFilterMac_Object = MibTableColumn
sw0657851MacTableStaticFilterMac = _Sw0657851MacTableStaticFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 2, 3, 1, 2),
    _Sw0657851MacTableStaticFilterMac_Type()
)
sw0657851MacTableStaticFilterMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticFilterMac.setStatus("current")


class _Sw0657851MacTableStaticFilterVid_Type(Integer32):
    """Custom type sw0657851MacTableStaticFilterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851MacTableStaticFilterVid_Type.__name__ = "Integer32"
_Sw0657851MacTableStaticFilterVid_Object = MibTableColumn
sw0657851MacTableStaticFilterVid = _Sw0657851MacTableStaticFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 2, 3, 1, 3),
    _Sw0657851MacTableStaticFilterVid_Type()
)
sw0657851MacTableStaticFilterVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticFilterVid.setStatus("current")
_Sw0657851MacTableStaticFilterAlias_Type = DisplayString
_Sw0657851MacTableStaticFilterAlias_Object = MibTableColumn
sw0657851MacTableStaticFilterAlias = _Sw0657851MacTableStaticFilterAlias_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 2, 3, 1, 4),
    _Sw0657851MacTableStaticFilterAlias_Type()
)
sw0657851MacTableStaticFilterAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticFilterAlias.setStatus("current")


class _Sw0657851MacTableStaticFilterEntryAction_Type(Integer32):
    """Custom type sw0657851MacTableStaticFilterEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Sw0657851MacTableStaticFilterEntryAction_Type.__name__ = "Integer32"
_Sw0657851MacTableStaticFilterEntryAction_Object = MibTableColumn
sw0657851MacTableStaticFilterEntryAction = _Sw0657851MacTableStaticFilterEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 2, 3, 1, 5),
    _Sw0657851MacTableStaticFilterEntryAction_Type()
)
sw0657851MacTableStaticFilterEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticFilterEntryAction.setStatus("current")
_Sw0657851MacTableStaticForward_ObjectIdentity = ObjectIdentity
sw0657851MacTableStaticForward = _Sw0657851MacTableStaticForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 3)
)


class _Sw0657851MacTableStaticForwardNumber_Type(Integer32):
    """Custom type sw0657851MacTableStaticForwardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Sw0657851MacTableStaticForwardNumber_Type.__name__ = "Integer32"
_Sw0657851MacTableStaticForwardNumber_Object = MibScalar
sw0657851MacTableStaticForwardNumber = _Sw0657851MacTableStaticForwardNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 3, 1),
    _Sw0657851MacTableStaticForwardNumber_Type()
)
sw0657851MacTableStaticForwardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticForwardNumber.setStatus("current")


class _Sw0657851MacTableStaticForwardEntryCreate_Type(Integer32):
    """Custom type sw0657851MacTableStaticForwardEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Sw0657851MacTableStaticForwardEntryCreate_Type.__name__ = "Integer32"
_Sw0657851MacTableStaticForwardEntryCreate_Object = MibScalar
sw0657851MacTableStaticForwardEntryCreate = _Sw0657851MacTableStaticForwardEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 3, 2),
    _Sw0657851MacTableStaticForwardEntryCreate_Type()
)
sw0657851MacTableStaticForwardEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticForwardEntryCreate.setStatus("current")
_Sw0657851MacTableStaticForwardTable_Object = MibTable
sw0657851MacTableStaticForwardTable = _Sw0657851MacTableStaticForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 3, 3)
)
if mibBuilder.loadTexts:
    sw0657851MacTableStaticForwardTable.setStatus("current")
_Sw0657851MacTableStaticForwardEntry_Object = MibTableRow
sw0657851MacTableStaticForwardEntry = _Sw0657851MacTableStaticForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 3, 3, 1)
)
sw0657851MacTableStaticForwardEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851MacTableStaticForwardIndex"),
)
if mibBuilder.loadTexts:
    sw0657851MacTableStaticForwardEntry.setStatus("current")


class _Sw0657851MacTableStaticForwardIndex_Type(Integer32):
    """Custom type sw0657851MacTableStaticForwardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Sw0657851MacTableStaticForwardIndex_Type.__name__ = "Integer32"
_Sw0657851MacTableStaticForwardIndex_Object = MibTableColumn
sw0657851MacTableStaticForwardIndex = _Sw0657851MacTableStaticForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 3, 3, 1, 1),
    _Sw0657851MacTableStaticForwardIndex_Type()
)
sw0657851MacTableStaticForwardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticForwardIndex.setStatus("current")
_Sw0657851MacTableStaticForwardMac_Type = DisplayString
_Sw0657851MacTableStaticForwardMac_Object = MibTableColumn
sw0657851MacTableStaticForwardMac = _Sw0657851MacTableStaticForwardMac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 3, 3, 1, 2),
    _Sw0657851MacTableStaticForwardMac_Type()
)
sw0657851MacTableStaticForwardMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticForwardMac.setStatus("current")


class _Sw0657851MacTableStaticForwardPort_Type(Integer32):
    """Custom type sw0657851MacTableStaticForwardPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851MacTableStaticForwardPort_Type.__name__ = "Integer32"
_Sw0657851MacTableStaticForwardPort_Object = MibTableColumn
sw0657851MacTableStaticForwardPort = _Sw0657851MacTableStaticForwardPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 3, 3, 1, 3),
    _Sw0657851MacTableStaticForwardPort_Type()
)
sw0657851MacTableStaticForwardPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticForwardPort.setStatus("current")


class _Sw0657851MacTableStaticForwardVid_Type(Integer32):
    """Custom type sw0657851MacTableStaticForwardVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851MacTableStaticForwardVid_Type.__name__ = "Integer32"
_Sw0657851MacTableStaticForwardVid_Object = MibTableColumn
sw0657851MacTableStaticForwardVid = _Sw0657851MacTableStaticForwardVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 3, 3, 1, 4),
    _Sw0657851MacTableStaticForwardVid_Type()
)
sw0657851MacTableStaticForwardVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticForwardVid.setStatus("current")
_Sw0657851MacTableStaticForwardAlias_Type = DisplayString
_Sw0657851MacTableStaticForwardAlias_Object = MibTableColumn
sw0657851MacTableStaticForwardAlias = _Sw0657851MacTableStaticForwardAlias_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 3, 3, 1, 5),
    _Sw0657851MacTableStaticForwardAlias_Type()
)
sw0657851MacTableStaticForwardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticForwardAlias.setStatus("current")


class _Sw0657851MacTableStaticForwardEntryAction_Type(Integer32):
    """Custom type sw0657851MacTableStaticForwardEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Sw0657851MacTableStaticForwardEntryAction_Type.__name__ = "Integer32"
_Sw0657851MacTableStaticForwardEntryAction_Object = MibTableColumn
sw0657851MacTableStaticForwardEntryAction = _Sw0657851MacTableStaticForwardEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 3, 3, 1, 6),
    _Sw0657851MacTableStaticForwardEntryAction_Type()
)
sw0657851MacTableStaticForwardEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacTableStaticForwardEntryAction.setStatus("current")
_Sw0657851MacAlias_ObjectIdentity = ObjectIdentity
sw0657851MacAlias = _Sw0657851MacAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 4)
)


class _Sw0657851MacAliasNumber_Type(Integer32):
    """Custom type sw0657851MacAliasNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Sw0657851MacAliasNumber_Type.__name__ = "Integer32"
_Sw0657851MacAliasNumber_Object = MibScalar
sw0657851MacAliasNumber = _Sw0657851MacAliasNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 4, 1),
    _Sw0657851MacAliasNumber_Type()
)
sw0657851MacAliasNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851MacAliasNumber.setStatus("current")


class _Sw0657851MacAliasEntryCreate_Type(Integer32):
    """Custom type sw0657851MacAliasEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Sw0657851MacAliasEntryCreate_Type.__name__ = "Integer32"
_Sw0657851MacAliasEntryCreate_Object = MibScalar
sw0657851MacAliasEntryCreate = _Sw0657851MacAliasEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 4, 2),
    _Sw0657851MacAliasEntryCreate_Type()
)
sw0657851MacAliasEntryCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851MacAliasEntryCreate.setStatus("current")
_Sw0657851MacAliasTable_Object = MibTable
sw0657851MacAliasTable = _Sw0657851MacAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 4, 3)
)
if mibBuilder.loadTexts:
    sw0657851MacAliasTable.setStatus("current")
_Sw0657851MacAliasEntry_Object = MibTableRow
sw0657851MacAliasEntry = _Sw0657851MacAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 4, 3, 1)
)
sw0657851MacAliasEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851MacAliasIndex"),
)
if mibBuilder.loadTexts:
    sw0657851MacAliasEntry.setStatus("current")


class _Sw0657851MacAliasIndex_Type(Integer32):
    """Custom type sw0657851MacAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Sw0657851MacAliasIndex_Type.__name__ = "Integer32"
_Sw0657851MacAliasIndex_Object = MibTableColumn
sw0657851MacAliasIndex = _Sw0657851MacAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 4, 3, 1, 1),
    _Sw0657851MacAliasIndex_Type()
)
sw0657851MacAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851MacAliasIndex.setStatus("current")
_Sw0657851AliasMac_Type = DisplayString
_Sw0657851AliasMac_Object = MibTableColumn
sw0657851AliasMac = _Sw0657851AliasMac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 4, 3, 1, 2),
    _Sw0657851AliasMac_Type()
)
sw0657851AliasMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AliasMac.setStatus("current")
_Sw0657851AliasName_Type = DisplayString
_Sw0657851AliasName_Object = MibTableColumn
sw0657851AliasName = _Sw0657851AliasName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 4, 3, 1, 3),
    _Sw0657851AliasName_Type()
)
sw0657851AliasName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AliasName.setStatus("current")


class _Sw0657851MacAliasEntryAction_Type(Integer32):
    """Custom type sw0657851MacAliasEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Sw0657851MacAliasEntryAction_Type.__name__ = "Integer32"
_Sw0657851MacAliasEntryAction_Object = MibTableColumn
sw0657851MacAliasEntryAction = _Sw0657851MacAliasEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 15, 4, 3, 1, 4),
    _Sw0657851MacAliasEntryAction_Type()
)
sw0657851MacAliasEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851MacAliasEntryAction.setStatus("current")
_Sw0657851GVRPInfo_ObjectIdentity = ObjectIdentity
sw0657851GVRPInfo = _Sw0657851GVRPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16)
)
_Sw0657851GvrpConf_ObjectIdentity = ObjectIdentity
sw0657851GvrpConf = _Sw0657851GvrpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 1)
)


class _Sw0657851GvrpConfState_Type(Integer32):
    """Custom type sw0657851GvrpConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851GvrpConfState_Type.__name__ = "Integer32"
_Sw0657851GvrpConfState_Object = MibScalar
sw0657851GvrpConfState = _Sw0657851GvrpConfState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 1, 1),
    _Sw0657851GvrpConfState_Type()
)
sw0657851GvrpConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851GvrpConfState.setStatus("current")
_Sw0657851GvrpConfTable_Object = MibTable
sw0657851GvrpConfTable = _Sw0657851GvrpConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    sw0657851GvrpConfTable.setStatus("current")
_Sw0657851GvrpConfEntry_Object = MibTableRow
sw0657851GvrpConfEntry = _Sw0657851GvrpConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 1, 2, 1)
)
sw0657851GvrpConfEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851GvrpConfIndex"),
)
if mibBuilder.loadTexts:
    sw0657851GvrpConfEntry.setStatus("current")


class _Sw0657851GvrpConfIndex_Type(Integer32):
    """Custom type sw0657851GvrpConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851GvrpConfIndex_Type.__name__ = "Integer32"
_Sw0657851GvrpConfIndex_Object = MibTableColumn
sw0657851GvrpConfIndex = _Sw0657851GvrpConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 1, 2, 1, 1),
    _Sw0657851GvrpConfIndex_Type()
)
sw0657851GvrpConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851GvrpConfIndex.setStatus("current")


class _Sw0657851GvrpConfJoinTime_Type(Integer32):
    """Custom type sw0657851GvrpConfJoinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_Sw0657851GvrpConfJoinTime_Type.__name__ = "Integer32"
_Sw0657851GvrpConfJoinTime_Object = MibTableColumn
sw0657851GvrpConfJoinTime = _Sw0657851GvrpConfJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 1, 2, 1, 2),
    _Sw0657851GvrpConfJoinTime_Type()
)
sw0657851GvrpConfJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851GvrpConfJoinTime.setStatus("current")


class _Sw0657851GvrpConfLeaveTime_Type(Integer32):
    """Custom type sw0657851GvrpConfLeaveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_Sw0657851GvrpConfLeaveTime_Type.__name__ = "Integer32"
_Sw0657851GvrpConfLeaveTime_Object = MibTableColumn
sw0657851GvrpConfLeaveTime = _Sw0657851GvrpConfLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 1, 2, 1, 3),
    _Sw0657851GvrpConfLeaveTime_Type()
)
sw0657851GvrpConfLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851GvrpConfLeaveTime.setStatus("current")


class _Sw0657851GvrpConfLeaveAllTime_Type(Integer32):
    """Custom type sw0657851GvrpConfLeaveAllTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 5000),
    )


_Sw0657851GvrpConfLeaveAllTime_Type.__name__ = "Integer32"
_Sw0657851GvrpConfLeaveAllTime_Object = MibTableColumn
sw0657851GvrpConfLeaveAllTime = _Sw0657851GvrpConfLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 1, 2, 1, 4),
    _Sw0657851GvrpConfLeaveAllTime_Type()
)
sw0657851GvrpConfLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851GvrpConfLeaveAllTime.setStatus("current")


class _Sw0657851GvrpConfDefaultAppMode_Type(Integer32):
    """Custom type sw0657851GvrpConfDefaultAppMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851GvrpConfDefaultAppMode_Type.__name__ = "Integer32"
_Sw0657851GvrpConfDefaultAppMode_Object = MibTableColumn
sw0657851GvrpConfDefaultAppMode = _Sw0657851GvrpConfDefaultAppMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 1, 2, 1, 5),
    _Sw0657851GvrpConfDefaultAppMode_Type()
)
sw0657851GvrpConfDefaultAppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851GvrpConfDefaultAppMode.setStatus("current")


class _Sw0657851GvrpConfDefaultRegMode_Type(Integer32):
    """Custom type sw0657851GvrpConfDefaultRegMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Sw0657851GvrpConfDefaultRegMode_Type.__name__ = "Integer32"
_Sw0657851GvrpConfDefaultRegMode_Object = MibTableColumn
sw0657851GvrpConfDefaultRegMode = _Sw0657851GvrpConfDefaultRegMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 1, 2, 1, 6),
    _Sw0657851GvrpConfDefaultRegMode_Type()
)
sw0657851GvrpConfDefaultRegMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851GvrpConfDefaultRegMode.setStatus("current")


class _Sw0657851GvrpConfRestrictedMode_Type(Integer32):
    """Custom type sw0657851GvrpConfRestrictedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851GvrpConfRestrictedMode_Type.__name__ = "Integer32"
_Sw0657851GvrpConfRestrictedMode_Object = MibTableColumn
sw0657851GvrpConfRestrictedMode = _Sw0657851GvrpConfRestrictedMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 1, 2, 1, 7),
    _Sw0657851GvrpConfRestrictedMode_Type()
)
sw0657851GvrpConfRestrictedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851GvrpConfRestrictedMode.setStatus("current")
_Sw0657851GvrpCounter_ObjectIdentity = ObjectIdentity
sw0657851GvrpCounter = _Sw0657851GvrpCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2)
)
_Sw0657851GvrpCounterTable_Object = MibTable
sw0657851GvrpCounterTable = _Sw0657851GvrpCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1)
)
if mibBuilder.loadTexts:
    sw0657851GvrpCounterTable.setStatus("current")
_Sw0657851GvrpCounterEntry_Object = MibTableRow
sw0657851GvrpCounterEntry = _Sw0657851GvrpCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1)
)
sw0657851GvrpCounterEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851GvrpCounterIndex"),
)
if mibBuilder.loadTexts:
    sw0657851GvrpCounterEntry.setStatus("current")


class _Sw0657851GvrpCounterIndex_Type(Integer32):
    """Custom type sw0657851GvrpCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851GvrpCounterIndex_Type.__name__ = "Integer32"
_Sw0657851GvrpCounterIndex_Object = MibTableColumn
sw0657851GvrpCounterIndex = _Sw0657851GvrpCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 1),
    _Sw0657851GvrpCounterIndex_Type()
)
sw0657851GvrpCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterIndex.setStatus("current")
_Sw0657851GvrpCounterRxTotalGvrpPkts_Type = Counter32
_Sw0657851GvrpCounterRxTotalGvrpPkts_Object = MibTableColumn
sw0657851GvrpCounterRxTotalGvrpPkts = _Sw0657851GvrpCounterRxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 2),
    _Sw0657851GvrpCounterRxTotalGvrpPkts_Type()
)
sw0657851GvrpCounterRxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterRxTotalGvrpPkts.setStatus("current")
_Sw0657851GvrpCounterRxInvalidGvrpPkts_Type = Counter32
_Sw0657851GvrpCounterRxInvalidGvrpPkts_Object = MibTableColumn
sw0657851GvrpCounterRxInvalidGvrpPkts = _Sw0657851GvrpCounterRxInvalidGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 3),
    _Sw0657851GvrpCounterRxInvalidGvrpPkts_Type()
)
sw0657851GvrpCounterRxInvalidGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterRxInvalidGvrpPkts.setStatus("current")
_Sw0657851GvrpCounterRxLeaveAllMsg_Type = Counter32
_Sw0657851GvrpCounterRxLeaveAllMsg_Object = MibTableColumn
sw0657851GvrpCounterRxLeaveAllMsg = _Sw0657851GvrpCounterRxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 4),
    _Sw0657851GvrpCounterRxLeaveAllMsg_Type()
)
sw0657851GvrpCounterRxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterRxLeaveAllMsg.setStatus("current")
_Sw0657851GvrpCounterRxJoinEmptyMsg_Type = Counter32
_Sw0657851GvrpCounterRxJoinEmptyMsg_Object = MibTableColumn
sw0657851GvrpCounterRxJoinEmptyMsg = _Sw0657851GvrpCounterRxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 5),
    _Sw0657851GvrpCounterRxJoinEmptyMsg_Type()
)
sw0657851GvrpCounterRxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterRxJoinEmptyMsg.setStatus("current")
_Sw0657851GvrpCounterRxJoinInMsg_Type = Counter32
_Sw0657851GvrpCounterRxJoinInMsg_Object = MibTableColumn
sw0657851GvrpCounterRxJoinInMsg = _Sw0657851GvrpCounterRxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 6),
    _Sw0657851GvrpCounterRxJoinInMsg_Type()
)
sw0657851GvrpCounterRxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterRxJoinInMsg.setStatus("current")
_Sw0657851GvrpCounterRxLeaveEmptyMsg_Type = Counter32
_Sw0657851GvrpCounterRxLeaveEmptyMsg_Object = MibTableColumn
sw0657851GvrpCounterRxLeaveEmptyMsg = _Sw0657851GvrpCounterRxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 7),
    _Sw0657851GvrpCounterRxLeaveEmptyMsg_Type()
)
sw0657851GvrpCounterRxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterRxLeaveEmptyMsg.setStatus("current")
_Sw0657851GvrpCounterRxEmptyMsg_Type = Counter32
_Sw0657851GvrpCounterRxEmptyMsg_Object = MibTableColumn
sw0657851GvrpCounterRxEmptyMsg = _Sw0657851GvrpCounterRxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 8),
    _Sw0657851GvrpCounterRxEmptyMsg_Type()
)
sw0657851GvrpCounterRxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterRxEmptyMsg.setStatus("current")
_Sw0657851GvrpCounterTxTotalGvrpPkts_Type = Counter32
_Sw0657851GvrpCounterTxTotalGvrpPkts_Object = MibTableColumn
sw0657851GvrpCounterTxTotalGvrpPkts = _Sw0657851GvrpCounterTxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 9),
    _Sw0657851GvrpCounterTxTotalGvrpPkts_Type()
)
sw0657851GvrpCounterTxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterTxTotalGvrpPkts.setStatus("current")
_Sw0657851GvrpCounterTxLeaveAllMsg_Type = Counter32
_Sw0657851GvrpCounterTxLeaveAllMsg_Object = MibTableColumn
sw0657851GvrpCounterTxLeaveAllMsg = _Sw0657851GvrpCounterTxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 10),
    _Sw0657851GvrpCounterTxLeaveAllMsg_Type()
)
sw0657851GvrpCounterTxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterTxLeaveAllMsg.setStatus("current")
_Sw0657851GvrpCounterTxJoinEmptyMsg_Type = Counter32
_Sw0657851GvrpCounterTxJoinEmptyMsg_Object = MibTableColumn
sw0657851GvrpCounterTxJoinEmptyMsg = _Sw0657851GvrpCounterTxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 11),
    _Sw0657851GvrpCounterTxJoinEmptyMsg_Type()
)
sw0657851GvrpCounterTxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterTxJoinEmptyMsg.setStatus("current")
_Sw0657851GvrpCounterTxJoinInMsg_Type = Counter32
_Sw0657851GvrpCounterTxJoinInMsg_Object = MibTableColumn
sw0657851GvrpCounterTxJoinInMsg = _Sw0657851GvrpCounterTxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 12),
    _Sw0657851GvrpCounterTxJoinInMsg_Type()
)
sw0657851GvrpCounterTxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterTxJoinInMsg.setStatus("current")
_Sw0657851GvrpCounterTxLeaveEmptyMsg_Type = Counter32
_Sw0657851GvrpCounterTxLeaveEmptyMsg_Object = MibTableColumn
sw0657851GvrpCounterTxLeaveEmptyMsg = _Sw0657851GvrpCounterTxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 13),
    _Sw0657851GvrpCounterTxLeaveEmptyMsg_Type()
)
sw0657851GvrpCounterTxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterTxLeaveEmptyMsg.setStatus("current")
_Sw0657851GvrpCounterTxEmptyMsg_Type = Counter32
_Sw0657851GvrpCounterTxEmptyMsg_Object = MibTableColumn
sw0657851GvrpCounterTxEmptyMsg = _Sw0657851GvrpCounterTxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 2, 1, 1, 14),
    _Sw0657851GvrpCounterTxEmptyMsg_Type()
)
sw0657851GvrpCounterTxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpCounterTxEmptyMsg.setStatus("current")
_Sw0657851GvrpGroup_ObjectIdentity = ObjectIdentity
sw0657851GvrpGroup = _Sw0657851GvrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3)
)


class _Sw0657851GvrpGroupNumber_Type(Integer32):
    """Custom type sw0657851GvrpGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Sw0657851GvrpGroupNumber_Type.__name__ = "Integer32"
_Sw0657851GvrpGroupNumber_Object = MibScalar
sw0657851GvrpGroupNumber = _Sw0657851GvrpGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 1),
    _Sw0657851GvrpGroupNumber_Type()
)
sw0657851GvrpGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpGroupNumber.setStatus("current")
_Sw0657851GvrpGroupTable_Object = MibTable
sw0657851GvrpGroupTable = _Sw0657851GvrpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 2)
)
if mibBuilder.loadTexts:
    sw0657851GvrpGroupTable.setStatus("current")
_Sw0657851GvrpGroupEntry_Object = MibTableRow
sw0657851GvrpGroupEntry = _Sw0657851GvrpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 2, 1)
)
sw0657851GvrpGroupEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851GvrpGroupId"),
)
if mibBuilder.loadTexts:
    sw0657851GvrpGroupEntry.setStatus("current")


class _Sw0657851GvrpGroupId_Type(Integer32):
    """Custom type sw0657851GvrpGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851GvrpGroupId_Type.__name__ = "Integer32"
_Sw0657851GvrpGroupId_Object = MibTableColumn
sw0657851GvrpGroupId = _Sw0657851GvrpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 2, 1, 1),
    _Sw0657851GvrpGroupId_Type()
)
sw0657851GvrpGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpGroupId.setStatus("current")


class _Sw0657851GvrpGroupVid_Type(Integer32):
    """Custom type sw0657851GvrpGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851GvrpGroupVid_Type.__name__ = "Integer32"
_Sw0657851GvrpGroupVid_Object = MibTableColumn
sw0657851GvrpGroupVid = _Sw0657851GvrpGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 2, 1, 2),
    _Sw0657851GvrpGroupVid_Type()
)
sw0657851GvrpGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpGroupVid.setStatus("current")
_Sw0657851GvrpGroupMemberPort_Type = DisplayString
_Sw0657851GvrpGroupMemberPort_Object = MibTableColumn
sw0657851GvrpGroupMemberPort = _Sw0657851GvrpGroupMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 2, 1, 3),
    _Sw0657851GvrpGroupMemberPort_Type()
)
sw0657851GvrpGroupMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpGroupMemberPort.setStatus("current")
_Sw0657851GvrpGroupAdministrativeCtrlTable_Object = MibTable
sw0657851GvrpGroupAdministrativeCtrlTable = _Sw0657851GvrpGroupAdministrativeCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 3)
)
if mibBuilder.loadTexts:
    sw0657851GvrpGroupAdministrativeCtrlTable.setStatus("current")
_Sw0657851GvrpGroupAdministrativeCtrlEntry_Object = MibTableRow
sw0657851GvrpGroupAdministrativeCtrlEntry = _Sw0657851GvrpGroupAdministrativeCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 3, 1)
)
sw0657851GvrpGroupAdministrativeCtrlEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851GvrpGroupAdministrativeCtrlVid"),
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851GvrpGroupAdministrativeCtrlPort"),
)
if mibBuilder.loadTexts:
    sw0657851GvrpGroupAdministrativeCtrlEntry.setStatus("current")


class _Sw0657851GvrpGroupAdministrativeCtrlVid_Type(Integer32):
    """Custom type sw0657851GvrpGroupAdministrativeCtrlVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851GvrpGroupAdministrativeCtrlVid_Type.__name__ = "Integer32"
_Sw0657851GvrpGroupAdministrativeCtrlVid_Object = MibTableColumn
sw0657851GvrpGroupAdministrativeCtrlVid = _Sw0657851GvrpGroupAdministrativeCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 3, 1, 1),
    _Sw0657851GvrpGroupAdministrativeCtrlVid_Type()
)
sw0657851GvrpGroupAdministrativeCtrlVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpGroupAdministrativeCtrlVid.setStatus("current")


class _Sw0657851GvrpGroupAdministrativeCtrlPort_Type(Integer32):
    """Custom type sw0657851GvrpGroupAdministrativeCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851GvrpGroupAdministrativeCtrlPort_Type.__name__ = "Integer32"
_Sw0657851GvrpGroupAdministrativeCtrlPort_Object = MibTableColumn
sw0657851GvrpGroupAdministrativeCtrlPort = _Sw0657851GvrpGroupAdministrativeCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 3, 1, 2),
    _Sw0657851GvrpGroupAdministrativeCtrlPort_Type()
)
sw0657851GvrpGroupAdministrativeCtrlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851GvrpGroupAdministrativeCtrlPort.setStatus("current")


class _Sw0657851GvrpGroupAdministrativeCtrlApp_Type(Integer32):
    """Custom type sw0657851GvrpGroupAdministrativeCtrlApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851GvrpGroupAdministrativeCtrlApp_Type.__name__ = "Integer32"
_Sw0657851GvrpGroupAdministrativeCtrlApp_Object = MibTableColumn
sw0657851GvrpGroupAdministrativeCtrlApp = _Sw0657851GvrpGroupAdministrativeCtrlApp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 3, 1, 3),
    _Sw0657851GvrpGroupAdministrativeCtrlApp_Type()
)
sw0657851GvrpGroupAdministrativeCtrlApp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851GvrpGroupAdministrativeCtrlApp.setStatus("current")


class _Sw0657851GvrpGroupAdministrativeCtrlReg_Type(Integer32):
    """Custom type sw0657851GvrpGroupAdministrativeCtrlReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Sw0657851GvrpGroupAdministrativeCtrlReg_Type.__name__ = "Integer32"
_Sw0657851GvrpGroupAdministrativeCtrlReg_Object = MibTableColumn
sw0657851GvrpGroupAdministrativeCtrlReg = _Sw0657851GvrpGroupAdministrativeCtrlReg_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 16, 3, 3, 1, 4),
    _Sw0657851GvrpGroupAdministrativeCtrlReg_Type()
)
sw0657851GvrpGroupAdministrativeCtrlReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851GvrpGroupAdministrativeCtrlReg.setStatus("current")
_Sw0657851QosInfo_ObjectIdentity = ObjectIdentity
sw0657851QosInfo = _Sw0657851QosInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17)
)
_Sw0657851QosPortConf_ObjectIdentity = ObjectIdentity
sw0657851QosPortConf = _Sw0657851QosPortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1)
)


class _Sw0657851QosNumOfClasses_Type(Integer32):
    """Custom type sw0657851QosNumOfClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_Sw0657851QosNumOfClasses_Type.__name__ = "Integer32"
_Sw0657851QosNumOfClasses_Object = MibScalar
sw0657851QosNumOfClasses = _Sw0657851QosNumOfClasses_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 1),
    _Sw0657851QosNumOfClasses_Type()
)
sw0657851QosNumOfClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosNumOfClasses.setStatus("current")
_Sw0657851QosPortConfTable_Object = MibTable
sw0657851QosPortConfTable = _Sw0657851QosPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 2)
)
if mibBuilder.loadTexts:
    sw0657851QosPortConfTable.setStatus("current")
_Sw0657851QosPortConfEntry_Object = MibTableRow
sw0657851QosPortConfEntry = _Sw0657851QosPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 2, 1)
)
sw0657851QosPortConfEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851QosPortConfIndex"),
)
if mibBuilder.loadTexts:
    sw0657851QosPortConfEntry.setStatus("current")


class _Sw0657851QosPortConfIndex_Type(Integer32):
    """Custom type sw0657851QosPortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851QosPortConfIndex_Type.__name__ = "Integer32"
_Sw0657851QosPortConfIndex_Object = MibTableColumn
sw0657851QosPortConfIndex = _Sw0657851QosPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 2, 1, 1),
    _Sw0657851QosPortConfIndex_Type()
)
sw0657851QosPortConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851QosPortConfIndex.setStatus("current")


class _Sw0657851QosPortConfDefaultClasses_Type(Integer32):
    """Custom type sw0657851QosPortConfDefaultClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Sw0657851QosPortConfDefaultClasses_Type.__name__ = "Integer32"
_Sw0657851QosPortConfDefaultClasses_Object = MibTableColumn
sw0657851QosPortConfDefaultClasses = _Sw0657851QosPortConfDefaultClasses_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 2, 1, 2),
    _Sw0657851QosPortConfDefaultClasses_Type()
)
sw0657851QosPortConfDefaultClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosPortConfDefaultClasses.setStatus("current")


class _Sw0657851QosPortConfQCL_Type(Integer32):
    """Custom type sw0657851QosPortConfQCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851QosPortConfQCL_Type.__name__ = "Integer32"
_Sw0657851QosPortConfQCL_Object = MibTableColumn
sw0657851QosPortConfQCL = _Sw0657851QosPortConfQCL_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 2, 1, 3),
    _Sw0657851QosPortConfQCL_Type()
)
sw0657851QosPortConfQCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosPortConfQCL.setStatus("current")


class _Sw0657851QosPortConfUserPriority_Type(Integer32):
    """Custom type sw0657851QosPortConfUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Sw0657851QosPortConfUserPriority_Type.__name__ = "Integer32"
_Sw0657851QosPortConfUserPriority_Object = MibTableColumn
sw0657851QosPortConfUserPriority = _Sw0657851QosPortConfUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 2, 1, 4),
    _Sw0657851QosPortConfUserPriority_Type()
)
sw0657851QosPortConfUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosPortConfUserPriority.setStatus("current")


class _Sw0657851QosPortConfQueuingMode_Type(Integer32):
    """Custom type sw0657851QosPortConfQueuingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851QosPortConfQueuingMode_Type.__name__ = "Integer32"
_Sw0657851QosPortConfQueuingMode_Object = MibTableColumn
sw0657851QosPortConfQueuingMode = _Sw0657851QosPortConfQueuingMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 2, 1, 5),
    _Sw0657851QosPortConfQueuingMode_Type()
)
sw0657851QosPortConfQueuingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosPortConfQueuingMode.setStatus("current")


class _Sw0657851QosPortConfQueueWeightedLow_Type(Integer32):
    """Custom type sw0657851QosPortConfQueueWeightedLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Sw0657851QosPortConfQueueWeightedLow_Type.__name__ = "Integer32"
_Sw0657851QosPortConfQueueWeightedLow_Object = MibTableColumn
sw0657851QosPortConfQueueWeightedLow = _Sw0657851QosPortConfQueueWeightedLow_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 2, 1, 6),
    _Sw0657851QosPortConfQueueWeightedLow_Type()
)
sw0657851QosPortConfQueueWeightedLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosPortConfQueueWeightedLow.setStatus("current")


class _Sw0657851QosPortConfQueueWeightedNormal_Type(Integer32):
    """Custom type sw0657851QosPortConfQueueWeightedNormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Sw0657851QosPortConfQueueWeightedNormal_Type.__name__ = "Integer32"
_Sw0657851QosPortConfQueueWeightedNormal_Object = MibTableColumn
sw0657851QosPortConfQueueWeightedNormal = _Sw0657851QosPortConfQueueWeightedNormal_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 2, 1, 7),
    _Sw0657851QosPortConfQueueWeightedNormal_Type()
)
sw0657851QosPortConfQueueWeightedNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosPortConfQueueWeightedNormal.setStatus("current")


class _Sw0657851QosPortConfQueueWeightedMedium_Type(Integer32):
    """Custom type sw0657851QosPortConfQueueWeightedMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Sw0657851QosPortConfQueueWeightedMedium_Type.__name__ = "Integer32"
_Sw0657851QosPortConfQueueWeightedMedium_Object = MibTableColumn
sw0657851QosPortConfQueueWeightedMedium = _Sw0657851QosPortConfQueueWeightedMedium_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 2, 1, 8),
    _Sw0657851QosPortConfQueueWeightedMedium_Type()
)
sw0657851QosPortConfQueueWeightedMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosPortConfQueueWeightedMedium.setStatus("current")


class _Sw0657851QosPortConfQueueWeightedHigh_Type(Integer32):
    """Custom type sw0657851QosPortConfQueueWeightedHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Sw0657851QosPortConfQueueWeightedHigh_Type.__name__ = "Integer32"
_Sw0657851QosPortConfQueueWeightedHigh_Object = MibTableColumn
sw0657851QosPortConfQueueWeightedHigh = _Sw0657851QosPortConfQueueWeightedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 1, 2, 1, 9),
    _Sw0657851QosPortConfQueueWeightedHigh_Type()
)
sw0657851QosPortConfQueueWeightedHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosPortConfQueueWeightedHigh.setStatus("current")
_Sw0657851QosRateLimiters_ObjectIdentity = ObjectIdentity
sw0657851QosRateLimiters = _Sw0657851QosRateLimiters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 3)
)
_Sw0657851QosRateLimitersTable_Object = MibTable
sw0657851QosRateLimitersTable = _Sw0657851QosRateLimitersTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    sw0657851QosRateLimitersTable.setStatus("current")
_Sw0657851QosRateLimitersEntry_Object = MibTableRow
sw0657851QosRateLimitersEntry = _Sw0657851QosRateLimitersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 3, 1, 1)
)
sw0657851QosRateLimitersEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851QosRateLimitersIndex"),
)
if mibBuilder.loadTexts:
    sw0657851QosRateLimitersEntry.setStatus("current")


class _Sw0657851QosRateLimitersIndex_Type(Integer32):
    """Custom type sw0657851QosRateLimitersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851QosRateLimitersIndex_Type.__name__ = "Integer32"
_Sw0657851QosRateLimitersIndex_Object = MibTableColumn
sw0657851QosRateLimitersIndex = _Sw0657851QosRateLimitersIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 3, 1, 1, 1),
    _Sw0657851QosRateLimitersIndex_Type()
)
sw0657851QosRateLimitersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851QosRateLimitersIndex.setStatus("current")


class _Sw0657851QosRateLimitersPolicer_Type(Integer32):
    """Custom type sw0657851QosRateLimitersPolicer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851QosRateLimitersPolicer_Type.__name__ = "Integer32"
_Sw0657851QosRateLimitersPolicer_Object = MibTableColumn
sw0657851QosRateLimitersPolicer = _Sw0657851QosRateLimitersPolicer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 3, 1, 1, 2),
    _Sw0657851QosRateLimitersPolicer_Type()
)
sw0657851QosRateLimitersPolicer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosRateLimitersPolicer.setStatus("current")


class _Sw0657851QosRateLimitersPolicerRate_Type(Integer32):
    """Custom type sw0657851QosRateLimitersPolicerRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Sw0657851QosRateLimitersPolicerRate_Type.__name__ = "Integer32"
_Sw0657851QosRateLimitersPolicerRate_Object = MibTableColumn
sw0657851QosRateLimitersPolicerRate = _Sw0657851QosRateLimitersPolicerRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 3, 1, 1, 3),
    _Sw0657851QosRateLimitersPolicerRate_Type()
)
sw0657851QosRateLimitersPolicerRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosRateLimitersPolicerRate.setStatus("current")


class _Sw0657851QosRateLimitersShaper_Type(Integer32):
    """Custom type sw0657851QosRateLimitersShaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851QosRateLimitersShaper_Type.__name__ = "Integer32"
_Sw0657851QosRateLimitersShaper_Object = MibTableColumn
sw0657851QosRateLimitersShaper = _Sw0657851QosRateLimitersShaper_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 3, 1, 1, 4),
    _Sw0657851QosRateLimitersShaper_Type()
)
sw0657851QosRateLimitersShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosRateLimitersShaper.setStatus("current")


class _Sw0657851QosRateLimitersShaperRate_Type(Integer32):
    """Custom type sw0657851QosRateLimitersShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Sw0657851QosRateLimitersShaperRate_Type.__name__ = "Integer32"
_Sw0657851QosRateLimitersShaperRate_Object = MibTableColumn
sw0657851QosRateLimitersShaperRate = _Sw0657851QosRateLimitersShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 3, 1, 1, 5),
    _Sw0657851QosRateLimitersShaperRate_Type()
)
sw0657851QosRateLimitersShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosRateLimitersShaperRate.setStatus("current")
_Sw0657851QosStormCtrl_ObjectIdentity = ObjectIdentity
sw0657851QosStormCtrl = _Sw0657851QosStormCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 4)
)


class _Sw0657851QosStromCtrlFloodedUnicastStatus_Type(Integer32):
    """Custom type sw0657851QosStromCtrlFloodedUnicastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851QosStromCtrlFloodedUnicastStatus_Type.__name__ = "Integer32"
_Sw0657851QosStromCtrlFloodedUnicastStatus_Object = MibScalar
sw0657851QosStromCtrlFloodedUnicastStatus = _Sw0657851QosStromCtrlFloodedUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 4, 1),
    _Sw0657851QosStromCtrlFloodedUnicastStatus_Type()
)
sw0657851QosStromCtrlFloodedUnicastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosStromCtrlFloodedUnicastStatus.setStatus("current")
_Sw0657851QosStromCtrlFloodedUnicastRate_Type = DisplayString
_Sw0657851QosStromCtrlFloodedUnicastRate_Object = MibScalar
sw0657851QosStromCtrlFloodedUnicastRate = _Sw0657851QosStromCtrlFloodedUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 4, 2),
    _Sw0657851QosStromCtrlFloodedUnicastRate_Type()
)
sw0657851QosStromCtrlFloodedUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosStromCtrlFloodedUnicastRate.setStatus("current")


class _Sw0657851QosStromCtrlMulticastStatus_Type(Integer32):
    """Custom type sw0657851QosStromCtrlMulticastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851QosStromCtrlMulticastStatus_Type.__name__ = "Integer32"
_Sw0657851QosStromCtrlMulticastStatus_Object = MibScalar
sw0657851QosStromCtrlMulticastStatus = _Sw0657851QosStromCtrlMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 4, 3),
    _Sw0657851QosStromCtrlMulticastStatus_Type()
)
sw0657851QosStromCtrlMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosStromCtrlMulticastStatus.setStatus("current")
_Sw0657851QosStromCtrlMulticastRate_Type = DisplayString
_Sw0657851QosStromCtrlMulticastRate_Object = MibScalar
sw0657851QosStromCtrlMulticastRate = _Sw0657851QosStromCtrlMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 4, 4),
    _Sw0657851QosStromCtrlMulticastRate_Type()
)
sw0657851QosStromCtrlMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosStromCtrlMulticastRate.setStatus("current")


class _Sw0657851QosStromCtrlBroadcastStatus_Type(Integer32):
    """Custom type sw0657851QosStromCtrlBroadcastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851QosStromCtrlBroadcastStatus_Type.__name__ = "Integer32"
_Sw0657851QosStromCtrlBroadcastStatus_Object = MibScalar
sw0657851QosStromCtrlBroadcastStatus = _Sw0657851QosStromCtrlBroadcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 4, 5),
    _Sw0657851QosStromCtrlBroadcastStatus_Type()
)
sw0657851QosStromCtrlBroadcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosStromCtrlBroadcastStatus.setStatus("current")
_Sw0657851QosStromCtrlBroadcastRate_Type = DisplayString
_Sw0657851QosStromCtrlBroadcastRate_Object = MibScalar
sw0657851QosStromCtrlBroadcastRate = _Sw0657851QosStromCtrlBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 17, 4, 6),
    _Sw0657851QosStromCtrlBroadcastRate_Type()
)
sw0657851QosStromCtrlBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851QosStromCtrlBroadcastRate.setStatus("current")
_Sw0657851AclInfo_ObjectIdentity = ObjectIdentity
sw0657851AclInfo = _Sw0657851AclInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18)
)
_Sw0657851AclPortsConfTable_Object = MibTable
sw0657851AclPortsConfTable = _Sw0657851AclPortsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 1)
)
if mibBuilder.loadTexts:
    sw0657851AclPortsConfTable.setStatus("current")
_Sw0657851AclPortsConfEntry_Object = MibTableRow
sw0657851AclPortsConfEntry = _Sw0657851AclPortsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 1, 1)
)
sw0657851AclPortsConfEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851AclPortsConfIndex"),
)
if mibBuilder.loadTexts:
    sw0657851AclPortsConfEntry.setStatus("current")


class _Sw0657851AclPortsConfIndex_Type(Integer32):
    """Custom type sw0657851AclPortsConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851AclPortsConfIndex_Type.__name__ = "Integer32"
_Sw0657851AclPortsConfIndex_Object = MibTableColumn
sw0657851AclPortsConfIndex = _Sw0657851AclPortsConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 1, 1, 1),
    _Sw0657851AclPortsConfIndex_Type()
)
sw0657851AclPortsConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851AclPortsConfIndex.setStatus("current")


class _Sw0657851AclPortsConfPolicyId_Type(Integer32):
    """Custom type sw0657851AclPortsConfPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Sw0657851AclPortsConfPolicyId_Type.__name__ = "Integer32"
_Sw0657851AclPortsConfPolicyId_Object = MibTableColumn
sw0657851AclPortsConfPolicyId = _Sw0657851AclPortsConfPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 1, 1, 2),
    _Sw0657851AclPortsConfPolicyId_Type()
)
sw0657851AclPortsConfPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AclPortsConfPolicyId.setStatus("current")


class _Sw0657851AclPortsConfAction_Type(Integer32):
    """Custom type sw0657851AclPortsConfAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851AclPortsConfAction_Type.__name__ = "Integer32"
_Sw0657851AclPortsConfAction_Object = MibTableColumn
sw0657851AclPortsConfAction = _Sw0657851AclPortsConfAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 1, 1, 3),
    _Sw0657851AclPortsConfAction_Type()
)
sw0657851AclPortsConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AclPortsConfAction.setStatus("current")


class _Sw0657851AclPortsConfRateLimiterId_Type(Integer32):
    """Custom type sw0657851AclPortsConfRateLimiterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Sw0657851AclPortsConfRateLimiterId_Type.__name__ = "Integer32"
_Sw0657851AclPortsConfRateLimiterId_Object = MibTableColumn
sw0657851AclPortsConfRateLimiterId = _Sw0657851AclPortsConfRateLimiterId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 1, 1, 4),
    _Sw0657851AclPortsConfRateLimiterId_Type()
)
sw0657851AclPortsConfRateLimiterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AclPortsConfRateLimiterId.setStatus("current")


class _Sw0657851AclPortsConfPortCopy_Type(Integer32):
    """Custom type sw0657851AclPortsConfPortCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Sw0657851AclPortsConfPortCopy_Type.__name__ = "Integer32"
_Sw0657851AclPortsConfPortCopy_Object = MibTableColumn
sw0657851AclPortsConfPortCopy = _Sw0657851AclPortsConfPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 1, 1, 5),
    _Sw0657851AclPortsConfPortCopy_Type()
)
sw0657851AclPortsConfPortCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AclPortsConfPortCopy.setStatus("current")
_Sw0657851AclPortsConfCounter_Type = Counter32
_Sw0657851AclPortsConfCounter_Object = MibTableColumn
sw0657851AclPortsConfCounter = _Sw0657851AclPortsConfCounter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 1, 1, 6),
    _Sw0657851AclPortsConfCounter_Type()
)
sw0657851AclPortsConfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851AclPortsConfCounter.setStatus("current")
_Sw0657851AclRateLimiter_ObjectIdentity = ObjectIdentity
sw0657851AclRateLimiter = _Sw0657851AclRateLimiter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 2)
)
_Sw0657851AclRateLimiterTable_Object = MibTable
sw0657851AclRateLimiterTable = _Sw0657851AclRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    sw0657851AclRateLimiterTable.setStatus("current")
_Sw0657851AclRateLimiterEntry_Object = MibTableRow
sw0657851AclRateLimiterEntry = _Sw0657851AclRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 2, 1, 1)
)
sw0657851AclRateLimiterEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851AclRateLimiterIndex"),
)
if mibBuilder.loadTexts:
    sw0657851AclRateLimiterEntry.setStatus("current")


class _Sw0657851AclRateLimiterIndex_Type(Integer32):
    """Custom type sw0657851AclRateLimiterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851AclRateLimiterIndex_Type.__name__ = "Integer32"
_Sw0657851AclRateLimiterIndex_Object = MibTableColumn
sw0657851AclRateLimiterIndex = _Sw0657851AclRateLimiterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 2, 1, 1, 1),
    _Sw0657851AclRateLimiterIndex_Type()
)
sw0657851AclRateLimiterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851AclRateLimiterIndex.setStatus("current")
_Sw0657851AclRateLimiterRate_Type = DisplayString
_Sw0657851AclRateLimiterRate_Object = MibTableColumn
sw0657851AclRateLimiterRate = _Sw0657851AclRateLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 18, 2, 1, 1, 2),
    _Sw0657851AclRateLimiterRate_Type()
)
sw0657851AclRateLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851AclRateLimiterRate.setStatus("current")
_Sw0657851IpMacBind_ObjectIdentity = ObjectIdentity
sw0657851IpMacBind = _Sw0657851IpMacBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19)
)
_Sw0657851IpMacBindConf_ObjectIdentity = ObjectIdentity
sw0657851IpMacBindConf = _Sw0657851IpMacBindConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 1)
)


class _Sw0657851IpMacBindstate_Type(Integer32):
    """Custom type sw0657851IpMacBindstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851IpMacBindstate_Type.__name__ = "Integer32"
_Sw0657851IpMacBindstate_Object = MibScalar
sw0657851IpMacBindstate = _Sw0657851IpMacBindstate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 1, 1),
    _Sw0657851IpMacBindstate_Type()
)
sw0657851IpMacBindstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IpMacBindstate.setStatus("current")
_Sw0657851IpMacBindTrustPort_Type = DisplayString
_Sw0657851IpMacBindTrustPort_Object = MibScalar
sw0657851IpMacBindTrustPort = _Sw0657851IpMacBindTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 1, 2),
    _Sw0657851IpMacBindTrustPort_Type()
)
sw0657851IpMacBindTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IpMacBindTrustPort.setStatus("current")
_Sw0657851IpMacBindSetting_ObjectIdentity = ObjectIdentity
sw0657851IpMacBindSetting = _Sw0657851IpMacBindSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 2)
)


class _Sw0657851IpMacBindSettingNumber_Type(Integer32):
    """Custom type sw0657851IpMacBindSettingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Sw0657851IpMacBindSettingNumber_Type.__name__ = "Integer32"
_Sw0657851IpMacBindSettingNumber_Object = MibScalar
sw0657851IpMacBindSettingNumber = _Sw0657851IpMacBindSettingNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 2, 1),
    _Sw0657851IpMacBindSettingNumber_Type()
)
sw0657851IpMacBindSettingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IpMacBindSettingNumber.setStatus("current")


class _Sw0657851IpMacBindSettingEntryCreate_Type(Integer32):
    """Custom type sw0657851IpMacBindSettingEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Sw0657851IpMacBindSettingEntryCreate_Type.__name__ = "Integer32"
_Sw0657851IpMacBindSettingEntryCreate_Object = MibScalar
sw0657851IpMacBindSettingEntryCreate = _Sw0657851IpMacBindSettingEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 2, 2),
    _Sw0657851IpMacBindSettingEntryCreate_Type()
)
sw0657851IpMacBindSettingEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IpMacBindSettingEntryCreate.setStatus("current")
_Sw0657851IpMacBindSettingTable_Object = MibTable
sw0657851IpMacBindSettingTable = _Sw0657851IpMacBindSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 2, 3)
)
if mibBuilder.loadTexts:
    sw0657851IpMacBindSettingTable.setStatus("current")
_Sw0657851IpMacBindSettingEntry_Object = MibTableRow
sw0657851IpMacBindSettingEntry = _Sw0657851IpMacBindSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 2, 3, 1)
)
sw0657851IpMacBindSettingEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851IpMacBindSettingIndex"),
)
if mibBuilder.loadTexts:
    sw0657851IpMacBindSettingEntry.setStatus("current")


class _Sw0657851IpMacBindSettingIndex_Type(Integer32):
    """Custom type sw0657851IpMacBindSettingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Sw0657851IpMacBindSettingIndex_Type.__name__ = "Integer32"
_Sw0657851IpMacBindSettingIndex_Object = MibTableColumn
sw0657851IpMacBindSettingIndex = _Sw0657851IpMacBindSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 2, 3, 1, 1),
    _Sw0657851IpMacBindSettingIndex_Type()
)
sw0657851IpMacBindSettingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851IpMacBindSettingIndex.setStatus("current")
_Sw0657851IpMacBindSettingMAC_Type = DisplayString
_Sw0657851IpMacBindSettingMAC_Object = MibTableColumn
sw0657851IpMacBindSettingMAC = _Sw0657851IpMacBindSettingMAC_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 2, 3, 1, 2),
    _Sw0657851IpMacBindSettingMAC_Type()
)
sw0657851IpMacBindSettingMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IpMacBindSettingMAC.setStatus("current")
_Sw0657851IpMacBindSettingIP_Type = IpAddress
_Sw0657851IpMacBindSettingIP_Object = MibTableColumn
sw0657851IpMacBindSettingIP = _Sw0657851IpMacBindSettingIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 2, 3, 1, 3),
    _Sw0657851IpMacBindSettingIP_Type()
)
sw0657851IpMacBindSettingIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IpMacBindSettingIP.setStatus("current")


class _Sw0657851IpMacBindSettingPort_Type(Integer32):
    """Custom type sw0657851IpMacBindSettingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851IpMacBindSettingPort_Type.__name__ = "Integer32"
_Sw0657851IpMacBindSettingPort_Object = MibTableColumn
sw0657851IpMacBindSettingPort = _Sw0657851IpMacBindSettingPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 2, 3, 1, 4),
    _Sw0657851IpMacBindSettingPort_Type()
)
sw0657851IpMacBindSettingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IpMacBindSettingPort.setStatus("current")


class _Sw0657851IpMacBindSettingVID_Type(Integer32):
    """Custom type sw0657851IpMacBindSettingVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851IpMacBindSettingVID_Type.__name__ = "Integer32"
_Sw0657851IpMacBindSettingVID_Object = MibTableColumn
sw0657851IpMacBindSettingVID = _Sw0657851IpMacBindSettingVID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 2, 3, 1, 5),
    _Sw0657851IpMacBindSettingVID_Type()
)
sw0657851IpMacBindSettingVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IpMacBindSettingVID.setStatus("current")


class _Sw0657851IpMacBindSettingEntryAction_Type(Integer32):
    """Custom type sw0657851IpMacBindSettingEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Sw0657851IpMacBindSettingEntryAction_Type.__name__ = "Integer32"
_Sw0657851IpMacBindSettingEntryAction_Object = MibTableColumn
sw0657851IpMacBindSettingEntryAction = _Sw0657851IpMacBindSettingEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 19, 2, 3, 1, 6),
    _Sw0657851IpMacBindSettingEntryAction_Type()
)
sw0657851IpMacBindSettingEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IpMacBindSettingEntryAction.setStatus("current")
_Sw0657851TrapEntry_ObjectIdentity = ObjectIdentity
sw0657851TrapEntry = _Sw0657851TrapEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20)
)
_Sw0657851TrapVariable_ObjectIdentity = ObjectIdentity
sw0657851TrapVariable = _Sw0657851TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 22)
)
_Username_Type = DisplayString
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 22, 1),
    _Username_Type()
)
username.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    username.setStatus("current")


class _GroupId_Type(Integer32):
    """Custom type groupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GroupId_Type.__name__ = "Integer32"
_GroupId_Object = MibScalar
groupId = _GroupId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 22, 2),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 22, 3),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 22, 4),
    _Partnerkey_Type()
)
partnerkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerkey.setStatus("current")
_Uplink_Type = DisplayString
_Uplink_Object = MibScalar
uplink = _Uplink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 22, 5),
    _Uplink_Type()
)
uplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplink.setStatus("current")
_IpmacIp_Type = DisplayString
_IpmacIp_Object = MibScalar
ipmacIp = _IpmacIp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 22, 7),
    _IpmacIp_Type()
)
ipmacIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmacIp.setStatus("current")
_IpmacMac_Type = DisplayString
_IpmacMac_Object = MibScalar
ipmacMac = _IpmacMac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 22, 8),
    _IpmacMac_Type()
)
ipmacMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmacMac.setStatus("current")
_IpmacClientIp_Type = DisplayString
_IpmacClientIp_Object = MibScalar
ipmacClientIp = _IpmacClientIp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 22, 9),
    _IpmacClientIp_Type()
)
ipmacClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmacClientIp.setStatus("current")
_IpmacClientMac_Type = DisplayString
_IpmacClientMac_Object = MibScalar
ipmacClientMac = _IpmacClientMac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 22, 10),
    _IpmacClientMac_Type()
)
ipmacClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmacClientMac.setStatus("current")
_IpmacServerIp_Type = DisplayString
_IpmacServerIp_Object = MibScalar
ipmacServerIp = _IpmacServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 22, 11),
    _IpmacServerIp_Type()
)
ipmacServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmacServerIp.setStatus("current")
_Sw0657851Dot1X_ObjectIdentity = ObjectIdentity
sw0657851Dot1X = _Sw0657851Dot1X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23)
)
_Sw0657851Dot1XServerConf_ObjectIdentity = ObjectIdentity
sw0657851Dot1XServerConf = _Sw0657851Dot1XServerConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 1)
)
_Sw0657851Dot1XServerConfAuthenticationServerIp_Type = IpAddress
_Sw0657851Dot1XServerConfAuthenticationServerIp_Object = MibScalar
sw0657851Dot1XServerConfAuthenticationServerIp = _Sw0657851Dot1XServerConfAuthenticationServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 1, 1),
    _Sw0657851Dot1XServerConfAuthenticationServerIp_Type()
)
sw0657851Dot1XServerConfAuthenticationServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XServerConfAuthenticationServerIp.setStatus("current")


class _Sw0657851Dot1XServerConfAuthenticationUdpPort_Type(Integer32):
    """Custom type sw0657851Dot1XServerConfAuthenticationUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Sw0657851Dot1XServerConfAuthenticationUdpPort_Type.__name__ = "Integer32"
_Sw0657851Dot1XServerConfAuthenticationUdpPort_Object = MibScalar
sw0657851Dot1XServerConfAuthenticationUdpPort = _Sw0657851Dot1XServerConfAuthenticationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 1, 2),
    _Sw0657851Dot1XServerConfAuthenticationUdpPort_Type()
)
sw0657851Dot1XServerConfAuthenticationUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XServerConfAuthenticationUdpPort.setStatus("current")
_Sw0657851Dot1XServerConfAuthenticationSecretKey_Type = DisplayString
_Sw0657851Dot1XServerConfAuthenticationSecretKey_Object = MibScalar
sw0657851Dot1XServerConfAuthenticationSecretKey = _Sw0657851Dot1XServerConfAuthenticationSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 1, 3),
    _Sw0657851Dot1XServerConfAuthenticationSecretKey_Type()
)
sw0657851Dot1XServerConfAuthenticationSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XServerConfAuthenticationSecretKey.setStatus("current")
_Sw0657851Dot1XServerConfAccountingServerIp_Type = IpAddress
_Sw0657851Dot1XServerConfAccountingServerIp_Object = MibScalar
sw0657851Dot1XServerConfAccountingServerIp = _Sw0657851Dot1XServerConfAccountingServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 1, 4),
    _Sw0657851Dot1XServerConfAccountingServerIp_Type()
)
sw0657851Dot1XServerConfAccountingServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XServerConfAccountingServerIp.setStatus("current")


class _Sw0657851Dot1XServerConfAccountingUdpPort_Type(Integer32):
    """Custom type sw0657851Dot1XServerConfAccountingUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Sw0657851Dot1XServerConfAccountingUdpPort_Type.__name__ = "Integer32"
_Sw0657851Dot1XServerConfAccountingUdpPort_Object = MibScalar
sw0657851Dot1XServerConfAccountingUdpPort = _Sw0657851Dot1XServerConfAccountingUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 1, 5),
    _Sw0657851Dot1XServerConfAccountingUdpPort_Type()
)
sw0657851Dot1XServerConfAccountingUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XServerConfAccountingUdpPort.setStatus("current")
_Sw0657851Dot1XServerConfAccountingSecretKey_Type = DisplayString
_Sw0657851Dot1XServerConfAccountingSecretKey_Object = MibScalar
sw0657851Dot1XServerConfAccountingSecretKey = _Sw0657851Dot1XServerConfAccountingSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 1, 6),
    _Sw0657851Dot1XServerConfAccountingSecretKey_Type()
)
sw0657851Dot1XServerConfAccountingSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XServerConfAccountingSecretKey.setStatus("current")
_Sw0657851Dot1XPortConfTable_Object = MibTable
sw0657851Dot1XPortConfTable = _Sw0657851Dot1XPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2)
)
if mibBuilder.loadTexts:
    sw0657851Dot1XPortConfTable.setStatus("current")
_Sw0657851Dot1XPortConfEntry_Object = MibTableRow
sw0657851Dot1XPortConfEntry = _Sw0657851Dot1XPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1)
)
sw0657851Dot1XPortConfEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851Dot1XPort"),
)
if mibBuilder.loadTexts:
    sw0657851Dot1XPortConfEntry.setStatus("current")


class _Sw0657851Dot1XPort_Type(Integer32):
    """Custom type sw0657851Dot1XPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851Dot1XPort_Type.__name__ = "Integer32"
_Sw0657851Dot1XPort_Object = MibTableColumn
sw0657851Dot1XPort = _Sw0657851Dot1XPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1, 1),
    _Sw0657851Dot1XPort_Type()
)
sw0657851Dot1XPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XPort.setStatus("current")


class _Sw0657851Dot1XPortMode_Type(Integer32):
    """Custom type sw0657851Dot1XPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Sw0657851Dot1XPortMode_Type.__name__ = "Integer32"
_Sw0657851Dot1XPortMode_Object = MibTableColumn
sw0657851Dot1XPortMode = _Sw0657851Dot1XPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1, 2),
    _Sw0657851Dot1XPortMode_Type()
)
sw0657851Dot1XPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XPortMode.setStatus("current")


class _Sw0657851Dot1XPortControl_Type(Integer32):
    """Custom type sw0657851Dot1XPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Sw0657851Dot1XPortControl_Type.__name__ = "Integer32"
_Sw0657851Dot1XPortControl_Object = MibTableColumn
sw0657851Dot1XPortControl = _Sw0657851Dot1XPortControl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1, 3),
    _Sw0657851Dot1XPortControl_Type()
)
sw0657851Dot1XPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XPortControl.setStatus("current")


class _Sw0657851Dot1XPortreAuthMax_Type(Integer32):
    """Custom type sw0657851Dot1XPortreAuthMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Sw0657851Dot1XPortreAuthMax_Type.__name__ = "Integer32"
_Sw0657851Dot1XPortreAuthMax_Object = MibTableColumn
sw0657851Dot1XPortreAuthMax = _Sw0657851Dot1XPortreAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1, 4),
    _Sw0657851Dot1XPortreAuthMax_Type()
)
sw0657851Dot1XPortreAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XPortreAuthMax.setStatus("current")


class _Sw0657851Dot1XPorttxPeriod_Type(Integer32):
    """Custom type sw0657851Dot1XPorttxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Sw0657851Dot1XPorttxPeriod_Type.__name__ = "Integer32"
_Sw0657851Dot1XPorttxPeriod_Object = MibTableColumn
sw0657851Dot1XPorttxPeriod = _Sw0657851Dot1XPorttxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1, 5),
    _Sw0657851Dot1XPorttxPeriod_Type()
)
sw0657851Dot1XPorttxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XPorttxPeriod.setStatus("current")


class _Sw0657851Dot1XPortquietPeriod_Type(Integer32):
    """Custom type sw0657851Dot1XPortquietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Sw0657851Dot1XPortquietPeriod_Type.__name__ = "Integer32"
_Sw0657851Dot1XPortquietPeriod_Object = MibTableColumn
sw0657851Dot1XPortquietPeriod = _Sw0657851Dot1XPortquietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1, 6),
    _Sw0657851Dot1XPortquietPeriod_Type()
)
sw0657851Dot1XPortquietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XPortquietPeriod.setStatus("current")


class _Sw0657851Dot1XPortreAuthEnabled_Type(Integer32):
    """Custom type sw0657851Dot1XPortreAuthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851Dot1XPortreAuthEnabled_Type.__name__ = "Integer32"
_Sw0657851Dot1XPortreAuthEnabled_Object = MibTableColumn
sw0657851Dot1XPortreAuthEnabled = _Sw0657851Dot1XPortreAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1, 7),
    _Sw0657851Dot1XPortreAuthEnabled_Type()
)
sw0657851Dot1XPortreAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XPortreAuthEnabled.setStatus("current")


class _Sw0657851Dot1XPortreAuthPeriod_Type(Integer32):
    """Custom type sw0657851Dot1XPortreAuthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Sw0657851Dot1XPortreAuthPeriod_Type.__name__ = "Integer32"
_Sw0657851Dot1XPortreAuthPeriod_Object = MibTableColumn
sw0657851Dot1XPortreAuthPeriod = _Sw0657851Dot1XPortreAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1, 8),
    _Sw0657851Dot1XPortreAuthPeriod_Type()
)
sw0657851Dot1XPortreAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XPortreAuthPeriod.setStatus("current")


class _Sw0657851Dot1XPortmaxReq_Type(Integer32):
    """Custom type sw0657851Dot1XPortmaxReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Sw0657851Dot1XPortmaxReq_Type.__name__ = "Integer32"
_Sw0657851Dot1XPortmaxReq_Object = MibTableColumn
sw0657851Dot1XPortmaxReq = _Sw0657851Dot1XPortmaxReq_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1, 9),
    _Sw0657851Dot1XPortmaxReq_Type()
)
sw0657851Dot1XPortmaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XPortmaxReq.setStatus("current")


class _Sw0657851Dot1XPortsuppTimeout_Type(Integer32):
    """Custom type sw0657851Dot1XPortsuppTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Sw0657851Dot1XPortsuppTimeout_Type.__name__ = "Integer32"
_Sw0657851Dot1XPortsuppTimeout_Object = MibTableColumn
sw0657851Dot1XPortsuppTimeout = _Sw0657851Dot1XPortsuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1, 10),
    _Sw0657851Dot1XPortsuppTimeout_Type()
)
sw0657851Dot1XPortsuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XPortsuppTimeout.setStatus("current")


class _Sw0657851Dot1XPortserverTimeout_Type(Integer32):
    """Custom type sw0657851Dot1XPortserverTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Sw0657851Dot1XPortserverTimeout_Type.__name__ = "Integer32"
_Sw0657851Dot1XPortserverTimeout_Object = MibTableColumn
sw0657851Dot1XPortserverTimeout = _Sw0657851Dot1XPortserverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 2, 1, 11),
    _Sw0657851Dot1XPortserverTimeout_Type()
)
sw0657851Dot1XPortserverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XPortserverTimeout.setStatus("current")
_Sw0657851Dot1XStatusTable_Object = MibTable
sw0657851Dot1XStatusTable = _Sw0657851Dot1XStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 3)
)
if mibBuilder.loadTexts:
    sw0657851Dot1XStatusTable.setStatus("current")
_Sw0657851Dot1XStatusEntry_Object = MibTableRow
sw0657851Dot1XStatusEntry = _Sw0657851Dot1XStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 3, 1)
)
sw0657851Dot1XStatusEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851Dot1XStatusIndex"),
)
if mibBuilder.loadTexts:
    sw0657851Dot1XStatusEntry.setStatus("current")


class _Sw0657851Dot1XStatusIndex_Type(Integer32):
    """Custom type sw0657851Dot1XStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851Dot1XStatusIndex_Type.__name__ = "Integer32"
_Sw0657851Dot1XStatusIndex_Object = MibTableColumn
sw0657851Dot1XStatusIndex = _Sw0657851Dot1XStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 3, 1, 1),
    _Sw0657851Dot1XStatusIndex_Type()
)
sw0657851Dot1XStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851Dot1XStatusIndex.setStatus("current")
_Sw0657851Dot1XStatusMode_Type = DisplayString
_Sw0657851Dot1XStatusMode_Object = MibTableColumn
sw0657851Dot1XStatusMode = _Sw0657851Dot1XStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 3, 1, 2),
    _Sw0657851Dot1XStatusMode_Type()
)
sw0657851Dot1XStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XStatusMode.setStatus("current")
_Sw0657851Dot1XStatusStatus_Type = DisplayString
_Sw0657851Dot1XStatusStatus_Object = MibTableColumn
sw0657851Dot1XStatusStatus = _Sw0657851Dot1XStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 3, 1, 3),
    _Sw0657851Dot1XStatusStatus_Type()
)
sw0657851Dot1XStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XStatusStatus.setStatus("current")
_Sw0657851Dot1XStatisticsTable_Object = MibTable
sw0657851Dot1XStatisticsTable = _Sw0657851Dot1XStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4)
)
if mibBuilder.loadTexts:
    sw0657851Dot1XStatisticsTable.setStatus("current")
_Sw0657851Dot1XStatisticsEntry_Object = MibTableRow
sw0657851Dot1XStatisticsEntry = _Sw0657851Dot1XStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1)
)
sw0657851Dot1XStatisticsEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851Dot1XStatisticsIndex"),
)
if mibBuilder.loadTexts:
    sw0657851Dot1XStatisticsEntry.setStatus("current")


class _Sw0657851Dot1XStatisticsIndex_Type(Integer32):
    """Custom type sw0657851Dot1XStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851Dot1XStatisticsIndex_Type.__name__ = "Integer32"
_Sw0657851Dot1XStatisticsIndex_Object = MibTableColumn
sw0657851Dot1XStatisticsIndex = _Sw0657851Dot1XStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 1),
    _Sw0657851Dot1XStatisticsIndex_Type()
)
sw0657851Dot1XStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851Dot1XStatisticsIndex.setStatus("current")


class _Sw0657851Dot1XClearCounter_Type(Integer32):
    """Custom type sw0657851Dot1XClearCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851Dot1XClearCounter_Type.__name__ = "Integer32"
_Sw0657851Dot1XClearCounter_Object = MibTableColumn
sw0657851Dot1XClearCounter = _Sw0657851Dot1XClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 2),
    _Sw0657851Dot1XClearCounter_Type()
)
sw0657851Dot1XClearCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851Dot1XClearCounter.setStatus("current")
_Sw0657851Dot1XAuthEntersConnecting_Type = Counter32
_Sw0657851Dot1XAuthEntersConnecting_Object = MibTableColumn
sw0657851Dot1XAuthEntersConnecting = _Sw0657851Dot1XAuthEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 3),
    _Sw0657851Dot1XAuthEntersConnecting_Type()
)
sw0657851Dot1XAuthEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthEntersConnecting.setStatus("current")
_Sw0657851Dot1XauthEapLogoffsWhileConnecting_Type = Counter32
_Sw0657851Dot1XauthEapLogoffsWhileConnecting_Object = MibTableColumn
sw0657851Dot1XauthEapLogoffsWhileConnecting = _Sw0657851Dot1XauthEapLogoffsWhileConnecting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 4),
    _Sw0657851Dot1XauthEapLogoffsWhileConnecting_Type()
)
sw0657851Dot1XauthEapLogoffsWhileConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XauthEapLogoffsWhileConnecting.setStatus("current")
_Sw0657851Dot1XAuthEntersAuthenticating_Type = Counter32
_Sw0657851Dot1XAuthEntersAuthenticating_Object = MibTableColumn
sw0657851Dot1XAuthEntersAuthenticating = _Sw0657851Dot1XAuthEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 5),
    _Sw0657851Dot1XAuthEntersAuthenticating_Type()
)
sw0657851Dot1XAuthEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthEntersAuthenticating.setStatus("current")
_Sw0657851Dot1XAuthAuthSuccessesWhileAuthenticating_Type = Counter32
_Sw0657851Dot1XAuthAuthSuccessesWhileAuthenticating_Object = MibTableColumn
sw0657851Dot1XAuthAuthSuccessesWhileAuthenticating = _Sw0657851Dot1XAuthAuthSuccessesWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 6),
    _Sw0657851Dot1XAuthAuthSuccessesWhileAuthenticating_Type()
)
sw0657851Dot1XAuthAuthSuccessesWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthAuthSuccessesWhileAuthenticating.setStatus("current")
_Sw0657851Dot1XAuthAuthTimeoutsWhileAuthenticating_Type = Counter32
_Sw0657851Dot1XAuthAuthTimeoutsWhileAuthenticating_Object = MibTableColumn
sw0657851Dot1XAuthAuthTimeoutsWhileAuthenticating = _Sw0657851Dot1XAuthAuthTimeoutsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 7),
    _Sw0657851Dot1XAuthAuthTimeoutsWhileAuthenticating_Type()
)
sw0657851Dot1XAuthAuthTimeoutsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthAuthTimeoutsWhileAuthenticating.setStatus("current")
_Sw0657851Dot1XAuthAuthFailWhileAuthenticating_Type = Counter32
_Sw0657851Dot1XAuthAuthFailWhileAuthenticating_Object = MibTableColumn
sw0657851Dot1XAuthAuthFailWhileAuthenticating = _Sw0657851Dot1XAuthAuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 8),
    _Sw0657851Dot1XAuthAuthFailWhileAuthenticating_Type()
)
sw0657851Dot1XAuthAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthAuthFailWhileAuthenticating.setStatus("current")
_Sw0657851Dot1XAuthAuthEapStartsWhileAuthenticating_Type = Counter32
_Sw0657851Dot1XAuthAuthEapStartsWhileAuthenticating_Object = MibTableColumn
sw0657851Dot1XAuthAuthEapStartsWhileAuthenticating = _Sw0657851Dot1XAuthAuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 9),
    _Sw0657851Dot1XAuthAuthEapStartsWhileAuthenticating_Type()
)
sw0657851Dot1XAuthAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthAuthEapStartsWhileAuthenticating.setStatus("current")
_Sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticating_Type = Counter32
_Sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticating_Object = MibTableColumn
sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticating = _Sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 10),
    _Sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticating_Type()
)
sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticating.setStatus("current")
_Sw0657851Dot1XAuthAuthReauthsWhileAuthenticated_Type = Counter32
_Sw0657851Dot1XAuthAuthReauthsWhileAuthenticated_Object = MibTableColumn
sw0657851Dot1XAuthAuthReauthsWhileAuthenticated = _Sw0657851Dot1XAuthAuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 11),
    _Sw0657851Dot1XAuthAuthReauthsWhileAuthenticated_Type()
)
sw0657851Dot1XAuthAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthAuthReauthsWhileAuthenticated.setStatus("current")
_Sw0657851Dot1XAuthAuthEapStartsWhileAuthenticated_Type = Counter32
_Sw0657851Dot1XAuthAuthEapStartsWhileAuthenticated_Object = MibTableColumn
sw0657851Dot1XAuthAuthEapStartsWhileAuthenticated = _Sw0657851Dot1XAuthAuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 12),
    _Sw0657851Dot1XAuthAuthEapStartsWhileAuthenticated_Type()
)
sw0657851Dot1XAuthAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthAuthEapStartsWhileAuthenticated.setStatus("current")
_Sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticated_Type = Counter32
_Sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticated_Object = MibTableColumn
sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticated = _Sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 13),
    _Sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticated_Type()
)
sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticated.setStatus("current")
_Sw0657851Dot1XBackendResponses_Type = Counter32
_Sw0657851Dot1XBackendResponses_Object = MibTableColumn
sw0657851Dot1XBackendResponses = _Sw0657851Dot1XBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 14),
    _Sw0657851Dot1XBackendResponses_Type()
)
sw0657851Dot1XBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XBackendResponses.setStatus("current")
_Sw0657851Dot1XBackendAccessChallenges_Type = Counter32
_Sw0657851Dot1XBackendAccessChallenges_Object = MibTableColumn
sw0657851Dot1XBackendAccessChallenges = _Sw0657851Dot1XBackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 15),
    _Sw0657851Dot1XBackendAccessChallenges_Type()
)
sw0657851Dot1XBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XBackendAccessChallenges.setStatus("current")
_Sw0657851Dot1XBackendOtherRequestsToSupplicant_Type = Counter32
_Sw0657851Dot1XBackendOtherRequestsToSupplicant_Object = MibTableColumn
sw0657851Dot1XBackendOtherRequestsToSupplicant = _Sw0657851Dot1XBackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 16),
    _Sw0657851Dot1XBackendOtherRequestsToSupplicant_Type()
)
sw0657851Dot1XBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XBackendOtherRequestsToSupplicant.setStatus("current")
_Sw0657851Dot1XBackendAuthSuccesses_Type = Counter32
_Sw0657851Dot1XBackendAuthSuccesses_Object = MibTableColumn
sw0657851Dot1XBackendAuthSuccesses = _Sw0657851Dot1XBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 17),
    _Sw0657851Dot1XBackendAuthSuccesses_Type()
)
sw0657851Dot1XBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XBackendAuthSuccesses.setStatus("current")
_Sw0657851Dot1XBackendAuthFails_Type = Counter32
_Sw0657851Dot1XBackendAuthFails_Object = MibTableColumn
sw0657851Dot1XBackendAuthFails = _Sw0657851Dot1XBackendAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 18),
    _Sw0657851Dot1XBackendAuthFails_Type()
)
sw0657851Dot1XBackendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XBackendAuthFails.setStatus("current")
_Sw0657851Dot1XAuthEapolFramesRx_Type = Counter32
_Sw0657851Dot1XAuthEapolFramesRx_Object = MibTableColumn
sw0657851Dot1XAuthEapolFramesRx = _Sw0657851Dot1XAuthEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 19),
    _Sw0657851Dot1XAuthEapolFramesRx_Type()
)
sw0657851Dot1XAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthEapolFramesRx.setStatus("current")
_Sw0657851Dot1XAuthEapolFramesTx_Type = Counter32
_Sw0657851Dot1XAuthEapolFramesTx_Object = MibTableColumn
sw0657851Dot1XAuthEapolFramesTx = _Sw0657851Dot1XAuthEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 20),
    _Sw0657851Dot1XAuthEapolFramesTx_Type()
)
sw0657851Dot1XAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthEapolFramesTx.setStatus("current")
_Sw0657851Dot1XAuthEapolStartFramesRx_Type = Counter32
_Sw0657851Dot1XAuthEapolStartFramesRx_Object = MibTableColumn
sw0657851Dot1XAuthEapolStartFramesRx = _Sw0657851Dot1XAuthEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 21),
    _Sw0657851Dot1XAuthEapolStartFramesRx_Type()
)
sw0657851Dot1XAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthEapolStartFramesRx.setStatus("current")
_Sw0657851Dot1XAuthEapolLogoffFramesRx_Type = Counter32
_Sw0657851Dot1XAuthEapolLogoffFramesRx_Object = MibTableColumn
sw0657851Dot1XAuthEapolLogoffFramesRx = _Sw0657851Dot1XAuthEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 22),
    _Sw0657851Dot1XAuthEapolLogoffFramesRx_Type()
)
sw0657851Dot1XAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthEapolLogoffFramesRx.setStatus("current")
_Sw0657851Dot1XAuthEapolRespIdFramesRx_Type = Counter32
_Sw0657851Dot1XAuthEapolRespIdFramesRx_Object = MibTableColumn
sw0657851Dot1XAuthEapolRespIdFramesRx = _Sw0657851Dot1XAuthEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 23),
    _Sw0657851Dot1XAuthEapolRespIdFramesRx_Type()
)
sw0657851Dot1XAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthEapolRespIdFramesRx.setStatus("current")
_Sw0657851Dot1XAuthEapolRespFramesRx_Type = Counter32
_Sw0657851Dot1XAuthEapolRespFramesRx_Object = MibTableColumn
sw0657851Dot1XAuthEapolRespFramesRx = _Sw0657851Dot1XAuthEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 24),
    _Sw0657851Dot1XAuthEapolRespFramesRx_Type()
)
sw0657851Dot1XAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthEapolRespFramesRx.setStatus("current")
_Sw0657851Dot1XAuthEapolReqIdFramesTx_Type = Counter32
_Sw0657851Dot1XAuthEapolReqIdFramesTx_Object = MibTableColumn
sw0657851Dot1XAuthEapolReqIdFramesTx = _Sw0657851Dot1XAuthEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 25),
    _Sw0657851Dot1XAuthEapolReqIdFramesTx_Type()
)
sw0657851Dot1XAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthEapolReqIdFramesTx.setStatus("current")
_Sw0657851Dot1XAuthEapolReqFramesTx_Type = Counter32
_Sw0657851Dot1XAuthEapolReqFramesTx_Object = MibTableColumn
sw0657851Dot1XAuthEapolReqFramesTx = _Sw0657851Dot1XAuthEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 26),
    _Sw0657851Dot1XAuthEapolReqFramesTx_Type()
)
sw0657851Dot1XAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthEapolReqFramesTx.setStatus("current")
_Sw0657851Dot1XAuthInvalidEapolFramesRx_Type = Counter32
_Sw0657851Dot1XAuthInvalidEapolFramesRx_Object = MibTableColumn
sw0657851Dot1XAuthInvalidEapolFramesRx = _Sw0657851Dot1XAuthInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 27),
    _Sw0657851Dot1XAuthInvalidEapolFramesRx_Type()
)
sw0657851Dot1XAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthInvalidEapolFramesRx.setStatus("current")
_Sw0657851Dot1XAuthEapLengthErrorFramesRx_Type = Counter32
_Sw0657851Dot1XAuthEapLengthErrorFramesRx_Object = MibTableColumn
sw0657851Dot1XAuthEapLengthErrorFramesRx = _Sw0657851Dot1XAuthEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 28),
    _Sw0657851Dot1XAuthEapLengthErrorFramesRx_Type()
)
sw0657851Dot1XAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthEapLengthErrorFramesRx.setStatus("current")
_Sw0657851Dot1XAuthLastEapolFrameVersion_Type = Counter32
_Sw0657851Dot1XAuthLastEapolFrameVersion_Object = MibTableColumn
sw0657851Dot1XAuthLastEapolFrameVersion = _Sw0657851Dot1XAuthLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 29),
    _Sw0657851Dot1XAuthLastEapolFrameVersion_Type()
)
sw0657851Dot1XAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthLastEapolFrameVersion.setStatus("current")
_Sw0657851Dot1XAuthLastEapolFrameSource_Type = DisplayString
_Sw0657851Dot1XAuthLastEapolFrameSource_Object = MibTableColumn
sw0657851Dot1XAuthLastEapolFrameSource = _Sw0657851Dot1XAuthLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 23, 4, 1, 30),
    _Sw0657851Dot1XAuthLastEapolFrameSource_Type()
)
sw0657851Dot1XAuthLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851Dot1XAuthLastEapolFrameSource.setStatus("current")
_Sw0657851TrunkInfo_ObjectIdentity = ObjectIdentity
sw0657851TrunkInfo = _Sw0657851TrunkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24)
)
_Sw0657851TrunkPort_ObjectIdentity = ObjectIdentity
sw0657851TrunkPort = _Sw0657851TrunkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 1)
)
_Sw0657851TrunkPortTable_Object = MibTable
sw0657851TrunkPortTable = _Sw0657851TrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 1, 1)
)
if mibBuilder.loadTexts:
    sw0657851TrunkPortTable.setStatus("current")
_Sw0657851TrunkPortEntry_Object = MibTableRow
sw0657851TrunkPortEntry = _Sw0657851TrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 1, 1, 1)
)
sw0657851TrunkPortEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851TrunkPortIndex"),
)
if mibBuilder.loadTexts:
    sw0657851TrunkPortEntry.setStatus("current")


class _Sw0657851TrunkPortIndex_Type(Integer32):
    """Custom type sw0657851TrunkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851TrunkPortIndex_Type.__name__ = "Integer32"
_Sw0657851TrunkPortIndex_Object = MibTableColumn
sw0657851TrunkPortIndex = _Sw0657851TrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 1, 1, 1, 1),
    _Sw0657851TrunkPortIndex_Type()
)
sw0657851TrunkPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851TrunkPortIndex.setStatus("current")


class _Sw0657851TrunkPortMethod_Type(Integer32):
    """Custom type sw0657851TrunkPortMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Sw0657851TrunkPortMethod_Type.__name__ = "Integer32"
_Sw0657851TrunkPortMethod_Object = MibTableColumn
sw0657851TrunkPortMethod = _Sw0657851TrunkPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 1, 1, 1, 2),
    _Sw0657851TrunkPortMethod_Type()
)
sw0657851TrunkPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TrunkPortMethod.setStatus("current")


class _Sw0657851TrunkPortGroup_Type(Integer32):
    """Custom type sw0657851TrunkPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Sw0657851TrunkPortGroup_Type.__name__ = "Integer32"
_Sw0657851TrunkPortGroup_Object = MibTableColumn
sw0657851TrunkPortGroup = _Sw0657851TrunkPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 1, 1, 1, 3),
    _Sw0657851TrunkPortGroup_Type()
)
sw0657851TrunkPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TrunkPortGroup.setStatus("current")


class _Sw0657851TrunkPortActiveLacp_Type(Integer32):
    """Custom type sw0657851TrunkPortActiveLacp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851TrunkPortActiveLacp_Type.__name__ = "Integer32"
_Sw0657851TrunkPortActiveLacp_Object = MibTableColumn
sw0657851TrunkPortActiveLacp = _Sw0657851TrunkPortActiveLacp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 1, 1, 1, 4),
    _Sw0657851TrunkPortActiveLacp_Type()
)
sw0657851TrunkPortActiveLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TrunkPortActiveLacp.setStatus("current")


class _Sw0657851TrunkPortAggtr_Type(Integer32):
    """Custom type sw0657851TrunkPortAggtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851TrunkPortAggtr_Type.__name__ = "Integer32"
_Sw0657851TrunkPortAggtr_Object = MibTableColumn
sw0657851TrunkPortAggtr = _Sw0657851TrunkPortAggtr_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 1, 1, 1, 5),
    _Sw0657851TrunkPortAggtr_Type()
)
sw0657851TrunkPortAggtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851TrunkPortAggtr.setStatus("current")


class _Sw0657851TrunkPortStatus_Type(Integer32):
    """Custom type sw0657851TrunkPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851TrunkPortStatus_Type.__name__ = "Integer32"
_Sw0657851TrunkPortStatus_Object = MibTableColumn
sw0657851TrunkPortStatus = _Sw0657851TrunkPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 1, 1, 1, 6),
    _Sw0657851TrunkPortStatus_Type()
)
sw0657851TrunkPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851TrunkPortStatus.setStatus("current")


class _Sw0657851TrunkPortCurrentMode_Type(Integer32):
    """Custom type sw0657851TrunkPortCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Sw0657851TrunkPortCurrentMode_Type.__name__ = "Integer32"
_Sw0657851TrunkPortCurrentMode_Object = MibTableColumn
sw0657851TrunkPortCurrentMode = _Sw0657851TrunkPortCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 1, 1, 1, 7),
    _Sw0657851TrunkPortCurrentMode_Type()
)
sw0657851TrunkPortCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851TrunkPortCurrentMode.setStatus("current")
_Sw0657851AggregatorView_ObjectIdentity = ObjectIdentity
sw0657851AggregatorView = _Sw0657851AggregatorView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 2)
)
_Sw0657851AggregatorViewTable_Object = MibTable
sw0657851AggregatorViewTable = _Sw0657851AggregatorViewTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    sw0657851AggregatorViewTable.setStatus("current")
_Sw0657851AggregatorViewEntry_Object = MibTableRow
sw0657851AggregatorViewEntry = _Sw0657851AggregatorViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 2, 1, 1)
)
sw0657851AggregatorViewEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851AggregatorViewIndex"),
)
if mibBuilder.loadTexts:
    sw0657851AggregatorViewEntry.setStatus("current")


class _Sw0657851AggregatorViewIndex_Type(Integer32):
    """Custom type sw0657851AggregatorViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sw0657851AggregatorViewIndex_Type.__name__ = "Integer32"
_Sw0657851AggregatorViewIndex_Object = MibTableColumn
sw0657851AggregatorViewIndex = _Sw0657851AggregatorViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 2, 1, 1, 1),
    _Sw0657851AggregatorViewIndex_Type()
)
sw0657851AggregatorViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851AggregatorViewIndex.setStatus("current")


class _Sw0657851AggregatorViewMethod_Type(Integer32):
    """Custom type sw0657851AggregatorViewMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Sw0657851AggregatorViewMethod_Type.__name__ = "Integer32"
_Sw0657851AggregatorViewMethod_Object = MibTableColumn
sw0657851AggregatorViewMethod = _Sw0657851AggregatorViewMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 2, 1, 1, 2),
    _Sw0657851AggregatorViewMethod_Type()
)
sw0657851AggregatorViewMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851AggregatorViewMethod.setStatus("current")
_Sw0657851AggregatorViewMemberPorts_Type = DisplayString
_Sw0657851AggregatorViewMemberPorts_Object = MibTableColumn
sw0657851AggregatorViewMemberPorts = _Sw0657851AggregatorViewMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 2, 1, 1, 3),
    _Sw0657851AggregatorViewMemberPorts_Type()
)
sw0657851AggregatorViewMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851AggregatorViewMemberPorts.setStatus("current")
_Sw0657851AggregatorViewReadyPorts_Type = DisplayString
_Sw0657851AggregatorViewReadyPorts_Object = MibTableColumn
sw0657851AggregatorViewReadyPorts = _Sw0657851AggregatorViewReadyPorts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 2, 1, 1, 4),
    _Sw0657851AggregatorViewReadyPorts_Type()
)
sw0657851AggregatorViewReadyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851AggregatorViewReadyPorts.setStatus("current")


class _Sw0657851LacpSystemPriority_Type(Integer32):
    """Custom type sw0657851LacpSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Sw0657851LacpSystemPriority_Type.__name__ = "Integer32"
_Sw0657851LacpSystemPriority_Object = MibScalar
sw0657851LacpSystemPriority = _Sw0657851LacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 24, 3),
    _Sw0657851LacpSystemPriority_Type()
)
sw0657851LacpSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851LacpSystemPriority.setStatus("current")
_Sw0657851IGMPInfo_ObjectIdentity = ObjectIdentity
sw0657851IGMPInfo = _Sw0657851IGMPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25)
)


class _Sw0657851IgmpProxyConfState_Type(Integer32):
    """Custom type sw0657851IgmpProxyConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851IgmpProxyConfState_Type.__name__ = "Integer32"
_Sw0657851IgmpProxyConfState_Object = MibScalar
sw0657851IgmpProxyConfState = _Sw0657851IgmpProxyConfState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 1),
    _Sw0657851IgmpProxyConfState_Type()
)
sw0657851IgmpProxyConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IgmpProxyConfState.setStatus("current")


class _Sw0657851IgmpProxyConfUnregIPMCFlooding_Type(Integer32):
    """Custom type sw0657851IgmpProxyConfUnregIPMCFlooding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657851IgmpProxyConfUnregIPMCFlooding_Type.__name__ = "Integer32"
_Sw0657851IgmpProxyConfUnregIPMCFlooding_Object = MibScalar
sw0657851IgmpProxyConfUnregIPMCFlooding = _Sw0657851IgmpProxyConfUnregIPMCFlooding_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 2),
    _Sw0657851IgmpProxyConfUnregIPMCFlooding_Type()
)
sw0657851IgmpProxyConfUnregIPMCFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IgmpProxyConfUnregIPMCFlooding.setStatus("current")


class _Sw0657851IgmpProxyConfGeneralQueuyInterval_Type(Integer32):
    """Custom type sw0657851IgmpProxyConfGeneralQueuyInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Sw0657851IgmpProxyConfGeneralQueuyInterval_Type.__name__ = "Integer32"
_Sw0657851IgmpProxyConfGeneralQueuyInterval_Object = MibScalar
sw0657851IgmpProxyConfGeneralQueuyInterval = _Sw0657851IgmpProxyConfGeneralQueuyInterval_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 3),
    _Sw0657851IgmpProxyConfGeneralQueuyInterval_Type()
)
sw0657851IgmpProxyConfGeneralQueuyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IgmpProxyConfGeneralQueuyInterval.setStatus("current")


class _Sw0657851IgmpProxyConfGeneralQueuyRepTimeout_Type(Integer32):
    """Custom type sw0657851IgmpProxyConfGeneralQueuyRepTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Sw0657851IgmpProxyConfGeneralQueuyRepTimeout_Type.__name__ = "Integer32"
_Sw0657851IgmpProxyConfGeneralQueuyRepTimeout_Object = MibScalar
sw0657851IgmpProxyConfGeneralQueuyRepTimeout = _Sw0657851IgmpProxyConfGeneralQueuyRepTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 4),
    _Sw0657851IgmpProxyConfGeneralQueuyRepTimeout_Type()
)
sw0657851IgmpProxyConfGeneralQueuyRepTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IgmpProxyConfGeneralQueuyRepTimeout.setStatus("current")


class _Sw0657851IgmpProxyConfGeneralQueuyMaxRepTime_Type(Integer32):
    """Custom type sw0657851IgmpProxyConfGeneralQueuyMaxRepTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Sw0657851IgmpProxyConfGeneralQueuyMaxRepTime_Type.__name__ = "Integer32"
_Sw0657851IgmpProxyConfGeneralQueuyMaxRepTime_Object = MibScalar
sw0657851IgmpProxyConfGeneralQueuyMaxRepTime = _Sw0657851IgmpProxyConfGeneralQueuyMaxRepTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 5),
    _Sw0657851IgmpProxyConfGeneralQueuyMaxRepTime_Type()
)
sw0657851IgmpProxyConfGeneralQueuyMaxRepTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IgmpProxyConfGeneralQueuyMaxRepTime.setStatus("current")


class _Sw0657851IgmpProxyConfLastMemberQueuyCount_Type(Integer32):
    """Custom type sw0657851IgmpProxyConfLastMemberQueuyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Sw0657851IgmpProxyConfLastMemberQueuyCount_Type.__name__ = "Integer32"
_Sw0657851IgmpProxyConfLastMemberQueuyCount_Object = MibScalar
sw0657851IgmpProxyConfLastMemberQueuyCount = _Sw0657851IgmpProxyConfLastMemberQueuyCount_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 6),
    _Sw0657851IgmpProxyConfLastMemberQueuyCount_Type()
)
sw0657851IgmpProxyConfLastMemberQueuyCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IgmpProxyConfLastMemberQueuyCount.setStatus("current")


class _Sw0657851IgmpProxyConfLastMemberQueuyInterval_Type(Integer32):
    """Custom type sw0657851IgmpProxyConfLastMemberQueuyInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Sw0657851IgmpProxyConfLastMemberQueuyInterval_Type.__name__ = "Integer32"
_Sw0657851IgmpProxyConfLastMemberQueuyInterval_Object = MibScalar
sw0657851IgmpProxyConfLastMemberQueuyInterval = _Sw0657851IgmpProxyConfLastMemberQueuyInterval_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 7),
    _Sw0657851IgmpProxyConfLastMemberQueuyInterval_Type()
)
sw0657851IgmpProxyConfLastMemberQueuyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IgmpProxyConfLastMemberQueuyInterval.setStatus("current")


class _Sw0657851IgmpProxyConfLastMemberQueuyMaxRepTime_Type(Integer32):
    """Custom type sw0657851IgmpProxyConfLastMemberQueuyMaxRepTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Sw0657851IgmpProxyConfLastMemberQueuyMaxRepTime_Type.__name__ = "Integer32"
_Sw0657851IgmpProxyConfLastMemberQueuyMaxRepTime_Object = MibScalar
sw0657851IgmpProxyConfLastMemberQueuyMaxRepTime = _Sw0657851IgmpProxyConfLastMemberQueuyMaxRepTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 8),
    _Sw0657851IgmpProxyConfLastMemberQueuyMaxRepTime_Type()
)
sw0657851IgmpProxyConfLastMemberQueuyMaxRepTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IgmpProxyConfLastMemberQueuyMaxRepTime.setStatus("current")
_Sw0657851IgmpProxyConfRouterPorts_Type = DisplayString
_Sw0657851IgmpProxyConfRouterPorts_Object = MibScalar
sw0657851IgmpProxyConfRouterPorts = _Sw0657851IgmpProxyConfRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 9),
    _Sw0657851IgmpProxyConfRouterPorts_Type()
)
sw0657851IgmpProxyConfRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IgmpProxyConfRouterPorts.setStatus("current")


class _Sw0657851IgmpGroupMembershipNumber_Type(Integer32):
    """Custom type sw0657851IgmpGroupMembershipNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Sw0657851IgmpGroupMembershipNumber_Type.__name__ = "Integer32"
_Sw0657851IgmpGroupMembershipNumber_Object = MibScalar
sw0657851IgmpGroupMembershipNumber = _Sw0657851IgmpGroupMembershipNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 10),
    _Sw0657851IgmpGroupMembershipNumber_Type()
)
sw0657851IgmpGroupMembershipNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657851IgmpGroupMembershipNumber.setStatus("current")
_Sw0657851IgmpGroupMembershipTable_Object = MibTable
sw0657851IgmpGroupMembershipTable = _Sw0657851IgmpGroupMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 11)
)
if mibBuilder.loadTexts:
    sw0657851IgmpGroupMembershipTable.setStatus("current")
_Sw0657851IgmpGroupMembershipEntry_Object = MibTableRow
sw0657851IgmpGroupMembershipEntry = _Sw0657851IgmpGroupMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 11, 1)
)
sw0657851IgmpGroupMembershipEntry.setIndexNames(
    (0, "SIGNAMAX-SW0657851-MIB", "sw0657851IgmpGroupNo"),
)
if mibBuilder.loadTexts:
    sw0657851IgmpGroupMembershipEntry.setStatus("current")


class _Sw0657851IgmpGroupNo_Type(Integer32):
    """Custom type sw0657851IgmpGroupNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Sw0657851IgmpGroupNo_Type.__name__ = "Integer32"
_Sw0657851IgmpGroupNo_Object = MibTableColumn
sw0657851IgmpGroupNo = _Sw0657851IgmpGroupNo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 11, 1, 1),
    _Sw0657851IgmpGroupNo_Type()
)
sw0657851IgmpGroupNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sw0657851IgmpGroupNo.setStatus("current")
_Sw0657851IgmpGroupAddress_Type = DisplayString
_Sw0657851IgmpGroupAddress_Object = MibTableColumn
sw0657851IgmpGroupAddress = _Sw0657851IgmpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 11, 1, 2),
    _Sw0657851IgmpGroupAddress_Type()
)
sw0657851IgmpGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851IgmpGroupAddress.setStatus("current")


class _Sw0657851IgmpGroupVLANId_Type(Integer32):
    """Custom type sw0657851IgmpGroupVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Sw0657851IgmpGroupVLANId_Type.__name__ = "Integer32"
_Sw0657851IgmpGroupVLANId_Object = MibTableColumn
sw0657851IgmpGroupVLANId = _Sw0657851IgmpGroupVLANId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 11, 1, 3),
    _Sw0657851IgmpGroupVLANId_Type()
)
sw0657851IgmpGroupVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851IgmpGroupVLANId.setStatus("current")
_Sw0657851IgmpGroupPortMembers_Type = DisplayString
_Sw0657851IgmpGroupPortMembers_Object = MibTableColumn
sw0657851IgmpGroupPortMembers = _Sw0657851IgmpGroupPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 25, 11, 1, 4),
    _Sw0657851IgmpGroupPortMembers_Type()
)
sw0657851IgmpGroupPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657851IgmpGroupPortMembers.setStatus("current")

# Managed Objects groups


# Notification objects

sw0657851UserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 1)
)
sw0657851UserLogin.setObjects(
    ("SIGNAMAX-SW0657851-MIB", "username")
)
if mibBuilder.loadTexts:
    sw0657851UserLogin.setStatus(
        "current"
    )

sw0657851UserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 2)
)
sw0657851UserLogout.setObjects(
    ("SIGNAMAX-SW0657851-MIB", "username")
)
if mibBuilder.loadTexts:
    sw0657851UserLogout.setStatus(
        "current"
    )

sw0657851ModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 3)
)
sw0657851ModuleInserted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    sw0657851ModuleInserted.setStatus(
        "current"
    )

sw0657851ModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 4)
)
sw0657851ModuleRemoved.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    sw0657851ModuleRemoved.setStatus(
        "current"
    )

sw0657851DualMediaSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 5)
)
sw0657851DualMediaSwapped.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    sw0657851DualMediaSwapped.setStatus(
        "current"
    )

sw0657851LoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 6)
)
sw0657851LoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    sw0657851LoopDetected.setStatus(
        "current"
    )

sw0657851StpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 7)
)
if mibBuilder.loadTexts:
    sw0657851StpStateDisabled.setStatus(
        "current"
    )

sw0657851StpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 8)
)
if mibBuilder.loadTexts:
    sw0657851StpStateEnabled.setStatus(
        "current"
    )

sw0657851StpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 9)
)
sw0657851StpTopologyChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    sw0657851StpTopologyChanged.setStatus(
        "current"
    )

sw0657851LacpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 10)
)
sw0657851LacpStateDisabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SIGNAMAX-SW0657851-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    sw0657851LacpStateDisabled.setStatus(
        "current"
    )

sw0657851LacpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 11)
)
sw0657851LacpStateEnabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SIGNAMAX-SW0657851-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    sw0657851LacpStateEnabled.setStatus(
        "current"
    )

sw0657851LacpPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 12)
)
sw0657851LacpPortAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SIGNAMAX-SW0657851-MIB", "actorkey"),
        ("SIGNAMAX-SW0657851-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    sw0657851LacpPortAdded.setStatus(
        "current"
    )

sw0657851LacpPortTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 13)
)
sw0657851LacpPortTrunkFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SIGNAMAX-SW0657851-MIB", "actorkey"),
        ("SIGNAMAX-SW0657851-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    sw0657851LacpPortTrunkFailure.setStatus(
        "current"
    )

sw0657851GvrpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 14)
)
if mibBuilder.loadTexts:
    sw0657851GvrpStateDisabled.setStatus(
        "current"
    )

sw0657851GvrpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 15)
)
if mibBuilder.loadTexts:
    sw0657851GvrpStateEnabled.setStatus(
        "current"
    )

sw0657851VlanStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 16)
)
if mibBuilder.loadTexts:
    sw0657851VlanStateDisabled.setStatus(
        "current"
    )

sw0657851VlanPortBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 17)
)
if mibBuilder.loadTexts:
    sw0657851VlanPortBaseEnabled.setStatus(
        "current"
    )

sw0657851VlanTagBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 18)
)
if mibBuilder.loadTexts:
    sw0657851VlanTagBaseEnabled.setStatus(
        "current"
    )

sw0657851IpmbStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 19)
)
if mibBuilder.loadTexts:
    sw0657851IpmbStateEnabled.setStatus(
        "current"
    )

sw0657851IpmbStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 20)
)
if mibBuilder.loadTexts:
    sw0657851IpmbStateDisabled.setStatus(
        "current"
    )

sw0657851IpmbClientFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 21)
)
sw0657851IpmbClientFailure.setObjects(
      *(("SIGNAMAX-SW0657851-MIB", "ipmacIp"),
        ("SIGNAMAX-SW0657851-MIB", "ipmacMac"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    sw0657851IpmbClientFailure.setStatus(
        "current"
    )

sw0657851IpmbServerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 34, 1, 20, 22)
)
sw0657851IpmbServerFailure.setObjects(
      *(("SIGNAMAX-SW0657851-MIB", "ipmacClientIp"),
        ("SIGNAMAX-SW0657851-MIB", "ipmacClientMac"),
        ("IF-MIB", "ifIndex"),
        ("SIGNAMAX-SW0657851-MIB", "ipmacServerIp"))
)
if mibBuilder.loadTexts:
    sw0657851IpmbServerFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIGNAMAX-SW0657851-MIB",
    **{"signamax": signamax,
       "switch": switch,
       "sw0657851ProductID": sw0657851ProductID,
       "sw0657851Produces": sw0657851Produces,
       "sw0657851System": sw0657851System,
       "sw0657851CommonSys": sw0657851CommonSys,
       "sw0657851Reboot": sw0657851Reboot,
       "sw0657851BiosVsersion": sw0657851BiosVsersion,
       "sw0657851FirmwareVersion": sw0657851FirmwareVersion,
       "sw0657851HardwareVersion": sw0657851HardwareVersion,
       "sw0657851MechanicalVersion": sw0657851MechanicalVersion,
       "sw0657851SerialNumber": sw0657851SerialNumber,
       "sw0657851HostMacAddress": sw0657851HostMacAddress,
       "sw0657851DevicePort": sw0657851DevicePort,
       "sw0657851RamSize": sw0657851RamSize,
       "sw0657851FlashSize": sw0657851FlashSize,
       "sw0657851DeviceName": sw0657851DeviceName,
       "sw0657851SystemDescription": sw0657851SystemDescription,
       "sw0657851IP": sw0657851IP,
       "sw0657851DhcpSetting": sw0657851DhcpSetting,
       "sw0657851IPAddress": sw0657851IPAddress,
       "sw0657851NetMask": sw0657851NetMask,
       "sw0657851DefaultGateway": sw0657851DefaultGateway,
       "sw0657851DnsSetting": sw0657851DnsSetting,
       "sw0657851DnsServer": sw0657851DnsServer,
       "sw0657851Time": sw0657851Time,
       "sw0657851SystemCurrentTime": sw0657851SystemCurrentTime,
       "sw0657851ManualTimeSetting": sw0657851ManualTimeSetting,
       "sw0657851NTPServer": sw0657851NTPServer,
       "sw0657851NTPTimeZone": sw0657851NTPTimeZone,
       "sw0657851NTPTimeSync": sw0657851NTPTimeSync,
       "sw0657851DaylightSavingTime": sw0657851DaylightSavingTime,
       "sw0657851DaylightStartTime": sw0657851DaylightStartTime,
       "sw0657851DaylightEndTime": sw0657851DaylightEndTime,
       "sw0657851Account": sw0657851Account,
       "sw0657851AccountNumber": sw0657851AccountNumber,
       "sw0657851AccountTable": sw0657851AccountTable,
       "sw0657851AccountEntry": sw0657851AccountEntry,
       "sw0657851AccountIndex": sw0657851AccountIndex,
       "sw0657851AccountAuthorization": sw0657851AccountAuthorization,
       "sw0657851AccountName": sw0657851AccountName,
       "sw0657851AccountPassword": sw0657851AccountPassword,
       "sw0657851AccountAddName": sw0657851AccountAddName,
       "sw0657851AccountAddPassword": sw0657851AccountAddPassword,
       "sw0657851DoAccountAdd": sw0657851DoAccountAdd,
       "sw0657851AccountDel": sw0657851AccountDel,
       "sw0657851Snmp": sw0657851Snmp,
       "sw0657851GetCommunity": sw0657851GetCommunity,
       "sw0657851SetCommunity": sw0657851SetCommunity,
       "sw0657851TrapHostNumber": sw0657851TrapHostNumber,
       "sw0657851TrapHostTable": sw0657851TrapHostTable,
       "sw0657851TrapHostEntry": sw0657851TrapHostEntry,
       "sw0657851TrapHostIndex": sw0657851TrapHostIndex,
       "sw0657851TrapHostIP": sw0657851TrapHostIP,
       "sw0657851TrapHostPort": sw0657851TrapHostPort,
       "sw0657851TrapHostCommunity": sw0657851TrapHostCommunity,
       "sw0657851Alarm": sw0657851Alarm,
       "sw0657851Event": sw0657851Event,
       "sw0657851EventNumber": sw0657851EventNumber,
       "sw0657851EventTable": sw0657851EventTable,
       "sw0657851EventEntry": sw0657851EventEntry,
       "sw0657851EventIndex": sw0657851EventIndex,
       "sw0657851EventName": sw0657851EventName,
       "sw0657851EventSendEmail": sw0657851EventSendEmail,
       "sw0657851EventSendTrap": sw0657851EventSendTrap,
       "sw0657851Email": sw0657851Email,
       "sw0657851EmailServer": sw0657851EmailServer,
       "sw0657851EmailUsername": sw0657851EmailUsername,
       "sw0657851EmailPassword": sw0657851EmailPassword,
       "sw0657851EmailUserNumber": sw0657851EmailUserNumber,
       "sw0657851EmailUserTable": sw0657851EmailUserTable,
       "sw0657851EmailUserEntry": sw0657851EmailUserEntry,
       "sw0657851EmailUserIndex": sw0657851EmailUserIndex,
       "sw0657851EmailUserAddress": sw0657851EmailUserAddress,
       "sw0657851Configuration": sw0657851Configuration,
       "sw0657851SaveRestore": sw0657851SaveRestore,
       "sw0657851SaveStart": sw0657851SaveStart,
       "sw0657851SaveUser": sw0657851SaveUser,
       "sw0657851RestoreDefault": sw0657851RestoreDefault,
       "sw0657851RestoreUser": sw0657851RestoreUser,
       "sw0657851ConfigFile": sw0657851ConfigFile,
       "sw0657851ExportIpAddress": sw0657851ExportIpAddress,
       "sw0657851DoExportConfig": sw0657851DoExportConfig,
       "sw0657851ImportIpAddress": sw0657851ImportIpAddress,
       "sw0657851ImportConfigName": sw0657851ImportConfigName,
       "sw0657851DoImportConfig": sw0657851DoImportConfig,
       "sw0657851Log": sw0657851Log,
       "sw0657851ClearLog": sw0657851ClearLog,
       "sw0657851LogNumber": sw0657851LogNumber,
       "sw0657851LogTable": sw0657851LogTable,
       "sw0657851LogEntry": sw0657851LogEntry,
       "sw0657851LogIndex": sw0657851LogIndex,
       "sw0657851LogEvent": sw0657851LogEvent,
       "sw0657851Firmware": sw0657851Firmware,
       "sw0657851FirmwareIpAddress": sw0657851FirmwareIpAddress,
       "sw0657851FirmwareFileName": sw0657851FirmwareFileName,
       "sw0657851DoFirmwareUpgrade": sw0657851DoFirmwareUpgrade,
       "sw0657851Port": sw0657851Port,
       "sw0657851PortStatus": sw0657851PortStatus,
       "sw0657851PortStatusNumber": sw0657851PortStatusNumber,
       "sw0657851PortStatusTable": sw0657851PortStatusTable,
       "sw0657851PortStatusEntry": sw0657851PortStatusEntry,
       "sw0657851PortStatusIndex": sw0657851PortStatusIndex,
       "sw0657851PortStatusMedia": sw0657851PortStatusMedia,
       "sw0657851PortStatusLink": sw0657851PortStatusLink,
       "sw0657851PortStatusSpdDpx": sw0657851PortStatusSpdDpx,
       "sw0657851PortStatusFlwCtrlRx": sw0657851PortStatusFlwCtrlRx,
       "sw0657851PortStatusFlwCtrlTx": sw0657851PortStatusFlwCtrlTx,
       "sw0657851PortStatuDescription": sw0657851PortStatuDescription,
       "sw0657851PortConf": sw0657851PortConf,
       "sw0657851PortConfNumber": sw0657851PortConfNumber,
       "sw0657851PortConfTable": sw0657851PortConfTable,
       "sw0657851PortConfEntry": sw0657851PortConfEntry,
       "sw0657851PortConfIndex": sw0657851PortConfIndex,
       "sw0657851PortConfPortState": sw0657851PortConfPortState,
       "sw0657851PortConfSpdDpx": sw0657851PortConfSpdDpx,
       "sw0657851PortConfFlwCtrl": sw0657851PortConfFlwCtrl,
       "sw0657851PortConfExcessiveCollisionMode": sw0657851PortConfExcessiveCollisionMode,
       "sw0657851PortConfDescription": sw0657851PortConfDescription,
       "sw0657851SFPInfo": sw0657851SFPInfo,
       "sw0657851SFPInfoNumber": sw0657851SFPInfoNumber,
       "sw0657851SFPInfoTable": sw0657851SFPInfoTable,
       "sw0657851SFPInfoEntry": sw0657851SFPInfoEntry,
       "sw0657851SFPInfoIndex": sw0657851SFPInfoIndex,
       "sw0657851SFPConnectorType": sw0657851SFPConnectorType,
       "sw0657851SFPFiberType": sw0657851SFPFiberType,
       "sw0657851SFPWavelength": sw0657851SFPWavelength,
       "sw0657851SFPBaudRate": sw0657851SFPBaudRate,
       "sw0657851SFPVendorOUI": sw0657851SFPVendorOUI,
       "sw0657851SFPVendorName": sw0657851SFPVendorName,
       "sw0657851SFPVendorPN": sw0657851SFPVendorPN,
       "sw0657851SFPVendorRev": sw0657851SFPVendorRev,
       "sw0657851SFPVendorSN": sw0657851SFPVendorSN,
       "sw0657851SFPDateCode": sw0657851SFPDateCode,
       "sw0657851SFPTemperature": sw0657851SFPTemperature,
       "sw0657851SFPVcc": sw0657851SFPVcc,
       "sw0657851SFPTxBias": sw0657851SFPTxBias,
       "sw0657851SFPTxPWR": sw0657851SFPTxPWR,
       "sw0657851SFPRxPWR": sw0657851SFPRxPWR,
       "sw0657851Mirror": sw0657851Mirror,
       "sw0657851MirroringPort": sw0657851MirroringPort,
       "sw0657851MirroredPortsTable": sw0657851MirroredPortsTable,
       "sw0657851MirroredPortsEntry": sw0657851MirroredPortsEntry,
       "sw0657851MirroredPortIndex": sw0657851MirroredPortIndex,
       "sw0657851MirroredPortSrouceEnable": sw0657851MirroredPortSrouceEnable,
       "sw0657851MirroredPortDestinationEnable": sw0657851MirroredPortDestinationEnable,
       "sw0657851MaxPktLen": sw0657851MaxPktLen,
       "sw0657851MaxPktLenPortNumber": sw0657851MaxPktLenPortNumber,
       "sw0657851MaxPktLenConfTable": sw0657851MaxPktLenConfTable,
       "sw0657851MaxPktLenConfEntry": sw0657851MaxPktLenConfEntry,
       "sw0657851MaxPktLenConfIndex": sw0657851MaxPktLenConfIndex,
       "sw0657851MaxPktLenConfSetting": sw0657851MaxPktLenConfSetting,
       "sw0657851LoopDetectedConf": sw0657851LoopDetectedConf,
       "sw0657851LoopDetectedNumber": sw0657851LoopDetectedNumber,
       "sw0657851LoopDetectedTable": sw0657851LoopDetectedTable,
       "sw0657851LoopDetectedEntry": sw0657851LoopDetectedEntry,
       "sw0657851LoopDetectedfIndex": sw0657851LoopDetectedfIndex,
       "sw0657851LoopDetectedPort": sw0657851LoopDetectedPort,
       "sw0657851LoopDetectedLockedPort": sw0657851LoopDetectedLockedPort,
       "sw0657851ManagementPolicy": sw0657851ManagementPolicy,
       "sw0657851ManagementSecurityNumber": sw0657851ManagementSecurityNumber,
       "sw0657851ManagementSecurityEntryCreate": sw0657851ManagementSecurityEntryCreate,
       "sw0657851ManagementSecurityTable": sw0657851ManagementSecurityTable,
       "sw0657851ManagementSecurityEntry": sw0657851ManagementSecurityEntry,
       "sw0657851ManagementSecurityIndex": sw0657851ManagementSecurityIndex,
       "sw0657851ManagementSecurityName": sw0657851ManagementSecurityName,
       "sw0657851ManagementSecurityIpRange": sw0657851ManagementSecurityIpRange,
       "sw0657851ManagementSecurityIncomigPort": sw0657851ManagementSecurityIncomigPort,
       "sw0657851ManagementSecurityAccessType": sw0657851ManagementSecurityAccessType,
       "sw0657851ManagementSecurityAction": sw0657851ManagementSecurityAction,
       "sw0657851ManagementSecurityEntryAction": sw0657851ManagementSecurityEntryAction,
       "sw0657851VLAN": sw0657851VLAN,
       "sw0657851VlanConf": sw0657851VlanConf,
       "sw0657851VlanMode": sw0657851VlanMode,
       "sw0657851ManagementVlan": sw0657851ManagementVlan,
       "sw0657851PortIsolation": sw0657851PortIsolation,
       "sw0657851TagBaseVlanGroup": sw0657851TagBaseVlanGroup,
       "sw0657851TagBaseVlanNumber": sw0657851TagBaseVlanNumber,
       "sw0657851TagBaseVlanGroupEntryCreate": sw0657851TagBaseVlanGroupEntryCreate,
       "sw0657851TagBaseVlanGroupTable": sw0657851TagBaseVlanGroupTable,
       "sw0657851TagBaseVlanGroupEntry": sw0657851TagBaseVlanGroupEntry,
       "sw0657851TagBaseVlanVid": sw0657851TagBaseVlanVid,
       "sw0657851TagBaseVlanName": sw0657851TagBaseVlanName,
       "sw0657851TagBaseVlanIgmpProxy": sw0657851TagBaseVlanIgmpProxy,
       "sw0657851TagBaseVlanPrivateVlan": sw0657851TagBaseVlanPrivateVlan,
       "sw0657851TagBaseVlanGvrp": sw0657851TagBaseVlanGvrp,
       "sw0657851TagBaseVlanMemberPort": sw0657851TagBaseVlanMemberPort,
       "sw0657851TagBaseVlanEntryAction": sw0657851TagBaseVlanEntryAction,
       "sw0657851VlanPortConfTable": sw0657851VlanPortConfTable,
       "sw0657851VlanPortConfEntry": sw0657851VlanPortConfEntry,
       "sw0657851VlanPortConfIndex": sw0657851VlanPortConfIndex,
       "sw0657851VlanPortConfVlanAware": sw0657851VlanPortConfVlanAware,
       "sw0657851VlanPortConfIngressFiltering": sw0657851VlanPortConfIngressFiltering,
       "sw0657851VlanPortConfFrameType": sw0657851VlanPortConfFrameType,
       "sw0657851VlanPortConfPvid": sw0657851VlanPortConfPvid,
       "sw0657851VlanPortConfRole": sw0657851VlanPortConfRole,
       "sw0657851VlanPortConfUntagVid": sw0657851VlanPortConfUntagVid,
       "sw0657851VlanPortConfDoubleTag": sw0657851VlanPortConfDoubleTag,
       "sw0657851PortBaseVlanGroup": sw0657851PortBaseVlanGroup,
       "sw0657851PortBaseVlanNumber": sw0657851PortBaseVlanNumber,
       "sw0657851PortBaseVlanGroupEntryCreate": sw0657851PortBaseVlanGroupEntryCreate,
       "sw0657851PortBaseVlanGroupTable": sw0657851PortBaseVlanGroupTable,
       "sw0657851PortBaseVlanGroupEntry": sw0657851PortBaseVlanGroupEntry,
       "sw0657851PortBaseVlanGroupIndex": sw0657851PortBaseVlanGroupIndex,
       "sw0657851PortBaseVlanGroupName": sw0657851PortBaseVlanGroupName,
       "sw0657851PortBaseVlanGroupMembers": sw0657851PortBaseVlanGroupMembers,
       "sw0657851PortBaseVlanGroupEntryAction": sw0657851PortBaseVlanGroupEntryAction,
       "sw0657851MacTableInfo": sw0657851MacTableInfo,
       "sw0657851MacTableConf": sw0657851MacTableConf,
       "sw0657851MacAgeTime": sw0657851MacAgeTime,
       "sw0657851MacTableLearningConfTable": sw0657851MacTableLearningConfTable,
       "sw0657851MacTableLearningConfEntry": sw0657851MacTableLearningConfEntry,
       "sw0657851MacTableLearningConfIndex": sw0657851MacTableLearningConfIndex,
       "sw0657851MacTableLearningConfstate": sw0657851MacTableLearningConfstate,
       "sw0657851MacTableStaticFilter": sw0657851MacTableStaticFilter,
       "sw0657851MacTableStaticFilterNumber": sw0657851MacTableStaticFilterNumber,
       "sw0657851MacTableStaticFilterEntryCreate": sw0657851MacTableStaticFilterEntryCreate,
       "sw0657851MacTableStaticFilterTable": sw0657851MacTableStaticFilterTable,
       "sw0657851MacTableStaticFilterEntry": sw0657851MacTableStaticFilterEntry,
       "sw0657851MacTableStaticFilterIndex": sw0657851MacTableStaticFilterIndex,
       "sw0657851MacTableStaticFilterMac": sw0657851MacTableStaticFilterMac,
       "sw0657851MacTableStaticFilterVid": sw0657851MacTableStaticFilterVid,
       "sw0657851MacTableStaticFilterAlias": sw0657851MacTableStaticFilterAlias,
       "sw0657851MacTableStaticFilterEntryAction": sw0657851MacTableStaticFilterEntryAction,
       "sw0657851MacTableStaticForward": sw0657851MacTableStaticForward,
       "sw0657851MacTableStaticForwardNumber": sw0657851MacTableStaticForwardNumber,
       "sw0657851MacTableStaticForwardEntryCreate": sw0657851MacTableStaticForwardEntryCreate,
       "sw0657851MacTableStaticForwardTable": sw0657851MacTableStaticForwardTable,
       "sw0657851MacTableStaticForwardEntry": sw0657851MacTableStaticForwardEntry,
       "sw0657851MacTableStaticForwardIndex": sw0657851MacTableStaticForwardIndex,
       "sw0657851MacTableStaticForwardMac": sw0657851MacTableStaticForwardMac,
       "sw0657851MacTableStaticForwardPort": sw0657851MacTableStaticForwardPort,
       "sw0657851MacTableStaticForwardVid": sw0657851MacTableStaticForwardVid,
       "sw0657851MacTableStaticForwardAlias": sw0657851MacTableStaticForwardAlias,
       "sw0657851MacTableStaticForwardEntryAction": sw0657851MacTableStaticForwardEntryAction,
       "sw0657851MacAlias": sw0657851MacAlias,
       "sw0657851MacAliasNumber": sw0657851MacAliasNumber,
       "sw0657851MacAliasEntryCreate": sw0657851MacAliasEntryCreate,
       "sw0657851MacAliasTable": sw0657851MacAliasTable,
       "sw0657851MacAliasEntry": sw0657851MacAliasEntry,
       "sw0657851MacAliasIndex": sw0657851MacAliasIndex,
       "sw0657851AliasMac": sw0657851AliasMac,
       "sw0657851AliasName": sw0657851AliasName,
       "sw0657851MacAliasEntryAction": sw0657851MacAliasEntryAction,
       "sw0657851GVRPInfo": sw0657851GVRPInfo,
       "sw0657851GvrpConf": sw0657851GvrpConf,
       "sw0657851GvrpConfState": sw0657851GvrpConfState,
       "sw0657851GvrpConfTable": sw0657851GvrpConfTable,
       "sw0657851GvrpConfEntry": sw0657851GvrpConfEntry,
       "sw0657851GvrpConfIndex": sw0657851GvrpConfIndex,
       "sw0657851GvrpConfJoinTime": sw0657851GvrpConfJoinTime,
       "sw0657851GvrpConfLeaveTime": sw0657851GvrpConfLeaveTime,
       "sw0657851GvrpConfLeaveAllTime": sw0657851GvrpConfLeaveAllTime,
       "sw0657851GvrpConfDefaultAppMode": sw0657851GvrpConfDefaultAppMode,
       "sw0657851GvrpConfDefaultRegMode": sw0657851GvrpConfDefaultRegMode,
       "sw0657851GvrpConfRestrictedMode": sw0657851GvrpConfRestrictedMode,
       "sw0657851GvrpCounter": sw0657851GvrpCounter,
       "sw0657851GvrpCounterTable": sw0657851GvrpCounterTable,
       "sw0657851GvrpCounterEntry": sw0657851GvrpCounterEntry,
       "sw0657851GvrpCounterIndex": sw0657851GvrpCounterIndex,
       "sw0657851GvrpCounterRxTotalGvrpPkts": sw0657851GvrpCounterRxTotalGvrpPkts,
       "sw0657851GvrpCounterRxInvalidGvrpPkts": sw0657851GvrpCounterRxInvalidGvrpPkts,
       "sw0657851GvrpCounterRxLeaveAllMsg": sw0657851GvrpCounterRxLeaveAllMsg,
       "sw0657851GvrpCounterRxJoinEmptyMsg": sw0657851GvrpCounterRxJoinEmptyMsg,
       "sw0657851GvrpCounterRxJoinInMsg": sw0657851GvrpCounterRxJoinInMsg,
       "sw0657851GvrpCounterRxLeaveEmptyMsg": sw0657851GvrpCounterRxLeaveEmptyMsg,
       "sw0657851GvrpCounterRxEmptyMsg": sw0657851GvrpCounterRxEmptyMsg,
       "sw0657851GvrpCounterTxTotalGvrpPkts": sw0657851GvrpCounterTxTotalGvrpPkts,
       "sw0657851GvrpCounterTxLeaveAllMsg": sw0657851GvrpCounterTxLeaveAllMsg,
       "sw0657851GvrpCounterTxJoinEmptyMsg": sw0657851GvrpCounterTxJoinEmptyMsg,
       "sw0657851GvrpCounterTxJoinInMsg": sw0657851GvrpCounterTxJoinInMsg,
       "sw0657851GvrpCounterTxLeaveEmptyMsg": sw0657851GvrpCounterTxLeaveEmptyMsg,
       "sw0657851GvrpCounterTxEmptyMsg": sw0657851GvrpCounterTxEmptyMsg,
       "sw0657851GvrpGroup": sw0657851GvrpGroup,
       "sw0657851GvrpGroupNumber": sw0657851GvrpGroupNumber,
       "sw0657851GvrpGroupTable": sw0657851GvrpGroupTable,
       "sw0657851GvrpGroupEntry": sw0657851GvrpGroupEntry,
       "sw0657851GvrpGroupId": sw0657851GvrpGroupId,
       "sw0657851GvrpGroupVid": sw0657851GvrpGroupVid,
       "sw0657851GvrpGroupMemberPort": sw0657851GvrpGroupMemberPort,
       "sw0657851GvrpGroupAdministrativeCtrlTable": sw0657851GvrpGroupAdministrativeCtrlTable,
       "sw0657851GvrpGroupAdministrativeCtrlEntry": sw0657851GvrpGroupAdministrativeCtrlEntry,
       "sw0657851GvrpGroupAdministrativeCtrlVid": sw0657851GvrpGroupAdministrativeCtrlVid,
       "sw0657851GvrpGroupAdministrativeCtrlPort": sw0657851GvrpGroupAdministrativeCtrlPort,
       "sw0657851GvrpGroupAdministrativeCtrlApp": sw0657851GvrpGroupAdministrativeCtrlApp,
       "sw0657851GvrpGroupAdministrativeCtrlReg": sw0657851GvrpGroupAdministrativeCtrlReg,
       "sw0657851QosInfo": sw0657851QosInfo,
       "sw0657851QosPortConf": sw0657851QosPortConf,
       "sw0657851QosNumOfClasses": sw0657851QosNumOfClasses,
       "sw0657851QosPortConfTable": sw0657851QosPortConfTable,
       "sw0657851QosPortConfEntry": sw0657851QosPortConfEntry,
       "sw0657851QosPortConfIndex": sw0657851QosPortConfIndex,
       "sw0657851QosPortConfDefaultClasses": sw0657851QosPortConfDefaultClasses,
       "sw0657851QosPortConfQCL": sw0657851QosPortConfQCL,
       "sw0657851QosPortConfUserPriority": sw0657851QosPortConfUserPriority,
       "sw0657851QosPortConfQueuingMode": sw0657851QosPortConfQueuingMode,
       "sw0657851QosPortConfQueueWeightedLow": sw0657851QosPortConfQueueWeightedLow,
       "sw0657851QosPortConfQueueWeightedNormal": sw0657851QosPortConfQueueWeightedNormal,
       "sw0657851QosPortConfQueueWeightedMedium": sw0657851QosPortConfQueueWeightedMedium,
       "sw0657851QosPortConfQueueWeightedHigh": sw0657851QosPortConfQueueWeightedHigh,
       "sw0657851QosRateLimiters": sw0657851QosRateLimiters,
       "sw0657851QosRateLimitersTable": sw0657851QosRateLimitersTable,
       "sw0657851QosRateLimitersEntry": sw0657851QosRateLimitersEntry,
       "sw0657851QosRateLimitersIndex": sw0657851QosRateLimitersIndex,
       "sw0657851QosRateLimitersPolicer": sw0657851QosRateLimitersPolicer,
       "sw0657851QosRateLimitersPolicerRate": sw0657851QosRateLimitersPolicerRate,
       "sw0657851QosRateLimitersShaper": sw0657851QosRateLimitersShaper,
       "sw0657851QosRateLimitersShaperRate": sw0657851QosRateLimitersShaperRate,
       "sw0657851QosStormCtrl": sw0657851QosStormCtrl,
       "sw0657851QosStromCtrlFloodedUnicastStatus": sw0657851QosStromCtrlFloodedUnicastStatus,
       "sw0657851QosStromCtrlFloodedUnicastRate": sw0657851QosStromCtrlFloodedUnicastRate,
       "sw0657851QosStromCtrlMulticastStatus": sw0657851QosStromCtrlMulticastStatus,
       "sw0657851QosStromCtrlMulticastRate": sw0657851QosStromCtrlMulticastRate,
       "sw0657851QosStromCtrlBroadcastStatus": sw0657851QosStromCtrlBroadcastStatus,
       "sw0657851QosStromCtrlBroadcastRate": sw0657851QosStromCtrlBroadcastRate,
       "sw0657851AclInfo": sw0657851AclInfo,
       "sw0657851AclPortsConfTable": sw0657851AclPortsConfTable,
       "sw0657851AclPortsConfEntry": sw0657851AclPortsConfEntry,
       "sw0657851AclPortsConfIndex": sw0657851AclPortsConfIndex,
       "sw0657851AclPortsConfPolicyId": sw0657851AclPortsConfPolicyId,
       "sw0657851AclPortsConfAction": sw0657851AclPortsConfAction,
       "sw0657851AclPortsConfRateLimiterId": sw0657851AclPortsConfRateLimiterId,
       "sw0657851AclPortsConfPortCopy": sw0657851AclPortsConfPortCopy,
       "sw0657851AclPortsConfCounter": sw0657851AclPortsConfCounter,
       "sw0657851AclRateLimiter": sw0657851AclRateLimiter,
       "sw0657851AclRateLimiterTable": sw0657851AclRateLimiterTable,
       "sw0657851AclRateLimiterEntry": sw0657851AclRateLimiterEntry,
       "sw0657851AclRateLimiterIndex": sw0657851AclRateLimiterIndex,
       "sw0657851AclRateLimiterRate": sw0657851AclRateLimiterRate,
       "sw0657851IpMacBind": sw0657851IpMacBind,
       "sw0657851IpMacBindConf": sw0657851IpMacBindConf,
       "sw0657851IpMacBindstate": sw0657851IpMacBindstate,
       "sw0657851IpMacBindTrustPort": sw0657851IpMacBindTrustPort,
       "sw0657851IpMacBindSetting": sw0657851IpMacBindSetting,
       "sw0657851IpMacBindSettingNumber": sw0657851IpMacBindSettingNumber,
       "sw0657851IpMacBindSettingEntryCreate": sw0657851IpMacBindSettingEntryCreate,
       "sw0657851IpMacBindSettingTable": sw0657851IpMacBindSettingTable,
       "sw0657851IpMacBindSettingEntry": sw0657851IpMacBindSettingEntry,
       "sw0657851IpMacBindSettingIndex": sw0657851IpMacBindSettingIndex,
       "sw0657851IpMacBindSettingMAC": sw0657851IpMacBindSettingMAC,
       "sw0657851IpMacBindSettingIP": sw0657851IpMacBindSettingIP,
       "sw0657851IpMacBindSettingPort": sw0657851IpMacBindSettingPort,
       "sw0657851IpMacBindSettingVID": sw0657851IpMacBindSettingVID,
       "sw0657851IpMacBindSettingEntryAction": sw0657851IpMacBindSettingEntryAction,
       "sw0657851TrapEntry": sw0657851TrapEntry,
       "sw0657851UserLogin": sw0657851UserLogin,
       "sw0657851UserLogout": sw0657851UserLogout,
       "sw0657851ModuleInserted": sw0657851ModuleInserted,
       "sw0657851ModuleRemoved": sw0657851ModuleRemoved,
       "sw0657851DualMediaSwapped": sw0657851DualMediaSwapped,
       "sw0657851LoopDetected": sw0657851LoopDetected,
       "sw0657851StpStateDisabled": sw0657851StpStateDisabled,
       "sw0657851StpStateEnabled": sw0657851StpStateEnabled,
       "sw0657851StpTopologyChanged": sw0657851StpTopologyChanged,
       "sw0657851LacpStateDisabled": sw0657851LacpStateDisabled,
       "sw0657851LacpStateEnabled": sw0657851LacpStateEnabled,
       "sw0657851LacpPortAdded": sw0657851LacpPortAdded,
       "sw0657851LacpPortTrunkFailure": sw0657851LacpPortTrunkFailure,
       "sw0657851GvrpStateDisabled": sw0657851GvrpStateDisabled,
       "sw0657851GvrpStateEnabled": sw0657851GvrpStateEnabled,
       "sw0657851VlanStateDisabled": sw0657851VlanStateDisabled,
       "sw0657851VlanPortBaseEnabled": sw0657851VlanPortBaseEnabled,
       "sw0657851VlanTagBaseEnabled": sw0657851VlanTagBaseEnabled,
       "sw0657851IpmbStateEnabled": sw0657851IpmbStateEnabled,
       "sw0657851IpmbStateDisabled": sw0657851IpmbStateDisabled,
       "sw0657851IpmbClientFailure": sw0657851IpmbClientFailure,
       "sw0657851IpmbServerFailure": sw0657851IpmbServerFailure,
       "sw0657851TrapVariable": sw0657851TrapVariable,
       "username": username,
       "groupId": groupId,
       "actorkey": actorkey,
       "partnerkey": partnerkey,
       "uplink": uplink,
       "ipmacIp": ipmacIp,
       "ipmacMac": ipmacMac,
       "ipmacClientIp": ipmacClientIp,
       "ipmacClientMac": ipmacClientMac,
       "ipmacServerIp": ipmacServerIp,
       "sw0657851Dot1X": sw0657851Dot1X,
       "sw0657851Dot1XServerConf": sw0657851Dot1XServerConf,
       "sw0657851Dot1XServerConfAuthenticationServerIp": sw0657851Dot1XServerConfAuthenticationServerIp,
       "sw0657851Dot1XServerConfAuthenticationUdpPort": sw0657851Dot1XServerConfAuthenticationUdpPort,
       "sw0657851Dot1XServerConfAuthenticationSecretKey": sw0657851Dot1XServerConfAuthenticationSecretKey,
       "sw0657851Dot1XServerConfAccountingServerIp": sw0657851Dot1XServerConfAccountingServerIp,
       "sw0657851Dot1XServerConfAccountingUdpPort": sw0657851Dot1XServerConfAccountingUdpPort,
       "sw0657851Dot1XServerConfAccountingSecretKey": sw0657851Dot1XServerConfAccountingSecretKey,
       "sw0657851Dot1XPortConfTable": sw0657851Dot1XPortConfTable,
       "sw0657851Dot1XPortConfEntry": sw0657851Dot1XPortConfEntry,
       "sw0657851Dot1XPort": sw0657851Dot1XPort,
       "sw0657851Dot1XPortMode": sw0657851Dot1XPortMode,
       "sw0657851Dot1XPortControl": sw0657851Dot1XPortControl,
       "sw0657851Dot1XPortreAuthMax": sw0657851Dot1XPortreAuthMax,
       "sw0657851Dot1XPorttxPeriod": sw0657851Dot1XPorttxPeriod,
       "sw0657851Dot1XPortquietPeriod": sw0657851Dot1XPortquietPeriod,
       "sw0657851Dot1XPortreAuthEnabled": sw0657851Dot1XPortreAuthEnabled,
       "sw0657851Dot1XPortreAuthPeriod": sw0657851Dot1XPortreAuthPeriod,
       "sw0657851Dot1XPortmaxReq": sw0657851Dot1XPortmaxReq,
       "sw0657851Dot1XPortsuppTimeout": sw0657851Dot1XPortsuppTimeout,
       "sw0657851Dot1XPortserverTimeout": sw0657851Dot1XPortserverTimeout,
       "sw0657851Dot1XStatusTable": sw0657851Dot1XStatusTable,
       "sw0657851Dot1XStatusEntry": sw0657851Dot1XStatusEntry,
       "sw0657851Dot1XStatusIndex": sw0657851Dot1XStatusIndex,
       "sw0657851Dot1XStatusMode": sw0657851Dot1XStatusMode,
       "sw0657851Dot1XStatusStatus": sw0657851Dot1XStatusStatus,
       "sw0657851Dot1XStatisticsTable": sw0657851Dot1XStatisticsTable,
       "sw0657851Dot1XStatisticsEntry": sw0657851Dot1XStatisticsEntry,
       "sw0657851Dot1XStatisticsIndex": sw0657851Dot1XStatisticsIndex,
       "sw0657851Dot1XClearCounter": sw0657851Dot1XClearCounter,
       "sw0657851Dot1XAuthEntersConnecting": sw0657851Dot1XAuthEntersConnecting,
       "sw0657851Dot1XauthEapLogoffsWhileConnecting": sw0657851Dot1XauthEapLogoffsWhileConnecting,
       "sw0657851Dot1XAuthEntersAuthenticating": sw0657851Dot1XAuthEntersAuthenticating,
       "sw0657851Dot1XAuthAuthSuccessesWhileAuthenticating": sw0657851Dot1XAuthAuthSuccessesWhileAuthenticating,
       "sw0657851Dot1XAuthAuthTimeoutsWhileAuthenticating": sw0657851Dot1XAuthAuthTimeoutsWhileAuthenticating,
       "sw0657851Dot1XAuthAuthFailWhileAuthenticating": sw0657851Dot1XAuthAuthFailWhileAuthenticating,
       "sw0657851Dot1XAuthAuthEapStartsWhileAuthenticating": sw0657851Dot1XAuthAuthEapStartsWhileAuthenticating,
       "sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticating": sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticating,
       "sw0657851Dot1XAuthAuthReauthsWhileAuthenticated": sw0657851Dot1XAuthAuthReauthsWhileAuthenticated,
       "sw0657851Dot1XAuthAuthEapStartsWhileAuthenticated": sw0657851Dot1XAuthAuthEapStartsWhileAuthenticated,
       "sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticated": sw0657851Dot1XAuthAuthEapLogoffWhileAuthenticated,
       "sw0657851Dot1XBackendResponses": sw0657851Dot1XBackendResponses,
       "sw0657851Dot1XBackendAccessChallenges": sw0657851Dot1XBackendAccessChallenges,
       "sw0657851Dot1XBackendOtherRequestsToSupplicant": sw0657851Dot1XBackendOtherRequestsToSupplicant,
       "sw0657851Dot1XBackendAuthSuccesses": sw0657851Dot1XBackendAuthSuccesses,
       "sw0657851Dot1XBackendAuthFails": sw0657851Dot1XBackendAuthFails,
       "sw0657851Dot1XAuthEapolFramesRx": sw0657851Dot1XAuthEapolFramesRx,
       "sw0657851Dot1XAuthEapolFramesTx": sw0657851Dot1XAuthEapolFramesTx,
       "sw0657851Dot1XAuthEapolStartFramesRx": sw0657851Dot1XAuthEapolStartFramesRx,
       "sw0657851Dot1XAuthEapolLogoffFramesRx": sw0657851Dot1XAuthEapolLogoffFramesRx,
       "sw0657851Dot1XAuthEapolRespIdFramesRx": sw0657851Dot1XAuthEapolRespIdFramesRx,
       "sw0657851Dot1XAuthEapolRespFramesRx": sw0657851Dot1XAuthEapolRespFramesRx,
       "sw0657851Dot1XAuthEapolReqIdFramesTx": sw0657851Dot1XAuthEapolReqIdFramesTx,
       "sw0657851Dot1XAuthEapolReqFramesTx": sw0657851Dot1XAuthEapolReqFramesTx,
       "sw0657851Dot1XAuthInvalidEapolFramesRx": sw0657851Dot1XAuthInvalidEapolFramesRx,
       "sw0657851Dot1XAuthEapLengthErrorFramesRx": sw0657851Dot1XAuthEapLengthErrorFramesRx,
       "sw0657851Dot1XAuthLastEapolFrameVersion": sw0657851Dot1XAuthLastEapolFrameVersion,
       "sw0657851Dot1XAuthLastEapolFrameSource": sw0657851Dot1XAuthLastEapolFrameSource,
       "sw0657851TrunkInfo": sw0657851TrunkInfo,
       "sw0657851TrunkPort": sw0657851TrunkPort,
       "sw0657851TrunkPortTable": sw0657851TrunkPortTable,
       "sw0657851TrunkPortEntry": sw0657851TrunkPortEntry,
       "sw0657851TrunkPortIndex": sw0657851TrunkPortIndex,
       "sw0657851TrunkPortMethod": sw0657851TrunkPortMethod,
       "sw0657851TrunkPortGroup": sw0657851TrunkPortGroup,
       "sw0657851TrunkPortActiveLacp": sw0657851TrunkPortActiveLacp,
       "sw0657851TrunkPortAggtr": sw0657851TrunkPortAggtr,
       "sw0657851TrunkPortStatus": sw0657851TrunkPortStatus,
       "sw0657851TrunkPortCurrentMode": sw0657851TrunkPortCurrentMode,
       "sw0657851AggregatorView": sw0657851AggregatorView,
       "sw0657851AggregatorViewTable": sw0657851AggregatorViewTable,
       "sw0657851AggregatorViewEntry": sw0657851AggregatorViewEntry,
       "sw0657851AggregatorViewIndex": sw0657851AggregatorViewIndex,
       "sw0657851AggregatorViewMethod": sw0657851AggregatorViewMethod,
       "sw0657851AggregatorViewMemberPorts": sw0657851AggregatorViewMemberPorts,
       "sw0657851AggregatorViewReadyPorts": sw0657851AggregatorViewReadyPorts,
       "sw0657851LacpSystemPriority": sw0657851LacpSystemPriority,
       "sw0657851IGMPInfo": sw0657851IGMPInfo,
       "sw0657851IgmpProxyConfState": sw0657851IgmpProxyConfState,
       "sw0657851IgmpProxyConfUnregIPMCFlooding": sw0657851IgmpProxyConfUnregIPMCFlooding,
       "sw0657851IgmpProxyConfGeneralQueuyInterval": sw0657851IgmpProxyConfGeneralQueuyInterval,
       "sw0657851IgmpProxyConfGeneralQueuyRepTimeout": sw0657851IgmpProxyConfGeneralQueuyRepTimeout,
       "sw0657851IgmpProxyConfGeneralQueuyMaxRepTime": sw0657851IgmpProxyConfGeneralQueuyMaxRepTime,
       "sw0657851IgmpProxyConfLastMemberQueuyCount": sw0657851IgmpProxyConfLastMemberQueuyCount,
       "sw0657851IgmpProxyConfLastMemberQueuyInterval": sw0657851IgmpProxyConfLastMemberQueuyInterval,
       "sw0657851IgmpProxyConfLastMemberQueuyMaxRepTime": sw0657851IgmpProxyConfLastMemberQueuyMaxRepTime,
       "sw0657851IgmpProxyConfRouterPorts": sw0657851IgmpProxyConfRouterPorts,
       "sw0657851IgmpGroupMembershipNumber": sw0657851IgmpGroupMembershipNumber,
       "sw0657851IgmpGroupMembershipTable": sw0657851IgmpGroupMembershipTable,
       "sw0657851IgmpGroupMembershipEntry": sw0657851IgmpGroupMembershipEntry,
       "sw0657851IgmpGroupNo": sw0657851IgmpGroupNo,
       "sw0657851IgmpGroupAddress": sw0657851IgmpGroupAddress,
       "sw0657851IgmpGroupVLANId": sw0657851IgmpGroupVLANId,
       "sw0657851IgmpGroupPortMembers": sw0657851IgmpGroupPortMembers}
)
