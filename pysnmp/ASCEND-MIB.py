# SNMP MIB module (ASCEND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:51 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ascend_ObjectIdentity = ObjectIdentity
ascend = _Ascend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1)
)
_Multiband_ObjectIdentity = ObjectIdentity
multiband = _Multiband_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 1)
)
_Max_ObjectIdentity = ObjectIdentity
max = _Max_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2)
)
_Max200_ObjectIdentity = ObjectIdentity
max200 = _Max200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 1)
)
_Max1800_ObjectIdentity = ObjectIdentity
max1800 = _Max1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 2)
)
_Max2000_ObjectIdentity = ObjectIdentity
max2000 = _Max2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 3)
)
_Max4000_ObjectIdentity = ObjectIdentity
max4000 = _Max4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 4)
)
_Max4002_ObjectIdentity = ObjectIdentity
max4002 = _Max4002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 5)
)
_Max4004_ObjectIdentity = ObjectIdentity
max4004 = _Max4004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 6)
)
_Max6000_ObjectIdentity = ObjectIdentity
max6000 = _Max6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 7)
)
_Max800_ObjectIdentity = ObjectIdentity
max800 = _Max800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 8)
)
_Max3000_ObjectIdentity = ObjectIdentity
max3000 = _Max3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 9)
)
_Dslmax20_ObjectIdentity = ObjectIdentity
dslmax20 = _Dslmax20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 10)
)
_Terminator_ObjectIdentity = ObjectIdentity
terminator = _Terminator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 11)
)
_Cvmax100_ObjectIdentity = ObjectIdentity
cvmax100 = _Cvmax100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 2, 12)
)
_Pipeline_ObjectIdentity = ObjectIdentity
pipeline = _Pipeline_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3)
)
_Pipe15_ObjectIdentity = ObjectIdentity
pipe15 = _Pipe15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 1)
)
_Pipe25_ObjectIdentity = ObjectIdentity
pipe25 = _Pipe25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 2)
)
_Pipe25Px_ObjectIdentity = ObjectIdentity
pipe25Px = _Pipe25Px_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 3)
)
_Pipe25Fx_ObjectIdentity = ObjectIdentity
pipe25Fx = _Pipe25Fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 4)
)
_Pipe50_ObjectIdentity = ObjectIdentity
pipe50 = _Pipe50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 5)
)
_Pipe75_ObjectIdentity = ObjectIdentity
pipe75 = _Pipe75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 6)
)
_Pipe130T1_ObjectIdentity = ObjectIdentity
pipe130T1 = _Pipe130T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 7)
)
_Pipe400_ObjectIdentity = ObjectIdentity
pipe400 = _Pipe400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 8)
)
_Pipe220_ObjectIdentity = ObjectIdentity
pipe220 = _Pipe220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 9)
)
_DslPipeAcap_ObjectIdentity = ObjectIdentity
dslPipeAcap = _DslPipeAcap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 10)
)
_DslPipeS_ObjectIdentity = ObjectIdentity
dslPipeS = _DslPipeS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 11)
)
_DslPipe2S_ObjectIdentity = ObjectIdentity
dslPipe2S = _DslPipe2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 12)
)
_DslPipeAdslCoeC_ObjectIdentity = ObjectIdentity
dslPipeAdslCoeC = _DslPipeAdslCoeC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 13)
)
_DslPipeSdslCoe_ObjectIdentity = ObjectIdentity
dslPipeSdslCoe = _DslPipeSdslCoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 14)
)
_DslPipeSdslCoe2S_ObjectIdentity = ObjectIdentity
dslPipeSdslCoe2S = _DslPipeSdslCoe2S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 15)
)
_Pipe85_ObjectIdentity = ObjectIdentity
pipe85 = _Pipe85_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 16)
)
_Pipe50LS56_ObjectIdentity = ObjectIdentity
pipe50LS56 = _Pipe50LS56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 17)
)
_Pipe130V35_ObjectIdentity = ObjectIdentity
pipe130V35 = _Pipe130V35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 18)
)
_Pipe130N56_ObjectIdentity = ObjectIdentity
pipe130N56 = _Pipe130N56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 19)
)
_DslPipeAdslCoeD_ObjectIdentity = ObjectIdentity
dslPipeAdslCoeD = _DslPipeAdslCoeD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 20)
)
_DslPipeAdmt_ObjectIdentity = ObjectIdentity
dslPipeAdmt = _DslPipeAdmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 21)
)
_DslPipeAlctlDmt_ObjectIdentity = ObjectIdentity
dslPipeAlctlDmt = _DslPipeAlctlDmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 22)
)
_Spipe95_ObjectIdentity = ObjectIdentity
spipe95 = _Spipe95_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 23)
)
_Spipe155T1_ObjectIdentity = ObjectIdentity
spipe155T1 = _Spipe155T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 24)
)
_DslPipe50SdslCell_ObjectIdentity = ObjectIdentity
dslPipe50SdslCell = _DslPipe50SdslCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 25)
)
_DslPipeSdslHs_ObjectIdentity = ObjectIdentity
dslPipeSdslHs = _DslPipeSdslHs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 3, 26)
)
_Max_tnt_ObjectIdentity = ObjectIdentity
max_tnt = _Max_tnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 4)
)
_DslTnt_ObjectIdentity = ObjectIdentity
dslTnt = _DslTnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 5)
)
_Aqueduct_ObjectIdentity = ObjectIdentity
aqueduct = _Aqueduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 6)
)
_Aq300_ObjectIdentity = ObjectIdentity
aq300 = _Aq300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 6, 1)
)
_Stinger_10_ObjectIdentity = ObjectIdentity
stinger_10 = _Stinger_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 7)
)
_Apx_8000_ObjectIdentity = ObjectIdentity
apx_8000 = _Apx_8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 1, 8)
)
_Slots_ObjectIdentity = ObjectIdentity
slots = _Slots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 2)
)
_HostTypes_ObjectIdentity = ObjectIdentity
hostTypes = _HostTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 3)
)
_HostTypeAny_ObjectIdentity = ObjectIdentity
hostTypeAny = _HostTypeAny_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 3, 1)
)
_HostTypeDual_ObjectIdentity = ObjectIdentity
hostTypeDual = _HostTypeDual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 3, 2)
)
_HostTypeQuad_ObjectIdentity = ObjectIdentity
hostTypeQuad = _HostTypeQuad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 3, 3)
)
_HostTypeAim2_ObjectIdentity = ObjectIdentity
hostTypeAim2 = _HostTypeAim2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 3, 4)
)
_HostTypeAim6_ObjectIdentity = ObjectIdentity
hostTypeAim6 = _HostTypeAim6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 3, 5)
)
_AdvancedAgent_ObjectIdentity = ObjectIdentity
advancedAgent = _AdvancedAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 4)
)
_LanTypes_ObjectIdentity = ObjectIdentity
lanTypes = _LanTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 5)
)
_LanTypeAny_ObjectIdentity = ObjectIdentity
lanTypeAny = _LanTypeAny_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 5, 1)
)
_LanTypeEthernet_ObjectIdentity = ObjectIdentity
lanTypeEthernet = _LanTypeEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 5, 2)
)
_LanTypeEtherData_ObjectIdentity = ObjectIdentity
lanTypeEtherData = _LanTypeEtherData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 5, 3)
)
_DoGroup_ObjectIdentity = ObjectIdentity
doGroup = _DoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 6)
)
_DoTable_Object = MibTable
doTable = _DoTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1)
)
if mibBuilder.loadTexts:
    doTable.setStatus("mandatory")
_DoEntry_Object = MibTableRow
doEntry = _DoEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1, 1)
)
doEntry.setIndexNames(
    (0, "ASCEND-MIB", "doSlotIndex"),
    (0, "ASCEND-MIB", "doItemIndex"),
)
if mibBuilder.loadTexts:
    doEntry.setStatus("mandatory")
_DoSlotIndex_Type = Integer32
_DoSlotIndex_Object = MibTableColumn
doSlotIndex = _DoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1, 1, 1),
    _DoSlotIndex_Type()
)
doSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doSlotIndex.setStatus("mandatory")
_DoItemIndex_Type = Integer32
_DoItemIndex_Object = MibTableColumn
doItemIndex = _DoItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1, 1, 2),
    _DoItemIndex_Type()
)
doItemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doItemIndex.setStatus("mandatory")


class _DoDial_Type(Integer32):
    """Custom type doDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 2),
          ("valid", 1))
    )


_DoDial_Type.__name__ = "Integer32"
_DoDial_Object = MibTableColumn
doDial = _DoDial_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1, 1, 3),
    _DoDial_Type()
)
doDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doDial.setStatus("mandatory")


class _DoHangUp_Type(Integer32):
    """Custom type doHangUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 2),
          ("valid", 1))
    )


_DoHangUp_Type.__name__ = "Integer32"
_DoHangUp_Object = MibTableColumn
doHangUp = _DoHangUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1, 1, 4),
    _DoHangUp_Type()
)
doHangUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doHangUp.setStatus("mandatory")


class _DoAnswer_Type(Integer32):
    """Custom type doAnswer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 2),
          ("valid", 1))
    )


_DoAnswer_Type.__name__ = "Integer32"
_DoAnswer_Object = MibTableColumn
doAnswer = _DoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1, 1, 5),
    _DoAnswer_Type()
)
doAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doAnswer.setStatus("mandatory")


class _DoExtendBW_Type(Integer32):
    """Custom type doExtendBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 2),
          ("valid", 1))
    )


_DoExtendBW_Type.__name__ = "Integer32"
_DoExtendBW_Object = MibTableColumn
doExtendBW = _DoExtendBW_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1, 1, 6),
    _DoExtendBW_Type()
)
doExtendBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doExtendBW.setStatus("mandatory")


class _DoContractBW_Type(Integer32):
    """Custom type doContractBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 2),
          ("valid", 1))
    )


_DoContractBW_Type.__name__ = "Integer32"
_DoContractBW_Object = MibTableColumn
doContractBW = _DoContractBW_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1, 1, 7),
    _DoContractBW_Type()
)
doContractBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doContractBW.setStatus("mandatory")


class _DoBegEndRemoteLB_Type(Integer32):
    """Custom type doBegEndRemoteLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 2),
          ("valid", 1))
    )


_DoBegEndRemoteLB_Type.__name__ = "Integer32"
_DoBegEndRemoteLB_Object = MibTableColumn
doBegEndRemoteLB = _DoBegEndRemoteLB_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1, 1, 8),
    _DoBegEndRemoteLB_Type()
)
doBegEndRemoteLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doBegEndRemoteLB.setStatus("mandatory")


class _DoBegEndBERT_Type(Integer32):
    """Custom type doBegEndBERT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 2),
          ("valid", 1))
    )


_DoBegEndBERT_Type.__name__ = "Integer32"
_DoBegEndBERT_Object = MibTableColumn
doBegEndBERT = _DoBegEndBERT_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1, 1, 9),
    _DoBegEndBERT_Type()
)
doBegEndBERT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doBegEndBERT.setStatus("mandatory")


class _DoResynchronize_Type(Integer32):
    """Custom type doResynchronize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 2),
          ("valid", 1))
    )


_DoResynchronize_Type.__name__ = "Integer32"
_DoResynchronize_Object = MibTableColumn
doResynchronize = _DoResynchronize_Object(
    (1, 3, 6, 1, 4, 1, 529, 6, 1, 1, 10),
    _DoResynchronize_Type()
)
doResynchronize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doResynchronize.setStatus("mandatory")
_HostStatus_ObjectIdentity = ObjectIdentity
hostStatus = _HostStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 7)
)
_HostStatusTable_Object = MibTable
hostStatusTable = _HostStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1)
)
if mibBuilder.loadTexts:
    hostStatusTable.setStatus("mandatory")
_HostStatusEntry_Object = MibTableRow
hostStatusEntry = _HostStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1)
)
hostStatusEntry.setIndexNames(
    (0, "ASCEND-MIB", "hostStatusSlotIndex"),
    (0, "ASCEND-MIB", "hostStatusItemIndex"),
)
if mibBuilder.loadTexts:
    hostStatusEntry.setStatus("mandatory")
_HostStatusSlotIndex_Type = Integer32
_HostStatusSlotIndex_Object = MibTableColumn
hostStatusSlotIndex = _HostStatusSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1, 1),
    _HostStatusSlotIndex_Type()
)
hostStatusSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatusSlotIndex.setStatus("mandatory")
_HostStatusItemIndex_Type = Integer32
_HostStatusItemIndex_Object = MibTableColumn
hostStatusItemIndex = _HostStatusItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1, 2),
    _HostStatusItemIndex_Type()
)
hostStatusItemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatusItemIndex.setStatus("mandatory")
_HostStatusLocalName_Type = OctetString
_HostStatusLocalName_Object = MibTableColumn
hostStatusLocalName = _HostStatusLocalName_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1, 3),
    _HostStatusLocalName_Type()
)
hostStatusLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatusLocalName.setStatus("mandatory")
_HostStatusDialNum_Type = OctetString
_HostStatusDialNum_Object = MibTableColumn
hostStatusDialNum = _HostStatusDialNum_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1, 4),
    _HostStatusDialNum_Type()
)
hostStatusDialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatusDialNum.setStatus("mandatory")


class _HostStatusCallType_Type(Integer32):
    """Custom type hostStatusCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aim", 1),
          ("bonding", 2),
          ("ft1", 5),
          ("ft1Aim", 6),
          ("ft1BandO", 7),
          ("one-channel", 3),
          ("two-channel", 4))
    )


_HostStatusCallType_Type.__name__ = "Integer32"
_HostStatusCallType_Object = MibTableColumn
hostStatusCallType = _HostStatusCallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1, 5),
    _HostStatusCallType_Type()
)
hostStatusCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatusCallType.setStatus("mandatory")


class _HostStatusCallMgm_Type(Integer32):
    """Custom type hostStatusCallMgm based on Integer32"""
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
        *(("delta", 5),
          ("dynamic", 4),
          ("manual", 2),
          ("mode0", 11),
          ("mode1", 8),
          ("mode2", 9),
          ("mode3", 10),
          ("none", 1),
          ("one-of-40", 7),
          ("one-of-8", 6),
          ("static", 3))
    )


_HostStatusCallMgm_Type.__name__ = "Integer32"
_HostStatusCallMgm_Object = MibTableColumn
hostStatusCallMgm = _HostStatusCallMgm_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1, 6),
    _HostStatusCallMgm_Type()
)
hostStatusCallMgm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatusCallMgm.setStatus("mandatory")


class _HostStatusDataSvc_Type(Integer32):
    """Custom type hostStatusDataSvc based on Integer32"""
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("service1024K", 23),
          ("service1088K", 24),
          ("service1152K", 25),
          ("service1216K", 26),
          ("service1280K", 27),
          ("service128K", 9),
          ("service1344K", 28),
          ("service1408K", 29),
          ("service1472K", 30),
          ("service1536K", 7),
          ("service1536KR", 8),
          ("service1600K", 31),
          ("service1664K", 32),
          ("service1728K", 33),
          ("service1792K", 34),
          ("service1856K", 35),
          ("service1920K", 36),
          ("service192K", 10),
          ("service256K", 11),
          ("service320K", 12),
          ("service384K", 13),
          ("service384K-H0", 6),
          ("service384KR", 5),
          ("service448K", 14),
          ("service512K", 15),
          ("service56K", 3),
          ("service56KR", 2),
          ("service576K", 16),
          ("service640K", 17),
          ("service64K", 4),
          ("service704K", 18),
          ("service768K", 19),
          ("service832K", 20),
          ("service896K", 21),
          ("service960K", 22),
          ("serviceModem", 37),
          ("serviceV110-192-56K", 41),
          ("serviceV110-192-56KR", 46),
          ("serviceV110-192-64K", 51),
          ("serviceV110-192-64KR", 56),
          ("serviceV110-24-56K", 38),
          ("serviceV110-24-56KR", 43),
          ("serviceV110-24-64K", 48),
          ("serviceV110-24-64KR", 53),
          ("serviceV110-384-56K", 42),
          ("serviceV110-384-56KR", 47),
          ("serviceV110-384-64K", 52),
          ("serviceV110-384-64KR", 57),
          ("serviceV110-48-56K", 39),
          ("serviceV110-48-56KR", 44),
          ("serviceV110-48-64K", 49),
          ("serviceV110-48-64KR", 54),
          ("serviceV110-96-56K", 40),
          ("serviceV110-96-56KR", 45),
          ("serviceV110-96-64K", 50),
          ("serviceV110-96-64KR", 55),
          ("serviceVoice", 1))
    )


_HostStatusDataSvc_Type.__name__ = "Integer32"
_HostStatusDataSvc_Object = MibTableColumn
hostStatusDataSvc = _HostStatusDataSvc_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1, 7),
    _HostStatusDataSvc_Type()
)
hostStatusDataSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatusDataSvc.setStatus("mandatory")


class _HostStatusCallState_Type(Integer32):
    """Custom type hostStatusCallState based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("answering", 2),
          ("bertMast", 11),
          ("bertSlav", 12),
          ("calling", 3),
          ("clearing", 4),
          ("handshake", 6),
          ("idle", 7),
          ("localLoop", 5),
          ("loopMast", 9),
          ("loopSlav", 10),
          ("online", 8),
          ("other", 1),
          ("remoteMg", 13),
          ("ringing", 14),
          ("setupAdd", 15),
          ("setupHnd", 16),
          ("setupRem", 17))
    )


_HostStatusCallState_Type.__name__ = "Integer32"
_HostStatusCallState_Object = MibTableColumn
hostStatusCallState = _HostStatusCallState_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1, 8),
    _HostStatusCallState_Type()
)
hostStatusCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatusCallState.setStatus("mandatory")
_HostStatusRemName_Type = OctetString
_HostStatusRemName_Object = MibTableColumn
hostStatusRemName = _HostStatusRemName_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1, 9),
    _HostStatusRemName_Type()
)
hostStatusRemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatusRemName.setStatus("mandatory")
_HostStatusChannels_Type = Integer32
_HostStatusChannels_Object = MibTableColumn
hostStatusChannels = _HostStatusChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1, 10),
    _HostStatusChannels_Type()
)
hostStatusChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatusChannels.setStatus("mandatory")
_HostStatusDuration_Type = Integer32
_HostStatusDuration_Object = MibTableColumn
hostStatusDuration = _HostStatusDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 7, 1, 1, 11),
    _HostStatusDuration_Type()
)
hostStatusDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatusDuration.setStatus("mandatory")
_Console_ObjectIdentity = ObjectIdentity
console = _Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 8)
)
_ConsoleNumber_Type = Integer32
_ConsoleNumber_Object = MibScalar
consoleNumber = _ConsoleNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 8, 1),
    _ConsoleNumber_Type()
)
consoleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleNumber.setStatus("mandatory")
_ConsoleTable_Object = MibTable
consoleTable = _ConsoleTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 8, 2)
)
if mibBuilder.loadTexts:
    consoleTable.setStatus("mandatory")
_ConsoleEntry_Object = MibTableRow
consoleEntry = _ConsoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 8, 2, 1)
)
consoleEntry.setIndexNames(
    (0, "ASCEND-MIB", "consoleIndex"),
)
if mibBuilder.loadTexts:
    consoleEntry.setStatus("mandatory")
_ConsoleIndex_Type = Integer32
_ConsoleIndex_Object = MibTableColumn
consoleIndex = _ConsoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 8, 2, 1, 1),
    _ConsoleIndex_Type()
)
consoleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleIndex.setStatus("mandatory")
_ConsoleIf_Type = Integer32
_ConsoleIf_Object = MibTableColumn
consoleIf = _ConsoleIf_Object(
    (1, 3, 6, 1, 4, 1, 529, 8, 2, 1, 2),
    _ConsoleIf_Type()
)
consoleIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleIf.setStatus("mandatory")


class _ConsoleType_Type(Integer32):
    """Custom type consoleType based on Integer32"""
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
        *(("inactive", 5),
          ("other", 1),
          ("palmtop", 4),
          ("primary", 2),
          ("remote", 6),
          ("secondary", 3))
    )


_ConsoleType_Type.__name__ = "Integer32"
_ConsoleType_Object = MibTableColumn
consoleType = _ConsoleType_Object(
    (1, 3, 6, 1, 4, 1, 529, 8, 2, 1, 3),
    _ConsoleType_Type()
)
consoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleType.setStatus("mandatory")
_ConsoleSecurity_Type = Integer32
_ConsoleSecurity_Object = MibTableColumn
consoleSecurity = _ConsoleSecurity_Object(
    (1, 3, 6, 1, 4, 1, 529, 8, 2, 1, 4),
    _ConsoleSecurity_Type()
)
consoleSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleSecurity.setStatus("mandatory")
_ConsoleSpecific_Type = ObjectIdentifier
_ConsoleSpecific_Object = MibTableColumn
consoleSpecific = _ConsoleSpecific_Object(
    (1, 3, 6, 1, 4, 1, 529, 8, 2, 1, 5),
    _ConsoleSpecific_Type()
)
consoleSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleSpecific.setStatus("mandatory")
_SystemStatusGroup_ObjectIdentity = ObjectIdentity
systemStatusGroup = _SystemStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 9)
)
_SysAbsoluteStartupTime_Type = Integer32
_SysAbsoluteStartupTime_Object = MibScalar
sysAbsoluteStartupTime = _SysAbsoluteStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 1),
    _SysAbsoluteStartupTime_Type()
)
sysAbsoluteStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAbsoluteStartupTime.setStatus("mandatory")
_SysSecsSinceStartup_Type = Integer32
_SysSecsSinceStartup_Object = MibScalar
sysSecsSinceStartup = _SysSecsSinceStartup_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 2),
    _SysSecsSinceStartup_Type()
)
sysSecsSinceStartup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecsSinceStartup.setStatus("mandatory")
_SysMibVersionNum_Type = Integer32
_SysMibVersionNum_Object = MibScalar
sysMibVersionNum = _SysMibVersionNum_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 3),
    _SysMibVersionNum_Type()
)
sysMibVersionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMibVersionNum.setStatus("mandatory")
_SysMibMinorRevNum_Type = Integer32
_SysMibMinorRevNum_Object = MibScalar
sysMibMinorRevNum = _SysMibMinorRevNum_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 4),
    _SysMibMinorRevNum_Type()
)
sysMibMinorRevNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMibMinorRevNum.setStatus("mandatory")
_SysConfigTftp_ObjectIdentity = ObjectIdentity
sysConfigTftp = _SysConfigTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 9, 5)
)


class _SysConfigTftpCmd_Type(Integer32):
    """Custom type sysConfigTftpCmd based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("loadCode", 6),
          ("restore", 2),
          ("save", 1),
          ("saveAll", 3),
          ("saveAllMib", 5),
          ("saveExcProf", 8),
          ("saveIncProf", 7),
          ("saveMib", 4))
    )


_SysConfigTftpCmd_Type.__name__ = "Integer32"
_SysConfigTftpCmd_Object = MibScalar
sysConfigTftpCmd = _SysConfigTftpCmd_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 5, 1),
    _SysConfigTftpCmd_Type()
)
sysConfigTftpCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigTftpCmd.setStatus("mandatory")


class _SysConfigTftpStatus_Type(Integer32):
    """Custom type sysConfigTftpStatus based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("access", 3),
          ("badOp", 5),
          ("badTid", 6),
          ("busy", 10),
          ("createFile", 15),
          ("exists", 7),
          ("inProgress", 17),
          ("noResources", 11),
          ("noSpace", 4),
          ("noSuchUser", 8),
          ("notFound", 2),
          ("ok", 1),
          ("openFile", 16),
          ("parameter", 9),
          ("timeout", 12),
          ("tooManyRetries", 14),
          ("unrecoverable", 13))
    )


_SysConfigTftpStatus_Type.__name__ = "Integer32"
_SysConfigTftpStatus_Object = MibScalar
sysConfigTftpStatus = _SysConfigTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 5, 2),
    _SysConfigTftpStatus_Type()
)
sysConfigTftpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigTftpStatus.setStatus("mandatory")
_SysConfigTftpHostAddr_Type = IpAddress
_SysConfigTftpHostAddr_Object = MibScalar
sysConfigTftpHostAddr = _SysConfigTftpHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 5, 3),
    _SysConfigTftpHostAddr_Type()
)
sysConfigTftpHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigTftpHostAddr.setStatus("mandatory")
_SysConfigTftpFilename_Type = DisplayString
_SysConfigTftpFilename_Object = MibScalar
sysConfigTftpFilename = _SysConfigTftpFilename_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 5, 4),
    _SysConfigTftpFilename_Type()
)
sysConfigTftpFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigTftpFilename.setStatus("mandatory")
_SysConfigTftpPort_Type = Integer32
_SysConfigTftpPort_Object = MibScalar
sysConfigTftpPort = _SysConfigTftpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 5, 5),
    _SysConfigTftpPort_Type()
)
sysConfigTftpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigTftpPort.setStatus("mandatory")
_SysConfigTftpParameter_Type = DisplayString
_SysConfigTftpParameter_Object = MibScalar
sysConfigTftpParameter = _SysConfigTftpParameter_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 5, 6),
    _SysConfigTftpParameter_Type()
)
sysConfigTftpParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigTftpParameter.setStatus("mandatory")
_SysConfigRadius_ObjectIdentity = ObjectIdentity
sysConfigRadius = _SysConfigRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 9, 6)
)


class _SysConfigRadiusCmd_Type(Integer32):
    """Custom type sysConfigRadiusCmd based on Integer32"""
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
        *(("all", 1),
          ("nailed", 4),
          ("pools", 3),
          ("routes", 2),
          ("source", 6),
          ("termsrv", 5))
    )


_SysConfigRadiusCmd_Type.__name__ = "Integer32"
_SysConfigRadiusCmd_Object = MibScalar
sysConfigRadiusCmd = _SysConfigRadiusCmd_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 6, 1),
    _SysConfigRadiusCmd_Type()
)
sysConfigRadiusCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigRadiusCmd.setStatus("mandatory")


class _SysConfigRadiusStatus_Type(Integer32):
    """Custom type sysConfigRadiusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("complete", 5),
          ("error", 4),
          ("init", 1),
          ("processing", 2),
          ("timeout", 3))
    )


_SysConfigRadiusStatus_Type.__name__ = "Integer32"
_SysConfigRadiusStatus_Object = MibScalar
sysConfigRadiusStatus = _SysConfigRadiusStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 6, 2),
    _SysConfigRadiusStatus_Type()
)
sysConfigRadiusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigRadiusStatus.setStatus("mandatory")
_SysAbsoluteCurrentTime_Type = Integer32
_SysAbsoluteCurrentTime_Object = MibScalar
sysAbsoluteCurrentTime = _SysAbsoluteCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 7),
    _SysAbsoluteCurrentTime_Type()
)
sysAbsoluteCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAbsoluteCurrentTime.setStatus("mandatory")


class _SysReset_Type(Integer32):
    """Custom type sysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-op", 1),
          ("reset", 2))
    )


_SysReset_Type.__name__ = "Integer32"
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 8),
    _SysReset_Type()
)
sysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysReset.setStatus("mandatory")
_SysLoadName_Type = DisplayString
_SysLoadName_Object = MibScalar
sysLoadName = _SysLoadName_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 9),
    _SysLoadName_Type()
)
sysLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoadName.setStatus("mandatory")


class _SysAuthPreference_Type(Integer32):
    """Custom type sysAuthPreference based on Integer32"""
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
        *(("local-first", 2),
          ("no-op", 1),
          ("remote-first", 3),
          ("remote-no", 4))
    )


_SysAuthPreference_Type.__name__ = "Integer32"
_SysAuthPreference_Object = MibScalar
sysAuthPreference = _SysAuthPreference_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 10),
    _SysAuthPreference_Type()
)
sysAuthPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAuthPreference.setStatus("mandatory")
_SysSPROM_ObjectIdentity = ObjectIdentity
sysSPROM = _SysSPROM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 9, 11)
)
_SysSPROMSerialNumber_Type = Integer32
_SysSPROMSerialNumber_Object = MibScalar
sysSPROMSerialNumber = _SysSPROMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 11, 1),
    _SysSPROMSerialNumber_Type()
)
sysSPROMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSPROMSerialNumber.setStatus("mandatory")
_SysSPROMOptions1_Type = Integer32
_SysSPROMOptions1_Object = MibScalar
sysSPROMOptions1 = _SysSPROMOptions1_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 11, 2),
    _SysSPROMOptions1_Type()
)
sysSPROMOptions1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSPROMOptions1.setStatus("mandatory")
_SysSPROMOptions2_Type = Integer32
_SysSPROMOptions2_Object = MibScalar
sysSPROMOptions2 = _SysSPROMOptions2_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 11, 3),
    _SysSPROMOptions2_Type()
)
sysSPROMOptions2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSPROMOptions2.setStatus("mandatory")
_SysSPROMCountries1_Type = Integer32
_SysSPROMCountries1_Object = MibScalar
sysSPROMCountries1 = _SysSPROMCountries1_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 11, 4),
    _SysSPROMCountries1_Type()
)
sysSPROMCountries1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSPROMCountries1.setStatus("mandatory")
_ResetStat_ObjectIdentity = ObjectIdentity
resetStat = _ResetStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 9, 12)
)
_ResetStatEther_Type = Integer32
_ResetStatEther_Object = MibScalar
resetStatEther = _ResetStatEther_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 12, 1),
    _ResetStatEther_Type()
)
resetStatEther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStatEther.setStatus("mandatory")
_ResetStatWAN_Type = Integer32
_ResetStatWAN_Object = MibScalar
resetStatWAN = _ResetStatWAN_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 12, 2),
    _ResetStatWAN_Type()
)
resetStatWAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStatWAN.setStatus("mandatory")
_ResetStatAll_Type = Integer32
_ResetStatAll_Object = MibScalar
resetStatAll = _ResetStatAll_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 12, 3),
    _ResetStatAll_Type()
)
resetStatAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStatAll.setStatus("mandatory")


class _SysLastRestartReason_Type(Integer32):
    """Custom type sysLastRestartReason based on Integer32"""
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
              24,
              25,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              55,
              60,
              61,
              62,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              129,
              130,
              131,
              135,
              136,
              140,
              145,
              146,
              150,
              151,
              152,
              153,
              154,
              160,
              161,
              165,
              170,
              171,
              175,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              200,
              201,
              210,
              211,
              220,
              221,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              309,
              310,
              311,
              312,
              313,
              314,
              320,
              321,
              330,
              381,
              382,
              383,
              384,
              385,
              400,
              512,
              550,
              767,
              768,
              800,
              801,
              999,
              1001,
              1002,
              1003,
              1005,
              1006,
              1007,
              2001,
              2002,
              2010,
              2022,
              2100,
              2101,
              3001,
              3002,
              3003,
              4000,
              4100,
              9998,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("errprPPPAsuncBufferInUse", 130),
          ("fataExecNoTimerPool", 14),
          ("fatalATMSVC", 46),
          ("fatalAssert", 1),
          ("fatalBadPower", 60),
          ("fatalClipping", 41),
          ("fatalDDDDead", 21),
          ("fatalDDDProtocolError", 22),
          ("fatalDRAMCard", 37),
          ("fatalDspDead", 16),
          ("fatalDspInternalError", 18),
          ("fatalDspLossOfSync", 19),
          ("fatalDspProtocolError", 17),
          ("fatalDspUnUsed", 20),
          ("fatalExcessPostCompl", 43),
          ("fatalExecInvalidSwitch", 9),
          ("fatalExecNoMailDesc", 10),
          ("fatalExecNoMailPoll", 11),
          ("fatalExecNoTask", 12),
          ("fatalExecNoTimer", 13),
          ("fatalExecRestricted", 35),
          ("fatalExecWaitInCtricalSection", 15),
          ("fatalFRSVC", 47),
          ("fatalIDECTimeout", 34),
          ("fatalInterruptCode", 48),
          ("fatalIsacTimeout", 7),
          ("fatalLcdError", 6),
          ("fatalLif", 5),
          ("fatalLinkedListCorruption", 55),
          ("fatalMbufPanic", 38),
          ("fatalMemcoyBadStart", 33),
          ("fatalMemcpyNoMagic", 31),
          ("fatalMemcpyTooLarge", 30),
          ("fatalMemcpyWrongMagic", 32),
          ("fatalNegativeMemoryAllocate", 28),
          ("fatalNoPriority2Task", 39),
          ("fatalOperatorReset", 99),
          ("fatalPoolsNoBuffer", 2),
          ("fatalPrimarySelected", 98),
          ("fatalProfileBad", 3),
          ("fatalProtectionFault", 40),
          ("fatalPureVirtual", 45),
          ("fatalReadyHangFault", 42),
          ("fatalSCCSpuriousInterrupt", 8),
          ("fatalStackOverflow", 36),
          ("fatalSwitchTypeBad", 4),
          ("fatalSystemUp", 100),
          ("fatalTaskLoop", 29),
          ("fatalUnexplainedNMI", 62),
          ("fatalWatchdogTimeout", 61),
          ("fatalWriteProtect", 44),
          ("fatalX25Buffers", 23),
          ("fatalX25Init", 24),
          ("fatalX25Stack", 25),
          ("fatalZeroMemoryAlloc", 27),
          ("infoCardBounced", 220),
          ("infoCardDown", 221),
          ("infoSystemResetOccurred", 385),
          ("notApplicable", 9998),
          ("unknown", 9999),
          ("warningBadChunk", 135),
          ("warningBadPowerSupply", 400),
          ("warningBaeepromChange", 2001),
          ("warningBaeepromImageMismatch", 2002),
          ("warningBriJumperConfiguration", 211),
          ("warningBriJumperNotPresent", 210),
          ("warningBufferBadMemAlloc", 105),
          ("warningBufferBogusHeap", 107),
          ("warningBufferBogusPool", 106),
          ("warningBufferBoundary", 110),
          ("warningBufferInUse", 101),
          ("warningBufferMemcpyMagic", 120),
          ("warningBufferMemcpyMagicNext", 121),
          ("warningBufferNegativeMemalloc", 108),
          ("warningBufferNoExtraDRAM", 129),
          ("warningBufferNotInUse", 119),
          ("warningBufferNotMemAlloc", 104),
          ("warningBufferNull", 112),
          ("warningBufferSegmentCountZero", 113),
          ("warningBufferTooBig", 111),
          ("warningBufferTrailerBuffer", 115),
          ("warningBufferTrailerLength", 116),
          ("warningBufferTrailerMagic", 114),
          ("warningBufferTrailerUserMagic", 117),
          ("warningBufferWriteAfterFree", 118),
          ("warningBufferWrongHeap", 103),
          ("warningBufferWrongPool", 102),
          ("warningBufferZeroMemalloc", 109),
          ("warningCdtUnprotectedAccess", 384),
          ("warningChannelDisplayStuck", 181),
          ("warningChannelMapStuck", 180),
          ("warningCidrBusy", 312),
          ("warningCidrDupDelete", 314),
          ("warningCidrNoMem", 311),
          ("warningCidrNonempty", 313),
          ("warningCidrWrongTree", 310),
          ("warningDisconnectRequestDropped", 184),
          ("warningDspCrashMax", 767),
          ("warningDspCrashMin", 512),
          ("warningDspWrongSlot", 768),
          ("warningEthernetAckFailure", 1002),
          ("warningEthernetCuActive", 1005),
          ("warningEthernetCuBusy", 1001),
          ("warningEthernetNoMACAddress", 1007),
          ("warningEthernetNoTxBuf", 550),
          ("warningEthernetReset", 1003),
          ("warningEthernetWaitScb", 1006),
          ("warningExecFailure", 175),
          ("warningExecNoMailbox", 177),
          ("warningExecNoResources", 178),
          ("warningExecRestricted", 999),
          ("warningFlashTypeBad", 2010),
          ("warningGdbProtectionFault", 330),
          ("warningH323NoResources", 801),
          ("warningHscxSlowRelay", 188),
          ("warningInFilterList", 381),
          ("warningIpcpIpLookup", 131),
          ("warningIpxsapFilterCountMismatch", 3003),
          ("warningIpxsapFilterCountZero", 3002),
          ("warningIpxsapFilterMagic", 3001),
          ("warningLCDAllocFailure", 145),
          ("warningLCDNonSense", 146),
          ("warningLmodDspDown", 196),
          ("warningLmodDspmodemDown", 197),
          ("warningLmodSlotDown", 195),
          ("warningMaxiopLoadFailure", 2022),
          ("warningMemcpyBadStart", 153),
          ("warningMemcpyNoMagic", 151),
          ("warningMemcpyTooLarge", 150),
          ("warningMemcpyWrongMagic", 152),
          ("warningMismatchCountFilterList", 383),
          ("warningModemTxChannelRecovered", 4100),
          ("warningModemTxChannelStuck", 4000),
          ("warningNewCallNoDiscRequest", 182),
          ("warningNewCallNoDiscResp", 183),
          ("warningNoCountInFilterList", 382),
          ("warningNoTimers", 140),
          ("warningOspfFatal", 200),
          ("warningOspfWarn", 201),
          ("warningPrimaryHWsetupFailed", 2100),
          ("warningSTACDataNotOwned", 171),
          ("warningSTACTimeout", 170),
          ("warningSauthBadAddr", 321),
          ("warningSauthWrongInfo", 320),
          ("warningSecondaryHWsetupFailed", 2101),
          ("warningSpyderBuffer", 185),
          ("warningSpyderDesc", 186),
          ("warningSpyderLoseChannel", 187),
          ("warningTacacsplusBase", 300),
          ("warningTacacsplusIndexInconsistency", 302),
          ("warningTacacsplusMax", 309),
          ("warningTacacsplusPointerInconsistency", 301),
          ("warningTacacsplusSocketMismatch", 305),
          ("warningTacacsplusTcpInconsistency", 303),
          ("warningTacacsplusTcpOutofrangesocket", 304),
          ("warningTacacsplusUnexpectedAuthState", 306),
          ("warningTcpBadOptions", 194),
          ("warningTcpSbcontTooBig", 190),
          ("warningTcpSequenceGap", 191),
          ("warningTcpTooMuchData", 192),
          ("warningTcpTooMuchWrite", 193),
          ("warningTcpXmitLooping", 198),
          ("warningTelnetFreeDrv", 165),
          ("warningTermSrvSemaphore", 161),
          ("warningTermSrvState", 160),
          ("warningUnalignedAccess", 800),
          ("warningUnexpected", 179),
          ("warningUnexpectedIF", 136),
          ("warningWANBufferLeak", 154))
    )


_SysLastRestartReason_Type.__name__ = "Integer32"
_SysLastRestartReason_Object = MibScalar
sysLastRestartReason = _SysLastRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 13),
    _SysLastRestartReason_Type()
)
sysLastRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLastRestartReason.setStatus("mandatory")
_SysConfigChange_Type = DisplayString
_SysConfigChange_Object = MibScalar
sysConfigChange = _SysConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 14),
    _SysConfigChange_Type()
)
sysConfigChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigChange.setStatus("mandatory")
_SysConfigFlash_ObjectIdentity = ObjectIdentity
sysConfigFlash = _SysConfigFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 9, 15)
)


class _SysConfigFlashCmd_Type(Integer32):
    """Custom type sysConfigFlashCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copyInternalToPCMCIA", 2),
          ("copyPCMCIAtoInternal", 1))
    )


_SysConfigFlashCmd_Type.__name__ = "Integer32"
_SysConfigFlashCmd_Object = MibScalar
sysConfigFlashCmd = _SysConfigFlashCmd_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 15, 1),
    _SysConfigFlashCmd_Type()
)
sysConfigFlashCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigFlashCmd.setStatus("mandatory")


class _SysConfigFlashCopyStatus_Type(Integer32):
    """Custom type sysConfigFlashCopyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("inProgress", 2),
          ("ok", 1))
    )


_SysConfigFlashCopyStatus_Type.__name__ = "Integer32"
_SysConfigFlashCopyStatus_Object = MibScalar
sysConfigFlashCopyStatus = _SysConfigFlashCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 15, 2),
    _SysConfigFlashCopyStatus_Type()
)
sysConfigFlashCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigFlashCopyStatus.setStatus("mandatory")
_SysConfigInternalFlashImageVersion_Type = DisplayString
_SysConfigInternalFlashImageVersion_Object = MibScalar
sysConfigInternalFlashImageVersion = _SysConfigInternalFlashImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 15, 3),
    _SysConfigInternalFlashImageVersion_Type()
)
sysConfigInternalFlashImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigInternalFlashImageVersion.setStatus("mandatory")
_SysConfigPCMCIAFlashImageVersion_Type = DisplayString
_SysConfigPCMCIAFlashImageVersion_Object = MibScalar
sysConfigPCMCIAFlashImageVersion = _SysConfigPCMCIAFlashImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 15, 4),
    _SysConfigPCMCIAFlashImageVersion_Type()
)
sysConfigPCMCIAFlashImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigPCMCIAFlashImageVersion.setStatus("mandatory")
_FatalLogTable_Object = MibTable
fatalLogTable = _FatalLogTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 16)
)
if mibBuilder.loadTexts:
    fatalLogTable.setStatus("mandatory")
_FatalLogTableEntry_Object = MibTableRow
fatalLogTableEntry = _FatalLogTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 16, 1)
)
fatalLogTableEntry.setIndexNames(
    (0, "ASCEND-MIB", "fatalLogIndex"),
)
if mibBuilder.loadTexts:
    fatalLogTableEntry.setStatus("mandatory")
_FatalLogIndex_Type = Integer32
_FatalLogIndex_Object = MibTableColumn
fatalLogIndex = _FatalLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 16, 1, 1),
    _FatalLogIndex_Type()
)
fatalLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fatalLogIndex.setStatus("mandatory")
_FatalLogSlotIndex_Type = Integer32
_FatalLogSlotIndex_Object = MibTableColumn
fatalLogSlotIndex = _FatalLogSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 16, 1, 2),
    _FatalLogSlotIndex_Type()
)
fatalLogSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fatalLogSlotIndex.setStatus("mandatory")
_FatalLogSoftwareVerion_Type = DisplayString
_FatalLogSoftwareVerion_Object = MibTableColumn
fatalLogSoftwareVerion = _FatalLogSoftwareVerion_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 16, 1, 3),
    _FatalLogSoftwareVerion_Type()
)
fatalLogSoftwareVerion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fatalLogSoftwareVerion.setStatus("mandatory")
_FatalLogUserprofile_Type = DisplayString
_FatalLogUserprofile_Object = MibTableColumn
fatalLogUserprofile = _FatalLogUserprofile_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 16, 1, 4),
    _FatalLogUserprofile_Type()
)
fatalLogUserprofile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fatalLogUserprofile.setStatus("mandatory")
_FatalLogLoadName_Type = DisplayString
_FatalLogLoadName_Object = MibTableColumn
fatalLogLoadName = _FatalLogLoadName_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 16, 1, 5),
    _FatalLogLoadName_Type()
)
fatalLogLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fatalLogLoadName.setStatus("mandatory")
_FatalLogLocation_Type = DisplayString
_FatalLogLocation_Object = MibTableColumn
fatalLogLocation = _FatalLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 16, 1, 6),
    _FatalLogLocation_Type()
)
fatalLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fatalLogLocation.setStatus("mandatory")


class _FatalLogReason_Type(Integer32):
    """Custom type fatalLogReason based on Integer32"""
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
              24,
              25,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              55,
              60,
              61,
              62,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              129,
              130,
              131,
              135,
              136,
              140,
              145,
              146,
              150,
              151,
              152,
              153,
              154,
              160,
              161,
              165,
              170,
              171,
              175,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              200,
              201,
              210,
              211,
              220,
              221,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              309,
              310,
              311,
              312,
              313,
              314,
              320,
              321,
              330,
              381,
              382,
              383,
              384,
              385,
              400,
              512,
              550,
              767,
              768,
              800,
              801,
              999,
              1001,
              1002,
              1003,
              1005,
              1006,
              1007,
              2001,
              2002,
              2010,
              2022,
              2100,
              2101,
              3001,
              3002,
              3003,
              4000,
              4100,
              9998,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("errprPPPAsuncBufferInUse", 130),
          ("fataExecNoTimerPool", 14),
          ("fatalATMSVC", 46),
          ("fatalAssert", 1),
          ("fatalBadPower", 60),
          ("fatalClipping", 41),
          ("fatalDDDDead", 21),
          ("fatalDDDProtocolError", 22),
          ("fatalDRAMCard", 37),
          ("fatalDspDead", 16),
          ("fatalDspInternalError", 18),
          ("fatalDspLossOfSync", 19),
          ("fatalDspProtocolError", 17),
          ("fatalDspUnUsed", 20),
          ("fatalExcessPostCompl", 43),
          ("fatalExecInvalidSwitch", 9),
          ("fatalExecNoMailDesc", 10),
          ("fatalExecNoMailPoll", 11),
          ("fatalExecNoTask", 12),
          ("fatalExecNoTimer", 13),
          ("fatalExecRestricted", 35),
          ("fatalExecWaitInCtricalSection", 15),
          ("fatalFRSVC", 47),
          ("fatalIDECTimeout", 34),
          ("fatalInterruptCode", 48),
          ("fatalIsacTimeout", 7),
          ("fatalLcdError", 6),
          ("fatalLif", 5),
          ("fatalLinkedListCorruption", 55),
          ("fatalMbufPanic", 38),
          ("fatalMemcoyBadStart", 33),
          ("fatalMemcpyNoMagic", 31),
          ("fatalMemcpyTooLarge", 30),
          ("fatalMemcpyWrongMagic", 32),
          ("fatalNegativeMemoryAllocate", 28),
          ("fatalNoPriority2Task", 39),
          ("fatalOperatorReset", 99),
          ("fatalPoolsNoBuffer", 2),
          ("fatalPrimarySelected", 98),
          ("fatalProfileBad", 3),
          ("fatalProtectionFault", 40),
          ("fatalPureVirtual", 45),
          ("fatalReadyHangFault", 42),
          ("fatalSCCSpuriousInterrupt", 8),
          ("fatalStackOverflow", 36),
          ("fatalSwitchTypeBad", 4),
          ("fatalSystemUp", 100),
          ("fatalTaskLoop", 29),
          ("fatalUnexplainedNMI", 62),
          ("fatalWatchdogTimeout", 61),
          ("fatalWriteProtect", 44),
          ("fatalX25Buffers", 23),
          ("fatalX25Init", 24),
          ("fatalX25Stack", 25),
          ("fatalZeroMemoryAlloc", 27),
          ("infoCardBounced", 220),
          ("infoCardDown", 221),
          ("infoSystemResetOccurred", 385),
          ("notApplicable", 9998),
          ("unknown", 9999),
          ("warningBadChunk", 135),
          ("warningBadPowerSupply", 400),
          ("warningBaeepromChange", 2001),
          ("warningBaeepromImageMismatch", 2002),
          ("warningBriJumperConfiguration", 211),
          ("warningBriJumperNotPresent", 210),
          ("warningBufferBadMemAlloc", 105),
          ("warningBufferBogusHeap", 107),
          ("warningBufferBogusPool", 106),
          ("warningBufferBoundary", 110),
          ("warningBufferInUse", 101),
          ("warningBufferMemcpyMagic", 120),
          ("warningBufferMemcpyMagicNext", 121),
          ("warningBufferNegativeMemalloc", 108),
          ("warningBufferNoExtraDRAM", 129),
          ("warningBufferNotInUse", 119),
          ("warningBufferNotMemAlloc", 104),
          ("warningBufferNull", 112),
          ("warningBufferSegmentCountZero", 113),
          ("warningBufferTooBig", 111),
          ("warningBufferTrailerBuffer", 115),
          ("warningBufferTrailerLength", 116),
          ("warningBufferTrailerMagic", 114),
          ("warningBufferTrailerUserMagic", 117),
          ("warningBufferWriteAfterFree", 118),
          ("warningBufferWrongHeap", 103),
          ("warningBufferWrongPool", 102),
          ("warningBufferZeroMemalloc", 109),
          ("warningCdtUnprotectedAccess", 384),
          ("warningChannelDisplayStuck", 181),
          ("warningChannelMapStuck", 180),
          ("warningCidrBusy", 312),
          ("warningCidrDupDelete", 314),
          ("warningCidrNoMem", 311),
          ("warningCidrNonempty", 313),
          ("warningCidrWrongTree", 310),
          ("warningDisconnectRequestDropped", 184),
          ("warningDspCrashMax", 767),
          ("warningDspCrashMin", 512),
          ("warningDspWrongSlot", 768),
          ("warningEthernetAckFailure", 1002),
          ("warningEthernetCuActive", 1005),
          ("warningEthernetCuBusy", 1001),
          ("warningEthernetNoMACAddress", 1007),
          ("warningEthernetNoTxBuf", 550),
          ("warningEthernetReset", 1003),
          ("warningEthernetWaitScb", 1006),
          ("warningExecFailure", 175),
          ("warningExecNoMailbox", 177),
          ("warningExecNoResources", 178),
          ("warningExecRestricted", 999),
          ("warningFlashTypeBad", 2010),
          ("warningGdbProtectionFault", 330),
          ("warningH323NoResources", 801),
          ("warningHscxSlowRelay", 188),
          ("warningInFilterList", 381),
          ("warningIpcpIpLookup", 131),
          ("warningIpxsapFilterCountMismatch", 3003),
          ("warningIpxsapFilterCountZero", 3002),
          ("warningIpxsapFilterMagic", 3001),
          ("warningLCDAllocFailure", 145),
          ("warningLCDNonSense", 146),
          ("warningLmodDspDown", 196),
          ("warningLmodDspmodemDown", 197),
          ("warningLmodSlotDown", 195),
          ("warningMaxiopLoadFailure", 2022),
          ("warningMemcpyBadStart", 153),
          ("warningMemcpyNoMagic", 151),
          ("warningMemcpyTooLarge", 150),
          ("warningMemcpyWrongMagic", 152),
          ("warningMismatchCountFilterList", 383),
          ("warningModemTxChannelRecovered", 4100),
          ("warningModemTxChannelStuck", 4000),
          ("warningNewCallNoDiscRequest", 182),
          ("warningNewCallNoDiscResp", 183),
          ("warningNoCountInFilterList", 382),
          ("warningNoTimers", 140),
          ("warningOspfFatal", 200),
          ("warningOspfWarn", 201),
          ("warningPrimaryHWsetupFailed", 2100),
          ("warningSTACDataNotOwned", 171),
          ("warningSTACTimeout", 170),
          ("warningSauthBadAddr", 321),
          ("warningSauthWrongInfo", 320),
          ("warningSecondaryHWsetupFailed", 2101),
          ("warningSpyderBuffer", 185),
          ("warningSpyderDesc", 186),
          ("warningSpyderLoseChannel", 187),
          ("warningTacacsplusBase", 300),
          ("warningTacacsplusIndexInconsistency", 302),
          ("warningTacacsplusMax", 309),
          ("warningTacacsplusPointerInconsistency", 301),
          ("warningTacacsplusSocketMismatch", 305),
          ("warningTacacsplusTcpInconsistency", 303),
          ("warningTacacsplusTcpOutofrangesocket", 304),
          ("warningTacacsplusUnexpectedAuthState", 306),
          ("warningTcpBadOptions", 194),
          ("warningTcpSbcontTooBig", 190),
          ("warningTcpSequenceGap", 191),
          ("warningTcpTooMuchData", 192),
          ("warningTcpTooMuchWrite", 193),
          ("warningTcpXmitLooping", 198),
          ("warningTelnetFreeDrv", 165),
          ("warningTermSrvSemaphore", 161),
          ("warningTermSrvState", 160),
          ("warningUnalignedAccess", 800),
          ("warningUnexpected", 179),
          ("warningUnexpectedIF", 136),
          ("warningWANBufferLeak", 154))
    )


_FatalLogReason_Type.__name__ = "Integer32"
_FatalLogReason_Object = MibTableColumn
fatalLogReason = _FatalLogReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 16, 1, 7),
    _FatalLogReason_Type()
)
fatalLogReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fatalLogReason.setStatus("mandatory")


class _FatalLogAbsoluteTime_Type(Integer32):
    """Custom type fatalLogAbsoluteTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FatalLogAbsoluteTime_Type.__name__ = "Integer32"
_FatalLogAbsoluteTime_Object = MibTableColumn
fatalLogAbsoluteTime = _FatalLogAbsoluteTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 9, 16, 1, 8),
    _FatalLogAbsoluteTime_Type()
)
fatalLogAbsoluteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fatalLogAbsoluteTime.setStatus("mandatory")
_EventGroup_ObjectIdentity = ObjectIdentity
eventGroup = _EventGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 10)
)
_CallStatusGroup_ObjectIdentity = ObjectIdentity
callStatusGroup = _CallStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 11)
)
_SessionStatusGroup_ObjectIdentity = ObjectIdentity
sessionStatusGroup = _SessionStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 12)
)
_RadiusGroup_ObjectIdentity = ObjectIdentity
radiusGroup = _RadiusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 13)
)
_MCastGroup_ObjectIdentity = ObjectIdentity
mCastGroup = _MCastGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 14)
)
_LanModemGroup_ObjectIdentity = ObjectIdentity
lanModemGroup = _LanModemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 15)
)
_FirewallGroup_ObjectIdentity = ObjectIdentity
firewallGroup = _FirewallGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 16)
)
_WanDialoutPkt_ObjectIdentity = ObjectIdentity
wanDialoutPkt = _WanDialoutPkt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 17)
)
_PowerSupply_ObjectIdentity = ObjectIdentity
powerSupply = _PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 18)
)
_MultiShelf_ObjectIdentity = ObjectIdentity
multiShelf = _MultiShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 19)
)
_MiscGroup_ObjectIdentity = ObjectIdentity
miscGroup = _MiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 20)
)
_AsgGroup_ObjectIdentity = ObjectIdentity
asgGroup = _AsgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 21)
)
_FlashGroup_ObjectIdentity = ObjectIdentity
flashGroup = _FlashGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 22)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23)
)
_MibinternetProfile_ObjectIdentity = ObjectIdentity
mibinternetProfile = _MibinternetProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 1)
)
_MibframeRelayProfile_ObjectIdentity = ObjectIdentity
mibframeRelayProfile = _MibframeRelayProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 2)
)
_MibanswerProfile_ObjectIdentity = ObjectIdentity
mibanswerProfile = _MibanswerProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 3)
)
_MibdS3NetworkProfile_ObjectIdentity = ObjectIdentity
mibdS3NetworkProfile = _MibdS3NetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 4)
)
_Mibuds3NetworkProfile_ObjectIdentity = ObjectIdentity
mibuds3NetworkProfile = _Mibuds3NetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 5)
)
_MibcadslNetworkProfile_ObjectIdentity = ObjectIdentity
mibcadslNetworkProfile = _MibcadslNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 6)
)
_MibdadslNetworkProfile_ObjectIdentity = ObjectIdentity
mibdadslNetworkProfile = _MibdadslNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 7)
)
_MibsdslNetworkProfile_ObjectIdentity = ObjectIdentity
mibsdslNetworkProfile = _MibsdslNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 8)
)
_MibvdslNetworkProfile_ObjectIdentity = ObjectIdentity
mibvdslNetworkProfile = _MibvdslNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 9)
)
_MibdmtAlDslNetworkProfile_ObjectIdentity = ObjectIdentity
mibdmtAlDslNetworkProfile = _MibdmtAlDslNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 10)
)
_Miboc3AtmNetworkProfile_ObjectIdentity = ObjectIdentity
miboc3AtmNetworkProfile = _Miboc3AtmNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 11)
)
_MiblimSparingConfigProfile_ObjectIdentity = ObjectIdentity
miblimSparingConfigProfile = _MiblimSparingConfigProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 12)
)
_Mibds3AtmNetworkProfile_ObjectIdentity = ObjectIdentity
mibds3AtmNetworkProfile = _Mibds3AtmNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 13)
)
_Mibhdsl2NetworkProfile_ObjectIdentity = ObjectIdentity
mibhdsl2NetworkProfile = _Mibhdsl2NetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 14)
)
_Mibe3AtmNetworkProfile_ObjectIdentity = ObjectIdentity
mibe3AtmNetworkProfile = _Mibe3AtmNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 15)
)
_MibredundancyProfile_ObjectIdentity = ObjectIdentity
mibredundancyProfile = _MibredundancyProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 16)
)
_MibredundancyStatsProfile_ObjectIdentity = ObjectIdentity
mibredundancyStatsProfile = _MibredundancyStatsProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 17)
)
_AtmpGroup_ObjectIdentity = ObjectIdentity
atmpGroup = _AtmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 24)
)
_CallLoggingGroup_ObjectIdentity = ObjectIdentity
callLoggingGroup = _CallLoggingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 25)
)
_SrvcMgmtGroup_ObjectIdentity = ObjectIdentity
srvcMgmtGroup = _SrvcMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 26)
)
_ResourcesGroup_ObjectIdentity = ObjectIdentity
resourcesGroup = _ResourcesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 27)
)
_VoipGroup_ObjectIdentity = ObjectIdentity
voipGroup = _VoipGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 28)
)
_MgGroup_ObjectIdentity = ObjectIdentity
mgGroup = _MgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 29)
)
_SparingGroup_ObjectIdentity = ObjectIdentity
sparingGroup = _SparingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 30)
)
_CltmGroup_ObjectIdentity = ObjectIdentity
cltmGroup = _CltmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 31)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIB",
    **{"DisplayString": DisplayString,
       "ascend": ascend,
       "products": products,
       "multiband": multiband,
       "max": max,
       "max200": max200,
       "max1800": max1800,
       "max2000": max2000,
       "max4000": max4000,
       "max4002": max4002,
       "max4004": max4004,
       "max6000": max6000,
       "max800": max800,
       "max3000": max3000,
       "dslmax20": dslmax20,
       "terminator": terminator,
       "cvmax100": cvmax100,
       "pipeline": pipeline,
       "pipe15": pipe15,
       "pipe25": pipe25,
       "pipe25Px": pipe25Px,
       "pipe25Fx": pipe25Fx,
       "pipe50": pipe50,
       "pipe75": pipe75,
       "pipe130T1": pipe130T1,
       "pipe400": pipe400,
       "pipe220": pipe220,
       "dslPipeAcap": dslPipeAcap,
       "dslPipeS": dslPipeS,
       "dslPipe2S": dslPipe2S,
       "dslPipeAdslCoeC": dslPipeAdslCoeC,
       "dslPipeSdslCoe": dslPipeSdslCoe,
       "dslPipeSdslCoe2S": dslPipeSdslCoe2S,
       "pipe85": pipe85,
       "pipe50LS56": pipe50LS56,
       "pipe130V35": pipe130V35,
       "pipe130N56": pipe130N56,
       "dslPipeAdslCoeD": dslPipeAdslCoeD,
       "dslPipeAdmt": dslPipeAdmt,
       "dslPipeAlctlDmt": dslPipeAlctlDmt,
       "spipe95": spipe95,
       "spipe155T1": spipe155T1,
       "dslPipe50SdslCell": dslPipe50SdslCell,
       "dslPipeSdslHs": dslPipeSdslHs,
       "max-tnt": max_tnt,
       "dslTnt": dslTnt,
       "aqueduct": aqueduct,
       "aq300": aq300,
       "stinger-10": stinger_10,
       "apx-8000": apx_8000,
       "slots": slots,
       "hostTypes": hostTypes,
       "hostTypeAny": hostTypeAny,
       "hostTypeDual": hostTypeDual,
       "hostTypeQuad": hostTypeQuad,
       "hostTypeAim2": hostTypeAim2,
       "hostTypeAim6": hostTypeAim6,
       "advancedAgent": advancedAgent,
       "lanTypes": lanTypes,
       "lanTypeAny": lanTypeAny,
       "lanTypeEthernet": lanTypeEthernet,
       "lanTypeEtherData": lanTypeEtherData,
       "doGroup": doGroup,
       "doTable": doTable,
       "doEntry": doEntry,
       "doSlotIndex": doSlotIndex,
       "doItemIndex": doItemIndex,
       "doDial": doDial,
       "doHangUp": doHangUp,
       "doAnswer": doAnswer,
       "doExtendBW": doExtendBW,
       "doContractBW": doContractBW,
       "doBegEndRemoteLB": doBegEndRemoteLB,
       "doBegEndBERT": doBegEndBERT,
       "doResynchronize": doResynchronize,
       "hostStatus": hostStatus,
       "hostStatusTable": hostStatusTable,
       "hostStatusEntry": hostStatusEntry,
       "hostStatusSlotIndex": hostStatusSlotIndex,
       "hostStatusItemIndex": hostStatusItemIndex,
       "hostStatusLocalName": hostStatusLocalName,
       "hostStatusDialNum": hostStatusDialNum,
       "hostStatusCallType": hostStatusCallType,
       "hostStatusCallMgm": hostStatusCallMgm,
       "hostStatusDataSvc": hostStatusDataSvc,
       "hostStatusCallState": hostStatusCallState,
       "hostStatusRemName": hostStatusRemName,
       "hostStatusChannels": hostStatusChannels,
       "hostStatusDuration": hostStatusDuration,
       "console": console,
       "consoleNumber": consoleNumber,
       "consoleTable": consoleTable,
       "consoleEntry": consoleEntry,
       "consoleIndex": consoleIndex,
       "consoleIf": consoleIf,
       "consoleType": consoleType,
       "consoleSecurity": consoleSecurity,
       "consoleSpecific": consoleSpecific,
       "systemStatusGroup": systemStatusGroup,
       "sysAbsoluteStartupTime": sysAbsoluteStartupTime,
       "sysSecsSinceStartup": sysSecsSinceStartup,
       "sysMibVersionNum": sysMibVersionNum,
       "sysMibMinorRevNum": sysMibMinorRevNum,
       "sysConfigTftp": sysConfigTftp,
       "sysConfigTftpCmd": sysConfigTftpCmd,
       "sysConfigTftpStatus": sysConfigTftpStatus,
       "sysConfigTftpHostAddr": sysConfigTftpHostAddr,
       "sysConfigTftpFilename": sysConfigTftpFilename,
       "sysConfigTftpPort": sysConfigTftpPort,
       "sysConfigTftpParameter": sysConfigTftpParameter,
       "sysConfigRadius": sysConfigRadius,
       "sysConfigRadiusCmd": sysConfigRadiusCmd,
       "sysConfigRadiusStatus": sysConfigRadiusStatus,
       "sysAbsoluteCurrentTime": sysAbsoluteCurrentTime,
       "sysReset": sysReset,
       "sysLoadName": sysLoadName,
       "sysAuthPreference": sysAuthPreference,
       "sysSPROM": sysSPROM,
       "sysSPROMSerialNumber": sysSPROMSerialNumber,
       "sysSPROMOptions1": sysSPROMOptions1,
       "sysSPROMOptions2": sysSPROMOptions2,
       "sysSPROMCountries1": sysSPROMCountries1,
       "resetStat": resetStat,
       "resetStatEther": resetStatEther,
       "resetStatWAN": resetStatWAN,
       "resetStatAll": resetStatAll,
       "sysLastRestartReason": sysLastRestartReason,
       "sysConfigChange": sysConfigChange,
       "sysConfigFlash": sysConfigFlash,
       "sysConfigFlashCmd": sysConfigFlashCmd,
       "sysConfigFlashCopyStatus": sysConfigFlashCopyStatus,
       "sysConfigInternalFlashImageVersion": sysConfigInternalFlashImageVersion,
       "sysConfigPCMCIAFlashImageVersion": sysConfigPCMCIAFlashImageVersion,
       "fatalLogTable": fatalLogTable,
       "fatalLogTableEntry": fatalLogTableEntry,
       "fatalLogIndex": fatalLogIndex,
       "fatalLogSlotIndex": fatalLogSlotIndex,
       "fatalLogSoftwareVerion": fatalLogSoftwareVerion,
       "fatalLogUserprofile": fatalLogUserprofile,
       "fatalLogLoadName": fatalLogLoadName,
       "fatalLogLocation": fatalLogLocation,
       "fatalLogReason": fatalLogReason,
       "fatalLogAbsoluteTime": fatalLogAbsoluteTime,
       "eventGroup": eventGroup,
       "callStatusGroup": callStatusGroup,
       "sessionStatusGroup": sessionStatusGroup,
       "radiusGroup": radiusGroup,
       "mCastGroup": mCastGroup,
       "lanModemGroup": lanModemGroup,
       "firewallGroup": firewallGroup,
       "wanDialoutPkt": wanDialoutPkt,
       "powerSupply": powerSupply,
       "multiShelf": multiShelf,
       "miscGroup": miscGroup,
       "asgGroup": asgGroup,
       "flashGroup": flashGroup,
       "configuration": configuration,
       "mibinternetProfile": mibinternetProfile,
       "mibframeRelayProfile": mibframeRelayProfile,
       "mibanswerProfile": mibanswerProfile,
       "mibdS3NetworkProfile": mibdS3NetworkProfile,
       "mibuds3NetworkProfile": mibuds3NetworkProfile,
       "mibcadslNetworkProfile": mibcadslNetworkProfile,
       "mibdadslNetworkProfile": mibdadslNetworkProfile,
       "mibsdslNetworkProfile": mibsdslNetworkProfile,
       "mibvdslNetworkProfile": mibvdslNetworkProfile,
       "mibdmtAlDslNetworkProfile": mibdmtAlDslNetworkProfile,
       "miboc3AtmNetworkProfile": miboc3AtmNetworkProfile,
       "miblimSparingConfigProfile": miblimSparingConfigProfile,
       "mibds3AtmNetworkProfile": mibds3AtmNetworkProfile,
       "mibhdsl2NetworkProfile": mibhdsl2NetworkProfile,
       "mibe3AtmNetworkProfile": mibe3AtmNetworkProfile,
       "mibredundancyProfile": mibredundancyProfile,
       "mibredundancyStatsProfile": mibredundancyStatsProfile,
       "atmpGroup": atmpGroup,
       "callLoggingGroup": callLoggingGroup,
       "srvcMgmtGroup": srvcMgmtGroup,
       "resourcesGroup": resourcesGroup,
       "voipGroup": voipGroup,
       "mgGroup": mgGroup,
       "sparingGroup": sparingGroup,
       "cltmGroup": cltmGroup}
)
