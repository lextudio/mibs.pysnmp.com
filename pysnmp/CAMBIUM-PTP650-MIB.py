# SNMP MIB module (CAMBIUM-PTP650-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAMBIUM-PTP650-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:27 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

cambium = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713)
)
cambium.setRevisions(
        ("2015-02-06 04:43",
         "2014-06-18 14:12",
         "2014-02-21 15:03",
         "2013-08-02 10:28")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ptp_ObjectIdentity = ObjectIdentity
ptp = _Ptp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1)
)
_Ptmp_ObjectIdentity = ObjectIdentity
ptmp = _Ptmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 2)
)
_Ptp650_ObjectIdentity = ObjectIdentity
ptp650 = _Ptp650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7)
)
_Dfs_ObjectIdentity = ObjectIdentity
dfs = _Dfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 3)
)


class _DfsTableNumber_Type(Integer32):
    """Custom type dfsTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_DfsTableNumber_Type.__name__ = "Integer32"
_DfsTableNumber_Object = MibScalar
dfsTableNumber = _DfsTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 3, 1),
    _DfsTableNumber_Type()
)
dfsTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsTableNumber.setStatus("current")
_DfsTable_Object = MibTable
dfsTable = _DfsTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 3, 2)
)
if mibBuilder.loadTexts:
    dfsTable.setStatus("current")
_DfsTableEntry_Object = MibTableRow
dfsTableEntry = _DfsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 3, 2, 1)
)
dfsTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP650-MIB", "dfsTableIndex"),
)
if mibBuilder.loadTexts:
    dfsTableEntry.setStatus("current")


class _DfsTableIndex_Type(Integer32):
    """Custom type dfsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_DfsTableIndex_Type.__name__ = "Integer32"
_DfsTableIndex_Object = MibTableColumn
dfsTableIndex = _DfsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 3, 2, 1, 1),
    _DfsTableIndex_Type()
)
dfsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfsTableIndex.setStatus("current")
_DfsMeans_Type = Integer32
_DfsMeans_Object = MibTableColumn
dfsMeans = _DfsMeans_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 3, 2, 1, 2),
    _DfsMeans_Type()
)
dfsMeans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsMeans.setStatus("current")
_DfsNineNinePointNinePercentiles_Type = Integer32
_DfsNineNinePointNinePercentiles_Object = MibTableColumn
dfsNineNinePointNinePercentiles = _DfsNineNinePointNinePercentiles_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 3, 2, 1, 3),
    _DfsNineNinePointNinePercentiles_Type()
)
dfsNineNinePointNinePercentiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsNineNinePointNinePercentiles.setStatus("current")
_DfsPeaks_Type = Integer32
_DfsPeaks_Object = MibTableColumn
dfsPeaks = _DfsPeaks_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 3, 2, 1, 4),
    _DfsPeaks_Type()
)
dfsPeaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsPeaks.setStatus("current")


class _ExtendedSpectrumScanning_Type(Integer32):
    """Custom type extendedSpectrumScanning based on Integer32"""
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


_ExtendedSpectrumScanning_Type.__name__ = "Integer32"
_ExtendedSpectrumScanning_Object = MibScalar
extendedSpectrumScanning = _ExtendedSpectrumScanning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 3, 3),
    _ExtendedSpectrumScanning_Type()
)
extendedSpectrumScanning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendedSpectrumScanning.setStatus("current")
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 4)
)


class _LocalPacketFiltering_Type(Integer32):
    """Custom type localPacketFiltering based on Integer32"""
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


_LocalPacketFiltering_Type.__name__ = "Integer32"
_LocalPacketFiltering_Object = MibScalar
localPacketFiltering = _LocalPacketFiltering_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 4, 1),
    _LocalPacketFiltering_Type()
)
localPacketFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localPacketFiltering.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5)
)
_IPv4Address_Type = IpAddress
_IPv4Address_Object = MibScalar
iPv4Address = _IPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 1),
    _IPv4Address_Type()
)
iPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPv4Address.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_GatewayIPAddress_Type = IpAddress
_GatewayIPAddress_Object = MibScalar
gatewayIPAddress = _GatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 3),
    _GatewayIPAddress_Type()
)
gatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayIPAddress.setStatus("current")


class _TargetMACAddress_Type(OctetString):
    """Custom type targetMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TargetMACAddress_Type.__name__ = "OctetString"
_TargetMACAddress_Object = MibScalar
targetMACAddress = _TargetMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 4),
    _TargetMACAddress_Type()
)
targetMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetMACAddress.setStatus("current")


class _MasterSlaveMode_Type(Integer32):
    """Custom type masterSlaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_MasterSlaveMode_Type.__name__ = "Integer32"
_MasterSlaveMode_Object = MibScalar
masterSlaveMode = _MasterSlaveMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 5),
    _MasterSlaveMode_Type()
)
masterSlaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterSlaveMode.setStatus("current")


class _MaximumTransmitPower_Type(Integer32):
    """Custom type maximumTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 30),
    )


_MaximumTransmitPower_Type.__name__ = "Integer32"
_MaximumTransmitPower_Object = MibScalar
maximumTransmitPower = _MaximumTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 6),
    _MaximumTransmitPower_Type()
)
maximumTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumTransmitPower.setStatus("current")


class _AntennaGain_Type(Integer32):
    """Custom type antennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(130, 610),
    )


_AntennaGain_Type.__name__ = "Integer32"
_AntennaGain_Object = MibScalar
antennaGain = _AntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 7),
    _AntennaGain_Type()
)
antennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antennaGain.setStatus("current")


class _CableLoss_Type(Integer32):
    """Custom type cableLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CableLoss_Type.__name__ = "Integer32"
_CableLoss_Object = MibScalar
cableLoss = _CableLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 8),
    _CableLoss_Type()
)
cableLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableLoss.setStatus("current")
_EIRP_Type = Integer32
_EIRP_Object = MibScalar
eIRP = _EIRP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 9),
    _EIRP_Type()
)
eIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eIRP.setStatus("current")


class _ChannelBandwidth_Type(Integer32):
    """Custom type channelBandwidth based on Integer32"""
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
        *(("bw10MHz", 2),
          ("bw15MHz", 1),
          ("bw20MHz", 4),
          ("bw30MHz", 0),
          ("bw40MHz", 7),
          ("bw45MHz", 8),
          ("bw50MHz", 6),
          ("bw56MHz", 5),
          ("bw5MHz", 3))
    )


_ChannelBandwidth_Type.__name__ = "Integer32"
_ChannelBandwidth_Object = MibScalar
channelBandwidth = _ChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 11),
    _ChannelBandwidth_Type()
)
channelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBandwidth.setStatus("current")


class _LinkName_Type(DisplayString):
    """Custom type linkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LinkName_Type.__name__ = "DisplayString"
_LinkName_Object = MibScalar
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 14),
    _LinkName_Type()
)
linkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkName.setStatus("current")


class _SiteName_Type(DisplayString):
    """Custom type siteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SiteName_Type.__name__ = "DisplayString"
_SiteName_Object = MibScalar
siteName = _SiteName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 15),
    _SiteName_Type()
)
siteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteName.setStatus("current")


class _AccessMethod_Type(Integer32):
    """Custom type accessMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("groupAccess", 2),
          ("linkAccess", 0),
          ("linkNameAccess", 1))
    )


_AccessMethod_Type.__name__ = "Integer32"
_AccessMethod_Object = MibScalar
accessMethod = _AccessMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 16),
    _AccessMethod_Type()
)
accessMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessMethod.setStatus("current")


class _GroupID_Type(Integer32):
    """Custom type groupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GroupID_Type.__name__ = "Integer32"
_GroupID_Object = MibScalar
groupID = _GroupID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 17),
    _GroupID_Type()
)
groupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupID.setStatus("current")


class _IPv6Address_Type(DisplayString):
    """Custom type iPv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IPv6Address_Type.__name__ = "DisplayString"
_IPv6Address_Object = MibScalar
iPv6Address = _IPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 18),
    _IPv6Address_Type()
)
iPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPv6Address.setStatus("current")


class _IPVersion_Type(Integer32):
    """Custom type iPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dualIPv4andIPv6", 2),
          ("iPv4", 0),
          ("iPv6", 1))
    )


_IPVersion_Type.__name__ = "Integer32"
_IPVersion_Object = MibScalar
iPVersion = _IPVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 20),
    _IPVersion_Type()
)
iPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPVersion.setStatus("current")


class _IPv6AutoConfiguredLinkLocalAddress_Type(DisplayString):
    """Custom type iPv6AutoConfiguredLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IPv6AutoConfiguredLinkLocalAddress_Type.__name__ = "DisplayString"
_IPv6AutoConfiguredLinkLocalAddress_Object = MibScalar
iPv6AutoConfiguredLinkLocalAddress = _IPv6AutoConfiguredLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 21),
    _IPv6AutoConfiguredLinkLocalAddress_Type()
)
iPv6AutoConfiguredLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPv6AutoConfiguredLinkLocalAddress.setStatus("current")


class _IPv6PrefixLength_Type(Integer32):
    """Custom type iPv6PrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IPv6PrefixLength_Type.__name__ = "Integer32"
_IPv6PrefixLength_Object = MibScalar
iPv6PrefixLength = _IPv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 22),
    _IPv6PrefixLength_Type()
)
iPv6PrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPv6PrefixLength.setStatus("current")


class _IPv6GatewayAddress_Type(DisplayString):
    """Custom type iPv6GatewayAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IPv6GatewayAddress_Type.__name__ = "DisplayString"
_IPv6GatewayAddress_Object = MibScalar
iPv6GatewayAddress = _IPv6GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 23),
    _IPv6GatewayAddress_Type()
)
iPv6GatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPv6GatewayAddress.setStatus("current")


class _RemoteInternetAddressType_Type(Integer32):
    """Custom type remoteInternetAddressType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dns", 16),
          ("ipv4", 1),
          ("ipv4z", 3),
          ("ipv6", 2),
          ("ipv6z", 4),
          ("unknown", 0),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8))
    )


_RemoteInternetAddressType_Type.__name__ = "Integer32"
_RemoteInternetAddressType_Object = MibScalar
remoteInternetAddressType = _RemoteInternetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 24),
    _RemoteInternetAddressType_Type()
)
remoteInternetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteInternetAddressType.setStatus("current")
_RemoteInternetAddress_Type = InetAddress
_RemoteInternetAddress_Object = MibScalar
remoteInternetAddress = _RemoteInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 25),
    _RemoteInternetAddress_Type()
)
remoteInternetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteInternetAddress.setStatus("current")
_SubbandLowestFrequency_Type = Integer32
_SubbandLowestFrequency_Object = MibScalar
subbandLowestFrequency = _SubbandLowestFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 26),
    _SubbandLowestFrequency_Type()
)
subbandLowestFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subbandLowestFrequency.setStatus("current")
_SubbandHighestFrequency_Type = Integer32
_SubbandHighestFrequency_Object = MibScalar
subbandHighestFrequency = _SubbandHighestFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 27),
    _SubbandHighestFrequency_Type()
)
subbandHighestFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subbandHighestFrequency.setStatus("current")


class _EnableTransmission_Type(Integer32):
    """Custom type enableTransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 0),
          ("muted", 1))
    )


_EnableTransmission_Type.__name__ = "Integer32"
_EnableTransmission_Object = MibScalar
enableTransmission = _EnableTransmission_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 5, 28),
    _EnableTransmission_Type()
)
enableTransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTransmission.setStatus("current")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6)
)


class _MainPSUPortAutoNegotiation_Type(Integer32):
    """Custom type mainPSUPortAutoNegotiation based on Integer32"""
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


_MainPSUPortAutoNegotiation_Type.__name__ = "Integer32"
_MainPSUPortAutoNegotiation_Object = MibScalar
mainPSUPortAutoNegotiation = _MainPSUPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 1),
    _MainPSUPortAutoNegotiation_Type()
)
mainPSUPortAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortAutoNegotiation.setStatus("current")


class _MainPSUPortAutoNegAdvertisement_Type(Bits):
    """Custom type mainPSUPortAutoNegAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("neg1000MbpsFullDuplex", 7),
          ("neg100MbpsFullDuplex", 6),
          ("neg100MbpsHalfDuplex", 5),
          ("neg10MbpsFullDuplex", 4),
          ("neg10MbpsHalfDuplex", 3),
          ("negInvalid", 2))
    )

_MainPSUPortAutoNegAdvertisement_Type.__name__ = "Bits"
_MainPSUPortAutoNegAdvertisement_Object = MibScalar
mainPSUPortAutoNegAdvertisement = _MainPSUPortAutoNegAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 2),
    _MainPSUPortAutoNegAdvertisement_Type()
)
mainPSUPortAutoNegAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortAutoNegAdvertisement.setStatus("current")


class _MainPSUPortAutoMdix_Type(Integer32):
    """Custom type mainPSUPortAutoMdix based on Integer32"""
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


_MainPSUPortAutoMdix_Type.__name__ = "Integer32"
_MainPSUPortAutoMdix_Object = MibScalar
mainPSUPortAutoMdix = _MainPSUPortAutoMdix_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 3),
    _MainPSUPortAutoMdix_Type()
)
mainPSUPortAutoMdix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortAutoMdix.setStatus("current")


class _MainPSUPortStatus_Type(Integer32):
    """Custom type mainPSUPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copperLinkUp", 1),
          ("down", 0),
          ("fiberLinkUp", 2))
    )


_MainPSUPortStatus_Type.__name__ = "Integer32"
_MainPSUPortStatus_Object = MibScalar
mainPSUPortStatus = _MainPSUPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 4),
    _MainPSUPortStatus_Type()
)
mainPSUPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortStatus.setStatus("current")


class _MainPSUPortSpeedAndDuplex_Type(Integer32):
    """Custom type mainPSUPortSpeedAndDuplex based on Integer32"""
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
        *(("speed1000MbpsFullDuplex", 0),
          ("speed100MbpsFullDuplex", 1),
          ("speed100MbpsHalfDuplex", 2),
          ("speed10MbpsFullDuplex", 3),
          ("speed10MbpsHalfDuplex", 4),
          ("speedUnknown6", 5))
    )


_MainPSUPortSpeedAndDuplex_Type.__name__ = "Integer32"
_MainPSUPortSpeedAndDuplex_Object = MibScalar
mainPSUPortSpeedAndDuplex = _MainPSUPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 5),
    _MainPSUPortSpeedAndDuplex_Type()
)
mainPSUPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortSpeedAndDuplex.setStatus("current")


class _DataPortWirelessDownAlert_Type(Integer32):
    """Custom type dataPortWirelessDownAlert based on Integer32"""
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


_DataPortWirelessDownAlert_Type.__name__ = "Integer32"
_DataPortWirelessDownAlert_Object = MibScalar
dataPortWirelessDownAlert = _DataPortWirelessDownAlert_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 6),
    _DataPortWirelessDownAlert_Type()
)
dataPortWirelessDownAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortWirelessDownAlert.setStatus("current")


class _UseVLANForManagementInterfaces_Type(Integer32):
    """Custom type useVLANForManagementInterfaces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iEEE8021QTaggedCTagType8100", 1),
          ("iEEE8021adTaggedSTagorBTagType88a8", 2),
          ("noVLANTagging", 0))
    )


_UseVLANForManagementInterfaces_Type.__name__ = "Integer32"
_UseVLANForManagementInterfaces_Object = MibScalar
useVLANForManagementInterfaces = _UseVLANForManagementInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 7),
    _UseVLANForManagementInterfaces_Type()
)
useVLANForManagementInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useVLANForManagementInterfaces.setStatus("current")


class _VLANManagementPriority_Type(Integer32):
    """Custom type vLANManagementPriority based on Integer32"""
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
        *(("p0", 0),
          ("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("p5", 5),
          ("p6", 6),
          ("p7", 7))
    )


_VLANManagementPriority_Type.__name__ = "Integer32"
_VLANManagementPriority_Object = MibScalar
vLANManagementPriority = _VLANManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 8),
    _VLANManagementPriority_Type()
)
vLANManagementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANManagementPriority.setStatus("current")


class _VLANManagementVID_Type(Integer32):
    """Custom type vLANManagementVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VLANManagementVID_Type.__name__ = "Integer32"
_VLANManagementVID_Object = MibScalar
vLANManagementVID = _VLANManagementVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 11),
    _VLANManagementVID_Type()
)
vLANManagementVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANManagementVID.setStatus("current")


class _AuxPortStatus_Type(Integer32):
    """Custom type auxPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("copperLinkUp", 1),
          ("down", 0))
    )


_AuxPortStatus_Type.__name__ = "Integer32"
_AuxPortStatus_Object = MibScalar
auxPortStatus = _AuxPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 12),
    _AuxPortStatus_Type()
)
auxPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortStatus.setStatus("current")


class _AuxPortSpeedAndDuplex_Type(Integer32):
    """Custom type auxPortSpeedAndDuplex based on Integer32"""
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
        *(("speed1000MbpsFullDuplex", 0),
          ("speed100MbpsFullDuplex", 1),
          ("speed100MbpsHalfDuplex", 2),
          ("speed10MbpsFullDuplex", 3),
          ("speed10MbpsHalfDuplex", 4),
          ("speedUnknown6", 5))
    )


_AuxPortSpeedAndDuplex_Type.__name__ = "Integer32"
_AuxPortSpeedAndDuplex_Object = MibScalar
auxPortSpeedAndDuplex = _AuxPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 13),
    _AuxPortSpeedAndDuplex_Type()
)
auxPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortSpeedAndDuplex.setStatus("current")


class _EthernetPriorityTableNumber_Type(Integer32):
    """Custom type ethernetPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 9),
    )


_EthernetPriorityTableNumber_Type.__name__ = "Integer32"
_EthernetPriorityTableNumber_Object = MibScalar
ethernetPriorityTableNumber = _EthernetPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 14),
    _EthernetPriorityTableNumber_Type()
)
ethernetPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPriorityTableNumber.setStatus("current")
_EthernetPriorityTable_Object = MibTable
ethernetPriorityTable = _EthernetPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 15)
)
if mibBuilder.loadTexts:
    ethernetPriorityTable.setStatus("current")
_EthernetPriorityTableEntry_Object = MibTableRow
ethernetPriorityTableEntry = _EthernetPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 15, 1)
)
ethernetPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP650-MIB", "ethernetPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    ethernetPriorityTableEntry.setStatus("current")


class _EthernetPriorityTableIndex_Type(Integer32):
    """Custom type ethernetPriorityTableIndex based on Integer32"""
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
        *(("p0", 1),
          ("p1", 2),
          ("p2", 3),
          ("p3", 4),
          ("p4", 5),
          ("p5", 6),
          ("p6", 7),
          ("p7", 8),
          ("untagged", 9))
    )


_EthernetPriorityTableIndex_Type.__name__ = "Integer32"
_EthernetPriorityTableIndex_Object = MibTableColumn
ethernetPriorityTableIndex = _EthernetPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 15, 1, 1),
    _EthernetPriorityTableIndex_Type()
)
ethernetPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethernetPriorityTableIndex.setStatus("current")


class _EthernetPriorityQueueMapping_Type(Integer32):
    """Custom type ethernetPriorityQueueMapping based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_EthernetPriorityQueueMapping_Type.__name__ = "Integer32"
_EthernetPriorityQueueMapping_Object = MibTableColumn
ethernetPriorityQueueMapping = _EthernetPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 15, 1, 2),
    _EthernetPriorityQueueMapping_Type()
)
ethernetPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPriorityQueueMapping.setStatus("current")


class _L2CPPriorityTableNumber_Type(Integer32):
    """Custom type l2CPPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
    )


_L2CPPriorityTableNumber_Type.__name__ = "Integer32"
_L2CPPriorityTableNumber_Object = MibScalar
l2CPPriorityTableNumber = _L2CPPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 16),
    _L2CPPriorityTableNumber_Type()
)
l2CPPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2CPPriorityTableNumber.setStatus("current")
_L2CPPriorityTable_Object = MibTable
l2CPPriorityTable = _L2CPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 17)
)
if mibBuilder.loadTexts:
    l2CPPriorityTable.setStatus("current")
_L2CPPriorityTableEntry_Object = MibTableRow
l2CPPriorityTableEntry = _L2CPPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 17, 1)
)
l2CPPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP650-MIB", "l2CPPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    l2CPPriorityTableEntry.setStatus("current")


class _L2CPPriorityTableIndex_Type(Integer32):
    """Custom type l2CPPriorityTableIndex based on Integer32"""
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
        *(("bridge", 1),
          ("cFM", 3),
          ("eAPS", 5),
          ("mRP", 2),
          ("rAPS", 4))
    )


_L2CPPriorityTableIndex_Type.__name__ = "Integer32"
_L2CPPriorityTableIndex_Object = MibTableColumn
l2CPPriorityTableIndex = _L2CPPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 17, 1, 1),
    _L2CPPriorityTableIndex_Type()
)
l2CPPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2CPPriorityTableIndex.setStatus("current")


class _L2CPPriorityQueueMapping_Type(Integer32):
    """Custom type l2CPPriorityQueueMapping based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_L2CPPriorityQueueMapping_Type.__name__ = "Integer32"
_L2CPPriorityQueueMapping_Object = MibTableColumn
l2CPPriorityQueueMapping = _L2CPPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 17, 1, 2),
    _L2CPPriorityQueueMapping_Type()
)
l2CPPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2CPPriorityQueueMapping.setStatus("current")


class _IPDSCPPriorityTableNumber_Type(Integer32):
    """Custom type iPDSCPPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 64),
    )


_IPDSCPPriorityTableNumber_Type.__name__ = "Integer32"
_IPDSCPPriorityTableNumber_Object = MibScalar
iPDSCPPriorityTableNumber = _IPDSCPPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 18),
    _IPDSCPPriorityTableNumber_Type()
)
iPDSCPPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPDSCPPriorityTableNumber.setStatus("current")
_IPDSCPPriorityTable_Object = MibTable
iPDSCPPriorityTable = _IPDSCPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 19)
)
if mibBuilder.loadTexts:
    iPDSCPPriorityTable.setStatus("current")
_IPDSCPPriorityTableEntry_Object = MibTableRow
iPDSCPPriorityTableEntry = _IPDSCPPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 19, 1)
)
iPDSCPPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP650-MIB", "iPDSCPPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    iPDSCPPriorityTableEntry.setStatus("current")


class _IPDSCPPriorityTableIndex_Type(Integer32):
    """Custom type iPDSCPPriorityTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IPDSCPPriorityTableIndex_Type.__name__ = "Integer32"
_IPDSCPPriorityTableIndex_Object = MibTableColumn
iPDSCPPriorityTableIndex = _IPDSCPPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 19, 1, 1),
    _IPDSCPPriorityTableIndex_Type()
)
iPDSCPPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iPDSCPPriorityTableIndex.setStatus("current")


class _IPDSCPPriorityQueueMapping_Type(Integer32):
    """Custom type iPDSCPPriorityQueueMapping based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_IPDSCPPriorityQueueMapping_Type.__name__ = "Integer32"
_IPDSCPPriorityQueueMapping_Object = MibTableColumn
iPDSCPPriorityQueueMapping = _IPDSCPPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 19, 1, 2),
    _IPDSCPPriorityQueueMapping_Type()
)
iPDSCPPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPDSCPPriorityQueueMapping.setStatus("current")


class _MPLSTCPriorityTableNumber_Type(Integer32):
    """Custom type mPLSTCPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8),
    )


_MPLSTCPriorityTableNumber_Type.__name__ = "Integer32"
_MPLSTCPriorityTableNumber_Object = MibScalar
mPLSTCPriorityTableNumber = _MPLSTCPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 20),
    _MPLSTCPriorityTableNumber_Type()
)
mPLSTCPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPLSTCPriorityTableNumber.setStatus("current")
_MPLSTCPriorityTable_Object = MibTable
mPLSTCPriorityTable = _MPLSTCPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 21)
)
if mibBuilder.loadTexts:
    mPLSTCPriorityTable.setStatus("current")
_MPLSTCPriorityTableEntry_Object = MibTableRow
mPLSTCPriorityTableEntry = _MPLSTCPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 21, 1)
)
mPLSTCPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP650-MIB", "mPLSTCPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    mPLSTCPriorityTableEntry.setStatus("current")


class _MPLSTCPriorityTableIndex_Type(Integer32):
    """Custom type mPLSTCPriorityTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MPLSTCPriorityTableIndex_Type.__name__ = "Integer32"
_MPLSTCPriorityTableIndex_Object = MibTableColumn
mPLSTCPriorityTableIndex = _MPLSTCPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 21, 1, 1),
    _MPLSTCPriorityTableIndex_Type()
)
mPLSTCPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mPLSTCPriorityTableIndex.setStatus("current")


class _MPLSTCPriorityQueueMapping_Type(Integer32):
    """Custom type mPLSTCPriorityQueueMapping based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_MPLSTCPriorityQueueMapping_Type.__name__ = "Integer32"
_MPLSTCPriorityQueueMapping_Object = MibTableColumn
mPLSTCPriorityQueueMapping = _MPLSTCPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 21, 1, 2),
    _MPLSTCPriorityQueueMapping_Type()
)
mPLSTCPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mPLSTCPriorityQueueMapping.setStatus("current")


class _ManagementPortWirelessDownAlert_Type(Integer32):
    """Custom type managementPortWirelessDownAlert based on Integer32"""
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


_ManagementPortWirelessDownAlert_Type.__name__ = "Integer32"
_ManagementPortWirelessDownAlert_Object = MibScalar
managementPortWirelessDownAlert = _ManagementPortWirelessDownAlert_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 23),
    _ManagementPortWirelessDownAlert_Type()
)
managementPortWirelessDownAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementPortWirelessDownAlert.setStatus("current")


class _QOSPriorityScheme_Type(Integer32):
    """Custom type qOSPriorityScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("iPMPLS", 1))
    )


_QOSPriorityScheme_Type.__name__ = "Integer32"
_QOSPriorityScheme_Object = MibScalar
qOSPriorityScheme = _QOSPriorityScheme_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 24),
    _QOSPriorityScheme_Type()
)
qOSPriorityScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qOSPriorityScheme.setStatus("current")


class _UnknownNetworkPriorityQueueMapping_Type(Integer32):
    """Custom type unknownNetworkPriorityQueueMapping based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_UnknownNetworkPriorityQueueMapping_Type.__name__ = "Integer32"
_UnknownNetworkPriorityQueueMapping_Object = MibScalar
unknownNetworkPriorityQueueMapping = _UnknownNetworkPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 25),
    _UnknownNetworkPriorityQueueMapping_Type()
)
unknownNetworkPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownNetworkPriorityQueueMapping.setStatus("current")


class _DSCPManagementPriority_Type(Integer32):
    """Custom type dSCPManagementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DSCPManagementPriority_Type.__name__ = "Integer32"
_DSCPManagementPriority_Object = MibScalar
dSCPManagementPriority = _DSCPManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 26),
    _DSCPManagementPriority_Type()
)
dSCPManagementPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSCPManagementPriority.setStatus("current")


class _DataBridgingStatus_Type(Integer32):
    """Custom type dataBridgingStatus based on Integer32"""
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


_DataBridgingStatus_Type.__name__ = "Integer32"
_DataBridgingStatus_Object = MibScalar
dataBridgingStatus = _DataBridgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 27),
    _DataBridgingStatus_Type()
)
dataBridgingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataBridgingStatus.setStatus("current")


class _MainPSUPortAllocation_Type(Integer32):
    """Custom type mainPSUPortAllocation based on Integer32"""
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
        *(("dataOnly", 1),
          ("dataandInBandManagement", 2),
          ("disabled", 0),
          ("outofBandLocalManagement", 3),
          ("outofBandRemoteManagement", 4),
          ("secondDataOnly", 5),
          ("secondDataandInBandManagement", 6))
    )


_MainPSUPortAllocation_Type.__name__ = "Integer32"
_MainPSUPortAllocation_Object = MibScalar
mainPSUPortAllocation = _MainPSUPortAllocation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 28),
    _MainPSUPortAllocation_Type()
)
mainPSUPortAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortAllocation.setStatus("current")


class _AuxPortAllocation_Type(Integer32):
    """Custom type auxPortAllocation based on Integer32"""
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
        *(("dataOnly", 1),
          ("dataandInBandManagement", 2),
          ("disabled", 0),
          ("outofBandLocalManagement", 3),
          ("outofBandRemoteManagement", 4),
          ("secondDataOnly", 5),
          ("secondDataandInBandManagement", 6))
    )


_AuxPortAllocation_Type.__name__ = "Integer32"
_AuxPortAllocation_Object = MibScalar
auxPortAllocation = _AuxPortAllocation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 29),
    _AuxPortAllocation_Type()
)
auxPortAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortAllocation.setStatus("current")


class _SFPPortAllocation_Type(Integer32):
    """Custom type sFPPortAllocation based on Integer32"""
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
        *(("dataOnly", 1),
          ("dataandInBandManagement", 2),
          ("disabled", 0),
          ("outofBandLocalManagement", 3),
          ("outofBandRemoteManagement", 4),
          ("secondDataOnly", 5),
          ("secondDataandInBandManagement", 6))
    )


_SFPPortAllocation_Type.__name__ = "Integer32"
_SFPPortAllocation_Object = MibScalar
sFPPortAllocation = _SFPPortAllocation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 30),
    _SFPPortAllocation_Type()
)
sFPPortAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortAllocation.setStatus("current")


class _DataPortPauseFrames_Type(Integer32):
    """Custom type dataPortPauseFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("tunnel", 0))
    )


_DataPortPauseFrames_Type.__name__ = "Integer32"
_DataPortPauseFrames_Object = MibScalar
dataPortPauseFrames = _DataPortPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 31),
    _DataPortPauseFrames_Type()
)
dataPortPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortPauseFrames.setStatus("current")


class _SFPPortAutoNegotiation_Type(Integer32):
    """Custom type sFPPortAutoNegotiation based on Integer32"""
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


_SFPPortAutoNegotiation_Type.__name__ = "Integer32"
_SFPPortAutoNegotiation_Object = MibScalar
sFPPortAutoNegotiation = _SFPPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 32),
    _SFPPortAutoNegotiation_Type()
)
sFPPortAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortAutoNegotiation.setStatus("current")


class _SFPPortAutoNegAdvertisement_Type(Bits):
    """Custom type sFPPortAutoNegAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("neg1000MbpsFullDuplex", 7),
          ("neg100MbpsFullDuplex", 6),
          ("neg100MbpsHalfDuplex", 5),
          ("neg10MbpsFullDuplex", 4),
          ("neg10MbpsHalfDuplex", 3),
          ("negInvalid", 2))
    )

_SFPPortAutoNegAdvertisement_Type.__name__ = "Bits"
_SFPPortAutoNegAdvertisement_Object = MibScalar
sFPPortAutoNegAdvertisement = _SFPPortAutoNegAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 33),
    _SFPPortAutoNegAdvertisement_Type()
)
sFPPortAutoNegAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortAutoNegAdvertisement.setStatus("current")


class _SFPPortAutoMdix_Type(Integer32):
    """Custom type sFPPortAutoMdix based on Integer32"""
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


_SFPPortAutoMdix_Type.__name__ = "Integer32"
_SFPPortAutoMdix_Object = MibScalar
sFPPortAutoMdix = _SFPPortAutoMdix_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 34),
    _SFPPortAutoMdix_Type()
)
sFPPortAutoMdix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortAutoMdix.setStatus("current")


class _SFPPortStatus_Type(Integer32):
    """Custom type sFPPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copperLinkUp", 1),
          ("down", 0),
          ("fiberLinkUp", 2))
    )


_SFPPortStatus_Type.__name__ = "Integer32"
_SFPPortStatus_Object = MibScalar
sFPPortStatus = _SFPPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 35),
    _SFPPortStatus_Type()
)
sFPPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortStatus.setStatus("current")


class _SFPPortSpeedAndDuplex_Type(Integer32):
    """Custom type sFPPortSpeedAndDuplex based on Integer32"""
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
        *(("speed1000MbpsFullDuplex", 0),
          ("speed100MbpsFullDuplex", 1),
          ("speed100MbpsHalfDuplex", 2),
          ("speed10MbpsFullDuplex", 3),
          ("speed10MbpsHalfDuplex", 4),
          ("speedUnknown6", 5))
    )


_SFPPortSpeedAndDuplex_Type.__name__ = "Integer32"
_SFPPortSpeedAndDuplex_Object = MibScalar
sFPPortSpeedAndDuplex = _SFPPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 36),
    _SFPPortSpeedAndDuplex_Type()
)
sFPPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortSpeedAndDuplex.setStatus("current")


class _AuxPortPowerOverEthernetOutput_Type(Integer32):
    """Custom type auxPortPowerOverEthernetOutput based on Integer32"""
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


_AuxPortPowerOverEthernetOutput_Type.__name__ = "Integer32"
_AuxPortPowerOverEthernetOutput_Object = MibScalar
auxPortPowerOverEthernetOutput = _AuxPortPowerOverEthernetOutput_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 37),
    _AuxPortPowerOverEthernetOutput_Type()
)
auxPortPowerOverEthernetOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortPowerOverEthernetOutput.setStatus("current")


class _AuxPortPowerOverEthernetOutputStatus_Type(Integer32):
    """Custom type auxPortPowerOverEthernetOutputStatus based on Integer32"""
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
        *(("poEOutputDisabled", 1),
          ("poEOutputEnabledbutNotActiveErrororNoLoadPresent", 2),
          ("poEOutputErrorDetected", 5),
          ("poEOutputOn", 0),
          ("poEOutputOverTempError", 4),
          ("poEOutputOverloadError", 3))
    )


_AuxPortPowerOverEthernetOutputStatus_Type.__name__ = "Integer32"
_AuxPortPowerOverEthernetOutputStatus_Object = MibScalar
auxPortPowerOverEthernetOutputStatus = _AuxPortPowerOverEthernetOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 38),
    _AuxPortPowerOverEthernetOutputStatus_Type()
)
auxPortPowerOverEthernetOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortPowerOverEthernetOutputStatus.setStatus("current")


class _SyncETracking_Type(Integer32):
    """Custom type syncETracking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("internalTDMUseOnly", 2))
    )


_SyncETracking_Type.__name__ = "Integer32"
_SyncETracking_Object = MibScalar
syncETracking = _SyncETracking_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 39),
    _SyncETracking_Type()
)
syncETracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncETracking.setStatus("current")


class _SyncEEquipmentClock_Type(Integer32):
    """Custom type syncEEquipmentClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eECOption1", 0),
          ("eECOption2", 1))
    )


_SyncEEquipmentClock_Type.__name__ = "Integer32"
_SyncEEquipmentClock_Object = MibScalar
syncEEquipmentClock = _SyncEEquipmentClock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 40),
    _SyncEEquipmentClock_Type()
)
syncEEquipmentClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncEEquipmentClock.setStatus("current")


class _MainPSUPortQLRxOverwrite_Type(Integer32):
    """Custom type mainPSUPortQLRxOverwrite based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("qLDNUQLDUS", 12),
          ("qLEEC1QLSEC", 9),
          ("qLEEC2QLST3", 8),
          ("qLPRC", 3),
          ("qLPROV", 11),
          ("qLPRS", 1),
          ("qLSMC", 10),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST2", 4),
          ("qLST3E", 7),
          ("qLSTU", 2))
    )


_MainPSUPortQLRxOverwrite_Type.__name__ = "Integer32"
_MainPSUPortQLRxOverwrite_Object = MibScalar
mainPSUPortQLRxOverwrite = _MainPSUPortQLRxOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 41),
    _MainPSUPortQLRxOverwrite_Type()
)
mainPSUPortQLRxOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainPSUPortQLRxOverwrite.setStatus("current")


class _MainPSUPortSSMTx_Type(Integer32):
    """Custom type mainPSUPortSSMTx based on Integer32"""
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


_MainPSUPortSSMTx_Type.__name__ = "Integer32"
_MainPSUPortSSMTx_Object = MibScalar
mainPSUPortSSMTx = _MainPSUPortSSMTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 42),
    _MainPSUPortSSMTx_Type()
)
mainPSUPortSSMTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainPSUPortSSMTx.setStatus("current")


class _SFPPortSSMTx_Type(Integer32):
    """Custom type sFPPortSSMTx based on Integer32"""
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


_SFPPortSSMTx_Type.__name__ = "Integer32"
_SFPPortSSMTx_Object = MibScalar
sFPPortSSMTx = _SFPPortSSMTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 43),
    _SFPPortSSMTx_Type()
)
sFPPortSSMTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFPPortSSMTx.setStatus("current")


class _AuxPortSSMTx_Type(Integer32):
    """Custom type auxPortSSMTx based on Integer32"""
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


_AuxPortSSMTx_Type.__name__ = "Integer32"
_AuxPortSSMTx_Object = MibScalar
auxPortSSMTx = _AuxPortSSMTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 44),
    _AuxPortSSMTx_Type()
)
auxPortSSMTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxPortSSMTx.setStatus("current")


class _SyncETrackingState_Type(Integer32):
    """Custom type syncETrackingState based on Integer32"""
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
        *(("acquiringWirelessLock", 1),
          ("disabled", 0),
          ("freeRunning", 2),
          ("holdover", 5),
          ("lockedLocalAcquiringHoldover", 3),
          ("lockedLocalHoldoverAcquired", 4),
          ("lockedRemoteAcquiringHoldover", 6),
          ("lockedRemoteHoldoverAcquired", 7))
    )


_SyncETrackingState_Type.__name__ = "Integer32"
_SyncETrackingState_Object = MibScalar
syncETrackingState = _SyncETrackingState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 45),
    _SyncETrackingState_Type()
)
syncETrackingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncETrackingState.setStatus("current")


class _MainPSUPortQLRx_Type(Integer32):
    """Custom type mainPSUPortQLRx based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLDNUQLDUS", 12),
          ("qLEEC1QLSEC", 9),
          ("qLEEC2QLST3", 8),
          ("qLFAILED", 13),
          ("qLPRC", 3),
          ("qLPROV", 11),
          ("qLPRS", 1),
          ("qLSMC", 10),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST2", 4),
          ("qLST3E", 7),
          ("qLSTU", 2))
    )


_MainPSUPortQLRx_Type.__name__ = "Integer32"
_MainPSUPortQLRx_Object = MibScalar
mainPSUPortQLRx = _MainPSUPortQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 46),
    _MainPSUPortQLRx_Type()
)
mainPSUPortQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortQLRx.setStatus("current")


class _AuxPortQLRx_Type(Integer32):
    """Custom type auxPortQLRx based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLDNUQLDUS", 12),
          ("qLEEC1QLSEC", 9),
          ("qLEEC2QLST3", 8),
          ("qLFAILED", 13),
          ("qLPRC", 3),
          ("qLPROV", 11),
          ("qLPRS", 1),
          ("qLSMC", 10),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST2", 4),
          ("qLST3E", 7),
          ("qLSTU", 2))
    )


_AuxPortQLRx_Type.__name__ = "Integer32"
_AuxPortQLRx_Object = MibScalar
auxPortQLRx = _AuxPortQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 47),
    _AuxPortQLRx_Type()
)
auxPortQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortQLRx.setStatus("current")


class _SFPPortQLRx_Type(Integer32):
    """Custom type sFPPortQLRx based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLDNUQLDUS", 12),
          ("qLEEC1QLSEC", 9),
          ("qLEEC2QLST3", 8),
          ("qLFAILED", 13),
          ("qLPRC", 3),
          ("qLPROV", 11),
          ("qLPRS", 1),
          ("qLSMC", 10),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST2", 4),
          ("qLST3E", 7),
          ("qLSTU", 2))
    )


_SFPPortQLRx_Type.__name__ = "Integer32"
_SFPPortQLRx_Object = MibScalar
sFPPortQLRx = _SFPPortQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 48),
    _SFPPortQLRx_Type()
)
sFPPortQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortQLRx.setStatus("current")


class _MainPSUPortQLTx_Type(Integer32):
    """Custom type mainPSUPortQLTx based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLDNUQLDUS", 12),
          ("qLEEC1QLSEC", 9),
          ("qLEEC2QLST3", 8),
          ("qLPRC", 3),
          ("qLPROV", 11),
          ("qLPRS", 1),
          ("qLSMC", 10),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST2", 4),
          ("qLST3E", 7),
          ("qLSTU", 2))
    )


_MainPSUPortQLTx_Type.__name__ = "Integer32"
_MainPSUPortQLTx_Object = MibScalar
mainPSUPortQLTx = _MainPSUPortQLTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 49),
    _MainPSUPortQLTx_Type()
)
mainPSUPortQLTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortQLTx.setStatus("current")


class _AuxPortQLTx_Type(Integer32):
    """Custom type auxPortQLTx based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLDNUQLDUS", 12),
          ("qLEEC1QLSEC", 9),
          ("qLEEC2QLST3", 8),
          ("qLPRC", 3),
          ("qLPROV", 11),
          ("qLPRS", 1),
          ("qLSMC", 10),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST2", 4),
          ("qLST3E", 7),
          ("qLSTU", 2))
    )


_AuxPortQLTx_Type.__name__ = "Integer32"
_AuxPortQLTx_Object = MibScalar
auxPortQLTx = _AuxPortQLTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 50),
    _AuxPortQLTx_Type()
)
auxPortQLTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortQLTx.setStatus("current")


class _SFPPortQLTx_Type(Integer32):
    """Custom type sFPPortQLTx based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLDNUQLDUS", 12),
          ("qLEEC1QLSEC", 9),
          ("qLEEC2QLST3", 8),
          ("qLPRC", 3),
          ("qLPROV", 11),
          ("qLPRS", 1),
          ("qLSMC", 10),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST2", 4),
          ("qLST3E", 7),
          ("qLSTU", 2))
    )


_SFPPortQLTx_Type.__name__ = "Integer32"
_SFPPortQLTx_Object = MibScalar
sFPPortQLTx = _SFPPortQLTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 51),
    _SFPPortQLTx_Type()
)
sFPPortQLTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortQLTx.setStatus("current")


class _MainPSUPortSyncEMasterSlaveStatus_Type(Integer32):
    """Custom type mainPSUPortSyncEMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_MainPSUPortSyncEMasterSlaveStatus_Type.__name__ = "Integer32"
_MainPSUPortSyncEMasterSlaveStatus_Object = MibScalar
mainPSUPortSyncEMasterSlaveStatus = _MainPSUPortSyncEMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 52),
    _MainPSUPortSyncEMasterSlaveStatus_Type()
)
mainPSUPortSyncEMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortSyncEMasterSlaveStatus.setStatus("current")


class _AuxPortSyncEMasterSlaveStatus_Type(Integer32):
    """Custom type auxPortSyncEMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_AuxPortSyncEMasterSlaveStatus_Type.__name__ = "Integer32"
_AuxPortSyncEMasterSlaveStatus_Object = MibScalar
auxPortSyncEMasterSlaveStatus = _AuxPortSyncEMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 53),
    _AuxPortSyncEMasterSlaveStatus_Type()
)
auxPortSyncEMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortSyncEMasterSlaveStatus.setStatus("current")


class _SFPPortSyncEMasterSlaveStatus_Type(Integer32):
    """Custom type sFPPortSyncEMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_SFPPortSyncEMasterSlaveStatus_Type.__name__ = "Integer32"
_SFPPortSyncEMasterSlaveStatus_Object = MibScalar
sFPPortSyncEMasterSlaveStatus = _SFPPortSyncEMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 54),
    _SFPPortSyncEMasterSlaveStatus_Type()
)
sFPPortSyncEMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortSyncEMasterSlaveStatus.setStatus("current")


class _MainPSUPortGigabitMasterSlaveStatus_Type(Integer32):
    """Custom type mainPSUPortGigabitMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("notApplicable", 2),
          ("slave", 1))
    )


_MainPSUPortGigabitMasterSlaveStatus_Type.__name__ = "Integer32"
_MainPSUPortGigabitMasterSlaveStatus_Object = MibScalar
mainPSUPortGigabitMasterSlaveStatus = _MainPSUPortGigabitMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 55),
    _MainPSUPortGigabitMasterSlaveStatus_Type()
)
mainPSUPortGigabitMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortGigabitMasterSlaveStatus.setStatus("current")


class _AuxPortGigabitMasterSlaveStatus_Type(Integer32):
    """Custom type auxPortGigabitMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("notApplicable", 2),
          ("slave", 1))
    )


_AuxPortGigabitMasterSlaveStatus_Type.__name__ = "Integer32"
_AuxPortGigabitMasterSlaveStatus_Object = MibScalar
auxPortGigabitMasterSlaveStatus = _AuxPortGigabitMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 56),
    _AuxPortGigabitMasterSlaveStatus_Type()
)
auxPortGigabitMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortGigabitMasterSlaveStatus.setStatus("current")


class _SFPPortGigabitMasterSlaveStatus_Type(Integer32):
    """Custom type sFPPortGigabitMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("notApplicable", 2),
          ("slave", 1))
    )


_SFPPortGigabitMasterSlaveStatus_Type.__name__ = "Integer32"
_SFPPortGigabitMasterSlaveStatus_Object = MibScalar
sFPPortGigabitMasterSlaveStatus = _SFPPortGigabitMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 57),
    _SFPPortGigabitMasterSlaveStatus_Type()
)
sFPPortGigabitMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortGigabitMasterSlaveStatus.setStatus("current")


class _TransparentClock_Type(Integer32):
    """Custom type transparentClock based on Integer32"""
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


_TransparentClock_Type.__name__ = "Integer32"
_TransparentClock_Object = MibScalar
transparentClock = _TransparentClock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 58),
    _TransparentClock_Type()
)
transparentClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transparentClock.setStatus("current")


class _TransparentClockVLAN_Type(Integer32):
    """Custom type transparentClockVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("cTagged", 2),
          ("sTagged", 1))
    )


_TransparentClockVLAN_Type.__name__ = "Integer32"
_TransparentClockVLAN_Object = MibScalar
transparentClockVLAN = _TransparentClockVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 59),
    _TransparentClockVLAN_Type()
)
transparentClockVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transparentClockVLAN.setStatus("current")


class _TransparentClockVID_Type(Integer32):
    """Custom type transparentClockVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TransparentClockVID_Type.__name__ = "Integer32"
_TransparentClockVID_Object = MibScalar
transparentClockVID = _TransparentClockVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 60),
    _TransparentClockVID_Type()
)
transparentClockVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transparentClockVID.setStatus("current")


class _MainPSUPortAcceptedQLRx_Type(Integer32):
    """Custom type mainPSUPortAcceptedQLRx based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLDNUQLDUS", 12),
          ("qLEEC1QLSEC", 9),
          ("qLEEC2QLST3", 8),
          ("qLFAILED", 13),
          ("qLPRC", 3),
          ("qLPROV", 11),
          ("qLPRS", 1),
          ("qLSMC", 10),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST2", 4),
          ("qLST3E", 7),
          ("qLSTU", 2))
    )


_MainPSUPortAcceptedQLRx_Type.__name__ = "Integer32"
_MainPSUPortAcceptedQLRx_Object = MibScalar
mainPSUPortAcceptedQLRx = _MainPSUPortAcceptedQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 61),
    _MainPSUPortAcceptedQLRx_Type()
)
mainPSUPortAcceptedQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortAcceptedQLRx.setStatus("current")


class _AuxPortAcceptedQLRx_Type(Integer32):
    """Custom type auxPortAcceptedQLRx based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLDNUQLDUS", 12),
          ("qLEEC1QLSEC", 9),
          ("qLEEC2QLST3", 8),
          ("qLFAILED", 13),
          ("qLPRC", 3),
          ("qLPROV", 11),
          ("qLPRS", 1),
          ("qLSMC", 10),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST2", 4),
          ("qLST3E", 7),
          ("qLSTU", 2))
    )


_AuxPortAcceptedQLRx_Type.__name__ = "Integer32"
_AuxPortAcceptedQLRx_Object = MibScalar
auxPortAcceptedQLRx = _AuxPortAcceptedQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 62),
    _AuxPortAcceptedQLRx_Type()
)
auxPortAcceptedQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortAcceptedQLRx.setStatus("current")


class _SFPPortAcceptedQLRx_Type(Integer32):
    """Custom type sFPPortAcceptedQLRx based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLDNUQLDUS", 12),
          ("qLEEC1QLSEC", 9),
          ("qLEEC2QLST3", 8),
          ("qLFAILED", 13),
          ("qLPRC", 3),
          ("qLPROV", 11),
          ("qLPRS", 1),
          ("qLSMC", 10),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST2", 4),
          ("qLST3E", 7),
          ("qLSTU", 2))
    )


_SFPPortAcceptedQLRx_Type.__name__ = "Integer32"
_SFPPortAcceptedQLRx_Object = MibScalar
sFPPortAcceptedQLRx = _SFPPortAcceptedQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 63),
    _SFPPortAcceptedQLRx_Type()
)
sFPPortAcceptedQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortAcceptedQLRx.setStatus("current")


class _MainPSUPortSyncERxStatus_Type(Integer32):
    """Custom type mainPSUPortSyncERxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("good", 0),
          ("waittoRestore", 1))
    )


_MainPSUPortSyncERxStatus_Type.__name__ = "Integer32"
_MainPSUPortSyncERxStatus_Object = MibScalar
mainPSUPortSyncERxStatus = _MainPSUPortSyncERxStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 64),
    _MainPSUPortSyncERxStatus_Type()
)
mainPSUPortSyncERxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortSyncERxStatus.setStatus("current")


class _AuxPortSyncERxStatus_Type(Integer32):
    """Custom type auxPortSyncERxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("good", 0),
          ("waittoRestore", 1))
    )


_AuxPortSyncERxStatus_Type.__name__ = "Integer32"
_AuxPortSyncERxStatus_Object = MibScalar
auxPortSyncERxStatus = _AuxPortSyncERxStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 65),
    _AuxPortSyncERxStatus_Type()
)
auxPortSyncERxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortSyncERxStatus.setStatus("current")


class _SFPPortSyncERxStatus_Type(Integer32):
    """Custom type sFPPortSyncERxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("good", 0),
          ("waittoRestore", 1))
    )


_SFPPortSyncERxStatus_Type.__name__ = "Integer32"
_SFPPortSyncERxStatus_Object = MibScalar
sFPPortSyncERxStatus = _SFPPortSyncERxStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 66),
    _SFPPortSyncERxStatus_Type()
)
sFPPortSyncERxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortSyncERxStatus.setStatus("current")


class _NIDULanPortStatus_Type(Integer32):
    """Custom type nIDULanPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copperLinkUp", 1),
          ("down", 0),
          ("fiberLinkUp", 2))
    )


_NIDULanPortStatus_Type.__name__ = "Integer32"
_NIDULanPortStatus_Object = MibScalar
nIDULanPortStatus = _NIDULanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 67),
    _NIDULanPortStatus_Type()
)
nIDULanPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortStatus.setStatus("current")


class _NIDULanPortSpeedAndDuplex_Type(Integer32):
    """Custom type nIDULanPortSpeedAndDuplex based on Integer32"""
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
        *(("speed1000MbpsFullDuplex", 0),
          ("speed100MbpsFullDuplex", 1),
          ("speed100MbpsHalfDuplex", 2),
          ("speed10MbpsFullDuplex", 3),
          ("speed10MbpsHalfDuplex", 4),
          ("speedUnknown6", 5))
    )


_NIDULanPortSpeedAndDuplex_Type.__name__ = "Integer32"
_NIDULanPortSpeedAndDuplex_Object = MibScalar
nIDULanPortSpeedAndDuplex = _NIDULanPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 68),
    _NIDULanPortSpeedAndDuplex_Type()
)
nIDULanPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortSpeedAndDuplex.setStatus("current")


class _OOBPriorityQueueMapping_Type(Integer32):
    """Custom type oOBPriorityQueueMapping based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_OOBPriorityQueueMapping_Type.__name__ = "Integer32"
_OOBPriorityQueueMapping_Object = MibScalar
oOBPriorityQueueMapping = _OOBPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 69),
    _OOBPriorityQueueMapping_Type()
)
oOBPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oOBPriorityQueueMapping.setStatus("current")


class _NIDULanPortAutoNegotiation_Type(Integer32):
    """Custom type nIDULanPortAutoNegotiation based on Integer32"""
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


_NIDULanPortAutoNegotiation_Type.__name__ = "Integer32"
_NIDULanPortAutoNegotiation_Object = MibScalar
nIDULanPortAutoNegotiation = _NIDULanPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 70),
    _NIDULanPortAutoNegotiation_Type()
)
nIDULanPortAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortAutoNegotiation.setStatus("current")


class _NIDULanPortAutoNegAdvertisement_Type(Bits):
    """Custom type nIDULanPortAutoNegAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("neg1000MbpsFullDuplex", 7),
          ("neg100MbpsFullDuplex", 6),
          ("neg100MbpsHalfDuplex", 5),
          ("neg10MbpsFullDuplex", 4),
          ("neg10MbpsHalfDuplex", 3),
          ("negInvalid", 2))
    )

_NIDULanPortAutoNegAdvertisement_Type.__name__ = "Bits"
_NIDULanPortAutoNegAdvertisement_Object = MibScalar
nIDULanPortAutoNegAdvertisement = _NIDULanPortAutoNegAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 71),
    _NIDULanPortAutoNegAdvertisement_Type()
)
nIDULanPortAutoNegAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortAutoNegAdvertisement.setStatus("current")


class _NIDULanPortAutoMdix_Type(Integer32):
    """Custom type nIDULanPortAutoMdix based on Integer32"""
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


_NIDULanPortAutoMdix_Type.__name__ = "Integer32"
_NIDULanPortAutoMdix_Object = MibScalar
nIDULanPortAutoMdix = _NIDULanPortAutoMdix_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 72),
    _NIDULanPortAutoMdix_Type()
)
nIDULanPortAutoMdix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortAutoMdix.setStatus("current")


class _NIDULanPortGigabitMasterSlaveStatus_Type(Integer32):
    """Custom type nIDULanPortGigabitMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("notApplicable", 2),
          ("slave", 1))
    )


_NIDULanPortGigabitMasterSlaveStatus_Type.__name__ = "Integer32"
_NIDULanPortGigabitMasterSlaveStatus_Object = MibScalar
nIDULanPortGigabitMasterSlaveStatus = _NIDULanPortGigabitMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 73),
    _NIDULanPortGigabitMasterSlaveStatus_Type()
)
nIDULanPortGigabitMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortGigabitMasterSlaveStatus.setStatus("current")
_TxMABFrames_Type = Integer32
_TxMABFrames_Object = MibScalar
txMABFrames = _TxMABFrames_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 74),
    _TxMABFrames_Type()
)
txMABFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMABFrames.setStatus("current")


class _ManagementNetworkAccessEnabled_Type(Integer32):
    """Custom type managementNetworkAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ManagementNetworkAccessEnabled_Type.__name__ = "Integer32"
_ManagementNetworkAccessEnabled_Object = MibScalar
managementNetworkAccessEnabled = _ManagementNetworkAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 75),
    _ManagementNetworkAccessEnabled_Type()
)
managementNetworkAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementNetworkAccessEnabled.setStatus("current")


class _SecondDataPortPauseFrames_Type(Integer32):
    """Custom type secondDataPortPauseFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("tunnel", 0))
    )


_SecondDataPortPauseFrames_Type.__name__ = "Integer32"
_SecondDataPortPauseFrames_Object = MibScalar
secondDataPortPauseFrames = _SecondDataPortPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 76),
    _SecondDataPortPauseFrames_Type()
)
secondDataPortPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondDataPortPauseFrames.setStatus("current")


class _SecondDataBridgingStatus_Type(Integer32):
    """Custom type secondDataBridgingStatus based on Integer32"""
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


_SecondDataBridgingStatus_Type.__name__ = "Integer32"
_SecondDataBridgingStatus_Object = MibScalar
secondDataBridgingStatus = _SecondDataBridgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 80),
    _SecondDataBridgingStatus_Type()
)
secondDataBridgingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondDataBridgingStatus.setStatus("current")


class _TransparentClockPort_Type(Integer32):
    """Custom type transparentClockPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aux", 1),
          ("mainPSU", 0),
          ("sFP", 2))
    )


_TransparentClockPort_Type.__name__ = "Integer32"
_TransparentClockPort_Object = MibScalar
transparentClockPort = _TransparentClockPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 6, 81),
    _TransparentClockPort_Type()
)
transparentClockPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transparentClockPort.setStatus("current")
_TDM_ObjectIdentity = ObjectIdentity
tDM = _TDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7)
)


class _TDMInterfaceControl_Type(Integer32):
    """Custom type tDMInterfaceControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("none", 0),
          ("t1", 2))
    )


_TDMInterfaceControl_Type.__name__ = "Integer32"
_TDMInterfaceControl_Object = MibScalar
tDMInterfaceControl = _TDMInterfaceControl_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 1),
    _TDMInterfaceControl_Type()
)
tDMInterfaceControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMInterfaceControl.setStatus("current")


class _TDMInterfaceStatus_Type(Integer32):
    """Custom type tDMInterfaceStatus based on Integer32"""
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
        *(("codeDownloadInProgress", 5),
          ("connectedNotConfigured", 1),
          ("error", 4),
          ("nIDUdetectedonAUXport", 3),
          ("notConnected", 2),
          ("ok", 0))
    )


_TDMInterfaceStatus_Type.__name__ = "Integer32"
_TDMInterfaceStatus_Object = MibScalar
tDMInterfaceStatus = _TDMInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 2),
    _TDMInterfaceStatus_Type()
)
tDMInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMInterfaceStatus.setStatus("current")


class _TDMEnabledChannels_Type(Integer32):
    """Custom type tDMEnabledChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TDMEnabledChannels_Type.__name__ = "Integer32"
_TDMEnabledChannels_Object = MibScalar
tDMEnabledChannels = _TDMEnabledChannels_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 3),
    _TDMEnabledChannels_Type()
)
tDMEnabledChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMEnabledChannels.setStatus("current")


class _TdmTableNumber_Type(Integer32):
    """Custom type tdmTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TdmTableNumber_Type.__name__ = "Integer32"
_TdmTableNumber_Object = MibScalar
tdmTableNumber = _TdmTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 4),
    _TdmTableNumber_Type()
)
tdmTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmTableNumber.setStatus("current")
_TdmTable_Object = MibTable
tdmTable = _TdmTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 5)
)
if mibBuilder.loadTexts:
    tdmTable.setStatus("current")
_TdmTableEntry_Object = MibTableRow
tdmTableEntry = _TdmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 5, 1)
)
tdmTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP650-MIB", "tdmTableIndex"),
)
if mibBuilder.loadTexts:
    tdmTableEntry.setStatus("current")


class _TdmTableIndex_Type(Integer32):
    """Custom type tdmTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TdmTableIndex_Type.__name__ = "Integer32"
_TdmTableIndex_Object = MibTableColumn
tdmTableIndex = _TdmTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 5, 1, 1),
    _TdmTableIndex_Type()
)
tdmTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmTableIndex.setStatus("current")


class _TDMChannelStatus_Type(Integer32):
    """Custom type tDMChannelStatus based on Integer32"""
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
        *(("disabled", 6),
          ("noSignalLocal", 1),
          ("noSignalLocalandRemote", 3),
          ("noSignalLocalandRemoteTiming", 5),
          ("noSignalRemote", 2),
          ("remoteTiming", 4),
          ("up", 0))
    )


_TDMChannelStatus_Type.__name__ = "Integer32"
_TDMChannelStatus_Object = MibTableColumn
tDMChannelStatus = _TDMChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 5, 1, 2),
    _TDMChannelStatus_Type()
)
tDMChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMChannelStatus.setStatus("current")


class _TDMChannelLineCode_Type(Integer32):
    """Custom type tDMChannelLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 0),
          ("b8ZSorHDB3", 1))
    )


_TDMChannelLineCode_Type.__name__ = "Integer32"
_TDMChannelLineCode_Object = MibTableColumn
tDMChannelLineCode = _TDMChannelLineCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 5, 1, 3),
    _TDMChannelLineCode_Type()
)
tDMChannelLineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMChannelLineCode.setStatus("current")


class _TDMChannelCableLength_Type(Integer32):
    """Custom type tDMChannelCableLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("feet133", 0),
          ("feet266", 1),
          ("feet399", 2),
          ("feet533", 3),
          ("feet655", 4))
    )


_TDMChannelCableLength_Type.__name__ = "Integer32"
_TDMChannelCableLength_Object = MibTableColumn
tDMChannelCableLength = _TDMChannelCableLength_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 5, 1, 4),
    _TDMChannelCableLength_Type()
)
tDMChannelCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMChannelCableLength.setStatus("current")


class _TDMChannelLoopback_Type(Integer32):
    """Custom type tDMChannelLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("none", 0),
          ("wireless", 2))
    )


_TDMChannelLoopback_Type.__name__ = "Integer32"
_TDMChannelLoopback_Object = MibTableColumn
tDMChannelLoopback = _TDMChannelLoopback_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 5, 1, 5),
    _TDMChannelLoopback_Type()
)
tDMChannelLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMChannelLoopback.setStatus("current")


class _TDMConfigurationMismatch_Type(Integer32):
    """Custom type tDMConfigurationMismatch based on Integer32"""
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
        *(("enabledchannelsmismatch", 2),
          ("linetypeandenabledchannelsmismatch", 3),
          ("linetypemismatch", 1),
          ("ok", 0))
    )


_TDMConfigurationMismatch_Type.__name__ = "Integer32"
_TDMConfigurationMismatch_Object = MibScalar
tDMConfigurationMismatch = _TDMConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 6),
    _TDMConfigurationMismatch_Type()
)
tDMConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMConfigurationMismatch.setStatus("current")


class _LowestTDMModulationMode_Type(Integer32):
    """Custom type lowestTDMModulationMode based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("mod16qam63percentDual", 16),
          ("mod16qam63percentSingleA", 6),
          ("mod16qam63percentSingleB", 15),
          ("mod16qam87percentDual", 18),
          ("mod16qam87percentSingle", 8),
          ("mod256qam81percentDual", 24),
          ("mod256qam81percentSingle", 14),
          ("mod64qam75percentDual", 20),
          ("mod64qam75percentSingle", 10),
          ("mod64qam92percentDual", 22),
          ("mod64qam92percentSingle", 12),
          ("modAcquisition", 0),
          ("modBpsk63percent", 1),
          ("modQpsk63percentSingle", 2),
          ("modQpsk87percentSingle", 4),
          ("modTransient1", 3),
          ("modTransient10", 23),
          ("modTransient2", 5),
          ("modTransient3", 7),
          ("modTransient4", 9),
          ("modTransient5", 11),
          ("modTransient6", 13),
          ("modTransient7", 17),
          ("modTransient8", 19),
          ("modTransient9", 21))
    )


_LowestTDMModulationMode_Type.__name__ = "Integer32"
_LowestTDMModulationMode_Object = MibScalar
lowestTDMModulationMode = _LowestTDMModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 7, 7),
    _LowestTDMModulationMode_Type()
)
lowestTDMModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowestTDMModulationMode.setStatus("current")
_License_ObjectIdentity = ObjectIdentity
license = _License_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8)
)


class _RegulatoryBand_Type(Integer32):
    """Custom type regulatoryBand based on Integer32"""
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
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("reg100", 100),
          ("reg101", 101),
          ("reg102", 102),
          ("reg103", 103),
          ("reg104", 104),
          ("reg105", 105),
          ("reg1058GHz", 10),
          ("reg106", 106),
          ("reg107", 107),
          ("reg108", 108),
          ("reg109", 109),
          ("reg110", 110),
          ("reg111", 111),
          ("reg112", 112),
          ("reg113", 113),
          ("reg114", 114),
          ("reg115", 115),
          ("reg1158GHz", 11),
          ("reg116", 116),
          ("reg117", 117),
          ("reg118", 118),
          ("reg119", 119),
          ("reg120", 120),
          ("reg121", 121),
          ("reg122", 122),
          ("reg123", 123),
          ("reg124", 124),
          ("reg125", 125),
          ("reg1254GHzFCCUNII2C", 12),
          ("reg126", 126),
          ("reg127", 127),
          ("reg128", 128),
          ("reg129", 129),
          ("reg130", 130),
          ("reg131", 131),
          ("reg132", 132),
          ("reg133", 133),
          ("reg134", 134),
          ("reg135", 135),
          ("reg1354GHz", 13),
          ("reg136", 136),
          ("reg137", 137),
          ("reg138", 138),
          ("reg139", 139),
          ("reg140", 140),
          ("reg141", 141),
          ("reg142", 142),
          ("reg143", 143),
          ("reg144", 144),
          ("reg1449GHzPublicSafety", 14),
          ("reg145", 145),
          ("reg146", 146),
          ("reg147", 147),
          ("reg148", 148),
          ("reg149", 149),
          ("reg15", 15),
          ("reg150", 150),
          ("reg151", 151),
          ("reg152", 152),
          ("reg153", 153),
          ("reg154", 154),
          ("reg155", 155),
          ("reg156", 156),
          ("reg157", 157),
          ("reg158", 158),
          ("reg158GHz", 1),
          ("reg159", 159),
          ("reg160", 160),
          ("reg161", 161),
          ("reg162", 162),
          ("reg163", 163),
          ("reg164", 164),
          ("reg165", 165),
          ("reg1659GHz", 16),
          ("reg166", 166),
          ("reg167", 167),
          ("reg168", 168),
          ("reg169", 169),
          ("reg170", 170),
          ("reg171", 171),
          ("reg172", 172),
          ("reg173", 173),
          ("reg174", 174),
          ("reg175", 175),
          ("reg1759GHz", 17),
          ("reg176", 176),
          ("reg177", 177),
          ("reg178", 178),
          ("reg179", 179),
          ("reg180", 180),
          ("reg181", 181),
          ("reg182", 182),
          ("reg183", 183),
          ("reg184", 184),
          ("reg1849GHzPublicSafety", 18),
          ("reg185", 185),
          ("reg186", 186),
          ("reg187", 187),
          ("reg188", 188),
          ("reg189", 189),
          ("reg190", 190),
          ("reg191", 191),
          ("reg192", 192),
          ("reg193", 193),
          ("reg194", 194),
          ("reg195", 195),
          ("reg1958GHz", 19),
          ("reg196", 196),
          ("reg197", 197),
          ("reg198", 198),
          ("reg199", 199),
          ("reg200", 200),
          ("reg201", 201),
          ("reg202", 202),
          ("reg203", 203),
          ("reg204", 204),
          ("reg205", 205),
          ("reg2054GHz", 20),
          ("reg206", 206),
          ("reg207", 207),
          ("reg208", 208),
          ("reg209", 209),
          ("reg210", 210),
          ("reg211", 211),
          ("reg212", 212),
          ("reg213", 213),
          ("reg214", 214),
          ("reg215", 215),
          ("reg2154GHz", 21),
          ("reg216", 216),
          ("reg217", 217),
          ("reg218", 218),
          ("reg219", 219),
          ("reg220", 220),
          ("reg221", 221),
          ("reg222", 222),
          ("reg223", 223),
          ("reg224", 224),
          ("reg225", 225),
          ("reg2258GHz", 22),
          ("reg226", 226),
          ("reg227", 227),
          ("reg228", 228),
          ("reg229", 229),
          ("reg23", 23),
          ("reg230", 230),
          ("reg231", 231),
          ("reg232", 232),
          ("reg233", 233),
          ("reg234", 234),
          ("reg235", 235),
          ("reg236", 236),
          ("reg237", 237),
          ("reg238", 238),
          ("reg239", 239),
          ("reg240", 240),
          ("reg241", 241),
          ("reg242", 242),
          ("reg243", 243),
          ("reg244", 244),
          ("reg245", 245),
          ("reg2458GHz", 24),
          ("reg246", 246),
          ("reg247", 247),
          ("reg248", 248),
          ("reg249", 249),
          ("reg250", 250),
          ("reg251", 251),
          ("reg252", 252),
          ("reg253", 253),
          ("reg254", 254),
          ("reg255", 255),
          ("reg2558GHzETSI", 25),
          ("reg258GHz", 2),
          ("reg2654GHzETSI", 26),
          ("reg2758GHz", 27),
          ("reg2858GHz", 28),
          ("reg2958GHzUnrestrictedEIRPwithDFSandRTTT", 29),
          ("reg3054GHz", 30),
          ("reg3158GHz", 31),
          ("reg3249GHzLicensed", 32),
          ("reg3349GHzETSIBroadbandDisasterRelief", 33),
          ("reg3458GHz", 34),
          ("reg3558GHzUnrestrictedEIRP", 35),
          ("reg358GHz", 3),
          ("reg3654GHz", 36),
          ("reg3758GHz", 37),
          ("reg3852GHzFCCUNII2A", 38),
          ("reg3951GHzETSIBroadbandDisasterRelief", 39),
          ("reg4054GHz", 40),
          ("reg4154GHz", 41),
          ("reg4254GHz", 42),
          ("reg4354GHz", 43),
          ("reg4458GHz", 44),
          ("reg4558GHz", 45),
          ("reg458GHz", 4),
          ("reg4658GHz", 46),
          ("reg4758GHz", 47),
          ("reg4858GHz", 48),
          ("reg4958GHz", 49),
          ("reg5058GHz", 50),
          ("reg5158GHz", 51),
          ("reg5258GHz", 52),
          ("reg5358GHz", 53),
          ("reg5458GHz", 54),
          ("reg5558GHz", 55),
          ("reg558GHz", 5),
          ("reg5654GHz", 56),
          ("reg5754GHz", 57),
          ("reg5858GHz", 58),
          ("reg5958GHz", 59),
          ("reg6058GHz", 60),
          ("reg6149GHz", 61),
          ("reg6252GHz", 62),
          ("reg6352GHz", 63),
          ("reg6451GHz", 64),
          ("reg6551GHz", 65),
          ("reg658GHz", 6),
          ("reg6651GHz", 66),
          ("reg6752GHz", 67),
          ("reg6852GHz", 68),
          ("reg6952GHz", 69),
          ("reg7052GHz", 70),
          ("reg7152GHz", 71),
          ("reg7252GHz", 72),
          ("reg7352GHz", 73),
          ("reg7452GHz", 74),
          ("reg754GHzUnrestrictedEIRPwithDFS", 7),
          ("reg7552GHz", 75),
          ("reg7652GHz", 76),
          ("reg7752GHz", 77),
          ("reg7849GHz", 78),
          ("reg7954GHz", 79),
          ("reg8049GHz", 80),
          ("reg8147GHz", 81),
          ("reg8247GHz", 82),
          ("reg8352GHz", 83),
          ("reg8451GHzFCCUNII1", 84),
          ("reg854GHzUnrestrictedEIRP", 8),
          ("reg8552GHzFCCUNII12A", 85),
          ("reg8654GHzFCCUNII2A2C", 86),
          ("reg8758GHz", 87),
          ("reg8849GHz", 88),
          ("reg8949GHz", 89),
          ("reg9", 9),
          ("reg9054GHzFCCUNII2CParabolicantenna", 90),
          ("reg9152GHzFCCUNII2AParabolicantenna", 91),
          ("reg9251GHzFCCUNII1Parabolicantenna", 92),
          ("reg9349GHz", 93),
          ("reg94", 94),
          ("reg95", 95),
          ("reg96", 96),
          ("reg97", 97),
          ("reg98", 98),
          ("reg99", 99),
          ("regInvalid", 0))
    )


_RegulatoryBand_Type.__name__ = "Integer32"
_RegulatoryBand_Object = MibScalar
regulatoryBand = _RegulatoryBand_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 1),
    _RegulatoryBand_Type()
)
regulatoryBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regulatoryBand.setStatus("current")


class _ProductVariant_Type(Integer32):
    """Custom type productVariant based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("pTP800", 15),
          ("pTPxx300", 5),
          ("pTPxx400Deprecated1", 1),
          ("pTPxx400Deprecated2", 2),
          ("pTPxx400Full", 0),
          ("pTPxx400Lite", 3),
          ("pTPxx500", 10),
          ("pTPxx500FullDeprecated", 8),
          ("pTPxx500LiteDeprecated", 9),
          ("pTPxx600Full", 12),
          ("pTPxx600Lite", 11),
          ("pTPxx650", 13),
          ("spare1", 4),
          ("spare2", 6),
          ("spare3", 7),
          ("spare6", 14))
    )


_ProductVariant_Type.__name__ = "Integer32"
_ProductVariant_Object = MibScalar
productVariant = _ProductVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 2),
    _ProductVariant_Type()
)
productVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVariant.setStatus("current")


class _ProductName_Type(DisplayString):
    """Custom type productName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ProductName_Type.__name__ = "DisplayString"
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 3),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")


class _FrequencyVariant_Type(Integer32):
    """Custom type frequencyVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("freq4GHz", 1),
          ("freq5GHz", 0))
    )


_FrequencyVariant_Type.__name__ = "Integer32"
_FrequencyVariant_Object = MibScalar
frequencyVariant = _FrequencyVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 5),
    _FrequencyVariant_Type()
)
frequencyVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyVariant.setStatus("current")


class _SNMPv3Enable_Type(Integer32):
    """Custom type sNMPv3Enable based on Integer32"""
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


_SNMPv3Enable_Type.__name__ = "Integer32"
_SNMPv3Enable_Object = MibScalar
sNMPv3Enable = _SNMPv3Enable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 9),
    _SNMPv3Enable_Type()
)
sNMPv3Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPv3Enable.setStatus("current")


class _LicenseVersion_Type(Integer32):
    """Custom type licenseVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_LicenseVersion_Type.__name__ = "Integer32"
_LicenseVersion_Object = MibScalar
licenseVersion = _LicenseVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 12),
    _LicenseVersion_Type()
)
licenseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseVersion.setStatus("current")


class _LicenseUnitSerialNumber_Type(DisplayString):
    """Custom type licenseUnitSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_LicenseUnitSerialNumber_Type.__name__ = "DisplayString"
_LicenseUnitSerialNumber_Object = MibScalar
licenseUnitSerialNumber = _LicenseUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 13),
    _LicenseUnitSerialNumber_Type()
)
licenseUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseUnitSerialNumber.setStatus("current")


class _LicenseIssueNumber_Type(Integer32):
    """Custom type licenseIssueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LicenseIssueNumber_Type.__name__ = "Integer32"
_LicenseIssueNumber_Object = MibScalar
licenseIssueNumber = _LicenseIssueNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 15),
    _LicenseIssueNumber_Type()
)
licenseIssueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseIssueNumber.setStatus("current")


class _LicenseCountry_Type(DisplayString):
    """Custom type licenseCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 103),
    )


_LicenseCountry_Type.__name__ = "DisplayString"
_LicenseCountry_Object = MibScalar
licenseCountry = _LicenseCountry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 16),
    _LicenseCountry_Type()
)
licenseCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseCountry.setStatus("current")


class _LicenseNumberOfRegulatoryBands_Type(Integer32):
    """Custom type licenseNumberOfRegulatoryBands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_LicenseNumberOfRegulatoryBands_Type.__name__ = "Integer32"
_LicenseNumberOfRegulatoryBands_Object = MibScalar
licenseNumberOfRegulatoryBands = _LicenseNumberOfRegulatoryBands_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 17),
    _LicenseNumberOfRegulatoryBands_Type()
)
licenseNumberOfRegulatoryBands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseNumberOfRegulatoryBands.setStatus("current")
_LicenseRegulatoryBandsTable_Object = MibTable
licenseRegulatoryBandsTable = _LicenseRegulatoryBandsTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 18)
)
if mibBuilder.loadTexts:
    licenseRegulatoryBandsTable.setStatus("current")
_LicenseRegulatoryBandsTableEntry_Object = MibTableRow
licenseRegulatoryBandsTableEntry = _LicenseRegulatoryBandsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 18, 1)
)
licenseRegulatoryBandsTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP650-MIB", "licenseRegulatoryBandsTableIndex"),
)
if mibBuilder.loadTexts:
    licenseRegulatoryBandsTableEntry.setStatus("current")


class _LicenseRegulatoryBandsTableIndex_Type(Integer32):
    """Custom type licenseRegulatoryBandsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LicenseRegulatoryBandsTableIndex_Type.__name__ = "Integer32"
_LicenseRegulatoryBandsTableIndex_Object = MibTableColumn
licenseRegulatoryBandsTableIndex = _LicenseRegulatoryBandsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 18, 1, 1),
    _LicenseRegulatoryBandsTableIndex_Type()
)
licenseRegulatoryBandsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseRegulatoryBandsTableIndex.setStatus("current")


class _LicenseRegulatoryBandsList_Type(Integer32):
    """Custom type licenseRegulatoryBandsList based on Integer32"""
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
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("reg100", 100),
          ("reg101", 101),
          ("reg102", 102),
          ("reg103", 103),
          ("reg104", 104),
          ("reg105", 105),
          ("reg1058GHz", 10),
          ("reg106", 106),
          ("reg107", 107),
          ("reg108", 108),
          ("reg109", 109),
          ("reg110", 110),
          ("reg111", 111),
          ("reg112", 112),
          ("reg113", 113),
          ("reg114", 114),
          ("reg115", 115),
          ("reg1158GHz", 11),
          ("reg116", 116),
          ("reg117", 117),
          ("reg118", 118),
          ("reg119", 119),
          ("reg120", 120),
          ("reg121", 121),
          ("reg122", 122),
          ("reg123", 123),
          ("reg124", 124),
          ("reg125", 125),
          ("reg1254GHzFCCUNII2C", 12),
          ("reg126", 126),
          ("reg127", 127),
          ("reg128", 128),
          ("reg129", 129),
          ("reg130", 130),
          ("reg131", 131),
          ("reg132", 132),
          ("reg133", 133),
          ("reg134", 134),
          ("reg135", 135),
          ("reg1354GHz", 13),
          ("reg136", 136),
          ("reg137", 137),
          ("reg138", 138),
          ("reg139", 139),
          ("reg140", 140),
          ("reg141", 141),
          ("reg142", 142),
          ("reg143", 143),
          ("reg144", 144),
          ("reg1449GHzPublicSafety", 14),
          ("reg145", 145),
          ("reg146", 146),
          ("reg147", 147),
          ("reg148", 148),
          ("reg149", 149),
          ("reg15", 15),
          ("reg150", 150),
          ("reg151", 151),
          ("reg152", 152),
          ("reg153", 153),
          ("reg154", 154),
          ("reg155", 155),
          ("reg156", 156),
          ("reg157", 157),
          ("reg158", 158),
          ("reg158GHz", 1),
          ("reg159", 159),
          ("reg160", 160),
          ("reg161", 161),
          ("reg162", 162),
          ("reg163", 163),
          ("reg164", 164),
          ("reg165", 165),
          ("reg1659GHz", 16),
          ("reg166", 166),
          ("reg167", 167),
          ("reg168", 168),
          ("reg169", 169),
          ("reg170", 170),
          ("reg171", 171),
          ("reg172", 172),
          ("reg173", 173),
          ("reg174", 174),
          ("reg175", 175),
          ("reg1759GHz", 17),
          ("reg176", 176),
          ("reg177", 177),
          ("reg178", 178),
          ("reg179", 179),
          ("reg180", 180),
          ("reg181", 181),
          ("reg182", 182),
          ("reg183", 183),
          ("reg184", 184),
          ("reg1849GHzPublicSafety", 18),
          ("reg185", 185),
          ("reg186", 186),
          ("reg187", 187),
          ("reg188", 188),
          ("reg189", 189),
          ("reg190", 190),
          ("reg191", 191),
          ("reg192", 192),
          ("reg193", 193),
          ("reg194", 194),
          ("reg195", 195),
          ("reg1958GHz", 19),
          ("reg196", 196),
          ("reg197", 197),
          ("reg198", 198),
          ("reg199", 199),
          ("reg200", 200),
          ("reg201", 201),
          ("reg202", 202),
          ("reg203", 203),
          ("reg204", 204),
          ("reg205", 205),
          ("reg2054GHz", 20),
          ("reg206", 206),
          ("reg207", 207),
          ("reg208", 208),
          ("reg209", 209),
          ("reg210", 210),
          ("reg211", 211),
          ("reg212", 212),
          ("reg213", 213),
          ("reg214", 214),
          ("reg215", 215),
          ("reg2154GHz", 21),
          ("reg216", 216),
          ("reg217", 217),
          ("reg218", 218),
          ("reg219", 219),
          ("reg220", 220),
          ("reg221", 221),
          ("reg222", 222),
          ("reg223", 223),
          ("reg224", 224),
          ("reg225", 225),
          ("reg2258GHz", 22),
          ("reg226", 226),
          ("reg227", 227),
          ("reg228", 228),
          ("reg229", 229),
          ("reg23", 23),
          ("reg230", 230),
          ("reg231", 231),
          ("reg232", 232),
          ("reg233", 233),
          ("reg234", 234),
          ("reg235", 235),
          ("reg236", 236),
          ("reg237", 237),
          ("reg238", 238),
          ("reg239", 239),
          ("reg240", 240),
          ("reg241", 241),
          ("reg242", 242),
          ("reg243", 243),
          ("reg244", 244),
          ("reg245", 245),
          ("reg2458GHz", 24),
          ("reg246", 246),
          ("reg247", 247),
          ("reg248", 248),
          ("reg249", 249),
          ("reg250", 250),
          ("reg251", 251),
          ("reg252", 252),
          ("reg253", 253),
          ("reg254", 254),
          ("reg255", 255),
          ("reg2558GHzETSI", 25),
          ("reg258GHz", 2),
          ("reg2654GHzETSI", 26),
          ("reg2758GHz", 27),
          ("reg2858GHz", 28),
          ("reg2958GHzUnrestrictedEIRPwithDFSandRTTT", 29),
          ("reg3054GHz", 30),
          ("reg3158GHz", 31),
          ("reg3249GHzLicensed", 32),
          ("reg3349GHzETSIBroadbandDisasterRelief", 33),
          ("reg3458GHz", 34),
          ("reg3558GHzUnrestrictedEIRP", 35),
          ("reg358GHz", 3),
          ("reg3654GHz", 36),
          ("reg3758GHz", 37),
          ("reg3852GHzFCCUNII2A", 38),
          ("reg3951GHzETSIBroadbandDisasterRelief", 39),
          ("reg4054GHz", 40),
          ("reg4154GHz", 41),
          ("reg4254GHz", 42),
          ("reg4354GHz", 43),
          ("reg4458GHz", 44),
          ("reg4558GHz", 45),
          ("reg458GHz", 4),
          ("reg4658GHz", 46),
          ("reg4758GHz", 47),
          ("reg4858GHz", 48),
          ("reg4958GHz", 49),
          ("reg5058GHz", 50),
          ("reg5158GHz", 51),
          ("reg5258GHz", 52),
          ("reg5358GHz", 53),
          ("reg5458GHz", 54),
          ("reg5558GHz", 55),
          ("reg558GHz", 5),
          ("reg5654GHz", 56),
          ("reg5754GHz", 57),
          ("reg5858GHz", 58),
          ("reg5958GHz", 59),
          ("reg6058GHz", 60),
          ("reg6149GHz", 61),
          ("reg6252GHz", 62),
          ("reg6352GHz", 63),
          ("reg6451GHz", 64),
          ("reg6551GHz", 65),
          ("reg658GHz", 6),
          ("reg6651GHz", 66),
          ("reg6752GHz", 67),
          ("reg6852GHz", 68),
          ("reg6952GHz", 69),
          ("reg7052GHz", 70),
          ("reg7152GHz", 71),
          ("reg7252GHz", 72),
          ("reg7352GHz", 73),
          ("reg7452GHz", 74),
          ("reg754GHzUnrestrictedEIRPwithDFS", 7),
          ("reg7552GHz", 75),
          ("reg7652GHz", 76),
          ("reg7752GHz", 77),
          ("reg7849GHz", 78),
          ("reg7954GHz", 79),
          ("reg8049GHz", 80),
          ("reg8147GHz", 81),
          ("reg8247GHz", 82),
          ("reg8352GHz", 83),
          ("reg8451GHzFCCUNII1", 84),
          ("reg854GHzUnrestrictedEIRP", 8),
          ("reg8552GHzFCCUNII12A", 85),
          ("reg8654GHzFCCUNII2A2C", 86),
          ("reg8758GHz", 87),
          ("reg8849GHz", 88),
          ("reg8949GHz", 89),
          ("reg9", 9),
          ("reg9054GHzFCCUNII2CParabolicantenna", 90),
          ("reg9152GHzFCCUNII2AParabolicantenna", 91),
          ("reg9251GHzFCCUNII1Parabolicantenna", 92),
          ("reg9349GHz", 93),
          ("reg94", 94),
          ("reg95", 95),
          ("reg96", 96),
          ("reg97", 97),
          ("reg98", 98),
          ("reg99", 99),
          ("regInvalid", 0))
    )


_LicenseRegulatoryBandsList_Type.__name__ = "Integer32"
_LicenseRegulatoryBandsList_Object = MibTableColumn
licenseRegulatoryBandsList = _LicenseRegulatoryBandsList_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 18, 1, 2),
    _LicenseRegulatoryBandsList_Type()
)
licenseRegulatoryBandsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseRegulatoryBandsList.setStatus("current")


class _LicenseBandwidthCap_Type(Integer32):
    """Custom type licenseBandwidthCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LicenseBandwidthCap_Type.__name__ = "Integer32"
_LicenseBandwidthCap_Object = MibScalar
licenseBandwidthCap = _LicenseBandwidthCap_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 20),
    _LicenseBandwidthCap_Type()
)
licenseBandwidthCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseBandwidthCap.setStatus("current")


class _LicenseEncryption_Type(Integer32):
    """Custom type licenseEncryption based on Integer32"""
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
        *(("aES192bitRijndael", 2),
          ("aES256bitRijndael", 3),
          ("aESRijndael", 1),
          ("none", 0))
    )


_LicenseEncryption_Type.__name__ = "Integer32"
_LicenseEncryption_Object = MibScalar
licenseEncryption = _LicenseEncryption_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 21),
    _LicenseEncryption_Type()
)
licenseEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseEncryption.setStatus("current")


class _LicenseSecurityLevel_Type(Integer32):
    """Custom type licenseSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fIPS", 1),
          ("normal", 0),
          ("uCAPL", 2))
    )


_LicenseSecurityLevel_Type.__name__ = "Integer32"
_LicenseSecurityLevel_Object = MibScalar
licenseSecurityLevel = _LicenseSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 22),
    _LicenseSecurityLevel_Type()
)
licenseSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseSecurityLevel.setStatus("current")


class _LicenseGroupAccess_Type(Integer32):
    """Custom type licenseGroupAccess based on Integer32"""
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


_LicenseGroupAccess_Type.__name__ = "Integer32"
_LicenseGroupAccess_Object = MibScalar
licenseGroupAccess = _LicenseGroupAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 23),
    _LicenseGroupAccess_Type()
)
licenseGroupAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseGroupAccess.setStatus("current")


class _LicenseOOBManagementSupport_Type(Integer32):
    """Custom type licenseOOBManagementSupport based on Integer32"""
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


_LicenseOOBManagementSupport_Type.__name__ = "Integer32"
_LicenseOOBManagementSupport_Object = MibScalar
licenseOOBManagementSupport = _LicenseOOBManagementSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 24),
    _LicenseOOBManagementSupport_Type()
)
licenseOOBManagementSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseOOBManagementSupport.setStatus("current")


class _LicenseSFPPortSupport_Type(Integer32):
    """Custom type licenseSFPPortSupport based on Integer32"""
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


_LicenseSFPPortSupport_Type.__name__ = "Integer32"
_LicenseSFPPortSupport_Object = MibScalar
licenseSFPPortSupport = _LicenseSFPPortSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 25),
    _LicenseSFPPortSupport_Type()
)
licenseSFPPortSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseSFPPortSupport.setStatus("current")


class _LicenseAuxiliaryPortSupport_Type(Integer32):
    """Custom type licenseAuxiliaryPortSupport based on Integer32"""
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


_LicenseAuxiliaryPortSupport_Type.__name__ = "Integer32"
_LicenseAuxiliaryPortSupport_Object = MibScalar
licenseAuxiliaryPortSupport = _LicenseAuxiliaryPortSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 26),
    _LicenseAuxiliaryPortSupport_Type()
)
licenseAuxiliaryPortSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseAuxiliaryPortSupport.setStatus("current")


class _LicenseCapacity_Type(Integer32):
    """Custom type licenseCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 0),
          ("lite", 2),
          ("mid", 1))
    )


_LicenseCapacity_Type.__name__ = "Integer32"
_LicenseCapacity_Object = MibScalar
licenseCapacity = _LicenseCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 27),
    _LicenseCapacity_Type()
)
licenseCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseCapacity.setStatus("current")


class _LicenseMaxNumberOfTDMChannels_Type(Integer32):
    """Custom type licenseMaxNumberOfTDMChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_LicenseMaxNumberOfTDMChannels_Type.__name__ = "Integer32"
_LicenseMaxNumberOfTDMChannels_Object = MibScalar
licenseMaxNumberOfTDMChannels = _LicenseMaxNumberOfTDMChannels_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 28),
    _LicenseMaxNumberOfTDMChannels_Type()
)
licenseMaxNumberOfTDMChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseMaxNumberOfTDMChannels.setStatus("current")


class _LicenseIEEE1588Support_Type(Integer32):
    """Custom type licenseIEEE1588Support based on Integer32"""
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


_LicenseIEEE1588Support_Type.__name__ = "Integer32"
_LicenseIEEE1588Support_Object = MibScalar
licenseIEEE1588Support = _LicenseIEEE1588Support_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 29),
    _LicenseIEEE1588Support_Type()
)
licenseIEEE1588Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseIEEE1588Support.setStatus("current")


class _LicenseSyncESupport_Type(Integer32):
    """Custom type licenseSyncESupport based on Integer32"""
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


_LicenseSyncESupport_Type.__name__ = "Integer32"
_LicenseSyncESupport_Object = MibScalar
licenseSyncESupport = _LicenseSyncESupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 30),
    _LicenseSyncESupport_Type()
)
licenseSyncESupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseSyncESupport.setStatus("current")


class _LicenseIPv6Support_Type(Integer32):
    """Custom type licenseIPv6Support based on Integer32"""
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


_LicenseIPv6Support_Type.__name__ = "Integer32"
_LicenseIPv6Support_Object = MibScalar
licenseIPv6Support = _LicenseIPv6Support_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 31),
    _LicenseIPv6Support_Type()
)
licenseIPv6Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseIPv6Support.setStatus("current")


class _LicenseMinimumFirmwareVersion_Type(DisplayString):
    """Custom type licenseMinimumFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_LicenseMinimumFirmwareVersion_Type.__name__ = "DisplayString"
_LicenseMinimumFirmwareVersion_Object = MibScalar
licenseMinimumFirmwareVersion = _LicenseMinimumFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 32),
    _LicenseMinimumFirmwareVersion_Type()
)
licenseMinimumFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseMinimumFirmwareVersion.setStatus("current")


class _LicenseFullCapabilityTrialStatus_Type(Integer32):
    """Custom type licenseFullCapabilityTrialStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("available", 0),
          ("expired", 3),
          ("inactive", 2),
          ("unavailable", 4))
    )


_LicenseFullCapabilityTrialStatus_Type.__name__ = "Integer32"
_LicenseFullCapabilityTrialStatus_Object = MibScalar
licenseFullCapabilityTrialStatus = _LicenseFullCapabilityTrialStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 33),
    _LicenseFullCapabilityTrialStatus_Type()
)
licenseFullCapabilityTrialStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFullCapabilityTrialStatus.setStatus("current")


class _LicenseRemainingTrialPeriod_Type(Integer32):
    """Custom type licenseRemainingTrialPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_LicenseRemainingTrialPeriod_Type.__name__ = "Integer32"
_LicenseRemainingTrialPeriod_Object = MibScalar
licenseRemainingTrialPeriod = _LicenseRemainingTrialPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 34),
    _LicenseRemainingTrialPeriod_Type()
)
licenseRemainingTrialPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseRemainingTrialPeriod.setStatus("current")


class _LicenseRemainingTrialPeriodAlarm_Type(Integer32):
    """Custom type licenseRemainingTrialPeriodAlarm based on Integer32"""
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
        *(("fullCapabilityTrialExpiringInLessThan1Day", 7),
          ("fullCapabilityTrialExpiringInLessThan2Days", 6),
          ("fullCapabilityTrialExpiringInLessThan3Days", 5),
          ("fullCapabilityTrialExpiringInLessThan4Days", 4),
          ("fullCapabilityTrialExpiringInLessThan5Days", 3),
          ("fullCapabilityTrialExpiringInLessThan6Days", 2),
          ("fullCapabilityTrialExpiringInLessThan7Days", 1),
          ("fullCapabilityTrialHasExpired", 8),
          ("fullCapabilityTrialNotActiveOrMoreThan7DaysRemaining", 0))
    )


_LicenseRemainingTrialPeriodAlarm_Type.__name__ = "Integer32"
_LicenseRemainingTrialPeriodAlarm_Object = MibScalar
licenseRemainingTrialPeriodAlarm = _LicenseRemainingTrialPeriodAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 35),
    _LicenseRemainingTrialPeriodAlarm_Type()
)
licenseRemainingTrialPeriodAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseRemainingTrialPeriodAlarm.setStatus("current")


class _CapacityVariantMismatch_Type(Integer32):
    """Custom type capacityVariantMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mismatchDetected", 1),
          ("noError", 0))
    )


_CapacityVariantMismatch_Type.__name__ = "Integer32"
_CapacityVariantMismatch_Object = MibScalar
capacityVariantMismatch = _CapacityVariantMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 36),
    _CapacityVariantMismatch_Type()
)
capacityVariantMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacityVariantMismatch.setStatus("current")


class _LicenseTDDSyncSupport_Type(Integer32):
    """Custom type licenseTDDSyncSupport based on Integer32"""
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


_LicenseTDDSyncSupport_Type.__name__ = "Integer32"
_LicenseTDDSyncSupport_Object = MibScalar
licenseTDDSyncSupport = _LicenseTDDSyncSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 37),
    _LicenseTDDSyncSupport_Type()
)
licenseTDDSyncSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseTDDSyncSupport.setStatus("current")


class _LicenseMaxLinkRange_Type(Integer32):
    """Custom type licenseMaxLinkRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_LicenseMaxLinkRange_Type.__name__ = "Integer32"
_LicenseMaxLinkRange_Object = MibScalar
licenseMaxLinkRange = _LicenseMaxLinkRange_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 38),
    _LicenseMaxLinkRange_Type()
)
licenseMaxLinkRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseMaxLinkRange.setStatus("current")


class _LicenseTrialPeriod_Type(Integer32):
    """Custom type licenseTrialPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_LicenseTrialPeriod_Type.__name__ = "Integer32"
_LicenseTrialPeriod_Object = MibScalar
licenseTrialPeriod = _LicenseTrialPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 39),
    _LicenseTrialPeriod_Type()
)
licenseTrialPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseTrialPeriod.setStatus("current")


class _LicenseRARSupport_Type(Integer32):
    """Custom type licenseRARSupport based on Integer32"""
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
        *(("dLEP", 2),
          ("disabled", 0),
          ("mAB", 1),
          ("mABandDLEP", 3))
    )


_LicenseRARSupport_Type.__name__ = "Integer32"
_LicenseRARSupport_Object = MibScalar
licenseRARSupport = _LicenseRARSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 8, 40),
    _LicenseRARSupport_Type()
)
licenseRARSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseRARSupport.setStatus("current")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9)
)


class _TargetRange_Type(Integer32):
    """Custom type targetRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_TargetRange_Type.__name__ = "Integer32"
_TargetRange_Object = MibScalar
targetRange = _TargetRange_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 1),
    _TargetRange_Type()
)
targetRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetRange.setStatus("current")


class _RangingMode_Type(Integer32):
    """Custom type rangingMode based on Integer32"""
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
        *(("auto0to100km", 1),
          ("auto0to200km", 2),
          ("auto0to40km", 0),
          ("targetRange", 3))
    )


_RangingMode_Type.__name__ = "Integer32"
_RangingMode_Object = MibScalar
rangingMode = _RangingMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 2),
    _RangingMode_Type()
)
rangingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangingMode.setStatus("current")


class _InstallStatus_Type(Integer32):
    """Custom type installStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("wrongPeer", 1))
    )


_InstallStatus_Type.__name__ = "Integer32"
_InstallStatus_Object = MibScalar
installStatus = _InstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 3),
    _InstallStatus_Type()
)
installStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installStatus.setStatus("current")


class _InstallArmState_Type(Integer32):
    """Custom type installArmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("armed", 1),
          ("disarmed", 0))
    )


_InstallArmState_Type.__name__ = "Integer32"
_InstallArmState_Object = MibScalar
installArmState = _InstallArmState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 4),
    _InstallArmState_Type()
)
installArmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installArmState.setStatus("current")


class _TFTPServerPortNumber_Type(Integer32):
    """Custom type tFTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TFTPServerPortNumber_Type.__name__ = "Integer32"
_TFTPServerPortNumber_Object = MibScalar
tFTPServerPortNumber = _TFTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 6),
    _TFTPServerPortNumber_Type()
)
tFTPServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPServerPortNumber.setStatus("current")


class _TFTPSoftwareUpgradeFileName_Type(DisplayString):
    """Custom type tFTPSoftwareUpgradeFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TFTPSoftwareUpgradeFileName_Type.__name__ = "DisplayString"
_TFTPSoftwareUpgradeFileName_Object = MibScalar
tFTPSoftwareUpgradeFileName = _TFTPSoftwareUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 7),
    _TFTPSoftwareUpgradeFileName_Type()
)
tFTPSoftwareUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeFileName.setStatus("current")
_TFTPStartSoftwareUpgrade_Type = Integer32
_TFTPStartSoftwareUpgrade_Object = MibScalar
tFTPStartSoftwareUpgrade = _TFTPStartSoftwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 8),
    _TFTPStartSoftwareUpgrade_Type()
)
tFTPStartSoftwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPStartSoftwareUpgrade.setStatus("current")


class _TFTPSoftwareUpgradeStatus_Type(Integer32):
    """Custom type tFTPSoftwareUpgradeStatus based on Integer32"""
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
        *(("idle", 0),
          ("upgradefailed", 4),
          ("upgradesuccessfulreboottorunthenewsoftwareimage", 3),
          ("upgradewarning", 5),
          ("uploadinprogress", 1),
          ("uploadsuccessfulprogrammingFLASH", 2))
    )


_TFTPSoftwareUpgradeStatus_Type.__name__ = "Integer32"
_TFTPSoftwareUpgradeStatus_Object = MibScalar
tFTPSoftwareUpgradeStatus = _TFTPSoftwareUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 9),
    _TFTPSoftwareUpgradeStatus_Type()
)
tFTPSoftwareUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeStatus.setStatus("current")


class _TFTPSoftwareUpgradeStatusText_Type(DisplayString):
    """Custom type tFTPSoftwareUpgradeStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TFTPSoftwareUpgradeStatusText_Type.__name__ = "DisplayString"
_TFTPSoftwareUpgradeStatusText_Object = MibScalar
tFTPSoftwareUpgradeStatusText = _TFTPSoftwareUpgradeStatusText_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 10),
    _TFTPSoftwareUpgradeStatusText_Type()
)
tFTPSoftwareUpgradeStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeStatusText.setStatus("current")


class _TFTPSoftwareUpgradeStatusAdditionalText_Type(DisplayString):
    """Custom type tFTPSoftwareUpgradeStatusAdditionalText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TFTPSoftwareUpgradeStatusAdditionalText_Type.__name__ = "DisplayString"
_TFTPSoftwareUpgradeStatusAdditionalText_Object = MibScalar
tFTPSoftwareUpgradeStatusAdditionalText = _TFTPSoftwareUpgradeStatusAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 11),
    _TFTPSoftwareUpgradeStatusAdditionalText_Type()
)
tFTPSoftwareUpgradeStatusAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeStatusAdditionalText.setStatus("current")


class _HTTPAccessEnabled_Type(Integer32):
    """Custom type hTTPAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_HTTPAccessEnabled_Type.__name__ = "Integer32"
_HTTPAccessEnabled_Object = MibScalar
hTTPAccessEnabled = _HTTPAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 12),
    _HTTPAccessEnabled_Type()
)
hTTPAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPAccessEnabled.setStatus("current")


class _TelnetAccessEnabled_Type(Integer32):
    """Custom type telnetAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TelnetAccessEnabled_Type.__name__ = "Integer32"
_TelnetAccessEnabled_Object = MibScalar
telnetAccessEnabled = _TelnetAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 13),
    _TelnetAccessEnabled_Type()
)
telnetAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetAccessEnabled.setStatus("current")


class _HTTPPortNumber_Type(Integer32):
    """Custom type hTTPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HTTPPortNumber_Type.__name__ = "Integer32"
_HTTPPortNumber_Object = MibScalar
hTTPPortNumber = _HTTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 14),
    _HTTPPortNumber_Type()
)
hTTPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPPortNumber.setStatus("current")


class _HTTPSPortNumber_Type(Integer32):
    """Custom type hTTPSPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HTTPSPortNumber_Type.__name__ = "Integer32"
_HTTPSPortNumber_Object = MibScalar
hTTPSPortNumber = _HTTPSPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 15),
    _HTTPSPortNumber_Type()
)
hTTPSPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPSPortNumber.setStatus("current")


class _TelnetPortNumber_Type(Integer32):
    """Custom type telnetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TelnetPortNumber_Type.__name__ = "Integer32"
_TelnetPortNumber_Object = MibScalar
telnetPortNumber = _TelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 16),
    _TelnetPortNumber_Type()
)
telnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortNumber.setStatus("current")


class _HTTPSAccessEnabled_Type(Integer32):
    """Custom type hTTPSAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_HTTPSAccessEnabled_Type.__name__ = "Integer32"
_HTTPSAccessEnabled_Object = MibScalar
hTTPSAccessEnabled = _HTTPSAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 17),
    _HTTPSAccessEnabled_Type()
)
hTTPSAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPSAccessEnabled.setStatus("current")


class _TFTPServerInternetAddressType_Type(Integer32):
    """Custom type tFTPServerInternetAddressType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dns", 16),
          ("ipv4", 1),
          ("ipv4z", 3),
          ("ipv6", 2),
          ("ipv6z", 4),
          ("unknown", 0),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8))
    )


_TFTPServerInternetAddressType_Type.__name__ = "Integer32"
_TFTPServerInternetAddressType_Object = MibScalar
tFTPServerInternetAddressType = _TFTPServerInternetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 18),
    _TFTPServerInternetAddressType_Type()
)
tFTPServerInternetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPServerInternetAddressType.setStatus("current")
_TFTPServerInternetAddress_Type = InetAddress
_TFTPServerInternetAddress_Object = MibScalar
tFTPServerInternetAddress = _TFTPServerInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 19),
    _TFTPServerInternetAddress_Type()
)
tFTPServerInternetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPServerInternetAddress.setStatus("current")


class _LowestDataModulationMode_Type(Integer32):
    """Custom type lowestDataModulationMode based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("mod16qam63percentDual", 16),
          ("mod16qam63percentSingleA", 6),
          ("mod16qam63percentSingleB", 15),
          ("mod16qam87percentDual", 18),
          ("mod16qam87percentSingle", 8),
          ("mod256qam81percentDual", 24),
          ("mod256qam81percentSingle", 14),
          ("mod64qam75percentDual", 20),
          ("mod64qam75percentSingle", 10),
          ("mod64qam92percentDual", 22),
          ("mod64qam92percentSingle", 12),
          ("modAcquisition", 0),
          ("modBpsk63percent", 1),
          ("modQpsk63percentSingle", 2),
          ("modQpsk87percentSingle", 4),
          ("modTransient1", 3),
          ("modTransient10", 23),
          ("modTransient2", 5),
          ("modTransient3", 7),
          ("modTransient4", 9),
          ("modTransient5", 11),
          ("modTransient6", 13),
          ("modTransient7", 17),
          ("modTransient8", 19),
          ("modTransient9", 21))
    )


_LowestDataModulationMode_Type.__name__ = "Integer32"
_LowestDataModulationMode_Object = MibScalar
lowestDataModulationMode = _LowestDataModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 20),
    _LowestDataModulationMode_Type()
)
lowestDataModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowestDataModulationMode.setStatus("current")


class _LowestSecondDataModulationMode_Type(Integer32):
    """Custom type lowestSecondDataModulationMode based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("mod16qam63percentDual", 16),
          ("mod16qam63percentSingleA", 6),
          ("mod16qam63percentSingleB", 15),
          ("mod16qam87percentDual", 18),
          ("mod16qam87percentSingle", 8),
          ("mod256qam81percentDual", 24),
          ("mod256qam81percentSingle", 14),
          ("mod64qam75percentDual", 20),
          ("mod64qam75percentSingle", 10),
          ("mod64qam92percentDual", 22),
          ("mod64qam92percentSingle", 12),
          ("modAcquisition", 0),
          ("modBpsk63percent", 1),
          ("modQpsk63percentSingle", 2),
          ("modQpsk87percentSingle", 4),
          ("modTransient1", 3),
          ("modTransient10", 23),
          ("modTransient2", 5),
          ("modTransient3", 7),
          ("modTransient4", 9),
          ("modTransient5", 11),
          ("modTransient6", 13),
          ("modTransient7", 17),
          ("modTransient8", 19),
          ("modTransient9", 21))
    )


_LowestSecondDataModulationMode_Type.__name__ = "Integer32"
_LowestSecondDataModulationMode_Object = MibScalar
lowestSecondDataModulationMode = _LowestSecondDataModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 9, 21),
    _LowestSecondDataModulationMode_Type()
)
lowestSecondDataModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowestSecondDataModulationMode.setStatus("current")
_PhyControl_ObjectIdentity = ObjectIdentity
phyControl = _PhyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 10)
)


class _LinkSymmetry_Type(Integer32):
    """Custom type linkSymmetry based on Integer32"""
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
        *(("symmetry1to1", 2),
          ("symmetry1to2", 3),
          ("symmetry1to3", 5),
          ("symmetry1to5", 7),
          ("symmetry2to1", 1),
          ("symmetry3to1", 4),
          ("symmetry5to1", 6),
          ("symmetryAdaptive", 0))
    )


_LinkSymmetry_Type.__name__ = "Integer32"
_LinkSymmetry_Object = MibScalar
linkSymmetry = _LinkSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 10, 1),
    _LinkSymmetry_Type()
)
linkSymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSymmetry.setStatus("current")


class _UserConfiguredMaxModulationMode_Type(Integer32):
    """Custom type userConfiguredMaxModulationMode based on Integer32"""
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
        *(("mod16qam63percent", 3),
          ("mod16qam87percent", 4),
          ("mod256qam81percent", 7),
          ("mod64qam75percent", 5),
          ("mod64qam92percent", 6),
          ("modBpsk63percent", 0),
          ("modQpsk63percent", 1),
          ("modQpsk87percent", 2))
    )


_UserConfiguredMaxModulationMode_Type.__name__ = "Integer32"
_UserConfiguredMaxModulationMode_Object = MibScalar
userConfiguredMaxModulationMode = _UserConfiguredMaxModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 10, 2),
    _UserConfiguredMaxModulationMode_Type()
)
userConfiguredMaxModulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userConfiguredMaxModulationMode.setStatus("current")


class _LinkModeOptimization_Type(Integer32):
    """Custom type linkModeOptimization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("iPTraffic", 0),
          ("tDMTraffic", 1))
    )


_LinkModeOptimization_Type.__name__ = "Integer32"
_LinkModeOptimization_Object = MibScalar
linkModeOptimization = _LinkModeOptimization_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 10, 3),
    _LinkModeOptimization_Type()
)
linkModeOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkModeOptimization.setStatus("current")


class _TxColorCode_Type(Integer32):
    """Custom type txColorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("a", 0),
          ("b", 1),
          ("c", 2),
          ("d", 3),
          ("e", 4))
    )


_TxColorCode_Type.__name__ = "Integer32"
_TxColorCode_Object = MibScalar
txColorCode = _TxColorCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 10, 4),
    _TxColorCode_Type()
)
txColorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txColorCode.setStatus("current")


class _RxColorCode_Type(Integer32):
    """Custom type rxColorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("a", 0),
          ("b", 1),
          ("c", 2),
          ("d", 3),
          ("e", 4))
    )


_RxColorCode_Type.__name__ = "Integer32"
_RxColorCode_Object = MibScalar
rxColorCode = _RxColorCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 10, 5),
    _RxColorCode_Type()
)
rxColorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxColorCode.setStatus("current")


class _RemoteMaximumTransmitPower_Type(Integer32):
    """Custom type remoteMaximumTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 30),
    )


_RemoteMaximumTransmitPower_Type.__name__ = "Integer32"
_RemoteMaximumTransmitPower_Object = MibScalar
remoteMaximumTransmitPower = _RemoteMaximumTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 10, 6),
    _RemoteMaximumTransmitPower_Type()
)
remoteMaximumTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMaximumTransmitPower.setStatus("current")
_PhyStatus_ObjectIdentity = ObjectIdentity
phyStatus = _PhyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12)
)


class _LinkLoss_Type(Integer32):
    """Custom type linkLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_LinkLoss_Type.__name__ = "Integer32"
_LinkLoss_Object = MibScalar
linkLoss = _LinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 1),
    _LinkLoss_Type()
)
linkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLoss.setStatus("current")
_ReceivePower_Type = Integer32
_ReceivePower_Object = MibScalar
receivePower = _ReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 2),
    _ReceivePower_Type()
)
receivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivePower.setStatus("current")
_VectorError_Type = Integer32
_VectorError_Object = MibScalar
vectorError = _VectorError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 3),
    _VectorError_Type()
)
vectorError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vectorError.setStatus("current")
_TransmitPower_Type = Integer32
_TransmitPower_Object = MibScalar
transmitPower = _TransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 4),
    _TransmitPower_Type()
)
transmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitPower.setStatus("current")


class _ReceiveChannel_Type(Integer32):
    """Custom type receiveChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ReceiveChannel_Type.__name__ = "Integer32"
_ReceiveChannel_Object = MibScalar
receiveChannel = _ReceiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 5),
    _ReceiveChannel_Type()
)
receiveChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveChannel.setStatus("current")


class _TransmitChannel_Type(Integer32):
    """Custom type transmitChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TransmitChannel_Type.__name__ = "Integer32"
_TransmitChannel_Object = MibScalar
transmitChannel = _TransmitChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 6),
    _TransmitChannel_Type()
)
transmitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitChannel.setStatus("current")


class _ReceiveFreqMHz_Type(Integer32):
    """Custom type receiveFreqMHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6050),
    )


_ReceiveFreqMHz_Type.__name__ = "Integer32"
_ReceiveFreqMHz_Object = MibScalar
receiveFreqMHz = _ReceiveFreqMHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 7),
    _ReceiveFreqMHz_Type()
)
receiveFreqMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveFreqMHz.setStatus("current")


class _TransmitFreqMHz_Type(Integer32):
    """Custom type transmitFreqMHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6050),
    )


_TransmitFreqMHz_Type.__name__ = "Integer32"
_TransmitFreqMHz_Object = MibScalar
transmitFreqMHz = _TransmitFreqMHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 8),
    _TransmitFreqMHz_Type()
)
transmitFreqMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitFreqMHz.setStatus("current")
_SignalStrengthRatio_Type = Integer32
_SignalStrengthRatio_Object = MibScalar
signalStrengthRatio = _SignalStrengthRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 9),
    _SignalStrengthRatio_Type()
)
signalStrengthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalStrengthRatio.setStatus("current")


class _ReceiveFreqKHz_Type(Integer32):
    """Custom type receiveFreqKHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6050000),
    )


_ReceiveFreqKHz_Type.__name__ = "Integer32"
_ReceiveFreqKHz_Object = MibScalar
receiveFreqKHz = _ReceiveFreqKHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 10),
    _ReceiveFreqKHz_Type()
)
receiveFreqKHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveFreqKHz.setStatus("current")


class _TransmitFreqKHz_Type(Integer32):
    """Custom type transmitFreqKHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6050000),
    )


_TransmitFreqKHz_Type.__name__ = "Integer32"
_TransmitFreqKHz_Object = MibScalar
transmitFreqKHz = _TransmitFreqKHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 11),
    _TransmitFreqKHz_Type()
)
transmitFreqKHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitFreqKHz.setStatus("current")
_RawReceivePower_Type = Integer32
_RawReceivePower_Object = MibScalar
rawReceivePower = _RawReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 12),
    _RawReceivePower_Type()
)
rawReceivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawReceivePower.setStatus("current")
_Range_Type = Integer32
_Range_Object = MibScalar
range = _Range_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 13),
    _Range_Type()
)
range.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range.setStatus("current")


class _ReceiveModulationMode_Type(Integer32):
    """Custom type receiveModulationMode based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("mod16qam63percentDual", 16),
          ("mod16qam63percentSingleA", 6),
          ("mod16qam63percentSingleB", 15),
          ("mod16qam87percentDual", 18),
          ("mod16qam87percentSingle", 8),
          ("mod256qam81percentDual", 24),
          ("mod256qam81percentSingle", 14),
          ("mod64qam75percentDual", 20),
          ("mod64qam75percentSingle", 10),
          ("mod64qam92percentDual", 22),
          ("mod64qam92percentSingle", 12),
          ("modAcquisition", 0),
          ("modBpsk63percent", 1),
          ("modQpsk63percentSingle", 2),
          ("modQpsk87percentSingle", 4),
          ("modTransient1", 3),
          ("modTransient10", 23),
          ("modTransient2", 5),
          ("modTransient3", 7),
          ("modTransient4", 9),
          ("modTransient5", 11),
          ("modTransient6", 13),
          ("modTransient7", 17),
          ("modTransient8", 19),
          ("modTransient9", 21))
    )


_ReceiveModulationMode_Type.__name__ = "Integer32"
_ReceiveModulationMode_Object = MibScalar
receiveModulationMode = _ReceiveModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 14),
    _ReceiveModulationMode_Type()
)
receiveModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveModulationMode.setStatus("current")


class _TransmitModulationMode_Type(Integer32):
    """Custom type transmitModulationMode based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("mod16qam63percentDual", 16),
          ("mod16qam63percentSingleA", 6),
          ("mod16qam63percentSingleB", 15),
          ("mod16qam87percentDual", 18),
          ("mod16qam87percentSingle", 8),
          ("mod256qam81percentDual", 24),
          ("mod256qam81percentSingle", 14),
          ("mod64qam75percentDual", 20),
          ("mod64qam75percentSingle", 10),
          ("mod64qam92percentDual", 22),
          ("mod64qam92percentSingle", 12),
          ("modAcquisition", 0),
          ("modBpsk63percent", 1),
          ("modQpsk63percentSingle", 2),
          ("modQpsk87percentSingle", 4),
          ("modTransient1", 3),
          ("modTransient10", 23),
          ("modTransient2", 5),
          ("modTransient3", 7),
          ("modTransient4", 9),
          ("modTransient5", 11),
          ("modTransient6", 13),
          ("modTransient7", 17),
          ("modTransient8", 19),
          ("modTransient9", 21))
    )


_TransmitModulationMode_Type.__name__ = "Integer32"
_TransmitModulationMode_Object = MibScalar
transmitModulationMode = _TransmitModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 15),
    _TransmitModulationMode_Type()
)
transmitModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitModulationMode.setStatus("current")


class _SearchState_Type(Integer32):
    """Custom type searchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acquiring", 2),
          ("registering", 0),
          ("searching", 1))
    )


_SearchState_Type.__name__ = "Integer32"
_SearchState_Object = MibScalar
searchState = _SearchState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 12, 16),
    _SearchState_Type()
)
searchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    searchState.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13)
)


class _UnitOutOfCalibration_Type(Integer32):
    """Custom type unitOutOfCalibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bandwidthvariantunsupportedPAsShutdown", 3),
          ("calibrated", 0),
          ("invalidCalibration", 2),
          ("outOfCalibrationPAsShutdown", 4),
          ("partialCalibration", 1))
    )


_UnitOutOfCalibration_Type.__name__ = "Integer32"
_UnitOutOfCalibration_Object = MibScalar
unitOutOfCalibration = _UnitOutOfCalibration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 1),
    _UnitOutOfCalibration_Type()
)
unitOutOfCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitOutOfCalibration.setStatus("current")


class _IncompatibleRegulatoryBands_Type(Integer32):
    """Custom type incompatibleRegulatoryBands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("regIncompatibleLicenseKeys", 1),
          ("regOK", 0))
    )


_IncompatibleRegulatoryBands_Type.__name__ = "Integer32"
_IncompatibleRegulatoryBands_Object = MibScalar
incompatibleRegulatoryBands = _IncompatibleRegulatoryBands_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 4),
    _IncompatibleRegulatoryBands_Type()
)
incompatibleRegulatoryBands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incompatibleRegulatoryBands.setStatus("current")


class _NoWirelessChannelAvailable_Type(Integer32):
    """Custom type noWirelessChannelAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noWirelessChannelAvailable", 1),
          ("ok", 0))
    )


_NoWirelessChannelAvailable_Type.__name__ = "Integer32"
_NoWirelessChannelAvailable_Object = MibScalar
noWirelessChannelAvailable = _NoWirelessChannelAvailable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 5),
    _NoWirelessChannelAvailable_Type()
)
noWirelessChannelAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noWirelessChannelAvailable.setStatus("current")


class _WirelessLinkDisabledWarning_Type(Integer32):
    """Custom type wirelessLinkDisabledWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabledBySNMPifAdminStatus", 1),
          ("ok", 0))
    )


_WirelessLinkDisabledWarning_Type.__name__ = "Integer32"
_WirelessLinkDisabledWarning_Object = MibScalar
wirelessLinkDisabledWarning = _WirelessLinkDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 6),
    _WirelessLinkDisabledWarning_Type()
)
wirelessLinkDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkDisabledWarning.setStatus("current")


class _MainPSUPortDisabledWarning_Type(Integer32):
    """Custom type mainPSUPortDisabledWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabledBySNMPifAdminStatus", 1),
          ("ok", 0))
    )


_MainPSUPortDisabledWarning_Type.__name__ = "Integer32"
_MainPSUPortDisabledWarning_Object = MibScalar
mainPSUPortDisabledWarning = _MainPSUPortDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 7),
    _MainPSUPortDisabledWarning_Type()
)
mainPSUPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortDisabledWarning.setStatus("current")


class _SFPError_Type(Integer32):
    """Custom type sFPError based on Integer32"""
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
        *(("fiberLinkNotEstablishedAndLOSDetected", 3),
          ("fiberLinkNotEstablishedButLOSNotDetected", 2),
          ("installedSFPNotLicensed", 1),
          ("installedSFPNotSupported", 4),
          ("ok", 0),
          ("sFPInitializationFailed", 5))
    )


_SFPError_Type.__name__ = "Integer32"
_SFPError_Object = MibScalar
sFPError = _SFPError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 8),
    _SFPError_Type()
)
sFPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPError.setStatus("current")


class _MainPSUPortConfigurationMismatch_Type(Integer32):
    """Custom type mainPSUPortConfigurationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mismatchDetected", 1),
          ("noError", 0))
    )


_MainPSUPortConfigurationMismatch_Type.__name__ = "Integer32"
_MainPSUPortConfigurationMismatch_Object = MibScalar
mainPSUPortConfigurationMismatch = _MainPSUPortConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 9),
    _MainPSUPortConfigurationMismatch_Type()
)
mainPSUPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortConfigurationMismatch.setStatus("current")


class _IncompatibleMasterAndSlave_Type(Integer32):
    """Custom type incompatibleMasterAndSlave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("differentSoftwareVersionsRunning", 2),
          ("incompatibleProductVariants", 1),
          ("ok", 0))
    )


_IncompatibleMasterAndSlave_Type.__name__ = "Integer32"
_IncompatibleMasterAndSlave_Object = MibScalar
incompatibleMasterAndSlave = _IncompatibleMasterAndSlave_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 10),
    _IncompatibleMasterAndSlave_Type()
)
incompatibleMasterAndSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incompatibleMasterAndSlave.setStatus("current")


class _TDDSynchronizationStatus_Type(Integer32):
    """Custom type tDDSynchronizationStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("acquiringLock", 8),
          ("clusterTimingMaster", 7),
          ("holdover", 1),
          ("holdoverNoGPSSyncIn", 2),
          ("inactive", 9),
          ("initialising", 6),
          ("locked", 0),
          ("notSynchronized", 3),
          ("notSynchronizedNoGPSSyncIn", 4),
          ("pTPSYNCNotConnected", 5))
    )


_TDDSynchronizationStatus_Type.__name__ = "Integer32"
_TDDSynchronizationStatus_Object = MibScalar
tDDSynchronizationStatus = _TDDSynchronizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 11),
    _TDDSynchronizationStatus_Type()
)
tDDSynchronizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDDSynchronizationStatus.setStatus("current")


class _AuxPortDisabledWarning_Type(Integer32):
    """Custom type auxPortDisabledWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabledBySNMPifAdminStatus", 1),
          ("ok", 0))
    )


_AuxPortDisabledWarning_Type.__name__ = "Integer32"
_AuxPortDisabledWarning_Object = MibScalar
auxPortDisabledWarning = _AuxPortDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 12),
    _AuxPortDisabledWarning_Type()
)
auxPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortDisabledWarning.setStatus("current")


class _TDDSynchronizationAlarm_Type(Integer32):
    """Custom type tDDSynchronizationAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("referenceSignalLost", 2),
          ("synchronizationLost", 1))
    )


_TDDSynchronizationAlarm_Type.__name__ = "Integer32"
_TDDSynchronizationAlarm_Object = MibScalar
tDDSynchronizationAlarm = _TDDSynchronizationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 13),
    _TDDSynchronizationAlarm_Type()
)
tDDSynchronizationAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDDSynchronizationAlarm.setStatus("current")


class _LinkModeOptimizationMismatch_Type(Integer32):
    """Custom type linkModeOptimizationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("linkModeOptimizationMismatch", 1),
          ("ok", 0))
    )


_LinkModeOptimizationMismatch_Type.__name__ = "Integer32"
_LinkModeOptimizationMismatch_Object = MibScalar
linkModeOptimizationMismatch = _LinkModeOptimizationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 14),
    _LinkModeOptimizationMismatch_Type()
)
linkModeOptimizationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkModeOptimizationMismatch.setStatus("current")


class _AuxPortConfigurationMismatch_Type(Integer32):
    """Custom type auxPortConfigurationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mismatchDetected", 1),
          ("noError", 0))
    )


_AuxPortConfigurationMismatch_Type.__name__ = "Integer32"
_AuxPortConfigurationMismatch_Object = MibScalar
auxPortConfigurationMismatch = _AuxPortConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 15),
    _AuxPortConfigurationMismatch_Type()
)
auxPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortConfigurationMismatch.setStatus("current")


class _SecureModeAlarm_Type(Integer32):
    """Custom type secureModeAlarm based on Integer32"""
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
        *(("secureModeIsActive", 0),
          ("secureModeIsConfiguredButNotActive", 2),
          ("secureModeIsNotConfigured", 1),
          ("secureModeIsNotSupported", 3))
    )


_SecureModeAlarm_Type.__name__ = "Integer32"
_SecureModeAlarm_Object = MibScalar
secureModeAlarm = _SecureModeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 16),
    _SecureModeAlarm_Type()
)
secureModeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureModeAlarm.setStatus("current")


class _DataBridgingStatusAlarm_Type(Integer32):
    """Custom type dataBridgingStatusAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridgingDisabled", 1),
          ("bridgingEnabled", 0))
    )


_DataBridgingStatusAlarm_Type.__name__ = "Integer32"
_DataBridgingStatusAlarm_Object = MibScalar
dataBridgingStatusAlarm = _DataBridgingStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 17),
    _DataBridgingStatusAlarm_Type()
)
dataBridgingStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataBridgingStatusAlarm.setStatus("current")


class _SFPPortDisabledWarning_Type(Integer32):
    """Custom type sFPPortDisabledWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabledBySNMPifAdminStatus", 1),
          ("ok", 0))
    )


_SFPPortDisabledWarning_Type.__name__ = "Integer32"
_SFPPortDisabledWarning_Object = MibScalar
sFPPortDisabledWarning = _SFPPortDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 18),
    _SFPPortDisabledWarning_Type()
)
sFPPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortDisabledWarning.setStatus("current")


class _SFPPortConfigurationMismatch_Type(Integer32):
    """Custom type sFPPortConfigurationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mismatchDetected", 1),
          ("noError", 0))
    )


_SFPPortConfigurationMismatch_Type.__name__ = "Integer32"
_SFPPortConfigurationMismatch_Object = MibScalar
sFPPortConfigurationMismatch = _SFPPortConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 19),
    _SFPPortConfigurationMismatch_Type()
)
sFPPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortConfigurationMismatch.setStatus("current")


class _MaxLinkRangeExceeded_Type(Integer32):
    """Custom type maxLinkRangeExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("maxLinkRangeExceeded", 1),
          ("maxLinkRangeOK", 0))
    )


_MaxLinkRangeExceeded_Type.__name__ = "Integer32"
_MaxLinkRangeExceeded_Object = MibScalar
maxLinkRangeExceeded = _MaxLinkRangeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 20),
    _MaxLinkRangeExceeded_Type()
)
maxLinkRangeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLinkRangeExceeded.setStatus("current")


class _NIDULanPortDisabledWarning_Type(Integer32):
    """Custom type nIDULanPortDisabledWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabledBySNMPifAdminStatus", 1),
          ("ok", 0))
    )


_NIDULanPortDisabledWarning_Type.__name__ = "Integer32"
_NIDULanPortDisabledWarning_Object = MibScalar
nIDULanPortDisabledWarning = _NIDULanPortDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 21),
    _NIDULanPortDisabledWarning_Type()
)
nIDULanPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortDisabledWarning.setStatus("current")


class _NIDULanPortConfigurationMismatch_Type(Integer32):
    """Custom type nIDULanPortConfigurationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mismatchDetected", 1),
          ("noError", 0))
    )


_NIDULanPortConfigurationMismatch_Type.__name__ = "Integer32"
_NIDULanPortConfigurationMismatch_Object = MibScalar
nIDULanPortConfigurationMismatch = _NIDULanPortConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 22),
    _NIDULanPortConfigurationMismatch_Type()
)
nIDULanPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortConfigurationMismatch.setStatus("current")


class _PortAllocationMismatch_Type(Integer32):
    """Custom type portAllocationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mismatchinOutofBandRemoteManagementService", 2),
          ("mismatchinSecondDataService", 1),
          ("portAllocationOK", 0))
    )


_PortAllocationMismatch_Type.__name__ = "Integer32"
_PortAllocationMismatch_Object = MibScalar
portAllocationMismatch = _PortAllocationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 23),
    _PortAllocationMismatch_Type()
)
portAllocationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAllocationMismatch.setStatus("current")


class _SecondDataBridgingStatusAlarm_Type(Integer32):
    """Custom type secondDataBridgingStatusAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridgingDisabled", 1),
          ("bridgingEnabled", 0))
    )


_SecondDataBridgingStatusAlarm_Type.__name__ = "Integer32"
_SecondDataBridgingStatusAlarm_Object = MibScalar
secondDataBridgingStatusAlarm = _SecondDataBridgingStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 24),
    _SecondDataBridgingStatusAlarm_Type()
)
secondDataBridgingStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondDataBridgingStatusAlarm.setStatus("current")


class _TransparentClockSourcePortAlarm_Type(Integer32):
    """Custom type transparentClockSourcePortAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalidTransparentClockSourcePort", 1),
          ("ok", 0))
    )


_TransparentClockSourcePortAlarm_Type.__name__ = "Integer32"
_TransparentClockSourcePortAlarm_Object = MibScalar
transparentClockSourcePortAlarm = _TransparentClockSourcePortAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 13, 25),
    _TransparentClockSourcePortAlarm_Type()
)
transparentClockSourcePortAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transparentClockSourcePortAlarm.setStatus("current")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 15)
)


class _SMTPEmailAlert_Type(Integer32):
    """Custom type sMTPEmailAlert based on Integer32"""
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


_SMTPEmailAlert_Type.__name__ = "Integer32"
_SMTPEmailAlert_Object = MibScalar
sMTPEmailAlert = _SMTPEmailAlert_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 15, 1),
    _SMTPEmailAlert_Type()
)
sMTPEmailAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPEmailAlert.setStatus("current")


class _SMTPServerPortNumber_Type(Integer32):
    """Custom type sMTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SMTPServerPortNumber_Type.__name__ = "Integer32"
_SMTPServerPortNumber_Object = MibScalar
sMTPServerPortNumber = _SMTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 15, 3),
    _SMTPServerPortNumber_Type()
)
sMTPServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPServerPortNumber.setStatus("current")


class _SMTPSourceEmailAddress_Type(DisplayString):
    """Custom type sMTPSourceEmailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SMTPSourceEmailAddress_Type.__name__ = "DisplayString"
_SMTPSourceEmailAddress_Object = MibScalar
sMTPSourceEmailAddress = _SMTPSourceEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 15, 4),
    _SMTPSourceEmailAddress_Type()
)
sMTPSourceEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPSourceEmailAddress.setStatus("current")


class _SMTPDestinationEmailAddress_Type(DisplayString):
    """Custom type sMTPDestinationEmailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SMTPDestinationEmailAddress_Type.__name__ = "DisplayString"
_SMTPDestinationEmailAddress_Object = MibScalar
sMTPDestinationEmailAddress = _SMTPDestinationEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 15, 5),
    _SMTPDestinationEmailAddress_Type()
)
sMTPDestinationEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPDestinationEmailAddress.setStatus("current")


class _SMTPEnabledMessages_Type(Bits):
    """Custom type sMTPEnabledMessages based on Bits"""
    namedValues = NamedValues(
        *(("auxPortUpDown", 2),
          ("channelChange", 6),
          ("dFSImpulseInterference", 5),
          ("enabledDiagnosticAlarms", 4),
          ("mainPSUPortUpDown", 3),
          ("nIDULanPortUpDown", 0),
          ("sFPPortUpDown", 1),
          ("wirelessLinkUpDown", 7))
    )

_SMTPEnabledMessages_Type.__name__ = "Bits"
_SMTPEnabledMessages_Object = MibScalar
sMTPEnabledMessages = _SMTPEnabledMessages_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 15, 6),
    _SMTPEnabledMessages_Type()
)
sMTPEnabledMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPEnabledMessages.setStatus("current")


class _SMTPServerInternetAddressType_Type(Integer32):
    """Custom type sMTPServerInternetAddressType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dns", 16),
          ("ipv4", 1),
          ("ipv4z", 3),
          ("ipv6", 2),
          ("ipv6z", 4),
          ("unknown", 0),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8))
    )


_SMTPServerInternetAddressType_Type.__name__ = "Integer32"
_SMTPServerInternetAddressType_Object = MibScalar
sMTPServerInternetAddressType = _SMTPServerInternetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 15, 7),
    _SMTPServerInternetAddressType_Type()
)
sMTPServerInternetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sMTPServerInternetAddressType.setStatus("current")
_SMTPServerInternetAddress_Type = InetAddress
_SMTPServerInternetAddress_Object = MibScalar
sMTPServerInternetAddress = _SMTPServerInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 15, 8),
    _SMTPServerInternetAddress_Type()
)
sMTPServerInternetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPServerInternetAddress.setStatus("current")
_SnmpControl_ObjectIdentity = ObjectIdentity
snmpControl = _SnmpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16)
)


class _SNMPPortNumber_Type(Integer32):
    """Custom type sNMPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SNMPPortNumber_Type.__name__ = "Integer32"
_SNMPPortNumber_Object = MibScalar
sNMPPortNumber = _SNMPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 1),
    _SNMPPortNumber_Type()
)
sNMPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPPortNumber.setStatus("current")


class _SNMPCommunityString_Type(DisplayString):
    """Custom type sNMPCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SNMPCommunityString_Type.__name__ = "DisplayString"
_SNMPCommunityString_Object = MibScalar
sNMPCommunityString = _SNMPCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 2),
    _SNMPCommunityString_Type()
)
sNMPCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPCommunityString.setStatus("current")


class _SNMPTrapTableNumber_Type(Integer32):
    """Custom type sNMPTrapTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_SNMPTrapTableNumber_Type.__name__ = "Integer32"
_SNMPTrapTableNumber_Object = MibScalar
sNMPTrapTableNumber = _SNMPTrapTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 3),
    _SNMPTrapTableNumber_Type()
)
sNMPTrapTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapTableNumber.setStatus("current")
_SNMPTrapTable_Object = MibTable
sNMPTrapTable = _SNMPTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 4)
)
if mibBuilder.loadTexts:
    sNMPTrapTable.setStatus("current")
_SNMPTrapTableEntry_Object = MibTableRow
sNMPTrapTableEntry = _SNMPTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 4, 1)
)
sNMPTrapTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP650-MIB", "sNMPTrapTableIndex"),
)
if mibBuilder.loadTexts:
    sNMPTrapTableEntry.setStatus("current")


class _SNMPTrapTableIndex_Type(Integer32):
    """Custom type sNMPTrapTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SNMPTrapTableIndex_Type.__name__ = "Integer32"
_SNMPTrapTableIndex_Object = MibTableColumn
sNMPTrapTableIndex = _SNMPTrapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 4, 1, 1),
    _SNMPTrapTableIndex_Type()
)
sNMPTrapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sNMPTrapTableIndex.setStatus("current")


class _SNMPTrapPortNumber_Type(Integer32):
    """Custom type sNMPTrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SNMPTrapPortNumber_Type.__name__ = "Integer32"
_SNMPTrapPortNumber_Object = MibTableColumn
sNMPTrapPortNumber = _SNMPTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 4, 1, 3),
    _SNMPTrapPortNumber_Type()
)
sNMPTrapPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapPortNumber.setStatus("current")


class _SNMPTrapInternetAddressType_Type(Integer32):
    """Custom type sNMPTrapInternetAddressType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dns", 16),
          ("ipv4", 1),
          ("ipv4z", 3),
          ("ipv6", 2),
          ("ipv6z", 4),
          ("unknown", 0),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8))
    )


_SNMPTrapInternetAddressType_Type.__name__ = "Integer32"
_SNMPTrapInternetAddressType_Object = MibTableColumn
sNMPTrapInternetAddressType = _SNMPTrapInternetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 4, 1, 4),
    _SNMPTrapInternetAddressType_Type()
)
sNMPTrapInternetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapInternetAddressType.setStatus("current")
_SNMPTrapInternetAddress_Type = InetAddress
_SNMPTrapInternetAddress_Object = MibTableColumn
sNMPTrapInternetAddress = _SNMPTrapInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 4, 1, 5),
    _SNMPTrapInternetAddress_Type()
)
sNMPTrapInternetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapInternetAddress.setStatus("current")


class _SNMPTrapReceiverEnabled_Type(Integer32):
    """Custom type sNMPTrapReceiverEnabled based on Integer32"""
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


_SNMPTrapReceiverEnabled_Type.__name__ = "Integer32"
_SNMPTrapReceiverEnabled_Object = MibTableColumn
sNMPTrapReceiverEnabled = _SNMPTrapReceiverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 4, 1, 6),
    _SNMPTrapReceiverEnabled_Type()
)
sNMPTrapReceiverEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapReceiverEnabled.setStatus("current")


class _SNMPTrapVersion_Type(Integer32):
    """Custom type sNMPTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1))
    )


_SNMPTrapVersion_Type.__name__ = "Integer32"
_SNMPTrapVersion_Object = MibScalar
sNMPTrapVersion = _SNMPTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 5),
    _SNMPTrapVersion_Type()
)
sNMPTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapVersion.setStatus("current")


class _SNMPEnabledTraps_Type(Bits):
    """Custom type sNMPEnabledTraps based on Bits"""
    namedValues = NamedValues(
        *(("authenticationFailure", 2),
          ("auxPortUpDown", 0),
          ("channelChange", 5),
          ("coldStart", 7),
          ("dFSImpulseInterference", 4),
          ("enabledDiagnosticAlarms", 3),
          ("mainPSUPortUpDown", 1),
          ("nIDULanPortUpDown", 14),
          ("sFPPortUpDown", 15),
          ("wirelessLinkUpDown", 6))
    )

_SNMPEnabledTraps_Type.__name__ = "Bits"
_SNMPEnabledTraps_Object = MibScalar
sNMPEnabledTraps = _SNMPEnabledTraps_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 6),
    _SNMPEnabledTraps_Type()
)
sNMPEnabledTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPEnabledTraps.setStatus("current")


class _EnabledDiagnosticAlarms_Type(Bits):
    """Custom type enabledDiagnosticAlarms based on Bits"""
    namedValues = NamedValues(
        *(("capacityVariantMismatch", 19),
          ("dataBridgingStatus", 21),
          ("incompatibleMasterAndSlave", 1),
          ("incompatibleRegulatoryBands", 2),
          ("installArmState", 5),
          ("installStatus", 6),
          ("linkModeOptimizationMismatch", 11),
          ("maximumLinkRangeExceeded", 3),
          ("noWirelessChannelAvailable", 15),
          ("portState", 0),
          ("regulatoryBand", 7),
          ("remainingFullCapacityTrialTime", 20),
          ("sNTPSynchronizationFailed", 14),
          ("syslogClientDisabledWarning", 23),
          ("syslogDisabledWarning", 10),
          ("syslogLocalNearlyFull", 9),
          ("syslogLocalWrapped", 8),
          ("tDDSynchronizationAlarm", 12),
          ("tDMAlarms", 18),
          ("unitOutOfCalibration", 4),
          ("unknown18", 22),
          ("wirelessLinkDisabledWarning", 13))
    )

_EnabledDiagnosticAlarms_Type.__name__ = "Bits"
_EnabledDiagnosticAlarms_Object = MibScalar
enabledDiagnosticAlarms = _EnabledDiagnosticAlarms_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 7),
    _EnabledDiagnosticAlarms_Type()
)
enabledDiagnosticAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enabledDiagnosticAlarms.setStatus("current")


class _SNMPSendAllTrapsAtStartup_Type(Integer32):
    """Custom type sNMPSendAllTrapsAtStartup based on Integer32"""
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


_SNMPSendAllTrapsAtStartup_Type.__name__ = "Integer32"
_SNMPSendAllTrapsAtStartup_Object = MibScalar
sNMPSendAllTrapsAtStartup = _SNMPSendAllTrapsAtStartup_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 16, 8),
    _SNMPSendAllTrapsAtStartup_Type()
)
sNMPSendAllTrapsAtStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPSendAllTrapsAtStartup.setStatus("current")
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17)
)


class _SNTPState_Type(Integer32):
    """Custom type sNTPState based on Integer32"""
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


_SNTPState_Type.__name__ = "Integer32"
_SNTPState_Object = MibScalar
sNTPState = _SNTPState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 1),
    _SNTPState_Type()
)
sNTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPState.setStatus("current")


class _SNTPPollInterval_Type(Integer32):
    """Custom type sNTPPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 43200),
    )


_SNTPPollInterval_Type.__name__ = "Integer32"
_SNTPPollInterval_Object = MibScalar
sNTPPollInterval = _SNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 4),
    _SNTPPollInterval_Type()
)
sNTPPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPPollInterval.setStatus("current")


class _SNTPSync_Type(Integer32):
    """Custom type sNTPSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("noSync", 0))
    )


_SNTPSync_Type.__name__ = "Integer32"
_SNTPSync_Object = MibScalar
sNTPSync = _SNTPSync_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 5),
    _SNTPSync_Type()
)
sNTPSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPSync.setStatus("current")
_SNTPLastSync_Type = Integer32
_SNTPLastSync_Object = MibScalar
sNTPLastSync = _SNTPLastSync_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 6),
    _SNTPLastSync_Type()
)
sNTPLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPLastSync.setStatus("current")
_SystemClock_Type = Integer32
_SystemClock_Object = MibScalar
systemClock = _SystemClock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 7),
    _SystemClock_Type()
)
systemClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemClock.setStatus("current")


class _TimeZone_Type(Integer32):
    """Custom type timeZone based on Integer32"""
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
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50)
        )
    )
    namedValues = NamedValues(
        *(("gmtMinus0030", 23),
          ("gmtMinus0100", 22),
          ("gmtMinus0130", 21),
          ("gmtMinus0200", 20),
          ("gmtMinus0230", 19),
          ("gmtMinus0300", 18),
          ("gmtMinus0330", 17),
          ("gmtMinus0400", 16),
          ("gmtMinus0430", 15),
          ("gmtMinus0500", 14),
          ("gmtMinus0530", 13),
          ("gmtMinus0600", 12),
          ("gmtMinus0630", 11),
          ("gmtMinus0700", 10),
          ("gmtMinus0730", 9),
          ("gmtMinus0800", 8),
          ("gmtMinus0830", 7),
          ("gmtMinus0900", 6),
          ("gmtMinus0930", 5),
          ("gmtMinus1000", 4),
          ("gmtMinus1030", 3),
          ("gmtMinus1100", 2),
          ("gmtMinus1130", 1),
          ("gmtMinus1200", 0),
          ("gmtPlus0030", 25),
          ("gmtPlus0100", 26),
          ("gmtPlus0130", 27),
          ("gmtPlus0200", 28),
          ("gmtPlus0230", 29),
          ("gmtPlus0300", 30),
          ("gmtPlus0330", 31),
          ("gmtPlus0400", 32),
          ("gmtPlus0430", 33),
          ("gmtPlus0500", 34),
          ("gmtPlus0530", 35),
          ("gmtPlus0600", 36),
          ("gmtPlus0630", 37),
          ("gmtPlus0700", 38),
          ("gmtPlus0730", 39),
          ("gmtPlus0800", 40),
          ("gmtPlus0830", 41),
          ("gmtPlus0900", 42),
          ("gmtPlus0930", 43),
          ("gmtPlus1000", 44),
          ("gmtPlus1030", 45),
          ("gmtPlus1100", 46),
          ("gmtPlus1130", 47),
          ("gmtPlus1200", 48),
          ("gmtPlus1230", 49),
          ("gmtPlus1300", 50),
          ("gmtZero", 24))
    )


_TimeZone_Type.__name__ = "Integer32"
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 8),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")


class _DaylightSaving_Type(Integer32):
    """Custom type daylightSaving based on Integer32"""
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


_DaylightSaving_Type.__name__ = "Integer32"
_DaylightSaving_Object = MibScalar
daylightSaving = _DaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 9),
    _DaylightSaving_Type()
)
daylightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSaving.setStatus("current")


class _SNTPPrimaryServer_Type(Integer32):
    """Custom type sNTPPrimaryServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("server1", 0),
          ("server2", 1))
    )


_SNTPPrimaryServer_Type.__name__ = "Integer32"
_SNTPPrimaryServer_Object = MibScalar
sNTPPrimaryServer = _SNTPPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 10),
    _SNTPPrimaryServer_Type()
)
sNTPPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPPrimaryServer.setStatus("current")


class _SNTPPrimaryServerDeadTime_Type(Integer32):
    """Custom type sNTPPrimaryServerDeadTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SNTPPrimaryServerDeadTime_Type.__name__ = "Integer32"
_SNTPPrimaryServerDeadTime_Object = MibScalar
sNTPPrimaryServerDeadTime = _SNTPPrimaryServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 11),
    _SNTPPrimaryServerDeadTime_Type()
)
sNTPPrimaryServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPPrimaryServerDeadTime.setStatus("current")


class _SNTPServerRetries_Type(Integer32):
    """Custom type sNTPServerRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SNTPServerRetries_Type.__name__ = "Integer32"
_SNTPServerRetries_Object = MibScalar
sNTPServerRetries = _SNTPServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 12),
    _SNTPServerRetries_Type()
)
sNTPServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerRetries.setStatus("current")


class _SNTPServerTimeout_Type(Integer32):
    """Custom type sNTPServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SNTPServerTimeout_Type.__name__ = "Integer32"
_SNTPServerTimeout_Object = MibScalar
sNTPServerTimeout = _SNTPServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 13),
    _SNTPServerTimeout_Type()
)
sNTPServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerTimeout.setStatus("current")


class _SNTPServerTableNumber_Type(Integer32):
    """Custom type sNTPServerTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_SNTPServerTableNumber_Type.__name__ = "Integer32"
_SNTPServerTableNumber_Object = MibScalar
sNTPServerTableNumber = _SNTPServerTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 14),
    _SNTPServerTableNumber_Type()
)
sNTPServerTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerTableNumber.setStatus("current")
_SNTPServerTable_Object = MibTable
sNTPServerTable = _SNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 15)
)
if mibBuilder.loadTexts:
    sNTPServerTable.setStatus("current")
_SNTPServerTableEntry_Object = MibTableRow
sNTPServerTableEntry = _SNTPServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 15, 1)
)
sNTPServerTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP650-MIB", "sNTPServerTableIndex"),
)
if mibBuilder.loadTexts:
    sNTPServerTableEntry.setStatus("current")


class _SNTPServerTableIndex_Type(Integer32):
    """Custom type sNTPServerTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SNTPServerTableIndex_Type.__name__ = "Integer32"
_SNTPServerTableIndex_Object = MibTableColumn
sNTPServerTableIndex = _SNTPServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 15, 1, 1),
    _SNTPServerTableIndex_Type()
)
sNTPServerTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sNTPServerTableIndex.setStatus("current")


class _SNTPServerPortNumber_Type(Integer32):
    """Custom type sNTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SNTPServerPortNumber_Type.__name__ = "Integer32"
_SNTPServerPortNumber_Object = MibTableColumn
sNTPServerPortNumber = _SNTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 15, 1, 3),
    _SNTPServerPortNumber_Type()
)
sNTPServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerPortNumber.setStatus("current")


class _SNTPServerStatus_Type(DisplayString):
    """Custom type sNTPServerStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SNTPServerStatus_Type.__name__ = "DisplayString"
_SNTPServerStatus_Object = MibTableColumn
sNTPServerStatus = _SNTPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 15, 1, 4),
    _SNTPServerStatus_Type()
)
sNTPServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerStatus.setStatus("current")


class _SNTPServerInternetAddressType_Type(Integer32):
    """Custom type sNTPServerInternetAddressType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dns", 16),
          ("ipv4", 1),
          ("ipv4z", 3),
          ("ipv6", 2),
          ("ipv6z", 4),
          ("unknown", 0),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8))
    )


_SNTPServerInternetAddressType_Type.__name__ = "Integer32"
_SNTPServerInternetAddressType_Object = MibTableColumn
sNTPServerInternetAddressType = _SNTPServerInternetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 15, 1, 5),
    _SNTPServerInternetAddressType_Type()
)
sNTPServerInternetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerInternetAddressType.setStatus("current")
_SNTPServerInternetAddress_Type = InetAddress
_SNTPServerInternetAddress_Object = MibTableColumn
sNTPServerInternetAddress = _SNTPServerInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 17, 15, 1, 6),
    _SNTPServerInternetAddress_Type()
)
sNTPServerInternetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerInternetAddress.setStatus("current")
_Reset_ObjectIdentity = ObjectIdentity
reset = _Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 18)
)


class _SystemReset_Type(Integer32):
    """Custom type systemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("consoleReboot", 1),
          ("running", 0))
    )


_SystemReset_Type.__name__ = "Integer32"
_SystemReset_Object = MibScalar
systemReset = _SystemReset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 18, 1),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("current")
_Versions_ObjectIdentity = ObjectIdentity
versions = _Versions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 19)
)


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 19, 1),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")


class _HardwareVersion_Type(DisplayString):
    """Custom type hardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HardwareVersion_Type.__name__ = "DisplayString"
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 19, 2),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")


class _SecondarySoftwareVersion_Type(DisplayString):
    """Custom type secondarySoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SecondarySoftwareVersion_Type.__name__ = "DisplayString"
_SecondarySoftwareVersion_Object = MibScalar
secondarySoftwareVersion = _SecondarySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 19, 3),
    _SecondarySoftwareVersion_Type()
)
secondarySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondarySoftwareVersion.setStatus("current")


class _BootVersion_Type(DisplayString):
    """Custom type bootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BootVersion_Type.__name__ = "DisplayString"
_BootVersion_Object = MibScalar
bootVersion = _BootVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 19, 4),
    _BootVersion_Type()
)
bootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersion.setStatus("current")
_PubStats_ObjectIdentity = ObjectIdentity
pubStats = _PubStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 20)
)
_ReceiveDataRate_Type = Integer32
_ReceiveDataRate_Object = MibScalar
receiveDataRate = _ReceiveDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 20, 1),
    _ReceiveDataRate_Type()
)
receiveDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveDataRate.setStatus("current")
_TransmitDataRate_Type = Integer32
_TransmitDataRate_Object = MibScalar
transmitDataRate = _TransmitDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 20, 2),
    _TransmitDataRate_Type()
)
transmitDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitDataRate.setStatus("current")
_AggregateDataRate_Type = Integer32
_AggregateDataRate_Object = MibScalar
aggregateDataRate = _AggregateDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 20, 3),
    _AggregateDataRate_Type()
)
aggregateDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregateDataRate.setStatus("current")


class _WirelessLinkAvailability_Type(Integer32):
    """Custom type wirelessLinkAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_WirelessLinkAvailability_Type.__name__ = "Integer32"
_WirelessLinkAvailability_Object = MibScalar
wirelessLinkAvailability = _WirelessLinkAvailability_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 20, 4),
    _WirelessLinkAvailability_Type()
)
wirelessLinkAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkAvailability.setStatus("current")


class _WirelessLinkStatus_Type(Integer32):
    """Custom type wirelessLinkStatus based on Integer32"""
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
        *(("acquiring", 3),
          ("initialising", 5),
          ("radarCAC", 4),
          ("registering", 1),
          ("searching", 2),
          ("up", 0))
    )


_WirelessLinkStatus_Type.__name__ = "Integer32"
_WirelessLinkStatus_Object = MibScalar
wirelessLinkStatus = _WirelessLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 20, 5),
    _WirelessLinkStatus_Type()
)
wirelessLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatus.setStatus("current")
_ByteErrorRatio_Type = Integer32
_ByteErrorRatio_Object = MibScalar
byteErrorRatio = _ByteErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 20, 6),
    _ByteErrorRatio_Type()
)
byteErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    byteErrorRatio.setStatus("current")


class _ReceiveModulationModeDetail_Type(Integer32):
    """Custom type receiveModulationModeDetail based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("limitedByTheWirelessConditions", 8),
          ("restrictedBecauseChannelChangeIsInProgress", 5),
          ("restrictedBecauseFullCapabilityTrialLicenseExpired", 9),
          ("restrictedBecauseInstallationIsArmed", 2),
          ("restrictedBecauseOfByteErrorsOnTheWirelessLink", 3),
          ("restrictedBecauseTheLinkParametersAreUpdating", 4),
          ("restrictedDueToTheLowEthernetLinkSpeed", 6),
          ("runningAtMaximumReceiveMode", 0),
          ("runningAtMaximumReceiveModeForChannelBandwidth", 7),
          ("runningAtUserConfiguredMaxModulationMode", 1))
    )


_ReceiveModulationModeDetail_Type.__name__ = "Integer32"
_ReceiveModulationModeDetail_Object = MibScalar
receiveModulationModeDetail = _ReceiveModulationModeDetail_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 20, 7),
    _ReceiveModulationModeDetail_Type()
)
receiveModulationModeDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveModulationModeDetail.setStatus("current")


class _DataBridgingAvailability_Type(Integer32):
    """Custom type dataBridgingAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_DataBridgingAvailability_Type.__name__ = "Integer32"
_DataBridgingAvailability_Object = MibScalar
dataBridgingAvailability = _DataBridgingAvailability_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 20, 8),
    _DataBridgingAvailability_Type()
)
dataBridgingAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataBridgingAvailability.setStatus("current")
_Encryption_ObjectIdentity = ObjectIdentity
encryption = _Encryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 22)
)


class _EncryptionAlgorithm_Type(Integer32):
    """Custom type encryptionAlgorithm based on Integer32"""
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
        *(("aES192bitRijndael", 2),
          ("aES256bitRijndael", 3),
          ("aESRijndael", 1),
          ("none", 0))
    )


_EncryptionAlgorithm_Type.__name__ = "Integer32"
_EncryptionAlgorithm_Object = MibScalar
encryptionAlgorithm = _EncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 22, 1),
    _EncryptionAlgorithm_Type()
)
encryptionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionAlgorithm.setStatus("current")
_TDDControl_ObjectIdentity = ObjectIdentity
tDDControl = _TDDControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 23)
)


class _TDDSynchronizationMode_Type(Integer32):
    """Custom type tDDSynchronizationMode based on Integer32"""
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


_TDDSynchronizationMode_Type.__name__ = "Integer32"
_TDDSynchronizationMode_Object = MibScalar
tDDSynchronizationMode = _TDDSynchronizationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 23, 1),
    _TDDSynchronizationMode_Type()
)
tDDSynchronizationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDDSynchronizationMode.setStatus("current")
_SyslogControl_ObjectIdentity = ObjectIdentity
syslogControl = _SyslogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 24)
)


class _SyslogClient_Type(Integer32):
    """Custom type syslogClient based on Integer32"""
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


_SyslogClient_Type.__name__ = "Integer32"
_SyslogClient_Object = MibScalar
syslogClient = _SyslogClient_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 24, 1),
    _SyslogClient_Type()
)
syslogClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogClient.setStatus("current")


class _SyslogState_Type(Integer32):
    """Custom type syslogState based on Integer32"""
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


_SyslogState_Type.__name__ = "Integer32"
_SyslogState_Object = MibScalar
syslogState = _SyslogState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 24, 2),
    _SyslogState_Type()
)
syslogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogState.setStatus("current")
_AAAControl_ObjectIdentity = ObjectIdentity
aAAControl = _AAAControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 25)
)


class _UserTableNumber_Type(Integer32):
    """Custom type userTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_UserTableNumber_Type.__name__ = "Integer32"
_UserTableNumber_Object = MibScalar
userTableNumber = _UserTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 25, 1),
    _UserTableNumber_Type()
)
userTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userTableNumber.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 25, 2)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserTableEntry_Object = MibTableRow
userTableEntry = _UserTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 25, 2, 1)
)
userTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP650-MIB", "userTableIndex"),
)
if mibBuilder.loadTexts:
    userTableEntry.setStatus("current")


class _UserTableIndex_Type(Integer32):
    """Custom type userTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_UserTableIndex_Type.__name__ = "Integer32"
_UserTableIndex_Object = MibTableColumn
userTableIndex = _UserTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 25, 2, 1, 1),
    _UserTableIndex_Type()
)
userTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userTableIndex.setStatus("current")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 67),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 25, 2, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserRole_Type(Integer32):
    """Custom type userRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 0),
          ("securityOfficer", 2),
          ("systemAdministrator", 1))
    )


_UserRole_Type.__name__ = "Integer32"
_UserRole_Object = MibTableColumn
userRole = _UserRole_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 25, 2, 1, 3),
    _UserRole_Type()
)
userRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userRole.setStatus("current")


class _UserEnabled_Type(Integer32):
    """Custom type userEnabled based on Integer32"""
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


_UserEnabled_Type.__name__ = "Integer32"
_UserEnabled_Object = MibTableColumn
userEnabled = _UserEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 25, 2, 1, 4),
    _UserEnabled_Type()
)
userEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userEnabled.setStatus("current")


class _UserPassword_Type(DisplayString):
    """Custom type userPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 67),
    )


_UserPassword_Type.__name__ = "DisplayString"
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 25, 2, 1, 5),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")
_RouterProtocols_ObjectIdentity = ObjectIdentity
routerProtocols = _RouterProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26)
)


class _MicrowaveAdaptiveBandwidth_Type(Integer32):
    """Custom type microwaveAdaptiveBandwidth based on Integer32"""
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


_MicrowaveAdaptiveBandwidth_Type.__name__ = "Integer32"
_MicrowaveAdaptiveBandwidth_Object = MibScalar
microwaveAdaptiveBandwidth = _MicrowaveAdaptiveBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26, 1),
    _MicrowaveAdaptiveBandwidth_Type()
)
microwaveAdaptiveBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    microwaveAdaptiveBandwidth.setStatus("current")


class _MABNominalModulationMode_Type(Integer32):
    """Custom type mABNominalModulationMode based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("mod16qam63percentDual", 16),
          ("mod16qam63percentSingleA", 6),
          ("mod16qam63percentSingleB", 15),
          ("mod16qam87percentDual", 18),
          ("mod16qam87percentSingle", 8),
          ("mod256qam81percentDual", 24),
          ("mod256qam81percentSingle", 14),
          ("mod64qam75percentDual", 20),
          ("mod64qam75percentSingle", 10),
          ("mod64qam92percentDual", 22),
          ("mod64qam92percentSingle", 12),
          ("modAcquisition", 0),
          ("modBpsk63percent", 1),
          ("modQpsk63percentSingle", 2),
          ("modQpsk87percentSingle", 4),
          ("modTransient1", 3),
          ("modTransient10", 23),
          ("modTransient2", 5),
          ("modTransient3", 7),
          ("modTransient4", 9),
          ("modTransient5", 11),
          ("modTransient6", 13),
          ("modTransient7", 17),
          ("modTransient8", 19),
          ("modTransient9", 21))
    )


_MABNominalModulationMode_Type.__name__ = "Integer32"
_MABNominalModulationMode_Object = MibScalar
mABNominalModulationMode = _MABNominalModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26, 2),
    _MABNominalModulationMode_Type()
)
mABNominalModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABNominalModulationMode.setStatus("current")


class _MABTransmissionInterval_Type(Integer32):
    """Custom type mABTransmissionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transmissionInterval10s", 1),
          ("transmissionInterval1s", 0),
          ("transmissionInterval60s", 2))
    )


_MABTransmissionInterval_Type.__name__ = "Integer32"
_MABTransmissionInterval_Object = MibScalar
mABTransmissionInterval = _MABTransmissionInterval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26, 3),
    _MABTransmissionInterval_Type()
)
mABTransmissionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABTransmissionInterval.setStatus("current")


class _MABHoldoffPeriod_Type(Integer32):
    """Custom type mABHoldoffPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_MABHoldoffPeriod_Type.__name__ = "Integer32"
_MABHoldoffPeriod_Object = MibScalar
mABHoldoffPeriod = _MABHoldoffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26, 4),
    _MABHoldoffPeriod_Type()
)
mABHoldoffPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABHoldoffPeriod.setStatus("current")


class _MABMaintenanceLevel_Type(Integer32):
    """Custom type mABMaintenanceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MABMaintenanceLevel_Type.__name__ = "Integer32"
_MABMaintenanceLevel_Object = MibScalar
mABMaintenanceLevel = _MABMaintenanceLevel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26, 5),
    _MABMaintenanceLevel_Type()
)
mABMaintenanceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABMaintenanceLevel.setStatus("current")


class _UseVLANForMABProtocol_Type(Integer32):
    """Custom type useVLANForMABProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("iEEE8021QTaggedCTagType8100", 1),
          ("noVLANTagging", 0))
    )


_UseVLANForMABProtocol_Type.__name__ = "Integer32"
_UseVLANForMABProtocol_Object = MibScalar
useVLANForMABProtocol = _UseVLANForMABProtocol_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26, 6),
    _UseVLANForMABProtocol_Type()
)
useVLANForMABProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useVLANForMABProtocol.setStatus("current")


class _MABProtocolVID_Type(Integer32):
    """Custom type mABProtocolVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MABProtocolVID_Type.__name__ = "Integer32"
_MABProtocolVID_Object = MibScalar
mABProtocolVID = _MABProtocolVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26, 7),
    _MABProtocolVID_Type()
)
mABProtocolVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABProtocolVID.setStatus("current")


class _MABProtocolVLANPriority_Type(Integer32):
    """Custom type mABProtocolVLANPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MABProtocolVLANPriority_Type.__name__ = "Integer32"
_MABProtocolVLANPriority_Object = MibScalar
mABProtocolVLANPriority = _MABProtocolVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26, 8),
    _MABProtocolVLANPriority_Type()
)
mABProtocolVLANPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABProtocolVLANPriority.setStatus("current")


class _MABState_Type(Integer32):
    """Custom type mABState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 1),
          ("normal", 0))
    )


_MABState_Type.__name__ = "Integer32"
_MABState_Object = MibScalar
mABState = _MABState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26, 9),
    _MABState_Type()
)
mABState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABState.setStatus("current")


class _MABNominalTransmitCapacity_Type(Integer32):
    """Custom type mABNominalTransmitCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MABNominalTransmitCapacity_Type.__name__ = "Integer32"
_MABNominalTransmitCapacity_Object = MibScalar
mABNominalTransmitCapacity = _MABNominalTransmitCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26, 10),
    _MABNominalTransmitCapacity_Type()
)
mABNominalTransmitCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABNominalTransmitCapacity.setStatus("current")


class _MABCurrentTransmitCapacity_Type(Integer32):
    """Custom type mABCurrentTransmitCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MABCurrentTransmitCapacity_Type.__name__ = "Integer32"
_MABCurrentTransmitCapacity_Object = MibScalar
mABCurrentTransmitCapacity = _MABCurrentTransmitCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 26, 11),
    _MABCurrentTransmitCapacity_Type()
)
mABCurrentTransmitCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABCurrentTransmitCapacity.setStatus("current")
_CableDiagnostics_ObjectIdentity = ObjectIdentity
cableDiagnostics = _CableDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27)
)


class _CableDiagnosticsPorts_Type(Bits):
    """Custom type cableDiagnosticsPorts based on Bits"""
    namedValues = NamedValues(
        *(("auxPort", 6),
          ("mainPSUPort", 7))
    )

_CableDiagnosticsPorts_Type.__name__ = "Bits"
_CableDiagnosticsPorts_Object = MibScalar
cableDiagnosticsPorts = _CableDiagnosticsPorts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 1),
    _CableDiagnosticsPorts_Type()
)
cableDiagnosticsPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableDiagnosticsPorts.setStatus("current")


class _CableDiagnosticsControl_Type(Integer32):
    """Custom type cableDiagnosticsControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("startTest", 0),
          ("testInProgress", 1))
    )


_CableDiagnosticsControl_Type.__name__ = "Integer32"
_CableDiagnosticsControl_Object = MibScalar
cableDiagnosticsControl = _CableDiagnosticsControl_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 2),
    _CableDiagnosticsControl_Type()
)
cableDiagnosticsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableDiagnosticsControl.setStatus("current")


class _CableDiagnosticsWarning_Type(Integer32):
    """Custom type cableDiagnosticsWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("testInProgress", 1))
    )


_CableDiagnosticsWarning_Type.__name__ = "Integer32"
_CableDiagnosticsWarning_Object = MibScalar
cableDiagnosticsWarning = _CableDiagnosticsWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 3),
    _CableDiagnosticsWarning_Type()
)
cableDiagnosticsWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagnosticsWarning.setStatus("current")


class _CableDiagnosticsResultTableNumber_Type(Integer32):
    """Custom type cableDiagnosticsResultTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CableDiagnosticsResultTableNumber_Type.__name__ = "Integer32"
_CableDiagnosticsResultTableNumber_Object = MibScalar
cableDiagnosticsResultTableNumber = _CableDiagnosticsResultTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 4),
    _CableDiagnosticsResultTableNumber_Type()
)
cableDiagnosticsResultTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagnosticsResultTableNumber.setStatus("current")
_CableDiagnosticsResultTable_Object = MibTable
cableDiagnosticsResultTable = _CableDiagnosticsResultTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5)
)
if mibBuilder.loadTexts:
    cableDiagnosticsResultTable.setStatus("current")
_CableDiagnosticsResultTableEntry_Object = MibTableRow
cableDiagnosticsResultTableEntry = _CableDiagnosticsResultTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5, 1)
)
cableDiagnosticsResultTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP650-MIB", "cableDiagnosticsResultTableIndex"),
)
if mibBuilder.loadTexts:
    cableDiagnosticsResultTableEntry.setStatus("current")


class _CableDiagnosticsResultTableIndex_Type(Integer32):
    """Custom type cableDiagnosticsResultTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CableDiagnosticsResultTableIndex_Type.__name__ = "Integer32"
_CableDiagnosticsResultTableIndex_Object = MibTableColumn
cableDiagnosticsResultTableIndex = _CableDiagnosticsResultTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5, 1, 1),
    _CableDiagnosticsResultTableIndex_Type()
)
cableDiagnosticsResultTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cableDiagnosticsResultTableIndex.setStatus("current")
_CableDiagnosticsResultsDateTime_Type = Integer32
_CableDiagnosticsResultsDateTime_Object = MibTableColumn
cableDiagnosticsResultsDateTime = _CableDiagnosticsResultsDateTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5, 1, 2),
    _CableDiagnosticsResultsDateTime_Type()
)
cableDiagnosticsResultsDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagnosticsResultsDateTime.setStatus("current")


class _CableDiagPair1Results_Type(Integer32):
    """Custom type cableDiagPair1Results based on Integer32"""
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
        *(("inProgress", 2),
          ("notTested", 3),
          ("ok", 0),
          ("openCircuit", 4),
          ("shortCircuit", 5),
          ("unknown", 1))
    )


_CableDiagPair1Results_Type.__name__ = "Integer32"
_CableDiagPair1Results_Object = MibTableColumn
cableDiagPair1Results = _CableDiagPair1Results_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5, 1, 3),
    _CableDiagPair1Results_Type()
)
cableDiagPair1Results.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair1Results.setStatus("current")
_CableDiagPair1Distance_Type = Integer32
_CableDiagPair1Distance_Object = MibTableColumn
cableDiagPair1Distance = _CableDiagPair1Distance_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5, 1, 4),
    _CableDiagPair1Distance_Type()
)
cableDiagPair1Distance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair1Distance.setStatus("current")


class _CableDiagPair2Results_Type(Integer32):
    """Custom type cableDiagPair2Results based on Integer32"""
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
        *(("inProgress", 2),
          ("notTested", 3),
          ("ok", 0),
          ("openCircuit", 4),
          ("shortCircuit", 5),
          ("unknown", 1))
    )


_CableDiagPair2Results_Type.__name__ = "Integer32"
_CableDiagPair2Results_Object = MibTableColumn
cableDiagPair2Results = _CableDiagPair2Results_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5, 1, 5),
    _CableDiagPair2Results_Type()
)
cableDiagPair2Results.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair2Results.setStatus("current")
_CableDiagPair2Distance_Type = Integer32
_CableDiagPair2Distance_Object = MibTableColumn
cableDiagPair2Distance = _CableDiagPair2Distance_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5, 1, 6),
    _CableDiagPair2Distance_Type()
)
cableDiagPair2Distance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair2Distance.setStatus("current")


class _CableDiagPair3Results_Type(Integer32):
    """Custom type cableDiagPair3Results based on Integer32"""
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
        *(("inProgress", 2),
          ("notTested", 3),
          ("ok", 0),
          ("openCircuit", 4),
          ("shortCircuit", 5),
          ("unknown", 1))
    )


_CableDiagPair3Results_Type.__name__ = "Integer32"
_CableDiagPair3Results_Object = MibTableColumn
cableDiagPair3Results = _CableDiagPair3Results_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5, 1, 7),
    _CableDiagPair3Results_Type()
)
cableDiagPair3Results.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair3Results.setStatus("current")
_CableDiagPair3Distance_Type = Integer32
_CableDiagPair3Distance_Object = MibTableColumn
cableDiagPair3Distance = _CableDiagPair3Distance_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5, 1, 8),
    _CableDiagPair3Distance_Type()
)
cableDiagPair3Distance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair3Distance.setStatus("current")


class _CableDiagPair4Results_Type(Integer32):
    """Custom type cableDiagPair4Results based on Integer32"""
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
        *(("inProgress", 2),
          ("notTested", 3),
          ("ok", 0),
          ("openCircuit", 4),
          ("shortCircuit", 5),
          ("unknown", 1))
    )


_CableDiagPair4Results_Type.__name__ = "Integer32"
_CableDiagPair4Results_Object = MibTableColumn
cableDiagPair4Results = _CableDiagPair4Results_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5, 1, 9),
    _CableDiagPair4Results_Type()
)
cableDiagPair4Results.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair4Results.setStatus("current")
_CableDiagPair4Distance_Type = Integer32
_CableDiagPair4Distance_Object = MibTableColumn
cableDiagPair4Distance = _CableDiagPair4Distance_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 27, 5, 1, 10),
    _CableDiagPair4Distance_Type()
)
cableDiagPair4Distance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair4Distance.setStatus("current")
_Supplementary_ObjectIdentity = ObjectIdentity
supplementary = _Supplementary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 96)
)


class _Longitude_Type(DisplayString):
    """Custom type longitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Longitude_Type.__name__ = "DisplayString"
_Longitude_Object = MibScalar
longitude = _Longitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 96, 1),
    _Longitude_Type()
)
longitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    longitude.setStatus("current")


class _Latitude_Type(DisplayString):
    """Custom type latitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Latitude_Type.__name__ = "DisplayString"
_Latitude_Object = MibScalar
latitude = _Latitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 96, 2),
    _Latitude_Type()
)
latitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latitude.setStatus("current")
_Altitude_Type = Integer32
_Altitude_Object = MibScalar
altitude = _Altitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 7, 96, 3),
    _Altitude_Type()
)
altitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altitude.setStatus("current")
_PtpGroups_ObjectIdentity = ObjectIdentity
ptpGroups = _PtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98)
)
_PtpTraps_ObjectIdentity = ObjectIdentity
ptpTraps = _PtpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99)
)
_PtpTrapPrefix_ObjectIdentity = ObjectIdentity
ptpTrapPrefix = _PtpTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0)
)

# Managed Objects groups

dfsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 3)
)
dfsGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "dfsTableNumber"),
        ("CAMBIUM-PTP650-MIB", "extendedSpectrumScanning"),
        ("CAMBIUM-PTP650-MIB", "dfsMeans"),
        ("CAMBIUM-PTP650-MIB", "dfsNineNinePointNinePercentiles"),
        ("CAMBIUM-PTP650-MIB", "dfsPeaks"))
)
if mibBuilder.loadTexts:
    dfsGroup.setStatus("current")

bridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 4)
)
bridgeGroup.setObjects(
    ("CAMBIUM-PTP650-MIB", "localPacketFiltering")
)
if mibBuilder.loadTexts:
    bridgeGroup.setStatus("current")

configurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 5)
)
configurationGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "iPv4Address"),
        ("CAMBIUM-PTP650-MIB", "subnetMask"),
        ("CAMBIUM-PTP650-MIB", "gatewayIPAddress"),
        ("CAMBIUM-PTP650-MIB", "targetMACAddress"),
        ("CAMBIUM-PTP650-MIB", "masterSlaveMode"),
        ("CAMBIUM-PTP650-MIB", "maximumTransmitPower"),
        ("CAMBIUM-PTP650-MIB", "antennaGain"),
        ("CAMBIUM-PTP650-MIB", "cableLoss"),
        ("CAMBIUM-PTP650-MIB", "eIRP"),
        ("CAMBIUM-PTP650-MIB", "channelBandwidth"),
        ("CAMBIUM-PTP650-MIB", "linkName"),
        ("CAMBIUM-PTP650-MIB", "siteName"),
        ("CAMBIUM-PTP650-MIB", "accessMethod"),
        ("CAMBIUM-PTP650-MIB", "groupID"),
        ("CAMBIUM-PTP650-MIB", "iPv6Address"),
        ("CAMBIUM-PTP650-MIB", "iPVersion"),
        ("CAMBIUM-PTP650-MIB", "iPv6AutoConfiguredLinkLocalAddress"),
        ("CAMBIUM-PTP650-MIB", "iPv6PrefixLength"),
        ("CAMBIUM-PTP650-MIB", "iPv6GatewayAddress"),
        ("CAMBIUM-PTP650-MIB", "remoteInternetAddressType"),
        ("CAMBIUM-PTP650-MIB", "remoteInternetAddress"),
        ("CAMBIUM-PTP650-MIB", "subbandLowestFrequency"),
        ("CAMBIUM-PTP650-MIB", "subbandHighestFrequency"),
        ("CAMBIUM-PTP650-MIB", "enableTransmission"))
)
if mibBuilder.loadTexts:
    configurationGroup.setStatus("current")

ethernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 6)
)
ethernetGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "mainPSUPortAutoNegotiation"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortAutoNegAdvertisement"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortAutoMdix"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortStatus"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortSpeedAndDuplex"),
        ("CAMBIUM-PTP650-MIB", "dataPortWirelessDownAlert"),
        ("CAMBIUM-PTP650-MIB", "useVLANForManagementInterfaces"),
        ("CAMBIUM-PTP650-MIB", "vLANManagementPriority"),
        ("CAMBIUM-PTP650-MIB", "vLANManagementVID"),
        ("CAMBIUM-PTP650-MIB", "auxPortStatus"),
        ("CAMBIUM-PTP650-MIB", "auxPortSpeedAndDuplex"),
        ("CAMBIUM-PTP650-MIB", "ethernetPriorityTableNumber"),
        ("CAMBIUM-PTP650-MIB", "l2CPPriorityTableNumber"),
        ("CAMBIUM-PTP650-MIB", "iPDSCPPriorityTableNumber"),
        ("CAMBIUM-PTP650-MIB", "mPLSTCPriorityTableNumber"),
        ("CAMBIUM-PTP650-MIB", "managementPortWirelessDownAlert"),
        ("CAMBIUM-PTP650-MIB", "qOSPriorityScheme"),
        ("CAMBIUM-PTP650-MIB", "unknownNetworkPriorityQueueMapping"),
        ("CAMBIUM-PTP650-MIB", "dSCPManagementPriority"),
        ("CAMBIUM-PTP650-MIB", "dataBridgingStatus"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortAllocation"),
        ("CAMBIUM-PTP650-MIB", "auxPortAllocation"),
        ("CAMBIUM-PTP650-MIB", "sFPPortAllocation"),
        ("CAMBIUM-PTP650-MIB", "dataPortPauseFrames"),
        ("CAMBIUM-PTP650-MIB", "sFPPortAutoNegotiation"),
        ("CAMBIUM-PTP650-MIB", "sFPPortAutoNegAdvertisement"),
        ("CAMBIUM-PTP650-MIB", "sFPPortAutoMdix"),
        ("CAMBIUM-PTP650-MIB", "sFPPortStatus"),
        ("CAMBIUM-PTP650-MIB", "sFPPortSpeedAndDuplex"),
        ("CAMBIUM-PTP650-MIB", "auxPortPowerOverEthernetOutput"),
        ("CAMBIUM-PTP650-MIB", "auxPortPowerOverEthernetOutputStatus"),
        ("CAMBIUM-PTP650-MIB", "syncETracking"),
        ("CAMBIUM-PTP650-MIB", "syncEEquipmentClock"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortQLRxOverwrite"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortSSMTx"),
        ("CAMBIUM-PTP650-MIB", "sFPPortSSMTx"),
        ("CAMBIUM-PTP650-MIB", "auxPortSSMTx"),
        ("CAMBIUM-PTP650-MIB", "syncETrackingState"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortQLRx"),
        ("CAMBIUM-PTP650-MIB", "auxPortQLRx"),
        ("CAMBIUM-PTP650-MIB", "sFPPortQLRx"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortQLTx"),
        ("CAMBIUM-PTP650-MIB", "auxPortQLTx"),
        ("CAMBIUM-PTP650-MIB", "sFPPortQLTx"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortSyncEMasterSlaveStatus"),
        ("CAMBIUM-PTP650-MIB", "auxPortSyncEMasterSlaveStatus"),
        ("CAMBIUM-PTP650-MIB", "sFPPortSyncEMasterSlaveStatus"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortGigabitMasterSlaveStatus"),
        ("CAMBIUM-PTP650-MIB", "auxPortGigabitMasterSlaveStatus"),
        ("CAMBIUM-PTP650-MIB", "sFPPortGigabitMasterSlaveStatus"),
        ("CAMBIUM-PTP650-MIB", "transparentClock"),
        ("CAMBIUM-PTP650-MIB", "transparentClockVLAN"),
        ("CAMBIUM-PTP650-MIB", "transparentClockVID"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortAcceptedQLRx"),
        ("CAMBIUM-PTP650-MIB", "auxPortAcceptedQLRx"),
        ("CAMBIUM-PTP650-MIB", "sFPPortAcceptedQLRx"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortSyncERxStatus"),
        ("CAMBIUM-PTP650-MIB", "auxPortSyncERxStatus"),
        ("CAMBIUM-PTP650-MIB", "sFPPortSyncERxStatus"),
        ("CAMBIUM-PTP650-MIB", "nIDULanPortStatus"),
        ("CAMBIUM-PTP650-MIB", "nIDULanPortSpeedAndDuplex"),
        ("CAMBIUM-PTP650-MIB", "oOBPriorityQueueMapping"),
        ("CAMBIUM-PTP650-MIB", "nIDULanPortAutoNegotiation"),
        ("CAMBIUM-PTP650-MIB", "nIDULanPortAutoNegAdvertisement"),
        ("CAMBIUM-PTP650-MIB", "nIDULanPortAutoMdix"),
        ("CAMBIUM-PTP650-MIB", "nIDULanPortGigabitMasterSlaveStatus"),
        ("CAMBIUM-PTP650-MIB", "txMABFrames"),
        ("CAMBIUM-PTP650-MIB", "managementNetworkAccessEnabled"),
        ("CAMBIUM-PTP650-MIB", "secondDataPortPauseFrames"),
        ("CAMBIUM-PTP650-MIB", "secondDataBridgingStatus"),
        ("CAMBIUM-PTP650-MIB", "transparentClockPort"),
        ("CAMBIUM-PTP650-MIB", "ethernetPriorityQueueMapping"),
        ("CAMBIUM-PTP650-MIB", "l2CPPriorityQueueMapping"),
        ("CAMBIUM-PTP650-MIB", "iPDSCPPriorityQueueMapping"),
        ("CAMBIUM-PTP650-MIB", "mPLSTCPriorityQueueMapping"))
)
if mibBuilder.loadTexts:
    ethernetGroup.setStatus("current")

tDMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 7)
)
tDMGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "tDMInterfaceControl"),
        ("CAMBIUM-PTP650-MIB", "tDMInterfaceStatus"),
        ("CAMBIUM-PTP650-MIB", "tDMEnabledChannels"),
        ("CAMBIUM-PTP650-MIB", "tdmTableNumber"),
        ("CAMBIUM-PTP650-MIB", "tDMConfigurationMismatch"),
        ("CAMBIUM-PTP650-MIB", "lowestTDMModulationMode"),
        ("CAMBIUM-PTP650-MIB", "tDMChannelStatus"),
        ("CAMBIUM-PTP650-MIB", "tDMChannelLineCode"),
        ("CAMBIUM-PTP650-MIB", "tDMChannelCableLength"),
        ("CAMBIUM-PTP650-MIB", "tDMChannelLoopback"))
)
if mibBuilder.loadTexts:
    tDMGroup.setStatus("current")

licenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 8)
)
licenseGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "regulatoryBand"),
        ("CAMBIUM-PTP650-MIB", "productVariant"),
        ("CAMBIUM-PTP650-MIB", "productName"),
        ("CAMBIUM-PTP650-MIB", "frequencyVariant"),
        ("CAMBIUM-PTP650-MIB", "sNMPv3Enable"),
        ("CAMBIUM-PTP650-MIB", "licenseVersion"),
        ("CAMBIUM-PTP650-MIB", "licenseUnitSerialNumber"),
        ("CAMBIUM-PTP650-MIB", "licenseIssueNumber"),
        ("CAMBIUM-PTP650-MIB", "licenseCountry"),
        ("CAMBIUM-PTP650-MIB", "licenseNumberOfRegulatoryBands"),
        ("CAMBIUM-PTP650-MIB", "licenseBandwidthCap"),
        ("CAMBIUM-PTP650-MIB", "licenseEncryption"),
        ("CAMBIUM-PTP650-MIB", "licenseSecurityLevel"),
        ("CAMBIUM-PTP650-MIB", "licenseGroupAccess"),
        ("CAMBIUM-PTP650-MIB", "licenseOOBManagementSupport"),
        ("CAMBIUM-PTP650-MIB", "licenseSFPPortSupport"),
        ("CAMBIUM-PTP650-MIB", "licenseAuxiliaryPortSupport"),
        ("CAMBIUM-PTP650-MIB", "licenseCapacity"),
        ("CAMBIUM-PTP650-MIB", "licenseMaxNumberOfTDMChannels"),
        ("CAMBIUM-PTP650-MIB", "licenseIEEE1588Support"),
        ("CAMBIUM-PTP650-MIB", "licenseSyncESupport"),
        ("CAMBIUM-PTP650-MIB", "licenseIPv6Support"),
        ("CAMBIUM-PTP650-MIB", "licenseMinimumFirmwareVersion"),
        ("CAMBIUM-PTP650-MIB", "licenseFullCapabilityTrialStatus"),
        ("CAMBIUM-PTP650-MIB", "licenseRemainingTrialPeriod"),
        ("CAMBIUM-PTP650-MIB", "licenseRemainingTrialPeriodAlarm"),
        ("CAMBIUM-PTP650-MIB", "capacityVariantMismatch"),
        ("CAMBIUM-PTP650-MIB", "licenseTDDSyncSupport"),
        ("CAMBIUM-PTP650-MIB", "licenseMaxLinkRange"),
        ("CAMBIUM-PTP650-MIB", "licenseTrialPeriod"),
        ("CAMBIUM-PTP650-MIB", "licenseRARSupport"),
        ("CAMBIUM-PTP650-MIB", "licenseRegulatoryBandsList"))
)
if mibBuilder.loadTexts:
    licenseGroup.setStatus("current")

managementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 9)
)
managementGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "targetRange"),
        ("CAMBIUM-PTP650-MIB", "rangingMode"),
        ("CAMBIUM-PTP650-MIB", "installStatus"),
        ("CAMBIUM-PTP650-MIB", "installArmState"),
        ("CAMBIUM-PTP650-MIB", "tFTPServerPortNumber"),
        ("CAMBIUM-PTP650-MIB", "tFTPSoftwareUpgradeFileName"),
        ("CAMBIUM-PTP650-MIB", "tFTPStartSoftwareUpgrade"),
        ("CAMBIUM-PTP650-MIB", "tFTPSoftwareUpgradeStatus"),
        ("CAMBIUM-PTP650-MIB", "tFTPSoftwareUpgradeStatusText"),
        ("CAMBIUM-PTP650-MIB", "tFTPSoftwareUpgradeStatusAdditionalText"),
        ("CAMBIUM-PTP650-MIB", "hTTPAccessEnabled"),
        ("CAMBIUM-PTP650-MIB", "telnetAccessEnabled"),
        ("CAMBIUM-PTP650-MIB", "hTTPPortNumber"),
        ("CAMBIUM-PTP650-MIB", "hTTPSPortNumber"),
        ("CAMBIUM-PTP650-MIB", "telnetPortNumber"),
        ("CAMBIUM-PTP650-MIB", "hTTPSAccessEnabled"),
        ("CAMBIUM-PTP650-MIB", "tFTPServerInternetAddressType"),
        ("CAMBIUM-PTP650-MIB", "tFTPServerInternetAddress"),
        ("CAMBIUM-PTP650-MIB", "lowestDataModulationMode"),
        ("CAMBIUM-PTP650-MIB", "lowestSecondDataModulationMode"))
)
if mibBuilder.loadTexts:
    managementGroup.setStatus("current")

phyControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 10)
)
phyControlGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "linkSymmetry"),
        ("CAMBIUM-PTP650-MIB", "userConfiguredMaxModulationMode"),
        ("CAMBIUM-PTP650-MIB", "linkModeOptimization"),
        ("CAMBIUM-PTP650-MIB", "txColorCode"),
        ("CAMBIUM-PTP650-MIB", "rxColorCode"),
        ("CAMBIUM-PTP650-MIB", "remoteMaximumTransmitPower"))
)
if mibBuilder.loadTexts:
    phyControlGroup.setStatus("current")

phyStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 12)
)
phyStatusGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "linkLoss"),
        ("CAMBIUM-PTP650-MIB", "receivePower"),
        ("CAMBIUM-PTP650-MIB", "vectorError"),
        ("CAMBIUM-PTP650-MIB", "transmitPower"),
        ("CAMBIUM-PTP650-MIB", "receiveChannel"),
        ("CAMBIUM-PTP650-MIB", "transmitChannel"),
        ("CAMBIUM-PTP650-MIB", "receiveFreqMHz"),
        ("CAMBIUM-PTP650-MIB", "transmitFreqMHz"),
        ("CAMBIUM-PTP650-MIB", "signalStrengthRatio"),
        ("CAMBIUM-PTP650-MIB", "receiveFreqKHz"),
        ("CAMBIUM-PTP650-MIB", "transmitFreqKHz"),
        ("CAMBIUM-PTP650-MIB", "rawReceivePower"),
        ("CAMBIUM-PTP650-MIB", "range"),
        ("CAMBIUM-PTP650-MIB", "receiveModulationMode"),
        ("CAMBIUM-PTP650-MIB", "transmitModulationMode"),
        ("CAMBIUM-PTP650-MIB", "searchState"))
)
if mibBuilder.loadTexts:
    phyStatusGroup.setStatus("current")

alarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 13)
)
alarmsGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "unitOutOfCalibration"),
        ("CAMBIUM-PTP650-MIB", "incompatibleRegulatoryBands"),
        ("CAMBIUM-PTP650-MIB", "noWirelessChannelAvailable"),
        ("CAMBIUM-PTP650-MIB", "wirelessLinkDisabledWarning"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortDisabledWarning"),
        ("CAMBIUM-PTP650-MIB", "sFPError"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortConfigurationMismatch"),
        ("CAMBIUM-PTP650-MIB", "incompatibleMasterAndSlave"),
        ("CAMBIUM-PTP650-MIB", "tDDSynchronizationStatus"),
        ("CAMBIUM-PTP650-MIB", "auxPortDisabledWarning"),
        ("CAMBIUM-PTP650-MIB", "tDDSynchronizationAlarm"),
        ("CAMBIUM-PTP650-MIB", "linkModeOptimizationMismatch"),
        ("CAMBIUM-PTP650-MIB", "auxPortConfigurationMismatch"),
        ("CAMBIUM-PTP650-MIB", "secureModeAlarm"),
        ("CAMBIUM-PTP650-MIB", "dataBridgingStatusAlarm"),
        ("CAMBIUM-PTP650-MIB", "sFPPortDisabledWarning"),
        ("CAMBIUM-PTP650-MIB", "sFPPortConfigurationMismatch"),
        ("CAMBIUM-PTP650-MIB", "maxLinkRangeExceeded"),
        ("CAMBIUM-PTP650-MIB", "nIDULanPortDisabledWarning"),
        ("CAMBIUM-PTP650-MIB", "nIDULanPortConfigurationMismatch"),
        ("CAMBIUM-PTP650-MIB", "portAllocationMismatch"),
        ("CAMBIUM-PTP650-MIB", "secondDataBridgingStatusAlarm"),
        ("CAMBIUM-PTP650-MIB", "transparentClockSourcePortAlarm"))
)
if mibBuilder.loadTexts:
    alarmsGroup.setStatus("current")

smtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 15)
)
smtpGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "sMTPEmailAlert"),
        ("CAMBIUM-PTP650-MIB", "sMTPServerPortNumber"),
        ("CAMBIUM-PTP650-MIB", "sMTPSourceEmailAddress"),
        ("CAMBIUM-PTP650-MIB", "sMTPDestinationEmailAddress"),
        ("CAMBIUM-PTP650-MIB", "sMTPEnabledMessages"),
        ("CAMBIUM-PTP650-MIB", "sMTPServerInternetAddressType"),
        ("CAMBIUM-PTP650-MIB", "sMTPServerInternetAddress"))
)
if mibBuilder.loadTexts:
    smtpGroup.setStatus("current")

snmpControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 16)
)
snmpControlGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "sNMPPortNumber"),
        ("CAMBIUM-PTP650-MIB", "sNMPCommunityString"),
        ("CAMBIUM-PTP650-MIB", "sNMPTrapTableNumber"),
        ("CAMBIUM-PTP650-MIB", "sNMPTrapVersion"),
        ("CAMBIUM-PTP650-MIB", "sNMPEnabledTraps"),
        ("CAMBIUM-PTP650-MIB", "enabledDiagnosticAlarms"),
        ("CAMBIUM-PTP650-MIB", "sNMPSendAllTrapsAtStartup"),
        ("CAMBIUM-PTP650-MIB", "sNMPTrapPortNumber"),
        ("CAMBIUM-PTP650-MIB", "sNMPTrapInternetAddressType"),
        ("CAMBIUM-PTP650-MIB", "sNMPTrapInternetAddress"),
        ("CAMBIUM-PTP650-MIB", "sNMPTrapReceiverEnabled"))
)
if mibBuilder.loadTexts:
    snmpControlGroup.setStatus("current")

sntpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 17)
)
sntpGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "sNTPState"),
        ("CAMBIUM-PTP650-MIB", "sNTPPollInterval"),
        ("CAMBIUM-PTP650-MIB", "sNTPSync"),
        ("CAMBIUM-PTP650-MIB", "sNTPLastSync"),
        ("CAMBIUM-PTP650-MIB", "systemClock"),
        ("CAMBIUM-PTP650-MIB", "timeZone"),
        ("CAMBIUM-PTP650-MIB", "daylightSaving"),
        ("CAMBIUM-PTP650-MIB", "sNTPPrimaryServer"),
        ("CAMBIUM-PTP650-MIB", "sNTPPrimaryServerDeadTime"),
        ("CAMBIUM-PTP650-MIB", "sNTPServerRetries"),
        ("CAMBIUM-PTP650-MIB", "sNTPServerTimeout"),
        ("CAMBIUM-PTP650-MIB", "sNTPServerTableNumber"),
        ("CAMBIUM-PTP650-MIB", "sNTPServerPortNumber"),
        ("CAMBIUM-PTP650-MIB", "sNTPServerStatus"),
        ("CAMBIUM-PTP650-MIB", "sNTPServerInternetAddressType"),
        ("CAMBIUM-PTP650-MIB", "sNTPServerInternetAddress"))
)
if mibBuilder.loadTexts:
    sntpGroup.setStatus("current")

resetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 18)
)
resetGroup.setObjects(
    ("CAMBIUM-PTP650-MIB", "systemReset")
)
if mibBuilder.loadTexts:
    resetGroup.setStatus("current")

versionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 19)
)
versionsGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "softwareVersion"),
        ("CAMBIUM-PTP650-MIB", "hardwareVersion"),
        ("CAMBIUM-PTP650-MIB", "secondarySoftwareVersion"),
        ("CAMBIUM-PTP650-MIB", "bootVersion"))
)
if mibBuilder.loadTexts:
    versionsGroup.setStatus("current")

pubStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 20)
)
pubStatsGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "receiveDataRate"),
        ("CAMBIUM-PTP650-MIB", "transmitDataRate"),
        ("CAMBIUM-PTP650-MIB", "aggregateDataRate"),
        ("CAMBIUM-PTP650-MIB", "wirelessLinkAvailability"),
        ("CAMBIUM-PTP650-MIB", "wirelessLinkStatus"),
        ("CAMBIUM-PTP650-MIB", "byteErrorRatio"),
        ("CAMBIUM-PTP650-MIB", "receiveModulationModeDetail"),
        ("CAMBIUM-PTP650-MIB", "dataBridgingAvailability"))
)
if mibBuilder.loadTexts:
    pubStatsGroup.setStatus("current")

encryptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 22)
)
encryptionGroup.setObjects(
    ("CAMBIUM-PTP650-MIB", "encryptionAlgorithm")
)
if mibBuilder.loadTexts:
    encryptionGroup.setStatus("current")

tDDControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 23)
)
tDDControlGroup.setObjects(
    ("CAMBIUM-PTP650-MIB", "tDDSynchronizationMode")
)
if mibBuilder.loadTexts:
    tDDControlGroup.setStatus("current")

syslogControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 24)
)
syslogControlGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "syslogClient"),
        ("CAMBIUM-PTP650-MIB", "syslogState"))
)
if mibBuilder.loadTexts:
    syslogControlGroup.setStatus("current")

aAAControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 25)
)
aAAControlGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "userTableNumber"),
        ("CAMBIUM-PTP650-MIB", "userName"),
        ("CAMBIUM-PTP650-MIB", "userRole"),
        ("CAMBIUM-PTP650-MIB", "userEnabled"),
        ("CAMBIUM-PTP650-MIB", "userPassword"))
)
if mibBuilder.loadTexts:
    aAAControlGroup.setStatus("current")

routerProtocolsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 26)
)
routerProtocolsGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "microwaveAdaptiveBandwidth"),
        ("CAMBIUM-PTP650-MIB", "mABNominalModulationMode"),
        ("CAMBIUM-PTP650-MIB", "mABTransmissionInterval"),
        ("CAMBIUM-PTP650-MIB", "mABHoldoffPeriod"),
        ("CAMBIUM-PTP650-MIB", "mABMaintenanceLevel"),
        ("CAMBIUM-PTP650-MIB", "useVLANForMABProtocol"),
        ("CAMBIUM-PTP650-MIB", "mABProtocolVID"),
        ("CAMBIUM-PTP650-MIB", "mABProtocolVLANPriority"),
        ("CAMBIUM-PTP650-MIB", "mABState"),
        ("CAMBIUM-PTP650-MIB", "mABNominalTransmitCapacity"),
        ("CAMBIUM-PTP650-MIB", "mABCurrentTransmitCapacity"))
)
if mibBuilder.loadTexts:
    routerProtocolsGroup.setStatus("current")

cableDiagnosticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 27)
)
cableDiagnosticsGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "cableDiagnosticsPorts"),
        ("CAMBIUM-PTP650-MIB", "cableDiagnosticsControl"),
        ("CAMBIUM-PTP650-MIB", "cableDiagnosticsWarning"),
        ("CAMBIUM-PTP650-MIB", "cableDiagnosticsResultTableNumber"),
        ("CAMBIUM-PTP650-MIB", "cableDiagnosticsResultsDateTime"),
        ("CAMBIUM-PTP650-MIB", "cableDiagPair1Results"),
        ("CAMBIUM-PTP650-MIB", "cableDiagPair1Distance"),
        ("CAMBIUM-PTP650-MIB", "cableDiagPair2Results"),
        ("CAMBIUM-PTP650-MIB", "cableDiagPair2Distance"),
        ("CAMBIUM-PTP650-MIB", "cableDiagPair3Results"),
        ("CAMBIUM-PTP650-MIB", "cableDiagPair3Distance"),
        ("CAMBIUM-PTP650-MIB", "cableDiagPair4Results"),
        ("CAMBIUM-PTP650-MIB", "cableDiagPair4Distance"))
)
if mibBuilder.loadTexts:
    cableDiagnosticsGroup.setStatus("current")

supplementaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 96)
)
supplementaryGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "longitude"),
        ("CAMBIUM-PTP650-MIB", "latitude"),
        ("CAMBIUM-PTP650-MIB", "altitude"))
)
if mibBuilder.loadTexts:
    supplementaryGroup.setStatus("current")


# Notification objects

channelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 1)
)
channelChangeTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "receiveChannel")
)
if mibBuilder.loadTexts:
    channelChangeTrap.setStatus(
        "current"
    )

dfsImpulsiveInterferenceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 2)
)
dfsImpulsiveInterferenceTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "receiveChannel")
)
if mibBuilder.loadTexts:
    dfsImpulsiveInterferenceTrap.setStatus(
        "current"
    )

mainPSUPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 3)
)
mainPSUPortStatusTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "mainPSUPortStatus")
)
if mibBuilder.loadTexts:
    mainPSUPortStatusTrap.setStatus(
        "current"
    )

mainPSUPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 4)
)
mainPSUPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "mainPSUPortDisabledWarning")
)
if mibBuilder.loadTexts:
    mainPSUPortDisabledWarningTrap.setStatus(
        "current"
    )

mainPSUPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 5)
)
mainPSUPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "mainPSUPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    mainPSUPortConfigurationMismatchTrap.setStatus(
        "current"
    )

auxPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 6)
)
auxPortStatusTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "auxPortStatus")
)
if mibBuilder.loadTexts:
    auxPortStatusTrap.setStatus(
        "current"
    )

auxPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 7)
)
auxPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "auxPortDisabledWarning")
)
if mibBuilder.loadTexts:
    auxPortDisabledWarningTrap.setStatus(
        "current"
    )

regulatoryBandTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 8)
)
regulatoryBandTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "regulatoryBand")
)
if mibBuilder.loadTexts:
    regulatoryBandTrap.setStatus(
        "current"
    )

installStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 9)
)
installStatusTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "installStatus")
)
if mibBuilder.loadTexts:
    installStatusTrap.setStatus(
        "current"
    )

installArmStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 10)
)
installArmStateTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "installArmState")
)
if mibBuilder.loadTexts:
    installArmStateTrap.setStatus(
        "current"
    )

unitOutOfCalibrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 11)
)
unitOutOfCalibrationTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "unitOutOfCalibration")
)
if mibBuilder.loadTexts:
    unitOutOfCalibrationTrap.setStatus(
        "current"
    )

auxPortPowerOverEthernetOutputStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 12)
)
auxPortPowerOverEthernetOutputStatusTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "auxPortPowerOverEthernetOutputStatus")
)
if mibBuilder.loadTexts:
    auxPortPowerOverEthernetOutputStatusTrap.setStatus(
        "current"
    )

incompatibleRegulatoryBandsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 14)
)
incompatibleRegulatoryBandsTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "incompatibleRegulatoryBands")
)
if mibBuilder.loadTexts:
    incompatibleRegulatoryBandsTrap.setStatus(
        "current"
    )

noWirelessChannelAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 15)
)
noWirelessChannelAvailableTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "noWirelessChannelAvailable")
)
if mibBuilder.loadTexts:
    noWirelessChannelAvailableTrap.setStatus(
        "current"
    )

wirelessLinkDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 16)
)
wirelessLinkDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "wirelessLinkDisabledWarning")
)
if mibBuilder.loadTexts:
    wirelessLinkDisabledWarningTrap.setStatus(
        "current"
    )

auxPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 17)
)
auxPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "auxPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    auxPortConfigurationMismatchTrap.setStatus(
        "current"
    )

sFPErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 18)
)
sFPErrorTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "sFPError")
)
if mibBuilder.loadTexts:
    sFPErrorTrap.setStatus(
        "current"
    )

sFPPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 19)
)
sFPPortStatusTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "sFPPortStatus")
)
if mibBuilder.loadTexts:
    sFPPortStatusTrap.setStatus(
        "current"
    )

incompatibleMasterAndSlaveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 20)
)
incompatibleMasterAndSlaveTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "incompatibleMasterAndSlave")
)
if mibBuilder.loadTexts:
    incompatibleMasterAndSlaveTrap.setStatus(
        "current"
    )

sNTPSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 21)
)
sNTPSyncTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "sNTPSync")
)
if mibBuilder.loadTexts:
    sNTPSyncTrap.setStatus(
        "current"
    )

tDDSynchronizationAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 22)
)
tDDSynchronizationAlarmTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "tDDSynchronizationAlarm")
)
if mibBuilder.loadTexts:
    tDDSynchronizationAlarmTrap.setStatus(
        "current"
    )

sFPPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 23)
)
sFPPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "sFPPortDisabledWarning")
)
if mibBuilder.loadTexts:
    sFPPortDisabledWarningTrap.setStatus(
        "current"
    )

sFPPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 24)
)
sFPPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "sFPPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    sFPPortConfigurationMismatchTrap.setStatus(
        "current"
    )

linkModeOptimizationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 25)
)
linkModeOptimizationMismatchTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "linkModeOptimizationMismatch")
)
if mibBuilder.loadTexts:
    linkModeOptimizationMismatchTrap.setStatus(
        "current"
    )

tDMInterfaceStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 26)
)
tDMInterfaceStatusTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "tDMInterfaceStatus")
)
if mibBuilder.loadTexts:
    tDMInterfaceStatusTrap.setStatus(
        "current"
    )

tDMChannelStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 27)
)
tDMChannelStatusTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "tDMChannelStatus")
)
if mibBuilder.loadTexts:
    tDMChannelStatusTrap.setStatus(
        "current"
    )

tDMChannelLoopbackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 28)
)
tDMChannelLoopbackTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "tDMChannelLoopback")
)
if mibBuilder.loadTexts:
    tDMChannelLoopbackTrap.setStatus(
        "current"
    )

nIDULanPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 29)
)
nIDULanPortStatusTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "nIDULanPortStatus")
)
if mibBuilder.loadTexts:
    nIDULanPortStatusTrap.setStatus(
        "current"
    )

syslogStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 30)
)
syslogStateTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "syslogState")
)
if mibBuilder.loadTexts:
    syslogStateTrap.setStatus(
        "current"
    )

syslogLocalNearlyFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 31)
)
if mibBuilder.loadTexts:
    syslogLocalNearlyFullTrap.setStatus(
        "current"
    )

syslogLocalWrappedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 32)
)
if mibBuilder.loadTexts:
    syslogLocalWrappedTrap.setStatus(
        "current"
    )

syslogClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 33)
)
syslogClientTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "syslogClient")
)
if mibBuilder.loadTexts:
    syslogClientTrap.setStatus(
        "current"
    )

secureModeAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 34)
)
secureModeAlarmTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "secureModeAlarm")
)
if mibBuilder.loadTexts:
    secureModeAlarmTrap.setStatus(
        "current"
    )

dataBridgingStatusAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 35)
)
dataBridgingStatusAlarmTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "dataBridgingStatusAlarm")
)
if mibBuilder.loadTexts:
    dataBridgingStatusAlarmTrap.setStatus(
        "current"
    )

licenseRemainingTrialPeriodAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 36)
)
licenseRemainingTrialPeriodAlarmTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "licenseRemainingTrialPeriodAlarm")
)
if mibBuilder.loadTexts:
    licenseRemainingTrialPeriodAlarmTrap.setStatus(
        "current"
    )

capacityVariantMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 37)
)
capacityVariantMismatchTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "capacityVariantMismatch")
)
if mibBuilder.loadTexts:
    capacityVariantMismatchTrap.setStatus(
        "current"
    )

maxLinkRangeExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 38)
)
maxLinkRangeExceededTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "maxLinkRangeExceeded")
)
if mibBuilder.loadTexts:
    maxLinkRangeExceededTrap.setStatus(
        "current"
    )

tDMConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 39)
)
tDMConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "tDMConfigurationMismatch")
)
if mibBuilder.loadTexts:
    tDMConfigurationMismatchTrap.setStatus(
        "current"
    )

nIDULanPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 40)
)
nIDULanPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "nIDULanPortDisabledWarning")
)
if mibBuilder.loadTexts:
    nIDULanPortDisabledWarningTrap.setStatus(
        "current"
    )

nIDULanPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 41)
)
nIDULanPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "nIDULanPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    nIDULanPortConfigurationMismatchTrap.setStatus(
        "current"
    )

secondDataBridgingStatusAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 42)
)
secondDataBridgingStatusAlarmTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "secondDataBridgingStatusAlarm")
)
if mibBuilder.loadTexts:
    secondDataBridgingStatusAlarmTrap.setStatus(
        "current"
    )

transparentClockSourcePortAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 43)
)
transparentClockSourcePortAlarmTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "transparentClockSourcePortAlarm")
)
if mibBuilder.loadTexts:
    transparentClockSourcePortAlarmTrap.setStatus(
        "current"
    )

portAllocationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 7, 99, 0, 44)
)
portAllocationMismatchTrap.setObjects(
    ("CAMBIUM-PTP650-MIB", "portAllocationMismatch")
)
if mibBuilder.loadTexts:
    portAllocationMismatchTrap.setStatus(
        "current"
    )


# Notifications groups

notificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 17713, 7, 98, 99)
)
notificationsGroup.setObjects(
      *(("CAMBIUM-PTP650-MIB", "channelChangeTrap"),
        ("CAMBIUM-PTP650-MIB", "dfsImpulsiveInterferenceTrap"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortStatusTrap"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortDisabledWarningTrap"),
        ("CAMBIUM-PTP650-MIB", "mainPSUPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP650-MIB", "auxPortStatusTrap"),
        ("CAMBIUM-PTP650-MIB", "auxPortDisabledWarningTrap"),
        ("CAMBIUM-PTP650-MIB", "regulatoryBandTrap"),
        ("CAMBIUM-PTP650-MIB", "installStatusTrap"),
        ("CAMBIUM-PTP650-MIB", "installArmStateTrap"),
        ("CAMBIUM-PTP650-MIB", "unitOutOfCalibrationTrap"),
        ("CAMBIUM-PTP650-MIB", "auxPortPowerOverEthernetOutputStatusTrap"),
        ("CAMBIUM-PTP650-MIB", "incompatibleRegulatoryBandsTrap"),
        ("CAMBIUM-PTP650-MIB", "noWirelessChannelAvailableTrap"),
        ("CAMBIUM-PTP650-MIB", "wirelessLinkDisabledWarningTrap"),
        ("CAMBIUM-PTP650-MIB", "auxPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP650-MIB", "sFPErrorTrap"),
        ("CAMBIUM-PTP650-MIB", "sFPPortStatusTrap"),
        ("CAMBIUM-PTP650-MIB", "incompatibleMasterAndSlaveTrap"),
        ("CAMBIUM-PTP650-MIB", "sNTPSyncTrap"),
        ("CAMBIUM-PTP650-MIB", "tDDSynchronizationAlarmTrap"),
        ("CAMBIUM-PTP650-MIB", "sFPPortDisabledWarningTrap"),
        ("CAMBIUM-PTP650-MIB", "sFPPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP650-MIB", "linkModeOptimizationMismatchTrap"),
        ("CAMBIUM-PTP650-MIB", "tDMInterfaceStatusTrap"),
        ("CAMBIUM-PTP650-MIB", "tDMChannelStatusTrap"),
        ("CAMBIUM-PTP650-MIB", "tDMChannelLoopbackTrap"),
        ("CAMBIUM-PTP650-MIB", "nIDULanPortStatusTrap"),
        ("CAMBIUM-PTP650-MIB", "syslogStateTrap"),
        ("CAMBIUM-PTP650-MIB", "syslogLocalNearlyFullTrap"),
        ("CAMBIUM-PTP650-MIB", "syslogLocalWrappedTrap"),
        ("CAMBIUM-PTP650-MIB", "syslogClientTrap"),
        ("CAMBIUM-PTP650-MIB", "secureModeAlarmTrap"),
        ("CAMBIUM-PTP650-MIB", "dataBridgingStatusAlarmTrap"),
        ("CAMBIUM-PTP650-MIB", "licenseRemainingTrialPeriodAlarmTrap"),
        ("CAMBIUM-PTP650-MIB", "capacityVariantMismatchTrap"),
        ("CAMBIUM-PTP650-MIB", "maxLinkRangeExceededTrap"),
        ("CAMBIUM-PTP650-MIB", "tDMConfigurationMismatchTrap"),
        ("CAMBIUM-PTP650-MIB", "nIDULanPortDisabledWarningTrap"),
        ("CAMBIUM-PTP650-MIB", "nIDULanPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP650-MIB", "secondDataBridgingStatusAlarmTrap"),
        ("CAMBIUM-PTP650-MIB", "transparentClockSourcePortAlarmTrap"),
        ("CAMBIUM-PTP650-MIB", "portAllocationMismatchTrap"))
)
if mibBuilder.loadTexts:
    notificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ptpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 17713, 7, 97)
)
if mibBuilder.loadTexts:
    ptpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-PTP650-MIB",
    **{"cambium": cambium,
       "ptp": ptp,
       "ptmp": ptmp,
       "ptp650": ptp650,
       "dfs": dfs,
       "dfsTableNumber": dfsTableNumber,
       "dfsTable": dfsTable,
       "dfsTableEntry": dfsTableEntry,
       "dfsTableIndex": dfsTableIndex,
       "dfsMeans": dfsMeans,
       "dfsNineNinePointNinePercentiles": dfsNineNinePointNinePercentiles,
       "dfsPeaks": dfsPeaks,
       "extendedSpectrumScanning": extendedSpectrumScanning,
       "bridge": bridge,
       "localPacketFiltering": localPacketFiltering,
       "configuration": configuration,
       "iPv4Address": iPv4Address,
       "subnetMask": subnetMask,
       "gatewayIPAddress": gatewayIPAddress,
       "targetMACAddress": targetMACAddress,
       "masterSlaveMode": masterSlaveMode,
       "maximumTransmitPower": maximumTransmitPower,
       "antennaGain": antennaGain,
       "cableLoss": cableLoss,
       "eIRP": eIRP,
       "channelBandwidth": channelBandwidth,
       "linkName": linkName,
       "siteName": siteName,
       "accessMethod": accessMethod,
       "groupID": groupID,
       "iPv6Address": iPv6Address,
       "iPVersion": iPVersion,
       "iPv6AutoConfiguredLinkLocalAddress": iPv6AutoConfiguredLinkLocalAddress,
       "iPv6PrefixLength": iPv6PrefixLength,
       "iPv6GatewayAddress": iPv6GatewayAddress,
       "remoteInternetAddressType": remoteInternetAddressType,
       "remoteInternetAddress": remoteInternetAddress,
       "subbandLowestFrequency": subbandLowestFrequency,
       "subbandHighestFrequency": subbandHighestFrequency,
       "enableTransmission": enableTransmission,
       "ethernet": ethernet,
       "mainPSUPortAutoNegotiation": mainPSUPortAutoNegotiation,
       "mainPSUPortAutoNegAdvertisement": mainPSUPortAutoNegAdvertisement,
       "mainPSUPortAutoMdix": mainPSUPortAutoMdix,
       "mainPSUPortStatus": mainPSUPortStatus,
       "mainPSUPortSpeedAndDuplex": mainPSUPortSpeedAndDuplex,
       "dataPortWirelessDownAlert": dataPortWirelessDownAlert,
       "useVLANForManagementInterfaces": useVLANForManagementInterfaces,
       "vLANManagementPriority": vLANManagementPriority,
       "vLANManagementVID": vLANManagementVID,
       "auxPortStatus": auxPortStatus,
       "auxPortSpeedAndDuplex": auxPortSpeedAndDuplex,
       "ethernetPriorityTableNumber": ethernetPriorityTableNumber,
       "ethernetPriorityTable": ethernetPriorityTable,
       "ethernetPriorityTableEntry": ethernetPriorityTableEntry,
       "ethernetPriorityTableIndex": ethernetPriorityTableIndex,
       "ethernetPriorityQueueMapping": ethernetPriorityQueueMapping,
       "l2CPPriorityTableNumber": l2CPPriorityTableNumber,
       "l2CPPriorityTable": l2CPPriorityTable,
       "l2CPPriorityTableEntry": l2CPPriorityTableEntry,
       "l2CPPriorityTableIndex": l2CPPriorityTableIndex,
       "l2CPPriorityQueueMapping": l2CPPriorityQueueMapping,
       "iPDSCPPriorityTableNumber": iPDSCPPriorityTableNumber,
       "iPDSCPPriorityTable": iPDSCPPriorityTable,
       "iPDSCPPriorityTableEntry": iPDSCPPriorityTableEntry,
       "iPDSCPPriorityTableIndex": iPDSCPPriorityTableIndex,
       "iPDSCPPriorityQueueMapping": iPDSCPPriorityQueueMapping,
       "mPLSTCPriorityTableNumber": mPLSTCPriorityTableNumber,
       "mPLSTCPriorityTable": mPLSTCPriorityTable,
       "mPLSTCPriorityTableEntry": mPLSTCPriorityTableEntry,
       "mPLSTCPriorityTableIndex": mPLSTCPriorityTableIndex,
       "mPLSTCPriorityQueueMapping": mPLSTCPriorityQueueMapping,
       "managementPortWirelessDownAlert": managementPortWirelessDownAlert,
       "qOSPriorityScheme": qOSPriorityScheme,
       "unknownNetworkPriorityQueueMapping": unknownNetworkPriorityQueueMapping,
       "dSCPManagementPriority": dSCPManagementPriority,
       "dataBridgingStatus": dataBridgingStatus,
       "mainPSUPortAllocation": mainPSUPortAllocation,
       "auxPortAllocation": auxPortAllocation,
       "sFPPortAllocation": sFPPortAllocation,
       "dataPortPauseFrames": dataPortPauseFrames,
       "sFPPortAutoNegotiation": sFPPortAutoNegotiation,
       "sFPPortAutoNegAdvertisement": sFPPortAutoNegAdvertisement,
       "sFPPortAutoMdix": sFPPortAutoMdix,
       "sFPPortStatus": sFPPortStatus,
       "sFPPortSpeedAndDuplex": sFPPortSpeedAndDuplex,
       "auxPortPowerOverEthernetOutput": auxPortPowerOverEthernetOutput,
       "auxPortPowerOverEthernetOutputStatus": auxPortPowerOverEthernetOutputStatus,
       "syncETracking": syncETracking,
       "syncEEquipmentClock": syncEEquipmentClock,
       "mainPSUPortQLRxOverwrite": mainPSUPortQLRxOverwrite,
       "mainPSUPortSSMTx": mainPSUPortSSMTx,
       "sFPPortSSMTx": sFPPortSSMTx,
       "auxPortSSMTx": auxPortSSMTx,
       "syncETrackingState": syncETrackingState,
       "mainPSUPortQLRx": mainPSUPortQLRx,
       "auxPortQLRx": auxPortQLRx,
       "sFPPortQLRx": sFPPortQLRx,
       "mainPSUPortQLTx": mainPSUPortQLTx,
       "auxPortQLTx": auxPortQLTx,
       "sFPPortQLTx": sFPPortQLTx,
       "mainPSUPortSyncEMasterSlaveStatus": mainPSUPortSyncEMasterSlaveStatus,
       "auxPortSyncEMasterSlaveStatus": auxPortSyncEMasterSlaveStatus,
       "sFPPortSyncEMasterSlaveStatus": sFPPortSyncEMasterSlaveStatus,
       "mainPSUPortGigabitMasterSlaveStatus": mainPSUPortGigabitMasterSlaveStatus,
       "auxPortGigabitMasterSlaveStatus": auxPortGigabitMasterSlaveStatus,
       "sFPPortGigabitMasterSlaveStatus": sFPPortGigabitMasterSlaveStatus,
       "transparentClock": transparentClock,
       "transparentClockVLAN": transparentClockVLAN,
       "transparentClockVID": transparentClockVID,
       "mainPSUPortAcceptedQLRx": mainPSUPortAcceptedQLRx,
       "auxPortAcceptedQLRx": auxPortAcceptedQLRx,
       "sFPPortAcceptedQLRx": sFPPortAcceptedQLRx,
       "mainPSUPortSyncERxStatus": mainPSUPortSyncERxStatus,
       "auxPortSyncERxStatus": auxPortSyncERxStatus,
       "sFPPortSyncERxStatus": sFPPortSyncERxStatus,
       "nIDULanPortStatus": nIDULanPortStatus,
       "nIDULanPortSpeedAndDuplex": nIDULanPortSpeedAndDuplex,
       "oOBPriorityQueueMapping": oOBPriorityQueueMapping,
       "nIDULanPortAutoNegotiation": nIDULanPortAutoNegotiation,
       "nIDULanPortAutoNegAdvertisement": nIDULanPortAutoNegAdvertisement,
       "nIDULanPortAutoMdix": nIDULanPortAutoMdix,
       "nIDULanPortGigabitMasterSlaveStatus": nIDULanPortGigabitMasterSlaveStatus,
       "txMABFrames": txMABFrames,
       "managementNetworkAccessEnabled": managementNetworkAccessEnabled,
       "secondDataPortPauseFrames": secondDataPortPauseFrames,
       "secondDataBridgingStatus": secondDataBridgingStatus,
       "transparentClockPort": transparentClockPort,
       "tDM": tDM,
       "tDMInterfaceControl": tDMInterfaceControl,
       "tDMInterfaceStatus": tDMInterfaceStatus,
       "tDMEnabledChannels": tDMEnabledChannels,
       "tdmTableNumber": tdmTableNumber,
       "tdmTable": tdmTable,
       "tdmTableEntry": tdmTableEntry,
       "tdmTableIndex": tdmTableIndex,
       "tDMChannelStatus": tDMChannelStatus,
       "tDMChannelLineCode": tDMChannelLineCode,
       "tDMChannelCableLength": tDMChannelCableLength,
       "tDMChannelLoopback": tDMChannelLoopback,
       "tDMConfigurationMismatch": tDMConfigurationMismatch,
       "lowestTDMModulationMode": lowestTDMModulationMode,
       "license": license,
       "regulatoryBand": regulatoryBand,
       "productVariant": productVariant,
       "productName": productName,
       "frequencyVariant": frequencyVariant,
       "sNMPv3Enable": sNMPv3Enable,
       "licenseVersion": licenseVersion,
       "licenseUnitSerialNumber": licenseUnitSerialNumber,
       "licenseIssueNumber": licenseIssueNumber,
       "licenseCountry": licenseCountry,
       "licenseNumberOfRegulatoryBands": licenseNumberOfRegulatoryBands,
       "licenseRegulatoryBandsTable": licenseRegulatoryBandsTable,
       "licenseRegulatoryBandsTableEntry": licenseRegulatoryBandsTableEntry,
       "licenseRegulatoryBandsTableIndex": licenseRegulatoryBandsTableIndex,
       "licenseRegulatoryBandsList": licenseRegulatoryBandsList,
       "licenseBandwidthCap": licenseBandwidthCap,
       "licenseEncryption": licenseEncryption,
       "licenseSecurityLevel": licenseSecurityLevel,
       "licenseGroupAccess": licenseGroupAccess,
       "licenseOOBManagementSupport": licenseOOBManagementSupport,
       "licenseSFPPortSupport": licenseSFPPortSupport,
       "licenseAuxiliaryPortSupport": licenseAuxiliaryPortSupport,
       "licenseCapacity": licenseCapacity,
       "licenseMaxNumberOfTDMChannels": licenseMaxNumberOfTDMChannels,
       "licenseIEEE1588Support": licenseIEEE1588Support,
       "licenseSyncESupport": licenseSyncESupport,
       "licenseIPv6Support": licenseIPv6Support,
       "licenseMinimumFirmwareVersion": licenseMinimumFirmwareVersion,
       "licenseFullCapabilityTrialStatus": licenseFullCapabilityTrialStatus,
       "licenseRemainingTrialPeriod": licenseRemainingTrialPeriod,
       "licenseRemainingTrialPeriodAlarm": licenseRemainingTrialPeriodAlarm,
       "capacityVariantMismatch": capacityVariantMismatch,
       "licenseTDDSyncSupport": licenseTDDSyncSupport,
       "licenseMaxLinkRange": licenseMaxLinkRange,
       "licenseTrialPeriod": licenseTrialPeriod,
       "licenseRARSupport": licenseRARSupport,
       "management": management,
       "targetRange": targetRange,
       "rangingMode": rangingMode,
       "installStatus": installStatus,
       "installArmState": installArmState,
       "tFTPServerPortNumber": tFTPServerPortNumber,
       "tFTPSoftwareUpgradeFileName": tFTPSoftwareUpgradeFileName,
       "tFTPStartSoftwareUpgrade": tFTPStartSoftwareUpgrade,
       "tFTPSoftwareUpgradeStatus": tFTPSoftwareUpgradeStatus,
       "tFTPSoftwareUpgradeStatusText": tFTPSoftwareUpgradeStatusText,
       "tFTPSoftwareUpgradeStatusAdditionalText": tFTPSoftwareUpgradeStatusAdditionalText,
       "hTTPAccessEnabled": hTTPAccessEnabled,
       "telnetAccessEnabled": telnetAccessEnabled,
       "hTTPPortNumber": hTTPPortNumber,
       "hTTPSPortNumber": hTTPSPortNumber,
       "telnetPortNumber": telnetPortNumber,
       "hTTPSAccessEnabled": hTTPSAccessEnabled,
       "tFTPServerInternetAddressType": tFTPServerInternetAddressType,
       "tFTPServerInternetAddress": tFTPServerInternetAddress,
       "lowestDataModulationMode": lowestDataModulationMode,
       "lowestSecondDataModulationMode": lowestSecondDataModulationMode,
       "phyControl": phyControl,
       "linkSymmetry": linkSymmetry,
       "userConfiguredMaxModulationMode": userConfiguredMaxModulationMode,
       "linkModeOptimization": linkModeOptimization,
       "txColorCode": txColorCode,
       "rxColorCode": rxColorCode,
       "remoteMaximumTransmitPower": remoteMaximumTransmitPower,
       "phyStatus": phyStatus,
       "linkLoss": linkLoss,
       "receivePower": receivePower,
       "vectorError": vectorError,
       "transmitPower": transmitPower,
       "receiveChannel": receiveChannel,
       "transmitChannel": transmitChannel,
       "receiveFreqMHz": receiveFreqMHz,
       "transmitFreqMHz": transmitFreqMHz,
       "signalStrengthRatio": signalStrengthRatio,
       "receiveFreqKHz": receiveFreqKHz,
       "transmitFreqKHz": transmitFreqKHz,
       "rawReceivePower": rawReceivePower,
       "range": range,
       "receiveModulationMode": receiveModulationMode,
       "transmitModulationMode": transmitModulationMode,
       "searchState": searchState,
       "alarms": alarms,
       "unitOutOfCalibration": unitOutOfCalibration,
       "incompatibleRegulatoryBands": incompatibleRegulatoryBands,
       "noWirelessChannelAvailable": noWirelessChannelAvailable,
       "wirelessLinkDisabledWarning": wirelessLinkDisabledWarning,
       "mainPSUPortDisabledWarning": mainPSUPortDisabledWarning,
       "sFPError": sFPError,
       "mainPSUPortConfigurationMismatch": mainPSUPortConfigurationMismatch,
       "incompatibleMasterAndSlave": incompatibleMasterAndSlave,
       "tDDSynchronizationStatus": tDDSynchronizationStatus,
       "auxPortDisabledWarning": auxPortDisabledWarning,
       "tDDSynchronizationAlarm": tDDSynchronizationAlarm,
       "linkModeOptimizationMismatch": linkModeOptimizationMismatch,
       "auxPortConfigurationMismatch": auxPortConfigurationMismatch,
       "secureModeAlarm": secureModeAlarm,
       "dataBridgingStatusAlarm": dataBridgingStatusAlarm,
       "sFPPortDisabledWarning": sFPPortDisabledWarning,
       "sFPPortConfigurationMismatch": sFPPortConfigurationMismatch,
       "maxLinkRangeExceeded": maxLinkRangeExceeded,
       "nIDULanPortDisabledWarning": nIDULanPortDisabledWarning,
       "nIDULanPortConfigurationMismatch": nIDULanPortConfigurationMismatch,
       "portAllocationMismatch": portAllocationMismatch,
       "secondDataBridgingStatusAlarm": secondDataBridgingStatusAlarm,
       "transparentClockSourcePortAlarm": transparentClockSourcePortAlarm,
       "smtp": smtp,
       "sMTPEmailAlert": sMTPEmailAlert,
       "sMTPServerPortNumber": sMTPServerPortNumber,
       "sMTPSourceEmailAddress": sMTPSourceEmailAddress,
       "sMTPDestinationEmailAddress": sMTPDestinationEmailAddress,
       "sMTPEnabledMessages": sMTPEnabledMessages,
       "sMTPServerInternetAddressType": sMTPServerInternetAddressType,
       "sMTPServerInternetAddress": sMTPServerInternetAddress,
       "snmpControl": snmpControl,
       "sNMPPortNumber": sNMPPortNumber,
       "sNMPCommunityString": sNMPCommunityString,
       "sNMPTrapTableNumber": sNMPTrapTableNumber,
       "sNMPTrapTable": sNMPTrapTable,
       "sNMPTrapTableEntry": sNMPTrapTableEntry,
       "sNMPTrapTableIndex": sNMPTrapTableIndex,
       "sNMPTrapPortNumber": sNMPTrapPortNumber,
       "sNMPTrapInternetAddressType": sNMPTrapInternetAddressType,
       "sNMPTrapInternetAddress": sNMPTrapInternetAddress,
       "sNMPTrapReceiverEnabled": sNMPTrapReceiverEnabled,
       "sNMPTrapVersion": sNMPTrapVersion,
       "sNMPEnabledTraps": sNMPEnabledTraps,
       "enabledDiagnosticAlarms": enabledDiagnosticAlarms,
       "sNMPSendAllTrapsAtStartup": sNMPSendAllTrapsAtStartup,
       "sntp": sntp,
       "sNTPState": sNTPState,
       "sNTPPollInterval": sNTPPollInterval,
       "sNTPSync": sNTPSync,
       "sNTPLastSync": sNTPLastSync,
       "systemClock": systemClock,
       "timeZone": timeZone,
       "daylightSaving": daylightSaving,
       "sNTPPrimaryServer": sNTPPrimaryServer,
       "sNTPPrimaryServerDeadTime": sNTPPrimaryServerDeadTime,
       "sNTPServerRetries": sNTPServerRetries,
       "sNTPServerTimeout": sNTPServerTimeout,
       "sNTPServerTableNumber": sNTPServerTableNumber,
       "sNTPServerTable": sNTPServerTable,
       "sNTPServerTableEntry": sNTPServerTableEntry,
       "sNTPServerTableIndex": sNTPServerTableIndex,
       "sNTPServerPortNumber": sNTPServerPortNumber,
       "sNTPServerStatus": sNTPServerStatus,
       "sNTPServerInternetAddressType": sNTPServerInternetAddressType,
       "sNTPServerInternetAddress": sNTPServerInternetAddress,
       "reset": reset,
       "systemReset": systemReset,
       "versions": versions,
       "softwareVersion": softwareVersion,
       "hardwareVersion": hardwareVersion,
       "secondarySoftwareVersion": secondarySoftwareVersion,
       "bootVersion": bootVersion,
       "pubStats": pubStats,
       "receiveDataRate": receiveDataRate,
       "transmitDataRate": transmitDataRate,
       "aggregateDataRate": aggregateDataRate,
       "wirelessLinkAvailability": wirelessLinkAvailability,
       "wirelessLinkStatus": wirelessLinkStatus,
       "byteErrorRatio": byteErrorRatio,
       "receiveModulationModeDetail": receiveModulationModeDetail,
       "dataBridgingAvailability": dataBridgingAvailability,
       "encryption": encryption,
       "encryptionAlgorithm": encryptionAlgorithm,
       "tDDControl": tDDControl,
       "tDDSynchronizationMode": tDDSynchronizationMode,
       "syslogControl": syslogControl,
       "syslogClient": syslogClient,
       "syslogState": syslogState,
       "aAAControl": aAAControl,
       "userTableNumber": userTableNumber,
       "userTable": userTable,
       "userTableEntry": userTableEntry,
       "userTableIndex": userTableIndex,
       "userName": userName,
       "userRole": userRole,
       "userEnabled": userEnabled,
       "userPassword": userPassword,
       "routerProtocols": routerProtocols,
       "microwaveAdaptiveBandwidth": microwaveAdaptiveBandwidth,
       "mABNominalModulationMode": mABNominalModulationMode,
       "mABTransmissionInterval": mABTransmissionInterval,
       "mABHoldoffPeriod": mABHoldoffPeriod,
       "mABMaintenanceLevel": mABMaintenanceLevel,
       "useVLANForMABProtocol": useVLANForMABProtocol,
       "mABProtocolVID": mABProtocolVID,
       "mABProtocolVLANPriority": mABProtocolVLANPriority,
       "mABState": mABState,
       "mABNominalTransmitCapacity": mABNominalTransmitCapacity,
       "mABCurrentTransmitCapacity": mABCurrentTransmitCapacity,
       "cableDiagnostics": cableDiagnostics,
       "cableDiagnosticsPorts": cableDiagnosticsPorts,
       "cableDiagnosticsControl": cableDiagnosticsControl,
       "cableDiagnosticsWarning": cableDiagnosticsWarning,
       "cableDiagnosticsResultTableNumber": cableDiagnosticsResultTableNumber,
       "cableDiagnosticsResultTable": cableDiagnosticsResultTable,
       "cableDiagnosticsResultTableEntry": cableDiagnosticsResultTableEntry,
       "cableDiagnosticsResultTableIndex": cableDiagnosticsResultTableIndex,
       "cableDiagnosticsResultsDateTime": cableDiagnosticsResultsDateTime,
       "cableDiagPair1Results": cableDiagPair1Results,
       "cableDiagPair1Distance": cableDiagPair1Distance,
       "cableDiagPair2Results": cableDiagPair2Results,
       "cableDiagPair2Distance": cableDiagPair2Distance,
       "cableDiagPair3Results": cableDiagPair3Results,
       "cableDiagPair3Distance": cableDiagPair3Distance,
       "cableDiagPair4Results": cableDiagPair4Results,
       "cableDiagPair4Distance": cableDiagPair4Distance,
       "supplementary": supplementary,
       "longitude": longitude,
       "latitude": latitude,
       "altitude": altitude,
       "ptpCompliance": ptpCompliance,
       "ptpGroups": ptpGroups,
       "dfsGroup": dfsGroup,
       "bridgeGroup": bridgeGroup,
       "configurationGroup": configurationGroup,
       "ethernetGroup": ethernetGroup,
       "tDMGroup": tDMGroup,
       "licenseGroup": licenseGroup,
       "managementGroup": managementGroup,
       "phyControlGroup": phyControlGroup,
       "phyStatusGroup": phyStatusGroup,
       "alarmsGroup": alarmsGroup,
       "smtpGroup": smtpGroup,
       "snmpControlGroup": snmpControlGroup,
       "sntpGroup": sntpGroup,
       "resetGroup": resetGroup,
       "versionsGroup": versionsGroup,
       "pubStatsGroup": pubStatsGroup,
       "encryptionGroup": encryptionGroup,
       "tDDControlGroup": tDDControlGroup,
       "syslogControlGroup": syslogControlGroup,
       "aAAControlGroup": aAAControlGroup,
       "routerProtocolsGroup": routerProtocolsGroup,
       "cableDiagnosticsGroup": cableDiagnosticsGroup,
       "supplementaryGroup": supplementaryGroup,
       "notificationsGroup": notificationsGroup,
       "ptpTraps": ptpTraps,
       "ptpTrapPrefix": ptpTrapPrefix,
       "channelChangeTrap": channelChangeTrap,
       "dfsImpulsiveInterferenceTrap": dfsImpulsiveInterferenceTrap,
       "mainPSUPortStatusTrap": mainPSUPortStatusTrap,
       "mainPSUPortDisabledWarningTrap": mainPSUPortDisabledWarningTrap,
       "mainPSUPortConfigurationMismatchTrap": mainPSUPortConfigurationMismatchTrap,
       "auxPortStatusTrap": auxPortStatusTrap,
       "auxPortDisabledWarningTrap": auxPortDisabledWarningTrap,
       "regulatoryBandTrap": regulatoryBandTrap,
       "installStatusTrap": installStatusTrap,
       "installArmStateTrap": installArmStateTrap,
       "unitOutOfCalibrationTrap": unitOutOfCalibrationTrap,
       "auxPortPowerOverEthernetOutputStatusTrap": auxPortPowerOverEthernetOutputStatusTrap,
       "incompatibleRegulatoryBandsTrap": incompatibleRegulatoryBandsTrap,
       "noWirelessChannelAvailableTrap": noWirelessChannelAvailableTrap,
       "wirelessLinkDisabledWarningTrap": wirelessLinkDisabledWarningTrap,
       "auxPortConfigurationMismatchTrap": auxPortConfigurationMismatchTrap,
       "sFPErrorTrap": sFPErrorTrap,
       "sFPPortStatusTrap": sFPPortStatusTrap,
       "incompatibleMasterAndSlaveTrap": incompatibleMasterAndSlaveTrap,
       "sNTPSyncTrap": sNTPSyncTrap,
       "tDDSynchronizationAlarmTrap": tDDSynchronizationAlarmTrap,
       "sFPPortDisabledWarningTrap": sFPPortDisabledWarningTrap,
       "sFPPortConfigurationMismatchTrap": sFPPortConfigurationMismatchTrap,
       "linkModeOptimizationMismatchTrap": linkModeOptimizationMismatchTrap,
       "tDMInterfaceStatusTrap": tDMInterfaceStatusTrap,
       "tDMChannelStatusTrap": tDMChannelStatusTrap,
       "tDMChannelLoopbackTrap": tDMChannelLoopbackTrap,
       "nIDULanPortStatusTrap": nIDULanPortStatusTrap,
       "syslogStateTrap": syslogStateTrap,
       "syslogLocalNearlyFullTrap": syslogLocalNearlyFullTrap,
       "syslogLocalWrappedTrap": syslogLocalWrappedTrap,
       "syslogClientTrap": syslogClientTrap,
       "secureModeAlarmTrap": secureModeAlarmTrap,
       "dataBridgingStatusAlarmTrap": dataBridgingStatusAlarmTrap,
       "licenseRemainingTrialPeriodAlarmTrap": licenseRemainingTrialPeriodAlarmTrap,
       "capacityVariantMismatchTrap": capacityVariantMismatchTrap,
       "maxLinkRangeExceededTrap": maxLinkRangeExceededTrap,
       "tDMConfigurationMismatchTrap": tDMConfigurationMismatchTrap,
       "nIDULanPortDisabledWarningTrap": nIDULanPortDisabledWarningTrap,
       "nIDULanPortConfigurationMismatchTrap": nIDULanPortConfigurationMismatchTrap,
       "secondDataBridgingStatusAlarmTrap": secondDataBridgingStatusAlarmTrap,
       "transparentClockSourcePortAlarmTrap": transparentClockSourcePortAlarmTrap,
       "portAllocationMismatchTrap": portAllocationMismatchTrap}
)
