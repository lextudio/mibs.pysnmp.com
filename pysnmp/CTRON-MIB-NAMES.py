# SNMP MIB module (CTRON-MIB-NAMES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-MIB-NAMES
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:59 2024
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

(cabletron,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "cabletron")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4)
)
_Ctron_ObjectIdentity = ObjectIdentity
ctron = _Ctron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1)
)
_CtPhysical_ObjectIdentity = ObjectIdentity
ctPhysical = _CtPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1)
)
_RepeaterRev4_ObjectIdentity = ObjectIdentity
repeaterRev4 = _RepeaterRev4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2)
)
_CtPhysRptrMim_ObjectIdentity = ObjectIdentity
ctPhysRptrMim = _CtPhysRptrMim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 3)
)
_CtPhysModule_ObjectIdentity = ObjectIdentity
ctPhysModule = _CtPhysModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4)
)
_CtPModuleETWMIM_ObjectIdentity = ObjectIdentity
ctPModuleETWMIM = _CtPModuleETWMIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1)
)
_CtDevice_ObjectIdentity = ObjectIdentity
ctDevice = _CtDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5)
)
_CtDot5PhysMgmt_ObjectIdentity = ObjectIdentity
ctDot5PhysMgmt = _CtDot5PhysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6)
)
_Ctps_ObjectIdentity = ObjectIdentity
ctps = _Ctps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7)
)
_Ctenv_ObjectIdentity = ObjectIdentity
ctenv = _Ctenv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8)
)
_CtChassis2_ObjectIdentity = ObjectIdentity
ctChassis2 = _CtChassis2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9)
)
_CtUPS_ObjectIdentity = ObjectIdentity
ctUPS = _CtUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10)
)
_CtTRStnAssign_ObjectIdentity = ObjectIdentity
ctTRStnAssign = _CtTRStnAssign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11)
)
_CtResource_ObjectIdentity = ObjectIdentity
ctResource = _CtResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12)
)
_CtIFRemap_ObjectIdentity = ObjectIdentity
ctIFRemap = _CtIFRemap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13)
)
_CtIFRemap2_ObjectIdentity = ObjectIdentity
ctIFRemap2 = _CtIFRemap2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14)
)
_CtOrpHSIM_ObjectIdentity = ObjectIdentity
ctOrpHSIM = _CtOrpHSIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15)
)
_CtPortMap_ObjectIdentity = ObjectIdentity
ctPortMap = _CtPortMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16)
)
_CtHSIMPhysMib_ObjectIdentity = ObjectIdentity
ctHSIMPhysMib = _CtHSIMPhysMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17)
)
_CtCMM_ObjectIdentity = ObjectIdentity
ctCMM = _CtCMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18)
)
_CtDataLink_ObjectIdentity = ObjectIdentity
ctDataLink = _CtDataLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2)
)
_Dot5_ObjectIdentity = ObjectIdentity
dot5 = _Dot5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1)
)
_Ctsmtmib_ObjectIdentity = ObjectIdentity
ctsmtmib = _Ctsmtmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2)
)
_CtBridge_ObjectIdentity = ObjectIdentity
ctBridge = _CtBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3)
)
_CtEthernet_ObjectIdentity = ObjectIdentity
ctEthernet = _CtEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4)
)
_CtCSMACD_ObjectIdentity = ObjectIdentity
ctCSMACD = _CtCSMACD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1)
)
_CtEthernetCtlParameters_ObjectIdentity = ObjectIdentity
ctEthernetCtlParameters = _CtEthernetCtlParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2)
)
_CtFDDI_ObjectIdentity = ObjectIdentity
ctFDDI = _CtFDDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5)
)
_CtFDDIFnb_ObjectIdentity = ObjectIdentity
ctFDDIFnb = _CtFDDIFnb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1)
)
_CtFDDIStats_ObjectIdentity = ObjectIdentity
ctFDDIStats = _CtFDDIStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2)
)
_CtTokenRing_ObjectIdentity = ObjectIdentity
ctTokenRing = _CtTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6)
)
_CtTokenRingFnb_ObjectIdentity = ObjectIdentity
ctTokenRingFnb = _CtTokenRingFnb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1)
)
_CtronWan_ObjectIdentity = ObjectIdentity
ctronWan = _CtronWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7)
)
_CtWan_ObjectIdentity = ObjectIdentity
ctWan = _CtWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1)
)
_CtRemoteAccess_ObjectIdentity = ObjectIdentity
ctRemoteAccess = _CtRemoteAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2)
)
_CtWanServices_ObjectIdentity = ObjectIdentity
ctWanServices = _CtWanServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3)
)
_CtDLSW_ObjectIdentity = ObjectIdentity
ctDLSW = _CtDLSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8)
)
_CtFastEthernet_ObjectIdentity = ObjectIdentity
ctFastEthernet = _CtFastEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9)
)
_CtATM_ObjectIdentity = ObjectIdentity
ctATM = _CtATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10)
)
_CtATMConfig_ObjectIdentity = ObjectIdentity
ctATMConfig = _CtATMConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1)
)
_CtSwitch_ObjectIdentity = ObjectIdentity
ctSwitch = _CtSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11)
)
_CtsfSwitch_ObjectIdentity = ObjectIdentity
ctsfSwitch = _CtsfSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1)
)
_CtSFCS_ObjectIdentity = ObjectIdentity
ctSFCS = _CtSFCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1)
)
_CtFPS_ObjectIdentity = ObjectIdentity
ctFPS = _CtFPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2)
)
_CtINB_ObjectIdentity = ObjectIdentity
ctINB = _CtINB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12)
)
_CtINBinfo_ObjectIdentity = ObjectIdentity
ctINBinfo = _CtINBinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1)
)
_CtINBinfo2_ObjectIdentity = ObjectIdentity
ctINBinfo2 = _CtINBinfo2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2)
)
_CtBroadcast_ObjectIdentity = ObjectIdentity
ctBroadcast = _CtBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13)
)
_CtPriorityExt_ObjectIdentity = ObjectIdentity
ctPriorityExt = _CtPriorityExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14)
)
_CtFPSServices_ObjectIdentity = ObjectIdentity
ctFPSServices = _CtFPSServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15)
)
_CtVlanExt_ObjectIdentity = ObjectIdentity
ctVlanExt = _CtVlanExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16)
)
_CtronVVD_ObjectIdentity = ObjectIdentity
ctronVVD = _CtronVVD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 18)
)
_CtVVD_ObjectIdentity = ObjectIdentity
ctVVD = _CtVVD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 18, 1)
)
_CtVoiceOverIP_ObjectIdentity = ObjectIdentity
ctVoiceOverIP = _CtVoiceOverIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 18, 1, 1)
)
_CtCDP_ObjectIdentity = ObjectIdentity
ctCDP = _CtCDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19)
)
_CtSmartTrunkBranch_ObjectIdentity = ObjectIdentity
ctSmartTrunkBranch = _CtSmartTrunkBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20)
)
_CtronVpnMonMIB_ObjectIdentity = ObjectIdentity
ctronVpnMonMIB = _CtronVpnMonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 21)
)
_CtNetwork_ObjectIdentity = ObjectIdentity
ctNetwork = _CtNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3)
)
_NwDiagnostics_ObjectIdentity = ObjectIdentity
nwDiagnostics = _NwDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1)
)
_CtTranslation_ObjectIdentity = ObjectIdentity
ctTranslation = _CtTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4)
)
_CtIGMPBranch_ObjectIdentity = ObjectIdentity
ctIGMPBranch = _CtIGMPBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5)
)
_CtDirectory_ObjectIdentity = ObjectIdentity
ctDirectory = _CtDirectory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 6)
)
_CtAliasMib_ObjectIdentity = ObjectIdentity
ctAliasMib = _CtAliasMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7)
)
_CtApplication_ObjectIdentity = ObjectIdentity
ctApplication = _CtApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4)
)
_CtNetManagement_ObjectIdentity = ObjectIdentity
ctNetManagement = _CtNetManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 2)
)
_CtCATV_ObjectIdentity = ObjectIdentity
ctCATV = _CtCATV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 3)
)
_CtCM_ObjectIdentity = ObjectIdentity
ctCM = _CtCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 3, 1)
)
_CtHETS_ObjectIdentity = ObjectIdentity
ctHETS = _CtHETS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 3, 2)
)
_CtWebView_ObjectIdentity = ObjectIdentity
ctWebView = _CtWebView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4)
)
_CtSystem_ObjectIdentity = ObjectIdentity
ctSystem = _CtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5)
)
_CtPoMIB_ObjectIdentity = ObjectIdentity
ctPoMIB = _CtPoMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 1)
)
_CtErrLog_ObjectIdentity = ObjectIdentity
ctErrLog = _CtErrLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 2)
)
_CtBackplaneProto_ObjectIdentity = ObjectIdentity
ctBackplaneProto = _CtBackplaneProto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 3)
)
_CtUPowerSupply_ObjectIdentity = ObjectIdentity
ctUPowerSupply = _CtUPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4)
)
_CtFpRedundancy_ObjectIdentity = ObjectIdentity
ctFpRedundancy = _CtFpRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5)
)
_CtTrapTable_ObjectIdentity = ObjectIdentity
ctTrapTable = _CtTrapTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7)
)
_CtDownLoad_ObjectIdentity = ObjectIdentity
ctDownLoad = _CtDownLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8)
)
_CtPIC_ObjectIdentity = ObjectIdentity
ctPIC = _CtPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9)
)
_CtFlash_ObjectIdentity = ObjectIdentity
ctFlash = _CtFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10)
)
_CtLFAP_ObjectIdentity = ObjectIdentity
ctLFAP = _CtLFAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11)
)
_CtTxQArb_ObjectIdentity = ObjectIdentity
ctTxQArb = _CtTxQArb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12)
)
_CtDcm_ObjectIdentity = ObjectIdentity
ctDcm = _CtDcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 6)
)
_CtTrapLog_ObjectIdentity = ObjectIdentity
ctTrapLog = _CtTrapLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 44)
)
_CtronExp_ObjectIdentity = ObjectIdentity
ctronExp = _CtronExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2)
)
_CtronDLM_ObjectIdentity = ObjectIdentity
ctronDLM = _CtronDLM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 1)
)
_CtLicense_ObjectIdentity = ObjectIdentity
ctLicense = _CtLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 5)
)
_CtX25_ObjectIdentity = ObjectIdentity
ctX25 = _CtX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 6)
)
_CtFault_ObjectIdentity = ObjectIdentity
ctFault = _CtFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 7)
)
_CtGateway_ObjectIdentity = ObjectIdentity
ctGateway = _CtGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 8)
)
_CtronHost_ObjectIdentity = ObjectIdentity
ctronHost = _CtronHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 9)
)
_CtronRunTimeDiag_ObjectIdentity = ObjectIdentity
ctronRunTimeDiag = _CtronRunTimeDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 10)
)
_CtProfiler_ObjectIdentity = ObjectIdentity
ctProfiler = _CtProfiler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 11)
)
_CtVLANMib_ObjectIdentity = ObjectIdentity
ctVLANMib = _CtVLANMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12)
)
_CtDistMgt_ObjectIdentity = ObjectIdentity
ctDistMgt = _CtDistMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 14)
)
_CtRmonDebug_ObjectIdentity = ObjectIdentity
ctRmonDebug = _CtRmonDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 15)
)
_CtNetSim_ObjectIdentity = ObjectIdentity
ctNetSim = _CtNetSim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 17)
)
_CtMemory_ObjectIdentity = ObjectIdentity
ctMemory = _CtMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 22)
)
_CtEngTest_ObjectIdentity = ObjectIdentity
ctEngTest = _CtEngTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 23)
)
_FlowPolicyPolling_ObjectIdentity = ObjectIdentity
flowPolicyPolling = _FlowPolicyPolling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 24)
)
_CtDemandAccess_ObjectIdentity = ObjectIdentity
ctDemandAccess = _CtDemandAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 27)
)
_CtHWDebug_ObjectIdentity = ObjectIdentity
ctHWDebug = _CtHWDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 28)
)
_CtFWDebug_ObjectIdentity = ObjectIdentity
ctFWDebug = _CtFWDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29)
)
_CtEntityStateTC_ObjectIdentity = ObjectIdentity
ctEntityStateTC = _CtEntityStateTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 30)
)
_CtEntityStateMib_ObjectIdentity = ObjectIdentity
ctEntityStateMib = _CtEntityStateMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31)
)
_CtDhcpServerExpMib_ObjectIdentity = ObjectIdentity
ctDhcpServerExpMib = _CtDhcpServerExpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 32)
)
_CtFastPathProtectedPortMib_ObjectIdentity = ObjectIdentity
ctFastPathProtectedPortMib = _CtFastPathProtectedPortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 33)
)
_CtArpAclExpMib_ObjectIdentity = ObjectIdentity
ctArpAclExpMib = _CtArpAclExpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 34)
)
_CtDhcpSnoopingExpMib_ObjectIdentity = ObjectIdentity
ctDhcpSnoopingExpMib = _CtDhcpSnoopingExpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 35)
)
_CtDynamicArpInspectionExpMib_ObjectIdentity = ObjectIdentity
ctDynamicArpInspectionExpMib = _CtDynamicArpInspectionExpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36)
)
_CtronExtn_ObjectIdentity = ObjectIdentity
ctronExtn = _CtronExtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3)
)
_CtronChassis_ObjectIdentity = ObjectIdentity
ctronChassis = _CtronChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 1)
)
_CtronRmon_ObjectIdentity = ObjectIdentity
ctronRmon = _CtronRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 2)
)
_CtronMib2_ObjectIdentity = ObjectIdentity
ctronMib2 = _CtronMib2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3)
)
_CtActions_ObjectIdentity = ObjectIdentity
ctActions = _CtActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 4)
)
_CtAtmfLanEmulation_ObjectIdentity = ObjectIdentity
ctAtmfLanEmulation = _CtAtmfLanEmulation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5)
)
_CtLeClient_ObjectIdentity = ObjectIdentity
ctLeClient = _CtLeClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 1)
)
_CtElan_ObjectIdentity = ObjectIdentity
ctElan = _CtElan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2)
)
_CtLes_ObjectIdentity = ObjectIdentity
ctLes = _CtLes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 3)
)
_CtBus_ObjectIdentity = ObjectIdentity
ctBus = _CtBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4)
)
_CtMidManager_ObjectIdentity = ObjectIdentity
ctMidManager = _CtMidManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 4)
)
_CtGateWay_ObjectIdentity = ObjectIdentity
ctGateWay = _CtGateWay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 4, 1)
)
_CtronV2H_ObjectIdentity = ObjectIdentity
ctronV2H = _CtronV2H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12)
)
_V2h124_24MIB_ObjectIdentity = ObjectIdentity
v2h124_24MIB = _V2h124_24MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30)
)
_CtronAP3000_ObjectIdentity = ObjectIdentity
ctronAP3000 = _CtronAP3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13)
)
_CtronWslMIB_ObjectIdentity = ObjectIdentity
ctronWslMIB = _CtronWslMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 14)
)
_CtronTrapeze_ObjectIdentity = ObjectIdentity
ctronTrapeze = _CtronTrapeze_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15)
)
_CtronInternal_ObjectIdentity = ObjectIdentity
ctronInternal = _CtronInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 100)
)
_CtDefaults_ObjectIdentity = ObjectIdentity
ctDefaults = _CtDefaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 100, 1)
)
_CtEnet_ObjectIdentity = ObjectIdentity
ctEnet = _CtEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 100, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-MIB-NAMES",
    **{"mibs": mibs,
       "ctron": ctron,
       "ctPhysical": ctPhysical,
       "repeaterRev4": repeaterRev4,
       "chassis": chassis,
       "ctPhysRptrMim": ctPhysRptrMim,
       "ctPhysModule": ctPhysModule,
       "ctPModuleETWMIM": ctPModuleETWMIM,
       "ctDevice": ctDevice,
       "ctDot5PhysMgmt": ctDot5PhysMgmt,
       "ctps": ctps,
       "ctenv": ctenv,
       "ctChassis2": ctChassis2,
       "ctUPS": ctUPS,
       "ctTRStnAssign": ctTRStnAssign,
       "ctResource": ctResource,
       "ctIFRemap": ctIFRemap,
       "ctIFRemap2": ctIFRemap2,
       "ctOrpHSIM": ctOrpHSIM,
       "ctPortMap": ctPortMap,
       "ctHSIMPhysMib": ctHSIMPhysMib,
       "ctCMM": ctCMM,
       "ctDataLink": ctDataLink,
       "dot5": dot5,
       "ctsmtmib": ctsmtmib,
       "ctBridge": ctBridge,
       "ctEthernet": ctEthernet,
       "ctCSMACD": ctCSMACD,
       "ctEthernetCtlParameters": ctEthernetCtlParameters,
       "ctFDDI": ctFDDI,
       "ctFDDIFnb": ctFDDIFnb,
       "ctFDDIStats": ctFDDIStats,
       "ctTokenRing": ctTokenRing,
       "ctTokenRingFnb": ctTokenRingFnb,
       "ctronWan": ctronWan,
       "ctWan": ctWan,
       "ctRemoteAccess": ctRemoteAccess,
       "ctWanServices": ctWanServices,
       "ctDLSW": ctDLSW,
       "ctFastEthernet": ctFastEthernet,
       "ctATM": ctATM,
       "ctATMConfig": ctATMConfig,
       "ctSwitch": ctSwitch,
       "ctsfSwitch": ctsfSwitch,
       "ctSFCS": ctSFCS,
       "ctFPS": ctFPS,
       "ctINB": ctINB,
       "ctINBinfo": ctINBinfo,
       "ctINBinfo2": ctINBinfo2,
       "ctBroadcast": ctBroadcast,
       "ctPriorityExt": ctPriorityExt,
       "ctFPSServices": ctFPSServices,
       "ctVlanExt": ctVlanExt,
       "ctronVVD": ctronVVD,
       "ctVVD": ctVVD,
       "ctVoiceOverIP": ctVoiceOverIP,
       "ctCDP": ctCDP,
       "ctSmartTrunkBranch": ctSmartTrunkBranch,
       "ctronVpnMonMIB": ctronVpnMonMIB,
       "ctNetwork": ctNetwork,
       "nwDiagnostics": nwDiagnostics,
       "ctTranslation": ctTranslation,
       "ctIGMPBranch": ctIGMPBranch,
       "ctDirectory": ctDirectory,
       "ctAliasMib": ctAliasMib,
       "ctApplication": ctApplication,
       "ctNetManagement": ctNetManagement,
       "ctCATV": ctCATV,
       "ctCM": ctCM,
       "ctHETS": ctHETS,
       "ctWebView": ctWebView,
       "ctSystem": ctSystem,
       "ctPoMIB": ctPoMIB,
       "ctErrLog": ctErrLog,
       "ctBackplaneProto": ctBackplaneProto,
       "ctUPowerSupply": ctUPowerSupply,
       "ctFpRedundancy": ctFpRedundancy,
       "ctTrapTable": ctTrapTable,
       "ctDownLoad": ctDownLoad,
       "ctPIC": ctPIC,
       "ctFlash": ctFlash,
       "ctLFAP": ctLFAP,
       "ctTxQArb": ctTxQArb,
       "ctDcm": ctDcm,
       "ctTrapLog": ctTrapLog,
       "ctronExp": ctronExp,
       "ctronDLM": ctronDLM,
       "ctLicense": ctLicense,
       "ctX25": ctX25,
       "ctFault": ctFault,
       "ctGateway": ctGateway,
       "ctronHost": ctronHost,
       "ctronRunTimeDiag": ctronRunTimeDiag,
       "ctProfiler": ctProfiler,
       "ctVLANMib": ctVLANMib,
       "ctDistMgt": ctDistMgt,
       "ctRmonDebug": ctRmonDebug,
       "ctNetSim": ctNetSim,
       "ctMemory": ctMemory,
       "ctEngTest": ctEngTest,
       "flowPolicyPolling": flowPolicyPolling,
       "ctDemandAccess": ctDemandAccess,
       "ctHWDebug": ctHWDebug,
       "ctFWDebug": ctFWDebug,
       "ctEntityStateTC": ctEntityStateTC,
       "ctEntityStateMib": ctEntityStateMib,
       "ctDhcpServerExpMib": ctDhcpServerExpMib,
       "ctFastPathProtectedPortMib": ctFastPathProtectedPortMib,
       "ctArpAclExpMib": ctArpAclExpMib,
       "ctDhcpSnoopingExpMib": ctDhcpSnoopingExpMib,
       "ctDynamicArpInspectionExpMib": ctDynamicArpInspectionExpMib,
       "ctronExtn": ctronExtn,
       "ctronChassis": ctronChassis,
       "ctronRmon": ctronRmon,
       "ctronMib2": ctronMib2,
       "ctActions": ctActions,
       "ctAtmfLanEmulation": ctAtmfLanEmulation,
       "ctLeClient": ctLeClient,
       "ctElan": ctElan,
       "ctLes": ctLes,
       "ctBus": ctBus,
       "ctMidManager": ctMidManager,
       "ctGateWay": ctGateWay,
       "ctronV2H": ctronV2H,
       "v2h124-24MIB": v2h124_24MIB,
       "ctronAP3000": ctronAP3000,
       "ctronWslMIB": ctronWslMIB,
       "ctronTrapeze": ctronTrapeze,
       "ctronInternal": ctronInternal,
       "ctDefaults": ctDefaults,
       "ctEnet": ctEnet}
)
