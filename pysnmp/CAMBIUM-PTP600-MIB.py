# SNMP MIB module (CAMBIUM-PTP600-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAMBIUM-PTP600-MIB
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
        ("2012-12-17 13:30",
         "2012-05-01 11:58",
         "2012-02-13 12:38",
         "2011-11-08 13:47",
         "2010-12-07 13:28",
         "2010-11-02 13:33",
         "2010-07-16 15:41",
         "2010-04-23 10:07",
         "2010-02-19 18:55",
         "2009-07-10 15:20",
         "2009-02-27 17:11",
         "2008-12-15 12:19",
         "2008-06-30 10:16",
         "2008-02-29 09:42",
         "2007-07-31 18:39",
         "2006-11-23 14:36",
         "2006-07-24 10:08")
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
_Ptp600_ObjectIdentity = ObjectIdentity
ptp600 = _Ptp600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6)
)
_Dfs_ObjectIdentity = ObjectIdentity
dfs = _Dfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 3)
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 3, 1),
    _DfsTableNumber_Type()
)
dfsTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsTableNumber.setStatus("current")
_DfsTable_Object = MibTable
dfsTable = _DfsTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 3, 2)
)
if mibBuilder.loadTexts:
    dfsTable.setStatus("current")
_DfsTableEntry_Object = MibTableRow
dfsTableEntry = _DfsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 3, 2, 1)
)
dfsTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP600-MIB", "dfsTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 3, 2, 1, 1),
    _DfsTableIndex_Type()
)
dfsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfsTableIndex.setStatus("current")
_DfsMeans_Type = Integer32
_DfsMeans_Object = MibTableColumn
dfsMeans = _DfsMeans_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 3, 2, 1, 2),
    _DfsMeans_Type()
)
dfsMeans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsMeans.setStatus("current")
_DfsNineNinePointNinePercentiles_Type = Integer32
_DfsNineNinePointNinePercentiles_Object = MibTableColumn
dfsNineNinePointNinePercentiles = _DfsNineNinePointNinePercentiles_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 3, 2, 1, 3),
    _DfsNineNinePointNinePercentiles_Type()
)
dfsNineNinePointNinePercentiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsNineNinePointNinePercentiles.setStatus("current")
_DfsPeaks_Type = Integer32
_DfsPeaks_Object = MibTableColumn
dfsPeaks = _DfsPeaks_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 3, 2, 1, 4),
    _DfsPeaks_Type()
)
dfsPeaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsPeaks.setStatus("current")
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 4)
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 4, 1),
    _LocalPacketFiltering_Type()
)
localPacketFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localPacketFiltering.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 5)
)
_IPAddress_Type = IpAddress
_IPAddress_Object = MibScalar
iPAddress = _IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 1),
    _IPAddress_Type()
)
iPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_GatewayIPAddress_Type = IpAddress
_GatewayIPAddress_Object = MibScalar
gatewayIPAddress = _GatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 5),
    _MasterSlaveMode_Type()
)
masterSlaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterSlaveMode.setStatus("current")


class _MaximumTransmitPower_Type(Integer32):
    """Custom type maximumTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 27),
    )


_MaximumTransmitPower_Type.__name__ = "Integer32"
_MaximumTransmitPower_Object = MibScalar
maximumTransmitPower = _MaximumTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 6),
    _MaximumTransmitPower_Type()
)
maximumTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumTransmitPower.setStatus("current")


class _AntennaGain_Type(Integer32):
    """Custom type antennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 610),
    )


_AntennaGain_Type.__name__ = "Integer32"
_AntennaGain_Object = MibScalar
antennaGain = _AntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 7),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 8),
    _CableLoss_Type()
)
cableLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableLoss.setStatus("current")
_EIRP_Type = Integer32
_EIRP_Object = MibScalar
eIRP = _EIRP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 9),
    _EIRP_Type()
)
eIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eIRP.setStatus("current")


class _EthernetCappedMaxWirelessSpeed_Type(Integer32):
    """Custom type ethernetCappedMaxWirelessSpeed based on Integer32"""
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


_EthernetCappedMaxWirelessSpeed_Type.__name__ = "Integer32"
_EthernetCappedMaxWirelessSpeed_Object = MibScalar
ethernetCappedMaxWirelessSpeed = _EthernetCappedMaxWirelessSpeed_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 10),
    _EthernetCappedMaxWirelessSpeed_Type()
)
ethernetCappedMaxWirelessSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetCappedMaxWirelessSpeed.setStatus("current")


class _ChannelBandwidth_Type(Integer32):
    """Custom type channelBandwidth based on Integer32"""
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
        *(("bw10MHz", 2),
          ("bw15MHz", 1),
          ("bw20MHz", 4),
          ("bw30MHz", 0),
          ("bw5MHz", 3))
    )


_ChannelBandwidth_Type.__name__ = "Integer32"
_ChannelBandwidth_Object = MibScalar
channelBandwidth = _ChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 11),
    _ChannelBandwidth_Type()
)
channelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBandwidth.setStatus("current")
_RemoteIPAddress_Type = IpAddress
_RemoteIPAddress_Object = MibScalar
remoteIPAddress = _RemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 12),
    _RemoteIPAddress_Type()
)
remoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIPAddress.setStatus("current")


class _LinkName_Type(DisplayString):
    """Custom type linkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LinkName_Type.__name__ = "DisplayString"
_LinkName_Object = MibScalar
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 14),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 15),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 16),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 5, 17),
    _GroupID_Type()
)
groupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupID.setStatus("current")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6)
)


class _DataPortAutoNegotiation_Type(Integer32):
    """Custom type dataPortAutoNegotiation based on Integer32"""
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


_DataPortAutoNegotiation_Type.__name__ = "Integer32"
_DataPortAutoNegotiation_Object = MibScalar
dataPortAutoNegotiation = _DataPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 1),
    _DataPortAutoNegotiation_Type()
)
dataPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortAutoNegotiation.setStatus("current")


class _DataPortAutoNegAdvertisement_Type(Bits):
    """Custom type dataPortAutoNegAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("neg1000MbpsFullDuplex", 7),
          ("neg100MbpsFullDuplex", 6),
          ("neg100MbpsHalfDuplex", 5),
          ("neg10MbpsFullDuplex", 4),
          ("neg10MbpsHalfDuplex", 3),
          ("negInvalid", 2))
    )

_DataPortAutoNegAdvertisement_Type.__name__ = "Bits"
_DataPortAutoNegAdvertisement_Object = MibScalar
dataPortAutoNegAdvertisement = _DataPortAutoNegAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 2),
    _DataPortAutoNegAdvertisement_Type()
)
dataPortAutoNegAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortAutoNegAdvertisement.setStatus("current")


class _DataPortAutoMdix_Type(Integer32):
    """Custom type dataPortAutoMdix based on Integer32"""
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


_DataPortAutoMdix_Type.__name__ = "Integer32"
_DataPortAutoMdix_Object = MibScalar
dataPortAutoMdix = _DataPortAutoMdix_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 3),
    _DataPortAutoMdix_Type()
)
dataPortAutoMdix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortAutoMdix.setStatus("current")


class _DataPortStatus_Type(Integer32):
    """Custom type dataPortStatus based on Integer32"""
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


_DataPortStatus_Type.__name__ = "Integer32"
_DataPortStatus_Object = MibScalar
dataPortStatus = _DataPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 4),
    _DataPortStatus_Type()
)
dataPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortStatus.setStatus("current")


class _DataPortSpeedAndDuplex_Type(Integer32):
    """Custom type dataPortSpeedAndDuplex based on Integer32"""
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


_DataPortSpeedAndDuplex_Type.__name__ = "Integer32"
_DataPortSpeedAndDuplex_Object = MibScalar
dataPortSpeedAndDuplex = _DataPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 5),
    _DataPortSpeedAndDuplex_Type()
)
dataPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortSpeedAndDuplex.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 6),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 7),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 8),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 11),
    _VLANManagementVID_Type()
)
vLANManagementVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANManagementVID.setStatus("current")


class _ManagementPortStatus_Type(Integer32):
    """Custom type managementPortStatus based on Integer32"""
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


_ManagementPortStatus_Type.__name__ = "Integer32"
_ManagementPortStatus_Object = MibScalar
managementPortStatus = _ManagementPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 12),
    _ManagementPortStatus_Type()
)
managementPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementPortStatus.setStatus("current")


class _ManagementPortSpeedAndDuplex_Type(Integer32):
    """Custom type managementPortSpeedAndDuplex based on Integer32"""
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
        *(("speed100MbpsFullDuplex", 1),
          ("speed100MbpsHalfDuplex", 2),
          ("speed10MbpsFullDuplex", 3),
          ("speed10MbpsHalfDuplex", 4),
          ("speedUnknown6", 5))
    )


_ManagementPortSpeedAndDuplex_Type.__name__ = "Integer32"
_ManagementPortSpeedAndDuplex_Object = MibScalar
managementPortSpeedAndDuplex = _ManagementPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 13),
    _ManagementPortSpeedAndDuplex_Type()
)
managementPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementPortSpeedAndDuplex.setStatus("current")


class _EthernetPriorityTableNumber_Type(Integer32):
    """Custom type ethernetPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 9),
    )


_EthernetPriorityTableNumber_Type.__name__ = "Integer32"
_EthernetPriorityTableNumber_Object = MibScalar
ethernetPriorityTableNumber = _EthernetPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 14),
    _EthernetPriorityTableNumber_Type()
)
ethernetPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPriorityTableNumber.setStatus("current")
_EthernetPriorityTable_Object = MibTable
ethernetPriorityTable = _EthernetPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 15)
)
if mibBuilder.loadTexts:
    ethernetPriorityTable.setStatus("current")
_EthernetPriorityTableEntry_Object = MibTableRow
ethernetPriorityTableEntry = _EthernetPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 15, 1)
)
ethernetPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP600-MIB", "ethernetPriorityTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 15, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 15, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 16),
    _L2CPPriorityTableNumber_Type()
)
l2CPPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2CPPriorityTableNumber.setStatus("current")
_L2CPPriorityTable_Object = MibTable
l2CPPriorityTable = _L2CPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 17)
)
if mibBuilder.loadTexts:
    l2CPPriorityTable.setStatus("current")
_L2CPPriorityTableEntry_Object = MibTableRow
l2CPPriorityTableEntry = _L2CPPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 17, 1)
)
l2CPPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP600-MIB", "l2CPPriorityTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 17, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 17, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 18),
    _IPDSCPPriorityTableNumber_Type()
)
iPDSCPPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPDSCPPriorityTableNumber.setStatus("current")
_IPDSCPPriorityTable_Object = MibTable
iPDSCPPriorityTable = _IPDSCPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 19)
)
if mibBuilder.loadTexts:
    iPDSCPPriorityTable.setStatus("current")
_IPDSCPPriorityTableEntry_Object = MibTableRow
iPDSCPPriorityTableEntry = _IPDSCPPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 19, 1)
)
iPDSCPPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP600-MIB", "iPDSCPPriorityTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 19, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 19, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 20),
    _MPLSTCPriorityTableNumber_Type()
)
mPLSTCPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPLSTCPriorityTableNumber.setStatus("current")
_MPLSTCPriorityTable_Object = MibTable
mPLSTCPriorityTable = _MPLSTCPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 21)
)
if mibBuilder.loadTexts:
    mPLSTCPriorityTable.setStatus("current")
_MPLSTCPriorityTableEntry_Object = MibTableRow
mPLSTCPriorityTableEntry = _MPLSTCPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 21, 1)
)
mPLSTCPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP600-MIB", "mPLSTCPriorityTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 21, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 21, 1, 2),
    _MPLSTCPriorityQueueMapping_Type()
)
mPLSTCPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mPLSTCPriorityQueueMapping.setStatus("current")


class _ManagementMode_Type(Integer32):
    """Custom type managementMode based on Integer32"""
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
        *(("inBand", 2),
          ("inBandLocal", 3),
          ("outofBand", 1),
          ("outofBandLocal", 0))
    )


_ManagementMode_Type.__name__ = "Integer32"
_ManagementMode_Object = MibScalar
managementMode = _ManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 22),
    _ManagementMode_Type()
)
managementMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementMode.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 23),
    _ManagementPortWirelessDownAlert_Type()
)
managementPortWirelessDownAlert.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 24),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 25),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 26),
    _DSCPManagementPriority_Type()
)
dSCPManagementPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSCPManagementPriority.setStatus("current")


class _EthernetBridgingStatus_Type(Integer32):
    """Custom type ethernetBridgingStatus based on Integer32"""
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


_EthernetBridgingStatus_Type.__name__ = "Integer32"
_EthernetBridgingStatus_Object = MibScalar
ethernetBridgingStatus = _EthernetBridgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 6, 27),
    _EthernetBridgingStatus_Type()
)
ethernetBridgingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetBridgingStatus.setStatus("current")
_Telecom_ObjectIdentity = ObjectIdentity
telecom = _Telecom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 7)
)


class _TelecomsInterface_Type(Integer32):
    """Custom type telecomsInterface based on Integer32"""
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


_TelecomsInterface_Type.__name__ = "Integer32"
_TelecomsInterface_Object = MibScalar
telecomsInterface = _TelecomsInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 7, 1),
    _TelecomsInterface_Type()
)
telecomsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telecomsInterface.setStatus("current")


class _TelecomsChannelAStatus_Type(Integer32):
    """Custom type telecomsChannelAStatus based on Integer32"""
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
        *(("disabled", 0),
          ("noSignalLocal", 1),
          ("noSignalLocalandRemote", 3),
          ("noSignalLocalandRemoteTiming", 6),
          ("noSignalRemote", 2),
          ("remoteTiming", 5),
          ("up", 4))
    )


_TelecomsChannelAStatus_Type.__name__ = "Integer32"
_TelecomsChannelAStatus_Object = MibScalar
telecomsChannelAStatus = _TelecomsChannelAStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 7, 2),
    _TelecomsChannelAStatus_Type()
)
telecomsChannelAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telecomsChannelAStatus.setStatus("current")


class _TelecomsChannelBStatus_Type(Integer32):
    """Custom type telecomsChannelBStatus based on Integer32"""
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
        *(("disabled", 0),
          ("noSignalLocal", 1),
          ("noSignalLocalandRemote", 3),
          ("noSignalLocalandRemoteTiming", 6),
          ("noSignalRemote", 2),
          ("remoteTiming", 5),
          ("up", 4))
    )


_TelecomsChannelBStatus_Type.__name__ = "Integer32"
_TelecomsChannelBStatus_Object = MibScalar
telecomsChannelBStatus = _TelecomsChannelBStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 7, 3),
    _TelecomsChannelBStatus_Type()
)
telecomsChannelBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telecomsChannelBStatus.setStatus("current")


class _ChannelALineCode_Type(Integer32):
    """Custom type channelALineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 0),
          ("b8ZSHDB3", 1))
    )


_ChannelALineCode_Type.__name__ = "Integer32"
_ChannelALineCode_Object = MibScalar
channelALineCode = _ChannelALineCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 7, 4),
    _ChannelALineCode_Type()
)
channelALineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelALineCode.setStatus("current")


class _ChannelBLineCode_Type(Integer32):
    """Custom type channelBLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 0),
          ("b8ZSHDB3", 1))
    )


_ChannelBLineCode_Type.__name__ = "Integer32"
_ChannelBLineCode_Object = MibScalar
channelBLineCode = _ChannelBLineCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 7, 5),
    _ChannelBLineCode_Type()
)
channelBLineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBLineCode.setStatus("current")


class _ChannelACableLength_Type(Integer32):
    """Custom type channelACableLength based on Integer32"""
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


_ChannelACableLength_Type.__name__ = "Integer32"
_ChannelACableLength_Object = MibScalar
channelACableLength = _ChannelACableLength_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 7, 6),
    _ChannelACableLength_Type()
)
channelACableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelACableLength.setStatus("current")


class _ChannelBCableLength_Type(Integer32):
    """Custom type channelBCableLength based on Integer32"""
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


_ChannelBCableLength_Type.__name__ = "Integer32"
_ChannelBCableLength_Object = MibScalar
channelBCableLength = _ChannelBCableLength_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 7, 7),
    _ChannelBCableLength_Type()
)
channelBCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBCableLength.setStatus("current")


class _ChannelALoopback_Type(Integer32):
    """Custom type channelALoopback based on Integer32"""
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


_ChannelALoopback_Type.__name__ = "Integer32"
_ChannelALoopback_Object = MibScalar
channelALoopback = _ChannelALoopback_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 7, 8),
    _ChannelALoopback_Type()
)
channelALoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelALoopback.setStatus("current")


class _ChannelBLoopback_Type(Integer32):
    """Custom type channelBLoopback based on Integer32"""
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


_ChannelBLoopback_Type.__name__ = "Integer32"
_ChannelBLoopback_Object = MibScalar
channelBLoopback = _ChannelBLoopback_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 7, 9),
    _ChannelBLoopback_Type()
)
channelBLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBLoopback.setStatus("current")


class _TelecomsChannelSelection_Type(Integer32):
    """Custom type telecomsChannelSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("channelAOnly", 0),
          ("channelsAandB", 1))
    )


_TelecomsChannelSelection_Type.__name__ = "Integer32"
_TelecomsChannelSelection_Object = MibScalar
telecomsChannelSelection = _TelecomsChannelSelection_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 7, 10),
    _TelecomsChannelSelection_Type()
)
telecomsChannelSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telecomsChannelSelection.setStatus("current")
_Licence_ObjectIdentity = ObjectIdentity
licence = _Licence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 8)
)


class _RegionCode_Type(Integer32):
    """Custom type regionCode based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("regionCode1", 1),
          ("regionCode10", 10),
          ("regionCode11", 11),
          ("regionCode12", 12),
          ("regionCode13", 13),
          ("regionCode14", 14),
          ("regionCode15", 15),
          ("regionCode16", 16),
          ("regionCode17", 17),
          ("regionCode18", 18),
          ("regionCode19", 19),
          ("regionCode2", 2),
          ("regionCode20", 20),
          ("regionCode21", 21),
          ("regionCode22", 22),
          ("regionCode23", 23),
          ("regionCode24", 24),
          ("regionCode25", 25),
          ("regionCode26", 26),
          ("regionCode27", 27),
          ("regionCode28", 28),
          ("regionCode29", 29),
          ("regionCode3", 3),
          ("regionCode30", 30),
          ("regionCode31", 31),
          ("regionCode4", 4),
          ("regionCode5", 5),
          ("regionCode6", 6),
          ("regionCode7", 7),
          ("regionCode8", 8),
          ("regionCode9", 9),
          ("regionCodeInvalid", 0))
    )


_RegionCode_Type.__name__ = "Integer32"
_RegionCode_Object = MibScalar
regionCode = _RegionCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 8, 1),
    _RegionCode_Type()
)
regionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regionCode.setStatus("current")


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
          ("spare1", 4),
          ("spare2", 6),
          ("spare3", 7),
          ("spare5", 13),
          ("spare6", 14))
    )


_ProductVariant_Type.__name__ = "Integer32"
_ProductVariant_Object = MibScalar
productVariant = _ProductVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 8, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 8, 3),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")


class _EthernetFiberSupport_Type(Integer32):
    """Custom type ethernetFiberSupport based on Integer32"""
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


_EthernetFiberSupport_Type.__name__ = "Integer32"
_EthernetFiberSupport_Object = MibScalar
ethernetFiberSupport = _EthernetFiberSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 8, 4),
    _EthernetFiberSupport_Type()
)
ethernetFiberSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetFiberSupport.setStatus("current")


class _FrequencyVariant_Type(Integer32):
    """Custom type frequencyVariant based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("freq2500MHz", 3),
          ("freq4500MHz", 6),
          ("freq4800MHz", 10),
          ("freq4900MHz", 2),
          ("freq5100MHz", 9),
          ("freq5200MHz", 8),
          ("freq5400MHz", 1),
          ("freq5400MHz2", 5),
          ("freq5800MHz", 0),
          ("freq5800MHz2", 4),
          ("freq5900MHz", 7))
    )


_FrequencyVariant_Type.__name__ = "Integer32"
_FrequencyVariant_Object = MibScalar
frequencyVariant = _FrequencyVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 8, 5),
    _FrequencyVariant_Type()
)
frequencyVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyVariant.setStatus("current")


class _BandwidthVariant_Type(Integer32):
    """Custom type bandwidthVariant based on Integer32"""
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
        *(("bw10MHz", 2),
          ("bw15MHz", 1),
          ("bw20MHz", 4),
          ("bw30MHz", 0),
          ("bw5MHz", 3))
    )


_BandwidthVariant_Type.__name__ = "Integer32"
_BandwidthVariant_Object = MibScalar
bandwidthVariant = _BandwidthVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 8, 6),
    _BandwidthVariant_Type()
)
bandwidthVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthVariant.setStatus("current")


class _ConstantPowerSpectralDensity_Type(Integer32):
    """Custom type constantPowerSpectralDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("constant", 0),
          ("fullPower", 1))
    )


_ConstantPowerSpectralDensity_Type.__name__ = "Integer32"
_ConstantPowerSpectralDensity_Object = MibScalar
constantPowerSpectralDensity = _ConstantPowerSpectralDensity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 8, 7),
    _ConstantPowerSpectralDensity_Type()
)
constantPowerSpectralDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    constantPowerSpectralDensity.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 6, 8, 9),
    _SNMPv3Enable_Type()
)
sNMPv3Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPv3Enable.setStatus("current")


class _HAZLOCConfiguration_Type(Integer32):
    """Custom type hAZLOCConfiguration based on Integer32"""
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
        *(("gasGroupA", 1),
          ("gasGroupB", 2),
          ("gasGroupC", 3),
          ("gasGroupD", 4),
          ("nonHAZLOCUnit", 0))
    )


_HAZLOCConfiguration_Type.__name__ = "Integer32"
_HAZLOCConfiguration_Object = MibScalar
hAZLOCConfiguration = _HAZLOCConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 8, 10),
    _HAZLOCConfiguration_Type()
)
hAZLOCConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hAZLOCConfiguration.setStatus("current")


class _SecurityLevel_Type(Integer32):
    """Custom type securityLevel based on Integer32"""
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


_SecurityLevel_Type.__name__ = "Integer32"
_SecurityLevel_Object = MibScalar
securityLevel = _SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 8, 11),
    _SecurityLevel_Type()
)
securityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityLevel.setStatus("current")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 9)
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 4),
    _InstallArmState_Type()
)
installArmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installArmState.setStatus("current")
_TFTPServerIPAddress_Type = IpAddress
_TFTPServerIPAddress_Object = MibScalar
tFTPServerIPAddress = _TFTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 5),
    _TFTPServerIPAddress_Type()
)
tFTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPServerIPAddress.setStatus("current")


class _TFTPServerPortNumber_Type(Integer32):
    """Custom type tFTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TFTPServerPortNumber_Type.__name__ = "Integer32"
_TFTPServerPortNumber_Object = MibScalar
tFTPServerPortNumber = _TFTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 6),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 7),
    _TFTPSoftwareUpgradeFileName_Type()
)
tFTPSoftwareUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeFileName.setStatus("current")
_TFTPStartSoftwareUpgrade_Type = Integer32
_TFTPStartSoftwareUpgrade_Object = MibScalar
tFTPStartSoftwareUpgrade = _TFTPStartSoftwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 8),
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
              4)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("upgradefailed", 4),
          ("upgradesuccessfulreboottorunthenewsoftwareimage", 3),
          ("uploadinprogress", 1),
          ("uploadsuccessfulprogrammingFLASH", 2))
    )


_TFTPSoftwareUpgradeStatus_Type.__name__ = "Integer32"
_TFTPSoftwareUpgradeStatus_Object = MibScalar
tFTPSoftwareUpgradeStatus = _TFTPSoftwareUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 9),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 10),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 11),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 12),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 13),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 14),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 15),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 16),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 9, 17),
    _HTTPSAccessEnabled_Type()
)
hTTPSAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPSAccessEnabled.setStatus("current")
_PhyControl_ObjectIdentity = ObjectIdentity
phyControl = _PhyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 10)
)


class _LinkSymmetry_Type(Integer32):
    """Custom type linkSymmetry based on Integer32"""
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
        *(("symmetry1to1", 2),
          ("symmetry1to2", 3),
          ("symmetry2to1", 1),
          ("symmetryAdaptive", 0))
    )


_LinkSymmetry_Type.__name__ = "Integer32"
_LinkSymmetry_Object = MibScalar
linkSymmetry = _LinkSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 10, 1),
    _LinkSymmetry_Type()
)
linkSymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSymmetry.setStatus("current")


class _LinkModeOptimisation_Type(Integer32):
    """Custom type linkModeOptimisation based on Integer32"""
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


_LinkModeOptimisation_Type.__name__ = "Integer32"
_LinkModeOptimisation_Object = MibScalar
linkModeOptimisation = _LinkModeOptimisation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 10, 2),
    _LinkModeOptimisation_Type()
)
linkModeOptimisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkModeOptimisation.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 6, 10, 3),
    _UserConfiguredMaxModulationMode_Type()
)
userConfiguredMaxModulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userConfiguredMaxModulationMode.setStatus("current")


class _RemoteMaximumTransmitPower_Type(Integer32):
    """Custom type remoteMaximumTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 27),
    )


_RemoteMaximumTransmitPower_Type.__name__ = "Integer32"
_RemoteMaximumTransmitPower_Object = MibScalar
remoteMaximumTransmitPower = _RemoteMaximumTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 10, 4),
    _RemoteMaximumTransmitPower_Type()
)
remoteMaximumTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMaximumTransmitPower.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 6, 10, 5),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 10, 6),
    _RxColorCode_Type()
)
rxColorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxColorCode.setStatus("current")


class _AutomaticTxPowerControl_Type(Integer32):
    """Custom type automaticTxPowerControl based on Integer32"""
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
          ("enabledwithinitialestimate", 2))
    )


_AutomaticTxPowerControl_Type.__name__ = "Integer32"
_AutomaticTxPowerControl_Object = MibScalar
automaticTxPowerControl = _AutomaticTxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 10, 8),
    _AutomaticTxPowerControl_Type()
)
automaticTxPowerControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automaticTxPowerControl.setStatus("current")


class _RemoteRxTargetPower_Type(Integer32):
    """Custom type remoteRxTargetPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, -400),
    )


_RemoteRxTargetPower_Type.__name__ = "Integer32"
_RemoteRxTargetPower_Object = MibScalar
remoteRxTargetPower = _RemoteRxTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 10, 9),
    _RemoteRxTargetPower_Type()
)
remoteRxTargetPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteRxTargetPower.setStatus("current")
_PhyStatus_ObjectIdentity = ObjectIdentity
phyStatus = _PhyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12)
)
_ReceivePower_Type = Integer32
_ReceivePower_Object = MibScalar
receivePower = _ReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 1),
    _ReceivePower_Type()
)
receivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivePower.setStatus("current")
_VectorError_Type = Integer32
_VectorError_Object = MibScalar
vectorError = _VectorError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 2),
    _VectorError_Type()
)
vectorError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vectorError.setStatus("current")
_TransmitPower_Type = Integer32
_TransmitPower_Object = MibScalar
transmitPower = _TransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 3),
    _TransmitPower_Type()
)
transmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitPower.setStatus("current")
_Range_Type = Integer32
_Range_Object = MibScalar
range = _Range_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 4),
    _Range_Type()
)
range.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range.setStatus("current")


class _LinkLoss_Type(Integer32):
    """Custom type linkLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_LinkLoss_Type.__name__ = "Integer32"
_LinkLoss_Object = MibScalar
linkLoss = _LinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 5),
    _LinkLoss_Type()
)
linkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLoss.setStatus("current")


class _ReceiveChannel_Type(Integer32):
    """Custom type receiveChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ReceiveChannel_Type.__name__ = "Integer32"
_ReceiveChannel_Object = MibScalar
receiveChannel = _ReceiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 6),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 7),
    _TransmitChannel_Type()
)
transmitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitChannel.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 8),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 9),
    _TransmitModulationMode_Type()
)
transmitModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitModulationMode.setStatus("current")


class _ReceiveFreqMHz_Type(Integer32):
    """Custom type receiveFreqMHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5925),
    )


_ReceiveFreqMHz_Type.__name__ = "Integer32"
_ReceiveFreqMHz_Object = MibScalar
receiveFreqMHz = _ReceiveFreqMHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 11),
    _ReceiveFreqMHz_Type()
)
receiveFreqMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveFreqMHz.setStatus("current")


class _TransmitFreqMHz_Type(Integer32):
    """Custom type transmitFreqMHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5925),
    )


_TransmitFreqMHz_Type.__name__ = "Integer32"
_TransmitFreqMHz_Object = MibScalar
transmitFreqMHz = _TransmitFreqMHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 12),
    _TransmitFreqMHz_Type()
)
transmitFreqMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitFreqMHz.setStatus("current")
_SignalStrengthRatio_Type = Integer32
_SignalStrengthRatio_Object = MibScalar
signalStrengthRatio = _SignalStrengthRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 13),
    _SignalStrengthRatio_Type()
)
signalStrengthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalStrengthRatio.setStatus("current")


class _ReceiveFreqKHz_Type(Integer32):
    """Custom type receiveFreqKHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5925000),
    )


_ReceiveFreqKHz_Type.__name__ = "Integer32"
_ReceiveFreqKHz_Object = MibScalar
receiveFreqKHz = _ReceiveFreqKHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 14),
    _ReceiveFreqKHz_Type()
)
receiveFreqKHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveFreqKHz.setStatus("current")


class _TransmitFreqKHz_Type(Integer32):
    """Custom type transmitFreqKHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5925000),
    )


_TransmitFreqKHz_Type.__name__ = "Integer32"
_TransmitFreqKHz_Object = MibScalar
transmitFreqKHz = _TransmitFreqKHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 15),
    _TransmitFreqKHz_Type()
)
transmitFreqKHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitFreqKHz.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 16),
    _SearchState_Type()
)
searchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    searchState.setStatus("current")
_RawReceivePower_Type = Integer32
_RawReceivePower_Object = MibScalar
rawReceivePower = _RawReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 12, 17),
    _RawReceivePower_Type()
)
rawReceivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawReceivePower.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13)
)


class _UnitOutOfCalibration_Type(Integer32):
    """Custom type unitOutOfCalibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("calibrated", 0),
          ("outOfCalibration", 1),
          ("outOfCalibrationPAsShutdown", 2))
    )


_UnitOutOfCalibration_Type.__name__ = "Integer32"
_UnitOutOfCalibration_Object = MibScalar
unitOutOfCalibration = _UnitOutOfCalibration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 1),
    _UnitOutOfCalibration_Type()
)
unitOutOfCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitOutOfCalibration.setStatus("current")


class _EncryptionEnabledMismatch_Type(Integer32):
    """Custom type encryptionEnabledMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encryptionEnabledMismatch", 1),
          ("ok", 0))
    )


_EncryptionEnabledMismatch_Type.__name__ = "Integer32"
_EncryptionEnabledMismatch_Object = MibScalar
encryptionEnabledMismatch = _EncryptionEnabledMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 3),
    _EncryptionEnabledMismatch_Type()
)
encryptionEnabledMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionEnabledMismatch.setStatus("current")


class _IncompatibleRegionCodes_Type(Integer32):
    """Custom type incompatibleRegionCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("incompatibleLicenceKeys", 1),
          ("ok", 0))
    )


_IncompatibleRegionCodes_Type.__name__ = "Integer32"
_IncompatibleRegionCodes_Object = MibScalar
incompatibleRegionCodes = _IncompatibleRegionCodes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 4),
    _IncompatibleRegionCodes_Type()
)
incompatibleRegionCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incompatibleRegionCodes.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 5),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 6),
    _WirelessLinkDisabledWarning_Type()
)
wirelessLinkDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkDisabledWarning.setStatus("current")


class _DataPortDisabledWarning_Type(Integer32):
    """Custom type dataPortDisabledWarning based on Integer32"""
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


_DataPortDisabledWarning_Type.__name__ = "Integer32"
_DataPortDisabledWarning_Object = MibScalar
dataPortDisabledWarning = _DataPortDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 7),
    _DataPortDisabledWarning_Type()
)
dataPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortDisabledWarning.setStatus("current")


class _DataPortFiberStatus_Type(Integer32):
    """Custom type dataPortFiberStatus based on Integer32"""
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
        *(("fiberLinkNotEstablishedAndLOSDetected", 3),
          ("fiberLinkNotEstablishedButLOSNotDetected", 2),
          ("installedFiberNotLicensed", 1),
          ("ok", 0))
    )


_DataPortFiberStatus_Type.__name__ = "Integer32"
_DataPortFiberStatus_Object = MibScalar
dataPortFiberStatus = _DataPortFiberStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 8),
    _DataPortFiberStatus_Type()
)
dataPortFiberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortFiberStatus.setStatus("current")


class _DataPortConfigurationMismatch_Type(Integer32):
    """Custom type dataPortConfigurationMismatch based on Integer32"""
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


_DataPortConfigurationMismatch_Type.__name__ = "Integer32"
_DataPortConfigurationMismatch_Object = MibScalar
dataPortConfigurationMismatch = _DataPortConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 9),
    _DataPortConfigurationMismatch_Type()
)
dataPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortConfigurationMismatch.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 10),
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("acquiringLock", 3),
          ("clusterTimingMaster", 7),
          ("holdover", 1),
          ("holdoverNotConnected", 2),
          ("initialising", 6),
          ("locked", 0),
          ("noTimingReference", 4),
          ("tDDSyncNotActive", 8),
          ("timingSystemNotConnected", 5))
    )


_TDDSynchronizationStatus_Type.__name__ = "Integer32"
_TDDSynchronizationStatus_Object = MibScalar
tDDSynchronizationStatus = _TDDSynchronizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 11),
    _TDDSynchronizationStatus_Type()
)
tDDSynchronizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDDSynchronizationStatus.setStatus("current")


class _ManagementPortDisabledWarning_Type(Integer32):
    """Custom type managementPortDisabledWarning based on Integer32"""
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


_ManagementPortDisabledWarning_Type.__name__ = "Integer32"
_ManagementPortDisabledWarning_Object = MibScalar
managementPortDisabledWarning = _ManagementPortDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 12),
    _ManagementPortDisabledWarning_Type()
)
managementPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementPortDisabledWarning.setStatus("current")


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
        *(("notSynchronized", 1),
          ("ok", 0),
          ("timingSystemFailure", 2))
    )


_TDDSynchronizationAlarm_Type.__name__ = "Integer32"
_TDDSynchronizationAlarm_Object = MibScalar
tDDSynchronizationAlarm = _TDDSynchronizationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 13),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 14),
    _LinkModeOptimizationMismatch_Type()
)
linkModeOptimizationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkModeOptimizationMismatch.setStatus("current")


class _ManagementPortConfigurationMismatch_Type(Integer32):
    """Custom type managementPortConfigurationMismatch based on Integer32"""
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


_ManagementPortConfigurationMismatch_Type.__name__ = "Integer32"
_ManagementPortConfigurationMismatch_Object = MibScalar
managementPortConfigurationMismatch = _ManagementPortConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 15),
    _ManagementPortConfigurationMismatch_Type()
)
managementPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementPortConfigurationMismatch.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 16),
    _SecureModeAlarm_Type()
)
secureModeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureModeAlarm.setStatus("current")


class _EthernetBridgingStatusAlarm_Type(Integer32):
    """Custom type ethernetBridgingStatusAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ethernetBridgingDisabled", 1),
          ("ethernetBridgingEnabled", 0))
    )


_EthernetBridgingStatusAlarm_Type.__name__ = "Integer32"
_EthernetBridgingStatusAlarm_Object = MibScalar
ethernetBridgingStatusAlarm = _EthernetBridgingStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 13, 17),
    _EthernetBridgingStatusAlarm_Type()
)
ethernetBridgingStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetBridgingStatusAlarm.setStatus("current")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 15)
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 15, 1),
    _SMTPEmailAlert_Type()
)
sMTPEmailAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPEmailAlert.setStatus("current")
_SMTPServerIPAddress_Type = IpAddress
_SMTPServerIPAddress_Object = MibScalar
sMTPServerIPAddress = _SMTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 15, 2),
    _SMTPServerIPAddress_Type()
)
sMTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPServerIPAddress.setStatus("current")


class _SMTPServerPortNumber_Type(Integer32):
    """Custom type sMTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SMTPServerPortNumber_Type.__name__ = "Integer32"
_SMTPServerPortNumber_Object = MibScalar
sMTPServerPortNumber = _SMTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 15, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 15, 4),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 15, 5),
    _SMTPDestinationEmailAddress_Type()
)
sMTPDestinationEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPDestinationEmailAddress.setStatus("current")


class _SMTPEnabledMessages_Type(Bits):
    """Custom type sMTPEnabledMessages based on Bits"""
    namedValues = NamedValues(
        *(("dFSChannelChange", 6),
          ("dFSImpulseInterference", 5),
          ("dataPortUpDown", 3),
          ("enabledDiagnosticAlarms", 4),
          ("managementPortUpDown", 2),
          ("telecomsChannelUpDown", 1),
          ("wirelessLinkUpDown", 7))
    )

_SMTPEnabledMessages_Type.__name__ = "Bits"
_SMTPEnabledMessages_Object = MibScalar
sMTPEnabledMessages = _SMTPEnabledMessages_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 15, 6),
    _SMTPEnabledMessages_Type()
)
sMTPEnabledMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPEnabledMessages.setStatus("current")
_SnmpControl_ObjectIdentity = ObjectIdentity
snmpControl = _SnmpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 16)
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 16, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 16, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 16, 3),
    _SNMPTrapTableNumber_Type()
)
sNMPTrapTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapTableNumber.setStatus("current")
_SNMPTrapTable_Object = MibTable
sNMPTrapTable = _SNMPTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 16, 4)
)
if mibBuilder.loadTexts:
    sNMPTrapTable.setStatus("current")
_SNMPTrapTableEntry_Object = MibTableRow
sNMPTrapTableEntry = _SNMPTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 16, 4, 1)
)
sNMPTrapTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP600-MIB", "sNMPTrapTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 16, 4, 1, 1),
    _SNMPTrapTableIndex_Type()
)
sNMPTrapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sNMPTrapTableIndex.setStatus("current")
_SNMPTrapIPAddress_Type = IpAddress
_SNMPTrapIPAddress_Object = MibTableColumn
sNMPTrapIPAddress = _SNMPTrapIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 16, 4, 1, 2),
    _SNMPTrapIPAddress_Type()
)
sNMPTrapIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapIPAddress.setStatus("current")


class _SNMPTrapPortNumber_Type(Integer32):
    """Custom type sNMPTrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SNMPTrapPortNumber_Type.__name__ = "Integer32"
_SNMPTrapPortNumber_Object = MibTableColumn
sNMPTrapPortNumber = _SNMPTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 16, 4, 1, 3),
    _SNMPTrapPortNumber_Type()
)
sNMPTrapPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapPortNumber.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 6, 16, 5),
    _SNMPTrapVersion_Type()
)
sNMPTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapVersion.setStatus("current")


class _SNMPEnabledTraps_Type(Bits):
    """Custom type sNMPEnabledTraps based on Bits"""
    namedValues = NamedValues(
        *(("authenticationFailure", 2),
          ("coldStart", 7),
          ("dFSChannelChange", 5),
          ("dFSImpulseInterference", 4),
          ("dataPortUpDown", 1),
          ("enabledDiagnosticAlarms", 3),
          ("managementPortUpDown", 0),
          ("telecomsChannelUpDown", 15),
          ("wirelessLinkUpDown", 6))
    )

_SNMPEnabledTraps_Type.__name__ = "Bits"
_SNMPEnabledTraps_Object = MibScalar
sNMPEnabledTraps = _SNMPEnabledTraps_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 16, 6),
    _SNMPEnabledTraps_Type()
)
sNMPEnabledTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPEnabledTraps.setStatus("current")


class _EnabledDiagnosticAlarms_Type(Bits):
    """Custom type enabledDiagnosticAlarms based on Bits"""
    namedValues = NamedValues(
        *(("dataPortConfigurationMismatch", 15),
          ("dataPortDisabledWarning", 11),
          ("dataPortFiberStatus", 9),
          ("dataPortStatus", 10),
          ("ethernetBridgingStatus", 26),
          ("incompatibleMasterAndSlave", 0),
          ("incompatibleRegionCodes", 1),
          ("installArmState", 5),
          ("installStatus", 6),
          ("linkModeOptimizationMismatch", 17),
          ("managementPortConfigurationMismatch", 29),
          ("managementPortDisabledWarning", 19),
          ("managementPortStatus", 18),
          ("noWirelessChannelAvailable", 14),
          ("regionCode", 7),
          ("sNTPSyncronisationFailed", 13),
          ("secureMode", 27),
          ("syslogClientDisabledWarning", 28),
          ("syslogDisabledWarning", 16),
          ("syslogLocalNearlyFull", 31),
          ("syslogLocalWrapped", 30),
          ("tDDSynchronizationAlarm", 20),
          ("telecomsChannelALoopback", 22),
          ("telecomsChannelAStatus", 8),
          ("telecomsChannelBLoopback", 21),
          ("telecomsChannelBStatus", 23),
          ("unitOutOfCalibration", 4),
          ("unknown5", 3),
          ("unknown6", 2),
          ("wirelessLinkDisabledWarning", 12))
    )

_EnabledDiagnosticAlarms_Type.__name__ = "Bits"
_EnabledDiagnosticAlarms_Object = MibScalar
enabledDiagnosticAlarms = _EnabledDiagnosticAlarms_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 16, 7),
    _EnabledDiagnosticAlarms_Type()
)
enabledDiagnosticAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enabledDiagnosticAlarms.setStatus("current")
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 17)
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 4),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 5),
    _SNTPSync_Type()
)
sNTPSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPSync.setStatus("current")
_SNTPLastSync_Type = Integer32
_SNTPLastSync_Object = MibScalar
sNTPLastSync = _SNTPLastSync_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 6),
    _SNTPLastSync_Type()
)
sNTPLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPLastSync.setStatus("current")
_SystemClock_Type = Integer32
_SystemClock_Object = MibScalar
systemClock = _SystemClock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 7),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 8),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 9),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 10),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 11),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 12),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 13),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 14),
    _SNTPServerTableNumber_Type()
)
sNTPServerTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerTableNumber.setStatus("current")
_SNTPServerTable_Object = MibTable
sNTPServerTable = _SNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 15)
)
if mibBuilder.loadTexts:
    sNTPServerTable.setStatus("current")
_SNTPServerTableEntry_Object = MibTableRow
sNTPServerTableEntry = _SNTPServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 15, 1)
)
sNTPServerTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP600-MIB", "sNTPServerTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 15, 1, 1),
    _SNTPServerTableIndex_Type()
)
sNTPServerTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sNTPServerTableIndex.setStatus("current")
_SNTPServerIPAddress_Type = IpAddress
_SNTPServerIPAddress_Object = MibTableColumn
sNTPServerIPAddress = _SNTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 15, 1, 2),
    _SNTPServerIPAddress_Type()
)
sNTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerIPAddress.setStatus("current")


class _SNTPServerPortNumber_Type(Integer32):
    """Custom type sNTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SNTPServerPortNumber_Type.__name__ = "Integer32"
_SNTPServerPortNumber_Object = MibTableColumn
sNTPServerPortNumber = _SNTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 15, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 17, 15, 1, 4),
    _SNTPServerStatus_Type()
)
sNTPServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerStatus.setStatus("current")
_Reset_ObjectIdentity = ObjectIdentity
reset = _Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 18)
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 18, 1),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("current")
_Versions_ObjectIdentity = ObjectIdentity
versions = _Versions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 19)
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 19, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 19, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 19, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 19, 4),
    _BootVersion_Type()
)
bootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersion.setStatus("current")
_PubStats_ObjectIdentity = ObjectIdentity
pubStats = _PubStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 20)
)
_ReceiveDataRate_Type = Integer32
_ReceiveDataRate_Object = MibScalar
receiveDataRate = _ReceiveDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 20, 1),
    _ReceiveDataRate_Type()
)
receiveDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveDataRate.setStatus("current")
_TransmitDataRate_Type = Integer32
_TransmitDataRate_Object = MibScalar
transmitDataRate = _TransmitDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 20, 2),
    _TransmitDataRate_Type()
)
transmitDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitDataRate.setStatus("current")
_AggregateDataRate_Type = Integer32
_AggregateDataRate_Object = MibScalar
aggregateDataRate = _AggregateDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 20, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 20, 4),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 20, 5),
    _WirelessLinkStatus_Type()
)
wirelessLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatus.setStatus("current")
_ByteErrorRatio_Type = Integer32
_ByteErrorRatio_Object = MibScalar
byteErrorRatio = _ByteErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 20, 6),
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("limitedByTheWirelessConditions", 8),
          ("restrictedBecauseDFSchannelChangeIsInProgress", 5),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 20, 7),
    _ReceiveModulationModeDetail_Type()
)
receiveModulationModeDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveModulationModeDetail.setStatus("current")


class _EthernetBridgingAvailability_Type(Integer32):
    """Custom type ethernetBridgingAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_EthernetBridgingAvailability_Type.__name__ = "Integer32"
_EthernetBridgingAvailability_Object = MibScalar
ethernetBridgingAvailability = _EthernetBridgingAvailability_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 20, 8),
    _EthernetBridgingAvailability_Type()
)
ethernetBridgingAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetBridgingAvailability.setStatus("current")
_Encryption_ObjectIdentity = ObjectIdentity
encryption = _Encryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 22)
)


class _EncryptionAlgorithm_Type(Integer32):
    """Custom type encryptionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aES256bitRijndael", 2),
          ("aESRijndael", 1),
          ("none", 0))
    )


_EncryptionAlgorithm_Type.__name__ = "Integer32"
_EncryptionAlgorithm_Object = MibScalar
encryptionAlgorithm = _EncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 22, 1),
    _EncryptionAlgorithm_Type()
)
encryptionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionAlgorithm.setStatus("current")
_TDDControl_ObjectIdentity = ObjectIdentity
tDDControl = _TDDControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 23)
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 23, 1),
    _TDDSynchronizationMode_Type()
)
tDDSynchronizationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDDSynchronizationMode.setStatus("current")
_SyslogControl_ObjectIdentity = ObjectIdentity
syslogControl = _SyslogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 24)
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 24, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 24, 2),
    _SyslogState_Type()
)
syslogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogState.setStatus("current")
_Supplementary_ObjectIdentity = ObjectIdentity
supplementary = _Supplementary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 96)
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 96, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 6, 96, 2),
    _Latitude_Type()
)
latitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latitude.setStatus("current")
_Altitude_Type = Integer32
_Altitude_Object = MibScalar
altitude = _Altitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 6, 96, 3),
    _Altitude_Type()
)
altitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altitude.setStatus("current")
_PtpGroups_ObjectIdentity = ObjectIdentity
ptpGroups = _PtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98)
)
_PtpTraps_ObjectIdentity = ObjectIdentity
ptpTraps = _PtpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99)
)
_PtpTrapPrefix_ObjectIdentity = ObjectIdentity
ptpTrapPrefix = _PtpTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0)
)

# Managed Objects groups

dfsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 3)
)
dfsGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "dfsTableNumber"),
        ("CAMBIUM-PTP600-MIB", "dfsMeans"),
        ("CAMBIUM-PTP600-MIB", "dfsNineNinePointNinePercentiles"),
        ("CAMBIUM-PTP600-MIB", "dfsPeaks"))
)
if mibBuilder.loadTexts:
    dfsGroup.setStatus("current")

bridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 4)
)
bridgeGroup.setObjects(
    ("CAMBIUM-PTP600-MIB", "localPacketFiltering")
)
if mibBuilder.loadTexts:
    bridgeGroup.setStatus("current")

configurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 5)
)
configurationGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "iPAddress"),
        ("CAMBIUM-PTP600-MIB", "subnetMask"),
        ("CAMBIUM-PTP600-MIB", "gatewayIPAddress"),
        ("CAMBIUM-PTP600-MIB", "targetMACAddress"),
        ("CAMBIUM-PTP600-MIB", "masterSlaveMode"),
        ("CAMBIUM-PTP600-MIB", "maximumTransmitPower"),
        ("CAMBIUM-PTP600-MIB", "antennaGain"),
        ("CAMBIUM-PTP600-MIB", "cableLoss"),
        ("CAMBIUM-PTP600-MIB", "eIRP"),
        ("CAMBIUM-PTP600-MIB", "ethernetCappedMaxWirelessSpeed"),
        ("CAMBIUM-PTP600-MIB", "channelBandwidth"),
        ("CAMBIUM-PTP600-MIB", "remoteIPAddress"),
        ("CAMBIUM-PTP600-MIB", "linkName"),
        ("CAMBIUM-PTP600-MIB", "siteName"),
        ("CAMBIUM-PTP600-MIB", "accessMethod"),
        ("CAMBIUM-PTP600-MIB", "groupID"))
)
if mibBuilder.loadTexts:
    configurationGroup.setStatus("current")

ethernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 6)
)
ethernetGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "dataPortAutoNegotiation"),
        ("CAMBIUM-PTP600-MIB", "dataPortAutoNegAdvertisement"),
        ("CAMBIUM-PTP600-MIB", "dataPortAutoMdix"),
        ("CAMBIUM-PTP600-MIB", "dataPortStatus"),
        ("CAMBIUM-PTP600-MIB", "dataPortSpeedAndDuplex"),
        ("CAMBIUM-PTP600-MIB", "dataPortWirelessDownAlert"),
        ("CAMBIUM-PTP600-MIB", "useVLANForManagementInterfaces"),
        ("CAMBIUM-PTP600-MIB", "vLANManagementPriority"),
        ("CAMBIUM-PTP600-MIB", "vLANManagementVID"),
        ("CAMBIUM-PTP600-MIB", "managementPortStatus"),
        ("CAMBIUM-PTP600-MIB", "managementPortSpeedAndDuplex"),
        ("CAMBIUM-PTP600-MIB", "ethernetPriorityTableNumber"),
        ("CAMBIUM-PTP600-MIB", "l2CPPriorityTableNumber"),
        ("CAMBIUM-PTP600-MIB", "iPDSCPPriorityTableNumber"),
        ("CAMBIUM-PTP600-MIB", "mPLSTCPriorityTableNumber"),
        ("CAMBIUM-PTP600-MIB", "managementMode"),
        ("CAMBIUM-PTP600-MIB", "managementPortWirelessDownAlert"),
        ("CAMBIUM-PTP600-MIB", "qOSPriorityScheme"),
        ("CAMBIUM-PTP600-MIB", "unknownNetworkPriorityQueueMapping"),
        ("CAMBIUM-PTP600-MIB", "dSCPManagementPriority"),
        ("CAMBIUM-PTP600-MIB", "ethernetBridgingStatus"),
        ("CAMBIUM-PTP600-MIB", "ethernetPriorityQueueMapping"),
        ("CAMBIUM-PTP600-MIB", "l2CPPriorityQueueMapping"),
        ("CAMBIUM-PTP600-MIB", "iPDSCPPriorityQueueMapping"),
        ("CAMBIUM-PTP600-MIB", "mPLSTCPriorityQueueMapping"))
)
if mibBuilder.loadTexts:
    ethernetGroup.setStatus("current")

telecomGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 7)
)
telecomGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "telecomsInterface"),
        ("CAMBIUM-PTP600-MIB", "telecomsChannelAStatus"),
        ("CAMBIUM-PTP600-MIB", "telecomsChannelBStatus"),
        ("CAMBIUM-PTP600-MIB", "channelALineCode"),
        ("CAMBIUM-PTP600-MIB", "channelBLineCode"),
        ("CAMBIUM-PTP600-MIB", "channelACableLength"),
        ("CAMBIUM-PTP600-MIB", "channelBCableLength"),
        ("CAMBIUM-PTP600-MIB", "channelALoopback"),
        ("CAMBIUM-PTP600-MIB", "channelBLoopback"),
        ("CAMBIUM-PTP600-MIB", "telecomsChannelSelection"))
)
if mibBuilder.loadTexts:
    telecomGroup.setStatus("current")

licenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 8)
)
licenceGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "regionCode"),
        ("CAMBIUM-PTP600-MIB", "productVariant"),
        ("CAMBIUM-PTP600-MIB", "productName"),
        ("CAMBIUM-PTP600-MIB", "ethernetFiberSupport"),
        ("CAMBIUM-PTP600-MIB", "frequencyVariant"),
        ("CAMBIUM-PTP600-MIB", "bandwidthVariant"),
        ("CAMBIUM-PTP600-MIB", "constantPowerSpectralDensity"),
        ("CAMBIUM-PTP600-MIB", "sNMPv3Enable"),
        ("CAMBIUM-PTP600-MIB", "hAZLOCConfiguration"),
        ("CAMBIUM-PTP600-MIB", "securityLevel"))
)
if mibBuilder.loadTexts:
    licenceGroup.setStatus("current")

managementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 9)
)
managementGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "targetRange"),
        ("CAMBIUM-PTP600-MIB", "rangingMode"),
        ("CAMBIUM-PTP600-MIB", "installStatus"),
        ("CAMBIUM-PTP600-MIB", "installArmState"),
        ("CAMBIUM-PTP600-MIB", "tFTPServerIPAddress"),
        ("CAMBIUM-PTP600-MIB", "tFTPServerPortNumber"),
        ("CAMBIUM-PTP600-MIB", "tFTPSoftwareUpgradeFileName"),
        ("CAMBIUM-PTP600-MIB", "tFTPStartSoftwareUpgrade"),
        ("CAMBIUM-PTP600-MIB", "tFTPSoftwareUpgradeStatus"),
        ("CAMBIUM-PTP600-MIB", "tFTPSoftwareUpgradeStatusText"),
        ("CAMBIUM-PTP600-MIB", "tFTPSoftwareUpgradeStatusAdditionalText"),
        ("CAMBIUM-PTP600-MIB", "hTTPAccessEnabled"),
        ("CAMBIUM-PTP600-MIB", "telnetAccessEnabled"),
        ("CAMBIUM-PTP600-MIB", "hTTPPortNumber"),
        ("CAMBIUM-PTP600-MIB", "hTTPSPortNumber"),
        ("CAMBIUM-PTP600-MIB", "telnetPortNumber"),
        ("CAMBIUM-PTP600-MIB", "hTTPSAccessEnabled"))
)
if mibBuilder.loadTexts:
    managementGroup.setStatus("current")

phyControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 10)
)
phyControlGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "linkSymmetry"),
        ("CAMBIUM-PTP600-MIB", "linkModeOptimisation"),
        ("CAMBIUM-PTP600-MIB", "userConfiguredMaxModulationMode"),
        ("CAMBIUM-PTP600-MIB", "remoteMaximumTransmitPower"),
        ("CAMBIUM-PTP600-MIB", "txColorCode"),
        ("CAMBIUM-PTP600-MIB", "rxColorCode"),
        ("CAMBIUM-PTP600-MIB", "automaticTxPowerControl"),
        ("CAMBIUM-PTP600-MIB", "remoteRxTargetPower"))
)
if mibBuilder.loadTexts:
    phyControlGroup.setStatus("current")

phyStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 12)
)
phyStatusGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "receivePower"),
        ("CAMBIUM-PTP600-MIB", "vectorError"),
        ("CAMBIUM-PTP600-MIB", "transmitPower"),
        ("CAMBIUM-PTP600-MIB", "range"),
        ("CAMBIUM-PTP600-MIB", "linkLoss"),
        ("CAMBIUM-PTP600-MIB", "receiveChannel"),
        ("CAMBIUM-PTP600-MIB", "transmitChannel"),
        ("CAMBIUM-PTP600-MIB", "receiveModulationMode"),
        ("CAMBIUM-PTP600-MIB", "transmitModulationMode"),
        ("CAMBIUM-PTP600-MIB", "receiveFreqMHz"),
        ("CAMBIUM-PTP600-MIB", "transmitFreqMHz"),
        ("CAMBIUM-PTP600-MIB", "signalStrengthRatio"),
        ("CAMBIUM-PTP600-MIB", "receiveFreqKHz"),
        ("CAMBIUM-PTP600-MIB", "transmitFreqKHz"),
        ("CAMBIUM-PTP600-MIB", "searchState"),
        ("CAMBIUM-PTP600-MIB", "rawReceivePower"))
)
if mibBuilder.loadTexts:
    phyStatusGroup.setStatus("current")

alarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 13)
)
alarmsGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "unitOutOfCalibration"),
        ("CAMBIUM-PTP600-MIB", "encryptionEnabledMismatch"),
        ("CAMBIUM-PTP600-MIB", "incompatibleRegionCodes"),
        ("CAMBIUM-PTP600-MIB", "noWirelessChannelAvailable"),
        ("CAMBIUM-PTP600-MIB", "wirelessLinkDisabledWarning"),
        ("CAMBIUM-PTP600-MIB", "dataPortDisabledWarning"),
        ("CAMBIUM-PTP600-MIB", "dataPortFiberStatus"),
        ("CAMBIUM-PTP600-MIB", "dataPortConfigurationMismatch"),
        ("CAMBIUM-PTP600-MIB", "incompatibleMasterAndSlave"),
        ("CAMBIUM-PTP600-MIB", "tDDSynchronizationStatus"),
        ("CAMBIUM-PTP600-MIB", "managementPortDisabledWarning"),
        ("CAMBIUM-PTP600-MIB", "tDDSynchronizationAlarm"),
        ("CAMBIUM-PTP600-MIB", "linkModeOptimizationMismatch"),
        ("CAMBIUM-PTP600-MIB", "managementPortConfigurationMismatch"),
        ("CAMBIUM-PTP600-MIB", "secureModeAlarm"),
        ("CAMBIUM-PTP600-MIB", "ethernetBridgingStatusAlarm"))
)
if mibBuilder.loadTexts:
    alarmsGroup.setStatus("current")

smtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 15)
)
smtpGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "sMTPEmailAlert"),
        ("CAMBIUM-PTP600-MIB", "sMTPServerIPAddress"),
        ("CAMBIUM-PTP600-MIB", "sMTPServerPortNumber"),
        ("CAMBIUM-PTP600-MIB", "sMTPSourceEmailAddress"),
        ("CAMBIUM-PTP600-MIB", "sMTPDestinationEmailAddress"),
        ("CAMBIUM-PTP600-MIB", "sMTPEnabledMessages"))
)
if mibBuilder.loadTexts:
    smtpGroup.setStatus("current")

snmpControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 16)
)
snmpControlGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "sNMPPortNumber"),
        ("CAMBIUM-PTP600-MIB", "sNMPCommunityString"),
        ("CAMBIUM-PTP600-MIB", "sNMPTrapTableNumber"),
        ("CAMBIUM-PTP600-MIB", "sNMPTrapVersion"),
        ("CAMBIUM-PTP600-MIB", "sNMPEnabledTraps"),
        ("CAMBIUM-PTP600-MIB", "enabledDiagnosticAlarms"),
        ("CAMBIUM-PTP600-MIB", "sNMPTrapIPAddress"),
        ("CAMBIUM-PTP600-MIB", "sNMPTrapPortNumber"))
)
if mibBuilder.loadTexts:
    snmpControlGroup.setStatus("current")

sntpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 17)
)
sntpGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "sNTPState"),
        ("CAMBIUM-PTP600-MIB", "sNTPPollInterval"),
        ("CAMBIUM-PTP600-MIB", "sNTPSync"),
        ("CAMBIUM-PTP600-MIB", "sNTPLastSync"),
        ("CAMBIUM-PTP600-MIB", "systemClock"),
        ("CAMBIUM-PTP600-MIB", "timeZone"),
        ("CAMBIUM-PTP600-MIB", "daylightSaving"),
        ("CAMBIUM-PTP600-MIB", "sNTPPrimaryServer"),
        ("CAMBIUM-PTP600-MIB", "sNTPPrimaryServerDeadTime"),
        ("CAMBIUM-PTP600-MIB", "sNTPServerRetries"),
        ("CAMBIUM-PTP600-MIB", "sNTPServerTimeout"),
        ("CAMBIUM-PTP600-MIB", "sNTPServerTableNumber"),
        ("CAMBIUM-PTP600-MIB", "sNTPServerIPAddress"),
        ("CAMBIUM-PTP600-MIB", "sNTPServerPortNumber"),
        ("CAMBIUM-PTP600-MIB", "sNTPServerStatus"))
)
if mibBuilder.loadTexts:
    sntpGroup.setStatus("current")

resetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 18)
)
resetGroup.setObjects(
    ("CAMBIUM-PTP600-MIB", "systemReset")
)
if mibBuilder.loadTexts:
    resetGroup.setStatus("current")

versionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 19)
)
versionsGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "softwareVersion"),
        ("CAMBIUM-PTP600-MIB", "hardwareVersion"),
        ("CAMBIUM-PTP600-MIB", "secondarySoftwareVersion"),
        ("CAMBIUM-PTP600-MIB", "bootVersion"))
)
if mibBuilder.loadTexts:
    versionsGroup.setStatus("current")

pubStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 20)
)
pubStatsGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "receiveDataRate"),
        ("CAMBIUM-PTP600-MIB", "transmitDataRate"),
        ("CAMBIUM-PTP600-MIB", "aggregateDataRate"),
        ("CAMBIUM-PTP600-MIB", "wirelessLinkAvailability"),
        ("CAMBIUM-PTP600-MIB", "wirelessLinkStatus"),
        ("CAMBIUM-PTP600-MIB", "byteErrorRatio"),
        ("CAMBIUM-PTP600-MIB", "receiveModulationModeDetail"),
        ("CAMBIUM-PTP600-MIB", "ethernetBridgingAvailability"))
)
if mibBuilder.loadTexts:
    pubStatsGroup.setStatus("current")

encryptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 22)
)
encryptionGroup.setObjects(
    ("CAMBIUM-PTP600-MIB", "encryptionAlgorithm")
)
if mibBuilder.loadTexts:
    encryptionGroup.setStatus("current")

tDDControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 23)
)
tDDControlGroup.setObjects(
    ("CAMBIUM-PTP600-MIB", "tDDSynchronizationMode")
)
if mibBuilder.loadTexts:
    tDDControlGroup.setStatus("current")

syslogControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 24)
)
syslogControlGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "syslogClient"),
        ("CAMBIUM-PTP600-MIB", "syslogState"))
)
if mibBuilder.loadTexts:
    syslogControlGroup.setStatus("current")

supplementaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 96)
)
supplementaryGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "longitude"),
        ("CAMBIUM-PTP600-MIB", "latitude"),
        ("CAMBIUM-PTP600-MIB", "altitude"))
)
if mibBuilder.loadTexts:
    supplementaryGroup.setStatus("current")


# Notification objects

dfsChannelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 1)
)
dfsChannelChangeTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "receiveChannel")
)
if mibBuilder.loadTexts:
    dfsChannelChangeTrap.setStatus(
        "current"
    )

dfsImpulsiveInterferenceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 2)
)
dfsImpulsiveInterferenceTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "receiveChannel")
)
if mibBuilder.loadTexts:
    dfsImpulsiveInterferenceTrap.setStatus(
        "current"
    )

dataPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 3)
)
dataPortStatusTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "dataPortStatus")
)
if mibBuilder.loadTexts:
    dataPortStatusTrap.setStatus(
        "current"
    )

telecomsChannelAStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 4)
)
telecomsChannelAStatusTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "telecomsChannelAStatus")
)
if mibBuilder.loadTexts:
    telecomsChannelAStatusTrap.setStatus(
        "current"
    )

telecomsChannelBStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 5)
)
telecomsChannelBStatusTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "telecomsChannelBStatus")
)
if mibBuilder.loadTexts:
    telecomsChannelBStatusTrap.setStatus(
        "current"
    )

channelALoopbackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 6)
)
channelALoopbackTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "channelALoopback")
)
if mibBuilder.loadTexts:
    channelALoopbackTrap.setStatus(
        "current"
    )

channelBLoopbackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 7)
)
channelBLoopbackTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "channelBLoopback")
)
if mibBuilder.loadTexts:
    channelBLoopbackTrap.setStatus(
        "current"
    )

regionCodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 8)
)
regionCodeTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "regionCode")
)
if mibBuilder.loadTexts:
    regionCodeTrap.setStatus(
        "current"
    )

installStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 9)
)
installStatusTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "installStatus")
)
if mibBuilder.loadTexts:
    installStatusTrap.setStatus(
        "current"
    )

installArmStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 10)
)
installArmStateTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "installArmState")
)
if mibBuilder.loadTexts:
    installArmStateTrap.setStatus(
        "current"
    )

unitOutOfCalibrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 11)
)
unitOutOfCalibrationTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "unitOutOfCalibration")
)
if mibBuilder.loadTexts:
    unitOutOfCalibrationTrap.setStatus(
        "current"
    )

encryptionEnabledMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 13)
)
encryptionEnabledMismatchTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "encryptionEnabledMismatch")
)
if mibBuilder.loadTexts:
    encryptionEnabledMismatchTrap.setStatus(
        "current"
    )

incompatibleRegionCodesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 14)
)
incompatibleRegionCodesTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "incompatibleRegionCodes")
)
if mibBuilder.loadTexts:
    incompatibleRegionCodesTrap.setStatus(
        "current"
    )

noWirelessChannelAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 15)
)
noWirelessChannelAvailableTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "noWirelessChannelAvailable")
)
if mibBuilder.loadTexts:
    noWirelessChannelAvailableTrap.setStatus(
        "current"
    )

wirelessLinkDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 16)
)
wirelessLinkDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "wirelessLinkDisabledWarning")
)
if mibBuilder.loadTexts:
    wirelessLinkDisabledWarningTrap.setStatus(
        "current"
    )

dataPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 17)
)
dataPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "dataPortDisabledWarning")
)
if mibBuilder.loadTexts:
    dataPortDisabledWarningTrap.setStatus(
        "current"
    )

dataPortFiberStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 18)
)
dataPortFiberStatusTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "dataPortFiberStatus")
)
if mibBuilder.loadTexts:
    dataPortFiberStatusTrap.setStatus(
        "current"
    )

dataPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 19)
)
dataPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "dataPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    dataPortConfigurationMismatchTrap.setStatus(
        "current"
    )

incompatibleMasterAndSlaveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 20)
)
incompatibleMasterAndSlaveTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "incompatibleMasterAndSlave")
)
if mibBuilder.loadTexts:
    incompatibleMasterAndSlaveTrap.setStatus(
        "current"
    )

sNTPSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 21)
)
sNTPSyncTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "sNTPSync")
)
if mibBuilder.loadTexts:
    sNTPSyncTrap.setStatus(
        "current"
    )

tDDSynchronizationAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 22)
)
tDDSynchronizationAlarmTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "tDDSynchronizationAlarm")
)
if mibBuilder.loadTexts:
    tDDSynchronizationAlarmTrap.setStatus(
        "current"
    )

managementPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 23)
)
managementPortStatusTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "managementPortStatus")
)
if mibBuilder.loadTexts:
    managementPortStatusTrap.setStatus(
        "current"
    )

managementPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 24)
)
managementPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "managementPortDisabledWarning")
)
if mibBuilder.loadTexts:
    managementPortDisabledWarningTrap.setStatus(
        "current"
    )

linkModeOptimizationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 25)
)
linkModeOptimizationMismatchTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "linkModeOptimizationMismatch")
)
if mibBuilder.loadTexts:
    linkModeOptimizationMismatchTrap.setStatus(
        "current"
    )

managementPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 28)
)
managementPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "managementPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    managementPortConfigurationMismatchTrap.setStatus(
        "current"
    )

syslogStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 30)
)
syslogStateTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "syslogState")
)
if mibBuilder.loadTexts:
    syslogStateTrap.setStatus(
        "current"
    )

syslogLocalNearlyFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 31)
)
if mibBuilder.loadTexts:
    syslogLocalNearlyFullTrap.setStatus(
        "current"
    )

syslogLocalWrappedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 32)
)
if mibBuilder.loadTexts:
    syslogLocalWrappedTrap.setStatus(
        "current"
    )

syslogClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 33)
)
syslogClientTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "syslogClient")
)
if mibBuilder.loadTexts:
    syslogClientTrap.setStatus(
        "current"
    )

secureModeAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 34)
)
secureModeAlarmTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "secureModeAlarm")
)
if mibBuilder.loadTexts:
    secureModeAlarmTrap.setStatus(
        "current"
    )

ethernetBridgingStatusAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 6, 99, 0, 35)
)
ethernetBridgingStatusAlarmTrap.setObjects(
    ("CAMBIUM-PTP600-MIB", "ethernetBridgingStatusAlarm")
)
if mibBuilder.loadTexts:
    ethernetBridgingStatusAlarmTrap.setStatus(
        "current"
    )


# Notifications groups

notificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 17713, 6, 98, 99)
)
notificationsGroup.setObjects(
      *(("CAMBIUM-PTP600-MIB", "dfsChannelChangeTrap"),
        ("CAMBIUM-PTP600-MIB", "dfsImpulsiveInterferenceTrap"),
        ("CAMBIUM-PTP600-MIB", "dataPortStatusTrap"),
        ("CAMBIUM-PTP600-MIB", "telecomsChannelAStatusTrap"),
        ("CAMBIUM-PTP600-MIB", "telecomsChannelBStatusTrap"),
        ("CAMBIUM-PTP600-MIB", "channelALoopbackTrap"),
        ("CAMBIUM-PTP600-MIB", "channelBLoopbackTrap"),
        ("CAMBIUM-PTP600-MIB", "regionCodeTrap"),
        ("CAMBIUM-PTP600-MIB", "installStatusTrap"),
        ("CAMBIUM-PTP600-MIB", "installArmStateTrap"),
        ("CAMBIUM-PTP600-MIB", "unitOutOfCalibrationTrap"),
        ("CAMBIUM-PTP600-MIB", "encryptionEnabledMismatchTrap"),
        ("CAMBIUM-PTP600-MIB", "incompatibleRegionCodesTrap"),
        ("CAMBIUM-PTP600-MIB", "noWirelessChannelAvailableTrap"),
        ("CAMBIUM-PTP600-MIB", "wirelessLinkDisabledWarningTrap"),
        ("CAMBIUM-PTP600-MIB", "dataPortDisabledWarningTrap"),
        ("CAMBIUM-PTP600-MIB", "dataPortFiberStatusTrap"),
        ("CAMBIUM-PTP600-MIB", "dataPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP600-MIB", "incompatibleMasterAndSlaveTrap"),
        ("CAMBIUM-PTP600-MIB", "sNTPSyncTrap"),
        ("CAMBIUM-PTP600-MIB", "tDDSynchronizationAlarmTrap"),
        ("CAMBIUM-PTP600-MIB", "managementPortStatusTrap"),
        ("CAMBIUM-PTP600-MIB", "managementPortDisabledWarningTrap"),
        ("CAMBIUM-PTP600-MIB", "linkModeOptimizationMismatchTrap"),
        ("CAMBIUM-PTP600-MIB", "managementPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP600-MIB", "syslogStateTrap"),
        ("CAMBIUM-PTP600-MIB", "syslogLocalNearlyFullTrap"),
        ("CAMBIUM-PTP600-MIB", "syslogLocalWrappedTrap"),
        ("CAMBIUM-PTP600-MIB", "syslogClientTrap"),
        ("CAMBIUM-PTP600-MIB", "secureModeAlarmTrap"),
        ("CAMBIUM-PTP600-MIB", "ethernetBridgingStatusAlarmTrap"))
)
if mibBuilder.loadTexts:
    notificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ptpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 17713, 6, 97)
)
if mibBuilder.loadTexts:
    ptpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-PTP600-MIB",
    **{"cambium": cambium,
       "ptp": ptp,
       "ptmp": ptmp,
       "ptp600": ptp600,
       "dfs": dfs,
       "dfsTableNumber": dfsTableNumber,
       "dfsTable": dfsTable,
       "dfsTableEntry": dfsTableEntry,
       "dfsTableIndex": dfsTableIndex,
       "dfsMeans": dfsMeans,
       "dfsNineNinePointNinePercentiles": dfsNineNinePointNinePercentiles,
       "dfsPeaks": dfsPeaks,
       "bridge": bridge,
       "localPacketFiltering": localPacketFiltering,
       "configuration": configuration,
       "iPAddress": iPAddress,
       "subnetMask": subnetMask,
       "gatewayIPAddress": gatewayIPAddress,
       "targetMACAddress": targetMACAddress,
       "masterSlaveMode": masterSlaveMode,
       "maximumTransmitPower": maximumTransmitPower,
       "antennaGain": antennaGain,
       "cableLoss": cableLoss,
       "eIRP": eIRP,
       "ethernetCappedMaxWirelessSpeed": ethernetCappedMaxWirelessSpeed,
       "channelBandwidth": channelBandwidth,
       "remoteIPAddress": remoteIPAddress,
       "linkName": linkName,
       "siteName": siteName,
       "accessMethod": accessMethod,
       "groupID": groupID,
       "ethernet": ethernet,
       "dataPortAutoNegotiation": dataPortAutoNegotiation,
       "dataPortAutoNegAdvertisement": dataPortAutoNegAdvertisement,
       "dataPortAutoMdix": dataPortAutoMdix,
       "dataPortStatus": dataPortStatus,
       "dataPortSpeedAndDuplex": dataPortSpeedAndDuplex,
       "dataPortWirelessDownAlert": dataPortWirelessDownAlert,
       "useVLANForManagementInterfaces": useVLANForManagementInterfaces,
       "vLANManagementPriority": vLANManagementPriority,
       "vLANManagementVID": vLANManagementVID,
       "managementPortStatus": managementPortStatus,
       "managementPortSpeedAndDuplex": managementPortSpeedAndDuplex,
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
       "managementMode": managementMode,
       "managementPortWirelessDownAlert": managementPortWirelessDownAlert,
       "qOSPriorityScheme": qOSPriorityScheme,
       "unknownNetworkPriorityQueueMapping": unknownNetworkPriorityQueueMapping,
       "dSCPManagementPriority": dSCPManagementPriority,
       "ethernetBridgingStatus": ethernetBridgingStatus,
       "telecom": telecom,
       "telecomsInterface": telecomsInterface,
       "telecomsChannelAStatus": telecomsChannelAStatus,
       "telecomsChannelBStatus": telecomsChannelBStatus,
       "channelALineCode": channelALineCode,
       "channelBLineCode": channelBLineCode,
       "channelACableLength": channelACableLength,
       "channelBCableLength": channelBCableLength,
       "channelALoopback": channelALoopback,
       "channelBLoopback": channelBLoopback,
       "telecomsChannelSelection": telecomsChannelSelection,
       "licence": licence,
       "regionCode": regionCode,
       "productVariant": productVariant,
       "productName": productName,
       "ethernetFiberSupport": ethernetFiberSupport,
       "frequencyVariant": frequencyVariant,
       "bandwidthVariant": bandwidthVariant,
       "constantPowerSpectralDensity": constantPowerSpectralDensity,
       "sNMPv3Enable": sNMPv3Enable,
       "hAZLOCConfiguration": hAZLOCConfiguration,
       "securityLevel": securityLevel,
       "management": management,
       "targetRange": targetRange,
       "rangingMode": rangingMode,
       "installStatus": installStatus,
       "installArmState": installArmState,
       "tFTPServerIPAddress": tFTPServerIPAddress,
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
       "phyControl": phyControl,
       "linkSymmetry": linkSymmetry,
       "linkModeOptimisation": linkModeOptimisation,
       "userConfiguredMaxModulationMode": userConfiguredMaxModulationMode,
       "remoteMaximumTransmitPower": remoteMaximumTransmitPower,
       "txColorCode": txColorCode,
       "rxColorCode": rxColorCode,
       "automaticTxPowerControl": automaticTxPowerControl,
       "remoteRxTargetPower": remoteRxTargetPower,
       "phyStatus": phyStatus,
       "receivePower": receivePower,
       "vectorError": vectorError,
       "transmitPower": transmitPower,
       "range": range,
       "linkLoss": linkLoss,
       "receiveChannel": receiveChannel,
       "transmitChannel": transmitChannel,
       "receiveModulationMode": receiveModulationMode,
       "transmitModulationMode": transmitModulationMode,
       "receiveFreqMHz": receiveFreqMHz,
       "transmitFreqMHz": transmitFreqMHz,
       "signalStrengthRatio": signalStrengthRatio,
       "receiveFreqKHz": receiveFreqKHz,
       "transmitFreqKHz": transmitFreqKHz,
       "searchState": searchState,
       "rawReceivePower": rawReceivePower,
       "alarms": alarms,
       "unitOutOfCalibration": unitOutOfCalibration,
       "encryptionEnabledMismatch": encryptionEnabledMismatch,
       "incompatibleRegionCodes": incompatibleRegionCodes,
       "noWirelessChannelAvailable": noWirelessChannelAvailable,
       "wirelessLinkDisabledWarning": wirelessLinkDisabledWarning,
       "dataPortDisabledWarning": dataPortDisabledWarning,
       "dataPortFiberStatus": dataPortFiberStatus,
       "dataPortConfigurationMismatch": dataPortConfigurationMismatch,
       "incompatibleMasterAndSlave": incompatibleMasterAndSlave,
       "tDDSynchronizationStatus": tDDSynchronizationStatus,
       "managementPortDisabledWarning": managementPortDisabledWarning,
       "tDDSynchronizationAlarm": tDDSynchronizationAlarm,
       "linkModeOptimizationMismatch": linkModeOptimizationMismatch,
       "managementPortConfigurationMismatch": managementPortConfigurationMismatch,
       "secureModeAlarm": secureModeAlarm,
       "ethernetBridgingStatusAlarm": ethernetBridgingStatusAlarm,
       "smtp": smtp,
       "sMTPEmailAlert": sMTPEmailAlert,
       "sMTPServerIPAddress": sMTPServerIPAddress,
       "sMTPServerPortNumber": sMTPServerPortNumber,
       "sMTPSourceEmailAddress": sMTPSourceEmailAddress,
       "sMTPDestinationEmailAddress": sMTPDestinationEmailAddress,
       "sMTPEnabledMessages": sMTPEnabledMessages,
       "snmpControl": snmpControl,
       "sNMPPortNumber": sNMPPortNumber,
       "sNMPCommunityString": sNMPCommunityString,
       "sNMPTrapTableNumber": sNMPTrapTableNumber,
       "sNMPTrapTable": sNMPTrapTable,
       "sNMPTrapTableEntry": sNMPTrapTableEntry,
       "sNMPTrapTableIndex": sNMPTrapTableIndex,
       "sNMPTrapIPAddress": sNMPTrapIPAddress,
       "sNMPTrapPortNumber": sNMPTrapPortNumber,
       "sNMPTrapVersion": sNMPTrapVersion,
       "sNMPEnabledTraps": sNMPEnabledTraps,
       "enabledDiagnosticAlarms": enabledDiagnosticAlarms,
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
       "sNTPServerIPAddress": sNTPServerIPAddress,
       "sNTPServerPortNumber": sNTPServerPortNumber,
       "sNTPServerStatus": sNTPServerStatus,
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
       "ethernetBridgingAvailability": ethernetBridgingAvailability,
       "encryption": encryption,
       "encryptionAlgorithm": encryptionAlgorithm,
       "tDDControl": tDDControl,
       "tDDSynchronizationMode": tDDSynchronizationMode,
       "syslogControl": syslogControl,
       "syslogClient": syslogClient,
       "syslogState": syslogState,
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
       "telecomGroup": telecomGroup,
       "licenceGroup": licenceGroup,
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
       "supplementaryGroup": supplementaryGroup,
       "notificationsGroup": notificationsGroup,
       "ptpTraps": ptpTraps,
       "ptpTrapPrefix": ptpTrapPrefix,
       "dfsChannelChangeTrap": dfsChannelChangeTrap,
       "dfsImpulsiveInterferenceTrap": dfsImpulsiveInterferenceTrap,
       "dataPortStatusTrap": dataPortStatusTrap,
       "telecomsChannelAStatusTrap": telecomsChannelAStatusTrap,
       "telecomsChannelBStatusTrap": telecomsChannelBStatusTrap,
       "channelALoopbackTrap": channelALoopbackTrap,
       "channelBLoopbackTrap": channelBLoopbackTrap,
       "regionCodeTrap": regionCodeTrap,
       "installStatusTrap": installStatusTrap,
       "installArmStateTrap": installArmStateTrap,
       "unitOutOfCalibrationTrap": unitOutOfCalibrationTrap,
       "encryptionEnabledMismatchTrap": encryptionEnabledMismatchTrap,
       "incompatibleRegionCodesTrap": incompatibleRegionCodesTrap,
       "noWirelessChannelAvailableTrap": noWirelessChannelAvailableTrap,
       "wirelessLinkDisabledWarningTrap": wirelessLinkDisabledWarningTrap,
       "dataPortDisabledWarningTrap": dataPortDisabledWarningTrap,
       "dataPortFiberStatusTrap": dataPortFiberStatusTrap,
       "dataPortConfigurationMismatchTrap": dataPortConfigurationMismatchTrap,
       "incompatibleMasterAndSlaveTrap": incompatibleMasterAndSlaveTrap,
       "sNTPSyncTrap": sNTPSyncTrap,
       "tDDSynchronizationAlarmTrap": tDDSynchronizationAlarmTrap,
       "managementPortStatusTrap": managementPortStatusTrap,
       "managementPortDisabledWarningTrap": managementPortDisabledWarningTrap,
       "linkModeOptimizationMismatchTrap": linkModeOptimizationMismatchTrap,
       "managementPortConfigurationMismatchTrap": managementPortConfigurationMismatchTrap,
       "syslogStateTrap": syslogStateTrap,
       "syslogLocalNearlyFullTrap": syslogLocalNearlyFullTrap,
       "syslogLocalWrappedTrap": syslogLocalWrappedTrap,
       "syslogClientTrap": syslogClientTrap,
       "secureModeAlarmTrap": secureModeAlarmTrap,
       "ethernetBridgingStatusAlarmTrap": ethernetBridgingStatusAlarmTrap}
)
