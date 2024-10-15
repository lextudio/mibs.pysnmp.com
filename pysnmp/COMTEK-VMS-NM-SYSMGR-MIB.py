# SNMP MIB module (COMTEK-VMS-NM-SYSMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COMTEK-VMS-NM-SYSMGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:53 2024
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

_Comtek_ObjectIdentity = ObjectIdentity
comtek = _Comtek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597)
)
_ComtekVms_ObjectIdentity = ObjectIdentity
comtekVms = _ComtekVms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4)
)
_ComtekVmsNMSysMgrMib_ObjectIdentity = ObjectIdentity
comtekVmsNMSysMgrMib = _ComtekVmsNMSysMgrMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3)
)
_SResources_ObjectIdentity = ObjectIdentity
sResources = _SResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1)
)
_SSyi_ObjectIdentity = ObjectIdentity
sSyi = _SSyi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1)
)


class _SSyiNodeName_Type(DisplayString):
    """Custom type sSyiNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SSyiNodeName_Type.__name__ = "DisplayString"
_SSyiNodeName_Object = MibScalar
sSyiNodeName = _SSyiNodeName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 1),
    _SSyiNodeName_Type()
)
sSyiNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiNodeName.setStatus("mandatory")


class _SSyiHwName_Type(DisplayString):
    """Custom type sSyiHwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SSyiHwName_Type.__name__ = "DisplayString"
_SSyiHwName_Object = MibScalar
sSyiHwName = _SSyiHwName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 2),
    _SSyiHwName_Type()
)
sSyiHwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiHwName.setStatus("mandatory")


class _SSyiBootTime_Type(DisplayString):
    """Custom type sSyiBootTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(23, 23),
    )


_SSyiBootTime_Type.__name__ = "DisplayString"
_SSyiBootTime_Object = MibScalar
sSyiBootTime = _SSyiBootTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 3),
    _SSyiBootTime_Type()
)
sSyiBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiBootTime.setStatus("mandatory")


class _SSyiVersion_Type(DisplayString):
    """Custom type sSyiVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SSyiVersion_Type.__name__ = "DisplayString"
_SSyiVersion_Object = MibScalar
sSyiVersion = _SSyiVersion_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 4),
    _SSyiVersion_Type()
)
sSyiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiVersion.setStatus("mandatory")
_SSyiMemSize_Type = Integer32
_SSyiMemSize_Object = MibScalar
sSyiMemSize = _SSyiMemSize_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 5),
    _SSyiMemSize_Type()
)
sSyiMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiMemSize.setStatus("mandatory")
_SSyiAvailCpuCnt_Type = Integer32
_SSyiAvailCpuCnt_Object = MibScalar
sSyiAvailCpuCnt = _SSyiAvailCpuCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 6),
    _SSyiAvailCpuCnt_Type()
)
sSyiAvailCpuCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiAvailCpuCnt.setStatus("mandatory")
_SSyiActiveCpuCnt_Type = Integer32
_SSyiActiveCpuCnt_Object = MibScalar
sSyiActiveCpuCnt = _SSyiActiveCpuCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 7),
    _SSyiActiveCpuCnt_Type()
)
sSyiActiveCpuCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiActiveCpuCnt.setStatus("mandatory")
_SSyiPgSize_Type = Integer32
_SSyiPgSize_Object = MibScalar
sSyiPgSize = _SSyiPgSize_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 8),
    _SSyiPgSize_Type()
)
sSyiPgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiPgSize.setStatus("mandatory")
_SSyiPgFree_Type = Integer32
_SSyiPgFree_Object = MibScalar
sSyiPgFree = _SSyiPgFree_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 9),
    _SSyiPgFree_Type()
)
sSyiPgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiPgFree.setStatus("mandatory")


class _SSyiPgUsedPercent_Type(Integer32):
    """Custom type sSyiPgUsedPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SSyiPgUsedPercent_Type.__name__ = "Integer32"
_SSyiPgUsedPercent_Object = MibScalar
sSyiPgUsedPercent = _SSyiPgUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 10),
    _SSyiPgUsedPercent_Type()
)
sSyiPgUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiPgUsedPercent.setStatus("mandatory")
_SSyiSwpSize_Type = Integer32
_SSyiSwpSize_Object = MibScalar
sSyiSwpSize = _SSyiSwpSize_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 11),
    _SSyiSwpSize_Type()
)
sSyiSwpSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiSwpSize.setStatus("mandatory")
_SSyiSwpFree_Type = Integer32
_SSyiSwpFree_Object = MibScalar
sSyiSwpFree = _SSyiSwpFree_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 12),
    _SSyiSwpFree_Type()
)
sSyiSwpFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiSwpFree.setStatus("mandatory")


class _SSyiSwpUsedPercent_Type(Integer32):
    """Custom type sSyiSwpUsedPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SSyiSwpUsedPercent_Type.__name__ = "Integer32"
_SSyiSwpUsedPercent_Object = MibScalar
sSyiSwpUsedPercent = _SSyiSwpUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 13),
    _SSyiSwpUsedPercent_Type()
)
sSyiSwpUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiSwpUsedPercent.setStatus("mandatory")
_SSyiCpuPgSize_Type = Integer32
_SSyiCpuPgSize_Object = MibScalar
sSyiCpuPgSize = _SSyiCpuPgSize_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 14),
    _SSyiCpuPgSize_Type()
)
sSyiCpuPgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiCpuPgSize.setStatus("mandatory")
_SSyiTime_Type = TimeTicks
_SSyiTime_Object = MibScalar
sSyiTime = _SSyiTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 15),
    _SSyiTime_Type()
)
sSyiTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiTime.setStatus("mandatory")
_SSyiMemFreePg_Type = Integer32
_SSyiMemFreePg_Object = MibScalar
sSyiMemFreePg = _SSyiMemFreePg_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 16),
    _SSyiMemFreePg_Type()
)
sSyiMemFreePg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiMemFreePg.setStatus("mandatory")
_SSyiMemUsed_Type = Integer32
_SSyiMemUsed_Object = MibScalar
sSyiMemUsed = _SSyiMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 1, 17),
    _SSyiMemUsed_Type()
)
sSyiMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSyiMemUsed.setStatus("mandatory")
_SCpu_ObjectIdentity = ObjectIdentity
sCpu = _SCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2)
)


class _SCpuPercentUsed_Type(Integer32):
    """Custom type sCpuPercentUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SCpuPercentUsed_Type.__name__ = "Integer32"
_SCpuPercentUsed_Object = MibScalar
sCpuPercentUsed = _SCpuPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 1),
    _SCpuPercentUsed_Type()
)
sCpuPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCpuPercentUsed.setStatus("mandatory")


class _SIntPercentUsed_Type(Integer32):
    """Custom type sIntPercentUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SIntPercentUsed_Type.__name__ = "Integer32"
_SIntPercentUsed_Object = MibScalar
sIntPercentUsed = _SIntPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 2),
    _SIntPercentUsed_Type()
)
sIntPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sIntPercentUsed.setStatus("mandatory")
_SCpuTicks_Type = Integer32
_SCpuTicks_Object = MibScalar
sCpuTicks = _SCpuTicks_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 3),
    _SCpuTicks_Type()
)
sCpuTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCpuTicks.setStatus("mandatory")
_SCpuLoadOneMinute_ObjectIdentity = ObjectIdentity
sCpuLoadOneMinute = _SCpuLoadOneMinute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 4)
)
_SKernelOne_Type = Integer32
_SKernelOne_Object = MibScalar
sKernelOne = _SKernelOne_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 4, 1),
    _SKernelOne_Type()
)
sKernelOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKernelOne.setStatus("mandatory")
_SExecOne_Type = Integer32
_SExecOne_Object = MibScalar
sExecOne = _SExecOne_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 4, 2),
    _SExecOne_Type()
)
sExecOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sExecOne.setStatus("mandatory")
_SSuprOne_Type = Integer32
_SSuprOne_Object = MibScalar
sSuprOne = _SSuprOne_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 4, 3),
    _SSuprOne_Type()
)
sSuprOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSuprOne.setStatus("mandatory")
_SUserOne_Type = Integer32
_SUserOne_Object = MibScalar
sUserOne = _SUserOne_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 4, 4),
    _SUserOne_Type()
)
sUserOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUserOne.setStatus("mandatory")
_SIntrOne_Type = Integer32
_SIntrOne_Object = MibScalar
sIntrOne = _SIntrOne_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 4, 5),
    _SIntrOne_Type()
)
sIntrOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sIntrOne.setStatus("mandatory")
_SCompOne_Type = Integer32
_SCompOne_Object = MibScalar
sCompOne = _SCompOne_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 4, 6),
    _SCompOne_Type()
)
sCompOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCompOne.setStatus("mandatory")
_SSpinOne_Type = Integer32
_SSpinOne_Object = MibScalar
sSpinOne = _SSpinOne_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 4, 7),
    _SSpinOne_Type()
)
sSpinOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSpinOne.setStatus("mandatory")
_SNullOne_Type = Integer32
_SNullOne_Object = MibScalar
sNullOne = _SNullOne_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 4, 8),
    _SNullOne_Type()
)
sNullOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNullOne.setStatus("mandatory")
_SCpuLoadFiveMinute_ObjectIdentity = ObjectIdentity
sCpuLoadFiveMinute = _SCpuLoadFiveMinute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 5)
)
_SKernelFive_Type = Integer32
_SKernelFive_Object = MibScalar
sKernelFive = _SKernelFive_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 5, 1),
    _SKernelFive_Type()
)
sKernelFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKernelFive.setStatus("mandatory")
_SExecFive_Type = Integer32
_SExecFive_Object = MibScalar
sExecFive = _SExecFive_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 5, 2),
    _SExecFive_Type()
)
sExecFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sExecFive.setStatus("mandatory")
_SSuprFive_Type = Integer32
_SSuprFive_Object = MibScalar
sSuprFive = _SSuprFive_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 5, 3),
    _SSuprFive_Type()
)
sSuprFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSuprFive.setStatus("mandatory")
_SUserFive_Type = Integer32
_SUserFive_Object = MibScalar
sUserFive = _SUserFive_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 5, 4),
    _SUserFive_Type()
)
sUserFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUserFive.setStatus("mandatory")
_SIntrFive_Type = Integer32
_SIntrFive_Object = MibScalar
sIntrFive = _SIntrFive_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 5, 5),
    _SIntrFive_Type()
)
sIntrFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sIntrFive.setStatus("mandatory")
_SCompFive_Type = Integer32
_SCompFive_Object = MibScalar
sCompFive = _SCompFive_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 5, 6),
    _SCompFive_Type()
)
sCompFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCompFive.setStatus("mandatory")
_SSpinFive_Type = Integer32
_SSpinFive_Object = MibScalar
sSpinFive = _SSpinFive_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 5, 7),
    _SSpinFive_Type()
)
sSpinFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSpinFive.setStatus("mandatory")
_SNullFive_Type = Integer32
_SNullFive_Object = MibScalar
sNullFive = _SNullFive_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 5, 8),
    _SNullFive_Type()
)
sNullFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNullFive.setStatus("mandatory")
_SCpuLoadFifteenMinute_ObjectIdentity = ObjectIdentity
sCpuLoadFifteenMinute = _SCpuLoadFifteenMinute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 6)
)
_SKernelFifteen_Type = Integer32
_SKernelFifteen_Object = MibScalar
sKernelFifteen = _SKernelFifteen_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 6, 1),
    _SKernelFifteen_Type()
)
sKernelFifteen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sKernelFifteen.setStatus("mandatory")
_SExecFifteen_Type = Integer32
_SExecFifteen_Object = MibScalar
sExecFifteen = _SExecFifteen_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 6, 2),
    _SExecFifteen_Type()
)
sExecFifteen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sExecFifteen.setStatus("mandatory")
_SSuprFifteen_Type = Integer32
_SSuprFifteen_Object = MibScalar
sSuprFifteen = _SSuprFifteen_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 6, 3),
    _SSuprFifteen_Type()
)
sSuprFifteen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSuprFifteen.setStatus("mandatory")
_SUserFifteen_Type = Integer32
_SUserFifteen_Object = MibScalar
sUserFifteen = _SUserFifteen_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 6, 4),
    _SUserFifteen_Type()
)
sUserFifteen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUserFifteen.setStatus("mandatory")
_SIntrFifteen_Type = Integer32
_SIntrFifteen_Object = MibScalar
sIntrFifteen = _SIntrFifteen_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 6, 5),
    _SIntrFifteen_Type()
)
sIntrFifteen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sIntrFifteen.setStatus("mandatory")
_SCompFifteen_Type = Integer32
_SCompFifteen_Object = MibScalar
sCompFifteen = _SCompFifteen_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 6, 6),
    _SCompFifteen_Type()
)
sCompFifteen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCompFifteen.setStatus("mandatory")
_SSpinFifteen_Type = Integer32
_SSpinFifteen_Object = MibScalar
sSpinFifteen = _SSpinFifteen_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 6, 7),
    _SSpinFifteen_Type()
)
sSpinFifteen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSpinFifteen.setStatus("mandatory")
_SNullFifteen_Type = Integer32
_SNullFifteen_Object = MibScalar
sNullFifteen = _SNullFifteen_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 2, 6, 8),
    _SNullFifteen_Type()
)
sNullFifteen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNullFifteen.setStatus("mandatory")
_SDsk_ObjectIdentity = ObjectIdentity
sDsk = _SDsk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3)
)
_SDskTblCnt_Type = Integer32
_SDskTblCnt_Object = MibScalar
sDskTblCnt = _SDskTblCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 1),
    _SDskTblCnt_Type()
)
sDskTblCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskTblCnt.setStatus("mandatory")
_SDskTblTime_Type = TimeTicks
_SDskTblTime_Object = MibScalar
sDskTblTime = _SDskTblTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 2),
    _SDskTblTime_Type()
)
sDskTblTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskTblTime.setStatus("mandatory")
_SDskTbl_Object = MibTable
sDskTbl = _SDskTbl_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    sDskTbl.setStatus("mandatory")
_SDskEntry_Object = MibTableRow
sDskEntry = _SDskEntry_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1)
)
sDskEntry.setIndexNames(
    (0, "COMTEK-VMS-NM-SYSMGR-MIB", "sDskIndex"),
)
if mibBuilder.loadTexts:
    sDskEntry.setStatus("mandatory")
_SDskIndex_Type = Integer32
_SDskIndex_Object = MibTableColumn
sDskIndex = _SDskIndex_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 1),
    _SDskIndex_Type()
)
sDskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskIndex.setStatus("mandatory")


class _SDskName_Type(DisplayString):
    """Custom type sDskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SDskName_Type.__name__ = "DisplayString"
_SDskName_Object = MibTableColumn
sDskName = _SDskName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 2),
    _SDskName_Type()
)
sDskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskName.setStatus("mandatory")
_SDskUsedPercent_Type = Integer32
_SDskUsedPercent_Object = MibTableColumn
sDskUsedPercent = _SDskUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 3),
    _SDskUsedPercent_Type()
)
sDskUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskUsedPercent.setStatus("mandatory")
_SDskOps_Type = Integer32
_SDskOps_Object = MibTableColumn
sDskOps = _SDskOps_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 4),
    _SDskOps_Type()
)
sDskOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskOps.setStatus("mandatory")
_SDskMountCnt_Type = Integer32
_SDskMountCnt_Object = MibTableColumn
sDskMountCnt = _SDskMountCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 5),
    _SDskMountCnt_Type()
)
sDskMountCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskMountCnt.setStatus("mandatory")
_SDskRefCnt_Type = Integer32
_SDskRefCnt_Object = MibTableColumn
sDskRefCnt = _SDskRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 6),
    _SDskRefCnt_Type()
)
sDskRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskRefCnt.setStatus("mandatory")
_SDskTransCnt_Type = Integer32
_SDskTransCnt_Object = MibTableColumn
sDskTransCnt = _SDskTransCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 7),
    _SDskTransCnt_Type()
)
sDskTransCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskTransCnt.setStatus("mandatory")


class _SDskMediaName_Type(DisplayString):
    """Custom type sDskMediaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SDskMediaName_Type.__name__ = "DisplayString"
_SDskMediaName_Object = MibTableColumn
sDskMediaName = _SDskMediaName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 8),
    _SDskMediaName_Type()
)
sDskMediaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskMediaName.setStatus("mandatory")
_SDskOpCnt_Type = Integer32
_SDskOpCnt_Object = MibTableColumn
sDskOpCnt = _SDskOpCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 9),
    _SDskOpCnt_Type()
)
sDskOpCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskOpCnt.setStatus("mandatory")
_SDskFreeBlocks_Type = Integer32
_SDskFreeBlocks_Object = MibTableColumn
sDskFreeBlocks = _SDskFreeBlocks_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 10),
    _SDskFreeBlocks_Type()
)
sDskFreeBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskFreeBlocks.setStatus("mandatory")
_SDskMaxBlocks_Type = Integer32
_SDskMaxBlocks_Object = MibTableColumn
sDskMaxBlocks = _SDskMaxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 11),
    _SDskMaxBlocks_Type()
)
sDskMaxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskMaxBlocks.setStatus("mandatory")
_SDskStatus_Type = Integer32
_SDskStatus_Object = MibTableColumn
sDskStatus = _SDskStatus_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 12),
    _SDskStatus_Type()
)
sDskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskStatus.setStatus("mandatory")
_SDskDevChar_Type = Integer32
_SDskDevChar_Object = MibTableColumn
sDskDevChar = _SDskDevChar_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 13),
    _SDskDevChar_Type()
)
sDskDevChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskDevChar.setStatus("mandatory")


class _SDskLogVolName_Type(DisplayString):
    """Custom type sDskLogVolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SDskLogVolName_Type.__name__ = "DisplayString"
_SDskLogVolName_Object = MibTableColumn
sDskLogVolName = _SDskLogVolName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 14),
    _SDskLogVolName_Type()
)
sDskLogVolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskLogVolName.setStatus("mandatory")


class _SDskTrapPercent_Type(Integer32):
    """Custom type sDskTrapPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SDskTrapPercent_Type.__name__ = "Integer32"
_SDskTrapPercent_Object = MibTableColumn
sDskTrapPercent = _SDskTrapPercent_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 15),
    _SDskTrapPercent_Type()
)
sDskTrapPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskTrapPercent.setStatus("mandatory")
_SDskTrapBlocks_Type = Integer32
_SDskTrapBlocks_Object = MibTableColumn
sDskTrapBlocks = _SDskTrapBlocks_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 16),
    _SDskTrapBlocks_Type()
)
sDskTrapBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskTrapBlocks.setStatus("mandatory")
_SDskShdCount_Type = Counter32
_SDskShdCount_Object = MibTableColumn
sDskShdCount = _SDskShdCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 17),
    _SDskShdCount_Type()
)
sDskShdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskShdCount.setStatus("mandatory")
_SDskTrapOpSec_Type = Integer32
_SDskTrapOpSec_Object = MibTableColumn
sDskTrapOpSec = _SDskTrapOpSec_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 18),
    _SDskTrapOpSec_Type()
)
sDskTrapOpSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskTrapOpSec.setStatus("mandatory")
_SDskQueueLength_Type = Integer32
_SDskQueueLength_Object = MibTableColumn
sDskQueueLength = _SDskQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 19),
    _SDskQueueLength_Type()
)
sDskQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskQueueLength.setStatus("mandatory")


class _SDskRemote_Type(Integer32):
    """Custom type sDskRemote based on Integer32"""
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


_SDskRemote_Type.__name__ = "Integer32"
_SDskRemote_Object = MibTableColumn
sDskRemote = _SDskRemote_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 3, 3, 1, 20),
    _SDskRemote_Type()
)
sDskRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sDskRemote.setStatus("mandatory")
_SShd_ObjectIdentity = ObjectIdentity
sShd = _SShd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 4)
)
_SShdTbl_Object = MibTable
sShdTbl = _SShdTbl_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sShdTbl.setStatus("mandatory")
_SShdEntry_Object = MibTableRow
sShdEntry = _SShdEntry_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 4, 1, 1)
)
sShdEntry.setIndexNames(
    (0, "COMTEK-VMS-NM-SYSMGR-MIB", "sDskIndex"),
    (0, "COMTEK-VMS-NM-SYSMGR-MIB", "sShdIndex"),
)
if mibBuilder.loadTexts:
    sShdEntry.setStatus("mandatory")
_SShdIndex_Type = Integer32
_SShdIndex_Object = MibTableColumn
sShdIndex = _SShdIndex_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 4, 1, 1, 1),
    _SShdIndex_Type()
)
sShdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sShdIndex.setStatus("mandatory")


class _SShdName_Type(DisplayString):
    """Custom type sShdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SShdName_Type.__name__ = "DisplayString"
_SShdName_Object = MibTableColumn
sShdName = _SShdName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 4, 1, 1, 2),
    _SShdName_Type()
)
sShdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sShdName.setStatus("mandatory")


class _SShdFail_Type(Integer32):
    """Custom type sShdFail based on Integer32"""
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


_SShdFail_Type.__name__ = "Integer32"
_SShdFail_Object = MibTableColumn
sShdFail = _SShdFail_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 4, 1, 1, 3),
    _SShdFail_Type()
)
sShdFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sShdFail.setStatus("mandatory")


class _SShdCopy_Type(Integer32):
    """Custom type sShdCopy based on Integer32"""
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


_SShdCopy_Type.__name__ = "Integer32"
_SShdCopy_Object = MibTableColumn
sShdCopy = _SShdCopy_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 4, 1, 1, 4),
    _SShdCopy_Type()
)
sShdCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sShdCopy.setStatus("mandatory")


class _SShdMerge_Type(Integer32):
    """Custom type sShdMerge based on Integer32"""
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


_SShdMerge_Type.__name__ = "Integer32"
_SShdMerge_Object = MibTableColumn
sShdMerge = _SShdMerge_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 4, 1, 1, 5),
    _SShdMerge_Type()
)
sShdMerge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sShdMerge.setStatus("mandatory")
_SQue_ObjectIdentity = ObjectIdentity
sQue = _SQue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5)
)
_SQueCnt_Type = Integer32
_SQueCnt_Object = MibScalar
sQueCnt = _SQueCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 1),
    _SQueCnt_Type()
)
sQueCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueCnt.setStatus("mandatory")
_SQueTime_Type = TimeTicks
_SQueTime_Object = MibScalar
sQueTime = _SQueTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 2),
    _SQueTime_Type()
)
sQueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueTime.setStatus("mandatory")
_SQTbl_Object = MibTable
sQTbl = _SQTbl_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    sQTbl.setStatus("mandatory")
_SQTblEntry_Object = MibTableRow
sQTblEntry = _SQTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 3, 1)
)
sQTblEntry.setIndexNames(
    (0, "COMTEK-VMS-NM-SYSMGR-MIB", "sQIndex"),
)
if mibBuilder.loadTexts:
    sQTblEntry.setStatus("mandatory")
_SQIndex_Type = Integer32
_SQIndex_Object = MibTableColumn
sQIndex = _SQIndex_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 3, 1, 1),
    _SQIndex_Type()
)
sQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQIndex.setStatus("mandatory")


class _SQName_Type(DisplayString):
    """Custom type sQName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SQName_Type.__name__ = "DisplayString"
_SQName_Object = MibTableColumn
sQName = _SQName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 3, 1, 2),
    _SQName_Type()
)
sQName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQName.setStatus("mandatory")


class _SQMonitor_Type(Integer32):
    """Custom type sQMonitor based on Integer32"""
    defaultValue = 1

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


_SQMonitor_Type.__name__ = "Integer32"
_SQMonitor_Object = MibTableColumn
sQMonitor = _SQMonitor_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 3, 1, 3),
    _SQMonitor_Type()
)
sQMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sQMonitor.setStatus("mandatory")
_SQStatus_Type = Integer32
_SQStatus_Object = MibTableColumn
sQStatus = _SQStatus_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 3, 1, 4),
    _SQStatus_Type()
)
sQStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQStatus.setStatus("mandatory")
_SQEntryCount_Type = Integer32
_SQEntryCount_Object = MibTableColumn
sQEntryCount = _SQEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 3, 1, 5),
    _SQEntryCount_Type()
)
sQEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQEntryCount.setStatus("mandatory")
_SQEntryTbl_Object = MibTable
sQEntryTbl = _SQEntryTbl_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 4)
)
if mibBuilder.loadTexts:
    sQEntryTbl.setStatus("mandatory")
_SQEntry_Object = MibTableRow
sQEntry = _SQEntry_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 4, 1)
)
sQEntry.setIndexNames(
    (0, "COMTEK-VMS-NM-SYSMGR-MIB", "sQIndex"),
    (0, "COMTEK-VMS-NM-SYSMGR-MIB", "sQEntryNum"),
)
if mibBuilder.loadTexts:
    sQEntry.setStatus("mandatory")
_SQEntryNum_Type = Integer32
_SQEntryNum_Object = MibTableColumn
sQEntryNum = _SQEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 4, 1, 1),
    _SQEntryNum_Type()
)
sQEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQEntryNum.setStatus("mandatory")


class _SQEntryJobname_Type(DisplayString):
    """Custom type sQEntryJobname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_SQEntryJobname_Type.__name__ = "DisplayString"
_SQEntryJobname_Object = MibTableColumn
sQEntryJobname = _SQEntryJobname_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 4, 1, 2),
    _SQEntryJobname_Type()
)
sQEntryJobname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQEntryJobname.setStatus("mandatory")
_SQEntryJobStatus_Type = Integer32
_SQEntryJobStatus_Object = MibTableColumn
sQEntryJobStatus = _SQEntryJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 4, 1, 3),
    _SQEntryJobStatus_Type()
)
sQEntryJobStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQEntryJobStatus.setStatus("mandatory")
_SQueBatch_ObjectIdentity = ObjectIdentity
sQueBatch = _SQueBatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 5)
)
_SQueBatchPending_Type = Integer32
_SQueBatchPending_Object = MibScalar
sQueBatchPending = _SQueBatchPending_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 5, 1),
    _SQueBatchPending_Type()
)
sQueBatchPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueBatchPending.setStatus("mandatory")
_SQueBatchExecuting_Type = Integer32
_SQueBatchExecuting_Object = MibScalar
sQueBatchExecuting = _SQueBatchExecuting_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 5, 2),
    _SQueBatchExecuting_Type()
)
sQueBatchExecuting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueBatchExecuting.setStatus("mandatory")
_SQueBatchTimed_Type = Integer32
_SQueBatchTimed_Object = MibScalar
sQueBatchTimed = _SQueBatchTimed_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 5, 3),
    _SQueBatchTimed_Type()
)
sQueBatchTimed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueBatchTimed.setStatus("mandatory")
_SQueBatchHolding_Type = Integer32
_SQueBatchHolding_Object = MibScalar
sQueBatchHolding = _SQueBatchHolding_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 5, 4),
    _SQueBatchHolding_Type()
)
sQueBatchHolding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueBatchHolding.setStatus("mandatory")
_SQueBatchRetained_Type = Integer32
_SQueBatchRetained_Object = MibScalar
sQueBatchRetained = _SQueBatchRetained_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 5, 5),
    _SQueBatchRetained_Type()
)
sQueBatchRetained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueBatchRetained.setStatus("mandatory")
_SQueGeneric_ObjectIdentity = ObjectIdentity
sQueGeneric = _SQueGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 6)
)
_SQueGenericPending_Type = Integer32
_SQueGenericPending_Object = MibScalar
sQueGenericPending = _SQueGenericPending_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 6, 1),
    _SQueGenericPending_Type()
)
sQueGenericPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueGenericPending.setStatus("mandatory")
_SQueGenericExecuting_Type = Integer32
_SQueGenericExecuting_Object = MibScalar
sQueGenericExecuting = _SQueGenericExecuting_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 6, 2),
    _SQueGenericExecuting_Type()
)
sQueGenericExecuting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueGenericExecuting.setStatus("mandatory")
_SQueGenericTimed_Type = Integer32
_SQueGenericTimed_Object = MibScalar
sQueGenericTimed = _SQueGenericTimed_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 6, 3),
    _SQueGenericTimed_Type()
)
sQueGenericTimed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueGenericTimed.setStatus("mandatory")
_SQueGenericHolding_Type = Integer32
_SQueGenericHolding_Object = MibScalar
sQueGenericHolding = _SQueGenericHolding_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 6, 4),
    _SQueGenericHolding_Type()
)
sQueGenericHolding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueGenericHolding.setStatus("mandatory")
_SQueGenericRetained_Type = Integer32
_SQueGenericRetained_Object = MibScalar
sQueGenericRetained = _SQueGenericRetained_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 6, 5),
    _SQueGenericRetained_Type()
)
sQueGenericRetained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueGenericRetained.setStatus("mandatory")
_SQuePrinter_ObjectIdentity = ObjectIdentity
sQuePrinter = _SQuePrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 7)
)
_SQuePrinterPending_Type = Integer32
_SQuePrinterPending_Object = MibScalar
sQuePrinterPending = _SQuePrinterPending_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 7, 1),
    _SQuePrinterPending_Type()
)
sQuePrinterPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQuePrinterPending.setStatus("mandatory")
_SQuePrinterExecuting_Type = Integer32
_SQuePrinterExecuting_Object = MibScalar
sQuePrinterExecuting = _SQuePrinterExecuting_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 7, 2),
    _SQuePrinterExecuting_Type()
)
sQuePrinterExecuting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQuePrinterExecuting.setStatus("mandatory")
_SQuePrinterTimed_Type = Integer32
_SQuePrinterTimed_Object = MibScalar
sQuePrinterTimed = _SQuePrinterTimed_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 7, 3),
    _SQuePrinterTimed_Type()
)
sQuePrinterTimed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQuePrinterTimed.setStatus("mandatory")
_SQuePrinterHolding_Type = Integer32
_SQuePrinterHolding_Object = MibScalar
sQuePrinterHolding = _SQuePrinterHolding_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 7, 4),
    _SQuePrinterHolding_Type()
)
sQuePrinterHolding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQuePrinterHolding.setStatus("mandatory")
_SQuePrinterRetained_Type = Integer32
_SQuePrinterRetained_Object = MibScalar
sQuePrinterRetained = _SQuePrinterRetained_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 7, 5),
    _SQuePrinterRetained_Type()
)
sQuePrinterRetained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQuePrinterRetained.setStatus("mandatory")
_SQueServer_ObjectIdentity = ObjectIdentity
sQueServer = _SQueServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 8)
)
_SQueServerPending_Type = Integer32
_SQueServerPending_Object = MibScalar
sQueServerPending = _SQueServerPending_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 8, 1),
    _SQueServerPending_Type()
)
sQueServerPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueServerPending.setStatus("mandatory")
_SQueServerExecuting_Type = Integer32
_SQueServerExecuting_Object = MibScalar
sQueServerExecuting = _SQueServerExecuting_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 8, 2),
    _SQueServerExecuting_Type()
)
sQueServerExecuting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueServerExecuting.setStatus("mandatory")
_SQueServerTimed_Type = Integer32
_SQueServerTimed_Object = MibScalar
sQueServerTimed = _SQueServerTimed_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 8, 3),
    _SQueServerTimed_Type()
)
sQueServerTimed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueServerTimed.setStatus("mandatory")
_SQueServerHolding_Type = Integer32
_SQueServerHolding_Object = MibScalar
sQueServerHolding = _SQueServerHolding_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 8, 4),
    _SQueServerHolding_Type()
)
sQueServerHolding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueServerHolding.setStatus("mandatory")
_SQueServerRetained_Type = Integer32
_SQueServerRetained_Object = MibScalar
sQueServerRetained = _SQueServerRetained_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 8, 5),
    _SQueServerRetained_Type()
)
sQueServerRetained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueServerRetained.setStatus("mandatory")
_SQueSymbiont_ObjectIdentity = ObjectIdentity
sQueSymbiont = _SQueSymbiont_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 9)
)
_SQueSymbiontPending_Type = Integer32
_SQueSymbiontPending_Object = MibScalar
sQueSymbiontPending = _SQueSymbiontPending_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 9, 1),
    _SQueSymbiontPending_Type()
)
sQueSymbiontPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueSymbiontPending.setStatus("mandatory")
_SQueSymbiontExecuting_Type = Integer32
_SQueSymbiontExecuting_Object = MibScalar
sQueSymbiontExecuting = _SQueSymbiontExecuting_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 9, 2),
    _SQueSymbiontExecuting_Type()
)
sQueSymbiontExecuting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueSymbiontExecuting.setStatus("mandatory")
_SQueSymbiontTimed_Type = Integer32
_SQueSymbiontTimed_Object = MibScalar
sQueSymbiontTimed = _SQueSymbiontTimed_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 9, 3),
    _SQueSymbiontTimed_Type()
)
sQueSymbiontTimed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueSymbiontTimed.setStatus("mandatory")
_SQueSymbiontHolding_Type = Integer32
_SQueSymbiontHolding_Object = MibScalar
sQueSymbiontHolding = _SQueSymbiontHolding_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 9, 4),
    _SQueSymbiontHolding_Type()
)
sQueSymbiontHolding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueSymbiontHolding.setStatus("mandatory")
_SQueSymbiontRetained_Type = Integer32
_SQueSymbiontRetained_Object = MibScalar
sQueSymbiontRetained = _SQueSymbiontRetained_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 9, 5),
    _SQueSymbiontRetained_Type()
)
sQueSymbiontRetained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueSymbiontRetained.setStatus("mandatory")
_SQueTerminal_ObjectIdentity = ObjectIdentity
sQueTerminal = _SQueTerminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 10)
)
_SQueTerminalPending_Type = Integer32
_SQueTerminalPending_Object = MibScalar
sQueTerminalPending = _SQueTerminalPending_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 10, 1),
    _SQueTerminalPending_Type()
)
sQueTerminalPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueTerminalPending.setStatus("mandatory")
_SQueTerminalExecuting_Type = Integer32
_SQueTerminalExecuting_Object = MibScalar
sQueTerminalExecuting = _SQueTerminalExecuting_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 10, 2),
    _SQueTerminalExecuting_Type()
)
sQueTerminalExecuting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueTerminalExecuting.setStatus("mandatory")
_SQueTerminalTimed_Type = Integer32
_SQueTerminalTimed_Object = MibScalar
sQueTerminalTimed = _SQueTerminalTimed_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 10, 3),
    _SQueTerminalTimed_Type()
)
sQueTerminalTimed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueTerminalTimed.setStatus("mandatory")
_SQueTerminalHolding_Type = Integer32
_SQueTerminalHolding_Object = MibScalar
sQueTerminalHolding = _SQueTerminalHolding_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 10, 4),
    _SQueTerminalHolding_Type()
)
sQueTerminalHolding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueTerminalHolding.setStatus("mandatory")
_SQueTerminalRetained_Type = Integer32
_SQueTerminalRetained_Object = MibScalar
sQueTerminalRetained = _SQueTerminalRetained_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 10, 5),
    _SQueTerminalRetained_Type()
)
sQueTerminalRetained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQueTerminalRetained.setStatus("mandatory")
_SQMan_ObjectIdentity = ObjectIdentity
sQMan = _SQMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 11)
)
_SQManCount_Type = Integer32
_SQManCount_Object = MibScalar
sQManCount = _SQManCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 11, 1),
    _SQManCount_Type()
)
sQManCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQManCount.setStatus("mandatory")
_SQManTbl_Object = MibTable
sQManTbl = _SQManTbl_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 11, 2)
)
if mibBuilder.loadTexts:
    sQManTbl.setStatus("mandatory")
_SQManTblEntry_Object = MibTableRow
sQManTblEntry = _SQManTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 11, 2, 1)
)
sQManTblEntry.setIndexNames(
    (0, "COMTEK-VMS-NM-SYSMGR-MIB", "sQManIndex"),
)
if mibBuilder.loadTexts:
    sQManTblEntry.setStatus("mandatory")
_SQManIndex_Type = Integer32
_SQManIndex_Object = MibTableColumn
sQManIndex = _SQManIndex_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 11, 2, 1, 1),
    _SQManIndex_Type()
)
sQManIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQManIndex.setStatus("mandatory")


class _SQManName_Type(DisplayString):
    """Custom type sQManName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SQManName_Type.__name__ = "DisplayString"
_SQManName_Object = MibTableColumn
sQManName = _SQManName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 11, 2, 1, 2),
    _SQManName_Type()
)
sQManName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQManName.setStatus("mandatory")
_SQManStatus_Type = Integer32
_SQManStatus_Object = MibTableColumn
sQManStatus = _SQManStatus_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 1, 5, 11, 2, 1, 3),
    _SQManStatus_Type()
)
sQManStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sQManStatus.setStatus("mandatory")
_SProcesses_ObjectIdentity = ObjectIdentity
sProcesses = _SProcesses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2)
)
_SProcInfo_ObjectIdentity = ObjectIdentity
sProcInfo = _SProcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1)
)
_SPsCnt_Type = Integer32
_SPsCnt_Object = MibScalar
sPsCnt = _SPsCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 1),
    _SPsCnt_Type()
)
sPsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsCnt.setStatus("mandatory")
_SPsTime_Type = TimeTicks
_SPsTime_Object = MibScalar
sPsTime = _SPsTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 2),
    _SPsTime_Type()
)
sPsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsTime.setStatus("mandatory")
_SPsTbl_Object = MibTable
sPsTbl = _SPsTbl_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    sPsTbl.setStatus("mandatory")
_SPsEntry_Object = MibTableRow
sPsEntry = _SPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1)
)
sPsEntry.setIndexNames(
    (0, "COMTEK-VMS-NM-SYSMGR-MIB", "sPsPID"),
)
if mibBuilder.loadTexts:
    sPsEntry.setStatus("mandatory")
_SPsPID_Type = Integer32
_SPsPID_Object = MibTableColumn
sPsPID = _SPsPID_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 1),
    _SPsPID_Type()
)
sPsPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsPID.setStatus("mandatory")


class _SPsProcName_Type(DisplayString):
    """Custom type sPsProcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SPsProcName_Type.__name__ = "DisplayString"
_SPsProcName_Object = MibTableColumn
sPsProcName = _SPsProcName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 2),
    _SPsProcName_Type()
)
sPsProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsProcName.setStatus("mandatory")


class _SPsState_Type(Integer32):
    """Custom type sPsState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("cef", 3),
          ("colpg", 1),
          ("com", 12),
          ("como", 13),
          ("cur", 14),
          ("fpg", 11),
          ("hib", 7),
          ("hibo", 8),
          ("lef", 5),
          ("lefo", 6),
          ("mwait", 2),
          ("pfw", 4),
          ("susp", 9),
          ("suspo", 10))
    )


_SPsState_Type.__name__ = "Integer32"
_SPsState_Object = MibTableColumn
sPsState = _SPsState_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 3),
    _SPsState_Type()
)
sPsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsState.setStatus("mandatory")


class _SPsPriority_Type(Integer32):
    """Custom type sPsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SPsPriority_Type.__name__ = "Integer32"
_SPsPriority_Object = MibTableColumn
sPsPriority = _SPsPriority_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 4),
    _SPsPriority_Type()
)
sPsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsPriority.setStatus("mandatory")
_SPsDirectIO_Type = Integer32
_SPsDirectIO_Object = MibTableColumn
sPsDirectIO = _SPsDirectIO_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 5),
    _SPsDirectIO_Type()
)
sPsDirectIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsDirectIO.setStatus("mandatory")
_SPsCpuTime_Type = TimeTicks
_SPsCpuTime_Object = MibTableColumn
sPsCpuTime = _SPsCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 6),
    _SPsCpuTime_Type()
)
sPsCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsCpuTime.setStatus("mandatory")
_SPsPgFaults_Type = Integer32
_SPsPgFaults_Object = MibTableColumn
sPsPgFaults = _SPsPgFaults_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 7),
    _SPsPgFaults_Type()
)
sPsPgFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsPgFaults.setStatus("mandatory")
_SPsWorkSetSize_Type = Integer32
_SPsWorkSetSize_Object = MibTableColumn
sPsWorkSetSize = _SPsWorkSetSize_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 8),
    _SPsWorkSetSize_Type()
)
sPsWorkSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsWorkSetSize.setStatus("mandatory")


class _SPsUsername_Type(DisplayString):
    """Custom type sPsUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_SPsUsername_Type.__name__ = "DisplayString"
_SPsUsername_Object = MibTableColumn
sPsUsername = _SPsUsername_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 9),
    _SPsUsername_Type()
)
sPsUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsUsername.setStatus("mandatory")


class _SPsPhysTerm_Type(DisplayString):
    """Custom type sPsPhysTerm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SPsPhysTerm_Type.__name__ = "DisplayString"
_SPsPhysTerm_Object = MibTableColumn
sPsPhysTerm = _SPsPhysTerm_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 10),
    _SPsPhysTerm_Type()
)
sPsPhysTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsPhysTerm.setStatus("mandatory")


class _SPsImageName_Type(DisplayString):
    """Custom type sPsImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SPsImageName_Type.__name__ = "DisplayString"
_SPsImageName_Object = MibTableColumn
sPsImageName = _SPsImageName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 11),
    _SPsImageName_Type()
)
sPsImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsImageName.setStatus("mandatory")
_SPsLoginTime_Type = DisplayString
_SPsLoginTime_Object = MibTableColumn
sPsLoginTime = _SPsLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 12),
    _SPsLoginTime_Type()
)
sPsLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsLoginTime.setStatus("mandatory")
_SPsPgTblCnt_Type = Integer32
_SPsPgTblCnt_Object = MibTableColumn
sPsPgTblCnt = _SPsPgTblCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 13),
    _SPsPgTblCnt_Type()
)
sPsPgTblCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsPgTblCnt.setStatus("mandatory")


class _SPsMode_Type(Integer32):
    """Custom type sPsMode based on Integer32"""
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
        *(("batch", 3),
          ("interactive", 4),
          ("network", 2),
          ("other", 1))
    )


_SPsMode_Type.__name__ = "Integer32"
_SPsMode_Object = MibTableColumn
sPsMode = _SPsMode_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 14),
    _SPsMode_Type()
)
sPsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsMode.setStatus("mandatory")


class _SPsRWState_Type(Integer32):
    """Custom type sPsRWState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              11,
              12,
              13,
              14,
              15,
              16,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("astwait", 1),
          ("clusrv", 16),
          ("clustran", 14),
          ("cpucap", 15),
          ("mailbox", 2),
          ("mplempty", 11),
          ("mpwbusy", 12),
          ("mutex", 19),
          ("npdynmem", 3),
          ("pgdynmem", 5),
          ("pgfile", 4),
          ("psxfrk", 18),
          ("scs", 13))
    )


_SPsRWState_Type.__name__ = "Integer32"
_SPsRWState_Object = MibTableColumn
sPsRWState = _SPsRWState_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 3, 1, 15),
    _SPsRWState_Type()
)
sPsRWState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsRWState.setStatus("mandatory")
_SPsCOMQueue_Type = Integer32
_SPsCOMQueue_Object = MibScalar
sPsCOMQueue = _SPsCOMQueue_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 4),
    _SPsCOMQueue_Type()
)
sPsCOMQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsCOMQueue.setStatus("mandatory")
_SPsCOMOQueue_Type = Integer32
_SPsCOMOQueue_Object = MibScalar
sPsCOMOQueue = _SPsCOMOQueue_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 5),
    _SPsCOMOQueue_Type()
)
sPsCOMOQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsCOMOQueue.setStatus("mandatory")
_SPsOther_Type = Counter32
_SPsOther_Object = MibScalar
sPsOther = _SPsOther_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 6),
    _SPsOther_Type()
)
sPsOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsOther.setStatus("mandatory")
_SPsNetwork_Type = Counter32
_SPsNetwork_Object = MibScalar
sPsNetwork = _SPsNetwork_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 7),
    _SPsNetwork_Type()
)
sPsNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsNetwork.setStatus("mandatory")
_SPsBatch_Type = Counter32
_SPsBatch_Object = MibScalar
sPsBatch = _SPsBatch_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 8),
    _SPsBatch_Type()
)
sPsBatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsBatch.setStatus("mandatory")
_SPsInteractive_Type = Counter32
_SPsInteractive_Object = MibScalar
sPsInteractive = _SPsInteractive_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 9),
    _SPsInteractive_Type()
)
sPsInteractive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsInteractive.setStatus("mandatory")
_SPsAvailProcSlots_Type = Counter32
_SPsAvailProcSlots_Object = MibScalar
sPsAvailProcSlots = _SPsAvailProcSlots_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 1, 10),
    _SPsAvailProcSlots_Type()
)
sPsAvailProcSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sPsAvailProcSlots.setStatus("mandatory")
_SCritInfo_ObjectIdentity = ObjectIdentity
sCritInfo = _SCritInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 2)
)


class _SCritCnt_Type(Integer32):
    """Custom type sCritCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SCritCnt_Type.__name__ = "Integer32"
_SCritCnt_Object = MibScalar
sCritCnt = _SCritCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 2, 1),
    _SCritCnt_Type()
)
sCritCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCritCnt.setStatus("mandatory")
_SCritTime_Type = TimeTicks
_SCritTime_Object = MibScalar
sCritTime = _SCritTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 2, 2),
    _SCritTime_Type()
)
sCritTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCritTime.setStatus("mandatory")
_SCritTbl_Object = MibTable
sCritTbl = _SCritTbl_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    sCritTbl.setStatus("mandatory")
_SCritEntry_Object = MibTableRow
sCritEntry = _SCritEntry_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 2, 3, 1)
)
sCritEntry.setIndexNames(
    (0, "COMTEK-VMS-NM-SYSMGR-MIB", "sCritIndex"),
)
if mibBuilder.loadTexts:
    sCritEntry.setStatus("mandatory")
_SCritIndex_Type = Integer32
_SCritIndex_Object = MibTableColumn
sCritIndex = _SCritIndex_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 2, 3, 1, 1),
    _SCritIndex_Type()
)
sCritIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCritIndex.setStatus("mandatory")


class _SCritName_Type(DisplayString):
    """Custom type sCritName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SCritName_Type.__name__ = "DisplayString"
_SCritName_Object = MibTableColumn
sCritName = _SCritName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 2, 3, 1, 2),
    _SCritName_Type()
)
sCritName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCritName.setStatus("mandatory")
_SCritReqCnt_Type = Integer32
_SCritReqCnt_Object = MibTableColumn
sCritReqCnt = _SCritReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 2, 3, 1, 3),
    _SCritReqCnt_Type()
)
sCritReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCritReqCnt.setStatus("mandatory")
_SCritCurCnt_Type = Integer32
_SCritCurCnt_Object = MibTableColumn
sCritCurCnt = _SCritCurCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 2, 2, 3, 1, 4),
    _SCritCurCnt_Type()
)
sCritCurCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCritCurCnt.setStatus("mandatory")
_STrapInfo_ObjectIdentity = ObjectIdentity
sTrapInfo = _STrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 3)
)
_STrapNextSeqNum_Type = Integer32
_STrapNextSeqNum_Object = MibScalar
sTrapNextSeqNum = _STrapNextSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 3, 1),
    _STrapNextSeqNum_Type()
)
sTrapNextSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTrapNextSeqNum.setStatus("mandatory")
_STrapTime_Type = TimeTicks
_STrapTime_Object = MibScalar
sTrapTime = _STrapTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 3, 2),
    _STrapTime_Type()
)
sTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTrapTime.setStatus("mandatory")
_STrapResendSeqNum_Type = Integer32
_STrapResendSeqNum_Object = MibScalar
sTrapResendSeqNum = _STrapResendSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 3, 3),
    _STrapResendSeqNum_Type()
)
sTrapResendSeqNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTrapResendSeqNum.setStatus("mandatory")
_STrapLastSeqNumSent_Type = Integer32
_STrapLastSeqNumSent_Object = MibScalar
sTrapLastSeqNumSent = _STrapLastSeqNumSent_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 3, 4),
    _STrapLastSeqNumSent_Type()
)
sTrapLastSeqNumSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTrapLastSeqNumSent.setStatus("mandatory")
_STrapLostCount_Type = Counter32
_STrapLostCount_Object = MibScalar
sTrapLostCount = _STrapLostCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 3, 5),
    _STrapLostCount_Type()
)
sTrapLostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTrapLostCount.setStatus("mandatory")
_SErrInfo_ObjectIdentity = ObjectIdentity
sErrInfo = _SErrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4)
)
_SHwErrInfo_ObjectIdentity = ObjectIdentity
sHwErrInfo = _SHwErrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 1)
)
_SHwErrDeviceCnt_Type = Integer32
_SHwErrDeviceCnt_Object = MibScalar
sHwErrDeviceCnt = _SHwErrDeviceCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 1, 1),
    _SHwErrDeviceCnt_Type()
)
sHwErrDeviceCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sHwErrDeviceCnt.setStatus("mandatory")
_SHwErrTime_Type = TimeTicks
_SHwErrTime_Object = MibScalar
sHwErrTime = _SHwErrTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 1, 2),
    _SHwErrTime_Type()
)
sHwErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sHwErrTime.setStatus("mandatory")
_SHwErrTbl_Object = MibTable
sHwErrTbl = _SHwErrTbl_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    sHwErrTbl.setStatus("mandatory")
_SHwErrEntry_Object = MibTableRow
sHwErrEntry = _SHwErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 1, 3, 1)
)
sHwErrEntry.setIndexNames(
    (0, "COMTEK-VMS-NM-SYSMGR-MIB", "sHwErrIndex"),
)
if mibBuilder.loadTexts:
    sHwErrEntry.setStatus("mandatory")
_SHwErrIndex_Type = Integer32
_SHwErrIndex_Object = MibTableColumn
sHwErrIndex = _SHwErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 1, 3, 1, 1),
    _SHwErrIndex_Type()
)
sHwErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sHwErrIndex.setStatus("mandatory")
_SHwErrDeviceName_Type = DisplayString
_SHwErrDeviceName_Object = MibTableColumn
sHwErrDeviceName = _SHwErrDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 1, 3, 1, 2),
    _SHwErrDeviceName_Type()
)
sHwErrDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sHwErrDeviceName.setStatus("mandatory")
_SHwErrCnt_Type = Integer32
_SHwErrCnt_Object = MibTableColumn
sHwErrCnt = _SHwErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 1, 3, 1, 3),
    _SHwErrCnt_Type()
)
sHwErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sHwErrCnt.setStatus("mandatory")
_SHwErrLastTime_Type = TimeTicks
_SHwErrLastTime_Object = MibTableColumn
sHwErrLastTime = _SHwErrLastTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 1, 3, 1, 4),
    _SHwErrLastTime_Type()
)
sHwErrLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sHwErrLastTime.setStatus("mandatory")
_SSwErrInfo_ObjectIdentity = ObjectIdentity
sSwErrInfo = _SSwErrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 2)
)
_SSwErrStatus_Type = Integer32
_SSwErrStatus_Object = MibScalar
sSwErrStatus = _SSwErrStatus_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 2, 1),
    _SSwErrStatus_Type()
)
sSwErrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSwErrStatus.setStatus("mandatory")


class _SSwErrFile_Type(DisplayString):
    """Custom type sSwErrFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SSwErrFile_Type.__name__ = "DisplayString"
_SSwErrFile_Object = MibScalar
sSwErrFile = _SSwErrFile_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 2, 2),
    _SSwErrFile_Type()
)
sSwErrFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSwErrFile.setStatus("mandatory")
_SSwErrLineNum_Type = Integer32
_SSwErrLineNum_Object = MibScalar
sSwErrLineNum = _SSwErrLineNum_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 2, 3),
    _SSwErrLineNum_Type()
)
sSwErrLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSwErrLineNum.setStatus("mandatory")
_SSwErrLastTime_Type = TimeTicks
_SSwErrLastTime_Object = MibScalar
sSwErrLastTime = _SSwErrLastTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 2, 4),
    _SSwErrLastTime_Type()
)
sSwErrLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSwErrLastTime.setStatus("mandatory")
_SSwErrMessage_Type = DisplayString
_SSwErrMessage_Object = MibScalar
sSwErrMessage = _SSwErrMessage_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 2, 5),
    _SSwErrMessage_Type()
)
sSwErrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sSwErrMessage.setStatus("mandatory")


class _SOpcomOne_Type(DisplayString):
    """Custom type sOpcomOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SOpcomOne_Type.__name__ = "DisplayString"
_SOpcomOne_Object = MibScalar
sOpcomOne = _SOpcomOne_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 3),
    _SOpcomOne_Type()
)
sOpcomOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sOpcomOne.setStatus("mandatory")


class _SOpcomTwo_Type(DisplayString):
    """Custom type sOpcomTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SOpcomTwo_Type.__name__ = "DisplayString"
_SOpcomTwo_Object = MibScalar
sOpcomTwo = _SOpcomTwo_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 4),
    _SOpcomTwo_Type()
)
sOpcomTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sOpcomTwo.setStatus("mandatory")


class _SOpcomThree_Type(DisplayString):
    """Custom type sOpcomThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SOpcomThree_Type.__name__ = "DisplayString"
_SOpcomThree_Object = MibScalar
sOpcomThree = _SOpcomThree_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 5),
    _SOpcomThree_Type()
)
sOpcomThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sOpcomThree.setStatus("mandatory")


class _SOpcomFour_Type(DisplayString):
    """Custom type sOpcomFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SOpcomFour_Type.__name__ = "DisplayString"
_SOpcomFour_Object = MibScalar
sOpcomFour = _SOpcomFour_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 6),
    _SOpcomFour_Type()
)
sOpcomFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sOpcomFour.setStatus("mandatory")


class _SOpcomFive_Type(DisplayString):
    """Custom type sOpcomFive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SOpcomFive_Type.__name__ = "DisplayString"
_SOpcomFive_Object = MibScalar
sOpcomFive = _SOpcomFive_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 7),
    _SOpcomFive_Type()
)
sOpcomFive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sOpcomFive.setStatus("mandatory")


class _SOpcomReplyId_Type(Integer32):
    """Custom type sOpcomReplyId based on Integer32"""
    defaultValue = 0


_SOpcomReplyId_Object = MibScalar
sOpcomReplyId = _SOpcomReplyId_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 8),
    _SOpcomReplyId_Type()
)
sOpcomReplyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sOpcomReplyId.setStatus("mandatory")


class _SOpcomReplyStatus_Type(Integer32):
    """Custom type sOpcomReplyStatus based on Integer32"""
    defaultValue = 1

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
        *(("blankTape", 2),
          ("initializeTape", 3),
          ("noStatus", 1),
          ("requestAborted", 6),
          ("requestComplete", 4),
          ("requestPending", 5))
    )


_SOpcomReplyStatus_Type.__name__ = "Integer32"
_SOpcomReplyStatus_Object = MibScalar
sOpcomReplyStatus = _SOpcomReplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 9),
    _SOpcomReplyStatus_Type()
)
sOpcomReplyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sOpcomReplyStatus.setStatus("mandatory")


class _SOpcomReplyText_Type(DisplayString):
    """Custom type sOpcomReplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SOpcomReplyText_Type.__name__ = "DisplayString"
_SOpcomReplyText_Object = MibScalar
sOpcomReplyText = _SOpcomReplyText_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 10),
    _SOpcomReplyText_Type()
)
sOpcomReplyText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sOpcomReplyText.setStatus("mandatory")


class _SOpcomReplySend_Type(Integer32):
    """Custom type sOpcomReplySend based on Integer32"""
    defaultValue = 2

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


_SOpcomReplySend_Type.__name__ = "Integer32"
_SOpcomReplySend_Object = MibScalar
sOpcomReplySend = _SOpcomReplySend_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 11),
    _SOpcomReplySend_Type()
)
sOpcomReplySend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sOpcomReplySend.setStatus("mandatory")


class _SOpcomSix_Type(DisplayString):
    """Custom type sOpcomSix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SOpcomSix_Type.__name__ = "DisplayString"
_SOpcomSix_Object = MibScalar
sOpcomSix = _SOpcomSix_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 12),
    _SOpcomSix_Type()
)
sOpcomSix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sOpcomSix.setStatus("mandatory")


class _SOpcomSeven_Type(DisplayString):
    """Custom type sOpcomSeven based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SOpcomSeven_Type.__name__ = "DisplayString"
_SOpcomSeven_Object = MibScalar
sOpcomSeven = _SOpcomSeven_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 4, 13),
    _SOpcomSeven_Type()
)
sOpcomSeven.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sOpcomSeven.setStatus("mandatory")
_SCfg_ObjectIdentity = ObjectIdentity
sCfg = _SCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5)
)


class _SCfgFile_Type(DisplayString):
    """Custom type sCfgFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SCfgFile_Type.__name__ = "DisplayString"
_SCfgFile_Object = MibScalar
sCfgFile = _SCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 1),
    _SCfgFile_Type()
)
sCfgFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgFile.setStatus("mandatory")


class _SCfgLogFile_Type(DisplayString):
    """Custom type sCfgLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SCfgLogFile_Type.__name__ = "DisplayString"
_SCfgLogFile_Object = MibScalar
sCfgLogFile = _SCfgLogFile_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 2),
    _SCfgLogFile_Type()
)
sCfgLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCfgLogFile.setStatus("mandatory")


class _SCfgCritFile_Type(DisplayString):
    """Custom type sCfgCritFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SCfgCritFile_Type.__name__ = "DisplayString"
_SCfgCritFile_Object = MibScalar
sCfgCritFile = _SCfgCritFile_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 3),
    _SCfgCritFile_Type()
)
sCfgCritFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgCritFile.setStatus("mandatory")


class _SCfgReinitSubagent_Type(Integer32):
    """Custom type sCfgReinitSubagent based on Integer32"""
    defaultValue = 2

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


_SCfgReinitSubagent_Type.__name__ = "Integer32"
_SCfgReinitSubagent_Object = MibScalar
sCfgReinitSubagent = _SCfgReinitSubagent_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 4),
    _SCfgReinitSubagent_Type()
)
sCfgReinitSubagent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgReinitSubagent.setStatus("mandatory")


class _SCfgTraps_Type(Integer32):
    """Custom type sCfgTraps based on Integer32"""
    defaultValue = 1

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


_SCfgTraps_Type.__name__ = "Integer32"
_SCfgTraps_Object = MibScalar
sCfgTraps = _SCfgTraps_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 5),
    _SCfgTraps_Type()
)
sCfgTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgTraps.setStatus("mandatory")


class _SCfgHwErrTraps_Type(Integer32):
    """Custom type sCfgHwErrTraps based on Integer32"""
    defaultValue = 1

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


_SCfgHwErrTraps_Type.__name__ = "Integer32"
_SCfgHwErrTraps_Object = MibScalar
sCfgHwErrTraps = _SCfgHwErrTraps_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 6),
    _SCfgHwErrTraps_Type()
)
sCfgHwErrTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgHwErrTraps.setStatus("mandatory")


class _SCfgCpuLimit_Type(Integer32):
    """Custom type sCfgCpuLimit based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SCfgCpuLimit_Type.__name__ = "Integer32"
_SCfgCpuLimit_Object = MibScalar
sCfgCpuLimit = _SCfgCpuLimit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 7),
    _SCfgCpuLimit_Type()
)
sCfgCpuLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgCpuLimit.setStatus("mandatory")


class _SCfgIntLimit_Type(Integer32):
    """Custom type sCfgIntLimit based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SCfgIntLimit_Type.__name__ = "Integer32"
_SCfgIntLimit_Object = MibScalar
sCfgIntLimit = _SCfgIntLimit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 8),
    _SCfgIntLimit_Type()
)
sCfgIntLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgIntLimit.setStatus("mandatory")


class _SCfgDskOps_Type(Integer32):
    """Custom type sCfgDskOps based on Integer32"""
    defaultValue = 25


_SCfgDskOps_Object = MibScalar
sCfgDskOps = _SCfgDskOps_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 9),
    _SCfgDskOps_Type()
)
sCfgDskOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgDskOps.setStatus("mandatory")


class _SCfgDskLimit_Type(Integer32):
    """Custom type sCfgDskLimit based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SCfgDskLimit_Type.__name__ = "Integer32"
_SCfgDskLimit_Object = MibScalar
sCfgDskLimit = _SCfgDskLimit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 10),
    _SCfgDskLimit_Type()
)
sCfgDskLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgDskLimit.setStatus("mandatory")


class _SCfgPgLimit_Type(Integer32):
    """Custom type sCfgPgLimit based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SCfgPgLimit_Type.__name__ = "Integer32"
_SCfgPgLimit_Object = MibScalar
sCfgPgLimit = _SCfgPgLimit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 11),
    _SCfgPgLimit_Type()
)
sCfgPgLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgPgLimit.setStatus("mandatory")


class _SCfgSwpLimit_Type(Integer32):
    """Custom type sCfgSwpLimit based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SCfgSwpLimit_Type.__name__ = "Integer32"
_SCfgSwpLimit_Object = MibScalar
sCfgSwpLimit = _SCfgSwpLimit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 12),
    _SCfgSwpLimit_Type()
)
sCfgSwpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgSwpLimit.setStatus("mandatory")


class _SCfgPsTimer_Type(Integer32):
    """Custom type sCfgPsTimer based on Integer32"""
    defaultValue = 5


_SCfgPsTimer_Object = MibScalar
sCfgPsTimer = _SCfgPsTimer_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 13),
    _SCfgPsTimer_Type()
)
sCfgPsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgPsTimer.setStatus("mandatory")


class _SCfgDskTimer_Type(Integer32):
    """Custom type sCfgDskTimer based on Integer32"""
    defaultValue = 1


_SCfgDskTimer_Object = MibScalar
sCfgDskTimer = _SCfgDskTimer_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 14),
    _SCfgDskTimer_Type()
)
sCfgDskTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgDskTimer.setStatus("mandatory")


class _SCfgHwErrTimer_Type(Integer32):
    """Custom type sCfgHwErrTimer based on Integer32"""
    defaultValue = 1


_SCfgHwErrTimer_Object = MibScalar
sCfgHwErrTimer = _SCfgHwErrTimer_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 15),
    _SCfgHwErrTimer_Type()
)
sCfgHwErrTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgHwErrTimer.setStatus("mandatory")


class _SCfgSysInfoTimer_Type(Integer32):
    """Custom type sCfgSysInfoTimer based on Integer32"""
    defaultValue = 1


_SCfgSysInfoTimer_Object = MibScalar
sCfgSysInfoTimer = _SCfgSysInfoTimer_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 16),
    _SCfgSysInfoTimer_Type()
)
sCfgSysInfoTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgSysInfoTimer.setStatus("mandatory")


class _SCfgCritTimer_Type(Integer32):
    """Custom type sCfgCritTimer based on Integer32"""
    defaultValue = 1


_SCfgCritTimer_Object = MibScalar
sCfgCritTimer = _SCfgCritTimer_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 17),
    _SCfgCritTimer_Type()
)
sCfgCritTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgCritTimer.setStatus("mandatory")


class _SCfgDskAlarm_Type(Integer32):
    """Custom type sCfgDskAlarm based on Integer32"""
    defaultValue = 5


_SCfgDskAlarm_Object = MibScalar
sCfgDskAlarm = _SCfgDskAlarm_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 18),
    _SCfgDskAlarm_Type()
)
sCfgDskAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgDskAlarm.setStatus("mandatory")


class _SCfgCritAlarm_Type(Integer32):
    """Custom type sCfgCritAlarm based on Integer32"""
    defaultValue = 5


_SCfgCritAlarm_Object = MibScalar
sCfgCritAlarm = _SCfgCritAlarm_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 19),
    _SCfgCritAlarm_Type()
)
sCfgCritAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgCritAlarm.setStatus("mandatory")


class _SCfgTrapTblSize_Type(Integer32):
    """Custom type sCfgTrapTblSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 5000),
    )


_SCfgTrapTblSize_Type.__name__ = "Integer32"
_SCfgTrapTblSize_Object = MibScalar
sCfgTrapTblSize = _SCfgTrapTblSize_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 20),
    _SCfgTrapTblSize_Type()
)
sCfgTrapTblSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgTrapTblSize.setStatus("mandatory")


class _SCfgHostName_Type(DisplayString):
    """Custom type sCfgHostName based on DisplayString"""
    defaultValue = OctetString("localhost")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SCfgHostName_Type.__name__ = "DisplayString"
_SCfgHostName_Object = MibScalar
sCfgHostName = _SCfgHostName_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 21),
    _SCfgHostName_Type()
)
sCfgHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCfgHostName.setStatus("mandatory")


class _SCfgAllPsData_Type(Integer32):
    """Custom type sCfgAllPsData based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SCfgAllPsData_Type.__name__ = "Integer32"
_SCfgAllPsData_Object = MibScalar
sCfgAllPsData = _SCfgAllPsData_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 22),
    _SCfgAllPsData_Type()
)
sCfgAllPsData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgAllPsData.setStatus("mandatory")


class _SCfgTimeout_Type(Integer32):
    """Custom type sCfgTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SCfgTimeout_Type.__name__ = "Integer32"
_SCfgTimeout_Object = MibScalar
sCfgTimeout = _SCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 23),
    _SCfgTimeout_Type()
)
sCfgTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCfgTimeout.setStatus("mandatory")


class _SCfgOpcomSecurity_Type(Integer32):
    """Custom type sCfgOpcomSecurity based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomSecurity_Type.__name__ = "Integer32"
_SCfgOpcomSecurity_Object = MibScalar
sCfgOpcomSecurity = _SCfgOpcomSecurity_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 24),
    _SCfgOpcomSecurity_Type()
)
sCfgOpcomSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomSecurity.setStatus("mandatory")


class _SCfgControlTermProc_Type(Integer32):
    """Custom type sCfgControlTermProc based on Integer32"""
    defaultValue = 2

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


_SCfgControlTermProc_Type.__name__ = "Integer32"
_SCfgControlTermProc_Object = MibScalar
sCfgControlTermProc = _SCfgControlTermProc_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 25),
    _SCfgControlTermProc_Type()
)
sCfgControlTermProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCfgControlTermProc.setStatus("mandatory")


class _SCfgTermProc_Type(Integer32):
    """Custom type sCfgTermProc based on Integer32"""
    defaultValue = 2

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


_SCfgTermProc_Type.__name__ = "Integer32"
_SCfgTermProc_Object = MibScalar
sCfgTermProc = _SCfgTermProc_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 26),
    _SCfgTermProc_Type()
)
sCfgTermProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgTermProc.setStatus("mandatory")
_SCfgVersion_Type = DisplayString
_SCfgVersion_Object = MibScalar
sCfgVersion = _SCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 27),
    _SCfgVersion_Type()
)
sCfgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCfgVersion.setStatus("mandatory")
_SCfgUpTime_Type = TimeTicks
_SCfgUpTime_Object = MibScalar
sCfgUpTime = _SCfgUpTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 28),
    _SCfgUpTime_Type()
)
sCfgUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCfgUpTime.setStatus("mandatory")


class _SCfgMaxTrapSec_Type(Integer32):
    """Custom type sCfgMaxTrapSec based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SCfgMaxTrapSec_Type.__name__ = "Integer32"
_SCfgMaxTrapSec_Object = MibScalar
sCfgMaxTrapSec = _SCfgMaxTrapSec_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 29),
    _SCfgMaxTrapSec_Type()
)
sCfgMaxTrapSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgMaxTrapSec.setStatus("mandatory")


class _SCfgCritDsk_Type(DisplayString):
    """Custom type sCfgCritDsk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SCfgCritDsk_Type.__name__ = "DisplayString"
_SCfgCritDsk_Object = MibScalar
sCfgCritDsk = _SCfgCritDsk_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 30),
    _SCfgCritDsk_Type()
)
sCfgCritDsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgCritDsk.setStatus("mandatory")


class _SCfgCritQue_Type(DisplayString):
    """Custom type sCfgCritQue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SCfgCritQue_Type.__name__ = "DisplayString"
_SCfgCritQue_Object = MibScalar
sCfgCritQue = _SCfgCritQue_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 31),
    _SCfgCritQue_Type()
)
sCfgCritQue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgCritQue.setStatus("mandatory")


class _SCfgQueTimer_Type(Integer32):
    """Custom type sCfgQueTimer based on Integer32"""
    defaultValue = 1


_SCfgQueTimer_Object = MibScalar
sCfgQueTimer = _SCfgQueTimer_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 32),
    _SCfgQueTimer_Type()
)
sCfgQueTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgQueTimer.setStatus("mandatory")
_SCfgDskMinFreeBlks_Type = Integer32
_SCfgDskMinFreeBlks_Object = MibScalar
sCfgDskMinFreeBlks = _SCfgDskMinFreeBlks_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 33),
    _SCfgDskMinFreeBlks_Type()
)
sCfgDskMinFreeBlks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgDskMinFreeBlks.setStatus("mandatory")


class _SCfgMemLimit_Type(Integer32):
    """Custom type sCfgMemLimit based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SCfgMemLimit_Type.__name__ = "Integer32"
_SCfgMemLimit_Object = MibScalar
sCfgMemLimit = _SCfgMemLimit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 34),
    _SCfgMemLimit_Type()
)
sCfgMemLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgMemLimit.setStatus("mandatory")


class _SCfgCOMQueueLimit_Type(Integer32):
    """Custom type sCfgCOMQueueLimit based on Integer32"""
    defaultValue = 5


_SCfgCOMQueueLimit_Object = MibScalar
sCfgCOMQueueLimit = _SCfgCOMQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 35),
    _SCfgCOMQueueLimit_Type()
)
sCfgCOMQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgCOMQueueLimit.setStatus("mandatory")


class _SCfgCOMOQueueLimit_Type(Integer32):
    """Custom type sCfgCOMOQueueLimit based on Integer32"""
    defaultValue = 1


_SCfgCOMOQueueLimit_Object = MibScalar
sCfgCOMOQueueLimit = _SCfgCOMOQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 36),
    _SCfgCOMOQueueLimit_Type()
)
sCfgCOMOQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgCOMOQueueLimit.setStatus("mandatory")


class _SCfgOpcomCards_Type(Integer32):
    """Custom type sCfgOpcomCards based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomCards_Type.__name__ = "Integer32"
_SCfgOpcomCards_Object = MibScalar
sCfgOpcomCards = _SCfgOpcomCards_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 37),
    _SCfgOpcomCards_Type()
)
sCfgOpcomCards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomCards.setStatus("mandatory")


class _SCfgOpcomCentral_Type(Integer32):
    """Custom type sCfgOpcomCentral based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomCentral_Type.__name__ = "Integer32"
_SCfgOpcomCentral_Object = MibScalar
sCfgOpcomCentral = _SCfgOpcomCentral_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 38),
    _SCfgOpcomCentral_Type()
)
sCfgOpcomCentral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomCentral.setStatus("mandatory")


class _SCfgOpcomCluster_Type(Integer32):
    """Custom type sCfgOpcomCluster based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomCluster_Type.__name__ = "Integer32"
_SCfgOpcomCluster_Object = MibScalar
sCfgOpcomCluster = _SCfgOpcomCluster_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 39),
    _SCfgOpcomCluster_Type()
)
sCfgOpcomCluster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomCluster.setStatus("mandatory")


class _SCfgOpcomDevices_Type(Integer32):
    """Custom type sCfgOpcomDevices based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomDevices_Type.__name__ = "Integer32"
_SCfgOpcomDevices_Object = MibScalar
sCfgOpcomDevices = _SCfgOpcomDevices_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 40),
    _SCfgOpcomDevices_Type()
)
sCfgOpcomDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomDevices.setStatus("mandatory")


class _SCfgOpcomDisks_Type(Integer32):
    """Custom type sCfgOpcomDisks based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomDisks_Type.__name__ = "Integer32"
_SCfgOpcomDisks_Object = MibScalar
sCfgOpcomDisks = _SCfgOpcomDisks_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 41),
    _SCfgOpcomDisks_Type()
)
sCfgOpcomDisks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomDisks.setStatus("mandatory")


class _SCfgOpcomLicense_Type(Integer32):
    """Custom type sCfgOpcomLicense based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomLicense_Type.__name__ = "Integer32"
_SCfgOpcomLicense_Object = MibScalar
sCfgOpcomLicense = _SCfgOpcomLicense_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 42),
    _SCfgOpcomLicense_Type()
)
sCfgOpcomLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomLicense.setStatus("mandatory")


class _SCfgOpcomNetwork_Type(Integer32):
    """Custom type sCfgOpcomNetwork based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomNetwork_Type.__name__ = "Integer32"
_SCfgOpcomNetwork_Object = MibScalar
sCfgOpcomNetwork = _SCfgOpcomNetwork_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 43),
    _SCfgOpcomNetwork_Type()
)
sCfgOpcomNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomNetwork.setStatus("mandatory")


class _SCfgOpcomOper1_Type(Integer32):
    """Custom type sCfgOpcomOper1 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper1_Type.__name__ = "Integer32"
_SCfgOpcomOper1_Object = MibScalar
sCfgOpcomOper1 = _SCfgOpcomOper1_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 44),
    _SCfgOpcomOper1_Type()
)
sCfgOpcomOper1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper1.setStatus("mandatory")


class _SCfgOpcomOper2_Type(Integer32):
    """Custom type sCfgOpcomOper2 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper2_Type.__name__ = "Integer32"
_SCfgOpcomOper2_Object = MibScalar
sCfgOpcomOper2 = _SCfgOpcomOper2_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 45),
    _SCfgOpcomOper2_Type()
)
sCfgOpcomOper2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper2.setStatus("mandatory")


class _SCfgOpcomOper3_Type(Integer32):
    """Custom type sCfgOpcomOper3 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper3_Type.__name__ = "Integer32"
_SCfgOpcomOper3_Object = MibScalar
sCfgOpcomOper3 = _SCfgOpcomOper3_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 46),
    _SCfgOpcomOper3_Type()
)
sCfgOpcomOper3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper3.setStatus("mandatory")


class _SCfgOpcomOper4_Type(Integer32):
    """Custom type sCfgOpcomOper4 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper4_Type.__name__ = "Integer32"
_SCfgOpcomOper4_Object = MibScalar
sCfgOpcomOper4 = _SCfgOpcomOper4_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 47),
    _SCfgOpcomOper4_Type()
)
sCfgOpcomOper4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper4.setStatus("mandatory")


class _SCfgOpcomOper5_Type(Integer32):
    """Custom type sCfgOpcomOper5 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper5_Type.__name__ = "Integer32"
_SCfgOpcomOper5_Object = MibScalar
sCfgOpcomOper5 = _SCfgOpcomOper5_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 48),
    _SCfgOpcomOper5_Type()
)
sCfgOpcomOper5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper5.setStatus("mandatory")


class _SCfgOpcomOper6_Type(Integer32):
    """Custom type sCfgOpcomOper6 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper6_Type.__name__ = "Integer32"
_SCfgOpcomOper6_Object = MibScalar
sCfgOpcomOper6 = _SCfgOpcomOper6_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 49),
    _SCfgOpcomOper6_Type()
)
sCfgOpcomOper6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper6.setStatus("mandatory")


class _SCfgOpcomOper7_Type(Integer32):
    """Custom type sCfgOpcomOper7 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper7_Type.__name__ = "Integer32"
_SCfgOpcomOper7_Object = MibScalar
sCfgOpcomOper7 = _SCfgOpcomOper7_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 50),
    _SCfgOpcomOper7_Type()
)
sCfgOpcomOper7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper7.setStatus("mandatory")


class _SCfgOpcomOper8_Type(Integer32):
    """Custom type sCfgOpcomOper8 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper8_Type.__name__ = "Integer32"
_SCfgOpcomOper8_Object = MibScalar
sCfgOpcomOper8 = _SCfgOpcomOper8_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 51),
    _SCfgOpcomOper8_Type()
)
sCfgOpcomOper8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper8.setStatus("mandatory")


class _SCfgOpcomOper9_Type(Integer32):
    """Custom type sCfgOpcomOper9 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper9_Type.__name__ = "Integer32"
_SCfgOpcomOper9_Object = MibScalar
sCfgOpcomOper9 = _SCfgOpcomOper9_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 52),
    _SCfgOpcomOper9_Type()
)
sCfgOpcomOper9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper9.setStatus("mandatory")


class _SCfgOpcomOper10_Type(Integer32):
    """Custom type sCfgOpcomOper10 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper10_Type.__name__ = "Integer32"
_SCfgOpcomOper10_Object = MibScalar
sCfgOpcomOper10 = _SCfgOpcomOper10_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 53),
    _SCfgOpcomOper10_Type()
)
sCfgOpcomOper10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper10.setStatus("mandatory")


class _SCfgOpcomOper11_Type(Integer32):
    """Custom type sCfgOpcomOper11 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper11_Type.__name__ = "Integer32"
_SCfgOpcomOper11_Object = MibScalar
sCfgOpcomOper11 = _SCfgOpcomOper11_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 54),
    _SCfgOpcomOper11_Type()
)
sCfgOpcomOper11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper11.setStatus("mandatory")


class _SCfgOpcomOper12_Type(Integer32):
    """Custom type sCfgOpcomOper12 based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomOper12_Type.__name__ = "Integer32"
_SCfgOpcomOper12_Object = MibScalar
sCfgOpcomOper12 = _SCfgOpcomOper12_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 55),
    _SCfgOpcomOper12_Type()
)
sCfgOpcomOper12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomOper12.setStatus("mandatory")


class _SCfgOpcomPrinter_Type(Integer32):
    """Custom type sCfgOpcomPrinter based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomPrinter_Type.__name__ = "Integer32"
_SCfgOpcomPrinter_Object = MibScalar
sCfgOpcomPrinter = _SCfgOpcomPrinter_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 56),
    _SCfgOpcomPrinter_Type()
)
sCfgOpcomPrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomPrinter.setStatus("mandatory")


class _SCfgOpcomTapes_Type(Integer32):
    """Custom type sCfgOpcomTapes based on Integer32"""
    defaultValue = 1

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


_SCfgOpcomTapes_Type.__name__ = "Integer32"
_SCfgOpcomTapes_Object = MibScalar
sCfgOpcomTapes = _SCfgOpcomTapes_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 57),
    _SCfgOpcomTapes_Type()
)
sCfgOpcomTapes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomTapes.setStatus("mandatory")


class _SCfgOpcomFilter_Type(Integer32):
    """Custom type sCfgOpcomFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dropMatch", 1),
          ("keepMatch", 2))
    )


_SCfgOpcomFilter_Type.__name__ = "Integer32"
_SCfgOpcomFilter_Object = MibScalar
sCfgOpcomFilter = _SCfgOpcomFilter_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 58),
    _SCfgOpcomFilter_Type()
)
sCfgOpcomFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgOpcomFilter.setStatus("mandatory")


class _SCfgLocalDisksOnly_Type(Integer32):
    """Custom type sCfgLocalDisksOnly based on Integer32"""
    defaultValue = 2

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


_SCfgLocalDisksOnly_Type.__name__ = "Integer32"
_SCfgLocalDisksOnly_Object = MibScalar
sCfgLocalDisksOnly = _SCfgLocalDisksOnly_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 59),
    _SCfgLocalDisksOnly_Type()
)
sCfgLocalDisksOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgLocalDisksOnly.setStatus("mandatory")


class _SCfgCritDisksOnly_Type(Integer32):
    """Custom type sCfgCritDisksOnly based on Integer32"""
    defaultValue = 2

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


_SCfgCritDisksOnly_Type.__name__ = "Integer32"
_SCfgCritDisksOnly_Object = MibScalar
sCfgCritDisksOnly = _SCfgCritDisksOnly_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 3, 5, 60),
    _SCfgCritDisksOnly_Type()
)
sCfgCritDisksOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sCfgCritDisksOnly.setStatus("mandatory")
_ComtekVmsNMVmsMonMib_ObjectIdentity = ObjectIdentity
comtekVmsNMVmsMonMib = _ComtekVmsNMVmsMonMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15)
)
_VmsModes_ObjectIdentity = ObjectIdentity
vmsModes = _VmsModes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1)
)
_VmsModeUpdateTime_Type = TimeTicks
_VmsModeUpdateTime_Object = MibScalar
vmsModeUpdateTime = _VmsModeUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 1),
    _VmsModeUpdateTime_Type()
)
vmsModeUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsModeUpdateTime.setStatus("mandatory")


class _VmsModeUpdateInterval_Type(Integer32):
    """Custom type vmsModeUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsModeUpdateInterval_Object = MibScalar
vmsModeUpdateInterval = _VmsModeUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 2),
    _VmsModeUpdateInterval_Type()
)
vmsModeUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsModeUpdateInterval.setStatus("mandatory")
_VmsModeCpuCount_Type = Counter32
_VmsModeCpuCount_Object = MibScalar
vmsModeCpuCount = _VmsModeCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 3),
    _VmsModeCpuCount_Type()
)
vmsModeCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsModeCpuCount.setStatus("mandatory")
_VmsModeTable_Object = MibTable
vmsModeTable = _VmsModeTable_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 4)
)
if mibBuilder.loadTexts:
    vmsModeTable.setStatus("mandatory")
_VmsModeTableEntry_Object = MibTableRow
vmsModeTableEntry = _VmsModeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 4, 1)
)
vmsModeTableEntry.setIndexNames(
    (0, "COMTEK-VMS-NM-SYSMGR-MIB", "vmsModeCpuId"),
)
if mibBuilder.loadTexts:
    vmsModeTableEntry.setStatus("mandatory")
_VmsModeCpuId_Type = Integer32
_VmsModeCpuId_Object = MibTableColumn
vmsModeCpuId = _VmsModeCpuId_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 4, 1, 1),
    _VmsModeCpuId_Type()
)
vmsModeCpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsModeCpuId.setStatus("mandatory")
_VmsModeKernel_Type = Integer32
_VmsModeKernel_Object = MibTableColumn
vmsModeKernel = _VmsModeKernel_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 4, 1, 2),
    _VmsModeKernel_Type()
)
vmsModeKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsModeKernel.setStatus("mandatory")
_VmsModeExec_Type = Integer32
_VmsModeExec_Object = MibTableColumn
vmsModeExec = _VmsModeExec_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 4, 1, 3),
    _VmsModeExec_Type()
)
vmsModeExec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsModeExec.setStatus("mandatory")
_VmsModeSuper_Type = Integer32
_VmsModeSuper_Object = MibTableColumn
vmsModeSuper = _VmsModeSuper_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 4, 1, 4),
    _VmsModeSuper_Type()
)
vmsModeSuper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsModeSuper.setStatus("mandatory")
_VmsModeUser_Type = Integer32
_VmsModeUser_Object = MibTableColumn
vmsModeUser = _VmsModeUser_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 4, 1, 5),
    _VmsModeUser_Type()
)
vmsModeUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsModeUser.setStatus("mandatory")
_VmsModeInter_Type = Integer32
_VmsModeInter_Object = MibTableColumn
vmsModeInter = _VmsModeInter_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 4, 1, 6),
    _VmsModeInter_Type()
)
vmsModeInter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsModeInter.setStatus("mandatory")
_VmsModeMPSync_Type = Integer32
_VmsModeMPSync_Object = MibTableColumn
vmsModeMPSync = _VmsModeMPSync_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 4, 1, 7),
    _VmsModeMPSync_Type()
)
vmsModeMPSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsModeMPSync.setStatus("mandatory")
_VmsModeCompat_Type = Integer32
_VmsModeCompat_Object = MibTableColumn
vmsModeCompat = _VmsModeCompat_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 4, 1, 8),
    _VmsModeCompat_Type()
)
vmsModeCompat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsModeCompat.setStatus("mandatory")
_VmsModeIdle_Type = Integer32
_VmsModeIdle_Object = MibTableColumn
vmsModeIdle = _VmsModeIdle_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 4, 1, 9),
    _VmsModeIdle_Type()
)
vmsModeIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsModeIdle.setStatus("mandatory")
_VmsTotalModes_ObjectIdentity = ObjectIdentity
vmsTotalModes = _VmsTotalModes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 5)
)
_VmsTotalKernel_Type = Integer32
_VmsTotalKernel_Object = MibScalar
vmsTotalKernel = _VmsTotalKernel_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 5, 1),
    _VmsTotalKernel_Type()
)
vmsTotalKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsTotalKernel.setStatus("mandatory")
_VmsTotalExec_Type = Integer32
_VmsTotalExec_Object = MibScalar
vmsTotalExec = _VmsTotalExec_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 5, 2),
    _VmsTotalExec_Type()
)
vmsTotalExec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsTotalExec.setStatus("mandatory")
_VmsTotalSuper_Type = Integer32
_VmsTotalSuper_Object = MibScalar
vmsTotalSuper = _VmsTotalSuper_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 5, 3),
    _VmsTotalSuper_Type()
)
vmsTotalSuper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsTotalSuper.setStatus("mandatory")
_VmsTotalUser_Type = Integer32
_VmsTotalUser_Object = MibScalar
vmsTotalUser = _VmsTotalUser_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 5, 4),
    _VmsTotalUser_Type()
)
vmsTotalUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsTotalUser.setStatus("mandatory")
_VmsTotalInter_Type = Integer32
_VmsTotalInter_Object = MibScalar
vmsTotalInter = _VmsTotalInter_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 5, 5),
    _VmsTotalInter_Type()
)
vmsTotalInter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsTotalInter.setStatus("mandatory")
_VmsTotalMPSync_Type = Integer32
_VmsTotalMPSync_Object = MibScalar
vmsTotalMPSync = _VmsTotalMPSync_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 5, 6),
    _VmsTotalMPSync_Type()
)
vmsTotalMPSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsTotalMPSync.setStatus("mandatory")
_VmsTotalComp_Type = Integer32
_VmsTotalComp_Object = MibScalar
vmsTotalComp = _VmsTotalComp_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 5, 7),
    _VmsTotalComp_Type()
)
vmsTotalComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsTotalComp.setStatus("mandatory")
_VmsTotalIdle_Type = Integer32
_VmsTotalIdle_Object = MibScalar
vmsTotalIdle = _VmsTotalIdle_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 1, 5, 8),
    _VmsTotalIdle_Type()
)
vmsTotalIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsTotalIdle.setStatus("mandatory")
_VmsFile_ObjectIdentity = ObjectIdentity
vmsFile = _VmsFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2)
)
_VmsFileUpdateTime_Type = TimeTicks
_VmsFileUpdateTime_Object = MibScalar
vmsFileUpdateTime = _VmsFileUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 1),
    _VmsFileUpdateTime_Type()
)
vmsFileUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileUpdateTime.setStatus("mandatory")


class _VmsFileUpdateInterval_Type(Integer32):
    """Custom type vmsFileUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsFileUpdateInterval_Object = MibScalar
vmsFileUpdateInterval = _VmsFileUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 2),
    _VmsFileUpdateInterval_Type()
)
vmsFileUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsFileUpdateInterval.setStatus("mandatory")
_VmsFileDirFCBHit_Type = Counter32
_VmsFileDirFCBHit_Object = MibScalar
vmsFileDirFCBHit = _VmsFileDirFCBHit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 3),
    _VmsFileDirFCBHit_Type()
)
vmsFileDirFCBHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileDirFCBHit.setStatus("mandatory")
_VmsFileDirFCBAttempt_Type = Counter32
_VmsFileDirFCBAttempt_Object = MibScalar
vmsFileDirFCBAttempt = _VmsFileDirFCBAttempt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 4),
    _VmsFileDirFCBAttempt_Type()
)
vmsFileDirFCBAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileDirFCBAttempt.setStatus("mandatory")
_VmsFileDirDataHit_Type = Counter32
_VmsFileDirDataHit_Object = MibScalar
vmsFileDirDataHit = _VmsFileDirDataHit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 5),
    _VmsFileDirDataHit_Type()
)
vmsFileDirDataHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileDirDataHit.setStatus("mandatory")
_VmsFileDirDataAttempt_Type = Counter32
_VmsFileDirDataAttempt_Object = MibScalar
vmsFileDirDataAttempt = _VmsFileDirDataAttempt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 6),
    _VmsFileDirDataAttempt_Type()
)
vmsFileDirDataAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileDirDataAttempt.setStatus("mandatory")
_VmsFileFileHdrHit_Type = Counter32
_VmsFileFileHdrHit_Object = MibScalar
vmsFileFileHdrHit = _VmsFileFileHdrHit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 7),
    _VmsFileFileHdrHit_Type()
)
vmsFileFileHdrHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileFileHdrHit.setStatus("mandatory")
_VmsFileFileHdrAttempt_Type = Counter32
_VmsFileFileHdrAttempt_Object = MibScalar
vmsFileFileHdrAttempt = _VmsFileFileHdrAttempt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 8),
    _VmsFileFileHdrAttempt_Type()
)
vmsFileFileHdrAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileFileHdrAttempt.setStatus("mandatory")
_VmsFileFileIdHit_Type = Counter32
_VmsFileFileIdHit_Object = MibScalar
vmsFileFileIdHit = _VmsFileFileIdHit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 9),
    _VmsFileFileIdHit_Type()
)
vmsFileFileIdHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileFileIdHit.setStatus("mandatory")
_VmsFileFileIdAttempt_Type = Counter32
_VmsFileFileIdAttempt_Object = MibScalar
vmsFileFileIdAttempt = _VmsFileFileIdAttempt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 10),
    _VmsFileFileIdAttempt_Type()
)
vmsFileFileIdAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileFileIdAttempt.setStatus("mandatory")
_VmsFileExtentHit_Type = Counter32
_VmsFileExtentHit_Object = MibScalar
vmsFileExtentHit = _VmsFileExtentHit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 11),
    _VmsFileExtentHit_Type()
)
vmsFileExtentHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileExtentHit.setStatus("mandatory")
_VmsFileExtentAttempt_Type = Counter32
_VmsFileExtentAttempt_Object = MibScalar
vmsFileExtentAttempt = _VmsFileExtentAttempt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 12),
    _VmsFileExtentAttempt_Type()
)
vmsFileExtentAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileExtentAttempt.setStatus("mandatory")
_VmsFileQuotaHit_Type = Counter32
_VmsFileQuotaHit_Object = MibScalar
vmsFileQuotaHit = _VmsFileQuotaHit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 13),
    _VmsFileQuotaHit_Type()
)
vmsFileQuotaHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileQuotaHit.setStatus("mandatory")
_VmsFileQuotaAttempt_Type = Counter32
_VmsFileQuotaAttempt_Object = MibScalar
vmsFileQuotaAttempt = _VmsFileQuotaAttempt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 14),
    _VmsFileQuotaAttempt_Type()
)
vmsFileQuotaAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileQuotaAttempt.setStatus("mandatory")
_VmsFileBitmapHit_Type = Counter32
_VmsFileBitmapHit_Object = MibScalar
vmsFileBitmapHit = _VmsFileBitmapHit_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 15),
    _VmsFileBitmapHit_Type()
)
vmsFileBitmapHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileBitmapHit.setStatus("mandatory")
_VmsFileBitmapAttempt_Type = Counter32
_VmsFileBitmapAttempt_Object = MibScalar
vmsFileBitmapAttempt = _VmsFileBitmapAttempt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 2, 16),
    _VmsFileBitmapAttempt_Type()
)
vmsFileBitmapAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFileBitmapAttempt.setStatus("mandatory")
_VmsFcp_ObjectIdentity = ObjectIdentity
vmsFcp = _VmsFcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3)
)
_VmsFcpUpdateTime_Type = TimeTicks
_VmsFcpUpdateTime_Object = MibScalar
vmsFcpUpdateTime = _VmsFcpUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 1),
    _VmsFcpUpdateTime_Type()
)
vmsFcpUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpUpdateTime.setStatus("mandatory")


class _VmsFcpUpdateInterval_Type(Integer32):
    """Custom type vmsFcpUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsFcpUpdateInterval_Object = MibScalar
vmsFcpUpdateInterval = _VmsFcpUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 2),
    _VmsFcpUpdateInterval_Type()
)
vmsFcpUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsFcpUpdateInterval.setStatus("mandatory")
_VmsFcpFCPCall_Type = Counter32
_VmsFcpFCPCall_Object = MibScalar
vmsFcpFCPCall = _VmsFcpFCPCall_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 3),
    _VmsFcpFCPCall_Type()
)
vmsFcpFCPCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpFCPCall.setStatus("mandatory")
_VmsFcpAllocation_Type = Counter32
_VmsFcpAllocation_Object = MibScalar
vmsFcpAllocation = _VmsFcpAllocation_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 4),
    _VmsFcpAllocation_Type()
)
vmsFcpAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpAllocation.setStatus("mandatory")
_VmsFcpCreate_Type = Counter32
_VmsFcpCreate_Object = MibScalar
vmsFcpCreate = _VmsFcpCreate_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 5),
    _VmsFcpCreate_Type()
)
vmsFcpCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpCreate.setStatus("mandatory")
_VmsFcpDiskRead_Type = Counter32
_VmsFcpDiskRead_Object = MibScalar
vmsFcpDiskRead = _VmsFcpDiskRead_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 6),
    _VmsFcpDiskRead_Type()
)
vmsFcpDiskRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpDiskRead.setStatus("mandatory")
_VmsFcpDiskWrite_Type = Counter32
_VmsFcpDiskWrite_Object = MibScalar
vmsFcpDiskWrite = _VmsFcpDiskWrite_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 7),
    _VmsFcpDiskWrite_Type()
)
vmsFcpDiskWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpDiskWrite.setStatus("mandatory")
_VmsFcpVolumeLockWait_Type = Counter32
_VmsFcpVolumeLockWait_Object = MibScalar
vmsFcpVolumeLockWait = _VmsFcpVolumeLockWait_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 8),
    _VmsFcpVolumeLockWait_Type()
)
vmsFcpVolumeLockWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpVolumeLockWait.setStatus("mandatory")
_VmsFcpCPUTick_Type = Counter32
_VmsFcpCPUTick_Object = MibScalar
vmsFcpCPUTick = _VmsFcpCPUTick_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 9),
    _VmsFcpCPUTick_Type()
)
vmsFcpCPUTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpCPUTick.setStatus("mandatory")
_VmsFcpPageFault_Type = Counter32
_VmsFcpPageFault_Object = MibScalar
vmsFcpPageFault = _VmsFcpPageFault_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 10),
    _VmsFcpPageFault_Type()
)
vmsFcpPageFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpPageFault.setStatus("mandatory")
_VmsFcpWindowTurn_Type = Counter32
_VmsFcpWindowTurn_Object = MibScalar
vmsFcpWindowTurn = _VmsFcpWindowTurn_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 11),
    _VmsFcpWindowTurn_Type()
)
vmsFcpWindowTurn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpWindowTurn.setStatus("mandatory")
_VmsFcpLookup_Type = Counter32
_VmsFcpLookup_Object = MibScalar
vmsFcpLookup = _VmsFcpLookup_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 12),
    _VmsFcpLookup_Type()
)
vmsFcpLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpLookup.setStatus("mandatory")
_VmsFcpOpen_Type = Counter32
_VmsFcpOpen_Object = MibScalar
vmsFcpOpen = _VmsFcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 13),
    _VmsFcpOpen_Type()
)
vmsFcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpOpen.setStatus("mandatory")
_VmsFcpErase_Type = Counter32
_VmsFcpErase_Object = MibScalar
vmsFcpErase = _VmsFcpErase_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 3, 14),
    _VmsFcpErase_Type()
)
vmsFcpErase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsFcpErase.setStatus("mandatory")
_VmsIo_ObjectIdentity = ObjectIdentity
vmsIo = _VmsIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4)
)
_VmsIoUpdateTime_Type = TimeTicks
_VmsIoUpdateTime_Object = MibScalar
vmsIoUpdateTime = _VmsIoUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 1),
    _VmsIoUpdateTime_Type()
)
vmsIoUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoUpdateTime.setStatus("mandatory")


class _VmsIoUpdateInterval_Type(Integer32):
    """Custom type vmsIoUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsIoUpdateInterval_Object = MibScalar
vmsIoUpdateInterval = _VmsIoUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 2),
    _VmsIoUpdateInterval_Type()
)
vmsIoUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsIoUpdateInterval.setStatus("mandatory")
_VmsIoDirectIO_Type = Counter32
_VmsIoDirectIO_Object = MibScalar
vmsIoDirectIO = _VmsIoDirectIO_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 3),
    _VmsIoDirectIO_Type()
)
vmsIoDirectIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoDirectIO.setStatus("mandatory")
_VmsIoBufferedIO_Type = Counter32
_VmsIoBufferedIO_Object = MibScalar
vmsIoBufferedIO = _VmsIoBufferedIO_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 4),
    _VmsIoBufferedIO_Type()
)
vmsIoBufferedIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoBufferedIO.setStatus("mandatory")
_VmsIoMailboxWrite_Type = Counter32
_VmsIoMailboxWrite_Object = MibScalar
vmsIoMailboxWrite = _VmsIoMailboxWrite_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 5),
    _VmsIoMailboxWrite_Type()
)
vmsIoMailboxWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoMailboxWrite.setStatus("mandatory")
_VmsIoSplitTransfer_Type = Counter32
_VmsIoSplitTransfer_Object = MibScalar
vmsIoSplitTransfer = _VmsIoSplitTransfer_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 6),
    _VmsIoSplitTransfer_Type()
)
vmsIoSplitTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoSplitTransfer.setStatus("mandatory")
_VmsIoLogNameTranslation_Type = Counter32
_VmsIoLogNameTranslation_Object = MibScalar
vmsIoLogNameTranslation = _VmsIoLogNameTranslation_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 7),
    _VmsIoLogNameTranslation_Type()
)
vmsIoLogNameTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoLogNameTranslation.setStatus("mandatory")
_VmsIoFileOpen_Type = Counter32
_VmsIoFileOpen_Object = MibScalar
vmsIoFileOpen = _VmsIoFileOpen_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 8),
    _VmsIoFileOpen_Type()
)
vmsIoFileOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoFileOpen.setStatus("mandatory")
_VmsIoPageFault_Type = Counter32
_VmsIoPageFault_Object = MibScalar
vmsIoPageFault = _VmsIoPageFault_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 9),
    _VmsIoPageFault_Type()
)
vmsIoPageFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoPageFault.setStatus("mandatory")
_VmsIoPageRead_Type = Counter32
_VmsIoPageRead_Object = MibScalar
vmsIoPageRead = _VmsIoPageRead_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 10),
    _VmsIoPageRead_Type()
)
vmsIoPageRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoPageRead.setStatus("mandatory")
_VmsIoPageReadIO_Type = Counter32
_VmsIoPageReadIO_Object = MibScalar
vmsIoPageReadIO = _VmsIoPageReadIO_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 11),
    _VmsIoPageReadIO_Type()
)
vmsIoPageReadIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoPageReadIO.setStatus("mandatory")
_VmsIoPageWrite_Type = Counter32
_VmsIoPageWrite_Object = MibScalar
vmsIoPageWrite = _VmsIoPageWrite_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 12),
    _VmsIoPageWrite_Type()
)
vmsIoPageWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoPageWrite.setStatus("mandatory")
_VmsIoPageWriteIO_Type = Counter32
_VmsIoPageWriteIO_Object = MibScalar
vmsIoPageWriteIO = _VmsIoPageWriteIO_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 13),
    _VmsIoPageWriteIO_Type()
)
vmsIoPageWriteIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoPageWriteIO.setStatus("mandatory")
_VmsIoInswap_Type = Counter32
_VmsIoInswap_Object = MibScalar
vmsIoInswap = _VmsIoInswap_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 14),
    _VmsIoInswap_Type()
)
vmsIoInswap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoInswap.setStatus("mandatory")
_VmsIoFreePageCount_Type = Counter32
_VmsIoFreePageCount_Object = MibScalar
vmsIoFreePageCount = _VmsIoFreePageCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 15),
    _VmsIoFreePageCount_Type()
)
vmsIoFreePageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoFreePageCount.setStatus("mandatory")
_VmsIoModifiedPageCount_Type = Counter32
_VmsIoModifiedPageCount_Object = MibScalar
vmsIoModifiedPageCount = _VmsIoModifiedPageCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 4, 16),
    _VmsIoModifiedPageCount_Type()
)
vmsIoModifiedPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsIoModifiedPageCount.setStatus("mandatory")
_VmsPage_ObjectIdentity = ObjectIdentity
vmsPage = _VmsPage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5)
)
_VmsPageUpdateTime_Type = TimeTicks
_VmsPageUpdateTime_Object = MibScalar
vmsPageUpdateTime = _VmsPageUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 1),
    _VmsPageUpdateTime_Type()
)
vmsPageUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageUpdateTime.setStatus("mandatory")


class _VmsPageUpdateInterval_Type(Integer32):
    """Custom type vmsPageUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsPageUpdateInterval_Object = MibScalar
vmsPageUpdateInterval = _VmsPageUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 2),
    _VmsPageUpdateInterval_Type()
)
vmsPageUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsPageUpdateInterval.setStatus("mandatory")
_VmsPageFault_Type = Counter32
_VmsPageFault_Object = MibScalar
vmsPageFault = _VmsPageFault_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 3),
    _VmsPageFault_Type()
)
vmsPageFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageFault.setStatus("mandatory")
_VmsPageRead_Type = Counter32
_VmsPageRead_Object = MibScalar
vmsPageRead = _VmsPageRead_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 4),
    _VmsPageRead_Type()
)
vmsPageRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageRead.setStatus("mandatory")
_VmsPageReadIO_Type = Counter32
_VmsPageReadIO_Object = MibScalar
vmsPageReadIO = _VmsPageReadIO_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 5),
    _VmsPageReadIO_Type()
)
vmsPageReadIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageReadIO.setStatus("mandatory")
_VmsPageWrite_Type = Counter32
_VmsPageWrite_Object = MibScalar
vmsPageWrite = _VmsPageWrite_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 6),
    _VmsPageWrite_Type()
)
vmsPageWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageWrite.setStatus("mandatory")
_VmsPageWriteIO_Type = Counter32
_VmsPageWriteIO_Object = MibScalar
vmsPageWriteIO = _VmsPageWriteIO_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 7),
    _VmsPageWriteIO_Type()
)
vmsPageWriteIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageWriteIO.setStatus("mandatory")
_VmsPageFreeListFault_Type = Counter32
_VmsPageFreeListFault_Object = MibScalar
vmsPageFreeListFault = _VmsPageFreeListFault_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 8),
    _VmsPageFreeListFault_Type()
)
vmsPageFreeListFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageFreeListFault.setStatus("mandatory")
_VmsPageModListFault_Type = Counter32
_VmsPageModListFault_Object = MibScalar
vmsPageModListFault = _VmsPageModListFault_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 9),
    _VmsPageModListFault_Type()
)
vmsPageModListFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageModListFault.setStatus("mandatory")
_VmsPageDemandZeroFault_Type = Counter32
_VmsPageDemandZeroFault_Object = MibScalar
vmsPageDemandZeroFault = _VmsPageDemandZeroFault_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 10),
    _VmsPageDemandZeroFault_Type()
)
vmsPageDemandZeroFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageDemandZeroFault.setStatus("mandatory")
_VmsPageGlobalValidFault_Type = Counter32
_VmsPageGlobalValidFault_Object = MibScalar
vmsPageGlobalValidFault = _VmsPageGlobalValidFault_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 11),
    _VmsPageGlobalValidFault_Type()
)
vmsPageGlobalValidFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageGlobalValidFault.setStatus("mandatory")
_VmsPageWrtInProgressFault_Type = Counter32
_VmsPageWrtInProgressFault_Object = MibScalar
vmsPageWrtInProgressFault = _VmsPageWrtInProgressFault_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 12),
    _VmsPageWrtInProgressFault_Type()
)
vmsPageWrtInProgressFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageWrtInProgressFault.setStatus("mandatory")
_VmsPageSystemFault_Type = Counter32
_VmsPageSystemFault_Object = MibScalar
vmsPageSystemFault = _VmsPageSystemFault_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 13),
    _VmsPageSystemFault_Type()
)
vmsPageSystemFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageSystemFault.setStatus("mandatory")
_VmsPageFreePageCount_Type = Counter32
_VmsPageFreePageCount_Object = MibScalar
vmsPageFreePageCount = _VmsPageFreePageCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 14),
    _VmsPageFreePageCount_Type()
)
vmsPageFreePageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageFreePageCount.setStatus("mandatory")
_VmsPageModifiedPageCount_Type = Counter32
_VmsPageModifiedPageCount_Object = MibScalar
vmsPageModifiedPageCount = _VmsPageModifiedPageCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 5, 15),
    _VmsPageModifiedPageCount_Type()
)
vmsPageModifiedPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsPageModifiedPageCount.setStatus("mandatory")
_VmsDecnet_ObjectIdentity = ObjectIdentity
vmsDecnet = _VmsDecnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 6)
)
_VmsDecnetUpdateTime_Type = TimeTicks
_VmsDecnetUpdateTime_Object = MibScalar
vmsDecnetUpdateTime = _VmsDecnetUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 6, 1),
    _VmsDecnetUpdateTime_Type()
)
vmsDecnetUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDecnetUpdateTime.setStatus("mandatory")


class _VmsDecnetUpdateInterval_Type(Integer32):
    """Custom type vmsDecnetUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsDecnetUpdateInterval_Object = MibScalar
vmsDecnetUpdateInterval = _VmsDecnetUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 6, 2),
    _VmsDecnetUpdateInterval_Type()
)
vmsDecnetUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsDecnetUpdateInterval.setStatus("mandatory")
_VmsDecnetArriveLocalPkt_Type = Counter32
_VmsDecnetArriveLocalPkt_Object = MibScalar
vmsDecnetArriveLocalPkt = _VmsDecnetArriveLocalPkt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 6, 3),
    _VmsDecnetArriveLocalPkt_Type()
)
vmsDecnetArriveLocalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDecnetArriveLocalPkt.setStatus("mandatory")
_VmsDecnetDepartLocalPkt_Type = Counter32
_VmsDecnetDepartLocalPkt_Object = MibScalar
vmsDecnetDepartLocalPkt = _VmsDecnetDepartLocalPkt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 6, 4),
    _VmsDecnetDepartLocalPkt_Type()
)
vmsDecnetDepartLocalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDecnetDepartLocalPkt.setStatus("mandatory")
_VmsDecnetArriveTransPkt_Type = Counter32
_VmsDecnetArriveTransPkt_Object = MibScalar
vmsDecnetArriveTransPkt = _VmsDecnetArriveTransPkt_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 6, 5),
    _VmsDecnetArriveTransPkt_Type()
)
vmsDecnetArriveTransPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDecnetArriveTransPkt.setStatus("mandatory")
_VmsDecnetTransCongestLoss_Type = Counter32
_VmsDecnetTransCongestLoss_Object = MibScalar
vmsDecnetTransCongestLoss = _VmsDecnetTransCongestLoss_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 6, 6),
    _VmsDecnetTransCongestLoss_Type()
)
vmsDecnetTransCongestLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDecnetTransCongestLoss.setStatus("mandatory")
_VmsDecnetReceiveBufFail_Type = Counter32
_VmsDecnetReceiveBufFail_Object = MibScalar
vmsDecnetReceiveBufFail = _VmsDecnetReceiveBufFail_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 6, 7),
    _VmsDecnetReceiveBufFail_Type()
)
vmsDecnetReceiveBufFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDecnetReceiveBufFail.setStatus("mandatory")
_VmsStates_ObjectIdentity = ObjectIdentity
vmsStates = _VmsStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7)
)
_VmsStatesUpdateTime_Type = TimeTicks
_VmsStatesUpdateTime_Object = MibScalar
vmsStatesUpdateTime = _VmsStatesUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 1),
    _VmsStatesUpdateTime_Type()
)
vmsStatesUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesUpdateTime.setStatus("mandatory")


class _VmsStatesUpdateInterval_Type(Integer32):
    """Custom type vmsStatesUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsStatesUpdateInterval_Object = MibScalar
vmsStatesUpdateInterval = _VmsStatesUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 2),
    _VmsStatesUpdateInterval_Type()
)
vmsStatesUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsStatesUpdateInterval.setStatus("mandatory")
_VmsStatesCOLPG_Type = Counter32
_VmsStatesCOLPG_Object = MibScalar
vmsStatesCOLPG = _VmsStatesCOLPG_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 3),
    _VmsStatesCOLPG_Type()
)
vmsStatesCOLPG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesCOLPG.setStatus("mandatory")
_VmsStatesMWAIT_Type = Counter32
_VmsStatesMWAIT_Object = MibScalar
vmsStatesMWAIT = _VmsStatesMWAIT_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 4),
    _VmsStatesMWAIT_Type()
)
vmsStatesMWAIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesMWAIT.setStatus("mandatory")
_VmsStatesCEF_Type = Counter32
_VmsStatesCEF_Object = MibScalar
vmsStatesCEF = _VmsStatesCEF_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 5),
    _VmsStatesCEF_Type()
)
vmsStatesCEF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesCEF.setStatus("mandatory")
_VmsStatesPFW_Type = Counter32
_VmsStatesPFW_Object = MibScalar
vmsStatesPFW = _VmsStatesPFW_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 6),
    _VmsStatesPFW_Type()
)
vmsStatesPFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesPFW.setStatus("mandatory")
_VmsStatesLEF_Type = Counter32
_VmsStatesLEF_Object = MibScalar
vmsStatesLEF = _VmsStatesLEF_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 7),
    _VmsStatesLEF_Type()
)
vmsStatesLEF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesLEF.setStatus("mandatory")
_VmsStatesLEFO_Type = Counter32
_VmsStatesLEFO_Object = MibScalar
vmsStatesLEFO = _VmsStatesLEFO_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 8),
    _VmsStatesLEFO_Type()
)
vmsStatesLEFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesLEFO.setStatus("mandatory")
_VmsStatesHIB_Type = Counter32
_VmsStatesHIB_Object = MibScalar
vmsStatesHIB = _VmsStatesHIB_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 9),
    _VmsStatesHIB_Type()
)
vmsStatesHIB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesHIB.setStatus("mandatory")
_VmsStatesHIBO_Type = Counter32
_VmsStatesHIBO_Object = MibScalar
vmsStatesHIBO = _VmsStatesHIBO_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 10),
    _VmsStatesHIBO_Type()
)
vmsStatesHIBO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesHIBO.setStatus("mandatory")
_VmsStatesSUSP_Type = Counter32
_VmsStatesSUSP_Object = MibScalar
vmsStatesSUSP = _VmsStatesSUSP_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 11),
    _VmsStatesSUSP_Type()
)
vmsStatesSUSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesSUSP.setStatus("mandatory")
_VmsStatesSUSPO_Type = Counter32
_VmsStatesSUSPO_Object = MibScalar
vmsStatesSUSPO = _VmsStatesSUSPO_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 12),
    _VmsStatesSUSPO_Type()
)
vmsStatesSUSPO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesSUSPO.setStatus("mandatory")
_VmsStatesFPG_Type = Counter32
_VmsStatesFPG_Object = MibScalar
vmsStatesFPG = _VmsStatesFPG_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 13),
    _VmsStatesFPG_Type()
)
vmsStatesFPG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesFPG.setStatus("mandatory")
_VmsStatesCOM_Type = Counter32
_VmsStatesCOM_Object = MibScalar
vmsStatesCOM = _VmsStatesCOM_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 14),
    _VmsStatesCOM_Type()
)
vmsStatesCOM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesCOM.setStatus("mandatory")
_VmsStatesCOMO_Type = Counter32
_VmsStatesCOMO_Object = MibScalar
vmsStatesCOMO = _VmsStatesCOMO_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 15),
    _VmsStatesCOMO_Type()
)
vmsStatesCOMO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesCOMO.setStatus("mandatory")
_VmsStatesCUR_Type = Counter32
_VmsStatesCUR_Object = MibScalar
vmsStatesCUR = _VmsStatesCUR_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 7, 16),
    _VmsStatesCUR_Type()
)
vmsStatesCUR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsStatesCUR.setStatus("mandatory")
_VmsCluster_ObjectIdentity = ObjectIdentity
vmsCluster = _VmsCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8)
)
_VmsClusterUpdateTime_Type = TimeTicks
_VmsClusterUpdateTime_Object = MibScalar
vmsClusterUpdateTime = _VmsClusterUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 1),
    _VmsClusterUpdateTime_Type()
)
vmsClusterUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterUpdateTime.setStatus("mandatory")


class _VmsClusterUpdateInterval_Type(Integer32):
    """Custom type vmsClusterUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsClusterUpdateInterval_Object = MibScalar
vmsClusterUpdateInterval = _VmsClusterUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 2),
    _VmsClusterUpdateInterval_Type()
)
vmsClusterUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsClusterUpdateInterval.setStatus("mandatory")
_VmsClusterCpuBusy_Type = Integer32
_VmsClusterCpuBusy_Object = MibScalar
vmsClusterCpuBusy = _VmsClusterCpuBusy_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 3),
    _VmsClusterCpuBusy_Type()
)
vmsClusterCpuBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterCpuBusy.setStatus("mandatory")
_VmsClusterFreeListSize_Type = Integer32
_VmsClusterFreeListSize_Object = MibScalar
vmsClusterFreeListSize = _VmsClusterFreeListSize_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 4),
    _VmsClusterFreeListSize_Type()
)
vmsClusterFreeListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterFreeListSize.setStatus("mandatory")
_VmsClusterTotalLocks_Type = Integer32
_VmsClusterTotalLocks_Object = MibScalar
vmsClusterTotalLocks = _VmsClusterTotalLocks_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 5),
    _VmsClusterTotalLocks_Type()
)
vmsClusterTotalLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterTotalLocks.setStatus("mandatory")
_VmsClusterNewEnqLocal_Type = Counter32
_VmsClusterNewEnqLocal_Object = MibScalar
vmsClusterNewEnqLocal = _VmsClusterNewEnqLocal_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 6),
    _VmsClusterNewEnqLocal_Type()
)
vmsClusterNewEnqLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterNewEnqLocal.setStatus("mandatory")
_VmsClusterNewEnqIncoming_Type = Counter32
_VmsClusterNewEnqIncoming_Object = MibScalar
vmsClusterNewEnqIncoming = _VmsClusterNewEnqIncoming_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 7),
    _VmsClusterNewEnqIncoming_Type()
)
vmsClusterNewEnqIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterNewEnqIncoming.setStatus("mandatory")
_VmsClusterNewEnqOutgoing_Type = Counter32
_VmsClusterNewEnqOutgoing_Object = MibScalar
vmsClusterNewEnqOutgoing = _VmsClusterNewEnqOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 8),
    _VmsClusterNewEnqOutgoing_Type()
)
vmsClusterNewEnqOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterNewEnqOutgoing.setStatus("mandatory")
_VmsClusterEnqConversionsLocal_Type = Counter32
_VmsClusterEnqConversionsLocal_Object = MibScalar
vmsClusterEnqConversionsLocal = _VmsClusterEnqConversionsLocal_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 9),
    _VmsClusterEnqConversionsLocal_Type()
)
vmsClusterEnqConversionsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterEnqConversionsLocal.setStatus("mandatory")
_VmsClusterEnqConversionsIncoming_Type = Counter32
_VmsClusterEnqConversionsIncoming_Object = MibScalar
vmsClusterEnqConversionsIncoming = _VmsClusterEnqConversionsIncoming_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 10),
    _VmsClusterEnqConversionsIncoming_Type()
)
vmsClusterEnqConversionsIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterEnqConversionsIncoming.setStatus("mandatory")
_VmsClusterEnqConversionsOutgoing_Type = Counter32
_VmsClusterEnqConversionsOutgoing_Object = MibScalar
vmsClusterEnqConversionsOutgoing = _VmsClusterEnqConversionsOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 11),
    _VmsClusterEnqConversionsOutgoing_Type()
)
vmsClusterEnqConversionsOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterEnqConversionsOutgoing.setStatus("mandatory")
_VmsClusterDeqLocal_Type = Counter32
_VmsClusterDeqLocal_Object = MibScalar
vmsClusterDeqLocal = _VmsClusterDeqLocal_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 12),
    _VmsClusterDeqLocal_Type()
)
vmsClusterDeqLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterDeqLocal.setStatus("mandatory")
_VmsClusterDeqIncoming_Type = Counter32
_VmsClusterDeqIncoming_Object = MibScalar
vmsClusterDeqIncoming = _VmsClusterDeqIncoming_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 13),
    _VmsClusterDeqIncoming_Type()
)
vmsClusterDeqIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterDeqIncoming.setStatus("mandatory")
_VmsClusterDeqOutgoing_Type = Counter32
_VmsClusterDeqOutgoing_Object = MibScalar
vmsClusterDeqOutgoing = _VmsClusterDeqOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 8, 14),
    _VmsClusterDeqOutgoing_Type()
)
vmsClusterDeqOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsClusterDeqOutgoing.setStatus("mandatory")
_VmsMscp_ObjectIdentity = ObjectIdentity
vmsMscp = _VmsMscp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9)
)
_VmsMscpUpdateTime_Type = TimeTicks
_VmsMscpUpdateTime_Object = MibScalar
vmsMscpUpdateTime = _VmsMscpUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 1),
    _VmsMscpUpdateTime_Type()
)
vmsMscpUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscpUpdateTime.setStatus("mandatory")


class _VmsMscpUpdateInterval_Type(Integer32):
    """Custom type vmsMscpUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsMscpUpdateInterval_Object = MibScalar
vmsMscpUpdateInterval = _VmsMscpUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 2),
    _VmsMscpUpdateInterval_Type()
)
vmsMscpUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsMscpUpdateInterval.setStatus("mandatory")
_VmsMscpRequests_Type = Counter32
_VmsMscpRequests_Object = MibScalar
vmsMscpRequests = _VmsMscpRequests_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 3),
    _VmsMscpRequests_Type()
)
vmsMscpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscpRequests.setStatus("mandatory")
_VmsMscpReads_Type = Counter32
_VmsMscpReads_Object = MibScalar
vmsMscpReads = _VmsMscpReads_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 4),
    _VmsMscpReads_Type()
)
vmsMscpReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscpReads.setStatus("mandatory")
_VmsMscpWrites_Type = Counter32
_VmsMscpWrites_Object = MibScalar
vmsMscpWrites = _VmsMscpWrites_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 5),
    _VmsMscpWrites_Type()
)
vmsMscpWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscpWrites.setStatus("mandatory")
_VmsMscpFragments_Type = Counter32
_VmsMscpFragments_Object = MibScalar
vmsMscpFragments = _VmsMscpFragments_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 6),
    _VmsMscpFragments_Type()
)
vmsMscpFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscpFragments.setStatus("mandatory")
_VmsMscpSplits_Type = Counter32
_VmsMscpSplits_Object = MibScalar
vmsMscpSplits = _VmsMscpSplits_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 7),
    _VmsMscpSplits_Type()
)
vmsMscpSplits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscpSplits.setStatus("mandatory")
_VmsMscpBufferWaits_Type = Counter32
_VmsMscpBufferWaits_Object = MibScalar
vmsMscpBufferWaits = _VmsMscpBufferWaits_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 8),
    _VmsMscpBufferWaits_Type()
)
vmsMscpBufferWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscpBufferWaits.setStatus("mandatory")
_VmsMscp1BlockIOs_Type = Counter32
_VmsMscp1BlockIOs_Object = MibScalar
vmsMscp1BlockIOs = _VmsMscp1BlockIOs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 9),
    _VmsMscp1BlockIOs_Type()
)
vmsMscp1BlockIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscp1BlockIOs.setStatus("mandatory")
_VmsMscp2_3BlockIOs_Type = Counter32
_VmsMscp2_3BlockIOs_Object = MibScalar
vmsMscp2_3BlockIOs = _VmsMscp2_3BlockIOs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 10),
    _VmsMscp2_3BlockIOs_Type()
)
vmsMscp2_3BlockIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscp2_3BlockIOs.setStatus("mandatory")
_VmsMscp4_7BlockIOs_Type = Counter32
_VmsMscp4_7BlockIOs_Object = MibScalar
vmsMscp4_7BlockIOs = _VmsMscp4_7BlockIOs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 11),
    _VmsMscp4_7BlockIOs_Type()
)
vmsMscp4_7BlockIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscp4_7BlockIOs.setStatus("mandatory")
_VmsMscp8_15BlockIOs_Type = Counter32
_VmsMscp8_15BlockIOs_Object = MibScalar
vmsMscp8_15BlockIOs = _VmsMscp8_15BlockIOs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 12),
    _VmsMscp8_15BlockIOs_Type()
)
vmsMscp8_15BlockIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscp8_15BlockIOs.setStatus("mandatory")
_VmsMscp16_31BlockIOs_Type = Counter32
_VmsMscp16_31BlockIOs_Object = MibScalar
vmsMscp16_31BlockIOs = _VmsMscp16_31BlockIOs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 13),
    _VmsMscp16_31BlockIOs_Type()
)
vmsMscp16_31BlockIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscp16_31BlockIOs.setStatus("mandatory")
_VmsMscp32_63BlockIOs_Type = Counter32
_VmsMscp32_63BlockIOs_Object = MibScalar
vmsMscp32_63BlockIOs = _VmsMscp32_63BlockIOs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 14),
    _VmsMscp32_63BlockIOs_Type()
)
vmsMscp32_63BlockIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscp32_63BlockIOs.setStatus("mandatory")
_VmsMscp64andOverBlockIOs_Type = Counter32
_VmsMscp64andOverBlockIOs_Object = MibScalar
vmsMscp64andOverBlockIOs = _VmsMscp64andOverBlockIOs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 9, 15),
    _VmsMscp64andOverBlockIOs_Type()
)
vmsMscp64andOverBlockIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsMscp64andOverBlockIOs.setStatus("mandatory")
_VmsLock_ObjectIdentity = ObjectIdentity
vmsLock = _VmsLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10)
)
_VmsLockUpdateTime_Type = TimeTicks
_VmsLockUpdateTime_Object = MibScalar
vmsLockUpdateTime = _VmsLockUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 1),
    _VmsLockUpdateTime_Type()
)
vmsLockUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsLockUpdateTime.setStatus("mandatory")


class _VmsLockUpdateInterval_Type(Integer32):
    """Custom type vmsLockUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsLockUpdateInterval_Object = MibScalar
vmsLockUpdateInterval = _VmsLockUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 2),
    _VmsLockUpdateInterval_Type()
)
vmsLockUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsLockUpdateInterval.setStatus("mandatory")
_VmsLockNewEnqs_Type = Counter32
_VmsLockNewEnqs_Object = MibScalar
vmsLockNewEnqs = _VmsLockNewEnqs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 3),
    _VmsLockNewEnqs_Type()
)
vmsLockNewEnqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsLockNewEnqs.setStatus("mandatory")
_VmsLockConvertedEnqs_Type = Counter32
_VmsLockConvertedEnqs_Object = MibScalar
vmsLockConvertedEnqs = _VmsLockConvertedEnqs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 4),
    _VmsLockConvertedEnqs_Type()
)
vmsLockConvertedEnqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsLockConvertedEnqs.setStatus("mandatory")
_VmsLockDeqs_Type = Counter32
_VmsLockDeqs_Object = MibScalar
vmsLockDeqs = _VmsLockDeqs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 5),
    _VmsLockDeqs_Type()
)
vmsLockDeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsLockDeqs.setStatus("mandatory")
_VmsLockBlockingASTs_Type = Counter32
_VmsLockBlockingASTs_Object = MibScalar
vmsLockBlockingASTs = _VmsLockBlockingASTs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 6),
    _VmsLockBlockingASTs_Type()
)
vmsLockBlockingASTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsLockBlockingASTs.setStatus("mandatory")
_VmsLockEnqWaits_Type = Counter32
_VmsLockEnqWaits_Object = MibScalar
vmsLockEnqWaits = _VmsLockEnqWaits_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 7),
    _VmsLockEnqWaits_Type()
)
vmsLockEnqWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsLockEnqWaits.setStatus("mandatory")
_VmsLockEnqsNotQueued_Type = Counter32
_VmsLockEnqsNotQueued_Object = MibScalar
vmsLockEnqsNotQueued = _VmsLockEnqsNotQueued_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 8),
    _VmsLockEnqsNotQueued_Type()
)
vmsLockEnqsNotQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsLockEnqsNotQueued.setStatus("mandatory")
_VmsLockDeadlockSearches_Type = Counter32
_VmsLockDeadlockSearches_Object = MibScalar
vmsLockDeadlockSearches = _VmsLockDeadlockSearches_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 9),
    _VmsLockDeadlockSearches_Type()
)
vmsLockDeadlockSearches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsLockDeadlockSearches.setStatus("mandatory")
_VmsLockDeadlocksFound_Type = Counter32
_VmsLockDeadlocksFound_Object = MibScalar
vmsLockDeadlocksFound = _VmsLockDeadlocksFound_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 10),
    _VmsLockDeadlocksFound_Type()
)
vmsLockDeadlocksFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsLockDeadlocksFound.setStatus("mandatory")
_VmsLockCurrentLocks_Type = Integer32
_VmsLockCurrentLocks_Object = MibScalar
vmsLockCurrentLocks = _VmsLockCurrentLocks_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 11),
    _VmsLockCurrentLocks_Type()
)
vmsLockCurrentLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsLockCurrentLocks.setStatus("mandatory")
_VmsLockCurrentResources_Type = Integer32
_VmsLockCurrentResources_Object = MibScalar
vmsLockCurrentResources = _VmsLockCurrentResources_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 10, 12),
    _VmsLockCurrentResources_Type()
)
vmsLockCurrentResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsLockCurrentResources.setStatus("mandatory")
_VmsDlock_ObjectIdentity = ObjectIdentity
vmsDlock = _VmsDlock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11)
)
_VmsDlockUpdateTime_Type = TimeTicks
_VmsDlockUpdateTime_Object = MibScalar
vmsDlockUpdateTime = _VmsDlockUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 1),
    _VmsDlockUpdateTime_Type()
)
vmsDlockUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockUpdateTime.setStatus("mandatory")


class _VmsDlockUpdateInterval_Type(Integer32):
    """Custom type vmsDlockUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsDlockUpdateInterval_Object = MibScalar
vmsDlockUpdateInterval = _VmsDlockUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 2),
    _VmsDlockUpdateInterval_Type()
)
vmsDlockUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsDlockUpdateInterval.setStatus("mandatory")
_VmsDlockNewLocksLocal_Type = Counter32
_VmsDlockNewLocksLocal_Object = MibScalar
vmsDlockNewLocksLocal = _VmsDlockNewLocksLocal_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 3),
    _VmsDlockNewLocksLocal_Type()
)
vmsDlockNewLocksLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockNewLocksLocal.setStatus("mandatory")
_VmsDlockNewLocksIncoming_Type = Counter32
_VmsDlockNewLocksIncoming_Object = MibScalar
vmsDlockNewLocksIncoming = _VmsDlockNewLocksIncoming_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 4),
    _VmsDlockNewLocksIncoming_Type()
)
vmsDlockNewLocksIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockNewLocksIncoming.setStatus("mandatory")
_VmsDlockNewLocksOutgoing_Type = Counter32
_VmsDlockNewLocksOutgoing_Object = MibScalar
vmsDlockNewLocksOutgoing = _VmsDlockNewLocksOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 5),
    _VmsDlockNewLocksOutgoing_Type()
)
vmsDlockNewLocksOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockNewLocksOutgoing.setStatus("mandatory")
_VmsDlockLockConversionsLocal_Type = Counter32
_VmsDlockLockConversionsLocal_Object = MibScalar
vmsDlockLockConversionsLocal = _VmsDlockLockConversionsLocal_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 6),
    _VmsDlockLockConversionsLocal_Type()
)
vmsDlockLockConversionsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockLockConversionsLocal.setStatus("mandatory")
_VmsDlockLockConversionsIncoming_Type = Counter32
_VmsDlockLockConversionsIncoming_Object = MibScalar
vmsDlockLockConversionsIncoming = _VmsDlockLockConversionsIncoming_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 7),
    _VmsDlockLockConversionsIncoming_Type()
)
vmsDlockLockConversionsIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockLockConversionsIncoming.setStatus("mandatory")
_VmsDlockLockConversionsOutgoing_Type = Counter32
_VmsDlockLockConversionsOutgoing_Object = MibScalar
vmsDlockLockConversionsOutgoing = _VmsDlockLockConversionsOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 8),
    _VmsDlockLockConversionsOutgoing_Type()
)
vmsDlockLockConversionsOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockLockConversionsOutgoing.setStatus("mandatory")
_VmsDlockUnlocksLocal_Type = Counter32
_VmsDlockUnlocksLocal_Object = MibScalar
vmsDlockUnlocksLocal = _VmsDlockUnlocksLocal_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 9),
    _VmsDlockUnlocksLocal_Type()
)
vmsDlockUnlocksLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockUnlocksLocal.setStatus("mandatory")
_VmsDlockUnlocksIncoming_Type = Counter32
_VmsDlockUnlocksIncoming_Object = MibScalar
vmsDlockUnlocksIncoming = _VmsDlockUnlocksIncoming_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 10),
    _VmsDlockUnlocksIncoming_Type()
)
vmsDlockUnlocksIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockUnlocksIncoming.setStatus("mandatory")
_VmsDlockUnlocksOutgoing_Type = Counter32
_VmsDlockUnlocksOutgoing_Object = MibScalar
vmsDlockUnlocksOutgoing = _VmsDlockUnlocksOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 11),
    _VmsDlockUnlocksOutgoing_Type()
)
vmsDlockUnlocksOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockUnlocksOutgoing.setStatus("mandatory")
_VmsDlockBlockingASTsLocal_Type = Counter32
_VmsDlockBlockingASTsLocal_Object = MibScalar
vmsDlockBlockingASTsLocal = _VmsDlockBlockingASTsLocal_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 12),
    _VmsDlockBlockingASTsLocal_Type()
)
vmsDlockBlockingASTsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockBlockingASTsLocal.setStatus("mandatory")
_VmsDlockBlockingASTsIncoming_Type = Counter32
_VmsDlockBlockingASTsIncoming_Object = MibScalar
vmsDlockBlockingASTsIncoming = _VmsDlockBlockingASTsIncoming_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 13),
    _VmsDlockBlockingASTsIncoming_Type()
)
vmsDlockBlockingASTsIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockBlockingASTsIncoming.setStatus("mandatory")
_VmsDlockBlockingASTsOutgoing_Type = Counter32
_VmsDlockBlockingASTsOutgoing_Object = MibScalar
vmsDlockBlockingASTsOutgoing = _VmsDlockBlockingASTsOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 14),
    _VmsDlockBlockingASTsOutgoing_Type()
)
vmsDlockBlockingASTsOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockBlockingASTsOutgoing.setStatus("mandatory")
_VmsDlockDirFuncIncoming_Type = Counter32
_VmsDlockDirFuncIncoming_Object = MibScalar
vmsDlockDirFuncIncoming = _VmsDlockDirFuncIncoming_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 15),
    _VmsDlockDirFuncIncoming_Type()
)
vmsDlockDirFuncIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockDirFuncIncoming.setStatus("mandatory")
_VmsDlockDirFuncOutgoing_Type = Counter32
_VmsDlockDirFuncOutgoing_Object = MibScalar
vmsDlockDirFuncOutgoing = _VmsDlockDirFuncOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 16),
    _VmsDlockDirFuncOutgoing_Type()
)
vmsDlockDirFuncOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockDirFuncOutgoing.setStatus("mandatory")
_VmsDlockDeadlockMessage_Type = Counter32
_VmsDlockDeadlockMessage_Object = MibScalar
vmsDlockDeadlockMessage = _VmsDlockDeadlockMessage_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 11, 17),
    _VmsDlockDeadlockMessage_Type()
)
vmsDlockDeadlockMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsDlockDeadlockMessage.setStatus("mandatory")
_VmsSystem_ObjectIdentity = ObjectIdentity
vmsSystem = _VmsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12)
)
_VmsSystemUpdateTime_Type = TimeTicks
_VmsSystemUpdateTime_Object = MibScalar
vmsSystemUpdateTime = _VmsSystemUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12, 1),
    _VmsSystemUpdateTime_Type()
)
vmsSystemUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSystemUpdateTime.setStatus("mandatory")


class _VmsSystemUpdateInterval_Type(Integer32):
    """Custom type vmsSystemUpdateInterval based on Integer32"""
    defaultValue = 1


_VmsSystemUpdateInterval_Object = MibScalar
vmsSystemUpdateInterval = _VmsSystemUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12, 2),
    _VmsSystemUpdateInterval_Type()
)
vmsSystemUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsSystemUpdateInterval.setStatus("mandatory")
_VmsSystemCpuBusy_Type = Counter32
_VmsSystemCpuBusy_Object = MibScalar
vmsSystemCpuBusy = _VmsSystemCpuBusy_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12, 3),
    _VmsSystemCpuBusy_Type()
)
vmsSystemCpuBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSystemCpuBusy.setStatus("mandatory")
_VmsSystemOtherStates_Type = Integer32
_VmsSystemOtherStates_Object = MibScalar
vmsSystemOtherStates = _VmsSystemOtherStates_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12, 4),
    _VmsSystemOtherStates_Type()
)
vmsSystemOtherStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSystemOtherStates.setStatus("mandatory")
_VmsSystemProcessCount_Type = Integer32
_VmsSystemProcessCount_Object = MibScalar
vmsSystemProcessCount = _VmsSystemProcessCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12, 5),
    _VmsSystemProcessCount_Type()
)
vmsSystemProcessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSystemProcessCount.setStatus("mandatory")
_VmsSystemPageFaults_Type = Counter32
_VmsSystemPageFaults_Object = MibScalar
vmsSystemPageFaults = _VmsSystemPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12, 6),
    _VmsSystemPageFaults_Type()
)
vmsSystemPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSystemPageFaults.setStatus("mandatory")
_VmsSystemReadIOs_Type = Counter32
_VmsSystemReadIOs_Object = MibScalar
vmsSystemReadIOs = _VmsSystemReadIOs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12, 7),
    _VmsSystemReadIOs_Type()
)
vmsSystemReadIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSystemReadIOs.setStatus("mandatory")
_VmsSystemFreePageCount_Type = Integer32
_VmsSystemFreePageCount_Object = MibScalar
vmsSystemFreePageCount = _VmsSystemFreePageCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12, 8),
    _VmsSystemFreePageCount_Type()
)
vmsSystemFreePageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSystemFreePageCount.setStatus("mandatory")
_VmsSystemModifiedPageCount_Type = Integer32
_VmsSystemModifiedPageCount_Object = MibScalar
vmsSystemModifiedPageCount = _VmsSystemModifiedPageCount_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12, 9),
    _VmsSystemModifiedPageCount_Type()
)
vmsSystemModifiedPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSystemModifiedPageCount.setStatus("mandatory")
_VmsSystemDirectIOs_Type = Counter32
_VmsSystemDirectIOs_Object = MibScalar
vmsSystemDirectIOs = _VmsSystemDirectIOs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12, 10),
    _VmsSystemDirectIOs_Type()
)
vmsSystemDirectIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSystemDirectIOs.setStatus("mandatory")
_VmsSystemBufferedIOs_Type = Counter32
_VmsSystemBufferedIOs_Object = MibScalar
vmsSystemBufferedIOs = _VmsSystemBufferedIOs_Object(
    (1, 3, 6, 1, 4, 1, 597, 4, 15, 12, 11),
    _VmsSystemBufferedIOs_Type()
)
vmsSystemBufferedIOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSystemBufferedIOs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMTEK-VMS-NM-SYSMGR-MIB",
    **{"comtek": comtek,
       "comtekVms": comtekVms,
       "comtekVmsNMSysMgrMib": comtekVmsNMSysMgrMib,
       "sResources": sResources,
       "sSyi": sSyi,
       "sSyiNodeName": sSyiNodeName,
       "sSyiHwName": sSyiHwName,
       "sSyiBootTime": sSyiBootTime,
       "sSyiVersion": sSyiVersion,
       "sSyiMemSize": sSyiMemSize,
       "sSyiAvailCpuCnt": sSyiAvailCpuCnt,
       "sSyiActiveCpuCnt": sSyiActiveCpuCnt,
       "sSyiPgSize": sSyiPgSize,
       "sSyiPgFree": sSyiPgFree,
       "sSyiPgUsedPercent": sSyiPgUsedPercent,
       "sSyiSwpSize": sSyiSwpSize,
       "sSyiSwpFree": sSyiSwpFree,
       "sSyiSwpUsedPercent": sSyiSwpUsedPercent,
       "sSyiCpuPgSize": sSyiCpuPgSize,
       "sSyiTime": sSyiTime,
       "sSyiMemFreePg": sSyiMemFreePg,
       "sSyiMemUsed": sSyiMemUsed,
       "sCpu": sCpu,
       "sCpuPercentUsed": sCpuPercentUsed,
       "sIntPercentUsed": sIntPercentUsed,
       "sCpuTicks": sCpuTicks,
       "sCpuLoadOneMinute": sCpuLoadOneMinute,
       "sKernelOne": sKernelOne,
       "sExecOne": sExecOne,
       "sSuprOne": sSuprOne,
       "sUserOne": sUserOne,
       "sIntrOne": sIntrOne,
       "sCompOne": sCompOne,
       "sSpinOne": sSpinOne,
       "sNullOne": sNullOne,
       "sCpuLoadFiveMinute": sCpuLoadFiveMinute,
       "sKernelFive": sKernelFive,
       "sExecFive": sExecFive,
       "sSuprFive": sSuprFive,
       "sUserFive": sUserFive,
       "sIntrFive": sIntrFive,
       "sCompFive": sCompFive,
       "sSpinFive": sSpinFive,
       "sNullFive": sNullFive,
       "sCpuLoadFifteenMinute": sCpuLoadFifteenMinute,
       "sKernelFifteen": sKernelFifteen,
       "sExecFifteen": sExecFifteen,
       "sSuprFifteen": sSuprFifteen,
       "sUserFifteen": sUserFifteen,
       "sIntrFifteen": sIntrFifteen,
       "sCompFifteen": sCompFifteen,
       "sSpinFifteen": sSpinFifteen,
       "sNullFifteen": sNullFifteen,
       "sDsk": sDsk,
       "sDskTblCnt": sDskTblCnt,
       "sDskTblTime": sDskTblTime,
       "sDskTbl": sDskTbl,
       "sDskEntry": sDskEntry,
       "sDskIndex": sDskIndex,
       "sDskName": sDskName,
       "sDskUsedPercent": sDskUsedPercent,
       "sDskOps": sDskOps,
       "sDskMountCnt": sDskMountCnt,
       "sDskRefCnt": sDskRefCnt,
       "sDskTransCnt": sDskTransCnt,
       "sDskMediaName": sDskMediaName,
       "sDskOpCnt": sDskOpCnt,
       "sDskFreeBlocks": sDskFreeBlocks,
       "sDskMaxBlocks": sDskMaxBlocks,
       "sDskStatus": sDskStatus,
       "sDskDevChar": sDskDevChar,
       "sDskLogVolName": sDskLogVolName,
       "sDskTrapPercent": sDskTrapPercent,
       "sDskTrapBlocks": sDskTrapBlocks,
       "sDskShdCount": sDskShdCount,
       "sDskTrapOpSec": sDskTrapOpSec,
       "sDskQueueLength": sDskQueueLength,
       "sDskRemote": sDskRemote,
       "sShd": sShd,
       "sShdTbl": sShdTbl,
       "sShdEntry": sShdEntry,
       "sShdIndex": sShdIndex,
       "sShdName": sShdName,
       "sShdFail": sShdFail,
       "sShdCopy": sShdCopy,
       "sShdMerge": sShdMerge,
       "sQue": sQue,
       "sQueCnt": sQueCnt,
       "sQueTime": sQueTime,
       "sQTbl": sQTbl,
       "sQTblEntry": sQTblEntry,
       "sQIndex": sQIndex,
       "sQName": sQName,
       "sQMonitor": sQMonitor,
       "sQStatus": sQStatus,
       "sQEntryCount": sQEntryCount,
       "sQEntryTbl": sQEntryTbl,
       "sQEntry": sQEntry,
       "sQEntryNum": sQEntryNum,
       "sQEntryJobname": sQEntryJobname,
       "sQEntryJobStatus": sQEntryJobStatus,
       "sQueBatch": sQueBatch,
       "sQueBatchPending": sQueBatchPending,
       "sQueBatchExecuting": sQueBatchExecuting,
       "sQueBatchTimed": sQueBatchTimed,
       "sQueBatchHolding": sQueBatchHolding,
       "sQueBatchRetained": sQueBatchRetained,
       "sQueGeneric": sQueGeneric,
       "sQueGenericPending": sQueGenericPending,
       "sQueGenericExecuting": sQueGenericExecuting,
       "sQueGenericTimed": sQueGenericTimed,
       "sQueGenericHolding": sQueGenericHolding,
       "sQueGenericRetained": sQueGenericRetained,
       "sQuePrinter": sQuePrinter,
       "sQuePrinterPending": sQuePrinterPending,
       "sQuePrinterExecuting": sQuePrinterExecuting,
       "sQuePrinterTimed": sQuePrinterTimed,
       "sQuePrinterHolding": sQuePrinterHolding,
       "sQuePrinterRetained": sQuePrinterRetained,
       "sQueServer": sQueServer,
       "sQueServerPending": sQueServerPending,
       "sQueServerExecuting": sQueServerExecuting,
       "sQueServerTimed": sQueServerTimed,
       "sQueServerHolding": sQueServerHolding,
       "sQueServerRetained": sQueServerRetained,
       "sQueSymbiont": sQueSymbiont,
       "sQueSymbiontPending": sQueSymbiontPending,
       "sQueSymbiontExecuting": sQueSymbiontExecuting,
       "sQueSymbiontTimed": sQueSymbiontTimed,
       "sQueSymbiontHolding": sQueSymbiontHolding,
       "sQueSymbiontRetained": sQueSymbiontRetained,
       "sQueTerminal": sQueTerminal,
       "sQueTerminalPending": sQueTerminalPending,
       "sQueTerminalExecuting": sQueTerminalExecuting,
       "sQueTerminalTimed": sQueTerminalTimed,
       "sQueTerminalHolding": sQueTerminalHolding,
       "sQueTerminalRetained": sQueTerminalRetained,
       "sQMan": sQMan,
       "sQManCount": sQManCount,
       "sQManTbl": sQManTbl,
       "sQManTblEntry": sQManTblEntry,
       "sQManIndex": sQManIndex,
       "sQManName": sQManName,
       "sQManStatus": sQManStatus,
       "sProcesses": sProcesses,
       "sProcInfo": sProcInfo,
       "sPsCnt": sPsCnt,
       "sPsTime": sPsTime,
       "sPsTbl": sPsTbl,
       "sPsEntry": sPsEntry,
       "sPsPID": sPsPID,
       "sPsProcName": sPsProcName,
       "sPsState": sPsState,
       "sPsPriority": sPsPriority,
       "sPsDirectIO": sPsDirectIO,
       "sPsCpuTime": sPsCpuTime,
       "sPsPgFaults": sPsPgFaults,
       "sPsWorkSetSize": sPsWorkSetSize,
       "sPsUsername": sPsUsername,
       "sPsPhysTerm": sPsPhysTerm,
       "sPsImageName": sPsImageName,
       "sPsLoginTime": sPsLoginTime,
       "sPsPgTblCnt": sPsPgTblCnt,
       "sPsMode": sPsMode,
       "sPsRWState": sPsRWState,
       "sPsCOMQueue": sPsCOMQueue,
       "sPsCOMOQueue": sPsCOMOQueue,
       "sPsOther": sPsOther,
       "sPsNetwork": sPsNetwork,
       "sPsBatch": sPsBatch,
       "sPsInteractive": sPsInteractive,
       "sPsAvailProcSlots": sPsAvailProcSlots,
       "sCritInfo": sCritInfo,
       "sCritCnt": sCritCnt,
       "sCritTime": sCritTime,
       "sCritTbl": sCritTbl,
       "sCritEntry": sCritEntry,
       "sCritIndex": sCritIndex,
       "sCritName": sCritName,
       "sCritReqCnt": sCritReqCnt,
       "sCritCurCnt": sCritCurCnt,
       "sTrapInfo": sTrapInfo,
       "sTrapNextSeqNum": sTrapNextSeqNum,
       "sTrapTime": sTrapTime,
       "sTrapResendSeqNum": sTrapResendSeqNum,
       "sTrapLastSeqNumSent": sTrapLastSeqNumSent,
       "sTrapLostCount": sTrapLostCount,
       "sErrInfo": sErrInfo,
       "sHwErrInfo": sHwErrInfo,
       "sHwErrDeviceCnt": sHwErrDeviceCnt,
       "sHwErrTime": sHwErrTime,
       "sHwErrTbl": sHwErrTbl,
       "sHwErrEntry": sHwErrEntry,
       "sHwErrIndex": sHwErrIndex,
       "sHwErrDeviceName": sHwErrDeviceName,
       "sHwErrCnt": sHwErrCnt,
       "sHwErrLastTime": sHwErrLastTime,
       "sSwErrInfo": sSwErrInfo,
       "sSwErrStatus": sSwErrStatus,
       "sSwErrFile": sSwErrFile,
       "sSwErrLineNum": sSwErrLineNum,
       "sSwErrLastTime": sSwErrLastTime,
       "sSwErrMessage": sSwErrMessage,
       "sOpcomOne": sOpcomOne,
       "sOpcomTwo": sOpcomTwo,
       "sOpcomThree": sOpcomThree,
       "sOpcomFour": sOpcomFour,
       "sOpcomFive": sOpcomFive,
       "sOpcomReplyId": sOpcomReplyId,
       "sOpcomReplyStatus": sOpcomReplyStatus,
       "sOpcomReplyText": sOpcomReplyText,
       "sOpcomReplySend": sOpcomReplySend,
       "sOpcomSix": sOpcomSix,
       "sOpcomSeven": sOpcomSeven,
       "sCfg": sCfg,
       "sCfgFile": sCfgFile,
       "sCfgLogFile": sCfgLogFile,
       "sCfgCritFile": sCfgCritFile,
       "sCfgReinitSubagent": sCfgReinitSubagent,
       "sCfgTraps": sCfgTraps,
       "sCfgHwErrTraps": sCfgHwErrTraps,
       "sCfgCpuLimit": sCfgCpuLimit,
       "sCfgIntLimit": sCfgIntLimit,
       "sCfgDskOps": sCfgDskOps,
       "sCfgDskLimit": sCfgDskLimit,
       "sCfgPgLimit": sCfgPgLimit,
       "sCfgSwpLimit": sCfgSwpLimit,
       "sCfgPsTimer": sCfgPsTimer,
       "sCfgDskTimer": sCfgDskTimer,
       "sCfgHwErrTimer": sCfgHwErrTimer,
       "sCfgSysInfoTimer": sCfgSysInfoTimer,
       "sCfgCritTimer": sCfgCritTimer,
       "sCfgDskAlarm": sCfgDskAlarm,
       "sCfgCritAlarm": sCfgCritAlarm,
       "sCfgTrapTblSize": sCfgTrapTblSize,
       "sCfgHostName": sCfgHostName,
       "sCfgAllPsData": sCfgAllPsData,
       "sCfgTimeout": sCfgTimeout,
       "sCfgOpcomSecurity": sCfgOpcomSecurity,
       "sCfgControlTermProc": sCfgControlTermProc,
       "sCfgTermProc": sCfgTermProc,
       "sCfgVersion": sCfgVersion,
       "sCfgUpTime": sCfgUpTime,
       "sCfgMaxTrapSec": sCfgMaxTrapSec,
       "sCfgCritDsk": sCfgCritDsk,
       "sCfgCritQue": sCfgCritQue,
       "sCfgQueTimer": sCfgQueTimer,
       "sCfgDskMinFreeBlks": sCfgDskMinFreeBlks,
       "sCfgMemLimit": sCfgMemLimit,
       "sCfgCOMQueueLimit": sCfgCOMQueueLimit,
       "sCfgCOMOQueueLimit": sCfgCOMOQueueLimit,
       "sCfgOpcomCards": sCfgOpcomCards,
       "sCfgOpcomCentral": sCfgOpcomCentral,
       "sCfgOpcomCluster": sCfgOpcomCluster,
       "sCfgOpcomDevices": sCfgOpcomDevices,
       "sCfgOpcomDisks": sCfgOpcomDisks,
       "sCfgOpcomLicense": sCfgOpcomLicense,
       "sCfgOpcomNetwork": sCfgOpcomNetwork,
       "sCfgOpcomOper1": sCfgOpcomOper1,
       "sCfgOpcomOper2": sCfgOpcomOper2,
       "sCfgOpcomOper3": sCfgOpcomOper3,
       "sCfgOpcomOper4": sCfgOpcomOper4,
       "sCfgOpcomOper5": sCfgOpcomOper5,
       "sCfgOpcomOper6": sCfgOpcomOper6,
       "sCfgOpcomOper7": sCfgOpcomOper7,
       "sCfgOpcomOper8": sCfgOpcomOper8,
       "sCfgOpcomOper9": sCfgOpcomOper9,
       "sCfgOpcomOper10": sCfgOpcomOper10,
       "sCfgOpcomOper11": sCfgOpcomOper11,
       "sCfgOpcomOper12": sCfgOpcomOper12,
       "sCfgOpcomPrinter": sCfgOpcomPrinter,
       "sCfgOpcomTapes": sCfgOpcomTapes,
       "sCfgOpcomFilter": sCfgOpcomFilter,
       "sCfgLocalDisksOnly": sCfgLocalDisksOnly,
       "sCfgCritDisksOnly": sCfgCritDisksOnly,
       "comtekVmsNMVmsMonMib": comtekVmsNMVmsMonMib,
       "vmsModes": vmsModes,
       "vmsModeUpdateTime": vmsModeUpdateTime,
       "vmsModeUpdateInterval": vmsModeUpdateInterval,
       "vmsModeCpuCount": vmsModeCpuCount,
       "vmsModeTable": vmsModeTable,
       "vmsModeTableEntry": vmsModeTableEntry,
       "vmsModeCpuId": vmsModeCpuId,
       "vmsModeKernel": vmsModeKernel,
       "vmsModeExec": vmsModeExec,
       "vmsModeSuper": vmsModeSuper,
       "vmsModeUser": vmsModeUser,
       "vmsModeInter": vmsModeInter,
       "vmsModeMPSync": vmsModeMPSync,
       "vmsModeCompat": vmsModeCompat,
       "vmsModeIdle": vmsModeIdle,
       "vmsTotalModes": vmsTotalModes,
       "vmsTotalKernel": vmsTotalKernel,
       "vmsTotalExec": vmsTotalExec,
       "vmsTotalSuper": vmsTotalSuper,
       "vmsTotalUser": vmsTotalUser,
       "vmsTotalInter": vmsTotalInter,
       "vmsTotalMPSync": vmsTotalMPSync,
       "vmsTotalComp": vmsTotalComp,
       "vmsTotalIdle": vmsTotalIdle,
       "vmsFile": vmsFile,
       "vmsFileUpdateTime": vmsFileUpdateTime,
       "vmsFileUpdateInterval": vmsFileUpdateInterval,
       "vmsFileDirFCBHit": vmsFileDirFCBHit,
       "vmsFileDirFCBAttempt": vmsFileDirFCBAttempt,
       "vmsFileDirDataHit": vmsFileDirDataHit,
       "vmsFileDirDataAttempt": vmsFileDirDataAttempt,
       "vmsFileFileHdrHit": vmsFileFileHdrHit,
       "vmsFileFileHdrAttempt": vmsFileFileHdrAttempt,
       "vmsFileFileIdHit": vmsFileFileIdHit,
       "vmsFileFileIdAttempt": vmsFileFileIdAttempt,
       "vmsFileExtentHit": vmsFileExtentHit,
       "vmsFileExtentAttempt": vmsFileExtentAttempt,
       "vmsFileQuotaHit": vmsFileQuotaHit,
       "vmsFileQuotaAttempt": vmsFileQuotaAttempt,
       "vmsFileBitmapHit": vmsFileBitmapHit,
       "vmsFileBitmapAttempt": vmsFileBitmapAttempt,
       "vmsFcp": vmsFcp,
       "vmsFcpUpdateTime": vmsFcpUpdateTime,
       "vmsFcpUpdateInterval": vmsFcpUpdateInterval,
       "vmsFcpFCPCall": vmsFcpFCPCall,
       "vmsFcpAllocation": vmsFcpAllocation,
       "vmsFcpCreate": vmsFcpCreate,
       "vmsFcpDiskRead": vmsFcpDiskRead,
       "vmsFcpDiskWrite": vmsFcpDiskWrite,
       "vmsFcpVolumeLockWait": vmsFcpVolumeLockWait,
       "vmsFcpCPUTick": vmsFcpCPUTick,
       "vmsFcpPageFault": vmsFcpPageFault,
       "vmsFcpWindowTurn": vmsFcpWindowTurn,
       "vmsFcpLookup": vmsFcpLookup,
       "vmsFcpOpen": vmsFcpOpen,
       "vmsFcpErase": vmsFcpErase,
       "vmsIo": vmsIo,
       "vmsIoUpdateTime": vmsIoUpdateTime,
       "vmsIoUpdateInterval": vmsIoUpdateInterval,
       "vmsIoDirectIO": vmsIoDirectIO,
       "vmsIoBufferedIO": vmsIoBufferedIO,
       "vmsIoMailboxWrite": vmsIoMailboxWrite,
       "vmsIoSplitTransfer": vmsIoSplitTransfer,
       "vmsIoLogNameTranslation": vmsIoLogNameTranslation,
       "vmsIoFileOpen": vmsIoFileOpen,
       "vmsIoPageFault": vmsIoPageFault,
       "vmsIoPageRead": vmsIoPageRead,
       "vmsIoPageReadIO": vmsIoPageReadIO,
       "vmsIoPageWrite": vmsIoPageWrite,
       "vmsIoPageWriteIO": vmsIoPageWriteIO,
       "vmsIoInswap": vmsIoInswap,
       "vmsIoFreePageCount": vmsIoFreePageCount,
       "vmsIoModifiedPageCount": vmsIoModifiedPageCount,
       "vmsPage": vmsPage,
       "vmsPageUpdateTime": vmsPageUpdateTime,
       "vmsPageUpdateInterval": vmsPageUpdateInterval,
       "vmsPageFault": vmsPageFault,
       "vmsPageRead": vmsPageRead,
       "vmsPageReadIO": vmsPageReadIO,
       "vmsPageWrite": vmsPageWrite,
       "vmsPageWriteIO": vmsPageWriteIO,
       "vmsPageFreeListFault": vmsPageFreeListFault,
       "vmsPageModListFault": vmsPageModListFault,
       "vmsPageDemandZeroFault": vmsPageDemandZeroFault,
       "vmsPageGlobalValidFault": vmsPageGlobalValidFault,
       "vmsPageWrtInProgressFault": vmsPageWrtInProgressFault,
       "vmsPageSystemFault": vmsPageSystemFault,
       "vmsPageFreePageCount": vmsPageFreePageCount,
       "vmsPageModifiedPageCount": vmsPageModifiedPageCount,
       "vmsDecnet": vmsDecnet,
       "vmsDecnetUpdateTime": vmsDecnetUpdateTime,
       "vmsDecnetUpdateInterval": vmsDecnetUpdateInterval,
       "vmsDecnetArriveLocalPkt": vmsDecnetArriveLocalPkt,
       "vmsDecnetDepartLocalPkt": vmsDecnetDepartLocalPkt,
       "vmsDecnetArriveTransPkt": vmsDecnetArriveTransPkt,
       "vmsDecnetTransCongestLoss": vmsDecnetTransCongestLoss,
       "vmsDecnetReceiveBufFail": vmsDecnetReceiveBufFail,
       "vmsStates": vmsStates,
       "vmsStatesUpdateTime": vmsStatesUpdateTime,
       "vmsStatesUpdateInterval": vmsStatesUpdateInterval,
       "vmsStatesCOLPG": vmsStatesCOLPG,
       "vmsStatesMWAIT": vmsStatesMWAIT,
       "vmsStatesCEF": vmsStatesCEF,
       "vmsStatesPFW": vmsStatesPFW,
       "vmsStatesLEF": vmsStatesLEF,
       "vmsStatesLEFO": vmsStatesLEFO,
       "vmsStatesHIB": vmsStatesHIB,
       "vmsStatesHIBO": vmsStatesHIBO,
       "vmsStatesSUSP": vmsStatesSUSP,
       "vmsStatesSUSPO": vmsStatesSUSPO,
       "vmsStatesFPG": vmsStatesFPG,
       "vmsStatesCOM": vmsStatesCOM,
       "vmsStatesCOMO": vmsStatesCOMO,
       "vmsStatesCUR": vmsStatesCUR,
       "vmsCluster": vmsCluster,
       "vmsClusterUpdateTime": vmsClusterUpdateTime,
       "vmsClusterUpdateInterval": vmsClusterUpdateInterval,
       "vmsClusterCpuBusy": vmsClusterCpuBusy,
       "vmsClusterFreeListSize": vmsClusterFreeListSize,
       "vmsClusterTotalLocks": vmsClusterTotalLocks,
       "vmsClusterNewEnqLocal": vmsClusterNewEnqLocal,
       "vmsClusterNewEnqIncoming": vmsClusterNewEnqIncoming,
       "vmsClusterNewEnqOutgoing": vmsClusterNewEnqOutgoing,
       "vmsClusterEnqConversionsLocal": vmsClusterEnqConversionsLocal,
       "vmsClusterEnqConversionsIncoming": vmsClusterEnqConversionsIncoming,
       "vmsClusterEnqConversionsOutgoing": vmsClusterEnqConversionsOutgoing,
       "vmsClusterDeqLocal": vmsClusterDeqLocal,
       "vmsClusterDeqIncoming": vmsClusterDeqIncoming,
       "vmsClusterDeqOutgoing": vmsClusterDeqOutgoing,
       "vmsMscp": vmsMscp,
       "vmsMscpUpdateTime": vmsMscpUpdateTime,
       "vmsMscpUpdateInterval": vmsMscpUpdateInterval,
       "vmsMscpRequests": vmsMscpRequests,
       "vmsMscpReads": vmsMscpReads,
       "vmsMscpWrites": vmsMscpWrites,
       "vmsMscpFragments": vmsMscpFragments,
       "vmsMscpSplits": vmsMscpSplits,
       "vmsMscpBufferWaits": vmsMscpBufferWaits,
       "vmsMscp1BlockIOs": vmsMscp1BlockIOs,
       "vmsMscp2-3BlockIOs": vmsMscp2_3BlockIOs,
       "vmsMscp4-7BlockIOs": vmsMscp4_7BlockIOs,
       "vmsMscp8-15BlockIOs": vmsMscp8_15BlockIOs,
       "vmsMscp16-31BlockIOs": vmsMscp16_31BlockIOs,
       "vmsMscp32-63BlockIOs": vmsMscp32_63BlockIOs,
       "vmsMscp64andOverBlockIOs": vmsMscp64andOverBlockIOs,
       "vmsLock": vmsLock,
       "vmsLockUpdateTime": vmsLockUpdateTime,
       "vmsLockUpdateInterval": vmsLockUpdateInterval,
       "vmsLockNewEnqs": vmsLockNewEnqs,
       "vmsLockConvertedEnqs": vmsLockConvertedEnqs,
       "vmsLockDeqs": vmsLockDeqs,
       "vmsLockBlockingASTs": vmsLockBlockingASTs,
       "vmsLockEnqWaits": vmsLockEnqWaits,
       "vmsLockEnqsNotQueued": vmsLockEnqsNotQueued,
       "vmsLockDeadlockSearches": vmsLockDeadlockSearches,
       "vmsLockDeadlocksFound": vmsLockDeadlocksFound,
       "vmsLockCurrentLocks": vmsLockCurrentLocks,
       "vmsLockCurrentResources": vmsLockCurrentResources,
       "vmsDlock": vmsDlock,
       "vmsDlockUpdateTime": vmsDlockUpdateTime,
       "vmsDlockUpdateInterval": vmsDlockUpdateInterval,
       "vmsDlockNewLocksLocal": vmsDlockNewLocksLocal,
       "vmsDlockNewLocksIncoming": vmsDlockNewLocksIncoming,
       "vmsDlockNewLocksOutgoing": vmsDlockNewLocksOutgoing,
       "vmsDlockLockConversionsLocal": vmsDlockLockConversionsLocal,
       "vmsDlockLockConversionsIncoming": vmsDlockLockConversionsIncoming,
       "vmsDlockLockConversionsOutgoing": vmsDlockLockConversionsOutgoing,
       "vmsDlockUnlocksLocal": vmsDlockUnlocksLocal,
       "vmsDlockUnlocksIncoming": vmsDlockUnlocksIncoming,
       "vmsDlockUnlocksOutgoing": vmsDlockUnlocksOutgoing,
       "vmsDlockBlockingASTsLocal": vmsDlockBlockingASTsLocal,
       "vmsDlockBlockingASTsIncoming": vmsDlockBlockingASTsIncoming,
       "vmsDlockBlockingASTsOutgoing": vmsDlockBlockingASTsOutgoing,
       "vmsDlockDirFuncIncoming": vmsDlockDirFuncIncoming,
       "vmsDlockDirFuncOutgoing": vmsDlockDirFuncOutgoing,
       "vmsDlockDeadlockMessage": vmsDlockDeadlockMessage,
       "vmsSystem": vmsSystem,
       "vmsSystemUpdateTime": vmsSystemUpdateTime,
       "vmsSystemUpdateInterval": vmsSystemUpdateInterval,
       "vmsSystemCpuBusy": vmsSystemCpuBusy,
       "vmsSystemOtherStates": vmsSystemOtherStates,
       "vmsSystemProcessCount": vmsSystemProcessCount,
       "vmsSystemPageFaults": vmsSystemPageFaults,
       "vmsSystemReadIOs": vmsSystemReadIOs,
       "vmsSystemFreePageCount": vmsSystemFreePageCount,
       "vmsSystemModifiedPageCount": vmsSystemModifiedPageCount,
       "vmsSystemDirectIOs": vmsSystemDirectIOs,
       "vmsSystemBufferedIOs": vmsSystemBufferedIOs}
)
