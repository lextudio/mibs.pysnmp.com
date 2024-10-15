# SNMP MIB module (CANOPY-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CANOPY-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:29 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Motorola_ObjectIdentity = ObjectIdentity
motorola = _Motorola_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713)
)
_P2p_ObjectIdentity = ObjectIdentity
p2p = _P2p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1, 5)
)
_IPAddress_Type = IpAddress
_IPAddress_Object = MibScalar
iPAddress = _IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 5, 1),
    _IPAddress_Type()
)
iPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPAddress.setStatus("mandatory")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 5, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetMask.setStatus("mandatory")
_GatewayIPAddress_Type = IpAddress
_GatewayIPAddress_Object = MibScalar
gatewayIPAddress = _GatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 5, 3),
    _GatewayIPAddress_Type()
)
gatewayIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayIPAddress.setStatus("mandatory")


class _TargetMACAddress_Type(OctetString):
    """Custom type targetMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TargetMACAddress_Type.__name__ = "OctetString"
_TargetMACAddress_Object = MibScalar
targetMACAddress = _TargetMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 5, 4),
    _TargetMACAddress_Type()
)
targetMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetMACAddress.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 17713, 1, 5, 5),
    _MasterSlaveMode_Type()
)
masterSlaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterSlaveMode.setStatus("mandatory")


class _MaximumTransmitPower_Type(Integer32):
    """Custom type maximumTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 27),
    )


_MaximumTransmitPower_Type.__name__ = "Integer32"
_MaximumTransmitPower_Object = MibScalar
maximumTransmitPower = _MaximumTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 5, 6),
    _MaximumTransmitPower_Type()
)
maximumTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumTransmitPower.setStatus("mandatory")
_Licence_ObjectIdentity = ObjectIdentity
licence = _Licence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1, 8)
)


class _RegionCode_Type(Integer32):
    """Custom type regionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_RegionCode_Type.__name__ = "Integer32"
_RegionCode_Object = MibScalar
regionCode = _RegionCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 8, 1),
    _RegionCode_Type()
)
regionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regionCode.setStatus("mandatory")


class _ProductVariant_Type(Integer32):
    """Custom type productVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("motorola-canopy-150mbps-backhaul", 11),
          ("motorola-canopy-300mbps-backhaul", 12),
          ("motorola-canopy-30mbps-backhaul", 3),
          ("motorola-canopy-60mbps-backhaul", 2),
          ("spare-1", 4),
          ("spare-2", 5),
          ("spare-3", 6),
          ("spare-4", 7),
          ("spare-5", 8),
          ("spare-6", 9),
          ("spare-7", 10))
    )


_ProductVariant_Type.__name__ = "Integer32"
_ProductVariant_Object = MibScalar
productVariant = _ProductVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 8, 2),
    _ProductVariant_Type()
)
productVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVariant.setStatus("mandatory")


class _ProductName_Type(DisplayString):
    """Custom type productName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProductName_Type.__name__ = "DisplayString"
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 8, 3),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("mandatory")


class _EthernetFibreSupport_Type(Integer32):
    """Custom type ethernetFibreSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EthernetFibreSupport_Type.__name__ = "Integer32"
_EthernetFibreSupport_Object = MibScalar
ethernetFibreSupport = _EthernetFibreSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 8, 4),
    _EthernetFibreSupport_Type()
)
ethernetFibreSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetFibreSupport.setStatus("mandatory")


class _FrequencyVariant_Type(Integer32):
    """Custom type frequencyVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq-4900-mhz", 2),
          ("freq-5400-mhz", 1),
          ("freq-5800-mhz", 0))
    )


_FrequencyVariant_Type.__name__ = "Integer32"
_FrequencyVariant_Object = MibScalar
frequencyVariant = _FrequencyVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 8, 5),
    _FrequencyVariant_Type()
)
frequencyVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyVariant.setStatus("mandatory")
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1, 9)
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
    (1, 3, 6, 1, 4, 1, 17713, 1, 9, 1),
    _TargetRange_Type()
)
targetRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetRange.setStatus("mandatory")


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
        *(("auto-0-100-km", 1),
          ("auto-0-200-km", 2),
          ("auto-0-40-km", 0),
          ("target-range", 3))
    )


_RangingMode_Type.__name__ = "Integer32"
_RangingMode_Object = MibScalar
rangingMode = _RangingMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 9, 2),
    _RangingMode_Type()
)
rangingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangingMode.setStatus("mandatory")
_PhyControl_ObjectIdentity = ObjectIdentity
phyControl = _PhyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1, 10)
)


class _AsymmetricTDD_Type(Integer32):
    """Custom type asymmetricTDD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric-data-rate-2-to-1", 1),
          ("symmetric-data-rate-1-to-1", 0))
    )


_AsymmetricTDD_Type.__name__ = "Integer32"
_AsymmetricTDD_Object = MibScalar
asymmetricTDD = _AsymmetricTDD_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 10, 1),
    _AsymmetricTDD_Type()
)
asymmetricTDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asymmetricTDD.setStatus("mandatory")
_PhyStatus_ObjectIdentity = ObjectIdentity
phyStatus = _PhyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12)
)
_ReceivePower_Type = Integer32
_ReceivePower_Object = MibScalar
receivePower = _ReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 1),
    _ReceivePower_Type()
)
receivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivePower.setStatus("mandatory")
_VectorError_Type = Integer32
_VectorError_Object = MibScalar
vectorError = _VectorError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 2),
    _VectorError_Type()
)
vectorError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vectorError.setStatus("mandatory")
_TransmitPower_Type = Integer32
_TransmitPower_Object = MibScalar
transmitPower = _TransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 3),
    _TransmitPower_Type()
)
transmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitPower.setStatus("mandatory")
_Range_Type = Integer32
_Range_Object = MibScalar
range = _Range_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 4),
    _Range_Type()
)
range.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range.setStatus("mandatory")


class _LinkLoss_Type(Integer32):
    """Custom type linkLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_LinkLoss_Type.__name__ = "Integer32"
_LinkLoss_Object = MibScalar
linkLoss = _LinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 5),
    _LinkLoss_Type()
)
linkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLoss.setStatus("mandatory")


class _ReceiveChannel_Type(Integer32):
    """Custom type receiveChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ReceiveChannel_Type.__name__ = "Integer32"
_ReceiveChannel_Object = MibScalar
receiveChannel = _ReceiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 6),
    _ReceiveChannel_Type()
)
receiveChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveChannel.setStatus("mandatory")


class _TransmitChannel_Type(Integer32):
    """Custom type transmitChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TransmitChannel_Type.__name__ = "Integer32"
_TransmitChannel_Object = MibScalar
transmitChannel = _TransmitChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 7),
    _TransmitChannel_Type()
)
transmitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitChannel.setStatus("mandatory")


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
        *(("mod-16qam-0-63-dual", 16),
          ("mod-16qam-0-63-single-a", 6),
          ("mod-16qam-0-63-single-b", 15),
          ("mod-16qam-0-87-dual", 18),
          ("mod-16qam-0-87-single", 8),
          ("mod-256qam-0-81-dual", 24),
          ("mod-256qam-0-81-single", 14),
          ("mod-64qam-0-75-dual", 20),
          ("mod-64qam-0-75-single", 10),
          ("mod-64qam-0-92-dual", 22),
          ("mod-64qam-0-92-single", 12),
          ("mod-acquisition", 0),
          ("mod-bpsk-0-63", 1),
          ("mod-qpsk-0-63-single", 2),
          ("mod-qpsk-0-87-single", 4),
          ("mod-transient-1", 3),
          ("mod-transient-10", 23),
          ("mod-transient-2", 5),
          ("mod-transient-3", 7),
          ("mod-transient-5", 11),
          ("mod-transient-6", 13),
          ("mod-transient-7", 17),
          ("mod-transient-8", 19),
          ("mod-transient-9", 21))
    )


_ReceiveModulationMode_Type.__name__ = "Integer32"
_ReceiveModulationMode_Object = MibScalar
receiveModulationMode = _ReceiveModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 8),
    _ReceiveModulationMode_Type()
)
receiveModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveModulationMode.setStatus("mandatory")


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
        *(("mod-16qam-0-63-dual", 16),
          ("mod-16qam-0-63-single-a", 6),
          ("mod-16qam-0-63-single-b", 15),
          ("mod-16qam-0-87-dual", 18),
          ("mod-16qam-0-87-single", 8),
          ("mod-256qam-0-81-dual", 24),
          ("mod-256qam-0-81-single", 14),
          ("mod-64qam-0-75-dual", 20),
          ("mod-64qam-0-75-single", 10),
          ("mod-64qam-0-92-dual", 22),
          ("mod-64qam-0-92-single", 12),
          ("mod-acquisition", 0),
          ("mod-bpsk-0-63", 1),
          ("mod-qpsk-0-63-single", 2),
          ("mod-qpsk-0-87-single", 4),
          ("mod-transient-1", 3),
          ("mod-transient-10", 23),
          ("mod-transient-2", 5),
          ("mod-transient-3", 7),
          ("mod-transient-5", 11),
          ("mod-transient-6", 13),
          ("mod-transient-7", 17),
          ("mod-transient-8", 19),
          ("mod-transient-9", 21))
    )


_TransmitModulationMode_Type.__name__ = "Integer32"
_TransmitModulationMode_Object = MibScalar
transmitModulationMode = _TransmitModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 9),
    _TransmitModulationMode_Type()
)
transmitModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitModulationMode.setStatus("mandatory")


class _ReceiveFreq_Type(Integer32):
    """Custom type receiveFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5875),
    )


_ReceiveFreq_Type.__name__ = "Integer32"
_ReceiveFreq_Object = MibScalar
receiveFreq = _ReceiveFreq_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 11),
    _ReceiveFreq_Type()
)
receiveFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveFreq.setStatus("mandatory")


class _TransmitFreq_Type(Integer32):
    """Custom type transmitFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5875),
    )


_TransmitFreq_Type.__name__ = "Integer32"
_TransmitFreq_Object = MibScalar
transmitFreq = _TransmitFreq_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 12),
    _TransmitFreq_Type()
)
transmitFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitFreq.setStatus("mandatory")
_SignalStrengthRatio_Type = Integer32
_SignalStrengthRatio_Object = MibScalar
signalStrengthRatio = _SignalStrengthRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 12, 13),
    _SignalStrengthRatio_Type()
)
signalStrengthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalStrengthRatio.setStatus("mandatory")
_Reset_ObjectIdentity = ObjectIdentity
reset = _Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1, 18)
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
        *(("console-reboot", 1),
          ("running", 0))
    )


_SystemReset_Type.__name__ = "Integer32"
_SystemReset_Object = MibScalar
systemReset = _SystemReset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 18, 1),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("mandatory")
_Versions_ObjectIdentity = ObjectIdentity
versions = _Versions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1, 19)
)


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 19, 1),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("mandatory")


class _HardwareVersion_Type(DisplayString):
    """Custom type hardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HardwareVersion_Type.__name__ = "DisplayString"
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 19, 2),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("mandatory")


class _SecondarySoftwareVersion_Type(DisplayString):
    """Custom type secondarySoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SecondarySoftwareVersion_Type.__name__ = "DisplayString"
_SecondarySoftwareVersion_Object = MibScalar
secondarySoftwareVersion = _SecondarySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 19, 3),
    _SecondarySoftwareVersion_Type()
)
secondarySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondarySoftwareVersion.setStatus("mandatory")


class _BootVersion_Type(DisplayString):
    """Custom type bootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BootVersion_Type.__name__ = "DisplayString"
_BootVersion_Object = MibScalar
bootVersion = _BootVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 19, 4),
    _BootVersion_Type()
)
bootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersion.setStatus("mandatory")
_PubStats_ObjectIdentity = ObjectIdentity
pubStats = _PubStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1, 20)
)
_ReceiveDataRate_Type = Integer32
_ReceiveDataRate_Object = MibScalar
receiveDataRate = _ReceiveDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 20, 1),
    _ReceiveDataRate_Type()
)
receiveDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveDataRate.setStatus("mandatory")
_TransmitDataRate_Type = Integer32
_TransmitDataRate_Object = MibScalar
transmitDataRate = _TransmitDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 20, 2),
    _TransmitDataRate_Type()
)
transmitDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitDataRate.setStatus("mandatory")
_AggregateDataRate_Type = Integer32
_AggregateDataRate_Object = MibScalar
aggregateDataRate = _AggregateDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 20, 3),
    _AggregateDataRate_Type()
)
aggregateDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregateDataRate.setStatus("mandatory")
_Encryption_ObjectIdentity = ObjectIdentity
encryption = _Encryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1, 22)
)


class _DEPRECATEDencryptionAlgorithm_Type(Integer32):
    """Custom type dEPRECATEDencryptionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DEPRECATEDencryptionAlgorithm_Type.__name__ = "Integer32"
_DEPRECATEDencryptionAlgorithm_Object = MibScalar
dEPRECATEDencryptionAlgorithm = _DEPRECATEDencryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 22, 1),
    _DEPRECATEDencryptionAlgorithm_Type()
)
dEPRECATEDencryptionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dEPRECATEDencryptionAlgorithm.setStatus("mandatory")


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
        *(("aes-256-bit-rijndael", 2),
          ("aes-rijndael", 1),
          ("none", 0))
    )


_EncryptionAlgorithm_Type.__name__ = "Integer32"
_EncryptionAlgorithm_Object = MibScalar
encryptionAlgorithm = _EncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 1, 22, 1),
    _EncryptionAlgorithm_Type()
)
encryptionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionAlgorithm.setStatus("mandatory")
_P2pTraps_ObjectIdentity = ObjectIdentity
p2pTraps = _P2pTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1, 99)
)
_P2mp_ObjectIdentity = ObjectIdentity
p2mp = _P2mp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 2)
)

# Managed Objects groups


# Notification objects

dfsChannelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 1, 99, 1)
)
dfsChannelChangeTrap.setObjects(
    ("CANOPY-SYS-MIB", "receiveChannel")
)
if mibBuilder.loadTexts:
    dfsChannelChangeTrap.setStatus(
        "current"
    )

dfsImpulsiveInterferenceDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 1, 99, 2)
)
dfsImpulsiveInterferenceDetectedTrap.setObjects(
    ("CANOPY-SYS-MIB", "receiveChannel")
)
if mibBuilder.loadTexts:
    dfsImpulsiveInterferenceDetectedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CANOPY-SYS-MIB",
    **{"motorola": motorola,
       "p2p": p2p,
       "configuration": configuration,
       "iPAddress": iPAddress,
       "subnetMask": subnetMask,
       "gatewayIPAddress": gatewayIPAddress,
       "targetMACAddress": targetMACAddress,
       "masterSlaveMode": masterSlaveMode,
       "maximumTransmitPower": maximumTransmitPower,
       "licence": licence,
       "regionCode": regionCode,
       "productVariant": productVariant,
       "productName": productName,
       "ethernetFibreSupport": ethernetFibreSupport,
       "frequencyVariant": frequencyVariant,
       "mgmt": mgmt,
       "targetRange": targetRange,
       "rangingMode": rangingMode,
       "phyControl": phyControl,
       "asymmetricTDD": asymmetricTDD,
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
       "receiveFreq": receiveFreq,
       "transmitFreq": transmitFreq,
       "signalStrengthRatio": signalStrengthRatio,
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
       "encryption": encryption,
       "dEPRECATEDencryptionAlgorithm": dEPRECATEDencryptionAlgorithm,
       "encryptionAlgorithm": encryptionAlgorithm,
       "p2pTraps": p2pTraps,
       "dfsChannelChangeTrap": dfsChannelChangeTrap,
       "dfsImpulsiveInterferenceDetectedTrap": dfsImpulsiveInterferenceDetectedTrap,
       "p2mp": p2mp}
)
