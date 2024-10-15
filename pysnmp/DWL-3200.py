# SNMP MIB module (DWL-3200) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DWL-3200
# Produced by pysmi-1.5.4 at Mon Oct 14 21:34:00 2024
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
 iso,
 private) = mibBuilder.importSymbols(
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
    "iso",
    "private")

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_Dlink_products_ObjectIdentity = ObjectIdentity
dlink_products = _Dlink_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10)
)
_Dlink_dwlfamily_ObjectIdentity = ObjectIdentity
dlink_dwlfamily = _Dlink_dwlfamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37)
)
_Dwl_3200AP_ObjectIdentity = ObjectIdentity
dwl_3200AP = _Dwl_3200AP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20)
)
_SystemInformation_ObjectIdentity = ObjectIdentity
systemInformation = _SystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 1)
)


class _SystemDescr_Type(DisplayString):
    """Custom type systemDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemDescr_Type.__name__ = "DisplayString"
_SystemDescr_Object = MibScalar
systemDescr = _SystemDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 1, 1),
    _SystemDescr_Type()
)
systemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDescr.setStatus("mandatory")
_SystemUpTime_Type = TimeTicks
_SystemUpTime_Object = MibScalar
systemUpTime = _SystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 1, 3),
    _SystemUpTime_Type()
)
systemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTime.setStatus("mandatory")


class _SystemContact_Type(DisplayString):
    """Custom type systemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemContact_Type.__name__ = "DisplayString"
_SystemContact_Object = MibScalar
systemContact = _SystemContact_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 1, 4),
    _SystemContact_Type()
)
systemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemContact.setStatus("mandatory")


class _SystemLocation_Type(DisplayString):
    """Custom type systemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemLocation_Type.__name__ = "DisplayString"
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 1, 6),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocation.setStatus("mandatory")


class _SystemModelName_Type(DisplayString):
    """Custom type systemModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemModelName_Type.__name__ = "DisplayString"
_SystemModelName_Object = MibScalar
systemModelName = _SystemModelName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 1, 8),
    _SystemModelName_Type()
)
systemModelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemModelName.setStatus("mandatory")


class _SystemFirmwareVersion_Type(DisplayString):
    """Custom type systemFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemFirmwareVersion_Type.__name__ = "DisplayString"
_SystemFirmwareVersion_Object = MibScalar
systemFirmwareVersion = _SystemFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 1, 9),
    _SystemFirmwareVersion_Type()
)
systemFirmwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFirmwareVersion.setStatus("mandatory")
_SystemIpAddress_Type = IpAddress
_SystemIpAddress_Object = MibScalar
systemIpAddress = _SystemIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 1, 10),
    _SystemIpAddress_Type()
)
systemIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemIpAddress.setStatus("mandatory")
_SystemTime_Type = OctetString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 1, 11),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("mandatory")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2)
)
_Lan_ObjectIdentity = ObjectIdentity
lan = _Lan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1)
)
_LanIfSetting_ObjectIdentity = ObjectIdentity
lanIfSetting = _LanIfSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 1)
)
_LanIfSettingTable_Object = MibTable
lanIfSettingTable = _LanIfSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lanIfSettingTable.setStatus("mandatory")
_LanIfSettingEntry_Object = MibTableRow
lanIfSettingEntry = _LanIfSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 1, 1, 1)
)
lanIfSettingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lanIfSettingEntry.setStatus("mandatory")


class _LanIfGetIpAddressFrom_Type(Integer32):
    """Custom type lanIfGetIpAddressFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_LanIfGetIpAddressFrom_Type.__name__ = "Integer32"
_LanIfGetIpAddressFrom_Object = MibTableColumn
lanIfGetIpAddressFrom = _LanIfGetIpAddressFrom_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 1, 1, 1, 1),
    _LanIfGetIpAddressFrom_Type()
)
lanIfGetIpAddressFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIfGetIpAddressFrom.setStatus("mandatory")
_LanIfIpAddress_Type = IpAddress
_LanIfIpAddress_Object = MibTableColumn
lanIfIpAddress = _LanIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 1, 1, 1, 2),
    _LanIfIpAddress_Type()
)
lanIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIfIpAddress.setStatus("mandatory")
_LanIfSubnetMask_Type = IpAddress
_LanIfSubnetMask_Object = MibTableColumn
lanIfSubnetMask = _LanIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 1, 1, 1, 3),
    _LanIfSubnetMask_Type()
)
lanIfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIfSubnetMask.setStatus("mandatory")
_LanIfDefaultGateway_Type = IpAddress
_LanIfDefaultGateway_Object = MibTableColumn
lanIfDefaultGateway = _LanIfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 1, 1, 1, 4),
    _LanIfDefaultGateway_Type()
)
lanIfDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIfDefaultGateway.setStatus("mandatory")
_LanIfMacAddress_Type = MacAddress
_LanIfMacAddress_Object = MibTableColumn
lanIfMacAddress = _LanIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 1, 1, 1, 5),
    _LanIfMacAddress_Type()
)
lanIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanIfMacAddress.setStatus("mandatory")
_Wirelesslan_ObjectIdentity = ObjectIdentity
wirelesslan = _Wirelesslan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3)
)
_WirelessLanIfNumber_Type = Integer32
_WirelessLanIfNumber_Object = MibScalar
wirelessLanIfNumber = _WirelessLanIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 1),
    _WirelessLanIfNumber_Type()
)
wirelessLanIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLanIfNumber.setStatus("mandatory")
_Ieee802dot11_ObjectIdentity = ObjectIdentity
ieee802dot11 = _Ieee802dot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3)
)
_Dot11Parameters_ObjectIdentity = ObjectIdentity
dot11Parameters = _Dot11Parameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1)
)
_Dot11ParametersTable_Object = MibTable
dot11ParametersTable = _Dot11ParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dot11ParametersTable.setStatus("mandatory")
_Dot11ParametersEntry_Object = MibTableRow
dot11ParametersEntry = _Dot11ParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1)
)
dot11ParametersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11ParametersEntry.setStatus("mandatory")
_Dot11Ssid_Type = OctetString
_Dot11Ssid_Object = MibTableColumn
dot11Ssid = _Dot11Ssid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 2),
    _Dot11Ssid_Type()
)
dot11Ssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Ssid.setStatus("mandatory")


class _Dot11SsidBroadcast_Type(Integer32):
    """Custom type dot11SsidBroadcast based on Integer32"""
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


_Dot11SsidBroadcast_Type.__name__ = "Integer32"
_Dot11SsidBroadcast_Object = MibTableColumn
dot11SsidBroadcast = _Dot11SsidBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 3),
    _Dot11SsidBroadcast_Type()
)
dot11SsidBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SsidBroadcast.setStatus("mandatory")
_Dot11Channel_Type = Integer32
_Dot11Channel_Object = MibTableColumn
dot11Channel = _Dot11Channel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 4),
    _Dot11Channel_Type()
)
dot11Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Channel.setStatus("mandatory")
_Dot11ChannelList_Type = OctetString
_Dot11ChannelList_Object = MibTableColumn
dot11ChannelList = _Dot11ChannelList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 5),
    _Dot11ChannelList_Type()
)
dot11ChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ChannelList.setStatus("mandatory")
_Dot11DynamicChannelList_Type = OctetString
_Dot11DynamicChannelList_Object = MibTableColumn
dot11DynamicChannelList = _Dot11DynamicChannelList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 6),
    _Dot11DynamicChannelList_Type()
)
dot11DynamicChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DynamicChannelList.setStatus("mandatory")
_Dot11WdsChannelList_Type = OctetString
_Dot11WdsChannelList_Object = MibTableColumn
dot11WdsChannelList = _Dot11WdsChannelList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 8),
    _Dot11WdsChannelList_Type()
)
dot11WdsChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsChannelList.setStatus("mandatory")
_Dot11WdsDynamicChannelList_Type = OctetString
_Dot11WdsDynamicChannelList_Object = MibTableColumn
dot11WdsDynamicChannelList = _Dot11WdsDynamicChannelList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 9),
    _Dot11WdsDynamicChannelList_Type()
)
dot11WdsDynamicChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsDynamicChannelList.setStatus("mandatory")
_Dot11Frequency_Type = OctetString
_Dot11Frequency_Object = MibTableColumn
dot11Frequency = _Dot11Frequency_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 11),
    _Dot11Frequency_Type()
)
dot11Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11Frequency.setStatus("mandatory")
_Dot11DataRate_Type = OctetString
_Dot11DataRate_Object = MibTableColumn
dot11DataRate = _Dot11DataRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 12),
    _Dot11DataRate_Type()
)
dot11DataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate.setStatus("mandatory")
_Dot11bModeDataRateList_Type = OctetString
_Dot11bModeDataRateList_Object = MibTableColumn
dot11bModeDataRateList = _Dot11bModeDataRateList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 14),
    _Dot11bModeDataRateList_Type()
)
dot11bModeDataRateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11bModeDataRateList.setStatus("mandatory")
_Dot11gModeDataRateList_Type = OctetString
_Dot11gModeDataRateList_Object = MibTableColumn
dot11gModeDataRateList = _Dot11gModeDataRateList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 15),
    _Dot11gModeDataRateList_Type()
)
dot11gModeDataRateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11gModeDataRateList.setStatus("mandatory")


class _Dot11WifiMode_Type(Integer32):
    """Custom type dot11WifiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dot11b", 2),
          ("dot11b-dot11g", 6),
          ("dot11g", 4))
    )


_Dot11WifiMode_Type.__name__ = "Integer32"
_Dot11WifiMode_Object = MibTableColumn
dot11WifiMode = _Dot11WifiMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 17),
    _Dot11WifiMode_Type()
)
dot11WifiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WifiMode.setStatus("mandatory")


class _Dot11BeaconInterval_Type(Integer32):
    """Custom type dot11BeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_Dot11BeaconInterval_Type.__name__ = "Integer32"
_Dot11BeaconInterval_Object = MibTableColumn
dot11BeaconInterval = _Dot11BeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 18),
    _Dot11BeaconInterval_Type()
)
dot11BeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11BeaconInterval.setStatus("mandatory")


class _Dot11Dtim_Type(Integer32):
    """Custom type dot11Dtim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11Dtim_Type.__name__ = "Integer32"
_Dot11Dtim_Object = MibTableColumn
dot11Dtim = _Dot11Dtim_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 19),
    _Dot11Dtim_Type()
)
dot11Dtim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Dtim.setStatus("mandatory")


class _Dot11FragmentLength_Type(Integer32):
    """Custom type dot11FragmentLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_Dot11FragmentLength_Type.__name__ = "Integer32"
_Dot11FragmentLength_Object = MibTableColumn
dot11FragmentLength = _Dot11FragmentLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 20),
    _Dot11FragmentLength_Type()
)
dot11FragmentLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FragmentLength.setStatus("mandatory")


class _Dot11RtsLength_Type(Integer32):
    """Custom type dot11RtsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_Dot11RtsLength_Type.__name__ = "Integer32"
_Dot11RtsLength_Object = MibTableColumn
dot11RtsLength = _Dot11RtsLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 21),
    _Dot11RtsLength_Type()
)
dot11RtsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RtsLength.setStatus("mandatory")


class _Dot11TransmitPower_Type(Integer32):
    """Custom type dot11TransmitPower based on Integer32"""
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
        *(("eighth", 4),
          ("full", 1),
          ("half", 2),
          ("min", 5),
          ("quarter", 3))
    )


_Dot11TransmitPower_Type.__name__ = "Integer32"
_Dot11TransmitPower_Object = MibTableColumn
dot11TransmitPower = _Dot11TransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 22),
    _Dot11TransmitPower_Type()
)
dot11TransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11TransmitPower.setStatus("mandatory")


class _Dot11SuperMode_Type(Integer32):
    """Custom type dot11SuperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("dynamic", 3),
          ("super", 1))
    )


_Dot11SuperMode_Type.__name__ = "Integer32"
_Dot11SuperMode_Object = MibTableColumn
dot11SuperMode = _Dot11SuperMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 23),
    _Dot11SuperMode_Type()
)
dot11SuperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SuperMode.setStatus("mandatory")


class _Dot11RadioWave_Type(Integer32):
    """Custom type dot11RadioWave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Dot11RadioWave_Type.__name__ = "Integer32"
_Dot11RadioWave_Object = MibTableColumn
dot11RadioWave = _Dot11RadioWave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 24),
    _Dot11RadioWave_Type()
)
dot11RadioWave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RadioWave.setStatus("mandatory")


class _Dot11AutoChannelScan_Type(Integer32):
    """Custom type dot11AutoChannelScan based on Integer32"""
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


_Dot11AutoChannelScan_Type.__name__ = "Integer32"
_Dot11AutoChannelScan_Object = MibTableColumn
dot11AutoChannelScan = _Dot11AutoChannelScan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 25),
    _Dot11AutoChannelScan_Type()
)
dot11AutoChannelScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AutoChannelScan.setStatus("mandatory")


class _Dot11Wmm_Type(Integer32):
    """Custom type dot11Wmm based on Integer32"""
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


_Dot11Wmm_Type.__name__ = "Integer32"
_Dot11Wmm_Object = MibTableColumn
dot11Wmm = _Dot11Wmm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 26),
    _Dot11Wmm_Type()
)
dot11Wmm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Wmm.setStatus("mandatory")


class _Dot11Preamble_Type(Integer32):
    """Custom type dot11Preamble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("longAndShort", 1),
          ("longOnly", 0))
    )


_Dot11Preamble_Type.__name__ = "Integer32"
_Dot11Preamble_Object = MibTableColumn
dot11Preamble = _Dot11Preamble_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 27),
    _Dot11Preamble_Type()
)
dot11Preamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Preamble.setStatus("mandatory")


class _Dot11Antenna_Type(Integer32):
    """Custom type dot11Antenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ant1", 1),
          ("ant2", 2),
          ("auto", 0))
    )


_Dot11Antenna_Type.__name__ = "Integer32"
_Dot11Antenna_Object = MibTableColumn
dot11Antenna = _Dot11Antenna_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 28),
    _Dot11Antenna_Type()
)
dot11Antenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Antenna.setStatus("mandatory")


class _Dot11ApMode_Type(Integer32):
    """Custom type dot11ApMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("wdsWithAp", 2),
          ("wdsWithoutAp", 3))
    )


_Dot11ApMode_Type.__name__ = "Integer32"
_Dot11ApMode_Object = MibTableColumn
dot11ApMode = _Dot11ApMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 29),
    _Dot11ApMode_Type()
)
dot11ApMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ApMode.setStatus("mandatory")


class _Dot11IgmpSnooping_Type(Integer32):
    """Custom type dot11IgmpSnooping based on Integer32"""
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


_Dot11IgmpSnooping_Type.__name__ = "Integer32"
_Dot11IgmpSnooping_Object = MibTableColumn
dot11IgmpSnooping = _Dot11IgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 1, 1, 34),
    _Dot11IgmpSnooping_Type()
)
dot11IgmpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11IgmpSnooping.setStatus("mandatory")
_Dot11RemoteApMacAddressTable_Object = MibTable
dot11RemoteApMacAddressTable = _Dot11RemoteApMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    dot11RemoteApMacAddressTable.setStatus("mandatory")
_Dot11RemoteApMacAddressEntry_Object = MibTableRow
dot11RemoteApMacAddressEntry = _Dot11RemoteApMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 2, 1)
)
dot11RemoteApMacAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DWL-3200", "dot11RemoteApMacAddressIndex"),
)
if mibBuilder.loadTexts:
    dot11RemoteApMacAddressEntry.setStatus("mandatory")


class _Dot11RemoteApMacAddressIndex_Type(Integer32):
    """Custom type dot11RemoteApMacAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dot11RemoteApMacAddressIndex_Type.__name__ = "Integer32"
_Dot11RemoteApMacAddressIndex_Object = MibTableColumn
dot11RemoteApMacAddressIndex = _Dot11RemoteApMacAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 2, 1, 1),
    _Dot11RemoteApMacAddressIndex_Type()
)
dot11RemoteApMacAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11RemoteApMacAddressIndex.setStatus("mandatory")
_Dot11RemoteApMacAddress_Type = MacAddress
_Dot11RemoteApMacAddress_Object = MibTableColumn
dot11RemoteApMacAddress = _Dot11RemoteApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 2, 1, 2),
    _Dot11RemoteApMacAddress_Type()
)
dot11RemoteApMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RemoteApMacAddress.setStatus("mandatory")
_Dot11SiteSurvey_ObjectIdentity = ObjectIdentity
dot11SiteSurvey = _Dot11SiteSurvey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3)
)
_Dot11SiteSurveyRefreshTable_Object = MibTable
dot11SiteSurveyRefreshTable = _Dot11SiteSurveyRefreshTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot11SiteSurveyRefreshTable.setStatus("mandatory")
_Dot11SiteSurveyRefreshEntry_Object = MibTableRow
dot11SiteSurveyRefreshEntry = _Dot11SiteSurveyRefreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 1, 1)
)
dot11SiteSurveyRefreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11SiteSurveyRefreshEntry.setStatus("mandatory")


class _Dot11SiteSurveyRefresh_Type(Integer32):
    """Custom type dot11SiteSurveyRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("refresh", 1))
    )


_Dot11SiteSurveyRefresh_Type.__name__ = "Integer32"
_Dot11SiteSurveyRefresh_Object = MibTableColumn
dot11SiteSurveyRefresh = _Dot11SiteSurveyRefresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 1, 1, 2),
    _Dot11SiteSurveyRefresh_Type()
)
dot11SiteSurveyRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SiteSurveyRefresh.setStatus("mandatory")
_Dot11SiteSurveyTable_Object = MibTable
dot11SiteSurveyTable = _Dot11SiteSurveyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dot11SiteSurveyTable.setStatus("mandatory")
_Dot11SiteSurveyEntry_Object = MibTableRow
dot11SiteSurveyEntry = _Dot11SiteSurveyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 2, 1)
)
dot11SiteSurveyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DWL-3200", "dot11SiteSurveyIndex"),
)
if mibBuilder.loadTexts:
    dot11SiteSurveyEntry.setStatus("mandatory")
_Dot11SiteSurveyIndex_Type = Integer32
_Dot11SiteSurveyIndex_Object = MibTableColumn
dot11SiteSurveyIndex = _Dot11SiteSurveyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 2, 1, 2),
    _Dot11SiteSurveyIndex_Type()
)
dot11SiteSurveyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11SiteSurveyIndex.setStatus("mandatory")
_Dot11SiteSurveyBssType_Type = OctetString
_Dot11SiteSurveyBssType_Object = MibTableColumn
dot11SiteSurveyBssType = _Dot11SiteSurveyBssType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 2, 1, 3),
    _Dot11SiteSurveyBssType_Type()
)
dot11SiteSurveyBssType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveyBssType.setStatus("mandatory")
_Dot11SiteSurveyChannel_Type = Integer32
_Dot11SiteSurveyChannel_Object = MibTableColumn
dot11SiteSurveyChannel = _Dot11SiteSurveyChannel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 2, 1, 4),
    _Dot11SiteSurveyChannel_Type()
)
dot11SiteSurveyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveyChannel.setStatus("mandatory")
_Dot11SiteSurveyRssi_Type = Integer32
_Dot11SiteSurveyRssi_Object = MibTableColumn
dot11SiteSurveyRssi = _Dot11SiteSurveyRssi_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 2, 1, 5),
    _Dot11SiteSurveyRssi_Type()
)
dot11SiteSurveyRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveyRssi.setStatus("mandatory")
_Dot11SiteSurveyBssid_Type = MacAddress
_Dot11SiteSurveyBssid_Object = MibTableColumn
dot11SiteSurveyBssid = _Dot11SiteSurveyBssid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 2, 1, 6),
    _Dot11SiteSurveyBssid_Type()
)
dot11SiteSurveyBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveyBssid.setStatus("mandatory")
_Dot11SiteSurveyEncryption_Type = OctetString
_Dot11SiteSurveyEncryption_Object = MibTableColumn
dot11SiteSurveyEncryption = _Dot11SiteSurveyEncryption_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 2, 1, 7),
    _Dot11SiteSurveyEncryption_Type()
)
dot11SiteSurveyEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveyEncryption.setStatus("mandatory")


class _Dot11SiteSurveySsid_Type(OctetString):
    """Custom type dot11SiteSurveySsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11SiteSurveySsid_Type.__name__ = "OctetString"
_Dot11SiteSurveySsid_Object = MibTableColumn
dot11SiteSurveySsid = _Dot11SiteSurveySsid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 2, 1, 8),
    _Dot11SiteSurveySsid_Type()
)
dot11SiteSurveySsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveySsid.setStatus("mandatory")


class _Dot11SiteSurveyWirelessMode_Type(Integer32):
    """Custom type dot11SiteSurveyWirelessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11b", 2),
          ("dot11g", 3))
    )


_Dot11SiteSurveyWirelessMode_Type.__name__ = "Integer32"
_Dot11SiteSurveyWirelessMode_Object = MibTableColumn
dot11SiteSurveyWirelessMode = _Dot11SiteSurveyWirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 2, 1, 9),
    _Dot11SiteSurveyWirelessMode_Type()
)
dot11SiteSurveyWirelessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveyWirelessMode.setStatus("mandatory")
_Dot11SiteSurveySupportWds_Type = Integer32
_Dot11SiteSurveySupportWds_Object = MibTableColumn
dot11SiteSurveySupportWds = _Dot11SiteSurveySupportWds_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 1, 3, 2, 1, 10),
    _Dot11SiteSurveySupportWds_Type()
)
dot11SiteSurveySupportWds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveySupportWds.setStatus("mandatory")
_Dot11Securities_ObjectIdentity = ObjectIdentity
dot11Securities = _Dot11Securities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2)
)
_Dot11SecuritiesTable_Object = MibTable
dot11SecuritiesTable = _Dot11SecuritiesTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dot11SecuritiesTable.setStatus("mandatory")
_Dot11SecuritiesEntry_Object = MibTableRow
dot11SecuritiesEntry = _Dot11SecuritiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1)
)
dot11SecuritiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11SecuritiesEntry.setStatus("mandatory")


class _Dot11Authentication_Type(Integer32):
    """Custom type dot11Authentication based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 1),
          ("opensystem-sharedkey", 3),
          ("sharedkey", 2),
          ("wpa-auto-eap", 9),
          ("wpa-auto-psk", 8),
          ("wpa-eap", 5),
          ("wpa-psk", 4),
          ("wpa2-eap", 7),
          ("wpa2-psk", 6))
    )


_Dot11Authentication_Type.__name__ = "Integer32"
_Dot11Authentication_Object = MibTableColumn
dot11Authentication = _Dot11Authentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 2),
    _Dot11Authentication_Type()
)
dot11Authentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Authentication.setStatus("mandatory")


class _Dot11Encryption_Type(Integer32):
    """Custom type dot11Encryption based on Integer32"""
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


_Dot11Encryption_Type.__name__ = "Integer32"
_Dot11Encryption_Object = MibTableColumn
dot11Encryption = _Dot11Encryption_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 3),
    _Dot11Encryption_Type()
)
dot11Encryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Encryption.setStatus("mandatory")


class _Dot11KeyIndex_Type(Integer32):
    """Custom type dot11KeyIndex based on Integer32"""
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
        *(("first", 1),
          ("fourth", 4),
          ("second", 2),
          ("third", 3))
    )


_Dot11KeyIndex_Type.__name__ = "Integer32"
_Dot11KeyIndex_Object = MibTableColumn
dot11KeyIndex = _Dot11KeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 4),
    _Dot11KeyIndex_Type()
)
dot11KeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11KeyIndex.setStatus("mandatory")


class _Dot11PassPhrase_Type(OctetString):
    """Custom type dot11PassPhrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_Dot11PassPhrase_Type.__name__ = "OctetString"
_Dot11PassPhrase_Object = MibTableColumn
dot11PassPhrase = _Dot11PassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 5),
    _Dot11PassPhrase_Type()
)
dot11PassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PassPhrase.setStatus("mandatory")


class _Dot11CipherType_Type(Integer32):
    """Custom type dot11CipherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("auto", 1),
          ("tkip", 3))
    )


_Dot11CipherType_Type.__name__ = "Integer32"
_Dot11CipherType_Object = MibTableColumn
dot11CipherType = _Dot11CipherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 6),
    _Dot11CipherType_Type()
)
dot11CipherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CipherType.setStatus("mandatory")


class _Dot11GroupKeyUpdateInterval_Type(Integer32):
    """Custom type dot11GroupKeyUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 9999999),
    )


_Dot11GroupKeyUpdateInterval_Type.__name__ = "Integer32"
_Dot11GroupKeyUpdateInterval_Object = MibTableColumn
dot11GroupKeyUpdateInterval = _Dot11GroupKeyUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 7),
    _Dot11GroupKeyUpdateInterval_Type()
)
dot11GroupKeyUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupKeyUpdateInterval.setStatus("mandatory")


class _Dot11KeyEntryMethod_Type(Integer32):
    """Custom type dot11KeyEntryMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2))
    )


_Dot11KeyEntryMethod_Type.__name__ = "Integer32"
_Dot11KeyEntryMethod_Object = MibTableColumn
dot11KeyEntryMethod = _Dot11KeyEntryMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 8),
    _Dot11KeyEntryMethod_Type()
)
dot11KeyEntryMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11KeyEntryMethod.setStatus("mandatory")


class _Dot11RadiusServer_Type(OctetString):
    """Custom type dot11RadiusServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11RadiusServer_Type.__name__ = "OctetString"
_Dot11RadiusServer_Object = MibTableColumn
dot11RadiusServer = _Dot11RadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 9),
    _Dot11RadiusServer_Type()
)
dot11RadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RadiusServer.setStatus("mandatory")


class _Dot11RadiusPort_Type(Integer32):
    """Custom type dot11RadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11RadiusPort_Type.__name__ = "Integer32"
_Dot11RadiusPort_Object = MibTableColumn
dot11RadiusPort = _Dot11RadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 10),
    _Dot11RadiusPort_Type()
)
dot11RadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RadiusPort.setStatus("mandatory")


class _Dot11RadiusSecret_Type(OctetString):
    """Custom type dot11RadiusSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Dot11RadiusSecret_Type.__name__ = "OctetString"
_Dot11RadiusSecret_Object = MibTableColumn
dot11RadiusSecret = _Dot11RadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 11),
    _Dot11RadiusSecret_Type()
)
dot11RadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RadiusSecret.setStatus("mandatory")


class _Dot11SecRADIUSServer_Type(OctetString):
    """Custom type dot11SecRADIUSServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11SecRADIUSServer_Type.__name__ = "OctetString"
_Dot11SecRADIUSServer_Object = MibTableColumn
dot11SecRADIUSServer = _Dot11SecRADIUSServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 15),
    _Dot11SecRADIUSServer_Type()
)
dot11SecRADIUSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SecRADIUSServer.setStatus("mandatory")


class _Dot11SecRADIUSPort_Type(Integer32):
    """Custom type dot11SecRADIUSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11SecRADIUSPort_Type.__name__ = "Integer32"
_Dot11SecRADIUSPort_Object = MibTableColumn
dot11SecRADIUSPort = _Dot11SecRADIUSPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 16),
    _Dot11SecRADIUSPort_Type()
)
dot11SecRADIUSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SecRADIUSPort.setStatus("mandatory")


class _Dot11SecRADIUSSecret_Type(OctetString):
    """Custom type dot11SecRADIUSSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Dot11SecRADIUSSecret_Type.__name__ = "OctetString"
_Dot11SecRADIUSSecret_Object = MibTableColumn
dot11SecRADIUSSecret = _Dot11SecRADIUSSecret_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 17),
    _Dot11SecRADIUSSecret_Type()
)
dot11SecRADIUSSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SecRADIUSSecret.setStatus("mandatory")


class _Dot11SecRADIUSStatus_Type(Integer32):
    """Custom type dot11SecRADIUSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Dot11SecRADIUSStatus_Type.__name__ = "Integer32"
_Dot11SecRADIUSStatus_Object = MibTableColumn
dot11SecRADIUSStatus = _Dot11SecRADIUSStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 1, 1, 18),
    _Dot11SecRADIUSStatus_Type()
)
dot11SecRADIUSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SecRADIUSStatus.setStatus("mandatory")
_Dot11WepKeyTable_Object = MibTable
dot11WepKeyTable = _Dot11WepKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    dot11WepKeyTable.setStatus("mandatory")
_Dot11WepKeyEntry_Object = MibTableRow
dot11WepKeyEntry = _Dot11WepKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 2, 1)
)
dot11WepKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DWL-3200", "dot11wepKeyIndex"),
)
if mibBuilder.loadTexts:
    dot11WepKeyEntry.setStatus("mandatory")


class _Dot11wepKeyIndex_Type(Integer32):
    """Custom type dot11wepKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dot11wepKeyIndex_Type.__name__ = "Integer32"
_Dot11wepKeyIndex_Object = MibTableColumn
dot11wepKeyIndex = _Dot11wepKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 2, 1, 1),
    _Dot11wepKeyIndex_Type()
)
dot11wepKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11wepKeyIndex.setStatus("mandatory")
_Dot11WepKey_Type = OctetString
_Dot11WepKey_Object = MibTableColumn
dot11WepKey = _Dot11WepKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 2, 1, 2),
    _Dot11WepKey_Type()
)
dot11WepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WepKey.setStatus("mandatory")
_Dot11Filter_ObjectIdentity = ObjectIdentity
dot11Filter = _Dot11Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3)
)
_Dot11PartionTable_Object = MibTable
dot11PartionTable = _Dot11PartionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dot11PartionTable.setStatus("mandatory")
_Dot11LanPartionEntry_Object = MibTableRow
dot11LanPartionEntry = _Dot11LanPartionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3, 1, 1)
)
dot11LanPartionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11LanPartionEntry.setStatus("mandatory")


class _Dot11InternalStationConnection_Type(Integer32):
    """Custom type dot11InternalStationConnection based on Integer32"""
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


_Dot11InternalStationConnection_Type.__name__ = "Integer32"
_Dot11InternalStationConnection_Object = MibTableColumn
dot11InternalStationConnection = _Dot11InternalStationConnection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3, 1, 1, 2),
    _Dot11InternalStationConnection_Type()
)
dot11InternalStationConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11InternalStationConnection.setStatus("mandatory")


class _Dot11EthernetToWlanAccess_Type(Integer32):
    """Custom type dot11EthernetToWlanAccess based on Integer32"""
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


_Dot11EthernetToWlanAccess_Type.__name__ = "Integer32"
_Dot11EthernetToWlanAccess_Object = MibTableColumn
dot11EthernetToWlanAccess = _Dot11EthernetToWlanAccess_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3, 1, 1, 3),
    _Dot11EthernetToWlanAccess_Type()
)
dot11EthernetToWlanAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EthernetToWlanAccess.setStatus("mandatory")
_Dot11MacAccessControlTable_Object = MibTable
dot11MacAccessControlTable = _Dot11MacAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dot11MacAccessControlTable.setStatus("mandatory")
_Dot11MacAccessControlEntry_Object = MibTableRow
dot11MacAccessControlEntry = _Dot11MacAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3, 2, 1)
)
dot11MacAccessControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11MacAccessControlEntry.setStatus("mandatory")


class _Dot11MacAccessControl_Type(Integer32):
    """Custom type dot11MacAccessControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("disabled", 3),
          ("reject", 2))
    )


_Dot11MacAccessControl_Type.__name__ = "Integer32"
_Dot11MacAccessControl_Object = MibTableColumn
dot11MacAccessControl = _Dot11MacAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3, 2, 1, 2),
    _Dot11MacAccessControl_Type()
)
dot11MacAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MacAccessControl.setStatus("mandatory")
_Dot11MacAccessControlListTable_Object = MibTable
dot11MacAccessControlListTable = _Dot11MacAccessControlListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    dot11MacAccessControlListTable.setStatus("mandatory")
_Dot11MacAccessControlListEntry_Object = MibTableRow
dot11MacAccessControlListEntry = _Dot11MacAccessControlListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3, 3, 1)
)
dot11MacAccessControlListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DWL-3200", "dot11MacAccessControlListIndex"),
)
if mibBuilder.loadTexts:
    dot11MacAccessControlListEntry.setStatus("mandatory")


class _Dot11MacAccessControlListIndex_Type(Integer32):
    """Custom type dot11MacAccessControlListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dot11MacAccessControlListIndex_Type.__name__ = "Integer32"
_Dot11MacAccessControlListIndex_Object = MibTableColumn
dot11MacAccessControlListIndex = _Dot11MacAccessControlListIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3, 3, 1, 2),
    _Dot11MacAccessControlListIndex_Type()
)
dot11MacAccessControlListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11MacAccessControlListIndex.setStatus("mandatory")
_Dot11MacAccessControlListMacAddress_Type = MacAddress
_Dot11MacAccessControlListMacAddress_Object = MibTableColumn
dot11MacAccessControlListMacAddress = _Dot11MacAccessControlListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 2, 3, 3, 1, 3),
    _Dot11MacAccessControlListMacAddress_Type()
)
dot11MacAccessControlListMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MacAccessControlListMacAddress.setStatus("mandatory")
_Dot11Accounting_ObjectIdentity = ObjectIdentity
dot11Accounting = _Dot11Accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 3)
)
_Dot11AccountingTable_Object = MibTable
dot11AccountingTable = _Dot11AccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    dot11AccountingTable.setStatus("mandatory")
_Dot11AccountingEntry_Object = MibTableRow
dot11AccountingEntry = _Dot11AccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 3, 1, 1)
)
dot11AccountingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11AccountingEntry.setStatus("mandatory")


class _Dot11AccountingStatus_Type(Integer32):
    """Custom type dot11AccountingStatus based on Integer32"""
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


_Dot11AccountingStatus_Type.__name__ = "Integer32"
_Dot11AccountingStatus_Object = MibTableColumn
dot11AccountingStatus = _Dot11AccountingStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 3, 1, 1, 2),
    _Dot11AccountingStatus_Type()
)
dot11AccountingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AccountingStatus.setStatus("mandatory")
_Dot11AccountingServer_Type = IpAddress
_Dot11AccountingServer_Object = MibTableColumn
dot11AccountingServer = _Dot11AccountingServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 3, 1, 1, 3),
    _Dot11AccountingServer_Type()
)
dot11AccountingServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AccountingServer.setStatus("mandatory")
_Dot11AccountingServerPort_Type = Integer32
_Dot11AccountingServerPort_Object = MibTableColumn
dot11AccountingServerPort = _Dot11AccountingServerPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 3, 1, 1, 4),
    _Dot11AccountingServerPort_Type()
)
dot11AccountingServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AccountingServerPort.setStatus("mandatory")
_Dot11SecAccountingTable_Object = MibTable
dot11SecAccountingTable = _Dot11SecAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    dot11SecAccountingTable.setStatus("mandatory")
_Dot11SecAccountingEntry_Object = MibTableRow
dot11SecAccountingEntry = _Dot11SecAccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 3, 2, 1)
)
dot11SecAccountingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11SecAccountingEntry.setStatus("mandatory")


class _Dot11SecAccountingStatus_Type(Integer32):
    """Custom type dot11SecAccountingStatus based on Integer32"""
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


_Dot11SecAccountingStatus_Type.__name__ = "Integer32"
_Dot11SecAccountingStatus_Object = MibTableColumn
dot11SecAccountingStatus = _Dot11SecAccountingStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 3, 2, 1, 2),
    _Dot11SecAccountingStatus_Type()
)
dot11SecAccountingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SecAccountingStatus.setStatus("mandatory")
_Dot11SecAccountingServer_Type = IpAddress
_Dot11SecAccountingServer_Object = MibTableColumn
dot11SecAccountingServer = _Dot11SecAccountingServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 3, 2, 1, 3),
    _Dot11SecAccountingServer_Type()
)
dot11SecAccountingServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SecAccountingServer.setStatus("mandatory")
_Dot11SecAccountingServerPort_Type = Integer32
_Dot11SecAccountingServerPort_Object = MibTableColumn
dot11SecAccountingServerPort = _Dot11SecAccountingServerPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 3, 2, 1, 4),
    _Dot11SecAccountingServerPort_Type()
)
dot11SecAccountingServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SecAccountingServerPort.setStatus("mandatory")
_Dot11ClientInformation_ObjectIdentity = ObjectIdentity
dot11ClientInformation = _Dot11ClientInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4)
)
_Dot11GetClientInformationTable_Object = MibTable
dot11GetClientInformationTable = _Dot11GetClientInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    dot11GetClientInformationTable.setStatus("mandatory")
_Dot11GetClientInformationEntry_Object = MibTableRow
dot11GetClientInformationEntry = _Dot11GetClientInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 1, 1)
)
dot11GetClientInformationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11GetClientInformationEntry.setStatus("mandatory")


class _Dot11ClientInformationRefresh_Type(Integer32):
    """Custom type dot11ClientInformationRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("nothing", 0))
    )


_Dot11ClientInformationRefresh_Type.__name__ = "Integer32"
_Dot11ClientInformationRefresh_Object = MibTableColumn
dot11ClientInformationRefresh = _Dot11ClientInformationRefresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 1, 1, 2),
    _Dot11ClientInformationRefresh_Type()
)
dot11ClientInformationRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ClientInformationRefresh.setStatus("mandatory")
_Dot11ClientInformationAssNum_Type = Integer32
_Dot11ClientInformationAssNum_Object = MibTableColumn
dot11ClientInformationAssNum = _Dot11ClientInformationAssNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 1, 1, 3),
    _Dot11ClientInformationAssNum_Type()
)
dot11ClientInformationAssNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientInformationAssNum.setStatus("mandatory")
_Dot11ClientInformationTable_Object = MibTable
dot11ClientInformationTable = _Dot11ClientInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    dot11ClientInformationTable.setStatus("mandatory")
_Dot11ClientInformationEntry_Object = MibTableRow
dot11ClientInformationEntry = _Dot11ClientInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 2, 1)
)
dot11ClientInformationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DWL-3200", "dot11ClinetIndex"),
)
if mibBuilder.loadTexts:
    dot11ClientInformationEntry.setStatus("mandatory")
_Dot11ClinetIndex_Type = Integer32
_Dot11ClinetIndex_Object = MibTableColumn
dot11ClinetIndex = _Dot11ClinetIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 2, 1, 2),
    _Dot11ClinetIndex_Type()
)
dot11ClinetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11ClinetIndex.setStatus("mandatory")
_Dot11ClientMacAddress_Type = MacAddress
_Dot11ClientMacAddress_Object = MibTableColumn
dot11ClientMacAddress = _Dot11ClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 2, 1, 3),
    _Dot11ClientMacAddress_Type()
)
dot11ClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientMacAddress.setStatus("mandatory")


class _Dot11ClientBand_Type(Integer32):
    """Custom type dot11ClientBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot11b", 1),
          ("dot11g", 2))
    )


_Dot11ClientBand_Type.__name__ = "Integer32"
_Dot11ClientBand_Object = MibTableColumn
dot11ClientBand = _Dot11ClientBand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 2, 1, 4),
    _Dot11ClientBand_Type()
)
dot11ClientBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientBand.setStatus("mandatory")


class _Dot11ClientAuthentication_Type(Integer32):
    """Custom type dot11ClientAuthentication based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 1),
          ("opensystem-sharedkey", 3),
          ("sharedkey", 2),
          ("wpa-auto-eap", 9),
          ("wpa-auto-psk", 8),
          ("wpa-eap", 5),
          ("wpa-psk", 4),
          ("wpa2-eap", 7),
          ("wpa2-psk", 6))
    )


_Dot11ClientAuthentication_Type.__name__ = "Integer32"
_Dot11ClientAuthentication_Object = MibTableColumn
dot11ClientAuthentication = _Dot11ClientAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 2, 1, 5),
    _Dot11ClientAuthentication_Type()
)
dot11ClientAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientAuthentication.setStatus("mandatory")
_Dot11ClientRssi_Type = Integer32
_Dot11ClientRssi_Object = MibTableColumn
dot11ClientRssi = _Dot11ClientRssi_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 2, 1, 6),
    _Dot11ClientRssi_Type()
)
dot11ClientRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientRssi.setStatus("mandatory")
_Dot11ClientPsm_Type = Integer32
_Dot11ClientPsm_Object = MibTableColumn
dot11ClientPsm = _Dot11ClientPsm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 2, 1, 7),
    _Dot11ClientPsm_Type()
)
dot11ClientPsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientPsm.setStatus("mandatory")
_Dot11SSIDIndex_Type = OctetString
_Dot11SSIDIndex_Object = MibTableColumn
dot11SSIDIndex = _Dot11SSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 2, 1, 8),
    _Dot11SSIDIndex_Type()
)
dot11SSIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SSIDIndex.setStatus("mandatory")
_Dot11ClientKickOff_ObjectIdentity = ObjectIdentity
dot11ClientKickOff = _Dot11ClientKickOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 3)
)
_Dot11KickOffClientMacAddress_Type = MacAddress
_Dot11KickOffClientMacAddress_Object = MibScalar
dot11KickOffClientMacAddress = _Dot11KickOffClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 3, 1),
    _Dot11KickOffClientMacAddress_Type()
)
dot11KickOffClientMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11KickOffClientMacAddress.setStatus("mandatory")
_Dot11KickOff_Type = Integer32
_Dot11KickOff_Object = MibScalar
dot11KickOff = _Dot11KickOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 2, 1, 3, 3, 4, 3, 2),
    _Dot11KickOff_Type()
)
dot11KickOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11KickOff.setStatus("mandatory")
_Advance_ObjectIdentity = ObjectIdentity
advance = _Advance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3)
)
_DhcpServer_ObjectIdentity = ObjectIdentity
dhcpServer = _DhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1)
)


class _DhcpServerControl_Type(Integer32):
    """Custom type dhcpServerControl based on Integer32"""
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


_DhcpServerControl_Type.__name__ = "Integer32"
_DhcpServerControl_Object = MibScalar
dhcpServerControl = _DhcpServerControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 1),
    _DhcpServerControl_Type()
)
dhcpServerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerControl.setStatus("mandatory")
_DhcpServerDynamicTable_ObjectIdentity = ObjectIdentity
dhcpServerDynamicTable = _DhcpServerDynamicTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 2)
)
_DynamicIpPoolStart_Type = IpAddress
_DynamicIpPoolStart_Object = MibScalar
dynamicIpPoolStart = _DynamicIpPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 2, 1),
    _DynamicIpPoolStart_Type()
)
dynamicIpPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicIpPoolStart.setStatus("mandatory")


class _DynamicIpPoolRange_Type(Integer32):
    """Custom type dynamicIpPoolRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DynamicIpPoolRange_Type.__name__ = "Integer32"
_DynamicIpPoolRange_Object = MibScalar
dynamicIpPoolRange = _DynamicIpPoolRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 2, 2),
    _DynamicIpPoolRange_Type()
)
dynamicIpPoolRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicIpPoolRange.setStatus("mandatory")
_DynamicMask_Type = IpAddress
_DynamicMask_Object = MibScalar
dynamicMask = _DynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 2, 3),
    _DynamicMask_Type()
)
dynamicMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicMask.setStatus("mandatory")
_DynamicGateway_Type = IpAddress
_DynamicGateway_Object = MibScalar
dynamicGateway = _DynamicGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 2, 4),
    _DynamicGateway_Type()
)
dynamicGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicGateway.setStatus("mandatory")
_DynamicWins_Type = IpAddress
_DynamicWins_Object = MibScalar
dynamicWins = _DynamicWins_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 2, 5),
    _DynamicWins_Type()
)
dynamicWins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicWins.setStatus("mandatory")
_DynamicDns_Type = IpAddress
_DynamicDns_Object = MibScalar
dynamicDns = _DynamicDns_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 2, 6),
    _DynamicDns_Type()
)
dynamicDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicDns.setStatus("mandatory")


class _DynamicDomainName_Type(OctetString):
    """Custom type dynamicDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DynamicDomainName_Type.__name__ = "OctetString"
_DynamicDomainName_Object = MibScalar
dynamicDomainName = _DynamicDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 2, 7),
    _DynamicDomainName_Type()
)
dynamicDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicDomainName.setStatus("mandatory")


class _DynamicLeaseTime_Type(Integer32):
    """Custom type dynamicLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 31536000),
    )


_DynamicLeaseTime_Type.__name__ = "Integer32"
_DynamicLeaseTime_Object = MibScalar
dynamicLeaseTime = _DynamicLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 2, 8),
    _DynamicLeaseTime_Type()
)
dynamicLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicLeaseTime.setStatus("mandatory")


class _DynamicFunction_Type(Integer32):
    """Custom type dynamicFunction based on Integer32"""
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


_DynamicFunction_Type.__name__ = "Integer32"
_DynamicFunction_Object = MibScalar
dynamicFunction = _DynamicFunction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 2, 9),
    _DynamicFunction_Type()
)
dynamicFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicFunction.setStatus("mandatory")
_DhcpServerStaticTable_Object = MibTable
dhcpServerStaticTable = _DhcpServerStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 3)
)
if mibBuilder.loadTexts:
    dhcpServerStaticTable.setStatus("mandatory")
_DhcpServerStaticEntry_Object = MibTableRow
dhcpServerStaticEntry = _DhcpServerStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 3, 1)
)
dhcpServerStaticEntry.setIndexNames(
    (0, "DWL-3200", "staticIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerStaticEntry.setStatus("mandatory")
_StaticIndex_Type = Integer32
_StaticIndex_Object = MibTableColumn
staticIndex = _StaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 3, 1, 1),
    _StaticIndex_Type()
)
staticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticIndex.setStatus("mandatory")
_StaticIP_Type = IpAddress
_StaticIP_Object = MibTableColumn
staticIP = _StaticIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 3, 1, 2),
    _StaticIP_Type()
)
staticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIP.setStatus("mandatory")
_StaticMac_Type = MacAddress
_StaticMac_Object = MibTableColumn
staticMac = _StaticMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 3, 1, 3),
    _StaticMac_Type()
)
staticMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMac.setStatus("mandatory")
_StaticMask_Type = IpAddress
_StaticMask_Object = MibTableColumn
staticMask = _StaticMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 3, 1, 4),
    _StaticMask_Type()
)
staticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMask.setStatus("mandatory")
_StaticGateway_Type = IpAddress
_StaticGateway_Object = MibTableColumn
staticGateway = _StaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 3, 1, 5),
    _StaticGateway_Type()
)
staticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticGateway.setStatus("mandatory")
_StaticDns_Type = IpAddress
_StaticDns_Object = MibTableColumn
staticDns = _StaticDns_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 3, 1, 6),
    _StaticDns_Type()
)
staticDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDns.setStatus("mandatory")
_StaticWins_Type = IpAddress
_StaticWins_Object = MibTableColumn
staticWins = _StaticWins_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 3, 1, 7),
    _StaticWins_Type()
)
staticWins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticWins.setStatus("mandatory")


class _StaticDomainName_Type(OctetString):
    """Custom type staticDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StaticDomainName_Type.__name__ = "OctetString"
_StaticDomainName_Object = MibTableColumn
staticDomainName = _StaticDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 3, 1, 8),
    _StaticDomainName_Type()
)
staticDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDomainName.setStatus("mandatory")


class _StaticStatus_Type(Integer32):
    """Custom type staticStatus based on Integer32"""
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


_StaticStatus_Type.__name__ = "Integer32"
_StaticStatus_Object = MibTableColumn
staticStatus = _StaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 3, 1, 9),
    _StaticStatus_Type()
)
staticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticStatus.setStatus("mandatory")
_DhcpServerCurrentListTable_ObjectIdentity = ObjectIdentity
dhcpServerCurrentListTable = _DhcpServerCurrentListTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4)
)
_CurrentDynamicTable_Object = MibTable
currentDynamicTable = _CurrentDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    currentDynamicTable.setStatus("mandatory")
_CurrentDynamicEntry_Object = MibTableRow
currentDynamicEntry = _CurrentDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4, 1, 1)
)
currentDynamicEntry.setIndexNames(
    (0, "DWL-3200", "currentDynamicIndex"),
)
if mibBuilder.loadTexts:
    currentDynamicEntry.setStatus("mandatory")
_CurrentDynamicIndex_Type = Integer32
_CurrentDynamicIndex_Object = MibTableColumn
currentDynamicIndex = _CurrentDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4, 1, 1, 1),
    _CurrentDynamicIndex_Type()
)
currentDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentDynamicIndex.setStatus("mandatory")
_CurrentDynamicMacAddress_Type = MacAddress
_CurrentDynamicMacAddress_Object = MibTableColumn
currentDynamicMacAddress = _CurrentDynamicMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4, 1, 1, 2),
    _CurrentDynamicMacAddress_Type()
)
currentDynamicMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDynamicMacAddress.setStatus("mandatory")
_CurrentDynamicAssignedIP_Type = IpAddress
_CurrentDynamicAssignedIP_Object = MibTableColumn
currentDynamicAssignedIP = _CurrentDynamicAssignedIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4, 1, 1, 3),
    _CurrentDynamicAssignedIP_Type()
)
currentDynamicAssignedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDynamicAssignedIP.setStatus("mandatory")
_CurrentDynamicLease_Type = Integer32
_CurrentDynamicLease_Object = MibTableColumn
currentDynamicLease = _CurrentDynamicLease_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4, 1, 1, 4),
    _CurrentDynamicLease_Type()
)
currentDynamicLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDynamicLease.setStatus("mandatory")
_CurrentStaticTable_Object = MibTable
currentStaticTable = _CurrentStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    currentStaticTable.setStatus("mandatory")
_CurrentStaticEntry_Object = MibTableRow
currentStaticEntry = _CurrentStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4, 2, 1)
)
currentStaticEntry.setIndexNames(
    (0, "DWL-3200", "currentStaticIndex"),
)
if mibBuilder.loadTexts:
    currentStaticEntry.setStatus("mandatory")
_CurrentStaticIndex_Type = Integer32
_CurrentStaticIndex_Object = MibTableColumn
currentStaticIndex = _CurrentStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4, 2, 1, 1),
    _CurrentStaticIndex_Type()
)
currentStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentStaticIndex.setStatus("mandatory")
_CurrentStaticMacAddress_Type = MacAddress
_CurrentStaticMacAddress_Object = MibTableColumn
currentStaticMacAddress = _CurrentStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4, 2, 1, 2),
    _CurrentStaticMacAddress_Type()
)
currentStaticMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentStaticMacAddress.setStatus("mandatory")
_CurrentStaticAssignedIP_Type = IpAddress
_CurrentStaticAssignedIP_Object = MibTableColumn
currentStaticAssignedIP = _CurrentStaticAssignedIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 1, 4, 2, 1, 3),
    _CurrentStaticAssignedIP_Type()
)
currentStaticAssignedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentStaticAssignedIP.setStatus("mandatory")
_Ieee802dot11Grouping_ObjectIdentity = ObjectIdentity
ieee802dot11Grouping = _Ieee802dot11Grouping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 2)
)
_Ieee802dot11GroupingTable_Object = MibTable
ieee802dot11GroupingTable = _Ieee802dot11GroupingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ieee802dot11GroupingTable.setStatus("mandatory")
_Ieee802dot11GroupingEntry_Object = MibTableRow
ieee802dot11GroupingEntry = _Ieee802dot11GroupingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 2, 1, 1)
)
ieee802dot11GroupingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ieee802dot11GroupingEntry.setStatus("mandatory")


class _Dot11LoadBalance_Type(Integer32):
    """Custom type dot11LoadBalance based on Integer32"""
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


_Dot11LoadBalance_Type.__name__ = "Integer32"
_Dot11LoadBalance_Object = MibTableColumn
dot11LoadBalance = _Dot11LoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 2, 1, 1, 2),
    _Dot11LoadBalance_Type()
)
dot11LoadBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11LoadBalance.setStatus("mandatory")


class _Dot11UserLimit_Type(Integer32):
    """Custom type dot11UserLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Dot11UserLimit_Type.__name__ = "Integer32"
_Dot11UserLimit_Object = MibTableColumn
dot11UserLimit = _Dot11UserLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 2, 1, 1, 3),
    _Dot11UserLimit_Type()
)
dot11UserLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11UserLimit.setStatus("mandatory")


class _Dot11LinkIntegrate_Type(Integer32):
    """Custom type dot11LinkIntegrate based on Integer32"""
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


_Dot11LinkIntegrate_Type.__name__ = "Integer32"
_Dot11LinkIntegrate_Object = MibTableColumn
dot11LinkIntegrate = _Dot11LinkIntegrate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 2, 1, 1, 4),
    _Dot11LinkIntegrate_Type()
)
dot11LinkIntegrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11LinkIntegrate.setStatus("mandatory")
_Ieee802dot11MultiSsid_ObjectIdentity = ObjectIdentity
ieee802dot11MultiSsid = _Ieee802dot11MultiSsid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3)
)
_Ieee802dot11MssidStateTable_Object = MibTable
ieee802dot11MssidStateTable = _Ieee802dot11MssidStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ieee802dot11MssidStateTable.setStatus("mandatory")
_Ieee802dot11MssidStateEntry_Object = MibTableRow
ieee802dot11MssidStateEntry = _Ieee802dot11MssidStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 1, 1)
)
ieee802dot11MssidStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ieee802dot11MssidStateEntry.setStatus("mandatory")


class _Dot11MssidState_Type(Integer32):
    """Custom type dot11MssidState based on Integer32"""
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


_Dot11MssidState_Type.__name__ = "Integer32"
_Dot11MssidState_Object = MibTableColumn
dot11MssidState = _Dot11MssidState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 1, 1, 2),
    _Dot11MssidState_Type()
)
dot11MssidState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidState.setStatus("mandatory")
_Ieee802dot11VlanTable_Object = MibTable
ieee802dot11VlanTable = _Ieee802dot11VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 2)
)
if mibBuilder.loadTexts:
    ieee802dot11VlanTable.setStatus("mandatory")
_Ieee802dot11VlanEntry_Object = MibTableRow
ieee802dot11VlanEntry = _Ieee802dot11VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 2, 1)
)
ieee802dot11VlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ieee802dot11VlanEntry.setStatus("mandatory")


class _Dot11VlanState_Type(Integer32):
    """Custom type dot11VlanState based on Integer32"""
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


_Dot11VlanState_Type.__name__ = "Integer32"
_Dot11VlanState_Object = MibTableColumn
dot11VlanState = _Dot11VlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 2, 1, 1),
    _Dot11VlanState_Type()
)
dot11VlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11VlanState.setStatus("mandatory")
_Ieee802dot11MssidTable_Object = MibTable
ieee802dot11MssidTable = _Ieee802dot11MssidTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3)
)
if mibBuilder.loadTexts:
    ieee802dot11MssidTable.setStatus("mandatory")
_Ieee802dot11MssidEntry_Object = MibTableRow
ieee802dot11MssidEntry = _Ieee802dot11MssidEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1)
)
ieee802dot11MssidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DWL-3200", "dot11MssidIndex"),
)
if mibBuilder.loadTexts:
    ieee802dot11MssidEntry.setStatus("mandatory")
_Dot11MssidIndex_Type = Integer32
_Dot11MssidIndex_Object = MibTableColumn
dot11MssidIndex = _Dot11MssidIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 2),
    _Dot11MssidIndex_Type()
)
dot11MssidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11MssidIndex.setStatus("mandatory")


class _Dot11MssIndividualState_Type(Integer32):
    """Custom type dot11MssIndividualState based on Integer32"""
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


_Dot11MssIndividualState_Type.__name__ = "Integer32"
_Dot11MssIndividualState_Object = MibTableColumn
dot11MssIndividualState = _Dot11MssIndividualState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 3),
    _Dot11MssIndividualState_Type()
)
dot11MssIndividualState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssIndividualState.setStatus("mandatory")


class _Dot11MssidSsid_Type(OctetString):
    """Custom type dot11MssidSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11MssidSsid_Type.__name__ = "OctetString"
_Dot11MssidSsid_Object = MibTableColumn
dot11MssidSsid = _Dot11MssidSsid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 4),
    _Dot11MssidSsid_Type()
)
dot11MssidSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidSsid.setStatus("mandatory")


class _Dot11MssidSuppress_Type(Integer32):
    """Custom type dot11MssidSuppress based on Integer32"""
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


_Dot11MssidSuppress_Type.__name__ = "Integer32"
_Dot11MssidSuppress_Object = MibTableColumn
dot11MssidSuppress = _Dot11MssidSuppress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 5),
    _Dot11MssidSuppress_Type()
)
dot11MssidSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidSuppress.setStatus("mandatory")


class _Dot11MssidAuthentication_Type(Integer32):
    """Custom type dot11MssidAuthentication based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 1),
          ("opensystem-sharedkey", 3),
          ("sharedkey", 2),
          ("wpa-auto-eap", 9),
          ("wpa-auto-psk", 8),
          ("wpa-eap", 5),
          ("wpa-psk", 4),
          ("wpa2-eap", 7),
          ("wpa2-psk", 6))
    )


_Dot11MssidAuthentication_Type.__name__ = "Integer32"
_Dot11MssidAuthentication_Object = MibTableColumn
dot11MssidAuthentication = _Dot11MssidAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 6),
    _Dot11MssidAuthentication_Type()
)
dot11MssidAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidAuthentication.setStatus("mandatory")


class _Dot11MssidEncryption_Type(Integer32):
    """Custom type dot11MssidEncryption based on Integer32"""
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


_Dot11MssidEncryption_Type.__name__ = "Integer32"
_Dot11MssidEncryption_Object = MibTableColumn
dot11MssidEncryption = _Dot11MssidEncryption_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 7),
    _Dot11MssidEncryption_Type()
)
dot11MssidEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidEncryption.setStatus("mandatory")


class _Dot11MssidWepKeyIndex_Type(Integer32):
    """Custom type dot11MssidWepKeyIndex based on Integer32"""
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
        *(("first", 1),
          ("fourth", 4),
          ("second", 2),
          ("third", 3))
    )


_Dot11MssidWepKeyIndex_Type.__name__ = "Integer32"
_Dot11MssidWepKeyIndex_Object = MibTableColumn
dot11MssidWepKeyIndex = _Dot11MssidWepKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 8),
    _Dot11MssidWepKeyIndex_Type()
)
dot11MssidWepKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidWepKeyIndex.setStatus("mandatory")
_Dot11MssidWepKey_Type = OctetString
_Dot11MssidWepKey_Object = MibTableColumn
dot11MssidWepKey = _Dot11MssidWepKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 9),
    _Dot11MssidWepKey_Type()
)
dot11MssidWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidWepKey.setStatus("mandatory")


class _Dot11MssidVlanTagID_Type(Integer32):
    """Custom type dot11MssidVlanTagID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Dot11MssidVlanTagID_Type.__name__ = "Integer32"
_Dot11MssidVlanTagID_Object = MibTableColumn
dot11MssidVlanTagID = _Dot11MssidVlanTagID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 10),
    _Dot11MssidVlanTagID_Type()
)
dot11MssidVlanTagID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidVlanTagID.setStatus("mandatory")


class _Dot11MssidCipherType_Type(Integer32):
    """Custom type dot11MssidCipherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("auto", 1),
          ("tkip", 3))
    )


_Dot11MssidCipherType_Type.__name__ = "Integer32"
_Dot11MssidCipherType_Object = MibTableColumn
dot11MssidCipherType = _Dot11MssidCipherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 11),
    _Dot11MssidCipherType_Type()
)
dot11MssidCipherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidCipherType.setStatus("mandatory")


class _Dot11MssidPassPhrase_Type(OctetString):
    """Custom type dot11MssidPassPhrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_Dot11MssidPassPhrase_Type.__name__ = "OctetString"
_Dot11MssidPassPhrase_Object = MibTableColumn
dot11MssidPassPhrase = _Dot11MssidPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 12),
    _Dot11MssidPassPhrase_Type()
)
dot11MssidPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidPassPhrase.setStatus("mandatory")


class _Dot11MssidKeyType_Type(Integer32):
    """Custom type dot11MssidKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2))
    )


_Dot11MssidKeyType_Type.__name__ = "Integer32"
_Dot11MssidKeyType_Object = MibTableColumn
dot11MssidKeyType = _Dot11MssidKeyType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 13),
    _Dot11MssidKeyType_Type()
)
dot11MssidKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidKeyType.setStatus("mandatory")


class _Dot11MssidAccountingStatus_Type(Integer32):
    """Custom type dot11MssidAccountingStatus based on Integer32"""
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


_Dot11MssidAccountingStatus_Type.__name__ = "Integer32"
_Dot11MssidAccountingStatus_Object = MibTableColumn
dot11MssidAccountingStatus = _Dot11MssidAccountingStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 14),
    _Dot11MssidAccountingStatus_Type()
)
dot11MssidAccountingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidAccountingStatus.setStatus("mandatory")


class _Dot11MssidWMM_Type(Integer32):
    """Custom type dot11MssidWMM based on Integer32"""
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


_Dot11MssidWMM_Type.__name__ = "Integer32"
_Dot11MssidWMM_Object = MibTableColumn
dot11MssidWMM = _Dot11MssidWMM_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 20),
    _Dot11MssidWMM_Type()
)
dot11MssidWMM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidWMM.setStatus("mandatory")


class _Dot11MssidDynamicVlan_Type(Integer32):
    """Custom type dot11MssidDynamicVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("manual", 1))
    )


_Dot11MssidDynamicVlan_Type.__name__ = "Integer32"
_Dot11MssidDynamicVlan_Object = MibTableColumn
dot11MssidDynamicVlan = _Dot11MssidDynamicVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 21),
    _Dot11MssidDynamicVlan_Type()
)
dot11MssidDynamicVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidDynamicVlan.setStatus("mandatory")


class _Dot11MssidEthNoTag_Type(Integer32):
    """Custom type dot11MssidEthNoTag based on Integer32"""
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


_Dot11MssidEthNoTag_Type.__name__ = "Integer32"
_Dot11MssidEthNoTag_Object = MibTableColumn
dot11MssidEthNoTag = _Dot11MssidEthNoTag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 22),
    _Dot11MssidEthNoTag_Type()
)
dot11MssidEthNoTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidEthNoTag.setStatus("mandatory")


class _Dot11MssidPriorityBySsid_Type(Integer32):
    """Custom type dot11MssidPriorityBySsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot11MssidPriorityBySsid_Type.__name__ = "Integer32"
_Dot11MssidPriorityBySsid_Object = MibTableColumn
dot11MssidPriorityBySsid = _Dot11MssidPriorityBySsid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 23),
    _Dot11MssidPriorityBySsid_Type()
)
dot11MssidPriorityBySsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidPriorityBySsid.setStatus("mandatory")


class _Dot11MssidInternalStationConnection_Type(Integer32):
    """Custom type dot11MssidInternalStationConnection based on Integer32"""
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


_Dot11MssidInternalStationConnection_Type.__name__ = "Integer32"
_Dot11MssidInternalStationConnection_Object = MibTableColumn
dot11MssidInternalStationConnection = _Dot11MssidInternalStationConnection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 3, 1, 24),
    _Dot11MssidInternalStationConnection_Type()
)
dot11MssidInternalStationConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidInternalStationConnection.setStatus("mandatory")
_Ieee802dot11functionTable_Object = MibTable
ieee802dot11functionTable = _Ieee802dot11functionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 4)
)
if mibBuilder.loadTexts:
    ieee802dot11functionTable.setStatus("mandatory")
_Ieee802dot11functionEntry_Object = MibTableRow
ieee802dot11functionEntry = _Ieee802dot11functionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 4, 1)
)
ieee802dot11functionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ieee802dot11functionEntry.setStatus("mandatory")


class _Dot11PrioritySsidState_Type(Integer32):
    """Custom type dot11PrioritySsidState based on Integer32"""
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


_Dot11PrioritySsidState_Type.__name__ = "Integer32"
_Dot11PrioritySsidState_Object = MibTableColumn
dot11PrioritySsidState = _Dot11PrioritySsidState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 3, 4, 1, 1),
    _Dot11PrioritySsidState_Type()
)
dot11PrioritySsidState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PrioritySsidState.setStatus("mandatory")
_Ieee802dot11RogueApDetection_ObjectIdentity = ObjectIdentity
ieee802dot11RogueApDetection = _Ieee802dot11RogueApDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4)
)


class _Dot11RogueApBssType_Type(Integer32):
    """Custom type dot11RogueApBssType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("independent", 2),
          ("infrastructure", 1))
    )


_Dot11RogueApBssType_Type.__name__ = "Integer32"
_Dot11RogueApBssType_Object = MibScalar
dot11RogueApBssType = _Dot11RogueApBssType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 1),
    _Dot11RogueApBssType_Type()
)
dot11RogueApBssType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApBssType.setStatus("mandatory")
_Dot11RogueApBandType_Type = Integer32
_Dot11RogueApBandType_Object = MibScalar
dot11RogueApBandType = _Dot11RogueApBandType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 2),
    _Dot11RogueApBandType_Type()
)
dot11RogueApBandType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApBandType.setStatus("mandatory")
_Dot11RogueApSecurityType_Type = Integer32
_Dot11RogueApSecurityType_Object = MibScalar
dot11RogueApSecurityType = _Dot11RogueApSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 3),
    _Dot11RogueApSecurityType_Type()
)
dot11RogueApSecurityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApSecurityType.setStatus("mandatory")
_Ieee802dot11RogueApSurvey_ObjectIdentity = ObjectIdentity
ieee802dot11RogueApSurvey = _Ieee802dot11RogueApSurvey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4)
)


class _Dot11RogueApSurveyRefresh_Type(Integer32):
    """Custom type dot11RogueApSurveyRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("refresh", 1))
    )


_Dot11RogueApSurveyRefresh_Type.__name__ = "Integer32"
_Dot11RogueApSurveyRefresh_Object = MibScalar
dot11RogueApSurveyRefresh = _Dot11RogueApSurveyRefresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 1),
    _Dot11RogueApSurveyRefresh_Type()
)
dot11RogueApSurveyRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApSurveyRefresh.setStatus("mandatory")


class _Dot11RogueApAddtoApList_Type(Integer32):
    """Custom type dot11RogueApAddtoApList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Dot11RogueApAddtoApList_Type.__name__ = "Integer32"
_Dot11RogueApAddtoApList_Object = MibScalar
dot11RogueApAddtoApList = _Dot11RogueApAddtoApList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 2),
    _Dot11RogueApAddtoApList_Type()
)
dot11RogueApAddtoApList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApAddtoApList.setStatus("mandatory")


class _Dot11RrogueApDelete_Type(Integer32):
    """Custom type dot11RrogueApDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Dot11RrogueApDelete_Type.__name__ = "Integer32"
_Dot11RrogueApDelete_Object = MibScalar
dot11RrogueApDelete = _Dot11RrogueApDelete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 3),
    _Dot11RrogueApDelete_Type()
)
dot11RrogueApDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RrogueApDelete.setStatus("mandatory")
_Ieee802dot11RogueApSurveyTable_Object = MibTable
ieee802dot11RogueApSurveyTable = _Ieee802dot11RogueApSurveyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 4)
)
if mibBuilder.loadTexts:
    ieee802dot11RogueApSurveyTable.setStatus("mandatory")
_Dot11RogueApSurveyEntry_Object = MibTableRow
dot11RogueApSurveyEntry = _Dot11RogueApSurveyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 4, 1)
)
dot11RogueApSurveyEntry.setIndexNames(
    (0, "DWL-3200", "dot11RogueApSurveyIndex"),
)
if mibBuilder.loadTexts:
    dot11RogueApSurveyEntry.setStatus("mandatory")
_Dot11RogueApSurveyIndex_Type = Integer32
_Dot11RogueApSurveyIndex_Object = MibTableColumn
dot11RogueApSurveyIndex = _Dot11RogueApSurveyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 4, 1, 1),
    _Dot11RogueApSurveyIndex_Type()
)
dot11RogueApSurveyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11RogueApSurveyIndex.setStatus("mandatory")
_Dot11RogueApSurveyBssType_Type = OctetString
_Dot11RogueApSurveyBssType_Object = MibTableColumn
dot11RogueApSurveyBssType = _Dot11RogueApSurveyBssType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 4, 1, 2),
    _Dot11RogueApSurveyBssType_Type()
)
dot11RogueApSurveyBssType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyBssType.setStatus("mandatory")
_Dot11RogueApSurveyChannel_Type = Integer32
_Dot11RogueApSurveyChannel_Object = MibTableColumn
dot11RogueApSurveyChannel = _Dot11RogueApSurveyChannel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 4, 1, 3),
    _Dot11RogueApSurveyChannel_Type()
)
dot11RogueApSurveyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyChannel.setStatus("mandatory")
_Dot11RogueApSurveyRssi_Type = Integer32
_Dot11RogueApSurveyRssi_Object = MibTableColumn
dot11RogueApSurveyRssi = _Dot11RogueApSurveyRssi_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 4, 1, 4),
    _Dot11RogueApSurveyRssi_Type()
)
dot11RogueApSurveyRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyRssi.setStatus("mandatory")
_Dot11RogueApSurveyBssid_Type = MacAddress
_Dot11RogueApSurveyBssid_Object = MibTableColumn
dot11RogueApSurveyBssid = _Dot11RogueApSurveyBssid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 4, 1, 5),
    _Dot11RogueApSurveyBssid_Type()
)
dot11RogueApSurveyBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyBssid.setStatus("mandatory")


class _Dot11RogueApSurveyAuthentication_Type(Integer32):
    """Custom type dot11RogueApSurveyAuthentication based on Integer32"""
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
        *(("off", 0),
          ("wep", 1),
          ("wpa-auto-eap", 6),
          ("wpa-auto-psk", 7),
          ("wpa-eap", 2),
          ("wpa-psk", 3),
          ("wpa2-eap", 4),
          ("wpa2-psk", 5))
    )


_Dot11RogueApSurveyAuthentication_Type.__name__ = "Integer32"
_Dot11RogueApSurveyAuthentication_Object = MibTableColumn
dot11RogueApSurveyAuthentication = _Dot11RogueApSurveyAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 4, 1, 6),
    _Dot11RogueApSurveyAuthentication_Type()
)
dot11RogueApSurveyAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyAuthentication.setStatus("mandatory")
_Dot11RogueApSurveyEncryption_Type = OctetString
_Dot11RogueApSurveyEncryption_Object = MibTableColumn
dot11RogueApSurveyEncryption = _Dot11RogueApSurveyEncryption_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 4, 1, 7),
    _Dot11RogueApSurveyEncryption_Type()
)
dot11RogueApSurveyEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyEncryption.setStatus("mandatory")


class _Dot11RogueApSurveyMode_Type(Integer32):
    """Custom type dot11RogueApSurveyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11b", 2),
          ("dot11g", 3))
    )


_Dot11RogueApSurveyMode_Type.__name__ = "Integer32"
_Dot11RogueApSurveyMode_Object = MibTableColumn
dot11RogueApSurveyMode = _Dot11RogueApSurveyMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 4, 1, 8),
    _Dot11RogueApSurveyMode_Type()
)
dot11RogueApSurveyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyMode.setStatus("mandatory")


class _Dot11RogueApSurveySsid_Type(OctetString):
    """Custom type dot11RogueApSurveySsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11RogueApSurveySsid_Type.__name__ = "OctetString"
_Dot11RogueApSurveySsid_Object = MibTableColumn
dot11RogueApSurveySsid = _Dot11RogueApSurveySsid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 4, 4, 1, 9),
    _Dot11RogueApSurveySsid_Type()
)
dot11RogueApSurveySsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveySsid.setStatus("mandatory")
_Dot11RogueApListRecord_ObjectIdentity = ObjectIdentity
dot11RogueApListRecord = _Dot11RogueApListRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5)
)


class _Dot11RogueApDeleteFromRecord_Type(Integer32):
    """Custom type dot11RogueApDeleteFromRecord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Dot11RogueApDeleteFromRecord_Type.__name__ = "Integer32"
_Dot11RogueApDeleteFromRecord_Object = MibScalar
dot11RogueApDeleteFromRecord = _Dot11RogueApDeleteFromRecord_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 1),
    _Dot11RogueApDeleteFromRecord_Type()
)
dot11RogueApDeleteFromRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApDeleteFromRecord.setStatus("mandatory")
_Dot11RogueApListRecordTable_Object = MibTable
dot11RogueApListRecordTable = _Dot11RogueApListRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 2)
)
if mibBuilder.loadTexts:
    dot11RogueApListRecordTable.setStatus("mandatory")
_Dot11RogueApListRecordEntry_Object = MibTableRow
dot11RogueApListRecordEntry = _Dot11RogueApListRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 2, 1)
)
dot11RogueApListRecordEntry.setIndexNames(
    (0, "DWL-3200", "dot11RogueApListRecordIndex"),
)
if mibBuilder.loadTexts:
    dot11RogueApListRecordEntry.setStatus("mandatory")
_Dot11RogueApListRecordIndex_Type = Integer32
_Dot11RogueApListRecordIndex_Object = MibTableColumn
dot11RogueApListRecordIndex = _Dot11RogueApListRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 2, 1, 1),
    _Dot11RogueApListRecordIndex_Type()
)
dot11RogueApListRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11RogueApListRecordIndex.setStatus("mandatory")
_Dot11RogueApListRecordBssType_Type = OctetString
_Dot11RogueApListRecordBssType_Object = MibTableColumn
dot11RogueApListRecordBssType = _Dot11RogueApListRecordBssType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 2, 1, 2),
    _Dot11RogueApListRecordBssType_Type()
)
dot11RogueApListRecordBssType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordBssType.setStatus("mandatory")
_Dot11RogueApListRecordChannel_Type = Integer32
_Dot11RogueApListRecordChannel_Object = MibTableColumn
dot11RogueApListRecordChannel = _Dot11RogueApListRecordChannel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 2, 1, 3),
    _Dot11RogueApListRecordChannel_Type()
)
dot11RogueApListRecordChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordChannel.setStatus("mandatory")
_Dot11RogueApListRecordRssi_Type = Integer32
_Dot11RogueApListRecordRssi_Object = MibTableColumn
dot11RogueApListRecordRssi = _Dot11RogueApListRecordRssi_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 2, 1, 4),
    _Dot11RogueApListRecordRssi_Type()
)
dot11RogueApListRecordRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordRssi.setStatus("mandatory")
_Dot11RogueApListRecordBssid_Type = MacAddress
_Dot11RogueApListRecordBssid_Object = MibTableColumn
dot11RogueApListRecordBssid = _Dot11RogueApListRecordBssid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 2, 1, 5),
    _Dot11RogueApListRecordBssid_Type()
)
dot11RogueApListRecordBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordBssid.setStatus("mandatory")


class _Dot11RogueApListRecordAuthentication_Type(Integer32):
    """Custom type dot11RogueApListRecordAuthentication based on Integer32"""
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
        *(("off", 0),
          ("wep", 1),
          ("wpa-auto-eap", 6),
          ("wpa-auto-psk", 7),
          ("wpa-eap", 2),
          ("wpa-psk", 3),
          ("wpa2-eap", 4),
          ("wpa2-psk", 5))
    )


_Dot11RogueApListRecordAuthentication_Type.__name__ = "Integer32"
_Dot11RogueApListRecordAuthentication_Object = MibTableColumn
dot11RogueApListRecordAuthentication = _Dot11RogueApListRecordAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 2, 1, 6),
    _Dot11RogueApListRecordAuthentication_Type()
)
dot11RogueApListRecordAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordAuthentication.setStatus("mandatory")
_Dot11RogueApListRecordEncryption_Type = OctetString
_Dot11RogueApListRecordEncryption_Object = MibTableColumn
dot11RogueApListRecordEncryption = _Dot11RogueApListRecordEncryption_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 2, 1, 7),
    _Dot11RogueApListRecordEncryption_Type()
)
dot11RogueApListRecordEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordEncryption.setStatus("mandatory")


class _Dot11RogueApListRecordMode_Type(Integer32):
    """Custom type dot11RogueApListRecordMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11b", 2),
          ("dot11g", 3))
    )


_Dot11RogueApListRecordMode_Type.__name__ = "Integer32"
_Dot11RogueApListRecordMode_Object = MibTableColumn
dot11RogueApListRecordMode = _Dot11RogueApListRecordMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 2, 1, 8),
    _Dot11RogueApListRecordMode_Type()
)
dot11RogueApListRecordMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordMode.setStatus("mandatory")


class _Dot11RogueApListRecordSsid_Type(OctetString):
    """Custom type dot11RogueApListRecordSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11RogueApListRecordSsid_Type.__name__ = "OctetString"
_Dot11RogueApListRecordSsid_Object = MibTableColumn
dot11RogueApListRecordSsid = _Dot11RogueApListRecordSsid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 5, 2, 1, 9),
    _Dot11RogueApListRecordSsid_Type()
)
dot11RogueApListRecordSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordSsid.setStatus("mandatory")


class _Dot11RogueApProtection_Type(Integer32):
    """Custom type dot11RogueApProtection based on Integer32"""
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


_Dot11RogueApProtection_Type.__name__ = "Integer32"
_Dot11RogueApProtection_Object = MibScalar
dot11RogueApProtection = _Dot11RogueApProtection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 4, 6),
    _Dot11RogueApProtection_Type()
)
dot11RogueApProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApProtection.setStatus("mandatory")
_Ieee802dot11DataRateControl_ObjectIdentity = ObjectIdentity
ieee802dot11DataRateControl = _Ieee802dot11DataRateControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5)
)
_Ieee802dot11DataRateControlTable_Object = MibTable
ieee802dot11DataRateControlTable = _Ieee802dot11DataRateControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 1)
)
if mibBuilder.loadTexts:
    ieee802dot11DataRateControlTable.setStatus("mandatory")
_Ieee802dot11DataRateControlEntry_Object = MibTableRow
ieee802dot11DataRateControlEntry = _Ieee802dot11DataRateControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 1, 1)
)
ieee802dot11DataRateControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ieee802dot11DataRateControlEntry.setStatus("mandatory")


class _Dot11DataRateControl_Type(Integer32):
    """Custom type dot11DataRateControl based on Integer32"""
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


_Dot11DataRateControl_Type.__name__ = "Integer32"
_Dot11DataRateControl_Object = MibTableColumn
dot11DataRateControl = _Dot11DataRateControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 1, 1, 2),
    _Dot11DataRateControl_Type()
)
dot11DataRateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRateControl.setStatus("mandatory")


class _Dot11DataRateSetDefault_Type(Integer32):
    """Custom type dot11DataRateSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("set", 1))
    )


_Dot11DataRateSetDefault_Type.__name__ = "Integer32"
_Dot11DataRateSetDefault_Object = MibTableColumn
dot11DataRateSetDefault = _Dot11DataRateSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 1, 1, 3),
    _Dot11DataRateSetDefault_Type()
)
dot11DataRateSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRateSetDefault.setStatus("mandatory")
_Ieee802dot11DataRateTable_Object = MibTable
ieee802dot11DataRateTable = _Ieee802dot11DataRateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2)
)
if mibBuilder.loadTexts:
    ieee802dot11DataRateTable.setStatus("mandatory")
_Ieee802dot11DataRateEntry_Object = MibTableRow
ieee802dot11DataRateEntry = _Ieee802dot11DataRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1)
)
ieee802dot11DataRateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ieee802dot11DataRateEntry.setStatus("mandatory")


class _Dot11DataRate1Mb_Type(Integer32):
    """Custom type dot11DataRate1Mb based on Integer32"""
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


_Dot11DataRate1Mb_Type.__name__ = "Integer32"
_Dot11DataRate1Mb_Object = MibTableColumn
dot11DataRate1Mb = _Dot11DataRate1Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 2),
    _Dot11DataRate1Mb_Type()
)
dot11DataRate1Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate1Mb.setStatus("mandatory")


class _Dot11DataRate2Mb_Type(Integer32):
    """Custom type dot11DataRate2Mb based on Integer32"""
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


_Dot11DataRate2Mb_Type.__name__ = "Integer32"
_Dot11DataRate2Mb_Object = MibTableColumn
dot11DataRate2Mb = _Dot11DataRate2Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 3),
    _Dot11DataRate2Mb_Type()
)
dot11DataRate2Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate2Mb.setStatus("mandatory")


class _Dot11DataRate5dot5Mb_Type(Integer32):
    """Custom type dot11DataRate5dot5Mb based on Integer32"""
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


_Dot11DataRate5dot5Mb_Type.__name__ = "Integer32"
_Dot11DataRate5dot5Mb_Object = MibTableColumn
dot11DataRate5dot5Mb = _Dot11DataRate5dot5Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 4),
    _Dot11DataRate5dot5Mb_Type()
)
dot11DataRate5dot5Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate5dot5Mb.setStatus("mandatory")


class _Dot11DataRate6Mb_Type(Integer32):
    """Custom type dot11DataRate6Mb based on Integer32"""
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


_Dot11DataRate6Mb_Type.__name__ = "Integer32"
_Dot11DataRate6Mb_Object = MibTableColumn
dot11DataRate6Mb = _Dot11DataRate6Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 5),
    _Dot11DataRate6Mb_Type()
)
dot11DataRate6Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate6Mb.setStatus("mandatory")


class _Dot11DataRate9Mb_Type(Integer32):
    """Custom type dot11DataRate9Mb based on Integer32"""
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


_Dot11DataRate9Mb_Type.__name__ = "Integer32"
_Dot11DataRate9Mb_Object = MibTableColumn
dot11DataRate9Mb = _Dot11DataRate9Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 6),
    _Dot11DataRate9Mb_Type()
)
dot11DataRate9Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate9Mb.setStatus("mandatory")


class _Dot11DataRate11Mb_Type(Integer32):
    """Custom type dot11DataRate11Mb based on Integer32"""
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


_Dot11DataRate11Mb_Type.__name__ = "Integer32"
_Dot11DataRate11Mb_Object = MibTableColumn
dot11DataRate11Mb = _Dot11DataRate11Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 7),
    _Dot11DataRate11Mb_Type()
)
dot11DataRate11Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate11Mb.setStatus("mandatory")


class _Dot11DataRate12Mb_Type(Integer32):
    """Custom type dot11DataRate12Mb based on Integer32"""
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


_Dot11DataRate12Mb_Type.__name__ = "Integer32"
_Dot11DataRate12Mb_Object = MibTableColumn
dot11DataRate12Mb = _Dot11DataRate12Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 8),
    _Dot11DataRate12Mb_Type()
)
dot11DataRate12Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate12Mb.setStatus("mandatory")


class _Dot11DataRate18Mb_Type(Integer32):
    """Custom type dot11DataRate18Mb based on Integer32"""
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


_Dot11DataRate18Mb_Type.__name__ = "Integer32"
_Dot11DataRate18Mb_Object = MibTableColumn
dot11DataRate18Mb = _Dot11DataRate18Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 9),
    _Dot11DataRate18Mb_Type()
)
dot11DataRate18Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate18Mb.setStatus("mandatory")


class _Dot11DataRate24Mb_Type(Integer32):
    """Custom type dot11DataRate24Mb based on Integer32"""
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


_Dot11DataRate24Mb_Type.__name__ = "Integer32"
_Dot11DataRate24Mb_Object = MibTableColumn
dot11DataRate24Mb = _Dot11DataRate24Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 10),
    _Dot11DataRate24Mb_Type()
)
dot11DataRate24Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate24Mb.setStatus("mandatory")


class _Dot11DataRate36Mb_Type(Integer32):
    """Custom type dot11DataRate36Mb based on Integer32"""
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


_Dot11DataRate36Mb_Type.__name__ = "Integer32"
_Dot11DataRate36Mb_Object = MibTableColumn
dot11DataRate36Mb = _Dot11DataRate36Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 11),
    _Dot11DataRate36Mb_Type()
)
dot11DataRate36Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate36Mb.setStatus("mandatory")


class _Dot11DataRate48Mb_Type(Integer32):
    """Custom type dot11DataRate48Mb based on Integer32"""
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


_Dot11DataRate48Mb_Type.__name__ = "Integer32"
_Dot11DataRate48Mb_Object = MibTableColumn
dot11DataRate48Mb = _Dot11DataRate48Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 12),
    _Dot11DataRate48Mb_Type()
)
dot11DataRate48Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate48Mb.setStatus("mandatory")


class _Dot11DataRate54Mb_Type(Integer32):
    """Custom type dot11DataRate54Mb based on Integer32"""
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


_Dot11DataRate54Mb_Type.__name__ = "Integer32"
_Dot11DataRate54Mb_Object = MibTableColumn
dot11DataRate54Mb = _Dot11DataRate54Mb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 3, 5, 2, 1, 13),
    _Dot11DataRate54Mb_Type()
)
dot11DataRate54Mb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate54Mb.setStatus("mandatory")
_Administration_ObjectIdentity = ObjectIdentity
administration = _Administration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4)
)
_Users_ObjectIdentity = ObjectIdentity
users = _Users_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 1)
)
_UsersTable_Object = MibTable
usersTable = _UsersTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usersTable.setStatus("mandatory")
_UsersEntry_Object = MibTableRow
usersEntry = _UsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 1, 1, 1)
)
usersEntry.setIndexNames(
    (0, "DWL-3200", "usersIndex"),
)
if mibBuilder.loadTexts:
    usersEntry.setStatus("mandatory")
_UsersIndex_Type = Integer32
_UsersIndex_Object = MibTableColumn
usersIndex = _UsersIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 1, 1, 1, 2),
    _UsersIndex_Type()
)
usersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usersIndex.setStatus("mandatory")


class _UsersName_Type(OctetString):
    """Custom type usersName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UsersName_Type.__name__ = "OctetString"
_UsersName_Object = MibTableColumn
usersName = _UsersName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 1, 1, 1, 3),
    _UsersName_Type()
)
usersName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usersName.setStatus("mandatory")


class _UsersPassword_Type(OctetString):
    """Custom type usersPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_UsersPassword_Type.__name__ = "OctetString"
_UsersPassword_Object = MibTableColumn
usersPassword = _UsersPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 1, 1, 1, 4),
    _UsersPassword_Type()
)
usersPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usersPassword.setStatus("mandatory")
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 2)
)


class _DeviceRestart_Type(Integer32):
    """Custom type deviceRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reboot", 1))
    )


_DeviceRestart_Type.__name__ = "Integer32"
_DeviceRestart_Object = MibScalar
deviceRestart = _DeviceRestart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 2, 1),
    _DeviceRestart_Type()
)
deviceRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceRestart.setStatus("mandatory")


class _DeviceFactoryDefault_Type(Integer32):
    """Custom type deviceFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reset", 1))
    )


_DeviceFactoryDefault_Type.__name__ = "Integer32"
_DeviceFactoryDefault_Object = MibScalar
deviceFactoryDefault = _DeviceFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 2, 2),
    _DeviceFactoryDefault_Type()
)
deviceFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceFactoryDefault.setStatus("mandatory")
_Update_ObjectIdentity = ObjectIdentity
update = _Update_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3)
)
_UpdateFirmwareVersion_Type = OctetString
_UpdateFirmwareVersion_Object = MibScalar
updateFirmwareVersion = _UpdateFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 1),
    _UpdateFirmwareVersion_Type()
)
updateFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updateFirmwareVersion.setStatus("mandatory")
_Tftp_ObjectIdentity = ObjectIdentity
tftp = _Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 2)
)
_TftpServerIPAddress_Type = IpAddress
_TftpServerIPAddress_Object = MibScalar
tftpServerIPAddress = _TftpServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 2, 1),
    _TftpServerIPAddress_Type()
)
tftpServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerIPAddress.setStatus("mandatory")
_TftpRemoteFileName_Type = OctetString
_TftpRemoteFileName_Object = MibScalar
tftpRemoteFileName = _TftpRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 2, 2),
    _TftpRemoteFileName_Type()
)
tftpRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpRemoteFileName.setStatus("mandatory")


class _TftpCommand_Type(Integer32):
    """Custom type tftpCommand based on Integer32"""
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
        *(("connect", 1),
          ("get", 2),
          ("nothing", 4),
          ("put", 3))
    )


_TftpCommand_Type.__name__ = "Integer32"
_TftpCommand_Object = MibScalar
tftpCommand = _TftpCommand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 2, 4),
    _TftpCommand_Type()
)
tftpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpCommand.setStatus("mandatory")


class _TftpUpgradeSettingCommand_Type(Integer32):
    """Custom type tftpUpgradeSettingCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("configSave", 3),
          ("factoryReset", 5),
          ("firmwareUpdate", 1),
          ("nothing", 6),
          ("reboot", 4))
    )


_TftpUpgradeSettingCommand_Type.__name__ = "Integer32"
_TftpUpgradeSettingCommand_Object = MibScalar
tftpUpgradeSettingCommand = _TftpUpgradeSettingCommand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 2, 5),
    _TftpUpgradeSettingCommand_Type()
)
tftpUpgradeSettingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpUpgradeSettingCommand.setStatus("mandatory")
_Ftp_ObjectIdentity = ObjectIdentity
ftp = _Ftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 3)
)
_FtpServerIPAddress_Type = IpAddress
_FtpServerIPAddress_Object = MibScalar
ftpServerIPAddress = _FtpServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 3, 1),
    _FtpServerIPAddress_Type()
)
ftpServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpServerIPAddress.setStatus("mandatory")
_FtpUserName_Type = OctetString
_FtpUserName_Object = MibScalar
ftpUserName = _FtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 3, 3),
    _FtpUserName_Type()
)
ftpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUserName.setStatus("mandatory")
_FtpPassword_Type = OctetString
_FtpPassword_Object = MibScalar
ftpPassword = _FtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 3, 4),
    _FtpPassword_Type()
)
ftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPassword.setStatus("mandatory")
_FtpRemoteFileName_Type = OctetString
_FtpRemoteFileName_Object = MibScalar
ftpRemoteFileName = _FtpRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 3, 5),
    _FtpRemoteFileName_Type()
)
ftpRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpRemoteFileName.setStatus("mandatory")


class _FtpCommand_Type(Integer32):
    """Custom type ftpCommand based on Integer32"""
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
        *(("connect", 1),
          ("get", 2),
          ("nothing", 4),
          ("put", 3))
    )


_FtpCommand_Type.__name__ = "Integer32"
_FtpCommand_Object = MibScalar
ftpCommand = _FtpCommand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 3, 7),
    _FtpCommand_Type()
)
ftpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpCommand.setStatus("mandatory")


class _FtpUpgradeSettingCommand_Type(Integer32):
    """Custom type ftpUpgradeSettingCommand based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("certificateFileUpdate", 7),
          ("configSave", 3),
          ("configSetting", 2),
          ("factoryReset", 5),
          ("firmwareUpdate", 1),
          ("keyFileUpdate", 8),
          ("nothing", 6),
          ("reboot", 4))
    )


_FtpUpgradeSettingCommand_Type.__name__ = "Integer32"
_FtpUpgradeSettingCommand_Object = MibScalar
ftpUpgradeSettingCommand = _FtpUpgradeSettingCommand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 3, 8),
    _FtpUpgradeSettingCommand_Type()
)
ftpUpgradeSettingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUpgradeSettingCommand.setStatus("mandatory")


class _DiscardChanges_Type(Integer32):
    """Custom type discardChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("nothing", 0))
    )


_DiscardChanges_Type.__name__ = "Integer32"
_DiscardChanges_Object = MibScalar
discardChanges = _DiscardChanges_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 3, 4),
    _DiscardChanges_Type()
)
discardChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discardChanges.setStatus("mandatory")
_Console_ObjectIdentity = ObjectIdentity
console = _Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 4)
)


class _Telnet_Type(Integer32):
    """Custom type telnet based on Integer32"""
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


_Telnet_Type.__name__ = "Integer32"
_Telnet_Object = MibScalar
telnet = _Telnet_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 4, 1),
    _Telnet_Type()
)
telnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnet.setStatus("mandatory")


class _Ssh_Type(Integer32):
    """Custom type ssh based on Integer32"""
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


_Ssh_Type.__name__ = "Integer32"
_Ssh_Object = MibScalar
ssh = _Ssh_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 4, 2),
    _Ssh_Type()
)
ssh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssh.setStatus("mandatory")


class _Timeout_Type(Integer32):
    """Custom type timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("never", 0),
          ("s180", 2),
          ("s300", 3),
          ("s60", 1),
          ("s600", 4),
          ("s900", 5))
    )


_Timeout_Type.__name__ = "Integer32"
_Timeout_Object = MibScalar
timeout = _Timeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 4, 3),
    _Timeout_Type()
)
timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeout.setStatus("mandatory")
_Web_ObjectIdentity = ObjectIdentity
web = _Web_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 5)
)
_Ssl_ObjectIdentity = ObjectIdentity
ssl = _Ssl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 7)
)
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 8)
)
_SntpServerIpAddress_Type = IpAddress
_SntpServerIpAddress_Object = MibScalar
sntpServerIpAddress = _SntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 8, 1),
    _SntpServerIpAddress_Type()
)
sntpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerIpAddress.setStatus("mandatory")


class _SntpTimeZoneIndex_Type(Integer32):
    """Custom type sntpTimeZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_SntpTimeZoneIndex_Type.__name__ = "Integer32"
_SntpTimeZoneIndex_Object = MibScalar
sntpTimeZoneIndex = _SntpTimeZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 8, 2),
    _SntpTimeZoneIndex_Type()
)
sntpTimeZoneIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpTimeZoneIndex.setStatus("mandatory")


class _SntpDayLightSaving_Type(Integer32):
    """Custom type sntpDayLightSaving based on Integer32"""
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


_SntpDayLightSaving_Type.__name__ = "Integer32"
_SntpDayLightSaving_Object = MibScalar
sntpDayLightSaving = _SntpDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 8, 3),
    _SntpDayLightSaving_Type()
)
sntpDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDayLightSaving.setStatus("mandatory")
_SntpTimeofDay_Type = OctetString
_SntpTimeofDay_Object = MibScalar
sntpTimeofDay = _SntpTimeofDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 8, 4),
    _SntpTimeofDay_Type()
)
sntpTimeofDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpTimeofDay.setStatus("mandatory")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 9)
)


class _SmtpStatus_Type(Integer32):
    """Custom type smtpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SmtpStatus_Type.__name__ = "Integer32"
_SmtpStatus_Object = MibScalar
smtpStatus = _SmtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 9, 1),
    _SmtpStatus_Type()
)
smtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpStatus.setStatus("mandatory")
_SmtpServerIpAddress_Type = IpAddress
_SmtpServerIpAddress_Object = MibScalar
smtpServerIpAddress = _SmtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 9, 2),
    _SmtpServerIpAddress_Type()
)
smtpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerIpAddress.setStatus("mandatory")
_SmtpSender_Type = OctetString
_SmtpSender_Object = MibScalar
smtpSender = _SmtpSender_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 9, 3),
    _SmtpSender_Type()
)
smtpSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSender.setStatus("mandatory")
_SmtpRecipient_Type = OctetString
_SmtpRecipient_Object = MibScalar
smtpRecipient = _SmtpRecipient_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 9, 4),
    _SmtpRecipient_Type()
)
smtpRecipient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpRecipient.setStatus("mandatory")
_ManagerIpAddressSetting_ObjectIdentity = ObjectIdentity
managerIpAddressSetting = _ManagerIpAddressSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 10)
)


class _ManagerIpAddressStatus_Type(Integer32):
    """Custom type managerIpAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ManagerIpAddressStatus_Type.__name__ = "Integer32"
_ManagerIpAddressStatus_Object = MibScalar
managerIpAddressStatus = _ManagerIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 10, 1),
    _ManagerIpAddressStatus_Type()
)
managerIpAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIpAddressStatus.setStatus("mandatory")
_ManagerIpAddressTable_Object = MibTable
managerIpAddressTable = _ManagerIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 10, 2)
)
if mibBuilder.loadTexts:
    managerIpAddressTable.setStatus("mandatory")
_ManagerIpAddressEntry_Object = MibTableRow
managerIpAddressEntry = _ManagerIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 10, 2, 1)
)
managerIpAddressEntry.setIndexNames(
    (0, "DWL-3200", "managerIpAddressIndex"),
)
if mibBuilder.loadTexts:
    managerIpAddressEntry.setStatus("mandatory")
_ManagerIpAddressIndex_Type = Integer32
_ManagerIpAddressIndex_Object = MibTableColumn
managerIpAddressIndex = _ManagerIpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 10, 2, 1, 1),
    _ManagerIpAddressIndex_Type()
)
managerIpAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    managerIpAddressIndex.setStatus("mandatory")
_ManagerIpAddress_Type = IpAddress
_ManagerIpAddress_Object = MibTableColumn
managerIpAddress = _ManagerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 10, 2, 1, 2),
    _ManagerIpAddress_Type()
)
managerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIpAddress.setStatus("mandatory")
_ManagerIpRangeTable_Object = MibTable
managerIpRangeTable = _ManagerIpRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 10, 3)
)
if mibBuilder.loadTexts:
    managerIpRangeTable.setStatus("mandatory")
_ManagerIpRangeEntry_Object = MibTableRow
managerIpRangeEntry = _ManagerIpRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 10, 3, 1)
)
managerIpRangeEntry.setIndexNames(
    (0, "DWL-3200", "managerIpRangeIndex"),
)
if mibBuilder.loadTexts:
    managerIpRangeEntry.setStatus("mandatory")
_ManagerIpRangeIndex_Type = Integer32
_ManagerIpRangeIndex_Object = MibTableColumn
managerIpRangeIndex = _ManagerIpRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 10, 3, 1, 1),
    _ManagerIpRangeIndex_Type()
)
managerIpRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    managerIpRangeIndex.setStatus("mandatory")
_ManagerStartIpAddress_Type = IpAddress
_ManagerStartIpAddress_Object = MibTableColumn
managerStartIpAddress = _ManagerStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 10, 3, 1, 2),
    _ManagerStartIpAddress_Type()
)
managerStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerStartIpAddress.setStatus("mandatory")
_ManagerEndIpAddress_Type = IpAddress
_ManagerEndIpAddress_Object = MibTableColumn
managerEndIpAddress = _ManagerEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 10, 3, 1, 3),
    _ManagerEndIpAddress_Type()
)
managerEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerEndIpAddress.setStatus("mandatory")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 11)
)


class _Pingcontrol_Type(Integer32):
    """Custom type pingcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pingcontrol_Type.__name__ = "Integer32"
_Pingcontrol_Object = MibScalar
pingcontrol = _Pingcontrol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 11, 1),
    _Pingcontrol_Type()
)
pingcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingcontrol.setStatus("mandatory")


class _AdminAPwithWlan_Type(Integer32):
    """Custom type adminAPwithWlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdminAPwithWlan_Type.__name__ = "Integer32"
_AdminAPwithWlan_Object = MibScalar
adminAPwithWlan = _AdminAPwithWlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 11, 3),
    _AdminAPwithWlan_Type()
)
adminAPwithWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminAPwithWlan.setStatus("mandatory")
_ManagerVLANIDSetting_ObjectIdentity = ObjectIdentity
managerVLANIDSetting = _ManagerVLANIDSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 12)
)


class _ManagerVLANIDStatus_Type(Integer32):
    """Custom type managerVLANIDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ManagerVLANIDStatus_Type.__name__ = "Integer32"
_ManagerVLANIDStatus_Object = MibScalar
managerVLANIDStatus = _ManagerVLANIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 12, 1),
    _ManagerVLANIDStatus_Type()
)
managerVLANIDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerVLANIDStatus.setStatus("mandatory")


class _ManagerVLANID_Type(Integer32):
    """Custom type managerVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ManagerVLANID_Type.__name__ = "Integer32"
_ManagerVLANID_Object = MibScalar
managerVLANID = _ManagerVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 4, 12, 2),
    _ManagerVLANID_Type()
)
managerVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerVLANID.setStatus("mandatory")
_Report_ObjectIdentity = ObjectIdentity
report = _Report_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5)
)
_DeviceInformation_ObjectIdentity = ObjectIdentity
deviceInformation = _DeviceInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1)
)
_DeviceInformationFirmwareVersion_Type = OctetString
_DeviceInformationFirmwareVersion_Object = MibScalar
deviceInformationFirmwareVersion = _DeviceInformationFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 1),
    _DeviceInformationFirmwareVersion_Type()
)
deviceInformationFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationFirmwareVersion.setStatus("mandatory")
_InterfaceInformation_ObjectIdentity = ObjectIdentity
interfaceInformation = _InterfaceInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 2)
)
_InterfaceInformationTable_Object = MibTable
interfaceInformationTable = _InterfaceInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    interfaceInformationTable.setStatus("mandatory")
_InterfaceInformationEntry_Object = MibTableRow
interfaceInformationEntry = _InterfaceInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 2, 1, 1)
)
interfaceInformationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    interfaceInformationEntry.setStatus("mandatory")


class _IfGetIpAddressFrom_Type(Integer32):
    """Custom type ifGetIpAddressFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_IfGetIpAddressFrom_Type.__name__ = "Integer32"
_IfGetIpAddressFrom_Object = MibTableColumn
ifGetIpAddressFrom = _IfGetIpAddressFrom_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 2, 1, 1, 1),
    _IfGetIpAddressFrom_Type()
)
ifGetIpAddressFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifGetIpAddressFrom.setStatus("mandatory")
_IfIpAddress_Type = IpAddress
_IfIpAddress_Object = MibTableColumn
ifIpAddress = _IfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 2, 1, 1, 2),
    _IfIpAddress_Type()
)
ifIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIpAddress.setStatus("mandatory")
_IfSubnetMask_Type = IpAddress
_IfSubnetMask_Object = MibTableColumn
ifSubnetMask = _IfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 2, 1, 1, 3),
    _IfSubnetMask_Type()
)
ifSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSubnetMask.setStatus("mandatory")
_IfDefaultGateway_Type = IpAddress
_IfDefaultGateway_Object = MibTableColumn
ifDefaultGateway = _IfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 2, 1, 1, 4),
    _IfDefaultGateway_Type()
)
ifDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDefaultGateway.setStatus("mandatory")
_IfMacAddress_Type = MacAddress
_IfMacAddress_Object = MibTableColumn
ifMacAddress = _IfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 2, 1, 1, 5),
    _IfMacAddress_Type()
)
ifMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMacAddress.setStatus("mandatory")
_Apstatus_ObjectIdentity = ObjectIdentity
apstatus = _Apstatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 3)
)


class _DeviceInformationCpuUtilization_Type(Integer32):
    """Custom type deviceInformationCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DeviceInformationCpuUtilization_Type.__name__ = "Integer32"
_DeviceInformationCpuUtilization_Object = MibScalar
deviceInformationCpuUtilization = _DeviceInformationCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 3, 1),
    _DeviceInformationCpuUtilization_Type()
)
deviceInformationCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationCpuUtilization.setStatus("mandatory")


class _DeviceInformationMemUtilization_Type(Integer32):
    """Custom type deviceInformationMemUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DeviceInformationMemUtilization_Type.__name__ = "Integer32"
_DeviceInformationMemUtilization_Object = MibScalar
deviceInformationMemUtilization = _DeviceInformationMemUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 1, 3, 2),
    _DeviceInformationMemUtilization_Type()
)
deviceInformationMemUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationMemUtilization.setStatus("mandatory")
_TrafficStatistics_ObjectIdentity = ObjectIdentity
trafficStatistics = _TrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2)
)
_TrafficStatisticsWired_ObjectIdentity = ObjectIdentity
trafficStatisticsWired = _TrafficStatisticsWired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 1)
)
_Dot3TrafficStatistics_ObjectIdentity = ObjectIdentity
dot3TrafficStatistics = _Dot3TrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 1, 1)
)
_Dot3TrafficStatisticsTable_Object = MibTable
dot3TrafficStatisticsTable = _Dot3TrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot3TrafficStatisticsTable.setStatus("mandatory")
_Dot3TrafficStatisticsEntry_Object = MibTableRow
dot3TrafficStatisticsEntry = _Dot3TrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 1, 1, 1, 1)
)
dot3TrafficStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3TrafficStatisticsEntry.setStatus("mandatory")
_Dot3TransmittedFrameCount_Type = Integer32
_Dot3TransmittedFrameCount_Object = MibTableColumn
dot3TransmittedFrameCount = _Dot3TransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 1, 1, 1, 1, 1),
    _Dot3TransmittedFrameCount_Type()
)
dot3TransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3TransmittedFrameCount.setStatus("mandatory")
_Dot3ReceivedFrameCount_Type = Integer32
_Dot3ReceivedFrameCount_Object = MibTableColumn
dot3ReceivedFrameCount = _Dot3ReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 1, 1, 1, 1, 2),
    _Dot3ReceivedFrameCount_Type()
)
dot3ReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ReceivedFrameCount.setStatus("mandatory")
_Dot3TransmittedByteCount_Type = Integer32
_Dot3TransmittedByteCount_Object = MibTableColumn
dot3TransmittedByteCount = _Dot3TransmittedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 1, 1, 1, 1, 3),
    _Dot3TransmittedByteCount_Type()
)
dot3TransmittedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3TransmittedByteCount.setStatus("mandatory")
_Dot3ReceivedByteCount_Type = Integer32
_Dot3ReceivedByteCount_Object = MibTableColumn
dot3ReceivedByteCount = _Dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 1, 1, 1, 1, 4),
    _Dot3ReceivedByteCount_Type()
)
dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ReceivedByteCount.setStatus("mandatory")
_TrafficStatisticsWireless_ObjectIdentity = ObjectIdentity
trafficStatisticsWireless = _TrafficStatisticsWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2)
)
_Dot11TrafficStatistics_ObjectIdentity = ObjectIdentity
dot11TrafficStatistics = _Dot11TrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1)
)
_Dot11TrafficStatisticsTable_Object = MibTable
dot11TrafficStatisticsTable = _Dot11TrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dot11TrafficStatisticsTable.setStatus("mandatory")
_Dot11TrafficStatisticsEntry_Object = MibTableRow
dot11TrafficStatisticsEntry = _Dot11TrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1)
)
dot11TrafficStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11TrafficStatisticsEntry.setStatus("mandatory")


class _Dot11TransmitSuccessRate_Type(Integer32):
    """Custom type dot11TransmitSuccessRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dot11TransmitSuccessRate_Type.__name__ = "Integer32"
_Dot11TransmitSuccessRate_Object = MibTableColumn
dot11TransmitSuccessRate = _Dot11TransmitSuccessRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 2),
    _Dot11TransmitSuccessRate_Type()
)
dot11TransmitSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmitSuccessRate.setStatus("mandatory")


class _Dot11TransmitRetryRate_Type(Integer32):
    """Custom type dot11TransmitRetryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dot11TransmitRetryRate_Type.__name__ = "Integer32"
_Dot11TransmitRetryRate_Object = MibTableColumn
dot11TransmitRetryRate = _Dot11TransmitRetryRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 3),
    _Dot11TransmitRetryRate_Type()
)
dot11TransmitRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmitRetryRate.setStatus("mandatory")


class _Dot11ReceiveSuccessRate_Type(Integer32):
    """Custom type dot11ReceiveSuccessRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dot11ReceiveSuccessRate_Type.__name__ = "Integer32"
_Dot11ReceiveSuccessRate_Object = MibTableColumn
dot11ReceiveSuccessRate = _Dot11ReceiveSuccessRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 4),
    _Dot11ReceiveSuccessRate_Type()
)
dot11ReceiveSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceiveSuccessRate.setStatus("mandatory")


class _Dot11ReceiveDuplicateRate_Type(Integer32):
    """Custom type dot11ReceiveDuplicateRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dot11ReceiveDuplicateRate_Type.__name__ = "Integer32"
_Dot11ReceiveDuplicateRate_Object = MibTableColumn
dot11ReceiveDuplicateRate = _Dot11ReceiveDuplicateRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 5),
    _Dot11ReceiveDuplicateRate_Type()
)
dot11ReceiveDuplicateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceiveDuplicateRate.setStatus("mandatory")
_Dot11RtsSuccessCount_Type = Integer32
_Dot11RtsSuccessCount_Object = MibTableColumn
dot11RtsSuccessCount = _Dot11RtsSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 6),
    _Dot11RtsSuccessCount_Type()
)
dot11RtsSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RtsSuccessCount.setStatus("mandatory")
_Dot11RtsFailureCount_Type = Integer32
_Dot11RtsFailureCount_Object = MibTableColumn
dot11RtsFailureCount = _Dot11RtsFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 7),
    _Dot11RtsFailureCount_Type()
)
dot11RtsFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RtsFailureCount.setStatus("mandatory")
_Dot11TransmittedFrameCount_Type = Integer32
_Dot11TransmittedFrameCount_Object = MibTableColumn
dot11TransmittedFrameCount = _Dot11TransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 8),
    _Dot11TransmittedFrameCount_Type()
)
dot11TransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedFrameCount.setStatus("mandatory")
_Dot11MulticastTransmittedFrameCount_Type = Integer32
_Dot11MulticastTransmittedFrameCount_Object = MibTableColumn
dot11MulticastTransmittedFrameCount = _Dot11MulticastTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 9),
    _Dot11MulticastTransmittedFrameCount_Type()
)
dot11MulticastTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MulticastTransmittedFrameCount.setStatus("mandatory")
_Dot11TransmittedErrorCount_Type = Integer32
_Dot11TransmittedErrorCount_Object = MibTableColumn
dot11TransmittedErrorCount = _Dot11TransmittedErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 10),
    _Dot11TransmittedErrorCount_Type()
)
dot11TransmittedErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedErrorCount.setStatus("mandatory")
_Dot11TransmittedTotalRetryCount_Type = Integer32
_Dot11TransmittedTotalRetryCount_Object = MibTableColumn
dot11TransmittedTotalRetryCount = _Dot11TransmittedTotalRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 11),
    _Dot11TransmittedTotalRetryCount_Type()
)
dot11TransmittedTotalRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedTotalRetryCount.setStatus("mandatory")
_Dot11TransmittedMultipleRetryCount_Type = Integer32
_Dot11TransmittedMultipleRetryCount_Object = MibTableColumn
dot11TransmittedMultipleRetryCount = _Dot11TransmittedMultipleRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 12),
    _Dot11TransmittedMultipleRetryCount_Type()
)
dot11TransmittedMultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedMultipleRetryCount.setStatus("mandatory")
_Dot11ReceivedFrameCount_Type = Integer32
_Dot11ReceivedFrameCount_Object = MibTableColumn
dot11ReceivedFrameCount = _Dot11ReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 13),
    _Dot11ReceivedFrameCount_Type()
)
dot11ReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedFrameCount.setStatus("mandatory")
_Dot11MulticastReceivedFrameCount_Type = Integer32
_Dot11MulticastReceivedFrameCount_Object = MibTableColumn
dot11MulticastReceivedFrameCount = _Dot11MulticastReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 14),
    _Dot11MulticastReceivedFrameCount_Type()
)
dot11MulticastReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MulticastReceivedFrameCount.setStatus("mandatory")
_Dot11ReceivedFrameFcsErrorCount_Type = Integer32
_Dot11ReceivedFrameFcsErrorCount_Object = MibTableColumn
dot11ReceivedFrameFcsErrorCount = _Dot11ReceivedFrameFcsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 15),
    _Dot11ReceivedFrameFcsErrorCount_Type()
)
dot11ReceivedFrameFcsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedFrameFcsErrorCount.setStatus("mandatory")
_Dot11ReceivedFrameDuplicateCount_Type = Integer32
_Dot11ReceivedFrameDuplicateCount_Object = MibTableColumn
dot11ReceivedFrameDuplicateCount = _Dot11ReceivedFrameDuplicateCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 16),
    _Dot11ReceivedFrameDuplicateCount_Type()
)
dot11ReceivedFrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedFrameDuplicateCount.setStatus("mandatory")
_Dot11AckReceivedFailureCount_Type = Integer32
_Dot11AckReceivedFailureCount_Object = MibTableColumn
dot11AckReceivedFailureCount = _Dot11AckReceivedFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 17),
    _Dot11AckReceivedFailureCount_Type()
)
dot11AckReceivedFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AckReceivedFailureCount.setStatus("mandatory")
_Dot11WepExcludedFrameCount_Type = Integer32
_Dot11WepExcludedFrameCount_Object = MibTableColumn
dot11WepExcludedFrameCount = _Dot11WepExcludedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 18),
    _Dot11WepExcludedFrameCount_Type()
)
dot11WepExcludedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WepExcludedFrameCount.setStatus("mandatory")
_Dot11WepIcvErrorCount_Type = Integer32
_Dot11WepIcvErrorCount_Object = MibTableColumn
dot11WepIcvErrorCount = _Dot11WepIcvErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 19),
    _Dot11WepIcvErrorCount_Type()
)
dot11WepIcvErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WepIcvErrorCount.setStatus("mandatory")
_Dot11TransmitedByteCount_Type = Integer32
_Dot11TransmitedByteCount_Object = MibTableColumn
dot11TransmitedByteCount = _Dot11TransmitedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 20),
    _Dot11TransmitedByteCount_Type()
)
dot11TransmitedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmitedByteCount.setStatus("mandatory")
_Dot11ReceivedByteCount_Type = Integer32
_Dot11ReceivedByteCount_Object = MibTableColumn
dot11ReceivedByteCount = _Dot11ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 1, 1, 1, 21),
    _Dot11ReceivedByteCount_Type()
)
dot11ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedByteCount.setStatus("mandatory")
_Dot16TrafficStatistics_ObjectIdentity = ObjectIdentity
dot16TrafficStatistics = _Dot16TrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 3)
)
_TrafficStatisticsOn11aEverySSID_ObjectIdentity = ObjectIdentity
trafficStatisticsOn11aEverySSID = _TrafficStatisticsOn11aEverySSID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4)
)
_TrafficStatisticsOn11APrimarySSID_ObjectIdentity = ObjectIdentity
trafficStatisticsOn11APrimarySSID = _TrafficStatisticsOn11APrimarySSID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1)
)
_OnPrimarySSIDdot11aReceivedByteCount_Type = Integer32
_OnPrimarySSIDdot11aReceivedByteCount_Object = MibScalar
onPrimarySSIDdot11aReceivedByteCount = _OnPrimarySSIDdot11aReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 1),
    _OnPrimarySSIDdot11aReceivedByteCount_Type()
)
onPrimarySSIDdot11aReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11aReceivedByteCount.setStatus("mandatory")
_OnPrimarySSIDdot11aTransmitByteCount_Type = Integer32
_OnPrimarySSIDdot11aTransmitByteCount_Object = MibScalar
onPrimarySSIDdot11aTransmitByteCount = _OnPrimarySSIDdot11aTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 2),
    _OnPrimarySSIDdot11aTransmitByteCount_Type()
)
onPrimarySSIDdot11aTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11aTransmitByteCount.setStatus("mandatory")
_On11aPrimarySSIDdot3ReceivedByteCount_Type = Integer32
_On11aPrimarySSIDdot3ReceivedByteCount_Object = MibScalar
on11aPrimarySSIDdot3ReceivedByteCount = _On11aPrimarySSIDdot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 3),
    _On11aPrimarySSIDdot3ReceivedByteCount_Type()
)
on11aPrimarySSIDdot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aPrimarySSIDdot3ReceivedByteCount.setStatus("mandatory")
_On11aPrimarySSIDdot3TransmitByteCount_Type = Integer32
_On11aPrimarySSIDdot3TransmitByteCount_Object = MibScalar
on11aPrimarySSIDdot3TransmitByteCount = _On11aPrimarySSIDdot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 4),
    _On11aPrimarySSIDdot3TransmitByteCount_Type()
)
on11aPrimarySSIDdot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aPrimarySSIDdot3TransmitByteCount.setStatus("mandatory")
_OnPrimarySSIDdot11aCRCErrorCount_Type = Integer32
_OnPrimarySSIDdot11aCRCErrorCount_Object = MibScalar
onPrimarySSIDdot11aCRCErrorCount = _OnPrimarySSIDdot11aCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 5),
    _OnPrimarySSIDdot11aCRCErrorCount_Type()
)
onPrimarySSIDdot11aCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11aCRCErrorCount.setStatus("mandatory")
_OnPrimarySSIDdot11aPHYErrorCount_Type = Integer32
_OnPrimarySSIDdot11aPHYErrorCount_Object = MibScalar
onPrimarySSIDdot11aPHYErrorCount = _OnPrimarySSIDdot11aPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 6),
    _OnPrimarySSIDdot11aPHYErrorCount_Type()
)
onPrimarySSIDdot11aPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11aPHYErrorCount.setStatus("mandatory")
_OnPrimarySSIDdot11aMICErrorCount_Type = Integer32
_OnPrimarySSIDdot11aMICErrorCount_Object = MibScalar
onPrimarySSIDdot11aMICErrorCount = _OnPrimarySSIDdot11aMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 7),
    _OnPrimarySSIDdot11aMICErrorCount_Type()
)
onPrimarySSIDdot11aMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11aMICErrorCount.setStatus("mandatory")
_OnPrimarySSIDdot11aKEYDecrErrorCount_Type = Integer32
_OnPrimarySSIDdot11aKEYDecrErrorCount_Object = MibScalar
onPrimarySSIDdot11aKEYDecrErrorCount = _OnPrimarySSIDdot11aKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 8),
    _OnPrimarySSIDdot11aKEYDecrErrorCount_Type()
)
onPrimarySSIDdot11aKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11aKEYDecrErrorCount.setStatus("mandatory")
_On11aPrimarySSIDdot3ReceivedPKTCount_Type = Integer32
_On11aPrimarySSIDdot3ReceivedPKTCount_Object = MibScalar
on11aPrimarySSIDdot3ReceivedPKTCount = _On11aPrimarySSIDdot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 9),
    _On11aPrimarySSIDdot3ReceivedPKTCount_Type()
)
on11aPrimarySSIDdot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aPrimarySSIDdot3ReceivedPKTCount.setStatus("mandatory")
_OnPrimarySSIDdot11aUserReceivedByteCount_Type = Integer32
_OnPrimarySSIDdot11aUserReceivedByteCount_Object = MibScalar
onPrimarySSIDdot11aUserReceivedByteCount = _OnPrimarySSIDdot11aUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 10),
    _OnPrimarySSIDdot11aUserReceivedByteCount_Type()
)
onPrimarySSIDdot11aUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11aUserReceivedByteCount.setStatus("mandatory")
_OnPrimarySSIDdot11aUserTransmitByteCount_Type = Integer32
_OnPrimarySSIDdot11aUserTransmitByteCount_Object = MibScalar
onPrimarySSIDdot11aUserTransmitByteCount = _OnPrimarySSIDdot11aUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 11),
    _OnPrimarySSIDdot11aUserTransmitByteCount_Type()
)
onPrimarySSIDdot11aUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11aUserTransmitByteCount.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnPrimarySSIDTable_Object = MibTable
dot11aTrafficStatisticsByTimeOnPrimarySSIDTable = _Dot11aTrafficStatisticsByTimeOnPrimarySSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 12)
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnPrimarySSIDTable.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnPrimarySSIDEntry_Object = MibTableRow
dot11aTrafficStatisticsByTimeOnPrimarySSIDEntry = _Dot11aTrafficStatisticsByTimeOnPrimarySSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 12, 1)
)
dot11aTrafficStatisticsByTimeOnPrimarySSIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnPrimarySSIDEntry.setStatus("mandatory")
_OnPrimarySSIDdot11aAssociatedMACCount_Type = Integer32
_OnPrimarySSIDdot11aAssociatedMACCount_Object = MibTableColumn
onPrimarySSIDdot11aAssociatedMACCount = _OnPrimarySSIDdot11aAssociatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 12, 1, 2),
    _OnPrimarySSIDdot11aAssociatedMACCount_Type()
)
onPrimarySSIDdot11aAssociatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11aAssociatedMACCount.setStatus("mandatory")
_OnPrimarySSIDdot11aErrorFrameRate_Type = Integer32
_OnPrimarySSIDdot11aErrorFrameRate_Object = MibTableColumn
onPrimarySSIDdot11aErrorFrameRate = _OnPrimarySSIDdot11aErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 12, 1, 3),
    _OnPrimarySSIDdot11aErrorFrameRate_Type()
)
onPrimarySSIDdot11aErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11aErrorFrameRate.setStatus("mandatory")
_On11aPrimarySSIDdot3ErrorFrameRate_Type = Integer32
_On11aPrimarySSIDdot3ErrorFrameRate_Object = MibTableColumn
on11aPrimarySSIDdot3ErrorFrameRate = _On11aPrimarySSIDdot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 12, 1, 4),
    _On11aPrimarySSIDdot3ErrorFrameRate_Type()
)
on11aPrimarySSIDdot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aPrimarySSIDdot3ErrorFrameRate.setStatus("mandatory")
_OnPrimarySSIDdot11aWirelessUsage_Type = Integer32
_OnPrimarySSIDdot11aWirelessUsage_Object = MibTableColumn
onPrimarySSIDdot11aWirelessUsage = _OnPrimarySSIDdot11aWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 1, 12, 1, 5),
    _OnPrimarySSIDdot11aWirelessUsage_Type()
)
onPrimarySSIDdot11aWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11aWirelessUsage.setStatus("mandatory")
_TrafficStatisticsOn11aSSID1_ObjectIdentity = ObjectIdentity
trafficStatisticsOn11aSSID1 = _TrafficStatisticsOn11aSSID1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2)
)
_OnSSID1dot11aReceivedByteCount_Type = Integer32
_OnSSID1dot11aReceivedByteCount_Object = MibScalar
onSSID1dot11aReceivedByteCount = _OnSSID1dot11aReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 1),
    _OnSSID1dot11aReceivedByteCount_Type()
)
onSSID1dot11aReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11aReceivedByteCount.setStatus("mandatory")
_OnSSID1dot11aTransmitByteCount_Type = Integer32
_OnSSID1dot11aTransmitByteCount_Object = MibScalar
onSSID1dot11aTransmitByteCount = _OnSSID1dot11aTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 2),
    _OnSSID1dot11aTransmitByteCount_Type()
)
onSSID1dot11aTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11aTransmitByteCount.setStatus("mandatory")
_On11aSSID1dot3ReceivedByteCount_Type = Integer32
_On11aSSID1dot3ReceivedByteCount_Object = MibScalar
on11aSSID1dot3ReceivedByteCount = _On11aSSID1dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 3),
    _On11aSSID1dot3ReceivedByteCount_Type()
)
on11aSSID1dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID1dot3ReceivedByteCount.setStatus("mandatory")
_On11aSSID1dot3TransmitByteCount_Type = Integer32
_On11aSSID1dot3TransmitByteCount_Object = MibScalar
on11aSSID1dot3TransmitByteCount = _On11aSSID1dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 4),
    _On11aSSID1dot3TransmitByteCount_Type()
)
on11aSSID1dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID1dot3TransmitByteCount.setStatus("mandatory")
_OnSSID1dot11aCRCErrorCount_Type = Integer32
_OnSSID1dot11aCRCErrorCount_Object = MibScalar
onSSID1dot11aCRCErrorCount = _OnSSID1dot11aCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 5),
    _OnSSID1dot11aCRCErrorCount_Type()
)
onSSID1dot11aCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11aCRCErrorCount.setStatus("mandatory")
_OnSSID1dot11aPHYErrorCount_Type = Integer32
_OnSSID1dot11aPHYErrorCount_Object = MibScalar
onSSID1dot11aPHYErrorCount = _OnSSID1dot11aPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 6),
    _OnSSID1dot11aPHYErrorCount_Type()
)
onSSID1dot11aPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11aPHYErrorCount.setStatus("mandatory")
_OnSSID1dot11aMICErrorCount_Type = Integer32
_OnSSID1dot11aMICErrorCount_Object = MibScalar
onSSID1dot11aMICErrorCount = _OnSSID1dot11aMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 7),
    _OnSSID1dot11aMICErrorCount_Type()
)
onSSID1dot11aMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11aMICErrorCount.setStatus("mandatory")
_OnSSID1dot11aKEYDecrErrorCount_Type = Integer32
_OnSSID1dot11aKEYDecrErrorCount_Object = MibScalar
onSSID1dot11aKEYDecrErrorCount = _OnSSID1dot11aKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 8),
    _OnSSID1dot11aKEYDecrErrorCount_Type()
)
onSSID1dot11aKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11aKEYDecrErrorCount.setStatus("mandatory")
_On11aSSID1dot3ReceivedPKTCount_Type = Integer32
_On11aSSID1dot3ReceivedPKTCount_Object = MibScalar
on11aSSID1dot3ReceivedPKTCount = _On11aSSID1dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 9),
    _On11aSSID1dot3ReceivedPKTCount_Type()
)
on11aSSID1dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID1dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID1dot11aUserReceivedByteCount_Type = Integer32
_OnSSID1dot11aUserReceivedByteCount_Object = MibScalar
onSSID1dot11aUserReceivedByteCount = _OnSSID1dot11aUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 10),
    _OnSSID1dot11aUserReceivedByteCount_Type()
)
onSSID1dot11aUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11aUserReceivedByteCount.setStatus("mandatory")
_OnSSID1dot11aUserTransmitByteCount_Type = Integer32
_OnSSID1dot11aUserTransmitByteCount_Object = MibScalar
onSSID1dot11aUserTransmitByteCount = _OnSSID1dot11aUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 11),
    _OnSSID1dot11aUserTransmitByteCount_Type()
)
onSSID1dot11aUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11aUserTransmitByteCount.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID1Table_Object = MibTable
dot11aTrafficStatisticsByTimeOnSSID1Table = _Dot11aTrafficStatisticsByTimeOnSSID1Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 12)
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID1Table.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID1Entry_Object = MibTableRow
dot11aTrafficStatisticsByTimeOnSSID1Entry = _Dot11aTrafficStatisticsByTimeOnSSID1Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 12, 1)
)
dot11aTrafficStatisticsByTimeOnSSID1Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID1Entry.setStatus("mandatory")
_OnSSID1dot11AssociatedMACCount_Type = Integer32
_OnSSID1dot11AssociatedMACCount_Object = MibTableColumn
onSSID1dot11AssociatedMACCount = _OnSSID1dot11AssociatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 12, 1, 2),
    _OnSSID1dot11AssociatedMACCount_Type()
)
onSSID1dot11AssociatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11AssociatedMACCount.setStatus("mandatory")
_OnSSID1dot11aErrorFrameRate_Type = Integer32
_OnSSID1dot11aErrorFrameRate_Object = MibTableColumn
onSSID1dot11aErrorFrameRate = _OnSSID1dot11aErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 12, 1, 3),
    _OnSSID1dot11aErrorFrameRate_Type()
)
onSSID1dot11aErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11aErrorFrameRate.setStatus("mandatory")
_On11aSSID1dot3ErrorFrameRate_Type = Integer32
_On11aSSID1dot3ErrorFrameRate_Object = MibTableColumn
on11aSSID1dot3ErrorFrameRate = _On11aSSID1dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 12, 1, 4),
    _On11aSSID1dot3ErrorFrameRate_Type()
)
on11aSSID1dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID1dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID1dot11aWirelessUsage_Type = Integer32
_OnSSID1dot11aWirelessUsage_Object = MibTableColumn
onSSID1dot11aWirelessUsage = _OnSSID1dot11aWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 2, 12, 1, 5),
    _OnSSID1dot11aWirelessUsage_Type()
)
onSSID1dot11aWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11aWirelessUsage.setStatus("mandatory")
_TrafficStatisticsOn11aSSID2_ObjectIdentity = ObjectIdentity
trafficStatisticsOn11aSSID2 = _TrafficStatisticsOn11aSSID2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3)
)
_OnSSID2dot11aReceivedByteCount_Type = Integer32
_OnSSID2dot11aReceivedByteCount_Object = MibScalar
onSSID2dot11aReceivedByteCount = _OnSSID2dot11aReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 1),
    _OnSSID2dot11aReceivedByteCount_Type()
)
onSSID2dot11aReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11aReceivedByteCount.setStatus("mandatory")
_OnSSID2dot11aTransmitByteCount_Type = Integer32
_OnSSID2dot11aTransmitByteCount_Object = MibScalar
onSSID2dot11aTransmitByteCount = _OnSSID2dot11aTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 2),
    _OnSSID2dot11aTransmitByteCount_Type()
)
onSSID2dot11aTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11aTransmitByteCount.setStatus("mandatory")
_On11aSSID2dot3ReceivedByteCount_Type = Integer32
_On11aSSID2dot3ReceivedByteCount_Object = MibScalar
on11aSSID2dot3ReceivedByteCount = _On11aSSID2dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 3),
    _On11aSSID2dot3ReceivedByteCount_Type()
)
on11aSSID2dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID2dot3ReceivedByteCount.setStatus("mandatory")
_On11aSSID2dot3TransmitByteCount_Type = Integer32
_On11aSSID2dot3TransmitByteCount_Object = MibScalar
on11aSSID2dot3TransmitByteCount = _On11aSSID2dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 4),
    _On11aSSID2dot3TransmitByteCount_Type()
)
on11aSSID2dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID2dot3TransmitByteCount.setStatus("mandatory")
_OnSSID2dot11aCRCErrorCount_Type = Integer32
_OnSSID2dot11aCRCErrorCount_Object = MibScalar
onSSID2dot11aCRCErrorCount = _OnSSID2dot11aCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 5),
    _OnSSID2dot11aCRCErrorCount_Type()
)
onSSID2dot11aCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11aCRCErrorCount.setStatus("mandatory")
_OnSSID2dot11aPHYErrorCount_Type = Integer32
_OnSSID2dot11aPHYErrorCount_Object = MibScalar
onSSID2dot11aPHYErrorCount = _OnSSID2dot11aPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 6),
    _OnSSID2dot11aPHYErrorCount_Type()
)
onSSID2dot11aPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11aPHYErrorCount.setStatus("mandatory")
_OnSSID2dot11aMICErrorCount_Type = Integer32
_OnSSID2dot11aMICErrorCount_Object = MibScalar
onSSID2dot11aMICErrorCount = _OnSSID2dot11aMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 7),
    _OnSSID2dot11aMICErrorCount_Type()
)
onSSID2dot11aMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11aMICErrorCount.setStatus("mandatory")
_OnSSID2dot11aKEYDecrErrorCount_Type = Integer32
_OnSSID2dot11aKEYDecrErrorCount_Object = MibScalar
onSSID2dot11aKEYDecrErrorCount = _OnSSID2dot11aKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 8),
    _OnSSID2dot11aKEYDecrErrorCount_Type()
)
onSSID2dot11aKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11aKEYDecrErrorCount.setStatus("mandatory")
_On11aSSID2dot3ReceivedPKTCount_Type = Integer32
_On11aSSID2dot3ReceivedPKTCount_Object = MibScalar
on11aSSID2dot3ReceivedPKTCount = _On11aSSID2dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 9),
    _On11aSSID2dot3ReceivedPKTCount_Type()
)
on11aSSID2dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID2dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID2dot11aUserReceivedByteCount_Type = Integer32
_OnSSID2dot11aUserReceivedByteCount_Object = MibScalar
onSSID2dot11aUserReceivedByteCount = _OnSSID2dot11aUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 10),
    _OnSSID2dot11aUserReceivedByteCount_Type()
)
onSSID2dot11aUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11aUserReceivedByteCount.setStatus("mandatory")
_OnSSID2dot11aUserTransmitByteCount_Type = Integer32
_OnSSID2dot11aUserTransmitByteCount_Object = MibScalar
onSSID2dot11aUserTransmitByteCount = _OnSSID2dot11aUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 11),
    _OnSSID2dot11aUserTransmitByteCount_Type()
)
onSSID2dot11aUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11aUserTransmitByteCount.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID2Table_Object = MibTable
dot11aTrafficStatisticsByTimeOnSSID2Table = _Dot11aTrafficStatisticsByTimeOnSSID2Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 12)
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID2Table.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID2Entry_Object = MibTableRow
dot11aTrafficStatisticsByTimeOnSSID2Entry = _Dot11aTrafficStatisticsByTimeOnSSID2Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 12, 1)
)
dot11aTrafficStatisticsByTimeOnSSID2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID2Entry.setStatus("mandatory")
_OnSSID2dot11associatedMACCount_Type = Integer32
_OnSSID2dot11associatedMACCount_Object = MibTableColumn
onSSID2dot11associatedMACCount = _OnSSID2dot11associatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 12, 1, 2),
    _OnSSID2dot11associatedMACCount_Type()
)
onSSID2dot11associatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11associatedMACCount.setStatus("mandatory")
_OnSSID2dot11aErrorFrameRate_Type = Integer32
_OnSSID2dot11aErrorFrameRate_Object = MibTableColumn
onSSID2dot11aErrorFrameRate = _OnSSID2dot11aErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 12, 1, 3),
    _OnSSID2dot11aErrorFrameRate_Type()
)
onSSID2dot11aErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11aErrorFrameRate.setStatus("mandatory")
_On11aSSID2dot3ErrorFrameRate_Type = Integer32
_On11aSSID2dot3ErrorFrameRate_Object = MibTableColumn
on11aSSID2dot3ErrorFrameRate = _On11aSSID2dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 12, 1, 4),
    _On11aSSID2dot3ErrorFrameRate_Type()
)
on11aSSID2dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID2dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID2dot11aWirelessUsage_Type = Integer32
_OnSSID2dot11aWirelessUsage_Object = MibTableColumn
onSSID2dot11aWirelessUsage = _OnSSID2dot11aWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 3, 12, 1, 5),
    _OnSSID2dot11aWirelessUsage_Type()
)
onSSID2dot11aWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11aWirelessUsage.setStatus("mandatory")
_TrafficStatisticsOn11aSSID3_ObjectIdentity = ObjectIdentity
trafficStatisticsOn11aSSID3 = _TrafficStatisticsOn11aSSID3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4)
)
_OnSSID3dot11aReceivedByteCount_Type = Integer32
_OnSSID3dot11aReceivedByteCount_Object = MibScalar
onSSID3dot11aReceivedByteCount = _OnSSID3dot11aReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 1),
    _OnSSID3dot11aReceivedByteCount_Type()
)
onSSID3dot11aReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11aReceivedByteCount.setStatus("mandatory")
_OnSSID3dot11aTransmitByteCount_Type = Integer32
_OnSSID3dot11aTransmitByteCount_Object = MibScalar
onSSID3dot11aTransmitByteCount = _OnSSID3dot11aTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 2),
    _OnSSID3dot11aTransmitByteCount_Type()
)
onSSID3dot11aTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11aTransmitByteCount.setStatus("mandatory")
_On11aSSID3dot3ReceivedByteCount_Type = Integer32
_On11aSSID3dot3ReceivedByteCount_Object = MibScalar
on11aSSID3dot3ReceivedByteCount = _On11aSSID3dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 3),
    _On11aSSID3dot3ReceivedByteCount_Type()
)
on11aSSID3dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID3dot3ReceivedByteCount.setStatus("mandatory")
_On11aSSID3dot3TransmitByteCount_Type = Integer32
_On11aSSID3dot3TransmitByteCount_Object = MibScalar
on11aSSID3dot3TransmitByteCount = _On11aSSID3dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 4),
    _On11aSSID3dot3TransmitByteCount_Type()
)
on11aSSID3dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID3dot3TransmitByteCount.setStatus("mandatory")
_OnSSID3dot11aCRCErrorCount_Type = Integer32
_OnSSID3dot11aCRCErrorCount_Object = MibScalar
onSSID3dot11aCRCErrorCount = _OnSSID3dot11aCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 5),
    _OnSSID3dot11aCRCErrorCount_Type()
)
onSSID3dot11aCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11aCRCErrorCount.setStatus("mandatory")
_OnSSID3dot11aPHYErrorCount_Type = Integer32
_OnSSID3dot11aPHYErrorCount_Object = MibScalar
onSSID3dot11aPHYErrorCount = _OnSSID3dot11aPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 6),
    _OnSSID3dot11aPHYErrorCount_Type()
)
onSSID3dot11aPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11aPHYErrorCount.setStatus("mandatory")
_OnSSID3dot11aMICErrorCount_Type = Integer32
_OnSSID3dot11aMICErrorCount_Object = MibScalar
onSSID3dot11aMICErrorCount = _OnSSID3dot11aMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 7),
    _OnSSID3dot11aMICErrorCount_Type()
)
onSSID3dot11aMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11aMICErrorCount.setStatus("mandatory")
_OnSSID3dot11aKEYDecrErrorCount_Type = Integer32
_OnSSID3dot11aKEYDecrErrorCount_Object = MibScalar
onSSID3dot11aKEYDecrErrorCount = _OnSSID3dot11aKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 8),
    _OnSSID3dot11aKEYDecrErrorCount_Type()
)
onSSID3dot11aKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11aKEYDecrErrorCount.setStatus("mandatory")
_On11aSSID3dot3ReceivedPKTCount_Type = Integer32
_On11aSSID3dot3ReceivedPKTCount_Object = MibScalar
on11aSSID3dot3ReceivedPKTCount = _On11aSSID3dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 9),
    _On11aSSID3dot3ReceivedPKTCount_Type()
)
on11aSSID3dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID3dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID3dot11aUserReceivedByteCount_Type = Integer32
_OnSSID3dot11aUserReceivedByteCount_Object = MibScalar
onSSID3dot11aUserReceivedByteCount = _OnSSID3dot11aUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 10),
    _OnSSID3dot11aUserReceivedByteCount_Type()
)
onSSID3dot11aUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11aUserReceivedByteCount.setStatus("mandatory")
_OnSSID3dot11aUserTransmitByteCount_Type = Integer32
_OnSSID3dot11aUserTransmitByteCount_Object = MibScalar
onSSID3dot11aUserTransmitByteCount = _OnSSID3dot11aUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 11),
    _OnSSID3dot11aUserTransmitByteCount_Type()
)
onSSID3dot11aUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11aUserTransmitByteCount.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID3Table_Object = MibTable
dot11aTrafficStatisticsByTimeOnSSID3Table = _Dot11aTrafficStatisticsByTimeOnSSID3Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 12)
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID3Table.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID3Entry_Object = MibTableRow
dot11aTrafficStatisticsByTimeOnSSID3Entry = _Dot11aTrafficStatisticsByTimeOnSSID3Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 12, 1)
)
dot11aTrafficStatisticsByTimeOnSSID3Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID3Entry.setStatus("mandatory")
_OnSSID3dot11associatedMACCount_Type = Integer32
_OnSSID3dot11associatedMACCount_Object = MibTableColumn
onSSID3dot11associatedMACCount = _OnSSID3dot11associatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 12, 1, 2),
    _OnSSID3dot11associatedMACCount_Type()
)
onSSID3dot11associatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11associatedMACCount.setStatus("mandatory")
_OnSSID3dot11aErrorFrameRate_Type = Integer32
_OnSSID3dot11aErrorFrameRate_Object = MibTableColumn
onSSID3dot11aErrorFrameRate = _OnSSID3dot11aErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 12, 1, 3),
    _OnSSID3dot11aErrorFrameRate_Type()
)
onSSID3dot11aErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11aErrorFrameRate.setStatus("mandatory")
_On11aSSID3dot3ErrorFrameRate_Type = Integer32
_On11aSSID3dot3ErrorFrameRate_Object = MibTableColumn
on11aSSID3dot3ErrorFrameRate = _On11aSSID3dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 12, 1, 4),
    _On11aSSID3dot3ErrorFrameRate_Type()
)
on11aSSID3dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID3dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID3dot11aWirelessUsage_Type = Integer32
_OnSSID3dot11aWirelessUsage_Object = MibTableColumn
onSSID3dot11aWirelessUsage = _OnSSID3dot11aWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 4, 12, 1, 5),
    _OnSSID3dot11aWirelessUsage_Type()
)
onSSID3dot11aWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11aWirelessUsage.setStatus("mandatory")
_TrafficStatisticsOn11aSSID4_ObjectIdentity = ObjectIdentity
trafficStatisticsOn11aSSID4 = _TrafficStatisticsOn11aSSID4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5)
)
_OnSSID4dot11aReceivedByteCount_Type = Integer32
_OnSSID4dot11aReceivedByteCount_Object = MibScalar
onSSID4dot11aReceivedByteCount = _OnSSID4dot11aReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 1),
    _OnSSID4dot11aReceivedByteCount_Type()
)
onSSID4dot11aReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11aReceivedByteCount.setStatus("mandatory")
_OnSSID4dot11aTransmitByteCount_Type = Integer32
_OnSSID4dot11aTransmitByteCount_Object = MibScalar
onSSID4dot11aTransmitByteCount = _OnSSID4dot11aTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 2),
    _OnSSID4dot11aTransmitByteCount_Type()
)
onSSID4dot11aTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11aTransmitByteCount.setStatus("mandatory")
_On11aSSID4dot3ReceivedByteCount_Type = Integer32
_On11aSSID4dot3ReceivedByteCount_Object = MibScalar
on11aSSID4dot3ReceivedByteCount = _On11aSSID4dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 3),
    _On11aSSID4dot3ReceivedByteCount_Type()
)
on11aSSID4dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID4dot3ReceivedByteCount.setStatus("mandatory")
_On11aSSID4dot3TransmitByteCount_Type = Integer32
_On11aSSID4dot3TransmitByteCount_Object = MibScalar
on11aSSID4dot3TransmitByteCount = _On11aSSID4dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 4),
    _On11aSSID4dot3TransmitByteCount_Type()
)
on11aSSID4dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID4dot3TransmitByteCount.setStatus("mandatory")
_OnSSID4dot11aCRCErrorCount_Type = Integer32
_OnSSID4dot11aCRCErrorCount_Object = MibScalar
onSSID4dot11aCRCErrorCount = _OnSSID4dot11aCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 5),
    _OnSSID4dot11aCRCErrorCount_Type()
)
onSSID4dot11aCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11aCRCErrorCount.setStatus("mandatory")
_OnSSID4dot11aPHYErrorCount_Type = Integer32
_OnSSID4dot11aPHYErrorCount_Object = MibScalar
onSSID4dot11aPHYErrorCount = _OnSSID4dot11aPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 6),
    _OnSSID4dot11aPHYErrorCount_Type()
)
onSSID4dot11aPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11aPHYErrorCount.setStatus("mandatory")
_OnSSID4dot11aMICErrorCount_Type = Integer32
_OnSSID4dot11aMICErrorCount_Object = MibScalar
onSSID4dot11aMICErrorCount = _OnSSID4dot11aMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 7),
    _OnSSID4dot11aMICErrorCount_Type()
)
onSSID4dot11aMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11aMICErrorCount.setStatus("mandatory")
_OnSSID4dot11aKEYDecrErrorCount_Type = Integer32
_OnSSID4dot11aKEYDecrErrorCount_Object = MibScalar
onSSID4dot11aKEYDecrErrorCount = _OnSSID4dot11aKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 8),
    _OnSSID4dot11aKEYDecrErrorCount_Type()
)
onSSID4dot11aKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11aKEYDecrErrorCount.setStatus("mandatory")
_On11aSSID4dot3ReceivedPKTCount_Type = Integer32
_On11aSSID4dot3ReceivedPKTCount_Object = MibScalar
on11aSSID4dot3ReceivedPKTCount = _On11aSSID4dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 9),
    _On11aSSID4dot3ReceivedPKTCount_Type()
)
on11aSSID4dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID4dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID4dot11aUserReceivedByteCount_Type = Integer32
_OnSSID4dot11aUserReceivedByteCount_Object = MibScalar
onSSID4dot11aUserReceivedByteCount = _OnSSID4dot11aUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 10),
    _OnSSID4dot11aUserReceivedByteCount_Type()
)
onSSID4dot11aUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11aUserReceivedByteCount.setStatus("mandatory")
_OnSSID4dot11aUserTransmitByteCount_Type = Integer32
_OnSSID4dot11aUserTransmitByteCount_Object = MibScalar
onSSID4dot11aUserTransmitByteCount = _OnSSID4dot11aUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 11),
    _OnSSID4dot11aUserTransmitByteCount_Type()
)
onSSID4dot11aUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11aUserTransmitByteCount.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID4Table_Object = MibTable
dot11aTrafficStatisticsByTimeOnSSID4Table = _Dot11aTrafficStatisticsByTimeOnSSID4Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 12)
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID4Table.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID4Entry_Object = MibTableRow
dot11aTrafficStatisticsByTimeOnSSID4Entry = _Dot11aTrafficStatisticsByTimeOnSSID4Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 12, 1)
)
dot11aTrafficStatisticsByTimeOnSSID4Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID4Entry.setStatus("mandatory")
_OnSSID4dot11associatedMACCount_Type = Integer32
_OnSSID4dot11associatedMACCount_Object = MibTableColumn
onSSID4dot11associatedMACCount = _OnSSID4dot11associatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 12, 1, 2),
    _OnSSID4dot11associatedMACCount_Type()
)
onSSID4dot11associatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11associatedMACCount.setStatus("mandatory")
_OnSSID4dot11aErrorFrameRate_Type = Integer32
_OnSSID4dot11aErrorFrameRate_Object = MibTableColumn
onSSID4dot11aErrorFrameRate = _OnSSID4dot11aErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 12, 1, 3),
    _OnSSID4dot11aErrorFrameRate_Type()
)
onSSID4dot11aErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11aErrorFrameRate.setStatus("mandatory")
_On11aSSID4dot3ErrorFrameRate_Type = Integer32
_On11aSSID4dot3ErrorFrameRate_Object = MibTableColumn
on11aSSID4dot3ErrorFrameRate = _On11aSSID4dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 12, 1, 4),
    _On11aSSID4dot3ErrorFrameRate_Type()
)
on11aSSID4dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID4dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID4dot11aWirelessUsage_Type = Integer32
_OnSSID4dot11aWirelessUsage_Object = MibTableColumn
onSSID4dot11aWirelessUsage = _OnSSID4dot11aWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 5, 12, 1, 5),
    _OnSSID4dot11aWirelessUsage_Type()
)
onSSID4dot11aWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11aWirelessUsage.setStatus("mandatory")
_TrafficStatisticsOn11aSSID5_ObjectIdentity = ObjectIdentity
trafficStatisticsOn11aSSID5 = _TrafficStatisticsOn11aSSID5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6)
)
_OnSSID5dot11aReceivedByteCount_Type = Integer32
_OnSSID5dot11aReceivedByteCount_Object = MibScalar
onSSID5dot11aReceivedByteCount = _OnSSID5dot11aReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 1),
    _OnSSID5dot11aReceivedByteCount_Type()
)
onSSID5dot11aReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11aReceivedByteCount.setStatus("mandatory")
_OnSSID5dot11aTransmitByteCount_Type = Integer32
_OnSSID5dot11aTransmitByteCount_Object = MibScalar
onSSID5dot11aTransmitByteCount = _OnSSID5dot11aTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 2),
    _OnSSID5dot11aTransmitByteCount_Type()
)
onSSID5dot11aTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11aTransmitByteCount.setStatus("mandatory")
_On11aSSID5dot3ReceivedByteCount_Type = Integer32
_On11aSSID5dot3ReceivedByteCount_Object = MibScalar
on11aSSID5dot3ReceivedByteCount = _On11aSSID5dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 3),
    _On11aSSID5dot3ReceivedByteCount_Type()
)
on11aSSID5dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID5dot3ReceivedByteCount.setStatus("mandatory")
_On11aSSID5dot3TransmitByteCount_Type = Integer32
_On11aSSID5dot3TransmitByteCount_Object = MibScalar
on11aSSID5dot3TransmitByteCount = _On11aSSID5dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 4),
    _On11aSSID5dot3TransmitByteCount_Type()
)
on11aSSID5dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID5dot3TransmitByteCount.setStatus("mandatory")
_OnSSID5dot11aCRCErrorCount_Type = Integer32
_OnSSID5dot11aCRCErrorCount_Object = MibScalar
onSSID5dot11aCRCErrorCount = _OnSSID5dot11aCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 5),
    _OnSSID5dot11aCRCErrorCount_Type()
)
onSSID5dot11aCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11aCRCErrorCount.setStatus("mandatory")
_OnSSID5dot11aPHYErrorCount_Type = Integer32
_OnSSID5dot11aPHYErrorCount_Object = MibScalar
onSSID5dot11aPHYErrorCount = _OnSSID5dot11aPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 6),
    _OnSSID5dot11aPHYErrorCount_Type()
)
onSSID5dot11aPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11aPHYErrorCount.setStatus("mandatory")
_OnSSID5dot11aMICErrorCount_Type = Integer32
_OnSSID5dot11aMICErrorCount_Object = MibScalar
onSSID5dot11aMICErrorCount = _OnSSID5dot11aMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 7),
    _OnSSID5dot11aMICErrorCount_Type()
)
onSSID5dot11aMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11aMICErrorCount.setStatus("mandatory")
_OnSSID5dot11aKEYDecrErrorCount_Type = Integer32
_OnSSID5dot11aKEYDecrErrorCount_Object = MibScalar
onSSID5dot11aKEYDecrErrorCount = _OnSSID5dot11aKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 8),
    _OnSSID5dot11aKEYDecrErrorCount_Type()
)
onSSID5dot11aKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11aKEYDecrErrorCount.setStatus("mandatory")
_On11aSSID5dot3ReceivedPKTCount_Type = Integer32
_On11aSSID5dot3ReceivedPKTCount_Object = MibScalar
on11aSSID5dot3ReceivedPKTCount = _On11aSSID5dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 9),
    _On11aSSID5dot3ReceivedPKTCount_Type()
)
on11aSSID5dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID5dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID5dot11aUserReceivedByteCount_Type = Integer32
_OnSSID5dot11aUserReceivedByteCount_Object = MibScalar
onSSID5dot11aUserReceivedByteCount = _OnSSID5dot11aUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 10),
    _OnSSID5dot11aUserReceivedByteCount_Type()
)
onSSID5dot11aUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11aUserReceivedByteCount.setStatus("mandatory")
_OnSSID5dot11aUserTransmitByteCount_Type = Integer32
_OnSSID5dot11aUserTransmitByteCount_Object = MibScalar
onSSID5dot11aUserTransmitByteCount = _OnSSID5dot11aUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 11),
    _OnSSID5dot11aUserTransmitByteCount_Type()
)
onSSID5dot11aUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11aUserTransmitByteCount.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID5Table_Object = MibTable
dot11aTrafficStatisticsByTimeOnSSID5Table = _Dot11aTrafficStatisticsByTimeOnSSID5Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 12)
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID5Table.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID5Entry_Object = MibTableRow
dot11aTrafficStatisticsByTimeOnSSID5Entry = _Dot11aTrafficStatisticsByTimeOnSSID5Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 12, 1)
)
dot11aTrafficStatisticsByTimeOnSSID5Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID5Entry.setStatus("mandatory")
_OnSSID5dot11associatedMACCount_Type = Integer32
_OnSSID5dot11associatedMACCount_Object = MibTableColumn
onSSID5dot11associatedMACCount = _OnSSID5dot11associatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 12, 1, 2),
    _OnSSID5dot11associatedMACCount_Type()
)
onSSID5dot11associatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11associatedMACCount.setStatus("mandatory")
_OnSSID5dot11aErrorFrameRate_Type = Integer32
_OnSSID5dot11aErrorFrameRate_Object = MibTableColumn
onSSID5dot11aErrorFrameRate = _OnSSID5dot11aErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 12, 1, 3),
    _OnSSID5dot11aErrorFrameRate_Type()
)
onSSID5dot11aErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11aErrorFrameRate.setStatus("mandatory")
_On11aSSID5dot3ErrorFrameRate_Type = Integer32
_On11aSSID5dot3ErrorFrameRate_Object = MibTableColumn
on11aSSID5dot3ErrorFrameRate = _On11aSSID5dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 12, 1, 4),
    _On11aSSID5dot3ErrorFrameRate_Type()
)
on11aSSID5dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID5dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID5dot11aWirelessUsage_Type = Integer32
_OnSSID5dot11aWirelessUsage_Object = MibTableColumn
onSSID5dot11aWirelessUsage = _OnSSID5dot11aWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 6, 12, 1, 5),
    _OnSSID5dot11aWirelessUsage_Type()
)
onSSID5dot11aWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11aWirelessUsage.setStatus("mandatory")
_TrafficStatisticsOn11aSSID6_ObjectIdentity = ObjectIdentity
trafficStatisticsOn11aSSID6 = _TrafficStatisticsOn11aSSID6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7)
)
_OnSSID6dot11aReceivedByteCount_Type = Integer32
_OnSSID6dot11aReceivedByteCount_Object = MibScalar
onSSID6dot11aReceivedByteCount = _OnSSID6dot11aReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 1),
    _OnSSID6dot11aReceivedByteCount_Type()
)
onSSID6dot11aReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11aReceivedByteCount.setStatus("mandatory")
_OnSSID6dot11aTransmitByteCount_Type = Integer32
_OnSSID6dot11aTransmitByteCount_Object = MibScalar
onSSID6dot11aTransmitByteCount = _OnSSID6dot11aTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 2),
    _OnSSID6dot11aTransmitByteCount_Type()
)
onSSID6dot11aTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11aTransmitByteCount.setStatus("mandatory")
_On11aSSID6dot3ReceivedByteCount_Type = Integer32
_On11aSSID6dot3ReceivedByteCount_Object = MibScalar
on11aSSID6dot3ReceivedByteCount = _On11aSSID6dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 3),
    _On11aSSID6dot3ReceivedByteCount_Type()
)
on11aSSID6dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID6dot3ReceivedByteCount.setStatus("mandatory")
_On11aSSID6dot3TransmitByteCount_Type = Integer32
_On11aSSID6dot3TransmitByteCount_Object = MibScalar
on11aSSID6dot3TransmitByteCount = _On11aSSID6dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 4),
    _On11aSSID6dot3TransmitByteCount_Type()
)
on11aSSID6dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID6dot3TransmitByteCount.setStatus("mandatory")
_OnSSID6dot11aCRCErrorCount_Type = Integer32
_OnSSID6dot11aCRCErrorCount_Object = MibScalar
onSSID6dot11aCRCErrorCount = _OnSSID6dot11aCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 5),
    _OnSSID6dot11aCRCErrorCount_Type()
)
onSSID6dot11aCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11aCRCErrorCount.setStatus("mandatory")
_OnSSID6dot11aPHYErrorCount_Type = Integer32
_OnSSID6dot11aPHYErrorCount_Object = MibScalar
onSSID6dot11aPHYErrorCount = _OnSSID6dot11aPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 6),
    _OnSSID6dot11aPHYErrorCount_Type()
)
onSSID6dot11aPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11aPHYErrorCount.setStatus("mandatory")
_OnSSID6dot11aMICErrorCount_Type = Integer32
_OnSSID6dot11aMICErrorCount_Object = MibScalar
onSSID6dot11aMICErrorCount = _OnSSID6dot11aMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 7),
    _OnSSID6dot11aMICErrorCount_Type()
)
onSSID6dot11aMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11aMICErrorCount.setStatus("mandatory")
_OnSSID6dot11aKEYDecrErrorCount_Type = Integer32
_OnSSID6dot11aKEYDecrErrorCount_Object = MibScalar
onSSID6dot11aKEYDecrErrorCount = _OnSSID6dot11aKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 8),
    _OnSSID6dot11aKEYDecrErrorCount_Type()
)
onSSID6dot11aKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11aKEYDecrErrorCount.setStatus("mandatory")
_On11aSSID6dot3ReceivedPKTCount_Type = Integer32
_On11aSSID6dot3ReceivedPKTCount_Object = MibScalar
on11aSSID6dot3ReceivedPKTCount = _On11aSSID6dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 9),
    _On11aSSID6dot3ReceivedPKTCount_Type()
)
on11aSSID6dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID6dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID6dot11aUserReceivedByteCount_Type = Integer32
_OnSSID6dot11aUserReceivedByteCount_Object = MibScalar
onSSID6dot11aUserReceivedByteCount = _OnSSID6dot11aUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 10),
    _OnSSID6dot11aUserReceivedByteCount_Type()
)
onSSID6dot11aUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11aUserReceivedByteCount.setStatus("mandatory")
_OnSSID6dot11aUserTransmitByteCount_Type = Integer32
_OnSSID6dot11aUserTransmitByteCount_Object = MibScalar
onSSID6dot11aUserTransmitByteCount = _OnSSID6dot11aUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 11),
    _OnSSID6dot11aUserTransmitByteCount_Type()
)
onSSID6dot11aUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11aUserTransmitByteCount.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID6Table_Object = MibTable
dot11aTrafficStatisticsByTimeOnSSID6Table = _Dot11aTrafficStatisticsByTimeOnSSID6Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 12)
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID6Table.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID6Entry_Object = MibTableRow
dot11aTrafficStatisticsByTimeOnSSID6Entry = _Dot11aTrafficStatisticsByTimeOnSSID6Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 12, 1)
)
dot11aTrafficStatisticsByTimeOnSSID6Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID6Entry.setStatus("mandatory")
_OnSSID6dot11associatedMACCount_Type = Integer32
_OnSSID6dot11associatedMACCount_Object = MibTableColumn
onSSID6dot11associatedMACCount = _OnSSID6dot11associatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 12, 1, 2),
    _OnSSID6dot11associatedMACCount_Type()
)
onSSID6dot11associatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11associatedMACCount.setStatus("mandatory")
_OnSSID6dot11aErrorFrameRate_Type = Integer32
_OnSSID6dot11aErrorFrameRate_Object = MibTableColumn
onSSID6dot11aErrorFrameRate = _OnSSID6dot11aErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 12, 1, 3),
    _OnSSID6dot11aErrorFrameRate_Type()
)
onSSID6dot11aErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11aErrorFrameRate.setStatus("mandatory")
_On11aSSID6dot3ErrorFrameRate_Type = Integer32
_On11aSSID6dot3ErrorFrameRate_Object = MibTableColumn
on11aSSID6dot3ErrorFrameRate = _On11aSSID6dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 12, 1, 4),
    _On11aSSID6dot3ErrorFrameRate_Type()
)
on11aSSID6dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID6dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID6dot11aWirelessUsage_Type = Integer32
_OnSSID6dot11aWirelessUsage_Object = MibTableColumn
onSSID6dot11aWirelessUsage = _OnSSID6dot11aWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 7, 12, 1, 5),
    _OnSSID6dot11aWirelessUsage_Type()
)
onSSID6dot11aWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11aWirelessUsage.setStatus("mandatory")
_TrafficStatisticsOn11aSSID7_ObjectIdentity = ObjectIdentity
trafficStatisticsOn11aSSID7 = _TrafficStatisticsOn11aSSID7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8)
)
_OnSSID7dot11aReceivedByteCount_Type = Integer32
_OnSSID7dot11aReceivedByteCount_Object = MibScalar
onSSID7dot11aReceivedByteCount = _OnSSID7dot11aReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 1),
    _OnSSID7dot11aReceivedByteCount_Type()
)
onSSID7dot11aReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11aReceivedByteCount.setStatus("mandatory")
_OnSSID7dot11aTransmitByteCount_Type = Integer32
_OnSSID7dot11aTransmitByteCount_Object = MibScalar
onSSID7dot11aTransmitByteCount = _OnSSID7dot11aTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 2),
    _OnSSID7dot11aTransmitByteCount_Type()
)
onSSID7dot11aTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11aTransmitByteCount.setStatus("mandatory")
_On11aSSID7dot3ReceivedByteCount_Type = Integer32
_On11aSSID7dot3ReceivedByteCount_Object = MibScalar
on11aSSID7dot3ReceivedByteCount = _On11aSSID7dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 3),
    _On11aSSID7dot3ReceivedByteCount_Type()
)
on11aSSID7dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID7dot3ReceivedByteCount.setStatus("mandatory")
_On11aSSID7dot3TransmitByteCount_Type = Integer32
_On11aSSID7dot3TransmitByteCount_Object = MibScalar
on11aSSID7dot3TransmitByteCount = _On11aSSID7dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 4),
    _On11aSSID7dot3TransmitByteCount_Type()
)
on11aSSID7dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID7dot3TransmitByteCount.setStatus("mandatory")
_OnSSID7dot11aCRCErrorCount_Type = Integer32
_OnSSID7dot11aCRCErrorCount_Object = MibScalar
onSSID7dot11aCRCErrorCount = _OnSSID7dot11aCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 5),
    _OnSSID7dot11aCRCErrorCount_Type()
)
onSSID7dot11aCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11aCRCErrorCount.setStatus("mandatory")
_OnSSID7dot11aPHYErrorCount_Type = Integer32
_OnSSID7dot11aPHYErrorCount_Object = MibScalar
onSSID7dot11aPHYErrorCount = _OnSSID7dot11aPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 6),
    _OnSSID7dot11aPHYErrorCount_Type()
)
onSSID7dot11aPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11aPHYErrorCount.setStatus("mandatory")
_OnSSID7dot11aMICErrorCount_Type = Integer32
_OnSSID7dot11aMICErrorCount_Object = MibScalar
onSSID7dot11aMICErrorCount = _OnSSID7dot11aMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 7),
    _OnSSID7dot11aMICErrorCount_Type()
)
onSSID7dot11aMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11aMICErrorCount.setStatus("mandatory")
_OnSSID7dot11aKEYDecrErrorCount_Type = Integer32
_OnSSID7dot11aKEYDecrErrorCount_Object = MibScalar
onSSID7dot11aKEYDecrErrorCount = _OnSSID7dot11aKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 8),
    _OnSSID7dot11aKEYDecrErrorCount_Type()
)
onSSID7dot11aKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11aKEYDecrErrorCount.setStatus("mandatory")
_On11aSSID7dot3ReceivedPKTCount_Type = Integer32
_On11aSSID7dot3ReceivedPKTCount_Object = MibScalar
on11aSSID7dot3ReceivedPKTCount = _On11aSSID7dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 9),
    _On11aSSID7dot3ReceivedPKTCount_Type()
)
on11aSSID7dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID7dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID7dot11aUserReceivedByteCount_Type = Integer32
_OnSSID7dot11aUserReceivedByteCount_Object = MibScalar
onSSID7dot11aUserReceivedByteCount = _OnSSID7dot11aUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 10),
    _OnSSID7dot11aUserReceivedByteCount_Type()
)
onSSID7dot11aUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11aUserReceivedByteCount.setStatus("mandatory")
_OnSSID7dot11aUserTransmitByteCount_Type = Integer32
_OnSSID7dot11aUserTransmitByteCount_Object = MibScalar
onSSID7dot11aUserTransmitByteCount = _OnSSID7dot11aUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 11),
    _OnSSID7dot11aUserTransmitByteCount_Type()
)
onSSID7dot11aUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11aUserTransmitByteCount.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID7Table_Object = MibTable
dot11aTrafficStatisticsByTimeOnSSID7Table = _Dot11aTrafficStatisticsByTimeOnSSID7Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 12)
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID7Table.setStatus("mandatory")
_Dot11aTrafficStatisticsByTimeOnSSID7Entry_Object = MibTableRow
dot11aTrafficStatisticsByTimeOnSSID7Entry = _Dot11aTrafficStatisticsByTimeOnSSID7Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 12, 1)
)
dot11aTrafficStatisticsByTimeOnSSID7Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11aTrafficStatisticsByTimeOnSSID7Entry.setStatus("mandatory")
_OnSSID7dot11associatedMACCount_Type = Integer32
_OnSSID7dot11associatedMACCount_Object = MibTableColumn
onSSID7dot11associatedMACCount = _OnSSID7dot11associatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 12, 1, 2),
    _OnSSID7dot11associatedMACCount_Type()
)
onSSID7dot11associatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11associatedMACCount.setStatus("mandatory")
_OnSSID7dot11aErrorFrameRate_Type = Integer32
_OnSSID7dot11aErrorFrameRate_Object = MibTableColumn
onSSID7dot11aErrorFrameRate = _OnSSID7dot11aErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 12, 1, 3),
    _OnSSID7dot11aErrorFrameRate_Type()
)
onSSID7dot11aErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11aErrorFrameRate.setStatus("mandatory")
_On11aSSID7dot3ErrorFrameRate_Type = Integer32
_On11aSSID7dot3ErrorFrameRate_Object = MibTableColumn
on11aSSID7dot3ErrorFrameRate = _On11aSSID7dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 12, 1, 4),
    _On11aSSID7dot3ErrorFrameRate_Type()
)
on11aSSID7dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11aSSID7dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID7dot11aWirelessUsage_Type = Integer32
_OnSSID7dot11aWirelessUsage_Object = MibTableColumn
onSSID7dot11aWirelessUsage = _OnSSID7dot11aWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 4, 8, 12, 1, 5),
    _OnSSID7dot11aWirelessUsage_Type()
)
onSSID7dot11aWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11aWirelessUsage.setStatus("mandatory")
_TrafficStatisticsOn11gEverySSID_ObjectIdentity = ObjectIdentity
trafficStatisticsOn11gEverySSID = _TrafficStatisticsOn11gEverySSID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5)
)
_TrafficStatisticson11gPrimarySSID_ObjectIdentity = ObjectIdentity
trafficStatisticson11gPrimarySSID = _TrafficStatisticson11gPrimarySSID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1)
)
_OnPrimarySSIDdot11gReceivedByteCount_Type = Integer32
_OnPrimarySSIDdot11gReceivedByteCount_Object = MibScalar
onPrimarySSIDdot11gReceivedByteCount = _OnPrimarySSIDdot11gReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 1),
    _OnPrimarySSIDdot11gReceivedByteCount_Type()
)
onPrimarySSIDdot11gReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11gReceivedByteCount.setStatus("mandatory")
_OnPrimarySSIDdot11gTransmitByteCount_Type = Integer32
_OnPrimarySSIDdot11gTransmitByteCount_Object = MibScalar
onPrimarySSIDdot11gTransmitByteCount = _OnPrimarySSIDdot11gTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 2),
    _OnPrimarySSIDdot11gTransmitByteCount_Type()
)
onPrimarySSIDdot11gTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11gTransmitByteCount.setStatus("mandatory")
_On11gPrimarySSIDdot3ReceivedByteCount_Type = Integer32
_On11gPrimarySSIDdot3ReceivedByteCount_Object = MibScalar
on11gPrimarySSIDdot3ReceivedByteCount = _On11gPrimarySSIDdot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 3),
    _On11gPrimarySSIDdot3ReceivedByteCount_Type()
)
on11gPrimarySSIDdot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gPrimarySSIDdot3ReceivedByteCount.setStatus("mandatory")
_On11gPrimarySSIDdot3TransmitByteCount_Type = Integer32
_On11gPrimarySSIDdot3TransmitByteCount_Object = MibScalar
on11gPrimarySSIDdot3TransmitByteCount = _On11gPrimarySSIDdot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 4),
    _On11gPrimarySSIDdot3TransmitByteCount_Type()
)
on11gPrimarySSIDdot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gPrimarySSIDdot3TransmitByteCount.setStatus("mandatory")
_OnPrimarySSIDdot11gCRCErrorCount_Type = Integer32
_OnPrimarySSIDdot11gCRCErrorCount_Object = MibScalar
onPrimarySSIDdot11gCRCErrorCount = _OnPrimarySSIDdot11gCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 5),
    _OnPrimarySSIDdot11gCRCErrorCount_Type()
)
onPrimarySSIDdot11gCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11gCRCErrorCount.setStatus("mandatory")
_OnPrimarySSIDdot11gPHYErrorCount_Type = Integer32
_OnPrimarySSIDdot11gPHYErrorCount_Object = MibScalar
onPrimarySSIDdot11gPHYErrorCount = _OnPrimarySSIDdot11gPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 6),
    _OnPrimarySSIDdot11gPHYErrorCount_Type()
)
onPrimarySSIDdot11gPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11gPHYErrorCount.setStatus("mandatory")
_OnPrimarySSIDdot11gMICErrorCount_Type = Integer32
_OnPrimarySSIDdot11gMICErrorCount_Object = MibScalar
onPrimarySSIDdot11gMICErrorCount = _OnPrimarySSIDdot11gMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 7),
    _OnPrimarySSIDdot11gMICErrorCount_Type()
)
onPrimarySSIDdot11gMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11gMICErrorCount.setStatus("mandatory")
_OnPrimarySSIDdot11gKEYDecrErrorCount_Type = Integer32
_OnPrimarySSIDdot11gKEYDecrErrorCount_Object = MibScalar
onPrimarySSIDdot11gKEYDecrErrorCount = _OnPrimarySSIDdot11gKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 8),
    _OnPrimarySSIDdot11gKEYDecrErrorCount_Type()
)
onPrimarySSIDdot11gKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11gKEYDecrErrorCount.setStatus("mandatory")
_On11gPrimarySSIDdot3ReceivedPKTCount_Type = Integer32
_On11gPrimarySSIDdot3ReceivedPKTCount_Object = MibScalar
on11gPrimarySSIDdot3ReceivedPKTCount = _On11gPrimarySSIDdot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 9),
    _On11gPrimarySSIDdot3ReceivedPKTCount_Type()
)
on11gPrimarySSIDdot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gPrimarySSIDdot3ReceivedPKTCount.setStatus("mandatory")
_OnPrimarySSIDdot11gUserReceivedByteCount_Type = Integer32
_OnPrimarySSIDdot11gUserReceivedByteCount_Object = MibScalar
onPrimarySSIDdot11gUserReceivedByteCount = _OnPrimarySSIDdot11gUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 10),
    _OnPrimarySSIDdot11gUserReceivedByteCount_Type()
)
onPrimarySSIDdot11gUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11gUserReceivedByteCount.setStatus("mandatory")
_OnPrimarySSIDdot11gUserTransmitByteCount_Type = Integer32
_OnPrimarySSIDdot11gUserTransmitByteCount_Object = MibScalar
onPrimarySSIDdot11gUserTransmitByteCount = _OnPrimarySSIDdot11gUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 11),
    _OnPrimarySSIDdot11gUserTransmitByteCount_Type()
)
onPrimarySSIDdot11gUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11gUserTransmitByteCount.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnPrimarySSIDTable_Object = MibTable
dot11gTrafficStatisticsByTimeOnPrimarySSIDTable = _Dot11gTrafficStatisticsByTimeOnPrimarySSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 12)
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnPrimarySSIDTable.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnPrimarySSIDEntry_Object = MibTableRow
dot11gTrafficStatisticsByTimeOnPrimarySSIDEntry = _Dot11gTrafficStatisticsByTimeOnPrimarySSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 12, 1)
)
dot11gTrafficStatisticsByTimeOnPrimarySSIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnPrimarySSIDEntry.setStatus("mandatory")
_OnPrimarySSIDdot11gAssociatedMACCount_Type = Integer32
_OnPrimarySSIDdot11gAssociatedMACCount_Object = MibTableColumn
onPrimarySSIDdot11gAssociatedMACCount = _OnPrimarySSIDdot11gAssociatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 12, 1, 2),
    _OnPrimarySSIDdot11gAssociatedMACCount_Type()
)
onPrimarySSIDdot11gAssociatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11gAssociatedMACCount.setStatus("mandatory")
_OnPrimarySSIDdot11gErrorFrameRate_Type = Integer32
_OnPrimarySSIDdot11gErrorFrameRate_Object = MibTableColumn
onPrimarySSIDdot11gErrorFrameRate = _OnPrimarySSIDdot11gErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 12, 1, 3),
    _OnPrimarySSIDdot11gErrorFrameRate_Type()
)
onPrimarySSIDdot11gErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11gErrorFrameRate.setStatus("mandatory")
_On11gPrimarySSIDdot3ErrorFrameRate_Type = Integer32
_On11gPrimarySSIDdot3ErrorFrameRate_Object = MibTableColumn
on11gPrimarySSIDdot3ErrorFrameRate = _On11gPrimarySSIDdot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 12, 1, 4),
    _On11gPrimarySSIDdot3ErrorFrameRate_Type()
)
on11gPrimarySSIDdot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gPrimarySSIDdot3ErrorFrameRate.setStatus("mandatory")
_OnPrimarySSIDdot11gWirelessUsage_Type = Integer32
_OnPrimarySSIDdot11gWirelessUsage_Object = MibTableColumn
onPrimarySSIDdot11gWirelessUsage = _OnPrimarySSIDdot11gWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 1, 12, 1, 5),
    _OnPrimarySSIDdot11gWirelessUsage_Type()
)
onPrimarySSIDdot11gWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onPrimarySSIDdot11gWirelessUsage.setStatus("mandatory")
_TrafficStatisticson11gSSID1_ObjectIdentity = ObjectIdentity
trafficStatisticson11gSSID1 = _TrafficStatisticson11gSSID1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2)
)
_OnSSID1dot11gReceivedByteCount_Type = Integer32
_OnSSID1dot11gReceivedByteCount_Object = MibScalar
onSSID1dot11gReceivedByteCount = _OnSSID1dot11gReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 1),
    _OnSSID1dot11gReceivedByteCount_Type()
)
onSSID1dot11gReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11gReceivedByteCount.setStatus("mandatory")
_OnSSID1dot11gTransmitByteCount_Type = Integer32
_OnSSID1dot11gTransmitByteCount_Object = MibScalar
onSSID1dot11gTransmitByteCount = _OnSSID1dot11gTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 2),
    _OnSSID1dot11gTransmitByteCount_Type()
)
onSSID1dot11gTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11gTransmitByteCount.setStatus("mandatory")
_On11gSSID1dot3ReceivedByteCount_Type = Integer32
_On11gSSID1dot3ReceivedByteCount_Object = MibScalar
on11gSSID1dot3ReceivedByteCount = _On11gSSID1dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 3),
    _On11gSSID1dot3ReceivedByteCount_Type()
)
on11gSSID1dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID1dot3ReceivedByteCount.setStatus("mandatory")
_On11gSSID1dot3TransmitByteCount_Type = Integer32
_On11gSSID1dot3TransmitByteCount_Object = MibScalar
on11gSSID1dot3TransmitByteCount = _On11gSSID1dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 4),
    _On11gSSID1dot3TransmitByteCount_Type()
)
on11gSSID1dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID1dot3TransmitByteCount.setStatus("mandatory")
_OnSSID1dot11gCRCErrorCount_Type = Integer32
_OnSSID1dot11gCRCErrorCount_Object = MibScalar
onSSID1dot11gCRCErrorCount = _OnSSID1dot11gCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 5),
    _OnSSID1dot11gCRCErrorCount_Type()
)
onSSID1dot11gCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11gCRCErrorCount.setStatus("mandatory")
_OnSSID1dot11gPHYErrorCount_Type = Integer32
_OnSSID1dot11gPHYErrorCount_Object = MibScalar
onSSID1dot11gPHYErrorCount = _OnSSID1dot11gPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 6),
    _OnSSID1dot11gPHYErrorCount_Type()
)
onSSID1dot11gPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11gPHYErrorCount.setStatus("mandatory")
_OnSSID1dot11gMICErrorCount_Type = Integer32
_OnSSID1dot11gMICErrorCount_Object = MibScalar
onSSID1dot11gMICErrorCount = _OnSSID1dot11gMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 7),
    _OnSSID1dot11gMICErrorCount_Type()
)
onSSID1dot11gMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11gMICErrorCount.setStatus("mandatory")
_OnSSID1dot11gKEYDecrErrorCount_Type = Integer32
_OnSSID1dot11gKEYDecrErrorCount_Object = MibScalar
onSSID1dot11gKEYDecrErrorCount = _OnSSID1dot11gKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 8),
    _OnSSID1dot11gKEYDecrErrorCount_Type()
)
onSSID1dot11gKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11gKEYDecrErrorCount.setStatus("mandatory")
_On11gSSID1dot3ReceivedPKTCount_Type = Integer32
_On11gSSID1dot3ReceivedPKTCount_Object = MibScalar
on11gSSID1dot3ReceivedPKTCount = _On11gSSID1dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 9),
    _On11gSSID1dot3ReceivedPKTCount_Type()
)
on11gSSID1dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID1dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID1dot11gUserReceivedByteCount_Type = Integer32
_OnSSID1dot11gUserReceivedByteCount_Object = MibScalar
onSSID1dot11gUserReceivedByteCount = _OnSSID1dot11gUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 10),
    _OnSSID1dot11gUserReceivedByteCount_Type()
)
onSSID1dot11gUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11gUserReceivedByteCount.setStatus("mandatory")
_OnSSID1dot11gUserTransmitByteCount_Type = Integer32
_OnSSID1dot11gUserTransmitByteCount_Object = MibScalar
onSSID1dot11gUserTransmitByteCount = _OnSSID1dot11gUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 11),
    _OnSSID1dot11gUserTransmitByteCount_Type()
)
onSSID1dot11gUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11gUserTransmitByteCount.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID1Table_Object = MibTable
dot11gTrafficStatisticsByTimeOnSSID1Table = _Dot11gTrafficStatisticsByTimeOnSSID1Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 12)
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID1Table.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID1Entry_Object = MibTableRow
dot11gTrafficStatisticsByTimeOnSSID1Entry = _Dot11gTrafficStatisticsByTimeOnSSID1Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 12, 1)
)
dot11gTrafficStatisticsByTimeOnSSID1Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID1Entry.setStatus("mandatory")
_OnSSID1dot11gssociatedMACCount_Type = Integer32
_OnSSID1dot11gssociatedMACCount_Object = MibTableColumn
onSSID1dot11gssociatedMACCount = _OnSSID1dot11gssociatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 12, 1, 2),
    _OnSSID1dot11gssociatedMACCount_Type()
)
onSSID1dot11gssociatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11gssociatedMACCount.setStatus("mandatory")
_OnSSID1dot11gErrorFrameRate_Type = Integer32
_OnSSID1dot11gErrorFrameRate_Object = MibTableColumn
onSSID1dot11gErrorFrameRate = _OnSSID1dot11gErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 12, 1, 3),
    _OnSSID1dot11gErrorFrameRate_Type()
)
onSSID1dot11gErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11gErrorFrameRate.setStatus("mandatory")
_On11gSSID1dot3ErrorFrameRate_Type = Integer32
_On11gSSID1dot3ErrorFrameRate_Object = MibTableColumn
on11gSSID1dot3ErrorFrameRate = _On11gSSID1dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 12, 1, 4),
    _On11gSSID1dot3ErrorFrameRate_Type()
)
on11gSSID1dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID1dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID1dot11gWirelessUsage_Type = Integer32
_OnSSID1dot11gWirelessUsage_Object = MibTableColumn
onSSID1dot11gWirelessUsage = _OnSSID1dot11gWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 2, 12, 1, 5),
    _OnSSID1dot11gWirelessUsage_Type()
)
onSSID1dot11gWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID1dot11gWirelessUsage.setStatus("mandatory")
_TrafficStatisticson11gSSID2_ObjectIdentity = ObjectIdentity
trafficStatisticson11gSSID2 = _TrafficStatisticson11gSSID2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3)
)
_OnSSID2dot11gReceivedByteCount_Type = Integer32
_OnSSID2dot11gReceivedByteCount_Object = MibScalar
onSSID2dot11gReceivedByteCount = _OnSSID2dot11gReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 1),
    _OnSSID2dot11gReceivedByteCount_Type()
)
onSSID2dot11gReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11gReceivedByteCount.setStatus("mandatory")
_OnSSID2dot11gTransmitByteCount_Type = Integer32
_OnSSID2dot11gTransmitByteCount_Object = MibScalar
onSSID2dot11gTransmitByteCount = _OnSSID2dot11gTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 2),
    _OnSSID2dot11gTransmitByteCount_Type()
)
onSSID2dot11gTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11gTransmitByteCount.setStatus("mandatory")
_On11gSSID2dot3ReceivedByteCount_Type = Integer32
_On11gSSID2dot3ReceivedByteCount_Object = MibScalar
on11gSSID2dot3ReceivedByteCount = _On11gSSID2dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 3),
    _On11gSSID2dot3ReceivedByteCount_Type()
)
on11gSSID2dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID2dot3ReceivedByteCount.setStatus("mandatory")
_On11gSSID2dot3TransmitByteCount_Type = Integer32
_On11gSSID2dot3TransmitByteCount_Object = MibScalar
on11gSSID2dot3TransmitByteCount = _On11gSSID2dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 4),
    _On11gSSID2dot3TransmitByteCount_Type()
)
on11gSSID2dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID2dot3TransmitByteCount.setStatus("mandatory")
_OnSSID2dot11gCRCErrorCount_Type = Integer32
_OnSSID2dot11gCRCErrorCount_Object = MibScalar
onSSID2dot11gCRCErrorCount = _OnSSID2dot11gCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 5),
    _OnSSID2dot11gCRCErrorCount_Type()
)
onSSID2dot11gCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11gCRCErrorCount.setStatus("mandatory")
_OnSSID2dot11gPHYErrorCount_Type = Integer32
_OnSSID2dot11gPHYErrorCount_Object = MibScalar
onSSID2dot11gPHYErrorCount = _OnSSID2dot11gPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 6),
    _OnSSID2dot11gPHYErrorCount_Type()
)
onSSID2dot11gPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11gPHYErrorCount.setStatus("mandatory")
_OnSSID2dot11gMICErrorCount_Type = Integer32
_OnSSID2dot11gMICErrorCount_Object = MibScalar
onSSID2dot11gMICErrorCount = _OnSSID2dot11gMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 7),
    _OnSSID2dot11gMICErrorCount_Type()
)
onSSID2dot11gMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11gMICErrorCount.setStatus("mandatory")
_OnSSID2dot11gKEYDecrErrorCount_Type = Integer32
_OnSSID2dot11gKEYDecrErrorCount_Object = MibScalar
onSSID2dot11gKEYDecrErrorCount = _OnSSID2dot11gKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 8),
    _OnSSID2dot11gKEYDecrErrorCount_Type()
)
onSSID2dot11gKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11gKEYDecrErrorCount.setStatus("mandatory")
_On11gSSID2dot3ReceivedPKTCount_Type = Integer32
_On11gSSID2dot3ReceivedPKTCount_Object = MibScalar
on11gSSID2dot3ReceivedPKTCount = _On11gSSID2dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 9),
    _On11gSSID2dot3ReceivedPKTCount_Type()
)
on11gSSID2dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID2dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID2dot11gUserReceivedByteCount_Type = Integer32
_OnSSID2dot11gUserReceivedByteCount_Object = MibScalar
onSSID2dot11gUserReceivedByteCount = _OnSSID2dot11gUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 10),
    _OnSSID2dot11gUserReceivedByteCount_Type()
)
onSSID2dot11gUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11gUserReceivedByteCount.setStatus("mandatory")
_OnSSID2dot11gUserTransmitByteCount_Type = Integer32
_OnSSID2dot11gUserTransmitByteCount_Object = MibScalar
onSSID2dot11gUserTransmitByteCount = _OnSSID2dot11gUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 11),
    _OnSSID2dot11gUserTransmitByteCount_Type()
)
onSSID2dot11gUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11gUserTransmitByteCount.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID2Table_Object = MibTable
dot11gTrafficStatisticsByTimeOnSSID2Table = _Dot11gTrafficStatisticsByTimeOnSSID2Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 12)
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID2Table.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID2Entry_Object = MibTableRow
dot11gTrafficStatisticsByTimeOnSSID2Entry = _Dot11gTrafficStatisticsByTimeOnSSID2Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 12, 1)
)
dot11gTrafficStatisticsByTimeOnSSID2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID2Entry.setStatus("mandatory")
_OnSSID2dot11gssociatedMACCount_Type = Integer32
_OnSSID2dot11gssociatedMACCount_Object = MibTableColumn
onSSID2dot11gssociatedMACCount = _OnSSID2dot11gssociatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 12, 1, 2),
    _OnSSID2dot11gssociatedMACCount_Type()
)
onSSID2dot11gssociatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11gssociatedMACCount.setStatus("mandatory")
_OnSSID2dot11gErrorFrameRate_Type = Integer32
_OnSSID2dot11gErrorFrameRate_Object = MibTableColumn
onSSID2dot11gErrorFrameRate = _OnSSID2dot11gErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 12, 1, 3),
    _OnSSID2dot11gErrorFrameRate_Type()
)
onSSID2dot11gErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11gErrorFrameRate.setStatus("mandatory")
_On11gSSID2dot3ErrorFrameRate_Type = Integer32
_On11gSSID2dot3ErrorFrameRate_Object = MibTableColumn
on11gSSID2dot3ErrorFrameRate = _On11gSSID2dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 12, 1, 4),
    _On11gSSID2dot3ErrorFrameRate_Type()
)
on11gSSID2dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID2dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID2dot11gWirelessUsage_Type = Integer32
_OnSSID2dot11gWirelessUsage_Object = MibTableColumn
onSSID2dot11gWirelessUsage = _OnSSID2dot11gWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 3, 12, 1, 5),
    _OnSSID2dot11gWirelessUsage_Type()
)
onSSID2dot11gWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID2dot11gWirelessUsage.setStatus("mandatory")
_TrafficStatisticson11gSSID3_ObjectIdentity = ObjectIdentity
trafficStatisticson11gSSID3 = _TrafficStatisticson11gSSID3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4)
)
_OnSSID3dot11gReceivedByteCount_Type = Integer32
_OnSSID3dot11gReceivedByteCount_Object = MibScalar
onSSID3dot11gReceivedByteCount = _OnSSID3dot11gReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 1),
    _OnSSID3dot11gReceivedByteCount_Type()
)
onSSID3dot11gReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11gReceivedByteCount.setStatus("mandatory")
_OnSSID3dot11gTransmitByteCount_Type = Integer32
_OnSSID3dot11gTransmitByteCount_Object = MibScalar
onSSID3dot11gTransmitByteCount = _OnSSID3dot11gTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 2),
    _OnSSID3dot11gTransmitByteCount_Type()
)
onSSID3dot11gTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11gTransmitByteCount.setStatus("mandatory")
_On11gSSID3dot3ReceivedByteCount_Type = Integer32
_On11gSSID3dot3ReceivedByteCount_Object = MibScalar
on11gSSID3dot3ReceivedByteCount = _On11gSSID3dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 3),
    _On11gSSID3dot3ReceivedByteCount_Type()
)
on11gSSID3dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID3dot3ReceivedByteCount.setStatus("mandatory")
_On11gSSID3dot3TransmitByteCount_Type = Integer32
_On11gSSID3dot3TransmitByteCount_Object = MibScalar
on11gSSID3dot3TransmitByteCount = _On11gSSID3dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 4),
    _On11gSSID3dot3TransmitByteCount_Type()
)
on11gSSID3dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID3dot3TransmitByteCount.setStatus("mandatory")
_OnSSID3dot11gCRCErrorCount_Type = Integer32
_OnSSID3dot11gCRCErrorCount_Object = MibScalar
onSSID3dot11gCRCErrorCount = _OnSSID3dot11gCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 5),
    _OnSSID3dot11gCRCErrorCount_Type()
)
onSSID3dot11gCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11gCRCErrorCount.setStatus("mandatory")
_OnSSID3dot11gPHYErrorCount_Type = Integer32
_OnSSID3dot11gPHYErrorCount_Object = MibScalar
onSSID3dot11gPHYErrorCount = _OnSSID3dot11gPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 6),
    _OnSSID3dot11gPHYErrorCount_Type()
)
onSSID3dot11gPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11gPHYErrorCount.setStatus("mandatory")
_OnSSID3dot11gMICErrorCount_Type = Integer32
_OnSSID3dot11gMICErrorCount_Object = MibScalar
onSSID3dot11gMICErrorCount = _OnSSID3dot11gMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 7),
    _OnSSID3dot11gMICErrorCount_Type()
)
onSSID3dot11gMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11gMICErrorCount.setStatus("mandatory")
_OnSSID3dot11gKEYDecrErrorCount_Type = Integer32
_OnSSID3dot11gKEYDecrErrorCount_Object = MibScalar
onSSID3dot11gKEYDecrErrorCount = _OnSSID3dot11gKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 8),
    _OnSSID3dot11gKEYDecrErrorCount_Type()
)
onSSID3dot11gKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11gKEYDecrErrorCount.setStatus("mandatory")
_On11gSSID3dot3ReceivedPKTCount_Type = Integer32
_On11gSSID3dot3ReceivedPKTCount_Object = MibScalar
on11gSSID3dot3ReceivedPKTCount = _On11gSSID3dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 9),
    _On11gSSID3dot3ReceivedPKTCount_Type()
)
on11gSSID3dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID3dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID3dot11gUserReceivedByteCount_Type = Integer32
_OnSSID3dot11gUserReceivedByteCount_Object = MibScalar
onSSID3dot11gUserReceivedByteCount = _OnSSID3dot11gUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 10),
    _OnSSID3dot11gUserReceivedByteCount_Type()
)
onSSID3dot11gUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11gUserReceivedByteCount.setStatus("mandatory")
_OnSSID3dot11gUserTransmitByteCount_Type = Integer32
_OnSSID3dot11gUserTransmitByteCount_Object = MibScalar
onSSID3dot11gUserTransmitByteCount = _OnSSID3dot11gUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 11),
    _OnSSID3dot11gUserTransmitByteCount_Type()
)
onSSID3dot11gUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11gUserTransmitByteCount.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID3Table_Object = MibTable
dot11gTrafficStatisticsByTimeOnSSID3Table = _Dot11gTrafficStatisticsByTimeOnSSID3Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 12)
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID3Table.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID3Entry_Object = MibTableRow
dot11gTrafficStatisticsByTimeOnSSID3Entry = _Dot11gTrafficStatisticsByTimeOnSSID3Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 12, 1)
)
dot11gTrafficStatisticsByTimeOnSSID3Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID3Entry.setStatus("mandatory")
_OnSSID3dot11gssociatedMACCount_Type = Integer32
_OnSSID3dot11gssociatedMACCount_Object = MibTableColumn
onSSID3dot11gssociatedMACCount = _OnSSID3dot11gssociatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 12, 1, 2),
    _OnSSID3dot11gssociatedMACCount_Type()
)
onSSID3dot11gssociatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11gssociatedMACCount.setStatus("mandatory")
_OnSSID3dot11gErrorFrameRate_Type = Integer32
_OnSSID3dot11gErrorFrameRate_Object = MibTableColumn
onSSID3dot11gErrorFrameRate = _OnSSID3dot11gErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 12, 1, 3),
    _OnSSID3dot11gErrorFrameRate_Type()
)
onSSID3dot11gErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11gErrorFrameRate.setStatus("mandatory")
_On11gSSID3dot3ErrorFrameRate_Type = Integer32
_On11gSSID3dot3ErrorFrameRate_Object = MibTableColumn
on11gSSID3dot3ErrorFrameRate = _On11gSSID3dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 12, 1, 4),
    _On11gSSID3dot3ErrorFrameRate_Type()
)
on11gSSID3dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID3dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID3dot11gWirelessUsage_Type = Integer32
_OnSSID3dot11gWirelessUsage_Object = MibTableColumn
onSSID3dot11gWirelessUsage = _OnSSID3dot11gWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 4, 12, 1, 5),
    _OnSSID3dot11gWirelessUsage_Type()
)
onSSID3dot11gWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID3dot11gWirelessUsage.setStatus("mandatory")
_TrafficStatisticson11gSSID4_ObjectIdentity = ObjectIdentity
trafficStatisticson11gSSID4 = _TrafficStatisticson11gSSID4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5)
)
_OnSSID4dot11gReceivedByteCount_Type = Integer32
_OnSSID4dot11gReceivedByteCount_Object = MibScalar
onSSID4dot11gReceivedByteCount = _OnSSID4dot11gReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 1),
    _OnSSID4dot11gReceivedByteCount_Type()
)
onSSID4dot11gReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11gReceivedByteCount.setStatus("mandatory")
_OnSSID4dot11gTransmitByteCount_Type = Integer32
_OnSSID4dot11gTransmitByteCount_Object = MibScalar
onSSID4dot11gTransmitByteCount = _OnSSID4dot11gTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 2),
    _OnSSID4dot11gTransmitByteCount_Type()
)
onSSID4dot11gTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11gTransmitByteCount.setStatus("mandatory")
_On11gSSID4dot3ReceivedByteCount_Type = Integer32
_On11gSSID4dot3ReceivedByteCount_Object = MibScalar
on11gSSID4dot3ReceivedByteCount = _On11gSSID4dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 3),
    _On11gSSID4dot3ReceivedByteCount_Type()
)
on11gSSID4dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID4dot3ReceivedByteCount.setStatus("mandatory")
_On11gSSID4dot3TransmitByteCount_Type = Integer32
_On11gSSID4dot3TransmitByteCount_Object = MibScalar
on11gSSID4dot3TransmitByteCount = _On11gSSID4dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 4),
    _On11gSSID4dot3TransmitByteCount_Type()
)
on11gSSID4dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID4dot3TransmitByteCount.setStatus("mandatory")
_OnSSID4dot11gCRCErrorCount_Type = Integer32
_OnSSID4dot11gCRCErrorCount_Object = MibScalar
onSSID4dot11gCRCErrorCount = _OnSSID4dot11gCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 5),
    _OnSSID4dot11gCRCErrorCount_Type()
)
onSSID4dot11gCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11gCRCErrorCount.setStatus("mandatory")
_OnSSID4dot11gPHYErrorCount_Type = Integer32
_OnSSID4dot11gPHYErrorCount_Object = MibScalar
onSSID4dot11gPHYErrorCount = _OnSSID4dot11gPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 6),
    _OnSSID4dot11gPHYErrorCount_Type()
)
onSSID4dot11gPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11gPHYErrorCount.setStatus("mandatory")
_OnSSID4dot11gMICErrorCount_Type = Integer32
_OnSSID4dot11gMICErrorCount_Object = MibScalar
onSSID4dot11gMICErrorCount = _OnSSID4dot11gMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 7),
    _OnSSID4dot11gMICErrorCount_Type()
)
onSSID4dot11gMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11gMICErrorCount.setStatus("mandatory")
_OnSSID4dot11gKEYDecrErrorCount_Type = Integer32
_OnSSID4dot11gKEYDecrErrorCount_Object = MibScalar
onSSID4dot11gKEYDecrErrorCount = _OnSSID4dot11gKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 8),
    _OnSSID4dot11gKEYDecrErrorCount_Type()
)
onSSID4dot11gKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11gKEYDecrErrorCount.setStatus("mandatory")
_On11gSSID4dot3ReceivedPKTCount_Type = Integer32
_On11gSSID4dot3ReceivedPKTCount_Object = MibScalar
on11gSSID4dot3ReceivedPKTCount = _On11gSSID4dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 9),
    _On11gSSID4dot3ReceivedPKTCount_Type()
)
on11gSSID4dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID4dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID4dot11gUserReceivedByteCount_Type = Integer32
_OnSSID4dot11gUserReceivedByteCount_Object = MibScalar
onSSID4dot11gUserReceivedByteCount = _OnSSID4dot11gUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 10),
    _OnSSID4dot11gUserReceivedByteCount_Type()
)
onSSID4dot11gUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11gUserReceivedByteCount.setStatus("mandatory")
_OnSSID4dot11gUserTransmitByteCount_Type = Integer32
_OnSSID4dot11gUserTransmitByteCount_Object = MibScalar
onSSID4dot11gUserTransmitByteCount = _OnSSID4dot11gUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 11),
    _OnSSID4dot11gUserTransmitByteCount_Type()
)
onSSID4dot11gUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11gUserTransmitByteCount.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID4Table_Object = MibTable
dot11gTrafficStatisticsByTimeOnSSID4Table = _Dot11gTrafficStatisticsByTimeOnSSID4Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 12)
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID4Table.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID4Entry_Object = MibTableRow
dot11gTrafficStatisticsByTimeOnSSID4Entry = _Dot11gTrafficStatisticsByTimeOnSSID4Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 12, 1)
)
dot11gTrafficStatisticsByTimeOnSSID4Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID4Entry.setStatus("mandatory")
_OnSSID4dot11gssociatedMACCount_Type = Integer32
_OnSSID4dot11gssociatedMACCount_Object = MibTableColumn
onSSID4dot11gssociatedMACCount = _OnSSID4dot11gssociatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 12, 1, 2),
    _OnSSID4dot11gssociatedMACCount_Type()
)
onSSID4dot11gssociatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11gssociatedMACCount.setStatus("mandatory")
_OnSSID4dot11gErrorFrameRate_Type = Integer32
_OnSSID4dot11gErrorFrameRate_Object = MibTableColumn
onSSID4dot11gErrorFrameRate = _OnSSID4dot11gErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 12, 1, 3),
    _OnSSID4dot11gErrorFrameRate_Type()
)
onSSID4dot11gErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11gErrorFrameRate.setStatus("mandatory")
_On11gSSID4dot3ErrorFrameRate_Type = Integer32
_On11gSSID4dot3ErrorFrameRate_Object = MibTableColumn
on11gSSID4dot3ErrorFrameRate = _On11gSSID4dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 12, 1, 4),
    _On11gSSID4dot3ErrorFrameRate_Type()
)
on11gSSID4dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID4dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID4dot11gWirelessUsage_Type = Integer32
_OnSSID4dot11gWirelessUsage_Object = MibTableColumn
onSSID4dot11gWirelessUsage = _OnSSID4dot11gWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 5, 12, 1, 5),
    _OnSSID4dot11gWirelessUsage_Type()
)
onSSID4dot11gWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID4dot11gWirelessUsage.setStatus("mandatory")
_TrafficStatisticson11gSSID5_ObjectIdentity = ObjectIdentity
trafficStatisticson11gSSID5 = _TrafficStatisticson11gSSID5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6)
)
_OnSSID5dot11gReceivedByteCount_Type = Integer32
_OnSSID5dot11gReceivedByteCount_Object = MibScalar
onSSID5dot11gReceivedByteCount = _OnSSID5dot11gReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 1),
    _OnSSID5dot11gReceivedByteCount_Type()
)
onSSID5dot11gReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11gReceivedByteCount.setStatus("mandatory")
_OnSSID5dot11gTransmitByteCount_Type = Integer32
_OnSSID5dot11gTransmitByteCount_Object = MibScalar
onSSID5dot11gTransmitByteCount = _OnSSID5dot11gTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 2),
    _OnSSID5dot11gTransmitByteCount_Type()
)
onSSID5dot11gTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11gTransmitByteCount.setStatus("mandatory")
_On11gSSID5dot3ReceivedByteCount_Type = Integer32
_On11gSSID5dot3ReceivedByteCount_Object = MibScalar
on11gSSID5dot3ReceivedByteCount = _On11gSSID5dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 3),
    _On11gSSID5dot3ReceivedByteCount_Type()
)
on11gSSID5dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID5dot3ReceivedByteCount.setStatus("mandatory")
_On11gSSID5dot3TransmitByteCount_Type = Integer32
_On11gSSID5dot3TransmitByteCount_Object = MibScalar
on11gSSID5dot3TransmitByteCount = _On11gSSID5dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 4),
    _On11gSSID5dot3TransmitByteCount_Type()
)
on11gSSID5dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID5dot3TransmitByteCount.setStatus("mandatory")
_OnSSID5dot11gCRCErrorCount_Type = Integer32
_OnSSID5dot11gCRCErrorCount_Object = MibScalar
onSSID5dot11gCRCErrorCount = _OnSSID5dot11gCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 5),
    _OnSSID5dot11gCRCErrorCount_Type()
)
onSSID5dot11gCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11gCRCErrorCount.setStatus("mandatory")
_OnSSID5dot11gPHYErrorCount_Type = Integer32
_OnSSID5dot11gPHYErrorCount_Object = MibScalar
onSSID5dot11gPHYErrorCount = _OnSSID5dot11gPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 6),
    _OnSSID5dot11gPHYErrorCount_Type()
)
onSSID5dot11gPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11gPHYErrorCount.setStatus("mandatory")
_OnSSID5dot11gMICErrorCount_Type = Integer32
_OnSSID5dot11gMICErrorCount_Object = MibScalar
onSSID5dot11gMICErrorCount = _OnSSID5dot11gMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 7),
    _OnSSID5dot11gMICErrorCount_Type()
)
onSSID5dot11gMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11gMICErrorCount.setStatus("mandatory")
_OnSSID5dot11gKEYDecrErrorCount_Type = Integer32
_OnSSID5dot11gKEYDecrErrorCount_Object = MibScalar
onSSID5dot11gKEYDecrErrorCount = _OnSSID5dot11gKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 8),
    _OnSSID5dot11gKEYDecrErrorCount_Type()
)
onSSID5dot11gKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11gKEYDecrErrorCount.setStatus("mandatory")
_On11gSSID5dot3ReceivedPKTCount_Type = Integer32
_On11gSSID5dot3ReceivedPKTCount_Object = MibScalar
on11gSSID5dot3ReceivedPKTCount = _On11gSSID5dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 9),
    _On11gSSID5dot3ReceivedPKTCount_Type()
)
on11gSSID5dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID5dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID5dot11gUserReceivedByteCount_Type = Integer32
_OnSSID5dot11gUserReceivedByteCount_Object = MibScalar
onSSID5dot11gUserReceivedByteCount = _OnSSID5dot11gUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 10),
    _OnSSID5dot11gUserReceivedByteCount_Type()
)
onSSID5dot11gUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11gUserReceivedByteCount.setStatus("mandatory")
_OnSSID5dot11gUserTransmitByteCount_Type = Integer32
_OnSSID5dot11gUserTransmitByteCount_Object = MibScalar
onSSID5dot11gUserTransmitByteCount = _OnSSID5dot11gUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 11),
    _OnSSID5dot11gUserTransmitByteCount_Type()
)
onSSID5dot11gUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11gUserTransmitByteCount.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID5Table_Object = MibTable
dot11gTrafficStatisticsByTimeOnSSID5Table = _Dot11gTrafficStatisticsByTimeOnSSID5Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 12)
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID5Table.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID5Entry_Object = MibTableRow
dot11gTrafficStatisticsByTimeOnSSID5Entry = _Dot11gTrafficStatisticsByTimeOnSSID5Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 12, 1)
)
dot11gTrafficStatisticsByTimeOnSSID5Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID5Entry.setStatus("mandatory")
_OnSSID5dot11gssociatedMACCount_Type = Integer32
_OnSSID5dot11gssociatedMACCount_Object = MibTableColumn
onSSID5dot11gssociatedMACCount = _OnSSID5dot11gssociatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 12, 1, 2),
    _OnSSID5dot11gssociatedMACCount_Type()
)
onSSID5dot11gssociatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11gssociatedMACCount.setStatus("mandatory")
_OnSSID5dot11gErrorFrameRate_Type = Integer32
_OnSSID5dot11gErrorFrameRate_Object = MibTableColumn
onSSID5dot11gErrorFrameRate = _OnSSID5dot11gErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 12, 1, 3),
    _OnSSID5dot11gErrorFrameRate_Type()
)
onSSID5dot11gErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11gErrorFrameRate.setStatus("mandatory")
_On11gSSID5dot3ErrorFrameRate_Type = Integer32
_On11gSSID5dot3ErrorFrameRate_Object = MibTableColumn
on11gSSID5dot3ErrorFrameRate = _On11gSSID5dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 12, 1, 4),
    _On11gSSID5dot3ErrorFrameRate_Type()
)
on11gSSID5dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID5dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID5dot11gWirelessUsage_Type = Integer32
_OnSSID5dot11gWirelessUsage_Object = MibTableColumn
onSSID5dot11gWirelessUsage = _OnSSID5dot11gWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 6, 12, 1, 5),
    _OnSSID5dot11gWirelessUsage_Type()
)
onSSID5dot11gWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID5dot11gWirelessUsage.setStatus("mandatory")
_TrafficStatisticson11gSSID6_ObjectIdentity = ObjectIdentity
trafficStatisticson11gSSID6 = _TrafficStatisticson11gSSID6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7)
)
_OnSSID6dot11gReceivedByteCount_Type = Integer32
_OnSSID6dot11gReceivedByteCount_Object = MibScalar
onSSID6dot11gReceivedByteCount = _OnSSID6dot11gReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 1),
    _OnSSID6dot11gReceivedByteCount_Type()
)
onSSID6dot11gReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11gReceivedByteCount.setStatus("mandatory")
_OnSSID6dot11gTransmitByteCount_Type = Integer32
_OnSSID6dot11gTransmitByteCount_Object = MibScalar
onSSID6dot11gTransmitByteCount = _OnSSID6dot11gTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 2),
    _OnSSID6dot11gTransmitByteCount_Type()
)
onSSID6dot11gTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11gTransmitByteCount.setStatus("mandatory")
_On11gSSID6dot3ReceivedByteCount_Type = Integer32
_On11gSSID6dot3ReceivedByteCount_Object = MibScalar
on11gSSID6dot3ReceivedByteCount = _On11gSSID6dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 3),
    _On11gSSID6dot3ReceivedByteCount_Type()
)
on11gSSID6dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID6dot3ReceivedByteCount.setStatus("mandatory")
_On11gSSID6dot3TransmitByteCount_Type = Integer32
_On11gSSID6dot3TransmitByteCount_Object = MibScalar
on11gSSID6dot3TransmitByteCount = _On11gSSID6dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 4),
    _On11gSSID6dot3TransmitByteCount_Type()
)
on11gSSID6dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID6dot3TransmitByteCount.setStatus("mandatory")
_OnSSID6dot11gCRCErrorCount_Type = Integer32
_OnSSID6dot11gCRCErrorCount_Object = MibScalar
onSSID6dot11gCRCErrorCount = _OnSSID6dot11gCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 5),
    _OnSSID6dot11gCRCErrorCount_Type()
)
onSSID6dot11gCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11gCRCErrorCount.setStatus("mandatory")
_OnSSID6dot11gPHYErrorCount_Type = Integer32
_OnSSID6dot11gPHYErrorCount_Object = MibScalar
onSSID6dot11gPHYErrorCount = _OnSSID6dot11gPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 6),
    _OnSSID6dot11gPHYErrorCount_Type()
)
onSSID6dot11gPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11gPHYErrorCount.setStatus("mandatory")
_OnSSID6dot11gMICErrorCount_Type = Integer32
_OnSSID6dot11gMICErrorCount_Object = MibScalar
onSSID6dot11gMICErrorCount = _OnSSID6dot11gMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 7),
    _OnSSID6dot11gMICErrorCount_Type()
)
onSSID6dot11gMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11gMICErrorCount.setStatus("mandatory")
_OnSSID6dot11gKEYDecrErrorCount_Type = Integer32
_OnSSID6dot11gKEYDecrErrorCount_Object = MibScalar
onSSID6dot11gKEYDecrErrorCount = _OnSSID6dot11gKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 8),
    _OnSSID6dot11gKEYDecrErrorCount_Type()
)
onSSID6dot11gKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11gKEYDecrErrorCount.setStatus("mandatory")
_On11gSSID6dot3ReceivedPKTCount_Type = Integer32
_On11gSSID6dot3ReceivedPKTCount_Object = MibScalar
on11gSSID6dot3ReceivedPKTCount = _On11gSSID6dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 9),
    _On11gSSID6dot3ReceivedPKTCount_Type()
)
on11gSSID6dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID6dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID6dot11gUserReceivedByteCount_Type = Integer32
_OnSSID6dot11gUserReceivedByteCount_Object = MibScalar
onSSID6dot11gUserReceivedByteCount = _OnSSID6dot11gUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 10),
    _OnSSID6dot11gUserReceivedByteCount_Type()
)
onSSID6dot11gUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11gUserReceivedByteCount.setStatus("mandatory")
_OnSSID6dot11gUserTransmitByteCount_Type = Integer32
_OnSSID6dot11gUserTransmitByteCount_Object = MibScalar
onSSID6dot11gUserTransmitByteCount = _OnSSID6dot11gUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 11),
    _OnSSID6dot11gUserTransmitByteCount_Type()
)
onSSID6dot11gUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11gUserTransmitByteCount.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID6Table_Object = MibTable
dot11gTrafficStatisticsByTimeOnSSID6Table = _Dot11gTrafficStatisticsByTimeOnSSID6Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 12)
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID6Table.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID6Entry_Object = MibTableRow
dot11gTrafficStatisticsByTimeOnSSID6Entry = _Dot11gTrafficStatisticsByTimeOnSSID6Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 12, 1)
)
dot11gTrafficStatisticsByTimeOnSSID6Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID6Entry.setStatus("mandatory")
_OnSSID6dot11gssociatedMACCount_Type = Integer32
_OnSSID6dot11gssociatedMACCount_Object = MibTableColumn
onSSID6dot11gssociatedMACCount = _OnSSID6dot11gssociatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 12, 1, 2),
    _OnSSID6dot11gssociatedMACCount_Type()
)
onSSID6dot11gssociatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11gssociatedMACCount.setStatus("mandatory")
_OnSSID6dot11gErrorFrameRate_Type = Integer32
_OnSSID6dot11gErrorFrameRate_Object = MibTableColumn
onSSID6dot11gErrorFrameRate = _OnSSID6dot11gErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 12, 1, 3),
    _OnSSID6dot11gErrorFrameRate_Type()
)
onSSID6dot11gErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11gErrorFrameRate.setStatus("mandatory")
_On11gSSID6dot3ErrorFrameRate_Type = Integer32
_On11gSSID6dot3ErrorFrameRate_Object = MibTableColumn
on11gSSID6dot3ErrorFrameRate = _On11gSSID6dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 12, 1, 4),
    _On11gSSID6dot3ErrorFrameRate_Type()
)
on11gSSID6dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID6dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID6dot11gWirelessUsage_Type = Integer32
_OnSSID6dot11gWirelessUsage_Object = MibTableColumn
onSSID6dot11gWirelessUsage = _OnSSID6dot11gWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 7, 12, 1, 5),
    _OnSSID6dot11gWirelessUsage_Type()
)
onSSID6dot11gWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID6dot11gWirelessUsage.setStatus("mandatory")
_TrafficStatisticson11gSSID7_ObjectIdentity = ObjectIdentity
trafficStatisticson11gSSID7 = _TrafficStatisticson11gSSID7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8)
)
_OnSSID7dot11gReceivedByteCount_Type = Integer32
_OnSSID7dot11gReceivedByteCount_Object = MibScalar
onSSID7dot11gReceivedByteCount = _OnSSID7dot11gReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 1),
    _OnSSID7dot11gReceivedByteCount_Type()
)
onSSID7dot11gReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11gReceivedByteCount.setStatus("mandatory")
_OnSSID7dot11gTransmitByteCount_Type = Integer32
_OnSSID7dot11gTransmitByteCount_Object = MibScalar
onSSID7dot11gTransmitByteCount = _OnSSID7dot11gTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 2),
    _OnSSID7dot11gTransmitByteCount_Type()
)
onSSID7dot11gTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11gTransmitByteCount.setStatus("mandatory")
_On11gSSID7dot3ReceivedByteCount_Type = Integer32
_On11gSSID7dot3ReceivedByteCount_Object = MibScalar
on11gSSID7dot3ReceivedByteCount = _On11gSSID7dot3ReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 3),
    _On11gSSID7dot3ReceivedByteCount_Type()
)
on11gSSID7dot3ReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID7dot3ReceivedByteCount.setStatus("mandatory")
_On11gSSID7dot3TransmitByteCount_Type = Integer32
_On11gSSID7dot3TransmitByteCount_Object = MibScalar
on11gSSID7dot3TransmitByteCount = _On11gSSID7dot3TransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 4),
    _On11gSSID7dot3TransmitByteCount_Type()
)
on11gSSID7dot3TransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID7dot3TransmitByteCount.setStatus("mandatory")
_OnSSID7dot11gCRCErrorCount_Type = Integer32
_OnSSID7dot11gCRCErrorCount_Object = MibScalar
onSSID7dot11gCRCErrorCount = _OnSSID7dot11gCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 5),
    _OnSSID7dot11gCRCErrorCount_Type()
)
onSSID7dot11gCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11gCRCErrorCount.setStatus("mandatory")
_OnSSID7dot11gPHYErrorCount_Type = Integer32
_OnSSID7dot11gPHYErrorCount_Object = MibScalar
onSSID7dot11gPHYErrorCount = _OnSSID7dot11gPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 6),
    _OnSSID7dot11gPHYErrorCount_Type()
)
onSSID7dot11gPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11gPHYErrorCount.setStatus("mandatory")
_OnSSID7dot11gMICErrorCount_Type = Integer32
_OnSSID7dot11gMICErrorCount_Object = MibScalar
onSSID7dot11gMICErrorCount = _OnSSID7dot11gMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 7),
    _OnSSID7dot11gMICErrorCount_Type()
)
onSSID7dot11gMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11gMICErrorCount.setStatus("mandatory")
_OnSSID7dot11gKEYDecrErrorCount_Type = Integer32
_OnSSID7dot11gKEYDecrErrorCount_Object = MibScalar
onSSID7dot11gKEYDecrErrorCount = _OnSSID7dot11gKEYDecrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 8),
    _OnSSID7dot11gKEYDecrErrorCount_Type()
)
onSSID7dot11gKEYDecrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11gKEYDecrErrorCount.setStatus("mandatory")
_On11gSSID7dot3ReceivedPKTCount_Type = Integer32
_On11gSSID7dot3ReceivedPKTCount_Object = MibScalar
on11gSSID7dot3ReceivedPKTCount = _On11gSSID7dot3ReceivedPKTCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 9),
    _On11gSSID7dot3ReceivedPKTCount_Type()
)
on11gSSID7dot3ReceivedPKTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID7dot3ReceivedPKTCount.setStatus("mandatory")
_OnSSID7dot11gUserReceivedByteCount_Type = Integer32
_OnSSID7dot11gUserReceivedByteCount_Object = MibScalar
onSSID7dot11gUserReceivedByteCount = _OnSSID7dot11gUserReceivedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 10),
    _OnSSID7dot11gUserReceivedByteCount_Type()
)
onSSID7dot11gUserReceivedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11gUserReceivedByteCount.setStatus("mandatory")
_OnSSID7dot11gUserTransmitByteCount_Type = Integer32
_OnSSID7dot11gUserTransmitByteCount_Object = MibScalar
onSSID7dot11gUserTransmitByteCount = _OnSSID7dot11gUserTransmitByteCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 11),
    _OnSSID7dot11gUserTransmitByteCount_Type()
)
onSSID7dot11gUserTransmitByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11gUserTransmitByteCount.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID7Table_Object = MibTable
dot11gTrafficStatisticsByTimeOnSSID7Table = _Dot11gTrafficStatisticsByTimeOnSSID7Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 12)
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID7Table.setStatus("mandatory")
_Dot11gTrafficStatisticsByTimeOnSSID7Entry_Object = MibTableRow
dot11gTrafficStatisticsByTimeOnSSID7Entry = _Dot11gTrafficStatisticsByTimeOnSSID7Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 12, 1)
)
dot11gTrafficStatisticsByTimeOnSSID7Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11gTrafficStatisticsByTimeOnSSID7Entry.setStatus("mandatory")
_OnSSID7dot11gssociatedMACCount_Type = Integer32
_OnSSID7dot11gssociatedMACCount_Object = MibTableColumn
onSSID7dot11gssociatedMACCount = _OnSSID7dot11gssociatedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 12, 1, 2),
    _OnSSID7dot11gssociatedMACCount_Type()
)
onSSID7dot11gssociatedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11gssociatedMACCount.setStatus("mandatory")
_OnSSID7dot11gErrorFrameRate_Type = Integer32
_OnSSID7dot11gErrorFrameRate_Object = MibTableColumn
onSSID7dot11gErrorFrameRate = _OnSSID7dot11gErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 12, 1, 3),
    _OnSSID7dot11gErrorFrameRate_Type()
)
onSSID7dot11gErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11gErrorFrameRate.setStatus("mandatory")
_On11gSSID7dot3ErrorFrameRate_Type = Integer32
_On11gSSID7dot3ErrorFrameRate_Object = MibTableColumn
on11gSSID7dot3ErrorFrameRate = _On11gSSID7dot3ErrorFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 12, 1, 4),
    _On11gSSID7dot3ErrorFrameRate_Type()
)
on11gSSID7dot3ErrorFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on11gSSID7dot3ErrorFrameRate.setStatus("mandatory")
_OnSSID7dot11gWirelessUsage_Type = Integer32
_OnSSID7dot11gWirelessUsage_Object = MibTableColumn
onSSID7dot11gWirelessUsage = _OnSSID7dot11gWirelessUsage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 2, 2, 5, 8, 12, 1, 5),
    _OnSSID7dot11gWirelessUsage_Type()
)
onSSID7dot11gWirelessUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onSSID7dot11gWirelessUsage.setStatus("mandatory")
_SystemLog_ObjectIdentity = ObjectIdentity
systemLog = _SystemLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 4)
)


class _SystemLogSystemLevel_Type(Integer32):
    """Custom type systemLogSystemLevel based on Integer32"""
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


_SystemLogSystemLevel_Type.__name__ = "Integer32"
_SystemLogSystemLevel_Object = MibScalar
systemLogSystemLevel = _SystemLogSystemLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 4, 1),
    _SystemLogSystemLevel_Type()
)
systemLogSystemLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogSystemLevel.setStatus("mandatory")


class _SystemLogWirelessLevel_Type(Integer32):
    """Custom type systemLogWirelessLevel based on Integer32"""
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


_SystemLogWirelessLevel_Type.__name__ = "Integer32"
_SystemLogWirelessLevel_Object = MibScalar
systemLogWirelessLevel = _SystemLogWirelessLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 4, 2),
    _SystemLogWirelessLevel_Type()
)
systemLogWirelessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogWirelessLevel.setStatus("mandatory")


class _SystemLogNoticeLevel_Type(Integer32):
    """Custom type systemLogNoticeLevel based on Integer32"""
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


_SystemLogNoticeLevel_Type.__name__ = "Integer32"
_SystemLogNoticeLevel_Object = MibScalar
systemLogNoticeLevel = _SystemLogNoticeLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 4, 3),
    _SystemLogNoticeLevel_Type()
)
systemLogNoticeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogNoticeLevel.setStatus("mandatory")
_SystemLogTFTPServerIPAddress_Type = IpAddress
_SystemLogTFTPServerIPAddress_Object = MibScalar
systemLogTFTPServerIPAddress = _SystemLogTFTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 4, 4),
    _SystemLogTFTPServerIPAddress_Type()
)
systemLogTFTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogTFTPServerIPAddress.setStatus("mandatory")
_SystemLogFileName_Type = OctetString
_SystemLogFileName_Object = MibScalar
systemLogFileName = _SystemLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 4, 5),
    _SystemLogFileName_Type()
)
systemLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogFileName.setStatus("mandatory")


class _SystemLogGetLog_Type(Integer32):
    """Custom type systemLogGetLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("nothing", 0))
    )


_SystemLogGetLog_Type.__name__ = "Integer32"
_SystemLogGetLog_Object = MibScalar
systemLogGetLog = _SystemLogGetLog_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 4, 6),
    _SystemLogGetLog_Type()
)
systemLogGetLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogGetLog.setStatus("mandatory")


class _SystemLogLocalLogState_Type(Integer32):
    """Custom type systemLogLocalLogState based on Integer32"""
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


_SystemLogLocalLogState_Type.__name__ = "Integer32"
_SystemLogLocalLogState_Object = MibScalar
systemLogLocalLogState = _SystemLogLocalLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 4, 7),
    _SystemLogLocalLogState_Type()
)
systemLogLocalLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogLocalLogState.setStatus("mandatory")


class _SystemLogRemoteLogState_Type(Integer32):
    """Custom type systemLogRemoteLogState based on Integer32"""
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


_SystemLogRemoteLogState_Type.__name__ = "Integer32"
_SystemLogRemoteLogState_Object = MibScalar
systemLogRemoteLogState = _SystemLogRemoteLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 4, 8),
    _SystemLogRemoteLogState_Type()
)
systemLogRemoteLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogRemoteLogState.setStatus("mandatory")
_SystemLogServerIPAddress_Type = IpAddress
_SystemLogServerIPAddress_Object = MibScalar
systemLogServerIPAddress = _SystemLogServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 4, 9),
    _SystemLogServerIPAddress_Type()
)
systemLogServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogServerIPAddress.setStatus("mandatory")


class _SystemLogClearLocalLog_Type(Integer32):
    """Custom type systemLogClearLocalLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 0))
    )


_SystemLogClearLocalLog_Type.__name__ = "Integer32"
_SystemLogClearLocalLog_Object = MibScalar
systemLogClearLocalLog = _SystemLogClearLocalLog_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 4, 10),
    _SystemLogClearLocalLog_Type()
)
systemLogClearLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogClearLocalLog.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7)
)
_TrapsNotify_ObjectIdentity = ObjectIdentity
trapsNotify = _TrapsNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1)
)
_TrapsNotifyBiding_ObjectIdentity = ObjectIdentity
trapsNotifyBiding = _TrapsNotifyBiding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 2)
)
_TrapAPMACaddr_Type = MacAddress
_TrapAPMACaddr_Object = MibScalar
trapAPMACaddr = _TrapAPMACaddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 2, 1),
    _TrapAPMACaddr_Type()
)
trapAPMACaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAPMACaddr.setStatus("mandatory")
_TrapSTAMACaddr_Type = MacAddress
_TrapSTAMACaddr_Object = MibScalar
trapSTAMACaddr = _TrapSTAMACaddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 2, 2),
    _TrapSTAMACaddr_Type()
)
trapSTAMACaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSTAMACaddr.setStatus("mandatory")


class _TrapAlarmLevel_Type(Integer32):
    """Custom type trapAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("wlan", 2))
    )


_TrapAlarmLevel_Type.__name__ = "Integer32"
_TrapAlarmLevel_Object = MibScalar
trapAlarmLevel = _TrapAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 2, 3),
    _TrapAlarmLevel_Type()
)
trapAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLevel.setStatus("mandatory")
_TrapPCIPAddr_Type = IpAddress
_TrapPCIPAddr_Object = MibScalar
trapPCIPAddr = _TrapPCIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 2, 4),
    _TrapPCIPAddr_Type()
)
trapPCIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPCIPAddr.setStatus("mandatory")


class _SwNotiResult_Type(Integer32):
    """Custom type swNotiResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("success", 1))
    )


_SwNotiResult_Type.__name__ = "Integer32"
_SwNotiResult_Object = MibScalar
swNotiResult = _SwNotiResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 2, 5),
    _SwNotiResult_Type()
)
swNotiResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNotiResult.setStatus("mandatory")


class _TrapBand_Type(Integer32):
    """Custom type trapBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wlan0", 0),
          ("wlan1", 1))
    )


_TrapBand_Type.__name__ = "Integer32"
_TrapBand_Object = MibScalar
trapBand = _TrapBand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 2, 6),
    _TrapBand_Type()
)
trapBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapBand.setStatus("mandatory")
_Miscellaneous_ObjectIdentity = ObjectIdentity
miscellaneous = _Miscellaneous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6)
)
_Compatible_ObjectIdentity = ObjectIdentity
compatible = _Compatible_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1)
)
_CompatibleTable_Object = MibTable
compatibleTable = _CompatibleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1)
)
if mibBuilder.loadTexts:
    compatibleTable.setStatus("mandatory")
_CompatibleEntry_Object = MibTableRow
compatibleEntry = _CompatibleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1)
)
compatibleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    compatibleEntry.setStatus("mandatory")
_Apmodes_Type = Integer32
_Apmodes_Object = MibTableColumn
apmodes = _Apmodes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 1),
    _Apmodes_Type()
)
apmodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmodes.setStatus("mandatory")


class _Turbomodes_Type(Integer32):
    """Custom type turbomodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allTurbo", 1),
          ("noTurbo", 0),
          ("onlyDynamic", 2))
    )


_Turbomodes_Type.__name__ = "Integer32"
_Turbomodes_Object = MibTableColumn
turbomodes = _Turbomodes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 2),
    _Turbomodes_Type()
)
turbomodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turbomodes.setStatus("mandatory")
_Aclnumber_Type = Integer32
_Aclnumber_Object = MibTableColumn
aclnumber = _Aclnumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 3),
    _Aclnumber_Type()
)
aclnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclnumber.setStatus("mandatory")
_Xrsupported_Type = Integer32
_Xrsupported_Object = MibTableColumn
xrsupported = _Xrsupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 4),
    _Xrsupported_Type()
)
xrsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xrsupported.setStatus("mandatory")


class _Codebase_Type(OctetString):
    """Custom type codebase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Codebase_Type.__name__ = "OctetString"
_Codebase_Object = MibTableColumn
codebase = _Codebase_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 5),
    _Codebase_Type()
)
codebase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codebase.setStatus("mandatory")


class _Countrycode_Type(OctetString):
    """Custom type countrycode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Countrycode_Type.__name__ = "OctetString"
_Countrycode_Object = MibTableColumn
countrycode = _Countrycode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 6),
    _Countrycode_Type()
)
countrycode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countrycode.setStatus("mandatory")
_Clientinfosupported_Type = Integer32
_Clientinfosupported_Object = MibTableColumn
clientinfosupported = _Clientinfosupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 7),
    _Clientinfosupported_Type()
)
clientinfosupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientinfosupported.setStatus("mandatory")
_Singlefirmware_Type = Integer32
_Singlefirmware_Object = MibTableColumn
singlefirmware = _Singlefirmware_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 8),
    _Singlefirmware_Type()
)
singlefirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    singlefirmware.setStatus("mandatory")
_Mssidsupported_Type = Integer32
_Mssidsupported_Object = MibTableColumn
mssidsupported = _Mssidsupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 9),
    _Mssidsupported_Type()
)
mssidsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssidsupported.setStatus("mandatory")
_Rogueapsupported_Type = Integer32
_Rogueapsupported_Object = MibTableColumn
rogueapsupported = _Rogueapsupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 10),
    _Rogueapsupported_Type()
)
rogueapsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueapsupported.setStatus("mandatory")
_Syslogsupported_Type = Integer32
_Syslogsupported_Object = MibTableColumn
syslogsupported = _Syslogsupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 11),
    _Syslogsupported_Type()
)
syslogsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogsupported.setStatus("mandatory")
_Wmmsupported_Type = Integer32
_Wmmsupported_Object = MibTableColumn
wmmsupported = _Wmmsupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 12),
    _Wmmsupported_Type()
)
wmmsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmmsupported.setStatus("mandatory")
_Mssidisolatedsecurity_Type = Integer32
_Mssidisolatedsecurity_Object = MibTableColumn
mssidisolatedsecurity = _Mssidisolatedsecurity_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 13),
    _Mssidisolatedsecurity_Type()
)
mssidisolatedsecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssidisolatedsecurity.setStatus("mandatory")
_Mssidindication_Type = Integer32
_Mssidindication_Object = MibTableColumn
mssidindication = _Mssidindication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 14),
    _Mssidindication_Type()
)
mssidindication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssidindication.setStatus("mandatory")
_Keytypeselection_Type = Integer32
_Keytypeselection_Object = MibTableColumn
keytypeselection = _Keytypeselection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 15),
    _Keytypeselection_Type()
)
keytypeselection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keytypeselection.setStatus("mandatory")
_Clustersupported_Type = Integer32
_Clustersupported_Object = MibTableColumn
clustersupported = _Clustersupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 16),
    _Clustersupported_Type()
)
clustersupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clustersupported.setStatus("mandatory")
_Greenpacketsupported_Type = Integer32
_Greenpacketsupported_Object = MibTableColumn
greenpacketsupported = _Greenpacketsupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 17),
    _Greenpacketsupported_Type()
)
greenpacketsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greenpacketsupported.setStatus("mandatory")
_Sshsupported_Type = Integer32
_Sshsupported_Object = MibTableColumn
sshsupported = _Sshsupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 18),
    _Sshsupported_Type()
)
sshsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshsupported.setStatus("mandatory")
_Wdschannellist_Type = Integer32
_Wdschannellist_Object = MibTableColumn
wdschannellist = _Wdschannellist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 19),
    _Wdschannellist_Type()
)
wdschannellist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdschannellist.setStatus("mandatory")
_MSSIDSuppress_Type = Integer32
_MSSIDSuppress_Object = MibTableColumn
mSSIDSuppress = _MSSIDSuppress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 20),
    _MSSIDSuppress_Type()
)
mSSIDSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSSIDSuppress.setStatus("mandatory")
_Antennasupported_Type = Integer32
_Antennasupported_Object = MibTableColumn
antennasupported = _Antennasupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 21),
    _Antennasupported_Type()
)
antennasupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennasupported.setStatus("mandatory")
_Vlan_Type = Integer32
_Vlan_Object = MibTableColumn
vlan = _Vlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 22),
    _Vlan_Type()
)
vlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlan.setStatus("mandatory")
_Bgmodesupported_Type = Integer32
_Bgmodesupported_Object = MibTableColumn
bgmodesupported = _Bgmodesupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 23),
    _Bgmodesupported_Type()
)
bgmodesupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgmodesupported.setStatus("mandatory")
_Wdssitesurvey_Type = Integer32
_Wdssitesurvey_Object = MibTableColumn
wdssitesurvey = _Wdssitesurvey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 24),
    _Wdssitesurvey_Type()
)
wdssitesurvey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdssitesurvey.setStatus("mandatory")
_Accounting_Type = Integer32
_Accounting_Object = MibTableColumn
accounting = _Accounting_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 26),
    _Accounting_Type()
)
accounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accounting.setStatus("mandatory")
_Mssidaccounting_Type = Integer32
_Mssidaccounting_Object = MibTableColumn
mssidaccounting = _Mssidaccounting_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 27),
    _Mssidaccounting_Type()
)
mssidaccounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssidaccounting.setStatus("mandatory")
_MSSIDWmmSupported_Type = Integer32
_MSSIDWmmSupported_Object = MibTableColumn
mSSIDWmmSupported = _MSSIDWmmSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 31),
    _MSSIDWmmSupported_Type()
)
mSSIDWmmSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSSIDWmmSupported.setStatus("mandatory")
_SMTPSupported_Type = Integer32
_SMTPSupported_Object = MibTableColumn
sMTPSupported = _SMTPSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 32),
    _SMTPSupported_Type()
)
sMTPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sMTPSupported.setStatus("mandatory")
_DfsSupported_Type = Integer32
_DfsSupported_Object = MibTableColumn
dfsSupported = _DfsSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 38),
    _DfsSupported_Type()
)
dfsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsSupported.setStatus("mandatory")
_WmmOverWDSSupported_Type = Integer32
_WmmOverWDSSupported_Object = MibTableColumn
wmmOverWDSSupported = _WmmOverWDSSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 42),
    _WmmOverWDSSupported_Type()
)
wmmOverWDSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmmOverWDSSupported.setStatus("mandatory")
_PriorityBySsidSupported_Type = Integer32
_PriorityBySsidSupported_Object = MibTableColumn
priorityBySsidSupported = _PriorityBySsidSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 6, 1, 1, 1, 43),
    _PriorityBySsidSupported_Type()
)
priorityBySsidSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priorityBySsidSupported.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapSSHLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 1)
)
trapSSHLogin.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"),
        ("DWL-3200", "trapPCIPAddr"),
        ("DWL-3200", "swNotiResult"))
)
if mibBuilder.loadTexts:
    trapSSHLogin.setStatus(
        "current"
    )

trapWebLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 2)
)
trapWebLogin.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"),
        ("DWL-3200", "trapPCIPAddr"),
        ("DWL-3200", "swNotiResult"))
)
if mibBuilder.loadTexts:
    trapWebLogin.setStatus(
        "current"
    )

trapTelLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 3)
)
trapTelLogin.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"),
        ("DWL-3200", "trapPCIPAddr"),
        ("DWL-3200", "swNotiResult"))
)
if mibBuilder.loadTexts:
    trapTelLogin.setStatus(
        "current"
    )

trapCPULoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 4)
)
trapCPULoad.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"))
)
if mibBuilder.loadTexts:
    trapCPULoad.setStatus(
        "current"
    )

trapMEMPoor = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 5)
)
trapMEMPoor.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"))
)
if mibBuilder.loadTexts:
    trapMEMPoor.setStatus(
        "current"
    )

trapAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 6)
)
trapAuthFail.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"),
        ("DWL-3200", "trapSTAMACaddr"))
)
if mibBuilder.loadTexts:
    trapAuthFail.setStatus(
        "current"
    )

trapWirelessLinkUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 7)
)
trapWirelessLinkUP.setObjects(
      *(("DWL-3200", "trapAlarmLevel"),
        ("DWL-3200", "trapBand"))
)
if mibBuilder.loadTexts:
    trapWirelessLinkUP.setStatus(
        "current"
    )

trapDeAuthAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 8)
)
trapDeAuthAttack.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"))
)
if mibBuilder.loadTexts:
    trapDeAuthAttack.setStatus(
        "current"
    )

trapDeAssocAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 9)
)
trapDeAssocAttack.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"))
)
if mibBuilder.loadTexts:
    trapDeAssocAttack.setStatus(
        "current"
    )

trapBCastAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 10)
)
trapBCastAttack.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"))
)
if mibBuilder.loadTexts:
    trapBCastAttack.setStatus(
        "current"
    )

trapWebLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 11)
)
trapWebLogout.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"),
        ("DWL-3200", "trapPCIPAddr"),
        ("DWL-3200", "swNotiResult"))
)
if mibBuilder.loadTexts:
    trapWebLogout.setStatus(
        "current"
    )

trapFWUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 12)
)
trapFWUpdate.setObjects(
    ("DWL-3200", "swNotiResult")
)
if mibBuilder.loadTexts:
    trapFWUpdate.setStatus(
        "current"
    )

trapWirelessLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 13)
)
trapWirelessLinkDown.setObjects(
      *(("DWL-3200", "trapAlarmLevel"),
        ("DWL-3200", "trapBand"))
)
if mibBuilder.loadTexts:
    trapWirelessLinkDown.setStatus(
        "current"
    )

trapSTALinkUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 14)
)
trapSTALinkUP.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"),
        ("DWL-3200", "trapSTAMACaddr"),
        ("DWL-3200", "swNotiResult"))
)
if mibBuilder.loadTexts:
    trapSTALinkUP.setStatus(
        "current"
    )

trapSTALinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 20, 5, 7, 1, 15)
)
trapSTALinkDown.setObjects(
      *(("DWL-3200", "trapAPMACaddr"),
        ("DWL-3200", "trapAlarmLevel"),
        ("DWL-3200", "trapSTAMACaddr"),
        ("DWL-3200", "swNotiResult"))
)
if mibBuilder.loadTexts:
    trapSTALinkDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DWL-3200",
    **{"DisplayString": DisplayString,
       "enterprises": enterprises,
       "dlink": dlink,
       "dlink-products": dlink_products,
       "dlink-dwlfamily": dlink_dwlfamily,
       "dwl-3200AP": dwl_3200AP,
       "systemInformation": systemInformation,
       "systemDescr": systemDescr,
       "systemUpTime": systemUpTime,
       "systemContact": systemContact,
       "systemLocation": systemLocation,
       "systemModelName": systemModelName,
       "systemFirmwareVersion": systemFirmwareVersion,
       "systemIpAddress": systemIpAddress,
       "systemTime": systemTime,
       "interface": interface,
       "lan": lan,
       "lanIfSetting": lanIfSetting,
       "lanIfSettingTable": lanIfSettingTable,
       "lanIfSettingEntry": lanIfSettingEntry,
       "lanIfGetIpAddressFrom": lanIfGetIpAddressFrom,
       "lanIfIpAddress": lanIfIpAddress,
       "lanIfSubnetMask": lanIfSubnetMask,
       "lanIfDefaultGateway": lanIfDefaultGateway,
       "lanIfMacAddress": lanIfMacAddress,
       "wirelesslan": wirelesslan,
       "wirelessLanIfNumber": wirelessLanIfNumber,
       "ieee802dot11": ieee802dot11,
       "dot11Parameters": dot11Parameters,
       "dot11ParametersTable": dot11ParametersTable,
       "dot11ParametersEntry": dot11ParametersEntry,
       "dot11Ssid": dot11Ssid,
       "dot11SsidBroadcast": dot11SsidBroadcast,
       "dot11Channel": dot11Channel,
       "dot11ChannelList": dot11ChannelList,
       "dot11DynamicChannelList": dot11DynamicChannelList,
       "dot11WdsChannelList": dot11WdsChannelList,
       "dot11WdsDynamicChannelList": dot11WdsDynamicChannelList,
       "dot11Frequency": dot11Frequency,
       "dot11DataRate": dot11DataRate,
       "dot11bModeDataRateList": dot11bModeDataRateList,
       "dot11gModeDataRateList": dot11gModeDataRateList,
       "dot11WifiMode": dot11WifiMode,
       "dot11BeaconInterval": dot11BeaconInterval,
       "dot11Dtim": dot11Dtim,
       "dot11FragmentLength": dot11FragmentLength,
       "dot11RtsLength": dot11RtsLength,
       "dot11TransmitPower": dot11TransmitPower,
       "dot11SuperMode": dot11SuperMode,
       "dot11RadioWave": dot11RadioWave,
       "dot11AutoChannelScan": dot11AutoChannelScan,
       "dot11Wmm": dot11Wmm,
       "dot11Preamble": dot11Preamble,
       "dot11Antenna": dot11Antenna,
       "dot11ApMode": dot11ApMode,
       "dot11IgmpSnooping": dot11IgmpSnooping,
       "dot11RemoteApMacAddressTable": dot11RemoteApMacAddressTable,
       "dot11RemoteApMacAddressEntry": dot11RemoteApMacAddressEntry,
       "dot11RemoteApMacAddressIndex": dot11RemoteApMacAddressIndex,
       "dot11RemoteApMacAddress": dot11RemoteApMacAddress,
       "dot11SiteSurvey": dot11SiteSurvey,
       "dot11SiteSurveyRefreshTable": dot11SiteSurveyRefreshTable,
       "dot11SiteSurveyRefreshEntry": dot11SiteSurveyRefreshEntry,
       "dot11SiteSurveyRefresh": dot11SiteSurveyRefresh,
       "dot11SiteSurveyTable": dot11SiteSurveyTable,
       "dot11SiteSurveyEntry": dot11SiteSurveyEntry,
       "dot11SiteSurveyIndex": dot11SiteSurveyIndex,
       "dot11SiteSurveyBssType": dot11SiteSurveyBssType,
       "dot11SiteSurveyChannel": dot11SiteSurveyChannel,
       "dot11SiteSurveyRssi": dot11SiteSurveyRssi,
       "dot11SiteSurveyBssid": dot11SiteSurveyBssid,
       "dot11SiteSurveyEncryption": dot11SiteSurveyEncryption,
       "dot11SiteSurveySsid": dot11SiteSurveySsid,
       "dot11SiteSurveyWirelessMode": dot11SiteSurveyWirelessMode,
       "dot11SiteSurveySupportWds": dot11SiteSurveySupportWds,
       "dot11Securities": dot11Securities,
       "dot11SecuritiesTable": dot11SecuritiesTable,
       "dot11SecuritiesEntry": dot11SecuritiesEntry,
       "dot11Authentication": dot11Authentication,
       "dot11Encryption": dot11Encryption,
       "dot11KeyIndex": dot11KeyIndex,
       "dot11PassPhrase": dot11PassPhrase,
       "dot11CipherType": dot11CipherType,
       "dot11GroupKeyUpdateInterval": dot11GroupKeyUpdateInterval,
       "dot11KeyEntryMethod": dot11KeyEntryMethod,
       "dot11RadiusServer": dot11RadiusServer,
       "dot11RadiusPort": dot11RadiusPort,
       "dot11RadiusSecret": dot11RadiusSecret,
       "dot11SecRADIUSServer": dot11SecRADIUSServer,
       "dot11SecRADIUSPort": dot11SecRADIUSPort,
       "dot11SecRADIUSSecret": dot11SecRADIUSSecret,
       "dot11SecRADIUSStatus": dot11SecRADIUSStatus,
       "dot11WepKeyTable": dot11WepKeyTable,
       "dot11WepKeyEntry": dot11WepKeyEntry,
       "dot11wepKeyIndex": dot11wepKeyIndex,
       "dot11WepKey": dot11WepKey,
       "dot11Filter": dot11Filter,
       "dot11PartionTable": dot11PartionTable,
       "dot11LanPartionEntry": dot11LanPartionEntry,
       "dot11InternalStationConnection": dot11InternalStationConnection,
       "dot11EthernetToWlanAccess": dot11EthernetToWlanAccess,
       "dot11MacAccessControlTable": dot11MacAccessControlTable,
       "dot11MacAccessControlEntry": dot11MacAccessControlEntry,
       "dot11MacAccessControl": dot11MacAccessControl,
       "dot11MacAccessControlListTable": dot11MacAccessControlListTable,
       "dot11MacAccessControlListEntry": dot11MacAccessControlListEntry,
       "dot11MacAccessControlListIndex": dot11MacAccessControlListIndex,
       "dot11MacAccessControlListMacAddress": dot11MacAccessControlListMacAddress,
       "dot11Accounting": dot11Accounting,
       "dot11AccountingTable": dot11AccountingTable,
       "dot11AccountingEntry": dot11AccountingEntry,
       "dot11AccountingStatus": dot11AccountingStatus,
       "dot11AccountingServer": dot11AccountingServer,
       "dot11AccountingServerPort": dot11AccountingServerPort,
       "dot11SecAccountingTable": dot11SecAccountingTable,
       "dot11SecAccountingEntry": dot11SecAccountingEntry,
       "dot11SecAccountingStatus": dot11SecAccountingStatus,
       "dot11SecAccountingServer": dot11SecAccountingServer,
       "dot11SecAccountingServerPort": dot11SecAccountingServerPort,
       "dot11ClientInformation": dot11ClientInformation,
       "dot11GetClientInformationTable": dot11GetClientInformationTable,
       "dot11GetClientInformationEntry": dot11GetClientInformationEntry,
       "dot11ClientInformationRefresh": dot11ClientInformationRefresh,
       "dot11ClientInformationAssNum": dot11ClientInformationAssNum,
       "dot11ClientInformationTable": dot11ClientInformationTable,
       "dot11ClientInformationEntry": dot11ClientInformationEntry,
       "dot11ClinetIndex": dot11ClinetIndex,
       "dot11ClientMacAddress": dot11ClientMacAddress,
       "dot11ClientBand": dot11ClientBand,
       "dot11ClientAuthentication": dot11ClientAuthentication,
       "dot11ClientRssi": dot11ClientRssi,
       "dot11ClientPsm": dot11ClientPsm,
       "dot11SSIDIndex": dot11SSIDIndex,
       "dot11ClientKickOff": dot11ClientKickOff,
       "dot11KickOffClientMacAddress": dot11KickOffClientMacAddress,
       "dot11KickOff": dot11KickOff,
       "advance": advance,
       "dhcpServer": dhcpServer,
       "dhcpServerControl": dhcpServerControl,
       "dhcpServerDynamicTable": dhcpServerDynamicTable,
       "dynamicIpPoolStart": dynamicIpPoolStart,
       "dynamicIpPoolRange": dynamicIpPoolRange,
       "dynamicMask": dynamicMask,
       "dynamicGateway": dynamicGateway,
       "dynamicWins": dynamicWins,
       "dynamicDns": dynamicDns,
       "dynamicDomainName": dynamicDomainName,
       "dynamicLeaseTime": dynamicLeaseTime,
       "dynamicFunction": dynamicFunction,
       "dhcpServerStaticTable": dhcpServerStaticTable,
       "dhcpServerStaticEntry": dhcpServerStaticEntry,
       "staticIndex": staticIndex,
       "staticIP": staticIP,
       "staticMac": staticMac,
       "staticMask": staticMask,
       "staticGateway": staticGateway,
       "staticDns": staticDns,
       "staticWins": staticWins,
       "staticDomainName": staticDomainName,
       "staticStatus": staticStatus,
       "dhcpServerCurrentListTable": dhcpServerCurrentListTable,
       "currentDynamicTable": currentDynamicTable,
       "currentDynamicEntry": currentDynamicEntry,
       "currentDynamicIndex": currentDynamicIndex,
       "currentDynamicMacAddress": currentDynamicMacAddress,
       "currentDynamicAssignedIP": currentDynamicAssignedIP,
       "currentDynamicLease": currentDynamicLease,
       "currentStaticTable": currentStaticTable,
       "currentStaticEntry": currentStaticEntry,
       "currentStaticIndex": currentStaticIndex,
       "currentStaticMacAddress": currentStaticMacAddress,
       "currentStaticAssignedIP": currentStaticAssignedIP,
       "ieee802dot11Grouping": ieee802dot11Grouping,
       "ieee802dot11GroupingTable": ieee802dot11GroupingTable,
       "ieee802dot11GroupingEntry": ieee802dot11GroupingEntry,
       "dot11LoadBalance": dot11LoadBalance,
       "dot11UserLimit": dot11UserLimit,
       "dot11LinkIntegrate": dot11LinkIntegrate,
       "ieee802dot11MultiSsid": ieee802dot11MultiSsid,
       "ieee802dot11MssidStateTable": ieee802dot11MssidStateTable,
       "ieee802dot11MssidStateEntry": ieee802dot11MssidStateEntry,
       "dot11MssidState": dot11MssidState,
       "ieee802dot11VlanTable": ieee802dot11VlanTable,
       "ieee802dot11VlanEntry": ieee802dot11VlanEntry,
       "dot11VlanState": dot11VlanState,
       "ieee802dot11MssidTable": ieee802dot11MssidTable,
       "ieee802dot11MssidEntry": ieee802dot11MssidEntry,
       "dot11MssidIndex": dot11MssidIndex,
       "dot11MssIndividualState": dot11MssIndividualState,
       "dot11MssidSsid": dot11MssidSsid,
       "dot11MssidSuppress": dot11MssidSuppress,
       "dot11MssidAuthentication": dot11MssidAuthentication,
       "dot11MssidEncryption": dot11MssidEncryption,
       "dot11MssidWepKeyIndex": dot11MssidWepKeyIndex,
       "dot11MssidWepKey": dot11MssidWepKey,
       "dot11MssidVlanTagID": dot11MssidVlanTagID,
       "dot11MssidCipherType": dot11MssidCipherType,
       "dot11MssidPassPhrase": dot11MssidPassPhrase,
       "dot11MssidKeyType": dot11MssidKeyType,
       "dot11MssidAccountingStatus": dot11MssidAccountingStatus,
       "dot11MssidWMM": dot11MssidWMM,
       "dot11MssidDynamicVlan": dot11MssidDynamicVlan,
       "dot11MssidEthNoTag": dot11MssidEthNoTag,
       "dot11MssidPriorityBySsid": dot11MssidPriorityBySsid,
       "dot11MssidInternalStationConnection": dot11MssidInternalStationConnection,
       "ieee802dot11functionTable": ieee802dot11functionTable,
       "ieee802dot11functionEntry": ieee802dot11functionEntry,
       "dot11PrioritySsidState": dot11PrioritySsidState,
       "ieee802dot11RogueApDetection": ieee802dot11RogueApDetection,
       "dot11RogueApBssType": dot11RogueApBssType,
       "dot11RogueApBandType": dot11RogueApBandType,
       "dot11RogueApSecurityType": dot11RogueApSecurityType,
       "ieee802dot11RogueApSurvey": ieee802dot11RogueApSurvey,
       "dot11RogueApSurveyRefresh": dot11RogueApSurveyRefresh,
       "dot11RogueApAddtoApList": dot11RogueApAddtoApList,
       "dot11RrogueApDelete": dot11RrogueApDelete,
       "ieee802dot11RogueApSurveyTable": ieee802dot11RogueApSurveyTable,
       "dot11RogueApSurveyEntry": dot11RogueApSurveyEntry,
       "dot11RogueApSurveyIndex": dot11RogueApSurveyIndex,
       "dot11RogueApSurveyBssType": dot11RogueApSurveyBssType,
       "dot11RogueApSurveyChannel": dot11RogueApSurveyChannel,
       "dot11RogueApSurveyRssi": dot11RogueApSurveyRssi,
       "dot11RogueApSurveyBssid": dot11RogueApSurveyBssid,
       "dot11RogueApSurveyAuthentication": dot11RogueApSurveyAuthentication,
       "dot11RogueApSurveyEncryption": dot11RogueApSurveyEncryption,
       "dot11RogueApSurveyMode": dot11RogueApSurveyMode,
       "dot11RogueApSurveySsid": dot11RogueApSurveySsid,
       "dot11RogueApListRecord": dot11RogueApListRecord,
       "dot11RogueApDeleteFromRecord": dot11RogueApDeleteFromRecord,
       "dot11RogueApListRecordTable": dot11RogueApListRecordTable,
       "dot11RogueApListRecordEntry": dot11RogueApListRecordEntry,
       "dot11RogueApListRecordIndex": dot11RogueApListRecordIndex,
       "dot11RogueApListRecordBssType": dot11RogueApListRecordBssType,
       "dot11RogueApListRecordChannel": dot11RogueApListRecordChannel,
       "dot11RogueApListRecordRssi": dot11RogueApListRecordRssi,
       "dot11RogueApListRecordBssid": dot11RogueApListRecordBssid,
       "dot11RogueApListRecordAuthentication": dot11RogueApListRecordAuthentication,
       "dot11RogueApListRecordEncryption": dot11RogueApListRecordEncryption,
       "dot11RogueApListRecordMode": dot11RogueApListRecordMode,
       "dot11RogueApListRecordSsid": dot11RogueApListRecordSsid,
       "dot11RogueApProtection": dot11RogueApProtection,
       "ieee802dot11DataRateControl": ieee802dot11DataRateControl,
       "ieee802dot11DataRateControlTable": ieee802dot11DataRateControlTable,
       "ieee802dot11DataRateControlEntry": ieee802dot11DataRateControlEntry,
       "dot11DataRateControl": dot11DataRateControl,
       "dot11DataRateSetDefault": dot11DataRateSetDefault,
       "ieee802dot11DataRateTable": ieee802dot11DataRateTable,
       "ieee802dot11DataRateEntry": ieee802dot11DataRateEntry,
       "dot11DataRate1Mb": dot11DataRate1Mb,
       "dot11DataRate2Mb": dot11DataRate2Mb,
       "dot11DataRate5dot5Mb": dot11DataRate5dot5Mb,
       "dot11DataRate6Mb": dot11DataRate6Mb,
       "dot11DataRate9Mb": dot11DataRate9Mb,
       "dot11DataRate11Mb": dot11DataRate11Mb,
       "dot11DataRate12Mb": dot11DataRate12Mb,
       "dot11DataRate18Mb": dot11DataRate18Mb,
       "dot11DataRate24Mb": dot11DataRate24Mb,
       "dot11DataRate36Mb": dot11DataRate36Mb,
       "dot11DataRate48Mb": dot11DataRate48Mb,
       "dot11DataRate54Mb": dot11DataRate54Mb,
       "administration": administration,
       "users": users,
       "usersTable": usersTable,
       "usersEntry": usersEntry,
       "usersIndex": usersIndex,
       "usersName": usersName,
       "usersPassword": usersPassword,
       "device": device,
       "deviceRestart": deviceRestart,
       "deviceFactoryDefault": deviceFactoryDefault,
       "update": update,
       "updateFirmwareVersion": updateFirmwareVersion,
       "tftp": tftp,
       "tftpServerIPAddress": tftpServerIPAddress,
       "tftpRemoteFileName": tftpRemoteFileName,
       "tftpCommand": tftpCommand,
       "tftpUpgradeSettingCommand": tftpUpgradeSettingCommand,
       "ftp": ftp,
       "ftpServerIPAddress": ftpServerIPAddress,
       "ftpUserName": ftpUserName,
       "ftpPassword": ftpPassword,
       "ftpRemoteFileName": ftpRemoteFileName,
       "ftpCommand": ftpCommand,
       "ftpUpgradeSettingCommand": ftpUpgradeSettingCommand,
       "discardChanges": discardChanges,
       "console": console,
       "telnet": telnet,
       "ssh": ssh,
       "timeout": timeout,
       "web": web,
       "ssl": ssl,
       "sntp": sntp,
       "sntpServerIpAddress": sntpServerIpAddress,
       "sntpTimeZoneIndex": sntpTimeZoneIndex,
       "sntpDayLightSaving": sntpDayLightSaving,
       "sntpTimeofDay": sntpTimeofDay,
       "smtp": smtp,
       "smtpStatus": smtpStatus,
       "smtpServerIpAddress": smtpServerIpAddress,
       "smtpSender": smtpSender,
       "smtpRecipient": smtpRecipient,
       "managerIpAddressSetting": managerIpAddressSetting,
       "managerIpAddressStatus": managerIpAddressStatus,
       "managerIpAddressTable": managerIpAddressTable,
       "managerIpAddressEntry": managerIpAddressEntry,
       "managerIpAddressIndex": managerIpAddressIndex,
       "managerIpAddress": managerIpAddress,
       "managerIpRangeTable": managerIpRangeTable,
       "managerIpRangeEntry": managerIpRangeEntry,
       "managerIpRangeIndex": managerIpRangeIndex,
       "managerStartIpAddress": managerStartIpAddress,
       "managerEndIpAddress": managerEndIpAddress,
       "control": control,
       "pingcontrol": pingcontrol,
       "adminAPwithWlan": adminAPwithWlan,
       "managerVLANIDSetting": managerVLANIDSetting,
       "managerVLANIDStatus": managerVLANIDStatus,
       "managerVLANID": managerVLANID,
       "report": report,
       "deviceInformation": deviceInformation,
       "deviceInformationFirmwareVersion": deviceInformationFirmwareVersion,
       "interfaceInformation": interfaceInformation,
       "interfaceInformationTable": interfaceInformationTable,
       "interfaceInformationEntry": interfaceInformationEntry,
       "ifGetIpAddressFrom": ifGetIpAddressFrom,
       "ifIpAddress": ifIpAddress,
       "ifSubnetMask": ifSubnetMask,
       "ifDefaultGateway": ifDefaultGateway,
       "ifMacAddress": ifMacAddress,
       "apstatus": apstatus,
       "deviceInformationCpuUtilization": deviceInformationCpuUtilization,
       "deviceInformationMemUtilization": deviceInformationMemUtilization,
       "trafficStatistics": trafficStatistics,
       "trafficStatisticsWired": trafficStatisticsWired,
       "dot3TrafficStatistics": dot3TrafficStatistics,
       "dot3TrafficStatisticsTable": dot3TrafficStatisticsTable,
       "dot3TrafficStatisticsEntry": dot3TrafficStatisticsEntry,
       "dot3TransmittedFrameCount": dot3TransmittedFrameCount,
       "dot3ReceivedFrameCount": dot3ReceivedFrameCount,
       "dot3TransmittedByteCount": dot3TransmittedByteCount,
       "dot3ReceivedByteCount": dot3ReceivedByteCount,
       "trafficStatisticsWireless": trafficStatisticsWireless,
       "dot11TrafficStatistics": dot11TrafficStatistics,
       "dot11TrafficStatisticsTable": dot11TrafficStatisticsTable,
       "dot11TrafficStatisticsEntry": dot11TrafficStatisticsEntry,
       "dot11TransmitSuccessRate": dot11TransmitSuccessRate,
       "dot11TransmitRetryRate": dot11TransmitRetryRate,
       "dot11ReceiveSuccessRate": dot11ReceiveSuccessRate,
       "dot11ReceiveDuplicateRate": dot11ReceiveDuplicateRate,
       "dot11RtsSuccessCount": dot11RtsSuccessCount,
       "dot11RtsFailureCount": dot11RtsFailureCount,
       "dot11TransmittedFrameCount": dot11TransmittedFrameCount,
       "dot11MulticastTransmittedFrameCount": dot11MulticastTransmittedFrameCount,
       "dot11TransmittedErrorCount": dot11TransmittedErrorCount,
       "dot11TransmittedTotalRetryCount": dot11TransmittedTotalRetryCount,
       "dot11TransmittedMultipleRetryCount": dot11TransmittedMultipleRetryCount,
       "dot11ReceivedFrameCount": dot11ReceivedFrameCount,
       "dot11MulticastReceivedFrameCount": dot11MulticastReceivedFrameCount,
       "dot11ReceivedFrameFcsErrorCount": dot11ReceivedFrameFcsErrorCount,
       "dot11ReceivedFrameDuplicateCount": dot11ReceivedFrameDuplicateCount,
       "dot11AckReceivedFailureCount": dot11AckReceivedFailureCount,
       "dot11WepExcludedFrameCount": dot11WepExcludedFrameCount,
       "dot11WepIcvErrorCount": dot11WepIcvErrorCount,
       "dot11TransmitedByteCount": dot11TransmitedByteCount,
       "dot11ReceivedByteCount": dot11ReceivedByteCount,
       "dot16TrafficStatistics": dot16TrafficStatistics,
       "trafficStatisticsOn11aEverySSID": trafficStatisticsOn11aEverySSID,
       "trafficStatisticsOn11APrimarySSID": trafficStatisticsOn11APrimarySSID,
       "onPrimarySSIDdot11aReceivedByteCount": onPrimarySSIDdot11aReceivedByteCount,
       "onPrimarySSIDdot11aTransmitByteCount": onPrimarySSIDdot11aTransmitByteCount,
       "on11aPrimarySSIDdot3ReceivedByteCount": on11aPrimarySSIDdot3ReceivedByteCount,
       "on11aPrimarySSIDdot3TransmitByteCount": on11aPrimarySSIDdot3TransmitByteCount,
       "onPrimarySSIDdot11aCRCErrorCount": onPrimarySSIDdot11aCRCErrorCount,
       "onPrimarySSIDdot11aPHYErrorCount": onPrimarySSIDdot11aPHYErrorCount,
       "onPrimarySSIDdot11aMICErrorCount": onPrimarySSIDdot11aMICErrorCount,
       "onPrimarySSIDdot11aKEYDecrErrorCount": onPrimarySSIDdot11aKEYDecrErrorCount,
       "on11aPrimarySSIDdot3ReceivedPKTCount": on11aPrimarySSIDdot3ReceivedPKTCount,
       "onPrimarySSIDdot11aUserReceivedByteCount": onPrimarySSIDdot11aUserReceivedByteCount,
       "onPrimarySSIDdot11aUserTransmitByteCount": onPrimarySSIDdot11aUserTransmitByteCount,
       "dot11aTrafficStatisticsByTimeOnPrimarySSIDTable": dot11aTrafficStatisticsByTimeOnPrimarySSIDTable,
       "dot11aTrafficStatisticsByTimeOnPrimarySSIDEntry": dot11aTrafficStatisticsByTimeOnPrimarySSIDEntry,
       "onPrimarySSIDdot11aAssociatedMACCount": onPrimarySSIDdot11aAssociatedMACCount,
       "onPrimarySSIDdot11aErrorFrameRate": onPrimarySSIDdot11aErrorFrameRate,
       "on11aPrimarySSIDdot3ErrorFrameRate": on11aPrimarySSIDdot3ErrorFrameRate,
       "onPrimarySSIDdot11aWirelessUsage": onPrimarySSIDdot11aWirelessUsage,
       "trafficStatisticsOn11aSSID1": trafficStatisticsOn11aSSID1,
       "onSSID1dot11aReceivedByteCount": onSSID1dot11aReceivedByteCount,
       "onSSID1dot11aTransmitByteCount": onSSID1dot11aTransmitByteCount,
       "on11aSSID1dot3ReceivedByteCount": on11aSSID1dot3ReceivedByteCount,
       "on11aSSID1dot3TransmitByteCount": on11aSSID1dot3TransmitByteCount,
       "onSSID1dot11aCRCErrorCount": onSSID1dot11aCRCErrorCount,
       "onSSID1dot11aPHYErrorCount": onSSID1dot11aPHYErrorCount,
       "onSSID1dot11aMICErrorCount": onSSID1dot11aMICErrorCount,
       "onSSID1dot11aKEYDecrErrorCount": onSSID1dot11aKEYDecrErrorCount,
       "on11aSSID1dot3ReceivedPKTCount": on11aSSID1dot3ReceivedPKTCount,
       "onSSID1dot11aUserReceivedByteCount": onSSID1dot11aUserReceivedByteCount,
       "onSSID1dot11aUserTransmitByteCount": onSSID1dot11aUserTransmitByteCount,
       "dot11aTrafficStatisticsByTimeOnSSID1Table": dot11aTrafficStatisticsByTimeOnSSID1Table,
       "dot11aTrafficStatisticsByTimeOnSSID1Entry": dot11aTrafficStatisticsByTimeOnSSID1Entry,
       "onSSID1dot11AssociatedMACCount": onSSID1dot11AssociatedMACCount,
       "onSSID1dot11aErrorFrameRate": onSSID1dot11aErrorFrameRate,
       "on11aSSID1dot3ErrorFrameRate": on11aSSID1dot3ErrorFrameRate,
       "onSSID1dot11aWirelessUsage": onSSID1dot11aWirelessUsage,
       "trafficStatisticsOn11aSSID2": trafficStatisticsOn11aSSID2,
       "onSSID2dot11aReceivedByteCount": onSSID2dot11aReceivedByteCount,
       "onSSID2dot11aTransmitByteCount": onSSID2dot11aTransmitByteCount,
       "on11aSSID2dot3ReceivedByteCount": on11aSSID2dot3ReceivedByteCount,
       "on11aSSID2dot3TransmitByteCount": on11aSSID2dot3TransmitByteCount,
       "onSSID2dot11aCRCErrorCount": onSSID2dot11aCRCErrorCount,
       "onSSID2dot11aPHYErrorCount": onSSID2dot11aPHYErrorCount,
       "onSSID2dot11aMICErrorCount": onSSID2dot11aMICErrorCount,
       "onSSID2dot11aKEYDecrErrorCount": onSSID2dot11aKEYDecrErrorCount,
       "on11aSSID2dot3ReceivedPKTCount": on11aSSID2dot3ReceivedPKTCount,
       "onSSID2dot11aUserReceivedByteCount": onSSID2dot11aUserReceivedByteCount,
       "onSSID2dot11aUserTransmitByteCount": onSSID2dot11aUserTransmitByteCount,
       "dot11aTrafficStatisticsByTimeOnSSID2Table": dot11aTrafficStatisticsByTimeOnSSID2Table,
       "dot11aTrafficStatisticsByTimeOnSSID2Entry": dot11aTrafficStatisticsByTimeOnSSID2Entry,
       "onSSID2dot11associatedMACCount": onSSID2dot11associatedMACCount,
       "onSSID2dot11aErrorFrameRate": onSSID2dot11aErrorFrameRate,
       "on11aSSID2dot3ErrorFrameRate": on11aSSID2dot3ErrorFrameRate,
       "onSSID2dot11aWirelessUsage": onSSID2dot11aWirelessUsage,
       "trafficStatisticsOn11aSSID3": trafficStatisticsOn11aSSID3,
       "onSSID3dot11aReceivedByteCount": onSSID3dot11aReceivedByteCount,
       "onSSID3dot11aTransmitByteCount": onSSID3dot11aTransmitByteCount,
       "on11aSSID3dot3ReceivedByteCount": on11aSSID3dot3ReceivedByteCount,
       "on11aSSID3dot3TransmitByteCount": on11aSSID3dot3TransmitByteCount,
       "onSSID3dot11aCRCErrorCount": onSSID3dot11aCRCErrorCount,
       "onSSID3dot11aPHYErrorCount": onSSID3dot11aPHYErrorCount,
       "onSSID3dot11aMICErrorCount": onSSID3dot11aMICErrorCount,
       "onSSID3dot11aKEYDecrErrorCount": onSSID3dot11aKEYDecrErrorCount,
       "on11aSSID3dot3ReceivedPKTCount": on11aSSID3dot3ReceivedPKTCount,
       "onSSID3dot11aUserReceivedByteCount": onSSID3dot11aUserReceivedByteCount,
       "onSSID3dot11aUserTransmitByteCount": onSSID3dot11aUserTransmitByteCount,
       "dot11aTrafficStatisticsByTimeOnSSID3Table": dot11aTrafficStatisticsByTimeOnSSID3Table,
       "dot11aTrafficStatisticsByTimeOnSSID3Entry": dot11aTrafficStatisticsByTimeOnSSID3Entry,
       "onSSID3dot11associatedMACCount": onSSID3dot11associatedMACCount,
       "onSSID3dot11aErrorFrameRate": onSSID3dot11aErrorFrameRate,
       "on11aSSID3dot3ErrorFrameRate": on11aSSID3dot3ErrorFrameRate,
       "onSSID3dot11aWirelessUsage": onSSID3dot11aWirelessUsage,
       "trafficStatisticsOn11aSSID4": trafficStatisticsOn11aSSID4,
       "onSSID4dot11aReceivedByteCount": onSSID4dot11aReceivedByteCount,
       "onSSID4dot11aTransmitByteCount": onSSID4dot11aTransmitByteCount,
       "on11aSSID4dot3ReceivedByteCount": on11aSSID4dot3ReceivedByteCount,
       "on11aSSID4dot3TransmitByteCount": on11aSSID4dot3TransmitByteCount,
       "onSSID4dot11aCRCErrorCount": onSSID4dot11aCRCErrorCount,
       "onSSID4dot11aPHYErrorCount": onSSID4dot11aPHYErrorCount,
       "onSSID4dot11aMICErrorCount": onSSID4dot11aMICErrorCount,
       "onSSID4dot11aKEYDecrErrorCount": onSSID4dot11aKEYDecrErrorCount,
       "on11aSSID4dot3ReceivedPKTCount": on11aSSID4dot3ReceivedPKTCount,
       "onSSID4dot11aUserReceivedByteCount": onSSID4dot11aUserReceivedByteCount,
       "onSSID4dot11aUserTransmitByteCount": onSSID4dot11aUserTransmitByteCount,
       "dot11aTrafficStatisticsByTimeOnSSID4Table": dot11aTrafficStatisticsByTimeOnSSID4Table,
       "dot11aTrafficStatisticsByTimeOnSSID4Entry": dot11aTrafficStatisticsByTimeOnSSID4Entry,
       "onSSID4dot11associatedMACCount": onSSID4dot11associatedMACCount,
       "onSSID4dot11aErrorFrameRate": onSSID4dot11aErrorFrameRate,
       "on11aSSID4dot3ErrorFrameRate": on11aSSID4dot3ErrorFrameRate,
       "onSSID4dot11aWirelessUsage": onSSID4dot11aWirelessUsage,
       "trafficStatisticsOn11aSSID5": trafficStatisticsOn11aSSID5,
       "onSSID5dot11aReceivedByteCount": onSSID5dot11aReceivedByteCount,
       "onSSID5dot11aTransmitByteCount": onSSID5dot11aTransmitByteCount,
       "on11aSSID5dot3ReceivedByteCount": on11aSSID5dot3ReceivedByteCount,
       "on11aSSID5dot3TransmitByteCount": on11aSSID5dot3TransmitByteCount,
       "onSSID5dot11aCRCErrorCount": onSSID5dot11aCRCErrorCount,
       "onSSID5dot11aPHYErrorCount": onSSID5dot11aPHYErrorCount,
       "onSSID5dot11aMICErrorCount": onSSID5dot11aMICErrorCount,
       "onSSID5dot11aKEYDecrErrorCount": onSSID5dot11aKEYDecrErrorCount,
       "on11aSSID5dot3ReceivedPKTCount": on11aSSID5dot3ReceivedPKTCount,
       "onSSID5dot11aUserReceivedByteCount": onSSID5dot11aUserReceivedByteCount,
       "onSSID5dot11aUserTransmitByteCount": onSSID5dot11aUserTransmitByteCount,
       "dot11aTrafficStatisticsByTimeOnSSID5Table": dot11aTrafficStatisticsByTimeOnSSID5Table,
       "dot11aTrafficStatisticsByTimeOnSSID5Entry": dot11aTrafficStatisticsByTimeOnSSID5Entry,
       "onSSID5dot11associatedMACCount": onSSID5dot11associatedMACCount,
       "onSSID5dot11aErrorFrameRate": onSSID5dot11aErrorFrameRate,
       "on11aSSID5dot3ErrorFrameRate": on11aSSID5dot3ErrorFrameRate,
       "onSSID5dot11aWirelessUsage": onSSID5dot11aWirelessUsage,
       "trafficStatisticsOn11aSSID6": trafficStatisticsOn11aSSID6,
       "onSSID6dot11aReceivedByteCount": onSSID6dot11aReceivedByteCount,
       "onSSID6dot11aTransmitByteCount": onSSID6dot11aTransmitByteCount,
       "on11aSSID6dot3ReceivedByteCount": on11aSSID6dot3ReceivedByteCount,
       "on11aSSID6dot3TransmitByteCount": on11aSSID6dot3TransmitByteCount,
       "onSSID6dot11aCRCErrorCount": onSSID6dot11aCRCErrorCount,
       "onSSID6dot11aPHYErrorCount": onSSID6dot11aPHYErrorCount,
       "onSSID6dot11aMICErrorCount": onSSID6dot11aMICErrorCount,
       "onSSID6dot11aKEYDecrErrorCount": onSSID6dot11aKEYDecrErrorCount,
       "on11aSSID6dot3ReceivedPKTCount": on11aSSID6dot3ReceivedPKTCount,
       "onSSID6dot11aUserReceivedByteCount": onSSID6dot11aUserReceivedByteCount,
       "onSSID6dot11aUserTransmitByteCount": onSSID6dot11aUserTransmitByteCount,
       "dot11aTrafficStatisticsByTimeOnSSID6Table": dot11aTrafficStatisticsByTimeOnSSID6Table,
       "dot11aTrafficStatisticsByTimeOnSSID6Entry": dot11aTrafficStatisticsByTimeOnSSID6Entry,
       "onSSID6dot11associatedMACCount": onSSID6dot11associatedMACCount,
       "onSSID6dot11aErrorFrameRate": onSSID6dot11aErrorFrameRate,
       "on11aSSID6dot3ErrorFrameRate": on11aSSID6dot3ErrorFrameRate,
       "onSSID6dot11aWirelessUsage": onSSID6dot11aWirelessUsage,
       "trafficStatisticsOn11aSSID7": trafficStatisticsOn11aSSID7,
       "onSSID7dot11aReceivedByteCount": onSSID7dot11aReceivedByteCount,
       "onSSID7dot11aTransmitByteCount": onSSID7dot11aTransmitByteCount,
       "on11aSSID7dot3ReceivedByteCount": on11aSSID7dot3ReceivedByteCount,
       "on11aSSID7dot3TransmitByteCount": on11aSSID7dot3TransmitByteCount,
       "onSSID7dot11aCRCErrorCount": onSSID7dot11aCRCErrorCount,
       "onSSID7dot11aPHYErrorCount": onSSID7dot11aPHYErrorCount,
       "onSSID7dot11aMICErrorCount": onSSID7dot11aMICErrorCount,
       "onSSID7dot11aKEYDecrErrorCount": onSSID7dot11aKEYDecrErrorCount,
       "on11aSSID7dot3ReceivedPKTCount": on11aSSID7dot3ReceivedPKTCount,
       "onSSID7dot11aUserReceivedByteCount": onSSID7dot11aUserReceivedByteCount,
       "onSSID7dot11aUserTransmitByteCount": onSSID7dot11aUserTransmitByteCount,
       "dot11aTrafficStatisticsByTimeOnSSID7Table": dot11aTrafficStatisticsByTimeOnSSID7Table,
       "dot11aTrafficStatisticsByTimeOnSSID7Entry": dot11aTrafficStatisticsByTimeOnSSID7Entry,
       "onSSID7dot11associatedMACCount": onSSID7dot11associatedMACCount,
       "onSSID7dot11aErrorFrameRate": onSSID7dot11aErrorFrameRate,
       "on11aSSID7dot3ErrorFrameRate": on11aSSID7dot3ErrorFrameRate,
       "onSSID7dot11aWirelessUsage": onSSID7dot11aWirelessUsage,
       "trafficStatisticsOn11gEverySSID": trafficStatisticsOn11gEverySSID,
       "trafficStatisticson11gPrimarySSID": trafficStatisticson11gPrimarySSID,
       "onPrimarySSIDdot11gReceivedByteCount": onPrimarySSIDdot11gReceivedByteCount,
       "onPrimarySSIDdot11gTransmitByteCount": onPrimarySSIDdot11gTransmitByteCount,
       "on11gPrimarySSIDdot3ReceivedByteCount": on11gPrimarySSIDdot3ReceivedByteCount,
       "on11gPrimarySSIDdot3TransmitByteCount": on11gPrimarySSIDdot3TransmitByteCount,
       "onPrimarySSIDdot11gCRCErrorCount": onPrimarySSIDdot11gCRCErrorCount,
       "onPrimarySSIDdot11gPHYErrorCount": onPrimarySSIDdot11gPHYErrorCount,
       "onPrimarySSIDdot11gMICErrorCount": onPrimarySSIDdot11gMICErrorCount,
       "onPrimarySSIDdot11gKEYDecrErrorCount": onPrimarySSIDdot11gKEYDecrErrorCount,
       "on11gPrimarySSIDdot3ReceivedPKTCount": on11gPrimarySSIDdot3ReceivedPKTCount,
       "onPrimarySSIDdot11gUserReceivedByteCount": onPrimarySSIDdot11gUserReceivedByteCount,
       "onPrimarySSIDdot11gUserTransmitByteCount": onPrimarySSIDdot11gUserTransmitByteCount,
       "dot11gTrafficStatisticsByTimeOnPrimarySSIDTable": dot11gTrafficStatisticsByTimeOnPrimarySSIDTable,
       "dot11gTrafficStatisticsByTimeOnPrimarySSIDEntry": dot11gTrafficStatisticsByTimeOnPrimarySSIDEntry,
       "onPrimarySSIDdot11gAssociatedMACCount": onPrimarySSIDdot11gAssociatedMACCount,
       "onPrimarySSIDdot11gErrorFrameRate": onPrimarySSIDdot11gErrorFrameRate,
       "on11gPrimarySSIDdot3ErrorFrameRate": on11gPrimarySSIDdot3ErrorFrameRate,
       "onPrimarySSIDdot11gWirelessUsage": onPrimarySSIDdot11gWirelessUsage,
       "trafficStatisticson11gSSID1": trafficStatisticson11gSSID1,
       "onSSID1dot11gReceivedByteCount": onSSID1dot11gReceivedByteCount,
       "onSSID1dot11gTransmitByteCount": onSSID1dot11gTransmitByteCount,
       "on11gSSID1dot3ReceivedByteCount": on11gSSID1dot3ReceivedByteCount,
       "on11gSSID1dot3TransmitByteCount": on11gSSID1dot3TransmitByteCount,
       "onSSID1dot11gCRCErrorCount": onSSID1dot11gCRCErrorCount,
       "onSSID1dot11gPHYErrorCount": onSSID1dot11gPHYErrorCount,
       "onSSID1dot11gMICErrorCount": onSSID1dot11gMICErrorCount,
       "onSSID1dot11gKEYDecrErrorCount": onSSID1dot11gKEYDecrErrorCount,
       "on11gSSID1dot3ReceivedPKTCount": on11gSSID1dot3ReceivedPKTCount,
       "onSSID1dot11gUserReceivedByteCount": onSSID1dot11gUserReceivedByteCount,
       "onSSID1dot11gUserTransmitByteCount": onSSID1dot11gUserTransmitByteCount,
       "dot11gTrafficStatisticsByTimeOnSSID1Table": dot11gTrafficStatisticsByTimeOnSSID1Table,
       "dot11gTrafficStatisticsByTimeOnSSID1Entry": dot11gTrafficStatisticsByTimeOnSSID1Entry,
       "onSSID1dot11gssociatedMACCount": onSSID1dot11gssociatedMACCount,
       "onSSID1dot11gErrorFrameRate": onSSID1dot11gErrorFrameRate,
       "on11gSSID1dot3ErrorFrameRate": on11gSSID1dot3ErrorFrameRate,
       "onSSID1dot11gWirelessUsage": onSSID1dot11gWirelessUsage,
       "trafficStatisticson11gSSID2": trafficStatisticson11gSSID2,
       "onSSID2dot11gReceivedByteCount": onSSID2dot11gReceivedByteCount,
       "onSSID2dot11gTransmitByteCount": onSSID2dot11gTransmitByteCount,
       "on11gSSID2dot3ReceivedByteCount": on11gSSID2dot3ReceivedByteCount,
       "on11gSSID2dot3TransmitByteCount": on11gSSID2dot3TransmitByteCount,
       "onSSID2dot11gCRCErrorCount": onSSID2dot11gCRCErrorCount,
       "onSSID2dot11gPHYErrorCount": onSSID2dot11gPHYErrorCount,
       "onSSID2dot11gMICErrorCount": onSSID2dot11gMICErrorCount,
       "onSSID2dot11gKEYDecrErrorCount": onSSID2dot11gKEYDecrErrorCount,
       "on11gSSID2dot3ReceivedPKTCount": on11gSSID2dot3ReceivedPKTCount,
       "onSSID2dot11gUserReceivedByteCount": onSSID2dot11gUserReceivedByteCount,
       "onSSID2dot11gUserTransmitByteCount": onSSID2dot11gUserTransmitByteCount,
       "dot11gTrafficStatisticsByTimeOnSSID2Table": dot11gTrafficStatisticsByTimeOnSSID2Table,
       "dot11gTrafficStatisticsByTimeOnSSID2Entry": dot11gTrafficStatisticsByTimeOnSSID2Entry,
       "onSSID2dot11gssociatedMACCount": onSSID2dot11gssociatedMACCount,
       "onSSID2dot11gErrorFrameRate": onSSID2dot11gErrorFrameRate,
       "on11gSSID2dot3ErrorFrameRate": on11gSSID2dot3ErrorFrameRate,
       "onSSID2dot11gWirelessUsage": onSSID2dot11gWirelessUsage,
       "trafficStatisticson11gSSID3": trafficStatisticson11gSSID3,
       "onSSID3dot11gReceivedByteCount": onSSID3dot11gReceivedByteCount,
       "onSSID3dot11gTransmitByteCount": onSSID3dot11gTransmitByteCount,
       "on11gSSID3dot3ReceivedByteCount": on11gSSID3dot3ReceivedByteCount,
       "on11gSSID3dot3TransmitByteCount": on11gSSID3dot3TransmitByteCount,
       "onSSID3dot11gCRCErrorCount": onSSID3dot11gCRCErrorCount,
       "onSSID3dot11gPHYErrorCount": onSSID3dot11gPHYErrorCount,
       "onSSID3dot11gMICErrorCount": onSSID3dot11gMICErrorCount,
       "onSSID3dot11gKEYDecrErrorCount": onSSID3dot11gKEYDecrErrorCount,
       "on11gSSID3dot3ReceivedPKTCount": on11gSSID3dot3ReceivedPKTCount,
       "onSSID3dot11gUserReceivedByteCount": onSSID3dot11gUserReceivedByteCount,
       "onSSID3dot11gUserTransmitByteCount": onSSID3dot11gUserTransmitByteCount,
       "dot11gTrafficStatisticsByTimeOnSSID3Table": dot11gTrafficStatisticsByTimeOnSSID3Table,
       "dot11gTrafficStatisticsByTimeOnSSID3Entry": dot11gTrafficStatisticsByTimeOnSSID3Entry,
       "onSSID3dot11gssociatedMACCount": onSSID3dot11gssociatedMACCount,
       "onSSID3dot11gErrorFrameRate": onSSID3dot11gErrorFrameRate,
       "on11gSSID3dot3ErrorFrameRate": on11gSSID3dot3ErrorFrameRate,
       "onSSID3dot11gWirelessUsage": onSSID3dot11gWirelessUsage,
       "trafficStatisticson11gSSID4": trafficStatisticson11gSSID4,
       "onSSID4dot11gReceivedByteCount": onSSID4dot11gReceivedByteCount,
       "onSSID4dot11gTransmitByteCount": onSSID4dot11gTransmitByteCount,
       "on11gSSID4dot3ReceivedByteCount": on11gSSID4dot3ReceivedByteCount,
       "on11gSSID4dot3TransmitByteCount": on11gSSID4dot3TransmitByteCount,
       "onSSID4dot11gCRCErrorCount": onSSID4dot11gCRCErrorCount,
       "onSSID4dot11gPHYErrorCount": onSSID4dot11gPHYErrorCount,
       "onSSID4dot11gMICErrorCount": onSSID4dot11gMICErrorCount,
       "onSSID4dot11gKEYDecrErrorCount": onSSID4dot11gKEYDecrErrorCount,
       "on11gSSID4dot3ReceivedPKTCount": on11gSSID4dot3ReceivedPKTCount,
       "onSSID4dot11gUserReceivedByteCount": onSSID4dot11gUserReceivedByteCount,
       "onSSID4dot11gUserTransmitByteCount": onSSID4dot11gUserTransmitByteCount,
       "dot11gTrafficStatisticsByTimeOnSSID4Table": dot11gTrafficStatisticsByTimeOnSSID4Table,
       "dot11gTrafficStatisticsByTimeOnSSID4Entry": dot11gTrafficStatisticsByTimeOnSSID4Entry,
       "onSSID4dot11gssociatedMACCount": onSSID4dot11gssociatedMACCount,
       "onSSID4dot11gErrorFrameRate": onSSID4dot11gErrorFrameRate,
       "on11gSSID4dot3ErrorFrameRate": on11gSSID4dot3ErrorFrameRate,
       "onSSID4dot11gWirelessUsage": onSSID4dot11gWirelessUsage,
       "trafficStatisticson11gSSID5": trafficStatisticson11gSSID5,
       "onSSID5dot11gReceivedByteCount": onSSID5dot11gReceivedByteCount,
       "onSSID5dot11gTransmitByteCount": onSSID5dot11gTransmitByteCount,
       "on11gSSID5dot3ReceivedByteCount": on11gSSID5dot3ReceivedByteCount,
       "on11gSSID5dot3TransmitByteCount": on11gSSID5dot3TransmitByteCount,
       "onSSID5dot11gCRCErrorCount": onSSID5dot11gCRCErrorCount,
       "onSSID5dot11gPHYErrorCount": onSSID5dot11gPHYErrorCount,
       "onSSID5dot11gMICErrorCount": onSSID5dot11gMICErrorCount,
       "onSSID5dot11gKEYDecrErrorCount": onSSID5dot11gKEYDecrErrorCount,
       "on11gSSID5dot3ReceivedPKTCount": on11gSSID5dot3ReceivedPKTCount,
       "onSSID5dot11gUserReceivedByteCount": onSSID5dot11gUserReceivedByteCount,
       "onSSID5dot11gUserTransmitByteCount": onSSID5dot11gUserTransmitByteCount,
       "dot11gTrafficStatisticsByTimeOnSSID5Table": dot11gTrafficStatisticsByTimeOnSSID5Table,
       "dot11gTrafficStatisticsByTimeOnSSID5Entry": dot11gTrafficStatisticsByTimeOnSSID5Entry,
       "onSSID5dot11gssociatedMACCount": onSSID5dot11gssociatedMACCount,
       "onSSID5dot11gErrorFrameRate": onSSID5dot11gErrorFrameRate,
       "on11gSSID5dot3ErrorFrameRate": on11gSSID5dot3ErrorFrameRate,
       "onSSID5dot11gWirelessUsage": onSSID5dot11gWirelessUsage,
       "trafficStatisticson11gSSID6": trafficStatisticson11gSSID6,
       "onSSID6dot11gReceivedByteCount": onSSID6dot11gReceivedByteCount,
       "onSSID6dot11gTransmitByteCount": onSSID6dot11gTransmitByteCount,
       "on11gSSID6dot3ReceivedByteCount": on11gSSID6dot3ReceivedByteCount,
       "on11gSSID6dot3TransmitByteCount": on11gSSID6dot3TransmitByteCount,
       "onSSID6dot11gCRCErrorCount": onSSID6dot11gCRCErrorCount,
       "onSSID6dot11gPHYErrorCount": onSSID6dot11gPHYErrorCount,
       "onSSID6dot11gMICErrorCount": onSSID6dot11gMICErrorCount,
       "onSSID6dot11gKEYDecrErrorCount": onSSID6dot11gKEYDecrErrorCount,
       "on11gSSID6dot3ReceivedPKTCount": on11gSSID6dot3ReceivedPKTCount,
       "onSSID6dot11gUserReceivedByteCount": onSSID6dot11gUserReceivedByteCount,
       "onSSID6dot11gUserTransmitByteCount": onSSID6dot11gUserTransmitByteCount,
       "dot11gTrafficStatisticsByTimeOnSSID6Table": dot11gTrafficStatisticsByTimeOnSSID6Table,
       "dot11gTrafficStatisticsByTimeOnSSID6Entry": dot11gTrafficStatisticsByTimeOnSSID6Entry,
       "onSSID6dot11gssociatedMACCount": onSSID6dot11gssociatedMACCount,
       "onSSID6dot11gErrorFrameRate": onSSID6dot11gErrorFrameRate,
       "on11gSSID6dot3ErrorFrameRate": on11gSSID6dot3ErrorFrameRate,
       "onSSID6dot11gWirelessUsage": onSSID6dot11gWirelessUsage,
       "trafficStatisticson11gSSID7": trafficStatisticson11gSSID7,
       "onSSID7dot11gReceivedByteCount": onSSID7dot11gReceivedByteCount,
       "onSSID7dot11gTransmitByteCount": onSSID7dot11gTransmitByteCount,
       "on11gSSID7dot3ReceivedByteCount": on11gSSID7dot3ReceivedByteCount,
       "on11gSSID7dot3TransmitByteCount": on11gSSID7dot3TransmitByteCount,
       "onSSID7dot11gCRCErrorCount": onSSID7dot11gCRCErrorCount,
       "onSSID7dot11gPHYErrorCount": onSSID7dot11gPHYErrorCount,
       "onSSID7dot11gMICErrorCount": onSSID7dot11gMICErrorCount,
       "onSSID7dot11gKEYDecrErrorCount": onSSID7dot11gKEYDecrErrorCount,
       "on11gSSID7dot3ReceivedPKTCount": on11gSSID7dot3ReceivedPKTCount,
       "onSSID7dot11gUserReceivedByteCount": onSSID7dot11gUserReceivedByteCount,
       "onSSID7dot11gUserTransmitByteCount": onSSID7dot11gUserTransmitByteCount,
       "dot11gTrafficStatisticsByTimeOnSSID7Table": dot11gTrafficStatisticsByTimeOnSSID7Table,
       "dot11gTrafficStatisticsByTimeOnSSID7Entry": dot11gTrafficStatisticsByTimeOnSSID7Entry,
       "onSSID7dot11gssociatedMACCount": onSSID7dot11gssociatedMACCount,
       "onSSID7dot11gErrorFrameRate": onSSID7dot11gErrorFrameRate,
       "on11gSSID7dot3ErrorFrameRate": on11gSSID7dot3ErrorFrameRate,
       "onSSID7dot11gWirelessUsage": onSSID7dot11gWirelessUsage,
       "systemLog": systemLog,
       "systemLogSystemLevel": systemLogSystemLevel,
       "systemLogWirelessLevel": systemLogWirelessLevel,
       "systemLogNoticeLevel": systemLogNoticeLevel,
       "systemLogTFTPServerIPAddress": systemLogTFTPServerIPAddress,
       "systemLogFileName": systemLogFileName,
       "systemLogGetLog": systemLogGetLog,
       "systemLogLocalLogState": systemLogLocalLogState,
       "systemLogRemoteLogState": systemLogRemoteLogState,
       "systemLogServerIPAddress": systemLogServerIPAddress,
       "systemLogClearLocalLog": systemLogClearLocalLog,
       "traps": traps,
       "trapsNotify": trapsNotify,
       "trapSSHLogin": trapSSHLogin,
       "trapWebLogin": trapWebLogin,
       "trapTelLogin": trapTelLogin,
       "trapCPULoad": trapCPULoad,
       "trapMEMPoor": trapMEMPoor,
       "trapAuthFail": trapAuthFail,
       "trapWirelessLinkUP": trapWirelessLinkUP,
       "trapDeAuthAttack": trapDeAuthAttack,
       "trapDeAssocAttack": trapDeAssocAttack,
       "trapBCastAttack": trapBCastAttack,
       "trapWebLogout": trapWebLogout,
       "trapFWUpdate": trapFWUpdate,
       "trapWirelessLinkDown": trapWirelessLinkDown,
       "trapSTALinkUP": trapSTALinkUP,
       "trapSTALinkDown": trapSTALinkDown,
       "trapsNotifyBiding": trapsNotifyBiding,
       "trapAPMACaddr": trapAPMACaddr,
       "trapSTAMACaddr": trapSTAMACaddr,
       "trapAlarmLevel": trapAlarmLevel,
       "trapPCIPAddr": trapPCIPAddr,
       "swNotiResult": swNotiResult,
       "trapBand": trapBand,
       "miscellaneous": miscellaneous,
       "compatible": compatible,
       "compatibleTable": compatibleTable,
       "compatibleEntry": compatibleEntry,
       "apmodes": apmodes,
       "turbomodes": turbomodes,
       "aclnumber": aclnumber,
       "xrsupported": xrsupported,
       "codebase": codebase,
       "countrycode": countrycode,
       "clientinfosupported": clientinfosupported,
       "singlefirmware": singlefirmware,
       "mssidsupported": mssidsupported,
       "rogueapsupported": rogueapsupported,
       "syslogsupported": syslogsupported,
       "wmmsupported": wmmsupported,
       "mssidisolatedsecurity": mssidisolatedsecurity,
       "mssidindication": mssidindication,
       "keytypeselection": keytypeselection,
       "clustersupported": clustersupported,
       "greenpacketsupported": greenpacketsupported,
       "sshsupported": sshsupported,
       "wdschannellist": wdschannellist,
       "mSSIDSuppress": mSSIDSuppress,
       "antennasupported": antennasupported,
       "vlan": vlan,
       "bgmodesupported": bgmodesupported,
       "wdssitesurvey": wdssitesurvey,
       "accounting": accounting,
       "mssidaccounting": mssidaccounting,
       "mSSIDWmmSupported": mSSIDWmmSupported,
       "sMTPSupported": sMTPSupported,
       "dfsSupported": dfsSupported,
       "wmmOverWDSSupported": wmmOverWDSSupported,
       "priorityBySsidSupported": priorityBySsidSupported}
)
