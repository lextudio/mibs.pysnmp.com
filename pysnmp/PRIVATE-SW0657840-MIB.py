# SNMP MIB module (PRIVATE-SW0657840-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PRIVATE-SW0657840-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:44 2024
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
_Sw0657840ProductID_ObjectIdentity = ObjectIdentity
sw0657840ProductID = _Sw0657840ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9)
)
_Sw0657840Produces_ObjectIdentity = ObjectIdentity
sw0657840Produces = _Sw0657840Produces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1)
)
_Sw0657840System_ObjectIdentity = ObjectIdentity
sw0657840System = _Sw0657840System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1)
)
_Sw0657840CommonSys_ObjectIdentity = ObjectIdentity
sw0657840CommonSys = _Sw0657840CommonSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 1)
)


class _Sw0657840Reboot_Type(Integer32):
    """Custom type sw0657840Reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Sw0657840Reboot_Type.__name__ = "Integer32"
_Sw0657840Reboot_Object = MibScalar
sw0657840Reboot = _Sw0657840Reboot_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 1, 1),
    _Sw0657840Reboot_Type()
)
sw0657840Reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840Reboot.setStatus("current")
_Sw0657840BiosVsersion_Type = DisplayString
_Sw0657840BiosVsersion_Object = MibScalar
sw0657840BiosVsersion = _Sw0657840BiosVsersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 1, 2),
    _Sw0657840BiosVsersion_Type()
)
sw0657840BiosVsersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840BiosVsersion.setStatus("current")
_Sw0657840FirmwareVersion_Type = DisplayString
_Sw0657840FirmwareVersion_Object = MibScalar
sw0657840FirmwareVersion = _Sw0657840FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 1, 3),
    _Sw0657840FirmwareVersion_Type()
)
sw0657840FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840FirmwareVersion.setStatus("current")
_Sw0657840HardwareVersion_Type = DisplayString
_Sw0657840HardwareVersion_Object = MibScalar
sw0657840HardwareVersion = _Sw0657840HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 1, 4),
    _Sw0657840HardwareVersion_Type()
)
sw0657840HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840HardwareVersion.setStatus("current")
_Sw0657840MechanicalVersion_Type = DisplayString
_Sw0657840MechanicalVersion_Object = MibScalar
sw0657840MechanicalVersion = _Sw0657840MechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 1, 5),
    _Sw0657840MechanicalVersion_Type()
)
sw0657840MechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840MechanicalVersion.setStatus("current")
_Sw0657840SerialNumber_Type = DisplayString
_Sw0657840SerialNumber_Object = MibScalar
sw0657840SerialNumber = _Sw0657840SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 1, 6),
    _Sw0657840SerialNumber_Type()
)
sw0657840SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SerialNumber.setStatus("current")
_Sw0657840HostMacAddress_Type = DisplayString
_Sw0657840HostMacAddress_Object = MibScalar
sw0657840HostMacAddress = _Sw0657840HostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 1, 7),
    _Sw0657840HostMacAddress_Type()
)
sw0657840HostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840HostMacAddress.setStatus("current")
_Sw0657840DevicePort_Type = DisplayString
_Sw0657840DevicePort_Object = MibScalar
sw0657840DevicePort = _Sw0657840DevicePort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 1, 8),
    _Sw0657840DevicePort_Type()
)
sw0657840DevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840DevicePort.setStatus("current")
_Sw0657840RamSize_Type = DisplayString
_Sw0657840RamSize_Object = MibScalar
sw0657840RamSize = _Sw0657840RamSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 1, 9),
    _Sw0657840RamSize_Type()
)
sw0657840RamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840RamSize.setStatus("current")
_Sw0657840FlashSize_Type = DisplayString
_Sw0657840FlashSize_Object = MibScalar
sw0657840FlashSize = _Sw0657840FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 1, 10),
    _Sw0657840FlashSize_Type()
)
sw0657840FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840FlashSize.setStatus("current")
_Sw0657840IP_ObjectIdentity = ObjectIdentity
sw0657840IP = _Sw0657840IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 2)
)


class _Sw0657840DhcpSetting_Type(Integer32):
    """Custom type sw0657840DhcpSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840DhcpSetting_Type.__name__ = "Integer32"
_Sw0657840DhcpSetting_Object = MibScalar
sw0657840DhcpSetting = _Sw0657840DhcpSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 2, 1),
    _Sw0657840DhcpSetting_Type()
)
sw0657840DhcpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840DhcpSetting.setStatus("current")
_Sw0657840IPAddress_Type = IpAddress
_Sw0657840IPAddress_Object = MibScalar
sw0657840IPAddress = _Sw0657840IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 2, 2),
    _Sw0657840IPAddress_Type()
)
sw0657840IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840IPAddress.setStatus("current")
_Sw0657840NetMask_Type = IpAddress
_Sw0657840NetMask_Object = MibScalar
sw0657840NetMask = _Sw0657840NetMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 2, 3),
    _Sw0657840NetMask_Type()
)
sw0657840NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840NetMask.setStatus("current")
_Sw0657840DefaultGateway_Type = IpAddress
_Sw0657840DefaultGateway_Object = MibScalar
sw0657840DefaultGateway = _Sw0657840DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 2, 4),
    _Sw0657840DefaultGateway_Type()
)
sw0657840DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840DefaultGateway.setStatus("current")


class _Sw0657840DnsSetting_Type(Integer32):
    """Custom type sw0657840DnsSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840DnsSetting_Type.__name__ = "Integer32"
_Sw0657840DnsSetting_Object = MibScalar
sw0657840DnsSetting = _Sw0657840DnsSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 2, 5),
    _Sw0657840DnsSetting_Type()
)
sw0657840DnsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840DnsSetting.setStatus("current")
_Sw0657840DnsServer_Type = IpAddress
_Sw0657840DnsServer_Object = MibScalar
sw0657840DnsServer = _Sw0657840DnsServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 2, 6),
    _Sw0657840DnsServer_Type()
)
sw0657840DnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840DnsServer.setStatus("current")
_Sw0657840Time_ObjectIdentity = ObjectIdentity
sw0657840Time = _Sw0657840Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 3)
)
_Sw0657840SystemCurrentTime_Type = DisplayString
_Sw0657840SystemCurrentTime_Object = MibScalar
sw0657840SystemCurrentTime = _Sw0657840SystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 3, 1),
    _Sw0657840SystemCurrentTime_Type()
)
sw0657840SystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SystemCurrentTime.setStatus("current")
_Sw0657840ManualTimeSetting_Type = DisplayString
_Sw0657840ManualTimeSetting_Object = MibScalar
sw0657840ManualTimeSetting = _Sw0657840ManualTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 3, 2),
    _Sw0657840ManualTimeSetting_Type()
)
sw0657840ManualTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840ManualTimeSetting.setStatus("current")
_Sw0657840NTPServer_Type = DisplayString
_Sw0657840NTPServer_Object = MibScalar
sw0657840NTPServer = _Sw0657840NTPServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 3, 3),
    _Sw0657840NTPServer_Type()
)
sw0657840NTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840NTPServer.setStatus("current")


class _Sw0657840NTPTimeZone_Type(Integer32):
    """Custom type sw0657840NTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_Sw0657840NTPTimeZone_Type.__name__ = "Integer32"
_Sw0657840NTPTimeZone_Object = MibScalar
sw0657840NTPTimeZone = _Sw0657840NTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 3, 4),
    _Sw0657840NTPTimeZone_Type()
)
sw0657840NTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840NTPTimeZone.setStatus("current")


class _Sw0657840NTPTimeSync_Type(Integer32):
    """Custom type sw0657840NTPTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840NTPTimeSync_Type.__name__ = "Integer32"
_Sw0657840NTPTimeSync_Object = MibScalar
sw0657840NTPTimeSync = _Sw0657840NTPTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 3, 5),
    _Sw0657840NTPTimeSync_Type()
)
sw0657840NTPTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840NTPTimeSync.setStatus("current")


class _Sw0657840DaylightSavingTime_Type(Integer32):
    """Custom type sw0657840DaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_Sw0657840DaylightSavingTime_Type.__name__ = "Integer32"
_Sw0657840DaylightSavingTime_Object = MibScalar
sw0657840DaylightSavingTime = _Sw0657840DaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 3, 6),
    _Sw0657840DaylightSavingTime_Type()
)
sw0657840DaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840DaylightSavingTime.setStatus("current")
_Sw0657840DaylightStartTime_Type = DisplayString
_Sw0657840DaylightStartTime_Object = MibScalar
sw0657840DaylightStartTime = _Sw0657840DaylightStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 3, 7),
    _Sw0657840DaylightStartTime_Type()
)
sw0657840DaylightStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840DaylightStartTime.setStatus("current")
_Sw0657840DaylightEndTime_Type = DisplayString
_Sw0657840DaylightEndTime_Object = MibScalar
sw0657840DaylightEndTime = _Sw0657840DaylightEndTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 3, 8),
    _Sw0657840DaylightEndTime_Type()
)
sw0657840DaylightEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840DaylightEndTime.setStatus("current")
_Sw0657840Account_ObjectIdentity = ObjectIdentity
sw0657840Account = _Sw0657840Account_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4)
)


class _Sw0657840AccountNumber_Type(Integer32):
    """Custom type sw0657840AccountNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Sw0657840AccountNumber_Type.__name__ = "Integer32"
_Sw0657840AccountNumber_Object = MibScalar
sw0657840AccountNumber = _Sw0657840AccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4, 1),
    _Sw0657840AccountNumber_Type()
)
sw0657840AccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840AccountNumber.setStatus("current")
_Sw0657840AccountTable_Object = MibTable
sw0657840AccountTable = _Sw0657840AccountTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sw0657840AccountTable.setStatus("current")
_Sw0657840AccountEntry_Object = MibTableRow
sw0657840AccountEntry = _Sw0657840AccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4, 2, 1)
)
sw0657840AccountEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840AccountIndex"),
)
if mibBuilder.loadTexts:
    sw0657840AccountEntry.setStatus("current")


class _Sw0657840AccountIndex_Type(Integer32):
    """Custom type sw0657840AccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Sw0657840AccountIndex_Type.__name__ = "Integer32"
_Sw0657840AccountIndex_Object = MibTableColumn
sw0657840AccountIndex = _Sw0657840AccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4, 2, 1, 1),
    _Sw0657840AccountIndex_Type()
)
sw0657840AccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840AccountIndex.setStatus("current")
_Sw0657840AccountAuthorization_Type = DisplayString
_Sw0657840AccountAuthorization_Object = MibTableColumn
sw0657840AccountAuthorization = _Sw0657840AccountAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4, 2, 1, 2),
    _Sw0657840AccountAuthorization_Type()
)
sw0657840AccountAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840AccountAuthorization.setStatus("current")
_Sw0657840AccountName_Type = DisplayString
_Sw0657840AccountName_Object = MibTableColumn
sw0657840AccountName = _Sw0657840AccountName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4, 2, 1, 3),
    _Sw0657840AccountName_Type()
)
sw0657840AccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840AccountName.setStatus("current")
_Sw0657840AccountPassword_Type = DisplayString
_Sw0657840AccountPassword_Object = MibTableColumn
sw0657840AccountPassword = _Sw0657840AccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4, 2, 1, 4),
    _Sw0657840AccountPassword_Type()
)
sw0657840AccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840AccountPassword.setStatus("current")
_Sw0657840AccountAddName_Type = DisplayString
_Sw0657840AccountAddName_Object = MibScalar
sw0657840AccountAddName = _Sw0657840AccountAddName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4, 3),
    _Sw0657840AccountAddName_Type()
)
sw0657840AccountAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840AccountAddName.setStatus("current")
_Sw0657840AccountAddPassword_Type = DisplayString
_Sw0657840AccountAddPassword_Object = MibScalar
sw0657840AccountAddPassword = _Sw0657840AccountAddPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4, 4),
    _Sw0657840AccountAddPassword_Type()
)
sw0657840AccountAddPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840AccountAddPassword.setStatus("current")


class _Sw0657840DoAccountAdd_Type(Integer32):
    """Custom type sw0657840DoAccountAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840DoAccountAdd_Type.__name__ = "Integer32"
_Sw0657840DoAccountAdd_Object = MibScalar
sw0657840DoAccountAdd = _Sw0657840DoAccountAdd_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4, 5),
    _Sw0657840DoAccountAdd_Type()
)
sw0657840DoAccountAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840DoAccountAdd.setStatus("current")


class _Sw0657840AccountDel_Type(Integer32):
    """Custom type sw0657840AccountDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_Sw0657840AccountDel_Type.__name__ = "Integer32"
_Sw0657840AccountDel_Object = MibScalar
sw0657840AccountDel = _Sw0657840AccountDel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 1, 4, 6),
    _Sw0657840AccountDel_Type()
)
sw0657840AccountDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840AccountDel.setStatus("current")
_Sw0657840Snmp_ObjectIdentity = ObjectIdentity
sw0657840Snmp = _Sw0657840Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 2)
)
_Sw0657840GetCommunity_Type = DisplayString
_Sw0657840GetCommunity_Object = MibScalar
sw0657840GetCommunity = _Sw0657840GetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 2, 1),
    _Sw0657840GetCommunity_Type()
)
sw0657840GetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840GetCommunity.setStatus("current")
_Sw0657840SetCommunity_Type = DisplayString
_Sw0657840SetCommunity_Object = MibScalar
sw0657840SetCommunity = _Sw0657840SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 2, 2),
    _Sw0657840SetCommunity_Type()
)
sw0657840SetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840SetCommunity.setStatus("current")


class _Sw0657840TrapHostNumber_Type(Integer32):
    """Custom type sw0657840TrapHostNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sw0657840TrapHostNumber_Type.__name__ = "Integer32"
_Sw0657840TrapHostNumber_Object = MibScalar
sw0657840TrapHostNumber = _Sw0657840TrapHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 2, 3),
    _Sw0657840TrapHostNumber_Type()
)
sw0657840TrapHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840TrapHostNumber.setStatus("current")
_Sw0657840TrapHostTable_Object = MibTable
sw0657840TrapHostTable = _Sw0657840TrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 2, 4)
)
if mibBuilder.loadTexts:
    sw0657840TrapHostTable.setStatus("current")
_Sw0657840TrapHostEntry_Object = MibTableRow
sw0657840TrapHostEntry = _Sw0657840TrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 2, 4, 1)
)
sw0657840TrapHostEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840TrapHostIndex"),
)
if mibBuilder.loadTexts:
    sw0657840TrapHostEntry.setStatus("current")


class _Sw0657840TrapHostIndex_Type(Integer32):
    """Custom type sw0657840TrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sw0657840TrapHostIndex_Type.__name__ = "Integer32"
_Sw0657840TrapHostIndex_Object = MibTableColumn
sw0657840TrapHostIndex = _Sw0657840TrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 2, 4, 1, 1),
    _Sw0657840TrapHostIndex_Type()
)
sw0657840TrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840TrapHostIndex.setStatus("current")
_Sw0657840TrapHostIP_Type = IpAddress
_Sw0657840TrapHostIP_Object = MibTableColumn
sw0657840TrapHostIP = _Sw0657840TrapHostIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 2, 4, 1, 2),
    _Sw0657840TrapHostIP_Type()
)
sw0657840TrapHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840TrapHostIP.setStatus("current")


class _Sw0657840TrapHostPort_Type(Integer32):
    """Custom type sw0657840TrapHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Sw0657840TrapHostPort_Type.__name__ = "Integer32"
_Sw0657840TrapHostPort_Object = MibTableColumn
sw0657840TrapHostPort = _Sw0657840TrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 2, 4, 1, 3),
    _Sw0657840TrapHostPort_Type()
)
sw0657840TrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840TrapHostPort.setStatus("current")
_Sw0657840TrapHostCommunity_Type = DisplayString
_Sw0657840TrapHostCommunity_Object = MibTableColumn
sw0657840TrapHostCommunity = _Sw0657840TrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 2, 4, 1, 4),
    _Sw0657840TrapHostCommunity_Type()
)
sw0657840TrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840TrapHostCommunity.setStatus("current")
_Sw0657840Alarm_ObjectIdentity = ObjectIdentity
sw0657840Alarm = _Sw0657840Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3)
)
_Sw0657840Event_ObjectIdentity = ObjectIdentity
sw0657840Event = _Sw0657840Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 1)
)


class _Sw0657840EventNumber_Type(Integer32):
    """Custom type sw0657840EventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840EventNumber_Type.__name__ = "Integer32"
_Sw0657840EventNumber_Object = MibScalar
sw0657840EventNumber = _Sw0657840EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 1, 1),
    _Sw0657840EventNumber_Type()
)
sw0657840EventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840EventNumber.setStatus("current")
_Sw0657840EventTable_Object = MibTable
sw0657840EventTable = _Sw0657840EventTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sw0657840EventTable.setStatus("current")
_Sw0657840EventEntry_Object = MibTableRow
sw0657840EventEntry = _Sw0657840EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 1, 2, 1)
)
sw0657840EventEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840EventIndex"),
)
if mibBuilder.loadTexts:
    sw0657840EventEntry.setStatus("current")


class _Sw0657840EventIndex_Type(Integer32):
    """Custom type sw0657840EventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840EventIndex_Type.__name__ = "Integer32"
_Sw0657840EventIndex_Object = MibTableColumn
sw0657840EventIndex = _Sw0657840EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 1, 2, 1, 1),
    _Sw0657840EventIndex_Type()
)
sw0657840EventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840EventIndex.setStatus("current")
_Sw0657840EventName_Type = DisplayString
_Sw0657840EventName_Object = MibTableColumn
sw0657840EventName = _Sw0657840EventName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 1, 2, 1, 2),
    _Sw0657840EventName_Type()
)
sw0657840EventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840EventName.setStatus("current")


class _Sw0657840EventSendEmail_Type(Integer32):
    """Custom type sw0657840EventSendEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840EventSendEmail_Type.__name__ = "Integer32"
_Sw0657840EventSendEmail_Object = MibTableColumn
sw0657840EventSendEmail = _Sw0657840EventSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 1, 2, 1, 3),
    _Sw0657840EventSendEmail_Type()
)
sw0657840EventSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840EventSendEmail.setStatus("current")


class _Sw0657840EventSendSMS_Type(Integer32):
    """Custom type sw0657840EventSendSMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840EventSendSMS_Type.__name__ = "Integer32"
_Sw0657840EventSendSMS_Object = MibTableColumn
sw0657840EventSendSMS = _Sw0657840EventSendSMS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 1, 2, 1, 4),
    _Sw0657840EventSendSMS_Type()
)
sw0657840EventSendSMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840EventSendSMS.setStatus("current")


class _Sw0657840EventSendTrap_Type(Integer32):
    """Custom type sw0657840EventSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840EventSendTrap_Type.__name__ = "Integer32"
_Sw0657840EventSendTrap_Object = MibTableColumn
sw0657840EventSendTrap = _Sw0657840EventSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 1, 2, 1, 5),
    _Sw0657840EventSendTrap_Type()
)
sw0657840EventSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840EventSendTrap.setStatus("current")
_Sw0657840Email_ObjectIdentity = ObjectIdentity
sw0657840Email = _Sw0657840Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 2)
)
_Sw0657840EmailServer_Type = DisplayString
_Sw0657840EmailServer_Object = MibScalar
sw0657840EmailServer = _Sw0657840EmailServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 2, 1),
    _Sw0657840EmailServer_Type()
)
sw0657840EmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840EmailServer.setStatus("current")
_Sw0657840EmailUsername_Type = DisplayString
_Sw0657840EmailUsername_Object = MibScalar
sw0657840EmailUsername = _Sw0657840EmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 2, 2),
    _Sw0657840EmailUsername_Type()
)
sw0657840EmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840EmailUsername.setStatus("current")
_Sw0657840EmailPassword_Type = DisplayString
_Sw0657840EmailPassword_Object = MibScalar
sw0657840EmailPassword = _Sw0657840EmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 2, 3),
    _Sw0657840EmailPassword_Type()
)
sw0657840EmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840EmailPassword.setStatus("current")


class _Sw0657840EmailUserNumber_Type(Integer32):
    """Custom type sw0657840EmailUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sw0657840EmailUserNumber_Type.__name__ = "Integer32"
_Sw0657840EmailUserNumber_Object = MibScalar
sw0657840EmailUserNumber = _Sw0657840EmailUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 2, 4),
    _Sw0657840EmailUserNumber_Type()
)
sw0657840EmailUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840EmailUserNumber.setStatus("current")
_Sw0657840EmailUserTable_Object = MibTable
sw0657840EmailUserTable = _Sw0657840EmailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    sw0657840EmailUserTable.setStatus("current")
_Sw0657840EmailUserEntry_Object = MibTableRow
sw0657840EmailUserEntry = _Sw0657840EmailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 2, 5, 1)
)
sw0657840EmailUserEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840EmailUserIndex"),
)
if mibBuilder.loadTexts:
    sw0657840EmailUserEntry.setStatus("current")


class _Sw0657840EmailUserIndex_Type(Integer32):
    """Custom type sw0657840EmailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sw0657840EmailUserIndex_Type.__name__ = "Integer32"
_Sw0657840EmailUserIndex_Object = MibTableColumn
sw0657840EmailUserIndex = _Sw0657840EmailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 2, 5, 1, 1),
    _Sw0657840EmailUserIndex_Type()
)
sw0657840EmailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840EmailUserIndex.setStatus("current")
_Sw0657840EmailUserAddress_Type = DisplayString
_Sw0657840EmailUserAddress_Object = MibTableColumn
sw0657840EmailUserAddress = _Sw0657840EmailUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 2, 5, 1, 2),
    _Sw0657840EmailUserAddress_Type()
)
sw0657840EmailUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840EmailUserAddress.setStatus("current")
_Sw0657840SMS_ObjectIdentity = ObjectIdentity
sw0657840SMS = _Sw0657840SMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 3)
)
_Sw0657840SMSServer_Type = DisplayString
_Sw0657840SMSServer_Object = MibScalar
sw0657840SMSServer = _Sw0657840SMSServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 3, 1),
    _Sw0657840SMSServer_Type()
)
sw0657840SMSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840SMSServer.setStatus("current")
_Sw0657840SMSUsername_Type = DisplayString
_Sw0657840SMSUsername_Object = MibScalar
sw0657840SMSUsername = _Sw0657840SMSUsername_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 3, 2),
    _Sw0657840SMSUsername_Type()
)
sw0657840SMSUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840SMSUsername.setStatus("current")
_Sw0657840SMSPassword_Type = DisplayString
_Sw0657840SMSPassword_Object = MibScalar
sw0657840SMSPassword = _Sw0657840SMSPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 3, 3),
    _Sw0657840SMSPassword_Type()
)
sw0657840SMSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840SMSPassword.setStatus("current")


class _Sw0657840SMSUserNumber_Type(Integer32):
    """Custom type sw0657840SMSUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sw0657840SMSUserNumber_Type.__name__ = "Integer32"
_Sw0657840SMSUserNumber_Object = MibScalar
sw0657840SMSUserNumber = _Sw0657840SMSUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 3, 4),
    _Sw0657840SMSUserNumber_Type()
)
sw0657840SMSUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SMSUserNumber.setStatus("current")
_Sw0657840SMSUserTable_Object = MibTable
sw0657840SMSUserTable = _Sw0657840SMSUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    sw0657840SMSUserTable.setStatus("current")
_Sw0657840SMSUserEntry_Object = MibTableRow
sw0657840SMSUserEntry = _Sw0657840SMSUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 3, 5, 1)
)
sw0657840SMSUserEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840SMSUserIndex"),
)
if mibBuilder.loadTexts:
    sw0657840SMSUserEntry.setStatus("current")


class _Sw0657840SMSUserIndex_Type(Integer32):
    """Custom type sw0657840SMSUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sw0657840SMSUserIndex_Type.__name__ = "Integer32"
_Sw0657840SMSUserIndex_Object = MibTableColumn
sw0657840SMSUserIndex = _Sw0657840SMSUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 3, 5, 1, 1),
    _Sw0657840SMSUserIndex_Type()
)
sw0657840SMSUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SMSUserIndex.setStatus("current")
_Sw0657840SMSUserMobilePhone_Type = DisplayString
_Sw0657840SMSUserMobilePhone_Object = MibTableColumn
sw0657840SMSUserMobilePhone = _Sw0657840SMSUserMobilePhone_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 3, 3, 5, 1, 2),
    _Sw0657840SMSUserMobilePhone_Type()
)
sw0657840SMSUserMobilePhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840SMSUserMobilePhone.setStatus("current")
_Sw0657840Tftp_ObjectIdentity = ObjectIdentity
sw0657840Tftp = _Sw0657840Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 4)
)
_Sw0657840TftpServer_Type = IpAddress
_Sw0657840TftpServer_Object = MibScalar
sw0657840TftpServer = _Sw0657840TftpServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 4, 1),
    _Sw0657840TftpServer_Type()
)
sw0657840TftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840TftpServer.setStatus("current")
_Sw0657840Configuration_ObjectIdentity = ObjectIdentity
sw0657840Configuration = _Sw0657840Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 5)
)
_Sw0657840SaveRestore_ObjectIdentity = ObjectIdentity
sw0657840SaveRestore = _Sw0657840SaveRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 5, 1)
)


class _Sw0657840SaveStart_Type(Integer32):
    """Custom type sw0657840SaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840SaveStart_Type.__name__ = "Integer32"
_Sw0657840SaveStart_Object = MibScalar
sw0657840SaveStart = _Sw0657840SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 5, 1, 1),
    _Sw0657840SaveStart_Type()
)
sw0657840SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840SaveStart.setStatus("current")


class _Sw0657840SaveUser_Type(Integer32):
    """Custom type sw0657840SaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840SaveUser_Type.__name__ = "Integer32"
_Sw0657840SaveUser_Object = MibScalar
sw0657840SaveUser = _Sw0657840SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 5, 1, 2),
    _Sw0657840SaveUser_Type()
)
sw0657840SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840SaveUser.setStatus("current")


class _Sw0657840RestoreDefault_Type(Integer32):
    """Custom type sw0657840RestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Sw0657840RestoreDefault_Type.__name__ = "Integer32"
_Sw0657840RestoreDefault_Object = MibScalar
sw0657840RestoreDefault = _Sw0657840RestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 5, 1, 3),
    _Sw0657840RestoreDefault_Type()
)
sw0657840RestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840RestoreDefault.setStatus("current")


class _Sw0657840RestoreUser_Type(Integer32):
    """Custom type sw0657840RestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840RestoreUser_Type.__name__ = "Integer32"
_Sw0657840RestoreUser_Object = MibScalar
sw0657840RestoreUser = _Sw0657840RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 5, 1, 4),
    _Sw0657840RestoreUser_Type()
)
sw0657840RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840RestoreUser.setStatus("current")
_Sw0657840ConfigFile_ObjectIdentity = ObjectIdentity
sw0657840ConfigFile = _Sw0657840ConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 5, 2)
)
_Sw0657840ExportConfigName_Type = DisplayString
_Sw0657840ExportConfigName_Object = MibScalar
sw0657840ExportConfigName = _Sw0657840ExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 5, 2, 1),
    _Sw0657840ExportConfigName_Type()
)
sw0657840ExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840ExportConfigName.setStatus("current")


class _Sw0657840DoExportConfig_Type(Integer32):
    """Custom type sw0657840DoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Sw0657840DoExportConfig_Type.__name__ = "Integer32"
_Sw0657840DoExportConfig_Object = MibScalar
sw0657840DoExportConfig = _Sw0657840DoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 5, 2, 2),
    _Sw0657840DoExportConfig_Type()
)
sw0657840DoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840DoExportConfig.setStatus("current")
_Sw0657840ImportConfigName_Type = DisplayString
_Sw0657840ImportConfigName_Object = MibScalar
sw0657840ImportConfigName = _Sw0657840ImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 5, 2, 3),
    _Sw0657840ImportConfigName_Type()
)
sw0657840ImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840ImportConfigName.setStatus("current")


class _Sw0657840DoImportConfig_Type(Integer32):
    """Custom type sw0657840DoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Sw0657840DoImportConfig_Type.__name__ = "Integer32"
_Sw0657840DoImportConfig_Object = MibScalar
sw0657840DoImportConfig = _Sw0657840DoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 5, 2, 4),
    _Sw0657840DoImportConfig_Type()
)
sw0657840DoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840DoImportConfig.setStatus("current")
_Sw0657840Diagnostic_ObjectIdentity = ObjectIdentity
sw0657840Diagnostic = _Sw0657840Diagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 6)
)
_Sw0657840EEPROMTest_Type = DisplayString
_Sw0657840EEPROMTest_Object = MibScalar
sw0657840EEPROMTest = _Sw0657840EEPROMTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 6, 1),
    _Sw0657840EEPROMTest_Type()
)
sw0657840EEPROMTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840EEPROMTest.setStatus("current")
_Sw0657840UartTest_Type = DisplayString
_Sw0657840UartTest_Object = MibScalar
sw0657840UartTest = _Sw0657840UartTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 6, 2),
    _Sw0657840UartTest_Type()
)
sw0657840UartTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840UartTest.setStatus("current")
_Sw0657840DramTest_Type = DisplayString
_Sw0657840DramTest_Object = MibScalar
sw0657840DramTest = _Sw0657840DramTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 6, 3),
    _Sw0657840DramTest_Type()
)
sw0657840DramTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840DramTest.setStatus("current")
_Sw0657840FlashTest_Type = DisplayString
_Sw0657840FlashTest_Object = MibScalar
sw0657840FlashTest = _Sw0657840FlashTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 6, 4),
    _Sw0657840FlashTest_Type()
)
sw0657840FlashTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840FlashTest.setStatus("current")
_Sw0657840InternalLoopbackTest_Type = DisplayString
_Sw0657840InternalLoopbackTest_Object = MibScalar
sw0657840InternalLoopbackTest = _Sw0657840InternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 6, 5),
    _Sw0657840InternalLoopbackTest_Type()
)
sw0657840InternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840InternalLoopbackTest.setStatus("current")
_Sw0657840ExternalLoopbackTest_Type = DisplayString
_Sw0657840ExternalLoopbackTest_Object = MibScalar
sw0657840ExternalLoopbackTest = _Sw0657840ExternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 6, 6),
    _Sw0657840ExternalLoopbackTest_Type()
)
sw0657840ExternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840ExternalLoopbackTest.setStatus("current")
_Sw0657840PingTest_Type = DisplayString
_Sw0657840PingTest_Object = MibScalar
sw0657840PingTest = _Sw0657840PingTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 6, 7),
    _Sw0657840PingTest_Type()
)
sw0657840PingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840PingTest.setStatus("current")
_Sw0657840Log_ObjectIdentity = ObjectIdentity
sw0657840Log = _Sw0657840Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 7)
)


class _Sw0657840ClearLog_Type(Integer32):
    """Custom type sw0657840ClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840ClearLog_Type.__name__ = "Integer32"
_Sw0657840ClearLog_Object = MibScalar
sw0657840ClearLog = _Sw0657840ClearLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 7, 1),
    _Sw0657840ClearLog_Type()
)
sw0657840ClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840ClearLog.setStatus("current")


class _Sw0657840UploadLog_Type(Integer32):
    """Custom type sw0657840UploadLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840UploadLog_Type.__name__ = "Integer32"
_Sw0657840UploadLog_Object = MibScalar
sw0657840UploadLog = _Sw0657840UploadLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 7, 2),
    _Sw0657840UploadLog_Type()
)
sw0657840UploadLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840UploadLog.setStatus("current")


class _Sw0657840AutoUploadLogState_Type(Integer32):
    """Custom type sw0657840AutoUploadLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840AutoUploadLogState_Type.__name__ = "Integer32"
_Sw0657840AutoUploadLogState_Object = MibScalar
sw0657840AutoUploadLogState = _Sw0657840AutoUploadLogState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 7, 3),
    _Sw0657840AutoUploadLogState_Type()
)
sw0657840AutoUploadLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840AutoUploadLogState.setStatus("current")


class _Sw0657840LogNumber_Type(Integer32):
    """Custom type sw0657840LogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Sw0657840LogNumber_Type.__name__ = "Integer32"
_Sw0657840LogNumber_Object = MibScalar
sw0657840LogNumber = _Sw0657840LogNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 7, 4),
    _Sw0657840LogNumber_Type()
)
sw0657840LogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840LogNumber.setStatus("current")
_Sw0657840LogTable_Object = MibTable
sw0657840LogTable = _Sw0657840LogTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 7, 5)
)
if mibBuilder.loadTexts:
    sw0657840LogTable.setStatus("current")
_Sw0657840LogEntry_Object = MibTableRow
sw0657840LogEntry = _Sw0657840LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 7, 5, 1)
)
sw0657840LogEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840LogIndex"),
)
if mibBuilder.loadTexts:
    sw0657840LogEntry.setStatus("current")


class _Sw0657840LogIndex_Type(Integer32):
    """Custom type sw0657840LogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Sw0657840LogIndex_Type.__name__ = "Integer32"
_Sw0657840LogIndex_Object = MibTableColumn
sw0657840LogIndex = _Sw0657840LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 7, 5, 1, 1),
    _Sw0657840LogIndex_Type()
)
sw0657840LogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840LogIndex.setStatus("current")
_Sw0657840LogEvent_Type = DisplayString
_Sw0657840LogEvent_Object = MibTableColumn
sw0657840LogEvent = _Sw0657840LogEvent_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 7, 5, 1, 2),
    _Sw0657840LogEvent_Type()
)
sw0657840LogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840LogEvent.setStatus("current")
_Sw0657840Firmware_ObjectIdentity = ObjectIdentity
sw0657840Firmware = _Sw0657840Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 8)
)
_Sw0657840FirmwareFileName_Type = DisplayString
_Sw0657840FirmwareFileName_Object = MibScalar
sw0657840FirmwareFileName = _Sw0657840FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 8, 1),
    _Sw0657840FirmwareFileName_Type()
)
sw0657840FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840FirmwareFileName.setStatus("current")


class _Sw0657840DoFirmwareUpgrade_Type(Integer32):
    """Custom type sw0657840DoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840DoFirmwareUpgrade_Type.__name__ = "Integer32"
_Sw0657840DoFirmwareUpgrade_Object = MibScalar
sw0657840DoFirmwareUpgrade = _Sw0657840DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 8, 2),
    _Sw0657840DoFirmwareUpgrade_Type()
)
sw0657840DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840DoFirmwareUpgrade.setStatus("current")
_Sw0657840Port_ObjectIdentity = ObjectIdentity
sw0657840Port = _Sw0657840Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9)
)
_Sw0657840PortStatus_ObjectIdentity = ObjectIdentity
sw0657840PortStatus = _Sw0657840PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1)
)


class _Sw0657840PortStatusNumber_Type(Integer32):
    """Custom type sw0657840PortStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840PortStatusNumber_Type.__name__ = "Integer32"
_Sw0657840PortStatusNumber_Object = MibScalar
sw0657840PortStatusNumber = _Sw0657840PortStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1, 1),
    _Sw0657840PortStatusNumber_Type()
)
sw0657840PortStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840PortStatusNumber.setStatus("current")
_Sw0657840PortStatusTable_Object = MibTable
sw0657840PortStatusTable = _Sw0657840PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    sw0657840PortStatusTable.setStatus("current")
_Sw0657840PortStatusEntry_Object = MibTableRow
sw0657840PortStatusEntry = _Sw0657840PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1, 2, 1)
)
sw0657840PortStatusEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840PortStatusIndex"),
)
if mibBuilder.loadTexts:
    sw0657840PortStatusEntry.setStatus("current")


class _Sw0657840PortStatusIndex_Type(Integer32):
    """Custom type sw0657840PortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840PortStatusIndex_Type.__name__ = "Integer32"
_Sw0657840PortStatusIndex_Object = MibTableColumn
sw0657840PortStatusIndex = _Sw0657840PortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1, 2, 1, 1),
    _Sw0657840PortStatusIndex_Type()
)
sw0657840PortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840PortStatusIndex.setStatus("current")
_Sw0657840PortStatusMedia_Type = DisplayString
_Sw0657840PortStatusMedia_Object = MibTableColumn
sw0657840PortStatusMedia = _Sw0657840PortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1, 2, 1, 2),
    _Sw0657840PortStatusMedia_Type()
)
sw0657840PortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840PortStatusMedia.setStatus("current")
_Sw0657840PortStatusLink_Type = DisplayString
_Sw0657840PortStatusLink_Object = MibTableColumn
sw0657840PortStatusLink = _Sw0657840PortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1, 2, 1, 3),
    _Sw0657840PortStatusLink_Type()
)
sw0657840PortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840PortStatusLink.setStatus("current")
_Sw0657840PortStatusPortState_Type = DisplayString
_Sw0657840PortStatusPortState_Object = MibTableColumn
sw0657840PortStatusPortState = _Sw0657840PortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1, 2, 1, 4),
    _Sw0657840PortStatusPortState_Type()
)
sw0657840PortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840PortStatusPortState.setStatus("current")
_Sw0657840PortStatusAutoNego_Type = DisplayString
_Sw0657840PortStatusAutoNego_Object = MibTableColumn
sw0657840PortStatusAutoNego = _Sw0657840PortStatusAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1, 2, 1, 5),
    _Sw0657840PortStatusAutoNego_Type()
)
sw0657840PortStatusAutoNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840PortStatusAutoNego.setStatus("current")
_Sw0657840PortStatusSpdDpx_Type = DisplayString
_Sw0657840PortStatusSpdDpx_Object = MibTableColumn
sw0657840PortStatusSpdDpx = _Sw0657840PortStatusSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1, 2, 1, 6),
    _Sw0657840PortStatusSpdDpx_Type()
)
sw0657840PortStatusSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840PortStatusSpdDpx.setStatus("current")
_Sw0657840PortStatusFlwCtrl_Type = DisplayString
_Sw0657840PortStatusFlwCtrl_Object = MibTableColumn
sw0657840PortStatusFlwCtrl = _Sw0657840PortStatusFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1, 2, 1, 7),
    _Sw0657840PortStatusFlwCtrl_Type()
)
sw0657840PortStatusFlwCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840PortStatusFlwCtrl.setStatus("current")
_Sw0657840PortStatuDescription_Type = DisplayString
_Sw0657840PortStatuDescription_Object = MibTableColumn
sw0657840PortStatuDescription = _Sw0657840PortStatuDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 1, 2, 1, 8),
    _Sw0657840PortStatuDescription_Type()
)
sw0657840PortStatuDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840PortStatuDescription.setStatus("current")
_Sw0657840PortConf_ObjectIdentity = ObjectIdentity
sw0657840PortConf = _Sw0657840PortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 2)
)


class _Sw0657840PortConfNumber_Type(Integer32):
    """Custom type sw0657840PortConfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840PortConfNumber_Type.__name__ = "Integer32"
_Sw0657840PortConfNumber_Object = MibScalar
sw0657840PortConfNumber = _Sw0657840PortConfNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 2, 1),
    _Sw0657840PortConfNumber_Type()
)
sw0657840PortConfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840PortConfNumber.setStatus("current")
_Sw0657840PortConfTable_Object = MibTable
sw0657840PortConfTable = _Sw0657840PortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    sw0657840PortConfTable.setStatus("current")
_Sw0657840PortConfEntry_Object = MibTableRow
sw0657840PortConfEntry = _Sw0657840PortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 2, 2, 1)
)
sw0657840PortConfEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840PortConfIndex"),
)
if mibBuilder.loadTexts:
    sw0657840PortConfEntry.setStatus("current")


class _Sw0657840PortConfIndex_Type(Integer32):
    """Custom type sw0657840PortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840PortConfIndex_Type.__name__ = "Integer32"
_Sw0657840PortConfIndex_Object = MibTableColumn
sw0657840PortConfIndex = _Sw0657840PortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 2, 2, 1, 1),
    _Sw0657840PortConfIndex_Type()
)
sw0657840PortConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840PortConfIndex.setStatus("current")


class _Sw0657840PortConfPortState_Type(Integer32):
    """Custom type sw0657840PortConfPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840PortConfPortState_Type.__name__ = "Integer32"
_Sw0657840PortConfPortState_Object = MibTableColumn
sw0657840PortConfPortState = _Sw0657840PortConfPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 2, 2, 1, 2),
    _Sw0657840PortConfPortState_Type()
)
sw0657840PortConfPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840PortConfPortState.setStatus("current")


class _Sw0657840PortConfSpdDpx_Type(Integer32):
    """Custom type sw0657840PortConfSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Sw0657840PortConfSpdDpx_Type.__name__ = "Integer32"
_Sw0657840PortConfSpdDpx_Object = MibTableColumn
sw0657840PortConfSpdDpx = _Sw0657840PortConfSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 2, 2, 1, 3),
    _Sw0657840PortConfSpdDpx_Type()
)
sw0657840PortConfSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840PortConfSpdDpx.setStatus("current")


class _Sw0657840PortConfFlwCtrl_Type(Integer32):
    """Custom type sw0657840PortConfFlwCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840PortConfFlwCtrl_Type.__name__ = "Integer32"
_Sw0657840PortConfFlwCtrl_Object = MibTableColumn
sw0657840PortConfFlwCtrl = _Sw0657840PortConfFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 2, 2, 1, 4),
    _Sw0657840PortConfFlwCtrl_Type()
)
sw0657840PortConfFlwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840PortConfFlwCtrl.setStatus("current")
_Sw0657840PortConfDescription_Type = DisplayString
_Sw0657840PortConfDescription_Object = MibTableColumn
sw0657840PortConfDescription = _Sw0657840PortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 9, 2, 2, 1, 5),
    _Sw0657840PortConfDescription_Type()
)
sw0657840PortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840PortConfDescription.setStatus("current")
_Sw0657840Mirror_ObjectIdentity = ObjectIdentity
sw0657840Mirror = _Sw0657840Mirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 10)
)


class _Sw0657840MirrorMode_Type(Integer32):
    """Custom type sw0657840MirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840MirrorMode_Type.__name__ = "Integer32"
_Sw0657840MirrorMode_Object = MibScalar
sw0657840MirrorMode = _Sw0657840MirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 10, 1),
    _Sw0657840MirrorMode_Type()
)
sw0657840MirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840MirrorMode.setStatus("current")


class _Sw0657840MirroringPort_Type(Integer32):
    """Custom type sw0657840MirroringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840MirroringPort_Type.__name__ = "Integer32"
_Sw0657840MirroringPort_Object = MibScalar
sw0657840MirroringPort = _Sw0657840MirroringPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 10, 2),
    _Sw0657840MirroringPort_Type()
)
sw0657840MirroringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840MirroringPort.setStatus("current")
_Sw0657840MirroredPorts_Type = DisplayString
_Sw0657840MirroredPorts_Object = MibScalar
sw0657840MirroredPorts = _Sw0657840MirroredPorts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 10, 3),
    _Sw0657840MirroredPorts_Type()
)
sw0657840MirroredPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840MirroredPorts.setStatus("current")
_Sw0657840MaxPktLen_ObjectIdentity = ObjectIdentity
sw0657840MaxPktLen = _Sw0657840MaxPktLen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 11)
)
_Sw0657840MaxPktLen1_ObjectIdentity = ObjectIdentity
sw0657840MaxPktLen1 = _Sw0657840MaxPktLen1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 11, 1)
)


class _Sw0657840MaxPktLenPortNumber_Type(Integer32):
    """Custom type sw0657840MaxPktLenPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840MaxPktLenPortNumber_Type.__name__ = "Integer32"
_Sw0657840MaxPktLenPortNumber_Object = MibScalar
sw0657840MaxPktLenPortNumber = _Sw0657840MaxPktLenPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 11, 1, 1),
    _Sw0657840MaxPktLenPortNumber_Type()
)
sw0657840MaxPktLenPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840MaxPktLenPortNumber.setStatus("current")
_Sw0657840MaxPktLenConfTable_Object = MibTable
sw0657840MaxPktLenConfTable = _Sw0657840MaxPktLenConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    sw0657840MaxPktLenConfTable.setStatus("current")
_Sw0657840MaxPktLenConfEntry_Object = MibTableRow
sw0657840MaxPktLenConfEntry = _Sw0657840MaxPktLenConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 11, 1, 2, 1)
)
sw0657840MaxPktLenConfEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840MaxPktLenConfIndex"),
)
if mibBuilder.loadTexts:
    sw0657840MaxPktLenConfEntry.setStatus("current")


class _Sw0657840MaxPktLenConfIndex_Type(Integer32):
    """Custom type sw0657840MaxPktLenConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840MaxPktLenConfIndex_Type.__name__ = "Integer32"
_Sw0657840MaxPktLenConfIndex_Object = MibTableColumn
sw0657840MaxPktLenConfIndex = _Sw0657840MaxPktLenConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 11, 1, 2, 1, 1),
    _Sw0657840MaxPktLenConfIndex_Type()
)
sw0657840MaxPktLenConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840MaxPktLenConfIndex.setStatus("current")


class _Sw0657840MaxPktLenConfSetting_Type(Integer32):
    """Custom type sw0657840MaxPktLenConfSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 1518),
        ValueRangeConstraint(1532, 1532),
        ValueRangeConstraint(9216, 9216),
    )


_Sw0657840MaxPktLenConfSetting_Type.__name__ = "Integer32"
_Sw0657840MaxPktLenConfSetting_Object = MibTableColumn
sw0657840MaxPktLenConfSetting = _Sw0657840MaxPktLenConfSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 11, 1, 2, 1, 2),
    _Sw0657840MaxPktLenConfSetting_Type()
)
sw0657840MaxPktLenConfSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840MaxPktLenConfSetting.setStatus("current")
_Sw0657840Bandwidth_ObjectIdentity = ObjectIdentity
sw0657840Bandwidth = _Sw0657840Bandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12)
)
_Sw0657840Bandwidth1_ObjectIdentity = ObjectIdentity
sw0657840Bandwidth1 = _Sw0657840Bandwidth1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12, 1)
)


class _Sw0657840BandwidthPortNumber_Type(Integer32):
    """Custom type sw0657840BandwidthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840BandwidthPortNumber_Type.__name__ = "Integer32"
_Sw0657840BandwidthPortNumber_Object = MibScalar
sw0657840BandwidthPortNumber = _Sw0657840BandwidthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12, 1, 1),
    _Sw0657840BandwidthPortNumber_Type()
)
sw0657840BandwidthPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840BandwidthPortNumber.setStatus("current")
_Sw0657840BandwidthConfTable_Object = MibTable
sw0657840BandwidthConfTable = _Sw0657840BandwidthConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    sw0657840BandwidthConfTable.setStatus("current")
_Sw0657840BandwidthConfEntry_Object = MibTableRow
sw0657840BandwidthConfEntry = _Sw0657840BandwidthConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12, 1, 2, 1)
)
sw0657840BandwidthConfEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840BandwidthConfIndex"),
)
if mibBuilder.loadTexts:
    sw0657840BandwidthConfEntry.setStatus("current")


class _Sw0657840BandwidthConfIndex_Type(Integer32):
    """Custom type sw0657840BandwidthConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840BandwidthConfIndex_Type.__name__ = "Integer32"
_Sw0657840BandwidthConfIndex_Object = MibTableColumn
sw0657840BandwidthConfIndex = _Sw0657840BandwidthConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12, 1, 2, 1, 1),
    _Sw0657840BandwidthConfIndex_Type()
)
sw0657840BandwidthConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840BandwidthConfIndex.setStatus("current")


class _Sw0657840BandwidthConfIngressState_Type(Integer32):
    """Custom type sw0657840BandwidthConfIngressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840BandwidthConfIngressState_Type.__name__ = "Integer32"
_Sw0657840BandwidthConfIngressState_Object = MibTableColumn
sw0657840BandwidthConfIngressState = _Sw0657840BandwidthConfIngressState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12, 1, 2, 1, 2),
    _Sw0657840BandwidthConfIngressState_Type()
)
sw0657840BandwidthConfIngressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840BandwidthConfIngressState.setStatus("current")


class _Sw0657840BandwidthConfIngressBW_Type(Integer32):
    """Custom type sw0657840BandwidthConfIngressBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Sw0657840BandwidthConfIngressBW_Type.__name__ = "Integer32"
_Sw0657840BandwidthConfIngressBW_Object = MibTableColumn
sw0657840BandwidthConfIngressBW = _Sw0657840BandwidthConfIngressBW_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12, 1, 2, 1, 3),
    _Sw0657840BandwidthConfIngressBW_Type()
)
sw0657840BandwidthConfIngressBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840BandwidthConfIngressBW.setStatus("current")


class _Sw0657840BandwidthConfStormState_Type(Integer32):
    """Custom type sw0657840BandwidthConfStormState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840BandwidthConfStormState_Type.__name__ = "Integer32"
_Sw0657840BandwidthConfStormState_Object = MibTableColumn
sw0657840BandwidthConfStormState = _Sw0657840BandwidthConfStormState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12, 1, 2, 1, 4),
    _Sw0657840BandwidthConfStormState_Type()
)
sw0657840BandwidthConfStormState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840BandwidthConfStormState.setStatus("current")


class _Sw0657840BandwidthConfStormBW_Type(Integer32):
    """Custom type sw0657840BandwidthConfStormBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Sw0657840BandwidthConfStormBW_Type.__name__ = "Integer32"
_Sw0657840BandwidthConfStormBW_Object = MibTableColumn
sw0657840BandwidthConfStormBW = _Sw0657840BandwidthConfStormBW_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12, 1, 2, 1, 5),
    _Sw0657840BandwidthConfStormBW_Type()
)
sw0657840BandwidthConfStormBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840BandwidthConfStormBW.setStatus("current")


class _Sw0657840BandwidthConfEgressState_Type(Integer32):
    """Custom type sw0657840BandwidthConfEgressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840BandwidthConfEgressState_Type.__name__ = "Integer32"
_Sw0657840BandwidthConfEgressState_Object = MibTableColumn
sw0657840BandwidthConfEgressState = _Sw0657840BandwidthConfEgressState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12, 1, 2, 1, 6),
    _Sw0657840BandwidthConfEgressState_Type()
)
sw0657840BandwidthConfEgressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840BandwidthConfEgressState.setStatus("current")


class _Sw0657840BandwidthConfEgressBW_Type(Integer32):
    """Custom type sw0657840BandwidthConfEgressBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Sw0657840BandwidthConfEgressBW_Type.__name__ = "Integer32"
_Sw0657840BandwidthConfEgressBW_Object = MibTableColumn
sw0657840BandwidthConfEgressBW = _Sw0657840BandwidthConfEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 12, 1, 2, 1, 7),
    _Sw0657840BandwidthConfEgressBW_Type()
)
sw0657840BandwidthConfEgressBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840BandwidthConfEgressBW.setStatus("current")
_Sw0657840LoopDetectedConf_ObjectIdentity = ObjectIdentity
sw0657840LoopDetectedConf = _Sw0657840LoopDetectedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 13)
)


class _Sw0657840LoopDetectedNumber_Type(Integer32):
    """Custom type sw0657840LoopDetectedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840LoopDetectedNumber_Type.__name__ = "Integer32"
_Sw0657840LoopDetectedNumber_Object = MibScalar
sw0657840LoopDetectedNumber = _Sw0657840LoopDetectedNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 13, 1),
    _Sw0657840LoopDetectedNumber_Type()
)
sw0657840LoopDetectedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840LoopDetectedNumber.setStatus("current")
_Sw0657840LoopDetectedTable_Object = MibTable
sw0657840LoopDetectedTable = _Sw0657840LoopDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 13, 2)
)
if mibBuilder.loadTexts:
    sw0657840LoopDetectedTable.setStatus("current")
_Sw0657840LoopDetectedEntry_Object = MibTableRow
sw0657840LoopDetectedEntry = _Sw0657840LoopDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 13, 2, 1)
)
sw0657840LoopDetectedEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840LoopDetectedfIndex"),
)
if mibBuilder.loadTexts:
    sw0657840LoopDetectedEntry.setStatus("current")


class _Sw0657840LoopDetectedfIndex_Type(Integer32):
    """Custom type sw0657840LoopDetectedfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840LoopDetectedfIndex_Type.__name__ = "Integer32"
_Sw0657840LoopDetectedfIndex_Object = MibTableColumn
sw0657840LoopDetectedfIndex = _Sw0657840LoopDetectedfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 13, 2, 1, 1),
    _Sw0657840LoopDetectedfIndex_Type()
)
sw0657840LoopDetectedfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840LoopDetectedfIndex.setStatus("current")


class _Sw0657840LoopDetectedStateEbl_Type(Integer32):
    """Custom type sw0657840LoopDetectedStateEbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840LoopDetectedStateEbl_Type.__name__ = "Integer32"
_Sw0657840LoopDetectedStateEbl_Object = MibTableColumn
sw0657840LoopDetectedStateEbl = _Sw0657840LoopDetectedStateEbl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 13, 2, 1, 2),
    _Sw0657840LoopDetectedStateEbl_Type()
)
sw0657840LoopDetectedStateEbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840LoopDetectedStateEbl.setStatus("current")


class _Sw0657840LoopDetectedCurrentStatus_Type(Integer32):
    """Custom type sw0657840LoopDetectedCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840LoopDetectedCurrentStatus_Type.__name__ = "Integer32"
_Sw0657840LoopDetectedCurrentStatus_Object = MibTableColumn
sw0657840LoopDetectedCurrentStatus = _Sw0657840LoopDetectedCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 13, 2, 1, 3),
    _Sw0657840LoopDetectedCurrentStatus_Type()
)
sw0657840LoopDetectedCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840LoopDetectedCurrentStatus.setStatus("current")


class _Sw0657840LoopDetectedResumed_Type(Integer32):
    """Custom type sw0657840LoopDetectedResumed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840LoopDetectedResumed_Type.__name__ = "Integer32"
_Sw0657840LoopDetectedResumed_Object = MibTableColumn
sw0657840LoopDetectedResumed = _Sw0657840LoopDetectedResumed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 13, 2, 1, 4),
    _Sw0657840LoopDetectedResumed_Type()
)
sw0657840LoopDetectedResumed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840LoopDetectedResumed.setStatus("current")


class _Sw0657840LoopDetectedAction_Type(Integer32):
    """Custom type sw0657840LoopDetectedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Sw0657840LoopDetectedAction_Type.__name__ = "Integer32"
_Sw0657840LoopDetectedAction_Object = MibScalar
sw0657840LoopDetectedAction = _Sw0657840LoopDetectedAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 13, 3),
    _Sw0657840LoopDetectedAction_Type()
)
sw0657840LoopDetectedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw0657840LoopDetectedAction.setStatus("current")
_Sw0657840SFPInfo_ObjectIdentity = ObjectIdentity
sw0657840SFPInfo = _Sw0657840SFPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14)
)


class _Sw0657840SFPInfoNumber_Type(Integer32):
    """Custom type sw0657840SFPInfoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840SFPInfoNumber_Type.__name__ = "Integer32"
_Sw0657840SFPInfoNumber_Object = MibScalar
sw0657840SFPInfoNumber = _Sw0657840SFPInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 1),
    _Sw0657840SFPInfoNumber_Type()
)
sw0657840SFPInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPInfoNumber.setStatus("current")
_Sw0657840SFPInfoTable_Object = MibTable
sw0657840SFPInfoTable = _Sw0657840SFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2)
)
if mibBuilder.loadTexts:
    sw0657840SFPInfoTable.setStatus("current")
_Sw0657840SFPInfoEntry_Object = MibTableRow
sw0657840SFPInfoEntry = _Sw0657840SFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1)
)
sw0657840SFPInfoEntry.setIndexNames(
    (0, "PRIVATE-SW0657840-MIB", "sw0657840SFPInfoIndex"),
)
if mibBuilder.loadTexts:
    sw0657840SFPInfoEntry.setStatus("current")


class _Sw0657840SFPInfoIndex_Type(Integer32):
    """Custom type sw0657840SFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sw0657840SFPInfoIndex_Type.__name__ = "Integer32"
_Sw0657840SFPInfoIndex_Object = MibTableColumn
sw0657840SFPInfoIndex = _Sw0657840SFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 1),
    _Sw0657840SFPInfoIndex_Type()
)
sw0657840SFPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPInfoIndex.setStatus("current")
_Sw0657840SFPConnectorType_Type = DisplayString
_Sw0657840SFPConnectorType_Object = MibTableColumn
sw0657840SFPConnectorType = _Sw0657840SFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 2),
    _Sw0657840SFPConnectorType_Type()
)
sw0657840SFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPConnectorType.setStatus("current")
_Sw0657840SFPFiberType_Type = DisplayString
_Sw0657840SFPFiberType_Object = MibTableColumn
sw0657840SFPFiberType = _Sw0657840SFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 3),
    _Sw0657840SFPFiberType_Type()
)
sw0657840SFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPFiberType.setStatus("current")
_Sw0657840SFPWavelength_Type = DisplayString
_Sw0657840SFPWavelength_Object = MibTableColumn
sw0657840SFPWavelength = _Sw0657840SFPWavelength_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 4),
    _Sw0657840SFPWavelength_Type()
)
sw0657840SFPWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPWavelength.setStatus("current")
_Sw0657840SFPBaudRate_Type = DisplayString
_Sw0657840SFPBaudRate_Object = MibTableColumn
sw0657840SFPBaudRate = _Sw0657840SFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 5),
    _Sw0657840SFPBaudRate_Type()
)
sw0657840SFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPBaudRate.setStatus("current")
_Sw0657840SFPVendorOUI_Type = DisplayString
_Sw0657840SFPVendorOUI_Object = MibTableColumn
sw0657840SFPVendorOUI = _Sw0657840SFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 6),
    _Sw0657840SFPVendorOUI_Type()
)
sw0657840SFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPVendorOUI.setStatus("current")
_Sw0657840SFPVendorName_Type = DisplayString
_Sw0657840SFPVendorName_Object = MibTableColumn
sw0657840SFPVendorName = _Sw0657840SFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 7),
    _Sw0657840SFPVendorName_Type()
)
sw0657840SFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPVendorName.setStatus("current")
_Sw0657840SFPVendorPN_Type = DisplayString
_Sw0657840SFPVendorPN_Object = MibTableColumn
sw0657840SFPVendorPN = _Sw0657840SFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 8),
    _Sw0657840SFPVendorPN_Type()
)
sw0657840SFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPVendorPN.setStatus("current")
_Sw0657840SFPVendorRev_Type = DisplayString
_Sw0657840SFPVendorRev_Object = MibTableColumn
sw0657840SFPVendorRev = _Sw0657840SFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 9),
    _Sw0657840SFPVendorRev_Type()
)
sw0657840SFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPVendorRev.setStatus("current")
_Sw0657840SFPVendorSN_Type = DisplayString
_Sw0657840SFPVendorSN_Object = MibTableColumn
sw0657840SFPVendorSN = _Sw0657840SFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 10),
    _Sw0657840SFPVendorSN_Type()
)
sw0657840SFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPVendorSN.setStatus("current")
_Sw0657840SFPDateCode_Type = DisplayString
_Sw0657840SFPDateCode_Object = MibTableColumn
sw0657840SFPDateCode = _Sw0657840SFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 11),
    _Sw0657840SFPDateCode_Type()
)
sw0657840SFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPDateCode.setStatus("current")
_Sw0657840SFPTemperature_Type = DisplayString
_Sw0657840SFPTemperature_Object = MibTableColumn
sw0657840SFPTemperature = _Sw0657840SFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 12),
    _Sw0657840SFPTemperature_Type()
)
sw0657840SFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPTemperature.setStatus("current")
_Sw0657840SFPVcc_Type = DisplayString
_Sw0657840SFPVcc_Object = MibTableColumn
sw0657840SFPVcc = _Sw0657840SFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 13),
    _Sw0657840SFPVcc_Type()
)
sw0657840SFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPVcc.setStatus("current")
_Sw0657840SFPTxBias_Type = DisplayString
_Sw0657840SFPTxBias_Object = MibTableColumn
sw0657840SFPTxBias = _Sw0657840SFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 14),
    _Sw0657840SFPTxBias_Type()
)
sw0657840SFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPTxBias.setStatus("current")
_Sw0657840SFPTxPWR_Type = DisplayString
_Sw0657840SFPTxPWR_Object = MibTableColumn
sw0657840SFPTxPWR = _Sw0657840SFPTxPWR_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 15),
    _Sw0657840SFPTxPWR_Type()
)
sw0657840SFPTxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPTxPWR.setStatus("current")
_Sw0657840SFPRxPWR_Type = DisplayString
_Sw0657840SFPRxPWR_Object = MibTableColumn
sw0657840SFPRxPWR = _Sw0657840SFPRxPWR_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 14, 2, 1, 16),
    _Sw0657840SFPRxPWR_Type()
)
sw0657840SFPRxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw0657840SFPRxPWR.setStatus("current")
_Sw0657840TrapEntry_ObjectIdentity = ObjectIdentity
sw0657840TrapEntry = _Sw0657840TrapEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20)
)
_Sw0657840TrapVariable_ObjectIdentity = ObjectIdentity
sw0657840TrapVariable = _Sw0657840TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 21)
)
_Username_Type = DisplayString
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 21, 1),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 21, 2),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 21, 3),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 21, 4),
    _Partnerkey_Type()
)
partnerkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerkey.setStatus("current")
_Uplink_Type = DisplayString
_Uplink_Object = MibScalar
uplink = _Uplink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 21, 5),
    _Uplink_Type()
)
uplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplink.setStatus("current")

# Managed Objects groups


# Notification objects

sw0657840ModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 1)
)
sw0657840ModuleInserted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    sw0657840ModuleInserted.setStatus(
        "current"
    )

sw0657840ModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 2)
)
sw0657840ModuleRemoved.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    sw0657840ModuleRemoved.setStatus(
        "current"
    )

sw0657840DualMediaSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 3)
)
sw0657840DualMediaSwapped.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    sw0657840DualMediaSwapped.setStatus(
        "current"
    )

sw0657840LoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 5)
)
sw0657840LoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    sw0657840LoopDetected.setStatus(
        "current"
    )

sw0657840StpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 100)
)
if mibBuilder.loadTexts:
    sw0657840StpStateDisabled.setStatus(
        "current"
    )

sw0657840StpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 101)
)
if mibBuilder.loadTexts:
    sw0657840StpStateEnabled.setStatus(
        "current"
    )

sw0657840StpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 102)
)
sw0657840StpTopologyChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    sw0657840StpTopologyChanged.setStatus(
        "current"
    )

sw0657840LacpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 120)
)
sw0657840LacpStateDisabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-SW0657840-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    sw0657840LacpStateDisabled.setStatus(
        "current"
    )

sw0657840LacpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 121)
)
sw0657840LacpStateEnabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-SW0657840-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    sw0657840LacpStateEnabled.setStatus(
        "current"
    )

sw0657840LacpPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 123)
)
sw0657840LacpPortAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-SW0657840-MIB", "actorkey"),
        ("PRIVATE-SW0657840-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    sw0657840LacpPortAdded.setStatus(
        "current"
    )

sw0657840LacpPortTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 124)
)
sw0657840LacpPortTrunkFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-SW0657840-MIB", "actorkey"),
        ("PRIVATE-SW0657840-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    sw0657840LacpPortTrunkFailure.setStatus(
        "current"
    )

sw0657840GvrpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 140)
)
if mibBuilder.loadTexts:
    sw0657840GvrpStateDisabled.setStatus(
        "current"
    )

sw0657840GvrpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 141)
)
if mibBuilder.loadTexts:
    sw0657840GvrpStateEnabled.setStatus(
        "current"
    )

sw0657840VlanStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 150)
)
if mibBuilder.loadTexts:
    sw0657840VlanStateDisabled.setStatus(
        "current"
    )

sw0657840VlanPortBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 151)
)
if mibBuilder.loadTexts:
    sw0657840VlanPortBaseEnabled.setStatus(
        "current"
    )

sw0657840VlanTagBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 152)
)
if mibBuilder.loadTexts:
    sw0657840VlanTagBaseEnabled.setStatus(
        "current"
    )

sw0657840VlanMetroModeEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 153)
)
sw0657840VlanMetroModeEnabled.setObjects(
    ("PRIVATE-SW0657840-MIB", "uplink")
)
if mibBuilder.loadTexts:
    sw0657840VlanMetroModeEnabled.setStatus(
        "current"
    )

sw0657840VlanDoubleTagEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 154)
)
if mibBuilder.loadTexts:
    sw0657840VlanDoubleTagEnabled.setStatus(
        "current"
    )

sw0657840UserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 200)
)
sw0657840UserLogin.setObjects(
    ("PRIVATE-SW0657840-MIB", "username")
)
if mibBuilder.loadTexts:
    sw0657840UserLogin.setStatus(
        "current"
    )

sw0657840UserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 9, 1, 20, 201)
)
sw0657840UserLogout.setObjects(
    ("PRIVATE-SW0657840-MIB", "username")
)
if mibBuilder.loadTexts:
    sw0657840UserLogout.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRIVATE-SW0657840-MIB",
    **{"privatetech": privatetech,
       "switch": switch,
       "sw0657840ProductID": sw0657840ProductID,
       "sw0657840Produces": sw0657840Produces,
       "sw0657840System": sw0657840System,
       "sw0657840CommonSys": sw0657840CommonSys,
       "sw0657840Reboot": sw0657840Reboot,
       "sw0657840BiosVsersion": sw0657840BiosVsersion,
       "sw0657840FirmwareVersion": sw0657840FirmwareVersion,
       "sw0657840HardwareVersion": sw0657840HardwareVersion,
       "sw0657840MechanicalVersion": sw0657840MechanicalVersion,
       "sw0657840SerialNumber": sw0657840SerialNumber,
       "sw0657840HostMacAddress": sw0657840HostMacAddress,
       "sw0657840DevicePort": sw0657840DevicePort,
       "sw0657840RamSize": sw0657840RamSize,
       "sw0657840FlashSize": sw0657840FlashSize,
       "sw0657840IP": sw0657840IP,
       "sw0657840DhcpSetting": sw0657840DhcpSetting,
       "sw0657840IPAddress": sw0657840IPAddress,
       "sw0657840NetMask": sw0657840NetMask,
       "sw0657840DefaultGateway": sw0657840DefaultGateway,
       "sw0657840DnsSetting": sw0657840DnsSetting,
       "sw0657840DnsServer": sw0657840DnsServer,
       "sw0657840Time": sw0657840Time,
       "sw0657840SystemCurrentTime": sw0657840SystemCurrentTime,
       "sw0657840ManualTimeSetting": sw0657840ManualTimeSetting,
       "sw0657840NTPServer": sw0657840NTPServer,
       "sw0657840NTPTimeZone": sw0657840NTPTimeZone,
       "sw0657840NTPTimeSync": sw0657840NTPTimeSync,
       "sw0657840DaylightSavingTime": sw0657840DaylightSavingTime,
       "sw0657840DaylightStartTime": sw0657840DaylightStartTime,
       "sw0657840DaylightEndTime": sw0657840DaylightEndTime,
       "sw0657840Account": sw0657840Account,
       "sw0657840AccountNumber": sw0657840AccountNumber,
       "sw0657840AccountTable": sw0657840AccountTable,
       "sw0657840AccountEntry": sw0657840AccountEntry,
       "sw0657840AccountIndex": sw0657840AccountIndex,
       "sw0657840AccountAuthorization": sw0657840AccountAuthorization,
       "sw0657840AccountName": sw0657840AccountName,
       "sw0657840AccountPassword": sw0657840AccountPassword,
       "sw0657840AccountAddName": sw0657840AccountAddName,
       "sw0657840AccountAddPassword": sw0657840AccountAddPassword,
       "sw0657840DoAccountAdd": sw0657840DoAccountAdd,
       "sw0657840AccountDel": sw0657840AccountDel,
       "sw0657840Snmp": sw0657840Snmp,
       "sw0657840GetCommunity": sw0657840GetCommunity,
       "sw0657840SetCommunity": sw0657840SetCommunity,
       "sw0657840TrapHostNumber": sw0657840TrapHostNumber,
       "sw0657840TrapHostTable": sw0657840TrapHostTable,
       "sw0657840TrapHostEntry": sw0657840TrapHostEntry,
       "sw0657840TrapHostIndex": sw0657840TrapHostIndex,
       "sw0657840TrapHostIP": sw0657840TrapHostIP,
       "sw0657840TrapHostPort": sw0657840TrapHostPort,
       "sw0657840TrapHostCommunity": sw0657840TrapHostCommunity,
       "sw0657840Alarm": sw0657840Alarm,
       "sw0657840Event": sw0657840Event,
       "sw0657840EventNumber": sw0657840EventNumber,
       "sw0657840EventTable": sw0657840EventTable,
       "sw0657840EventEntry": sw0657840EventEntry,
       "sw0657840EventIndex": sw0657840EventIndex,
       "sw0657840EventName": sw0657840EventName,
       "sw0657840EventSendEmail": sw0657840EventSendEmail,
       "sw0657840EventSendSMS": sw0657840EventSendSMS,
       "sw0657840EventSendTrap": sw0657840EventSendTrap,
       "sw0657840Email": sw0657840Email,
       "sw0657840EmailServer": sw0657840EmailServer,
       "sw0657840EmailUsername": sw0657840EmailUsername,
       "sw0657840EmailPassword": sw0657840EmailPassword,
       "sw0657840EmailUserNumber": sw0657840EmailUserNumber,
       "sw0657840EmailUserTable": sw0657840EmailUserTable,
       "sw0657840EmailUserEntry": sw0657840EmailUserEntry,
       "sw0657840EmailUserIndex": sw0657840EmailUserIndex,
       "sw0657840EmailUserAddress": sw0657840EmailUserAddress,
       "sw0657840SMS": sw0657840SMS,
       "sw0657840SMSServer": sw0657840SMSServer,
       "sw0657840SMSUsername": sw0657840SMSUsername,
       "sw0657840SMSPassword": sw0657840SMSPassword,
       "sw0657840SMSUserNumber": sw0657840SMSUserNumber,
       "sw0657840SMSUserTable": sw0657840SMSUserTable,
       "sw0657840SMSUserEntry": sw0657840SMSUserEntry,
       "sw0657840SMSUserIndex": sw0657840SMSUserIndex,
       "sw0657840SMSUserMobilePhone": sw0657840SMSUserMobilePhone,
       "sw0657840Tftp": sw0657840Tftp,
       "sw0657840TftpServer": sw0657840TftpServer,
       "sw0657840Configuration": sw0657840Configuration,
       "sw0657840SaveRestore": sw0657840SaveRestore,
       "sw0657840SaveStart": sw0657840SaveStart,
       "sw0657840SaveUser": sw0657840SaveUser,
       "sw0657840RestoreDefault": sw0657840RestoreDefault,
       "sw0657840RestoreUser": sw0657840RestoreUser,
       "sw0657840ConfigFile": sw0657840ConfigFile,
       "sw0657840ExportConfigName": sw0657840ExportConfigName,
       "sw0657840DoExportConfig": sw0657840DoExportConfig,
       "sw0657840ImportConfigName": sw0657840ImportConfigName,
       "sw0657840DoImportConfig": sw0657840DoImportConfig,
       "sw0657840Diagnostic": sw0657840Diagnostic,
       "sw0657840EEPROMTest": sw0657840EEPROMTest,
       "sw0657840UartTest": sw0657840UartTest,
       "sw0657840DramTest": sw0657840DramTest,
       "sw0657840FlashTest": sw0657840FlashTest,
       "sw0657840InternalLoopbackTest": sw0657840InternalLoopbackTest,
       "sw0657840ExternalLoopbackTest": sw0657840ExternalLoopbackTest,
       "sw0657840PingTest": sw0657840PingTest,
       "sw0657840Log": sw0657840Log,
       "sw0657840ClearLog": sw0657840ClearLog,
       "sw0657840UploadLog": sw0657840UploadLog,
       "sw0657840AutoUploadLogState": sw0657840AutoUploadLogState,
       "sw0657840LogNumber": sw0657840LogNumber,
       "sw0657840LogTable": sw0657840LogTable,
       "sw0657840LogEntry": sw0657840LogEntry,
       "sw0657840LogIndex": sw0657840LogIndex,
       "sw0657840LogEvent": sw0657840LogEvent,
       "sw0657840Firmware": sw0657840Firmware,
       "sw0657840FirmwareFileName": sw0657840FirmwareFileName,
       "sw0657840DoFirmwareUpgrade": sw0657840DoFirmwareUpgrade,
       "sw0657840Port": sw0657840Port,
       "sw0657840PortStatus": sw0657840PortStatus,
       "sw0657840PortStatusNumber": sw0657840PortStatusNumber,
       "sw0657840PortStatusTable": sw0657840PortStatusTable,
       "sw0657840PortStatusEntry": sw0657840PortStatusEntry,
       "sw0657840PortStatusIndex": sw0657840PortStatusIndex,
       "sw0657840PortStatusMedia": sw0657840PortStatusMedia,
       "sw0657840PortStatusLink": sw0657840PortStatusLink,
       "sw0657840PortStatusPortState": sw0657840PortStatusPortState,
       "sw0657840PortStatusAutoNego": sw0657840PortStatusAutoNego,
       "sw0657840PortStatusSpdDpx": sw0657840PortStatusSpdDpx,
       "sw0657840PortStatusFlwCtrl": sw0657840PortStatusFlwCtrl,
       "sw0657840PortStatuDescription": sw0657840PortStatuDescription,
       "sw0657840PortConf": sw0657840PortConf,
       "sw0657840PortConfNumber": sw0657840PortConfNumber,
       "sw0657840PortConfTable": sw0657840PortConfTable,
       "sw0657840PortConfEntry": sw0657840PortConfEntry,
       "sw0657840PortConfIndex": sw0657840PortConfIndex,
       "sw0657840PortConfPortState": sw0657840PortConfPortState,
       "sw0657840PortConfSpdDpx": sw0657840PortConfSpdDpx,
       "sw0657840PortConfFlwCtrl": sw0657840PortConfFlwCtrl,
       "sw0657840PortConfDescription": sw0657840PortConfDescription,
       "sw0657840Mirror": sw0657840Mirror,
       "sw0657840MirrorMode": sw0657840MirrorMode,
       "sw0657840MirroringPort": sw0657840MirroringPort,
       "sw0657840MirroredPorts": sw0657840MirroredPorts,
       "sw0657840MaxPktLen": sw0657840MaxPktLen,
       "sw0657840MaxPktLen1": sw0657840MaxPktLen1,
       "sw0657840MaxPktLenPortNumber": sw0657840MaxPktLenPortNumber,
       "sw0657840MaxPktLenConfTable": sw0657840MaxPktLenConfTable,
       "sw0657840MaxPktLenConfEntry": sw0657840MaxPktLenConfEntry,
       "sw0657840MaxPktLenConfIndex": sw0657840MaxPktLenConfIndex,
       "sw0657840MaxPktLenConfSetting": sw0657840MaxPktLenConfSetting,
       "sw0657840Bandwidth": sw0657840Bandwidth,
       "sw0657840Bandwidth1": sw0657840Bandwidth1,
       "sw0657840BandwidthPortNumber": sw0657840BandwidthPortNumber,
       "sw0657840BandwidthConfTable": sw0657840BandwidthConfTable,
       "sw0657840BandwidthConfEntry": sw0657840BandwidthConfEntry,
       "sw0657840BandwidthConfIndex": sw0657840BandwidthConfIndex,
       "sw0657840BandwidthConfIngressState": sw0657840BandwidthConfIngressState,
       "sw0657840BandwidthConfIngressBW": sw0657840BandwidthConfIngressBW,
       "sw0657840BandwidthConfStormState": sw0657840BandwidthConfStormState,
       "sw0657840BandwidthConfStormBW": sw0657840BandwidthConfStormBW,
       "sw0657840BandwidthConfEgressState": sw0657840BandwidthConfEgressState,
       "sw0657840BandwidthConfEgressBW": sw0657840BandwidthConfEgressBW,
       "sw0657840LoopDetectedConf": sw0657840LoopDetectedConf,
       "sw0657840LoopDetectedNumber": sw0657840LoopDetectedNumber,
       "sw0657840LoopDetectedTable": sw0657840LoopDetectedTable,
       "sw0657840LoopDetectedEntry": sw0657840LoopDetectedEntry,
       "sw0657840LoopDetectedfIndex": sw0657840LoopDetectedfIndex,
       "sw0657840LoopDetectedStateEbl": sw0657840LoopDetectedStateEbl,
       "sw0657840LoopDetectedCurrentStatus": sw0657840LoopDetectedCurrentStatus,
       "sw0657840LoopDetectedResumed": sw0657840LoopDetectedResumed,
       "sw0657840LoopDetectedAction": sw0657840LoopDetectedAction,
       "sw0657840SFPInfo": sw0657840SFPInfo,
       "sw0657840SFPInfoNumber": sw0657840SFPInfoNumber,
       "sw0657840SFPInfoTable": sw0657840SFPInfoTable,
       "sw0657840SFPInfoEntry": sw0657840SFPInfoEntry,
       "sw0657840SFPInfoIndex": sw0657840SFPInfoIndex,
       "sw0657840SFPConnectorType": sw0657840SFPConnectorType,
       "sw0657840SFPFiberType": sw0657840SFPFiberType,
       "sw0657840SFPWavelength": sw0657840SFPWavelength,
       "sw0657840SFPBaudRate": sw0657840SFPBaudRate,
       "sw0657840SFPVendorOUI": sw0657840SFPVendorOUI,
       "sw0657840SFPVendorName": sw0657840SFPVendorName,
       "sw0657840SFPVendorPN": sw0657840SFPVendorPN,
       "sw0657840SFPVendorRev": sw0657840SFPVendorRev,
       "sw0657840SFPVendorSN": sw0657840SFPVendorSN,
       "sw0657840SFPDateCode": sw0657840SFPDateCode,
       "sw0657840SFPTemperature": sw0657840SFPTemperature,
       "sw0657840SFPVcc": sw0657840SFPVcc,
       "sw0657840SFPTxBias": sw0657840SFPTxBias,
       "sw0657840SFPTxPWR": sw0657840SFPTxPWR,
       "sw0657840SFPRxPWR": sw0657840SFPRxPWR,
       "sw0657840TrapEntry": sw0657840TrapEntry,
       "sw0657840ModuleInserted": sw0657840ModuleInserted,
       "sw0657840ModuleRemoved": sw0657840ModuleRemoved,
       "sw0657840DualMediaSwapped": sw0657840DualMediaSwapped,
       "sw0657840LoopDetected": sw0657840LoopDetected,
       "sw0657840StpStateDisabled": sw0657840StpStateDisabled,
       "sw0657840StpStateEnabled": sw0657840StpStateEnabled,
       "sw0657840StpTopologyChanged": sw0657840StpTopologyChanged,
       "sw0657840LacpStateDisabled": sw0657840LacpStateDisabled,
       "sw0657840LacpStateEnabled": sw0657840LacpStateEnabled,
       "sw0657840LacpPortAdded": sw0657840LacpPortAdded,
       "sw0657840LacpPortTrunkFailure": sw0657840LacpPortTrunkFailure,
       "sw0657840GvrpStateDisabled": sw0657840GvrpStateDisabled,
       "sw0657840GvrpStateEnabled": sw0657840GvrpStateEnabled,
       "sw0657840VlanStateDisabled": sw0657840VlanStateDisabled,
       "sw0657840VlanPortBaseEnabled": sw0657840VlanPortBaseEnabled,
       "sw0657840VlanTagBaseEnabled": sw0657840VlanTagBaseEnabled,
       "sw0657840VlanMetroModeEnabled": sw0657840VlanMetroModeEnabled,
       "sw0657840VlanDoubleTagEnabled": sw0657840VlanDoubleTagEnabled,
       "sw0657840UserLogin": sw0657840UserLogin,
       "sw0657840UserLogout": sw0657840UserLogout,
       "sw0657840TrapVariable": sw0657840TrapVariable,
       "username": username,
       "groupId": groupId,
       "actorkey": actorkey,
       "partnerkey": partnerkey,
       "uplink": uplink}
)
