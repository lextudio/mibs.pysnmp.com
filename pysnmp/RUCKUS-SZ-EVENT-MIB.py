# SNMP MIB module (RUCKUS-SZ-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-SZ-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:46 2024
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

(ruckusEvents,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusEvents")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruckusSZEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusSZEventTraps_ObjectIdentity = ObjectIdentity
ruckusSZEventTraps = _RuckusSZEventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1)
)
_RuckusSZEventObjects_ObjectIdentity = ObjectIdentity
ruckusSZEventObjects = _RuckusSZEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2)
)
_RuckusSZEventDescription_Type = OctetString
_RuckusSZEventDescription_Object = MibScalar
ruckusSZEventDescription = _RuckusSZEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 1),
    _RuckusSZEventDescription_Type()
)
ruckusSZEventDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventDescription.setStatus("current")
_RuckusSZClusterName_Type = OctetString
_RuckusSZClusterName_Object = MibScalar
ruckusSZClusterName = _RuckusSZClusterName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 2),
    _RuckusSZClusterName_Type()
)
ruckusSZClusterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZClusterName.setStatus("current")
_RuckusSZEventCode_Type = OctetString
_RuckusSZEventCode_Object = MibScalar
ruckusSZEventCode = _RuckusSZEventCode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 10),
    _RuckusSZEventCode_Type()
)
ruckusSZEventCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventCode.setStatus("current")
_RuckusSZProcessName_Type = OctetString
_RuckusSZProcessName_Object = MibScalar
ruckusSZProcessName = _RuckusSZProcessName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 11),
    _RuckusSZProcessName_Type()
)
ruckusSZProcessName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZProcessName.setStatus("current")
_RuckusSZEventCtrlIP_Type = OctetString
_RuckusSZEventCtrlIP_Object = MibScalar
ruckusSZEventCtrlIP = _RuckusSZEventCtrlIP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 12),
    _RuckusSZEventCtrlIP_Type()
)
ruckusSZEventCtrlIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventCtrlIP.setStatus("current")
_RuckusSZEventSeverity_Type = OctetString
_RuckusSZEventSeverity_Object = MibScalar
ruckusSZEventSeverity = _RuckusSZEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 13),
    _RuckusSZEventSeverity_Type()
)
ruckusSZEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventSeverity.setStatus("current")
_RuckusSZEventType_Type = OctetString
_RuckusSZEventType_Object = MibScalar
ruckusSZEventType = _RuckusSZEventType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 14),
    _RuckusSZEventType_Type()
)
ruckusSZEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventType.setStatus("current")
_RuckusSZEventNodeMgmtIp_Type = OctetString
_RuckusSZEventNodeMgmtIp_Object = MibScalar
ruckusSZEventNodeMgmtIp = _RuckusSZEventNodeMgmtIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 15),
    _RuckusSZEventNodeMgmtIp_Type()
)
ruckusSZEventNodeMgmtIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventNodeMgmtIp.setStatus("current")
_RuckusSZEventNodeName_Type = OctetString
_RuckusSZEventNodeName_Object = MibScalar
ruckusSZEventNodeName = _RuckusSZEventNodeName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 16),
    _RuckusSZEventNodeName_Type()
)
ruckusSZEventNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventNodeName.setStatus("current")
_RuckusSZCPUPerc_Type = OctetString
_RuckusSZCPUPerc_Object = MibScalar
ruckusSZCPUPerc = _RuckusSZCPUPerc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 17),
    _RuckusSZCPUPerc_Type()
)
ruckusSZCPUPerc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZCPUPerc.setStatus("current")
_RuckusSZMemoryPerc_Type = OctetString
_RuckusSZMemoryPerc_Object = MibScalar
ruckusSZMemoryPerc = _RuckusSZMemoryPerc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 18),
    _RuckusSZMemoryPerc_Type()
)
ruckusSZMemoryPerc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZMemoryPerc.setStatus("current")
_RuckusSZDiskPerc_Type = OctetString
_RuckusSZDiskPerc_Object = MibScalar
ruckusSZDiskPerc = _RuckusSZDiskPerc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 19),
    _RuckusSZDiskPerc_Type()
)
ruckusSZDiskPerc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZDiskPerc.setStatus("current")
_RuckusSZEventMacAddr_Type = OctetString
_RuckusSZEventMacAddr_Object = MibScalar
ruckusSZEventMacAddr = _RuckusSZEventMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 20),
    _RuckusSZEventMacAddr_Type()
)
ruckusSZEventMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventMacAddr.setStatus("current")
_RuckusSZEventFirmwareVersion_Type = OctetString
_RuckusSZEventFirmwareVersion_Object = MibScalar
ruckusSZEventFirmwareVersion = _RuckusSZEventFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 21),
    _RuckusSZEventFirmwareVersion_Type()
)
ruckusSZEventFirmwareVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventFirmwareVersion.setStatus("current")
_RuckusSZEventUpgradedFirmwareVersion_Type = OctetString
_RuckusSZEventUpgradedFirmwareVersion_Object = MibScalar
ruckusSZEventUpgradedFirmwareVersion = _RuckusSZEventUpgradedFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 22),
    _RuckusSZEventUpgradedFirmwareVersion_Type()
)
ruckusSZEventUpgradedFirmwareVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventUpgradedFirmwareVersion.setStatus("current")
_RuckusSZEventAPMacAddr_Type = OctetString
_RuckusSZEventAPMacAddr_Object = MibScalar
ruckusSZEventAPMacAddr = _RuckusSZEventAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 23),
    _RuckusSZEventAPMacAddr_Type()
)
ruckusSZEventAPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventAPMacAddr.setStatus("current")
_RuckusSZEventReason_Type = OctetString
_RuckusSZEventReason_Object = MibScalar
ruckusSZEventReason = _RuckusSZEventReason_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 24),
    _RuckusSZEventReason_Type()
)
ruckusSZEventReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventReason.setStatus("current")
_RuckusSZEventAPName_Type = OctetString
_RuckusSZEventAPName_Object = MibScalar
ruckusSZEventAPName = _RuckusSZEventAPName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 25),
    _RuckusSZEventAPName_Type()
)
ruckusSZEventAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventAPName.setStatus("current")
_RuckusSZEventAPIP_Type = OctetString
_RuckusSZEventAPIP_Object = MibScalar
ruckusSZEventAPIP = _RuckusSZEventAPIP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 26),
    _RuckusSZEventAPIP_Type()
)
ruckusSZEventAPIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventAPIP.setStatus("current")
_RuckusSZEventAPLocation_Type = OctetString
_RuckusSZEventAPLocation_Object = MibScalar
ruckusSZEventAPLocation = _RuckusSZEventAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 27),
    _RuckusSZEventAPLocation_Type()
)
ruckusSZEventAPLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventAPLocation.setStatus("current")
_RuckusSZEventAPGPSCoordinates_Type = OctetString
_RuckusSZEventAPGPSCoordinates_Object = MibScalar
ruckusSZEventAPGPSCoordinates = _RuckusSZEventAPGPSCoordinates_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 28),
    _RuckusSZEventAPGPSCoordinates_Type()
)
ruckusSZEventAPGPSCoordinates.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventAPGPSCoordinates.setStatus("current")
_RuckusSZEventAPDescription_Type = OctetString
_RuckusSZEventAPDescription_Object = MibScalar
ruckusSZEventAPDescription = _RuckusSZEventAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 29),
    _RuckusSZEventAPDescription_Type()
)
ruckusSZEventAPDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventAPDescription.setStatus("current")
_RuckusSZAPModel_Type = OctetString
_RuckusSZAPModel_Object = MibScalar
ruckusSZAPModel = _RuckusSZAPModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 31),
    _RuckusSZAPModel_Type()
)
ruckusSZAPModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZAPModel.setStatus("current")
_RuckusSZConfigAPModel_Type = OctetString
_RuckusSZConfigAPModel_Object = MibScalar
ruckusSZConfigAPModel = _RuckusSZConfigAPModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 32),
    _RuckusSZConfigAPModel_Type()
)
ruckusSZConfigAPModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZConfigAPModel.setStatus("current")
_RuckusSZAPConfigID_Type = OctetString
_RuckusSZAPConfigID_Object = MibScalar
ruckusSZAPConfigID = _RuckusSZAPConfigID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 33),
    _RuckusSZAPConfigID_Type()
)
ruckusSZAPConfigID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZAPConfigID.setStatus("current")
_RuckusSZEventAPIPv6_Type = OctetString
_RuckusSZEventAPIPv6_Object = MibScalar
ruckusSZEventAPIPv6 = _RuckusSZEventAPIPv6_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 35),
    _RuckusSZEventAPIPv6_Type()
)
ruckusSZEventAPIPv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventAPIPv6.setStatus("current")
_RuckusSZLBSURL_Type = OctetString
_RuckusSZLBSURL_Object = MibScalar
ruckusSZLBSURL = _RuckusSZLBSURL_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 38),
    _RuckusSZLBSURL_Type()
)
ruckusSZLBSURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZLBSURL.setStatus("current")
_RuckusSZLBSPort_Type = OctetString
_RuckusSZLBSPort_Object = MibScalar
ruckusSZLBSPort = _RuckusSZLBSPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 39),
    _RuckusSZLBSPort_Type()
)
ruckusSZLBSPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZLBSPort.setStatus("current")
_RuckusSZEventSSID_Type = OctetString
_RuckusSZEventSSID_Object = MibScalar
ruckusSZEventSSID = _RuckusSZEventSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 40),
    _RuckusSZEventSSID_Type()
)
ruckusSZEventSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventSSID.setStatus("current")
_RuckusSZEventRogueMac_Type = OctetString
_RuckusSZEventRogueMac_Object = MibScalar
ruckusSZEventRogueMac = _RuckusSZEventRogueMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 45),
    _RuckusSZEventRogueMac_Type()
)
ruckusSZEventRogueMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventRogueMac.setStatus("current")
_RuckusPrimaryGRE_Type = OctetString
_RuckusPrimaryGRE_Object = MibScalar
ruckusPrimaryGRE = _RuckusPrimaryGRE_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 46),
    _RuckusPrimaryGRE_Type()
)
ruckusPrimaryGRE.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusPrimaryGRE.setStatus("current")
_RuckusSecondaryGRE_Type = OctetString
_RuckusSecondaryGRE_Object = MibScalar
ruckusSecondaryGRE = _RuckusSecondaryGRE_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 47),
    _RuckusSecondaryGRE_Type()
)
ruckusSecondaryGRE.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSecondaryGRE.setStatus("current")
_RuckusSoftGREGatewayList_Type = OctetString
_RuckusSoftGREGatewayList_Object = MibScalar
ruckusSoftGREGatewayList = _RuckusSoftGREGatewayList_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 48),
    _RuckusSoftGREGatewayList_Type()
)
ruckusSoftGREGatewayList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSoftGREGatewayList.setStatus("current")
_RuckusSZSoftGREGWAddress_Type = OctetString
_RuckusSZSoftGREGWAddress_Object = MibScalar
ruckusSZSoftGREGWAddress = _RuckusSZSoftGREGWAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 49),
    _RuckusSZSoftGREGWAddress_Type()
)
ruckusSZSoftGREGWAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZSoftGREGWAddress.setStatus("current")
_RuckusSZEventClientMacAddr_Type = OctetString
_RuckusSZEventClientMacAddr_Object = MibScalar
ruckusSZEventClientMacAddr = _RuckusSZEventClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 50),
    _RuckusSZEventClientMacAddr_Type()
)
ruckusSZEventClientMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZEventClientMacAddr.setStatus("current")
_RuckusSZDPKey_Type = OctetString
_RuckusSZDPKey_Object = MibScalar
ruckusSZDPKey = _RuckusSZDPKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 80),
    _RuckusSZDPKey_Type()
)
ruckusSZDPKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZDPKey.setStatus("current")
_RuckusSZDPConfigID_Type = OctetString
_RuckusSZDPConfigID_Object = MibScalar
ruckusSZDPConfigID = _RuckusSZDPConfigID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 81),
    _RuckusSZDPConfigID_Type()
)
ruckusSZDPConfigID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZDPConfigID.setStatus("current")
_RuckusSZDPIP_Type = OctetString
_RuckusSZDPIP_Object = MibScalar
ruckusSZDPIP = _RuckusSZDPIP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 82),
    _RuckusSZDPIP_Type()
)
ruckusSZDPIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZDPIP.setStatus("current")
_RuckusSZNetworkPortID_Type = OctetString
_RuckusSZNetworkPortID_Object = MibScalar
ruckusSZNetworkPortID = _RuckusSZNetworkPortID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 100),
    _RuckusSZNetworkPortID_Type()
)
ruckusSZNetworkPortID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZNetworkPortID.setStatus("current")
_RuckusSZNetworkInterface_Type = OctetString
_RuckusSZNetworkInterface_Object = MibScalar
ruckusSZNetworkInterface = _RuckusSZNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 101),
    _RuckusSZNetworkInterface_Type()
)
ruckusSZNetworkInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZNetworkInterface.setStatus("current")
_RuckusSZSwitchStatus_Type = OctetString
_RuckusSZSwitchStatus_Object = MibScalar
ruckusSZSwitchStatus = _RuckusSZSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 102),
    _RuckusSZSwitchStatus_Type()
)
ruckusSZSwitchStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZSwitchStatus.setStatus("current")
_RuckusSZTemperatureStatus_Type = OctetString
_RuckusSZTemperatureStatus_Object = MibScalar
ruckusSZTemperatureStatus = _RuckusSZTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 120),
    _RuckusSZTemperatureStatus_Type()
)
ruckusSZTemperatureStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZTemperatureStatus.setStatus("current")
_RuckusSZProcessorId_Type = OctetString
_RuckusSZProcessorId_Object = MibScalar
ruckusSZProcessorId = _RuckusSZProcessorId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 121),
    _RuckusSZProcessorId_Type()
)
ruckusSZProcessorId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZProcessorId.setStatus("current")
_RuckusSZFanId_Type = OctetString
_RuckusSZFanId_Object = MibScalar
ruckusSZFanId = _RuckusSZFanId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 122),
    _RuckusSZFanId_Type()
)
ruckusSZFanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZFanId.setStatus("current")
_RuckusSZFanStatus_Type = OctetString
_RuckusSZFanStatus_Object = MibScalar
ruckusSZFanStatus = _RuckusSZFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 123),
    _RuckusSZFanStatus_Type()
)
ruckusSZFanStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZFanStatus.setStatus("current")
_RuckusSZLicenseType_Type = OctetString
_RuckusSZLicenseType_Object = MibScalar
ruckusSZLicenseType = _RuckusSZLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 150),
    _RuckusSZLicenseType_Type()
)
ruckusSZLicenseType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZLicenseType.setStatus("current")
_RuckusSZLicenseUsagePerc_Type = OctetString
_RuckusSZLicenseUsagePerc_Object = MibScalar
ruckusSZLicenseUsagePerc = _RuckusSZLicenseUsagePerc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 151),
    _RuckusSZLicenseUsagePerc_Type()
)
ruckusSZLicenseUsagePerc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZLicenseUsagePerc.setStatus("current")
_RuckusSZLicenseServerName_Type = OctetString
_RuckusSZLicenseServerName_Object = MibScalar
ruckusSZLicenseServerName = _RuckusSZLicenseServerName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 152),
    _RuckusSZLicenseServerName_Type()
)
ruckusSZLicenseServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZLicenseServerName.setStatus("current")
_RuckusSZIPSecGWAddress_Type = OctetString
_RuckusSZIPSecGWAddress_Object = MibScalar
ruckusSZIPSecGWAddress = _RuckusSZIPSecGWAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 153),
    _RuckusSZIPSecGWAddress_Type()
)
ruckusSZIPSecGWAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZIPSecGWAddress.setStatus("current")
_RuckusSZSyslogServerAddress_Type = OctetString
_RuckusSZSyslogServerAddress_Object = MibScalar
ruckusSZSyslogServerAddress = _RuckusSZSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 154),
    _RuckusSZSyslogServerAddress_Type()
)
ruckusSZSyslogServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZSyslogServerAddress.setStatus("current")
_RuckusSZSrcSyslogServerAddress_Type = OctetString
_RuckusSZSrcSyslogServerAddress_Object = MibScalar
ruckusSZSrcSyslogServerAddress = _RuckusSZSrcSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 155),
    _RuckusSZSrcSyslogServerAddress_Type()
)
ruckusSZSrcSyslogServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZSrcSyslogServerAddress.setStatus("current")
_RuckusSZDestSyslogServerAddress_Type = OctetString
_RuckusSZDestSyslogServerAddress_Object = MibScalar
ruckusSZDestSyslogServerAddress = _RuckusSZDestSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 156),
    _RuckusSZDestSyslogServerAddress_Type()
)
ruckusSZDestSyslogServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZDestSyslogServerAddress.setStatus("current")
_RuckusSZFtpIp_Type = OctetString
_RuckusSZFtpIp_Object = MibScalar
ruckusSZFtpIp = _RuckusSZFtpIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 200),
    _RuckusSZFtpIp_Type()
)
ruckusSZFtpIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZFtpIp.setStatus("current")
_RuckusSZFtpPort_Type = OctetString
_RuckusSZFtpPort_Object = MibScalar
ruckusSZFtpPort = _RuckusSZFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 201),
    _RuckusSZFtpPort_Type()
)
ruckusSZFtpPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZFtpPort.setStatus("current")
_RuckusSZSrcProcess_Type = OctetString
_RuckusSZSrcProcess_Object = MibScalar
ruckusSZSrcProcess = _RuckusSZSrcProcess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 301),
    _RuckusSZSrcProcess_Type()
)
ruckusSZSrcProcess.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZSrcProcess.setStatus("current")
_RuckusSZUEImsi_Type = OctetString
_RuckusSZUEImsi_Object = MibScalar
ruckusSZUEImsi = _RuckusSZUEImsi_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 305),
    _RuckusSZUEImsi_Type()
)
ruckusSZUEImsi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZUEImsi.setStatus("current")
_RuckusSZUEMsisdn_Type = OctetString
_RuckusSZUEMsisdn_Object = MibScalar
ruckusSZUEMsisdn = _RuckusSZUEMsisdn_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 306),
    _RuckusSZUEMsisdn_Type()
)
ruckusSZUEMsisdn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZUEMsisdn.setStatus("current")
_RuckusSZAuthSrvrIp_Type = OctetString
_RuckusSZAuthSrvrIp_Object = MibScalar
ruckusSZAuthSrvrIp = _RuckusSZAuthSrvrIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 307),
    _RuckusSZAuthSrvrIp_Type()
)
ruckusSZAuthSrvrIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZAuthSrvrIp.setStatus("current")
_RuckusSZRadProxyIp_Type = OctetString
_RuckusSZRadProxyIp_Object = MibScalar
ruckusSZRadProxyIp = _RuckusSZRadProxyIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 308),
    _RuckusSZRadProxyIp_Type()
)
ruckusSZRadProxyIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZRadProxyIp.setStatus("current")
_RuckusSZAccSrvrIp_Type = OctetString
_RuckusSZAccSrvrIp_Object = MibScalar
ruckusSZAccSrvrIp = _RuckusSZAccSrvrIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 309),
    _RuckusSZAccSrvrIp_Type()
)
ruckusSZAccSrvrIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZAccSrvrIp.setStatus("current")
_RuckusSZRadSrvrIp_Type = OctetString
_RuckusSZRadSrvrIp_Object = MibScalar
ruckusSZRadSrvrIp = _RuckusSZRadSrvrIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 312),
    _RuckusSZRadSrvrIp_Type()
)
ruckusSZRadSrvrIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZRadSrvrIp.setStatus("current")
_RuckusSZUserName_Type = OctetString
_RuckusSZUserName_Object = MibScalar
ruckusSZUserName = _RuckusSZUserName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 324),
    _RuckusSZUserName_Type()
)
ruckusSZUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZUserName.setStatus("current")
_RuckusSZFileName_Type = OctetString
_RuckusSZFileName_Object = MibScalar
ruckusSZFileName = _RuckusSZFileName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 326),
    _RuckusSZFileName_Type()
)
ruckusSZFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZFileName.setStatus("current")
_RuckusSZLDAPSrvrIp_Type = OctetString
_RuckusSZLDAPSrvrIp_Object = MibScalar
ruckusSZLDAPSrvrIp = _RuckusSZLDAPSrvrIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 327),
    _RuckusSZLDAPSrvrIp_Type()
)
ruckusSZLDAPSrvrIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZLDAPSrvrIp.setStatus("current")
_RuckusSZADSrvrIp_Type = OctetString
_RuckusSZADSrvrIp_Object = MibScalar
ruckusSZADSrvrIp = _RuckusSZADSrvrIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 328),
    _RuckusSZADSrvrIp_Type()
)
ruckusSZADSrvrIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZADSrvrIp.setStatus("current")
_RuckusSZSoftwareName_Type = OctetString
_RuckusSZSoftwareName_Object = MibScalar
ruckusSZSoftwareName = _RuckusSZSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 329),
    _RuckusSZSoftwareName_Type()
)
ruckusSZSoftwareName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZSoftwareName.setStatus("current")
_RuckusSZDomainName_Type = OctetString
_RuckusSZDomainName_Object = MibScalar
ruckusSZDomainName = _RuckusSZDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 330),
    _RuckusSZDomainName_Type()
)
ruckusSZDomainName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZDomainName.setStatus("current")
_RuckusSZDNATIp_Type = OctetString
_RuckusSZDNATIp_Object = MibScalar
ruckusSZDNATIp = _RuckusSZDNATIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 2, 331),
    _RuckusSZDNATIp_Type()
)
ruckusSZDNATIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSZDNATIp.setStatus("current")

# Managed Objects groups


# Notification objects

ruckusSZSystemMiscEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 1)
)
ruckusSZSystemMiscEventTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventDescription"))
)
if mibBuilder.loadTexts:
    ruckusSZSystemMiscEventTrap.setStatus(
        "current"
    )

ruckusSZUpgradeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 2)
)
ruckusSZUpgradeSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventFirmwareVersion"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventUpgradedFirmwareVersion"))
)
if mibBuilder.loadTexts:
    ruckusSZUpgradeSuccessTrap.setStatus(
        "current"
    )

ruckusSZUpgradeFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 3)
)
ruckusSZUpgradeFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventFirmwareVersion"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventUpgradedFirmwareVersion"))
)
if mibBuilder.loadTexts:
    ruckusSZUpgradeFailedTrap.setStatus(
        "current"
    )

ruckusSZNodeRestartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 4)
)
ruckusSZNodeRestartedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"))
)
if mibBuilder.loadTexts:
    ruckusSZNodeRestartedTrap.setStatus(
        "current"
    )

ruckusSZNodeShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 5)
)
ruckusSZNodeShutdownTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZNodeShutdownTrap.setStatus(
        "current"
    )

ruckusSZCPUUsageThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 6)
)
ruckusSZCPUUsageThresholdExceededTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZCPUPerc"))
)
if mibBuilder.loadTexts:
    ruckusSZCPUUsageThresholdExceededTrap.setStatus(
        "current"
    )

ruckusSZMemoryUsageThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 7)
)
ruckusSZMemoryUsageThresholdExceededTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZMemoryPerc"))
)
if mibBuilder.loadTexts:
    ruckusSZMemoryUsageThresholdExceededTrap.setStatus(
        "current"
    )

ruckusSZDiskUsageThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 8)
)
ruckusSZDiskUsageThresholdExceededTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDiskPerc"))
)
if mibBuilder.loadTexts:
    ruckusSZDiskUsageThresholdExceededTrap.setStatus(
        "current"
    )

ruckusSZLicenseUsageThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 19)
)
ruckusSZLicenseUsageThresholdExceededTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLicenseType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLicenseUsagePerc"))
)
if mibBuilder.loadTexts:
    ruckusSZLicenseUsageThresholdExceededTrap.setStatus(
        "current"
    )

ruckusSZAPMiscEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 20)
)
ruckusSZAPMiscEventTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPMiscEventTrap.setStatus(
        "current"
    )

ruckusSZAPConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 21)
)
ruckusSZAPConnectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPConnectedTrap.setStatus(
        "current"
    )

ruckusSZAPDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 22)
)
ruckusSZAPDeletedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPDeletedTrap.setStatus(
        "current"
    )

ruckusSZAPDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 23)
)
ruckusSZAPDisconnectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPDisconnectedTrap.setStatus(
        "current"
    )

ruckusSZAPLostHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 24)
)
ruckusSZAPLostHeartbeatTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPLostHeartbeatTrap.setStatus(
        "current"
    )

ruckusSZAPRebootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 25)
)
ruckusSZAPRebootTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPRebootTrap.setStatus(
        "current"
    )

ruckusSZCriticalAPConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 26)
)
ruckusSZCriticalAPConnectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZCriticalAPConnectedTrap.setStatus(
        "current"
    )

ruckusSZCriticalAPDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 27)
)
ruckusSZCriticalAPDisconnectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZCriticalAPDisconnectedTrap.setStatus(
        "current"
    )

ruckusSZAPRejectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 28)
)
ruckusSZAPRejectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPRejectedTrap.setStatus(
        "current"
    )

ruckusSZAPConfUpdateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 29)
)
ruckusSZAPConfUpdateFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZAPConfigID"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPConfUpdateFailedTrap.setStatus(
        "current"
    )

ruckusSZAPConfUpdatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 30)
)
ruckusSZAPConfUpdatedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZAPConfigID"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPConfUpdatedTrap.setStatus(
        "current"
    )

ruckusSZAPSwapOutModelDiffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 31)
)
ruckusSZAPSwapOutModelDiffTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZAPModel"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZConfigAPModel"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPSwapOutModelDiffTrap.setStatus(
        "current"
    )

ruckusSZAPPreProvisionModelDiffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 32)
)
ruckusSZAPPreProvisionModelDiffTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZAPModel"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZConfigAPModel"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPPreProvisionModelDiffTrap.setStatus(
        "current"
    )

ruckusSZAPFirmwareUpdateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 34)
)
ruckusSZAPFirmwareUpdateFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPFirmwareUpdateFailedTrap.setStatus(
        "current"
    )

ruckusSZAPFirmwareUpdatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 35)
)
ruckusSZAPFirmwareUpdatedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPFirmwareUpdatedTrap.setStatus(
        "current"
    )

ruckusSZAPWlanOversubscribedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 36)
)
ruckusSZAPWlanOversubscribedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"))
)
if mibBuilder.loadTexts:
    ruckusSZAPWlanOversubscribedTrap.setStatus(
        "current"
    )

ruckusSZAPFactoryResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 37)
)
ruckusSZAPFactoryResetTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPFactoryResetTrap.setStatus(
        "current"
    )

ruckusSZCableModemDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 38)
)
ruckusSZCableModemDownTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZCableModemDownTrap.setStatus(
        "current"
    )

ruckusSZCableModemRebootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 39)
)
ruckusSZCableModemRebootTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZCableModemRebootTrap.setStatus(
        "current"
    )

ruckusSZAPManagedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 41)
)
ruckusSZAPManagedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"))
)
if mibBuilder.loadTexts:
    ruckusSZAPManagedTrap.setStatus(
        "current"
    )

ruckusSZCPUUsageThresholdBackToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 42)
)
ruckusSZCPUUsageThresholdBackToNormalTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZCPUPerc"))
)
if mibBuilder.loadTexts:
    ruckusSZCPUUsageThresholdBackToNormalTrap.setStatus(
        "current"
    )

ruckusSZMemoryUsageThresholdBackToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 43)
)
ruckusSZMemoryUsageThresholdBackToNormalTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZMemoryPerc"))
)
if mibBuilder.loadTexts:
    ruckusSZMemoryUsageThresholdBackToNormalTrap.setStatus(
        "current"
    )

ruckusSZDiskUsageThresholdBackToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 44)
)
ruckusSZDiskUsageThresholdBackToNormalTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDiskPerc"))
)
if mibBuilder.loadTexts:
    ruckusSZDiskUsageThresholdBackToNormalTrap.setStatus(
        "current"
    )

ruckusSZCableModemUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 45)
)
ruckusSZCableModemUpTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZCableModemUpTrap.setStatus(
        "current"
    )

ruckusSZAPDiscoverySuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 46)
)
ruckusSZAPDiscoverySuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPDiscoverySuccessTrap.setStatus(
        "current"
    )

ruckusSZCMResetByUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 47)
)
ruckusSZCMResetByUserTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZCMResetByUserTrap.setStatus(
        "current"
    )

ruckusSZCMResetFactoryByUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 48)
)
ruckusSZCMResetFactoryByUserTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZCMResetFactoryByUserTrap.setStatus(
        "current"
    )

ruckusSZSSIDSpoofingRogueAPDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 50)
)
ruckusSZSSIDSpoofingRogueAPDetectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventRogueMac"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSSID"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZSSIDSpoofingRogueAPDetectedTrap.setStatus(
        "current"
    )

ruckusSZMacSpoofingRogueAPDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 51)
)
ruckusSZMacSpoofingRogueAPDetectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventRogueMac"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSSID"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZMacSpoofingRogueAPDetectedTrap.setStatus(
        "current"
    )

ruckusSZSameNetworkRogueAPDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 52)
)
ruckusSZSameNetworkRogueAPDetectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventRogueMac"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSSID"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZSameNetworkRogueAPDetectedTrap.setStatus(
        "current"
    )

ruckusSZADHocNetworkRogueAPDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 53)
)
ruckusSZADHocNetworkRogueAPDetectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventRogueMac"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSSID"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZADHocNetworkRogueAPDetectedTrap.setStatus(
        "current"
    )

ruckusSZMaliciousRogueAPTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 54)
)
ruckusSZMaliciousRogueAPTimeoutTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventRogueMac"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZMaliciousRogueAPTimeoutTrap.setStatus(
        "current"
    )

ruckusSZAPLBSConnectSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 55)
)
ruckusSZAPLBSConnectSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSURL"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSPort"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPLBSConnectSuccessTrap.setStatus(
        "current"
    )

ruckusSZAPLBSNoResponsesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 56)
)
ruckusSZAPLBSNoResponsesTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSURL"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSPort"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPLBSNoResponsesTrap.setStatus(
        "current"
    )

ruckusSZAPLBSAuthFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 57)
)
ruckusSZAPLBSAuthFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSURL"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSPort"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPLBSAuthFailedTrap.setStatus(
        "current"
    )

ruckusSZAPLBSConnectFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 58)
)
ruckusSZAPLBSConnectFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSURL"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSPort"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPLBSConnectFailedTrap.setStatus(
        "current"
    )

ruckusSZAPTunnelBuildFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 60)
)
ruckusSZAPTunnelBuildFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPTunnelBuildFailedTrap.setStatus(
        "current"
    )

ruckusSZAPTunnelBuildSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 61)
)
ruckusSZAPTunnelBuildSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPTunnelBuildSuccessTrap.setStatus(
        "current"
    )

ruckusSZAPTunnelDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 62)
)
ruckusSZAPTunnelDisconnectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPTunnelDisconnectedTrap.setStatus(
        "current"
    )

ruckusSZAPSoftGRETunnelFailoverPtoSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 65)
)
ruckusSZAPSoftGRETunnelFailoverPtoSTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusPrimaryGRE"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSecondaryGRE"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPSoftGRETunnelFailoverPtoSTrap.setStatus(
        "current"
    )

ruckusSZAPSoftGRETunnelFailoverStoPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 66)
)
ruckusSZAPSoftGRETunnelFailoverStoPTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusPrimaryGRE"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSecondaryGRE"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPSoftGRETunnelFailoverStoPTrap.setStatus(
        "current"
    )

ruckusSZAPSoftGREGatewayNotReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 67)
)
ruckusSZAPSoftGREGatewayNotReachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSoftGREGatewayList"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPSoftGREGatewayNotReachableTrap.setStatus(
        "current"
    )

ruckusSZAPSoftGREGatewayReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 68)
)
ruckusSZAPSoftGREGatewayReachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSoftGREGWAddress"))
)
if mibBuilder.loadTexts:
    ruckusSZAPSoftGREGatewayReachableTrap.setStatus(
        "current"
    )

ruckusSZDPConfUpdateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 70)
)
ruckusSZDPConfUpdateFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPConfigID"))
)
if mibBuilder.loadTexts:
    ruckusSZDPConfUpdateFailedTrap.setStatus(
        "current"
    )

ruckusSZDPLostHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 71)
)
ruckusSZDPLostHeartbeatTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"))
)
if mibBuilder.loadTexts:
    ruckusSZDPLostHeartbeatTrap.setStatus(
        "current"
    )

ruckusSZDPDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 72)
)
ruckusSZDPDisconnectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"))
)
if mibBuilder.loadTexts:
    ruckusSZDPDisconnectedTrap.setStatus(
        "current"
    )

ruckusSZDPPhyInterfaceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 73)
)
ruckusSZDPPhyInterfaceDownTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZNetworkPortID"))
)
if mibBuilder.loadTexts:
    ruckusSZDPPhyInterfaceDownTrap.setStatus(
        "current"
    )

ruckusSZDPStatusUpdateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 74)
)
ruckusSZDPStatusUpdateFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"))
)
if mibBuilder.loadTexts:
    ruckusSZDPStatusUpdateFailedTrap.setStatus(
        "current"
    )

ruckusSZDPStatisticUpdateFaliedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 75)
)
ruckusSZDPStatisticUpdateFaliedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"))
)
if mibBuilder.loadTexts:
    ruckusSZDPStatisticUpdateFaliedTrap.setStatus(
        "current"
    )

ruckusSZDPConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 76)
)
ruckusSZDPConnectedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"))
)
if mibBuilder.loadTexts:
    ruckusSZDPConnectedTrap.setStatus(
        "current"
    )

ruckusSZDPPhyInterfaceUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 77)
)
ruckusSZDPPhyInterfaceUpTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZNetworkPortID"))
)
if mibBuilder.loadTexts:
    ruckusSZDPPhyInterfaceUpTrap.setStatus(
        "current"
    )

ruckusSZDPConfUpdatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 78)
)
ruckusSZDPConfUpdatedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPConfigID"))
)
if mibBuilder.loadTexts:
    ruckusSZDPConfUpdatedTrap.setStatus(
        "current"
    )

ruckusSZDPTunnelTearDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 79)
)
ruckusSZDPTunnelTearDownTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"))
)
if mibBuilder.loadTexts:
    ruckusSZDPTunnelTearDownTrap.setStatus(
        "current"
    )

ruckusSZDPAcceptTunnelRequestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 81)
)
ruckusSZDPAcceptTunnelRequestTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZDPAcceptTunnelRequestTrap.setStatus(
        "current"
    )

ruckusSZDPRejectTunnelRequestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 82)
)
ruckusSZDPRejectTunnelRequestTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"))
)
if mibBuilder.loadTexts:
    ruckusSZDPRejectTunnelRequestTrap.setStatus(
        "current"
    )

ruckusSZDPTunnelSetUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 85)
)
ruckusSZDPTunnelSetUpTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZDPTunnelSetUpTrap.setStatus(
        "current"
    )

ruckusSZDPDiscoverySuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 86)
)
ruckusSZDPDiscoverySuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"))
)
if mibBuilder.loadTexts:
    ruckusSZDPDiscoverySuccessTrap.setStatus(
        "current"
    )

ruckusSZDPDiscoveryFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 87)
)
ruckusSZDPDiscoveryFailTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"))
)
if mibBuilder.loadTexts:
    ruckusSZDPDiscoveryFailTrap.setStatus(
        "current"
    )

ruckusSZDPDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 94)
)
ruckusSZDPDeletedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"))
)
if mibBuilder.loadTexts:
    ruckusSZDPDeletedTrap.setStatus(
        "current"
    )

ruckusSZDPUpgradeStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 95)
)
ruckusSZDPUpgradeStartTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"))
)
if mibBuilder.loadTexts:
    ruckusSZDPUpgradeStartTrap.setStatus(
        "current"
    )

ruckusSZDPUpgradingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 96)
)
ruckusSZDPUpgradingTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"))
)
if mibBuilder.loadTexts:
    ruckusSZDPUpgradingTrap.setStatus(
        "current"
    )

ruckusSZDPUpgradeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 97)
)
ruckusSZDPUpgradeSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"))
)
if mibBuilder.loadTexts:
    ruckusSZDPUpgradeSuccessTrap.setStatus(
        "current"
    )

ruckusSZDPUpgradeFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 98)
)
ruckusSZDPUpgradeFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPKey"))
)
if mibBuilder.loadTexts:
    ruckusSZDPUpgradeFailedTrap.setStatus(
        "current"
    )

ruckusSZClientMiscEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 100)
)
ruckusSZClientMiscEventTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventClientMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventDescription"))
)
if mibBuilder.loadTexts:
    ruckusSZClientMiscEventTrap.setStatus(
        "current"
    )

ruckusSZNodeJoinFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 200)
)
ruckusSZNodeJoinFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZNodeJoinFailedTrap.setStatus(
        "current"
    )

ruckusSZNodeRemoveFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 201)
)
ruckusSZNodeRemoveFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZNodeRemoveFailedTrap.setStatus(
        "current"
    )

ruckusSZNodeOutOfServiceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 202)
)
ruckusSZNodeOutOfServiceTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZNodeOutOfServiceTrap.setStatus(
        "current"
    )

ruckusSZClusterInMaintenanceStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 203)
)
ruckusSZClusterInMaintenanceStateTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterInMaintenanceStateTrap.setStatus(
        "current"
    )

ruckusSZClusterBackupFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 204)
)
ruckusSZClusterBackupFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterBackupFailedTrap.setStatus(
        "current"
    )

ruckusSZClusterRestoreFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 205)
)
ruckusSZClusterRestoreFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterRestoreFailedTrap.setStatus(
        "current"
    )

ruckusSZClusterAppStoppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 206)
)
ruckusSZClusterAppStoppedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZProcessName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterAppStoppedTrap.setStatus(
        "current"
    )

ruckusSZNodeBondInterfaceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 207)
)
ruckusSZNodeBondInterfaceDownTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZNetworkInterface"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZNodeBondInterfaceDownTrap.setStatus(
        "current"
    )

ruckusSZNodePhyInterfaceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 208)
)
ruckusSZNodePhyInterfaceDownTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZNetworkInterface"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZNodePhyInterfaceDownTrap.setStatus(
        "current"
    )

ruckusSZClusterLeaderChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 209)
)
ruckusSZClusterLeaderChangedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterLeaderChangedTrap.setStatus(
        "current"
    )

ruckusSZClusterUpgradeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 210)
)
ruckusSZClusterUpgradeSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventFirmwareVersion"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventUpgradedFirmwareVersion"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterUpgradeSuccessTrap.setStatus(
        "current"
    )

ruckusSZNodeBondInterfaceUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 211)
)
ruckusSZNodeBondInterfaceUpTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZNetworkInterface"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZNodeBondInterfaceUpTrap.setStatus(
        "current"
    )

ruckusSZNodePhyInterfaceUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 212)
)
ruckusSZNodePhyInterfaceUpTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZNetworkInterface"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZNodePhyInterfaceUpTrap.setStatus(
        "current"
    )

ruckusSZClusterBackToInServiceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 216)
)
ruckusSZClusterBackToInServiceTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterBackToInServiceTrap.setStatus(
        "current"
    )

ruckusSZBackupClusterSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 217)
)
ruckusSZBackupClusterSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZBackupClusterSuccessTrap.setStatus(
        "current"
    )

ruckusSZNodeJoinSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 218)
)
ruckusSZNodeJoinSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZNodeJoinSuccessTrap.setStatus(
        "current"
    )

ruckusSZClusterAppStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 219)
)
ruckusSZClusterAppStartTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZProcessName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterAppStartTrap.setStatus(
        "current"
    )

ruckusSZNodeRemoveSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 220)
)
ruckusSZNodeRemoveSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZNodeRemoveSuccessTrap.setStatus(
        "current"
    )

ruckusSZClusterRestoreSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 221)
)
ruckusSZClusterRestoreSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterRestoreSuccessTrap.setStatus(
        "current"
    )

ruckusSZNodeBackToInServiceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 222)
)
ruckusSZNodeBackToInServiceTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZNodeBackToInServiceTrap.setStatus(
        "current"
    )

ruckusSZSshTunnelSwitchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 223)
)
ruckusSZSshTunnelSwitchedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSwitchStatus"))
)
if mibBuilder.loadTexts:
    ruckusSZSshTunnelSwitchedTrap.setStatus(
        "current"
    )

ruckusSZClusterCfgBackupStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 224)
)
ruckusSZClusterCfgBackupStartTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterCfgBackupStartTrap.setStatus(
        "current"
    )

ruckusSZClusterCfgBackupSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 225)
)
ruckusSZClusterCfgBackupSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterCfgBackupSuccessTrap.setStatus(
        "current"
    )

ruckusSZClusterCfgBackupFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 226)
)
ruckusSZClusterCfgBackupFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterCfgBackupFailedTrap.setStatus(
        "current"
    )

ruckusSZClusterCfgRestoreSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 227)
)
ruckusSZClusterCfgRestoreSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterCfgRestoreSuccessTrap.setStatus(
        "current"
    )

ruckusSZClusterCfgRestoreFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 228)
)
ruckusSZClusterCfgRestoreFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterCfgRestoreFailedTrap.setStatus(
        "current"
    )

ruckusSZClusterUploadSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 229)
)
ruckusSZClusterUploadSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterUploadSuccessTrap.setStatus(
        "current"
    )

ruckusSZClusterUploadFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 230)
)
ruckusSZClusterUploadFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterUploadFailedTrap.setStatus(
        "current"
    )

ruckusSZClusterOutOfServiceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 231)
)
ruckusSZClusterOutOfServiceTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterOutOfServiceTrap.setStatus(
        "current"
    )

ruckusSZClusterUploadVDPFirmwareStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 232)
)
ruckusSZClusterUploadVDPFirmwareStartTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterUploadVDPFirmwareStartTrap.setStatus(
        "current"
    )

ruckusSZClusterUploadVDPFirmwareSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 233)
)
ruckusSZClusterUploadVDPFirmwareSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterUploadVDPFirmwareSuccessTrap.setStatus(
        "current"
    )

ruckusSZClusterUploadVDPFirmwareFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 234)
)
ruckusSZClusterUploadVDPFirmwareFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZClusterName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"))
)
if mibBuilder.loadTexts:
    ruckusSZClusterUploadVDPFirmwareFailedTrap.setStatus(
        "current"
    )

ruckusSZIpmiTempBBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 251)
)
ruckusSZIpmiTempBBTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZTemperatureStatus"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZIpmiTempBBTrap.setStatus(
        "current"
    )

ruckusSZIpmiTempPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 256)
)
ruckusSZIpmiTempPTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZProcessorId"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZTemperatureStatus"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZIpmiTempPTrap.setStatus(
        "current"
    )

ruckusSZIpmiFanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 258)
)
ruckusSZIpmiFanTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZFanId"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZFanStatus"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZIpmiFanTrap.setStatus(
        "current"
    )

ruckusSZIpmiFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 261)
)
ruckusSZIpmiFanStatusTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZFanId"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZFanStatus"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZIpmiFanStatusTrap.setStatus(
        "current"
    )

ruckusSZIpmiRETempBBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 265)
)
ruckusSZIpmiRETempBBTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZTemperatureStatus"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZIpmiRETempBBTrap.setStatus(
        "current"
    )

ruckusSZIpmiRETempPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 270)
)
ruckusSZIpmiRETempPTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZProcessorId"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZTemperatureStatus"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZIpmiRETempPTrap.setStatus(
        "current"
    )

ruckusSZIpmiREFanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 272)
)
ruckusSZIpmiREFanTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZFanId"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZFanStatus"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZIpmiREFanTrap.setStatus(
        "current"
    )

ruckusSZIpmiREFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 275)
)
ruckusSZIpmiREFanStatusTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZFanId"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZFanStatus"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZIpmiREFanStatusTrap.setStatus(
        "current"
    )

ruckusSZFtpTransferErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 280)
)
ruckusSZFtpTransferErrorTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZFtpIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZFtpPort"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZFileName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZFtpTransferErrorTrap.setStatus(
        "current"
    )

ruckusSZSystemLBSConnectSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 290)
)
ruckusSZSystemLBSConnectSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSURL"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSPort"))
)
if mibBuilder.loadTexts:
    ruckusSZSystemLBSConnectSuccessTrap.setStatus(
        "current"
    )

ruckusSZSystemLBSNoResponseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 291)
)
ruckusSZSystemLBSNoResponseTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSURL"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSPort"))
)
if mibBuilder.loadTexts:
    ruckusSZSystemLBSNoResponseTrap.setStatus(
        "current"
    )

ruckusSZSystemLBSAuthFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 292)
)
ruckusSZSystemLBSAuthFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSURL"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSPort"))
)
if mibBuilder.loadTexts:
    ruckusSZSystemLBSAuthFailedTrap.setStatus(
        "current"
    )

ruckusSZSystemLBSConnectFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 293)
)
ruckusSZSystemLBSConnectFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSURL"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLBSPort"))
)
if mibBuilder.loadTexts:
    ruckusSZSystemLBSConnectFailedTrap.setStatus(
        "current"
    )

ruckusSZProcessRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 300)
)
ruckusSZProcessRestartTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZProcessName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZProcessRestartTrap.setStatus(
        "current"
    )

ruckusSZServiceUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 301)
)
ruckusSZServiceUnavailableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZProcessName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZServiceUnavailableTrap.setStatus(
        "current"
    )

ruckusSZKeepAliveFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 302)
)
ruckusSZKeepAliveFailureTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSrcProcess"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZProcessName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZKeepAliveFailureTrap.setStatus(
        "current"
    )

ruckusSZResourceUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 304)
)
ruckusSZResourceUnavailableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSrcProcess"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"))
)
if mibBuilder.loadTexts:
    ruckusSZResourceUnavailableTrap.setStatus(
        "current"
    )

ruckusSZSmfRegFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 305)
)
ruckusSZSmfRegFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSrcProcess"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZSmfRegFailedTrap.setStatus(
        "current"
    )

ruckusSZHipFailoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 306)
)
ruckusSZHipFailoverTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSrcProcess"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZHipFailoverTrap.setStatus(
        "current"
    )

ruckusSZConfUpdFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 307)
)
ruckusSZConfUpdFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZProcessName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"))
)
if mibBuilder.loadTexts:
    ruckusSZConfUpdFailedTrap.setStatus(
        "current"
    )

ruckusSZConfRcvFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 308)
)
ruckusSZConfRcvFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"))
)
if mibBuilder.loadTexts:
    ruckusSZConfRcvFailedTrap.setStatus(
        "current"
    )

ruckusSZLostCnxnToDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 309)
)
ruckusSZLostCnxnToDbladeTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZLostCnxnToDbladeTrap.setStatus(
        "current"
    )

ruckusSZAuthSrvrNotReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 314)
)
ruckusSZAuthSrvrNotReachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZAuthSrvrIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZRadProxyIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZAuthSrvrNotReachableTrap.setStatus(
        "current"
    )

ruckusSZAccSrvrNotReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 315)
)
ruckusSZAccSrvrNotReachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZAccSrvrIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZRadProxyIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZAccSrvrNotReachableTrap.setStatus(
        "current"
    )

ruckusSZAuthFailedNonPermanentIDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 317)
)
ruckusSZAuthFailedNonPermanentIDTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUEImsi"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUEMsisdn"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventReason"))
)
if mibBuilder.loadTexts:
    ruckusSZAuthFailedNonPermanentIDTrap.setStatus(
        "current"
    )

ruckusSZAPAcctRespWhileInvalidConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 347)
)
ruckusSZAPAcctRespWhileInvalidConfigTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSrcProcess"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUserName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPAcctRespWhileInvalidConfigTrap.setStatus(
        "current"
    )

ruckusSZAPAcctMsgDropNoAcctStartMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 348)
)
ruckusSZAPAcctMsgDropNoAcctStartMsgTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSrcProcess"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUserName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPAcctMsgDropNoAcctStartMsgTrap.setStatus(
        "current"
    )

ruckusSZUnauthorizedCoaDmMessageDroppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 349)
)
ruckusSZUnauthorizedCoaDmMessageDroppedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSrcProcess"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZRadSrvrIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZUnauthorizedCoaDmMessageDroppedTrap.setStatus(
        "current"
    )

ruckusSZConnectedToDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 350)
)
ruckusSZConnectedToDbladeTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZConnectedToDbladeTrap.setStatus(
        "current"
    )

ruckusSZSessUpdatedAtDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 354)
)
ruckusSZSessUpdatedAtDbladeTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUEImsi"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUEMsisdn"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZSessUpdatedAtDbladeTrap.setStatus(
        "current"
    )

ruckusSZSessUpdateErrAtDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 355)
)
ruckusSZSessUpdateErrAtDbladeTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUEImsi"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUEMsisdn"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZSessUpdateErrAtDbladeTrap.setStatus(
        "current"
    )

ruckusSZSessDeletedAtDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 356)
)
ruckusSZSessDeletedAtDbladeTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUEImsi"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUEMsisdn"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZSessDeletedAtDbladeTrap.setStatus(
        "current"
    )

ruckusSZSessDeleteErrAtDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 357)
)
ruckusSZSessDeleteErrAtDbladeTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCtrlIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUEImsi"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZUEMsisdn"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeMgmtIp"))
)
if mibBuilder.loadTexts:
    ruckusSZSessDeleteErrAtDbladeTrap.setStatus(
        "current"
    )

ruckusSZLicenseSyncSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 358)
)
ruckusSZLicenseSyncSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLicenseServerName"))
)
if mibBuilder.loadTexts:
    ruckusSZLicenseSyncSuccessTrap.setStatus(
        "current"
    )

ruckusSZLicenseSyncFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 359)
)
ruckusSZLicenseSyncFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLicenseServerName"))
)
if mibBuilder.loadTexts:
    ruckusSZLicenseSyncFailedTrap.setStatus(
        "current"
    )

ruckusSZLicenseImportSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 360)
)
ruckusSZLicenseImportSuccessTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"))
)
if mibBuilder.loadTexts:
    ruckusSZLicenseImportSuccessTrap.setStatus(
        "current"
    )

ruckusSZLicenseImportFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 361)
)
ruckusSZLicenseImportFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventNodeName"))
)
if mibBuilder.loadTexts:
    ruckusSZLicenseImportFailedTrap.setStatus(
        "current"
    )

ruckusSZSyslogServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 370)
)
ruckusSZSyslogServerReachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSyslogServerAddress"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZSyslogServerReachableTrap.setStatus(
        "current"
    )

ruckusSZSyslogServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 371)
)
ruckusSZSyslogServerUnreachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSyslogServerAddress"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZSyslogServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSZSyslogServerSwitchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 372)
)
ruckusSZSyslogServerSwitchedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSrcSyslogServerAddress"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDestSyslogServerAddress"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusSZSyslogServerSwitchedTrap.setStatus(
        "current"
    )

ruckusSZAPRadiusServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 400)
)
ruckusSZAPRadiusServerReachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZRadSrvrIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPRadiusServerReachableTrap.setStatus(
        "current"
    )

ruckusSZAPRadiusServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 401)
)
ruckusSZAPRadiusServerUnreachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZRadSrvrIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPRadiusServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSZAPLDAPServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 402)
)
ruckusSZAPLDAPServerReachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLDAPSrvrIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPLDAPServerReachableTrap.setStatus(
        "current"
    )

ruckusSZAPLDAPServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 403)
)
ruckusSZAPLDAPServerUnreachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZLDAPSrvrIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPLDAPServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSZAPADServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 404)
)
ruckusSZAPADServerReachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZADSrvrIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPADServerReachableTrap.setStatus(
        "current"
    )

ruckusSZAPADServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 405)
)
ruckusSZAPADServerUnreachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZADSrvrIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPADServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSZAPUsbSoftwarePackageDownloadedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 406)
)
ruckusSZAPUsbSoftwarePackageDownloadedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSoftwareName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPUsbSoftwarePackageDownloadedTrap.setStatus(
        "current"
    )

ruckusSZAPUsbSoftwarePackageDownloadFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 407)
)
ruckusSZAPUsbSoftwarePackageDownloadFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZSoftwareName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZAPUsbSoftwarePackageDownloadFailedTrap.setStatus(
        "current"
    )

ruckusSZEspAuthServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 408)
)
ruckusSZEspAuthServerReachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZAuthSrvrIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZEspAuthServerReachableTrap.setStatus(
        "current"
    )

ruckusSZEspAuthServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 409)
)
ruckusSZEspAuthServerUnreachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZAuthSrvrIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZEspAuthServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSZEspAuthServerResolvableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 410)
)
ruckusSZEspAuthServerResolvableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDomainName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZEspAuthServerResolvableTrap.setStatus(
        "current"
    )

ruckusSZEspAuthServerUnResolvableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 411)
)
ruckusSZEspAuthServerUnResolvableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDomainName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZEspAuthServerUnResolvableTrap.setStatus(
        "current"
    )

ruckusSZEspDNATServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 412)
)
ruckusSZEspDNATServerReachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDNATIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZEspDNATServerReachableTrap.setStatus(
        "current"
    )

ruckusSZEspDNATServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 413)
)
ruckusSZEspDNATServerUnreachableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDNATIp"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZEspDNATServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSZEspDNATServerResolvableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 414)
)
ruckusSZEspDNATServerResolvableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDomainName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZEspDNATServerResolvableTrap.setStatus(
        "current"
    )

ruckusSZEspDNATServerUnresolvableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 415)
)
ruckusSZEspDNATServerUnresolvableTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZDomainName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZEspDNATServerUnresolvableTrap.setStatus(
        "current"
    )

ruckusRateLimitTORSurpassedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 500)
)
ruckusRateLimitTORSurpassedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZRadSrvrIp"))
)
if mibBuilder.loadTexts:
    ruckusRateLimitTORSurpassedTrap.setStatus(
        "current"
    )

ruckusSZIPSecTunnelAssociatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 600)
)
ruckusSZIPSecTunnelAssociatedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZIPSecGWAddress"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZIPSecTunnelAssociatedTrap.setStatus(
        "current"
    )

ruckusSZIPSecTunnelDisassociatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 601)
)
ruckusSZIPSecTunnelDisassociatedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZIPSecGWAddress"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZIPSecTunnelDisassociatedTrap.setStatus(
        "current"
    )

ruckusSZIPSecTunnelAssociateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 11, 1, 602)
)
ruckusSZIPSecTunnelAssociateFailedTrap.setObjects(
      *(("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventSeverity"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventCode"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventType"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPName"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPMacAddr"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIP"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPLocation"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPDescription"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPGPSCoordinates"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZIPSecGWAddress"),
        ("RUCKUS-SZ-EVENT-MIB", "ruckusSZEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSZIPSecTunnelAssociateFailedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-SZ-EVENT-MIB",
    **{"ruckusSZEventMIB": ruckusSZEventMIB,
       "ruckusSZEventTraps": ruckusSZEventTraps,
       "ruckusSZSystemMiscEventTrap": ruckusSZSystemMiscEventTrap,
       "ruckusSZUpgradeSuccessTrap": ruckusSZUpgradeSuccessTrap,
       "ruckusSZUpgradeFailedTrap": ruckusSZUpgradeFailedTrap,
       "ruckusSZNodeRestartedTrap": ruckusSZNodeRestartedTrap,
       "ruckusSZNodeShutdownTrap": ruckusSZNodeShutdownTrap,
       "ruckusSZCPUUsageThresholdExceededTrap": ruckusSZCPUUsageThresholdExceededTrap,
       "ruckusSZMemoryUsageThresholdExceededTrap": ruckusSZMemoryUsageThresholdExceededTrap,
       "ruckusSZDiskUsageThresholdExceededTrap": ruckusSZDiskUsageThresholdExceededTrap,
       "ruckusSZLicenseUsageThresholdExceededTrap": ruckusSZLicenseUsageThresholdExceededTrap,
       "ruckusSZAPMiscEventTrap": ruckusSZAPMiscEventTrap,
       "ruckusSZAPConnectedTrap": ruckusSZAPConnectedTrap,
       "ruckusSZAPDeletedTrap": ruckusSZAPDeletedTrap,
       "ruckusSZAPDisconnectedTrap": ruckusSZAPDisconnectedTrap,
       "ruckusSZAPLostHeartbeatTrap": ruckusSZAPLostHeartbeatTrap,
       "ruckusSZAPRebootTrap": ruckusSZAPRebootTrap,
       "ruckusSZCriticalAPConnectedTrap": ruckusSZCriticalAPConnectedTrap,
       "ruckusSZCriticalAPDisconnectedTrap": ruckusSZCriticalAPDisconnectedTrap,
       "ruckusSZAPRejectedTrap": ruckusSZAPRejectedTrap,
       "ruckusSZAPConfUpdateFailedTrap": ruckusSZAPConfUpdateFailedTrap,
       "ruckusSZAPConfUpdatedTrap": ruckusSZAPConfUpdatedTrap,
       "ruckusSZAPSwapOutModelDiffTrap": ruckusSZAPSwapOutModelDiffTrap,
       "ruckusSZAPPreProvisionModelDiffTrap": ruckusSZAPPreProvisionModelDiffTrap,
       "ruckusSZAPFirmwareUpdateFailedTrap": ruckusSZAPFirmwareUpdateFailedTrap,
       "ruckusSZAPFirmwareUpdatedTrap": ruckusSZAPFirmwareUpdatedTrap,
       "ruckusSZAPWlanOversubscribedTrap": ruckusSZAPWlanOversubscribedTrap,
       "ruckusSZAPFactoryResetTrap": ruckusSZAPFactoryResetTrap,
       "ruckusSZCableModemDownTrap": ruckusSZCableModemDownTrap,
       "ruckusSZCableModemRebootTrap": ruckusSZCableModemRebootTrap,
       "ruckusSZAPManagedTrap": ruckusSZAPManagedTrap,
       "ruckusSZCPUUsageThresholdBackToNormalTrap": ruckusSZCPUUsageThresholdBackToNormalTrap,
       "ruckusSZMemoryUsageThresholdBackToNormalTrap": ruckusSZMemoryUsageThresholdBackToNormalTrap,
       "ruckusSZDiskUsageThresholdBackToNormalTrap": ruckusSZDiskUsageThresholdBackToNormalTrap,
       "ruckusSZCableModemUpTrap": ruckusSZCableModemUpTrap,
       "ruckusSZAPDiscoverySuccessTrap": ruckusSZAPDiscoverySuccessTrap,
       "ruckusSZCMResetByUserTrap": ruckusSZCMResetByUserTrap,
       "ruckusSZCMResetFactoryByUserTrap": ruckusSZCMResetFactoryByUserTrap,
       "ruckusSZSSIDSpoofingRogueAPDetectedTrap": ruckusSZSSIDSpoofingRogueAPDetectedTrap,
       "ruckusSZMacSpoofingRogueAPDetectedTrap": ruckusSZMacSpoofingRogueAPDetectedTrap,
       "ruckusSZSameNetworkRogueAPDetectedTrap": ruckusSZSameNetworkRogueAPDetectedTrap,
       "ruckusSZADHocNetworkRogueAPDetectedTrap": ruckusSZADHocNetworkRogueAPDetectedTrap,
       "ruckusSZMaliciousRogueAPTimeoutTrap": ruckusSZMaliciousRogueAPTimeoutTrap,
       "ruckusSZAPLBSConnectSuccessTrap": ruckusSZAPLBSConnectSuccessTrap,
       "ruckusSZAPLBSNoResponsesTrap": ruckusSZAPLBSNoResponsesTrap,
       "ruckusSZAPLBSAuthFailedTrap": ruckusSZAPLBSAuthFailedTrap,
       "ruckusSZAPLBSConnectFailedTrap": ruckusSZAPLBSConnectFailedTrap,
       "ruckusSZAPTunnelBuildFailedTrap": ruckusSZAPTunnelBuildFailedTrap,
       "ruckusSZAPTunnelBuildSuccessTrap": ruckusSZAPTunnelBuildSuccessTrap,
       "ruckusSZAPTunnelDisconnectedTrap": ruckusSZAPTunnelDisconnectedTrap,
       "ruckusSZAPSoftGRETunnelFailoverPtoSTrap": ruckusSZAPSoftGRETunnelFailoverPtoSTrap,
       "ruckusSZAPSoftGRETunnelFailoverStoPTrap": ruckusSZAPSoftGRETunnelFailoverStoPTrap,
       "ruckusSZAPSoftGREGatewayNotReachableTrap": ruckusSZAPSoftGREGatewayNotReachableTrap,
       "ruckusSZAPSoftGREGatewayReachableTrap": ruckusSZAPSoftGREGatewayReachableTrap,
       "ruckusSZDPConfUpdateFailedTrap": ruckusSZDPConfUpdateFailedTrap,
       "ruckusSZDPLostHeartbeatTrap": ruckusSZDPLostHeartbeatTrap,
       "ruckusSZDPDisconnectedTrap": ruckusSZDPDisconnectedTrap,
       "ruckusSZDPPhyInterfaceDownTrap": ruckusSZDPPhyInterfaceDownTrap,
       "ruckusSZDPStatusUpdateFailedTrap": ruckusSZDPStatusUpdateFailedTrap,
       "ruckusSZDPStatisticUpdateFaliedTrap": ruckusSZDPStatisticUpdateFaliedTrap,
       "ruckusSZDPConnectedTrap": ruckusSZDPConnectedTrap,
       "ruckusSZDPPhyInterfaceUpTrap": ruckusSZDPPhyInterfaceUpTrap,
       "ruckusSZDPConfUpdatedTrap": ruckusSZDPConfUpdatedTrap,
       "ruckusSZDPTunnelTearDownTrap": ruckusSZDPTunnelTearDownTrap,
       "ruckusSZDPAcceptTunnelRequestTrap": ruckusSZDPAcceptTunnelRequestTrap,
       "ruckusSZDPRejectTunnelRequestTrap": ruckusSZDPRejectTunnelRequestTrap,
       "ruckusSZDPTunnelSetUpTrap": ruckusSZDPTunnelSetUpTrap,
       "ruckusSZDPDiscoverySuccessTrap": ruckusSZDPDiscoverySuccessTrap,
       "ruckusSZDPDiscoveryFailTrap": ruckusSZDPDiscoveryFailTrap,
       "ruckusSZDPDeletedTrap": ruckusSZDPDeletedTrap,
       "ruckusSZDPUpgradeStartTrap": ruckusSZDPUpgradeStartTrap,
       "ruckusSZDPUpgradingTrap": ruckusSZDPUpgradingTrap,
       "ruckusSZDPUpgradeSuccessTrap": ruckusSZDPUpgradeSuccessTrap,
       "ruckusSZDPUpgradeFailedTrap": ruckusSZDPUpgradeFailedTrap,
       "ruckusSZClientMiscEventTrap": ruckusSZClientMiscEventTrap,
       "ruckusSZNodeJoinFailedTrap": ruckusSZNodeJoinFailedTrap,
       "ruckusSZNodeRemoveFailedTrap": ruckusSZNodeRemoveFailedTrap,
       "ruckusSZNodeOutOfServiceTrap": ruckusSZNodeOutOfServiceTrap,
       "ruckusSZClusterInMaintenanceStateTrap": ruckusSZClusterInMaintenanceStateTrap,
       "ruckusSZClusterBackupFailedTrap": ruckusSZClusterBackupFailedTrap,
       "ruckusSZClusterRestoreFailedTrap": ruckusSZClusterRestoreFailedTrap,
       "ruckusSZClusterAppStoppedTrap": ruckusSZClusterAppStoppedTrap,
       "ruckusSZNodeBondInterfaceDownTrap": ruckusSZNodeBondInterfaceDownTrap,
       "ruckusSZNodePhyInterfaceDownTrap": ruckusSZNodePhyInterfaceDownTrap,
       "ruckusSZClusterLeaderChangedTrap": ruckusSZClusterLeaderChangedTrap,
       "ruckusSZClusterUpgradeSuccessTrap": ruckusSZClusterUpgradeSuccessTrap,
       "ruckusSZNodeBondInterfaceUpTrap": ruckusSZNodeBondInterfaceUpTrap,
       "ruckusSZNodePhyInterfaceUpTrap": ruckusSZNodePhyInterfaceUpTrap,
       "ruckusSZClusterBackToInServiceTrap": ruckusSZClusterBackToInServiceTrap,
       "ruckusSZBackupClusterSuccessTrap": ruckusSZBackupClusterSuccessTrap,
       "ruckusSZNodeJoinSuccessTrap": ruckusSZNodeJoinSuccessTrap,
       "ruckusSZClusterAppStartTrap": ruckusSZClusterAppStartTrap,
       "ruckusSZNodeRemoveSuccessTrap": ruckusSZNodeRemoveSuccessTrap,
       "ruckusSZClusterRestoreSuccessTrap": ruckusSZClusterRestoreSuccessTrap,
       "ruckusSZNodeBackToInServiceTrap": ruckusSZNodeBackToInServiceTrap,
       "ruckusSZSshTunnelSwitchedTrap": ruckusSZSshTunnelSwitchedTrap,
       "ruckusSZClusterCfgBackupStartTrap": ruckusSZClusterCfgBackupStartTrap,
       "ruckusSZClusterCfgBackupSuccessTrap": ruckusSZClusterCfgBackupSuccessTrap,
       "ruckusSZClusterCfgBackupFailedTrap": ruckusSZClusterCfgBackupFailedTrap,
       "ruckusSZClusterCfgRestoreSuccessTrap": ruckusSZClusterCfgRestoreSuccessTrap,
       "ruckusSZClusterCfgRestoreFailedTrap": ruckusSZClusterCfgRestoreFailedTrap,
       "ruckusSZClusterUploadSuccessTrap": ruckusSZClusterUploadSuccessTrap,
       "ruckusSZClusterUploadFailedTrap": ruckusSZClusterUploadFailedTrap,
       "ruckusSZClusterOutOfServiceTrap": ruckusSZClusterOutOfServiceTrap,
       "ruckusSZClusterUploadVDPFirmwareStartTrap": ruckusSZClusterUploadVDPFirmwareStartTrap,
       "ruckusSZClusterUploadVDPFirmwareSuccessTrap": ruckusSZClusterUploadVDPFirmwareSuccessTrap,
       "ruckusSZClusterUploadVDPFirmwareFailedTrap": ruckusSZClusterUploadVDPFirmwareFailedTrap,
       "ruckusSZIpmiTempBBTrap": ruckusSZIpmiTempBBTrap,
       "ruckusSZIpmiTempPTrap": ruckusSZIpmiTempPTrap,
       "ruckusSZIpmiFanTrap": ruckusSZIpmiFanTrap,
       "ruckusSZIpmiFanStatusTrap": ruckusSZIpmiFanStatusTrap,
       "ruckusSZIpmiRETempBBTrap": ruckusSZIpmiRETempBBTrap,
       "ruckusSZIpmiRETempPTrap": ruckusSZIpmiRETempPTrap,
       "ruckusSZIpmiREFanTrap": ruckusSZIpmiREFanTrap,
       "ruckusSZIpmiREFanStatusTrap": ruckusSZIpmiREFanStatusTrap,
       "ruckusSZFtpTransferErrorTrap": ruckusSZFtpTransferErrorTrap,
       "ruckusSZSystemLBSConnectSuccessTrap": ruckusSZSystemLBSConnectSuccessTrap,
       "ruckusSZSystemLBSNoResponseTrap": ruckusSZSystemLBSNoResponseTrap,
       "ruckusSZSystemLBSAuthFailedTrap": ruckusSZSystemLBSAuthFailedTrap,
       "ruckusSZSystemLBSConnectFailedTrap": ruckusSZSystemLBSConnectFailedTrap,
       "ruckusSZProcessRestartTrap": ruckusSZProcessRestartTrap,
       "ruckusSZServiceUnavailableTrap": ruckusSZServiceUnavailableTrap,
       "ruckusSZKeepAliveFailureTrap": ruckusSZKeepAliveFailureTrap,
       "ruckusSZResourceUnavailableTrap": ruckusSZResourceUnavailableTrap,
       "ruckusSZSmfRegFailedTrap": ruckusSZSmfRegFailedTrap,
       "ruckusSZHipFailoverTrap": ruckusSZHipFailoverTrap,
       "ruckusSZConfUpdFailedTrap": ruckusSZConfUpdFailedTrap,
       "ruckusSZConfRcvFailedTrap": ruckusSZConfRcvFailedTrap,
       "ruckusSZLostCnxnToDbladeTrap": ruckusSZLostCnxnToDbladeTrap,
       "ruckusSZAuthSrvrNotReachableTrap": ruckusSZAuthSrvrNotReachableTrap,
       "ruckusSZAccSrvrNotReachableTrap": ruckusSZAccSrvrNotReachableTrap,
       "ruckusSZAuthFailedNonPermanentIDTrap": ruckusSZAuthFailedNonPermanentIDTrap,
       "ruckusSZAPAcctRespWhileInvalidConfigTrap": ruckusSZAPAcctRespWhileInvalidConfigTrap,
       "ruckusSZAPAcctMsgDropNoAcctStartMsgTrap": ruckusSZAPAcctMsgDropNoAcctStartMsgTrap,
       "ruckusSZUnauthorizedCoaDmMessageDroppedTrap": ruckusSZUnauthorizedCoaDmMessageDroppedTrap,
       "ruckusSZConnectedToDbladeTrap": ruckusSZConnectedToDbladeTrap,
       "ruckusSZSessUpdatedAtDbladeTrap": ruckusSZSessUpdatedAtDbladeTrap,
       "ruckusSZSessUpdateErrAtDbladeTrap": ruckusSZSessUpdateErrAtDbladeTrap,
       "ruckusSZSessDeletedAtDbladeTrap": ruckusSZSessDeletedAtDbladeTrap,
       "ruckusSZSessDeleteErrAtDbladeTrap": ruckusSZSessDeleteErrAtDbladeTrap,
       "ruckusSZLicenseSyncSuccessTrap": ruckusSZLicenseSyncSuccessTrap,
       "ruckusSZLicenseSyncFailedTrap": ruckusSZLicenseSyncFailedTrap,
       "ruckusSZLicenseImportSuccessTrap": ruckusSZLicenseImportSuccessTrap,
       "ruckusSZLicenseImportFailedTrap": ruckusSZLicenseImportFailedTrap,
       "ruckusSZSyslogServerReachableTrap": ruckusSZSyslogServerReachableTrap,
       "ruckusSZSyslogServerUnreachableTrap": ruckusSZSyslogServerUnreachableTrap,
       "ruckusSZSyslogServerSwitchedTrap": ruckusSZSyslogServerSwitchedTrap,
       "ruckusSZAPRadiusServerReachableTrap": ruckusSZAPRadiusServerReachableTrap,
       "ruckusSZAPRadiusServerUnreachableTrap": ruckusSZAPRadiusServerUnreachableTrap,
       "ruckusSZAPLDAPServerReachableTrap": ruckusSZAPLDAPServerReachableTrap,
       "ruckusSZAPLDAPServerUnreachableTrap": ruckusSZAPLDAPServerUnreachableTrap,
       "ruckusSZAPADServerReachableTrap": ruckusSZAPADServerReachableTrap,
       "ruckusSZAPADServerUnreachableTrap": ruckusSZAPADServerUnreachableTrap,
       "ruckusSZAPUsbSoftwarePackageDownloadedTrap": ruckusSZAPUsbSoftwarePackageDownloadedTrap,
       "ruckusSZAPUsbSoftwarePackageDownloadFailedTrap": ruckusSZAPUsbSoftwarePackageDownloadFailedTrap,
       "ruckusSZEspAuthServerReachableTrap": ruckusSZEspAuthServerReachableTrap,
       "ruckusSZEspAuthServerUnreachableTrap": ruckusSZEspAuthServerUnreachableTrap,
       "ruckusSZEspAuthServerResolvableTrap": ruckusSZEspAuthServerResolvableTrap,
       "ruckusSZEspAuthServerUnResolvableTrap": ruckusSZEspAuthServerUnResolvableTrap,
       "ruckusSZEspDNATServerReachableTrap": ruckusSZEspDNATServerReachableTrap,
       "ruckusSZEspDNATServerUnreachableTrap": ruckusSZEspDNATServerUnreachableTrap,
       "ruckusSZEspDNATServerResolvableTrap": ruckusSZEspDNATServerResolvableTrap,
       "ruckusSZEspDNATServerUnresolvableTrap": ruckusSZEspDNATServerUnresolvableTrap,
       "ruckusRateLimitTORSurpassedTrap": ruckusRateLimitTORSurpassedTrap,
       "ruckusSZIPSecTunnelAssociatedTrap": ruckusSZIPSecTunnelAssociatedTrap,
       "ruckusSZIPSecTunnelDisassociatedTrap": ruckusSZIPSecTunnelDisassociatedTrap,
       "ruckusSZIPSecTunnelAssociateFailedTrap": ruckusSZIPSecTunnelAssociateFailedTrap,
       "ruckusSZEventObjects": ruckusSZEventObjects,
       "ruckusSZEventDescription": ruckusSZEventDescription,
       "ruckusSZClusterName": ruckusSZClusterName,
       "ruckusSZEventCode": ruckusSZEventCode,
       "ruckusSZProcessName": ruckusSZProcessName,
       "ruckusSZEventCtrlIP": ruckusSZEventCtrlIP,
       "ruckusSZEventSeverity": ruckusSZEventSeverity,
       "ruckusSZEventType": ruckusSZEventType,
       "ruckusSZEventNodeMgmtIp": ruckusSZEventNodeMgmtIp,
       "ruckusSZEventNodeName": ruckusSZEventNodeName,
       "ruckusSZCPUPerc": ruckusSZCPUPerc,
       "ruckusSZMemoryPerc": ruckusSZMemoryPerc,
       "ruckusSZDiskPerc": ruckusSZDiskPerc,
       "ruckusSZEventMacAddr": ruckusSZEventMacAddr,
       "ruckusSZEventFirmwareVersion": ruckusSZEventFirmwareVersion,
       "ruckusSZEventUpgradedFirmwareVersion": ruckusSZEventUpgradedFirmwareVersion,
       "ruckusSZEventAPMacAddr": ruckusSZEventAPMacAddr,
       "ruckusSZEventReason": ruckusSZEventReason,
       "ruckusSZEventAPName": ruckusSZEventAPName,
       "ruckusSZEventAPIP": ruckusSZEventAPIP,
       "ruckusSZEventAPLocation": ruckusSZEventAPLocation,
       "ruckusSZEventAPGPSCoordinates": ruckusSZEventAPGPSCoordinates,
       "ruckusSZEventAPDescription": ruckusSZEventAPDescription,
       "ruckusSZAPModel": ruckusSZAPModel,
       "ruckusSZConfigAPModel": ruckusSZConfigAPModel,
       "ruckusSZAPConfigID": ruckusSZAPConfigID,
       "ruckusSZEventAPIPv6": ruckusSZEventAPIPv6,
       "ruckusSZLBSURL": ruckusSZLBSURL,
       "ruckusSZLBSPort": ruckusSZLBSPort,
       "ruckusSZEventSSID": ruckusSZEventSSID,
       "ruckusSZEventRogueMac": ruckusSZEventRogueMac,
       "ruckusPrimaryGRE": ruckusPrimaryGRE,
       "ruckusSecondaryGRE": ruckusSecondaryGRE,
       "ruckusSoftGREGatewayList": ruckusSoftGREGatewayList,
       "ruckusSZSoftGREGWAddress": ruckusSZSoftGREGWAddress,
       "ruckusSZEventClientMacAddr": ruckusSZEventClientMacAddr,
       "ruckusSZDPKey": ruckusSZDPKey,
       "ruckusSZDPConfigID": ruckusSZDPConfigID,
       "ruckusSZDPIP": ruckusSZDPIP,
       "ruckusSZNetworkPortID": ruckusSZNetworkPortID,
       "ruckusSZNetworkInterface": ruckusSZNetworkInterface,
       "ruckusSZSwitchStatus": ruckusSZSwitchStatus,
       "ruckusSZTemperatureStatus": ruckusSZTemperatureStatus,
       "ruckusSZProcessorId": ruckusSZProcessorId,
       "ruckusSZFanId": ruckusSZFanId,
       "ruckusSZFanStatus": ruckusSZFanStatus,
       "ruckusSZLicenseType": ruckusSZLicenseType,
       "ruckusSZLicenseUsagePerc": ruckusSZLicenseUsagePerc,
       "ruckusSZLicenseServerName": ruckusSZLicenseServerName,
       "ruckusSZIPSecGWAddress": ruckusSZIPSecGWAddress,
       "ruckusSZSyslogServerAddress": ruckusSZSyslogServerAddress,
       "ruckusSZSrcSyslogServerAddress": ruckusSZSrcSyslogServerAddress,
       "ruckusSZDestSyslogServerAddress": ruckusSZDestSyslogServerAddress,
       "ruckusSZFtpIp": ruckusSZFtpIp,
       "ruckusSZFtpPort": ruckusSZFtpPort,
       "ruckusSZSrcProcess": ruckusSZSrcProcess,
       "ruckusSZUEImsi": ruckusSZUEImsi,
       "ruckusSZUEMsisdn": ruckusSZUEMsisdn,
       "ruckusSZAuthSrvrIp": ruckusSZAuthSrvrIp,
       "ruckusSZRadProxyIp": ruckusSZRadProxyIp,
       "ruckusSZAccSrvrIp": ruckusSZAccSrvrIp,
       "ruckusSZRadSrvrIp": ruckusSZRadSrvrIp,
       "ruckusSZUserName": ruckusSZUserName,
       "ruckusSZFileName": ruckusSZFileName,
       "ruckusSZLDAPSrvrIp": ruckusSZLDAPSrvrIp,
       "ruckusSZADSrvrIp": ruckusSZADSrvrIp,
       "ruckusSZSoftwareName": ruckusSZSoftwareName,
       "ruckusSZDomainName": ruckusSZDomainName,
       "ruckusSZDNATIp": ruckusSZDNATIp}
)
