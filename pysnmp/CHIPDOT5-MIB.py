# SNMP MIB module (CHIPDOT5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHIPDOT5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:47 2024
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
_Dot5Table_Object = MibTable
dot5Table = _Dot5Table_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot5Table.setStatus("mandatory")
_Dot5Entry_Object = MibTableRow
dot5Entry = _Dot5Entry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1)
)
dot5Entry.setIndexNames(
    (0, "CHIPDOT5-MIB", "dot5IfIndex"),
)
if mibBuilder.loadTexts:
    dot5Entry.setStatus("mandatory")
_Dot5IfIndex_Type = Integer32
_Dot5IfIndex_Object = MibTableColumn
dot5IfIndex = _Dot5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 1),
    _Dot5IfIndex_Type()
)
dot5IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5IfIndex.setStatus("mandatory")


class _Dot5Commands_Type(Integer32):
    """Custom type dot5Commands based on Integer32"""
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
        *(("close", 4),
          ("no-op", 1),
          ("open", 2),
          ("reset", 3))
    )


_Dot5Commands_Type.__name__ = "Integer32"
_Dot5Commands_Object = MibTableColumn
dot5Commands = _Dot5Commands_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 2),
    _Dot5Commands_Type()
)
dot5Commands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5Commands.setStatus("mandatory")
_Dot5RingStatus_Type = Integer32
_Dot5RingStatus_Object = MibTableColumn
dot5RingStatus = _Dot5RingStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 3),
    _Dot5RingStatus_Type()
)
dot5RingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5RingStatus.setStatus("mandatory")


class _Dot5RingState_Type(Integer32):
    """Custom type dot5RingState based on Integer32"""
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
        *(("closed", 2),
          ("closing", 4),
          ("openFailure", 5),
          ("opened", 1),
          ("opening", 3),
          ("ringFailure", 6))
    )


_Dot5RingState_Type.__name__ = "Integer32"
_Dot5RingState_Object = MibTableColumn
dot5RingState = _Dot5RingState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 4),
    _Dot5RingState_Type()
)
dot5RingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5RingState.setStatus("mandatory")


class _Dot5RingOpenStatus_Type(Integer32):
    """Custom type dot5RingOpenStatus based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("badParam", 2),
          ("beaconing", 7),
          ("duplicateMAC", 8),
          ("insertionTimeout", 5),
          ("lobeFailed", 3),
          ("noOpen", 1),
          ("open", 11),
          ("removeReceived", 10),
          ("requestFailed", 9),
          ("ringFailed", 6),
          ("signalLoss", 4))
    )


_Dot5RingOpenStatus_Type.__name__ = "Integer32"
_Dot5RingOpenStatus_Object = MibTableColumn
dot5RingOpenStatus = _Dot5RingOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 5),
    _Dot5RingOpenStatus_Type()
)
dot5RingOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5RingOpenStatus.setStatus("mandatory")


class _Dot5RingSpeed_Type(Integer32):
    """Custom type dot5RingSpeed based on Integer32"""
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
        *(("fourMegabit", 3),
          ("oneMegabit", 2),
          ("sixteenMegabit", 4),
          ("unknown", 1))
    )


_Dot5RingSpeed_Type.__name__ = "Integer32"
_Dot5RingSpeed_Object = MibTableColumn
dot5RingSpeed = _Dot5RingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 6),
    _Dot5RingSpeed_Type()
)
dot5RingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5RingSpeed.setStatus("mandatory")
_Dot5UpStream_Type = MacAddress
_Dot5UpStream_Object = MibTableColumn
dot5UpStream = _Dot5UpStream_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 7),
    _Dot5UpStream_Type()
)
dot5UpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5UpStream.setStatus("mandatory")


class _Dot5ActMonParticipate_Type(Integer32):
    """Custom type dot5ActMonParticipate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Dot5ActMonParticipate_Type.__name__ = "Integer32"
_Dot5ActMonParticipate_Object = MibTableColumn
dot5ActMonParticipate = _Dot5ActMonParticipate_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 8),
    _Dot5ActMonParticipate_Type()
)
dot5ActMonParticipate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5ActMonParticipate.setStatus("mandatory")
_Dot5Functional_Type = MacAddress
_Dot5Functional_Object = MibTableColumn
dot5Functional = _Dot5Functional_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 1, 1, 9),
    _Dot5Functional_Type()
)
dot5Functional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5Functional.setStatus("mandatory")
_Dot5StatsTable_Object = MibTable
dot5StatsTable = _Dot5StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot5StatsTable.setStatus("mandatory")
_Dot5StatsEntry_Object = MibTableRow
dot5StatsEntry = _Dot5StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1)
)
dot5StatsEntry.setIndexNames(
    (0, "CHIPDOT5-MIB", "dot5StatsIfIndex"),
)
if mibBuilder.loadTexts:
    dot5StatsEntry.setStatus("mandatory")
_Dot5StatsIfIndex_Type = Integer32
_Dot5StatsIfIndex_Object = MibTableColumn
dot5StatsIfIndex = _Dot5StatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 1),
    _Dot5StatsIfIndex_Type()
)
dot5StatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsIfIndex.setStatus("mandatory")
_Dot5StatsLineErrors_Type = Counter32
_Dot5StatsLineErrors_Object = MibTableColumn
dot5StatsLineErrors = _Dot5StatsLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 2),
    _Dot5StatsLineErrors_Type()
)
dot5StatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsLineErrors.setStatus("mandatory")
_Dot5StatsBurstErrors_Type = Counter32
_Dot5StatsBurstErrors_Object = MibTableColumn
dot5StatsBurstErrors = _Dot5StatsBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 3),
    _Dot5StatsBurstErrors_Type()
)
dot5StatsBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsBurstErrors.setStatus("mandatory")
_Dot5StatsACErrors_Type = Counter32
_Dot5StatsACErrors_Object = MibTableColumn
dot5StatsACErrors = _Dot5StatsACErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 4),
    _Dot5StatsACErrors_Type()
)
dot5StatsACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsACErrors.setStatus("mandatory")
_Dot5StatsAbortTransErrors_Type = Counter32
_Dot5StatsAbortTransErrors_Object = MibTableColumn
dot5StatsAbortTransErrors = _Dot5StatsAbortTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 5),
    _Dot5StatsAbortTransErrors_Type()
)
dot5StatsAbortTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsAbortTransErrors.setStatus("mandatory")
_Dot5StatsInternalErrors_Type = Counter32
_Dot5StatsInternalErrors_Object = MibTableColumn
dot5StatsInternalErrors = _Dot5StatsInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 6),
    _Dot5StatsInternalErrors_Type()
)
dot5StatsInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsInternalErrors.setStatus("mandatory")
_Dot5StatsLostFrameErrors_Type = Counter32
_Dot5StatsLostFrameErrors_Object = MibTableColumn
dot5StatsLostFrameErrors = _Dot5StatsLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 7),
    _Dot5StatsLostFrameErrors_Type()
)
dot5StatsLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsLostFrameErrors.setStatus("mandatory")
_Dot5StatsReceiveCongestions_Type = Counter32
_Dot5StatsReceiveCongestions_Object = MibTableColumn
dot5StatsReceiveCongestions = _Dot5StatsReceiveCongestions_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 8),
    _Dot5StatsReceiveCongestions_Type()
)
dot5StatsReceiveCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsReceiveCongestions.setStatus("mandatory")
_Dot5StatsFrameCopiedErrors_Type = Counter32
_Dot5StatsFrameCopiedErrors_Object = MibTableColumn
dot5StatsFrameCopiedErrors = _Dot5StatsFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 9),
    _Dot5StatsFrameCopiedErrors_Type()
)
dot5StatsFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsFrameCopiedErrors.setStatus("mandatory")
_Dot5StatsTokenErrors_Type = Counter32
_Dot5StatsTokenErrors_Object = MibTableColumn
dot5StatsTokenErrors = _Dot5StatsTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 10),
    _Dot5StatsTokenErrors_Type()
)
dot5StatsTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsTokenErrors.setStatus("mandatory")
_Dot5StatsSoftErrors_Type = Counter32
_Dot5StatsSoftErrors_Object = MibTableColumn
dot5StatsSoftErrors = _Dot5StatsSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 11),
    _Dot5StatsSoftErrors_Type()
)
dot5StatsSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsSoftErrors.setStatus("mandatory")
_Dot5StatsHardErrors_Type = Counter32
_Dot5StatsHardErrors_Object = MibTableColumn
dot5StatsHardErrors = _Dot5StatsHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 12),
    _Dot5StatsHardErrors_Type()
)
dot5StatsHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsHardErrors.setStatus("mandatory")
_Dot5StatsSignalLoss_Type = Counter32
_Dot5StatsSignalLoss_Object = MibTableColumn
dot5StatsSignalLoss = _Dot5StatsSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 13),
    _Dot5StatsSignalLoss_Type()
)
dot5StatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsSignalLoss.setStatus("mandatory")
_Dot5StatsTransmitBeacons_Type = Counter32
_Dot5StatsTransmitBeacons_Object = MibTableColumn
dot5StatsTransmitBeacons = _Dot5StatsTransmitBeacons_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 14),
    _Dot5StatsTransmitBeacons_Type()
)
dot5StatsTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsTransmitBeacons.setStatus("mandatory")
_Dot5StatsRecoverys_Type = Counter32
_Dot5StatsRecoverys_Object = MibTableColumn
dot5StatsRecoverys = _Dot5StatsRecoverys_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 15),
    _Dot5StatsRecoverys_Type()
)
dot5StatsRecoverys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsRecoverys.setStatus("mandatory")
_Dot5StatsLobeWires_Type = Counter32
_Dot5StatsLobeWires_Object = MibTableColumn
dot5StatsLobeWires = _Dot5StatsLobeWires_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 16),
    _Dot5StatsLobeWires_Type()
)
dot5StatsLobeWires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsLobeWires.setStatus("mandatory")
_Dot5StatsRemoves_Type = Counter32
_Dot5StatsRemoves_Object = MibTableColumn
dot5StatsRemoves = _Dot5StatsRemoves_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 17),
    _Dot5StatsRemoves_Type()
)
dot5StatsRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsRemoves.setStatus("mandatory")
_Dot5StatsSingles_Type = Counter32
_Dot5StatsSingles_Object = MibTableColumn
dot5StatsSingles = _Dot5StatsSingles_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 18),
    _Dot5StatsSingles_Type()
)
dot5StatsSingles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsSingles.setStatus("mandatory")
_Dot5StatsFreqErrors_Type = Counter32
_Dot5StatsFreqErrors_Object = MibTableColumn
dot5StatsFreqErrors = _Dot5StatsFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 2, 1, 19),
    _Dot5StatsFreqErrors_Type()
)
dot5StatsFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsFreqErrors.setStatus("optional")
_Dot5Tests_ObjectIdentity = ObjectIdentity
dot5Tests = _Dot5Tests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 3)
)
_TestInsertFunc_ObjectIdentity = ObjectIdentity
testInsertFunc = _TestInsertFunc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 3, 1)
)
_Dot5ChipSets_ObjectIdentity = ObjectIdentity
dot5ChipSets = _Dot5ChipSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 4)
)
_ChipSetIBM16_ObjectIdentity = ObjectIdentity
chipSetIBM16 = _ChipSetIBM16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 4, 1)
)
_ChipSetTItms380_ObjectIdentity = ObjectIdentity
chipSetTItms380 = _ChipSetTItms380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 4, 2)
)
_ChipSetTItms380c16_ObjectIdentity = ObjectIdentity
chipSetTItms380c16 = _ChipSetTItms380c16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 4, 3)
)
_Dot5TimerTable_Object = MibTable
dot5TimerTable = _Dot5TimerTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dot5TimerTable.setStatus("mandatory")
_Dot5TimerEntry_Object = MibTableRow
dot5TimerEntry = _Dot5TimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1)
)
dot5TimerEntry.setIndexNames(
    (0, "CHIPDOT5-MIB", "dot5TimerIfIndex"),
)
if mibBuilder.loadTexts:
    dot5TimerEntry.setStatus("mandatory")
_Dot5TimerIfIndex_Type = Integer32
_Dot5TimerIfIndex_Object = MibTableColumn
dot5TimerIfIndex = _Dot5TimerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 1),
    _Dot5TimerIfIndex_Type()
)
dot5TimerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerIfIndex.setStatus("mandatory")
_Dot5TimerReturnRepeat_Type = Integer32
_Dot5TimerReturnRepeat_Object = MibTableColumn
dot5TimerReturnRepeat = _Dot5TimerReturnRepeat_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 2),
    _Dot5TimerReturnRepeat_Type()
)
dot5TimerReturnRepeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerReturnRepeat.setStatus("mandatory")
_Dot5TimerHolding_Type = Integer32
_Dot5TimerHolding_Object = MibTableColumn
dot5TimerHolding = _Dot5TimerHolding_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 3),
    _Dot5TimerHolding_Type()
)
dot5TimerHolding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerHolding.setStatus("mandatory")
_Dot5TimerQueuePDU_Type = Integer32
_Dot5TimerQueuePDU_Object = MibTableColumn
dot5TimerQueuePDU = _Dot5TimerQueuePDU_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 4),
    _Dot5TimerQueuePDU_Type()
)
dot5TimerQueuePDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerQueuePDU.setStatus("mandatory")
_Dot5TimerValidTransmit_Type = Integer32
_Dot5TimerValidTransmit_Object = MibTableColumn
dot5TimerValidTransmit = _Dot5TimerValidTransmit_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 5),
    _Dot5TimerValidTransmit_Type()
)
dot5TimerValidTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerValidTransmit.setStatus("mandatory")
_Dot5TimerNoToken_Type = Integer32
_Dot5TimerNoToken_Object = MibTableColumn
dot5TimerNoToken = _Dot5TimerNoToken_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 6),
    _Dot5TimerNoToken_Type()
)
dot5TimerNoToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerNoToken.setStatus("mandatory")
_Dot5TimerActiveMon_Type = Integer32
_Dot5TimerActiveMon_Object = MibTableColumn
dot5TimerActiveMon = _Dot5TimerActiveMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 7),
    _Dot5TimerActiveMon_Type()
)
dot5TimerActiveMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerActiveMon.setStatus("mandatory")
_Dot5TimerStandbyMon_Type = Integer32
_Dot5TimerStandbyMon_Object = MibTableColumn
dot5TimerStandbyMon = _Dot5TimerStandbyMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 8),
    _Dot5TimerStandbyMon_Type()
)
dot5TimerStandbyMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerStandbyMon.setStatus("mandatory")
_Dot5TimerErrorReport_Type = Integer32
_Dot5TimerErrorReport_Object = MibTableColumn
dot5TimerErrorReport = _Dot5TimerErrorReport_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 9),
    _Dot5TimerErrorReport_Type()
)
dot5TimerErrorReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerErrorReport.setStatus("mandatory")
_Dot5TimerBeaconTransmit_Type = Integer32
_Dot5TimerBeaconTransmit_Object = MibTableColumn
dot5TimerBeaconTransmit = _Dot5TimerBeaconTransmit_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 10),
    _Dot5TimerBeaconTransmit_Type()
)
dot5TimerBeaconTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerBeaconTransmit.setStatus("mandatory")
_Dot5TimerBeaconReceive_Type = Integer32
_Dot5TimerBeaconReceive_Object = MibTableColumn
dot5TimerBeaconReceive = _Dot5TimerBeaconReceive_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1, 5, 1, 11),
    _Dot5TimerBeaconReceive_Type()
)
dot5TimerBeaconReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerBeaconReceive.setStatus("mandatory")
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14)
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


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHIPDOT5-MIB",
    **{"MacAddress": MacAddress,
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
       "trmm": trmm,
       "fmm": fmm,
       "focus1": focus1,
       "oeim": oeim,
       "chipExperiment": chipExperiment,
       "chipExpTokenRing": chipExpTokenRing,
       "dot5": dot5,
       "dot5Table": dot5Table,
       "dot5Entry": dot5Entry,
       "dot5IfIndex": dot5IfIndex,
       "dot5Commands": dot5Commands,
       "dot5RingStatus": dot5RingStatus,
       "dot5RingState": dot5RingState,
       "dot5RingOpenStatus": dot5RingOpenStatus,
       "dot5RingSpeed": dot5RingSpeed,
       "dot5UpStream": dot5UpStream,
       "dot5ActMonParticipate": dot5ActMonParticipate,
       "dot5Functional": dot5Functional,
       "dot5StatsTable": dot5StatsTable,
       "dot5StatsEntry": dot5StatsEntry,
       "dot5StatsIfIndex": dot5StatsIfIndex,
       "dot5StatsLineErrors": dot5StatsLineErrors,
       "dot5StatsBurstErrors": dot5StatsBurstErrors,
       "dot5StatsACErrors": dot5StatsACErrors,
       "dot5StatsAbortTransErrors": dot5StatsAbortTransErrors,
       "dot5StatsInternalErrors": dot5StatsInternalErrors,
       "dot5StatsLostFrameErrors": dot5StatsLostFrameErrors,
       "dot5StatsReceiveCongestions": dot5StatsReceiveCongestions,
       "dot5StatsFrameCopiedErrors": dot5StatsFrameCopiedErrors,
       "dot5StatsTokenErrors": dot5StatsTokenErrors,
       "dot5StatsSoftErrors": dot5StatsSoftErrors,
       "dot5StatsHardErrors": dot5StatsHardErrors,
       "dot5StatsSignalLoss": dot5StatsSignalLoss,
       "dot5StatsTransmitBeacons": dot5StatsTransmitBeacons,
       "dot5StatsRecoverys": dot5StatsRecoverys,
       "dot5StatsLobeWires": dot5StatsLobeWires,
       "dot5StatsRemoves": dot5StatsRemoves,
       "dot5StatsSingles": dot5StatsSingles,
       "dot5StatsFreqErrors": dot5StatsFreqErrors,
       "dot5Tests": dot5Tests,
       "testInsertFunc": testInsertFunc,
       "dot5ChipSets": dot5ChipSets,
       "chipSetIBM16": chipSetIBM16,
       "chipSetTItms380": chipSetTItms380,
       "chipSetTItms380c16": chipSetTItms380c16,
       "dot5TimerTable": dot5TimerTable,
       "dot5TimerEntry": dot5TimerEntry,
       "dot5TimerIfIndex": dot5TimerIfIndex,
       "dot5TimerReturnRepeat": dot5TimerReturnRepeat,
       "dot5TimerHolding": dot5TimerHolding,
       "dot5TimerQueuePDU": dot5TimerQueuePDU,
       "dot5TimerValidTransmit": dot5TimerValidTransmit,
       "dot5TimerNoToken": dot5TimerNoToken,
       "dot5TimerActiveMon": dot5TimerActiveMon,
       "dot5TimerStandbyMon": dot5TimerStandbyMon,
       "dot5TimerErrorReport": dot5TimerErrorReport,
       "dot5TimerBeaconTransmit": dot5TimerBeaconTransmit,
       "dot5TimerBeaconReceive": dot5TimerBeaconReceive,
       "dot1dBridge": dot1dBridge,
       "chipTTY": chipTTY,
       "chipTFTP": chipTFTP,
       "chipDownload": chipDownload}
)
