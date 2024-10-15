# SNMP MIB module (TWTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TWTRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:04 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 internet,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "internet",
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17)
)
_Dot1dBase_ObjectIdentity = ObjectIdentity
dot1dBase = _Dot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 1)
)
_Dot1dStp_ObjectIdentity = ObjectIdentity
dot1dStp = _Dot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 2)
)
_Dot1dStpPortTable_ObjectIdentity = ObjectIdentity
dot1dStpPortTable = _Dot1dStpPortTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 2, 15)
)
_Dot1dStpPortEntry_ObjectIdentity = ObjectIdentity
dot1dStpPortEntry = _Dot1dStpPortEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1)
)
_Dot1dStpPort_ObjectIdentity = ObjectIdentity
dot1dStpPort = _Dot1dStpPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 1)
)
_Dot1dSr_ObjectIdentity = ObjectIdentity
dot1dSr = _Dot1dSr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 3)
)
_Dot1dTp_ObjectIdentity = ObjectIdentity
dot1dTp = _Dot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 4)
)
_Dot1dStatic_ObjectIdentity = ObjectIdentity
dot1dStatic = _Dot1dStatic_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 5)
)
_SnmpDot3RptrMgt_ObjectIdentity = ObjectIdentity
snmpDot3RptrMgt = _SnmpDot3RptrMgt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22)
)
_RptrBasicPackage_ObjectIdentity = ObjectIdentity
rptrBasicPackage = _RptrBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1)
)
_RptrRptrInfo_ObjectIdentity = ObjectIdentity
rptrRptrInfo = _RptrRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 1)
)
_RptrGroupInfo_ObjectIdentity = ObjectIdentity
rptrGroupInfo = _RptrGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 2)
)
_RptrPortInfo_ObjectIdentity = ObjectIdentity
rptrPortInfo = _RptrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 3)
)
_RptrPortTable_ObjectIdentity = ObjectIdentity
rptrPortTable = _RptrPortTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1)
)
_RptrPortEntry_ObjectIdentity = ObjectIdentity
rptrPortEntry = _RptrPortEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1)
)
_RptrPortGroupIndex_ObjectIdentity = ObjectIdentity
rptrPortGroupIndex = _RptrPortGroupIndex_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 1)
)
_RptrPortIndex_ObjectIdentity = ObjectIdentity
rptrPortIndex = _RptrPortIndex_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 2)
)
_RptrMonitorPackage_ObjectIdentity = ObjectIdentity
rptrMonitorPackage = _RptrMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2)
)
_RptrMonitorRptrInfo_ObjectIdentity = ObjectIdentity
rptrMonitorRptrInfo = _RptrMonitorRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 1)
)
_RptrMonitorGroupInfo_ObjectIdentity = ObjectIdentity
rptrMonitorGroupInfo = _RptrMonitorGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 2)
)
_RptrMonitorPortInfo_ObjectIdentity = ObjectIdentity
rptrMonitorPortInfo = _RptrMonitorPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 3)
)
_RptrAddrTrackPackage_ObjectIdentity = ObjectIdentity
rptrAddrTrackPackage = _RptrAddrTrackPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3)
)
_RptrAddrTrackRptrInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackRptrInfo = _RptrAddrTrackRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 1)
)
_RptrAddrTrackGroupInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackGroupInfo = _RptrAddrTrackGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 2)
)
_RptrAddrTrackPortInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackPortInfo = _RptrAddrTrackPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 3)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Npi_ObjectIdentity = ObjectIdentity
npi = _Npi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 1)
)
_DevDeviceInfo_ObjectIdentity = ObjectIdentity
devDeviceInfo = _DevDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 1, 1)
)
_DevMonitorInfo_ObjectIdentity = ObjectIdentity
devMonitorInfo = _DevMonitorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 1, 2)
)
_DevMonTrapReportLevel_ObjectIdentity = ObjectIdentity
devMonTrapReportLevel = _DevMonTrapReportLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 1, 2, 2)
)
_DevActionInfo_ObjectIdentity = ObjectIdentity
devActionInfo = _DevActionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 1, 3)
)
_Npi_Switching_MIB_ObjectIdentity = ObjectIdentity
npi_Switching_MIB = _Npi_Switching_MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2)
)
_Switch_Common_MIB_ObjectIdentity = ObjectIdentity
switch_Common_MIB = _Switch_Common_MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1)
)
_SwitchBasicHubInfo_ObjectIdentity = ObjectIdentity
switchBasicHubInfo = _SwitchBasicHubInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 1)
)
_BasicSwitchPowerState_ObjectIdentity = ObjectIdentity
basicSwitchPowerState = _BasicSwitchPowerState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 1, 14)
)
_SwitchBasicPortInfo_ObjectIdentity = ObjectIdentity
switchBasicPortInfo = _SwitchBasicPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 2)
)
_SwitchPortTable_ObjectIdentity = ObjectIdentity
switchPortTable = _SwitchPortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1)
)
_SwitchPortEntry_ObjectIdentity = ObjectIdentity
switchPortEntry = _SwitchPortEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1, 1)
)
_SwitchPortIndex_ObjectIdentity = ObjectIdentity
switchPortIndex = _SwitchPortIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1, 1, 1)
)
_SwitchPortFullDuplex_ObjectIdentity = ObjectIdentity
switchPortFullDuplex = _SwitchPortFullDuplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1, 1, 6)
)
_SwitchPortFlowControl_ObjectIdentity = ObjectIdentity
switchPortFlowControl = _SwitchPortFlowControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1, 1, 7)
)
_SwitchPortSpeed_ObjectIdentity = ObjectIdentity
switchPortSpeed = _SwitchPortSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1, 1, 13)
)
_SwitchAddrTrackInfo_ObjectIdentity = ObjectIdentity
switchAddrTrackInfo = _SwitchAddrTrackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 3)
)
_SwitchAddrPortInfo_ObjectIdentity = ObjectIdentity
switchAddrPortInfo = _SwitchAddrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 3, 1)
)
_SwitchAddrPortTable_ObjectIdentity = ObjectIdentity
switchAddrPortTable = _SwitchAddrPortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 3, 1, 1)
)
_SwitchAddrPortEntry_ObjectIdentity = ObjectIdentity
switchAddrPortEntry = _SwitchAddrPortEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 3, 1, 1, 1)
)
_SwitchAddrPortIndex_ObjectIdentity = ObjectIdentity
switchAddrPortIndex = _SwitchAddrPortIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 3, 1, 1, 1, 1)
)
_SwitchAddrPortPackMaxCount_ObjectIdentity = ObjectIdentity
switchAddrPortPackMaxCount = _SwitchAddrPortPackMaxCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 3, 1, 1, 1, 6)
)
_SwitchAddrStaticInfo_ObjectIdentity = ObjectIdentity
switchAddrStaticInfo = _SwitchAddrStaticInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 4)
)
_SwitchAddrStaticPackMaxCount_ObjectIdentity = ObjectIdentity
switchAddrStaticPackMaxCount = _SwitchAddrStaticPackMaxCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 4, 4)
)
_SwitchAddrStaticTable_ObjectIdentity = ObjectIdentity
switchAddrStaticTable = _SwitchAddrStaticTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 4, 6)
)
_SwitchAddrStaticEntry_ObjectIdentity = ObjectIdentity
switchAddrStaticEntry = _SwitchAddrStaticEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 4, 6, 1)
)
_SwitchAddrStaticIndex_ObjectIdentity = ObjectIdentity
switchAddrStaticIndex = _SwitchAddrStaticIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 4, 6, 1, 1)
)
_SwitchAddrStaticSetAddress_ObjectIdentity = ObjectIdentity
switchAddrStaticSetAddress = _SwitchAddrStaticSetAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 4, 6, 1, 2)
)
_SwitchThresholdInfo_ObjectIdentity = ObjectIdentity
switchThresholdInfo = _SwitchThresholdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 5)
)
_BasicThresholdTable_ObjectIdentity = ObjectIdentity
basicThresholdTable = _BasicThresholdTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4)
)
_BasicThresholdTableEntry_ObjectIdentity = ObjectIdentity
basicThresholdTableEntry = _BasicThresholdTableEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4, 1)
)
_SwitchThresholdUnit_ObjectIdentity = ObjectIdentity
switchThresholdUnit = _SwitchThresholdUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4, 1, 4)
)
_SwitchThresholdPort_ObjectIdentity = ObjectIdentity
switchThresholdPort = _SwitchThresholdPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4, 1, 5)
)
_SwitchThresholdType_ObjectIdentity = ObjectIdentity
switchThresholdType = _SwitchThresholdType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4, 1, 6)
)
_SwitchThresholdCounter_ObjectIdentity = ObjectIdentity
switchThresholdCounter = _SwitchThresholdCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4, 1, 9)
)
_SwitchPowerLinkInfo_ObjectIdentity = ObjectIdentity
switchPowerLinkInfo = _SwitchPowerLinkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 9)
)
_SwitchPowerLinkOperationMode_ObjectIdentity = ObjectIdentity
switchPowerLinkOperationMode = _SwitchPowerLinkOperationMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 9, 2)
)
_SwitchPowerLinkUserSettingInfo_ObjectIdentity = ObjectIdentity
switchPowerLinkUserSettingInfo = _SwitchPowerLinkUserSettingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 9, 5)
)
_SwitchPowerLinkUserOperationMode_ObjectIdentity = ObjectIdentity
switchPowerLinkUserOperationMode = _SwitchPowerLinkUserOperationMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 9, 5, 1)
)
_SwitchPowerLinkUserRange_ObjectIdentity = ObjectIdentity
switchPowerLinkUserRange = _SwitchPowerLinkUserRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 9, 5, 2)
)
_SwitchPowerLinkStatus_ObjectIdentity = ObjectIdentity
switchPowerLinkStatus = _SwitchPowerLinkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 1, 9, 7)
)
_Switch_Cascade_MIB_ObjectIdentity = ObjectIdentity
switch_Cascade_MIB = _Switch_Cascade_MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2)
)
_SwitchCmsBasicPackage_ObjectIdentity = ObjectIdentity
switchCmsBasicPackage = _SwitchCmsBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 1)
)
_SwitchCmsBasicClusterInfo_ObjectIdentity = ObjectIdentity
switchCmsBasicClusterInfo = _SwitchCmsBasicClusterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 1)
)
_SwitchCmsBasicUnitInfo_ObjectIdentity = ObjectIdentity
switchCmsBasicUnitInfo = _SwitchCmsBasicUnitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 2)
)
_BasicUnitTable_ObjectIdentity = ObjectIdentity
basicUnitTable = _BasicUnitTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 2, 1)
)
_BasicUnitEntry_ObjectIdentity = ObjectIdentity
basicUnitEntry = _BasicUnitEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 2, 1, 1)
)
_BasicUnitIndex_ObjectIdentity = ObjectIdentity
basicUnitIndex = _BasicUnitIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 2, 1, 1, 1)
)
_SwitchCmsBasicPortInfo_ObjectIdentity = ObjectIdentity
switchCmsBasicPortInfo = _SwitchCmsBasicPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 3)
)
_BasicPortTable_ObjectIdentity = ObjectIdentity
basicPortTable = _BasicPortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 3, 1)
)
_BasicPortEntry_ObjectIdentity = ObjectIdentity
basicPortEntry = _BasicPortEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 3, 1, 1)
)
_BasicPortUnitIndex_ObjectIdentity = ObjectIdentity
basicPortUnitIndex = _BasicPortUnitIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 3, 1, 1, 1)
)
_BasicPortIndex_ObjectIdentity = ObjectIdentity
basicPortIndex = _BasicPortIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 3, 1, 1, 2)
)
_SwitchCmsAddrTrackPackage_ObjectIdentity = ObjectIdentity
switchCmsAddrTrackPackage = _SwitchCmsAddrTrackPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 3)
)
_SwitchCmsAddrTrackPortInfo_ObjectIdentity = ObjectIdentity
switchCmsAddrTrackPortInfo = _SwitchCmsAddrTrackPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 3, 3)
)
_AddrTrackPortTable_ObjectIdentity = ObjectIdentity
addrTrackPortTable = _AddrTrackPortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 3, 3, 1)
)
_AddrTrackPortEntry_ObjectIdentity = ObjectIdentity
addrTrackPortEntry = _AddrTrackPortEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 3, 3, 1, 1)
)
_AddrTrackPortUnitIndex_ObjectIdentity = ObjectIdentity
addrTrackPortUnitIndex = _AddrTrackPortUnitIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 3, 3, 1, 1, 1)
)
_AddrTrackPortPortIndex_ObjectIdentity = ObjectIdentity
addrTrackPortPortIndex = _AddrTrackPortPortIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 2, 3, 3, 1, 1, 2)
)
_Switch_FE1200_ObjectIdentity = ObjectIdentity
switch_FE1200 = _Switch_FE1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 3)
)
_Switch_TidalWave_ObjectIdentity = ObjectIdentity
switch_TidalWave = _Switch_TidalWave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10)
)
_Switch_FE1200PLUS_ObjectIdentity = ObjectIdentity
switch_FE1200PLUS = _Switch_FE1200PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1)
)
_Switch_DS24_ObjectIdentity = ObjectIdentity
switch_DS24 = _Switch_DS24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13)
)
_SwitchSecureAddrInfo_ObjectIdentity = ObjectIdentity
switchSecureAddrInfo = _SwitchSecureAddrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 6)
)
_SwitchAddrSecureTable_ObjectIdentity = ObjectIdentity
switchAddrSecureTable = _SwitchAddrSecureTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 6, 4)
)
_SwitchAddrSecureEntry_ObjectIdentity = ObjectIdentity
switchAddrSecureEntry = _SwitchAddrSecureEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 6, 4, 1)
)
_SwitchAddrSecurePortIndex_ObjectIdentity = ObjectIdentity
switchAddrSecurePortIndex = _SwitchAddrSecurePortIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 6, 4, 1, 1)
)
_SwitchAddrSecureIndex_ObjectIdentity = ObjectIdentity
switchAddrSecureIndex = _SwitchAddrSecureIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 6, 4, 1, 2)
)
_SwitchAddrSecureAddress_ObjectIdentity = ObjectIdentity
switchAddrSecureAddress = _SwitchAddrSecureAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 6, 4, 1, 3)
)
_SwitchPortMonitorInfo_ObjectIdentity = ObjectIdentity
switchPortMonitorInfo = _SwitchPortMonitorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 7)
)
_SwitchPortMonitorTable_ObjectIdentity = ObjectIdentity
switchPortMonitorTable = _SwitchPortMonitorTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 7, 4)
)
_SwitchPortMonitorEntry_ObjectIdentity = ObjectIdentity
switchPortMonitorEntry = _SwitchPortMonitorEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 7, 4, 1)
)
_SwitchPortMonitorIndex_ObjectIdentity = ObjectIdentity
switchPortMonitorIndex = _SwitchPortMonitorIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 7, 4, 1, 1)
)
_SwitchPortMonitorMessageStatus_ObjectIdentity = ObjectIdentity
switchPortMonitorMessageStatus = _SwitchPortMonitorMessageStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 7, 4, 1, 3)
)
_SwitchVirtualLanInfo_ObjectIdentity = ObjectIdentity
switchVirtualLanInfo = _SwitchVirtualLanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 8)
)
_SwitchVirtualLanMessage_ObjectIdentity = ObjectIdentity
switchVirtualLanMessage = _SwitchVirtualLanMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 8, 5)
)
_SwitchTrapInfo_ObjectIdentity = ObjectIdentity
switchTrapInfo = _SwitchTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 13)
)
_SwitchTrapStaticCollisionAddress_ObjectIdentity = ObjectIdentity
switchTrapStaticCollisionAddress = _SwitchTrapStaticCollisionAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 13, 1)
)
_SwitchTrapStaticCollisionAddress2_ObjectIdentity = ObjectIdentity
switchTrapStaticCollisionAddress2 = _SwitchTrapStaticCollisionAddress2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 13, 2)
)
_SwitchTrapFilterCollisionAddress_ObjectIdentity = ObjectIdentity
switchTrapFilterCollisionAddress = _SwitchTrapFilterCollisionAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1101, 2, 13, 13, 3)
)

# Managed Objects groups


# Notification objects

newRoot = NotificationType(
    (1, 3, 6, 1, 2, 1, 17, 0, 1)
)
newRoot.setObjects(
    ("TWTRAP-MIB", "devMonTrapReportLevel")
)
if mibBuilder.loadTexts:
    newRoot.setStatus(
        ""
    )

topologyChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 17, 0, 2)
)
topologyChange.setObjects(
    ("TWTRAP-MIB", "devMonTrapReportLevel")
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        ""
    )

rptr_Reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 256)
)
rptr_Reset.setObjects(
    ("TWTRAP-MIB", "devMonTrapReportLevel")
)
if mibBuilder.loadTexts:
    rptr_Reset.setStatus(
        ""
    )

rptr_FReset1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 257)
)
rptr_FReset1.setObjects(
    ("TWTRAP-MIB", "devMonTrapReportLevel")
)
if mibBuilder.loadTexts:
    rptr_FReset1.setStatus(
        ""
    )

rptr_Port_Enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 288)
)
rptr_Port_Enabled.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "rptrPortGroupIndex"),
        ("TWTRAP-MIB", "rptrPortIndex"))
)
if mibBuilder.loadTexts:
    rptr_Port_Enabled.setStatus(
        ""
    )

rptr_Port_Disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 289)
)
rptr_Port_Disabled.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "rptrPortGroupIndex"),
        ("TWTRAP-MIB", "rptrPortIndex"))
)
if mibBuilder.loadTexts:
    rptr_Port_Disabled.setStatus(
        ""
    )

rptr_Port_Link_Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 292)
)
rptr_Port_Link_Up.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "rptrPortGroupIndex"),
        ("TWTRAP-MIB", "rptrPortIndex"))
)
if mibBuilder.loadTexts:
    rptr_Port_Link_Up.setStatus(
        ""
    )

rptr_Port_Link_Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 293)
)
rptr_Port_Link_Down.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "rptrPortGroupIndex"),
        ("TWTRAP-MIB", "rptrPortIndex"))
)
if mibBuilder.loadTexts:
    rptr_Port_Link_Down.setStatus(
        ""
    )

switch_Unit_Power_Status = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 512)
)
switch_Unit_Power_Status.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "basicSwitchPowerState"))
)
if mibBuilder.loadTexts:
    switch_Unit_Power_Status.setStatus(
        ""
    )

switch_Port_Monitor_Rx_CBPDU = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 514)
)
switch_Port_Monitor_Rx_CBPDU.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "dot1dStpPort"),
        ("TWTRAP-MIB", "switchPortMonitorIndex"))
)
if mibBuilder.loadTexts:
    switch_Port_Monitor_Rx_CBPDU.setStatus(
        ""
    )

switch_Port_Duplex_Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 532)
)
switch_Port_Duplex_Change.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchPortIndex"),
        ("TWTRAP-MIB", "switchPortFullDuplex"))
)
if mibBuilder.loadTexts:
    switch_Port_Duplex_Change.setStatus(
        ""
    )

switch_Port_Speed_Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 533)
)
switch_Port_Speed_Change.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchPortIndex"),
        ("TWTRAP-MIB", "switchPortSpeed"))
)
if mibBuilder.loadTexts:
    switch_Port_Speed_Change.setStatus(
        ""
    )

switch_Port_FlowControl_Changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 534)
)
switch_Port_FlowControl_Changed.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchPortIndex"),
        ("TWTRAP-MIB", "switchPortFlowControl"))
)
if mibBuilder.loadTexts:
    switch_Port_FlowControl_Changed.setStatus(
        ""
    )

switch_Unit_Accumulate_reach = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 576)
)
switch_Unit_Accumulate_reach.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchThresholdUnit"),
        ("TWTRAP-MIB", "switchThresholdType"),
        ("TWTRAP-MIB", "switchThresholdCounter"))
)
if mibBuilder.loadTexts:
    switch_Unit_Accumulate_reach.setStatus(
        ""
    )

switch_Unit_Rate_notification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 577)
)
switch_Unit_Rate_notification.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchThresholdUnit"),
        ("TWTRAP-MIB", "switchThresholdType"),
        ("TWTRAP-MIB", "switchThresholdCounter"))
)
if mibBuilder.loadTexts:
    switch_Unit_Rate_notification.setStatus(
        ""
    )

switch_Port_Accumulate_reach = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 579)
)
switch_Port_Accumulate_reach.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchThresholdUnit"),
        ("TWTRAP-MIB", "switchThresholdPort"),
        ("TWTRAP-MIB", "switchThresholdType"),
        ("TWTRAP-MIB", "switchThresholdCounter"))
)
if mibBuilder.loadTexts:
    switch_Port_Accumulate_reach.setStatus(
        ""
    )

switch_Port_Rate_notification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 580)
)
switch_Port_Rate_notification.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchThresholdUnit"),
        ("TWTRAP-MIB", "switchThresholdPort"),
        ("TWTRAP-MIB", "switchThresholdType"),
        ("TWTRAP-MIB", "switchThresholdCounter"))
)
if mibBuilder.loadTexts:
    switch_Port_Rate_notification.setStatus(
        ""
    )

switch_Security_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 592)
)
switch_Security_On.setObjects(
    ("TWTRAP-MIB", "devMonTrapReportLevel")
)
if mibBuilder.loadTexts:
    switch_Security_On.setStatus(
        ""
    )

switch_Security_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 593)
)
switch_Security_Off.setObjects(
    ("TWTRAP-MIB", "devMonTrapReportLevel")
)
if mibBuilder.loadTexts:
    switch_Security_Off.setStatus(
        ""
    )

switch_Security_Addr_Collision = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 595)
)
switch_Security_Addr_Collision.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchTrapFilterCollisionAddress"),
        ("TWTRAP-MIB", "switchAddrSecurePortIndex"),
        ("TWTRAP-MIB", "switchAddrSecureIndex"),
        ("TWTRAP-MIB", "switchAddrSecureAddress"))
)
if mibBuilder.loadTexts:
    switch_Security_Addr_Collision.setStatus(
        ""
    )

switch_Security_Reserved_Addr_Collision = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 596)
)
switch_Security_Reserved_Addr_Collision.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchTrapFilterCollisionAddress"),
        ("TWTRAP-MIB", "switchAddrStaticIndex"),
        ("TWTRAP-MIB", "switchAddrStaticSetAddress"))
)
if mibBuilder.loadTexts:
    switch_Security_Reserved_Addr_Collision.setStatus(
        ""
    )

switch_Port_Monitor_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 608)
)
switch_Port_Monitor_On.setObjects(
    ("TWTRAP-MIB", "devMonTrapReportLevel")
)
if mibBuilder.loadTexts:
    switch_Port_Monitor_On.setStatus(
        ""
    )

switch_Port_Monitor_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 609)
)
switch_Port_Monitor_Off.setObjects(
    ("TWTRAP-MIB", "devMonTrapReportLevel")
)
if mibBuilder.loadTexts:
    switch_Port_Monitor_Off.setStatus(
        ""
    )

switch_Port_Monitor_Port_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 610)
)
switch_Port_Monitor_Port_On.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchPortIndex"))
)
if mibBuilder.loadTexts:
    switch_Port_Monitor_Port_On.setStatus(
        ""
    )

switch_Port_Monitor_Port_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 611)
)
switch_Port_Monitor_Port_Off.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchPortIndex"))
)
if mibBuilder.loadTexts:
    switch_Port_Monitor_Port_Off.setStatus(
        ""
    )

switch_Port_Monitor_Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 612)
)
switch_Port_Monitor_Active.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchPortMonitorIndex"))
)
if mibBuilder.loadTexts:
    switch_Port_Monitor_Active.setStatus(
        ""
    )

switch_Port_Monitor_Removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 613)
)
switch_Port_Monitor_Removed.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchPortMonitorIndex"))
)
if mibBuilder.loadTexts:
    switch_Port_Monitor_Removed.setStatus(
        ""
    )

switch_Port_Monitor_Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 614)
)
switch_Port_Monitor_Error.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchPortMonitorIndex"),
        ("TWTRAP-MIB", "switchPortMonitorMessageStatus"))
)
if mibBuilder.loadTexts:
    switch_Port_Monitor_Error.setStatus(
        ""
    )

switch_Virtual_LAN_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 624)
)
switch_Virtual_LAN_On.setObjects(
    ("TWTRAP-MIB", "devMonTrapReportLevel")
)
if mibBuilder.loadTexts:
    switch_Virtual_LAN_On.setStatus(
        ""
    )

switch_Virtual_LAN_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 625)
)
switch_Virtual_LAN_Off.setObjects(
    ("TWTRAP-MIB", "devMonTrapReportLevel")
)
if mibBuilder.loadTexts:
    switch_Virtual_LAN_Off.setStatus(
        ""
    )

switch_VL_Port_On = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 626)
)
switch_VL_Port_On.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchPortIndex"))
)
if mibBuilder.loadTexts:
    switch_VL_Port_On.setStatus(
        ""
    )

switch_VL_Port_Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 1101, 2, 10, 1, 0, 627)
)
switch_VL_Port_Off.setObjects(
      *(("TWTRAP-MIB", "devMonTrapReportLevel"),
        ("TWTRAP-MIB", "switchPortIndex"))
)
if mibBuilder.loadTexts:
    switch_VL_Port_Off.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TWTRAP-MIB",
    **{"MacAddress": MacAddress,
       "directory": directory,
       "mgmt": mgmt,
       "mib-2": mib_2,
       "dot1dBridge": dot1dBridge,
       "newRoot": newRoot,
       "topologyChange": topologyChange,
       "dot1dBase": dot1dBase,
       "dot1dStp": dot1dStp,
       "dot1dStpPortTable": dot1dStpPortTable,
       "dot1dStpPortEntry": dot1dStpPortEntry,
       "dot1dStpPort": dot1dStpPort,
       "dot1dSr": dot1dSr,
       "dot1dTp": dot1dTp,
       "dot1dStatic": dot1dStatic,
       "snmpDot3RptrMgt": snmpDot3RptrMgt,
       "rptrBasicPackage": rptrBasicPackage,
       "rptrRptrInfo": rptrRptrInfo,
       "rptrGroupInfo": rptrGroupInfo,
       "rptrPortInfo": rptrPortInfo,
       "rptrPortTable": rptrPortTable,
       "rptrPortEntry": rptrPortEntry,
       "rptrPortGroupIndex": rptrPortGroupIndex,
       "rptrPortIndex": rptrPortIndex,
       "rptrMonitorPackage": rptrMonitorPackage,
       "rptrMonitorRptrInfo": rptrMonitorRptrInfo,
       "rptrMonitorGroupInfo": rptrMonitorGroupInfo,
       "rptrMonitorPortInfo": rptrMonitorPortInfo,
       "rptrAddrTrackPackage": rptrAddrTrackPackage,
       "rptrAddrTrackRptrInfo": rptrAddrTrackRptrInfo,
       "rptrAddrTrackGroupInfo": rptrAddrTrackGroupInfo,
       "rptrAddrTrackPortInfo": rptrAddrTrackPortInfo,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "npi": npi,
       "common": common,
       "devDeviceInfo": devDeviceInfo,
       "devMonitorInfo": devMonitorInfo,
       "devMonTrapReportLevel": devMonTrapReportLevel,
       "devActionInfo": devActionInfo,
       "npi-Switching-MIB": npi_Switching_MIB,
       "switch-Common-MIB": switch_Common_MIB,
       "switchBasicHubInfo": switchBasicHubInfo,
       "basicSwitchPowerState": basicSwitchPowerState,
       "switchBasicPortInfo": switchBasicPortInfo,
       "switchPortTable": switchPortTable,
       "switchPortEntry": switchPortEntry,
       "switchPortIndex": switchPortIndex,
       "switchPortFullDuplex": switchPortFullDuplex,
       "switchPortFlowControl": switchPortFlowControl,
       "switchPortSpeed": switchPortSpeed,
       "switchAddrTrackInfo": switchAddrTrackInfo,
       "switchAddrPortInfo": switchAddrPortInfo,
       "switchAddrPortTable": switchAddrPortTable,
       "switchAddrPortEntry": switchAddrPortEntry,
       "switchAddrPortIndex": switchAddrPortIndex,
       "switchAddrPortPackMaxCount": switchAddrPortPackMaxCount,
       "switchAddrStaticInfo": switchAddrStaticInfo,
       "switchAddrStaticPackMaxCount": switchAddrStaticPackMaxCount,
       "switchAddrStaticTable": switchAddrStaticTable,
       "switchAddrStaticEntry": switchAddrStaticEntry,
       "switchAddrStaticIndex": switchAddrStaticIndex,
       "switchAddrStaticSetAddress": switchAddrStaticSetAddress,
       "switchThresholdInfo": switchThresholdInfo,
       "basicThresholdTable": basicThresholdTable,
       "basicThresholdTableEntry": basicThresholdTableEntry,
       "switchThresholdUnit": switchThresholdUnit,
       "switchThresholdPort": switchThresholdPort,
       "switchThresholdType": switchThresholdType,
       "switchThresholdCounter": switchThresholdCounter,
       "switchPowerLinkInfo": switchPowerLinkInfo,
       "switchPowerLinkOperationMode": switchPowerLinkOperationMode,
       "switchPowerLinkUserSettingInfo": switchPowerLinkUserSettingInfo,
       "switchPowerLinkUserOperationMode": switchPowerLinkUserOperationMode,
       "switchPowerLinkUserRange": switchPowerLinkUserRange,
       "switchPowerLinkStatus": switchPowerLinkStatus,
       "switch-Cascade-MIB": switch_Cascade_MIB,
       "switchCmsBasicPackage": switchCmsBasicPackage,
       "switchCmsBasicClusterInfo": switchCmsBasicClusterInfo,
       "switchCmsBasicUnitInfo": switchCmsBasicUnitInfo,
       "basicUnitTable": basicUnitTable,
       "basicUnitEntry": basicUnitEntry,
       "basicUnitIndex": basicUnitIndex,
       "switchCmsBasicPortInfo": switchCmsBasicPortInfo,
       "basicPortTable": basicPortTable,
       "basicPortEntry": basicPortEntry,
       "basicPortUnitIndex": basicPortUnitIndex,
       "basicPortIndex": basicPortIndex,
       "switchCmsAddrTrackPackage": switchCmsAddrTrackPackage,
       "switchCmsAddrTrackPortInfo": switchCmsAddrTrackPortInfo,
       "addrTrackPortTable": addrTrackPortTable,
       "addrTrackPortEntry": addrTrackPortEntry,
       "addrTrackPortUnitIndex": addrTrackPortUnitIndex,
       "addrTrackPortPortIndex": addrTrackPortPortIndex,
       "switch-FE1200": switch_FE1200,
       "switch-TidalWave": switch_TidalWave,
       "switch-FE1200PLUS": switch_FE1200PLUS,
       "rptr-Reset": rptr_Reset,
       "rptr-FReset1": rptr_FReset1,
       "rptr-Port-Enabled": rptr_Port_Enabled,
       "rptr-Port-Disabled": rptr_Port_Disabled,
       "rptr-Port-Link-Up": rptr_Port_Link_Up,
       "rptr-Port-Link-Down": rptr_Port_Link_Down,
       "switch-Unit-Power-Status": switch_Unit_Power_Status,
       "switch-Port-Monitor-Rx-CBPDU": switch_Port_Monitor_Rx_CBPDU,
       "switch-Port-Duplex-Change": switch_Port_Duplex_Change,
       "switch-Port-Speed-Change": switch_Port_Speed_Change,
       "switch-Port-FlowControl-Changed": switch_Port_FlowControl_Changed,
       "switch-Unit-Accumulate-reach": switch_Unit_Accumulate_reach,
       "switch-Unit-Rate-notification": switch_Unit_Rate_notification,
       "switch-Port-Accumulate-reach": switch_Port_Accumulate_reach,
       "switch-Port-Rate-notification": switch_Port_Rate_notification,
       "switch-Security-On": switch_Security_On,
       "switch-Security-Off": switch_Security_Off,
       "switch-Security-Addr-Collision": switch_Security_Addr_Collision,
       "switch-Security-Reserved-Addr-Collision": switch_Security_Reserved_Addr_Collision,
       "switch-Port-Monitor-On": switch_Port_Monitor_On,
       "switch-Port-Monitor-Off": switch_Port_Monitor_Off,
       "switch-Port-Monitor-Port-On": switch_Port_Monitor_Port_On,
       "switch-Port-Monitor-Port-Off": switch_Port_Monitor_Port_Off,
       "switch-Port-Monitor-Active": switch_Port_Monitor_Active,
       "switch-Port-Monitor-Removed": switch_Port_Monitor_Removed,
       "switch-Port-Monitor-Error": switch_Port_Monitor_Error,
       "switch-Virtual-LAN-On": switch_Virtual_LAN_On,
       "switch-Virtual-LAN-Off": switch_Virtual_LAN_Off,
       "switch-VL-Port-On": switch_VL_Port_On,
       "switch-VL-Port-Off": switch_VL_Port_Off,
       "switch-DS24": switch_DS24,
       "switchSecureAddrInfo": switchSecureAddrInfo,
       "switchAddrSecureTable": switchAddrSecureTable,
       "switchAddrSecureEntry": switchAddrSecureEntry,
       "switchAddrSecurePortIndex": switchAddrSecurePortIndex,
       "switchAddrSecureIndex": switchAddrSecureIndex,
       "switchAddrSecureAddress": switchAddrSecureAddress,
       "switchPortMonitorInfo": switchPortMonitorInfo,
       "switchPortMonitorTable": switchPortMonitorTable,
       "switchPortMonitorEntry": switchPortMonitorEntry,
       "switchPortMonitorIndex": switchPortMonitorIndex,
       "switchPortMonitorMessageStatus": switchPortMonitorMessageStatus,
       "switchVirtualLanInfo": switchVirtualLanInfo,
       "switchVirtualLanMessage": switchVirtualLanMessage,
       "switchTrapInfo": switchTrapInfo,
       "switchTrapStaticCollisionAddress": switchTrapStaticCollisionAddress,
       "switchTrapStaticCollisionAddress2": switchTrapStaticCollisionAddress2,
       "switchTrapFilterCollisionAddress": switchTrapFilterCollisionAddress}
)
