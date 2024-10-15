# SNMP MIB module (CHIPDOT1D-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHIPDOT1D-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:46 2024
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

(DisplayString,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "DisplayString")

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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Chipcom_ObjectIdentity = ObjectIdentity
chipcom = _Chipcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49)
)
_Chipmib02_ObjectIdentity = ObjectIdentity
chipmib02 = _Chipmib02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2)
)
_ChipGen_ObjectIdentity = ObjectIdentity
chipGen = _ChipGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 1)
)
_ChipEcho_ObjectIdentity = ObjectIdentity
chipEcho = _ChipEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 2)
)
_ChipProducts_ObjectIdentity = ObjectIdentity
chipProducts = _ChipProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3)
)
_Online_ObjectIdentity = ObjectIdentity
online = _Online_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1)
)
_OlAgents_ObjectIdentity = ObjectIdentity
olAgents = _OlAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1)
)
_OlConc_ObjectIdentity = ObjectIdentity
olConc = _OlConc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2)
)
_OlEnv_ObjectIdentity = ObjectIdentity
olEnv = _OlEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3)
)
_OlModules_ObjectIdentity = ObjectIdentity
olModules = _OlModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4)
)
_OlSpecMods_ObjectIdentity = ObjectIdentity
olSpecMods = _OlSpecMods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4)
)
_Ol50nnMCTL_ObjectIdentity = ObjectIdentity
ol50nnMCTL = _Ol50nnMCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3)
)
_Ol51nnMMGT_ObjectIdentity = ObjectIdentity
ol51nnMMGT = _Ol51nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4)
)
_Ol51nnMFIB_ObjectIdentity = ObjectIdentity
ol51nnMFIB = _Ol51nnMFIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5)
)
_Ol51nnMUTP_ObjectIdentity = ObjectIdentity
ol51nnMUTP = _Ol51nnMUTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6)
)
_Ol51nnMTP_ObjectIdentity = ObjectIdentity
ol51nnMTP = _Ol51nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7)
)
_Ol51nnMBNC_ObjectIdentity = ObjectIdentity
ol51nnMBNC = _Ol51nnMBNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8)
)
_Ol51nnBEE_ObjectIdentity = ObjectIdentity
ol51nnBEE = _Ol51nnBEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9)
)
_Ol51nnRES_ObjectIdentity = ObjectIdentity
ol51nnRES = _Ol51nnRES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10)
)
_Ol51nnREE_ObjectIdentity = ObjectIdentity
ol51nnREE = _Ol51nnREE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11)
)
_Ol51nnMAUIF_ObjectIdentity = ObjectIdentity
ol51nnMAUIF = _Ol51nnMAUIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12)
)
_Ol51nnMAUIM_ObjectIdentity = ObjectIdentity
ol51nnMAUIM = _Ol51nnMAUIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13)
)
_Ol5208MTP_ObjectIdentity = ObjectIdentity
ol5208MTP = _Ol5208MTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14)
)
_Ol51nnMFP_ObjectIdentity = ObjectIdentity
ol51nnMFP = _Ol51nnMFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15)
)
_Ol51nnMFBP_ObjectIdentity = ObjectIdentity
ol51nnMFBP = _Ol51nnMFBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16)
)
_Ol51nnMTPL_ObjectIdentity = ObjectIdentity
ol51nnMTPL = _Ol51nnMTPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17)
)
_Ol51nnMTPPL_ObjectIdentity = ObjectIdentity
ol51nnMTPPL = _Ol51nnMTPPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18)
)
_Ol52nnMTP_ObjectIdentity = ObjectIdentity
ol52nnMTP = _Ol52nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19)
)
_Ol52nnMFR_ObjectIdentity = ObjectIdentity
ol52nnMFR = _Ol52nnMFR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20)
)
_Ol51nnMTS_ObjectIdentity = ObjectIdentity
ol51nnMTS = _Ol51nnMTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21)
)
_Ol51nnMFL_ObjectIdentity = ObjectIdentity
ol51nnMFL = _Ol51nnMFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22)
)
_Ol50nnMRCTL_ObjectIdentity = ObjectIdentity
ol50nnMRCTL = _Ol50nnMRCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23)
)
_Ol51nnMFB_ObjectIdentity = ObjectIdentity
ol51nnMFB = _Ol51nnMFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24)
)
_Ol53nnMMGT_ObjectIdentity = ObjectIdentity
ol53nnMMGT = _Ol53nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25)
)
_Ol53nnMFBMIC_ObjectIdentity = ObjectIdentity
ol53nnMFBMIC = _Ol53nnMFBMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26)
)
_Ol53nnMFIBST_ObjectIdentity = ObjectIdentity
ol53nnMFIBST = _Ol53nnMFIBST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27)
)
_Ol53nnMSTP_ObjectIdentity = ObjectIdentity
ol53nnMSTP = _Ol53nnMSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28)
)
_Ol51nnMTPCL_ObjectIdentity = ObjectIdentity
ol51nnMTPCL = _Ol51nnMTPCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29)
)
_Ol52nnBTT_ObjectIdentity = ObjectIdentity
ol52nnBTT = _Ol52nnBTT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30)
)
_Ol51nnIx_ObjectIdentity = ObjectIdentity
ol51nnIx = _Ol51nnIx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31)
)
_Ol52nnMMGT_ObjectIdentity = ObjectIdentity
ol52nnMMGT = _Ol52nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32)
)
_Ol50nnMHCTL_ObjectIdentity = ObjectIdentity
ol50nnMHCTL = _Ol50nnMHCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33)
)
_OlNets_ObjectIdentity = ObjectIdentity
olNets = _OlNets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5)
)
_OlNet_ObjectIdentity = ObjectIdentity
olNet = _OlNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1)
)
_OlEnet_ObjectIdentity = ObjectIdentity
olEnet = _OlEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2)
)
_OlTRnet_ObjectIdentity = ObjectIdentity
olTRnet = _OlTRnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3)
)
_OlFDDInet_ObjectIdentity = ObjectIdentity
olFDDInet = _OlFDDInet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4)
)
_OlGroups_ObjectIdentity = ObjectIdentity
olGroups = _OlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6)
)
_OlAlarm_ObjectIdentity = ObjectIdentity
olAlarm = _OlAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7)
)
_OlThresh_ObjectIdentity = ObjectIdentity
olThresh = _OlThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1)
)
_OlThreshControl_ObjectIdentity = ObjectIdentity
olThreshControl = _OlThreshControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1)
)
_Oebm_ObjectIdentity = ObjectIdentity
oebm = _Oebm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 2)
)
_Midnight_ObjectIdentity = ObjectIdentity
midnight = _Midnight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 3)
)
_WorkGroupHub_ObjectIdentity = ObjectIdentity
workGroupHub = _WorkGroupHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4)
)
_HubSysGroup_ObjectIdentity = ObjectIdentity
hubSysGroup = _HubSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 1)
)
_HardwareGroup_ObjectIdentity = ObjectIdentity
hardwareGroup = _HardwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 2)
)
_SoftwareGroup_ObjectIdentity = ObjectIdentity
softwareGroup = _SoftwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 3)
)
_HubGroup_ObjectIdentity = ObjectIdentity
hubGroup = _HubGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 4)
)
_BoardGroup_ObjectIdentity = ObjectIdentity
boardGroup = _BoardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 5)
)
_PortGroup_ObjectIdentity = ObjectIdentity
portGroup = _PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 6)
)
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 7)
)
_Emm_ObjectIdentity = ObjectIdentity
emm = _Emm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 5)
)
_ChipBridge_ObjectIdentity = ObjectIdentity
chipBridge = _ChipBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 6)
)


class _ChipBridgeSideSwitchMode_Type(Integer32):
    """Custom type chipBridgeSideSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ChipBridgeSideSwitchMode_Type.__name__ = "Integer32"
_ChipBridgeSideSwitchMode_Object = MibScalar
chipBridgeSideSwitchMode = _ChipBridgeSideSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 6, 1),
    _ChipBridgeSideSwitchMode_Type()
)
chipBridgeSideSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipBridgeSideSwitchMode.setStatus("mandatory")
_Trmm_ObjectIdentity = ObjectIdentity
trmm = _Trmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 7)
)
_Fmm_ObjectIdentity = ObjectIdentity
fmm = _Fmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 8)
)
_Focus1_ObjectIdentity = ObjectIdentity
focus1 = _Focus1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 9)
)
_Oeim_ObjectIdentity = ObjectIdentity
oeim = _Oeim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 10)
)
_ChipExperiment_ObjectIdentity = ObjectIdentity
chipExperiment = _ChipExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4)
)
_ChipExpTokenRing_ObjectIdentity = ObjectIdentity
chipExpTokenRing = _ChipExpTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1)
)
_Dot5_ObjectIdentity = ObjectIdentity
dot5 = _Dot5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1)
)
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14)
)
_Dot1dBase_ObjectIdentity = ObjectIdentity
dot1dBase = _Dot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 1)
)
_Dot1dBaseBridgeAddress_Type = MacAddress
_Dot1dBaseBridgeAddress_Object = MibScalar
dot1dBaseBridgeAddress = _Dot1dBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 1, 1),
    _Dot1dBaseBridgeAddress_Type()
)
dot1dBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseBridgeAddress.setStatus("mandatory")
_Dot1dBaseNumPorts_Type = Integer32
_Dot1dBaseNumPorts_Object = MibScalar
dot1dBaseNumPorts = _Dot1dBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 1, 2),
    _Dot1dBaseNumPorts_Type()
)
dot1dBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseNumPorts.setStatus("mandatory")


class _Dot1dBaseType_Type(Integer32):
    """Custom type dot1dBaseType based on Integer32"""
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
        *(("sourceroute-only", 3),
          ("srt", 4),
          ("transparent-only", 2),
          ("unknown", 1))
    )


_Dot1dBaseType_Type.__name__ = "Integer32"
_Dot1dBaseType_Object = MibScalar
dot1dBaseType = _Dot1dBaseType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 1, 3),
    _Dot1dBaseType_Type()
)
dot1dBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseType.setStatus("mandatory")
_Dot1dBasePortTable_Object = MibTable
dot1dBasePortTable = _Dot1dBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 1, 4)
)
if mibBuilder.loadTexts:
    dot1dBasePortTable.setStatus("mandatory")
_Dot1dBasePortEntry_Object = MibTableRow
dot1dBasePortEntry = _Dot1dBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 1, 4, 1)
)
dot1dBasePortEntry.setIndexNames(
    (0, "CHIPDOT1D-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dot1dBasePortEntry.setStatus("mandatory")
_Dot1dBasePort_Type = Integer32
_Dot1dBasePort_Object = MibTableColumn
dot1dBasePort = _Dot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 1, 4, 1, 1),
    _Dot1dBasePort_Type()
)
dot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePort.setStatus("mandatory")
_Dot1dBasePortIfIndex_Type = Integer32
_Dot1dBasePortIfIndex_Object = MibTableColumn
dot1dBasePortIfIndex = _Dot1dBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 1, 4, 1, 2),
    _Dot1dBasePortIfIndex_Type()
)
dot1dBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortIfIndex.setStatus("mandatory")
_Dot1dBasePortCircuit_Type = ObjectIdentifier
_Dot1dBasePortCircuit_Object = MibTableColumn
dot1dBasePortCircuit = _Dot1dBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 1, 4, 1, 3),
    _Dot1dBasePortCircuit_Type()
)
dot1dBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortCircuit.setStatus("mandatory")
_Dot1dBasePortDelayExceededDiscards_Type = Counter32
_Dot1dBasePortDelayExceededDiscards_Object = MibTableColumn
dot1dBasePortDelayExceededDiscards = _Dot1dBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 1, 4, 1, 4),
    _Dot1dBasePortDelayExceededDiscards_Type()
)
dot1dBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortDelayExceededDiscards.setStatus("mandatory")
_Dot1dBasePortMtuExceededDiscards_Type = Counter32
_Dot1dBasePortMtuExceededDiscards_Object = MibTableColumn
dot1dBasePortMtuExceededDiscards = _Dot1dBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 1, 4, 1, 5),
    _Dot1dBasePortMtuExceededDiscards_Type()
)
dot1dBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortMtuExceededDiscards.setStatus("mandatory")
_Dot1dStp_ObjectIdentity = ObjectIdentity
dot1dStp = _Dot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2)
)


class _Dot1dStpProtocolSpecification_Type(Integer32):
    """Custom type dot1dStpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_Dot1dStpProtocolSpecification_Type.__name__ = "Integer32"
_Dot1dStpProtocolSpecification_Object = MibScalar
dot1dStpProtocolSpecification = _Dot1dStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 1),
    _Dot1dStpProtocolSpecification_Type()
)
dot1dStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpProtocolSpecification.setStatus("mandatory")


class _Dot1dStpPriority_Type(Integer32):
    """Custom type dot1dStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1dStpPriority_Type.__name__ = "Integer32"
_Dot1dStpPriority_Object = MibScalar
dot1dStpPriority = _Dot1dStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 2),
    _Dot1dStpPriority_Type()
)
dot1dStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPriority.setStatus("mandatory")
_Dot1dStpTimeSinceTopologyChange_Type = TimeTicks
_Dot1dStpTimeSinceTopologyChange_Object = MibScalar
dot1dStpTimeSinceTopologyChange = _Dot1dStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 3),
    _Dot1dStpTimeSinceTopologyChange_Type()
)
dot1dStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpTimeSinceTopologyChange.setStatus("mandatory")
_Dot1dStpTopChanges_Type = Counter32
_Dot1dStpTopChanges_Object = MibScalar
dot1dStpTopChanges = _Dot1dStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 4),
    _Dot1dStpTopChanges_Type()
)
dot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpTopChanges.setStatus("mandatory")
_Dot1dStpDesignatedRoot_Type = BridgeId
_Dot1dStpDesignatedRoot_Object = MibScalar
dot1dStpDesignatedRoot = _Dot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 5),
    _Dot1dStpDesignatedRoot_Type()
)
dot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpDesignatedRoot.setStatus("mandatory")
_Dot1dStpRootCost_Type = Integer32
_Dot1dStpRootCost_Object = MibScalar
dot1dStpRootCost = _Dot1dStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 6),
    _Dot1dStpRootCost_Type()
)
dot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpRootCost.setStatus("mandatory")
_Dot1dStpRootPort_Type = Integer32
_Dot1dStpRootPort_Object = MibScalar
dot1dStpRootPort = _Dot1dStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 7),
    _Dot1dStpRootPort_Type()
)
dot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpRootPort.setStatus("mandatory")
_Dot1dStpMaxAge_Type = Timeout
_Dot1dStpMaxAge_Object = MibScalar
dot1dStpMaxAge = _Dot1dStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 8),
    _Dot1dStpMaxAge_Type()
)
dot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpMaxAge.setStatus("mandatory")
_Dot1dStpHelloTime_Type = Timeout
_Dot1dStpHelloTime_Object = MibScalar
dot1dStpHelloTime = _Dot1dStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 9),
    _Dot1dStpHelloTime_Type()
)
dot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpHelloTime.setStatus("mandatory")
_Dot1dStpHoldTime_Type = Integer32
_Dot1dStpHoldTime_Object = MibScalar
dot1dStpHoldTime = _Dot1dStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 10),
    _Dot1dStpHoldTime_Type()
)
dot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpHoldTime.setStatus("mandatory")
_Dot1dStpForwardDelay_Type = Timeout
_Dot1dStpForwardDelay_Object = MibScalar
dot1dStpForwardDelay = _Dot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 11),
    _Dot1dStpForwardDelay_Type()
)
dot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpForwardDelay.setStatus("mandatory")
_Dot1dStpBridgeMaxAge_Type = Timeout
_Dot1dStpBridgeMaxAge_Object = MibScalar
dot1dStpBridgeMaxAge = _Dot1dStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 12),
    _Dot1dStpBridgeMaxAge_Type()
)
dot1dStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeMaxAge.setStatus("mandatory")
_Dot1dStpBridgeHelloTime_Type = Timeout
_Dot1dStpBridgeHelloTime_Object = MibScalar
dot1dStpBridgeHelloTime = _Dot1dStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 13),
    _Dot1dStpBridgeHelloTime_Type()
)
dot1dStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeHelloTime.setStatus("mandatory")
_Dot1dStpBridgeForwardDelay_Type = Timeout
_Dot1dStpBridgeForwardDelay_Object = MibScalar
dot1dStpBridgeForwardDelay = _Dot1dStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 14),
    _Dot1dStpBridgeForwardDelay_Type()
)
dot1dStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpBridgeForwardDelay.setStatus("mandatory")
_Dot1dStpPortTable_Object = MibTable
dot1dStpPortTable = _Dot1dStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15)
)
if mibBuilder.loadTexts:
    dot1dStpPortTable.setStatus("mandatory")
_Dot1dStpPortEntry_Object = MibTableRow
dot1dStpPortEntry = _Dot1dStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15, 1)
)
dot1dStpPortEntry.setIndexNames(
    (0, "CHIPDOT1D-MIB", "dot1dStpPort"),
)
if mibBuilder.loadTexts:
    dot1dStpPortEntry.setStatus("mandatory")
_Dot1dStpPort_Type = Integer32
_Dot1dStpPort_Object = MibTableColumn
dot1dStpPort = _Dot1dStpPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15, 1, 1),
    _Dot1dStpPort_Type()
)
dot1dStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPort.setStatus("mandatory")
_Dot1dStpPortPriority_Type = Integer32
_Dot1dStpPortPriority_Object = MibTableColumn
dot1dStpPortPriority = _Dot1dStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15, 1, 2),
    _Dot1dStpPortPriority_Type()
)
dot1dStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortPriority.setStatus("mandatory")


class _Dot1dStpPortState_Type(Integer32):
    """Custom type dot1dStpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_Dot1dStpPortState_Type.__name__ = "Integer32"
_Dot1dStpPortState_Object = MibTableColumn
dot1dStpPortState = _Dot1dStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15, 1, 3),
    _Dot1dStpPortState_Type()
)
dot1dStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortState.setStatus("mandatory")


class _Dot1dStpPortEnable_Type(Integer32):
    """Custom type dot1dStpPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Dot1dStpPortEnable_Type.__name__ = "Integer32"
_Dot1dStpPortEnable_Object = MibTableColumn
dot1dStpPortEnable = _Dot1dStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15, 1, 4),
    _Dot1dStpPortEnable_Type()
)
dot1dStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortEnable.setStatus("mandatory")
_Dot1dStpPortPathCost_Type = Integer32
_Dot1dStpPortPathCost_Object = MibTableColumn
dot1dStpPortPathCost = _Dot1dStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15, 1, 5),
    _Dot1dStpPortPathCost_Type()
)
dot1dStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortPathCost.setStatus("mandatory")
_Dot1dStpPortDesignatedRoot_Type = BridgeId
_Dot1dStpPortDesignatedRoot_Object = MibTableColumn
dot1dStpPortDesignatedRoot = _Dot1dStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15, 1, 6),
    _Dot1dStpPortDesignatedRoot_Type()
)
dot1dStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedRoot.setStatus("mandatory")
_Dot1dStpPortDesignatedCost_Type = Integer32
_Dot1dStpPortDesignatedCost_Object = MibTableColumn
dot1dStpPortDesignatedCost = _Dot1dStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15, 1, 7),
    _Dot1dStpPortDesignatedCost_Type()
)
dot1dStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedCost.setStatus("mandatory")
_Dot1dStpPortDesignatedBridge_Type = BridgeId
_Dot1dStpPortDesignatedBridge_Object = MibTableColumn
dot1dStpPortDesignatedBridge = _Dot1dStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15, 1, 8),
    _Dot1dStpPortDesignatedBridge_Type()
)
dot1dStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedBridge.setStatus("mandatory")


class _Dot1dStpPortDesignatedPort_Type(OctetString):
    """Custom type dot1dStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Dot1dStpPortDesignatedPort_Type.__name__ = "OctetString"
_Dot1dStpPortDesignatedPort_Object = MibTableColumn
dot1dStpPortDesignatedPort = _Dot1dStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15, 1, 9),
    _Dot1dStpPortDesignatedPort_Type()
)
dot1dStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedPort.setStatus("mandatory")
_Dot1dStpPortForwardTransitions_Type = Counter32
_Dot1dStpPortForwardTransitions_Object = MibTableColumn
dot1dStpPortForwardTransitions = _Dot1dStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 2, 15, 1, 10),
    _Dot1dStpPortForwardTransitions_Type()
)
dot1dStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortForwardTransitions.setStatus("mandatory")
_Dot1dTp_ObjectIdentity = ObjectIdentity
dot1dTp = _Dot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 4)
)
_Dot1dTpLearnedEntryDiscards_Type = Counter32
_Dot1dTpLearnedEntryDiscards_Object = MibScalar
dot1dTpLearnedEntryDiscards = _Dot1dTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 4, 1),
    _Dot1dTpLearnedEntryDiscards_Type()
)
dot1dTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpLearnedEntryDiscards.setStatus("mandatory")
_Dot1dTpAgingTime_Type = Integer32
_Dot1dTpAgingTime_Object = MibScalar
dot1dTpAgingTime = _Dot1dTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 4, 2),
    _Dot1dTpAgingTime_Type()
)
dot1dTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dTpAgingTime.setStatus("mandatory")
_Dot1dTpPortTable_Object = MibTable
dot1dTpPortTable = _Dot1dTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 4, 4)
)
if mibBuilder.loadTexts:
    dot1dTpPortTable.setStatus("mandatory")
_Dot1dTpPortEntry_Object = MibTableRow
dot1dTpPortEntry = _Dot1dTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 4, 4, 1)
)
dot1dTpPortEntry.setIndexNames(
    (0, "CHIPDOT1D-MIB", "dot1dTpPort"),
)
if mibBuilder.loadTexts:
    dot1dTpPortEntry.setStatus("mandatory")
_Dot1dTpPort_Type = Integer32
_Dot1dTpPort_Object = MibTableColumn
dot1dTpPort = _Dot1dTpPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 4, 4, 1, 1),
    _Dot1dTpPort_Type()
)
dot1dTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPort.setStatus("mandatory")
_Dot1dTpPortMaxInfo_Type = Integer32
_Dot1dTpPortMaxInfo_Object = MibTableColumn
dot1dTpPortMaxInfo = _Dot1dTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 4, 4, 1, 2),
    _Dot1dTpPortMaxInfo_Type()
)
dot1dTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortMaxInfo.setStatus("mandatory")
_Dot1dTpPortInFrames_Type = Counter32
_Dot1dTpPortInFrames_Object = MibTableColumn
dot1dTpPortInFrames = _Dot1dTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 4, 4, 1, 3),
    _Dot1dTpPortInFrames_Type()
)
dot1dTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInFrames.setStatus("mandatory")
_Dot1dTpPortOutFrames_Type = Counter32
_Dot1dTpPortOutFrames_Object = MibTableColumn
dot1dTpPortOutFrames = _Dot1dTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 4, 4, 1, 4),
    _Dot1dTpPortOutFrames_Type()
)
dot1dTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortOutFrames.setStatus("mandatory")
_Dot1dTpPortInDiscards_Type = Counter32
_Dot1dTpPortInDiscards_Object = MibTableColumn
dot1dTpPortInDiscards = _Dot1dTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 4, 4, 1, 5),
    _Dot1dTpPortInDiscards_Type()
)
dot1dTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInDiscards.setStatus("mandatory")
_Dot1dStatic_ObjectIdentity = ObjectIdentity
dot1dStatic = _Dot1dStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 5)
)
_ChipTTY_ObjectIdentity = ObjectIdentity
chipTTY = _ChipTTY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 5)
)
_ChipTFTP_ObjectIdentity = ObjectIdentity
chipTFTP = _ChipTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 6)
)
_ChipDownload_ObjectIdentity = ObjectIdentity
chipDownload = _ChipDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 7)
)

# Managed Objects groups


# Notification objects

newRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 0, 1)
)
if mibBuilder.loadTexts:
    newRoot.setStatus(
        ""
    )

topologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14, 0, 2)
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHIPDOT1D-MIB",
    **{"MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "chipcom": chipcom,
       "chipmib02": chipmib02,
       "chipGen": chipGen,
       "chipEcho": chipEcho,
       "chipProducts": chipProducts,
       "online": online,
       "olAgents": olAgents,
       "olConc": olConc,
       "olEnv": olEnv,
       "olModules": olModules,
       "olSpecMods": olSpecMods,
       "ol50nnMCTL": ol50nnMCTL,
       "ol51nnMMGT": ol51nnMMGT,
       "ol51nnMFIB": ol51nnMFIB,
       "ol51nnMUTP": ol51nnMUTP,
       "ol51nnMTP": ol51nnMTP,
       "ol51nnMBNC": ol51nnMBNC,
       "ol51nnBEE": ol51nnBEE,
       "ol51nnRES": ol51nnRES,
       "ol51nnREE": ol51nnREE,
       "ol51nnMAUIF": ol51nnMAUIF,
       "ol51nnMAUIM": ol51nnMAUIM,
       "ol5208MTP": ol5208MTP,
       "ol51nnMFP": ol51nnMFP,
       "ol51nnMFBP": ol51nnMFBP,
       "ol51nnMTPL": ol51nnMTPL,
       "ol51nnMTPPL": ol51nnMTPPL,
       "ol52nnMTP": ol52nnMTP,
       "ol52nnMFR": ol52nnMFR,
       "ol51nnMTS": ol51nnMTS,
       "ol51nnMFL": ol51nnMFL,
       "ol50nnMRCTL": ol50nnMRCTL,
       "ol51nnMFB": ol51nnMFB,
       "ol53nnMMGT": ol53nnMMGT,
       "ol53nnMFBMIC": ol53nnMFBMIC,
       "ol53nnMFIBST": ol53nnMFIBST,
       "ol53nnMSTP": ol53nnMSTP,
       "ol51nnMTPCL": ol51nnMTPCL,
       "ol52nnBTT": ol52nnBTT,
       "ol51nnIx": ol51nnIx,
       "ol52nnMMGT": ol52nnMMGT,
       "ol50nnMHCTL": ol50nnMHCTL,
       "olNets": olNets,
       "olNet": olNet,
       "olEnet": olEnet,
       "olTRnet": olTRnet,
       "olFDDInet": olFDDInet,
       "olGroups": olGroups,
       "olAlarm": olAlarm,
       "olThresh": olThresh,
       "olThreshControl": olThreshControl,
       "oebm": oebm,
       "midnight": midnight,
       "workGroupHub": workGroupHub,
       "hubSysGroup": hubSysGroup,
       "hardwareGroup": hardwareGroup,
       "softwareGroup": softwareGroup,
       "hubGroup": hubGroup,
       "boardGroup": boardGroup,
       "portGroup": portGroup,
       "alarmGroup": alarmGroup,
       "emm": emm,
       "chipBridge": chipBridge,
       "chipBridgeSideSwitchMode": chipBridgeSideSwitchMode,
       "trmm": trmm,
       "fmm": fmm,
       "focus1": focus1,
       "oeim": oeim,
       "chipExperiment": chipExperiment,
       "chipExpTokenRing": chipExpTokenRing,
       "dot5": dot5,
       "dot1dBridge": dot1dBridge,
       "newRoot": newRoot,
       "topologyChange": topologyChange,
       "dot1dBase": dot1dBase,
       "dot1dBaseBridgeAddress": dot1dBaseBridgeAddress,
       "dot1dBaseNumPorts": dot1dBaseNumPorts,
       "dot1dBaseType": dot1dBaseType,
       "dot1dBasePortTable": dot1dBasePortTable,
       "dot1dBasePortEntry": dot1dBasePortEntry,
       "dot1dBasePort": dot1dBasePort,
       "dot1dBasePortIfIndex": dot1dBasePortIfIndex,
       "dot1dBasePortCircuit": dot1dBasePortCircuit,
       "dot1dBasePortDelayExceededDiscards": dot1dBasePortDelayExceededDiscards,
       "dot1dBasePortMtuExceededDiscards": dot1dBasePortMtuExceededDiscards,
       "dot1dStp": dot1dStp,
       "dot1dStpProtocolSpecification": dot1dStpProtocolSpecification,
       "dot1dStpPriority": dot1dStpPriority,
       "dot1dStpTimeSinceTopologyChange": dot1dStpTimeSinceTopologyChange,
       "dot1dStpTopChanges": dot1dStpTopChanges,
       "dot1dStpDesignatedRoot": dot1dStpDesignatedRoot,
       "dot1dStpRootCost": dot1dStpRootCost,
       "dot1dStpRootPort": dot1dStpRootPort,
       "dot1dStpMaxAge": dot1dStpMaxAge,
       "dot1dStpHelloTime": dot1dStpHelloTime,
       "dot1dStpHoldTime": dot1dStpHoldTime,
       "dot1dStpForwardDelay": dot1dStpForwardDelay,
       "dot1dStpBridgeMaxAge": dot1dStpBridgeMaxAge,
       "dot1dStpBridgeHelloTime": dot1dStpBridgeHelloTime,
       "dot1dStpBridgeForwardDelay": dot1dStpBridgeForwardDelay,
       "dot1dStpPortTable": dot1dStpPortTable,
       "dot1dStpPortEntry": dot1dStpPortEntry,
       "dot1dStpPort": dot1dStpPort,
       "dot1dStpPortPriority": dot1dStpPortPriority,
       "dot1dStpPortState": dot1dStpPortState,
       "dot1dStpPortEnable": dot1dStpPortEnable,
       "dot1dStpPortPathCost": dot1dStpPortPathCost,
       "dot1dStpPortDesignatedRoot": dot1dStpPortDesignatedRoot,
       "dot1dStpPortDesignatedCost": dot1dStpPortDesignatedCost,
       "dot1dStpPortDesignatedBridge": dot1dStpPortDesignatedBridge,
       "dot1dStpPortDesignatedPort": dot1dStpPortDesignatedPort,
       "dot1dStpPortForwardTransitions": dot1dStpPortForwardTransitions,
       "dot1dTp": dot1dTp,
       "dot1dTpLearnedEntryDiscards": dot1dTpLearnedEntryDiscards,
       "dot1dTpAgingTime": dot1dTpAgingTime,
       "dot1dTpPortTable": dot1dTpPortTable,
       "dot1dTpPortEntry": dot1dTpPortEntry,
       "dot1dTpPort": dot1dTpPort,
       "dot1dTpPortMaxInfo": dot1dTpPortMaxInfo,
       "dot1dTpPortInFrames": dot1dTpPortInFrames,
       "dot1dTpPortOutFrames": dot1dTpPortOutFrames,
       "dot1dTpPortInDiscards": dot1dTpPortInDiscards,
       "dot1dStatic": dot1dStatic,
       "chipTTY": chipTTY,
       "chipTFTP": chipTFTP,
       "chipDownload": chipDownload}
)
