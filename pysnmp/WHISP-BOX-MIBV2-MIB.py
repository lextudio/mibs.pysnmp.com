# SNMP MIB module (WHISP-BOX-MIBV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WHISP-BOX-MIBV2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:51 2024
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
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(whispBox,
 whispModules) = mibBuilder.importSymbols(
    "WHISP-GLOBAL-REG-MIB",
    "whispBox",
    "whispModules")

(EventString,
 WhispLUID,
 WhispMACAddress) = mibBuilder.importSymbols(
    "WHISP-TCV2-MIB",
    "EventString",
    "WhispLUID",
    "WhispMACAddress")


# MODULE-IDENTITY

whispBoxLevelMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WhispBoxStatus_ObjectIdentity = ObjectIdentity
whispBoxStatus = _WhispBoxStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1)
)
_WhispBoxSoftwareVer_Type = DisplayString
_WhispBoxSoftwareVer_Object = MibScalar
whispBoxSoftwareVer = _WhispBoxSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 1),
    _WhispBoxSoftwareVer_Type()
)
whispBoxSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBoxSoftwareVer.setStatus("current")
_WhispBoxFPGAVer_Type = DisplayString
_WhispBoxFPGAVer_Object = MibScalar
whispBoxFPGAVer = _WhispBoxFPGAVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 2),
    _WhispBoxFPGAVer_Type()
)
whispBoxFPGAVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBoxFPGAVer.setStatus("current")
_WhispBoxEsn_Type = DisplayString
_WhispBoxEsn_Object = MibScalar
whispBoxEsn = _WhispBoxEsn_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 3),
    _WhispBoxEsn_Type()
)
whispBoxEsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBoxEsn.setStatus("current")
_WhispBoxBoot_Type = DisplayString
_WhispBoxBoot_Object = MibScalar
whispBoxBoot = _WhispBoxBoot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 4),
    _WhispBoxBoot_Type()
)
whispBoxBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBoxBoot.setStatus("current")
_BoxTemperature_Type = DisplayString
_BoxTemperature_Object = MibScalar
boxTemperature = _BoxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 5),
    _BoxTemperature_Type()
)
boxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxTemperature.setStatus("obsolete")
_BoxDeviceType_Type = DisplayString
_BoxDeviceType_Object = MibScalar
boxDeviceType = _BoxDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 6),
    _BoxDeviceType_Type()
)
boxDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxDeviceType.setStatus("current")
_BoxDeviceTypeID_Type = DisplayString
_BoxDeviceTypeID_Object = MibScalar
boxDeviceTypeID = _BoxDeviceTypeID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 7),
    _BoxDeviceTypeID_Type()
)
boxDeviceTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxDeviceTypeID.setStatus("current")
_BoxEncryption_Type = DisplayString
_BoxEncryption_Object = MibScalar
boxEncryption = _BoxEncryption_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 8),
    _BoxEncryption_Type()
)
boxEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxEncryption.setStatus("current")
_EtherLinkStatus_Type = DisplayString
_EtherLinkStatus_Object = MibScalar
etherLinkStatus = _EtherLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 9),
    _EtherLinkStatus_Type()
)
etherLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherLinkStatus.setStatus("current")
_BoxFrequency_Type = DisplayString
_BoxFrequency_Object = MibScalar
boxFrequency = _BoxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 10),
    _BoxFrequency_Type()
)
boxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxFrequency.setStatus("current")
_PlatformVer_Type = Integer32
_PlatformVer_Object = MibScalar
platformVer = _PlatformVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 11),
    _PlatformVer_Type()
)
platformVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformVer.setStatus("current")
_PlatformType_Type = DisplayString
_PlatformType_Object = MibScalar
platformType = _PlatformType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 12),
    _PlatformType_Type()
)
platformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformType.setStatus("current")
_DhcpLanIp_Type = IpAddress
_DhcpLanIp_Object = MibScalar
dhcpLanIp = _DhcpLanIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 13),
    _DhcpLanIp_Type()
)
dhcpLanIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLanIp.setStatus("current")
_DhcpLanSubnetMask_Type = IpAddress
_DhcpLanSubnetMask_Object = MibScalar
dhcpLanSubnetMask = _DhcpLanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 14),
    _DhcpLanSubnetMask_Type()
)
dhcpLanSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLanSubnetMask.setStatus("current")
_DhcpLanGateway_Type = IpAddress
_DhcpLanGateway_Object = MibScalar
dhcpLanGateway = _DhcpLanGateway_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 15),
    _DhcpLanGateway_Type()
)
dhcpLanGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLanGateway.setStatus("current")
_DhcpRfPublicIp_Type = IpAddress
_DhcpRfPublicIp_Object = MibScalar
dhcpRfPublicIp = _DhcpRfPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 16),
    _DhcpRfPublicIp_Type()
)
dhcpRfPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRfPublicIp.setStatus("current")
_DhcpRfPublicSubnetMask_Type = IpAddress
_DhcpRfPublicSubnetMask_Object = MibScalar
dhcpRfPublicSubnetMask = _DhcpRfPublicSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 17),
    _DhcpRfPublicSubnetMask_Type()
)
dhcpRfPublicSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRfPublicSubnetMask.setStatus("current")
_DhcpRfPublicGateway_Type = IpAddress
_DhcpRfPublicGateway_Object = MibScalar
dhcpRfPublicGateway = _DhcpRfPublicGateway_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 18),
    _DhcpRfPublicGateway_Type()
)
dhcpRfPublicGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRfPublicGateway.setStatus("current")
_LanDhcpStatus_Type = DisplayString
_LanDhcpStatus_Object = MibScalar
lanDhcpStatus = _LanDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 19),
    _LanDhcpStatus_Type()
)
lanDhcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDhcpStatus.setStatus("current")
_RfPublicDhcpStatus_Type = DisplayString
_RfPublicDhcpStatus_Object = MibScalar
rfPublicDhcpStatus = _RfPublicDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 20),
    _RfPublicDhcpStatus_Type()
)
rfPublicDhcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfPublicDhcpStatus.setStatus("current")
_InSyncCount_Type = Integer32
_InSyncCount_Object = MibScalar
inSyncCount = _InSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 21),
    _InSyncCount_Type()
)
inSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSyncCount.setStatus("current")
_OutSyncCount_Type = Integer32
_OutSyncCount_Object = MibScalar
outSyncCount = _OutSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 22),
    _OutSyncCount_Type()
)
outSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outSyncCount.setStatus("current")
_PllOutLockCount_Type = Integer32
_PllOutLockCount_Object = MibScalar
pllOutLockCount = _PllOutLockCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 23),
    _PllOutLockCount_Type()
)
pllOutLockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pllOutLockCount.setStatus("current")
_TxCalFailure_Type = Integer32
_TxCalFailure_Object = MibScalar
txCalFailure = _TxCalFailure_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 24),
    _TxCalFailure_Type()
)
txCalFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCalFailure.setStatus("current")
_SwVersion_Type = DisplayString
_SwVersion_Object = MibScalar
swVersion = _SwVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 25),
    _SwVersion_Type()
)
swVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersion.setStatus("current")
_PldVersion_Type = DisplayString
_PldVersion_Object = MibScalar
pldVersion = _PldVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 26),
    _PldVersion_Type()
)
pldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldVersion.setStatus("current")
_PlatformInfo_Type = DisplayString
_PlatformInfo_Object = MibScalar
platformInfo = _PlatformInfo_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 27),
    _PlatformInfo_Type()
)
platformInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformInfo.setStatus("current")
_AntPolarization_Type = DisplayString
_AntPolarization_Object = MibScalar
antPolarization = _AntPolarization_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 28),
    _AntPolarization_Type()
)
antPolarization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antPolarization.setStatus("current")
_PacketOverloadCounter_Type = Counter32
_PacketOverloadCounter_Object = MibScalar
packetOverloadCounter = _PacketOverloadCounter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 29),
    _PacketOverloadCounter_Type()
)
packetOverloadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetOverloadCounter.setStatus("current")
_WhispBoxP11Personality_Type = DisplayString
_WhispBoxP11Personality_Object = MibScalar
whispBoxP11Personality = _WhispBoxP11Personality_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 30),
    _WhispBoxP11Personality_Type()
)
whispBoxP11Personality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBoxP11Personality.setStatus("current")
_WhispBoxP11FPGAType_Type = DisplayString
_WhispBoxP11FPGAType_Object = MibScalar
whispBoxP11FPGAType = _WhispBoxP11FPGAType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 31),
    _WhispBoxP11FPGAType_Type()
)
whispBoxP11FPGAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBoxP11FPGAType.setStatus("current")
_WhispBoxP11BstrapFPGAVer_Type = DisplayString
_WhispBoxP11BstrapFPGAVer_Object = MibScalar
whispBoxP11BstrapFPGAVer = _WhispBoxP11BstrapFPGAVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 32),
    _WhispBoxP11BstrapFPGAVer_Type()
)
whispBoxP11BstrapFPGAVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBoxP11BstrapFPGAVer.setStatus("current")
_NumDFSDetections_Type = Counter32
_NumDFSDetections_Object = MibScalar
numDFSDetections = _NumDFSDetections_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 33),
    _NumDFSDetections_Type()
)
numDFSDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDFSDetections.setStatus("current")
_RxOverrunPkts_Type = Counter32
_RxOverrunPkts_Object = MibScalar
rxOverrunPkts = _RxOverrunPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 34),
    _RxOverrunPkts_Type()
)
rxOverrunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOverrunPkts.setStatus("current")
_BoxTemperatureC_Type = Integer32
_BoxTemperatureC_Object = MibScalar
boxTemperatureC = _BoxTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 35),
    _BoxTemperatureC_Type()
)
boxTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxTemperatureC.setStatus("current")
_BoxTemperatureF_Type = Integer32
_BoxTemperatureF_Object = MibScalar
boxTemperatureF = _BoxTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 36),
    _BoxTemperatureF_Type()
)
boxTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxTemperatureF.setStatus("current")
_BridgeCbFecStatbin_Type = Counter32
_BridgeCbFecStatbin_Object = MibScalar
bridgeCbFecStatbin = _BridgeCbFecStatbin_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 37),
    _BridgeCbFecStatbin_Type()
)
bridgeCbFecStatbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbFecStatbin.setStatus("current")
_BridgeCbFecStatbout_Type = Counter32
_BridgeCbFecStatbout_Object = MibScalar
bridgeCbFecStatbout = _BridgeCbFecStatbout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 38),
    _BridgeCbFecStatbout_Type()
)
bridgeCbFecStatbout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbFecStatbout.setStatus("current")
_BridgeCbFecStatbtoss_Type = Counter32
_BridgeCbFecStatbtoss_Object = MibScalar
bridgeCbFecStatbtoss = _BridgeCbFecStatbtoss_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 39),
    _BridgeCbFecStatbtoss_Type()
)
bridgeCbFecStatbtoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbFecStatbtoss.setStatus("current")
_BridgeCbFecStatbtosscap_Type = Counter32
_BridgeCbFecStatbtosscap_Object = MibScalar
bridgeCbFecStatbtosscap = _BridgeCbFecStatbtosscap_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 40),
    _BridgeCbFecStatbtosscap_Type()
)
bridgeCbFecStatbtosscap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbFecStatbtosscap.setStatus("current")
_BridgeCbFecStatuin_Type = Counter32
_BridgeCbFecStatuin_Object = MibScalar
bridgeCbFecStatuin = _BridgeCbFecStatuin_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 41),
    _BridgeCbFecStatuin_Type()
)
bridgeCbFecStatuin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbFecStatuin.setStatus("current")
_BridgeCbFecStatuout_Type = Counter32
_BridgeCbFecStatuout_Object = MibScalar
bridgeCbFecStatuout = _BridgeCbFecStatuout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 42),
    _BridgeCbFecStatuout_Type()
)
bridgeCbFecStatuout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbFecStatuout.setStatus("current")
_BridgeCbFecStatutoss_Type = Counter32
_BridgeCbFecStatutoss_Object = MibScalar
bridgeCbFecStatutoss = _BridgeCbFecStatutoss_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 43),
    _BridgeCbFecStatutoss_Type()
)
bridgeCbFecStatutoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbFecStatutoss.setStatus("current")
_BridgeCbFecStatutosscap_Type = Counter32
_BridgeCbFecStatutosscap_Object = MibScalar
bridgeCbFecStatutosscap = _BridgeCbFecStatutosscap_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 44),
    _BridgeCbFecStatutosscap_Type()
)
bridgeCbFecStatutosscap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbFecStatutosscap.setStatus("current")
_BridgeCbRFStatbin_Type = Counter32
_BridgeCbRFStatbin_Object = MibScalar
bridgeCbRFStatbin = _BridgeCbRFStatbin_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 45),
    _BridgeCbRFStatbin_Type()
)
bridgeCbRFStatbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbRFStatbin.setStatus("current")
_BridgeCbRFStatbout_Type = Counter32
_BridgeCbRFStatbout_Object = MibScalar
bridgeCbRFStatbout = _BridgeCbRFStatbout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 46),
    _BridgeCbRFStatbout_Type()
)
bridgeCbRFStatbout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbRFStatbout.setStatus("current")
_BridgeCbRFStatbtoss_Type = Counter32
_BridgeCbRFStatbtoss_Object = MibScalar
bridgeCbRFStatbtoss = _BridgeCbRFStatbtoss_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 47),
    _BridgeCbRFStatbtoss_Type()
)
bridgeCbRFStatbtoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbRFStatbtoss.setStatus("current")
_BridgeCbRFStatbtosscap_Type = Counter32
_BridgeCbRFStatbtosscap_Object = MibScalar
bridgeCbRFStatbtosscap = _BridgeCbRFStatbtosscap_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 48),
    _BridgeCbRFStatbtosscap_Type()
)
bridgeCbRFStatbtosscap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbRFStatbtosscap.setStatus("current")
_BridgeCbRFStatuin_Type = Counter32
_BridgeCbRFStatuin_Object = MibScalar
bridgeCbRFStatuin = _BridgeCbRFStatuin_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 49),
    _BridgeCbRFStatuin_Type()
)
bridgeCbRFStatuin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbRFStatuin.setStatus("current")
_BridgeCbRFStatuout_Type = Counter32
_BridgeCbRFStatuout_Object = MibScalar
bridgeCbRFStatuout = _BridgeCbRFStatuout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 50),
    _BridgeCbRFStatuout_Type()
)
bridgeCbRFStatuout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbRFStatuout.setStatus("current")
_BridgeCbRFStatutoss_Type = Counter32
_BridgeCbRFStatutoss_Object = MibScalar
bridgeCbRFStatutoss = _BridgeCbRFStatutoss_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 51),
    _BridgeCbRFStatutoss_Type()
)
bridgeCbRFStatutoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbRFStatutoss.setStatus("current")
_BridgeCbRFStatutosscap_Type = Counter32
_BridgeCbRFStatutosscap_Object = MibScalar
bridgeCbRFStatutosscap = _BridgeCbRFStatutosscap_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 52),
    _BridgeCbRFStatutosscap_Type()
)
bridgeCbRFStatutosscap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbRFStatutosscap.setStatus("current")
_BridgeCbErrStatNI1QSend_Type = Counter32
_BridgeCbErrStatNI1QSend_Object = MibScalar
bridgeCbErrStatNI1QSend = _BridgeCbErrStatNI1QSend_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 53),
    _BridgeCbErrStatNI1QSend_Type()
)
bridgeCbErrStatNI1QSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbErrStatNI1QSend.setStatus("current")
_BridgeCbErrStatNI2QSend_Type = Counter32
_BridgeCbErrStatNI2QSend_Object = MibScalar
bridgeCbErrStatNI2QSend = _BridgeCbErrStatNI2QSend_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 54),
    _BridgeCbErrStatNI2QSend_Type()
)
bridgeCbErrStatNI2QSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbErrStatNI2QSend.setStatus("current")
_BridgeCbErrStatBridgeFull_Type = Counter32
_BridgeCbErrStatBridgeFull_Object = MibScalar
bridgeCbErrStatBridgeFull = _BridgeCbErrStatBridgeFull_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 55),
    _BridgeCbErrStatBridgeFull_Type()
)
bridgeCbErrStatBridgeFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbErrStatBridgeFull.setStatus("current")
_BridgeCbErrStatSendMsg_Type = Counter32
_BridgeCbErrStatSendMsg_Object = MibScalar
bridgeCbErrStatSendMsg = _BridgeCbErrStatSendMsg_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 56),
    _BridgeCbErrStatSendMsg_Type()
)
bridgeCbErrStatSendMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbErrStatSendMsg.setStatus("current")
_BridgeCbErrStatAPFecQSend_Type = Counter32
_BridgeCbErrStatAPFecQSend_Object = MibScalar
bridgeCbErrStatAPFecQSend = _BridgeCbErrStatAPFecQSend_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 57),
    _BridgeCbErrStatAPFecQSend_Type()
)
bridgeCbErrStatAPFecQSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbErrStatAPFecQSend.setStatus("current")
_BridgeCbErrStatApRfQSend_Type = Counter32
_BridgeCbErrStatApRfQSend_Object = MibScalar
bridgeCbErrStatApRfQSend = _BridgeCbErrStatApRfQSend_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 58),
    _BridgeCbErrStatApRfQSend_Type()
)
bridgeCbErrStatApRfQSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbErrStatApRfQSend.setStatus("current")
_RfStatXmtUDataCnt_Type = Counter32
_RfStatXmtUDataCnt_Object = MibScalar
rfStatXmtUDataCnt = _RfStatXmtUDataCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 59),
    _RfStatXmtUDataCnt_Type()
)
rfStatXmtUDataCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatXmtUDataCnt.setStatus("current")
_RfStatXmtBDataCnt_Type = Counter32
_RfStatXmtBDataCnt_Object = MibScalar
rfStatXmtBDataCnt = _RfStatXmtBDataCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 60),
    _RfStatXmtBDataCnt_Type()
)
rfStatXmtBDataCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatXmtBDataCnt.setStatus("current")
_RfStatRcvUDataCnt_Type = Counter32
_RfStatRcvUDataCnt_Object = MibScalar
rfStatRcvUDataCnt = _RfStatRcvUDataCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 61),
    _RfStatRcvUDataCnt_Type()
)
rfStatRcvUDataCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatRcvUDataCnt.setStatus("current")
_RfStatRcvBDataCnt_Type = Counter32
_RfStatRcvBDataCnt_Object = MibScalar
rfStatRcvBDataCnt = _RfStatRcvBDataCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 62),
    _RfStatRcvBDataCnt_Type()
)
rfStatRcvBDataCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatRcvBDataCnt.setStatus("current")
_RfStatXmtCntlCnt_Type = Counter32
_RfStatXmtCntlCnt_Object = MibScalar
rfStatXmtCntlCnt = _RfStatXmtCntlCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 63),
    _RfStatXmtCntlCnt_Type()
)
rfStatXmtCntlCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatXmtCntlCnt.setStatus("current")
_RfStatRcvCntlCnt_Type = Counter32
_RfStatRcvCntlCnt_Object = MibScalar
rfStatRcvCntlCnt = _RfStatRcvCntlCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 64),
    _RfStatRcvCntlCnt_Type()
)
rfStatRcvCntlCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatRcvCntlCnt.setStatus("current")
_RfStatInSyncCount_Type = Counter32
_RfStatInSyncCount_Object = MibScalar
rfStatInSyncCount = _RfStatInSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 65),
    _RfStatInSyncCount_Type()
)
rfStatInSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatInSyncCount.setStatus("current")
_RfStatOutSyncCount_Type = Counter32
_RfStatOutSyncCount_Object = MibScalar
rfStatOutSyncCount = _RfStatOutSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 66),
    _RfStatOutSyncCount_Type()
)
rfStatOutSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatOutSyncCount.setStatus("current")
_RfStatOverrunCount_Type = Counter32
_RfStatOverrunCount_Object = MibScalar
rfStatOverrunCount = _RfStatOverrunCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 67),
    _RfStatOverrunCount_Type()
)
rfStatOverrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatOverrunCount.setStatus("current")
_RfStatUnderrunCount_Type = Counter32
_RfStatUnderrunCount_Object = MibScalar
rfStatUnderrunCount = _RfStatUnderrunCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 68),
    _RfStatUnderrunCount_Type()
)
rfStatUnderrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatUnderrunCount.setStatus("current")
_RfStatRcvCorruptDataCount_Type = Counter32
_RfStatRcvCorruptDataCount_Object = MibScalar
rfStatRcvCorruptDataCount = _RfStatRcvCorruptDataCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 69),
    _RfStatRcvCorruptDataCount_Type()
)
rfStatRcvCorruptDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatRcvCorruptDataCount.setStatus("current")
_RfStatBadBcastCtlCnt_Type = Counter32
_RfStatBadBcastCtlCnt_Object = MibScalar
rfStatBadBcastCtlCnt = _RfStatBadBcastCtlCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 70),
    _RfStatBadBcastCtlCnt_Type()
)
rfStatBadBcastCtlCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatBadBcastCtlCnt.setStatus("current")
_RfStatPLLOutOfLockCnt_Type = Counter32
_RfStatPLLOutOfLockCnt_Object = MibScalar
rfStatPLLOutOfLockCnt = _RfStatPLLOutOfLockCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 71),
    _RfStatPLLOutOfLockCnt_Type()
)
rfStatPLLOutOfLockCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatPLLOutOfLockCnt.setStatus("current")
_RfStatBeaconVerMismatchCnt_Type = Counter32
_RfStatBeaconVerMismatchCnt_Object = MibScalar
rfStatBeaconVerMismatchCnt = _RfStatBeaconVerMismatchCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 72),
    _RfStatBeaconVerMismatchCnt_Type()
)
rfStatBeaconVerMismatchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatBeaconVerMismatchCnt.setStatus("current")
_RfStatBadFreqBcnRcvCnt_Type = Counter32
_RfStatBadFreqBcnRcvCnt_Object = MibScalar
rfStatBadFreqBcnRcvCnt = _RfStatBadFreqBcnRcvCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 73),
    _RfStatBadFreqBcnRcvCnt_Type()
)
rfStatBadFreqBcnRcvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatBadFreqBcnRcvCnt.setStatus("current")
_RfStatnonLiteBcnRcvCnt_Type = Counter32
_RfStatnonLiteBcnRcvCnt_Object = MibScalar
rfStatnonLiteBcnRcvCnt = _RfStatnonLiteBcnRcvCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 74),
    _RfStatnonLiteBcnRcvCnt_Type()
)
rfStatnonLiteBcnRcvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatnonLiteBcnRcvCnt.setStatus("current")
_RfStatUnsupFeatBcnRcvCnt_Type = Counter32
_RfStatUnsupFeatBcnRcvCnt_Object = MibScalar
rfStatUnsupFeatBcnRcvCnt = _RfStatUnsupFeatBcnRcvCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 75),
    _RfStatUnsupFeatBcnRcvCnt_Type()
)
rfStatUnsupFeatBcnRcvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatUnsupFeatBcnRcvCnt.setStatus("current")
_RfStatUnkwnFeatBcnRcvCnt_Type = Counter32
_RfStatUnkwnFeatBcnRcvCnt_Object = MibScalar
rfStatUnkwnFeatBcnRcvCnt = _RfStatUnkwnFeatBcnRcvCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 76),
    _RfStatUnkwnFeatBcnRcvCnt_Type()
)
rfStatUnkwnFeatBcnRcvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatUnkwnFeatBcnRcvCnt.setStatus("current")
_RfStatTxCalFailCnt_Type = Counter32
_RfStatTxCalFailCnt_Object = MibScalar
rfStatTxCalFailCnt = _RfStatTxCalFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 77),
    _RfStatTxCalFailCnt_Type()
)
rfStatTxCalFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatTxCalFailCnt.setStatus("current")
_RfStatBadInSyncIDRcv_Type = Counter32
_RfStatBadInSyncIDRcv_Object = MibScalar
rfStatBadInSyncIDRcv = _RfStatBadInSyncIDRcv_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 78),
    _RfStatBadInSyncIDRcv_Type()
)
rfStatBadInSyncIDRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatBadInSyncIDRcv.setStatus("current")
_RfStatTempOutOfRange_Type = Counter32
_RfStatTempOutOfRange_Object = MibScalar
rfStatTempOutOfRange = _RfStatTempOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 79),
    _RfStatTempOutOfRange_Type()
)
rfStatTempOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatTempOutOfRange.setStatus("current")
_RfStatRSSIOutOfRange_Type = Counter32
_RfStatRSSIOutOfRange_Object = MibScalar
rfStatRSSIOutOfRange = _RfStatRSSIOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 80),
    _RfStatRSSIOutOfRange_Type()
)
rfStatRSSIOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatRSSIOutOfRange.setStatus("current")
_RfStatRangeCapEnf_Type = Counter32
_RfStatRangeCapEnf_Object = MibScalar
rfStatRangeCapEnf = _RfStatRangeCapEnf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 81),
    _RfStatRangeCapEnf_Type()
)
rfStatRangeCapEnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatRangeCapEnf.setStatus("current")
_RfStatRcvLTStart_Type = Counter32
_RfStatRcvLTStart_Object = MibScalar
rfStatRcvLTStart = _RfStatRcvLTStart_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 82),
    _RfStatRcvLTStart_Type()
)
rfStatRcvLTStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatRcvLTStart.setStatus("current")
_RfStatRcvLTStartHS_Type = Counter32
_RfStatRcvLTStartHS_Object = MibScalar
rfStatRcvLTStartHS = _RfStatRcvLTStartHS_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 83),
    _RfStatRcvLTStartHS_Type()
)
rfStatRcvLTStartHS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatRcvLTStartHS.setStatus("current")
_RfStatRcvLTResult_Type = Counter32
_RfStatRcvLTResult_Object = MibScalar
rfStatRcvLTResult = _RfStatRcvLTResult_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 84),
    _RfStatRcvLTResult_Type()
)
rfStatRcvLTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatRcvLTResult.setStatus("current")
_RfStatXmtLTResult_Type = Counter32
_RfStatXmtLTResult_Object = MibScalar
rfStatXmtLTResult = _RfStatXmtLTResult_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 85),
    _RfStatXmtLTResult_Type()
)
rfStatXmtLTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatXmtLTResult.setStatus("current")
_WhispFeatureKeyOrigin_Type = DisplayString
_WhispFeatureKeyOrigin_Object = MibScalar
whispFeatureKeyOrigin = _WhispFeatureKeyOrigin_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 86),
    _WhispFeatureKeyOrigin_Type()
)
whispFeatureKeyOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispFeatureKeyOrigin.setStatus("current")
_RadioMSN_Type = DisplayString
_RadioMSN_Object = MibScalar
radioMSN = _RadioMSN_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 87),
    _RadioMSN_Type()
)
radioMSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioMSN.setStatus("current")
_UpdateStatus_Type = Integer32
_UpdateStatus_Object = MibScalar
updateStatus = _UpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 88),
    _UpdateStatus_Type()
)
updateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updateStatus.setStatus("current")
_SyslogStatTxSuccesses_Type = Integer32
_SyslogStatTxSuccesses_Object = MibScalar
syslogStatTxSuccesses = _SyslogStatTxSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 89),
    _SyslogStatTxSuccesses_Type()
)
syslogStatTxSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogStatTxSuccesses.setStatus("current")
_SyslogStatDropped_Type = Integer32
_SyslogStatDropped_Object = MibScalar
syslogStatDropped = _SyslogStatDropped_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 90),
    _SyslogStatDropped_Type()
)
syslogStatDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogStatDropped.setStatus("current")
_FecStatLinkLost_Type = Counter32
_FecStatLinkLost_Object = MibScalar
fecStatLinkLost = _FecStatLinkLost_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 91),
    _FecStatLinkLost_Type()
)
fecStatLinkLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecStatLinkLost.setStatus("current")
_FecStatLinkDetected_Type = Counter32
_FecStatLinkDetected_Object = MibScalar
fecStatLinkDetected = _FecStatLinkDetected_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 92),
    _FecStatLinkDetected_Type()
)
fecStatLinkDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecStatLinkDetected.setStatus("current")
_NatDhcpStatus_Type = DisplayString
_NatDhcpStatus_Object = MibScalar
natDhcpStatus = _NatDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 93),
    _NatDhcpStatus_Type()
)
natDhcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natDhcpStatus.setStatus("current")
_FecInDiscardsCount_Type = Unsigned32
_FecInDiscardsCount_Object = MibScalar
fecInDiscardsCount = _FecInDiscardsCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 94),
    _FecInDiscardsCount_Type()
)
fecInDiscardsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecInDiscardsCount.setStatus("current")
_FecInErrorsCount_Type = Unsigned32
_FecInErrorsCount_Object = MibScalar
fecInErrorsCount = _FecInErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 95),
    _FecInErrorsCount_Type()
)
fecInErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecInErrorsCount.setStatus("current")
_FecOutDiscardsCount_Type = Unsigned32
_FecOutDiscardsCount_Object = MibScalar
fecOutDiscardsCount = _FecOutDiscardsCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 96),
    _FecOutDiscardsCount_Type()
)
fecOutDiscardsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecOutDiscardsCount.setStatus("current")
_FecOutErrorsCount_Type = Unsigned32
_FecOutErrorsCount_Object = MibScalar
fecOutErrorsCount = _FecOutErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 97),
    _FecOutErrorsCount_Type()
)
fecOutErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecOutErrorsCount.setStatus("current")
_RfInDiscardsCount_Type = Unsigned32
_RfInDiscardsCount_Object = MibScalar
rfInDiscardsCount = _RfInDiscardsCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 98),
    _RfInDiscardsCount_Type()
)
rfInDiscardsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInDiscardsCount.setStatus("current")
_RfInErrorsCount_Type = Unsigned32
_RfInErrorsCount_Object = MibScalar
rfInErrorsCount = _RfInErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 99),
    _RfInErrorsCount_Type()
)
rfInErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInErrorsCount.setStatus("current")
_RfOutDiscardsCount_Type = Unsigned32
_RfOutDiscardsCount_Object = MibScalar
rfOutDiscardsCount = _RfOutDiscardsCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 100),
    _RfOutDiscardsCount_Type()
)
rfOutDiscardsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOutDiscardsCount.setStatus("current")
_RfOutErrorsCount_Type = Unsigned32
_RfOutErrorsCount_Object = MibScalar
rfOutErrorsCount = _RfOutErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 101),
    _RfOutErrorsCount_Type()
)
rfOutErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOutErrorsCount.setStatus("current")
_FecInDiscardsOverloadCount_Type = Counter32
_FecInDiscardsOverloadCount_Object = MibScalar
fecInDiscardsOverloadCount = _FecInDiscardsOverloadCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 102),
    _FecInDiscardsOverloadCount_Type()
)
fecInDiscardsOverloadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecInDiscardsOverloadCount.setStatus("current")
_FecOutDiscardsOverloadCount_Type = Counter32
_FecOutDiscardsOverloadCount_Object = MibScalar
fecOutDiscardsOverloadCount = _FecOutDiscardsOverloadCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 103),
    _FecOutDiscardsOverloadCount_Type()
)
fecOutDiscardsOverloadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecOutDiscardsOverloadCount.setStatus("current")
_RfInDiscardsOverloadCount_Type = Counter32
_RfInDiscardsOverloadCount_Object = MibScalar
rfInDiscardsOverloadCount = _RfInDiscardsOverloadCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 104),
    _RfInDiscardsOverloadCount_Type()
)
rfInDiscardsOverloadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInDiscardsOverloadCount.setStatus("current")
_RfOutDiscardsOverloadCount_Type = Counter32
_RfOutDiscardsOverloadCount_Object = MibScalar
rfOutDiscardsOverloadCount = _RfOutDiscardsOverloadCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 105),
    _RfOutDiscardsOverloadCount_Type()
)
rfOutDiscardsOverloadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOutDiscardsOverloadCount.setStatus("current")
_FpgaCompileInfo_Type = DisplayString
_FpgaCompileInfo_Object = MibScalar
fpgaCompileInfo = _FpgaCompileInfo_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 106),
    _FpgaCompileInfo_Type()
)
fpgaCompileInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaCompileInfo.setStatus("current")
_FpgaBuildDate_Type = DisplayString
_FpgaBuildDate_Object = MibScalar
fpgaBuildDate = _FpgaBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 107),
    _FpgaBuildDate_Type()
)
fpgaBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaBuildDate.setStatus("current")
_AggregateBandwidthCap_Type = Integer32
_AggregateBandwidthCap_Object = MibScalar
aggregateBandwidthCap = _AggregateBandwidthCap_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 108),
    _AggregateBandwidthCap_Type()
)
aggregateBandwidthCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregateBandwidthCap.setStatus("current")


class _CalibrationStatusBool_Type(Integer32):
    """Custom type calibrationStatusBool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("calibrated", 1),
          ("notCalibrated", 0))
    )


_CalibrationStatusBool_Type.__name__ = "Integer32"
_CalibrationStatusBool_Object = MibScalar
calibrationStatusBool = _CalibrationStatusBool_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 109),
    _CalibrationStatusBool_Type()
)
calibrationStatusBool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calibrationStatusBool.setStatus("current")
_CalibrationStatusBox_Type = DisplayString
_CalibrationStatusBox_Object = MibScalar
calibrationStatusBox = _CalibrationStatusBox_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 110),
    _CalibrationStatusBox_Type()
)
calibrationStatusBox.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calibrationStatusBox.setStatus("current")
_RadioEngKeyed_Type = Integer32
_RadioEngKeyed_Object = MibScalar
radioEngKeyed = _RadioEngKeyed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 111),
    _RadioEngKeyed_Type()
)
radioEngKeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioEngKeyed.setStatus("current")
_BridgeCbFecStatfloods_Type = Counter32
_BridgeCbFecStatfloods_Object = MibScalar
bridgeCbFecStatfloods = _BridgeCbFecStatfloods_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 112),
    _BridgeCbFecStatfloods_Type()
)
bridgeCbFecStatfloods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbFecStatfloods.setStatus("current")
_BridgeCbRFStatfloods_Type = Counter32
_BridgeCbRFStatfloods_Object = MibScalar
bridgeCbRFStatfloods = _BridgeCbRFStatfloods_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 113),
    _BridgeCbRFStatfloods_Type()
)
bridgeCbRFStatfloods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCbRFStatfloods.setStatus("current")
_AgcGainRxCH1_Type = Integer32
_AgcGainRxCH1_Object = MibScalar
agcGainRxCH1 = _AgcGainRxCH1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 114),
    _AgcGainRxCH1_Type()
)
agcGainRxCH1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agcGainRxCH1.setStatus("current")
_AgcGainRxCH2_Type = Integer32
_AgcGainRxCH2_Object = MibScalar
agcGainRxCH2 = _AgcGainRxCH2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 115),
    _AgcGainRxCH2_Type()
)
agcGainRxCH2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agcGainRxCH2.setStatus("current")


class _AntType_Type(Integer32):
    """Custom type antType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("integrated", 0))
    )


_AntType_Type.__name__ = "Integer32"
_AntType_Object = MibScalar
antType = _AntType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 116),
    _AntType_Type()
)
antType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antType.setStatus("current")
_RfStatRcvCorruptControlCount_Type = Counter32
_RfStatRcvCorruptControlCount_Object = MibScalar
rfStatRcvCorruptControlCount = _RfStatRcvCorruptControlCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 117),
    _RfStatRcvCorruptControlCount_Type()
)
rfStatRcvCorruptControlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatRcvCorruptControlCount.setStatus("current")
_RfStatXmtMDataCnt_Type = Counter32
_RfStatXmtMDataCnt_Object = MibScalar
rfStatXmtMDataCnt = _RfStatXmtMDataCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 217),
    _RfStatXmtMDataCnt_Type()
)
rfStatXmtMDataCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatXmtMDataCnt.setStatus("current")
_RfStatRcvMDataCnt_Type = Counter32
_RfStatRcvMDataCnt_Object = MibScalar
rfStatRcvMDataCnt = _RfStatRcvMDataCnt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 1, 218),
    _RfStatRcvMDataCnt_Type()
)
rfStatRcvMDataCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfStatRcvMDataCnt.setStatus("current")
_WhispBoxConfig_ObjectIdentity = ObjectIdentity
whispBoxConfig = _WhispBoxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2)
)
_LinkNegoSpeed_Type = DisplayString
_LinkNegoSpeed_Object = MibScalar
linkNegoSpeed = _LinkNegoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 1),
    _LinkNegoSpeed_Type()
)
linkNegoSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkNegoSpeed.setStatus("obsolete")


class _ColorCode_Type(Integer32):
    """Custom type colorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ColorCode_Type.__name__ = "Integer32"
_ColorCode_Object = MibScalar
colorCode = _ColorCode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 2),
    _ColorCode_Type()
)
colorCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCode.setStatus("current")
_DisplayOnlyAccess_Type = DisplayString
_DisplayOnlyAccess_Object = MibScalar
displayOnlyAccess = _DisplayOnlyAccess_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 3),
    _DisplayOnlyAccess_Type()
)
displayOnlyAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    displayOnlyAccess.setStatus("obsolete")
_FullAccess_Type = DisplayString
_FullAccess_Object = MibScalar
fullAccess = _FullAccess_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 4),
    _FullAccess_Type()
)
fullAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fullAccess.setStatus("current")
_WebAutoUpdate_Type = Integer32
_WebAutoUpdate_Object = MibScalar
webAutoUpdate = _WebAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 5),
    _WebAutoUpdate_Type()
)
webAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAutoUpdate.setStatus("current")
if mibBuilder.loadTexts:
    webAutoUpdate.setUnits("Seconds")
_Pass1Status_Type = DisplayString
_Pass1Status_Object = MibScalar
pass1Status = _Pass1Status_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 6),
    _Pass1Status_Type()
)
pass1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pass1Status.setStatus("current")
_Pass2Status_Type = DisplayString
_Pass2Status_Object = MibScalar
pass2Status = _Pass2Status_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 7),
    _Pass2Status_Type()
)
pass2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pass2Status.setStatus("current")


class _BridgeEntryTimeout_Type(Integer32):
    """Custom type bridgeEntryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 1440),
    )


_BridgeEntryTimeout_Type.__name__ = "Integer32"
_BridgeEntryTimeout_Object = MibScalar
bridgeEntryTimeout = _BridgeEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 8),
    _BridgeEntryTimeout_Type()
)
bridgeEntryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEntryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    bridgeEntryTimeout.setUnits("minutes")


class _SnmpMibPerm_Type(Integer32):
    """Custom type snmpMibPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 0))
    )


_SnmpMibPerm_Type.__name__ = "Integer32"
_SnmpMibPerm_Object = MibScalar
snmpMibPerm = _SnmpMibPerm_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 9),
    _SnmpMibPerm_Type()
)
snmpMibPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpMibPerm.setStatus("current")


class _BhTimingMode_Type(Integer32):
    """Custom type bhTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("timeingSlave", 0),
          ("timingMaster", 1))
    )


_BhTimingMode_Type.__name__ = "Integer32"
_BhTimingMode_Object = MibScalar
bhTimingMode = _BhTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 10),
    _BhTimingMode_Type()
)
bhTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bhTimingMode.setStatus("current")


class _BhModulation_Type(Integer32):
    """Custom type bhModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tenMbitsPerSecond", 0),
          ("twentyMbitsPerSecond", 1))
    )


_BhModulation_Type.__name__ = "Integer32"
_BhModulation_Object = MibScalar
bhModulation = _BhModulation_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 11),
    _BhModulation_Type()
)
bhModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bhModulation.setStatus("obsolete")


class _PowerControl_Type(Integer32):
    """Custom type powerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("normal", 1))
    )


_PowerControl_Type.__name__ = "Integer32"
_PowerControl_Object = MibScalar
powerControl = _PowerControl_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 12),
    _PowerControl_Type()
)
powerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerControl.setStatus("current")
_ExtFilterDelay_Type = Integer32
_ExtFilterDelay_Object = MibScalar
extFilterDelay = _ExtFilterDelay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 13),
    _ExtFilterDelay_Type()
)
extFilterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extFilterDelay.setStatus("current")
if mibBuilder.loadTexts:
    extFilterDelay.setUnits("nanoseconds")
_AntennaGain_Type = Integer32
_AntennaGain_Object = MibScalar
antennaGain = _AntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 14),
    _AntennaGain_Type()
)
antennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antennaGain.setStatus("current")
if mibBuilder.loadTexts:
    antennaGain.setUnits("dBi")
_Eirp_Type = Integer32
_Eirp_Object = MibScalar
eirp = _Eirp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 15),
    _Eirp_Type()
)
eirp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eirp.setStatus("obsolete")
if mibBuilder.loadTexts:
    eirp.setUnits("dBm")


class _DynamicLearning_Type(Integer32):
    """Custom type dynamicLearning based on Integer32"""
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


_DynamicLearning_Type.__name__ = "Integer32"
_DynamicLearning_Object = MibScalar
dynamicLearning = _DynamicLearning_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 16),
    _DynamicLearning_Type()
)
dynamicLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicLearning.setStatus("current")
_ManagementVID_Type = Integer32
_ManagementVID_Object = MibScalar
managementVID = _ManagementVID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 17),
    _ManagementVID_Type()
)
managementVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementVID.setStatus("current")
_AgingTimeout_Type = Integer32
_AgingTimeout_Object = MibScalar
agingTimeout = _AgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 18),
    _AgingTimeout_Type()
)
agingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agingTimeout.setStatus("current")


class _FrameType_Type(Integer32):
    """Custom type frameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allframes", 0),
          ("taggedonly", 1),
          ("untaggedonly", 2))
    )


_FrameType_Type.__name__ = "Integer32"
_FrameType_Object = MibScalar
frameType = _FrameType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 19),
    _FrameType_Type()
)
frameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameType.setStatus("current")
_AddVlanMember_Type = Integer32
_AddVlanMember_Object = MibScalar
addVlanMember = _AddVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 20),
    _AddVlanMember_Type()
)
addVlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addVlanMember.setStatus("current")
_RemoveVlanMember_Type = Integer32
_RemoveVlanMember_Object = MibScalar
removeVlanMember = _RemoveVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 21),
    _RemoveVlanMember_Type()
)
removeVlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    removeVlanMember.setStatus("current")


class _Scheduling_Type(Integer32):
    """Custom type scheduling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("hardware", 1)
    )


_Scheduling_Type.__name__ = "Integer32"
_Scheduling_Object = MibScalar
scheduling = _Scheduling_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 22),
    _Scheduling_Type()
)
scheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduling.setStatus("current")
_TransmitterOP_Type = Integer32
_TransmitterOP_Object = MibScalar
transmitterOP = _TransmitterOP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 23),
    _TransmitterOP_Type()
)
transmitterOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmitterOP.setStatus("current")
if mibBuilder.loadTexts:
    transmitterOP.setUnits("dBm")


class _BridgeEnable_Type(Integer32):
    """Custom type bridgeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_BridgeEnable_Type.__name__ = "Integer32"
_BridgeEnable_Object = MibScalar
bridgeEnable = _BridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 24),
    _BridgeEnable_Type()
)
bridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEnable.setStatus("current")


class _FecEnable_Type(Integer32):
    """Custom type fecEnable based on Integer32"""
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


_FecEnable_Type.__name__ = "Integer32"
_FecEnable_Object = MibScalar
fecEnable = _FecEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 25),
    _FecEnable_Type()
)
fecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecEnable.setStatus("current")
_TrapIP1_Type = IpAddress
_TrapIP1_Object = MibScalar
trapIP1 = _TrapIP1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 26),
    _TrapIP1_Type()
)
trapIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP1.setStatus("obsolete")
_TrapIP2_Type = IpAddress
_TrapIP2_Object = MibScalar
trapIP2 = _TrapIP2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 27),
    _TrapIP2_Type()
)
trapIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP2.setStatus("obsolete")
_TrapIP3_Type = IpAddress
_TrapIP3_Object = MibScalar
trapIP3 = _TrapIP3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 28),
    _TrapIP3_Type()
)
trapIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP3.setStatus("obsolete")
_TrapIP4_Type = IpAddress
_TrapIP4_Object = MibScalar
trapIP4 = _TrapIP4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 29),
    _TrapIP4_Type()
)
trapIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP4.setStatus("obsolete")
_TrapIP5_Type = IpAddress
_TrapIP5_Object = MibScalar
trapIP5 = _TrapIP5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 30),
    _TrapIP5_Type()
)
trapIP5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP5.setStatus("obsolete")
_TrapIP6_Type = IpAddress
_TrapIP6_Object = MibScalar
trapIP6 = _TrapIP6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 31),
    _TrapIP6_Type()
)
trapIP6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP6.setStatus("obsolete")
_TrapIP7_Type = IpAddress
_TrapIP7_Object = MibScalar
trapIP7 = _TrapIP7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 32),
    _TrapIP7_Type()
)
trapIP7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP7.setStatus("obsolete")
_TrapIP8_Type = IpAddress
_TrapIP8_Object = MibScalar
trapIP8 = _TrapIP8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 33),
    _TrapIP8_Type()
)
trapIP8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP8.setStatus("obsolete")
_TrapIP9_Type = IpAddress
_TrapIP9_Object = MibScalar
trapIP9 = _TrapIP9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 34),
    _TrapIP9_Type()
)
trapIP9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP9.setStatus("obsolete")
_TrapIP10_Type = IpAddress
_TrapIP10_Object = MibScalar
trapIP10 = _TrapIP10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 35),
    _TrapIP10_Type()
)
trapIP10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP10.setStatus("obsolete")
_CommStringRWrite_Type = DisplayString
_CommStringRWrite_Object = MibScalar
commStringRWrite = _CommStringRWrite_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 36),
    _CommStringRWrite_Type()
)
commStringRWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commStringRWrite.setStatus("current")
_SubnetMask_Type = Integer32
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 37),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_MngtIP_Type = IpAddress
_MngtIP_Object = MibScalar
mngtIP = _MngtIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 38),
    _MngtIP_Type()
)
mngtIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngtIP.setStatus("current")


class _AllowVIDAccess_Type(Integer32):
    """Custom type allowVIDAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_AllowVIDAccess_Type.__name__ = "Integer32"
_AllowVIDAccess_Object = MibScalar
allowVIDAccess = _AllowVIDAccess_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 39),
    _AllowVIDAccess_Type()
)
allowVIDAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowVIDAccess.setStatus("current")


class _SetDefaultPlug_Type(Integer32):
    """Custom type setDefaultPlug based on Integer32"""
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


_SetDefaultPlug_Type.__name__ = "Integer32"
_SetDefaultPlug_Object = MibScalar
setDefaultPlug = _SetDefaultPlug_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 40),
    _SetDefaultPlug_Type()
)
setDefaultPlug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDefaultPlug.setStatus("current")


class _HwsCompatibility_Type(Integer32):
    """Custom type hwsCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_HwsCompatibility_Type.__name__ = "Integer32"
_HwsCompatibility_Object = MibScalar
hwsCompatibility = _HwsCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 41),
    _HwsCompatibility_Type()
)
hwsCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwsCompatibility.setStatus("obsolete")


class _GpsInput_Type(Integer32):
    """Custom type gpsInput based on Integer32"""
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
        *(("autoSync", 4),
          ("autoSyncFreeRun", 5),
          ("generateSyncSignal", 0),
          ("syncToReceivedSignalPowerPort", 2),
          ("syncToReceivedSignalTimingPort", 1),
          ("syncToiGPS", 3))
    )


_GpsInput_Type.__name__ = "Integer32"
_GpsInput_Object = MibScalar
gpsInput = _GpsInput_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 42),
    _GpsInput_Type()
)
gpsInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpsInput.setStatus("current")


class _Ism_Type(Integer32):
    """Custom type ism based on Integer32"""
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


_Ism_Type.__name__ = "Integer32"
_Ism_Object = MibScalar
ism = _Ism_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 43),
    _Ism_Type()
)
ism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ism.setStatus("current")


class _HiPriority_Type(Integer32):
    """Custom type hiPriority based on Integer32"""
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


_HiPriority_Type.__name__ = "Integer32"
_HiPriority_Object = MibScalar
hiPriority = _HiPriority_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 44),
    _HiPriority_Type()
)
hiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiPriority.setStatus("obsolete")
_UserName_Type = DisplayString
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 45),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_UserPassword_Type = DisplayString
_UserPassword_Object = MibScalar
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 46),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")
_UserAccessLevel_Type = Integer32
_UserAccessLevel_Object = MibScalar
userAccessLevel = _UserAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 47),
    _UserAccessLevel_Type()
)
userAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAccessLevel.setStatus("current")
_DeleteUser_Type = DisplayString
_DeleteUser_Object = MibScalar
deleteUser = _DeleteUser_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 48),
    _DeleteUser_Type()
)
deleteUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deleteUser.setStatus("current")


class _TwoXRate_Type(Integer32):
    """Custom type twoXRate based on Integer32"""
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


_TwoXRate_Type.__name__ = "Integer32"
_TwoXRate_Object = MibScalar
twoXRate = _TwoXRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 49),
    _TwoXRate_Type()
)
twoXRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twoXRate.setStatus("obsolete")


class _LanDhcpState_Type(Integer32):
    """Custom type lanDhcpState based on Integer32"""
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


_LanDhcpState_Type.__name__ = "Integer32"
_LanDhcpState_Object = MibScalar
lanDhcpState = _LanDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 50),
    _LanDhcpState_Type()
)
lanDhcpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanDhcpState.setStatus("current")
_SessionTimeout_Type = Integer32
_SessionTimeout_Object = MibScalar
sessionTimeout = _SessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 51),
    _SessionTimeout_Type()
)
sessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionTimeout.setStatus("current")


class _VlanMemberSource_Type(Integer32):
    """Custom type vlanMemberSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("configured", 0))
    )


_VlanMemberSource_Type.__name__ = "Integer32"
_VlanMemberSource_Object = MibScalar
vlanMemberSource = _VlanMemberSource_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 52),
    _VlanMemberSource_Type()
)
vlanMemberSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMemberSource.setStatus("current")
_AddCustomFreqList_Type = DisplayString
_AddCustomFreqList_Object = MibScalar
addCustomFreqList = _AddCustomFreqList_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 53),
    _AddCustomFreqList_Type()
)
addCustomFreqList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addCustomFreqList.setStatus("current")
_RemoveCustomFreqList_Type = DisplayString
_RemoveCustomFreqList_Object = MibScalar
removeCustomFreqList = _RemoveCustomFreqList_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 54),
    _RemoveCustomFreqList_Type()
)
removeCustomFreqList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    removeCustomFreqList.setStatus("current")


class _AllowColocation_Type(Integer32):
    """Custom type allowColocation based on Integer32"""
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


_AllowColocation_Type.__name__ = "Integer32"
_AllowColocation_Object = MibScalar
allowColocation = _AllowColocation_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 55),
    _AllowColocation_Type()
)
allowColocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowColocation.setStatus("obsolete")
_ChangeUsrPwd_Type = DisplayString
_ChangeUsrPwd_Object = MibScalar
changeUsrPwd = _ChangeUsrPwd_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 56),
    _ChangeUsrPwd_Type()
)
changeUsrPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    changeUsrPwd.setStatus("current")
_MngtIP2_Type = IpAddress
_MngtIP2_Object = MibScalar
mngtIP2 = _MngtIP2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 57),
    _MngtIP2_Type()
)
mngtIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngtIP2.setStatus("current")
_SubnetMask2_Type = Integer32
_SubnetMask2_Object = MibScalar
subnetMask2 = _SubnetMask2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 58),
    _SubnetMask2_Type()
)
subnetMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask2.setStatus("current")
_MngtIP3_Type = IpAddress
_MngtIP3_Object = MibScalar
mngtIP3 = _MngtIP3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 59),
    _MngtIP3_Type()
)
mngtIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngtIP3.setStatus("current")
_SubnetMask3_Type = Integer32
_SubnetMask3_Object = MibScalar
subnetMask3 = _SubnetMask3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 60),
    _SubnetMask3_Type()
)
subnetMask3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask3.setStatus("current")
_MngtIP4_Type = IpAddress
_MngtIP4_Object = MibScalar
mngtIP4 = _MngtIP4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 61),
    _MngtIP4_Type()
)
mngtIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngtIP4.setStatus("current")
_SubnetMask4_Type = Integer32
_SubnetMask4_Object = MibScalar
subnetMask4 = _SubnetMask4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 62),
    _SubnetMask4_Type()
)
subnetMask4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask4.setStatus("current")
_MngtIP5_Type = IpAddress
_MngtIP5_Object = MibScalar
mngtIP5 = _MngtIP5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 63),
    _MngtIP5_Type()
)
mngtIP5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngtIP5.setStatus("current")
_SubnetMask5_Type = Integer32
_SubnetMask5_Object = MibScalar
subnetMask5 = _SubnetMask5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 64),
    _SubnetMask5_Type()
)
subnetMask5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask5.setStatus("current")
_MngtIP6_Type = IpAddress
_MngtIP6_Object = MibScalar
mngtIP6 = _MngtIP6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 65),
    _MngtIP6_Type()
)
mngtIP6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngtIP6.setStatus("current")
_SubnetMask6_Type = Integer32
_SubnetMask6_Object = MibScalar
subnetMask6 = _SubnetMask6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 66),
    _SubnetMask6_Type()
)
subnetMask6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask6.setStatus("current")
_MngtIP7_Type = IpAddress
_MngtIP7_Object = MibScalar
mngtIP7 = _MngtIP7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 67),
    _MngtIP7_Type()
)
mngtIP7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngtIP7.setStatus("current")
_SubnetMask7_Type = Integer32
_SubnetMask7_Object = MibScalar
subnetMask7 = _SubnetMask7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 68),
    _SubnetMask7_Type()
)
subnetMask7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask7.setStatus("current")
_MngtIP8_Type = IpAddress
_MngtIP8_Object = MibScalar
mngtIP8 = _MngtIP8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 69),
    _MngtIP8_Type()
)
mngtIP8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngtIP8.setStatus("current")
_SubnetMask8_Type = Integer32
_SubnetMask8_Object = MibScalar
subnetMask8 = _SubnetMask8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 70),
    _SubnetMask8_Type()
)
subnetMask8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask8.setStatus("current")
_MngtIP9_Type = IpAddress
_MngtIP9_Object = MibScalar
mngtIP9 = _MngtIP9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 71),
    _MngtIP9_Type()
)
mngtIP9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngtIP9.setStatus("current")
_SubnetMask9_Type = Integer32
_SubnetMask9_Object = MibScalar
subnetMask9 = _SubnetMask9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 72),
    _SubnetMask9_Type()
)
subnetMask9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask9.setStatus("current")
_MngtIP10_Type = IpAddress
_MngtIP10_Object = MibScalar
mngtIP10 = _MngtIP10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 73),
    _MngtIP10_Type()
)
mngtIP10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngtIP10.setStatus("current")
_SubnetMask10_Type = Integer32
_SubnetMask10_Object = MibScalar
subnetMask10 = _SubnetMask10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 74),
    _SubnetMask10_Type()
)
subnetMask10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask10.setStatus("current")


class _BhvlanEnable_Type(Integer32):
    """Custom type bhvlanEnable based on Integer32"""
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


_BhvlanEnable_Type.__name__ = "Integer32"
_BhvlanEnable_Object = MibScalar
bhvlanEnable = _BhvlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 75),
    _BhvlanEnable_Type()
)
bhvlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bhvlanEnable.setStatus("current")


class _LldpBroadcastEnable_Type(Integer32):
    """Custom type lldpBroadcastEnable based on Integer32"""
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


_LldpBroadcastEnable_Type.__name__ = "Integer32"
_LldpBroadcastEnable_Object = MibScalar
lldpBroadcastEnable = _LldpBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 76),
    _LldpBroadcastEnable_Type()
)
lldpBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpBroadcastEnable.setStatus("current")


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
              11)
        )
    )
    namedValues = NamedValues(
        *(("australia", 6),
          ("brazil", 5),
          ("canada", 3),
          ("europe", 4),
          ("india", 8),
          ("indonesia", 10),
          ("ireland", 11),
          ("none", 0),
          ("other", 1),
          ("russia", 7),
          ("spain", 9),
          ("us", 2))
    )


_RegionCode_Type.__name__ = "Integer32"
_RegionCode_Object = MibScalar
regionCode = _RegionCode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 77),
    _RegionCode_Type()
)
regionCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regionCode.setStatus("deprecated")


class _RussiaRegion_Type(Integer32):
    """Custom type russiaRegion based on Integer32"""
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
        *(("category1", 1),
          ("category2", 2),
          ("category3", 3),
          ("category4", 4))
    )


_RussiaRegion_Type.__name__ = "Integer32"
_RussiaRegion_Object = MibScalar
russiaRegion = _RussiaRegion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 78),
    _RussiaRegion_Type()
)
russiaRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    russiaRegion.setStatus("deprecated")
_CommStringROnly_Type = DisplayString
_CommStringROnly_Object = MibScalar
commStringROnly = _CommStringROnly_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 79),
    _CommStringROnly_Type()
)
commStringROnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commStringROnly.setStatus("current")


class _EthernetLinkSpeed_Type(Integer32):
    """Custom type ethernetLinkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              12,
              13,
              15,
              63)
        )
    )
    namedValues = NamedValues(
        *(("auto1000F-100F-100H-10F-10H", 63),
          ("auto100F-100H", 12),
          ("auto100F-100H-10F-10H", 15),
          ("auto100F-100H-10H", 13),
          ("auto100H-10F-10H", 7),
          ("auto100H-10H", 5),
          ("auto10F-10H", 3),
          ("forced100F", 8),
          ("forced100H", 4),
          ("forced10F", 2),
          ("forced10H", 1))
    )


_EthernetLinkSpeed_Type.__name__ = "Integer32"
_EthernetLinkSpeed_Object = MibScalar
ethernetLinkSpeed = _EthernetLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 80),
    _EthernetLinkSpeed_Type()
)
ethernetLinkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetLinkSpeed.setStatus("current")


class _CyclicPrefix_Type(Integer32):
    """Custom type cyclicPrefix based on Integer32"""
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
        *(("one-eighth", 1),
          ("one-eighth-one-sixteenth", 5),
          ("one-quarter", 0),
          ("one-quarter-one-eighth", 3),
          ("one-quarter-one-eighth-one-sixteenth", 6),
          ("one-quarter-one-sixteenth", 4),
          ("one-sixteenth", 2))
    )


_CyclicPrefix_Type.__name__ = "Integer32"
_CyclicPrefix_Object = MibScalar
cyclicPrefix = _CyclicPrefix_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 81),
    _CyclicPrefix_Type()
)
cyclicPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyclicPrefix.setStatus("current")
_NumberCustomFreq_Type = Integer32
_NumberCustomFreq_Object = MibScalar
numberCustomFreq = _NumberCustomFreq_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 82),
    _NumberCustomFreq_Type()
)
numberCustomFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberCustomFreq.setStatus("current")
_ChannelBandwidth_Type = DisplayString
_ChannelBandwidth_Object = MibScalar
channelBandwidth = _ChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 83),
    _ChannelBandwidth_Type()
)
channelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBandwidth.setStatus("current")


class _SetDefaults_Type(Integer32):
    """Custom type setDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefaultsSet-AwaitingReboot", 2),
          ("noChangeOrUndoFactoryDefaults", 0),
          ("setToFactoryDefaults", 1))
    )


_SetDefaults_Type.__name__ = "Integer32"
_SetDefaults_Object = MibScalar
setDefaults = _SetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 84),
    _SetDefaults_Type()
)
setDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDefaults.setStatus("current")


class _RadioRateAdapt_Type(Integer32):
    """Custom type radioRateAdapt based on Integer32"""
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
        *(("onex", 0),
          ("onexmimo", 4),
          ("onextwox", 1),
          ("onextwoxfourx", 7),
          ("onextwoxfourxsixx", 8),
          ("onextwoxfourxsixxeightx", 9),
          ("onextwoxmimo", 5),
          ("onextwoxthreex", 2),
          ("onextwoxthreexfourx", 3))
    )


_RadioRateAdapt_Type.__name__ = "Integer32"
_RadioRateAdapt_Object = MibScalar
radioRateAdapt = _RadioRateAdapt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 85),
    _RadioRateAdapt_Type()
)
radioRateAdapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioRateAdapt.setStatus("current")


class _SiteInfoViewable_Type(Integer32):
    """Custom type siteInfoViewable based on Integer32"""
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


_SiteInfoViewable_Type.__name__ = "Integer32"
_SiteInfoViewable_Object = MibScalar
siteInfoViewable = _SiteInfoViewable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 86),
    _SiteInfoViewable_Type()
)
siteInfoViewable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteInfoViewable.setStatus("current")


class _LargeVCQ_Type(Integer32):
    """Custom type largeVCQ based on Integer32"""
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


_LargeVCQ_Type.__name__ = "Integer32"
_LargeVCQ_Object = MibScalar
largeVCQ = _LargeVCQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 87),
    _LargeVCQ_Type()
)
largeVCQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    largeVCQ.setStatus("current")
_Latitude_Type = DisplayString
_Latitude_Object = MibScalar
latitude = _Latitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 88),
    _Latitude_Type()
)
latitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latitude.setStatus("current")
_Longitude_Type = DisplayString
_Longitude_Object = MibScalar
longitude = _Longitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 89),
    _Longitude_Type()
)
longitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    longitude.setStatus("current")


class _Height_Type(Integer32):
    """Custom type height based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_Height_Type.__name__ = "Integer32"
_Height_Object = MibScalar
height = _Height_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 90),
    _Height_Type()
)
height.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    height.setStatus("current")


class _Bandwidth_Type(Integer32):
    """Custom type bandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth10-20mhz", 10),
          ("bandwidth10mhz", 3),
          ("bandwidth20mhz", 5),
          ("bandwidth5-10-20mhz", 11),
          ("bandwidth5-10mhz", 8),
          ("bandwidth5-20mhz", 9),
          ("bandwidth5mhz", 1))
    )


_Bandwidth_Type.__name__ = "Integer32"
_Bandwidth_Object = MibScalar
bandwidth = _Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 91),
    _Bandwidth_Type()
)
bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidth.setStatus("current")


class _DataScramblingMethod_Type(Integer32):
    """Custom type dataScramblingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("legacyDataScrambling", 0),
          ("r10DataScrambling", 1))
    )


_DataScramblingMethod_Type.__name__ = "Integer32"
_DataScramblingMethod_Object = MibScalar
dataScramblingMethod = _DataScramblingMethod_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 92),
    _DataScramblingMethod_Type()
)
dataScramblingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataScramblingMethod.setStatus("obsolete")
_PortVID_Type = Integer32
_PortVID_Object = MibScalar
portVID = _PortVID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 93),
    _PortVID_Type()
)
portVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVID.setStatus("current")


class _RadioRateAdaptUL_Type(Integer32):
    """Custom type radioRateAdaptUL based on Integer32"""
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
        *(("onex", 0),
          ("onexmimo", 4),
          ("onextwox", 1),
          ("onextwoxfourx", 7),
          ("onextwoxfourxsixx", 8),
          ("onextwoxfourxsixxeightx", 9),
          ("onextwoxmimo", 5),
          ("onextwoxthreex", 2),
          ("onextwoxthreexfourx", 3))
    )


_RadioRateAdaptUL_Type.__name__ = "Integer32"
_RadioRateAdaptUL_Object = MibScalar
radioRateAdaptUL = _RadioRateAdaptUL_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 94),
    _RadioRateAdaptUL_Type()
)
radioRateAdaptUL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioRateAdaptUL.setStatus("current")
_ProviderVID_Type = Integer32
_ProviderVID_Object = MibScalar
providerVID = _ProviderVID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 95),
    _ProviderVID_Type()
)
providerVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    providerVID.setStatus("current")
_Mac1VIDMapAddr_Type = MacAddress
_Mac1VIDMapAddr_Object = MibScalar
mac1VIDMapAddr = _Mac1VIDMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 96),
    _Mac1VIDMapAddr_Type()
)
mac1VIDMapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac1VIDMapAddr.setStatus("current")
_Mac1VIDMapVid_Type = Integer32
_Mac1VIDMapVid_Object = MibScalar
mac1VIDMapVid = _Mac1VIDMapVid_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 97),
    _Mac1VIDMapVid_Type()
)
mac1VIDMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac1VIDMapVid.setStatus("current")
_Mac2VIDMapAddr_Type = MacAddress
_Mac2VIDMapAddr_Object = MibScalar
mac2VIDMapAddr = _Mac2VIDMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 98),
    _Mac2VIDMapAddr_Type()
)
mac2VIDMapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac2VIDMapAddr.setStatus("current")
_Mac2VIDMapVid_Type = Integer32
_Mac2VIDMapVid_Object = MibScalar
mac2VIDMapVid = _Mac2VIDMapVid_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 99),
    _Mac2VIDMapVid_Type()
)
mac2VIDMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac2VIDMapVid.setStatus("current")
_Mac3VIDMapAddr_Type = MacAddress
_Mac3VIDMapAddr_Object = MibScalar
mac3VIDMapAddr = _Mac3VIDMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 100),
    _Mac3VIDMapAddr_Type()
)
mac3VIDMapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac3VIDMapAddr.setStatus("current")
_Mac3VIDMapVid_Type = Integer32
_Mac3VIDMapVid_Object = MibScalar
mac3VIDMapVid = _Mac3VIDMapVid_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 101),
    _Mac3VIDMapVid_Type()
)
mac3VIDMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac3VIDMapVid.setStatus("current")
_Mac4VIDMapAddr_Type = MacAddress
_Mac4VIDMapAddr_Object = MibScalar
mac4VIDMapAddr = _Mac4VIDMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 102),
    _Mac4VIDMapAddr_Type()
)
mac4VIDMapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac4VIDMapAddr.setStatus("current")
_Mac4VIDMapVid_Type = Integer32
_Mac4VIDMapVid_Object = MibScalar
mac4VIDMapVid = _Mac4VIDMapVid_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 103),
    _Mac4VIDMapVid_Type()
)
mac4VIDMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac4VIDMapVid.setStatus("current")
_Mac5VIDMapAddr_Type = MacAddress
_Mac5VIDMapAddr_Object = MibScalar
mac5VIDMapAddr = _Mac5VIDMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 104),
    _Mac5VIDMapAddr_Type()
)
mac5VIDMapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac5VIDMapAddr.setStatus("current")
_Mac5VIDMapVid_Type = Integer32
_Mac5VIDMapVid_Object = MibScalar
mac5VIDMapVid = _Mac5VIDMapVid_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 105),
    _Mac5VIDMapVid_Type()
)
mac5VIDMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac5VIDMapVid.setStatus("current")
_Mac6VIDMapAddr_Type = MacAddress
_Mac6VIDMapAddr_Object = MibScalar
mac6VIDMapAddr = _Mac6VIDMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 106),
    _Mac6VIDMapAddr_Type()
)
mac6VIDMapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac6VIDMapAddr.setStatus("current")
_Mac6VIDMapVid_Type = Integer32
_Mac6VIDMapVid_Object = MibScalar
mac6VIDMapVid = _Mac6VIDMapVid_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 107),
    _Mac6VIDMapVid_Type()
)
mac6VIDMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac6VIDMapVid.setStatus("current")
_Mac7VIDMapAddr_Type = MacAddress
_Mac7VIDMapAddr_Object = MibScalar
mac7VIDMapAddr = _Mac7VIDMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 108),
    _Mac7VIDMapAddr_Type()
)
mac7VIDMapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac7VIDMapAddr.setStatus("current")
_Mac7VIDMapVid_Type = Integer32
_Mac7VIDMapVid_Object = MibScalar
mac7VIDMapVid = _Mac7VIDMapVid_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 109),
    _Mac7VIDMapVid_Type()
)
mac7VIDMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac7VIDMapVid.setStatus("current")
_Mac8VIDMapAddr_Type = MacAddress
_Mac8VIDMapAddr_Object = MibScalar
mac8VIDMapAddr = _Mac8VIDMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 110),
    _Mac8VIDMapAddr_Type()
)
mac8VIDMapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac8VIDMapAddr.setStatus("current")
_Mac8VIDMapVid_Type = Integer32
_Mac8VIDMapVid_Object = MibScalar
mac8VIDMapVid = _Mac8VIDMapVid_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 111),
    _Mac8VIDMapVid_Type()
)
mac8VIDMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac8VIDMapVid.setStatus("current")
_Mac9VIDMapAddr_Type = MacAddress
_Mac9VIDMapAddr_Object = MibScalar
mac9VIDMapAddr = _Mac9VIDMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 112),
    _Mac9VIDMapAddr_Type()
)
mac9VIDMapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac9VIDMapAddr.setStatus("current")
_Mac9VIDMapVid_Type = Integer32
_Mac9VIDMapVid_Object = MibScalar
mac9VIDMapVid = _Mac9VIDMapVid_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 113),
    _Mac9VIDMapVid_Type()
)
mac9VIDMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac9VIDMapVid.setStatus("current")
_Mac10VIDMapAddr_Type = MacAddress
_Mac10VIDMapAddr_Object = MibScalar
mac10VIDMapAddr = _Mac10VIDMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 114),
    _Mac10VIDMapAddr_Type()
)
mac10VIDMapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac10VIDMapAddr.setStatus("current")
_Mac10VIDMapVid_Type = Integer32
_Mac10VIDMapVid_Object = MibScalar
mac10VIDMapVid = _Mac10VIDMapVid_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 115),
    _Mac10VIDMapVid_Type()
)
mac10VIDMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac10VIDMapVid.setStatus("current")


class _VlanPortType_Type(Integer32):
    """Custom type vlanPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("q", 0),
          ("qinq", 1))
    )


_VlanPortType_Type.__name__ = "Integer32"
_VlanPortType_Object = MibScalar
vlanPortType = _VlanPortType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 116),
    _VlanPortType_Type()
)
vlanPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortType.setStatus("current")


class _VlanAcceptQinQFrames_Type(Integer32):
    """Custom type vlanAcceptQinQFrames based on Integer32"""
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


_VlanAcceptQinQFrames_Type.__name__ = "Integer32"
_VlanAcceptQinQFrames_Object = MibScalar
vlanAcceptQinQFrames = _VlanAcceptQinQFrames_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 117),
    _VlanAcceptQinQFrames_Type()
)
vlanAcceptQinQFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAcceptQinQFrames.setStatus("current")


class _WhispWebUserAccessMode_Type(Integer32):
    """Custom type whispWebUserAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1),
          ("remotethenlocal", 2))
    )


_WhispWebUserAccessMode_Type.__name__ = "Integer32"
_WhispWebUserAccessMode_Object = MibScalar
whispWebUserAccessMode = _WhispWebUserAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 118),
    _WhispWebUserAccessMode_Type()
)
whispWebUserAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    whispWebUserAccessMode.setStatus("current")


class _UsrAccountEnableAccounting_Type(Integer32):
    """Custom type usrAccountEnableAccounting based on Integer32"""
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
        *(("all", 3),
          ("dataUsage", 2),
          ("deviceAccess", 1),
          ("disable", 0))
    )


_UsrAccountEnableAccounting_Type.__name__ = "Integer32"
_UsrAccountEnableAccounting_Object = MibScalar
usrAccountEnableAccounting = _UsrAccountEnableAccounting_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 119),
    _UsrAccountEnableAccounting_Type()
)
usrAccountEnableAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usrAccountEnableAccounting.setStatus("current")


class _AllowRejectThenLocal_Type(Integer32):
    """Custom type allowRejectThenLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowLocalAuthIfAAAReject", 1),
          ("doNotAllowLocalAuthifAAAReject", 0))
    )


_AllowRejectThenLocal_Type.__name__ = "Integer32"
_AllowRejectThenLocal_Object = MibScalar
allowRejectThenLocal = _AllowRejectThenLocal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 120),
    _AllowRejectThenLocal_Type()
)
allowRejectThenLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowRejectThenLocal.setStatus("current")


class _SnrCalculation_Type(Integer32):
    """Custom type snrCalculation based on Integer32"""
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


_SnrCalculation_Type.__name__ = "Integer32"
_SnrCalculation_Object = MibScalar
snrCalculation = _SnrCalculation_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 121),
    _SnrCalculation_Type()
)
snrCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snrCalculation.setStatus("deprecated")


class _PriorityPrecedence_Type(Integer32):
    """Custom type priorityPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("diffservThenEight021p", 1),
          ("eight021pThenDiffServ", 0))
    )


_PriorityPrecedence_Type.__name__ = "Integer32"
_PriorityPrecedence_Object = MibScalar
priorityPrecedence = _PriorityPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 122),
    _PriorityPrecedence_Type()
)
priorityPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityPrecedence.setStatus("current")


class _InstallationColorCode_Type(Integer32):
    """Custom type installationColorCode based on Integer32"""
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


_InstallationColorCode_Type.__name__ = "Integer32"
_InstallationColorCode_Object = MibScalar
installationColorCode = _InstallationColorCode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 123),
    _InstallationColorCode_Type()
)
installationColorCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    installationColorCode.setStatus("current")


class _ApSmMode_Type(Integer32):
    """Custom type apSmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ap", 0),
          ("sm", 1))
    )


_ApSmMode_Type.__name__ = "Integer32"
_ApSmMode_Object = MibScalar
apSmMode = _ApSmMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 124),
    _ApSmMode_Type()
)
apSmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSmMode.setStatus("current")


class _PppoeFilter_Type(Integer32):
    """Custom type pppoeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_PppoeFilter_Type.__name__ = "Integer32"
_PppoeFilter_Object = MibScalar
pppoeFilter = _PppoeFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 125),
    _PppoeFilter_Type()
)
pppoeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeFilter.setStatus("current")


class _SmbFilter_Type(Integer32):
    """Custom type smbFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_SmbFilter_Type.__name__ = "Integer32"
_SmbFilter_Object = MibScalar
smbFilter = _SmbFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 126),
    _SmbFilter_Type()
)
smbFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smbFilter.setStatus("current")


class _SnmpFilter_Type(Integer32):
    """Custom type snmpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_SnmpFilter_Type.__name__ = "Integer32"
_SnmpFilter_Object = MibScalar
snmpFilter = _SnmpFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 127),
    _SnmpFilter_Type()
)
snmpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFilter.setStatus("current")


class _UserP1Filter_Type(Integer32):
    """Custom type userP1Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_UserP1Filter_Type.__name__ = "Integer32"
_UserP1Filter_Object = MibScalar
userP1Filter = _UserP1Filter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 128),
    _UserP1Filter_Type()
)
userP1Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userP1Filter.setStatus("current")


class _UserP2Filter_Type(Integer32):
    """Custom type userP2Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_UserP2Filter_Type.__name__ = "Integer32"
_UserP2Filter_Object = MibScalar
userP2Filter = _UserP2Filter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 129),
    _UserP2Filter_Type()
)
userP2Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userP2Filter.setStatus("current")


class _UserP3Filter_Type(Integer32):
    """Custom type userP3Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_UserP3Filter_Type.__name__ = "Integer32"
_UserP3Filter_Object = MibScalar
userP3Filter = _UserP3Filter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 130),
    _UserP3Filter_Type()
)
userP3Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userP3Filter.setStatus("current")


class _AllOtherIpFilter_Type(Integer32):
    """Custom type allOtherIpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_AllOtherIpFilter_Type.__name__ = "Integer32"
_AllOtherIpFilter_Object = MibScalar
allOtherIpFilter = _AllOtherIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 131),
    _AllOtherIpFilter_Type()
)
allOtherIpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allOtherIpFilter.setStatus("current")


class _AllIpv4Filter_Type(Integer32):
    """Custom type allIpv4Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_AllIpv4Filter_Type.__name__ = "Integer32"
_AllIpv4Filter_Object = MibScalar
allIpv4Filter = _AllIpv4Filter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 132),
    _AllIpv4Filter_Type()
)
allIpv4Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allIpv4Filter.setStatus("current")


class _ArpFilter_Type(Integer32):
    """Custom type arpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_ArpFilter_Type.__name__ = "Integer32"
_ArpFilter_Object = MibScalar
arpFilter = _ArpFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 133),
    _ArpFilter_Type()
)
arpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpFilter.setStatus("current")


class _AllOthersFilter_Type(Integer32):
    """Custom type allOthersFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_AllOthersFilter_Type.__name__ = "Integer32"
_AllOthersFilter_Object = MibScalar
allOthersFilter = _AllOthersFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 134),
    _AllOthersFilter_Type()
)
allOthersFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allOthersFilter.setStatus("current")
_UserDefinedPort1_Type = Integer32
_UserDefinedPort1_Object = MibScalar
userDefinedPort1 = _UserDefinedPort1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 135),
    _UserDefinedPort1_Type()
)
userDefinedPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDefinedPort1.setStatus("current")


class _Port1TCPFilter_Type(Integer32):
    """Custom type port1TCPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port1TCPFilter_Type.__name__ = "Integer32"
_Port1TCPFilter_Object = MibScalar
port1TCPFilter = _Port1TCPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 136),
    _Port1TCPFilter_Type()
)
port1TCPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1TCPFilter.setStatus("current")


class _Port1UDPFilter_Type(Integer32):
    """Custom type port1UDPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port1UDPFilter_Type.__name__ = "Integer32"
_Port1UDPFilter_Object = MibScalar
port1UDPFilter = _Port1UDPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 137),
    _Port1UDPFilter_Type()
)
port1UDPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1UDPFilter.setStatus("current")
_UserDefinedPort2_Type = Integer32
_UserDefinedPort2_Object = MibScalar
userDefinedPort2 = _UserDefinedPort2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 138),
    _UserDefinedPort2_Type()
)
userDefinedPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDefinedPort2.setStatus("current")


class _Port2TCPFilter_Type(Integer32):
    """Custom type port2TCPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port2TCPFilter_Type.__name__ = "Integer32"
_Port2TCPFilter_Object = MibScalar
port2TCPFilter = _Port2TCPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 139),
    _Port2TCPFilter_Type()
)
port2TCPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2TCPFilter.setStatus("current")


class _Port2UDPFilter_Type(Integer32):
    """Custom type port2UDPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port2UDPFilter_Type.__name__ = "Integer32"
_Port2UDPFilter_Object = MibScalar
port2UDPFilter = _Port2UDPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 140),
    _Port2UDPFilter_Type()
)
port2UDPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2UDPFilter.setStatus("current")
_UserDefinedPort3_Type = Integer32
_UserDefinedPort3_Object = MibScalar
userDefinedPort3 = _UserDefinedPort3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 141),
    _UserDefinedPort3_Type()
)
userDefinedPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDefinedPort3.setStatus("current")


class _Port3TCPFilter_Type(Integer32):
    """Custom type port3TCPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port3TCPFilter_Type.__name__ = "Integer32"
_Port3TCPFilter_Object = MibScalar
port3TCPFilter = _Port3TCPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 142),
    _Port3TCPFilter_Type()
)
port3TCPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3TCPFilter.setStatus("current")


class _Port3UDPFilter_Type(Integer32):
    """Custom type port3UDPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Port3UDPFilter_Type.__name__ = "Integer32"
_Port3UDPFilter_Object = MibScalar
port3UDPFilter = _Port3UDPFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 143),
    _Port3UDPFilter_Type()
)
port3UDPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3UDPFilter.setStatus("current")


class _BootpcFilter_Type(Integer32):
    """Custom type bootpcFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_BootpcFilter_Type.__name__ = "Integer32"
_BootpcFilter_Object = MibScalar
bootpcFilter = _BootpcFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 144),
    _BootpcFilter_Type()
)
bootpcFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpcFilter.setStatus("current")


class _BootpsFilter_Type(Integer32):
    """Custom type bootpsFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_BootpsFilter_Type.__name__ = "Integer32"
_BootpsFilter_Object = MibScalar
bootpsFilter = _BootpsFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 145),
    _BootpsFilter_Type()
)
bootpsFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpsFilter.setStatus("current")


class _Ip4MultFilter_Type(Integer32):
    """Custom type ip4MultFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filterOff", 0),
          ("filterOn", 1))
    )


_Ip4MultFilter_Type.__name__ = "Integer32"
_Ip4MultFilter_Object = MibScalar
ip4MultFilter = _Ip4MultFilter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 146),
    _Ip4MultFilter_Type()
)
ip4MultFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip4MultFilter.setStatus("current")


class _PacketFilterDirection_Type(Integer32):
    """Custom type packetFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )


_PacketFilterDirection_Type.__name__ = "Integer32"
_PacketFilterDirection_Object = MibScalar
packetFilterDirection = _PacketFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 147),
    _PacketFilterDirection_Type()
)
packetFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    packetFilterDirection.setStatus("current")


class _EncryptionConfig_Type(Integer32):
    """Custom type encryptionConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aes", 1),
          ("des", 0))
    )


_EncryptionConfig_Type.__name__ = "Integer32"
_EncryptionConfig_Object = MibScalar
encryptionConfig = _EncryptionConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 148),
    _EncryptionConfig_Type()
)
encryptionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryptionConfig.setStatus("current")


class _PppoeCtlPriority_Type(Integer32):
    """Custom type pppoeCtlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_PppoeCtlPriority_Type.__name__ = "Integer32"
_PppoeCtlPriority_Object = MibScalar
pppoeCtlPriority = _PppoeCtlPriority_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 149),
    _PppoeCtlPriority_Type()
)
pppoeCtlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeCtlPriority.setStatus("current")
_FtpPort_Type = Integer32
_FtpPort_Object = MibScalar
ftpPort = _FtpPort_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 150),
    _FtpPort_Type()
)
ftpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPort.setStatus("current")
_HttpPort_Type = Integer32
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 151),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")
_SnmpPort_Type = Integer32
_SnmpPort_Object = MibScalar
snmpPort = _SnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 153),
    _SnmpPort_Type()
)
snmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPort.setStatus("current")
_SnmpTrapPort_Type = Integer32
_SnmpTrapPort_Object = MibScalar
snmpTrapPort = _SnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 154),
    _SnmpTrapPort_Type()
)
snmpTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapPort.setStatus("current")


class _SyslogDomainNameAppend_Type(Integer32):
    """Custom type syslogDomainNameAppend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("appendDomain", 1),
          ("disableDomain", 0))
    )


_SyslogDomainNameAppend_Type.__name__ = "Integer32"
_SyslogDomainNameAppend_Object = MibScalar
syslogDomainNameAppend = _SyslogDomainNameAppend_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 156),
    _SyslogDomainNameAppend_Type()
)
syslogDomainNameAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDomainNameAppend.setStatus("current")
_SyslogServerAddr_Type = DisplayString
_SyslogServerAddr_Object = MibScalar
syslogServerAddr = _SyslogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 157),
    _SyslogServerAddr_Type()
)
syslogServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerAddr.setStatus("current")
_SyslogServerPort_Type = Integer32
_SyslogServerPort_Object = MibScalar
syslogServerPort = _SyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 158),
    _SyslogServerPort_Type()
)
syslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerPort.setStatus("current")


class _SyslogMinLevel_Type(Integer32):
    """Custom type syslogMinLevel based on Integer32"""
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
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("error", 3),
          ("fatal", 0),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_SyslogMinLevel_Type.__name__ = "Integer32"
_SyslogMinLevel_Object = MibScalar
syslogMinLevel = _SyslogMinLevel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 159),
    _SyslogMinLevel_Type()
)
syslogMinLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMinLevel.setStatus("current")


class _Lan1DhcpRelease_Type(Integer32):
    """Custom type lan1DhcpRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("releaseIP", 1)
    )


_Lan1DhcpRelease_Type.__name__ = "Integer32"
_Lan1DhcpRelease_Object = MibScalar
lan1DhcpRelease = _Lan1DhcpRelease_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 201),
    _Lan1DhcpRelease_Type()
)
lan1DhcpRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1DhcpRelease.setStatus("current")


class _Lan1DhcpRenew_Type(Integer32):
    """Custom type lan1DhcpRenew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("renewIP", 1)
    )


_Lan1DhcpRenew_Type.__name__ = "Integer32"
_Lan1DhcpRenew_Object = MibScalar
lan1DhcpRenew = _Lan1DhcpRenew_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 202),
    _Lan1DhcpRenew_Type()
)
lan1DhcpRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1DhcpRenew.setStatus("current")


class _Lan3DhcpRelease_Type(Integer32):
    """Custom type lan3DhcpRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("releaseIP", 1)
    )


_Lan3DhcpRelease_Type.__name__ = "Integer32"
_Lan3DhcpRelease_Object = MibScalar
lan3DhcpRelease = _Lan3DhcpRelease_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 203),
    _Lan3DhcpRelease_Type()
)
lan3DhcpRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan3DhcpRelease.setStatus("current")


class _Lan3DhcpRenew_Type(Integer32):
    """Custom type lan3DhcpRenew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("renewIP", 1)
    )


_Lan3DhcpRenew_Type.__name__ = "Integer32"
_Lan3DhcpRenew_Object = MibScalar
lan3DhcpRenew = _Lan3DhcpRenew_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 204),
    _Lan3DhcpRenew_Type()
)
lan3DhcpRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan3DhcpRenew.setStatus("current")


class _NatDhcpRelease_Type(Integer32):
    """Custom type natDhcpRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("releaseIP", 1)
    )


_NatDhcpRelease_Type.__name__ = "Integer32"
_NatDhcpRelease_Object = MibScalar
natDhcpRelease = _NatDhcpRelease_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 205),
    _NatDhcpRelease_Type()
)
natDhcpRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natDhcpRelease.setStatus("current")


class _NatDhcpRenew_Type(Integer32):
    """Custom type natDhcpRenew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("renewIP", 1)
    )


_NatDhcpRenew_Type.__name__ = "Integer32"
_NatDhcpRenew_Object = MibScalar
natDhcpRenew = _NatDhcpRenew_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 206),
    _NatDhcpRenew_Type()
)
natDhcpRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natDhcpRenew.setStatus("current")


class _Region_Type(Integer32):
    """Custom type region based on Integer32"""
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
        *(("africa", 7),
          ("asia", 6),
          ("europe", 3),
          ("none", 0),
          ("northAmerica", 2),
          ("oceania", 5),
          ("otherRegulatory", 1),
          ("southAmerica", 4))
    )


_Region_Type.__name__ = "Integer32"
_Region_Object = MibScalar
region = _Region_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 207),
    _Region_Type()
)
region.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    region.setStatus("current")


class _RegionAsia_Type(Integer32):
    """Custom type regionAsia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("india", 2),
          ("indonesia", 3),
          ("none", 0),
          ("russiacategory1", 4),
          ("russiacategory2", 5),
          ("russiacategory3", 6),
          ("russiacategory4", 7),
          ("vietnam", 8))
    )


_RegionAsia_Type.__name__ = "Integer32"
_RegionAsia_Object = MibScalar
regionAsia = _RegionAsia_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 208),
    _RegionAsia_Type()
)
regionAsia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regionAsia.setStatus("current")


class _RegionEurope_Type(Integer32):
    """Custom type regionEurope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("denmark", 4),
          ("finland", 5),
          ("germany", 6),
          ("greece", 7),
          ("iceland", 8),
          ("ireland", 3),
          ("liechtenstein", 9),
          ("none", 0),
          ("norway", 10),
          ("portugal", 11),
          ("serbia", 13),
          ("spain", 2),
          ("switzerland", 12),
          ("unitedkingdom", 14))
    )


_RegionEurope_Type.__name__ = "Integer32"
_RegionEurope_Object = MibScalar
regionEurope = _RegionEurope_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 209),
    _RegionEurope_Type()
)
regionEurope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regionEurope.setStatus("current")


class _RegionNorthAmerica_Type(Integer32):
    """Custom type regionNorthAmerica based on Integer32"""
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
        *(("canada", 3),
          ("mexico", 4),
          ("none", 0),
          ("unitedStates", 2))
    )


_RegionNorthAmerica_Type.__name__ = "Integer32"
_RegionNorthAmerica_Object = MibScalar
regionNorthAmerica = _RegionNorthAmerica_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 210),
    _RegionNorthAmerica_Type()
)
regionNorthAmerica.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regionNorthAmerica.setStatus("current")


class _RegionOceania_Type(Integer32):
    """Custom type regionOceania based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("australia", 2),
          ("none", 0))
    )


_RegionOceania_Type.__name__ = "Integer32"
_RegionOceania_Object = MibScalar
regionOceania = _RegionOceania_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 211),
    _RegionOceania_Type()
)
regionOceania.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regionOceania.setStatus("current")


class _RegionSouthAmerica_Type(Integer32):
    """Custom type regionSouthAmerica based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("brazil", 2),
          ("none", 0))
    )


_RegionSouthAmerica_Type.__name__ = "Integer32"
_RegionSouthAmerica_Object = MibScalar
regionSouthAmerica = _RegionSouthAmerica_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 212),
    _RegionSouthAmerica_Type()
)
regionSouthAmerica.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regionSouthAmerica.setStatus("current")


class _RegionOtherRegulatory_Type(Integer32):
    """Custom type regionOtherRegulatory based on Integer32"""
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
        *(("none", 0),
          ("other", 1),
          ("otherETSI", 3),
          ("otherFCC", 2))
    )


_RegionOtherRegulatory_Type.__name__ = "Integer32"
_RegionOtherRegulatory_Object = MibScalar
regionOtherRegulatory = _RegionOtherRegulatory_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 213),
    _RegionOtherRegulatory_Type()
)
regionOtherRegulatory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regionOtherRegulatory.setStatus("current")


class _Interleave_Type(Integer32):
    """Custom type interleave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_Interleave_Type.__name__ = "Integer32"
_Interleave_Object = MibScalar
interleave = _Interleave_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 214),
    _Interleave_Type()
)
interleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interleave.setStatus("current")


class _ReceiveQualityDebug_Type(Integer32):
    """Custom type receiveQualityDebug based on Integer32"""
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


_ReceiveQualityDebug_Type.__name__ = "Integer32"
_ReceiveQualityDebug_Object = MibScalar
receiveQualityDebug = _ReceiveQualityDebug_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 215),
    _ReceiveQualityDebug_Type()
)
receiveQualityDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiveQualityDebug.setStatus("current")


class _ApType_Type(Integer32):
    """Custom type apType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remoteAP", 1),
          ("standardAP", 0))
    )


_ApType_Type.__name__ = "Integer32"
_ApType_Object = MibScalar
apType = _ApType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 216),
    _ApType_Type()
)
apType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apType.setStatus("current")


class _RegionAfrica_Type(Integer32):
    """Custom type regionAfrica based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("algeria", 2),
          ("none", 0))
    )


_RegionAfrica_Type.__name__ = "Integer32"
_RegionAfrica_Object = MibScalar
regionAfrica = _RegionAfrica_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 217),
    _RegionAfrica_Type()
)
regionAfrica.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regionAfrica.setStatus("current")
_AddCustomFreqMimo_Type = DisplayString
_AddCustomFreqMimo_Object = MibScalar
addCustomFreqMimo = _AddCustomFreqMimo_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 218),
    _AddCustomFreqMimo_Type()
)
addCustomFreqMimo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addCustomFreqMimo.setStatus("current")
_RemoveCustomFreqMimo_Type = DisplayString
_RemoveCustomFreqMimo_Object = MibScalar
removeCustomFreqMimo = _RemoveCustomFreqMimo_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 219),
    _RemoveCustomFreqMimo_Type()
)
removeCustomFreqMimo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    removeCustomFreqMimo.setStatus("current")


class _TimedSpectrumAnalysisDurationBox_Type(Integer32):
    """Custom type timedSpectrumAnalysisDurationBox based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TimedSpectrumAnalysisDurationBox_Type.__name__ = "Integer32"
_TimedSpectrumAnalysisDurationBox_Object = MibScalar
timedSpectrumAnalysisDurationBox = _TimedSpectrumAnalysisDurationBox_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 220),
    _TimedSpectrumAnalysisDurationBox_Type()
)
timedSpectrumAnalysisDurationBox.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timedSpectrumAnalysisDurationBox.setStatus("current")


class _SpectrumAnalysisActionBox_Type(Integer32):
    """Custom type spectrumAnalysisActionBox based on Integer32"""
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
        *(("idleCompleteSpectrumAnalysis", 4),
          ("idleNoSpectrumAnalysis", 3),
          ("inProgressContinuousSpectrumAnalysis", 6),
          ("inProgressTimedSpectrumAnalysis", 5),
          ("notReady", 7),
          ("startContinuousSpectrumAnalysis", 2),
          ("startTimedSpectrumAnalysis", 1),
          ("stopSpectrumAnalysis", 0))
    )


_SpectrumAnalysisActionBox_Type.__name__ = "Integer32"
_SpectrumAnalysisActionBox_Object = MibScalar
spectrumAnalysisActionBox = _SpectrumAnalysisActionBox_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 2, 221),
    _SpectrumAnalysisActionBox_Type()
)
spectrumAnalysisActionBox.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spectrumAnalysisActionBox.setStatus("current")
_WhispBoxControls_ObjectIdentity = ObjectIdentity
whispBoxControls = _WhispBoxControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 3)
)


class _SaveFlash_Type(Integer32):
    """Custom type saveFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNotSaveToFlash", 0),
          ("saveToFlash", 1))
    )


_SaveFlash_Type.__name__ = "Integer32"
_SaveFlash_Object = MibScalar
saveFlash = _SaveFlash_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 3, 1),
    _SaveFlash_Type()
)
saveFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveFlash.setStatus("obsolete")


class _Reboot_Type(Integer32):
    """Custom type reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("finishedReboot", 0),
          ("reboot", 1))
    )


_Reboot_Type.__name__ = "Integer32"
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 3, 2),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("current")


class _ClearEventLog_Type(Integer32):
    """Custom type clearEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("notClear", 0))
    )


_ClearEventLog_Type.__name__ = "Integer32"
_ClearEventLog_Object = MibScalar
clearEventLog = _ClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 3, 3),
    _ClearEventLog_Type()
)
clearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearEventLog.setStatus("current")


class _RebootIfRequired_Type(Integer32):
    """Custom type rebootIfRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rebootNotRequired", 0),
          ("rebootRequired", 1))
    )


_RebootIfRequired_Type.__name__ = "Integer32"
_RebootIfRequired_Object = MibScalar
rebootIfRequired = _RebootIfRequired_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 3, 4),
    _RebootIfRequired_Type()
)
rebootIfRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootIfRequired.setStatus("current")


class _ClearBERStats_Type(Integer32):
    """Custom type clearBERStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clearBERStats", 1),
          ("doNotClearBERStats", 0))
    )


_ClearBERStats_Type.__name__ = "Integer32"
_ClearBERStats_Object = MibScalar
clearBERStats = _ClearBERStats_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 3, 5),
    _ClearBERStats_Type()
)
clearBERStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearBERStats.setStatus("current")


class _UpdateDevice_Type(Integer32):
    """Custom type updateDevice based on Integer32"""
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


_UpdateDevice_Type.__name__ = "Integer32"
_UpdateDevice_Object = MibScalar
updateDevice = _UpdateDevice_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 3, 6),
    _UpdateDevice_Type()
)
updateDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    updateDevice.setStatus("current")
_WhispBoxBridgeTable_Object = MibTable
whispBoxBridgeTable = _WhispBoxBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 4)
)
if mibBuilder.loadTexts:
    whispBoxBridgeTable.setStatus("current")
_WhispBoxBridgeEntry_Object = MibTableRow
whispBoxBridgeEntry = _WhispBoxBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 4, 1)
)
whispBoxBridgeEntry.setIndexNames(
    (0, "WHISP-BOX-MIBV2-MIB", "whispBridgeMacAddr"),
)
if mibBuilder.loadTexts:
    whispBoxBridgeEntry.setStatus("current")
_WhispBridgeMacAddr_Type = MacAddress
_WhispBridgeMacAddr_Object = MibTableColumn
whispBridgeMacAddr = _WhispBridgeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 4, 1, 1),
    _WhispBridgeMacAddr_Type()
)
whispBridgeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBridgeMacAddr.setStatus("current")
_WhispBridgeDesLuid_Type = WhispLUID
_WhispBridgeDesLuid_Object = MibTableColumn
whispBridgeDesLuid = _WhispBridgeDesLuid_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 4, 1, 2),
    _WhispBridgeDesLuid_Type()
)
whispBridgeDesLuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBridgeDesLuid.setStatus("current")
_WhispBridgeAge_Type = Integer32
_WhispBridgeAge_Object = MibTableColumn
whispBridgeAge = _WhispBridgeAge_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 4, 1, 3),
    _WhispBridgeAge_Type()
)
whispBridgeAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBridgeAge.setStatus("current")
_WhispBridgeExt_Type = Integer32
_WhispBridgeExt_Object = MibTableColumn
whispBridgeExt = _WhispBridgeExt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 4, 1, 4),
    _WhispBridgeExt_Type()
)
whispBridgeExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBridgeExt.setStatus("current")
_WhispBridgeHash_Type = Integer32
_WhispBridgeHash_Object = MibTableColumn
whispBridgeHash = _WhispBridgeHash_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 4, 1, 5),
    _WhispBridgeHash_Type()
)
whispBridgeHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBridgeHash.setStatus("current")
_WhispBridgeCAM_Type = Integer32
_WhispBridgeCAM_Object = MibTableColumn
whispBridgeCAM = _WhispBridgeCAM_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 4, 1, 6),
    _WhispBridgeCAM_Type()
)
whispBridgeCAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBridgeCAM.setStatus("obsolete")
_WhispBoxEventLog_ObjectIdentity = ObjectIdentity
whispBoxEventLog = _WhispBoxEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 5)
)
_WhispBoxEvntLog_Type = EventString
_WhispBoxEvntLog_Object = MibScalar
whispBoxEvntLog = _WhispBoxEvntLog_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 5, 1),
    _WhispBoxEvntLog_Type()
)
whispBoxEvntLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBoxEvntLog.setStatus("current")
_WhispBoxConf_ObjectIdentity = ObjectIdentity
whispBoxConf = _WhispBoxConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 6)
)
_WhispBoxGroups_ObjectIdentity = ObjectIdentity
whispBoxGroups = _WhispBoxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 6, 1)
)
_WhispBoxBridgeVar_ObjectIdentity = ObjectIdentity
whispBoxBridgeVar = _WhispBoxBridgeVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 7)
)
_WhispBridgeTbUsed_Type = Integer32
_WhispBridgeTbUsed_Object = MibScalar
whispBridgeTbUsed = _WhispBridgeTbUsed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 7, 1),
    _WhispBridgeTbUsed_Type()
)
whispBridgeTbUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBridgeTbUsed.setStatus("current")
_WhispBridgeTbFree_Type = Integer32
_WhispBridgeTbFree_Object = MibScalar
whispBridgeTbFree = _WhispBridgeTbFree_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 7, 2),
    _WhispBridgeTbFree_Type()
)
whispBridgeTbFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBridgeTbFree.setStatus("current")
_WhispBridgeTbErr_Type = Integer32
_WhispBridgeTbErr_Object = MibScalar
whispBridgeTbErr = _WhispBridgeTbErr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 7, 3),
    _WhispBridgeTbErr_Type()
)
whispBridgeTbErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispBridgeTbErr.setStatus("current")
_WhispVLANTable_Object = MibTable
whispVLANTable = _WhispVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 8)
)
if mibBuilder.loadTexts:
    whispVLANTable.setStatus("current")
_WhispVLANEntry_Object = MibTableRow
whispVLANEntry = _WhispVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 8, 1)
)
whispVLANEntry.setIndexNames(
    (0, "WHISP-BOX-MIBV2-MIB", "whispVID"),
)
if mibBuilder.loadTexts:
    whispVLANEntry.setStatus("current")


class _WhispVID_Type(Integer32):
    """Custom type whispVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WhispVID_Type.__name__ = "Integer32"
_WhispVID_Object = MibTableColumn
whispVID = _WhispVID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 8, 1, 1),
    _WhispVID_Type()
)
whispVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispVID.setStatus("current")
_WhispVType_Type = DisplayString
_WhispVType_Object = MibTableColumn
whispVType = _WhispVType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 8, 1, 2),
    _WhispVType_Type()
)
whispVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispVType.setStatus("current")
_WhispVAge_Type = Integer32
_WhispVAge_Object = MibTableColumn
whispVAge = _WhispVAge_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 8, 1, 3),
    _WhispVAge_Type()
)
whispVAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispVAge.setStatus("current")
_WhispBoxCPVar_ObjectIdentity = ObjectIdentity
whispBoxCPVar = _WhispBoxCPVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9)
)
_CodePoint0_Type = Integer32
_CodePoint0_Object = MibScalar
codePoint0 = _CodePoint0_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 1),
    _CodePoint0_Type()
)
codePoint0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codePoint0.setStatus("current")
_CodePoint1_Type = Integer32
_CodePoint1_Object = MibScalar
codePoint1 = _CodePoint1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 2),
    _CodePoint1_Type()
)
codePoint1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint1.setStatus("current")
_CodePoint2_Type = Integer32
_CodePoint2_Object = MibScalar
codePoint2 = _CodePoint2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 3),
    _CodePoint2_Type()
)
codePoint2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint2.setStatus("current")
_CodePoint3_Type = Integer32
_CodePoint3_Object = MibScalar
codePoint3 = _CodePoint3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 4),
    _CodePoint3_Type()
)
codePoint3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint3.setStatus("current")
_CodePoint4_Type = Integer32
_CodePoint4_Object = MibScalar
codePoint4 = _CodePoint4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 5),
    _CodePoint4_Type()
)
codePoint4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint4.setStatus("current")
_CodePoint5_Type = Integer32
_CodePoint5_Object = MibScalar
codePoint5 = _CodePoint5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 6),
    _CodePoint5_Type()
)
codePoint5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint5.setStatus("current")
_CodePoint6_Type = Integer32
_CodePoint6_Object = MibScalar
codePoint6 = _CodePoint6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 7),
    _CodePoint6_Type()
)
codePoint6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint6.setStatus("current")
_CodePoint7_Type = Integer32
_CodePoint7_Object = MibScalar
codePoint7 = _CodePoint7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 8),
    _CodePoint7_Type()
)
codePoint7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint7.setStatus("current")
_CodePoint8_Type = Integer32
_CodePoint8_Object = MibScalar
codePoint8 = _CodePoint8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 9),
    _CodePoint8_Type()
)
codePoint8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint8.setStatus("current")
_CodePoint9_Type = Integer32
_CodePoint9_Object = MibScalar
codePoint9 = _CodePoint9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 10),
    _CodePoint9_Type()
)
codePoint9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint9.setStatus("current")
_CodePoint10_Type = Integer32
_CodePoint10_Object = MibScalar
codePoint10 = _CodePoint10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 11),
    _CodePoint10_Type()
)
codePoint10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint10.setStatus("current")
_CodePoint11_Type = Integer32
_CodePoint11_Object = MibScalar
codePoint11 = _CodePoint11_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 12),
    _CodePoint11_Type()
)
codePoint11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint11.setStatus("current")
_CodePoint12_Type = Integer32
_CodePoint12_Object = MibScalar
codePoint12 = _CodePoint12_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 13),
    _CodePoint12_Type()
)
codePoint12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint12.setStatus("current")
_CodePoint13_Type = Integer32
_CodePoint13_Object = MibScalar
codePoint13 = _CodePoint13_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 14),
    _CodePoint13_Type()
)
codePoint13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint13.setStatus("current")
_CodePoint14_Type = Integer32
_CodePoint14_Object = MibScalar
codePoint14 = _CodePoint14_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 15),
    _CodePoint14_Type()
)
codePoint14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint14.setStatus("current")
_CodePoint15_Type = Integer32
_CodePoint15_Object = MibScalar
codePoint15 = _CodePoint15_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 16),
    _CodePoint15_Type()
)
codePoint15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint15.setStatus("current")
_CodePoint16_Type = Integer32
_CodePoint16_Object = MibScalar
codePoint16 = _CodePoint16_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 17),
    _CodePoint16_Type()
)
codePoint16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint16.setStatus("current")
_CodePoint17_Type = Integer32
_CodePoint17_Object = MibScalar
codePoint17 = _CodePoint17_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 18),
    _CodePoint17_Type()
)
codePoint17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint17.setStatus("current")
_CodePoint18_Type = Integer32
_CodePoint18_Object = MibScalar
codePoint18 = _CodePoint18_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 19),
    _CodePoint18_Type()
)
codePoint18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint18.setStatus("current")
_CodePoint19_Type = Integer32
_CodePoint19_Object = MibScalar
codePoint19 = _CodePoint19_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 20),
    _CodePoint19_Type()
)
codePoint19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint19.setStatus("current")
_CodePoint20_Type = Integer32
_CodePoint20_Object = MibScalar
codePoint20 = _CodePoint20_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 21),
    _CodePoint20_Type()
)
codePoint20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint20.setStatus("current")
_CodePoint21_Type = Integer32
_CodePoint21_Object = MibScalar
codePoint21 = _CodePoint21_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 22),
    _CodePoint21_Type()
)
codePoint21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint21.setStatus("current")
_CodePoint22_Type = Integer32
_CodePoint22_Object = MibScalar
codePoint22 = _CodePoint22_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 23),
    _CodePoint22_Type()
)
codePoint22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint22.setStatus("current")
_CodePoint23_Type = Integer32
_CodePoint23_Object = MibScalar
codePoint23 = _CodePoint23_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 24),
    _CodePoint23_Type()
)
codePoint23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint23.setStatus("current")
_CodePoint24_Type = Integer32
_CodePoint24_Object = MibScalar
codePoint24 = _CodePoint24_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 25),
    _CodePoint24_Type()
)
codePoint24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint24.setStatus("current")
_CodePoint25_Type = Integer32
_CodePoint25_Object = MibScalar
codePoint25 = _CodePoint25_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 26),
    _CodePoint25_Type()
)
codePoint25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint25.setStatus("current")
_CodePoint26_Type = Integer32
_CodePoint26_Object = MibScalar
codePoint26 = _CodePoint26_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 27),
    _CodePoint26_Type()
)
codePoint26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint26.setStatus("current")
_CodePoint27_Type = Integer32
_CodePoint27_Object = MibScalar
codePoint27 = _CodePoint27_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 28),
    _CodePoint27_Type()
)
codePoint27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint27.setStatus("current")
_CodePoint28_Type = Integer32
_CodePoint28_Object = MibScalar
codePoint28 = _CodePoint28_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 29),
    _CodePoint28_Type()
)
codePoint28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint28.setStatus("current")
_CodePoint29_Type = Integer32
_CodePoint29_Object = MibScalar
codePoint29 = _CodePoint29_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 30),
    _CodePoint29_Type()
)
codePoint29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint29.setStatus("current")
_CodePoint30_Type = Integer32
_CodePoint30_Object = MibScalar
codePoint30 = _CodePoint30_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 31),
    _CodePoint30_Type()
)
codePoint30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint30.setStatus("current")
_CodePoint31_Type = Integer32
_CodePoint31_Object = MibScalar
codePoint31 = _CodePoint31_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 32),
    _CodePoint31_Type()
)
codePoint31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint31.setStatus("current")
_CodePoint32_Type = Integer32
_CodePoint32_Object = MibScalar
codePoint32 = _CodePoint32_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 33),
    _CodePoint32_Type()
)
codePoint32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint32.setStatus("current")
_CodePoint33_Type = Integer32
_CodePoint33_Object = MibScalar
codePoint33 = _CodePoint33_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 34),
    _CodePoint33_Type()
)
codePoint33.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint33.setStatus("current")
_CodePoint34_Type = Integer32
_CodePoint34_Object = MibScalar
codePoint34 = _CodePoint34_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 35),
    _CodePoint34_Type()
)
codePoint34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint34.setStatus("current")
_CodePoint35_Type = Integer32
_CodePoint35_Object = MibScalar
codePoint35 = _CodePoint35_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 36),
    _CodePoint35_Type()
)
codePoint35.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint35.setStatus("current")
_CodePoint36_Type = Integer32
_CodePoint36_Object = MibScalar
codePoint36 = _CodePoint36_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 37),
    _CodePoint36_Type()
)
codePoint36.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint36.setStatus("current")
_CodePoint37_Type = Integer32
_CodePoint37_Object = MibScalar
codePoint37 = _CodePoint37_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 38),
    _CodePoint37_Type()
)
codePoint37.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint37.setStatus("current")
_CodePoint38_Type = Integer32
_CodePoint38_Object = MibScalar
codePoint38 = _CodePoint38_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 39),
    _CodePoint38_Type()
)
codePoint38.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint38.setStatus("current")
_CodePoint39_Type = Integer32
_CodePoint39_Object = MibScalar
codePoint39 = _CodePoint39_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 40),
    _CodePoint39_Type()
)
codePoint39.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint39.setStatus("current")
_CodePoint40_Type = Integer32
_CodePoint40_Object = MibScalar
codePoint40 = _CodePoint40_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 41),
    _CodePoint40_Type()
)
codePoint40.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint40.setStatus("current")
_CodePoint41_Type = Integer32
_CodePoint41_Object = MibScalar
codePoint41 = _CodePoint41_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 42),
    _CodePoint41_Type()
)
codePoint41.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint41.setStatus("current")
_CodePoint42_Type = Integer32
_CodePoint42_Object = MibScalar
codePoint42 = _CodePoint42_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 43),
    _CodePoint42_Type()
)
codePoint42.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint42.setStatus("current")
_CodePoint43_Type = Integer32
_CodePoint43_Object = MibScalar
codePoint43 = _CodePoint43_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 44),
    _CodePoint43_Type()
)
codePoint43.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint43.setStatus("current")
_CodePoint44_Type = Integer32
_CodePoint44_Object = MibScalar
codePoint44 = _CodePoint44_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 45),
    _CodePoint44_Type()
)
codePoint44.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint44.setStatus("current")
_CodePoint45_Type = Integer32
_CodePoint45_Object = MibScalar
codePoint45 = _CodePoint45_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 46),
    _CodePoint45_Type()
)
codePoint45.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint45.setStatus("current")
_CodePoint46_Type = Integer32
_CodePoint46_Object = MibScalar
codePoint46 = _CodePoint46_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 47),
    _CodePoint46_Type()
)
codePoint46.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint46.setStatus("current")
_CodePoint47_Type = Integer32
_CodePoint47_Object = MibScalar
codePoint47 = _CodePoint47_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 48),
    _CodePoint47_Type()
)
codePoint47.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint47.setStatus("current")
_CodePoint48_Type = Integer32
_CodePoint48_Object = MibScalar
codePoint48 = _CodePoint48_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 49),
    _CodePoint48_Type()
)
codePoint48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codePoint48.setStatus("current")
_CodePoint49_Type = Integer32
_CodePoint49_Object = MibScalar
codePoint49 = _CodePoint49_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 50),
    _CodePoint49_Type()
)
codePoint49.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint49.setStatus("current")
_CodePoint50_Type = Integer32
_CodePoint50_Object = MibScalar
codePoint50 = _CodePoint50_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 51),
    _CodePoint50_Type()
)
codePoint50.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint50.setStatus("current")
_CodePoint51_Type = Integer32
_CodePoint51_Object = MibScalar
codePoint51 = _CodePoint51_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 52),
    _CodePoint51_Type()
)
codePoint51.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint51.setStatus("current")
_CodePoint52_Type = Integer32
_CodePoint52_Object = MibScalar
codePoint52 = _CodePoint52_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 53),
    _CodePoint52_Type()
)
codePoint52.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint52.setStatus("current")
_CodePoint53_Type = Integer32
_CodePoint53_Object = MibScalar
codePoint53 = _CodePoint53_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 54),
    _CodePoint53_Type()
)
codePoint53.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint53.setStatus("current")
_CodePoint54_Type = Integer32
_CodePoint54_Object = MibScalar
codePoint54 = _CodePoint54_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 55),
    _CodePoint54_Type()
)
codePoint54.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint54.setStatus("current")
_CodePoint55_Type = Integer32
_CodePoint55_Object = MibScalar
codePoint55 = _CodePoint55_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 56),
    _CodePoint55_Type()
)
codePoint55.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint55.setStatus("current")
_CodePoint56_Type = Integer32
_CodePoint56_Object = MibScalar
codePoint56 = _CodePoint56_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 57),
    _CodePoint56_Type()
)
codePoint56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codePoint56.setStatus("current")
_CodePoint57_Type = Integer32
_CodePoint57_Object = MibScalar
codePoint57 = _CodePoint57_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 58),
    _CodePoint57_Type()
)
codePoint57.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint57.setStatus("current")
_CodePoint58_Type = Integer32
_CodePoint58_Object = MibScalar
codePoint58 = _CodePoint58_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 59),
    _CodePoint58_Type()
)
codePoint58.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint58.setStatus("current")
_CodePoint59_Type = Integer32
_CodePoint59_Object = MibScalar
codePoint59 = _CodePoint59_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 60),
    _CodePoint59_Type()
)
codePoint59.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint59.setStatus("current")
_CodePoint60_Type = Integer32
_CodePoint60_Object = MibScalar
codePoint60 = _CodePoint60_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 61),
    _CodePoint60_Type()
)
codePoint60.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint60.setStatus("current")
_CodePoint61_Type = Integer32
_CodePoint61_Object = MibScalar
codePoint61 = _CodePoint61_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 62),
    _CodePoint61_Type()
)
codePoint61.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint61.setStatus("current")
_CodePoint62_Type = Integer32
_CodePoint62_Object = MibScalar
codePoint62 = _CodePoint62_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 63),
    _CodePoint62_Type()
)
codePoint62.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint62.setStatus("current")
_CodePoint63_Type = Integer32
_CodePoint63_Object = MibScalar
codePoint63 = _CodePoint63_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 9, 64),
    _CodePoint63_Type()
)
codePoint63.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codePoint63.setStatus("current")
_WhispUserTable_Object = MibTable
whispUserTable = _WhispUserTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 10)
)
if mibBuilder.loadTexts:
    whispUserTable.setStatus("current")
_WhispUserEntry_Object = MibTableRow
whispUserEntry = _WhispUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 10, 1)
)
whispUserEntry.setIndexNames(
    (0, "WHISP-BOX-MIBV2-MIB", "entryIndex"),
)
if mibBuilder.loadTexts:
    whispUserEntry.setStatus("current")


class _EntryIndex_Type(Integer32):
    """Custom type entryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_EntryIndex_Type.__name__ = "Integer32"
_EntryIndex_Object = MibTableColumn
entryIndex = _EntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 10, 1, 1),
    _EntryIndex_Type()
)
entryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entryIndex.setStatus("current")
_UserLoginName_Type = DisplayString
_UserLoginName_Object = MibTableColumn
userLoginName = _UserLoginName_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 10, 1, 2),
    _UserLoginName_Type()
)
userLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userLoginName.setStatus("current")
_UserPswd_Type = DisplayString
_UserPswd_Object = MibTableColumn
userPswd = _UserPswd_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 10, 1, 3),
    _UserPswd_Type()
)
userPswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPswd.setStatus("current")
_AccessLevel_Type = Integer32
_AccessLevel_Object = MibTableColumn
accessLevel = _AccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 10, 1, 4),
    _AccessLevel_Type()
)
accessLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessLevel.setStatus("current")
_LoginStatus_Type = Integer32
_LoginStatus_Object = MibTableColumn
loginStatus = _LoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 10, 1, 5),
    _LoginStatus_Type()
)
loginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatus.setStatus("current")
_LoginMethod_Type = Integer32
_LoginMethod_Object = MibTableColumn
loginMethod = _LoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 10, 1, 6),
    _LoginMethod_Type()
)
loginMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginMethod.setStatus("current")
_SessionTime_Type = Integer32
_SessionTime_Object = MibTableColumn
sessionTime = _SessionTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 10, 1, 7),
    _SessionTime_Type()
)
sessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionTime.setStatus("current")
_WhispLayer2NeighborTable_Object = MibTable
whispLayer2NeighborTable = _WhispLayer2NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 11)
)
if mibBuilder.loadTexts:
    whispLayer2NeighborTable.setStatus("current")
_WhispLayer2NeighborEntry_Object = MibTableRow
whispLayer2NeighborEntry = _WhispLayer2NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 11, 1)
)
whispLayer2NeighborEntry.setIndexNames(
    (0, "WHISP-BOX-MIBV2-MIB", "entryL2Index"),
)
if mibBuilder.loadTexts:
    whispLayer2NeighborEntry.setStatus("current")


class _EntryL2Index_Type(Integer32):
    """Custom type entryL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_EntryL2Index_Type.__name__ = "Integer32"
_EntryL2Index_Object = MibTableColumn
entryL2Index = _EntryL2Index_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 11, 1, 1),
    _EntryL2Index_Type()
)
entryL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entryL2Index.setStatus("current")
_NeighborMAC_Type = DisplayString
_NeighborMAC_Object = MibTableColumn
neighborMAC = _NeighborMAC_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 11, 1, 2),
    _NeighborMAC_Type()
)
neighborMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborMAC.setStatus("current")
_NeighborIP_Type = DisplayString
_NeighborIP_Object = MibTableColumn
neighborIP = _NeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 11, 1, 3),
    _NeighborIP_Type()
)
neighborIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborIP.setStatus("current")
_NeighborSiteName_Type = DisplayString
_NeighborSiteName_Object = MibTableColumn
neighborSiteName = _NeighborSiteName_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 11, 1, 4),
    _NeighborSiteName_Type()
)
neighborSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborSiteName.setStatus("current")
_WhispBoxEvent_ObjectIdentity = ObjectIdentity
whispBoxEvent = _WhispBoxEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 12)
)
_WhispBoxDHCPClientEvent_ObjectIdentity = ObjectIdentity
whispBoxDHCPClientEvent = _WhispBoxDHCPClientEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 12, 1)
)
_WhispBoxDNS_ObjectIdentity = ObjectIdentity
whispBoxDNS = _WhispBoxDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13)
)


class _DnsIpState_Type(Integer32):
    """Custom type dnsIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 0))
    )


_DnsIpState_Type.__name__ = "Integer32"
_DnsIpState_Object = MibScalar
dnsIpState = _DnsIpState_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 1),
    _DnsIpState_Type()
)
dnsIpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsIpState.setStatus("current")
_DnsPrimaryMgmtIP_Type = IpAddress
_DnsPrimaryMgmtIP_Object = MibScalar
dnsPrimaryMgmtIP = _DnsPrimaryMgmtIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 2),
    _DnsPrimaryMgmtIP_Type()
)
dnsPrimaryMgmtIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsPrimaryMgmtIP.setStatus("current")
_DnsAlternateMgmtIP_Type = IpAddress
_DnsAlternateMgmtIP_Object = MibScalar
dnsAlternateMgmtIP = _DnsAlternateMgmtIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 3),
    _DnsAlternateMgmtIP_Type()
)
dnsAlternateMgmtIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsAlternateMgmtIP.setStatus("current")
_DnsMgmtDomainName_Type = DisplayString
_DnsMgmtDomainName_Object = MibScalar
dnsMgmtDomainName = _DnsMgmtDomainName_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 4),
    _DnsMgmtDomainName_Type()
)
dnsMgmtDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsMgmtDomainName.setStatus("current")


class _TrapDomainNameAppend_Type(Integer32):
    """Custom type trapDomainNameAppend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("appendDomain", 1),
          ("disableDomain", 0))
    )


_TrapDomainNameAppend_Type.__name__ = "Integer32"
_TrapDomainNameAppend_Object = MibScalar
trapDomainNameAppend = _TrapDomainNameAppend_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 5),
    _TrapDomainNameAppend_Type()
)
trapDomainNameAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDomainNameAppend.setStatus("current")
_Trap1_Type = DisplayString
_Trap1_Object = MibScalar
trap1 = _Trap1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 6),
    _Trap1_Type()
)
trap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap1.setStatus("current")
_Trap2_Type = DisplayString
_Trap2_Object = MibScalar
trap2 = _Trap2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 7),
    _Trap2_Type()
)
trap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap2.setStatus("current")
_Trap3_Type = DisplayString
_Trap3_Object = MibScalar
trap3 = _Trap3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 8),
    _Trap3_Type()
)
trap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap3.setStatus("current")
_Trap4_Type = DisplayString
_Trap4_Object = MibScalar
trap4 = _Trap4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 9),
    _Trap4_Type()
)
trap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap4.setStatus("current")
_Trap5_Type = DisplayString
_Trap5_Object = MibScalar
trap5 = _Trap5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 10),
    _Trap5_Type()
)
trap5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap5.setStatus("current")
_Trap6_Type = DisplayString
_Trap6_Object = MibScalar
trap6 = _Trap6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 11),
    _Trap6_Type()
)
trap6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap6.setStatus("current")
_Trap7_Type = DisplayString
_Trap7_Object = MibScalar
trap7 = _Trap7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 12),
    _Trap7_Type()
)
trap7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap7.setStatus("current")
_Trap8_Type = DisplayString
_Trap8_Object = MibScalar
trap8 = _Trap8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 13),
    _Trap8_Type()
)
trap8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap8.setStatus("current")
_Trap9_Type = DisplayString
_Trap9_Object = MibScalar
trap9 = _Trap9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 14),
    _Trap9_Type()
)
trap9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap9.setStatus("current")
_Trap10_Type = DisplayString
_Trap10_Object = MibScalar
trap10 = _Trap10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 13, 15),
    _Trap10_Type()
)
trap10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap10.setStatus("current")
_WhispBoxRFPhysical_ObjectIdentity = ObjectIdentity
whispBoxRFPhysical = _WhispBoxRFPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15)
)
_WhispBoxRFPhysicalRadios_Object = MibTable
whispBoxRFPhysicalRadios = _WhispBoxRFPhysicalRadios_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15, 1)
)
if mibBuilder.loadTexts:
    whispBoxRFPhysicalRadios.setStatus("current")
_WhispBoxRFPhysicalRadioEntry_Object = MibTableRow
whispBoxRFPhysicalRadioEntry = _WhispBoxRFPhysicalRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15, 1, 1)
)
whispBoxRFPhysicalRadioEntry.setIndexNames(
    (0, "WHISP-BOX-MIBV2-MIB", "radioIndex"),
)
if mibBuilder.loadTexts:
    whispBoxRFPhysicalRadioEntry.setStatus("current")


class _RadioIndex_Type(Integer32):
    """Custom type radioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RadioIndex_Type.__name__ = "Integer32"
_RadioIndex_Object = MibTableColumn
radioIndex = _RadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15, 1, 1, 1),
    _RadioIndex_Type()
)
radioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioIndex.setStatus("current")


class _RadioType_Type(Integer32):
    """Custom type radioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fsk", 0),
          ("ofdm", 1))
    )


_RadioType_Type.__name__ = "Integer32"
_RadioType_Object = MibTableColumn
radioType = _RadioType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15, 1, 1, 2),
    _RadioType_Type()
)
radioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioType.setStatus("current")


class _RadioPaths_Type(Integer32):
    """Custom type radioPaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RadioPaths_Type.__name__ = "Integer32"
_RadioPaths_Object = MibTableColumn
radioPaths = _RadioPaths_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15, 1, 1, 3),
    _RadioPaths_Type()
)
radioPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioPaths.setStatus("current")
_WhispBoxRFPhysicalRadioPaths_Object = MibTable
whispBoxRFPhysicalRadioPaths = _WhispBoxRFPhysicalRadioPaths_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15, 2)
)
if mibBuilder.loadTexts:
    whispBoxRFPhysicalRadioPaths.setStatus("current")
_WhispBoxRFPhysicalRadioPathEntry_Object = MibTableRow
whispBoxRFPhysicalRadioPathEntry = _WhispBoxRFPhysicalRadioPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15, 2, 1)
)
whispBoxRFPhysicalRadioPathEntry.setIndexNames(
    (0, "WHISP-BOX-MIBV2-MIB", "radioIndex"),
    (0, "WHISP-BOX-MIBV2-MIB", "pathIndex"),
)
if mibBuilder.loadTexts:
    whispBoxRFPhysicalRadioPathEntry.setStatus("current")


class _PathIndex_Type(Integer32):
    """Custom type pathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PathIndex_Type.__name__ = "Integer32"
_PathIndex_Object = MibTableColumn
pathIndex = _PathIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15, 2, 1, 1),
    _PathIndex_Type()
)
pathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathIndex.setStatus("current")
_WhispBoxRFPhysicalRadioFrequencies_Object = MibTable
whispBoxRFPhysicalRadioFrequencies = _WhispBoxRFPhysicalRadioFrequencies_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15, 3)
)
if mibBuilder.loadTexts:
    whispBoxRFPhysicalRadioFrequencies.setStatus("current")
_WhispBoxRFPhysicalRadioFrequencyEntry_Object = MibTableRow
whispBoxRFPhysicalRadioFrequencyEntry = _WhispBoxRFPhysicalRadioFrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15, 3, 1)
)
whispBoxRFPhysicalRadioFrequencyEntry.setIndexNames(
    (0, "WHISP-BOX-MIBV2-MIB", "radioIndex"),
    (0, "WHISP-BOX-MIBV2-MIB", "frequency"),
)
if mibBuilder.loadTexts:
    whispBoxRFPhysicalRadioFrequencyEntry.setStatus("current")


class _Frequency_Type(Integer32):
    """Custom type frequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900000),
    )


_Frequency_Type.__name__ = "Integer32"
_Frequency_Object = MibTableColumn
frequency = _Frequency_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 15, 3, 1, 1),
    _Frequency_Type()
)
frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequency.setStatus("current")
_WhispBoxRFConfig_ObjectIdentity = ObjectIdentity
whispBoxRFConfig = _WhispBoxRFConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 16)
)
_WhispBoxRFConfigRadios_Object = MibTable
whispBoxRFConfigRadios = _WhispBoxRFConfigRadios_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 16, 1)
)
if mibBuilder.loadTexts:
    whispBoxRFConfigRadios.setStatus("current")
_WhispBoxRFConfigRadioEntry_Object = MibTableRow
whispBoxRFConfigRadioEntry = _WhispBoxRFConfigRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 16, 1, 1)
)
whispBoxRFConfigRadioEntry.setIndexNames(
    (0, "WHISP-BOX-MIBV2-MIB", "radioConfigIndex"),
)
if mibBuilder.loadTexts:
    whispBoxRFConfigRadioEntry.setStatus("current")


class _RadioConfigIndex_Type(Integer32):
    """Custom type radioConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RadioConfigIndex_Type.__name__ = "Integer32"
_RadioConfigIndex_Object = MibTableColumn
radioConfigIndex = _RadioConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 16, 1, 1, 1),
    _RadioConfigIndex_Type()
)
radioConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioConfigIndex.setStatus("current")


class _RadioFrequencyBand_Type(Integer32):
    """Custom type radioFrequencyBand based on Integer32"""
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
        *(("band2400", 2),
          ("band3500", 3),
          ("band3700", 4),
          ("band4900", 5),
          ("band5100", 6),
          ("band5200", 7),
          ("band5400", 8),
          ("band5700", 9),
          ("band5800", 10),
          ("band5900", 11),
          ("band6050", 12),
          ("band700", 0),
          ("band900", 1))
    )


_RadioFrequencyBand_Type.__name__ = "Integer32"
_RadioFrequencyBand_Object = MibTableColumn
radioFrequencyBand = _RadioFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 16, 1, 1, 2),
    _RadioFrequencyBand_Type()
)
radioFrequencyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioFrequencyBand.setStatus("current")

# Managed Objects groups

whispBoxAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 6, 1, 1)
)
whispBoxAttributesGroup.setObjects(
      *(("WHISP-BOX-MIBV2-MIB", "vlanAcceptQinQFrames"),
        ("WHISP-BOX-MIBV2-MIB", "providerVID"),
        ("WHISP-BOX-MIBV2-MIB", "mac1VIDMapAddr"),
        ("WHISP-BOX-MIBV2-MIB", "mac1VIDMapVid"),
        ("WHISP-BOX-MIBV2-MIB", "mac2VIDMapAddr"),
        ("WHISP-BOX-MIBV2-MIB", "mac2VIDMapVid"),
        ("WHISP-BOX-MIBV2-MIB", "mac3VIDMapAddr"),
        ("WHISP-BOX-MIBV2-MIB", "mac3VIDMapVid"),
        ("WHISP-BOX-MIBV2-MIB", "mac4VIDMapAddr"),
        ("WHISP-BOX-MIBV2-MIB", "mac4VIDMapVid"),
        ("WHISP-BOX-MIBV2-MIB", "mac5VIDMapAddr"),
        ("WHISP-BOX-MIBV2-MIB", "mac5VIDMapVid"),
        ("WHISP-BOX-MIBV2-MIB", "mac6VIDMapAddr"),
        ("WHISP-BOX-MIBV2-MIB", "mac6VIDMapVid"),
        ("WHISP-BOX-MIBV2-MIB", "mac7VIDMapAddr"),
        ("WHISP-BOX-MIBV2-MIB", "mac7VIDMapVid"),
        ("WHISP-BOX-MIBV2-MIB", "mac8VIDMapAddr"),
        ("WHISP-BOX-MIBV2-MIB", "mac8VIDMapVid"),
        ("WHISP-BOX-MIBV2-MIB", "mac9VIDMapAddr"),
        ("WHISP-BOX-MIBV2-MIB", "mac9VIDMapVid"),
        ("WHISP-BOX-MIBV2-MIB", "mac10VIDMapAddr"),
        ("WHISP-BOX-MIBV2-MIB", "mac10VIDMapVid"),
        ("WHISP-BOX-MIBV2-MIB", "vlanPortType"),
        ("WHISP-BOX-MIBV2-MIB", "portVID"),
        ("WHISP-BOX-MIBV2-MIB", "timedSpectrumAnalysisDurationBox"),
        ("WHISP-BOX-MIBV2-MIB", "spectrumAnalysisActionBox"),
        ("WHISP-BOX-MIBV2-MIB", "calibrationStatusBox"),
        ("WHISP-BOX-MIBV2-MIB", "calibrationStatusBool"),
        ("WHISP-BOX-MIBV2-MIB", "agcGainRxCH1"),
        ("WHISP-BOX-MIBV2-MIB", "agcGainRxCH2"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxSoftwareVer"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxFPGAVer"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxBoot"),
        ("WHISP-BOX-MIBV2-MIB", "boxTemperature"),
        ("WHISP-BOX-MIBV2-MIB", "boxDeviceType"),
        ("WHISP-BOX-MIBV2-MIB", "boxDeviceTypeID"),
        ("WHISP-BOX-MIBV2-MIB", "boxEncryption"),
        ("WHISP-BOX-MIBV2-MIB", "etherLinkStatus"),
        ("WHISP-BOX-MIBV2-MIB", "boxFrequency"),
        ("WHISP-BOX-MIBV2-MIB", "platformVer"),
        ("WHISP-BOX-MIBV2-MIB", "platformType"),
        ("WHISP-BOX-MIBV2-MIB", "dhcpLanIp"),
        ("WHISP-BOX-MIBV2-MIB", "dhcpLanSubnetMask"),
        ("WHISP-BOX-MIBV2-MIB", "dhcpLanGateway"),
        ("WHISP-BOX-MIBV2-MIB", "dhcpRfPublicIp"),
        ("WHISP-BOX-MIBV2-MIB", "dhcpRfPublicSubnetMask"),
        ("WHISP-BOX-MIBV2-MIB", "dhcpRfPublicGateway"),
        ("WHISP-BOX-MIBV2-MIB", "lanDhcpStatus"),
        ("WHISP-BOX-MIBV2-MIB", "rfPublicDhcpStatus"),
        ("WHISP-BOX-MIBV2-MIB", "natDhcpStatus"),
        ("WHISP-BOX-MIBV2-MIB", "inSyncCount"),
        ("WHISP-BOX-MIBV2-MIB", "outSyncCount"),
        ("WHISP-BOX-MIBV2-MIB", "pllOutLockCount"),
        ("WHISP-BOX-MIBV2-MIB", "txCalFailure"),
        ("WHISP-BOX-MIBV2-MIB", "swVersion"),
        ("WHISP-BOX-MIBV2-MIB", "pldVersion"),
        ("WHISP-BOX-MIBV2-MIB", "platformInfo"),
        ("WHISP-BOX-MIBV2-MIB", "antType"),
        ("WHISP-BOX-MIBV2-MIB", "antPolarization"),
        ("WHISP-BOX-MIBV2-MIB", "packetOverloadCounter"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxP11Personality"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxP11FPGAType"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxP11BstrapFPGAVer"),
        ("WHISP-BOX-MIBV2-MIB", "numDFSDetections"),
        ("WHISP-BOX-MIBV2-MIB", "rxOverrunPkts"),
        ("WHISP-BOX-MIBV2-MIB", "boxTemperatureC"),
        ("WHISP-BOX-MIBV2-MIB", "boxTemperatureF"),
        ("WHISP-BOX-MIBV2-MIB", "linkNegoSpeed"),
        ("WHISP-BOX-MIBV2-MIB", "installationColorCode"),
        ("WHISP-BOX-MIBV2-MIB", "colorCode"),
        ("WHISP-BOX-MIBV2-MIB", "displayOnlyAccess"),
        ("WHISP-BOX-MIBV2-MIB", "fullAccess"),
        ("WHISP-BOX-MIBV2-MIB", "webAutoUpdate"),
        ("WHISP-BOX-MIBV2-MIB", "pass1Status"),
        ("WHISP-BOX-MIBV2-MIB", "pass2Status"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeEntryTimeout"),
        ("WHISP-BOX-MIBV2-MIB", "snmpMibPerm"),
        ("WHISP-BOX-MIBV2-MIB", "bhTimingMode"),
        ("WHISP-BOX-MIBV2-MIB", "powerControl"),
        ("WHISP-BOX-MIBV2-MIB", "extFilterDelay"),
        ("WHISP-BOX-MIBV2-MIB", "antennaGain"),
        ("WHISP-BOX-MIBV2-MIB", "eirp"),
        ("WHISP-BOX-MIBV2-MIB", "dynamicLearning"),
        ("WHISP-BOX-MIBV2-MIB", "managementVID"),
        ("WHISP-BOX-MIBV2-MIB", "agingTimeout"),
        ("WHISP-BOX-MIBV2-MIB", "frameType"),
        ("WHISP-BOX-MIBV2-MIB", "addVlanMember"),
        ("WHISP-BOX-MIBV2-MIB", "removeVlanMember"),
        ("WHISP-BOX-MIBV2-MIB", "scheduling"),
        ("WHISP-BOX-MIBV2-MIB", "transmitterOP"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeEnable"),
        ("WHISP-BOX-MIBV2-MIB", "fecEnable"),
        ("WHISP-BOX-MIBV2-MIB", "trapIP1"),
        ("WHISP-BOX-MIBV2-MIB", "trapIP2"),
        ("WHISP-BOX-MIBV2-MIB", "trapIP3"),
        ("WHISP-BOX-MIBV2-MIB", "trapIP4"),
        ("WHISP-BOX-MIBV2-MIB", "trapIP5"),
        ("WHISP-BOX-MIBV2-MIB", "trapIP6"),
        ("WHISP-BOX-MIBV2-MIB", "trapIP7"),
        ("WHISP-BOX-MIBV2-MIB", "trapIP8"),
        ("WHISP-BOX-MIBV2-MIB", "trapIP9"),
        ("WHISP-BOX-MIBV2-MIB", "trapIP10"),
        ("WHISP-BOX-MIBV2-MIB", "commStringRWrite"),
        ("WHISP-BOX-MIBV2-MIB", "subnetMask"),
        ("WHISP-BOX-MIBV2-MIB", "mngtIP"),
        ("WHISP-BOX-MIBV2-MIB", "allowVIDAccess"),
        ("WHISP-BOX-MIBV2-MIB", "setDefaultPlug"),
        ("WHISP-BOX-MIBV2-MIB", "hwsCompatibility"),
        ("WHISP-BOX-MIBV2-MIB", "gpsInput"),
        ("WHISP-BOX-MIBV2-MIB", "ism"),
        ("WHISP-BOX-MIBV2-MIB", "hiPriority"),
        ("WHISP-BOX-MIBV2-MIB", "userName"),
        ("WHISP-BOX-MIBV2-MIB", "userPassword"),
        ("WHISP-BOX-MIBV2-MIB", "userAccessLevel"),
        ("WHISP-BOX-MIBV2-MIB", "deleteUser"),
        ("WHISP-BOX-MIBV2-MIB", "twoXRate"),
        ("WHISP-BOX-MIBV2-MIB", "lanDhcpState"),
        ("WHISP-BOX-MIBV2-MIB", "dnsIpState"),
        ("WHISP-BOX-MIBV2-MIB", "sessionTimeout"),
        ("WHISP-BOX-MIBV2-MIB", "vlanMemberSource"),
        ("WHISP-BOX-MIBV2-MIB", "addCustomFreqList"),
        ("WHISP-BOX-MIBV2-MIB", "removeCustomFreqList"),
        ("WHISP-BOX-MIBV2-MIB", "allowColocation"),
        ("WHISP-BOX-MIBV2-MIB", "changeUsrPwd"),
        ("WHISP-BOX-MIBV2-MIB", "mngtIP2"),
        ("WHISP-BOX-MIBV2-MIB", "subnetMask2"),
        ("WHISP-BOX-MIBV2-MIB", "mngtIP3"),
        ("WHISP-BOX-MIBV2-MIB", "subnetMask3"),
        ("WHISP-BOX-MIBV2-MIB", "mngtIP4"),
        ("WHISP-BOX-MIBV2-MIB", "subnetMask4"),
        ("WHISP-BOX-MIBV2-MIB", "mngtIP5"),
        ("WHISP-BOX-MIBV2-MIB", "subnetMask5"),
        ("WHISP-BOX-MIBV2-MIB", "mngtIP6"),
        ("WHISP-BOX-MIBV2-MIB", "subnetMask6"),
        ("WHISP-BOX-MIBV2-MIB", "mngtIP7"),
        ("WHISP-BOX-MIBV2-MIB", "subnetMask7"),
        ("WHISP-BOX-MIBV2-MIB", "mngtIP8"),
        ("WHISP-BOX-MIBV2-MIB", "subnetMask8"),
        ("WHISP-BOX-MIBV2-MIB", "mngtIP9"),
        ("WHISP-BOX-MIBV2-MIB", "subnetMask9"),
        ("WHISP-BOX-MIBV2-MIB", "mngtIP10"),
        ("WHISP-BOX-MIBV2-MIB", "subnetMask10"),
        ("WHISP-BOX-MIBV2-MIB", "bhvlanEnable"),
        ("WHISP-BOX-MIBV2-MIB", "lldpBroadcastEnable"),
        ("WHISP-BOX-MIBV2-MIB", "radioRateAdapt"),
        ("WHISP-BOX-MIBV2-MIB", "fpgaBuildDate"),
        ("WHISP-BOX-MIBV2-MIB", "fpgaCompileInfo"),
        ("WHISP-BOX-MIBV2-MIB", "syslogDomainNameAppend"),
        ("WHISP-BOX-MIBV2-MIB", "syslogServerAddr"),
        ("WHISP-BOX-MIBV2-MIB", "syslogServerPort"),
        ("WHISP-BOX-MIBV2-MIB", "syslogMinLevel"),
        ("WHISP-BOX-MIBV2-MIB", "syslogStatTxSuccesses"),
        ("WHISP-BOX-MIBV2-MIB", "syslogStatDropped"),
        ("WHISP-BOX-MIBV2-MIB", "apType"),
        ("WHISP-BOX-MIBV2-MIB", "apSmMode"),
        ("WHISP-BOX-MIBV2-MIB", "region"),
        ("WHISP-BOX-MIBV2-MIB", "regionCode"),
        ("WHISP-BOX-MIBV2-MIB", "regionAsia"),
        ("WHISP-BOX-MIBV2-MIB", "regionEurope"),
        ("WHISP-BOX-MIBV2-MIB", "regionNorthAmerica"),
        ("WHISP-BOX-MIBV2-MIB", "regionOceania"),
        ("WHISP-BOX-MIBV2-MIB", "regionSouthAmerica"),
        ("WHISP-BOX-MIBV2-MIB", "regionAfrica"),
        ("WHISP-BOX-MIBV2-MIB", "regionOtherRegulatory"),
        ("WHISP-BOX-MIBV2-MIB", "radioRateAdaptUL"),
        ("WHISP-BOX-MIBV2-MIB", "dnsPrimaryMgmtIP"),
        ("WHISP-BOX-MIBV2-MIB", "dnsAlternateMgmtIP"),
        ("WHISP-BOX-MIBV2-MIB", "dnsMgmtDomainName"),
        ("WHISP-BOX-MIBV2-MIB", "addCustomFreqMimo"),
        ("WHISP-BOX-MIBV2-MIB", "removeCustomFreqMimo"),
        ("WHISP-BOX-MIBV2-MIB", "ftpPort"),
        ("WHISP-BOX-MIBV2-MIB", "httpPort"),
        ("WHISP-BOX-MIBV2-MIB", "snmpPort"),
        ("WHISP-BOX-MIBV2-MIB", "snmpTrapPort"),
        ("WHISP-BOX-MIBV2-MIB", "lan1DhcpRelease"),
        ("WHISP-BOX-MIBV2-MIB", "lan1DhcpRenew"),
        ("WHISP-BOX-MIBV2-MIB", "lan3DhcpRelease"),
        ("WHISP-BOX-MIBV2-MIB", "lan3DhcpRenew"),
        ("WHISP-BOX-MIBV2-MIB", "natDhcpRelease"),
        ("WHISP-BOX-MIBV2-MIB", "natDhcpRenew"),
        ("WHISP-BOX-MIBV2-MIB", "radioEngKeyed"),
        ("WHISP-BOX-MIBV2-MIB", "priorityPrecedence"),
        ("WHISP-BOX-MIBV2-MIB", "pppoeCtlPriority"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatXmtUDataCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatXmtBDataCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatXmtMDataCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatRcvUDataCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatRcvBDataCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatRcvMDataCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatXmtCntlCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatRcvCntlCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatInSyncCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatOutSyncCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatOverrunCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatUnderrunCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatRcvCorruptDataCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatRcvCorruptControlCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatBadBcastCtlCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatPLLOutOfLockCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatBeaconVerMismatchCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatBadFreqBcnRcvCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatnonLiteBcnRcvCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatUnsupFeatBcnRcvCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatUnkwnFeatBcnRcvCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatTxCalFailCnt"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatBadInSyncIDRcv"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatTempOutOfRange"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatRSSIOutOfRange"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatRangeCapEnf"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatRcvLTStart"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatRcvLTStartHS"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatRcvLTResult"),
        ("WHISP-BOX-MIBV2-MIB", "rfStatXmtLTResult"),
        ("WHISP-BOX-MIBV2-MIB", "whispFeatureKeyOrigin"),
        ("WHISP-BOX-MIBV2-MIB", "updateStatus"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbFecStatbin"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbFecStatbout"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbFecStatbtoss"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbFecStatbtosscap"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbFecStatuin"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbFecStatuout"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbFecStatutoss"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbFecStatutosscap"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbRFStatbin"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbRFStatbout"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbFecStatfloods"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbRFStatfloods"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbRFStatbtoss"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbRFStatbtosscap"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbRFStatuin"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbRFStatuout"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbRFStatutoss"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbRFStatutosscap"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbErrStatNI1QSend"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbErrStatNI2QSend"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbErrStatBridgeFull"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbErrStatSendMsg"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbErrStatAPFecQSend"),
        ("WHISP-BOX-MIBV2-MIB", "bridgeCbErrStatApRfQSend"),
        ("WHISP-BOX-MIBV2-MIB", "fecStatLinkDetected"),
        ("WHISP-BOX-MIBV2-MIB", "fecStatLinkLost"),
        ("WHISP-BOX-MIBV2-MIB", "fecInDiscardsCount"),
        ("WHISP-BOX-MIBV2-MIB", "fecInErrorsCount"),
        ("WHISP-BOX-MIBV2-MIB", "fecOutDiscardsCount"),
        ("WHISP-BOX-MIBV2-MIB", "fecOutErrorsCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfInDiscardsCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfInErrorsCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfOutDiscardsCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfOutErrorsCount"),
        ("WHISP-BOX-MIBV2-MIB", "fecInDiscardsOverloadCount"),
        ("WHISP-BOX-MIBV2-MIB", "fecOutDiscardsOverloadCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfInDiscardsOverloadCount"),
        ("WHISP-BOX-MIBV2-MIB", "rfOutDiscardsOverloadCount"),
        ("WHISP-BOX-MIBV2-MIB", "interleave"),
        ("WHISP-BOX-MIBV2-MIB", "radioMSN"),
        ("WHISP-BOX-MIBV2-MIB", "latitude"),
        ("WHISP-BOX-MIBV2-MIB", "longitude"),
        ("WHISP-BOX-MIBV2-MIB", "height"),
        ("WHISP-BOX-MIBV2-MIB", "bandwidth"),
        ("WHISP-BOX-MIBV2-MIB", "dataScramblingMethod"),
        ("WHISP-BOX-MIBV2-MIB", "whispWebUserAccessMode"),
        ("WHISP-BOX-MIBV2-MIB", "usrAccountEnableAccounting"),
        ("WHISP-BOX-MIBV2-MIB", "allowRejectThenLocal"),
        ("WHISP-BOX-MIBV2-MIB", "pppoeFilter"),
        ("WHISP-BOX-MIBV2-MIB", "smbFilter"),
        ("WHISP-BOX-MIBV2-MIB", "snmpFilter"),
        ("WHISP-BOX-MIBV2-MIB", "userP1Filter"),
        ("WHISP-BOX-MIBV2-MIB", "userP2Filter"),
        ("WHISP-BOX-MIBV2-MIB", "userP3Filter"),
        ("WHISP-BOX-MIBV2-MIB", "allOtherIpFilter"),
        ("WHISP-BOX-MIBV2-MIB", "allIpv4Filter"),
        ("WHISP-BOX-MIBV2-MIB", "arpFilter"),
        ("WHISP-BOX-MIBV2-MIB", "allOthersFilter"),
        ("WHISP-BOX-MIBV2-MIB", "userDefinedPort1"),
        ("WHISP-BOX-MIBV2-MIB", "port1TCPFilter"),
        ("WHISP-BOX-MIBV2-MIB", "port1UDPFilter"),
        ("WHISP-BOX-MIBV2-MIB", "userDefinedPort2"),
        ("WHISP-BOX-MIBV2-MIB", "port2TCPFilter"),
        ("WHISP-BOX-MIBV2-MIB", "port2UDPFilter"),
        ("WHISP-BOX-MIBV2-MIB", "userDefinedPort3"),
        ("WHISP-BOX-MIBV2-MIB", "port3TCPFilter"),
        ("WHISP-BOX-MIBV2-MIB", "port3UDPFilter"),
        ("WHISP-BOX-MIBV2-MIB", "bootpcFilter"),
        ("WHISP-BOX-MIBV2-MIB", "bootpsFilter"),
        ("WHISP-BOX-MIBV2-MIB", "ip4MultFilter"),
        ("WHISP-BOX-MIBV2-MIB", "packetFilterDirection"),
        ("WHISP-BOX-MIBV2-MIB", "encryptionConfig"))
)
if mibBuilder.loadTexts:
    whispBoxAttributesGroup.setStatus("current")

whispBoxControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 6, 1, 2)
)
whispBoxControlGroup.setObjects(
      *(("WHISP-BOX-MIBV2-MIB", "saveFlash"),
        ("WHISP-BOX-MIBV2-MIB", "reboot"),
        ("WHISP-BOX-MIBV2-MIB", "clearEventLog"),
        ("WHISP-BOX-MIBV2-MIB", "rebootIfRequired"),
        ("WHISP-BOX-MIBV2-MIB", "clearBERStats"),
        ("WHISP-BOX-MIBV2-MIB", "updateDevice"),
        ("WHISP-BOX-MIBV2-MIB", "siteInfoViewable"),
        ("WHISP-BOX-MIBV2-MIB", "largeVCQ"),
        ("WHISP-BOX-MIBV2-MIB", "snrCalculation"),
        ("WHISP-BOX-MIBV2-MIB", "receiveQualityDebug"))
)
if mibBuilder.loadTexts:
    whispBoxControlGroup.setStatus("current")

whispBoxBTGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 6, 1, 3)
)
whispBoxBTGroup.setObjects(
      *(("WHISP-BOX-MIBV2-MIB", "whispBridgeMacAddr"),
        ("WHISP-BOX-MIBV2-MIB", "whispBridgeDesLuid"),
        ("WHISP-BOX-MIBV2-MIB", "whispBridgeAge"),
        ("WHISP-BOX-MIBV2-MIB", "whispBridgeExt"),
        ("WHISP-BOX-MIBV2-MIB", "whispBridgeHash"),
        ("WHISP-BOX-MIBV2-MIB", "whispBridgeCAM"))
)
if mibBuilder.loadTexts:
    whispBoxBTGroup.setStatus("current")

whispBoxVLANTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 6, 1, 4)
)
whispBoxVLANTableGroup.setObjects(
      *(("WHISP-BOX-MIBV2-MIB", "whispVID"),
        ("WHISP-BOX-MIBV2-MIB", "whispVType"),
        ("WHISP-BOX-MIBV2-MIB", "whispVAge"))
)
if mibBuilder.loadTexts:
    whispBoxVLANTableGroup.setStatus("current")

whispBoxCPTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 6, 1, 5)
)
whispBoxCPTableGroup.setObjects(
      *(("WHISP-BOX-MIBV2-MIB", "codePoint0"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint1"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint2"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint3"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint4"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint5"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint6"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint7"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint8"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint9"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint10"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint11"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint12"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint13"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint14"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint15"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint16"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint17"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint18"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint19"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint20"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint21"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint22"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint23"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint24"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint25"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint26"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint27"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint28"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint29"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint30"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint31"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint32"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint33"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint34"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint35"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint36"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint37"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint38"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint39"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint40"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint41"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint42"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint43"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint44"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint45"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint46"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint47"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint48"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint49"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint50"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint51"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint52"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint53"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint54"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint55"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint56"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint57"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint58"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint59"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint60"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint61"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint62"),
        ("WHISP-BOX-MIBV2-MIB", "codePoint63"))
)
if mibBuilder.loadTexts:
    whispBoxCPTableGroup.setStatus("current")

whispBoxUserTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 6, 1, 6)
)
whispBoxUserTableGroup.setObjects(
      *(("WHISP-BOX-MIBV2-MIB", "entryIndex"),
        ("WHISP-BOX-MIBV2-MIB", "userLoginName"),
        ("WHISP-BOX-MIBV2-MIB", "userPswd"),
        ("WHISP-BOX-MIBV2-MIB", "accessLevel"),
        ("WHISP-BOX-MIBV2-MIB", "loginStatus"),
        ("WHISP-BOX-MIBV2-MIB", "loginMethod"),
        ("WHISP-BOX-MIBV2-MIB", "sessionTime"))
)
if mibBuilder.loadTexts:
    whispBoxUserTableGroup.setStatus("current")

whispLayer2NeighborTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 6, 1, 7)
)
whispLayer2NeighborTableGroup.setObjects(
      *(("WHISP-BOX-MIBV2-MIB", "entryL2Index"),
        ("WHISP-BOX-MIBV2-MIB", "neighborMAC"),
        ("WHISP-BOX-MIBV2-MIB", "neighborIP"),
        ("WHISP-BOX-MIBV2-MIB", "neighborSiteName"))
)
if mibBuilder.loadTexts:
    whispLayer2NeighborTableGroup.setStatus("current")


# Notification objects

boxLan1DHCPClientEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 12, 1, 1)
)
boxLan1DHCPClientEvent.setObjects(
      *(("WHISP-BOX-MIBV2-MIB", "dhcpLanIp"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    boxLan1DHCPClientEvent.setStatus(
        "current"
    )


# Notifications groups

whispBoxNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 3, 6, 1, 8)
)
whispBoxNotifGroup.setObjects(
    ("WHISP-BOX-MIBV2-MIB", "boxLan1DHCPClientEvent")
)
if mibBuilder.loadTexts:
    whispBoxNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WHISP-BOX-MIBV2-MIB",
    **{"whispBoxLevelMibModule": whispBoxLevelMibModule,
       "whispBoxStatus": whispBoxStatus,
       "whispBoxSoftwareVer": whispBoxSoftwareVer,
       "whispBoxFPGAVer": whispBoxFPGAVer,
       "whispBoxEsn": whispBoxEsn,
       "whispBoxBoot": whispBoxBoot,
       "boxTemperature": boxTemperature,
       "boxDeviceType": boxDeviceType,
       "boxDeviceTypeID": boxDeviceTypeID,
       "boxEncryption": boxEncryption,
       "etherLinkStatus": etherLinkStatus,
       "boxFrequency": boxFrequency,
       "platformVer": platformVer,
       "platformType": platformType,
       "dhcpLanIp": dhcpLanIp,
       "dhcpLanSubnetMask": dhcpLanSubnetMask,
       "dhcpLanGateway": dhcpLanGateway,
       "dhcpRfPublicIp": dhcpRfPublicIp,
       "dhcpRfPublicSubnetMask": dhcpRfPublicSubnetMask,
       "dhcpRfPublicGateway": dhcpRfPublicGateway,
       "lanDhcpStatus": lanDhcpStatus,
       "rfPublicDhcpStatus": rfPublicDhcpStatus,
       "inSyncCount": inSyncCount,
       "outSyncCount": outSyncCount,
       "pllOutLockCount": pllOutLockCount,
       "txCalFailure": txCalFailure,
       "swVersion": swVersion,
       "pldVersion": pldVersion,
       "platformInfo": platformInfo,
       "antPolarization": antPolarization,
       "packetOverloadCounter": packetOverloadCounter,
       "whispBoxP11Personality": whispBoxP11Personality,
       "whispBoxP11FPGAType": whispBoxP11FPGAType,
       "whispBoxP11BstrapFPGAVer": whispBoxP11BstrapFPGAVer,
       "numDFSDetections": numDFSDetections,
       "rxOverrunPkts": rxOverrunPkts,
       "boxTemperatureC": boxTemperatureC,
       "boxTemperatureF": boxTemperatureF,
       "bridgeCbFecStatbin": bridgeCbFecStatbin,
       "bridgeCbFecStatbout": bridgeCbFecStatbout,
       "bridgeCbFecStatbtoss": bridgeCbFecStatbtoss,
       "bridgeCbFecStatbtosscap": bridgeCbFecStatbtosscap,
       "bridgeCbFecStatuin": bridgeCbFecStatuin,
       "bridgeCbFecStatuout": bridgeCbFecStatuout,
       "bridgeCbFecStatutoss": bridgeCbFecStatutoss,
       "bridgeCbFecStatutosscap": bridgeCbFecStatutosscap,
       "bridgeCbRFStatbin": bridgeCbRFStatbin,
       "bridgeCbRFStatbout": bridgeCbRFStatbout,
       "bridgeCbRFStatbtoss": bridgeCbRFStatbtoss,
       "bridgeCbRFStatbtosscap": bridgeCbRFStatbtosscap,
       "bridgeCbRFStatuin": bridgeCbRFStatuin,
       "bridgeCbRFStatuout": bridgeCbRFStatuout,
       "bridgeCbRFStatutoss": bridgeCbRFStatutoss,
       "bridgeCbRFStatutosscap": bridgeCbRFStatutosscap,
       "bridgeCbErrStatNI1QSend": bridgeCbErrStatNI1QSend,
       "bridgeCbErrStatNI2QSend": bridgeCbErrStatNI2QSend,
       "bridgeCbErrStatBridgeFull": bridgeCbErrStatBridgeFull,
       "bridgeCbErrStatSendMsg": bridgeCbErrStatSendMsg,
       "bridgeCbErrStatAPFecQSend": bridgeCbErrStatAPFecQSend,
       "bridgeCbErrStatApRfQSend": bridgeCbErrStatApRfQSend,
       "rfStatXmtUDataCnt": rfStatXmtUDataCnt,
       "rfStatXmtBDataCnt": rfStatXmtBDataCnt,
       "rfStatRcvUDataCnt": rfStatRcvUDataCnt,
       "rfStatRcvBDataCnt": rfStatRcvBDataCnt,
       "rfStatXmtCntlCnt": rfStatXmtCntlCnt,
       "rfStatRcvCntlCnt": rfStatRcvCntlCnt,
       "rfStatInSyncCount": rfStatInSyncCount,
       "rfStatOutSyncCount": rfStatOutSyncCount,
       "rfStatOverrunCount": rfStatOverrunCount,
       "rfStatUnderrunCount": rfStatUnderrunCount,
       "rfStatRcvCorruptDataCount": rfStatRcvCorruptDataCount,
       "rfStatBadBcastCtlCnt": rfStatBadBcastCtlCnt,
       "rfStatPLLOutOfLockCnt": rfStatPLLOutOfLockCnt,
       "rfStatBeaconVerMismatchCnt": rfStatBeaconVerMismatchCnt,
       "rfStatBadFreqBcnRcvCnt": rfStatBadFreqBcnRcvCnt,
       "rfStatnonLiteBcnRcvCnt": rfStatnonLiteBcnRcvCnt,
       "rfStatUnsupFeatBcnRcvCnt": rfStatUnsupFeatBcnRcvCnt,
       "rfStatUnkwnFeatBcnRcvCnt": rfStatUnkwnFeatBcnRcvCnt,
       "rfStatTxCalFailCnt": rfStatTxCalFailCnt,
       "rfStatBadInSyncIDRcv": rfStatBadInSyncIDRcv,
       "rfStatTempOutOfRange": rfStatTempOutOfRange,
       "rfStatRSSIOutOfRange": rfStatRSSIOutOfRange,
       "rfStatRangeCapEnf": rfStatRangeCapEnf,
       "rfStatRcvLTStart": rfStatRcvLTStart,
       "rfStatRcvLTStartHS": rfStatRcvLTStartHS,
       "rfStatRcvLTResult": rfStatRcvLTResult,
       "rfStatXmtLTResult": rfStatXmtLTResult,
       "whispFeatureKeyOrigin": whispFeatureKeyOrigin,
       "radioMSN": radioMSN,
       "updateStatus": updateStatus,
       "syslogStatTxSuccesses": syslogStatTxSuccesses,
       "syslogStatDropped": syslogStatDropped,
       "fecStatLinkLost": fecStatLinkLost,
       "fecStatLinkDetected": fecStatLinkDetected,
       "natDhcpStatus": natDhcpStatus,
       "fecInDiscardsCount": fecInDiscardsCount,
       "fecInErrorsCount": fecInErrorsCount,
       "fecOutDiscardsCount": fecOutDiscardsCount,
       "fecOutErrorsCount": fecOutErrorsCount,
       "rfInDiscardsCount": rfInDiscardsCount,
       "rfInErrorsCount": rfInErrorsCount,
       "rfOutDiscardsCount": rfOutDiscardsCount,
       "rfOutErrorsCount": rfOutErrorsCount,
       "fecInDiscardsOverloadCount": fecInDiscardsOverloadCount,
       "fecOutDiscardsOverloadCount": fecOutDiscardsOverloadCount,
       "rfInDiscardsOverloadCount": rfInDiscardsOverloadCount,
       "rfOutDiscardsOverloadCount": rfOutDiscardsOverloadCount,
       "fpgaCompileInfo": fpgaCompileInfo,
       "fpgaBuildDate": fpgaBuildDate,
       "aggregateBandwidthCap": aggregateBandwidthCap,
       "calibrationStatusBool": calibrationStatusBool,
       "calibrationStatusBox": calibrationStatusBox,
       "radioEngKeyed": radioEngKeyed,
       "bridgeCbFecStatfloods": bridgeCbFecStatfloods,
       "bridgeCbRFStatfloods": bridgeCbRFStatfloods,
       "agcGainRxCH1": agcGainRxCH1,
       "agcGainRxCH2": agcGainRxCH2,
       "antType": antType,
       "rfStatRcvCorruptControlCount": rfStatRcvCorruptControlCount,
       "rfStatXmtMDataCnt": rfStatXmtMDataCnt,
       "rfStatRcvMDataCnt": rfStatRcvMDataCnt,
       "whispBoxConfig": whispBoxConfig,
       "linkNegoSpeed": linkNegoSpeed,
       "colorCode": colorCode,
       "displayOnlyAccess": displayOnlyAccess,
       "fullAccess": fullAccess,
       "webAutoUpdate": webAutoUpdate,
       "pass1Status": pass1Status,
       "pass2Status": pass2Status,
       "bridgeEntryTimeout": bridgeEntryTimeout,
       "snmpMibPerm": snmpMibPerm,
       "bhTimingMode": bhTimingMode,
       "bhModulation": bhModulation,
       "powerControl": powerControl,
       "extFilterDelay": extFilterDelay,
       "antennaGain": antennaGain,
       "eirp": eirp,
       "dynamicLearning": dynamicLearning,
       "managementVID": managementVID,
       "agingTimeout": agingTimeout,
       "frameType": frameType,
       "addVlanMember": addVlanMember,
       "removeVlanMember": removeVlanMember,
       "scheduling": scheduling,
       "transmitterOP": transmitterOP,
       "bridgeEnable": bridgeEnable,
       "fecEnable": fecEnable,
       "trapIP1": trapIP1,
       "trapIP2": trapIP2,
       "trapIP3": trapIP3,
       "trapIP4": trapIP4,
       "trapIP5": trapIP5,
       "trapIP6": trapIP6,
       "trapIP7": trapIP7,
       "trapIP8": trapIP8,
       "trapIP9": trapIP9,
       "trapIP10": trapIP10,
       "commStringRWrite": commStringRWrite,
       "subnetMask": subnetMask,
       "mngtIP": mngtIP,
       "allowVIDAccess": allowVIDAccess,
       "setDefaultPlug": setDefaultPlug,
       "hwsCompatibility": hwsCompatibility,
       "gpsInput": gpsInput,
       "ism": ism,
       "hiPriority": hiPriority,
       "userName": userName,
       "userPassword": userPassword,
       "userAccessLevel": userAccessLevel,
       "deleteUser": deleteUser,
       "twoXRate": twoXRate,
       "lanDhcpState": lanDhcpState,
       "sessionTimeout": sessionTimeout,
       "vlanMemberSource": vlanMemberSource,
       "addCustomFreqList": addCustomFreqList,
       "removeCustomFreqList": removeCustomFreqList,
       "allowColocation": allowColocation,
       "changeUsrPwd": changeUsrPwd,
       "mngtIP2": mngtIP2,
       "subnetMask2": subnetMask2,
       "mngtIP3": mngtIP3,
       "subnetMask3": subnetMask3,
       "mngtIP4": mngtIP4,
       "subnetMask4": subnetMask4,
       "mngtIP5": mngtIP5,
       "subnetMask5": subnetMask5,
       "mngtIP6": mngtIP6,
       "subnetMask6": subnetMask6,
       "mngtIP7": mngtIP7,
       "subnetMask7": subnetMask7,
       "mngtIP8": mngtIP8,
       "subnetMask8": subnetMask8,
       "mngtIP9": mngtIP9,
       "subnetMask9": subnetMask9,
       "mngtIP10": mngtIP10,
       "subnetMask10": subnetMask10,
       "bhvlanEnable": bhvlanEnable,
       "lldpBroadcastEnable": lldpBroadcastEnable,
       "regionCode": regionCode,
       "russiaRegion": russiaRegion,
       "commStringROnly": commStringROnly,
       "ethernetLinkSpeed": ethernetLinkSpeed,
       "cyclicPrefix": cyclicPrefix,
       "numberCustomFreq": numberCustomFreq,
       "channelBandwidth": channelBandwidth,
       "setDefaults": setDefaults,
       "radioRateAdapt": radioRateAdapt,
       "siteInfoViewable": siteInfoViewable,
       "largeVCQ": largeVCQ,
       "latitude": latitude,
       "longitude": longitude,
       "height": height,
       "bandwidth": bandwidth,
       "dataScramblingMethod": dataScramblingMethod,
       "portVID": portVID,
       "radioRateAdaptUL": radioRateAdaptUL,
       "providerVID": providerVID,
       "mac1VIDMapAddr": mac1VIDMapAddr,
       "mac1VIDMapVid": mac1VIDMapVid,
       "mac2VIDMapAddr": mac2VIDMapAddr,
       "mac2VIDMapVid": mac2VIDMapVid,
       "mac3VIDMapAddr": mac3VIDMapAddr,
       "mac3VIDMapVid": mac3VIDMapVid,
       "mac4VIDMapAddr": mac4VIDMapAddr,
       "mac4VIDMapVid": mac4VIDMapVid,
       "mac5VIDMapAddr": mac5VIDMapAddr,
       "mac5VIDMapVid": mac5VIDMapVid,
       "mac6VIDMapAddr": mac6VIDMapAddr,
       "mac6VIDMapVid": mac6VIDMapVid,
       "mac7VIDMapAddr": mac7VIDMapAddr,
       "mac7VIDMapVid": mac7VIDMapVid,
       "mac8VIDMapAddr": mac8VIDMapAddr,
       "mac8VIDMapVid": mac8VIDMapVid,
       "mac9VIDMapAddr": mac9VIDMapAddr,
       "mac9VIDMapVid": mac9VIDMapVid,
       "mac10VIDMapAddr": mac10VIDMapAddr,
       "mac10VIDMapVid": mac10VIDMapVid,
       "vlanPortType": vlanPortType,
       "vlanAcceptQinQFrames": vlanAcceptQinQFrames,
       "whispWebUserAccessMode": whispWebUserAccessMode,
       "usrAccountEnableAccounting": usrAccountEnableAccounting,
       "allowRejectThenLocal": allowRejectThenLocal,
       "snrCalculation": snrCalculation,
       "priorityPrecedence": priorityPrecedence,
       "installationColorCode": installationColorCode,
       "apSmMode": apSmMode,
       "pppoeFilter": pppoeFilter,
       "smbFilter": smbFilter,
       "snmpFilter": snmpFilter,
       "userP1Filter": userP1Filter,
       "userP2Filter": userP2Filter,
       "userP3Filter": userP3Filter,
       "allOtherIpFilter": allOtherIpFilter,
       "allIpv4Filter": allIpv4Filter,
       "arpFilter": arpFilter,
       "allOthersFilter": allOthersFilter,
       "userDefinedPort1": userDefinedPort1,
       "port1TCPFilter": port1TCPFilter,
       "port1UDPFilter": port1UDPFilter,
       "userDefinedPort2": userDefinedPort2,
       "port2TCPFilter": port2TCPFilter,
       "port2UDPFilter": port2UDPFilter,
       "userDefinedPort3": userDefinedPort3,
       "port3TCPFilter": port3TCPFilter,
       "port3UDPFilter": port3UDPFilter,
       "bootpcFilter": bootpcFilter,
       "bootpsFilter": bootpsFilter,
       "ip4MultFilter": ip4MultFilter,
       "packetFilterDirection": packetFilterDirection,
       "encryptionConfig": encryptionConfig,
       "pppoeCtlPriority": pppoeCtlPriority,
       "ftpPort": ftpPort,
       "httpPort": httpPort,
       "snmpPort": snmpPort,
       "snmpTrapPort": snmpTrapPort,
       "syslogDomainNameAppend": syslogDomainNameAppend,
       "syslogServerAddr": syslogServerAddr,
       "syslogServerPort": syslogServerPort,
       "syslogMinLevel": syslogMinLevel,
       "lan1DhcpRelease": lan1DhcpRelease,
       "lan1DhcpRenew": lan1DhcpRenew,
       "lan3DhcpRelease": lan3DhcpRelease,
       "lan3DhcpRenew": lan3DhcpRenew,
       "natDhcpRelease": natDhcpRelease,
       "natDhcpRenew": natDhcpRenew,
       "region": region,
       "regionAsia": regionAsia,
       "regionEurope": regionEurope,
       "regionNorthAmerica": regionNorthAmerica,
       "regionOceania": regionOceania,
       "regionSouthAmerica": regionSouthAmerica,
       "regionOtherRegulatory": regionOtherRegulatory,
       "interleave": interleave,
       "receiveQualityDebug": receiveQualityDebug,
       "apType": apType,
       "regionAfrica": regionAfrica,
       "addCustomFreqMimo": addCustomFreqMimo,
       "removeCustomFreqMimo": removeCustomFreqMimo,
       "timedSpectrumAnalysisDurationBox": timedSpectrumAnalysisDurationBox,
       "spectrumAnalysisActionBox": spectrumAnalysisActionBox,
       "whispBoxControls": whispBoxControls,
       "saveFlash": saveFlash,
       "reboot": reboot,
       "clearEventLog": clearEventLog,
       "rebootIfRequired": rebootIfRequired,
       "clearBERStats": clearBERStats,
       "updateDevice": updateDevice,
       "whispBoxBridgeTable": whispBoxBridgeTable,
       "whispBoxBridgeEntry": whispBoxBridgeEntry,
       "whispBridgeMacAddr": whispBridgeMacAddr,
       "whispBridgeDesLuid": whispBridgeDesLuid,
       "whispBridgeAge": whispBridgeAge,
       "whispBridgeExt": whispBridgeExt,
       "whispBridgeHash": whispBridgeHash,
       "whispBridgeCAM": whispBridgeCAM,
       "whispBoxEventLog": whispBoxEventLog,
       "whispBoxEvntLog": whispBoxEvntLog,
       "whispBoxConf": whispBoxConf,
       "whispBoxGroups": whispBoxGroups,
       "whispBoxAttributesGroup": whispBoxAttributesGroup,
       "whispBoxControlGroup": whispBoxControlGroup,
       "whispBoxBTGroup": whispBoxBTGroup,
       "whispBoxVLANTableGroup": whispBoxVLANTableGroup,
       "whispBoxCPTableGroup": whispBoxCPTableGroup,
       "whispBoxUserTableGroup": whispBoxUserTableGroup,
       "whispLayer2NeighborTableGroup": whispLayer2NeighborTableGroup,
       "whispBoxNotifGroup": whispBoxNotifGroup,
       "whispBoxBridgeVar": whispBoxBridgeVar,
       "whispBridgeTbUsed": whispBridgeTbUsed,
       "whispBridgeTbFree": whispBridgeTbFree,
       "whispBridgeTbErr": whispBridgeTbErr,
       "whispVLANTable": whispVLANTable,
       "whispVLANEntry": whispVLANEntry,
       "whispVID": whispVID,
       "whispVType": whispVType,
       "whispVAge": whispVAge,
       "whispBoxCPVar": whispBoxCPVar,
       "codePoint0": codePoint0,
       "codePoint1": codePoint1,
       "codePoint2": codePoint2,
       "codePoint3": codePoint3,
       "codePoint4": codePoint4,
       "codePoint5": codePoint5,
       "codePoint6": codePoint6,
       "codePoint7": codePoint7,
       "codePoint8": codePoint8,
       "codePoint9": codePoint9,
       "codePoint10": codePoint10,
       "codePoint11": codePoint11,
       "codePoint12": codePoint12,
       "codePoint13": codePoint13,
       "codePoint14": codePoint14,
       "codePoint15": codePoint15,
       "codePoint16": codePoint16,
       "codePoint17": codePoint17,
       "codePoint18": codePoint18,
       "codePoint19": codePoint19,
       "codePoint20": codePoint20,
       "codePoint21": codePoint21,
       "codePoint22": codePoint22,
       "codePoint23": codePoint23,
       "codePoint24": codePoint24,
       "codePoint25": codePoint25,
       "codePoint26": codePoint26,
       "codePoint27": codePoint27,
       "codePoint28": codePoint28,
       "codePoint29": codePoint29,
       "codePoint30": codePoint30,
       "codePoint31": codePoint31,
       "codePoint32": codePoint32,
       "codePoint33": codePoint33,
       "codePoint34": codePoint34,
       "codePoint35": codePoint35,
       "codePoint36": codePoint36,
       "codePoint37": codePoint37,
       "codePoint38": codePoint38,
       "codePoint39": codePoint39,
       "codePoint40": codePoint40,
       "codePoint41": codePoint41,
       "codePoint42": codePoint42,
       "codePoint43": codePoint43,
       "codePoint44": codePoint44,
       "codePoint45": codePoint45,
       "codePoint46": codePoint46,
       "codePoint47": codePoint47,
       "codePoint48": codePoint48,
       "codePoint49": codePoint49,
       "codePoint50": codePoint50,
       "codePoint51": codePoint51,
       "codePoint52": codePoint52,
       "codePoint53": codePoint53,
       "codePoint54": codePoint54,
       "codePoint55": codePoint55,
       "codePoint56": codePoint56,
       "codePoint57": codePoint57,
       "codePoint58": codePoint58,
       "codePoint59": codePoint59,
       "codePoint60": codePoint60,
       "codePoint61": codePoint61,
       "codePoint62": codePoint62,
       "codePoint63": codePoint63,
       "whispUserTable": whispUserTable,
       "whispUserEntry": whispUserEntry,
       "entryIndex": entryIndex,
       "userLoginName": userLoginName,
       "userPswd": userPswd,
       "accessLevel": accessLevel,
       "loginStatus": loginStatus,
       "loginMethod": loginMethod,
       "sessionTime": sessionTime,
       "whispLayer2NeighborTable": whispLayer2NeighborTable,
       "whispLayer2NeighborEntry": whispLayer2NeighborEntry,
       "entryL2Index": entryL2Index,
       "neighborMAC": neighborMAC,
       "neighborIP": neighborIP,
       "neighborSiteName": neighborSiteName,
       "whispBoxEvent": whispBoxEvent,
       "whispBoxDHCPClientEvent": whispBoxDHCPClientEvent,
       "boxLan1DHCPClientEvent": boxLan1DHCPClientEvent,
       "whispBoxDNS": whispBoxDNS,
       "dnsIpState": dnsIpState,
       "dnsPrimaryMgmtIP": dnsPrimaryMgmtIP,
       "dnsAlternateMgmtIP": dnsAlternateMgmtIP,
       "dnsMgmtDomainName": dnsMgmtDomainName,
       "trapDomainNameAppend": trapDomainNameAppend,
       "trap1": trap1,
       "trap2": trap2,
       "trap3": trap3,
       "trap4": trap4,
       "trap5": trap5,
       "trap6": trap6,
       "trap7": trap7,
       "trap8": trap8,
       "trap9": trap9,
       "trap10": trap10,
       "whispBoxRFPhysical": whispBoxRFPhysical,
       "whispBoxRFPhysicalRadios": whispBoxRFPhysicalRadios,
       "whispBoxRFPhysicalRadioEntry": whispBoxRFPhysicalRadioEntry,
       "radioIndex": radioIndex,
       "radioType": radioType,
       "radioPaths": radioPaths,
       "whispBoxRFPhysicalRadioPaths": whispBoxRFPhysicalRadioPaths,
       "whispBoxRFPhysicalRadioPathEntry": whispBoxRFPhysicalRadioPathEntry,
       "pathIndex": pathIndex,
       "whispBoxRFPhysicalRadioFrequencies": whispBoxRFPhysicalRadioFrequencies,
       "whispBoxRFPhysicalRadioFrequencyEntry": whispBoxRFPhysicalRadioFrequencyEntry,
       "frequency": frequency,
       "whispBoxRFConfig": whispBoxRFConfig,
       "whispBoxRFConfigRadios": whispBoxRFConfigRadios,
       "whispBoxRFConfigRadioEntry": whispBoxRFConfigRadioEntry,
       "radioConfigIndex": radioConfigIndex,
       "radioFrequencyBand": radioFrequencyBand}
)
