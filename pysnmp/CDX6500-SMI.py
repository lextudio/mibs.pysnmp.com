# SNMP MIB module (CDX6500-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CDX6500-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:56 2024
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



class Counter16(Integer32):
    """Custom type Counter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class Counter8(Integer32):
    """Custom type Counter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500NodeMgmt_ObjectIdentity = ObjectIdentity
cdx6500NodeMgmt = _Cdx6500NodeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1)
)
_Cdx6500NMSNMPGroup_ObjectIdentity = ObjectIdentity
cdx6500NMSNMPGroup = _Cdx6500NMSNMPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1)
)
_Cdx6500NMNodeParametersGroup_ObjectIdentity = ObjectIdentity
cdx6500NMNodeParametersGroup = _Cdx6500NMNodeParametersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2)
)
_Cdx6500NMDiagnosticsGroup_ObjectIdentity = ObjectIdentity
cdx6500NMDiagnosticsGroup = _Cdx6500NMDiagnosticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3)
)
_Cdx6500NMControlsGroup_ObjectIdentity = ObjectIdentity
cdx6500NMControlsGroup = _Cdx6500NMControlsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 4)
)
_Cdx6500NMDLSVGroup_ObjectIdentity = ObjectIdentity
cdx6500NMDLSVGroup = _Cdx6500NMDLSVGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
_Cdx6500PCTBSC3270DeviceGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTBSC3270DeviceGroup = _Cdx6500PCTBSC3270DeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4)
)
_Cdx6500PCTRouterGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTRouterGroup = _Cdx6500PCTRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5)
)
_Cdx6500PCTBridgeGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTBridgeGroup = _Cdx6500PCTBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6)
)
_Cdx6500PCTNCRBSCDeviceGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTNCRBSCDeviceGroup = _Cdx6500PCTNCRBSCDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 7)
)
_Cdx6500PCTBSTDDeviceGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTBSTDDeviceGroup = _Cdx6500PCTBSTDDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8)
)
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_IsgIsdnCfgGroup_ObjectIdentity = ObjectIdentity
isgIsdnCfgGroup = _IsgIsdnCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19)
)
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500PSTRouterGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTRouterGroup = _Cdx6500PSTRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4)
)
_Cdx6500PSTBridgeGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTBridgeGroup = _Cdx6500PSTBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5)
)
_Cdx6500PSTLANConnectionGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTLANConnectionGroup = _Cdx6500PSTLANConnectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_IsgIsdnStatsGroup_ObjectIdentity = ObjectIdentity
isgIsdnStatsGroup = _IsgIsdnStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9)
)
_Cdx6500StatTFTPGroup_ObjectIdentity = ObjectIdentity
cdx6500StatTFTPGroup = _Cdx6500StatTFTPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3)
)
_Cdx6500StatNetworkSvcsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatNetworkSvcsGroup = _Cdx6500StatNetworkSvcsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4)
)
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContWANAdaptor_ObjectIdentity = ObjectIdentity
cdx6500ContWANAdaptor = _Cdx6500ContWANAdaptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 1)
)
_Cdx6500ContTFTP_ObjectIdentity = ObjectIdentity
cdx6500ContTFTP = _Cdx6500ContTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2)
)
_Cdx6500dsdControls_ObjectIdentity = ObjectIdentity
cdx6500dsdControls = _Cdx6500dsdControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 3)
)
_Cdx6500statControls_ObjectIdentity = ObjectIdentity
cdx6500statControls = _Cdx6500statControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 4)
)
_Cdx6500ContSDLC_ObjectIdentity = ObjectIdentity
cdx6500ContSDLC = _Cdx6500ContSDLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5)
)
_Cdx6500ContMX25_ObjectIdentity = ObjectIdentity
cdx6500ContMX25 = _Cdx6500ContMX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6)
)
_Cdx6500ContXDLC_ObjectIdentity = ObjectIdentity
cdx6500ContXDLC = _Cdx6500ContXDLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 7)
)
_IsgIsdnCtrlGroup_ObjectIdentity = ObjectIdentity
isgIsdnCtrlGroup = _IsgIsdnCtrlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CDX6500-SMI",
    **{"Counter16": Counter16,
       "Counter8": Counter8,
       "MacAddress": MacAddress,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500NodeMgmt": cdx6500NodeMgmt,
       "cdx6500NMSNMPGroup": cdx6500NMSNMPGroup,
       "cdx6500NMNodeParametersGroup": cdx6500NMNodeParametersGroup,
       "cdx6500NMDiagnosticsGroup": cdx6500NMDiagnosticsGroup,
       "cdx6500NMControlsGroup": cdx6500NMControlsGroup,
       "cdx6500NMDLSVGroup": cdx6500NMDLSVGroup,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500PCTBSC3270DeviceGroup": cdx6500PCTBSC3270DeviceGroup,
       "cdx6500PCTRouterGroup": cdx6500PCTRouterGroup,
       "cdx6500PCTBridgeGroup": cdx6500PCTBridgeGroup,
       "cdx6500PCTNCRBSCDeviceGroup": cdx6500PCTNCRBSCDeviceGroup,
       "cdx6500PCTBSTDDeviceGroup": cdx6500PCTBSTDDeviceGroup,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "isgIsdnCfgGroup": isgIsdnCfgGroup,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500PSTRouterGroup": cdx6500PSTRouterGroup,
       "cdx6500PSTBridgeGroup": cdx6500PSTBridgeGroup,
       "cdx6500PSTLANConnectionGroup": cdx6500PSTLANConnectionGroup,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "isgIsdnStatsGroup": isgIsdnStatsGroup,
       "cdx6500StatTFTPGroup": cdx6500StatTFTPGroup,
       "cdx6500StatNetworkSvcsGroup": cdx6500StatNetworkSvcsGroup,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContWANAdaptor": cdx6500ContWANAdaptor,
       "cdx6500ContTFTP": cdx6500ContTFTP,
       "cdx6500dsdControls": cdx6500dsdControls,
       "cdx6500statControls": cdx6500statControls,
       "cdx6500ContSDLC": cdx6500ContSDLC,
       "cdx6500ContMX25": cdx6500ContMX25,
       "cdx6500ContXDLC": cdx6500ContXDLC,
       "isgIsdnCtrlGroup": isgIsdnCtrlGroup}
)
