# SNMP MIB module (CAMBIUM-PTP800-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAMBIUM-PTP800-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:28 2024
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
        ("2012-04-20 12:26",
         "2011-08-19 12:29",
         "2011-03-16 17:23",
         "2010-09-30 16:29",
         "2010-07-30 13:07",
         "2010-05-27 19:52",
         "2010-03-31 13:09",
         "2010-01-04 18:33",
         "2009-10-21 14:26")
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
_Ptp800_ObjectIdentity = ObjectIdentity
ptp800 = _Ptp800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8)
)
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 4)
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 4, 1),
    _LocalPacketFiltering_Type()
)
localPacketFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localPacketFiltering.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5)
)
_IPAddress_Type = IpAddress
_IPAddress_Object = MibScalar
iPAddress = _IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 1),
    _IPAddress_Type()
)
iPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_GatewayIPAddress_Type = IpAddress
_GatewayIPAddress_Object = MibScalar
gatewayIPAddress = _GatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 3),
    _GatewayIPAddress_Type()
)
gatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayIPAddress.setStatus("current")


class _MaximumTransmitPower_Type(Integer32):
    """Custom type maximumTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 370),
    )


_MaximumTransmitPower_Type.__name__ = "Integer32"
_MaximumTransmitPower_Object = MibScalar
maximumTransmitPower = _MaximumTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 6),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 7),
    _AntennaGain_Type()
)
antennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antennaGain.setStatus("current")


class _RFFeederLoss_Type(Integer32):
    """Custom type rFFeederLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RFFeederLoss_Type.__name__ = "Integer32"
_RFFeederLoss_Object = MibScalar
rFFeederLoss = _RFFeederLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 8),
    _RFFeederLoss_Type()
)
rFFeederLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFFeederLoss.setStatus("current")
_RemoteIPAddress_Type = IpAddress
_RemoteIPAddress_Object = MibScalar
remoteIPAddress = _RemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 12),
    _RemoteIPAddress_Type()
)
remoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIPAddress.setStatus("current")


class _RemoteMACAddress_Type(OctetString):
    """Custom type remoteMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RemoteMACAddress_Type.__name__ = "OctetString"
_RemoteMACAddress_Object = MibScalar
remoteMACAddress = _RemoteMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 13),
    _RemoteMACAddress_Type()
)
remoteMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMACAddress.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 14),
    _EnableTransmission_Type()
)
enableTransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTransmission.setStatus("current")


class _ATPCEnable_Type(Integer32):
    """Custom type aTPCEnable based on Integer32"""
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


_ATPCEnable_Type.__name__ = "Integer32"
_ATPCEnable_Object = MibScalar
aTPCEnable = _ATPCEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 15),
    _ATPCEnable_Type()
)
aTPCEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aTPCEnable.setStatus("current")


class _IFCableLength_Type(Integer32):
    """Custom type iFCableLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19000),
    )


_IFCableLength_Type.__name__ = "Integer32"
_IFCableLength_Object = MibScalar
iFCableLength = _IFCableLength_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 16),
    _IFCableLength_Type()
)
iFCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iFCableLength.setStatus("current")


class _LinkName_Type(DisplayString):
    """Custom type linkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LinkName_Type.__name__ = "DisplayString"
_LinkName_Object = MibScalar
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 17),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 18),
    _SiteName_Type()
)
siteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteName.setStatus("current")


class _DiverseAntennaGain_Type(Integer32):
    """Custom type diverseAntennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 610),
    )


_DiverseAntennaGain_Type.__name__ = "Integer32"
_DiverseAntennaGain_Object = MibScalar
diverseAntennaGain = _DiverseAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 19),
    _DiverseAntennaGain_Type()
)
diverseAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diverseAntennaGain.setStatus("current")


class _DiverseRfFeederLoss_Type(Integer32):
    """Custom type diverseRfFeederLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DiverseRfFeederLoss_Type.__name__ = "Integer32"
_DiverseRfFeederLoss_Object = MibScalar
diverseRfFeederLoss = _DiverseRfFeederLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 5, 20),
    _DiverseRfFeederLoss_Type()
)
diverseRfFeederLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diverseRfFeederLoss.setStatus("current")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6)
)


class _DataPortCopperAutoNegotiation_Type(Integer32):
    """Custom type dataPortCopperAutoNegotiation based on Integer32"""
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


_DataPortCopperAutoNegotiation_Type.__name__ = "Integer32"
_DataPortCopperAutoNegotiation_Object = MibScalar
dataPortCopperAutoNegotiation = _DataPortCopperAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 1),
    _DataPortCopperAutoNegotiation_Type()
)
dataPortCopperAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortCopperAutoNegotiation.setStatus("current")


class _DataPortCopperAutoNegAdvertisement_Type(Bits):
    """Custom type dataPortCopperAutoNegAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("neg1000MbpsFullDuplex", 7),
          ("neg100MbpsFullDuplex", 6))
    )

_DataPortCopperAutoNegAdvertisement_Type.__name__ = "Bits"
_DataPortCopperAutoNegAdvertisement_Object = MibScalar
dataPortCopperAutoNegAdvertisement = _DataPortCopperAutoNegAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 2),
    _DataPortCopperAutoNegAdvertisement_Type()
)
dataPortCopperAutoNegAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortCopperAutoNegAdvertisement.setStatus("current")


class _DataPortStatus_Type(Integer32):
    """Custom type dataPortStatus based on Integer32"""
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
        *(("copperLinkUp", 1),
          ("down", 0),
          ("fiberLinkUp", 2),
          ("fiberYInactive", 3))
    )


_DataPortStatus_Type.__name__ = "Integer32"
_DataPortStatus_Object = MibScalar
dataPortStatus = _DataPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 4),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed1000MbpsFullDuplex", 0),
          ("speed100MbpsFullDuplex", 1),
          ("unknown", 3))
    )


_DataPortSpeedAndDuplex_Type.__name__ = "Integer32"
_DataPortSpeedAndDuplex_Object = MibScalar
dataPortSpeedAndDuplex = _DataPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 5),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 6),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 7),
    _UseVLANForManagementInterfaces_Type()
)
useVLANForManagementInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useVLANForManagementInterfaces.setStatus("current")


class _VLANManagementPriority_Type(Integer32):
    """Custom type vLANManagementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VLANManagementPriority_Type.__name__ = "Integer32"
_VLANManagementPriority_Object = MibScalar
vLANManagementPriority = _VLANManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 8),
    _VLANManagementPriority_Type()
)
vLANManagementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANManagementPriority.setStatus("current")


class _VLANManagementVIDValidation_Type(Integer32):
    """Custom type vLANManagementVIDValidation based on Integer32"""
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


_VLANManagementVIDValidation_Type.__name__ = "Integer32"
_VLANManagementVIDValidation_Object = MibScalar
vLANManagementVIDValidation = _VLANManagementVIDValidation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 9),
    _VLANManagementVIDValidation_Type()
)
vLANManagementVIDValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANManagementVIDValidation.setStatus("current")


class _VLANManagementVID_Type(Integer32):
    """Custom type vLANManagementVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VLANManagementVID_Type.__name__ = "Integer32"
_VLANManagementVID_Object = MibScalar
vLANManagementVID = _VLANManagementVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 11),
    _VLANManagementVID_Type()
)
vLANManagementVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANManagementVID.setStatus("current")


class _EthernetPriorityTableNumber_Type(Integer32):
    """Custom type ethernetPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 9),
    )


_EthernetPriorityTableNumber_Type.__name__ = "Integer32"
_EthernetPriorityTableNumber_Object = MibScalar
ethernetPriorityTableNumber = _EthernetPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 14),
    _EthernetPriorityTableNumber_Type()
)
ethernetPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPriorityTableNumber.setStatus("current")
_EthernetPriorityTable_Object = MibTable
ethernetPriorityTable = _EthernetPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 15)
)
if mibBuilder.loadTexts:
    ethernetPriorityTable.setStatus("current")
_EthernetPriorityTableEntry_Object = MibTableRow
ethernetPriorityTableEntry = _EthernetPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 15, 1)
)
ethernetPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP800-MIB", "ethernetPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    ethernetPriorityTableEntry.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 15, 1, 1),
    _EthernetPriorityQueueMapping_Type()
)
ethernetPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPriorityQueueMapping.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 15, 1, 2),
    _EthernetPriorityTableIndex_Type()
)
ethernetPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethernetPriorityTableIndex.setStatus("current")


class _ManagementPortAutoNegotiation_Type(Integer32):
    """Custom type managementPortAutoNegotiation based on Integer32"""
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


_ManagementPortAutoNegotiation_Type.__name__ = "Integer32"
_ManagementPortAutoNegotiation_Object = MibScalar
managementPortAutoNegotiation = _ManagementPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 16),
    _ManagementPortAutoNegotiation_Type()
)
managementPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementPortAutoNegotiation.setStatus("current")


class _ManagementPortAutoNegAdvertisement_Type(Bits):
    """Custom type managementPortAutoNegAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("neg100MbpsFullDuplex", 7),
          ("neg10MbpsFullDuplex", 6))
    )

_ManagementPortAutoNegAdvertisement_Type.__name__ = "Bits"
_ManagementPortAutoNegAdvertisement_Object = MibScalar
managementPortAutoNegAdvertisement = _ManagementPortAutoNegAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 17),
    _ManagementPortAutoNegAdvertisement_Type()
)
managementPortAutoNegAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementPortAutoNegAdvertisement.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 18),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100MbpsFullDuplex", 1),
          ("speed10MbpsFullDuplex", 2),
          ("unknown", 3))
    )


_ManagementPortSpeedAndDuplex_Type.__name__ = "Integer32"
_ManagementPortSpeedAndDuplex_Object = MibScalar
managementPortSpeedAndDuplex = _ManagementPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 19),
    _ManagementPortSpeedAndDuplex_Type()
)
managementPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementPortSpeedAndDuplex.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 20),
    _ManagementPortWirelessDownAlert_Type()
)
managementPortWirelessDownAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementPortWirelessDownAlert.setStatus("current")


class _ManagementMode_Type(Integer32):
    """Custom type managementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inBand", 2),
          ("outofBand", 1),
          ("outofBandLocal", 0))
    )


_ManagementMode_Type.__name__ = "Integer32"
_ManagementMode_Object = MibScalar
managementMode = _ManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 22),
    _ManagementMode_Type()
)
managementMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementMode.setStatus("current")


class _ManagementCommittedInformationRate_Type(Integer32):
    """Custom type managementCommittedInformationRate based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("kbps1000", 8),
          ("kbps1100", 9),
          ("kbps1200", 10),
          ("kbps1300", 11),
          ("kbps1400", 12),
          ("kbps1500", 13),
          ("kbps1600", 14),
          ("kbps1700", 15),
          ("kbps1800", 16),
          ("kbps1900", 17),
          ("kbps200", 0),
          ("kbps2000", 18),
          ("kbps300", 1),
          ("kbps400", 2),
          ("kbps500", 3),
          ("kbps600", 4),
          ("kbps700", 5),
          ("kbps800", 6),
          ("kbps900", 7))
    )


_ManagementCommittedInformationRate_Type.__name__ = "Integer32"
_ManagementCommittedInformationRate_Object = MibScalar
managementCommittedInformationRate = _ManagementCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 23),
    _ManagementCommittedInformationRate_Type()
)
managementCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementCommittedInformationRate.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 24),
    _DataPortPauseFrames_Type()
)
dataPortPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortPauseFrames.setStatus("current")


class _TransmitCapacityLimit_Type(Integer32):
    """Custom type transmitCapacityLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TransmitCapacityLimit_Type.__name__ = "Integer32"
_TransmitCapacityLimit_Object = MibScalar
transmitCapacityLimit = _TransmitCapacityLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 26),
    _TransmitCapacityLimit_Type()
)
transmitCapacityLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitCapacityLimit.setStatus("current")


class _TransmitCapacityLimitDetail_Type(Integer32):
    """Custom type transmitCapacityLimitDetail based on Integer32"""
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
        *(("limitedDueToAbsenceOfLicenseKey", 0),
          ("limitedDueToDevelopmentOverride", 4),
          ("restrictedDueToRemoteEthernetSpeed", 3),
          ("runningAtTheCapacityLimit", 1),
          ("runningAtUnlimitedCapacity", 2),
          ("unlimitedCapacityTrialPeriod", 6),
          ("unlimitedDueToDevelopmentOverride", 5))
    )


_TransmitCapacityLimitDetail_Type.__name__ = "Integer32"
_TransmitCapacityLimitDetail_Object = MibScalar
transmitCapacityLimitDetail = _TransmitCapacityLimitDetail_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 27),
    _TransmitCapacityLimitDetail_Type()
)
transmitCapacityLimitDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitCapacityLimitDetail.setStatus("current")


class _DataPortEthernetMediaTypeToUse_Type(Integer32):
    """Custom type dataPortEthernetMediaTypeToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("autowithFiberPreference", 0),
          ("forceCopper", 1))
    )


_DataPortEthernetMediaTypeToUse_Type.__name__ = "Integer32"
_DataPortEthernetMediaTypeToUse_Object = MibScalar
dataPortEthernetMediaTypeToUse = _DataPortEthernetMediaTypeToUse_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 28),
    _DataPortEthernetMediaTypeToUse_Type()
)
dataPortEthernetMediaTypeToUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortEthernetMediaTypeToUse.setStatus("current")


class _DataPortCopperForcedConfiguration_Type(Integer32):
    """Custom type dataPortCopperForcedConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("force100MbpsFullDuplex", 1)
    )


_DataPortCopperForcedConfiguration_Type.__name__ = "Integer32"
_DataPortCopperForcedConfiguration_Object = MibScalar
dataPortCopperForcedConfiguration = _DataPortCopperForcedConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 29),
    _DataPortCopperForcedConfiguration_Type()
)
dataPortCopperForcedConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortCopperForcedConfiguration.setStatus("current")


class _ManagementPortForcedConfiguration_Type(Integer32):
    """Custom type managementPortForcedConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("force100MbpsFullDuplex", 0),
          ("force10MbpsFullDuplex", 1))
    )


_ManagementPortForcedConfiguration_Type.__name__ = "Integer32"
_ManagementPortForcedConfiguration_Object = MibScalar
managementPortForcedConfiguration = _ManagementPortForcedConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 30),
    _ManagementPortForcedConfiguration_Type()
)
managementPortForcedConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementPortForcedConfiguration.setStatus("current")


class _L2CPPriorityTableNumber_Type(Integer32):
    """Custom type l2CPPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
    )


_L2CPPriorityTableNumber_Type.__name__ = "Integer32"
_L2CPPriorityTableNumber_Object = MibScalar
l2CPPriorityTableNumber = _L2CPPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 31),
    _L2CPPriorityTableNumber_Type()
)
l2CPPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2CPPriorityTableNumber.setStatus("current")
_L2CPPriorityTable_Object = MibTable
l2CPPriorityTable = _L2CPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 32)
)
if mibBuilder.loadTexts:
    l2CPPriorityTable.setStatus("current")
_L2CPPriorityTableEntry_Object = MibTableRow
l2CPPriorityTableEntry = _L2CPPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 32, 1)
)
l2CPPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP800-MIB", "l2CPPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    l2CPPriorityTableEntry.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 32, 1, 1),
    _L2CPPriorityQueueMapping_Type()
)
l2CPPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2CPPriorityQueueMapping.setStatus("current")


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
          ("gARPMRP", 2),
          ("rAPS", 4))
    )


_L2CPPriorityTableIndex_Type.__name__ = "Integer32"
_L2CPPriorityTableIndex_Object = MibTableColumn
l2CPPriorityTableIndex = _L2CPPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 32, 1, 2),
    _L2CPPriorityTableIndex_Type()
)
l2CPPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2CPPriorityTableIndex.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 33),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 34),
    _DSCPManagementPriority_Type()
)
dSCPManagementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSCPManagementPriority.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 35),
    _QOSPriorityScheme_Type()
)
qOSPriorityScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qOSPriorityScheme.setStatus("current")


class _IPDSCPPriorityTableNumber_Type(Integer32):
    """Custom type iPDSCPPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 64),
    )


_IPDSCPPriorityTableNumber_Type.__name__ = "Integer32"
_IPDSCPPriorityTableNumber_Object = MibScalar
iPDSCPPriorityTableNumber = _IPDSCPPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 37),
    _IPDSCPPriorityTableNumber_Type()
)
iPDSCPPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPDSCPPriorityTableNumber.setStatus("current")
_IPDSCPPriorityTable_Object = MibTable
iPDSCPPriorityTable = _IPDSCPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 38)
)
if mibBuilder.loadTexts:
    iPDSCPPriorityTable.setStatus("current")
_IPDSCPPriorityTableEntry_Object = MibTableRow
iPDSCPPriorityTableEntry = _IPDSCPPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 38, 1)
)
iPDSCPPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP800-MIB", "iPDSCPPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    iPDSCPPriorityTableEntry.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 38, 1, 1),
    _IPDSCPPriorityQueueMapping_Type()
)
iPDSCPPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPDSCPPriorityQueueMapping.setStatus("current")


class _IPDSCPPriorityTableIndex_Type(Integer32):
    """Custom type iPDSCPPriorityTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IPDSCPPriorityTableIndex_Type.__name__ = "Integer32"
_IPDSCPPriorityTableIndex_Object = MibTableColumn
iPDSCPPriorityTableIndex = _IPDSCPPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 38, 1, 2),
    _IPDSCPPriorityTableIndex_Type()
)
iPDSCPPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iPDSCPPriorityTableIndex.setStatus("current")


class _MPLSTCPriorityTableNumber_Type(Integer32):
    """Custom type mPLSTCPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8),
    )


_MPLSTCPriorityTableNumber_Type.__name__ = "Integer32"
_MPLSTCPriorityTableNumber_Object = MibScalar
mPLSTCPriorityTableNumber = _MPLSTCPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 39),
    _MPLSTCPriorityTableNumber_Type()
)
mPLSTCPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPLSTCPriorityTableNumber.setStatus("current")
_MPLSTCPriorityTable_Object = MibTable
mPLSTCPriorityTable = _MPLSTCPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 40)
)
if mibBuilder.loadTexts:
    mPLSTCPriorityTable.setStatus("current")
_MPLSTCPriorityTableEntry_Object = MibTableRow
mPLSTCPriorityTableEntry = _MPLSTCPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 40, 1)
)
mPLSTCPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP800-MIB", "mPLSTCPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    mPLSTCPriorityTableEntry.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 40, 1, 1),
    _MPLSTCPriorityQueueMapping_Type()
)
mPLSTCPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mPLSTCPriorityQueueMapping.setStatus("current")


class _MPLSTCPriorityTableIndex_Type(Integer32):
    """Custom type mPLSTCPriorityTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MPLSTCPriorityTableIndex_Type.__name__ = "Integer32"
_MPLSTCPriorityTableIndex_Object = MibTableColumn
mPLSTCPriorityTableIndex = _MPLSTCPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 6, 40, 1, 2),
    _MPLSTCPriorityTableIndex_Type()
)
mPLSTCPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mPLSTCPriorityTableIndex.setStatus("current")
_Licence_ObjectIdentity = ObjectIdentity
licence = _Licence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 8)
)


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 8, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 8, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 8, 4),
    _EthernetFiberSupport_Type()
)
ethernetFiberSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetFiberSupport.setStatus("current")


class _TransmitCapacity_Type(Integer32):
    """Custom type transmitCapacity based on Integer32"""
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
        *(("rate100Mbps", 5),
          ("rate10Mbps", 0),
          ("rate150Mbps", 6),
          ("rate200Mbps", 7),
          ("rate20Mbps", 1),
          ("rate300Mbps", 8),
          ("rate30Mbps", 2),
          ("rate40Mbps", 3),
          ("rate50Mbps", 4),
          ("rateUnlimited", 9))
    )


_TransmitCapacity_Type.__name__ = "Integer32"
_TransmitCapacity_Object = MibScalar
transmitCapacity = _TransmitCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 8, 10),
    _TransmitCapacity_Type()
)
transmitCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitCapacity.setStatus("current")


class _EncryptionAlgorithmsAvail_Type(Integer32):
    """Custom type encryptionAlgorithmsAvail based on Integer32"""
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


_EncryptionAlgorithmsAvail_Type.__name__ = "Integer32"
_EncryptionAlgorithmsAvail_Object = MibScalar
encryptionAlgorithmsAvail = _EncryptionAlgorithmsAvail_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 8, 11),
    _EncryptionAlgorithmsAvail_Type()
)
encryptionAlgorithmsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionAlgorithmsAvail.setStatus("current")


class _SecurityLevel_Type(Integer32):
    """Custom type securityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SecurityLevel_Type.__name__ = "Integer32"
_SecurityLevel_Object = MibScalar
securityLevel = _SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 8, 12),
    _SecurityLevel_Type()
)
securityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityLevel.setStatus("current")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 9)
)


class _LinkNameMismatch_Type(Integer32):
    """Custom type linkNameMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("linkNameMismatch", 1),
          ("ok", 0))
    )


_LinkNameMismatch_Type.__name__ = "Integer32"
_LinkNameMismatch_Object = MibScalar
linkNameMismatch = _LinkNameMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 3),
    _LinkNameMismatch_Type()
)
linkNameMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNameMismatch.setStatus("current")


class _AlignmentMode_Type(Integer32):
    """Custom type alignmentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aligning", 1),
          ("normal", 0))
    )


_AlignmentMode_Type.__name__ = "Integer32"
_AlignmentMode_Object = MibScalar
alignmentMode = _AlignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 4),
    _AlignmentMode_Type()
)
alignmentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alignmentMode.setStatus("current")
_TFTPServerIPAddress_Type = IpAddress
_TFTPServerIPAddress_Object = MibScalar
tFTPServerIPAddress = _TFTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 5),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 6),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 7),
    _TFTPSoftwareUpgradeFileName_Type()
)
tFTPSoftwareUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeFileName.setStatus("current")
_TFTPStartSoftwareUpgrade_Type = Integer32
_TFTPStartSoftwareUpgrade_Object = MibScalar
tFTPStartSoftwareUpgrade = _TFTPStartSoftwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 8),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 9),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 10),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 11),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 12),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 13),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 14),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 15),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 16),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 9, 17),
    _HTTPSAccessEnabled_Type()
)
hTTPSAccessEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hTTPSAccessEnabled.setStatus("current")
_PhyControl_ObjectIdentity = ObjectIdentity
phyControl = _PhyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 10)
)


class _RemoteMaximumTransmitPower_Type(Integer32):
    """Custom type remoteMaximumTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 370),
    )


_RemoteMaximumTransmitPower_Type.__name__ = "Integer32"
_RemoteMaximumTransmitPower_Object = MibScalar
remoteMaximumTransmitPower = _RemoteMaximumTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 10, 4),
    _RemoteMaximumTransmitPower_Type()
)
remoteMaximumTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMaximumTransmitPower.setStatus("current")


class _MinModulation_Type(Integer32):
    """Custom type minModulation based on Integer32"""
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
        *(("mod128QAM", 5),
          ("mod16QAM", 2),
          ("mod256QAM", 6),
          ("mod32QAM", 3),
          ("mod64QAM", 4),
          ("mod8PSK", 1),
          ("modQPSK", 0))
    )


_MinModulation_Type.__name__ = "Integer32"
_MinModulation_Object = MibScalar
minModulation = _MinModulation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 10, 6),
    _MinModulation_Type()
)
minModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minModulation.setStatus("current")


class _MinCodeRate_Type(Integer32):
    """Custom type minCodeRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MinCodeRate_Type.__name__ = "Integer32"
_MinCodeRate_Object = MibScalar
minCodeRate = _MinCodeRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 10, 7),
    _MinCodeRate_Type()
)
minCodeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minCodeRate.setStatus("current")


class _MaxModulation_Type(Integer32):
    """Custom type maxModulation based on Integer32"""
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
        *(("mod128QAM", 5),
          ("mod16QAM", 2),
          ("mod256QAM", 6),
          ("mod32QAM", 3),
          ("mod64QAM", 4),
          ("mod8PSK", 1),
          ("modQPSK", 0))
    )


_MaxModulation_Type.__name__ = "Integer32"
_MaxModulation_Object = MibScalar
maxModulation = _MaxModulation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 10, 8),
    _MaxModulation_Type()
)
maxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxModulation.setStatus("current")


class _MaxCodeRate_Type(Integer32):
    """Custom type maxCodeRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaxCodeRate_Type.__name__ = "Integer32"
_MaxCodeRate_Object = MibScalar
maxCodeRate = _MaxCodeRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 10, 9),
    _MaxCodeRate_Type()
)
maxCodeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxCodeRate.setStatus("current")
_PhyStatus_ObjectIdentity = ObjectIdentity
phyStatus = _PhyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 12)
)
_ReceivePower_Type = Integer32
_ReceivePower_Object = MibScalar
receivePower = _ReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 12, 1),
    _ReceivePower_Type()
)
receivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivePower.setStatus("current")
_VectorError_Type = Integer32
_VectorError_Object = MibScalar
vectorError = _VectorError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 12, 2),
    _VectorError_Type()
)
vectorError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vectorError.setStatus("current")
_TransmitPower_Type = Integer32
_TransmitPower_Object = MibScalar
transmitPower = _TransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 12, 3),
    _TransmitPower_Type()
)
transmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitPower.setStatus("current")


class _LinkLoss_Type(Integer32):
    """Custom type linkLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 1800),
    )


_LinkLoss_Type.__name__ = "Integer32"
_LinkLoss_Object = MibScalar
linkLoss = _LinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 12, 5),
    _LinkLoss_Type()
)
linkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLoss.setStatus("current")


class _ReceiveModulation_Type(Integer32):
    """Custom type receiveModulation based on Integer32"""
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
        *(("mod128QAM", 5),
          ("mod16QAM", 2),
          ("mod256QAM", 6),
          ("mod32QAM", 3),
          ("mod64QAM", 4),
          ("mod8PSK", 1),
          ("modQPSK", 0))
    )


_ReceiveModulation_Type.__name__ = "Integer32"
_ReceiveModulation_Object = MibScalar
receiveModulation = _ReceiveModulation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 12, 8),
    _ReceiveModulation_Type()
)
receiveModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveModulation.setStatus("current")


class _TransmitModulation_Type(Integer32):
    """Custom type transmitModulation based on Integer32"""
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
        *(("mod128QAM", 5),
          ("mod16QAM", 2),
          ("mod256QAM", 6),
          ("mod32QAM", 3),
          ("mod64QAM", 4),
          ("mod8PSK", 1),
          ("modQPSK", 0))
    )


_TransmitModulation_Type.__name__ = "Integer32"
_TransmitModulation_Object = MibScalar
transmitModulation = _TransmitModulation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 12, 9),
    _TransmitModulation_Type()
)
transmitModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitModulation.setStatus("current")
_ReceiveCodeRate_Type = Integer32
_ReceiveCodeRate_Object = MibScalar
receiveCodeRate = _ReceiveCodeRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 12, 16),
    _ReceiveCodeRate_Type()
)
receiveCodeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveCodeRate.setStatus("current")
_TransmitCodeRate_Type = Integer32
_TransmitCodeRate_Object = MibScalar
transmitCodeRate = _TransmitCodeRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 12, 17),
    _TransmitCodeRate_Type()
)
transmitCodeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitCodeRate.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 13)
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 3),
    _EncryptionEnabledMismatch_Type()
)
encryptionEnabledMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionEnabledMismatch.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 6),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 7),
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
        *(("installedFiberNotLicensed", 1),
          ("noFiberLinkEstablishedAndLOSDetected", 3),
          ("noFiberLinkEstablishedButLOSNotDetected", 2),
          ("ok", 0))
    )


_DataPortFiberStatus_Type.__name__ = "Integer32"
_DataPortFiberStatus_Object = MibScalar
dataPortFiberStatus = _DataPortFiberStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 8),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 9),
    _DataPortConfigurationMismatch_Type()
)
dataPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortConfigurationMismatch.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 12),
    _ManagementPortDisabledWarning_Type()
)
managementPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementPortDisabledWarning.setStatus("current")


class _RFUStatus_Type(Integer32):
    """Custom type rFUStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("downloadInProgress", 4),
          ("fault", 1),
          ("iFICardAttached", 7),
          ("inReset", 3),
          ("incompatibleDevice", 6),
          ("incompatibleFirmwareVersion", 5),
          ("noResponse", 8),
          ("ok", 0),
          ("powerSupplyDisabled", 10),
          ("powerSupplyFault", 9),
          ("switchingmemorybanks", 11),
          ("unknown3", 2))
    )


_RFUStatus_Type.__name__ = "Integer32"
_RFUStatus_Object = MibScalar
rFUStatus = _RFUStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 16),
    _RFUStatus_Type()
)
rFUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUStatus.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 17),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 18),
    _SecureModeAlarm_Type()
)
secureModeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureModeAlarm.setStatus("current")


class _RFUPlatformCompatibility_Type(Integer32):
    """Custom type rFUPlatformCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mismatch", 1),
          ("ok", 0))
    )


_RFUPlatformCompatibility_Type.__name__ = "Integer32"
_RFUPlatformCompatibility_Object = MibScalar
rFUPlatformCompatibility = _RFUPlatformCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 19),
    _RFUPlatformCompatibility_Type()
)
rFUPlatformCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUPlatformCompatibility.setStatus("current")


class _RFUProtectionCompatibility_Type(Integer32):
    """Custom type rFUProtectionCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mismatch", 1),
          ("ok", 0))
    )


_RFUProtectionCompatibility_Type.__name__ = "Integer32"
_RFUProtectionCompatibility_Object = MibScalar
rFUProtectionCompatibility = _RFUProtectionCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 13, 20),
    _RFUProtectionCompatibility_Type()
)
rFUProtectionCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUProtectionCompatibility.setStatus("current")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 15)
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 15, 1),
    _SMTPEmailAlert_Type()
)
sMTPEmailAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPEmailAlert.setStatus("current")
_SMTPServerIPAddress_Type = IpAddress
_SMTPServerIPAddress_Object = MibScalar
sMTPServerIPAddress = _SMTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 15, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 15, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 15, 4),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 15, 5),
    _SMTPDestinationEmailAddress_Type()
)
sMTPDestinationEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPDestinationEmailAddress.setStatus("current")


class _SMTPEnabledMessages_Type(Bits):
    """Custom type sMTPEnabledMessages based on Bits"""
    namedValues = NamedValues(
        *(("dataPortUpDown", 6),
          ("enabledDiagnosticAlarms", 4),
          ("managementPortUpDown", 5),
          ("protectionState", 3),
          ("wirelessLinkUpDown", 7))
    )

_SMTPEnabledMessages_Type.__name__ = "Bits"
_SMTPEnabledMessages_Object = MibScalar
sMTPEnabledMessages = _SMTPEnabledMessages_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 15, 6),
    _SMTPEnabledMessages_Type()
)
sMTPEnabledMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPEnabledMessages.setStatus("current")
_SnmpControl_ObjectIdentity = ObjectIdentity
snmpControl = _SnmpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 16)
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 2),
    _SNMPCommunityString_Type()
)
sNMPCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPCommunityString.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 5),
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
          ("dataPortUpDown", 5),
          ("enabledDiagnosticAlarms", 3),
          ("managementPortUpDown", 4),
          ("protectionState", 1),
          ("wirelessLinkUpDown", 6))
    )

_SNMPEnabledTraps_Type.__name__ = "Bits"
_SNMPEnabledTraps_Object = MibScalar
sNMPEnabledTraps = _SNMPEnabledTraps_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 6),
    _SNMPEnabledTraps_Type()
)
sNMPEnabledTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPEnabledTraps.setStatus("current")


class _EnabledDiagnosticAlarms_Type(Bits):
    """Custom type enabledDiagnosticAlarms based on Bits"""
    namedValues = NamedValues(
        *(("alignmentMode", 7),
          ("dataPortConfigurationMismatch", 0),
          ("dataPortDisabledWarning", 15),
          ("dataPortFiberStatus", 14),
          ("dataPortStatus", 10),
          ("encryptionEnabledMismatch", 4),
          ("linkNameMismatch", 6),
          ("managementPortConfigurationMismatch", 13),
          ("managementPortDisabledWarning", 12),
          ("managementPortStatus", 9),
          ("rFUPowerButtonPressed", 20),
          ("rFUStatus", 11),
          ("sNTPSync", 3),
          ("secureMode", 21),
          ("syslogClientDisabledWarning", 19),
          ("syslogDisabledWarning", 8),
          ("syslogLocalNearlyFull", 23),
          ("syslogLocalWrapped", 22),
          ("unitOutOfCalibration", 5),
          ("wirelessLinkDisabledWarning", 1),
          ("wirelessLinkStatus", 2))
    )

_EnabledDiagnosticAlarms_Type.__name__ = "Bits"
_EnabledDiagnosticAlarms_Object = MibScalar
enabledDiagnosticAlarms = _EnabledDiagnosticAlarms_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 7),
    _EnabledDiagnosticAlarms_Type()
)
enabledDiagnosticAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enabledDiagnosticAlarms.setStatus("current")


class _EnabledDiagnosticProtectionAlarms_Type(Bits):
    """Custom type enabledDiagnosticProtectionAlarms based on Bits"""
    namedValues = NamedValues(
        *(("dataPortEthernetSpeedStatus", 3),
          ("endWirelessReceiveSignalStatus", 0),
          ("licensedTransmitCapacityStatus", 4),
          ("managementPortEthernetSpeedStatus", 2),
          ("protectionAvailabilityStatus", 7),
          ("protectionConfigurationStatus", 6),
          ("protectionInterfaceStatus", 1),
          ("rxDiversityAvailabilityStatus", 13),
          ("rxDiversityConfigurationStatus", 14),
          ("rxDiversityDataPortStatus", 15),
          ("wirelessReceiveSignalStatus", 5))
    )

_EnabledDiagnosticProtectionAlarms_Type.__name__ = "Bits"
_EnabledDiagnosticProtectionAlarms_Object = MibScalar
enabledDiagnosticProtectionAlarms = _EnabledDiagnosticProtectionAlarms_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 8),
    _EnabledDiagnosticProtectionAlarms_Type()
)
enabledDiagnosticProtectionAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enabledDiagnosticProtectionAlarms.setStatus("current")


class _SNMPTrapTableNumber_Type(Integer32):
    """Custom type sNMPTrapTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_SNMPTrapTableNumber_Type.__name__ = "Integer32"
_SNMPTrapTableNumber_Object = MibScalar
sNMPTrapTableNumber = _SNMPTrapTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 9),
    _SNMPTrapTableNumber_Type()
)
sNMPTrapTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapTableNumber.setStatus("current")
_SNMPTrapTable_Object = MibTable
sNMPTrapTable = _SNMPTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 10)
)
if mibBuilder.loadTexts:
    sNMPTrapTable.setStatus("current")
_SNMPTrapTableEntry_Object = MibTableRow
sNMPTrapTableEntry = _SNMPTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 10, 1)
)
sNMPTrapTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP800-MIB", "sNMPTrapTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 10, 1, 1),
    _SNMPTrapTableIndex_Type()
)
sNMPTrapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sNMPTrapTableIndex.setStatus("current")
_SNMPTrapIPAddress_Type = IpAddress
_SNMPTrapIPAddress_Object = MibTableColumn
sNMPTrapIPAddress = _SNMPTrapIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 10, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 16, 10, 1, 3),
    _SNMPTrapPortNumber_Type()
)
sNMPTrapPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapPortNumber.setStatus("current")
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 17)
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 4),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 5),
    _SNTPSync_Type()
)
sNTPSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPSync.setStatus("current")
_SNTPLastSync_Type = Integer32
_SNTPLastSync_Object = MibScalar
sNTPLastSync = _SNTPLastSync_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 6),
    _SNTPLastSync_Type()
)
sNTPLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPLastSync.setStatus("current")
_SystemClock_Type = Integer32
_SystemClock_Object = MibScalar
systemClock = _SystemClock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 7),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 8),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 9),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 10),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 11),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 12),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 13),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 14),
    _SNTPServerTableNumber_Type()
)
sNTPServerTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerTableNumber.setStatus("current")
_SNTPServerTable_Object = MibTable
sNTPServerTable = _SNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 15)
)
if mibBuilder.loadTexts:
    sNTPServerTable.setStatus("current")
_SNTPServerTableEntry_Object = MibTableRow
sNTPServerTableEntry = _SNTPServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 15, 1)
)
sNTPServerTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP800-MIB", "sNTPServerTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 15, 1, 1),
    _SNTPServerTableIndex_Type()
)
sNTPServerTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sNTPServerTableIndex.setStatus("current")
_SNTPServerIPAddress_Type = IpAddress
_SNTPServerIPAddress_Object = MibTableColumn
sNTPServerIPAddress = _SNTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 15, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 15, 1, 3),
    _SNTPServerPortNumber_Type()
)
sNTPServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerPortNumber.setStatus("current")


class _SNTPServerResponse_Type(DisplayString):
    """Custom type sNTPServerResponse based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SNTPServerResponse_Type.__name__ = "DisplayString"
_SNTPServerResponse_Object = MibTableColumn
sNTPServerResponse = _SNTPServerResponse_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 17, 15, 1, 4),
    _SNTPServerResponse_Type()
)
sNTPServerResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerResponse.setStatus("current")
_Reset_ObjectIdentity = ObjectIdentity
reset = _Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 18)
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 18, 1),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("current")
_Versions_ObjectIdentity = ObjectIdentity
versions = _Versions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 19)
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 19, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 19, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 19, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 19, 4),
    _BootVersion_Type()
)
bootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersion.setStatus("current")
_PubStats_ObjectIdentity = ObjectIdentity
pubStats = _PubStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 20)
)
_ReceiveDataRate_Type = Integer32
_ReceiveDataRate_Object = MibScalar
receiveDataRate = _ReceiveDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 20, 1),
    _ReceiveDataRate_Type()
)
receiveDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveDataRate.setStatus("current")
_TransmitDataRate_Type = Integer32
_TransmitDataRate_Object = MibScalar
transmitDataRate = _TransmitDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 20, 2),
    _TransmitDataRate_Type()
)
transmitDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitDataRate.setStatus("current")
_AggregateDataRate_Type = Integer32
_AggregateDataRate_Object = MibScalar
aggregateDataRate = _AggregateDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 20, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 20, 4),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 20, 5),
    _WirelessLinkStatus_Type()
)
wirelessLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatus.setStatus("current")
_ByteErrorRatio_Type = Counter64
_ByteErrorRatio_Object = MibScalar
byteErrorRatio = _ByteErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 20, 6),
    _ByteErrorRatio_Type()
)
byteErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    byteErrorRatio.setStatus("current")
_CodeWordErrorRatio_Type = Counter64
_CodeWordErrorRatio_Object = MibScalar
codeWordErrorRatio = _CodeWordErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 20, 8),
    _CodeWordErrorRatio_Type()
)
codeWordErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codeWordErrorRatio.setStatus("current")
_Encryption_ObjectIdentity = ObjectIdentity
encryption = _Encryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 22)
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 22, 1),
    _EncryptionAlgorithm_Type()
)
encryptionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionAlgorithm.setStatus("current")
_Rfu_ObjectIdentity = ObjectIdentity
rfu = _Rfu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23)
)


class _RFURfBand_Type(Integer32):
    """Custom type rFURfBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6000, 38000),
    )


_RFURfBand_Type.__name__ = "Integer32"
_RFURfBand_Object = MibScalar
rFURfBand = _RFURfBand_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 1),
    _RFURfBand_Type()
)
rFURfBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFURfBand.setStatus("current")


class _RFUTxBandAboveRx_Type(Integer32):
    """Custom type rFUTxBandAboveRx based on Integer32"""
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


_RFUTxBandAboveRx_Type.__name__ = "Integer32"
_RFUTxBandAboveRx_Object = MibScalar
rFUTxBandAboveRx = _RFUTxBandAboveRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 2),
    _RFUTxBandAboveRx_Type()
)
rFUTxBandAboveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUTxBandAboveRx.setStatus("current")


class _RFUFreqSpacing_Type(Integer32):
    """Custom type rFUFreqSpacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1560000),
    )


_RFUFreqSpacing_Type.__name__ = "Integer32"
_RFUFreqSpacing_Object = MibScalar
rFUFreqSpacing = _RFUFreqSpacing_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 3),
    _RFUFreqSpacing_Type()
)
rFUFreqSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUFreqSpacing.setStatus("current")


class _RFUTxPowerMin_Type(Integer32):
    """Custom type rFUTxPowerMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_RFUTxPowerMin_Type.__name__ = "Integer32"
_RFUTxPowerMin_Object = MibScalar
rFUTxPowerMin = _RFUTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 4),
    _RFUTxPowerMin_Type()
)
rFUTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUTxPowerMin.setStatus("current")


class _RFUTxPowerMax_Type(Integer32):
    """Custom type rFUTxPowerMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 370),
    )


_RFUTxPowerMax_Type.__name__ = "Integer32"
_RFUTxPowerMax_Object = MibScalar
rFUTxPowerMax = _RFUTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 5),
    _RFUTxPowerMax_Type()
)
rFUTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUTxPowerMax.setStatus("current")


class _RFURxFreqMin_Type(Integer32):
    """Custom type rFURxFreqMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5725000, 41000000),
    )


_RFURxFreqMin_Type.__name__ = "Integer32"
_RFURxFreqMin_Object = MibScalar
rFURxFreqMin = _RFURxFreqMin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 6),
    _RFURxFreqMin_Type()
)
rFURxFreqMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFURxFreqMin.setStatus("current")


class _RFURxFreqMax_Type(Integer32):
    """Custom type rFURxFreqMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5725000, 41000000),
    )


_RFURxFreqMax_Type.__name__ = "Integer32"
_RFURxFreqMax_Object = MibScalar
rFURxFreqMax = _RFURxFreqMax_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 7),
    _RFURxFreqMax_Type()
)
rFURxFreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFURxFreqMax.setStatus("current")


class _RFUTxFreqMin_Type(Integer32):
    """Custom type rFUTxFreqMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5725000, 41000000),
    )


_RFUTxFreqMin_Type.__name__ = "Integer32"
_RFUTxFreqMin_Object = MibScalar
rFUTxFreqMin = _RFUTxFreqMin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 8),
    _RFUTxFreqMin_Type()
)
rFUTxFreqMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUTxFreqMin.setStatus("current")


class _RFUTxFreqMax_Type(Integer32):
    """Custom type rFUTxFreqMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5725000, 41000000),
    )


_RFUTxFreqMax_Type.__name__ = "Integer32"
_RFUTxFreqMax_Object = MibScalar
rFUTxFreqMax = _RFUTxFreqMax_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 9),
    _RFUTxFreqMax_Type()
)
rFUTxFreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUTxFreqMax.setStatus("current")


class _RFUSerial_Type(DisplayString):
    """Custom type rFUSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_RFUSerial_Type.__name__ = "DisplayString"
_RFUSerial_Object = MibScalar
rFUSerial = _RFUSerial_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 10),
    _RFUSerial_Type()
)
rFUSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUSerial.setStatus("current")


class _RFUActiveFirmwareBank_Type(Integer32):
    """Custom type rFUActiveFirmwareBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RFUActiveFirmwareBank_Type.__name__ = "Integer32"
_RFUActiveFirmwareBank_Object = MibScalar
rFUActiveFirmwareBank = _RFUActiveFirmwareBank_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 11),
    _RFUActiveFirmwareBank_Type()
)
rFUActiveFirmwareBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUActiveFirmwareBank.setStatus("current")


class _RFUVersionBank1_Type(DisplayString):
    """Custom type rFUVersionBank1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_RFUVersionBank1_Type.__name__ = "DisplayString"
_RFUVersionBank1_Object = MibScalar
rFUVersionBank1 = _RFUVersionBank1_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 12),
    _RFUVersionBank1_Type()
)
rFUVersionBank1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUVersionBank1.setStatus("current")


class _RFUVersionBank2_Type(DisplayString):
    """Custom type rFUVersionBank2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_RFUVersionBank2_Type.__name__ = "DisplayString"
_RFUVersionBank2_Object = MibScalar
rFUVersionBank2 = _RFUVersionBank2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 13),
    _RFUVersionBank2_Type()
)
rFUVersionBank2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUVersionBank2.setStatus("current")


class _RFUType_Type(DisplayString):
    """Custom type rFUType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_RFUType_Type.__name__ = "DisplayString"
_RFUType_Object = MibScalar
rFUType = _RFUType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 14),
    _RFUType_Type()
)
rFUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUType.setStatus("current")


class _RFURxRFSynthLockAlarm_Type(Integer32):
    """Custom type rFURxRFSynthLockAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("outOfLock", 1))
    )


_RFURxRFSynthLockAlarm_Type.__name__ = "Integer32"
_RFURxRFSynthLockAlarm_Object = MibScalar
rFURxRFSynthLockAlarm = _RFURxRFSynthLockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 15),
    _RFURxRFSynthLockAlarm_Type()
)
rFURxRFSynthLockAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFURxRFSynthLockAlarm.setStatus("current")


class _RFUTxRFSynthLockAlarm_Type(Integer32):
    """Custom type rFUTxRFSynthLockAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("outOfLock", 1))
    )


_RFUTxRFSynthLockAlarm_Type.__name__ = "Integer32"
_RFUTxRFSynthLockAlarm_Object = MibScalar
rFUTxRFSynthLockAlarm = _RFUTxRFSynthLockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 16),
    _RFUTxRFSynthLockAlarm_Type()
)
rFUTxRFSynthLockAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUTxRFSynthLockAlarm.setStatus("current")


class _RFUTxPowerAlarm_Type(Integer32):
    """Custom type rFUTxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("txOutputFailed", 1))
    )


_RFUTxPowerAlarm_Type.__name__ = "Integer32"
_RFUTxPowerAlarm_Object = MibScalar
rFUTxPowerAlarm = _RFUTxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 17),
    _RFUTxPowerAlarm_Type()
)
rFUTxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUTxPowerAlarm.setStatus("current")


class _RFUCommonIFSynthLockAlarm_Type(Integer32):
    """Custom type rFUCommonIFSynthLockAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("outOfLock", 1))
    )


_RFUCommonIFSynthLockAlarm_Type.__name__ = "Integer32"
_RFUCommonIFSynthLockAlarm_Object = MibScalar
rFUCommonIFSynthLockAlarm = _RFUCommonIFSynthLockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 18),
    _RFUCommonIFSynthLockAlarm_Type()
)
rFUCommonIFSynthLockAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUCommonIFSynthLockAlarm.setStatus("current")


class _RFUPowerAlarm_Type(Integer32):
    """Custom type rFUPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("powerFailed", 1))
    )


_RFUPowerAlarm_Type.__name__ = "Integer32"
_RFUPowerAlarm_Object = MibScalar
rFUPowerAlarm = _RFUPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 19),
    _RFUPowerAlarm_Type()
)
rFUPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUPowerAlarm.setStatus("current")


class _RFULockoutAlarm_Type(Integer32):
    """Custom type rFULockoutAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lockedOut", 1),
          ("ok", 0))
    )


_RFULockoutAlarm_Type.__name__ = "Integer32"
_RFULockoutAlarm_Object = MibScalar
rFULockoutAlarm = _RFULockoutAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 20),
    _RFULockoutAlarm_Type()
)
rFULockoutAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFULockoutAlarm.setStatus("current")


class _RFUCableAlarm_Type(Integer32):
    """Custom type rFUCableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("iFCableVoltageOutOfRange", 1),
          ("ok", 0))
    )


_RFUCableAlarm_Type.__name__ = "Integer32"
_RFUCableAlarm_Object = MibScalar
rFUCableAlarm = _RFUCableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 21),
    _RFUCableAlarm_Type()
)
rFUCableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUCableAlarm.setStatus("current")


class _RFUCableAttenuationAdjustAlarm_Type(Integer32):
    """Custom type rFUCableAttenuationAdjustAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("iFCableAttenuatorAdjusting", 1),
          ("ok", 0))
    )


_RFUCableAttenuationAdjustAlarm_Type.__name__ = "Integer32"
_RFUCableAttenuationAdjustAlarm_Object = MibScalar
rFUCableAttenuationAdjustAlarm = _RFUCableAttenuationAdjustAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 22),
    _RFUCableAttenuationAdjustAlarm_Type()
)
rFUCableAttenuationAdjustAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUCableAttenuationAdjustAlarm.setStatus("current")


class _RFUTxPowerDegradedAlarm_Type(Integer32):
    """Custom type rFUTxPowerDegradedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 1),
          ("ok", 0))
    )


_RFUTxPowerDegradedAlarm_Type.__name__ = "Integer32"
_RFUTxPowerDegradedAlarm_Object = MibScalar
rFUTxPowerDegradedAlarm = _RFUTxPowerDegradedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 23),
    _RFUTxPowerDegradedAlarm_Type()
)
rFUTxPowerDegradedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUTxPowerDegradedAlarm.setStatus("current")


class _RFURpsAlarm_Type(Integer32):
    """Custom type rFURpsAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("rPSAlarmActive", 1))
    )


_RFURpsAlarm_Type.__name__ = "Integer32"
_RFURpsAlarm_Object = MibScalar
rFURpsAlarm = _RFURpsAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 24),
    _RFURpsAlarm_Type()
)
rFURpsAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFURpsAlarm.setStatus("current")


class _RFUTxMuteStatus_Type(Integer32):
    """Custom type rFUTxMuteStatus based on Integer32"""
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
        *(("mutedByUser", 1),
          ("mutedDueToConfigurationError", 2),
          ("mutedDueToInactive", 6),
          ("mutedDueToRFUConfiguring", 4),
          ("mutedDueToRFUFault", 3),
          ("mutedDueToRFUIncompatiblewithCMU", 5),
          ("transmitting", 0))
    )


_RFUTxMuteStatus_Type.__name__ = "Integer32"
_RFUTxMuteStatus_Object = MibScalar
rFUTxMuteStatus = _RFUTxMuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 25),
    _RFUTxMuteStatus_Type()
)
rFUTxMuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUTxMuteStatus.setStatus("current")


class _RFUFanAssemblyAlarm_Type(Integer32):
    """Custom type rFUFanAssemblyAlarm based on Integer32"""
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
          ("partialFanFailure", 1),
          ("totalFanFailure", 2))
    )


_RFUFanAssemblyAlarm_Type.__name__ = "Integer32"
_RFUFanAssemblyAlarm_Object = MibScalar
rFUFanAssemblyAlarm = _RFUFanAssemblyAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 26),
    _RFUFanAssemblyAlarm_Type()
)
rFUFanAssemblyAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUFanAssemblyAlarm.setStatus("current")


class _RFUHighTemperatureAlarm_Type(Integer32):
    """Custom type rFUHighTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highTemperature", 1),
          ("ok", 0),
          ("veryHighTemperature", 2))
    )


_RFUHighTemperatureAlarm_Type.__name__ = "Integer32"
_RFUHighTemperatureAlarm_Object = MibScalar
rFUHighTemperatureAlarm = _RFUHighTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 27),
    _RFUHighTemperatureAlarm_Type()
)
rFUHighTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUHighTemperatureAlarm.setStatus("current")


class _RFURFSwitchAlarm_Type(Integer32):
    """Custom type rFURFSwitchAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("ok", 0))
    )


_RFURFSwitchAlarm_Type.__name__ = "Integer32"
_RFURFSwitchAlarm_Object = MibScalar
rFURFSwitchAlarm = _RFURFSwitchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 28),
    _RFURFSwitchAlarm_Type()
)
rFURFSwitchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFURFSwitchAlarm.setStatus("current")


class _RFURxIFSynthLockAlarm_Type(Integer32):
    """Custom type rFURxIFSynthLockAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("outOfLock", 1))
    )


_RFURxIFSynthLockAlarm_Type.__name__ = "Integer32"
_RFURxIFSynthLockAlarm_Object = MibScalar
rFURxIFSynthLockAlarm = _RFURxIFSynthLockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 29),
    _RFURxIFSynthLockAlarm_Type()
)
rFURxIFSynthLockAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFURxIFSynthLockAlarm.setStatus("current")


class _RFUTxIFSynthLockAlarm_Type(Integer32):
    """Custom type rFUTxIFSynthLockAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("outOfLock", 1))
    )


_RFUTxIFSynthLockAlarm_Type.__name__ = "Integer32"
_RFUTxIFSynthLockAlarm_Object = MibScalar
rFUTxIFSynthLockAlarm = _RFUTxIFSynthLockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 30),
    _RFUTxIFSynthLockAlarm_Type()
)
rFUTxIFSynthLockAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUTxIFSynthLockAlarm.setStatus("current")


class _RFUPowerButtonPressed_Type(Integer32):
    """Custom type rFUPowerButtonPressed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("iRFUPowerButtonwaspressed", 1),
          ("ok", 0))
    )


_RFUPowerButtonPressed_Type.__name__ = "Integer32"
_RFUPowerButtonPressed_Object = MibScalar
rFUPowerButtonPressed = _RFUPowerButtonPressed_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 31),
    _RFUPowerButtonPressed_Type()
)
rFUPowerButtonPressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUPowerButtonPressed.setStatus("current")


class _RFUConnectedPlatform_Type(Integer32):
    """Custom type rFUConnectedPlatform based on Integer32"""
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
        *(("iRFUHP", 3),
          ("oDUA", 1),
          ("oDUB", 2),
          ("unknown", 0))
    )


_RFUConnectedPlatform_Type.__name__ = "Integer32"
_RFUConnectedPlatform_Object = MibScalar
rFUConnectedPlatform = _RFUConnectedPlatform_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 32),
    _RFUConnectedPlatform_Type()
)
rFUConnectedPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUConnectedPlatform.setStatus("current")


class _RFUCommonRFSynthLockAlarm_Type(Integer32):
    """Custom type rFUCommonRFSynthLockAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("outOfLock", 1))
    )


_RFUCommonRFSynthLockAlarm_Type.__name__ = "Integer32"
_RFUCommonRFSynthLockAlarm_Object = MibScalar
rFUCommonRFSynthLockAlarm = _RFUCommonRFSynthLockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 33),
    _RFUCommonRFSynthLockAlarm_Type()
)
rFUCommonRFSynthLockAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUCommonRFSynthLockAlarm.setStatus("current")


class _RFUBranchingConfiguration_Type(Integer32):
    """Custom type rFUBranchingConfiguration based on Integer32"""
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
        *(("rFU1plus0", 0),
          ("rFU1plus0MHSBReadyEqual", 1),
          ("rFU1plus0MHSBReadyUnequal", 2),
          ("rFU1plus1MHSBEqual", 3),
          ("rFU1plus1MHSBUnequal", 4),
          ("rFU1plus1TxMHSBRxSD", 5),
          ("rFU2plus0", 6))
    )


_RFUBranchingConfiguration_Type.__name__ = "Integer32"
_RFUBranchingConfiguration_Object = MibScalar
rFUBranchingConfiguration = _RFUBranchingConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 34),
    _RFUBranchingConfiguration_Type()
)
rFUBranchingConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rFUBranchingConfiguration.setStatus("current")


class _RFUTransceiverLocation_Type(Integer32):
    """Custom type rFUTransceiverLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("leftTRxA", 0),
          ("rightTRxB", 1))
    )


_RFUTransceiverLocation_Type.__name__ = "Integer32"
_RFUTransceiverLocation_Object = MibScalar
rFUTransceiverLocation = _RFUTransceiverLocation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 35),
    _RFUTransceiverLocation_Type()
)
rFUTransceiverLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rFUTransceiverLocation.setStatus("current")


class _RFURfSwitchCableAlarm_Type(Integer32):
    """Custom type rFURfSwitchCableAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("ok", 0))
    )


_RFURfSwitchCableAlarm_Type.__name__ = "Integer32"
_RFURfSwitchCableAlarm_Object = MibScalar
rFURfSwitchCableAlarm = _RFURfSwitchCableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 36),
    _RFURfSwitchCableAlarm_Type()
)
rFURfSwitchCableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFURfSwitchCableAlarm.setStatus("current")
_RFUReceiveBranchingUnitLoss_Type = Integer32
_RFUReceiveBranchingUnitLoss_Object = MibScalar
rFUReceiveBranchingUnitLoss = _RFUReceiveBranchingUnitLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 37),
    _RFUReceiveBranchingUnitLoss_Type()
)
rFUReceiveBranchingUnitLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUReceiveBranchingUnitLoss.setStatus("current")
_RFUTransmitBranchingUnitLoss_Type = Integer32
_RFUTransmitBranchingUnitLoss_Object = MibScalar
rFUTransmitBranchingUnitLoss = _RFUTransmitBranchingUnitLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 23, 38),
    _RFUTransmitBranchingUnitLoss_Type()
)
rFUTransmitBranchingUnitLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFUTransmitBranchingUnitLoss.setStatus("current")
_RadioLicense_ObjectIdentity = ObjectIdentity
radioLicense = _RadioLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24)
)


class _RadioLicenseIdentifier_Type(DisplayString):
    """Custom type radioLicenseIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RadioLicenseIdentifier_Type.__name__ = "DisplayString"
_RadioLicenseIdentifier_Object = MibScalar
radioLicenseIdentifier = _RadioLicenseIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 1),
    _RadioLicenseIdentifier_Type()
)
radioLicenseIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseIdentifier.setStatus("current")


class _RadioLicenseBand_Type(Integer32):
    """Custom type radioLicenseBand based on Integer32"""
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
        *(("band11GHz", 3),
          ("band13GHz", 4),
          ("band15GHz", 5),
          ("band18GHz", 6),
          ("band23GHz", 7),
          ("band26GHz", 8),
          ("band28GHz", 12),
          ("band32GHz", 9),
          ("band38GHz", 10),
          ("band7GHz", 1),
          ("band8GHz", 2),
          ("bandLower6GHz", 0),
          ("bandUpper6GHz", 11))
    )


_RadioLicenseBand_Type.__name__ = "Integer32"
_RadioLicenseBand_Object = MibScalar
radioLicenseBand = _RadioLicenseBand_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 2),
    _RadioLicenseBand_Type()
)
radioLicenseBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseBand.setStatus("current")


class _RadioLicenseRegion_Type(Integer32):
    """Custom type radioLicenseRegion based on Integer32"""
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
        *(("brazil", 3),
          ("canada", 2),
          ("eTSI", 0),
          ("fCC", 1),
          ("nTIA", 4))
    )


_RadioLicenseRegion_Type.__name__ = "Integer32"
_RadioLicenseRegion_Object = MibScalar
radioLicenseRegion = _RadioLicenseRegion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 3),
    _RadioLicenseRegion_Type()
)
radioLicenseRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseRegion.setStatus("current")


class _RadioLicenseTxFreq_Type(Integer32):
    """Custom type radioLicenseTxFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5925000, 40105000),
    )


_RadioLicenseTxFreq_Type.__name__ = "Integer32"
_RadioLicenseTxFreq_Object = MibScalar
radioLicenseTxFreq = _RadioLicenseTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 4),
    _RadioLicenseTxFreq_Type()
)
radioLicenseTxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseTxFreq.setStatus("current")


class _RadioLicenseRxFreq_Type(Integer32):
    """Custom type radioLicenseRxFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5925000, 40105000),
    )


_RadioLicenseRxFreq_Type.__name__ = "Integer32"
_RadioLicenseRxFreq_Object = MibScalar
radioLicenseRxFreq = _RadioLicenseRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 5),
    _RadioLicenseRxFreq_Type()
)
radioLicenseRxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseRxFreq.setStatus("current")


class _RadioLicenseBandwidth_Type(Integer32):
    """Custom type radioLicenseBandwidth based on Integer32"""
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
        *(("bw10MHz", 1),
          ("bw1375MHz", 2),
          ("bw14MHz", 3),
          ("bw20MHz", 4),
          ("bw25MHz", 13),
          ("bw275MHz", 5),
          ("bw28MHz", 6),
          ("bw30MHz", 7),
          ("bw40MHz", 8),
          ("bw50MHz", 9),
          ("bw55MHz", 10),
          ("bw56MHz", 11),
          ("bw7MHz", 0),
          ("bw80MHz", 12))
    )


_RadioLicenseBandwidth_Type.__name__ = "Integer32"
_RadioLicenseBandwidth_Object = MibScalar
radioLicenseBandwidth = _RadioLicenseBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 6),
    _RadioLicenseBandwidth_Type()
)
radioLicenseBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseBandwidth.setStatus("current")


class _RadioLicenseMaxEIRP_Type(Integer32):
    """Custom type radioLicenseMaxEIRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 1000),
    )


_RadioLicenseMaxEIRP_Type.__name__ = "Integer32"
_RadioLicenseMaxEIRP_Object = MibScalar
radioLicenseMaxEIRP = _RadioLicenseMaxEIRP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 7),
    _RadioLicenseMaxEIRP_Type()
)
radioLicenseMaxEIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseMaxEIRP.setStatus("current")


class _RadioLicenseModulation_Type(Integer32):
    """Custom type radioLicenseModulation based on Integer32"""
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
        *(("mod128QAM", 5),
          ("mod16QAM", 2),
          ("mod256QAM", 6),
          ("mod32QAM", 3),
          ("mod64QAM", 4),
          ("mod8PSK", 1),
          ("modQPSK", 0))
    )


_RadioLicenseModulation_Type.__name__ = "Integer32"
_RadioLicenseModulation_Object = MibScalar
radioLicenseModulation = _RadioLicenseModulation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 8),
    _RadioLicenseModulation_Type()
)
radioLicenseModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseModulation.setStatus("current")


class _RadioLicenseCodeRate_Type(Integer32):
    """Custom type radioLicenseCodeRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RadioLicenseCodeRate_Type.__name__ = "Integer32"
_RadioLicenseCodeRate_Object = MibScalar
radioLicenseCodeRate = _RadioLicenseCodeRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 9),
    _RadioLicenseCodeRate_Type()
)
radioLicenseCodeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseCodeRate.setStatus("current")


class _RadioLicenseIncompatibleAlarm_Type(Integer32):
    """Custom type radioLicenseIncompatibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("radioLicenseIncompatiblewithRFU", 1))
    )


_RadioLicenseIncompatibleAlarm_Type.__name__ = "Integer32"
_RadioLicenseIncompatibleAlarm_Object = MibScalar
radioLicenseIncompatibleAlarm = _RadioLicenseIncompatibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 10),
    _RadioLicenseIncompatibleAlarm_Type()
)
radioLicenseIncompatibleAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseIncompatibleAlarm.setStatus("current")


class _RadioLicenseMinModulation_Type(Integer32):
    """Custom type radioLicenseMinModulation based on Integer32"""
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
        *(("mod128QAM", 5),
          ("mod16QAM", 2),
          ("mod256QAM", 6),
          ("mod32QAM", 3),
          ("mod64QAM", 4),
          ("mod8PSK", 1),
          ("modQPSK", 0))
    )


_RadioLicenseMinModulation_Type.__name__ = "Integer32"
_RadioLicenseMinModulation_Object = MibScalar
radioLicenseMinModulation = _RadioLicenseMinModulation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 11),
    _RadioLicenseMinModulation_Type()
)
radioLicenseMinModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseMinModulation.setStatus("current")


class _RadioLicenseMinCodeRate_Type(Integer32):
    """Custom type radioLicenseMinCodeRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RadioLicenseMinCodeRate_Type.__name__ = "Integer32"
_RadioLicenseMinCodeRate_Object = MibScalar
radioLicenseMinCodeRate = _RadioLicenseMinCodeRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 12),
    _RadioLicenseMinCodeRate_Type()
)
radioLicenseMinCodeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseMinCodeRate.setStatus("current")


class _RadioLicenseMaxModulation_Type(Integer32):
    """Custom type radioLicenseMaxModulation based on Integer32"""
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
        *(("mod128QAM", 5),
          ("mod16QAM", 2),
          ("mod256QAM", 6),
          ("mod32QAM", 3),
          ("mod64QAM", 4),
          ("mod8PSK", 1),
          ("modQPSK", 0))
    )


_RadioLicenseMaxModulation_Type.__name__ = "Integer32"
_RadioLicenseMaxModulation_Object = MibScalar
radioLicenseMaxModulation = _RadioLicenseMaxModulation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 13),
    _RadioLicenseMaxModulation_Type()
)
radioLicenseMaxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseMaxModulation.setStatus("current")


class _RadioLicenseMaxCodeRate_Type(Integer32):
    """Custom type radioLicenseMaxCodeRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RadioLicenseMaxCodeRate_Type.__name__ = "Integer32"
_RadioLicenseMaxCodeRate_Object = MibScalar
radioLicenseMaxCodeRate = _RadioLicenseMaxCodeRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 24, 14),
    _RadioLicenseMaxCodeRate_Type()
)
radioLicenseMaxCodeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLicenseMaxCodeRate.setStatus("current")
_ProtectionConfig_ObjectIdentity = ObjectIdentity
protectionConfig = _ProtectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25)
)


class _Protection_Type(Integer32):
    """Custom type protection based on Integer32"""
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
          ("hotStandby1plus1", 1),
          ("hotStandby1plus1withRxDiversity", 2))
    )


_Protection_Type.__name__ = "Integer32"
_Protection_Object = MibScalar
protection = _Protection_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 1),
    _Protection_Type()
)
protection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protection.setStatus("current")


class _FaultProtectionSwitching_Type(Integer32):
    """Custom type faultProtectionSwitching based on Integer32"""
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


_FaultProtectionSwitching_Type.__name__ = "Integer32"
_FaultProtectionSwitching_Object = MibScalar
faultProtectionSwitching = _FaultProtectionSwitching_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 2),
    _FaultProtectionSwitching_Type()
)
faultProtectionSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultProtectionSwitching.setStatus("current")


class _PrimarySecondaryMode_Type(Integer32):
    """Custom type primarySecondaryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_PrimarySecondaryMode_Type.__name__ = "Integer32"
_PrimarySecondaryMode_Object = MibScalar
primarySecondaryMode = _PrimarySecondaryMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 3),
    _PrimarySecondaryMode_Type()
)
primarySecondaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primarySecondaryMode.setStatus("current")


class _NumberOfAntennas_Type(Integer32):
    """Custom type numberOfAntennas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("one", 0),
          ("two", 1))
    )


_NumberOfAntennas_Type.__name__ = "Integer32"
_NumberOfAntennas_Object = MibScalar
numberOfAntennas = _NumberOfAntennas_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 4),
    _NumberOfAntennas_Type()
)
numberOfAntennas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfAntennas.setStatus("current")


class _PrimaryRecovery_Type(Integer32):
    """Custom type primaryRecovery based on Integer32"""
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


_PrimaryRecovery_Type.__name__ = "Integer32"
_PrimaryRecovery_Object = MibScalar
primaryRecovery = _PrimaryRecovery_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 5),
    _PrimaryRecovery_Type()
)
primaryRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRecovery.setStatus("current")


class _PrimaryRecoveryPeriod_Type(Integer32):
    """Custom type primaryRecoveryPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2880),
    )


_PrimaryRecoveryPeriod_Type.__name__ = "Integer32"
_PrimaryRecoveryPeriod_Object = MibScalar
primaryRecoveryPeriod = _PrimaryRecoveryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 6),
    _PrimaryRecoveryPeriod_Type()
)
primaryRecoveryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryRecoveryPeriod.setStatus("current")


class _RequestedProtectionState_Type(Integer32):
    """Custom type requestedProtectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_RequestedProtectionState_Type.__name__ = "Integer32"
_RequestedProtectionState_Object = MibScalar
requestedProtectionState = _RequestedProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 7),
    _RequestedProtectionState_Type()
)
requestedProtectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    requestedProtectionState.setStatus("current")


class _AntennaReceiveLevelDeltaThreshold_Type(Integer32):
    """Custom type antennaReceiveLevelDeltaThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AntennaReceiveLevelDeltaThreshold_Type.__name__ = "Integer32"
_AntennaReceiveLevelDeltaThreshold_Object = MibScalar
antennaReceiveLevelDeltaThreshold = _AntennaReceiveLevelDeltaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 8),
    _AntennaReceiveLevelDeltaThreshold_Type()
)
antennaReceiveLevelDeltaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antennaReceiveLevelDeltaThreshold.setStatus("current")


class _AntennaReceiveLevelMeasurementWindow_Type(Integer32):
    """Custom type antennaReceiveLevelMeasurementWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2880),
    )


_AntennaReceiveLevelMeasurementWindow_Type.__name__ = "Integer32"
_AntennaReceiveLevelMeasurementWindow_Object = MibScalar
antennaReceiveLevelMeasurementWindow = _AntennaReceiveLevelMeasurementWindow_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 9),
    _AntennaReceiveLevelMeasurementWindow_Type()
)
antennaReceiveLevelMeasurementWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antennaReceiveLevelMeasurementWindow.setStatus("current")


class _FiberY_Type(Integer32):
    """Custom type fiberY based on Integer32"""
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


_FiberY_Type.__name__ = "Integer32"
_FiberY_Object = MibScalar
fiberY = _FiberY_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 12),
    _FiberY_Type()
)
fiberY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberY.setStatus("current")


class _RxDiversityVlanTpid_Type(Integer32):
    """Custom type rxDiversityVlanTpid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("iEEE8021QTaggedCTagType8100", 0),
          ("iEEE8021adTaggedSTagorBTagType88a8", 1))
    )


_RxDiversityVlanTpid_Type.__name__ = "Integer32"
_RxDiversityVlanTpid_Object = MibScalar
rxDiversityVlanTpid = _RxDiversityVlanTpid_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 14),
    _RxDiversityVlanTpid_Type()
)
rxDiversityVlanTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxDiversityVlanTpid.setStatus("current")


class _RxDiversityVid_Type(Integer32):
    """Custom type rxDiversityVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RxDiversityVid_Type.__name__ = "Integer32"
_RxDiversityVid_Object = MibScalar
rxDiversityVid = _RxDiversityVid_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 25, 15),
    _RxDiversityVid_Type()
)
rxDiversityVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxDiversityVid.setStatus("current")
_ProtectionStatus_ObjectIdentity = ObjectIdentity
protectionStatus = _ProtectionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26)
)


class _ProtectionAvailabilityStatus_Type(Integer32):
    """Custom type protectionAvailabilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notProtected", 1),
          ("notProtecting", 2),
          ("ok", 0))
    )


_ProtectionAvailabilityStatus_Type.__name__ = "Integer32"
_ProtectionAvailabilityStatus_Object = MibScalar
protectionAvailabilityStatus = _ProtectionAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 2),
    _ProtectionAvailabilityStatus_Type()
)
protectionAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectionAvailabilityStatus.setStatus("current")


class _ProtectionConfigurationStatus_Type(Integer32):
    """Custom type protectionConfigurationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("configurationNotProtecting", 1),
          ("ok", 0))
    )


_ProtectionConfigurationStatus_Type.__name__ = "Integer32"
_ProtectionConfigurationStatus_Object = MibScalar
protectionConfigurationStatus = _ProtectionConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 3),
    _ProtectionConfigurationStatus_Type()
)
protectionConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectionConfigurationStatus.setStatus("current")


class _ProtectionState_Type(Integer32):
    """Custom type protectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_ProtectionState_Type.__name__ = "Integer32"
_ProtectionState_Object = MibScalar
protectionState = _ProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 4),
    _ProtectionState_Type()
)
protectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectionState.setStatus("current")


class _ActiveUnit_Type(Integer32):
    """Custom type activeUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_ActiveUnit_Type.__name__ = "Integer32"
_ActiveUnit_Object = MibScalar
activeUnit = _ActiveUnit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 5),
    _ActiveUnit_Type()
)
activeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeUnit.setStatus("current")


class _ProtectionSwitchCause_Type(Integer32):
    """Custom type protectionSwitchCause based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("byteErrorRatioOverThreshold", 12),
          ("byteErrorRatioOverThresholdatRemoteEnd", 17),
          ("cMURebooting", 14),
          ("codeWordErrorRatioOverThreshold", 13),
          ("codeWordErrorRatioOverThresholdatRemoteEnd", 18),
          ("configurationNotProtecting", 15),
          ("dataPortDown", 9),
          ("managedProtectionSwitch", 21),
          ("managementPortDown", 10),
          ("multipleReceiveFailureatRemoteEnd", 19),
          ("neighborCMUConnectedButNotResponding", 1),
          ("noPreviousProtectionSwitch", 0),
          ("primaryRecovery", 20),
          ("rFUCableAttenuatorAdjustmentFailure", 7),
          ("rFUCableFailure", 6),
          ("rFUCommonIFSynthOutofLock", 24),
          ("rFUCommonRFSynthOutofLock", 5),
          ("rFUNotResponding", 2),
          ("rFURxIFSynthOutofLock", 22),
          ("rFURxRFSynthOutofLock", 3),
          ("rFUTxIFSynthOutofLock", 23),
          ("rFUTxPowerDegraded", 8),
          ("rFUTxRFSynthOutofLock", 4),
          ("rFUVeryHighTemperature", 25),
          ("wirelessReceiveSignalNotDetected", 11),
          ("wirelessReceiveSignalNotDetectedatRemoteEnd", 16))
    )


_ProtectionSwitchCause_Type.__name__ = "Integer32"
_ProtectionSwitchCause_Object = MibScalar
protectionSwitchCause = _ProtectionSwitchCause_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 6),
    _ProtectionSwitchCause_Type()
)
protectionSwitchCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectionSwitchCause.setStatus("current")


class _EndId_Type(DisplayString):
    """Custom type endId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EndId_Type.__name__ = "DisplayString"
_EndId_Object = MibScalar
endId = _EndId_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 7),
    _EndId_Type()
)
endId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endId.setStatus("current")
_NeighborIPAddress_Type = IpAddress
_NeighborIPAddress_Object = MibScalar
neighborIPAddress = _NeighborIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 8),
    _NeighborIPAddress_Type()
)
neighborIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborIPAddress.setStatus("current")


class _NeighborMACAddress_Type(OctetString):
    """Custom type neighborMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NeighborMACAddress_Type.__name__ = "OctetString"
_NeighborMACAddress_Object = MibScalar
neighborMACAddress = _NeighborMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 9),
    _NeighborMACAddress_Type()
)
neighborMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborMACAddress.setStatus("current")


class _WirelessReceiveSignalStatus_Type(Integer32):
    """Custom type wirelessReceiveSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notDetected", 1),
          ("ok", 0))
    )


_WirelessReceiveSignalStatus_Type.__name__ = "Integer32"
_WirelessReceiveSignalStatus_Object = MibScalar
wirelessReceiveSignalStatus = _WirelessReceiveSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 10),
    _WirelessReceiveSignalStatus_Type()
)
wirelessReceiveSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessReceiveSignalStatus.setStatus("current")


class _LicensedTransmitCapacityStatus_Type(Integer32):
    """Custom type licensedTransmitCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lessThanNeighbor", 1),
          ("ok", 0))
    )


_LicensedTransmitCapacityStatus_Type.__name__ = "Integer32"
_LicensedTransmitCapacityStatus_Object = MibScalar
licensedTransmitCapacityStatus = _LicensedTransmitCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 14),
    _LicensedTransmitCapacityStatus_Type()
)
licensedTransmitCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licensedTransmitCapacityStatus.setStatus("current")


class _DataPortEthernetSpeedStatus_Type(Integer32):
    """Custom type dataPortEthernetSpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lessThanNeighbor", 1),
          ("ok", 0))
    )


_DataPortEthernetSpeedStatus_Type.__name__ = "Integer32"
_DataPortEthernetSpeedStatus_Object = MibScalar
dataPortEthernetSpeedStatus = _DataPortEthernetSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 15),
    _DataPortEthernetSpeedStatus_Type()
)
dataPortEthernetSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortEthernetSpeedStatus.setStatus("current")


class _ManagementPortEthernetSpeedStatus_Type(Integer32):
    """Custom type managementPortEthernetSpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lessThanNeighbor", 1),
          ("ok", 0))
    )


_ManagementPortEthernetSpeedStatus_Type.__name__ = "Integer32"
_ManagementPortEthernetSpeedStatus_Object = MibScalar
managementPortEthernetSpeedStatus = _ManagementPortEthernetSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 16),
    _ManagementPortEthernetSpeedStatus_Type()
)
managementPortEthernetSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementPortEthernetSpeedStatus.setStatus("current")


class _ProtectionInterfaceStatus_Type(Integer32):
    """Custom type protectionInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("neighborNotConnected", 2),
          ("neighborNotResponding", 1),
          ("ok", 0))
    )


_ProtectionInterfaceStatus_Type.__name__ = "Integer32"
_ProtectionInterfaceStatus_Object = MibScalar
protectionInterfaceStatus = _ProtectionInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 17),
    _ProtectionInterfaceStatus_Type()
)
protectionInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectionInterfaceStatus.setStatus("current")
_RemotePrimaryIPAddress_Type = IpAddress
_RemotePrimaryIPAddress_Object = MibScalar
remotePrimaryIPAddress = _RemotePrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 18),
    _RemotePrimaryIPAddress_Type()
)
remotePrimaryIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePrimaryIPAddress.setStatus("current")
_RemoteSecondaryIPAddress_Type = IpAddress
_RemoteSecondaryIPAddress_Object = MibScalar
remoteSecondaryIPAddress = _RemoteSecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 19),
    _RemoteSecondaryIPAddress_Type()
)
remoteSecondaryIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSecondaryIPAddress.setStatus("current")


class _RemotePrimaryMACAddress_Type(OctetString):
    """Custom type remotePrimaryMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RemotePrimaryMACAddress_Type.__name__ = "OctetString"
_RemotePrimaryMACAddress_Object = MibScalar
remotePrimaryMACAddress = _RemotePrimaryMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 20),
    _RemotePrimaryMACAddress_Type()
)
remotePrimaryMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePrimaryMACAddress.setStatus("current")


class _RemoteSecondaryMACAddress_Type(OctetString):
    """Custom type remoteSecondaryMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RemoteSecondaryMACAddress_Type.__name__ = "OctetString"
_RemoteSecondaryMACAddress_Object = MibScalar
remoteSecondaryMACAddress = _RemoteSecondaryMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 21),
    _RemoteSecondaryMACAddress_Type()
)
remoteSecondaryMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteSecondaryMACAddress.setStatus("current")


class _RemotePrimarySecondaryMode_Type(Integer32):
    """Custom type remotePrimarySecondaryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_RemotePrimarySecondaryMode_Type.__name__ = "Integer32"
_RemotePrimarySecondaryMode_Object = MibScalar
remotePrimarySecondaryMode = _RemotePrimarySecondaryMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 22),
    _RemotePrimarySecondaryMode_Type()
)
remotePrimarySecondaryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePrimarySecondaryMode.setStatus("current")


class _TransmitterStatus_Type(Integer32):
    """Custom type transmitterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 2),
          ("muted", 0),
          ("transmitting", 1))
    )


_TransmitterStatus_Type.__name__ = "Integer32"
_TransmitterStatus_Object = MibScalar
transmitterStatus = _TransmitterStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 23),
    _TransmitterStatus_Type()
)
transmitterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitterStatus.setStatus("current")


class _EndWirelessReceiveSignalStatus_Type(Integer32):
    """Custom type endWirelessReceiveSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notDetected", 1),
          ("ok", 0))
    )


_EndWirelessReceiveSignalStatus_Type.__name__ = "Integer32"
_EndWirelessReceiveSignalStatus_Object = MibScalar
endWirelessReceiveSignalStatus = _EndWirelessReceiveSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 26),
    _EndWirelessReceiveSignalStatus_Type()
)
endWirelessReceiveSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endWirelessReceiveSignalStatus.setStatus("current")


class _RxDiversityDataPortStatus_Type(Integer32):
    """Custom type rxDiversityDataPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notProtecting", 1),
          ("ok", 0))
    )


_RxDiversityDataPortStatus_Type.__name__ = "Integer32"
_RxDiversityDataPortStatus_Object = MibScalar
rxDiversityDataPortStatus = _RxDiversityDataPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 27),
    _RxDiversityDataPortStatus_Type()
)
rxDiversityDataPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDiversityDataPortStatus.setStatus("current")


class _RxDiversityAvailabilityStatus_Type(Integer32):
    """Custom type rxDiversityAvailabilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notProtected", 1),
          ("notProtecting", 2),
          ("ok", 0))
    )


_RxDiversityAvailabilityStatus_Type.__name__ = "Integer32"
_RxDiversityAvailabilityStatus_Object = MibScalar
rxDiversityAvailabilityStatus = _RxDiversityAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 28),
    _RxDiversityAvailabilityStatus_Type()
)
rxDiversityAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDiversityAvailabilityStatus.setStatus("current")


class _RxDiversityConfigurationStatus_Type(Integer32):
    """Custom type rxDiversityConfigurationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("configurationNotProtecting", 1),
          ("ok", 0))
    )


_RxDiversityConfigurationStatus_Type.__name__ = "Integer32"
_RxDiversityConfigurationStatus_Object = MibScalar
rxDiversityConfigurationStatus = _RxDiversityConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 29),
    _RxDiversityConfigurationStatus_Type()
)
rxDiversityConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDiversityConfigurationStatus.setStatus("current")


class _RxDiversityNeighborCompatibility_Type(Integer32):
    """Custom type rxDiversityNeighborCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mismatch", 1),
          ("ok", 0))
    )


_RxDiversityNeighborCompatibility_Type.__name__ = "Integer32"
_RxDiversityNeighborCompatibility_Object = MibScalar
rxDiversityNeighborCompatibility = _RxDiversityNeighborCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 30),
    _RxDiversityNeighborCompatibility_Type()
)
rxDiversityNeighborCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDiversityNeighborCompatibility.setStatus("current")


class _RxDiversityVlanTpidNeighborCompatibility_Type(Integer32):
    """Custom type rxDiversityVlanTpidNeighborCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mismatch", 1),
          ("ok", 0))
    )


_RxDiversityVlanTpidNeighborCompatibility_Type.__name__ = "Integer32"
_RxDiversityVlanTpidNeighborCompatibility_Object = MibScalar
rxDiversityVlanTpidNeighborCompatibility = _RxDiversityVlanTpidNeighborCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 31),
    _RxDiversityVlanTpidNeighborCompatibility_Type()
)
rxDiversityVlanTpidNeighborCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDiversityVlanTpidNeighborCompatibility.setStatus("current")


class _RxDiversityVidNeighborCompatibility_Type(Integer32):
    """Custom type rxDiversityVidNeighborCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mismatch", 1),
          ("ok", 0))
    )


_RxDiversityVidNeighborCompatibility_Type.__name__ = "Integer32"
_RxDiversityVidNeighborCompatibility_Object = MibScalar
rxDiversityVidNeighborCompatibility = _RxDiversityVidNeighborCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 26, 32),
    _RxDiversityVidNeighborCompatibility_Type()
)
rxDiversityVidNeighborCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDiversityVidNeighborCompatibility.setStatus("current")
_ProtectionStats_ObjectIdentity = ObjectIdentity
protectionStats = _ProtectionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 27)
)
_ActiveCodeWordCount_Type = Counter64
_ActiveCodeWordCount_Object = MibScalar
activeCodeWordCount = _ActiveCodeWordCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 27, 1),
    _ActiveCodeWordCount_Type()
)
activeCodeWordCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeCodeWordCount.setStatus("current")
_ActiveCodeWordErrorCount_Type = Counter64
_ActiveCodeWordErrorCount_Object = MibScalar
activeCodeWordErrorCount = _ActiveCodeWordErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 27, 2),
    _ActiveCodeWordErrorCount_Type()
)
activeCodeWordErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeCodeWordErrorCount.setStatus("current")
_ActiveByteCount_Type = Counter64
_ActiveByteCount_Object = MibScalar
activeByteCount = _ActiveByteCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 27, 3),
    _ActiveByteCount_Type()
)
activeByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeByteCount.setStatus("current")
_ActiveByteErrorCount_Type = Counter64
_ActiveByteErrorCount_Object = MibScalar
activeByteErrorCount = _ActiveByteErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 27, 4),
    _ActiveByteErrorCount_Type()
)
activeByteErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeByteErrorCount.setStatus("current")
_ActiveAvailableTime_Type = Integer32
_ActiveAvailableTime_Object = MibScalar
activeAvailableTime = _ActiveAvailableTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 27, 5),
    _ActiveAvailableTime_Type()
)
activeAvailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAvailableTime.setStatus("current")
_ActiveCounterMeasurementPeriod_Type = Integer32
_ActiveCounterMeasurementPeriod_Object = MibScalar
activeCounterMeasurementPeriod = _ActiveCounterMeasurementPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 27, 6),
    _ActiveCounterMeasurementPeriod_Type()
)
activeCounterMeasurementPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeCounterMeasurementPeriod.setStatus("current")


class _ActiveWirelessLinkAvailability_Type(Integer32):
    """Custom type activeWirelessLinkAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ActiveWirelessLinkAvailability_Type.__name__ = "Integer32"
_ActiveWirelessLinkAvailability_Object = MibScalar
activeWirelessLinkAvailability = _ActiveWirelessLinkAvailability_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 27, 7),
    _ActiveWirelessLinkAvailability_Type()
)
activeWirelessLinkAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeWirelessLinkAvailability.setStatus("current")
_ActiveCodeWordErrorRatio_Type = Counter64
_ActiveCodeWordErrorRatio_Object = MibScalar
activeCodeWordErrorRatio = _ActiveCodeWordErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 27, 8),
    _ActiveCodeWordErrorRatio_Type()
)
activeCodeWordErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeCodeWordErrorRatio.setStatus("current")
_ActiveByteErrorRatio_Type = Counter64
_ActiveByteErrorRatio_Object = MibScalar
activeByteErrorRatio = _ActiveByteErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 27, 9),
    _ActiveByteErrorRatio_Type()
)
activeByteErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeByteErrorRatio.setStatus("current")
_SyslogControl_ObjectIdentity = ObjectIdentity
syslogControl = _SyslogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 28)
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 28, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 28, 2),
    _SyslogState_Type()
)
syslogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogState.setStatus("current")
_Supplementary_ObjectIdentity = ObjectIdentity
supplementary = _Supplementary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 96)
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 96, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 8, 96, 2),
    _Latitude_Type()
)
latitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latitude.setStatus("current")
_Altitude_Type = Integer32
_Altitude_Object = MibScalar
altitude = _Altitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 8, 96, 3),
    _Altitude_Type()
)
altitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altitude.setStatus("current")
_PtpGroups_ObjectIdentity = ObjectIdentity
ptpGroups = _PtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98)
)
_PtpTraps_ObjectIdentity = ObjectIdentity
ptpTraps = _PtpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99)
)
_PtpTrapPrefix_ObjectIdentity = ObjectIdentity
ptpTrapPrefix = _PtpTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0)
)

# Managed Objects groups

bridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 4)
)
bridgeGroup.setObjects(
    ("CAMBIUM-PTP800-MIB", "localPacketFiltering")
)
if mibBuilder.loadTexts:
    bridgeGroup.setStatus("current")

configurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 5)
)
configurationGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "iPAddress"),
        ("CAMBIUM-PTP800-MIB", "subnetMask"),
        ("CAMBIUM-PTP800-MIB", "gatewayIPAddress"),
        ("CAMBIUM-PTP800-MIB", "maximumTransmitPower"),
        ("CAMBIUM-PTP800-MIB", "antennaGain"),
        ("CAMBIUM-PTP800-MIB", "rFFeederLoss"),
        ("CAMBIUM-PTP800-MIB", "remoteIPAddress"),
        ("CAMBIUM-PTP800-MIB", "remoteMACAddress"),
        ("CAMBIUM-PTP800-MIB", "enableTransmission"),
        ("CAMBIUM-PTP800-MIB", "aTPCEnable"),
        ("CAMBIUM-PTP800-MIB", "iFCableLength"),
        ("CAMBIUM-PTP800-MIB", "linkName"),
        ("CAMBIUM-PTP800-MIB", "siteName"),
        ("CAMBIUM-PTP800-MIB", "diverseAntennaGain"),
        ("CAMBIUM-PTP800-MIB", "diverseRfFeederLoss"))
)
if mibBuilder.loadTexts:
    configurationGroup.setStatus("current")

ethernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 6)
)
ethernetGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "dataPortCopperAutoNegotiation"),
        ("CAMBIUM-PTP800-MIB", "dataPortCopperAutoNegAdvertisement"),
        ("CAMBIUM-PTP800-MIB", "dataPortStatus"),
        ("CAMBIUM-PTP800-MIB", "dataPortSpeedAndDuplex"),
        ("CAMBIUM-PTP800-MIB", "dataPortWirelessDownAlert"),
        ("CAMBIUM-PTP800-MIB", "useVLANForManagementInterfaces"),
        ("CAMBIUM-PTP800-MIB", "vLANManagementPriority"),
        ("CAMBIUM-PTP800-MIB", "vLANManagementVIDValidation"),
        ("CAMBIUM-PTP800-MIB", "vLANManagementVID"),
        ("CAMBIUM-PTP800-MIB", "ethernetPriorityTableNumber"),
        ("CAMBIUM-PTP800-MIB", "managementPortAutoNegotiation"),
        ("CAMBIUM-PTP800-MIB", "managementPortAutoNegAdvertisement"),
        ("CAMBIUM-PTP800-MIB", "managementPortStatus"),
        ("CAMBIUM-PTP800-MIB", "managementPortSpeedAndDuplex"),
        ("CAMBIUM-PTP800-MIB", "managementPortWirelessDownAlert"),
        ("CAMBIUM-PTP800-MIB", "managementMode"),
        ("CAMBIUM-PTP800-MIB", "managementCommittedInformationRate"),
        ("CAMBIUM-PTP800-MIB", "dataPortPauseFrames"),
        ("CAMBIUM-PTP800-MIB", "transmitCapacityLimit"),
        ("CAMBIUM-PTP800-MIB", "transmitCapacityLimitDetail"),
        ("CAMBIUM-PTP800-MIB", "dataPortEthernetMediaTypeToUse"),
        ("CAMBIUM-PTP800-MIB", "dataPortCopperForcedConfiguration"),
        ("CAMBIUM-PTP800-MIB", "managementPortForcedConfiguration"),
        ("CAMBIUM-PTP800-MIB", "l2CPPriorityTableNumber"),
        ("CAMBIUM-PTP800-MIB", "unknownNetworkPriorityQueueMapping"),
        ("CAMBIUM-PTP800-MIB", "dSCPManagementPriority"),
        ("CAMBIUM-PTP800-MIB", "qOSPriorityScheme"),
        ("CAMBIUM-PTP800-MIB", "iPDSCPPriorityTableNumber"),
        ("CAMBIUM-PTP800-MIB", "mPLSTCPriorityTableNumber"),
        ("CAMBIUM-PTP800-MIB", "ethernetPriorityQueueMapping"),
        ("CAMBIUM-PTP800-MIB", "l2CPPriorityQueueMapping"),
        ("CAMBIUM-PTP800-MIB", "iPDSCPPriorityQueueMapping"),
        ("CAMBIUM-PTP800-MIB", "mPLSTCPriorityQueueMapping"))
)
if mibBuilder.loadTexts:
    ethernetGroup.setStatus("current")

licenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 8)
)
licenceGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "productVariant"),
        ("CAMBIUM-PTP800-MIB", "productName"),
        ("CAMBIUM-PTP800-MIB", "ethernetFiberSupport"),
        ("CAMBIUM-PTP800-MIB", "transmitCapacity"),
        ("CAMBIUM-PTP800-MIB", "encryptionAlgorithmsAvail"),
        ("CAMBIUM-PTP800-MIB", "securityLevel"))
)
if mibBuilder.loadTexts:
    licenceGroup.setStatus("current")

managementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 9)
)
managementGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "linkNameMismatch"),
        ("CAMBIUM-PTP800-MIB", "alignmentMode"),
        ("CAMBIUM-PTP800-MIB", "tFTPServerIPAddress"),
        ("CAMBIUM-PTP800-MIB", "tFTPServerPortNumber"),
        ("CAMBIUM-PTP800-MIB", "tFTPSoftwareUpgradeFileName"),
        ("CAMBIUM-PTP800-MIB", "tFTPStartSoftwareUpgrade"),
        ("CAMBIUM-PTP800-MIB", "tFTPSoftwareUpgradeStatus"),
        ("CAMBIUM-PTP800-MIB", "tFTPSoftwareUpgradeStatusText"),
        ("CAMBIUM-PTP800-MIB", "tFTPSoftwareUpgradeStatusAdditionalText"),
        ("CAMBIUM-PTP800-MIB", "hTTPAccessEnabled"),
        ("CAMBIUM-PTP800-MIB", "telnetAccessEnabled"),
        ("CAMBIUM-PTP800-MIB", "hTTPPortNumber"),
        ("CAMBIUM-PTP800-MIB", "hTTPSPortNumber"),
        ("CAMBIUM-PTP800-MIB", "telnetPortNumber"),
        ("CAMBIUM-PTP800-MIB", "hTTPSAccessEnabled"))
)
if mibBuilder.loadTexts:
    managementGroup.setStatus("current")

phyControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 10)
)
phyControlGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "remoteMaximumTransmitPower"),
        ("CAMBIUM-PTP800-MIB", "minModulation"),
        ("CAMBIUM-PTP800-MIB", "minCodeRate"),
        ("CAMBIUM-PTP800-MIB", "maxModulation"),
        ("CAMBIUM-PTP800-MIB", "maxCodeRate"))
)
if mibBuilder.loadTexts:
    phyControlGroup.setStatus("current")

phyStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 12)
)
phyStatusGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "receivePower"),
        ("CAMBIUM-PTP800-MIB", "vectorError"),
        ("CAMBIUM-PTP800-MIB", "transmitPower"),
        ("CAMBIUM-PTP800-MIB", "linkLoss"),
        ("CAMBIUM-PTP800-MIB", "receiveModulation"),
        ("CAMBIUM-PTP800-MIB", "transmitModulation"),
        ("CAMBIUM-PTP800-MIB", "receiveCodeRate"),
        ("CAMBIUM-PTP800-MIB", "transmitCodeRate"))
)
if mibBuilder.loadTexts:
    phyStatusGroup.setStatus("current")

alarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 13)
)
alarmsGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "unitOutOfCalibration"),
        ("CAMBIUM-PTP800-MIB", "encryptionEnabledMismatch"),
        ("CAMBIUM-PTP800-MIB", "wirelessLinkDisabledWarning"),
        ("CAMBIUM-PTP800-MIB", "dataPortDisabledWarning"),
        ("CAMBIUM-PTP800-MIB", "dataPortFiberStatus"),
        ("CAMBIUM-PTP800-MIB", "dataPortConfigurationMismatch"),
        ("CAMBIUM-PTP800-MIB", "managementPortDisabledWarning"),
        ("CAMBIUM-PTP800-MIB", "rFUStatus"),
        ("CAMBIUM-PTP800-MIB", "managementPortConfigurationMismatch"),
        ("CAMBIUM-PTP800-MIB", "secureModeAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUPlatformCompatibility"),
        ("CAMBIUM-PTP800-MIB", "rFUProtectionCompatibility"))
)
if mibBuilder.loadTexts:
    alarmsGroup.setStatus("current")

smtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 15)
)
smtpGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "sMTPEmailAlert"),
        ("CAMBIUM-PTP800-MIB", "sMTPServerIPAddress"),
        ("CAMBIUM-PTP800-MIB", "sMTPServerPortNumber"),
        ("CAMBIUM-PTP800-MIB", "sMTPSourceEmailAddress"),
        ("CAMBIUM-PTP800-MIB", "sMTPDestinationEmailAddress"),
        ("CAMBIUM-PTP800-MIB", "sMTPEnabledMessages"))
)
if mibBuilder.loadTexts:
    smtpGroup.setStatus("current")

snmpControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 16)
)
snmpControlGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "sNMPPortNumber"),
        ("CAMBIUM-PTP800-MIB", "sNMPCommunityString"),
        ("CAMBIUM-PTP800-MIB", "sNMPTrapVersion"),
        ("CAMBIUM-PTP800-MIB", "sNMPEnabledTraps"),
        ("CAMBIUM-PTP800-MIB", "enabledDiagnosticAlarms"),
        ("CAMBIUM-PTP800-MIB", "enabledDiagnosticProtectionAlarms"),
        ("CAMBIUM-PTP800-MIB", "sNMPTrapTableNumber"),
        ("CAMBIUM-PTP800-MIB", "sNMPTrapIPAddress"),
        ("CAMBIUM-PTP800-MIB", "sNMPTrapPortNumber"))
)
if mibBuilder.loadTexts:
    snmpControlGroup.setStatus("current")

sntpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 17)
)
sntpGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "sNTPState"),
        ("CAMBIUM-PTP800-MIB", "sNTPPollInterval"),
        ("CAMBIUM-PTP800-MIB", "sNTPSync"),
        ("CAMBIUM-PTP800-MIB", "sNTPLastSync"),
        ("CAMBIUM-PTP800-MIB", "systemClock"),
        ("CAMBIUM-PTP800-MIB", "timeZone"),
        ("CAMBIUM-PTP800-MIB", "daylightSaving"),
        ("CAMBIUM-PTP800-MIB", "sNTPPrimaryServer"),
        ("CAMBIUM-PTP800-MIB", "sNTPPrimaryServerDeadTime"),
        ("CAMBIUM-PTP800-MIB", "sNTPServerRetries"),
        ("CAMBIUM-PTP800-MIB", "sNTPServerTimeout"),
        ("CAMBIUM-PTP800-MIB", "sNTPServerTableNumber"),
        ("CAMBIUM-PTP800-MIB", "sNTPServerIPAddress"),
        ("CAMBIUM-PTP800-MIB", "sNTPServerPortNumber"),
        ("CAMBIUM-PTP800-MIB", "sNTPServerResponse"))
)
if mibBuilder.loadTexts:
    sntpGroup.setStatus("current")

resetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 18)
)
resetGroup.setObjects(
    ("CAMBIUM-PTP800-MIB", "systemReset")
)
if mibBuilder.loadTexts:
    resetGroup.setStatus("current")

versionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 19)
)
versionsGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "softwareVersion"),
        ("CAMBIUM-PTP800-MIB", "hardwareVersion"),
        ("CAMBIUM-PTP800-MIB", "secondarySoftwareVersion"),
        ("CAMBIUM-PTP800-MIB", "bootVersion"))
)
if mibBuilder.loadTexts:
    versionsGroup.setStatus("current")

pubStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 20)
)
pubStatsGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "receiveDataRate"),
        ("CAMBIUM-PTP800-MIB", "transmitDataRate"),
        ("CAMBIUM-PTP800-MIB", "aggregateDataRate"),
        ("CAMBIUM-PTP800-MIB", "wirelessLinkAvailability"),
        ("CAMBIUM-PTP800-MIB", "wirelessLinkStatus"),
        ("CAMBIUM-PTP800-MIB", "byteErrorRatio"),
        ("CAMBIUM-PTP800-MIB", "codeWordErrorRatio"))
)
if mibBuilder.loadTexts:
    pubStatsGroup.setStatus("current")

encryptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 22)
)
encryptionGroup.setObjects(
    ("CAMBIUM-PTP800-MIB", "encryptionAlgorithm")
)
if mibBuilder.loadTexts:
    encryptionGroup.setStatus("current")

rfuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 23)
)
rfuGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "rFURfBand"),
        ("CAMBIUM-PTP800-MIB", "rFUTxBandAboveRx"),
        ("CAMBIUM-PTP800-MIB", "rFUFreqSpacing"),
        ("CAMBIUM-PTP800-MIB", "rFUTxPowerMin"),
        ("CAMBIUM-PTP800-MIB", "rFUTxPowerMax"),
        ("CAMBIUM-PTP800-MIB", "rFURxFreqMin"),
        ("CAMBIUM-PTP800-MIB", "rFURxFreqMax"),
        ("CAMBIUM-PTP800-MIB", "rFUTxFreqMin"),
        ("CAMBIUM-PTP800-MIB", "rFUTxFreqMax"),
        ("CAMBIUM-PTP800-MIB", "rFUSerial"),
        ("CAMBIUM-PTP800-MIB", "rFUActiveFirmwareBank"),
        ("CAMBIUM-PTP800-MIB", "rFUVersionBank1"),
        ("CAMBIUM-PTP800-MIB", "rFUVersionBank2"),
        ("CAMBIUM-PTP800-MIB", "rFUType"),
        ("CAMBIUM-PTP800-MIB", "rFURxRFSynthLockAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUTxRFSynthLockAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUTxPowerAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUCommonIFSynthLockAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUPowerAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFULockoutAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUCableAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUCableAttenuationAdjustAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUTxPowerDegradedAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFURpsAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUTxMuteStatus"),
        ("CAMBIUM-PTP800-MIB", "rFUFanAssemblyAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUHighTemperatureAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFURFSwitchAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFURxIFSynthLockAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUTxIFSynthLockAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUPowerButtonPressed"),
        ("CAMBIUM-PTP800-MIB", "rFUConnectedPlatform"),
        ("CAMBIUM-PTP800-MIB", "rFUCommonRFSynthLockAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUBranchingConfiguration"),
        ("CAMBIUM-PTP800-MIB", "rFUTransceiverLocation"),
        ("CAMBIUM-PTP800-MIB", "rFURfSwitchCableAlarm"),
        ("CAMBIUM-PTP800-MIB", "rFUReceiveBranchingUnitLoss"),
        ("CAMBIUM-PTP800-MIB", "rFUTransmitBranchingUnitLoss"))
)
if mibBuilder.loadTexts:
    rfuGroup.setStatus("current")

radioLicenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 24)
)
radioLicenseGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "radioLicenseIdentifier"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseBand"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseRegion"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseTxFreq"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseRxFreq"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseBandwidth"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseMaxEIRP"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseModulation"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseCodeRate"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseIncompatibleAlarm"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseMinModulation"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseMinCodeRate"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseMaxModulation"),
        ("CAMBIUM-PTP800-MIB", "radioLicenseMaxCodeRate"))
)
if mibBuilder.loadTexts:
    radioLicenseGroup.setStatus("current")

protectionConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 25)
)
protectionConfigGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "protection"),
        ("CAMBIUM-PTP800-MIB", "faultProtectionSwitching"),
        ("CAMBIUM-PTP800-MIB", "primarySecondaryMode"),
        ("CAMBIUM-PTP800-MIB", "numberOfAntennas"),
        ("CAMBIUM-PTP800-MIB", "primaryRecovery"),
        ("CAMBIUM-PTP800-MIB", "primaryRecoveryPeriod"),
        ("CAMBIUM-PTP800-MIB", "requestedProtectionState"),
        ("CAMBIUM-PTP800-MIB", "antennaReceiveLevelDeltaThreshold"),
        ("CAMBIUM-PTP800-MIB", "antennaReceiveLevelMeasurementWindow"),
        ("CAMBIUM-PTP800-MIB", "fiberY"),
        ("CAMBIUM-PTP800-MIB", "rxDiversityVlanTpid"),
        ("CAMBIUM-PTP800-MIB", "rxDiversityVid"))
)
if mibBuilder.loadTexts:
    protectionConfigGroup.setStatus("current")

protectionStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 26)
)
protectionStatusGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "protectionAvailabilityStatus"),
        ("CAMBIUM-PTP800-MIB", "protectionConfigurationStatus"),
        ("CAMBIUM-PTP800-MIB", "protectionState"),
        ("CAMBIUM-PTP800-MIB", "activeUnit"),
        ("CAMBIUM-PTP800-MIB", "protectionSwitchCause"),
        ("CAMBIUM-PTP800-MIB", "endId"),
        ("CAMBIUM-PTP800-MIB", "neighborIPAddress"),
        ("CAMBIUM-PTP800-MIB", "neighborMACAddress"),
        ("CAMBIUM-PTP800-MIB", "wirelessReceiveSignalStatus"),
        ("CAMBIUM-PTP800-MIB", "licensedTransmitCapacityStatus"),
        ("CAMBIUM-PTP800-MIB", "dataPortEthernetSpeedStatus"),
        ("CAMBIUM-PTP800-MIB", "managementPortEthernetSpeedStatus"),
        ("CAMBIUM-PTP800-MIB", "protectionInterfaceStatus"),
        ("CAMBIUM-PTP800-MIB", "remotePrimaryIPAddress"),
        ("CAMBIUM-PTP800-MIB", "remoteSecondaryIPAddress"),
        ("CAMBIUM-PTP800-MIB", "remotePrimaryMACAddress"),
        ("CAMBIUM-PTP800-MIB", "remoteSecondaryMACAddress"),
        ("CAMBIUM-PTP800-MIB", "remotePrimarySecondaryMode"),
        ("CAMBIUM-PTP800-MIB", "transmitterStatus"),
        ("CAMBIUM-PTP800-MIB", "endWirelessReceiveSignalStatus"),
        ("CAMBIUM-PTP800-MIB", "rxDiversityDataPortStatus"),
        ("CAMBIUM-PTP800-MIB", "rxDiversityAvailabilityStatus"),
        ("CAMBIUM-PTP800-MIB", "rxDiversityConfigurationStatus"),
        ("CAMBIUM-PTP800-MIB", "rxDiversityNeighborCompatibility"),
        ("CAMBIUM-PTP800-MIB", "rxDiversityVlanTpidNeighborCompatibility"),
        ("CAMBIUM-PTP800-MIB", "rxDiversityVidNeighborCompatibility"))
)
if mibBuilder.loadTexts:
    protectionStatusGroup.setStatus("current")

protectionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 27)
)
protectionStatsGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "activeCodeWordCount"),
        ("CAMBIUM-PTP800-MIB", "activeCodeWordErrorCount"),
        ("CAMBIUM-PTP800-MIB", "activeByteCount"),
        ("CAMBIUM-PTP800-MIB", "activeByteErrorCount"),
        ("CAMBIUM-PTP800-MIB", "activeAvailableTime"),
        ("CAMBIUM-PTP800-MIB", "activeCounterMeasurementPeriod"),
        ("CAMBIUM-PTP800-MIB", "activeWirelessLinkAvailability"),
        ("CAMBIUM-PTP800-MIB", "activeCodeWordErrorRatio"),
        ("CAMBIUM-PTP800-MIB", "activeByteErrorRatio"))
)
if mibBuilder.loadTexts:
    protectionStatsGroup.setStatus("current")

syslogControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 28)
)
syslogControlGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "syslogClient"),
        ("CAMBIUM-PTP800-MIB", "syslogState"))
)
if mibBuilder.loadTexts:
    syslogControlGroup.setStatus("current")

supplementaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 96)
)
supplementaryGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "longitude"),
        ("CAMBIUM-PTP800-MIB", "latitude"),
        ("CAMBIUM-PTP800-MIB", "altitude"))
)
if mibBuilder.loadTexts:
    supplementaryGroup.setStatus("current")


# Notification objects

dataPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 3)
)
dataPortStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "dataPortStatus")
)
if mibBuilder.loadTexts:
    dataPortStatusTrap.setStatus(
        "current"
    )

linkNameMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 9)
)
linkNameMismatchTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "linkNameMismatch")
)
if mibBuilder.loadTexts:
    linkNameMismatchTrap.setStatus(
        "current"
    )

alignmentModeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 10)
)
alignmentModeTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "alignmentMode")
)
if mibBuilder.loadTexts:
    alignmentModeTrap.setStatus(
        "current"
    )

unitOutOfCalibrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 11)
)
unitOutOfCalibrationTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "unitOutOfCalibration")
)
if mibBuilder.loadTexts:
    unitOutOfCalibrationTrap.setStatus(
        "current"
    )

encryptionEnabledMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 13)
)
encryptionEnabledMismatchTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "encryptionEnabledMismatch")
)
if mibBuilder.loadTexts:
    encryptionEnabledMismatchTrap.setStatus(
        "current"
    )

wirelessLinkDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 16)
)
wirelessLinkDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "wirelessLinkDisabledWarning")
)
if mibBuilder.loadTexts:
    wirelessLinkDisabledWarningTrap.setStatus(
        "current"
    )

dataPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 17)
)
dataPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "dataPortDisabledWarning")
)
if mibBuilder.loadTexts:
    dataPortDisabledWarningTrap.setStatus(
        "current"
    )

dataPortFiberStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 18)
)
dataPortFiberStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "dataPortFiberStatus")
)
if mibBuilder.loadTexts:
    dataPortFiberStatusTrap.setStatus(
        "current"
    )

dataPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 19)
)
dataPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "dataPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    dataPortConfigurationMismatchTrap.setStatus(
        "current"
    )

sNTPSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 21)
)
sNTPSyncTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "sNTPSync")
)
if mibBuilder.loadTexts:
    sNTPSyncTrap.setStatus(
        "current"
    )

managementPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 23)
)
managementPortStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "managementPortStatus")
)
if mibBuilder.loadTexts:
    managementPortStatusTrap.setStatus(
        "current"
    )

managementPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 24)
)
managementPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "managementPortDisabledWarning")
)
if mibBuilder.loadTexts:
    managementPortDisabledWarningTrap.setStatus(
        "current"
    )

rFUStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 27)
)
rFUStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "rFUStatus")
)
if mibBuilder.loadTexts:
    rFUStatusTrap.setStatus(
        "current"
    )

managementPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 28)
)
managementPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "managementPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    managementPortConfigurationMismatchTrap.setStatus(
        "current"
    )

wirelessLinkStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 29)
)
wirelessLinkStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "wirelessLinkStatus")
)
if mibBuilder.loadTexts:
    wirelessLinkStatusTrap.setStatus(
        "current"
    )

protectionAvailabilityStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 31)
)
protectionAvailabilityStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "protectionAvailabilityStatus")
)
if mibBuilder.loadTexts:
    protectionAvailabilityStatusTrap.setStatus(
        "current"
    )

protectionConfigurationStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 32)
)
protectionConfigurationStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "protectionConfigurationStatus")
)
if mibBuilder.loadTexts:
    protectionConfigurationStatusTrap.setStatus(
        "current"
    )

protectionStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 33)
)
protectionStateTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "protectionState")
)
if mibBuilder.loadTexts:
    protectionStateTrap.setStatus(
        "current"
    )

wirelessReceiveSignalStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 34)
)
wirelessReceiveSignalStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "wirelessReceiveSignalStatus")
)
if mibBuilder.loadTexts:
    wirelessReceiveSignalStatusTrap.setStatus(
        "current"
    )

licensedTransmitCapacityStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 36)
)
licensedTransmitCapacityStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "licensedTransmitCapacityStatus")
)
if mibBuilder.loadTexts:
    licensedTransmitCapacityStatusTrap.setStatus(
        "current"
    )

dataPortEthernetSpeedStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 37)
)
dataPortEthernetSpeedStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "dataPortEthernetSpeedStatus")
)
if mibBuilder.loadTexts:
    dataPortEthernetSpeedStatusTrap.setStatus(
        "current"
    )

managementPortEthernetSpeedStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 38)
)
managementPortEthernetSpeedStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "managementPortEthernetSpeedStatus")
)
if mibBuilder.loadTexts:
    managementPortEthernetSpeedStatusTrap.setStatus(
        "current"
    )

protectionInterfaceStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 39)
)
protectionInterfaceStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "protectionInterfaceStatus")
)
if mibBuilder.loadTexts:
    protectionInterfaceStatusTrap.setStatus(
        "current"
    )

syslogStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 40)
)
syslogStateTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "syslogState")
)
if mibBuilder.loadTexts:
    syslogStateTrap.setStatus(
        "current"
    )

syslogLocalNearlyFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 41)
)
if mibBuilder.loadTexts:
    syslogLocalNearlyFullTrap.setStatus(
        "current"
    )

syslogLocalWrappedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 42)
)
if mibBuilder.loadTexts:
    syslogLocalWrappedTrap.setStatus(
        "current"
    )

secureModeAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 43)
)
secureModeAlarmTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "secureModeAlarm")
)
if mibBuilder.loadTexts:
    secureModeAlarmTrap.setStatus(
        "current"
    )

endWirelessReceiveSignalStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 44)
)
endWirelessReceiveSignalStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "endWirelessReceiveSignalStatus")
)
if mibBuilder.loadTexts:
    endWirelessReceiveSignalStatusTrap.setStatus(
        "current"
    )

rxDiversityDataPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 45)
)
rxDiversityDataPortStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "rxDiversityDataPortStatus")
)
if mibBuilder.loadTexts:
    rxDiversityDataPortStatusTrap.setStatus(
        "current"
    )

rxDiversityAvailabilityStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 46)
)
rxDiversityAvailabilityStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "rxDiversityAvailabilityStatus")
)
if mibBuilder.loadTexts:
    rxDiversityAvailabilityStatusTrap.setStatus(
        "current"
    )

rxDiversityConfigurationStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 47)
)
rxDiversityConfigurationStatusTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "rxDiversityConfigurationStatus")
)
if mibBuilder.loadTexts:
    rxDiversityConfigurationStatusTrap.setStatus(
        "current"
    )

rFUPowerButtonPressedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 48)
)
rFUPowerButtonPressedTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "rFUPowerButtonPressed")
)
if mibBuilder.loadTexts:
    rFUPowerButtonPressedTrap.setStatus(
        "current"
    )

syslogClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 8, 99, 0, 49)
)
syslogClientTrap.setObjects(
    ("CAMBIUM-PTP800-MIB", "syslogClient")
)
if mibBuilder.loadTexts:
    syslogClientTrap.setStatus(
        "current"
    )


# Notifications groups

notificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 17713, 8, 98, 99)
)
notificationsGroup.setObjects(
      *(("CAMBIUM-PTP800-MIB", "dataPortStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "linkNameMismatchTrap"),
        ("CAMBIUM-PTP800-MIB", "alignmentModeTrap"),
        ("CAMBIUM-PTP800-MIB", "unitOutOfCalibrationTrap"),
        ("CAMBIUM-PTP800-MIB", "encryptionEnabledMismatchTrap"),
        ("CAMBIUM-PTP800-MIB", "wirelessLinkDisabledWarningTrap"),
        ("CAMBIUM-PTP800-MIB", "dataPortDisabledWarningTrap"),
        ("CAMBIUM-PTP800-MIB", "dataPortFiberStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "dataPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP800-MIB", "sNTPSyncTrap"),
        ("CAMBIUM-PTP800-MIB", "managementPortStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "managementPortDisabledWarningTrap"),
        ("CAMBIUM-PTP800-MIB", "rFUStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "managementPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP800-MIB", "wirelessLinkStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "protectionAvailabilityStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "protectionConfigurationStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "protectionStateTrap"),
        ("CAMBIUM-PTP800-MIB", "wirelessReceiveSignalStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "licensedTransmitCapacityStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "dataPortEthernetSpeedStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "managementPortEthernetSpeedStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "protectionInterfaceStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "syslogStateTrap"),
        ("CAMBIUM-PTP800-MIB", "syslogLocalNearlyFullTrap"),
        ("CAMBIUM-PTP800-MIB", "syslogLocalWrappedTrap"),
        ("CAMBIUM-PTP800-MIB", "secureModeAlarmTrap"),
        ("CAMBIUM-PTP800-MIB", "endWirelessReceiveSignalStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "rxDiversityDataPortStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "rxDiversityAvailabilityStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "rxDiversityConfigurationStatusTrap"),
        ("CAMBIUM-PTP800-MIB", "rFUPowerButtonPressedTrap"),
        ("CAMBIUM-PTP800-MIB", "syslogClientTrap"))
)
if mibBuilder.loadTexts:
    notificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ptpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 17713, 8, 97)
)
if mibBuilder.loadTexts:
    ptpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-PTP800-MIB",
    **{"cambium": cambium,
       "ptp": ptp,
       "ptmp": ptmp,
       "ptp800": ptp800,
       "bridge": bridge,
       "localPacketFiltering": localPacketFiltering,
       "configuration": configuration,
       "iPAddress": iPAddress,
       "subnetMask": subnetMask,
       "gatewayIPAddress": gatewayIPAddress,
       "maximumTransmitPower": maximumTransmitPower,
       "antennaGain": antennaGain,
       "rFFeederLoss": rFFeederLoss,
       "remoteIPAddress": remoteIPAddress,
       "remoteMACAddress": remoteMACAddress,
       "enableTransmission": enableTransmission,
       "aTPCEnable": aTPCEnable,
       "iFCableLength": iFCableLength,
       "linkName": linkName,
       "siteName": siteName,
       "diverseAntennaGain": diverseAntennaGain,
       "diverseRfFeederLoss": diverseRfFeederLoss,
       "ethernet": ethernet,
       "dataPortCopperAutoNegotiation": dataPortCopperAutoNegotiation,
       "dataPortCopperAutoNegAdvertisement": dataPortCopperAutoNegAdvertisement,
       "dataPortStatus": dataPortStatus,
       "dataPortSpeedAndDuplex": dataPortSpeedAndDuplex,
       "dataPortWirelessDownAlert": dataPortWirelessDownAlert,
       "useVLANForManagementInterfaces": useVLANForManagementInterfaces,
       "vLANManagementPriority": vLANManagementPriority,
       "vLANManagementVIDValidation": vLANManagementVIDValidation,
       "vLANManagementVID": vLANManagementVID,
       "ethernetPriorityTableNumber": ethernetPriorityTableNumber,
       "ethernetPriorityTable": ethernetPriorityTable,
       "ethernetPriorityTableEntry": ethernetPriorityTableEntry,
       "ethernetPriorityQueueMapping": ethernetPriorityQueueMapping,
       "ethernetPriorityTableIndex": ethernetPriorityTableIndex,
       "managementPortAutoNegotiation": managementPortAutoNegotiation,
       "managementPortAutoNegAdvertisement": managementPortAutoNegAdvertisement,
       "managementPortStatus": managementPortStatus,
       "managementPortSpeedAndDuplex": managementPortSpeedAndDuplex,
       "managementPortWirelessDownAlert": managementPortWirelessDownAlert,
       "managementMode": managementMode,
       "managementCommittedInformationRate": managementCommittedInformationRate,
       "dataPortPauseFrames": dataPortPauseFrames,
       "transmitCapacityLimit": transmitCapacityLimit,
       "transmitCapacityLimitDetail": transmitCapacityLimitDetail,
       "dataPortEthernetMediaTypeToUse": dataPortEthernetMediaTypeToUse,
       "dataPortCopperForcedConfiguration": dataPortCopperForcedConfiguration,
       "managementPortForcedConfiguration": managementPortForcedConfiguration,
       "l2CPPriorityTableNumber": l2CPPriorityTableNumber,
       "l2CPPriorityTable": l2CPPriorityTable,
       "l2CPPriorityTableEntry": l2CPPriorityTableEntry,
       "l2CPPriorityQueueMapping": l2CPPriorityQueueMapping,
       "l2CPPriorityTableIndex": l2CPPriorityTableIndex,
       "unknownNetworkPriorityQueueMapping": unknownNetworkPriorityQueueMapping,
       "dSCPManagementPriority": dSCPManagementPriority,
       "qOSPriorityScheme": qOSPriorityScheme,
       "iPDSCPPriorityTableNumber": iPDSCPPriorityTableNumber,
       "iPDSCPPriorityTable": iPDSCPPriorityTable,
       "iPDSCPPriorityTableEntry": iPDSCPPriorityTableEntry,
       "iPDSCPPriorityQueueMapping": iPDSCPPriorityQueueMapping,
       "iPDSCPPriorityTableIndex": iPDSCPPriorityTableIndex,
       "mPLSTCPriorityTableNumber": mPLSTCPriorityTableNumber,
       "mPLSTCPriorityTable": mPLSTCPriorityTable,
       "mPLSTCPriorityTableEntry": mPLSTCPriorityTableEntry,
       "mPLSTCPriorityQueueMapping": mPLSTCPriorityQueueMapping,
       "mPLSTCPriorityTableIndex": mPLSTCPriorityTableIndex,
       "licence": licence,
       "productVariant": productVariant,
       "productName": productName,
       "ethernetFiberSupport": ethernetFiberSupport,
       "transmitCapacity": transmitCapacity,
       "encryptionAlgorithmsAvail": encryptionAlgorithmsAvail,
       "securityLevel": securityLevel,
       "management": management,
       "linkNameMismatch": linkNameMismatch,
       "alignmentMode": alignmentMode,
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
       "remoteMaximumTransmitPower": remoteMaximumTransmitPower,
       "minModulation": minModulation,
       "minCodeRate": minCodeRate,
       "maxModulation": maxModulation,
       "maxCodeRate": maxCodeRate,
       "phyStatus": phyStatus,
       "receivePower": receivePower,
       "vectorError": vectorError,
       "transmitPower": transmitPower,
       "linkLoss": linkLoss,
       "receiveModulation": receiveModulation,
       "transmitModulation": transmitModulation,
       "receiveCodeRate": receiveCodeRate,
       "transmitCodeRate": transmitCodeRate,
       "alarms": alarms,
       "unitOutOfCalibration": unitOutOfCalibration,
       "encryptionEnabledMismatch": encryptionEnabledMismatch,
       "wirelessLinkDisabledWarning": wirelessLinkDisabledWarning,
       "dataPortDisabledWarning": dataPortDisabledWarning,
       "dataPortFiberStatus": dataPortFiberStatus,
       "dataPortConfigurationMismatch": dataPortConfigurationMismatch,
       "managementPortDisabledWarning": managementPortDisabledWarning,
       "rFUStatus": rFUStatus,
       "managementPortConfigurationMismatch": managementPortConfigurationMismatch,
       "secureModeAlarm": secureModeAlarm,
       "rFUPlatformCompatibility": rFUPlatformCompatibility,
       "rFUProtectionCompatibility": rFUProtectionCompatibility,
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
       "sNMPTrapVersion": sNMPTrapVersion,
       "sNMPEnabledTraps": sNMPEnabledTraps,
       "enabledDiagnosticAlarms": enabledDiagnosticAlarms,
       "enabledDiagnosticProtectionAlarms": enabledDiagnosticProtectionAlarms,
       "sNMPTrapTableNumber": sNMPTrapTableNumber,
       "sNMPTrapTable": sNMPTrapTable,
       "sNMPTrapTableEntry": sNMPTrapTableEntry,
       "sNMPTrapTableIndex": sNMPTrapTableIndex,
       "sNMPTrapIPAddress": sNMPTrapIPAddress,
       "sNMPTrapPortNumber": sNMPTrapPortNumber,
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
       "sNTPServerResponse": sNTPServerResponse,
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
       "codeWordErrorRatio": codeWordErrorRatio,
       "encryption": encryption,
       "encryptionAlgorithm": encryptionAlgorithm,
       "rfu": rfu,
       "rFURfBand": rFURfBand,
       "rFUTxBandAboveRx": rFUTxBandAboveRx,
       "rFUFreqSpacing": rFUFreqSpacing,
       "rFUTxPowerMin": rFUTxPowerMin,
       "rFUTxPowerMax": rFUTxPowerMax,
       "rFURxFreqMin": rFURxFreqMin,
       "rFURxFreqMax": rFURxFreqMax,
       "rFUTxFreqMin": rFUTxFreqMin,
       "rFUTxFreqMax": rFUTxFreqMax,
       "rFUSerial": rFUSerial,
       "rFUActiveFirmwareBank": rFUActiveFirmwareBank,
       "rFUVersionBank1": rFUVersionBank1,
       "rFUVersionBank2": rFUVersionBank2,
       "rFUType": rFUType,
       "rFURxRFSynthLockAlarm": rFURxRFSynthLockAlarm,
       "rFUTxRFSynthLockAlarm": rFUTxRFSynthLockAlarm,
       "rFUTxPowerAlarm": rFUTxPowerAlarm,
       "rFUCommonIFSynthLockAlarm": rFUCommonIFSynthLockAlarm,
       "rFUPowerAlarm": rFUPowerAlarm,
       "rFULockoutAlarm": rFULockoutAlarm,
       "rFUCableAlarm": rFUCableAlarm,
       "rFUCableAttenuationAdjustAlarm": rFUCableAttenuationAdjustAlarm,
       "rFUTxPowerDegradedAlarm": rFUTxPowerDegradedAlarm,
       "rFURpsAlarm": rFURpsAlarm,
       "rFUTxMuteStatus": rFUTxMuteStatus,
       "rFUFanAssemblyAlarm": rFUFanAssemblyAlarm,
       "rFUHighTemperatureAlarm": rFUHighTemperatureAlarm,
       "rFURFSwitchAlarm": rFURFSwitchAlarm,
       "rFURxIFSynthLockAlarm": rFURxIFSynthLockAlarm,
       "rFUTxIFSynthLockAlarm": rFUTxIFSynthLockAlarm,
       "rFUPowerButtonPressed": rFUPowerButtonPressed,
       "rFUConnectedPlatform": rFUConnectedPlatform,
       "rFUCommonRFSynthLockAlarm": rFUCommonRFSynthLockAlarm,
       "rFUBranchingConfiguration": rFUBranchingConfiguration,
       "rFUTransceiverLocation": rFUTransceiverLocation,
       "rFURfSwitchCableAlarm": rFURfSwitchCableAlarm,
       "rFUReceiveBranchingUnitLoss": rFUReceiveBranchingUnitLoss,
       "rFUTransmitBranchingUnitLoss": rFUTransmitBranchingUnitLoss,
       "radioLicense": radioLicense,
       "radioLicenseIdentifier": radioLicenseIdentifier,
       "radioLicenseBand": radioLicenseBand,
       "radioLicenseRegion": radioLicenseRegion,
       "radioLicenseTxFreq": radioLicenseTxFreq,
       "radioLicenseRxFreq": radioLicenseRxFreq,
       "radioLicenseBandwidth": radioLicenseBandwidth,
       "radioLicenseMaxEIRP": radioLicenseMaxEIRP,
       "radioLicenseModulation": radioLicenseModulation,
       "radioLicenseCodeRate": radioLicenseCodeRate,
       "radioLicenseIncompatibleAlarm": radioLicenseIncompatibleAlarm,
       "radioLicenseMinModulation": radioLicenseMinModulation,
       "radioLicenseMinCodeRate": radioLicenseMinCodeRate,
       "radioLicenseMaxModulation": radioLicenseMaxModulation,
       "radioLicenseMaxCodeRate": radioLicenseMaxCodeRate,
       "protectionConfig": protectionConfig,
       "protection": protection,
       "faultProtectionSwitching": faultProtectionSwitching,
       "primarySecondaryMode": primarySecondaryMode,
       "numberOfAntennas": numberOfAntennas,
       "primaryRecovery": primaryRecovery,
       "primaryRecoveryPeriod": primaryRecoveryPeriod,
       "requestedProtectionState": requestedProtectionState,
       "antennaReceiveLevelDeltaThreshold": antennaReceiveLevelDeltaThreshold,
       "antennaReceiveLevelMeasurementWindow": antennaReceiveLevelMeasurementWindow,
       "fiberY": fiberY,
       "rxDiversityVlanTpid": rxDiversityVlanTpid,
       "rxDiversityVid": rxDiversityVid,
       "protectionStatus": protectionStatus,
       "protectionAvailabilityStatus": protectionAvailabilityStatus,
       "protectionConfigurationStatus": protectionConfigurationStatus,
       "protectionState": protectionState,
       "activeUnit": activeUnit,
       "protectionSwitchCause": protectionSwitchCause,
       "endId": endId,
       "neighborIPAddress": neighborIPAddress,
       "neighborMACAddress": neighborMACAddress,
       "wirelessReceiveSignalStatus": wirelessReceiveSignalStatus,
       "licensedTransmitCapacityStatus": licensedTransmitCapacityStatus,
       "dataPortEthernetSpeedStatus": dataPortEthernetSpeedStatus,
       "managementPortEthernetSpeedStatus": managementPortEthernetSpeedStatus,
       "protectionInterfaceStatus": protectionInterfaceStatus,
       "remotePrimaryIPAddress": remotePrimaryIPAddress,
       "remoteSecondaryIPAddress": remoteSecondaryIPAddress,
       "remotePrimaryMACAddress": remotePrimaryMACAddress,
       "remoteSecondaryMACAddress": remoteSecondaryMACAddress,
       "remotePrimarySecondaryMode": remotePrimarySecondaryMode,
       "transmitterStatus": transmitterStatus,
       "endWirelessReceiveSignalStatus": endWirelessReceiveSignalStatus,
       "rxDiversityDataPortStatus": rxDiversityDataPortStatus,
       "rxDiversityAvailabilityStatus": rxDiversityAvailabilityStatus,
       "rxDiversityConfigurationStatus": rxDiversityConfigurationStatus,
       "rxDiversityNeighborCompatibility": rxDiversityNeighborCompatibility,
       "rxDiversityVlanTpidNeighborCompatibility": rxDiversityVlanTpidNeighborCompatibility,
       "rxDiversityVidNeighborCompatibility": rxDiversityVidNeighborCompatibility,
       "protectionStats": protectionStats,
       "activeCodeWordCount": activeCodeWordCount,
       "activeCodeWordErrorCount": activeCodeWordErrorCount,
       "activeByteCount": activeByteCount,
       "activeByteErrorCount": activeByteErrorCount,
       "activeAvailableTime": activeAvailableTime,
       "activeCounterMeasurementPeriod": activeCounterMeasurementPeriod,
       "activeWirelessLinkAvailability": activeWirelessLinkAvailability,
       "activeCodeWordErrorRatio": activeCodeWordErrorRatio,
       "activeByteErrorRatio": activeByteErrorRatio,
       "syslogControl": syslogControl,
       "syslogClient": syslogClient,
       "syslogState": syslogState,
       "supplementary": supplementary,
       "longitude": longitude,
       "latitude": latitude,
       "altitude": altitude,
       "ptpCompliance": ptpCompliance,
       "ptpGroups": ptpGroups,
       "bridgeGroup": bridgeGroup,
       "configurationGroup": configurationGroup,
       "ethernetGroup": ethernetGroup,
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
       "rfuGroup": rfuGroup,
       "radioLicenseGroup": radioLicenseGroup,
       "protectionConfigGroup": protectionConfigGroup,
       "protectionStatusGroup": protectionStatusGroup,
       "protectionStatsGroup": protectionStatsGroup,
       "syslogControlGroup": syslogControlGroup,
       "supplementaryGroup": supplementaryGroup,
       "notificationsGroup": notificationsGroup,
       "ptpTraps": ptpTraps,
       "ptpTrapPrefix": ptpTrapPrefix,
       "dataPortStatusTrap": dataPortStatusTrap,
       "linkNameMismatchTrap": linkNameMismatchTrap,
       "alignmentModeTrap": alignmentModeTrap,
       "unitOutOfCalibrationTrap": unitOutOfCalibrationTrap,
       "encryptionEnabledMismatchTrap": encryptionEnabledMismatchTrap,
       "wirelessLinkDisabledWarningTrap": wirelessLinkDisabledWarningTrap,
       "dataPortDisabledWarningTrap": dataPortDisabledWarningTrap,
       "dataPortFiberStatusTrap": dataPortFiberStatusTrap,
       "dataPortConfigurationMismatchTrap": dataPortConfigurationMismatchTrap,
       "sNTPSyncTrap": sNTPSyncTrap,
       "managementPortStatusTrap": managementPortStatusTrap,
       "managementPortDisabledWarningTrap": managementPortDisabledWarningTrap,
       "rFUStatusTrap": rFUStatusTrap,
       "managementPortConfigurationMismatchTrap": managementPortConfigurationMismatchTrap,
       "wirelessLinkStatusTrap": wirelessLinkStatusTrap,
       "protectionAvailabilityStatusTrap": protectionAvailabilityStatusTrap,
       "protectionConfigurationStatusTrap": protectionConfigurationStatusTrap,
       "protectionStateTrap": protectionStateTrap,
       "wirelessReceiveSignalStatusTrap": wirelessReceiveSignalStatusTrap,
       "licensedTransmitCapacityStatusTrap": licensedTransmitCapacityStatusTrap,
       "dataPortEthernetSpeedStatusTrap": dataPortEthernetSpeedStatusTrap,
       "managementPortEthernetSpeedStatusTrap": managementPortEthernetSpeedStatusTrap,
       "protectionInterfaceStatusTrap": protectionInterfaceStatusTrap,
       "syslogStateTrap": syslogStateTrap,
       "syslogLocalNearlyFullTrap": syslogLocalNearlyFullTrap,
       "syslogLocalWrappedTrap": syslogLocalWrappedTrap,
       "secureModeAlarmTrap": secureModeAlarmTrap,
       "endWirelessReceiveSignalStatusTrap": endWirelessReceiveSignalStatusTrap,
       "rxDiversityDataPortStatusTrap": rxDiversityDataPortStatusTrap,
       "rxDiversityAvailabilityStatusTrap": rxDiversityAvailabilityStatusTrap,
       "rxDiversityConfigurationStatusTrap": rxDiversityConfigurationStatusTrap,
       "rFUPowerButtonPressedTrap": rFUPowerButtonPressedTrap,
       "syslogClientTrap": syslogClientTrap}
)
