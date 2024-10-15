# SNMP MIB module (CTRON-SFPS-INCLUDE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-INCLUDE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:16 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4)
)
_CtronExp_ObjectIdentity = ObjectIdentity
ctronExp = _CtronExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2)
)
_CtronSwitch_ObjectIdentity = ObjectIdentity
ctronSwitch = _CtronSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4)
)
_SwitchCommon_ObjectIdentity = ObjectIdentity
switchCommon = _SwitchCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 1)
)
_SwitchSFPS_ObjectIdentity = ObjectIdentity
switchSFPS = _SwitchSFPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2)
)
_SfpsSwitchEngine_ObjectIdentity = ObjectIdentity
sfpsSwitchEngine = _SfpsSwitchEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1)
)
_SfpsSwitchSystem_ObjectIdentity = ObjectIdentity
sfpsSwitchSystem = _SfpsSwitchSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1)
)
_SfpsSystemConfig_ObjectIdentity = ObjectIdentity
sfpsSystemConfig = _SfpsSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1)
)
_SfpsSystemStats_ObjectIdentity = ObjectIdentity
sfpsSystemStats = _SfpsSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2)
)
_SfpsMemHeapStat_ObjectIdentity = ObjectIdentity
sfpsMemHeapStat = _SfpsMemHeapStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2)
)
_SfpsMemHeapStats_ObjectIdentity = ObjectIdentity
sfpsMemHeapStats = _SfpsMemHeapStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1)
)
_SfpsSystemGenerics_ObjectIdentity = ObjectIdentity
sfpsSystemGenerics = _SfpsSystemGenerics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3)
)
_SfpsSystemPool_ObjectIdentity = ObjectIdentity
sfpsSystemPool = _SfpsSystemPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4)
)
_SfpsAOProperties_ObjectIdentity = ObjectIdentity
sfpsAOProperties = _SfpsAOProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5)
)
_SfpsAOPropertiesAPI_ObjectIdentity = ObjectIdentity
sfpsAOPropertiesAPI = _SfpsAOPropertiesAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2)
)
_SfpsSystemSwitchChange_ObjectIdentity = ObjectIdentity
sfpsSystemSwitchChange = _SfpsSystemSwitchChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 6)
)
_SfpsSwitchPorts_ObjectIdentity = ObjectIdentity
sfpsSwitchPorts = _SfpsSwitchPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2)
)
_SfpsPortConfig_ObjectIdentity = ObjectIdentity
sfpsPortConfig = _SfpsPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1)
)
_SfpsPortAttribute_ObjectIdentity = ObjectIdentity
sfpsPortAttribute = _SfpsPortAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9)
)
_SfpsPortAttributeTable_ObjectIdentity = ObjectIdentity
sfpsPortAttributeTable = _SfpsPortAttributeTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 1)
)
_SfpsPortAttributeAPI_ObjectIdentity = ObjectIdentity
sfpsPortAttributeAPI = _SfpsPortAttributeAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 2)
)
_SfpsPortStats_ObjectIdentity = ObjectIdentity
sfpsPortStats = _SfpsPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2)
)
_SfpsSwitchConnections_ObjectIdentity = ObjectIdentity
sfpsSwitchConnections = _SfpsSwitchConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3)
)
_SfpsConnectionLookupAPI_ObjectIdentity = ObjectIdentity
sfpsConnectionLookupAPI = _SfpsConnectionLookupAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2)
)
_SfpsConnectionConfigAPI_ObjectIdentity = ObjectIdentity
sfpsConnectionConfigAPI = _SfpsConnectionConfigAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3)
)
_SfpsConnectionStats_ObjectIdentity = ObjectIdentity
sfpsConnectionStats = _SfpsConnectionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4)
)
_SfpsConnectionQueryAPI_ObjectIdentity = ObjectIdentity
sfpsConnectionQueryAPI = _SfpsConnectionQueryAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5)
)
_SfpsConnectionTestAPI_ObjectIdentity = ObjectIdentity
sfpsConnectionTestAPI = _SfpsConnectionTestAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 6)
)
_SfpsConnectionAPI_ObjectIdentity = ObjectIdentity
sfpsConnectionAPI = _SfpsConnectionAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4)
)
_SfpsGAPI_ObjectIdentity = ObjectIdentity
sfpsGAPI = _SfpsGAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 6)
)
_SfpsGAPIATM_ObjectIdentity = ObjectIdentity
sfpsGAPIATM = _SfpsGAPIATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 6, 6)
)
_SfpsSwitchSfpsPacket_ObjectIdentity = ObjectIdentity
sfpsSwitchSfpsPacket = _SfpsSwitchSfpsPacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7)
)
_SfpsPktDispatchStats_ObjectIdentity = ObjectIdentity
sfpsPktDispatchStats = _SfpsPktDispatchStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5)
)
_SfpsCSPPacket_ObjectIdentity = ObjectIdentity
sfpsCSPPacket = _SfpsCSPPacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10)
)
_SfpsCallTap_ObjectIdentity = ObjectIdentity
sfpsCallTap = _SfpsCallTap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11)
)
_SfpsTap_ObjectIdentity = ObjectIdentity
sfpsTap = _SfpsTap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12)
)
_SfpsTapStats_ObjectIdentity = ObjectIdentity
sfpsTapStats = _SfpsTapStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13)
)
_SfpsSizeServices_ObjectIdentity = ObjectIdentity
sfpsSizeServices = _SfpsSizeServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14)
)
_SfpsSizeService_ObjectIdentity = ObjectIdentity
sfpsSizeService = _SfpsSizeService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1)
)
_SfpsSizeServiceAPI_ObjectIdentity = ObjectIdentity
sfpsSizeServiceAPI = _SfpsSizeServiceAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2)
)
_SfpsCNXPacketStats_ObjectIdentity = ObjectIdentity
sfpsCNXPacketStats = _SfpsCNXPacketStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 15)
)
_SfpsSwitchAgent_ObjectIdentity = ObjectIdentity
sfpsSwitchAgent = _SfpsSwitchAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2)
)
_SfpsAgentACMS_ObjectIdentity = ObjectIdentity
sfpsAgentACMS = _SfpsAgentACMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 1)
)
_SfpsAgentRedirector_ObjectIdentity = ObjectIdentity
sfpsAgentRedirector = _SfpsAgentRedirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2)
)
_SfpsSap_ObjectIdentity = ObjectIdentity
sfpsSap = _SfpsSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2)
)
_SfpsSapAPI_ObjectIdentity = ObjectIdentity
sfpsSapAPI = _SfpsSapAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2)
)
_SfpsCPResources_ObjectIdentity = ObjectIdentity
sfpsCPResources = _SfpsCPResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 3)
)
_SfpsServiceCenter_ObjectIdentity = ObjectIdentity
sfpsServiceCenter = _SfpsServiceCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4)
)
_SfpsISPResolve_ObjectIdentity = ObjectIdentity
sfpsISPResolve = _SfpsISPResolve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1)
)
_SfpsSwitchResolve_ObjectIdentity = ObjectIdentity
sfpsSwitchResolve = _SfpsSwitchResolve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 2)
)
_SfpsResolveStats_ObjectIdentity = ObjectIdentity
sfpsResolveStats = _SfpsResolveStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3)
)
_SfpsBlockResolve_ObjectIdentity = ObjectIdentity
sfpsBlockResolve = _SfpsBlockResolve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4)
)
_SfpsBlockResolveAPI_ObjectIdentity = ObjectIdentity
sfpsBlockResolveAPI = _SfpsBlockResolveAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 2)
)
_SfpsBlockResolveStats_ObjectIdentity = ObjectIdentity
sfpsBlockResolveStats = _SfpsBlockResolveStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 3)
)
_SfpsUnresolve_ObjectIdentity = ObjectIdentity
sfpsUnresolve = _SfpsUnresolve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5)
)
_SfpsUnresolveTableAPI_ObjectIdentity = ObjectIdentity
sfpsUnresolveTableAPI = _SfpsUnresolveTableAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 2)
)
_SfpsUnresolveTableStats_ObjectIdentity = ObjectIdentity
sfpsUnresolveTableStats = _SfpsUnresolveTableStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 3)
)
_SfpsTableResolve_ObjectIdentity = ObjectIdentity
sfpsTableResolve = _SfpsTableResolve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6)
)
_SfpsTableResolveAPI_ObjectIdentity = ObjectIdentity
sfpsTableResolveAPI = _SfpsTableResolveAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2)
)
_SfpsSubnetResolve_ObjectIdentity = ObjectIdentity
sfpsSubnetResolve = _SfpsSubnetResolve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7)
)
_SfpsSubnetResolveStats_ObjectIdentity = ObjectIdentity
sfpsSubnetResolveStats = _SfpsSubnetResolveStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 1)
)
_SfpsSubnetResolveAPI_ObjectIdentity = ObjectIdentity
sfpsSubnetResolveAPI = _SfpsSubnetResolveAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 2)
)
_SfpsSubnetResolveNvram_ObjectIdentity = ObjectIdentity
sfpsSubnetResolveNvram = _SfpsSubnetResolveNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 4)
)
_SfpsRelayAgent_ObjectIdentity = ObjectIdentity
sfpsRelayAgent = _SfpsRelayAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 10)
)
_SfpsRelayAgentResolve_ObjectIdentity = ObjectIdentity
sfpsRelayAgentResolve = _SfpsRelayAgentResolve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 10, 4)
)
_SfpsRelayAgentResolveStats_ObjectIdentity = ObjectIdentity
sfpsRelayAgentResolveStats = _SfpsRelayAgentResolveStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 10, 5)
)
_SfpsISPPolicy_ObjectIdentity = ObjectIdentity
sfpsISPPolicy = _SfpsISPPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2)
)
_SfpsVlanMatrix_ObjectIdentity = ObjectIdentity
sfpsVlanMatrix = _SfpsVlanMatrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 2)
)
_SfpsVlanMatrixApi_ObjectIdentity = ObjectIdentity
sfpsVlanMatrixApi = _SfpsVlanMatrixApi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 3)
)
_SfpsVMMatrix_ObjectIdentity = ObjectIdentity
sfpsVMMatrix = _SfpsVMMatrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 2, 4)
)
_SfpsISPPath_ObjectIdentity = ObjectIdentity
sfpsISPPath = _SfpsISPPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5)
)
_SfpsPathAPI_ObjectIdentity = ObjectIdentity
sfpsPathAPI = _SfpsPathAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 3)
)
_SfpsStaticPath_ObjectIdentity = ObjectIdentity
sfpsStaticPath = _SfpsStaticPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 4)
)
_SfpsPathMaskObj_ObjectIdentity = ObjectIdentity
sfpsPathMaskObj = _SfpsPathMaskObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 5)
)
_SfpsDirPath_ObjectIdentity = ObjectIdentity
sfpsDirPath = _SfpsDirPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 6)
)
_SfpsDirPathAPI_ObjectIdentity = ObjectIdentity
sfpsDirPathAPI = _SfpsDirPathAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 7)
)
_SfpsAdminPath_ObjectIdentity = ObjectIdentity
sfpsAdminPath = _SfpsAdminPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 8)
)
_SfpsAdminPathAPI_ObjectIdentity = ObjectIdentity
sfpsAdminPathAPI = _SfpsAdminPathAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 9)
)
_SfpsUpLinkPath_ObjectIdentity = ObjectIdentity
sfpsUpLinkPath = _SfpsUpLinkPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 10)
)
_SfpsChassisRIPPath_ObjectIdentity = ObjectIdentity
sfpsChassisRIPPath = _SfpsChassisRIPPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 5, 12)
)
_SfpsISPFlood_ObjectIdentity = ObjectIdentity
sfpsISPFlood = _SfpsISPFlood_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6)
)
_SfpsResolveCounter_ObjectIdentity = ObjectIdentity
sfpsResolveCounter = _SfpsResolveCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 8)
)
_SfpsMobileUser_ObjectIdentity = ObjectIdentity
sfpsMobileUser = _SfpsMobileUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9)
)
_SfpsMobileUserTable_ObjectIdentity = ObjectIdentity
sfpsMobileUserTable = _SfpsMobileUserTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 1)
)
_SfpsMobileUserReset_ObjectIdentity = ObjectIdentity
sfpsMobileUserReset = _SfpsMobileUserReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 6, 9, 2)
)
_SfpsISPSwitchPath_ObjectIdentity = ObjectIdentity
sfpsISPSwitchPath = _SfpsISPSwitchPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7)
)
_SfpsSwitchPath_ObjectIdentity = ObjectIdentity
sfpsSwitchPath = _SfpsSwitchPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2)
)
_SfpsSwitchPathStats_ObjectIdentity = ObjectIdentity
sfpsSwitchPathStats = _SfpsSwitchPathStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 1)
)
_SfpsSwitchPathAPI_ObjectIdentity = ObjectIdentity
sfpsSwitchPathAPI = _SfpsSwitchPathAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 7, 2, 2)
)
_SfpsCSPControl_ObjectIdentity = ObjectIdentity
sfpsCSPControl = _SfpsCSPControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 5)
)
_SfpsAgentTopology_ObjectIdentity = ObjectIdentity
sfpsAgentTopology = _SfpsAgentTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3)
)
_SfpsTopologyAdjacencies_ObjectIdentity = ObjectIdentity
sfpsTopologyAdjacencies = _SfpsTopologyAdjacencies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 2)
)
_SfpsTopologyNodes_ObjectIdentity = ObjectIdentity
sfpsTopologyNodes = _SfpsTopologyNodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5)
)
_SfpsTopologyAliases_ObjectIdentity = ObjectIdentity
sfpsTopologyAliases = _SfpsTopologyAliases_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6)
)
_SfpsTopologyVNSNeighbors_ObjectIdentity = ObjectIdentity
sfpsTopologyVNSNeighbors = _SfpsTopologyVNSNeighbors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 7)
)
_SfpsTopologyVLANNeighbors_ObjectIdentity = ObjectIdentity
sfpsTopologyVLANNeighbors = _SfpsTopologyVLANNeighbors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 8)
)
_SfpsTopologyDAPITest_ObjectIdentity = ObjectIdentity
sfpsTopologyDAPITest = _SfpsTopologyDAPITest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9)
)
_SfpsTopologyDAPI_ObjectIdentity = ObjectIdentity
sfpsTopologyDAPI = _SfpsTopologyDAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 10)
)
_SfpsTopologyDirStats_ObjectIdentity = ObjectIdentity
sfpsTopologyDirStats = _SfpsTopologyDirStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11)
)
_SfpsTopology_ObjectIdentity = ObjectIdentity
sfpsTopology = _SfpsTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12)
)
_SfpsTopologyPortManager_ObjectIdentity = ObjectIdentity
sfpsTopologyPortManager = _SfpsTopologyPortManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1)
)
_SfpsTPMPortTableAPIIn_ObjectIdentity = ObjectIdentity
sfpsTPMPortTableAPIIn = _SfpsTPMPortTableAPIIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 2)
)
_SfpsTPMPortTableAPIOut_ObjectIdentity = ObjectIdentity
sfpsTPMPortTableAPIOut = _SfpsTPMPortTableAPIOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 1, 3)
)
_SfpsTopologyAgentCommon_ObjectIdentity = ObjectIdentity
sfpsTopologyAgentCommon = _SfpsTopologyAgentCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 2)
)
_SfpsTopologyAgents_ObjectIdentity = ObjectIdentity
sfpsTopologyAgents = _SfpsTopologyAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3)
)
_SfpsVLANTopologyAgent_ObjectIdentity = ObjectIdentity
sfpsVLANTopologyAgent = _SfpsVLANTopologyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1)
)
_SfpsVLANTopAgentPortTableAPIIn_ObjectIdentity = ObjectIdentity
sfpsVLANTopAgentPortTableAPIIn = _SfpsVLANTopAgentPortTableAPIIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 1, 3)
)
_SfpsRATopologyAgent_ObjectIdentity = ObjectIdentity
sfpsRATopologyAgent = _SfpsRATopologyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2)
)
_SfpsRATopAgentPortTableAPIIn_ObjectIdentity = ObjectIdentity
sfpsRATopAgentPortTableAPIIn = _SfpsRATopAgentPortTableAPIIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 3)
)
_SfpsRATopAgentPortTableAPIOut_ObjectIdentity = ObjectIdentity
sfpsRATopAgentPortTableAPIOut = _SfpsRATopAgentPortTableAPIOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 2, 4)
)
_SfpsESPTopologyAgent_ObjectIdentity = ObjectIdentity
sfpsESPTopologyAgent = _SfpsESPTopologyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 3, 3)
)
_SfpsTopologyServers_ObjectIdentity = ObjectIdentity
sfpsTopologyServers = _SfpsTopologyServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4)
)
_SfpsVMTopologyServer_ObjectIdentity = ObjectIdentity
sfpsVMTopologyServer = _SfpsVMTopologyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 1)
)
_SfpsHistTopologyServer_ObjectIdentity = ObjectIdentity
sfpsHistTopologyServer = _SfpsHistTopologyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 4, 2)
)
_SfpsTopologyTestApplication_ObjectIdentity = ObjectIdentity
sfpsTopologyTestApplication = _SfpsTopologyTestApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5)
)
_SfpsTAPITest_ObjectIdentity = ObjectIdentity
sfpsTAPITest = _SfpsTAPITest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1)
)
_SfpsTAPITestIn_ObjectIdentity = ObjectIdentity
sfpsTAPITestIn = _SfpsTAPITestIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1, 1)
)
_SfpsTAPITestOut_ObjectIdentity = ObjectIdentity
sfpsTAPITestOut = _SfpsTAPITestOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 1, 2)
)
_SfpsTopologyServerTest_ObjectIdentity = ObjectIdentity
sfpsTopologyServerTest = _SfpsTopologyServerTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2)
)
_SfpsTopologyServerTestIn_ObjectIdentity = ObjectIdentity
sfpsTopologyServerTestIn = _SfpsTopologyServerTestIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 1)
)
_SfpsTopologyServerPortEventRelay_ObjectIdentity = ObjectIdentity
sfpsTopologyServerPortEventRelay = _SfpsTopologyServerPortEventRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 5, 2, 4)
)
_SfpsTopologyStatistics_ObjectIdentity = ObjectIdentity
sfpsTopologyStatistics = _SfpsTopologyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 6)
)
_SfpsNeighborEvents_ObjectIdentity = ObjectIdentity
sfpsNeighborEvents = _SfpsNeighborEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 6, 1)
)
_SfpsTopologyFCL_ObjectIdentity = ObjectIdentity
sfpsTopologyFCL = _SfpsTopologyFCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 12, 7)
)
_SfpsTopologyRemoteNodes_ObjectIdentity = ObjectIdentity
sfpsTopologyRemoteNodes = _SfpsTopologyRemoteNodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13)
)
_SfpsDirFilterAPI_ObjectIdentity = ObjectIdentity
sfpsDirFilterAPI = _SfpsDirFilterAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 1)
)
_SfpsTopologyRemoteAliases_ObjectIdentity = ObjectIdentity
sfpsTopologyRemoteAliases = _SfpsTopologyRemoteAliases_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 14)
)
_SfpsTopologyDirLock_ObjectIdentity = ObjectIdentity
sfpsTopologyDirLock = _SfpsTopologyDirLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15)
)
_SfpsDirViolation_ObjectIdentity = ObjectIdentity
sfpsDirViolation = _SfpsDirViolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1)
)
_SfpsDirViolationAPI_ObjectIdentity = ObjectIdentity
sfpsDirViolationAPI = _SfpsDirViolationAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 2)
)
_SfpsDirViolationDeltaAPI_ObjectIdentity = ObjectIdentity
sfpsDirViolationDeltaAPI = _SfpsDirViolationDeltaAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 1, 4)
)
_SfpsDirRestriction_ObjectIdentity = ObjectIdentity
sfpsDirRestriction = _SfpsDirRestriction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 2)
)
_SfpsDirLockConfig_ObjectIdentity = ObjectIdentity
sfpsDirLockConfig = _SfpsDirLockConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 3)
)
_SfpsDirLockStats_ObjectIdentity = ObjectIdentity
sfpsDirLockStats = _SfpsDirLockStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 4)
)
_SfpsRestrictedMobility_ObjectIdentity = ObjectIdentity
sfpsRestrictedMobility = _SfpsRestrictedMobility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5)
)
_SfpsRestrictedMobilityAPI_ObjectIdentity = ObjectIdentity
sfpsRestrictedMobilityAPI = _SfpsRestrictedMobilityAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 15, 5, 2)
)
_SfpsDapiNvramStats_ObjectIdentity = ObjectIdentity
sfpsDapiNvramStats = _SfpsDapiNvramStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 16)
)
_SfpsTRTimeOut_ObjectIdentity = ObjectIdentity
sfpsTRTimeOut = _SfpsTRTimeOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 18)
)
_SfpsAgentSignalling_ObjectIdentity = ObjectIdentity
sfpsAgentSignalling = _SfpsAgentSignalling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5)
)
_SfpsCallManagement_ObjectIdentity = ObjectIdentity
sfpsCallManagement = _SfpsCallManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1)
)
_SfpsCallByTuple_ObjectIdentity = ObjectIdentity
sfpsCallByTuple = _SfpsCallByTuple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5)
)
_SfpsCallTableStats_ObjectIdentity = ObjectIdentity
sfpsCallTableStats = _SfpsCallTableStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6)
)
_SfpsEventsAndSignals_ObjectIdentity = ObjectIdentity
sfpsEventsAndSignals = _SfpsEventsAndSignals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 2)
)
_SfpsEventStatistics_ObjectIdentity = ObjectIdentity
sfpsEventStatistics = _SfpsEventStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 2, 1)
)
_SfpsEventSummaryStatistics_ObjectIdentity = ObjectIdentity
sfpsEventSummaryStatistics = _SfpsEventSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 2, 1, 1)
)
_SfpsSignallingSummaryStatistics_ObjectIdentity = ObjectIdentity
sfpsSignallingSummaryStatistics = _SfpsSignallingSummaryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 2, 1, 1, 1)
)
_SfpsAgentDiagnostics_ObjectIdentity = ObjectIdentity
sfpsAgentDiagnostics = _SfpsAgentDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6)
)
_SfpsDiagEventLog_ObjectIdentity = ObjectIdentity
sfpsDiagEventLog = _SfpsDiagEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1)
)
_SfpsEventLogStats_ObjectIdentity = ObjectIdentity
sfpsEventLogStats = _SfpsEventLogStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3)
)
_SfpsEventLogGenConfig_ObjectIdentity = ObjectIdentity
sfpsEventLogGenConfig = _SfpsEventLogGenConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4)
)
_SfpsEventLogClientConfig_ObjectIdentity = ObjectIdentity
sfpsEventLogClientConfig = _SfpsEventLogClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5)
)
_SfpsEventLogClientConfigAPI_ObjectIdentity = ObjectIdentity
sfpsEventLogClientConfigAPI = _SfpsEventLogClientConfigAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2)
)
_SfpsEventLogLevelConfig_ObjectIdentity = ObjectIdentity
sfpsEventLogLevelConfig = _SfpsEventLogLevelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 6)
)
_SfpsTraps_ObjectIdentity = ObjectIdentity
sfpsTraps = _SfpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7)
)
_SfpsTrapAPI_ObjectIdentity = ObjectIdentity
sfpsTrapAPI = _SfpsTrapAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 1)
)
_SfpsTrapTable_ObjectIdentity = ObjectIdentity
sfpsTrapTable = _SfpsTrapTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2)
)
_SfpsFragStats_ObjectIdentity = ObjectIdentity
sfpsFragStats = _SfpsFragStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11)
)
_SfpsDiagStats_ObjectIdentity = ObjectIdentity
sfpsDiagStats = _SfpsDiagStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2)
)
_SfpsFloodCounters_ObjectIdentity = ObjectIdentity
sfpsFloodCounters = _SfpsFloodCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1)
)
_SfpsFloodCountersReset_ObjectIdentity = ObjectIdentity
sfpsFloodCountersReset = _SfpsFloodCountersReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2)
)
_SfpsIsolatedSwitch_ObjectIdentity = ObjectIdentity
sfpsIsolatedSwitch = _SfpsIsolatedSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5)
)
_SfpsResetNVRAM_ObjectIdentity = ObjectIdentity
sfpsResetNVRAM = _SfpsResetNVRAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3)
)
_SfpsAgentConfig_ObjectIdentity = ObjectIdentity
sfpsAgentConfig = _SfpsAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7)
)
_SfpsAgentInterSwitchProtocals_ObjectIdentity = ObjectIdentity
sfpsAgentInterSwitchProtocals = _SfpsAgentInterSwitchProtocals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9)
)
_SfpsISPTraffic_ObjectIdentity = ObjectIdentity
sfpsISPTraffic = _SfpsISPTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 1)
)
_SfpsLinkLoad_ObjectIdentity = ObjectIdentity
sfpsLinkLoad = _SfpsLinkLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 1, 5)
)
_SfpsISPNewUser_ObjectIdentity = ObjectIdentity
sfpsISPNewUser = _SfpsISPNewUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2)
)
_SfpsMobilityStats_ObjectIdentity = ObjectIdentity
sfpsMobilityStats = _SfpsMobilityStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3)
)
_SfpsISPTransport_ObjectIdentity = ObjectIdentity
sfpsISPTransport = _SfpsISPTransport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 3)
)
_SfpsReliableDelivery_ObjectIdentity = ObjectIdentity
sfpsReliableDelivery = _SfpsReliableDelivery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 3, 1)
)
_SfpsAgentFacility_ObjectIdentity = ObjectIdentity
sfpsAgentFacility = _SfpsAgentFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11)
)
_SfpsCentersFacility_ObjectIdentity = ObjectIdentity
sfpsCentersFacility = _SfpsCentersFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 1)
)
_SfpsVNSFacility_ObjectIdentity = ObjectIdentity
sfpsVNSFacility = _SfpsVNSFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 2)
)
_SfpsVLANFacility_ObjectIdentity = ObjectIdentity
sfpsVLANFacility = _SfpsVLANFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 3)
)
_SfpsDiagFacility_ObjectIdentity = ObjectIdentity
sfpsDiagFacility = _SfpsDiagFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 4)
)
_SfpsFabricFacility_ObjectIdentity = ObjectIdentity
sfpsFabricFacility = _SfpsFabricFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 6)
)
_SfpsLiteFacility_ObjectIdentity = ObjectIdentity
sfpsLiteFacility = _SfpsLiteFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 7)
)
_SfpsFpcFacility_ObjectIdentity = ObjectIdentity
sfpsFpcFacility = _SfpsFpcFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 8)
)
_SfpsATMFacility_ObjectIdentity = ObjectIdentity
sfpsATMFacility = _SfpsATMFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 12)
)
_SfpsATMDiagFacility_ObjectIdentity = ObjectIdentity
sfpsATMDiagFacility = _SfpsATMDiagFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 13)
)
_SfpsRAFacility_ObjectIdentity = ObjectIdentity
sfpsRAFacility = _SfpsRAFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 14)
)
_SfpsMcastFacility_ObjectIdentity = ObjectIdentity
sfpsMcastFacility = _SfpsMcastFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 15)
)
_SfpsUpLinkFacility_ObjectIdentity = ObjectIdentity
sfpsUpLinkFacility = _SfpsUpLinkFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 16)
)
_SfpsVRAFacility_ObjectIdentity = ObjectIdentity
sfpsVRAFacility = _SfpsVRAFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 17)
)
_SfpsToggleFacility_ObjectIdentity = ObjectIdentity
sfpsToggleFacility = _SfpsToggleFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 18)
)
_SfpsMatrixFacility_ObjectIdentity = ObjectIdentity
sfpsMatrixFacility = _SfpsMatrixFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 19)
)
_SfpsFepFacility_ObjectIdentity = ObjectIdentity
sfpsFepFacility = _SfpsFepFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 20)
)
_SfpsBetaFacility_ObjectIdentity = ObjectIdentity
sfpsBetaFacility = _SfpsBetaFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 21)
)
_SfpsL4Facility_ObjectIdentity = ObjectIdentity
sfpsL4Facility = _SfpsL4Facility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 22)
)
_SfpsRemoteDeviceManagerFacility_ObjectIdentity = ObjectIdentity
sfpsRemoteDeviceManagerFacility = _SfpsRemoteDeviceManagerFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 23)
)
_SfpsCallTapFacility_ObjectIdentity = ObjectIdentity
sfpsCallTapFacility = _SfpsCallTapFacility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 11, 32)
)
_SfpsAgentScout_ObjectIdentity = ObjectIdentity
sfpsAgentScout = _SfpsAgentScout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 12)
)
_SfpsSourceBlock_ObjectIdentity = ObjectIdentity
sfpsSourceBlock = _SfpsSourceBlock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14)
)
_SfpsBlockSource_ObjectIdentity = ObjectIdentity
sfpsBlockSource = _SfpsBlockSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 1)
)
_SfpsBlockSourceOnly_ObjectIdentity = ObjectIdentity
sfpsBlockSourceOnly = _SfpsBlockSourceOnly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 2)
)
_SfpsBlockSourcePort_ObjectIdentity = ObjectIdentity
sfpsBlockSourcePort = _SfpsBlockSourcePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 3)
)
_SfpsBlockSourceAPI_ObjectIdentity = ObjectIdentity
sfpsBlockSourceAPI = _SfpsBlockSourceAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 4)
)
_SfpsBlockSourceExclude_ObjectIdentity = ObjectIdentity
sfpsBlockSourceExclude = _SfpsBlockSourceExclude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 5)
)
_SfpsBlockSourceStats_ObjectIdentity = ObjectIdentity
sfpsBlockSourceStats = _SfpsBlockSourceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 14, 6)
)
_SfpsDHCPServerVLAN_ObjectIdentity = ObjectIdentity
sfpsDHCPServerVLAN = _SfpsDHCPServerVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 15)
)
_SfpsATalkAMRVLANControl_ObjectIdentity = ObjectIdentity
sfpsATalkAMRVLANControl = _SfpsATalkAMRVLANControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 16)
)
_SfpsRSVRouter_ObjectIdentity = ObjectIdentity
sfpsRSVRouter = _SfpsRSVRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 3)
)
_SfpsATM_ObjectIdentity = ObjectIdentity
sfpsATM = _SfpsATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4)
)
_SfpsATMElan_ObjectIdentity = ObjectIdentity
sfpsATMElan = _SfpsATMElan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1)
)
_SfpsATMDiag_ObjectIdentity = ObjectIdentity
sfpsATMDiag = _SfpsATMDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 2)
)
_SfpsATMResolver_ObjectIdentity = ObjectIdentity
sfpsATMResolver = _SfpsATMResolver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3)
)
_SfpsATMResolverCounters_ObjectIdentity = ObjectIdentity
sfpsATMResolverCounters = _SfpsATMResolverCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2)
)
_SfpsATMAnibIfoStats_ObjectIdentity = ObjectIdentity
sfpsATMAnibIfoStats = _SfpsATMAnibIfoStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4)
)
_SfpsATMPorts_ObjectIdentity = ObjectIdentity
sfpsATMPorts = _SfpsATMPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5)
)
_SfpsATMPortsMgr_ObjectIdentity = ObjectIdentity
sfpsATMPortsMgr = _SfpsATMPortsMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 2)
)
_SfpsATMHistory_ObjectIdentity = ObjectIdentity
sfpsATMHistory = _SfpsATMHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 6)
)
_SfpsATMLecForum_ObjectIdentity = ObjectIdentity
sfpsATMLecForum = _SfpsATMLecForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 7)
)
_SfpsATMSvcHistory_ObjectIdentity = ObjectIdentity
sfpsATMSvcHistory = _SfpsATMSvcHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8)
)
_SfpsATMSvcHistoryMgr_ObjectIdentity = ObjectIdentity
sfpsATMSvcHistoryMgr = _SfpsATMSvcHistoryMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 1)
)
_SfpsATMSvcHistoryEvent_ObjectIdentity = ObjectIdentity
sfpsATMSvcHistoryEvent = _SfpsATMSvcHistoryEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2)
)
_SfpsMulticast_ObjectIdentity = ObjectIdentity
sfpsMulticast = _SfpsMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5)
)
_SfpsMcastConnection_ObjectIdentity = ObjectIdentity
sfpsMcastConnection = _SfpsMcastConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1)
)
_SfpsMcastCnx_ObjectIdentity = ObjectIdentity
sfpsMcastCnx = _SfpsMcastCnx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 1)
)
_SfpsMcastCnxAPI_ObjectIdentity = ObjectIdentity
sfpsMcastCnxAPI = _SfpsMcastCnxAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 1, 2)
)
_SfpsMcastIP_ObjectIdentity = ObjectIdentity
sfpsMcastIP = _SfpsMcastIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2)
)
_SfpsMcastIPRouter_ObjectIdentity = ObjectIdentity
sfpsMcastIPRouter = _SfpsMcastIPRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 1)
)
_SfpsMcastIGMP_ObjectIdentity = ObjectIdentity
sfpsMcastIGMP = _SfpsMcastIGMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 2)
)
_SfpsMcastIPReceiverInfoBase_ObjectIdentity = ObjectIdentity
sfpsMcastIPReceiverInfoBase = _SfpsMcastIPReceiverInfoBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3)
)
_SfpsMcastIPRIBApi_ObjectIdentity = ObjectIdentity
sfpsMcastIPRIBApi = _SfpsMcastIPRIBApi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 3, 2)
)
_SfpsMcastIPSenderInfoBase_ObjectIdentity = ObjectIdentity
sfpsMcastIPSenderInfoBase = _SfpsMcastIPSenderInfoBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 4)
)
_SfpsMcastIPSIBApi_ObjectIdentity = ObjectIdentity
sfpsMcastIPSIBApi = _SfpsMcastIPSIBApi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 2, 4, 2)
)
_SfpsMcastConfig_ObjectIdentity = ObjectIdentity
sfpsMcastConfig = _SfpsMcastConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4)
)
_SfpsMcastConfigApi_ObjectIdentity = ObjectIdentity
sfpsMcastConfigApi = _SfpsMcastConfigApi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 5, 4, 1)
)
_SfpsChassis_ObjectIdentity = ObjectIdentity
sfpsChassis = _SfpsChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6)
)
_SfpsChassisRip_ObjectIdentity = ObjectIdentity
sfpsChassisRip = _SfpsChassisRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1)
)
_SfpsChassisRipTable_ObjectIdentity = ObjectIdentity
sfpsChassisRipTable = _SfpsChassisRipTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1)
)
_SfpsChassisRipAPI_ObjectIdentity = ObjectIdentity
sfpsChassisRipAPI = _SfpsChassisRipAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2)
)
_CtVLANMib_ObjectIdentity = ObjectIdentity
ctVLANMib = _CtVLANMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12)
)
_VlanSwitch_ObjectIdentity = ObjectIdentity
vlanSwitch = _VlanSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1)
)
_VlanAPI_ObjectIdentity = ObjectIdentity
vlanAPI = _VlanAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1)
)
_VlanInternal_ObjectIdentity = ObjectIdentity
vlanInternal = _VlanInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2)
)
_VlanName_ObjectIdentity = ObjectIdentity
vlanName = _VlanName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1)
)
_VlanOutPort_ObjectIdentity = ObjectIdentity
vlanOutPort = _VlanOutPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 2)
)
_VlanSystem_ObjectIdentity = ObjectIdentity
vlanSystem = _VlanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5)
)
_VlanPort_ObjectIdentity = ObjectIdentity
vlanPort = _VlanPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6)
)
_VlanSflsp_ObjectIdentity = ObjectIdentity
vlanSflsp = _VlanSflsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7)
)
_VlanSflspGeneral_ObjectIdentity = ObjectIdentity
vlanSflspGeneral = _VlanSflspGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1)
)
_VlanSflspGeneralVariables_ObjectIdentity = ObjectIdentity
vlanSflspGeneralVariables = _VlanSflspGeneralVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1)
)
_VlanSflspLsdb_ObjectIdentity = ObjectIdentity
vlanSflspLsdb = _VlanSflspLsdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2)
)
_VlanSflspInterfaces_ObjectIdentity = ObjectIdentity
vlanSflspInterfaces = _VlanSflspInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3)
)
_VlanSflspIfMetric_ObjectIdentity = ObjectIdentity
vlanSflspIfMetric = _VlanSflspIfMetric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 4)
)
_VlanSflspNeighbors_ObjectIdentity = ObjectIdentity
vlanSflspNeighbors = _VlanSflspNeighbors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5)
)
_VlanSflspArea_ObjectIdentity = ObjectIdentity
vlanSflspArea = _VlanSflspArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 6)
)
_VlanSflsp1stHop_ObjectIdentity = ObjectIdentity
vlanSflsp1stHop = _VlanSflsp1stHop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 7)
)
_VlanSflspTracePath_ObjectIdentity = ObjectIdentity
vlanSflspTracePath = _VlanSflspTracePath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8)
)
_VlanSflspTracePathExternal_ObjectIdentity = ObjectIdentity
vlanSflspTracePathExternal = _VlanSflspTracePathExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 1)
)
_VlanSflspTracePathAPI_ObjectIdentity = ObjectIdentity
vlanSflspTracePathAPI = _VlanSflspTracePathAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 1, 1)
)
_VlanSflspTracePathInternal_ObjectIdentity = ObjectIdentity
vlanSflspTracePathInternal = _VlanSflspTracePathInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2)
)
_VlanSflspLSDBFlood_ObjectIdentity = ObjectIdentity
vlanSflspLSDBFlood = _VlanSflspLSDBFlood_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20)
)
_VlanSflspLSPStats_ObjectIdentity = ObjectIdentity
vlanSflspLSPStats = _VlanSflspLSPStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21)
)
_VlanSpanning_ObjectIdentity = ObjectIdentity
vlanSpanning = _VlanSpanning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8)
)
_VlanSpanningTreePort_ObjectIdentity = ObjectIdentity
vlanSpanningTreePort = _VlanSpanningTreePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1)
)
_VlanSpanningTreeSwitch_ObjectIdentity = ObjectIdentity
vlanSpanningTreeSwitch = _VlanSpanningTreeSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2)
)
_VlanTestAPI_ObjectIdentity = ObjectIdentity
vlanTestAPI = _VlanTestAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9)
)
_VlanCount_ObjectIdentity = ObjectIdentity
vlanCount = _VlanCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 10)
)
_VlanCountAPI_ObjectIdentity = ObjectIdentity
vlanCountAPI = _VlanCountAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 10, 1)
)
_VlanPriority_ObjectIdentity = ObjectIdentity
vlanPriority = _VlanPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3)
)
_VlanPriorityAPI_ObjectIdentity = ObjectIdentity
vlanPriorityAPI = _VlanPriorityAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 1)
)
_VlanPriorityTable_ObjectIdentity = ObjectIdentity
vlanPriorityTable = _VlanPriorityTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 3, 2)
)
_VlanGARP_ObjectIdentity = ObjectIdentity
vlanGARP = _VlanGARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4)
)
_VlanGARPAPI_ObjectIdentity = ObjectIdentity
vlanGARPAPI = _VlanGARPAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 1)
)
_VlanGARPTable_ObjectIdentity = ObjectIdentity
vlanGARPTable = _VlanGARPTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 4, 2)
)
_VlanAMRTop_ObjectIdentity = ObjectIdentity
vlanAMRTop = _VlanAMRTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3)
)
_VlanAMRRules_ObjectIdentity = ObjectIdentity
vlanAMRRules = _VlanAMRRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6)
)
_VlanAMRSubnets_ObjectIdentity = ObjectIdentity
vlanAMRSubnets = _VlanAMRSubnets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 7)
)
_VlanAMRStats_ObjectIdentity = ObjectIdentity
vlanAMRStats = _VlanAMRStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    **{"cabletron": cabletron,
       "mibs": mibs,
       "ctronExp": ctronExp,
       "ctronSwitch": ctronSwitch,
       "switchCommon": switchCommon,
       "switchSFPS": switchSFPS,
       "sfpsSwitchEngine": sfpsSwitchEngine,
       "sfpsSwitchSystem": sfpsSwitchSystem,
       "sfpsSystemConfig": sfpsSystemConfig,
       "sfpsSystemStats": sfpsSystemStats,
       "sfpsMemHeapStat": sfpsMemHeapStat,
       "sfpsMemHeapStats": sfpsMemHeapStats,
       "sfpsSystemGenerics": sfpsSystemGenerics,
       "sfpsSystemPool": sfpsSystemPool,
       "sfpsAOProperties": sfpsAOProperties,
       "sfpsAOPropertiesAPI": sfpsAOPropertiesAPI,
       "sfpsSystemSwitchChange": sfpsSystemSwitchChange,
       "sfpsSwitchPorts": sfpsSwitchPorts,
       "sfpsPortConfig": sfpsPortConfig,
       "sfpsPortAttribute": sfpsPortAttribute,
       "sfpsPortAttributeTable": sfpsPortAttributeTable,
       "sfpsPortAttributeAPI": sfpsPortAttributeAPI,
       "sfpsPortStats": sfpsPortStats,
       "sfpsSwitchConnections": sfpsSwitchConnections,
       "sfpsConnectionLookupAPI": sfpsConnectionLookupAPI,
       "sfpsConnectionConfigAPI": sfpsConnectionConfigAPI,
       "sfpsConnectionStats": sfpsConnectionStats,
       "sfpsConnectionQueryAPI": sfpsConnectionQueryAPI,
       "sfpsConnectionTestAPI": sfpsConnectionTestAPI,
       "sfpsConnectionAPI": sfpsConnectionAPI,
       "sfpsGAPI": sfpsGAPI,
       "sfpsGAPIATM": sfpsGAPIATM,
       "sfpsSwitchSfpsPacket": sfpsSwitchSfpsPacket,
       "sfpsPktDispatchStats": sfpsPktDispatchStats,
       "sfpsCSPPacket": sfpsCSPPacket,
       "sfpsCallTap": sfpsCallTap,
       "sfpsTap": sfpsTap,
       "sfpsTapStats": sfpsTapStats,
       "sfpsSizeServices": sfpsSizeServices,
       "sfpsSizeService": sfpsSizeService,
       "sfpsSizeServiceAPI": sfpsSizeServiceAPI,
       "sfpsCNXPacketStats": sfpsCNXPacketStats,
       "sfpsSwitchAgent": sfpsSwitchAgent,
       "sfpsAgentACMS": sfpsAgentACMS,
       "sfpsAgentRedirector": sfpsAgentRedirector,
       "sfpsSap": sfpsSap,
       "sfpsSapAPI": sfpsSapAPI,
       "sfpsCPResources": sfpsCPResources,
       "sfpsServiceCenter": sfpsServiceCenter,
       "sfpsISPResolve": sfpsISPResolve,
       "sfpsSwitchResolve": sfpsSwitchResolve,
       "sfpsResolveStats": sfpsResolveStats,
       "sfpsBlockResolve": sfpsBlockResolve,
       "sfpsBlockResolveAPI": sfpsBlockResolveAPI,
       "sfpsBlockResolveStats": sfpsBlockResolveStats,
       "sfpsUnresolve": sfpsUnresolve,
       "sfpsUnresolveTableAPI": sfpsUnresolveTableAPI,
       "sfpsUnresolveTableStats": sfpsUnresolveTableStats,
       "sfpsTableResolve": sfpsTableResolve,
       "sfpsTableResolveAPI": sfpsTableResolveAPI,
       "sfpsSubnetResolve": sfpsSubnetResolve,
       "sfpsSubnetResolveStats": sfpsSubnetResolveStats,
       "sfpsSubnetResolveAPI": sfpsSubnetResolveAPI,
       "sfpsSubnetResolveNvram": sfpsSubnetResolveNvram,
       "sfpsRelayAgent": sfpsRelayAgent,
       "sfpsRelayAgentResolve": sfpsRelayAgentResolve,
       "sfpsRelayAgentResolveStats": sfpsRelayAgentResolveStats,
       "sfpsISPPolicy": sfpsISPPolicy,
       "sfpsVlanMatrix": sfpsVlanMatrix,
       "sfpsVlanMatrixApi": sfpsVlanMatrixApi,
       "sfpsVMMatrix": sfpsVMMatrix,
       "sfpsISPPath": sfpsISPPath,
       "sfpsPathAPI": sfpsPathAPI,
       "sfpsStaticPath": sfpsStaticPath,
       "sfpsPathMaskObj": sfpsPathMaskObj,
       "sfpsDirPath": sfpsDirPath,
       "sfpsDirPathAPI": sfpsDirPathAPI,
       "sfpsAdminPath": sfpsAdminPath,
       "sfpsAdminPathAPI": sfpsAdminPathAPI,
       "sfpsUpLinkPath": sfpsUpLinkPath,
       "sfpsChassisRIPPath": sfpsChassisRIPPath,
       "sfpsISPFlood": sfpsISPFlood,
       "sfpsResolveCounter": sfpsResolveCounter,
       "sfpsMobileUser": sfpsMobileUser,
       "sfpsMobileUserTable": sfpsMobileUserTable,
       "sfpsMobileUserReset": sfpsMobileUserReset,
       "sfpsISPSwitchPath": sfpsISPSwitchPath,
       "sfpsSwitchPath": sfpsSwitchPath,
       "sfpsSwitchPathStats": sfpsSwitchPathStats,
       "sfpsSwitchPathAPI": sfpsSwitchPathAPI,
       "sfpsCSPControl": sfpsCSPControl,
       "sfpsAgentTopology": sfpsAgentTopology,
       "sfpsTopologyAdjacencies": sfpsTopologyAdjacencies,
       "sfpsTopologyNodes": sfpsTopologyNodes,
       "sfpsTopologyAliases": sfpsTopologyAliases,
       "sfpsTopologyVNSNeighbors": sfpsTopologyVNSNeighbors,
       "sfpsTopologyVLANNeighbors": sfpsTopologyVLANNeighbors,
       "sfpsTopologyDAPITest": sfpsTopologyDAPITest,
       "sfpsTopologyDAPI": sfpsTopologyDAPI,
       "sfpsTopologyDirStats": sfpsTopologyDirStats,
       "sfpsTopology": sfpsTopology,
       "sfpsTopologyPortManager": sfpsTopologyPortManager,
       "sfpsTPMPortTableAPIIn": sfpsTPMPortTableAPIIn,
       "sfpsTPMPortTableAPIOut": sfpsTPMPortTableAPIOut,
       "sfpsTopologyAgentCommon": sfpsTopologyAgentCommon,
       "sfpsTopologyAgents": sfpsTopologyAgents,
       "sfpsVLANTopologyAgent": sfpsVLANTopologyAgent,
       "sfpsVLANTopAgentPortTableAPIIn": sfpsVLANTopAgentPortTableAPIIn,
       "sfpsRATopologyAgent": sfpsRATopologyAgent,
       "sfpsRATopAgentPortTableAPIIn": sfpsRATopAgentPortTableAPIIn,
       "sfpsRATopAgentPortTableAPIOut": sfpsRATopAgentPortTableAPIOut,
       "sfpsESPTopologyAgent": sfpsESPTopologyAgent,
       "sfpsTopologyServers": sfpsTopologyServers,
       "sfpsVMTopologyServer": sfpsVMTopologyServer,
       "sfpsHistTopologyServer": sfpsHistTopologyServer,
       "sfpsTopologyTestApplication": sfpsTopologyTestApplication,
       "sfpsTAPITest": sfpsTAPITest,
       "sfpsTAPITestIn": sfpsTAPITestIn,
       "sfpsTAPITestOut": sfpsTAPITestOut,
       "sfpsTopologyServerTest": sfpsTopologyServerTest,
       "sfpsTopologyServerTestIn": sfpsTopologyServerTestIn,
       "sfpsTopologyServerPortEventRelay": sfpsTopologyServerPortEventRelay,
       "sfpsTopologyStatistics": sfpsTopologyStatistics,
       "sfpsNeighborEvents": sfpsNeighborEvents,
       "sfpsTopologyFCL": sfpsTopologyFCL,
       "sfpsTopologyRemoteNodes": sfpsTopologyRemoteNodes,
       "sfpsDirFilterAPI": sfpsDirFilterAPI,
       "sfpsTopologyRemoteAliases": sfpsTopologyRemoteAliases,
       "sfpsTopologyDirLock": sfpsTopologyDirLock,
       "sfpsDirViolation": sfpsDirViolation,
       "sfpsDirViolationAPI": sfpsDirViolationAPI,
       "sfpsDirViolationDeltaAPI": sfpsDirViolationDeltaAPI,
       "sfpsDirRestriction": sfpsDirRestriction,
       "sfpsDirLockConfig": sfpsDirLockConfig,
       "sfpsDirLockStats": sfpsDirLockStats,
       "sfpsRestrictedMobility": sfpsRestrictedMobility,
       "sfpsRestrictedMobilityAPI": sfpsRestrictedMobilityAPI,
       "sfpsDapiNvramStats": sfpsDapiNvramStats,
       "sfpsTRTimeOut": sfpsTRTimeOut,
       "sfpsAgentSignalling": sfpsAgentSignalling,
       "sfpsCallManagement": sfpsCallManagement,
       "sfpsCallByTuple": sfpsCallByTuple,
       "sfpsCallTableStats": sfpsCallTableStats,
       "sfpsEventsAndSignals": sfpsEventsAndSignals,
       "sfpsEventStatistics": sfpsEventStatistics,
       "sfpsEventSummaryStatistics": sfpsEventSummaryStatistics,
       "sfpsSignallingSummaryStatistics": sfpsSignallingSummaryStatistics,
       "sfpsAgentDiagnostics": sfpsAgentDiagnostics,
       "sfpsDiagEventLog": sfpsDiagEventLog,
       "sfpsEventLogStats": sfpsEventLogStats,
       "sfpsEventLogGenConfig": sfpsEventLogGenConfig,
       "sfpsEventLogClientConfig": sfpsEventLogClientConfig,
       "sfpsEventLogClientConfigAPI": sfpsEventLogClientConfigAPI,
       "sfpsEventLogLevelConfig": sfpsEventLogLevelConfig,
       "sfpsTraps": sfpsTraps,
       "sfpsTrapAPI": sfpsTrapAPI,
       "sfpsTrapTable": sfpsTrapTable,
       "sfpsFragStats": sfpsFragStats,
       "sfpsDiagStats": sfpsDiagStats,
       "sfpsFloodCounters": sfpsFloodCounters,
       "sfpsFloodCountersReset": sfpsFloodCountersReset,
       "sfpsIsolatedSwitch": sfpsIsolatedSwitch,
       "sfpsResetNVRAM": sfpsResetNVRAM,
       "sfpsAgentConfig": sfpsAgentConfig,
       "sfpsAgentInterSwitchProtocals": sfpsAgentInterSwitchProtocals,
       "sfpsISPTraffic": sfpsISPTraffic,
       "sfpsLinkLoad": sfpsLinkLoad,
       "sfpsISPNewUser": sfpsISPNewUser,
       "sfpsMobilityStats": sfpsMobilityStats,
       "sfpsISPTransport": sfpsISPTransport,
       "sfpsReliableDelivery": sfpsReliableDelivery,
       "sfpsAgentFacility": sfpsAgentFacility,
       "sfpsCentersFacility": sfpsCentersFacility,
       "sfpsVNSFacility": sfpsVNSFacility,
       "sfpsVLANFacility": sfpsVLANFacility,
       "sfpsDiagFacility": sfpsDiagFacility,
       "sfpsFabricFacility": sfpsFabricFacility,
       "sfpsLiteFacility": sfpsLiteFacility,
       "sfpsFpcFacility": sfpsFpcFacility,
       "sfpsATMFacility": sfpsATMFacility,
       "sfpsATMDiagFacility": sfpsATMDiagFacility,
       "sfpsRAFacility": sfpsRAFacility,
       "sfpsMcastFacility": sfpsMcastFacility,
       "sfpsUpLinkFacility": sfpsUpLinkFacility,
       "sfpsVRAFacility": sfpsVRAFacility,
       "sfpsToggleFacility": sfpsToggleFacility,
       "sfpsMatrixFacility": sfpsMatrixFacility,
       "sfpsFepFacility": sfpsFepFacility,
       "sfpsBetaFacility": sfpsBetaFacility,
       "sfpsL4Facility": sfpsL4Facility,
       "sfpsRemoteDeviceManagerFacility": sfpsRemoteDeviceManagerFacility,
       "sfpsCallTapFacility": sfpsCallTapFacility,
       "sfpsAgentScout": sfpsAgentScout,
       "sfpsSourceBlock": sfpsSourceBlock,
       "sfpsBlockSource": sfpsBlockSource,
       "sfpsBlockSourceOnly": sfpsBlockSourceOnly,
       "sfpsBlockSourcePort": sfpsBlockSourcePort,
       "sfpsBlockSourceAPI": sfpsBlockSourceAPI,
       "sfpsBlockSourceExclude": sfpsBlockSourceExclude,
       "sfpsBlockSourceStats": sfpsBlockSourceStats,
       "sfpsDHCPServerVLAN": sfpsDHCPServerVLAN,
       "sfpsATalkAMRVLANControl": sfpsATalkAMRVLANControl,
       "sfpsRSVRouter": sfpsRSVRouter,
       "sfpsATM": sfpsATM,
       "sfpsATMElan": sfpsATMElan,
       "sfpsATMDiag": sfpsATMDiag,
       "sfpsATMResolver": sfpsATMResolver,
       "sfpsATMResolverCounters": sfpsATMResolverCounters,
       "sfpsATMAnibIfoStats": sfpsATMAnibIfoStats,
       "sfpsATMPorts": sfpsATMPorts,
       "sfpsATMPortsMgr": sfpsATMPortsMgr,
       "sfpsATMHistory": sfpsATMHistory,
       "sfpsATMLecForum": sfpsATMLecForum,
       "sfpsATMSvcHistory": sfpsATMSvcHistory,
       "sfpsATMSvcHistoryMgr": sfpsATMSvcHistoryMgr,
       "sfpsATMSvcHistoryEvent": sfpsATMSvcHistoryEvent,
       "sfpsMulticast": sfpsMulticast,
       "sfpsMcastConnection": sfpsMcastConnection,
       "sfpsMcastCnx": sfpsMcastCnx,
       "sfpsMcastCnxAPI": sfpsMcastCnxAPI,
       "sfpsMcastIP": sfpsMcastIP,
       "sfpsMcastIPRouter": sfpsMcastIPRouter,
       "sfpsMcastIGMP": sfpsMcastIGMP,
       "sfpsMcastIPReceiverInfoBase": sfpsMcastIPReceiverInfoBase,
       "sfpsMcastIPRIBApi": sfpsMcastIPRIBApi,
       "sfpsMcastIPSenderInfoBase": sfpsMcastIPSenderInfoBase,
       "sfpsMcastIPSIBApi": sfpsMcastIPSIBApi,
       "sfpsMcastConfig": sfpsMcastConfig,
       "sfpsMcastConfigApi": sfpsMcastConfigApi,
       "sfpsChassis": sfpsChassis,
       "sfpsChassisRip": sfpsChassisRip,
       "sfpsChassisRipTable": sfpsChassisRipTable,
       "sfpsChassisRipAPI": sfpsChassisRipAPI,
       "ctVLANMib": ctVLANMib,
       "vlanSwitch": vlanSwitch,
       "vlanAPI": vlanAPI,
       "vlanInternal": vlanInternal,
       "vlanName": vlanName,
       "vlanOutPort": vlanOutPort,
       "vlanSystem": vlanSystem,
       "vlanPort": vlanPort,
       "vlanSflsp": vlanSflsp,
       "vlanSflspGeneral": vlanSflspGeneral,
       "vlanSflspGeneralVariables": vlanSflspGeneralVariables,
       "vlanSflspLsdb": vlanSflspLsdb,
       "vlanSflspInterfaces": vlanSflspInterfaces,
       "vlanSflspIfMetric": vlanSflspIfMetric,
       "vlanSflspNeighbors": vlanSflspNeighbors,
       "vlanSflspArea": vlanSflspArea,
       "vlanSflsp1stHop": vlanSflsp1stHop,
       "vlanSflspTracePath": vlanSflspTracePath,
       "vlanSflspTracePathExternal": vlanSflspTracePathExternal,
       "vlanSflspTracePathAPI": vlanSflspTracePathAPI,
       "vlanSflspTracePathInternal": vlanSflspTracePathInternal,
       "vlanSflspLSDBFlood": vlanSflspLSDBFlood,
       "vlanSflspLSPStats": vlanSflspLSPStats,
       "vlanSpanning": vlanSpanning,
       "vlanSpanningTreePort": vlanSpanningTreePort,
       "vlanSpanningTreeSwitch": vlanSpanningTreeSwitch,
       "vlanTestAPI": vlanTestAPI,
       "vlanCount": vlanCount,
       "vlanCountAPI": vlanCountAPI,
       "vlanPriority": vlanPriority,
       "vlanPriorityAPI": vlanPriorityAPI,
       "vlanPriorityTable": vlanPriorityTable,
       "vlanGARP": vlanGARP,
       "vlanGARPAPI": vlanGARPAPI,
       "vlanGARPTable": vlanGARPTable,
       "vlanAMRTop": vlanAMRTop,
       "vlanAMRRules": vlanAMRRules,
       "vlanAMRSubnets": vlanAMRSubnets,
       "vlanAMRStats": vlanAMRStats}
)
