# SNMP MIB module (CAMBIUM-PTP250-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAMBIUM-PTP250-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:26 2024
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
        ("2012-12-07 09:35",
         "2011-10-18 10:47")
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
_Ptp250_ObjectIdentity = ObjectIdentity
ptp250 = _Ptp250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1)
)
_IPAddress_Type = IpAddress
_IPAddress_Object = MibScalar
iPAddress = _IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 1),
    _IPAddress_Type()
)
iPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_GatewayIPAddress_Type = IpAddress
_GatewayIPAddress_Object = MibScalar
gatewayIPAddress = _GatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 3),
    _GatewayIPAddress_Type()
)
gatewayIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayIPAddress.setStatus("current")


class _RemoteMACAddress_Type(OctetString):
    """Custom type remoteMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RemoteMACAddress_Type.__name__ = "OctetString"
_RemoteMACAddress_Object = MibScalar
remoteMACAddress = _RemoteMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 4),
    _RemoteMACAddress_Type()
)
remoteMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMACAddress.setStatus("current")


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
        *(("master", 1),
          ("slave", 0))
    )


_MasterSlaveMode_Type.__name__ = "Integer32"
_MasterSlaveMode_Object = MibScalar
masterSlaveMode = _MasterSlaveMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 5),
    _MasterSlaveMode_Type()
)
masterSlaveMode.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 7),
    _AntennaGain_Type()
)
antennaGain.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 8),
    _CableLoss_Type()
)
cableLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableLoss.setStatus("current")


class _ChannelBandwidth_Type(Integer32):
    """Custom type channelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bw20MHz", 0),
          ("bw40MHz", 1))
    )


_ChannelBandwidth_Type.__name__ = "Integer32"
_ChannelBandwidth_Object = MibScalar
channelBandwidth = _ChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 9),
    _ChannelBandwidth_Type()
)
channelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBandwidth.setStatus("current")
_RemoteIPAddress_Type = IpAddress
_RemoteIPAddress_Object = MibScalar
remoteIPAddress = _RemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 11),
    _LinkName_Type()
)
linkName.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 12),
    _SiteName_Type()
)
siteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteName.setStatus("current")


class _ConfiguredModulationMode_Type(Integer32):
    """Custom type configuredModulationMode based on Integer32"""
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
        *(("mod16QamHalf", 3),
          ("mod16QamThreeQuarters", 4),
          ("mod64QamFiveSixths", 7),
          ("mod64QamThreeQuarters", 6),
          ("mod64QamTwoThirds", 5),
          ("modBpskHalf", 0),
          ("modQpskHalf", 1),
          ("modQpskThreeQuarters", 2))
    )


_ConfiguredModulationMode_Type.__name__ = "Integer32"
_ConfiguredModulationMode_Object = MibScalar
configuredModulationMode = _ConfiguredModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 13),
    _ConfiguredModulationMode_Type()
)
configuredModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configuredModulationMode.setStatus("current")


class _Band_Type(Integer32):
    """Custom type band based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq5400MHz", 1),
          ("freq5800MHz", 2),
          ("unset", 0))
    )


_Band_Type.__name__ = "Integer32"
_Band_Object = MibScalar
band = _Band_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 14),
    _Band_Type()
)
band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    band.setStatus("current")


class _ConfiguredRange_Type(Integer32):
    """Custom type configuredRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5400),
    )


_ConfiguredRange_Type.__name__ = "Integer32"
_ConfiguredRange_Object = MibScalar
configuredRange = _ConfiguredRange_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 15),
    _ConfiguredRange_Type()
)
configuredRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configuredRange.setStatus("current")


class _ChannelSelection_Type(Bits):
    """Custom type channelSelection based on Bits"""
    namedValues = NamedValues(
        *(("channum100", 0),
          ("channum104", 1),
          ("channum108", 2),
          ("channum112", 3),
          ("channum116", 4),
          ("channum120", 5),
          ("channum124", 6),
          ("channum128", 7),
          ("channum132", 8),
          ("channum136", 9),
          ("channum140", 10),
          ("channum149", 11),
          ("channum153", 12),
          ("channum157", 13),
          ("channum161", 14),
          ("channum165", 15))
    )

_ChannelSelection_Type.__name__ = "Bits"
_ChannelSelection_Object = MibScalar
channelSelection = _ChannelSelection_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 16),
    _ChannelSelection_Type()
)
channelSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelSelection.setStatus("current")


class _VlanTagging_Type(Integer32):
    """Custom type vlanTagging based on Integer32"""
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


_VlanTagging_Type.__name__ = "Integer32"
_VlanTagging_Object = MibScalar
vlanTagging = _VlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 17),
    _VlanTagging_Type()
)
vlanTagging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTagging.setStatus("current")


class _VlanId_Type(Integer32):
    """Custom type vlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VlanId_Type.__name__ = "Integer32"
_VlanId_Object = MibScalar
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 18),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")


class _VlanPriority_Type(Integer32):
    """Custom type vlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanPriority_Type.__name__ = "Integer32"
_VlanPriority_Object = MibScalar
vlanPriority = _VlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 19),
    _VlanPriority_Type()
)
vlanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPriority.setStatus("current")


class _FixedModMode_Type(Integer32):
    """Custom type fixedModMode based on Integer32"""
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


_FixedModMode_Type.__name__ = "Integer32"
_FixedModMode_Object = MibScalar
fixedModMode = _FixedModMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 22),
    _FixedModMode_Type()
)
fixedModMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fixedModMode.setStatus("current")


class _DualPayload_Type(Integer32):
    """Custom type dualPayload based on Integer32"""
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


_DualPayload_Type.__name__ = "Integer32"
_DualPayload_Object = MibScalar
dualPayload = _DualPayload_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 1, 23),
    _DualPayload_Type()
)
dualPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualPayload.setStatus("current")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 2)
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 2, 1),
    _DataPortAutoNegotiation_Type()
)
dataPortAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortAutoNegotiation.setStatus("current")


class _DataPortAutoNegAdvertisement_Type(Bits):
    """Custom type dataPortAutoNegAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("neg1000MbpsFullDuplex", 5),
          ("neg100MbpsFullDuplex", 4),
          ("neg100MbpsHalfDuplex", 3),
          ("neg10MbpsFullDuplex", 2),
          ("neg10MbpsHalfDuplex", 1),
          ("negInvalid", 0))
    )

_DataPortAutoNegAdvertisement_Type.__name__ = "Bits"
_DataPortAutoNegAdvertisement_Object = MibScalar
dataPortAutoNegAdvertisement = _DataPortAutoNegAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 2, 2),
    _DataPortAutoNegAdvertisement_Type()
)
dataPortAutoNegAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortAutoNegAdvertisement.setStatus("current")


class _DataPortStatus_Type(Integer32):
    """Custom type dataPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_DataPortStatus_Type.__name__ = "Integer32"
_DataPortStatus_Object = MibScalar
dataPortStatus = _DataPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 2, 4),
    _DataPortSpeedAndDuplex_Type()
)
dataPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortSpeedAndDuplex.setStatus("current")
_Licence_ObjectIdentity = ObjectIdentity
licence = _Licence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 3)
)


class _RegionCode_Type(DisplayString):
    """Custom type regionCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RegionCode_Type.__name__ = "DisplayString"
_RegionCode_Object = MibScalar
regionCode = _RegionCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 3, 1),
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
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ptp250", 16),
          ("ptp800", 15),
          ("ptpXX300", 5),
          ("ptpXX400Deprecated1", 1),
          ("ptpXX400Deprecated2", 2),
          ("ptpXX400Full", 0),
          ("ptpXX400Lite", 3),
          ("ptpXX500", 10),
          ("ptpXX500FullDeprecated", 8),
          ("ptpXX500LiteDeprecated", 9),
          ("ptpXX600Full", 12),
          ("ptpXX600Lite", 11),
          ("spare1", 4),
          ("spare2", 6),
          ("spare3", 7),
          ("spare5", 13),
          ("spare6", 14))
    )


_ProductVariant_Type.__name__ = "Integer32"
_ProductVariant_Object = MibScalar
productVariant = _ProductVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 3, 3),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 4)
)


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
    (1, 3, 6, 1, 4, 1, 17713, 250, 4, 1),
    _InstallArmState_Type()
)
installArmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installArmState.setStatus("current")
_TFTPServerIPAddress_Type = IpAddress
_TFTPServerIPAddress_Object = MibScalar
tFTPServerIPAddress = _TFTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 4, 2),
    _TFTPServerIPAddress_Type()
)
tFTPServerIPAddress.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 4, 3),
    _TFTPServerPortNumber_Type()
)
tFTPServerPortNumber.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 4, 4),
    _TFTPSoftwareUpgradeFileName_Type()
)
tFTPSoftwareUpgradeFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeFileName.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 250, 4, 5),
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 4, 6),
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 4, 7),
    _TFTPSoftwareUpgradeStatusAdditionalText_Type()
)
tFTPSoftwareUpgradeStatusAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeStatusAdditionalText.setStatus("current")
_PhyStatus_ObjectIdentity = ObjectIdentity
phyStatus = _PhyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5)
)
_ReceivePower_Type = Integer32
_ReceivePower_Object = MibScalar
receivePower = _ReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 1),
    _ReceivePower_Type()
)
receivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivePower.setStatus("current")
_VectorError_Type = Integer32
_VectorError_Object = MibScalar
vectorError = _VectorError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 2),
    _VectorError_Type()
)
vectorError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vectorError.setStatus("current")
_TransmitPower_Type = Integer32
_TransmitPower_Object = MibScalar
transmitPower = _TransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 3),
    _TransmitPower_Type()
)
transmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitPower.setStatus("current")


class _LinkLoss_Type(Integer32):
    """Custom type linkLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_LinkLoss_Type.__name__ = "Integer32"
_LinkLoss_Object = MibScalar
linkLoss = _LinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 5),
    _LinkLoss_Type()
)
linkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLoss.setStatus("current")


class _CurrentChannel_Type(Integer32):
    """Custom type currentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CurrentChannel_Type.__name__ = "Integer32"
_CurrentChannel_Object = MibScalar
currentChannel = _CurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 6),
    _CurrentChannel_Type()
)
currentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentChannel.setStatus("current")


class _ExtendedChannel_Type(Integer32):
    """Custom type extendedChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ExtendedChannel_Type.__name__ = "Integer32"
_ExtendedChannel_Object = MibScalar
extendedChannel = _ExtendedChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 7),
    _ExtendedChannel_Type()
)
extendedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendedChannel.setStatus("current")


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
              16)
        )
    )
    namedValues = NamedValues(
        *(("acquisition", 0),
          ("mod16QamHalfDual", 12),
          ("mod16QamHalfSingle", 4),
          ("mod16QamThreeQuartersDual", 13),
          ("mod16QamThreeQuartersSingle", 5),
          ("mod64QamFiveSixthsDual", 16),
          ("mod64QamFiveSixthsSingle", 8),
          ("mod64QamThreeQuartersDual", 15),
          ("mod64QamThreeQuartersSingle", 7),
          ("mod64QamTwoThirdsDual", 14),
          ("mod64QamTwoThirdsSingle", 6),
          ("modBpskHalfDual", 9),
          ("modBpskHalfSingle", 1),
          ("modQpskHalfDual", 10),
          ("modQpskHalfSingle", 2),
          ("modQpskThreeQuartersDual", 11),
          ("modQpskThreeQuartersSingle", 3))
    )


_ReceiveModulationMode_Type.__name__ = "Integer32"
_ReceiveModulationMode_Object = MibScalar
receiveModulationMode = _ReceiveModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 8),
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("acquisition", 0),
          ("mod16QamHalfDual", 12),
          ("mod16QamHalfSingle", 4),
          ("mod16QamThreeQuartersDual", 13),
          ("mod16QamThreeQuartersSingle", 5),
          ("mod64QamFiveSixthsDual", 16),
          ("mod64QamFiveSixthsSingle", 8),
          ("mod64QamThreeQuartersDual", 15),
          ("mod64QamThreeQuartersSingle", 7),
          ("mod64QamTwoThirdsDual", 14),
          ("mod64QamTwoThirdsSingle", 6),
          ("modBpskHalfDual", 9),
          ("modBpskHalfSingle", 1),
          ("modQpskHalfDual", 10),
          ("modQpskHalfSingle", 2),
          ("modQpskThreeQuartersDual", 11),
          ("modQpskThreeQuartersSingle", 3))
    )


_TransmitModulationMode_Type.__name__ = "Integer32"
_TransmitModulationMode_Object = MibScalar
transmitModulationMode = _TransmitModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 9),
    _TransmitModulationMode_Type()
)
transmitModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitModulationMode.setStatus("current")
_CurrentFreqMHz_Type = Integer32
_CurrentFreqMHz_Object = MibScalar
currentFreqMHz = _CurrentFreqMHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 11),
    _CurrentFreqMHz_Type()
)
currentFreqMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFreqMHz.setStatus("current")
_ExtendedFreqMHz_Type = Integer32
_ExtendedFreqMHz_Object = MibScalar
extendedFreqMHz = _ExtendedFreqMHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 12),
    _ExtendedFreqMHz_Type()
)
extendedFreqMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendedFreqMHz.setStatus("current")
_SignalStrengthRatio_Type = Integer32
_SignalStrengthRatio_Object = MibScalar
signalStrengthRatio = _SignalStrengthRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 13),
    _SignalStrengthRatio_Type()
)
signalStrengthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalStrengthRatio.setStatus("current")


class _SearchState_Type(Integer32):
    """Custom type searchState based on Integer32"""
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
        *(("acquiring", 2),
          ("initialising", 5),
          ("noChannels", 6),
          ("radarCAC", 4),
          ("registering", 1),
          ("searching", 3),
          ("up", 0))
    )


_SearchState_Type.__name__ = "Integer32"
_SearchState_Object = MibScalar
searchState = _SearchState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 14),
    _SearchState_Type()
)
searchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    searchState.setStatus("current")
_NoiseFloor_Type = Integer32
_NoiseFloor_Object = MibScalar
noiseFloor = _NoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 15),
    _NoiseFloor_Type()
)
noiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiseFloor.setStatus("current")


class _RadarDetectChannel_Type(Integer32):
    """Custom type radarDetectChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RadarDetectChannel_Type.__name__ = "Integer32"
_RadarDetectChannel_Object = MibScalar
radarDetectChannel = _RadarDetectChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 16),
    _RadarDetectChannel_Type()
)
radarDetectChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    radarDetectChannel.setStatus("current")
_MeasuredRange_Type = Integer32
_MeasuredRange_Object = MibScalar
measuredRange = _MeasuredRange_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 5, 17),
    _MeasuredRange_Type()
)
measuredRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measuredRange.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 6)
)


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
    (1, 3, 6, 1, 4, 1, 17713, 250, 6, 1),
    _NoWirelessChannelAvailable_Type()
)
noWirelessChannelAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noWirelessChannelAvailable.setStatus("current")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 7)
)
_SMTPServerIPAddress_Type = IpAddress
_SMTPServerIPAddress_Object = MibScalar
sMTPServerIPAddress = _SMTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 7, 1),
    _SMTPServerIPAddress_Type()
)
sMTPServerIPAddress.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 7, 2),
    _SMTPServerPortNumber_Type()
)
sMTPServerPortNumber.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 7, 3),
    _SMTPSourceEmailAddress_Type()
)
sMTPSourceEmailAddress.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 7, 4),
    _SMTPDestinationEmailAddress_Type()
)
sMTPDestinationEmailAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sMTPDestinationEmailAddress.setStatus("current")


class _SMTPEnabledMessages_Type(Bits):
    """Custom type sMTPEnabledMessages based on Bits"""
    namedValues = NamedValues(
        *(("coldStart", 2),
          ("dataPortUpDown", 0),
          ("installArmState", 4),
          ("noChannelAvailable", 5),
          ("radarDetect", 3),
          ("wirelessLinkUpDown", 1))
    )

_SMTPEnabledMessages_Type.__name__ = "Bits"
_SMTPEnabledMessages_Object = MibScalar
sMTPEnabledMessages = _SMTPEnabledMessages_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 7, 5),
    _SMTPEnabledMessages_Type()
)
sMTPEnabledMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sMTPEnabledMessages.setStatus("current")
_SnmpControl_ObjectIdentity = ObjectIdentity
snmpControl = _SnmpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8)
)


class _SNMPCommunityTableNumber_Type(Integer32):
    """Custom type sNMPCommunityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_SNMPCommunityTableNumber_Type.__name__ = "Integer32"
_SNMPCommunityTableNumber_Object = MibScalar
sNMPCommunityTableNumber = _SNMPCommunityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 1),
    _SNMPCommunityTableNumber_Type()
)
sNMPCommunityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPCommunityTableNumber.setStatus("current")
_SNMPCommunityTable_Object = MibTable
sNMPCommunityTable = _SNMPCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 2)
)
if mibBuilder.loadTexts:
    sNMPCommunityTable.setStatus("current")
_SNMPCommunityTableEntry_Object = MibTableRow
sNMPCommunityTableEntry = _SNMPCommunityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 2, 1)
)
sNMPCommunityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP250-MIB", "sNMPCommunityTableIndex"),
)
if mibBuilder.loadTexts:
    sNMPCommunityTableEntry.setStatus("current")


class _SNMPCommunityTableIndex_Type(Integer32):
    """Custom type sNMPCommunityTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SNMPCommunityTableIndex_Type.__name__ = "Integer32"
_SNMPCommunityTableIndex_Object = MibTableColumn
sNMPCommunityTableIndex = _SNMPCommunityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 2, 1, 1),
    _SNMPCommunityTableIndex_Type()
)
sNMPCommunityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sNMPCommunityTableIndex.setStatus("current")
_SNMPCommunityString_Type = OctetString
_SNMPCommunityString_Object = MibTableColumn
sNMPCommunityString = _SNMPCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 2, 1, 2),
    _SNMPCommunityString_Type()
)
sNMPCommunityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPCommunityString.setStatus("current")


class _SNMPCommunityAccess_Type(Integer32):
    """Custom type sNMPCommunityAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 0),
          ("readWrite", 1))
    )


_SNMPCommunityAccess_Type.__name__ = "Integer32"
_SNMPCommunityAccess_Object = MibTableColumn
sNMPCommunityAccess = _SNMPCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 2, 1, 3),
    _SNMPCommunityAccess_Type()
)
sNMPCommunityAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPCommunityAccess.setStatus("current")
_SNMPCommunityOid_Type = ObjectIdentifier
_SNMPCommunityOid_Object = MibTableColumn
sNMPCommunityOid = _SNMPCommunityOid_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 2, 1, 4),
    _SNMPCommunityOid_Type()
)
sNMPCommunityOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPCommunityOid.setStatus("current")


class _SNMPTrapTableNumber_Type(Integer32):
    """Custom type sNMPTrapTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_SNMPTrapTableNumber_Type.__name__ = "Integer32"
_SNMPTrapTableNumber_Object = MibScalar
sNMPTrapTableNumber = _SNMPTrapTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 3),
    _SNMPTrapTableNumber_Type()
)
sNMPTrapTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapTableNumber.setStatus("current")
_SNMPTrapTable_Object = MibTable
sNMPTrapTable = _SNMPTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 4)
)
if mibBuilder.loadTexts:
    sNMPTrapTable.setStatus("current")
_SNMPTrapTableEntry_Object = MibTableRow
sNMPTrapTableEntry = _SNMPTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1)
)
sNMPTrapTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP250-MIB", "sNMPTrapTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1, 1),
    _SNMPTrapTableIndex_Type()
)
sNMPTrapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sNMPTrapTableIndex.setStatus("current")
_SNMPTrapIPAddress_Type = IpAddress
_SNMPTrapIPAddress_Object = MibTableColumn
sNMPTrapIPAddress = _SNMPTrapIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1, 2),
    _SNMPTrapIPAddress_Type()
)
sNMPTrapIPAddress.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1, 3),
    _SNMPTrapPortNumber_Type()
)
sNMPTrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapPortNumber.setStatus("current")
_SNMPTrapCommunity_Type = OctetString
_SNMPTrapCommunity_Object = MibTableColumn
sNMPTrapCommunity = _SNMPTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1, 4),
    _SNMPTrapCommunity_Type()
)
sNMPTrapCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapCommunity.setStatus("current")


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
_SNMPTrapVersion_Object = MibTableColumn
sNMPTrapVersion = _SNMPTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 4, 1, 5),
    _SNMPTrapVersion_Type()
)
sNMPTrapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapVersion.setStatus("current")


class _SNMPEnabledTraps_Type(Bits):
    """Custom type sNMPEnabledTraps based on Bits"""
    namedValues = NamedValues(
        *(("coldStart", 2),
          ("dataPortUpDown", 0),
          ("installArmState", 4),
          ("noChannelAvailable", 5),
          ("radarDetect", 3),
          ("wirelessLinkUpDown", 1))
    )

_SNMPEnabledTraps_Type.__name__ = "Bits"
_SNMPEnabledTraps_Object = MibScalar
sNMPEnabledTraps = _SNMPEnabledTraps_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 8, 6),
    _SNMPEnabledTraps_Type()
)
sNMPEnabledTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPEnabledTraps.setStatus("current")
_Ntp_ObjectIdentity = ObjectIdentity
ntp = _Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 9)
)


class _NTPState_Type(Integer32):
    """Custom type nTPState based on Integer32"""
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


_NTPState_Type.__name__ = "Integer32"
_NTPState_Object = MibScalar
nTPState = _NTPState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 9, 1),
    _NTPState_Type()
)
nTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nTPState.setStatus("current")


class _NTPPollInterval_Type(Integer32):
    """Custom type nTPPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 43200),
    )


_NTPPollInterval_Type.__name__ = "Integer32"
_NTPPollInterval_Object = MibScalar
nTPPollInterval = _NTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 9, 2),
    _NTPPollInterval_Type()
)
nTPPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nTPPollInterval.setStatus("current")


class _NTPSync_Type(Integer32):
    """Custom type nTPSync based on Integer32"""
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


_NTPSync_Type.__name__ = "Integer32"
_NTPSync_Object = MibScalar
nTPSync = _NTPSync_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 9, 3),
    _NTPSync_Type()
)
nTPSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nTPSync.setStatus("current")
_NTPLastSync_Type = Integer32
_NTPLastSync_Object = MibScalar
nTPLastSync = _NTPLastSync_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 9, 4),
    _NTPLastSync_Type()
)
nTPLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nTPLastSync.setStatus("current")
_SystemClock_Type = Integer32
_SystemClock_Object = MibScalar
systemClock = _SystemClock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 9, 5),
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 9, 6),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")
_NTPServerIp_Type = IpAddress
_NTPServerIp_Object = MibScalar
nTPServerIp = _NTPServerIp_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 9, 7),
    _NTPServerIp_Type()
)
nTPServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nTPServerIp.setStatus("current")


class _NTPServerPortNumber_Type(Integer32):
    """Custom type nTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NTPServerPortNumber_Type.__name__ = "Integer32"
_NTPServerPortNumber_Object = MibScalar
nTPServerPortNumber = _NTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 9, 8),
    _NTPServerPortNumber_Type()
)
nTPServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nTPServerPortNumber.setStatus("current")
_Versions_ObjectIdentity = ObjectIdentity
versions = _Versions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 10)
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 10, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 250, 10, 2),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")


class _BootVersion_Type(DisplayString):
    """Custom type bootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BootVersion_Type.__name__ = "DisplayString"
_BootVersion_Object = MibScalar
bootVersion = _BootVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 10, 3),
    _BootVersion_Type()
)
bootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersion.setStatus("current")
_PubStats_ObjectIdentity = ObjectIdentity
pubStats = _PubStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 11)
)
_ReceiveDataRate_Type = Integer32
_ReceiveDataRate_Object = MibScalar
receiveDataRate = _ReceiveDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 11, 1),
    _ReceiveDataRate_Type()
)
receiveDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveDataRate.setStatus("current")
_TransmitDataRate_Type = Integer32
_TransmitDataRate_Object = MibScalar
transmitDataRate = _TransmitDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 11, 2),
    _TransmitDataRate_Type()
)
transmitDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitDataRate.setStatus("current")
_AggregateDataRate_Type = Integer32
_AggregateDataRate_Object = MibScalar
aggregateDataRate = _AggregateDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 11, 3),
    _AggregateDataRate_Type()
)
aggregateDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregateDataRate.setStatus("current")


class _WirelessLinkStatus_Type(Integer32):
    """Custom type wirelessLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_WirelessLinkStatus_Type.__name__ = "Integer32"
_WirelessLinkStatus_Object = MibScalar
wirelessLinkStatus = _WirelessLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 250, 11, 4),
    _WirelessLinkStatus_Type()
)
wirelessLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatus.setStatus("current")
_PtpGroups_ObjectIdentity = ObjectIdentity
ptpGroups = _PtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98)
)
_PtpTraps_ObjectIdentity = ObjectIdentity
ptpTraps = _PtpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 99)
)
_PtpTrapPrefix_ObjectIdentity = ObjectIdentity
ptpTrapPrefix = _PtpTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 250, 99, 0)
)

# Managed Objects groups

configurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 5)
)
configurationGroup.setObjects(
      *(("CAMBIUM-PTP250-MIB", "iPAddress"),
        ("CAMBIUM-PTP250-MIB", "subnetMask"),
        ("CAMBIUM-PTP250-MIB", "gatewayIPAddress"),
        ("CAMBIUM-PTP250-MIB", "masterSlaveMode"),
        ("CAMBIUM-PTP250-MIB", "maximumTransmitPower"),
        ("CAMBIUM-PTP250-MIB", "antennaGain"),
        ("CAMBIUM-PTP250-MIB", "cableLoss"),
        ("CAMBIUM-PTP250-MIB", "channelBandwidth"),
        ("CAMBIUM-PTP250-MIB", "remoteIPAddress"),
        ("CAMBIUM-PTP250-MIB", "remoteMACAddress"),
        ("CAMBIUM-PTP250-MIB", "linkName"),
        ("CAMBIUM-PTP250-MIB", "siteName"),
        ("CAMBIUM-PTP250-MIB", "band"),
        ("CAMBIUM-PTP250-MIB", "configuredModulationMode"),
        ("CAMBIUM-PTP250-MIB", "configuredRange"),
        ("CAMBIUM-PTP250-MIB", "channelSelection"),
        ("CAMBIUM-PTP250-MIB", "vlanTagging"),
        ("CAMBIUM-PTP250-MIB", "vlanId"),
        ("CAMBIUM-PTP250-MIB", "vlanPriority"),
        ("CAMBIUM-PTP250-MIB", "fixedModMode"),
        ("CAMBIUM-PTP250-MIB", "dualPayload"))
)
if mibBuilder.loadTexts:
    configurationGroup.setStatus("current")

ethernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 6)
)
ethernetGroup.setObjects(
      *(("CAMBIUM-PTP250-MIB", "dataPortAutoNegotiation"),
        ("CAMBIUM-PTP250-MIB", "dataPortAutoNegAdvertisement"),
        ("CAMBIUM-PTP250-MIB", "dataPortStatus"),
        ("CAMBIUM-PTP250-MIB", "dataPortSpeedAndDuplex"))
)
if mibBuilder.loadTexts:
    ethernetGroup.setStatus("current")

licenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 8)
)
licenceGroup.setObjects(
      *(("CAMBIUM-PTP250-MIB", "regionCode"),
        ("CAMBIUM-PTP250-MIB", "productVariant"),
        ("CAMBIUM-PTP250-MIB", "productName"))
)
if mibBuilder.loadTexts:
    licenceGroup.setStatus("current")

managementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 9)
)
managementGroup.setObjects(
      *(("CAMBIUM-PTP250-MIB", "installArmState"),
        ("CAMBIUM-PTP250-MIB", "tFTPServerIPAddress"),
        ("CAMBIUM-PTP250-MIB", "tFTPServerPortNumber"),
        ("CAMBIUM-PTP250-MIB", "tFTPSoftwareUpgradeFileName"),
        ("CAMBIUM-PTP250-MIB", "tFTPSoftwareUpgradeStatus"),
        ("CAMBIUM-PTP250-MIB", "tFTPSoftwareUpgradeStatusText"),
        ("CAMBIUM-PTP250-MIB", "tFTPSoftwareUpgradeStatusAdditionalText"))
)
if mibBuilder.loadTexts:
    managementGroup.setStatus("current")

phyStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 12)
)
phyStatusGroup.setObjects(
      *(("CAMBIUM-PTP250-MIB", "receivePower"),
        ("CAMBIUM-PTP250-MIB", "vectorError"),
        ("CAMBIUM-PTP250-MIB", "transmitPower"),
        ("CAMBIUM-PTP250-MIB", "linkLoss"),
        ("CAMBIUM-PTP250-MIB", "currentChannel"),
        ("CAMBIUM-PTP250-MIB", "extendedChannel"),
        ("CAMBIUM-PTP250-MIB", "receiveModulationMode"),
        ("CAMBIUM-PTP250-MIB", "transmitModulationMode"),
        ("CAMBIUM-PTP250-MIB", "currentFreqMHz"),
        ("CAMBIUM-PTP250-MIB", "extendedFreqMHz"),
        ("CAMBIUM-PTP250-MIB", "signalStrengthRatio"),
        ("CAMBIUM-PTP250-MIB", "searchState"),
        ("CAMBIUM-PTP250-MIB", "noiseFloor"),
        ("CAMBIUM-PTP250-MIB", "radarDetectChannel"),
        ("CAMBIUM-PTP250-MIB", "measuredRange"))
)
if mibBuilder.loadTexts:
    phyStatusGroup.setStatus("current")

alarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 13)
)
alarmsGroup.setObjects(
    ("CAMBIUM-PTP250-MIB", "noWirelessChannelAvailable")
)
if mibBuilder.loadTexts:
    alarmsGroup.setStatus("current")

smtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 15)
)
smtpGroup.setObjects(
      *(("CAMBIUM-PTP250-MIB", "sMTPServerIPAddress"),
        ("CAMBIUM-PTP250-MIB", "sMTPServerPortNumber"),
        ("CAMBIUM-PTP250-MIB", "sMTPSourceEmailAddress"),
        ("CAMBIUM-PTP250-MIB", "sMTPDestinationEmailAddress"),
        ("CAMBIUM-PTP250-MIB", "sMTPEnabledMessages"))
)
if mibBuilder.loadTexts:
    smtpGroup.setStatus("current")

snmpControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 16)
)
snmpControlGroup.setObjects(
      *(("CAMBIUM-PTP250-MIB", "sNMPCommunityTableNumber"),
        ("CAMBIUM-PTP250-MIB", "sNMPTrapTableNumber"),
        ("CAMBIUM-PTP250-MIB", "sNMPEnabledTraps"),
        ("CAMBIUM-PTP250-MIB", "sNMPTrapIPAddress"),
        ("CAMBIUM-PTP250-MIB", "sNMPTrapPortNumber"),
        ("CAMBIUM-PTP250-MIB", "sNMPCommunityString"),
        ("CAMBIUM-PTP250-MIB", "sNMPCommunityAccess"),
        ("CAMBIUM-PTP250-MIB", "sNMPCommunityOid"),
        ("CAMBIUM-PTP250-MIB", "sNMPTrapCommunity"),
        ("CAMBIUM-PTP250-MIB", "sNMPTrapVersion"))
)
if mibBuilder.loadTexts:
    snmpControlGroup.setStatus("current")

ntpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 17)
)
ntpGroup.setObjects(
      *(("CAMBIUM-PTP250-MIB", "nTPState"),
        ("CAMBIUM-PTP250-MIB", "nTPPollInterval"),
        ("CAMBIUM-PTP250-MIB", "nTPSync"),
        ("CAMBIUM-PTP250-MIB", "nTPLastSync"),
        ("CAMBIUM-PTP250-MIB", "systemClock"),
        ("CAMBIUM-PTP250-MIB", "timeZone"),
        ("CAMBIUM-PTP250-MIB", "nTPServerIp"),
        ("CAMBIUM-PTP250-MIB", "nTPServerPortNumber"))
)
if mibBuilder.loadTexts:
    ntpGroup.setStatus("current")

versionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 19)
)
versionsGroup.setObjects(
      *(("CAMBIUM-PTP250-MIB", "softwareVersion"),
        ("CAMBIUM-PTP250-MIB", "hardwareVersion"),
        ("CAMBIUM-PTP250-MIB", "bootVersion"))
)
if mibBuilder.loadTexts:
    versionsGroup.setStatus("current")

pubStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 20)
)
pubStatsGroup.setObjects(
      *(("CAMBIUM-PTP250-MIB", "receiveDataRate"),
        ("CAMBIUM-PTP250-MIB", "transmitDataRate"),
        ("CAMBIUM-PTP250-MIB", "aggregateDataRate"),
        ("CAMBIUM-PTP250-MIB", "wirelessLinkStatus"))
)
if mibBuilder.loadTexts:
    pubStatsGroup.setStatus("current")


# Notification objects

dataPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 250, 99, 0, 1)
)
dataPortStatusTrap.setObjects(
    ("CAMBIUM-PTP250-MIB", "dataPortStatus")
)
if mibBuilder.loadTexts:
    dataPortStatusTrap.setStatus(
        "current"
    )

installArmStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 250, 99, 0, 2)
)
installArmStateTrap.setObjects(
    ("CAMBIUM-PTP250-MIB", "installArmState")
)
if mibBuilder.loadTexts:
    installArmStateTrap.setStatus(
        "current"
    )

noWirelessChannelAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 250, 99, 0, 3)
)
noWirelessChannelAvailableTrap.setObjects(
    ("CAMBIUM-PTP250-MIB", "noWirelessChannelAvailable")
)
if mibBuilder.loadTexts:
    noWirelessChannelAvailableTrap.setStatus(
        "current"
    )

linkStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 250, 99, 0, 4)
)
linkStatusTrap.setObjects(
    ("CAMBIUM-PTP250-MIB", "wirelessLinkStatus")
)
if mibBuilder.loadTexts:
    linkStatusTrap.setStatus(
        "current"
    )

radarDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 250, 99, 0, 5)
)
radarDetectTrap.setObjects(
    ("CAMBIUM-PTP250-MIB", "radarDetectChannel")
)
if mibBuilder.loadTexts:
    radarDetectTrap.setStatus(
        "current"
    )


# Notifications groups

notificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 17713, 250, 98, 99)
)
notificationsGroup.setObjects(
      *(("CAMBIUM-PTP250-MIB", "dataPortStatusTrap"),
        ("CAMBIUM-PTP250-MIB", "installArmStateTrap"),
        ("CAMBIUM-PTP250-MIB", "noWirelessChannelAvailableTrap"),
        ("CAMBIUM-PTP250-MIB", "linkStatusTrap"),
        ("CAMBIUM-PTP250-MIB", "radarDetectTrap"))
)
if mibBuilder.loadTexts:
    notificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ptpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 17713, 250, 97)
)
if mibBuilder.loadTexts:
    ptpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-PTP250-MIB",
    **{"cambium": cambium,
       "ptp": ptp,
       "ptmp": ptmp,
       "ptp250": ptp250,
       "configuration": configuration,
       "iPAddress": iPAddress,
       "subnetMask": subnetMask,
       "gatewayIPAddress": gatewayIPAddress,
       "remoteMACAddress": remoteMACAddress,
       "masterSlaveMode": masterSlaveMode,
       "maximumTransmitPower": maximumTransmitPower,
       "antennaGain": antennaGain,
       "cableLoss": cableLoss,
       "channelBandwidth": channelBandwidth,
       "remoteIPAddress": remoteIPAddress,
       "linkName": linkName,
       "siteName": siteName,
       "configuredModulationMode": configuredModulationMode,
       "band": band,
       "configuredRange": configuredRange,
       "channelSelection": channelSelection,
       "vlanTagging": vlanTagging,
       "vlanId": vlanId,
       "vlanPriority": vlanPriority,
       "fixedModMode": fixedModMode,
       "dualPayload": dualPayload,
       "ethernet": ethernet,
       "dataPortAutoNegotiation": dataPortAutoNegotiation,
       "dataPortAutoNegAdvertisement": dataPortAutoNegAdvertisement,
       "dataPortStatus": dataPortStatus,
       "dataPortSpeedAndDuplex": dataPortSpeedAndDuplex,
       "licence": licence,
       "regionCode": regionCode,
       "productVariant": productVariant,
       "productName": productName,
       "management": management,
       "installArmState": installArmState,
       "tFTPServerIPAddress": tFTPServerIPAddress,
       "tFTPServerPortNumber": tFTPServerPortNumber,
       "tFTPSoftwareUpgradeFileName": tFTPSoftwareUpgradeFileName,
       "tFTPSoftwareUpgradeStatus": tFTPSoftwareUpgradeStatus,
       "tFTPSoftwareUpgradeStatusText": tFTPSoftwareUpgradeStatusText,
       "tFTPSoftwareUpgradeStatusAdditionalText": tFTPSoftwareUpgradeStatusAdditionalText,
       "phyStatus": phyStatus,
       "receivePower": receivePower,
       "vectorError": vectorError,
       "transmitPower": transmitPower,
       "linkLoss": linkLoss,
       "currentChannel": currentChannel,
       "extendedChannel": extendedChannel,
       "receiveModulationMode": receiveModulationMode,
       "transmitModulationMode": transmitModulationMode,
       "currentFreqMHz": currentFreqMHz,
       "extendedFreqMHz": extendedFreqMHz,
       "signalStrengthRatio": signalStrengthRatio,
       "searchState": searchState,
       "noiseFloor": noiseFloor,
       "radarDetectChannel": radarDetectChannel,
       "measuredRange": measuredRange,
       "alarms": alarms,
       "noWirelessChannelAvailable": noWirelessChannelAvailable,
       "smtp": smtp,
       "sMTPServerIPAddress": sMTPServerIPAddress,
       "sMTPServerPortNumber": sMTPServerPortNumber,
       "sMTPSourceEmailAddress": sMTPSourceEmailAddress,
       "sMTPDestinationEmailAddress": sMTPDestinationEmailAddress,
       "sMTPEnabledMessages": sMTPEnabledMessages,
       "snmpControl": snmpControl,
       "sNMPCommunityTableNumber": sNMPCommunityTableNumber,
       "sNMPCommunityTable": sNMPCommunityTable,
       "sNMPCommunityTableEntry": sNMPCommunityTableEntry,
       "sNMPCommunityTableIndex": sNMPCommunityTableIndex,
       "sNMPCommunityString": sNMPCommunityString,
       "sNMPCommunityAccess": sNMPCommunityAccess,
       "sNMPCommunityOid": sNMPCommunityOid,
       "sNMPTrapTableNumber": sNMPTrapTableNumber,
       "sNMPTrapTable": sNMPTrapTable,
       "sNMPTrapTableEntry": sNMPTrapTableEntry,
       "sNMPTrapTableIndex": sNMPTrapTableIndex,
       "sNMPTrapIPAddress": sNMPTrapIPAddress,
       "sNMPTrapPortNumber": sNMPTrapPortNumber,
       "sNMPTrapCommunity": sNMPTrapCommunity,
       "sNMPTrapVersion": sNMPTrapVersion,
       "sNMPEnabledTraps": sNMPEnabledTraps,
       "ntp": ntp,
       "nTPState": nTPState,
       "nTPPollInterval": nTPPollInterval,
       "nTPSync": nTPSync,
       "nTPLastSync": nTPLastSync,
       "systemClock": systemClock,
       "timeZone": timeZone,
       "nTPServerIp": nTPServerIp,
       "nTPServerPortNumber": nTPServerPortNumber,
       "versions": versions,
       "softwareVersion": softwareVersion,
       "hardwareVersion": hardwareVersion,
       "bootVersion": bootVersion,
       "pubStats": pubStats,
       "receiveDataRate": receiveDataRate,
       "transmitDataRate": transmitDataRate,
       "aggregateDataRate": aggregateDataRate,
       "wirelessLinkStatus": wirelessLinkStatus,
       "ptpCompliance": ptpCompliance,
       "ptpGroups": ptpGroups,
       "configurationGroup": configurationGroup,
       "ethernetGroup": ethernetGroup,
       "licenceGroup": licenceGroup,
       "managementGroup": managementGroup,
       "phyStatusGroup": phyStatusGroup,
       "alarmsGroup": alarmsGroup,
       "smtpGroup": smtpGroup,
       "snmpControlGroup": snmpControlGroup,
       "ntpGroup": ntpGroup,
       "versionsGroup": versionsGroup,
       "pubStatsGroup": pubStatsGroup,
       "notificationsGroup": notificationsGroup,
       "ptpTraps": ptpTraps,
       "ptpTrapPrefix": ptpTrapPrefix,
       "dataPortStatusTrap": dataPortStatusTrap,
       "installArmStateTrap": installArmStateTrap,
       "noWirelessChannelAvailableTrap": noWirelessChannelAvailableTrap,
       "linkStatusTrap": linkStatusTrap,
       "radarDetectTrap": radarDetectTrap}
)
