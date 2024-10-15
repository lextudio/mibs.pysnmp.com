# SNMP MIB module (ANNEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANNEX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:54 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
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


class _Prodannex_Type(DisplayString):
    """Custom type prodannex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Prodannex_Type.__name__ = "DisplayString"
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
              16,
              42,
              52,
              55)
        )
    )
    namedValues = NamedValues(
        *(("annex3", 42),
          ("annexII", 16),
          ("err", 1),
          ("microannex", 52),
          ("microels", 55))
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


class _HwRev_Type(DisplayString):
    """Custom type hwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwRev_Type.__name__ = "DisplayString"
_HwRev_Object = MibScalar
hwRev = _HwRev_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 1, 2),
    _HwRev_Type()
)
hwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRev.setStatus("mandatory")


class _RomRev_Type(DisplayString):
    """Custom type romRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RomRev_Type.__name__ = "DisplayString"
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
              16,
              17,
              42,
              43,
              52,
              53,
              55)
        )
    )
    namedValues = NamedValues(
        *(("annex3mx", 43),
          ("annex3ux", 42),
          ("annexIImx", 16),
          ("annexIIux", 17),
          ("err", 1),
          ("microannexmx", 53),
          ("microannexux", 52),
          ("microels", 55))
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


class _SwBuild_Type(DisplayString):
    """Custom type swBuild based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwBuild_Type.__name__ = "DisplayString"
_SwBuild_Object = MibScalar
swBuild = _SwBuild_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 4),
    _SwBuild_Type()
)
swBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBuild.setStatus("mandatory")


class _ImageName_Type(DisplayString):
    """Custom type imageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_ImageName_Type.__name__ = "DisplayString"
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


class _DefaultDomain_Type(DisplayString):
    """Custom type defaultDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DefaultDomain_Type.__name__ = "DisplayString"
_DefaultDomain_Object = MibScalar
defaultDomain = _DefaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 7),
    _DefaultDomain_Type()
)
defaultDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultDomain.setStatus("mandatory")


class _CurrentDate_Type(DisplayString):
    """Custom type currentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CurrentDate_Type.__name__ = "DisplayString"
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
_CpuIRescheds_Type = Gauge32
_CpuIRescheds_Object = MibScalar
cpuIRescheds = _CpuIRescheds_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 16),
    _CpuIRescheds_Type()
)
cpuIRescheds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIRescheds.setStatus("mandatory")
_CpuTRescheds_Type = Counter32
_CpuTRescheds_Object = MibScalar
cpuTRescheds = _CpuTRescheds_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 17),
    _CpuTRescheds_Type()
)
cpuTRescheds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTRescheds.setStatus("mandatory")
_ContextISwtchs_Type = Gauge32
_ContextISwtchs_Object = MibScalar
contextISwtchs = _ContextISwtchs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 18),
    _ContextISwtchs_Type()
)
contextISwtchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contextISwtchs.setStatus("mandatory")
_ContextTSwtchs_Type = Counter32
_ContextTSwtchs_Object = MibScalar
contextTSwtchs = _ContextTSwtchs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 19),
    _ContextTSwtchs_Type()
)
contextTSwtchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contextTSwtchs.setStatus("mandatory")
_CpuIActivates_Type = Gauge32
_CpuIActivates_Object = MibScalar
cpuIActivates = _CpuIActivates_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 20),
    _CpuIActivates_Type()
)
cpuIActivates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIActivates.setStatus("mandatory")
_CpuTActivates_Type = Counter32
_CpuTActivates_Object = MibScalar
cpuTActivates = _CpuTActivates_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 21),
    _CpuTActivates_Type()
)
cpuTActivates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTActivates.setStatus("mandatory")
_MaxCallouts_Type = Integer32
_MaxCallouts_Object = MibScalar
maxCallouts = _MaxCallouts_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 22),
    _MaxCallouts_Type()
)
maxCallouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxCallouts.setStatus("mandatory")
_LeastCallouts_Type = Integer32
_LeastCallouts_Object = MibScalar
leastCallouts = _LeastCallouts_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 23),
    _LeastCallouts_Type()
)
leastCallouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leastCallouts.setStatus("mandatory")
_FreeCallouts_Type = Gauge32
_FreeCallouts_Object = MibScalar
freeCallouts = _FreeCallouts_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 2, 24),
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
_TotalInChars_Type = Counter32
_TotalInChars_Object = MibScalar
totalInChars = _TotalInChars_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 2),
    _TotalInChars_Type()
)
totalInChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInChars.setStatus("mandatory")
_TotalOutChars_Type = Counter32
_TotalOutChars_Object = MibScalar
totalOutChars = _TotalOutChars_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 3),
    _TotalOutChars_Type()
)
totalOutChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOutChars.setStatus("mandatory")
_TotalParityErrs_Type = Counter32
_TotalParityErrs_Object = MibScalar
totalParityErrs = _TotalParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 4),
    _TotalParityErrs_Type()
)
totalParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalParityErrs.setStatus("mandatory")
_TotalOverrunErrs_Type = Counter32
_TotalOverrunErrs_Object = MibScalar
totalOverrunErrs = _TotalOverrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 5),
    _TotalOverrunErrs_Type()
)
totalOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOverrunErrs.setStatus("mandatory")
_TotalFramingErrs_Type = Counter32
_TotalFramingErrs_Object = MibScalar
totalFramingErrs = _TotalFramingErrs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 6),
    _TotalFramingErrs_Type()
)
totalFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalFramingErrs.setStatus("mandatory")
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
portEntry.setIndexNames(
    (0, "ANNEX-MIB", "anxpPortIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_AnxpPortIndex_Type = Integer32
_AnxpPortIndex_Object = MibTableColumn
anxpPortIndex = _AnxpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 1),
    _AnxpPortIndex_Type()
)
anxpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpPortIndex.setStatus("mandatory")


class _AnxpMode_Type(Integer32):
    """Custom type anxpMode based on Integer32"""
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
        *(("adaptive", 3),
          ("cli", 1),
          ("dedicated", 6),
          ("ppp", 7),
          ("slave", 2),
          ("slip", 5),
          ("unused", 4))
    )


_AnxpMode_Type.__name__ = "Integer32"
_AnxpMode_Object = MibTableColumn
anxpMode = _AnxpMode_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 2),
    _AnxpMode_Type()
)
anxpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpMode.setStatus("mandatory")


class _AnxpCtrlLines_Type(Integer32):
    """Custom type anxpCtrlLines based on Integer32"""
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


_AnxpCtrlLines_Type.__name__ = "Integer32"
_AnxpCtrlLines_Object = MibTableColumn
anxpCtrlLines = _AnxpCtrlLines_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 3),
    _AnxpCtrlLines_Type()
)
anxpCtrlLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpCtrlLines.setStatus("mandatory")


class _AnxpBidirModem_Type(Integer32):
    """Custom type anxpBidirModem based on Integer32"""
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


_AnxpBidirModem_Type.__name__ = "Integer32"
_AnxpBidirModem_Object = MibTableColumn
anxpBidirModem = _AnxpBidirModem_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 4),
    _AnxpBidirModem_Type()
)
anxpBidirModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpBidirModem.setStatus("mandatory")


class _AnxpAllowBcast_Type(Integer32):
    """Custom type anxpAllowBcast based on Integer32"""
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


_AnxpAllowBcast_Type.__name__ = "Integer32"
_AnxpAllowBcast_Object = MibTableColumn
anxpAllowBcast = _AnxpAllowBcast_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 5),
    _AnxpAllowBcast_Type()
)
anxpAllowBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpAllowBcast.setStatus("mandatory")


class _AnxpBcastDirection_Type(Integer32):
    """Custom type anxpBcastDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("port", 1))
    )


_AnxpBcastDirection_Type.__name__ = "Integer32"
_AnxpBcastDirection_Object = MibTableColumn
anxpBcastDirection = _AnxpBcastDirection_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 6),
    _AnxpBcastDirection_Type()
)
anxpBcastDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpBcastDirection.setStatus("mandatory")


class _AnxpInputStartChar_Type(DisplayString):
    """Custom type anxpInputStartChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AnxpInputStartChar_Type.__name__ = "DisplayString"
_AnxpInputStartChar_Object = MibTableColumn
anxpInputStartChar = _AnxpInputStartChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 7),
    _AnxpInputStartChar_Type()
)
anxpInputStartChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpInputStartChar.setStatus("mandatory")


class _AnxpInputStopChar_Type(DisplayString):
    """Custom type anxpInputStopChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AnxpInputStopChar_Type.__name__ = "DisplayString"
_AnxpInputStopChar_Object = MibTableColumn
anxpInputStopChar = _AnxpInputStopChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 8),
    _AnxpInputStopChar_Type()
)
anxpInputStopChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpInputStopChar.setStatus("mandatory")


class _AnxpOutputStartChar_Type(DisplayString):
    """Custom type anxpOutputStartChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AnxpOutputStartChar_Type.__name__ = "DisplayString"
_AnxpOutputStartChar_Object = MibTableColumn
anxpOutputStartChar = _AnxpOutputStartChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 9),
    _AnxpOutputStartChar_Type()
)
anxpOutputStartChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpOutputStartChar.setStatus("mandatory")


class _AnxpOutputStopChar_Type(DisplayString):
    """Custom type anxpOutputStopChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AnxpOutputStopChar_Type.__name__ = "DisplayString"
_AnxpOutputStopChar_Object = MibTableColumn
anxpOutputStopChar = _AnxpOutputStopChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 10),
    _AnxpOutputStopChar_Type()
)
anxpOutputStopChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpOutputStopChar.setStatus("mandatory")


class _AnxpIxanyFlowCtl_Type(Integer32):
    """Custom type anxpIxanyFlowCtl based on Integer32"""
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


_AnxpIxanyFlowCtl_Type.__name__ = "Integer32"
_AnxpIxanyFlowCtl_Object = MibTableColumn
anxpIxanyFlowCtl = _AnxpIxanyFlowCtl_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 11),
    _AnxpIxanyFlowCtl_Type()
)
anxpIxanyFlowCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpIxanyFlowCtl.setStatus("mandatory")


class _AnxpLongBreak_Type(Integer32):
    """Custom type anxpLongBreak based on Integer32"""
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


_AnxpLongBreak_Type.__name__ = "Integer32"
_AnxpLongBreak_Object = MibTableColumn
anxpLongBreak = _AnxpLongBreak_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 12),
    _AnxpLongBreak_Type()
)
anxpLongBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpLongBreak.setStatus("mandatory")


class _AnxpShortBreak_Type(Integer32):
    """Custom type anxpShortBreak based on Integer32"""
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


_AnxpShortBreak_Type.__name__ = "Integer32"
_AnxpShortBreak_Object = MibTableColumn
anxpShortBreak = _AnxpShortBreak_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 13),
    _AnxpShortBreak_Type()
)
anxpShortBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpShortBreak.setStatus("mandatory")


class _AnxpForwardTimer_Type(Integer32):
    """Custom type anxpForwardTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxpForwardTimer_Type.__name__ = "Integer32"
_AnxpForwardTimer_Object = MibTableColumn
anxpForwardTimer = _AnxpForwardTimer_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 14),
    _AnxpForwardTimer_Type()
)
anxpForwardTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpForwardTimer.setStatus("mandatory")


class _AnxpForwardCount_Type(Integer32):
    """Custom type anxpForwardCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxpForwardCount_Type.__name__ = "Integer32"
_AnxpForwardCount_Object = MibTableColumn
anxpForwardCount = _AnxpForwardCount_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 15),
    _AnxpForwardCount_Type()
)
anxpForwardCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpForwardCount.setStatus("mandatory")


class _AnxpImask7Bits_Type(Integer32):
    """Custom type anxpImask7Bits based on Integer32"""
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


_AnxpImask7Bits_Type.__name__ = "Integer32"
_AnxpImask7Bits_Object = MibTableColumn
anxpImask7Bits = _AnxpImask7Bits_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 16),
    _AnxpImask7Bits_Type()
)
anxpImask7Bits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpImask7Bits.setStatus("mandatory")


class _AnxpAttnChar_Type(DisplayString):
    """Custom type anxpAttnChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_AnxpAttnChar_Type.__name__ = "DisplayString"
_AnxpAttnChar_Object = MibTableColumn
anxpAttnChar = _AnxpAttnChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 17),
    _AnxpAttnChar_Type()
)
anxpAttnChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpAttnChar.setStatus("mandatory")


class _AnxpInputBufSize_Type(Integer32):
    """Custom type anxpInputBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 255),
    )


_AnxpInputBufSize_Type.__name__ = "Integer32"
_AnxpInputBufSize_Object = MibTableColumn
anxpInputBufSize = _AnxpInputBufSize_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 18),
    _AnxpInputBufSize_Type()
)
anxpInputBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpInputBufSize.setStatus("mandatory")


class _AnxpInputIsActivity_Type(Integer32):
    """Custom type anxpInputIsActivity based on Integer32"""
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


_AnxpInputIsActivity_Type.__name__ = "Integer32"
_AnxpInputIsActivity_Object = MibTableColumn
anxpInputIsActivity = _AnxpInputIsActivity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 19),
    _AnxpInputIsActivity_Type()
)
anxpInputIsActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpInputIsActivity.setStatus("mandatory")


class _AnxpOutputIsActivity_Type(Integer32):
    """Custom type anxpOutputIsActivity based on Integer32"""
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


_AnxpOutputIsActivity_Type.__name__ = "Integer32"
_AnxpOutputIsActivity_Object = MibTableColumn
anxpOutputIsActivity = _AnxpOutputIsActivity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 20),
    _AnxpOutputIsActivity_Type()
)
anxpOutputIsActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpOutputIsActivity.setStatus("mandatory")


class _AnxpInactivityTimer_Type(Integer32):
    """Custom type anxpInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxpInactivityTimer_Type.__name__ = "Integer32"
_AnxpInactivityTimer_Object = MibTableColumn
anxpInactivityTimer = _AnxpInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 21),
    _AnxpInactivityTimer_Type()
)
anxpInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpInactivityTimer.setStatus("mandatory")


class _AnxpResetIdleTimer_Type(Integer32):
    """Custom type anxpResetIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_AnxpResetIdleTimer_Type.__name__ = "Integer32"
_AnxpResetIdleTimer_Object = MibTableColumn
anxpResetIdleTimer = _AnxpResetIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 22),
    _AnxpResetIdleTimer_Type()
)
anxpResetIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpResetIdleTimer.setStatus("mandatory")


class _AnxpCliInactivity_Type(Integer32):
    """Custom type anxpCliInactivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxpCliInactivity_Type.__name__ = "Integer32"
_AnxpCliInactivity_Object = MibTableColumn
anxpCliInactivity = _AnxpCliInactivity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 23),
    _AnxpCliInactivity_Type()
)
anxpCliInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpCliInactivity.setStatus("mandatory")


class _AnxpCliSecurity_Type(Integer32):
    """Custom type anxpCliSecurity based on Integer32"""
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


_AnxpCliSecurity_Type.__name__ = "Integer32"
_AnxpCliSecurity_Object = MibTableColumn
anxpCliSecurity = _AnxpCliSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 24),
    _AnxpCliSecurity_Type()
)
anxpCliSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpCliSecurity.setStatus("mandatory")


class _AnxpConnectSecurity_Type(Integer32):
    """Custom type anxpConnectSecurity based on Integer32"""
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


_AnxpConnectSecurity_Type.__name__ = "Integer32"
_AnxpConnectSecurity_Object = MibTableColumn
anxpConnectSecurity = _AnxpConnectSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 25),
    _AnxpConnectSecurity_Type()
)
anxpConnectSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpConnectSecurity.setStatus("mandatory")


class _AnxpPortServerSecurity_Type(Integer32):
    """Custom type anxpPortServerSecurity based on Integer32"""
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


_AnxpPortServerSecurity_Type.__name__ = "Integer32"
_AnxpPortServerSecurity_Object = MibTableColumn
anxpPortServerSecurity = _AnxpPortServerSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 26),
    _AnxpPortServerSecurity_Type()
)
anxpPortServerSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPortServerSecurity.setStatus("mandatory")


class _AnxpPortPassword_Type(DisplayString):
    """Custom type anxpPortPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnxpPortPassword_Type.__name__ = "DisplayString"
_AnxpPortPassword_Object = MibTableColumn
anxpPortPassword = _AnxpPortPassword_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 27),
    _AnxpPortPassword_Type()
)
anxpPortPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPortPassword.setStatus("mandatory")


class _AnxpUserName_Type(DisplayString):
    """Custom type anxpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpUserName_Type.__name__ = "DisplayString"
_AnxpUserName_Object = MibTableColumn
anxpUserName = _AnxpUserName_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 28),
    _AnxpUserName_Type()
)
anxpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpUserName.setStatus("mandatory")
_AnxpDedicatedAddr_Type = IpAddress
_AnxpDedicatedAddr_Object = MibTableColumn
anxpDedicatedAddr = _AnxpDedicatedAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 29),
    _AnxpDedicatedAddr_Type()
)
anxpDedicatedAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpDedicatedAddr.setStatus("mandatory")


class _AnxpDedicatedPort_Type(DisplayString):
    """Custom type anxpDedicatedPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpDedicatedPort_Type.__name__ = "DisplayString"
_AnxpDedicatedPort_Object = MibTableColumn
anxpDedicatedPort = _AnxpDedicatedPort_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 30),
    _AnxpDedicatedPort_Type()
)
anxpDedicatedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpDedicatedPort.setStatus("mandatory")


class _AnxpPrompt_Type(DisplayString):
    """Custom type anxpPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpPrompt_Type.__name__ = "DisplayString"
_AnxpPrompt_Object = MibTableColumn
anxpPrompt = _AnxpPrompt_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 31),
    _AnxpPrompt_Type()
)
anxpPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPrompt.setStatus("mandatory")


class _AnxpTermVar_Type(DisplayString):
    """Custom type anxpTermVar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpTermVar_Type.__name__ = "DisplayString"
_AnxpTermVar_Object = MibTableColumn
anxpTermVar = _AnxpTermVar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 32),
    _AnxpTermVar_Type()
)
anxpTermVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpTermVar.setStatus("mandatory")


class _AnxpNewLineTerm_Type(Integer32):
    """Custom type anxpNewLineTerm based on Integer32"""
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


_AnxpNewLineTerm_Type.__name__ = "Integer32"
_AnxpNewLineTerm_Object = MibTableColumn
anxpNewLineTerm = _AnxpNewLineTerm_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 33),
    _AnxpNewLineTerm_Type()
)
anxpNewLineTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNewLineTerm.setStatus("mandatory")


class _AnxpEcho_Type(Integer32):
    """Custom type anxpEcho based on Integer32"""
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


_AnxpEcho_Type.__name__ = "Integer32"
_AnxpEcho_Object = MibTableColumn
anxpEcho = _AnxpEcho_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 34),
    _AnxpEcho_Type()
)
anxpEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpEcho.setStatus("mandatory")


class _AnxpMapToLower_Type(Integer32):
    """Custom type anxpMapToLower based on Integer32"""
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


_AnxpMapToLower_Type.__name__ = "Integer32"
_AnxpMapToLower_Object = MibTableColumn
anxpMapToLower = _AnxpMapToLower_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 35),
    _AnxpMapToLower_Type()
)
anxpMapToLower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpMapToLower.setStatus("mandatory")


class _AnxpMapToUpper_Type(Integer32):
    """Custom type anxpMapToUpper based on Integer32"""
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


_AnxpMapToUpper_Type.__name__ = "Integer32"
_AnxpMapToUpper_Object = MibTableColumn
anxpMapToUpper = _AnxpMapToUpper_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 36),
    _AnxpMapToUpper_Type()
)
anxpMapToUpper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpMapToUpper.setStatus("mandatory")


class _AnxpHardwareTabs_Type(Integer32):
    """Custom type anxpHardwareTabs based on Integer32"""
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


_AnxpHardwareTabs_Type.__name__ = "Integer32"
_AnxpHardwareTabs_Object = MibTableColumn
anxpHardwareTabs = _AnxpHardwareTabs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 37),
    _AnxpHardwareTabs_Type()
)
anxpHardwareTabs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpHardwareTabs.setStatus("mandatory")


class _AnxpCharErase_Type(Integer32):
    """Custom type anxpCharErase based on Integer32"""
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


_AnxpCharErase_Type.__name__ = "Integer32"
_AnxpCharErase_Object = MibTableColumn
anxpCharErase = _AnxpCharErase_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 38),
    _AnxpCharErase_Type()
)
anxpCharErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpCharErase.setStatus("mandatory")


class _AnxpLineErase_Type(Integer32):
    """Custom type anxpLineErase based on Integer32"""
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


_AnxpLineErase_Type.__name__ = "Integer32"
_AnxpLineErase_Object = MibTableColumn
anxpLineErase = _AnxpLineErase_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 39),
    _AnxpLineErase_Type()
)
anxpLineErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpLineErase.setStatus("mandatory")


class _AnxpEraseChar_Type(DisplayString):
    """Custom type anxpEraseChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AnxpEraseChar_Type.__name__ = "DisplayString"
_AnxpEraseChar_Object = MibTableColumn
anxpEraseChar = _AnxpEraseChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 40),
    _AnxpEraseChar_Type()
)
anxpEraseChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpEraseChar.setStatus("mandatory")


class _AnxpEraseWord_Type(DisplayString):
    """Custom type anxpEraseWord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AnxpEraseWord_Type.__name__ = "DisplayString"
_AnxpEraseWord_Object = MibTableColumn
anxpEraseWord = _AnxpEraseWord_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 41),
    _AnxpEraseWord_Type()
)
anxpEraseWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpEraseWord.setStatus("mandatory")


class _AnxpEraseLine_Type(DisplayString):
    """Custom type anxpEraseLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AnxpEraseLine_Type.__name__ = "DisplayString"
_AnxpEraseLine_Object = MibTableColumn
anxpEraseLine = _AnxpEraseLine_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 42),
    _AnxpEraseLine_Type()
)
anxpEraseLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpEraseLine.setStatus("mandatory")


class _AnxpRedisplayLine_Type(DisplayString):
    """Custom type anxpRedisplayLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AnxpRedisplayLine_Type.__name__ = "DisplayString"
_AnxpRedisplayLine_Object = MibTableColumn
anxpRedisplayLine = _AnxpRedisplayLine_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 43),
    _AnxpRedisplayLine_Type()
)
anxpRedisplayLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpRedisplayLine.setStatus("mandatory")


class _AnxpToggleOutput_Type(DisplayString):
    """Custom type anxpToggleOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AnxpToggleOutput_Type.__name__ = "DisplayString"
_AnxpToggleOutput_Object = MibTableColumn
anxpToggleOutput = _AnxpToggleOutput_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 44),
    _AnxpToggleOutput_Type()
)
anxpToggleOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpToggleOutput.setStatus("mandatory")


class _AnxpTelnetEscape_Type(DisplayString):
    """Custom type anxpTelnetEscape based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AnxpTelnetEscape_Type.__name__ = "DisplayString"
_AnxpTelnetEscape_Object = MibTableColumn
anxpTelnetEscape = _AnxpTelnetEscape_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 45),
    _AnxpTelnetEscape_Type()
)
anxpTelnetEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpTelnetEscape.setStatus("mandatory")


class _AnxpNeedDsr_Type(Integer32):
    """Custom type anxpNeedDsr based on Integer32"""
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


_AnxpNeedDsr_Type.__name__ = "Integer32"
_AnxpNeedDsr_Object = MibTableColumn
anxpNeedDsr = _AnxpNeedDsr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 46),
    _AnxpNeedDsr_Type()
)
anxpNeedDsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNeedDsr.setStatus("mandatory")


class _AnxpTelnetCRLF_Type(Integer32):
    """Custom type anxpTelnetCRLF based on Integer32"""
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


_AnxpTelnetCRLF_Type.__name__ = "Integer32"
_AnxpTelnetCRLF_Object = MibTableColumn
anxpTelnetCRLF = _AnxpTelnetCRLF_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 47),
    _AnxpTelnetCRLF_Type()
)
anxpTelnetCRLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpTelnetCRLF.setStatus("mandatory")


class _AnxpLatbEnable_Type(Integer32):
    """Custom type anxpLatbEnable based on Integer32"""
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


_AnxpLatbEnable_Type.__name__ = "Integer32"
_AnxpLatbEnable_Object = MibTableColumn
anxpLatbEnable = _AnxpLatbEnable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 48),
    _AnxpLatbEnable_Type()
)
anxpLatbEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpLatbEnable.setStatus("mandatory")


class _AnxpSlipSecure_Type(Integer32):
    """Custom type anxpSlipSecure based on Integer32"""
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


_AnxpSlipSecure_Type.__name__ = "Integer32"
_AnxpSlipSecure_Object = MibTableColumn
anxpSlipSecure = _AnxpSlipSecure_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 49),
    _AnxpSlipSecure_Type()
)
anxpSlipSecure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpSlipSecure.setStatus("mandatory")
_AnxpNetLocalAddr_Type = IpAddress
_AnxpNetLocalAddr_Object = MibTableColumn
anxpNetLocalAddr = _AnxpNetLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 50),
    _AnxpNetLocalAddr_Type()
)
anxpNetLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNetLocalAddr.setStatus("mandatory")
_AnxpNetRemoteAddr_Type = IpAddress
_AnxpNetRemoteAddr_Object = MibTableColumn
anxpNetRemoteAddr = _AnxpNetRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 51),
    _AnxpNetRemoteAddr_Type()
)
anxpNetRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNetRemoteAddr.setStatus("mandatory")
_AnxpSlipSubnetMask_Type = IpAddress
_AnxpSlipSubnetMask_Object = MibTableColumn
anxpSlipSubnetMask = _AnxpSlipSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 52),
    _AnxpSlipSubnetMask_Type()
)
anxpSlipSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipSubnetMask.setStatus("mandatory")
_AnxpSlipLoadDumpHost_Type = IpAddress
_AnxpSlipLoadDumpHost_Object = MibTableColumn
anxpSlipLoadDumpHost = _AnxpSlipLoadDumpHost_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 53),
    _AnxpSlipLoadDumpHost_Type()
)
anxpSlipLoadDumpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipLoadDumpHost.setStatus("mandatory")


class _AnxpNetMetric_Type(Integer32):
    """Custom type anxpNetMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AnxpNetMetric_Type.__name__ = "Integer32"
_AnxpNetMetric_Object = MibTableColumn
anxpNetMetric = _AnxpNetMetric_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 54),
    _AnxpNetMetric_Type()
)
anxpNetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNetMetric.setStatus("mandatory")


class _AnxpSlipAllowDump_Type(Integer32):
    """Custom type anxpSlipAllowDump based on Integer32"""
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


_AnxpSlipAllowDump_Type.__name__ = "Integer32"
_AnxpSlipAllowDump_Object = MibTableColumn
anxpSlipAllowDump = _AnxpSlipAllowDump_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 55),
    _AnxpSlipAllowDump_Type()
)
anxpSlipAllowDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipAllowDump.setStatus("mandatory")


class _AnxpSlipDoCompression_Type(Integer32):
    """Custom type anxpSlipDoCompression based on Integer32"""
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


_AnxpSlipDoCompression_Type.__name__ = "Integer32"
_AnxpSlipDoCompression_Object = MibTableColumn
anxpSlipDoCompression = _AnxpSlipDoCompression_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 56),
    _AnxpSlipDoCompression_Type()
)
anxpSlipDoCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipDoCompression.setStatus("mandatory")


class _AnxpSlipAllowCompression_Type(Integer32):
    """Custom type anxpSlipAllowCompression based on Integer32"""
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


_AnxpSlipAllowCompression_Type.__name__ = "Integer32"
_AnxpSlipAllowCompression_Object = MibTableColumn
anxpSlipAllowCompression = _AnxpSlipAllowCompression_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 57),
    _AnxpSlipAllowCompression_Type()
)
anxpSlipAllowCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipAllowCompression.setStatus("mandatory")


class _AnxpSlipMtuSize_Type(Integer32):
    """Custom type anxpSlipMtuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("large", 1),
          ("small", 2))
    )


_AnxpSlipMtuSize_Type.__name__ = "Integer32"
_AnxpSlipMtuSize_Object = MibTableColumn
anxpSlipMtuSize = _AnxpSlipMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 58),
    _AnxpSlipMtuSize_Type()
)
anxpSlipMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipMtuSize.setStatus("mandatory")


class _AnxpSlipNoIcmp_Type(Integer32):
    """Custom type anxpSlipNoIcmp based on Integer32"""
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


_AnxpSlipNoIcmp_Type.__name__ = "Integer32"
_AnxpSlipNoIcmp_Object = MibTableColumn
anxpSlipNoIcmp = _AnxpSlipNoIcmp_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 59),
    _AnxpSlipNoIcmp_Type()
)
anxpSlipNoIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipNoIcmp.setStatus("mandatory")


class _AnxpSlipTos_Type(Integer32):
    """Custom type anxpSlipTos based on Integer32"""
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


_AnxpSlipTos_Type.__name__ = "Integer32"
_AnxpSlipTos_Object = MibTableColumn
anxpSlipTos = _AnxpSlipTos_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 60),
    _AnxpSlipTos_Type()
)
anxpSlipTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipTos.setStatus("mandatory")


class _AnxpPppMru_Type(Integer32):
    """Custom type anxpPppMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_AnxpPppMru_Type.__name__ = "Integer32"
_AnxpPppMru_Object = MibTableColumn
anxpPppMru = _AnxpPppMru_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 61),
    _AnxpPppMru_Type()
)
anxpPppMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppMru.setStatus("mandatory")


class _AnxpPppAcm_Type(DisplayString):
    """Custom type anxpPppAcm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 10),
    )


_AnxpPppAcm_Type.__name__ = "DisplayString"
_AnxpPppAcm_Object = MibTableColumn
anxpPppAcm = _AnxpPppAcm_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 62),
    _AnxpPppAcm_Type()
)
anxpPppAcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppAcm.setStatus("mandatory")


class _AnxpPppSecurityProto_Type(Integer32):
    """Custom type anxpPppSecurityProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pap", 2))
    )


_AnxpPppSecurityProto_Type.__name__ = "Integer32"
_AnxpPppSecurityProto_Object = MibTableColumn
anxpPppSecurityProto = _AnxpPppSecurityProto_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 63),
    _AnxpPppSecurityProto_Type()
)
anxpPppSecurityProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppSecurityProto.setStatus("mandatory")


class _AnxpPppUserRemote_Type(DisplayString):
    """Custom type anxpPppUserRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnxpPppUserRemote_Type.__name__ = "DisplayString"
_AnxpPppUserRemote_Object = MibTableColumn
anxpPppUserRemote = _AnxpPppUserRemote_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 64),
    _AnxpPppUserRemote_Type()
)
anxpPppUserRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppUserRemote.setStatus("mandatory")


class _AnxpPppPasswdRemote_Type(DisplayString):
    """Custom type anxpPppPasswdRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnxpPppPasswdRemote_Type.__name__ = "DisplayString"
_AnxpPppPasswdRemote_Object = MibTableColumn
anxpPppPasswdRemote = _AnxpPppPasswdRemote_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 65),
    _AnxpPppPasswdRemote_Type()
)
anxpPppPasswdRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppPasswdRemote.setStatus("mandatory")


class _AnxpLatAuthGroupVal_Type(DisplayString):
    """Custom type anxpLatAuthGroupVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_AnxpLatAuthGroupVal_Type.__name__ = "DisplayString"
_AnxpLatAuthGroupVal_Object = MibTableColumn
anxpLatAuthGroupVal = _AnxpLatAuthGroupVal_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 66),
    _AnxpLatAuthGroupVal_Type()
)
anxpLatAuthGroupVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpLatAuthGroupVal.setStatus("mandatory")


class _AnxpPppDialupAddr_Type(Integer32):
    """Custom type anxpPppDialupAddr based on Integer32"""
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


_AnxpPppDialupAddr_Type.__name__ = "Integer32"
_AnxpPppDialupAddr_Object = MibTableColumn
anxpPppDialupAddr = _AnxpPppDialupAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 67),
    _AnxpPppDialupAddr_Type()
)
anxpPppDialupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppDialupAddr.setStatus("mandatory")


class _AnxpBanner_Type(Integer32):
    """Custom type anxpBanner based on Integer32"""
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


_AnxpBanner_Type.__name__ = "Integer32"
_AnxpBanner_Object = MibTableColumn
anxpBanner = _AnxpBanner_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 68),
    _AnxpBanner_Type()
)
anxpBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpBanner.setStatus("mandatory")


class _AnxpPsHistory_Type(Integer32):
    """Custom type anxpPsHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AnxpPsHistory_Type.__name__ = "Integer32"
_AnxpPsHistory_Object = MibTableColumn
anxpPsHistory = _AnxpPsHistory_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 69),
    _AnxpPsHistory_Type()
)
anxpPsHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPsHistory.setStatus("mandatory")


class _AnxpLocation_Type(DisplayString):
    """Custom type anxpLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AnxpLocation_Type.__name__ = "DisplayString"
_AnxpLocation_Object = MibTableColumn
anxpLocation = _AnxpLocation_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 70),
    _AnxpLocation_Type()
)
anxpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpLocation.setStatus("mandatory")


class _AnxpType_Type(Integer32):
    """Custom type anxpType based on Integer32"""
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
        *(("dialin", 1),
          ("hardwired", 2),
          ("modem", 4),
          ("printer", 5),
          ("terminal", 3))
    )


_AnxpType_Type.__name__ = "Integer32"
_AnxpType_Object = MibTableColumn
anxpType = _AnxpType_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 71),
    _AnxpType_Type()
)
anxpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpType.setStatus("mandatory")


class _AnxpCliImask7_Type(Integer32):
    """Custom type anxpCliImask7 based on Integer32"""
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


_AnxpCliImask7_Type.__name__ = "Integer32"
_AnxpCliImask7_Object = MibTableColumn
anxpCliImask7 = _AnxpCliImask7_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 72),
    _AnxpCliImask7_Type()
)
anxpCliImask7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpCliImask7.setStatus("mandatory")
_Parallelport_ObjectIdentity = ObjectIdentity
parallelport = _Parallelport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 4)
)
_AnxpParaPorts_Type = Integer32
_AnxpParaPorts_Object = MibScalar
anxpParaPorts = _AnxpParaPorts_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 1),
    _AnxpParaPorts_Type()
)
anxpParaPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpParaPorts.setStatus("mandatory")
_AnxpParaPortTable_Object = MibTable
anxpParaPortTable = _AnxpParaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2)
)
if mibBuilder.loadTexts:
    anxpParaPortTable.setStatus("mandatory")
_AnxpParaPortEntry_Object = MibTableRow
anxpParaPortEntry = _AnxpParaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1)
)
anxpParaPortEntry.setIndexNames(
    (0, "ANNEX-MIB", "anxpParaPortIndex"),
)
if mibBuilder.loadTexts:
    anxpParaPortEntry.setStatus("mandatory")
_AnxpParaPortIndex_Type = Integer32
_AnxpParaPortIndex_Object = MibTableColumn
anxpParaPortIndex = _AnxpParaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 1),
    _AnxpParaPortIndex_Type()
)
anxpParaPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpParaPortIndex.setStatus("mandatory")


class _AnxpParaPortHardwareTabs_Type(Integer32):
    """Custom type anxpParaPortHardwareTabs based on Integer32"""
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


_AnxpParaPortHardwareTabs_Type.__name__ = "Integer32"
_AnxpParaPortHardwareTabs_Object = MibTableColumn
anxpParaPortHardwareTabs = _AnxpParaPortHardwareTabs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 2),
    _AnxpParaPortHardwareTabs_Type()
)
anxpParaPortHardwareTabs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortHardwareTabs.setStatus("mandatory")


class _AnxpParaPortMapToUpper_Type(Integer32):
    """Custom type anxpParaPortMapToUpper based on Integer32"""
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


_AnxpParaPortMapToUpper_Type.__name__ = "Integer32"
_AnxpParaPortMapToUpper_Object = MibTableColumn
anxpParaPortMapToUpper = _AnxpParaPortMapToUpper_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 3),
    _AnxpParaPortMapToUpper_Type()
)
anxpParaPortMapToUpper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortMapToUpper.setStatus("mandatory")


class _AnxpParaPortPrinterWidth_Type(Integer32):
    """Custom type anxpParaPortPrinterWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 132),
    )


_AnxpParaPortPrinterWidth_Type.__name__ = "Integer32"
_AnxpParaPortPrinterWidth_Object = MibTableColumn
anxpParaPortPrinterWidth = _AnxpParaPortPrinterWidth_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 4),
    _AnxpParaPortPrinterWidth_Type()
)
anxpParaPortPrinterWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortPrinterWidth.setStatus("mandatory")


class _AnxpParaPortInterface_Type(Integer32):
    """Custom type anxpParaPortInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("centronics", 1),
          ("dataproducts", 2))
    )


_AnxpParaPortInterface_Type.__name__ = "Integer32"
_AnxpParaPortInterface_Object = MibTableColumn
anxpParaPortInterface = _AnxpParaPortInterface_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 5),
    _AnxpParaPortInterface_Type()
)
anxpParaPortInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortInterface.setStatus("mandatory")


class _AnxpParaPortSpeed_Type(Integer32):
    """Custom type anxpParaPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high-speed", 2),
          ("normal", 1))
    )


_AnxpParaPortSpeed_Type.__name__ = "Integer32"
_AnxpParaPortSpeed_Object = MibTableColumn
anxpParaPortSpeed = _AnxpParaPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 6),
    _AnxpParaPortSpeed_Type()
)
anxpParaPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortSpeed.setStatus("mandatory")
_Annexconfig_ObjectIdentity = ObjectIdentity
annexconfig = _Annexconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 5)
)
_AnxInetAddr_Type = IpAddress
_AnxInetAddr_Object = MibScalar
anxInetAddr = _AnxInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 1),
    _AnxInetAddr_Type()
)
anxInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxInetAddr.setStatus("mandatory")
_AnxPrefLoadAddr_Type = IpAddress
_AnxPrefLoadAddr_Object = MibScalar
anxPrefLoadAddr = _AnxPrefLoadAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 2),
    _AnxPrefLoadAddr_Type()
)
anxPrefLoadAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxPrefLoadAddr.setStatus("mandatory")
_AnxPrefDumpAddr_Type = IpAddress
_AnxPrefDumpAddr_Object = MibScalar
anxPrefDumpAddr = _AnxPrefDumpAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 3),
    _AnxPrefDumpAddr_Type()
)
anxPrefDumpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxPrefDumpAddr.setStatus("mandatory")
_AnxLoadDumpGateway_Type = IpAddress
_AnxLoadDumpGateway_Object = MibScalar
anxLoadDumpGateway = _AnxLoadDumpGateway_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 4),
    _AnxLoadDumpGateway_Type()
)
anxLoadDumpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxLoadDumpGateway.setStatus("mandatory")


class _AnxLoadDumpSeq_Type(DisplayString):
    """Custom type anxLoadDumpSeq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AnxLoadDumpSeq_Type.__name__ = "DisplayString"
_AnxLoadDumpSeq_Object = MibScalar
anxLoadDumpSeq = _AnxLoadDumpSeq_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 5),
    _AnxLoadDumpSeq_Type()
)
anxLoadDumpSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxLoadDumpSeq.setStatus("mandatory")


class _AnxLoadBcast_Type(Integer32):
    """Custom type anxLoadBcast based on Integer32"""
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


_AnxLoadBcast_Type.__name__ = "Integer32"
_AnxLoadBcast_Object = MibScalar
anxLoadBcast = _AnxLoadBcast_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 6),
    _AnxLoadBcast_Type()
)
anxLoadBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxLoadBcast.setStatus("mandatory")


class _AnxServerCap_Type(DisplayString):
    """Custom type anxServerCap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AnxServerCap_Type.__name__ = "DisplayString"
_AnxServerCap_Object = MibScalar
anxServerCap = _AnxServerCap_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 7),
    _AnxServerCap_Type()
)
anxServerCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxServerCap.setStatus("mandatory")


class _AnxTimeBcast_Type(Integer32):
    """Custom type anxTimeBcast based on Integer32"""
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


_AnxTimeBcast_Type.__name__ = "Integer32"
_AnxTimeBcast_Object = MibScalar
anxTimeBcast = _AnxTimeBcast_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 8),
    _AnxTimeBcast_Type()
)
anxTimeBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxTimeBcast.setStatus("mandatory")
_AnxBcastAddr_Type = IpAddress
_AnxBcastAddr_Object = MibScalar
anxBcastAddr = _AnxBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 9),
    _AnxBcastAddr_Type()
)
anxBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxBcastAddr.setStatus("mandatory")
_AnxSubnetMask_Type = IpAddress
_AnxSubnetMask_Object = MibScalar
anxSubnetMask = _AnxSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 10),
    _AnxSubnetMask_Type()
)
anxSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSubnetMask.setStatus("mandatory")


class _AnxAuthAgent_Type(Integer32):
    """Custom type anxAuthAgent based on Integer32"""
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


_AnxAuthAgent_Type.__name__ = "Integer32"
_AnxAuthAgent_Object = MibScalar
anxAuthAgent = _AnxAuthAgent_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 11),
    _AnxAuthAgent_Type()
)
anxAuthAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxAuthAgent.setStatus("mandatory")


class _AnxMaxVcli_Type(Integer32):
    """Custom type anxMaxVcli based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxMaxVcli_Type.__name__ = "Integer32"
_AnxMaxVcli_Object = MibScalar
anxMaxVcli = _AnxMaxVcli_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 12),
    _AnxMaxVcli_Type()
)
anxMaxVcli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxMaxVcli.setStatus("mandatory")


class _AnxIpEncapType_Type(Integer32):
    """Custom type anxIpEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee802", 2))
    )


_AnxIpEncapType_Type.__name__ = "Integer32"
_AnxIpEncapType_Object = MibScalar
anxIpEncapType = _AnxIpEncapType_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 13),
    _AnxIpEncapType_Type()
)
anxIpEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxIpEncapType.setStatus("mandatory")


class _AnxNameServer1Type_Type(Integer32):
    """Custom type anxNameServer1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dns", 3),
          ("ien116", 2),
          ("none", 1))
    )


_AnxNameServer1Type_Type.__name__ = "Integer32"
_AnxNameServer1Type_Object = MibScalar
anxNameServer1Type = _AnxNameServer1Type_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 14),
    _AnxNameServer1Type_Type()
)
anxNameServer1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxNameServer1Type.setStatus("mandatory")
_AnxNameServer1Addr_Type = IpAddress
_AnxNameServer1Addr_Object = MibScalar
anxNameServer1Addr = _AnxNameServer1Addr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 15),
    _AnxNameServer1Addr_Type()
)
anxNameServer1Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxNameServer1Addr.setStatus("mandatory")


class _AnxNameServer2Type_Type(Integer32):
    """Custom type anxNameServer2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dns", 3),
          ("ien116", 2),
          ("none", 1))
    )


_AnxNameServer2Type_Type.__name__ = "Integer32"
_AnxNameServer2Type_Object = MibScalar
anxNameServer2Type = _AnxNameServer2Type_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 16),
    _AnxNameServer2Type_Type()
)
anxNameServer2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxNameServer2Type.setStatus("mandatory")
_AnxNameServer2Addr_Type = IpAddress
_AnxNameServer2Addr_Object = MibScalar
anxNameServer2Addr = _AnxNameServer2Addr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 17),
    _AnxNameServer2Addr_Type()
)
anxNameServer2Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxNameServer2Addr.setStatus("mandatory")


class _AnxNameServerBcast_Type(Integer32):
    """Custom type anxNameServerBcast based on Integer32"""
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


_AnxNameServerBcast_Type.__name__ = "Integer32"
_AnxNameServerBcast_Object = MibScalar
anxNameServerBcast = _AnxNameServerBcast_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 18),
    _AnxNameServerBcast_Type()
)
anxNameServerBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxNameServerBcast.setStatus("mandatory")


class _AnxRwhod_Type(Integer32):
    """Custom type anxRwhod based on Integer32"""
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


_AnxRwhod_Type.__name__ = "Integer32"
_AnxRwhod_Object = MibScalar
anxRwhod = _AnxRwhod_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 19),
    _AnxRwhod_Type()
)
anxRwhod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxRwhod.setStatus("mandatory")


class _AnxMinUniqueHostNames_Type(Integer32):
    """Custom type anxMinUniqueHostNames based on Integer32"""
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


_AnxMinUniqueHostNames_Type.__name__ = "Integer32"
_AnxMinUniqueHostNames_Object = MibScalar
anxMinUniqueHostNames = _AnxMinUniqueHostNames_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 20),
    _AnxMinUniqueHostNames_Type()
)
anxMinUniqueHostNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxMinUniqueHostNames.setStatus("mandatory")


class _AnxHostTableSize_Type(Integer32):
    """Custom type anxHostTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 251),
    )


_AnxHostTableSize_Type.__name__ = "Integer32"
_AnxHostTableSize_Object = MibScalar
anxHostTableSize = _AnxHostTableSize_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 21),
    _AnxHostTableSize_Type()
)
anxHostTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxHostTableSize.setStatus("mandatory")


class _AnxRouted_Type(Integer32):
    """Custom type anxRouted based on Integer32"""
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


_AnxRouted_Type.__name__ = "Integer32"
_AnxRouted_Object = MibScalar
anxRouted = _AnxRouted_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 22),
    _AnxRouted_Type()
)
anxRouted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxRouted.setStatus("mandatory")


class _AnxEnableSecurity_Type(Integer32):
    """Custom type anxEnableSecurity based on Integer32"""
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


_AnxEnableSecurity_Type.__name__ = "Integer32"
_AnxEnableSecurity_Object = MibScalar
anxEnableSecurity = _AnxEnableSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 23),
    _AnxEnableSecurity_Type()
)
anxEnableSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxEnableSecurity.setStatus("mandatory")


class _AnxPassword_Type(DisplayString):
    """Custom type anxPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnxPassword_Type.__name__ = "DisplayString"
_AnxPassword_Object = MibScalar
anxPassword = _AnxPassword_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 24),
    _AnxPassword_Type()
)
anxPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxPassword.setStatus("mandatory")
_AnxSecurServer1Addr_Type = IpAddress
_AnxSecurServer1Addr_Object = MibScalar
anxSecurServer1Addr = _AnxSecurServer1Addr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 25),
    _AnxSecurServer1Addr_Type()
)
anxSecurServer1Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSecurServer1Addr.setStatus("mandatory")
_AnxSecurServer2Addr_Type = IpAddress
_AnxSecurServer2Addr_Object = MibScalar
anxSecurServer2Addr = _AnxSecurServer2Addr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 26),
    _AnxSecurServer2Addr_Type()
)
anxSecurServer2Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSecurServer2Addr.setStatus("mandatory")


class _AnxNetTurnAround_Type(Integer32):
    """Custom type anxNetTurnAround based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AnxNetTurnAround_Type.__name__ = "Integer32"
_AnxNetTurnAround_Object = MibScalar
anxNetTurnAround = _AnxNetTurnAround_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 27),
    _AnxNetTurnAround_Type()
)
anxNetTurnAround.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxNetTurnAround.setStatus("mandatory")


class _AnxSecurBcast_Type(Integer32):
    """Custom type anxSecurBcast based on Integer32"""
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


_AnxSecurBcast_Type.__name__ = "Integer32"
_AnxSecurBcast_Object = MibScalar
anxSecurBcast = _AnxSecurBcast_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 28),
    _AnxSecurBcast_Type()
)
anxSecurBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSecurBcast.setStatus("mandatory")


class _AnxVcliSecurity_Type(Integer32):
    """Custom type anxVcliSecurity based on Integer32"""
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


_AnxVcliSecurity_Type.__name__ = "Integer32"
_AnxVcliSecurity_Object = MibScalar
anxVcliSecurity = _AnxVcliSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 29),
    _AnxVcliSecurity_Type()
)
anxVcliSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxVcliSecurity.setStatus("mandatory")


class _AnxVcliPassword_Type(DisplayString):
    """Custom type anxVcliPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnxVcliPassword_Type.__name__ = "DisplayString"
_AnxVcliPassword_Object = MibScalar
anxVcliPassword = _AnxVcliPassword_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 30),
    _AnxVcliPassword_Type()
)
anxVcliPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxVcliPassword.setStatus("mandatory")


class _AnxAcpKey_Type(DisplayString):
    """Custom type anxAcpKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnxAcpKey_Type.__name__ = "DisplayString"
_AnxAcpKey_Object = MibScalar
anxAcpKey = _AnxAcpKey_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 31),
    _AnxAcpKey_Type()
)
anxAcpKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxAcpKey.setStatus("mandatory")


class _AnxSysLogMask_Type(DisplayString):
    """Custom type anxSysLogMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AnxSysLogMask_Type.__name__ = "DisplayString"
_AnxSysLogMask_Object = MibScalar
anxSysLogMask = _AnxSysLogMask_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 32),
    _AnxSysLogMask_Type()
)
anxSysLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSysLogMask.setStatus("mandatory")


class _AnxSysLogFacility_Type(Integer32):
    """Custom type anxSysLogFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("loglocal0", 17),
          ("loglocal1", 18),
          ("loglocal2", 19),
          ("loglocal3", 20),
          ("loglocal4", 21),
          ("loglocal5", 22),
          ("loglocal6", 23),
          ("loglocal7", 24))
    )


_AnxSysLogFacility_Type.__name__ = "Integer32"
_AnxSysLogFacility_Object = MibScalar
anxSysLogFacility = _AnxSysLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 33),
    _AnxSysLogFacility_Type()
)
anxSysLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSysLogFacility.setStatus("mandatory")
_AnxSysLogHost_Type = IpAddress
_AnxSysLogHost_Object = MibScalar
anxSysLogHost = _AnxSysLogHost_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 34),
    _AnxSysLogHost_Type()
)
anxSysLogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSysLogHost.setStatus("mandatory")


class _AnxCliPrompt_Type(DisplayString):
    """Custom type anxCliPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AnxCliPrompt_Type.__name__ = "DisplayString"
_AnxCliPrompt_Object = MibScalar
anxCliPrompt = _AnxCliPrompt_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 35),
    _AnxCliPrompt_Type()
)
anxCliPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxCliPrompt.setStatus("mandatory")


class _AnxMotdFile_Type(DisplayString):
    """Custom type anxMotdFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AnxMotdFile_Type.__name__ = "DisplayString"
_AnxMotdFile_Object = MibScalar
anxMotdFile = _AnxMotdFile_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 36),
    _AnxMotdFile_Type()
)
anxMotdFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxMotdFile.setStatus("mandatory")


class _AnxTftpDirName_Type(DisplayString):
    """Custom type anxTftpDirName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AnxTftpDirName_Type.__name__ = "DisplayString"
_AnxTftpDirName_Object = MibScalar
anxTftpDirName = _AnxTftpDirName_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 37),
    _AnxTftpDirName_Type()
)
anxTftpDirName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxTftpDirName.setStatus("mandatory")


class _AnxTftpDumpName_Type(DisplayString):
    """Custom type anxTftpDumpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AnxTftpDumpName_Type.__name__ = "DisplayString"
_AnxTftpDumpName_Object = MibScalar
anxTftpDumpName = _AnxTftpDumpName_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 38),
    _AnxTftpDumpName_Type()
)
anxTftpDumpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxTftpDumpName.setStatus("mandatory")


class _AnxTimeZone_Type(Integer32):
    """Custom type anxTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1200, 1200),
    )


_AnxTimeZone_Type.__name__ = "Integer32"
_AnxTimeZone_Object = MibScalar
anxTimeZone = _AnxTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 39),
    _AnxTimeZone_Type()
)
anxTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxTimeZone.setStatus("mandatory")


class _AnxDaylightSavings_Type(Integer32):
    """Custom type anxDaylightSavings based on Integer32"""
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
        *(("australian", 2),
          ("british", 7),
          ("canadian", 6),
          ("easteuropean", 5),
          ("mideuropean", 4),
          ("none", 8),
          ("us", 1),
          ("westeuropean", 3))
    )


_AnxDaylightSavings_Type.__name__ = "Integer32"
_AnxDaylightSavings_Object = MibScalar
anxDaylightSavings = _AnxDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 40),
    _AnxDaylightSavings_Type()
)
anxDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxDaylightSavings.setStatus("mandatory")


class _AnxLatKey_Type(DisplayString):
    """Custom type anxLatKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AnxLatKey_Type.__name__ = "DisplayString"
_AnxLatKey_Object = MibScalar
anxLatKey = _AnxLatKey_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 41),
    _AnxLatKey_Type()
)
anxLatKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxLatKey.setStatus("mandatory")


class _AnxCircuitTimer_Type(Integer32):
    """Custom type anxCircuitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AnxCircuitTimer_Type.__name__ = "Integer32"
_AnxCircuitTimer_Object = MibScalar
anxCircuitTimer = _AnxCircuitTimer_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 42),
    _AnxCircuitTimer_Type()
)
anxCircuitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxCircuitTimer.setStatus("mandatory")


class _AnxFacilityNum_Type(Integer32):
    """Custom type anxFacilityNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AnxFacilityNum_Type.__name__ = "Integer32"
_AnxFacilityNum_Object = MibScalar
anxFacilityNum = _AnxFacilityNum_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 43),
    _AnxFacilityNum_Type()
)
anxFacilityNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxFacilityNum.setStatus("mandatory")


class _AnxLatGroupVal_Type(DisplayString):
    """Custom type anxLatGroupVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_AnxLatGroupVal_Type.__name__ = "DisplayString"
_AnxLatGroupVal_Object = MibScalar
anxLatGroupVal = _AnxLatGroupVal_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 44),
    _AnxLatGroupVal_Type()
)
anxLatGroupVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxLatGroupVal.setStatus("mandatory")


class _AnxKeepAliveTimer_Type(Integer32):
    """Custom type anxKeepAliveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_AnxKeepAliveTimer_Type.__name__ = "Integer32"
_AnxKeepAliveTimer_Object = MibScalar
anxKeepAliveTimer = _AnxKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 45),
    _AnxKeepAliveTimer_Type()
)
anxKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxKeepAliveTimer.setStatus("mandatory")


class _AnxReXmitLimit_Type(Integer32):
    """Custom type anxReXmitLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 120),
    )


_AnxReXmitLimit_Type.__name__ = "Integer32"
_AnxReXmitLimit_Object = MibScalar
anxReXmitLimit = _AnxReXmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 46),
    _AnxReXmitLimit_Type()
)
anxReXmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxReXmitLimit.setStatus("mandatory")


class _AnxServerName_Type(DisplayString):
    """Custom type anxServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxServerName_Type.__name__ = "DisplayString"
_AnxServerName_Object = MibScalar
anxServerName = _AnxServerName_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 47),
    _AnxServerName_Type()
)
anxServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxServerName.setStatus("mandatory")


class _AnxServiceLimit_Type(Integer32):
    """Custom type anxServiceLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 2048),
    )


_AnxServiceLimit_Type.__name__ = "Integer32"
_AnxServiceLimit_Object = MibScalar
anxServiceLimit = _AnxServiceLimit_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 48),
    _AnxServiceLimit_Type()
)
anxServiceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxServiceLimit.setStatus("mandatory")


class _AnxConfigFile_Type(DisplayString):
    """Custom type anxConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AnxConfigFile_Type.__name__ = "DisplayString"
_AnxConfigFile_Object = MibScalar
anxConfigFile = _AnxConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 49),
    _AnxConfigFile_Type()
)
anxConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxConfigFile.setStatus("mandatory")


class _AnxLatVcliGroupVal_Type(DisplayString):
    """Custom type anxLatVcliGroupVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_AnxLatVcliGroupVal_Type.__name__ = "DisplayString"
_AnxLatVcliGroupVal_Object = MibScalar
anxLatVcliGroupVal = _AnxLatVcliGroupVal_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 50),
    _AnxLatVcliGroupVal_Type()
)
anxLatVcliGroupVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxLatVcliGroupVal.setStatus("mandatory")


class _AnxLatQueueMax_Type(Integer32):
    """Custom type anxLatQueueMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxLatQueueMax_Type.__name__ = "Integer32"
_AnxLatQueueMax_Object = MibScalar
anxLatQueueMax = _AnxLatQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 51),
    _AnxLatQueueMax_Type()
)
anxLatQueueMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxLatQueueMax.setStatus("mandatory")


class _AnxLatLocation_Type(DisplayString):
    """Custom type anxLatLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AnxLatLocation_Type.__name__ = "DisplayString"
_AnxLatLocation_Object = MibScalar
anxLatLocation = _AnxLatLocation_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 52),
    _AnxLatLocation_Type()
)
anxLatLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxLatLocation.setStatus("mandatory")


class _AnxDisabledModules_Type(DisplayString):
    """Custom type anxDisabledModules based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AnxDisabledModules_Type.__name__ = "DisplayString"
_AnxDisabledModules_Object = MibScalar
anxDisabledModules = _AnxDisabledModules_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 53),
    _AnxDisabledModules_Type()
)
anxDisabledModules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxDisabledModules.setStatus("mandatory")


class _AnxSysLogPort_Type(Integer32):
    """Custom type anxSysLogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AnxSysLogPort_Type.__name__ = "Integer32"
_AnxSysLogPort_Object = MibScalar
anxSysLogPort = _AnxSysLogPort_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 5, 54),
    _AnxSysLogPort_Type()
)
anxSysLogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSysLogPort.setStatus("mandatory")
_Annexcmds_ObjectIdentity = ObjectIdentity
annexcmds = _Annexcmds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15, 2, 6)
)


class _AnxcBoot_Type(Integer32):
    """Custom type anxcBoot based on Integer32"""
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
        *(("abortschedule", 5),
          ("delayed", 2),
          ("diagnosticboot", 4),
          ("dumpboot", 3),
          ("immediate", 1),
          ("quiet", 6))
    )


_AnxcBoot_Type.__name__ = "Integer32"
_AnxcBoot_Object = MibScalar
anxcBoot = _AnxcBoot_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 6, 1),
    _AnxcBoot_Type()
)
anxcBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxcBoot.setStatus("mandatory")


class _AnxcBootImage_Type(DisplayString):
    """Custom type anxcBootImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AnxcBootImage_Type.__name__ = "DisplayString"
_AnxcBootImage_Object = MibScalar
anxcBootImage = _AnxcBootImage_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 6, 2),
    _AnxcBootImage_Type()
)
anxcBootImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxcBootImage.setStatus("mandatory")


class _AnxcBootTime_Type(DisplayString):
    """Custom type anxcBootTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 10),
    )


_AnxcBootTime_Type.__name__ = "DisplayString"
_AnxcBootTime_Object = MibScalar
anxcBootTime = _AnxcBootTime_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 6, 3),
    _AnxcBootTime_Type()
)
anxcBootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxcBootTime.setStatus("mandatory")


class _AnxcBootMsg_Type(DisplayString):
    """Custom type anxcBootMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AnxcBootMsg_Type.__name__ = "DisplayString"
_AnxcBootMsg_Object = MibScalar
anxcBootMsg = _AnxcBootMsg_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 6, 4),
    _AnxcBootMsg_Type()
)
anxcBootMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxcBootMsg.setStatus("mandatory")


class _AnxcReset_Type(Integer32):
    """Custom type anxcReset based on Integer32"""
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
        *(("all", 1),
          ("macros", 2),
          ("motd", 3),
          ("nameserver", 4),
          ("printerport", 6),
          ("security", 5),
          ("serialports", 7),
          ("virtualports", 8))
    )


_AnxcReset_Type.__name__ = "Integer32"
_AnxcReset_Object = MibScalar
anxcReset = _AnxcReset_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 6, 5),
    _AnxcReset_Type()
)
anxcReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxcReset.setStatus("mandatory")


class _AnxcBcast_Type(Integer32):
    """Custom type anxcBcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("serial", 2),
          ("virtual", 3))
    )


_AnxcBcast_Type.__name__ = "Integer32"
_AnxcBcast_Object = MibScalar
anxcBcast = _AnxcBcast_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 6, 6),
    _AnxcBcast_Type()
)
anxcBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxcBcast.setStatus("mandatory")


class _AnxcBcastMsg_Type(DisplayString):
    """Custom type anxcBcastMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AnxcBcastMsg_Type.__name__ = "DisplayString"
_AnxcBcastMsg_Object = MibScalar
anxcBcastMsg = _AnxcBcastMsg_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 6, 7),
    _AnxcBcastMsg_Type()
)
anxcBcastMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxcBcastMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANNEX-MIB",
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
       "cpuIRescheds": cpuIRescheds,
       "cpuTRescheds": cpuTRescheds,
       "contextISwtchs": contextISwtchs,
       "contextTSwtchs": contextTSwtchs,
       "cpuIActivates": cpuIActivates,
       "cpuTActivates": cpuTActivates,
       "maxCallouts": maxCallouts,
       "leastCallouts": leastCallouts,
       "freeCallouts": freeCallouts,
       "ports": ports,
       "totalPorts": totalPorts,
       "totalInChars": totalInChars,
       "totalOutChars": totalOutChars,
       "totalParityErrs": totalParityErrs,
       "totalOverrunErrs": totalOverrunErrs,
       "totalFramingErrs": totalFramingErrs,
       "portTable": portTable,
       "portEntry": portEntry,
       "anxpPortIndex": anxpPortIndex,
       "anxpMode": anxpMode,
       "anxpCtrlLines": anxpCtrlLines,
       "anxpBidirModem": anxpBidirModem,
       "anxpAllowBcast": anxpAllowBcast,
       "anxpBcastDirection": anxpBcastDirection,
       "anxpInputStartChar": anxpInputStartChar,
       "anxpInputStopChar": anxpInputStopChar,
       "anxpOutputStartChar": anxpOutputStartChar,
       "anxpOutputStopChar": anxpOutputStopChar,
       "anxpIxanyFlowCtl": anxpIxanyFlowCtl,
       "anxpLongBreak": anxpLongBreak,
       "anxpShortBreak": anxpShortBreak,
       "anxpForwardTimer": anxpForwardTimer,
       "anxpForwardCount": anxpForwardCount,
       "anxpImask7Bits": anxpImask7Bits,
       "anxpAttnChar": anxpAttnChar,
       "anxpInputBufSize": anxpInputBufSize,
       "anxpInputIsActivity": anxpInputIsActivity,
       "anxpOutputIsActivity": anxpOutputIsActivity,
       "anxpInactivityTimer": anxpInactivityTimer,
       "anxpResetIdleTimer": anxpResetIdleTimer,
       "anxpCliInactivity": anxpCliInactivity,
       "anxpCliSecurity": anxpCliSecurity,
       "anxpConnectSecurity": anxpConnectSecurity,
       "anxpPortServerSecurity": anxpPortServerSecurity,
       "anxpPortPassword": anxpPortPassword,
       "anxpUserName": anxpUserName,
       "anxpDedicatedAddr": anxpDedicatedAddr,
       "anxpDedicatedPort": anxpDedicatedPort,
       "anxpPrompt": anxpPrompt,
       "anxpTermVar": anxpTermVar,
       "anxpNewLineTerm": anxpNewLineTerm,
       "anxpEcho": anxpEcho,
       "anxpMapToLower": anxpMapToLower,
       "anxpMapToUpper": anxpMapToUpper,
       "anxpHardwareTabs": anxpHardwareTabs,
       "anxpCharErase": anxpCharErase,
       "anxpLineErase": anxpLineErase,
       "anxpEraseChar": anxpEraseChar,
       "anxpEraseWord": anxpEraseWord,
       "anxpEraseLine": anxpEraseLine,
       "anxpRedisplayLine": anxpRedisplayLine,
       "anxpToggleOutput": anxpToggleOutput,
       "anxpTelnetEscape": anxpTelnetEscape,
       "anxpNeedDsr": anxpNeedDsr,
       "anxpTelnetCRLF": anxpTelnetCRLF,
       "anxpLatbEnable": anxpLatbEnable,
       "anxpSlipSecure": anxpSlipSecure,
       "anxpNetLocalAddr": anxpNetLocalAddr,
       "anxpNetRemoteAddr": anxpNetRemoteAddr,
       "anxpSlipSubnetMask": anxpSlipSubnetMask,
       "anxpSlipLoadDumpHost": anxpSlipLoadDumpHost,
       "anxpNetMetric": anxpNetMetric,
       "anxpSlipAllowDump": anxpSlipAllowDump,
       "anxpSlipDoCompression": anxpSlipDoCompression,
       "anxpSlipAllowCompression": anxpSlipAllowCompression,
       "anxpSlipMtuSize": anxpSlipMtuSize,
       "anxpSlipNoIcmp": anxpSlipNoIcmp,
       "anxpSlipTos": anxpSlipTos,
       "anxpPppMru": anxpPppMru,
       "anxpPppAcm": anxpPppAcm,
       "anxpPppSecurityProto": anxpPppSecurityProto,
       "anxpPppUserRemote": anxpPppUserRemote,
       "anxpPppPasswdRemote": anxpPppPasswdRemote,
       "anxpLatAuthGroupVal": anxpLatAuthGroupVal,
       "anxpPppDialupAddr": anxpPppDialupAddr,
       "anxpBanner": anxpBanner,
       "anxpPsHistory": anxpPsHistory,
       "anxpLocation": anxpLocation,
       "anxpType": anxpType,
       "anxpCliImask7": anxpCliImask7,
       "parallelport": parallelport,
       "anxpParaPorts": anxpParaPorts,
       "anxpParaPortTable": anxpParaPortTable,
       "anxpParaPortEntry": anxpParaPortEntry,
       "anxpParaPortIndex": anxpParaPortIndex,
       "anxpParaPortHardwareTabs": anxpParaPortHardwareTabs,
       "anxpParaPortMapToUpper": anxpParaPortMapToUpper,
       "anxpParaPortPrinterWidth": anxpParaPortPrinterWidth,
       "anxpParaPortInterface": anxpParaPortInterface,
       "anxpParaPortSpeed": anxpParaPortSpeed,
       "annexconfig": annexconfig,
       "anxInetAddr": anxInetAddr,
       "anxPrefLoadAddr": anxPrefLoadAddr,
       "anxPrefDumpAddr": anxPrefDumpAddr,
       "anxLoadDumpGateway": anxLoadDumpGateway,
       "anxLoadDumpSeq": anxLoadDumpSeq,
       "anxLoadBcast": anxLoadBcast,
       "anxServerCap": anxServerCap,
       "anxTimeBcast": anxTimeBcast,
       "anxBcastAddr": anxBcastAddr,
       "anxSubnetMask": anxSubnetMask,
       "anxAuthAgent": anxAuthAgent,
       "anxMaxVcli": anxMaxVcli,
       "anxIpEncapType": anxIpEncapType,
       "anxNameServer1Type": anxNameServer1Type,
       "anxNameServer1Addr": anxNameServer1Addr,
       "anxNameServer2Type": anxNameServer2Type,
       "anxNameServer2Addr": anxNameServer2Addr,
       "anxNameServerBcast": anxNameServerBcast,
       "anxRwhod": anxRwhod,
       "anxMinUniqueHostNames": anxMinUniqueHostNames,
       "anxHostTableSize": anxHostTableSize,
       "anxRouted": anxRouted,
       "anxEnableSecurity": anxEnableSecurity,
       "anxPassword": anxPassword,
       "anxSecurServer1Addr": anxSecurServer1Addr,
       "anxSecurServer2Addr": anxSecurServer2Addr,
       "anxNetTurnAround": anxNetTurnAround,
       "anxSecurBcast": anxSecurBcast,
       "anxVcliSecurity": anxVcliSecurity,
       "anxVcliPassword": anxVcliPassword,
       "anxAcpKey": anxAcpKey,
       "anxSysLogMask": anxSysLogMask,
       "anxSysLogFacility": anxSysLogFacility,
       "anxSysLogHost": anxSysLogHost,
       "anxCliPrompt": anxCliPrompt,
       "anxMotdFile": anxMotdFile,
       "anxTftpDirName": anxTftpDirName,
       "anxTftpDumpName": anxTftpDumpName,
       "anxTimeZone": anxTimeZone,
       "anxDaylightSavings": anxDaylightSavings,
       "anxLatKey": anxLatKey,
       "anxCircuitTimer": anxCircuitTimer,
       "anxFacilityNum": anxFacilityNum,
       "anxLatGroupVal": anxLatGroupVal,
       "anxKeepAliveTimer": anxKeepAliveTimer,
       "anxReXmitLimit": anxReXmitLimit,
       "anxServerName": anxServerName,
       "anxServiceLimit": anxServiceLimit,
       "anxConfigFile": anxConfigFile,
       "anxLatVcliGroupVal": anxLatVcliGroupVal,
       "anxLatQueueMax": anxLatQueueMax,
       "anxLatLocation": anxLatLocation,
       "anxDisabledModules": anxDisabledModules,
       "anxSysLogPort": anxSysLogPort,
       "annexcmds": annexcmds,
       "anxcBoot": anxcBoot,
       "anxcBootImage": anxcBootImage,
       "anxcBootTime": anxcBootTime,
       "anxcBootMsg": anxcBootMsg,
       "anxcReset": anxcReset,
       "anxcBcast": anxcBcast,
       "anxcBcastMsg": anxcBcastMsg}
)
