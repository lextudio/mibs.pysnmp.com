# SNMP MIB module (Wellfleet-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:17 2024
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

_Wellfleet_ObjectIdentity = ObjectIdentity
wellfleet = _Wellfleet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18)
)
_WfSwSeries7_ObjectIdentity = ObjectIdentity
wfSwSeries7 = _WfSwSeries7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3)
)
_WfHardwareConfig_ObjectIdentity = ObjectIdentity
wfHardwareConfig = _WfHardwareConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1)
)
_WfHwModuleGroup_ObjectIdentity = ObjectIdentity
wfHwModuleGroup = _WfHwModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 4)
)
_WfHwIdentities_ObjectIdentity = ObjectIdentity
wfHwIdentities = _WfHwIdentities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5)
)
_WfHwFn_ObjectIdentity = ObjectIdentity
wfHwFn = _WfHwFn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 1)
)
_WfHwLn_ObjectIdentity = ObjectIdentity
wfHwLn = _WfHwLn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 2)
)
_WfHwCn_ObjectIdentity = ObjectIdentity
wfHwCn = _WfHwCn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 3)
)
_WfHwAfn_ObjectIdentity = ObjectIdentity
wfHwAfn = _WfHwAfn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 4)
)
_WfHwIn_ObjectIdentity = ObjectIdentity
wfHwIn = _WfHwIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 5)
)
_WfHwAn_ObjectIdentity = ObjectIdentity
wfHwAn = _WfHwAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 16)
)
_WfHwAnMpr_ObjectIdentity = ObjectIdentity
wfHwAnMpr = _WfHwAnMpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 16, 1)
)
_WfHwAnHub_ObjectIdentity = ObjectIdentity
wfHwAnHub = _WfHwAnHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 16, 2)
)
_WfHwBln_ObjectIdentity = ObjectIdentity
wfHwBln = _WfHwBln_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 16640)
)
_WfHwBcn_ObjectIdentity = ObjectIdentity
wfHwBcn = _WfHwBcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 16896)
)
_WfHwRbln_ObjectIdentity = ObjectIdentity
wfHwRbln = _WfHwRbln_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 17152)
)
_WfHwAsn_ObjectIdentity = ObjectIdentity
wfHwAsn = _WfHwAsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 20480)
)
_WfHwAsnZ_ObjectIdentity = ObjectIdentity
wfHwAsnZ = _WfHwAsnZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 20736)
)
_WfHwAsnB_ObjectIdentity = ObjectIdentity
wfHwAsnB = _WfHwAsnB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 20992)
)
_WfSwitchNode_ObjectIdentity = ObjectIdentity
wfSwitchNode = _WfSwitchNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 5, 24576)
)
_WfSoftwareConfig_ObjectIdentity = ObjectIdentity
wfSoftwareConfig = _WfSoftwareConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 2)
)
_WfSystem_ObjectIdentity = ObjectIdentity
wfSystem = _WfSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3)
)
_WfServices_ObjectIdentity = ObjectIdentity
wfServices = _WfServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2)
)
_WfPacketGenGroup_ObjectIdentity = ObjectIdentity
wfPacketGenGroup = _WfPacketGenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4)
)
_WfBacPktGenGroup_ObjectIdentity = ObjectIdentity
wfBacPktGenGroup = _WfBacPktGenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1)
)
_WfGameGroup_ObjectIdentity = ObjectIdentity
wfGameGroup = _WfGameGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5)
)
_WfStaGroup_ObjectIdentity = ObjectIdentity
wfStaGroup = _WfStaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6)
)
_WfMibHeapGroup_ObjectIdentity = ObjectIdentity
wfMibHeapGroup = _WfMibHeapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 7)
)
_WfCircuitNameExtension_ObjectIdentity = ObjectIdentity
wfCircuitNameExtension = _WfCircuitNameExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 9)
)
_WfNetBootGroup_ObjectIdentity = ObjectIdentity
wfNetBootGroup = _WfNetBootGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10)
)
_WfSerialPortGroup_ObjectIdentity = ObjectIdentity
wfSerialPortGroup = _WfSerialPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11)
)
_WfFileSystemGroup_ObjectIdentity = ObjectIdentity
wfFileSystemGroup = _WfFileSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 12)
)
_WfPingGroup_ObjectIdentity = ObjectIdentity
wfPingGroup = _WfPingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13)
)
_WfRuiBootGroup_ObjectIdentity = ObjectIdentity
wfRuiBootGroup = _WfRuiBootGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14)
)
_WfSyslogGroup_ObjectIdentity = ObjectIdentity
wfSyslogGroup = _WfSyslogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 15)
)
_WfDCMmwGroup_ObjectIdentity = ObjectIdentity
wfDCMmwGroup = _WfDCMmwGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 16)
)
_WfStatsDcGroup_ObjectIdentity = ObjectIdentity
wfStatsDcGroup = _WfStatsDcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17)
)
_WfName_ObjectIdentity = ObjectIdentity
wfName = _WfName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 18)
)
_WfEntityGroup_ObjectIdentity = ObjectIdentity
wfEntityGroup = _WfEntityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 20)
)
_WfUserServicesGroup_ObjectIdentity = ObjectIdentity
wfUserServicesGroup = _WfUserServicesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22)
)
_WfDiffServGroup_ObjectIdentity = ObjectIdentity
wfDiffServGroup = _WfDiffServGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23)
)
_WfServicePkgGroup_ObjectIdentity = ObjectIdentity
wfServicePkgGroup = _WfServicePkgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 1)
)
_WfAcctGroup_ObjectIdentity = ObjectIdentity
wfAcctGroup = _WfAcctGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2)
)
_WfLine_ObjectIdentity = ObjectIdentity
wfLine = _WfLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4)
)
_WfHwFGroup_ObjectIdentity = ObjectIdentity
wfHwFGroup = _WfHwFGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 6)
)
_WfMcT1Group_ObjectIdentity = ObjectIdentity
wfMcT1Group = _WfMcT1Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8)
)
_WfDs1E1Group_ObjectIdentity = ObjectIdentity
wfDs1E1Group = _WfDs1E1Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9)
)
_WfDs1Group_ObjectIdentity = ObjectIdentity
wfDs1Group = _WfDs1Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 12)
)
_WfDs3Group_ObjectIdentity = ObjectIdentity
wfDs3Group = _WfDs3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 13)
)
_WfSipGroup_ObjectIdentity = ObjectIdentity
wfSipGroup = _WfSipGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 14)
)
_WfFddiGroup_ObjectIdentity = ObjectIdentity
wfFddiGroup = _WfFddiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15)
)
_WfCSMACDAutoNegGroup_ObjectIdentity = ObjectIdentity
wfCSMACDAutoNegGroup = _WfCSMACDAutoNegGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16)
)
_WfDiagsGroup_ObjectIdentity = ObjectIdentity
wfDiagsGroup = _WfDiagsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 20)
)
_WfPktCaptureGroup_ObjectIdentity = ObjectIdentity
wfPktCaptureGroup = _WfPktCaptureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21)
)
_WfCompressionGroup_ObjectIdentity = ObjectIdentity
wfCompressionGroup = _WfCompressionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 22)
)
_WfAtmInterfaceGroup_ObjectIdentity = ObjectIdentity
wfAtmInterfaceGroup = _WfAtmInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23)
)
_WfSonetGroup_ObjectIdentity = ObjectIdentity
wfSonetGroup = _WfSonetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24)
)
_WfTaxiGroup_ObjectIdentity = ObjectIdentity
wfTaxiGroup = _WfTaxiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 25)
)
_WfDsx3Group_ObjectIdentity = ObjectIdentity
wfDsx3Group = _WfDsx3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26)
)
_WfBisyncGroup_ObjectIdentity = ObjectIdentity
wfBisyncGroup = _WfBisyncGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27)
)
_WfLinkEncryptionGroup_ObjectIdentity = ObjectIdentity
wfLinkEncryptionGroup = _WfLinkEncryptionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 28)
)
_WfModemGroup_ObjectIdentity = ObjectIdentity
wfModemGroup = _WfModemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29)
)
_WfDsuCsuGroup_ObjectIdentity = ObjectIdentity
wfDsuCsuGroup = _WfDsuCsuGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30)
)
_WfSwitchMediaGroup_ObjectIdentity = ObjectIdentity
wfSwitchMediaGroup = _WfSwitchMediaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 31)
)
_WfXCtlGroup_ObjectIdentity = ObjectIdentity
wfXCtlGroup = _WfXCtlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 31, 1)
)
_WfCSMACDIfGroup_ObjectIdentity = ObjectIdentity
wfCSMACDIfGroup = _WfCSMACDIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 31, 2)
)
_WfMAUGroup_ObjectIdentity = ObjectIdentity
wfMAUGroup = _WfMAUGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 31, 3)
)
_WfFntsAtmGroup_ObjectIdentity = ObjectIdentity
wfFntsAtmGroup = _WfFntsAtmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32)
)
_WfIsdbGroup_ObjectIdentity = ObjectIdentity
wfIsdbGroup = _WfIsdbGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 33)
)
_WfDeviceCtlGroup_ObjectIdentity = ObjectIdentity
wfDeviceCtlGroup = _WfDeviceCtlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34)
)
_WfModCtlGroup_ObjectIdentity = ObjectIdentity
wfModCtlGroup = _WfModCtlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 1)
)
_WfIfpGroup_ObjectIdentity = ObjectIdentity
wfIfpGroup = _WfIfpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 34, 2)
)
_WfApplication_ObjectIdentity = ObjectIdentity
wfApplication = _WfApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5)
)
_WfDataLink_ObjectIdentity = ObjectIdentity
wfDataLink = _WfDataLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1)
)
_WfBridgeGroup_ObjectIdentity = ObjectIdentity
wfBridgeGroup = _WfBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1)
)
_WfSpanningTree_ObjectIdentity = ObjectIdentity
wfSpanningTree = _WfSpanningTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2)
)
_WfIfGroup_ObjectIdentity = ObjectIdentity
wfIfGroup = _WfIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3)
)
_WfCircuitOptsGroup_ObjectIdentity = ObjectIdentity
wfCircuitOptsGroup = _WfCircuitOptsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 4)
)
_WfDlsGroup_ObjectIdentity = ObjectIdentity
wfDlsGroup = _WfDlsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5)
)
_WfLlcGroup_ObjectIdentity = ObjectIdentity
wfLlcGroup = _WfLlcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 6)
)
_WfSdlcGroup_ObjectIdentity = ObjectIdentity
wfSdlcGroup = _WfSdlcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 7)
)
_WfProtocolPriorityGroup_ObjectIdentity = ObjectIdentity
wfProtocolPriorityGroup = _WfProtocolPriorityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 9)
)
_WfIRedundGroup_ObjectIdentity = ObjectIdentity
wfIRedundGroup = _WfIRedundGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10)
)
_WfFwallGroup_ObjectIdentity = ObjectIdentity
wfFwallGroup = _WfFwallGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 11)
)
_WfVlanGroup_ObjectIdentity = ObjectIdentity
wfVlanGroup = _WfVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 12)
)
_WfPortMatrixGroup_ObjectIdentity = ObjectIdentity
wfPortMatrixGroup = _WfPortMatrixGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 12, 1)
)
_WfCommonVlanGroup_ObjectIdentity = ObjectIdentity
wfCommonVlanGroup = _WfCommonVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 12, 2)
)
_WfMacAddrAssgGroup_ObjectIdentity = ObjectIdentity
wfMacAddrAssgGroup = _WfMacAddrAssgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 12, 3)
)
_WfHelloGroup_ObjectIdentity = ObjectIdentity
wfHelloGroup = _WfHelloGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 12, 4)
)
_WfDot1dConfigGroup_ObjectIdentity = ObjectIdentity
wfDot1dConfigGroup = _WfDot1dConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 12, 5)
)
_WfDot1qTagConfigGroup_ObjectIdentity = ObjectIdentity
wfDot1qTagConfigGroup = _WfDot1qTagConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 12, 6)
)
_WfConvSteeringGroup_ObjectIdentity = ObjectIdentity
wfConvSteeringGroup = _WfConvSteeringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 13)
)
_WfDecGroup_ObjectIdentity = ObjectIdentity
wfDecGroup = _WfDecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2)
)
_WfInternet_ObjectIdentity = ObjectIdentity
wfInternet = _WfInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3)
)
_WfArpGroup_ObjectIdentity = ObjectIdentity
wfArpGroup = _WfArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 1)
)
_WfIpRouting_ObjectIdentity = ObjectIdentity
wfIpRouting = _WfIpRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2)
)
_WfIpGroup_ObjectIdentity = ObjectIdentity
wfIpGroup = _WfIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1)
)
_WfRipGroup_ObjectIdentity = ObjectIdentity
wfRipGroup = _WfRipGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2)
)
_WfOspfGroup_ObjectIdentity = ObjectIdentity
wfOspfGroup = _WfOspfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 3)
)
_WfEgpGroup_ObjectIdentity = ObjectIdentity
wfEgpGroup = _WfEgpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 4)
)
_WfBgpGroup_ObjectIdentity = ObjectIdentity
wfBgpGroup = _WfBgpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5)
)
_WfIpPolicyGroup_ObjectIdentity = ObjectIdentity
wfIpPolicyGroup = _WfIpPolicyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 6)
)
_WfNatGroup_ObjectIdentity = ObjectIdentity
wfNatGroup = _WfNatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7)
)
_WfIisisGroup_ObjectIdentity = ObjectIdentity
wfIisisGroup = _WfIisisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 8)
)
_WfTcpGroup_ObjectIdentity = ObjectIdentity
wfTcpGroup = _WfTcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3)
)
_WfUdpGroup_ObjectIdentity = ObjectIdentity
wfUdpGroup = _WfUdpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4)
)
_WfSnmpGroup_ObjectIdentity = ObjectIdentity
wfSnmpGroup = _WfSnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5)
)
_WfTelnetGroup_ObjectIdentity = ObjectIdentity
wfTelnetGroup = _WfTelnetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7)
)
_WfBootpGroup_ObjectIdentity = ObjectIdentity
wfBootpGroup = _WfBootpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 8)
)
_WfRarpGroup_ObjectIdentity = ObjectIdentity
wfRarpGroup = _WfRarpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 9)
)
_WfFtpGroup_ObjectIdentity = ObjectIdentity
wfFtpGroup = _WfFtpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 10)
)
_WfNetBIOSIpGroup_ObjectIdentity = ObjectIdentity
wfNetBIOSIpGroup = _WfNetBIOSIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 11)
)
_WfDvmrpGroup_ObjectIdentity = ObjectIdentity
wfDvmrpGroup = _WfDvmrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12)
)
_WfIgmpGroup_ObjectIdentity = ObjectIdentity
wfIgmpGroup = _WfIgmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13)
)
_WfPimGroup_ObjectIdentity = ObjectIdentity
wfPimGroup = _WfPimGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 14)
)
_WfIpv6Group_ObjectIdentity = ObjectIdentity
wfIpv6Group = _WfIpv6Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16)
)
_WfNtpGroup_ObjectIdentity = ObjectIdentity
wfNtpGroup = _WfNtpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 17)
)
_WfRcmdsGroup_ObjectIdentity = ObjectIdentity
wfRcmdsGroup = _WfRcmdsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18)
)
_WfDnsGroup_ObjectIdentity = ObjectIdentity
wfDnsGroup = _WfDnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 19)
)
_WfGreGroup_ObjectIdentity = ObjectIdentity
wfGreGroup = _WfGreGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20)
)
_WfMobileIpGroup_ObjectIdentity = ObjectIdentity
wfMobileIpGroup = _WfMobileIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 21)
)
_WfHttpGroup_ObjectIdentity = ObjectIdentity
wfHttpGroup = _WfHttpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22)
)
_WfNhrpGroup_ObjectIdentity = ObjectIdentity
wfNhrpGroup = _WfNhrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 23)
)
_WfDhcpServerGroup_ObjectIdentity = ObjectIdentity
wfDhcpServerGroup = _WfDhcpServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24)
)
_WfVrrpGroup_ObjectIdentity = ObjectIdentity
wfVrrpGroup = _WfVrrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25)
)
_WfIpsecGroup_ObjectIdentity = ObjectIdentity
wfIpsecGroup = _WfIpsecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 26)
)
_WfAppletalkGroup_ObjectIdentity = ObjectIdentity
wfAppletalkGroup = _WfAppletalkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4)
)
_WfIpxGroup_ObjectIdentity = ObjectIdentity
wfIpxGroup = _WfIpxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5)
)
_WfNlspGroup_ObjectIdentity = ObjectIdentity
wfNlspGroup = _WfNlspGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 5, 128)
)
_WfOsiGroup_ObjectIdentity = ObjectIdentity
wfOsiGroup = _WfOsiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 6)
)
_WfVinesGroup_ObjectIdentity = ObjectIdentity
wfVinesGroup = _WfVinesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8)
)
_WfWanGroup_ObjectIdentity = ObjectIdentity
wfWanGroup = _WfWanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9)
)
_WfFrameRelayGroup_ObjectIdentity = ObjectIdentity
wfFrameRelayGroup = _WfFrameRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1)
)
_WfPppGroup_ObjectIdentity = ObjectIdentity
wfPppGroup = _WfPppGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 2)
)
_WfX25Group_ObjectIdentity = ObjectIdentity
wfX25Group = _WfX25Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 4)
)
_WfAtmGroup_ObjectIdentity = ObjectIdentity
wfAtmGroup = _WfAtmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5)
)
_WfAtmLeGroup_ObjectIdentity = ObjectIdentity
wfAtmLeGroup = _WfAtmLeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 5, 20)
)
_WfFrswGroup_ObjectIdentity = ObjectIdentity
wfFrswGroup = _WfFrswGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6)
)
_WfSmdsSwGroup_ObjectIdentity = ObjectIdentity
wfSmdsSwGroup = _WfSmdsSwGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 7)
)
_WfIsdnGroup_ObjectIdentity = ObjectIdentity
wfIsdnGroup = _WfIsdnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 8)
)
_WfFrameRelay2Group_ObjectIdentity = ObjectIdentity
wfFrameRelay2Group = _WfFrameRelay2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9)
)
_WfmpsObjects_ObjectIdentity = ObjectIdentity
wfmpsObjects = _WfmpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10)
)
_WfAsrGroup_ObjectIdentity = ObjectIdentity
wfAsrGroup = _WfAsrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 11)
)
_WfX25PadGroup_ObjectIdentity = ObjectIdentity
wfX25PadGroup = _WfX25PadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12)
)
_WfAtmHalfBridgeGroup_ObjectIdentity = ObjectIdentity
wfAtmHalfBridgeGroup = _WfAtmHalfBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 13)
)
_WfmpcObjects_ObjectIdentity = ObjectIdentity
wfmpcObjects = _WfmpcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 14)
)
_WfMplsLdpGroup_ObjectIdentity = ObjectIdentity
wfMplsLdpGroup = _WfMplsLdpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15)
)
_WfMplsAtmGroup_ObjectIdentity = ObjectIdentity
wfMplsAtmGroup = _WfMplsAtmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 16)
)
_WfXnsGroup_ObjectIdentity = ObjectIdentity
wfXnsGroup = _WfXnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 10)
)
_WfTestGroup_ObjectIdentity = ObjectIdentity
wfTestGroup = _WfTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 11)
)
_WfLanManagerGroup_ObjectIdentity = ObjectIdentity
wfLanManagerGroup = _WfLanManagerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 12)
)
_WfOsiConsGroup_ObjectIdentity = ObjectIdentity
wfOsiConsGroup = _WfOsiConsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 13)
)
_WfAppnGroup_ObjectIdentity = ObjectIdentity
wfAppnGroup = _WfAppnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14)
)
_WfIpexGroup_ObjectIdentity = ObjectIdentity
wfIpexGroup = _WfIpexGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 15)
)
_WfIntegratedServicesGroup_ObjectIdentity = ObjectIdentity
wfIntegratedServicesGroup = _WfIntegratedServicesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16)
)
_WfReservationProtocolGroup_ObjectIdentity = ObjectIdentity
wfReservationProtocolGroup = _WfReservationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1)
)
_WfRRedGroup_ObjectIdentity = ObjectIdentity
wfRRedGroup = _WfRRedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17)
)
_WfBotGroup_ObjectIdentity = ObjectIdentity
wfBotGroup = _WfBotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18)
)
_WfAccountingGroup_ObjectIdentity = ObjectIdentity
wfAccountingGroup = _WfAccountingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 20)
)
_WfAsyncOverTcpGroup_ObjectIdentity = ObjectIdentity
wfAsyncOverTcpGroup = _WfAsyncOverTcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21)
)
_WfRadiusGroup_ObjectIdentity = ObjectIdentity
wfRadiusGroup = _WfRadiusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 22)
)
_WfL2TPGroup_ObjectIdentity = ObjectIdentity
wfL2TPGroup = _WfL2TPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 23)
)
_WfVcctGroup_ObjectIdentity = ObjectIdentity
wfVcctGroup = _WfVcctGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 24)
)
_WfQoSPolicyGroup_ObjectIdentity = ObjectIdentity
wfQoSPolicyGroup = _WfQoSPolicyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25)
)
_WfCopsCGroup_ObjectIdentity = ObjectIdentity
wfCopsCGroup = _WfCopsCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1)
)
_WfDiffServAppGroup_ObjectIdentity = ObjectIdentity
wfDiffServAppGroup = _WfDiffServAppGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 26)
)
_WfIKEGroup_ObjectIdentity = ObjectIdentity
wfIKEGroup = _WfIKEGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 27)
)
_WfPgmGroup_ObjectIdentity = ObjectIdentity
wfPgmGroup = _WfPgmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-COMMON-MIB",
    **{"wellfleet": wellfleet,
       "wfSwSeries7": wfSwSeries7,
       "wfHardwareConfig": wfHardwareConfig,
       "wfHwModuleGroup": wfHwModuleGroup,
       "wfHwIdentities": wfHwIdentities,
       "wfHwFn": wfHwFn,
       "wfHwLn": wfHwLn,
       "wfHwCn": wfHwCn,
       "wfHwAfn": wfHwAfn,
       "wfHwIn": wfHwIn,
       "wfHwAn": wfHwAn,
       "wfHwAnMpr": wfHwAnMpr,
       "wfHwAnHub": wfHwAnHub,
       "wfHwBln": wfHwBln,
       "wfHwBcn": wfHwBcn,
       "wfHwRbln": wfHwRbln,
       "wfHwAsn": wfHwAsn,
       "wfHwAsnZ": wfHwAsnZ,
       "wfHwAsnB": wfHwAsnB,
       "wfSwitchNode": wfSwitchNode,
       "wfSoftwareConfig": wfSoftwareConfig,
       "wfSystem": wfSystem,
       "wfServices": wfServices,
       "wfPacketGenGroup": wfPacketGenGroup,
       "wfBacPktGenGroup": wfBacPktGenGroup,
       "wfGameGroup": wfGameGroup,
       "wfStaGroup": wfStaGroup,
       "wfMibHeapGroup": wfMibHeapGroup,
       "wfCircuitNameExtension": wfCircuitNameExtension,
       "wfNetBootGroup": wfNetBootGroup,
       "wfSerialPortGroup": wfSerialPortGroup,
       "wfFileSystemGroup": wfFileSystemGroup,
       "wfPingGroup": wfPingGroup,
       "wfRuiBootGroup": wfRuiBootGroup,
       "wfSyslogGroup": wfSyslogGroup,
       "wfDCMmwGroup": wfDCMmwGroup,
       "wfStatsDcGroup": wfStatsDcGroup,
       "wfName": wfName,
       "wfEntityGroup": wfEntityGroup,
       "wfUserServicesGroup": wfUserServicesGroup,
       "wfDiffServGroup": wfDiffServGroup,
       "wfServicePkgGroup": wfServicePkgGroup,
       "wfAcctGroup": wfAcctGroup,
       "wfLine": wfLine,
       "wfHwFGroup": wfHwFGroup,
       "wfMcT1Group": wfMcT1Group,
       "wfDs1E1Group": wfDs1E1Group,
       "wfDs1Group": wfDs1Group,
       "wfDs3Group": wfDs3Group,
       "wfSipGroup": wfSipGroup,
       "wfFddiGroup": wfFddiGroup,
       "wfCSMACDAutoNegGroup": wfCSMACDAutoNegGroup,
       "wfDiagsGroup": wfDiagsGroup,
       "wfPktCaptureGroup": wfPktCaptureGroup,
       "wfCompressionGroup": wfCompressionGroup,
       "wfAtmInterfaceGroup": wfAtmInterfaceGroup,
       "wfSonetGroup": wfSonetGroup,
       "wfTaxiGroup": wfTaxiGroup,
       "wfDsx3Group": wfDsx3Group,
       "wfBisyncGroup": wfBisyncGroup,
       "wfLinkEncryptionGroup": wfLinkEncryptionGroup,
       "wfModemGroup": wfModemGroup,
       "wfDsuCsuGroup": wfDsuCsuGroup,
       "wfSwitchMediaGroup": wfSwitchMediaGroup,
       "wfXCtlGroup": wfXCtlGroup,
       "wfCSMACDIfGroup": wfCSMACDIfGroup,
       "wfMAUGroup": wfMAUGroup,
       "wfFntsAtmGroup": wfFntsAtmGroup,
       "wfIsdbGroup": wfIsdbGroup,
       "wfDeviceCtlGroup": wfDeviceCtlGroup,
       "wfModCtlGroup": wfModCtlGroup,
       "wfIfpGroup": wfIfpGroup,
       "wfApplication": wfApplication,
       "wfDataLink": wfDataLink,
       "wfBridgeGroup": wfBridgeGroup,
       "wfSpanningTree": wfSpanningTree,
       "wfIfGroup": wfIfGroup,
       "wfCircuitOptsGroup": wfCircuitOptsGroup,
       "wfDlsGroup": wfDlsGroup,
       "wfLlcGroup": wfLlcGroup,
       "wfSdlcGroup": wfSdlcGroup,
       "wfProtocolPriorityGroup": wfProtocolPriorityGroup,
       "wfIRedundGroup": wfIRedundGroup,
       "wfFwallGroup": wfFwallGroup,
       "wfVlanGroup": wfVlanGroup,
       "wfPortMatrixGroup": wfPortMatrixGroup,
       "wfCommonVlanGroup": wfCommonVlanGroup,
       "wfMacAddrAssgGroup": wfMacAddrAssgGroup,
       "wfHelloGroup": wfHelloGroup,
       "wfDot1dConfigGroup": wfDot1dConfigGroup,
       "wfDot1qTagConfigGroup": wfDot1qTagConfigGroup,
       "wfConvSteeringGroup": wfConvSteeringGroup,
       "wfDecGroup": wfDecGroup,
       "wfInternet": wfInternet,
       "wfArpGroup": wfArpGroup,
       "wfIpRouting": wfIpRouting,
       "wfIpGroup": wfIpGroup,
       "wfRipGroup": wfRipGroup,
       "wfOspfGroup": wfOspfGroup,
       "wfEgpGroup": wfEgpGroup,
       "wfBgpGroup": wfBgpGroup,
       "wfIpPolicyGroup": wfIpPolicyGroup,
       "wfNatGroup": wfNatGroup,
       "wfIisisGroup": wfIisisGroup,
       "wfTcpGroup": wfTcpGroup,
       "wfUdpGroup": wfUdpGroup,
       "wfSnmpGroup": wfSnmpGroup,
       "wfTelnetGroup": wfTelnetGroup,
       "wfBootpGroup": wfBootpGroup,
       "wfRarpGroup": wfRarpGroup,
       "wfFtpGroup": wfFtpGroup,
       "wfNetBIOSIpGroup": wfNetBIOSIpGroup,
       "wfDvmrpGroup": wfDvmrpGroup,
       "wfIgmpGroup": wfIgmpGroup,
       "wfPimGroup": wfPimGroup,
       "wfIpv6Group": wfIpv6Group,
       "wfNtpGroup": wfNtpGroup,
       "wfRcmdsGroup": wfRcmdsGroup,
       "wfDnsGroup": wfDnsGroup,
       "wfGreGroup": wfGreGroup,
       "wfMobileIpGroup": wfMobileIpGroup,
       "wfHttpGroup": wfHttpGroup,
       "wfNhrpGroup": wfNhrpGroup,
       "wfDhcpServerGroup": wfDhcpServerGroup,
       "wfVrrpGroup": wfVrrpGroup,
       "wfIpsecGroup": wfIpsecGroup,
       "wfAppletalkGroup": wfAppletalkGroup,
       "wfIpxGroup": wfIpxGroup,
       "wfNlspGroup": wfNlspGroup,
       "wfOsiGroup": wfOsiGroup,
       "wfVinesGroup": wfVinesGroup,
       "wfWanGroup": wfWanGroup,
       "wfFrameRelayGroup": wfFrameRelayGroup,
       "wfPppGroup": wfPppGroup,
       "wfX25Group": wfX25Group,
       "wfAtmGroup": wfAtmGroup,
       "wfAtmLeGroup": wfAtmLeGroup,
       "wfFrswGroup": wfFrswGroup,
       "wfSmdsSwGroup": wfSmdsSwGroup,
       "wfIsdnGroup": wfIsdnGroup,
       "wfFrameRelay2Group": wfFrameRelay2Group,
       "wfmpsObjects": wfmpsObjects,
       "wfAsrGroup": wfAsrGroup,
       "wfX25PadGroup": wfX25PadGroup,
       "wfAtmHalfBridgeGroup": wfAtmHalfBridgeGroup,
       "wfmpcObjects": wfmpcObjects,
       "wfMplsLdpGroup": wfMplsLdpGroup,
       "wfMplsAtmGroup": wfMplsAtmGroup,
       "wfXnsGroup": wfXnsGroup,
       "wfTestGroup": wfTestGroup,
       "wfLanManagerGroup": wfLanManagerGroup,
       "wfOsiConsGroup": wfOsiConsGroup,
       "wfAppnGroup": wfAppnGroup,
       "wfIpexGroup": wfIpexGroup,
       "wfIntegratedServicesGroup": wfIntegratedServicesGroup,
       "wfReservationProtocolGroup": wfReservationProtocolGroup,
       "wfRRedGroup": wfRRedGroup,
       "wfBotGroup": wfBotGroup,
       "wfAccountingGroup": wfAccountingGroup,
       "wfAsyncOverTcpGroup": wfAsyncOverTcpGroup,
       "wfRadiusGroup": wfRadiusGroup,
       "wfL2TPGroup": wfL2TPGroup,
       "wfVcctGroup": wfVcctGroup,
       "wfQoSPolicyGroup": wfQoSPolicyGroup,
       "wfCopsCGroup": wfCopsCGroup,
       "wfDiffServAppGroup": wfDiffServAppGroup,
       "wfIKEGroup": wfIKEGroup,
       "wfPgmGroup": wfPgmGroup}
)
