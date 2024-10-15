# SNMP MIB module (XYLOGICS-ANNEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLOGICS-ANNEX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:37 2024
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

_Xylogics_ObjectIdentity = ObjectIdentity
xylogics = _Xylogics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 1)
)
_Prodannex_Type = OctetString
_Prodannex_Object = MibScalar
prodannex = _Prodannex_Object(
    (1, 3, 6, 1, 4, 1, 15, 1, 1),
    _Prodannex_Type()
)
prodannex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodannex.setStatus("mandatory")
_Annex_ObjectIdentity = ObjectIdentity
annex = _Annex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2)
)
_Hw_ObjectIdentity = ObjectIdentity
hw = _Hw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 1)
)


class _HwType_Type(Integer32):
    """Custom type hwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              16,
              23,
              42,
              52)
        )
    )
    namedValues = NamedValues(
        *(("annex3", 42),
          ("annexI", 11),
          ("annexII", 16),
          ("annexX25", 23),
          ("err", 1),
          ("microannex", 52))
    )


_HwType_Type.__name__ = "Integer32"
_HwType_Object = MibScalar
hwType = _HwType_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 1, 1),
    _HwType_Type()
)
hwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwType.setStatus("mandatory")
_HwRev_Type = OctetString
_HwRev_Object = MibScalar
hwRev = _HwRev_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 1, 2),
    _HwRev_Type()
)
hwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRev.setStatus("mandatory")
_RomRev_Type = OctetString
_RomRev_Object = MibScalar
romRev = _RomRev_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 1, 3),
    _RomRev_Type()
)
romRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    romRev.setStatus("mandatory")
_SerialNumber_Type = Integer32
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 1, 4),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")
_MemorySize_Type = Integer32
_MemorySize_Object = MibScalar
memorySize = _MemorySize_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 1, 5),
    _MemorySize_Type()
)
memorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memorySize.setStatus("mandatory")
_Sw_ObjectIdentity = ObjectIdentity
sw = _Sw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 2)
)


class _SwType_Type(Integer32):
    """Custom type swType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              13,
              16,
              17,
              23,
              42,
              43,
              52)
        )
    )
    namedValues = NamedValues(
        *(("annex3mx", 43),
          ("annex3ux", 42),
          ("annexIImx", 16),
          ("annexIIux", 17),
          ("annexImx", 11),
          ("annexIux", 13),
          ("annexX25", 23),
          ("err", 1),
          ("microannexux", 52))
    )


_SwType_Type.__name__ = "Integer32"
_SwType_Object = MibScalar
swType = _SwType_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 1),
    _SwType_Type()
)
swType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swType.setStatus("mandatory")
_SwRevMajor_Type = Integer32
_SwRevMajor_Object = MibScalar
swRevMajor = _SwRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 2),
    _SwRevMajor_Type()
)
swRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRevMajor.setStatus("mandatory")
_SwRevMinor_Type = Integer32
_SwRevMinor_Object = MibScalar
swRevMinor = _SwRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 3),
    _SwRevMinor_Type()
)
swRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRevMinor.setStatus("mandatory")
_SwBuild_Type = OctetString
_SwBuild_Object = MibScalar
swBuild = _SwBuild_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 4),
    _SwBuild_Type()
)
swBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBuild.setStatus("mandatory")
_ImageName_Type = OctetString
_ImageName_Object = MibScalar
imageName = _ImageName_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 5),
    _ImageName_Type()
)
imageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageName.setStatus("mandatory")
_BootHost_Type = IpAddress
_BootHost_Object = MibScalar
bootHost = _BootHost_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 6),
    _BootHost_Type()
)
bootHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootHost.setStatus("mandatory")
_DefaultDomain_Type = OctetString
_DefaultDomain_Object = MibScalar
defaultDomain = _DefaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 7),
    _DefaultDomain_Type()
)
defaultDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultDomain.setStatus("mandatory")
_CurrentDate_Type = OctetString
_CurrentDate_Object = MibScalar
currentDate = _CurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 8),
    _CurrentDate_Type()
)
currentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDate.setStatus("mandatory")
_UsableMemory_Type = Integer32
_UsableMemory_Object = MibScalar
usableMemory = _UsableMemory_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 9),
    _UsableMemory_Type()
)
usableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usableMemory.setStatus("mandatory")
_FreeMemory_Type = Gauge32
_FreeMemory_Object = MibScalar
freeMemory = _FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 10),
    _FreeMemory_Type()
)
freeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMemory.setStatus("mandatory")
_MinFreeMemory_Type = Integer32
_MinFreeMemory_Object = MibScalar
minFreeMemory = _MinFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 11),
    _MinFreeMemory_Type()
)
minFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minFreeMemory.setStatus("mandatory")
_CpuUtilization_Type = Gauge32
_CpuUtilization_Object = MibScalar
cpuUtilization = _CpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 12),
    _CpuUtilization_Type()
)
cpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilization.setStatus("mandatory")
_MaxProcs_Type = Integer32
_MaxProcs_Object = MibScalar
maxProcs = _MaxProcs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 13),
    _MaxProcs_Type()
)
maxProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxProcs.setStatus("mandatory")
_MostProcs_Type = Integer32
_MostProcs_Object = MibScalar
mostProcs = _MostProcs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 14),
    _MostProcs_Type()
)
mostProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mostProcs.setStatus("mandatory")
_ActiveProcs_Type = Gauge32
_ActiveProcs_Object = MibScalar
activeProcs = _ActiveProcs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 15),
    _ActiveProcs_Type()
)
activeProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeProcs.setStatus("mandatory")
_CpuReschedsI_Type = Gauge32
_CpuReschedsI_Object = MibScalar
cpuReschedsI = _CpuReschedsI_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 16),
    _CpuReschedsI_Type()
)
cpuReschedsI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuReschedsI.setStatus("mandatory")
_CpuReschedsT_Type = Counter32
_CpuReschedsT_Object = MibScalar
cpuReschedsT = _CpuReschedsT_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 17),
    _CpuReschedsT_Type()
)
cpuReschedsT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuReschedsT.setStatus("mandatory")
_ContextSwI_Type = Gauge32
_ContextSwI_Object = MibScalar
contextSwI = _ContextSwI_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 18),
    _ContextSwI_Type()
)
contextSwI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contextSwI.setStatus("mandatory")
_ContextSwT_Type = Counter32
_ContextSwT_Object = MibScalar
contextSwT = _ContextSwT_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 19),
    _ContextSwT_Type()
)
contextSwT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contextSwT.setStatus("mandatory")
_CpuActivatesI_Type = Gauge32
_CpuActivatesI_Object = MibScalar
cpuActivatesI = _CpuActivatesI_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 20),
    _CpuActivatesI_Type()
)
cpuActivatesI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuActivatesI.setStatus("mandatory")
_CpuActivatesT_Type = Counter32
_CpuActivatesT_Object = MibScalar
cpuActivatesT = _CpuActivatesT_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 21),
    _CpuActivatesT_Type()
)
cpuActivatesT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuActivatesT.setStatus("mandatory")
_CBlocksTotal_Type = Integer32
_CBlocksTotal_Object = MibScalar
cBlocksTotal = _CBlocksTotal_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 22),
    _CBlocksTotal_Type()
)
cBlocksTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBlocksTotal.setStatus("mandatory")
_CBlocksFree_Type = Integer32
_CBlocksFree_Object = MibScalar
cBlocksFree = _CBlocksFree_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 23),
    _CBlocksFree_Type()
)
cBlocksFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBlocksFree.setStatus("mandatory")
_CBlocksMinFree_Type = Integer32
_CBlocksMinFree_Object = MibScalar
cBlocksMinFree = _CBlocksMinFree_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 24),
    _CBlocksMinFree_Type()
)
cBlocksMinFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBlocksMinFree.setStatus("mandatory")
_CBlocksDenied_Type = Counter32
_CBlocksDenied_Object = MibScalar
cBlocksDenied = _CBlocksDenied_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 25),
    _CBlocksDenied_Type()
)
cBlocksDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBlocksDenied.setStatus("mandatory")
_MaxCallouts_Type = Integer32
_MaxCallouts_Object = MibScalar
maxCallouts = _MaxCallouts_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 26),
    _MaxCallouts_Type()
)
maxCallouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxCallouts.setStatus("mandatory")
_LeastCallouts_Type = Integer32
_LeastCallouts_Object = MibScalar
leastCallouts = _LeastCallouts_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 27),
    _LeastCallouts_Type()
)
leastCallouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leastCallouts.setStatus("mandatory")
_FreeCallouts_Type = Gauge32
_FreeCallouts_Object = MibScalar
freeCallouts = _FreeCallouts_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 28),
    _FreeCallouts_Type()
)
freeCallouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeCallouts.setStatus("mandatory")
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 3)
)
_TotalPorts_Type = Integer32
_TotalPorts_Object = MibScalar
totalPorts = _TotalPorts_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 1),
    _TotalPorts_Type()
)
totalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPorts.setStatus("mandatory")
_TotalCharsIn_Type = Counter32
_TotalCharsIn_Object = MibScalar
totalCharsIn = _TotalCharsIn_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 2),
    _TotalCharsIn_Type()
)
totalCharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCharsIn.setStatus("mandatory")
_TotalCharsOut_Type = Counter32
_TotalCharsOut_Object = MibScalar
totalCharsOut = _TotalCharsOut_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 3),
    _TotalCharsOut_Type()
)
totalCharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCharsOut.setStatus("mandatory")
_TotalErrsParity_Type = Counter32
_TotalErrsParity_Object = MibScalar
totalErrsParity = _TotalErrsParity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 4),
    _TotalErrsParity_Type()
)
totalErrsParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalErrsParity.setStatus("mandatory")
_TotalErrsOverrun_Type = Counter32
_TotalErrsOverrun_Object = MibScalar
totalErrsOverrun = _TotalErrsOverrun_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 5),
    _TotalErrsOverrun_Type()
)
totalErrsOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalErrsOverrun.setStatus("mandatory")
_TotalErrsFraming_Type = Counter32
_TotalErrsFraming_Object = MibScalar
totalErrsFraming = _TotalErrsFraming_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 6),
    _TotalErrsFraming_Type()
)
totalErrsFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalErrsFraming.setStatus("mandatory")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")
_ISpeed_Type = Integer32
_ISpeed_Object = MibTableColumn
iSpeed = _ISpeed_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 2),
    _ISpeed_Type()
)
iSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSpeed.setStatus("mandatory")
_OSpeed_Type = Integer32
_OSpeed_Object = MibTableColumn
oSpeed = _OSpeed_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 3),
    _OSpeed_Type()
)
oSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oSpeed.setStatus("mandatory")


class _CtrlLines_Type(Integer32):
    """Custom type ctrlLines based on Integer32"""
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
        *(("both", 4),
          ("ctsrts", 3),
          ("dcddtr", 2),
          ("none", 1))
    )


_CtrlLines_Type.__name__ = "Integer32"
_CtrlLines_Object = MibTableColumn
ctrlLines = _CtrlLines_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 4),
    _CtrlLines_Type()
)
ctrlLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlLines.setStatus("mandatory")


class _FlowTypeIn_Type(Integer32):
    """Custom type flowTypeIn based on Integer32"""
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
        *(("bell", 4),
          ("eia", 3),
          ("none", 1),
          ("xonxoff", 2))
    )


_FlowTypeIn_Type.__name__ = "Integer32"
_FlowTypeIn_Object = MibTableColumn
flowTypeIn = _FlowTypeIn_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 5),
    _FlowTypeIn_Type()
)
flowTypeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowTypeIn.setStatus("mandatory")


class _FlowTypeOut_Type(Integer32):
    """Custom type flowTypeOut based on Integer32"""
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
        *(("bell", 4),
          ("eia", 3),
          ("none", 1),
          ("xonxoff", 2))
    )


_FlowTypeOut_Type.__name__ = "Integer32"
_FlowTypeOut_Object = MibTableColumn
flowTypeOut = _FlowTypeOut_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 6),
    _FlowTypeOut_Type()
)
flowTypeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowTypeOut.setStatus("mandatory")


class _BitsPerChar_Type(Integer32):
    """Custom type bitsPerChar based on Integer32"""
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
        *(("eight", 4),
          ("five", 1),
          ("seven", 3),
          ("six", 2))
    )


_BitsPerChar_Type.__name__ = "Integer32"
_BitsPerChar_Object = MibTableColumn
bitsPerChar = _BitsPerChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 7),
    _BitsPerChar_Type()
)
bitsPerChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitsPerChar.setStatus("mandatory")


class _StopBits_Type(Integer32):
    """Custom type stopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("onefive", 2),
          ("two", 3))
    )


_StopBits_Type.__name__ = "Integer32"
_StopBits_Object = MibTableColumn
stopBits = _StopBits_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 8),
    _StopBits_Type()
)
stopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stopBits.setStatus("mandatory")


class _Parity_Type(Integer32):
    """Custom type parity based on Integer32"""
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
        *(("even", 2),
          ("mark", 4),
          ("none", 1),
          ("odd", 3),
          ("space", 5))
    )


_Parity_Type.__name__ = "Integer32"
_Parity_Object = MibTableColumn
parity = _Parity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 9),
    _Parity_Type()
)
parity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parity.setStatus("mandatory")


class _ModemDCD_Type(Integer32):
    """Custom type modemDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hi", 3),
          ("lo", 2),
          ("unused", 1))
    )


_ModemDCD_Type.__name__ = "Integer32"
_ModemDCD_Object = MibTableColumn
modemDCD = _ModemDCD_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 10),
    _ModemDCD_Type()
)
modemDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemDCD.setStatus("mandatory")


class _ModemDTR_Type(Integer32):
    """Custom type modemDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hi", 3),
          ("lo", 2),
          ("unused", 1))
    )


_ModemDTR_Type.__name__ = "Integer32"
_ModemDTR_Object = MibTableColumn
modemDTR = _ModemDTR_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 11),
    _ModemDTR_Type()
)
modemDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemDTR.setStatus("mandatory")


class _ModemCTS_Type(Integer32):
    """Custom type modemCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hi", 3),
          ("lo", 2),
          ("unused", 1))
    )


_ModemCTS_Type.__name__ = "Integer32"
_ModemCTS_Object = MibTableColumn
modemCTS = _ModemCTS_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 12),
    _ModemCTS_Type()
)
modemCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCTS.setStatus("mandatory")


class _ModemRTS_Type(Integer32):
    """Custom type modemRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hi", 3),
          ("lo", 2),
          ("unused", 1))
    )


_ModemRTS_Type.__name__ = "Integer32"
_ModemRTS_Object = MibTableColumn
modemRTS = _ModemRTS_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 13),
    _ModemRTS_Type()
)
modemRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemRTS.setStatus("mandatory")
_CharsIn_Type = Counter32
_CharsIn_Object = MibTableColumn
charsIn = _CharsIn_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 14),
    _CharsIn_Type()
)
charsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charsIn.setStatus("mandatory")
_CharsOut_Type = Counter32
_CharsOut_Object = MibTableColumn
charsOut = _CharsOut_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 15),
    _CharsOut_Type()
)
charsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charsOut.setStatus("mandatory")
_ErrsParity_Type = Counter32
_ErrsParity_Object = MibTableColumn
errsParity = _ErrsParity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 16),
    _ErrsParity_Type()
)
errsParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errsParity.setStatus("mandatory")
_ErrsOverrun_Type = Counter32
_ErrsOverrun_Object = MibTableColumn
errsOverrun = _ErrsOverrun_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 17),
    _ErrsOverrun_Type()
)
errsOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errsOverrun.setStatus("mandatory")
_ErrsFraming_Type = Counter32
_ErrsFraming_Object = MibTableColumn
errsFraming = _ErrsFraming_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 18),
    _ErrsFraming_Type()
)
errsFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errsFraming.setStatus("mandatory")
_InCC_Type = Gauge32
_InCC_Object = MibTableColumn
inCC = _InCC_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 19),
    _InCC_Type()
)
inCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inCC.setStatus("mandatory")
_OutCC_Type = Gauge32
_OutCC_Object = MibTableColumn
outCC = _OutCC_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 20),
    _OutCC_Type()
)
outCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outCC.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLOGICS-ANNEX-MIB",
    **{"xylogics": xylogics,
       "prod": prod,
       "prodannex": prodannex,
       "annex": annex,
       "hw": hw,
       "hwType": hwType,
       "hwRev": hwRev,
       "romRev": romRev,
       "serialNumber": serialNumber,
       "memorySize": memorySize,
       "sw": sw,
       "swType": swType,
       "swRevMajor": swRevMajor,
       "swRevMinor": swRevMinor,
       "swBuild": swBuild,
       "imageName": imageName,
       "bootHost": bootHost,
       "defaultDomain": defaultDomain,
       "currentDate": currentDate,
       "usableMemory": usableMemory,
       "freeMemory": freeMemory,
       "minFreeMemory": minFreeMemory,
       "cpuUtilization": cpuUtilization,
       "maxProcs": maxProcs,
       "mostProcs": mostProcs,
       "activeProcs": activeProcs,
       "cpuReschedsI": cpuReschedsI,
       "cpuReschedsT": cpuReschedsT,
       "contextSwI": contextSwI,
       "contextSwT": contextSwT,
       "cpuActivatesI": cpuActivatesI,
       "cpuActivatesT": cpuActivatesT,
       "cBlocksTotal": cBlocksTotal,
       "cBlocksFree": cBlocksFree,
       "cBlocksMinFree": cBlocksMinFree,
       "cBlocksDenied": cBlocksDenied,
       "maxCallouts": maxCallouts,
       "leastCallouts": leastCallouts,
       "freeCallouts": freeCallouts,
       "ports": ports,
       "totalPorts": totalPorts,
       "totalCharsIn": totalCharsIn,
       "totalCharsOut": totalCharsOut,
       "totalErrsParity": totalErrsParity,
       "totalErrsOverrun": totalErrsOverrun,
       "totalErrsFraming": totalErrsFraming,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "iSpeed": iSpeed,
       "oSpeed": oSpeed,
       "ctrlLines": ctrlLines,
       "flowTypeIn": flowTypeIn,
       "flowTypeOut": flowTypeOut,
       "bitsPerChar": bitsPerChar,
       "stopBits": stopBits,
       "parity": parity,
       "modemDCD": modemDCD,
       "modemDTR": modemDTR,
       "modemCTS": modemCTS,
       "modemRTS": modemRTS,
       "charsIn": charsIn,
       "charsOut": charsOut,
       "errsParity": errsParity,
       "errsOverrun": errsOverrun,
       "errsFraming": errsFraming,
       "inCC": inCC,
       "outCC": outCC}
)
