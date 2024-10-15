# SNMP MIB module (DAP-3520-v115) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DAP-3520-v115
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:55 2024
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
_Dlink_dapfamily_ObjectIdentity = ObjectIdentity
dlink_dapfamily = _Dlink_dapfamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37)
)
_Dap3520_ObjectIdentity = ObjectIdentity
dap3520 = _Dap3520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37)
)
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2)
)
_Lan_ObjectIdentity = ObjectIdentity
lan = _Lan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1)
)
_LanIfSetting_ObjectIdentity = ObjectIdentity
lanIfSetting = _LanIfSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 1)
)
_LanIfSettingTable_Object = MibTable
lanIfSettingTable = _LanIfSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lanIfSettingTable.setStatus("mandatory")
_LanIfSettingEntry_Object = MibTableRow
lanIfSettingEntry = _LanIfSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 1, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 1, 1, 1, 1),
    _LanIfGetIpAddressFrom_Type()
)
lanIfGetIpAddressFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIfGetIpAddressFrom.setStatus("mandatory")
_LanIfIpAddress_Type = IpAddress
_LanIfIpAddress_Object = MibTableColumn
lanIfIpAddress = _LanIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 1, 1, 1, 2),
    _LanIfIpAddress_Type()
)
lanIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIfIpAddress.setStatus("mandatory")
_LanIfSubnetMask_Type = IpAddress
_LanIfSubnetMask_Object = MibTableColumn
lanIfSubnetMask = _LanIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 1, 1, 1, 3),
    _LanIfSubnetMask_Type()
)
lanIfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIfSubnetMask.setStatus("mandatory")
_LanIfDefaultGateway_Type = IpAddress
_LanIfDefaultGateway_Object = MibTableColumn
lanIfDefaultGateway = _LanIfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 1, 1, 1, 4),
    _LanIfDefaultGateway_Type()
)
lanIfDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIfDefaultGateway.setStatus("mandatory")
_LanIfMacAddress_Type = MacAddress
_LanIfMacAddress_Object = MibTableColumn
lanIfMacAddress = _LanIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 1, 1, 1, 5),
    _LanIfMacAddress_Type()
)
lanIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanIfMacAddress.setStatus("mandatory")
_LanIfPrimaryDNS_Type = IpAddress
_LanIfPrimaryDNS_Object = MibTableColumn
lanIfPrimaryDNS = _LanIfPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 1, 1, 1, 6),
    _LanIfPrimaryDNS_Type()
)
lanIfPrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIfPrimaryDNS.setStatus("mandatory")
_LanIfSecondaryDNS_Type = IpAddress
_LanIfSecondaryDNS_Object = MibTableColumn
lanIfSecondaryDNS = _LanIfSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 1, 1, 1, 7),
    _LanIfSecondaryDNS_Type()
)
lanIfSecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIfSecondaryDNS.setStatus("mandatory")
_Wirelesslan_ObjectIdentity = ObjectIdentity
wirelesslan = _Wirelesslan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3)
)
_WirelessLanIfNumber_Type = Integer32
_WirelessLanIfNumber_Object = MibScalar
wirelessLanIfNumber = _WirelessLanIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 1),
    _WirelessLanIfNumber_Type()
)
wirelessLanIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLanIfNumber.setStatus("mandatory")
_WirelessLanIfTable_Object = MibTable
wirelessLanIfTable = _WirelessLanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wirelessLanIfTable.setStatus("mandatory")
_WirelessLanIfEntry_Object = MibTableRow
wirelessLanIfEntry = _WirelessLanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 2, 1)
)
wirelessLanIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wirelessLanIfEntry.setStatus("mandatory")
_WirelessLanIfDesc_Type = OctetString
_WirelessLanIfDesc_Object = MibTableColumn
wirelessLanIfDesc = _WirelessLanIfDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 2, 1, 1),
    _WirelessLanIfDesc_Type()
)
wirelessLanIfDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessLanIfDesc.setStatus("mandatory")
_WirelessLanIfObjectID_Type = ObjectIdentifier
_WirelessLanIfObjectID_Object = MibTableColumn
wirelessLanIfObjectID = _WirelessLanIfObjectID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 2, 1, 2),
    _WirelessLanIfObjectID_Type()
)
wirelessLanIfObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLanIfObjectID.setStatus("mandatory")
_Ieee802dot11_ObjectIdentity = ObjectIdentity
ieee802dot11 = _Ieee802dot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3)
)
_Dot11Parameters_ObjectIdentity = ObjectIdentity
dot11Parameters = _Dot11Parameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1)
)
_Dot11ParametersTable_Object = MibTable
dot11ParametersTable = _Dot11ParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dot11ParametersTable.setStatus("mandatory")
_Dot11ParametersEntry_Object = MibTableRow
dot11ParametersEntry = _Dot11ParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1)
)
dot11ParametersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11ParametersEntry.setStatus("mandatory")
_Dot11Ssid_Type = OctetString
_Dot11Ssid_Object = MibTableColumn
dot11Ssid = _Dot11Ssid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 2),
    _Dot11SsidBroadcast_Type()
)
dot11SsidBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SsidBroadcast.setStatus("mandatory")
_Dot11Channel_Type = Integer32
_Dot11Channel_Object = MibTableColumn
dot11Channel = _Dot11Channel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 3),
    _Dot11Channel_Type()
)
dot11Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Channel.setStatus("mandatory")
_Dot11ChannelList_Type = OctetString
_Dot11ChannelList_Object = MibTableColumn
dot11ChannelList = _Dot11ChannelList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 4),
    _Dot11ChannelList_Type()
)
dot11ChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ChannelList.setStatus("mandatory")
_Dot11Frequency_Type = OctetString
_Dot11Frequency_Object = MibTableColumn
dot11Frequency = _Dot11Frequency_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 10),
    _Dot11Frequency_Type()
)
dot11Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11Frequency.setStatus("mandatory")
_Dot11DataRate_Type = OctetString
_Dot11DataRate_Object = MibTableColumn
dot11DataRate = _Dot11DataRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 11),
    _Dot11DataRate_Type()
)
dot11DataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DataRate.setStatus("mandatory")


class _Dot11WifiMode_Type(Integer32):
    """Custom type dot11WifiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("band2dot4-bg", 3),
          ("band2dot4-bgn", 6),
          ("band2dot4-n", 2),
          ("band5-a", 7),
          ("band5-an", 9),
          ("band5-n", 8))
    )


_Dot11WifiMode_Type.__name__ = "Integer32"
_Dot11WifiMode_Object = MibTableColumn
dot11WifiMode = _Dot11WifiMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 16),
    _Dot11WifiMode_Type()
)
dot11WifiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WifiMode.setStatus("mandatory")


class _Dot11BeaconInterval_Type(Integer32):
    """Custom type dot11BeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 200),
    )


_Dot11BeaconInterval_Type.__name__ = "Integer32"
_Dot11BeaconInterval_Object = MibTableColumn
dot11BeaconInterval = _Dot11BeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 17),
    _Dot11BeaconInterval_Type()
)
dot11BeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11BeaconInterval.setStatus("mandatory")


class _Dot11Dtim_Type(Integer32):
    """Custom type dot11Dtim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Dot11Dtim_Type.__name__ = "Integer32"
_Dot11Dtim_Object = MibTableColumn
dot11Dtim = _Dot11Dtim_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 18),
    _Dot11Dtim_Type()
)
dot11Dtim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Dtim.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 21),
    _Dot11TransmitPower_Type()
)
dot11TransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11TransmitPower.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 25),
    _Dot11Wmm_Type()
)
dot11Wmm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Wmm.setStatus("mandatory")


class _Dot11ApMode_Type(Integer32):
    """Custom type dot11ApMode based on Integer32"""
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
        *(("ap", 1),
          ("wdsWithAp", 2),
          ("wdsWithoutAp", 3),
          ("wirelessClient", 4))
    )


_Dot11ApMode_Type.__name__ = "Integer32"
_Dot11ApMode_Object = MibTableColumn
dot11ApMode = _Dot11ApMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 28),
    _Dot11ApMode_Type()
)
dot11ApMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ApMode.setStatus("mandatory")


class _Dot11ChannelWidth_Type(Integer32):
    """Custom type dot11ChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cwm20MHz", 1),
          ("cwmAuto", 2))
    )


_Dot11ChannelWidth_Type.__name__ = "Integer32"
_Dot11ChannelWidth_Object = MibTableColumn
dot11ChannelWidth = _Dot11ChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 29),
    _Dot11ChannelWidth_Type()
)
dot11ChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ChannelWidth.setStatus("mandatory")
_Dot11DataRateList_Type = OctetString
_Dot11DataRateList_Object = MibTableColumn
dot11DataRateList = _Dot11DataRateList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 30),
    _Dot11DataRateList_Type()
)
dot11DataRateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DataRateList.setStatus("mandatory")
_Dot11AckTimeout_Type = Integer32
_Dot11AckTimeout_Object = MibTableColumn
dot11AckTimeout = _Dot11AckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 31),
    _Dot11AckTimeout_Type()
)
dot11AckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AckTimeout.setStatus("mandatory")


class _Dot11ShortGI_Type(Integer32):
    """Custom type dot11ShortGI based on Integer32"""
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


_Dot11ShortGI_Type.__name__ = "Integer32"
_Dot11ShortGI_Object = MibTableColumn
dot11ShortGI = _Dot11ShortGI_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 32),
    _Dot11ShortGI_Type()
)
dot11ShortGI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ShortGI.setStatus("mandatory")


class _Dot11Igmpsnooping_Type(Integer32):
    """Custom type dot11Igmpsnooping based on Integer32"""
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


_Dot11Igmpsnooping_Type.__name__ = "Integer32"
_Dot11Igmpsnooping_Object = MibTableColumn
dot11Igmpsnooping = _Dot11Igmpsnooping_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 33),
    _Dot11Igmpsnooping_Type()
)
dot11Igmpsnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Igmpsnooping.setStatus("mandatory")


class _Dot11Band_Type(Integer32):
    """Custom type dot11Band based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("band2dot4gHz", 0),
          ("band5gHz", 1))
    )


_Dot11Band_Type.__name__ = "Integer32"
_Dot11Band_Object = MibTableColumn
dot11Band = _Dot11Band_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 34),
    _Dot11Band_Type()
)
dot11Band.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Band.setStatus("mandatory")
_Dot11Band5GHzDataRateList_Type = OctetString
_Dot11Band5GHzDataRateList_Object = MibTableColumn
dot11Band5GHzDataRateList = _Dot11Band5GHzDataRateList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 35),
    _Dot11Band5GHzDataRateList_Type()
)
dot11Band5GHzDataRateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11Band5GHzDataRateList.setStatus("mandatory")
_Dot11Band5GHzWdsChannelList_Type = OctetString
_Dot11Band5GHzWdsChannelList_Object = MibTableColumn
dot11Band5GHzWdsChannelList = _Dot11Band5GHzWdsChannelList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 36),
    _Dot11Band5GHzWdsChannelList_Type()
)
dot11Band5GHzWdsChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11Band5GHzWdsChannelList.setStatus("mandatory")
_Dot11Band5GHzChannelList_Type = OctetString
_Dot11Band5GHzChannelList_Object = MibTableColumn
dot11Band5GHzChannelList = _Dot11Band5GHzChannelList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 37),
    _Dot11Band5GHzChannelList_Type()
)
dot11Band5GHzChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11Band5GHzChannelList.setStatus("mandatory")
_Dot11ApModeStatus_Type = OctetString
_Dot11ApModeStatus_Object = MibTableColumn
dot11ApModeStatus = _Dot11ApModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 38),
    _Dot11ApModeStatus_Type()
)
dot11ApModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ApModeStatus.setStatus("mandatory")
_Dot11Countrycode_Type = OctetString
_Dot11Countrycode_Object = MibTableColumn
dot11Countrycode = _Dot11Countrycode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 39),
    _Dot11Countrycode_Type()
)
dot11Countrycode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11Countrycode.setStatus("mandatory")


class _Dot11Application_Type(Integer32):
    """Custom type dot11Application based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("indoor", 1),
          ("outdoor", 2))
    )


_Dot11Application_Type.__name__ = "Integer32"
_Dot11Application_Object = MibTableColumn
dot11Application = _Dot11Application_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 40),
    _Dot11Application_Type()
)
dot11Application.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Application.setStatus("mandatory")
_Dot11Band5GHzOutdoorChannelList_Type = OctetString
_Dot11Band5GHzOutdoorChannelList_Object = MibTableColumn
dot11Band5GHzOutdoorChannelList = _Dot11Band5GHzOutdoorChannelList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 41),
    _Dot11Band5GHzOutdoorChannelList_Type()
)
dot11Band5GHzOutdoorChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11Band5GHzOutdoorChannelList.setStatus("mandatory")
_Dot11MulticastRateABandList_Type = OctetString
_Dot11MulticastRateABandList_Object = MibTableColumn
dot11MulticastRateABandList = _Dot11MulticastRateABandList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 42),
    _Dot11MulticastRateABandList_Type()
)
dot11MulticastRateABandList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MulticastRateABandList.setStatus("mandatory")
_Dot11MulticastRateGBandList_Type = OctetString
_Dot11MulticastRateGBandList_Object = MibTableColumn
dot11MulticastRateGBandList = _Dot11MulticastRateGBandList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 43),
    _Dot11MulticastRateGBandList_Type()
)
dot11MulticastRateGBandList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MulticastRateGBandList.setStatus("mandatory")
_Dot11MulticastRateABand_Type = OctetString
_Dot11MulticastRateABand_Object = MibTableColumn
dot11MulticastRateABand = _Dot11MulticastRateABand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 44),
    _Dot11MulticastRateABand_Type()
)
dot11MulticastRateABand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MulticastRateABand.setStatus("mandatory")
_Dot11MulticastRateGBand_Type = OctetString
_Dot11MulticastRateGBand_Object = MibTableColumn
dot11MulticastRateGBand = _Dot11MulticastRateGBand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 45),
    _Dot11MulticastRateGBand_Type()
)
dot11MulticastRateGBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MulticastRateGBand.setStatus("mandatory")


class _Dot11HT2040Coexistence_Type(Integer32):
    """Custom type dot11HT2040Coexistence based on Integer32"""
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


_Dot11HT2040Coexistence_Type.__name__ = "Integer32"
_Dot11HT2040Coexistence_Object = MibTableColumn
dot11HT2040Coexistence = _Dot11HT2040Coexistence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 1, 1, 49),
    _Dot11HT2040Coexistence_Type()
)
dot11HT2040Coexistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11HT2040Coexistence.setStatus("mandatory")
_Dot11RemoteApMacAddress_ObjectIdentity = ObjectIdentity
dot11RemoteApMacAddress = _Dot11RemoteApMacAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 2)
)
_Dot11RemoteApMacAddressTable_Object = MibTable
dot11RemoteApMacAddressTable = _Dot11RemoteApMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot11RemoteApMacAddressTable.setStatus("mandatory")
_Dot11RemoteApMacAddressEntry_Object = MibTableRow
dot11RemoteApMacAddressEntry = _Dot11RemoteApMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 2, 1, 1)
)
dot11RemoteApMacAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DAP-3520-v115", "dot11RemoteApMacAddressIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 2, 1, 1, 1),
    _Dot11RemoteApMacAddressIndex_Type()
)
dot11RemoteApMacAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11RemoteApMacAddressIndex.setStatus("mandatory")
_Dot11RemoteApMacAddressList_Type = MacAddress
_Dot11RemoteApMacAddressList_Object = MibTableColumn
dot11RemoteApMacAddressList = _Dot11RemoteApMacAddressList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 2, 1, 1, 2),
    _Dot11RemoteApMacAddressList_Type()
)
dot11RemoteApMacAddressList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RemoteApMacAddressList.setStatus("mandatory")
_Dot11RemoteApMacAddressAccessTable_Object = MibTable
dot11RemoteApMacAddressAccessTable = _Dot11RemoteApMacAddressAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot11RemoteApMacAddressAccessTable.setStatus("mandatory")
_Dot11RemoteApMacAddressAccessEntry_Object = MibTableRow
dot11RemoteApMacAddressAccessEntry = _Dot11RemoteApMacAddressAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 2, 2, 1)
)
dot11RemoteApMacAddressAccessEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11RemoteApMacAddressAccessEntry.setStatus("mandatory")
_Dot11RemoteApMacAddressAdd_Type = MacAddress
_Dot11RemoteApMacAddressAdd_Object = MibTableColumn
dot11RemoteApMacAddressAdd = _Dot11RemoteApMacAddressAdd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 2, 2, 1, 1),
    _Dot11RemoteApMacAddressAdd_Type()
)
dot11RemoteApMacAddressAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RemoteApMacAddressAdd.setStatus("mandatory")
_Dot11RemoteApMacAddressDelete_Type = MacAddress
_Dot11RemoteApMacAddressDelete_Object = MibTableColumn
dot11RemoteApMacAddressDelete = _Dot11RemoteApMacAddressDelete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 2, 2, 1, 2),
    _Dot11RemoteApMacAddressDelete_Type()
)
dot11RemoteApMacAddressDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RemoteApMacAddressDelete.setStatus("mandatory")


class _Dot11RemoteApMacAddressDeleteAll_Type(Integer32):
    """Custom type dot11RemoteApMacAddressDeleteAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deleteall", 1),
          ("nothing", 0))
    )


_Dot11RemoteApMacAddressDeleteAll_Type.__name__ = "Integer32"
_Dot11RemoteApMacAddressDeleteAll_Object = MibTableColumn
dot11RemoteApMacAddressDeleteAll = _Dot11RemoteApMacAddressDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 2, 2, 1, 3),
    _Dot11RemoteApMacAddressDeleteAll_Type()
)
dot11RemoteApMacAddressDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RemoteApMacAddressDeleteAll.setStatus("mandatory")
_Dot11SiteSurvey_ObjectIdentity = ObjectIdentity
dot11SiteSurvey = _Dot11SiteSurvey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3)
)
_Dot11SiteSurveyRefreshTable_Object = MibTable
dot11SiteSurveyRefreshTable = _Dot11SiteSurveyRefreshTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot11SiteSurveyRefreshTable.setStatus("mandatory")
_Dot11SiteSurveyRefreshEntry_Object = MibTableRow
dot11SiteSurveyRefreshEntry = _Dot11SiteSurveyRefreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 1, 1, 1),
    _Dot11SiteSurveyRefresh_Type()
)
dot11SiteSurveyRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SiteSurveyRefresh.setStatus("mandatory")
_Dot11SiteSurveyTable_Object = MibTable
dot11SiteSurveyTable = _Dot11SiteSurveyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dot11SiteSurveyTable.setStatus("mandatory")
_Dot11SiteSurveyEntry_Object = MibTableRow
dot11SiteSurveyEntry = _Dot11SiteSurveyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 2, 1)
)
dot11SiteSurveyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DAP-3520-v115", "dot11SiteSurveyIndex"),
)
if mibBuilder.loadTexts:
    dot11SiteSurveyEntry.setStatus("mandatory")
_Dot11SiteSurveyIndex_Type = Integer32
_Dot11SiteSurveyIndex_Object = MibTableColumn
dot11SiteSurveyIndex = _Dot11SiteSurveyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 2, 1, 1),
    _Dot11SiteSurveyIndex_Type()
)
dot11SiteSurveyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11SiteSurveyIndex.setStatus("mandatory")
_Dot11SiteSurveyBssType_Type = OctetString
_Dot11SiteSurveyBssType_Object = MibTableColumn
dot11SiteSurveyBssType = _Dot11SiteSurveyBssType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 2, 1, 2),
    _Dot11SiteSurveyBssType_Type()
)
dot11SiteSurveyBssType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveyBssType.setStatus("mandatory")
_Dot11SiteSurveyChannel_Type = Integer32
_Dot11SiteSurveyChannel_Object = MibTableColumn
dot11SiteSurveyChannel = _Dot11SiteSurveyChannel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 2, 1, 3),
    _Dot11SiteSurveyChannel_Type()
)
dot11SiteSurveyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveyChannel.setStatus("mandatory")
_Dot11SiteSurveyRssi_Type = Integer32
_Dot11SiteSurveyRssi_Object = MibTableColumn
dot11SiteSurveyRssi = _Dot11SiteSurveyRssi_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 2, 1, 4),
    _Dot11SiteSurveyRssi_Type()
)
dot11SiteSurveyRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveyRssi.setStatus("mandatory")
_Dot11SiteSurveyBssid_Type = MacAddress
_Dot11SiteSurveyBssid_Object = MibTableColumn
dot11SiteSurveyBssid = _Dot11SiteSurveyBssid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 2, 1, 5),
    _Dot11SiteSurveyBssid_Type()
)
dot11SiteSurveyBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveyBssid.setStatus("mandatory")
_Dot11SiteSurveyEncryption_Type = OctetString
_Dot11SiteSurveyEncryption_Object = MibTableColumn
dot11SiteSurveyEncryption = _Dot11SiteSurveyEncryption_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 3, 2, 1, 7),
    _Dot11SiteSurveySsid_Type()
)
dot11SiteSurveySsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SiteSurveySsid.setStatus("mandatory")
_Dot11WdsSiteSurvey_ObjectIdentity = ObjectIdentity
dot11WdsSiteSurvey = _Dot11WdsSiteSurvey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4)
)
_Dot11WdsSiteSurveyRefreshTable_Object = MibTable
dot11WdsSiteSurveyRefreshTable = _Dot11WdsSiteSurveyRefreshTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dot11WdsSiteSurveyRefreshTable.setStatus("mandatory")
_Dot11WdsSiteSurveyRefreshEntry_Object = MibTableRow
dot11WdsSiteSurveyRefreshEntry = _Dot11WdsSiteSurveyRefreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4, 1, 1)
)
dot11WdsSiteSurveyRefreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11WdsSiteSurveyRefreshEntry.setStatus("mandatory")


class _Dot11WdsSiteSurveyRefresh_Type(Integer32):
    """Custom type dot11WdsSiteSurveyRefresh based on Integer32"""
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


_Dot11WdsSiteSurveyRefresh_Type.__name__ = "Integer32"
_Dot11WdsSiteSurveyRefresh_Object = MibTableColumn
dot11WdsSiteSurveyRefresh = _Dot11WdsSiteSurveyRefresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4, 1, 1, 1),
    _Dot11WdsSiteSurveyRefresh_Type()
)
dot11WdsSiteSurveyRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WdsSiteSurveyRefresh.setStatus("mandatory")
_Dot11WdsSiteSurveyTable_Object = MibTable
dot11WdsSiteSurveyTable = _Dot11WdsSiteSurveyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dot11WdsSiteSurveyTable.setStatus("mandatory")
_Dot11WdsSiteSurveyEntry_Object = MibTableRow
dot11WdsSiteSurveyEntry = _Dot11WdsSiteSurveyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4, 2, 1)
)
dot11WdsSiteSurveyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DAP-3520-v115", "dot11WdsSiteSurveyIndex"),
)
if mibBuilder.loadTexts:
    dot11WdsSiteSurveyEntry.setStatus("mandatory")
_Dot11WdsSiteSurveyIndex_Type = Integer32
_Dot11WdsSiteSurveyIndex_Object = MibTableColumn
dot11WdsSiteSurveyIndex = _Dot11WdsSiteSurveyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4, 2, 1, 1),
    _Dot11WdsSiteSurveyIndex_Type()
)
dot11WdsSiteSurveyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11WdsSiteSurveyIndex.setStatus("mandatory")
_Dot11WdsSiteSurveyChannel_Type = Integer32
_Dot11WdsSiteSurveyChannel_Object = MibTableColumn
dot11WdsSiteSurveyChannel = _Dot11WdsSiteSurveyChannel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4, 2, 1, 2),
    _Dot11WdsSiteSurveyChannel_Type()
)
dot11WdsSiteSurveyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsSiteSurveyChannel.setStatus("mandatory")
_Dot11WdsSiteSurveyMode_Type = Integer32
_Dot11WdsSiteSurveyMode_Object = MibTableColumn
dot11WdsSiteSurveyMode = _Dot11WdsSiteSurveyMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4, 2, 1, 3),
    _Dot11WdsSiteSurveyMode_Type()
)
dot11WdsSiteSurveyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsSiteSurveyMode.setStatus("mandatory")
_Dot11WdsSiteSurveyBssid_Type = MacAddress
_Dot11WdsSiteSurveyBssid_Object = MibTableColumn
dot11WdsSiteSurveyBssid = _Dot11WdsSiteSurveyBssid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4, 2, 1, 4),
    _Dot11WdsSiteSurveyBssid_Type()
)
dot11WdsSiteSurveyBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsSiteSurveyBssid.setStatus("mandatory")
_Dot11WdsSiteSurveyEncryption_Type = OctetString
_Dot11WdsSiteSurveyEncryption_Object = MibTableColumn
dot11WdsSiteSurveyEncryption = _Dot11WdsSiteSurveyEncryption_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4, 2, 1, 5),
    _Dot11WdsSiteSurveyEncryption_Type()
)
dot11WdsSiteSurveyEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsSiteSurveyEncryption.setStatus("mandatory")


class _Dot11WdsSiteSurveySsid_Type(OctetString):
    """Custom type dot11WdsSiteSurveySsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11WdsSiteSurveySsid_Type.__name__ = "OctetString"
_Dot11WdsSiteSurveySsid_Object = MibTableColumn
dot11WdsSiteSurveySsid = _Dot11WdsSiteSurveySsid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 1, 4, 2, 1, 6),
    _Dot11WdsSiteSurveySsid_Type()
)
dot11WdsSiteSurveySsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsSiteSurveySsid.setStatus("mandatory")
_Dot11Securities_ObjectIdentity = ObjectIdentity
dot11Securities = _Dot11Securities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2)
)
_Dot11SecuritiesTable_Object = MibTable
dot11SecuritiesTable = _Dot11SecuritiesTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dot11SecuritiesTable.setStatus("mandatory")
_Dot11SecuritiesEntry_Object = MibTableRow
dot11SecuritiesEntry = _Dot11SecuritiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1)
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 10),
          ("opensystem", 1),
          ("opensystem-sharedkey", 3),
          ("sharedkey", 2),
          ("wpa-eap", 5),
          ("wpa-psk", 4),
          ("wpa2-auto-eap", 9),
          ("wpa2-auto-psk", 8),
          ("wpa2-eap", 7),
          ("wpa2-psk", 6))
    )


_Dot11Authentication_Type.__name__ = "Integer32"
_Dot11Authentication_Object = MibTableColumn
dot11Authentication = _Dot11Authentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 4),
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
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("auto", 1),
          ("tkip", 3),
          ("wep", 4))
    )


_Dot11CipherType_Type.__name__ = "Integer32"
_Dot11CipherType_Object = MibTableColumn
dot11CipherType = _Dot11CipherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 6),
    _Dot11GroupKeyUpdateInterval_Type()
)
dot11GroupKeyUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupKeyUpdateInterval.setStatus("mandatory")
_Dot11PrimaryRadiusServer_Type = IpAddress
_Dot11PrimaryRadiusServer_Object = MibTableColumn
dot11PrimaryRadiusServer = _Dot11PrimaryRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 8),
    _Dot11PrimaryRadiusServer_Type()
)
dot11PrimaryRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PrimaryRadiusServer.setStatus("mandatory")


class _Dot11PrimaryRadiusPort_Type(Integer32):
    """Custom type dot11PrimaryRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11PrimaryRadiusPort_Type.__name__ = "Integer32"
_Dot11PrimaryRadiusPort_Object = MibTableColumn
dot11PrimaryRadiusPort = _Dot11PrimaryRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 9),
    _Dot11PrimaryRadiusPort_Type()
)
dot11PrimaryRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PrimaryRadiusPort.setStatus("mandatory")


class _Dot11PrimaryRadiusSecret_Type(OctetString):
    """Custom type dot11PrimaryRadiusSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11PrimaryRadiusSecret_Type.__name__ = "OctetString"
_Dot11PrimaryRadiusSecret_Object = MibTableColumn
dot11PrimaryRadiusSecret = _Dot11PrimaryRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 10),
    _Dot11PrimaryRadiusSecret_Type()
)
dot11PrimaryRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PrimaryRadiusSecret.setStatus("mandatory")


class _Dot11NetworkAccessProtection_Type(Integer32):
    """Custom type dot11NetworkAccessProtection based on Integer32"""
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


_Dot11NetworkAccessProtection_Type.__name__ = "Integer32"
_Dot11NetworkAccessProtection_Object = MibTableColumn
dot11NetworkAccessProtection = _Dot11NetworkAccessProtection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 22),
    _Dot11NetworkAccessProtection_Type()
)
dot11NetworkAccessProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11NetworkAccessProtection.setStatus("mandatory")


class _Dot11RadiusKeyUpdateInterval_Type(Integer32):
    """Custom type dot11RadiusKeyUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 9999999),
    )


_Dot11RadiusKeyUpdateInterval_Type.__name__ = "Integer32"
_Dot11RadiusKeyUpdateInterval_Object = MibTableColumn
dot11RadiusKeyUpdateInterval = _Dot11RadiusKeyUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 24),
    _Dot11RadiusKeyUpdateInterval_Type()
)
dot11RadiusKeyUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RadiusKeyUpdateInterval.setStatus("mandatory")


class _Dot11WpaEapType_Type(Integer32):
    """Custom type dot11WpaEapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("peap", 2),
          ("ttls", 1))
    )


_Dot11WpaEapType_Type.__name__ = "Integer32"
_Dot11WpaEapType_Object = MibTableColumn
dot11WpaEapType = _Dot11WpaEapType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 25),
    _Dot11WpaEapType_Type()
)
dot11WpaEapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WpaEapType.setStatus("mandatory")


class _Dot11WpaEapAuthenticationType_Type(Integer32):
    """Custom type dot11WpaEapAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("chap", 4),
          ("mschapv2", 2),
          ("pap", 3))
    )


_Dot11WpaEapAuthenticationType_Type.__name__ = "Integer32"
_Dot11WpaEapAuthenticationType_Object = MibTableColumn
dot11WpaEapAuthenticationType = _Dot11WpaEapAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 26),
    _Dot11WpaEapAuthenticationType_Type()
)
dot11WpaEapAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WpaEapAuthenticationType.setStatus("mandatory")
_Dot11WpaEapUsername_Type = OctetString
_Dot11WpaEapUsername_Object = MibTableColumn
dot11WpaEapUsername = _Dot11WpaEapUsername_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 27),
    _Dot11WpaEapUsername_Type()
)
dot11WpaEapUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WpaEapUsername.setStatus("mandatory")
_Dot11WpaEapPasswd_Type = OctetString
_Dot11WpaEapPasswd_Object = MibTableColumn
dot11WpaEapPasswd = _Dot11WpaEapPasswd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 28),
    _Dot11WpaEapPasswd_Type()
)
dot11WpaEapPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WpaEapPasswd.setStatus("mandatory")


class _Dot11AutoRekeyControl_Type(Integer32):
    """Custom type dot11AutoRekeyControl based on Integer32"""
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


_Dot11AutoRekeyControl_Type.__name__ = "Integer32"
_Dot11AutoRekeyControl_Object = MibTableColumn
dot11AutoRekeyControl = _Dot11AutoRekeyControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 29),
    _Dot11AutoRekeyControl_Type()
)
dot11AutoRekeyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AutoRekeyControl.setStatus("mandatory")


class _Dot11AutoRekeyStartWeek_Type(Integer32):
    """Custom type dot11AutoRekeyStartWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fri", 5),
          ("mon", 1),
          ("sat", 6),
          ("sun", 0),
          ("thu", 4),
          ("tue", 2),
          ("wed", 3))
    )


_Dot11AutoRekeyStartWeek_Type.__name__ = "Integer32"
_Dot11AutoRekeyStartWeek_Object = MibTableColumn
dot11AutoRekeyStartWeek = _Dot11AutoRekeyStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 30),
    _Dot11AutoRekeyStartWeek_Type()
)
dot11AutoRekeyStartWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AutoRekeyStartWeek.setStatus("mandatory")
_Dot11AutoRekeyStartTime_Type = OctetString
_Dot11AutoRekeyStartTime_Object = MibTableColumn
dot11AutoRekeyStartTime = _Dot11AutoRekeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 31),
    _Dot11AutoRekeyStartTime_Type()
)
dot11AutoRekeyStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AutoRekeyStartTime.setStatus("mandatory")


class _Dot11AutoRekeyTimeInterval_Type(Integer32):
    """Custom type dot11AutoRekeyTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 168),
    )


_Dot11AutoRekeyTimeInterval_Type.__name__ = "Integer32"
_Dot11AutoRekeyTimeInterval_Object = MibTableColumn
dot11AutoRekeyTimeInterval = _Dot11AutoRekeyTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 32),
    _Dot11AutoRekeyTimeInterval_Type()
)
dot11AutoRekeyTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AutoRekeyTimeInterval.setStatus("mandatory")
_Dot11AutoRekeyPassPhrase_Type = OctetString
_Dot11AutoRekeyPassPhrase_Object = MibTableColumn
dot11AutoRekeyPassPhrase = _Dot11AutoRekeyPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 1, 1, 33),
    _Dot11AutoRekeyPassPhrase_Type()
)
dot11AutoRekeyPassPhrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11AutoRekeyPassPhrase.setStatus("mandatory")
_Dot11WepKeyTable_Object = MibTable
dot11WepKeyTable = _Dot11WepKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    dot11WepKeyTable.setStatus("mandatory")
_Dot11WepKeyEntry_Object = MibTableRow
dot11WepKeyEntry = _Dot11WepKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 2, 1)
)
dot11WepKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DAP-3520-v115", "dot11wepKeyIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 2, 1, 1),
    _Dot11wepKeyIndex_Type()
)
dot11wepKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11wepKeyIndex.setStatus("mandatory")


class _Dot11WepKeyEntryMethod_Type(Integer32):
    """Custom type dot11WepKeyEntryMethod based on Integer32"""
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


_Dot11WepKeyEntryMethod_Type.__name__ = "Integer32"
_Dot11WepKeyEntryMethod_Object = MibTableColumn
dot11WepKeyEntryMethod = _Dot11WepKeyEntryMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 2, 1, 2),
    _Dot11WepKeyEntryMethod_Type()
)
dot11WepKeyEntryMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WepKeyEntryMethod.setStatus("mandatory")
_Dot11WepKey_Type = OctetString
_Dot11WepKey_Object = MibTableColumn
dot11WepKey = _Dot11WepKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 2, 1, 3),
    _Dot11WepKey_Type()
)
dot11WepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WepKey.setStatus("mandatory")
_Dot11Filter_ObjectIdentity = ObjectIdentity
dot11Filter = _Dot11Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3)
)
_Dot11PartionTable_Object = MibTable
dot11PartionTable = _Dot11PartionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dot11PartionTable.setStatus("mandatory")
_Dot11PartionEntry_Object = MibTableRow
dot11PartionEntry = _Dot11PartionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 1, 1)
)
dot11PartionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11PartionEntry.setStatus("mandatory")


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
        *(("disable", 0),
          ("enable", 1))
    )


_Dot11EthernetToWlanAccess_Type.__name__ = "Integer32"
_Dot11EthernetToWlanAccess_Object = MibTableColumn
dot11EthernetToWlanAccess = _Dot11EthernetToWlanAccess_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 1, 1, 2),
    _Dot11EthernetToWlanAccess_Type()
)
dot11EthernetToWlanAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11EthernetToWlanAccess.setStatus("mandatory")


class _Dot11InternalStationConnectionPrimarySSID_Type(Integer32):
    """Custom type dot11InternalStationConnectionPrimarySSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0),
          ("guestmode", 2))
    )


_Dot11InternalStationConnectionPrimarySSID_Type.__name__ = "Integer32"
_Dot11InternalStationConnectionPrimarySSID_Object = MibTableColumn
dot11InternalStationConnectionPrimarySSID = _Dot11InternalStationConnectionPrimarySSID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 1, 1, 4),
    _Dot11InternalStationConnectionPrimarySSID_Type()
)
dot11InternalStationConnectionPrimarySSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11InternalStationConnectionPrimarySSID.setStatus("mandatory")


class _Dot11InternalStationConnectionMultiSSID1_Type(Integer32):
    """Custom type dot11InternalStationConnectionMultiSSID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0),
          ("guestmode", 2))
    )


_Dot11InternalStationConnectionMultiSSID1_Type.__name__ = "Integer32"
_Dot11InternalStationConnectionMultiSSID1_Object = MibTableColumn
dot11InternalStationConnectionMultiSSID1 = _Dot11InternalStationConnectionMultiSSID1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 1, 1, 5),
    _Dot11InternalStationConnectionMultiSSID1_Type()
)
dot11InternalStationConnectionMultiSSID1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11InternalStationConnectionMultiSSID1.setStatus("mandatory")


class _Dot11InternalStationConnectionMultiSSID2_Type(Integer32):
    """Custom type dot11InternalStationConnectionMultiSSID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0),
          ("guestmode", 2))
    )


_Dot11InternalStationConnectionMultiSSID2_Type.__name__ = "Integer32"
_Dot11InternalStationConnectionMultiSSID2_Object = MibTableColumn
dot11InternalStationConnectionMultiSSID2 = _Dot11InternalStationConnectionMultiSSID2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 1, 1, 6),
    _Dot11InternalStationConnectionMultiSSID2_Type()
)
dot11InternalStationConnectionMultiSSID2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11InternalStationConnectionMultiSSID2.setStatus("mandatory")


class _Dot11InternalStationConnectionMultiSSID3_Type(Integer32):
    """Custom type dot11InternalStationConnectionMultiSSID3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0),
          ("guestmode", 2))
    )


_Dot11InternalStationConnectionMultiSSID3_Type.__name__ = "Integer32"
_Dot11InternalStationConnectionMultiSSID3_Object = MibTableColumn
dot11InternalStationConnectionMultiSSID3 = _Dot11InternalStationConnectionMultiSSID3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 1, 1, 7),
    _Dot11InternalStationConnectionMultiSSID3_Type()
)
dot11InternalStationConnectionMultiSSID3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11InternalStationConnectionMultiSSID3.setStatus("mandatory")
_Dot11MacAccessControlTable_Object = MibTable
dot11MacAccessControlTable = _Dot11MacAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dot11MacAccessControlTable.setStatus("mandatory")
_Dot11MacAccessControlEntry_Object = MibTableRow
dot11MacAccessControlEntry = _Dot11MacAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 2, 1, 1),
    _Dot11MacAccessControl_Type()
)
dot11MacAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MacAccessControl.setStatus("mandatory")
_Dot11MacAccessControlMacAddressAdd_Type = MacAddress
_Dot11MacAccessControlMacAddressAdd_Object = MibTableColumn
dot11MacAccessControlMacAddressAdd = _Dot11MacAccessControlMacAddressAdd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 2, 1, 2),
    _Dot11MacAccessControlMacAddressAdd_Type()
)
dot11MacAccessControlMacAddressAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MacAccessControlMacAddressAdd.setStatus("mandatory")
_Dot11MacAccessControlMacAddressDelete_Type = MacAddress
_Dot11MacAccessControlMacAddressDelete_Object = MibTableColumn
dot11MacAccessControlMacAddressDelete = _Dot11MacAccessControlMacAddressDelete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 2, 1, 3),
    _Dot11MacAccessControlMacAddressDelete_Type()
)
dot11MacAccessControlMacAddressDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MacAccessControlMacAddressDelete.setStatus("mandatory")
_Dot11MacAccessControlListTable_Object = MibTable
dot11MacAccessControlListTable = _Dot11MacAccessControlListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    dot11MacAccessControlListTable.setStatus("mandatory")
_Dot11MacAccessControlListEntry_Object = MibTableRow
dot11MacAccessControlListEntry = _Dot11MacAccessControlListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 3, 1)
)
dot11MacAccessControlListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DAP-3520-v115", "dot11MacAccessControlListIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 3, 1, 1),
    _Dot11MacAccessControlListIndex_Type()
)
dot11MacAccessControlListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11MacAccessControlListIndex.setStatus("mandatory")
_Dot11MacAccessControlListMacAddress_Type = MacAddress
_Dot11MacAccessControlListMacAddress_Object = MibTableColumn
dot11MacAccessControlListMacAddress = _Dot11MacAccessControlListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 2, 3, 3, 1, 2),
    _Dot11MacAccessControlListMacAddress_Type()
)
dot11MacAccessControlListMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MacAccessControlListMacAddress.setStatus("mandatory")
_Dot11ClientInformation_ObjectIdentity = ObjectIdentity
dot11ClientInformation = _Dot11ClientInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4)
)
_Dot11GetClientInformationTable_Object = MibTable
dot11GetClientInformationTable = _Dot11GetClientInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    dot11GetClientInformationTable.setStatus("mandatory")
_Dot11GetClientInformationEntry_Object = MibTableRow
dot11GetClientInformationEntry = _Dot11GetClientInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 1, 1, 1),
    _Dot11ClientInformationRefresh_Type()
)
dot11ClientInformationRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ClientInformationRefresh.setStatus("mandatory")
_Dot11ClientInformationTable_Object = MibTable
dot11ClientInformationTable = _Dot11ClientInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    dot11ClientInformationTable.setStatus("mandatory")
_Dot11ClientInformationEntry_Object = MibTableRow
dot11ClientInformationEntry = _Dot11ClientInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2, 1)
)
dot11ClientInformationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DAP-3520-v115", "dot11ClientIndex"),
)
if mibBuilder.loadTexts:
    dot11ClientInformationEntry.setStatus("mandatory")
_Dot11ClientIndex_Type = Integer32
_Dot11ClientIndex_Object = MibTableColumn
dot11ClientIndex = _Dot11ClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2, 1, 1),
    _Dot11ClientIndex_Type()
)
dot11ClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11ClientIndex.setStatus("mandatory")
_Dot11ClientMacAddress_Type = MacAddress
_Dot11ClientMacAddress_Object = MibTableColumn
dot11ClientMacAddress = _Dot11ClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2, 1, 2),
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11b", 1),
          ("dot11g", 2),
          ("dot11n", 3))
    )


_Dot11ClientBand_Type.__name__ = "Integer32"
_Dot11ClientBand_Object = MibTableColumn
dot11ClientBand = _Dot11ClientBand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2, 1, 3),
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
        *(("dot1x", 10),
          ("opensystem", 1),
          ("sharedkey", 2),
          ("wep", 11),
          ("wpa-eap", 5),
          ("wpa-psk", 4),
          ("wpa2-auto-eap", 9),
          ("wpa2-auto-psk", 8),
          ("wpa2-eap", 7),
          ("wpa2-psk", 6))
    )


_Dot11ClientAuthentication_Type.__name__ = "Integer32"
_Dot11ClientAuthentication_Object = MibTableColumn
dot11ClientAuthentication = _Dot11ClientAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2, 1, 4),
    _Dot11ClientAuthentication_Type()
)
dot11ClientAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientAuthentication.setStatus("mandatory")
_Dot11ClientRssi_Type = Integer32
_Dot11ClientRssi_Object = MibTableColumn
dot11ClientRssi = _Dot11ClientRssi_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2, 1, 5),
    _Dot11ClientRssi_Type()
)
dot11ClientRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientRssi.setStatus("mandatory")


class _Dot11ClientPsm_Type(Integer32):
    """Custom type dot11ClientPsm based on Integer32"""
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


_Dot11ClientPsm_Type.__name__ = "Integer32"
_Dot11ClientPsm_Object = MibTableColumn
dot11ClientPsm = _Dot11ClientPsm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2, 1, 6),
    _Dot11ClientPsm_Type()
)
dot11ClientPsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientPsm.setStatus("mandatory")
_Dot11SSIDIndex_Type = OctetString
_Dot11SSIDIndex_Object = MibTableColumn
dot11SSIDIndex = _Dot11SSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2, 1, 7),
    _Dot11SSIDIndex_Type()
)
dot11SSIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11SSIDIndex.setStatus("mandatory")
_Dot11ClientIpAddress_Type = IpAddress
_Dot11ClientIpAddress_Object = MibTableColumn
dot11ClientIpAddress = _Dot11ClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2, 1, 10),
    _Dot11ClientIpAddress_Type()
)
dot11ClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientIpAddress.setStatus("mandatory")
_Dot11ClientTxBytesCount_Type = Integer32
_Dot11ClientTxBytesCount_Object = MibTableColumn
dot11ClientTxBytesCount = _Dot11ClientTxBytesCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2, 1, 11),
    _Dot11ClientTxBytesCount_Type()
)
dot11ClientTxBytesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientTxBytesCount.setStatus("mandatory")
_Dot11ClientRxBytesCount_Type = Integer32
_Dot11ClientRxBytesCount_Object = MibTableColumn
dot11ClientRxBytesCount = _Dot11ClientRxBytesCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 4, 2, 1, 12),
    _Dot11ClientRxBytesCount_Type()
)
dot11ClientRxBytesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ClientRxBytesCount.setStatus("mandatory")
_Dot11WdsMonitor_ObjectIdentity = ObjectIdentity
dot11WdsMonitor = _Dot11WdsMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5)
)
_Dot11GetWdsTable_Object = MibTable
dot11GetWdsTable = _Dot11GetWdsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    dot11GetWdsTable.setStatus("mandatory")
_Dot11GetWdsEntry_Object = MibTableRow
dot11GetWdsEntry = _Dot11GetWdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 1, 1)
)
dot11GetWdsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11GetWdsEntry.setStatus("mandatory")


class _Dot11WdsRefresh_Type(Integer32):
    """Custom type dot11WdsRefresh based on Integer32"""
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


_Dot11WdsRefresh_Type.__name__ = "Integer32"
_Dot11WdsRefresh_Object = MibTableColumn
dot11WdsRefresh = _Dot11WdsRefresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 1, 1, 1),
    _Dot11WdsRefresh_Type()
)
dot11WdsRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WdsRefresh.setStatus("mandatory")
_Dot11WdsTable_Object = MibTable
dot11WdsTable = _Dot11WdsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 2)
)
if mibBuilder.loadTexts:
    dot11WdsTable.setStatus("mandatory")
_Dot11WdsEntry_Object = MibTableRow
dot11WdsEntry = _Dot11WdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 2, 1)
)
dot11WdsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DAP-3520-v115", "dot11WdsIndex"),
)
if mibBuilder.loadTexts:
    dot11WdsEntry.setStatus("mandatory")
_Dot11WdsIndex_Type = Integer32
_Dot11WdsIndex_Object = MibTableColumn
dot11WdsIndex = _Dot11WdsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 2, 1, 1),
    _Dot11WdsIndex_Type()
)
dot11WdsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11WdsIndex.setStatus("mandatory")
_Dot11WdsMacAddress_Type = MacAddress
_Dot11WdsMacAddress_Object = MibTableColumn
dot11WdsMacAddress = _Dot11WdsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 2, 1, 2),
    _Dot11WdsMacAddress_Type()
)
dot11WdsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsMacAddress.setStatus("mandatory")


class _Dot11WdsBand_Type(Integer32):
    """Custom type dot11WdsBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dot11b", 1),
          ("dot11g", 2),
          ("dot11n", 4))
    )


_Dot11WdsBand_Type.__name__ = "Integer32"
_Dot11WdsBand_Object = MibTableColumn
dot11WdsBand = _Dot11WdsBand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 2, 1, 3),
    _Dot11WdsBand_Type()
)
dot11WdsBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsBand.setStatus("mandatory")


class _Dot11WdsAuthentication_Type(Integer32):
    """Custom type dot11WdsAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 1),
          ("sharedkey", 2),
          ("wep", 11),
          ("wpa-enterprise", 3),
          ("wpa-personal", 4),
          ("wpa2-auto-enterprise", 8),
          ("wpa2-auto-personal", 9),
          ("wpa2-enterprise", 6),
          ("wpa2-personal", 7))
    )


_Dot11WdsAuthentication_Type.__name__ = "Integer32"
_Dot11WdsAuthentication_Object = MibTableColumn
dot11WdsAuthentication = _Dot11WdsAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 2, 1, 4),
    _Dot11WdsAuthentication_Type()
)
dot11WdsAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsAuthentication.setStatus("mandatory")
_Dot11WdsRssi_Type = Integer32
_Dot11WdsRssi_Object = MibTableColumn
dot11WdsRssi = _Dot11WdsRssi_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 2, 1, 5),
    _Dot11WdsRssi_Type()
)
dot11WdsRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsRssi.setStatus("mandatory")
_Dot11WdsSsidIndex_Type = OctetString
_Dot11WdsSsidIndex_Object = MibTableColumn
dot11WdsSsidIndex = _Dot11WdsSsidIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 2, 1, 7),
    _Dot11WdsSsidIndex_Type()
)
dot11WdsSsidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsSsidIndex.setStatus("mandatory")
_Dot11WdsConnected_Type = Integer32
_Dot11WdsConnected_Object = MibTableColumn
dot11WdsConnected = _Dot11WdsConnected_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 2, 1, 8),
    _Dot11WdsConnected_Type()
)
dot11WdsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsConnected.setStatus("mandatory")
_Dot11WdsStatus_Type = OctetString
_Dot11WdsStatus_Object = MibTableColumn
dot11WdsStatus = _Dot11WdsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 2, 1, 9),
    _Dot11WdsStatus_Type()
)
dot11WdsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsStatus.setStatus("mandatory")


class _Dot11WdsPsm_Type(Integer32):
    """Custom type dot11WdsPsm based on Integer32"""
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


_Dot11WdsPsm_Type.__name__ = "Integer32"
_Dot11WdsPsm_Object = MibTableColumn
dot11WdsPsm = _Dot11WdsPsm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 5, 2, 1, 10),
    _Dot11WdsPsm_Type()
)
dot11WdsPsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11WdsPsm.setStatus("mandatory")
_Dot11MacClone_ObjectIdentity = ObjectIdentity
dot11MacClone = _Dot11MacClone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 6)
)
_Dot11MacCloneTable_Object = MibTable
dot11MacCloneTable = _Dot11MacCloneTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 6, 1)
)
if mibBuilder.loadTexts:
    dot11MacCloneTable.setStatus("mandatory")
_Dot11MacCloneEntry_Object = MibTableRow
dot11MacCloneEntry = _Dot11MacCloneEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 6, 1, 1)
)
dot11MacCloneEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11MacCloneEntry.setStatus("mandatory")


class _Dot11MacCloneStatus_Type(Integer32):
    """Custom type dot11MacCloneStatus based on Integer32"""
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


_Dot11MacCloneStatus_Type.__name__ = "Integer32"
_Dot11MacCloneStatus_Object = MibTableColumn
dot11MacCloneStatus = _Dot11MacCloneStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 6, 1, 1, 1),
    _Dot11MacCloneStatus_Type()
)
dot11MacCloneStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MacCloneStatus.setStatus("mandatory")


class _Dot11MacCloneSource_Type(Integer32):
    """Custom type dot11MacCloneSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("disabled", 0),
          ("manual", 2))
    )


_Dot11MacCloneSource_Type.__name__ = "Integer32"
_Dot11MacCloneSource_Object = MibTableColumn
dot11MacCloneSource = _Dot11MacCloneSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 6, 1, 1, 2),
    _Dot11MacCloneSource_Type()
)
dot11MacCloneSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MacCloneSource.setStatus("mandatory")
_Dot11MacCloneMacAddress_Type = MacAddress
_Dot11MacCloneMacAddress_Object = MibTableColumn
dot11MacCloneMacAddress = _Dot11MacCloneMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 6, 1, 1, 3),
    _Dot11MacCloneMacAddress_Type()
)
dot11MacCloneMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MacCloneMacAddress.setStatus("mandatory")


class _Dot11MacCloneAddressRefresh_Type(Integer32):
    """Custom type dot11MacCloneAddressRefresh based on Integer32"""
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


_Dot11MacCloneAddressRefresh_Type.__name__ = "Integer32"
_Dot11MacCloneAddressRefresh_Object = MibTableColumn
dot11MacCloneAddressRefresh = _Dot11MacCloneAddressRefresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 6, 1, 1, 4),
    _Dot11MacCloneAddressRefresh_Type()
)
dot11MacCloneAddressRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MacCloneAddressRefresh.setStatus("mandatory")
_Dot11MacCloneSurveryTable_Object = MibTable
dot11MacCloneSurveryTable = _Dot11MacCloneSurveryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 6, 2)
)
if mibBuilder.loadTexts:
    dot11MacCloneSurveryTable.setStatus("mandatory")
_Dot11MacCloneSurveryEntry_Object = MibTableRow
dot11MacCloneSurveryEntry = _Dot11MacCloneSurveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 6, 2, 1)
)
dot11MacCloneSurveryEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11MacCloneSurveryIndex"),
)
if mibBuilder.loadTexts:
    dot11MacCloneSurveryEntry.setStatus("mandatory")
_Dot11MacCloneSurveryIndex_Type = Integer32
_Dot11MacCloneSurveryIndex_Object = MibTableColumn
dot11MacCloneSurveryIndex = _Dot11MacCloneSurveryIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 6, 2, 1, 1),
    _Dot11MacCloneSurveryIndex_Type()
)
dot11MacCloneSurveryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11MacCloneSurveryIndex.setStatus("mandatory")
_Dot11MacCloneSurveryMacAddress_Type = MacAddress
_Dot11MacCloneSurveryMacAddress_Object = MibTableColumn
dot11MacCloneSurveryMacAddress = _Dot11MacCloneSurveryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 6, 2, 1, 2),
    _Dot11MacCloneSurveryMacAddress_Type()
)
dot11MacCloneSurveryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MacCloneSurveryMacAddress.setStatus("mandatory")
_Dot11ZoneDefence_ObjectIdentity = ObjectIdentity
dot11ZoneDefence = _Dot11ZoneDefence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 7)
)
_Dot11ZoneDefenceTable_Object = MibTable
dot11ZoneDefenceTable = _Dot11ZoneDefenceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 7, 1)
)
if mibBuilder.loadTexts:
    dot11ZoneDefenceTable.setStatus("mandatory")
_Dot11ZoneDefenceEntry_Object = MibTableRow
dot11ZoneDefenceEntry = _Dot11ZoneDefenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 7, 1, 1)
)
dot11ZoneDefenceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11ZoneDefenceEntry.setStatus("mandatory")


class _Dot11ZoneDefenceControl_Type(Integer32):
    """Custom type dot11ZoneDefenceControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enable", 1))
    )


_Dot11ZoneDefenceControl_Type.__name__ = "Integer32"
_Dot11ZoneDefenceControl_Object = MibTableColumn
dot11ZoneDefenceControl = _Dot11ZoneDefenceControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 7, 1, 1, 1),
    _Dot11ZoneDefenceControl_Type()
)
dot11ZoneDefenceControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ZoneDefenceControl.setStatus("mandatory")
_Dot11ZoneDefenceIpAddressAdd_Type = IpAddress
_Dot11ZoneDefenceIpAddressAdd_Object = MibTableColumn
dot11ZoneDefenceIpAddressAdd = _Dot11ZoneDefenceIpAddressAdd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 7, 1, 1, 2),
    _Dot11ZoneDefenceIpAddressAdd_Type()
)
dot11ZoneDefenceIpAddressAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ZoneDefenceIpAddressAdd.setStatus("mandatory")
_Dot11ZoneDefenceIpAddressDelete_Type = Integer32
_Dot11ZoneDefenceIpAddressDelete_Object = MibTableColumn
dot11ZoneDefenceIpAddressDelete = _Dot11ZoneDefenceIpAddressDelete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 7, 1, 1, 3),
    _Dot11ZoneDefenceIpAddressDelete_Type()
)
dot11ZoneDefenceIpAddressDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ZoneDefenceIpAddressDelete.setStatus("mandatory")
_Dot11ZoneDefenceIpAddressListTable_Object = MibTable
dot11ZoneDefenceIpAddressListTable = _Dot11ZoneDefenceIpAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 7, 2)
)
if mibBuilder.loadTexts:
    dot11ZoneDefenceIpAddressListTable.setStatus("mandatory")
_Dot11ZoneDefenceIpAddressListEntry_Object = MibTableRow
dot11ZoneDefenceIpAddressListEntry = _Dot11ZoneDefenceIpAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 7, 2, 1)
)
dot11ZoneDefenceIpAddressListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DAP-3520-v115", "dot11ZoneDefenceIpAddressListIndex"),
)
if mibBuilder.loadTexts:
    dot11ZoneDefenceIpAddressListEntry.setStatus("mandatory")


class _Dot11ZoneDefenceIpAddressListIndex_Type(Integer32):
    """Custom type dot11ZoneDefenceIpAddressListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dot11ZoneDefenceIpAddressListIndex_Type.__name__ = "Integer32"
_Dot11ZoneDefenceIpAddressListIndex_Object = MibTableColumn
dot11ZoneDefenceIpAddressListIndex = _Dot11ZoneDefenceIpAddressListIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 7, 2, 1, 1),
    _Dot11ZoneDefenceIpAddressListIndex_Type()
)
dot11ZoneDefenceIpAddressListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11ZoneDefenceIpAddressListIndex.setStatus("mandatory")
_Dot11ZoneDefenceIpAddressList_Type = IpAddress
_Dot11ZoneDefenceIpAddressList_Object = MibTableColumn
dot11ZoneDefenceIpAddressList = _Dot11ZoneDefenceIpAddressList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 2, 1, 3, 3, 7, 2, 1, 2),
    _Dot11ZoneDefenceIpAddressList_Type()
)
dot11ZoneDefenceIpAddressList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ZoneDefenceIpAddressList.setStatus("mandatory")
_Advance_ObjectIdentity = ObjectIdentity
advance = _Advance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3)
)
_DhcpServer_ObjectIdentity = ObjectIdentity
dhcpServer = _DhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 1),
    _DhcpServerControl_Type()
)
dhcpServerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerControl.setStatus("mandatory")
_DhcpServerDynamicParameter_ObjectIdentity = ObjectIdentity
dhcpServerDynamicParameter = _DhcpServerDynamicParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2)
)


class _DhcpServerDynamicControl_Type(Integer32):
    """Custom type dhcpServerDynamicControl based on Integer32"""
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


_DhcpServerDynamicControl_Type.__name__ = "Integer32"
_DhcpServerDynamicControl_Object = MibScalar
dhcpServerDynamicControl = _DhcpServerDynamicControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 1),
    _DhcpServerDynamicControl_Type()
)
dhcpServerDynamicControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDynamicControl.setStatus("mandatory")
_DhcpServerDynamicTable_Object = MibTable
dhcpServerDynamicTable = _DhcpServerDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dhcpServerDynamicTable.setStatus("mandatory")
_DhcpServerDynamicEntry_Object = MibTableRow
dhcpServerDynamicEntry = _DhcpServerDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 2, 1)
)
dhcpServerDynamicEntry.setIndexNames(
    (0, "DAP-3520-v115", "dynamicIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerDynamicEntry.setStatus("mandatory")
_DynamicIndex_Type = Integer32
_DynamicIndex_Object = MibTableColumn
dynamicIndex = _DynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 2, 1, 1),
    _DynamicIndex_Type()
)
dynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dynamicIndex.setStatus("mandatory")
_DynamicIpPoolStart_Type = IpAddress
_DynamicIpPoolStart_Object = MibTableColumn
dynamicIpPoolStart = _DynamicIpPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 2, 1, 3),
    _DynamicIpPoolStart_Type()
)
dynamicIpPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicIpPoolStart.setStatus("mandatory")
_DynamicIpPoolEnd_Type = IpAddress
_DynamicIpPoolEnd_Object = MibTableColumn
dynamicIpPoolEnd = _DynamicIpPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 2, 1, 4),
    _DynamicIpPoolEnd_Type()
)
dynamicIpPoolEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicIpPoolEnd.setStatus("mandatory")
_DynamicMask_Type = IpAddress
_DynamicMask_Object = MibTableColumn
dynamicMask = _DynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 2, 1, 6),
    _DynamicMask_Type()
)
dynamicMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicMask.setStatus("mandatory")
_DynamicGateway_Type = IpAddress
_DynamicGateway_Object = MibTableColumn
dynamicGateway = _DynamicGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 2, 1, 7),
    _DynamicGateway_Type()
)
dynamicGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicGateway.setStatus("mandatory")
_DynamicWins_Type = IpAddress
_DynamicWins_Object = MibTableColumn
dynamicWins = _DynamicWins_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 2, 1, 8),
    _DynamicWins_Type()
)
dynamicWins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicWins.setStatus("mandatory")
_DynamicDns_Type = IpAddress
_DynamicDns_Object = MibTableColumn
dynamicDns = _DynamicDns_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 2, 1, 9),
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
_DynamicDomainName_Object = MibTableColumn
dynamicDomainName = _DynamicDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 2, 1, 10),
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
_DynamicLeaseTime_Object = MibTableColumn
dynamicLeaseTime = _DynamicLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 2, 1, 11),
    _DynamicLeaseTime_Type()
)
dynamicLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicLeaseTime.setStatus("mandatory")


class _DhcpServerDomainNameStatus_Type(Integer32):
    """Custom type dhcpServerDomainNameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("dynamic", 1),
          ("static", 2))
    )


_DhcpServerDomainNameStatus_Type.__name__ = "Integer32"
_DhcpServerDomainNameStatus_Object = MibScalar
dhcpServerDomainNameStatus = _DhcpServerDomainNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 2, 3),
    _DhcpServerDomainNameStatus_Type()
)
dhcpServerDomainNameStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerDomainNameStatus.setStatus("mandatory")
_DhcpServerStaticParameter_ObjectIdentity = ObjectIdentity
dhcpServerStaticParameter = _DhcpServerStaticParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3)
)


class _DhcpServerStaticControl_Type(Integer32):
    """Custom type dhcpServerStaticControl based on Integer32"""
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


_DhcpServerStaticControl_Type.__name__ = "Integer32"
_DhcpServerStaticControl_Object = MibScalar
dhcpServerStaticControl = _DhcpServerStaticControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 1),
    _DhcpServerStaticControl_Type()
)
dhcpServerStaticControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerStaticControl.setStatus("mandatory")
_DhcpServerStaticTable_Object = MibTable
dhcpServerStaticTable = _DhcpServerStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dhcpServerStaticTable.setStatus("mandatory")
_DhcpServerStaticEntry_Object = MibTableRow
dhcpServerStaticEntry = _DhcpServerStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2, 1)
)
dhcpServerStaticEntry.setIndexNames(
    (0, "DAP-3520-v115", "staticIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerStaticEntry.setStatus("mandatory")
_StaticIndex_Type = Integer32
_StaticIndex_Object = MibTableColumn
staticIndex = _StaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2, 1, 1),
    _StaticIndex_Type()
)
staticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticIndex.setStatus("mandatory")


class _StaticEntryStatus_Type(Integer32):
    """Custom type staticEntryStatus based on Integer32"""
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


_StaticEntryStatus_Type.__name__ = "Integer32"
_StaticEntryStatus_Object = MibTableColumn
staticEntryStatus = _StaticEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2, 1, 2),
    _StaticEntryStatus_Type()
)
staticEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticEntryStatus.setStatus("mandatory")


class _StaticHostName_Type(OctetString):
    """Custom type staticHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StaticHostName_Type.__name__ = "OctetString"
_StaticHostName_Object = MibTableColumn
staticHostName = _StaticHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2, 1, 3),
    _StaticHostName_Type()
)
staticHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticHostName.setStatus("mandatory")
_StaticIP_Type = IpAddress
_StaticIP_Object = MibTableColumn
staticIP = _StaticIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2, 1, 4),
    _StaticIP_Type()
)
staticIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIP.setStatus("mandatory")
_StaticMac_Type = MacAddress
_StaticMac_Object = MibTableColumn
staticMac = _StaticMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2, 1, 5),
    _StaticMac_Type()
)
staticMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMac.setStatus("mandatory")
_StaticMask_Type = IpAddress
_StaticMask_Object = MibTableColumn
staticMask = _StaticMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2, 1, 6),
    _StaticMask_Type()
)
staticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMask.setStatus("mandatory")
_StaticGateway_Type = IpAddress
_StaticGateway_Object = MibTableColumn
staticGateway = _StaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2, 1, 7),
    _StaticGateway_Type()
)
staticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticGateway.setStatus("mandatory")
_StaticDns_Type = IpAddress
_StaticDns_Object = MibTableColumn
staticDns = _StaticDns_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2, 1, 8),
    _StaticDns_Type()
)
staticDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDns.setStatus("mandatory")
_StaticWins_Type = IpAddress
_StaticWins_Object = MibTableColumn
staticWins = _StaticWins_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 2, 1, 10),
    _StaticDomainName_Type()
)
staticDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticDomainName.setStatus("mandatory")


class _DhcpServerStaticDelete_Type(Integer32):
    """Custom type dhcpServerStaticDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_DhcpServerStaticDelete_Type.__name__ = "Integer32"
_DhcpServerStaticDelete_Object = MibScalar
dhcpServerStaticDelete = _DhcpServerStaticDelete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 3, 3),
    _DhcpServerStaticDelete_Type()
)
dhcpServerStaticDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerStaticDelete.setStatus("mandatory")
_DhcpServerCurrentList_ObjectIdentity = ObjectIdentity
dhcpServerCurrentList = _DhcpServerCurrentList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4)
)


class _RefreshCurrentDynamicList_Type(Integer32):
    """Custom type refreshCurrentDynamicList based on Integer32"""
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


_RefreshCurrentDynamicList_Type.__name__ = "Integer32"
_RefreshCurrentDynamicList_Object = MibScalar
refreshCurrentDynamicList = _RefreshCurrentDynamicList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 1),
    _RefreshCurrentDynamicList_Type()
)
refreshCurrentDynamicList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refreshCurrentDynamicList.setStatus("mandatory")
_CurrentDynamicTable_Object = MibTable
currentDynamicTable = _CurrentDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    currentDynamicTable.setStatus("mandatory")
_CurrentDynamicEntry_Object = MibTableRow
currentDynamicEntry = _CurrentDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 2, 1)
)
currentDynamicEntry.setIndexNames(
    (0, "DAP-3520-v115", "currentDynamicIndex"),
)
if mibBuilder.loadTexts:
    currentDynamicEntry.setStatus("mandatory")
_CurrentDynamicIndex_Type = Integer32
_CurrentDynamicIndex_Object = MibTableColumn
currentDynamicIndex = _CurrentDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 2, 1, 1),
    _CurrentDynamicIndex_Type()
)
currentDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentDynamicIndex.setStatus("mandatory")


class _CurrentDynamicHostName_Type(OctetString):
    """Custom type currentDynamicHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CurrentDynamicHostName_Type.__name__ = "OctetString"
_CurrentDynamicHostName_Object = MibTableColumn
currentDynamicHostName = _CurrentDynamicHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 2, 1, 2),
    _CurrentDynamicHostName_Type()
)
currentDynamicHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentDynamicHostName.setStatus("mandatory")
_CurrentDynamicMacAddress_Type = MacAddress
_CurrentDynamicMacAddress_Object = MibTableColumn
currentDynamicMacAddress = _CurrentDynamicMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 2, 1, 3),
    _CurrentDynamicMacAddress_Type()
)
currentDynamicMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDynamicMacAddress.setStatus("mandatory")
_CurrentDynamicAssignedIP_Type = IpAddress
_CurrentDynamicAssignedIP_Object = MibTableColumn
currentDynamicAssignedIP = _CurrentDynamicAssignedIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 2, 1, 4),
    _CurrentDynamicAssignedIP_Type()
)
currentDynamicAssignedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDynamicAssignedIP.setStatus("mandatory")
_CurrentDynamicLease_Type = TimeTicks
_CurrentDynamicLease_Object = MibTableColumn
currentDynamicLease = _CurrentDynamicLease_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 2, 1, 5),
    _CurrentDynamicLease_Type()
)
currentDynamicLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDynamicLease.setStatus("mandatory")


class _RefreshCurrentStaticList_Type(Integer32):
    """Custom type refreshCurrentStaticList based on Integer32"""
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


_RefreshCurrentStaticList_Type.__name__ = "Integer32"
_RefreshCurrentStaticList_Object = MibScalar
refreshCurrentStaticList = _RefreshCurrentStaticList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 3),
    _RefreshCurrentStaticList_Type()
)
refreshCurrentStaticList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refreshCurrentStaticList.setStatus("mandatory")
_CurrentStaticTable_Object = MibTable
currentStaticTable = _CurrentStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    currentStaticTable.setStatus("mandatory")
_CurrentStaticEntry_Object = MibTableRow
currentStaticEntry = _CurrentStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 4, 1)
)
currentStaticEntry.setIndexNames(
    (0, "DAP-3520-v115", "currentStaticIndex"),
)
if mibBuilder.loadTexts:
    currentStaticEntry.setStatus("mandatory")
_CurrentStaticIndex_Type = Integer32
_CurrentStaticIndex_Object = MibTableColumn
currentStaticIndex = _CurrentStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 4, 1, 1),
    _CurrentStaticIndex_Type()
)
currentStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentStaticIndex.setStatus("mandatory")


class _CurrentStaticHostName_Type(OctetString):
    """Custom type currentStaticHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CurrentStaticHostName_Type.__name__ = "OctetString"
_CurrentStaticHostName_Object = MibTableColumn
currentStaticHostName = _CurrentStaticHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 4, 1, 2),
    _CurrentStaticHostName_Type()
)
currentStaticHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentStaticHostName.setStatus("mandatory")
_CurrentStaticMacAddress_Type = MacAddress
_CurrentStaticMacAddress_Object = MibTableColumn
currentStaticMacAddress = _CurrentStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 4, 1, 3),
    _CurrentStaticMacAddress_Type()
)
currentStaticMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentStaticMacAddress.setStatus("mandatory")
_CurrentStaticAssignedIP_Type = IpAddress
_CurrentStaticAssignedIP_Object = MibTableColumn
currentStaticAssignedIP = _CurrentStaticAssignedIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 1, 4, 4, 1, 4),
    _CurrentStaticAssignedIP_Type()
)
currentStaticAssignedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentStaticAssignedIP.setStatus("mandatory")
_Ieee802dot11Grouping_ObjectIdentity = ObjectIdentity
ieee802dot11Grouping = _Ieee802dot11Grouping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 2)
)
_Dot11GroupingTable_Object = MibTable
dot11GroupingTable = _Dot11GroupingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dot11GroupingTable.setStatus("mandatory")
_Dot11GroupingEntry_Object = MibTableRow
dot11GroupingEntry = _Dot11GroupingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 2, 1, 1)
)
dot11GroupingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11GroupingEntry.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 2, 1, 1, 3),
    _Dot11LinkIntegrate_Type()
)
dot11LinkIntegrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11LinkIntegrate.setStatus("mandatory")
_Ieee802dot11MultiSsid_ObjectIdentity = ObjectIdentity
ieee802dot11MultiSsid = _Ieee802dot11MultiSsid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3)
)
_Dot11MssidStateTable_Object = MibTable
dot11MssidStateTable = _Dot11MssidStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 1)
)
if mibBuilder.loadTexts:
    dot11MssidStateTable.setStatus("mandatory")
_Dot11MssidStateEntry_Object = MibTableRow
dot11MssidStateEntry = _Dot11MssidStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 1, 1)
)
dot11MssidStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11MssidStateEntry.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 1, 1, 1),
    _Dot11MssidState_Type()
)
dot11MssidState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidState.setStatus("mandatory")


class _Dot11MssidPriorityState_Type(Integer32):
    """Custom type dot11MssidPriorityState based on Integer32"""
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


_Dot11MssidPriorityState_Type.__name__ = "Integer32"
_Dot11MssidPriorityState_Object = MibTableColumn
dot11MssidPriorityState = _Dot11MssidPriorityState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 1, 1, 2),
    _Dot11MssidPriorityState_Type()
)
dot11MssidPriorityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidPriorityState.setStatus("mandatory")
_Dot11MssidTable_Object = MibTable
dot11MssidTable = _Dot11MssidTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3)
)
if mibBuilder.loadTexts:
    dot11MssidTable.setStatus("mandatory")
_Dot11MssidEntry_Object = MibTableRow
dot11MssidEntry = _Dot11MssidEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1)
)
dot11MssidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DAP-3520-v115", "dot11MssidIndex"),
)
if mibBuilder.loadTexts:
    dot11MssidEntry.setStatus("mandatory")
_Dot11MssidIndex_Type = Integer32
_Dot11MssidIndex_Object = MibTableColumn
dot11MssidIndex = _Dot11MssidIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 4),
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 10),
          ("opensystem", 1),
          ("opensystem-sharedkey", 3),
          ("sharedkey", 2),
          ("wpa-eap", 5),
          ("wpa-psk", 4),
          ("wpa2-auto-eap", 9),
          ("wpa2-auto-psk", 8),
          ("wpa2-eap", 7),
          ("wpa2-psk", 6))
    )


_Dot11MssidAuthentication_Type.__name__ = "Integer32"
_Dot11MssidAuthentication_Object = MibTableColumn
dot11MssidAuthentication = _Dot11MssidAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 7),
    _Dot11MssidWepKeyIndex_Type()
)
dot11MssidWepKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidWepKeyIndex.setStatus("mandatory")
_Dot11MssidWepKey_Type = OctetString
_Dot11MssidWepKey_Object = MibTableColumn
dot11MssidWepKey = _Dot11MssidWepKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 8),
    _Dot11MssidWepKey_Type()
)
dot11MssidWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidWepKey.setStatus("mandatory")


class _Dot11MssidCipherType_Type(Integer32):
    """Custom type dot11MssidCipherType based on Integer32"""
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
        *(("aes", 2),
          ("auto", 1),
          ("tkip", 3),
          ("wep", 4))
    )


_Dot11MssidCipherType_Type.__name__ = "Integer32"
_Dot11MssidCipherType_Object = MibTableColumn
dot11MssidCipherType = _Dot11MssidCipherType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 12),
    _Dot11MssidKeyType_Type()
)
dot11MssidKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidKeyType.setStatus("mandatory")


class _Dot11MssidWmm_Type(Integer32):
    """Custom type dot11MssidWmm based on Integer32"""
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


_Dot11MssidWmm_Type.__name__ = "Integer32"
_Dot11MssidWmm_Object = MibTableColumn
dot11MssidWmm = _Dot11MssidWmm_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 14),
    _Dot11MssidWmm_Type()
)
dot11MssidWmm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidWmm.setStatus("mandatory")


class _Dot11MssidGroupKeyUpdateInterval_Type(Integer32):
    """Custom type dot11MssidGroupKeyUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 9999999),
    )


_Dot11MssidGroupKeyUpdateInterval_Type.__name__ = "Integer32"
_Dot11MssidGroupKeyUpdateInterval_Object = MibTableColumn
dot11MssidGroupKeyUpdateInterval = _Dot11MssidGroupKeyUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 15),
    _Dot11MssidGroupKeyUpdateInterval_Type()
)
dot11MssidGroupKeyUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidGroupKeyUpdateInterval.setStatus("mandatory")


class _Dot11MssidPriority_Type(Integer32):
    """Custom type dot11MssidPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot11MssidPriority_Type.__name__ = "Integer32"
_Dot11MssidPriority_Object = MibTableColumn
dot11MssidPriority = _Dot11MssidPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 16),
    _Dot11MssidPriority_Type()
)
dot11MssidPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidPriority.setStatus("mandatory")


class _Dot11MssidAutoRekeyControl_Type(Integer32):
    """Custom type dot11MssidAutoRekeyControl based on Integer32"""
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


_Dot11MssidAutoRekeyControl_Type.__name__ = "Integer32"
_Dot11MssidAutoRekeyControl_Object = MibTableColumn
dot11MssidAutoRekeyControl = _Dot11MssidAutoRekeyControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 17),
    _Dot11MssidAutoRekeyControl_Type()
)
dot11MssidAutoRekeyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidAutoRekeyControl.setStatus("mandatory")


class _Dot11MssidAutoRekeyStartWeek_Type(Integer32):
    """Custom type dot11MssidAutoRekeyStartWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fri", 5),
          ("mon", 1),
          ("sat", 6),
          ("sun", 0),
          ("thu", 4),
          ("tue", 2),
          ("wed", 3))
    )


_Dot11MssidAutoRekeyStartWeek_Type.__name__ = "Integer32"
_Dot11MssidAutoRekeyStartWeek_Object = MibTableColumn
dot11MssidAutoRekeyStartWeek = _Dot11MssidAutoRekeyStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 18),
    _Dot11MssidAutoRekeyStartWeek_Type()
)
dot11MssidAutoRekeyStartWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidAutoRekeyStartWeek.setStatus("mandatory")
_Dot11MssidAutoRekeyStartTime_Type = OctetString
_Dot11MssidAutoRekeyStartTime_Object = MibTableColumn
dot11MssidAutoRekeyStartTime = _Dot11MssidAutoRekeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 19),
    _Dot11MssidAutoRekeyStartTime_Type()
)
dot11MssidAutoRekeyStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidAutoRekeyStartTime.setStatus("mandatory")


class _Dot11MssidAutoRekeyTimeInterval_Type(Integer32):
    """Custom type dot11MssidAutoRekeyTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 168),
    )


_Dot11MssidAutoRekeyTimeInterval_Type.__name__ = "Integer32"
_Dot11MssidAutoRekeyTimeInterval_Object = MibTableColumn
dot11MssidAutoRekeyTimeInterval = _Dot11MssidAutoRekeyTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 20),
    _Dot11MssidAutoRekeyTimeInterval_Type()
)
dot11MssidAutoRekeyTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidAutoRekeyTimeInterval.setStatus("mandatory")
_Dot11MssidAutoRekeyPassPhrase_Type = OctetString
_Dot11MssidAutoRekeyPassPhrase_Object = MibTableColumn
dot11MssidAutoRekeyPassPhrase = _Dot11MssidAutoRekeyPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 3, 1, 21),
    _Dot11MssidAutoRekeyPassPhrase_Type()
)
dot11MssidAutoRekeyPassPhrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11MssidAutoRekeyPassPhrase.setStatus("mandatory")
_Dot11MssidRADIUSTable_Object = MibTable
dot11MssidRADIUSTable = _Dot11MssidRADIUSTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 4)
)
if mibBuilder.loadTexts:
    dot11MssidRADIUSTable.setStatus("mandatory")
_Dot11MssidRADIUSEntry_Object = MibTableRow
dot11MssidRADIUSEntry = _Dot11MssidRADIUSEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 4, 1)
)
dot11MssidRADIUSEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11MssidRADIUSIndex"),
    (0, "DAP-3520-v115", "dot11MssidIndex"),
)
if mibBuilder.loadTexts:
    dot11MssidRADIUSEntry.setStatus("mandatory")
_Dot11MssidRADIUSIndex_Type = Integer32
_Dot11MssidRADIUSIndex_Object = MibTableColumn
dot11MssidRADIUSIndex = _Dot11MssidRADIUSIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 4, 1, 1),
    _Dot11MssidRADIUSIndex_Type()
)
dot11MssidRADIUSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11MssidRADIUSIndex.setStatus("mandatory")
_Dot11MssidRADIUSServer_Type = IpAddress
_Dot11MssidRADIUSServer_Object = MibTableColumn
dot11MssidRADIUSServer = _Dot11MssidRADIUSServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 4, 1, 2),
    _Dot11MssidRADIUSServer_Type()
)
dot11MssidRADIUSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidRADIUSServer.setStatus("mandatory")


class _Dot11MssidRADIUSPort_Type(Integer32):
    """Custom type dot11MssidRADIUSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot11MssidRADIUSPort_Type.__name__ = "Integer32"
_Dot11MssidRADIUSPort_Object = MibTableColumn
dot11MssidRADIUSPort = _Dot11MssidRADIUSPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 4, 1, 3),
    _Dot11MssidRADIUSPort_Type()
)
dot11MssidRADIUSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidRADIUSPort.setStatus("mandatory")


class _Dot11MssidRADIUSSecret_Type(OctetString):
    """Custom type dot11MssidRADIUSSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11MssidRADIUSSecret_Type.__name__ = "OctetString"
_Dot11MssidRADIUSSecret_Object = MibTableColumn
dot11MssidRADIUSSecret = _Dot11MssidRADIUSSecret_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 4, 1, 4),
    _Dot11MssidRADIUSSecret_Type()
)
dot11MssidRADIUSSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidRADIUSSecret.setStatus("mandatory")
_Dot11MssidRadiusKeyUpdateInterval_Type = Integer32
_Dot11MssidRadiusKeyUpdateInterval_Object = MibTableColumn
dot11MssidRadiusKeyUpdateInterval = _Dot11MssidRadiusKeyUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 3, 4, 1, 6),
    _Dot11MssidRadiusKeyUpdateInterval_Type()
)
dot11MssidRadiusKeyUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MssidRadiusKeyUpdateInterval.setStatus("mandatory")
_Ieee802dot11RogueApDetection_ObjectIdentity = ObjectIdentity
ieee802dot11RogueApDetection = _Ieee802dot11RogueApDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4)
)
_Dot11RogueApSurvey_ObjectIdentity = ObjectIdentity
dot11RogueApSurvey = _Dot11RogueApSurvey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 1),
    _Dot11RogueApSurveyRefresh_Type()
)
dot11RogueApSurveyRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApSurveyRefresh.setStatus("mandatory")
_Dot11RogueApSurveyTable_Object = MibTable
dot11RogueApSurveyTable = _Dot11RogueApSurveyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 4)
)
if mibBuilder.loadTexts:
    dot11RogueApSurveyTable.setStatus("mandatory")
_Dot11RogueApSurveyEntry_Object = MibTableRow
dot11RogueApSurveyEntry = _Dot11RogueApSurveyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 4, 1)
)
dot11RogueApSurveyEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11RogueApSurveyIndex"),
)
if mibBuilder.loadTexts:
    dot11RogueApSurveyEntry.setStatus("mandatory")
_Dot11RogueApSurveyIndex_Type = Integer32
_Dot11RogueApSurveyIndex_Object = MibTableColumn
dot11RogueApSurveyIndex = _Dot11RogueApSurveyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 4, 1, 1),
    _Dot11RogueApSurveyIndex_Type()
)
dot11RogueApSurveyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11RogueApSurveyIndex.setStatus("mandatory")
_Dot11RogueApSurveyChannel_Type = Integer32
_Dot11RogueApSurveyChannel_Object = MibTableColumn
dot11RogueApSurveyChannel = _Dot11RogueApSurveyChannel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 4, 1, 3),
    _Dot11RogueApSurveyChannel_Type()
)
dot11RogueApSurveyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyChannel.setStatus("mandatory")
_Dot11RogueApSurveyBssid_Type = MacAddress
_Dot11RogueApSurveyBssid_Object = MibTableColumn
dot11RogueApSurveyBssid = _Dot11RogueApSurveyBssid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 4, 1, 5),
    _Dot11RogueApSurveyBssid_Type()
)
dot11RogueApSurveyBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyBssid.setStatus("mandatory")


class _Dot11RogueApSurveyMode_Type(Integer32):
    """Custom type dot11RogueApSurveyMode based on Integer32"""
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
        *(("dot11a", 3),
          ("dot11b", 4),
          ("dot11g", 1),
          ("dot11n", 2))
    )


_Dot11RogueApSurveyMode_Type.__name__ = "Integer32"
_Dot11RogueApSurveyMode_Object = MibTableColumn
dot11RogueApSurveyMode = _Dot11RogueApSurveyMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 4, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 4, 1, 9),
    _Dot11RogueApSurveySsid_Type()
)
dot11RogueApSurveySsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveySsid.setStatus("mandatory")
_Dot11RogueApSurveyLastseen_Type = OctetString
_Dot11RogueApSurveyLastseen_Object = MibTableColumn
dot11RogueApSurveyLastseen = _Dot11RogueApSurveyLastseen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 4, 1, 10),
    _Dot11RogueApSurveyLastseen_Type()
)
dot11RogueApSurveyLastseen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyLastseen.setStatus("mandatory")


class _Dot11RogueApSurveyType_Type(Integer32):
    """Custom type dot11RogueApSurveyType based on Integer32"""
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
        *(("neighborhood", 3),
          ("new", 1),
          ("rogue", 4),
          ("valid", 2))
    )


_Dot11RogueApSurveyType_Type.__name__ = "Integer32"
_Dot11RogueApSurveyType_Object = MibTableColumn
dot11RogueApSurveyType = _Dot11RogueApSurveyType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 4, 1, 11),
    _Dot11RogueApSurveyType_Type()
)
dot11RogueApSurveyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyType.setStatus("mandatory")


class _Dot11RogueApSurveyStatus_Type(Integer32):
    """Custom type dot11RogueApSurveyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_Dot11RogueApSurveyStatus_Type.__name__ = "Integer32"
_Dot11RogueApSurveyStatus_Object = MibTableColumn
dot11RogueApSurveyStatus = _Dot11RogueApSurveyStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 4, 1, 12),
    _Dot11RogueApSurveyStatus_Type()
)
dot11RogueApSurveyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApSurveyStatus.setStatus("mandatory")


class _Dot11RogueApAddtoValid_Type(Integer32):
    """Custom type dot11RogueApAddtoValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Dot11RogueApAddtoValid_Type.__name__ = "Integer32"
_Dot11RogueApAddtoValid_Object = MibScalar
dot11RogueApAddtoValid = _Dot11RogueApAddtoValid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 5),
    _Dot11RogueApAddtoValid_Type()
)
dot11RogueApAddtoValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApAddtoValid.setStatus("mandatory")


class _Dot11RogueApAddtoNeighbor_Type(Integer32):
    """Custom type dot11RogueApAddtoNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Dot11RogueApAddtoNeighbor_Type.__name__ = "Integer32"
_Dot11RogueApAddtoNeighbor_Object = MibScalar
dot11RogueApAddtoNeighbor = _Dot11RogueApAddtoNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 6),
    _Dot11RogueApAddtoNeighbor_Type()
)
dot11RogueApAddtoNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApAddtoNeighbor.setStatus("mandatory")


class _Dot11RogueApAddtoRouge_Type(Integer32):
    """Custom type dot11RogueApAddtoRouge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Dot11RogueApAddtoRouge_Type.__name__ = "Integer32"
_Dot11RogueApAddtoRouge_Object = MibScalar
dot11RogueApAddtoRouge = _Dot11RogueApAddtoRouge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 7),
    _Dot11RogueApAddtoRouge_Type()
)
dot11RogueApAddtoRouge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApAddtoRouge.setStatus("mandatory")


class _Dot11RogueApAddtoNew_Type(Integer32):
    """Custom type dot11RogueApAddtoNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Dot11RogueApAddtoNew_Type.__name__ = "Integer32"
_Dot11RogueApAddtoNew_Object = MibScalar
dot11RogueApAddtoNew = _Dot11RogueApAddtoNew_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 8),
    _Dot11RogueApAddtoNew_Type()
)
dot11RogueApAddtoNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApAddtoNew.setStatus("mandatory")


class _Dot11RogueApAllNewNodesAsValid_Type(Integer32):
    """Custom type dot11RogueApAllNewNodesAsValid based on Integer32"""
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


_Dot11RogueApAllNewNodesAsValid_Type.__name__ = "Integer32"
_Dot11RogueApAllNewNodesAsValid_Object = MibScalar
dot11RogueApAllNewNodesAsValid = _Dot11RogueApAllNewNodesAsValid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 9),
    _Dot11RogueApAllNewNodesAsValid_Type()
)
dot11RogueApAllNewNodesAsValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApAllNewNodesAsValid.setStatus("mandatory")


class _Dot11RogueApAllNewNodesAsRogue_Type(Integer32):
    """Custom type dot11RogueApAllNewNodesAsRogue based on Integer32"""
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


_Dot11RogueApAllNewNodesAsRogue_Type.__name__ = "Integer32"
_Dot11RogueApAllNewNodesAsRogue_Object = MibScalar
dot11RogueApAllNewNodesAsRogue = _Dot11RogueApAllNewNodesAsRogue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 4, 10),
    _Dot11RogueApAllNewNodesAsRogue_Type()
)
dot11RogueApAllNewNodesAsRogue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApAllNewNodesAsRogue.setStatus("mandatory")
_Dot11RogueApListRecord_ObjectIdentity = ObjectIdentity
dot11RogueApListRecord = _Dot11RogueApListRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5, 1),
    _Dot11RogueApDeleteFromRecord_Type()
)
dot11RogueApDeleteFromRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RogueApDeleteFromRecord.setStatus("mandatory")
_Dot11RogueApListRecordTable_Object = MibTable
dot11RogueApListRecordTable = _Dot11RogueApListRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5, 2)
)
if mibBuilder.loadTexts:
    dot11RogueApListRecordTable.setStatus("mandatory")
_Dot11RogueApListRecordEntry_Object = MibTableRow
dot11RogueApListRecordEntry = _Dot11RogueApListRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5, 2, 1)
)
dot11RogueApListRecordEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11RogueApListRecordIndex"),
)
if mibBuilder.loadTexts:
    dot11RogueApListRecordEntry.setStatus("mandatory")
_Dot11RogueApListRecordIndex_Type = Integer32
_Dot11RogueApListRecordIndex_Object = MibTableColumn
dot11RogueApListRecordIndex = _Dot11RogueApListRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5, 2, 1, 1),
    _Dot11RogueApListRecordIndex_Type()
)
dot11RogueApListRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11RogueApListRecordIndex.setStatus("mandatory")
_Dot11RogueApListRecordChannel_Type = Integer32
_Dot11RogueApListRecordChannel_Object = MibTableColumn
dot11RogueApListRecordChannel = _Dot11RogueApListRecordChannel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5, 2, 1, 3),
    _Dot11RogueApListRecordChannel_Type()
)
dot11RogueApListRecordChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordChannel.setStatus("mandatory")
_Dot11RogueApListRecordBssid_Type = MacAddress
_Dot11RogueApListRecordBssid_Object = MibTableColumn
dot11RogueApListRecordBssid = _Dot11RogueApListRecordBssid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5, 2, 1, 5),
    _Dot11RogueApListRecordBssid_Type()
)
dot11RogueApListRecordBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordBssid.setStatus("mandatory")


class _Dot11RogueApListRecordMode_Type(Integer32):
    """Custom type dot11RogueApListRecordMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 0),
          ("dot11b", 2),
          ("dot11g", 3),
          ("dot11n", 4))
    )


_Dot11RogueApListRecordMode_Type.__name__ = "Integer32"
_Dot11RogueApListRecordMode_Object = MibTableColumn
dot11RogueApListRecordMode = _Dot11RogueApListRecordMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5, 2, 1, 9),
    _Dot11RogueApListRecordSsid_Type()
)
dot11RogueApListRecordSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordSsid.setStatus("mandatory")
_Dot11RogueApListRecordLastseen_Type = OctetString
_Dot11RogueApListRecordLastseen_Object = MibTableColumn
dot11RogueApListRecordLastseen = _Dot11RogueApListRecordLastseen_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5, 2, 1, 10),
    _Dot11RogueApListRecordLastseen_Type()
)
dot11RogueApListRecordLastseen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordLastseen.setStatus("mandatory")


class _Dot11RogueApListRecordType_Type(Integer32):
    """Custom type dot11RogueApListRecordType based on Integer32"""
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
        *(("neighborhood", 3),
          ("new", 1),
          ("rogue", 4),
          ("valid", 2))
    )


_Dot11RogueApListRecordType_Type.__name__ = "Integer32"
_Dot11RogueApListRecordType_Object = MibTableColumn
dot11RogueApListRecordType = _Dot11RogueApListRecordType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5, 2, 1, 11),
    _Dot11RogueApListRecordType_Type()
)
dot11RogueApListRecordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordType.setStatus("mandatory")


class _Dot11RogueApListRecordStatus_Type(Integer32):
    """Custom type dot11RogueApListRecordStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_Dot11RogueApListRecordStatus_Type.__name__ = "Integer32"
_Dot11RogueApListRecordStatus_Object = MibTableColumn
dot11RogueApListRecordStatus = _Dot11RogueApListRecordStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 4, 5, 2, 1, 12),
    _Dot11RogueApListRecordStatus_Type()
)
dot11RogueApListRecordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11RogueApListRecordStatus.setStatus("mandatory")
_Ieee802dot11VLAN_ObjectIdentity = ObjectIdentity
ieee802dot11VLAN = _Ieee802dot11VLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6)
)
_Dot11VLANParameter_ObjectIdentity = ObjectIdentity
dot11VLANParameter = _Dot11VLANParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1)
)


class _Dot11VlanStatus_Type(Integer32):
    """Custom type dot11VlanStatus based on Integer32"""
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


_Dot11VlanStatus_Type.__name__ = "Integer32"
_Dot11VlanStatus_Object = MibScalar
dot11VlanStatus = _Dot11VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 1),
    _Dot11VlanStatus_Type()
)
dot11VlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11VlanStatus.setStatus("mandatory")


class _Dot11VlanMode_Type(Integer32):
    """Custom type dot11VlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 0))
    )


_Dot11VlanMode_Type.__name__ = "Integer32"
_Dot11VlanMode_Object = MibScalar
dot11VlanMode = _Dot11VlanMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 2),
    _Dot11VlanMode_Type()
)
dot11VlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11VlanMode.setStatus("mandatory")
_Dot11GroupVlanListTable_Object = MibTable
dot11GroupVlanListTable = _Dot11GroupVlanListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    dot11GroupVlanListTable.setStatus("mandatory")
_Dot11GroupVlanListEntry_Object = MibTableRow
dot11GroupVlanListEntry = _Dot11GroupVlanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1)
)
dot11GroupVlanListEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11GroupVlanListIndex"),
)
if mibBuilder.loadTexts:
    dot11GroupVlanListEntry.setStatus("mandatory")
_Dot11GroupVlanListIndex_Type = Integer32
_Dot11GroupVlanListIndex_Object = MibTableColumn
dot11GroupVlanListIndex = _Dot11GroupVlanListIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 1),
    _Dot11GroupVlanListIndex_Type()
)
dot11GroupVlanListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11GroupVlanListIndex.setStatus("mandatory")
_Dot11GroupVlanListVid_Type = Integer32
_Dot11GroupVlanListVid_Object = MibTableColumn
dot11GroupVlanListVid = _Dot11GroupVlanListVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 2),
    _Dot11GroupVlanListVid_Type()
)
dot11GroupVlanListVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListVid.setStatus("mandatory")


class _Dot11GroupVlanListName_Type(OctetString):
    """Custom type dot11GroupVlanListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Dot11GroupVlanListName_Type.__name__ = "OctetString"
_Dot11GroupVlanListName_Object = MibTableColumn
dot11GroupVlanListName = _Dot11GroupVlanListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 3),
    _Dot11GroupVlanListName_Type()
)
dot11GroupVlanListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListName.setStatus("mandatory")


class _Dot11GroupVlanListMgmt_Type(Integer32):
    """Custom type dot11GroupVlanListMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tag", 1),
          ("untag", 2))
    )


_Dot11GroupVlanListMgmt_Type.__name__ = "Integer32"
_Dot11GroupVlanListMgmt_Object = MibTableColumn
dot11GroupVlanListMgmt = _Dot11GroupVlanListMgmt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 4),
    _Dot11GroupVlanListMgmt_Type()
)
dot11GroupVlanListMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListMgmt.setStatus("mandatory")


class _Dot11GroupVlanListLan_Type(Integer32):
    """Custom type dot11GroupVlanListLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tag", 1),
          ("untag", 2))
    )


_Dot11GroupVlanListLan_Type.__name__ = "Integer32"
_Dot11GroupVlanListLan_Object = MibTableColumn
dot11GroupVlanListLan = _Dot11GroupVlanListLan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 5),
    _Dot11GroupVlanListLan_Type()
)
dot11GroupVlanListLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListLan.setStatus("mandatory")


class _Dot11GroupVlanListPrimary_Type(Integer32):
    """Custom type dot11GroupVlanListPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tag", 1),
          ("untag", 2))
    )


_Dot11GroupVlanListPrimary_Type.__name__ = "Integer32"
_Dot11GroupVlanListPrimary_Object = MibTableColumn
dot11GroupVlanListPrimary = _Dot11GroupVlanListPrimary_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 6),
    _Dot11GroupVlanListPrimary_Type()
)
dot11GroupVlanListPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListPrimary.setStatus("mandatory")


class _Dot11GroupVlanListMssid1_Type(Integer32):
    """Custom type dot11GroupVlanListMssid1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tag", 1),
          ("untag", 2))
    )


_Dot11GroupVlanListMssid1_Type.__name__ = "Integer32"
_Dot11GroupVlanListMssid1_Object = MibTableColumn
dot11GroupVlanListMssid1 = _Dot11GroupVlanListMssid1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 7),
    _Dot11GroupVlanListMssid1_Type()
)
dot11GroupVlanListMssid1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListMssid1.setStatus("mandatory")


class _Dot11GroupVlanListMssid2_Type(Integer32):
    """Custom type dot11GroupVlanListMssid2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tag", 1),
          ("untag", 2))
    )


_Dot11GroupVlanListMssid2_Type.__name__ = "Integer32"
_Dot11GroupVlanListMssid2_Object = MibTableColumn
dot11GroupVlanListMssid2 = _Dot11GroupVlanListMssid2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 8),
    _Dot11GroupVlanListMssid2_Type()
)
dot11GroupVlanListMssid2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListMssid2.setStatus("mandatory")


class _Dot11GroupVlanListMssid3_Type(Integer32):
    """Custom type dot11GroupVlanListMssid3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tag", 1),
          ("untag", 2))
    )


_Dot11GroupVlanListMssid3_Type.__name__ = "Integer32"
_Dot11GroupVlanListMssid3_Object = MibTableColumn
dot11GroupVlanListMssid3 = _Dot11GroupVlanListMssid3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 9),
    _Dot11GroupVlanListMssid3_Type()
)
dot11GroupVlanListMssid3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListMssid3.setStatus("mandatory")


class _Dot11GroupVlanListWds1_Type(Integer32):
    """Custom type dot11GroupVlanListWds1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tag", 1),
          ("untag", 2))
    )


_Dot11GroupVlanListWds1_Type.__name__ = "Integer32"
_Dot11GroupVlanListWds1_Object = MibTableColumn
dot11GroupVlanListWds1 = _Dot11GroupVlanListWds1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 14),
    _Dot11GroupVlanListWds1_Type()
)
dot11GroupVlanListWds1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListWds1.setStatus("mandatory")


class _Dot11GroupVlanListWds2_Type(Integer32):
    """Custom type dot11GroupVlanListWds2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tag", 1),
          ("untag", 2))
    )


_Dot11GroupVlanListWds2_Type.__name__ = "Integer32"
_Dot11GroupVlanListWds2_Object = MibTableColumn
dot11GroupVlanListWds2 = _Dot11GroupVlanListWds2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 15),
    _Dot11GroupVlanListWds2_Type()
)
dot11GroupVlanListWds2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListWds2.setStatus("mandatory")


class _Dot11GroupVlanListWds3_Type(Integer32):
    """Custom type dot11GroupVlanListWds3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tag", 1),
          ("untag", 2))
    )


_Dot11GroupVlanListWds3_Type.__name__ = "Integer32"
_Dot11GroupVlanListWds3_Object = MibTableColumn
dot11GroupVlanListWds3 = _Dot11GroupVlanListWds3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 16),
    _Dot11GroupVlanListWds3_Type()
)
dot11GroupVlanListWds3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListWds3.setStatus("mandatory")


class _Dot11GroupVlanListWds4_Type(Integer32):
    """Custom type dot11GroupVlanListWds4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tag", 1),
          ("untag", 2))
    )


_Dot11GroupVlanListWds4_Type.__name__ = "Integer32"
_Dot11GroupVlanListWds4_Object = MibTableColumn
dot11GroupVlanListWds4 = _Dot11GroupVlanListWds4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 17),
    _Dot11GroupVlanListWds4_Type()
)
dot11GroupVlanListWds4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11GroupVlanListWds4.setStatus("mandatory")


class _Dot11VlanListSurveydelete_Type(Integer32):
    """Custom type dot11VlanListSurveydelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("nothing", 0))
    )


_Dot11VlanListSurveydelete_Type.__name__ = "Integer32"
_Dot11VlanListSurveydelete_Object = MibTableColumn
dot11VlanListSurveydelete = _Dot11VlanListSurveydelete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 1, 3, 1, 22),
    _Dot11VlanListSurveydelete_Type()
)
dot11VlanListSurveydelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11VlanListSurveydelete.setStatus("mandatory")
_Dot11PvidSettingRecord_ObjectIdentity = ObjectIdentity
dot11PvidSettingRecord = _Dot11PvidSettingRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2)
)


class _Dot11PvidAutoAssignStatus_Type(Integer32):
    """Custom type dot11PvidAutoAssignStatus based on Integer32"""
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


_Dot11PvidAutoAssignStatus_Type.__name__ = "Integer32"
_Dot11PvidAutoAssignStatus_Object = MibScalar
dot11PvidAutoAssignStatus = _Dot11PvidAutoAssignStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 1),
    _Dot11PvidAutoAssignStatus_Type()
)
dot11PvidAutoAssignStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PvidAutoAssignStatus.setStatus("mandatory")
_Dot11PvidSettingTable_Object = MibTable
dot11PvidSettingTable = _Dot11PvidSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2)
)
if mibBuilder.loadTexts:
    dot11PvidSettingTable.setStatus("mandatory")
_Dot11PvidSettingEntry_Object = MibTableRow
dot11PvidSettingEntry = _Dot11PvidSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1)
)
dot11PvidSettingEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11PvidSettingIndex"),
)
if mibBuilder.loadTexts:
    dot11PvidSettingEntry.setStatus("mandatory")
_Dot11PvidSettingIndex_Type = Integer32
_Dot11PvidSettingIndex_Object = MibTableColumn
dot11PvidSettingIndex = _Dot11PvidSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1, 1),
    _Dot11PvidSettingIndex_Type()
)
dot11PvidSettingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11PvidSettingIndex.setStatus("mandatory")


class _Dot11PvidSettingMgmt_Type(Integer32):
    """Custom type dot11PvidSettingMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot11PvidSettingMgmt_Type.__name__ = "Integer32"
_Dot11PvidSettingMgmt_Object = MibTableColumn
dot11PvidSettingMgmt = _Dot11PvidSettingMgmt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1, 2),
    _Dot11PvidSettingMgmt_Type()
)
dot11PvidSettingMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PvidSettingMgmt.setStatus("mandatory")


class _Dot11PvidSettingLan_Type(Integer32):
    """Custom type dot11PvidSettingLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot11PvidSettingLan_Type.__name__ = "Integer32"
_Dot11PvidSettingLan_Object = MibTableColumn
dot11PvidSettingLan = _Dot11PvidSettingLan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1, 3),
    _Dot11PvidSettingLan_Type()
)
dot11PvidSettingLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PvidSettingLan.setStatus("mandatory")


class _Dot11PvidSettingPrimary_Type(Integer32):
    """Custom type dot11PvidSettingPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot11PvidSettingPrimary_Type.__name__ = "Integer32"
_Dot11PvidSettingPrimary_Object = MibTableColumn
dot11PvidSettingPrimary = _Dot11PvidSettingPrimary_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1, 4),
    _Dot11PvidSettingPrimary_Type()
)
dot11PvidSettingPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PvidSettingPrimary.setStatus("mandatory")


class _Dot11PvidSettingMssid1_Type(Integer32):
    """Custom type dot11PvidSettingMssid1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot11PvidSettingMssid1_Type.__name__ = "Integer32"
_Dot11PvidSettingMssid1_Object = MibTableColumn
dot11PvidSettingMssid1 = _Dot11PvidSettingMssid1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1, 5),
    _Dot11PvidSettingMssid1_Type()
)
dot11PvidSettingMssid1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PvidSettingMssid1.setStatus("mandatory")


class _Dot11PvidSettingMssid2_Type(Integer32):
    """Custom type dot11PvidSettingMssid2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot11PvidSettingMssid2_Type.__name__ = "Integer32"
_Dot11PvidSettingMssid2_Object = MibTableColumn
dot11PvidSettingMssid2 = _Dot11PvidSettingMssid2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1, 6),
    _Dot11PvidSettingMssid2_Type()
)
dot11PvidSettingMssid2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PvidSettingMssid2.setStatus("mandatory")


class _Dot11PvidSettingMssid3_Type(Integer32):
    """Custom type dot11PvidSettingMssid3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot11PvidSettingMssid3_Type.__name__ = "Integer32"
_Dot11PvidSettingMssid3_Object = MibTableColumn
dot11PvidSettingMssid3 = _Dot11PvidSettingMssid3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1, 7),
    _Dot11PvidSettingMssid3_Type()
)
dot11PvidSettingMssid3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PvidSettingMssid3.setStatus("mandatory")


class _Dot11PvidSettingWds1_Type(Integer32):
    """Custom type dot11PvidSettingWds1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot11PvidSettingWds1_Type.__name__ = "Integer32"
_Dot11PvidSettingWds1_Object = MibTableColumn
dot11PvidSettingWds1 = _Dot11PvidSettingWds1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1, 12),
    _Dot11PvidSettingWds1_Type()
)
dot11PvidSettingWds1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PvidSettingWds1.setStatus("mandatory")


class _Dot11PvidSettingWds2_Type(Integer32):
    """Custom type dot11PvidSettingWds2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot11PvidSettingWds2_Type.__name__ = "Integer32"
_Dot11PvidSettingWds2_Object = MibTableColumn
dot11PvidSettingWds2 = _Dot11PvidSettingWds2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1, 13),
    _Dot11PvidSettingWds2_Type()
)
dot11PvidSettingWds2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PvidSettingWds2.setStatus("mandatory")


class _Dot11PvidSettingWds3_Type(Integer32):
    """Custom type dot11PvidSettingWds3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot11PvidSettingWds3_Type.__name__ = "Integer32"
_Dot11PvidSettingWds3_Object = MibTableColumn
dot11PvidSettingWds3 = _Dot11PvidSettingWds3_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1, 14),
    _Dot11PvidSettingWds3_Type()
)
dot11PvidSettingWds3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PvidSettingWds3.setStatus("mandatory")


class _Dot11PvidSettingWds4_Type(Integer32):
    """Custom type dot11PvidSettingWds4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot11PvidSettingWds4_Type.__name__ = "Integer32"
_Dot11PvidSettingWds4_Object = MibTableColumn
dot11PvidSettingWds4 = _Dot11PvidSettingWds4_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 2, 2, 1, 15),
    _Dot11PvidSettingWds4_Type()
)
dot11PvidSettingWds4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PvidSettingWds4.setStatus("mandatory")
_Dot11PortListRecord_ObjectIdentity = ObjectIdentity
dot11PortListRecord = _Dot11PortListRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 3)
)


class _Dot11PortListRefresh_Type(Integer32):
    """Custom type dot11PortListRefresh based on Integer32"""
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


_Dot11PortListRefresh_Type.__name__ = "Integer32"
_Dot11PortListRefresh_Object = MibScalar
dot11PortListRefresh = _Dot11PortListRefresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 3, 1),
    _Dot11PortListRefresh_Type()
)
dot11PortListRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PortListRefresh.setStatus("mandatory")
_Dot11PortListTable_Object = MibTable
dot11PortListTable = _Dot11PortListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 3, 2)
)
if mibBuilder.loadTexts:
    dot11PortListTable.setStatus("mandatory")
_Dot11PortListEntry_Object = MibTableRow
dot11PortListEntry = _Dot11PortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 3, 2, 1)
)
dot11PortListEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11PortListIndex"),
)
if mibBuilder.loadTexts:
    dot11PortListEntry.setStatus("mandatory")
_Dot11PortListIndex_Type = Integer32
_Dot11PortListIndex_Object = MibTableColumn
dot11PortListIndex = _Dot11PortListIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 3, 2, 1, 1),
    _Dot11PortListIndex_Type()
)
dot11PortListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11PortListIndex.setStatus("mandatory")
_Dot11PortListTagVid_Type = OctetString
_Dot11PortListTagVid_Object = MibTableColumn
dot11PortListTagVid = _Dot11PortListTagVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 3, 2, 1, 2),
    _Dot11PortListTagVid_Type()
)
dot11PortListTagVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PortListTagVid.setStatus("mandatory")
_Dot11PortListUntagVid_Type = OctetString
_Dot11PortListUntagVid_Object = MibTableColumn
dot11PortListUntagVid = _Dot11PortListUntagVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 3, 2, 1, 3),
    _Dot11PortListUntagVid_Type()
)
dot11PortListUntagVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PortListUntagVid.setStatus("mandatory")
_Dot11PortLisPortName_Type = OctetString
_Dot11PortLisPortName_Object = MibTableColumn
dot11PortLisPortName = _Dot11PortLisPortName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 6, 3, 2, 1, 4),
    _Dot11PortLisPortName_Type()
)
dot11PortLisPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PortLisPortName.setStatus("mandatory")
_Ieee802dot11Qos_ObjectIdentity = ObjectIdentity
ieee802dot11Qos = _Ieee802dot11Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7)
)


class _Dot11QosStatus_Type(Integer32):
    """Custom type dot11QosStatus based on Integer32"""
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


_Dot11QosStatus_Type.__name__ = "Integer32"
_Dot11QosStatus_Object = MibScalar
dot11QosStatus = _Dot11QosStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 1),
    _Dot11QosStatus_Type()
)
dot11QosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosStatus.setStatus("mandatory")
_Dot11QosPriorityClassifiers_ObjectIdentity = ObjectIdentity
dot11QosPriorityClassifiers = _Dot11QosPriorityClassifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2)
)


class _Dot11QosHttp_Type(Integer32):
    """Custom type dot11QosHttp based on Integer32"""
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


_Dot11QosHttp_Type.__name__ = "Integer32"
_Dot11QosHttp_Object = MibScalar
dot11QosHttp = _Dot11QosHttp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 1),
    _Dot11QosHttp_Type()
)
dot11QosHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosHttp.setStatus("mandatory")


class _Dot11QosAutomatic_Type(Integer32):
    """Custom type dot11QosAutomatic based on Integer32"""
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


_Dot11QosAutomatic_Type.__name__ = "Integer32"
_Dot11QosAutomatic_Object = MibScalar
dot11QosAutomatic = _Dot11QosAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 2),
    _Dot11QosAutomatic_Type()
)
dot11QosAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosAutomatic.setStatus("mandatory")


class _Dot11QosRuleStatus_Type(Integer32):
    """Custom type dot11QosRuleStatus based on Integer32"""
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


_Dot11QosRuleStatus_Type.__name__ = "Integer32"
_Dot11QosRuleStatus_Object = MibScalar
dot11QosRuleStatus = _Dot11QosRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 3),
    _Dot11QosRuleStatus_Type()
)
dot11QosRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRuleStatus.setStatus("mandatory")


class _Dot11QosRulesDelete_Type(Integer32):
    """Custom type dot11QosRulesDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Dot11QosRulesDelete_Type.__name__ = "Integer32"
_Dot11QosRulesDelete_Object = MibScalar
dot11QosRulesDelete = _Dot11QosRulesDelete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 4),
    _Dot11QosRulesDelete_Type()
)
dot11QosRulesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesDelete.setStatus("mandatory")
_Dot11QosRulesTable_Object = MibTable
dot11QosRulesTable = _Dot11QosRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5)
)
if mibBuilder.loadTexts:
    dot11QosRulesTable.setStatus("mandatory")
_Dot11QosRulesEntry_Object = MibTableRow
dot11QosRulesEntry = _Dot11QosRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1)
)
dot11QosRulesEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11QosRulesIndex"),
)
if mibBuilder.loadTexts:
    dot11QosRulesEntry.setStatus("mandatory")
_Dot11QosRulesIndex_Type = Integer32
_Dot11QosRulesIndex_Object = MibTableColumn
dot11QosRulesIndex = _Dot11QosRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 1),
    _Dot11QosRulesIndex_Type()
)
dot11QosRulesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11QosRulesIndex.setStatus("mandatory")


class _Dot11QosRulesState_Type(Integer32):
    """Custom type dot11QosRulesState based on Integer32"""
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


_Dot11QosRulesState_Type.__name__ = "Integer32"
_Dot11QosRulesState_Object = MibTableColumn
dot11QosRulesState = _Dot11QosRulesState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 2),
    _Dot11QosRulesState_Type()
)
dot11QosRulesState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesState.setStatus("mandatory")


class _Dot11QosRulesName_Type(OctetString):
    """Custom type dot11QosRulesName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Dot11QosRulesName_Type.__name__ = "OctetString"
_Dot11QosRulesName_Object = MibTableColumn
dot11QosRulesName = _Dot11QosRulesName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 3),
    _Dot11QosRulesName_Type()
)
dot11QosRulesName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesName.setStatus("mandatory")


class _Dot11QosRulesPriority_Type(Integer32):
    """Custom type dot11QosRulesPriority based on Integer32"""
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
        *(("be", 2),
          ("bk", 3),
          ("vi", 1),
          ("vo", 0))
    )


_Dot11QosRulesPriority_Type.__name__ = "Integer32"
_Dot11QosRulesPriority_Object = MibTableColumn
dot11QosRulesPriority = _Dot11QosRulesPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 4),
    _Dot11QosRulesPriority_Type()
)
dot11QosRulesPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesPriority.setStatus("mandatory")


class _Dot11QosRulesProtocol_Type(Integer32):
    """Custom type dot11QosRulesProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Dot11QosRulesProtocol_Type.__name__ = "Integer32"
_Dot11QosRulesProtocol_Object = MibTableColumn
dot11QosRulesProtocol = _Dot11QosRulesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 5),
    _Dot11QosRulesProtocol_Type()
)
dot11QosRulesProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesProtocol.setStatus("mandatory")


class _Dot11QosRulesProtocolType_Type(Integer32):
    """Custom type dot11QosRulesProtocolType based on Integer32"""
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
        *(("any", 0),
          ("both", 3),
          ("icmp", 4),
          ("other", 5),
          ("tcp", 1),
          ("udp", 2))
    )


_Dot11QosRulesProtocolType_Type.__name__ = "Integer32"
_Dot11QosRulesProtocolType_Object = MibTableColumn
dot11QosRulesProtocolType = _Dot11QosRulesProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 6),
    _Dot11QosRulesProtocolType_Type()
)
dot11QosRulesProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesProtocolType.setStatus("mandatory")
_Dot11QosRulesHostOneIpStart_Type = IpAddress
_Dot11QosRulesHostOneIpStart_Object = MibTableColumn
dot11QosRulesHostOneIpStart = _Dot11QosRulesHostOneIpStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 7),
    _Dot11QosRulesHostOneIpStart_Type()
)
dot11QosRulesHostOneIpStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostOneIpStart.setStatus("mandatory")
_Dot11QosRulesHostOneIpEnd_Type = IpAddress
_Dot11QosRulesHostOneIpEnd_Object = MibTableColumn
dot11QosRulesHostOneIpEnd = _Dot11QosRulesHostOneIpEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 8),
    _Dot11QosRulesHostOneIpEnd_Type()
)
dot11QosRulesHostOneIpEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostOneIpEnd.setStatus("mandatory")
_Dot11QosRulesHostOneIpRange_Type = Integer32
_Dot11QosRulesHostOneIpRange_Object = MibTableColumn
dot11QosRulesHostOneIpRange = _Dot11QosRulesHostOneIpRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 9),
    _Dot11QosRulesHostOneIpRange_Type()
)
dot11QosRulesHostOneIpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostOneIpRange.setStatus("mandatory")
_Dot11QosRulesHostOnePortStart_Type = Integer32
_Dot11QosRulesHostOnePortStart_Object = MibTableColumn
dot11QosRulesHostOnePortStart = _Dot11QosRulesHostOnePortStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 10),
    _Dot11QosRulesHostOnePortStart_Type()
)
dot11QosRulesHostOnePortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostOnePortStart.setStatus("mandatory")
_Dot11QosRulesHostOnePortEnd_Type = Integer32
_Dot11QosRulesHostOnePortEnd_Object = MibTableColumn
dot11QosRulesHostOnePortEnd = _Dot11QosRulesHostOnePortEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 11),
    _Dot11QosRulesHostOnePortEnd_Type()
)
dot11QosRulesHostOnePortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostOnePortEnd.setStatus("mandatory")
_Dot11QosRulesHostOnePortRange_Type = Integer32
_Dot11QosRulesHostOnePortRange_Object = MibTableColumn
dot11QosRulesHostOnePortRange = _Dot11QosRulesHostOnePortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 12),
    _Dot11QosRulesHostOnePortRange_Type()
)
dot11QosRulesHostOnePortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostOnePortRange.setStatus("mandatory")
_Dot11QosRulesHostTwoIpStart_Type = IpAddress
_Dot11QosRulesHostTwoIpStart_Object = MibTableColumn
dot11QosRulesHostTwoIpStart = _Dot11QosRulesHostTwoIpStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 13),
    _Dot11QosRulesHostTwoIpStart_Type()
)
dot11QosRulesHostTwoIpStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostTwoIpStart.setStatus("mandatory")
_Dot11QosRulesHostTwoIpEnd_Type = IpAddress
_Dot11QosRulesHostTwoIpEnd_Object = MibTableColumn
dot11QosRulesHostTwoIpEnd = _Dot11QosRulesHostTwoIpEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 14),
    _Dot11QosRulesHostTwoIpEnd_Type()
)
dot11QosRulesHostTwoIpEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostTwoIpEnd.setStatus("mandatory")
_Dot11QosRulesHostTwoIpRange_Type = Integer32
_Dot11QosRulesHostTwoIpRange_Object = MibTableColumn
dot11QosRulesHostTwoIpRange = _Dot11QosRulesHostTwoIpRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 15),
    _Dot11QosRulesHostTwoIpRange_Type()
)
dot11QosRulesHostTwoIpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostTwoIpRange.setStatus("mandatory")
_Dot11QosRulesHostTwoPortStart_Type = Integer32
_Dot11QosRulesHostTwoPortStart_Object = MibTableColumn
dot11QosRulesHostTwoPortStart = _Dot11QosRulesHostTwoPortStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 16),
    _Dot11QosRulesHostTwoPortStart_Type()
)
dot11QosRulesHostTwoPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostTwoPortStart.setStatus("mandatory")
_Dot11QosRulesHostTwoPortEnd_Type = Integer32
_Dot11QosRulesHostTwoPortEnd_Object = MibTableColumn
dot11QosRulesHostTwoPortEnd = _Dot11QosRulesHostTwoPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 17),
    _Dot11QosRulesHostTwoPortEnd_Type()
)
dot11QosRulesHostTwoPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostTwoPortEnd.setStatus("mandatory")
_Dot11QosRulesHostTwoPortRange_Type = Integer32
_Dot11QosRulesHostTwoPortRange_Object = MibTableColumn
dot11QosRulesHostTwoPortRange = _Dot11QosRulesHostTwoPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 7, 2, 5, 1, 18),
    _Dot11QosRulesHostTwoPortRange_Type()
)
dot11QosRulesHostTwoPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11QosRulesHostTwoPortRange.setStatus("mandatory")
_Capwap_ObjectIdentity = ObjectIdentity
capwap = _Capwap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8)
)
_CapwapWlanSwitchSetting_ObjectIdentity = ObjectIdentity
capwapWlanSwitchSetting = _CapwapWlanSwitchSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1)
)


class _CapwapWtpStatus_Type(Integer32):
    """Custom type capwapWtpStatus based on Integer32"""
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


_CapwapWtpStatus_Type.__name__ = "Integer32"
_CapwapWtpStatus_Object = MibScalar
capwapWtpStatus = _CapwapWtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1, 1),
    _CapwapWtpStatus_Type()
)
capwapWtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWtpStatus.setStatus("mandatory")
_CapwapWtpName_Type = OctetString
_CapwapWtpName_Object = MibScalar
capwapWtpName = _CapwapWtpName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1, 2),
    _CapwapWtpName_Type()
)
capwapWtpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWtpName.setStatus("mandatory")
_CapwapWtpLocationData_Type = OctetString
_CapwapWtpLocationData_Object = MibScalar
capwapWtpLocationData = _CapwapWtpLocationData_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1, 3),
    _CapwapWtpLocationData_Type()
)
capwapWtpLocationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWtpLocationData.setStatus("mandatory")
_CapwapWtpConnectingSwitchIP_Type = IpAddress
_CapwapWtpConnectingSwitchIP_Object = MibScalar
capwapWtpConnectingSwitchIP = _CapwapWtpConnectingSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1, 4),
    _CapwapWtpConnectingSwitchIP_Type()
)
capwapWtpConnectingSwitchIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWtpConnectingSwitchIP.setStatus("mandatory")
_CapwapWtpConnectingSwitchName_Type = OctetString
_CapwapWtpConnectingSwitchName_Object = MibScalar
capwapWtpConnectingSwitchName = _CapwapWtpConnectingSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1, 5),
    _CapwapWtpConnectingSwitchName_Type()
)
capwapWtpConnectingSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapWtpConnectingSwitchName.setStatus("mandatory")


class _CapwapWtpSwitchIpAddressDelete_Type(Integer32):
    """Custom type capwapWtpSwitchIpAddressDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CapwapWtpSwitchIpAddressDelete_Type.__name__ = "Integer32"
_CapwapWtpSwitchIpAddressDelete_Object = MibScalar
capwapWtpSwitchIpAddressDelete = _CapwapWtpSwitchIpAddressDelete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1, 6),
    _CapwapWtpSwitchIpAddressDelete_Type()
)
capwapWtpSwitchIpAddressDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWtpSwitchIpAddressDelete.setStatus("mandatory")
_CapwapWtpSwitchIpAddressAdd_Type = IpAddress
_CapwapWtpSwitchIpAddressAdd_Object = MibScalar
capwapWtpSwitchIpAddressAdd = _CapwapWtpSwitchIpAddressAdd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1, 7),
    _CapwapWtpSwitchIpAddressAdd_Type()
)
capwapWtpSwitchIpAddressAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapWtpSwitchIpAddressAdd.setStatus("mandatory")
_WtpSwitchAddressListTable_Object = MibTable
wtpSwitchAddressListTable = _WtpSwitchAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1, 8)
)
if mibBuilder.loadTexts:
    wtpSwitchAddressListTable.setStatus("mandatory")
_WtpSwitchAddressListEntry_Object = MibTableRow
wtpSwitchAddressListEntry = _WtpSwitchAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1, 8, 1)
)
wtpSwitchAddressListEntry.setIndexNames(
    (0, "DAP-3520-v115", "wtpSwitchAddressIndex"),
)
if mibBuilder.loadTexts:
    wtpSwitchAddressListEntry.setStatus("mandatory")
_WtpSwitchAddressIndex_Type = Integer32
_WtpSwitchAddressIndex_Object = MibTableColumn
wtpSwitchAddressIndex = _WtpSwitchAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1, 8, 1, 1),
    _WtpSwitchAddressIndex_Type()
)
wtpSwitchAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wtpSwitchAddressIndex.setStatus("mandatory")
_WtpSwitchIpAddress_Type = IpAddress
_WtpSwitchIpAddress_Object = MibTableColumn
wtpSwitchIpAddress = _WtpSwitchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 8, 1, 8, 1, 2),
    _WtpSwitchIpAddress_Type()
)
wtpSwitchIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtpSwitchIpAddress.setStatus("mandatory")
_Ieee802dot11Schedule_ObjectIdentity = ObjectIdentity
ieee802dot11Schedule = _Ieee802dot11Schedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10)
)
_Ieee802dot11ScheduleSetting_ObjectIdentity = ObjectIdentity
ieee802dot11ScheduleSetting = _Ieee802dot11ScheduleSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1)
)
_Ieee802dot11ScheduleStatus_ObjectIdentity = ObjectIdentity
ieee802dot11ScheduleStatus = _Ieee802dot11ScheduleStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 1)
)


class _Dot11ScheduleStatus_Type(Integer32):
    """Custom type dot11ScheduleStatus based on Integer32"""
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


_Dot11ScheduleStatus_Type.__name__ = "Integer32"
_Dot11ScheduleStatus_Object = MibScalar
dot11ScheduleStatus = _Dot11ScheduleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 1, 1),
    _Dot11ScheduleStatus_Type()
)
dot11ScheduleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleStatus.setStatus("mandatory")
_Ieee802dot11ScheduleRuleSetting_ObjectIdentity = ObjectIdentity
ieee802dot11ScheduleRuleSetting = _Ieee802dot11ScheduleRuleSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 2)
)


class _Dot11ScheduleRuleName_Type(OctetString):
    """Custom type dot11ScheduleRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11ScheduleRuleName_Type.__name__ = "OctetString"
_Dot11ScheduleRuleName_Object = MibScalar
dot11ScheduleRuleName = _Dot11ScheduleRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 2, 1),
    _Dot11ScheduleRuleName_Type()
)
dot11ScheduleRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleRuleName.setStatus("mandatory")
_Dot11ScheduleDaysSelect_Type = Integer32
_Dot11ScheduleDaysSelect_Object = MibScalar
dot11ScheduleDaysSelect = _Dot11ScheduleDaysSelect_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 2, 2),
    _Dot11ScheduleDaysSelect_Type()
)
dot11ScheduleDaysSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleDaysSelect.setStatus("mandatory")


class _Dot11ScheduleAllDaySelect_Type(Integer32):
    """Custom type dot11ScheduleAllDaySelect based on Integer32"""
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


_Dot11ScheduleAllDaySelect_Type.__name__ = "Integer32"
_Dot11ScheduleAllDaySelect_Object = MibScalar
dot11ScheduleAllDaySelect = _Dot11ScheduleAllDaySelect_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 2, 3),
    _Dot11ScheduleAllDaySelect_Type()
)
dot11ScheduleAllDaySelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleAllDaySelect.setStatus("mandatory")


class _Dot11ScheduleRuleStartTime_Type(OctetString):
    """Custom type dot11ScheduleRuleStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Dot11ScheduleRuleStartTime_Type.__name__ = "OctetString"
_Dot11ScheduleRuleStartTime_Object = MibScalar
dot11ScheduleRuleStartTime = _Dot11ScheduleRuleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 2, 4),
    _Dot11ScheduleRuleStartTime_Type()
)
dot11ScheduleRuleStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleRuleStartTime.setStatus("mandatory")


class _Dot11ScheduleRuleEndTime_Type(OctetString):
    """Custom type dot11ScheduleRuleEndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Dot11ScheduleRuleEndTime_Type.__name__ = "OctetString"
_Dot11ScheduleRuleEndTime_Object = MibScalar
dot11ScheduleRuleEndTime = _Dot11ScheduleRuleEndTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 2, 5),
    _Dot11ScheduleRuleEndTime_Type()
)
dot11ScheduleRuleEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleRuleEndTime.setStatus("mandatory")


class _Dot11ScheduleAction_Type(Integer32):
    """Custom type dot11ScheduleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 0))
    )


_Dot11ScheduleAction_Type.__name__ = "Integer32"
_Dot11ScheduleAction_Object = MibScalar
dot11ScheduleAction = _Dot11ScheduleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 2, 7),
    _Dot11ScheduleAction_Type()
)
dot11ScheduleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleAction.setStatus("mandatory")


class _Dot11ScheduleSSIDIndex_Type(Integer32):
    """Custom type dot11ScheduleSSIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dot11ScheduleSSIDIndex_Type.__name__ = "Integer32"
_Dot11ScheduleSSIDIndex_Object = MibScalar
dot11ScheduleSSIDIndex = _Dot11ScheduleSSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 2, 8),
    _Dot11ScheduleSSIDIndex_Type()
)
dot11ScheduleSSIDIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleSSIDIndex.setStatus("mandatory")


class _Dot11ScheduleNodeStatus_Type(Integer32):
    """Custom type dot11ScheduleNodeStatus based on Integer32"""
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


_Dot11ScheduleNodeStatus_Type.__name__ = "Integer32"
_Dot11ScheduleNodeStatus_Object = MibScalar
dot11ScheduleNodeStatus = _Dot11ScheduleNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 2, 9),
    _Dot11ScheduleNodeStatus_Type()
)
dot11ScheduleNodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleNodeStatus.setStatus("mandatory")


class _Dot11ScheduleOverNight_Type(Integer32):
    """Custom type dot11ScheduleOverNight based on Integer32"""
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


_Dot11ScheduleOverNight_Type.__name__ = "Integer32"
_Dot11ScheduleOverNight_Object = MibScalar
dot11ScheduleOverNight = _Dot11ScheduleOverNight_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 1, 2, 10),
    _Dot11ScheduleOverNight_Type()
)
dot11ScheduleOverNight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleOverNight.setStatus("mandatory")
_Ieee802dot11ScheduleList_ObjectIdentity = ObjectIdentity
ieee802dot11ScheduleList = _Ieee802dot11ScheduleList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2)
)
_Dot11ScheduleListTable_Object = MibTable
dot11ScheduleListTable = _Dot11ScheduleListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2, 1)
)
if mibBuilder.loadTexts:
    dot11ScheduleListTable.setStatus("mandatory")
_Dot11ScheduleListEntry_Object = MibTableRow
dot11ScheduleListEntry = _Dot11ScheduleListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2, 1, 1)
)
dot11ScheduleListEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11ScheduleListIndex"),
)
if mibBuilder.loadTexts:
    dot11ScheduleListEntry.setStatus("mandatory")
_Dot11ScheduleListIndex_Type = Integer32
_Dot11ScheduleListIndex_Object = MibTableColumn
dot11ScheduleListIndex = _Dot11ScheduleListIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2, 1, 1, 1),
    _Dot11ScheduleListIndex_Type()
)
dot11ScheduleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11ScheduleListIndex.setStatus("mandatory")


class _Dot11ScheduleListName_Type(OctetString):
    """Custom type dot11ScheduleListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11ScheduleListName_Type.__name__ = "OctetString"
_Dot11ScheduleListName_Object = MibTableColumn
dot11ScheduleListName = _Dot11ScheduleListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2, 1, 1, 2),
    _Dot11ScheduleListName_Type()
)
dot11ScheduleListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleListName.setStatus("mandatory")


class _Dot11ScheduleListDays_Type(OctetString):
    """Custom type dot11ScheduleListDays based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11ScheduleListDays_Type.__name__ = "OctetString"
_Dot11ScheduleListDays_Object = MibTableColumn
dot11ScheduleListDays = _Dot11ScheduleListDays_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2, 1, 1, 3),
    _Dot11ScheduleListDays_Type()
)
dot11ScheduleListDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleListDays.setStatus("mandatory")


class _Dot11ScheduleListTimeFrame_Type(OctetString):
    """Custom type dot11ScheduleListTimeFrame based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11ScheduleListTimeFrame_Type.__name__ = "OctetString"
_Dot11ScheduleListTimeFrame_Object = MibTableColumn
dot11ScheduleListTimeFrame = _Dot11ScheduleListTimeFrame_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2, 1, 1, 4),
    _Dot11ScheduleListTimeFrame_Type()
)
dot11ScheduleListTimeFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleListTimeFrame.setStatus("mandatory")


class _Dot11ScheduleListWirelessStatus_Type(Integer32):
    """Custom type dot11ScheduleListWirelessStatus based on Integer32"""
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


_Dot11ScheduleListWirelessStatus_Type.__name__ = "Integer32"
_Dot11ScheduleListWirelessStatus_Object = MibTableColumn
dot11ScheduleListWirelessStatus = _Dot11ScheduleListWirelessStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2, 1, 1, 5),
    _Dot11ScheduleListWirelessStatus_Type()
)
dot11ScheduleListWirelessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleListWirelessStatus.setStatus("mandatory")


class _Dot11ScheduleListSSIDIndex_Type(Integer32):
    """Custom type dot11ScheduleListSSIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dot11ScheduleListSSIDIndex_Type.__name__ = "Integer32"
_Dot11ScheduleListSSIDIndex_Object = MibTableColumn
dot11ScheduleListSSIDIndex = _Dot11ScheduleListSSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2, 1, 1, 6),
    _Dot11ScheduleListSSIDIndex_Type()
)
dot11ScheduleListSSIDIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleListSSIDIndex.setStatus("mandatory")


class _Dot11ScheduleListSSID_Type(OctetString):
    """Custom type dot11ScheduleListSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11ScheduleListSSID_Type.__name__ = "OctetString"
_Dot11ScheduleListSSID_Object = MibTableColumn
dot11ScheduleListSSID = _Dot11ScheduleListSSID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2, 1, 1, 7),
    _Dot11ScheduleListSSID_Type()
)
dot11ScheduleListSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleListSSID.setStatus("mandatory")


class _Dot11ScheduleListNodeStatus_Type(Integer32):
    """Custom type dot11ScheduleListNodeStatus based on Integer32"""
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


_Dot11ScheduleListNodeStatus_Type.__name__ = "Integer32"
_Dot11ScheduleListNodeStatus_Object = MibTableColumn
dot11ScheduleListNodeStatus = _Dot11ScheduleListNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2, 1, 1, 8),
    _Dot11ScheduleListNodeStatus_Type()
)
dot11ScheduleListNodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleListNodeStatus.setStatus("mandatory")


class _Dot11ScheduleListOverNight_Type(Integer32):
    """Custom type dot11ScheduleListOverNight based on Integer32"""
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


_Dot11ScheduleListOverNight_Type.__name__ = "Integer32"
_Dot11ScheduleListOverNight_Object = MibTableColumn
dot11ScheduleListOverNight = _Dot11ScheduleListOverNight_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 10, 2, 1, 1, 9),
    _Dot11ScheduleListOverNight_Type()
)
dot11ScheduleListOverNight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ScheduleListOverNight.setStatus("mandatory")
_Ieee802dot11APArray_ObjectIdentity = ObjectIdentity
ieee802dot11APArray = _Ieee802dot11APArray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11)
)
_Ieee802dot11APArraySetting_ObjectIdentity = ObjectIdentity
ieee802dot11APArraySetting = _Ieee802dot11APArraySetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1)
)
_Ieee802dot11APArrayStatus_ObjectIdentity = ObjectIdentity
ieee802dot11APArrayStatus = _Ieee802dot11APArrayStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 1)
)


class _Dot11APArrayStatus_Type(Integer32):
    """Custom type dot11APArrayStatus based on Integer32"""
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


_Dot11APArrayStatus_Type.__name__ = "Integer32"
_Dot11APArrayStatus_Object = MibScalar
dot11APArrayStatus = _Dot11APArrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 1, 1),
    _Dot11APArrayStatus_Type()
)
dot11APArrayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArrayStatus.setStatus("mandatory")


class _Dot11APArrayModeSelect_Type(Integer32):
    """Custom type dot11APArrayModeSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("masterbackup", 2),
          ("slave", 3))
    )


_Dot11APArrayModeSelect_Type.__name__ = "Integer32"
_Dot11APArrayModeSelect_Object = MibScalar
dot11APArrayModeSelect = _Dot11APArrayModeSelect_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 1, 2),
    _Dot11APArrayModeSelect_Type()
)
dot11APArrayModeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArrayModeSelect.setStatus("mandatory")


class _Dot11ApArrayName_Type(OctetString):
    """Custom type dot11ApArrayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11ApArrayName_Type.__name__ = "OctetString"
_Dot11ApArrayName_Object = MibScalar
dot11ApArrayName = _Dot11ApArrayName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 1, 3),
    _Dot11ApArrayName_Type()
)
dot11ApArrayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ApArrayName.setStatus("mandatory")


class _Dot11ApArrayPassword_Type(OctetString):
    """Custom type dot11ApArrayPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Dot11ApArrayPassword_Type.__name__ = "OctetString"
_Dot11ApArrayPassword_Object = MibScalar
dot11ApArrayPassword = _Dot11ApArrayPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 1, 4),
    _Dot11ApArrayPassword_Type()
)
dot11ApArrayPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ApArrayPassword.setStatus("mandatory")
_Ieee802dot11APArrayScans_ObjectIdentity = ObjectIdentity
ieee802dot11APArrayScans = _Ieee802dot11APArrayScans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2)
)
_Ieee802dot11APArrayScanSetting_ObjectIdentity = ObjectIdentity
ieee802dot11APArrayScanSetting = _Ieee802dot11APArrayScanSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1)
)


class _Dot11ApArrayScan_Type(Integer32):
    """Custom type dot11ApArrayScan based on Integer32"""
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


_Dot11ApArrayScan_Type.__name__ = "Integer32"
_Dot11ApArrayScan_Object = MibScalar
dot11ApArrayScan = _Dot11ApArrayScan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 1),
    _Dot11ApArrayScan_Type()
)
dot11ApArrayScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ApArrayScan.setStatus("mandatory")
_Ieee802dot11APArrayScanList_ObjectIdentity = ObjectIdentity
ieee802dot11APArrayScanList = _Ieee802dot11APArrayScanList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 3)
)
_Dot11APArrayScanListTable_Object = MibTable
dot11APArrayScanListTable = _Dot11APArrayScanListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot11APArrayScanListTable.setStatus("mandatory")
_Dot11APArrayScanListEntry_Object = MibTableRow
dot11APArrayScanListEntry = _Dot11APArrayScanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 3, 1, 1)
)
dot11APArrayScanListEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11APArrayScanListIndex"),
)
if mibBuilder.loadTexts:
    dot11APArrayScanListEntry.setStatus("mandatory")
_Dot11APArrayScanListIndex_Type = Integer32
_Dot11APArrayScanListIndex_Object = MibTableColumn
dot11APArrayScanListIndex = _Dot11APArrayScanListIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 3, 1, 1, 1),
    _Dot11APArrayScanListIndex_Type()
)
dot11APArrayScanListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11APArrayScanListIndex.setStatus("mandatory")


class _Dot11APArrayScanListName_Type(OctetString):
    """Custom type dot11APArrayScanListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11APArrayScanListName_Type.__name__ = "OctetString"
_Dot11APArrayScanListName_Object = MibTableColumn
dot11APArrayScanListName = _Dot11APArrayScanListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 3, 1, 1, 2),
    _Dot11APArrayScanListName_Type()
)
dot11APArrayScanListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APArrayScanListName.setStatus("mandatory")
_Dot11APArrayScanListMasterIP_Type = IpAddress
_Dot11APArrayScanListMasterIP_Object = MibTableColumn
dot11APArrayScanListMasterIP = _Dot11APArrayScanListMasterIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 3, 1, 1, 3),
    _Dot11APArrayScanListMasterIP_Type()
)
dot11APArrayScanListMasterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APArrayScanListMasterIP.setStatus("mandatory")
_Dot11APArrayScanListMac_Type = MacAddress
_Dot11APArrayScanListMac_Object = MibTableColumn
dot11APArrayScanListMac = _Dot11APArrayScanListMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 3, 1, 1, 4),
    _Dot11APArrayScanListMac_Type()
)
dot11APArrayScanListMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APArrayScanListMac.setStatus("mandatory")
_Dot11APArrayScanListMasterNumber_Type = Integer32
_Dot11APArrayScanListMasterNumber_Object = MibTableColumn
dot11APArrayScanListMasterNumber = _Dot11APArrayScanListMasterNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 3, 1, 1, 5),
    _Dot11APArrayScanListMasterNumber_Type()
)
dot11APArrayScanListMasterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APArrayScanListMasterNumber.setStatus("mandatory")
_Dot11APArrayScanListBackupNumber_Type = Integer32
_Dot11APArrayScanListBackupNumber_Object = MibTableColumn
dot11APArrayScanListBackupNumber = _Dot11APArrayScanListBackupNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 3, 1, 1, 6),
    _Dot11APArrayScanListBackupNumber_Type()
)
dot11APArrayScanListBackupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APArrayScanListBackupNumber.setStatus("mandatory")
_Dot11APArrayScanListSlaverNumber_Type = Integer32
_Dot11APArrayScanListSlaverNumber_Object = MibTableColumn
dot11APArrayScanListSlaverNumber = _Dot11APArrayScanListSlaverNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 3, 1, 1, 7),
    _Dot11APArrayScanListSlaverNumber_Type()
)
dot11APArrayScanListSlaverNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APArrayScanListSlaverNumber.setStatus("mandatory")
_Dot11APArrayScanListTotal_Type = Integer32
_Dot11APArrayScanListTotal_Object = MibTableColumn
dot11APArrayScanListTotal = _Dot11APArrayScanListTotal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 1, 2, 1, 3, 1, 1, 8),
    _Dot11APArrayScanListTotal_Type()
)
dot11APArrayScanListTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APArrayScanListTotal.setStatus("mandatory")
_Ieee802dot11APArrayMeberList_ObjectIdentity = ObjectIdentity
ieee802dot11APArrayMeberList = _Ieee802dot11APArrayMeberList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 2)
)
_Dot11APArrayMeberListTable_Object = MibTable
dot11APArrayMeberListTable = _Dot11APArrayMeberListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 2, 1)
)
if mibBuilder.loadTexts:
    dot11APArrayMeberListTable.setStatus("mandatory")
_Dot11APArrayMeberListEntry_Object = MibTableRow
dot11APArrayMeberListEntry = _Dot11APArrayMeberListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 2, 1, 1)
)
dot11APArrayMeberListEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11APArrayMeberListIndex"),
)
if mibBuilder.loadTexts:
    dot11APArrayMeberListEntry.setStatus("mandatory")
_Dot11APArrayMeberListIndex_Type = Integer32
_Dot11APArrayMeberListIndex_Object = MibTableColumn
dot11APArrayMeberListIndex = _Dot11APArrayMeberListIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 2, 1, 1, 1),
    _Dot11APArrayMeberListIndex_Type()
)
dot11APArrayMeberListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11APArrayMeberListIndex.setStatus("mandatory")


class _Dot11APArrayMeberListRole_Type(Integer32):
    """Custom type dot11APArrayMeberListRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("masterbackup", 2),
          ("slave", 3))
    )


_Dot11APArrayMeberListRole_Type.__name__ = "Integer32"
_Dot11APArrayMeberListRole_Object = MibTableColumn
dot11APArrayMeberListRole = _Dot11APArrayMeberListRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 2, 1, 1, 3),
    _Dot11APArrayMeberListRole_Type()
)
dot11APArrayMeberListRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APArrayMeberListRole.setStatus("mandatory")
_Dot11APArrayMeberListIP_Type = IpAddress
_Dot11APArrayMeberListIP_Object = MibTableColumn
dot11APArrayMeberListIP = _Dot11APArrayMeberListIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 2, 1, 1, 4),
    _Dot11APArrayMeberListIP_Type()
)
dot11APArrayMeberListIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APArrayMeberListIP.setStatus("mandatory")
_Dot11APArrayMeberListMac_Type = MacAddress
_Dot11APArrayMeberListMac_Object = MibTableColumn
dot11APArrayMeberListMac = _Dot11APArrayMeberListMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 2, 1, 1, 5),
    _Dot11APArrayMeberListMac_Type()
)
dot11APArrayMeberListMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APArrayMeberListMac.setStatus("mandatory")


class _Dot11APArrayMeberListLoacation_Type(OctetString):
    """Custom type dot11APArrayMeberListLoacation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Dot11APArrayMeberListLoacation_Type.__name__ = "OctetString"
_Dot11APArrayMeberListLoacation_Object = MibTableColumn
dot11APArrayMeberListLoacation = _Dot11APArrayMeberListLoacation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 2, 1, 1, 6),
    _Dot11APArrayMeberListLoacation_Type()
)
dot11APArrayMeberListLoacation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11APArrayMeberListLoacation.setStatus("mandatory")
_Ieee802dot11APArraySyncParametersStatus_ObjectIdentity = ObjectIdentity
ieee802dot11APArraySyncParametersStatus = _Ieee802dot11APArraySyncParametersStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3)
)
_Dot11APArraySyncParametersStatusTable_Object = MibTable
dot11APArraySyncParametersStatusTable = _Dot11APArraySyncParametersStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1)
)
if mibBuilder.loadTexts:
    dot11APArraySyncParametersStatusTable.setStatus("mandatory")
_Dot11APArraySyncParametersStatusEntry_Object = MibTableRow
dot11APArraySyncParametersStatusEntry = _Dot11APArraySyncParametersStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1)
)
dot11APArraySyncParametersStatusEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11APArraySyncParametersStatusIndex"),
)
if mibBuilder.loadTexts:
    dot11APArraySyncParametersStatusEntry.setStatus("mandatory")
_Dot11APArraySyncParametersStatusIndex_Type = Integer32
_Dot11APArraySyncParametersStatusIndex_Object = MibTableColumn
dot11APArraySyncParametersStatusIndex = _Dot11APArraySyncParametersStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 1),
    _Dot11APArraySyncParametersStatusIndex_Type()
)
dot11APArraySyncParametersStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11APArraySyncParametersStatusIndex.setStatus("mandatory")


class _Dot11APArraySyncSSIDStatus_Type(Integer32):
    """Custom type dot11APArraySyncSSIDStatus based on Integer32"""
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


_Dot11APArraySyncSSIDStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncSSIDStatus_Object = MibTableColumn
dot11APArraySyncSSIDStatus = _Dot11APArraySyncSSIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 2),
    _Dot11APArraySyncSSIDStatus_Type()
)
dot11APArraySyncSSIDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncSSIDStatus.setStatus("mandatory")


class _Dot11APArraySyncSsidHiddenStatus_Type(Integer32):
    """Custom type dot11APArraySyncSsidHiddenStatus based on Integer32"""
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


_Dot11APArraySyncSsidHiddenStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncSsidHiddenStatus_Object = MibTableColumn
dot11APArraySyncSsidHiddenStatus = _Dot11APArraySyncSsidHiddenStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 3),
    _Dot11APArraySyncSsidHiddenStatus_Type()
)
dot11APArraySyncSsidHiddenStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncSsidHiddenStatus.setStatus("mandatory")


class _Dot11APArraySyncAutoChannelStatus_Type(Integer32):
    """Custom type dot11APArraySyncAutoChannelStatus based on Integer32"""
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


_Dot11APArraySyncAutoChannelStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncAutoChannelStatus_Object = MibTableColumn
dot11APArraySyncAutoChannelStatus = _Dot11APArraySyncAutoChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 4),
    _Dot11APArraySyncAutoChannelStatus_Type()
)
dot11APArraySyncAutoChannelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncAutoChannelStatus.setStatus("mandatory")


class _Dot11APArraySyncChannelWidthStatus_Type(Integer32):
    """Custom type dot11APArraySyncChannelWidthStatus based on Integer32"""
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


_Dot11APArraySyncChannelWidthStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncChannelWidthStatus_Object = MibTableColumn
dot11APArraySyncChannelWidthStatus = _Dot11APArraySyncChannelWidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 5),
    _Dot11APArraySyncChannelWidthStatus_Type()
)
dot11APArraySyncChannelWidthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncChannelWidthStatus.setStatus("mandatory")


class _Dot11APArraySyncSecurityStatus_Type(Integer32):
    """Custom type dot11APArraySyncSecurityStatus based on Integer32"""
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


_Dot11APArraySyncSecurityStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncSecurityStatus_Object = MibTableColumn
dot11APArraySyncSecurityStatus = _Dot11APArraySyncSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 6),
    _Dot11APArraySyncSecurityStatus_Type()
)
dot11APArraySyncSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncSecurityStatus.setStatus("mandatory")


class _Dot11APArraySyncFixedRateStatus_Type(Integer32):
    """Custom type dot11APArraySyncFixedRateStatus based on Integer32"""
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


_Dot11APArraySyncFixedRateStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncFixedRateStatus_Object = MibTableColumn
dot11APArraySyncFixedRateStatus = _Dot11APArraySyncFixedRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 7),
    _Dot11APArraySyncFixedRateStatus_Type()
)
dot11APArraySyncFixedRateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncFixedRateStatus.setStatus("mandatory")


class _Dot11APArraySyncBeaconIntervalStatus_Type(Integer32):
    """Custom type dot11APArraySyncBeaconIntervalStatus based on Integer32"""
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


_Dot11APArraySyncBeaconIntervalStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncBeaconIntervalStatus_Object = MibTableColumn
dot11APArraySyncBeaconIntervalStatus = _Dot11APArraySyncBeaconIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 8),
    _Dot11APArraySyncBeaconIntervalStatus_Type()
)
dot11APArraySyncBeaconIntervalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncBeaconIntervalStatus.setStatus("mandatory")


class _Dot11APArraySyncDtimStatus_Type(Integer32):
    """Custom type dot11APArraySyncDtimStatus based on Integer32"""
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


_Dot11APArraySyncDtimStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncDtimStatus_Object = MibTableColumn
dot11APArraySyncDtimStatus = _Dot11APArraySyncDtimStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 9),
    _Dot11APArraySyncDtimStatus_Type()
)
dot11APArraySyncDtimStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncDtimStatus.setStatus("mandatory")


class _Dot11APArraySyncTxPowerStatus_Type(Integer32):
    """Custom type dot11APArraySyncTxPowerStatus based on Integer32"""
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


_Dot11APArraySyncTxPowerStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncTxPowerStatus_Object = MibTableColumn
dot11APArraySyncTxPowerStatus = _Dot11APArraySyncTxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 10),
    _Dot11APArraySyncTxPowerStatus_Type()
)
dot11APArraySyncTxPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncTxPowerStatus.setStatus("mandatory")


class _Dot11APArraySyncWMMStatus_Type(Integer32):
    """Custom type dot11APArraySyncWMMStatus based on Integer32"""
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


_Dot11APArraySyncWMMStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncWMMStatus_Object = MibTableColumn
dot11APArraySyncWMMStatus = _Dot11APArraySyncWMMStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 11),
    _Dot11APArraySyncWMMStatus_Type()
)
dot11APArraySyncWMMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncWMMStatus.setStatus("mandatory")


class _Dot11APArraySyncAckTimeoutStatus_Type(Integer32):
    """Custom type dot11APArraySyncAckTimeoutStatus based on Integer32"""
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


_Dot11APArraySyncAckTimeoutStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncAckTimeoutStatus_Object = MibTableColumn
dot11APArraySyncAckTimeoutStatus = _Dot11APArraySyncAckTimeoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 12),
    _Dot11APArraySyncAckTimeoutStatus_Type()
)
dot11APArraySyncAckTimeoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncAckTimeoutStatus.setStatus("mandatory")


class _Dot11APArraySyncShortGIStatus_Type(Integer32):
    """Custom type dot11APArraySyncShortGIStatus based on Integer32"""
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


_Dot11APArraySyncShortGIStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncShortGIStatus_Object = MibTableColumn
dot11APArraySyncShortGIStatus = _Dot11APArraySyncShortGIStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 13),
    _Dot11APArraySyncShortGIStatus_Type()
)
dot11APArraySyncShortGIStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncShortGIStatus.setStatus("mandatory")


class _Dot11APArraySyncIgmpSnoopStatus_Type(Integer32):
    """Custom type dot11APArraySyncIgmpSnoopStatus based on Integer32"""
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


_Dot11APArraySyncIgmpSnoopStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncIgmpSnoopStatus_Object = MibTableColumn
dot11APArraySyncIgmpSnoopStatus = _Dot11APArraySyncIgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 14),
    _Dot11APArraySyncIgmpSnoopStatus_Type()
)
dot11APArraySyncIgmpSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncIgmpSnoopStatus.setStatus("mandatory")


class _Dot11APArraySyncConnectionLimitStatus_Type(Integer32):
    """Custom type dot11APArraySyncConnectionLimitStatus based on Integer32"""
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


_Dot11APArraySyncConnectionLimitStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncConnectionLimitStatus_Object = MibTableColumn
dot11APArraySyncConnectionLimitStatus = _Dot11APArraySyncConnectionLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 15),
    _Dot11APArraySyncConnectionLimitStatus_Type()
)
dot11APArraySyncConnectionLimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncConnectionLimitStatus.setStatus("mandatory")


class _Dot11APArraySyncLinkIntegrityStatus_Type(Integer32):
    """Custom type dot11APArraySyncLinkIntegrityStatus based on Integer32"""
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


_Dot11APArraySyncLinkIntegrityStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncLinkIntegrityStatus_Object = MibTableColumn
dot11APArraySyncLinkIntegrityStatus = _Dot11APArraySyncLinkIntegrityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 16),
    _Dot11APArraySyncLinkIntegrityStatus_Type()
)
dot11APArraySyncLinkIntegrityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncLinkIntegrityStatus.setStatus("mandatory")


class _Dot11APArraySyncMultiSsidStatus_Type(Integer32):
    """Custom type dot11APArraySyncMultiSsidStatus based on Integer32"""
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


_Dot11APArraySyncMultiSsidStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncMultiSsidStatus_Object = MibTableColumn
dot11APArraySyncMultiSsidStatus = _Dot11APArraySyncMultiSsidStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 17),
    _Dot11APArraySyncMultiSsidStatus_Type()
)
dot11APArraySyncMultiSsidStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncMultiSsidStatus.setStatus("mandatory")


class _Dot11APArraySyncMultiSsidHiddenStatus_Type(Integer32):
    """Custom type dot11APArraySyncMultiSsidHiddenStatus based on Integer32"""
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


_Dot11APArraySyncMultiSsidHiddenStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncMultiSsidHiddenStatus_Object = MibTableColumn
dot11APArraySyncMultiSsidHiddenStatus = _Dot11APArraySyncMultiSsidHiddenStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 18),
    _Dot11APArraySyncMultiSsidHiddenStatus_Type()
)
dot11APArraySyncMultiSsidHiddenStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncMultiSsidHiddenStatus.setStatus("mandatory")


class _Dot11APArraySyncMultiSsidSecurityStatus_Type(Integer32):
    """Custom type dot11APArraySyncMultiSsidSecurityStatus based on Integer32"""
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


_Dot11APArraySyncMultiSsidSecurityStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncMultiSsidSecurityStatus_Object = MibTableColumn
dot11APArraySyncMultiSsidSecurityStatus = _Dot11APArraySyncMultiSsidSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 19),
    _Dot11APArraySyncMultiSsidSecurityStatus_Type()
)
dot11APArraySyncMultiSsidSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncMultiSsidSecurityStatus.setStatus("mandatory")


class _Dot11APArraySyncMultiSsidWMMStatus_Type(Integer32):
    """Custom type dot11APArraySyncMultiSsidWMMStatus based on Integer32"""
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


_Dot11APArraySyncMultiSsidWMMStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncMultiSsidWMMStatus_Object = MibTableColumn
dot11APArraySyncMultiSsidWMMStatus = _Dot11APArraySyncMultiSsidWMMStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 20),
    _Dot11APArraySyncMultiSsidWMMStatus_Type()
)
dot11APArraySyncMultiSsidWMMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncMultiSsidWMMStatus.setStatus("mandatory")


class _Dot11APArraySyncQOSStatus_Type(Integer32):
    """Custom type dot11APArraySyncQOSStatus based on Integer32"""
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


_Dot11APArraySyncQOSStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncQOSStatus_Object = MibTableColumn
dot11APArraySyncQOSStatus = _Dot11APArraySyncQOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 21),
    _Dot11APArraySyncQOSStatus_Type()
)
dot11APArraySyncQOSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncQOSStatus.setStatus("mandatory")


class _Dot11APArraySyncVlanStatus_Type(Integer32):
    """Custom type dot11APArraySyncVlanStatus based on Integer32"""
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


_Dot11APArraySyncVlanStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncVlanStatus_Object = MibTableColumn
dot11APArraySyncVlanStatus = _Dot11APArraySyncVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 22),
    _Dot11APArraySyncVlanStatus_Type()
)
dot11APArraySyncVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncVlanStatus.setStatus("mandatory")


class _Dot11APArraySyncScheduleStatus_Type(Integer32):
    """Custom type dot11APArraySyncScheduleStatus based on Integer32"""
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


_Dot11APArraySyncScheduleStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncScheduleStatus_Object = MibTableColumn
dot11APArraySyncScheduleStatus = _Dot11APArraySyncScheduleStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 23),
    _Dot11APArraySyncScheduleStatus_Type()
)
dot11APArraySyncScheduleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncScheduleStatus.setStatus("mandatory")


class _Dot11APArraySyncTimeStatus_Type(Integer32):
    """Custom type dot11APArraySyncTimeStatus based on Integer32"""
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


_Dot11APArraySyncTimeStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncTimeStatus_Object = MibTableColumn
dot11APArraySyncTimeStatus = _Dot11APArraySyncTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 24),
    _Dot11APArraySyncTimeStatus_Type()
)
dot11APArraySyncTimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncTimeStatus.setStatus("mandatory")


class _Dot11APArraySyncLogStatus_Type(Integer32):
    """Custom type dot11APArraySyncLogStatus based on Integer32"""
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


_Dot11APArraySyncLogStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncLogStatus_Object = MibTableColumn
dot11APArraySyncLogStatus = _Dot11APArraySyncLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 25),
    _Dot11APArraySyncLogStatus_Type()
)
dot11APArraySyncLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncLogStatus.setStatus("mandatory")


class _Dot11APArraySyncAdminLimitStatus_Type(Integer32):
    """Custom type dot11APArraySyncAdminLimitStatus based on Integer32"""
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


_Dot11APArraySyncAdminLimitStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncAdminLimitStatus_Object = MibTableColumn
dot11APArraySyncAdminLimitStatus = _Dot11APArraySyncAdminLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 26),
    _Dot11APArraySyncAdminLimitStatus_Type()
)
dot11APArraySyncAdminLimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncAdminLimitStatus.setStatus("mandatory")


class _Dot11APArraySyncSystemStatus_Type(Integer32):
    """Custom type dot11APArraySyncSystemStatus based on Integer32"""
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


_Dot11APArraySyncSystemStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncSystemStatus_Object = MibTableColumn
dot11APArraySyncSystemStatus = _Dot11APArraySyncSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 27),
    _Dot11APArraySyncSystemStatus_Type()
)
dot11APArraySyncSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncSystemStatus.setStatus("mandatory")


class _Dot11APArraySyncConsoleProtocolStatus_Type(Integer32):
    """Custom type dot11APArraySyncConsoleProtocolStatus based on Integer32"""
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


_Dot11APArraySyncConsoleProtocolStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncConsoleProtocolStatus_Object = MibTableColumn
dot11APArraySyncConsoleProtocolStatus = _Dot11APArraySyncConsoleProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 28),
    _Dot11APArraySyncConsoleProtocolStatus_Type()
)
dot11APArraySyncConsoleProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncConsoleProtocolStatus.setStatus("mandatory")


class _Dot11APArraySyncSnmpStatus_Type(Integer32):
    """Custom type dot11APArraySyncSnmpStatus based on Integer32"""
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


_Dot11APArraySyncSnmpStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncSnmpStatus_Object = MibTableColumn
dot11APArraySyncSnmpStatus = _Dot11APArraySyncSnmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 29),
    _Dot11APArraySyncSnmpStatus_Type()
)
dot11APArraySyncSnmpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncSnmpStatus.setStatus("mandatory")


class _Dot11APArraySyncPingCtlStatus_Type(Integer32):
    """Custom type dot11APArraySyncPingCtlStatus based on Integer32"""
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


_Dot11APArraySyncPingCtlStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncPingCtlStatus_Object = MibTableColumn
dot11APArraySyncPingCtlStatus = _Dot11APArraySyncPingCtlStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 30),
    _Dot11APArraySyncPingCtlStatus_Type()
)
dot11APArraySyncPingCtlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncPingCtlStatus.setStatus("mandatory")


class _Dot11APArraySyncDhcpStatus_Type(Integer32):
    """Custom type dot11APArraySyncDhcpStatus based on Integer32"""
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


_Dot11APArraySyncDhcpStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncDhcpStatus_Object = MibTableColumn
dot11APArraySyncDhcpStatus = _Dot11APArraySyncDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 31),
    _Dot11APArraySyncDhcpStatus_Type()
)
dot11APArraySyncDhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncDhcpStatus.setStatus("mandatory")


class _Dot11APArraySyncLoginStatus_Type(Integer32):
    """Custom type dot11APArraySyncLoginStatus based on Integer32"""
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


_Dot11APArraySyncLoginStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncLoginStatus_Object = MibTableColumn
dot11APArraySyncLoginStatus = _Dot11APArraySyncLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 32),
    _Dot11APArraySyncLoginStatus_Type()
)
dot11APArraySyncLoginStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncLoginStatus.setStatus("mandatory")


class _Dot11APArraySyncAclStatus_Type(Integer32):
    """Custom type dot11APArraySyncAclStatus based on Integer32"""
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


_Dot11APArraySyncAclStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncAclStatus_Object = MibTableColumn
dot11APArraySyncAclStatus = _Dot11APArraySyncAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 33),
    _Dot11APArraySyncAclStatus_Type()
)
dot11APArraySyncAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncAclStatus.setStatus("mandatory")


class _Dot11APArraySyncBandStatus_Type(Integer32):
    """Custom type dot11APArraySyncBandStatus based on Integer32"""
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


_Dot11APArraySyncBandStatus_Type.__name__ = "Integer32"
_Dot11APArraySyncBandStatus_Object = MibTableColumn
dot11APArraySyncBandStatus = _Dot11APArraySyncBandStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 11, 3, 1, 1, 34),
    _Dot11APArraySyncBandStatus_Type()
)
dot11APArraySyncBandStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11APArraySyncBandStatus.setStatus("mandatory")
_Ieee802dot11WebRedirection_ObjectIdentity = ObjectIdentity
ieee802dot11WebRedirection = _Ieee802dot11WebRedirection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14)
)
_Ieee802dot11WebRedirectionSetting_ObjectIdentity = ObjectIdentity
ieee802dot11WebRedirectionSetting = _Ieee802dot11WebRedirectionSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 1)
)


class _Dot11WebRedirectionStatus_Type(Integer32):
    """Custom type dot11WebRedirectionStatus based on Integer32"""
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


_Dot11WebRedirectionStatus_Type.__name__ = "Integer32"
_Dot11WebRedirectionStatus_Object = MibScalar
dot11WebRedirectionStatus = _Dot11WebRedirectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 1, 1),
    _Dot11WebRedirectionStatus_Type()
)
dot11WebRedirectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WebRedirectionStatus.setStatus("mandatory")
_Ieee802dot11WebRedirectionAccountSetting_ObjectIdentity = ObjectIdentity
ieee802dot11WebRedirectionAccountSetting = _Ieee802dot11WebRedirectionAccountSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 2)
)
_Dot11WebRedirectionAccountName_Type = OctetString
_Dot11WebRedirectionAccountName_Object = MibScalar
dot11WebRedirectionAccountName = _Dot11WebRedirectionAccountName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 2, 1),
    _Dot11WebRedirectionAccountName_Type()
)
dot11WebRedirectionAccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WebRedirectionAccountName.setStatus("mandatory")
_Dot11WebRedirectionAccountPasswd_Type = OctetString
_Dot11WebRedirectionAccountPasswd_Object = MibScalar
dot11WebRedirectionAccountPasswd = _Dot11WebRedirectionAccountPasswd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 2, 2),
    _Dot11WebRedirectionAccountPasswd_Type()
)
dot11WebRedirectionAccountPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WebRedirectionAccountPasswd.setStatus("mandatory")


class _Dot11WebRedirectionAccountStatus_Type(Integer32):
    """Custom type dot11WebRedirectionAccountStatus based on Integer32"""
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


_Dot11WebRedirectionAccountStatus_Type.__name__ = "Integer32"
_Dot11WebRedirectionAccountStatus_Object = MibScalar
dot11WebRedirectionAccountStatus = _Dot11WebRedirectionAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 2, 3),
    _Dot11WebRedirectionAccountStatus_Type()
)
dot11WebRedirectionAccountStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WebRedirectionAccountStatus.setStatus("mandatory")


class _Dot11WebRedirectionAccountAction_Type(Integer32):
    """Custom type dot11WebRedirectionAccountAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 0))
    )


_Dot11WebRedirectionAccountAction_Type.__name__ = "Integer32"
_Dot11WebRedirectionAccountAction_Object = MibScalar
dot11WebRedirectionAccountAction = _Dot11WebRedirectionAccountAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 2, 4),
    _Dot11WebRedirectionAccountAction_Type()
)
dot11WebRedirectionAccountAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WebRedirectionAccountAction.setStatus("mandatory")
_Dot11WebRedirectionAccountTable_Object = MibTable
dot11WebRedirectionAccountTable = _Dot11WebRedirectionAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 2, 5)
)
if mibBuilder.loadTexts:
    dot11WebRedirectionAccountTable.setStatus("mandatory")
_Dot11WebRedirectionAccountEntry_Object = MibTableRow
dot11WebRedirectionAccountEntry = _Dot11WebRedirectionAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 2, 5, 1)
)
dot11WebRedirectionAccountEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11WebRedirectionIndex"),
)
if mibBuilder.loadTexts:
    dot11WebRedirectionAccountEntry.setStatus("mandatory")
_Dot11WebRedirectionIndex_Type = Integer32
_Dot11WebRedirectionIndex_Object = MibTableColumn
dot11WebRedirectionIndex = _Dot11WebRedirectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 2, 5, 1, 1),
    _Dot11WebRedirectionIndex_Type()
)
dot11WebRedirectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11WebRedirectionIndex.setStatus("mandatory")
_Dot11WebRedirectionListAccountName_Type = OctetString
_Dot11WebRedirectionListAccountName_Object = MibTableColumn
dot11WebRedirectionListAccountName = _Dot11WebRedirectionListAccountName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 2, 5, 1, 2),
    _Dot11WebRedirectionListAccountName_Type()
)
dot11WebRedirectionListAccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WebRedirectionListAccountName.setStatus("mandatory")
_Dot11WebRedirectionListAccountPasswd_Type = OctetString
_Dot11WebRedirectionListAccountPasswd_Object = MibTableColumn
dot11WebRedirectionListAccountPasswd = _Dot11WebRedirectionListAccountPasswd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 2, 5, 1, 3),
    _Dot11WebRedirectionListAccountPasswd_Type()
)
dot11WebRedirectionListAccountPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WebRedirectionListAccountPasswd.setStatus("mandatory")


class _Dot11WebRedirectionListAccountStatus_Type(Integer32):
    """Custom type dot11WebRedirectionListAccountStatus based on Integer32"""
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


_Dot11WebRedirectionListAccountStatus_Type.__name__ = "Integer32"
_Dot11WebRedirectionListAccountStatus_Object = MibTableColumn
dot11WebRedirectionListAccountStatus = _Dot11WebRedirectionListAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 14, 2, 5, 1, 4),
    _Dot11WebRedirectionListAccountStatus_Type()
)
dot11WebRedirectionListAccountStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WebRedirectionListAccountStatus.setStatus("mandatory")
_Ieee802dot11ARPSpoofingPrevention_ObjectIdentity = ObjectIdentity
ieee802dot11ARPSpoofingPrevention = _Ieee802dot11ARPSpoofingPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15)
)
_Ieee802dot11ARPSpoofingPreventionSetting_ObjectIdentity = ObjectIdentity
ieee802dot11ARPSpoofingPreventionSetting = _Ieee802dot11ARPSpoofingPreventionSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15, 1)
)


class _Dot11ARPSpoofingPreventionStatus_Type(Integer32):
    """Custom type dot11ARPSpoofingPreventionStatus based on Integer32"""
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


_Dot11ARPSpoofingPreventionStatus_Type.__name__ = "Integer32"
_Dot11ARPSpoofingPreventionStatus_Object = MibScalar
dot11ARPSpoofingPreventionStatus = _Dot11ARPSpoofingPreventionStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15, 1, 1),
    _Dot11ARPSpoofingPreventionStatus_Type()
)
dot11ARPSpoofingPreventionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ARPSpoofingPreventionStatus.setStatus("mandatory")
_Ieee802dot11ARPSpoofingPreventionAddressSetting_ObjectIdentity = ObjectIdentity
ieee802dot11ARPSpoofingPreventionAddressSetting = _Ieee802dot11ARPSpoofingPreventionAddressSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15, 2)
)
_Dot11ARPSpoofingPreventionIpAddress_Type = IpAddress
_Dot11ARPSpoofingPreventionIpAddress_Object = MibScalar
dot11ARPSpoofingPreventionIpAddress = _Dot11ARPSpoofingPreventionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15, 2, 1),
    _Dot11ARPSpoofingPreventionIpAddress_Type()
)
dot11ARPSpoofingPreventionIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ARPSpoofingPreventionIpAddress.setStatus("mandatory")
_Dot11ARPSpoofingPreventionMacAddress_Type = MacAddress
_Dot11ARPSpoofingPreventionMacAddress_Object = MibScalar
dot11ARPSpoofingPreventionMacAddress = _Dot11ARPSpoofingPreventionMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15, 2, 2),
    _Dot11ARPSpoofingPreventionMacAddress_Type()
)
dot11ARPSpoofingPreventionMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ARPSpoofingPreventionMacAddress.setStatus("mandatory")


class _Dot11ARPSpoofingPreventionAction_Type(Integer32):
    """Custom type dot11ARPSpoofingPreventionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 0))
    )


_Dot11ARPSpoofingPreventionAction_Type.__name__ = "Integer32"
_Dot11ARPSpoofingPreventionAction_Object = MibScalar
dot11ARPSpoofingPreventionAction = _Dot11ARPSpoofingPreventionAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15, 2, 3),
    _Dot11ARPSpoofingPreventionAction_Type()
)
dot11ARPSpoofingPreventionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ARPSpoofingPreventionAction.setStatus("mandatory")
_Dot11ARPSpoofingPreventionTable_Object = MibTable
dot11ARPSpoofingPreventionTable = _Dot11ARPSpoofingPreventionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15, 2, 4)
)
if mibBuilder.loadTexts:
    dot11ARPSpoofingPreventionTable.setStatus("mandatory")
_Dot11ARPSpoofingPreventionEntry_Object = MibTableRow
dot11ARPSpoofingPreventionEntry = _Dot11ARPSpoofingPreventionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15, 2, 4, 1)
)
dot11ARPSpoofingPreventionEntry.setIndexNames(
    (0, "DAP-3520-v115", "dot11ARPSpoofingPreventionIndex"),
)
if mibBuilder.loadTexts:
    dot11ARPSpoofingPreventionEntry.setStatus("mandatory")
_Dot11ARPSpoofingPreventionIndex_Type = Integer32
_Dot11ARPSpoofingPreventionIndex_Object = MibTableColumn
dot11ARPSpoofingPreventionIndex = _Dot11ARPSpoofingPreventionIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15, 2, 4, 1, 1),
    _Dot11ARPSpoofingPreventionIndex_Type()
)
dot11ARPSpoofingPreventionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11ARPSpoofingPreventionIndex.setStatus("mandatory")
_Dot11ARPSpoofingPreventionListIpAddress_Type = IpAddress
_Dot11ARPSpoofingPreventionListIpAddress_Object = MibTableColumn
dot11ARPSpoofingPreventionListIpAddress = _Dot11ARPSpoofingPreventionListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15, 2, 4, 1, 2),
    _Dot11ARPSpoofingPreventionListIpAddress_Type()
)
dot11ARPSpoofingPreventionListIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ARPSpoofingPreventionListIpAddress.setStatus("mandatory")
_Dot11ARPSpoofingPreventionListMacAddress_Type = MacAddress
_Dot11ARPSpoofingPreventionListMacAddress_Object = MibTableColumn
dot11ARPSpoofingPreventionListMacAddress = _Dot11ARPSpoofingPreventionListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 3, 15, 2, 4, 1, 3),
    _Dot11ARPSpoofingPreventionListMacAddress_Type()
)
dot11ARPSpoofingPreventionListMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ARPSpoofingPreventionListMacAddress.setStatus("mandatory")
_Administration_ObjectIdentity = ObjectIdentity
administration = _Administration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4)
)
_Users_ObjectIdentity = ObjectIdentity
users = _Users_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 1)
)
_UsersTable_Object = MibTable
usersTable = _UsersTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usersTable.setStatus("mandatory")
_UsersEntry_Object = MibTableRow
usersEntry = _UsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 1, 1, 1)
)
usersEntry.setIndexNames(
    (0, "DAP-3520-v115", "usersIndex"),
)
if mibBuilder.loadTexts:
    usersEntry.setStatus("mandatory")
_UsersIndex_Type = Integer32
_UsersIndex_Object = MibTableColumn
usersIndex = _UsersIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 1, 1, 1, 3),
    _UsersPassword_Type()
)
usersPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usersPassword.setStatus("mandatory")
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 2, 2),
    _DeviceFactoryDefault_Type()
)
deviceFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceFactoryDefault.setStatus("mandatory")


class _DeviceSettingApply_Type(Integer32):
    """Custom type deviceSettingApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("nothing", 0))
    )


_DeviceSettingApply_Type.__name__ = "Integer32"
_DeviceSettingApply_Object = MibScalar
deviceSettingApply = _DeviceSettingApply_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 2, 3),
    _DeviceSettingApply_Type()
)
deviceSettingApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceSettingApply.setStatus("mandatory")


class _DeviceSettingDiscard_Type(Integer32):
    """Custom type deviceSettingDiscard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("nothing", 0))
    )


_DeviceSettingDiscard_Type.__name__ = "Integer32"
_DeviceSettingDiscard_Object = MibScalar
deviceSettingDiscard = _DeviceSettingDiscard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 2, 4),
    _DeviceSettingDiscard_Type()
)
deviceSettingDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceSettingDiscard.setStatus("mandatory")


class _LanguagePackClear_Type(Integer32):
    """Custom type languagePackClear based on Integer32"""
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


_LanguagePackClear_Type.__name__ = "Integer32"
_LanguagePackClear_Object = MibScalar
languagePackClear = _LanguagePackClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 2, 5),
    _LanguagePackClear_Type()
)
languagePackClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    languagePackClear.setStatus("mandatory")
_Update_ObjectIdentity = ObjectIdentity
update = _Update_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3)
)
_UpdateFirmwareVersion_Type = OctetString
_UpdateFirmwareVersion_Object = MibScalar
updateFirmwareVersion = _UpdateFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 1),
    _UpdateFirmwareVersion_Type()
)
updateFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updateFirmwareVersion.setStatus("mandatory")
_Tftp_ObjectIdentity = ObjectIdentity
tftp = _Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 2)
)
_TftpServerIPAddress_Type = IpAddress
_TftpServerIPAddress_Object = MibScalar
tftpServerIPAddress = _TftpServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 2, 1),
    _TftpServerIPAddress_Type()
)
tftpServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerIPAddress.setStatus("mandatory")
_TftpRemoteFileName_Type = OctetString
_TftpRemoteFileName_Object = MibScalar
tftpRemoteFileName = _TftpRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 2, 2),
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
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("get", 2),
          ("nothing", 4),
          ("put", 3),
          ("putacl", 5))
    )


_TftpCommand_Type.__name__ = "Integer32"
_TftpCommand_Object = MibScalar
tftpCommand = _TftpCommand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 2, 4),
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
        *(("certificateFileUpdate", 7),
          ("configSave", 3),
          ("configSetting", 2),
          ("factoryReset", 5),
          ("firmwareUpdate", 1),
          ("getacl", 9),
          ("keyFileUpdate", 8),
          ("nothing", 6),
          ("reboot", 4))
    )


_TftpUpgradeSettingCommand_Type.__name__ = "Integer32"
_TftpUpgradeSettingCommand_Object = MibScalar
tftpUpgradeSettingCommand = _TftpUpgradeSettingCommand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 2, 5),
    _TftpUpgradeSettingCommand_Type()
)
tftpUpgradeSettingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpUpgradeSettingCommand.setStatus("mandatory")
_Ftp_ObjectIdentity = ObjectIdentity
ftp = _Ftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 3)
)
_FtpServerIPAddress_Type = IpAddress
_FtpServerIPAddress_Object = MibScalar
ftpServerIPAddress = _FtpServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 3, 1),
    _FtpServerIPAddress_Type()
)
ftpServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpServerIPAddress.setStatus("mandatory")
_FtpUserName_Type = OctetString
_FtpUserName_Object = MibScalar
ftpUserName = _FtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 3, 3),
    _FtpUserName_Type()
)
ftpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUserName.setStatus("mandatory")
_FtpPassword_Type = OctetString
_FtpPassword_Object = MibScalar
ftpPassword = _FtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 3, 4),
    _FtpPassword_Type()
)
ftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPassword.setStatus("mandatory")
_FtpRemoteFileName_Type = OctetString
_FtpRemoteFileName_Object = MibScalar
ftpRemoteFileName = _FtpRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 3, 5),
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
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("get", 2),
          ("nothing", 4),
          ("put", 3),
          ("putacl", 5))
    )


_FtpCommand_Type.__name__ = "Integer32"
_FtpCommand_Object = MibScalar
ftpCommand = _FtpCommand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 3, 7),
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("certificateFileUpdate", 7),
          ("configSave", 3),
          ("configSetting", 2),
          ("factoryReset", 5),
          ("firmwareUpdate", 1),
          ("getacl", 9),
          ("keyFileUpdate", 8),
          ("nothing", 6),
          ("reboot", 4))
    )


_FtpUpgradeSettingCommand_Type.__name__ = "Integer32"
_FtpUpgradeSettingCommand_Object = MibScalar
ftpUpgradeSettingCommand = _FtpUpgradeSettingCommand_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 3, 8),
    _FtpUpgradeSettingCommand_Type()
)
ftpUpgradeSettingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUpgradeSettingCommand.setStatus("mandatory")


class _UpdateStatus_Type(Integer32):
    """Custom type updateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("configSuccess", 5),
          ("correct", 0),
          ("failed", 8),
          ("fwSuccess", 1),
          ("inProcess", 7),
          ("none", 9),
          ("wrongAclFile", 4),
          ("wrongConfigFile", 3),
          ("wrongImageFile", 2))
    )


_UpdateStatus_Type.__name__ = "Integer32"
_UpdateStatus_Object = MibScalar
updateStatus = _UpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 3, 6),
    _UpdateStatus_Type()
)
updateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updateStatus.setStatus("mandatory")
_Console_ObjectIdentity = ObjectIdentity
console = _Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 4, 3),
    _Timeout_Type()
)
timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeout.setStatus("mandatory")
_Web_ObjectIdentity = ObjectIdentity
web = _Web_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 5)
)


class _WebStatus_Type(Integer32):
    """Custom type webStatus based on Integer32"""
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


_WebStatus_Type.__name__ = "Integer32"
_WebStatus_Object = MibScalar
webStatus = _WebStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 5, 1),
    _WebStatus_Type()
)
webStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webStatus.setStatus("mandatory")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 6)
)
_Ssl_ObjectIdentity = ObjectIdentity
ssl = _Ssl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 7)
)
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8)
)
_SntpServerIpAddress_Type = OctetString
_SntpServerIpAddress_Object = MibScalar
sntpServerIpAddress = _SntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 3),
    _SntpDayLightSaving_Type()
)
sntpDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDayLightSaving.setStatus("mandatory")
_SntpTimeofDay_Type = OctetString
_SntpTimeofDay_Object = MibScalar
sntpTimeofDay = _SntpTimeofDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 4),
    _SntpTimeofDay_Type()
)
sntpTimeofDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpTimeofDay.setStatus("mandatory")


class _SntpStatus_Type(Integer32):
    """Custom type sntpStatus based on Integer32"""
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


_SntpStatus_Type.__name__ = "Integer32"
_SntpStatus_Object = MibScalar
sntpStatus = _SntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 5),
    _SntpStatus_Type()
)
sntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpStatus.setStatus("mandatory")


class _SntpInterval_Type(Integer32):
    """Custom type sntpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one-day", 1),
          ("seven-days", 3),
          ("three-days", 2))
    )


_SntpInterval_Type.__name__ = "Integer32"
_SntpInterval_Object = MibScalar
sntpInterval = _SntpInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 6),
    _SntpInterval_Type()
)
sntpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpInterval.setStatus("mandatory")
_SetTimeManually_Type = OctetString
_SetTimeManually_Object = MibScalar
setTimeManually = _SetTimeManually_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 7),
    _SetTimeManually_Type()
)
setTimeManually.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTimeManually.setStatus("mandatory")


class _SntpDstStartMonth_Type(Integer32):
    """Custom type sntpDstStartMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SntpDstStartMonth_Type.__name__ = "Integer32"
_SntpDstStartMonth_Object = MibScalar
sntpDstStartMonth = _SntpDstStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 8),
    _SntpDstStartMonth_Type()
)
sntpDstStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDstStartMonth.setStatus("mandatory")


class _SntpDstStartWeek_Type(Integer32):
    """Custom type sntpDstStartWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SntpDstStartWeek_Type.__name__ = "Integer32"
_SntpDstStartWeek_Object = MibScalar
sntpDstStartWeek = _SntpDstStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 9),
    _SntpDstStartWeek_Type()
)
sntpDstStartWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDstStartWeek.setStatus("mandatory")


class _SntpDstStartDayOfWeek_Type(Integer32):
    """Custom type sntpDstStartDayOfWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fri", 5),
          ("mon", 1),
          ("sat", 6),
          ("sun", 0),
          ("thu", 4),
          ("tue", 2),
          ("wed", 3))
    )


_SntpDstStartDayOfWeek_Type.__name__ = "Integer32"
_SntpDstStartDayOfWeek_Object = MibScalar
sntpDstStartDayOfWeek = _SntpDstStartDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 10),
    _SntpDstStartDayOfWeek_Type()
)
sntpDstStartDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDstStartDayOfWeek.setStatus("mandatory")


class _SntpDstStartCurrentTime_Type(Integer32):
    """Custom type sntpDstStartCurrentTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SntpDstStartCurrentTime_Type.__name__ = "Integer32"
_SntpDstStartCurrentTime_Object = MibScalar
sntpDstStartCurrentTime = _SntpDstStartCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 11),
    _SntpDstStartCurrentTime_Type()
)
sntpDstStartCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDstStartCurrentTime.setStatus("mandatory")


class _SntpDstEndMonth_Type(Integer32):
    """Custom type sntpDstEndMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SntpDstEndMonth_Type.__name__ = "Integer32"
_SntpDstEndMonth_Object = MibScalar
sntpDstEndMonth = _SntpDstEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 12),
    _SntpDstEndMonth_Type()
)
sntpDstEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDstEndMonth.setStatus("mandatory")


class _SntpDstEndWeek_Type(Integer32):
    """Custom type sntpDstEndWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SntpDstEndWeek_Type.__name__ = "Integer32"
_SntpDstEndWeek_Object = MibScalar
sntpDstEndWeek = _SntpDstEndWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 13),
    _SntpDstEndWeek_Type()
)
sntpDstEndWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDstEndWeek.setStatus("mandatory")


class _SntpDstEndDayOfWeek_Type(Integer32):
    """Custom type sntpDstEndDayOfWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fri", 5),
          ("mon", 1),
          ("sat", 6),
          ("sun", 0),
          ("thu", 4),
          ("tue", 2),
          ("wed", 3))
    )


_SntpDstEndDayOfWeek_Type.__name__ = "Integer32"
_SntpDstEndDayOfWeek_Object = MibScalar
sntpDstEndDayOfWeek = _SntpDstEndDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 14),
    _SntpDstEndDayOfWeek_Type()
)
sntpDstEndDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDstEndDayOfWeek.setStatus("mandatory")


class _SntpDstEndCurrentTime_Type(Integer32):
    """Custom type sntpDstEndCurrentTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SntpDstEndCurrentTime_Type.__name__ = "Integer32"
_SntpDstEndCurrentTime_Object = MibScalar
sntpDstEndCurrentTime = _SntpDstEndCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 15),
    _SntpDstEndCurrentTime_Type()
)
sntpDstEndCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDstEndCurrentTime.setStatus("mandatory")


class _SntpDayLightSavingOffset_Type(Integer32):
    """Custom type sntpDayLightSavingOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SntpDayLightSavingOffset_Type.__name__ = "Integer32"
_SntpDayLightSavingOffset_Object = MibScalar
sntpDayLightSavingOffset = _SntpDayLightSavingOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 8, 16),
    _SntpDayLightSavingOffset_Type()
)
sntpDayLightSavingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpDayLightSavingOffset.setStatus("mandatory")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 9, 1),
    _SmtpStatus_Type()
)
smtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpStatus.setStatus("mandatory")
_SmtpServerIpAddress_Type = IpAddress
_SmtpServerIpAddress_Object = MibScalar
smtpServerIpAddress = _SmtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 9, 2),
    _SmtpServerIpAddress_Type()
)
smtpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerIpAddress.setStatus("mandatory")
_SmtpAccountingName_Type = OctetString
_SmtpAccountingName_Object = MibScalar
smtpAccountingName = _SmtpAccountingName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 9, 5),
    _SmtpAccountingName_Type()
)
smtpAccountingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpAccountingName.setStatus("mandatory")
_SmtpPassword_Type = OctetString
_SmtpPassword_Object = MibScalar
smtpPassword = _SmtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 9, 6),
    _SmtpPassword_Type()
)
smtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpPassword.setStatus("mandatory")
_LimitedAdministrator_ObjectIdentity = ObjectIdentity
limitedAdministrator = _LimitedAdministrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 10)
)
_ManagerAddress_ObjectIdentity = ObjectIdentity
managerAddress = _ManagerAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 10, 1)
)


class _ManagerIpAddressStatus_Type(Integer32):
    """Custom type managerIpAddressStatus based on Integer32"""
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
        *(("both", 3),
          ("disable", 0),
          ("ipaddress", 2),
          ("vlanID", 1))
    )


_ManagerIpAddressStatus_Type.__name__ = "Integer32"
_ManagerIpAddressStatus_Object = MibScalar
managerIpAddressStatus = _ManagerIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 10, 1, 1),
    _ManagerIpAddressStatus_Type()
)
managerIpAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIpAddressStatus.setStatus("mandatory")


class _ManagerIpAddressDelete_Type(Integer32):
    """Custom type managerIpAddressDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ManagerIpAddressDelete_Type.__name__ = "Integer32"
_ManagerIpAddressDelete_Object = MibScalar
managerIpAddressDelete = _ManagerIpAddressDelete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 10, 1, 3),
    _ManagerIpAddressDelete_Type()
)
managerIpAddressDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIpAddressDelete.setStatus("mandatory")
_ManagerIpAddressTable_Object = MibTable
managerIpAddressTable = _ManagerIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 10, 1, 4)
)
if mibBuilder.loadTexts:
    managerIpAddressTable.setStatus("mandatory")
_ManagerIpAddressEntry_Object = MibTableRow
managerIpAddressEntry = _ManagerIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 10, 1, 4, 1)
)
managerIpAddressEntry.setIndexNames(
    (0, "DAP-3520-v115", "managerIpAddressIndex"),
)
if mibBuilder.loadTexts:
    managerIpAddressEntry.setStatus("mandatory")
_ManagerIpAddressIndex_Type = Integer32
_ManagerIpAddressIndex_Object = MibTableColumn
managerIpAddressIndex = _ManagerIpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 10, 1, 4, 1, 1),
    _ManagerIpAddressIndex_Type()
)
managerIpAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    managerIpAddressIndex.setStatus("mandatory")
_ManagerIpAddressPoolStart_Type = IpAddress
_ManagerIpAddressPoolStart_Object = MibTableColumn
managerIpAddressPoolStart = _ManagerIpAddressPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 10, 1, 4, 1, 3),
    _ManagerIpAddressPoolStart_Type()
)
managerIpAddressPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIpAddressPoolStart.setStatus("mandatory")
_ManagerIpAddressPoolEnd_Type = IpAddress
_ManagerIpAddressPoolEnd_Object = MibTableColumn
managerIpAddressPoolEnd = _ManagerIpAddressPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 10, 1, 4, 1, 4),
    _ManagerIpAddressPoolEnd_Type()
)
managerIpAddressPoolEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIpAddressPoolEnd.setStatus("mandatory")
_ManergeVLANTag_Type = Integer32
_ManergeVLANTag_Object = MibScalar
manergeVLANTag = _ManergeVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 10, 3),
    _ManergeVLANTag_Type()
)
manergeVLANTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manergeVLANTag.setStatus("mandatory")
_PingControl_ObjectIdentity = ObjectIdentity
pingControl = _PingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 12)
)


class _PingControlStatus_Type(Integer32):
    """Custom type pingControlStatus based on Integer32"""
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


_PingControlStatus_Type.__name__ = "Integer32"
_PingControlStatus_Object = MibScalar
pingControlStatus = _PingControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 4, 12, 1),
    _PingControlStatus_Type()
)
pingControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingControlStatus.setStatus("mandatory")
_Report_ObjectIdentity = ObjectIdentity
report = _Report_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5)
)
_DeviceInformation_ObjectIdentity = ObjectIdentity
deviceInformation = _DeviceInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1)
)
_DeviceInformationFirmwareVersion_Type = OctetString
_DeviceInformationFirmwareVersion_Object = MibScalar
deviceInformationFirmwareVersion = _DeviceInformationFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 1),
    _DeviceInformationFirmwareVersion_Type()
)
deviceInformationFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInformationFirmwareVersion.setStatus("mandatory")
_InterfaceInformation_ObjectIdentity = ObjectIdentity
interfaceInformation = _InterfaceInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2)
)
_InterfaceInformationTable_Object = MibTable
interfaceInformationTable = _InterfaceInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    interfaceInformationTable.setStatus("mandatory")
_InterfaceInformationEntry_Object = MibTableRow
interfaceInformationEntry = _InterfaceInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 1),
    _IfGetIpAddressFrom_Type()
)
ifGetIpAddressFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifGetIpAddressFrom.setStatus("mandatory")
_IfIpAddress_Type = IpAddress
_IfIpAddress_Object = MibTableColumn
ifIpAddress = _IfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 2),
    _IfIpAddress_Type()
)
ifIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIpAddress.setStatus("mandatory")
_IfSubnetMask_Type = IpAddress
_IfSubnetMask_Object = MibTableColumn
ifSubnetMask = _IfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 3),
    _IfSubnetMask_Type()
)
ifSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSubnetMask.setStatus("mandatory")
_IfDefaultGateway_Type = IpAddress
_IfDefaultGateway_Object = MibTableColumn
ifDefaultGateway = _IfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 4),
    _IfDefaultGateway_Type()
)
ifDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDefaultGateway.setStatus("mandatory")
_IfMacAddress_Type = MacAddress
_IfMacAddress_Object = MibTableColumn
ifMacAddress = _IfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 5),
    _IfMacAddress_Type()
)
ifMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMacAddress.setStatus("mandatory")


class _WirelessLed2dot4G_Type(Integer32):
    """Custom type wirelessLed2dot4G based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blinking", 1),
          ("disable", 0))
    )


_WirelessLed2dot4G_Type.__name__ = "Integer32"
_WirelessLed2dot4G_Object = MibTableColumn
wirelessLed2dot4G = _WirelessLed2dot4G_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 6),
    _WirelessLed2dot4G_Type()
)
wirelessLed2dot4G.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLed2dot4G.setStatus("mandatory")


class _WirelessLed5G_Type(Integer32):
    """Custom type wirelessLed5G based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blinking", 1),
          ("disable", 0))
    )


_WirelessLed5G_Type.__name__ = "Integer32"
_WirelessLed5G_Object = MibTableColumn
wirelessLed5G = _WirelessLed5G_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 7),
    _WirelessLed5G_Type()
)
wirelessLed5G.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLed5G.setStatus("mandatory")
_DataBaseChannel_Type = Integer32
_DataBaseChannel_Object = MibTableColumn
dataBaseChannel = _DataBaseChannel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 8),
    _DataBaseChannel_Type()
)
dataBaseChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataBaseChannel.setStatus("mandatory")
_Mssid1MacAddress_Type = MacAddress
_Mssid1MacAddress_Object = MibTableColumn
mssid1MacAddress = _Mssid1MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 11),
    _Mssid1MacAddress_Type()
)
mssid1MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssid1MacAddress.setStatus("mandatory")
_Mssid2MacAddress_Type = MacAddress
_Mssid2MacAddress_Object = MibTableColumn
mssid2MacAddress = _Mssid2MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 12),
    _Mssid2MacAddress_Type()
)
mssid2MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssid2MacAddress.setStatus("mandatory")
_Mssid3MacAddress_Type = MacAddress
_Mssid3MacAddress_Object = MibTableColumn
mssid3MacAddress = _Mssid3MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 13),
    _Mssid3MacAddress_Type()
)
mssid3MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssid3MacAddress.setStatus("mandatory")


class _LanLED_Type(Integer32):
    """Custom type lanLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blinking", 1),
          ("disable", 0))
    )


_LanLED_Type.__name__ = "Integer32"
_LanLED_Object = MibTableColumn
lanLED = _LanLED_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 1, 2, 1, 1, 14),
    _LanLED_Type()
)
lanLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanLED.setStatus("mandatory")
_TrafficStatistics_ObjectIdentity = ObjectIdentity
trafficStatistics = _TrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2)
)
_TrafficStatisticsWired_ObjectIdentity = ObjectIdentity
trafficStatisticsWired = _TrafficStatisticsWired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 1)
)
_Dot3TrafficStatistics_ObjectIdentity = ObjectIdentity
dot3TrafficStatistics = _Dot3TrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 1, 1)
)
_Dot3TrafficStatisticsTable_Object = MibTable
dot3TrafficStatisticsTable = _Dot3TrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot3TrafficStatisticsTable.setStatus("mandatory")
_Dot3TrafficStatisticsEntry_Object = MibTableRow
dot3TrafficStatisticsEntry = _Dot3TrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 1, 1, 1, 1)
)
dot3TrafficStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3TrafficStatisticsEntry.setStatus("mandatory")
_Dot3TransmittedPacketCount_Type = Integer32
_Dot3TransmittedPacketCount_Object = MibTableColumn
dot3TransmittedPacketCount = _Dot3TransmittedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 1, 1, 1, 1, 1),
    _Dot3TransmittedPacketCount_Type()
)
dot3TransmittedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3TransmittedPacketCount.setStatus("mandatory")
_Dot3TransmittedBytesCount_Type = Integer32
_Dot3TransmittedBytesCount_Object = MibTableColumn
dot3TransmittedBytesCount = _Dot3TransmittedBytesCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 1, 1, 1, 1, 2),
    _Dot3TransmittedBytesCount_Type()
)
dot3TransmittedBytesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3TransmittedBytesCount.setStatus("mandatory")
_Dot3TransmittedDroppedPacketCount_Type = Integer32
_Dot3TransmittedDroppedPacketCount_Object = MibTableColumn
dot3TransmittedDroppedPacketCount = _Dot3TransmittedDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 1, 1, 1, 1, 3),
    _Dot3TransmittedDroppedPacketCount_Type()
)
dot3TransmittedDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3TransmittedDroppedPacketCount.setStatus("mandatory")
_Dot3ReceivedPacketCount_Type = Integer32
_Dot3ReceivedPacketCount_Object = MibTableColumn
dot3ReceivedPacketCount = _Dot3ReceivedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 1, 1, 1, 1, 4),
    _Dot3ReceivedPacketCount_Type()
)
dot3ReceivedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ReceivedPacketCount.setStatus("mandatory")
_Dot3ReceivedBytesCount_Type = Integer32
_Dot3ReceivedBytesCount_Object = MibTableColumn
dot3ReceivedBytesCount = _Dot3ReceivedBytesCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 1, 1, 1, 1, 5),
    _Dot3ReceivedBytesCount_Type()
)
dot3ReceivedBytesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ReceivedBytesCount.setStatus("mandatory")
_Dot3ReceivedDroppedPacketCount_Type = Integer32
_Dot3ReceivedDroppedPacketCount_Object = MibTableColumn
dot3ReceivedDroppedPacketCount = _Dot3ReceivedDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 1, 1, 1, 1, 6),
    _Dot3ReceivedDroppedPacketCount_Type()
)
dot3ReceivedDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3ReceivedDroppedPacketCount.setStatus("mandatory")


class _Dot3Clear_Type(Integer32):
    """Custom type dot3Clear based on Integer32"""
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


_Dot3Clear_Type.__name__ = "Integer32"
_Dot3Clear_Object = MibTableColumn
dot3Clear = _Dot3Clear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 1, 1, 1, 1, 16),
    _Dot3Clear_Type()
)
dot3Clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3Clear.setStatus("mandatory")
_TrafficStatisticsWireless_ObjectIdentity = ObjectIdentity
trafficStatisticsWireless = _TrafficStatisticsWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2)
)
_Dot11TrafficStatistics_ObjectIdentity = ObjectIdentity
dot11TrafficStatistics = _Dot11TrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1)
)
_Dot11TrafficStatisticsTable_Object = MibTable
dot11TrafficStatisticsTable = _Dot11TrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dot11TrafficStatisticsTable.setStatus("mandatory")
_Dot11TrafficStatisticsEntry_Object = MibTableRow
dot11TrafficStatisticsEntry = _Dot11TrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 2),
    _Dot11TransmitRetryRate_Type()
)
dot11TransmitRetryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmitRetryRate.setStatus("mandatory")
_Dot11TransmittedPacketCount_Type = Integer32
_Dot11TransmittedPacketCount_Object = MibTableColumn
dot11TransmittedPacketCount = _Dot11TransmittedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 19),
    _Dot11TransmittedPacketCount_Type()
)
dot11TransmittedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedPacketCount.setStatus("mandatory")
_Dot11TransmittedBytesCount_Type = Integer32
_Dot11TransmittedBytesCount_Object = MibTableColumn
dot11TransmittedBytesCount = _Dot11TransmittedBytesCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 20),
    _Dot11TransmittedBytesCount_Type()
)
dot11TransmittedBytesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedBytesCount.setStatus("mandatory")
_Dot11TransmittedDroppedPacketCount_Type = Integer32
_Dot11TransmittedDroppedPacketCount_Object = MibTableColumn
dot11TransmittedDroppedPacketCount = _Dot11TransmittedDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 21),
    _Dot11TransmittedDroppedPacketCount_Type()
)
dot11TransmittedDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedDroppedPacketCount.setStatus("mandatory")
_Dot11TransmittedRetryCount_Type = Integer32
_Dot11TransmittedRetryCount_Object = MibTableColumn
dot11TransmittedRetryCount = _Dot11TransmittedRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 22),
    _Dot11TransmittedRetryCount_Type()
)
dot11TransmittedRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TransmittedRetryCount.setStatus("mandatory")
_Dot11ReceivedPacketCount_Type = Integer32
_Dot11ReceivedPacketCount_Object = MibTableColumn
dot11ReceivedPacketCount = _Dot11ReceivedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 23),
    _Dot11ReceivedPacketCount_Type()
)
dot11ReceivedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedPacketCount.setStatus("mandatory")
_Dot11ReceivedBytesCount_Type = Integer32
_Dot11ReceivedBytesCount_Object = MibTableColumn
dot11ReceivedBytesCount = _Dot11ReceivedBytesCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 24),
    _Dot11ReceivedBytesCount_Type()
)
dot11ReceivedBytesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedBytesCount.setStatus("mandatory")
_Dot11ReceivedDroppedPacketCount_Type = Integer32
_Dot11ReceivedDroppedPacketCount_Object = MibTableColumn
dot11ReceivedDroppedPacketCount = _Dot11ReceivedDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 25),
    _Dot11ReceivedDroppedPacketCount_Type()
)
dot11ReceivedDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedDroppedPacketCount.setStatus("mandatory")
_Dot11ReceivedCRCCount_Type = Integer32
_Dot11ReceivedCRCCount_Object = MibTableColumn
dot11ReceivedCRCCount = _Dot11ReceivedCRCCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 26),
    _Dot11ReceivedCRCCount_Type()
)
dot11ReceivedCRCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedCRCCount.setStatus("mandatory")
_Dot11ReceivedDecryptionErrorCount_Type = Integer32
_Dot11ReceivedDecryptionErrorCount_Object = MibTableColumn
dot11ReceivedDecryptionErrorCount = _Dot11ReceivedDecryptionErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 27),
    _Dot11ReceivedDecryptionErrorCount_Type()
)
dot11ReceivedDecryptionErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedDecryptionErrorCount.setStatus("mandatory")
_Dot11ReceivedMICErrorCount_Type = Integer32
_Dot11ReceivedMICErrorCount_Object = MibTableColumn
dot11ReceivedMICErrorCount = _Dot11ReceivedMICErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 28),
    _Dot11ReceivedMICErrorCount_Type()
)
dot11ReceivedMICErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedMICErrorCount.setStatus("mandatory")
_Dot11ReceivedPHYErrorCount_Type = Integer32
_Dot11ReceivedPHYErrorCount_Object = MibTableColumn
dot11ReceivedPHYErrorCount = _Dot11ReceivedPHYErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 29),
    _Dot11ReceivedPHYErrorCount_Type()
)
dot11ReceivedPHYErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11ReceivedPHYErrorCount.setStatus("mandatory")


class _Dot11Clear_Type(Integer32):
    """Custom type dot11Clear based on Integer32"""
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


_Dot11Clear_Type.__name__ = "Integer32"
_Dot11Clear_Object = MibTableColumn
dot11Clear = _Dot11Clear_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 2, 2, 1, 1, 1, 30),
    _Dot11Clear_Type()
)
dot11Clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Clear.setStatus("mandatory")
_SystemLog_ObjectIdentity = ObjectIdentity
systemLog = _SystemLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 3),
    _SystemLogNoticeLevel_Type()
)
systemLogNoticeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogNoticeLevel.setStatus("mandatory")
_SystemLogTFTPServerIPAddress_Type = IpAddress
_SystemLogTFTPServerIPAddress_Object = MibScalar
systemLogTFTPServerIPAddress = _SystemLogTFTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 4),
    _SystemLogTFTPServerIPAddress_Type()
)
systemLogTFTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogTFTPServerIPAddress.setStatus("mandatory")
_SystemLogFileName_Type = OctetString
_SystemLogFileName_Object = MibScalar
systemLogFileName = _SystemLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 6),
    _SystemLogGetLog_Type()
)
systemLogGetLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogGetLog.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 8),
    _SystemLogRemoteLogState_Type()
)
systemLogRemoteLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogRemoteLogState.setStatus("mandatory")
_SystemLogServerIPAddress_Type = IpAddress
_SystemLogServerIPAddress_Object = MibScalar
systemLogServerIPAddress = _SystemLogServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 10),
    _SystemLogClearLocalLog_Type()
)
systemLogClearLocalLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogClearLocalLog.setStatus("mandatory")
_EmailNotification_ObjectIdentity = ObjectIdentity
emailNotification = _EmailNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11)
)
_EmailNotificationTable_Object = MibTable
emailNotificationTable = _EmailNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1)
)
if mibBuilder.loadTexts:
    emailNotificationTable.setStatus("mandatory")
_EmailNotificationEntry_Object = MibTableRow
emailNotificationEntry = _EmailNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1)
)
emailNotificationEntry.setIndexNames(
    (0, "DAP-3520-v115", "emailNtfIndex"),
)
if mibBuilder.loadTexts:
    emailNotificationEntry.setStatus("mandatory")
_EmailNtfIndex_Type = Integer32
_EmailNtfIndex_Object = MibTableColumn
emailNtfIndex = _EmailNtfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 1),
    _EmailNtfIndex_Type()
)
emailNtfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    emailNtfIndex.setStatus("mandatory")


class _EmailNtfStatus_Type(Integer32):
    """Custom type emailNtfStatus based on Integer32"""
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


_EmailNtfStatus_Type.__name__ = "Integer32"
_EmailNtfStatus_Object = MibTableColumn
emailNtfStatus = _EmailNtfStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 2),
    _EmailNtfStatus_Type()
)
emailNtfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNtfStatus.setStatus("mandatory")
_EmailNtfFromIPAddress_Type = OctetString
_EmailNtfFromIPAddress_Object = MibTableColumn
emailNtfFromIPAddress = _EmailNtfFromIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 3),
    _EmailNtfFromIPAddress_Type()
)
emailNtfFromIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNtfFromIPAddress.setStatus("mandatory")
_EmailNtfToIPAddress_Type = OctetString
_EmailNtfToIPAddress_Object = MibTableColumn
emailNtfToIPAddress = _EmailNtfToIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 4),
    _EmailNtfToIPAddress_Type()
)
emailNtfToIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNtfToIPAddress.setStatus("mandatory")
_EmailNtfServerIPAddress_Type = OctetString
_EmailNtfServerIPAddress_Object = MibTableColumn
emailNtfServerIPAddress = _EmailNtfServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 5),
    _EmailNtfServerIPAddress_Type()
)
emailNtfServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNtfServerIPAddress.setStatus("mandatory")


class _EmailNtfAuthentication_Type(Integer32):
    """Custom type emailNtfAuthentication based on Integer32"""
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


_EmailNtfAuthentication_Type.__name__ = "Integer32"
_EmailNtfAuthentication_Object = MibTableColumn
emailNtfAuthentication = _EmailNtfAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 6),
    _EmailNtfAuthentication_Type()
)
emailNtfAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNtfAuthentication.setStatus("mandatory")
_EmailNtfPassword_Type = OctetString
_EmailNtfPassword_Object = MibTableColumn
emailNtfPassword = _EmailNtfPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 7),
    _EmailNtfPassword_Type()
)
emailNtfPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNtfPassword.setStatus("mandatory")
_EmailNtfOnSchedule_Type = OctetString
_EmailNtfOnSchedule_Object = MibTableColumn
emailNtfOnSchedule = _EmailNtfOnSchedule_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 9),
    _EmailNtfOnSchedule_Type()
)
emailNtfOnSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNtfOnSchedule.setStatus("mandatory")


class _EmailNtfPort_Type(Integer32):
    """Custom type emailNtfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EmailNtfPort_Type.__name__ = "Integer32"
_EmailNtfPort_Object = MibTableColumn
emailNtfPort = _EmailNtfPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 10),
    _EmailNtfPort_Type()
)
emailNtfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNtfPort.setStatus("mandatory")


class _EmailNtfSSL_Type(Integer32):
    """Custom type emailNtfSSL based on Integer32"""
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


_EmailNtfSSL_Type.__name__ = "Integer32"
_EmailNtfSSL_Object = MibTableColumn
emailNtfSSL = _EmailNtfSSL_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 11),
    _EmailNtfSSL_Type()
)
emailNtfSSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNtfSSL.setStatus("mandatory")


class _EmailNtfMailServerIndex_Type(Integer32):
    """Custom type emailNtfMailServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gmail", 2),
          ("hotmail", 3),
          ("internal", 1))
    )


_EmailNtfMailServerIndex_Type.__name__ = "Integer32"
_EmailNtfMailServerIndex_Object = MibTableColumn
emailNtfMailServerIndex = _EmailNtfMailServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 12),
    _EmailNtfMailServerIndex_Type()
)
emailNtfMailServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNtfMailServerIndex.setStatus("mandatory")
_EmailNtfUsername_Type = OctetString
_EmailNtfUsername_Object = MibTableColumn
emailNtfUsername = _EmailNtfUsername_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 4, 11, 1, 1, 13),
    _EmailNtfUsername_Type()
)
emailNtfUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNtfUsername.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7)
)
_TrapSetting_ObjectIdentity = ObjectIdentity
trapSetting = _TrapSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 1)
)


class _TrapStatus_Type(Integer32):
    """Custom type trapStatus based on Integer32"""
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


_TrapStatus_Type.__name__ = "Integer32"
_TrapStatus_Object = MibScalar
trapStatus = _TrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 1, 1),
    _TrapStatus_Type()
)
trapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapStatus.setStatus("mandatory")
_TrapHostTable_Object = MibTable
trapHostTable = _TrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 1, 3)
)
if mibBuilder.loadTexts:
    trapHostTable.setStatus("mandatory")
_TrapHostEntry_Object = MibTableRow
trapHostEntry = _TrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 1, 3, 1)
)
trapHostEntry.setIndexNames(
    (0, "DAP-3520-v115", "trapHostIndex"),
)
if mibBuilder.loadTexts:
    trapHostEntry.setStatus("mandatory")
_TrapHostIndex_Type = Integer32
_TrapHostIndex_Object = MibTableColumn
trapHostIndex = _TrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 1, 3, 1, 1),
    _TrapHostIndex_Type()
)
trapHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapHostIndex.setStatus("mandatory")
_TrapHostIPAddress_Type = IpAddress
_TrapHostIPAddress_Object = MibTableColumn
trapHostIPAddress = _TrapHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 1, 3, 1, 2),
    _TrapHostIPAddress_Type()
)
trapHostIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHostIPAddress.setStatus("mandatory")


class _TrapVersion_Type(Integer32):
    """Custom type trapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2))
    )


_TrapVersion_Type.__name__ = "Integer32"
_TrapVersion_Object = MibTableColumn
trapVersion = _TrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 1, 3, 1, 3),
    _TrapVersion_Type()
)
trapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapVersion.setStatus("mandatory")
_TrapSecurityName_Type = OctetString
_TrapSecurityName_Object = MibTableColumn
trapSecurityName = _TrapSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 1, 3, 1, 4),
    _TrapSecurityName_Type()
)
trapSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSecurityName.setStatus("mandatory")
_TrapInstances_ObjectIdentity = ObjectIdentity
trapInstances = _TrapInstances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2)
)
_Miscellaneous_ObjectIdentity = ObjectIdentity
miscellaneous = _Miscellaneous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 6)
)

# Managed Objects groups


# Notification objects

sshLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 1)
)
sshLoginFail.setObjects(
    ("DAP-3520-v115", "usersName")
)
if mibBuilder.loadTexts:
    sshLoginFail.setStatus(
        "current"
    )

webNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 2)
)
webNotify.setObjects(
    ("DAP-3520-v115", "usersName")
)
if mibBuilder.loadTexts:
    webNotify.setStatus(
        "current"
    )

telnetLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 3)
)
telnetLoginFail.setObjects(
    ("DAP-3520-v115", "usersName")
)
if mibBuilder.loadTexts:
    telnetLoginFail.setStatus(
        "current"
    )

cpuLoadingFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 4)
)
if mibBuilder.loadTexts:
    cpuLoadingFull.setStatus(
        "current"
    )

memoryPoor = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 5)
)
if mibBuilder.loadTexts:
    memoryPoor.setStatus(
        "current"
    )

wlanIfLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 7)
)
wlanIfLinkUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    wlanIfLinkUp.setStatus(
        "current"
    )

deauthenticateAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 8)
)
deauthenticateAttack.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    deauthenticateAttack.setStatus(
        "current"
    )

disassociateAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 9)
)
disassociateAttack.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    disassociateAttack.setStatus(
        "current"
    )

bcFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 10)
)
bcFlood.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    bcFlood.setStatus(
        "current"
    )

webLogoutSuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 11)
)
webLogoutSuccessful.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    webLogoutSuccessful.setStatus(
        "current"
    )

wlanIfLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 13)
)
wlanIfLinkDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    wlanIfLinkDown.setStatus(
        "current"
    )

stationAssocNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 14)
)
if mibBuilder.loadTexts:
    stationAssocNotify.setStatus(
        "current"
    )

stationDisassocNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 15)
)
if mibBuilder.loadTexts:
    stationDisassocNotify.setStatus(
        "current"
    )

deAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 37, 37, 5, 7, 2, 20)
)
if mibBuilder.loadTexts:
    deAuthentication.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DAP-3520-v115",
    **{"DisplayString": DisplayString,
       "enterprises": enterprises,
       "dlink": dlink,
       "dlink-products": dlink_products,
       "dlink-dapfamily": dlink_dapfamily,
       "dap3520": dap3520,
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
       "lanIfPrimaryDNS": lanIfPrimaryDNS,
       "lanIfSecondaryDNS": lanIfSecondaryDNS,
       "wirelesslan": wirelesslan,
       "wirelessLanIfNumber": wirelessLanIfNumber,
       "wirelessLanIfTable": wirelessLanIfTable,
       "wirelessLanIfEntry": wirelessLanIfEntry,
       "wirelessLanIfDesc": wirelessLanIfDesc,
       "wirelessLanIfObjectID": wirelessLanIfObjectID,
       "ieee802dot11": ieee802dot11,
       "dot11Parameters": dot11Parameters,
       "dot11ParametersTable": dot11ParametersTable,
       "dot11ParametersEntry": dot11ParametersEntry,
       "dot11Ssid": dot11Ssid,
       "dot11SsidBroadcast": dot11SsidBroadcast,
       "dot11Channel": dot11Channel,
       "dot11ChannelList": dot11ChannelList,
       "dot11Frequency": dot11Frequency,
       "dot11DataRate": dot11DataRate,
       "dot11WifiMode": dot11WifiMode,
       "dot11BeaconInterval": dot11BeaconInterval,
       "dot11Dtim": dot11Dtim,
       "dot11TransmitPower": dot11TransmitPower,
       "dot11RadioWave": dot11RadioWave,
       "dot11AutoChannelScan": dot11AutoChannelScan,
       "dot11Wmm": dot11Wmm,
       "dot11ApMode": dot11ApMode,
       "dot11ChannelWidth": dot11ChannelWidth,
       "dot11DataRateList": dot11DataRateList,
       "dot11AckTimeout": dot11AckTimeout,
       "dot11ShortGI": dot11ShortGI,
       "dot11Igmpsnooping": dot11Igmpsnooping,
       "dot11Band": dot11Band,
       "dot11Band5GHzDataRateList": dot11Band5GHzDataRateList,
       "dot11Band5GHzWdsChannelList": dot11Band5GHzWdsChannelList,
       "dot11Band5GHzChannelList": dot11Band5GHzChannelList,
       "dot11ApModeStatus": dot11ApModeStatus,
       "dot11Countrycode": dot11Countrycode,
       "dot11Application": dot11Application,
       "dot11Band5GHzOutdoorChannelList": dot11Band5GHzOutdoorChannelList,
       "dot11MulticastRateABandList": dot11MulticastRateABandList,
       "dot11MulticastRateGBandList": dot11MulticastRateGBandList,
       "dot11MulticastRateABand": dot11MulticastRateABand,
       "dot11MulticastRateGBand": dot11MulticastRateGBand,
       "dot11HT2040Coexistence": dot11HT2040Coexistence,
       "dot11RemoteApMacAddress": dot11RemoteApMacAddress,
       "dot11RemoteApMacAddressTable": dot11RemoteApMacAddressTable,
       "dot11RemoteApMacAddressEntry": dot11RemoteApMacAddressEntry,
       "dot11RemoteApMacAddressIndex": dot11RemoteApMacAddressIndex,
       "dot11RemoteApMacAddressList": dot11RemoteApMacAddressList,
       "dot11RemoteApMacAddressAccessTable": dot11RemoteApMacAddressAccessTable,
       "dot11RemoteApMacAddressAccessEntry": dot11RemoteApMacAddressAccessEntry,
       "dot11RemoteApMacAddressAdd": dot11RemoteApMacAddressAdd,
       "dot11RemoteApMacAddressDelete": dot11RemoteApMacAddressDelete,
       "dot11RemoteApMacAddressDeleteAll": dot11RemoteApMacAddressDeleteAll,
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
       "dot11WdsSiteSurvey": dot11WdsSiteSurvey,
       "dot11WdsSiteSurveyRefreshTable": dot11WdsSiteSurveyRefreshTable,
       "dot11WdsSiteSurveyRefreshEntry": dot11WdsSiteSurveyRefreshEntry,
       "dot11WdsSiteSurveyRefresh": dot11WdsSiteSurveyRefresh,
       "dot11WdsSiteSurveyTable": dot11WdsSiteSurveyTable,
       "dot11WdsSiteSurveyEntry": dot11WdsSiteSurveyEntry,
       "dot11WdsSiteSurveyIndex": dot11WdsSiteSurveyIndex,
       "dot11WdsSiteSurveyChannel": dot11WdsSiteSurveyChannel,
       "dot11WdsSiteSurveyMode": dot11WdsSiteSurveyMode,
       "dot11WdsSiteSurveyBssid": dot11WdsSiteSurveyBssid,
       "dot11WdsSiteSurveyEncryption": dot11WdsSiteSurveyEncryption,
       "dot11WdsSiteSurveySsid": dot11WdsSiteSurveySsid,
       "dot11Securities": dot11Securities,
       "dot11SecuritiesTable": dot11SecuritiesTable,
       "dot11SecuritiesEntry": dot11SecuritiesEntry,
       "dot11Authentication": dot11Authentication,
       "dot11Encryption": dot11Encryption,
       "dot11KeyIndex": dot11KeyIndex,
       "dot11PassPhrase": dot11PassPhrase,
       "dot11CipherType": dot11CipherType,
       "dot11GroupKeyUpdateInterval": dot11GroupKeyUpdateInterval,
       "dot11PrimaryRadiusServer": dot11PrimaryRadiusServer,
       "dot11PrimaryRadiusPort": dot11PrimaryRadiusPort,
       "dot11PrimaryRadiusSecret": dot11PrimaryRadiusSecret,
       "dot11NetworkAccessProtection": dot11NetworkAccessProtection,
       "dot11RadiusKeyUpdateInterval": dot11RadiusKeyUpdateInterval,
       "dot11WpaEapType": dot11WpaEapType,
       "dot11WpaEapAuthenticationType": dot11WpaEapAuthenticationType,
       "dot11WpaEapUsername": dot11WpaEapUsername,
       "dot11WpaEapPasswd": dot11WpaEapPasswd,
       "dot11AutoRekeyControl": dot11AutoRekeyControl,
       "dot11AutoRekeyStartWeek": dot11AutoRekeyStartWeek,
       "dot11AutoRekeyStartTime": dot11AutoRekeyStartTime,
       "dot11AutoRekeyTimeInterval": dot11AutoRekeyTimeInterval,
       "dot11AutoRekeyPassPhrase": dot11AutoRekeyPassPhrase,
       "dot11WepKeyTable": dot11WepKeyTable,
       "dot11WepKeyEntry": dot11WepKeyEntry,
       "dot11wepKeyIndex": dot11wepKeyIndex,
       "dot11WepKeyEntryMethod": dot11WepKeyEntryMethod,
       "dot11WepKey": dot11WepKey,
       "dot11Filter": dot11Filter,
       "dot11PartionTable": dot11PartionTable,
       "dot11PartionEntry": dot11PartionEntry,
       "dot11EthernetToWlanAccess": dot11EthernetToWlanAccess,
       "dot11InternalStationConnectionPrimarySSID": dot11InternalStationConnectionPrimarySSID,
       "dot11InternalStationConnectionMultiSSID1": dot11InternalStationConnectionMultiSSID1,
       "dot11InternalStationConnectionMultiSSID2": dot11InternalStationConnectionMultiSSID2,
       "dot11InternalStationConnectionMultiSSID3": dot11InternalStationConnectionMultiSSID3,
       "dot11MacAccessControlTable": dot11MacAccessControlTable,
       "dot11MacAccessControlEntry": dot11MacAccessControlEntry,
       "dot11MacAccessControl": dot11MacAccessControl,
       "dot11MacAccessControlMacAddressAdd": dot11MacAccessControlMacAddressAdd,
       "dot11MacAccessControlMacAddressDelete": dot11MacAccessControlMacAddressDelete,
       "dot11MacAccessControlListTable": dot11MacAccessControlListTable,
       "dot11MacAccessControlListEntry": dot11MacAccessControlListEntry,
       "dot11MacAccessControlListIndex": dot11MacAccessControlListIndex,
       "dot11MacAccessControlListMacAddress": dot11MacAccessControlListMacAddress,
       "dot11ClientInformation": dot11ClientInformation,
       "dot11GetClientInformationTable": dot11GetClientInformationTable,
       "dot11GetClientInformationEntry": dot11GetClientInformationEntry,
       "dot11ClientInformationRefresh": dot11ClientInformationRefresh,
       "dot11ClientInformationTable": dot11ClientInformationTable,
       "dot11ClientInformationEntry": dot11ClientInformationEntry,
       "dot11ClientIndex": dot11ClientIndex,
       "dot11ClientMacAddress": dot11ClientMacAddress,
       "dot11ClientBand": dot11ClientBand,
       "dot11ClientAuthentication": dot11ClientAuthentication,
       "dot11ClientRssi": dot11ClientRssi,
       "dot11ClientPsm": dot11ClientPsm,
       "dot11SSIDIndex": dot11SSIDIndex,
       "dot11ClientIpAddress": dot11ClientIpAddress,
       "dot11ClientTxBytesCount": dot11ClientTxBytesCount,
       "dot11ClientRxBytesCount": dot11ClientRxBytesCount,
       "dot11WdsMonitor": dot11WdsMonitor,
       "dot11GetWdsTable": dot11GetWdsTable,
       "dot11GetWdsEntry": dot11GetWdsEntry,
       "dot11WdsRefresh": dot11WdsRefresh,
       "dot11WdsTable": dot11WdsTable,
       "dot11WdsEntry": dot11WdsEntry,
       "dot11WdsIndex": dot11WdsIndex,
       "dot11WdsMacAddress": dot11WdsMacAddress,
       "dot11WdsBand": dot11WdsBand,
       "dot11WdsAuthentication": dot11WdsAuthentication,
       "dot11WdsRssi": dot11WdsRssi,
       "dot11WdsSsidIndex": dot11WdsSsidIndex,
       "dot11WdsConnected": dot11WdsConnected,
       "dot11WdsStatus": dot11WdsStatus,
       "dot11WdsPsm": dot11WdsPsm,
       "dot11MacClone": dot11MacClone,
       "dot11MacCloneTable": dot11MacCloneTable,
       "dot11MacCloneEntry": dot11MacCloneEntry,
       "dot11MacCloneStatus": dot11MacCloneStatus,
       "dot11MacCloneSource": dot11MacCloneSource,
       "dot11MacCloneMacAddress": dot11MacCloneMacAddress,
       "dot11MacCloneAddressRefresh": dot11MacCloneAddressRefresh,
       "dot11MacCloneSurveryTable": dot11MacCloneSurveryTable,
       "dot11MacCloneSurveryEntry": dot11MacCloneSurveryEntry,
       "dot11MacCloneSurveryIndex": dot11MacCloneSurveryIndex,
       "dot11MacCloneSurveryMacAddress": dot11MacCloneSurveryMacAddress,
       "dot11ZoneDefence": dot11ZoneDefence,
       "dot11ZoneDefenceTable": dot11ZoneDefenceTable,
       "dot11ZoneDefenceEntry": dot11ZoneDefenceEntry,
       "dot11ZoneDefenceControl": dot11ZoneDefenceControl,
       "dot11ZoneDefenceIpAddressAdd": dot11ZoneDefenceIpAddressAdd,
       "dot11ZoneDefenceIpAddressDelete": dot11ZoneDefenceIpAddressDelete,
       "dot11ZoneDefenceIpAddressListTable": dot11ZoneDefenceIpAddressListTable,
       "dot11ZoneDefenceIpAddressListEntry": dot11ZoneDefenceIpAddressListEntry,
       "dot11ZoneDefenceIpAddressListIndex": dot11ZoneDefenceIpAddressListIndex,
       "dot11ZoneDefenceIpAddressList": dot11ZoneDefenceIpAddressList,
       "advance": advance,
       "dhcpServer": dhcpServer,
       "dhcpServerControl": dhcpServerControl,
       "dhcpServerDynamicParameter": dhcpServerDynamicParameter,
       "dhcpServerDynamicControl": dhcpServerDynamicControl,
       "dhcpServerDynamicTable": dhcpServerDynamicTable,
       "dhcpServerDynamicEntry": dhcpServerDynamicEntry,
       "dynamicIndex": dynamicIndex,
       "dynamicIpPoolStart": dynamicIpPoolStart,
       "dynamicIpPoolEnd": dynamicIpPoolEnd,
       "dynamicMask": dynamicMask,
       "dynamicGateway": dynamicGateway,
       "dynamicWins": dynamicWins,
       "dynamicDns": dynamicDns,
       "dynamicDomainName": dynamicDomainName,
       "dynamicLeaseTime": dynamicLeaseTime,
       "dhcpServerDomainNameStatus": dhcpServerDomainNameStatus,
       "dhcpServerStaticParameter": dhcpServerStaticParameter,
       "dhcpServerStaticControl": dhcpServerStaticControl,
       "dhcpServerStaticTable": dhcpServerStaticTable,
       "dhcpServerStaticEntry": dhcpServerStaticEntry,
       "staticIndex": staticIndex,
       "staticEntryStatus": staticEntryStatus,
       "staticHostName": staticHostName,
       "staticIP": staticIP,
       "staticMac": staticMac,
       "staticMask": staticMask,
       "staticGateway": staticGateway,
       "staticDns": staticDns,
       "staticWins": staticWins,
       "staticDomainName": staticDomainName,
       "dhcpServerStaticDelete": dhcpServerStaticDelete,
       "dhcpServerCurrentList": dhcpServerCurrentList,
       "refreshCurrentDynamicList": refreshCurrentDynamicList,
       "currentDynamicTable": currentDynamicTable,
       "currentDynamicEntry": currentDynamicEntry,
       "currentDynamicIndex": currentDynamicIndex,
       "currentDynamicHostName": currentDynamicHostName,
       "currentDynamicMacAddress": currentDynamicMacAddress,
       "currentDynamicAssignedIP": currentDynamicAssignedIP,
       "currentDynamicLease": currentDynamicLease,
       "refreshCurrentStaticList": refreshCurrentStaticList,
       "currentStaticTable": currentStaticTable,
       "currentStaticEntry": currentStaticEntry,
       "currentStaticIndex": currentStaticIndex,
       "currentStaticHostName": currentStaticHostName,
       "currentStaticMacAddress": currentStaticMacAddress,
       "currentStaticAssignedIP": currentStaticAssignedIP,
       "ieee802dot11Grouping": ieee802dot11Grouping,
       "dot11GroupingTable": dot11GroupingTable,
       "dot11GroupingEntry": dot11GroupingEntry,
       "dot11LoadBalance": dot11LoadBalance,
       "dot11UserLimit": dot11UserLimit,
       "dot11LinkIntegrate": dot11LinkIntegrate,
       "ieee802dot11MultiSsid": ieee802dot11MultiSsid,
       "dot11MssidStateTable": dot11MssidStateTable,
       "dot11MssidStateEntry": dot11MssidStateEntry,
       "dot11MssidState": dot11MssidState,
       "dot11MssidPriorityState": dot11MssidPriorityState,
       "dot11MssidTable": dot11MssidTable,
       "dot11MssidEntry": dot11MssidEntry,
       "dot11MssidIndex": dot11MssidIndex,
       "dot11MssIndividualState": dot11MssIndividualState,
       "dot11MssidSsid": dot11MssidSsid,
       "dot11MssidSuppress": dot11MssidSuppress,
       "dot11MssidAuthentication": dot11MssidAuthentication,
       "dot11MssidEncryption": dot11MssidEncryption,
       "dot11MssidWepKeyIndex": dot11MssidWepKeyIndex,
       "dot11MssidWepKey": dot11MssidWepKey,
       "dot11MssidCipherType": dot11MssidCipherType,
       "dot11MssidPassPhrase": dot11MssidPassPhrase,
       "dot11MssidKeyType": dot11MssidKeyType,
       "dot11MssidWmm": dot11MssidWmm,
       "dot11MssidGroupKeyUpdateInterval": dot11MssidGroupKeyUpdateInterval,
       "dot11MssidPriority": dot11MssidPriority,
       "dot11MssidAutoRekeyControl": dot11MssidAutoRekeyControl,
       "dot11MssidAutoRekeyStartWeek": dot11MssidAutoRekeyStartWeek,
       "dot11MssidAutoRekeyStartTime": dot11MssidAutoRekeyStartTime,
       "dot11MssidAutoRekeyTimeInterval": dot11MssidAutoRekeyTimeInterval,
       "dot11MssidAutoRekeyPassPhrase": dot11MssidAutoRekeyPassPhrase,
       "dot11MssidRADIUSTable": dot11MssidRADIUSTable,
       "dot11MssidRADIUSEntry": dot11MssidRADIUSEntry,
       "dot11MssidRADIUSIndex": dot11MssidRADIUSIndex,
       "dot11MssidRADIUSServer": dot11MssidRADIUSServer,
       "dot11MssidRADIUSPort": dot11MssidRADIUSPort,
       "dot11MssidRADIUSSecret": dot11MssidRADIUSSecret,
       "dot11MssidRadiusKeyUpdateInterval": dot11MssidRadiusKeyUpdateInterval,
       "ieee802dot11RogueApDetection": ieee802dot11RogueApDetection,
       "dot11RogueApSurvey": dot11RogueApSurvey,
       "dot11RogueApSurveyRefresh": dot11RogueApSurveyRefresh,
       "dot11RogueApSurveyTable": dot11RogueApSurveyTable,
       "dot11RogueApSurveyEntry": dot11RogueApSurveyEntry,
       "dot11RogueApSurveyIndex": dot11RogueApSurveyIndex,
       "dot11RogueApSurveyChannel": dot11RogueApSurveyChannel,
       "dot11RogueApSurveyBssid": dot11RogueApSurveyBssid,
       "dot11RogueApSurveyMode": dot11RogueApSurveyMode,
       "dot11RogueApSurveySsid": dot11RogueApSurveySsid,
       "dot11RogueApSurveyLastseen": dot11RogueApSurveyLastseen,
       "dot11RogueApSurveyType": dot11RogueApSurveyType,
       "dot11RogueApSurveyStatus": dot11RogueApSurveyStatus,
       "dot11RogueApAddtoValid": dot11RogueApAddtoValid,
       "dot11RogueApAddtoNeighbor": dot11RogueApAddtoNeighbor,
       "dot11RogueApAddtoRouge": dot11RogueApAddtoRouge,
       "dot11RogueApAddtoNew": dot11RogueApAddtoNew,
       "dot11RogueApAllNewNodesAsValid": dot11RogueApAllNewNodesAsValid,
       "dot11RogueApAllNewNodesAsRogue": dot11RogueApAllNewNodesAsRogue,
       "dot11RogueApListRecord": dot11RogueApListRecord,
       "dot11RogueApDeleteFromRecord": dot11RogueApDeleteFromRecord,
       "dot11RogueApListRecordTable": dot11RogueApListRecordTable,
       "dot11RogueApListRecordEntry": dot11RogueApListRecordEntry,
       "dot11RogueApListRecordIndex": dot11RogueApListRecordIndex,
       "dot11RogueApListRecordChannel": dot11RogueApListRecordChannel,
       "dot11RogueApListRecordBssid": dot11RogueApListRecordBssid,
       "dot11RogueApListRecordMode": dot11RogueApListRecordMode,
       "dot11RogueApListRecordSsid": dot11RogueApListRecordSsid,
       "dot11RogueApListRecordLastseen": dot11RogueApListRecordLastseen,
       "dot11RogueApListRecordType": dot11RogueApListRecordType,
       "dot11RogueApListRecordStatus": dot11RogueApListRecordStatus,
       "ieee802dot11VLAN": ieee802dot11VLAN,
       "dot11VLANParameter": dot11VLANParameter,
       "dot11VlanStatus": dot11VlanStatus,
       "dot11VlanMode": dot11VlanMode,
       "dot11GroupVlanListTable": dot11GroupVlanListTable,
       "dot11GroupVlanListEntry": dot11GroupVlanListEntry,
       "dot11GroupVlanListIndex": dot11GroupVlanListIndex,
       "dot11GroupVlanListVid": dot11GroupVlanListVid,
       "dot11GroupVlanListName": dot11GroupVlanListName,
       "dot11GroupVlanListMgmt": dot11GroupVlanListMgmt,
       "dot11GroupVlanListLan": dot11GroupVlanListLan,
       "dot11GroupVlanListPrimary": dot11GroupVlanListPrimary,
       "dot11GroupVlanListMssid1": dot11GroupVlanListMssid1,
       "dot11GroupVlanListMssid2": dot11GroupVlanListMssid2,
       "dot11GroupVlanListMssid3": dot11GroupVlanListMssid3,
       "dot11GroupVlanListWds1": dot11GroupVlanListWds1,
       "dot11GroupVlanListWds2": dot11GroupVlanListWds2,
       "dot11GroupVlanListWds3": dot11GroupVlanListWds3,
       "dot11GroupVlanListWds4": dot11GroupVlanListWds4,
       "dot11VlanListSurveydelete": dot11VlanListSurveydelete,
       "dot11PvidSettingRecord": dot11PvidSettingRecord,
       "dot11PvidAutoAssignStatus": dot11PvidAutoAssignStatus,
       "dot11PvidSettingTable": dot11PvidSettingTable,
       "dot11PvidSettingEntry": dot11PvidSettingEntry,
       "dot11PvidSettingIndex": dot11PvidSettingIndex,
       "dot11PvidSettingMgmt": dot11PvidSettingMgmt,
       "dot11PvidSettingLan": dot11PvidSettingLan,
       "dot11PvidSettingPrimary": dot11PvidSettingPrimary,
       "dot11PvidSettingMssid1": dot11PvidSettingMssid1,
       "dot11PvidSettingMssid2": dot11PvidSettingMssid2,
       "dot11PvidSettingMssid3": dot11PvidSettingMssid3,
       "dot11PvidSettingWds1": dot11PvidSettingWds1,
       "dot11PvidSettingWds2": dot11PvidSettingWds2,
       "dot11PvidSettingWds3": dot11PvidSettingWds3,
       "dot11PvidSettingWds4": dot11PvidSettingWds4,
       "dot11PortListRecord": dot11PortListRecord,
       "dot11PortListRefresh": dot11PortListRefresh,
       "dot11PortListTable": dot11PortListTable,
       "dot11PortListEntry": dot11PortListEntry,
       "dot11PortListIndex": dot11PortListIndex,
       "dot11PortListTagVid": dot11PortListTagVid,
       "dot11PortListUntagVid": dot11PortListUntagVid,
       "dot11PortLisPortName": dot11PortLisPortName,
       "ieee802dot11Qos": ieee802dot11Qos,
       "dot11QosStatus": dot11QosStatus,
       "dot11QosPriorityClassifiers": dot11QosPriorityClassifiers,
       "dot11QosHttp": dot11QosHttp,
       "dot11QosAutomatic": dot11QosAutomatic,
       "dot11QosRuleStatus": dot11QosRuleStatus,
       "dot11QosRulesDelete": dot11QosRulesDelete,
       "dot11QosRulesTable": dot11QosRulesTable,
       "dot11QosRulesEntry": dot11QosRulesEntry,
       "dot11QosRulesIndex": dot11QosRulesIndex,
       "dot11QosRulesState": dot11QosRulesState,
       "dot11QosRulesName": dot11QosRulesName,
       "dot11QosRulesPriority": dot11QosRulesPriority,
       "dot11QosRulesProtocol": dot11QosRulesProtocol,
       "dot11QosRulesProtocolType": dot11QosRulesProtocolType,
       "dot11QosRulesHostOneIpStart": dot11QosRulesHostOneIpStart,
       "dot11QosRulesHostOneIpEnd": dot11QosRulesHostOneIpEnd,
       "dot11QosRulesHostOneIpRange": dot11QosRulesHostOneIpRange,
       "dot11QosRulesHostOnePortStart": dot11QosRulesHostOnePortStart,
       "dot11QosRulesHostOnePortEnd": dot11QosRulesHostOnePortEnd,
       "dot11QosRulesHostOnePortRange": dot11QosRulesHostOnePortRange,
       "dot11QosRulesHostTwoIpStart": dot11QosRulesHostTwoIpStart,
       "dot11QosRulesHostTwoIpEnd": dot11QosRulesHostTwoIpEnd,
       "dot11QosRulesHostTwoIpRange": dot11QosRulesHostTwoIpRange,
       "dot11QosRulesHostTwoPortStart": dot11QosRulesHostTwoPortStart,
       "dot11QosRulesHostTwoPortEnd": dot11QosRulesHostTwoPortEnd,
       "dot11QosRulesHostTwoPortRange": dot11QosRulesHostTwoPortRange,
       "capwap": capwap,
       "capwapWlanSwitchSetting": capwapWlanSwitchSetting,
       "capwapWtpStatus": capwapWtpStatus,
       "capwapWtpName": capwapWtpName,
       "capwapWtpLocationData": capwapWtpLocationData,
       "capwapWtpConnectingSwitchIP": capwapWtpConnectingSwitchIP,
       "capwapWtpConnectingSwitchName": capwapWtpConnectingSwitchName,
       "capwapWtpSwitchIpAddressDelete": capwapWtpSwitchIpAddressDelete,
       "capwapWtpSwitchIpAddressAdd": capwapWtpSwitchIpAddressAdd,
       "wtpSwitchAddressListTable": wtpSwitchAddressListTable,
       "wtpSwitchAddressListEntry": wtpSwitchAddressListEntry,
       "wtpSwitchAddressIndex": wtpSwitchAddressIndex,
       "wtpSwitchIpAddress": wtpSwitchIpAddress,
       "ieee802dot11Schedule": ieee802dot11Schedule,
       "ieee802dot11ScheduleSetting": ieee802dot11ScheduleSetting,
       "ieee802dot11ScheduleStatus": ieee802dot11ScheduleStatus,
       "dot11ScheduleStatus": dot11ScheduleStatus,
       "ieee802dot11ScheduleRuleSetting": ieee802dot11ScheduleRuleSetting,
       "dot11ScheduleRuleName": dot11ScheduleRuleName,
       "dot11ScheduleDaysSelect": dot11ScheduleDaysSelect,
       "dot11ScheduleAllDaySelect": dot11ScheduleAllDaySelect,
       "dot11ScheduleRuleStartTime": dot11ScheduleRuleStartTime,
       "dot11ScheduleRuleEndTime": dot11ScheduleRuleEndTime,
       "dot11ScheduleAction": dot11ScheduleAction,
       "dot11ScheduleSSIDIndex": dot11ScheduleSSIDIndex,
       "dot11ScheduleNodeStatus": dot11ScheduleNodeStatus,
       "dot11ScheduleOverNight": dot11ScheduleOverNight,
       "ieee802dot11ScheduleList": ieee802dot11ScheduleList,
       "dot11ScheduleListTable": dot11ScheduleListTable,
       "dot11ScheduleListEntry": dot11ScheduleListEntry,
       "dot11ScheduleListIndex": dot11ScheduleListIndex,
       "dot11ScheduleListName": dot11ScheduleListName,
       "dot11ScheduleListDays": dot11ScheduleListDays,
       "dot11ScheduleListTimeFrame": dot11ScheduleListTimeFrame,
       "dot11ScheduleListWirelessStatus": dot11ScheduleListWirelessStatus,
       "dot11ScheduleListSSIDIndex": dot11ScheduleListSSIDIndex,
       "dot11ScheduleListSSID": dot11ScheduleListSSID,
       "dot11ScheduleListNodeStatus": dot11ScheduleListNodeStatus,
       "dot11ScheduleListOverNight": dot11ScheduleListOverNight,
       "ieee802dot11APArray": ieee802dot11APArray,
       "ieee802dot11APArraySetting": ieee802dot11APArraySetting,
       "ieee802dot11APArrayStatus": ieee802dot11APArrayStatus,
       "dot11APArrayStatus": dot11APArrayStatus,
       "dot11APArrayModeSelect": dot11APArrayModeSelect,
       "dot11ApArrayName": dot11ApArrayName,
       "dot11ApArrayPassword": dot11ApArrayPassword,
       "ieee802dot11APArrayScans": ieee802dot11APArrayScans,
       "ieee802dot11APArrayScanSetting": ieee802dot11APArrayScanSetting,
       "dot11ApArrayScan": dot11ApArrayScan,
       "ieee802dot11APArrayScanList": ieee802dot11APArrayScanList,
       "dot11APArrayScanListTable": dot11APArrayScanListTable,
       "dot11APArrayScanListEntry": dot11APArrayScanListEntry,
       "dot11APArrayScanListIndex": dot11APArrayScanListIndex,
       "dot11APArrayScanListName": dot11APArrayScanListName,
       "dot11APArrayScanListMasterIP": dot11APArrayScanListMasterIP,
       "dot11APArrayScanListMac": dot11APArrayScanListMac,
       "dot11APArrayScanListMasterNumber": dot11APArrayScanListMasterNumber,
       "dot11APArrayScanListBackupNumber": dot11APArrayScanListBackupNumber,
       "dot11APArrayScanListSlaverNumber": dot11APArrayScanListSlaverNumber,
       "dot11APArrayScanListTotal": dot11APArrayScanListTotal,
       "ieee802dot11APArrayMeberList": ieee802dot11APArrayMeberList,
       "dot11APArrayMeberListTable": dot11APArrayMeberListTable,
       "dot11APArrayMeberListEntry": dot11APArrayMeberListEntry,
       "dot11APArrayMeberListIndex": dot11APArrayMeberListIndex,
       "dot11APArrayMeberListRole": dot11APArrayMeberListRole,
       "dot11APArrayMeberListIP": dot11APArrayMeberListIP,
       "dot11APArrayMeberListMac": dot11APArrayMeberListMac,
       "dot11APArrayMeberListLoacation": dot11APArrayMeberListLoacation,
       "ieee802dot11APArraySyncParametersStatus": ieee802dot11APArraySyncParametersStatus,
       "dot11APArraySyncParametersStatusTable": dot11APArraySyncParametersStatusTable,
       "dot11APArraySyncParametersStatusEntry": dot11APArraySyncParametersStatusEntry,
       "dot11APArraySyncParametersStatusIndex": dot11APArraySyncParametersStatusIndex,
       "dot11APArraySyncSSIDStatus": dot11APArraySyncSSIDStatus,
       "dot11APArraySyncSsidHiddenStatus": dot11APArraySyncSsidHiddenStatus,
       "dot11APArraySyncAutoChannelStatus": dot11APArraySyncAutoChannelStatus,
       "dot11APArraySyncChannelWidthStatus": dot11APArraySyncChannelWidthStatus,
       "dot11APArraySyncSecurityStatus": dot11APArraySyncSecurityStatus,
       "dot11APArraySyncFixedRateStatus": dot11APArraySyncFixedRateStatus,
       "dot11APArraySyncBeaconIntervalStatus": dot11APArraySyncBeaconIntervalStatus,
       "dot11APArraySyncDtimStatus": dot11APArraySyncDtimStatus,
       "dot11APArraySyncTxPowerStatus": dot11APArraySyncTxPowerStatus,
       "dot11APArraySyncWMMStatus": dot11APArraySyncWMMStatus,
       "dot11APArraySyncAckTimeoutStatus": dot11APArraySyncAckTimeoutStatus,
       "dot11APArraySyncShortGIStatus": dot11APArraySyncShortGIStatus,
       "dot11APArraySyncIgmpSnoopStatus": dot11APArraySyncIgmpSnoopStatus,
       "dot11APArraySyncConnectionLimitStatus": dot11APArraySyncConnectionLimitStatus,
       "dot11APArraySyncLinkIntegrityStatus": dot11APArraySyncLinkIntegrityStatus,
       "dot11APArraySyncMultiSsidStatus": dot11APArraySyncMultiSsidStatus,
       "dot11APArraySyncMultiSsidHiddenStatus": dot11APArraySyncMultiSsidHiddenStatus,
       "dot11APArraySyncMultiSsidSecurityStatus": dot11APArraySyncMultiSsidSecurityStatus,
       "dot11APArraySyncMultiSsidWMMStatus": dot11APArraySyncMultiSsidWMMStatus,
       "dot11APArraySyncQOSStatus": dot11APArraySyncQOSStatus,
       "dot11APArraySyncVlanStatus": dot11APArraySyncVlanStatus,
       "dot11APArraySyncScheduleStatus": dot11APArraySyncScheduleStatus,
       "dot11APArraySyncTimeStatus": dot11APArraySyncTimeStatus,
       "dot11APArraySyncLogStatus": dot11APArraySyncLogStatus,
       "dot11APArraySyncAdminLimitStatus": dot11APArraySyncAdminLimitStatus,
       "dot11APArraySyncSystemStatus": dot11APArraySyncSystemStatus,
       "dot11APArraySyncConsoleProtocolStatus": dot11APArraySyncConsoleProtocolStatus,
       "dot11APArraySyncSnmpStatus": dot11APArraySyncSnmpStatus,
       "dot11APArraySyncPingCtlStatus": dot11APArraySyncPingCtlStatus,
       "dot11APArraySyncDhcpStatus": dot11APArraySyncDhcpStatus,
       "dot11APArraySyncLoginStatus": dot11APArraySyncLoginStatus,
       "dot11APArraySyncAclStatus": dot11APArraySyncAclStatus,
       "dot11APArraySyncBandStatus": dot11APArraySyncBandStatus,
       "ieee802dot11WebRedirection": ieee802dot11WebRedirection,
       "ieee802dot11WebRedirectionSetting": ieee802dot11WebRedirectionSetting,
       "dot11WebRedirectionStatus": dot11WebRedirectionStatus,
       "ieee802dot11WebRedirectionAccountSetting": ieee802dot11WebRedirectionAccountSetting,
       "dot11WebRedirectionAccountName": dot11WebRedirectionAccountName,
       "dot11WebRedirectionAccountPasswd": dot11WebRedirectionAccountPasswd,
       "dot11WebRedirectionAccountStatus": dot11WebRedirectionAccountStatus,
       "dot11WebRedirectionAccountAction": dot11WebRedirectionAccountAction,
       "dot11WebRedirectionAccountTable": dot11WebRedirectionAccountTable,
       "dot11WebRedirectionAccountEntry": dot11WebRedirectionAccountEntry,
       "dot11WebRedirectionIndex": dot11WebRedirectionIndex,
       "dot11WebRedirectionListAccountName": dot11WebRedirectionListAccountName,
       "dot11WebRedirectionListAccountPasswd": dot11WebRedirectionListAccountPasswd,
       "dot11WebRedirectionListAccountStatus": dot11WebRedirectionListAccountStatus,
       "ieee802dot11ARPSpoofingPrevention": ieee802dot11ARPSpoofingPrevention,
       "ieee802dot11ARPSpoofingPreventionSetting": ieee802dot11ARPSpoofingPreventionSetting,
       "dot11ARPSpoofingPreventionStatus": dot11ARPSpoofingPreventionStatus,
       "ieee802dot11ARPSpoofingPreventionAddressSetting": ieee802dot11ARPSpoofingPreventionAddressSetting,
       "dot11ARPSpoofingPreventionIpAddress": dot11ARPSpoofingPreventionIpAddress,
       "dot11ARPSpoofingPreventionMacAddress": dot11ARPSpoofingPreventionMacAddress,
       "dot11ARPSpoofingPreventionAction": dot11ARPSpoofingPreventionAction,
       "dot11ARPSpoofingPreventionTable": dot11ARPSpoofingPreventionTable,
       "dot11ARPSpoofingPreventionEntry": dot11ARPSpoofingPreventionEntry,
       "dot11ARPSpoofingPreventionIndex": dot11ARPSpoofingPreventionIndex,
       "dot11ARPSpoofingPreventionListIpAddress": dot11ARPSpoofingPreventionListIpAddress,
       "dot11ARPSpoofingPreventionListMacAddress": dot11ARPSpoofingPreventionListMacAddress,
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
       "deviceSettingApply": deviceSettingApply,
       "deviceSettingDiscard": deviceSettingDiscard,
       "languagePackClear": languagePackClear,
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
       "updateStatus": updateStatus,
       "console": console,
       "telnet": telnet,
       "ssh": ssh,
       "timeout": timeout,
       "web": web,
       "webStatus": webStatus,
       "snmp": snmp,
       "ssl": ssl,
       "sntp": sntp,
       "sntpServerIpAddress": sntpServerIpAddress,
       "sntpTimeZoneIndex": sntpTimeZoneIndex,
       "sntpDayLightSaving": sntpDayLightSaving,
       "sntpTimeofDay": sntpTimeofDay,
       "sntpStatus": sntpStatus,
       "sntpInterval": sntpInterval,
       "setTimeManually": setTimeManually,
       "sntpDstStartMonth": sntpDstStartMonth,
       "sntpDstStartWeek": sntpDstStartWeek,
       "sntpDstStartDayOfWeek": sntpDstStartDayOfWeek,
       "sntpDstStartCurrentTime": sntpDstStartCurrentTime,
       "sntpDstEndMonth": sntpDstEndMonth,
       "sntpDstEndWeek": sntpDstEndWeek,
       "sntpDstEndDayOfWeek": sntpDstEndDayOfWeek,
       "sntpDstEndCurrentTime": sntpDstEndCurrentTime,
       "sntpDayLightSavingOffset": sntpDayLightSavingOffset,
       "smtp": smtp,
       "smtpStatus": smtpStatus,
       "smtpServerIpAddress": smtpServerIpAddress,
       "smtpAccountingName": smtpAccountingName,
       "smtpPassword": smtpPassword,
       "limitedAdministrator": limitedAdministrator,
       "managerAddress": managerAddress,
       "managerIpAddressStatus": managerIpAddressStatus,
       "managerIpAddressDelete": managerIpAddressDelete,
       "managerIpAddressTable": managerIpAddressTable,
       "managerIpAddressEntry": managerIpAddressEntry,
       "managerIpAddressIndex": managerIpAddressIndex,
       "managerIpAddressPoolStart": managerIpAddressPoolStart,
       "managerIpAddressPoolEnd": managerIpAddressPoolEnd,
       "manergeVLANTag": manergeVLANTag,
       "pingControl": pingControl,
       "pingControlStatus": pingControlStatus,
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
       "wirelessLed2dot4G": wirelessLed2dot4G,
       "wirelessLed5G": wirelessLed5G,
       "dataBaseChannel": dataBaseChannel,
       "mssid1MacAddress": mssid1MacAddress,
       "mssid2MacAddress": mssid2MacAddress,
       "mssid3MacAddress": mssid3MacAddress,
       "lanLED": lanLED,
       "trafficStatistics": trafficStatistics,
       "trafficStatisticsWired": trafficStatisticsWired,
       "dot3TrafficStatistics": dot3TrafficStatistics,
       "dot3TrafficStatisticsTable": dot3TrafficStatisticsTable,
       "dot3TrafficStatisticsEntry": dot3TrafficStatisticsEntry,
       "dot3TransmittedPacketCount": dot3TransmittedPacketCount,
       "dot3TransmittedBytesCount": dot3TransmittedBytesCount,
       "dot3TransmittedDroppedPacketCount": dot3TransmittedDroppedPacketCount,
       "dot3ReceivedPacketCount": dot3ReceivedPacketCount,
       "dot3ReceivedBytesCount": dot3ReceivedBytesCount,
       "dot3ReceivedDroppedPacketCount": dot3ReceivedDroppedPacketCount,
       "dot3Clear": dot3Clear,
       "trafficStatisticsWireless": trafficStatisticsWireless,
       "dot11TrafficStatistics": dot11TrafficStatistics,
       "dot11TrafficStatisticsTable": dot11TrafficStatisticsTable,
       "dot11TrafficStatisticsEntry": dot11TrafficStatisticsEntry,
       "dot11TransmitSuccessRate": dot11TransmitSuccessRate,
       "dot11TransmitRetryRate": dot11TransmitRetryRate,
       "dot11TransmittedPacketCount": dot11TransmittedPacketCount,
       "dot11TransmittedBytesCount": dot11TransmittedBytesCount,
       "dot11TransmittedDroppedPacketCount": dot11TransmittedDroppedPacketCount,
       "dot11TransmittedRetryCount": dot11TransmittedRetryCount,
       "dot11ReceivedPacketCount": dot11ReceivedPacketCount,
       "dot11ReceivedBytesCount": dot11ReceivedBytesCount,
       "dot11ReceivedDroppedPacketCount": dot11ReceivedDroppedPacketCount,
       "dot11ReceivedCRCCount": dot11ReceivedCRCCount,
       "dot11ReceivedDecryptionErrorCount": dot11ReceivedDecryptionErrorCount,
       "dot11ReceivedMICErrorCount": dot11ReceivedMICErrorCount,
       "dot11ReceivedPHYErrorCount": dot11ReceivedPHYErrorCount,
       "dot11Clear": dot11Clear,
       "systemLog": systemLog,
       "systemLogSystemLevel": systemLogSystemLevel,
       "systemLogWirelessLevel": systemLogWirelessLevel,
       "systemLogNoticeLevel": systemLogNoticeLevel,
       "systemLogTFTPServerIPAddress": systemLogTFTPServerIPAddress,
       "systemLogFileName": systemLogFileName,
       "systemLogGetLog": systemLogGetLog,
       "systemLogRemoteLogState": systemLogRemoteLogState,
       "systemLogServerIPAddress": systemLogServerIPAddress,
       "systemLogClearLocalLog": systemLogClearLocalLog,
       "emailNotification": emailNotification,
       "emailNotificationTable": emailNotificationTable,
       "emailNotificationEntry": emailNotificationEntry,
       "emailNtfIndex": emailNtfIndex,
       "emailNtfStatus": emailNtfStatus,
       "emailNtfFromIPAddress": emailNtfFromIPAddress,
       "emailNtfToIPAddress": emailNtfToIPAddress,
       "emailNtfServerIPAddress": emailNtfServerIPAddress,
       "emailNtfAuthentication": emailNtfAuthentication,
       "emailNtfPassword": emailNtfPassword,
       "emailNtfOnSchedule": emailNtfOnSchedule,
       "emailNtfPort": emailNtfPort,
       "emailNtfSSL": emailNtfSSL,
       "emailNtfMailServerIndex": emailNtfMailServerIndex,
       "emailNtfUsername": emailNtfUsername,
       "traps": traps,
       "trapSetting": trapSetting,
       "trapStatus": trapStatus,
       "trapHostTable": trapHostTable,
       "trapHostEntry": trapHostEntry,
       "trapHostIndex": trapHostIndex,
       "trapHostIPAddress": trapHostIPAddress,
       "trapVersion": trapVersion,
       "trapSecurityName": trapSecurityName,
       "trapInstances": trapInstances,
       "sshLoginFail": sshLoginFail,
       "webNotify": webNotify,
       "telnetLoginFail": telnetLoginFail,
       "cpuLoadingFull": cpuLoadingFull,
       "memoryPoor": memoryPoor,
       "wlanIfLinkUp": wlanIfLinkUp,
       "deauthenticateAttack": deauthenticateAttack,
       "disassociateAttack": disassociateAttack,
       "bcFlood": bcFlood,
       "webLogoutSuccessful": webLogoutSuccessful,
       "wlanIfLinkDown": wlanIfLinkDown,
       "stationAssocNotify": stationAssocNotify,
       "stationDisassocNotify": stationDisassocNotify,
       "deAuthentication": deAuthentication,
       "miscellaneous": miscellaneous}
)
